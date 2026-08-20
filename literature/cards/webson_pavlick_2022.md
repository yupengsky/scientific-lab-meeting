# Do Prompt-Based Models Really Understand the Meaning of Their Prompts?

> Note: the requested author/year pair corresponds to this paper. “Measuring Inductive Biases of In-Context Learning with Underspecified Demonstrations” is a separate paper by Si et al. (ACL 2023).

## Metadata
**Authors:** Albert Webson, Ellie Pavlick
**Year:** 2022
**arXiv:** https://arxiv.org/abs/2109.01247
**Published venue:** NAACL-HLT 2022, pp. 2300–2344
**DOI:** 10.18653/v1/2022.naacl-main.167
**Publisher / proceedings:** ACL Anthology
**Publication status:** PUBLISHED
**Reading status:** FULL_TEXT

## Abstract
Using more than 30 manually written NLI templates and 13 target-word sets, the paper tests whether prompt-based models benefit from semantically meaningful instructions. Models often learn equally quickly from irrelevant or misleading templates; the pattern holds from 235M to 175B parameters and in instruction-tuned models. Target-word choice matters more than template meaning in the reported setting.

## Scientific question
Do prompt-based models use the semantic meaning of natural-language task instructions in a way analogous to humans?

## Main claims
- Irrelevant or misleading prompt templates can support similar NLI performance to instructive templates.
- Instruction-tuned models can remain robust to prompt semantics, including misleading prompts.
- LM target words/verbalizers have a larger effect than template meaning in these experiments.

## Key observations
- NLI performance was measured over prompt templates, target-word mappings, model sizes, and shot counts from 0 to 256 (Secs. 3–5; Figs. 2–7).
- Semantically irrelevant and pathological templates often produced similar learning curves to good templates (Sec. 4; Figs. 2–4).
- Changing target words produced larger performance changes than changing template semantics (Sec. 5; Fig. 7; Tables 2–4).
- Instruction tuning improved average robustness/performance but did not make behavior reliably sensitive to instruction meaning (Sec. 4.4).

## Evidence for major claims
Experimental design: Sec. 3. Template categories and NLI tasks: Sec. 3.1–3.3. Main semantic-sensitivity results: Sec. 4. Verbalizer analysis: Sec. 5. Limitations/discussion: Sec. 6.

## Observation vs interpretation
### Observed / demonstrated
- Under the tested NLI prompts, performance and few-shot learning curves were often similar across good, irrelevant, and misleading template wording.
- Scores changed substantially across LM target-word sets.
### Author interpretation
- The results provide limited evidence that performance gains come from understanding task instructions in a human-like way.
- Models may rely more on pretrained task knowledge, format, or verbalizer associations than prompt semantics.
### Inference
- The experiments causally manipulate wording while holding examples and task data fixed, so they test semantic dependence behaviorally; they do not identify the model’s internal representation or rule out partial semantic use.

## Important controls
- More than 30 manually designed templates; 13 target-word sets; zero- through few-shot trajectories; models from 235M to 175B; base and instruction-tuned models; deliberately irrelevant/pathological controls.

## Critical assumptions
- Template categories accurately represent semantic relevance and misleadingness.
- NLI accuracy and learning curves are adequate measures of instruction use.
- Target-word changes are a separable verbalizer intervention.

## Remaining alternative explanations
- Pretraining may already encode NLI behavior; templates may share useful surface format; target words may alter label priors; coarse behavioral equivalence can conceal different internal strategies.

## Limitations
The study centers on manually authored discrete prompts and NLI, with a finite template set and model sample; prompt semantics may matter in other tasks, languages, or architectures (Secs. 3 and 6).

## What this paper supports
Prompt success and few-shot improvement can occur without strong behavioral sensitivity to the literal meaning of the prompt, and verbalizer choice is a major confound.

## What this paper does NOT establish
It does not show that models never understand prompts, that all prompting gains are non-semantic, or that the finding applies to every task or instruction-following model.

## Explicit open questions
When prompt semantics are causally used, how to distinguish semantic use from pretrained task recognition, and how these effects vary beyond NLI (Sec. 6).

## Evidence concerns
**Replication:** GPT-3 access limits exact replication.
**Measurement limitations:** Behavioral performance cannot directly measure semantic representations.
**Potential confounding:** Template form, tokenization, verbalizers, and prior task knowledge co-vary.
**Statistical / experimental concerns:** Manual prompt selection and NLI-centric evaluation limit scope.

## Source pointers
| Item | Source |
|---|---|
| Abstract | https://arxiv.org/abs/2109.01247 |
| Full paper | https://aclanthology.org/2022.naacl-main.167.pdf |
| Main result | Sec. 4; Figs. 2–7 |
| Important control | Sec. 5; Fig. 7; Tables 2–4 |
| Limitations | Sec. 6 |
