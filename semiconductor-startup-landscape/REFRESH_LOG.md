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

## 2026-08-13 — Full Database Refresh (Refresh #3)

- **Type:** Full refresh across all 17 category files, all 5 deal-tracker files, the researcher/paper/patent watchlists, the data indexes, and the top-level docs.
- **Scope:** Events from roughly 2025 H2 through 2026-08-13 — a period in which the AI-silicon exit environment changed shape.
- **Coverage window note:** the initial build was written from a knowledge base that effectively ended in mid-2025, so this refresh also backfills several 2025 H2 events that were missing rather than merely adding 2026 news.

### Headline changes

**Exits and structural deals (12 added to [deal_tracker/20_ma_tracker.md](deal_tracker/20_ma_tracker.md)):**
- **Cerebras IPO'd** — NASDAQ: CBRS, 2026-05-14, priced at $185, raised ~$5.5B at a ~$56B implied valuation, closed day one +68%. Enabled by a January 2026 OpenAI agreement for up to **750MW**, reported at **>$20B**. FY2026 core revenue guidance ~$855–865M.
- **NVIDIA licensed Groq's LPU technology and hired its founder for ~$20B** (2025-12) — its largest transaction on record — after a similar **>$900M deal for Enfabrica** (2025-09). Both companies continue standalone. A Senate inquiry into HSR avoidance opened in March 2026. **This "licence + hire" structure is now the highest-value exit path in AI silicon and is treated as a distinct outcome class throughout the database.**
- **Marvell** acquired **Celestial AI** (~$3.25B, up to ~$5.5B; closed 2026-02-02) and **XConn** (~$540M; closed 2026-02-10). **Meta** acquired **Rivos** (~$2B). **Qualcomm** closed **Alphawave** ($2.4B). **Microchip** agreed to acquire **Hailo** out of distress. **IonQ** agreed to acquire **SkyWater** (~$1.8B). **GlobalFoundries** bought Synopsys's ARC processor IP business; **Siemens** bought Canopus AI; **d-Matrix** bought GigaIO's SuperNODE/FabreX assets.

**Funding (26 rounds added to [deal_tracker/22_funding_round_tracker.md](deal_tracker/22_funding_round_tracker.md)):** Etched $300M at ~$10.3B · SambaNova ~$1B at ~$11B · Ayar Labs ~$500M at ~$3.75B · MatX $500M · SiFive $400M at ~$3.65B · OLIX $312M at ~$3.3B (largest European semi round on record) · Ricursive Intelligence $300M at ~$4B · d-Matrix $275M · Axelera >$250M · Positron $230M · Eliyan $145M at ~$1B · ChipAgents to $134M cumulative · Tenstorrent ~$800M at ~$3.2B · Groq ~$750M then ~$650M · Rebellions ~$400M pre-IPO · Substrate $100M · Xscape $37M extension, plus seed-stage entries.

**New companies added:** OLIX, Eliyan (promoted), SiFive, Ricursive Intelligence, ChipAgents, Substrate, EdgeCortix, XCENA, Oriole Networks, AheadComputing, Architect Labs, Bronco AI, plus archived-in entries for XConn and Alphawave.

**Companies archived:** Celestial AI (→ Marvell), Rivos (→ Meta), Hailo (→ Microchip, distressed), XConn (→ Marvell), Alphawave (→ Qualcomm), SkyWater (→ IonQ).

**Research-to-startup conversions ([categories/17](categories/17_emerging_research_to_startup_pipeline.md), [researchers/researcher_to_startup_signal_tracker.md](researchers/researcher_to_startup_signal_tracker.md)):**
- **AI-EDA watch-item → Ricursive Intelligence.** Azalia Mirhoseini and Anna Goldie (AlphaChip) raised $300M at ~$4B less than two months after launch. They were on this database's researcher watchlist at the initial build. **Lag from watchlist to $4B: under a year.**
- **Photonic compute → OLIX**; **cryo-CMOS → FrostByte** (QuTech/TU Delft spinout).

### Analytical changes (not just data)

- **New outcome class — "licence + hire."** Added to the M&A tracker, the exit tracker's pattern summary, the strategic investor usage guide, and category theses. The underwriting instruction is to model three separate values: proceeds to the company, consideration/retention to the team, and residual value of what remains.
- **New competitive risk — lab-commissioned merchant ASICs.** OpenAI and Broadcom unveiled **"Jalapeño"** (2026-06-24), taken from design to tape-out in ~9 months with a claimed ~50% cost advantage, inside a 10GW program. "Why not just commission a Broadcom ASIC?" is now a first-meeting question for accelerator startups.
- **New capital-source class — quant/prop and sovereign.** Jane Street, Jump Trading, Hudson River Trading and Situational Awareness LP now lead silicon rounds; Korea's National Growth Fund, the UK sovereign AI venture fund, QIA and MGX supply state capital. Added to [deal_tracker/21_vc_investor_tracker.md](deal_tracker/21_vc_investor_tracker.md) with syndicate-signal rules.
- **New failure mode — liquidity mistiming.** The Hailo post-mortem (real silicon, 300+ customers, ~$425M raised, still forced into a distressed sale) is now the reference case for edge inference and is reflected in category 03's thesis.
- **Category verdicts:** [06 Optical/CPO](categories/06_optical_interconnect_and_cpo.md) is the refresh's validated call (control exit + volume production + capital); [12 EDA/IP](categories/12_eda_ip_and_design_tools.md) is the fastest-repricing category; [03 Edge Inference](categories/03_edge_inference_chips.md) is downgraded in practice by the Hailo outcome; [02 Inference](categories/02_inference_accelerators.md) is simultaneously the most validated and the most crowded.

### Data confidence posture

Most figures remain `[TO VERIFY]`. Specific cautions for this cycle: (1) several rounds are **first closes or extensions** (SambaNova's Series F, ChipAgents' Series A, Xscape's Series A) and are widely mis-stated as full rounds; (2) the Celestial AI headline value includes large **milestone-contingent** consideration — the ~$3.25B upfront figure is the correct comparable; (3) **FuriosaAI's Series D is in market, not closed** — tagged `[UNCONFIRMED]`; (4) Blaize's FY2026 revenue guidance implies a very large ramp from a $2.7M quarter and is guidance, not fact; (5) PsiQuantum's cumulative funding is reported inconsistently across sources and needs reconciliation; (6) Tenstorrent takeover interest from Intel/Qualcomm is **rumor** and tagged as such.

### Known gaps to close at the next refresh

- No verifiable 2026 financing data surfaced for **Rain AI, Sagence, Mythic, Numem** or several analog/timing entries — marked `[NO PUBLIC DATA]` rather than assumed unchanged. Silence in capital-hungry categories warrants an active check.
- **Lightmatter has no disclosed round since its 2024 Series D** while peers raised heavily; establish cash position and next-round status.
- Chinese AI-silicon companies (Horizon Robotics, Black Sesame, SemiDrive, Cambricon, Biren, Moore Threads) remain under-covered relative to their market weight.
- Ayar Labs' Series E lead and exact valuation, Axelera's round label, and the composition of Etched's ">$1B in contracts" all need primary-source confirmation.

### Method note

Primary research for this refresh was conducted through web search against public press releases, company announcements, acquirer disclosures and trade press; several source domains were unreachable from the research environment, so figures rest on search-result summaries and are tagged accordingly. No private or non-public data was used.

**Validation:** `scripts/validate_database.py` PASSED; README master indexes regenerated via `scripts/build_index.py`.

---

<!-- Append new refresh entries above this line, newest first. -->
