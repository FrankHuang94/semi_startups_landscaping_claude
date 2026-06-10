# Refresh Log

Chronological log of all database refreshes. Newest entries on top. Each entry should record scope, what changed, and the confidence posture of new data.

> **Commit message convention for refreshes:**
> `refresh: [filename] — [brief change summary] (YYYY-MM-DD)`

---

## 2026-06-09 — Initial Full Build (Refresh #1)

- **Type:** Full initial build
- **Scope:** Entire repository created from public knowledge as of the model knowledge cutoff and analyst synthesis.
- **Files created:** 45 (6 top-level docs, 9 templates, 17 category files, 5 deal-tracker files, 6 researcher files, 10 data indexes, 3 scripts — see completion summary).
- **Entries added:**
  - Categories 01–17 populated with thesis, market context, startup tables, marquee company profiles, heatmaps, investor tables, research signals, diligence questions.
  - ~40 full company profiles + ~70 lighter table entries (110+ companies referenced total).
  - 14 VC investor profiles, 12 strategic investor profiles.
  - 18 funding rounds, 10 M&A deals, 8 exit/shutdown entries.
  - 10 leading researchers, 12 labs, 12 papers, 6 patents.
- **Entries archived:** Graphcore (acquired, SoftBank 2024), Untether AI (wound down, IP to AMD 2025), and other exits flagged in [deal_tracker/23_exit_and_shutdown_tracker.md](deal_tracker/23_exit_and_shutdown_tracker.md).
- **Key changes:** Repository scaffolding, indexes, scripts, and dashboard established. Baseline for all future refreshes.
- **Data confidence posture:** Most financial figures tagged `[TO VERIFY]` or `[ESTIMATED]`. Funding totals are point-in-time and frequently mis-reported; re-verify each at next refresh. Company existence, category, and HQ are high-confidence; round sizes, valuations, and headcounts are lower-confidence.
- **Known data gaps:** Valuations largely undisclosed; stealth-company financials unknown; private revenue unverified; some Korean/Chinese/EU startups under-covered; patent watchlist is seed-level only.
- **Sources:** Public company sites, press releases, reputable trade press (point-in-time), academic publications, conference programs. No private or non-public data used.

---

<!-- Append new refresh entries above this line, newest first. -->
