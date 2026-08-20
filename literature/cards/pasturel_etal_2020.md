# Humans adapt their anticipatory eye movements to the volatility of visual motion properties

## Metadata

**Authors:** Chloé Pasturel; Anna Montagnini; Laurent Udo Perrinet

**Year:** 2020

**arXiv:** None identified

**Published venue:** PLOS Computational Biology 16(4):e1007438

**DOI:** 10.1371/journal.pcbi.1007438

**Publication status:** PUBLISHED

**READING_STATUS:** FULL_TEXT

**Source URL:** https://doi.org/10.1371/journal.pcbi.1007438

**Evidence role:** CORE

## Scientific question

Can people adapt trial-by-trial predictions of visual-motion direction when the latent direction bias changes at unannounced, stochastic times, and does a Bayesian binary change-point (BBCP) model describe anticipatory pursuit and explicit prediction better than a leaky integrator?

## Exact system and regime

Twelve adults (7 female; mean age 29) completed two sessions on separate days with the same pseudo-random sequence of left/right moving ring targets. Each 15°/s, 1-s step-ramp followed a 300-ms gap; the probability of rightward motion was constant within randomly sized epochs and changed at hidden switches (generative hazard 1/40). One session measured 1-kHz anticipatory smooth-pursuit velocity; the other collected a pre-trial continuous left/unsure/right rating. Head movement was restrained. (Methods, pp. 21–22; Fig. 1.)

## Main claims

### Volatile direction statistics track both response modalities

**OBSERVATION:** Across the 12 participants, anticipatory-pursuit polarity and explicit ratings varied with the hidden direction-bias sequence; behavioral traces showed delayed changes after hidden switches. BBCP prediction was more strongly associated with pursuit (participant median r²=0.459±0.104; MI=0.707±0.134) than the true probability or leaky estimate, and with ratings (r²=0.670±0.145; MI=1.312±0.364) than either comparator. Wilcoxon comparisons are reported. 

**AUTHOR INTERPRETATION:** Humans flexibly adapt to volatility and use an internal belief about environmental contingencies for sensorimotor control and explicit judgments.

**INFERENCE:** The results support a volatility-sensitive computational description of behavior; they do not directly establish the neural implementation or a shared latent representation across the two modalities.

**Intervention or measurement:** Experimenter-generated binary direction sequence with hidden probability switches; eye velocity or explicit next-direction rating; BBCP, leaky-integrator, and true-probability regressors.

**Observed result:** BBCP outperformed the specified comparators for both measures; results remained qualitatively/conclusively similar when the model’s assumed switch at each 50-trial pause was removed.

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Same stimulus sequence in the two sessions; fixed target kinematics; exclusion of saccades/blinks from velocity traces; comparison with true latent probability and leaky integrator; pause-assumption sensitivity analysis.

**Alternative explanations not excluded:** Correlation with a model does not rule out other adaptive algorithms; session order/modality differences and a small sample could contribute to fitted differences.

**Scope limitations:** Binary horizontal motion, screen-based head-restrained pursuit, n=12, and one specified volatility regime.

**Source pointer:** Results, “Anticipatory pursuit and explicit ratings,” pp. 12–15, Figs. 3–4; Methods, pp. 21–22.

### Fitted volatility differs between implicit and explicit sessions

**OBSERVATION:** Individually fitted BBCP hazard rates had medians 1/14 for anticipatory pursuit and 1/36 for ratings; distributions differed and the two estimates lacked an apparent correlation.

**AUTHOR INTERPRETATION:** Different implicit and explicit mechanisms, or stronger individual modulation in explicit processing, may guide exploitation–exploration tendencies.

**INFERENCE:** The data show modality-dependent fitted parameters; they do not demonstrate distinct learning mechanisms.

**Intervention or measurement:** Per-participant model fits to pursuit velocity and rating sequences.

**Observed result:** Higher and less dispersed fitted hazard estimates for the pursuit session than ratings; ground-truth hazard was 1/40.

**Causal strength:** CORRELATIONAL

**Controls:** Identical target-direction sequence across sessions; fits were also examined by trial block.

**Alternative explanations not excluded:** Measurement scaling/noise, task instructions, and session-specific response demands.

**Scope limitations:** Twelve participants; no direct test of common versus separate learning processes.

**Source pointer:** Results, “Analyzing inter-individual differences,” pp. 15–17, Fig. 5; Discussion, p. 18.

## Important controls

- Fixed target speed, duration, gap, display and head restraint; fixation-control procedure (Methods, pp. 21–22).
- Eye and rating sessions used exactly the same sequence, although participants did not notice this (Methods, p. 21).
- BBCP was benchmarked against a leaky integrator and the hidden true probability; a pause/switch modeling choice was checked for sensitivity (pp. 14–15).

## Critical assumptions

- The experiment’s binary-switching generative model and hazard-rate parameter adequately capture the relevant environmental volatility.
- Anticipatory velocity and ratings can be modeled as readouts of inferred direction probability.
- Pupil/oculomotor artifacts removed by the stated processing do not drive the reported associations.

## Limitations

Authors state that their agent is limited by its assumed generative model and fixed hazard parameter (Discussion, p. 18). They did not test visual-motion perception during the volatile sequence, and state that more evidence is needed to determine whether the apparent implicit/explicit hazard-rate dissociation reflects setup or separate volatility processing (pp. 17–19).

## What this paper supports

In this controlled binary visual-motion task, anticipatory pursuit and explicit expectation reports adapt across hidden changes in direction statistics, and a change-point model describes both better than the paper’s leaky-integrator comparator.

## What this paper does not establish

It does not establish Bayesian neural computation, a common representation across implicit and explicit responses, general adaptation to arbitrary real-world volatility, or causation from fitted belief to eye movement.

## Explicit open questions

- How volatility affects visual perception and other cognitive functions (Discussion, pp. 17–20).
- Whether implicit and explicit estimates reflect experimental setup or separate processing (p. 17).
- Origins and trait relations of individual variability (p. 20).

## Evidence concerns

**Replication:** No independent replication in this paper; it reports consistency with earlier anticipatory-pursuit findings.

**Measurement limitations:** Anticipatory pursuit is an indirect behavioral readout; ratings and pursuit were obtained in separate sessions.

**Potential confounding:** The model treated every 50-trial pause as a switch in its primary analysis, although the authors report a sensitivity analysis without this assumption.

**Statistical / experimental concerns:** Small n=12; key superiority results are model comparisons rather than out-of-sample neural or causal tests.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://doi.org/10.1371/journal.pcbi.1007438, p. 1 |
| Full paper | https://journals.plos.org/ploscompbiol/article/file?id=10.1371%2Fjournal.pcbi.1007438&type=printable |
| Main result | Full paper, Results pp. 12–15, Figs. 3–4 |
| Important control | Full paper, Results pp. 14–15; Methods pp. 21–22 |
| Limitations | Full paper, Discussion pp. 17–20 |
