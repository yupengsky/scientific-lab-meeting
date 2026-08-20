# Localization for Robotic Assemblies with Position Uncertainty

## Metadata

**Authors:** Siddharth R. Chhatpar; Michael S. Branicky

**Year:** 2003

**arXiv:** None found.

**Published venue:** Proceedings of the 2003 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), vol. 3, pp. 2534–2540, Las Vegas, Nevada.

**DOI:** 10.1109/IROS.2003.1249251

**Publication status:** PUBLISHED

**READING_STATUS:** PARTIAL

**Source URL:** https://citeseerx.ist.psu.edu/document?doi=3dd9b81f0c854367b2d861b4604e249e3d7545b2&repid=rep1&type=pdf

**Evidence role:** HIGH-LEVERAGE SUPPORTING

## Scientific question

Can contact observations made while probing a mating part localize peg–hole misalignment when pose uncertainty exceeds assembly clearance and vision is unavailable?

## Exact system and regime

The general formulation is arbitrary peg-in-hole assembly with bounded relative pose uncertainty, represented by a six-dimensional relative C-space and its five-DOF contact hypersurface. The implemented examples are: (1) a simulated two-dimensional probe moving on a curve, with unknown position and orientation; and (2) a simulated three-dimensional probe on a 60 × 60 discretized surface, with a restricted straight-line sampling motion. The motivating physical setup is a ParaDex robot probing a fixtured lock with a pointed key. For that example the lock surface is assumed horizontal, the key vertical, and uncertainty is restricted to lock position in (x,y,z) and yaw. The paper also reports circular peg-in-hole assembly using the strategy and a modified straight-line-observation procedure for square peg-in-hole assembly; the available partial text does not establish trial counts or quantitative outcomes for those physical assemblies.

## Main claims

### Contact-map localization can resolve pose ambiguity in the simulated 2-D problem.

**OBSERVATION:** Across 100 simulation trials per grid size, the two-dimensional strategy localized the probe position on the curve and its orientation in every trial. Finer grids reduced average estimation error, while increasing average CPU time and number of moves after a threshold.

**AUTHOR INTERPRETATION:** Matching sequential contact observations to a pre-acquired C-space map can efficiently identify peg–hole misalignment; grid resolution trades localization accuracy against computation and probing effort.

**INFERENCE:** In the deterministic, discretized 2-D simulation regime, the approach can provide a reliable localization primitive if the resolution is selected within available computation.

**Intervention or measurement:** Simulated controller selected probe moves; environment returned contact-height observations. Results averaged over 100 randomized trials for each cell size; success meant localization to three or fewer cells.

**Observed result:** 100% success in the stated 2-D trials; lower residual-area error at higher grid resolution, with higher computation/moves (Fig. 12).

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Multiple grid sizes; randomized hidden curve pose/orientation; fixed success threshold; 100 trials per grid size.

**Alternative explanations not excluded:** Performance may depend on the chosen curve/simulation model, deterministic sensing and actuation, and the stopping rule.

**Scope limitations:** Simulation only; two-dimensional probe–curve formulation, not a full physical six-DOF assembly.

**Source pointer:** Sec. V–VI, p. 2539; Fig. 11–12; original PDF URL above.

### The direct cell-matching implementation becomes less reliable and more computationally costly in the simulated 3-D problem.

**OBSERVATION:** For a 60 × 60 unit-discretized surface, the 3-D strategy restricted exploration to straight lines to avoid computing general transformation sets. Over 100 trials per grid size, it was not always successful; larger cells increased failures, whereas finer resolution decreased error and increased average run time. Trials were aborted on a fixed time limit or when candidate count exceeded a threshold.

**AUTHOR INTERPRETATION:** Reduced within-cell height variation at coarse resolution weakens discrimination; finer cells create many more candidate cell combinations. The cell approach enables implementation on 3-D surfaces but exposes a computation–accuracy tradeoff.

**INFERENCE:** This deterministic map-matching formulation faces scaling constraints before it reaches the full six-dimensional uncertainty problem.

**Intervention or measurement:** Vary grid/cell size in 3-D simulations; record failures, estimation error, and time.

**Observed result:** Nonzero failures in the 3-D regime; finer grids improved localization error while raising computation (Fig. 13, described in text).

**Causal strength:** INTERVENTION EVIDENCE

**Controls:** Several grid sizes; 100 trials per grid size; identical restricted straight-line sampling formulation.

**Alternative explanations not excluded:** The straight-line constraint, surface geometry, abort criteria, and unreported hardware/runtime details may drive the reported tradeoff.

**Scope limitations:** The authors explicitly avoid general transformation-set computation; no demonstrated full 6-DOF implementation.

