---
category_id: "02"
category_name: "Inference Accelerators"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-08-13"
refresh_count: 2
total_companies: 9
active_companies: 8
archived_companies: 1
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$6B+ [ESTIMATED], excluding the ~$20B NVIDIA-Groq licence"
top_investors: ["Sequoia", "Jane Street", "General Atlantic", "BlackRock", "Temasek", "Arm", "QIA", "SK hynix"]
key_technical_inflections: ["Cost-per-token economics", "Deterministic low-latency serving", "Transformer-specialized ASICs", "Memory-centric inference", "Sovereign inference clouds", "Prefill/decode disaggregation", "HBM-free inference architectures"]
key_open_questions: ["Does CUDA lock-in hold for inference?", "Will transformer-hardwired ASICs survive architecture drift?", "Who wins reasoning/long-context serving?", "After NVIDIA licensed Groq's LPU tech, is deterministic low-latency still a startup category or an NVIDIA product line?", "Do lab-commissioned merchant ASICs (OpenAI/Broadcom) foreclose the merchant inference market?"]
---

# 02 — Inference Accelerators

> The best risk/reward in the landscape: the market is shifting from training to serving, and cost-per-token is a board-level metric. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis

- **Why now:** LLM serving cost is the dominant AI opex; transformer architecture is stable enough to specialize silicon against; CUDA lock-in is weaker for inference than training.
- **Venture-scale potential:** High — startups can win on perf/$ and perf/W, especially deterministic low-latency, high-throughput batch, and reasoning/long-context serving.
- **Key inflections:** Cost-per-token, deterministic latency, transformer-hardwired ASICs (Etched bet), memory-centric inference (d-Matrix), sovereign/regional inference clouds.
- **Market pull:** Inference now dwarfs training in aggregate compute; enterprises want NVIDIA alternatives where switching cost is lower.
- **Likely acquirers:** AMD, Qualcomm, hyperscalers, networking incumbents. **Exit:** M&A or IPO (Groq scale).
- **Why incumbents may dominate/fail:** NVIDIA can cut inference prices and ships strong serving software; startups "win" by being dramatically better on a specific axis (latency, $/token) with real software.
- **Winning startup:** Differentiated serving silicon + a working compiler + multi-customer revenue. **Non-investable:** undifferentiated GPU + no software + no customers.

## 2. Market Context

- **Structure:** NVIDIA dominant but contestable; hyperscaler in-house (TPU/Trainium-Inferentia/Maia); merchant challengers; sovereign clouds.
- **Segments:** AI clouds, enterprises, sovereign/regional clouds, API providers.
- **Adoption drivers:** $/token, latency SLAs, power, supply availability, data residency.
- **Bottlenecks:** Memory bandwidth/capacity, software/compiler maturity, model-architecture drift.
- **Supply chain:** TSMC, HBM/LPDDR, advanced packaging.
- **Competitive landscape:** NVIDIA (inference), AMD MI-series, Inferentia, Groq, d-Matrix, Etched, SambaNova, Positron, Rebellions, FuriosaAI.
- **Funding env:** Strong for credible serving economics + traction; Groq/SambaNova mega-rounds.
- **Recent M&A/exits:** Untether AI wound down, IP to AMD (2025); see [../deal_tracker/23_exit_and_shutdown_tracker.md](../deal_tracker/23_exit_and_shutdown_tracker.md).
- **Comparables:** NVIDIA, AMD, **Cerebras (NASDAQ: CBRS)**. **Risks:** software ecosystem, NVIDIA price response, architecture drift.

### 2026 Update — what changed since the last refresh (2026-08-13)

This category moved more than any other, and in two opposite directions at once.

- **NVIDIA took Groq's technology and its founder — for ~$20B.** In December 2025, NVIDIA agreed to pay approximately **$20B for a non-exclusive licence** to Groq's LPU inference technology and to hire founder/CEO Jonathan Ross, President Sunny Madra and other senior leaders. Groq continues as an independent company (CEO Simon Edwards, formerly CFO), re-staffed, and raised a further **~$650M in June 2026** led by Disruptive and Infinitum — at roughly **$6B, below its ~$6.9B September 2025 mark**. US senators opened an inquiry in March 2026 into whether the structure was designed to avoid Hart-Scott-Rodino review [TO VERIFY current status].
  - **What this means for the thesis:** the single strongest validation the category has ever received *and* the removal of its flagship independent competitor. Deterministic low-latency inference is now, in part, an NVIDIA roadmap item.
