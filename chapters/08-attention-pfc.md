# Attention, executive control & prefrontal cortex

## Attention is not one thing either

Three roughly orthogonal axes (Posner & Petersen, 1990; modernized [Petersen & Posner, 2012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3413263/)):

- **Alerting** — global arousal; locus coeruleus, noradrenaline.
- **Orienting** — directing the spotlight; superior parietal, frontal eye fields.
- **Executive control** — selecting among conflicts; ACC, dlPFC.

And a separate distinction between **bottom-up** (stimulus-driven, salient pop-out) and **top-down** (goal-driven) attention.

## Biased competition: the canonical neural mechanism

📄 [Desimone & Duncan, 1995 — Neural mechanisms of selective visual attention](https://en.wikipedia.org/wiki/Visual_attention). Multiple stimuli compete for representation; top-down signals from PFC bias the competition toward the goal-relevant one. Empirical signature: a V4 neuron's response to its preferred stimulus is enhanced when attended.

**🤖 AI-relevance.** Soft attention in transformers is exactly this: query-driven competition resolved by softmax. It's striking how directly the biased-competition motif maps to QKV attention. See Ch 22.

## Prefrontal cortex: the executive

Lateral PFC handles working memory, rules, task switching, planning. Medial PFC (ACC, vmPFC) handles value, conflict, decision-making. Frontopolar PFC (BA 10) handles meta-level control and prospection.

**Lesion evidence.**
- vmPFC damage → poor decision-making despite intact intelligence (Phineas Gage, [Damasio, 1994](https://en.wikipedia.org/wiki/Descartes%27_Error)).
- dlPFC damage → working memory deficits, poor planning.
- Anterior cingulate (ACC) damage → poor error monitoring and conflict resolution.

## Mixed selectivity: the modern PFC story

PFC neurons don't cleanly encode "rule X" vs "stimulus Y." They encode random-looking nonlinear mixtures. This sounds like a bug; it's a feature.

📄 [Rigotti et al., 2013 — The importance of mixed selectivity in complex cognitive tasks](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4040002/). High-dimensional mixed representations make any task variable linearly readable. They are exactly what overparameterized neural networks produce.

**🤖 AI-relevance.** Mixed selectivity in PFC ≈ random feature representations / wide hidden layers. It is one of the deepest convergences between cortex and ML: both gain expressivity by being **nonlinearly random**, then doing linear readout.

## Cognitive control & the rule-governed brain

📄 [Miller & Cohen, 2001 — An integrative theory of prefrontal cortex function](https://en.wikipedia.org/wiki/Prefrontal_cortex#Theories_of_function). PFC represents goals and rules; biases processing throughout cortex to favor goal-consistent computations.

**🤖 AI-relevance.** This is the cleanest neuro framing of "in-context instruction-following." Modern LLM RLHF and instruction tuning produce systems that hold a specification and bias generation toward it. Whether the mechanism is the same is open and very interesting.

## Metacognition & error monitoring

The brain represents its own confidence. [Fleming & Lau, 2014](https://www.frontiersin.org/articles/10.3389/fnhum.2014.00443/full) review the neural correlates (rostrolateral PFC, ACC). Calibration matters: depression and schizophrenia involve metacognitive miscalibration.

**🤖 AI-relevance.** LLM hallucinations are calibration failures. Self-consistency, chain-of-thought verification, and verifier-guided sampling are first-pass attempts at machine metacognition. The brain's mechanisms here are still poorly understood — open frontier.

## Cognitive flexibility & set-shifting

Switching strategies under feedback is mediated by PFC + striatum. Dopamine controls the **stay vs switch** trade-off. Tonic vs phasic dopamine roughly maps to exploration vs exploitation. See [Cools & D'Esposito, 2011](https://en.wikipedia.org/wiki/Dopamine#Cognition_and_frontal_cortex).

## Sources

- Kandel ch 18, 65, 67.
- [Badre, 2008 — Cognitive control, hierarchy, and the rostro-caudal organization of the frontal lobes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2710857/).
- [Fuster — The Prefrontal Cortex (book, 5e)](https://en.wikipedia.org/wiki/Prefrontal_cortex) — the standard reference.
