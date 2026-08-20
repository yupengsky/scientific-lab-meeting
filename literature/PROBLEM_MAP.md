# Scientific Problem Map

**Status:** COMPLETE

**Scope and provenance.** This map addresses mechanistic understanding of active visual perception under partial observability and environmental uncertainty. It uses the current paper cards as primary evidence. The `isoda_etal_2024` record is excluded: the index records a source-metadata mismatch. `glaser_etal_2020` is also not used as evidence for FEF prior-to-saccade selection: its card is *Machine Learning for Neural Decoding* (motor/somatosensory cortex and rat hippocampus), which does not match the index entry. This is **NEEDS_VERIFICATION** against the intended original source.

## Distinct phenomena

1. **Foveated target search and next-fixation choice.** A target location is hidden; foveal/peripheral sensitivity, target prior, time, and action constraints affect one or more saccades. This includes the synthetic/natural-spectrum search benchmarks of Najemnik & Geisler, the one-saccade choice task of Morvan & Maloney, and the continuous-time Gabor-in-noise search of Zhou & Yu. It is distinct from category sampling and from transsaccadic displacement judgment.
2. **Sequential visual sampling for category inference.** Gaze reveals local evidence about a hidden category in masked, gaze-contingent displays. Yang et al. study synthetic-pattern category information; Mirza et al. study a structured 2x2 scene. These tasks make action-dependent observations explicit, but omit ordinary peripheral input.
3. **Perception across saccades under source-specific uncertainty.** Chari et al. manipulate external image blur and with-saccade versus no-saccade conditions in displacement judgments. The phenomenon is prior weighting in perceptual report, rather than selection of a next gaze location.
4. **Adaptation to environmental volatility.** Pasturel et al. study anticipatory pursuit and explicit direction prediction when latent motion statistics change. This concerns updating a predictive belief over trials, rather than visual search within a scene.
5. **Neural target selection.** SC activity covaries with selected saccade targets and focal SC inactivation impairs selection in monkey search. These results bear on circuit necessity/contribution, not on whether the selection objective is information gain, expected free energy, or cost-sensitive utility.
6. **Action/effort and embodied context.** Direction-dependent pupil-linked effort covaries with saccade choice, and cognitive load changes saccade distribution (Koevoet et al.). Natural behavior also couples eyes with head/body motion, task goals, scene structure, and memory (Goettker et al.). These scope factors cannot be reduced to the laboratory target-search phenomena without evidence.

## Explanatory levels

| Level | Evidence-supported content | Boundary |
|---|---|---|
| Computational / normative | Bayesian information gain, expected-cost POMDP control, and active-inference expected free energy define candidate action-evaluation rules. | A good behavioral fit does not establish that the brain computes the fitted objective. |
| Algorithmic / representational | Belief updating, learned priors, discriminative categorization, fixed-form scan heuristics, finite effective memory, and change-point-like volatility tracking describe behavior. | Cards do not establish a common representation across tasks or a unique algorithm. |
| Behavioral / oculomotor | Prior-, evidence-, uncertainty-, cost-, and volatility-sensitive choices, fixation patterns, pursuit, and reports have been measured under interventions. | Strongest claims are regime-specific and often based on small samples or constrained displays. |
| Neural circuit | SC prelude activity correlates with target selection; reversible SC inactivation causally disrupts selection. | No card supplies a causal circuit implementation of Bayesian, active-inference, discriminative, memory, or volatility computations. |
| Ecological / embodied | Head/body movements, changing task goals, and rich scene structure alter the information and cost landscape. | Current direct mechanistic evidence is primarily head-restrained and screen-based. |

## Established knowledge

