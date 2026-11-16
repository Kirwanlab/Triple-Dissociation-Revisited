#!/usr/bin/env python3
"""
match_bids_derivatives.py
─────────────────────────────────────────────────────────────────────────────
Match subjects between bids/sub-*/anat/*.json and derivatives/sub-*/**/*.json

Matching key:  AcquisitionTime  +  TxRefAmp
  - AcquisitionTime : exact millisecond timestamp copied from DICOM header —
                      identical in both datasets for the same scan regardless
                      of dcm2niix version or processing pipeline
  - TxRefAmp        : RF amplitude calibrated per-subject tissue load —
                      unique to each individual, confirms the person matches

No third-party packages required — standard library only.
─────────────────────────────────────────────────────────────────────────────
"""

import json
import csv
import argparse
from pathlib import Path
from collections import defaultdict


TX_TOLERANCE = 1.0   # Volts — tighter than before since this should be exact


def parse_acquisition_time(raw: str) -> str:
    """
    Normalise AcquisitionTime to 'HHMMSS' (drop sub-seconds and colons)
    so minor formatting differences between dcm2niix versions don't break
    the match.

    Handles:  '10:16:24.037500'  →  '101624'
              '101624.0375'      →  '101624'
    """
    t = raw.strip().replace(":", "")   # remove colons
    t = t.split(".")[0]                # drop sub-seconds
    return t.zfill(6)                  # ensure HHMMSS


def load_jsons(root: Path, glob_pattern: str, label: str) -> dict[str, dict]:
    """
    Walk *root* with *glob_pattern*.  For each sub-* subject, collect the
    first JSON that contains both AcquisitionTime and TxRefAmp.

    Returns { subject_id: { subject_id, acq_time, tx_ref_amp, json_path } }
    """
    subjects: dict[str, dict] = {}
    all_jsons = sorted(root.glob(glob_pattern))
    print(f"  Found {len(all_jsons)} JSON files in {label}")

    for jf in all_jsons:
        sub = next((p for p in jf.parts if p.startswith("sub-")), None)
        if sub is None:
            continue

        try:
            meta = json.loads(jf.read_text())
        except (json.JSONDecodeError, OSError) as e:
            print(f"  [WARN] Could not read {jf}: {e}")
            continue

        raw_time = meta.get("AcquisitionTime", "")
        tx_ref   = meta.get("TxRefAmp")

        acq_time = parse_acquisition_time(raw_time) if raw_time else None
        tx_ref   = round(float(tx_ref), 3) if tx_ref is not None else None

        if sub not in subjects:
            subjects[sub] = {
                "subject_id": sub,
                "acq_time":   acq_time,
                "tx_ref_amp": tx_ref,
                "json_path":  str(jf),
            }
        else:
            rec = subjects[sub]
            if rec["acq_time"]   is None and acq_time is not None:
                rec["acq_time"]   = acq_time
                rec["json_path"]  = str(jf)
            if rec["tx_ref_amp"] is None and tx_ref is not None:
                rec["tx_ref_amp"] = tx_ref

    print(f"  → {len(subjects)} unique subjects loaded from {label}")
    return subjects


def build_deriv_index(deriv: dict) -> tuple[dict, dict]:
    """
    Build two lookup indexes over derivatives subjects:
        compound_index : (acq_time, tx_rounded) → [dsub, ...]
        time_index     : acq_time               → [dsub, ...]
    """
    compound_index: dict[tuple, list[str]] = defaultdict(list)
    time_index:     dict[str,   list[str]] = defaultdict(list)

    for dsub, ddata in deriv.items():
        t  = ddata["acq_time"]
        tx = ddata["tx_ref_amp"]
        if t:
            time_index[t].append(dsub)
            if tx is not None:
                compound_index[(t, round(tx, 1))].append(dsub)

    return compound_index, time_index


