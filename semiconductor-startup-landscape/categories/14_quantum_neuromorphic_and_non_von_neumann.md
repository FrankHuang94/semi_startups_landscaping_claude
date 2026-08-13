---
category_id: "14"
category_name: "Quantum, Neuromorphic & Non-Von-Neumann"
primary_datacenter_relevance: "Low/Long-term"
vc_relevance: "Medium"
last_refreshed: "2026-08-13"
refresh_count: 2
total_companies: 8
active_companies: 8
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$2.5B+ [ESTIMATED]"
top_investors: ["BlackRock", "Temasek", "Tiger Global", "In-Q-Tel", "RTX Ventures"]
key_technical_inflections: ["Analog/in-memory compute for energy-per-token", "Fault-tolerant quantum", "Cryogenic CMOS control", "Neuromorphic/sparse event compute"]
key_open_questions: ["Does analog IMC cross the accuracy/software chasm?", "When (if) does fault-tolerant quantum arrive?", "Does neuromorphic find a killer app?"]
---

# 14 — Quantum, Neuromorphic & Non-Von-Neumann

> Long-horizon, binary-outcome, category-defining upside. Analog/in-memory compute has the nearest commercial path (AI energy efficiency); quantum is a 5–10yr moonshot needing patient/strategic capital. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis
- **Why now:** AI energy-per-token is unsustainable on digital von-Neumann silicon → analog/in-memory compute (IMC) is the near-term non-vN bet; quantum error-correction milestones are reviving quantum capital.
- **Venture-scale:** Medium overall, but binary — IMC can produce real near-term efficiency wins; quantum is moonshot/strategic.
- **Inflections:** Analog IMC inference, digital IMC, neuromorphic/sparse, fault-tolerant quantum, cryo-CMOS control, quantum control electronics.
- **Acquirers:** NVIDIA, Intel, hyperscalers, defense, quantum strategics. **Exit:** strategic M&A or long-hold IPO; binary.
- **Winning startup:** analog IMC with energy/token leadership + working software; or a credible fault-tolerance roadmap. **Non-investable:** neuromorphic without a killer app; quantum without error-correction credibility.

## 2. Market Context
- **Structure:** Analog/IMC startups; neuromorphic (BrainChip, Innatera); quantum (PsiQuantum, IonQ, Rigetti, Quantinuum) + control-electronics layer (Quantum Machines, SEEQC).
- **Segments:** AI inference efficiency (IMC), edge sparse compute (neuromorphic), HPC/crypto/chemistry (quantum, long-term).
- **Drivers:** Energy wall, defense, sovereign quantum programs, error-correction progress.
- **Bottlenecks:** Analog accuracy/PVT + software (IMC); qubit error rates/scaling (quantum); programming models (neuromorphic).
- **Competitive:** Digital GPUs dominate near-term; non-vN must beat them on energy/$ at acceptable accuracy.
- **Risks:** Long timelines, capital intensity, software immaturity, binary outcomes.

### 2026 Update — quantum got a funding wave and a vertical-integration move (2026-08-13)

