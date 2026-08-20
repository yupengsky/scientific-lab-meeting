#!/usr/bin/env python3
"""Lightweight regression checks for protocol validator record gates."""

from __future__ import annotations

import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
import validate as protocol_validate


def record(fields: list[str], overrides: dict[str, str] | None = None) -> str:
    overrides = overrides or {}
    return "\n\n".join(f"{field}: {overrides.get(field, 'present')}" for field in fields)


@contextmanager
def fixture_root() -> Path:
    original = protocol_validate.ROOT
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        (root / "candidates").mkdir()
        (root / "outputs").mkdir()
        protocol_validate.ROOT = root
        try:
            yield root
        finally:
            protocol_validate.ROOT = original


class ValidatorRegressionTests(unittest.TestCase):
    def test_clean_baseline_passes(self) -> None:
        self.assertEqual(protocol_validate.Validator().run(), 0)

    def test_rejects_hamming_paraphrase_verdict(self) -> None:
        validator = protocol_validate.Validator()
        schema = protocol_validate.CRITIC_SCHEMAS["Hamming"]
        validator.validate_record(protocol_validate.ROOT / "candidates/C001.md", "Hamming", record(schema["fields"], {"VERDICT": "HIGH IMPORTANCE"}), schema)
        self.assertTrue(any("invalid VERDICT" in error for error in validator.errors))

    def test_rejects_incomplete_medawar_review(self) -> None:
        validator = protocol_validate.Validator()
        schema = protocol_validate.CRITIC_SCHEMAS["Medawar"]
        validator.validate_record(protocol_validate.ROOT / "candidates/C001.md", "Medawar", "VERDICT: TRACTABLE\n\nREASONABLE ATTACK: present", schema)
        self.assertTrue(any("must contain exactly one" in error for error in validator.errors))

    def test_rejects_platt_missing_prediction_and_elimination(self) -> None:
        validator = protocol_validate.Validator()
        schema = protocol_validate.CRITIC_SCHEMAS["Platt"]
        fields = [field for field in schema["fields"] if field not in {"PREDICTION TABLE", "WHAT EACH OUTCOME ELIMINATES"}]
        validator.validate_record(protocol_validate.ROOT / "candidates/C001.md", "Platt", record(fields, {"VERDICT": "PURSUE", "DISCRIMINATION STRENGTH": "PARTIAL"}), schema)
        self.assertTrue(any("PREDICTION TABLE" in error for error in validator.errors))
        self.assertTrue(any("WHAT EACH OUTCOME ELIMINATES" in error for error in validator.errors))

    def test_rejects_alon_missing_expected_value(self) -> None:
        validator = protocol_validate.Validator()
        schema = protocol_validate.CRITIC_SCHEMAS["Alon"]
        fields = [field for field in schema["fields"] if field != "EXPECTED KNOWLEDGE GAIN"]
        validator.validate_record(protocol_validate.ROOT / "candidates/C001.md", "Alon", record(fields, {"VERDICT": "PURSUE"}), schema)
        self.assertTrue(any("EXPECTED KNOWLEDGE GAIN" in error for error in validator.errors))

    def test_rejects_pi_decision_only(self) -> None:
        validator = protocol_validate.Validator()
        validator.validate_pi_record(protocol_validate.ROOT / "candidates/C001.md", "DECISION: PILOT ONLY")
        self.assertTrue(any("CORE SCIENTIFIC QUESTION" in error for error in validator.errors))

    def test_rejects_stage7_screening_omission(self) -> None:
        with fixture_root() as root:
            (root / "candidates/SCREENING.md").write_text(
                "# Candidate Screening\n\n| Uxx | Disposition | Reason | Candidate(s) |\n|---|---|---|---|\n| U001 | DEFERRED | no discriminator | NONE |\n",
                encoding="utf-8",
            )
            validator = protocol_validate.Validator()
            validator.validate_screening({7}, ["U001", "U002"], {})
            self.assertTrue(any("omits problem-map nodes" in error for error in validator.errors))

    def test_rejects_nonpilot_pilot_selection(self) -> None:
        with fixture_root() as root:
            (root / "outputs/PILOT_SELECTION.md").write_text(
                "# Pilot Scarcity Selection\n\n"
                "## Eligible pilots\n\nC001\n\n"
                "## Absolute threshold against RUN NO PILOT\n\nC001 is compared with RUN NO PILOT.\n\n"
                "## Pairwise comparison\n\nNOT APPLICABLE\n\n"
                "## Selection\n\nSELECTED: C999\n\n"
                "## Why run rather than no pilot\n\npresent\n\n"
                "## Why no pilot\n\npresent\n\n"
                "## Selected pilot stop criterion\n\npresent\n\n"
                "## Selected pilot go criterion\n\npresent\n\n"
                "## Claim permitted after success\n\npresent\n\n"
                "## Claim permitted after a clean negative result\n\npresent\n\n"
                "## Claim not permitted after either result\n\npresent\n",
                encoding="utf-8",
            )
            validator = protocol_validate.Validator()
            validator.validate_pilot_selection({"C001"})
            self.assertTrue(any("selects non-PILOT candidate" in error for error in validator.errors))


if __name__ == "__main__":
    unittest.main()
