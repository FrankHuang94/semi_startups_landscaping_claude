---
category_id: "12"
category_name: "EDA, IP & Design Tools"
primary_datacenter_relevance: "Medium"
vc_relevance: "High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 13
active_companies: 12
archived_companies: 1
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$850M+ [ESTIMATED]"
top_investors: ["Lightspeed", "Sequoia", "Bessemer", "Matter Venture Partners", "Seligman Ventures", "Mayfield", "Lux", "Samsung Catalyst", "NVentures", "Eurazeo"]
key_technical_inflections: ["Agentic AI for RTL/verification/debug", "RL/foundation models for physical design (AlphaChip lineage)", "AI analog/PCB design", "RISC-V IP consolidation", "EDA + simulation convergence (Synopsys–Ansys)"]
key_open_questions: ["Do AI-EDA startups stay independent at $1B+ valuations or get acquired by Synopsys/Cadence/Siemens?", "Is ARR real and durable vs. pilots?", "Can RISC-V IP vendors survive as standalone companies?"]
---

# 12 — EDA, IP & Design Tools

> The 2026 breakout category. AI-native chip design went from seed experiments to a funding wave: Ricursive Intelligence ($300M Series A at $4B, Jan 2026), ChipAgents ($134M cumulative Series A, Jul 2026), Cognichip ($60M Series A, Apr 2026), Normal Computing ($50M, Mar 2026). Incumbents are buying (Cadence–ChipStack, Nov 2025) and reshaping portfolios (Synopsys closed Ansys and is selling ARC processor IP to GlobalFoundries). Standalone RISC-V IP is consolidating (Codasip sale process). See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis
- **Why now:** Custom-silicon demand (hyperscaler ASICs, sovereign AI) is exploding while design talent is scarce; LLM agents now credibly automate RTL generation, testbench/assertion creation, and debug; RL-based physical design (AlphaChip lineage) is being commercialized.
- **Venture-scale:** High — software economics; 2026 valuations price in platform outcomes (Ricursive $4B post [CONFIRMED]). Risk has shifted from "does it work" to "is ARR durable vs. incumbent bundling".
- **Inflections:** agentic verification/debug, spec-to-RTL, AI physical design/floorplanning, "AI designing AI chips" closed loops, AI analog/PCB design, RISC-V IP consolidation.
- **Acquirers:** Synopsys, Cadence, Siemens EDA, Keysight, Arm, NVIDIA (partner/investor), foundries (GlobalFoundries bought ARC IP). **Exit:** strategic M&A (Cadence–ChipStack precedent) or scale-up; IPO plausible for top AI-EDA platforms long-term.
- **Winning startup:** AI-native tool that measurably cuts verification/design time with paid deployments at many design houses; or RL/foundation-model design platform with frontier talent. **Non-investable:** reimplementing place-and-route from scratch vs. the duopoly; sub-scale RISC-V core vendors.

## 2. Market Context
- **Structure:** EDA duopoly (Synopsys, Cadence) + Siemens EDA; IP (Arm, Synopsys, Cadence, Imagination) + RISC-V vendors (SiFive, Andes, MIPS/GlobalFoundries, SemiDynamics); AI-EDA startup wave.
- **Incumbent moves (2025–26):**
  - **Synopsys–Ansys** ($35B) completed in 2025 (Jul 2025 [TO VERIFY]) — EDA + multiphysics simulation convergence.
  - **Synopsys → GlobalFoundries:** definitive agreement (Jan 14 2026) to sell the Processor IP Solutions business (ARC-V/ARC CPU/DSP/NPU IP, MetaWare, ASIP Designer); ARC teams to integrate into GF's MIPS; close expected 2H 2026 [CONFIRMED].
  - **Cadence–ChipStack:** agreement announced Nov 10 2025 (AI verification, ~20 staff; terms undisclosed) [CONFIRMED].
  - **Qualcomm–Alphawave Semi:** ~$2.4B, completed mid-Dec 2025, ~a quarter ahead of schedule; Tony Pialis heads Qualcomm's data-center unit [CONFIRMED] (connectivity IP; tracked in [04](04_custom_asic_and_chiplets.md)/[05](05_networking_and_interconnect.md)).
  - **NVIDIA:** expanded partnerships with AI-EDA startups (ChipAgents) and NVentures investment in Ricursive [TO VERIFY].
