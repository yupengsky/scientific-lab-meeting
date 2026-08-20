# Transformers Learn In-Context by Gradient Descent

## Metadata

**Authors:** Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, Max Vladymyrov

**Year:** 2023

**arXiv:** https://arxiv.org/abs/2212.07677

**Published venue:** ICML 2023, PMLR 202

**DOI:** Not recorded in source

**Publisher / proceedings:** PMLR 202; exact proceedings URL not verified in the paper text

**Publication status:** PUBLISHED

**Reading status:** FULL_TEXT

---

## Abstract

The paper studies whether self-attention transformers can perform gradient-based learning during the forward pass. A linear self-attention layer can implement one gradient-descent update for linear regression. Synthetically trained self-attention-only transformers resemble gradient descent; deeper models can perform curvature correction. With MLPs, models learn linear predictors on learned representations for nonlinear regression.

## Scientific question

Can in-context prediction in transformers be mechanistically understood as an implicit optimization procedure operating on the context?

## Main claims

The authors claim that trained synthetic transformers can become “mesa-optimizers”: their forward pass constructs and updates an implicit predictor using context examples. They present this as one mechanism for ICL, not a universal account of language-model ICL.

## Key observations

- Explicit linear-self-attention weights reproduce one GD step on mean-squared-error linear regression (Sec. 2; Proposition 1).
- Trained linear self-attention models either approach this construction or produce predictors closely aligned with GD on in- and out-of-distribution validation tasks (Sec. 2–3; Figs. 2–4).
- Multiple layers can show iterative curvature correction and outperform plain GD (Sec. 3; Figs. 5–6).
- For nonlinear regression, MLP-plus-attention models behave like linear learning on learned/deep representations (Sec. 3; Figs. 7–9).
- Token representations become suitable for later in-context updates; the result is not restricted to the paper’s initial tokenization (Sec. 4; Fig. 10).

## Evidence for major claims

The constructive equivalence is algebraic. The empirical evidence uses self-attention-only or MLP-augmented transformers trained on synthetic regression distributions and compares their predictions, weights, and layerwise behavior with GD/meta-learned baselines. No natural-language transformer is trained or causally dissected.

## Observation vs interpretation

### Observed / demonstrated

- A specified linear attention parameterization has the same data transformation as one GD update.
- Synthetic trained models match GD-like predictors and exhibit layerwise improvements consistent with curvature correction.

### Author interpretation

- The trained forward pass implements gradient-based optimization of an implicit context-dependent loss.
- Induction-head-like behavior may be a special case of this optimization mechanism.

## Important controls

- Comparisons with explicit GD, meta-learned output layers, and kernel/regression baselines.
- In- versus out-of-distribution validation tasks.
- Linear versus nonlinear regression and token-encoding variants.

## Critical assumptions

- The task distribution is synthetic regression and the relevant loss is compatible with the constructed attention computation.
- Similar predictions/weights imply algorithmic similarity; this is stronger when paired with the explicit construction but does not identify a unique mechanism.

## Remaining alternative explanations

Associative-memory, retrieval, induction-head, or other learned algorithms could explain the same restricted behavior. The paper does not distinguish these mechanisms in natural-language LMs.

## Limitations

The authors state that the findings concern linear self-attention-only transformers and explain only a limited part of a complex process; ICL may have multiple mechanisms (Introduction, pp. 2–3). The inner loss is implicit and its generality is not established.

## What this paper supports

- Linear attention can realize GD in the forward pass.
- Synthetic transformer training can discover GD-like or related optimization procedures.

## What this paper does NOT establish

- That all transformer ICL, especially natural-language ICL, is gradient descent.
- That prediction similarity proves the unique internal causal algorithm.

## Explicit open questions

How these mechanisms extend to other transformer shapes, domains, distributions, and natural language; how the implicit loss is constructed; and how the mechanism relates causally to induction heads (Introduction, Conclusion).

## Evidence concerns

**Replication:** Code is linked by the paper; cross-seed and natural-language replication are not established here.

**Measurement limitations:** Algorithmic matching is measured mainly through outputs, weights, and representational comparisons.

**Potential confounding:** Synthetic task distribution and architecture make GD easy to represent.

**Statistical / experimental concerns:** Scope is controlled and narrow; no evidence of broad-model necessity or sufficiency.

## Source pointers

| Item | Source |
|---|---|
| Abstract | https://arxiv.org/abs/2212.07677 |
| Full paper | https://arxiv.org/pdf/2212.07677 |
| Main result | Secs. 2–4; Figs. 2–10; Proposition 1 |
| Important control | GD/meta-learning comparisons, Secs. 2–3 |
| Limitations | Introduction, pp. 2–3; Conclusion |
