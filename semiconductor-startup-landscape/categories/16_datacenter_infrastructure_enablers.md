---
category_id: "16"
category_name: "Datacenter Infrastructure Enablers"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 10
active_companies: 8
archived_companies: 2
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$600M+ incl. Enfabrica and JetCool (exited) [ESTIMATED; most cooling figures TO VERIFY]"
top_investors: ["Johnson Controls", "Trane Technologies", "nVent", "BlueYard", "Mango Capital", "Planet First Partners", "NVIDIA / Sutter Hill"]
key_technical_inflections: ["Liquid cooling becomes default at 100kW–1MW racks", "Microfluidic / in-chip cooling", "Two-phase direct-to-chip", "800V DC rack power (see 08)", "Optical circuit switching", "Strategic consolidation of thermal vendors"]
key_open_questions: ["Which cooling approach wins at hyperscale (single-phase DTC vs. two-phase vs. microfluidic)?", "Do startups beat Vertiv/Schneider/Eaton scale, or just sell to them?", "Where is the silicon-adjacent venture value?"]
---

# 16 — Datacenter Infrastructure Enablers

> The "picks and shovels around the chip" — cooling, rack power, optical switching, smart NICs, and DC fabric. High-conviction way to ride AI capex with less single-chip risk; strong near-term revenue and an increasingly active strategic M&A market as thermal incumbents consolidate. See [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis
- **Why now:** AI racks at 100kW+ (and NVIDIA's roadmap toward ~1MW Kyber racks with 800V DC distribution) break air cooling and conventional power distribution; the physical datacenter is being re-architected around the GPU. Liquid cooling moved from option to default for GB200/GB300/Rubin-class deployments.
- **Venture-scale:** High in differentiated liquid cooling (two-phase, microfluidic/in-chip), rack-scale power (800V, see [08](08_power_semiconductors_and_power_delivery.md)), and optical circuit switching; nearer-term revenue than pure-silicon plays.
- **Inflections:** Direct-to-chip single/two-phase, microfluidic cooling etched into or bonded onto silicon (Corintis–Microsoft demonstration, 2025 [TO VERIFY]), immersion for specific niches, 800V DC/rack power shelves, optical circuit switching (Google in-house; startups), SmartNIC/DPU (see [05](05_networking_and_interconnect.md)), memory-disaggregated servers (Majestic Labs, see [07](07_memory_and_storage.md)).
- **Acquirers:** Vertiv, Schneider, Eaton, Trane, Daikin, Johnson Controls, nVent, Flex, hyperscalers, networking incumbents; NVIDIA via license + acqui-hire (Enfabrica, 2025). **Exit:** strategic M&A; some near-term revenue scale.
- **Winning startup:** differentiated cooling/power/switching at hyperscale qualification + deployment, ideally aligned with NVIDIA reference designs. **Non-investable:** undifferentiated cooling vs. Vertiv/Schneider scale.

## 2. Market Context
- **Structure:** DC infra incumbents (Vertiv, Schneider, Eaton, nVent, Trane, Johnson Controls) + cooling startups + optical-switch (Google in-house, Lumentum, startups) + DPU/NIC.
- **Consolidation (2024–26) [all TO VERIFY — not re-verified this refresh]:** Flex acquired JetCool (Nov 2024); Schneider Electric took a 75% stake in Motivair (~$850M, 2024); Eaton agreed to acquire Boyd Thermal (~$9.5B, late 2025); Vertiv acquired PurgeRite (2025); Daikin Applied reportedly acquired Chilldyne (2025) [UNCONFIRMED]. The pattern: thermal incumbents buy liquid-cooling know-how; startup exits come via strategic M&A rather than IPO.
- **NVIDIA platform effects:** Enfabrica's CEO and team joined NVIDIA with a technology license (Sept 2025; >$900M reported by CNBC) [TO VERIFY — primary coverage in [05](05_networking_and_interconnect.md)]; 800V HVDC rack ecosystem (Vertiv products 2H 2026 [TO VERIFY]); Cerebras and other accelerator vendors now operate their own inference datacenters (see [01](01_training_accelerators.md)).
- **Segments:** Hyperscale AI DC, neoclouds, sovereign AI DCs, enterprise AI, colo.
- **Drivers:** Rack density/power, PUE/water, grid limits, GPU utilization, capex velocity.
- **Bottlenecks:** Thermal at 100kW–1MW, power distribution, deployment/qualification speed, CDU/coldplate supply.
- **Competitive:** Vertiv/Schneider/Eaton dominate; startups win on density/efficiency + hyperscaler adoption, then sell to incumbents.
- **Risks:** Incumbent scale, long qualification, capex cyclicality, NVIDIA reference-design lock-in.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Corintis | CH | 2022 | Series A | ~$24M Series A (Sept 2025) [TO VERIFY] | BlueYard [TO VERIFY] | Microfluidic cooling designed into chip/package | AI GPUs/XPUs | Chip-specific microchannel design (EPFL spinout) | Microsoft in-chip microfluidics demo (2025) [TO VERIFY] | High | Active |
| Accelsius | US | 2022 | Series B | ~$65M Series B (2025) [TO VERIFY] | Johnson Controls, Legrand [TO VERIFY] | NeuCool two-phase direct-to-chip | AI servers/colo | Pumped two-phase DTC for >1kW chips | Deployments/partnerships [TO VERIFY] | Medium-High | Active |
| Frore Systems | US | 2018 | Growth | [TO VERIFY] | [TO VERIFY] | AirJet solid-state cooling; LiquidJet DTC coldplate | Edge + AI DC | Microfabricated (MEMS-style) coldplate manufacturing | LiquidJet for AI DC (2025) [TO VERIFY] | Medium-High | Active |
| LiquidStack | US | 2012 | Growth | [TO VERIFY] | Trane Technologies (strategic) [TO VERIFY] | Two-phase immersion + CDUs | Hyperscale/colo | Two-phase immersion pioneer; CDU pivot | Deployments | Medium | Active |
| Submer | ES | 2015 | Series B+ | ~$70M+ [TO VERIFY] | Mango, Planet First | Immersion cooling | Hyperscale/colo | Single/two-phase immersion | Deployments | Medium-High | Active |
| ZutaCore | US/IL | 2016 | Series B+ | ~$60M+ [TO VERIFY] | Mizmaa, Extreme | Two-phase direct-to-chip cooling | AI servers | Waterless 2-phase DTC | NVIDIA-ecosystem pilots | Medium-High | Active |
| Iceotope | UK | 2005 | Growth | ~$70M+ [TO VERIFY] | nVent, ABC IM | Precision liquid cooling | AI/edge DC | Chassis-level liquid | nVent partnership | Medium | Active |
| Chilldyne / negative-pressure DTC | US | 2011 | Growth | [TO VERIFY] | [TO VERIFY] | Negative-pressure liquid cooling | AI/HPC DC | Leak-safe negative pressure | Reported acquisition by Daikin Applied (2025) [UNCONFIRMED] | Medium | Active |
| Enfabrica | US | 2020 | Licensed/Acqui-hired | ~$290M+ raised [TO VERIFY] | NVIDIA, Sutter Hill | SuperNIC + memory fabric | AI fabric (see [05](05_networking_and_interconnect.md)) | Converged network+memory | CEO/team to NVIDIA + tech license (Sept 2025; >$900M reported) [TO VERIFY] | Archived | Licensed/Acqui-hired |
| JetCool | US | 2019 | Acquired | ~$20M+ raised | [TO VERIFY] | Microconvective DTC cooling | AI servers | Targeted microjet cooling | Acquired by Flex 2024 | Archived | Acquired |

## 4. Company Profiles

### Corintis (new)
- **Status:** Active · **HQ:** Lausanne, CH · **Founded:** 2022 · **Origin:** EPFL spinout [TO VERIFY]
- **Funding:** ~$24M Series A (Sept 2025) led by BlueYard [TO VERIFY — not re-verified this refresh].
- **One-Line:** Designs chip-specific microfluidic cooling (microchannels tailored to a die's hotspot map) that can be integrated into coldplates or the package/silicon itself.
- **Signal:** Microsoft publicly demonstrated in-chip microfluidic cooling developed with Corintis (2025), claiming materially lower peak die temperature vs. coldplates [TO VERIFY]. **Risk:** manufacturing integration with foundry/OSAT; hyperscaler-specific customization. **VC view:** High — the most silicon-adjacent cooling bet; acquirers = thermal incumbents, OSATs, hyperscalers. **Data quality:** Low-Medium. **Last updated:** 2026-11-04.

### ZutaCore
- **Status:** Active · **HQ:** San Jose, US / Israel · **Founded:** 2016 · **One-Line:** Waterless two-phase direct-to-chip liquid cooling (HyperCool) for high-power AI GPUs, enabling 100kW+ racks without facility water risk.
- **Tech:** dielectric two-phase evaporative cooling directly on the chip; targets next-gen GPU TDPs. **Differentiation:** waterless + high heat flux. **Risk:** single-phase DTC became the NVIDIA reference default; competition from Accelsius and incumbents. **VC view:** Medium-High; acquirers = Vertiv/Schneider/Eaton/Flex. No new verified financing this refresh. **Data quality:** Low-Medium. **Last updated:** 2026-11-04.

### Submer
- **Status:** Active · **HQ:** Barcelona, ES · **Founded:** 2015 · **One-Line:** Immersion cooling systems and coolants for hyperscale and AI datacenters, improving density and PUE.
- **Tech:** single-/two-phase immersion tanks + coolant + management software. **Risk:** hyperscalers standardized on DTC for GPU racks; immersion remains niche. **VC view:** Medium-High. No new verified financing this refresh. **Data quality:** Low-Medium. **Last updated:** 2026-11-04.

> Accelsius, Frore, LiquidStack, Iceotope, Chilldyne (cooling) at table level. Archived: Enfabrica (NVIDIA license + acqui-hire, 2025 — primary in [05](05_networking_and_interconnect.md)); JetCool (Flex, 2024). Optical circuit switching startups (e.g., nEye) tracked in [06](06_optical_interconnect_and_cpo.md) [TO VERIFY]. Power-side enablers in [08](08_power_semiconductors_and_power_delivery.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Direct-to-chip cooling (single-phase) | Very High | Medium-High | Medium | Very High (Vertiv, Eaton/Boyd, CoolIT) | Narrow | Medium |
| Two-phase DTC | High | High | Medium | High | Real | Medium-High |
| Microfluidic / in-chip cooling | High (rising) | Very High | Medium-High | Medium | Real | High |
| Immersion cooling | Medium | Medium-High | Medium-High | Medium | Niche | Medium |
| Rack-scale power (800V) | Very High | High | Medium-High | High | Real (see 08) | Medium-High |
| Optical circuit switching | High | High | Medium | High | Narrow | Medium |
| SmartNIC/DPU | High | High | Medium | High (NVIDIA absorbed Enfabrica) | Real (see 05) | Medium-High |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| nVent | Strategic | Iceotope | Growth | Iceotope | Cooling roll-up |
| Johnson Controls / Legrand | Strategic | Accelsius [TO VERIFY] | B | 2025 | Thermal incumbents buying optionality |
| Trane Technologies | Strategic | LiquidStack [TO VERIFY] | Growth | — | HVAC → liquid cooling |
| BlueYard | VC | Corintis [TO VERIFY] | A | 2025 | Silicon-adjacent cooling |
| Climate/infra VCs | VC | Submer, ZutaCore | B–Growth | Cooling | DC efficiency |
| NVIDIA / Sutter Hill | Strategic/VC | Enfabrica | C → exit | License + acqui-hire 2025 | AI infra fabric |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Two-phase cooling labs | Stanford/Purdue/Georgia Tech | Microfluidic/2-phase cooling | Heat-flux limits at 100kW+ | Likely | Many; microfluidics | 4 | Medium |
| EPFL microfluidic cooling (Matioli lab) | EPFL | Co-designed microfluidic cooling in chips | Corintis lineage [TO VERIFY] | Confirmed (Corintis) [TO VERIFY] | Nature 2020 microfluidic cooling | 4 | Medium |
| DC energy systems | Berkeley/LBNL | DC efficiency/power | PUE/grid optimization | Watchlist | Many | 3 | Medium |

## 8. Diligence Questions
- **Technical:** Heat flux/density at next-gen TDPs (>2kW per package); reliability/leak-safety; PUE/water impact measured?
- **Market:** DTC vs. two-phase vs. microfluidic adoption; NVIDIA reference-design alignment; hyperscaler qualification status?
- **Customer:** Hyperscaler/neocloud/sovereign deployments committed?
- **Competitive:** Defensible vs. Vertiv/Schneider/Eaton scale + hyperscaler in-house?
- **Financial:** Capex/services mix; gross margin; deployment velocity? **Founder:** DC infra pedigree?
- **Exit:** strategic acquirer precedent (Flex–JetCool, Schneider–Motivair, Eaton–Boyd)?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 6 | 0 | 0 | Initial build; ZutaCore/Submer profiles; cooling/power/fabric coverage | Company sites, trade press |
| 2026-11-04 | Full (Refresh #3) | 4 | 5 | 1 (Enfabrica) | Added Corintis, Accelsius, Frore, LiquidStack; Enfabrica archived (NVIDIA license + acqui-hire, Sept 2025); thermal-incumbent consolidation context (Flex–JetCool, Schneider–Motivair, Eaton–Boyd, Vertiv–PurgeRite); 800V rack power + microfluidic cooling in thesis/heatmap. NOTE: cooling-startup figures not re-verified this refresh (search budget exhausted) — all tagged [TO VERIFY]/[UNCONFIRMED] | Prior DB, trade press (CNBC, DCD) — to be re-verified next refresh |
