# Language Models are Few-Shot Learners

## Metadata
**Authors:** Tom B. Brown et al. (OpenAI)
**Year:** 2020
**arXiv:** https://arxiv.org/abs/2005.14165
**Published venue:** NeurIPS 2020
**DOI:** —
**Publisher / proceedings:** NeurIPS
**Publication status:** PUBLISHED
**Reading status:** FULL_TEXT

## Abstract
The paper evaluates GPT-3, a 175B autoregressive Transformer, without gradient updates or task-specific fine-tuning. Scaling improves few-shot performance across language, QA, translation, reasoning, and synthetic tasks, sometimes approaching fine-tuned systems; substantial failures and contamination concerns remain.

## Scientific question
Can scale alone make a task-agnostic autoregressive LM use natural-language instructions and a few demonstrations effectively at inference time?

## Main claims
- Larger GPT-3 models improve in-context learning with model size.
- The 175B model is competitive with prior fine-tuned results on some tasks.
- Few-shot behavior is broad but uneven and vulnerable to benchmark contamination and prompt/task formulation.

## Key observations
- Zero-, one-, few-shot evaluations were run across many NLP and synthetic tasks (Sec. 2.4; Sec. 3; Appendix H).
- Performance generally rises with scale and number of demonstrations, with task-specific exceptions (Fig. 1.2; Fig. 3.1; Sec. 3).
- GPT-3 produces news samples that human raters often do not distinguish from human-written samples (Sec. 3.9.4; Appendix E).

## Evidence for major claims
Architecture/training: 8–10; scaling curves: Fig. 1.2 and Sec. 3; task results: Tables 3.1–3.19; contamination: Sec. 4 and Appendix C; limitations: Sec. 5.

## Observation vs interpretation
### Observed / demonstrated
- Prompted GPT-3 generated task outputs with no parameter updates; measured scores varied by task, model size, shots, and prompt formulation.
- Some benchmark examples may overlap with training data or have near duplicates.
### Author interpretation
- Scaling increases the model’s ability to recognize or adapt to tasks from context, described as in-context learning/meta-learning.
- Strong results indicate broad task-agnostic capability, while failures show it is not uniformly reliable.
### Inference
- These experiments establish behavioral adaptation, not a specific internal mechanism or causal role for attention components.

## Important controls
- Multiple model sizes and shot settings; zero-shot comparisons; contamination checks and deduplication analyses; human evaluation for news.

## Critical assumptions
- Benchmark scores and textual completion likelihood are adequate measures of task competence.
- Prompt templates and demonstrations faithfully operationalize intended tasks.

## Remaining alternative explanations
- Memorization, benchmark leakage, lexical/template priors, and pretraining distribution effects can contribute to scores.

## Limitations
The authors explicitly discuss uneven task performance, contamination, calibration/format sensitivity, factual errors, social bias, misuse, and training/inference cost (Sec. 4–6).

## What this paper supports
Large pretrained autoregressive Transformers can perform many tasks from text-only context without updates, with scale-dependent and task-dependent performance.

## What this paper does NOT establish
It does not show human-like learning, reliable novel reasoning, absence of memorization, or a mechanistic explanation of in-context learning.

## Explicit open questions
How to improve reliability, detect and prevent memorization, reduce bias/misuse, and understand why scaling produces these abilities (Secs. 4–6).

## Evidence concerns
**Replication:** Closed GPT-3 access limits exact replication.
**Measurement limitations:** Prompt and benchmark choice strongly affect scores.
**Potential confounding:** Training-set contamination and overlap with web data.
**Statistical / experimental concerns:** Broad task suite has heterogeneous metrics and limited causal isolation of mechanisms.

## Source pointers
| Item | Source |
|---|---|
| Abstract | https://arxiv.org/abs/2005.14165 |
| Full paper | https://arxiv.org/pdf/2005.14165 |
| Main result | Sec. 3; Fig. 1.2; Appendix H |
| Important control | Sec. 4; Appendix C |
| Limitations | Sec. 5 |