- **Q2 2026 was an exceptional quarter for quantum financing: 21 companies raised, six of them $100M or more**, spanning superconducting, spin, neutral-atom and ion-trap modalities plus the supply layer — cryogenic control electronics, qubit fabrication services, test and networking [TO VERIFY]. The capital is now spread across the *supply chain*, not just the qubit companies, which is the healthier structure for venture returns.
- **IonQ agreed to acquire SkyWater Technology (~$1.8B, January 2026)** to own manufacturing — the first vertical-integration move of this size by a quantum company (see [13](13_foundry_packaging_and_chiplet_integration.md)). IonQ reported Q1 2026 revenue of ~$64.7M against ~$7.6M a year earlier [TO VERIFY].
- **The cryo-electronics layer is producing spinouts:** **FrostByte**, a 2025 spin-out from **QuTech at TU Delft**, builds cryogenic ICs and control electronics operating alongside the quantum processor — the specific bottleneck between hundreds and thousands of qubits. This is exactly the "supply-layer picks and shovels" position this category's thesis favors over qubit bets.
- **PsiQuantum** remains the capital-intensive photonic FT bet, with roughly $665M–$1.3B cited across sources [TO VERIFY — figures diverge widely; reconcile before use] and reported participation in a proposed US government investment program.
- **Analog/in-memory compute (the near-term half of this category) is quieter.** EnCharge AI shipped **EN100** — an M.2/PCIe analog in-memory accelerator claiming 200+ TOPS in an ~8.25W envelope and ~20x perf/W versus digital alternatives — but has **no disclosed round since the ~$100M Series B**, total ~$144M plus an $18.6M DARPA grant [TO VERIFY]. No 2026 financing news surfaced for **Rain AI**, **Sagence** or **Mythic** in this refresh; treat all three as **[NO PUBLIC DATA] pending verification**, and note that silence in a category this capital-hungry is itself a signal to check on.
- **Contrast worth holding:** digital in-memory compute (d-Matrix, ~$450M raised) and photonic compute (OLIX, $312M) both raised large rounds in this window while analog IMC did not. The market is funding *deterministic* alternatives to the von Neumann bottleneck and discounting analog-precision approaches.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| EnCharge AI | US | 2022 | Series B | ~$144M+ [TO VERIFY] | Tiger Global, RTX, In-Q-Tel | Analog in-memory AI accelerator | Edge+DC inference | Charge-domain analog IMC (high accuracy) | Sampling; defense | High | Active |
| Sagence AI | US | 2018 | Series A+ | [TO VERIFY] | [TO VERIFY] | Analog in-memory inference | DC inference | Analog compute for LLM efficiency | Early | Medium-High | Active |
| Mythic | US | 2012 | Series C (restructured) | ~$165M+ [TO VERIFY] | DCVC, Lux, SoftBank | Analog matrix processor (flash IMC) | Edge inference | Flash-based analog compute | Restructured/relaunched | Medium | Active |
| Rain AI | US | 2017 | Series B [TO VERIFY] | ~$60M+ [TO VERIFY] | Prosperity7, S. Altman | Compute-in-memory NPU | Edge/DC inference | Analog/digital IMC | Early | Medium | Active |
| PsiQuantum | US | 2016 | Growth | ~$1.3B+ [TO VERIFY] | BlackRock, Temasek, BlackBird | Photonic fault-tolerant quantum | Quantum computing | Silicon-photonic FT quantum at scale | Gov megaprojects (AU/US) | Medium | Active |
| SEEQC | US | 2019 | Series B | ~$80M+ [TO VERIFY] | LG, EQT, M Ventures | Digital quantum control (cryo-CMOS) | Quantum control | Single-chip cryogenic control | Partnerships | Medium | Active |
| Quantum Machines | IL | 2018 | Series B+ | ~$170M+ [TO VERIFY] | Red Dot, Intel Cap | Quantum control/orchestration (OPX) | Quantum control | Quantum controller + software | Broad install base | Medium | Active |
| Innatera | NL | 2020 | Series A+ | ~$25M+ [TO VERIFY] | InnovationQuarter, MIG | Neuromorphic spiking processor | Ultra-low-power edge | Analog spiking neural net chip | Early | Medium | Active |

## 4. Company Profiles

### EnCharge AI
- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2022 · **Founders:** Naveen Verma (Princeton), Kailash Gopalakrishnan (ex-IBM), Echere Iroaga
- **Stage:** Series B · **Total Funding:** ~$144M+ [TO VERIFY] · **Last Round:** ~$100M Series B, 2024, led by Tiger Global; backers incl. RTX Ventures, In-Q-Tel, Samsung, HH, ACVC · **Website:** encharge.ai
- **Primary:** 14 · **Secondary:** 02/03 · **One-Line:** Charge-domain analog in-memory compute accelerator delivering dramatically higher energy-efficiency (TOPS/W) for AI inference from edge to datacenter.
- **Tech:** switched-capacitor charge-domain IMC (metal-cap based) that sidesteps the accuracy/PVT problems of current/resistive analog IMC; full software stack. **Differentiation:** robust, precise analog IMC + Princeton research lineage; defense/strategic backing. **Risk:** software maturity, scaling to largest models, analog productization.
- **VC view:** High (best near-term non-vN bet). **Acquirers:** NVIDIA/Intel/defense/hyperscalers. **Data quality:** Medium. **Last updated:** 2026-06-09.

