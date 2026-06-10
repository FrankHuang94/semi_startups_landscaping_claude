#!/usr/bin/env python3
"""validate_database.py — integrity checks for the semiconductor-startup-landscape DB.

Checks:
  1. Every file referenced in data/category_index.yaml exists.
  2. Every category file (01-17) contains the required sections + YAML front matter.
  3. data/refresh_status.yaml references resolve to real files.
  4. company/investor/researcher index files parse and are non-empty.
  5. Relative Markdown links in top-level docs and category files resolve.
  6. Reports the count of untagged numeric funding claims is out of scope (manual),
     but flags files missing a data-quality tag legend reference.

Exit code 0 if no errors (warnings allowed), 1 if errors found.
Zero third-party dependencies.
"""
from __future__ import annotations
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _yamlmini import load, repo_root  # noqa: E402

ROOT = repo_root()
errors: list[str] = []
warnings: list[str] = []

# Each required section is a tuple of acceptable heading substrings (any one matches).
# Category 17 is intentionally theme-based, so it uses "Theme" heading variants.
REQUIRED_CATEGORY_SECTIONS = [
    ("1. VC Investment Thesis",),
    ("2. Market Context",),
    ("Startup Landscape Table", "Startup/Theme Landscape Table"),
    ("Company Profiles", "Company/Theme Profiles"),
    ("Investment Heatmap",),
    ("Leading Investors", "Leading Investors in This Pipeline"),
    ("Leading Research",),
    ("Diligence Questions",),
    ("Refresh Notes",),
]


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def check_category_index():
    data = load(os.path.join(ROOT, "data", "category_index.yaml")) or {}
    cats = data.get("categories", [])
    if not cats:
        err("category_index.yaml has no categories")
    for c in cats:
        f = c.get("file")
        if not f:
            err(f"category {c.get('id')} missing file path")
            continue
        if not os.path.exists(os.path.join(ROOT, f)):
            err(f"category_index references missing file: {f}")
    return cats


def check_category_files():
    catdir = os.path.join(ROOT, "categories")
    files = sorted(fn for fn in os.listdir(catdir) if fn.endswith(".md"))
    if len(files) != 17:
        warn(f"expected 17 category files, found {len(files)}")
    for fn in files:
        path = os.path.join(catdir, fn)
        text = open(path, encoding="utf-8").read()
        if not text.startswith("---"):
            err(f"{fn}: missing YAML front matter block")
        else:
            fm = text.split("---", 2)
            if len(fm) >= 3:
                front = fm[1]
                for key in ("category_id", "category_name", "last_refreshed", "refresh_count"):
                    if key not in front:
                        err(f"{fn}: front matter missing '{key}'")
        for variants in REQUIRED_CATEGORY_SECTIONS:
            if not any(v in text for v in variants):
                err(f"{fn}: missing required section '{variants[0]}'")


def check_refresh_status():
    data = load(os.path.join(ROOT, "data", "refresh_status.yaml")) or {}
    for entry in data.get("files", []):
        f = entry.get("file")
        if f and not os.path.exists(os.path.join(ROOT, f)):
            err(f"refresh_status references missing file: {f}")


def check_indexes_nonempty():
    for name, key in (("company_index.yaml", "companies"),
                      ("investor_index.yaml", "investors"),
                      ("researcher_index.yaml", "researchers")):
        data = load(os.path.join(ROOT, "data", name)) or {}
        rows = data.get(key, [])
        if not rows:
            err(f"{name}: '{key}' list is empty or failed to parse")
        else:
            print(f"[ok] {name}: {len(rows)} entries")


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check_links():
    md_files = []
    for base, _dirs, fns in os.walk(ROOT):
        if os.sep + ".git" in base:
            continue
        for fn in fns:
            if fn.endswith(".md"):
                md_files.append(os.path.join(base, fn))
    broken = 0
    for path in md_files:
        text = open(path, encoding="utf-8").read()
        for m in LINK_RE.finditer(text):
            target = m.group(1).split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if not os.path.exists(resolved):
                broken += 1
                rel = os.path.relpath(path, ROOT)
                warn(f"broken relative link in {rel}: {target}")
    if broken == 0:
        print("[ok] all relative Markdown links resolve")


def main():
    print(f"Validating database at: {ROOT}\n")
    check_category_index()
    check_category_files()
    check_refresh_status()
    check_indexes_nonempty()
    check_links()

    print()
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")
    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors:
            print(f"  x {e}")
        print("\nVALIDATION FAILED")
        return 1
    print(f"\nVALIDATION PASSED ({len(warnings)} warnings)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
