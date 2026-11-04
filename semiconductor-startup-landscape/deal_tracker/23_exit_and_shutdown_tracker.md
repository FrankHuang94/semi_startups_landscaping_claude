# 23 — Exit & Shutdown Tracker

Companies that were acquired, shut down, pivoted, or became inactive. The most instructive part of the database: each entry carries an investor lesson, a technical lesson, and a category implication.

> **Last updated:** 2026-11-04 (Refresh #3). Outcome vocabulary: Acquired · Licensed + acqui-hired (target survives as a shell/independent company) · Team acqui-hired (company wound down) · Public (IPO) · Pending acquisition · Shut Down · Pivoted. Rows newest-first.

> Linked: [20_ma_tracker.md](20_ma_tracker.md) · [22_funding_round_tracker.md](22_funding_round_tracker.md) · category "Archived" sections.

## Exit / Shutdown Table

| Company | Category | Outcome | Date | What Happened | Investor Lesson | Source |
|---------|----------|---------|------|---------------|-----------------|--------|
| NeuReality | 02 Inference | Pending acquisition (Unconventional AI) | Announced 2026-10-26; close expected Q4 2026 | Israeli inference-server/NIC-offload startup (~$105M raised [TO VERIFY]) sold for undisclosed cash + stock; ~40 staff join | Sub-scale inference startups now exit to better-funded 2025-vintage peers, not just incumbents | Reuters [CONFIRMED]; CTech (close timing) [TO VERIFY] |
| Hailo | 03 Edge Inference | Acquired (Microchip) | Announced 2026-07; closed 2026-09-21 | Edge NPU leader (Hailo-8/10/15, 100+ customers) sold for undisclosed, "not material" sum; investor write-downs reported (Calcalist) | Edge-AI standalone scale is hard vs. integrated MCU/SoC vendors; exit ≈ strategic tuck-in | Microchip PR; DCD [CONFIRMED] |
| GigaIO (data center business) | 05 Interconnect / 16 Systems | Carve-out acquired (d-Matrix) | 2026-04-02 | SuperNODE + FabreX PCIe memory-fabric business and Carlsbad team sold; GigaIO continues as edge company | Systems/fabric assets are valuable to chip startups going rack-scale | d-Matrix PR [CONFIRMED] |
| Cerebras Systems | 01 Training / 02 Inference | **Public (Nasdaq: CBRS)** | IPO priced 2026-05-13; trading 2026-05-14 | After withdrawing its first IPO filing in Oct 2025 [TO VERIFY] and raising $1.1B (Series G, ~$8.1B) and $1B (Series H, ~$23B), refiled 2026-04-17 and raised $5.55B at $185/sh (~$56.4B fully diluted); >20× oversubscribed; opened ~$350 (one source: $385) [UNCONFIRMED open] | Inference-cloud revenue + sovereign/hyperscale anchors turned a stalled IPO into 2026's largest US IPO — public markets will pay for AI-compute revenue scale | Reuters; SiliconANGLE; IPOScoop [CONFIRMED] |
| Celestial AI | 06 Optical/CPO | Acquired (Marvell) | Announced 2025-12; closed ~2026-02-02 | Photonic Fabric optical scale-up interconnect; ~$3.25B upfront + earn-out [TO VERIFY] | Optical I/O is a strategic multi-billion category; custom-silicon houses are natural buyers | Marvell IR [CONFIRMED close] |
| SambaNova Systems | 01 Training/Inference | Acquisition talks failed → minority strategic investment | Talks late 2025; Series E 2026-02-24 | Intel pursued an acquisition (~$1.6B reported) that stalled; Intel instead joined a $350M Series E + collaboration | Legacy 2021 valuation overhang can block exits; failed M&A ≠ failure | Intel/SambaNova announcements [CONFIRMED]; deal price [TO VERIFY] |
| Groq | 02 Inference | **Licensed + acqui-hired (NVIDIA)**; company continues | 2025-12-24 | Non-exclusive license of LPU tech; founder/CEO Jonathan Ross, president Sunny Madra and core engineers joined NVIDIA; ~$20B reported (CNBC); Groq continues under CEO Simon Edwards with GroqCloud | Reverse-acquihire is now a top-tier exit path; diligence how license proceeds reach shareholders | Groq/NVIDIA statements; CNBC [CONFIRMED structure; value TO VERIFY] |
| Alphawave Semi | 05 Interconnect / 04 Chiplets | Acquired (Qualcomm) | Closed 2025-12-18 | ~$2.4B; SerDes/chiplet IP becomes core of Qualcomm data-center unit | Connectivity IP is a scarce strategic asset | Qualcomm PR [CONFIRMED] |
| Ampere Computing | 04 ASIC/CPU | Acquired (SoftBank) | Closed 2025-11-25 | $6.5B; Arm-server CPU maker joins SoftBank AI-compute portfolio | PE/strategic-owned silicon (Carlyle/Oracle) can exit at strong values to platform consolidators | Bloomberg; SoftBank [CONFIRMED] |
| Kinara | 03 Edge Inference | Acquired (NXP) | Closed 2025-10-27 | $307M cash for discrete edge NPUs | Edge-AI exits cluster in the $200–500M band | NXP PR [CONFIRMED] |
| DreamBig Semiconductor | 05 Networking | Acquired (Arm) — closing [TO VERIFY] | Agreed 2025-10 | ~$265M cash for AI-SuperNIC/chiplet networking | Early chiplet/networking IP can sell to IP-licensors moving into silicon | Arm 6-K [CONFIRMED agreement] |
| Rivos | 04 Custom ASIC/RISC-V | Acquired (Meta) | 2025-09-30 (reported); completed later in 2025 | RISC-V AI-inference team folded into Meta MTIA; terms undisclosed (>$850M estimate [UNCONFIRMED]) | Anchor-customer relationship with a hyperscaler is the best acquisition precursor | Reuters; Bloomberg [CONFIRMED] |
| Enfabrica | 05 Networking | **Licensed + acqui-hired (NVIDIA)** | 2025-09 | >$900M cash + stock (CNBC) for tech license + CEO Rochan Sankar and staff | ~1.5× last post-money in under 2 years; NVIDIA prefers license+hire over acquisitions | CNBC via DCD/Tom's Hardware [CONFIRMED structure; value TO VERIFY] |
| Untether AI | 02 Inference | Team acqui-hired (AMD); company wound down | 2025-06-05 | AMD hired the entire engineering team; speedAI processors and imAIgine SDK no longer supplied or supported | Inference needs revenue + software, not just efficiency | Untether announcement; Tom's Hardware [CONFIRMED] |
| Brium | 12 EDA/AI software | Acquired (AMD) | 2025-06 | AI inference-software optimization for ROCm | Software tuck-ins accompany silicon roadmaps | DCD [CONFIRMED] |
| Enosemi | 06 Optical/CPO | Acquired (AMD) | 2025-05 | Silicon-photonics team for rack-scale Instinct | Small photonics teams have strategic exit options | AMD [CONFIRMED] |
| Graphcore | 01 Training | Acquired (SoftBank) | 2024 | Sold below peak after losing the training-ecosystem race | Architecture ≠ ecosystem; CUDA moat is real | Press [TO VERIFY] |
| Habana Labs | 01/02 | Acquired (Intel, 2019) | 2019 | Became Intel Gaudi line | Early exit can beat the long grind | Press [CONFIRMED] |
| GaN Systems | 08 Power | Acquired (Infineon) | 2023 | Strong outcome consolidating GaN | Power-semi exits to incumbents work | Press [CONFIRMED announced] |
| Transphorm | 08 Power | Acquired (Renesas) | 2024 | GaN capability tuck-in | Strategic power M&A is reliable | Press [TO VERIFY] |
| GrAI Matter Labs | 03/14 | Acquired (Snap) | 2023 | Neuromorphic edge talent acqui-hire | Neuromorphic struggles to find paying markets | Press [TO VERIFY] |
| Esperanto Technologies | 01 | Pivoted / scaled back | ~2024 | Stepped back from broad AI silicon | Many-core RISC-V alone wasn't enough | Press [TO VERIFY] |
| JetCool | 16 Cooling | Acquired (Flex) | 2024 | DTC cooling tuck-in | Cooling exits to DC/EMS incumbents | Press [TO VERIFY] |

**Watchlist (not yet exits):** Groq post-license shell (independence/strategy under new CEO); Lightmatter (aggregator claims of an S-1 filing in 2026 — unverified [UNCONFIRMED]); Rebellions and FuriosaAI (Korean pre-IPO candidates [TO VERIFY]); Etched (rapid valuation step-ups ahead of published revenue).

## Selected Post-Mortems

### Graphcore (Training)
- **What happened:** UK IPU pioneer raised ~$700M at a ~$2.8B peak, but couldn't build a CUDA-class software ecosystem or win durable demand; acquired by SoftBank at a steep discount. **Why it matters:** the canonical training-silicon cautionary tale. **Investor lesson:** in training, underwrite software + demand anchor, not just FLOPS/architecture. **Technical lesson:** novel architectures impose a compiler/ecosystem tax that can exceed the hardware advantage. **Category implication:** [01](../categories/01_training_accelerators.md) is the hardest category; require a captive demand anchor.

### Untether AI (Inference)
- **What happened:** at-memory compute pioneer with strong perf/W; despite credible technology, commercial traction lagged. On 2025-06-05 AMD hired the entire engineering team (not the company), and Untether stopped supplying and supporting speedAI / imAIgine [CONFIRMED]. **Investor lesson:** efficiency leadership without revenue and software is not a business. **Technical lesson:** at-memory/analog-adjacent approaches need a mature software stack to convert benchmark wins into design wins. **Category implication:** validates the [02](../categories/02_inference_accelerators.md) thesis that software + multi-customer revenue gate outcomes; acqui-hire is the floor, not the goal.

### Groq & Enfabrica (Licensed + acqui-hired by NVIDIA)
- **What happened:** NVIDIA licensed each company's technology non-exclusively and hired founders/core engineers (Enfabrica Sept 2025, >$900M reported; Groq Dec 2025, ~$20B reported) instead of acquiring the companies. **Investor lesson:** these structures can deliver acquisition-like value quickly and sidestep merger review, but leave a founder-less operating company; protective provisions, proceeds waterfall and retention of non-moving staff become central. **Technical lesson:** SRAM-centric deterministic inference (Groq) and memory-fabric NICs (Enfabrica) were valuable enough to NVIDIA to pay up rather than out-engineer. **Category implication:** in [02](../categories/02_inference_accelerators.md) and [05](../categories/05_networking_and_interconnect.md), the highest-value exit may be to the incumbent being challenged.

### Hailo (Edge inference)
- **What happened:** one of the best-funded edge-AI chip startups (100+ customers) sold to Microchip for an undisclosed, "not material" amount amid reported investor write-downs. **Investor lesson:** customer count ≠ revenue scale; edge-AI silicon gets absorbed into MCU/SoC portfolios. **Category implication:** [03](../categories/03_edge_inference_chips.md) exit values cluster well below datacenter AI.

### Cerebras (IPO)
- **What happened:** wafer-scale pioneer withdrew its first IPO filing (Oct 2025) [TO VERIFY] amid CFIUS/customer-concentration questions [TO VERIFY], raised $2.1B privately in five months, then completed 2026's largest US IPO. **Investor lesson:** inference-as-a-service revenue converted a hardware story into a public-market growth story. **Category implication:** a public comp now exists for AI-compute startups (valuation benchmarking for Groq, Etched, Tenstorrent, SambaNova).

### Pattern Summary (for IC discussions)
- **Failure modes:** (1) ecosystem/software gap, (2) demand concentration/absence, (3) capital intensity outrunning traction, (4) market mistimed (neuromorphic), (5) edge-AI commoditization by integrated SoCs. **Success modes:** clean strategic fit (power → Infineon/Renesas; optical → Marvell; connectivity → Qualcomm), license+acqui-hire by the incumbent (NVIDIA), or escaping to public scale (Astera, Cerebras 2026 IPO). **Underwriting rule:** for hard-tech silicon, the base case should be strategic M&A with a credible acquirer; size losses accordingly — but 2025–26 shows the right tail (Groq ~$20B, Cerebras IPO) is fatter than assumed for inference compute with real revenue.

## Refresh Notes

| Date | Refresh Type | Added | Updated | Key Changes | Sources |
|------|--------------|-------|---------|-------------|---------|
| 2026-11-04 | Full (Refresh #3) | 14 | 1 | Added Cerebras IPO (May 2026), Groq & Enfabrica (licensed+acqui-hired by NVIDIA), Celestial AI→Marvell, Rivos→Meta, Hailo→Microchip, Kinara→NXP, Ampere→SoftBank, Alphawave→Qualcomm, DreamBig→Arm, GigaIO DC unit→d-Matrix, NeuReality→Unconventional AI (pending), Enosemi & Brium→AMD, SambaNova (failed Intel talks). Corrected Untether AI (team hire 2025-06-05, product support ended). New post-mortems (Groq/Enfabrica, Hailo, Cerebras), watchlist, expanded pattern summary | Reuters, Bloomberg, CNBC, company PRs (Marvell, Qualcomm, NXP, Microchip, d-Matrix), Arm 6-K, Tom's Hardware, DCD |
| 2026-06-09 | Full (initial) | 8 | 0 | Initial build; exits/shutdowns + post-mortems | Press [many TO VERIFY] |
