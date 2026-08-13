---
category_id: "06"
category_name: "Optical Interconnect & Co-Packaged Optics (CPO)"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-08-13"
refresh_count: 2
total_companies: 9
active_companies: 8
archived_companies: 1
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$3.7B+ [ESTIMATED], plus a ~$3.25B+ realized exit"
top_investors: ["Neuberger Berman", "GV", "T. Rowe Price", "Fidelity", "BlackRock", "NVIDIA", "Addition", "Arm"]
key_technical_inflections: ["Copper reach/energy wall", "Co-packaged optics", "Optical I/O chiplets", "Linear-drive optics (LPO)", "Optical compute fabric", "Detachable fiber-attach for CPO manufacturability", "Multi-wavelength external laser sources", "Photonic tensor compute without HBM"]
key_open_questions: ["When does CPO cross into volume? (2026 answer: it started)", "Optical I/O vs. pluggables vs. LPO?", "Can photonics yield/packaging scale economically?", "After Marvell bought Celestial AI, who is left to buy Ayar, Lightmatter or OLIX — and at what multiple?"]
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

### 2026 Update — the thesis paid off (2026-08-13)

This was the highest-conviction hard-tech call in the initial build, and 2026 H1 validated it on all three axes: a large control exit, volume production, and a step-change in capital availability.

- **Celestial AI was acquired by Marvell — the category's first large control exit.** Announced 2025-12-02 at **~$3.25B upfront, up to ~$5.5B on revenue milestones**, closed **2026-02-02**, against roughly $594M raised. Marvell also bought **XConn** ($540M) eight days later. Every remaining private company in this category should now be priced against a real comparable.
- **Ayar Labs raised $500M and went to volume.** A **Series E of ~$500M (March 2026) at roughly $3.75B** [TO VERIFY lead — reported as Neuberger Berman], explicitly to mass-produce TeraPHY optical-engine chiplets, alongside a rack-scale 1,024-accelerator reference design with **Wiwynn** shown at OFC 2026.
- **Lightmatter shipped the manufacturability answer.** In March 2026 it added the **Passage L20** unified optical engine for NPO/OBO and, more importantly, **vClick Optics — a detachable fiber array unit for CPO packaging**, which addresses the single ugliest problem in co-packaged optics (fiber attach, rework and yield in high-volume assembly). In June 2026 Lightmatter **joined the NVIDIA NVLink Fusion ecosystem**, claiming a ~50% reduction in fiber and connector count. L200 (32 Tb/s) and L200X (64 Tb/s) are entering customer integration via GlobalFoundries, ASE and Amkor. Total funding remains ~$850M at a ~$4.4B valuation from the 2024 Series D — **no new round since**, which is itself worth noting given peers' raises.
- **The laser/source layer got funded.** **Xscape Photonics** added ~$37M (March 2026, led by Addition with IAG and NVIDIA), bringing its Series A to ~$81M at roughly double the prior valuation, and launched **FalconX**, a fully redundant eight-wavelength external laser source (ELSFP). External multi-wavelength sources are the enabling component for DWDM-based optical I/O.
- **A new, large European entrant reframed photonics as compute, not just interconnect.** **OLIX** (London, founded 2024) raised **$312M Series B at ~$3.3B in August 2026** — the largest semiconductor venture round ever raised by a European company — backed by Hummingbird, Crane, Plural, Creandum, Phoenix Court, Transition, Fundomo, **Arm**, Hudson River Trading and the UK sovereign AI venture fund, with Reed Hastings among angels and **Nick McKeown** joining the board. Its X-1 platform and DX-1 decode accelerator are **optical tensor processing units that remove HBM from the inference datapath** — a direct attack on the cost structure that makes GPUs expensive. Claims of >10,000 tokens/sec/user for ~100B-parameter models are vendor figures [TO VERIFY].
- **Oriole Networks** (UK) partnered with **Tower Semiconductor** to build PRISM/PRISM Ultra deterministic-latency photonic networking on a mature silicon-photonics platform — see [05](05_networking_and_interconnect.md).
- **Where this leaves the thesis:** CPO crossed from proof-of-concept into volume across several programs in 2026 H1. The bottleneck moved from "does it work?" to **packaging, fiber attach, laser reliability and test throughput** — which is where the remaining startup opportunity and the remaining risk both sit. The acquirer set has shortened by one (Marvell has bought), so remaining exits concentrate on Broadcom, NVIDIA, Cisco, Coherent/Lumentum, or an IPO.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Lightmatter | US | 2017 | Series D (2024; no new round) | ~$850M [TO VERIFY] | GV, T. Rowe, Fidelity | Passage L200/L200X/L20 + vClick fiber attach | AI scale-up fabric | 3D photonic interposer; detachable fiber array | ~$4.4B val; **joined NVLink Fusion (2026-06)**; GF/ASE/Amkor integration | High | Active |
| Celestial AI | US | 2020 | **Acquired (Marvell), closed 2026-02-02** | ~$594M raised | Fidelity, BlackRock, Maverick, Tiger | Photonic Fabric optical interconnect | XPU↔memory/optical fabric | Optical interconnect for memory disagg. | **~$3.25B upfront, up to ~$5.5B with milestones** | Archived | Acquired |
| Ayar Labs | US | 2015 | **Series E (2026-03)** | ~$870M [TO VERIFY] | Neuberger Berman [TO VERIFY], Advent, Light Street, NVIDIA, Intel Cap | TeraPHY optical I/O chiplet + SuperNova laser | In-package optical I/O | UCIe-optical chiplet, standards push | **~$500M raise at ~$3.75B; volume production; Wiwynn 1,024-accelerator design at OFC 2026** | High | Active |
| Xscape Photonics | US | 2022 | **Series A ext. (2026-03)** | ~$81M [TO VERIFY] | Addition, IAG, NVIDIA, Cisco | FalconX 8-wavelength ELSFP; ChromX DWDM | GPU-to-GPU/memory | Multi-wavelength external laser sources | ~$37M ext. at ~2x prior valuation | High | Active |
| OLIX | UK | 2024 | **Series B (2026-08)** | ~$350M+ [TO VERIFY] | Hummingbird, Plural, Creandum, Arm, HRT, UK sovereign AI fund | X-1 platform / DX-1 optical TPU | Frontier LLM decode inference | Photonic tensor compute; no HBM in the datapath | **~$3.3B valuation — largest European semi VC round** | High (high-variance) | Active |
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
- **2026 product and ecosystem moves:** **Passage L20** unified optical engine for NPO/OBO and **vClick Optics**, a detachable fiber array unit for CPO packaging (March 2026) — the fiber-attach problem is the real barrier to CPO volume, and a detachable, reworkable interface is a genuine manufacturing advance. **Joined the NVIDIA NVLink Fusion ecosystem in June 2026**, claiming ~50% fewer fibers and connectors. L200 (32 Tb/s) and L200X (64 Tb/s) are entering customer chip integration through GlobalFoundries, ASE and Amkor.
- **2026 financing note:** no disclosed round since the 2024 Series D, while Ayar raised ~$500M and OLIX raised $312M. Either the company is well-capitalized at ~$850M raised, or it is due — worth establishing which before the next refresh.
- **VC view:** High; acquirers = NVIDIA/Broadcom/Cisco or IPO — **note Marvell has now spent its optical budget on Celestial**. **Data quality:** Medium. **Verify next:** cash position/next round, L200 design wins, NVLink Fusion revenue path. **Last updated:** 2026-08-13.

