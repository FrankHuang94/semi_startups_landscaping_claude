---
category_id: "16"
category_name: "Datacenter Infrastructure Enablers"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-08-13"
refresh_count: 2
total_companies: 6
active_companies: 6
archived_companies: 0
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$500M+ [ESTIMATED]"
top_investors: ["various climate/infra VCs", "strategic DC vendors"]
key_technical_inflections: ["Liquid/immersion cooling at 100kW+ racks", "Rack-scale power", "Optical circuit switching", "Smart NIC/DPU", "DC energy efficiency"]
key_open_questions: ["Which cooling approach wins at hyperscale?", "Do startups beat Vertiv/Schneider scale?", "Where is the silicon-adjacent venture value?"]
---

# 16 — Datacenter Infrastructure Enablers

> The "picks and shovels around the chip" — cooling, rack power, optical switching, smart NICs, and DC fabric. High-conviction way to ride AI capex with less single-chip risk; strong near-term revenue and M&A. See [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis
- **Why now:** AI racks at 100kW+ break air cooling and conventional power distribution; the physical datacenter is being re-architected around the GPU.
- **Venture-scale:** High in liquid/immersion cooling at hyperscale, rack-scale power, and optical circuit switching; nearer-term revenue than pure-silicon plays.
- **Inflections:** Direct-to-chip + immersion cooling, 800V DC/rack power shelves (see [08](08_power_semiconductors_and_power_delivery.md)), optical circuit switching, SmartNIC/DPU (see [05](05_networking_and_interconnect.md)), DC energy efficiency software.
- **Acquirers:** Vertiv, Schneider, Flex, hyperscalers, networking incumbents. **Exit:** strategic M&A; some near-term revenue scale.
- **Winning startup:** differentiated cooling/power/switching at hyperscale qualification + deployment. **Non-investable:** undifferentiated cooling vs. Vertiv scale.

## 2. Market Context
- **Structure:** DC infra incumbents (Vertiv, Schneider, nVent) + cooling startups + optical-switch (incl. Google in-house) + DPU/NIC.
- **Segments:** Hyperscale AI DC, neoclouds, enterprise AI, colo.
- **Drivers:** Rack density/power, PUE/water, grid limits, GPU utilization, capex velocity.
- **Bottlenecks:** Thermal at 100kW+, power distribution, deployment/qualification speed, supply.
- **Competitive:** Vertiv/Schneider dominate; startups win on density/efficiency + hyperscaler adoption.
- **Risks:** Incumbent scale, long qualification, capex cyclicality.

### 2026 Update — power and thermal became the binding constraint (2026-08-13)

- **The 800VDC transition is shipping.** NVIDIA's Vera Rubin platform and Google's next-generation datacenters are reported as first adopters with initial infrastructure shipments in **Q3 2026**; **Vertiv** committed to a complete 800V DC line in 2026 and **Delta** is shipping row-based 800V systems with integrated liquid cooling. Rack power targets quoted in the ecosystem run to **~450kW (Rubin Ultra)** and **600kW–1MW (Feynman)** [TO VERIFY]. See [08](08_power_semiconductors_and_power_delivery.md) for the device layer.
- **At 450kW+ per rack, liquid cooling stops being an option.** Direct-to-chip and immersion move from differentiated to mandatory, which is good for volume and bad for pricing power — and it means the durable startup positions are in the parts incumbents cannot qualify quickly (CDU control, two-phase, in-rack power conversion, telemetry).
- **Grid interconnection and behind-the-meter power** are now the gating factor on deployment schedules, ahead of chip supply in many regions. Large capital is flowing to AI-infrastructure buildouts directly — e.g. **Firmus Grid's reported ~$2B raise (August 2026)** [TO VERIFY] — which is an adjacent market this database should track as a demand signal, not as a semiconductor investment.
- **Rack-scale systems became a chip-company product line:** d-Matrix acquired **GigaIO's SuperNODE and FabreX**; Ayar Labs and **Wiwynn** showed a 1,024-accelerator rack-scale reference design at OFC 2026. The "enabler" layer and the "silicon" layer are merging, and integration partners (Wiwynn, Alchip, ASE, Amkor) are becoming kingmakers.
- **Underwriting note:** this category converts an architectural transition into revenue faster than silicon does, with lower technical risk and lower gross margins. In a cycle where accelerator startups need 3+ years to revenue, the 2026–27 power/thermal socket decisions are a nearer-term, more diligenceable bet.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|-----------------|----------|--------------|--------|
| Submer | ES | 2015 | Series B+ | ~$70M+ [TO VERIFY] | Mango, Planet First | Immersion cooling | Hyperscale/colo | Single/two-phase immersion | Deployments | Medium-High | Active |
| ZutaCore | US/IL | 2016 | Series B+ | ~$60M+ [TO VERIFY] | Mizmaa, Extreme | Two-phase direct-to-chip cooling | AI servers | Waterless 2-phase DTC | NVIDIA-ecosystem pilots | Medium-High | Active |
| Iceotope | UK | 2005 | Growth | ~$70M+ [TO VERIFY] | nVent, ABC IM | Precision liquid cooling | AI/edge DC | Chassis-level liquid | nVent partnership | Medium | Active |
| Enfabrica | US | 2020 | Series C | ~$290M+ [TO VERIFY] | NVIDIA, Sutter Hill | SuperNIC + memory fabric | AI fabric (see [05](05_networking_and_interconnect.md)) | Converged network+memory | NVIDIA-backed | High | Active |
| JetCool | US | 2019 | Acquired | ~$20M+ raised | [TO VERIFY] | Microconvective DTC cooling | AI servers | Targeted microjet cooling | Acquired by Flex 2024 | Medium | Acquired |
| Chilldyne / negative-pressure DTC | US | 2011 | Growth | [TO VERIFY] | [TO VERIFY] | Negative-pressure liquid cooling | AI/HPC DC | Leak-safe negative pressure | Deployments | Medium | Active |

## 4. Company Profiles

### ZutaCore
- **Status:** Active · **HQ:** San Jose, US / Israel · **Founded:** 2016 · **One-Line:** Waterless two-phase direct-to-chip liquid cooling (HyperCool) for high-power AI GPUs, enabling 100kW+ racks without facility water risk.
- **Tech:** dielectric two-phase evaporative cooling directly on the chip; targets next-gen GPU TDPs. **Differentiation:** waterless + high heat flux; ecosystem alignment with GPU TDP roadmaps. **Risk:** qualification vs. DTC water loops, incumbent competition. **VC view:** Medium-High; acquirers = Vertiv/Schneider/Flex. **Data quality:** Low-Medium. **Last updated:** 2026-06-09.

### Submer
- **Status:** Active · **HQ:** Barcelona, ES · **Founded:** 2015 · **One-Line:** Immersion cooling systems and coolants for hyperscale and AI datacenters, improving density and PUE.
- **Tech:** single-/two-phase immersion tanks + coolant + management software. **Differentiation:** full immersion stack + sustainability angle. **Risk:** immersion adoption vs. DTC preference at hyperscale. **VC view:** Medium-High. **Data quality:** Low-Medium. **Last updated:** 2026-06-09.

> Iceotope, Chilldyne (cooling), Enfabrica (fabric, see [05](05_networking_and_interconnect.md)) at table level; JetCool acquired by Flex (2024). Power-side enablers in [08](08_power_semiconductors_and_power_delivery.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Direct-to-chip cooling | High | High | Medium | High | Real | Medium-High |
| Immersion cooling | High | Medium-High | Medium-High | Medium | Real | Medium-High |
| Rack-scale power | High | High | Medium-High | High | Real | Medium-High |
| Optical circuit switching | High | High | Medium | High | Narrow | Medium |
| SmartNIC/DPU | High | High | Medium | High | Real (see 05) | High |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| nVent | Strategic | Iceotope | Growth | Iceotope | Cooling roll-up |
| Climate/infra VCs | VC | Submer, ZutaCore | B–Growth | Cooling | DC efficiency |
| NVIDIA / Sutter Hill | Strategic/VC | Enfabrica | C | Fabric | AI infra fabric |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------|----------------|:------------:|------------|
| Two-phase cooling labs | Stanford/Purdue/Georgia Tech | Microfluidic/2-phase cooling | Heat-flux limits at 100kW+ | Likely | Many; microfluidics | 4 | Medium |
| DC energy systems | Berkeley/LBNL | DC efficiency/power | PUE/grid optimization | Watchlist | Many | 3 | Medium |

## 8. Diligence Questions
- **Technical:** Heat flux/density at next-gen TDPs; reliability/leak-safety; PUE impact measured?
- **Market:** DTC vs. immersion adoption; hyperscaler qualification status?
- **Customer:** Hyperscaler/neocloud deployments committed?
- **Competitive:** Defensible vs. Vertiv/Schneider scale + hyperscaler in-house?
- **Financial:** Capex/services mix; gross margin; deployment velocity? **Founder:** DC infra pedigree?
- **Exit:** strategic acquirer (Vertiv/Schneider/Flex) precedent?

## 9. Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 6 | 0 | 0 | Initial build; ZutaCore/Submer profiles; cooling/power/fabric coverage | Company sites, trade press |
| 2026-08-13 | Full refresh | 0 | 2 (market context, thesis emphasis) | 0 | 800VDC shipping from Q3 2026 (NVIDIA Vera Rubin, Google; Vertiv/Delta product lines) with 450kW–1MW rack targets making liquid cooling mandatory; grid interconnection as the gating constraint; rack-scale integration merging with silicon (d-Matrix→GigaIO, Ayar/Wiwynn 1,024-accelerator design) | Vendor announcements, trade press [many TO VERIFY] |
