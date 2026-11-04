# Investment Theses — AI Semiconductor Landscape

A 3–5 year, category-by-category thesis map for a VC team building a proprietary sourcing and diligence system in AI semiconductor infrastructure. Each thesis states *why now*, where venture-backed startups can and cannot win, and the evidence that would upgrade or downgrade the view.

> Theses are analytical opinions for internal pipeline shaping, not recommendations. Re-rate at each full refresh.
>
> **Last re-rated:** 2026-11-04 (Refresh #3). Previous rating: 2026-06-09.

---

## What Changed Since the Last Rating (Jun → Nov 2026)

The market moved faster in late 2025–2026 than the original build assumed. The key facts behind the re-rating (details and confidence tags in the linked trackers):

1. **Exits came, but mostly not in the expected shape.** NVIDIA's ~$20B non-exclusive licence of Groq's technology plus hiring of its leadership (Dec 2025) [reported value] and its >$900M Enfabrica licence + team hire (Sep 2025) made the **"licence + acqui-hire" (reverse acquihire)** a mainstream exit route. Conventional M&A also cleared: Marvell–Celestial AI (closed 2026-02-02, ~$3.25B upfront) [CONFIRMED], Meta–Rivos (2025), Qualcomm–Ventana (Dec 2025) and Qualcomm–Alphawave (~$2.4B, Dec 2025), AMD–Taalas (Aug 2026), Microchip–Hailo (2026), NXP–Kinara ($307M, Oct 2025), ADI–Empower ($1.5B, 2026). See [deal_tracker/20_ma_tracker.md](deal_tracker/20_ma_tracker.md).
2. **The IPO window reopened.** Cerebras listed on Nasdaq (CBRS) on 2026-05-14, raising ~$5.5B [CONFIRMED]. Chinese GPU makers (Moore Threads, MetaX, Biren) listed in Dec 2025–Jan 2026. SiFive and Rebellions are openly pre-IPO.
3. **Inference mega-rounds became the norm.** Tenstorrent $1.5B at $6.2B (Oct 2026), FuriosaAI $620M at $2.9B (Oct 2026), MatX $500M (Feb 2026), Etched ~$500M (Jan 2026) plus later rounds at much higher marks [TO VERIFY], Positron $230M, Fractile $220M, Rebellions $400M pre-IPO. Valuations now price in exit optionality created by NVIDIA/AMD deal-making.
4. **Interconnect and optics funding broke out.** Ayar Labs $500M Series E (Mar 2026), Lumilens $700M+ Series C (Aug 2026), Xsight Labs >$300M at $2.8B (Jul 2026), Upscale AI ~$390M across two 2026 rounds, Cornelis $205M (Sep 2026). CPO switches from NVIDIA and Broadcom moved from sampling to early deployment.
5. **Memory became the acute bottleneck.** HBM4 ramped for NVIDIA Vera Rubin; DRAM contract prices roughly doubled in early 2026 (TrendForce) and the shortage is expected to run into 2027+. This lifts memory-architecture startups (CXL/compute-in-memory/memory-dense servers).
6. **AI-for-chip-design was the breakout software wedge.** Ricursive Intelligence $300M Series A at ~$4B (Jan 2026), ChipAgents (Series A total $134M), Cognichip $60M Series A.
7. **Demand stayed strong.** Big-cloud 2026 capex is tracking ~$800B+ (company guidance and press tallies), and hyperscalers signal higher 2027 spend. Custom silicon scaled too: Google sells TPUs outside its own cloud (Anthropic up to 1M TPUs), OpenAI has 10 GW with Broadcom and 6 GW with AMD, and AMD agreed to invest up to $5B in Anthropic.

**Net re-rating:** Interconnect/optics, memory, and power delivery are upgraded. Inference stays High, but entry valuations are now a real risk. Training stays Medium (the Cerebras IPO validates the endgame, but the field has narrowed). EDA is upgraded to the top tier on the AI-for-design wave. Edge stays Medium, though M&A is now proven (Hailo, Kinara).

---

## Thesis Ratings Summary

| Category | VC Attractiveness | Time Horizon | Capital Intensity | Incumbent Risk | Exit Potential | Overall Priority | Change (Nov 2026) |
|----------|:-----------------:|:------------:|:-----------------:|:--------------:|:--------------:|:----------------:|:-----------------:|
| 01 Training Accelerators | Medium | 2–4 yr | Very High | Very High (NVIDIA) | High (IPO proven: Cerebras) | Medium | ↔ |
| 02 Inference Accelerators | **High** | 1–3 yr | High | High | **Very High** (licence/M&A/IPO) | **High** | ↔ (valuation risk ↑) |
| 03 Edge Inference | Medium | 2–4 yr | Medium | Medium | Medium-High (M&A proven) | Medium | ↑ exit |
| 04 Custom ASIC & Chiplets | **High** | 1–3 yr | Medium-High | Medium | High (RISC-V roll-up: Meta, Qualcomm) | **High** | ↔ |
| 05 Networking & Interconnect | **High** | 1–3 yr | Medium | High (Broadcom/NVDA) | **Very High** (NVIDIA–Enfabrica, Arm–DreamBig) | **High** | ↑ |
| 06 Optical Interconnect & CPO | **High** | 2–4 yr | High | Medium | **Very High** (Marvell–Celestial) | **High** | ↑ (timeline pulled in) |
| 07 Memory & Storage (CXL/PIM) | **High** | 2–4 yr | High | High (3 DRAM makers) | Medium-High | **High** | ↑ (shortage) |
| 08 Power & Power Delivery | **High** | 1–3 yr | Medium-High | Medium | **High** (ADI–Empower $1.5B) | **High** | ↑ |
| 09 Security & Confidential Compute | Medium | 2–5 yr | Medium | Medium | Medium | Medium | ↔ |
| 10 RF & Wireless | Low | 3–5 yr | Medium | High | Low-Medium | Low | ↔ |
| 11 Analog, Mixed-Signal & Timing | Medium | 2–4 yr | Medium | High | Medium (M&A) | Medium | ↔ |
| 12 EDA, IP & Design Tools | **High** | 1–3 yr | Low-Medium | High (Synopsys/Cadence) | High (M&A) | **High** | ↑ (AI-for-design) |
| 13 Foundry, Packaging & Chiplets | High | 3–6 yr | Very High | High | Medium-High | High | ↔ (litho startups ↑) |
| 14 Quantum / Neuromorphic / Analog | Medium | 4–10 yr | Very High | Low (greenfield) | Binary | Medium | ↔ |
| 15 Automotive & Robotics Silicon | Medium | 2–5 yr | High | High | Medium | Medium | ↔ |
| 16 DC Infrastructure Enablers | **High** | 1–3 yr | Medium-High | Medium | High | **High** | ↔ |
| 17 Research-to-Startup Pipeline | **High** | 0–2 yr (sourcing) | n/a | n/a | n/a (sourcing) | **High** | ↔ (lab-to-unicorn faster) |

---

## 01 — Training Accelerators
- **3–5 yr thesis:** Frontier-model training is a capex super-cycle, but it is the *hardest* category for startups: NVIDIA's CUDA moat, packaging/HBM supply allocation, and systems integration favor incumbents and hyperscaler in-house silicon (TPU, Trainium, MTIA). Venture-scale wins require a genuinely differentiated systems story (wafer-scale, dataflow, memory bandwidth) **and** a captive demand anchor (sovereign, hyperscaler, or model lab).
- **Why now / what changed:** Model training demand is structurally supply-constrained; nations and clouds want NVIDIA alternatives; HBM and CoWoS are the real bottlenecks.
- **Where startups win:** Differentiated memory/bandwidth architectures (Cerebras wafer-scale), sovereign-AI demand (G42), or pivoting to inference/cloud services. **Where they don't:** "Better GPU" plays without software or supply.
- **Watch companies:** Cerebras, SambaNova, Tenstorrent, MatX, Graphcore (acquired). **Labs/researchers:** Stanford/Dally, Berkeley ADEPT. **Active investors:** G42, SoftBank, Samsung, Benchmark. **Likely acquirers:** AMD, Intel, hyperscalers, SoftBank.
- **Risks:** CUDA lock-in, capital intensity, HBM allocation, demand concentration.
- **Upgrade if:** A startup lands a multi-year sovereign or hyperscaler training commitment. **Downgrade if:** NVIDIA Rubin-class roadmap + supply expansion closes the gap.
- **Nov 2026 update:** The upgrade trigger fired for Cerebras: OpenAI signed a 750 MW / >$10B compute deal (Jan 2026) [reported], followed by a $1B Series H and a Nasdaq IPO (May 2026) [CONFIRMED]. Graphcore is inside SoftBank. Intel's talks to buy SambaNova stalled and became a minority stake plus partnership. Tenstorrent ($1.5B at $6.2B) and MatX ($500M Series B) are the remaining venture-scale independents. **Watch now:** Tenstorrent, MatX, SambaNova, Cerebras (public comp). Vera Rubin (HBM4) shipping in 2H26 resets the bar.

## 02 — Inference Accelerators
- **3–5 yr thesis:** Inference is the best risk/reward in the landscape. The market is shifting from training to serving; cost-per-token and latency are board-level metrics; workloads (transformers) are stable enough to specialize silicon against. Startups can win on perf/$ and perf/W for serving, especially for reasoning/long-context and high-throughput batch.
- **Why now:** LLM serving cost is the dominant opex; transformer architecture stability enables ASIC specialization (Etched's bet); enterprises want NVIDIA alternatives for inference where CUDA lock-in is weaker.
- **Where startups win:** Deterministic low-latency (Groq), memory-centric inference (d-Matrix), transformer-hardwired ASICs (Etched), sovereign/regional clouds (Rebellions, FuriosaAI). **Where they don't:** Undifferentiated GPUs; ignoring the compiler/software burden.
- **Watch:** Groq, d-Matrix, Etched, Positron, Rebellions, FuriosaAI, SambaNova. **Investors:** BlackRock, Temasek, Atreides, Samsung. **Acquirers:** AMD, Qualcomm, hyperscalers, networking incumbents.
- **Risks:** Software ecosystem, model-architecture drift, NVIDIA inference price cuts.
- **Upgrade if:** Independent MLPerf-class wins + multi-customer revenue. **Downgrade if:** A single open software stack (e.g., NVIDIA Dynamo/vLLM ubiquity) neutralizes hardware edge.
- **Nov 2026 update:** NVIDIA validated the thesis by paying a reported ~$20B to license Groq's LPU technology and hire its leaders (Dec 2025). AMD bought Taalas (Aug 2026), and Unconventional AI agreed to buy NeuReality (Oct 2026). Capital followed: FuriosaAI $620M, Etched ~$500M+ (later rounds at much higher marks [TO VERIFY]), Positron $230M, Fractile $220M, d-Matrix $275M, Rebellions $400M pre-IPO. **New risk:** entry valuations ($1–20B+) for pre-volume silicon. Underwrite to signed capacity contracts (e.g., Cerebras–OpenAI-style) rather than benchmarks. **Watch:** d-Matrix, Etched, Positron, Fractile, MatX, FuriosaAI, Rebellions, residual Groq/GroqCloud.

## 03 — Edge Inference Chips
- **Thesis:** Large but fragmented; design wins are sticky but small; venture outcomes mostly via strategic M&A (automotive, industrial, consumer). Physical-AI/robotics is the new pull.
- **Win:** Power-efficiency leadership + reference software + a vertical anchor (vision, robotics, automotive). **Lose:** Horizontal "edge AI chip" with no GTM.
- **Watch:** Axelera AI, SiMa.ai, DeepX, Quadric, Kneron. **Acquirers:** automotive Tier-1s, Qualcomm, NXP, Renesas, ST, Microchip.
- **Nov 2026 update:** The M&A exit path is proven: NXP bought Kinara ($307M, Oct 2025) and Microchip agreed to buy Hailo (2026). Axelera raised >$250M (Feb 2026). Physical AI/robotics demand is the main new pull.

## 04 — Custom ASIC & Chiplets
- **Thesis:** Every hyperscaler and AI lab now wants custom silicon; the merchant ASIC/chiplet enablement layer (interconnect IP, D2D, design services, RISC-V platforms) is a high-conviction, capital-efficient way to ride that without betting on one chip winning. UCIe + chiplet disaggregation creates a new IP/tooling market.
- **Win:** D2D interconnect IP/fabric (Eliyan, Baya), RISC-V server platforms (Rivos, Ventana), turnkey chiplet design. **Lose:** Pure design services without IP leverage.
- **Watch:** Eliyan, Baya Systems, SiFive (pre-IPO), Chipletz. **Acquirers:** Broadcom, Marvell, Qualcomm, Meta, Synopsys, Cadence, hyperscalers. **Investors:** Matrix, Intel Capital, MediaTek, Atreides, NVIDIA.
- **Nov 2026 update:** RISC-V server/IP consolidated fast: Meta–Rivos (2025), Qualcomm–Ventana (Dec 2025), Tenstorrent–Blue Cheetah (Jul 2025), and a reported Qualcomm–Akeana deal (Oct 2026) [TO VERIFY]. SiFive raised $400M at $3.65B (Apr 2026), which it calls its last private round. Few independent RISC-V server plays remain. Whitespace has shifted to D2D/UCIe IP, NoC fabrics and turnkey chiplet integration.

## 05 — Networking & Interconnect
- **Thesis:** The network is the computer. Scale-up/scale-out bandwidth is the binding constraint on AI clusters; Broadcom and NVIDIA dominate but leave room in NICs/DPUs, memory-fabric, and Ethernet-for-AI. High-conviction, nearer-term, with clear strategic acquirers.
- **Win:** Memory/IO fabric (Enfabrica), high-radix Ethernet (Xsight), HPC fabric (Cornelis), CXL switching. **Lose:** Competing head-on with Broadcom Tomahawk/Jericho on standard switching.
- **Watch:** Upscale AI, Xsight Labs, Cornelis, Auradine, Astera Labs (public comp). **Acquirers:** NVIDIA, Broadcom, AMD, Arm, Cisco, Marvell.
- **Nov 2026 update:** Open scale-up fabrics (UALink, ESUN) and scale-out fabrics (Ultra Ethernet) created a merchant-switch opening. Upscale AI raised ~$390M in 2026 and Xsight >$300M at $2.8B. NVIDIA licensed Enfabrica and hired its team (Sep 2025), and Arm agreed to buy DreamBig (~$265M). Astera Labs' revenue ramp (Q2'26 $392M, Q3 guide $540–560M) [CONFIRMED] is the public proof point for scale-up switching.

## 06 — Optical Interconnect & CPO
- **Thesis:** Copper is hitting reach/energy limits at scale-up; co-packaged optics and optical I/O are a genuine technical inflection with venture-scale potential. Capital-intensive and timeline risk, but strategic pull from NVIDIA/Broadcom and hyperscalers is strong. One of the highest-quality hard-tech theses.
- **Win:** Optical I/O chiplets (Ayar), optical compute-interconnect fabric (Celestial AI, Lightmatter), wavelength-scaled links (Xscape). **Lose:** Sub-scale photonics without packaging/supply and a host-silicon design win.
- **Watch:** Ayar Labs, Lightmatter, Lumilens, Xscape, nEye, Salience Labs, OpenLight, Avicena, Lightelligence. **Labs:** Columbia/Bergman, MIT, UCSB. **Acquirers:** NVIDIA, Broadcom, Marvell, Ciena, Cisco, Intel.
- **Nov 2026 update:** The thesis is validated earlier than expected. Marvell–Celestial AI closed (Feb 2026; $3.25B upfront, up to $5.5B with earn-out) [CONFIRMED], and Ciena–Nubis ($270M) went through. Broadcom's TH6-Davisson CPO switch shipped, and NVIDIA Spectrum-X/Quantum-X Photonics entered early deployment. Funding: Ayar $500M Series E plus a $150M extension, Lumilens $700M+ at $5.51B, Salience $125M, nEye $80M. The horizon is cut from 2–5 years to 2–4.

## 07 — Memory & Storage (CXL, PIM, HBM-adjacent)
- **Thesis:** Memory is *the* AI bottleneck (capacity, bandwidth, cost). DRAM is a 3-player oligopoly, so startups play in the *fabric and architecture* layer: CXL memory pooling/expansion, processing-in-memory, near-memory compute, and HBM-base-die IP. Strategic-heavy exits.
- **Win:** CXL switching/pooling (Panmnesia, UnifabriX), PIM IP, memory-controller IP. **Lose:** Trying to make DRAM/NAND.
- **Watch:** Panmnesia, XCENA, Majestic Labs, UnifabriX, NEO Semiconductor, MemVerge (software). **Labs:** ETH/Mutlu (PIM), Samsung/SK hynix research. **Acquirers:** SK hynix, Samsung, Micron, Marvell, Astera.
- **Nov 2026 update:** The 2026 memory shortage (HBM4 for Rubin absorbing wafer capacity; DRAM contract prices roughly doubled in 1H26 per TrendForce [TO VERIFY]) makes memory capacity and cost the most acute constraint in the stack. Venture opportunity: memory-dense servers (Majestic Labs, ~$100M), CXL compute-memory (XCENA $135M Series B), High-Bandwidth Flash (the SK hynix + Sandisk HBF spec), and DRAM-stacked inference (d-Matrix Raptor). Upgraded to High.

## 08 — Power Semiconductors & Power Delivery
- **Thesis:** AI racks are going from ~10kW to 100kW+; power delivery, conversion efficiency, and vertical power delivery are first-order datacenter problems. GaN/SiC and high-density point-of-load conversion have real pull and clean M&A exits (Infineon/Renesas/ADI buy here).
- **Win:** Datacenter-grade GaN, integrated lateral/vertical power delivery (Empower), 48V/800V architectures. **Lose:** Commodity discretes vs. Infineon/onsemi scale.
- **Watch:** PowerLattice, C2i, Cambridge GaN Devices, Vertical Semiconductor, Navitas (public), Vicor (public). **Acquirers:** Infineon, Renesas, ADI, TI, Monolithic Power.
- **Nov 2026 update:** ADI agreed to buy Empower Semiconductor for $1.5B cash [CONFIRMED], the clean strategic exit this thesis predicted. 800V DC rack architectures (NVIDIA Kyber-class racks) and in-package/vertical power delivery are the next wave (PowerLattice raised ~$86M per an Oct 2026 Form D). Wolfspeed's Chapter 11 (2025) is a reminder that SiC substrate economics are brutal.

## 09 — Security, Crypto & Confidential Compute
- **Thesis:** Confidential computing for AI (TEEs, GPU confidential compute) and crypto-acceleration (ZK, FHE) are emerging. ZK/FHE hardware is a real bottleneck if those workloads scale; speculative but venture-shaped.
- **Win:** ZK/FHE accelerators (Fabric Cryptography, Cysic), confidential-compute IP. **Lose:** Generic security IP vs. Arm/Synopsys.
- **Watch:** Fabric Cryptography, Cysic, Chain Reaction. **Acquirers:** NVIDIA, Intel, Arm, crypto infra.

## 10 — RF, Wireless & Connectivity
- **Thesis:** Low VC priority for AI-datacenter; mostly incumbent (Qorvo/Skyworks/Broadcom). Selective interest in mmWave/datacenter wireless and advanced packaging RF. Mostly acqui-hire/IP exits.

## 11 — Analog, Mixed-Signal & Timing
- **Thesis:** AI clocking/jitter, high-speed SerDes analog, and precision timing are quietly critical. SiTime proved MEMS timing can be venture-scale. Mostly M&A exits; IP-leverage matters.
- **Watch:** Movellus, Aura Semiconductor, Agile Analog, SiTime (public). **Acquirers:** Renesas, Skyworks, Microchip, Synopsys.

## 12 — EDA, IP & Design Tools
- **Thesis:** AI-for-chip-design is the most capital-efficient AI-infra thesis. Synopsys/Cadence own the stack but AI-native verification, RTL generation, and design-space optimization are a wedge; RISC-V IP disaggregates the incumbent IP model. Fast software-like iteration with strategic acquirers.
- **Win:** AI verification/debug copilots (ChipStack, Silimate, Astrus), RISC-V IP (Codasip, SemiDynamics). **Lose:** Reimplementing place-and-route from scratch.
- **Watch:** Ricursive Intelligence, ChipAgents, Cognichip, ChipStack, Silimate, Bronco AI, Normal Computing, Codasip, SemiDynamics, Quilter. **Acquirers:** Synopsys, Cadence, Siemens EDA, Arm, Qualcomm.
- **Nov 2026 update:** The breakout year for agentic AI-for-chip-design. Ricursive Intelligence (Mirhoseini/Goldie) raised $300M at ~$4B (Jan 2026), ChipAgents expanded its Series A to $134M (Jul 2026), and Cognichip raised $60M (Apr 2026). NVIDIA invested $2B in Synopsys (Dec 2025). The risk is now valuation and incumbent bundling, not adoption.

## 13 — Foundry, Packaging & Chiplet Integration
- **Thesis:** Advanced packaging (CoWoS, hybrid bonding, glass substrate, panel-level) is the new Moore's Law and the actual supply bottleneck for AI. Very capital-intensive; startups win in packaging IP, materials, and novel fab approaches more than in building fabs.
- **Win:** Glass/panel substrates, hybrid-bonding IP, novel litho/fab (Atomic Semi, Substrate). **Lose:** Competing with TSMC on leading-edge logic fabs.
- **Watch:** Substrate, xLight, Lace Lithography, Fab2 (ex-Atomic Semi), Inversion, Chipletz, Eliyan. **Acquirers:** TSMC ecosystem, Amkor, ASE, Intel Foundry, ASML.
- **Nov 2026 update:** "New lithography" became venture-fundable. Substrate (X-ray litho) raised ~$100M at >$1B (Oct 2025). xLight (free-electron-laser EUV source) received up to $150M of US CHIPS equity. Lace Lithography raised a $40M Series A. Atomic Semi rebranded as Fab2 (reported $500M round [UNCONFIRMED]). CoWoS and HBM packaging remain allocation-constrained through 2026.

## 14 — Quantum, Neuromorphic & Non-Von-Neumann
- **Thesis:** Long-horizon, binary-outcome, but the upside is category-defining. Analog/in-memory compute (EnCharge, Sagence) has the nearest commercial path for AI efficiency; quantum (PsiQuantum) is a 5–10 yr moonshot needing patient/strategic capital.
- **Win:** Analog in-memory inference at energy-per-token leadership; fault-tolerant quantum if it arrives. **Lose:** Neuromorphic without a killer app.
- **Watch:** Unconventional AI, EnCharge AI, Sagence, Normal Computing, Extropic, Mythic, PsiQuantum, Quantinuum, QuEra. **Labs:** Princeton/Verma, Stanford. **Investors:** patient/strategic only, plus a new class of mega-seed investors.
- **Nov 2026 update:** Naveen Rao's Unconventional AI raised a ~$475M seed at ~$4.5B [TO VERIFY] and agreed to buy NeuReality (Oct 2026). That shows non-von-Neumann compute can raise frontier-lab-sized capital on founder pedigree alone. Quantum raised record rounds (PsiQuantum ~$1B, Quantinuum ~$600M in 2025 [TO VERIFY]). See [categories/14_quantum_neuromorphic_and_non_von_neumann.md](categories/14_quantum_neuromorphic_and_non_von_neumann.md) for Rain AI and other status changes.

## 15 — Autonomous, Robotics & Automotive Silicon
- **Thesis:** Physical AI (humanoids, autonomy) is the next compute frontier; automotive silicon is a long, design-win-gated game with Tier-1/OEM gatekeepers. Robotics is earlier and more venture-shaped.
- **Watch:** Recogni, Blaize, Hailo, Mobileye (public). **Acquirers:** Qualcomm, NVIDIA, automotive Tier-1s.

## 16 — Datacenter Infrastructure Enablers
- **Thesis:** The "picks and shovels around the chip" — cooling (liquid/immersion), rack power, optical switching, smart NICs, and DC fabric — are a high-conviction way to ride AI capex with less single-chip risk. Strong near-term revenue and M&A.
- **Win:** Liquid/immersion cooling at hyperscale (Submer, ZutaCore), rack-scale power, optical circuit switching. **Lose:** Undifferentiated cooling vs. Vertiv scale.
- **Watch:** Corintis, Accelsius, Frore, LiquidStack, Submer, ZutaCore. **Acquirers:** Vertiv, Schneider, Eaton, Flex, Daikin, hyperscalers.
- **Nov 2026 update:** Large strategics are rolling up liquid cooling (e.g., Eaton–Boyd Thermal, Schneider–Motivair [TO VERIFY]). Racks are heading past 200 kW with 800V DC distribution. Cooling entries in category 16 were not fully re-verified this refresh; prioritize them at the next refresh.

## 17 — Emerging Research-to-Startup Pipeline
- **Thesis:** The sourcing engine. The best Seed/Series A AI-silicon deals are pre-narrative, forming out of a handful of labs (Stanford, Berkeley, MIT, Princeton, ETH, Columbia, UCSB) and hyperscaler/chip-co research teams. Track papers, patents, and people to be first call.
- **Use:** Convert lab/paper/patent/people signals into a ranked outreach list. See [STEALTH_STARTUP_DISCOVERY.md](STEALTH_STARTUP_DISCOVERY.md) and [RESEARCH_AND_RESEARCHERS.md](RESEARCH_AND_RESEARCHERS.md).

---

## Cross-Cutting Theses
1. **Inference > Training for venture risk-adjusted return.** Lower CUDA lock-in, clearer perf/$ story, faster sales cycles.
2. **Sell the bottleneck, not the chip.** Memory bandwidth, interconnect, power, and packaging are where the constraints — and the durable margins — live.
3. **Strategic demand is the real moat.** Sovereign AI and hyperscaler custom-silicon programs de-risk otherwise un-fundable hard-tech.
4. **Software is the silent killer.** Compiler/runtime/ecosystem maturity decides most AI-silicon outcomes; diligence it as hard as the silicon.
5. **Exits are mostly M&A, including licence + acqui-hire.** Underwrite to strategic acquisition by NVIDIA/AMD/Broadcom/Marvell/Qualcomm/Intel/hyperscalers. IPO is the exception, but it is open again (Astera, Cerebras 2026). *(Updated Nov 2026.)*
6. **New (Nov 2026): Model "reverse acquihire" outcomes explicitly.** NVIDIA–Groq and NVIDIA–Enfabrica show that the buyer may take the IP licence and the team while leaving a residual company. Diligence the cap-table waterfall and the employee-retention terms: preferred holders were paid out, but residual-company economics vary. Expect antitrust scrutiny of the structure (a DOJ inquiry into NVIDIA–Groq has been reported [UNCONFIRMED]).
7. **New (Nov 2026): The memory shortage is a tailwind for architecture startups.** Anything that cuts HBM/DRAM bits per token (SRAM-heavy inference, compression, CXL pooling, HBF) has unusually strong pull through 2027.
8. **New (Nov 2026): Valuation discipline.** Seed and Series A rounds of $300–500M at $4B+ (Ricursive, Unconventional AI) and late-stage marks of $5–20B for pre-volume silicon reflect a crowded trade. Prefer bottleneck-adjacent companies with signed capacity contracts.