- **Segments:** Verification, RTL design, physical design, analog/PCB, IP licensing.
- **Drivers:** Custom-silicon proliferation, talent scarcity, design cost/time, LLM/agent capability.
- **Bottlenecks:** Verification (~50%+ of effort), analog productivity, IP integration, PDK/data access for AI training.
- **Competitive:** Synopsys (AgentEngineer), Cadence (JedAI / silicon agents) and Siemens ship their own AI; startups must show step-change value and integrate with incumbent simulators.
- **Risks:** Incumbent bundling, acquisition-or-die dynamics, valuation froth, data access.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Ricursive Intelligence | US (Palo Alto) | 2025 | Series A | ~$335M [CONFIRMED] ($35M seed Dec 2025 + $300M Series A Jan 2026 at $4B post) | Lightspeed (A), Sequoia (seed); NVentures, DST, Felicis [TO VERIFY] | AI lab for self-improving chip design (RL/foundation models) | Chip design end-to-end | AlphaChip founders (Goldie, Mirhoseini) | Pre-product/early; unicorn in ~4 months | Very High | Active |
| ChipAgents | US (Santa Barbara/Santa Clara) [TO VERIFY] | 2023 [TO VERIFY] | Series A (A/A1/A2) | ~$137M [CONFIRMED] ($134M cumulative Series A) | Bessemer (A), Matter Venture Partners (A1), A2 incl. Micron, MediaTek, B Capital, Ericsson | Agentic AI for RTL, testbench, verification, debug | Design & verification teams | Multi-agent EDA platform; NVIDIA partnership | 6x ARR growth H1 2026; >120 semiconductor companies (company claim) | Very High | Active |
| Cognichip | US (Redwood City) | 2024 | Series A | ~$93M [CONFIRMED] | Seligman Ventures (A); Mayfield, Lux, FPV, SBI | "Artificial Chip Intelligence" physics-informed design AI | Chip design platform | Physics-informed foundation model; Lip-Bu Tan on board [TO VERIFY] | Claims >75% cost / >50% time reduction (company claim) | High | Active |
| Normal Computing | US (New York) | 2022 | Strategic/Growth | ~$85M+ [CONFIRMED] (incl. $50M Mar 2026 led by Samsung Catalyst) | Samsung Catalyst; Galvanize, Brevan Howard MVF, ArcTern | AI EDA software + CN101 thermodynamic chip | Verification/design + gen-AI inference | EDA used by >half of top-10 chipmakers (company claim) | Cross-listed — primary in [14](14_quantum_neuromorphic_and_non_von_neumann.md) | High | Active |
| Bronco AI | US | 2022–23 [TO VERIFY] | Pre-seed/Seed | ~$0.5M+ [TO VERIFY] | Y Combinator, Glasswing, FJOR | AI agents for verification & debug ("Bronco Debug") | DV/debug | Full-chip SoC debug in <15 min (company claim) | Early revenue (~$0.9M 2024, unverified) | Medium-High | Active |
| Silimate | US | 2023 | Seed | [TO VERIFY] | [TO VERIFY] | AI design copilot/PPA | RTL/design | "Copilot for chip design" | Early; no 2025–26 news found | Medium | Active |
| Astrus | CA (Toronto/Waterloo) | 2023 | Seed | ~$8M [TO VERIFY] (Sept 2025) | [TO VERIFY] | Physics-aware AI for analog layout | Analog design | RL generating candidate layouts | Early | Medium-High | Active |
| Quilter | US | 2019 | Series A+ | ~$10M+ [TO VERIFY] | Benchmark, Plug&Play | AI PCB design (cloud) | PCB design | RL-based autonomous PCB | Early customers | Medium-High | Active |
| PrimisAI | US | 2022 | Seed | [TO VERIFY] | [TO VERIFY] | Generative RTL / agents | RTL design | LLM agents for HDL | Early | Medium | Active |
| Codasip | CZ | 2014 | In sale process | ~€119M grants + equity (~$140M) [CONFIRMED, company] | Smart Eureka, Eurazeo | Customizable RISC-V IP + Studio tools | RISC-V IP | Customizable cores | Board launched sale Jul 2025; low-end RISC-V business sold to onsemi (~$14.5M, reported Oct 2026) [UNCONFIRMED] | Medium | Active (partial divestiture) |
| SemiDynamics | ES | 2016 | Growth | [TO VERIFY] (SK hynix strategic investment, Apr 2026 [TO VERIFY]) | SK hynix (strategic) | RISC-V + AI tensor IP; memory-centric inference chip | RISC-V AI IP / chips | Vector+tensor RISC-V; moving toward own inference silicon | Licensing; SK hynix partnership | Medium-High | Active |
| Bluespec | US | 2003 | Private | [TO VERIFY] | [TO VERIFY] | RISC-V cores + HLS tools | RISC-V IP/tools | High-level synthesis heritage | Licensing | Low-Medium | Active |
| ChipStack | US (Seattle) | 2023 | Acquired | [TO VERIFY] | [TO VERIFY] | AI verification/test generation | Verification | LLM-driven verification | Acquired by Cadence (announced Nov 10 2025) [CONFIRMED] | Archived | Acquired |

