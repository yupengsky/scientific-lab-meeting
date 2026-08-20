# Scientific Problem Map

**Status:** COMPLETE

**Topic:** Mechanistic understanding of robust contact-rich robotic assembly under physical and perceptual uncertainty.

## Distinct phenomena

1. **Contact accommodation during mating:** whether geometry, friction, support compliance, and impedance lead contact forces to correct misalignment or to jam. This is a physical interaction phenomenon.
2. **Pre-insertion pose localization:** reducing ambiguity about relative pose through contact probes or other observations before committing to insertion. This is a state-estimation phenomenon.
3. **Reactive residual-error correction:** selecting actions after contact from force/torque, tactile, visual, and/or position histories. This is a closed-loop control phenomenon.
4. **Uncertainty-aware motion selection before execution:** selecting compliant trajectories that are robust across modeled initial states. This is a planning phenomenon.
5. **Transfer and system reliability:** retaining assembly performance when the controller, contact model, sensing, and deployment system differ from training or planning conditions. This is a system-integration phenomenon. Terminal insertion success, engagement, slip, wedging, and recovery are separate outcomes.

## Explanatory levels

- **Contact-mechanical:** geometry, friction, stiffness, compliance-center placement, contact forces, jam/tilt.
- **State-estimation / perceptual:** what contact, tactile, force, or visual observations identify about relative pose and contact state.
- **Control / policy:** how observations and action histories are converted into compliant corrective motion.
- **Planning / uncertainty representation:** how initial uncertainty is represented when trajectories are selected.
- **System / transfer:** simulator mismatch, grasp and perception errors, fixture/calibration effects, and component failure modes.

Evidence presently connects these levels in selected systems; it does not establish one general causal chain from sensing through contact mechanics to reliable industrial assembly.

## Established knowledge

- **CONSENSUS:** Contact-rich insertion is strongly regime-dependent. Clearance, geometry, initial translational/angular error, friction, compliance, sensing, controller, fixture, and success definition materially constrain claims. [whitney_1982; chhatpar_branicky_2003; inoue_2017; dong_2021; lenz_2024; wirnshofer_2018; tang_2023]
- **CONSENSUS:** In the quasi-static rigid-part model, support compliance, geometry, and friction alter contact-force paths and jamming conditions. Whitney reports experimental force-model verification, though the card is partial and quantitative validation is unavailable. [whitney_1982]
- **CONSENSUS:** Contact observations can reduce pose ambiguity in restricted, discretized simulated localization settings; resolution produces an error/reliability/computation trade-off. [chhatpar_branicky_2003]
- **CONSENSUS:** Several closed-loop approaches achieved successful physical insertion in their own constrained regimes: recurrent force/position RL at 10–20 micrometre cylindrical clearances; tactile RL at 3-mm clearance with selected held-out objects; vision+tactile RL in a 0.5-mm peg/hole regime; and simulation-trained policies on fixed-workcell parts. These are intervention evidence for complete systems, not universal mechanism claims. [inoue_2017; dong_2021; lenz_2024; tang_2023]
- **CONSENSUS:** Modeling initial uncertainty during compliant planning improved success relative to the stated EST baseline in the simulated and physical rigid-part regimes of Wirnshofer et al. [wirnshofer_2018]
- **CONSENSUS:** Full insertion and partial engagement are empirically distinct. In IndustReal, engagement exceeded full-insertion success and slip/wedging remained observed failures. [tang_2023]

## Explanatory families and relations

| Family | Proposed explanation of robustness | Evidence and scope | Relation to other families |
|---|---|---|---|
| Passive / active compliance | Favorable support or impedance behavior lets contact forces accommodate error. | Quasi-static rigid planar model with stated 3-D force verification; sensorless 0.1-mm result is abstract-only. [whitney_1982; park_2017] | **COMPOSITIONAL** with planning and feedback; **PARTIALLY COMPETING** with sensing when either can address the same residual error. |
| Explicit contact-state localization | Contact sequences identify pose/contact hypotheses, enabling alignment actions. | Deterministic, discretized 2-D/3-D simulations; full 6-DoF physical generality unshown. [chhatpar_branicky_2003] | **COMPOSITIONAL** with reactive control; **DIFFERENT LEVELS OF EXPLANATION** from mechanics. |
| Learned force/tactile/visual feedback | Sensor histories support corrective motion under partial observability. | Physical, but tightly scoped robot/geometry/error-distribution evidence; modality effects contain architecture/training confounds. [inoue_2017; dong_2021; lenz_2024] | **PARTIALLY COMPETING** among modalities for the same state information; **COMPOSITIONAL** with compliance. |
| Belief-space / robust planning | Selecting trajectories across modeled pose uncertainty avoids forceful or failure-prone contact paths. | Simulated and KUKA rigid-part tasks; deterministic belief propagation omits measurement updates. [wirnshofer_2018] | **COMPOSITIONAL** with compliance; **DIFFERENT LEVELS OF EXPLANATION** from reactive sensing. |
| Simulation-to-real training and deployment compensation | Contact-model-aware training, rewards/curricula, and deployment action integration yield transferable policies. | Strong simulation ablations and reported fixed-workcell hardware outcomes; no full-task hardware transfer baseline. [tang_2023] | **COMPOSITIONAL** with controller/compliance; **RELATION UNKNOWN** to tactile sensing and explicit localization in matched tests. |

