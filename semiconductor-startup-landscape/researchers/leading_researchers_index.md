# Leading Researchers Index

Profiles of leading academic and industry researchers whose work is most relevant to future AI-semiconductor company formation. **Public, professional information only.** VC Relevance Score 1–5. See framework in [../RESEARCH_AND_RESEARCHERS.md](../RESEARCH_AND_RESEARCHERS.md).

> We do not assert any researcher is forming a company without public evidence. "Startup Signal Level" reflects public signals only. Affiliations are point-in-time and may carry joint academic/industry roles — verify each refresh.

## Domain Navigation
- [A. Accelerator Architecture & Systems](#a-accelerator-architecture--systems)
- [B. Efficient ML / Inference Hardware-Software Co-design](#b-efficient-ml--inference-hardware-software-co-design)
- [C. Memory, PIM & Near-Memory](#c-memory-pim--near-memory)
- [D. Interconnect & Networking](#d-interconnect--networking)
- [E. Silicon Photonics & Optical Computing](#e-silicon-photonics--optical-computing)
- [F. Analog / In-Memory / Emerging-Device Compute](#f-analog--in-memory--emerging-device-compute)
- [G. EDA & AI-for-Chip-Design](#g-eda--ai-for-chip-design)
- [H. Packaging & 3D Integration](#h-packaging--3d-integration)
- [I. Power Electronics & Delivery](#i-power-electronics--delivery)
- [J. Quantum & Cryogenic Hardware](#j-quantum--cryogenic-hardware)

---

## A. Accelerator Architecture & Systems

### Bill Dally
- **Institution / Role:** Stanford (Professor) / NVIDIA (Chief Scientist & SVP Research)
- **Research Areas:** Accelerator architecture, interconnect, efficient deep learning hardware
- **Why VC Should Track:** Defines the GPU/accelerator state of the art; his group and NVIDIA Research are a primary talent source for founders. Reading his work forecasts where incumbents go next.
- **Recent/Relevant Work:** Large body in ISCA/MICRO/HotChips (efficient inference, sparsity, on-chip interconnect); NVIDIA Hopper/Blackwell-era research talks. **Patents:** High. **Prior Startups:** Stream Processors, Velio.
- **Startup Signal:** Watchlist Only · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### David Patterson
- **Institution / Role:** UC Berkeley (Emeritus) / Google (TPU)
- **Research Areas:** RISC-V, domain-specific architectures, TPU
- **Why VC Should Track:** Father of RISC + RISC-V; the DSA thesis underpins the custom-silicon boom; Berkeley lineage seeds many silicon founders.
- **Recent/Relevant Work:** "A New Golden Age for Computer Architecture"; TPU v4/v5 datacenter papers (incl. ISCA 2023 TPUv4 + OCS). **Startup Signal:** Watchlist · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Krste Asanović
- **Institution / Role:** UC Berkeley (Professor) / SiFive (co-founder, Chief Architect)
- **Research Areas:** RISC-V, vector/parallel architectures, agile hardware (Chipyard)
- **Why VC Should Track:** Co-created RISC-V; SiFive proves the academic→IP path; Berkeley ADEPT/SLICE alumni are prime founder candidates ([04](../categories/04_custom_asic_and_chiplets.md)/[12](../categories/12_eda_ip_and_design_tools.md)).
- **Prior Startups:** SiFive (Confirmed). **Startup Signal:** Confirmed (SiFive) · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Yakun Sophia Shao
- **Institution / Role:** UC Berkeley (Assistant Professor); ex-NVIDIA Research
- **Research Areas:** Accelerator design automation, deep-learning accelerators, chiplet/SoC architecture
- **Why VC Should Track:** Leading next-gen architecture academic bridging accelerators and design automation (Gemmini/Chipyard ecosystem, accelerator generators); trains highly recruitable systems-architecture talent.
- **Recent/Relevant Work:** Accelerator-design and chiplet-architecture papers (ISCA/MICRO 2023–2025); NVIDIA Research lineage (MAGNet). **Startup Signal:** Likely Startup Signal · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Joel Emer
- **Institution / Role:** MIT (Professor of the Practice) / NVIDIA (Senior Distinguished Research Scientist)
- **Research Areas:** Accelerator modeling/evaluation (Timeloop/Accelergy), sparse tensor accelerators, Eyeriss
- **Why VC Should Track:** Co-defined the field's methodology for accelerator design-space exploration; tools and students feed the inference-silicon ecosystem.
- **Recent/Relevant Work:** Sparse-tensor accelerator + design-space frameworks (with Sze; ISCA/MICRO 2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 4 · **Confidence:** High · **Last updated:** 2026-06-09

### Tushar Krishna
- **Institution / Role:** Georgia Tech (Associate Professor)
- **Research Areas:** On-chip/scale-up interconnect for ML, collective communication, NoC, ASTRA-sim, MAERI
- **Why VC Should Track:** Among the few academics focused squarely on the #2 bottleneck (interconnect/collectives) for large-model training; work informs networking/fabric startups ([05](../categories/05_networking_and_interconnect.md)).
- **Recent/Relevant Work:** ASTRA-sim distributed-training network modeling; collective-comms acceleration (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Daniel Sanchez
- **Institution / Role:** MIT (Professor)
- **Research Areas:** Scalable architectures, memory hierarchies, sparse/graph acceleration
- **Why VC Should Track:** Deep work on data-movement-centric and sparse acceleration — directly relevant to inference-efficiency and memory-bound workloads.
- **Recent/Relevant Work:** Sparse tensor-algebra accelerators, cache/memory-hierarchy architectures (ISCA/MICRO/ASPLOS 2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Hadi Esmaeilzadeh
- **Institution / Role:** UC San Diego (Professor)
- **Research Areas:** Accelerators, approximate/efficient computing, near-data acceleration, ML serving systems
- **Why VC Should Track:** Prolific accelerator researcher with a commercialization bent; relevant to inference + near-data startups.
- **Recent/Relevant Work:** Generative-inference acceleration and serving-systems papers (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium · **Last updated:** 2026-06-09

### David Brooks & Gu-Yeon Wei
- **Institution / Role:** Harvard (Professors)
- **Research Areas:** Energy-efficient architecture, accelerator SoCs, edge ML systems, hardware-aware ML
- **Why VC Should Track:** Long-running architecture+circuits duo producing edge/efficient-accelerator talent and open platforms.
- **Recent/Relevant Work:** Edge-AI SoC and accelerator co-design (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 3 · **Confidence:** Medium · **Last updated:** 2026-06-09

### Kunle Olukotun
- **Institution / Role:** Stanford (Professor) / SambaNova (co-founder, Chief Technologist)
- **Research Areas:** Reconfigurable dataflow architectures (Plasticine/RDA), parallel computing
- **Why VC Should Track:** Confirmed academic→startup (SambaNova); dataflow lineage; group seeds reconfigurable-compute founders.
- **Prior Startups:** Afara Websystems, SambaNova (Confirmed). **2026 status:** SambaNova raised a ~$1B Series F first close at ~$11B post-money in July 2026 led by General Atlantic, repositioned around enterprise and agentic inference. **Startup Signal:** Confirmed · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-08-13

### Mark Horowitz
- **Institution / Role:** Stanford (Professor)
- **Research Areas:** Digital/mixed-signal circuits, agile hardware design, energy-efficient systems
- **Why VC Should Track:** Foundational circuits + agile-design researcher (Rambus co-founder lineage); trains circuit/architecture founders.
- **Prior Startups:** Rambus (co-founder). **Startup Signal:** Confirmed (legacy) · **VC Relevance:** 4 · **Confidence:** High · **Last updated:** 2026-06-09

---

## B. Efficient ML / Inference Hardware-Software Co-design

### Song Han
- **Institution / Role:** MIT (Associate Professor) / NVIDIA (Distinguished Scientist)
- **Research Areas:** Model compression, quantization (AWQ/SmoothQuant), efficient LLM serving, TinyML
- **Why VC Should Track:** His techniques define inference-efficiency economics; founded OmniML (acquired by NVIDIA) — the lab→startup→strategic path. A founder factory for [02](../categories/02_inference_accelerators.md).
- **Recent/Relevant Work:** AWQ (2023), QServe/W4A8KV4 (2024), StreamingLLM (2023), SpAtten. **Prior Startups:** OmniML→NVIDIA (Confirmed); DeePhi (earlier, →Xilinx). **Startup Signal:** Likely · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Vivienne Sze
- **Institution / Role:** MIT (Professor)
- **Research Areas:** Energy-efficient deep-learning hardware (Eyeriss), hardware-aware co-design, efficient autonomy
- **Why VC Should Track:** Authoritative on energy-efficiency methodology for edge/DC inference ([03](../categories/03_edge_inference_chips.md)/[02](../categories/02_inference_accelerators.md)); trains hardware-efficiency talent.
- **Recent/Relevant Work:** Eyeriss line; sparse-tensor accelerator co-design with Emer (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 4 · **Confidence:** High · **Last updated:** 2026-06-09

### Tri Dao
- **Institution / Role:** Princeton (Assistant Professor) / Together AI (Chief Scientist)
- **Research Areas:** IO-aware attention (FlashAttention), state-space models (Mamba), efficient inference kernels
- **Why VC Should Track:** His kernels/architectures define *what inference silicon must optimize for*; FlashAttention is ubiquitous, and Mamba/SSMs are the key architecture-drift risk for transformer-hardwired ASICs ([Etched](../categories/02_inference_accelerators.md)).
- **Recent/Relevant Work:** FlashAttention-2 (2023), FlashAttention-3 (2024), Mamba (2023), Mamba-2 (2024). **Industry:** Together AI (Confirmed). **Startup Signal:** Likely (Together) · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Christopher Ré
- **Institution / Role:** Stanford (Professor) / SambaNova (co-founder)
- **Research Areas:** ML systems, state-space models (S4/H3 lineage), data-centric ML, efficient architectures
- **Why VC Should Track:** Co-founder of SambaNova and serial company-builder; SSM lineage shapes future inference-hardware targets.
- **Prior Startups:** SambaNova, Snorkel, Lattice Data (acq. Apple) (Confirmed). **Startup Signal:** Confirmed · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Vijay Janapa Reddi
- **Institution / Role:** Harvard (Professor); MLCommons
- **Research Areas:** ML systems benchmarking (MLPerf), edge/TinyML, autonomous-machine computing
- **Why VC Should Track:** Drives the benchmarks (MLPerf Inference/Training, MLPerf Tiny) by which all AI silicon is judged; a neutral lens on real performance claims for diligence.
- **Recent/Relevant Work:** MLPerf inference/edge benchmarking, robot-learning compute (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 4 · **Confidence:** High · **Last updated:** 2026-06-09

### Saman Amarasinghe
- **Institution / Role:** MIT (Professor)
- **Research Areas:** Compilers for accelerators (Halide, TACO, Exo), domain-specific code generation
- **Why VC Should Track:** The compiler stack is the silent killer of AI silicon; his group's tooling and students are central to making novel hardware programmable ([12](../categories/12_eda_ip_and_design_tools.md)/[02](../categories/02_inference_accelerators.md)).
- **Recent/Relevant Work:** Exo (exocompilation for accelerators), sparse-tensor compilers (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

---

## C. Memory, PIM & Near-Memory

### Onur Mutlu
- **Institution / Role:** ETH Zürich (Professor); CMU (adjunct)
- **Research Areas:** Processing-in-memory, near-memory computing, memory systems/reliability (RowHammer)
- **Why VC Should Track:** Leading PIM research at the #1 bottleneck; repeated commercially-urgent publications; memory-maker collaborations ([07](../categories/07_memory_and_storage.md)/[14](../categories/14_quantum_neuromorphic_and_non_von_neumann.md)).
- **Recent/Relevant Work:** PIM-for-LLM/genomics, real-PIM system studies (UPMEM, HBM-PIM analyses), RowHammer/RowPress (2023–2025). **Patents:** High. **Startup Signal:** Likely · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Saugata Ghose
- **Institution / Role:** UIUC (Assistant Professor)
- **Research Areas:** Processing-in-memory, memory systems, near-data acceleration
- **Why VC Should Track:** Co-author of foundational PIM surveys; productization-oriented PIM research relevant to memory-fabric/PIM startups.
- **Recent/Relevant Work:** PIM architectures and workload studies (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium · **Last updated:** 2026-06-09

### Moinuddin Qureshi
- **Institution / Role:** Georgia Tech (Professor)
- **Research Areas:** Memory systems, caching, memory security, CXL/emerging memory
- **Why VC Should Track:** Influential memory-architecture researcher; work informs CXL tiering and memory-security IP ([07](../categories/07_memory_and_storage.md)).
- **Recent/Relevant Work:** CXL/memory-tiering and memory-security papers (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 3 · **Confidence:** Medium · **Last updated:** 2026-06-09

### Myoungsoo Jung
- **Institution / Role:** KAIST (Professor) / Panmnesia (founder)
- **Research Areas:** CXL systems, memory disaggregation, storage/memory architecture
- **Why VC Should Track:** Confirmed lab→startup (Panmnesia); Korea's CXL research strength; CXL fabric/pooling is a live commercialization wave ([07](../categories/07_memory_and_storage.md)).
- **Recent/Relevant Work:** CXL 3.x switch/fabric and memory-pooling systems (2023–2025). **Prior Startups:** Panmnesia (Confirmed). **Startup Signal:** Confirmed · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Mattan Erez
- **Institution / Role:** UT Austin (Professor)
- **Research Areas:** Memory systems, reliability, GPU/accelerator memory, HBM-adjacent
- **Why VC Should Track:** Deep memory-systems expertise relevant to HBM efficiency and resilience for AI accelerators.
- **Recent/Relevant Work:** Memory reliability/efficiency for accelerators (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 3 · **Confidence:** Medium · **Last updated:** 2026-06-09

---

## D. Interconnect & Networking

### Amin Vahdat
- **Institution / Role:** Google (Fellow & VP, ML/Systems/Cloud Infrastructure)
- **Research Areas:** Datacenter networking (Jupiter, Aquila), optical circuit switching, ML systems infrastructure
- **Why VC Should Track:** Defines hyperscale fabric requirements; Google's OCS-in-TPU approach signals where scale-up interconnect is heading ([05](../categories/05_networking_and_interconnect.md)/[06](../categories/06_optical_interconnect_and_cpo.md)).
- **Recent/Relevant Work:** TPU v4 optical-circuit-switch fabric (ISCA 2023); datacenter-network evolution (2023–2025). **Startup Signal:** Watchlist (incumbent) · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Ramin Farjadrad
- **Institution / Role:** Eliyan (co-founder & CEO); ex-Aquantia/Marvell
- **Research Areas:** SerDes, die-to-die interconnect, chiplet PHY
- **Why VC Should Track:** Serial-link/D2D pedigree; Eliyan's interposer-free chiplet links attack the CoWoS bottleneck ([04](../categories/04_custom_asic_and_chiplets.md)/[13](../categories/13_foundry_packaging_and_chiplet_integration.md)).
- **Prior Startups:** Velio, Aquantia (Confirmed), Eliyan (Confirmed). **Patents:** High (D2D/SerDes). **Startup Signal:** Confirmed · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

---

## E. Silicon Photonics & Optical Computing

### Keren Bergman
- **Institution / Role:** Columbia (Professor, Lightwave Research Lab)
- **Research Areas:** Silicon photonics, optical interconnect networks, photonic fabric, DWDM links
- **Why VC Should Track:** Premier academic photonic-interconnect group at the #2 bottleneck; talent and IP source for [06](../categories/06_optical_interconnect_and_cpo.md) (Xscape adjacency).
- **Recent/Relevant Work:** Energy-efficient DWDM optical interconnect, photonic fabric for AI clusters (2023–2025); leadership in DARPA/photonics programs. **Patents:** High. **Startup Signal:** Likely · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### John Bowers
- **Institution / Role:** UC Santa Barbara (Professor)
- **Research Areas:** Heterogeneous/quantum-dot lasers on silicon, integrated photonics
- **Why VC Should Track:** Laser integration is the hard bottleneck in CPO/optical I/O; Bowers' work underpins multiple photonics ventures ([06](../categories/06_optical_interconnect_and_cpo.md)).
- **Recent/Relevant Work:** QD comb lasers, heterogeneous integration on Si (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Michal Lipson
- **Institution / Role:** Columbia (Professor)
- **Research Areas:** Silicon photonics, frequency combs, programmable photonics
- **Why VC Should Track:** Foundational silicon-photonics researcher; her group seeds photonics founders for interconnect and sensing.
- **Recent/Relevant Work:** Integrated comb sources and programmable photonics (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Dirk Englund
- **Institution / Role:** MIT (Professor)
- **Research Areas:** Photonic computing, quantum photonics, optical neural networks
- **Why VC Should Track:** Optical-compute and quantum-photonics leadership; co-founder lineage relevant to photonic accelerators and quantum ([06](../categories/06_optical_interconnect_and_cpo.md)/[14](../categories/14_quantum_neuromorphic_and_non_von_neumann.md)).
- **Recent/Relevant Work:** Photonic deep-learning inference, integrated-photonics systems (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Marin Soljačić
- **Institution / Role:** MIT (Professor)
- **Research Areas:** Photonic computing, nanophotonics, AI-for-physics
- **Why VC Should Track:** Photonic-computing pioneer in the Lightelligence/Lightmatter intellectual lineage; relevant to optical compute/interconnect ([06](../categories/06_optical_interconnect_and_cpo.md)).
- **Recent/Relevant Work:** Optical neural-network and photonic-computing advances (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium · **Last updated:** 2026-06-09

### Jelena Vučković
- **Institution / Role:** Stanford (Professor)
- **Research Areas:** Nanophotonics, inverse-designed photonics, quantum photonics
- **Why VC Should Track:** Inverse-design photonics could compress photonic-device development cycles — relevant to scalable CPO/optical-I/O and quantum photonics.
- **Recent/Relevant Work:** Inverse-designed photonic devices, integrated quantum photonics (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 4 · **Confidence:** Medium · **Last updated:** 2026-06-09

---

## F. Analog / In-Memory / Emerging-Device Compute

### Naveen Verma
- **Institution / Role:** Princeton (Professor) / EnCharge AI (co-founder, CEO)
- **Research Areas:** Charge-domain analog in-memory compute, mixed-signal AI circuits
- **Why VC Should Track:** Confirmed lab→startup (EnCharge); robust analog IMC is the best near-term non-von-Neumann efficiency bet ([14](../categories/14_quantum_neuromorphic_and_non_von_neumann.md)); his students are prime founder candidates.
- **Recent/Relevant Work:** Charge-domain IMC macros, scalable analog-compute architectures (ISSCC/VLSI 2023–2025). **Prior Startups:** EnCharge (Confirmed). **Patents:** High (IMC). **Startup Signal:** Confirmed · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### H.-S. Philip Wong
- **Institution / Role:** Stanford (Professor); ex-TSMC VP Research
- **Research Areas:** Emerging memory (RRAM), in-memory compute, 3D integration, N3XT
- **Why VC Should Track:** Bridges device innovation and manufacturability (TSMC pedigree); central to IMC and 3D-integration startup theses ([14](../categories/14_quantum_neuromorphic_and_non_von_neumann.md)/[13](../categories/13_foundry_packaging_and_chiplet_integration.md)).
- **Recent/Relevant Work:** RRAM compute-in-memory, monolithic-3D (N3XT) systems (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### Naresh Shanbhag
- **Institution / Role:** UIUC (Professor)
- **Research Areas:** Deep in-memory architecture (DIMA), error-resilient/SRAM in-memory compute
- **Why VC Should Track:** Originated influential SRAM in-memory-compute concepts; foundational to the analog/digital IMC startup wave (EnCharge/Sagence lineage).
- **Recent/Relevant Work:** In-memory compute macros and analysis (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Kaushik Roy
- **Institution / Role:** Purdue (Professor)
- **Research Areas:** Neuromorphic computing, spintronic/emerging-device IMC, energy-efficient AI
- **Why VC Should Track:** Prolific neuromorphic/IMC researcher; talent pipeline for sparse/event-driven and emerging-device compute ([14](../categories/14_quantum_neuromorphic_and_non_von_neumann.md)).
- **Recent/Relevant Work:** Spiking/neuromorphic accelerators, in-memory compute with emerging devices (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 4 · **Confidence:** Medium · **Last updated:** 2026-06-09

### Wei Lu
- **Institution / Role:** University of Michigan (Professor)
- **Research Areas:** Memristors/RRAM, analog in-memory compute, neuromorphic devices
- **Why VC Should Track:** Memristor-IMC pioneer with commercialization track record; emerging-device compute IP ([14](../categories/14_quantum_neuromorphic_and_non_von_neumann.md)).
- **Recent/Relevant Work:** Memristor crossbar compute systems (2023–2025). **Prior Startups:** Crossbar; MemryX (co-founder, Confirmed). **Startup Signal:** Confirmed · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Dmitri Strukov
- **Institution / Role:** UC Santa Barbara (Professor)
- **Research Areas:** Memristive devices, analog neural-network hardware
- **Why VC Should Track:** Co-author of the canonical memristor work; analog-IMC device IP source.
- **Recent/Relevant Work:** Analog neuromorphic and memristor compute (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 3 · **Confidence:** Medium · **Last updated:** 2026-06-09

---

## G. EDA & AI-for-Chip-Design

### Brucek Khailany
- **Institution / Role:** NVIDIA (Senior Director, Design Automation Research)
- **Research Areas:** ML for EDA, agile VLSI design, accelerator design methodology
- **Why VC Should Track:** Leads NVIDIA's ML-for-design research (ChipNeMo, generative/RL design flows) — the frontier for AI-EDA startups ([12](../categories/12_eda_ip_and_design_tools.md)).
- **Recent/Relevant Work:** ChipNeMo (domain LLMs for chip design, 2023–2024); ML-driven design-automation (2023–2025). **Startup Signal:** Watchlist (incumbent) · **VC Relevance:** 4 · **Confidence:** High · **Last updated:** 2026-06-09

### Azalia Mirhoseini & Anna Goldie — **CONVERTED TO STARTUP (2026)**
- **Institution / Role:** **Co-founders, Ricursive Intelligence** (previously Stanford / Google DeepMind)
- **Research Areas:** RL for chip floorplanning (AlphaChip), ML for systems
- **Why VC Should Track:** Authors of the Nature chip-placement work (AlphaChip) that catalyzed the AI-for-physical-design wave; their methods underpin a generation of AI-EDA startups.
- **Recent/Relevant Work:** "A graph placement methodology for fast chip design" (Nature 2021) + AlphaChip extension (2024).
- **Outcome:** **Ricursive Intelligence raised a ~$300M Series A at roughly $4B post-money on 2026-01-26** — less than two months after launching — led by Lightspeed with DST Global, NVIDIA's NVentures, Felicis, Sequoia, Radical AI and 49 Palms. The pitch is a recursive loop: AI designs the silicon that runs the next generation of AI. This is the highest-value research-to-startup conversion recorded in this database. See [12](../categories/12_eda_ip_and_design_tools.md).
- **Startup Signal:** **Confirmed** · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-08-13

### Jason Cong
- **Institution / Role:** UCLA (Professor)
- **Research Areas:** FPGA/HLS, EDA, customized computing, accelerator-rich architectures
- **Why VC Should Track:** One of the most influential EDA/accelerator academics; serial company founder; HLS and customized-compute IP ([12](../categories/12_eda_ip_and_design_tools.md)/[04](../categories/04_custom_asic_and_chiplets.md)).
- **Prior Startups:** AutoESL (→Xilinx HLS), Falcon Computing, Neptune (Confirmed). **Recent/Relevant Work:** HLS + ML-for-EDA, accelerator design automation (2023–2025). **Startup Signal:** Confirmed (serial) · **VC Relevance:** 5 · **Confidence:** High · **Last updated:** 2026-06-09

### David Z. Pan
- **Institution / Role:** UT Austin (Professor)
- **Research Areas:** Physical design, ML for EDA, design for manufacturability, analog-design automation
- **Why VC Should Track:** Leading ML-for-EDA academic spanning digital + analog automation — the heart of the AI-EDA thesis ([12](../categories/12_eda_ip_and_design_tools.md)).
- **Recent/Relevant Work:** ML-driven place-and-route, analog layout automation, DFM (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Siddharth Garg
- **Institution / Role:** NYU (Professor)
- **Research Areas:** Hardware security, ML for hardware (LLMs for HDL), trustworthy ASICs
- **Why VC Should Track:** Bridges hardware security and AI-assisted design (e.g., LLM-generated Verilog studies) — relevant to [12](../categories/12_eda_ip_and_design_tools.md)/[09](../categories/09_security_crypto_and_confidential_compute.md).
- **Recent/Relevant Work:** LLMs-for-Verilog and hardware-security papers (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 3 · **Confidence:** Medium · **Last updated:** 2026-06-09

### Deming Chen
- **Institution / Role:** UIUC (Professor)
- **Research Areas:** HLS, FPGA, hardware-aware ML/AutoML, accelerator design
- **Why VC Should Track:** HLS + hardware-aware ML leader; tooling and students feed AI-EDA and FPGA-acceleration startups.
- **Recent/Relevant Work:** HLS for ML accelerators, DNN-hardware co-design (2023–2025). **Prior Startups:** Inspirit IoT (Confirmed). **Startup Signal:** Likely · **VC Relevance:** 3 · **Confidence:** Medium · **Last updated:** 2026-06-09

---

## H. Packaging & 3D Integration

### Subhasish Mitra
- **Institution / Role:** Stanford (Professor)
- **Research Areas:** Monolithic 3D integration (N3XT), robust systems, CNT/emerging-device computing
- **Why VC Should Track:** 3D integration is a packaging/architecture frontier ([13](../categories/13_foundry_packaging_and_chiplet_integration.md)); collaborations with Wong on N3XT point to high-density compute-memory integration.
- **Recent/Relevant Work:** Monolithic-3D compute systems and CNT FET integration (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Muhannad Bakir
- **Institution / Role:** Georgia Tech (Professor; Packaging Research Center / 3D Systems)
- **Research Areas:** Heterogeneous integration, interconnect, glass/Si interposers, thermal-aware packaging
- **Why VC Should Track:** Premier advanced-packaging research at the #3 bottleneck; substrate/interconnect IP and talent ([13](../categories/13_foundry_packaging_and_chiplet_integration.md)).
- **Recent/Relevant Work:** Heterogeneous-integration and interconnect/thermal packaging (2023–2025). **Patents:** High. **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Subramanian Iyer
- **Institution / Role:** UCLA (Professor; CHIPS consortium)
- **Research Areas:** Heterogeneous integration, dies-on-wafer, silicon-interconnect fabric, chiplets
- **Why VC Should Track:** Leads UCLA's silicon-interconnect-fabric work (a chiplet/packaging alternative); ex-IBM Fellow; central to chiplet-integration IP ([13](../categories/13_foundry_packaging_and_chiplet_integration.md)/[04](../categories/04_custom_asic_and_chiplets.md)).
- **Recent/Relevant Work:** Silicon-interconnect fabric, fine-pitch chiplet integration (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

---

## I. Power Electronics & Delivery

### David Perreault
- **Institution / Role:** MIT (Professor)
- **Research Areas:** High-density power conversion, high-frequency power electronics
- **Why VC Should Track:** Power delivery is rising fast with 100kW+ racks ([08](../categories/08_power_semiconductors_and_power_delivery.md)/[16](../categories/16_datacenter_infrastructure_enablers.md)); his topologies/students feed power-IC startups.
- **Recent/Relevant Work:** High-density converters, integrated power conversion (2023–2025). **Prior Startups:** Eta Devices (→Nokia), Eta Wireless (→Murata) (Confirmed). **Startup Signal:** Confirmed (serial) · **VC Relevance:** 4 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Tomás Palacios
- **Institution / Role:** MIT (Professor)
- **Research Areas:** GaN devices/electronics, wide-bandgap power, RF
- **Why VC Should Track:** GaN is core to datacenter power and RF; Finwave (GaN) lineage; device IP relevant to [08](../categories/08_power_semiconductors_and_power_delivery.md)/[10](../categories/10_rf_wireless_and_connectivity.md).
- **Recent/Relevant Work:** GaN power/RF devices and integration (2023–2025). **Prior Startups:** Finwave Semiconductor (Confirmed). **Startup Signal:** Confirmed · **VC Relevance:** 4 · **Confidence:** Medium · **Last updated:** 2026-06-09

### Khurram Afridi
- **Institution / Role:** Cornell (Professor)
- **Research Areas:** High-frequency power conversion, wireless power, datacenter power delivery
- **Why VC Should Track:** Power-delivery research aligned to AI-rack density; talent for power-IC/delivery startups.
- **Recent/Relevant Work:** High-frequency/high-density power conversion (2023–2025). **Startup Signal:** Watchlist · **VC Relevance:** 3 · **Confidence:** Medium · **Last updated:** 2026-06-09

---

## J. Quantum & Cryogenic Hardware

### Mikhail Lukin
- **Institution / Role:** Harvard (Professor)
- **Research Areas:** Neutral-atom quantum computing, quantum networks
- **Why VC Should Track:** Co-founder lineage of QuEra; neutral-atom is a leading qubit modality; error-correction milestones revive quantum capital ([14](../categories/14_quantum_neuromorphic_and_non_von_neumann.md)).
- **Recent/Relevant Work:** "Logical quantum processor based on reconfigurable atom arrays" (Nature 2023); subsequent logical-qubit advances (2024–2025). **Prior Startups:** QuEra (co-founder, Confirmed). **Startup Signal:** Confirmed · **VC Relevance:** 4 · **Confidence:** High · **Last updated:** 2026-06-09

### John Martinis
- **Institution / Role:** UC Santa Barbara (Professor); ex-Google Quantum
- **Research Areas:** Superconducting qubits, quantum hardware scaling
- **Why VC Should Track:** Built Google's superconducting-qubit program; founded Qolab; among the most credible voices on quantum-hardware engineering ([14](../categories/14_quantum_neuromorphic_and_non_von_neumann.md)).
- **Recent/Relevant Work:** Superconducting-qubit scaling/quality (2023–2025). **Prior Startups:** Qolab (co-founder, Confirmed). **Startup Signal:** Confirmed · **VC Relevance:** 4 · **Confidence:** High · **Last updated:** 2026-06-09

### Robert Schoelkopf
- **Institution / Role:** Yale (Professor)
- **Research Areas:** Circuit QED, superconducting qubits, bosonic error correction
- **Why VC Should Track:** Quantum Circuits, Inc. co-founder; bosonic-code approach to fault tolerance; a distinct quantum-hardware path.
- **Recent/Relevant Work:** Error-corrected bosonic qubits (2023–2025). **Prior Startups:** Quantum Circuits Inc. (co-founder, Confirmed). **Startup Signal:** Confirmed · **VC Relevance:** 3 · **Confidence:** Medium-High · **Last updated:** 2026-06-09

### Edoardo Charbon
- **Institution / Role:** EPFL (Professor)
- **Research Areas:** Cryogenic CMOS (Horse Ridge collaboration), quantum control electronics, SPADs
- **Why VC Should Track:** Cryo-CMOS control is the picks-and-shovels layer for scaling quantum ([14](../categories/14_quantum_neuromorphic_and_non_von_neumann.md)); SEEQC/Intel-adjacent relevance.
- **Recent/Relevant Work:** Cryogenic CMOS control ICs for qubits (2023–2025). **Startup Signal:** Likely · **VC Relevance:** 3 · **Confidence:** Medium · **Last updated:** 2026-06-09

---

## Refresh Notes
| Date | Refresh Type | Added | Updated | Sources |
|------|--------------|-------|---------|---------|
| 2026-06-09 | Full (initial) | 10 | 0 | Public academic/institutional pages, publications |
| 2026-06-09 | Expansion #2 | 28 | 10 | Public faculty pages, arXiv, ISSCC/ISCA/MICRO/OFC/Nature (2023–2025); founder histories from public records |
| 2026-08-13 | Status refresh | 0 | 3 | Mirhoseini & Goldie marked **Confirmed** (Ricursive Intelligence, ~$300M A at ~$4B); Jonathan Ross reclassified as incumbent after moving to NVIDIA in the ~$20B Groq licence deal; Kunle Olukotun/SambaNova note updated for the Series F. Sources: company releases, public role changes |
