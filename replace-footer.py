#!/usr/bin/env python3
"""
replace-footer.py
=================
Replaces the <footer>...</footer> block in every .html file in the
current folder (and sub-folders) with the universal footer from
footer-snippet.html.

Usage:
  1. Put this script + footer-snippet.html in your PROJECT ROOT.
  2. Run: python replace-footer.py
  3. It creates backups as filename.html.bak before touching any file.
  4. Run again safely — it detects the universal footer and skips already-updated files.
"""

import os
import re
import shutil
import sys

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
SNIPPET_FILE = os.path.join(SCRIPT_DIR, "footer-snippet.html")
FOOTER_MARKER = "UNIVERSAL FOOTER"      # marker in the snippet to detect already-replaced files
DRY_RUN = "--dry-run" in sys.argv       # pass --dry-run to preview without changing files

# ---------- load the new footer snippet ----------
with open(SNIPPET_FILE, "r", encoding="utf-8") as f:
    NEW_FOOTER = f.read().strip()

# Regex: matches everything from <footer ... > to </footer>
# re.DOTALL so it crosses newlines; re.IGNORECASE for edge cases
FOOTER_REGEX = re.compile(r'<footer[\s\S]*?</footer>', re.IGNORECASE | re.DOTALL)

replaced = []
skipped_already_done = []
skipped_no_footer = []
errors = []

for root, dirs, files in os.walk(SCRIPT_DIR):
    # skip node_modules, .git, .next, dist, .vercel
    dirs[:] = [d for d in dirs if d not in ("node_modules", ".git", ".next", "dist", ".vercel", "__pycache__")]

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

            # Already using the universal footer? Skip.
            if FOOTER_MARKER in content:
                skipped_already_done.append(rel)
                continue

            # No footer tag at all? Skip.
            if not FOOTER_REGEX.search(content):
                skipped_no_footer.append(rel)
                continue

            # Replace ALL footer blocks with the new one
            new_content = FOOTER_REGEX.sub(NEW_FOOTER, content)

            if DRY_RUN:
                replaced.append(rel)
                continue

            # Backup original
            shutil.copy2(fpath, fpath + ".bak")

            # Write updated file
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)

            replaced.append(rel)

        except Exception as e:
            errors.append(f"{rel}: {e}")

# ---------- report ----------
print("=" * 56)
print("  CRS Footer Replacement Script")
print("=" * 56)

if DRY_RUN:
    print("  ⚠️  DRY RUN — no files were changed\n")

print(f"\n✅ Files updated ({len(replaced)}):")
for r in replaced:
    print(f"   → {r}")

print(f"\n⏩ Already using universal footer ({len(skipped_already_done)}):")
for r in skipped_already_done:
    print(f"   · {r}")

print(f"\n⚠️  No <footer> tag found ({len(skipped_no_footer)}):")
for r in skipped_no_footer:
    print(f"   ! {r}")

if errors:
    print(f"\n❌ Errors ({len(errors)}):")
    for e in errors:
        print(f"   ✗ {e}")

print("\n" + "=" * 56)
if not DRY_RUN and replaced:
    print(f"  Backups saved as filename.html.bak")
print("=" * 56)
