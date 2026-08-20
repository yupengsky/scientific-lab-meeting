# Robust, Compliant Assembly via Optimal Belief Space Planning

## Metadata

**Authors:** Florian Wirnshofer; Philipp S. Schmitt; Wendelin Feiten; Georg v. Wichert; Wolfram Burgard

**Year:** 2018

**arXiv:** arXiv:1811.03904

**Published venue:** 2018 IEEE International Conference on Robotics and Automation (ICRA)

**DOI:** 10.1109/ICRA.2018.8460995

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://arxiv.org/pdf/1811.03904

**Evidence role:** HIGH-LEVERAGE SUPPORTING

## Scientific question

Can a sampling-based belief-space planner generate low-force, robust compliant motions for uncertain rigid-part assembly directly from CAD geometry, without manually specified contact modes?

## Exact system and regime

Rigid-body assembly of a robot-held part to an environment-fixed part. Cartesian impedance control is simulated as a six-DoF spring-damper; initial grasp-transform uncertainty is represented by particles with Gaussian translational SD 2.5 mm and rotational SD 0.015 rad. Benchmarks: a three-mating-motion puzzle (1–2 mm tolerances), 0.5-mm-tolerance peg-in-hole, and zero-clearance fuse-on-top-hat-rail task. Planning uses 3- or 5-DoF projections and Bullet simulation; hardware uses a KUKA iiwa 7 R800, two-jaw gripper, wrist camera, and 200-Hz command interface. [§III.A, §V, §VI.A–B; pp. 2, 4–5]

## Main claims

### Particle belief-space planning improved simulated robustness over standard EST in the peg task

**OBSERVATION:** For Peg-3D plans evaluated under initial states drawn from the planning distribution, standard EST had mean failure rate 31%; particle-based planning reached mean failure rate 1% with 12 particles. Each plan was evaluated in 100 trials and the plan–evaluate procedure was repeated 50 times.

**AUTHOR INTERPRETATION:** The particle representation gives a robustness gain for parts assembly.

**INFERENCE:** Under this simulated uncertainty model, optimizing a trajectory across sampled initial states is associated with substantially lower failure than planning for the standard EST formulation; it does not establish robustness to uncertainty distributions outside that model.

**Intervention or measurement:** Vary particle number N while planning Peg-3D trajectories; evaluate failures across 100 sampled initial states per plan.

**Observed result:** 31% mean failure for standard EST versus 1% at N=12 particle-based planning.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Standard EST baseline; same stated initial-state distribution for planning and evaluation; 50 repetitions.

**Alternative explanations not excluded:** Simulator/contact-model fidelity; benefit of the particular noise distribution and particle count; comparisons involving a particle-based B-EST formulation rather than an isolated change only in uncertainty representation.

**Scope limitations:** One simulated Peg-3D benchmark; results do not quantify performance under unmodeled dynamics, sensing feedback, or physical execution.

**Source pointer:** §VI.C, Fig. 6, pp. 5–6, https://arxiv.org/pdf/1811.03904

### AO-B-EST achieved higher success rates than EST in three physical assembly benchmarks

**OBSERVATION:** Across 14 planned trajectories per task, each executed five times (70 trials/planner/task), physical success rates were Peg-5D 96% versus 67%, Rail-3D 90% versus 51%, and Puzzle-5D 90% versus 54% for AO-B-EST versus EST. The authors report Fisher exact-test p-values of 1.63e-5, 6.81e-7, and 3.40e-6, respectively; they also flag dependence among five executions of a common trajectory.

**AUTHOR INTERPRETATION:** AO-B-EST robustly outperforms the baseline despite imposed grasp-pose uncertainty and simulation-to-reality differences.

**INFERENCE:** In this calibrated KUKA setup with artificially distorted grasp-pose knowledge, the complete AO-B-EST pipeline was associated with higher assembly success than the evaluated EST baseline. The experiment does not isolate contributions from belief representation, AO optimization, or other implementation choices.

**Intervention or measurement:** Compare AO-B-EST (N=10) and EST on Peg-5D, Puzzle-5D, and Rail-3D planned trajectories executed on hardware; inject planning-matched Gaussian grasp-pose noise into the system’s pose knowledge.

**Observed result:** AO-B-EST success exceeded EST by 29, 39, and 36 percentage points for peg, rail, and puzzle, respectively.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Same three task families; 14 trajectories and five executions each per planner/task; online Fisher exact test and offline trajectory-level Welch t-test analyses.

**Alternative explanations not excluded:** Repeated executions per trajectory violate trial independence for the online analysis; the physical setup was more precise than the planning uncertainty assumption; results may depend on the selected force/torque bounds and artificially injected uncertainty.

**Scope limitations:** Three rigid-part tasks on one robot/setup; no comparison with broader state-of-the-art planners; sensor feedback beyond impedance control is absent from the model.

