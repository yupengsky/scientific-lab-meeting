# Scientific Lab Meeting Protocol

This repository runs one scientific topic per working tree. `TOPIC.md` supplies a broad research direction. Do not infer a preferred theory, hypothesis, method, paper, or conclusion.

## Scientific input isolation

Scientific reasoning for a run may use only:

1. `TOPIC.md`;
2. scientific artifacts generated in the current working tree;
3. public scholarly sources relevant to the current topic.

Do not inspect or use Git history, deleted files, `main`, other branches, tags, previous dry-run candidates, previous literature selections, previous PI decisions, or previous pilot selections as scientific input. Git history is protocol provenance only.

One working tree represents exactly one scientific topic. Test a different topic from a fresh branch created from the clean `start` baseline. If a started run's topic snapshot differs from `TOPIC.md`, stop with `TOPIC CHANGED — CLEAN START BRANCH REQUIRED`.

## Automatic orchestration

The parent orchestrator owns the workflow and follows `WORKFLOW.md`. It continues automatically between successful stages and updates `RUN_STATE.md` after every stage. Normal stages require no user permission.

Pause only for a blocking condition defined in `WORKFLOW.md` or a defined terminal state. On resume, validate completed-stage artifacts and continue from the first incomplete stage.

## Ownership

- **Parent orchestrator:** workflow state; `literature/INDEX.md`; evidence-set selection; librarian assignments; candidate framing and files; insertion of read-only critic results; disagreement detection and rebuttal routing; evidence-verification routing; integrity validation; `outputs/FINAL_DECISION.md`; optional `outputs/PILOT_SELECTION.md`; pilot scarcity allocation.
- **literature_scout:** read-only literature discovery, classification, coverage assessment, and saturation judgment. It returns structured records to the parent.
- **librarian:** assigned-paper evidence compression into `literature/cards/` only.
- **literature_mapper:** `literature/PROBLEM_MAP.md` only.
- **hamming / medawar / platt / alon:** independent candidate-level scientific judgments only.
- **skeptical_pi:** one candidate-level final scientific decision.

The parent mediates every persistent write produced by a read-only agent.

## Evidence discipline

Use this evidence hierarchy:

1. `literature/PROBLEM_MAP.md`
2. `literature/INDEX.md`
3. relevant `literature/cards/*.md`
4. original arXiv, publisher, or proceedings sources when verification matters

Distinguish ESTABLISHED FACT, AUTHOR CLAIM, OBSERVATION, INFERENCE, and SPECULATION. Paper cards are compressed evidence. Never represent abstract-only reading as full-text review. Mark decision-relevant uncertainty `NEEDS_VERIFICATION` with the source and exact detail. Never resolve uncertainty by guessing.

## Candidate gate

Generate candidates only from explicit Uxx uncertainty nodes in `literature/PROBLEM_MAP.md`. Every candidate cites its source node and uses `candidates/TEMPLATE.md`. Candidates may refine or partition a broad node.

Do not create a candidate for novelty alone, applying a method to a new system, another benchmark or dataset, a question already answered, or explanations at different levels without a possible discriminator. Do not impose a candidate count. Zero candidates is a valid terminal scientific result.

## Lab meeting

Freeze one eligible evidence snapshot, then run hamming, medawar, platt, and alon independently and blindly for every candidate. Each receives the same eligible evidence state and sees no other critic output.

Validate all four reviews before debate. Route only substantive disagreements to targeted rebuttal. Verify only decision-critical source claims against original scholarly sources. Keep design requirements separate from source-verifiable questions.

Run a separate skeptical PI instance for each ready candidate. Allowed decisions are `FUND`, `PILOT ONLY`, `REDESIGN`, `KILL`, and `DECISION BLOCKED — VERIFY EVIDENCE`. A fatal flaw may dominate other dimensions. `FUND NONE` is valid.

Use `outputs/FINAL_DECISION.md` for the cross-candidate decision. Create `outputs/PILOT_SELECTION.md` only when scarcity selection applies. Do not use dated output filenames for the normal pipeline.

## Integrity

Run `python scripts/validate.py` at the gates specified in `WORKFLOW.md`. The validator checks structure only. Repair structural failures before continuing. Do not overwrite template files.
