# Refresh Log

Chronological log of all database refreshes. Newest entries on top. Each entry should record scope, what changed, and the confidence posture of new data.

> **Commit message convention for refreshes:**
> `refresh: [filename] — [brief change summary] (YYYY-MM-DD)`

---

## 2026-11-04 — Full Database Refresh (Refresh #3)

- **Type:** Full refresh (all categories, deal trackers, investors, research pipeline, theses, market map, indexes).
- **Scope:** Public developments from mid-2025 through 2026-11-04. The initial build had missed several major late-2025 events, which this refresh corrects (NVIDIA–Groq, NVIDIA–Enfabrica, Marvell–Celestial AI, Meta–Rivos, the Intel–SambaNova outcome, the Cerebras IPO path).
- **Method:** Seven parallel research passes (compute 01–03; ASIC/networking/optical 04–06; memory/power/packaging/DC infra 07/08/13/16; security/RF/analog/EDA/quantum/auto 09–12/14/15; M&A/funding/exits 20/22/23; investors 21/24; research pipeline 17 + researchers). A coordinator then verified the conflicting or unconfirmed items (Etched rounds, Rain AI, Quantinuum IPO, Tensordyne, Qualcomm–Akeana, Molex–Teramount, ADI–Empower close, AMD–Taalas, Tesla Dojo).
- **Key changes:**
  - **Exits:**
    - NVIDIA–Groq: ~$20B reported licence + leadership hire, Dec 2025.
    - NVIDIA–Enfabrica: >$900M, Sep 2025.
    - Marvell–Celestial AI: closed 2026-02-02.
    - Meta–Rivos.
    - Qualcomm–Ventana, Qualcomm–Alphawave and Qualcomm–Akeana.
    - AMD–Taalas.
    - Microchip–Hailo.
    - NXP–Kinara.
    - ADI–Empower: $1.5B, closed 2026-07-07.
    - Molex–Teramount: closed 2026-05-07.
    - Ciena–Nubis.
    - Tenstorrent–Blue Cheetah.
    - Cadence–ChipStack.
    - SiTime–Renesas timing.
    - SoftBank–Ampere.
    - Unconventional AI–NeuReality: pending.
    - Rain AI: wound down; patents sold to OpenAI [TO VERIFY].
    - Pharrowtech: shut down.
  - **IPOs:** Cerebras (CBRS, 2026-05-14) and Quantinuum (QNT, 2026-06-03).
  - **Funding:** 2025H2–2026 rounds added across all categories. Highlights:
    - Tenstorrent $1.5B at $6.2B
    - FuriosaAI $620M at $2.9B
    - MatX $500M
    - Etched $500M at $5B, then later reported rounds [TO VERIFY]
    - Ayar Labs $500M
    - Lumilens $700M+
    - Xsight >$300M
    - Upscale AI ~$390M
    - SiFive $400M
    - Ricursive $300M
    - Unconventional AI ~$475M seed
    - Positron, Fractile, Rebellions, d-Matrix, Cornelis, Salience, nEye, XCENA, Majestic Labs, Substrate, Lace, ChipAgents, Cognichip, Normal Computing
  - **New companies added**, including: Fractile, Taalas, Quadric, SiFive, Upscale AI, Lumilens, Salience Labs, nEye, OpenLight, XCENA, Majestic Labs, PowerLattice, C2i, xLight, Lace Lithography, Fab2, Ricursive, ChipAgents, Cognichip, Bronco AI, Unconventional AI, Normal Computing, Extropic, Quantinuum, QuEra, Neurophos and Callosum.
  - **Corrections:**
    - Intel Capital's spin-out was reversed in Apr 2025; it is not independent.
    - Recogni was renamed Tensordyne (Sept 2025).
    - Blaize is public.
    - Funding figures corrected for Movellus, Agile Analog, Cysic, Fabric Cryptography and Baya.
    - Bogus "Anlogic" analog row removed.
  - **Theses re-rated:** [INVESTMENT_THESES.md](INVESTMENT_THESES.md) gained a "What Changed" section and a Change column. Interconnect/optics, memory, power and EDA were upgraded, and new cross-cutting theses were added on licence + acqui-hire exits, the memory shortage and valuation discipline.
  - **Market map:** [MARKET_MAP.md](MARKET_MAP.md) gained a 2026 State of the Stack section, refreshed bottleneck notes and a rebuilt acquirer map.
- **Index/count changes:**
  - Company index: 38 → **81** (rebuilt; status vocabulary now includes Public, Acquired (pending), Licensed/Acqui-hired).
  - Investors: 14 → **48**.
  - Researchers: 52 → **62**.
  - Labs: → **44**.
  - Papers: → **38**.
  - Patent clusters: → **30**.
  - Founders: → **32**.
  - Trackers: M&A 10 → **36**; exits 8 → **34**; funding rounds 18 → **56**; strategic investors 12 → **20**.
  - README: Latest Developments section added; dashboard, master indexes and Key Stats regenerated.
  - `data/refresh_status.yaml`: all files current as of 2026-11-04.
- **Scripts:** `scripts/build_index.py` now emits README-ready links (category-number links for companies, `[profile]` links for researchers).
- **Data confidence posture:** Major deals and rounds are `[CONFIRMED]` against company press releases, SEC filings, Reuters, Bloomberg or TechCrunch where possible. Aggregator-only items are tagged `[TO VERIFY]` or `[UNCONFIRMED]`. Examples: Etched's Jul/Aug 2026 valuations, Fab2's round, Lightmatter IPO claims (treated as not having happened), the Ayar Labs extension valuation, Groq's residual valuation and a reported DOJ inquiry.
- **Known gaps (prioritize next refresh):**
  - Web-search quotas cut the research passes short, so these areas were only partly re-verified:
    - Liquid-cooling vendors and thermal M&A (16)
    - IonQ deals, the Infleqtion SPAC, QuEra and Alice & Bob rounds (14)
    - Ambarella and Mobileye items (15)
    - Rapidus, CoWoS capacity and glass substrates (13)
  - Venues for some 2025–2026 papers.
  - No confirmed 2025–26 rounds were found for Fabric Cryptography, EdgeQ, Pivotal Commware, Movellus, Agile Analog, Silimate or Bronco AI; this is a runway-risk flag.
- **Validation:** `scripts/validate_database.py` PASSED (0 errors, 0 warnings); all relative links resolve.
- **Sources:** Company press releases and IR pages (Marvell, Qualcomm, AMD, ADI, Molex, Microchip, NXP, SiTime, Synopsys, Cadence, Tenstorrent), SEC filings (Form D, 8-K), Reuters, Bloomberg, CNBC, TechCrunch, SiliconANGLE, DatacenterDynamics, HPCwire, The Next Platform, TrendForce, Renaissance Capital, Sifted, TNW, Business Wire/PR Newswire. Aggregators (aiweekly, pulse.bot, dealroom) were used only as leads and are tagged accordingly.

> Note on numbering: `refresh_count` inside individual files counts that file's own refreshes (most categories are now at 2). The log-level number (#3) counts database-wide refresh events.

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
