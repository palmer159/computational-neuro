# World models, planning & model-based cognition

## What a world model is

A **world model** is an internal predictive model of how the world evolves: $P(s_{t+1} \mid s_t, a_t)$. Variants:

- **Dynamics model** — predict next state given action.
- **Generative model** — sample full trajectories.
- **Latent world model** — model in a learned compact state space.

The brain has all three, distributed across cerebellum, hippocampus, prefrontal cortex.

## The case for world models in cognition

Behavioral evidence:

- **Tolman's rats** — already in the 1940s, rats showed they had cognitive maps and could plan novel routes ([Tolman, 1948](https://en.wikipedia.org/wiki/Cognitive_map)).
- **Mental simulation** — humans simulate physical interactions to answer "would the tower fall?" with errors that match a noisy physics simulator ([Battaglia, Hamrick & Tenenbaum, 2013](https://www.pnas.org/doi/10.1073/pnas.1306572110)).
- **Imagination during rest** — hippocampal replay sometimes traces routes the animal has never taken; consistent with offline planning.

Neural evidence:

- Hippocampal preplay and forward sweeps before decision points ([Pfeiffer & Foster, 2013](https://en.wikipedia.org/wiki/Place_cell#Preplay)).
- Theta-sweep encoding of upcoming options at choice points.
- vmPFC encoding of imagined outcomes ([Schacter, Addis & Buckner, 2007](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2477443/)).

## The cerebellum as a forward model

Already in Ch 06. Cerebellum predicts sensory consequences of motor commands and learns from errors. Generic supervised learner with strong wiring priors.

📄 [Wolpert, Miall & Kawato, 1998 — Internal models in the cerebellum](https://en.wikipedia.org/wiki/Internal_model_(motor_control)).

## Hippocampus as a generative model

📄 [Buckner, 2010 — The role of the hippocampus in prediction and imagination](https://en.wikipedia.org/wiki/Episodic_memory#Future_thinking). Patients with hippocampal damage cannot vividly imagine future scenes — episodic memory and episodic future thought are bound together.

This is consequential: the same neural machinery for remembering and for imagining suggests **memory is sampling from a generative model**, not retrieval from a database.

## World models in modern AI

📄 [Ha & Schmidhuber, 2018 — World Models](https://arxiv.org/abs/1803.10122) and [their NeurIPS version](https://worldmodels.github.io/). Latent world model + dreamed-up policy training. Brought neuroscience-flavored world-model thinking back to deep learning.

📄 [Hafner et al., DreamerV3, 2023](https://arxiv.org/abs/2301.04104). Model-based deep RL via latent world models. Strong on diverse benchmarks.

📄 [Schrittwieser et al., MuZero, 2020 — Mastering Atari, Go, Chess and Shogi by planning with a learned model](https://arxiv.org/abs/1911.08265). Plan with a learned latent model. Closer to brain-style model-based RL than AlphaGo.

📄 [LeCun, 2022 — A path towards autonomous machine intelligence](https://openreview.net/pdf?id=BZ5a1r-kVsf). Argues the missing piece for AGI is hierarchical predictive world models, with planning at multiple time scales. Brains are the existence proof.

## Planning: tree search vs amortized inference

Two regimes of model use:

| | Brain | AI |
|---|---|---|
| **Explicit search** | hippocampal forward replay, deliberate cognition | MCTS, beam search |
| **Amortized inference** | habit, intuition, "system 1" | A trained policy network |

The brain seamlessly arbitrates. AlphaZero/MuZero arbitrate explicitly via training. LLMs running chain-of-thought are doing a form of amortized search through the latent space; verifier-guided sampling adds more explicit search.

📄 [Daw, Gershman, Seymour, Dayan & Dolan, 2011 — Model-based influences on humans' choices and striatal prediction errors](https://www.princeton.edu/~ndaw/dgsdd11.pdf). Behavioral assay (the two-step task) widely used to dissect MF/MB in humans.

## Causal models: a known gap

Brains seem to extract causal structure from limited data; modern AI mostly does not. Causality remains an open problem with strong neuro-inspired hypotheses about interventional, counterfactual cognition. See [Lake et al., 2017 — Building machines that learn and think like people](https://arxiv.org/abs/1604.00289). A great single read.

## What "world models" really need to add to LLMs

LLMs implicitly contain world knowledge. They are weak at:
- Long-horizon, action-conditioned prediction.
- Counterfactual simulation.
- Embodied causal interaction.
- Maintaining persistent state across long horizons.

The neuro story suggests these capabilities require dedicated machinery — hippocampus-like memory, cerebellum-like forward models, persistent representations. Some current AI work is converging on this.

## Sources

- [Pezzulo, Cisek & Friston, 2024 — Generating meaning: active inference and the scope and limits of passive AI](https://en.wikipedia.org/wiki/Active_inference).
- [Hamrick, 2019 — Analogues of mental simulation and imagination in deep learning](https://en.wikipedia.org/wiki/Mental_imagery).