- **CONSENSUS:** Active visual behavior depends on partial observations and prior/task context in multiple controlled paradigms. Spatial priors alter fixation/choice dynamics (Ahmad et al.); accumulated local evidence guides category sampling (Yang et al.); learned motion statistics alter anticipatory pursuit and explicit reports (Pasturel et al.).
- **CONSENSUS:** A measured-sensitivity Bayesian observer is a useful conditional benchmark for foveated search. It requires assumptions about scene statistics, visibility, priors, and objective (Najemnik & Geisler; Zhou & Yu).
- **CONSENSUS:** Generic unconstrained information-maximizing policies do not fully describe human scan paths in the tested tasks. Participants did not switch strategy at individual sensitivity-predicted optima in one constrained task (Morvan & Maloney); adding landing, amplitude, and effective-memory constraints improved a continuous-time Bayesian model’s scan-path fit (Zhou & Yu).
- **CONSENSUS:** Evidence relevant to uncertainty is heterogeneous. Categorical transsaccadic judgments showed decreased prior use with added external blur, whereas continuous reports and categorical judgments under saccade-related uncertainty were consistent with the tested Bayesian predictions (Chari et al.).
- **CONSENSUS:** SC contributes causally to target selection in the particular monkey visual-search regime tested by reversible inactivation (McPeek & Keller). SC prelude activity also covaries with selected target and, in a subset, motion coherence (Horwitz & Newsome). These statements do not identify the computation.
- **INFERENCE:** A useful working landscape separates an action-value problem (what next action is worthwhile), an observation/inference problem (what the observation means), and an implementation problem (how circuits generate the choice). The evidence supports each level separately more strongly than it supports a single unifying account.

## Explanatory families and relations

| Family | Claim and empirical scope | Relationship | Evidence / limits |
|---|---|---|---|
| Information-gain Bayesian search | Choose fixation expected to reduce uncertainty about target/category location. Defined for foveated target/noise search and synthetic-pattern sampling. | **PARTIALLY COMPETING** with fixed heuristics and pure extrinsic/cost objectives; **COMPATIBLE** with sensory/motor constraints. | Normative benchmark and reported near-optimal aggregate performance: Najemnik & Geisler (**PARTIAL** card). BAS captures synthetic-pattern maps and beats specified heuristics: Yang et al. Model-dependent; it does not establish neural computation or natural-scene generality. |
| Cost-sensitive Bayesian control | Select actions by expected error, time, and switching cost. | **COMPOSITIONAL** with Bayesian inference; **PARTIALLY COMPETING** with information gain when objectives produce different actions. | C-DAC reproduced an explicit-incentive three-location pattern that the paper’s Infomax implementation missed: Ahmad et al. Intrinsic cost remains unresolved because points imposed switch cost. |
| Bounded/constrained Bayesian search | Approximate an information benchmark subject to saccade amplitude, landing variability, memory, and temporal constraints. | **COMPOSITIONAL** with information-gain accounts; **COMPATIBLE** with cost-sensitive control. | CCTELM better matched artificial Gabor-search oculomotor statistics than less constrained models: Zhou & Yu. The fitted ~eight-fixation window is an effective model parameter, not a direct memory measure. |
| Active inference / epistemic value | Policy evaluation combines expected uncertainty reduction with extrinsic preferences. | **PARTIALLY COMPETING** with extrinsic-only and fixed heuristic accounts; **COMPATIBLE** with a Bayesian belief-state description; **RELATION UNKNOWN** to SC implementation. | Epistemic model outperformed its extrinsic-only comparator in a structured 2x2 task: Mirza et al.; formal simulations show feasibility under partial observability: Parr & Friston. Epistemic and heuristic actions can coincide; neither card identifies a neural implementation. |
| Discriminative or hybrid perceptual policy | Learned categorical mapping may govern categorical reports, with Bayesian inference better for other uncertainty/report regimes. | **PARTIALLY COMPETING** with the tested categorical Bayesian observer; hybrid is **COMPOSITIONAL**. | Discriminative/combined simulations capture major categorical anti-Bayesian trends: Chari et al. Alternative Bayesian parameterizations and incomplete fits remain viable. |
| Heuristic, history, and response-bias accounts | Fixed scan orders, sequential repetition, proximity bias, urgency/threshold shifts, or learned response policies drive some choices. | **PARTIALLY COMPETING** with action-by-action optimal control; can be **COMPOSITIONAL** with inference. | Scan heuristics were frequent in Mirza et al.; strategy repetition/proximity associations in Morvan & Maloney. These associations do not establish their causal role. |
| Volatility-sensitive belief updating | A change-point-like learner adjusts prediction after hidden changes in environmental statistics. | **PARTIALLY COMPETING** with the specified leaky integrator; **RELATION UNKNOWN** to within-scene search policy. | BBCP described pursuit and ratings better than stated comparators: Pasturel et al. Fitted modality differences may reflect separate mechanisms, measurement, or task demand. |
| Circuit-selection account | SC neuronal signals and pathways participate in selecting the saccade target. | **DIFFERENT LEVELS OF EXPLANATION** relative to computational families. | Correlation: Horwitz & Newsome. Intervention/causal contribution: McPeek & Keller. Neither maps computation onto cells/pathways. |
| Effort/resource account | Direction-specific oculomotor/cognitive effort is weighted during selection. | **COMPOSITIONAL** with reward/error/time objectives; **PARTIALLY COMPETING** with models that omit intrinsic cost. | Pupil-linked direction map predicts choice and dual task changes saccades: Koevoet et al. Pupil is non-specific; cost source and circuitry are unresolved. |

