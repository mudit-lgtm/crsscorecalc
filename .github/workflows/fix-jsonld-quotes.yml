name: Fix JSON-LD Quotes

on:
  workflow_dispatch:

permissions:
  contents: write

jobs:
  fix-jsonld:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repo
        uses: actions/checkout@v4.2.2

      - name: Dry run JSON-LD fixer
        run: python fix_jsonld_quotes.py --dry-run

      - name: Apply JSON-LD fixer
        run: python fix_jsonld_quotes.py

      - name: Show diff summary
        run: git diff --stat || echo "No changes"

      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -A
          git diff --staged --quiet || git commit -m "fix: repair broken JSON-LD quotes"
          git push
