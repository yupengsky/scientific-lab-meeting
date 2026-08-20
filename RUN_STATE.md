# Run State

STATUS: COMPLETE
TOPIC_SNAPSHOT: sha256:e106db55c25d2d385d329ac6e41bf6d31f2fc000e88a896280b14302cb7d089e
CURRENT_STAGE: FINAL_VALIDATION
EVIDENCE_SNAPSHOT: sha256:77a945c0176b59df1878e93a6a50fd73c5da920bc281d3469462ed053bd356c5

## Stage completion

- [x] 0. WORKSPACE INITIALIZATION
- [x] 1. LITERATURE DISCOVERY
- [x] 2. COVERAGE CHALLENGE
- [x] 3. MINIMUM SUFFICIENT EVIDENCE SET
- [x] 4. TARGETED PAPER CARDS
- [x] 5. EVIDENCE SUFFICIENCY / TARGETED REPAIR
- [x] 6. PROBLEM MAP
- [x] 7. CANDIDATE GENERATION
- [x] 8. ROUND-1 BLIND CRITICS
- [x] 9. REVIEW INTEGRITY CHECK
- [x] 10. TARGETED REBUTTAL
- [x] 11. DECISION-CRITICAL EVIDENCE VERIFICATION
- [x] 12. PI READINESS GATE
- [x] 13. INDEPENDENT SKEPTICAL PI
- [x] 14. FINAL PORTFOLIO DECISION
- [x] 15. PILOT SCARCITY SELECTION
- [x] 16. FINAL VALIDATION

## Stage notes

Record only blocking, repair, or explicitly skipped-stage facts needed for reliable resume.

- Stage 15: SKIPPED — no candidate received PILOT ONLY.
- Stage 16: Final structural validation passed. No workflow scratch roots were present for cleanup.

## State rules

- At initialization, set `TOPIC_SNAPSHOT` to `sha256:` followed by the SHA-256 of the exact `TOPIC.md` bytes.
- Before every resumed stage, compare `TOPIC.md` with `TOPIC_SNAPSHOT`.
- If they differ after the run has started, stop with `TOPIC CHANGED — CLEAN START BRANCH REQUIRED`.
- Before Round 1, set `EVIDENCE_SNAPSHOT` from `python scripts/validate.py --print-evidence-snapshot`. It hashes the index, problem map, generated cards, and candidate scientific framing before `# Lab meeting`.
- Mark a stage complete only after its artifacts pass the required integrity gate.
- On resume, verify completed stages and continue from the first incomplete stage.
