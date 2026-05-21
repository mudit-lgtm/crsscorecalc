#!/usr/bin/env python3
"""
replace-footer.py — FORCE mode
Replaces <footer>...</footer> in every .html file unconditionally.
Safe: backs up every file as .html.bak before writing.
Usage:
  python replace-footer.py            # force replace all
  python replace-footer.py --dry-run  # preview only
"""
import os, re, shutil, sys

SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
FOOTER_FILE = os.path.join(SCRIPT_DIR, "footer-snippet.html")
DRY_RUN     = "--dry-run" in sys.argv
SKIP_DIRS   = {"node_modules", ".git", ".next", "dist", ".vercel", "__pycache__"}

if not os.path.exists(FOOTER_FILE):
    print("ERROR: footer-snippet.html not found in repo root.")
    sys.exit(1)

with open(FOOTER_FILE, "r", encoding="utf-8") as f:
    NEW_FOOTER = f.read().strip()

FOOTER_RE = re.compile(r'<footer[\s\S]*</footer>', re.IGNORECASE | re.DOTALL)

replaced, skip_none, errors = [], [], []

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

            if not FOOTER_RE.search(content):
                skip_none.append(rel)
                continue

            new_content = FOOTER_RE.sub(NEW_FOOTER, content)

            if new_content == content:
                skip_none.append(f"{rel} (footer already identical)")
                continue

            if DRY_RUN:
                replaced.append(rel)
                continue

            shutil.copy2(fpath, fpath + ".bak")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)

            replaced.append(rel)

        except Exception as e:
            errors.append(f"{rel}: {e}")

W = 60
print("=" * W)
print("  CRS Footer Replacement — FORCE MODE")
print("=" * W)
if DRY_RUN:
    print("  DRY RUN — no files were changed\n")

print(f"\nFooter replaced ({len(replaced)}):")
for r in replaced:
    print(f"   -> {r}")

print(f"\nSkipped — no <footer> tag or already identical ({len(skip_none)}):")
for r in skip_none:
    print(f"   ! {r}")

if errors:
    print(f"\nErrors ({len(errors)}):")
    for e in errors:
        print(f"   x {e}")

print("\n" + "=" * W)
if not DRY_RUN and replaced:
    print(f"  {len(replaced)} file(s) updated. Backups: .html.bak")
elif DRY_RUN:
    print(f"  {len(replaced)} file(s) WOULD be updated.")
print("=" * W)
