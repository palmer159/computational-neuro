# Roads to [AGI](https://en.wikipedia.org/wiki/Artificial_general_intelligence) / [ASI](https://en.wikipedia.org/wiki/Superintelligence): what neuroscience suggests is missing

The synthesis chapter. We will look at the AGI gap table from Ch 01 row by row and ask what neuroscience suggests is needed to close it.

```
Capability gap                          What neuro suggests is needed
-----------------------------------------------------------------------------
Continual learning                      Synaptic consolidation + replay
Sample efficiency                       Strong inductive biases (cognitive maps,
                                        causal structure, theory of mind)
Energy efficiency                       Sparse coding, event-driven compute,
                                        local learning
Embodied causal interaction             Forward + inverse models, active inference
Long autobiography                      Hippocampus-cortex consolidation,
                                        episodic memory
Sleep & consolidation                   Offline replay, slow-wave generative
                                        regeneration of representations
Self-modeling / metacognition           Higher-order representations, attention
                                        schema
Goal genesis                            Hypothalamus, drives, homeostatic loops,
                                        intrinsic motivation
```

## Five honest claims about what's missing

### 1. Embodied agency, not just text

The brain's organizing problem is keeping a body alive in a hostile world. Cognition is in service of homeostasis (Damasio; Friston; LeDoux). LLMs are pure text predictors, lacking the homeostatic substrate that gives cognition its motivational shape.

**🤖 Implication.** Grounded multimodal agents with persistent state and consequences are the path forward. Robotics is the obvious instance, but virtual embodiment (long-running agents in software environments) might suffice.

### 2. Real long-term memory and consolidation

Hippocampus-style fast episodic memory + neocortex-style slow consolidation, with replay between them, is the only known continual-learning system in the universe.

**🤖 Implication.** Retrieval-augmented LLMs are step zero. Step one is generative replay during downtime that updates weights in the direction of consolidated knowledge. We don't have this yet at scale.

### 3. World models with causal structure

Brains do not just predict next state; they intervene, simulate counterfactuals, learn causal graphs. LLMs and image models do prediction but not counterfactual reasoning robustly. Cognitive science identifies this as a core gap (Lake et al., 2017; Pearl).

**🤖 Implication.** Causal world models are an underexplored frontier. Active learning + intervention is the natural training setup. Pure observational pretraining will plateau short of this.

### 4. Genuine metacognition

The brain models its own confidence, knows what it doesn't know, and distinguishes "I know" from "I'm guessing." LLMs are calibration-poor; hallucinations are calibration failures. Higher-order theories of consciousness (Ch 10) literally identify metacognition as the substrate.

**🤖 Implication.** Verifier-guided sampling, [RLHF](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) on calibration, self-consistency are first steps. The neural mechanism for metacognition is poorly understood — open frontier.

### 5. Goal genesis

Animals want things. They have drives that come from inside the system. Modern AI has no drives — only externally specified rewards. This is a fundamental architectural choice; whether AGI requires drives or whether good external scaffolding suffices is the most important unresolved alignment-relevant question.

**🤖 Implication.** Either we build systems with intrinsic drives (and inherit alignment problems brains have) or we figure out how to keep highly capable goal-less systems in service of human goals (corrigibility). The current frontier dodges this question; future systems may not be able to.

## Two big roads

### Road A — Scale + sloppy bio inspiration

Frontier labs' current bet. Ride the deep-learning paradigm. Add multimodality, long context, tool use, online learning incrementally. Fix gaps with engineering, not architecture.

If you believe **representations follow from objective + data + scale**, this works. The Yamins-style results (Ch 18) are the strongest argument it might.

### Road B — Architectural overhaul informed by neuroscience

LeCun-style, Bengio-style, partly DeepMind-style. Argue scaling alone cannot reach AGI; we need new architectures with hierarchical world models, predictive coding, persistent memory, agency.

If you believe **the missing capabilities require structure** (homeostasis, hippocampus, drives), this is the path.

These are not mutually exclusive. Most labs hedge.

## On ASI

Artificial superintelligence — systems substantially beyond human in general capability. Neuroscience has very little to say directly. What it says indirectly:

- **The 20-watt argument.** A human brain runs on 20W. If physics permits, vastly more capable systems might run on much more or much less, but a strong "brains are near optimal" claim is unsupported.
- **Architectural slack.** Brains are full of evolutionary kludges (recurrent laryngeal nerve, blind spot, the sleep imperative). Engineered systems should be able to do much better in many dimensions.
- **Plateau possibilities.** Some cognitive capacities (working memory ~4 items) may be architectural choices rather than physics-imposed. Engineered systems can blow past them.

