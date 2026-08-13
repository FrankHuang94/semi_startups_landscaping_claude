---
category_id: "12"
category_name: "EDA, IP & Design Tools"
primary_datacenter_relevance: "Medium"
vc_relevance: "High"
last_refreshed: "2026-08-13"
refresh_count: 2
total_companies: 13
active_companies: 13
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$300M+ [ESTIMATED]"
top_investors: ["Eclipse", "Lightspeed", "Mayfield", "a16z", "Eurazeo"]
key_technical_inflections: ["AI-for-chip-design (RTL gen, verification)", "LLM agents for EDA", "RISC-V IP disaggregation", "Cloud-native EDA", "AI PCB/analog design"]
key_open_questions: ["Do AI-EDA startups stay independent or get acquired by Synopsys/Cadence?", "Can RISC-V IP unseat Arm in servers?", "Where does AI add the most design value?"]
---

# 12 — EDA, IP & Design Tools

> The most capital-efficient AI-infra thesis: AI-native verification, RTL generation, and design optimization are a wedge into a Synopsys/Cadence duopoly, and RISC-V disaggregates the IP model. Fast software-like iteration with strategic acquirers. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis
- **Why now:** Chip-design demand is exploding (custom silicon boom) while design talent is scarce and EDA productivity lags; LLMs/agents can attack verification, RTL, and debug; RISC-V breaks Arm's IP lock.
- **Venture-scale:** High — software economics, fast iteration, clear acquirers; the wedge is AI-native point tools and RISC-V server IP.
- **Inflections:** AI verification/debug copilots, RTL generation, design-space optimization, cloud-native EDA, AI analog/PCB design.
- **Acquirers:** Synopsys, Cadence, Siemens EDA, Arm. **Exit:** strategic M&A (active acquirers) or scale-up.
- **Winning startup:** AI-native tool that measurably cuts verification/design time, or RISC-V IP with software. **Non-investable:** reimplementing place-and-route from scratch vs. the duopoly.

## 2. Market Context
- **Structure:** EDA duopoly (Synopsys, Cadence) + Siemens EDA; IP (Arm, Synopsys, Imagination) + RISC-V challengers (SiFive, Codasip, Ventana); AI-EDA startups.
- **Segments:** Verification, RTL design, physical design, analog/PCB, IP licensing.
- **Drivers:** Custom-silicon proliferation, design-talent scarcity, design cost/time, AI capability.
- **Bottlenecks:** Verification (~50%+ of effort), analog design productivity, IP integration, foundry PDK access.
- **Competitive:** Synopsys/Cadence acquire aggressively and add AI (DSO.ai, JedAI); startups must show step-change value.
- **Risks:** Incumbent bundling, acquisition-or-die dynamics, data access for AI tools.

### 2026 Update — agentic EDA became the fastest-repricing category in the database (2026-08-13)

The initial build rated AI-EDA "High" on thesis but had almost no funding data. Twelve months of data arrived at once, and the numbers are larger than anything else at comparable stage.

