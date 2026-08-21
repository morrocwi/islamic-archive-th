#!/usr/bin/env python3
"""Scaffold: fill/update the `en` block of a record from its `th` block.

STUB — no translation backend wired in yet. Defines the contract:
  1. `th` is always the input; this script never edits `th`.
  2. Every write sets en.translation_status = "machine" (never "reviewed"/"verified"
     from this script — those require a human pass, see docs/PROCESS.md).
  3. Re-running this script on a record whose en.translation_status is already
     "reviewed" or "verified" must be a no-op unless --force is passed, so an
     automated re-run can never silently clobber human-checked translations.

Usage (once implemented):
  python scripts/translate_th_to_en.py data/records/mosque-<slug>-<seq>.json
"""
import argparse
import json
import sys
from pathlib import Path

PROTECTED_STATUSES = {"reviewed", "verified"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record_path", type=Path)
    parser.add_argument("--force", action="store_true",
                         help="Overwrite even a reviewed/verified en block")
    args = parser.parse_args()

    record = json.loads(args.record_path.read_text(encoding="utf-8"))
    current_status = record.get("en", {}).get("translation_status", "missing")

    if current_status in PROTECTED_STATUSES and not args.force:
        sys.exit(
            f"Refusing to overwrite: en.translation_status='{current_status}' "
            f"on {args.record_path}. Pass --force if this is intentional."
        )

    sys.exit(
        "Not implemented: wire in a translation backend here.\n"
        "On success, write record['en'] with translation_status='machine' "
        "and translated_at=<now>, then save back to the same path."
    )


if __name__ == "__main__":
    main()
