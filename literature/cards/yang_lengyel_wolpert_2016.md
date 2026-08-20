# Active sensing in the categorization of visual patterns

## Metadata

**Authors:** Scott Cheng-Hsin Yang; Máté Lengyel; Daniel M Wolpert

**Year:** 2016

**arXiv:** None identified

**Published venue:** eLife 5:e12215

**DOI:** 10.7554/eLife.12215

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://elifesciences.org/articles/12215

**Evidence role:** CORE

## Scientific question

Do human saccade choices during visual categorization integrate prior knowledge and trial-specific evidence, and how efficient are those choices relative to a Bayesian information-gain policy?

## Exact system and regime

Three healthy, naive adults (25–35 years) categorized synthetic Gaussian-process images as patchy versus stripy. Images were initially masked; a Gaussian aperture (SD 0.18°) revealed image content at each gaze-contingent fixation. The free-scan trials stopped after an unknown, balanced 5–25 revealings. Passive conditions supplied random, ideal-BAS, or anti-BAS revealings. Eye position was recorded at 1 kHz. The main experiment was within-participant (about 12 h across 6 days); a separate 3-person no-rescanning control and an independent 6-person saccade-error measurement supported controls/modeling.

## Main claims

### Claim

**OBSERVATION:** Active-condition accuracy increased with number of revealings. Reveal-density patterns depended on the true image type: within-type maps were positively correlated and across-type maps negatively correlated (all reported p<0.001). Random passive revealings impaired performance; no-rescanning participants showed similar scan maps and slightly lower but similar accuracy.

**AUTHOR INTERPRETATION:** Participants use accumulated scene evidence and learned pattern statistics to guide active sensing; the active selection contributes to categorization performance.

**INFERENCE:** The gaze-contingent paradigm supports a causal contribution of selecting revealing locations versus random computer-selected locations within this synthetic task. It does not isolate a neural mechanism for the policy.

**Intervention or measurement:** Compare human free scan with computer-controlled passive revealing; analyze fixation-density maps and accuracy across revealings; remove final rescanning in a control.

**Observed result:** Active revealings were 2.93-fold more information-efficient than random revealings (95% CI 2.60–3.32); active participants had average accuracy 0.66 versus 0.63 in the no-rescanning control.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Equalized opportunity to inspect revealed regions through post-revealing rescanning; passive random/ideal/anti-BAS conditions; no-rescanning control; model comparisons with heuristics retaining subsets of scan statistics.

**Alternative explanations not excluded:** A task-specific learned strategy for stationary synthetic patterns, general biases in saccades, or unmodeled perceptual/decision processes can contribute to the observed maps and performance.

**Scope limitations:** Three participants; artificial, stationary patterns; masked gaze-contingent vision; trials constrained by number of revealings rather than time.

**Source pointer:** Results, “Categorization performance and eye movement patterns,” Fig. 2–3; Materials and methods, Participants/Task/No-rescanning control. https://elifesciences.org/articles/12215

### Claim

**OBSERVATION:** A Bayesian active sensor (BAS) that maximizes expected category-entropy reduction, with participants’ fitted prior bias and perceptual noise plus measured saccadic error, generated reveal maps correlated with participant maps (same-type positive, different-type negative; all reported p<0.001). BAS-matched efficiency relative to participant scans was 1.45 (95% CI 1.37–1.53), yielding the reported ~70% efficiency estimate. The full BAS fit fixation data better than maximum-entropy sampling; participant scans were 1.81–1.92 times more efficient than three reduced heuristics.

**AUTHOR INTERPRETATION:** The central process selecting fixation locations is about 70% efficient; much apparent suboptimality arises from prior bias, perceptual noise, and saccadic inaccuracy rather than fixation planning.

**INFERENCE:** The ~70% figure is a model-dependent decomposition of behavior, conditional on the assumed stimulus statistics, fitted observer parameters, and modeled motor error. It does not directly measure planning efficiency independently of those assumptions.

