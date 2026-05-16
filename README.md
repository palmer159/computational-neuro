# Neuroscience and AI - Understand basics of neuroscience concepts and relevance with AI

A study guide for anyone with AI knowledge who wants to understand the brain to understand the relevance of neuroscience concepts with AI and AGI, and begin to understand the neuro × AI boundary. This is not a deep neuroscience textbook or an AI textbook. Its simply to understand the relevance of the field of neuroscience with AI, and it assumes no prior knowledge of neuroscience. 

## Why this study guide
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
or choose to run a local web server using the instructions below. 

## Design notes

- **External-first**. Almost every paper, textbook, and dataset is linked to its public URL — Nature, Science, arXiv, PNAS, Neuron, Annual Reviews, Neuromatch, Allen Brain Atlas, etc. Nothing is downloaded that isn't strictly needed.
- **Markdown is rendered in the browser** via `marked.js` (CDN) and sanitized with `DOMPurify`. Mermaid diagrams render client-side. The server is dumb file-serving.
- **AI-relevance call-outs** in every chapter — what each idea means for AGI, LLMs, and current AI research.

## Suggested reading paths

| You have | Read |
|---|---|
| 1 weekend | Ch 01, 02, 09, 13, 18, 22, 25 |
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

- `manifest.json` — table of contents (5 parts, 28 chapters).
- `chapters/*.md` — one Markdown file per chapter.
- `index.html` — single-page app: client-side Markdown + Mermaid rendering, sidebar navigation, search.
- `server.py` — minimal local HTTP server (Python stdlib).


## Authoring

To add a chapter: drop `chapters/<id>.md` and add an entry to `manifest.json`.
