# Adversarial Robustness of In-Context Learning in Transformers for Linear Regression

## Metadata
**Authors:** Usman Anwar, Johannes von Oswald, Louis Kirsch, David Krueger, Spencer Frei
**Year:** 2024
**arXiv:** https://arxiv.org/abs/2411.05189
**Published venue:** PREPRINT
**DOI:** UNCLEAR
**Publisher / proceedings:** arXiv
**Publication status:** PREPRINT
**Reading status:** PARTIAL

## Abstract
The paper studies prompt hijacking attacks against transformers implementing linear regression in context.

## Scientific question
How robust are learned ICL algorithms to adversarial manipulation of in-context examples?

## Main claims
- **AUTHOR CLAIM:** Single-layer linear transformers can be forced to arbitrary predictions by perturbing one example.
- **AUTHOR CLAIM:** GPT-2-style transformers resist the tested attacks but can be hijacked by gradient-based attacks.
- **AUTHOR CLAIM:** Adversarial training improves robustness, including in some cases against stronger attacks.

## Key observations
- Attacks succeed on linear transformers; transfer to more complex GPT-2 architectures is poor for the tested attack, while gradient attacks succeed. Attack transfer is effective among small-scale transformers but poor across scales and between transformers and OLS.

## Evidence for major claims
- **OBSERVATION:** Output-targeted prompt perturbations change predictions under the reported attack settings.
- **AUTHOR INTERPRETATION:** Learned in-context algorithms are vulnerable because prompt examples can steer the inferred regression solution; adversarial training can suppress this vulnerability.

## Observation vs interpretation
### Observed / demonstrated
- Theoretical non-robustness result for single-layer linear transformers and empirical attack/transfer results.
### Author interpretation
- Robustness depends on architecture, scale, attack strength, and training procedure.

## Important controls
- Linear versus GPT-2 architectures; weak versus gradient-based attacks; scale/seed transfer; OLS comparison; adversarial training at finetuning.

## Critical assumptions
- Hijacking attacks model the relevant threat: an adversary may alter in-context training examples to force an output.

## Remaining alternative explanations
- Attack failure may reflect optimization or budget limits rather than intrinsic robustness.

## Limitations
- Results focus on linear regression and selected transformer architectures; they do not establish robustness properties of general-purpose LLM ICL.

## What this paper supports
- Prompt-based ICL can be adversarially manipulable, with vulnerability varying substantially by architecture and scale.

## What this paper does NOT establish
- Universal attackability, universal transfer, or production-level security guarantees from adversarial training.

## Explicit open questions
- Robustness for nonlinear tasks, natural-language prompts, larger models, and adaptive attackers.

## Evidence concerns
**Replication:** Theory plus experiments; external replication not assessed.
**Measurement limitations:** Attack success depends on perturbation budget and objective.
**Potential confounding:** Architecture, initialization, scale, and attack optimization.
**Statistical / experimental concerns:** Transfer results are setting-specific; full attack protocols need verification.

## Source pointers
| Item | Source |
|---|---|
| Abstract | https://arxiv.org/abs/2411.05189 |
| Full paper | https://arxiv.org/pdf/2411.05189 |
| Main result | Abstract; attack and transfer experiments |
| Important control | Architecture/scale transfer and adversarial training |
| Limitations | Paper discussion; needs verification |