**Source pointer:** §VI.D, Table I, pp. 6–7, https://arxiv.org/pdf/1811.03904

### Formal completeness and asymptotic-optimality guarantees are conditional

**OBSERVATION:** The authors map deterministic, finitely parameterized belief evolution to kinodynamic planning in belief-parameter space. They derive probabilistic completeness for B-EST under α-β expansiveness and nonzero reachable-goal volume, and asymptotic optimality for AO-B-EST with the additional AO-x well-behavedness condition.

**AUTHOR INTERPRETATION:** The proposed planner is probabilistically complete and asymptotically optimal under these conditions; experiments strongly indicate expansiveness for their assembly domain.

**INFERENCE:** The paper supplies conditional theoretical guarantees, not a demonstration that the real assembly domains meet all assumptions.

**Intervention or measurement:** Mathematical reduction to EST/AO-x assumptions; empirical convergence and solution-rate plots in five simulated benchmark variants.

**Observed result:** Cost decreased over planning time in reported simulations; no direct proof that the benchmark belief spaces satisfy expansiveness.

**Causal strength:** CAUSAL EVIDENCE

**Controls:** Guarantees explicitly trace to prior EST and AO-x results under stated assumptions.

**Alternative explanations not excluded:** Failure of α-β expansiveness, nonzero reachable-goal volume, or the AO-x well-behavedness condition in a given assembly domain.

**Scope limitations:** Deterministic belief propagation requires omitting measurement updates; finite particle parameterization approximates the belief.

**Source pointer:** §IV.C, §VI.C, pp. 4–6, https://arxiv.org/pdf/1811.03904

## Important controls

- All three benchmark types used a common algorithm version, cost function, and no manually specified constrained/free-motion directions or surfaces. [§VI.A, p. 5]
- Hardware comparison uses the same task families and reports both trial-level and trajectory-level analyses. [§VI.D, pp. 6–7]
- Simulated particle-number evaluation samples evaluation initial states from the planning distribution. [§VI.C, pp. 5–6]

## Critical assumptions

- The grasped part is rigidly attached; particle dynamics and impedance-controlled contact are adequately represented by the simulator.
- Initial grasp-transform Gaussian noise captures relevant uncertainty; measurement updates are omitted so belief evolution remains deterministic.
- The conditional theory assumes α-β expansiveness, nonzero relative reachable-goal volume, and AO-x well-behavedness.
- Hardware impedance parameters match planning parameters. [§III.A–B, §IV.C, §V, §VI.B]

## Limitations

- Authors explicitly omit sensor feedback beyond active impedance control and identify extension to a full POMDP as future work.
- The 30-N / 3-Nm force/torque limits sometimes produced grasp slippage, violating the rigid-grasp assumption.
- The authors state that the online Fisher analysis may be biased because groups of five trials share a planned trajectory.
- The paper calls for comparison to related state-of-the-art planners and extension to deformable objects. [§VI.D, §VII, pp. 6–7]

## What this paper supports

Evidence that, in the stated simulated and KUKA physical rigid-assembly settings, an AO-B-EST implementation using particle-modeled grasp uncertainty attained higher success rates than its EST baseline and can produce executable compliant trajectories from CAD geometry, initial pose, and goal condition.

## What this paper does not establish

General real-world optimality or robustness; validity of the theory’s expansiveness/well-behavedness assumptions for arbitrary assembly; robustness under sensor-feedback belief updates, deformable parts, unmodeled uncertainty, or other robots; superiority over all contemporary planners.

## Explicit open questions

- Incorporating sensor feedback through a full POMDP model.
- Handling increasingly complex dynamics, including deformable objects.
- Thorough comparison with related state-of-the-art planners. [§VII, p. 7]

## Evidence concerns

**Replication:** No independent replication reported.

**Measurement limitations:** Physical grasp uncertainty was imposed by corrupting system knowledge in a setup the authors say was more precise than the planning assumption; the study does not measure naturally occurring uncertainty distribution.

**Potential confounding:** The planner changes both belief-space/particle handling and the AO-B-EST planning procedure relative to EST; the reported comparison does not decompose these effects.

**Statistical / experimental concerns:** Five physical executions share each planned trajectory, so 70 trial-level samples are not independent; authors identify this as a potential bias. The offline analysis reduces to 14 trajectory means under independent Gaussian-distribution assumptions.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://arxiv.org/pdf/1811.03904, p. 1 |
| Full paper | https://arxiv.org/pdf/1811.03904, pp. 1–8 |
| Main result | https://arxiv.org/pdf/1811.03904, §VI.C Fig. 6 pp. 5–6; §VI.D Table I pp. 6–7 |
| Important control | https://arxiv.org/pdf/1811.03904, §VI.A p. 5; §VI.D pp. 6–7 |
| Limitations | https://arxiv.org/pdf/1811.03904, §VI.D and §VII pp. 6–7 |
