# Scientific Lab Meeting

A reusable Codex workspace for discovering and evaluating scientific research problems from one broad research direction.

## Start a run

1. Create a new branch from the clean `start` branch.
2. Edit `TOPIC.md` with one broad scientific direction.
3. Open a fresh Codex session in that working tree.
4. Give Codex this single instruction:

> Read TOPIC.md and run the complete workflow defined by AGENTS.md and WORKFLOW.md.
>
> Start from public scientific evidence for this topic. Do not use Git history, other branches, previous experiments, or user scientific priors as scientific input.
>
> Continue automatically until a terminal state or a genuinely blocking condition is reached.

Normal runs require no intermediate user prompts.

## Main artifacts

```text
TOPIC.md
  -> literature/INDEX.md
  -> literature/cards/
  -> literature/PROBLEM_MAP.md
  -> candidates/Cxxx.md
  -> outputs/FINAL_DECISION.md
  -> outputs/PILOT_SELECTION.md  (only when applicable)
```

`RUN_STATE.md` supports interruption and resume within the same topic. Use a fresh branch from `start` for every different topic.
