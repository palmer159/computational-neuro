# Backprop in the brain? Biologically plausible learning

The single deepest open question in neuroscience for AI: **how does the brain solve credit assignment?**

## Why backprop is biologically suspect

Backpropagation requires:

1. **Symmetric weights** — the backward pass uses $W^T$. Real synapses are unidirectional.
2. **Distinct phases** — forward pass, then backward. The brain runs continuously.
3. **Non-local error signals** — the gradient at any layer requires information from many layers downstream.
4. **Precise multiplication** — the chain rule multiplies derivatives of nonlinearities, requires fine-grained signed scalars.

None are obviously implementable in cortical hardware. Yet the brain clearly solves credit assignment for perception, motor learning, and language. **Something** does the work.

📄 [Lillicrap, Santoro, Marris, Akerman & Hinton, 2020 — Backpropagation and the brain](https://arxiv.org/abs/2004.13316). The status-of-the-field paper. Recommended.

> Lillicrap and co-authors lay out the central question: can the brain implement an algorithm functionally equivalent to backpropagation despite violating its three apparent prerequisites — symmetric weights, distinct forward/backward phases, and non-local error signals? They review candidate mechanisms (feedback alignment, equilibrium propagation, predictive coding, target propagation, dendritic burstprop, three-factor neuromodulated learning) and assess each against biological constraints and scalability evidence. They argue convergent results suggest cortex likely uses some approximation of gradient-based credit assignment built from local rules, with apical dendrites and neuromodulators carrying the necessary signals. The paper emphasizes that this is not a settled question but a tractable research frontier that matters both for explaining the brain and for designing neuromorphic hardware. It is the field's clearest single statement of the credit-assignment problem and the standard reference for anyone working at the boundary between biologically-plausible learning and modern deep learning.

## Candidate biologically plausible learning rules

### 1. Feedback alignment (and direct feedback alignment)

📄 [Lillicrap, Cownden, Tweed & Akerman, 2016 — Random synaptic feedback weights support error backpropagation for deep learning](https://arxiv.org/abs/1411.0247). Replace $W^T$ in the backward pass with **random fixed** weights $B$. The forward weights still align well enough during training to give learning. Works on small problems, struggles on big ones.

> Lillicrap and colleagues showed the surprising result that backpropagation does not require the backward pass to use the transpose of the forward weights — random fixed feedback weights work nearly as well on small problems. During training, the forward weights spontaneously evolve to "align" with the random feedback matrices in a way that delivers usable error signals, dissolving one of the strongest biological objections to backprop (the symmetric-weights problem). The mechanism, called "feedback alignment," provides a proof of concept that biologically plausible local rules can approximate gradient learning without architectural symmetry constraints. The result was an early breakthrough in the biologically-plausible-learning literature and inspired direct feedback alignment, sign-symmetric learning, and other variants. Subsequent work showed feedback alignment struggles on larger architectures like deep CNNs, motivating the more elaborate predictive-coding and burstprop alternatives that followed.

Removes the symmetric-weights problem. Doesn't fully scale.

### 2. Equilibrium propagation

📄 [Scellier & Bengio, 2017 — Equilibrium propagation: bridging the gap between energy-based models and backpropagation](https://www.frontiersin.org/articles/10.3389/fncom.2017.00024/full). An energy-based network with two phases (free, clamped). Local learning rule, no explicit gradients flowing backward. Provably equivalent to backprop in the limit.

### 3. Predictive coding networks

📄 [Whittington & Bogacz, 2017 — An approximation of the error backpropagation algorithm in a predictive coding network with local Hebbian synaptic plasticity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5467749/). A predictive-coding hierarchy with prediction-error neurons that, with local Hebbian updates, reproduces backprop arithmetic. Beautiful result.

> Whittington and Bogacz showed analytically that a hierarchical predictive-coding network with separate "value" and "error" neurons at each level, updated by purely local Hebbian-like rules, performs computations that closely approximate backpropagation. The key insight is that prediction errors propagated through the local network architecture serve the role of the gradient signals normally computed by backprop's chain rule. Every required computation reduces to neuron-local arithmetic, removing the symmetric-weight problem and the non-locality problem in one stroke. They demonstrated empirically that predictive-coding networks match backprop performance on standard supervised benchmarks while remaining biologically plausible. The paper is one of the cleanest mathematical results connecting cortex-style local learning to deep-learning gradient methods and a foundational reference for any biologically plausible scaling work.

📄 [Millidge, Tschantz & Buckley, 2022 — Predictive coding approximates backprop along arbitrary computation graphs](https://arxiv.org/abs/2202.09467). Generalizes the result.

**🤖 AI-relevance.** Predictive coding may be the **best current candidate** for "what cortex does that gives backprop-like learning." Increasingly relevant beyond neuroscience as a candidate replacement for backprop on neuromorphic hardware.

### 4. Burstprop / Dendritic learning

📄 [Payeur, Guerguiev, Zenke, Richards & Naud, 2021 — Burst-dependent synaptic plasticity can coordinate learning in hierarchical circuits](https://doi.org/10.1038/s41593-021-00857-x). Pyramidal neurons emit two distinct signals — single spikes (forward) and bursts (error). Apical and basal dendrites separate forward and feedback streams. A neurally grounded version of backprop credit assignment.

> Payeur and colleagues built a learning rule grounded in the empirical observation that cortical pyramidal neurons can emit either single spikes or high-frequency bursts, and that these two output modes carry distinct information. In their model, single spikes propagate the forward signal while bursts encode error or teaching signals, with apical dendrites receiving top-down feedback that triggers bursting based on prediction error. The framework cleanly separates forward and feedback streams onto different dendritic compartments of the same cell, removing the symmetric-weight problem while remaining anatomically plausible. The model trains deep cortical-like networks on benchmark tasks with performance approaching standard backprop, while every learning rule used is local and biologically realistic. It is one of the most physiologically grounded biologically plausible learning rules to date and a strong candidate for what cortex actually does.

### 5. Target propagation

📄 [Bengio, 2014; Lee, Zhang, Fischer & Bengio, 2015](https://arxiv.org/abs/1412.7525). Each layer learns to invert the next; targets propagate back instead of gradients. Local at each layer.

### 6. Three-factor / neuromodulated Hebbian learning

A global neuromodulator (dopamine, [ACh](https://en.wikipedia.org/wiki/Acetylcholine)) gates Hebbian learning. With eligibility traces, this implements approximate gradient methods.

📄 [Frémaux & Gerstner, 2016](https://www.frontiersin.org/articles/10.3389/fncir.2015.00085/full). Standard reference.

📄 [Roelfsema & Holtmaat, 2018 — Control of synaptic plasticity in deep cortical networks](https://doi.org/10.1038/nrn.2018.6). Argues attention + neuromodulation can coordinate deep credit assignment.

### 7. Hebbian / contrastive / self-supervised learning

If the brain is mostly self-supervised (predict next sensory input, predict masked pieces), then much of "credit assignment" reduces to local prediction error at each layer — no global backprop needed.

📄 [Konkle & Alvarez, 2022 — A self-supervised domain-general learning framework for human ventral stream representation](https://www.nature.com/articles/s41467-022-28091-4). Self-supervised models match IT representations as well as supervised ones. Important for plausibility — suggests cortex doesn't need the labels.

## What we don't know

- Whether the brain actually uses any of these.
- How effective these rules are at scale (most demonstrations are MNIST/CIFAR).
- Whether the brain uses different rules in different areas (likely).

## A pragmatic synthesis

Most working theorists currently bet on something like:

- Self-supervised local prediction at the layer level (predictive coding).
- Three-factor neuromodulated learning for reward-driven behavior.
- Hippocampus-mediated replay for offline consolidation.
- Apical dendrites carrying top-down signals.

None of this is settled. It is a top-tier research frontier.

## 🤖 AI-relevance summary

Two distinct AI motivations care about this:

1. **Understanding the brain to inspire [AGI](https://en.wikipedia.org/wiki/Artificial_general_intelligence).** If we can identify what credit-assignment principle the brain actually uses, it might be more sample-efficient or composable than backprop.
2. **Beyond-backprop AI for hardware reasons.** Neuromorphic chips, on-device learning, massive parallelism — all benefit from local rules. This is the practical engine driving plausibility research now.

## Sources

- [Whittington & Bogacz, 2019 — Theories of error back-propagation in the brain](https://arxiv.org/abs/1906.04937) — comprehensive review.
- [Richards et al., 2019 — A deep learning framework for neuroscience](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7115933/).
- [Pogodin et al., 2023](https://arxiv.org/abs/2305.14060) — local learning rule benchmarks at scale.
