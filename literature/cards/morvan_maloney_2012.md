# Human Visual Search Does Not Maximize the Post-Saccadic Probability of Identifying Targets

## Metadata

**Authors:** Camille Morvan; Laurence T. Maloney

**Year:** 2012

**arXiv:** Not reported

**Published venue:** PLOS Computational Biology 8(2): e1002342

**DOI:** 10.1371/journal.pcbi.1002342

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002342

**Evidence role:** CORE

## Scientific question

Do human observers choose a one-saccade visual-search strategy that uses their extrafoveal sensitivity to maximize post-saccadic discrimination probability/expected gain, as predicted by the tested optimal statistical model?

## Exact system and regime

Two controlled laboratory experiments with NYU undergraduates: four observers in Experiment 1 (three female) and two in Experiment 2 (one also participated in Experiment 1), all with normal or corrected vision and unaware of the purpose. On each trial, participants made one permitted saccade to one of three horizontal grey tokens (left, center, right); a dot-up versus dot-down target then appeared equiprobably at a side token, never the center. Experiment 1 varied token separation (8–24°); Experiment 2 varied token size (0.6–1.8°). Individual retinal sensitivity was mapped before choices. Correct discrimination earned monetary reward (maximum $20); a second saccade or an endpoint outside the token criterion aborted the trial.

## Main claims

### Participants did not adjust center-versus-side saccade strategy at the individual optimal switch point.

**OBSERVATION:** Individual sensitivity maps predicted a sharp switch from center to side strategy as separation increased or size decreased. None of the six observers switched at that point; choice frequency did not change with the manipulated separation or size.

**AUTHOR INTERPRETATION:** Observers did not correctly use extrafoveal sensitivity to optimize visual search in this task.

**INFERENCE:** The result rejects the tested policy in this task; it does not identify a unique alternative policy or show that all normative visual-search models fail.

**Intervention or measurement:** Sensitivity-mapping phase fitted individual psychometric functions; randomized/interleaved separation or size in a subsequent decision phase with eye tracking.

**Observed result:** Human side-choice functions departed markedly from ideal step functions (Fig. 5); the authors report idiosyncratic center/side biases and no adaptation across condition values.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Individual rather than generic sensitivity functions; both eccentricity and size manipulations; randomized/interleaved conditions; participants unaware of experimental purpose.

**Alternative explanations not excluded:** Strategy-switching/cognitive costs, motor preferences, center-of-mass heuristics, or task-specific mismatch to learned heuristics. The authors do not establish which explains the behaviour.

**Scope limitations:** One-saccade, three-destination, artificial dot-discrimination task in six students; claims do not directly extend to multi-saccade or natural-scene search.

**Source pointer:** Results, “Decision phase—Strategy,” Fig. 5; Discussion, “Summary,” pp. e1002342: 1–10 (HTML source).

### The suboptimal strategy reduced attainable reward, while observers could execute model-selected saccades.

**OBSERVATION:** Decision-phase strategies reduced expected winnings by 9% on average (range 6.1–17%). In a verification phase that indicated the model-optimal target token, mean gain increased and was indistinguishable from model-predicted maximum expected gain.

**AUTHOR INTERPRETATION:** Failure in the decision phase reflects saccadic strategy selection rather than inability to perform the prescribed eye movements or to discriminate after them.

**INFERENCE:** The verification phase strengthens the task-specific account of suboptimal choice, but it cannot isolate all differences between self-selected and instructed movement planning.

**Intervention or measurement:** Decision phase versus verification phase, in which a token disappearance instructed the model-predicted saccade before movement.

**Observed result:** Verification-phase points lay around the model’s maximum-gain line (Fig. 6); authors report formal rejection of maximum expected gain overall in both experiments, with one Experiment-1 observer not significantly different individually.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Same basic protocol across decision and verification phases; trial abort/replay for saccades outside a 1° radius of the indicated object; sensitivity estimates rederived from other sessions gave the same qualitative conclusion.

**Alternative explanations not excluded:** An instruction cue may alter attention, decision time, or planning relative to free selection; rewards may not fully represent participants' internal costs.

**Scope limitations:** Expected-gain loss pertains to this payoff and discrimination design, with model estimates of each observer's sensitivity.

**Source pointer:** Results, “Performance (Gain),” Fig. 6; Results, sensitivity-estimation robustness; Discussion, “Summary.”

### Sequential and oculomotor biases may describe the observed choices, but causal explanation remains unresolved.

**OBSERVATION:** Participants favored the nearer side when choosing a side (reported proportions 0.64–0.99) and repeated prior strategies above their overall frequencies (side: 0.76 vs 0.50, p=0.04; center: 0.60 vs 0.50, p=0.03).

