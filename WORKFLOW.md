# Automatic Expertise-First Scientific Lab Meeting Workflow

`AGENTS.md` governs scientific integrity. `RUN_STATE.md` is the resumable checkpoint. This workflow begins only in a fresh Codex session after topic scoping has ended; its scientific inputs are `TOPIC.md`, current-tree artifacts, and public scholarly sources.

## Execution and routing rules

The parent orchestrator advances automatically after each successful stage, validates structure, records completion and the next stage in `RUN_STATE.md`, and loops back when a gate requires more evidence. Do not use generic inheriting worker/explorer agents for scientific retrieval, extraction, mapping, framing, novelty assessment, critic, or PI work. Use the named custom role with its configured model and `model_reasoning_effort`. If that pinned role cannot run with its configured profile, stop; do not fall back to the parent model.

The parent owns durable writes except mapper-owned `PROBLEM_MAP.md` and librarian-owned assigned cards. Scouts transport retrieval and metadata; librarians faithfully compress individual sources; reasoning roles synthesize from durable records. The parent must preserve specialist outputs rather than replacing them with scientific paraphrase.

Pause only for decision-critical inaccessible evidence, failed pinned-agent routing, tool failure, unrepaired integrity failure, or a terminal state. On resume, verify the topic hash and completed artifacts, then resume at the first incomplete stage. A started run whose `TOPIC.md` hash differs from `TOPIC_SNAPSHOT` stops with `TOPIC CHANGED — CLEAN START BRANCH REQUIRED`.

## Stage 0 — WORKSPACE INITIALIZATION

Confirm the baseline topic placeholder has been replaced; read protocol/templates; set `STATUS: IN_PROGRESS`; record exact `TOPIC_SNAPSHOT`; confirm generated locations are clean; run validation. Do not inspect history, branches, deleted artifacts, or other topics.

## Stage 1 — BROAD FIELD DISCOVERY

Run repeated `literature_scout` passes with independent scopes: taxonomy/terminology; foundational/canonical work; explanatory families; backward lineage; direct follow-ups/rebuttals; contradictions, limiting evidence, negative results, and replications; alternative terminology; directly bearing adjacent literatures; and recent frontier/capability changes. Persist the deduplicated field corpus in `INDEX.md`. No paper-count target applies; every discovered paper need not get a card. Set index status `BROAD_DISCOVERY_COMPLETE`.

## Stage 2 — STRUCTURAL COVERAGE EXPANSION

Use scouts to fill gaps exposed by the corpus and create/update `COVERAGE.md` for every major explanatory family. Challenge weak family support, absent competing accounts, contradiction searches, follow-up/rebuttal searches, and frontier searches. Persist explicit gaps and set index status `STRUCTURAL_EXPANSION_COMPLETE`.

## Stage 3 — FIELD SATURATION GATE

Pass only when each major family has multiple meaningful support sources or is explicitly sparse and therefore not mature; competing explanations have adequate primary evidence; important claims were actively challenged; anchor follow-ups/rebuttals and recent capability work were searched; no major family's key evidence is predominantly abstract-only/weak partial; and a final targeted coverage challenge adds no new major family, fatal scope boundary, or map-changing evidence. Mark each family `READY` or `NOT READY` in `COVERAGE.md`. If any required gap is `NOT READY`, record exact search gaps and return to Stage 2. Never pass because results look repetitive. Set index status `FIELD_SATURATED` only after passing.

## Stage 4 — HIGH-LEVERAGE EVIDENCE SELECTION + PAPER CARDS

Select CORE and high-leverage SUPPORTING evidence needed to preserve field structure, competing accounts, limitations, causal strength, scope, and recent capabilities. Assign non-overlapping cards to `librarian`. Cards require identity verification against INDEX and reading-depth recording. `INDEX.md` remains the field corpus; cards are a high-leverage layer.

## Stage 5 — EVIDENCE IDENTITY / DEPTH REPAIR

Repair or exclude MISMATCH/UNRESOLVED cards. Repair decision-relevant abstract-only/partial depth with original sources where accessible. Only VERIFIED cards may support map, Uxx saturation, framing, or frozen evidence. Pause if a decision-critical claim remains inaccessible and would require guessing.

## Stage 6 — DEFINITIVE PROBLEM MAP