## Evidence and scope matrix

| Claim | Evidence type | System and regime | Main confounders / scope limit | Card references |
|---|---|---|---|---|
| Priors influence visual choices and fixation-time dynamics | **INTERVENTION EVIDENCE**: target-location odds manipulated | 11 humans; three gaze-contingent motion patches with explicit points | Learned response bias, explicit payoff, unmodeled motor cost; no peripheral vision | Ahmad et al. 2014 |
| Active selection improves category sampling relative to random revealing | **INTERVENTION EVIDENCE**: active versus computer-selected revealing | 3 humans; masked synthetic Gaussian-process patterns | Tiny sample; stationary synthetic images; reveal-count task | Yang et al. 2016 |
| Constrained Bayesian model fits search better than unconstrained model | Behavioral measurement plus model-component ablation; causal status for human constraints is **UNCLEAR** | 10 humans; static Gabor in 1/f² noise | Model misspecification, training differences, sparse visibility sampling, threshold matching | Zhou & Yu 2021 |
| Participants fail a tested sensitivity-optimal first-saccade policy | **INTERVENTION EVIDENCE**: separation/size varied; instructed optimal saccade verification | 6 humans total; one-saccade, three-destination task | Small samples; unmeasured planning costs; specific policy and artificial destination set | Morvan & Maloney 2012 |
| External and motor-linked uncertainty affect prior use differently | **INTERVENTION EVIDENCE**: blur, priors, saccade/no-saccade, report format | Humans (n=9/11) and two macaques; displacement judgment | Blur is one external uncertainty; no-saccade baseline differs; limited task | Chari et al. 2023 |
| Volatile direction statistics alter prediction | **INTERVENTION EVIDENCE**: hidden probability switches | 12 humans; head-restrained step-ramp pursuit and ratings | Binary fixed-hazard environment; model fit does not establish common latent belief | Pasturel et al. 2020 |
| SC is necessary/contributory for selection in one search task | **CAUSAL INTERVENTION EVIDENCE**: focal reversible inactivation | Monkey visual search; detailed methods unavailable in card | `ABSTRACT_ONLY`; population/pathway/computation unspecified | McPeek & Keller 2004 |
| SC prelude activity is associated with selected target/evidence | **CORRELATIONAL** neural evidence | 3 trained macaques; motion discrimination | Selected-cell sampling and sequential recordings; no causal test | Horwitz & Newsome 2001 |
| Direction-dependent effort relates to choice | Controlled association plus **INTERVENTION EVIDENCE** for cognitive-demand effect | 20 humans, plus natural-scene reanalyses | Pupil specificity, residual scene covariates, dual-task priority | Koevoet et al. 2025 |
| Natural/embodied behavior changes the relevant state/action space | Review-level synthesis; no new direct causal evidence | Mobile and VR/natural-task literature | Review card; cited primary results require source-specific assessment | Goettker et al. 2025 |