## 4. Company Profiles

### Ricursive Intelligence (new)
- **Status:** Active · **HQ:** Palo Alto, US · **Founded:** 2025 · **Founders:** Anna Goldie (CEO), Azalia Mirhoseini (CTO) — co-creators of Google's AlphaChip
- **Stage:** Series A · **Total Funding:** ~$335M [CONFIRMED] · **Rounds:** $35M seed (Dec 2025) led by Sequoia at ~$750M post [TO VERIFY]; $300M Series A (announced Jan 26 2026) led by Lightspeed at $4B post-money [CONFIRMED — company PR]. One secondary report cites $500M incl. secondaries [UNCONFIRMED]. Other investors reportedly NVentures, DST Global, Felicis [TO VERIFY].
- **Primary:** 12 · **One-Line:** Frontier AI lab building self-improving AI for chip design ("AI designing the chips that train AI"), from RL floorplanning toward full-flow automation.
- **Risk:** valuation far ahead of revenue; needs incumbent-tool interoperability and real tape-out proof. **VC view:** Very High-variance; strategic interest from NVIDIA/hyperscalers. **Data quality:** Medium-High. **Last updated:** 2026-11-04.

### ChipAgents (new)
- **Status:** Active · **HQ:** California, US [TO VERIFY city] · **Founder/CEO:** William Wang (UCSB) [TO VERIFY]
- **Funding:** $21M Series A (Oct 2025, Bessemer-led; total then $24M) → $50M Series A1 (Feb 2026, Matter Venture Partners-led; total $74M) → $60M Series A2 (Jul 29 2026; Series A total $134M) [CONFIRMED — BusinessWire/DCD/Quartz]. Investors incl. Micron, MediaTek, Ericsson, B Capital, Bessemer, ScOp.
- **One-Line:** Agentic AI platform automating RTL generation, testbench creation, debugging and verification; expanded NVIDIA partnership (Jul 2026).
- **Traction (company claim):** 6x ARR growth in H1 2026; deployments at >120 semiconductor companies. **VC view:** Very High (leading agentic-EDA pure play). **Data quality:** Medium-High. **Last updated:** 2026-11-04.

### Cognichip (new)
- **Status:** Active · **HQ:** Redwood City, US · **Founded:** 2024 · **Funding:** $60M oversubscribed Series A (Apr 1 2026) led by Seligman Ventures; total ~$93M [CONFIRMED — BusinessWire]; participants incl. Mayfield, Lux, FPV, SBI Investment. Intel CEO Lip-Bu Tan and Seligman's Umesh Padval reported joining board [TO VERIFY].
- **One-Line:** "Artificial Chip Intelligence" — physics-informed foundation model for semiconductor design; claims >75% cost and >50% schedule reduction (company claim). **VC view:** High. **Data quality:** Medium. **Last updated:** 2026-11-04.

### Codasip
- **Status:** Active (partial divestiture) · **HQ:** Brno, CZ · **Founded:** 2014 · **One-Line:** Customizable RISC-V processor IP with Codasip Studio tooling.
- **2025–26:** Board launched an expedited sale process (Jul 1 2025) for the whole company or its four separable units (Studio, two RISC-V portfolios, high-performance application cores) [CONFIRMED — Codasip PR]. onsemi reportedly acquired the low-end RISC-V processor business for ~$14.5M (reported Oct 2026, citing Czech outlet e15) [UNCONFIRMED]; earlier GlobalFoundries speculation (Apr 2026) unconfirmed. Disposition of remaining units unclear [TO VERIFY].
- **VC view:** Medium (signal: sub-scale RISC-V IP is hard to monetize). **Data quality:** Medium. **Last updated:** 2026-11-04.

### ChipStack (archived)
- **Status:** Acquired · **HQ:** Seattle, US · Cadence announced agreement to acquire (Nov 10 2025); ~20 employees joining; terms undisclosed; built on prior Xcelium/Jasper integration [CONFIRMED — Cadence blog]. **Last updated:** 2026-11-04.

