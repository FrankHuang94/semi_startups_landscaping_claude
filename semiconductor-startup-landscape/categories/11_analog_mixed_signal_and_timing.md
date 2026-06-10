---
category_id: "11"
category_name: "Analog, Mixed Signal & Timing"
primary_datacenter_relevance: "Medium"
vc_relevance: "Medium"
last_refreshed: "2026-06-09"
refresh_count: 1
total_companies: 5
active_companies: 5
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$150M+ [ESTIMATED]"
top_investors: ["Various", "Corporate strategics"]
key_technical_inflections: ["AI clock/jitter requirements", "High-speed SerDes analog", "MEMS timing", "Automated analog design", "Precision timing for distributed AI"]
key_open_questions: ["Can analog/timing startups reach venture scale beyond M&A?", "Does AI-EDA unlock analog design productivity?"]
---

# 11 — Analog, Mixed Signal & Timing

> Quietly critical to AI systems (clocking, jitter, SerDes analog, precision timing). SiTime proved MEMS timing can be venture-scale. Mostly M&A exits; IP leverage matters. See [12](12_eda_ip_and_design_tools.md) for analog-design automation.

## 1. VC Investment Thesis
- **Why now:** AI clusters need ultra-low-jitter clocking, precise timing for synchronization, and bleading SerDes analog; MEMS timing displaces quartz.
- **Venture-scale:** Medium — SiTime (public) is the proof; mostly strategic M&A exits; analog-design automation (AI-EDA) could expand opportunity.
- **Inflections:** AI clocking/jitter, MEMS resonators, precision timing for distributed training, high-speed SerDes analog IP.
- **Acquirers:** Renesas, Skyworks, Microchip, Synopsys, ADI. **Exit:** strategic M&A.
- **Winning startup:** differentiated timing/analog IP with design wins; or AI-driven analog design productivity. **Non-investable:** undifferentiated analog vs. ADI/TI.

## 2. Market Context
- **Structure:** Analog/timing incumbents (ADI, TI, Renesas/IDT, Skyworks/SiTime, Microchip) + thin startup layer + AI-EDA crossover.
- **Segments:** AI server clocking/timing, SerDes IP, sensor interfaces, automotive.
- **Drivers:** Clock-tree complexity, jitter budgets, synchronization across large clusters, IP reuse.
- **Bottlenecks:** Analog design productivity (manual, slow), PVT robustness, IP portability.
- **Competitive:** Incumbent-heavy; startups win via IP + automation + niche performance. **Risks:** long cycles, incumbent scale.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Movellus | US | 2014 | Series B+ | ~$50M+ [TO VERIFY] | Intel Cap, Hortons, Stata | Intelligent clock networks (Aeonic) | AI SoC clocking/PDN | Digitally-managed clocking IP | IP design wins | Medium-High | Active |
| Aura Semiconductor | IN/US | 2012 | Growth | [TO VERIFY] | [TO VERIFY] | Timing + power management | Timing/PMIC | High-performance timing IC | Production | Medium | Active |
| Agile Analog | UK | 2017 | Series B | ~$40M+ [TO VERIFY] | DCVC, Foresight | Configurable analog IP (composa) | SoC analog IP | Automated/configurable analog IP | IP licensing | Medium | Active |
| SiTime | US | 2005 | Public (SITM) | (public) | (public) | MEMS timing | Timing across markets | MEMS resonators vs. quartz | Public; AI DC timing | Medium-High | Active |
| Anlogic / niche analog | Various | — | — | [TO VERIFY] | [TO VERIFY] | Analog/mixed-signal IP | SoC IP | Niche analog | Varies | Low-Medium | Active |

## 4. Company Profiles

### Movellus
- **Status:** Active · **HQ:** San Jose, US · **Founded:** 2014 · **Founders:** Mo Faisal (CEO)
- **Stage:** Series B+ · **Funding:** ~$50M+ [TO VERIFY] · **Investors:** Intel Capital, Hortons Capital, Stata VP · **Website:** movellus.com
- **Primary:** 11 · **Secondary:** 12 IP · **One-Line:** "Aeonic" intelligent clock-network and power-integrity IP that replaces analog PLL/clock trees with digital, scalable clocking for large AI SoCs.
- **Tech:** all-digital clock generation/distribution + droop mitigation, portable across nodes — directly relevant to large GPU/AI die clocking and power integrity. **Differentiation:** digital, synthesizable clocking IP. **Risk:** IP-licensing GTM, incumbent bundling.
- **VC view:** Medium-High; acquirers = Synopsys/Cadence/Renesas. **Data quality:** Medium. **Last updated:** 2026-06-09.

### SiTime (public comparable)
- **Status:** Active (NASDAQ: SITM) · **One-Line:** MEMS-based precision timing displacing quartz; relevant to AI-DC synchronization/jitter. **Why it's here:** the venture-to-public proof point for timing. **Data quality:** High. **Last updated:** 2026-06-09.

> Aura, Agile Analog at table level.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| AI clocking/PDN IP | Medium-High | High | Low-Medium | Medium | Real | Medium-High |
| MEMS timing | Medium | High | Medium | High (SiTime) | Narrow | Medium |
| Configurable analog IP | Medium | High | Low-Medium | Medium | Real | Medium |
| SerDes analog IP | Medium-High | Very High | Medium | High | Narrow | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Intel Capital | Strategic | Movellus | B | Movellus | Clocking IP for AI SoCs |
| DCVC | VC | Agile Analog | B | Agile Analog | Analog automation |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Analog-design-automation academics | UT Austin/CMU | ML for analog design | AI-EDA for analog productivity | Watchlist | Many | 3 | Medium |
| High-speed link labs | Stanford/Berkeley | SerDes/clocking | Link IP talent | Watchlist | Many | 3 | Medium |

## 8. Diligence Questions
- **Technical:** Jitter/PVT performance; node portability; integration?
- **Market:** IP-licensing vs. catalog; AI-SoC clocking pull?
- **Customer:** Tape-out design wins? **Competitive:** vs. Synopsys/Cadence IP, ADI?
- **Financial:** royalty model; gross margin? **Founder:** analog/IP pedigree? **Exit:** EDA/analog incumbent tuck-in?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 5 | 0 | 0 | Initial build; Movellus profile; timing/analog IP coverage | Company sites, public filings |