## Evidence and scope matrix

| Claim | Evidence type / causal strength | Scope and important confounders |
|---|---|---|
| Compliance changes modeled insertion mechanics. | Analytical model plus reported experimental force verification; **INTERVENTION EVIDENCE** for model parameter variation, limited physical detail. | Small-angle, planar, rigid, quasi-static, constant-friction model; gravity/inertia omitted. [whitney_1982] |
| Contact-map matching localizes relative pose. | Grid-resolution interventions; **INTERVENTION EVIDENCE** in simulations. | Deterministic contact sensing/actuation, restricted motions and surfaces; physical quantitative outcomes unavailable. [chhatpar_branicky_2003] |
| Recurrent force/position policy performs tight insertion. | Trained and executed real robot policy; **INTERVENTION EVIDENCE**. | Two steel cylindrical configurations, pre-contact start, configuration-specific training; no matched baseline or seed replication. [inoue_2017] |
| Tactile RL transfers across selected objects and may help rotation-sensitive geometries. | Policy and representation/curriculum comparisons; **INTERVENTION EVIDENCE**. | 3-mm clearance, one hardware stack; F/T comparison also changes architecture and training schedule. [dong_2021] |
| Vision+tactile input improves 0.5-mm performance. | Modality-policy comparison; **INTERVENTION EVIDENCE** for the reported setup. Axis Shapley attribution is **CORRELATIONAL**. | One peg/hole platform, 20 trials/condition, incomplete seed reporting; training clearance can confound comparisons. [lenz_2024] |
| Belief-space planner improves physical task success versus EST. | Planner comparison; **INTERVENTION EVIDENCE**. | Artificially corrupted grasp knowledge; five executions share a trajectory; no sensor-feedback belief updates. [wirnshofer_2018] |
| Sim-trained policy transfers to reported hardware assemblies. | Hardware deployment; **INTERVENTION EVIDENCE** for the complete system. | Fixed Franka/camera/breadboard, selected assets, calibration/manual target heights; no full-task hardware baseline. [tang_2023] |

## Tensions, anomalies, and limiting evidence

- **POTENTIAL TENSION — NEEDS VERIFICATION:** Sensor-minimal compliant assembly is reported by Park, while tactile and force/vision feedback systems report benefits in difficult regimes. The claims are not directly comparable: Park is abstract-only and lacks error distribution, trial outcomes, and controller details; the other cards use different robots, geometries, clearances, and sensing stacks. [park_2017; dong_2021; lenz_2024]
- **POTENTIAL TENSION — NEEDS VERIFICATION:** Tactile RL exceeds the compared F/T RL on selected cuboid-like held-out objects, whereas F/T RL is competitive or better on round-edged objects. The experiment changes modality, policy architecture, and training procedure, so the causal source of the difference is unresolved. [dong_2021]
- **ANOMALY / measurement limitation:** High binary success can mask distinct failure modes and physical quality. Inoue uses displacement thresholds; Dong infers success from a slip detector; IndustReal separates engagement from full insertion and observes wedging/slip. These metrics cannot be treated as interchangeable measures of alignment, contact load, wear, or recovery. [inoue_2017; dong_2021; tang_2023]
- **LIMITING EVIDENCE:** Classical contact localization scales poorly in the reported sampled representation, while learned policies can succeed in restricted physical tasks. This does not establish that learning resolves the localization scaling problem, because the state representations, tasks, and evaluation metrics differ. [chhatpar_branicky_2003; inoue_2017; dong_2021]

## Composite explanations under challenge

**INFERENCE — composite hypothesis:** Robust assembly may arise when compliance shapes contact dynamics, planning selects motions robust to modeled uncertainty, and sensing/policies correct residual unmodeled error.

