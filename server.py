#!/usr/bin/env python3
"""Local study-guide server. Stdlib only.

Serves index.html, manifest.json, and chapter markdown.
The frontend renders Markdown + Mermaid client-side via marked.js + mermaid (CDN).
"""
from __future__ import annotations

import argparse
import http.server
import os
import socketserver
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):  # noqa: A003
        sys.stderr.write("[server] %s - %s\n" % (self.address_string(), fmt % args))


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8765")))
    p.add_argument("--host", default="127.0.0.1")
    args = p.parse_args()

    os.chdir(ROOT)
    with socketserver.TCPServer((args.host, args.port), Handler) as httpd:
        url = f"http://{args.host}:{args.port}/"
        sys.stderr.write(f"\n  Neuroscience for AI — study guide\n  serving {ROOT}\n  open {url}\n  Ctrl-C to stop\n\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            sys.stderr.write("\n  shutting down\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
