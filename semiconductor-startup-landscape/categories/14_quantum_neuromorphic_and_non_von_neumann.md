---
category_id: "14"
category_name: "Quantum, Neuromorphic & Non-Von-Neumann"
primary_datacenter_relevance: "Low/Long-term"
vc_relevance: "Medium-High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 15
active_companies: 14
archived_companies: 1
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$6B+ [ESTIMATED]"
top_investors: ["BlackRock", "Temasek", "Baillie Gifford", "NVentures", "a16z", "Lightspeed", "Samsung Catalyst", "Tiger Global", "In-Q-Tel", "RTX Ventures"]
key_technical_inflections: ["Analog/in-memory compute for energy-per-token", "Thermodynamic / probabilistic computing (CN101, Extropic)", "Mega-seed 'new physics of compute' labs (Unconventional AI)", "Fault-tolerant quantum (logical qubits)", "Cryogenic CMOS control", "Neuromorphic/sparse event compute"]
key_open_questions: ["Does analog IMC cross the accuracy/software chasm?", "Do thermodynamic chips scale beyond diffusion demos?", "When (if) does fault-tolerant quantum arrive, and are 2025–26 quantum valuations sustainable?", "Does neuromorphic find a killer app?"]
---

# 14 — Quantum, Neuromorphic & Non-Von-Neumann

> Long-horizon, binary-outcome, category-defining upside. 2025–26 changed the capital picture: quantum raised at record valuations (PsiQuantum ~$1B at ~$7B; Quantinuum ~$600M at ~$10B; SPAC/IPO activity) [TO VERIFY]; "new physics of compute" got mega-seeds (Unconventional AI, Naveen Rao — reported $475M) [UNCONFIRMED]; thermodynamic computing taped out first silicon (Normal Computing CN101) and raised strategic money (Samsung Catalyst). Analog IMC still has the nearest commercial path; some first-wave analog players failed (Rain AI wound down; patents sold to OpenAI, Aug 2026 [TO VERIFY]). Quantinuum's Jun 2026 Nasdaq IPO (~$1.68B raised) [CONFIRMED] opened the quantum IPO window. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

