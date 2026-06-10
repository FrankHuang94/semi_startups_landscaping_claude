---
category_id: "04"
category_name: "Custom ASIC & Chiplets"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-06-09"
refresh_count: 1
total_companies: 7
active_companies: 7
archived_companies: 0
stealth_or_semi_stealth_companies: 1
total_disclosed_funding: "~$700M+ [ESTIMATED]"
top_investors: ["Matrix Partners", "Intel Capital", "Mayfield", "MediaTek"]
key_technical_inflections: ["UCIe / die-to-die interconnect", "Chiplet disaggregation", "RISC-V server platforms", "Custom silicon proliferation"]
key_open_questions: ["Does an open chiplet marketplace emerge?", "Can RISC-V take server share?", "Who owns the D2D IP layer?"]
---

# 04 — Custom ASIC & Chiplets

> Sell the enablement layer for the custom-silicon boom rather than betting on one chip. High-conviction, capital-efficient. See [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis
- **Why now:** Every hyperscaler and AI lab wants custom silicon; UCIe + chiplet disaggregation creates a new IP/tooling/services market.
- **Venture-scale:** High via D2D interconnect IP/fabric, RISC-V server platforms, and turnkey chiplet design — IP leverage beats pure services.
- **Inflections:** UCIe standardization, die-to-die PHY/fabric, chiplet economics, RISC-V server momentum.
- **Likely acquirers:** Broadcom, Marvell, Synopsys, Cadence, Arm, hyperscalers. **Exit:** strategic M&A.
- **Winning startup:** owns reusable IP (interconnect fabric, NoC, D2D PHY) or a RISC-V platform with software. **Non-investable:** pure design-services body shop without IP.

## 2. Market Context
- **Structure:** Merchant ASIC (Broadcom, Marvell, Alchip, GUC) + IP (Arm, Synopsys, Cadence) + chiplet/D2D startups + RISC-V challengers.
- **Segments:** Hyperscaler custom AI silicon, networking ASICs, sovereign chips, automotive.
- **Drivers:** Cost/perf of custom vs. merchant GPU; reticle limits → chiplets; supply diversification.
- **Bottlenecks:** D2D bandwidth/energy, packaging, NoC scalability, verification.
- **Competitive:** Broadcom/Marvell dominate merchant ASIC; startups attack the IP/fabric layer.
- **Risks:** Incumbent IP bundling, long sales cycles, packaging dependence.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Eliyan | US | 2021 | Series B | ~$100M+ [TO VERIFY] | Tiger Global, Samsung, Micron, Intel Cap | NuLink D2D PHY (organic substrate) | Chiplet interconnect | UCIe-class D2D without silicon interposer | Samsung/Micron strategic | High | Active |
| Baya Systems | US | 2022 | Series B | ~$57M+ [TO VERIFY] | Matrix, Maverick, Intel Cap | NoC / chiplet fabric IP (WeaveIP) | SoC/chiplet builders | Software-driven NoC + chiplet fabric | IP licensing deals | High | Active |
| Rivos | US | 2021 | Series A+ | ~$250M+ [TO VERIFY] | Matrix, Intel Cap, MediaTek, Dell | RISC-V data-analytics + GenAI server SoC | DC servers | RISC-V + integrated GPGPU/HBM | Stealth-ish; large raise | High | Semi-Stealth |
| Ventana Micro | US | 2018 | Series C [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | Veyron RISC-V server CPU chiplets | DC/edge servers | High-perf RISC-V chiplet CPU IP | IP/chiplet customers | High | Active |
| Blue Cheetah | US | 2018 | Series A+ | [TO VERIFY] | [TO VERIFY] | Customizable D2D IP | Chiplet builders | Portable D2D PHY across nodes | IP deals | Medium-High | Active |
| zeroASIC | US | 2021 | Seed/A | [TO VERIFY] | [TO VERIFY] | Composable chiplets + open EDA | Chiplet marketplace | Open chiplet platform | Early | Medium | Active |
| Akeana | US | 2021 | Series A+ | ~$100M+ [TO VERIFY] | [TO VERIFY] | RISC-V IP portfolio | SoC builders | Broad RISC-V core IP | Early licensing | Medium | Active |

## 4. Company Profiles

### Eliyan
- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2021 · **Founders:** Ramin Farjadrad (CEO), Syrus Ziai
- **Stage:** Series B · **Total Funding:** ~$100M+ [TO VERIFY] · **Investors:** Tiger Global (Series B lead), Samsung Catalyst, Micron, Intel Capital, Cleveland Avenue · **Website:** eliyan.com
- **Primary:** 04 · **Secondary:** 13 Packaging · **One-Line:** NuLink die-to-die interconnect PHY enabling chiplets on standard organic substrates (no silicon interposer).
- **Tech:** UCIe-compatible D2D PHY with high bandwidth/energy on cheaper organic packaging; also memory-interconnect ("UMI") concepts for HBM disaggregation. **Differentiation:** removes interposer cost/supply bottleneck — directly attacks the CoWoS constraint. **Strategic backing from Samsung+Micron is a strong signal.**
- **VC view:** High; acquirers = packaging/IP incumbents, memory makers. **Risk:** UCIe ecosystem competition (Synopsys/Cadence PHY). **Data quality:** Medium. **Last updated:** 2026-06-09.

### Rivos
- **Status:** Semi-Stealth/Active · **HQ:** Mountain View, US · **Founded:** 2021
- **Stage:** Series A+ (large) · **Total Funding:** ~$250M+ [TO VERIFY] · **Investors:** Matrix, Intel Capital, MediaTek, Dell, Koch [TO VERIFY] · **Website:** rivosinc.com
- **Primary:** 04 · **Secondary:** 01/02 · **One-Line:** RISC-V server SoC integrating high-performance CPUs with GPGPU/AI acceleration and HBM for data analytics + GenAI.
- **Tech:** RISC-V application-class CPU + integrated accelerator + memory; full-stack software. **Differentiation:** open-ISA server platform alternative to x86/Arm + NVIDIA. **Risk:** software ecosystem, execution against giants. **VC view:** High (high-variance). **Acquirers:** hyperscalers, MediaTek. **Data quality:** Low-Medium (stealth). **Last updated:** 2026-06-09.

> Baya Systems, Ventana, Blue Cheetah, zeroASIC, Akeana covered at table level. **Astera Labs** (D2D/connectivity, now public) is profiled in [05](05_networking_and_interconnect.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| D2D / UCIe PHY IP | High | High | Medium | Medium-High | Real | High |
| NoC / chiplet fabric IP | High | High | Medium | Medium | Real | High |
| RISC-V server platforms | Medium-High | Very High | High | High | High-variance | Medium-High |
| Open chiplet marketplace | Medium | High | Medium | Medium | Emerging | Medium |
| RISC-V core IP | Medium | High | Medium | High (Arm) | Real | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Matrix Partners | VC | Rivos, Baya | Seed–B | Multi-deal | Compute infra/IP |
| Intel Capital | Strategic | Eliyan, Rivos, Baya | Seed–Growth | Multi-deal | Chiplet ecosystem |
| MediaTek | Strategic | Rivos | A–Growth | Rivos | ASIC partner play |
| Samsung/Micron | Strategic | Eliyan | B | Eliyan | Memory-interconnect |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Ramin Farjadrad | Industry (Eliyan) | SerDes/D2D | Serial-link pedigree (Aquantia) | Confirmed (Eliyan) | D2D patents | 5 | High |
| Krste Asanović | UC Berkeley | RISC-V | RISC-V ecosystem origin | Confirmed (SiFive) | RISC-V | 5 | High |
| UCLA/CHIPS, Georgia Tech 3D | UCLA/GT | Heterogeneous integration | Chiplet/packaging research base | Watchlist | Many | 4 | Medium |

## 8. Diligence Questions
- **Technical:** D2D bandwidth/energy vs. UCIe/Synopsys? Node portability? Verification IP?
- **Market:** Merchant-ASIC vs. IP-licensing model; attach to which chiplet programs?
- **Customer:** Signed IP licenses/tape-outs vs. evaluations?
- **Competitive:** Defensible vs. Synopsys/Cadence PHY bundling?
- **Financial:** Royalty vs. NRE mix; gross-margin profile?
- **Founder:** Shipped IP at scale? **Exit:** IP-tuck-in logic for EDA/networking incumbents?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 7 | 0 | 0 | Initial build; Eliyan/Rivos profiles; D2D/RISC-V coverage | Company sites, trade press |
