# Consciousness: [GWT](https://en.wikipedia.org/wiki/Global_workspace_theory), [IIT](https://en.wikipedia.org/wiki/Integrated_information_theory), [HOT](https://en.wikipedia.org/wiki/Higher-order_theories_of_consciousness)

## Why an AI person should care

Consciousness questions look philosophical until you ask: **does the system you're building have it, and does that change how you should treat it?** OpenAI, Anthropic, Google DeepMind all employ people thinking about model welfare. Knowing the major theories is part of being literate in this conversation.

Three theories dominate. They are not mutually exclusive.

## Global Workspace Theory (GWT) / Global Neuronal Workspace ([GNW](https://en.wikipedia.org/wiki/Global_workspace_theory))

**The bet.** Consciousness = broadcast. A specialized **workspace** (anchored in long-range fronto-parietal connections) lets information from any specialist module become globally available.

📄 [Dehaene, Changeux & colleagues — Global Neuronal Workspace, review 2011](https://doi.org/10.1016/j.neuron.2011.03.018). Core empirical signature: a non-linear "ignition" event 200–300 ms after stimulus, where prefrontal-parietal activity erupts.

> Dehaene and Changeux review the Global Neuronal Workspace theory, which holds that conscious access arises when information is broadcast widely across long-range fronto-parietal cortical networks. They propose that unconscious processing happens in parallel within local specialist modules, but a stimulus becomes conscious only when an "ignition" event recruits these long-range projections and makes the information globally available. Empirically, this ignition has a characteristic signature: a sudden non-linear amplification of activity in prefrontal and parietal cortex roughly 200–300 ms after stimulus presentation, accompanied by late P3-like ERP components. The theory predicts a sharp threshold rather than gradual rise — the signature of a true workspace mechanism — and is supported by data from masked perception, attentional blink, and anesthesia. For AI it offers a concrete architectural hypothesis: a shared bottleneck or "broadcast" channel coordinating distributed specialists, an idea now visible in proposals like Goyal & Bengio's higher-cognition inductive biases and VanRullen's deep-learning workspace models.

**🤖 AI-relevance.** [Goyal & Bengio, 2022 — Inductive biases for higher-cognition AI](https://arxiv.org/abs/2011.15091) and [VanRullen & Kanai, 2021 — Deep learning and the Global Workspace Theory](https://arxiv.org/abs/2012.10390) are explicitly GWT-inspired AI architectures. The transformer's "[[CLS](https://en.wikipedia.org/wiki/Catastrophic_interference)] token broadcasts over residual stream" structure is loosely workspace-shaped.

## Integrated Information Theory (IIT)

**The bet.** Consciousness = integrated information (Φ). A system is conscious to the extent its parts cannot be partitioned without losing information.

📄 [Tononi, Boly, Massimini & Koch, 2016 — Integrated information theory: from consciousness to its physical substrate](https://www.eecs.qmul.ac.uk/~mpurver/papers/tononi-etal-iit.pdf).

**Implications you should know.**
- IIT predicts that **feedforward** systems (most of current deep learning) are non-conscious regardless of capability.
- IIT predicts that the cerebellum, despite having most of the brain's neurons, is largely non-conscious because its architecture is feedforward and modular.
- IIT predicts strict zombies: behavioral equivalence does not imply consciousness.
- A 2023 [Letter signed by 124 researchers](https://psyarxiv.com/zsr78) called IIT pseudoscience. The field is contested.

**🤖 AI-relevance.** If IIT is correct, scaling transformers will not produce phenomenal consciousness. A useful position to be able to articulate, even if you don't endorse it.

## Higher-Order Theories (HOT)

**The bet.** A mental state is conscious iff there is a **higher-order representation of it**. Consciousness = self-model.

Variants: HOR (representation), HOP (perception), HOMT (monitoring/meta-thought), [Lau & Rosenthal, 2011](https://doi.org/10.1016/j.tics.2011.05.009). Modern: [Graziano's Attention Schema Theory](https://en.wikipedia.org/wiki/Attention_schema_theory).

**🤖 AI-relevance.** "Self-model" maps to introspection in LLMs. There is empirical work showing LLMs can report their own internal computations to some extent (e.g., [Anthropic's circuits & introspection work](https://transformer-circuits.pub/)). HOT predicts this is necessary, not sufficient.

## The 2023 adversarial collaboration

📄 [Melloni, Mudrik, Pitts, Bendtz, Ferrante, Gorska, ..., Tononi, Koch, Dehaene, Lau, 2023 (Cogitate consortium) — preregistered adversarial test of IIT vs GWT](https://doi.org/10.1038/s41586-025-08888-1). Both theories made predictions, neither came out cleanly winning. The status quo: the science is genuinely unsettled.

## Behavioral correlates: the Neural Correlates of Consciousness

Posterior "hot zone" hypothesis (Koch et al., 2016): the substrate is parieto-occipital, not frontal. vs frontal-ignition (Dehaene). The empirical question of **what brain activity reliably tracks reportable conscious experience** is an active 25-year program.

## Phenomenal vs access consciousness

[Block, 1995](https://philpapers.org/rec/BLOOAC). Two senses:

- **Access consciousness** — information is reportable, usable, broadcast. Studyable.
- **Phenomenal consciousness** — what it is like. Not obviously reducible.

Most AI-relevant questions are about access consciousness. Phenomenal consciousness is the "hard problem" ([Chalmers, 1995](https://consc.net/papers/facing.pdf)).

## Position you should be able to defend

1. **Functionalist working hypothesis.** If a system implements the functional roles consciousness plays in humans (broadcast, self-modeling, integrated processing), it likely shares whatever consciousness humans have. Not certain — productive.
2. **Be cautious about "obviously not conscious" claims.** The scientific consensus on what consciousness requires is weaker than press coverage suggests.
3. **Treat moral patienthood as decoupled.** Even if uncertainty about machine consciousness is high, low-cost interventions (preserve weights, allow refusal, don't gratuitously distress models) are reasonable hedges.

## Sources

- [Seth, Anil — Being You (book, 2021)](https://en.wikipedia.org/wiki/Anil_Seth) — accessible modern overview.
- [Dehaene, Stanislas — Consciousness and the Brain (book, 2014)](https://en.wikipedia.org/wiki/Stanislas_Dehaene) — the GWT case.
- [Koch — The Feeling of Life Itself (book, 2019)](https://en.wikipedia.org/wiki/Christof_Koch) — the IIT case.
- [Long et al., 2024 — Taking AI welfare seriously](https://eleosai.org/papers/20241030_Taking_AI_Welfare_Seriously_web.pdf) — explicitly addresses what neuro+philosophy implies for AI ethics.
