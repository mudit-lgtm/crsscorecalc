#!/usr/bin/env python3
"""
fix_jsonld_quotes_html_only.py
Safely fixes broken JSON-LD quote issues only inside .html/.htm files.

Usage:
  python fix_jsonld_quotes_html_only.py
  python fix_jsonld_quotes_html_only.py --dry-run
"""

import re
import sys
import json
import shutil
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv
ROOT = Path(__file__).resolve().parent
SKIP_DIRS = {"node_modules", ".git", ".next", "dist", ".vercel", "__pycache__"}
TEXT_EXTS = {".html", ".htm"}

script_tag_re = re.compile(
    r'(<script\s+type=["\']application/ld\+json["\'][^>]*>)([\s\S]*?)(</script>)',
    re.IGNORECASE
)
escaped_url_re = re.compile(r'(?<=https://[^"\\\s>]+)\\\"')
trailing_backslash_quote_re = re.compile(r'\\\"(?=[\s\n\r]*[}\]])')

changed = []
fixed_blocks = 0
errors = []


def clean_json_text(text: str):
    text2 = escaped_url_re.sub('"', text)
    text2 = trailing_backslash_quote_re.sub('"', text2)
    return text2


for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if any(part in SKIP_DIRS for part in path.parts):
        continue
    if path.suffix.lower() not in TEXT_EXTS:
        continue

    try:
        original = path.read_text(encoding="utf-8", errors="replace")
        updated = original
        local_changes = [0]

        def repl(match):
            start, body, end = match.group(1), match.group(2), match.group(3)
            body2 = body.strip()
            body3 = clean_json_text(body2)

            try:
                json.loads(body3)
            except Exception:
                body4 = re.sub(r',\s*([}\]])', r'\1', body3)
                try:
                    json.loads(body4)
                    body3 = body4
                except Exception:
                    pass

            if body3 != body:
                local_changes[0] += 1

            return start + body3 + end

        updated = script_tag_re.sub(repl, updated)

        if updated != original:
            if DRY_RUN:
                changed.append(str(path.relative_to(ROOT)))
            else:
                backup = path.with_suffix(path.suffix + ".bak")
                if not backup.exists():
                    try:
                        shutil.copy2(path, backup)
                    except Exception:
                        pass
                path.write_text(updated, encoding="utf-8")
                changed.append(str(path.relative_to(ROOT)))
                fixed_blocks += local_changes[0]

    except Exception as e:
        errors.append(f"{path}: {e}")

print("=" * 60)
print("JSON-LD FIXER (HTML ONLY)")
print("=" * 60)
print(f"DRY RUN: {DRY_RUN}")
print(f"Changed files: {len(changed)}")
for f in changed[:200]:
    print(" ->", f)
if len(changed) > 200:
    print(f" ... and {len(changed) - 200} more")
print(f"Fixed schema blocks: {fixed_blocks}")
if errors:
    print("\nErrors:")
    for e in errors:
        print(" x", e)
print("=" * 60)