### Ayar Labs
- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2015 · **Founders:** Chen Sun, Mark Wade, Alex Wright-Gladstein, Roy Meade (MIT/Berkeley/CU Boulder)
- **Stage:** Series E · **Total Funding:** **~$870M** [TO VERIFY] · **Last Round:** **~$500M Series E, March 2026, at roughly $3.75B** — reported lead Neuberger Berman [TO VERIFY] · **Investors:** Advent, Light Street, NVIDIA, Intel Capital, GlobalFoundries, HPE, Lockheed · **Website:** ayarlabs.com
- **Primary:** 06 · **Secondary:** 04/13 · **One-Line:** TeraPHY in-package optical I/O chiplet + SuperNova multi-wavelength laser, standardizing optical die-to-die (UCIe-optical).
- **Tech:** CMOS-compatible optical I/O chiplet co-packaged with XPUs; pushing open optical-chiplet standards. **Differentiation:** standards leadership + strategic investor breadth (NVIDIA, Intel, GF, HPE). **Risk:** timing to volume, host design-win dependence.
- **2026:** the Series E is explicitly a **mass-production** round for TeraPHY optical engines; at OFC 2026 Ayar and **Wiwynn** showed a rack-scale reference design connecting 1,024 accelerators. The company has moved from standards advocacy to supply-chain execution — which shifts the diligence questions to yield, test throughput, laser reliability and per-port cost.
- **VC view:** High; deep strategic backing, and now the best-funded independent optical-I/O company. **Data quality:** Medium. **Verify next:** Series E lead and exact valuation, production yields, named host design wins. **Last updated:** 2026-08-13.

### Celestial AI — ARCHIVED (acquired by Marvell, closed 2026-02-02)
- **Status:** **Archived — acquired by Marvell Technology** · **HQ:** Santa Clara, US · **Founded:** 2020 · **Founder:** Dave Lazovsky
- **Deal:** announced 2025-12-02 at **~$3.25B in cash and stock, rising to as much as ~$5.5B if revenue milestones are met**; closed 2026-02-02. Total raised before the exit was roughly **$594M** (including a ~$250M Series C1 in March 2025), with about 137 employees as of late 2025 [TO VERIFY].
- **Investors:** Fidelity, BlackRock, Maverick, Tiger, Temasek, Porsche, AMD Ventures · **Website:** celestial.ai
- **Primary:** 06 · **Secondary:** 07 Memory · **One-Line:** "Photonic Fabric" optical interconnect for XPU-to-XPU and XPU-to-memory disaggregation, directly targeting the memory-bandwidth wall.
- **Why it exited when it did:** Marvell needed scale-up connectivity to compete with NVIDIA's NVLink and Broadcom's ecosystem, and buying the photonic fabric was faster than building it. Note the structure — roughly 40% of the maximum headline value sits in milestones. **Use this as the base comparable for the category, at the $3.25B figure rather than the $5.5B one.** **Data quality:** High (public acquirer disclosures). **Last updated:** 2026-08-13.

> Avicena, Lightelligence, Nubis, Quintessent and OLIX are covered at table level; OLIX is also cross-referenced in [02](02_inference_accelerators.md) because it competes on $/token, not only on interconnect.

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
| 2026-08-13 | Full refresh | 1 (OLIX) | 4 (Lightmatter, Ayar, Xscape, market context) | 1 (Celestial AI → Marvell) | The thesis paid off: Celestial AI acquired by Marvell (~$3.25B, up to ~$5.5B) and archived as the category's base comparable; Ayar raised ~$500M Series E at ~$3.75B for volume production; Lightmatter shipped vClick detachable fiber attach and joined NVLink Fusion; Xscape extended its Series A to ~$81M with FalconX; OLIX added at ~$3.3B as photonic compute. Bottleneck reframed from feasibility to packaging/fiber-attach/test | Company releases, acquirer disclosures, trade press |
