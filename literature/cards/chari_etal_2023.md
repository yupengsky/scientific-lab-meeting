# Bayesian and Discriminative Models for Active Visual Perception across Saccades

## Metadata

**Authors:** Divya Subramanian; John M. Pearson; Marc A. Sommer

**Year:** 2023

**arXiv:** Not reported

**Published venue:** eNeuro 10(7): ENEURO.0403-22.2023

**DOI:** 10.1523/ENEURO.0403-22.2023

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/

**Evidence role:** CORE

## Scientific question

Do priors receive greater weight as uncertainty rises during perception of target displacement across saccades, as a Bayesian ideal observer predicts; does the answer depend on report format and whether uncertainty is external image noise or saccade-related?

## Exact system and regime

Human psychophysics (Experiments 1–3; n = 9 in noise-selection experiment, n = 11 continuous-report experiment) and two rhesus macaques (Experiments 4–5). Participants/animals judged whether a visual target displaced during a saccade (categorical “jump/no jump”), or humans reported horizontal displacement continuously. Target blur manipulated external visual uncertainty; with- versus no-saccade trials operationalized motor-driven uncertainty through saccadic suppression. Priors were learned/cued by task statistics.

## Main claims

### Categorical displacement judgments used priors less as external image noise increased

**OBSERVATION:** In humans and both macaques, categorical psychometric curves for high- versus low-jump priors converged as Gaussian-blob image noise increased. This is opposite to the ideal-observer prediction of greater prior separation at higher sensory uncertainty.

**AUTHOR INTERPRETATION:** Categorical active-vision judgments are anti-Bayesian for external image uncertainty; a process outside the categorical Bayesian model contributes.

**INFERENCE:** The behavioral effect rejects this particular ideal-observer implementation under these task conditions; it does not demonstrate that neural computation is globally non-Bayesian.

**Intervention or measurement:** Manipulated Gaussian-blob width and prior probability (jump probability 0.2, 0.5, or 0.8); categorical reports and psychometric-function/intercept or criterion analyses.

**Observed result:** In Experiment 4, high/low-prior intercept separation declined from 0.25 to 0.03 for Monkey S and 0.12 to 0.01 for Monkey T from medium to high image noise; controls and direction/criterion analyses agreed (Fig. 7; Extended Data Figs. 7-1 to 7-3).

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Experiment 1 selected blur because it significantly reduced human sensitivity (d′ 2.08 to 1.62, corrected p = 0.0023); macaque Experiment 4 spatially separated the blurred probe from the saccade target and found no endpoint-error change across noise; valid-prior control; analyses by displacement direction and criterion.

**Alternative explanations not excluded:** The authors state that a different parameterization of prior or sensory likelihood, including asymmetric likelihoods from efficient encoding, could potentially yield apparent anti-Bayesian behavior.

**Scope limitations:** Two monkeys; narrow displacement-detection paradigm; blur is one external-noise manipulation; learning stage influenced human versus monkey curve shapes.

**Source pointer:** Results, “Gaussian blurring induces uncertainty of image movement” (Fig. 2); “Categorical judgments of displacement are ‘anti’-Bayesian” (Figs. 3–4); “Anti-Bayesian categorization…” (Figs. 6–7); Discussion. https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/

### Continuous human displacement reports were consistent with a Bayesian model with a saccade-opposite prior bias

**OBSERVATION:** In continuous-report Experiment 3, fitted likelihood SD increased with blob noise (repeated-measures ANOVA F(2) = 20.18, p = 0.00001), and a Bayesian model with a small prior bias opposite the saccade direction qualitatively captured response patterns; fitted bias was 0.08 ± 0.05° opposite the saccade (p = 0.0009).

**AUTHOR INTERPRETATION:** Continuous reports across saccades matched Bayesian ideal-observer predictions with biased priors, unlike categorical reports.

**INFERENCE:** Report format/representational task demands may affect which model is descriptively adequate; the experiment does not localize the computation.

**Intervention or measurement:** Humans trained on a Gaussian prior centered at 0° (600 feedback trials), then made 400 no-feedback continuous estimates at low, medium, high, or absent postsaccadic target uncertainty.

**Observed result:** Estimated sensory-noise parameters increased with experimental noise; infinite-noise responses reverted near the presaccadic position; direction-split discontinuities were captured by biased-prior simulations (Fig. 5).

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Noise levels included an infinite-noise/no-postsaccadic-target condition; responses were checked by displacement direction; categorical Bayesian simulations adding bias did not reproduce the categorical anti-Bayesian effect.

**Alternative explanations not excluded:** The biased-prior parameterization is one account; responses were not smoothly linear and the design does not distinguish all alternative continuous models.

**Scope limitations:** Human sample n = 11; one-dimensional horizontal report and one trained prior distribution.

**Source pointer:** Results, “Continuous judgments of displacement are Bayesian,” Fig. 5; Extended Data Fig. 5-1. https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/

### Categorical prior use increased with motor-driven uncertainty in macaques

**OBSERVATION:** For both macaques, high- versus low-prior categorical psychometric curves were more separated in with-saccade than no-saccade trials. Intercept differences rose from 0.07 to 0.41 (Monkey S) and 0.03 to 0.37 (Monkey T); each animal had 6000 analyzed trials.

**AUTHOR INTERPRETATION:** Categorical perception was Bayesian for uncertainty attributed to saccadic suppression (motor-driven uncertainty), contrasting with external image noise.

**INFERENCE:** The results support a dissociation in this paradigm between uncertainty sources; they do not establish that the underlying source classification is the operative neural mechanism.

**Intervention or measurement:** With-saccade versus no-saccade categorical trials at three prior levels; ideal-observer simulations varied nonjump likelihood width to model saccadic suppression.

