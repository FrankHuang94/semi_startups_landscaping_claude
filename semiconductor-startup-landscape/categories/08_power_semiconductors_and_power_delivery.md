---
category_id: "08"
category_name: "Power Semiconductors & Power Delivery"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 13
active_companies: 10
archived_companies: 3
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$690M+ venture (incl. exited Empower, GaN Systems; excl. public comps) [ESTIMATED]"
top_investors: ["Fidelity", "Sutter Hill", "Intel Capital", "Playground Global", "CapitalG", "TDK Ventures", "Peak XV", "Foresight"]
key_technical_inflections: ["100kW→1MW AI racks", "800V HVDC (NVIDIA Kyber / Rubin Ultra, 2027)", "GaN/SiC adoption in DC power", "Integrated / vertical power delivery (IVR chiplets)", "800V→PoL direct conversion", "Solid-state DC protection"]
key_open_questions: ["Who wins datacenter GaN at 800V scale (Infineon, Navitas, Power Integrations, startups)?", "Does in-package IVR / vertical power delivery become standard after ADI–Empower?", "Startup vs. Infineon/onsemi scale?", "Can SiC suppliers recover post-Wolfspeed restructuring?"]
---

# 08 — Power Semiconductors & Power Delivery

> AI racks are going from ~10kW to 100kW+ and toward 1MW (NVIDIA Kyber, 800V HVDC); power delivery and conversion efficiency are first-order datacenter problems with clean M&A exits — validated in 2026 by **Analog Devices' $1.5B all-cash acquisition of Empower Semiconductor**. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis
- **Why now:** Rack power density is exploding; every watt of conversion loss is cost + heat; NVIDIA's 800V HVDC architecture (announced May 2025 with Navitas, Infineon, and others; targeted at Kyber racks / Rubin Ultra) reframed GaN/SiC and high-density point-of-load conversion as core AI infrastructure.
- **Venture-scale:** High in integrated voltage regulators / power-delivery chiplets, datacenter-grade GaN (incl. vertical GaN for 800V), and 800V conversion/protection; proven clean M&A exits (ADI–Empower $1.5B, 2026; Infineon–GaN Systems 2023; Renesas–Transphorm 2024).
- **Inflections:** In-package IVR / power chiplets (PowerLattice, Empower→ADI, Ferric), vertical power delivery (Vicor VPD licensing), GaN at 48V→PoL and 800V→PoL direct conversion, 800V DC distribution, solid-state circuit protection, software-defined VRs.
- **Acquirers:** Analog Devices (now active), Infineon, Renesas, TI, Monolithic Power, onsemi, Navitas, Power Integrations, Microchip. **Exit:** strategic M&A.
- **Winning startup:** integrated power delivery IP/devices with efficiency leadership near the load and a design-in with a GPU/XPU vendor. **Non-investable:** commodity discretes vs. Infineon/onsemi scale; SiC substrate capex plays (see Wolfspeed).

