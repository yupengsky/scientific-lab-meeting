# What Learning Algorithm Is In-Context Learning? Investigations with Linear Models

## Metadata

**Authors:** Ekin Akyürek, Dale Schuurmans, Jacob Andreas, Tengyu Ma, Denny Zhou

**Year:** 2023

**arXiv:** https://arxiv.org/abs/2211.15661

**Published venue:** ICLR 2023

**DOI:** Not recorded in source

**Publisher / proceedings:** ICLR 2023; exact proceedings URL not verified in the paper text

**Publication status:** PUBLISHED

**Reading status:** FULL_TEXT

---

## Abstract

The paper asks which learning algorithms trained transformers implement during ICL, using linear regression. It constructs transformers for GD and ridge regression, compares trained learners with GD, ridge, least-squares, and Bayesian predictors under depth, width, and noise changes, and decodes weight vectors and moment matrices from late activations.

## Scientific question

Do transformers implement recognizable estimation algorithms when learning a linear predictor from in-context examples?

## Main claims

The authors claim that at least some ICL learners rediscover standard estimation procedures. The learned procedure varies with architecture and data noise: trained models can resemble GD, ridge, exact least squares, or Bayesian estimators.

## Key observations

- Constant-depth transformers can implement one GD step with O(d) hidden size and ridge updates with O(d²) hidden size (Sec. 3).
- Trained models closely match different candidate predictors as depth, width, and training noise vary (Sec. 4; Figs. 2–6).
- Larger/deeper models in some settings converge toward Bayesian estimators (Sec. 4).
- Late hidden states nonlinearly encode parameter vectors and moment matrices used by these algorithms (Sec. 5; Figs. 7–9).

## Evidence for major claims

The construction proves representability, not discovery. Discovery evidence comes from underdetermined synthetic linear-regression tasks where candidate algorithms make different held-out predictions. Representation evidence comes from decoding intermediate quantities from activations.

## Observation vs interpretation

### Observed / demonstrated

- Transformers can be parameterized to execute GD and ridge updates.
- Trained predictors align with named estimators under tested conditions.
- Algorithm-relevant quantities are decodable from late activations.

### Author interpretation

- The learners use algorithmic internal computation and may rediscover familiar learning rules.

## Important controls

- Underdetermined tasks separate candidate estimators by held-out behavior.
- Varying depth, width, and noise tests algorithm transitions.
- Comparisons include GD, ridge, exact least squares, and Bayesian predictors.

## Critical assumptions

Linear regression is treated as a useful prototype of ICL. Predictor alignment and decoding are taken as evidence about computation, though neither alone proves causal execution.

## Remaining alternative explanations

A different nonlinear predictor can agree with the tested estimators on the evaluation distribution. Decodability may reflect correlates rather than variables used causally by the model.

## Limitations

The paper focuses on linear models and calls the activation-decoding evidence preliminary (Secs. 1 and 5). It does not identify the algorithm for general natural-language ICL.

## What this paper supports

- Candidate learning algorithms are empirically distinguishable in controlled ICL.
- Synthetic transformers can exhibit estimator-specific, algorithm-like behavior.

## What this paper does NOT establish

- A single universal ICL algorithm.
- That decoded weights/moments are causally necessary.
- That the same transitions occur in pretrained language models.

## Explicit open questions

Which algorithms are implementable/discovered in broader settings and how to characterize them beyond linear regression (Introduction, Conclusion).

## Evidence concerns

**Replication:** Code is provided by the paper; broad replication is outside this card.

**Measurement limitations:** Alignment and decoding are indirect algorithmic evidence.

**Potential confounding:** Synthetic task distribution, finite depth, and noise determine which estimator is favored.

**Statistical / experimental concerns:** Results are controlled but not evidence of necessity in large pretrained LMs.

## Source pointers

| Item | Source |
|---|---|
| Abstract | https://arxiv.org/abs/2211.15661 |
| Full paper | https://arxiv.org/pdf/2211.15661 |
| Main result | Secs. 3–5; Figs. 2–9 |
| Important control | Underdetermined regression tasks, Sec. 4 |
| Limitations | Introduction; Sec. 5; Conclusion |
