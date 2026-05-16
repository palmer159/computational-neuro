# Reinforcement learning & the basal ganglia

Builds on Ch 09 (dopamine) and Ch 06 ([BG](https://en.wikipedia.org/wiki/Basal_ganglia) action selection). Here we focus on the cleanest neuro→AI mappings in [RL](https://en.wikipedia.org/wiki/Reinforcement_learning).

## Mappings, succinctly

| RL concept | Brain implementation |
|---|---|
| [TD](https://en.wikipedia.org/wiki/Temporal_difference_learning) error δ | Phasic dopamine ([VTA](https://en.wikipedia.org/wiki/Ventral_tegmental_area) / SNc) |
| State value V(s) | Striatal medium spiny neurons (D1/D2) |
| Action value Q(s,a) | Striatum, [OFC](https://en.wikipedia.org/wiki/Orbitofrontal_cortex) |
| Policy π | Basal ganglia + motor cortex |
| Critic | Ventral striatum |
| Actor | Dorsal striatum |
| World model | Hippocampus + dmPFC |
| Successor representation | Hippocampal/EC predictive map |
| Eligibility trace | Synaptic tag (calcium / CaMKII), seconds |
| Discount factor γ | Serotonin (proposed) |
| Inverse temperature β | Noradrenaline (proposed) |
| Learning rate α | Acetylcholine (proposed) |
| Replay | Hippocampal SWRs |

This is the table that makes neuroscience worth your time as an RL researcher.

## Model-free vs model-based: arbitration

Two systems with different speed/flexibility trade-offs. The brain arbitrates between them based on **uncertainty**:

📄 [Daw, Niv & Dayan, 2005 — Uncertainty-based competition](https://www.princeton.edu/~ndaw/dnd05.pdf).
📄 [Lee, Shimojo & O'Doherty, 2014](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3968946/) — [fMRI](https://en.wikipedia.org/wiki/Functional_magnetic_resonance_imaging) evidence for arbitration.

**🤖 AI-relevance.** AI is rediscovering hybrid systems (Dyna, AlphaZero, Muzero). The neuroscience-inspired insight: **arbitrate dynamically based on epistemic uncertainty**, not static.

## Hierarchical RL: options & subgoals

Behavior is hierarchical: brush teeth → pick up brush → grasp → ... Brains likely implement RL hierarchically — supported by behavior, by lesion data, and by anatomy ([PFC](https://en.wikipedia.org/wiki/Prefrontal_cortex) encodes goals; BG encodes options; [M1](https://en.wikipedia.org/wiki/Primary_motor_cortex) encodes primitives).

📄 [Botvinick, Niv & Barto, 2009 — Hierarchically organized behavior and its neural foundations](https://doi.org/10.1016/j.cognition.2008.08.011).

**🤖 AI-relevance.** Options framework ([Sutton, Precup & Singh, 1999](https://doi.org/10.1016/S0004-3702(99)00052-1)), feudal RL, hierarchical actor-critic — all neuro-adjacent. [LLM](https://en.wikipedia.org/wiki/Large_language_model) agents that decompose goals into subgoals ("plan-then-execute") are doing hierarchical RL by another name.

## Goal-conditioned and meta-RL

The brain learns to learn. PFC carries task-set representations that bias all subordinate computation. PFC + DA can implement **meta-RL**, where the slow synaptic learning of an [RNN](https://en.wikipedia.org/wiki/Recurrent_neural_network) trains the RNN's own activity dynamics to be a fast RL learner.

📄 [Wang, Kurth-Nelson, Kumaran, Tirumala, Soyer, Leibo, Hassabis & Botvinick, 2018 — Prefrontal cortex as a meta-reinforcement learning system](https://doi.org/10.1038/s41593-018-0147-8). DeepMind. RNN trained on a distribution of bandits learns to do RL **in its activations**, without weight changes during the task. They argue this is what PFC + DA does.

**🤖 AI-relevance.** Meta-RL is one of the cleanest accounts of how slow learning produces fast adaptation. In-context learning in LLMs has the same flavor — slow weight learning during pretraining produces fast adaptation in activations during inference. Plausibly the same algorithmic family.

## Successor features for transfer

📄 [Barreto, Dabney, Munos, Hunt, Schaul, van Hasselt & Silver, 2017 — Successor features for transfer in reinforcement learning](https://arxiv.org/abs/1606.05312). Decompose value into reward weights × predictive features. Lets you transfer between tasks with shared dynamics but different rewards.

📄 [Momennejad et al., 2017 — The successor representation in human reinforcement learning](https://gershmanlab.com/pubs/Momennejad17.pdf). Behavioral evidence humans use SR-style learning.

## Curiosity / intrinsic motivation

Already covered in Ch 09. Worth restating: agents with intrinsic motivation learn more efficiently when extrinsic reward is sparse. The brain's curiosity machinery (novelty bursts, information-gain, dopaminergic signals to surprise) is a working biological example.

📄 [Schmidhuber, 1991 — A possibility for implementing curiosity and boredom in model-building neural controllers](http://people.idsia.ch/~juergen/curioussingapore/curioussingapore.html). The grand-old paper.
📄 [Pathak, Agrawal, Efros & Darrell, 2017 — Curiosity-driven exploration by self-supervised prediction](https://arxiv.org/abs/1705.05363). The modern deep-RL version.

## What current RL still does badly compared to brains

- One-shot learning of complex policies.
- Sparse extrinsic reward without bespoke shaping.
- Real-time embodied learning (not in simulation).
- Transfer across tasks with little common structure.
- Lifelong continual learning without catastrophic interference.

Each of these is a research direction informed by neuroscience.

## Sources

- Sutton & Barto 2nd ed. ch 14 (psychology), ch 15 (neuroscience). [Free PDF](http://incompleteideas.net/book/the-book-2nd.html).
- [Botvinick, Wang, Dabney, Miller, Kurth-Nelson, 2020 — Deep reinforcement learning and its neuroscientific implications](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7340124/). DeepMind's review.
