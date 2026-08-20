# Cost-sensitive Bayesian control policy in human active sensing

## Metadata

**Authors:** Sheeraz Ahmad; He Huang; Angela J. Yu

**Year:** 2014

**arXiv:** None identified

**Published venue:** Frontiers in Human Neuroscience 8:955

**DOI:** 10.3389/fnhum.2014.00955

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00955/full

**Evidence role:** CORE

## Scientific question

Can a Bayesian controller that explicitly trades response error, elapsed time, and sensor-switching cost account for human within-trial visual-search dynamics better than information-maximization policies?

## Exact system and regime

Eleven analyzed UCSD undergraduates (from 12 recruited; five female) made a gaze-contingent visual-search decision among three random-dot-motion patches: one direction-defined target and two opposite-direction distractors. Target locations followed either 1:3:9 odds or an equal-probability 1:1:1 control. Only the fixated patch was visible. Participants received feedback and monetary-point incentives: time penalty, 25-point switch penalty, and ±50-point accuracy outcome. The model treats target location as a hidden state and observations as binary Bernoulli signals.

## Main claims

### Claim

**OBSERVATION:** In the 1:3:9 condition, people were more accurate and faster than in the 1:1:1 condition. Conditional on first fixating a labeled location, they more often accepted the high-prior “9” location both when it was target (hits) and distractor (false alarms); they accepted true targets there faster and rejected distractors there more slowly.

**AUTHOR INTERPRETATION:** Spatial priors influence both perceptual choice and the fine temporal dynamics of within-trial eye movements/processing, producing a form of confirmation bias.

**INFERENCE:** These observations demonstrate context-sensitive behavior under explicit incentives. They cannot distinguish use of a switch-cost objective from a learned response bias or other task-specific strategies.

**Intervention or measurement:** Manipulate target-location distribution (1:3:9 versus 1:1:1); record eye movements, choices, and fixation duration in a gaze-contingent task.

**Observed result:** Participants allocated first fixations approximately according to learned spatial probabilities and showed the Fig. 3 prior-dependent choice/fixation-duration pattern.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Equal-probability condition; gaze-contingent display limits unmeasured covert-attention dynamics; Fig. 3 analysis includes only trials first fixated at the labeled patch to reduce motor-selection effects; target-direction assignment was balanced across participants.

**Alternative explanations not excluded:** Explicit point structure, reinforcement learning, response thresholds, attention allocation, or unmodeled motor costs can generate prior-dependent dwell times and choices.

**Scope limitations:** Small student sample; three discrete locations; artificial motion discrimination and instructed reward schedule; peripheral vision excluded from the behavioral experiment.

**Source pointer:** Methods 2.8; Results 3, Fig. 2–3. https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00955/full

### Claim

**OBSERVATION:** C-DAC, a belief-state POMDP policy minimizing time, switching, and error costs, reproduced the human Fig. 3 pattern in simulation. Infomax did not; the authors attribute this to its absent switch-cost sensitivity. Simulations further show C-DAC lowers total modeled cost and reduces switches when switch cost is added. The paper also gives RBF/GPR and myopic approximations to reduce computational load.

**AUTHOR INTERPRETATION:** Human active search is apparently sensitive to switching cost, and C-DAC is a better account than Infomax or greedy MAP for this task. Approximate policies retain contextual sensitivity with lower computation.

**INFERENCE:** The model comparison provides a mechanistic explanation conditional on fitted cost/noise parameters. It does not establish that humans compute dynamic-programming values or encode the stated loss function.

**Intervention or measurement:** Fit C-DAC near experimentally derived parameters; compare its simulated behavioral outputs with Infomax/greedy MAP; vary switching cost in simulations and in an extended peripheral-vision simulation.

**Observed result:** At (c, c_s, beta) = (0.005, 0.1, 0.68), C-DAC reproduced Fig. 3 while Infomax did not. In model simulations, adding c_s reduced C-DAC switches and total cost relative to Infomax.

**Causal strength:** CORRELATIONAL

**Controls:** Same Bayesian belief-updating basis for C-DAC and Infomax; a stopping-bound augmentation for Infomax; greedy MAP considered and described as highly suboptimal for the task; matched-accuracy comparison in the peripheral-vision simulation.

**Alternative explanations not excluded:** Other decision models with learned priors, urgency/threshold changes, or switch aversion may fit the qualitative confirmation-bias pattern. The implementation uses a narrow grid search around translated experimental parameters.

**Scope limitations:** Exact C-DAC dynamic programming grows exponentially with number of target locations; approximations add parameters and were not claimed as uniquely biologically realized. Peripheral-vision results are simulations, not human data.

**Source pointer:** Methods 2.1–2.7; Results 3.1–3.2, Fig. 3–6; Discussion. https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00955/full

## Important controls

- 1:1:1 target distribution tests behavior without unequal spatial priors (Results, Fig. 2).
- Gaze-contingent display makes only the currently fixated stimulus visible, reducing unobserved covert-attention dynamics (Methods 2.8; Results 3).
- Fig. 3 restricts analysis to first fixation at the labeled patch, separating prior effects on processing from first-saccade selection.
- C-DAC is compared with Infomax under shared Bayesian observation assumptions; the extended simulation matches accuracy before comparison (Results, Fig. 3–6).

## Critical assumptions

- Target position is static and visual observations are conditionally Bernoulli with a single noise parameter.
- People seek to minimize a linear combination of time, switch, and error costs.
- Experimental points faithfully instantiate behavioral costs.
- The fitted/simulated observation and cost parameters are suitable for comparing models to human behavior.

## Limitations

The authors state that exact dynamic programming is exponentially costly in target-location number. They identify approximation-parameter burden and lack of general convergence proof. Their behavioral task excludes peripheral vision; peripheral-vision results are introduced as a model extension for future experiments.

## What this paper supports

In this three-location gaze-contingent search task with explicit time, accuracy, and switching incentives, spatial priors affect choices and fixation durations. A cost-sensitive Bayesian controller reproduces a qualitative human pattern that their Infomax implementation misses.

## What this paper does not establish

It does not establish that human saccades generally minimize the C-DAC loss, identify a neural implementation, isolate intrinsic saccade cost from the imposed point penalty, or validate C-DAC in natural visual search.

## Explicit open questions

The authors propose future investigation of approximate-policy limitations and experiments including peripheral vision; they state the framework could extend to active scene categorization and foraging.

## Evidence concerns

**Replication:** No independent replication is reported; behavioral data include 11 analyzed participants.

**Measurement limitations:** Binary-observation model and gaze-contingent, three-patch task simplify ordinary vision; peripheral vision is modeled only in simulation.

**Potential confounding:** A 25-point fixation-switch penalty directly incentivizes the model’s proposed switch-cost component; intrinsic versus task-imposed cost is unresolved.

**Statistical / experimental concerns:** Results reported here are largely figure-level behavioral/model comparisons; the paper describes parameter selection through a narrow grid search and does not present an out-of-sample model-selection test in the inspected text.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00955/full — Abstract |
| Full paper | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00955/full — sections 1–4 |
| Main result | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00955/full — Results 3.1, Fig. 2–4 |
| Important control | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00955/full — Methods 2.8; Results 3, Fig. 3 |
| Limitations | https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00955/full — Introduction; Methods 2.4–2.6; Results 3.2; Discussion |
