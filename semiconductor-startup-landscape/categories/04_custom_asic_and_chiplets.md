---
category_id: "04"
category_name: "Custom ASIC & Chiplets"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 9
active_companies: 5
archived_companies: 4
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$1.35B+ incl. archived; ~$0.97B active [ESTIMATED]"
top_investors: ["Atreides", "NVIDIA", "Intel Capital", "Samsung Catalyst", "Meta (strategic)", "Matrix Partners", "Maverick Silicon"]
key_technical_inflections: ["UCIe / die-to-die interconnect", "Chiplet disaggregation", "RISC-V server platforms (RVA23)", "Custom silicon proliferation", "Hyperscaler/strategic acqui-hires of RISC-V + D2D teams"]
key_open_questions: ["Does an open chiplet marketplace emerge?", "Can RISC-V take server share now that Meta/Qualcomm own RISC-V server teams?", "Who owns the D2D IP layer?", "Will SiFive IPO and set a public comp for RISC-V IP?"]
---

# 04 — Custom ASIC & Chiplets

> Sell the enablement layer for the custom-silicon boom rather than betting on one chip. High-conviction, capital-efficient — and 2025–26 proved the exit path: strategics (Meta, Qualcomm, Tenstorrent) bought RISC-V and D2D teams outright. See [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis
- **Why now:** Every hyperscaler and AI lab wants custom silicon; UCIe + chiplet disaggregation creates a new IP/tooling/services market. Custom XPU programs (Broadcom/Marvell/Alchip/GUC-built) keep multiplying as inference spend overtakes training.
- **Venture-scale:** High via D2D interconnect IP/fabric, RISC-V server platforms, and turnkey chiplet design — IP leverage beats pure services.
- **Inflections:** UCIe standardization, die-to-die PHY/fabric, chiplet economics, RISC-V server momentum (RVA23 profile), memory-interconnect disaggregation (HBM4/custom base dies).
- **2025–26 exit evidence (new):** Meta bought **Rivos** (reported Sept 2025) [CONFIRMED — per Bloomberg/Reuters]; Qualcomm bought **Ventana Micro** (Dec 2025) [CONFIRMED] and reportedly **Akeana** (Oct 2026) [TO VERIFY]; Tenstorrent bought **Blue Cheetah** (Jul 2025) [CONFIRMED]. Strategics are paying for *teams + RISC-V/D2D IP* before products ship — the dominant exit mode in this category is now early strategic M&A, not IPO. SiFive's $400M Series G at $3.65B (Apr 2026) [CONFIRMED] is positioned as the last private round before an IPO.
- **Likely acquirers:** Broadcom, Marvell, Qualcomm, Synopsys, Cadence, Arm, Meta/Google/Amazon/Microsoft, Tenstorrent, MediaTek. **Exit:** strategic M&A (dominant); IPO for platform-scale IP (SiFive).
- **Winning startup:** owns reusable IP (interconnect fabric, NoC, D2D PHY) or a RISC-V platform with software. **Non-investable:** pure design-services body shop without IP.

## 2. Market Context
- **Structure:** Merchant/custom ASIC (Broadcom, Marvell, Alchip, GUC, MediaTek) + IP (Arm, Synopsys, Cadence, Alphawave→Qualcomm [TO VERIFY — see [../deal_tracker/20_ma_tracker.md](../deal_tracker/20_ma_tracker.md)]) + chiplet/D2D startups + RISC-V challengers.
- **Custom-XPU context (2026):** Broadcom and Marvell remain the two dominant custom-XPU partners for hyperscalers; Taiwan design houses (Alchip, GUC) take an increasing share of custom AI ASIC back-end and CoWoS integration work. GUC also partners with photonics startups (e.g., Lightmatter partnership reported Jan 2026 [TO VERIFY]). Marvell's purchase of Celestial AI (closed Feb 2026, see [06](06_optical_interconnect_and_cpo.md)) shows custom-ASIC houses buying optical scale-up IP to differentiate.
- **RISC-V consolidation:** The independent RISC-V *server CPU* field shrank sharply in 2025–26 (Rivos→Meta, Ventana→Qualcomm, Akeana→Qualcomm [TO VERIFY]). Remaining independents: SiFive (IP), Tenstorrent (IP + chips; see [01](01_training_accelerators.md)), plus Chinese/European players. NVIDIA invested in SiFive's Series G [CONFIRMED].
- **Segments:** Hyperscaler custom AI silicon, networking ASICs, sovereign chips, automotive.
- **Drivers:** Cost/perf of custom vs. merchant GPU; reticle limits → chiplets; supply diversification; inference cost per token.
- **Bottlenecks:** D2D bandwidth/energy, advanced packaging (CoWoS/interposer supply), NoC scalability, verification.
- **Competitive:** Broadcom/Marvell dominate custom ASIC; startups attack the IP/fabric layer; strategic buyers absorb the most advanced RISC-V teams.
- **Risks:** Incumbent IP bundling, long sales cycles, packaging dependence, acqui-hire-style exits capping venture returns.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| SiFive | US | 2015 | Series G (pre-IPO) | ~$766M [ESTIMATED]; $400M Series G Apr 2026 at $3.65B [CONFIRMED] | Atreides (G lead), NVIDIA, Apollo, Point72, T. Rowe Price, Prosperity7, Sutter Hill | RISC-V CPU/AI core IP; data-center RISC-V push | SoC/XPU builders, DC | Largest independent RISC-V IP vendor | CEO calls Series G the last private round before IPO [CONFIRMED] | High | Active |
| Eliyan | US | 2021 | Series B + strategic | ~$150M [TO VERIFY] | Samsung Catalyst, Tiger Global, Intel Cap, Meta (2026 strategic, reported) [TO VERIFY] | NuLink D2D PHY (organic substrate) | Chiplet / HBM interconnect | UCIe-class D2D without silicon interposer | $50M strategic round Jan 2026 [TO VERIFY] | High | Active |
| Baya Systems | US | 2022 | Series B | ~$47M+ [TO VERIFY] (CB Insights: 3 rounds) | Maverick Silicon (B lead), Synopsys, Matrix, Intel Cap | NoC / chiplet fabric IP (WeaveIP) | SoC/chiplet builders | Software-driven NoC + chiplet fabric | $36M Series B Jan 2025 [CONFIRMED]; no 2026 round found | High | Active |
| zeroASIC | US | 2021 | Seed / gov-funded | ~$6.9M [TO VERIFY] | Lockheed Martin Ventures [TO VERIFY] | Composable chiplets + open EDA | Chiplet marketplace / defense | Open chiplet platform | DARPA NGMM 3DHI + DoE awards (company-reported) | Medium | Active |
| Chipletz | US | 2021 [TO VERIFY] | Early [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | "Smart Substrate" multi-chip packaging | AI/HPC chiplet integration | Substrate-level chiplet integration | Low public visibility | Medium | Active |
| Akeana | US | 2021 | Acquired [TO VERIFY] | ~$100M+ raised | Kleiner Perkins, Mayfield, Fidelity | RISC-V IP + Alpine server test chip | SoC / DC | Broad RISC-V core IP | Reported acquired by Qualcomm Oct 2026 [TO VERIFY] | Archived | Acquired [TO VERIFY] |
| Rivos | US | 2021 | Acquired | ~$250M+ raised [TO VERIFY] | Matrix, Intel Cap, MediaTek, Dell | RISC-V + AI accelerator server SoC | (now Meta) | RISC-V + GPGPU/HBM, CUDA-compatible stack claim | Acquired by Meta, reported Sept 2025; terms undisclosed [CONFIRMED] | Archived | Acquired (Meta) |
| Ventana Micro | US | 2018 | Acquired | [TO VERIFY] | [TO VERIFY] | Veyron RISC-V server CPU chiplets | (now Qualcomm) | High-perf RISC-V chiplet CPU | Acquired by Qualcomm, Dec 2025; terms undisclosed [CONFIRMED] | Archived | Acquired (Qualcomm) |
| Blue Cheetah | US | 2018 | Acquired | [TO VERIFY] | NEA [TO VERIFY] | BlueLynx D2D IP | (now Tenstorrent) | Portable D2D PHY across nodes | Acquired by Tenstorrent, Jul 2025; still licenses IP externally [CONFIRMED] | Archived | Acquired (Tenstorrent) |

## 4. Company Profiles

### SiFive
- **Status:** Active (pre-IPO) · **HQ:** Santa Clara / San Mateo, US [TO VERIFY] · **Founded:** 2015 · **Founders:** Krste Asanović, Yunsup Lee, Andrew Waterman (UC Berkeley RISC-V originators) · **CEO:** Patrick Little
- **Stage:** Series G · **Total Funding:** ~$766M [ESTIMATED, aggregator] · **Last Round:** $400M Series G, Apr 9 2026, at $3.65B valuation, led by Atreides; NVIDIA, Apollo, Point72, T. Rowe Price, Prosperity7, Sutter Hill participated [CONFIRMED — company announcement / press] · **Website:** sifive.com
- **Primary:** 04 · **Secondary:** 01/02 (AI core IP) · **One-Line:** The largest independent RISC-V CPU/AI-core IP licensor, now pushing into data-center RISC-V.
- **Tech:** Performance/Intelligence/Essential RISC-V core families, vector/AI extensions, DC-class cores. **Differentiation:** ecosystem scale + NVIDIA strategic backing (NVIDIA had already announced CUDA support for RISC-V hosts in 2025 [TO VERIFY]). **Signal:** CEO described the Series G as the final private round before an IPO [CONFIRMED]; no filing timeline disclosed. Secondary-market marks ~$3.9B (Caplight, May 2026) [UNCONFIRMED].
- **VC view:** High; the likely first public RISC-V IP comparable. **Risk:** Arm competition, customers in-sourcing (Meta/Qualcomm now own RISC-V teams). **Data quality:** Medium-High. **Last updated:** 2026-11-04.

### Eliyan
- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2021 · **Founders:** Ramin Farjadrad (CEO), Syrus Ziai
- **Stage:** Series B + 2026 strategic round · **Total Funding:** ~$150M [TO VERIFY] (aggregators range $90M–$150M) · **Rounds:** $40M Series A (Nov 2022); $60M Series B (Mar 2024, Samsung Catalyst + Tiger Global) [CONFIRMED]; ~$50M strategic round announced Jan 28 2026, reportedly with Meta, Samsung Catalyst and Intel Capital [TO VERIFY — no primary release retrieved] · **Website:** eliyan.com
- **Primary:** 04 · **Secondary:** 13 Packaging, 07 Memory · **One-Line:** NuLink die-to-die interconnect PHY enabling chiplets on standard organic substrates (no silicon interposer).
- **Tech:** UCIe-compatible D2D PHY with high bandwidth/energy on cheaper organic packaging; memory-interconnect ("UMI") concepts for HBM disaggregation. **Differentiation:** removes interposer cost/supply bottleneck — directly attacks the CoWoS constraint. **Strategic backing from Samsung + Micron, and reportedly Meta, is a strong signal** — Meta is now also the owner of Rivos.
- **VC view:** High; acquirers = packaging/IP incumbents, memory makers, hyperscalers. **Risk:** UCIe ecosystem competition (Synopsys/Cadence PHY), strategic acqui-hire capping upside. **Data quality:** Medium. **Last updated:** 2026-11-04.

### Rivos (archived — acquired by Meta)
- **Status:** Acquired by Meta Platforms — first reported by Bloomberg, Reuters followed, late Sept 2025; terms not disclosed [CONFIRMED]. Rivos had reportedly been seeking funding at >$2B valuation in Aug 2025 [TO VERIFY]; one outlet estimated deal value >$850M [UNCONFIRMED].
- **HQ:** Santa Clara, US · **Founded:** 2021 · **Pre-exit funding:** ~$250M+ [TO VERIFY] (Matrix, Intel Capital, MediaTek, Dell).
- **Why it matters:** Meta was reportedly one of Rivos' largest customers; the deal folds a RISC-V + AI-accelerator team (with a CUDA-compatible software effort) into Meta's MTIA program — a template for hyperscalers buying startup silicon teams to reduce NVIDIA dependence. Apple's 2023 trade-secret suit against Rivos had been settled. **Last updated:** 2026-11-04.

### Ventana Micro Systems (archived — acquired by Qualcomm)
- **Status:** Acquired by Qualcomm, announced mid-Dec 2025; terms not disclosed [CONFIRMED — Qualcomm announcement, DCD/Tom's Hardware]. Team joins Qualcomm's RISC-V and Oryon CPU efforts; Qualcomm has not confirmed continuation of the Veyron V2 product line. Veyron V1 never reached market; V2 had been targeted for 2026.
- **Why it matters:** Second RISC-V server-CPU startup absorbed by a strategic within three months. **Last updated:** 2026-11-04.

### Akeana (archived — acquisition reported)
- **Status:** Reported acquired by Qualcomm, Oct 2026; terms undisclosed [TO VERIFY — aggregator + Chinese-language trade report dated Oct 21 2026; no primary Qualcomm release retrieved]. Pre-exit: >$100M raised (Kleiner Perkins, Mayfield, Fidelity); Alpine RVA23 server test chip reportedly taped out Dec 2025 with Samsung Foundry [UNCONFIRMED]; Axiomise formal-verification partnership Feb 2026 (company-reported).
- **Note:** If confirmed, Qualcomm will have bought two RISC-V CPU teams (Ventana + Akeana) within a year. **Last updated:** 2026-11-04.

> Baya Systems, zeroASIC, Chipletz covered at table level. Blue Cheetah archived (Tenstorrent, Jul 2025). **Tenstorrent** (RISC-V/chiplet IP + chips) is profiled in [01](01_training_accelerators.md). **Astera Labs** (connectivity, public) is profiled in [05](05_networking_and_interconnect.md). Exits are logged in [../deal_tracker/23_exit_and_shutdown_tracker.md](../deal_tracker/23_exit_and_shutdown_tracker.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| D2D / UCIe PHY IP | High | High | Medium | Medium-High | Real | High |
| NoC / chiplet fabric IP | High | High | Medium | Medium | Real | High |
| RISC-V server platforms | Medium-High | Very High | High | High | Mostly absorbed by strategics (2025–26) | Medium (exit = early M&A) |
| RISC-V core IP (platform scale) | Medium-High | High | Medium | High (Arm) | Real — SiFive pre-IPO | Medium-High |
| Open chiplet marketplace / substrates | Medium | High | Medium | Medium | Emerging | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Atreides | Crossover | SiFive | Growth | Led SiFive $400M Series G (Apr 2026) | Pre-IPO compute IP |
| NVIDIA (NVentures) | Strategic | SiFive | Growth | SiFive Series G (Apr 2026) | Hedges into RISC-V host CPUs |
| Intel Capital | Strategic | Eliyan, Baya, (Rivos) | Seed–Growth | Eliyan 2026 strategic [TO VERIFY] | Chiplet ecosystem |
| Samsung Catalyst | Strategic | Eliyan | B+ | Eliyan B + 2026 round | Memory/packaging interconnect |
| Meta | Strategic / acquirer | Rivos (acquired), Eliyan [TO VERIFY] | — | Bought Rivos 2025 | In-house MTIA silicon |
| Qualcomm | Acquirer | Ventana, Akeana [TO VERIFY] | — | Two RISC-V CPU tuck-ins | DC CPU ambitions |
| Maverick Silicon | VC | Baya | B | Led Baya Series B | Silicon IP |
| Matrix Partners | VC | Baya, (Rivos) | Seed–B | Rivos exit | Compute infra/IP |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Ramin Farjadrad | Industry (Eliyan) | SerDes/D2D | Serial-link pedigree (Aquantia) | Confirmed (Eliyan) | D2D patents | 5 | High |
| Krste Asanović | UC Berkeley | RISC-V | RISC-V ecosystem origin | Confirmed (SiFive) | RISC-V | 5 | High |
| Elad Alon | UC Berkeley / Tenstorrent | Mixed-signal D2D | Blue Cheetah founder, now at Tenstorrent | Confirmed (acquired) | D2D/SerDes | 4 | High |
| UCLA/CHIPS, Georgia Tech 3D | UCLA/GT | Heterogeneous integration | Chiplet/packaging research base | Watchlist | Many | 4 | Medium |

## 8. Diligence Questions
- **Technical:** D2D bandwidth/energy vs. UCIe/Synopsys? Node portability? Verification IP? RVA23 compliance for RISC-V cores?
- **Market:** Merchant-ASIC vs. IP-licensing model; attach to which chiplet/custom-XPU programs (Broadcom, Marvell, Alchip, GUC)?
- **Customer:** Signed IP licenses/tape-outs vs. evaluations? Is the largest customer also the most likely acquirer (Rivos/Meta pattern)?
- **Competitive:** Defensible vs. Synopsys/Cadence PHY bundling and Arm's custom-silicon programs?
- **Financial:** Royalty vs. NRE mix; gross-margin profile? Preference stack vs. likely acqui-hire price?
- **Founder:** Shipped IP at scale? **Exit:** IP-tuck-in logic for EDA/networking incumbents, hyperscalers, Qualcomm?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 7 | 0 | 0 | Initial build; Eliyan/Rivos profiles; D2D/RISC-V coverage | Company sites, trade press |
| 2026-11-04 | Full (Refresh #3) | 2 | 4 | 4 | Added SiFive (profiled; $400M Series G at $3.65B, Apr 2026) and Chipletz. Archived Rivos (Meta, Sept 2025), Ventana (Qualcomm, Dec 2025), Blue Cheetah (Tenstorrent, Jul 2025), Akeana (Qualcomm, Oct 2026 [TO VERIFY]). Updated Eliyan (Jan 2026 strategic round [TO VERIFY]), Baya (funding corrected to Jan 2025 Series B), zeroASIC. Thesis/market rewritten around strategic RISC-V consolidation + custom-XPU context. | Bloomberg/Reuters via DCD (Rivos); Qualcomm/DCD/Tom's Hardware (Ventana); Tenstorrent PR (Blue Cheetah); TNW/press (SiFive); Cooley/Latham (Baya); aggregators (Eliyan, Akeana) |
