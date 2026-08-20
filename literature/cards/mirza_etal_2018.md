# Human visual exploration reduces uncertainty about the sensed world

## Metadata

**Authors:** M. Berk Mirza; Rick A. Adams; Christoph Mathys; Karl J. Friston

**Year:** 2018

**arXiv:** None found in inspected paper

**Published venue:** PLOS ONE 13(1): e0190429

**DOI:** 10.1371/journal.pone.0190429

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://doi.org/10.1371/journal.pone.0190429

**Evidence role:** CORE

## Scientific question

Do healthy humans' scan paths in a gaze-contingent scene-categorisation task contain evidence for epistemic, uncertainty-resolving visual foraging, and can individual differences be expressed as fitted active-inference parameters?

## Exact system and regime

22 healthy adults (9 male, 13 female; 19–57 years; mainly UCL students) completed five 100-trial blocks after 20 pre-training trials. In each trial, they classified a masked 2×2 scene as Flee, Feed, or Wait by moving gaze to reveal bird/seed/cat/null objects, then reported the category. Eye movements were measured with EyeLink 1000. Correct/incorrect responses and successive samples had explicit point costs and individual 2–4 s time limits. Scan paths were fitted with discrete-state MDP active-inference models containing either epistemic plus extrinsic value or extrinsic value alone; 24 fixed-form scan-path heuristics were also modelled. [Methods, pp. 3–10; Fig. 4]

## Main claims

### Epistemic value improves explanation of human scan paths

**OBSERVATION:** For every participant, the fitted model including epistemic value had greater log evidence than the extrinsic-only model; pooled log-evidence difference was approximately 888. Participants also showed repeated context-independent reading-like or clockwise scan paths. [Results, p. 12; Figs. 6–7A]

**AUTHOR INTERPRETATION:** Healthy visual exploration incorporates epistemic affordance/salience: locations are selected partly for their expected uncertainty reduction, alongside fixed-form heuristics.

**INFERENCE:** Within this narrowly specified task and model family, scan paths are better accounted for by an epistemic-value term than by preference-driven policies alone; this does not directly measure a participant's internal computation.

**Intervention or measurement:** Gaze-contingent 2×2 scene task; eye-tracked scan paths; Bayesian comparison of fitted MDPs with versus without epistemic value.

