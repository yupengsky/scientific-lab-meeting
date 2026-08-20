# Automatic Scientific Lab Meeting Workflow

This file defines the complete single-topic state machine. `AGENTS.md` is the scientific constitution. `RUN_STATE.md` is the interruption/resume checkpoint.

## Execution rules

The parent orchestrator automatically continues from every successful stage to the next. It does not request permission between normal stages. After each successful stage, it validates the relevant structure, marks the stage complete in `RUN_STATE.md`, and advances `CURRENT_STAGE`.

## Scratch and source-cache policy

Temporary source downloads may be stored only in ignored scratch roots: `tmp/`, `verification_tmp/`, `literature/source_pdfs/`, and `literature/source_text/`. They are never durable evidence. Durable evidence consists of index metadata, paper cards, original-source URLs and pointers, and candidate verification records.

At finalization, attempt best-effort cleanup of scratch material. If environment policy prevents deletion, record the residual ignored, untracked path in the Stage 16 notes. That residual does not block finalization unless it is referenced as a durable scientific artifact. Source verification remains permitted to use temporary downloads when needed.

Pause only when:

- a decision-critical evidence question cannot be resolved;
- required scholarly sources are inaccessible and continuation would require guessing;
- a tool failure prevents reliable continuation;
- repository integrity cannot be repaired safely;
- a defined terminal state is reached.

On resume:

1. read `RUN_STATE.md`;
2. verify the topic snapshot;
3. validate artifacts claimed by completed stages;
4. repair structural integrity failures when safe;
5. resume from the first incomplete stage.

If `STATUS` is not `NOT_STARTED` and the hash of `TOPIC.md` differs from `TOPIC_SNAPSHOT`, stop with:

`TOPIC CHANGED — CLEAN START BRANCH REQUIRED`

Never merge scientific state across topics. Never use Git history or another ref as scientific input.

## Persistent ownership

The parent orchestrator owns workflow state, index persistence, evidence-set selection, librarian assignments, candidate framing and files, insertion of read-only reviews, disagreement classification, rebuttal and verification routing, integrity checks, portfolio outputs, and pilot scarcity allocation.

The scout discovers literature only. Librarians compress assigned papers only. The mapper owns only `PROBLEM_MAP.md`. Each specialist critic owns only its independent judgment. Each skeptical PI owns one candidate-level decision. The parent mediates persistent writes from read-only agents.

## Stage 0 — WORKSPACE INITIALIZATION

1. Confirm this working tree represents one topic and `TOPIC.md` no longer contains the baseline instruction.
2. Read `AGENTS.md`, `WORKFLOW.md`, `TOPIC.md`, `RUN_STATE.md`, and the artifact templates.
3. Do not inspect Git history, branches, tags, or deleted scientific artifacts.
4. Set `STATUS: IN_PROGRESS`.
5. Store the exact `TOPIC.md` byte hash as `TOPIC_SNAPSHOT: sha256:<digest>`.
6. Confirm generated-artifact locations are empty or clean skeletons.
7. Run `python scripts/validate.py` and repair structural failures.

Success: the workspace is structurally valid and bound to one topic snapshot.

## Stage 1 — LITERATURE DISCOVERY

Spawn `literature_scout` for an initial broad-then-narrow pass. The scout returns structured discovery records to the parent and does not write files.

Discovery must:

- construct a provisional field map instead of an exhaustive bibliography;
- prefer published or accepted work for retrieval priority when relevance is comparable;
- treat publication status as metadata, never a truth criterion;
- include important preprints;
- seek competing explanations, contradictory evidence, negative results, failed replications, anomalies, critiques, and recent capabilities;
- apply no target paper count;
- stop at saturation, when more discovery is unlikely to materially change the provisional map.

For every record return title, authors, year, publication status and venue, stable source URL or identifier, compact abstract-level description, relevance, evidence role, classification, reading availability, and any metadata uncertainty.

The parent deduplicates records and writes `literature/INDEX.md`, including topic, discovery date, literature cutoff/search date, broad query scope, classification, source URL, evidence role, and card path when later available. When Stage 1 records are persisted, set the index status to `DISCOVERY_PASS_COMPLETE`. This is the valid resumable state before Stage 2.

