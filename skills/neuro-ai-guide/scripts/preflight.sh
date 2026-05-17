#!/usr/bin/env bash
# Preflight: verify git + python3 are available.
# Prints either "OK" with discovered versions or fails with a clear message.
set -euo pipefail

missing=()
command -v git >/dev/null 2>&1 || missing+=("git")
command -v python3 >/dev/null 2>&1 || missing+=("python3")

if [[ ${#missing[@]} -gt 0 ]]; then
  echo "ERROR: missing required tools: ${missing[*]}" >&2
  echo "Install via Homebrew (macOS): brew install ${missing[*]}" >&2
  echo "Install via apt (Debian/Ubuntu): sudo apt-get install ${missing[*]/python3/python3-minimal}" >&2
  exit 1
fi

echo "git:     $(git --version)"
echo "python3: $(python3 --version)"
echo "OK"