This is coherent across levels, yet unproven. The cards do not provide a factorial comparison that identifies the marginal or interaction effects of physical compliance, explicit belief/state estimation, reactive sensing, and planning under common geometry, uncertainty, safety, and time constraints. Existing evidence mainly evaluates bundled systems or single-family comparisons. Sim-to-real wedging and slip further show that a coherent composite does not guarantee system reliability. [whitney_1982; wirnshofer_2018; dong_2021; lenz_2024; tang_2023]

## Structured uncertainty nodes

### U01 — Physical conditions for passive versus feedback-dependent error accommodation

- **Phenomenon:** Alignment, jamming, and insertion under initial pose error.
- **Established knowledge:** Compliance, geometry, and friction affect quasi-static mating; several feedback systems can correct errors in their tested regimes. [whitney_1982; inoue_2017; dong_2021; lenz_2024]
- **Exact unknown:** The boundary in clearance, geometry, friction variation, pose error, and stiffness at which compliance alone remains sufficient versus feedback materially changes reliability.
- **Relevant explanations:** passive/active compliance; explicit contact localization; learned reactive feedback.
- **Relationship among explanations:** **PARTIALLY COMPETING** for a shared residual-error problem; **COMPOSITIONAL** in a full system.
- **Supporting and limiting evidence:** Whitney supports the mechanical premise under restricted assumptions. Park's claimed sensorless result is abstract-only. Feedback results use nonmatched systems and bundles. [whitney_1982; park_2017; inoue_2017; dong_2021; lenz_2024]
- **Causal strength:** Mechanical model support and system-level interventions; no cross-family causal comparison.
- **Scope and confounders:** Geometry, initial state, controller implementation, fixture/passive compliance, success metric, and unreported Park details.
- **Why insufficient:** No shared test distribution or component-isolating evidence.
- **Observation type that would reduce uncertainty:** Matched phase-resolved outcomes across controlled error, friction, clearance, and stiffness conditions with identical task and success definitions.
- **References:** [whitney_1982; park_2017; inoue_2017; dong_2021; lenz_2024]

### U02 — What contact sensing identifies, and when it enables causal corrective control

- **Phenomenon:** Inferring relative pose/contact state from contact, force, tactile, and visual observations.
- **Established knowledge:** Contact-map observations localize in restricted simulations; sensor-feedback policies achieve task success; one policy attribution suggests axis-specific modality use. [chhatpar_branicky_2003; inoue_2017; dong_2021; lenz_2024]
- **Exact unknown:** Which observation histories uniquely identify actionable translational, rotational, contact-mode, and jam states across geometries and uncertainty sources.
- **Relevant explanations:** explicit C-space matching; recurrent implicit state; tactile marker flow; force/torque; vision+tactile fusion.
- **Relationship among explanations:** **PARTIALLY COMPETING** as alternative estimators; **COMPOSITIONAL** with control; explicit versus implicit estimates are **DIFFERENT LEVELS OF EXPLANATION** from contact mechanics.
- **Supporting and limiting evidence:** Localization and policy success do not validate the same latent state. Lenz's Shapley result is correlational and one trajectory; Dong's modality contrast is confounded. [chhatpar_branicky_2003; dong_2021; lenz_2024]
- **Causal strength:** Interventions establish task effects for complete policies; causal identification of latent contact state remains unshown.
- **Scope and confounders:** Deterministic simulation, camera pose, recurrent-state dependence, sensor architecture, object selection, and training distribution.
- **Why insufficient:** Success metrics rarely include independently measured contact state or alignment trajectory.
- **Observation type that would reduce uncertainty:** Joint ground-truth relative pose/contact-mode measurements and sensor histories, with out-of-distribution geometry/error conditions and separated estimator versus controller outcomes.
- **References:** [chhatpar_branicky_2003; inoue_2017; dong_2021; lenz_2024]

### U03 — Robustness to modeled uncertainty versus naturally occurring uncertainty

