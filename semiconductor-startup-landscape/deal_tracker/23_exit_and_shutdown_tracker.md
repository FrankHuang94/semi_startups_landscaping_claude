# 23 — Exit & Shutdown Tracker

Companies that were acquired, shut down, pivoted, or became inactive. The most instructive part of the database: each entry carries an investor lesson, a technical lesson, and a category implication.

> Linked: [20_ma_tracker.md](20_ma_tracker.md) · category "Archived" sections.

## Exit / Shutdown Table

| Company | Category | Outcome | Date | What Happened | Investor Lesson | Source |
|---------|----------|---------|------|---------------|-----------------|--------|
| Graphcore | 01 Training | Acquired (SoftBank) | 2024 | Sold below peak after losing the training-ecosystem race | Architecture ≠ ecosystem; CUDA moat is real | Press [TO VERIFY] |
| Untether AI | 02 Inference | Wound down; IP/team → AMD | 2025 | Strong at-memory tech, insufficient commercial traction | Inference needs revenue + software, not just efficiency | Press [TO VERIFY] |
| Habana Labs | 01/02 | Acquired (Intel, 2019) | 2019 | Became Intel Gaudi line | Early exit can beat the long grind | Press [CONFIRMED] |
| GaN Systems | 08 Power | Acquired (Infineon) | 2023 | Strong outcome consolidating GaN | Power-semi exits to incumbents work | Press [CONFIRMED announced] |
| Transphorm | 08 Power | Acquired (Renesas) | 2024 | GaN capability tuck-in | Strategic power M&A is reliable | Press [TO VERIFY] |
| GrAI Matter Labs | 03/14 | Acquired (Snap) | 2023 | Neuromorphic edge talent acqui-hire | Neuromorphic struggles to find paying markets | Press [TO VERIFY] |
| Esperanto Technologies | 01 | Pivoted / scaled back | ~2024 | Stepped back from broad AI silicon | Many-core RISC-V alone wasn't enough | Press [TO VERIFY] |
| JetCool | 16 Cooling | Acquired (Flex) | 2024 | DTC cooling tuck-in | Cooling exits to DC/EMS incumbents | Press [TO VERIFY] |

## Exit / Outcome Table — 2025 H2 to 2026 (added 2026-08-13)

| Company | Category | Outcome | Date | What Happened | Investor Lesson | Source |
|---------|----------|---------|------|---------------|-----------------|--------|
| **Cerebras Systems** | 01 Training | **IPO (NASDAQ: CBRS)** | 2026-05-14 | Priced at $185, raised ~$5.5B at a ~$56B implied valuation; opened ~$350, closed +68% — the largest semiconductor IPO on record | The IPO window for AI silicon reopened for companies with contracted revenue; a demand anchor (OpenAI, >$20B/750MW) is what made it underwritable | Company releases, press [CONFIRMED] |
| **Groq** | 02 Inference | Licence + team → NVIDIA; company continues | 2025-12 | ~$20B non-exclusive licence of LPU tech; founder/CEO and senior leaders joined NVIDIA; Groq re-staffed and raised ~$650M in June 2026 at a *lower* valuation (~$6B vs ~$6.9B) | A record-value "exit" can leave the residual equity worth less than before — know which asset your position holds | Press [TO VERIFY] |
| **Enfabrica** | 05 Networking | Licence + team → NVIDIA; company continues | 2025-09 | >$900M for tech licence + CEO/staff hires against ~$260M raised | Fabric/networking IP monetizes early; the incumbent buys the bottleneck, not the company | Press [TO VERIFY] |
| **Celestial AI** | 06 Optical/CPO | Acquired (Marvell) | closed 2026-02-02 | ~$3.25B upfront, up to ~$5.5B with milestones, on ~$594M raised | The clean control exit in CPO exists — and earnouts carry much of the headline value | Press [CONFIRMED announced] |
| **Rivos** | 04 ASIC/RISC-V | Acquired (Meta) | 2025-10 | ~$2B reported, pre-revenue, design handed to TSMC; integration reportedly difficult afterward | Hyperscalers buy schedule and team; cohesion is the asset, and post-close attrition is the risk | Press [TO VERIFY] |
| **Hailo** | 03 Edge Inference | **Distressed sale (Microchip)** | 2026 | Collapsed SPAC → layoffs → emergency loan (Jan 2026) → valuation cut from ~$1.2B to <$500M → definitive agreement to sell | Design wins ≠ cash flow. Edge silicon ramps are long and low-ASP; underwrite working capital, not benchmarks | Press [TO VERIFY] |
| **XConn Technologies** | 07 Memory/CXL | Acquired (Marvell) | 2026-02 | ~$540M for CXL/PCIe switch silicon | CXL finally produced a real exit — via switching silicon, not memory-pooling appliances | Press [TO VERIFY] |
| **Alphawave Semi** | 04/05 IP | Acquired (Qualcomm) | closed ~Q4 2025 | $2.4B all-cash; CEO now runs Qualcomm's datacenter business | Connectivity IP is the entry ticket incumbents buy when they decide to enter the datacenter | Press [CONFIRMED] |
| **SkyWater Technology** | 13 Foundry | Acquired (IonQ) | 2026-01 | ~$1.8B — a quantum company buying a US foundry | Vertical integration is flowing *upstream* now; specialty fab capacity is strategic | Press [TO VERIFY] |
| **GigaIO** | 05/16 Fabric | Assets acquired (d-Matrix) | 2026 | SuperNODE and FabreX assets sold to an inference startup | Startup-to-startup asset sales are a viable soft landing as chip startups become systems companies | Press [TO VERIFY] |

