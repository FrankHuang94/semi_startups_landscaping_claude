---
category_id: "15"
category_name: "Autonomous, Robotics & Automotive Silicon"
primary_datacenter_relevance: "Medium"
vc_relevance: "Medium"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 7
active_companies: 7
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$800M+ private/pre-IPO [ESTIMATED]"
top_investors: ["BMW i Ventures", "Celesta", "GreatPoint", "Mercedes", "Samsung", "Temasek"]
key_technical_inflections: ["Physical AI / humanoids", "Centralized vehicle compute", "In-house OEM silicon (Tesla AI5/AI6)", "Energy-efficient on-vehicle inference", "Robotics perception+control SoCs", "Auto-chip startups pivoting to DC inference"]
key_open_questions: ["Does physical AI create new venture-scale silicon or is it NVIDIA Jetson Thor's to lose?", "Can startups pass automotive qualification gates?", "Robotics volume timing?", "Do auto-AI chip vendors consolidate (Ambarella sale process)?"]
---

# 15 — Autonomous, Robotics & Automotive Silicon

> Physical AI (humanoids, autonomy) is the next compute frontier; automotive is a long, design-win-gated game with OEM/Tier-1 gatekeepers. 2025–26 pattern: OEMs consolidate in-house silicon (Tesla ended Dojo in Aug 2025 to focus on AI5/AI6 [CONFIRMED — Bloomberg; Musk on X]), incumbents buy robotics (Mobileye–Mentee Robotics [UNCONFIRMED]), auto-AI chip startups pivot to datacenter inference (Recogni → Tensordyne, Sept 2025 [CONFIRMED by multiple outlets]), and listed edge/auto vendors explore sales (Ambarella [UNCONFIRMED]). See [03](03_edge_inference_chips.md) for overlap.

