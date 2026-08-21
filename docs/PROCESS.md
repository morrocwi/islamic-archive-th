# Ingestion & review process

## 1. Add the source PDF

Drop the original PDF under `sources/pdf/`. Keep the filename traceable to its origin (e.g.
`2559-phra-ratchabanyat-islamic-org-admin.pdf`), never a generic name.

## 2. Extract (Thai only)

Run `scripts/extract_pdf_to_json.py` (once implemented) or extract manually. Fill every `th.*`
field directly from the PDF. Always set:

- `source.document_pdf` — relative path under `sources/pdf/`
- `source.checksum_sha256` — sha256 of the exact PDF used
- `source.retrieved_date` — today
- `provenance.extraction_method` — `manual` / `ocr` / `pdf-text` / `mixed`, truthfully
- `provenance.verified = false` — until step 4

`th.summary` is a rewritten summary of the document, not a copy-paste of the operative text.

## 3. Translate

Run `scripts/translate_th_to_en.py` (once a translation backend is wired in). It writes `en.*`
with `translation_status = "machine"`. It refuses to touch a record whose `translation_status`
is already `reviewed` or `verified` unless `--force` is passed.

## 4. Human review (required before `verified: true`)

A human checks the `th` block against the PDF page-by-page (`source.page_ref`), and — separately —
a person fluent in both legal Thai and English checks the `en` block against `th`. Only then:

- `provenance.verified = true`, `provenance.verified_by`, `provenance.verified_at`
- `en.translation_status = "reviewed"` (a second bilingual legal reviewer bumps it to `verified`)

## 5. Validate

`python scripts/validate_records.py` must pass before committing.