> ⚠️ **Verification note (Refresh #3):** the shared web-search budget was exhausted before the quantum/analog-IMC sub-batch was searched. Items tagged [TO VERIFY]/[UNCONFIRMED] below are carried from prior knowledge and must be re-checked next refresh. Normal Computing and EnCharge figures were verified via search.

## 1. VC Investment Thesis
- **Why now:** AI energy-per-token is unsustainable on digital von-Neumann silicon → analog IMC, thermodynamic/probabilistic and other physics-native compute are getting funded at AI-lab scale; quantum error-correction milestones and sovereign programs pulled in crossover/sovereign capital and public listings.
- **Venture-scale:** Medium-High but binary — IMC can produce near-term efficiency wins; thermodynamic/physics-native labs are new high-variance bets; quantum is moonshot/strategic with public-market exits now available (IonQ, Rigetti, D-Wave, SPACs).
- **Inflections:** Analog IMC inference (EnCharge EN100 [TO VERIFY]), thermodynamic sampling chips (CN101), neuromorphic/sparse, logical-qubit demonstrations, cryo-CMOS control, quantum consolidation by public players (IonQ roll-up).
- **Acquirers:** NVIDIA, Intel, hyperscalers, defense, Samsung, quantum strategics (IonQ, Honeywell/Quantinuum). **Exit:** strategic M&A, IPO/SPAC (quantum), or long-hold.
- **Winning startup:** analog IMC with energy/token leadership + working software; or physics-native compute with a credible path to beat GPUs on a real workload; or quantum with a credible fault-tolerance roadmap. **Non-investable:** neuromorphic without a killer app; quantum without error-correction credibility; analog without a software stack (Rain AI lesson).

## 2. Market Context
- **Structure:** Analog/IMC startups; thermodynamic/probabilistic compute (Normal Computing, Extropic); new physics-native AI labs (Unconventional AI); neuromorphic (BrainChip, Innatera); quantum hardware (PsiQuantum, Quantinuum, QuEra, Infleqtion, Alice & Bob, Atom Computing, Pasqal; public IonQ, Rigetti, D-Wave) + control layer (Quantum Machines, SEEQC).
- **Key 2025–26 events:**
  - PsiQuantum ~$1B Series E at ~$7B valuation (Sept 2025; BlackRock, Temasek, Baillie Gifford; NVentures participation) [TO VERIFY].
  - Quantinuum ~$600M raise at ~$10B pre-money (Sept 2025) [TO VERIFY]; **IPO on Nasdaq (QNT) priced 2026-06-03 at $60/share, raising ~$1.68B — the largest quantum listing to date** [CONFIRMED].
  - PsiQuantum $1B Series E at ~$7B (Sept 2025) [CONFIRMED by multiple outlets]; 2027 IPO speculation [UNCONFIRMED].
  - Rain AI: Series B collapse and failed sale; OpenAI bought selected patents (Aug 2026) [TO VERIFY].
  - IonQ acquisition spree (Oxford Ionics ~$1.08B, 2025 [TO VERIFY]; further deals incl. reported SkyWater Technology acquisition announced early 2026 [UNCONFIRMED]).
  - Infleqtion business combination with Churchill Capital Corp X (announced Sept 2025) [TO VERIFY]; listing status in 2026 [UNCONFIRMED].
  - Normal Computing $50M led by Samsung Catalyst (Mar 2026), total >$85M; CN101 thermodynamic chip taped out mid-2025 [CONFIRMED].
  - Unconventional AI (Naveen Rao) reported $475M seed for physics-native/"neuromorphic-like" AI chips [UNCONFIRMED amount; reported ~$4.5B valuation, a16z/Lightspeed-led — TO VERIFY].
  - EnCharge AI $100M Series B (Feb 2025, Tiger Global-led), total ~$144M [CONFIRMED].
- **Segments:** AI inference efficiency (IMC, thermodynamic), edge sparse compute (neuromorphic), HPC/crypto/chemistry (quantum, long-term).
- **Drivers:** Energy wall, defense, sovereign quantum programs, error-correction progress, NVIDIA's quantum-GPU (NVQLink/CUDA-Q) ecosystem [TO VERIFY].
- **Bottlenecks:** Analog accuracy/PVT + software (IMC); scaling beyond toy workloads (thermodynamic); qubit error rates/scaling (quantum); programming models (neuromorphic).
- **Risks:** Long timelines, capital intensity, valuation froth in quantum, binary outcomes.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| EnCharge AI | US (Santa Clara) | 2022 | Series B | ~$144M+ [CONFIRMED] | Tiger Global (B), RTX Ventures, In-Q-Tel, Samsung | Analog in-memory AI accelerator (EN100) | Edge/client + DC inference | Charge-domain analog IMC | $100M B (Feb 2025) [CONFIRMED]; EN100 launch 2025 [TO VERIFY] | High | Active |
| Normal Computing | US (New York) | 2022 | Strategic/Growth | ~$85M+ [CONFIRMED] | Samsung Catalyst (Mar 2026); Galvanize, Brevan Howard MVF, ArcTern | CN101 thermodynamic chip + AI EDA software | Gen-AI (diffusion) inference; chip design | First taped-out thermodynamic computing chip (company claim); ARIA co-research | CN101 tape-out mid-2025 (June vs. Aug conflict); EDA at >half of top-10 chipmakers (company claim) | High | Active |
| Unconventional AI | US | 2025 | Seed (mega) | ~$475M [UNCONFIRMED] | a16z, Lightspeed [TO VERIFY] | Physics-native / brain-inspired AI compute | AI training/inference (long-term) | Naveen Rao (Nervana, MosaicML) | Pre-product | High (high-variance) | Active |
| Extropic | US | 2022 | Seed | ~$14M+ [TO VERIFY] | Kindred Ventures [TO VERIFY] | Thermodynamic sampling units (probabilistic bits) | Generative AI sampling | All-transistor probabilistic computing | Dev hardware/Z1 announced 2025 [UNCONFIRMED] | Medium | Active |
| Sagence AI | US | 2018 | Series A+ | [TO VERIFY] | [TO VERIFY] | Analog in-memory inference | DC inference | Analog compute for LLM efficiency | No 2025–26 update found | Medium | Active |
| Mythic | US (Austin) | 2012 | Growth (recapitalized) | ~$165M+ prior + reported ~$125M (Dec 2025) [UNCONFIRMED] | DCVC, Lux, SoftBank; [TO VERIFY] | Analog matrix processor (flash IMC) | Edge + DC inference | Flash-based analog compute | Relaunch under new leadership; new round reported [UNCONFIRMED] | Medium | Active |
| Rain AI | US | 2017 | Wound down / asset sale | ~$60M+ [TO VERIFY] | Prosperity7, S. Altman | Compute-in-memory NPU | Edge/DC inference | Analog/digital IMC | $150M Series B collapsed (2025), sale process failed; OpenAI bought selected patents (Aug 2026) [TO VERIFY — The Information via secondary] | Archived | Effectively shut down |
| PsiQuantum | US (Palo Alto) | 2016 | Growth (Series E) | ~$2.3B+ [ESTIMATED] (incl. ~$1B Sept 2025 at ~$7B [TO VERIFY]) | BlackRock, Temasek, Baillie Gifford; NVentures [TO VERIFY] | Photonic fault-tolerant quantum | Quantum computing | Silicon-photonic FT quantum (GlobalFoundries) | Brisbane & Chicago utility-scale sites (gov-backed) | Medium | Active |
| Quantinuum | US/UK | 2021 | **Public (Nasdaq: QNT, IPO Jun 2026)** [CONFIRMED] | ~$1.6B+ [ESTIMATED] (incl. ~$600M Sept 2025 at ~$10B pre [TO VERIFY]) | Honeywell (majority), NVentures, Quanta [TO VERIFY] | Trapped-ion quantum (H-series, Helios) | Quantum computing | Highest-fidelity trapped ions; logical-qubit leadership | IPO priced 2026-06-03 at $60/sh, raising ~$1.68B [CONFIRMED] | Medium | Public |
| QuEra | US (Boston) | 2018 | Growth | ~$300M+ [TO VERIFY] (>$230M Feb 2025) | Google, SoftBank Vision Fund [TO VERIFY] | Neutral-atom quantum | Quantum computing | Harvard/MIT neutral-atom error correction | AIST Japan system [TO VERIFY] | Medium | Active |
| Infleqtion | US (Boulder) | 2007 | SPAC (2025–26) | [TO VERIFY] | Churchill Capital Corp X (SPAC) [TO VERIFY] | Neutral-atom quantum + quantum sensors/clocks | Quantum computing, defense PNT | Revenue from sensing/timing products | SPAC listing status [UNCONFIRMED] | Medium | Active |
| Alice & Bob | FR (Paris) | 2020 | Series B | ~€130M+ [TO VERIFY] (€100M B Jan 2025) | Future French Champions, AVP, Bpifrance [TO VERIFY] | Cat-qubit superconducting quantum | Quantum computing | Bosonic cat qubits (hardware-efficient QEC) | Roadmap to FT by ~2030 (company claim) | Medium | Active |
| SEEQC | US | 2019 | Series B | ~$80M+ [TO VERIFY] | LG, EQT, M Ventures | Digital quantum control (SFQ cryo chips) | Quantum control | Single-chip cryogenic control | Partnerships | Medium | Active |
| Quantum Machines | IL | 2018 | Series C | ~$280M [TO VERIFY] (incl. $170M C, Feb 2025, PSG Equity-led [TO VERIFY]) | PSG Equity, Red Dot, Intel Capital | Quantum control/orchestration (OPX) | Quantum control | Controller + software; NVIDIA DGX Quantum | Broad install base | Medium | Active |
| Innatera | NL | 2020 | Series A+ | ~$25M+ [TO VERIFY] | InnovationQuarter, MIG | Neuromorphic spiking MCU (Pulsar) | Ultra-low-power edge | Analog/digital spiking NN | Pulsar commercial launch 2025 [TO VERIFY] | Medium | Active |

## 4. Company Profiles

### EnCharge AI
- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2022 · **Founders:** Naveen Verma (Princeton), Kailash Gopalakrishnan (ex-IBM), Echere Iroaga
- **Stage:** Series B · **Total Funding:** ~$144M+ [CONFIRMED] · **Last Round:** $100M+ oversubscribed Series B (Feb 2025) led by Tiger Global; backers incl. RTX Ventures, In-Q-Tel, Samsung Ventures, HH-CTBC, ACVC [CONFIRMED — TechCrunch/DCD] · **Website:** encharge.ai
- **Primary:** 14 · **Secondary:** 02/03 · **One-Line:** Charge-domain analog in-memory compute accelerator for AI inference from client/edge to datacenter.
- **Tech:** switched-capacitor charge-domain IMC (metal-cap based) sidestepping PVT problems of resistive analog IMC; full software stack. First product EN100 (client/edge) [TO VERIFY]. **Risk:** software maturity, scaling to largest models, competition from digital NPUs.
- **VC view:** High (best near-term analog-IMC bet). **Data quality:** Medium-High. **Last updated:** 2026-11-04.

### Normal Computing (new)
- **Status:** Active · **HQ:** New York, US · **Founded:** 2022 · **Stage:** Strategic/growth · **Total Funding:** >$85M [CONFIRMED — SiliconANGLE] · **Last Round:** $50M led by Samsung Catalyst Fund (Mar 25 2026), with Galvanize, Brevan Howard Macro Venture Fund, ArcTern Ventures [CONFIRMED]
- **Primary:** 14 · **Secondary:** [12](12_eda_ip_and_design_tools.md) · **One-Line:** Full-stack "physics-based" AI company: AI-native EDA/verification software (near-term revenue) plus CN101, described as the first taped-out thermodynamic computing chip, targeting diffusion-model inference with a long-term 1,000x energy-efficiency goal (company claim).
- **Notes:** Tape-out date conflict (June vs. Aug 2025 across sources); ARIA (UK) co-researches the architecture and notes scalability is unproven. **VC view:** High-variance; Samsung strategic. **Data quality:** Medium. **Last updated:** 2026-11-04.

### Unconventional AI (new)
- **Status:** Active · **HQ:** US · **Founded:** 2025 · **Founder/CEO:** Naveen Rao (founder of Nervana, acquired by Intel; MosaicML, acquired by Databricks)
- **Funding:** reported ~$475M seed [UNCONFIRMED — single headline source seen this refresh]; reported ~$4.5B valuation led by a16z and Lightspeed [TO VERIFY].
- **One-Line:** Lab pursuing physics-native/brain-inspired hardware to cut AI energy by orders of magnitude. **Risk:** extreme technical risk, multi-year horizon. **VC view:** High-variance flagship of the "new compute physics" wave. **Data quality:** Low. **Last updated:** 2026-11-04.

### PsiQuantum
- **Status:** Active · **HQ:** Palo Alto, US · **Founded:** 2016 · **Founders:** Jeremy O'Brien, Terry Rudolph, Mark Thompson, Pete Shadbolt
- **Stage:** Series E · **Total Funding:** ~$2.3B+ [ESTIMATED] · **Last Round:** ~$1B (Sept 2025) at ~$7B valuation, led by BlackRock, Temasek, Baillie Gifford, with NVentures [TO VERIFY]; plus large government commitments (Australia/Queensland, US/Illinois) [TO VERIFY] · **Website:** psiquantum.com
- **Primary:** 14 · **One-Line:** Utility-scale, fault-tolerant quantum computer using silicon photonics and conventional semiconductor manufacturing (GlobalFoundries).
- **Risk:** the hardest moonshot in the database; timeline + physics risk. **VC view:** Medium (moonshot, strategic/sovereign capital). **Data quality:** Medium. **Last updated:** 2026-11-04.

> Sagence, Mythic, Rain (analog IMC); Extropic (thermodynamic); Quantinuum, QuEra, Infleqtion, Alice & Bob (quantum hardware); SEEQC, Quantum Machines (quantum control); Innatera (neuromorphic) at table level. Public quantum names (IonQ, Rigetti, D-Wave) and BrainChip (public, neuromorphic) are comparables; GrAI Matter (acquired) see [03](03_edge_inference_chips.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Analog in-memory compute | High | Very High | Medium-High | Medium | Real (near-term) but shake-out | Medium-High |
| Digital in-memory compute | High | High | Medium | Medium | Real | Medium-High |
| Thermodynamic / probabilistic compute | Medium (rising) | Very High | Medium | Low | High-variance; first silicon | Medium-High |
| Physics-native AI labs (mega-seed) | Medium | Extreme | Very High | Low | Moonshot | Medium (price-sensitive) |
| Neuromorphic/sparse | Medium | High | Medium | Low | Niche (needs app) | Medium |
| Fault-tolerant quantum | Long-term (capital-rich) | Extreme | Very High | Low | Moonshot; public exits exist | Medium |
| Quantum control electronics | Medium | High | Medium | Medium | Real (picks/shovels) | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Tiger Global | Crossover | EnCharge | B | Led EnCharge B (Feb 2025) | Energy-efficient inference |
| Samsung Catalyst | Strategic | Normal Computing (also Samsung in EnCharge) | Growth | Led $50M (Mar 2026) | Thermodynamic + AI EDA |
| a16z / Lightspeed | VC | Unconventional AI [TO VERIFY] | Seed (mega) | 2025 | New compute physics |
| NVentures (NVIDIA) | Strategic | PsiQuantum, Quantinuum, QuEra [TO VERIFY] | Growth | 2025 | Quantum-GPU hybrid ecosystem |
| In-Q-Tel / RTX Ventures | Strategic (defense) | EnCharge | B | EnCharge | Defense efficiency |
| BlackRock / Temasek / Baillie Gifford | Crossover/Sovereign | PsiQuantum | Growth | ~$1B round (2025) [TO VERIFY] | Moonshot patience |
| Intel Capital / PSG Equity | Strategic / PE | Quantum Machines | B–C | $170M C (2025) [TO VERIFY] | Quantum stack |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Naveen Verma | Princeton | Charge-domain IMC | EnCharge origin; robust analog IMC | Confirmed (EnCharge) | IMC papers/patents | 5 | High |
| Naveen Rao | Unconventional AI | Brain-inspired / physics-native compute | Serial founder (Nervana, MosaicML) leading mega-seed | Confirmed (founder) | — | 5 | Medium |
| ARIA "Scaling Compute" programme | ARIA (UK) | Thermodynamic / novel compute | Co-research with Normal Computing; funds new-physics compute | Watchlist | — | 4 | Medium |
| H.-S. Philip Wong | Stanford | Emerging memory/IMC | RRAM/IMC device leadership | Likely | Many | 5 | High |
| Kaushik Roy | Purdue | Neuromorphic/IMC | Sparse/neuromorphic compute | Watchlist | Many | 4 | Medium |
| Quantum hardware groups | MIT/Harvard/Maryland/UCSB/Delft | Qubits, error correction | Quantum founder pipeline (QuEra lineage) | Watchlist/Confirmed | Many | 4 | Medium |

## 8. Diligence Questions
- **Technical (IMC):** Accuracy at INT4/8 vs. digital; PVT robustness; software stack; energy/token measured on real models?
- **Technical (thermodynamic/physics-native):** Which workload beats a GPU end-to-end (not just at the kernel)? Scaling path beyond diffusion demos?
- **Technical (quantum):** Logical-qubit roadmap, error rates, manufacturability?
- **Market:** Which workload pulls first; near-term revenue (e.g., Normal's EDA, Infleqtion's sensors) vs. moonshot?
- **Customer:** Defense/strategic/cloud commitments?
- **Financial:** Capital to milestone; mega-seed valuations vs. milestones; quantum public-comps volatility?
- **Founder:** device + systems + software depth? **Exit:** strategic acquirer; IPO/SPAC; binary outcome sizing?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | 0 | Initial build; EnCharge/PsiQuantum profiles; IMC/quantum/neuromorphic coverage | Company sites, academic, trade press |
| 2026-11-04 | Full (Refresh #3) | 7 (Normal Computing, Unconventional AI, Extropic, Quantinuum, QuEra, Infleqtion, Alice & Bob) | 8 (all existing re-checked) | 0 | Normal Computing $50M Samsung Catalyst (Mar 2026) [CONFIRMED]; EnCharge $100M B confirmed; Unconventional AI mega-seed [UNCONFIRMED]; PsiQuantum ~$1B @ ~$7B, Quantinuum ~$600M @ ~$10B, IonQ roll-up, Infleqtion SPAC [all TO VERIFY — search budget exhausted]; Rain AI flagged distressed [UNCONFIRMED]; thermodynamic subsegment added | SiliconANGLE / Fortune (Normal), TechCrunch / DCD (EnCharge), ARIA update; quantum items pending re-verification |
