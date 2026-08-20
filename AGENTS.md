# Scientific Lab Meeting Protocol

The user provides only a broad research direction through `TOPIC.md`. Do not infer that the topic implies a preferred theory, hypothesis, method, paper, or conclusion.

## Evidence hierarchy

Use:

1. `literature/PROBLEM_MAP.md`
2. `literature/INDEX.md`
3. relevant `literature/cards/*.md`
4. the original arXiv, publisher, or proceedings source when verification is important

Paper cards are compressed evidence. Original scholarly sources are consulted selectively. Never pretend an abstract-only reading is a full-text review.

## Literature workflow

1. Read `TOPIC.md`.
2. Spawn `literature_scout` to search arXiv and the scholarly web broadly.
3. Update `literature/INDEX.md` with lightweight discovery records.
4. Send CORE and important SUPPORTING papers to `librarian`.
5. Spawn `literature_mapper` to update `literature/PROBLEM_MAP.md`.
6. Generate candidates only after the problem map exists.

The scout discovers literature. The librarian reads specified scholarly sources and creates cards. The mapper synthesizes cards. None of these agents should generate research ideas during their assigned stages.

## Evidence discipline

Distinguish ESTABLISHED FACT, AUTHOR CLAIM, OBSERVATION, INFERENCE, and SPECULATION. Critics operate over the curated evidence state. If a conclusion depends on an uncertain detail, mark `NEEDS_VERIFICATION` with the paper and detail. Do not resolve uncertainty by guessing.

## Lab meeting

Run `hamming`, `medawar`, `platt`, and `alon` independently and blindly for the first round. Preserve real disagreements, then run targeted rebuttals. Finally send the complete case to `skeptical_pi`.

The PI must return `FUND`, `PILOT ONLY`, `REDESIGN`, `KILL`, or `DECISION BLOCKED — VERIFY EVIDENCE`.

Do not reward novelty alone, technical difficulty, or complexity. Prefer decisive experiments whose outcomes reduce scientific uncertainty.
