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

## Selected Post-Mortems

### Graphcore (Training)
- **What happened:** UK IPU pioneer raised ~$700M at a ~$2.8B peak, but couldn't build a CUDA-class software ecosystem or win durable demand; acquired by SoftBank at a steep discount. **Why it matters:** the canonical training-silicon cautionary tale. **Investor lesson:** in training, underwrite software + demand anchor, not just FLOPS/architecture. **Technical lesson:** novel architectures impose a compiler/ecosystem tax that can exceed the hardware advantage. **Category implication:** [01](../categories/01_training_accelerators.md) is the hardest category; require a captive demand anchor.

### Untether AI (Inference)
- **What happened:** at-memory compute pioneer with strong perf/W; despite credible technology, commercial traction lagged and the company wound down, with IP/talent going to AMD (2025). **Investor lesson:** efficiency leadership without revenue and software is not a business. **Technical lesson:** at-memory/analog-adjacent approaches need a mature software stack to convert benchmark wins into design wins. **Category implication:** validates the [02](../categories/02_inference_accelerators.md) thesis that software + multi-customer revenue gate outcomes; acqui-hire is the floor, not the goal.

### Pattern Summary (for IC discussions)
- **Failure modes:** (1) ecosystem/software gap, (2) demand concentration/absence, (3) capital intensity outrunning traction, (4) market mistimed (neuromorphic). **Success modes:** clean strategic fit (power → Infineon/Renesas), or escaping to public scale (Astera, Cerebras path). **Underwriting rule:** for hard-tech silicon, the base case should be strategic M&A with a credible acquirer; size losses accordingly.

## Refresh Notes

| Date | Refresh Type | Added | Updated | Key Changes | Sources |
|------|--------------|-------|---------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | Initial build; exits/shutdowns + post-mortems | Press [many TO VERIFY] |
