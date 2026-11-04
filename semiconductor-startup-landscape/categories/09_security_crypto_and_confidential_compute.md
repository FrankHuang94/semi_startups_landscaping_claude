---
category_id: "09"
category_name: "Security, Crypto & Confidential Compute"
primary_datacenter_relevance: "Medium"
vc_relevance: "Medium"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 7
active_companies: 7
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$500M+ [ESTIMATED]"
top_investors: ["Blockchain Capital", "1kx", "Fusion Fund", "Northern Gritstone", "SoftBank", "Polychain", "In-Q-Tel"]
key_technical_inflections: ["FHE silicon tape-outs (Samsung 8nm, photonic)", "ZK proof acceleration", "Confidential compute for AI (TEEs/GPU CC)", "Post-quantum crypto (ML-KEM/ML-DSA) hardware IP", "New FHE schemes lowering overhead"]
key_open_questions: ["Do ZK/FHE workloads scale enough to need ASICs?", "Does confidential/encrypted AI become mandatory?", "Crypto-market dependence risk?", "Who consolidates PQC IP (chipmakers vs. security vendors)?"]
---

# 09 — Security, Crypto & Confidential Compute

> Emerging and partly speculative: confidential computing for AI and crypto-acceleration (ZK/FHE) are venture-shaped if those workloads scale. 2025–26 saw FHE move from research toward silicon (Niobium on Samsung 8nm via SEMIFIVE; Optalysys photonic + digital FHE nodes) and PQC IP become a compliance-driven market. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis
- **Why now:** ZK rollups and FHE are compute-bound; confidential computing (TEEs, GPU confidential compute) is becoming a requirement for regulated/sovereign AI; PQC migration deadlines (NIST FIPS 203/204/205, CNSA 2.0) are now pulling PQC IP into every new SoC.
- **Venture-scale:** Medium — FHE accelerators and PQC IP can be venture-scale if encrypted-AI workloads materialize; crypto-market dependence remains the key risk for ZK-hardware plays (Cysic shifted to a token-network model).
- **Inflections (2026 update):** FHE ASIC tape-outs reaching commercial foundry nodes (Niobium/SEMIFIVE/Samsung 8LPU, Feb 2026 [CONFIRMED]); encrypted-LLM demos (Cornami + DESILO, Sept 2025 [TO VERIFY]); new FHE schemes (Gentry–Lee "GL" scheme, Mar 2026 [TO VERIFY]) that could shift the HW/SW balance; PQC IP licensing into MCUs (PQShield–Microchip [TO VERIFY]).
- **Acquirers:** NVIDIA, Intel, Arm, Synopsys/Cadence (security IP), Rambus, crypto infra, cloud providers, defense primes. **Exit:** strategic M&A.
- **Winning startup:** FHE/ZK accelerator with software + a real workload anchor (regulated data / government), or PQC IP with certifications (FIPS 140-3) and MCU/SoC design wins. **Non-investable:** generic security IP vs. Arm/Synopsys; pure crypto-cycle bets.