> Normal Computing (primary [14](14_quantum_neuromorphic_and_non_von_neumann.md)), Bronco AI, Silimate, Astrus, Quilter, PrimisAI (AI-EDA) and SemiDynamics, Bluespec (RISC-V IP) at table level. This remains the most fluid sub-sector — re-scan for new AI-EDA seed companies every refresh (2026 seed rounds of $18–24M for unnamed agentic-design and formal-verification startups were reported [UNCONFIRMED]).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Agentic verification/debug | Very High | High | Low | High | Real (proven ARR growth) | High (valuations rich) |
| Generative RTL / spec-to-RTL | High | High | Low | High | Real | High |
| AI physical design / full-flow (RL, foundation models) | High | Very High | Medium (compute) | High | High-variance, mega-rounds | High |
| AI analog/PCB design | Medium-High | High | Low-Medium | Medium | Real | Medium-High |
| RISC-V IP (standalone) | Medium | Very High | Medium | High (Arm, consolidation) | Narrow (consolidating) | Medium-Low |
| Cloud-native EDA | Medium | Medium | Medium | High | Narrow | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Lightspeed / Sequoia | VC | Ricursive Intelligence | Seed–A | $300M A at $4B (Jan 2026) | Frontier AI-for-chips lab |
| Bessemer / Matter Venture Partners / B Capital | VC | ChipAgents | A | A1 (Feb 2026), A2 (Jul 2026) | Agentic EDA |
| Micron / MediaTek / Ericsson | Strategic | ChipAgents | A | Series A tranches | Customers as investors |
| Seligman Ventures / Mayfield / Lux | VC | Cognichip | A | $60M A (Apr 2026) | Physics-informed design AI |
| Samsung Catalyst | Strategic | Normal Computing | Growth | $50M (Mar 2026) | AI-EDA + thermodynamic HW |
| NVentures (NVIDIA) | Strategic | Ricursive [TO VERIFY]; ChipAgents partner | A | 2026 | NVIDIA seeding the design ecosystem |
| SK hynix | Strategic | SemiDynamics | Growth | Apr 2026 [TO VERIFY] | Memory-centric RISC-V inference |
| Benchmark | VC | Quilter | Seed–A | — | Autonomous PCB |
| Eurazeo / Smart Eureka | VC | Codasip | A–Growth | Sale process | RISC-V IP |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Anna Goldie / Azalia Mirhoseini | Ricursive (ex-Google DeepMind; Mirhoseini also Stanford) | RL for chip floorplanning (AlphaChip) | Founded the highest-valued AI-EDA startup | Confirmed (Ricursive) | AlphaChip (Nature 2021) | 5 | High |
| William Wang | UCSB / ChipAgents [TO VERIFY] | LLM agents for hardware | Agentic EDA leader | Confirmed (ChipAgents) | Many | 5 | Medium |
| NVIDIA Research (ML-for-EDA) | NVIDIA | RTL/verif with LLMs | Defines AI-EDA frontier (ChipNeMo etc.) | Watchlist | ChipNeMo etc. | 4 | High |
| Brucek Khailany (NVIDIA) | NVIDIA | ML for chip design | Leading ML-EDA research | Watchlist | Many | 4 | High |
| Berkeley/Stanford agile HW | UC Berkeley/Stanford | Chisel, agile design | Open hardware tooling pipeline | Likely | Chisel/FIRRTL | 4 | Medium |

## 8. Diligence Questions
- **Technical:** Measured design-time/quality improvement on real tape-outs (not benchmarks)? Integration with Xcelium/VCS/Jasper/Fusion? Data/PDK access strategy?
- **Market:** Point-tool vs. platform; which workflow is the wedge; per-seat vs. per-agent/usage pricing?
- **Customer:** Paid production deployments vs. pilots; logo concentration; ARR quality (company ARR claims are unaudited)?
- **Competitive:** Survives Synopsys/Cadence/Siemens agentic features + bundling; what happens when incumbents restrict tool APIs?
- **Financial:** Valuation vs. ARR multiple (Ricursive $4B pre-revenue); compute costs for RL/foundation-model training? **Founder:** EDA + ML credibility?
- **Exit:** Acquisition logic/price ceiling for the duopoly at $1B+ valuations; standalone/IPO path?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | 0 | Initial build; ChipStack/Codasip profiles; AI-EDA + RISC-V IP coverage | Company sites, trade press |
| 2026-11-04 | Full (Refresh #3) | 5 (Ricursive, ChipAgents, Cognichip, Normal Computing [cross-list], Bronco AI) | 4 (Codasip, SemiDynamics, Astrus, Quilter/others re-checked) | 1 (ChipStack → Cadence) | AI-EDA funding wave: Ricursive $300M A @ $4B (Jan 2026); ChipAgents A total $134M (Jul 2026); Cognichip $60M A (Apr 2026); Normal Computing $50M (Mar 2026). Cadence–ChipStack (Nov 2025); Synopsys→GF ARC IP sale (Jan 2026); Qualcomm–Alphawave closed (Dec 2025); Codasip sale process + reported onsemi partial buy [UNCONFIRMED] | Ricursive PR / Crunchbase News, BusinessWire (ChipAgents, Cognichip), SiliconANGLE (Normal), Cadence blog, Synopsys newsroom, Codasip PR, Alliance News/Law360 (Alphawave) |