- **Etched became the category's price-setter.** ~$500M at ~$5B (Dec 2025), then a **~$300M Series C at ~$10.3B led by Sequoia** (2026-07-23) with a16z, Jane Street, Diffusion and **SK hynix** — roughly doubling its valuation in about seven months, reportedly on first working Sohu silicon (TSMC N4P) and >$1B of customer contracts [TO VERIFY]. The transformer-hardwiring bet is no longer theoretical; the architecture-drift risk is unchanged.
- **Positron reached unicorn status on a shipping product.** ~$230M Series B at >$1B post (Feb 2026), co-led by ARENA Private Wealth, Jump Trading and Unless, with **QIA, Arm and Helena**. Atlas is shipping; the custom "Asimov" silicon targets tape-out in late 2026 and production in early 2027. Reports of a further ~$750M raise in discussion [UNCONFIRMED].
- **d-Matrix became a systems company.** ~$275M Series C (late 2025) at ~$2B, total ~$450M — and then **acquired GigaIO's SuperNODE and FabreX assets** in 2026. Selling racks, not chips, is now the default posture in this category.
- **Korea consolidated into an IPO story.** Rebellions raised ~$400M pre-IPO (March 2026) including **₩250B (~$178M) from Korea's National Growth Fund**, at roughly ₩3.4T, with its listing pushed to H1 of next year; FuriosaAI is in market for a ~$300–500M Series D / pre-IPO round at about ₩3T targeting a 2028 listing, after beginning volume RNGD shipments and signing LG CNS [TO VERIFY]; DeepX sits around ₩2.85T with a 2027–28 IPO target.
- **New entrant worth tracking: OLIX (London)** — $312M Series B at ~$3.3B (Aug 2026), Europe's largest semiconductor venture round, building optical tensor processing units that eliminate HBM from the inference datapath. Covered in [06](06_optical_interconnect_and_cpo.md) but competes squarely here.
- **The substitution risk is now concrete:** OpenAI and Broadcom's **"Jalapeño"** LLM inference accelerator (unveiled 2026-06-24, ~9 months design-to-tape-out, claimed ~50% cost advantage, 10GW program) shows a frontier lab can get specialized inference silicon without buying a startup's chip.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Technical Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|---------------------------|----------|--------------|--------|
| Groq | US | 2016 | **Late; post-NVIDIA licence** | ~$2.4B [TO VERIFY] | Disruptive, Infinitum, BlackRock, Samsung, Cisco | LPU + GroqCloud | API/cloud inference | Deterministic SRAM dataflow, ultra-low latency | ~$20B NVIDIA licence (2025-12); founder/CEO left; ~$650M raise at ~$6B (2026-06) | High (special situation) | Active |
| d-Matrix | US | 2019 | **Series C (2025-11)** | ~$450M [TO VERIFY] | Temasek, M12, Playground | Corsair + JetStream; SuperNODE/FabreX (ex-GigaIO) | DC inference | Digital IMC (SRAM) + chiplets, now rack-scale systems | ~$2B valuation; acquired GigaIO assets 2026 | High | Active |
| Etched | US | 2022 | **Series C (2026-07)** | ~$800M+ [TO VERIFY] | Sequoia, a16z, Jane Street, SK hynix | Sohu — transformer-hardwired ASIC | Transformer serving | Hardwires transformer into silicon for max throughput | ~$10.3B valuation; first silicon on TSMC N4P; >$1B contracts [TO VERIFY] | High | Active |
| SambaNova | US | 2017 | **Series F (2026-07)** | ~$2.1B [TO VERIFY] | General Atlantic, SoftBank, BlackRock | SN40L systems | Enterprise/gov inference | Dataflow + 3-tier memory; agentic serving | ~$11B post; JPMorganChase partner [TO VERIFY] | Medium-High | Active (see [01](01_training_accelerators.md)) |
| Positron AI | US | 2023 | **Series B (2026-02)** | ~$280M+ [TO VERIFY] | ARENA, Jump Trading, Unless, QIA, Arm | Atlas appliance; "Asimov" custom silicon | Memory-bound LLM inference | Memory-optimized, power-efficient transformer inference | Unicorn; Atlas shipping, Asimov tape-out late 2026 | High | Active |
| Rebellions | KR | 2020 | **Pre-IPO (2026-03)** | ~$725M+ [TO VERIFY] | Korea National Growth Fund, KT, Temasek | ATOM/REBEL inference chips | Korea/Asia DC, sovereign | Energy-efficient inference; merged w/ Sapeon | ~₩3.4T valuation; IPO deferred to H1 next year | Medium-High | Active |
| FuriosaAI | KR | 2017 | **Series D / pre-IPO (in market)** | ~$325M+ [TO VERIFY] | DSC, Naver, Crit | RNGD (Tensor Contraction Processor) | DC inference, sovereign | TCP arch, high efficiency; declined Meta bid (2025) | Volume RNGD shipments; LG CNS; ~₩3T target [UNCONFIRMED] | Medium-High | Active |
| OLIX | UK | 2024 | **Series B (2026-08)** | ~$350M+ [TO VERIFY] | Hummingbird, Plural, Creandum, Arm, HRT | X-1 platform / DX-1 optical TPU | Frontier decode inference | Photonic tensor compute; removes HBM from the datapath | ~$3.3B valuation; Europe's largest semi VC round | High (high-variance) | Active — see [06](06_optical_interconnect_and_cpo.md) |
| Untether AI | CA | 2018 | Wound down | ~$150M raised | Intel Cap, Tracker, CPPIB | At-memory compute (speedAI) | DC/edge inference | At-memory compute architecture | Assets/IP→AMD 2025 | Archived | Shut Down |