## Tensions, anomalies, and limiting evidence

- **POTENTIAL TENSION — NEEDS VERIFICATION:** Najemnik & Geisler report near-optimal aggregate human search performance, while Morvan & Maloney show failure to adapt first-saccade strategy to an individually derived optimum and Zhou & Yu find constrained models closer to human scan paths. These claims use different stimuli, choice horizons, objectives, and optimality metrics. They do not directly contradict one another. The Najemnik & Geisler card is `PARTIAL`; detailed comparison requires its full original article.
- **DISPUTED:** Greater sensory uncertainty need not yield greater prior influence across all active-vision reports. Chari et al. find the opposite in categorical external-blur judgments, yet Bayesian-consistent prior weighting in continuous reports and in categorical saccade-related uncertainty. This is evidence for a task/uncertainty-source/report-format dissociation in that paradigm; it does not establish a general external-versus-motor neural classification.
- **POTENTIAL TENSION — NEEDS VERIFICATION:** Mirza et al.’s epistemic active-inference advantage and Yang et al.’s information-gain BAS fit are compatible at a broad computational level, while both report residual heuristic structure. The evidence cannot determine whether shared behavior reflects one common algorithm, different objective parameterizations, or task-specific fit flexibility.
- **UNKNOWN:** Whether the apparent implicit/explicit volatility-rate difference in Pasturel et al. indicates separate learners. Identical stimulus sequences were used, but measurement modality, session demands, and response scale differed.
- **LIMITING EVIDENCE:** The card labelled `glaser_etal_2020` concerns generic neural decoding and cannot support the index’s stated FEF result. The intended FEF source must be checked before making a FEF mechanistic claim.
- **ANOMALY / SCOPE LIMIT:** Laboratory tasks often suppress peripheral vision, head movement, scene dynamics, or ordinary action consequences. Goettker et al. identify these as material variables; their review does not demonstrate that any particular laboratory effect fails to generalize.

## Composite explanations under challenge

### Constraint-weighted belief-state control

**Hypothesis (INFERENCE):** Active visual behavior may combine belief updating from prior and sensory evidence with a policy that trades expected information/task value against time, switching/effort, motor uncertainty, and finite memory.

**What supports coherence:** Cost-sensitive control accounts for explicit-incentive behavior (Ahmad et al.); motor/memory constraints improve model fit in controlled search (Zhou & Yu); direction-linked effort covaries with selection (Koevoet et al.); belief-sensitive sampling appears in category tasks (Yang et al.; Mirza et al.).

**What remains unproven:** No card tests all components jointly or identifies their relative weights in the same behavior. The components can be absorbed by alternative heuristics or response biases. Intrinsic effort is not isolated from task design, and none of the cards causally maps this composite policy to a circuit.

**Scope:** The evidence comes from separate, mostly small, head-restrained or gaze-contingent laboratory regimes. It does not justify extrapolation to natural eye-head-body behavior.

### Source- and format-dependent uncertainty processing

**Hypothesis (INFERENCE):** External image uncertainty, saccade-linked uncertainty, and report format recruit partially distinct algorithmic routes, with categorical judgments admitting a discriminative component and continuous reports admitting the tested Bayesian description.

**What supports coherence:** Chari et al. manipulated these factors and found qualitatively divergent prior-use patterns; their combined Bayesian/discriminative model captured more of the data than either simple account.

**What remains unproven:** A different Bayesian likelihood/prior parameterization may reproduce the categorical result. The evidence does not localize a source classifier, establish a distinct neural route, or generalize beyond displacement judgments and one blur manipulation.

### Sequential embodied active perception

**Hypothesis (INFERENCE):** Extended natural gaze behavior is a sequence of coupled inference-and-action decisions in which gaze, head/body movement, memory, task goals, and motor noise jointly alter later observations.

