# Motor systems & action selection

## The motor stack

```mermaid
flowchart TD
    PFC[PFC: goals] --> PMC[Premotor: plans]
    PMC --> M1[M1: commands]
    M1 --> SC[Spinal cord]
    SC --> Muscles
    M1 -.efference copy.-> Cb[Cerebellum: forward model]
    BG[Basal ganglia: select / gate] --> PMC
    Cb -.error.-> M1
```

## Five things to remember

1. **Motor cortex is somatotopic** — hand area, leg area, etc. Same homunculus as S1.
2. **The cerebellum is a forward model.** It predicts the sensory consequences of motor commands and computes errors. Deeply analogous to model-based RL.
3. **Basal ganglia gate actions.** They select among competing plans via direct (Go) and indirect (No-Go) pathways modulated by dopamine.
4. **Spinal cord is not dumb.** Central pattern generators (CPGs) produce rhythmic locomotion without cortical input.
5. **Mirror neurons** in premotor cortex fire both when you act and when you watch someone else act ([Rizzolatti & Sinigaglia, 2010](https://en.wikipedia.org/wiki/Mirror_neuron)). Hyped, but real.

## The cerebellum as a learning machine

📄 [Marr, 1969 — A theory of cerebellar cortex](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1351747/). The cerebellum has ~80% of the brain's neurons (granule cells), each receiving sparse, high-dimensional inputs. Marr proposed it learns supervised input-output mappings — and he was largely right. Climbing fibers from the inferior olive carry **error signals** that drive LTD at parallel-fiber → Purkinje synapses.

Modern view: the cerebellum is a generic supervised learner used for motor control, timing, and (controversially) cognitive prediction.

**🤖 AI-relevance.** The cerebellum is a real, biological, three-layer feedforward network with a teacher signal. Closer to a textbook ANN than cortex is. See [Raymond & Medina, 2018](https://en.wikipedia.org/wiki/Cerebellum#Theories_of_function).

## The basal ganglia as RL

The basal ganglia (striatum, GP, STN, SNc) implement **action selection via reinforcement learning**. Phasic dopamine from the substantia nigra and VTA delivers a TD-style reward prediction error to striatal medium spiny neurons. We will return to this in detail in Ch 09 and Ch 20.

Key reading: [Doya, 2000 — Complementary roles of basal ganglia and cerebellum in learning and motor control](https://en.wikipedia.org/wiki/Basal_ganglia#Theories_of_function) — argues cerebellum = supervised, basal ganglia = RL, cortex = unsupervised. A strong organizing hypothesis even if oversimple.

## Forward, inverse, and internal models

- **Forward model.** Given action a and state s, predict next state s'. Implemented (largely) in cerebellum.
- **Inverse model.** Given desired s', compute action a. Implemented in motor cortex + basal ganglia + spinal cord.
- **Internal model** in general: the brain simulates outcomes before acting.

📄 [Wolpert, Ghahramani & Jordan, 1995 — An internal model for sensorimotor integration](https://en.wikipedia.org/wiki/Internal_model_(motor_control)). Foundational.

**🤖 AI-relevance.** Model-based RL, Dreamer, Muzero, world-models — these are inverse and forward models. The brain version emphasizes (a) very fast learning, (b) tight coupling to control, (c) modularity per body part.

## Sources

- Kandel ch 33–37.
- [Shadmehr & Krakauer, 2008 — A computational neuroanatomy for motor control](https://en.wikipedia.org/wiki/Motor_control) — bridges nicely to control theory.
