#!/usr/bin/env python3
"""Scaffold: pull one document record out of a source PDF into a data/records/*.json file.

This is a STUB — it defines the pipeline contract, not a working OCR/parser yet.
Wire in a real PDF-to-text step (e.g. pdfplumber for born-digital PDFs like
ราชกิจจานุเบกษา releases, or an OCR pass for scanned circulars/older documents)
once the first real source PDF is available under sources/pdf/.

Scope: laws (พ.ร.บ.), ministerial regulations, provincial Islamic-committee
rules, administrative circulars, and research/guideline papers on mosque
administration in Thailand — see schema/document.schema.json `th.category`.

Contract this script must uphold, per schema/document.schema.json:
  1. Never write an `en` block from this script — extraction is Thai-only.
     `en` is filled in later by translate_th_to_en.py, and stays paired to `th`.
  2. Always fill `source.document_pdf` with the relative path under sources/pdf/,
     and `source.checksum_sha256` with the sha256 of that exact file, so a later
     edit to the source PDF is detectable.
  3. Always set provenance.extraction_method truthfully (manual/ocr/pdf-text/mixed)
     and provenance.verified = false until a human checks it against the PDF.
  4. `th.summary` must be a rewritten summary, never a verbatim copy of the
     operative legal text — copy only into page_ref-cited quotes if needed.

Usage (once implemented):
  python scripts/extract_pdf_to_json.py sources/pdf/<file>.pdf --category law
"""
import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES = ["law", "regulation", "circular", "guideline", "research", "other"]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def next_seq(category: str) -> str:
    existing = sorted((ROOT / "data" / "records").glob(f"doc-{category}-*.json"))
    n = len(existing) + 1
    return f"{n:04d}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf_path", type=Path, help="Path to the source PDF under sources/pdf/")
    parser.add_argument("--category", required=True, choices=CATEGORIES)
    args = parser.parse_args()

    if not args.pdf_path.exists():
        sys.exit(f"PDF not found: {args.pdf_path}")

    sys.exit(
        "Not implemented: this stub only computes the checksum + next id.\n"
        "Wire in real text/OCR extraction, fill th.* fields, then write to\n"
        f"data/records/doc-{args.category}-{next_seq(args.category)}.json\n"
        f"checksum_sha256 would be: {sha256_of(args.pdf_path)}\n"
        f"retrieved_date would default to: {date.today().isoformat()}"
    )


if __name__ == "__main__":
    main()
