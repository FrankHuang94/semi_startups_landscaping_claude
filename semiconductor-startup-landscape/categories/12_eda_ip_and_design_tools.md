---
category_id: "12"
category_name: "EDA, IP & Design Tools"
primary_datacenter_relevance: "Medium"
vc_relevance: "High"
last_refreshed: "2026-06-09"
refresh_count: 1
total_companies: 8
active_companies: 8
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

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| ChipStack | US | 2023 | Seed/A | [TO VERIFY] | [TO VERIFY] | AI verification/test generation | Verification | LLM-driven verification | Early | High | Active |
| Silimate | US | 2023 | Seed | [TO VERIFY] | [TO VERIFY] | AI design copilot/productivity | RTL/design | "Copilot for chip design" | Early | High | Active |
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
