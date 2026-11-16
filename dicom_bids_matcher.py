#!/usr/bin/env python3
"""
dicom_bids_matcher.py
─────────────────────────────────────────────────────────────────────────────
Match DICOM studies to BIDS subjects using subject-specific scanner
calibration values written into every Siemens DICOM:

  • ShimSetting  – 8 gradient shim offsets calibrated per-subject (PRIMARY)
  • TxRefAmp     – transmitter reference amplitude, also per-subject (CONFIRM)

Both values are extracted from the Siemens MrPhoenixProtocol private block
(DICOM tag 0029,1020) — the same source dcm2niix uses to populate the BIDS
JSON sidecars — so matching is exact with no fuzzy logic needed.

Requirements:
    pip install pydicom pandas tqdm colorama
─────────────────────────────────────────────────────────────────────────────
"""

import re
import json
import argparse
from pathlib import Path
from collections import defaultdict

import pandas as pd
import pydicom
from tqdm import tqdm
from colorama import Fore, Style, init as colorama_init

colorama_init(autoreset=True)

# ── How many DICOM files to sample per directory (one is usually enough) ──
DICOM_SAMPLE_PER_DIR = 3


# ═══════════════════════════════════════════════════════════════════════════
#  SIEMENS MrPhoenixProtocol PARSER
# ═══════════════════════════════════════════════════════════════════════════

def parse_phoenix_protocol(ds: pydicom.Dataset) -> tuple[list[int] | None, float | None]:
    """
    Read the Siemens MrPhoenixProtocol ASCII block from DICOM tag (0029,1020)
    and extract:
        • ShimSetting  – list of 8 integers  (sGRADSPEC.asArray[n].lOffset)
        • TxRefAmp     – float               (sTXSPEC…flReferenceAmplitude)

    Returns (None, None) if the tag is absent or unparseable.
    """
    try:
        raw = ds[0x0029, 0x1020].value
    except KeyError:
        return None, None

    # The tag is a binary blob; the human-readable ASCCONV section is delimited
    if isinstance(raw, bytes):
        start = raw.find(b"### ASCCONV BEGIN")
        end   = raw.find(b"### ASCCONV END ###")
        if start == -1 or end == -1:
            return None, None
        text = raw[start:end].decode("latin-1", errors="replace")
    else:
        text = str(raw)

    # ── ShimSetting ────────────────────────────────────────────────────────
    # sGRADSPEC.asArray[0].lOffset  =  -2768
    shim = []
    for i in range(8):
        m = re.search(
            rf"sGRADSPEC\.asArray\[{i}\]\.lOffset\s*=\s*(-?\d+)", text
        )
        shim.append(int(m.group(1)) if m else None)

    shim_clean = shim if all(v is not None for v in shim) else None

    # ── TxRefAmp ──────────────────────────────────────────────────────────
    # sTXSPEC.asNucleusInfo[0].flReferenceAmplitude  =  358.200012
    m_tx = re.search(
        r"sTXSPEC\.asNucleusInfo\[0\]\.flReferenceAmplitude\s*=\s*([\d.]+)", text
    )
    tx_ref = round(float(m_tx.group(1)), 2) if m_tx else None

    return shim_clean, tx_ref


# ═══════════════════════════════════════════════════════════════════════════
#  EXTRACT METADATA FROM DICOM TREE
# ═══════════════════════════════════════════════════════════════════════════

def extract_dicom_metadata(dcm_root: Path) -> pd.DataFrame:
    """
    Walk *dcm_root* recursively, sample DICOM files, and return one row per
    unique StudyInstanceUID containing ShimSetting, TxRefAmp, and basic IDs.
    """
    print(f"\n{Fore.CYAN}── Scanning DICOM tree: {dcm_root}{Style.RESET_ALL}")

    # Group files by parent directory (≈ one series per folder)
    dir_files: dict[Path, list[Path]] = defaultdict(list)
    for f in dcm_root.rglob("*"):
        if f.is_file() and f.suffix.lower() in (".dcm", ""):
            dir_files[f.parent].append(f)

    seen: dict[str, dict] = {}   # keyed by StudyInstanceUID

    for folder, files in tqdm(dir_files.items(), desc="DICOM dirs", unit="dir"):
        for fpath in sorted(files)[:DICOM_SAMPLE_PER_DIR]:
            try:
                ds = pydicom.dcmread(str(fpath), stop_before_pixels=True, force=True)
            except Exception:
                continue

            def tag(t, default=""):
                try:
                    return str(ds[t].value).strip()
                except KeyError:
                    return default

            study_uid = tag((0x0020, 0x000D))
            if not study_uid:
                continue

            shim, tx_ref = parse_phoenix_protocol(ds)

            if study_uid not in seen:
                seen[study_uid] = {
                    "dcm_study_uid":    study_uid,
                    "dcm_patient_id":   tag((0x0010, 0x0020)),
                    "dcm_patient_name": tag((0x0010, 0x0010)),
                    "dcm_study_date":   tag((0x0008, 0x0020)),
                    "dcm_shim":         shim,
                    "dcm_tx_ref_amp":   tx_ref,
                    "dcm_source_dir":   str(folder),
                }
            else:
                # Fill in calibration values if we found them in a later file
                rec = seen[study_uid]
                if rec["dcm_shim"] is None and shim is not None:
                    rec["dcm_shim"] = shim
                if rec["dcm_tx_ref_amp"] is None and tx_ref is not None:
                    rec["dcm_tx_ref_amp"] = tx_ref

    records = list(seen.values())
    df = pd.DataFrame(records)
    print(f"  → Found {len(df)} unique DICOM studies")
    return df


