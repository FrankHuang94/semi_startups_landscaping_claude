---
category_id: "07"
category_name: "Memory & Storage"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 8
active_companies: 8
archived_companies: 0
stealth_or_semi_stealth_companies: 1
total_disclosed_funding: "~$430M+ excl. Astera [ESTIMATED]"
top_investors: ["Atinum Investment", "IMM Investment", "Bow Wave Capital", "Grove Ventures", "Intel Capital", "Samsung", "SK hynix", "Micron Ventures"]
key_technical_inflections: ["Memory wall (bandwidth+capacity)", "HBM4 ramp on NVIDIA Rubin (2026)", "2026 DRAM/NAND shortage (memory supercycle)", "CXL 3.x pooling/computational memory", "High-Bandwidth Flash (HBF) standard", "3D-stacked DRAM on logic", "Memory-disaggregated AI servers"]
key_open_questions: ["Does CXL reach volume in AI DC now that DRAM is scarce and expensive?", "Does HBF create a new inference memory tier?", "Can 3D-stacked DRAM-on-logic displace HBM for inference?", "Do startups capture value vs. the 3 DRAM makers during a supercycle?"]
---

# 07 — Memory & Storage

> Memory is *the* AI bottleneck (capacity, bandwidth, cost) — and in 2026 it became a pricing and supply crisis as well. DRAM is a 3-player oligopoly, so startups play in the fabric, architecture and IP layer (CXL pooling/computational memory, memory-disaggregated servers, novel 3D-DRAM IP). Strategic-heavy exits. See [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis
- **Why now:** HBM is supply-constrained and dominates the AI accelerator BOM; HBM4 began its volume ramp in 2026 for NVIDIA Vera Rubin; AI demand pulled wafer capacity away from conventional DRAM/NAND and triggered a 2026 memory shortage with record contract-price increases (TrendForce forecast Q1 2026 conventional DRAM contract prices +90–95% QoQ and Q2 +58–63% QoQ [TO VERIFY — secondary reports of TrendForce]). Inference (long context, KV-cache, agentic memory) is shifting the bottleneck from compute to memory capacity — XCENA, Majestic Labs, d-Matrix and Positron all raised in 2025–26 explicitly on a "memory wall" thesis.
- **Venture-scale:** High in CXL computational memory/pooling silicon, memory-disaggregated AI servers, 3D-DRAM and PIM IP, and KV-cache/memory-tiering software. **Don't** try to make commodity DRAM/NAND.
- **Inflections:** CXL 3.x pooling + near-data processing (XCENA MX1), memory-disaggregated servers (Majestic Prometheus), High-Bandwidth Flash (HBF; SK hynix + Sandisk spec published Aug 2026), face-to-face 3D DRAM on logic (d-Matrix Raptor), HBM4/4E custom base dies, 3D DRAM cell IP (NEO).
- **Acquirers:** SK hynix, Samsung, Micron, Sandisk, Marvell, Astera, Microchip, NVIDIA (licensing/acqui-hire pattern, e.g., Enfabrica 2025 — see [05](05_networking_and_interconnect.md)). **Exit:** strategic M&A / licensing; supercycle pricing raises strategic valuations.
- **Winning startup:** owns memory-fabric/controller or 3D-memory IP with a memory-maker or hyperscaler partnership, and a production path (4nm tape-out, rack-level product). **Non-investable:** capital-intensive DRAM/NAND fab plays.

## 2. Market Context
- **Structure:** DRAM oligopoly (SK hynix, Samsung, Micron); NAND (Samsung, SK hynix/Solidigm, Kioxia, Sandisk, Micron); controller/IP (Astera, Marvell, Microchip, Rambus, XConn); CXL/computational-memory startups (Panmnesia, XCENA, UnifabriX); memory-centric AI systems (Majestic Labs, d-Matrix, Positron — latter two primarily in [02](02_inference_accelerators.md)).
- **HBM4 (2026):** TrendForce reported NVIDIA raised Rubin's HBM4 per-pin speed requirement, pushing supplier mass production to late 1Q26–early 2Q26 [TO VERIFY]; NVIDIA said at CES 2026 that Vera Rubin was in full production [TO VERIFY]; SK hynix remains the HBM share leader (MR-MUF; first to show 16-high HBM4 at CES 2026), Samsung uses 1c DRAM + in-house foundry base die, Micron ramping HBM4 on 1-beta in 2026 with HBM4E in development [TO VERIFY — TrendForce/company statements]. 16-high and HBM4E custom base dies (logic-foundry) are the 2H26–2027 battleground.
- **Memory supercycle / shortage:** Conventional DRAM and SSD shortages persisted through 2026; vendors (Samsung, SK hynix) guided to tightness through at least late 2027, with SK Group's chairman suggesting it could last to 2030 [TO VERIFY — secondary reports]. Hyperscalers reportedly pre-contracting 2027 supply at higher prices (per BofA, via secondary reports) [UNCONFIRMED]. Implication: TCO case for CXL pooling / stranded-memory recovery and for flash-based tiers (HBF) strengthened materially.
- **High-Bandwidth Flash (HBF):** Sandisk–SK hynix MoU (Aug 2025) → HBF consortium (Feb 2026) → first spec published via OCP at FMS (Aug 2026), reportedly up to 512 GB/stack and up to ~3 TB/s over UCIe [TO VERIFY]; positioned at HBM-class bandwidth with 8–16× capacity at similar cost (company claims). Sandisk targeted first HBF samples 2H 2026 and HBF-equipped inference devices early 2027 (2025 guidance) [TO VERIFY]. Google and Tenstorrent reportedly joined the initiative [UNCONFIRMED].
- **Segments:** AI training/inference memory, KV-cache offload, memory pooling for TCO, in-memory analytics, agent memory software.
- **Bottlenecks:** CXL latency and software support, ecosystem timing, PIM programmability, custom-DRAM supply for 3D-stacked designs (d-Matrix has not named a DRAM partner), DRAM allocation to startups during shortage.
- **Competitive:** Astera (CXL controllers), Rambus (IP), Marvell, XConn (CXL switch); startups in computational memory, pooling, 3D DRAM IP.
- **Risks:** CXL adoption still slower than hoped; memory makers internalize value (custom HBM base dies, HBF); startups cannot secure DRAM allocation in a shortage.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| XCENA | KR | ~2021 [TO VERIFY] | Series B | ~$185M (incl. $135M Series B, May 2026, ~$570M post) [CONFIRMED per company PR] | Atinum Investment, IMM Investment | MX1 CXL 3.x computational memory controller (RISC-V near-data cores, up to 2TB DDR5) | AI inference/DB memory expansion | Compute-in-CXL-memory on 4nm | 4nm MX1 mass production targeted 2H 2026 [TO VERIFY] | High | Active |
| Majestic Labs | US/IL | 2023 [TO VERIFY] | Series A | ~$100M (seed + Series A, Nov 2025) [CONFIRMED per company PR] | Bow Wave Capital (Series A lead per SiliconANGLE), Grove Ventures | Prometheus memory-disaggregated AI server (custom accelerator + memory-interface chips) | Memory-bound LLM/agentic inference | Up to 128TB memory per server (company claim) | Prometheus unveiled Apr 2026; early deployments (company claim); orders "several hundred $M" per industry estimates [UNCONFIRMED] | High | Active |
| Panmnesia | KR | 2022 | Series A+ | ~$80M+ equity; ~₩100B+ incl. grants [TO VERIFY] | Daekyo, SL Investment (Series A >$60M, Nov 2024, >$250M valuation [CONFIRMED per Blocks&Files]) | CXL 3.x switch/IP & memory pooling | AI DC memory disagg. | Low-latency CXL fabric IP (KAIST spinout) | CES awards; pilots; ~$30M follow-on May 2025 per PitchBook [UNCONFIRMED] | High | Active |
| UnifabriX | IL | 2020 | Seed | ~$11M [TO VERIFY] | Grove Ventures, Harel [TO VERIFY] | Smart Memory Node (CXL) | Memory pooling/HPC | CXL memory appliance, bandwidth boost | Demos; no new round found through 2026 | Medium-High | Active |
| MemVerge | US | 2017 | Series B | ~$44M [TO VERIFY] (prior est. ~$60M+) | Intel Cap, Cisco, NEA | Memory Machine + MemMachine (open-source AI agent memory layer, Sept 2025) | CXL memory orchestration; agent memory | Pivot from CXL tiering toward AI/agent memory software | XConn collaboration (Nov 2025) [TO VERIFY] | Medium | Active |
| Numem | US | 2018 | Series A | ~$10M [TO VERIFY] | Cambium Capital, Doorga Capital | NuRAM (MRAM) compute-in-memory IP / smart memory | AI memory subsystems | NVRAM/MRAM for AI | Early; no 2026 round found | Medium | Semi-Stealth |
| NEO Semiconductor | US | 2012 | Strategic/Seed | Undisclosed strategic round led by Stan Shih consortium (Apr 2026) [CONFIRMED per company PR] | Stan Shih (Acer founder)-led consortium | 3D X-DRAM / 3D NAND cell IP | DRAM scaling / HBM alternative IP | 3D DRAM built on 3D-NAND-like flow | 3D X-DRAM proof-of-concept validated (Apr 2026, company claim); licensing talks | Medium-High | Active |
| Astera Labs (Leo) | US | 2017 | Public | (see [05](05_networking_and_interconnect.md)) | Sutter Hill | CXL memory controllers | AI DC memory expansion | Production CXL controller | Hyperscaler revenue | High | Active |

## 4. Company Profiles

### XCENA (new — 2026)
- **Status:** Active · **HQ:** South Korea · **Founded:** ~2021 [TO VERIFY] · **CEO:** Jin Kim [TO VERIFY]
- **Stage:** Series B · **Total Funding:** ~$185M · **Latest:** $135M Series B (announced ~May 29, 2026) at ~$570M valuation, co-led by Atinum Investment and IMM Investment [CONFIRMED per company PR / TechCrunch coverage]; a July 2026 Korean report describes ~₩200B raised in this cycle [TO VERIFY].
- **Primary:** 07 · **Secondary:** 02 · **One-Line:** MX1 "computational memory" — a CXL 3.x memory controller with integrated RISC-V near-data cores pooling up to 2TB of DDR5, aimed at turning inference's "memory scaling problem" into an expandable memory tier.
- **Tech:** 4nm MX1; near-data processing for vector search, KV-cache, analytics. **Differentiation:** compute inside the CXL device rather than a passive expander. **Traction:** mass production targeted 2H 2026 [TO VERIFY]. **Risk:** CXL software adoption; Astera/Marvell/Samsung CMM-D competition; DRAM allocation in a shortage.
- **VC view:** High — best-funded pure CXL startup; acquirers = SK hynix/Samsung, Marvell, Astera. **Data quality:** Medium. **Last updated:** 2026-11-04.

### Majestic Labs (new — 2025/26)
- **Status:** Active · **HQ:** US / Israel · **Founders:** Ofer Shacham (CEO), Sha Rabii, Masumi Reynders (ex-Google/Meta custom silicon)
- **Stage:** Series A · **Funding:** ~$100M at stealth exit (Nov 10, 2025) [CONFIRMED per company PR]; split reported inconsistently ($10M seed + $90M A per Globes vs. $71M A led by Bow Wave Capital per SiliconANGLE) [TO VERIFY]; Grove Ventures participated.
- **Primary:** 07 · **Secondary:** 02, 16 · **One-Line:** "Prometheus" AI server that disaggregates memory from compute with custom accelerator + memory-interface chips — up to 128TB of high-bandwidth memory per server (company claim).
- **Traction:** Prometheus unveiled Apr 28, 2026; early deployments underway, broader availability 2027 (company); industry estimates of several hundred million dollars of paper orders [UNCONFIRMED — Globes]. **Risk:** system-level execution, memory supply, NVIDIA rack-scale incumbency.
- **VC view:** High (pedigree + clear memory-wall thesis). **Data quality:** Medium. **Last updated:** 2026-11-04.

### Panmnesia
- **Status:** Active · **HQ:** Daejeon, KR · **Founded:** 2022 · **Origin:** KAIST spinout (Myoungsoo Jung)
- **Stage:** Series A+ · **Total Funding:** Series A >$60M (Nov 2024) at >$250M valuation [CONFIRMED per Blocks&Files]; ~$12.5M seed (2023); PitchBook lists a further ~$30M (May 2025) and ~$100M total incl. grants [UNCONFIRMED] · **Investors:** Daekyo Investment, SL Investment, others · **Website:** panmnesia.com
- **Primary:** 07 · **Secondary:** 05 Fabric · **One-Line:** Ultra-low-latency CXL 3.x switch and IP enabling large-scale memory (and GPU) pooling/expansion for AI datacenters.
- **Tech:** sub-100ns CXL fabric IP, full-stack CXL switch SoC, memory/accelerator pooling; CES Innovation recognition; continued ISCA-level publication cadence in 2026. **Differentiation:** latency leadership + academic-grade CXL depth. **Risk:** CXL adoption timing, scaling GTM, now-better-funded XCENA as Korean peer.
- **VC view:** High; acquirers = memory makers, Astera, Marvell. No 2026 round found. **Data quality:** Medium. **Last updated:** 2026-11-04.

### UnifabriX
- **Status:** Active · **HQ:** Yokneam, IL · **Founded:** 2020 · **Founders:** Ronen Hyatt, Danny Volkind
- **Stage:** Seed · **Funding:** ~$11M seed [TO VERIFY]; a follow-on planned for 2H 2025 had not been reported closed as of 2026 · **Website:** unifabrix.com
- **Primary:** 07 · **One-Line:** "Smart Memory Node" CXL appliance for memory pooling and bandwidth expansion in HPC/AI servers.
- **Tech:** CXL-based memory appliance recovering stranded memory and boosting effective bandwidth; claims ~2× rack server density [TO VERIFY]. **VC view:** Medium-High, but financing risk rising vs. XCENA. **Data quality:** Low-Medium. **Last updated:** 2026-11-04.

### NEO Semiconductor
- **Status:** Active · **HQ:** San Jose, US · **Founded:** 2012 · **CEO:** Andy Hsu
- **One-Line:** 3D X-DRAM cell IP — vertically stacked DRAM built with 3D-NAND-like process, pitched as an HBM/DRAM-scaling alternative licensed to memory makers.
- **2026:** Announced 3D X-DRAM proof-of-concept validation and a strategic investment led by Acer founder Stan Shih (Apr 23, 2026; amount undisclosed) [CONFIRMED per company PR]; company-reported retention/endurance figures not independently verified; FMS 2026 keynote. **VC view:** Medium-High (IP/licensing option on the supercycle). **Data quality:** Low-Medium. **Last updated:** 2026-11-04.

> MemVerge (software; now AI-agent memory), Numem at table level; Astera Leo cross-referenced from [05](05_networking_and_interconnect.md). **Cross-references:** d-Matrix (primary [02](02_inference_accelerators.md)) presented *Raptor* at Hot Chips 2026 — a 4nm compute die face-to-face bonded onto custom DRAM (~32GB/card, ~100 TB/s claimed) — and announced an NVLink Fusion collaboration (Sept 2026; availability targeted Q4 2027) [TO VERIFY]; Positron AI (primary [02](02_inference_accelerators.md)) raised ~$230M (Feb 2026) on a memory-first inference thesis [TO VERIFY]. Sandisk/SK hynix HBF is tracked as an incumbent standard (Market Context).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| CXL switching/pooling | High (↑ with DRAM shortage) | High | Medium | Medium | Real | High |
| CXL computational memory | High | High | Medium-High | Medium (Samsung CMM, Astera) | Real (XCENA) | High |
| CXL memory controllers | High | High | Medium | High (Astera) | Narrow | Medium |
| Memory-disaggregated AI servers | High | Very High | High | High (NVIDIA rack-scale) | Real, high-variance | Medium-High |
| 3D-stacked DRAM-on-logic | High | Very High | High | High | High-variance | Medium-High |
| High-Bandwidth Flash (HBF) | Medium-High (new) | Very High | Very High | Very High (Sandisk/SK hynix) | Narrow (controllers/software) | Medium |
| Processing-in-memory IP | High | Very High | Medium-High | High (DRAM cos) | High-variance | Medium-High |
| Novel DRAM/NAND IP | Medium-High | Very High | High | High | Niche (IP) | Medium |
| KV-cache / agent memory software | High | Medium | Low | Medium | Real | Medium-High |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Atinum Investment / IMM Investment | VC/PE (KR) | XCENA | B | Co-led $135M Series B (May 2026) | Korean CXL champion |
| Bow Wave Capital / Grove Ventures | VC | Majestic Labs (Grove also UnifabriX) | Seed–A | ~$100M (Nov 2025) | Memory-wall systems |
| Intel Capital | Strategic | MemVerge | Seed–B | CXL ecosystem | Memory disaggregation |
| Samsung / SK hynix / Micron | Strategic | (PIM/CXL R&D, Eliyan, HBF consortium) | Various | HBM4, HBF standard | Memory-maker pull |
| Korean VCs (Daekyo, SL) | VC | Panmnesia | Seed–A | Panmnesia | CXL early bets |
| Stan Shih-led consortium | Angel/strategic | NEO Semiconductor | Strategic | Apr 2026 | Taiwan ecosystem pull for 3D DRAM IP |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Onur Mutlu | ETH Zürich | PIM / near-memory | Leading PIM research; commercial urgency | Likely Startup Signal | RowHammer, PIM survey | 5 | High |
| Myoungsoo Jung | KAIST | CXL systems | Panmnesia origin | Confirmed (Panmnesia) | CXL papers; ISCA 2026 | 5 | High |
| Samsung/SK hynix research | Corporate | HBM-PIM, CXL, HBF | Defines productizable PIM and HBF | Watchlist | HBM-PIM papers; HBF spec | 4 | High |

## 8. Diligence Questions
- **Technical:** CXL latency/bandwidth measured; OS/hypervisor support; PIM programmability/software? For 3D-DRAM-on-logic: who supplies the custom DRAM die and at what yield?
- **Market:** Pooling TCO case quantified at 2026 DRAM prices; which workloads (KV-cache, RAG/vector DB) pull first?
- **Customer:** Memory-maker or hyperscaler partnership signed? DRAM allocation secured through the shortage?
- **Competitive:** Defensible vs. Astera/Marvell/Rambus, Samsung CMM-D, HBF, and DRAM-maker internalization?
- **Financial:** IP-royalty vs. hardware margins; capital to product; exposure to memory price swings when the cycle turns?
- **Founder:** memory/controller silicon pedigree? **Exit:** strategic memory-maker logic, NVIDIA-style license/acqui-hire?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 6 | 0 | 0 | Initial build; Panmnesia/UnifabriX profiles; CXL/PIM coverage | Company sites, KAIST, trade press |
| 2026-11-04 | Full (Refresh #3) | 2 | 6 | 0 | Added XCENA ($135M Series B, ~$570M val., May 2026) and Majestic Labs (~$100M, Nov 2025; Prometheus Apr 2026); NEO 3D X-DRAM PoC + Stan Shih strategic round (Apr 2026); Panmnesia funding corrected (>$60M Series A); MemVerge pivot to agent memory; HBM4 ramp, 2026 DRAM shortage, HBF spec (Aug 2026), d-Matrix Raptor 3D DRAM cross-ref; heatmap expanded | Company PRs (XCENA, Majestic, NEO), TechCrunch, SiliconANGLE, Globes, Blocks&Files, TrendForce, Tom's Hardware, Next Platform, Futurum |
