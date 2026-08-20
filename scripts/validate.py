#!/usr/bin/env python3
"""Validate repository structure without making scientific judgments."""

from __future__ import annotations

import hashlib
import re
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_PI = {
    "FUND",
    "PILOT ONLY",
    "REDESIGN",
    "KILL",
    "DECISION BLOCKED — VERIFY EVIDENCE",
}
REQUIRED_CANDIDATE_HEADINGS = [
    "Source uncertainty",
    "Scientific question",
    "Scientific uncertainty being reduced",
    "Established evidence",
    "Relevant explanations",
    "Relationship among explanations",
    "Why current evidence is insufficient",
    "Potential discriminating observation",
    "Provisional attack",
    "Why now",
    "Scope",
    "Negative-result information",
    "Evidence basis",
    "Unverified assumptions",
    "Hamming",
    "Medawar",
    "Platt",
    "Alon",
    "Review integrity",
    "Debate",
    "Decision-critical evidence verification",
    "PI readiness",
    "Skeptical PI",
]
STAGE_NAMES = [
    "WORKSPACE INITIALIZATION",
    "LITERATURE DISCOVERY",
    "COVERAGE CHALLENGE",
    "MINIMUM SUFFICIENT EVIDENCE SET",
    "TARGETED PAPER CARDS",
    "EVIDENCE SUFFICIENCY / TARGETED REPAIR",
    "PROBLEM MAP",
    "CANDIDATE GENERATION",
    "ROUND-1 BLIND CRITICS",
    "REVIEW INTEGRITY CHECK",
    "TARGETED REBUTTAL",
    "DECISION-CRITICAL EVIDENCE VERIFICATION",
    "PI READINESS GATE",
    "INDEPENDENT SKEPTICAL PI",
    "FINAL PORTFOLIO DECISION",
    "PILOT SCARCITY SELECTION",
    "FINAL VALIDATION",
]
STAGE_IDS = [
    "WORKSPACE_INITIALIZATION",
    "LITERATURE_DISCOVERY",
    "COVERAGE_CHALLENGE",
    "MINIMUM_SUFFICIENT_EVIDENCE_SET",
    "TARGETED_PAPER_CARDS",
    "EVIDENCE_SUFFICIENCY_TARGETED_REPAIR",
    "PROBLEM_MAP",
    "CANDIDATE_GENERATION",
    "ROUND_1_BLIND_CRITICS",
    "REVIEW_INTEGRITY_CHECK",
    "TARGETED_REBUTTAL",
    "DECISION_CRITICAL_EVIDENCE_VERIFICATION",
    "PI_READINESS_GATE",
    "INDEPENDENT_SKEPTICAL_PI",
    "FINAL_PORTFOLIO_DECISION",
    "PILOT_SCARCITY_SELECTION",
    "FINAL_VALIDATION",
]
SHELL_PREFIX = re.compile(
    r"^(Exit code:|Wall time:|Process exited|Output:|Script completed|Traceback \(most recent call last\):)",
    re.MULTILINE,
)


