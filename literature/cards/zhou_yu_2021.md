# Human visual search follows a suboptimal Bayesian strategy revealed by a spatiotemporal computational model and experiment

## Metadata

**Authors:** Yunhui Zhou; Yuguo Yu

**Year:** 2021

**arXiv:** Not reported

**Published venue:** Communications Biology 4, 34

**DOI:** 10.1038/s42003-020-01485-0

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://www.nature.com/articles/s42003-020-01485-0

**Evidence role:** CORE

## Scientific question

Can an ideal Bayesian visual-search model that controls both fixation location and duration account for human scan paths, and which modeled constraints account for any discrepancy?

## Exact system and regime

Ten healthy student volunteers (six male; 19–30 years) searched a 15° circular 1/f²-noise image for a 0.3° Gabor target. Target contrast was individualized to foveal d′ = 3. Eye position was recorded at 2 kHz. Four participants supplied the temporal visibility-map training data; six were held out for model testing. Models were compared with this artificial, static-noise visual-search task, not naturalistic everyday search.

## Main claims

### Constrained continuous-time Bayesian search better matches human oculomotor statistics than unconstrained optimal search

**OBSERVATION:** Human fixation locations were relatively uniform and saccades favored shorter amplitudes. ELM and continuous-time ELM (CTELM) produced doughnut-shaped fixation distributions, more long saccades, and stronger successive-direction changes. A constrained CTELM (CCTELM) matched spatial metrics and temporal fixation statistics more closely by Bhattacharyya-coefficient comparisons.

**AUTHOR INTERPRETATION:** Constraints on saccade amplitude, landing accuracy, and memory explain much of the mismatch between human behavior and the idealized models.

**INFERENCE:** In this stimulus regime, unconstrained information-gain maximization is insufficient as a descriptive account of scan paths.

**Intervention or measurement:** Eye tracking during search; simulations of ELM, CTELM, and CCTELM, with parameters fit on four participants and evaluated against six held-out participants.

**Observed result:** CCTELM gave better and more stable fits to fixation-location distributions (Fig. 3), saccade amplitudes and sequential relations (Fig. 4), and fixation-duration distributions (Fig. 5) than ELM/CTELM.

**Causal strength:** INTERVENTION EVIDENCE (model-component ablations; no causal manipulation of human constraints).

**Controls:** Baseline ELM replicated the earlier ideal-search framework; CTELM separated added temporal control from the three CCTELM constraints; ablations removed each constraint with other parameters unchanged (Fig. 9).

**Alternative explanations not excluded:** Individual strategy differences, unequal pre-task training, imperfect visibility-map sampling, heuristic control, and model misspecification can also contribute.

**Scope limitations:** Ten participants; one Gabor-in-noise task; model uses prior literature for landing bias/variance and an artificial collapsing bound.

**Source pointer:** Results, “Human eye movement strategy in visual search,” Figs. 3–5; Results, Fig. 9; Discussion. https://www.nature.com/articles/s42003-020-01485-0

### The fitted constrained model implies a finite memory window of about eight fixations

**OBSERVATION:** Limiting CCTELM integration to roughly eight fixations, including the current one, improved agreement with human fixation-distance-to-center statistics; removing the memory limit chiefly degraded that metric.

**AUTHOR INTERPRETATION:** Human eye-movement statistics predict a visual-search memory capacity of about eight previous/current fixations.

**INFERENCE:** The estimate is a model-dependent effective memory window, not a direct measurement of stored fixation representations.

**Intervention or measurement:** CCTELM simulations with fixed-number all-or-none retention of whole fixations; fits to training data and testing against held-out data.

**Observed result:** Best-fit capacity was about eight; memory ablation most affected fixation-distance distribution fit (Figs. 7 and 9f).

**Causal strength:** UNCLEAR

**Controls:** Capacity was varied; model versions with unlimited memory and other single-constraint removals were compared.

**Alternative explanations not excluded:** Other decay forms, partial memory, scene representation, and unmodeled search policies may yield comparable behavior.

**Scope limitations:** The model assumes a fixation is either fully retained or fully forgotten; estimate derives from pooled/artificial-task behavior.

**Source pointer:** Results, “Effect of memory capacity”; Methods, “Memory capacity”; Fig. 7; Fig. 9f; Discussion. https://www.nature.com/articles/s42003-020-01485-0

