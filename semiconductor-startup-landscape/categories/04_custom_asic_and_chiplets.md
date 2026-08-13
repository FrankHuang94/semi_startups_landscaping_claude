---
category_id: "04"
category_name: "Custom ASIC & Chiplets"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-08-13"
refresh_count: 2
total_companies: 9
active_companies: 8
archived_companies: 1
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$1.6B+ [ESTIMATED]"
top_investors: ["Seligman Ventures", "Atreides", "Matrix Partners", "Intel Capital", "Arm", "AMD", "Cisco Investments", "MediaTek"]
key_technical_inflections: ["UCIe / die-to-die interconnect", "Chiplet disaggregation", "RISC-V server platforms", "Custom silicon proliferation", "Electro-optical die-to-die and rack-to-rack links", "Lab-commissioned merchant ASICs (OpenAI/Broadcom)"]
key_open_questions: ["Does an open chiplet marketplace emerge?", "Can RISC-V take server share?", "Who owns the D2D IP layer?", "With Rivos inside Meta and Alphawave inside Qualcomm, is the independent custom-silicon layer consolidating faster than it is forming?"]
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

### 2026 Update — what changed since the last refresh (2026-08-13)

- **Rivos was acquired by Meta (announced 2025-10, reported ~$2B)** — archived here. Rivos had completed its design and handed it to TSMC for trial production; Meta bought the team to accelerate MTIA. 2026 reporting describes the integration as difficult. This is now the reference comparable for "hyperscaler buys the whole silicon team."
- **Eliyan became a unicorn and moved into optics.** ~$50M strategic round in January 2026 (**AMD, Arm, Coherent, Meta**), then a **~$145M Series C at ~$1B led by Seligman Ventures with Cisco Investments and Lumentum** (2026-07-29), taking total funding to ~$295M. The product story extended from NuLink die-to-die PHY to **NuGear** electro-optical links spanning die-to-die, chip-to-chip and **rack-to-rack**, targeting roughly 1.6–12.8 Tbps per link on standard packaging. The cap table now contains four potential acquirers.
- **SiFive re-rated as the RISC-V datacenter bet.** $400M Series G at ~$3.65B (2026-04-09) led by **Atreides** with **NVIDIA**, Apollo, D1, T. Rowe and Capital Group; ~$970M raised in total, 10B+ cores shipped and 500+ designs in production. Added to this category as the incumbent-scale RISC-V IP player.
- **Qualcomm closed Alphawave ($2.4B)** and put its CEO in charge of Qualcomm's datacenter business — removing the largest independent SerDes/chiplet-IP vendor from the market and creating a new acquirer for the rest. **GlobalFoundries acquired Synopsys's ARC processor IP business**, adding another IP consolidator.
- **The demand-side proof point:** OpenAI and Broadcom's **"Jalapeño"** went from design to tape-out in ~9 months (unveiled 2026-06-24) inside a 10GW program. Custom silicon is no longer a hyperscaler-only capability — it is available to any buyer with enough volume, which is exactly the tailwind this category's IP and fabric vendors sell into.
- **Net read:** the enablement-layer thesis is working (Eliyan, Baya, SiFive all up), but the independent *platform* players keep being absorbed (Rivos → Meta, Alphawave → Qualcomm, ARC IP → GF). Prefer the picks-and-shovels layer; expect it to be bought.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Eliyan | US | 2021 | **Series C (2026-07) — unicorn** | ~$295M [TO VERIFY] | Seligman Ventures, Cisco, Lumentum, AMD, Arm, Coherent, Meta | NuLink D2D PHY + NuGear (electro-optical) | Chiplet + rack-to-rack interconnect | UCIe-class D2D on standard packaging; now optical links | ~$1B valuation; strategic-heavy cap table | High | Active |
| Baya Systems | US | 2022 | Series B | ~$57M+ [TO VERIFY] | Matrix, Maverick, Intel Cap | NoC / chiplet fabric IP (WeaveIP) | SoC/chiplet builders | Software-driven NoC + chiplet fabric | IP licensing deals | High | Active |
| Rivos | US | 2021 | **Acquired (Meta, 2025-10)** | ~$250M+ raised | Matrix, Intel Cap, MediaTek, Dell | RISC-V data-analytics + GenAI server SoC | (now Meta MTIA) | RISC-V + integrated GPGPU/HBM | **~$2B reported acquisition; design handed to TSMC pre-close** | Archived | Acquired |
| SiFive | US | 2015 | **Series G (2026-04)** | ~$970M [TO VERIFY] | Atreides, NVIDIA, Apollo, D1, T. Rowe | RISC-V core IP incl. datacenter/AI portfolio | SoC + DC builders | Largest RISC-V IP install base (10B+ cores shipped) | ~$3.65B valuation; pre-IPO posture | High | Active |
| Ventana Micro | US | 2018 | Series C [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | Veyron RISC-V server CPU chiplets | DC/edge servers | High-perf RISC-V chiplet CPU IP | IP/chiplet customers | High | Active |
| AheadComputing | US | 2024 | Seed 2 | ~$30M+ [TO VERIFY] | Eclipse Ventures, Toyota Ventures, Cambium | 64-bit RISC-V application-processor IP | SoC builders | Ex-Intel core-design team; per-core performance focus | Early IP engagements | Medium-High | Active |
| Blue Cheetah | US | 2018 | Series A+ | [TO VERIFY] | [TO VERIFY] | Customizable D2D IP | Chiplet builders | Portable D2D PHY across nodes | IP deals | Medium-High | Active |
| zeroASIC | US | 2021 | Seed/A | [TO VERIFY] | [TO VERIFY] | Composable chiplets + open EDA | Chiplet marketplace | Open chiplet platform | Early | Medium | Active |
| Akeana | US | 2021 | Series A+ | ~$100M+ [TO VERIFY] | [TO VERIFY] | RISC-V IP portfolio | SoC builders | Broad RISC-V core IP | Early licensing | Medium | Active |

## 4. Company Profiles

### Eliyan
- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2021 · **Founders:** Ramin Farjadrad (CEO), Syrus Ziai
- **Stage:** Series C · **Total Funding:** **~$295M** [TO VERIFY] · **Round history:** $40M A (2022-11) → $60M B (2024-03) → **~$50M strategic (2026-01: AMD, Arm, Coherent, Meta)** → **~$145M Series C at ~$1B, 2026-07-29, led by Seligman Ventures** with Cisco Investments and Lumentum · **Investors:** Seligman, Cisco, Lumentum, AMD, Arm, Coherent, Meta, Tiger Global, Samsung Catalyst, Micron, Intel Capital · **Website:** eliyan.com
- **Primary:** 04 · **Secondary:** 13 Packaging, 06 Optical · **One-Line:** NuLink die-to-die interconnect PHY enabling chiplets on standard organic substrates — now extended to **NuGear** electro-optical links for chip-to-chip and rack-to-rack.
- **Tech:** UCIe-compatible D2D PHY with high bandwidth/energy on cheaper organic packaging; memory-interconnect ("UMI") concepts for HBM disaggregation; **NuGear** targets roughly 1.6–12.8 Tbps links across accelerator and memory-expansion topologies [TO VERIFY]. **Differentiation:** removes interposer cost/supply bottleneck — directly attacks the CoWoS constraint — and now spans the copper-to-optical boundary that [06](06_optical_interconnect_and_cpo.md) is built on.
- **VC view:** High. **The cap table is the story:** AMD, Arm, Meta, Cisco, Lumentum, Coherent, Samsung and Micron are all in, which is simultaneously the strongest possible validation and a crowded ROFR problem. **Risk:** UCIe ecosystem competition (Synopsys/Cadence PHY), and now competition with its own strategic investors in optical links. **Data quality:** Medium. **Verify next:** NuGear customer commitments, licensing revenue. **Last updated:** 2026-08-13.

### Rivos — ARCHIVED (acquired by Meta, 2025-10)
- **Status:** **Archived — acquired by Meta, announced October 2025, reported at ~$2B** [ESTIMATED — terms undisclosed] · **HQ:** Mountain View, US · **Founded:** 2021
- **Stage at exit:** Series A+ (large) · **Total Funding:** ~$250M+ raised · **Investors:** Matrix, Intel Capital, MediaTek, Dell, Koch [TO VERIFY] · **Website:** rivosinc.com
- **Primary:** 04 · **Secondary:** 01/02 · **One-Line:** RISC-V server SoC integrating high-performance CPUs with GPGPU/AI acceleration and HBM for data analytics + GenAI.
- **Outcome:** Rivos completed its design and handed it to TSMC for trial production, with an AI chip targeted for as early as 2026; Meta acquired the company to accelerate MTIA and reduce NVIDIA dependence. **Reported at roughly 8x invested capital, pre-revenue.**
- **Post-close note:** 2026 reporting describes integration difficulties inside Meta's silicon organization [TO VERIFY]. Relevant to how earnouts and retention should be structured in team-acquisition outcomes. **Data quality:** Medium. **Last updated:** 2026-08-13.

> Baya Systems, Ventana, SiFive, AheadComputing, Blue Cheetah, zeroASIC and Akeana are covered at table level. **Astera Labs** (D2D/connectivity, now public) is profiled in [05](05_networking_and_interconnect.md).

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
| 2026-08-13 | Full refresh | 2 (SiFive, AheadComputing) | 2 (Eliyan, market context) | 1 (Rivos → Meta) | Rivos archived after Meta's ~$2B acquisition; Eliyan to unicorn on a $145M Series C with an all-strategic cap table and the NuGear electro-optical line; SiFive added at ~$3.65B after a $400M Series G; Qualcomm/Alphawave and GF/Synopsys-ARC consolidation and the OpenAI/Broadcom "Jalapeño" demand proof added to context | Company releases, trade press [many TO VERIFY] |
