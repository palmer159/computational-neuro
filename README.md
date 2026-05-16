# Neuroscience & Computational Neuroscience for AI Researchers

A study guide for post-graduate computer science majors with no prior neuroscience background, written for someone who wants to understand the brain well enough to read NeuroAI papers, form an informed view on AGI, and work productively at the neuro × AI boundary.

## Run it

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

## Authoring

To add a chapter: drop `chapters/<id>.md` and add an entry to `manifest.json`.