## Stage 2 — COVERAGE CHALLENGE

Run a targeted scout challenge against the provisional map. Ask which missing evidence could materially change it. Challenge specifically for:

- missing explanatory families;
- contradictory evidence;
- negative results;
- replication failures;
- missing scope regimes;
- recent capabilities.

Do not run another generic broad search. Zero added papers is valid. The parent merges and deduplicates returned records and records the coverage assessment and saturation judgment in `INDEX.md`.

When the coverage challenge is persisted, set the index status to `DISCOVERY_COMPLETE`.

## Stage 3 — MINIMUM SUFFICIENT EVIDENCE SET

The parent selects the smallest set of papers whose removal would materially weaken the ability to determine:

- established phenomena;
- competing or compatible explanations;
- causal versus correlational evidence;
- limiting evidence;
- scope limitations;
- important confounds;
- recent capability changes.

Select CORE and only high-leverage SUPPORTING papers. Do not card every discovered paper. Persist selections through the index classification and card-path fields.

## Stage 4 — TARGETED PAPER CARDS

Assign selected papers to `librarian` with unique, non-overlapping card filenames. Each librarian reads only assigned sources and creates one card per paper from `literature/cards/TEMPLATE.md`.

Required reading states are `FULL_TEXT`, `PARTIAL`, and `ABSTRACT_ONLY`. `FULL_TEXT` requires actual inspection of the relevant full text.

For important claims, cards explicitly separate:

- `OBSERVATION`;
- `AUTHOR INTERPRETATION`;
- `INFERENCE`.

Cards record the scientific question, exact system/model/organism/regime, intervention or measurement, observed result, causal strength, controls, unexcluded alternatives, scope limits, source URL, and section/figure/page pointers when available. The parent updates card paths in `INDEX.md`.

## Stage 5 — EVIDENCE SUFFICIENCY / TARGETED REPAIR

Before mapping, identify high-leverage claims resting on `ABSTRACT_ONLY`, `PARTIAL`, inaccessible, or otherwise weak inspection.

Repair only claims whose resolution could materially change the problem map. Use original scholarly sources. Do not broadly reread the corpus. Update the relevant cards and index metadata. If a decision-critical mapping claim remains inaccessible and guessing would be required, pause.

## Stage 6 — PROBLEM MAP

Run `literature_mapper` over `TOPIC.md`, `INDEX.md`, and current paper cards. A populated prior map is never required. The mapper writes only `literature/PROBLEM_MAP.md`.

The map must:

- separate distinct phenomena hidden under umbrella terminology;
- separate explanatory levels;
- classify relations as `MUTUALLY EXCLUSIVE`, `PARTIALLY COMPETING`, `COMPATIBLE`, `COMPOSITIONAL`, `DIFFERENT LEVELS OF EXPLANATION`, or `RELATION UNKNOWN`;
- prevent scope leakage;
- distinguish correlation, intervention, and causal evidence;
- challenge coherent composite stories instead of adopting them automatically;
- end in structured, traceable Uxx uncertainty nodes;
- contain no project proposals.

## Stage 7 — CANDIDATE GENERATION

The parent frames candidates only from explicit Uxx nodes and writes `candidates/Cxxx.md` using the candidate template. Broad nodes may be partitioned. Before freezing Round-1 evidence, write `candidates/SCREENING.md` with exactly one row for every Uxx node in `PROBLEM_MAP.md`:

| Uxx | Disposition | Reason | Candidate(s) |
|---|---|---|---|

Allowed dispositions are `CANDIDATE`, `PARTITIONED`, `DEFERRED`, and `REJECTED`. `CANDIDATE` produces one Cxxx; `PARTITIONED` produces multiple narrower Cxxx candidates; `DEFERRED` records a scientifically real uncertainty without a sufficiently discriminating or tractable candidate; and `REJECTED` records an apparent uncertainty that fails the candidate gate. For `CANDIDATE` and `PARTITIONED`, list the actual Cxxx IDs. For `DEFERRED` and `REJECTED`, record one main scientific reason. This screening audit is not critic input or a scientific evidence source.

