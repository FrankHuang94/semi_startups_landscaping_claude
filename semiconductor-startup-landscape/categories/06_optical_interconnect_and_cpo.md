---
category_id: "06"
category_name: "Optical Interconnect & Co-Packaged Optics (CPO)"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 16
active_companies: 13
archived_companies: 3
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$4.4B+ incl. archived; ~$3.7B+ active [ESTIMATED]"
top_investors: ["Neuberger Berman", "Atreides", "NVIDIA", "Sutter Hill", "Bullhound Capital", "Fidelity", "GV", "AMD Ventures", "Intel Capital"]
key_technical_inflections: ["Copper reach/energy wall at scale-up", "Co-packaged optics shipping (Broadcom TH6-Davisson, NVIDIA Quantum-X/Spectrum-X Photonics)", "Optical I/O chiplets", "Linear-drive optics (LPO) as CPO competitor", "Optical circuit switching (OCS)", "Multi-wavelength lasers / DWDM"]
key_open_questions: ["When does CPO cross into volume at the XPU (not just switch)?", "Optical I/O vs. pluggables vs. LPO vs. NPO?", "Can photonics yield/packaging/laser supply scale economically?", "Are $3.75B–$5.5B photonics valuations supported by revenue?"]
---

# 06 — Optical Interconnect & Co-Packaged Optics

> One of the highest-quality hard-tech theses: copper is hitting reach/energy limits at scale-up, and optical I/O/CPO is a genuine inflection with strong strategic pull. 2025–26 delivered the first big exits (Marvell–Celestial AI, Ciena–Nubis) and the largest photonics rounds on record (Ayar Labs, Lumilens). Capital-intensive, timeline risk. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis
- **Why now:** Scale-up bandwidth (GPU-to-GPU/memory) is outrunning copper's reach and energy budget; CPO and optical I/O move optics into the package. Broadcom began shipping a 102.4 Tb/s CPO switch (Tomahawk 6–Davisson) in Oct 2025 [CONFIRMED — Broadcom PR] and NVIDIA's Quantum-X/Spectrum-X Photonics CPO switches were slated for 2025–2026 [CONFIRMED — NVIDIA GTC 2025 announcement; 2026 volume shipment status TO VERIFY].
- **Venture-scale:** High for optical I/O chiplets, optical scale-up fabric, optical circuit switching, and wavelength-scaled lasers/links. Capital-intensive but defensible; growth investors now writing $100M–$700M checks.
- **Inflections:** CPO at switch and XPU, optical I/O chiplets (UCIe-optical), NPO, linear-drive/LPO, DWDM scaling, optical circuit switching (OCS).
- **Exit evidence (new):** Marvell acquired **Celestial AI** — $3.25B upfront ($1B cash + 27.2M shares) plus earn-out to up to $5.5B total, announced Dec 2 2025, closed Feb 2 2026 [CONFIRMED — Marvell PR]. Ciena agreed to buy **Nubis** for $270M cash (Sept 2025) [CONFIRMED]. Molex agreed to buy **Teramount** (Apr 2026) [TO VERIFY].
- **Acquirers:** NVIDIA, Broadcom, Marvell, Cisco, Ciena, Intel, AMD, Coherent/Lumentum, Molex, Corning. **Exit:** strategic M&A (proven) or IPO (Ayar/Lightmatter/Lumilens scale).
- **Winning startup:** optical I/O or fabric with a host-silicon design win + packaging/laser supply path. **Non-investable:** sub-scale photonics with no design win or packaging answer.

