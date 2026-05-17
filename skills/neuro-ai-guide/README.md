# neuro-ai-guide skill

A Claude skill that regenerates the **Neuroscience and Computational Neuroscience for AI Researchers** study guide on demand and re-verifies every external citation against current open-access databases, so what the user gets always reflects:

1. The latest content from `main` of this repo, and
2. The current live state of every linked paper on the public web.

## Install

Drop the entire `skills/neuro-ai-guide/` directory into wherever your Claude environment loads skills from. For Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R skills/neuro-ai-guide ~/.claude/skills/
```

Then ask Claude something like *"generate the latest neuroscience study guide"*.

## Use without Claude

The scripts work standalone:

```bash
# 1. Pull the latest content
./scripts/generate.sh ~/my-neuro-guide

# 2. Re-verify every external link (writes link_audit.json)
python3 ./scripts/verify_links.py ~/my-neuro-guide

# 3. (Optional) Auto-rewrite markdown so paywalled DOIs become their OA copies
python3 ./scripts/verify_links.py ~/my-neuro-guide --apply

# 4. Serve locally
./scripts/serve.sh 8765 ~/my-neuro-guide
# open http://127.0.0.1:8765/
```

## How "always shows the latest content" works

- `generate.sh` clones / fast-forwards the canonical repo on every run.
- `verify_links.py` HEAD/GET-tests every URL, then queries Unpaywall for any DOI to find a free copy if one exists (papers move between paywalled and OA over time as embargo periods lapse).
- The link audit is written to `link_audit.json` so the user can see exactly which links were verified, which are bot-blocked, and which are dead.

## Layout

```
skills/neuro-ai-guide/
├── SKILL.md            # Claude skill manifest
├── README.md           # this file
└── scripts/
    ├── preflight.sh    # check git + python3
    ├── generate.sh     # clone or fast-forward the repo
    ├── verify_links.py # reachability + Unpaywall OA upgrade
    └── serve.sh        # start the local HTTP server
```

## No third-party dependencies

Only `git` and `python3` (stdlib). The verifier talks to `api.unpaywall.org` over HTTPS using `urllib`. No `pip install` step.
