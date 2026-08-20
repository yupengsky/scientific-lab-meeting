# Deep Reinforcement Learning for High Precision Assembly Tasks

## Metadata

**Authors:** Tadanobu Inoue; Giovanni De Magistris; Asim Munawar; Tsuyoshi Yokoya; Ryuki Tachibana

**Year:** 2017

**arXiv:** 1708.04033v2

**Published venue:** IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Vancouver, 2017

**DOI:** UNCLEAR (the inspected arXiv record supplies only the arXiv DataCite DOI: 10.48550/arXiv.1708.04033)

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://arxiv.org/pdf/1708.04033

**Evidence role:** HIGH-LEVERAGE SUPPORTING

## Scientific question

Can online deep reinforcement learning using routine force/torque and position sensing acquire a tight-clearance peg-in-hole search-and-insertion skill on a real industrial robot, despite placement and angular errors larger than nominal robot precision?

## Exact system and regime

7-axis articulated robot arm with gripper and 6-axis force/torque sensor (force resolution 0.024 N); steel 34.990-mm or 34.980-mm cylindrical pegs into a 35.000-mm steel hole (10 or 20 µm clearance), while stated arm accuracy is ±60 µm. The peg begins grasped and in contact with the hole plate. Search and insertion are trained as separate online Q-learning policies, each a two-layer LSTM (20 and 15 units), from force/moment plus encoder-derived position inputs. Reported post-learning tests: 100 executions each for (A) 3-mm offset/10-µm clearance/0° tilt and (B) 1-mm offset/20-µm clearance/1.6° tilt. [§IV, pp. 4–6; Table I–II]

## Main claims

### An LSTM Q-learning policy completed the reported high-precision assembly trials.

**OBSERVATION:** After learning, the robot achieved a reported 100% success rate across 100 trials in each of two tested conditions. Mean total times were 4.68 s for case A and 4.36 s for case B; the table also reports 3.47 s for an additional proposed-method condition (1-mm offset, 10-µm clearance, 0° tilt).

**AUTHOR INTERPRETATION:** The technique acquires fitting skills robust to the tested position and angle errors.

**INFERENCE:** In this apparatus and narrow set of initial errors, a learned sensor-feedback policy can compensate for errors exceeding the listed arm accuracy and can execute 10-µm-clearance insertion.

**Intervention or measurement:** Train separate recurrent Q-learning policies online for search then insertion; execute post-learning peg-in-hole trials. State includes force/moment and coarse encoder position; actions are discrete force/rotation commands.

**Observed result:** Table II reports the 100/100 outcome and execution-time means above; Fig. 10 gives time distributions.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Same method evaluated at two clearance/offset/tilt combinations; preliminary sensor-force calibration informed the 20-N search force. A catalog specification for a fixed-search-pattern system is tabulated, not experimentally re-run side by side.

**Alternative explanations not excluded:** Success could depend on the particular robot, steel parts, initial contact state, reward/goal thresholds, staged training, and hand-tuned action/state design. No ablation isolates the LSTM, online learning, position quantization, or curriculum contributions.

**Scope limitations:** Only cylindrical steel peg/hole geometry; two post-learning cases; maximum tested tilt 1.6°; task begins after grasp/contact; policies are trained for each configuration.

**Source pointer:** §IV.C, p. 6; Table II; Fig. 10; https://arxiv.org/pdf/1708.04033

### Learning performance improved during the reported search-phase training run.

**OBSERVATION:** For the 10-µm-clearance, 0°-tilt, 1-mm-offset search condition, Fig. 9 displays increasing reward and a reduced number of steps over episodes (moving 20-episode windows with 90% confidence bounds).

**AUTHOR INTERPRETATION:** The learning converged and the search phase became more efficient.

**INFERENCE:** The reported training trace is consistent with within-condition policy improvement; it does not quantify generalization to unseen configurations.

**Intervention or measurement:** Online RL training on the physical robot, with random added initial-position error direction and staged initial offsets (1 then 3 mm).

