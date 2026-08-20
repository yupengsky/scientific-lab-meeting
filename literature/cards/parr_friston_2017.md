# Working memory, attention, and salience in active inference

## Metadata

**Authors:** Thomas Parr; Karl J. Friston

**Year:** 2017

**arXiv:** None found in inspected paper

**Published venue:** Scientific Reports 7:14678

**DOI:** 10.1038/s41598-017-15249-0

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://doi.org/10.1038/s41598-017-15249-0

**Evidence role:** HIGH-LEVERAGE SUPPORTING

## Scientific question

Can a hierarchical active-inference MDP give formal definitions of working memory, attention, and salience, and reproduce selected behavioural and electrophysiological patterns in simulation?

## Exact system and regime

This is a theoretical/simulation study, not a new human or animal experiment. Agents use a two-level discrete-state hierarchical MDP in a visual delayed-recognition task: two scenes are presented, a 90% valid or uninformative retrocue follows, then a probe requires same/different/withhold response. The lower level represents scene and eye position across four quadrants; the higher level represents scene pair, order, probe, trial phase, and report. Simulations also alter policy precision (γ, interpreted as dopaminergic modulation), transition precision/volatility, and likelihood precision. [Active inference and simulation sections; Figs. 4, 6–8, 12–13]

## Main claims

### Working memory and salience have separable active-inference roles

**OBSERVATION:** In the model, beliefs about previously presented scenes persist at the higher temporal level through the delay, while lower-level beliefs change quickly with samples. Policy evaluation contains pragmatic and epistemic expected-free-energy terms; saccade locations with greatest expected uncertainty reduction are selected as salient. [pp. 7–9; Figs. 5, 8]

**AUTHOR INTERPRETATION:** Working memory is temporally hierarchical evidence accumulation used to evaluate future policies. Salience is an attribute of actions/sampling policies that offer epistemic affordance, whereas attention in the sensory-gain sense is precision attributed to sensory evidence.

**INFERENCE:** These are formal definitions within the adopted generative-model framework, not direct evidence that biological systems use exactly these variables or message-passing operations.

**Intervention or measurement:** In silico hierarchical MDP; posterior state beliefs and selected saccades; decomposition of expected free energy.

**Observed result:** Persisting higher-level posterior representation followed scene presentation; the agent selected informative locations and classified scenes with two fixations in the illustrated trial. [Fig. 8 and accompanying text]

**Causal strength:** CAUSAL EVIDENCE

**Controls:** Model architecture separates eye position from scene state, fast lower from slow higher temporal level, and expected free energy into epistemic/pragmatic terms; the claim is conditional on these programmed elements.

**Alternative explanations not excluded:** Other computational architectures can produce delayed activity, evidence accumulation, or information-seeking actions; anatomy discussed in the paper does not identify the proposed implementation.

**Scope limitations:** Demonstration uses discrete, hand-specified visual scenes and a constructed generative model; it does not fit or perturb biological neural data.

**Source pointer:** https://doi.org/10.1038/s41598-017-15249-0, “Working memory and attention in active inference,” pp. 6–7; Figs. 5–8; Discussion.

### The model reproduces selected empirical signatures in simulation

**OBSERVATION:** Increasing the number of possible scenes from 3 to 5 produced a linear increase in simulated computational response time. Altering retrocue validity produced simulated higher-level ERP differences with an early effect and later reversal; valid versus uninformative retrocues also altered a simulated probe ERP in the time range compared with a published load-sensitive N3RS effect. [Results, pp. 8–10; Figs. 9–11]

**AUTHOR INTERPRETATION:** The hierarchical active-inference formulation can reproduce behavioural and electrophysiological phenomena associated with working memory and context updating.

**INFERENCE:** The qualitative match provides a model demonstration and hypothesis-generating link. It does not validate the model against newly collected or quantitatively fitted neural data.

**Intervention or measurement:** Simulated task-set size and retrocue validity; response time defined as computer time from probe to response; simulated ERPs defined from the rate of change of model-unit activity.

**Observed result:** Linear simulated response-time pattern; context-dependent waveform difference/reversal; probe waveform difference beginning around 300 ms. [Figs. 9–11]

**Causal strength:** CAUSAL EVIDENCE

**Controls:** Same task structure across set-size simulations except total possible scenes; 90%-valid versus 50%-valid (uninformative) retrocues; simulations compare outputs with explicitly cited external empirical patterns.

**Alternative explanations not excluded:** Qualitative waveform resemblance can arise from other models; simulation time and model-unit derivatives are not behavioural reaction times or measured scalp ERPs.

**Scope limitations:** No new empirical participant data; timing was explicitly “not exactly the same” as the compared frontal ERP. [Fig. 10 caption]

