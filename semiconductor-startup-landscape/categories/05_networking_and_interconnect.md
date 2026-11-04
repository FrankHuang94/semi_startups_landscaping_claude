---
category_id: "05"
category_name: "Networking & Interconnect"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 7
active_companies: 6
archived_companies: 1
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$2.5B+ private incl. archived Enfabrica; ~$2.3B active private (excl. Astera IPO) [ESTIMATED]"
top_investors: ["Fidelity", "NVIDIA", "Intel Capital", "Tiger Global", "IAG Capital Partners", "Sutter Hill", "Atreides", "Mayfield"]
key_technical_inflections: ["Scale-up bandwidth wall", "Open scale-up fabrics (UALink, ESUN) vs. NVLink Fusion", "Ethernet-for-AI (UEC 1.0)", "Memory/IO fabric (CXL)", "DPU/SuperNIC", "Collective communication offload"]
key_open_questions: ["Does UALink or Ethernet-based scale-up (ESUN) win vs. NVLink Fusion?", "Can startups ship scale-up switches before Broadcom/NVIDIA lock the rack?", "Who wins the SuperNIC?", "Are $2B+ pre-revenue switch valuations justified?"]
---

# 05 — Networking & Interconnect

> "The network is the computer." Scale-up/scale-out bandwidth is the binding constraint on AI clusters. 2025–26 brought NVIDIA's licensing-style takeout of Enfabrica, unicorn rounds for Xsight Labs and Upscale AI, and Astera Labs' Scorpio scale-up switch ramp. See [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis
- **Why now:** Collective communication dominates training time and inference fleets need rack-scale memory/bandwidth; AI clusters are bandwidth-bound. Open standards (UALink 1.0, Ultra Ethernet 1.0, ESUN) open contested ground around NVIDIA NVLink and Broadcom.
- **Venture-scale:** High in scale-up switches, NICs/DPUs, memory/IO fabric, and Ethernet-for-AI; strong acquirer set and now growth-equity appetite (Xsight $2.8B, Upscale AI $2B valuations).
- **Inflections:** Open scale-up switching (UALink/ESUN), Ethernet-for-AI (UEC), memory fabric (CXL pooling), SuperNIC/DPU, in-network collectives, optical scale-up (see [06](06_optical_interconnect_and_cpo.md)).
- **Exit pattern update:** NVIDIA paid a reported >$900M (cash + stock) to hire Enfabrica's CEO/team and license its technology (Sept 2025) [CONFIRMED — per CNBC/Reuters] rather than acquire the company outright — the same "license + acqui-hire" template used in AI chips (see [02](02_inference_accelerators.md)). Investors must underwrite this exit form (who gets paid, what remains of the entity).
- **Acquirers:** NVIDIA, Broadcom, AMD, Cisco, Marvell, Intel, Qualcomm, Arista. **Exit:** strategic M&A / license-and-hire or IPO (Astera precedent).
- **Winning startup:** solves a specific cluster bottleneck (scale-up fan-out, memory bandwidth, congestion) better than Broadcom/NVIDIA and ships on an open standard. **Non-investable:** head-on standard scale-out switching vs. Tomahawk/Jericho without differentiation.

## 2. Market Context
- **Structure:** Broadcom (Tomahawk/Jericho switching, custom ASIC), NVIDIA (InfiniBand/Spectrum-X, NVLink + NVLink Fusion), Marvell, Cisco, Arista; UALink/UEC/CXL/OCP consortia; startups in scale-up switches, fabric, NIC.
- **Standards status (2026):** UALink 1.0 spec released Apr 2025 [CONFIRMED]; Ultra Ethernet 1.0 spec released Jun 2025 [CONFIRMED]; ESUN (Ethernet for Scale-Up Networking) workstream launched at OCP in Oct 2025 by hyperscalers and vendors [TO VERIFY]. First merchant UALink switch silicon (Upscale AI SkyHammer) targeted Q4 2026 [TO VERIFY]; Cornelis plans an "Active Compute Fabric" using UALink + ESUN for scale-up and UEC for scale-out (Sept 2026) [CONFIRMED — HPCwire].
- **Segments:** AI training clusters, inference fleets, hyperscale DC fabric, HPC.
- **Drivers:** GPU utilization, rack-scale scale-up domains (72→1,000+ accelerators), congestion/tail latency, memory disaggregation, cost/W of bandwidth.
- **Bottlenecks:** Scale-up bandwidth (NVLink-class), congestion control, memory bandwidth, copper reach → optics.
- **Competitive:** Astera Labs (public) sets the comp — Q2 2026 revenue a record $392.4M and Q3 2026 guidance $540–560M on the Scorpio X-Series scale-up switch ramp [CONFIRMED — company PR]. Startups target scale-up switches, NIC/DPU, memory fabric.
- **Risks:** NVLink/Broadcom lock-in, standards timing, hyperscaler in-house, pre-product valuations.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Astera Labs | US | 2017 | Public (ALAB) | IPO Mar 2024 | Sutter Hill, Fidelity | Smart connectivity (Aries/Taurus/Leo/Scorpio P & X) | AI DC connectivity + scale-up switching | PCIe/CXL retimers, CXL memory, fabric switches | Q2 2026 rev $392.4M record; Q3 guide $540–560M [CONFIRMED] | High | Active (Public) |
| Xsight Labs | IL/US | 2017 | Late-stage growth | ~$530M+ [ESTIMATED]; $300M+ round Jul 2026 at $2.8B post [CONFIRMED] | Fidelity (2026 lead), Intel Capital, Atreides, Valor, T. Rowe Price | X2 Ethernet switch + E1 DPU | Ethernet-for-AI / cloud | High-radix programmable Ethernet; UEC roadmap | Unicorn round Jul 30 2026 | High | Active |
| Upscale AI | US | 2025 [TO VERIFY] | Series A-1 | ~$500M [TO VERIFY]; $200M Series A Jan 2026 [CONFIRMED]; $190M A-1 Jun 2026 at ~$2B [TO VERIFY] | Tiger Global, Mayfield, NVIDIA, Intel Capital, Qualcomm Ventures, Salesforce Ventures, Temasek | SkyHammer UALink scale-up switch + open rack networking | Rack-scale AI scale-up | Open (UALink/ESUN/SONiC) NVSwitch alternative | Chip (TSMC) targeted Q4 2026; pre-revenue | High | Active |
| Cornelis Networks | US | 2020 | Growth | ~$335M [TO VERIFY]; $205M round Sept 2026 [CONFIRMED] | IAG Capital Partners (2026 lead), Chevron Tech, DCVC | Omni-Path CN5000 (shipping), CN6000 800G UEC SuperNIC (sampling), CN7000 1.6T (2027) | HPC/AI fabric | Low-latency fabric (ex-Intel OPA) now UEC/UALink/ESUN | Qualcomm partnership announced with raise [TO VERIFY] | Medium-High | Active |
| Auradine | US | 2022 | Series C | ~$314M [TO VERIFY] (incl. $153M Series C Apr 2025 [CONFIRMED]) | StepStone (C lead), Samsung Catalyst, Qualcomm Ventures, Celesta, Mayfield | Bitcoin-mining ASICs + AuraLinks AI networking unit | Mining + AI DC networking | UALink/UEC-based AI networking group | Mining revenue; AI unit early | Medium | Active |
| Drivenets | IL | 2015 | Growth | ~$590M+ [TO VERIFY] | D1 Capital, Bessemer | Disaggregated network OS (AI fabric) | Telco/AI fabric | Software-based cluster routing | Telco + AI deployments; no 2026 update verified | Medium | Active |
| Enfabrica | US | 2019/2020 | Licensed / acqui-hired | ~$260M raised (per Reuters) | Atreides, Sutter Hill, NVIDIA | ACF SuperNIC / EMFASYS memory fabric | (team + tech licensed to NVIDIA) | Converged network+memory fabric | NVIDIA >$900M cash+stock to hire CEO/staff + license tech, Sept 2025 [CONFIRMED per CNBC/Reuters] | Archived | Licensed/Acqui-hired (NVIDIA) |

## 4. Company Profiles

### Astera Labs (public comparable)
- **Status:** Active (NASDAQ: ALAB) · **HQ:** Santa Clara, US · **Founded:** 2017 · **Founders:** Jitendra Mohan, Sanjay Gajendra, Casey Morrison
- **Stage:** Public (IPO Mar 2024) · **Funding:** private rounds + IPO; backed by Sutter Hill, Fidelity, Intel Cap, Sanmina · **Website:** asteralabs.com
- **Primary:** 05 · **Secondary:** 07 (CXL memory) · **One-Line:** Connectivity semiconductors (PCIe/CXL retimers, CXL memory controllers, smart cable modules, Scorpio P/X fabric switches) purpose-built for AI infrastructure.
- **2026 performance:** Q2 2026 revenue a record $392.4M (vs. ~$361M consensus); Q3 2026 guidance $540–560M (~40% q/q at midpoint), non-GAAP EPS $1.16–1.21, gross margin ~72% as mix shifts to switches/modules; management said Scorpio becomes the largest product family in Q3, driven by the Scorpio X-Series 320-lane scale-up fabric switch production ramp [CONFIRMED — Astera Q2 2026 release, Aug 4 2026]. Q3 2026 actuals (reported ~Nov 3 2026) not captured in this refresh [TO VERIFY].
- **Why it's here:** the public benchmark and exit comparable for private interconnect startups — and now a direct scale-up switch competitor to Upscale AI and others.
- **VC view:** the IPO that validated the category. **Data quality:** High (public filings). **Last updated:** 2026-11-04.

### Xsight Labs
- **Status:** Active · **HQ:** Kiryat Gat/Tel Aviv, IL + Silicon Valley [TO VERIFY] · **Founded:** 2017 · **Founders:** Guy Koren (CEO), Erez Shaizaf [TO VERIFY]
- **Stage:** Late-stage growth · **Total Funding:** ~$530M+ [ESTIMATED; aggregators conflict] · **Last Round:** >$300M, closed Jul 30 2026, at $2.8B post-money, led by Fidelity Management & Research with Intel Capital; Atreides, Valor, T. Rowe Price also reported [CONFIRMED — Intel Capital release / Globes] · **Website:** xsightlabs.com
- **Primary:** 05 · **One-Line:** Open, programmable X2 Ethernet switch and E1 Arm-based DPU for AI and cloud networks.
- **Use of funds:** multi-generation switch + DPU roadmap including UEC support; team expansion (company-stated). **Differentiation:** one of very few independent merchant Ethernet switch silicon vendors. **Risk:** Broadcom Tomahawk dominance; NVIDIA Spectrum-X.
- **VC view:** High; potential IPO candidate or strategic target (Intel, AMD, Marvell, Cisco). **Data quality:** Medium. **Last updated:** 2026-11-04.

### Upscale AI (new)
- **Status:** Active, pre-revenue · **HQ:** Santa Clara, US [TO VERIFY] · **Founded:** 2025 [TO VERIFY] (emerged from Auradine's AuraLinks AI networking group [TO VERIFY])
- **Stage:** Series A-1 · **Total Funding:** ~$500M [TO VERIFY] · **Rounds:** seed ~2025 (>$100M implied) [ESTIMATED]; $200M Series A Jan 21 2026 with Intel Capital and Qualcomm Ventures participating, bringing outside funding to >$300M [CONFIRMED — SiliconANGLE/HPCwire]; $190M Series A-1 ~Jun 2026 at ~$2B valuation with NVIDIA participation [TO VERIFY — DCD/aggregators; one April report called it a Series B in talks] · **Investors:** Tiger Global, Mayfield, NVIDIA, Intel Capital, Qualcomm Ventures, Salesforce Ventures, Temasek
- **Primary:** 05 · **Secondary:** 06 · **One-Line:** Open-standards rack-scale AI networking — SkyHammer UALink 1.0 scale-up switch (up to 1,024 accelerators per pod) positioned as an NVSwitch alternative.
- **Tech:** TSMC-built scale-up switch ASIC + open software (SONiC/SAI); availability targeted Q4 2026 [TO VERIFY]. **Differentiation:** first merchant UALink switch for operators avoiding NVLink lock-in. **Risk:** no product shipped yet; Astera Scorpio X, Broadcom (Tomahawk Ultra/ESUN path) and NVLink Fusion compete; UALink vs. Ethernet scale-up uncertainty.
- **VC view:** High-variance; three rounds in ~9 months is a hot-market signal. **Data quality:** Medium-Low. **Last updated:** 2026-11-04.

### Enfabrica (archived — licensed/acqui-hired by NVIDIA)
- **Status:** NVIDIA paid >$900M in cash and stock to hire CEO Rochan Sankar and other staff and license Enfabrica's technology; closed ~Sept 2025 [CONFIRMED — per CNBC, Reuters; companies did not comment]. Not a full acquisition; residual corporate entity status [TO VERIFY].
- **Pre-exit:** ~$260M VC raised (per Reuters); $125M Series B 2023 led by Atreides with NVIDIA; later round post-money ~$600M (PitchBook estimate) [UNCONFIRMED]. Tech: ACF-S SuperNIC (claimed ability to connect ~100k GPUs) + EMFASYS CXL memory pooling.
- **Why it matters:** sets the networking-category comp for NVIDIA's license-and-hire exits; reported deal value (>$900M) vs. ~$600M estimated last post-money implies a modest step-up, but distribution to preferred holders is undisclosed [TO VERIFY]. **Last updated:** 2026-11-04.

> Cornelis, Auradine, Drivenets covered at table level. Cornelis: $205M Sept 2026 led by IAG Capital Partners; CN5000 shipping, CN6000 800G UEC SuperNIC sampling with broader availability Q4 2026; CN7000 (1.6T) slated 2027 [CONFIRMED — HPCwire]. Exits are logged in [../deal_tracker/23_exit_and_shutdown_tracker.md](../deal_tracker/23_exit_and_shutdown_tracker.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Open scale-up switching (UALink/ESUN) | Very High | Very High | High | High (NVLink, Broadcom, Astera) | Real but crowded; valuations rich | High |
| SuperNIC / DPU | High | High | Medium | Medium-High | Real (Enfabrica exit proves pull) | High |
| Memory/IO fabric (CXL) | High | High | Medium | Medium | Real | Medium-High |
| Ethernet-for-AI scale-out switching | High | Very High | High | Very High (Broadcom) | Narrow — Xsight the exception | Medium |
| HPC fabric | Medium | High | Medium | High | Niche, pivoting to UEC/UALink | Medium |
| Network OS / software fabric | Medium | Medium | Low-Medium | Medium | Real | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Fidelity | Crossover | Xsight, (Astera) | Growth | Led Xsight >$300M (Jul 2026) | Pre-IPO networking silicon |
| NVIDIA (NVentures) | Strategic | Upscale AI, (Enfabrica) | A–C | Upscale A-1; Enfabrica license+hire | Hedges open scale-up while owning NVLink |
| Intel Capital | Strategic | Xsight, Upscale AI | A–Growth | Both 2026 rounds | Open Ethernet/UALink ecosystem |
| Qualcomm Ventures | Strategic | Upscale AI, Auradine | A–C | Upscale Jan 2026 | DC networking for Qualcomm AI200/AI250 |
| Tiger Global | Crossover | Upscale AI | A | Upscale rounds | Momentum in AI infra |
| IAG Capital Partners | VC | Cornelis | Growth | Led $205M (Sept 2026) | HPC/AI fabric |
| Sutter Hill | VC | Astera, (Enfabrica) | Seed–A | Repeat winner | Deep connectivity-silicon thesis |
| Atreides | Crossover | Xsight, (Enfabrica) | B–Growth | Xsight 2026 | Crossover validation |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Amin Vahdat | Google | DC networking | Defines hyperscale fabric needs | Watchlist (incumbent) | Jupiter/Aquila | 5 | High |
| MIT/Stanford networking | MIT/Stanford | Congestion control, RDMA | Algorithms → silicon offload | Watchlist | Many | 4 | Medium |
| Rochan Sankar | NVIDIA (ex-Enfabrica, ex-Broadcom) | Fabric silicon | Founder pedigree; now inside NVIDIA | Confirmed (exit) | — | 4 | High |

## 8. Diligence Questions
- **Technical:** Aggregate bandwidth, radix, latency for scale-up; congestion handling; CXL latency? Interop with NVLink Fusion/Spectrum/Tomahawk? UALink 1.0 vs. ESUN compliance?
- **Market:** Scale-up vs. scale-out positioning; which standard wins (UALink vs. ESUN vs. NVLink Fusion)?
- **Customer:** Hyperscaler/neocloud design wins committed vs. trials? Silicon in hand vs. roadmap?
- **Competitive:** Survives Broadcom/NVIDIA roadmap + bundling, and Astera Scorpio X?
- **Financial:** ASIC NRE/mask cost; gross margin; is a $2B+ pre-revenue valuation covered by a realistic exit? **Founder:** networking-silicon shipping pedigree?
- **Exit:** Astera-style IPO, strategic acquisition, or NVIDIA-style license + acqui-hire (how are preferred holders paid)?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 6 | 0 | 0 | Initial build; Astera comp + Enfabrica profile; fabric/NIC coverage | Public filings, company sites |
| 2026-11-04 | Full (Refresh #3) | 1 | 4 | 1 | Added Upscale AI (profiled; $200M Jan 2026 + $190M A-1 at ~$2B). Archived Enfabrica (NVIDIA >$900M license + acqui-hire, Sept 2025). Updated Astera (Q2 2026 record $392.4M; Q3 guide $540–560M, Scorpio X ramp), Xsight (>$300M at $2.8B, Jul 2026; new profile), Cornelis ($205M, Sept 2026; CN6000/CN7000; UALink+ESUN), Auradine ($153M Series C Apr 2025; AuraLinks AI). Thesis/market rewritten for open scale-up standards war. | CNBC/Reuters via DCD/Tom's HW (Enfabrica); Astera IR; Intel Capital + Globes (Xsight); SiliconANGLE/HPCwire/DCD (Upscale); HPCwire (Cornelis); The Block/SiliconANGLE (Auradine) |
