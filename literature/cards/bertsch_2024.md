# In-Context Learning with Long-Context Models: An In-Depth Exploration

## Metadata
**Authors:** Amanda Bertsch, Maor Ivgi, Uri Alon, Jonathan Berant, Matthew R. Gormley, Graham Neubig
**Year:** 2024
**arXiv:** https://arxiv.org/abs/2405.00200
**Published venue:** PREPRINT
**DOI:** UNCLEAR
**Publisher / proceedings:** arXiv
**Publication status:** PREPRINT
**Reading status:** PARTIAL

## Abstract
The paper studies ICL with hundreds or thousands of demonstrations and compares it with retrieval and fine-tuning.

## Scientific question
What changes when ICL operates at long context lengths approaching training-set scale?

## Main claims
- **AUTHOR CLAIM:** For many large-label-space datasets, performance continues improving with hundreds or thousands of examples.
- **AUTHOR CLAIM:** Most gains arise from attending to similar examples rather than cumulative task learning.

## Key observations
- Long-context ICL improves with more demonstrations; retrieval has strong low-context performance with diminishing gains; fine-tuning is more data hungry but can exceed ICL with more data. Long-context ICL is less sensitive to shuffling, while grouping same-label examples can hurt.

## Evidence for major claims
- **OBSERVATION:** Accuracy curves and comparisons across datasets/models show the reported scaling and method differences.
- **AUTHOR INTERPRETATION:** Similar-example attention explains most long-context gains; gains are not simply additive encoding of all examples.

## Observation vs interpretation
### Observed / demonstrated
- Performance varies with context length, ordering, grouping, retrieval, and fine-tuning baselines.
### Author interpretation
- Long-context ICL behaves primarily as similarity-based use of demonstrations rather than full task induction.

## Important controls
- Random shuffling, same-label grouping, retrieval, and fine-tuning comparisons.

## Critical assumptions
- Benchmark performance and perturbations diagnose whether examples are used by retrieval or task learning.

## Remaining alternative explanations
- Similarity attention and task learning may coexist; ordering effects may reflect positional/formatting artifacts.

## Limitations
- Conclusions depend on selected datasets, models, prompts, and feasible context windows; “most” gains are not a universal quantitative bound.

## What this paper supports
- Long contexts can materially improve ICL, especially on large-label-space tasks, with strong example-similarity dependence.

## What this paper does NOT establish
- That long-context models cannot learn tasks from many examples or that retrieval explains all gains.

## Explicit open questions
- How to design contexts that induce genuine task learning at extreme lengths.

## Evidence concerns
**Replication:** Multiple datasets/models reported; independent replication not assessed.
**Measurement limitations:** Accuracy and perturbation tests are indirect mechanism measures.
**Potential confounding:** Dataset label space, example similarity, prompt order, and context position.
**Statistical / experimental concerns:** Baseline tuning and cross-model comparability require full-text checking.

## Source pointers
| Item | Source |
|---|---|
| Abstract | https://arxiv.org/abs/2405.00200 |
| Full paper | https://arxiv.org/pdf/2405.00200 |
| Main result | Abstract; long-context scaling experiments |
| Important control | Shuffling/grouping and retrieval/fine-tuning comparisons |
| Limitations | Paper discussion; needs verification |