## Selected Post-Mortems

### Graphcore (Training)
- **What happened:** UK IPU pioneer raised ~$700M at a ~$2.8B peak, but couldn't build a CUDA-class software ecosystem or win durable demand; acquired by SoftBank at a steep discount. **Why it matters:** the canonical training-silicon cautionary tale. **Investor lesson:** in training, underwrite software + demand anchor, not just FLOPS/architecture. **Technical lesson:** novel architectures impose a compiler/ecosystem tax that can exceed the hardware advantage. **Category implication:** [01](../categories/01_training_accelerators.md) is the hardest category; require a captive demand anchor.

### Untether AI (Inference)
- **What happened:** at-memory compute pioneer with strong perf/W; despite credible technology, commercial traction lagged and the company wound down, with IP/talent going to AMD (2025). **Investor lesson:** efficiency leadership without revenue and software is not a business. **Technical lesson:** at-memory/analog-adjacent approaches need a mature software stack to convert benchmark wins into design wins. **Category implication:** validates the [02](../categories/02_inference_accelerators.md) thesis that software + multi-customer revenue gate outcomes; acqui-hire is the floor, not the goal.

### Hailo (Edge Inference) — added 2026-08-13
- **What happened:** ~$425M raised, unicorn valuation, 300+ customers, credible silicon (26 TOPS at ~2.5W without external memory) — and none of it produced enough cash. A SPAC route to liquidity collapsed, layoffs followed, a shareholder had to extend an emergency loan at ~1.5%/month in January 2026, the valuation fell to under $500M, and Microchip bought the company. **Investor lesson:** in edge silicon, revenue quality dominates revenue growth — long design-in cycles, low ASPs and customer-funded NRE consume working capital faster than the P&L suggests. **Technical lesson:** perf/W leadership is not a moat when the customer's decision is driven by tools, longevity guarantees and supply assurance, which favor incumbents like Microchip, NXP and Renesas. **Category implication:** [03](../categories/03_edge_inference_chips.md) should be underwritten to a strategic-tuck-in exit at 1–3x invested capital, not to a venture-scale independent outcome — Axelera's >$250M round in the same quarter is the exception that proves how much capital the ramp actually needs.

### Cerebras (Training) — the upside case, added 2026-08-13
- **What happened:** the same company the initial build listed as "pre-IPO with customer-concentration risk" went public on 2026-05-14 in the largest semiconductor IPO on record (~$5.5B raised, ~$56B implied), after converting the G42 concentration problem into a bigger one of a different kind: a >$20B, 750MW multi-year OpenAI contract announced in January 2026. **Investor lesson:** in training silicon, the anchor customer is simultaneously the risk and the entire thesis — the market paid for contracted revenue, not architecture. **Technical lesson:** wafer-scale economics held up well enough at volume to fund a public listing; the SRAM-bandwidth advantage found its market in *fast inference*, not training. **Open question for the next refresh:** whether concentration (one customer ≈ 23x annual core revenue in contracted value) survives contact with the public market's expectations.

### Pattern Summary (for IC discussions)
- **Failure modes:** (1) ecosystem/software gap, (2) demand concentration/absence, (3) capital intensity outrunning traction, (4) market mistimed (neuromorphic), (5) **liquidity mistiming** — a real business that runs out of runway between design win and revenue (Hailo).
- **Success modes:** clean strategic fit (power → Infineon/Renesas; CPO → Marvell), escaping to public scale (Astera 2024, **Cerebras 2026**), the hyperscaler team-buy (Rivos → Meta), and the **licence + hire** structure (Groq, Enfabrica → NVIDIA).
- **The 2026 addition:** the licence+hire outcome now sits between M&A and failure and is the highest-value structure observed to date (~$20B). It transfers technology and leadership while leaving a funded shell that must re-staff and re-price. When modeling it, separate three things: proceeds to the company, proceeds/retention to the team, and the value of what remains.
- **Underwriting rule (updated):** for hard-tech silicon, the base case remains strategic M&A with a credible acquirer; but the acquirer list should now include the *licensor* case (NVIDIA), the *hyperscaler team-buy* case (Meta, Google, Microsoft, Amazon), and the distressed-tuck-in floor (Microchip/Hailo). Size losses to the floor, not to the average.

## Refresh Notes

| Date | Refresh Type | Added | Updated | Key Changes | Sources |
|------|--------------|-------|---------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | Initial build; exits/shutdowns + post-mortems | Press [many TO VERIFY] |
| 2026-08-13 | Full refresh | 10 | 2 (Cerebras, Groq status) | Added the 2025 H2–2026 outcome table (Cerebras IPO, Groq/Enfabrica licence+hire, Celestial→Marvell, Rivos→Meta, Hailo distressed sale, XConn, Alphawave, SkyWater, GigaIO). New post-mortems for Hailo and Cerebras; pattern summary now includes liquidity mistiming and the licence+hire structure | Company releases, trade press [many TO VERIFY] |