# ═══════════════════════════════════════════════════════════════════════════
#  EXTRACT METADATA FROM BIDS JSON SIDECARS
# ═══════════════════════════════════════════════════════════════════════════

def extract_bids_metadata(bids_root: Path) -> pd.DataFrame:
    """
    Walk *bids_root* and read all JSON sidecars inside sub-* directories.
    Returns one row per unique (subject, session) pair with the first
    ShimSetting and TxRefAmp found.
    """
    print(f"\n{Fore.CYAN}── Scanning BIDS tree: {bids_root}{Style.RESET_ALL}")

    sub_session: dict[tuple, dict] = {}

    for jf in tqdm(sorted(bids_root.rglob("*.json")), desc="BIDS JSONs", unit="file"):
        parts = jf.parts
        sub = next((p for p in parts if p.startswith("sub-")), None)
        if sub is None:
            continue
        ses = next((p for p in parts if p.startswith("ses-")), "")
        key = (sub, ses)

        try:
            meta = json.loads(jf.read_text())
        except (json.JSONDecodeError, OSError):
            continue

        shim   = meta.get("ShimSetting")        # list of 8 ints
        tx_ref = meta.get("TxRefAmp")            # float
        if tx_ref is not None:
            tx_ref = round(float(tx_ref), 2)

        if key not in sub_session:
            sub_session[key] = {
                "bids_subject":  sub,
                "bids_session":  ses,
                "bids_shim":     shim,
                "bids_tx_ref_amp": tx_ref,
                "bids_json_example": str(jf),
            }
        else:
            rec = sub_session[key]
            if rec["bids_shim"] is None and shim is not None:
                rec["bids_shim"] = shim
            if rec["bids_tx_ref_amp"] is None and tx_ref is not None:
                rec["bids_tx_ref_amp"] = tx_ref

    df = pd.DataFrame(list(sub_session.values()))
    print(f"  → Found {len(df)} unique BIDS subject/sessions")
    return df


# ═══════════════════════════════════════════════════════════════════════════
#  MATCHING ENGINE
# ═══════════════════════════════════════════════════════════════════════════

def match(bids_df: pd.DataFrame, dcm_df: pd.DataFrame) -> pd.DataFrame:
    """
    For every BIDS subject/session, find the DICOM study whose ShimSetting
    matches exactly.  TxRefAmp is used as a confirmation check.

    match_status values:
        EXACT      – ShimSetting matched AND TxRefAmp confirmed
        SHIM_ONLY  – ShimSetting matched but TxRefAmp missing/mismatch
        NO_MATCH   – no DICOM study shared the same ShimSetting
        NO_SHIM    – BIDS sidecar had no ShimSetting to match on
    """
    print(f"\n{Fore.CYAN}── Matching …{Style.RESET_ALL}")
    rows = []

    for _, brow in bids_df.iterrows():
        bids_shim  = brow["bids_shim"]
        bids_tx    = brow["bids_tx_ref_amp"]

        result = {
            "bids_subject":        brow["bids_subject"],
            "bids_session":        brow["bids_session"],
            "bids_shim":           str(bids_shim),
            "bids_tx_ref_amp":     bids_tx,
            "dcm_study_uid":       "",
            "dcm_patient_id":      "",
            "dcm_patient_name":    "",
            "dcm_study_date":      "",
            "dcm_shim":            "",
            "dcm_tx_ref_amp":      "",
            "dcm_source_dir":      "",
            "match_status":        "",
            "match_notes":         "",
        }

        if bids_shim is None:
            result["match_status"] = "NO_SHIM"
            result["match_notes"]  = "ShimSetting absent from BIDS sidecars"
            rows.append(result)
            continue

        # ── Find DICOM rows whose ShimSetting equals bids_shim ────────────
        matches = dcm_df[
            dcm_df["dcm_shim"].apply(lambda s: s == bids_shim if s is not None else False)
        ]

        if matches.empty:
            result["match_status"] = "NO_MATCH"
            result["match_notes"]  = "No DICOM study matched ShimSetting"
            rows.append(result)
            continue

        if len(matches) > 1:
            result["match_notes"] = (
                f"WARNING: {len(matches)} DICOM studies share this ShimSetting — "
                "using first; inspect manually"
            )

        best = matches.iloc[0]

        # Populate DICOM fields
        result["dcm_study_uid"]    = best["dcm_study_uid"]
        result["dcm_patient_id"]   = best["dcm_patient_id"]
        result["dcm_patient_name"] = best["dcm_patient_name"]
        result["dcm_study_date"]   = best["dcm_study_date"]
        result["dcm_shim"]         = str(best["dcm_shim"])
        result["dcm_tx_ref_amp"]   = best["dcm_tx_ref_amp"]
        result["dcm_source_dir"]   = best["dcm_source_dir"]

        # Confirm with TxRefAmp
        dcm_tx = best["dcm_tx_ref_amp"]
        if bids_tx is not None and dcm_tx is not None:
            if abs(bids_tx - dcm_tx) < 0.5:          # <0.5 V tolerance
                result["match_status"] = "EXACT"
            else:
                result["match_status"] = "SHIM_ONLY"
                result["match_notes"] += (
                    f" TxRefAmp mismatch: BIDS={bids_tx} vs DCM={dcm_tx}"
                )
        else:
            result["match_status"] = "SHIM_ONLY"
            result["match_notes"] += " TxRefAmp not available for confirmation"

        rows.append(result)

    return pd.DataFrame(rows)