Do not free-form brainstorm, impose a count, or create candidates for novelty, method-to-system application, another benchmark, another dataset, an answered question, or explanations at different levels without a possible discriminator.

The construct-validity section must state the scientific construct the proposed discriminator is intended to identify, implementation-level alternatives that could generate the same outcome, and what the experiment would not identify even if successful. An implementation alternative alone does not reject a candidate. If the proposed discriminator cannot distinguish the stated uncertainty from implementation effects, narrow the scientific claim, redesign the discriminator, or do not promote the Uxx node.

Zero candidates is a valid terminal scientific result. Document that result in `outputs/FINAL_DECISION.md`, record `SKIPPED — ZERO CANDIDATES` for inapplicable review and PI stages in the run-state notes, mark those stages complete, advance through final validation, set `STATUS: COMPLETE`, and stop.

Run `python scripts/validate.py` after candidate generation.

## Stage 8 — ROUND-1 BLIND CRITICS

Freeze the eligible evidence state before launching reviews. Store `EVIDENCE_SNAPSHOT: sha256:<digest>` in `RUN_STATE.md`; use `python scripts/validate.py --print-evidence-snapshot` to compute the digest. It covers the index, problem map, generated cards, and the scientific-framing portion of every candidate before `# Lab meeting`. Do not modify those frozen inputs after Round 1. Decision-critical verification findings are appended inside candidate lab-meeting sections.

For every candidate, run hamming, medawar, platt, and alon independently. Each receives the same eligible evidence snapshot:

- target candidate;
- `PROBLEM_MAP.md`;
- relevant paper cards;
- `INDEX.md` only when necessary.

No critic receives another critic's review or verdict, or parent synthesis of another review. Apply no consensus pressure. The parent persists each returned review verbatim inside its matching candidate section. It may indent or Markdown-fence the response, preserving complete textual content. It must not summarize, shorten, rewrite, normalize verdict wording, merge fields, or replace a structured review with prose.

Run `python scripts/validate.py` after Round 1.

## Stage 9 — REVIEW INTEGRITY CHECK

For every candidate, verify complete, structurally intact Hamming, Medawar, Platt, and Alon sections. If one is missing or corrupted, rerun only that critic under the original blind evidence snapshot. Do not begin debate with an incomplete Round-1 record.

## Stage 10 — TARGETED REBUTTAL

The parent classifies review disagreements as `NONE`, `APPARENT`, or `SUBSTANTIVE` and records the classification. It compares the substantive claims in the complete reviews before writing `NONE`; same or compatible top-level verdicts alone do not establish agreement. Compare at least the central uncertainty, whether the tractable version preserves the important question, whether the experiment discriminates, whether a pilot is hypothesis-reducing rather than feasibility-only, what a negative result eliminates, fatal assumptions, and whether verification is decision-critical. Do not manufacture disagreement when those claims are genuinely aligned.

Route rebuttal only for substantive disagreements and only to involved critics. Each receives:

- its own original review;
- the strongest opposing argument;
- relevant eligible evidence.

Critics may change verdicts. Do not pressure them to defend prior positions. Preserve genuine disagreement. A cheap experiment with ambiguous outcomes is not a high-value pilot.

## Stage 11 — DECISION-CRITICAL EVIDENCE VERIFICATION

Separate unresolved items into:

- `SOURCE-VERIFIABLE EVIDENCE`: factual questions about existing work;
- `DESIGN REQUIREMENT`: conditions a future study must satisfy.

Rereading papers cannot resolve design requirements. Verify only decision-critical source claims, using original scholarly sources. Record each finding in the candidate as `VERIFIED`, `PARTIALLY VERIFIED`, `NOT SUPPORTED`, or `INCONCLUSIVE`, with a source and precise pointer. Never convert `INCONCLUSIVE` into inference.

Set each candidate's `VERIFICATION_STATUS` to exactly `COMPLETE`, `NONE REQUIRED`, or `BLOCKED`. `COMPLETE` means all decision-critical source verification was resolved and recorded. `NONE REQUIRED` means no decision-critical source claim required verification. `BLOCKED` means unresolved source evidence prevents reliable continuation.

## Stage 12 — PI READINESS GATE

Classify every candidate as:

