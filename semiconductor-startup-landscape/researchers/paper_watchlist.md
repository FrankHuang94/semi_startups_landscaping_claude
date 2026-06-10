# Paper Watchlist

Breakthrough and commercially-urgent papers (emphasis on 2023–2026) that point toward AI-semiconductor commercialization. Template: [../_templates/paper_entry_template.md](../_templates/paper_entry_template.md). VC Relevance 1–5.

> Inclusion criteria: addresses a binding bottleneck (memory, interconnect, packaging, inference cost, power) and/or has a plausible lab→startup path. Venues/years are best-effort; where a specific venue is uncertain it is tagged `[TO VERIFY]`. Treat as a reading/sourcing list, not citations of record.

## A. Inference Efficiency, Serving & Quantization

| Paper / Line of Work | Authors / Lab | Year | Why It Matters for VC | Bottleneck | Signal | VC Rel | Conf |
|----------------------|---------------|:----:|------------------------|-----------|--------|:------:|------|
| FlashAttention-2 | Tri Dao (Princeton) | 2023 | IO-aware attention; defines what inference silicon must optimize | Inference cost | Likely (Together) | 5 | High |
| FlashAttention-3 | Dao et al. (Princeton/NVIDIA/Together) | 2024 | Hopper-tuned attention; HW-software co-design exemplar | Inference cost | Likely | 5 | High |
| AWQ (activation-aware quant) | Lin, Han et al. (MIT) | 2023 | 4-bit weight quant baseline for serving economics | Inference cost | Likely | 5 | High |
| QServe (W4A8KV4) | Han group (MIT) | 2024 | Quant + system co-design for cheaper GPU serving | Inference cost | Likely | 5 | High |
| StreamingLLM (attention sinks) | Xiao, Han et al. (MIT) | 2023 | Long-context streaming; shapes KV-cache HW needs | Memory/KV | Likely | 4 | High |
| PagedAttention / vLLM | Kwon et al. (UC Berkeley) | 2023 | KV-cache paging now standard; defines memory behavior of serving | Memory/KV | Watchlist | 5 | High |
| SGLang / RadixAttention | Zheng et al. (Stanford/Berkeley) | 2024 | KV reuse for agentic/structured serving | Inference cost | Watchlist | 4 | Medium-High |
| Speculative decoding / Medusa | Cai et al. (Princeton/Together) | 2024 | Throughput technique reshaping accelerator utilization | Inference cost | Watchlist | 4 | Medium-High |
| Quest / KV-cache sparsity | MIT/SJTU | 2024 | Sparse KV access; near-memory/PIM relevance | Memory | Watchlist | 4 | Medium |

## B. Architecture & Systems (industrial silicon disclosures)

| Paper / Line of Work | Authors / Lab | Year | Why It Matters for VC | Bottleneck | Signal | VC Rel | Conf |
|----------------------|---------------|:----:|------------------------|-----------|--------|:------:|------|
| TPU v4 + Optical Circuit Switch | Google (ISCA) | 2023 | OCS scale-up fabric signals where interconnect heads | Interconnect | Watchlist | 5 | High |
| MTIA inference accelerator | Meta (ISCA) | 2023 | Hyperscaler in-house inference silicon; build vs. buy | Inference | Watchlist | 4 | High |
| Microsoft Maia 100 disclosure | Microsoft (Hot Chips) | 2024 | Hyperscaler AI silicon + network/cooling co-design | DC systems | Watchlist | 4 | Medium-High |
| Chiplet Cloud (LLM ASIC cost model) | Univ. of Washington | 2023 | Quantifies when custom LLM ASICs beat GPUs | Custom ASIC econ | Likely | 4 | Medium-High |
| Blackwell / MI300 microarchitecture analyses | NVIDIA / AMD (Hot Chips) | 2024 | Incumbent roadmap = the bar startups must clear | Compute | Watchlist | 4 | Medium |

## C. Memory, CXL & PIM

| Paper / Line of Work | Authors / Lab | Year | Why It Matters for VC | Bottleneck | Signal | VC Rel | Conf |
|----------------------|---------------|:----:|------------------------|-----------|--------|:------:|------|
| Pond (CXL memory pooling) | Microsoft Azure (ASPLOS) | 2023 | Proves CXL pooling TCO at hyperscale | Memory | Likely | 5 | High |
| TPP (transparent page placement) | Meta (ASPLOS) | 2023 | OS tiering for CXL/tiered memory | Memory | Watchlist | 4 | High |
| PIM-for-LLM / real-PIM studies | Mutlu group (ETH) | 2023–2025 | Productizable near-memory for AI workloads | Memory | Likely | 5 | High |
| HBM-PIM / LPDDR-PIM | Samsung / SK hynix (ISSCC) | 2023–2024 | Memory makers productizing PIM | Memory | Watchlist | 4 | High |
| PIM/near-data processing surveys | Mutlu, Ghose et al. | 2023 | Field roadmap; sourcing map for PIM startups | Memory | Likely | 5 | High |

## D. Photonics, Optical Interconnect & Optical Compute

