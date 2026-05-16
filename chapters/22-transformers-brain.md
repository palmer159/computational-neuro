# Transformers, attention & the brain

## The interesting question

Transformers are the dominant architecture in AI. They are also conspicuously **not** the canonical neural-network architecture. No biological neuron does softmax over a thousand keys. So:

- Are transformers brain-like in any deep sense?
- Or did we find a non-biological architecture that beats biology at biology's own job?

Both stances are honestly defended in the literature. You should be able to articulate both.

## Where transformers and brains converge

### 1. Attention as biased competition

Already noted in Ch 08. Soft attention — query-driven competition resolved by softmax — is a clean implementation of biased competition (Desimone & Duncan 1995). Cortical attention biases competing representations toward the goal-relevant one. Transformer attention biases competing tokens toward the query.

### 2. Modern Hopfield networks

📄 [Ramsauer et al., 2020 — Hopfield Networks is All You Need](https://arxiv.org/abs/2008.02217). Showed softmax attention is exactly equivalent to a continuous (modern) Hopfield network. Hopfield networks are 1980s biological neural-network classics.

So: transformer attention has a clean reading as **content-addressable associative memory**. That is a textbook hippocampus operation.

### 3. LMs predict language cortex

📄 [Schrimpf et al., 2021](https://www.pnas.org/doi/10.1073/pnas.2105646118) and [Goldstein et al., 2022](https://en.wikipedia.org/wiki/Language_model). Transformer LM activations linearly predict cortical language responses, and the better the LM at next-word prediction, the better at brain prediction. Whatever language cortex is doing, it is in the same representational neighborhood as a transformer LM.

### 4. In-context learning ≈ meta-RL

The mapping in Ch 20: PFC + DA implements meta-RL where slow synaptic changes train fast in-activation learners. LLM in-context learning has the same shape — slow pretraining produces a system that does fast adaptation in activations during inference. If meta-RL is right about PFC, LLMs do something computationally adjacent.

📄 [von Oswald et al., 2022 — Transformers learn in-context by gradient descent](https://arxiv.org/abs/2212.07677). One mechanistic account.

### 5. Positional encodings ≈ entorhinal grid codes?

Speculative. Both impose a sinusoidal/Fourier-like structural prior on a learned space. [Whittington et al., 2022 — Relating transformers to models and neural representations of the hippocampal formation](https://arxiv.org/abs/2112.04035) makes this case explicitly: a transformer with a particular positional encoding maps to the Tolman-Eichenbaum Machine (Ch 16).

## Where transformers and brains diverge

- **No recurrence** at the architectural level (in standard transformers). Brains are massively recurrent.
- **Global attention** over all positions in a context window. Cortex has no obvious analog of "every neuron attends to every other neuron."
- **One-shot decoding** of every position in parallel. Cortex is causal, sequential, with continuous dynamics.
- **Massive parameter counts** in dense layers. Cortex is highly sparse (each cortical neuron synapses with maybe 10⁴ others out of 10¹¹).
- **Phase-free** computation. No gamma rhythm, no theta, no replay.
- **No homeostasis.** Transformers do not regulate their own state.

## A defensible synthesis

The transformer's **attention operation** has plausible biological readings (biased competition, Hopfield-style memory). The transformer's **architecture** does not. Pretraining on next-token prediction produces representations that linearly align with language cortex, but this is a strong **representational** convergence with weaker mechanistic implications.

The interesting question for AI: which **inductive biases** of cortex (recurrence, sparsity, top-down feedback, local learning, neuromodulation) might improve transformers if added back? Some early answers:

- Recurrence improves brain prediction in vision ([Kar et al., 2019](https://en.wikipedia.org/wiki/Recurrent_neural_network)) and offers iterative refinement at inference ([RNN-augmented LLMs](https://arxiv.org/abs/2402.11651)).
- Sparsity (mixture-of-experts) gives capacity per FLOP.
- Top-down feedback in iterative diffusion models loosely resembles predictive coding.

## Worth keeping an eye on

- **State space models / Mamba** ([Gu & Dao, 2023](https://arxiv.org/abs/2312.00752)) — recurrent, state-tracking, more cortical-feeling than transformers.
- **Hyena, RWKV, RetNet** — alternative attention-replacements with closer biological analogs.
- **Diffusion models** — iterative refinement, energy-based, predictive-coding-flavored.
- **Memory-augmented transformers** — explicit hippocampus-like memory ([MEMIT](https://memit.baulab.info/), [MemGPT](https://memgpt.ai/), [Titans](https://arxiv.org/abs/2501.00663)).

## Sources

- [Whittington et al., 2022](https://arxiv.org/abs/2112.04035).
- [Olah, 2024 — circuits.transformer-circuits.pub](https://transformer-circuits.pub/) — Anthropic's mechanistic interpretability of transformers; surprisingly neuroscience-flavored.
- [Kanwisher, Khosla & Dobs, 2023 — Using artificial neural networks to ask 'why' questions of minds and brains](https://en.wikipedia.org/wiki/Nancy_Kanwisher).
