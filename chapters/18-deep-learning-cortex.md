# Deep learning ↔ cortex: convergent representations

The empirical finding that brought deep learning back to neuroscience.

## The result that started this wave

📄 [Yamins, Hong, Cadieu, Solomon, Seibert & DiCarlo, 2014 — Performance-optimized hierarchical models predict neural responses in higher visual cortex](https://www.pnas.org/doi/10.1073/pnas.1403112111). Train a CNN on ImageNet; its top layers predict macaque IT firing rates better than any prior model. ImageNet performance and IT-prediction are correlated.

Three years later: [Kriegeskorte, 2015 — Deep neural networks: a new framework for modeling biological vision and brain information processing](https://en.wikipedia.org/wiki/Convolutional_neural_network#Biological_inspiration). The framing that cemented the methodology.

## Brain-Score: the leaderboard

[Schrimpf et al. — Brain-Score: which artificial neural network for object recognition is most brain-like?](https://www.brain-score.org/). Standard benchmark: how well does your model predict V1, V2, V4, IT recordings, plus behavioral consistency? Anyone publishing a model of vision references this.

Notable trend: the strongest predictors of brain data are **the strongest models on ImageNet/CLIP-style benchmarks**, not models that "look biological." Performance, not plausibility, predicts brain-likeness — within vision.

## Beyond vision: language

📄 [Schrimpf, Blank, Tuckute, Kauf, Hosseini, Kanwisher, Tenenbaum & Fedorenko, 2021 — The neural architecture of language: Integrative modeling converges on predictive processing](https://www.pnas.org/doi/10.1073/pnas.2105646118). LLMs predict cortical responses to sentences. The better the model at next-word prediction, the better at predicting the brain. **Language cortex looks like an autoregressive language model.**

📄 [Caucheteux & King, 2022 — Brains and algorithms partially converge in natural language processing](https://www.nature.com/articles/s42003-022-03036-1). Confirms and extends.

📄 [Goldstein et al., 2022 — Shared computational principles for language processing in humans and deep language models](https://en.wikipedia.org/wiki/Language_model). ECoG recordings during natural conversation predicted by GPT-2 embeddings.

**🤖 AI-relevance.** The convergence holds beyond vision. Language cortex behaves like a LM. This does not mean human language IS GPT — it means whatever cortex is computing for language is in a representational neighborhood that next-token prediction also reaches.

## Audition

📄 [Kell, Yamins, Shook, Norman-Haignere & McDermott, 2018 — A task-optimized neural network replicates human auditory behavior, predicts brain responses, and reveals a cortical processing hierarchy](https://mcdermottlab.mit.edu/papers/Kell_etal_2018_DNN_auditory_cortex.pdf).

CNNs trained on speech + music predict A1 and beyond.

## What this convergence is and is not

**Is.** Trained ANNs are by far the best **predictive models** of sensory cortex. They beat hand-crafted models that came before by a wide margin. This is non-trivial.

**Is not.** Mechanistic explanations. A CNN that predicts IT firing rates linearly does not tell us what learning rule cortex uses, what objective it optimizes, or what the actual circuit is doing. Predicting ≠ explaining.

This caveat has spawned a literature on **how to use ANNs as scientific models without confusing prediction for explanation**:

📄 [Cao & Yamins, 2024 — Explanatory models in neuroscience, Part 1 & 2](https://arxiv.org/abs/2104.01489) — careful philosophy.
📄 [Doerig et al., 2023 — The neuroconnectionist research programme](https://arxiv.org/abs/2209.03718) — the field's status doc.

## Representational Similarity Analysis (RSA)

A common methodology: compute pairwise stimulus-by-stimulus similarity matrices in (a) brain population activity, (b) ANN layer activations. Compare matrices.

📄 [Kriegeskorte, Mur & Bandettini, 2008 — Representational similarity analysis](https://www.frontiersin.org/articles/10.3389/neuro.06.004.2008/full).

**🤖 AI-relevance.** RSA is increasingly used in interpretability — comparing model layers across architectures, comparing aligned models, comparing pre/post fine-tuning. It is a scientific tool that came from neuro and is migrating into ML.

## What deep nets get wrong about cortex

Even within vision:

- **Adversarial robustness** is poor in CNNs but not in primates ([Geirhos et al.](https://arxiv.org/abs/1811.12231)).
- **Texture vs shape bias** differs.
- **Sample efficiency** is dramatically different — humans need orders of magnitude fewer examples.
- **Recurrence**. Cortex is massively recurrent; CNNs are mostly feedforward. Adding recurrence improves brain prediction, especially for difficult/occluded stimuli ([Kar et al., 2019](https://en.wikipedia.org/wiki/Recurrent_neural_network)).

## Strong takeaway

Where backprop-trained nets succeed at cortex prediction, they vindicate a research strategy: **objective + architecture + data ≈ representations**. They do not vindicate any specific account of how cortex itself learns.

## Sources

- [Doerig et al., 2023](https://arxiv.org/abs/2209.03718).
- [Yamins & DiCarlo, 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6526887/).
- [Kriegeskorte & Douglas, 2018](https://en.wikipedia.org/wiki/Cognitive_neuroscience).
