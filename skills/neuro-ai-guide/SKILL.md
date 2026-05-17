---
name: neuro-ai-guide
description: Generate the latest "Neuroscience and Computational Neuroscience for AI Researchers" study guide locally — clone the canonical repo, optionally re-verify every external link against Unpaywall/Crossref so paywalled or dead citations are auto-replaced with verified open-access copies, and serve via a stdlib HTTP server. Use when the user asks to "generate the neuroscience study guide", "build the neuro-AI study guide", "set up the comp-neuro guide", "give me the latest neuro × AI guide", or any phrasing that points to the palmer159/computational-neuro study guide.
---

# neuro-ai-guide

This skill regenerates the **palmer159/computational-neuro** study guide on the user's machine. It always pulls the latest content from `main` and (optionally) re-verifies every external citation, so the guide a user sees today reflects the latest chapters and the latest live state of every linked paper.

## When to use

Trigger when the user asks for any of:

- "generate the neuroscience study guide"
- "build / create / install / set up the neuro × AI guide"
- "give me the latest comp-neuro for AI researchers guide"
- "regenerate the palmer159 study guide"
- "spin up the neuroscience-for-AI tutorial site"

If unsure, ask one clarifying question.

## What it does

1. **Clones or updates** `https://github.com/palmer159/computational-neuro` into a target directory (default: `~/computational-neuro`). On re-runs, fast-forwards `main`.
2. **Optionally re-verifies** every external URL across all chapters using a local Python checker that:
   - HEAD/GET-tests each URL
   - For DOI URLs that resolve to a paywall, queries Unpaywall (free OA-locator) and substitutes the OA copy when available
   - Reports paywalled / dead links and writes a `link_audit.json` next to the chapters
3. **Serves the SPA locally** via the bundled `server.py` (Python stdlib, no installs).

Output is a fully working local copy at `http://127.0.0.1:8765/` plus the underlying markdown for offline reading.

## Prerequisites

- `git` (for clone/pull)
- `python3` ≥ 3.8 (stdlib only — no pip installs required)

The skill checks for both at the start and surfaces a clear error if either is missing.

## How to run

Steps for the assistant to execute when this skill fires:

### Step 1 — preflight

Run `scripts/preflight.sh` to verify `git` and `python3` are present and to capture the current Git config so we don't accidentally rewrite the user's identity.

### Step 2 — generate

Run `scripts/generate.sh [TARGET_DIR]`. Default target is `~/computational-neuro`. The script:

- Clones the repo if missing, else `git fetch && git pull --ff-only origin main`
- Prints the latest commit hash and `manifest.json` chapter count

### Step 3 — re-verify links (optional but recommended)

Run `python3 scripts/verify_links.py <TARGET_DIR>`. The script:

- Walks every `chapters/*.md` file
- Extracts every external URL
- Reachability-checks each
- For DOI URLs, queries `api.unpaywall.org` and upgrades to OA when a free copy exists
- Writes `link_audit.json` with `{ok: [], dead: [], replaced: []}`
- Optionally rewrites the markdown (`--apply` flag) so paywalled DOIs are replaced with verified OA URLs in-place

This is the step that makes the output reflect the *current* live state of the web rather than what was correct at last commit.

### Step 4 — serve

Run `scripts/serve.sh [PORT]` (default 8765). Tells the user the URL to open. Backgrounds the process and shows how to stop it.

## Important rules for the assistant

1. **Never rewrite the user's git identity.** The repo is read-only from this skill's perspective. If the target dir already has a checkout with a different identity, leave it alone.
2. **No pip installs.** All scripts use only the Python standard library. If a dependency would be useful, write the code without it.
3. **Be transparent about link-verification trade-offs.** Several authoritative open-access publishers (PNAS, JNeurosci, bioRxiv, cell.com, science.org) Cloudflare-block scripted requests. The verifier flags these as "bot-blocked, OK for human readers" — not as dead. Tell the user this when summarizing.
4. **Honor user-provided target directory.** If the user names a directory, use that; otherwise default to `~/computational-neuro` (the skill scripts handle this).
5. **Do not regenerate chapter content from scratch.** This skill *fetches* the canonical chapters from the upstream repo. If the user asks to *edit* the guide, point them at the upstream repo workflow (clone, edit, PR) — generation is for consumers, not authors.

## What the user gets

After successful run:

```
~/computational-neuro/
├── README.md
├── manifest.json
├── index.html
├── server.py
├── chapters/
│   ├── 00-how-to-use.md
│   ├── 01-why-neuroscience-for-ai.md
│   ├── 02a-brain-overview.md
│   └── ... (28 more)
├── link_audit.json   ← fresh audit, only if step 3 ran
└── skills/neuro-ai-guide/   ← this skill itself
```

A local server at `http://127.0.0.1:8765/` serves the SPA with sidebar navigation, search, dark-mode CSS, and Mermaid-rendered diagrams.

## Failure modes the assistant should handle

- **Network down on first run** → clone fails; surface the error and stop.
- **Pull conflicts on re-run** → user has uncommitted local edits; skill should NOT auto-resolve; report the dirty state and stop.
- **Port 8765 in use** → `serve.sh` accepts a port arg; suggest `./scripts/serve.sh 8766`.
- **Unpaywall API rate-limit (rare)** → `verify_links.py` retries with backoff; if persistent, it skips upgrade and keeps the DOI.

## After-run summary the assistant should produce

Tell the user:

1. Where the guide is on disk.
2. Latest commit hash and date.
3. Whether link verification ran, and if so the headline numbers (`N reachable, M paywalled-host, K bot-blocked`).
4. The URL to open.
5. How to stop the server.
