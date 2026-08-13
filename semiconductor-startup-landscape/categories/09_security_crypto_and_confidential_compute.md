---
category_id: "09"
category_name: "Security, Crypto & Confidential Compute"
primary_datacenter_relevance: "Medium"
vc_relevance: "Medium"
last_refreshed: "2026-08-13"
refresh_count: 2
total_companies: 5
active_companies: 5
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$200M+ [ESTIMATED]"
top_investors: ["Blockchain Capital", "Paradigm", "1kx", "In-Q-Tel"]
key_technical_inflections: ["ZK proof acceleration", "FHE hardware", "Confidential compute for AI (TEEs/GPU CC)", "Post-quantum crypto"]
key_open_questions: ["Do ZK/FHE workloads scale enough to need ASICs?", "Does confidential AI become mandatory?", "Crypto-market dependence risk?"]
---

# 09 — Security, Crypto & Confidential Compute

> Emerging and partly speculative: confidential computing for AI and crypto-acceleration (ZK/FHE) are venture-shaped if those workloads scale. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis
- **Why now:** ZK rollups and FHE are compute-bound; confidential computing (TEEs, GPU confidential compute) is becoming a requirement for regulated AI; post-quantum migration looms.
- **Venture-scale:** Medium — ZK/FHE accelerators and confidential-compute IP can be venture-scale if workloads scale; crypto-market dependence is the key risk.
- **Inflections:** ZK proof generation acceleration, FHE bootstrapping hardware, GPU/CPU confidential compute, PQC accelerators.
- **Acquirers:** NVIDIA, Intel, Arm, crypto infra, cloud providers. **Exit:** strategic M&A.
- **Winning startup:** ZK/FHE accelerator with software + a real workload anchor. **Non-investable:** generic security IP vs. Arm/Synopsys; pure crypto-cycle bets.

## 2. Market Context
- **Structure:** Security IP incumbents (Arm, Synopsys, Rambus), confidential-compute (Intel SGX/TDX, NVIDIA CC, AMD SEV), ZK/FHE startups.
- **Segments:** Blockchain infra, privacy-preserving AI, regulated cloud, defense.
- **Drivers:** ZK rollup growth, privacy regulation, AI data confidentiality, PQC mandates.
- **Bottlenecks:** FHE 1000x overhead, ZK prover cost, software/toolchains, standards.
- **Competitive:** GPUs currently do ZK; ASICs emerging; confidential compute is incumbent-led.
- **Risks:** Crypto-cycle dependence, workload uncertainty, incumbent internalization.

### 2026 Update — silicon reached production, demand still unproven (2026-08-13)

- **Fabric Cryptography moved its VPU (Verifiable Processing Unit) toward production** and reports tens of millions of dollars of pre-orders [TO VERIFY]. Its pitch — an ISA built around the mathematical primitives underlying zero-knowledge proofs and FHE rather than a fixed-function accelerator — is the more durable formulation in a category where the target algorithms keep changing.
- **Niobium partnered with SEMIFIVE and Samsung Foundry** to bring what it describes as the first commercially viable **FHE accelerator ASIC** to production [TO VERIFY]. Two independent teams reaching production silicon in the same window is a genuine category milestone.
- **What has *not* changed:** paying demand. Confidential-compute revenue at scale still sits with incumbents (Intel TDX, AMD SEV-SNP, NVIDIA confidential computing), and ZK demand remains tied to the crypto cycle. The bull case now depends on regulated-AI workloads — running inference on encrypted data for healthcare, finance and government — which is a policy-driven timeline, not a technology one.
- **Adjacent signal worth noting:** SambaNova naming a large bank as an inference partner, and the general enterprise push into regulated AI, is the demand pattern that would eventually pull FHE silicon. Track it as a leading indicator rather than assuming it.
- **Underwriting posture:** unchanged at Medium. Fund teams whose silicon is programmable across ZK/FHE/MPC, insist on non-crypto-cycle revenue in the model, and treat 2026's production milestones as de-risking execution, not demand.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Fabric Cryptography | US | 2022 | Series A | ~$33M+ [TO VERIFY] | Blockchain Capital, 1kx | VPU (crypto-acceleration chip) | ZK/MPC/FHE compute | Programmable "crypto-native" processor | Early; high-profile | Medium-High | Active |
| Cysic | US | 2022 | Seed/A | ~$22M+ [TO VERIFY] | Polychain, OKX, HashKey | ZK/FHE acceleration HW | ZK proving | ZK prover ASIC/board | Provider network | Medium | Active |
| Chain Reaction | IL | 2017 | Series C | ~$140M+ [TO VERIFY] | Morgan Creek, KCK | 3PU FHE/blockchain chips | FHE + crypto compute | FHE acceleration silicon | Pivots; mining→FHE | Medium | Active |
| Niobium | US | 2023 | Seed | [TO VERIFY] | [TO VERIFY] | FHE accelerator ASIC | FHE compute | DPRIVE/DARPA lineage FHE | Early | Medium | Active |
| Optalysys | UK | 2013 | Seed/A | [TO VERIFY] | [TO VERIFY] | Optical FHE acceleration | FHE compute | Photonic FHE approach | Research/early | Medium | Active |

