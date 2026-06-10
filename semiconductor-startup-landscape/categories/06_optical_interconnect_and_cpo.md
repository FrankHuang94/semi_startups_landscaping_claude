---
category_id: "06"
category_name: "Optical Interconnect & Co-Packaged Optics (CPO)"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-06-09"
refresh_count: 1
total_companies: 8
active_companies: 8
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$2.5B+ [ESTIMATED]"
top_investors: ["GV", "Fidelity", "BlackRock", "Maverick", "NVIDIA"]
key_technical_inflections: ["Copper reach/energy wall", "Co-packaged optics", "Optical I/O chiplets", "Linear-drive optics (LPO)", "Optical compute fabric"]
key_open_questions: ["When does CPO cross into volume?", "Optical I/O vs. pluggables vs. LPO?", "Can photonics yield/packaging scale economically?"]
---

# 06 — Optical Interconnect & Co-Packaged Optics

> One of the highest-quality hard-tech theses: copper is hitting reach/energy limits at scale-up, and optical I/O/CPO is a genuine inflection with strong strategic pull. Capital-intensive, timeline risk. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis
- **Why now:** Scale-up bandwidth (GPU-to-GPU/memory) is outrunning copper's reach and energy budget; CPO and optical I/O move optics into the package. NVIDIA/Broadcom and hyperscalers are pulling hard.
- **Venture-scale:** High for optical I/O chiplets, optical compute-interconnect fabric, and wavelength-scaled links. Capital-intensive but defensible.
- **Inflections:** CPO at switch and XPU, optical I/O chiplets (UCIe-optical), linear-drive/LPO, DWDM scaling, optical circuit switching.
- **Acquirers:** NVIDIA, Broadcom, Marvell, Cisco, Intel, Coherent/Lumentum. **Exit:** strategic M&A or IPO.
- **Winning startup:** optical I/O with a host-silicon design win + packaging/supply path. **Non-investable:** sub-scale photonics with no design win or packaging answer.

## 2. Market Context
- **Structure:** Transceiver incumbents (Coherent, Lumentum, InnoLight), switch (Broadcom, NVIDIA), foundries (GlobalFoundries/Tower silicon photonics, TSMC COUPE), startups below.
- **Segments:** AI scale-up fabric, switch-to-switch, XPU-to-memory, DC interconnect.
- **Drivers:** Bandwidth density, pJ/bit energy, reach, GPU utilization.
- **Bottlenecks:** Laser integration/reliability, packaging/coupling, thermal, yield, test, supply.
- **Competitive:** Pluggable optics vs. CPO vs. LPO vs. optical I/O — architecture still contested.
- **Risks:** Timeline slippage, packaging/supply, reliability, incumbent in-house CPO (NVIDIA/Broadcom).

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Lightmatter | US | 2017 | Series D | ~$850M+ [TO VERIFY] | GV, T. Rowe, Fidelity | Passage optical interconnect + photonic compute | AI scale-up fabric | 3D photonic interposer (Passage) | High-profile; ~$4B+ val [TO VERIFY] | High | Active |
| Celestial AI | US | 2020 | Series C | ~$515M+ [TO VERIFY] | Fidelity, BlackRock, Maverick, Tiger | Photonic Fabric optical interconnect | XPU↔memory/optical fabric | Optical interconnect for memory disagg. | Strategic interest | High | Active |
| Ayar Labs | US | 2015 | Series D | ~$370M+ [TO VERIFY] | Advent, Light Street, NVIDIA, Intel Cap | TeraPHY optical I/O chiplet + SuperNova laser | In-package optical I/O | UCIe-optical chiplet, standards push | Multiple foundry/partners | High | Active |
| Xscape Photonics | US | 2022 | Series A | ~$57M+ [TO VERIFY] | IAG, Karman, NVIDIA, Cisco | Multi-wavelength programmable optics | GPU-to-GPU/memory | DWDM "ChromX" scaling | Early; NVIDIA-backed | High | Active |
| Avicena | US | 2019 | Series A/B | [TO VERIFY] | Cerberus, Clear Ventures | microLED-based LightBundle links | Short-reach chip-to-chip | microLED interconnect (low power) | Demos | Medium-High | Active |
| Lightelligence | US/CN | 2017 | Series B+ | ~$200M+ [TO VERIFY] | [TO VERIFY] | Photonic compute + oNOC | Optical compute/interconnect | Optical network-on-chip | Demos | Medium | Active |
| Nubis Communications | US | 2020 | Series B | ~$120M+ [TO VERIFY] | Matrix, MJ Capital | Linear pluggable/CPO optical engines | Linear optics for AI | High-density linear optics | Sampling | Medium-High | Active |
| Quintessent | US | 2022 | Seed/A | [TO VERIFY] | [TO VERIFY] | Quantum-dot laser photonics | Integrated lasers/DWDM | QD comb lasers on silicon | Early | Medium | Active |

## 4. Company Profiles

