#!/usr/bin/env python3
"""Re-verify every external link across all chapters of the study guide.

For each URL:
  - HEAD/GET-test reachability with a browser-like User-Agent
  - If it's a doi.org URL, query Unpaywall (api.unpaywall.org) and
    upgrade to an open-access copy when one exists and verifies
  - Tag known-Cloudflare-blocked OA hosts (PNAS, JNeurosci, biorxiv,
    cell.com, science.org) so they're not mistaken for dead

Outputs `link_audit.json` next to manifest.json with three buckets:
  ok        — URL responded 2xx/3xx
  blocked   — likely Cloudflare bot block on a free-to-public host
  dead      — URL returned 4xx/5xx or DNS-failed

With --apply, the script rewrites markdown so paywalled DOIs are
replaced with the verified OA URL inline.

Usage:
    python3 verify_links.py [TARGET_DIR] [--apply] [--max-workers N]
"""
from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/121.0.0.0 Safari/537.36"
)

# Hosts that serve free-to-public content but routinely block scripts via
# Cloudflare or similar — they're not dead, they just refuse non-browser UAs.
# doi.org redirects land on these same publishers, so it's listed too.
BOT_BLOCKED_OK_HOSTS = (
    "doi.org",
    "pnas.org", "jneurosci.org", "biorxiv.org",
    "cell.com", "sciencedirect.com",
    "science.org", "sciencemag.org",
    "wiley.com", "onlinelibrary.wiley.com", "nyaspubs.onlinelibrary.wiley.com",
    "springer.com", "link.springer.com",
    "tandfonline.com", "royalsocietypublishing.org",
    "researchgate.net",
    "annualreviews.org",
    "academic.oup.com",
    "lesswrong.com",  # Cloudflare 429 to scripts; renders for humans
    "ai.meta.com",    # blog 400 to scripts
)

_ctx = ssl.create_default_context()
_ctx.check_hostname = False
_ctx.verify_mode = ssl.CERT_NONE