## 4. Company Profiles

### Groq

- **Status:** Active · **HQ:** Mountain View, US · **Founded:** 2016
- **Founders:** Jonathan Ross (ex-Google TPU), Douglas Wightman
- **Stage:** Late — **special situation post-NVIDIA licence** · **Total Funding:** ~$2.4B [TO VERIFY] · **Round history:** ~$640M Series D (2024, BlackRock) → ~$750M at ~$6.9B (2025-09) → **~$650M at ~$6B, June 2026, led by Disruptive and Infinitum**
- **Leadership change (2025-12):** founder/CEO **Jonathan Ross** and President **Sunny Madra** left for NVIDIA as part of the ~$20B licence-and-hire transaction; former CFO **Simon Edwards** is now CEO
- **Key/Strategic Investors:** Disruptive, Infinitum, BlackRock, Samsung Catalyst, Cisco Investments, Tiger Global, Sequoia [TO VERIFY] · **Employees:** ~300+, re-staffing after the NVIDIA hires [ESTIMATED] · **Website:** groq.com
- **Primary:** 02 · **Secondary:** 16 DC Infra
- **One-Line:** Deterministic Language Processing Unit (LPU) and GroqCloud delivering industry-leading inference latency/throughput.

#### Product / Technology
- **Builds:** LPU inference chips + GroqCloud API + on-prem systems. **Architecture:** software-scheduled, deterministic dataflow with large on-chip SRAM, no external HBM — predictable ultra-low latency. **Claims:** leading tokens/sec/user at low latency. **Software:** Groq compiler maps models to deterministic schedule. **Deps:** mature node (no HBM dependence is a supply advantage). **Differentiation:** determinism + latency; **risk:** SRAM capacity limits model size per chip → many chips per large model (system cost).

#### Market / Traction / Competitive
- **Customers:** GroqCloud developers, Aramco Digital/Saudi sovereign inference build-out [TO VERIFY], enterprise. **GTM:** cloud API + sovereign data-center deals. **Competitors:** NVIDIA, SambaNova, Cerebras inference, Together/Fireworks (software). **Defensibility:** latency + compiler + cloud distribution.

#### The NVIDIA transaction (2025-12) — how to read it
- **Structure:** ~$20B for a **non-exclusive** licence to the LPU inference technology plus the hiring of the founder/CEO, president and senior staff. Not a merger; Groq remains an independent company and kept its IP on a non-exclusive basis. Reported as NVIDIA's largest transaction on record.
- **Why NVIDIA paid:** deterministic, SRAM-resident serving is the one regime where an HBM-centric GPU is structurally disadvantaged. Buying the licence and the team removes an architectural threat without a merger filing.
- **Regulatory:** a Senate inquiry (Warren, Blumenthal, March 2026) argues the structure is a reverse acquihire designed to avoid HSR review [TO VERIFY outcome]. If the structure is successfully challenged, it changes the exit calculus for every startup in this database.
- **Where it left Groq:** funded (~$650M more in June 2026) but at a **lower valuation than nine months earlier**, without its founding leadership, and competing against a licensee with unlimited manufacturing scale. Reported Groq 3 specifications (150 TB/s on-chip SRAM bandwidth, ~315 PFLOPS FP8/rack, Samsung 4nm, shipping Q3 2026) are vendor figures [TO VERIFY].

