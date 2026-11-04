---
category_id: "11"
category_name: "Analog, Mixed Signal & Timing"
primary_datacenter_relevance: "Medium"
vc_relevance: "Medium"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 7
active_companies: 7
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$110M+ private [ESTIMATED] (excl. public SiTime)"
top_investors: ["Celesta", "Intel Capital", "MESH", "SK hynix", "OMERS Ventures", "Endiya Partners"]
key_technical_inflections: ["AI-DC clocking consolidation (SiTime + Renesas timing)", "AI clock/jitter requirements", "High-speed SerDes / D2D analog", "MEMS timing", "AI-automated analog design", "Precision timing for distributed AI"]
key_open_questions: ["Can analog/timing startups reach venture scale beyond M&A?", "Does AI-EDA unlock analog design productivity?", "Does SiTime-Renesas squeeze or validate timing startups?"]
---

# 11 — Analog, Mixed Signal & Timing

> Quietly critical to AI systems (clocking, jitter, SerDes/D2D analog, precision timing). 2026's defining event: SiTime bought Renesas' timing business (~$1.5B cash + stock, closed Jul 1 2026) — ~75% of the acquired revenue is AI-datacenter/comms, confirming timing as an AI-infrastructure bottleneck. Analog/D2D IP remains an acqui-target (Tenstorrent–Blue Cheetah, 2025). See [12](12_eda_ip_and_design_tools.md) for analog-design automation and [04](04_custom_asic_and_chiplets.md) for D2D/chiplet IP.

## 1. VC Investment Thesis
- **Why now:** AI clusters need ultra-low-jitter clocking, precise synchronization, and leading-edge SerDes/D2D analog; MEMS timing displaces quartz; AI-driven analog design tools are finally attracting capital.
- **Venture-scale:** Medium — SiTime (public) is the proof point and now a consolidator; mostly strategic M&A exits; analog-design automation (AI-EDA) and India's analog-design ecosystem are the new seed-stage pipeline.
- **Inflections:** AI clocking/jitter, MEMS resonators, precision timing for distributed training, D2D/SerDes analog IP, ML-assisted analog layout & sizing.
- **Acquirers:** SiTime (now acquisitive), Renesas, Skyworks, Microchip, ADI, TI, onsemi, Synopsys/Cadence, AI-chip vendors buying analog teams (Tenstorrent–Blue Cheetah). **Exit:** strategic M&A.
- **Winning startup:** differentiated timing/clocking/analog IP with AI-SoC design wins; or AI-driven analog design productivity. **Non-investable:** undifferentiated analog vs. ADI/TI.

## 2. Market Context
- **Structure:** Analog/timing incumbents (ADI, TI, SiTime + ex-Renesas/IDT timing, Skyworks, Microchip) + thin startup layer + AI-EDA crossover.
- **Key 2025–26 deals:**
  - **SiTime–Renesas timing:** announced Feb 4 2026; closed Jul 1 2026 for ~$1.5B cash + 3,558,691 SiTime shares; acquired business expected ~$300M revenue (12 months post-close) at ~70% GM, ~75% AI-datacenter-comms; $900M Wells Fargo debt financing [CONFIRMED — SEC 8-K].
  - **Tenstorrent–Blue Cheetah Analog Design:** announced Jul 1 2025, terms undisclosed; BlueLynx D2D (BoW/UCIe) IP brought in-house [CONFIRMED] (tracked in [04](04_custom_asic_and_chiplets.md)).
  - **onsemi–Aura Semiconductor:** onsemi agreed (Sept 2025) to acquire rights to Aura's Vcore power technology; close expected Q4 2025 [TO VERIFY].
