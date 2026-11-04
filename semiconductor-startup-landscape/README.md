# AI Semiconductor Startup Landscape Database

**Purpose:** A VC-style, indexed, independently refreshable knowledge base tracking the global startup, research, funding, and M&A ecosystem in semiconductors relevant to AI datacenter and adjacent edge/automotive markets.

- **Maintained by:** [Your name / team]
- **Database Created:** 2026-06-09
- **Last Full Refresh:** 2026-11-04 (Refresh #3)

> ⚠️ **Data integrity note:** Every figure in this database is tagged with a confidence marker — `[CONFIRMED]`, `[TO VERIFY]`, `[ESTIMATED]`, `[UNCONFIRMED]`, or `[NO PUBLIC DATA]`. Funding amounts, valuations, customers, and headcounts move fast and are frequently mis-reported; treat all numbers as point-in-time snapshots to be re-verified at each refresh. This file is an analytical research aid, not investment advice.

---

## Latest Developments — Refresh #3 (2026-11-04)

> Highlights only. Details, sources and confidence tags are in the linked files. Full change list: [REFRESH_LOG.md](REFRESH_LOG.md).

**Exits & structure**
- **NVIDIA–Groq:** NVIDIA took a non-exclusive licence to Groq's LPU technology and hired its founder/CEO and core team (Dec 2025; ~$20B reported). Groq/GroqCloud continues under a new CEO. Together with NVIDIA–Enfabrica (>$900M, Sep 2025), this made the **licence + acqui-hire** a mainstream exit route. → [20](deal_tracker/20_ma_tracker.md)
- **Acquisitions:**
  - Closed: Marvell–Celestial AI (Feb 2026; $3.25B upfront, up to $5.5B), Analog Devices–Empower ($1.5B, Jul 2026), Microchip–Hailo (Sep 2026), Molex–Teramount (May 2026), NXP–Kinara ($307M), SiTime–Renesas timing, Qualcomm–Alphawave (~$2.4B), SoftBank–Ampere ($6.5B).
  - Announced in 2026: AMD–Taalas (Aug 2026) and Unconventional AI–NeuReality (Oct 2026).
  - RISC-V roll-up: Meta–Rivos, Qualcomm–Ventana and Qualcomm–Akeana.
- **IPOs:** Cerebras (Nasdaq: CBRS, May 2026, ~$5.5B raised) and Quantinuum (Nasdaq: QNT, Jun 2026, ~$1.68B raised). Chinese GPU makers Moore Threads, MetaX and Biren listed in Dec 2025–Jan 2026.

**Capital**
- **Inference/compute mega-rounds:**
  - Tenstorrent $1.5B at $6.2B (Oct 2026)
  - FuriosaAI $620M at $2.9B (Oct 2026)
  - MatX $500M (Feb 2026)
  - Etched $500M at $5B (Jan 2026), then reported rounds at $10.3B and ~$21B [TO VERIFY]
  - Rebellions $400M pre-IPO, Positron $230M, Fractile $220M, d-Matrix $275M
- **Interconnect & optics:** Ayar Labs $500M Series E, Lumilens $700M+ at $5.51B, Xsight Labs >$300M at $2.8B, Upscale AI ~$390M across two rounds, Cornelis $205M, SiFive $400M at $3.65B (pre-IPO).
- **AI-for-chip-design:** Ricursive Intelligence $300M at ~$4B, ChipAgents (Series A total $134M), Cognichip $60M. **New physics:** Unconventional AI ~$475M seed at ~$4.5B.

**Market**
- 2026 big-cloud capex is tracking ~$800B+. NVIDIA Vera Rubin (HBM4) ramps in 2H26. The **DRAM/HBM shortage** (contract prices roughly doubled in 1H26 per TrendForce) is expected to last into 2027+.
- CPO switches (Broadcom TH6-Davisson, NVIDIA Spectrum-X/Quantum-X Photonics) moved into early deployment.
- Custom silicon scaled: Google sells TPUs outside its own cloud (Anthropic up to 1M TPUs), OpenAI has 10 GW with Broadcom and 6 GW with AMD, and OpenAI signed a >$10B compute deal with Cerebras.

**Re-rating:** Interconnect/optics, memory, power delivery and EDA are upgraded. Inference stays High, with valuation risk flagged. → [INVESTMENT_THESES.md](INVESTMENT_THESES.md)

> ⚠️ **Coverage caveat for this refresh:** Web-search budgets limited verification in a few areas: liquid-cooling vendors (16), parts of quantum (14), automotive (15), and some funding totals. Those items are tagged `[TO VERIFY]` / `[UNCONFIRMED]` and should be prioritized at the next refresh.

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
| [01_training_accelerators.md](categories/01_training_accelerators.md) | Training Chips | 8 | 2026-11-04 | 2 | 🟢 Current | High |
| [02_inference_accelerators.md](categories/02_inference_accelerators.md) | Inference Chips | 10 | 2026-11-04 | 2 | 🟢 Current | High |
| [03_edge_inference_chips.md](categories/03_edge_inference_chips.md) | Edge Inference | 10 | 2026-11-04 | 2 | 🟢 Current | Medium |
| [04_custom_asic_and_chiplets.md](categories/04_custom_asic_and_chiplets.md) | Custom ASIC & Chiplets | 9 | 2026-11-04 | 2 | 🟢 Current | High |
| [05_networking_and_interconnect.md](categories/05_networking_and_interconnect.md) | Networking & Interconnect | 7 | 2026-11-04 | 2 | 🟢 Current | High |
| [06_optical_interconnect_and_cpo.md](categories/06_optical_interconnect_and_cpo.md) | Optical & CPO | 16 | 2026-11-04 | 2 | 🟢 Current | High |
| [07_memory_and_storage.md](categories/07_memory_and_storage.md) | Memory & Storage | 8 | 2026-11-04 | 2 | 🟢 Current | High |
| [08_power_semiconductors_and_power_delivery.md](categories/08_power_semiconductors_and_power_delivery.md) | Power | 13 | 2026-11-04 | 2 | 🟢 Current | High |
| [09_security_crypto_and_confidential_compute.md](categories/09_security_crypto_and_confidential_compute.md) | Security & Confidential Compute | 7 | 2026-11-04 | 2 | 🟢 Current | Medium |
| [10_rf_wireless_and_connectivity.md](categories/10_rf_wireless_and_connectivity.md) | RF & Wireless | 7 | 2026-11-04 | 2 | 🟢 Current | Low |
| [11_analog_mixed_signal_and_timing.md](categories/11_analog_mixed_signal_and_timing.md) | Analog & Timing | 7 | 2026-11-04 | 2 | 🟢 Current | Medium |
| [12_eda_ip_and_design_tools.md](categories/12_eda_ip_and_design_tools.md) | EDA, IP & Tools | 13 | 2026-11-04 | 2 | 🟢 Current | High |
| [13_foundry_packaging_and_chiplet_integration.md](categories/13_foundry_packaging_and_chiplet_integration.md) | Foundry & Packaging | 10 | 2026-11-04 | 2 | 🟢 Current | High |
| [14_quantum_neuromorphic_and_non_von_neumann.md](categories/14_quantum_neuromorphic_and_non_von_neumann.md) | Quantum & Neuromorphic | 15 | 2026-11-04 | 2 | 🟢 Current | Medium |
| [15_autonomous_robotics_and_automotive_silicon.md](categories/15_autonomous_robotics_and_automotive_silicon.md) | Automotive & Robotics | 7 | 2026-11-04 | 2 | 🟢 Current | Medium |
| [16_datacenter_infrastructure_enablers.md](categories/16_datacenter_infrastructure_enablers.md) | DC Infra Enablers | 10 | 2026-11-04 | 2 | 🟢 Current | High |
| [17_emerging_research_to_startup_pipeline.md](categories/17_emerging_research_to_startup_pipeline.md) | Research-to-Startup | 18 | 2026-11-04 | 2 | 🟢 Current | High |
| [20_ma_tracker.md](deal_tracker/20_ma_tracker.md) | M&A | 36 | 2026-11-04 | 2 | 🟢 Current | High |
| [21_vc_investor_tracker.md](deal_tracker/21_vc_investor_tracker.md) | Investors | 34 | 2026-11-04 | 2 | 🟢 Current | High |
| [22_funding_round_tracker.md](deal_tracker/22_funding_round_tracker.md) | Funding Rounds | 56 | 2026-11-04 | 2 | 🟢 Current | High |
| [23_exit_and_shutdown_tracker.md](deal_tracker/23_exit_and_shutdown_tracker.md) | Exits & Shutdowns | 34 | 2026-11-04 | 2 | 🟢 Current | Medium |
| [24_strategic_investor_tracker.md](deal_tracker/24_strategic_investor_tracker.md) | Strategic Investors | 20 | 2026-11-04 | 2 | 🟢 Current | High |
| [leading_researchers_index.md](researchers/leading_researchers_index.md) | Leading Researchers | 62 | 2026-11-04 | 3 | 🟢 Current | High |
| [university_labs_index.md](researchers/university_labs_index.md) | University Labs | 28 | 2026-11-04 | 3 | 🟢 Current | High |
| [corporate_research_labs_index.md](researchers/corporate_research_labs_index.md) | Corporate Labs | 15 | 2026-11-04 | 3 | 🟢 Current | Medium |
| [paper_watchlist.md](researchers/paper_watchlist.md) | Paper Watchlist | 38 | 2026-11-04 | 3 | 🟢 Current | High |
| [patent_watchlist.md](researchers/patent_watchlist.md) | Patent Watchlist | 30 | 2026-11-04 | 3 | 🟢 Current | Medium |

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
| Accelsius | 16 DC Infra | Austin, US | 2022 | Series B | ~$65M [TO VERIFY] | [TO VERIFY] | Active | [16](categories/16_datacenter_infrastructure_enablers.md) |
| Akeana | 04 Custom ASIC/RISC-V | Santa Clara, US | 2021 | Acquired by Qualcomm (Oct 2026) [reported] | ~$100M+ | Kleiner Perkins, Mayfield, Fidelity | Acquired | [04](categories/04_custom_asic_and_chiplets.md) |
| Astera Labs | 05 Networking/Interconnect | Santa Clara, US | 2017 | Public (NASDAQ: ALAB); Q2'26 revenue $392.4M [CONFIRMED] | IPO 2024 | Sutter Hill, Fidelity | Public | [05](categories/05_networking_and_interconnect.md) |
| Auradine | 05 Networking/Interconnect | Santa Clara, US | 2022 | Series C ($153M, Apr 2025) [CONFIRMED] | ~$314M [TO VERIFY] | StepStone, Samsung Catalyst, Qualcomm Ventures, Mayfield | Active | [05](categories/05_networking_and_interconnect.md) |
| Axelera AI | 03 Edge Inference | Eindhoven, NL | 2021 | Growth (>$250M, Feb 2026) [CONFIRMED] | ~$450M+ incl. grants [CONFIRMED] | Innovation Industries, BlackRock, EIC Fund | Active | [03](categories/03_edge_inference_chips.md) |
| Ayar Labs | 06 Optical/CPO | San Jose, US | 2015 | Series E ($500M at ~$3.75B, Mar 2026) [CONFIRMED] + $150M ext. (Sep 2026) [TO VERIFY] | ~$870M-1.0B+ [TO VERIFY] | Neuberger Berman, NVIDIA, AMD, Intel Capital | Active | [06](categories/06_optical_interconnect_and_cpo.md) |
| Baya Systems | 04 Custom ASIC/Chiplets | Santa Clara, US | 2022 | Series B ($36M, Jan 2025) [CONFIRMED] | ~$47M+ [TO VERIFY] | Maverick Silicon, Matrix Partners, Intel Capital | Active | [04](categories/04_custom_asic_and_chiplets.md) |
| Blaize | 15 Automotive/Edge | El Dorado Hills, US | 2010 | Public (NASDAQ: BZAI, SPAC Jan 2025) | ~$330M+ pre-SPAC [TO VERIFY] | Temasek, Samsung | Public | [15](categories/15_autonomous_robotics_and_automotive_silicon.md) |
| Blue Cheetah | 04 Custom ASIC/Chiplets | Sunnyvale, US | 2018 | Acquired by Tenstorrent (Jul 2025) [CONFIRMED] | [TO VERIFY] | [TO VERIFY] | Acquired | [04](categories/04_custom_asic_and_chiplets.md) |
| C2i Semiconductors | 08 Power | Bangalore, IN | 2024 | Series A | ~$16.7M [CONFIRMED] | TDK Ventures, Peak XV | Active | [08](categories/08_power_semiconductors_and_power_delivery.md) |
| Callosum | 02 Inference (orchestration) | London, UK | 2025 | Seed ($100M, Aug 2026) [CONFIRMED] | ~$110M [CONFIRMED] | Atomico, Plural, UK Sovereign AI Fund | Active | [17](categories/17_emerging_research_to_startup_pipeline.md) |
| Cambridge GaN Devices | 08 Power | Cambridge, UK | 2016 | Series C ($32M, Feb 2025) [CONFIRMED] | ~$60M [TO VERIFY] | Foresight | Active | [08](categories/08_power_semiconductors_and_power_delivery.md) |
| Celestial AI | 06 Optical/CPO | Santa Clara, US | 2020 | Acquired by Marvell ($3.25B upfront, up to $5.5B w/ earn-out; closed 2026-02-02) [CONFIRMED] | ~$515M+ [TO VERIFY] | Fidelity, BlackRock, Maverick | Acquired | [06](categories/06_optical_interconnect_and_cpo.md) |
| Cerebras Systems | 01 Training | Sunnyvale, US | 2015 | Public (Nasdaq: CBRS, IPO 2026-05-14, ~$5.55B raised at $185/sh) [CONFIRMED] | ~$2.8B private [ESTIMATED] + IPO | Benchmark, Fidelity, Atreides, Tiger Global | Public | [01](categories/01_training_accelerators.md) |
| ChipAgents | 12 EDA/IP | Santa Clara, US | 2023 | Series A (A2, Jul 2026) [CONFIRMED] | ~$134M Series A total [CONFIRMED] | Bessemer, Matter Venture Partners, B Capital | Active | [12](categories/12_eda_ip_and_design_tools.md) |
| ChipStack | 12 EDA/IP | Seattle, US | 2023 | Acquired by Cadence (Nov 2025) [CONFIRMED] | [TO VERIFY] | [TO VERIFY] | Acquired | [12](categories/12_eda_ip_and_design_tools.md) |
| Codasip | 12 EDA/IP | Brno, CZ | 2014 | In sale process since Jul 2025 [CONFIRMED]; partial divestiture reported [UNCONFIRMED] | ~EUR119M grants+equity [CONFIRMED] | Smart Eureka, Eurazeo | Active | [12](categories/12_eda_ip_and_design_tools.md) |
| Cognichip | 12 EDA/IP | Redwood City, US | 2024 | Series A ($60M, Apr 2026) [CONFIRMED] | ~$93M [CONFIRMED] | Seligman Ventures, Mayfield, Lux Capital | Active | [12](categories/12_eda_ip_and_design_tools.md) |
| Corintis | 16 DC Infra | Lausanne, CH | 2022 | Series A | ~$24M [TO VERIFY] | [TO VERIFY] | Active | [16](categories/16_datacenter_infrastructure_enablers.md) |
| Cornelis Networks | 05 Networking/Interconnect | Chesterbrook, US | 2020 | Growth ($205M, Sep 2026) [CONFIRMED] | ~$335M [TO VERIFY] | IAG Capital Partners, Chevron Technology Ventures, DCVC | Active | [05](categories/05_networking_and_interconnect.md) |
| d-Matrix | 02 Inference | Santa Clara, US | 2019 | Series C ($275M at ~$2B, Nov 2025) [CONFIRMED]; bought GigaIO DC unit (Apr 2026) | ~$450M [CONFIRMED] | Bullhound Capital, Triatomic Capital, Temasek | Active | [02](categories/02_inference_accelerators.md) |
| DeepX | 03 Edge Inference | Seongnam, KR | 2018 | Series D / pre-IPO [TO VERIFY] | ~$150M+ [ESTIMATED] | SkyLake, BNW | Active | [03](categories/03_edge_inference_chips.md) |
| DreamBig Semiconductor | 05 Networking/Interconnect | San Jose, US | 2019 | Acquired by Arm (~$265M, agreed Oct 2025) [CONFIRMED agreement] | ~$75-92M [TO VERIFY] | Samsung | Acquired | [05](categories/05_networking_and_interconnect.md) |
| Eliyan | 04 Custom ASIC/Chiplets | Santa Clara, US | 2021 | Series B + strategic (Jan 2026) [TO VERIFY] | ~$150M [TO VERIFY] | Samsung Catalyst, Tiger Global, Intel Capital | Active | [04](categories/04_custom_asic_and_chiplets.md) |
| Empower Semiconductor | 08 Power | San Jose, US | 2014 | Acquired by Analog Devices ($1.5B cash, closed 2026-07-07) [CONFIRMED] | ~$200M+ [ESTIMATED] | Fidelity, CapitalG, Sutter Hill, Intel Capital | Acquired | [08](categories/08_power_semiconductors_and_power_delivery.md) |
| EnCharge AI | 14 Analog/In-Memory | Santa Clara, US | 2022 | Series B ($100M, Feb 2025) [CONFIRMED] | ~$144M+ [CONFIRMED] | Tiger Global, RTX Ventures, In-Q-Tel | Active | [14](categories/14_quantum_neuromorphic_and_non_von_neumann.md) |
| Enfabrica | 05 Networking/Interconnect | Mountain View, US | 2020 | NVIDIA tech licence + CEO/team hire (>$900M, Sep 2025) [CONFIRMED structure] | ~$260M | Atreides, Sutter Hill, NVIDIA | Licensed/Acqui-hired | [05](categories/05_networking_and_interconnect.md) |
| Etched | 02 Inference | San Jose, US | 2022 | Growth ($500M at $5B Jan 2026 [CONFIRMED]; $300M at $10.3B Jul 2026 and $700M at ~$21B Aug 2026 [TO VERIFY]) | ~$1.1B-1.8B [ESTIMATED] | Stripes, Sequoia, Jane Street, Primary Venture Partners | Active | [02](categories/02_inference_accelerators.md) |
| Fab2 (formerly Atomic Semi) | 13 Foundry/Packaging | Austin, US [TO VERIFY] | 2022 | Series A (~$500M at ~$3.7B reported) [UNCONFIRMED] | [UNCONFIRMED] | Founders Fund | Active | [13](categories/13_foundry_packaging_and_chiplet_integration.md) |
| Fabric Cryptography | 09 Security/Crypto | San Francisco, US | 2022 | Series A | ~$39M [CONFIRMED] | Blockchain Capital, 1kx | Active | [09](categories/09_security_crypto_and_confidential_compute.md) |
| Fractile | 02 Inference | London, UK | 2022 | Series B ($220M, May 2026) [CONFIRMED] | ~$240M [ESTIMATED] | Accel, Founders Fund, Factorial Funds | Active | [02](categories/02_inference_accelerators.md) |
| FuriosaAI | 02 Inference | Seoul, KR | 2017 | Series D ($620M at ~$2.9B, Oct 2026) [CONFIRMED] | ~$0.9-1B [ESTIMATED] | Korea National Growth Fund, DSC Investment, Naver | Active | [02](categories/02_inference_accelerators.md) |
| Graphcore | 01 Training | Bristol, UK | 2016 | Acquired (SoftBank, 2024) | ~$700M raised | Sequoia, BMW i Ventures | Acquired | [01](categories/01_training_accelerators.md) |
| Groq | 02 Inference | Mountain View, US | 2016 | NVIDIA non-exclusive licence + leadership hire (~$20B reported, Dec 2025); GroqCloud continues under CEO Simon Edwards | ~$2.5-3B [ESTIMATED] | Disruptive, BlackRock, Samsung Catalyst, Cisco | Licensed/Acqui-hired | [02](categories/02_inference_accelerators.md) |
| Hailo | 03 Edge Inference | Tel Aviv, IL | 2017 | Acquired by Microchip (agreed Jul 2026; closed 2026-09-21) [CONFIRMED] | ~$340M+ [TO VERIFY] | Poalim Equity, Gil Agmon | Acquired | [03](categories/03_edge_inference_chips.md) |
| Kinara | 03 Edge Inference | Los Altos, US | 2013 | Acquired by NXP ($307M, closed 2025-10-27) [CONFIRMED] | [TO VERIFY] | [TO VERIFY] | Acquired | [03](categories/03_edge_inference_chips.md) |
| Lace Lithography | 13 Foundry/Packaging | Bergen, NO | 2023 | Series A ($40M, Mar 2026) [CONFIRMED] | ~$60M | Atomico, M12, Nysno | Active | [13](categories/13_foundry_packaging_and_chiplet_integration.md) |
| Lightmatter | 06 Optical/CPO | Mountain View, US | 2017 | Series D ($400M at $4.4B, Oct 2024) [CONFIRMED]; no confirmed 2026 round | ~$850M | T. Rowe Price, GV, Fidelity | Active | [06](categories/06_optical_interconnect_and_cpo.md) |
| Lumilens | 06 Optical/CPO | [TO VERIFY] | 2024 | Series C ($700M+ at $5.51B, Aug 2026) [CONFIRMED] | ~$900M+ [TO VERIFY] | Atreides, Bain Capital Ventures, Meritech, Spark Capital | Active | [06](categories/06_optical_interconnect_and_cpo.md) |
| Majestic Labs | 07 Memory/CXL | US / IL | 2023 | Series A (~$100M total, Nov 2025) [CONFIRMED] | ~$100M | Bow Wave Capital, Grove Ventures | Active | [07](categories/07_memory_and_storage.md) |
| MatX | 01 Training | Mountain View, US | 2022 | Series B ($500M, Feb 2026) [CONFIRMED] | ~$600M+ [ESTIMATED] | Jane Street, Situational Awareness, Spark Capital | Active | [01](categories/01_training_accelerators.md) |
| Mythic | 14 Analog/Edge | Austin, US | 2012 | Growth (recapitalized; ~$125M Dec 2025 [UNCONFIRMED]) | ~$165M+ prior [TO VERIFY] | DCVC, Lux Capital, SoftBank | Active | [14](categories/14_quantum_neuromorphic_and_non_von_neumann.md) |
| NEO Semiconductor | 07 Memory/CXL | San Jose, US | 2012 | Strategic round (Apr 2026) [CONFIRMED] | Undisclosed | Stan Shih-led consortium | Active | [07](categories/07_memory_and_storage.md) |
| NeuReality | 02 Inference | Caesarea, IL | 2019 | Being acquired by Unconventional AI (announced 2026-10-26) [CONFIRMED] | ~$105M [TO VERIFY] | [TO VERIFY] | Acquired (pending) | [02](categories/02_inference_accelerators.md) |
| Neurophos | 06 Optical/CPO (photonic compute) | Austin, US [TO VERIFY] | 2020 | Series A ($110M, Jan 2026) [CONFIRMED] | ~$118M | Gates Frontier, M12 | Active | [17](categories/17_emerging_research_to_startup_pipeline.md) |
| nEye | 06 Optical/CPO | Santa Clara, US | 2021 | Series C ($80M, Apr 2026) [CONFIRMED] | ~$152M [CONFIRMED] | Sutter Hill, CapitalG | Active | [06](categories/06_optical_interconnect_and_cpo.md) |
| Niobium | 09 Security/Crypto | Dayton, US | 2023 | Seed+ ($23M+ follow-on, Dec 2025) [CONFIRMED] | ~$28M+ [CONFIRMED] | Fusion Fund, Morgan Creek, Rev1 Ventures | Active | [09](categories/09_security_crypto_and_confidential_compute.md) |
| Normal Computing | 14 Thermodynamic/AI-EDA | New York, US | 2022 | Growth ($50M, Mar 2026) [CONFIRMED] | ~$85M+ [CONFIRMED] | Samsung Catalyst | Active | [14](categories/14_quantum_neuromorphic_and_non_von_neumann.md) |
| Nubis Communications | 06 Optical/CPO | New Providence, US | 2020 | Acquired by Ciena ($270M cash, announced Sep 2025) [CONFIRMED] | ~$120M+ [TO VERIFY] | Matrix Partners | Acquired | [06](categories/06_optical_interconnect_and_cpo.md) |
| OpenLight | 06 Optical/CPO | Goleta, US | 2022 | Series A-1 ($50M, Apr 2026) [CONFIRMED] | ~$84M [CONFIRMED] | Xora Innovation, Capricorn | Active | [06](categories/06_optical_interconnect_and_cpo.md) |
| Optalysys | 09 Security/Crypto | Leeds, UK | 2013 | Series A ext. (GBP23M, Jan 2026) [CONFIRMED] | ~$59M [ESTIMATED] | Northern Gritstone, imec.xpand, NSSIF | Active | [09](categories/09_security_crypto_and_confidential_compute.md) |
| Panmnesia | 07 Memory/CXL | Daejeon, KR | 2022 | Series A+ | ~$80-100M [TO VERIFY] | Daekyo Investment, SL Investment | Active | [07](categories/07_memory_and_storage.md) |
| Positron AI | 02 Inference | Reno, US | 2023 | Series B ($230M at >$1B, Feb 2026) [CONFIRMED] | ~$300M+ [ESTIMATED] | ARENA Private Wealth, Jump Trading, Unless, Valor | Active | [02](categories/02_inference_accelerators.md) |
| PowerLattice | 08 Power | Vancouver WA, US | 2023 | Growth (Form D: $86M of $111M, Oct 2026) [CONFIRMED] | ~$86M+ | [TO VERIFY] | Active | [08](categories/08_power_semiconductors_and_power_delivery.md) |
| PsiQuantum | 14 Quantum | Palo Alto, US | 2016 | Series E ($1B at ~$7B, Sep 2025) [CONFIRMED] | ~$2.3B+ [ESTIMATED] | BlackRock, Temasek, Baillie Gifford | Active | [14](categories/14_quantum_neuromorphic_and_non_von_neumann.md) |
| Quadric | 03 Edge Inference | Burlingame, US | 2016 | Series C | ~$72-90M [TO VERIFY] | Accelerate Fund, Volta | Active | [03](categories/03_edge_inference_chips.md) |
| Quantinuum | 14 Quantum | Broomfield, US / Cambridge, UK | 2021 | Public (Nasdaq: QNT, IPO Jun 2026, ~$1.68B raised) [CONFIRMED] | ~$1.6B+ private [ESTIMATED] + IPO | Honeywell | Public | [14](categories/14_quantum_neuromorphic_and_non_von_neumann.md) |
| Rain AI | 14 Analog/Neuromorphic | San Francisco, US | 2017 | Wound down; patents sold to OpenAI (Aug 2026) [TO VERIFY] | ~$60M+ [TO VERIFY] | Prosperity7, Sam Altman | Shut Down | [14](categories/14_quantum_neuromorphic_and_non_von_neumann.md) |
| Rebellions | 02 Inference | Seongnam, KR | 2020 | Pre-IPO ($400M at ~$2.34B, Mar 2026) [CONFIRMED] | ~$850M [ESTIMATED] | Mirae Asset, Korea National Growth Fund, KT, Arm | Active | [02](categories/02_inference_accelerators.md) |
| Ricursive Intelligence | 12 EDA/IP | SF Bay Area, US [TO VERIFY] | 2025 | Series A ($300M at ~$4B, Jan 2026) [CONFIRMED] | ~$335M [CONFIRMED] | Lightspeed, Sequoia | Active | [12](categories/12_eda_ip_and_design_tools.md) |
| Rivos | 04 Custom ASIC/RISC-V | Santa Clara, US | 2021 | Acquired by Meta (2025, terms undisclosed) [CONFIRMED] | ~$250M+ [TO VERIFY] | Matrix Partners, Intel Capital, MediaTek | Acquired | [04](categories/04_custom_asic_and_chiplets.md) |
| Sagence AI | 14 Analog/In-Memory | Santa Clara, US | 2018 | Series A+ (not re-verified) | [TO VERIFY] | [TO VERIFY] | Active | [14](categories/14_quantum_neuromorphic_and_non_von_neumann.md) |
| Salience Labs | 06 Optical/CPO | Oxford, UK | 2021 | Series B ($125M, Oct 2026) [CONFIRMED] | ~$165M+ [ESTIMATED] | Bullhound Capital, AMD Ventures, Intel Capital | Active | [06](categories/06_optical_interconnect_and_cpo.md) |
| SambaNova Systems | 01 Training/Inference | Palo Alto, US | 2017 | Series E ($350M, Feb 2026) after Intel acquisition talks stalled; Intel stake ~8.2% [CONFIRMED] | ~$1.5B+ [ESTIMATED] | SoftBank, BlackRock, Intel Capital | Active | [01](categories/01_training_accelerators.md) |
| SiFive | 04 Custom ASIC/Chiplets | Santa Clara, US | 2015 | Series G ($400M at $3.65B, Apr 2026; pre-IPO) [CONFIRMED] | ~$766M [ESTIMATED] | Atreides, NVIDIA, Apollo, Sutter Hill | Active | [04](categories/04_custom_asic_and_chiplets.md) |
| SiMa.ai | 03 Edge Inference | San Jose, US | 2018 | Series C (~$150M at ~$1.45B, 2026) [TO VERIFY] | ~$500M+ [TO VERIFY] | Fidelity, Maverick, Amplify Partners | Active | [03](categories/03_edge_inference_chips.md) |
| SiTime | 11 Analog/Timing | Santa Clara, US | 2005 | Public (NASDAQ: SITM); acquired Renesas timing business (closed 2026-07-01) [CONFIRMED] | (public) | (public) | Public | [11](categories/11_analog_mixed_signal_and_timing.md) |
| Substrate | 13 Foundry/Packaging | San Francisco, US | 2022 | ~$100M at >$1B (Oct 2025) [CONFIRMED] | >$100M | Founders Fund, General Catalyst, Valor, In-Q-Tel | Active | [13](categories/13_foundry_packaging_and_chiplet_integration.md) |
| Taalas | 02 Inference | Toronto, CA | 2023 | Being acquired by AMD (announced 2026-08-06) [CONFIRMED] | ~$219M [CONFIRMED] | Quiet Capital, Fidelity, Pierre Lamond | Acquired (pending) | [02](categories/02_inference_accelerators.md) |
| Tensordyne (formerly Recogni) | 15 Automotive/Inference | San Jose, US | 2017 | Series C; renamed Sept 2025; Series D in preparation [TO VERIFY] | ~$175M+ [TO VERIFY] | Celesta, GreatPoint, BMW i Ventures | Active | [15](categories/15_autonomous_robotics_and_automotive_silicon.md) |
| Tenstorrent | 01 Training/Inference | Toronto, CA | 2016 | Series E ($1.5B at ~$6.2B, Oct 2026) [CONFIRMED] | ~$2.5B+ [ESTIMATED] | Trace Capital, Innovation X, Samsung, AFW Partners | Active | [01](categories/01_training_accelerators.md) |
| Teramount | 06 Optical/CPO | Jerusalem, IL | 2013 | Acquired by Molex (closed 2026-05-07) [CONFIRMED] | ~$58M | Koch Disruptive Technologies, AMD, Samsung | Acquired | [06](categories/06_optical_interconnect_and_cpo.md) |
| Unconventional AI | 14 Non-von-Neumann | Bay Area, US [TO VERIFY] | 2025 | Seed (~$475M at ~$4.5B, Dec 2025) [CONFIRMED]; acquiring NeuReality (Oct 2026) | ~$475M [CONFIRMED] | Andreessen Horowitz, Lightspeed | Active | [14](categories/14_quantum_neuromorphic_and_non_von_neumann.md) |
| UnifabriX | 07 Memory/CXL | Yokneam, IL | 2020 | Seed/A | ~$11M [TO VERIFY] | Grove Ventures, Harel | Active | [07](categories/07_memory_and_storage.md) |
| Untether AI | 02 Inference | Toronto, CA | 2018 | Wound down; engineering team hired by AMD (Jun 2025) [CONFIRMED] | ~$150M raised | Intel Capital, Tracker Capital, CPPIB | Shut Down | [02](categories/02_inference_accelerators.md) |
| Upscale AI | 05 Networking/Interconnect | Santa Clara, US [TO VERIFY] | 2024 | Series A ($200M, Jan 2026) [CONFIRMED] + A-1 ($190M at ~$2B, Jun 2026) [TO VERIFY] | ~$500M [TO VERIFY] | Tiger Global, Mayfield, NVIDIA, Intel Capital, Qualcomm Ventures | Active | [05](categories/05_networking_and_interconnect.md) |
| Ventana Micro Systems | 04 Custom ASIC/RISC-V | Cupertino, US | 2018 | Acquired by Qualcomm (Dec 2025) [CONFIRMED] | [TO VERIFY] | [TO VERIFY] | Acquired | [04](categories/04_custom_asic_and_chiplets.md) |
| XCENA | 07 Memory/CXL | KR | 2021 | Series B ($135M at ~$570M, May 2026) [CONFIRMED] | ~$185M | Atinum Investment, IMM Investment | Active | [07](categories/07_memory_and_storage.md) |
| xLight | 13 Foundry/Packaging | Palo Alto, US [TO VERIFY] | 2021 | Series B + up to $150M US CHIPS equity [CONFIRMED] | $40M + gov. equity | Playground Global, US Dept. of Commerce | Active | [13](categories/13_foundry_packaging_and_chiplet_integration.md) |
| Xscape Photonics | 06 Optical/CPO | New York, US | 2022 | Series A ext. ($37M, Mar 2026) [CONFIRMED] | ~$95M [TO VERIFY] | Addition, IAG Capital Partners, NVIDIA | Active | [06](categories/06_optical_interconnect_and_cpo.md) |
| Xsight Labs | 05 Networking/Interconnect | Kiryat Gat, IL | 2017 | Growth (>$300M at $2.8B, Jul 2026) [CONFIRMED] | ~$530M+ [ESTIMATED] | Fidelity, Intel Capital, Atreides, Valor | Active | [05](categories/05_networking_and_interconnect.md) |

> 81 companies: marquee and representative entries, including exited ones (see the Status column). See the category files for the full set (~175 table entries, some cross-listed) and lighter-coverage entries. Counts in the dashboard reflect total entries per file.

---

## Master Investor Index

> Auto-generated from `data/investor_index.yaml`. See [21_vc_investor_tracker.md](deal_tracker/21_vc_investor_tracker.md) and [24_strategic_investor_tracker.md](deal_tracker/24_strategic_investor_tracker.md) for full profiles.

| Investor | Type | Semi Focus | AI Infra Focus | Relevant Portfolio | Stage Pref | Notes |
|----------|------|-----------|----------------|--------------------|-----------|-------|
| 1789 Capital | Growth | Low | High | Cerebras | Growth | Listed pre-IPO Cerebras backer [TO VERIFY] |
| Accel | VC/Growth | Medium | High | Fractile | A-Growth | Co-led Fractile $220M B at ~$1B May 2026 [CONFIRMED] |
| AMD Ventures | Strategic | High | High | TensorWave, Ayar Labs, Liquid AI | A-Growth | Co-led TensorWave $350M B Jun 2026; AMD up to $5B in Anthropic Jul 2026 [CONFIRMED] |
| Andreessen Horowitz (a16z) | VC/Growth | Medium | High | Etched, Unconventional AI | Seed-Growth | Etched C participant [TO VERIFY]; co-led Unconventional AI mega-seed Dec 2025 [TO VERIFY] |
| ARK Invest | Crossover | Medium | High | Ayar Labs, Tenstorrent | Growth | Ayar E Mar 2026 [CONFIRMED]; Tenstorrent E Oct 2026 [TO VERIFY] |
| Arm | Strategic | High | High | Rebellions, Positron AI | B-Growth | Anchored Rebellions ~$250M Sep 2025; Positron B Feb 2026 [CONFIRMED] |
| Atreides Management | Crossover | High | High | Cerebras, Enfabrica, Positron AI | B-Growth | Public/private crossover; Positron B Feb 2026; Cerebras IPO May 2026 |
| Benchmark | VC | Medium | High | Cerebras, Quilter | Early-Growth | ~$225M into Cerebras via special infrastructure vehicles [TO VERIFY] |
| Bullhound Capital | VC/Growth | High | High | d-Matrix | B-C | Co-led d-Matrix $275M C Nov 2025 with Triatomic and Temasek [CONFIRMED] |
| Celesta Capital | VC | High | High | Recogni, Auradine, Stathera, Normal Computing | A-C | India deep-tech fund planned Mar 2026 [UNCONFIRMED] |
| Cisco Investments | Strategic | Medium | High | Groq, FuriosaAI | B-Growth | FuriosaAI $620M D Oct 2026 participant [TO VERIFY] |
| Cloudberry VC | VC | High | Medium |  | Pre-seed-A | EUR 30M European semiconductor fund May 2026, GlobalFoundries strategic LP [TO VERIFY] |
| DCVC | VC | High | High | Cornelis Networks, Mythic, Agile Analog | Seed-B | Deep-tech/compute; no verified new AI-chip lead in Refresh #3 |
| Disruptive | Growth | Medium | High | Groq | Growth | Led Groq $750M Sep 2025; >$500M invested; NVIDIA licence payout Dec 2025 [CONFIRMED] |
| Eclipse Ventures | VC | High | High | Cerebras | Seed-Growth | Raised $1.3B Fund VI + Early Growth III Apr 2026 [CONFIRMED]; Cerebras IPO May 2026 |
| Factorial Funds | VC | Medium | High | Fractile | A-B | Co-led Fractile $220M B May 2026 [CONFIRMED] |
| Fidelity / BlackRock / T. Rowe Price | Crossover | High | High | Cerebras, Groq, Lightmatter, Celestial AI, Tenstorrent | Growth/Pre-IPO | Pre-IPO bridge; Fidelity and T. Rowe in Tenstorrent $1.5B E Oct 2026; BlackRock in Groq (NVIDIA licence payout) |
| Founders Fund | VC/Growth | Medium | High | Fractile | A-Growth | Co-led Fractile $220M B May 2026 [CONFIRMED] |
| Intel Capital | Strategic | High | Medium | Rivos, Eliyan, Empower Semiconductor, Movellus, SambaNova | Seed-Growth | Spin-out reversed Apr 2025 - remains in-house, monetising portfolio [CONFIRMED] |
| Jane Street | Crossover | High | High | MatX, Etched | B-Growth | Led MatX $500M B Feb 2026 [CONFIRMED]; led Etched D ~$700M at ~$21B Aug 2026 [TO VERIFY] |
| Jump Trading | Crossover | Medium | High | Positron AI | B-Growth | Co-led Positron $230M B with ARENA Private Wealth and Unless Feb 2026 [CONFIRMED] |
| Korea National Growth Fund | Sovereign | High | High | Rebellions, FuriosaAI | Growth/Pre-IPO | Rebellions pre-IPO Mar 2026; ~$280M of FuriosaAI $620M D Oct 2026 [TO VERIFY amount] |
| Lightspeed Venture Partners | VC/Growth | Medium | High | Unconventional AI | Seed-Growth | Co-led Unconventional AI mega-seed Dec 2025 [TO VERIFY] |
| Lux Capital | VC | High | High | Mythic | Seed-B | Frontier hardware; no verified new AI-chip lead in Refresh #3 |
| M12 (Microsoft) | Strategic | Medium | High | d-Matrix | A-Growth | Follow-on in d-Matrix $275M C Nov 2025 [CONFIRMED] |
| Magnetar | Crossover | Low | High | TensorWave | Growth | Co-led TensorWave $350M B with AMD Ventures Jun 2026 [CONFIRMED] |
| Marvell | Strategic | High | High | Celestial AI, MatX | Growth/M&A | Closed Celestial AI acquisition 2 Feb 2026 [CONFIRMED]; MatX B participant [TO VERIFY] |
| Matrix Partners | VC | High | High | Rivos, Baya Systems, Lightmatter | Seed-B | Compute infra/IP; Rivos acquired by Meta 2025 [TO VERIFY] |
| Maverick Silicon | VC/Growth | High | High | Celestial AI, SiMa.ai, Ethernovia, Kandou AI, Upscale AI, Point2 Technology, Stathera, TensorWave | A-Growth | Maverick Capital semi division; most active 2026 specialist (interconnect/networking); Celestial exit to Marvell Feb 2026 |
| MediaTek | Strategic | High | High | Ayar Labs, Stathera | A-Growth | Ayar Labs E Mar 2026 with Alchip, AMD, NVIDIA [CONFIRMED] |
| Mirae Asset | Growth | High | High | Rebellions, d-Matrix | B-Pre-IPO | Co-led Rebellions ~$400M pre-IPO at ~$2.34B Mar 2026 [CONFIRMED] |
| Neuberger Berman | Crossover | Medium | High | Ayar Labs | Growth/Pre-IPO | Led Ayar Labs $500M E at ~$3.75B Mar 2026 [CONFIRMED] |
| NVIDIA (NVentures) | Strategic | High | High | Enfabrica, Xscape Photonics, Ayar Labs, Groq, Intel | A-Growth | Ecosystem signal + acquirer; Groq ~$20B licence Dec 2025; direct stakes Intel $5B, Synopsys $2B, Nokia, Anthropic, OpenAI |
| Playground Global | VC | High | High | d-Matrix | Seed-A | Hard-tech silicon |
| Qatar Investment Authority | Sovereign | Medium | High | d-Matrix, Ayar Labs, Positron AI | B-Growth | d-Matrix C Nov 2025, Positron B Feb 2026, Ayar E Mar 2026 [CONFIRMED] |
| Qualcomm Ventures | Strategic | High | Medium | Upscale AI, Auradine | Seed-Growth | Qualcomm closed Alphawave ~$2.4B Dec 2025; $150M India AI fund Feb 2026 [CONFIRMED] |
| Samsung Catalyst Fund | Strategic | High | High | Tenstorrent, Groq, Blaize, Axelera AI, Eliyan, Normal Computing, Rebellions | A-Growth | Memory/foundry adjacency; led Normal Computing $50M Mar 2026 [TO VERIFY] |
| Sequoia Capital | VC/Growth | Medium | High | Etched, Ayar Labs | A-Growth | Reportedly led Etched $300M C at ~$10.3B Jul 2026 [TO VERIFY]; Ayar E via Sequoia Global Equities |
| Situational Awareness LP | Crossover | Medium | High | MatX | B-Growth | Co-led MatX $500M B Feb 2026 [CONFIRMED] |
| SK hynix | Strategic | High | High | Rebellions, Etched | B-Growth | HBM/CXL; Rebellions pre-IPO Mar 2026; Etched C Jul 2026 [TO VERIFY] |
| SoftBank Group | Strategic | High | High | Ampere, Graphcore, SambaNova | Growth/M&A | Closed Ampere $6.5B Nov 2025 [CONFIRMED]; Vision Fund 2 led SambaNova 2021 |
| Spark Capital | VC | Medium | High | MatX | A-B | Led MatX A; in MatX B Feb 2026 |
| Sutter Hill Ventures | VC | High | High | Astera Labs, Enfabrica, Empower Semiconductor | Seed-A | Deep silicon incubation track record; Enfabrica team to NVIDIA and Empower to ADI reported [TO VERIFY] |
| Temasek | Sovereign | High | High | d-Matrix, Rebellions, PsiQuantum | B-Growth | Co-led d-Matrix $275M Series C at ~$2B Nov 2025 [CONFIRMED] |
| Tiger Global | Crossover | Medium | High | Cerebras, EnCharge AI, Eliyan | B-Growth | Reportedly led Cerebras ~$1B at ~$23B Feb 2026 [TO VERIFY] |
| Trace Capital | Growth | Medium | High | Tenstorrent | Growth | New 2026 firm; co-led Tenstorrent $1.5B E at $6.2B Oct 2026 with Innovation X Advisors |
| Valor Equity Partners | Growth | Medium | High | Positron AI, Cerebras | A-Growth | Co-led Positron A 2025; in Positron B Feb 2026 [CONFIRMED] |
| Walden Catalyst | VC | High | Medium | SambaNova | A-Growth | Lip-Bu Tan network; founder now Intel CEO - conflict-of-interest diligence |

---

## Master Researcher Index

> Auto-generated from `data/researcher_index.yaml` via `scripts/build_index.py researchers`. See [researchers/leading_researchers_index.md](researchers/leading_researchers_index.md) for full profiles (organized by domain). **VC Relevance Score: 1–5.** 62 researchers across architecture, efficient ML, memory/PIM, interconnect, photonics, analog/IMC, EDA, packaging, power, and quantum (10 added in Refresh #3, incl. new founders).

| Researcher | Institution | Research Area | Patent Activity | Startup Signals | VC Relevance | Profile |
|------------|-------------|---------------|-----------------|-----------------|:------------:|---------|
| Albert Gu | Carnegie Mellon / Cartesia (co-founder) | State-space models (S4, Mamba), efficient sequence models | Low | Confirmed (Cartesia) | 4 | [profile](researchers/leading_researchers_index.md) |
| Alexander Gaeta | Columbia | Nonlinear/quantum photonics, Kerr frequency combs | Medium | Confirmed (Xscape Photonics co-founder) [TO VERIFY] | 4 | [profile](researchers/leading_researchers_index.md) |
| Amin Vahdat | Google | DC networking, optical circuit switching | High | Watchlist (incumbent) | 5 | [profile](researchers/leading_researchers_index.md) |
| Azalia Mirhoseini & Anna Goldie | Ricursive Intelligence (Goldie CEO / Mirhoseini CTO) / Stanford (Mirhoseini); ex-Google DeepMind | RL for chip placement (AlphaChip) | Medium | Confirmed (Ricursive Intelligence; $300M Series A @ $4B, Jan 2026) | 5 | [profile](researchers/leading_researchers_index.md) |
| Bill Dally | Stanford / NVIDIA | Accelerator arch, interconnect | High | Watchlist (incumbent) | 5 | [profile](researchers/leading_researchers_index.md) |
| Brucek Khailany | NVIDIA | ML for EDA, agile VLSI | High | Watchlist (incumbent) | 4 | [profile](researchers/leading_researchers_index.md) |
| Christopher Re | Stanford / SambaNova, Together AI (co-founder) | ML systems, SSMs, data-centric ML | Medium | Confirmed (serial; no new co. found 2026) | 5 | [profile](researchers/leading_researchers_index.md) |
| Daniel Sanchez | MIT | Scalable arch, memory hierarchy, sparse accel | Low | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Danyal Akarca & Jascha Achterberg | Callosum (co-founders); academic neuroscience/ML background [TO VERIFY affiliations] | Brain-inspired heterogeneous compute orchestration | Low | Confirmed (Callosum; $100M seed, Aug 2026) | 4 | [profile](researchers/leading_researchers_index.md) |
| David Brooks & Gu-Yeon Wei | Harvard | Energy-efficient arch, edge accel SoCs | Medium | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| David Patterson | UC Berkeley / Google | RISC-V, DSAs, TPU | Medium | Watchlist | 5 | [profile](researchers/leading_researchers_index.md) |
| David Perreault | MIT | High-density power conversion | High | Confirmed (serial) | 4 | [profile](researchers/leading_researchers_index.md) |
| David R. Smith | Duke University | Metamaterials, metasurface optics | High | Confirmed (lab lineage: Neurophos, Kymeta, Metacept) | 4 | [profile](researchers/leading_researchers_index.md) |
| David Z. Pan | UT Austin | ML for EDA, physical design, analog automation | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Deming Chen | UIUC | HLS, hardware-aware ML, accelerators | Medium | Likely (Inspirit IoT) | 3 | [profile](researchers/leading_researchers_index.md) |
| Dirk Englund | MIT | Photonic computing, quantum photonics | High | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Dmitri Strukov | UC Santa Barbara | Memristive devices, analog NN HW | High | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| Edoardo Charbon | EPFL | Cryogenic CMOS, quantum control | High | Likely | 3 | [profile](researchers/leading_researchers_index.md) |
| H.-S. Philip Wong | Stanford | Emerging memory, IMC, 3D | High | Likely | 5 | [profile](researchers/leading_researchers_index.md) |
| Hadi Esmaeilzadeh | UC San Diego | Accelerators, near-data, serving systems | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Jason Cong | UCLA | FPGA/HLS, EDA, customized computing | High | Confirmed (serial) | 5 | [profile](researchers/leading_researchers_index.md) |
| Jelena Vuckovic | Stanford | Nanophotonics, inverse design, quantum photonics | Medium | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Joel Emer | MIT / NVIDIA | Accelerator modeling, sparse tensor accel | Medium | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| John Bowers | UC Santa Barbara | Lasers on silicon, photonics | High | Likely | 5 | [profile](researchers/leading_researchers_index.md) |
| John Martinis | UC Santa Barbara (ex-Google) | Superconducting qubits | High | Confirmed (Qolab) | 4 | [profile](researchers/leading_researchers_index.md) |
| Kaushik Roy | Purdue | Neuromorphic, emerging-device IMC | High | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Keren Bergman | Columbia | Silicon photonics, optical interconnect | High | Confirmed (Xscape Photonics co-founder) [TO VERIFY] | 5 | [profile](researchers/leading_researchers_index.md) |
| Khurram Afridi | Cornell | High-frequency power conversion | Medium | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| Krste Asanovic | UC Berkeley / SiFive | RISC-V, vector arch | Medium | Confirmed (SiFive) | 5 | [profile](researchers/leading_researchers_index.md) |
| Kunle Olukotun | Stanford / SambaNova | Reconfigurable dataflow (RDA) | High | Confirmed (SambaNova; Intel sale talks stalled Jan 2026 [TO VERIFY outcome]) | 5 | [profile](researchers/leading_researchers_index.md) |
| Liam Fedus & Ekin Dogus Cubuk | Periodic Labs (co-founders); ex-OpenAI / Google DeepMind | AI-driven materials discovery (incl. superconductors) | Low | Confirmed (Periodic Labs, 2025) [TO VERIFY round size] | 3 | [profile](researchers/leading_researchers_index.md) |
| Marin Soljacic | MIT | Photonic computing, nanophotonics | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Mark Horowitz | Stanford | Circuits, agile hardware | High | Confirmed (legacy) | 4 | [profile](researchers/leading_researchers_index.md) |
| Mattan Erez | UT Austin | Memory systems, accelerator memory | Medium | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| Michael Carbin | MIT / Unconventional AI (co-founder) | Programming systems, approximate & analog computation | Low | Confirmed (Unconventional AI) | 4 | [profile](researchers/leading_researchers_index.md) |
| Michal Lipson | Columbia | Silicon photonics, combs, programmable photonics | High | Likely | 5 | [profile](researchers/leading_researchers_index.md) |
| Mikhail Lukin | Harvard | Neutral-atom quantum computing | High | Confirmed (QuEra) | 4 | [profile](researchers/leading_researchers_index.md) |
| Moinuddin Qureshi | Georgia Tech | Memory systems, CXL, memory security | Medium | Watchlist | 3 | [profile](researchers/leading_researchers_index.md) |
| Muhannad Bakir | Georgia Tech | Heterogeneous integration, interposers, thermal | High | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Myoungsoo Jung | KAIST / Panmnesia | CXL systems, memory disaggregation | High | Confirmed (Panmnesia) | 5 | [profile](researchers/leading_researchers_index.md) |
| Naresh Shanbhag | UIUC | Deep in-memory architecture (DIMA) | High | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Naveen Rao | Unconventional AI (CEO); ex-Databricks, MosaicML, Nervana | Analog / energy-efficient AI computers | Medium | Confirmed (serial; Unconventional AI $475M seed, Dec 2025) | 5 | [profile](researchers/leading_researchers_index.md) |
| Naveen Verma | Princeton / EnCharge AI | Analog in-memory compute | High | Confirmed (EnCharge) | 5 | [profile](researchers/leading_researchers_index.md) |
| Onur Mutlu | ETH Zurich | PIM / near-memory | High | Likely | 5 | [profile](researchers/leading_researchers_index.md) |
| Ramin Farjadrad | Eliyan (ex-Marvell/Aquantia) | SerDes, die-to-die interconnect | High | Confirmed (Eliyan) | 5 | [profile](researchers/leading_researchers_index.md) |
| Robert Schoelkopf | Yale | Circuit QED, bosonic error correction | High | Confirmed (Quantum Circuits) | 3 | [profile](researchers/leading_researchers_index.md) |
| Saman Amarasinghe | MIT | Compilers for accelerators (Exo/TACO/Halide) | Low | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Sara Achour | Stanford / Unconventional AI (co-founder) | Compilers for analog & unconventional hardware | Low | Confirmed (Unconventional AI) | 4 | [profile](researchers/leading_researchers_index.md) |
| Saugata Ghose | UIUC | PIM, memory systems, near-data | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Siddharth Garg | NYU | Hardware security, LLMs for HDL | Medium | Likely | 3 | [profile](researchers/leading_researchers_index.md) |
| Song Han | MIT / NVIDIA (Research Director, Efficient AI) | Model compression, efficient inference | Medium | Watchlist (inside NVIDIA; prior OmniML->NVIDIA, DeePhi->Xilinx/AMD; no new co. as of 2026-11) | 5 | [profile](researchers/leading_researchers_index.md) |
| Subhasish Mitra | Stanford | Monolithic 3D (N3XT), CNT computing | High | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Subramanian Iyer | UCLA | Heterogeneous integration, SiIF, chiplets | High | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Tomas Palacios | MIT | GaN devices, wide-bandgap power, RF | High | Confirmed (Finwave) | 4 | [profile](researchers/leading_researchers_index.md) |
| Tri Dao | Princeton / Together AI | FlashAttention (1-4), SSMs (Mamba), kernels | Low | Confirmed (Together AI co-founder/chief scientist) | 5 | [profile](researchers/leading_researchers_index.md) |
| Tushar Krishna | Georgia Tech | ML interconnect, collectives, NoC | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |
| Vijay Janapa Reddi | Harvard / MLCommons | MLPerf benchmarking, edge/TinyML | Low | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Vivienne Sze | MIT | Energy-efficient DL hardware | Medium | Watchlist | 4 | [profile](researchers/leading_researchers_index.md) |
| Vladimir Stojanovic | UC Berkeley / Ayar Labs (co-founder) | Silicon photonics, optical I/O, monolithic photonics in CMOS | High | Confirmed (Ayar Labs) | 5 | [profile](researchers/leading_researchers_index.md) |
| Wei Lu | University of Michigan | Memristor/RRAM IMC | High | Confirmed (Crossbar/MemryX) | 4 | [profile](researchers/leading_researchers_index.md) |
| William Wang | UCSB (on leave) / ChipAgents (founder, CEO) | LLM agents for RTL design & verification | Low | Confirmed (ChipAgents; $134M Series A total, company-reported) | 4 | [profile](researchers/leading_researchers_index.md) |
| Yakun Sophia Shao | UC Berkeley | Accelerator design automation, chiplets | Medium | Likely | 4 | [profile](researchers/leading_researchers_index.md) |

---

## Key Stats

> Updated on each full refresh. Last updated 2026-11-04 (Refresh #3; previous 2026-06-09). Counts reflect entries in this database, not the total market.

- **Category table entries:** ~175 across 17 category files (~150 unique companies; some cross-listed); **81** in the master company index
- **Master index status mix:** 57 active · 5 public · 13 acquired · 2 pending acquisition · 2 licensed/acqui-hired · 2 shut down
- **Stealth / semi-stealth companies tracked:** ~11 (see [STEALTH_STARTUP_DISCOVERY.md](STEALTH_STARTUP_DISCOVERY.md))
- **M&A / licensing deals tracked:** 36 (was 10)
- **Exits & shutdowns tracked:** 34 (was 8)
- **Funding rounds tracked:** 56 (was 18; ~36 dated 2025H2–2026)
- **VC/crossover/sovereign investors tracked:** 34 in tracker 21; **48** in the master investor index (was 14)
- **Strategic investors tracked:** 20 (was 12)
- **Research labs tracked:** 44 (28 university + 15 corporate in the Markdown indexes; 44 in `lab_index.yaml`)
- **Leading researchers tracked:** 62 (was 52) · **Founders indexed:** 32
- **Papers tracked:** 38 · **Patent clusters tracked:** 30
- **Disclosed private funding tracked:** ~$30B+ [ESTIMATED — sum of category-level estimates; double-counting likely], plus ~$7B+ raised in IPOs (Cerebras, Quantinuum)

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
