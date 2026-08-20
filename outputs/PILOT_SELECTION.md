# Pilot Portfolio Decision

## Comparative matrix

| Candidate | Importance preserved | Discrimination | Expected uncertainty reduction | Negative-result value | Interpretability | Tractability | Cost/risk |
|---|---|---|---|---|---|---|---|
| C001 | High within scoped causal ICL; broad mechanism remains out of scope | Medium; redundancy and path non-specificity remain serious | Medium | Medium; constrains induction-head necessity only in the tested regime | Medium-low | Medium | High technical risk from selective suppression and rescue |
| C002 | High; directly tests what context contributes to ICL behavior | High relative to the alternatives; mapping, retrieval, priors, and format have divergent behavioral predictions | High for U3 | High; a clean null weakens independent mapping acquisition in the tested regime | Medium-high after controls | High | Lowest technical risk among the candidates |
| C003 | Medium-high; causal representation question is preserved, with localization claims excluded | Medium; transfer can show functional sufficiency without identifying native computation | Medium | Medium-low; nulls are difficult to interpret under representation non-uniqueness | Medium-low | Medium | High intervention and representation risk |
| C004 | High within synthetic training dynamics | Medium-high in principle, low until reciprocal interventions are validated | Medium-high if the reciprocal test succeeds | Medium; a clean null can weaken competition, but failed probes are ambiguous | Low-medium | Low-medium | Highest design and compute burden |
| C005 | Medium; failure-mechanism question remains heterogeneous | Medium-low; selective rescue may still reflect task-specific mechanisms | Medium | Low-medium; nulls often leave heterogeneity and intervention failure unresolved | Low | Medium-low | High confounding and task-heterogeneity risk |

## Pairwise dominance

C002 DOMINATES C003 under the scarcity constraint: it has comparable or better tractability and lower technical risk, while its matched behavioral contrasts provide clearer divergent predictions and higher negative-result value. C003’s transfer result could still be compatible with multiple distributed representations.

C002 DOMINATES C005: it targets a cleaner uncertainty with fewer task-heterogeneity branches, stronger control logic, and a more informative null at similar or lower cost.

C002 DOMINATES C001 for the single-pilot allocation: its behavioral decomposition is more interpretable before undertaking high-risk causal path suppression. C001 has greater mechanistic ambition, while its intervention ambiguity reduces expected information per unit effort.

C002 does not clearly dominate C004. C004 addresses a highly consequential training-dynamics uncertainty and could have greater information value if the reciprocal intervention works. Its cost and ambiguity are substantially higher, so the comparison is not a strong same-cost dominance relation.

C004 does not dominate C002 because its central evaluator and route-separation requirements are still unvalidated. C003, C005, and C001 do not dominate C002 because their causal or mechanistic measurements have larger interpretation risks under one-pilot scarcity.

## Selected pilot

C002

## Why this pilot beats the strongest alternative

C004 is the strongest alternative because it addresses a high-leverage uncertainty about why ICL emerges and disappears. C002 is preferable under a one-pilot budget because its key outcomes are behavioral, its competing explanations have clearer divergent predictions, and a clean null directly weakens independent mapping-acquisition claims. C004 requires successful evaluator validation and reciprocal route interventions before its result becomes interpretable; C002 can establish a useful scientific boundary with a smaller, more reliable pilot.

## Exact scientific question tested

Does demonstrated input-output mapping contribute independently to in-context performance after calibration, prompt format, verbalizer, and retrieval/similarity effects are matched?

## Exact pilot

Run a preregistered answer-level mapping contrast across held-out queries and multiple seeds. Compare arbitrary-label demonstrations with relation-informative and relation-uninformative contexts while matching example similarity, prompt format, label priors, verbalizers, and calibration. Use query-only and retrieval-matched controls.

## Predictions that diverge

H1 — independent mapping acquisition:

Mapping-sensitive contexts produce a reproducible answer-level effect that survives calibration, format, verbalizer, and retrieval controls.

H2 — priors, formatting, or verbalization:

The apparent mapping effect disappears after calibration or format/verbalizer controls, or remains tied to output-space statistics rather than demonstrated relations.

H3 — retrieval/similarity explanation:

The effect disappears after similarity-matched retrieval controls and tracks the availability of near-neighbor evidence rather than the demonstrated mapping.

## Stop criterion

Stop if the mapping contrast is unstable across seeds or held-out queries, disappears under calibration or retrieval matching, or the controls are not independent. Do not add mechanistic probes after a non-diagnostic behavioral result.

## Go criterion

Proceed only if the mapping contrast is reproducible, exceeds calibrated prior and format controls, survives retrieval matching, and has a prespecified effect size and replication criterion.

## What a positive result permits us to claim

Demonstrated mapping information contributes independently to ICL behavior in the tested task and model regime.

## What a negative result permits us to claim

Independent mapping acquisition has no detectable behavioral contribution under the tested controls and regime, weakening claims that benchmark ICL generally reflects mapping learning.

## What neither result permits us to claim

Neither result identifies a unique internal mechanism, proves that all ICL is or is not mapping acquisition, or separates Bayesian inference from optimization internally.

## Why the other four pilots should wait

- C001: selective induction-path suppression has higher intervention ambiguity and should follow a clearer behavioral decomposition.
- C003: task-vector transfer can demonstrate functional sufficiency without resolving native localization or representation uniqueness.
- C004: reciprocal ICL/IWL intervention requires a larger, higher-risk setup whose evaluators and route selectivity are not yet validated.
- C005: failure mechanisms are heterogeneous, making a single-pilot null difficult to interpret and a positive rescue hard to generalize.
