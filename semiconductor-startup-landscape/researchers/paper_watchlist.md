# Paper Watchlist

Breakthrough and commercially-urgent papers that point toward AI-semiconductor commercialization. Template: [../_templates/paper_entry_template.md](../_templates/paper_entry_template.md). VC Relevance 1–5.

> Inclusion criteria: addresses a binding bottleneck (memory, interconnect, packaging, inference cost, power) and/or has a plausible lab→startup path.

| Paper / Line of Work | Authors / Lab | Area | Why It Matters for VC | Bottleneck | Signal | VC Rel | Confidence |
|----------------------|---------------|------|------------------------|-----------|--------|:------:|------------|
| FlashAttention (1/2/3) | Tri Dao et al. (Stanford/Princeton) | Inference kernels | Reshapes what inference silicon must optimize (IO-aware attention) | Inference cost | Likely (Together) | 5 | High |
| Mamba / SSMs | Gu, Dao (Princeton/CMU) | Architectures | If SSMs displace transformers, transformer-hardwired ASICs ([Etched](../categories/02_inference_accelerators.md)) face risk | Architecture drift | Watchlist | 5 | High |
| AWQ / SmoothQuant | Song Han et al. (MIT) | Quantization | Defines low-precision serving economics | Inference cost | Likely | 5 | High |
| Eyeriss | Sze, Chen (MIT) | Efficient HW | Canonical energy-efficient dataflow for edge/DC | Energy/op | Watchlist | 4 | High |
| Charge-domain IMC | Verma et al. (Princeton) | Analog IMC | Underpins EnCharge; robust analog compute | Energy/token | Confirmed (EnCharge) | 5 | High |
| PIM / near-data processing surveys | Mutlu et al. (ETH) | PIM | Roadmap for productizable near-memory | Memory | Likely | 5 | High |
| Photonic fabric / DWDM interconnect | Bergman et al. (Columbia) | Photonics | Optical-fabric scaling for AI clusters | Interconnect | Likely | 5 | High |
| Heterogeneous/QD lasers on Si | Bowers et al. (UCSB) | Photonics | Laser integration = CPO bottleneck | Interconnect | Likely | 5 | High |
| ChipNeMo / LLMs for chip design | NVIDIA Research | AI-EDA | Validates AI-for-design wedge | Design productivity | Watchlist | 4 | High |
| HBM-PIM | Samsung/SK hynix research | Memory | Productizing PIM in HBM/LPDDR | Memory | Watchlist | 4 | High |
| Glass-core substrate work | Georgia Tech PRC / Intel | Packaging | Next substrate generation for AI | Packaging | Weak | 4 | Medium |
| Optical I/O standardization (UCIe-O) | Ayar/Berkeley/consortia | Photonics | Standardizes in-package optical I/O | Interconnect | Likely | 5 | High |

## How to Use
- Track venues: ISSCC, ISCA, MICRO, HotChips, OFC, VLSI Symposia, DAC, MLSys, NeurIPS (systems).
- For each commercially-urgent paper, check: who are the students/postdocs, are there patents, any new-entity assignees, any role changes? Promote to [researcher_to_startup_signal_tracker.md](researcher_to_startup_signal_tracker.md) when signals converge.

## Refresh Notes
| Date | Refresh Type | Added | Updated | Sources |
|------|--------------|-------|---------|---------|
| 2026-06-09 | Full (initial) | 12 | 0 | Public publications, arXiv, conference programs |
