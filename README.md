# Scientific Lab Meeting

A reusable Codex workspace for discovering and evaluating scientific research problems from one broad research direction.

## A. Scope a topic interactively

Start a Codex session in a clean working tree and give it:

> Use the `topic_advisor` agent to help me choose one neutral scientific research direction. Do not start WORKFLOW.md or create literature artifacts. When we agree, write only the final neutral direction to TOPIC.md.

The topic-scoping conversation must end before the scientific run begins. It must not be carried into the next session.

## B. Run the full research workflow in a fresh session

1. Create a new branch from the clean `start` branch.
2. Complete topic scoping and retain only the neutral direction in `TOPIC.md`.
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
  -> literature/COVERAGE.md
  -> literature/cards/
  -> literature/PROBLEM_MAP.md
  -> candidates/Cxxx.md
  -> outputs/EXPERT_BRIEF.md
  -> outputs/RESEARCH_QUESTIONS.md
  -> outputs/FINAL_DECISION.md
  -> outputs/PILOT_SELECTION.md  (only when applicable)
```

`RUN_STATE.md` supports interruption and resume within the same topic. Use a fresh branch from `start` for every different topic.