### PsiQuantum
- **Status:** Active · **HQ:** Palo Alto, US · **Founded:** 2016 · **Founders:** Jeremy O'Brien, Terry Rudolph, Mark Thompson, Pete Shadbolt
- **Stage:** Growth · **Total Funding:** ~$1.3B+ [TO VERIFY] · **Investors:** BlackRock, Temasek, Baillie Gifford, M12, Blackbird; plus large government commitments (Australia, US/Illinois) [TO VERIFY] · **Website:** psiquantum.com
- **Primary:** 14 · **One-Line:** Building a utility-scale, fault-tolerant quantum computer using silicon photonics and conventional semiconductor manufacturing (GlobalFoundries partnership).
- **Tech:** photonic qubits manufacturable in a standard fab; betting on error-corrected scale over near-term NISQ. **Differentiation:** manufacturability + fault-tolerance focus. **Risk:** the hardest moonshot in the database; timeline + physics risk. **VC view:** Medium (moonshot, strategic/sovereign capital). **Data quality:** Medium. **Last updated:** 2026-06-09.

> Sagence, Mythic, Rain (analog IMC); SEEQC, Quantum Machines (quantum control); Innatera (neuromorphic) at table level. BrainChip (public, neuromorphic) and GrAI Matter (acquired, see [03](03_edge_inference_chips.md)) noted for completeness.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Analog in-memory compute | High | Very High | Medium-High | Medium | Real (near-term) | Medium-High |
| Digital in-memory compute | High | High | Medium | Medium | Real | Medium-High |
| Neuromorphic/sparse | Medium | High | Medium | Low | Niche (needs app) | Medium |
| Fault-tolerant quantum | Long-term | Extreme | Very High | Low | Moonshot | Medium |
| Quantum control electronics | Medium | High | Medium | Medium | Real (picks/shovels) | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Tiger Global | Crossover | EnCharge | B | Led EnCharge B | Energy-efficient inference |
| In-Q-Tel / RTX Ventures | Strategic (defense) | EnCharge | B | EnCharge | Defense efficiency |
| BlackRock/Temasek | Crossover/Sovereign | PsiQuantum | Growth | Quantum | Moonshot patience |
| Intel Capital | Strategic | Quantum Machines | B | Control | Quantum stack |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Naveen Verma | Princeton | Charge-domain IMC | EnCharge origin; robust analog IMC | Confirmed (EnCharge) | IMC papers/patents | 5 | High |
| H.-S. Philip Wong | Stanford | Emerging memory/IMC | RRAM/IMC device leadership | Likely | Many | 5 | High |
| Kaushik Roy | Purdue | Neuromorphic/IMC | Sparse/neuromorphic compute | Watchlist | Many | 4 | Medium |
| Quantum hardware groups | MIT/Maryland/UCSB/Delft | Qubits, error correction | Quantum founder pipeline | Watchlist/Confirmed | Many | 4 | Medium |

## 8. Diligence Questions
- **Technical (IMC):** Accuracy at INT4/8 vs. digital; PVT robustness; software stack; energy/token measured?
- **Technical (quantum):** Logical-qubit roadmap, error rates, manufacturability?
- **Market:** Which workload pulls first; near-term revenue vs. moonshot?
- **Customer:** Defense/strategic/cloud commitments?
- **Competitive:** Beats digital GPU on energy/$ at usable accuracy?
- **Financial:** Capital to milestone; strategic/sovereign backing?
- **Founder:** device + systems + software depth? **Exit:** strategic acquirer; binary outcome sizing?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | 0 | Initial build; EnCharge/PsiQuantum profiles; IMC/quantum/neuromorphic coverage | Company sites, academic, trade press |
| 2026-08-13 | Full refresh | 1 (FrostByte) | 3 (EnCharge, IonQ/quantum context, analog IMC status) | 0 | Q2 2026 quantum funding wave (21 raises, six ≥$100M) spread across the supply layer; IonQ→SkyWater vertical integration; FrostByte cryo-electronics spinout added; flagged that analog IMC (Rain, Sagence, Mythic) produced no verifiable 2026 financing news while digital IMC and photonic compute raised large rounds | Company releases, trade press [many TO VERIFY] |
