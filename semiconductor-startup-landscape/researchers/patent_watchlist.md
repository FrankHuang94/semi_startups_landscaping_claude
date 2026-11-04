# Patent Watchlist

Patent clusters and assignment signals relevant to AI-semiconductor commercialization. Template: [../_templates/patent_entry_template.md](../_templates/patent_entry_template.md). Public patent databases only.

> **Key sourcing signal:** a patent assignment transitioning from a university to a *new/unknown entity* (or a researcher's new company) is a High commercialization signal — see the framework in [../RESEARCH_AND_RESEARCHERS.md](../RESEARCH_AND_RESEARCHERS.md). Entries below are *clusters/themes to monitor*, not specific patent numbers, pending verification.

| Patent Cluster / Theme | Likely Assignee Type | Area | Why It Matters for VC | Signal | Related Labs/Cos | VC Rel | Confidence |
|------------------------|----------------------|------|------------------------|--------|------------------|:------:|------------|
| Charge-domain / metal-cap IMC | Princeton → EnCharge | Analog IMC | Tracks IMC commercialization & follow-ons | Likely | Verma / EnCharge | 5 | Medium |
| D2D PHY over organic substrate | Eliyan / individuals | Chiplet interconnect | Interposer-free packaging IP | Likely | Eliyan | 5 | Medium |
| Optical I/O chiplet / SuperNova laser | Ayar Labs / Berkeley | Photonics | Optical-I/O IP moat | Likely | Ayar / Stojanović | 5 | Medium |
| Photonic fabric / DWDM links | Columbia / startups | Photonics | Optical-interconnect commercialization | Weak | Bergman / Xscape | 4 | Medium |
| CXL switch / fabric IP | KAIST → Panmnesia | Memory fabric | CXL commercialization signal | Likely | Jung / Panmnesia | 4 | Medium |
| HBM-PIM / near-memory | Samsung/SK hynix | Memory | Memory-maker PIM direction | Watchlist | Samsung/SK | 4 | Medium |
| Glass-core substrate processes | Intel / GT / SKC | Packaging | Substrate-generation IP | Weak | Absolics / GT | 4 | Medium |
| Two-phase / microjet cooling | Cooling startups / labs | Thermal | 100kW-rack cooling IP | Weak | ZutaCore / JetCool | 3 | Medium |
| GaN integration / vertical power | Power startups | Power | Datacenter power IP | Watchlist | Empower / Navitas | 4 | Medium |
| Crypto/ZK-FHE arithmetic units | Fabric/Cysic/Niobium | Security | Crypto-accelerator IP | Weak | Fabric Cryptography | 3 | Medium |
| UCIe / die-to-die PHY IP | Multiple (Synopsys/Cadence/startups) | Chiplet interconnect | D2D standard IP land-grab (2023–) | Watchlist | Blue Cheetah / Baya | 4 | Medium |
| NoC / chiplet fabric IP | Baya Systems / individuals | Chiplet fabric | Software-defined fabric IP | Likely | Baya Systems | 4 | Medium |
| Digital in-memory compute (SRAM) | d-Matrix / academia | Inference | DIMC accuracy-safe IP | Likely | d-Matrix / Shanbhag | 4 | Medium |
| Transformer-dataflow ASIC | Etched / individuals | Inference | Transformer-specialized silicon IP | Weak | Etched | 3 | Low-Medium |
| Linear-drive optics (LPO/LRO) | Optics startups | Photonics | Lower-power pluggable/CPO IP | Watchlist | Nubis / incumbents | 4 | Medium |
| Co-packaged optics / fiber attach | NVIDIA/Broadcom/startups | Photonics | CPO packaging & coupling IP (2023–) | Watchlist | Ayar / Celestial | 4 | Medium |
| 800V HVDC / vertical power delivery | NVIDIA-ecosystem / power cos | Power | Rack-scale power architecture IP | Watchlist | Navitas / Vicor / Empower | 4 | Medium |
| Hybrid bonding / 3D stacking | TSMC / imec / Besi | Packaging | 3D stacking pitch/yield IP | Watchlist | imec / TSMC | 4 | Medium |
| RL/LLM for chip design (AI-EDA) | Google / NVIDIA / startups | EDA | AI-for-design method IP (2023–) | Watchlist | AlphaChip / ChipNeMo lineage | 3 | Medium |
| Reconfigurable atom-array control | QuEra / Harvard | Quantum | Neutral-atom control IP | Watchlist | Lukin / QuEra | 3 | Low-Medium |
| Cryogenic CMOS control ICs | Intel / SEEQC / EPFL | Quantum control | Qubit-control electronics IP | Watchlist | Charbon / SEEQC | 3 | Low-Medium |
| Metasurface optical modulators for matrix compute *(2026-11-04)* | Duke / Metacept → Neurophos | Optical compute | Core IP behind a $110M Series A (Jan 2026) | Likely | D. R. Smith / Neurophos | 4 | Medium |
| Metal-layer-programmable / model-hardwired inference ASIC *(2026-11-04)* | Taalas / individuals | Inference | Per-model silicon with few-mask respins | Likely | Taalas | 4 | Medium |
| Agentic LLM flows for RTL generation & verification *(2026-11-04)* | ChipAgents / Cognichip / Ricursive / Synopsys / Cadence | EDA | Startups vs. incumbents racing to claim agentic-EDA methods | Likely | W. Wang / Goldie & Mirhoseini | 5 | Medium |
| Analog-silicon AI compute + analog compilation *(2026-11-04)* | Unconventional AI / MIT / Stanford | Analog compute | Watch first assignments to Unconventional AI (none verified yet) | Watchlist | Rao / Carbin / Achour | 4 | Low-Medium |
| Thermodynamic / stochastic sampling hardware *(2026-11-04)* | Normal Computing / Extropic | Probabilistic compute | New-paradigm accelerator IP | Weak | Normal Computing / Extropic | 3 | Low-Medium |
| Memory-pooled rack-scale AI server architecture *(2026-11-04)* | Majestic Labs / hyperscalers | Memory systems | Memory-wall system IP (ship 2027) | Likely | Majestic Labs | 4 | Medium |
| HBM4 custom base-die / logic-in-base-die *(2026-11-04)* | SK hynix / Samsung / TSMC | Memory | Custom-HBM opens near-memory compute IP licensing | Watchlist | Samsung / SK hynix | 4 | Medium |
| CPO switch micro-ring modulators & detachable fiber connectors *(2026-11-04)* | NVIDIA / TSMC (COUPE) / Broadcom / startups | Photonics | Production CPO creates component-level IP openings | Watchlist | Ayar / Xscape / incumbents | 5 | Medium |
| qLDPC / neutral-atom fault-tolerant QEC architectures *(2026-11-04)* | IBM / QuEra / Harvard | Quantum | QEC architecture IP for fault tolerance | Watchlist | Lukin / IBM | 3 | Low-Medium |

## Monitoring Workflow
1. Watch assignee changes (university → new LLC) for tracked researchers.
2. Cross-reference new entities against domain registrations, Form D, and LinkedIn role changes.
3. When a new-entity assignment + one more signal appears, promote to [researcher_to_startup_signal_tracker.md](researcher_to_startup_signal_tracker.md) and [../STEALTH_STARTUP_DISCOVERY.md](../STEALTH_STARTUP_DISCOVERY.md).

## Refresh Notes
| Date | Refresh Type | Added | Updated | Sources |
|------|--------------|-------|---------|---------|
| 2026-06-09 | Full (initial) | 10 (clusters) | 0 | Public patent databases (themes; numbers TO VERIFY) |
| 2026-06-09 | Expansion #2 | 12 (clusters) | 0 | Public patent databases; emphasis on 2023– filing activity (numbers TO VERIFY) |
| 2026-11-04 | Full (Refresh #3) | 9 (clusters) | 0 | Company funding disclosures mapped to IP themes; patent numbers TO VERIFY; data/patent_index.yaml synced to 30 clusters |