**Observed result:** Both animals showed the ideal model’s predicted greater high/low-prior separation in the with-saccade condition (Fig. 8; Extended Data Fig. 8-1).

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Saccade/no-saccade trials and priors were randomly interleaved; alternative criterion analysis and displacement-direction splits reproduced the effect; scleral search coils gave precise eye monitoring.

**Alternative explanations not excluded:** The motor manipulation was limited to saccadic suppression and no-saccade trials allowed microsaccades; other saccade-induced effects were omitted.

**Scope limitations:** Two macaques; no-saccade baseline differs behaviorally from with-saccade trials; saccadic suppression is represented by one likelihood-width change.

**Source pointer:** Results, “Anti-Bayesian categorization is driven by image noise but not motor-driven noise,” Fig. 8 and Extended Data Figs. 8-1 to 8-2; Discussion. https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/

### A simple discriminative learner is a candidate account of the anti-Bayesian categorical pattern

**OBSERVATION:** A two-layer perceptron-like discriminative model trained to classify continuous displacement as jump/no-jump reproduced key qualitative anti-Bayesian effects; a combined Bayesian/discriminative model better recapitulated overall performance. Categorical Bayesian fitting failed to reproduce human Experiment 2 behavior or required reversed sensory-noise parameters for monkeys in Experiment 4.

**AUTHOR INTERPRETATION:** Discriminative learning is a parsimonious candidate explanation for categorical anti-Bayesian behavior, and active vision may deploy Bayesian and discriminative models according to task and uncertainty source.

**INFERENCE:** Model comparison supplies a plausible computational account; it does not identify a neural implementation or rule out other models.

**Intervention or measurement:** Simulations/fits of categorical Bayesian ideal observer, discriminative network, and combined model against behavioral psychometric data.

**Observed result:** The discriminative/combined models captured principal qualitative trends, while the authors acknowledge remaining intercept and complete-curve-collapse mismatches (Fig. 10; Discussion).

**Causal strength:** UNCLEAR

**Controls:** Bayesian models were simulated and fit using experimentally mapped parameters; behavior was evaluated across humans, monkeys, noise sources, and report formats.

**Alternative explanations not excluded:** Alternative Bayesian parameterizations and additional hybrid-model components; model was deliberately minimal and did not fit every data feature.

**Scope limitations:** Computational rather than neural evidence; no out-of-sample neural test; learning rule and component combination are assumptions.

**Source pointer:** Results, “A discriminative model provides a candidate explanation…” (Figs. 9–10); Discussion, limitations paragraphs. https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/

## Important controls

- Experiment 1 compared four uncertainty manipulations and retained Gaussian blur only after a corrected sensitivity difference (Fig. 2).
- Endpoint-error analyses in human experiments and probe/target separation plus scleral search coils in macaque Experiment 4 tested whether blur changed motor uncertainty (Fig. 6).
- Valid-prior control, displacement-direction analyses, and criterion-based analyses accompanied categorical results.
- Continuous-report experiment separated report format from the categorical result; categorical simulations showed that the measured continuous-task bias alone did not explain it.

## Critical assumptions

- Bayesian ideal observer maps experimental priors/noise to likelihood distributions; motor uncertainty is modeled as widened nonjump likelihood during saccades.
- Gaussian target width manipulates visual uncertainty while endpoint scatter indexes motor uncertainty.
- The discriminative model’s two-layer learning rule and the hybrid combination are adequate candidate architectures.
- With-saccade/no-saccade contrast isolates saccadic suppression sufficiently for the modeled question.

## Limitations

Authors explicitly note possible alternative Bayesian parameterizations, including asymmetric likelihoods; motor-driven noise was represented only by saccadic suppression, excluding compression, receptive-field shifts/smearing, amplitude/direction effects, and uncontrolled microsaccades in no-saccade trials. The discriminative and combined models leave some decreasing-intercept and complete-prior-curve-collapse patterns unexplained. The study does not provide a synthesized account of when Bayesian versus discriminative computations are used.

## What this paper supports

In these human and two-macaque saccadic-displacement tasks, categorical use of learned priors decreases with manipulated external image noise but increases with the with-saccade motor-uncertainty manipulation; continuous human reports fit the stated Bayesian model. It also supports a discriminative learner as a candidate computational explanation for the external-noise categorical effect.

## What this paper does not establish

It does not establish a general source-based rule for all active perception, a neural mechanism for Bayesian/discriminative switching, or that external and internal uncertainty are cleanly separated in the brain.

## Explicit open questions

What determines Bayesian versus discriminative model use; how neural organization relates to the dissociation; how a model should include the omitted fine-grained motor effects; and how Bayesian and discriminative components combine.

## Evidence concerns

**Replication:** Human categorical pattern was further tested in two macaques; independent-laboratory replication is not reported.

**Measurement limitations:** Human eye movements were less precisely monitored than macaque scleral-coil data; no-saccade trials did not prevent microsaccades.

**Potential confounding:** Trial/training stage differs between single-session humans and extensively trained monkeys; source manipulation relies on operational models of visual versus motor uncertainty.

**Statistical / experimental concerns:** Two-animal inference; several conclusions rest on qualitative ideal-observer/model comparisons; the authors report residual model-data mismatches.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/ (Abstract) |
| Full paper | https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/ |
| Main result | https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/ (Results, Figs. 5, 7, 8, 10) |
| Important control | https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/ (Results, Figs. 2, 6; Extended Data Figs. 7-1–7-3, 8-1) |
| Limitations | https://pmc.ncbi.nlm.nih.gov/articles/PMC10368208/ (Discussion, limitations paragraphs) |
