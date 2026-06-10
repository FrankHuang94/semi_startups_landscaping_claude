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

## 2026-06-09 — Researchers & Research Watchlists Expansion (Refresh #2)

- **Type:** Targeted expansion (researchers, labs, papers, patents)
- **Scope:** [RESEARCH_AND_RESEARCHERS.md](RESEARCH_AND_RESEARCHERS.md) ecosystem — significantly deepened the sourcing engine.
- **Entries added/updated:**
  - **Leading researchers:** 10 → **52**, reorganized into 10 domain sections (architecture/systems, efficient-ML, memory/PIM, interconnect, photonics, analog/IMC, EDA, packaging/3D, power, quantum/cryo). New names incl. Tri Dao, Christopher Ré, Kunle Olukotun, Mark Horowitz, Joel Emer, Tushar Krishna, Daniel Sanchez, Hadi Esmaeilzadeh, Brooks/Wei, Vijay Janapa Reddi, Saman Amarasinghe, Saugata Ghose, Moinuddin Qureshi, Mattan Erez, Amin Vahdat, Ramin Farjadrad, Michal Lipson, Dirk Englund, Marin Soljačić, Jelena Vučković, Naresh Shanbhag, Kaushik Roy, Wei Lu, Dmitri Strukov, Brucek Khailany, Mirhoseini & Goldie, Jason Cong, David Z. Pan, Siddharth Garg, Deming Chen, Subhasish Mitra, Muhannad Bakir, Subramanian Iyer, David Perreault, Tomás Palacios, Khurram Afridi, Mikhail Lukin, John Martinis, Robert Schoelkopf, Edoardo Charbon.
  - **University labs:** 9 → **23** (added UCLA CHIPS/SiIF, GT 3D Systems, MIT RLE photonics, UCSB cluster, UIUC, UT Austin, Purdue, Michigan, Yale, Harvard, MIT power, EPFL, NYU).
  - **Corporate labs:** 8 → **14** (added AWS Annapurna, AMD Research, Apple silicon, Tesla Dojo, TSMC research, Qualcomm AI Research).
  - **Paper watchlist:** 12 → **34**, organized by domain with 2023–2026 emphasis (FlashAttention-2/3, AWQ/QServe, StreamingLLM, vLLM/PagedAttention, SGLang, speculative decoding, TPU v4 OCS, MTIA, Maia, Chiplet Cloud, Pond/TPP CXL, PIM-for-LLM, IBM analog-AI, photonic DNN, Taichi, Lightmatter Nature, AlphaChip, ChipNeMo, VerilogEval, QEC "Willow", neutral-atom logical processor, cryo-CMOS, etc.).
  - **Patent watchlist:** 10 → **22** clusters (UCIe/D2D, NoC fabric, DIMC, LPO, CPO/fiber-attach, 800V/vertical power, hybrid bonding, RL/LLM-for-EDA, atom-array control, cryo-CMOS).
- **Indexes/README updated:** `data/researcher_index.yaml` (52), `data/lab_index.yaml` (25), `data/paper_index.yaml`, `data/patent_index.yaml`, `data/refresh_status.yaml`; README Master Researcher Index regenerated via `scripts/build_index.py researchers`; README Key Stats + dashboard counts updated.
- **Data confidence posture:** Researcher existence/affiliation/areas high-confidence (public faculty pages, publications); paper venues tagged `[TO VERIFY]` where uncertain; patent entries are clusters/themes, not specific numbers. Startup signals reflect public evidence only; "Likely"/"Watchlist" are analyst judgments, not claims of company formation.
- **Validation:** `scripts/validate_database.py` PASSED (0 errors); all relative links resolve.
- **Sources:** Public faculty/lab pages, arXiv, ISSCC/ISCA/MICRO/ASPLOS/SOSP/OFC/Hot Chips programs, Nature/Science (2023–2025), public founder/spinout records.

---

<!-- Append new refresh entries above this line, newest first. -->
