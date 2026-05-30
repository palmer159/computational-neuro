# Neuro-inspired architectures: SNNs, neuromorphic, Hopfield, predictive nets

A practical tour of architectures that visibly take from neuroscience. None is currently the dominant paradigm in commercial AI; most are alive in research and in neuromorphic hardware.

## Spiking neural networks (SNNs)

Discrete, event-driven networks of spiking neurons ([LIF](https://en.wikipedia.org/wiki/Biological_neuron_model) or Izhikevich). Bring in:

- Temporal coding.
- Sparse activations (only spikes consume energy).
- Neuromorphic hardware compatibility.

**Training.** Three approaches:
1. **Convert [ANN](https://en.wikipedia.org/wiki/Artificial_neural_network) → [SNN](https://en.wikipedia.org/wiki/Spiking_neural_network).** Train a rate model, replace [ReLU](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)) with rate-coded spiking neuron. Works for vision, struggles for time-extended tasks.
2. **Surrogate gradient.** Replace the non-differentiable spike with a smooth surrogate at backward pass. ([Neftci, Mostafa & Zenke, 2019](https://arxiv.org/abs/1901.09948)).
3. **Local rules** ([STDP](https://en.wikipedia.org/wiki/Spike-timing-dependent_plasticity), three-factor). Less effective at scale, more biologically plausible.

**Hardware.**
- **Intel Loihi 2** — 1M neurons per chip, on-chip learning. [docs](https://en.wikipedia.org/wiki/Cognitive_computer).
- **IBM TrueNorth, NorthPole** — research chips ([Modha et al., 2023](https://doi.org/10.1126/science.adh1174)).
- **SpiNNaker 2** — Manchester, ARM-based. [SpiNNaker](https://apt.cs.manchester.ac.uk/projects/SpiNNaker/).
- **BrainScaleS** — analog accelerated emulation.

**🤖 AI-relevance.** SNNs are the only architecture currently practical on neuromorphic hardware, which is the only practical route to **kHz-rate, milliwatt** edge AI. Don't expect SNNs to win in cloud training; do expect them in robotics, embedded, prosthetics.

## Hopfield networks (modern)

📄 [Ramsauer et al., 2020](https://arxiv.org/abs/2008.02217) — already cited. Modern Hopfield = softmax attention with massive storage capacity. Can be a layer in a deep net (`HopfieldLayers`).

📄 [Hoover et al., 2023 — Energy transformer](https://arxiv.org/abs/2302.07253). Energy-based transformers from Hopfield principles.

**🤖 AI-relevance.** Hopfield-style associative memories are a clean drop-in for content-addressable memory in transformer architectures.

## Predictive coding networks (PCNs)

Biologically plausible alternatives to backprop discussed in Ch 19. Recent results show PCNs can train modern architectures with local rules:

📄 [Salvatori et al., 2023 — Brain-inspired predictive coding networks](https://arxiv.org/abs/2308.07870).
📄 [Millidge et al., 2024 — Predictive coding networks: an overview](https://arxiv.org/abs/2407.04117).

Practical use cases: neuromorphic hardware, on-device continual learning, energy-efficient training.

## Capsule networks

📄 [Sabour, Frosst & Hinton, 2017 — Dynamic routing between capsules](https://arxiv.org/abs/1710.09829). Hinton's attempt at viewpoint-invariant, parts-and-wholes-aware vision. Loose biological inspiration (cortical microcolumns, viewpoint reference frames). Has not displaced CNNs; lives on in occasional follow-ups.

> Sabour, Frosst, and Hinton introduced capsule networks, in which groups of neurons ("capsules") jointly encode the presence, pose, and viewpoint of visual entities, with dynamic routing-by-agreement determining which lower-level capsules contribute to which higher-level capsules. The architecture was inspired by Hinton's long-standing argument that vision must explicitly represent part-whole hierarchies and viewpoint reference frames, drawing loose analogy to cortical columns and the parts-and-wholes structure of cortex. CapsNets achieved competitive performance on small benchmarks while showing better viewpoint generalization than CNNs of similar size. The architecture has not displaced convolutional or transformer-based vision systems, but variants and follow-ups have continued to explore part-based representations. The paper remains an important worked example of biology-inspired architectural design, even if the empirical case for capsules at scale has not materialized.

## Liquid neural networks / continuous-time

📄 [Hasani et al., 2021 — Liquid time-constant networks](https://arxiv.org/abs/2006.04439). Continuous-time [RNN](https://en.wikipedia.org/wiki/Recurrent_neural_network) with input-dependent time constants — closer to biophysics. Works well on small robotics tasks.

> Hasani and colleagues introduced Liquid Time-constant (LTC) networks, continuous-time recurrent networks in which each neuron's time constant depends on its input, mirroring how biological neurons modulate their integration timescales based on synaptic activity. The architecture is closer to biophysical neuron models than standard RNNs, with dynamics governed by a system of nonlinear ordinary differential equations rather than discrete updates. The networks proved compact and expressive on small robotics control tasks — outperforming much larger LSTMs and transformers on autonomous driving with as few as nineteen neurons. They are also relatively interpretable because each neuron has explicit dynamics that can be analyzed mathematically. The paper is one of the most successful recent examples of biophysics-inspired architecture and has driven renewed interest in continuous-time neural networks for embedded and edge applications.

## Hierarchical Temporal Memory (Numenta)

Jeff Hawkins' research. Cortical-microcolumn-inspired sparse distributed representations + temporal sequence learning. Strong claims ("a thousand brains"); modest empirical track record. Worth knowing about; don't bet on it in production.

## Reservoir computing / echo state networks

A fixed random recurrent network with trained linear readout. Cheap; sometimes competitive on small dynamical tasks. Loosely cortex-flavored (random dynamics + readout).

📄 [Jaeger, 2001 — The "echo state" approach to analysing and training recurrent neural networks](https://www.ai.rug.nl/minds/uploads/EchoStatesTechRep.pdf).

## State-space models — adjacent if not neuro-inspired

Mamba, S4, S5, RWKV are recurrent linear-time architectures with strong sequence performance. They are not explicitly neuro-inspired, but they recover several brain-like properties (recurrence, selectivity, content-addressable state-update). Increasingly compared to cortex in recent papers.

## What "neuro-inspired" really buys you

Honest summary:

| Property | Neuro-inspired arch helps? |
|---|---|
| Energy efficiency at edge | Yes — SNNs on neuromorphic |
| Fast online learning | Some — local rules, three-factor |
| Long-term retention | Yes — Hopfield-style memory |
| Continual learning | Sometimes |
| Standard benchmarks | No — transformers + scaling still wins |
| Explanatory traction in cognitive science | Yes — predictive coding, attractor networks |

Don't expect neuro-inspired architectures to beat transformers at [LLM](https://en.wikipedia.org/wiki/Large_language_model) benchmarks any time soon. Do expect them to matter for embodied, on-device, energy-constrained, or scientifically-motivated work.

## Sources

- [Tavanaei et al., 2019 — Deep learning in spiking neural networks](https://arxiv.org/abs/1804.08150).
- [Pfeiffer & Pfeil, 2018 — Deep learning with spiking neurons: opportunities & challenges](https://www.frontiersin.org/articles/10.3389/fnins.2018.00774/full).
- [Davies et al., 2021 — Advancing neuromorphic computing with Loihi](https://doi.org/10.3389/fnins.2021.617527).