**What supports coherence:** It organizes the variables identified by Goettker et al. and is consistent with formal POMDP/active-inference descriptions.

**What remains unproven:** The review provides no common fitted model or causal dataset. Its evidence does not show that one sequential-decision mechanism explains natural behavior, nor that controlled-task parameters transfer.

## Structured uncertainty nodes

### U01 — Objective of next-fixation selection

- **Phenomenon:** Choice of where/when to look during foveated search under uncertainty.
- **Established knowledge:** Priors affect selection dynamics; unconstrained information-only policies miss some controlled behavior; costs and motor/memory constraints can improve descriptive fit.
- **Exact unknown:** Whether observed deviations from information gain primarily reflect a different objective (time/switch/effort/error), bounded implementation of the same objective, or non-value-based heuristics.
- **Relevant explanations:** Information-gain Bayesian; cost-sensitive Bayesian; bounded Bayesian; heuristic/history bias.
- **Relationship among explanations:** Cost-sensitive and bounded accounts are **COMPOSITIONAL** with Bayesian inference; each is **PARTIALLY COMPETING** with a pure information-gain account; heuristic relationship is **PARTIALLY COMPETING** and may also be compositional.
- **Supporting evidence:** Ahmad et al.; Zhou & Yu; Morvan & Maloney; Yang et al.; Koevoet et al.
- **Limiting evidence:** Explicit point penalties confound intrinsic and imposed costs; fitted constraints and model comparisons do not identify causal computation; small/artificial tasks differ in horizon and sensory access.
- **Causal strength:** Behavioral interventions establish context sensitivity and task-specific policy failure. They do not causally distinguish internal objective, approximation, or heuristic.
- **Scope and confounders:** Discrete three-location, one-saccade, masked, or Gabor/noise tasks; reward, training, response thresholds, motor bias, and model parameterization.
- **Why current evidence is insufficient:** Different candidate accounts have not been discriminated in a genuinely comparable regime with independently identified costs/constraints.
- **Observation type that would reduce uncertainty:** Behavioral data in which candidate objectives, bounded policies, and history heuristics make distinct predictions while sensory information, externally imposed costs, motor variability, and performance are measured separately.
- **Relevant paper-card references:** Ahmad et al. 2014; Morvan & Maloney 2012; Yang et al. 2016; Zhou & Yu 2021; Koevoet et al. 2025.

### U02 — Meaning of uncertainty for active perception

- **Phenomenon:** Prior weighting and perceptual report across saccades as external image uncertainty or saccade-linked uncertainty changes.
- **Established knowledge:** In Chari et al., categorical prior use decreased with added blur but increased with saccade-related uncertainty; continuous reports were qualitatively consistent with a biased Bayesian model.
- **Exact unknown:** Whether the dissociation is caused by uncertainty source, report format/category learning, a discriminative route, or an inadequately specified Bayesian observer.
- **Relevant explanations:** Bayesian source-specific likelihoods; discriminative categorization; Bayesian/discriminative hybrid; report/decision-rule change.
- **Relationship among explanations:** Bayesian and discriminative accounts are **PARTIALLY COMPETING**; hybrid is **COMPOSITIONAL**; report-rule account is **COMPATIBLE** with either.
- **Supporting evidence:** Blur, prior, saccade/no-saccade, and report-format manipulations with human and macaque results; discriminative/combined simulations (Chari et al.).
- **Limiting evidence:** Two macaques; one external-noise manipulation; no-saccade conditions differ from saccade conditions; alternative likelihood/prior parameterizations remain untested.
- **Causal strength:** Intervention evidence establishes the behavioral dissociation in this paradigm. Causal mechanism is unknown.
- **Scope and confounders:** One-dimensional target displacement, trained priors, categorical versus continuous response mappings, saccadic suppression operationalization, learning stage.
- **Why current evidence is insufficient:** The observed behavioral pattern is compatible with several computational decompositions and has no neural localization.
- **Observation type that would reduce uncertainty:** Joint measurements that distinguish source-specific sensory likelihood changes from report-rule and category-learning changes, with model comparison spanning the stated alternative parameterizations.
- **Relevant paper-card references:** Chari et al. 2023.

