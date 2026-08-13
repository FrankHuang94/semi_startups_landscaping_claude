# 20 — M&A Tracker

Mergers and acquisitions relevant to AI semiconductor infrastructure. Use for comparables, exit-path planning, and acquirer-behavior signals. All deal values point-in-time and tagged; many semiconductor deals are undisclosed.

> Linked: [21_vc_investor_tracker.md](21_vc_investor_tracker.md) · [23_exit_and_shutdown_tracker.md](23_exit_and_shutdown_tracker.md) · [24_strategic_investor_tracker.md](24_strategic_investor_tracker.md) · [../MARKET_MAP.md](../MARKET_MAP.md)

## Deal Table

| Acquirer | Target | Date Announced | Deal Value | Category | Strategic Rationale | Investors (target) | Return Signal | Source |
|----------|--------|----------------|-----------|----------|---------------------|--------------------|---------------|--------|
| SoftBank | Graphcore | 2024-07 | Undisclosed (~$500M est.) [ESTIMATED] | 01 Training | Own AI compute stack alongside Arm | Sequoia, BMW i, Atomico | Below peak (down round outcome) | Press [TO VERIFY] |
| SoftBank | Ampere Computing | 2025 | ~$6.5B [TO VERIFY] | 04 ASIC/CPU | Arm-server compute for AI | Carlyle, Oracle | Strong | Press [TO VERIFY] |
| AMD | ZT Systems | 2024-08 | ~$4.9B [TO VERIFY] | 16 DC Infra | Rack-scale AI systems integration | — | Strategic | Press [TO VERIFY] |
| AMD | Silo AI | 2024-07 | ~$665M [TO VERIFY] | (software/AI) | AI software/services for silicon | — | Strategic | Press [TO VERIFY] |
| AMD | Untether AI (assets/IP + team) | 2025 | Undisclosed | 02 Inference | At-memory inference IP + talent | Intel Cap, CPPIB, Tracker | Acqui-hire (wind-down) | Press [TO VERIFY] |
| Infineon | GaN Systems | 2023-10 | ~$830M [TO VERIFY] | 08 Power | GaN device portfolio for power | BDC, Fidelity | Strong | Press [CONFIRMED announced] |
| Renesas | Transphorm | 2024 | ~$339M [TO VERIFY] | 08 Power | GaN power capability | KKR, Yaskawa | Solid | Press [TO VERIFY] |
| Snap | GrAI Matter Labs | 2023 | Undisclosed | 03/14 Neuromorphic | Edge/neuromorphic talent | iBionext, 360 | Acqui-hire | Press [TO VERIFY] |
| Flex | JetCool | 2024 | Undisclosed | 16 Cooling | Liquid cooling for AI servers | — | Strategic | Press [TO VERIFY] |
| Sivers Semiconductors | MixComm | 2022 | ~$30M [TO VERIFY] | 10 RF | mmWave beamforming | — | Modest | Press [TO VERIFY] |

## Deal Table — 2025 H2 to 2026 (added 2026-08-13)

The defining development since the last refresh: **the two largest "exits" in AI silicon were not acquisitions.** NVIDIA took the technology and the leadership of both Groq and Enfabrica through non-exclusive licence + hire structures that leave the companies nominally independent — and, in Groq's case, drew a Senate inquiry over whether the structure evades Hart-Scott-Rodino review. Treat licence+hire as a live exit path (and a live comparable) in every inference and interconnect underwriting.

