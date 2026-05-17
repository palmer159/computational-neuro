#!/usr/bin/env bash
# Serve the local SPA. Usage: serve.sh [PORT] [TARGET_DIR]
set -euo pipefail

PORT="${1:-8765}"
TARGET="${2:-$HOME/computational-neuro}"

if [[ ! -f "$TARGET/server.py" ]]; then
  echo "ERROR: $TARGET/server.py missing. Run generate.sh first." >&2
  exit 1
fi

cd "$TARGET"
if lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "ERROR: port $PORT already in use. Try: $0 $((PORT+1))" >&2
  exit 1
fi

echo "==> starting server on port $PORT (CWD: $TARGET)"
echo "    open http://127.0.0.1:$PORT/"
echo "    stop with: kill \$(lsof -tiTCP:$PORT -sTCP:LISTEN)"
exec python3 server.py --port "$PORT"