**Observed result:** Reward rose and successful-search step count fell in the plotted 1-mm-offset condition.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Initial exploration decayed across episodes; subsequent 3-mm training initialized from the 1-mm-trained network. No untrained, feed-forward, or fixed-pattern experimental baseline is reported for this trace.

**Alternative explanations not excluded:** Changes reflect the combined algorithm, reward shaping, curriculum, exploration schedule, and apparatus-specific sensor signals.

**Scope limitations:** Plot is one clearance/tilt/offset regime and uses moving-window summaries; raw trial outcomes and independent training seeds are not reported.

**Source pointer:** §IV.A, pp. 5–6; Fig. 9; https://arxiv.org/pdf/1708.04033

## Important controls

- Sensor calibration set peg orientation so Mx and My were zero under a 20-N downward force; nine position/force combinations established that 10 N gave no detectable moment whereas 20 and 30 N did. The authors selected 20 N to limit wear. [§IV.A, p. 5; Figs. 7–8]
- Search and insertion use separate networks. Search is trained before insertion, so insertion tests depend on the learned search skill. [§IV, p. 4; §IV.B, p. 5]
- Table II juxtaposes reported method times with a conventional fixed-search-pattern product-catalog specification. It is a contextual comparison, not a matched experimental control. [§IV.C, p. 6; Table II]

## Critical assumptions

- Force/moment histories and encoder-derived positions contain enough information for state estimation under contact and controller delay; the authors motivate LSTM because robot action effects are observed two cycles later. [§III, p. 4]
- The peg is pre-grasped and already contacting the plate. [§IV, p. 4]
- The discrete action set and reward thresholds represent successful search/insertion adequately. Search success is defined by 0.5-mm vertical drop; insertion by 19-mm downward displacement. [§IV.A–B, pp. 5–6]
- Training-position perturbations in 16 randomly selected directions provide useful robustness to deployment position error. [§IV.A, p. 5]

## Limitations

- **Explicitly stated by authors:** A skill is learned for each configuration using online learning; generalization across materials, manipulators, insertion angles, and shapes remains future work. [§V, p. 6]
- **Explicitly stated by authors:** The approach has a discrete action set; comparison with continuous-control approaches is left for future analysis. [§V, p. 6]
- The paper does not report cross-configuration holdout performance, repeated independent training runs, failure modes, or ablations. These are reporting limits, not author-stated limitations.

## What this paper supports

Physical-robot evidence that the specified recurrent Q-learning system achieved the reported successful tight-clearance cylindrical peg-in-hole executions in two constrained steel-part test regimes, using force/torque and encoder sensing.

## What this paper does not establish

General transfer across robot models, materials, geometries, or wider error distributions; superiority over a matched conventional or non-recurrent RL baseline; sample efficiency; robustness under grasp acquisition, vision occlusion, or production-line variation; causal necessity of LSTM or any individual design choice.

## Explicit open questions

- Can pooled trials from multiple robots yield a more general cloud-trained model?
- Can the model handle different materials, manipulators, insertion angles, and shapes?
- How does this discrete-action method compare with continuous-space learning such as A3C or DDPG?

Source: §V, p. 6.

## Evidence concerns

**Replication:** No independent replication or multi-seed repetition is reported.

**Measurement limitations:** Success is operationalized by vertical-displacement thresholds; reported task completion does not separately quantify alignment quality, contact force, wear, or part damage.

**Potential confounding:** Initial-contact setup, fixed steel geometry, staged curriculum, custom sensing/control stack, and training/test configuration coupling may contribute to reported performance.

**Statistical / experimental concerns:** The 100 trials per reported case establish an empirical run count, but the paper does not state randomization, independence, confidence intervals for success rate, or an experimentally matched baseline. Fig. 9 confidence bounds are moving-window training summaries.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://arxiv.org/abs/1708.04033; abstract |
| Full paper | https://arxiv.org/pdf/1708.04033 |
| Main result | https://arxiv.org/pdf/1708.04033; §IV.C, p. 6; Table II; Fig. 10 |
| Important control | https://arxiv.org/pdf/1708.04033; §IV.A, p. 5; Figs. 7–8 |
| Limitations | https://arxiv.org/pdf/1708.04033; §V, p. 6 |
