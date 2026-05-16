# Neuroscience and AI - Understand basics of neuroscience concepts and relevance with AI

A study guide for anyone with AI knowledge who wants to understand the key concepts of neuroscience along with its relevance with AI, and begin to understand the neuro × AI boundary. This is not a deep neuroscience textbook or an AI textbook. Its simply to understand the relevance of the field of neuroscience with AI, and it assumes no prior knowledge of neuroscience. 

## Why understand the brain for AI?
The brain is the only existence proof of general intelligence we have. It runs on a mere ~20 watts whereas AI needs several Megawatts of power! It learns from a handful of examples, generalizes out of distribution, and stays coherent for ~80 years. Modern LLMs match or exceed it on narrow tasks while burning megawatts and hallucinating their own training data. Whatever the brain is doing, we have not reproduced it, even if we have surpassed it in places.

That is the case for caring about neuroscience. The case for not over-caring is that we may build AGI without ever resolving how cortex works. Take from neuroscience what is computationally clarifying; don't be religious about biological plausibility.

The most productive AI researchers in this space (DeepMind, Numenta, MIT BCS, Stanford, the Mila / Bengio crowd) treat neuroscience as a **source of inductive biases and existence proofs**, not as a target to reverse-engineer. 

## Why this study guide
Neuroscience has made fundamental contributions to advancing AI research. The past contributions of neuroscience to AI have rarely involved a simple transfer of full-fledged solutions that could be directly re-implemented in machines. Rather, neuroscience has typically been useful in a subtler way, stimulating algorithmic-level questions about facets of human learning and intelligence of interest to AI researchers and providing initial leads toward relevant mechanisms. 

Every chapter here is a summary of key neuroscience concepts for a beginner, with a description of its relevance or divergence with AI concepts
Everything here is summarized from authoritative open articles and reputed research papers, with links to the papers for detailed study.

## Who this is for

You are someone who understands the basics of machine learning, deep learning, and AI. You know **zero neuroscience**. You want to understand the brain well enough to:
- relate neuroscience concepts with AI
- read neuro-inspired AI papers (predictive coding, world models, Hopfield nets, SNNs) without bluffing,
- form your own view on what AGI/ASI is missing,

This is **not** a neuroscience textbook. It is a high-velocity bridge from Computer science into the parts of neuro that matter for AI research. This guide is a curated list of articles with links to relevant research papers without a paywall. 

## How to read
You can browse the entire guide right here on git https://github.com/palmer159/computational-neuro/tree/main/chapters, 
or choose to run a local web server using the instructions below (some architecture or illustrations will render better). 

## Design notes

- **External-first**. Almost every paper, textbook, and dataset is linked to its public URL — Nature, Science, arXiv, PNAS, Neuron, Annual Reviews, Neuromatch, Allen Brain Atlas, etc. Nothing is downloaded that isn't strictly needed.
- **Markdown is rendered in the browser** via `marked.js` (CDN) and sanitized with `DOMPurify`. Mermaid diagrams render client-side. The server is dumb file-serving.
- **AI-relevance call-outs** in every chapter — what each idea means for AGI, LLMs, and current AI research.

## Suggested reading paths

| You have | Read |
|---|---|
| 1 weekend | Ch 01, 02a, 02b, 02c, 09, 13, 18, 22, 25 |
| 2 weeks | Part II + Part IV |
| 1 quarter | All of it, in order |
| LLM-only | Ch 13, 14, 18, 22, 23, 25 |


## Run the web server to load the content if you dont want to browse on git

```bash
python3 server.py
# then open http://127.0.0.1:8765/
```

Stdlib only. No build step. No installs.

## What's here

- `manifest.json` — table of contents (5 parts, 31 chapters).
- `chapters/*.md` — one Markdown file per chapter.
- `index.html` — single-page app: client-side Markdown + Mermaid rendering, sidebar navigation, search.
- `server.py` — minimal local HTTP server (Python stdlib).


## Authoring

To add a chapter: drop `chapters/<id>.md` and add an entry to `manifest.json`.