### U03 — Volatility representation and transfer to visual action

- **Phenomenon:** Anticipatory visual action and explicit prediction after hidden changes in environmental statistics.
- **Established knowledge:** Pursuit and ratings adapt to hidden direction-probability switches; a specified change-point model outperformed a leaky-integrator comparator in the reported task.
- **Exact unknown:** Whether implicit pursuit and explicit reports share a volatility representation, and whether volatility updating controls visual search/perception beyond binary motion prediction.
- **Relevant explanations:** Common change-point belief; separate implicit/explicit learners; response/measurement-specific readout of one belief; simpler adaptive learner.
- **Relationship among explanations:** Common versus separate learners are **PARTIALLY COMPETING**; readout account is **COMPATIBLE** with a common belief; relation to search control is **RELATION UNKNOWN**.
- **Supporting evidence:** Same hidden sequence affects both modalities; differing fitted hazards (Pasturel et al.).
- **Limiting evidence:** Modality was tested in separate sessions; fixed binary hazard model; fitted hazard is correlational and may reflect response scaling/noise.
- **Causal strength:** Intervention evidence for behavioral adaptation; no causal evidence from fitted belief to eye movement.
- **Scope and confounders:** Head-restrained, binary horizontal step-ramp motion; 12 participants; session order and task demands.
- **Why current evidence is insufficient:** Equivalent behavioral fits do not establish a shared internal state or a mechanism linking volatility inference to search.
- **Observation type that would reduce uncertainty:** Matched implicit and explicit readouts under common task timing, with observations able to separate shared-state predictions from independent adaptive processes.
- **Relevant paper-card references:** Pasturel et al. 2020; Parr & Friston 2017 (formal but simulation-only context).

### U04 — Neural implementation of evidence-, prior-, and cost-sensitive selection

- **Phenomenon:** Circuit generation of target selection during visually guided saccades.
- **Established knowledge:** SC prelude activity correlates with selected target and motion coherence in a trained task; reversible SC inactivation increases distractor selection when target representation lies in the affected field.
- **Exact unknown:** Which circuits/cell populations represent evidence, priors, uncertainty, effort, or policy values, and how they causally produce the selected saccade.
- **Relevant explanations:** SC as selection-contributing node; cortical-to-SC input account; distributed circuit implementation; computational-family-specific implementation.
- **Relationship among explanations:** SC and distributed/cortical input accounts are **COMPATIBLE**; alternatives for locus of computation are **PARTIALLY COMPETING**; computational objective and circuit account are **DIFFERENT LEVELS OF EXPLANATION**.
- **Supporting evidence:** Horwitz & Newsome correlational recordings; McPeek & Keller focal reversible inactivation.
- **Limiting evidence:** McPeek & Keller is `ABSTRACT_ONLY`; causal effect lacks inspected cellular/pathway detail. Horwitz & Newsome selected a nonrepresentative cell subset and did not manipulate activity. No usable FEF prior-selection evidence is available because the Glaser card/index mismatch is unresolved.
- **Causal strength:** Task-specific causal contribution of SC from inactivation; correlational evidence for firing/evidence relation; causal computational role unknown.
- **Scope and confounders:** Trained macaque tasks, particular visual-search/direction-discrimination designs, potential input versus local computation, motor and perceptual consequences of perturbation.
- **Why current evidence is insufficient:** Necessity/contribution at an anatomical site does not identify information content, algorithm, or source of the relevant signal.
- **Observation type that would reduce uncertainty:** Circuit-resolved observations linking trial-level prior/evidence/cost variables, population dynamics, and selection effects under interventions whose sensory and motor consequences are separately characterized.
- **Relevant paper-card references:** Horwitz & Newsome 2001; McPeek & Keller 2004; Koevoet et al. 2025. **NEEDS_VERIFICATION:** intended FEF source indexed as Glaser et al. 2020.