**Source pointer:** Sec. V–VI, pp. 2538–2539; Fig. 7, Fig. 13; original PDF URL above.

### Contact C-space is proposed as a general representation for pose-localization before insertion.

**OBSERVATION:** The paper defines the feasible relative peg–hole configurations as a six-dimensional volume bounded by a five-DOF contact hypersurface, and uses sequential contact observations plus a pre-acquired map to retain pose hypotheses consistent with observations.

**AUTHOR INTERPRETATION:** This representation generalizes the localization strategy to arbitrarily shaped peg-in-hole assemblies and converts alignment search into contact-map matching.

**INFERENCE:** Generality is a geometric formulation claim; practical generality remains unverified because reported implementations are restricted low-dimensional cases.

**Intervention or measurement:** Analytical C-space formulation and sampled-map matching; simulations and reported physical assembly demonstrations.

**Observed result:** A working localization procedure is shown for the restricted simulated cases; abstract reports simulations and experiments across assembly scenarios.

**Causal strength:** UNCLEAR

**Controls:** Comparison across discretization resolutions; no baseline method or quantitative experimental comparison was recoverable from the inspected partial text.

**Alternative explanations not excluded:** Success may rely on the point-probe approximation, horizontal/vertical fixture assumptions, high robot repeatability, or distinctive surface height patterns.

**Scope limitations:** A sampled map discretizes a continuous contact space; authors identify efficient transformation-set intersection and full-dimensional scaling as unresolved.

**Source pointer:** Abstract; Sec. I–II, pp. 2534–2535; Sec. VII, p. 2540; original PDF URL above.

## Important controls

- Random hidden initialization in the simulations, unknown to the controller.
- 100 runs per grid size in both the 2-D and 3-D simulations.
- Fixed success criterion: residual localization of three or fewer cells.
- Grid-size variation directly tests the resolution/computation tradeoff.

## Critical assumptions

- A pre-acquired contact C-space map is accurate enough for matching.
- In the reported ParaDex context, robot actuation and contact observations can be treated as deterministic; the paper attributes this to high accuracy and repeatability.
- In the lock–key example, the lock surface is horizontal, key vertical, and the key tip can be approximated as a point probe.
- The 3-D implementation assumes straight-line sampled motion to simplify candidate updates.

## Limitations

- Full six-dimensional localization is formulated but not implemented or validated here.
- Coarse map discretization reduces discriminative height variation; fine discretization raises candidate-combination cost.
- 3-D trials can fail under the stated time/candidate thresholds.
- The partial reading did not recover sufficient quantitative detail to assess the physical experiments independently.

## What this paper supports

- Contact-height probing against a pre-acquired map can localize pose in controlled, discretized low-dimensional simulations.
- Discretization resolution creates an empirical error/reliability/computational-cost tradeoff.
- Contact C-space provides a geometrically explicit representation of pre-insertion alignment uncertainty.

## What this paper does not establish

- Reliable full six-DOF, arbitrary-shape assembly localization in physical settings.
- Robustness to substantial sensing error, actuation error, map error, changing surfaces, or unknown contact compliance.
- Superiority to vision, spiral/exhaustive search, probabilistic localization, or other baselines.

## Explicit open questions

- How to compute transformation sets easily and represent them for fast intersections.
- How to distribute computation through multi-resolution subdivision.
- Whether a particle-filter formulation can address the localization problem more effectively; authors report only promising preliminary 2-D results.

## Evidence concerns

**Replication:** No independent replication identified or assessed in this card.

**Measurement limitations:** Localization error is residual uncertainty area/cell count; it is not a direct physical insertion-accuracy measurement in the reported simulations.

**Potential confounding:** Grid resolution changes both observation discriminability and computational burden; the design does not isolate those mechanisms. The deterministic robot/sensor assumption narrows external validity.

**Statistical / experimental concerns:** Simulations report 100 trials per grid size, but inspected excerpts do not provide confidence intervals, distributions, exact failure counts, or a quantitative physical-experiment result. This card is therefore PARTIAL.

## Source pointers

| Item | Source URL and section / figure / page |
|---|---|
| Abstract | https://citeseerx.ist.psu.edu/document?doi=3dd9b81f0c854367b2d861b4604e249e3d7545b2&repid=rep1&type=pdf ; p. 2534 |
| Full paper | Same URL; IROS 2003, pp. 2534–2540. Partially inspected through the source's indexed PDF text after direct PDF retrieval failed. |
| Main result | Same URL; Sec. V–VI, p. 2539; Fig. 11–13. |
| Important control | Same URL; Sec. V–VI, p. 2539; grid-size comparison and 100 trials per grid size. |
| Limitations | Same URL; Sec. VI–VII, pp. 2539–2540; transformation-set complexity, grid tradeoff, and future work. |