| Acquirer | Target | Date Announced | Deal Value | Category | Strategic Rationale | Investors (target) | Return Signal | Source |
|----------|--------|----------------|-----------|----------|---------------------|--------------------|---------------|--------|
| NVIDIA | Groq (licence + team, **not** an acquisition) | 2025-12 | ~$20B [TO VERIFY] | 02 Inference | Non-exclusive licence to LPU inference tech; CEO Jonathan Ross, President Sunny Madra + senior leaders join NVIDIA | BlackRock, Samsung, Cisco, D1 | Very strong (largest AI-silicon deal on record) | Press [TO VERIFY] |
| NVIDIA | Enfabrica (licence + team) | 2025-09 | >$900M cash+stock [TO VERIFY] | 05 Networking | Licence ACF SuperNIC tech; hire CEO Rochan Sankar + staff; scale-up fabric to ~100k accelerators | Sutter Hill, Atreides, NVIDIA | Strong vs. ~$260M raised | Press [TO VERIFY] |
| Meta | Rivos | 2025-10 | ~$2B [ESTIMATED, reported] | 04 Custom ASIC/RISC-V | Accelerate MTIA; RISC-V inference silicon + team | Matrix, Intel Cap, MediaTek, Dell | Strong vs. ~$250M raised | Press [TO VERIFY] |
| Marvell | Celestial AI | 2025-12 (closed 2026-02-02) | ~$3.25B upfront; up to ~$5.5B with milestones | 06 Optical/CPO | Photonic Fabric for scale-up connectivity | Fidelity, BlackRock, Maverick, AMD Ventures | Strong (~$594M raised) | Press [CONFIRMED announced] |
| Marvell | XConn Technologies | 2026-02 (closed 2026-02-10) | ~$540M [TO VERIFY] | 07 Memory/CXL | CXL/PCIe switch silicon for memory pooling | — | Solid | Press [TO VERIFY] |
| Qualcomm | Alphawave Semi | 2025-06 (closed ~Q4 2025, a quarter early) | ~$2.4B all-cash | 04/05 SerDes & chiplet IP | High-speed connectivity IP for Qualcomm's datacenter push (AI200/AI250); Tony Pialis leads Qualcomm DC business | Public (LSE) | Strong | Press [CONFIRMED] |
| Microchip Technology | Hailo | 2026 | Undisclosed [TO VERIFY] | 03 Edge Inference | Edge NPU portfolio + team at distressed price | Poalim, Gil Agmon, Delek Motors | **Distressed** — valuation fell from ~$1.2B to <$500M | Press [TO VERIFY] |
| IonQ | SkyWater Technology | 2026-01 | ~$1.8B [TO VERIFY] | 13 Foundry | Domestic fab capacity + supply-chain control for quantum | Public (NASDAQ: SKYT) | Strong (public premium) | Press [TO VERIFY] |
| GlobalFoundries | Synopsys ARC Processor IP business | 2026 | Undisclosed [TO VERIFY] | 12 EDA/IP | ARC-V/ARC-Classic/VPX-DSP/NPX NPU IP retargeted at physical AI | — | Carve-out | Press [TO VERIFY] |
| Siemens | Canopus AI | 2026-02 | Undisclosed [TO VERIFY] | 13 Metrology | AI-driven computational metrology for fabs | — | Tuck-in | Press [TO VERIFY] |
| d-Matrix | GigaIO (SuperNODE, FabreX assets) | 2026 | Undisclosed [TO VERIFY] | 02/05 | Rack-scale fabric to sell systems, not chips | — | Startup-buys-startup (consolidation signal) | Press [TO VERIFY] |
| Intel / Qualcomm (reported approaches) | Tenstorrent | 2026 | — | 01/04 | Early-stage takeover conversations reported; nothing agreed | Samsung, Hyundai, Fidelity, AFW | [UNCONFIRMED — rumor] | Press [UNCONFIRMED] |

## Deal Notes (selected)

### NVIDIA → Groq (licence + team, Dec 2025) — the new template
- **Structure:** ~$20B for a **non-exclusive licence** to Groq's LPU inference technology plus the hiring of founder/CEO Jonathan Ross, President Sunny Madra and senior leadership. Groq continues as an independent company under a new CEO (former CFO Simon Edwards) and subsequently raised ~$650M more (June 2026) at a valuation *below* its September 2025 mark. **Rationale:** NVIDIA buying optionality on deterministic, SRAM-resident low-latency inference — the one workload where a GPU's HBM-centric design is structurally disadvantaged. **Regulatory:** Senators Warren and Blumenthal opened an inquiry in March 2026 arguing the reverse-acquihire structure is designed to avoid HSR filing [TO VERIFY current status]. **Investor outcome:** strong on paper; but note the licence proceeds and the residual equity are different assets — diligence *which* one a given cap-table position actually captures.
- **Lesson for VCs:** the incumbent no longer needs to buy the company to neutralize it. Underwrite the licence+hire outcome explicitly: who gets paid, what the remaining company owns, and whether the team that made the technology work is still there.

### NVIDIA → Enfabrica (licence + team, Sep 2025)
- **Background:** >$900M in cash and stock to license Enfabrica's ACF SuperNIC technology and hire CEO Rochan Sankar and staff; the company had raised ~$260M and remains standalone. **Implied category value:** scale-up fabric is strategic enough that NVIDIA will pay ~3.5x invested capital to keep it in-house rather than let it become a competitive rack-level offering. **Lesson:** networking/fabric startups have a shorter and richer path to a liquidity event than compute startups — but the outcome may arrive as a talent+IP transaction, not a control sale.