## 2. Market Context
- **Structure:** Security IP incumbents (Arm, Synopsys, Rambus), confidential-compute (Intel TDX, NVIDIA Blackwell/Rubin CC, AMD SEV-SNP), FHE/ZK silicon startups, PQC IP specialists (PQShield and others).
- **Segments:** Blockchain infra (ZK), privacy-preserving / encrypted AI (FHE), regulated & sovereign cloud, defense, PQC for embedded/IoT.
- **Drivers:** Sovereign-AI data-residency, privacy regulation, AI data confidentiality, PQC mandates and "harvest-now-decrypt-later" risk, quantum-computing progress (see [14](14_quantum_neuromorphic_and_non_von_neumann.md)).
- **Bottlenecks:** FHE overhead (still orders of magnitude vs. plaintext), ZK prover cost, compilers/toolchains, standards.
- **Funding signal (2025–26):** Niobium $23M+ follow-on (Dec 2025) [CONFIRMED]; Optalysys £23M Series A extension (Jan 2026) [CONFIRMED]; otherwise sparse — the category remains small vs. AI compute.
- **Competitive:** GPUs still do most ZK proving; FHE ASICs emerging; confidential compute is incumbent-led.
- **Risks:** Crypto-cycle dependence, workload uncertainty, incumbent internalization, algorithmic advances shrinking the need for dedicated HW.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Fabric Cryptography | US | 2022 | Series A | ~$39M [CONFIRMED] ($6M seed + $33M Series A, Aug 2024) | Blockchain Capital, 1kx (co-leads); Metaplanet (seed) | VPU (crypto-acceleration chip) | ZK/MPC/FHE compute | Programmable crypto-native ISA | No new round found 2025–26 [TO VERIFY] | Medium | Active |
| Niobium | US (Dayton, OH) | 2023 | Seed+ (follow-on) | ~$28M+ [CONFIRMED] | Fusion Fund, Morgan Creek, Rev1, Ohio Innovation Fund | FHE accelerator ASIC | FHE compute / encrypted AI | DARPA DPRIVE lineage; 2nd-gen platform on Samsung 8LPU | SEMIFIVE design contract ~KRW10B (Feb 2026) [CONFIRMED] | Medium-High | Active |
| Optalysys | UK (Leeds) | 2013 | Series A (ext.) | ~£44M (~$59M) [ESTIMATED] (£21M A 2023 + £23M ext. Jan 2026 [CONFIRMED]) | Northern Gritstone, imec.xpand, Lingotto Horizon, NSSIF | Photonic compute + LightLocker FHE nodes | FHE / secure cloud compute | Silicon-photonic acceleration; US expansion | LightLocker Node shipping (company claim) | Medium | Active |
| Cornami | US | 2011 [TO VERIFY] | Series C+ | ~$150M+ [TO VERIFY] ($50M C led by SoftBank; $68M round 2022 [CONFIRMED]) | SoftBank, [TO VERIFY] | Mx2 FracTLcore FHE compute fabric | Encrypted AI / FHE | Reconfigurable fabric; Craig Gentry as Chief Scientist | DESILO encrypted-LLM collaboration (Sept 2025) [TO VERIFY] | Medium | Active |
| PQShield | UK (Oxford) | 2018 | Series B | ~$63M [TO VERIFY] ($37M Series B, 2024) | Addition [TO VERIFY] | PQC hardware + software IP | SoC/MCU vendors, government | FIPS 140-3-ready PQC IP; side-channel hardened | Microchip licensee; Carahsoft US-gov distribution; Tech Nation Future Fifty 2026 [TO VERIFY] | Medium | Active |
| Cysic | US | 2022 | Seed/pre-A + token | ~$18M [TO VERIFY] ($6M seed Polychain + $12M pre-A HashKey/OKX, May 2024) | Polychain, HashKey, OKX Ventures | ZK proving network + planned ZK ASICs | ZK proving | Hardware-backed decentralized prover; CYS token | CYS token live (2025–26); ASIC timelines unverified | Low-Medium | Active |
| Chain Reaction | IL | 2017 | Series C | ~$140M+ [TO VERIFY] | Morgan Creek, KCK | 3PU FHE/blockchain chips | FHE + crypto compute | FHE acceleration silicon | Mining→FHE pivot; no 2026 update found | Medium | Active |

## 4. Company Profiles

### Niobium (new profile)
- **Status:** Active · **HQ:** Dayton, Ohio, US · **Founded:** 2023 · **Website:** niobiummicrosystems.com
- **Stage:** Seed + oversubscribed follow-on · **Total Funding:** ~$28M+ [CONFIRMED] · **Last Round:** $23M+ follow-on, announced Dec 2025, backers incl. Fusion Fund, Morgan Creek, Rev1 Ventures, Ohio Innovation Fund [CONFIRMED]; prior $5.5M (May 2024, Fusion Fund-led) [CONFIRMED]
- **Primary:** 09 · **One-Line:** FHE accelerator ASIC built from DARPA DPRIVE program work, aimed at making computation on encrypted data practical for cloud/AI.
- **Milestones:** Feb 2026 — SEMIFIVE announced a ~KRW10B (~$6.9M) contract to develop Niobium's FHE accelerator on Samsung Foundry 8nm (8LPU) [CONFIRMED]. Funds directed to 2nd-gen FHE platform (HW/SW co-design, compiler).
- **Risk:** FHE workload adoption timing; competition from algorithmic advances (new schemes) and GPU FHE libraries. **VC view:** Medium-High (best-funded US FHE-silicon pure play). **Data quality:** Medium-High. **Last updated:** 2026-11-04.

### Fabric Cryptography
- **Status:** Active · **HQ:** San Francisco, US · **Founded:** 2022 · **Founders:** Michael Gao, Tina Ju
- **Stage:** Series A · **Total Funding:** ~$39M [CONFIRMED] · **Last Round:** $33M Series A (Aug 2024) co-led by Blockchain Capital and 1kx, with Offchain Labs, Polygon, Matter Labs; $6M seed led by Metaplanet [CONFIRMED] · **Website:** fabriccryptography.com
- **Primary:** 09 · **One-Line:** "Verifiable Processing Unit" (VPU) — a programmable chip purpose-built to accelerate cryptography (ZK proofs, MPC, FHE).
- **Tech:** crypto-native ISA accelerating modular arithmetic/NTT across ZK/FHE. **Differentiation:** programmability across crypto primitives vs. single-algorithm ASICs. **Risk:** workload scale + crypto-cycle dependence; no new round or production-volume disclosure found in 2025–26 searches — re-check runway [TO VERIFY].
- **VC view:** Medium (high-variance; downgraded from Medium-High given no visible 2025–26 momentum). **Acquirers:** crypto infra, NVIDIA/Intel. **Data quality:** Medium. **Last updated:** 2026-11-04.