# ═══════════════════════════════════════════════════════════════════════════
#  SUMMARY PRINTER
# ═══════════════════════════════════════════════════════════════════════════

def print_summary(df: pd.DataFrame):
    counts = df["match_status"].value_counts()
    total  = len(df)

    print(f"\n{Fore.GREEN}╔══ MATCHING SUMMARY {'═'*38}")
    print(f"║  Total BIDS subjects/sessions  : {total}")
    print(f"║  EXACT  (shim + TxRefAmp)      : "
          f"{Fore.GREEN}{counts.get('EXACT',0)}{Style.RESET_ALL}")
    print(f"║  SHIM_ONLY (shim matched only) : "
          f"{Fore.YELLOW}{counts.get('SHIM_ONLY',0)}{Style.RESET_ALL}")
    print(f"║  NO_MATCH                      : "
          f"{Fore.RED}{counts.get('NO_MATCH',0)}{Style.RESET_ALL}")
    print(f"║  NO_SHIM  (missing in BIDS)    : "
          f"{Fore.RED}{counts.get('NO_SHIM',0)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}╚{'═'*56}{Style.RESET_ALL}\n")

    print(df[[
        "bids_subject", "bids_session",
        "dcm_patient_id", "dcm_patient_name",
        "dcm_study_date", "match_status", "match_notes"
    ]].to_string(index=False))


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Match DICOM studies to BIDS subjects via ShimSetting + TxRefAmp "
            "extracted from the Siemens MrPhoenixProtocol."
        )
    )
    parser.add_argument("--dicom_dir", required=True,
                        help="Root directory of raw DICOM files")
    parser.add_argument("--bids_dir",  required=True,
                        help="Root directory of BIDS dataset")
    parser.add_argument("--output",    default="dicom_bids_match.csv",
                        help="Output CSV path  (default: dicom_bids_match.csv)")
    parser.add_argument("--dump_dicom_meta", default="",
                        help="Optional: save raw DICOM metadata table here")
    parser.add_argument("--dump_bids_meta",  default="",
                        help="Optional: save raw BIDS metadata table here")
    args = parser.parse_args()

    bids_root = Path(args.bids_dir)
    dcm_root  = Path(args.dicom_dir)

    if not bids_root.exists():
        raise FileNotFoundError(f"BIDS directory not found: {bids_root}")
    if not dcm_root.exists():
        raise FileNotFoundError(f"DICOM directory not found: {dcm_root}")

    bids_df = extract_bids_metadata(bids_root)
    dcm_df  = extract_dicom_metadata(dcm_root)

    if args.dump_bids_meta:
        bids_df.to_csv(args.dump_bids_meta, index=False)
        print(f"  Saved BIDS metadata  → {args.dump_bids_meta}")
    if args.dump_dicom_meta:
        dcm_df.to_csv(args.dump_dicom_meta, index=False)
        print(f"  Saved DICOM metadata → {args.dump_dicom_meta}")

    matched_df = match(bids_df, dcm_df)
    matched_df.to_csv(args.output, index=False)
    print(f"\n{Fore.GREEN}✔  Results saved → {args.output}{Style.RESET_ALL}")
    print_summary(matched_df)


if __name__ == "__main__":
    main()