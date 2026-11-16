#!/usr/bin/env python3
"""
fix_duplicate_events.py

Removes duplicate rows from all BIDS *_events.tsv files under a given
BIDS root directory. Preserves row order and keeps the first occurrence
of any repeated row (including any repeated header rows).

Usage:
    python fix_duplicate_events.py /path/to/bids_root

Optional dry-run (preview only, no files written):
    python fix_duplicate_events.py /path/to/bids_root --dry-run
"""

import argparse
import os
from pathlib import Path


def deduplicate_tsv(filepath: Path, dry_run: bool = False) -> dict:
    """
    Remove duplicate lines from a TSV file, keeping the first occurrence
    of every line (including the header).

    Returns a summary dict with keys:
        path, original_rows, final_rows, duplicates_removed, modified
    """
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    seen = set()
    deduplicated = []

    for line in lines:
        # Normalize whitespace for comparison, but write original line
        normalized = line.rstrip("\n").rstrip("\r")
        if normalized not in seen:
            seen.add(normalized)
            deduplicated.append(line)

    original_count = len(lines)
    final_count    = len(deduplicated)
    removed        = original_count - final_count
    modified       = removed > 0

    if modified and not dry_run:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(deduplicated)

    return {
        "path":               filepath,
        "original_rows":      original_count,
        "final_rows":         final_count,
        "duplicates_removed": removed,
        "modified":           modified,
    }


def find_events_files(bids_root: Path) -> list[Path]:
    """
    Recursively find all *_events.tsv files under bids_root,
    skipping hidden directories (e.g. .git) and the BIDS
    derivatives/ folder.
    """
    events_files = []
    for root, dirs, files in os.walk(bids_root):
        # Skip hidden dirs and derivatives in-place
        dirs[:] = [
            d for d in dirs
            if not d.startswith(".")
            and d != "derivatives"
        ]
        for fname in files:
            if fname.endswith("_events.tsv"):
                events_files.append(Path(root) / fname)
    return sorted(events_files)


def main():
    parser = argparse.ArgumentParser(
        description="Remove duplicate rows from BIDS *_events.tsv files."
    )
    parser.add_argument(
        "bids_root",
        type=Path,
        help="Path to the root of your BIDS dataset.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying any files.",
    )
    args = parser.parse_args()

    bids_root = args.bids_root.resolve()
    if not bids_root.is_dir():
        raise SystemExit(f"ERROR: '{bids_root}' is not a directory.")

    events_files = find_events_files(bids_root)
    if not events_files:
        print("No *_events.tsv files found. Check your BIDS root path.")
        return

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Found {len(events_files)} "
          f"events.tsv file(s) under: {bids_root}\n")

    total_removed = 0
    modified_files = 0

    for evfile in events_files:
        result = deduplicate_tsv(evfile, dry_run=args.dry_run)
        status = ""

        if result["modified"]:
            status = (
                f"  ✔  FIXED   — removed {result['duplicates_removed']} "
                f"duplicate row(s)  "
                f"({result['original_rows']} → {result['final_rows']} rows)"
            )
            modified_files += 1
            total_removed  += result["duplicates_removed"]
        else:
            status = f"  –  OK      — no duplicates  ({result['final_rows']} rows)"

        # Print relative path for readability
        try:
            rel = evfile.relative_to(bids_root)
        except ValueError:
            rel = evfile
        print(f"{rel}\n{status}\n")

    # ── Summary ──────────────────────────────────────────────────────────────
    action = "Would modify" if args.dry_run else "Modified"
    print("─" * 60)
    print(f"Summary")
    print(f"  Files scanned  : {len(events_files)}")
    print(f"  {action:<20}: {modified_files}")
    print(f"  Total rows removed: {total_removed}")
    if args.dry_run:
        print("\n  Dry-run complete — no files were changed.")
    print("─" * 60)


if __name__ == "__main__":
    main()