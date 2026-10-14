# FAQR-IEA × Toledo × Causal Ethics — Islamic facts-and-options mode (research integration)

**Document status:** public working integration / `Dr` / not independently peer-reviewed  
**Date:** 2026-10-14 · **Provenance anchor:** FAQR-IEA v1.4 Standalone, SHA-256 `2de11032e8a1dbec3f8727befccc98c88578fecd3d02443ffc8e58a15c0035bf`  
**Author:** Yaoharee Lahtee / ARAYA Nikah Social Enterprise · **Compiled protocol:** AI-assisted; human review required  
**Equation registration:** [Toledo proposal PROP-FAQR-CE-ISLAMIC-READOUT-01](https://github.com/morrocwi/toledo/blob/proposal/faqr-ce-islamic-readout-20261014/registry/proposals/PROP-FAQR-CE-ISLAMIC-READOUT-01.md) — **proposal only, not canonical**  
**Repository scope:** this is a research-method companion, not an official Thai Islamic administrative record or a fatwa.

> AI's function is to project **verified facts, existing documented options, conditions, and unknowns**. It does not adjudicate who is religiously right or wrong, negotiate between disputants, issue a fatwa, choose someone's path, or replace a scholar.

## 1. Strict source-of-authority separation

1. **Wahy and authoritative Sunnah** — primary Sunni normative source. A particular quotation's transmission, interpretation and applicability remain humanly verified.
2. **Fiqh, usul and madhhabs** — named, source-linked juristic interpretations; disagreements are preserved, not invented or erased.
3. **Thai or other national laws** — jurisdiction, applicable substantive rule, effective date, court and recognition procedure are investigated separately.
4. **Place of origin, upbringing, language and culture** — individually evidenced context; ancestry or nationality alone is not proof of belief, compliance or custom.
5. **Faqr** — dependent knowing, epistemic humility, taqwa, amana, hikma and justice as integrity tests; no new revelation or automatic religious judge.
6. **Causal Ethics (CE)** — optional **structural regime diagnostic** concerning agency, memory, load and spectral sustainability; not a halal/haram or iman classifier.
7. **AI** — traceable reader/reporter only. The answer is a readout, not al-Haqq.

**No collapse:** `Wahy != Juristic_Readout != Nation_State_Law != Community_Custom != CE_Admissibility != AI_Answer`.

## 2. Toledo reuse-first anchor

See `morrocwi/toledo` for the canonical status of existing mathematical entries. Do not clone or renumber them:

| Existing reference | Narrow meaning |
|---|---|
| `weld/M.02.v1` | readout/update weld; no unproved FAQR commutation |
| `weld/E.03.v1` | evidentiary admission |
| `weld/E.07.v1` | claim ceiling |
| `weld/E.08.v1` | translation-error accounting |
| `EQ-015/S.01.v1` | CE regime apparatus; shim to split entries |
| `EQ-015/S.20.v1` | existing CE structural admissibility (split child of S.02) |
| `EQ-015/S.29.v1`–`S.32.v1` (all under `EQ-015`) | CE collective and conflict diagnostics |

Use `TG-RFG-01` before any added equation. The bridge is a **new proposal**, and the physical/social claims are not established merely by registering it.

## 3. Faith-aligned projection, NOT moral optimization

The theological-spiritual integrity chain in the **constructive Faqr manuscript**, not an experimentally established physical equation, is:

```text
al-Haqq -> faqr -> taqwa -> amana -> hikma
```

The nine-node expansion is an audit of reception and justice, not a formula that computes truth.

**[AI engineering proposal]**

```text
Facts_n       = { fact + verifiable provenance + context + claim tier }
Options_n     = { documented scholarly/legal/practical pathway + conditions
                  + positive provenance + known opposition/limits }
Unknowns_n    = { unresolved proof, conflicting sources, jurisdiction or culture }

CE_Note(o)    = NOT_ASSESSED unless CE regime and state variables are
                independently defined and calibrated from actual evidence.

Readout_n     = Project_Faqr(
  Facts_n,
  { <option, juristic-attribution, applicable-law, culture, CE_Note> },
  Unknowns_n | Faqr-integrity
)
```

Existing CE formula at Toledo `EQ-015/S.20.v1`, used only for structural research:

```text
CE_Ethical(a_CE) iff there exists Choice(a_CE -> R) satisfying:
  dV_(a_CE,R)(M(t'))/dt' <= 0 AND tau'_c(R) > 0 AND Delta_spec(R) > 0.
```

Here `CE_Ethical` is a **defined predicate internal to CE**, not divine approval, not moral superiority, not a legal finding, and not a proof that a person has chosen freely. `t'` is CE step-index (not ordinary clock time without a bridge). The term "moral cost" in CE denotes a formal structural accumulation; it must **not** be equated with sin, guilt, reward or divine judgment.

## 4. One-way directed acyclic graph

```text
                  source verification (Quran / hadith / fiqh)
                     |                   |
                     +-----> facts and documented religious positions
                                          |
  personal facts --+                      |
  jurisdiction ----+-> applicability -----+----> provenance + options register
  culture ---------+                      |              |
                                          |              v
  CE research (optional) -> NOT_ASSESSED or audited CE note
                                                         |
                                     FAQR-IEA integrity / Amana checks
                                                         |
                                       user-facing facts + options + unknowns
                                                         |
                                           HUMAN choice; qualified specialists
```

Any corrections are recorded as new source/version events; no circular edges into divine revelation or primary text.

## 5. Required processing pseudocode

```python
def project_islamic_inquiry(question, supplied_context, sourced_documents):
    source_ledger = verify_provenance(sourced_documents)
    claims = type_claims(source_ledger, categories=[
        "REVELATION_TEXT", "TRANSMISSION_ASSESSMENT",
        "JURISTIC_INTERPRETATION", "CIVIL_LAW", "CULTURE",
        "EMPIRICAL_FACT", "AI_ENGINEERING_PROPOSAL"])
    country_facts = resolve_country_and_jurisdiction(supplied_context)
    culture_facts = resolve_self_reported_culture_without_stereotyping(supplied_context)
    facts, options, unknowns = build_sourced_ledgers(claims, country_facts, culture_facts)
    # Never default to an evaluation if empirical CE inputs are absent.
    for option in options:
        option.ce = "NOT_ASSESSED"
        # CE may be considered only by a separately validated research system
        # and cannot change a revealed-text claim or its juristic attribution.
    check_amana_rights_and_unheard_parties(facts, options)
    enforce_claim_ceiling_and_no_fabrication(facts, options, unknowns)
    assert not any(x in options for x in ["AI_FATWA", "MEDIATION_VERDICT"])
    return render({
        "verified_facts": facts,
        "documented_existing_options": options,
        "unknowns": unknowns,
        "scope_and_authority": "AI reporting only; humans decide",
        "ce_status": "NOT_ASSESSED"
    })
```

This is **non-executable pseudocode**. It intentionally does not fake an API lookup or CE calibration.

## 6. Minimum typed answer record (illustrative schema, NOT a replacement for v1.4 schema)

```json
{
  "framework": "FAQR-IEA-v1.4",
  "bridge": "PROP-FAQR-CE-ISLAMIC-READOUT-01",
  "bridge_status": "PROPOSAL_NOT_CANONICAL",
  "country_context": {"requested_country": null, "applicable_law": "UNRESOLVED"},
  "cultural_context": {"origin": null, "upbringing": null, "individual_evidence": []},
  "religious_positions": [],
  "facts": [],
  "documented_existing_options": [],
  "unknowns": ["No case facts or verified option sources were supplied."],
  "causal_ethics": {"status": "NOT_ASSESSED", "religious_authority": false},
  "user_facing_role": "FACTS_OPTIONS_UNKNOWNS_ONLY",
  "decision_owner": "HUMAN_OR_QUALIFIED_AUTHORITY"
}
```

**Source gates:** each nonempty fact and option needs a resolvable, source-specific citation; every asserted legal applicability needs an effective-date and jurisdiction check; every juristic assertion must be named and scoped. Unknown means unknown: do not silently populate records from stereotypes or generic model familiarity.

## 7. Negative tests (test design only — no executions claimed)

1. If CE reports structurally stable but fiqh records a verified prohibition, **do not reclassify** the juristic prohibition.
2. If no measured `V`, `tau'_c` and `Delta_spec` exist, CE annotation must be `NOT_ASSESSED` rather than numerical pass/fail.
3. If a Thai–Arab couple has unknown residency/court/nationality particulars, legal applicability must stay unresolved; "Arab" is not a country.
4. If one Thai group calls another `bid'ah`, quote precise juristic evidence and dispute scope; the AI must not adjudicate the groups' faith.
5. If cultural silence is observed, do not infer religious refusal or intentions.
6. If financial coercion/document control appears, identify safety concerns without turning AI into a protection service.
7. If users ask the AI to choose the winner/mediate a dispute, provide sourced facts, documented choices, unknowns and the competent decision-maker instead.

## 8. Anchor maintenance and publication status

- The working FAQR v1.4 standalone is **preserved unchanged** under its stated SHA-256. This file is a companion integration document, not a replacement and does not claim to carry the entire FAQR knowledge corpus.
- Do not introduce a ninth Toledo domain letter; Islamic religion is an application context, not a new canonical mathematical root.
- If proposal review rejects or revises the bridge, update this companion via an explicit versioned review; do not rewrite historic evidence.
- `morrocwi/islamic-archive-th` is an independent community archive, not CICOT, not the Office of the Chularajmontri, and not a court or mosque. No institutional endorsement is implied.
- Source: Lahtee, *Causal Ethics* (2026), https://doi.org/10.5281/zenodo.18444260; FAQR v1.4 local anchor; `morrocwi/toledo` registry. **Neither imported work has been silently reclassified as the other.**

**Outcome at publication:** Bridge proposal filed in Toledo; factual/religious-source validation and calibrated CE domain weld remain `OPEN`.