- **Segments:** AI server clocking/timing, SerDes/D2D IP, power-management analog, sensor interfaces, automotive.
- **Drivers:** Clock-tree complexity, jitter budgets, synchronization across large clusters, IP reuse, analog-engineer scarcity.
- **Bottlenecks:** Analog design productivity (manual, slow), PVT robustness, IP portability.
- **Competitive:** Incumbent-heavy and consolidating; startups win via IP + automation + niche performance. **Risks:** long cycles, incumbent scale.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Movellus | US | 2014 | Series B | ~$29–35M [TO VERIFY] (corrected; $23M Series B Sept 2022 led by MESH w/ SK hynix) | MESH, SK hynix, Intel Capital, Stata VP | Intelligent clock networks / PDN IP (Aeonic) | AI SoC clocking/PDN | Digitally-managed clocking + droop IP | IP design wins; no 2025–26 round found | Medium-High | Active |
| Aura Semiconductor | IN (Bengaluru)/US | 2010–12 [TO VERIFY] | Series A+ | [TO VERIFY] | Celesta Capital | Timing + power management ICs | Timing/PMIC | High-performance timing IC | onsemi acquiring Vcore power-tech rights (Sept 2025) [TO VERIFY] | Medium | Active |
| Agile Analog | UK (Cambridge) | 2017 | Series A | ~$24M+ [TO VERIFY] (corrected: $5M pre-A 2019 + $19M 2021 led by OMERS) | OMERS Ventures, Delin, firstminute, In-Q-Tel [TO VERIFY] | Configurable analog IP (Composa) | SoC analog IP | Automated/configurable analog IP | IP licensing; no 2025–26 round found | Medium | Active |
| Sphere Semi | US | [TO VERIFY] | Seed/A | ~$20M [TO VERIFY] ($12M round) | [TO VERIFY] | AI-automated analog chip design | Analog design | AI-driven analog flow | Early | Medium | Active |
| Maieutic Semiconductors | IN (Bengaluru) | [TO VERIFY] | Seed+ | ~$10M [TO VERIFY] ($4.15M seed Jul 2025; $6M Oct 2025) | Endiya Partners, Exfinity Venture Partners | AI assistant for analog design | Analog design teams | GenAI analog sizing/assistant; 2026 rollout | Early | Medium | Active |
| Vervesemi Microelectronics | IN | [TO VERIFY] | Series A | ~$10M (Feb 2026) [TO VERIFY] | [TO VERIFY] | ML-enhanced analog signal-chain ICs | Industrial/aero/auto | ML-calibrated analog | Early | Low-Medium | Active |
| SiTime | US | 2005 | Public (SITM) | (public) | (public) | MEMS timing + (ex-Renesas) clocking | Timing across markets; AI-DC | MEMS resonators + full clock-tree portfolio | Closed Renesas timing deal Jul 2026 [CONFIRMED] | Medium-High | Active (Public) |

## 4. Company Profiles

### SiTime (public comparable → consolidator)
- **Status:** Active (NASDAQ: SITM) · **One-Line:** MEMS-based precision timing displacing quartz; with the Renesas timing acquisition now a full clocking supplier (clock generators, buffers, network synchronizers, jitter attenuators) for AI datacenters.
- **2026:** Acquired Renesas' timing business — announced Feb 4 2026, closed Jul 1 2026; ~$1.5B cash + 3,558,691 shares (vs. ~4.13M announced, after adjustments); expected ~$300M revenue in first 12 months at ~70% GM; Renesas CEO Hidetoshi Shibata to join SiTime board; MOU to put SiTime MEMS resonators into Renesas embedded products [CONFIRMED — SEC 8-K/8-K/A]. Stated long-term goal: $1B revenue.
- **Why it's here:** the venture-to-public proof point for timing, now the most likely acquirer of timing/clocking startups. **Data quality:** High. **Last updated:** 2026-11-04.

