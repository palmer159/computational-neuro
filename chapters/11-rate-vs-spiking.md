# Rate models vs spiking models

A computational neuroscientist's first methodological choice: model neurons as **firing rates** (continuous real numbers) or as **spike trains** (binary point processes in time)?

## Rate models

A neuron's state is a single real number $r(t) \in [0, r_{max}]$ representing instantaneous firing rate.

$$\tau \frac{dr_i}{dt} = -r_i + f\left(\sum_j w_{ij} r_j + I_i\right)$$

This is a **continuous-time RNN**. Set $\tau \to 0$ and you get a feedforward network with sigmoid/ReLU. **Every standard deep learning model is a rate model.**

When to use:
- You care about input-output mappings, not timing.
- You want to use ML toolchains.
- You're modeling cortex at the population level.

## Spiking models

Each neuron is a leaky integrator emitting binary spikes at threshold:

$$\tau \frac{dV_i}{dt} = -(V_i - V_{rest}) + R \sum_j w_{ij} \sum_k \delta(t - t_j^k) + I_i$$

When to use:
- You care about millisecond timing.
- You're modeling oscillations, synchrony, phase coding.
- You're targeting neuromorphic hardware (Loihi, SpiNNaker, TrueNorth).
- You're testing biologically-plausible learning rules where spike timing matters.

## What you lose by going to rates

- **Phase coding.** Information in spike phase relative to a population oscillation (theta, gamma).
- **Synchrony.** Coincidence detection in postsynaptic neurons.
- **Refractory dynamics.** Real ceilings on firing.
- **Energy realism.** Spikes are events; rates are continuous and don't model the energy budget.

## What you lose by going to spikes

- Differentiability. Surrogate-gradient methods help ([Neftci, Mostafa & Zenke, 2019](https://arxiv.org/abs/1901.09948)) but you're still off the GPU happy path.
- Tractability. 100k spiking neurons is hard; 100M rate units is a Tuesday.

## Population dynamics: a rate-model triumph

When a thousand neurons are recorded simultaneously, the population trajectory often lives on a low-dimensional manifold. Rate models in continuous-time recurrent form recover this beautifully.

📄 [Vyas, Golub, Sussillo & Shenoy, 2020 — Computation through neural population dynamics](https://en.wikipedia.org/wiki/Neural_coding). The modern paradigm: train an RNN to do the task, look at its hidden dynamics, compare to neural data. Often matches strikingly well.

**🤖 AI-relevance.** This is one of the most active fronts in NeuroAI. Trained RNN dynamics are being used as **explanatory models** of motor cortex, PFC, and even cognition. See [Sussillo & Barak, 2013](https://en.wikipedia.org/wiki/Recurrent_neural_network) and [Mante et al., 2013](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3923572/).

## A pragmatic table

| You want to... | Use |
|---|---|
| Match cognitive-task behavior | Rate RNN |
| Match millisecond ephys spike data | Spiking (LIF or GLM) |
| Run on neuromorphic hardware | Spiking |
| Train with backprop, large scale | Rate (or surrogate-gradient SNN) |
| Test biologically-plausible learning rules | Spiking |
| Probe representations / decoding | Either; rate is easier |

## Sources

- Dayan & Abbott chs 5–7.
- [Eliasmith & Anderson, 2003 — Neural Engineering](https://en.wikipedia.org/wiki/Neural_engineering) — rate-coded population approach (Nengo / SPA / Spaun).
- [Gerstner et al. — Neuronal Dynamics](https://neuronaldynamics.epfl.ch/) — spiking, free.
