# Does Circuit Analysis Interpretability Scale? Evidence from Multiple Choice Capabilities in Chinchilla

## Metadata

**Authors:** Tom Lieberum, Matthew Rahtz, János Kramár, Neel Nanda, Geoffrey Irving, Rohin Shah, Vladimir Mikulik

**Year:** 2023

**arXiv:** [2307.09458](https://arxiv.org/abs/2307.09458)

**Published venue:** arXiv

**DOI:** UNCLEAR

**Publisher / proceedings:** arXiv

**Publication status:** PREPRINT

**Reading status:** FULL_TEXT

---

## Abstract

The paper tests whether circuit-analysis methods scale to Chinchilla 70B using multiple-choice answering. Logit attribution, attention visualization, and activation patching identify a small set of output attention heads and MLPs. “Correct letter” heads show compressible query/key/value structure, with query/key features partly representing enumeration position and values carrying token identity; semantic generalization is mixed.

## Scientific question

Can circuit-analysis techniques identify and causally validate interpretable mechanisms in a frontier-scale language model?

## Main claims

- Existing circuit tools scale sufficiently to identify a distributed output circuit in Chinchilla 70B.
- Correct-letter heads can be categorized and compressed with limited performance loss in the tested setting.
- Their semantic interpretation is only partial and distribution-dependent.

## Key observations

- Activation patching of identified nodes changes loss, and patching the set together recovers substantial performance (Sec. 3.1).
- Heads cluster into correct-letter, single-letter, uniform, and amplification/content-gatherer behaviors (Sec. 3.2; Appendix E).
- Low-rank QK/OV interventions preserve performance on several mutations, while random letters retain only part of the effect and number labels largely fail (Sec. 4.1–4.2, Fig. 11).
- L24 H18 has large total effect but small direct effect, consistent with an indirect role through correct-letter heads (Sec. 3.1; Appendix B).

## Evidence for major claims

- Logit attribution and attention patterns nominate output nodes; activation patching validates causal contribution (Sec. 3).
- Prompt mutations test whether the hypothesized “nth item in an enumeration” feature generalizes (Sec. 4.2, Fig. 11).

## Observation vs interpretation

### Observed / demonstrated

- Patching selected heads/MLPs changes correct-answer-letter loss.
- Low-rank subspace interventions can match full-rank effects in tested prompts.
- Generalization to random letters is partial; number-label performance and head contribution are poor.

### Author interpretation

- QK subspaces encode an enumeration-position feature and values encode token identity.
- The circuit performs content gathering followed by answer-letter selection/amplification.

## Important controls

- 1B, 7B, and 70B Chinchilla comparison; standard 5-shot MMLU is effective mainly at 70B (Sec. 2.2).
- Prompt mutations: random letters, ordered letters, numbers, separators, and prelude removal (Sec. 4.2).
- Direct versus total effects distinguish direct output roles from upstream mediation (Sec. 2.3, 3.1).

## Critical assumptions

- Patching from carefully selected source prompts estimates component contribution without introducing artifacts that dominate interpretation.
- Low-rank preservation on tested mutations indicates feature compression rather than prompt-specific memorization.

## Remaining alternative explanations

- The learned directions may be specific to multiple-choice formatting or tokenization.
- Partial generalization leaves open whether “enumeration” is the full semantic feature.

## Limitations

- The paper reports mixed semantic results; identified directions do not always explain behavior on broader distributions (Sec. 1, 4).
- The studied capability is multiple-choice answer-label selection, not general ICL.

## What this paper supports

- Causal circuit analysis can identify useful, distributed mechanisms in a 70B model.
- Large-model circuit interpretations require behavioral mutation tests and retain uncertainty about feature semantics.

## What this paper does NOT establish

- A universal or complete circuit for ICL.
- That correct-letter heads implement a fully general enumeration abstraction.

## Explicit open questions

- How broadly the identified head semantics transfer beyond multiple-choice tasks and label formats.
- Whether the same methods scale to more distributed capabilities.

## Evidence concerns

**Replication:** Single model family and primary case study; cross-model replication is limited.

**Measurement limitations:** Loss on answer labels is the principal outcome.

**Potential confounding:** Prompt format, tokenization, and rarity of multiple-choice data may drive scale dependence.

**Statistical / experimental concerns:** Several conclusions are based on selected prompt mutations and approximate low-rank interventions.

## Source pointers

| Item | Source |
|---|---|
| Abstract | https://arxiv.org/abs/2307.09458 |
| Full paper | https://arxiv.org/html/2307.09458 |
| Main result | Sec. 3.1; Fig. 11 |
| Important control | Sec. 4.2; Fig. 11 |
| Limitations | Sec. 1; Sec. 4.2 |
