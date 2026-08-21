# Islamic Archive TH

> **โปรเจกต์อิสระ ไม่ใช่หน่วยงานราชการ และไม่ได้เป็นส่วนหนึ่งของสำนักจุฬาราชมนตรีหรือ CICOT** — เป็นการ
> รวบรวมเอกสารสาธารณะมาจัดระบบ ไม่ใช่แหล่งข้อมูลทางการขององค์กรใด
>
> **Independent project — not a government agency, and not affiliated with the Office of the
> Chularajmontri or CICOT.** This is a community effort to organize publicly available documents;
> it is not an official source for any organization.
>
> **โปรดตรวจสอบข้อมูลกับต้นฉบับทางการด้วยตนเองทุกครั้งก่อนนำไปใช้อ้างอิง — ใช้ข้อมูลนี้ด้วยความเสี่ยงของ
> ผู้ใช้เอง ผู้จัดทำไม่รับผิดชอบต่อความเสียหายใดๆ ทั้งสิ้น** อ่านรายละเอียดเต็มที่ [`DISCLAIMER.md`](DISCLAIMER.md)
>
> **Always verify against the official original before relying on any information here — use at
> your own risk; the maintainers accept no liability.** Full text: [`DISCLAIMER.md`](DISCLAIMER.md)

ฐานข้อมูลเอกสารการบริหารองค์กรศาสนาอิสลามทั้งระบบในประเทศไทย — ตั้งแต่สำนักจุฬาราชมนตรี คณะกรรมการอิสลาม
ประจำจังหวัด ไปจนถึงมัสยิดแต่ละแห่ง — พระราชบัญญัติ กฎกระทรวง ระเบียบ หนังสือเวียน และแนวทาง/งานวิจัยด้าน
การบริหาร — ทุกเรคคอร์ดผูกกับไฟล์ PDF ต้นฉบับและลิงก์แหล่งที่มาเสมอ เพื่อให้ทั้งประชาชนทั่วไปและผู้บริหาร
องค์กร/มัสยิดเข้าถึงข้อมูลได้อย่างเป็นระบบ

A structured, source-traceable database of laws, regulations, circulars, and research/guideline
documents covering the **administration of Islamic organizations in Thailand as a whole** — the
Office of the Chularajmontri (Sheikhul Islam), Central and Provincial Islamic Committees, and
individual mosques. Every record links back to its original PDF and source URL — nothing is
entered without a retrievable original. Built for both the general public and mosque/organization
administrators to access this information systematically.

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
schema/document.schema.json        JSON Schema — the canonical shape of one record
data/records/*.json                One JSON file per document (th + en pair + source + provenance)
sources/originals/                 Original files (PDF, or native .doc/.docx for blank forms), referenced by data/records/*.json
scripts/
  extract_pdf_to_json.py           Stub: PDF → data/records/*.json (Thai-only extraction)
  translate_th_to_en.py            Stub: fills/updates the en block from th
  validate_records.py              Validates every record against the schema
docs/PROCESS.md                    Human review workflow (extraction → translation → verification)
docs/DOCUMENT_MAP.md               Backlog: which laws/regulations/forms are found vs. still pending
docs/MOSQUE_ADMIN_FRAMEWORK.md     5-dimension organizing framework for mosque administration topics
docs/CICOT_STRUCTURE.md            CICOT's legal status, institutional DAG, and department functions
docs/RELATED_ORGANIZATIONS.md       Semi-private associations/foundations that interface with state agencies
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