#### VC Investment View
- **Attractiveness:** High but as a **special situation**, not a growth story · **Why now:** the technology is validated at the highest price ever paid in the category; the company that owns it is cheaper than it was a year ago. **Upside:** licence proceeds plus a re-staffed independent cloud business. **Downside:** the architects are at NVIDIA, and the licensee is the competitor. **Exit:** IPO/strategic; the licence may already have been the exit for some holders.
- **Diligence Qs (new):** How were the licence proceeds allocated between company and individuals? What technical leadership remains? Does the licence constrain Groq's own roadmap or customers? What is GroqCloud revenue and gross margin now?
- **Data quality:** Medium. **Verify next:** licence terms, post-deal engineering retention, GroqCloud revenue, Senate inquiry outcome. **Last updated:** 2026-08-13.

### d-Matrix

- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2019
- **Founders:** Sid Sheth, Sudeep Bhoja (ex-Inphi/Marvell/Broadcom)
- **Stage:** Series C · **Total Funding:** ~$450M [TO VERIFY] · **Last Round:** **~$275M Series C at ~$2B, November 2025** [TO VERIFY]; prior ~$110M Series B led by Temasek, 2023
- **M&A (2026):** acquired **GigaIO's SuperNODE and FabreX** assets — moving from chiplets to rack-scale systems [TO VERIFY terms]
- **Key Investors:** Temasek, M12 (Microsoft), Playground Global, Nautilus, Industry Ventures · **Website:** d-matrix.ai
- **Primary:** 02 · **Secondary:** 07 Memory, 04 Chiplets
- **One-Line:** Digital in-memory compute (DIMC) chiplet platform ("Corsair") for low-latency, cost-efficient datacenter inference.

#### Product / Technology
- Digital in-memory compute in SRAM + chiplet/3D packaging; targets generative/batch inference with high throughput-per-dollar and memory-bound efficiency. **Differentiation:** DIMC avoids analog-IMC accuracy issues while cutting memory movement energy. **Risks:** software stack maturity, scaling to largest models.

#### VC View
- **Attractiveness:** High · **Venture-scale:** High · **Acquirers:** AMD, Marvell, Broadcom, hyperscalers. **Risks:** competition, software, sales cycle.
- **2026 read:** the GigaIO asset purchase is the tell for the whole category — customers buy deployable racks with a fabric, not accelerator cards. Model the systems BOM, inventory and support cost, because the gross-margin profile of a systems company is not the gross-margin profile of a chip company. **Data quality:** Medium. **Verify next:** Series C final terms, JetStream/Corsair revenue, GigaIO integration. **Last updated:** 2026-08-13.

### Etched

- **Status:** Active · **HQ:** Cupertino, US · **Founded:** 2022
- **Founders:** Gavin Uberti, Chris Zhu, Robert Wachen (Harvard dropouts)
- **Stage:** Series C · **Total Funding:** ~$800M+ [TO VERIFY] · **Round history:** ~$120M Series A (2024) → **~$500M at ~$5B (2025-12)** → **~$300M Series C at ~$10.3B led by Sequoia (2026-07-23)** with a16z, Jane Street, Diffusion and **SK hynix** [TO VERIFY]
- **Reported traction:** first working Sohu silicon on TSMC N4P; **>$1B in customer contracts** [TO VERIFY — company-reported]
- **Website:** etched.com · **Primary:** 02
- **One-Line:** "Sohu" — an ASIC with the transformer architecture hardwired into silicon, betting on transformer dominance for extreme throughput.

#### Product / Technology
- Transformer-specialized ASIC (no general-purpose flexibility); claims order-of-magnitude throughput vs. GPUs for transformer inference. **Differentiation:** maximal specialization. **Risk (central):** architecture drift — if dominant models move away from vanilla transformers (e.g., new attention/SSM hybrids), the bet erodes. Pre-revenue; execution/tape-out risk.

#### VC View
- **Attractiveness:** High (high-variance) · **Venture-scale:** High · **Why now:** transformer ubiquity + inference cost. **Upside:** dominant transformer-serving ASIC. **Downside:** architecture obsolescence, single-product risk. **Exit:** strategic/IPO. **Acquirers:** hyperscalers, NVIDIA/AMD.
- **2026 read:** the valuation went from ~$5B to ~$10.3B in about seven months, which prices in a successful ramp of a single, maximally specialized product. Two things changed the risk profile in Etched's favor — working silicon and contracted demand — and one did not: if frontier serving drifts toward hybrid attention/SSM or heavy MoE routing, hardwiring is a liability. **SK hynix on the cap table is the important detail** for memory supply. **Diligence:** what exactly is in the ">$1B contracts" figure (bookings vs. LOIs vs. prepaid), yield on N4P, and what fraction of the datapath is actually fixed-function.
- **Data quality:** Medium (first silicon, but company-reported traction). **Verify next:** contract composition, shipping customers, whether the reported August 2026 late-stage raise is separate from the Series C. **Last updated:** 2026-08-13.