### Lightmatter
- **Status:** Active · **HQ:** Mountain View, US · **Founded:** 2017 · **Founders:** Nicholas Harris (MIT), Darius Bunandar, Thomas Graham
- **Stage:** Series D · **Total Funding:** ~$850M+ [TO VERIFY] · **Last Round:** ~$400M Series D, 2024, led by T. Rowe Price; valuation ~$4.4B [TO VERIFY] · **Investors:** GV, Fidelity, Viking, G15, SIP Global · **Website:** lightmatter.co
- **Primary:** 06 · **Secondary:** 14 (photonic compute) · **One-Line:** Photonic interconnect (Passage) and photonic computing, pivoting emphasis to optical interconnect as the near-term wedge.
- **Tech:** Passage 3D photonic interposer for wafer-scale optical interconnect between many chiplets; earlier Envise photonic compute; Idiom software. **Differentiation:** in-package optical interconnect at very high bandwidth density. **Risk:** packaging/yield, time-to-volume, incumbent CPO.
- **VC view:** High; acquirers = NVIDIA/Broadcom/Intel or IPO. **Data quality:** Medium. **Last updated:** 2026-06-09.

### Ayar Labs
- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2015 · **Founders:** Chen Sun, Mark Wade, Alex Wright-Gladstein, Roy Meade (MIT/Berkeley/CU Boulder)
- **Stage:** Series D · **Total Funding:** ~$370M+ [TO VERIFY] · **Investors:** Advent, Light Street, NVIDIA, Intel Capital, GlobalFoundries, HPE, Lockheed · **Website:** ayarlabs.com
- **Primary:** 06 · **Secondary:** 04/13 · **One-Line:** TeraPHY in-package optical I/O chiplet + SuperNova multi-wavelength laser, standardizing optical die-to-die (UCIe-optical).
- **Tech:** CMOS-compatible optical I/O chiplet co-packaged with XPUs; pushing open optical-chiplet standards. **Differentiation:** standards leadership + strategic investor breadth (NVIDIA, Intel, GF, HPE). **Risk:** timing to volume, host design-win dependence.
- **VC view:** High; deep strategic backing. **Data quality:** Medium. **Last updated:** 2026-06-09.

### Celestial AI
- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2020 · **Founder:** Dave Lazovsky
- **Stage:** Series C · **Total Funding:** ~$515M+ [TO VERIFY] · **Last Round:** ~$250M Series C, 2025, led by Fidelity/others [TO VERIFY] · **Investors:** Fidelity, BlackRock, Maverick, Tiger, Temasek, Porsche · **Website:** celestial.ai
- **Primary:** 06 · **Secondary:** 07 Memory · **One-Line:** "Photonic Fabric" optical interconnect for XPU-to-XPU and XPU-to-memory disaggregation, directly targeting the memory-bandwidth wall.
- **Tech:** optical fabric enabling memory pooling/expansion over photonics. **Differentiation:** memory-centric optical fabric. **Risk:** packaging, ecosystem adoption. **VC view:** High. **Data quality:** Medium. **Last updated:** 2026-06-09.

> Xscape, Avicena, Lightelligence, Nubis, Quintessent at table level.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Optical I/O chiplets | High | Very High | High | Medium | Real | High |
| Optical interconnect fabric | High | Very High | High | Medium | Real | High |
| CPO for switches | High | High | High | High (Broadcom/NVDA) | Narrow | Medium |
| Linear/LPO optics | High | High | Medium | High | Real | Medium-High |
| Integrated lasers / DWDM | High | Very High | High | Medium | Real | Medium-High |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| GV | VC | Lightmatter | Early–Growth | Lightmatter | Photonics conviction |
| Fidelity/BlackRock | Crossover | Celestial, Lightmatter | Growth | Mega-rounds | Pre-IPO photonics |
| NVIDIA (NVentures) | Strategic | Xscape, Ayar | A–D | Multi-deal | Optical fabric ecosystem |
| Maverick | VC | Celestial | Growth | Celestial | Silicon/photonics |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Keren Bergman | Columbia (Lightwave Research Lab) | Silicon photonics, optical fabric | Leading academic photonic-fabric group; talent source | Likely Startup Signal | Many; Xscape adjacency | 5 | High |
| Vladimir Stojanović | UC Berkeley | Monolithic photonics | Ayar Labs lineage | Confirmed (Ayar) | Monolithic photonics | 5 | High |
| Rajeev Ram / MIT photonics | MIT | Integrated photonics | Photonics founder pipeline | Watchlist | Many | 4 | Medium |
| John Bowers | UCSB | Heterogeneous lasers on Si | Laser integration is the bottleneck | Likely | QD/heterogeneous lasers | 5 | High |

## 8. Diligence Questions
- **Technical:** pJ/bit, bandwidth density, laser reliability/temperature, coupling loss, yield/test cost?
- **Market:** Pluggable vs. CPO vs. LPO vs. optical-I/O positioning; standards (UCIe-O)?
- **Customer:** Host-silicon design win (which XPU/switch)? Foundry/packaging partner?
- **Competitive:** Survives NVIDIA/Broadcom in-house CPO?
- **Financial:** Capital to volume; packaging/supply secured?
- **Founder:** Photonics + packaging shipping pedigree?
- **Exit:** Strategic acquirer fit; transceiver-incumbent roll-up logic?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | 0 | Initial build; Lightmatter/Ayar/Celestial profiles; CPO/optical-I/O coverage | Company sites, trade press |