- `READY FOR PI`; or
- `DECISION BLOCKED — EVIDENCE STILL UNRESOLVED`.

Design requirements alone do not block PI. Run `python scripts/validate.py` before PI routing. Pause if a decision-critical source question remains unresolved.

## Stage 13 — INDEPENDENT SKEPTICAL PI

Use a separate `skeptical_pi` instance for every ready candidate. Each receives:

- the complete target candidate record;
- verified evidence;
- relevant problem-map context;
- other candidate files only as opportunity-cost alternatives.

A PI never receives another PI verdict. The parent persists the complete skeptical-PI response verbatim in the target candidate. It may indent or Markdown-fence the response, preserving complete textual content. It must not compress the response to a decision and synopsis, rewrite it, or merge fields.

Allowed decisions: `FUND`, `PILOT ONLY`, `REDESIGN`, `KILL`, `DECISION BLOCKED — VERIFY EVIDENCE`.

`PILOT ONLY` is a strict scientific decision, never a safe middle category. A valid pilot is bounded, tractable, hypothesis-reducing, interpretable, and equipped with explicit stop/go criteria. Feasibility-only work is insufficient. Do not use `REDESIGN` to avoid `KILL`. A fatal flaw may dominate positive dimensions. `FUND NONE` is valid.

## Stage 14 — FINAL PORTFOLIO DECISION

After all independent PI decisions, the parent writes `outputs/FINAL_DECISION.md` containing:

- PI decision matrix;
- FUND candidates;
- PILOT ONLY candidates;
- REDESIGN candidates;
- KILL candidates;
- fatal flaws;
- decisive next steps.

Never promote `PILOT ONLY` to `FUND` because no candidate was funded. Explicitly allow: `NO CANDIDATE CURRENTLY JUSTIFIES SUBSTANTIAL RESEARCH EFFORT.`

## Stage 15 — PILOT SCARCITY SELECTION

This stage applies when FUND count is zero and PILOT ONLY count is at least one. The parent assumes resources for at most one pilot and may select `RUN NO PILOT`. Every eligible pilot competes against `RUN NO PILOT`, including when exactly one eligible pilot exists. Sole eligibility never establishes selection.

Compare eligible pilots on:

- importance preserved by the bounded pilot;
- discrimination strength;
- expected uncertainty reduction;
- negative-result value;
- interpretability;
- tractability;
- cost and technical risk.

Scientific information value precedes cheapness. For each eligible pilot, explicitly decide whether expected scientific information gain sufficiently exceeds cost, ambiguity, and technical risk to clear the no-action threshold. Write `outputs/PILOT_SELECTION.md` with this structure:

# Pilot Scarcity Selection

## Eligible pilots

## Absolute threshold against RUN NO PILOT

## Pairwise comparison

Use this only for two or more eligible pilots; otherwise write `NOT APPLICABLE`.

## Selection

Write exactly `SELECTED: Cxxx` or `SELECTED: RUN NO PILOT`.

## Why run rather than no pilot

Required when a pilot is selected.

## Why no pilot

Required when `RUN NO PILOT` is selected.

## Selected pilot stop criterion

## Selected pilot go criterion

## Claim permitted after success

## Claim permitted after a clean negative result

## Claim not permitted after either result

When `RUN NO PILOT` is selected, the selected-pilot sections may say `NOT APPLICABLE`. Use no new custom agent.

When the trigger is false, record the stage as completed and do not create `PILOT_SELECTION.md`.

## Stage 16 — FINAL VALIDATION

1. Run `python scripts/validate.py`.
2. Repair every structural failure before finalization.
3. Confirm authoritative output consistency with candidate PI decisions.
4. Set `STATUS: COMPLETE`, mark Stage 16 complete, and retain `CURRENT_STAGE: FINAL_VALIDATION`.
5. Run `python scripts/validate.py` again against the finalized state.
6. Attempt scratch cleanup and record any permitted residual path in Stage 16 notes.
7. Report the scientific terminal result and any unresolved evidence explicitly.

The validator performs no scientific judgment. Scientific uncertainty, disagreement, `FUND NONE`, zero candidates, and `RUN NO PILOT` are valid outcomes.