## 2. Market Context
- **Structure:** Transceiver incumbents (Coherent, Lumentum, InnoLight, Eoptolink), switch (Broadcom, NVIDIA, Marvell), foundries (GlobalFoundries/Tower silicon photonics, TSMC COUPE), connector/fiber (Corning, Molex), startups below.
- **2026 state of play:** Broadcom TH6–Davisson CPO shipping; Meta reported 1M cumulative 400G CPO port-device hours with zero link flaps on earlier Broadcom CPO (vendor-reported) [CONFIRMED as vendor claim]. NVIDIA photonics switches built on TSMC COUPE with MRM modulators. LPO remains a live competitor — Arista's Tomahawk 6 7060XE7 (LPO) slated for Q4 2026 [TO VERIFY]. Marvell now owns Celestial's Photonic Fabric (targets $500M annualized revenue run-rate by Q4 FY2028; $1B by Q4 FY2029 — company projections).
- **Segments:** AI scale-up fabric, switch-to-switch, XPU-to-memory, optical circuit switching, DC interconnect.
- **Drivers:** Bandwidth density, pJ/bit energy, reach, GPU utilization, power-limited data centers.
- **Bottlenecks:** Laser integration/reliability, fiber-to-chip coupling, thermal, yield, test, supply.
- **Competitive:** Pluggable vs. LPO vs. NPO vs. CPO vs. optical I/O — architecture still contested; incumbents (NVIDIA/Broadcom/Marvell) now own in-house CPO.
- **Risks:** Timeline slippage, packaging/supply, reliability, incumbent in-house CPO, valuation compression if XPU-level CPO slips to 2028+.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Ayar Labs | US | 2015 | Series E (+ext.) | ~$1.0B+ [TO VERIFY]; $500M Series E Mar 2026 + $150M ext. Sept 2026 [CONFIRMED] | Neuberger Berman (E lead), QIA, NVIDIA, AMD, Intel Cap, MediaTek, Wiwynn | TeraPHY optical I/O chiplet + SuperNova laser | In-package optical I/O / CPO | UCIe-optical chiplet, standards push | Val. ~$3.75B (Mar 2026) [TO VERIFY]; $5B+ (Sept) [UNCONFIRMED] | High | Active |
| Lumilens | US [TO VERIFY] | 2024 | Series C | ~$900M+ [TO VERIFY]; $700M+ Series C Aug 2026 at $5.51B [CONFIRMED] | Atreides, Bain Capital Ventures, Meritech, Seligman, Spark (co-leads); Peak XV, EDBI | NPO/CPO + pluggable optical transceivers | AI DC optics at volume | Vertically integrated silicon→systems→HVM | Emerged from stealth Aug 2026 | High | Active |
| Lightmatter | US | 2017 | Series D | ~$850M [CONFIRMED-ish, multiple sources] | T. Rowe Price (D lead), GV, Fidelity | Passage M1000/L200 photonic interconnect | AI scale-up fabric | 3D photonic interposer (Passage) | $4.4B val. (Oct 2024) [CONFIRMED]; 2026 Series E claim [UNCONFIRMED] | High | Active |
| Salience Labs | UK | 2021 | Series B | ~$165M+ [ESTIMATED]; $125M Series B Oct 2026 [CONFIRMED] | Bullhound Capital (B lead), AMD Ventures, Intel Capital, SBI, HRT, British Business Bank | Photonic switching chips (SOA-based [TO VERIFY]) | AI DC scale-up/scale-out switching | Fast photonic packet/circuit switching | Oxford/Münster spinout | High | Active |
| nEye | US | 2021 [TO VERIFY] | Series C | ~$152M [CONFIRMED, company] | Sutter Hill (C lead), CapitalG | Wafer-scale MEMS optical circuit switch | AI cluster OCS | Chip-scale OCS vs. bulky mirror OCS | $80M Series C Apr 2026 [CONFIRMED] | High | Active |
| Xscape Photonics | US | 2022 | Series A (ext.) | ~$95M [TO VERIFY] (Series A total $81M) | Addition (ext. lead), IAG, NVIDIA, Cisco | ChromX multi-wavelength optics; FalconX 8-λ laser | GPU-to-GPU/memory | DWDM comb-laser scaling | $37M extension Mar 2026 [CONFIRMED] | High | Active |
| Avicena | US | 2019 | Series B | ~$120M [CONFIRMED-ish] | Tiger Global (B lead), SK hynix, Cerberus | microLED LightBundle links | Short-reach chip-to-chip, memory | microLED interconnect (low power) | $65M Series B May 2025; eval platform Mar 2026 | Medium-High | Active |
| OpenLight | US | 2022 | Series A-1 | ~$84M [CONFIRMED] | Xora Innovation, Capricorn (A co-leads) | Open PDK silicon photonics w/ integrated lasers (InP-on-Si) | PIC designers / transceivers | Heterogeneous laser integration platform | $50M A-1 Apr 2026 [CONFIRMED] | Medium-High | Active |
| Lightelligence | US/CN | 2017 | Series B+ | ~$200M+ [TO VERIFY] | [TO VERIFY] | Photonic compute + oNOC | Optical compute/interconnect | Optical network-on-chip | No 2026 update verified | Medium | Active |
| Scintil Photonics | FR | 2018 | Series B | ~$70M+ [TO VERIFY] ($58M Series B Sept 2025 [TO VERIFY]) | [TO VERIFY] | III-V-on-Si integrated DWDM laser sources | CPO laser supply | Heterogeneous lasers on SOI | Early CPO design-ins [TO VERIFY] | Medium-High | Active |
| Oriole Networks | UK | 2023 | Series A | ~$35M [CONFIRMED-ish] | Plural (A lead), UCL Tech Fund, XTX | PRISM all-optical network fabric | AI training clusters | Fast optical switching fabric | No 2026 round found | Medium | Active |
| iPronics | ES | 2019 | Series A [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | Programmable photonic processor / OCS [TO VERIFY] | DC optical switching | Software-defined photonic mesh | No 2026 data verified | Medium | Active |
| Quintessent | US | 2022 | Seed/A | [TO VERIFY] | [TO VERIFY] | Quantum-dot laser photonics | Integrated lasers/DWDM | QD comb lasers on silicon | No 2026 update verified | Medium | Active |
| Celestial AI | US | 2020 | Acquired | ~$515M+ raised [TO VERIFY] | Fidelity, BlackRock, Maverick, Tiger | Photonic Fabric optical interconnect | (now Marvell) | Optical memory/XPU fabric | Marvell $3.25B upfront + up to $5.5B; closed Feb 2 2026 [CONFIRMED] | Archived | Acquired (Marvell) |
| Nubis Communications | US | 2020 | Acquired | ~$120M+ raised [TO VERIFY] | Matrix, MJ Capital | Linear/CPO/NPO optical engines; ACC analog | (now Ciena) | 6.4T optical engines + 200G/lane ACC | Ciena $270M cash, announced Sept 22 2025 [CONFIRMED]; close expected late 2025 [TO VERIFY] | Archived | Acquired (Ciena) |
| Teramount | IL | 2013 | Acquired [TO VERIFY] | ~$58M raised | AMD, Samsung, Hitachi ($50M, Jul 2025) | Detachable fiber-to-chip (PhotonicPlug) | CPO fiber attach | Self-aligning fiber coupling | Molex agreement to acquire, Apr 2026 [TO VERIFY] | Archived | Acquired (Molex) [TO VERIFY] |

## 4. Company Profiles

### Ayar Labs
- **Status:** Active · **HQ:** San Jose / Santa Clara, US · **Founded:** 2015 · **Founders:** Chen Sun, Mark Wade, Alex Wright-Gladstein, Roy Meade (MIT/Berkeley/CU Boulder)
- **Stage:** Series E (+extension) · **Total Funding:** >$1B [TO VERIFY] · **2026 rounds:** $500M Series E closed Mar 3 2026, led by Neuberger Berman (QIA participated), reported ~$3.75B post-money and ~$870M cumulative [CONFIRMED round; valuation TO VERIFY]; $150M Series E extension announced Sept 10 2026, bringing 2026 primary capital to $650M; reports of $5B+ valuation [UNCONFIRMED] · **Strategic investors:** NVIDIA, AMD, Intel, MediaTek, Wiwynn, GlobalFoundries, HPE, Lockheed · **Website:** ayarlabs.com
- **Primary:** 06 · **Secondary:** 04/13 · **One-Line:** TeraPHY in-package optical I/O chiplet + SuperNova multi-wavelength laser — now moving to volume CPO production.
- **Tech:** CMOS-compatible optical I/O chiplet co-packaged with XPUs; open optical-chiplet standards. New Bengaluru design center (2026) alongside US + Hsinchu teams. **Differentiation:** broadest strategic cap table in the category (NVIDIA + AMD + Intel). **Risk:** timing to volume, host design-win dependence.
- **VC view:** High; IPO candidate. **Data quality:** Medium-High. **Last updated:** 2026-11-04.

### Lumilens (new)
- **Status:** Active · **HQ:** [TO VERIFY] · **Founded:** 2024 (per announcement, "two years" before Aug 2026)
- **Stage:** Series C · **Total Funding:** >$900M [TO VERIFY] · **Last Round:** $700M+ Series C, Aug 2026, at $5.51B valuation, co-led by Atreides Management, Bain Capital Ventures, Meritech, Seligman Ventures and Spark Capital; Peak XV and EDBI participated [CONFIRMED — announcement coverage incl. DealStreetAsia, Fibre Systems]
- **Primary:** 06 · **One-Line:** Near-package, co-packaged and pluggable optics for AI data centers, emerging from stealth with the largest photonics round of 2026.
- **Use of funds:** silicon, systems, software, process engineering and high-volume manufacturing (company-stated). **Risk:** stealth-era technical claims unverified; HVM execution vs. InnoLight/Coherent; valuation ahead of disclosed revenue.
- **VC view:** High-variance; signals growth capital treating optics as a "picks-and-shovels" mega-category. **Data quality:** Low-Medium. **Last updated:** 2026-11-04.

### Lightmatter
- **Status:** Active · **HQ:** Mountain View, US · **Founded:** 2017 · **Founders:** Nicholas Harris (MIT), Darius Bunandar, Thomas Graham
- **Stage:** Series D · **Total Funding:** ~$850M · **Last Round:** $400M Series D, Oct 2024, led by T. Rowe Price, $4.4B valuation [CONFIRMED]. A single aggregator claims a 2026 $500M Series E at $3.75B — figures identical to Ayar Labs' round, likely a conflation [UNCONFIRMED; treat as not occurred] · **Investors:** GV, Fidelity, Viking, G15, SIP Global · **Website:** lightmatter.co
- **Primary:** 06 · **Secondary:** 14 (photonic compute) · **One-Line:** Passage photonic interconnect (M1000 3D photonic superchip, 114 Tbps; L200 CPO chiplet), emphasis now fully on optical interconnect.
- **2026 signals:** GUC strategic partnership (Jan 2026) [TO VERIFY]; joined NVIDIA NVLink Fusion ecosystem (Jun 2026) [TO VERIFY]; showed 204.8 Tbps 1U optical switch with Passage engines built with Flex at OCP (Oct 2026) [TO VERIFY]; M1000 product availability targeted ~2027 [TO VERIFY].
- **Risk:** packaging/yield, time-to-volume, incumbent CPO; no new primary round since 2024 while peers raised. **VC view:** High; acquirers = NVIDIA/Broadcom/AMD or IPO. **Data quality:** Medium. **Last updated:** 2026-11-04.

### Salience Labs (new profile)
- **Status:** Active · **HQ:** Oxford, UK · **Founded:** 2021 (Oxford/Münster spinout)
- **Stage:** Series B · **Total Funding:** ~$165M+ [ESTIMATED: ~$11.5M seed + ~$30M Series A (Feb 2025) + $125M B] · **Last Round:** $125M oversubscribed Series B announced Oct 14 2026, led by Bullhound Capital; AMD Ventures, Intel Capital, SBI Group, Hudson River Trading, British Business Bank participated [CONFIRMED — DCD, Latham & Watkins]
- **Primary:** 06 · **Secondary:** 05 · **One-Line:** Photonic switching chips to remove data-movement bottlenecks in AI data centers.
- **VC view:** High; AMD + Intel strategic participation. **Risk:** OCS/photonic-switch adoption timing vs. electrical switches. **Data quality:** Medium. **Last updated:** 2026-11-04.

### Celestial AI (archived — acquired by Marvell)
- **Status:** Acquired by Marvell. Announced Dec 2 2025: $1B cash + 27.2M Marvell shares (~$2.25B) = ~$3.25B upfront; additional earn-out up to ~$5.5B total if Celestial reaches $2B cumulative revenue by end of FY2029; Amazon received a related Marvell warrant [CONFIRMED — Marvell PR / Reuters]. Closed Feb 2 2026; team joins Marvell Data Center Group [CONFIRMED — Marvell PR].
- **Pre-exit:** ~$515M+ raised [TO VERIFY] (Fidelity, BlackRock, Maverick, Tiger, Temasek, Porsche). **Why it matters:** largest photonics-startup exit to date; validates optical scale-up fabric as a strategic must-have for custom-XPU vendors. **Last updated:** 2026-11-04.

> Xscape, nEye, OpenLight, Avicena, Oriole, Scintil, iPronics, Lightelligence, Quintessent at table level. Nubis (Ciena) and Teramount (Molex [TO VERIFY]) archived. Exits are logged in [../deal_tracker/23_exit_and_shutdown_tracker.md](../deal_tracker/23_exit_and_shutdown_tracker.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Optical I/O chiplets | Very High | Very High | High | Medium (rising) | Real — late-stage, pricey | High |
| Optical scale-up fabric | Very High | Very High | High | Medium-High (Marvell owns Celestial) | Real | High |
| CPO for switches | High | High | High | Very High (Broadcom/NVDA shipping) | Narrow | Medium-Low |
| Optical circuit switching (OCS) | High | High | Medium-High | Medium (Google in-house) | Real — nEye, Salience, Oriole, iPronics | High |
| Linear/LPO/NPO optics | High | High | Medium | High | Real | Medium-High |
| Integrated lasers / DWDM / fiber attach | High | Very High | High | Medium | Real — tuck-in M&A (Teramount) | Medium-High |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Neuberger Berman | Crossover | Ayar Labs | Growth | Led $500M Series E (Mar 2026) | Pre-IPO optical I/O |
| Atreides | Crossover | Lumilens | Growth | Co-led $700M+ (Aug 2026) | AI-infra mega-rounds |
| NVIDIA (NVentures) | Strategic | Ayar, Xscape | A–E | Multi-deal 2026 | Optical fabric ecosystem |
| AMD Ventures | Strategic | Ayar, Salience, Teramount | A–E | Salience B (Oct 2026) | Counter-NVIDIA optical scale-up |
| Intel Capital | Strategic | Ayar, Salience | A–E | Salience B | Photonics ecosystem |
| Sutter Hill | VC | nEye | B–C | Led $80M Series C (Apr 2026) | OCS |
| Bullhound Capital | VC | Salience Labs | B | Led $125M (Oct 2026) | European photonics |
| GV | VC | Lightmatter | Early–Growth | Lightmatter | Photonics conviction |
| Fidelity/BlackRock | Crossover | (Celestial), Lightmatter | Growth | Celestial exit | Pre-IPO photonics |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Keren Bergman | Columbia (Lightwave Research Lab) | Silicon photonics, optical fabric | Leading academic photonic-fabric group; talent source | Confirmed (Xscape adjacency) | Many | 5 | High |
| Vladimir Stojanović | UC Berkeley | Monolithic photonics | Ayar Labs lineage | Confirmed (Ayar) | Monolithic photonics | 5 | High |
| Ming Wu | UC Berkeley | MEMS photonic switches | Wafer-scale OCS (nEye lineage) [TO VERIFY] | Confirmed (nEye) [TO VERIFY] | Silicon photonic MEMS switches | 5 | Medium |
| Harish Bhaskaran / Wolfram Pernice | Oxford / Münster | Photonic computing/switching | Salience Labs founders' lineage | Confirmed (Salience) | Many | 4 | Medium |
| Rajeev Ram / MIT photonics | MIT | Integrated photonics | Photonics founder pipeline | Watchlist | Many | 4 | Medium |
| John Bowers | UCSB | Heterogeneous lasers on Si | Laser integration is the bottleneck | Likely (Quintessent/OpenLight lineage) | QD/heterogeneous lasers | 5 | High |

## 8. Diligence Questions
- **Technical:** pJ/bit, bandwidth density, laser reliability/temperature, coupling loss, yield/test cost? Field reliability data (link flaps, FIT) comparable to Broadcom/Meta CPO data?
- **Market:** Pluggable vs. LPO vs. NPO vs. CPO vs. optical-I/O positioning; standards (UCIe-O)? Scale-up vs. scale-out vs. OCS?
- **Customer:** Host-silicon design win (which XPU/switch)? Foundry/packaging partner (TSMC COUPE, GF, Tower)?
- **Competitive:** Survives NVIDIA/Broadcom in-house CPO and Marvell-Celestial?
- **Financial:** Capital to volume; packaging/laser supply secured? Revenue multiple implied by $3.75B–$5.5B marks?
- **Founder:** Photonics + packaging shipping pedigree?
- **Exit:** Strategic acquirer fit (Marvell/Celestial and Ciena/Nubis comps); transceiver-incumbent roll-up logic?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | 0 | Initial build; Lightmatter/Ayar/Celestial profiles; CPO/optical-I/O coverage | Company sites, trade press |
| 2026-11-04 | Full (Refresh #3) | 8 | 6 | 3 | Added Lumilens ($700M+ C at $5.51B), Salience Labs ($125M B), nEye ($80M C), OpenLight ($50M A-1), Oriole, Scintil, iPronics, Teramount. Archived Celestial AI (Marvell, closed Feb 2026), Nubis (Ciena $270M), Teramount (Molex [TO VERIFY]). Updated Ayar ($500M E + $150M ext.), Xscape ($37M ext.), Lightmatter (2026 Series E claim flagged unconfirmed), Avicena, Lightelligence, Quintessent. Market context updated for Broadcom TH6-Davisson/NVIDIA photonics CPO and OCS subsegment. | Marvell PR/BusinessWire; Ciena via trade press; Ayar Labs PR (BusinessWire)/Latham; DealStreetAsia/Fibre Systems (Lumilens); Latham/DCD (Salience); BusinessWire/optics.org (nEye); SiliconANGLE (Xscape); Photonics Online (OpenLight); Broadcom IR |
