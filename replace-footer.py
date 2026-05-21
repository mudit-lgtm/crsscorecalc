#!/usr/bin/env python3
"""
replace-footer.py
=================
Replaces <footer>...</footer> in every .html file with footer-snippet.html
Place this script + footer-snippet.html in your project root.

Usage:
  python replace-footer.py            # apply changes
  python replace-footer.py --dry-run  # preview only, no writes
"""
import os, re, shutil, sys

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
FOOTER_FILE = os.path.join(SCRIPT_DIR, "footer-snippet.html")
FOOTER_MARK = "UNIVERSAL FOOTER"
DRY_RUN     = "--dry-run" in sys.argv
SKIP_DIRS   = {"node_modules", ".git", ".next", "dist", ".vercel", "__pycache__"}

if not os.path.exists(FOOTER_FILE):
    print("❌ Missing: footer-snippet.html — place it next to this script.")
    sys.exit(1)

with open(FOOTER_FILE, "r", encoding="utf-8") as f:
    NEW_FOOTER = f.read().strip()

FOOTER_RE = re.compile(r'<footer[\s\S]*?</footer>', re.IGNORECASE | re.DOTALL)

replaced, skip_done, skip_none, errors = [], [], [], []

for root, dirs, files in os.walk(SCRIPT_DIR):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for fname in files:
        if not fname.endswith(".html"):
            continue
        if fname == "footer-snippet.html":
            continue

        fpath = os.path.join(root, fname)
        rel   = os.path.relpath(fpath, SCRIPT_DIR)

        try:
            with open(fpath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()

            if FOOTER_MARK in content:
                skip_done.append(rel)
                continue

            if not FOOTER_RE.search(content):
                skip_none.append(rel)
                continue

            new_content = FOOTER_RE.sub(NEW_FOOTER, content)

            if DRY_RUN:
                replaced.append(rel)
                continue

            shutil.copy2(fpath, fpath + ".bak")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)

            replaced.append(rel)

        except Exception as e:
            errors.append(f"{rel}: {e}")

W = 56
print("=" * W)
print("  CRS Footer Replacement Script")
print("=" * W)
if DRY_RUN:
    print("  ⚠️  DRY RUN — no files were changed\n")

print(f"\n✅ Footer replaced     ({len(replaced)}):")
for r in replaced:
    print(f"   → {r}")

print(f"\n⏩ Already up to date  ({len(skip_done)}):")
for r in skip_done:
    print(f"   · {r}")

print(f"\n⚠️  No <footer> tag     ({len(skip_none)}):")
for r in skip_none:
    print(f"   ! {r}")

if errors:
    print(f"\n❌ Errors ({len(errors)}):")
    for e in errors:
        print(f"   ✗ {e}")

print("\n" + "=" * W)
if not DRY_RUN and replaced:
    print(f"  {len(replaced)} file(s) updated. Backups saved as .html.bak")
elif DRY_RUN:
    print(f"  {len(replaced)} file(s) would be updated.")
print("=" * W)