| Paper / Line of Work | Authors / Lab | Year | Why It Matters for VC | Bottleneck | Signal | VC Rel | Conf |
|----------------------|---------------|:----:|------------------------|-----------|--------|:------:|------|
| Energy-efficient DWDM optical interconnect | Bergman (Columbia) | 2023–2025 | Optical fabric scaling for AI clusters | Interconnect | Likely | 5 | High |
| Heterogeneous / QD comb lasers on Si | Bowers (UCSB) | 2023–2025 | Laser integration = the CPO bottleneck | Interconnect | Likely | 5 | High |
| Single-chip photonic deep neural network | Englund et al. (MIT) | 2024 | Optical inference feasibility milestone | Compute energy | Likely | 4 | Medium-High |
| "Taichi" large-scale photonic chiplet | Tsinghua | 2024 | Scaled photonic compute demonstration | Compute | Watchlist | 3 | Medium |
| Lightmatter photonic processor (Passage/compute) | Lightmatter (Nature) | 2025 | Company-backed photonic interconnect/compute proof | Interconnect | Confirmed (Lightmatter) | 5 | Medium-High |
| Optical I/O standardization (UCIe-O / OFC) | Ayar/Berkeley/consortia | 2023–2025 | Standardizes in-package optical I/O | Interconnect | Likely | 5 | High |

## E. Analog / In-Memory / Emerging-Device Compute

| Paper / Line of Work | Authors / Lab | Year | Why It Matters for VC | Bottleneck | Signal | VC Rel | Conf |
|----------------------|---------------|:----:|------------------------|-----------|--------|:------:|------|
| Charge-domain IMC macros | Verma (Princeton) | 2023–2025 | Underpins EnCharge; robust analog compute | Energy/token | Confirmed (EnCharge) | 5 | High |
| IBM analog-AI chip (PCM-based) | IBM Research (Nature) | 2023 | Analog inference at scale demonstration | Energy/token | Watchlist | 4 | Medium-High |
| RRAM compute-in-memory systems | Wong (Stanford) | 2023–2025 | Device→system IMC manufacturability | Energy/token | Likely | 4 | Medium |
| SRAM deep-in-memory (DIMA) | Shanbhag (UIUC) | 2023–2025 | Foundational to IMC startup wave | Energy/op | Likely | 4 | Medium |

## F. AI-for-Chip-Design (EDA)

| Paper / Line of Work | Authors / Lab | Year | Why It Matters for VC | Bottleneck | Signal | VC Rel | Conf |
|----------------------|---------------|:----:|------------------------|-----------|--------|:------:|------|
| AlphaChip (graph placement) + extension | Mirhoseini, Goldie et al. (Google) | 2021 / 2024 | Catalyzed AI-for-physical-design wave | Design productivity | Likely | 5 | High |
| ChipNeMo (domain LLMs for chip design) | NVIDIA Research | 2023–2024 | Validates AI-for-design wedge | Design productivity | Watchlist | 4 | High |
| VerilogEval / RTLLM (LLM-HDL benchmarks) | NVIDIA / academia | 2023–2024 | Benchmarks for generative RTL startups | Design productivity | Likely | 4 | Medium-High |
| ML place-and-route / analog layout automation | Pan (UT Austin) | 2023–2025 | Digital+analog EDA automation | Design productivity | Likely | 4 | Medium-High |

## G. Packaging, Power & Cooling

| Paper / Line of Work | Authors / Lab | Year | Why It Matters for VC | Bottleneck | Signal | VC Rel | Conf |
|----------------------|---------------|:----:|------------------------|-----------|--------|:------:|------|
| Glass-core / panel substrate | Georgia Tech PRC / Intel | 2023–2025 | Next substrate generation for AI | Packaging | Weak | 4 | Medium |
| Hybrid bonding scaling | imec / TSMC | 2023–2025 | 3D stacking yield/pitch roadmap | Packaging | Watchlist | 4 | Medium |
| Heterogeneous integration / SiIF | Iyer (UCLA), Bakir (GT) | 2023–2025 | Chiplet-integration alternatives | Packaging | Likely | 4 | Medium-High |
| In-chip microfluidic cooling | Microsoft / academia | 2024 | Cooling at 100kW+ rack densities | Thermal | Watchlist | 3 | Medium |
| High-density power conversion / GaN | Perreault, Palacios (MIT) | 2023–2025 | Datacenter power-delivery roadmap | Power | Likely | 4 | Medium-High |

## H. Quantum & Cryogenic

| Paper / Line of Work | Authors / Lab | Year | Why It Matters for VC | Bottleneck | Signal | VC Rel | Conf |
|----------------------|---------------|:----:|------------------------|-----------|--------|:------:|------|
| QEC below surface-code threshold ("Willow") | Google Quantum (Nature) | 2024 | Error-correction milestone reviving quantum capital | Quantum FT | Watchlist | 4 | High |
| Logical processor on reconfigurable atom arrays | Lukin et al. (Harvard, Nature) | 2023 | Neutral-atom logical-qubit milestone (QuEra) | Quantum FT | Likely (QuEra) | 4 | High |
| Cryogenic CMOS control ICs | Charbon (EPFL) | 2023–2025 | Scaling layer (picks-and-shovels) for quantum | Quantum control | Likely | 3 | Medium |

## How to Use
- Track venues: ISSCC, ISCA, MICRO, HotChips, OFC, VLSI Symposia, DAC, ASPLOS, MLSys, SOSP/OSDI, NeurIPS (systems), Nature/Science.
- For each commercially-urgent paper, check: who are the students/postdocs, are there patents, any new-entity assignees, any role changes? Promote to [researcher_to_startup_signal_tracker.md](researcher_to_startup_signal_tracker.md) when signals converge.

## Refresh Notes
| Date | Refresh Type | Added | Updated | Sources |
|------|--------------|-------|---------|---------|
| 2026-06-09 | Full (initial) | 12 | 0 | Public publications, arXiv, conference programs |
| 2026-06-09 | Expansion #2 | 22 | 12 | arXiv, ISSCC/ISCA/MICRO/ASPLOS/SOSP/OFC/Hot Chips, Nature/Science (2023–2025); venues tagged [TO VERIFY] where uncertain |