### U05 — Memory and integration across successive fixations

- **Phenomenon:** Retention and use of earlier visual evidence during search and categorization.
- **Established knowledge:** Sequential category sampling depends on accumulated evidence in its task; a constrained search model has a best-fit effective memory window near eight fixations; near-optimal aggregate search has been reported under a restricted ideal benchmark.
- **Exact unknown:** What is retained across saccades, for how long, in what format, and whether apparent limits arise from memory, policy, scene statistics, or motor/sensory constraints.
- **Relevant explanations:** Finite all-or-none fixation memory; graded/partial scene representation; minimal integration with high within-fixation efficiency; heuristic revisit/selection strategies.
- **Relationship among explanations:** Finite and graded memory are **PARTIALLY COMPETING**; within-fixation efficiency is **COMPATIBLE** with several memory forms; strategy explanations are **PARTIALLY COMPETING** with a literal capacity interpretation.
- **Supporting evidence:** Zhou & Yu model fits/ablations; Yang et al. accumulated-evidence behavior; Najemnik & Geisler conditional benchmark.
- **Limiting evidence:** Eight-fixation estimate is model-dependent; Najemnik & Geisler card is `PARTIAL`; tasks use synthetic/masked or static-noise displays and do not directly measure retained content.
- **Causal strength:** Behavioral intervention supports value of sequential sampling in a synthetic task. Memory-capacity claim is model-based and causal strength is unclear.
- **Scope and confounders:** Static scenes, fixed reveal apertures, target/noise stimuli, visibility-map assumptions, resampling/revisit policies, training.
- **Why current evidence is insufficient:** Observable scan paths can arise from multiple internal retention schemes, and existing measures do not identify content or mechanism of memory.
- **Observation type that would reduce uncertainty:** Measurements that independently identify retained information from prior fixations and distinguish discrete capacity, graded decay, and policy-driven revisiting predictions.
- **Relevant paper-card references:** Najemnik & Geisler 2005; Yang et al. 2016; Zhou & Yu 2021.

### U06 — Generalization to embodied, natural visual behavior

- **Phenomenon:** Active perception when gaze is coupled to head/body movement, dynamic scenes, and extended task goals.
- **Established knowledge:** Natural behavior changes sensory input and action possibilities; mobile multimodal measurement and scene reconstruction now make more of these variables observable. Laboratory mechanisms reviewed here were largely obtained under head restraint or gaze-contingent simplification.
- **Exact unknown:** Which controlled active-vision mechanisms and parameter values transfer to ordinary eye-head-body behavior, and which apparent lab effects depend on removed contextual variables.
- **Relevant explanations:** Transferable sequential belief-state control; task-specific laboratory strategies; embodied coordination as an additional control level.
- **Relationship among explanations:** Embodied coordination is **COMPOSITIONAL** with belief-state control; transferable versus task-specific claims are **PARTIALLY COMPETING**.
- **Supporting evidence:** Goettker et al. review of head movement and natural-behavior measurement; Koevoet et al. covariate-adjusted natural-scene analyses.
- **Limiting evidence:** Review-level evidence and secondary datasets do not validate transfer; natural settings co-vary goals, visual structure, motor demands, and social/task context.
- **Causal strength:** No general causal evidence for transfer.
- **Scope and confounders:** Tracking/scene-reconstruction errors, uncontrolled covariates, differences in head restraint, task instruction, and behaviorally relevant consequences.
- **Why current evidence is insufficient:** Existing natural and laboratory evidence lacks a common mechanistic measurement basis and direct comparison of matched variables.
- **Observation type that would reduce uncertainty:** Matched descriptions of sensory input, eye-head-body action, task state, and performance that allow quantitative comparison of the same mechanistic variables across controlled and embodied regimes.
- **Relevant paper-card references:** Goettker et al. 2025; Koevoet et al. 2025; Zhou & Yu 2021; Yang et al. 2016.
