#!/usr/bin/env python3
import tempfile, unittest
from pathlib import Path
import validate

class Gates(unittest.TestCase):
 def test_clean_baseline(self): self.assertEqual(validate.Validator().run(),0)
 def test_model_matrix_is_exact(self):
  v=validate.Validator();v.validate_agents();self.assertFalse(v.errors)
 def test_missing_model_pin_is_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/".codex/agents").mkdir(parents=True);(root/".codex/config.toml").write_text("[agents.literature_scout]\nconfig_file = 'agents/literature_scout.toml'",encoding="utf-8");(root/".codex/agents/literature_scout.toml").write_text("name = 'literature_scout'\nmodel_reasoning_effort = 'low'",encoding="utf-8")
   old=validate.ROOT;validate.ROOT=root;v=validate.Validator();v.validate_agents();validate.ROOT=old;self.assertTrue(v.errors)
 def test_unexpected_model_and_effort_are_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/".codex/agents").mkdir(parents=True);(root/".codex/config.toml").write_text("[agents.literature_scout]\nconfig_file = 'agents/literature_scout.toml'",encoding="utf-8");(root/".codex/agents/literature_scout.toml").write_text("name='literature_scout'\nmodel='wrong'\nmodel_reasoning_effort='high'",encoding="utf-8")
   old=validate.ROOT;validate.ROOT=root;v=validate.Validator();v.validate_agents();validate.ROOT=old;self.assertTrue(any("unexpected" in e for e in v.errors))
 def test_rejects_missing_card_identity(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/"x.md";p.write_text("**READING_STATUS:** FULL_TEXT",encoding="utf-8")
   v=validate.Validator(); old=validate.ROOT; validate.ROOT=Path(d); (Path(d)/"literature/cards").mkdir(parents=True); p.rename(Path(d)/"literature/cards/x.md");v.cards({4});validate.ROOT=old;self.assertTrue(v.errors)
 def test_rejects_invalid_confidence_and_verification(self):
  t="VERDICT: IMPORTANT\nCONFIDENCE: MAYBE\nCONFIDENCE RATIONALE: x\nNEEDS_VERIFICATION: SOURCE: x"
  v=validate.Validator(); old=validate.ROOT
  with tempfile.TemporaryDirectory() as d:
   validate.ROOT=Path(d);(Path(d)/"candidates").mkdir();(Path(d)/"candidates/C001.md").write_text(t,encoding="utf-8");v.candidates({11},[])
  validate.ROOT=old;self.assertTrue(v.errors)
 def test_field_ready_with_gap_is_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/"literature").mkdir();(root/"literature/COVERAGE.md").write_text("## Field-level explanatory families\n\n### Family: x\nEXPLANATORY FAMILY: x\nPRIMARY SUPPORT: NOT READY\nINDEPENDENT SUPPORT: x\nCOMPETING ACCOUNT: x\nCONTRADICTORY / LIMITING EVIDENCE: x\nDIRECT FOLLOW-UPS / REBUTTALS: x\nRECENT CAPABILITY CHANGE: x\nREADING DEPTH: x\nREMAINING GAP: x\nSTATUS: READY\n\n## Uxx-specific coverage",encoding="utf-8")
   old=validate.ROOT;validate.ROOT=root;v=validate.Validator();v.coverage({3});validate.ROOT=old;self.assertTrue(v.errors)
if __name__=="__main__": unittest.main()
