---
category_id: "05"
category_name: "Networking & Interconnect"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-06-09"
refresh_count: 1
total_companies: 6
active_companies: 6
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$700M+ [ESTIMATED]"
top_investors: ["Sutter Hill", "NVIDIA", "Atreides", "DCVC"]
key_technical_inflections: ["Scale-up bandwidth wall", "Ethernet-for-AI (UEC)", "Memory/IO fabric (CXL)", "DPU/SuperNIC", "Collective communication offload"]
key_open_questions: ["Can Ethernet displace InfiniBand for AI?", "Does a memory-fabric layer become a standalone market?", "Who wins the SuperNIC?"]
---

# 05 — Networking & Interconnect

> "The network is the computer." Scale-up/scale-out bandwidth is the binding constraint on AI clusters. Clear strategic acquirers. See [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis
- **Why now:** Collective communication dominates training time; AI clusters are bandwidth-bound; Ultra Ethernet (UEC) and CXL open contested ground around Broadcom/NVIDIA.
- **Venture-scale:** High in NICs/DPUs, memory/IO fabric, and Ethernet-for-AI; near-term with strong acquirer set.
- **Inflections:** Ethernet-for-AI, memory fabric (CXL pooling), SuperNIC/DPU, in-network collectives, optical scale-up (see [06](06_optical_interconnect_and_cpo.md)).
- **Acquirers:** NVIDIA, Broadcom, AMD, Cisco, Marvell, Intel. **Exit:** strategic M&A or IPO (Astera precedent).
- **Winning startup:** solves a specific cluster bottleneck (memory bandwidth, IO fan-out, congestion) better than Broadcom/NVIDIA. **Non-investable:** head-on standard-switching vs. Tomahawk/Jericho.

## 2. Market Context
- **Structure:** Broadcom (switching/ASIC), NVIDIA (InfiniBand/Spectrum, NVLink), Marvell, Cisco, Arista; CXL/UEC consortia; startups in fabric/NIC.
- **Segments:** AI training clusters, inference fleets, hyperscale DC fabric, HPC.
- **Drivers:** GPU utilization, congestion/tail latency, memory disaggregation, cost/W of bandwidth.
- **Bottlenecks:** Scale-up bandwidth (NVLink-class), congestion control, memory bandwidth, optics reach.
- **Competitive:** Astera Labs (public) sets the comp; startups target NIC/DPU + memory fabric.
- **Risks:** NVLink/Broadcom lock-in, standards timing, hyperscaler in-house.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Astera Labs | US | 2017 | Public (ALAB) | IPO 2024 | Sutter Hill, Fidelity | Smart connectivity (Aries/Taurus/Leo/Scorpio) | AI DC connectivity | PCIe/CXL retimers, CXL memory, fabric | Hyperscaler revenue; public | High | Active |
| Enfabrica | US | 2020 | Series C | ~$290M+ [TO VERIFY] | NVIDIA, Sutter Hill, Atreides | ACF SuperNIC / memory-fabric | AI cluster IO + memory | Converged network+memory fabric (EMFASYS) | Hyperscaler interest; NVIDIA-backed | High | Active |
| Xsight Labs | IL/US | 2017 | Late | ~$250M+ [TO VERIFY] | [TO VERIFY] | X2 Ethernet switch + E1 DPU | Ethernet-for-AI | High-radix programmable Ethernet | Sampling | Medium-High | Active |
| Cornelis Networks | US | 2020 | Series B/C | ~$130M+ [TO VERIFY] | Chevron Tech, DCVC | Omni-Path (CN5000) fabric | HPC/AI fabric | High-perf low-latency fabric (ex-Intel OPA) | HPC + AI customers | Medium-High | Active |
| Auradine | US | 2022 | Series B | ~$80M+ [TO VERIFY] | Celesta, MVP, Mayfield | DC infra/networking + (also mining) | DC infra | Networking + blockchain infra | Early | Medium | Active |
| Drivenets | IL | 2015 | Growth | ~$590M+ [TO VERIFY] | D1 Capital, Bessemer | Disaggregated network OS (AI fabric) | Telco/AI fabric | Software-based cluster routing | Telco + AI deployments | Medium | Active |

## 4. Company Profiles

### Astera Labs (public comparable)
- **Status:** Active (NASDAQ: ALAB) · **HQ:** Santa Clara, US · **Founded:** 2017 · **Founders:** Jitendra Mohan, Sanjay Gajendra, Casey Morrison
- **Stage:** Public (IPO Mar 2024) · **Funding:** private rounds + IPO; backed by Sutter Hill, Fidelity, Intel Cap, Sanmina · **Website:** asteralabs.com
- **Primary:** 05 · **Secondary:** 07 (CXL memory) · **One-Line:** Connectivity semiconductors (PCIe/CXL retimers, CXL memory controllers, smart cable modules, fabric switches) purpose-built for AI infrastructure.
- **Tech:** Aries retimers, Taurus Ethernet modules, Leo CXL memory controllers, Scorpio fabric switches + COSMOS software. **Differentiation:** first-mover in AI connectivity silicon with hyperscaler design wins + software. **Why it's here:** the public benchmark and exit comparable for private interconnect startups.
- **VC view:** the IPO that validated the category. **Data quality:** High (public filings). **Last updated:** 2026-06-09.

### Enfabrica
- **Status:** Active · **HQ:** Mountain View, US · **Founded:** 2020 · **Founders:** Rochan Sankar (CEO, ex-Broadcom), Shrijeet Mukherjee (ex-Google/Cisco)
- **Stage:** Series C · **Total Funding:** ~$290M+ [TO VERIFY] · **Last Round:** ~$125M Series C, 2025, NVIDIA-backed [TO VERIFY] · **Investors:** Sutter Hill, Atreides, NVIDIA, IAG · **Website:** enfabrica.net
- **Primary:** 05 · **Secondary:** 07 Memory · **One-Line:** Accelerated Compute Fabric SuperNIC and memory-fabric (EMFASYS) converging networking and memory for GPU clusters.
- **Tech:** ACF-S "SuperNIC" with very high aggregate bandwidth + CXL-attached memory pooling to feed GPUs and cut memory cost. **Differentiation:** converged network+memory fabric; **NVIDIA investment = strong validation + acquirer signal.** **Risk:** competing where NVIDIA/Broadcom are strong.
- **VC view:** High; acquirers = NVIDIA/Broadcom/AMD. **Data quality:** Medium. **Last updated:** 2026-06-09.

> Xsight Labs, Cornelis, Auradine, Drivenets covered at table level.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| SuperNIC / DPU | High | High | Medium | Medium-High | Real | High |
| Memory/IO fabric (CXL) | High | High | Medium | Medium | Real | High |
| Ethernet-for-AI switching | High | Very High | High | Very High (Broadcom) | Narrow | Medium |
| HPC fabric | Medium | High | Medium | High | Niche | Medium |
| Network OS / software fabric | Medium | Medium | Low-Medium | Medium | Real | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Sutter Hill | VC | Astera, Enfabrica | Seed–A | Repeat winner | Deep connectivity-silicon thesis |
| NVIDIA (NVentures) | Strategic | Enfabrica | C | Enfabrica | Fabric ecosystem |
| Atreides | Crossover | Enfabrica | C | Enfabrica | Crossover validation |
| DCVC | VC | Cornelis | B | Cornelis | HPC/AI fabric |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Amin Vahdat | Google | DC networking | Defines hyperscale fabric needs | Watchlist (incumbent) | Jupiter/Aquila | 5 | High |
| MIT/Stanford networking | MIT/Stanford | Congestion control, RDMA | Algorithms → silicon offload | Watchlist | Many | 4 | Medium |
| Rochan Sankar | Enfabrica (ex-Broadcom) | Fabric silicon | Founder pedigree | Confirmed (Enfabrica) | — | 5 | High |

## 8. Diligence Questions
- **Technical:** Aggregate bandwidth, congestion handling, CXL latency? Interop with NVLink/Spectrum/Tomahawk?
- **Market:** Scale-up vs. scale-out positioning; standards alignment (UEC/UCIe/CXL)?
- **Customer:** Hyperscaler design wins committed vs. trials?
- **Competitive:** Survives Broadcom/NVIDIA roadmap + bundling?
- **Financial:** ASIC NRE/mask cost; gross margin? **Founder:** networking-silicon shipping pedigree?
- **Exit:** Astera-style IPO or strategic acquisition logic?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 6 | 0 | 0 | Initial build; Astera comp + Enfabrica profile; fabric/NIC coverage | Public filings, company sites |
