---
category_id: "08"
category_name: "Power Semiconductors & Power Delivery"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-08-13"
refresh_count: 2
total_companies: 6
active_companies: 5
archived_companies: 1
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$400M+ [ESTIMATED]"
top_investors: ["Sutter Hill", "Intel Capital", "Capricorn", "Fidelity"]
key_technical_inflections: ["100kW+ AI racks", "GaN/SiC adoption", "Vertical power delivery", "48V→point-of-load", "800V DC architectures"]
key_open_questions: ["Who wins datacenter GaN at scale?", "Does vertical power delivery become standard?", "Startup vs. Infineon/onsemi scale?"]
---

# 08 — Power Semiconductors & Power Delivery

> AI racks are going from ~10kW to 100kW+; power delivery and conversion efficiency are first-order datacenter problems with clean M&A exits. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis
- **Why now:** Rack power density is exploding; every watt of conversion loss is cost + heat; GaN/SiC and high-density point-of-load conversion have real pull near the GPU.
- **Venture-scale:** High in datacenter-grade GaN, integrated lateral/vertical power delivery, and 48V/800V architectures; clean M&A exits.
- **Inflections:** Vertical power delivery (under-die), GaN at 48V→PoL, 800V DC distribution, integrated power ICs.
- **Acquirers:** Infineon, Renesas, ADI, TI, Monolithic Power, onsemi, Navitas. **Exit:** strategic M&A.
- **Winning startup:** integrated power delivery IP/devices with efficiency leadership near the load. **Non-investable:** commodity discretes vs. Infineon/onsemi scale.

## 2. Market Context
- **Structure:** Power incumbents (Infineon, onsemi, STMicro, TI, ADI, MPS, Vicor, Navitas) + startups in GaN/integration.
- **Segments:** AI server VRM/PoL, rack power shelves, 48V/800V conversion, EV (adjacent).
- **Drivers:** Rack density, PUE/efficiency, copper/thermal limits, grid constraints.
- **Bottlenecks:** Device efficiency at high current, packaging/thermal, reliability, vertical integration.
- **Competitive:** Navitas/EPC (GaN), Vicor (modules), Infineon (broad); startups in integration + datacenter GaN.
- **Risks:** Incumbent scale, qualification cycles, capital intensity.

### 2026 Update — 800VDC went from roadmap to shipping (2026-08-13)

The power category's central bet — that rack power density would force an architectural change — is now a scheduled product transition rather than a forecast.

