# Curated reading list & papers (annotated)

Forty papers, organized by topic, each with a one-line "why this matters." Most freely accessible. **Bold** = top-priority.

## Foundations

- **[Hubel & Wiesel, 1962 — Receptive fields in cat V1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1359523/)** — the founding paper of vision neuroscience and spiritual ancestor of CNNs.
- [Hodgkin & Huxley, 1952 — A quantitative description of membrane current](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1392413/) — Nobel-winning model of the spike.
- [Mountcastle, 1997 — Columnar organization of neocortex](https://en.wikipedia.org/wiki/Cortical_column) — the canonical-cortex hypothesis.
- [Felleman & Van Essen, 1991 — Hierarchical processing in primate cortex](https://en.wikipedia.org/wiki/Visual_cortex) — the famous spaghetti diagram.

## Neural coding & representation

- **[Olshausen & Field, 1996 — Sparse coding of natural images](https://www.rctn.org/bruno/papers/sparse-coding.pdf)** — sparse-coding objective recovers V1 Gabor filters. Now the basis of LLM SAE interpretability.
- [Pouget, Dayan & Zemel, 2000 — Population codes](https://en.wikipedia.org/wiki/Population_coding) — probability in spike rates.
- [Quian Quiroga & Panzeri, 2009 — Decoding neural populations](https://en.wikipedia.org/wiki/Neural_decoding).
- [Rigotti et al., 2013 — Mixed selectivity in PFC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4040002/) — random nonlinear mixing for expressive readouts.

## Bayesian & predictive coding

- **[Rao & Ballard, 1999 — Predictive coding in V1](https://en.wikipedia.org/wiki/Predictive_coding)** — the most-cited candidate cortical algorithm.
- **[Friston, 2010 — Free-energy principle: a unified brain theory?](https://www.fil.ion.ucl.ac.uk/~karl/The%20free-energy%20principle%20A%20unified%20brain%20theory.pdf)** — the FEP manifesto.
- [Knill & Pouget, 2004 — The Bayesian brain](https://en.wikipedia.org/wiki/Bayesian_approaches_to_brain_function).
- [Whittington & Bogacz, 2017 — Predictive coding ≈ backprop with local rules](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5467749/).

## Memory & hippocampus

- **[McClelland, McNaughton & O'Reilly, 1995 — Complementary learning systems](https://en.wikipedia.org/wiki/Catastrophic_interference)** — the framework that justified replay buffers.
- **[Hafting et al., 2005 — Grid cells in entorhinal cortex](https://en.wikipedia.org/wiki/Grid_cell)** — Nobel 2014.
- **[Stachenfeld, Botvinick & Gershman, 2017 — Hippocampus as a predictive map](https://en.wikipedia.org/wiki/Hippocampus)** — successor representations as place + grid cells. Field-defining.
- [Kumaran, Hassabis & McClelland, 2016 — What learning systems do intelligent agents need?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4920642/) — DeepMind manifesto.
- [Whittington et al., 2020 — Tolman-Eichenbaum Machine](https://en.wikipedia.org/wiki/Hippocampus#Models_of_hippocampal_function) — neural model unifying space + relations.
- [Mattar & Daw, 2018 — Prioritized memory access explains replay](https://www.princeton.edu/~ndaw/md18.pdf).

## Reward & RL in the brain

- **[Schultz, Dayan & Montague, 1997 — Neural substrate of prediction & reward](https://www.gatsby.ucl.ac.uk/~dayan/papers/sdm97.pdf)** — dopamine = TD error. Required reading.
- [Daw, Niv & Dayan, 2005 — Uncertainty-based competition between MF and MB](https://www.princeton.edu/~ndaw/dnd05.pdf).
- **[Dabney et al., 2020 — Distributional code for value in dopamine](https://arxiv.org/abs/1707.06887)** — AI predicted neuroscience.
- [Niv, 2009 — RL in the brain (review)](https://www.princeton.edu/~yael/Publications/Niv2009.pdf) — best pedagogical entry.
- [Doya, 2002 — Metalearning and neuromodulation](https://en.wikipedia.org/wiki/Neuromodulation) — neuromodulators ↔ RL hyperparameters.

## Deep learning ↔ cortex

- **[Yamins et al., 2014 — Performance-optimized models predict IT](https://www.pnas.org/doi/10.1073/pnas.1403112111)** — task pressure produces brain-like representations.
- [Yamins & DiCarlo, 2016 — Goal-driven DNNs as models of sensory cortex](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6526887/).
- **[Schrimpf et al., 2021 — LMs predict language cortex](https://www.pnas.org/doi/10.1073/pnas.2105646118)**.
- [Goldstein et al., 2022 — Shared computational principles for human + LLM language](https://en.wikipedia.org/wiki/Language_model).
- [Beniaguev, Segev & London, 2021 — A single neuron is a deep ANN](https://www.biorxiv.org/content/10.1101/613141v2.full).
- [Kar et al., 2019 — Recurrence helps recognition](https://en.wikipedia.org/wiki/Recurrent_neural_network).

## Biologically plausible learning

- **[Lillicrap et al., 2020 — Backpropagation and the brain](https://arxiv.org/abs/2004.13316)** — the status-of-the-field paper.
- [Lillicrap et al., 2016 — Feedback alignment](https://arxiv.org/abs/1411.0247).
- [Payeur et al., 2021 — Burstprop / dendritic learning](https://en.wikipedia.org/wiki/Backpropagation).
- [Scellier & Bengio, 2017 — Equilibrium propagation](https://www.frontiersin.org/articles/10.3389/fncom.2017.00024/full).
- [Richards et al., 2019 — Deep learning framework for neuroscience](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7115933/).

## NeuroAI manifestos & directions

- **[Hassabis, Kumaran, Summerfield & Botvinick, 2017 — Neuroscience-inspired AI](https://arxiv.org/abs/1709.05206)** — DeepMind manifesto.
- **[Lake, Ullman, Tenenbaum & Gershman, 2017 — Building machines that learn and think like people](https://arxiv.org/abs/1604.00289)** — cognitive science manifesto.
- [Doerig et al., 2023 — Neuroconnectionist research programme](https://arxiv.org/abs/2209.03718).
- [Botvinick et al., 2020 — Deep RL and its neuroscientific implications](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7340124/).
- [Wang et al., 2018 — PFC as meta-RL](https://en.wikipedia.org/wiki/Meta-learning_(computer_science)).
- [Banino et al., 2018 — Vector navigation with grid-like RNN units](https://en.wikipedia.org/wiki/Grid_cell) — AI paper that recovered grid cells.
- [LeCun, 2022 — A path towards autonomous machine intelligence](https://openreview.net/pdf?id=BZ5a1r-kVsf) — strongly opinionated AGI architecture proposal.

## Transformers, LLMs, language

- **[Ramsauer et al., 2020 — Hopfield Networks is All You Need](https://arxiv.org/abs/2008.02217)** — softmax attention = modern Hopfield.
- [Whittington et al., 2022 — Relating transformers to hippocampus](https://arxiv.org/abs/2112.04035).
- [Fedorenko, Ivanova & Regev, 2024 — Language network as a natural kind](https://en.wikipedia.org/wiki/Language_module) — language is for communication, not thought.
- [Mitchell & Krakauer, 2023 — The debate over understanding in LLMs](https://arxiv.org/abs/2210.13966).

## Consciousness

- [Dehaene & Changeux, 2011 — Global neuronal workspace review](https://en.wikipedia.org/wiki/Global_workspace_theory).
- [Tononi et al., 2016 — Integrated information theory](https://www.eecs.qmul.ac.uk/~mpurver/papers/tononi-etal-iit.pdf).
- [Cogitate consortium, 2025 — Adversarial collaboration GWT vs IIT](https://en.wikipedia.org/wiki/Neural_correlates_of_consciousness).

## A 5-paper "if you only read 5" list

1. **Hassabis et al., 2017 — Neuroscience-Inspired AI** (the field's raison d'être).
2. **Schultz, Dayan & Montague, 1997** (the cleanest brain↔AI mapping).
3. **Yamins et al., 2014** (the convergence that started the modern wave).
4. **McClelland, McNaughton & O'Reilly, 1995** (CLS — explains replay buffers and continual learning).
5. **Lake, Ullman, Tenenbaum & Gershman, 2017** (what AI is missing, from cognitive science).
