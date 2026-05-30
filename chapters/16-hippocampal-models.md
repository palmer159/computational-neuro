# Hippocampal computation: place cells, replay, successor representations

The hippocampus is the most computationally **legible** part of the brain — beautiful single-cell tunings, identifiable circuit motifs, clean theory. It is also where the strongest brain↔AI bridges have been built ([CLS](https://en.wikipedia.org/wiki/Catastrophic_interference), replay, grid codes, successor representations).

## The macro-circuit: a 3-step loop

```mermaid
flowchart LR
    EC[Entorhinal Cortex<br/>grid cells, head-direction] --> DG[Dentate Gyrus<br/>pattern separation]
    DG --> CA3[CA3<br/>auto-associative attractor]
    CA3 --> CA1[CA1<br/>pattern completion + readout]
    CA1 --> EC
    EC --> CA1
    CA3 -.recurrent collaterals.-> CA3
```

Each subregion has a clear computational reading:

| Region | Function | ML analogue |
|---|---|---|
| **DG** | Sparse high-dim expansion; pattern separation | Random projections / hashing |
| **[CA3](https://en.wikipedia.org/wiki/Hippocampus_anatomy)** | Recurrent attractor; auto-associative recall | Hopfield network |
| **[CA1](https://en.wikipedia.org/wiki/Hippocampus_anatomy)** | Mismatch / novelty detector; main output | Comparator / decoder |
| **EC** | Spatial + non-spatial relational scaffold (grid cells) | Position embedding |

📄 [Marr, 1971 — Simple memory: a theory for archicortex](https://royalsocietypublishing.org/doi/10.1098/rstb.1971.0078). David Marr did this in 1971, before computers were common. He was right about the auto-associative role of CA3.

## Place cells & cognitive maps

Place cells in CA1 fire at specific locations in an environment. They remap when the environment changes. They reactivate during sleep, replaying past trajectories.

📄 [O'Keefe & Nadel, 1978 — The Hippocampus as a Cognitive Map (book)](https://en.wikipedia.org/wiki/Cognitive_map) — the founding text.

## Grid cells & the entorhinal scaffold

Grid cells in medial entorhinal cortex fire on a hexagonal lattice. Multiple grid scales from medial to lateral. Combined with head-direction and border cells, they constitute a **path-integration system** that the hippocampus reads out.

📄 [Hafting, Fyhn, Molden, Moser & Moser, 2005](https://doi.org/10.1038/nature03721) — discovered them. Nobel 2014.

📄 [Banino et al., 2018 — Vector-based navigation using grid-like representations in artificial agents](https://doi.org/10.1038/s41586-018-0102-6). Train an agent on path integration with a generic [RNN](https://en.wikipedia.org/wiki/Recurrent_neural_network); grid-like units emerge. **AI predicts neuro again.**

> Banino and colleagues at DeepMind trained a recurrent neural network to perform path integration — predicting position from a sequence of velocity inputs — and found that hexagonal grid-like units spontaneously emerged in the network's hidden layer. The grid units shared the key properties of biological grid cells: hexagonal lattice firing fields, multiple discrete spatial scales, and stable preferred orientations. Adding the grid representation enabled vector-based goal-directed navigation, including taking shortcuts through unfamiliar terrain — behaviors previously associated with hippocampal cognitive maps. The result mirrored Yamins-style convergence in vision: networks optimized for an ecological task spontaneously develop cortex-like representations as a side effect. It is one of the cleanest cases where AI predicted neuroscience, demonstrating that grid cells follow naturally from path-integration computation rather than requiring explicit hexagonal priors.

## Successor representations: the Rosetta stone

A representation of state $s$ as the **expected discounted future occupancy** of all other states under the current policy:

$$M(s, s') = \mathbb{E}\left[\sum_{t=0}^\infty \gamma^t \mathbb{1}(s_t = s') \mid s_0 = s\right]$$

📄 [Dayan, 1993 — Improving generalization for temporal difference learning: the successor representation](https://doi.org/10.1162/neco.1993.5.4.613). Originally an [RL](https://en.wikipedia.org/wiki/Reinforcement_learning) idea.

📄 [Stachenfeld, Botvinick & Gershman, 2017 — The hippocampus as a predictive map](https://doi.org/10.1038/nn.4650). Place cells **are** rows of the SR matrix; **grid cells are its eigenvectors**. One of the cleanest unifying results in the field.

> Stachenfeld, Botvinick, and Gershman propose that hippocampal place cells encode the rows of a successor representation (SR) matrix — the expected discounted future state-occupancies under the current policy — rather than instantaneous location. Under this view, place fields naturally distort to favor predictively relevant locations, an asymmetry that matches empirical observations during goal-directed navigation. They further show that grid cells in entorhinal cortex correspond to the principal eigenvectors of the SR, mathematically unifying place cells, grid cells, and the cognitive-map literature within reinforcement-learning theory. The framework explains a host of previously puzzling findings, including why place fields elongate against the direction of travel and why grid scales form a discrete hierarchy. For AI it provides one of the cleanest neuro→ML translations available: a hippocampal mechanism that generalizes value functions across reward changes, directly mirroring successor-feature methods in deep RL.

**🤖 AI-relevance.** Successor features and successor representations are an active area in deep RL ([Barreto et al., 2017](https://arxiv.org/abs/1606.05312)). They give you transferable value functions across reward changes. The neuro story is that the brain may implement them directly.

## Replay: the bridge to model-based RL

Hippocampal sharp-wave ripples reactivate trajectories — forward, reverse, even unobserved (shortcut) trajectories. This looks computationally like:

- **Experience replay** ([DQN](https://en.wikipedia.org/wiki/Q-learning)-style).
- **Planning** (Dyna-style, [MCTS](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)-style backups).
- **Generative simulation** (rollout of imagined futures).

📄 [Mattar & Daw, 2018 — Prioritized memory access explains planning and hippocampal replay](https://www.princeton.edu/~ndaw/md18.pdf). Replay statistics are well-fit by **prioritized sweeping** — the brain replays experiences whose updates have the most expected value. Tight neuro→ML mapping.

> Mattar and Daw derived a normative theory of hippocampal replay: which experience the brain should replay at any moment is the one whose memory access produces the largest expected improvement in future behavior. They formalized this as a product of two terms — "need" (how often the state will be visited) and "gain" (how much the value update would change behavior). Fitting this to hippocampal replay data, they showed it accounts for empirical patterns far better than random replay or simple recency: forward replay before decisions, reverse replay after rewards, and replay at choice points all fall out of the prioritization rule. The framework provides a principled neuroscience grounding for prioritized experience replay in deep RL and unifies replay, planning, and memory consolidation under a single optimization objective. It is one of the tightest neuro→ML mappings in current research and a model of how computational theory and biological data can mutually constrain each other.

📄 [Wittkuhn, Krippner, Koch & Schuck, 2024 — Replay in humans during fast offline planning](https://doi.org/10.1038/s41586-024-07675-8) — fast (~50 ms) sequential reactivation in humans during decision-making.

## Tolman-Eichenbaum Machine ([TEM](https://doi.org/10.1016/j.cell.2020.10.024))

📄 [Whittington, Muller, Mark, Chen, Barry, Burgess & Behrens, 2020 — The Tolman-Eichenbaum Machine: unifying space and relational memory through generalization in the hippocampal formation](https://doi.org/10.1016/j.cell.2020.10.024). A neural network model that derives place cells, grid cells, and relational generalization from a single self-supervised objective. Pure NeuroAI: explicitly designed to explain neural data and to compute non-trivially.

> Whittington and colleagues built the Tolman-Eichenbaum Machine (TEM), a neural network that learns to factor experience into a slowly varying structural component (e.g., the geometry of a maze) and a fast-changing content component (which objects are at which locations). The model is trained by self-supervised next-observation prediction with a memory module that combines structural and content codes. As the network learns, units in the structural module spontaneously develop grid-cell-like properties and units in the memory module develop place-cell-like properties — directly recovering the empirical signatures of entorhinal and hippocampal coding. Crucially, TEM generalizes to novel environments by reusing structural knowledge across content, mirroring relational generalization observed in animals and humans. The paper is one of the most successful examples of pure NeuroAI: a model designed jointly to explain neural data and to perform a non-trivial computation, and it has since been linked to transformer architectures in Whittington et al. (2022).

**🤖 AI-relevance.** TEM and successor-representation models are one of the most active interfaces between neuroscience and AI right now, and a great research topic for someone like you.

## What this all might mean for AI

If hippocampus is a:
- **Sparse memory store** ([DG](https://en.wikipedia.org/wiki/Dentate_gyrus)/CA3),
- **Pattern completion engine** (CA3),
- **Predictive map** (entorhinal SR),
- **Replay engine** for offline learning and planning (CA3 ripples),

then "AI is missing a hippocampus" is a coherent claim. Modern memory-augmented architectures (Memformer, MemGPT, retrieval-augmented LLMs, [Titans](https://arxiv.org/abs/2501.00663)) are step-zero attempts. None of them yet implement targeted, prioritized, generative replay during downtime.

## Sources

- [Behrens et al., 2018](https://doi.org/10.1016/j.neuron.2018.10.002) — modern review.
- [Eichenbaum, 2017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5538858/) — modern memory review.
- [Stachenfeld lab and Behrens lab papers](https://en.wikipedia.org/wiki/Hippocampus) — the most active groups in this niche.