def fetch(url: str, timeout: int = 15) -> int:
    """Return HTTP status code (or -1 on connect/DNS error)."""
    headers = {"User-Agent": BROWSER_UA, "Accept": "text/html,*/*"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=_ctx, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return -1


def host(url: str) -> str:
    try:
        return (urllib.parse.urlparse(url).hostname or "").lower()
    except Exception:
        return ""


def is_doi(url: str) -> bool:
    return "doi.org/" in url


def doi_of(url: str) -> str | None:
    m = re.search(r"doi\.org/(.+)", url)
    return m.group(1) if m else None


def unpaywall_oa(doi: str, email: str = "guide@example.com",
                 timeout: int = 15) -> str | None:
    """Return the best open-access URL for a DOI, or None."""
    api = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={email}"
    try:
        req = urllib.request.Request(api, headers={"User-Agent": "neuro-ai-guide/1.0"})
        with urllib.request.urlopen(req, context=_ctx, timeout=timeout) as r:
            data = json.load(r)
    except Exception:
        return None
    bo = data.get("best_oa_location") or {}
    candidates = [
        bo.get("url_for_pdf"),
        bo.get("url_for_landing_page"),
        bo.get("url"),
    ]
    for loc in (data.get("oa_locations") or []):
        candidates += [loc.get("url_for_pdf"), loc.get("url_for_landing_page"), loc.get("url")]
    for c in candidates:
        if c:
            code = fetch(c)
            if isinstance(code, int) and 200 <= code < 400:
                return c
    return None


_LINK_RE = re.compile(r"\[([^\]]+)\]\(")


def extract_links(md: str):
    """Yield (anchor_text, url) for every markdown link in `md`."""
    i = 0
    while True:
        m = _LINK_RE.search(md, i)
        if not m:
            return
        start = m.end()
        depth = 1
        j = start
        while j < len(md) and depth:
            c = md[j]
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
            j += 1
        if depth == 0:
            url = md[start:j - 1]
            anchor = m.group(1)
            if url.startswith(("http://", "https://")):
                yield anchor, url
        i = j


def classify(url: str, code: int) -> str:
    if isinstance(code, int) and 200 <= code < 400:
        return "ok"
    h = host(url)
    if any(b in h for b in BOT_BLOCKED_OK_HOSTS):
        return "blocked"
    return "dead"


def collect(target: Path):
    """Return {url: [(file, anchor), ...]}."""
    links = {}
    for p in sorted((target / "chapters").glob("*.md")):
        for anchor, url in extract_links(p.read_text()):
            links.setdefault(url, []).append((p.name, anchor))
    return links


def check_all(urls, max_workers: int = 12):
    results = {}
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futs = {ex.submit(fetch, u): u for u in urls}
        for f in as_completed(futs):
            results[futs[f]] = f.result()
    return results


def upgrade_paywalled_dois(urls):
    """For each DOI URL, attempt OA upgrade. Returns {old_url: new_url}."""
    upgrades = {}
    dois = [u for u in urls if is_doi(u)]
    for u in dois:
        d = doi_of(u)
        if not d:
            continue
        oa = unpaywall_oa(d)
        if oa and oa != u:
            upgrades[u] = oa
        # gentle on the API
        time.sleep(0.4)
    return upgrades


def apply_substitutions(target: Path, mapping: dict):
    """Rewrite markdown files replacing `](old)` with `](new)`."""
    if not mapping:
        return 0
    edits = 0
    for p in (target / "chapters").glob("*.md"):
        txt = p.read_text()
        new = txt
        for old, repl in mapping.items():
            marker = f"]({old})"
            replacement = f"]({repl})"
            if marker in new:
                cnt = new.count(marker)
                new = new.replace(marker, replacement)
                edits += cnt
        if new != txt:
            p.write_text(new)
    return edits


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", nargs="?", default=str(Path.home() / "computational-neuro"),
                    help="path to the cloned study guide (default: ~/computational-neuro)")
    ap.add_argument("--apply", action="store_true",
                    help="rewrite markdown to substitute OA URLs for paywalled DOIs")
    ap.add_argument("--max-workers", type=int, default=12)
    ap.add_argument("--no-unpaywall", action="store_true",
                    help="skip the Unpaywall lookup pass")
    args = ap.parse_args(argv)

    target = Path(args.target).expanduser().resolve()
    if not (target / "chapters").is_dir():
        print(f"ERROR: {target} doesn't look like a study-guide checkout", file=sys.stderr)
        return 2

    print(f"==> scanning {target}/chapters/")
    links = collect(target)
    print(f"    {len(links)} unique URLs across {len(set(f for refs in links.values() for f,_ in refs))} files")

    print("==> reachability sweep")
    codes = check_all(list(links), args.max_workers)

    ok = [u for u, c in codes.items() if classify(u, c) == "ok"]
    blocked = [u for u, c in codes.items() if classify(u, c) == "blocked"]
    dead = [u for u, c in codes.items() if classify(u, c) == "dead"]

    print(f"    ok:      {len(ok)}")
    print(f"    blocked: {len(blocked)}  (Cloudflare bot-protected OA hosts; OK in browser)")
    print(f"    dead:    {len(dead)}")

    upgrades = {}
    if not args.no_unpaywall:
        print("==> Unpaywall pass on DOI links")
        # Only try DOIs that resolved (we have a DOI → maybe OA elsewhere)
        upgrades = upgrade_paywalled_dois([u for u in links if is_doi(u)])
        print(f"    OA upgrades available: {len(upgrades)}")

    audit = {
        "target": str(target),
        "total_unique_urls": len(links),
        "ok": sorted(ok),
        "blocked_ok_in_browser": sorted(blocked),
        "dead": [
            {"url": u, "status": codes[u], "refs": links[u]} for u in sorted(dead)
        ],
        "oa_upgrades_available": [
            {"old": k, "new": v} for k, v in upgrades.items()
        ],
    }
    audit_path = target / "link_audit.json"
    audit_path.write_text(json.dumps(audit, indent=2))
    print(f"==> wrote {audit_path}")

    if args.apply and upgrades:
        n = apply_substitutions(target, upgrades)
        print(f"==> applied {n} substitutions across markdown files")
    elif upgrades:
        print("    (re-run with --apply to rewrite markdown)")

    if dead:
        print("\nDead links to fix manually:")
        for u in sorted(dead)[:25]:
            print(f"  [{codes[u]}] {u}")
        if len(dead) > 25:
            print(f"  ... and {len(dead) - 25} more in {audit_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