> Rebellions, FuriosaAI and OLIX are covered at table level plus the lighter entries below; Positron now has a full profile; Untether AI archived (see [../deal_tracker/23_exit_and_shutdown_tracker.md](../deal_tracker/23_exit_and_shutdown_tracker.md)).

### Positron AI (promoted from lighter coverage, 2026-08-13)

- **Status:** Active · **HQ:** Reno, US · **Founded:** 2023 · **Stage:** Series B · **Total Funding:** ~$280M+ [TO VERIFY]
- **Rounds:** ~$51.6M Series A (2025-07) → **~$230M Series B at >$1B post (2026-02)**, co-led by ARENA Private Wealth, Jump Trading and Unless, with **QIA, Arm and Helena**; reports of a further ~$750M raise in discussion [UNCONFIRMED]
- **Product:** **Atlas** — a shipping, memory-optimized inference appliance (FPGA-based) — with **Asimov**, its first custom silicon, targeting tape-out in late 2026 and production in early 2027.
- **Why it matters:** Positron is the clearest case in the database of the *ship-first, tape-out-later* strategy — revenue from FPGA systems funds the ASIC, which inverts the normal capital profile of a chip startup. It reached unicorn status in roughly 2.5 years.
- **VC view:** Attractiveness High. **Risks:** the FPGA-to-ASIC transition is where this strategy usually breaks (different team, different economics, 18-month gap); competing against NVIDIA's Rubin generation on the exact axis NVIDIA is optimizing. **Diligence:** revenue quality and repeat orders on Atlas, Asimov tape-out schedule and PDK access, whether Arm's investment comes with a CPU/interconnect commitment. **Data quality:** Medium. **Last updated:** 2026-08-13.

**Rebellions (KR)** — merged with SK-backed Sapeon; ATOM/REBEL inference chips; **raised ~$400M pre-IPO in March 2026 including ₩250B (~$178M) from Korea's National Growth Fund, at roughly ₩3.4T; IPO deferred to H1 next year** [TO VERIFY]. The most explicitly state-backed AI silicon company in the database. **FuriosaAI (KR)** — RNGD TCP inference chip in volume shipment, LG CNS partnership; declined a Meta acquisition offer (~$800M) in 2025; **in market for a ~$300–500M Series D / ~₩750B pre-IPO round at about ₩3T, IPO targeted for H2 2028** [UNCONFIRMED — not closed]. **OLIX (UK)** — see [06](06_optical_interconnect_and_cpo.md); photonic decode accelerator competing directly on $/token without HBM.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Deterministic low-latency serving | High | High | High | **Very High (NVIDIA now licenses it)** | Narrowed | Medium |
| Digital in-memory compute | High | High | Medium-High | Medium | Real (d-Matrix) | High |
| Transformer-hardwired ASIC | High | High | High | Medium | Proven-out (Etched: silicon + contracts) | High |
| Sovereign/regional inference | High | Medium | High | Medium | Real (Rebellions/Furiosa) — now state-funded | Medium-High |
| Memory-optimized appliances | Medium-High | Medium | Medium | Medium | Real (Positron: ship FPGA, fund ASIC) | Medium-High |
| Rack-scale inference systems | High | Medium-High | High | High | Real (d-Matrix/GigaIO) — the default posture | Medium-High |
| Photonic inference compute | Medium-High | Very High | High | Low today | Early (OLIX) — removes HBM from the datapath | Medium (high-variance) |
| Lab-commissioned merchant ASIC | High | High | Very High | — | **Not a startup opportunity — a competitive threat** (OpenAI/Broadcom) | n/a |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| BlackRock | Crossover | Groq | Growth | Led Groq D | Inference cloud at scale |
| Temasek | Sovereign | d-Matrix, Rebellions | B–Growth | Led d-Matrix B | Asia + efficiency |
| Samsung Catalyst | Strategic | Groq | A–Growth | Groq backer | Memory/foundry adjacency |
| M12 (Microsoft) | Strategic | d-Matrix | A–B | d-Matrix | Hyperscaler inference signal |
| Atreides / Valor | VC/Crossover | Positron | A–Growth | Positron | Memory-bound inference |
| Sequoia | VC | Etched | A–Growth | Led Etched $300M C at ~$10.3B (2026-07) | Specialization beats generality in serving |
| Jane Street | Prop/quant | Etched, MatX | B–Growth | Etched C; MatX B | Latency-native diligence; balance-sheet checks |
| Jump Trading / ARENA / Unless | Prop/quant + wealth | Positron | B | Co-led Positron $230M B (2026-02) | Ship-first, tape-out-later economics |
| Arm | Strategic | Positron, Eliyan, OLIX | B–Growth | Three inference-adjacent bets in 2026 | Buying optionality outside its IP business |
| SK hynix | Strategic | Etched | Growth | Etched C (2026-07) | Memory supply aligned to the winning ASIC |
| Korea National Growth Fund | Sovereign | Rebellions | Pre-IPO | ₩250B (2026-03) | State-directed "K-NVIDIA" program |
| Disruptive / Infinitum | Growth | Groq | Growth | Led Groq ~$650M (2026-06) | Backing the post-licence residual business |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Startup Formation Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------------------------|----------------|:------------:|------------|
| Song Han | MIT | Efficient inference, quantization | AWQ/SmoothQuant define serving efficiency; OmniML→NVIDIA | Likely Startup Signal | Deep Compression, AWQ | 5 | High |
| Tri Dao | Princeton/Together | FlashAttention, SSMs (Mamba) | Attention/SSM kernels shape inference silicon targets | Likely (Together) | FlashAttention, Mamba | 5 | High |
| Jonathan Ross | **NVIDIA (ex-Groq, ex-Google)** | Deterministic compute | Founder pedigree; TPU lineage — **moved to NVIDIA in the 2025-12 licence deal**; his next team is inside the incumbent | Confirmed (Groq); now incumbent | TPU lineage | 4 | High |
| Stanford/Berkeley systems | Stanford/UCB | Serving systems (vLLM lineage) | Software that defines hardware needs | Watchlist | vLLM, PagedAttention | 4 | Medium |

