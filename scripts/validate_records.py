#!/usr/bin/env python3
"""Validate every data/records/*.json against schema/document.schema.json.

Usage: python scripts/validate_records.py
Exit code 0 = all records valid. Non-zero = at least one failure (details printed).
"""
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    sys.exit("Missing dependency: pip install jsonschema")

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "document.schema.json"
RECORDS_DIR = ROOT / "data" / "records"


def main():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft7Validator(schema)

    failures = []
    records = sorted(RECORDS_DIR.glob("*.json"))
    if not records:
        print("No records found under data/records/ — nothing to validate.")
        return 0

    for path in records:
        record = json.loads(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(record), key=lambda e: e.path)
        if errors:
            failures.append((path, errors))

    for path, errors in failures:
        print(f"\n[FAIL] {path.relative_to(ROOT)}")
        for err in errors:
            loc = "/".join(str(p) for p in err.path) or "(root)"
            print(f"  - {loc}: {err.message}")

    print(f"\n{len(records) - len(failures)}/{len(records)} records valid.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