Run `literature_mapper` over TOPIC, INDEX, COVERAGE, and VERIFIED cards. It writes the definitive traceable map with structured Uxx nodes and no project proposals.

## Stage 7 — Uxx-SPECIFIC LITERATURE SATURATION

For every decision-relevant Uxx, run targeted scout/reading loops for supporting evidence, serious competing explanations, contradictory/limiting evidence, direct follow-ups/rebuttals, recent capability changes, and sufficient primary evidence on all sides of any mechanism comparison. Update the Uxx coverage record. Do not let a mechanism A-vs-B candidate proceed if one side rests mainly on one weak or abstract source.

## Stage 8 — Uxx SATURATION GATE

Mark every Uxx `READY` or `NOT READY` with exact missing coverage. Only READY nodes may be framed. If targeted prior art changes/resolves the map, return to Stage 6 or Stage 7 as appropriate. NOT READY is valid.

## Stage 9 — CANDIDATE GENERATION + SCREENING

For each READY Uxx, run `candidate_framer` independently with that node, relevant VERIFIED cards, and map context. The parent writes candidate files from the returned framing and records every Uxx in `SCREENING.md`, including NOT READY, deferred, rejected, candidate, and partitioned dispositions. No fixed count; zero candidates is valid.

## Stage 10 — CANDIDATE PRIOR-ART / NOVELTY SATURATION

For every candidate, use `literature_scout` for a fresh search of the exact question, competing hypotheses, discriminator, nearest design, alternative terms, direct citations/follow-ups, and recent frontier work. Use `novelty_auditor` independently to classify and complete the candidate novelty audit. Require `NOVELTY SATURATION: PASS`. If prior art materially changes the map or resolves the Uxx, loop to Stage 6–9 before freezing evidence. An old question may survive as reconciliation, boundary, or new-discriminator work; never label it new silently.

## Stage 11 — ROUND-1 BLIND CRITICS

Freeze eligible evidence with `EVIDENCE_SNAPSHOT`. For every candidate run hamming, medawar, platt, and alon independently with the same snapshot and no other critic output. Persist responses verbatim. Validate afterward.

## Stage 12 — REVIEW INTEGRITY + TARGETED REBUTTAL

Repair missing/corrupt reviews under the frozen snapshot. Classify only substantive disagreements and route only those to involved critics with their own review, strongest opposing argument, and eligible evidence. Preserve genuine disagreement.

## Stage 13 — DECISION-CRITICAL VERIFICATION + PI READINESS

Separate source-verifiable questions from future design requirements. Verify only decision-critical source claims against original sources and record outcomes. Mark each candidate `READY FOR PI` or `DECISION BLOCKED — EVIDENCE STILL UNRESOLVED`; design requirements alone do not block. Pause on blocked source evidence.

## Stage 14 — INDEPENDENT SKEPTICAL PI

Use a separate `skeptical_pi` instance for each ready candidate. Persist the complete response verbatim. Allowed decisions: FUND, PILOT ONLY, REDESIGN, KILL, or DECISION BLOCKED — VERIFY EVIDENCE. `PILOT ONLY` requires a substantive discriminator and stop/go criteria; `KILL` may mark pilot fields `NOT APPLICABLE — fatal flaw is not pilot-resolvable`.

## Stage 15 — PORTFOLIO + PILOT SCARCITY

Write `outputs/EXPERT_BRIEF.md`, `outputs/RESEARCH_QUESTIONS.md`, and `outputs/FINAL_DECISION.md`. The expert brief covers field structure, families, lineages, established knowledge, disagreements, negative results, scope, capability changes, mature-looking-open lines, and genuine unresolved areas. Research questions records every surviving or interesting question with scientific question, novelty type, closest prior work, importance, unresolvedness, discriminator, why now, failure reason, and meeting decision. When no candidate is funded, this remains a useful question-centered output. Create `PILOT_SELECTION.md` only when no candidate is funded and one or more are PILOT ONLY; compare every pilot against RUN NO PILOT.

## Stage 16 — FINAL VALIDATION

Run `python scripts/validate.py`, repair structural failures, check output/candidate consistency, set `STATUS: COMPLETE`, retain `CURRENT_STAGE: FINAL_VALIDATION`, validate again, and clean ignored scratch material best-effort. The validator does not judge scientific quality. `FUND NONE`, zero candidates, NOT READY nodes, disagreement, and RUN NO PILOT are valid outcomes.