### Humans were suboptimal relative to peripheral-visibility-only ideal search, with little median fixation-cost increase

**OBSERVATION:** CCTELM and subjects had similar median fixation counts in correct training-set trials (7–8); optimal models generated scan-path distributions unlike humans. Model correct rates were calibrated near training-set performance (~88%) and exceeded the testing-set human rate (83.8%).

**AUTHOR INTERPRETATION:** Humans may trade some information-optimality for saccade, accuracy, memory, and computation costs while retaining high search performance.

**INFERENCE:** The evidence supports a descriptive cost-sensitive reconciliation in this task; it does not identify the objective function humans optimize.

**Intervention or measurement:** Human performance and simulated search performance under threshold-matched models.

**Observed result:** Constrained behavior fit human eye-movement details better without a large increase in median fixations; model/human performance differed across training and testing groups.

**Causal strength:** CORRELATIONAL

**Controls:** Same measured visibility-map framework across models; detection threshold selected to make model accuracy comparable to participants; held-out participant comparison.

**Alternative explanations not excluded:** The authors explicitly note different amounts of prior training and individual variability; static stimulus noise may cause error behavior absent from the model.

**Scope limitations:** “Suboptimal” is conditional on the peripheral-visibility-only benchmark; task costs were not independently measured or manipulated.

**Source pointer:** Results, “Human visual search performance,” Table 1 and Fig. 6; Discussion, paragraphs 1–3. https://www.nature.com/articles/s42003-020-01485-0

## Important controls

- Individual target contrast calibration to foveal d′ = 3; fixation-contingent trial aborts and repeated eye-tracker calibration (Methods).
- Visibility was measured over exposure times and locations; visibility rose then saturated and was faster/higher centrally, grounding the continuous-time evidence model (Fig. 1; Results).
- Four-person training and six-person testing split for model parameters; an extended task with seven participants was used only as a supplementary testing set.
- CCTELM ablations isolate amplitude penalty, landing inaccuracy, and memory limitation (Fig. 9).

## Critical assumptions

- Independent Gaussian visual evidence across locations/fixations and leaky within-fixation accumulation.
- Uniform target-location prior; posterior-probability thresholds govern target decision and fixation termination.
- A collapsing fixation threshold and a fixed 3% low-latency-saccade component.
- Whole-fixation, fixed-capacity memory; saccade landing bias/variance imported from prior work.

## Limitations

Authors state that visibility maps were not densely sampled and full temporal visibility was not measured for some testing participants; participants had variable trial counts and training. Static background noise can cause error patterns that the model’s dynamic noise does not reproduce, including the many human fixations in error trials. Secondary saccades were omitted and may explain the large-saccade duration mismatch. The collapsing threshold is artificial and its biological status remains controversial.

## What this paper supports

For this controlled human visual-search task, a Bayesian continuous-time model augmented with explicit short-saccade, landing-accuracy, and finite-memory constraints describes scan-path and fixation-time distributions better than the unconstrained ideal models. It provides model-based evidence for an approximately eight-fixation effective memory parameter.

## What this paper does not establish

It does not establish a directly measured neural or cognitive memory capacity, that humans optimize a defined effort-cost objective, or that the proposed constraints cause human behavior outside this task.

## Explicit open questions

Which mechanisms produce the fitted memory limit; how training changes proximity to the ideal model; whether models should incorporate secondary saccades and static-noise error structure; and how to make the collapsing decision threshold biologically grounded.

## Evidence concerns

**Replication:** Baseline ELM was used as a replication framework; no independent behavioral replication is reported.

**Measurement limitations:** Visibility data were pooled for the main map and incompletely measured in some testing participants; task trial counts differed across people.

**Potential confounding:** Training amount and individual strategy covary with group/model differences; model accuracy was threshold-matched.

**Statistical / experimental concerns:** Small sample (n = 10), only four visibility-map participants, and several key conclusions derive from relative model fit rather than preregistered model selection.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://www.nature.com/articles/s42003-020-01485-0 (Abstract) |
| Full paper | https://www.nature.com/articles/s42003-020-01485-0 |
| Main result | https://www.nature.com/articles/s42003-020-01485-0 (Results, Figs. 3–5, 7, 9) |
| Important control | https://www.nature.com/articles/s42003-020-01485-0 (Methods; Results, Fig. 9) |
| Limitations | https://www.nature.com/articles/s42003-020-01485-0 (Discussion; Results, error trials) |
