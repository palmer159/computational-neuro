# Neural dynamics: attractors, oscillations, criticality

Most ML models are stateless functions: $y = f(x)$. Brains are dynamical systems: $\dot{x} = F(x, u)$. The dynamics carry information.

## Attractor dynamics

A trained recurrent network's hidden state often settles into stereotyped trajectories — fixed points, limit cycles, or low-dimensional manifolds. These are **attractors**. Three flavors used in computational neuroscience:

| Type | Function | Example |
|---|---|---|
| **Point attractor** | Discrete memory, decision | Working memory, decision threshold |
| **Line / ring attractor** | Continuous variable | Head direction, oculomotor integrator |
| **Manifold attractor** | Multi-D continuous | Place fields, motor command |

📄 [Khona & Fiete, 2022 — Attractor and integrator networks in the brain](https://arxiv.org/abs/2112.03978). The modern review.

> Khona and Fiete review attractor networks across the brain, taxonomizing them by their geometry — point attractors for discrete decisions, ring attractors for continuous variables like head direction, line and plane attractors for working memory, and high-dimensional manifold attractors for spatial coding. They synthesize evidence that these dynamical structures are pervasive in the brain and provide a robust substrate for memory, navigation, and decision-making. The review connects classical Hopfield-style theory to modern recordings, showing how trained recurrent networks recover similar dynamics from task pressure alone. They argue attractor dynamics are a general computational primitive that the brain reuses across systems, with parallels in modern AI like content-addressable memory and stable representations in trained RNNs. The paper is the standard contemporary reference on attractor dynamics in neuroscience and bridges to AI through both Hopfield-style energy models and RNN dynamics analysis.

### Hopfield networks

📄 [Hopfield, 1982 — Neural networks and physical systems with emergent collective computational abilities](https://www.pnas.org/doi/10.1073/pnas.79.8.2554). A symmetric recurrent network with binary or rate units that stores patterns as fixed points. Energy-based, content-addressable.

> Hopfield introduced a symmetric recurrent network of binary neurons whose dynamics are governed by an energy function that descends monotonically to local minima. The minima of this energy landscape correspond to memorized patterns, making the network a content-addressable associative memory: present a partial or noisy cue and the dynamics complete it by relaxing to the nearest stored pattern. This was the first widely-used connection between statistical physics — specifically the Ising model — and neural computation, providing a clean mathematical framework for collective neural behavior. The network demonstrated that distributed, parallel, noise-tolerant memory could emerge from simple symmetric synaptic interactions, validating a key intuition about how brains might store information. Forty years later, modern Hopfield networks were shown to be mathematically equivalent to the softmax attention operation in transformers, retroactively making this 1982 paper a foundational reference for understanding the most important architecture in modern AI.

📄 [Ramsauer et al., 2020 — Hopfield Networks is All You Need](https://arxiv.org/abs/2008.02217). Showed that softmax attention is mathematically equivalent to a continuous (modern) Hopfield network. Hugely consequential — a 1982 neural-net idea is one mathematical reframing of the transformer's core operation.

> Ramsauer and colleagues prove that softmax attention — the central operation of the transformer — is mathematically equivalent to a single update step of a continuous-state ("modern") Hopfield network. They generalize the classical binary Hopfield model to continuous patterns and show this generalization has exponentially larger storage capacity, making it a viable content-addressable memory at the scale of modern AI systems. The equivalence reframes attention as content-addressable associative retrieval: queries fetch values weighted by similarity to keys, exactly as a Hopfield network completes patterns from partial cues. This retroactively grounds one of the most important architectural innovations in modern AI in 1980s biological neural-network theory and provides a clean energy-based reading of what attention does. It also opens design space for "Hopfield layers" as drop-in associative memory modules and gives transformers a biologically plausible interpretation as iterative attractor dynamics rather than opaque parallel attention.

**🤖 AI-relevance.** This is a strong rebuttal to "transformers are non-biological." The attention operation has a clean energy-based, attractor-network reading. Whether the brain uses it that way is open; the math doesn't care.

### Decision-making as a 2-attractor network

📄 [Wang, 2002 — Probabilistic decision making by slow reverberation in cortical circuits](https://doi.org/10.1016/S0896-6273(02)01092-9). A 2-attractor network with [NMDA](https://en.wikipedia.org/wiki/NMDA_receptor)-driven slow reverberation reproduces psychophysical data on perceptual decision-making (and the famous LIP neuron ramp-up data of Shadlen and Newsome).

> Wang built a recurrent cortical network with two competing populations connected by lateral inhibition and stabilized by slow NMDA-dependent reverberation. The network's dynamics implement a noisy attractor competition that integrates ambiguous sensory evidence over hundreds of milliseconds before committing to one of two choices. The model quantitatively reproduced classic LIP-neuron ramp-up data from Shadlen and Newsome's monkey experiments, including the dependence of decision time on stimulus difficulty and the trial-by-trial variability of choice. NMDA's slow time constants turned out to be essential: faster excitation produces premature decisions, while NMDA matches the observed integration timescales. The paper is the canonical computational model of perceptual decision-making and links psychophysics, single-neuron physiology, and recurrent network theory in a single concrete circuit, providing the cleanest worked example of attractor dynamics implementing cognition.

## Oscillations: the brain's rhythms

| Band | Frequency | Where / when |
|---|---|---|
| Delta | 0.5–4 Hz | Slow-wave sleep |
| Theta | 4–8 Hz | Hippocampus during exploration & [REM](https://en.wikipedia.org/wiki/Rapid_eye_movement_sleep) |
| Alpha | 8–13 Hz | Eyes-closed cortex |
| Beta | 13–30 Hz | Motor preparation |
| Gamma | 30–100 Hz | Local cortical processing, attention |
| Ripple | 150–250 Hz | Hippocampal replay |

📄 [Buzsáki, 2006 — Rhythms of the Brain (book)](https://en.wikipedia.org/wiki/Gy%C3%B6rgy_Buzs%C3%A1ki). Required reading.
📄 [Fries, 2015 — Rhythms for Cognition: Communication through Coherence](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5117586/). Argues phase locking gates communication between areas.

**🤖 AI-relevance.** ML mostly ignores temporal rhythms. Two ways this might matter:
- **Routing.** Phase coherence as a dynamic routing mechanism — brains may switch what talks to what on the fly via gamma synchrony. ML uses static routing in MoE; phase-style dynamic routing is a less explored design.
- **Coordination.** Theta-gamma coupling carries hierarchical structure. Worth keeping in your design space.

## Criticality

A claim from physics-of-cortex: cortical activity hovers near a phase transition between order and chaos, where information processing capacity is maximized.

📄 [Beggs & Plenz, 2003 — Neuronal Avalanches in Neocortical Circuits](https://www.jneurosci.org/content/23/35/11167). Empirical signature: spike avalanches with power-law size distributions.
📄 [Wilting & Priesemann, 2018](https://www.nature.com/articles/s41467-018-04725-4) — pushes back, says cortex is **subcritical**, not critical.

**🤖 AI-relevance.** [RNN](https://en.wikipedia.org/wiki/Recurrent_neural_network) training is sometimes pictured as targeting an "edge of chaos" regime. Mostly metaphor in ML; mostly metaphor in neuro too. Be skeptical.

## Excitation-inhibition balance

A robust empirical finding: cortical networks are tuned so that excitatory and inhibitory inputs onto each neuron are balanced moment by moment. The result: irregular Poisson-like firing, fast responses, dynamic gain control.

📄 [van Vreeswijk & Sompolinsky, 1996 — Chaos in neuronal networks with balanced excitatory and inhibitory activity](https://doi.org/10.1126/science.274.5293.1724).

**🤖 AI-relevance.** The "balanced amplification" regime predicts irregular asynchronous firing matching cortex; informs how to initialize and tune RNNs that aim to be brain-like. See [Murray et al., 2017](https://doi.org/10.1038/s41586-018-0202-3) for the modern follow-on.

## Sources

- Dayan & Abbott chs 7–8.
- [Sussillo & Barak, 2013 — Opening the black box: low-dimensional dynamics in high-dimensional recurrent neural networks](https://doi.org/10.1162/NECO_a_00409) — best methodological intro to analyzing trained RNNs as dynamical systems.
