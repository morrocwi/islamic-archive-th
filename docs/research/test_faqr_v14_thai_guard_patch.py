#!/usr/bin/env python3
"""Regression tests for FAQR-IEA v1.4 Thai authority-claim guard.
Run: python3 docs/research/test_faqr_v14_thai_guard_patch.py
These are synthetic test strings ([SimulatedData]), NOT religious verdicts.
"""
from __future__ import annotations
from pathlib import Path
import runpy
import unittest

module = runpy.run_path(str(Path(__file__).with_name("FAQR_V14_THAI_AUTHORITY_GUARD_PATCH.py")))
thai_violations=module["thai_violations"]
validate=module["validate"]

def fixture(text):
    return {"direct_answer":{"text":text},"narrative_sections":[],"fact_ledger":[],"option_ledger":[],"projection":{"rendered_text":""}}

class ThaiGuardTests(unittest.TestCase):
    def test_self_issued_fatwa_rejected(self):
        self.assertIn("ai_fatwa",thai_violations(fixture("ข้าพเจ้าออกฟัตวาว่าญาติผิด")))
    def test_mediation_rejected(self):
        self.assertIn("ai_mediation",thai_violations(fixture("ฉันจะไกล่เกลี่ยความขัดแย้งนี้")))
    def test_choose_winner_rejected(self):
        self.assertIn("ai_choose_winner",thai_violations(fixture("ผมจะตัดสินให้ว่าฝ่ายไหนถูก")))
    def test_takfir_rejected(self):
        self.assertIn("ai_personal_takfir",thai_violations(fixture("ฉันขอตัดสินว่าญาติเป็นมุชริก")))
    def test_negated_statement_allowed(self):
        self.assertEqual([],thai_violations(fixture("AI ไม่ออกฟัตวาและไม่ไกล่เกลี่ย")))
    def test_attributed_scholar_statement_allowed(self):
        self.assertEqual([],thai_violations(fixture("สำนักฟัตวาอียิปต์เห็นว่าการรำลึกถึงเมาลิดทำได้")))
    def test_untrusted_anchor_rejected_before_exec(self):
        with self.assertRaisesRegex(ValueError,"Untrusted/mismatched"):
            validate("UNTRUSTED FILE",fixture("คำถามทั่วไป"))

if __name__=="__main__":
    unittest.main()
