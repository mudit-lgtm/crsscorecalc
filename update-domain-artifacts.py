#!/usr/bin/env python3
"""
update-domain-artifacts.py
Updates canonical tags, sitemap URLs, robots.txt sitemap line, and JSON-LD schema URLs
from OLD_DOMAIN to NEW_DOMAIN across HTML/JSON/JS files in a GitHub repo.

Usage:
  python update-domain-artifacts.py
  python update-domain-artifacts.py --dry-run
"""

import re
import sys
import shutil
from pathlib import Path

OLD_DOMAIN = "https://crsscorecalculator.vercel.app"
NEW_DOMAIN = "https://crscalculator.site"
DRY_RUN = "--dry-run" in sys.argv
SKIP_DIRS = {"node_modules", ".git", ".next", "dist", ".vercel", "__pycache__"}
ROOT = Path(__file__).resolve().parent

TEXT_EXTS = {".html", ".htm", ".xml", ".txt", ".json", ".js", ".jsx", ".ts", ".tsx", ".md"}

replace_counts = {
    "files": 0,
    "canonicals": 0,
    "sitemaps": 0,
    "schema_urls": 0,
    "robots": 0,
    "other": 0,
}

changed = []
skipped = []
errors = []

canonical_re = re.compile(r'(<link\s+[^>]*rel=["\']canonical["\'][^>]*href=["\'])[^"\']+(["\'])', re.IGNORECASE)
meta_og_url_re = re.compile(r'(<meta\s+[^>]*property=["\']og:url["\'][^>]*content=["\'])[^"\']+(["\'])', re.IGNORECASE)
meta_twitter_url_re = re.compile(r'(<meta\s+[^>]*name=["\']twitter:url["\'][^>]*content=["\'])[^"\']+(["\'])', re.IGNORECASE)
url_re = re.compile(re.escape(OLD_DOMAIN))
sitemap_loc_re = re.compile(r'(<loc>)' + re.escape(OLD_DOMAIN) + r'([^<]*)(</loc>)', re.IGNORECASE)
robots_sitemap_re = re.compile(r'(^\s*Sitemap:\s*)' + re.escape(OLD_DOMAIN) + r'(/[^\s]*)\s*$', re.IGNORECASE | re.MULTILINE)
json_ld_url_re = re.compile(r'("(?:@id|url|mainEntityOfPage)"\s*:\s*")' + re.escape(OLD_DOMAIN) + r'([^"\n]*)"', re.IGNORECASE)

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if any(part in SKIP_DIRS for part in path.parts):
        continue
    if path.suffix.lower() not in TEXT_EXTS:
        continue

    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        original = text

        if path.name.lower() == "robots.txt":
            text, n = robots_sitemap_re.subn(r"\1" + NEW_DOMAIN + r"\2", text)
            if n:
                replace_counts["robots"] += n

        text, n1 = canonical_re.subn(r"\1" + NEW_DOMAIN + r"\2", text)
        text, n2 = meta_og_url_re.subn(r"\1" + NEW_DOMAIN + r"\2", text)
        text, n3 = meta_twitter_url_re.subn(r"\1" + NEW_DOMAIN + r"\2", text)
        text, n4 = sitemap_loc_re.subn(r"\1" + NEW_DOMAIN + r"\2\3", text)
        text, n5 = json_ld_url_re.subn(r"\1" + NEW_DOMAIN + r"\2\"", text)
        text, n6 = url_re.subn(NEW_DOMAIN, text)

        file_counts = n1 + n2 + n3 + n4 + n5 + n6
        if file_counts:
            if DRY_RUN:
                changed.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(text, encoding="utf-8")
                backup = path.with_suffix(path.suffix + ".bak")
                try:
                    if not backup.exists():
                        shutil.copy2(path, backup)
                except Exception:
                    pass
                changed.append(str(path.relative_to(ROOT)))
                replace_counts["files"] += 1
                replace_counts["canonicals"] += n1 + n2 + n3
                replace_counts["sitemaps"] += n4
                replace_counts["schema_urls"] += n5
                replace_counts["other"] += n6
        else:
            skipped.append(str(path.relative_to(ROOT)))

    except Exception as e:
        errors.append(f"{path}: {e}")

print("=" * 60)
print("DOMAIN UPDATE SCRIPT")
print("=" * 60)
print(f"OLD: {OLD_DOMAIN}")
print(f"NEW: {NEW_DOMAIN}")
print(f"DRY RUN: {DRY_RUN}")
print()
print(f"Changed files: {len(changed)}")
for f in changed[:200]:
    print(" ->", f)
if len(changed) > 200:
    print(f" ... and {len(changed) - 200} more")
print()
print("Replacement counts:", replace_counts)

if errors:
    print("\nErrors:")
    for e in errors:
        print(" x", e)

print("=" * 60)