def match_subjects(bids: dict, deriv: dict) -> list[dict]:
    compound_index, time_index = build_deriv_index(deriv)

    results = []

    for bids_sub, bdata in sorted(bids.items()):
        row = {
            "bids_subject":     bids_sub,
            "deriv_subject":    "",
            "match_status":     "",
            "bids_acq_time":    bdata["acq_time"],
            "deriv_acq_time":   "",
            "bids_tx_ref_amp":  bdata["tx_ref_amp"],
            "deriv_tx_ref_amp": "",
            "bids_json":        bdata["json_path"],
            "deriv_json":       "",
            "notes":            "",
        }

        b_time = bdata["acq_time"]
        b_tx   = bdata["tx_ref_amp"]

        # ── Guard: missing AcquisitionTime ────────────────────────────────
        if not b_time:
            row["match_status"] = "NO_TIME"
            row["notes"]        = "AcquisitionTime missing from BIDS sidecar"
            results.append(row)
            continue

        # ── Strategy 1: AcquisitionTime + TxRefAmp compound key ──────────
        matched_dsub   = None
        match_status   = ""

        if b_tx is not None:
            compound_key  = (b_time, round(b_tx, 1))
            compound_hits = compound_index.get(compound_key, [])

            if len(compound_hits) == 1:
                matched_dsub = compound_hits[0]
                match_status = "EXACT"

            elif len(compound_hits) > 1:
                # Tighten TxRefAmp tolerance
                tight = [
                    d for d in compound_hits
                    if deriv[d]["tx_ref_amp"] is not None
                    and abs(deriv[d]["tx_ref_amp"] - b_tx) < TX_TOLERANCE
                ]
                if len(tight) == 1:
                    matched_dsub = tight[0]
                    match_status = "EXACT"
                else:
                    row["match_status"] = "AMBIGUOUS"
                    row["deriv_subject"] = " | ".join(compound_hits)
                    row["notes"] = (
                        f"{len(compound_hits)} derivatives subjects share "
                        "AcquisitionTime+TxRefAmp — manual review needed"
                    )
                    results.append(row)
                    continue

        # ── Strategy 2: AcquisitionTime only (TxRefAmp missing) ──────────
        if matched_dsub is None:
            time_hits = time_index.get(b_time, [])

            if not time_hits:
                row["match_status"] = "NO_MATCH"
                row["notes"]        = "No derivatives subject matched AcquisitionTime"
                results.append(row)
                continue

            elif len(time_hits) == 1:
                matched_dsub = time_hits[0]
                match_status = "TIME_ONLY"
                row["notes"] = "TxRefAmp unavailable for confirmation"

            else:
                # Multiple time hits — try TxRefAmp as tiebreaker
                if b_tx is not None:
                    tx_hits = [
                        d for d in time_hits
                        if deriv[d]["tx_ref_amp"] is not None
                        and abs(deriv[d]["tx_ref_amp"] - b_tx) < TX_TOLERANCE
                    ]
                    if len(tx_hits) == 1:
                        matched_dsub = tx_hits[0]
                        match_status = "EXACT"
                    else:
                        row["match_status"] = "AMBIGUOUS"
                        row["deriv_subject"] = " | ".join(time_hits)
                        row["notes"] = (
                            f"{len(time_hits)} derivatives subjects share "
                            "AcquisitionTime — manual review needed"
                        )
                        results.append(row)
                        continue
                else:
                    row["match_status"] = "AMBIGUOUS"
                    row["deriv_subject"] = " | ".join(time_hits)
                    row["notes"] = (
                        f"{len(time_hits)} candidates share AcquisitionTime "
                        "and TxRefAmp is missing"
                    )
                    results.append(row)
                    continue

        # ── Populate matched fields ────────────────────────────────────────
        ddata = deriv[matched_dsub]
        row["deriv_subject"]    = matched_dsub
        row["deriv_acq_time"]   = ddata["acq_time"]
        row["deriv_tx_ref_amp"] = ddata["tx_ref_amp"]
        row["deriv_json"]       = ddata["json_path"]
        row["match_status"]     = match_status

        results.append(row)

    return results


def print_results(results: list[dict]):
    from collections import Counter
    counts = Counter(r["match_status"] for r in results)

    print("\n" + "═" * 72)
    print("  SUMMARY")
    print("═" * 72)
    print(f"  Total              : {len(results)}")
    print(f"  EXACT              : {counts.get('EXACT',     0)}")
    print(f"  TIME_ONLY          : {counts.get('TIME_ONLY', 0)}")
    print(f"  AMBIGUOUS          : {counts.get('AMBIGUOUS', 0)}")
    print(f"  NO_MATCH           : {counts.get('NO_MATCH',  0)}")
    print(f"  NO_TIME            : {counts.get('NO_TIME',   0)}")
    print("═" * 72)

    col = "{:<18} {:<18} {:<12} {:<10} {:<10} {}"
    print("\n" + col.format(
        "BIDS subject", "Deriv subject", "Status",
        "BIDS_time", "Deriv_time", "Notes"
    ))
    print("  " + "-" * 90)
    for r in results:
        print(col.format(
            r["bids_subject"],
            r["deriv_subject"],
            r["match_status"],
            str(r["bids_acq_time"]),
            str(r["deriv_acq_time"]),
            r["notes"],
        ))
    print()


def save_csv(results: list[dict], output_path: Path):
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)
    print(f"  Saved → {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Match BIDS ↔ derivatives subjects via AcquisitionTime + TxRefAmp."
    )
    parser.add_argument("--bids_dir",        required=True)
    parser.add_argument("--derivatives_dir", required=True)
    parser.add_argument("--output",          default="subject_mapping.csv")
    args = parser.parse_args()

    bids_root  = Path(args.bids_dir)
    deriv_root = Path(args.derivatives_dir)

    if not bids_root.exists():
        raise FileNotFoundError(f"Not found: {bids_root}")
    if not deriv_root.exists():
        raise FileNotFoundError(f"Not found: {deriv_root}")

    print(f"\nLoading BIDS:        {bids_root}")
    bids  = load_jsons(bids_root,  "sub-*/anat/*.json",  "BIDS")

    print(f"\nLoading derivatives: {deriv_root}")
    deriv = load_jsons(deriv_root, "sub-*/**/*.json", "derivatives")

    results = match_subjects(bids, deriv)
    print_results(results)
    save_csv(results, Path(args.output))


if __name__ == "__main__":
    main()