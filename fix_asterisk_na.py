#!/usr/bin/env python3
"""
fix_asterisk_na.py

Replaces all "*" cell values with "n/a" in every BIDS *_events.tsv
file found under a given BIDS root directory.

Usage:
    python fix_asterisk_na.py /path/to/bids_root

Optional dry-run (preview only, no files written):
    python fix_asterisk_na.py /path/to/bids_root --dry-run
"""

import argparse
import csv
import io
import os
from pathlib import Path


def fix_asterisks(filepath: Path, dry_run: bool = False) -> dict:
    """
    Replace every cell value of exactly "*" with "n/a" in a TSV file.

    Returns a summary dict with keys:
        path, rows_affected, cells_replaced, modified
    """
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        content = f.read()

    reader = csv.reader(io.StringIO(content), delimiter="\t")
    rows = list(reader)

    cells_replaced = 0
    rows_affected  = set()
    fixed_rows     = []

    for i, row in enumerate(rows):
        new_row = []
        for cell in row:
            if cell == "*":
                new_row.append("n/a")
                cells_replaced += 1
                rows_affected.add(i)
            else:
                new_row.append(cell)
        fixed_rows.append(new_row)

    modified = cells_replaced > 0

    if modified and not dry_run:
        with open(filepath, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter="\t", lineterminator="\n")
            writer.writerows(fixed_rows)

    return {
        "path":           filepath,
        "rows_affected":  len(rows_affected),
        "cells_replaced": cells_replaced,
        "modified":       modified,
    }


def find_events_files(bids_root: Path) -> list[Path]:
    """
    Recursively find all *_events.tsv files under bids_root,
    skipping hidden directories and derivatives/.
    """
    events_files = []
    for root, dirs, files in os.walk(bids_root):
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
        description='Replace "*" cell values with "n/a" in BIDS *_events.tsv files.'
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

    total_cells    = 0
    modified_files = 0

    for evfile in events_files:
        result = fix_asterisks(evfile, dry_run=args.dry_run)

        try:
            rel = evfile.relative_to(bids_root)
        except ValueError:
            rel = evfile

        if result["modified"]:
            status = (
                f"  ✔  FIXED   — replaced {result['cells_replaced']} "
                f"\"*\" cell(s) across {result['rows_affected']} row(s)"
            )
            modified_files += 1
            total_cells    += result["cells_replaced"]
        else:
            status = "  –  OK      — no \"*\" values found"

        print(f"{rel}\n{status}\n")

    # ── Summary ───────────────────────────────────────────────────────────────
    action = "Would modify" if args.dry_run else "Modified"
    print("─" * 60)
    print("Summary")
    print(f"  Files scanned      : {len(events_files)}")
    print(f"  {action:<21}: {modified_files}")
    print(f"  Total cells fixed  : {total_cells}")
    if args.dry_run:
        print("\n  Dry-run complete — no files were changed.")
    print("─" * 60)


if __name__ == "__main__":
    main()