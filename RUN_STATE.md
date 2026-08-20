# Run State

STATUS: NOT_STARTED
TOPIC_SNAPSHOT:
CURRENT_STAGE: WORKSPACE_INITIALIZATION
EVIDENCE_SNAPSHOT:

## Stage completion

- [ ] 0. WORKSPACE INITIALIZATION
- [ ] 1. LITERATURE DISCOVERY
- [ ] 2. COVERAGE CHALLENGE
- [ ] 3. MINIMUM SUFFICIENT EVIDENCE SET
- [ ] 4. TARGETED PAPER CARDS
- [ ] 5. EVIDENCE SUFFICIENCY / TARGETED REPAIR
- [ ] 6. PROBLEM MAP
- [ ] 7. CANDIDATE GENERATION
- [ ] 8. ROUND-1 BLIND CRITICS
- [ ] 9. REVIEW INTEGRITY CHECK
- [ ] 10. TARGETED REBUTTAL
- [ ] 11. DECISION-CRITICAL EVIDENCE VERIFICATION
- [ ] 12. PI READINESS GATE
- [ ] 13. INDEPENDENT SKEPTICAL PI
- [ ] 14. FINAL PORTFOLIO DECISION
- [ ] 15. PILOT SCARCITY SELECTION
- [ ] 16. FINAL VALIDATION

## Stage notes

Record only blocking, repair, or explicitly skipped-stage facts needed for reliable resume.

## State rules

- At initialization, set `TOPIC_SNAPSHOT` to `sha256:` followed by the SHA-256 of the exact `TOPIC.md` bytes.
- Before every resumed stage, compare `TOPIC.md` with `TOPIC_SNAPSHOT`.
- If they differ after the run has started, stop with `TOPIC CHANGED — CLEAN START BRANCH REQUIRED`.
- Before Round 1, set `EVIDENCE_SNAPSHOT` from `python scripts/validate.py --print-evidence-snapshot`. It hashes the index, problem map, generated cards, and candidate scientific framing before `# Lab meeting`.
- Mark a stage complete only after its artifacts pass the required integrity gate.
- On resume, verify completed stages and continue from the first incomplete stage.