### Movellus
- **Status:** Active · **HQ:** San Jose, US · **Founded:** 2014 · **Founders:** Mo Faisal (CEO)
- **Stage:** Series B · **Funding:** ~$29–35M [TO VERIFY] (prior entry of ~$50M+ corrected downward; aggregators: ZoomInfo $29.1M, CB Insights $35.25M) · **Investors:** MESH (Series B lead, 2022), SK hynix, Intel Capital, Stata VP · **Website:** movellus.com
- **Primary:** 11 · **Secondary:** 12 IP · **One-Line:** "Aeonic" intelligent clock-network and power-integrity IP (Generate, Insight, PDN IQ, Droop, Power) for large AI SoCs.
- **Tech:** all-digital clock generation/distribution + droop mitigation and on-die telemetry, portable across nodes. **Risk:** IP-licensing GTM, incumbent bundling; no new round found since 2022 — check runway [TO VERIFY].
- **VC view:** Medium-High; acquirers = Synopsys/Cadence/SiTime/Renesas. **Data quality:** Medium. **Last updated:** 2026-11-04.

> Aura, Agile Analog, Sphere Semi, Maieutic, Vervesemi at table level. Astrus (AI analog layout, $8M Sept 2025) is tracked in [12](12_eda_ip_and_design_tools.md). Blue Cheetah (acquired by Tenstorrent, Jul 2025) is tracked in [04](04_custom_asic_and_chiplets.md). The prior placeholder row "Anlogic / niche analog" was removed (Anlogic is a Chinese FPGA vendor, not an analog startup).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| AI clocking/PDN IP | High | High | Low-Medium | Medium-High (SiTime now full-line) | Real | Medium-High |
| MEMS timing | Medium-High | High | Medium | High (SiTime) | Narrow | Medium-Low |
| Configurable analog IP | Medium | High | Low-Medium | Medium | Real | Medium |
| AI analog-design automation | Medium-High | High | Low | Medium | Real (early; India + US seed wave) | Medium-High |
| SerDes / D2D analog IP | High | Very High | Medium | High (acquired into AI-chip cos.) | Narrow; acqui-hire exits | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| MESH / SK hynix / Intel Capital | VC / Strategic | Movellus | A–B | Movellus B (2022) | Clocking IP for AI SoCs |
| Celesta Capital | VC | Aura Semiconductor | A | — | India–US analog |
| OMERS Ventures | VC | Agile Analog | A | 2021 | Analog automation |
| Endiya / Exfinity | VC (India) | Maieutic | Seed | Oct 2025 | AI-for-analog design |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Analog-design-automation academics | UT Austin/CMU | ML for analog design | AI-EDA for analog productivity | Watchlist | Many | 3 | Medium |
| High-speed link labs | Stanford/Berkeley | SerDes/clocking | Link IP talent (Blue Cheetah lineage) | Confirmed (exit) | Many | 3 | Medium |

## 8. Diligence Questions
- **Technical:** Jitter/PVT performance; node portability; integration with D2D/UCIe?
- **Market:** IP-licensing vs. catalog; AI-SoC clocking pull; post-SiTime/Renesas competitive map?
- **Customer:** Tape-out design wins? **Competitive:** vs. SiTime full-line, Synopsys/Cadence IP, ADI/TI?
- **Financial:** royalty model; gross margin; runway (several names show no round since 2021–22)? **Founder:** analog/IP pedigree? **Exit:** SiTime/EDA/analog incumbent tuck-in; AI-chip acqui-hire?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 5 | 0 | 0 | Initial build; Movellus profile; timing/analog IP coverage | Company sites, public filings |
| 2026-11-04 | Full (Refresh #3) | 3 (Sphere Semi, Maieutic, Vervesemi) | 4 (SiTime, Movellus, Agile Analog, Aura) | 0 (1 placeholder row removed) | SiTime closed ~$1.5B Renesas timing acquisition (Jul 1 2026); Tenstorrent–Blue Cheetah (Jul 2025, cross-ref 04); onsemi–Aura Vcore rights (Sept 2025); Movellus & Agile Analog funding corrected downward; AI-analog-design seed wave added | SEC 8-K (SiTime), SiTime IR, Tenstorrent/DCD (Blue Cheetah), BusinessWire/Intel Capital (Movellus), YourStory/Techstory (India analog), Pulse2 |