> ⚠️ **Verification note (Refresh #3):** the shared web-search budget was exhausted before this category's sub-batch was searched. All 2025–26 events below are carried from prior knowledge and tagged [TO VERIFY] / [UNCONFIRMED]; no new amounts were added without a source. Re-verify next refresh.

## 1. VC Investment Thesis
- **Why now:** Humanoid/robotics momentum + centralized vehicle compute + energy-constrained on-vehicle inference create demand for efficient, safety-grade AI silicon; VLA (vision-language-action) models raise robot compute requirements.
- **Venture-scale:** Medium — automotive cycles are long and gated; robotics is earlier and higher-variance; NVIDIA (Jetson Thor / DRIVE Thor) [TO VERIFY] and Qualcomm set a high bar; outcomes mostly via strategic M&A.
- **Inflections:** Physical-AI compute, zonal/central E/E architectures, efficient perception+planning SoCs, functional-safety AI, OEM in-sourcing (Tesla, Chinese OEMs).
- **Acquirers:** Qualcomm, NVIDIA, Mobileye, NXP, Renesas, Tier-1s (Bosch, Continental), private equity (Ambarella-type sale processes). **Exit:** M&A, SPAC/IPO (Blaize; Horizon Robotics / Black Sesame HK listings).
- **Winning startup:** efficient safety-grade AI SoC + reference stack with an OEM/robotics anchor; or robotics-native compute designed around VLA models. **Non-investable:** generic auto-AI chip without qualification path or design wins.

## 2. Market Context
- **Structure:** Mobileye, NVIDIA (DRIVE Thor, Jetson Thor), Qualcomm (Snapdragon Ride), Tesla (in-house), Ambarella; China: Horizon Robotics, Black Sesame (both HK-listed); startups thin.
- **2025–26 events (all [TO VERIFY] unless noted):**
  - Tesla wound down the Dojo supercomputer team (Aug 2025, per Bloomberg) to focus on AI5/AI6 inference chips; AI6 to be fabbed by Samsung under a ~$16.5B agreement (Jul 2025); AI5 at TSMC, production targeted end-2026 [CONFIRMED — Bloomberg/Engadget; timing per Musk].
  - Recogni rebranded as **Tensordyne** and refocused on datacenter generative-AI inference using its log-math architecture (Sept 2025); launched the Napier inference platform (Jun 2026) and says it expects >$200M in orders (company claim); preparing a Series D [TO VERIFY].
  - Ambarella reportedly explored a sale (2025 press reports) [UNCONFIRMED]; outcome unknown as of this refresh.
  - Mobileye agreed to acquire humanoid-robotics startup Mentee Robotics (announced around CES, Jan 2026) [UNCONFIRMED].
  - Blaize trades publicly (NASDAQ: BZAI) after its Jan 2025 SPAC close [TO VERIFY].
- **Segments:** ADAS/AV, humanoid/mobile robotics, drones/defense autonomy, industrial autonomy.
- **Drivers:** Autonomy levels, robotics capex, power/thermal in vehicles/robots, safety regulation, China OEM volume.
- **Bottlenecks:** Functional safety (ISO 26262), qualification time, power efficiency, software stacks.
- **Competitive:** NVIDIA/Qualcomm/Mobileye dominate AV; robotics silicon contested but NVIDIA-led. **Risks:** long cycles, OEM in-sourcing, AV demand timing, China/export controls.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Tensordyne (fka Recogni) | US (San Jose) | 2017 | Series C | ~$150M+ [TO VERIFY] | Celesta, GreatPoint, BMW i | Log-number-system inference systems | DC GenAI inference (pivot from auto) | Multiplication-free log math | Rebrand + DC pivot (Sept 2025); Napier platform (Jun 2026); >$200M expected orders (company claim) | Medium | Active |
| Hailo | IL | 2017 | Series C+ | ~$340M+ [TO VERIFY] | Poalim, Gil Agmon | Edge NPUs (auto, GenAI edge) | Automotive/edge | Efficiency (see [03](03_edge_inference_chips.md)) | Auto design wins; Hailo-10H GenAI edge [TO VERIFY] | Medium-High | Active |
| Blaize | US (El Dorado Hills) | 2010 | Public (NASDAQ: BZAI, SPAC Jan 2025) [TO VERIFY] | ~$330M+ pre-SPAC [TO VERIFY] | Temasek, Samsung, Mercedes | GSP graph processor | Edge/defense/smart-city | Graph-streaming architecture | Public; Asia/defense contracts (company claims) | Medium | Active (Public) |
| Ambarella | US | 2004 | Public (AMBA) | (public) | (public) | CVflow AI SoCs | Auto/cameras/robotics | Low-power vision AI SoCs | Reported sale exploration 2025 [UNCONFIRMED] | Medium | Active (Public) |
| Horizon Robotics | CN (Beijing) | 2015 | Public (HKEX: 9660, Oct 2024) [TO VERIFY] | (public) | (public; VW/CARIAD JV) | Journey ADAS SoCs + HSD stack | China ADAS/AV | China volume leader in ADAS SoCs | Public comparable | Medium | Active (Public) |
| Black Sesame Technologies | CN (Wuhan) | 2016 | Public (HKEX: 2533, Aug 2024) [TO VERIFY] | (public) | (public) | Huashan/Wudang auto SoCs | China ADAS + robotics | Cross-domain auto compute | Public comparable | Low-Medium | Active (Public) |
| indie Semiconductor | US | 2007 | Public (INDI) | (public) | (public) | Automotive mixed-signal/ADAS | Auto sensing | ADAS sensing/connectivity | Public | Low-Medium | Active (Public) |

## 4. Company Profiles

### Tensordyne (formerly Recogni)
- **Status:** Active · **HQ:** San Jose, US · **Founded:** 2017 · **Founders:** RK Anand, Gilles Backhus, Eugene Feinberg, Marc Bolitho
- **Stage:** Series C · **Total Funding:** ~$150M+ [TO VERIFY] · **Last Round:** ~$102M Series C, 2024, co-led by Celesta & GreatPoint [TO VERIFY] · **Investors:** BMW i Ventures, Mayfield, Toyota, Bosch, Continental
- **Primary:** 15 · **Secondary:** 02 · **One-Line:** Logarithmic-number-system (multiplication-free) inference silicon, originally for automotive vision; rebranded Tensordyne and refocused on datacenter GenAI inference systems (2025) [TO VERIFY].
- **Risk:** crowded DC-inference market (see [02](02_inference_accelerators.md)); automotive heritage now secondary. **VC view:** Medium (downgraded from Medium-High given pivot risk). **Acquirers:** Tier-1s, Qualcomm, DC-inference consolidators. **Data quality:** Medium-Low. **Last updated:** 2026-11-04.

> Hailo (see [03](03_edge_inference_chips.md)), Blaize, Ambarella, Horizon Robotics, Black Sesame, indie Semiconductor at table level. Tesla (in-house AI5/AI6), Mobileye, NVIDIA and Qualcomm are incumbent references, not tracked entries. Track humanoid-robotics compute startups (often stealth) at each refresh — see [../STEALTH_STARTUP_DISCOVERY.md](../STEALTH_STARTUP_DISCOVERY.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Robotics/physical-AI compute | High | High | Medium-High | Medium-High (NVIDIA Jetson Thor) | Real (early) | Medium-High |
| Automotive central compute | High | Very High | High | Very High (+ OEM in-sourcing) | Narrow | Medium-Low |
| Efficient on-vehicle inference | High | High | Medium | High | Real | Medium |
| ADAS sensing/mixed-signal | Medium | Medium | Medium | High | Narrow | Low-Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| BMW i / Mercedes / Toyota / Bosch | Strategic (auto) | Tensordyne (Recogni), Blaize | B–Growth | Multi-deal | OEM validation + exit |
| Celesta / Mayfield / GreatPoint | VC | Tensordyne (Recogni) | B–C | Series C (2024) | Efficient AI silicon |
| Samsung / Temasek | Strategic/Sovereign | Blaize | Growth | Pre-SPAC | Edge/auto |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Robotics/embodied-AI labs | Stanford/CMU/Berkeley | Perception+control compute; VLA models | Physical-AI compute requirements | Watchlist | Many | 4 | Medium |
| Automotive efficient-DL labs | ETH/TU Munich | Efficient on-vehicle DL | Auto-grade efficiency | Watchlist | Many | 3 | Medium |

## 8. Diligence Questions
- **Technical:** TOPS/W at safety-grade; ISO 26262 path; sensor/stack integration; VLA-model fit for robotics?
- **Market:** Robotics vs. automotive timing; physical-AI pull; OEM in-sourcing risk?
- **Customer:** OEM/Tier-1/robotics design wins committed?
- **Competitive:** vs. NVIDIA (Thor)/Qualcomm/Mobileye/Horizon?
- **Financial:** NRE/long-cycle funding; gross margin? **Founder:** auto/robotics shipping pedigree?
- **Exit:** Tier-1/Qualcomm/Mobileye acquisition logic; SPAC/IPO viability (Blaize post-SPAC performance)?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 5 | 0 | 0 | Initial build; Recogni profile; auto/robotics coverage | Company sites, trade press |
| 2026-11-04 | Full (Refresh #3) | 2 (Horizon Robotics, Black Sesame — public comparables) | 5 | 0 | Recogni → Tensordyne rebrand/DC pivot [TO VERIFY]; Tesla Dojo shutdown + AI5/AI6 [TO VERIFY]; Ambarella sale exploration [UNCONFIRMED]; Mobileye–Mentee [UNCONFIRMED]; Blaize public status. Web search budget exhausted before this category was searched — all new items need re-verification | Prior knowledge only (no new sources fetched this refresh) |
