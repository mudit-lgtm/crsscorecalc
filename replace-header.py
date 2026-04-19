#!/usr/bin/env python3
"""
replace-header.py
=================
Replaces <header>...</header> in every .html file with header-snippet.html
Place this script + header-snippet.html in your project root.

Usage:
  python replace-header.py            # apply
  python replace-header.py --dry-run  # preview only
"""
import os, re, shutil, sys

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
HEADER_FILE = os.path.join(SCRIPT_DIR, "header-snippet.html")
HEADER_MARK = "UNIVERSAL HEADER"
DRY_RUN     = "--dry-run" in sys.argv
SKIP_DIRS   = {"node_modules", ".git", ".next", "dist", ".vercel", "__pycache__"}

if not os.path.exists(HEADER_FILE):
    print("❌ Missing: header-snippet.html — place it next to this script.")
    sys.exit(1)

with open(HEADER_FILE, "r", encoding="utf-8") as f:
    NEW_HEADER = f.read().strip()

HEADER_RE = re.compile(r'<header[\s\S]*?</header>', re.IGNORECASE | re.DOTALL)

replaced, skip_done, skip_none, errors = [], [], [], []

for root, dirs, files in os.walk(SCRIPT_DIR):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for fname in files:
        if not fname.endswith(".html"):
            continue
        if fname == "header-snippet.html":
            continue

        fpath = os.path.join(root, fname)
        rel   = os.path.relpath(fpath, SCRIPT_DIR)

        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()

            # Already replaced? Skip
            if HEADER_MARK in content:
                skip_done.append(rel)
                continue

            # No header tag? Skip
            if not HEADER_RE.search(content):
                skip_none.append(rel)
                continue

            new_content = HEADER_RE.sub(NEW_HEADER, content)

            if DRY_RUN:
                replaced.append(rel)
                continue

            shutil.copy2(fpath, fpath + ".bak")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)

            replaced.append(rel)

        except Exception as e:
            errors.append(f"{rel}: {e}")

# Report
print("=" * 54)
print("  CRS Header Replacement Script")
print("=" * 54)
if DRY_RUN:
    print("  ⚠️  DRY RUN — no files changed\n")

print(f"\n✅ Header replaced ({len(replaced)}):")
for r in replaced: print(f"   → {r}")

print(f"\n⏩ Already up to date ({len(skip_done)}):")
for r in skip_done: print(f"   · {r}")

print(f"\n⚠️  No <header> tag found ({len(skip_none)}):")
for r in skip_none: print(f"   ! {r}")

if errors:
    print(f"\n❌ Errors ({len(errors)}):")
    for e in errors: print(f"   ✗ {e}")

print("\n" + "=" * 54)
if not DRY_RUN and replaced:
    print(f"  {len(replaced)} file(s) updated. Backups: .html.bak")
elif DRY_RUN:
    print(f"  {len(replaced)} file(s) would be updated.")
print("=" * 54)