class Validator:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    @staticmethod
    def topic_snapshot() -> str:
        return f"sha256:{hashlib.sha256((ROOT / 'TOPIC.md').read_bytes()).hexdigest()}"

    @staticmethod
    def evidence_snapshot() -> str:
        paths = [ROOT / "literature/INDEX.md", ROOT / "literature/PROBLEM_MAP.md"]
        paths.extend(
            path for path in sorted((ROOT / "literature/cards").glob("*.md"))
            if path.name != "TEMPLATE.md"
        )
        paths.extend(
            path for path in sorted((ROOT / "candidates").glob("C[0-9][0-9][0-9].md"))
        )
        manifest = hashlib.sha256()
        for path in paths:
            relative = path.relative_to(ROOT).as_posix().encode("utf-8")
            data = path.read_bytes()
            if path.parent == ROOT / "candidates":
                data = data.split(b"\n# Lab meeting", 1)[0]
            manifest.update(relative)
            manifest.update(b"\0")
            manifest.update(hashlib.sha256(data).digest())
            manifest.update(b"\0")
        return f"sha256:{manifest.hexdigest()}"

    def text(self, relative: str) -> str:
        path = ROOT / relative
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error(f"cannot read {relative}: {exc}")
            return ""

    def require_layout(self) -> None:
        required_dirs = [".codex/agents", "literature/cards", "candidates", "outputs", "scripts"]
        required_files = [
            "AGENTS.md",
            "WORKFLOW.md",
            "README.md",
            "TOPIC.md",
            "RUN_STATE.md",
            ".codex/config.toml",
            "literature/INDEX.md",
            "literature/PROBLEM_MAP.md",
            "literature/cards/TEMPLATE.md",
            "candidates/TEMPLATE.md",
            "outputs/README.md",
        ]
        for relative in required_dirs:
            if not (ROOT / relative).is_dir():
                self.error(f"missing required directory: {relative}")
        for relative in required_files:
            if not (ROOT / relative).is_file():
                self.error(f"missing required file: {relative}")

    def validate_toml(self) -> None:
        for path in sorted((ROOT / ".codex").rglob("*.toml")):
            try:
                tomllib.loads(path.read_text(encoding="utf-8-sig"))
            except (OSError, UnicodeError, tomllib.TOMLDecodeError) as exc:
                self.error(f"invalid TOML {path.relative_to(ROOT)}: {exc}")

    def parse_state(self) -> tuple[str, str, str, str, set[int]]:
        state = self.text("RUN_STATE.md")
        status_match = re.search(r"^STATUS:[ \t]*(\S.*)?$", state, re.MULTILINE)
        topic_match = re.search(r"^TOPIC_SNAPSHOT:[ \t]*(\S.*)?$", state, re.MULTILINE)
        current_match = re.search(r"^CURRENT_STAGE:[ \t]*(\S.*)?$", state, re.MULTILINE)
        evidence_match = re.search(r"^EVIDENCE_SNAPSHOT:[ \t]*(\S.*)?$", state, re.MULTILINE)
        status = (status_match.group(1) or "").strip() if status_match else ""
        topic_snapshot = (topic_match.group(1) or "").strip() if topic_match else ""
        current_stage = (current_match.group(1) or "").strip() if current_match else ""
        evidence_snapshot = (evidence_match.group(1) or "").strip() if evidence_match else ""
        if not status_match:
            self.error("RUN_STATE.md lacks STATUS")
        if status not in {"NOT_STARTED", "IN_PROGRESS", "COMPLETE", "BLOCKED"}:
            self.error(f"RUN_STATE.md has invalid STATUS: {status or '<empty>'}")
        if not current_match:
            self.error("RUN_STATE.md lacks CURRENT_STAGE")
        elif current_stage not in STAGE_IDS:
            self.error(f"RUN_STATE.md has invalid CURRENT_STAGE: {current_stage or '<empty>'}")

        stages: dict[int, tuple[bool, str]] = {}
        pattern = re.compile(r"^- \[([ xX])\] (\d+)\. (.+)$", re.MULTILINE)
        for mark, number_text, name in pattern.findall(state):
            number = int(number_text)
            if number in stages:
                self.error(f"RUN_STATE.md duplicates stage {number}")
            stages[number] = (mark.lower() == "x", name.strip())
        for number, expected in enumerate(STAGE_NAMES):
            if number not in stages:
                self.error(f"RUN_STATE.md lacks stage {number}")
            elif stages[number][1] != expected:
                self.error(f"RUN_STATE.md stage {number} name differs from WORKFLOW.md")
        completed = {number for number, (done, _) in stages.items() if done}
        for number in completed:
            missing_prior = [prior for prior in range(number) if prior not in completed]
            if missing_prior:
                self.error(f"stage {number} is complete before stage {missing_prior[0]}")
        if status == "NOT_STARTED" and current_stage != STAGE_IDS[0]:
            self.error("NOT_STARTED run must point to WORKSPACE INITIALIZATION")
        if status == "IN_PROGRESS":
            first_incomplete = next((number for number in range(len(STAGE_NAMES)) if number not in completed), None)
            if first_incomplete is not None and current_stage != STAGE_IDS[first_incomplete]:
                self.error("CURRENT_STAGE does not match the first incomplete stage")
        if status == "COMPLETE" and (len(completed) != len(STAGE_NAMES) or current_stage != STAGE_IDS[-1]):
            self.error("COMPLETE run must have every stage checked and point to FINAL VALIDATION")
        return status, topic_snapshot, current_stage, evidence_snapshot, completed

    def validate_topic_snapshot(self, status: str, snapshot: str) -> None:
        topic_path = ROOT / "TOPIC.md"
        if status == "NOT_STARTED":
            if snapshot:
                self.error("TOPIC_SNAPSHOT must be empty while STATUS is NOT_STARTED")
            return
        if not re.fullmatch(r"sha256:[0-9a-f]{64}", snapshot):
            self.error("started run requires TOPIC_SNAPSHOT in sha256:<64 lowercase hex> form")
            return
        if snapshot != self.topic_snapshot():
            self.error("TOPIC CHANGED — CLEAN START BRANCH REQUIRED")

    def validate_baseline_state(self, status: str, completed: set[int]) -> None:
        if status != "NOT_STARTED":
            if "Replace this line with one broad scientific research direction" in self.text("TOPIC.md"):
                self.error("started run still contains the baseline TOPIC.md instruction")
            return
        if completed:
            self.error("NOT_STARTED run cannot claim completed stages")
        generated = self.candidate_files()
        generated.extend(path for path in (ROOT / "literature/cards").glob("*.md") if path.name != "TEMPLATE.md")
        generated.extend(path for path in (ROOT / "outputs").glob("*.md") if path.name != "README.md")
        if generated:
            names = ", ".join(str(path.relative_to(ROOT)) for path in generated)
            self.error(f"NOT_STARTED baseline contains generated artifacts: {names}")

    def candidate_files(self) -> list[Path]:
        directory = ROOT / "candidates"
        candidates: list[Path] = []
        for path in sorted(directory.glob("*.md")):
            if path.name == "TEMPLATE.md":
                continue
            if not re.fullmatch(r"C\d{3}\.md", path.name):
                self.error(f"invalid generated candidate filename: candidates/{path.name}")
                continue
            candidates.append(path)
        return candidates

    @staticmethod
    def section(text: str, heading: str) -> str:
        match = re.search(
            rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)",
            text,
            re.MULTILINE,
        )
        return match.group(1).strip() if match else ""

    def validate_candidates(
        self, completed: set[int]
    ) -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
        decisions: dict[str, str] = {}
        contents: dict[str, str] = {}
        source_nodes: dict[str, str] = {}
        seen_ids: set[str] = set()
        for path in self.candidate_files():
            candidate_id = path.stem
            if candidate_id in seen_ids:
                self.error(f"duplicate candidate ID: {candidate_id}")
            seen_ids.add(candidate_id)
            text = path.read_text(encoding="utf-8")
            contents[candidate_id] = text
            if not re.search(rf"^# Candidate {candidate_id}$", text, re.MULTILINE):
                self.error(f"{path.relative_to(ROOT)} title does not match filename")
            nodes = re.findall(r"\*\*Problem-map node:\*\*\s*(U\d+)", text)
            if len(nodes) != 1:
                self.error(f"{path.relative_to(ROOT)} must cite exactly one Uxx source node")
            else:
                source_nodes[candidate_id] = nodes[0]
            headings = set(re.findall(r"^## (.+?)\s*$", text, re.MULTILINE))
            for heading in REQUIRED_CANDIDATE_HEADINGS:
                if heading not in headings:
                    self.error(f"{path.relative_to(ROOT)} lacks required heading: {heading}")
            if re.search(r"\[\.\.\.\]|\bCxxx\b|\bUxx\b|\[Paper title\]", text):
                self.error(f"{path.relative_to(ROOT)} contains an unresolved template placeholder")

            if 8 in completed:
                for critic in ("Hamming", "Medawar", "Platt", "Alon"):
                    section = self.section(text, critic)
                    if not section or "PENDING" in section:
                        self.error(f"{path.relative_to(ROOT)} has incomplete Round-1 section: {critic}")
            if 9 in completed:
                section = self.section(text, "Review integrity")
                if not section or "PENDING" in section:
                    self.error(f"{path.relative_to(ROOT)} lacks completed review-integrity record")
            if 10 in completed:
                section = self.section(text, "Debate")
                if not section or "PENDING" in section:
                    self.error(f"{path.relative_to(ROOT)} has stale PENDING content in Debate")
                if not re.search(r"\b(APPARENT|SUBSTANTIVE|NONE)\b", section):
                    self.error(f"{path.relative_to(ROOT)} lacks a disagreement classification")
            if 11 in completed:
                section = self.section(text, "Decision-critical evidence verification")
                if not section or "PENDING" in section:
                    self.error(f"{path.relative_to(ROOT)} has incomplete evidence-verification record")
            if 12 in completed:
                section = self.section(text, "PI readiness")
                if not section or "PENDING" in section:
                    self.error(f"{path.relative_to(ROOT)} lacks a PI-readiness classification")
                elif not re.search(
                    r"\bREADY FOR PI\b|\bDECISION BLOCKED — EVIDENCE STILL UNRESOLVED\b",
                    section,
                ):
                    self.error(f"{path.relative_to(ROOT)} has invalid PI-readiness vocabulary")

            pi_section = self.section(text, "Skeptical PI")
            decision_match = re.search(r"^DECISION:\s*(.+?)\s*$", pi_section, re.MULTILINE)
            if decision_match and decision_match.group(1) != "PENDING":
                decision = decision_match.group(1).strip()
                if decision not in ALLOWED_PI:
                    self.error(f"{path.relative_to(ROOT)} has invalid PI decision: {decision}")
                else:
                    decisions[candidate_id] = decision
            elif 13 in completed:
                self.error(f"{path.relative_to(ROOT)} lacks a completed PI decision")
        return decisions, contents, source_nodes

    def validate_cards(self, completed: set[int]) -> None:
        if 4 not in completed:
            return
        for path in sorted((ROOT / "literature/cards").glob("*.md")):
            if path.name == "TEMPLATE.md":
                continue
            text = path.read_text(encoding="utf-8")
            status = re.search(r"^\*\*READING_STATUS:\*\*\s*(\S.*)$", text, re.MULTILINE)
            if not status or status.group(1).strip() not in {"FULL_TEXT", "PARTIAL", "ABSTRACT_ONLY"}:
                self.error(f"{path.relative_to(ROOT)} has invalid or missing READING_STATUS")
            for marker in ("OBSERVATION", "AUTHOR INTERPRETATION", "INFERENCE"):
                if f"**{marker}:**" not in text:
                    self.error(f"{path.relative_to(ROOT)} lacks claim marker: {marker}")
            if not re.search(r"^\*\*Source URL:\*\*[ \t]+\S.*$", text, re.MULTILINE):
                self.error(f"{path.relative_to(ROOT)} lacks Source URL")

    def validate_markdown_hygiene(self) -> None:
        paths: list[Path] = []
        paths.extend(self.candidate_files())
        paths.extend(path for path in (ROOT / "literature/cards").glob("*.md") if path.name != "TEMPLATE.md")
        paths.extend([ROOT / "literature/INDEX.md", ROOT / "literature/PROBLEM_MAP.md"])
        paths.extend(path for path in (ROOT / "outputs").glob("*.md") if path.name != "README.md")
        for path in paths:
            if not path.exists():
                continue
            opening = "\n".join(path.read_text(encoding="utf-8").splitlines()[:6])
            if SHELL_PREFIX.search(opening):
                self.error(f"captured shell/terminal output at start of {path.relative_to(ROOT)}")
            text = path.read_text(encoding="utf-8")
            if re.search(r"\[\.\.\.\]|\bCxxx\b|\[Paper title\]", text):
                self.error(f"unresolved template placeholder in {path.relative_to(ROOT)}")

    def validate_stage_artifacts(
        self,
        status: str,
        evidence_snapshot: str,
        completed: set[int],
        decisions: dict[str, str],
        candidate_contents: dict[str, str],
        source_nodes: dict[str, str],
    ) -> None:
        index = self.text("literature/INDEX.md")
        problem_map = self.text("literature/PROBLEM_MAP.md")
        candidates = set(candidate_contents)
        map_nodes = re.findall(r"^###? (U\d+)\b", problem_map, re.MULTILINE)
        duplicate_nodes = {node for node in map_nodes if map_nodes.count(node) > 1}
        if duplicate_nodes:
            self.error(f"PROBLEM_MAP duplicates uncertainty nodes: {', '.join(sorted(duplicate_nodes))}")
        for candidate_id, node in source_nodes.items():
            if 6 in completed and node not in map_nodes:
                self.error(f"{candidate_id} cites missing problem-map node {node}")

        if 1 in completed:
            if "**Status:** NOT_STARTED" in index:
                self.error("stage 1 claims completion while INDEX status is NOT_STARTED")
            for field in ("Topic", "Discovery date", "Literature cutoff / search date", "Broad query scope"):
                if not re.search(rf"^\*\*{re.escape(field)}:\*\*[ \t]+\S.*$", index, re.MULTILINE):
                    self.error(f"completed literature discovery lacks INDEX field: {field}")
        if 4 in completed:
            cards = [path for path in (ROOT / "literature/cards").glob("*.md") if path.name != "TEMPLATE.md"]
            if not cards:
                self.error("stage 4 claims completion but no generated paper card exists")
        if 6 in completed:
            if "**Status:** NOT_STARTED" in problem_map:
                self.error("stage 6 claims completion while PROBLEM_MAP status is NOT_STARTED")
            if not re.search(r"^###? U\d+\b", problem_map, re.MULTILINE):
                self.error("completed PROBLEM_MAP contains no structured Uxx node")
        if 8 in completed and candidates and not re.fullmatch(r"sha256:[0-9a-f]{64}", evidence_snapshot):
            self.error("completed Round 1 requires EVIDENCE_SNAPSHOT in sha256 form")
        elif 8 in completed and candidates and evidence_snapshot != self.evidence_snapshot():
            self.error("EVIDENCE_SNAPSHOT does not match the frozen Round-1 evidence manifest")

        final_path = ROOT / "outputs/FINAL_DECISION.md"
        if 14 in completed:
            if not final_path.is_file():
                self.error("stage 14 claims completion without outputs/FINAL_DECISION.md")
            else:
                final_text = final_path.read_text(encoding="utf-8")
                refs = set(re.findall(r"\bC\d{3}\b", final_text))
                missing = refs - candidates
                if missing:
                    self.error(f"FINAL_DECISION references missing candidates: {', '.join(sorted(missing))}")
                if candidates and refs != candidates:
                    omitted = candidates - refs
                    self.error(f"FINAL_DECISION omits candidates: {', '.join(sorted(omitted))}")
                for candidate_id, decision in decisions.items():
                    candidate_lines = [line for line in final_text.splitlines() if candidate_id in line]
                    if not any(decision in line for line in candidate_lines):
                        self.error(f"FINAL_DECISION does not preserve {candidate_id} decision {decision}")

        fund_count = sum(decision == "FUND" for decision in decisions.values())
        pilot_ids = {candidate_id for candidate_id, decision in decisions.items() if decision == "PILOT ONLY"}
        pilot_path = ROOT / "outputs/PILOT_SELECTION.md"
        scarcity_applies = bool(decisions) and fund_count == 0 and bool(pilot_ids)
        if 15 in completed and scarcity_applies:
            if not pilot_path.is_file():
                self.error("pilot scarcity applies but outputs/PILOT_SELECTION.md is missing")
            else:
                refs = set(re.findall(r"\bC\d{3}\b", pilot_path.read_text(encoding="utf-8")))
                ineligible = refs - pilot_ids
                if ineligible:
                    self.error(f"PILOT_SELECTION references ineligible candidates: {', '.join(sorted(ineligible))}")
        if 15 in completed and not scarcity_applies and pilot_path.exists():
            self.error("PILOT_SELECTION exists when scarcity selection is not applicable")
        if 16 in completed and status != "COMPLETE":
            self.error("stage 16 claims completion while STATUS is not COMPLETE")

    def run(self) -> int:
        self.require_layout()
        self.validate_toml()
        status, topic_snapshot, _current_stage, evidence_snapshot, completed = self.parse_state()
        self.validate_topic_snapshot(status, topic_snapshot)
        self.validate_baseline_state(status, completed)
        decisions, contents, source_nodes = self.validate_candidates(completed)
        self.validate_cards(completed)
        self.validate_markdown_hygiene()
        self.validate_stage_artifacts(
            status, evidence_snapshot, completed, decisions, contents, source_nodes
        )
        if self.errors:
            print(f"STRUCTURAL VALIDATION FAILED ({len(self.errors)} error(s))")
            for error in self.errors:
                print(f"- {error}")
            return 1
        print("STRUCTURAL VALIDATION PASSED")
        return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--print-topic-snapshot"]:
        print(Validator.topic_snapshot())
        sys.exit(0)
    if sys.argv[1:] == ["--print-evidence-snapshot"]:
        print(Validator.evidence_snapshot())
        sys.exit(0)
    if len(sys.argv) > 1:
        print("usage: validate.py [--print-topic-snapshot | --print-evidence-snapshot]", file=sys.stderr)
        sys.exit(2)
    sys.exit(Validator().run())