**Source pointer:** https://doi.org/10.1038/s41598-017-15249-0, “Reaction times” and “Evoked responses,” pp. 8–10; Figs. 9–11.

### Policy and sensory precision alter simulated visual sampling and memory updating

**OBSERVATION:** Reducing policy precision γ made simulated policy selection increasingly stochastic, increased saccades, and led to uninformative or suboptimal fixations. In a separate precision simulation, a more precise likelihood mapping caused new sensory data to update maintained beliefs more strongly; lower likelihood precision and low volatility favoured maintenance. [Results, pp. 10–12; Figs. 12–13]

**AUTHOR INTERPRETATION:** γ may correspond to dopaminergic precision over policies; sensory precision is an active-inference account of attention as gain, with implications for working-memory updating versus distractor resistance.

**INFERENCE:** The simulations predict that changing these precision-like biological variables could alter saccades and memory updating; the paper itself does not establish a dopamine-to-γ mapping or test patients.

**Intervention or measurement:** Programmed reduction of γ; programmed A-matrix likelihood precision and B-matrix transition precision; simulated saccades and posterior expectations.

**Observed result:** Lower γ yielded stochastic/suboptimal sampling; precise likelihoods sped evidence accumulation and amplified updating of maintained representations. [Figs. 12–13]

**Causal strength:** CAUSAL EVIDENCE

**Controls:** Same trial shown at different γ values; likelihood and transition precisions varied in a 2×2 arrangement. [Figs. 12–13]

**Alternative explanations not excluded:** γ is a model parameter and simulated lesion, not pharmacological or neural evidence; effects depend on supplied matrices, state space, and priors.

**Scope limitations:** The authors propose Parkinsonian testing as future empirical validation rather than presenting it. [“Dopamine,” p. 11]

**Source pointer:** https://doi.org/10.1038/s41598-017-15249-0, “Dopamine,” pp. 10–11; “Attention and precision,” pp. 11–12; Figs. 12–13.

## Important controls

- Retrocue comparison uses 90% validity versus 50% validity, the latter uninformative between two alternatives. [Fig. 10]
- Set-size simulations retain two encoded scenes and alter only the total scene set. [Fig. 9]
- Likelihood precision and transition precision are independently varied in Fig. 13.
- Dopamine/policy-precision simulations use the same trial across levels of γ. [Fig. 12]

## Critical assumptions

- The hierarchical discrete MDP adequately represents the task and temporal structure.
- Posterior beliefs, their rate of change, and computer simulation time are meaningful model analogues of neural activity, ERP, and reaction time respectively.
- Expected free energy and its decomposition specify policy selection; γ is a useful candidate proxy for precision over policies.

## Limitations

- All central demonstrations are simulations; the paper reports no new behavioural, neural, pharmacological, or patient data.
- The authors describe simulated and published ERP timing as imperfectly matched. [Fig. 10 caption]
- The MDP uses discrete state spaces; the authors state this only crudely approximates continuous variables in the attention discussion. [“Attention and precision,” p. 11]

## What this paper supports

It supplies a formal active-inference account in which memory-like maintenance, sensory precision, and epistemic action selection are distinct model operations. It demonstrates that this model can generate several qualitative patterns resembling prior working-memory observations.

## What this paper does not establish

It does not demonstrate that neural working memory is active-inference belief propagation, that dopamine encodes policy precision, that basal ganglia implement model averaging, or that simulated effects hold in human or animal visual search.

## Explicit open questions

- Test Parkinsonian participants on and off dopaminergic medication in the task to assess the proposed dopamine/policy-precision account. [“Dopamine,” p. 11]
- Examine the proposed basal-ganglia role in robustness of working-memory representations in future work. [“Working memory” discussion before “Attention and precision,” p. 11]

## Evidence concerns

**Replication:** No new replication study; comparisons are against previously published empirical results.

**Measurement limitations:** “ERPs” and reaction times are model-derived quantities, not recordings or human responses collected here.

**Potential confounding:** Apparent matches can depend on hand-specified generative-model structure and parameter choices; the model itself encodes task contingencies and preferences.

**Statistical / experimental concerns:** The paper reports illustrative simulations and qualitative cross-study comparisons rather than parameter fitting, out-of-sample prediction, or formal model comparison against alternatives.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://doi.org/10.1038/s41598-017-15249-0, Abstract |
| Full paper | https://doi.org/10.1038/s41598-017-15249-0 |
| Main result | “Working memory and attention in active inference,” pp. 6–7; Figs. 8–13 |
| Important control | Figs. 9, 10, 12, 13 and associated Results text |
| Limitations | Fig. 10 caption; “Attention and precision,” p. 11; “Dopamine,” p. 11 |
