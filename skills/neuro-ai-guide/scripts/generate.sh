#!/usr/bin/env bash
# Generate (clone or update) the study guide from the canonical upstream.
# Usage: generate.sh [TARGET_DIR]
#   TARGET_DIR defaults to ~/computational-neuro
set -euo pipefail

REPO_URL="https://github.com/palmer159/computational-neuro.git"
TARGET="${1:-$HOME/computational-neuro}"

if [[ -d "$TARGET/.git" ]]; then
  echo "==> updating existing checkout at $TARGET"
  cd "$TARGET"
  # Check for uncommitted changes and refuse to clobber them.
  if [[ -n "$(git status --porcelain)" ]]; then
    echo "ERROR: $TARGET has uncommitted local changes. Commit/stash them first, then re-run." >&2
    git status --short >&2
    exit 2
  fi
  # Capture default branch (handles forks where it might not be 'main')
  branch="$(git rev-parse --abbrev-ref HEAD)"
  git fetch origin "$branch"
  git pull --ff-only origin "$branch"
elif [[ -e "$TARGET" ]]; then
  echo "ERROR: $TARGET exists but is not a git checkout. Pick a different target." >&2
  exit 2
else
  echo "==> cloning $REPO_URL into $TARGET"
  git clone --depth 1 "$REPO_URL" "$TARGET"
  cd "$TARGET"
fi

commit="$(git log -1 --format='%h')"
date="$(git log -1 --format='%ad' --date=short)"
chapters="$(ls chapters/*.md 2>/dev/null | wc -l | tr -d ' ')"
manifest_count="$(python3 -c "import json; m=json.load(open('manifest.json')); print(sum(len(p['chapters']) for p in m['parts']))" 2>/dev/null || echo '?')"

echo
echo "  target:           $TARGET"
echo "  latest commit:    $commit ($date)"
echo "  chapters on disk: $chapters"
echo "  manifest entries: $manifest_count"
echo
echo "Next: re-verify links with:"
echo "  python3 \"$(dirname "$0")/verify_links.py\" \"$TARGET\""
echo "Or skip straight to serving:"
echo "  \"$(dirname "$0")/serve.sh\""