## On alignment

Neuroscience-informed observations relevant to alignment:

- The brain's reward system is **hackable** and known to be hacked. Drug addiction is the existence proof of catastrophic reward hacking in a biological system. Alignment researchers should learn from how brains defend against this ([PFC](https://en.wikipedia.org/wiki/Prefrontal_cortex) inhibition, satiety, social context, long-horizon evaluation) and how those defenses fail.
- **Shard theory** in alignment ([Pope, 2022](https://www.lesswrong.com/posts/iCfdcxiyr2Kj8m8mT/the-shard-theory-of-human-values)) is roughly an attempt to extend [RL](https://en.wikipedia.org/wiki/Reinforcement_learning) + neuro models of human values to AI. Worth reading.
- **Embodied agency may be a feature, not a bug,** for alignment. A system without drives may be safer in some senses but harder to specify in others.

## What to actually read for AGI thinking

- [Lake, Ullman, Tenenbaum & Gershman, 2017 — Building machines that learn and think like people](https://arxiv.org/abs/1604.00289). The cognitive-science manifesto.

  > Lake and colleagues argue that even highly capable deep-learning systems differ from human cognition in ways that matter for general intelligence, particularly in sample efficiency, compositional generalization, and causal reasoning. They identify three core "ingredients" they claim are missing from current AI: rich internal models of physics and psychology that support intuitive theories, the ability to learn from very few examples by leveraging compositional structure, and the explicit handling of causal relationships through interventional and counterfactual reasoning. They contrast humans, who can learn new visual concepts from a single example by composing parts and relations, with neural networks that require millions of training examples and still fail to generalize systematically. The paper makes a strong case that scaling alone will not close these gaps and that progress requires building systems with structured priors and causal models. It functions as the cognitive-science manifesto for the AGI debate and is one of the five papers in the recommended "if you only read 5" list for this whole guide.
- [LeCun, 2022 — A path towards autonomous machine intelligence](https://openreview.net/pdf?id=BZ5a1r-kVsf). The architectural-overhaul manifesto.
- [Hassabis et al., 2017 — Neuroscience-Inspired AI](https://arxiv.org/abs/1709.05206). The DeepMind manifesto.
- [Bengio, 2017 — The consciousness prior](https://arxiv.org/abs/1709.08568). Workspace-flavored AGI proposal.

  > Bengio's "consciousness prior" proposes that the conscious state at any moment is a low-dimensional, sparse projection of the much higher-dimensional unconscious state of the brain — and that this bottleneck is where high-level abstractions and verbalizable thought live. The proposal is explicitly inspired by Global Workspace Theory: a small workspace receives information from many specialist modules and selectively broadcasts a sparse summary back. Bengio formalizes this as an inductive bias for neural networks: enforce a low-dimensional bottleneck that produces interpretable, manipulable, factored representations. He argues such priors are necessary for systematic generalization, planning, language use, and out-of-distribution reasoning — capabilities standard deep nets struggle with. The piece is the workspace-flavored AGI manifesto and has motivated a substantial line of subsequent work on attention bottlenecks and structured representations in deep learning.
- [Doerig et al., 2023 — Neuroconnectionist research programme](https://arxiv.org/abs/2209.03718).

  > Doerig and a large multi-author team articulate the "neuroconnectionist research programme" — the position that trained ANNs are now legitimate scientific models of the brain, not just engineering artifacts. They survey the methodology, successes (vision, language, motor cortex), and methodological limits (prediction does not entail mechanistic explanation, model-data correlations can be spurious without causal experiments). They argue the field has matured into a distinct research programme with its own standards, techniques, and unresolved questions. The paper functions as the field's contemporary self-portrait and methodological manifesto. It is essential reading for anyone evaluating claims that a particular ANN "matches" or "explains" a given brain region, and provides the conceptual scaffolding for distinguishing strong from weak versions of those claims.
- [Mitchell — Artificial Intelligence: A Guide for Thinking Humans (book, 2019)](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Guide_for_Thinking_Humans) — most balanced popular treatment.

## Practical research stance

If you are choosing what to work on at a tech company in 2026:

1. Embodied / multimodal agents with persistent state are systematically under-served and likely high-leverage.
2. Continual learning + targeted replay is real, hard, important, and there is a plausible neural blueprint.
3. World models + causal counterfactual reasoning are an under-built primitive.
4. Mechanistic interpretability is borrowing more from neuroscience than vice-versa right now; the methodology transfer is huge.
5. Anything you build that pretends "neuroscience-inspired" without engaging the actual literature will be embarrassed by people who do.