### Marvell → Celestial AI ($3.25B–$5.5B, closed Feb 2026) + XConn ($540M)
- **Background:** Marvell paid ~$3.25B upfront (up to ~$5.5B on revenue milestones) for Celestial AI's Photonic Fabric, closing 2026-02-02, and $540M for XConn's CXL/PCIe switch silicon eight days later. **Implied category value:** this is the first *clean, large, control* acquisition of a CPO startup — it repriced [06](../categories/06_optical_interconnect_and_cpo.md) as a whole and is the reference comparable for Ayar Labs, Lightmatter, Xscape and OLIX. **Lesson:** in optical interconnect, the exit is real, the acquirer set is short (Marvell, Broadcom, NVIDIA, Cisco, Coherent/Lumentum), and earnout structures carry a large share of the headline number — diligence the milestone schedule, not the press release.

### Microchip → Hailo (2026) — the downside comparable
- **Background:** Hailo raised ~$425M and reached a ~$1.2B valuation with 300+ edge customers, then hit a liquidity wall: a collapsed SPAC, workforce reductions, an emergency shareholder loan (Delek Motors, Jan 2026), a valuation cut to under $500M, and finally a definitive agreement to sell to Microchip. **Why it matters:** edge inference has real design wins and real revenue but multi-year, low-ASP ramps that do not service venture-scale capital. **Lesson:** in [03](../categories/03_edge_inference_chips.md), underwrite the working-capital ramp, not the TOPS/W benchmark; the strategic acquirer will still be there at a distressed price.

### Meta → Rivos (~$2B, Oct 2025)
- **Background:** Meta acquired the RISC-V datacenter startup to accelerate MTIA after in-house silicon progress lagged; Rivos had completed a design and handed it to TSMC. 2026 reporting suggests integration has been rocky. **Implied category value:** hyperscalers will buy a whole silicon team at ~8x invested capital to compress two years off a roadmap. **Lesson:** for [04](../categories/04_custom_asic_and_chiplets.md), the hyperscaler-buys-the-team outcome is now the modal good outcome — but it prices the *team and schedule*, so team cohesion is the asset to diligence.

### SoftBank → Graphcore (2024)
- **Background:** Graphcore (UK IPU pioneer) struggled commercially against NVIDIA; acquired by SoftBank reportedly well below its ~$2.8B peak valuation. **Rationale:** assemble an AI-compute portfolio around Arm. **Technology acquired:** IPU dataflow architecture, UK silicon talent. **Implied category value:** training-chip startups face brutal incumbent economics; "great tech, no ecosystem" is a recurring failure mode. **Investor outcome:** likely a loss/down outcome for late investors. **Lesson for VCs:** in training silicon, software ecosystem + demand anchor matter more than architecture elegance.

### Infineon → GaN Systems (2023)
- **Background:** Infineon acquired GaN Systems to consolidate GaN power leadership. **Rationale:** datacenter/EV power demand for GaN. **Implied category value:** validates [08](../categories/08_power_semiconductors_and_power_delivery.md) — power-semi startups have clean strategic exits to Infineon/Renesas/ADI. **Lesson:** power startups should underwrite to strategic M&A multiples.

### AMD → ZT Systems + Silo AI + Untether IP (2024–25)
- **Background:** AMD assembled systems (ZT), software (Silo AI), and inference IP/talent (Untether) to close the gap with NVIDIA's full-stack. **Implied category value:** acquirers want **systems + software + IP**, not just chips; talent/IP acqui-hires are a real (if modest) exit for inference startups that miss escape velocity. **Lesson:** position for the full-stack acquirer thesis.

## Refresh Notes

| Date | Refresh Type | Deals Added | Deals Updated | Key Changes | Sources |
|------|--------------|-------------|---------------|-------------|---------|
| 2026-06-09 | Full (initial) | 10 | 0 | Initial build; key AI-silicon M&A + rationale notes | Press, company releases [many TO VERIFY] |
| 2026-08-13 | Full refresh | 12 | 0 | Added NVIDIA→Groq (~$20B licence+hire), NVIDIA→Enfabrica (>$900M), Meta→Rivos (~$2B), Marvell→Celestial AI ($3.25–5.5B) and →XConn ($540M), Qualcomm→Alphawave ($2.4B closed), Microchip→Hailo (distressed), IonQ→SkyWater ($1.8B), GF→Synopsys ARC IP, Siemens→Canopus, d-Matrix→GigaIO assets, Tenstorrent approach rumors. New deal notes on the licence+hire structure and the Hailo downside comparable | Company releases, trade press [many TO VERIFY] |