- **First 800V HVDC shipments are landing in Q3 2026.** NVIDIA's **Vera Rubin** platform and Google's next-generation datacenters are reported as the first adopters, with initial infrastructure shipments beginning in the third quarter of 2026 [TO VERIFY]. Rack power targets quoted in the ecosystem: **Rubin Ultra ~450kW/rack**, with the Feynman generation projected at **600kW–1MW** [TO VERIFY — vendor/analyst figures].
- **The incumbents have already lined up.** **Texas Instruments announced an 800V power partnership with NVIDIA in March 2026**; **STMicroelectronics** expanded its 800VDC conversion portfolio (12V and 6V architectures) in collaboration with NVIDIA; Renesas and **Navitas** positioned GaN and SiC parts into the architecture; **Vertiv** committed to a full 800VDC product line in 2026; **Delta** is shipping row-based 800V DC systems with integrated liquid cooling.
- **What this means for startups:** the architectural window is open but narrow, and it is being filled by public incumbents with qualification track records. The defensible startup positions are the ones the incumbents cannot serve quickly — **integrated vertical power delivery at the package/board level** (Empower's territory), high-voltage vertical GaN devices, and power conversion co-designed with the accelerator rather than with the rack.
- **Diligence emphasis shifts to qualification and allocation:** who is designed into a Rubin-class or Feynman-class rack, at what stage of qualification, and with what second-source position. In this category a design-in is worth more than a datasheet advantage, and the 2026–2027 sockets are being decided now.
- **Cross-reference:** this transition is also the largest single driver in [16](16_datacenter_infrastructure_enablers.md); the thermal side (liquid cooling at 450kW+/rack) moves with it.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Empower Semiconductor | US | 2014 | Growth | [TO VERIFY] | Sutter Hill, Intel Cap, Fidelity | Integrated voltage regulators (FCPM) | AI/DC vertical power delivery | Silicon-cap integrated VR, vertical power | AI/CPU PoL design wins | High | Active |
| Navitas Semiconductor | US | 2014 | Public (NVTS) | IPO 2021 | (public) | GaNFast + GeneSiC | DC power, chargers, EV | GaNIC integration; NVIDIA 800V collab [TO VERIFY] | NVIDIA 800V program | High | Active |
| Vicor | US | 1981 | Public (VICR) | (public) | (public) | Factorized power / VPD modules | AI PoL, vertical power | Vertical power delivery modules | GPU power design wins | Medium-High | Active |
| VisIC Technologies | IL | 2010 | Growth | ~$100M+ [TO VERIFY] | [TO VERIFY] | High-voltage GaN (D3GaN) | EV + DC power | High-voltage GaN | Auto/DC pilots | Medium | Active |
| Odyssey Semiconductor | US | 2016 | Public/Small | [TO VERIFY] | [TO VERIFY] | Vertical GaN power devices | High-voltage power | True vertical GaN | Early | Medium | Active |
| GaN Systems | CA | 2008 | Acquired | ~$200M+ raised | BDC, Fidelity | GaN power transistors | (now Infineon) | GaN device leader | Acquired by Infineon 2023 | Archived | Acquired |

## 4. Company Profiles

### Empower Semiconductor
- **Status:** Active · **HQ:** San Jose, US · **Founded:** 2014 · **Founders:** team incl. Steve Saletta [TO VERIFY]
- **Stage:** Growth · **Funding:** [TO VERIFY] · **Investors:** Sutter Hill Ventures, Intel Capital, Fidelity, Anzu · **Website:** empowersemi.com
- **Primary:** 08 · **Secondary:** 16 · **One-Line:** Integrated voltage regulators and vertical power delivery placing high-density conversion directly beneath the processor — built for AI compute current demands.
- **Tech:** silicon-capacitor + integrated power FET VRs (FCPM family), lateral/vertical power delivery to reduce IR loss and board area at the load. **Differentiation:** integration + transient response at AI-class currents. **Risk:** qualification cycles, incumbent response.
- **VC view:** High; acquirers = Infineon/ADI/MPS/Renesas. **Data quality:** Medium. **Last updated:** 2026-06-09.

### Navitas Semiconductor (public comparable)
- **Status:** Active (NASDAQ: NVTS) · **HQ:** Torrance, US · **Founded:** 2014
- **One-Line:** GaN (GaNFast) and SiC (GeneSiC) power ICs; publicly disclosed collaboration on NVIDIA's 800V HVDC datacenter power architecture [TO VERIFY].
- **Why it's here:** the listed comp showing datacenter power is a venture-to-public path; **the NVIDIA 800V signal reframed GaN/SiC as core AI-infra.** **Data quality:** High (public). **Last updated:** 2026-06-09.

> Vicor, VisIC, Odyssey at table level; GaN Systems archived (Infineon, 2023). Transphorm acquired by Renesas (2024) — see [../deal_tracker/20_ma_tracker.md](../deal_tracker/20_ma_tracker.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Vertical power delivery | High | High | Medium-High | Medium | Real | High |
| Datacenter GaN (48V→PoL) | High | High | Medium-High | High | Real | Medium-High |
| 800V HVDC architecture | High | High | High | Medium | Real | Medium-High |
| Integrated VR ICs | High | High | Medium | High | Real | High |
| High-voltage SiC/GaN devices | Medium | High | High | High | Narrow | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Sutter Hill | VC | Empower | Seed–Growth | Empower | Power-IC integration |
| Intel Capital | Strategic | Empower | Growth | Empower | Compute power delivery |
| Capricorn / Fidelity | VC/Crossover | Empower (adj.) | Growth | — | DC power TCO |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| MIT/CICS power electronics | MIT | High-density power conversion | Topologies for dense conversion | Watchlist | Many | 3 | Medium |
| Virginia Tech CPES | Virginia Tech | Power electronics systems | Premier power-electronics lab; talent | Watchlist | Many | 4 | Medium |
| Tomás Palacios (MIT) | MIT | GaN devices | GaN device innovation (Finwave lineage) | Likely | GaN papers | 4 | Medium |

## 8. Diligence Questions
- **Technical:** Efficiency/transient response at AI currents; thermal; reliability/qualification?
- **Market:** 48V/800V architecture alignment; design-in proximity to GPU?
- **Customer:** OEM/ODM/hyperscaler design wins committed?
- **Competitive:** Defensible vs. Infineon/onsemi/MPS scale?
- **Financial:** Capex for fab/packaging; gross margin?
- **Founder:** power-IC shipping pedigree? **Exit:** which incumbent strategic acquirer and precedent multiples (GaN Systems/Transphorm)?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 6 | 0 | 1 (GaN Systems) | Initial build; Empower profile; GaN/SiC + vertical power coverage | Company sites, public filings |
| 2026-08-13 | Full refresh | 0 | 2 (market context, thesis emphasis) | 0 | 800VDC moved from roadmap to first shipments (Q3 2026, NVIDIA Vera Rubin / Google); TI-NVIDIA and ST 800V programs, Vertiv/Delta product lines; rack power targets (Rubin Ultra ~450kW, Feynman 600kW–1MW); diligence emphasis shifted to design-in and qualification for 2026–27 sockets | Vendor announcements, trade press [many TO VERIFY] |
