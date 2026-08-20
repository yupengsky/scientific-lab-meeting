# Scientific Lab Meeting

A reusable Codex workspace for discovering and evaluating high-value scientific research problems from a broad research direction.

## Workflow

```text
TOPIC.md
  ↓
literature_scout → literature/INDEX.md
  ↓
librarian → literature/cards/
  ↓
literature_mapper → literature/PROBLEM_MAP.md
  ↓
candidate problems
  ↓
Hamming / Medawar / Platt / Alon
  ↓
Skeptical PI
```

Edit `TOPIC.md`, then ask Codex:

> Read TOPIC.md. Run the complete literature discovery and scientific problem-finding workflow defined in AGENTS.md. Start from public scientific literature. Do not ask me for papers or scientific priors.

The scout searches arXiv and scholarly web sources. Librarians create traceable cards from selected paper URLs. Original sources are revisited only when a decision requires verification.
