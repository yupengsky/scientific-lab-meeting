# The Transient Nature of Emergent In-Context Learning in Transformers

## Metadata
**Authors:** Aaditya K. Singh, Stephanie C. Y. Chan, Ted Moskovitz, Erin Grant, Andrew M. Saxe, Felix Hill
**Year:** 2023
**arXiv:** https://arxiv.org/abs/2311.08360
**Published venue:** NeurIPS 2023
**DOI:** UNCLEAR
**Publisher / proceedings:** NeurIPS
**Publication status:** PUBLISHED
**Reading status:** PARTIAL

## Abstract
Using synthetic data where both ICL and in-weights learning (IWL) can solve the task, the paper finds that ICL can emerge, disappear during continued training, and be replaced by IWL while training loss keeps decreasing.

## Scientific question
Is emergent ICL a persistent endpoint of training, or can it be transient?

## Main claims
- **AUTHOR CLAIM:** ICL is often transient in the studied transformers.
- **AUTHOR CLAIM:** L2 regularization can make ICL more persistent; preliminary circuit evidence suggests competition between ICL and IWL.

## Key observations
- ICL evaluator accuracy rises and later falls; IWL rises as ICL falls; training loss continues decreasing. The pattern appears across model sizes and datasets.

## Evidence for major claims
- **OBSERVATION:** Evaluator curves separate ICL and IWL behavior over training (main Fig. 1 and related experiments).
- **AUTHOR INTERPRETATION:** Continued optimization favors IWL and may suppress an ICL circuit through competition.

## Observation vs interpretation
### Observed / demonstrated
- Transient ICL under the paper’s synthetic training/evaluation setup; regularization changes persistence.
### Author interpretation
- The dynamics reflect competing ICL and IWL circuits.

## Important controls
- Multiple model sizes/datasets; training-loss trajectory; regularized versus unregularized training; different evaluator types.

## Critical assumptions
- ICL and IWL evaluators adequately distinguish the strategies.

## Remaining alternative explanations
- Evaluator distribution shift, optimization bias, or representation changes could contribute without literal circuit competition.

## Limitations
- Synthetic data and controlled architectures limit direct extrapolation to web-scale pretrained LLMs.

## What this paper supports
- Emergent ICL can disappear with overtraining in controlled transformer settings.

## What this paper does NOT establish
- That all ICL in deployed LLMs is transient or that L2 regularization is sufficient generally.

## Explicit open questions
- How often transience occurs in natural data and which circuit interactions cause it.

## Evidence concerns
**Replication:** Multiple internal settings; external replication not assessed.
**Measurement limitations:** Strategy evaluators are proxies.
**Potential confounding:** Training duration, data burstiness, architecture, and regularization.
**Statistical / experimental concerns:** Circuit-competition evidence is explicitly preliminary.

## Source pointers
| Item | Source |
|---|---|
| Abstract | https://arxiv.org/abs/2311.08360 |
| Full paper | https://proceedings.neurips.cc/paper_files/paper/2023/file/58692a1701314e09cbd7a5f5f3871cc9-Paper-Conference.pdf |
| Main result | Fig. 1; Sections 3–4 |
| Important control | Regularization and evaluator comparisons |
| Limitations | Discussion/conclusion |
