#!/usr/bin/env python3
"""build_index.py — regenerate Markdown index tables from data/*.yaml.

Usage:
    python scripts/build_index.py [companies|investors|researchers|all] [--check]

By default prints the rendered Markdown table(s) to stdout so you can paste
them into README.md. With --check it only reports row counts (used by CI/validate).

Zero third-party dependencies: uses scripts/_yamlmini.py (PyYAML if installed).
"""
from __future__ import annotations
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _yamlmini import load, repo_root  # noqa: E402

ROOT = repo_root()
DATA = os.path.join(ROOT, "data")


def _fmt_list(v):
    if isinstance(v, list):
        return ", ".join(str(x) for x in v)
    return str(v) if v is not None else ""


def companies_table():
    data = load(os.path.join(DATA, "company_index.yaml")) or {}
    rows = sorted(data.get("companies", []), key=lambda c: str(c.get("name", "")).lower())
    out = ["| Company | Category | HQ | Founded | Stage | Total Funding | Lead Investors | Status | Primary File |",
           "|---------|----------|----|---------|-------|---------------|----------------|--------|--------------|"]
    for c in rows:
        out.append("| {name} | {category} | {hq} | {founded} | {stage} | {tf} | {li} | {status} | {pf} |".format(
            name=c.get("name", ""), category=c.get("category", ""), hq=c.get("hq", ""),
            founded=c.get("founded", ""), stage=c.get("stage", ""), tf=c.get("total_funding", ""),
            li=_fmt_list(c.get("lead_investors")), status=c.get("status", ""), pf=c.get("primary_file", "")))
    return "\n".join(out), len(rows)


def investors_table():
    data = load(os.path.join(DATA, "investor_index.yaml")) or {}
    rows = sorted(data.get("investors", []), key=lambda c: str(c.get("name", "")).lower())
    out = ["| Investor | Type | Semi Focus | AI Infra Focus | Relevant Portfolio | Stage Pref | Notes |",
           "|----------|------|-----------|----------------|--------------------|-----------|-------|"]
    for i in rows:
        out.append("| {name} | {type} | {sf} | {ai} | {pf} | {sp} | {notes} |".format(
            name=i.get("name", ""), type=i.get("type", ""), sf=i.get("semi_focus", ""),
            ai=i.get("ai_infra_focus", ""), pf=_fmt_list(i.get("portfolio")),
            sp=i.get("stage_pref", ""), notes=i.get("notes", "")))
    return "\n".join(out), len(rows)


def researchers_table():
    data = load(os.path.join(DATA, "researcher_index.yaml")) or {}
    rows = sorted(data.get("researchers", []), key=lambda c: str(c.get("name", "")).lower())
    out = ["| Researcher | Institution | Research Area | Patent Activity | Startup Signals | VC Relevance | Profile |",
           "|------------|-------------|---------------|-----------------|-----------------|:------------:|---------|"]
    for r in rows:
        out.append("| {name} | {inst} | {area} | {pa} | {ss} | {vc} | {file} |".format(
            name=r.get("name", ""), inst=r.get("institution", ""), area=r.get("research_area", ""),
            pa=r.get("patent_activity", ""), ss=r.get("startup_signal", ""),
            vc=r.get("vc_relevance", ""), file=r.get("file", "")))
    return "\n".join(out), len(rows)


BUILDERS = {
    "companies": companies_table,
    "investors": investors_table,
    "researchers": researchers_table,
}


def main(argv):
    target = argv[1] if len(argv) > 1 and not argv[1].startswith("--") else "all"
    check = "--check" in argv
    targets = list(BUILDERS) if target == "all" else [target]
    for t in targets:
        if t not in BUILDERS:
            print(f"Unknown target: {t}. Choose from {list(BUILDERS)} or 'all'.", file=sys.stderr)
            return 2
        table, n = BUILDERS[t]()
        if check:
            print(f"[build_index] {t}: {n} rows")
        else:
            print(f"\n## {t.title()} ({n})\n")
            print(table)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
