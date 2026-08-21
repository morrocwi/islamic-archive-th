# Thai Mosque Governance Archive

ฐานข้อมูลเอกสารการบริหารกิจการมัสยิดในประเทศไทย — พระราชบัญญัติ กฎกระทรวง ระเบียบคณะกรรมการอิสลามประจำจังหวัด
หนังสือเวียน และแนวทาง/งานวิจัยด้านการบริหารมัสยิด — ทุกเรคคอร์ดผูกกับไฟล์ PDF ต้นฉบับและลิงก์แหล่งที่มาเสมอ

A structured, source-traceable database of laws, regulations, circulars, and research/guideline
documents on **mosque administration and governance in Thailand**. Every record links back to its
original PDF and source URL — nothing is entered without a retrievable original.

## หลักการ / Design principles

- **ภาษาไทยคือต้นฉบับ (Thai is the source of truth).** ทุกเรคคอร์ดถูกป้อน/ตรวจสอบเป็นภาษาไทยก่อนเสมอ
  ตรงกับเอกสารต้นฉบับ 100% ก่อนจะมีการแปล
- **English is a translation pair, never an independent entry.** The `en` block is always derived
  from `th` and carries `translation_status` (`missing` → `machine` → `reviewed` → `verified`).
  A translation status of `reviewed`/`verified` is protected — the translation pipeline will not
  silently overwrite it (see `scripts/translate_th_to_en.py`).
- **Readout, not truth.** Every record is a retained readout of one specific PDF at one retrieval
  date (`source.retrieved_date`, `source.checksum_sha256`). A law's real-world status can change;
  `th.status` reflects what was verified as of this record, not an assumed current state.
- **No record without a source.** `source.document_pdf` and/or `source.document_url` are required —
  a summary with no traceable original is not accepted into this archive.

## โครงสร้าง / Structure

```
schema/document.schema.json   JSON Schema — the canonical shape of one record
data/records/*.json           One JSON file per document (th + en pair + source + provenance)
sources/pdf/                  Original PDF files, referenced by data/records/*.json
scripts/
  extract_pdf_to_json.py      Stub: PDF → data/records/*.json (Thai-only extraction)
  translate_th_to_en.py       Stub: fills/updates the en block from th
  validate_records.py         Validates every record against the schema
docs/PROCESS.md               Human review workflow (extraction → translation → verification)
```

## Categories (`th.category`)

| category | ตัวอย่าง |
|---|---|
| `law` | พระราชบัญญัติ เช่น พ.ร.บ.การบริหารองค์กรศาสนาอิสลาม |
| `regulation` | กฎกระทรวง / ระเบียบ / ประกาศ |
| `circular` | หนังสือเวียน / คำสั่ง |
| `guideline` | แนวทางบริหาร / คู่มือ |
| `research` | งานวิจัย / บทความวิชาการที่เกี่ยวข้อง |
| `other` | อื่นๆ |

## Running the validator

```bash
pip install jsonschema
python scripts/validate_records.py
```

## Status

Scaffold only — schema and pipeline contracts are in place; `data/records/` currently holds one
placeholder (`doc-law-example-0001.json`) for testing. Real ingestion starts once the first source
PDFs are supplied.