**Intervention or measurement:** Fit six ideal-observer variants to choice data using BIC; simulate BAS from fitted parameters and independently measured saccade error; compare predicted/observed density maps and information curves.

**Observed result:** Idealized BAS revealings supplied 2.48-fold more information than participant scans (95% CI 2.33–2.62); accounting for modeled participant constraints reduced this gap to 1.45-fold.

**Causal strength:** CORRELATIONAL

**Controls:** BIC-controlled model selection; eye-movement predictions made after fitting choice data, without eye-movement tuning; maximum-entropy and three heuristic comparator policies; independent saccade-error measurements.

**Alternative explanations not excluded:** Unmodeled cardinal/center biases, incorrect assumed internal statistics, temporal variation in sensory extraction, or another policy that produces similar maps could explain part of the correspondence.

**Scope limitations:** BAS assumes known generative statistics, fixed information extracted per revealing, and no fixation-duration effects. The authors state that unmodeled biases could place the 70% estimate as a lower bound if they reflect execution.

**Source pointer:** Results, “Predicting eye movement patterns…” and “Fixation informativeness,” Fig. 3–5; Discussion, “The efficiency of active sensing in human vision”; Methods, “Ideal observer” and “BAS.” https://elifesciences.org/articles/12215

## Important controls

- Passive random revealings test the value of active location selection; ideal-BAS and anti-BAS passive trials prevent location patterns from directly cueing category (Methods, Passive revealing; Fig. 2).
- Post-revealing rescanning equalized access to revealed information; the no-rescanning control tested whether it changed initial selection (Results, Fig. 2 supplement/Fig. 3 supplement).
- Maximum-entropy and partial-information heuristics test whether simpler map statistics account for results (Results, Fig. 4–5).
- Independent saccade-error data were incorporated into BAS simulations (Methods, Saccadic variability and bias).

## Critical assumptions

- The image categories are adequately represented by the specified Gaussian-process correlation statistics.
- The fitted prior bias, perceptual noise, and decision noise represent participant beliefs/choices.
- Expected entropy reduction is the relevant normative objective for each next fixation.
- Fixed information per aperture and the saccade-error model adequately approximate the relevant perceptual and motor constraints.

## Limitations

Authors explicitly note the restricted field of view, voluntary macro-saccade focus, strictly stationary stimuli, and reveal-count rather than time constraints. The study uses three main participants and emphasizes within-participant analysis. A 2017 correction replaced prior with posterior weights in Equation 9; the online article is corrected.

## What this paper supports

Within this masked synthetic-pattern task, humans select gaze locations in a way linked to accumulated category-relevant information, outperforming random and specified heuristic revealing policies; a fitted BAS model captures important map-level and information-efficiency features.

## What this paper does not establish

It does not establish that natural-scene eye movements optimize information gain, that BAS is the neural computation, or that the ~70% model-based planning-efficiency estimate generalizes beyond this task.

## Explicit open questions

The authors call for more naturalistic tasks with full-field vision, local non-stationarity, and time constraints while preserving quantifiable task-relevant information. They state that micro-saccades/drift may matter more for fine natural structure.

## Evidence concerns

**Replication:** No independent replication is reported in this paper; main sample is three participants.

**Measurement limitations:** Gaze-contingent apertures and synthetic stationary images alter natural visual input; fixation duration is excluded from the observer model.

**Potential confounding:** The efficiency decomposition depends on fitted perceptual/prior parameters and assumed motor variability; the authors identify unmodeled directional/central fixation biases.

**Statistical / experimental concerns:** Reported confidence intervals and p-values support the stated within-task comparisons; the small sample constrains population-level inference.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://elifesciences.org/articles/12215 — Abstract |
| Full paper | https://elifesciences.org/articles/12215 — full text |
| Main result | https://elifesciences.org/articles/12215 — Results, Fig. 2–5 |
| Important control | https://elifesciences.org/articles/12215 — Methods, Passive revealing and No-rescanning control; Results, Fig. 2 supplement / Fig. 3 supplement |
| Limitations | https://elifesciences.org/articles/12215 — Discussion, “Relevance for natural vision” |