- **Ricursive Intelligence raised $300M Series A at ~$4B post — less than two months after launching** (2026-01-26). Led by **Lightspeed** with DST Global, **NVIDIA's NVentures**, Felicis, Sequoia, Radical AI and 49 Palms. Founded by **Azalia Mirhoseini and Anna Goldie**, the authors of the AlphaChip RL floorplanning work used across four generations of Google TPUs. **This is the single most important research-to-startup conversion in the database this cycle** — the initial build listed Mirhoseini & Goldie on the researcher watchlist; they are now a $4B company. See [17](17_emerging_research_to_startup_pipeline.md) and [../researchers/researcher_to_startup_signal_tracker.md](../researchers/researcher_to_startup_signal_tracker.md).
- **ChipAgents reached $134M with production deployments.** A $50M Series A (Feb 2026) extended by **$60M on 2026-07-29**, with **Micron and MediaTek investing as strategics *and* deploying as customers**. Reported: **6x ARR growth in H1 2026** and **120+ deployments** at semiconductor companies, claiming ~10x productivity in RTL design, debug and verification [TO VERIFY — company-reported].
- **Seed formation continues at pace:** **Architect Labs** emerged from stealth with a **$24M seed** led by Kindred Ventures (2026-07-13) aiming at AI-driven custom chip verification and a "designless semiconductor industry"; **Bronco AI** and **Silimate** showed production metrics at DAC 2026.
- **SiFive re-rated the IP side:** $400M Series G at ~$3.65B (2026-04-09), led by Atreides with **NVIDIA**, Apollo, D1, T. Rowe and Capital Group; ~$970M raised, 10B+ cores shipped, 500+ designs in production. **GlobalFoundries acquired Synopsys's ARC processor IP business** (ARC-V, ARC-Classic, VPX-DSP, NPX NPU), retargeted at physical AI — the IP layer is consolidating and re-segmenting around robotics.
- **Why this repriced so fast:** verification is roughly half of design effort, the workload is text-and-tool-shaped (exactly where agentic models are strongest), and the buyers — Micron, MediaTek, and 100+ others — have an acute shortage of design engineers. Unlike accelerator startups, these companies sell software with software margins into an existing budget line.
- **The risks are unchanged and still real:** Synopsys and Cadence bundle aggressively and can attach AI features to renewals; proprietary design data is the scarce asset and customers are reluctant to share it; and "acquisition-or-die" remains the base case for sub-scale tools. What 2026 showed is that the good outcomes in this category can be very large before that point.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Ricursive Intelligence | US | 2025 | **Series A (2026-01)** | ~$300M+ [TO VERIFY] | Lightspeed, DST, NVentures, Sequoia, Felicis | AI systems for chip design (AlphaChip lineage) | Physical design / full-stack design AI | Founders authored AlphaChip (used in 4 generations of Google TPU) | **~$4B post-money <2 months after launch** | High | Active |
| ChipAgents | US | 2023 | **Series A + ext. (2026-07)** | ~$134M [TO VERIFY] | Micron, MediaTek (strategic) | Agentic AI for RTL design, debug and verification | Verification / RTL | Agents across the EDA workflow; ~10x claimed productivity | **120+ deployments; 6x ARR growth in H1 2026** [TO VERIFY] | High | Active |
| ChipStack | US | 2023 | Seed/A | [TO VERIFY] | [TO VERIFY] | AI verification/test generation | Verification | LLM-driven verification | Early | High | Active |
| Silimate | US | 2023 | Seed | [TO VERIFY] | [TO VERIFY] | AI design copilot/productivity | RTL/design | "Copilot for chip design" | Production metrics shown at DAC 2026 | High | Active |
| Architect Labs | US | 2025 | **Seed (2026-07)** | ~$24M [TO VERIFY] | Kindred Ventures | AI system for custom chip verification | Verification / custom silicon | "Designless semiconductor industry" thesis | Emerged from stealth 2026-07 | Medium-High | Active |
| Bronco AI | US | 2024 | Seed [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | AI verification/debug | Verification | Agentic debug workflows | Production metrics shown at DAC 2026 | Medium-High | Active |
| SiFive | US | 2015 | **Series G (2026-04)** | ~$970M [TO VERIFY] | Atreides, NVIDIA, Apollo, D1, T. Rowe | RISC-V core IP incl. datacenter/AI | RISC-V IP | 10B+ cores shipped; 500+ designs in production | ~$3.65B valuation | High | Active |
| Astrus | US | 2023 | Seed | [TO VERIFY] | [TO VERIFY] | AI analog design automation | Analog design | ML-driven analog layout | Early | Medium-High | Active |
| Quilter | US | 2019 | Series A | ~$10M+ [TO VERIFY] | Benchmark, Plug&Play | AI PCB design (cloud) | PCB design | RL-based autonomous PCB | Early customers | Medium-High | Active |
| PrimisAI | US | 2022 | Seed | [TO VERIFY] | [TO VERIFY] | Generative RTL / agents | RTL design | LLM agents for HDL | Early | Medium | Active |
| Codasip | CZ | 2014 | Series A+ | ~$60M+ [TO VERIFY] | Smart Eureka, Eurazeo | Customizable RISC-V IP + tools | RISC-V IP | Customizable cores (Studio) | Licensing | High | Active |
| SemiDynamics | ES | 2016 | Growth | [TO VERIFY] | [TO VERIFY] | High-perf RISC-V + AI tensor IP | RISC-V AI IP | Vector+tensor RISC-V cores | Licensing | Medium-High | Active |
| Bluespec | US | 2003 | Private | [TO VERIFY] | [TO VERIFY] | RISC-V cores + HLS tools | RISC-V IP/tools | High-level synthesis heritage | Licensing | Medium | Active |

## 4. Company Profiles

### ChipStack
- **Status:** Active · **HQ:** US · **Founded:** 2023 · **One-Line:** AI platform that automates hardware verification — generating testbenches, assertions, and tests from specs to cut the largest cost in chip design.
- **Tech:** LLM/agent pipeline for verification (the ~50%+ of design effort), spec-to-test generation, coverage closure. **Differentiation:** attacks the highest-cost, most-automatable workflow. **Risk:** incumbent (Synopsys/Cadence) AI-verification response; data/PDK access. **VC view:** High; acquirers = Synopsys/Cadence/Siemens. **Data quality:** Low-Medium. **Last updated:** 2026-06-09.

### Codasip
- **Status:** Active · **HQ:** Brno, CZ · **Founded:** 2014 · **One-Line:** Customizable RISC-V processor IP with design-automation tooling (Codasip Studio) enabling domain-specific cores.
- **Tech:** customizable RISC-V cores + CodAL/Studio toolchain for processor customization; high-perf application cores. **Differentiation:** customization tooling + open ISA vs. Arm. **Risk:** RISC-V server adoption pace, funding (has faced restructuring [TO VERIFY]). **VC view:** High; acquirers = IP/EDA incumbents. **Data quality:** Medium. **Last updated:** 2026-06-09.

> Silimate, Astrus, Quilter, PrimisAI (AI-EDA) and SemiDynamics, Bluespec (RISC-V IP) at table level. Note: this is one of the most fluid sub-sectors — re-scan for new AI-EDA seed companies every refresh.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| AI verification/debug | High | High | Low | High | Real | High |
| Generative RTL | High | High | Low | High | Real (early) | Medium-High |
| AI analog/PCB design | Medium-High | High | Low-Medium | Medium | Real | Medium-High |
| RISC-V server IP | Medium-High | Very High | Medium | High (Arm) | High-variance | Medium-High |
| Cloud-native EDA | Medium | Medium | Medium | High | Narrow | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Eclipse / Lightspeed / a16z | VC | AI-EDA seed cohort | Seed–A | New bets | AI-for-hard-tech |
| Benchmark | VC | Quilter | Seed–A | Quilter | Autonomous design |
| Eurazeo / Smart Eureka | VC | Codasip | A–Growth | Codasip | RISC-V IP |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| NVIDIA Research (ML-for-EDA) | NVIDIA | RTL/verif with LLMs | Defines AI-EDA frontier (e.g., chip-design LLMs) | Watchlist | ChipNeMo etc. | 4 | High |
| Berkeley/Stanford agile HW | UC Berkeley/Stanford | Chisel, agile design | Open hardware tooling pipeline | Likely | Chisel/FIRRTL | 4 | Medium |
| Brucek Khailany (NVIDIA) | NVIDIA | ML for chip design | Leading ML-EDA research | Watchlist | Many | 4 | High |

## 8. Diligence Questions
- **Technical:** Measured design-time/quality improvement on real tape-outs? Data/PDK access strategy?
- **Market:** Point-tool vs. platform; wedge into which workflow?
- **Customer:** Paid deployments at real design houses?
- **Competitive:** Survives Synopsys/Cadence AI features + bundling?
- **Financial:** SaaS vs. seat-license economics? **Founder:** EDA + ML credibility?
- **Exit:** acquisition logic/timing for the duopoly; standalone scale potential?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | 0 | Initial build; ChipStack/Codasip profiles; AI-EDA + RISC-V IP coverage | Company sites, trade press |
| 2026-08-13 | Full refresh | 5 (Ricursive, ChipAgents, Architect Labs, Bronco AI, SiFive) | 2 (Silimate, market context) | 0 | Agentic EDA repriced hard: Ricursive Intelligence $300M A at ~$4B (AlphaChip founders — the database's biggest research-to-startup conversion), ChipAgents to $134M with Micron/MediaTek as investors and customers, Architect Labs $24M seed; SiFive $400M G at ~$3.65B; GF acquired Synopsys's ARC IP business | Company releases, DAC 2026, trade press [many TO VERIFY] |