## 2. Market Context
- **Structure:** Power incumbents (Infineon, onsemi, STMicro, TI, ADI, MPS, Vicor, Navitas, Power Integrations, Renesas) + startups in integration, IVR, and GaN.
- **2025–26 events:** NVIDIA 800V HVDC ecosystem formed (Navitas May 2025 [CONFIRMED]; Power Integrations joined Oct 2025 per Reuters [CONFIRMED]; Infineon–NVIDIA GaN power conversion for 800VDC racks, Oct 2026 [TO VERIFY]; Vertiv 800V HVDC products slated 2H 2026 [TO VERIFY]). Navitas showed an 800V→6V DC-DC board at GTC (Mar 2026) eliminating the 50V intermediate stage (company claim ~96.5% peak efficiency) [CONFIRMED per company PR] and reportedly a joint reference design with Microchip (Oct 2026) [UNCONFIRMED]. **ADI agreed to acquire Empower for $1.5B cash (May 2026) [CONFIRMED]; closing reported ~July 7, 2026 [TO VERIFY].** Wolfspeed filed a prepackaged Chapter 11 (June 30, 2025) and emerged Sept 29, 2025 with ~70% less debt (per SEC filings) [CONFIRMED]. Vicor guided ~20%+ growth in 2026 on VPD and licensing (Q1 2026 revenue $113M, +20% YoY) [TO VERIFY — earnings transcript].
- **Segments:** AI server VRM/PoL, in-package IVR, rack power shelves, 48V/800V conversion, DC protection, EV (adjacent).
- **Drivers:** Rack density, PUE/efficiency, copper/thermal limits, grid constraints, 1MW rack roadmaps.
- **Bottlenecks:** Device efficiency at high current, packaging/thermal, reliability, qualification with GPU vendors.
- **Competitive:** Navitas/EPC/Infineon/Power Integrations (GaN), Vicor (modules/VPD), Infineon (broad), MPS (VRMs), ADI+Empower (IVR); startups in IVR chiplets, vertical GaN, software-defined VRs.
- **Risks:** Incumbent scale, qualification cycles, capital intensity, NVIDIA architecture choices concentrating winners.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| PowerLattice | US | ~2023 [TO VERIFY] | Growth | ~$86M sold of $111M offering (SEC Form D, Oct 30, 2026) [CONFIRMED per SEC filing, via GeekWire] | Playground Global, Celesta [TO VERIFY] | Power-delivery chiplet (monolithic IVR: controller + FETs + inductors) | In-package PoL for AI XPUs | IVR chiplet integrated in processor package | Monolithic IVR chiplet demo (company claim) | High | Active |
| C2i Semiconductors | IN/US | ~2024 [TO VERIFY] | Series A | ~$16.7M Series A (May 2026) [CONFIRMED per TDK Ventures] | TDK Ventures, Peak XV Partners | Software-defined voltage regulators / VRM control | GPU VRMs, AI DC | Digital/software-defined VR control architecture | First-gen tape-out May 2026 (company claim) | Medium-High | Active |
| Vertical Semiconductor | US | ~2024 [TO VERIFY] | Seed | ~$11M (Oct 2025) [TO VERIFY] | [TO VERIFY] | Vertical GaN transistors (>1,200V) | 800V DC-DC in AI DCs | True vertical GaN for HV at GaN cost | Early | Medium-High | Active |
| Cambridge GaN Devices (CGD) | UK | 2016 | Series C | ~$60M total [TO VERIFY]; $32M Series C (Feb 2025) [CONFIRMED per company PR] | Foresight, others [TO VERIFY] | ICeGaN power HEMTs | DC PSUs, motor drives, EV | Easy-drive GaN ICs (Cambridge Univ. spinout) | New CEO Fabio Necco (2026) [TO VERIFY] | Medium | Active |
| Ferric | US | [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | Integrated voltage regulators (Fe1766, 160A) | AI/HPC processors | Thin-film-inductor IVR, small footprint | Product launch (company claim) | Medium | Active |
| Finwave Semiconductor | US | 2012 | Bridge/B | $8.2M bridge (May 2025) + earlier ~$12M A [TO VERIFY] | Fine Structure, Engine Ventures, Safar, GlobalFoundries | 3DGaN / GaN-on-Si (FinFET GaN) | RF switches/PAs (5G/6G); power adjacency | MIT GaN FinFET lineage (Palacios) | GF partnership | Medium | Active |
| VisIC Technologies | IL | 2010 | Series B | ~$100M+ [TO VERIFY]; $26M Series B (Dec 2025) [UNCONFIRMED] | HKMC (Series B) [UNCONFIRMED] | High-voltage GaN (D3GaN) | EV traction + 800V DC power | High-voltage GaN | Auto/DC pilots | Medium | Active |
| Navitas Semiconductor | US | 2014 | Public (NVTS) | IPO 2021 | (public) | GaNFast + GeneSiC | AI DC 800V, grid, EV | GaN+SiC; NVIDIA 800V HVDC partner [CONFIRMED] | 800V→6V board (GTC 2026); refocus on high-power markets [TO VERIFY] | High | Active |
| Vicor | US | 1981 | Public (VICR) | (public) | (public) | Factorized power / VPD modules + IP licensing | AI PoL, vertical power | Vertical power delivery (2nd-gen VPD) | Q1 2026 rev $113M, +20% YoY [TO VERIFY] | Medium-High | Active |
| Wolfspeed | US | 1987 | Public (post-Ch.11) | (public) | (public) | SiC substrates/devices | EV, industrial, DC power | 200mm SiC scale | Ch.11 June 30, 2025 → emerged Sept 29, 2025 [CONFIRMED per SEC] | Low (comp) | Active |
| Empower Semiconductor | US | 2014 | Acquired | >$200M (incl. >$140M Series D, Sept 2025, Fidelity-led) [CONFIRMED per company PR] | Fidelity, CapitalG, Sutter Hill, Intel Cap | Integrated voltage regulators (FCPM / Crescendo) | AI/DC vertical power delivery | Silicon-cap IVR, vertical power | Acquired by Analog Devices, $1.5B cash (ann. May 2026; closed ~Jul 2026 [TO VERIFY]) | Archived | Acquired |
| Odyssey Semiconductor | US | 2016 | Acquired (assets) | [TO VERIFY] | [TO VERIFY] | Vertical GaN power devices | High-voltage power | True vertical GaN | Assets acquired by Power Integrations (2024) [TO VERIFY] | Archived | Acquired |
| GaN Systems | CA | 2008 | Acquired | ~$200M+ raised | BDC, Fidelity | GaN power transistors | (now Infineon) | GaN device leader | Acquired by Infineon 2023 | Archived | Acquired |

## 4. Company Profiles

### Empower Semiconductor (exited — Acquired by Analog Devices, 2026)
- **Status:** Acquired · **HQ:** San Jose, US · **Founded:** 2014 · **CEO:** Tim Phillips (to lead IVR technology at ADI)
- **Funding history:** >$140M Series D (Sept 2025) led by Fidelity with CapitalG, Walden Catalyst, Maverick Silicon, Atreides, Knollwood and an ADIA subsidiary [CONFIRMED per company PR / Electronic Design]; >$200M total external funding [TO VERIFY]; earlier investors Sutter Hill, Intel Capital.
- **Exit:** Analog Devices agreed to acquire Empower for **$1.5B in cash** (announced May 2026) [CONFIRMED per ADI announcement / DCD]; completion reported ~July 7–9, 2026 [TO VERIFY — secondary reports]. ~7× total capital raised [ESTIMATED]; the clearest 2026 proof point that AI power delivery produces venture-scale strategic exits.
- **Tech:** silicon-capacitor + integrated power-FET IVRs (FCPM, Crescendo); APEC 2026 demo of a Crescendo-based vertical architecture with 16 VRs delivering ~1,000A at 0.75V (company claim). **Data quality:** Medium-High. **Last updated:** 2026-11-04. See [../deal_tracker/20_ma_tracker.md](../deal_tracker/20_ma_tracker.md).

### PowerLattice (new)
- **Status:** Active · **HQ:** Vancouver, WA, US · **Founders:** Peng Zou, Gang Ren, Sujith Dermal [TO VERIFY]
- **Funding:** SEC Form D filed Oct 30, 2026 shows ~$86M sold of a ~$111M equity offering [CONFIRMED per SEC filing, as reported by GeekWire]; earlier Series A at stealth exit (late 2025) [TO VERIFY amount/investors].
- **One-Line:** "Power delivery chiplet" — a monolithic integrated voltage regulator (controller, power transistors and inductors on one die) dropped into the processor package for point-of-load power. **Why it matters:** the most direct post-Empower venture bet on in-package IVR. **Risk:** GPU/XPU vendor qualification; ADI/Empower and Intel FIVR-style incumbency. **VC view:** High. **Data quality:** Low-Medium. **Last updated:** 2026-11-04.

### Navitas Semiconductor (public comparable)
- **Status:** Active (NASDAQ: NVTS) · **HQ:** Torrance, US · **Founded:** 2014
- **One-Line:** GaN (GaNFast) and SiC (GeneSiC) power ICs; NVIDIA selected Navitas for its 800V HVDC architecture (May 2025) [CONFIRMED]; 800V→6V DC-DC board at GTC 2026; reported Microchip reference design (Oct 2026) [UNCONFIRMED]; strategic refocus on AI DC / high-power markets and away from mobile chargers under new leadership (late 2025) [TO VERIFY].
- **Why it's here:** the listed comp showing datacenter power is a venture-to-public path; still a small revenue base (~$83M in 2024) relative to valuation swings. **Data quality:** High (public). **Last updated:** 2026-11-04.

> Startups C2i, Vertical Semiconductor, CGD, Ferric, Finwave, VisIC at table level. Also tracked: AlpSemi (~$17M; solid-state circuit breakers for 800V DC, Navitas-backed) [UNCONFIRMED]; Endura Technologies (IVR) [TO VERIFY]. Public comps: Vicor, Wolfspeed (restructured). Archived: Empower (ADI 2026), Odyssey (assets → Power Integrations 2024 [TO VERIFY]), GaN Systems (Infineon 2023); Transphorm acquired by Renesas (2024) — see [../deal_tracker/20_ma_tracker.md](../deal_tracker/20_ma_tracker.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| In-package IVR / power chiplets | Very High | High | Medium-High | Medium (ADI+Empower now) | Real (proven exit) | High |
| Vertical power delivery | High | High | Medium-High | Medium (Vicor) | Real | High |
| Datacenter GaN (48V→PoL) | High | High | Medium-High | High | Real | Medium-High |
| 800V HVDC conversion (800V→PoL) | Very High | High | High | Medium-High (Infineon, Navitas, PI) | Real | Medium-High |
| Vertical GaN (>1.2kV) | Medium-High | Very High | High | Medium | Real (early) | Medium-High |
| Solid-state DC protection | Medium-High | Medium | Medium | Medium | Real | Medium |
| Software-defined VR control | Medium-High | Medium-High | Medium | High (MPS, Infineon) | Real | Medium |
| High-voltage SiC devices/substrates | Medium | High | Very High | High | Narrow | Low-Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Fidelity | Crossover | Empower (Series D lead) | Growth | Exited via ADI 2026 | AI power pre-exit growth |
| Sutter Hill | VC | Empower | Seed–Growth | Exited via ADI 2026 | Power-IC integration |
| Intel Capital | Strategic | Empower | Growth | Exit | Compute power delivery |
| Playground Global | VC | PowerLattice [TO VERIFY], xLight (see [13](13_foundry_packaging_and_chiplet_integration.md)) | Seed–B | 2025–26 | Hard-tech power/fab |
| TDK Ventures / Peak XV | Strategic/VC | C2i Semiconductors | A | May 2026 | Software-defined VRs |
| CapitalG / Atreides / Maverick | Growth | Empower | D | Sept 2025 | AI power crossover |
| Analog Devices | Strategic acquirer | Empower | M&A | $1.5B (2026) | IVR into ADI power stack |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| MIT/CICS power electronics | MIT | High-density power conversion | Topologies for dense conversion | Watchlist | Many | 3 | Medium |
| Virginia Tech CPES | Virginia Tech | Power electronics systems | Premier power-electronics lab; talent | Watchlist | Many | 4 | Medium |
| Tomás Palacios (MIT) | MIT | GaN devices | GaN device innovation (Finwave lineage; vertical GaN) | Confirmed (Finwave) | GaN papers | 4 | Medium |

## 8. Diligence Questions
- **Technical:** Efficiency/transient response at AI currents (>1,000A); thermal; reliability/qualification; 800V isolation/safety?
- **Market:** 48V vs. 800V architecture alignment; design-in proximity to GPU (in-package vs. board)?
- **Customer:** NVIDIA/AMD/hyperscaler XPU or ODM design wins committed?
- **Competitive:** Defensible vs. Infineon/onsemi/MPS scale and ADI+Empower?
- **Financial:** Capex for fab/packaging; gross margin; IP-licensing optionality (Vicor model)?
- **Founder:** power-IC shipping pedigree? **Exit:** which strategic acquirer and precedent multiples (ADI–Empower $1.5B; GaN Systems/Transphorm)?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 6 | 0 | 1 (GaN Systems) | Initial build; Empower profile; GaN/SiC + vertical power coverage | Company sites, public filings |
| 2026-11-04 | Full (Refresh #3) | 7 | 5 | 2 (Empower, Odyssey) | Empower Series D (>$140M, Sept 2025) then acquired by ADI for $1.5B cash (May 2026; close ~Jul 2026); added PowerLattice (~$86M Form D, Oct 2026), C2i ($16.7M A), Vertical Semi, CGD, Ferric, Finwave, Wolfspeed (Ch.11 + emergence 2025); Navitas 800V updates; Vicor 2026; 800V HVDC ecosystem (PI, Infineon, Vertiv); heatmap expanded | ADI/DCD, Electronic Design, SEC (Wolfspeed 10-Q; PowerLattice Form D via GeekWire), TDK Ventures, Navitas PRs, Reuters, Vicor earnings |