**Observed result:** Epistemic model won for all 22 subjects and in pooled evidence; six heuristic strategies occurred, with reading-like and clockwise strategies most common (47% and 42% of trials for subjects' respective favourite heuristics). [pp. 12–13; Figs. 6–7A]

**Causal strength:** CORRELATIONAL

**Controls:** Direct nested-model comparison against extrinsic-only policy selection; models included 24 possible fixed-form heuristic policies, rather than treating all non-epistemic structure as random.

**Alternative explanations not excluded:** Other unmodelled scan-path strategies, task-learning mechanisms, motor biases, and model misspecification could account for some evidence advantage.

**Scope limitations:** Simple, highly structured 2×2 displays; the authors state that epistemic and heuristic policies can produce the same action, making them difficult to disambiguate, and expect a larger grid to separate them better. [Discussion, pp. 17–18]

**Source pointer:** https://doi.org/10.1371/journal.pone.0190429, Results “Scan path results,” pp. 12–14; Fig. 7A.

### Fitted priors covary with performance and experience

**OBSERVATION:** Across blocks, accuracy and score rose while saccades/trial and inter-saccade interval fell (first vs fifth block two-sample tests, all p < 0.001). Model reduction retained experience-dependent changes mainly in preferences for correctness and speed, with prior-policy precision and heuristic-bias changes redundant. Canonical correlation analysis found three significant correlations; its fitted parameter combinations accounted for 96%, 92%, and 70% of variance in three behavioural canonical factors. [pp. 11, 13–16; Figs. 5, 7–8]

**AUTHOR INTERPRETATION:** Experience systematically changes implicit expectations about being correct and quick; lower fitted heuristic bias is associated with more accurate and more efficient categorisation, supporting computational phenotyping by active-inference priors.

**INFERENCE:** The fitted parameters summarize behavioural variation in this dataset. They should not yet be treated as validated psychological traits or neural quantities.

**Intervention or measurement:** Blockwise behavioural measures; hierarchical Bayesian model reduction/averaging over 256 between-block parameter models; canonical correlation of fitted priors and behavioural scores.

**Observed result:** Mean group changes favoured increased precision of especially speed preferences; three canonical variates were significant, and the first associated lower heuristic bias with greater accuracy and fewer saccades. [pp. 13–16; Figs. 7B, 8]

**Causal strength:** CORRELATIONAL

**Controls:** Training preceded test blocks; blockwise model comparison considered all combinations of constant and exponential changes for four fitted priors; scan paths used for fitting were distinct from performance variables used in canonical correlation. [Methods, pp. 7–10]

**Alternative explanations not excluded:** Parameter–behaviour associations can reflect overfitting, parameter identifiability, task incentives, or other latent abilities; canonical associations establish no causal role for priors.

**Scope limitations:** Small non-clinical convenience sample; task time limits were individually staircase-adjusted; no clinical cohort was tested.

**Source pointer:** https://doi.org/10.1371/journal.pone.0190429, Results “Behavioural results,” pp. 11–12; “Bayesian model comparison,” pp. 12–14; “Canonical correlation,” pp. 14–16; Figs. 5, 7, 8.

## Important controls

- Epistemic and extrinsic-only MDPs were compared on the same scan paths.
- Fixed-form policies represented each of the 24 non-revisiting quadrant orders.
- Parameter recovery was examined by simulating and re-estimating scan paths using fitted parameters. [Methods/Results, pp. 7–9; Fig. 3]
- The model comparison penalized unnecessary parameters through Bayesian model reduction. [p. 13; Fig. 7]

## Critical assumptions

- Participants' task beliefs can be represented by the specified discrete MDP, including its likelihoods, preferences, and one-step policies.
- Bayesian model evidence distinguishes the epistemic component from heuristic policy priors in these scan paths.
- Fitted parameters (policy precision, heuristic bias, correctness/speed preferences) have an interpretable correspondence to subject-level beliefs.

## Limitations

- The model deterministically specifies what is seen at a sampled location and does not process visual features. [Discussion, p. 17]
- Small displays can make epistemic and heuristic actions identical; the authors explicitly identify this as a disambiguation problem. [Discussion, pp. 17–18]
- Evidence concerns healthy adults in an artificial, reward- and time-constrained task; it does not test real-world visual exploration or clinical salience.

## What this paper supports

In this task, an active-inference model with expected uncertainty reduction explains human scan paths better than an extrinsic-only comparator, while allowing systematic heuristics. It also supports a model-dependent association between fitted scan-path priors and behavioural performance.

## What this paper does not establish

It does not demonstrate the neural implementation of active inference, prove that humans explicitly compute expected free energy, establish causal effects of fitted priors, or validate the framework for schizophrenia or other populations.

## Explicit open questions

- Whether this paradigm reveals altered salience attribution in schizophrenia; the authors propose future clinical work. [Discussion, p. 18]
- Whether a larger grid improves discrimination between epistemic and heuristic strategies. [Discussion, p. 18]

## Evidence concerns

**Replication:** No independent replication reported in this paper.

**Measurement limitations:** Eye position indexes overt sampling; it does not measure covert attention or internal beliefs directly.

**Potential confounding:** Explicit sampling costs, feedback, adaptive deadlines, and learned button mappings can shape scan paths independently of the hypothesised epistemic computation.

**Statistical / experimental concerns:** Key mechanistic result is model comparison conditioned on the authors' model space; the canonical-correlation analysis is within the same modest sample.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://doi.org/10.1371/journal.pone.0190429, p. 1 |
| Full paper | https://doi.org/10.1371/journal.pone.0190429 |
| Main result | Results “Scan path results,” pp. 12–14; Fig. 7A |
| Important control | Methods “Characterising empirical behaviour,” pp. 7–9; Fig. 3; Results pp. 12–13 |
| Limitations | Discussion, pp. 17–18 |
