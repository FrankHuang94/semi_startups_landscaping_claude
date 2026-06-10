---
category_id: "07"
category_name: "Memory & Storage"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-06-09"
refresh_count: 1
total_companies: 6
active_companies: 6
archived_companies: 0
stealth_or_semi_stealth_companies: 1
total_disclosed_funding: "~$300M+ [ESTIMATED]"
top_investors: ["Intel Capital", "Samsung", "SK hynix", "Micron Ventures"]
key_technical_inflections: ["Memory wall (bandwidth+capacity)", "CXL pooling/expansion", "Processing-in-memory", "Near-memory compute", "HBM base-die IP"]
key_open_questions: ["Does CXL reach volume in AI DC?", "Can PIM cross the software chasm?", "Do startups capture value vs. the 3 DRAM makers?"]
---

# 07 — Memory & Storage

> Memory is *the* AI bottleneck (capacity, bandwidth, cost). DRAM is a 3-player oligopoly, so startups play in the fabric and architecture layer. Strategic-heavy exits. See [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis
- **Why now:** HBM is supply-constrained and dominates AI BOM; model size outpaces on-package memory; CXL enables disaggregation/pooling.
- **Venture-scale:** Medium-High in CXL switching/pooling, PIM IP, near-memory compute, and memory-controller IP. **Don't** try to make DRAM/NAND.
- **Inflections:** CXL 2.0/3.x pooling, PIM (HBM-PIM/LPDDR-PIM), near-memory accelerators, base-die customization.
- **Acquirers:** SK hynix, Samsung, Micron, Marvell, Astera, Microchip. **Exit:** strategic M&A.
- **Winning startup:** owns memory-fabric/controller IP or PIM IP with a memory-maker partnership. **Non-investable:** capital-intensive DRAM/NAND fab plays.

## 2. Market Context
- **Structure:** DRAM oligopoly (Samsung, SK hynix, Micron); controller/IP (Astera, Marvell, Microchip, Rambus); CXL startups; storage incumbents (Phison, Silicon Motion).
- **Segments:** AI training/inference memory, memory pooling for TCO, in-memory analytics.
- **Drivers:** HBM scarcity/cost, capacity-per-GPU, stranded-memory recovery, bandwidth.
- **Bottlenecks:** CXL latency, software/OS support, ecosystem timing, PIM programmability.
- **Competitive:** Astera (CXL controllers), Rambus (IP), Marvell; startups in switching/pooling + PIM.
- **Risks:** CXL adoption slower than hoped; memory makers internalize value.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Panmnesia | KR | 2022 | Seed/A | ~$28M+ [TO VERIFY] | Daekyo, SL Investment | CXL 3.x switch/IP & memory pooling | AI DC memory disagg. | Low-latency CXL fabric IP (KAIST spinout) | CES awards; pilots | High | Active |
| UnifabriX | IL | 2020 | Seed/A | [TO VERIFY] | [TO VERIFY] | Smart Memory Node (CXL) | Memory pooling/HPC | CXL memory appliance, bandwidth boost | Demos | Medium-High | Active |
| MemVerge | US | 2017 | Series B | ~$60M+ [TO VERIFY] | Intel Cap, Cisco, NEA | Memory Machine (software) | CXL memory orchestration | Software tiering for CXL/DRAM | Enterprise pilots | Medium | Active |
| Numem | US | 2018 | Seed/A | [TO VERIFY] | [TO VERIFY] | MRAM-based smart memory | AI memory subsystems | NVRAM/MRAM for AI | Early | Medium | Semi-Stealth |
| Neo Semiconductor | US | 2012 | Seed/A | [TO VERIFY] | [TO VERIFY] | 3D X-DRAM / 3D NAND IP | DRAM/NAND scaling IP | Novel 3D DRAM cell IP | IP/demos | Medium | Active |
| Astera Labs (Leo) | US | 2017 | Public | (see [05](05_networking_and_interconnect.md)) | Sutter Hill | CXL memory controllers | AI DC memory expansion | Production CXL controller | Hyperscaler revenue | High | Active |

## 4. Company Profiles

### Panmnesia
- **Status:** Active · **HQ:** Daejeon, KR · **Founded:** 2022 · **Origin:** KAIST spinout (Myoungsoo Jung)
- **Stage:** Seed/A · **Total Funding:** ~$28M+ [TO VERIFY] · **Investors:** Daekyo Investment, SL Investment, others · **Website:** panmnesia.com
- **Primary:** 07 · **Secondary:** 05 Fabric · **One-Line:** Ultra-low-latency CXL 3.x switch and IP enabling large-scale memory (and GPU) pooling/expansion for AI datacenters.
- **Tech:** sub-100ns CXL fabric IP, full-stack CXL switch SoC, memory/accelerator pooling; CES Innovation recognition. **Differentiation:** latency leadership + academic-grade CXL depth. **Risk:** CXL adoption timing, scaling GTM.
- **VC view:** High; acquirers = memory makers, Astera, Marvell. **Data quality:** Medium. **Last updated:** 2026-06-09.

### UnifabriX
- **Status:** Active · **HQ:** Yokneam, IL · **Founded:** 2020 · **Founders:** Ronen Hyatt, Danny Volkind
- **Stage:** Seed/A · **Funding:** [TO VERIFY] · **Website:** unifabrix.com
- **Primary:** 07 · **One-Line:** "Smart Memory Node" CXL appliance for memory pooling and bandwidth expansion in HPC/AI servers.
- **Tech:** CXL-based memory appliance recovering stranded memory and boosting effective bandwidth; demonstrated MLPerf-style gains [TO VERIFY]. **VC view:** Medium-High. **Data quality:** Low-Medium. **Last updated:** 2026-06-09.

> MemVerge (software), Numem, Neo Semiconductor at table level; Astera Leo cross-referenced from [05](05_networking_and_interconnect.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| CXL switching/pooling | High | High | Medium | Medium | Real | High |
| CXL memory controllers | High | High | Medium | High (Astera) | Narrow | Medium |
| Processing-in-memory IP | High | Very High | Medium-High | High (DRAM cos) | High-variance | Medium-High |
| Near-memory accelerators | Medium-High | High | Medium-High | Medium | Real | Medium |
| Novel DRAM/NAND IP | Medium | Very High | High | High | Niche (IP) | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Intel Capital | Strategic | MemVerge | Seed–B | CXL ecosystem | Memory disaggregation |
| Samsung / SK hynix / Micron | Strategic | (PIM/CXL R&D, Eliyan) | Various | Strategic | Memory-maker pull |
| Korean VCs (Daekyo, SL) | VC | Panmnesia | Seed–A | Panmnesia | CXL early bets |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Onur Mutlu | ETH Zürich | PIM / near-memory | Leading PIM research; commercial urgency | Likely Startup Signal | RowHammer, PIM survey | 5 | High |
| Myoungsoo Jung | KAIST | CXL systems | Panmnesia origin | Confirmed (Panmnesia) | CXL papers | 5 | High |
| Samsung/SK hynix research | Corporate | HBM-PIM, CXL | Defines productizable PIM | Watchlist | HBM-PIM papers | 4 | High |

## 8. Diligence Questions
- **Technical:** CXL latency/bandwidth measured; OS/hypervisor support; PIM programmability/software?
- **Market:** Pooling TCO case quantified; which workloads pull first?
- **Customer:** Memory-maker or hyperscaler partnership signed?
- **Competitive:** Defensible vs. Astera/Marvell/Rambus and DRAM-maker internalization?
- **Financial:** IP-royalty vs. hardware margins; capital to product?
- **Founder:** memory/controller silicon pedigree? **Exit:** strategic memory-maker logic?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 6 | 0 | 0 | Initial build; Panmnesia/UnifabriX profiles; CXL/PIM coverage | Company sites, KAIST, trade press |
