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

## I. 2025–2026 Additions (Refresh #3)

> Venue/date details for 2025–2026 items are tagged `[TO VERIFY]` where they could not be re-checked against the publisher this refresh. Company "papers" are disclosures/claims, not peer-reviewed results.

| Paper / Line of Work | Authors / Lab | Year | Why It Matters for VC | Bottleneck | Signal | VC Rel | Conf |
|----------------------|---------------|:----:|------------------------|-----------|--------|:------:|------|
| FlashAttention-4 (Blackwell-targeted attention) | Tri Dao et al. (Princeton/Together) | 2026 | Kernel co-design sets the bar for next-gen inference silicon utilization | Inference cost | Confirmed (Together) | 5 | High |
| AlphaEvolve — LLM-driven algorithm/circuit discovery incl. Verilog rewrite for TPU arithmetic `[TO VERIFY venue]` | Google DeepMind | 2025 | Evidence that agentic LLMs can improve shipped silicon RTL | Design productivity | Likely | 5 | Medium-High |
| Agentic RTL / verification benchmarks (e.g., NVIDIA CVDP) `[TO VERIFY]` | NVIDIA Research / academia | 2025 | Yardsticks for ChipAgents/Ricursive/Cognichip-class claims | Design productivity | Confirmed (category funded) | 4 | Medium |
| Analog optical computer for AI inference & optimization (Nature) `[TO VERIFY]` | Microsoft Research Cambridge | 2025 | Hyperscaler-backed analog-optical compute proof | Compute energy | Watchlist | 4 | Medium |
| Metasurface optical processing unit (Tulkas T100) disclosures | Neurophos (Duke lineage) | 2026 | Million-element optical matrix compute — claims are simulation-based | Compute energy | Confirmed (Neurophos) | 4 | Medium (company claims) |
| Analog in-memory attention for LLMs (Nature Computational Science) `[TO VERIFY]` | Leroux et al. (FZ Jülich) | 2025 | Gain-cell IMC for KV/attention — analog IMC moves into LLM serving | Memory/KV energy | Likely | 4 | Medium |
| High-precision RRAM analog matrix-equation solver (Nature Electronics) `[TO VERIFY]` | Peking University (Zhong Sun et al.) | 2025 | Addresses analog precision — the core objection to analog AI | Energy/op | Watchlist | 3 | Medium |
| HBM4 / custom base-die disclosures (ISSCC 2026) `[TO VERIFY]` | Samsung, SK hynix | 2026 | Logic-in-base-die opens custom-HBM and near-memory compute IP | Memory bandwidth | Watchlist | 4 | Medium |
| Ironwood TPU (inference-first TPU) (Hot Chips 2025) `[TO VERIFY]` | Google | 2025 | Hyperscaler inference-silicon bar; OCS scale-up | Inference cost | Watchlist | 4 | Medium |
| CPO switch silicon — Spectrum-X / Quantum-X Photonics (GTC/Hot Chips/OFC) `[TO VERIFY]` | NVIDIA / TSMC | 2025–2026 | CPO enters production; supply chain (lasers, fiber attach, test) opens to startups | Interconnect | Watchlist | 5 | Medium-High |
| Model-hardwired inference chip (HC1, Llama 3.1 8B; ~2 of ~100 metal layers per model) | Taalas | 2026 | Mask-programmable per-model silicon; tests the "architecture drift" risk | Inference cost | Confirmed (Taalas) | 4 | Medium (company claims) |
| In-chip microfluidic cooling demonstration `[TO VERIFY]` | Microsoft | 2025 | Thermal path for >1kW packages | Thermal | Watchlist | 3 | Medium |
| Fault-tolerant neutral-atom architecture (Nature) `[TO VERIFY]` | Lukin et al. (Harvard/MIT/QuEra) | 2025 | Below-threshold, repeated-QEC neutral-atom milestone | Quantum FT | Likely (QuEra) | 4 | Medium |
| Verifiable quantum advantage — "Quantum Echoes" OTOC (Nature) `[TO VERIFY]` | Google Quantum AI | 2025 | Useful-advantage claim on Willow hardware | Quantum FT | Watchlist | 3 | Medium |

**Conference programs to scan next (pre-formation signal):** ISSCC 2027 advance program (Nov 2026), MICRO 2026 (Oct 2026), Hot Chips 2026 (Aug 2026), ISCA 2026 (Jun 2026), OFC 2026 (Mar 2026), DAC/ICCAD 2026 AI-EDA tracks — prioritize student first-authors on analog/photonic compute, HBM4/PIM, CPO packaging, and agentic EDA. Specific 2026 program papers were not individually verified this refresh `[TO VERIFY]`.

## How to Use
- Track venues: ISSCC, ISCA, MICRO, HotChips, OFC, VLSI Symposia, DAC, ASPLOS, MLSys, SOSP/OSDI, NeurIPS (systems), Nature/Science.
- For each commercially-urgent paper, check: who are the students/postdocs, are there patents, any new-entity assignees, any role changes? Promote to [researcher_to_startup_signal_tracker.md](researcher_to_startup_signal_tracker.md) when signals converge.

## Refresh Notes
| Date | Refresh Type | Added | Updated | Sources |
|------|--------------|-------|---------|---------|
| 2026-06-09 | Full (initial) | 12 | 0 | Public publications, arXiv, conference programs |
| 2026-06-09 | Expansion #2 | 22 | 12 | arXiv, ISSCC/ISCA/MICRO/ASPLOS/SOSP/OFC/Hot Chips, Nature/Science (2023–2025); venues tagged [TO VERIFY] where uncertain |
| 2026-11-04 | Full (Refresh #3) | 14 (section I) | 0 | Company disclosures (Taalas, Neurophos), arXiv (FlashAttention-4), DeepMind/NVIDIA research pages, Nature/Nature-family 2025 [venues TO VERIFY]; data/paper_index.yaml now 38 entries |
