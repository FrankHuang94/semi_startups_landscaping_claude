#!/usr/bin/env python3
"""refresh_section.py — helper to drive a category/section refresh.

This does NOT fetch data (that is the analyst/LLM's job). It:
  1. Prints the standard refresh checklist for a target file.
  2. Optionally stamps a file's `last_refreshed` date and bumps `refresh_count`
     in its YAML front matter (--stamp YYYY-MM-DD).
  3. Prints the matching copy-paste refresh prompt.

Usage:
    python scripts/refresh_section.py <relative_file_path> [--stamp YYYY-MM-DD]
    python scripts/refresh_section.py --list

Zero third-party dependencies.
"""
from __future__ import annotations
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _yamlmini import load, repo_root  # noqa: E402

ROOT = repo_root()

CHECKLIST = """
Refresh checklist for {target}:
  1. Search for new public info since last_refreshed.
  2. Add new companies; update funding rounds, valuations, stage changes.
  3. Update investor lists + strategic investors.
  4. Refresh customer traction / design wins.
  5. Move exits/shutdowns to Archived + deal_tracker/23.
  6. Refresh research / researcher / paper / patent signals.
  7. Update YAML front matter (counts, last_refreshed, refresh_count).
  8. Update data/*.yaml indexes + data/refresh_status.yaml.
  9. Update README dashboard + append REFRESH_LOG.md.
 10. Re-tag all data: [CONFIRMED] [TO VERIFY] [ESTIMATED] [UNCONFIRMED] [NO PUBLIC DATA].
"""

PROMPT = (
    "REFRESH CATEGORY: {target} — Refresh this category with new startups, funding "
    "rounds, investors, customer traction, technical milestones, M&A events, "
    "shutdowns, and research-to-startup signals since the last refresh. Update all "
    "relevant indexes and append REFRESH_LOG.md."
)


def list_files():
    data = load(os.path.join(ROOT, "data", "category_index.yaml")) or {}
    for c in data.get("categories", []):
        print(f"  {c.get('id')}  {c.get('file')}")


def stamp(path, date):
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        print("  (no YAML front matter; skipping stamp)")
        return
    parts = text.split("---", 2)
    front = parts[1]
    front = re.sub(r'last_refreshed:\s*"[^"]*"', f'last_refreshed: "{date}"', front)

    def bump(m):
        return f"refresh_count: {int(m.group(1)) + 1}"
    front = re.sub(r'refresh_count:\s*(\d+)', bump, front, count=1)
    new = "---" + front + "---" + parts[2]
    open(path, "w", encoding="utf-8").write(new)
    print(f"  stamped last_refreshed={date} and bumped refresh_count in {os.path.relpath(path, ROOT)}")


def main(argv):
    if "--list" in argv:
        list_files()
        return 0
    if len(argv) < 2:
        print(__doc__)
        return 2
    target = argv[1]
    path = os.path.join(ROOT, target)
    if not os.path.exists(path):
        print(f"File not found: {target}", file=sys.stderr)
        return 1
    print(CHECKLIST.format(target=target))
    if "--stamp" in argv:
        i = argv.index("--stamp")
        if i + 1 < len(argv):
            stamp(path, argv[i + 1])
        else:
            print("--stamp requires a YYYY-MM-DD date", file=sys.stderr)
            return 2
    print("\nCopy-paste prompt:\n")
    print(PROMPT.format(target=target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
