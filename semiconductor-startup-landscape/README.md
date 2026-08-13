# AI Semiconductor Startup Landscape Database

**Purpose:** A VC-style, indexed, independently refreshable knowledge base tracking the global startup, research, funding, and M&A ecosystem in semiconductors relevant to AI datacenter and adjacent edge/automotive markets.

- **Maintained by:** [Your name / team]
- **Database Created:** 2026-06-09
- **Last Full Refresh:** 2026-08-13

> **What changed in the 2026-08-13 refresh (headlines):** **Cerebras IPO'd** (NASDAQ: CBRS, 2026-05-14, ~$5.5B raised at ~$56B implied) on the back of a **>$20B / 750MW OpenAI contract**. **NVIDIA licensed Groq's LPU technology and hired its founder for ~$20B** (2025-12) after a similar >$900M deal for **Enfabrica** (2025-09) — a licence-and-hire structure that is now the highest-value exit path in AI silicon. **Marvell acquired Celestial AI** (~$3.25B, up to ~$5.5B) and **XConn** ($540M); **Meta acquired Rivos** (~$2B); **Qualcomm closed Alphawave** ($2.4B); **Microchip is buying Hailo out of distress**. Mega-rounds: **Etched $300M at ~$10.3B**, **SambaNova $1B at ~$11B**, **Ayar Labs ~$500M at ~$3.75B**, **MatX $500M**, **OLIX $312M at ~$3.3B** (Europe's largest), **Positron $230M**, **Eliyan $145M**, **SiFive $400M**, **Ricursive Intelligence $300M at ~$4B**. Full detail in [REFRESH_LOG.md](REFRESH_LOG.md).

> ⚠️ **Data integrity note:** Every figure in this database is tagged with a confidence marker — `[CONFIRMED]`, `[TO VERIFY]`, `[ESTIMATED]`, `[UNCONFIRMED]`, or `[NO PUBLIC DATA]`. Funding amounts, valuations, customers, and headcounts move fast and are frequently mis-reported; treat all numbers as point-in-time snapshots to be re-verified at each refresh. This file is an analytical research aid, not investment advice.

---

## Core Use Cases

- Source new AI semiconductor startup investments.
- Track Series Seed, Series A, Series B, and growth-stage opportunities.
- Monitor emerging technical inflections before they become consensus.
- Identify leading researchers and labs likely to produce future startups.
- Track VC and strategic investors active in AI semiconductor infrastructure.
- Monitor M&A and exit activity.
- Build category-specific investment theses.
- Support investment committee memos and technical due diligence.

---

## Refresh Status Dashboard

Status legend: 🟢 **Current** (≤30 days) · 🟡 **Needs refresh** (30–90 days) · 🔴 **Stale** (>90 days)

| File | Category | Entries | Last Refreshed | Refresh Count | Status | Priority |
|------|----------|--------:|----------------|--------------:|--------|----------|
| [01_training_accelerators.md](categories/01_training_accelerators.md) | Training Chips | 8 | 2026-08-13 | 2 | 🟢 Current | High |
| [02_inference_accelerators.md](categories/02_inference_accelerators.md) | Inference Chips | 9 | 2026-08-13 | 2 | 🟢 Current | High |
| [03_edge_inference_chips.md](categories/03_edge_inference_chips.md) | Edge Inference | 9 | 2026-08-13 | 2 | 🟢 Current | Medium |
| [04_custom_asic_and_chiplets.md](categories/04_custom_asic_and_chiplets.md) | Custom ASIC & Chiplets | 9 | 2026-08-13 | 2 | 🟢 Current | High |
| [05_networking_and_interconnect.md](categories/05_networking_and_interconnect.md) | Networking & Interconnect | 7 | 2026-08-13 | 2 | 🟢 Current | High |
| [06_optical_interconnect_and_cpo.md](categories/06_optical_interconnect_and_cpo.md) | Optical & CPO | 9 | 2026-08-13 | 2 | 🟢 Current | High |
| [07_memory_and_storage.md](categories/07_memory_and_storage.md) | Memory & Storage | 8 | 2026-08-13 | 2 | 🟢 Current | High |
| [08_power_semiconductors_and_power_delivery.md](categories/08_power_semiconductors_and_power_delivery.md) | Power | 6 | 2026-08-13 | 2 | 🟢 Current | High |
| [09_security_crypto_and_confidential_compute.md](categories/09_security_crypto_and_confidential_compute.md) | Security & Confidential Compute | 5 | 2026-08-13 | 2 | 🟢 Current | Medium |
| [10_rf_wireless_and_connectivity.md](categories/10_rf_wireless_and_connectivity.md) | RF & Wireless | 4 | 2026-08-13 | 2 | 🟢 Current | Low |
| [11_analog_mixed_signal_and_timing.md](categories/11_analog_mixed_signal_and_timing.md) | Analog & Timing | 5 | 2026-08-13 | 2 | 🟢 Current | Medium |
| [12_eda_ip_and_design_tools.md](categories/12_eda_ip_and_design_tools.md) | EDA, IP & Tools | 13 | 2026-08-13 | 2 | 🟢 Current | High |
| [13_foundry_packaging_and_chiplet_integration.md](categories/13_foundry_packaging_and_chiplet_integration.md) | Foundry & Packaging | 5 | 2026-08-13 | 2 | 🟢 Current | High |
| [14_quantum_neuromorphic_and_non_von_neumann.md](categories/14_quantum_neuromorphic_and_non_von_neumann.md) | Quantum & Neuromorphic | 8 | 2026-08-13 | 2 | 🟢 Current | Medium |
| [15_autonomous_robotics_and_automotive_silicon.md](categories/15_autonomous_robotics_and_automotive_silicon.md) | Automotive & Robotics | 5 | 2026-08-13 | 2 | 🟢 Current | Medium |
| [16_datacenter_infrastructure_enablers.md](categories/16_datacenter_infrastructure_enablers.md) | DC Infra Enablers | 6 | 2026-08-13 | 2 | 🟢 Current | High |
| [17_emerging_research_to_startup_pipeline.md](categories/17_emerging_research_to_startup_pipeline.md) | Research-to-Startup | 9 | 2026-08-13 | 2 | 🟢 Current | High |
| [20_ma_tracker.md](deal_tracker/20_ma_tracker.md) | M&A | 22 | 2026-08-13 | 2 | 🟢 Current | High |
| [21_vc_investor_tracker.md](deal_tracker/21_vc_investor_tracker.md) | Investors | 31 | 2026-08-13 | 2 | 🟢 Current | High |
| [22_funding_round_tracker.md](deal_tracker/22_funding_round_tracker.md) | Funding Rounds | 44 | 2026-08-13 | 2 | 🟢 Current | High |
| [23_exit_and_shutdown_tracker.md](deal_tracker/23_exit_and_shutdown_tracker.md) | Exits & Shutdowns | 18 | 2026-08-13 | 2 | 🟢 Current | Medium |
| [24_strategic_investor_tracker.md](deal_tracker/24_strategic_investor_tracker.md) | Strategic Investors | 12 | 2026-08-13 | 2 | 🟢 Current | High |
| [leading_researchers_index.md](researchers/leading_researchers_index.md) | Leading Researchers | 52 | 2026-08-13 | 3 | 🟢 Current | High |

---

## Category Quick Reference

| # | Category | VC Relevance | Primary AI DC Relevance | File |
|---|----------|--------------|-------------------------|------|
| 01 | Training Accelerators | High | High | [categories/01_training_accelerators.md](categories/01_training_accelerators.md) |
| 02 | Inference Accelerators | High | High | [categories/02_inference_accelerators.md](categories/02_inference_accelerators.md) |
| 03 | Edge Inference Chips | Medium | Medium | [categories/03_edge_inference_chips.md](categories/03_edge_inference_chips.md) |
| 04 | Custom ASIC & Chiplets | High | High | [categories/04_custom_asic_and_chiplets.md](categories/04_custom_asic_and_chiplets.md) |
| 05 | Networking & Interconnect | High | High | [categories/05_networking_and_interconnect.md](categories/05_networking_and_interconnect.md) |
| 06 | Optical Interconnect & CPO | High | High | [categories/06_optical_interconnect_and_cpo.md](categories/06_optical_interconnect_and_cpo.md) |
| 07 | Memory & Storage | High | High | [categories/07_memory_and_storage.md](categories/07_memory_and_storage.md) |
| 08 | Power Semiconductors & Power Delivery | High | High | [categories/08_power_semiconductors_and_power_delivery.md](categories/08_power_semiconductors_and_power_delivery.md) |
| 09 | Security, Crypto & Confidential Compute | Medium | Medium | [categories/09_security_crypto_and_confidential_compute.md](categories/09_security_crypto_and_confidential_compute.md) |
| 10 | RF, Wireless & Connectivity | Low | Low | [categories/10_rf_wireless_and_connectivity.md](categories/10_rf_wireless_and_connectivity.md) |
| 11 | Analog, Mixed Signal & Timing | Medium | Medium | [categories/11_analog_mixed_signal_and_timing.md](categories/11_analog_mixed_signal_and_timing.md) |
| 12 | EDA, IP & Design Tools | High | Medium | [categories/12_eda_ip_and_design_tools.md](categories/12_eda_ip_and_design_tools.md) |
| 13 | Foundry, Packaging & Chiplet Integration | High | High | [categories/13_foundry_packaging_and_chiplet_integration.md](categories/13_foundry_packaging_and_chiplet_integration.md) |
| 14 | Quantum, Neuromorphic & Non-Von-Neumann | Medium | Low/Long-term | [categories/14_quantum_neuromorphic_and_non_von_neumann.md](categories/14_quantum_neuromorphic_and_non_von_neumann.md) |
| 15 | Autonomous, Robotics & Automotive Silicon | Medium | Medium | [categories/15_autonomous_robotics_and_automotive_silicon.md](categories/15_autonomous_robotics_and_automotive_silicon.md) |
| 16 | Datacenter Infrastructure Enablers | High | High | [categories/16_datacenter_infrastructure_enablers.md](categories/16_datacenter_infrastructure_enablers.md) |
| 17 | Emerging Research-to-Startup Pipeline | High | High | [categories/17_emerging_research_to_startup_pipeline.md](categories/17_emerging_research_to_startup_pipeline.md) |
| 20 | M&A Tracker | High | — | [deal_tracker/20_ma_tracker.md](deal_tracker/20_ma_tracker.md) |
| 21 | VC Investor Tracker | High | — | [deal_tracker/21_vc_investor_tracker.md](deal_tracker/21_vc_investor_tracker.md) |
| 22 | Funding Round Tracker | High | — | [deal_tracker/22_funding_round_tracker.md](deal_tracker/22_funding_round_tracker.md) |
| 23 | Exit & Shutdown Tracker | Medium | — | [deal_tracker/23_exit_and_shutdown_tracker.md](deal_tracker/23_exit_and_shutdown_tracker.md) |
| 24 | Strategic Investor Tracker | High | — | [deal_tracker/24_strategic_investor_tracker.md](deal_tracker/24_strategic_investor_tracker.md) |

Supporting docs: [INVESTMENT_THESES.md](INVESTMENT_THESES.md) · [MARKET_MAP.md](MARKET_MAP.md) · [RESEARCH_AND_RESEARCHERS.md](RESEARCH_AND_RESEARCHERS.md) · [STEALTH_STARTUP_DISCOVERY.md](STEALTH_STARTUP_DISCOVERY.md) · [REFRESH_LOG.md](REFRESH_LOG.md)

---

## Master Company Index

> Auto-generated by `scripts/build_index.py` from `data/company_index.yaml`. Alphabetical. All financials point-in-time and tagged in the source files.

| Company | Category | HQ | Founded | Stage | Total Funding | Lead Investors | Status | Primary File |
|---------|----------|----|---------|-------|---------------|----------------|--------|--------------|
| AheadComputing | 04 Custom ASIC/Chiplets (RISC-V IP) | Portland, US | 2024 | Seed 2 | ~$30M+ [TO VERIFY] | Eclipse Ventures, Toyota Ventures, Cambium | Active | categories/04_custom_asic_and_chiplets.md |
| Alphawave Semi | 04 Custom ASIC/Chiplets (IP) | Toronto/London | 2017 | Acquired (Qualcomm, closed ~Q4 2025) | ~$2.4B exit | Public (LSE) | Acquired | categories/04_custom_asic_and_chiplets.md |
| Astera Labs | 05 Networking/Interconnect | Santa Clara, US | 2017 | Public (NASDAQ: ALAB) | IPO 2024 | Sutter Hill, Fidelity | Active | categories/05_networking_and_interconnect.md |
| Axelera AI | 03 Edge Inference | Eindhoven, NL | 2021 | Series C [TO VERIFY] | ~$450M [TO VERIFY] | Innovation Industries, BlackRock, Samsung Catalyst | Active | categories/03_edge_inference_chips.md |
| Ayar Labs | 06 Optical/CPO | Santa Clara, US | 2015 | Series E | ~$870M [TO VERIFY] | Neuberger Berman [TO VERIFY], Advent, Light Street | Active | categories/06_optical_interconnect_and_cpo.md |
| Baya Systems | 04 Custom ASIC/Chiplets | Santa Clara, US | 2022 | Series B | ~$57M+ [TO VERIFY] | Matrix Partners, Maverick | Active | categories/04_custom_asic_and_chiplets.md |
| Blaize | 15 Automotive/Edge | El Dorado Hills, US | 2010 | Public (SPAC 2025) | ~$330M+ [TO VERIFY] | Temasek, Samsung | Active | categories/15_autonomous_robotics_and_automotive_silicon.md |
| Celestial AI | 06 Optical/CPO | Santa Clara, US | 2020 | Acquired (Marvell, closed 2026-02) | ~$594M raised; ~$3.25B-$5.5B exit | Fidelity, BlackRock, Maverick | Acquired | categories/06_optical_interconnect_and_cpo.md |
| Cerebras Systems | 01 Training | Sunnyvale, US | 2015 | Public (NASDAQ: CBRS, 2026-05) | ~$720M private + ~$5.5B IPO | Benchmark, Foundation Capital, G42 | Active | categories/01_training_accelerators.md |
| ChipAgents | 12 EDA/IP (agentic verification) | Santa Barbara, US | 2023 | Series A + ext. (2026-07) | ~$134M [TO VERIFY] | Micron, MediaTek | Active | categories/12_eda_ip_and_design_tools.md |
| Codasip | 12 EDA/IP | Brno, CZ | 2014 | Series A+ | ~$60M+ [TO VERIFY] | Smart Eureka, Eurazeo | Active | categories/12_eda_ip_and_design_tools.md |
| Cornelis Networks | 05 Networking | Wayne, US | 2020 | Series B/C | ~$130M+ [TO VERIFY] | Chevron Technology Ventures, DCVC | Active | categories/05_networking_and_interconnect.md |
| d-Matrix | 02 Inference | Santa Clara, US | 2019 | Series C | ~$450M [TO VERIFY] | Temasek, M12, Playground Global | Active | categories/02_inference_accelerators.md |
| DeepX | 03 Edge Inference | Seongnam, KR | 2018 | Series C | ~$120M+ [TO VERIFY] | SkyLake, BNW | Active | categories/03_edge_inference_chips.md |
| EdgeCortix | 03 Edge Inference | Tokyo, JP | 2019 | Series B (2025-11) | >$110M [TO VERIFY] | [TO VERIFY] | Active | categories/03_edge_inference_chips.md |
| Eliyan | 04 Custom ASIC/Chiplets | Santa Clara, US | 2021 | Series C (2026-07) | ~$295M [TO VERIFY] | Seligman Ventures, Cisco Investments, Lumentum | Active | categories/04_custom_asic_and_chiplets.md |
| Empower Semiconductor | 08 Power | San Jose, US | 2014 | Growth | [TO VERIFY] | Sutter Hill, Intel Capital | Active | categories/08_power_semiconductors_and_power_delivery.md |
| EnCharge AI | 14 Analog/In-Memory | Santa Clara, US | 2022 | Series B | ~$144M+ [TO VERIFY] | Tiger Global, RTX Ventures, In-Q-Tel | Active | categories/14_quantum_neuromorphic_and_non_von_neumann.md |
| Enfabrica | 05 Networking | Mountain View, US | 2020 | Standalone post-NVIDIA licence (2025-09) | ~$260M raised; >$900M NVIDIA licence | NVIDIA, Sutter Hill, Atreides | Active | categories/05_networking_and_interconnect.md |
| Etched | 02 Inference | Cupertino, US | 2022 | Series C (2026-07) | ~$800M+ [TO VERIFY] | Sequoia, a16z, Jane Street, SK hynix | Active | categories/02_inference_accelerators.md |
| Fabric Cryptography | 09 Security/Crypto | San Francisco, US | 2022 | Series A | ~$33M+ [TO VERIFY] | Blockchain Capital, 1kx | Active | categories/09_security_crypto_and_confidential_compute.md |
| FuriosaAI | 02 Inference | Seoul, KR | 2017 | Series D / pre-IPO (in market) | ~$200M+ [TO VERIFY] | DSC Investment, Naver | Active | categories/02_inference_accelerators.md |
| Graphcore | 01 Training | Bristol, UK | 2016 | Acquired (SoftBank, 2024) | ~$700M raised | Sequoia, BMW i Ventures | Acquired | categories/01_training_accelerators.md |
| Groq | 02 Inference | Mountain View, US | 2016 | Late; post-NVIDIA licence | ~$2.4B [TO VERIFY] | Disruptive, Infinitum, BlackRock | Active | categories/02_inference_accelerators.md |
| Hailo | 03 Edge Inference | Tel Aviv, IL | 2017 | Acquired (Microchip, 2026) | ~$425M raised | Poalim Equity, Gil Agmon | Acquired | categories/03_edge_inference_chips.md |
| Lightmatter | 06 Optical/CPO | Mountain View, US | 2017 | Series D | ~$850M+ [TO VERIFY] | GV, T. Rowe Price, Fidelity | Active | categories/06_optical_interconnect_and_cpo.md |
| MatX | 01 Training | Mountain View, US | 2022 | Series B (2026-02) | ~$500M+ [TO VERIFY] | Jane Street, Situational Awareness LP, Spark Capital | Active | categories/01_training_accelerators.md |
| Mythic | 14 Analog/Edge | Austin, US | 2012 | Series C (restructured) | ~$165M+ [TO VERIFY] | DCVC, Lux Capital, SoftBank | Active | categories/14_quantum_neuromorphic_and_non_von_neumann.md |
| OLIX | 06 Optical/CPO | London, UK | 2024 | Series B (2026-08) | ~$350M+ [TO VERIFY] | Hummingbird, Plural, Creandum, Arm | Active | categories/06_optical_interconnect_and_cpo.md |
| Oriole Networks | 05 Networking/Interconnect | London, UK | 2023 | Series A/B [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | Active | categories/05_networking_and_interconnect.md |
| Panmnesia | 07 Memory/CXL | Daejeon, KR | 2022 | Seed/A | ~$28M+ [TO VERIFY] | Daekyo Investment, SL Investment | Active | categories/07_memory_and_storage.md |
| Positron AI | 02 Inference | Reno, US | 2023 | Series B (2026-02) | ~$280M+ [TO VERIFY] | ARENA Private Wealth, Jump Trading, Unless, QIA, Arm | Active | categories/02_inference_accelerators.md |
| PsiQuantum | 14 Quantum | Palo Alto, US | 2016 | Growth | ~$1.3B+ [TO VERIFY] | BlackRock, Temasek, Baillie Gifford | Active | categories/14_quantum_neuromorphic_and_non_von_neumann.md |
| Rain AI | 14 Analog/Neuromorphic | San Francisco, US | 2017 | Series B [TO VERIFY] | ~$60M+ [TO VERIFY] | Prosperity7, Sam Altman | Active | categories/14_quantum_neuromorphic_and_non_von_neumann.md |
| Rebellions | 02 Inference | Seongnam, KR | 2020 | Pre-IPO (2026-03) | ~$725M+ [TO VERIFY] | Korea National Growth Fund, KT, Temasek | Active | categories/02_inference_accelerators.md |
| Recogni | 15 Automotive/Inference | San Jose, US | 2017 | Series C | ~$150M+ [TO VERIFY] | Celesta, GreatPoint, BMW i Ventures | Active | categories/15_autonomous_robotics_and_automotive_silicon.md |
| Ricursive Intelligence | 12 EDA/IP (AI for design) | US | 2025 | Series A (2026-01) | ~$300M+ [TO VERIFY] | Lightspeed, DST Global, NVentures, Sequoia | Active | categories/12_eda_ip_and_design_tools.md |
| Rivos | 04 Custom ASIC/RISC-V | Mountain View, US | 2021 | Acquired (Meta, 2025-10) | ~$250M+ raised; ~$2B exit [ESTIMATED] | Matrix Partners, Intel Capital, MediaTek | Acquired | categories/04_custom_asic_and_chiplets.md |
| Sagence AI | 14 Analog/In-Memory | Santa Clara, US | 2018 | Series A+ | [TO VERIFY] | [TO VERIFY] | Active | categories/14_quantum_neuromorphic_and_non_von_neumann.md |
| SambaNova Systems | 01 Training/Inference | Palo Alto, US | 2017 | Series F (2026-07) | ~$2.1B [TO VERIFY] | General Atlantic, SoftBank, BlackRock | Active | categories/01_training_accelerators.md |
| SiFive | 12 EDA/IP (RISC-V) | Santa Clara, US | 2015 | Series G (2026-04) | ~$970M [TO VERIFY] | Atreides Management, NVIDIA, Apollo | Active | categories/12_eda_ip_and_design_tools.md |
| SiMa.ai | 03 Edge Inference | San Jose, US | 2018 | Series B+ | ~$270M+ [TO VERIFY] | Maverick, Fidelity, Dell Technologies Capital | Active | categories/03_edge_inference_chips.md |
| Substrate | 13 Foundry/Packaging (lithography) | US | 2024 | Series A (2025-10) | ~$100M at >$1B [TO VERIFY] | General Catalyst, Founders Fund, In-Q-Tel | Active | categories/13_foundry_packaging_and_chiplet_integration.md |
| Tenstorrent | 01 Training/Inference | Toronto, CA | 2016 | Late (2025-11) | ~$1.18B [TO VERIFY] | Fidelity, Samsung, AFW Partners | Active | categories/01_training_accelerators.md |
| UnifabriX | 07 Memory/CXL | Yokneam, IL | 2020 | Seed/A | [TO VERIFY] | [TO VERIFY] | Active | categories/07_memory_and_storage.md |
| Untether AI | 02 Inference | Toronto, CA | 2018 | Wound down (IP to AMD, 2025) | ~$150M raised | Intel Capital, Tracker, CPPIB | Shut Down | categories/02_inference_accelerators.md |
| Ventana Micro Systems | 04 Custom ASIC/RISC-V | Cupertino, US | 2018 | Series C [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | Active | categories/04_custom_asic_and_chiplets.md |
| XConn Technologies | 07 Memory/CXL | San Jose, US | 2020 | Acquired (Marvell, 2026-02) | ~$540M exit [TO VERIFY] | [TO VERIFY] | Acquired | categories/07_memory_and_storage.md |
| Xscape Photonics | 06 Optical/CPO | New York, US | 2022 | Series A ext. (2026-03) | ~$81M [TO VERIFY] | Addition, IAG Capital, NVIDIA | Active | categories/06_optical_interconnect_and_cpo.md |

> This index lists marquee and representative entries; see individual category files for the full set and lighter-coverage entries. Counts in the dashboard reflect total entries per file.

---

## Master Investor Index

> Auto-generated from `data/investor_index.yaml`. See [21_vc_investor_tracker.md](deal_tracker/21_vc_investor_tracker.md) and [24_strategic_investor_tracker.md](deal_tracker/24_strategic_investor_tracker.md) for full profiles.

| Investor | Type | Semi Focus | AI Infra Focus | Relevant Portfolio | Stage Pref | Notes |
|----------|------|-----------|----------------|--------------------|-----------|-------|
| Arm (strategic) | Strategic | High | High | Positron AI, Eliyan, OLIX | B-Growth | Now an active silicon investor; Physical AI unit launched 2026-01 |
| Atreides Management | Crossover | High | High | Enfabrica, Positron AI | B-Growth | Public/private crossover |
| DCVC | VC | High | High | Cornelis Networks, Mythic, Agile Analog | Seed-B | Deep-tech/compute |
| Eclipse Ventures | VC | High | High | Cerebras | Seed-B | Full-stack hard-tech |
| Fidelity / BlackRock / T. Rowe Price | Crossover | High | High | Cerebras, Groq, Lightmatter, Celestial AI | Growth/Pre-IPO | Pre-IPO bridge |
| General Atlantic | Growth | Medium | High | SambaNova | Growth | Led SambaNova $1B Series F at ~$11B (2026-07) |
| Innovation Industries | VC (NL) | High | High | Axelera AI | A-C | Led Axelera >$250M (2026-02); Europe's key edge-silicon investor |
| Intel Capital | Strategic | High | Medium | Rivos, Eliyan, Empower Semiconductor, Movellus | Seed-Growth | Now independent fund |
| Jane Street | Prop/quant | Medium | High | MatX, Etched | B-Growth | Balance-sheet capital; co-led MatX $500M B (2026) |
| Korea National Growth Fund | Sovereign | High | High | Rebellions | Growth/Pre-IPO | KRW 250B (~$178M) into Rebellions (2026-03); state K-NVIDIA program |
| Lightspeed Venture Partners | VC | Medium | High | Ricursive Intelligence | A-Growth | Led Ricursive $300M A at ~$4B (2026-01) |
| Lux Capital | VC | High | High | Mythic | Seed-B | Frontier hardware |
| Marvell (corp dev) | Strategic | High | High | MatX, Celestial AI (acquired), XConn (acquired) | M&A + growth | Most acquisitive AI-silicon buyer of 2026 (~$3.8B across two deals) |
| Matrix Partners | VC | High | High | Rivos, Baya Systems | Seed-B | Compute infra/IP |
| Maverick | VC/Growth | High | High | Celestial AI, SiMa.ai | A-Growth | Silicon-focused |
| NVIDIA (NVentures) | Strategic | High | High | Enfabrica, Xscape Photonics, Ayar Labs | A-Growth | Ecosystem signal + acquirer |
| Playground Global | VC | High | High | d-Matrix | Seed-A | Hard-tech silicon |
| Qatar Investment Authority | Sovereign | Medium | High | Positron AI | B-Growth | Gulf capital entering inference silicon directly |
| Samsung Catalyst Fund | Strategic | High | High | Tenstorrent, Groq, Blaize, Axelera AI, Eliyan | A-Growth | Memory/foundry adjacency |
| Seligman Ventures | Growth | High | High | Eliyan, SambaNova | B-Growth | Led Eliyan $145M Series C at ~$1B (2026-07) |
| Sequoia Capital | VC | Medium | High | Etched, Ricursive Intelligence | A-Growth | Led Etched $300M C at ~$10.3B (2026-07) |
| Situational Awareness LP | Thesis fund | Medium | High | MatX | B-Growth | AGI-compute thesis fund; co-led MatX B |
| Sutter Hill Ventures | VC | High | High | Astera Labs, Enfabrica, Empower Semiconductor | Seed-A | Deep silicon incubation track record |
| Temasek | Sovereign | High | High | d-Matrix, Rebellions, PsiQuantum | B-Growth | Patient capital |
| Tiger Global | Crossover | Medium | High | EnCharge AI, Eliyan | B-Growth | Growth-stage AI infra |

---

## Master Researcher Index

> Auto-generated from `data/researcher_index.yaml` via `scripts/build_index.py researchers`. See [researchers/leading_researchers_index.md](researchers/leading_researchers_index.md) for full profiles (organized by domain). **VC Relevance Score: 1–5.** 52 researchers across architecture, efficient ML, memory/PIM, interconnect, photonics, analog/IMC, EDA, packaging, power, and quantum.

| Researcher | Institution | Research Area | Patent Activity | Startup Signals | VC Relevance | Profile |
|------------|-------------|---------------|-----------------|-----------------|:------------:|---------|
| Amin Vahdat | Google | DC networking, optical circuit switching | High | Watchlist (incumbent) | 5 | [profile](researchers/leading_researchers_index.md) |
| Azalia Mirhoseini & Anna Goldie | Stanford / industry (ex-DeepMind) | RL for chip placement (AlphaChip) | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Bill Dally | Stanford / NVIDIA | Accelerator arch, interconnect | High | Watchlist (incumbent) | 5 | [profile](researchers/leading_researchers_index.md) |
| Brucek Khailany | NVIDIA | ML for EDA, agile VLSI | High | Watchlist (incumbent) | 4 | [profile](researchers/leading_researchers_index.md) |
| Christopher Ré | Stanford / SambaNova | ML systems, SSMs, data-centric ML | Medium | Confirmed (serial) | 5 | [profile](researchers/leading_researchers_index.md) |
| Daniel Sanchez | MIT | Scalable arch, memory hierarchy, sparse accel | Low | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| David Brooks & Gu-Yeon Wei | Harvard | Energy-efficient arch, edge accel SoCs | Medium | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| David Patterson | UC Berkeley / Google | RISC-V, DSAs, TPU | Medium | Watchlist | 5 | [profile](researchers/leading_researchers_index.md) |
| David Perreault | MIT | High-density power conversion | High | Confirmed (serial) | 4 | [profile](researchers/leading_researchers_index.md) |
| David Z. Pan | UT Austin | ML for EDA, physical design, analog automation | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Deming Chen | UIUC | HLS, hardware-aware ML, accelerators | Medium | Likely (Inspirit IoT) | 3 | [profile](researchers/leading_researchers_index.md) |
| Dirk Englund | MIT | Photonic computing, quantum photonics | High | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Dmitri Strukov | UC Santa Barbara | Memristive devices, analog NN HW | High | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| Edoardo Charbon | EPFL | Cryogenic CMOS, quantum control | High | Likely | 3 | [profile](researchers/leading_researchers_index.md) |
| H.-S. Philip Wong | Stanford | Emerging memory, IMC, 3D | High | Likely | 5 | [profile](researchers/leading_researchers_index.md) |
| Hadi Esmaeilzadeh | UC San Diego | Accelerators, near-data, serving systems | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Jason Cong | UCLA | FPGA/HLS, EDA, customized computing | High | Confirmed (serial) | 5 | [profile](researchers/leading_researchers_index.md) |
| Jelena Vučković | Stanford | Nanophotonics, inverse design, quantum photonics | Medium | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Joel Emer | MIT / NVIDIA | Accelerator modeling, sparse tensor accel | Medium | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| John Bowers | UC Santa Barbara | Lasers on silicon, photonics | High | Likely | 5 | [profile](researchers/leading_researchers_index.md) |
| John Martinis | UC Santa Barbara (ex-Google) | Superconducting qubits | High | Confirmed (Qolab) | 4 | [profile](researchers/leading_researchers_index.md) |
| Kaushik Roy | Purdue | Neuromorphic, emerging-device IMC | High | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Keren Bergman | Columbia | Silicon photonics, optical interconnect | High | Likely | 5 | [profile](researchers/leading_researchers_index.md) |
| Khurram Afridi | Cornell | High-frequency power conversion | Medium | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| Krste Asanović | UC Berkeley / SiFive | RISC-V, vector arch | Medium | Confirmed (SiFive) | 5 | [profile](researchers/leading_researchers_index.md) |
| Kunle Olukotun | Stanford / SambaNova | Reconfigurable dataflow (RDA) | High | Confirmed (SambaNova) | 5 | [profile](researchers/leading_researchers_index.md) |
| Marin Soljačić | MIT | Photonic computing, nanophotonics | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Mark Horowitz | Stanford | Circuits, agile hardware | High | Confirmed (legacy) | 4 | [profile](researchers/leading_researchers_index.md) |
| Mattan Erez | UT Austin | Memory systems, accelerator memory | Medium | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| Michal Lipson | Columbia | Silicon photonics, combs, programmable photonics | High | Likely | 5 | [profile](researchers/leading_researchers_index.md) |
| Mikhail Lukin | Harvard | Neutral-atom quantum computing | High | Confirmed (QuEra) | 4 | [profile](researchers/leading_researchers_index.md) |
| Moinuddin Qureshi | Georgia Tech | Memory systems, CXL, memory security | Medium | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| Muhannad Bakir | Georgia Tech | Heterogeneous integration, interposers, thermal | High | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Myoungsoo Jung | KAIST / Panmnesia | CXL systems, memory disaggregation | High | Confirmed (Panmnesia) | 5 | [profile](researchers/leading_researchers_index.md) |
| Naresh Shanbhag | UIUC | Deep in-memory architecture (DIMA) | High | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Naveen Verma | Princeton / EnCharge AI | Analog in-memory compute | High | Confirmed (EnCharge) | 5 | [profile](researchers/leading_researchers_index.md) |
| Onur Mutlu | ETH Zürich | PIM / near-memory | High | Likely | 5 | [profile](researchers/leading_researchers_index.md) |
| Ramin Farjadrad | Eliyan (ex-Marvell/Aquantia) | SerDes, die-to-die interconnect | High | Confirmed (Eliyan) | 5 | [profile](researchers/leading_researchers_index.md) |
| Robert Schoelkopf | Yale | Circuit QED, bosonic error correction | High | Confirmed (Quantum Circuits) | 3 | [profile](researchers/leading_researchers_index.md) |
| Saman Amarasinghe | MIT | Compilers for accelerators (Exo/TACO/Halide) | Low | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Saugata Ghose | UIUC | PIM, memory systems, near-data | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Siddharth Garg | NYU | Hardware security, LLMs for HDL | Medium | Likely | 3 | [profile](researchers/leading_researchers_index.md) |
| Song Han | MIT / NVIDIA | Model compression, efficient inference | Medium | Likely (OmniML→NVIDIA) | 5 | [profile](researchers/leading_researchers_index.md) |
| Subhasish Mitra | Stanford | Monolithic 3D (N3XT), CNT computing | High | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Subramanian Iyer | UCLA | Heterogeneous integration, SiIF, chiplets | High | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Tomás Palacios | MIT | GaN devices, wide-bandgap power, RF | High | Confirmed (Finwave) | 4 | [profile](researchers/leading_researchers_index.md) |
| Tri Dao | Princeton / Together AI | FlashAttention, SSMs (Mamba), kernels | Low | Likely (Together) | 5 | [profile](researchers/leading_researchers_index.md) |
| Tushar Krishna | Georgia Tech | ML interconnect, collectives, NoC | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Vijay Janapa Reddi | Harvard / MLCommons | MLPerf benchmarking, edge/TinyML | Low | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Vivienne Sze | MIT | Energy-efficient DL hardware | Medium | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Wei Lu | University of Michigan | Memristor/RRAM IMC | High | Confirmed (Crossbar/MemryX) | 4 | [profile](researchers/leading_researchers_index.md) |
| Yakun Sophia Shao | UC Berkeley | Accelerator design automation, chiplets | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |

---

## Key Stats

> Updated on each full refresh. Initial build 2026-06-09; latest full refresh 2026-08-13. Counts reflect entries in this database, not the total market.

- **Total startups tracked:** 125+ (across all category files; ~45 with full profiles)
- **Active companies:** ~100
- **Stealth / semi-stealth companies tracked:** 5
- **Exited companies — acquired:** 16 (added 2026: Celestial AI, Rivos, Hailo, XConn, Alphawave, SkyWater, GigaIO assets)
- **Companies taken public:** 2 (Astera Labs 2024; **Cerebras 2026**)
- **Companies with licence-and-hire outcomes:** 2 (**Groq ~$20B, Enfabrica >$900M — both to NVIDIA**)
- **Exited companies — shut down:** 4
- **Total VC/crossover investors tracked:** 31 profiled rows in [21_vc_investor_tracker.md](deal_tracker/21_vc_investor_tracker.md) (14 original + 17 added in 2026); 25 in the machine-readable `data/investor_index.yaml`
- **Strategic investors tracked:** 12 profiles + 11 behavior updates
- **M&A / structural deals tracked:** 22
- **Funding rounds tracked:** 44
- **Research labs tracked:** 25 (university + corporate)
- **Leading researchers tracked:** 52 (across 10 domains)
- **Papers tracked:** 34 (emphasis on 2023–2026)
- **Patents tracked:** 22 (clusters/themes)
- **Research-to-startup conversions recorded:** 2 (**Ricursive Intelligence** from the AI-EDA watch-item; **OLIX** from photonic compute)
- **Total disclosed funding tracked:** ~$18B+ [ESTIMATED — sum of disclosed rounds, double-counting possible], plus ~$28B of 2025–26 acquisition/licence value and a ~$5.5B IPO

---

## Future Refresh Prompts

> Copy-paste any block below into a new Claude Code session pointed at this repo.

### Full Database Refresh
```
REFRESH FULL DATABASE — Update every category, company, investor, funding round, M&A deal, researcher, lab, paper, patent, and research-to-startup signal. Search for new public information since the last full refresh. Add new companies, update funding rounds, archive exited or shut-down companies, update investor portfolios, refresh leading researchers and labs, update research/patent watchlists, rebuild all indexes, update README dashboard, and append REFRESH_LOG.md. Clearly mark each update as Confirmed, Estimated, Unconfirmed, or To Verify.
```

### Category Refresh
```
REFRESH CATEGORY: [filename.md] — Refresh this category with new startups, funding rounds, investors, customer traction, technical milestones, M&A events, shutdowns, and research-to-startup signals since the last refresh. Update all relevant indexes and append REFRESH_LOG.md.
```

### VC Investor Refresh
```
REFRESH VC INVESTOR TRACKER — Update active VC and strategic investors in AI semiconductor infrastructure. Refresh portfolio companies, new deals, stage preference, investment themes, public thesis statements, and notable partners. Prioritize investors with recent activity in AI infrastructure, semiconductors, datacenter chips, networking, optical, memory, EDA, power, and packaging.
```

### Emerging Research Refresh
```
REFRESH RESEARCH PIPELINE — Refresh leading papers, university labs, corporate research labs, patents, technical conference activity, and researcher profiles. Identify researchers whose work could plausibly produce future stealth-mode startups in AI accelerators, interconnect, chiplets, memory, packaging, photonics, EDA, power delivery, or non-von-Neumann computing. Do not infer private company formation without public evidence. Label all startup signals by confidence level.
```

### Stealth Startup Discovery Refresh
```
REFRESH STEALTH STARTUP DISCOVERY — Search public signals that may indicate new stealth-mode semiconductor startups, including recent company incorporations if publicly available, founder LinkedIn changes, research lab spinouts, patent assignments, conference talks, seed funding announcements, job postings, domain launches, GitHub activity, accelerator cohorts, and investor portfolio pages. Use only public sources. Do not include private personal data. Mark all findings as Confirmed, Likely, Weak Signal, or To Verify.
```

---

## Data Quality Conventions

| Tag | Meaning |
|-----|---------|
| `[CONFIRMED]` | Backed by a reliable public source |
| `[TO VERIFY]` | Plausible but needs confirmation |
| `[ESTIMATED]` | Estimated from available public data |
| `[UNCONFIRMED]` | Reported by a low-confidence source |
| `[NO PUBLIC DATA]` | No reliable public information found |

We never invent funding amounts, valuations, customers, revenue, headcounts, investors, acquisition interest, startup formation, or researcher intentions. When unavailable, fields read "Unavailable from public sources." Claims are attributed: company claim vs. customer-validated vs. investor claim vs. media-reported vs. analyst estimate vs. technical inference.
