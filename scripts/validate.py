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
CRITIC_SCHEMAS = {
    "Hamming": {
        "verdicts": {"IMPORTANT", "QUESTIONABLE", "LOW-VALUE"},
        "fields": [
            "VERDICT", "CORE QUESTION", "WHY IT MATTERS", "WHAT CHANGES IF SOLVED",
            "WHAT DOES NOT CHANGE", "STRONGEST SO-WHAT OBJECTION", "FATAL IMPORTANCE FLAW",
            "CONFIDENCE", "NEEDS_VERIFICATION",
        ],
    },
    "Medawar": {
        "verdicts": {"TRACTABLE", "WEAK ATTACK", "CURRENTLY INSOLUBLE"},
        "fields": [
            "VERDICT", "REASONABLE ATTACK", "WHY NOW", "MINIMUM TRACTABLE QUESTION",
            "MINIMUM FIRST STEP", "MAIN TECHNICAL BOTTLENECK", "CHEAPER ATTACK",
            "FATAL TRACTABILITY FLAW", "CONFIDENCE", "NEEDS_VERIFICATION",
        ],
    },
    "Platt": {
        "verdicts": {"PURSUE", "REDESIGN", "KILL"},
        "fields": [
            "PHENOMENON", "COMPETING HYPOTHESES", "PREDICTION TABLE",
            "PROPOSED CRITICAL EXPERIMENT", "WHAT EACH OUTCOME ELIMINATES",
            "SURVIVING ALTERNATIVE EXPLANATIONS", "NEGATIVE-RESULT VALUE",
            "BETTER DISCRIMINATING EXPERIMENT", "DISCRIMINATION STRENGTH", "VERDICT",
            "FATAL INFERENCE FLAW", "CONFIDENCE", "NEEDS_VERIFICATION",
        ],
        "allowed": {"DISCRIMINATION STRENGTH": {"STRONG", "PARTIAL", "WEAK", "NONE"}},
    },
    "Alon": {
        "verdicts": {"PURSUE", "PILOT FIRST", "QUESTIONABLE", "KILL"},
        "fields": [
            "SCIENTIFIC INTEREST", "FEASIBILITY", "EXPECTED KNOWLEDGE GAIN",
            "VALUE IF MAIN HYPOTHESIS IS WRONG", "COST", "TECHNICAL RISK", "CONCEPTUAL RISK",
            "BETTER SMALLER VERSION", "EXPECTED RESEARCH VALUE", "VERDICT", "FATAL VALUE FLAW",
            "CONFIDENCE", "NEEDS_VERIFICATION",
        ],
    },
}
PI_FIELDS = [
    "DECISION", "CORE SCIENTIFIC QUESTION", "STRONGEST ARGUMENT FOR",
    "STRONGEST ARGUMENT AGAINST", "FATAL FLAW", "CHEAPEST DECISIVE PILOT",
    "WHAT THE PILOT MUST DISTINGUISH", "STOP CRITERION", "GO CRITERION",
    "WHAT A NEGATIVE RESULT WOULD TEACH", "WHAT SUCCESS WOULD PERMIT US TO CLAIM",
    "WHAT SUCCESS WOULD NOT PERMIT US TO CLAIM", "WHAT WOULD CHANGE MY DECISION",
    "BIGGEST REMAINING UNCERTAINTY", "STRONGEST ALTERNATIVE CANDIDATE",
    "WHY THIS CANDIDATE IS BETTER OR WORSE THAN THAT ALTERNATIVE", "FINAL RATIONALE",
]
REQUIRED_CANDIDATE_HEADINGS = [
    "Source uncertainty", "Scientific question", "Scientific uncertainty being reduced",
    "Established evidence", "Relevant explanations", "Relationship among explanations",
    "Why current evidence is insufficient", "Potential discriminating observation",
    "Provisional attack", "Why now", "Scope", "Negative-result information", "Evidence basis",
    "Unverified assumptions", "Construct validity and surviving implementation alternatives",
    "Hamming", "Medawar", "Platt", "Alon", "Review integrity", "Debate",
    "Decision-critical evidence verification", "PI readiness", "Skeptical PI",
]
STAGE_NAMES = [
    "WORKSPACE INITIALIZATION", "LITERATURE DISCOVERY", "COVERAGE CHALLENGE",
    "MINIMUM SUFFICIENT EVIDENCE SET", "TARGETED PAPER CARDS",
    "EVIDENCE SUFFICIENCY / TARGETED REPAIR", "PROBLEM MAP", "CANDIDATE GENERATION",
    "ROUND-1 BLIND CRITICS", "REVIEW INTEGRITY CHECK", "TARGETED REBUTTAL",
    "DECISION-CRITICAL EVIDENCE VERIFICATION", "PI READINESS GATE",
    "INDEPENDENT SKEPTICAL PI", "FINAL PORTFOLIO DECISION", "PILOT SCARCITY SELECTION",
    "FINAL VALIDATION",
]
STAGE_IDS = [
    "WORKSPACE_INITIALIZATION", "LITERATURE_DISCOVERY", "COVERAGE_CHALLENGE",
    "MINIMUM_SUFFICIENT_EVIDENCE_SET", "TARGETED_PAPER_CARDS",
    "EVIDENCE_SUFFICIENCY_TARGETED_REPAIR", "PROBLEM_MAP", "CANDIDATE_GENERATION",
    "ROUND_1_BLIND_CRITICS", "REVIEW_INTEGRITY_CHECK", "TARGETED_REBUTTAL",
    "DECISION_CRITICAL_EVIDENCE_VERIFICATION", "PI_READINESS_GATE",
    "INDEPENDENT_SKEPTICAL_PI", "FINAL_PORTFOLIO_DECISION", "PILOT_SCARCITY_SELECTION",
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
        paths.extend(path for path in sorted((ROOT / "literature/cards").glob("*.md")) if path.name != "TEMPLATE.md")
        paths.extend(sorted((ROOT / "candidates").glob("C[0-9][0-9][0-9].md")))
        manifest = hashlib.sha256()
        for path in paths:
            data = path.read_bytes()
            if path.parent == ROOT / "candidates":
                data = data.split(b"\n# Lab meeting", 1)[0]
            manifest.update(path.relative_to(ROOT).as_posix().encode("utf-8"))
            manifest.update(b"\0")
            manifest.update(hashlib.sha256(data).digest())
            manifest.update(b"\0")
        return f"sha256:{manifest.hexdigest()}"

    def text(self, relative: str) -> str:
        try:
            return (ROOT / relative).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.error(f"cannot read {relative}: {exc}")
            return ""

    def require_layout(self) -> None:
        for relative in [".codex/agents", "literature/cards", "candidates", "outputs", "scripts"]:
            if not (ROOT / relative).is_dir():
                self.error(f"missing required directory: {relative}")
        for relative in [
            "AGENTS.md", "WORKFLOW.md", "README.md", "TOPIC.md", "RUN_STATE.md",
            ".codex/config.toml", "literature/INDEX.md", "literature/PROBLEM_MAP.md",
            "literature/cards/TEMPLATE.md", "candidates/TEMPLATE.md", "candidates/SCREENING.md",
            "outputs/README.md",
        ]:
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
        def value(name: str) -> tuple[str, bool]:
            match = re.search(rf"^{name}:[ \t]*(\S.*)?$", state, re.MULTILINE)
            return ((match.group(1) or "").strip(), bool(match))

        status, status_found = value("STATUS")
        snapshot, _ = value("TOPIC_SNAPSHOT")
        current, current_found = value("CURRENT_STAGE")
        evidence, _ = value("EVIDENCE_SNAPSHOT")
        if not status_found:
            self.error("RUN_STATE.md lacks STATUS")
        elif status not in {"NOT_STARTED", "IN_PROGRESS", "COMPLETE", "BLOCKED"}:
            self.error(f"RUN_STATE.md has invalid STATUS: {status or '<empty>'}")
        if not current_found:
            self.error("RUN_STATE.md lacks CURRENT_STAGE")
        elif current not in STAGE_IDS:
            self.error(f"RUN_STATE.md has invalid CURRENT_STAGE: {current or '<empty>'}")

        stages: dict[int, tuple[bool, str]] = {}
        for mark, number_text, name in re.findall(r"^- \[([ xX])\] (\d+)\. (.+)$", state, re.MULTILINE):
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
            if any(prior not in completed for prior in range(number)):
                self.error(f"stage {number} is complete before an earlier stage")
        if status == "NOT_STARTED" and current != STAGE_IDS[0]:
            self.error("NOT_STARTED run must point to WORKSPACE INITIALIZATION")
        if status == "IN_PROGRESS":
            first = next((number for number in range(len(STAGE_NAMES)) if number not in completed), None)
            if first is not None and current != STAGE_IDS[first]:
                self.error("CURRENT_STAGE does not match the first incomplete stage")
        if status == "COMPLETE" and (len(completed) != len(STAGE_NAMES) or current != STAGE_IDS[-1]):
            self.error("COMPLETE run must have every stage checked and point to FINAL VALIDATION")
        return status, snapshot, current, evidence, completed

    def validate_topic_snapshot(self, status: str, snapshot: str) -> None:
        if status == "NOT_STARTED":
            if snapshot:
                self.error("TOPIC_SNAPSHOT must be empty while STATUS is NOT_STARTED")
            return
        if not re.fullmatch(r"sha256:[0-9a-f]{64}", snapshot):
            self.error("started run requires TOPIC_SNAPSHOT in sha256:<64 lowercase hex> form")
        elif snapshot != self.topic_snapshot():
            self.error("TOPIC CHANGED — CLEAN START BRANCH REQUIRED")

    def candidate_files(self) -> list[Path]:
        candidates: list[Path] = []
        for path in sorted((ROOT / "candidates").glob("*.md")):
            if path.name in {"TEMPLATE.md", "SCREENING.md"}:
                continue
            if not re.fullmatch(r"C\d{3}\.md", path.name):
                self.error(f"invalid generated candidate filename: candidates/{path.name}")
            else:
                candidates.append(path)
        return candidates

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

    @staticmethod
    def section(text: str, heading: str) -> str:
        match = re.search(rf"^## {re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)", text, re.MULTILINE)
        return match.group(1).strip() if match else ""

    @staticmethod
    def labeled_fields(text: str, labels: list[str]) -> dict[str, str]:
        prefix = r"^[ \t>]*"
        alternatives = "|".join(re.escape(label) for label in labels)
        result: dict[str, str] = {}
        for label in labels:
            matches = list(re.finditer(rf"{prefix}{re.escape(label)}:[ \t]*(.*)$", text, re.MULTILINE))
            if len(matches) != 1:
                continue
            start = matches[0].end()
            next_label = re.search(rf"{prefix}(?:{alternatives}):[ \t]*.*$", text[start:], re.MULTILINE)
            result[label] = text[start:start + next_label.start()].strip() if next_label else text[start:].strip()
            inline = matches[0].group(1).strip()
            if inline:
                result[label] = inline + ("\n" + result[label] if result[label] else "")
        return result

    def validate_record(self, path: Path, role: str, section: str, schema: dict) -> None:
        fields = schema["fields"]
        record = self.labeled_fields(section, fields)
        for field in fields:
            occurrences = len(re.findall(rf"^[ \t>]*{re.escape(field)}:[ \t]*.*$", section, re.MULTILINE))
            if occurrences != 1:
                self.error(f"{path.relative_to(ROOT)} {role} must contain exactly one {field} field")
            elif not record.get(field) or record[field].strip().upper() == "PENDING":
                self.error(f"{path.relative_to(ROOT)} {role} field is empty: {field}")
        verdict = record.get("VERDICT", "").strip()
        if verdict and verdict not in schema["verdicts"]:
            self.error(f"{path.relative_to(ROOT)} {role} has invalid VERDICT: {verdict}")
        for field, allowed in schema.get("allowed", {}).items():
            value = record.get(field, "").strip()
            if value and value not in allowed:
                self.error(f"{path.relative_to(ROOT)} {role} has invalid {field}: {value}")

    def validate_pi_record(self, path: Path, section: str) -> str | None:
        record = self.labeled_fields(section, PI_FIELDS)
        for field in PI_FIELDS:
            occurrences = len(re.findall(rf"^[ \t>]*{re.escape(field)}:[ \t]*.*$", section, re.MULTILINE))
            if occurrences != 1:
                self.error(f"{path.relative_to(ROOT)} Skeptical PI must contain exactly one {field} field")
            elif not record.get(field) or record[field].strip().upper() == "PENDING":
                self.error(f"{path.relative_to(ROOT)} Skeptical PI field is empty: {field}")
        decision = record.get("DECISION", "").strip()
        if decision not in ALLOWED_PI:
            self.error(f"{path.relative_to(ROOT)} has invalid PI decision: {decision or '<empty>'}")
            return None
        if decision == "PILOT ONLY":
            for field in ("STOP CRITERION", "GO CRITERION", "WHAT THE PILOT MUST DISTINGUISH"):
                if not record.get(field) or record[field].strip().upper() == "PENDING":
                    self.error(f"{path.relative_to(ROOT)} PILOT ONLY requires non-empty {field}")
        return decision

    def validate_candidates(self, completed: set[int]) -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
        decisions: dict[str, str] = {}
        contents: dict[str, str] = {}
        source_nodes: dict[str, str] = {}
        for path in self.candidate_files():
            candidate_id = path.stem
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
                for critic, schema in CRITIC_SCHEMAS.items():
                    critic_section = self.section(text, critic)
                    if not critic_section or "PENDING" in critic_section:
                        self.error(f"{path.relative_to(ROOT)} has incomplete Round-1 section: {critic}")
                    else:
                        self.validate_record(path, critic, critic_section, schema)
            if 9 in completed:
                integrity = self.section(text, "Review integrity")
                if not integrity or "PENDING" in integrity:
                    self.error(f"{path.relative_to(ROOT)} lacks completed review-integrity record")
            if 10 in completed:
                debate = self.section(text, "Debate")
                if not debate or "PENDING" in debate:
                    self.error(f"{path.relative_to(ROOT)} has stale PENDING content in Debate")
                elif not re.search(r"^\*\*Disagreement classification:\*\*\s*(NONE|APPARENT|SUBSTANTIVE)\s*$", debate, re.MULTILINE):
                    self.error(f"{path.relative_to(ROOT)} lacks a valid disagreement classification")
            if 11 in completed:
                verification = self.section(text, "Decision-critical evidence verification")
                values = re.findall(r"^VERIFICATION_STATUS:[ \t]*(.+?)\s*$", verification, re.MULTILINE)
                if len(values) != 1 or values[0].strip() not in {"COMPLETE", "NONE REQUIRED", "BLOCKED"}:
                    self.error(f"{path.relative_to(ROOT)} has invalid VERIFICATION_STATUS")
            readiness = self.section(text, "PI readiness")
            ready = bool(re.search(r"^READY FOR PI\s*$", readiness, re.MULTILINE))
            blocked = bool(re.search(r"^DECISION BLOCKED — EVIDENCE STILL UNRESOLVED\s*$", readiness, re.MULTILINE))
            if 12 in completed and (not readiness or "PENDING" in readiness or (not ready and not blocked)):
                self.error(f"{path.relative_to(ROOT)} has invalid PI-readiness vocabulary")

            pi_section = self.section(text, "Skeptical PI")
            has_pi = bool(re.search(r"^[ \t>]*DECISION:[ \t]*(?!PENDING\s*$).+", pi_section, re.MULTILINE))
            if has_pi:
                decision = self.validate_pi_record(path, pi_section)
                if decision:
                    decisions[candidate_id] = decision
            elif 13 in completed and ready:
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

    def validate_screening(self, completed: set[int], map_nodes: list[str], source_nodes: dict[str, str]) -> None:
        if 7 not in completed:
            return
        path = ROOT / "candidates/SCREENING.md"
        if not path.is_file():
            self.error("stage 7 claims completion without candidates/SCREENING.md")
            return
        lines = path.read_text(encoding="utf-8").splitlines()
        header = "| Uxx | Disposition | Reason | Candidate(s) |"
        if header not in lines:
            self.error("SCREENING.md lacks the required table header")
            return
        start = lines.index(header) + 2
        rows: list[tuple[str, str, str, str]] = []
        for line in lines[start:]:
            if not line.strip():
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 4:
                self.error(f"SCREENING.md has invalid table row: {line}")
                continue
            rows.append(tuple(cells))
        seen: dict[str, tuple[str, str, str]] = {}
        listed_candidates: dict[str, str] = {}
        for node, disposition, reason, candidate_cell in rows:
            if not re.fullmatch(r"U\d+", node):
                self.error(f"SCREENING.md has invalid Uxx identifier: {node or '<empty>'}")
                continue
            if node in seen:
                self.error(f"SCREENING.md duplicates {node}")
                continue
            seen[node] = (disposition, reason, candidate_cell)
            if disposition not in {"CANDIDATE", "PARTITIONED", "DEFERRED", "REJECTED"}:
                self.error(f"SCREENING.md has invalid disposition for {node}: {disposition or '<empty>'}")
            ids = re.findall(r"\bC\d{3}\b", candidate_cell)
            extra = re.sub(r"\bC\d{3}\b|[\s,;]", "", candidate_cell)
            if disposition == "CANDIDATE" and len(ids) != 1:
                self.error(f"SCREENING.md CANDIDATE row {node} must list exactly one Cxxx")
            if disposition == "PARTITIONED" and len(ids) < 2:
                self.error(f"SCREENING.md PARTITIONED row {node} must list multiple Cxxx IDs")
            if disposition in {"DEFERRED", "REJECTED"}:
                if ids or candidate_cell.strip().upper() not in {"", "NONE", "N/A"}:
                    self.error(f"SCREENING.md {disposition} row {node} must not list candidates")
                if not reason.strip():
                    self.error(f"SCREENING.md {disposition} row {node} lacks a reason")
            if disposition in {"CANDIDATE", "PARTITIONED"} and extra:
                self.error(f"SCREENING.md {node} has invalid candidate IDs")
            for candidate_id in ids:
                if candidate_id in listed_candidates:
                    self.error(f"SCREENING.md lists {candidate_id} more than once")
                listed_candidates[candidate_id] = node
        map_set = set(map_nodes)
        if set(seen) != map_set:
            missing = map_set - set(seen)
            extra = set(seen) - map_set
            if missing:
                self.error(f"SCREENING.md omits problem-map nodes: {', '.join(sorted(missing))}")
            if extra:
                self.error(f"SCREENING.md has nonexistent problem-map nodes: {', '.join(sorted(extra))}")
        actual = set(source_nodes)
        if set(listed_candidates) != actual:
            missing = actual - set(listed_candidates)
            extra = set(listed_candidates) - actual
            if missing:
                self.error(f"SCREENING.md omits generated candidates: {', '.join(sorted(missing))}")
            if extra:
                self.error(f"SCREENING.md references nonexistent candidates: {', '.join(sorted(extra))}")
        for candidate_id, node in source_nodes.items():
            if listed_candidates.get(candidate_id) != node:
                self.error(f"SCREENING.md source node disagrees with {candidate_id}: expected {node}")

    def validate_markdown_hygiene(self) -> None:
        paths = self.candidate_files()
        paths.extend(path for path in (ROOT / "literature/cards").glob("*.md") if path.name != "TEMPLATE.md")
        paths.extend([ROOT / "literature/INDEX.md", ROOT / "literature/PROBLEM_MAP.md"])
        paths.extend(path for path in (ROOT / "outputs").glob("*.md") if path.name != "README.md")
        for path in paths:
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            if SHELL_PREFIX.search("\n".join(text.splitlines()[:6])):
                self.error(f"captured shell/terminal output at start of {path.relative_to(ROOT)}")
            if re.search(r"\[\.\.\.\]|\bCxxx\b|\[Paper title\]", text):
                self.error(f"unresolved template placeholder in {path.relative_to(ROOT)}")

    def validate_pilot_selection(self, pilot_ids: set[str]) -> None:
        path = ROOT / "outputs/PILOT_SELECTION.md"
        if not path.is_file():
            self.error("pilot scarcity applies but outputs/PILOT_SELECTION.md is missing")
            return
        text = path.read_text(encoding="utf-8")
        headings = [
            "Eligible pilots", "Absolute threshold against RUN NO PILOT", "Pairwise comparison", "Selection",
            "Why run rather than no pilot", "Why no pilot", "Selected pilot stop criterion",
            "Selected pilot go criterion", "Claim permitted after success",
            "Claim permitted after a clean negative result", "Claim not permitted after either result",
        ]
        for heading in headings:
            if not self.section(text, heading):
                self.error(f"PILOT_SELECTION lacks non-empty section: {heading}")
        threshold = self.section(text, "Absolute threshold against RUN NO PILOT")
        if "RUN NO PILOT" not in threshold:
            self.error("PILOT_SELECTION absolute-threshold section must compare RUN NO PILOT")
        for candidate_id in pilot_ids:
            if candidate_id not in threshold:
                self.error(f"PILOT_SELECTION absolute-threshold section omits {candidate_id}")
        pairwise = self.section(text, "Pairwise comparison")
        if len(pilot_ids) < 2 and pairwise.strip() != "NOT APPLICABLE":
            self.error("PILOT_SELECTION pairwise comparison must be NOT APPLICABLE with fewer than two pilots")
        selection = self.section(text, "Selection")
        match = re.search(r"^SELECTED:[ \t]*(C\d{3}|RUN NO PILOT)\s*$", selection, re.MULTILINE)
        if not match:
            self.error("PILOT_SELECTION lacks a valid SELECTED value")
            return
        selected = match.group(1)
        if selected != "RUN NO PILOT" and selected not in pilot_ids:
            self.error(f"PILOT_SELECTION selects non-PILOT candidate: {selected}")
        if selected == "RUN NO PILOT":
            if self.section(text, "Why no pilot").strip().upper() == "NOT APPLICABLE":
                self.error("PILOT_SELECTION selecting RUN NO PILOT requires Why no pilot")
        elif self.section(text, "Why run rather than no pilot").strip().upper() == "NOT APPLICABLE":
            self.error("PILOT_SELECTION selecting a pilot requires Why run rather than no pilot")

    def validate_stage_artifacts(self, status: str, evidence_snapshot: str, completed: set[int], decisions: dict[str, str], candidate_contents: dict[str, str], source_nodes: dict[str, str]) -> None:
        index = self.text("literature/INDEX.md")
        problem_map = self.text("literature/PROBLEM_MAP.md")
        candidates = set(candidate_contents)
        map_nodes = re.findall(r"^#{1,6} (U\d+)\b", problem_map, re.MULTILINE)
        duplicates = {node for node in map_nodes if map_nodes.count(node) > 1}
        if duplicates:
            self.error(f"PROBLEM_MAP duplicates uncertainty nodes: {', '.join(sorted(duplicates))}")
        for candidate_id, node in source_nodes.items():
            if 6 in completed and node not in map_nodes:
                self.error(f"{candidate_id} cites missing problem-map node {node}")
        self.validate_screening(completed, map_nodes, source_nodes)

        index_status = re.search(r"^\*\*Status:\*\*[ \t]*(\S.*)$", index, re.MULTILINE)
        if 1 in completed:
            expected = "DISCOVERY_COMPLETE" if 2 in completed else "DISCOVERY_PASS_COMPLETE"
            if not index_status or index_status.group(1).strip() != expected:
                self.error(f"INDEX status must be {expected} for the completed discovery stages")
            for field in ("Topic", "Discovery date", "Literature cutoff / search date", "Broad query scope"):
                if not re.search(rf"^\*\*{re.escape(field)}:\*\*[ \t]+\S.*$", index, re.MULTILINE):
                    self.error(f"completed literature discovery lacks INDEX field: {field}")
        if 4 in completed and not [path for path in (ROOT / "literature/cards").glob("*.md") if path.name != "TEMPLATE.md"]:
            self.error("stage 4 claims completion but no generated paper card exists")
        if 6 in completed:
            if "**Status:** NOT_STARTED" in problem_map:
                self.error("stage 6 claims completion while PROBLEM_MAP status is NOT_STARTED")
            if not map_nodes:
                self.error("completed PROBLEM_MAP contains no structured Uxx node")
        if 8 in completed and candidates:
            if not re.fullmatch(r"sha256:[0-9a-f]{64}", evidence_snapshot):
                self.error("completed Round 1 requires EVIDENCE_SNAPSHOT in sha256 form")
            elif evidence_snapshot != self.evidence_snapshot():
                self.error("EVIDENCE_SNAPSHOT does not match the frozen Round-1 evidence manifest")

        final_path = ROOT / "outputs/FINAL_DECISION.md"
        if 14 in completed:
            if not final_path.is_file():
                self.error("stage 14 claims completion without outputs/FINAL_DECISION.md")
            else:
                final_text = final_path.read_text(encoding="utf-8")
                refs = set(re.findall(r"\bC\d{3}\b", final_text))
                if refs - candidates:
                    self.error(f"FINAL_DECISION references missing candidates: {', '.join(sorted(refs - candidates))}")
                if candidates and refs != candidates:
                    self.error(f"FINAL_DECISION omits candidates: {', '.join(sorted(candidates - refs))}")
                for candidate_id, decision in decisions.items():
                    if not any(decision in line for line in final_text.splitlines() if candidate_id in line):
                        self.error(f"FINAL_DECISION does not preserve {candidate_id} decision {decision}")

        funds = sum(decision == "FUND" for decision in decisions.values())
        pilot_ids = {candidate_id for candidate_id, decision in decisions.items() if decision == "PILOT ONLY"}
        scarcity_applies = bool(decisions) and funds == 0 and bool(pilot_ids)
        pilot_path = ROOT / "outputs/PILOT_SELECTION.md"
        if 15 in completed and scarcity_applies:
            self.validate_pilot_selection(pilot_ids)
        if 15 in completed and not scarcity_applies and pilot_path.exists():
            self.error("PILOT_SELECTION exists when scarcity selection is not applicable")
        if 16 in completed and status != "COMPLETE":
            self.error("stage 16 claims completion while STATUS is not COMPLETE")

    def run(self) -> int:
        self.require_layout()
        self.validate_toml()
        status, snapshot, _current, evidence_snapshot, completed = self.parse_state()
        self.validate_topic_snapshot(status, snapshot)
        self.validate_baseline_state(status, completed)
        decisions, contents, source_nodes = self.validate_candidates(completed)
        self.validate_cards(completed)
        self.validate_markdown_hygiene()
        self.validate_stage_artifacts(status, evidence_snapshot, completed, decisions, contents, source_nodes)
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