- **Phenomenon:** Avoiding failure when grasp, perception, and contact conditions differ from nominal assumptions.
- **Established knowledge:** Particle belief-space planning improves over EST under its modeled/injected uncertainty; simulation-trained policies transfer in a reported fixed workcell. [wirnshofer_2018; tang_2023]
- **Exact unknown:** Whether robustness gains persist when uncertainty distributions, contact properties, and perception failures differ materially from the planner/training model.
- **Relevant explanations:** particle belief-space planning; simulator/contact-model-aware learning; deployment action integration; reactive sensing.
- **Relationship among explanations:** **COMPOSITIONAL**; relationship of explicit belief planning to reactive sensor feedback is **RELATION UNKNOWN** under matched evaluation.
- **Supporting and limiting evidence:** Wirnshofer injects grasp-pose error into knowledge in a precise system and omits measurement updates. Tang reports hardware transfer, yet calibration, fixtures, selected assets, and manual target heights remain important scope conditions. [wirnshofer_2018; tang_2023]
- **Causal strength:** Intervention evidence for each complete approach in its stated distribution; no causal evidence for robustness outside that distribution.
- **Scope and confounders:** Simulator fidelity, initial uncertainty distribution, fixture/calibration, policy/controller coupling, and task asset selection.
- **Why insufficient:** The cards do not characterize natural uncertainty distributions or conduct cross-method transfer tests.
- **Observation type that would reduce uncertainty:** Distribution-stratified reliability and failure-mode measurements under independently measured deployment uncertainty, including model-mismatch conditions.
- **References:** [wirnshofer_2018; tang_2023]

### U04 — Mechanisms and limits of apparent cross-geometry learned-policy generalization

- **Phenomenon:** Correcting insertion error for objects or contact geometries outside training.
- **Established knowledge:** Dong reports selected held-out-object performance; Tang reports transfer from peg/hole training to selected NEMA connectors; Inoue explicitly trains per configuration. [dong_2021; tang_2023; inoue_2017]
- **Exact unknown:** Whether apparent transfer follows shared contact geometry, sensor representations, object-shape similarity, task fixtures, or other hidden common structure.
- **Relevant explanations:** tactile marker-flow representation; curriculum; force/position recurrent policy; simulation randomization/reward design.
- **Relationship among explanations:** **PARTIALLY COMPETING** as sources of generalization; potentially **COMPOSITIONAL** within a policy pipeline.
- **Supporting and limiting evidence:** Dong's ablations associate curriculum/marker flow with performance but lack independent-seed uncertainty and clean modality controls. Tang's hardware results are system-level; Inoue reports no cross-configuration holdout result. [dong_2021; tang_2023; inoue_2017]
- **Causal strength:** Intervention evidence for specified pipelines; individual causal mechanisms remain incompletely isolated.
- **Scope and confounders:** Object selection, clearance, reset fixture, upstream pose estimate, architecture, training schedule, simulator assets, and task-specific grasp.
- **Why insufficient:** “Novel object” sets are small and lack a common geometry-distance or uncertainty taxonomy.
- **Observation type that would reduce uncertainty:** Generalization outcomes stratified by independently specified contact-geometry, clearance, and error-distribution differences, with component ablations measured on the same sets.
- **References:** [inoue_2017; dong_2021; tang_2023]

### U05 — Meaningful reliability measurement for contact-rich assembly

- **Phenomenon:** Distinguishing alignment, engagement, full insertion, force safety, damage/wear, and recovery after off-nominal contact.
- **Established knowledge:** Existing cards use heterogeneous terminal metrics; IndustReal documents a separation between engagement and full insertion and identifies slip/wedging. [inoue_2017; dong_2021; lenz_2024; tang_2023]
- **Exact unknown:** Which phase-resolved measurements are necessary to make robustness claims comparable and to attribute failures to mechanics, estimation, policy, or transfer.
- **Relevant explanations:** genuine contact-mechanical correction; threshold/metric artifact; upstream perception/grasp failure; deployment mismatch.
- **Relationship among explanations:** **COMPOSITIONAL** failure sources; **RELATION UNKNOWN** without phase-resolved measurement.
- **Supporting and limiting evidence:** Displacement/slip-detector success can register terminal completion without contact-load, alignment-quality, or damage measurements. [inoue_2017; dong_2021] IndustReal's engagement/full-success split demonstrates the metric distinction. [tang_2023]
- **Causal strength:** Observational measurement limitation, not evidence that any one failure source causes all reported failures.
- **Scope and confounders:** Success thresholds, trial reset, unreported failure classification, sensor calibration, and dependence among repeated planned trajectories.
- **Why insufficient:** No shared outcome ontology or matched measurement suite across cards.
- **Observation type that would reduce uncertainty:** Time-resolved contact state, relative pose, forces/torques, terminal seating, damage/wear, and recovery outcomes reported with clear denominators and uncertainty.
- **References:** [inoue_2017; dong_2021; lenz_2024; wirnshofer_2018; tang_2023]