**AUTHOR INTERPRETATION:** These dependencies characterize choices beyond the generic claim of suboptimality; simple heuristics are proposed as a possible account.

**INFERENCE:** These associations are consistent with motor or sequential heuristics, but they do not establish that a particular heuristic caused the failure to adapt.

**Intervention or measurement:** Analysis of saccade endpoints and conditional trial-to-trial strategy frequencies.

**Observed result:** Repeating conditions did not significantly raise optimal-choice probability (0.59 versus 0.57 overall; one-tailed p=0.19).

**Causal strength:** CORRELATIONAL

**Controls:** Conditions were randomized and interleaved; authors tested whether repeated conditions improved optimal choices.

**Alternative explanations not excluded:** Recent-choice dependence could be a consequence rather than cause of ignorance of the correct strategy.

**Scope limitations:** Small samples and task-specific endpoint constraints limit inference about general oculomotor biases.

**Source pointer:** Results, “Saccade length” and “Inter-trial dependencies”; Discussion, “Heuristic based planning.”

## Important controls

- Sensitivity was measured separately for each observer before decision modelling (Fig. 4).
- The critical prediction was varied two ways: token separation in Experiment 1 and target size in Experiment 2.
- Condition values were randomized and interleaved, limiting simple blocked reinforcement learning.
- Verification forced the predicted optimal destination and tested whether predicted gain could be realized (Fig. 6).
- Recomputing sensitivity from decision or verification sessions did not change the qualitative conclusion (Results, after Fig. 6; Fig. S3).
- Latency did not appear to predict closeness to optimality (Fig. S2).

## Critical assumptions

- The fitted retinal sensitivity function accurately predicts post-saccadic discrimination probability.
- Maximizing probability correct/expected gain in this task represents the relevant normative policy; authors show equivalence to minimizing saccades only for their stipulated modified task.
- The three allowed destinations adequately describe available strategies.
- Monetary reward captures the objective participants ought to optimize, apart from unmeasured planning costs.

## Limitations

- Six undergraduate participants across two experiments; Experiment 2 has two observers.
- Artificial, constrained one-saccade task with three marked destinations and a dot-up/dot-down target.
- Abort criteria and endpoint categorization impose an analysis structure; authors state failed 1° endpoints cannot by themselves reveal intended destinations.
- The authors explicitly leave possible cognitive costs of planning unmeasured and do not show that they explain choices.
- Results test a specific expected-gain policy, not every Bayesian, heuristic, salience, or natural-search account.

## What this paper supports

- In this controlled task, participants did not adapt first-saccade center/side strategy to individual sensitivity-predicted changes in separation or size.
- Prescribed model-optimal saccades improved attainable gain, supporting a task-specific strategy-selection deficit relative to the model.

## What this paper does not establish

- That human visual search generally ignores extrafoveal sensitivity.
- That the proposed heuristic/motor-preference account caused the observed suboptimality.
- A direct contradiction of the earlier near-optimal aggregate-performance result in a different target/noise regime.
- That free search with multiple saccades, natural scenes, or different incentives follows the same policy.

## Explicit open questions

- Whether hidden cognitive planning costs are real and sufficient to explain the observed strategy choices (Discussion, “Summary”).
- Which heuristic rules, if any, govern human saccade selection and when they approximate ideal performance (Discussion, “Heuristic based planning”).
- Whether altered retinal sensitivity leads to the predicted adjustment in search strategy (Discussion, “Heuristic based planning”).

## Evidence concerns

**Replication:** No independent replication is reported in this article.

**Measurement limitations:** Retinal sensitivity was estimated outside a saccade in the primary mapping session; authors note a preceding saccade could transiently alter sensitivity, then report robustness when estimating it from other sessions.

**Potential confounding:** Instruction during verification can change attention/planning; monetary gain may omit cognitive and motor costs. Sequential dependencies are descriptive and causally ambiguous.

**Statistical / experimental concerns:** Small observer samples; one Experiment-1 observer was not individually significantly different from maximal expected gain. The reported tests and effect summary are condition-specific.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002342 — Abstract |
| Full paper | https://doi.org/10.1371/journal.pcbi.1002342 — full HTML inspected |
| Main result | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002342 — Results: “Decision phase—Strategy,” Fig. 5; Discussion: “Summary” |
| Important control | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002342 — Fig. 4; Fig. 6; Results following Fig. 6; Methods: “Experimental design” |
| Limitations | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002342 — Discussion: “Summary” and “Heuristic based planning” |