### Optalysys
- **Status:** Active · **HQ:** Leeds, UK · **Founded:** 2013 · **Stage:** Series A extension · **Funding:** £21M Series A (2023) led by Northern Gritstone with imec.xpand, Lingotto Horizon, NSSIF; £23M (~$31M) extension Jan 2026 [CONFIRMED] · **Total:** ~£44M [ESTIMATED]
- **One-Line:** Silicon-photonic compute aimed at FHE/encrypted workloads, with digital FHE acceleration already shipping in LightLocker Node servers (company claim). Extension funds production scale-up and US expansion. **VC view:** Medium. **Data quality:** Medium. **Last updated:** 2026-11-04.

> Cornami, PQShield, Cysic, Chain Reaction at table level.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| ZK proof acceleration | Medium | High | Medium | Medium | Real (cycle-dependent; tokenized models) | Low-Medium |
| FHE hardware | Medium (rising) | Very High | High | Low | High-variance; first commercial-node tape-outs | Medium |
| Confidential compute IP | Medium-High | High | Medium | High (Intel/NVDA/AMD) | Narrow | Low-Medium |
| Post-quantum crypto IP | Medium-High (mandates) | High | Low-Medium | Medium-High | Real (compliance-driven) | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Blockchain Capital / 1kx | VC (crypto) | Fabric Cryptography | Seed–A | Fabric (2024) | Crypto compute |
| Fusion Fund / Morgan Creek / Rev1 | VC | Niobium (Morgan Creek also Chain Reaction) | Seed–A | Niobium $23M+ (Dec 2025) | FHE silicon |
| Northern Gritstone / imec.xpand / NSSIF | VC / sovereign | Optalysys | A | £23M ext. (Jan 2026) | UK secure/photonic compute |
| SoftBank | Strategic/crossover | Cornami | C | — | FHE fabric |
| Polychain / HashKey / OKX | VC (crypto) | Cysic | Seed–A | Token launch | ZK infra |
| In-Q-Tel | Strategic (gov) | (confidential/FHE) | Seed–B | — | Defense privacy |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| DARPA DPRIVE alumni | Multiple | FHE acceleration | Government-funded FHE HW base (Niobium lineage) | Confirmed (Niobium) | DPRIVE outputs | 4 | Medium |
| Craig Gentry | Cornami / DESILO collab | FHE schemes | Inventor of FHE; GL scheme (Mar 2026) [TO VERIFY] could reshape HW requirements | Watchlist | Many | 4 | Medium |
| Crypto-HW academics | MIT/Berkeley/EPFL | ZK/FHE primitives | Define algorithms → silicon | Watchlist | Many | 3 | Medium |

## 8. Diligence Questions
- **Technical:** Speedup vs. GPU FHE/ZK libraries on target primitive; programmability; compiler maturity; robustness to scheme changes (e.g., new FHE schemes)?
- **Market:** Workload scale + durability (not just crypto cycle)? Which regulated buyer pays first?
- **Customer:** Proving-network/cloud/government commitments?
- **Competitive:** Defensible vs. GPU + incumbent confidential compute + PQC IP from Synopsys/Rambus?
- **Financial:** Capital to tape-out (Samsung 8nm ~ $7M design contract benchmark); revenue model (chip vs. node vs. token)? **Founder:** crypto + silicon depth?
- **Exit:** strategic acquirer beyond crypto market?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 5 | 0 | 0 | Initial build; Fabric profile; ZK/FHE/confidential coverage | Company sites, trade press |
| 2026-11-04 | Full (Refresh #3) | 2 (Cornami, PQShield) | 5 | 0 | Niobium $23M+ follow-on (Dec 2025) + SEMIFIVE/Samsung 8nm FHE contract (Feb 2026); Optalysys £23M ext. (Jan 2026); Fabric funding corrected to ~$39M; Cysic corrected to ~$18M + token; Niobium & Optalysys profiles; PQC subsegment upgraded. Web search budget exhausted before PQShield/Cornami deep-verify | Niobium PR (accessnewswire), iconnect007 (SEMIFIVE), BusinessCloud/IntelligentCIO (Optalysys), The Block/SecurityWeek (Fabric), SiliconANGLE (Cornami 2022), PQShield newsroom |