## 4. Company Profiles

### Fabric Cryptography
- **Status:** Active · **HQ:** San Francisco, US · **Founded:** 2022 · **Founders:** Michael Gao, Tina Ju
- **Stage:** Series A · **Total Funding:** ~$33M+ [TO VERIFY] · **Investors:** Blockchain Capital, 1kx, Offchain Labs, Inflection · **Website:** fabriccryptography.com
- **Primary:** 09 · **One-Line:** "Verifiable Processing Unit" (VPU) — a programmable chip purpose-built to accelerate cryptography (ZK proofs, MPC, FHE).
- **Tech:** crypto-native ISA accelerating modular arithmetic/NTT across ZK/FHE; aims to be the "GPU of cryptography." **Differentiation:** programmability across crypto primitives vs. single-algorithm ASICs. **Risk:** workload scale + crypto-cycle dependence.
- **VC view:** Medium-High (high-variance). **Acquirers:** crypto infra, NVIDIA/Intel. **Data quality:** Medium. **Last updated:** 2026-06-09.

> Cysic, Chain Reaction, Niobium, Optalysys at table level.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| ZK proof acceleration | Medium-High | High | Medium | Medium | Real (cycle-dependent) | Medium |
| FHE hardware | Medium | Very High | High | Low | High-variance | Medium |
| Confidential compute IP | Medium | High | Medium | High (Intel/NVDA) | Narrow | Low-Medium |
| Post-quantum crypto IP | Medium | High | Medium | High | Niche | Low-Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Blockchain Capital / 1kx | VC (crypto) | Fabric Cryptography | Seed–A | Fabric | Crypto compute |
| Polychain / HashKey | VC (crypto) | Cysic | Seed–A | Cysic | ZK infra |
| In-Q-Tel | Strategic (gov) | (confidential/FHE) | Seed–B | — | Defense privacy |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| DARPA DPRIVE alumni | Multiple | FHE acceleration | Government-funded FHE HW base | Likely | DPRIVE outputs | 4 | Medium |
| Crypto-HW academics | MIT/Berkeley/EPFL | ZK/FHE primitives | Define algorithms → silicon | Watchlist | Many | 3 | Medium |

## 8. Diligence Questions
- **Technical:** Speedup vs. GPU on target primitive; programmability; software stack?
- **Market:** Workload scale + durability (not just crypto cycle)?
- **Customer:** Proving-network/cloud commitments?
- **Competitive:** Defensible vs. GPU + incumbent confidential compute?
- **Financial:** Capital to tape-out; revenue model? **Founder:** crypto + silicon depth?
- **Exit:** strategic acquirer beyond crypto market?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 5 | 0 | 0 | Initial build; Fabric profile; ZK/FHE/confidential coverage | Company sites, trade press |
| 2026-08-13 | Full refresh | 0 | 3 (Fabric, Niobium, market context) | 0 | Fabric's VPU moved toward production with reported pre-orders; Niobium's FHE ASIC entered production with SEMIFIVE/Samsung Foundry; noted that execution de-risked while demand did not — category stays Medium | Company releases, trade press [many TO VERIFY] |