## 8. Diligence Questions

- **Technical:** Independent perf/$ & latency benchmarks? Compiler/runtime maturity? Largest model that fits efficiently?
- **Market:** Serviceable inference TAM and segment? Latency-sensitive vs. batch positioning?
- **Customer:** Committed cloud/enterprise revenue vs. pilots? Concentration?
- **Competitive:** Survives NVIDIA inference price cuts + Dynamo/vLLM ubiquity?
- **Financial:** Chips-per-model cost economics? Path to gross-margin-positive serving?
- **Founder:** Silicon + compiler track record? Cloud GTM capability?
- **Exit:** Strategic logic for AMD/Qualcomm/hyperscaler acquisition? IPO scale?
- **(2026) Substitution:** Why would this customer not commission a Broadcom/Marvell ASIC instead? OpenAI went design-to-tape-out in ~9 months.
- **(2026) Licence+hire:** If NVIDIA offered a non-exclusive licence plus the founding team, what would our position be worth? Who signs, who gets paid, what remains?
- **(2026) Systems reality:** Are we selling chips, cards, or racks? Price the fabric, integration, inventory and support — the Corsair/GigaIO path is now the norm.
- **(2026) Memory supply:** Is there an HBM/LPDDR allocation commitment, and does a memory vendor sit on the cap table (SK hynix→Etched, Samsung→several)?

## 9. Refresh Notes

| Date | Refresh Type | Entries Added | Entries Updated | Entries Archived | Key Changes | Sources |
|------|--------------|---------------|-----------------|------------------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | 1 (Untether AI) | Initial build; full profiles Groq/d-Matrix/Etched; KR players; heatmap/investors/research | Company sites, trade press |
| 2026-08-13 | Full refresh | 2 (OLIX, Positron promoted) | 7 (Groq, Etched, d-Matrix, Rebellions, FuriosaAI, heatmap, investors) | 0 | NVIDIA's ~$20B Groq licence-and-hire and its aftermath (leadership exit, ~$650M down-round-ish raise); Etched to ~$10.3B with first silicon; Positron unicorn; d-Matrix Series C + GigaIO assets; Korea pre-IPO rounds and state capital; added rack-scale, photonic and merchant-ASIC rows to the heatmap and four new diligence questions | Company releases, trade press [many TO VERIFY] |
