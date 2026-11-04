---
category_id: "02"
category_name: "Inference Accelerators"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 10
active_companies: 7
archived_companies: 3
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$8B+ [ESTIMATED]"
top_investors: ["Sequoia", "Temasek", "Korea National Growth Fund", "Disruptive", "Jane Street", "Accel", "Founders Fund", "Mirae Asset", "BlackRock"]
key_technical_inflections: ["Cost-per-token economics", "Deterministic low-latency serving", "Transformer-specialized ASICs", "Model-specific (hardwired-weight) silicon", "Memory-centric inference", "Prefill/decode disaggregation", "Sovereign inference clouds"]
key_open_questions: ["Does CUDA lock-in hold for inference?", "Will transformer-hardwired ASICs survive architecture drift?", "Who wins reasoning/long-context serving?", "Are license-and-hire deals (NVIDIA–Groq) the new exit template?", "Can frontier-lab offtake contracts (OpenAI, Anthropic) anchor startups before silicon ships?"]
---

# 02 — Inference Accelerators

> The best risk/reward in the landscape — and the category where 2025–2026 exits happened: NVIDIA licensed Groq's LPU and hired its leadership (~$20B reported), AMD agreed to buy Taalas, and frontier labs signed direct offtake deals with startups. See [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md).

## 1. VC Investment Thesis

- **Why now:** LLM serving cost is the dominant AI opex; reasoning/agentic workloads multiply tokens; transformer architecture is stable enough to specialize silicon against; CUDA lock-in is weaker for inference than training.
- **Validation in 2025–2026:** (1) **NVIDIA–Groq** non-exclusive license + hiring of founder Jonathan Ross, president Sunny Madra and engineers (announced 2025-12-24; ~$20B reported) [CONFIRMED structure; value per CNBC/investor sources] — NVIDIA paid to own low-latency SRAM inference; (2) **AMD–Taalas** acquisition agreement (Aug 2026) [CONFIRMED — AMD release]; (3) frontier-lab offtake: **OpenAI–Cerebras** >$10B/750 MW (Jan 2026) and a reported **Anthropic–Fractile** ~$250M chip agreement (Aug 2026) [UNCONFIRMED]; (4) Korean sovereign capital (National Growth Fund) backing Rebellions and FuriosaAI.
- **Venture-scale potential:** High — startups can win on perf/$ and perf/W, especially deterministic low-latency decode, memory-capacity-bound serving, and model-specific silicon.
- **Key inflections:** Cost-per-token; prefill/decode disaggregation (GPUs for prefill, specialized silicon for decode — the stated AMD–Taalas rationale); transformer-hardwired ASICs (Etched); hardwired-weights silicon (Taalas); memory-centric inference (d-Matrix, Positron, Fractile); sovereign inference clouds.
- **Market pull:** Inference now dwarfs training in aggregate compute; frontier labs want non-NVIDIA capacity and will pre-buy.
- **Likely acquirers:** NVIDIA (license + acqui-hire), AMD (Untether team 2025, Taalas 2026), Intel, Qualcomm, Marvell/Broadcom, hyperscalers. **Exit:** M&A/licensing or IPO (Korean IPO window for Rebellions/FuriosaAI).
- **Why incumbents may dominate/fail:** NVIDIA can cut inference prices, ships strong serving software (Dynamo), and now owns Groq IP; startups "win" by being dramatically better on a specific axis (latency, $/token, memory capacity) with real software.
- **Winning startup:** Differentiated serving silicon + a working compiler + a committed anchor customer. **Non-investable:** undifferentiated GPU + no software + no customers.

## 2. Market Context

- **Structure:** NVIDIA dominant (now incl. Groq LPU IP) but contestable; hyperscaler in-house (Google TPU v7 Ironwood, AWS Trainium3/Inferentia, Microsoft Maia 200, Meta MTIA) and the OpenAI–Broadcom custom accelerator program (10 GW, deployments from H2 2026) [CONFIRMED announcement; status TO VERIFY]; merchant challengers; sovereign clouds. Hyperscaler figures are context only — see [01](01_training_accelerators.md).
- **Segments:** Frontier labs (offtake contracts), AI clouds, enterprises, sovereign/regional clouds, API providers.
- **Adoption drivers:** $/token, latency SLAs, power, supply availability, data residency.
- **Bottlenecks:** Memory bandwidth/capacity (HBM4 allocation), software/compiler maturity, model-architecture drift, SRAM capacity per chip.
- **Supply chain:** TSMC, HBM/LPDDR, advanced packaging; Samsung Foundry for Korean players.
- **Competitive landscape:** NVIDIA (Blackwell/Rubin + Groq IP), AMD MI-series (+ Taalas), Inferentia/Trainium, TPU, Cerebras (public), Groq residual cloud, d-Matrix, Etched, SambaNova, Positron, Rebellions, FuriosaAI, Fractile, MatX.
- **Funding env (2026):** Extremely strong — Etched $500M @ $5B (Jan), $300M @ $10.3B (Jul, SK hynix participating) and a reported $700M @ ~$21B (Aug, Jane Street) [TO VERIFY]; Positron $230M @ >$1B (Feb); Taalas $169M (Feb); Rebellions $400M pre-IPO (Mar); Fractile $220M (May) with reported talks at $6.5B (Aug); Groq residual $650M (Jun); FuriosaAI $620M @ $2.9B (Oct).
- **Recent M&A/exits:** Untether AI wound down, team acqui-hired by AMD (2025); NVIDIA–Groq license + acqui-hire (Dec 2025); Intel–SambaNova talks ended (Jan 2026); AMD–Taalas (Aug 2026). See [../deal_tracker/23_exit_and_shutdown_tracker.md](../deal_tracker/23_exit_and_shutdown_tracker.md) and [../deal_tracker/20_ma_tracker.md](../deal_tracker/20_ma_tracker.md).
- **Comparables:** NVIDIA, AMD; Cerebras (Nasdaq: CBRS, IPO May 2026, ~$56B fully diluted at IPO price).
- **Risks:** software ecosystem, NVIDIA price response, architecture drift, regulatory scrutiny of license-and-hire deals (DOJ reportedly examining NVIDIA–Groq structure [UNCONFIRMED — per NYT via Business Insider]).

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Technical Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|---------------------------|----------|--------------|--------|
| Groq | US | 2016 | Licensed/acqui-hired; residual GroqCloud growth-stage | ~$3B [ESTIMATED] | BlackRock, Disruptive, Samsung, Cisco | LPU (IP licensed to NVIDIA) + GroqCloud | API/cloud inference | Deterministic SRAM dataflow, ultra-low latency | NVIDIA license + leadership hire (Dec 2025); GroqCloud continues under CEO Simon Edwards | High (exit precedent) | Licensed/Acqui-hired (residual GroqCloud active) |
| d-Matrix | US | 2019 | Series C | ~$450M [CONFIRMED] | Bullhound, Triatomic, Temasek | Corsair (digital in-memory compute) | DC inference | Digital IMC (SRAM) + chiplets for low-latency batch | $275M Series C @ $2B (Nov 2025) | High | Active |
| Etched | US | 2022 | Series C | ~$1.1B [ESTIMATED] | Sequoia, Stripes, Primary, Positive Sum | Sohu — transformer-hardwired ASIC | Transformer serving | Hardwires transformer into silicon for max throughput | Working Sohu silicon; >$1B signed orders (company claim, Jun 2026); $10.3B (Jul 2026) → reported $700M at ~$21B led by Jane Street (Aug 2026) [TO VERIFY] | High | Active |
| SambaNova | US | 2017 | Series D+ (strategic) | ~$1.1B+ [TO VERIFY] | SoftBank, BlackRock, Intel Capital | SN40L systems, SambaCloud | Enterprise/gov inference | Dataflow + 3-tier memory; agentic serving | Intel partnership + 8.2% stake (Feb 2026) | Medium | Active (see [01](01_training_accelerators.md)) |
| Positron AI | US | 2023 | Series B | ~$300M+ [ESTIMATED] | ARENA Private Wealth, Jump Trading, Unless, Valor | Atlas appliance; Asimov ASIC | Memory-bound LLM inference | Memory-first design (claims ~2 TB/accelerator for Asimov) | $230M Series B @ >$1B (Feb 2026); Asimov tape-out late 2026 | High | Active |
| Rebellions | KR | 2020 | Pre-IPO | ~$850M [ESTIMATED] | Mirae Asset, Korea National Growth Fund, KT, Samsung, Arm | ATOM/REBEL chips; RebelRack/RebelPOD | Korea/Asia DC, sovereign, US expansion | Energy-efficient inference; merged w/ Sapeon | $400M pre-IPO @ ~$2.3B (Mar 2026); KR IPO targeted | Medium-High | Active |
| FuriosaAI | KR | 2017 | Series D | ~$1B [ESTIMATED] | Korea National Growth Fund, DSC, Naver | RNGD (Tensor Contraction Processor) | DC inference, sovereign, enterprise | TCP arch, high efficiency; declined Meta bid (2025) | $620M Series D @ $2.9B (Oct 2026); LG customer | High | Active |
| Fractile | UK | 2022 | Series B | ~$240M [ESTIMATED] | Accel, Founders Fund, Factorial Funds | In-memory-compute inference chips/systems | Frontier-lab inference | Compute-in-memory for fast decode | $220M Series B (May 2026); reported ~$250M Anthropic deal; talks @ $6.5B [UNCONFIRMED] | High | Active |
| Taalas | CA | 2023 | Acquired (AMD, Aug 2026) | ~$219M [CONFIRMED] | Quiet Capital, Fidelity, Pierre Lamond | HC1/HC2 model-specific "hardcore" chips | Token generation / decode | Model weights etched into 2 of ~100 metal layers; ~2-month turn | AMD acquisition agreement (Aug 2026) | Archived | Acquired (AMD; closing TO VERIFY) |
| Untether AI | CA | 2018 | Wound down | ~$150M raised | Intel Cap, Tracker, CPPIB | At-memory compute (speedAI) | DC/edge inference | At-memory compute architecture | Team acqui-hired by AMD 2025 | Archived | Shut Down |

## 4. Company Profiles

### Groq

- **Status:** Licensed/Acqui-hired (Dec 2025); residual Groq Inc. operates GroqCloud independently · **HQ:** Mountain View, US · **Founded:** 2016
- **Founders:** Jonathan Ross (ex-Google TPU; now at NVIDIA), Douglas Wightman
- **NVIDIA deal (announced 2025-12-24):** Non-exclusive license of Groq's LPU inference technology; Jonathan Ross, President Sunny Madra and other engineers joined NVIDIA; no equity acquisition [CONFIRMED — Groq/NVIDIA statements]. Value **~$20B cash reported** (CNBC, citing Disruptive CEO Alex Davis), terms undisclosed [TO VERIFY]. Per Davis, NVIDIA took all assets except the cloud business [UNCONFIRMED]. Jensen Huang reportedly told staff "we are not acquiring Groq as a company." DOJ reportedly examining the structure [UNCONFIRMED].
- **Residual company:** CEO **Simon Edwards** (ex-CFO). GroqCloud "continues without interruption" [CONFIRMED — Groq]. Reported footprint: ~13 datacenters, millions of developers [UNCONFIRMED — Business Insider]. Some customers reported weaker support/model selection post-deal [UNCONFIRMED].
- **Funding:** Series D ~$640M (Aug 2024, BlackRock-led, $2.8B); **$750M at $6.9B (Sep 2025, Disruptive-led)** [CONFIRMED]; post-deal **$650M growth round led by Disruptive and Infinitum (Jun 2026)** [TO VERIFY — valuation reports conflict]; Bloomberg reported a raise of ~$350M at **~$3.5B valuation** (Aug 2026), roughly half the 2025 mark [CONFIRMED per Bloomberg; relationship to June round TO VERIFY]. Pre-deal investors received distributions from the NVIDIA payment [UNCONFIRMED].
- **Key/Strategic Investors:** BlackRock, Disruptive, Samsung Catalyst, Cisco Investments, Tiger Global, KSA-linked commitments (~$1.5B, Feb 2025) [TO VERIFY] · **Website:** groq.com
- **Primary:** 02 · **Secondary:** 16 DC Infra
- **One-Line:** Deterministic LPU inventor whose chip IP and leadership went to NVIDIA via license-and-hire; the remaining company is an inference cloud (GroqCloud).

#### Product / Technology
- **Builds:** LPU inference chips (IP now licensed non-exclusively to NVIDIA) + GroqCloud API + sovereign DC builds. **Architecture:** software-scheduled, deterministic dataflow with large on-chip SRAM, no HBM. **Open question:** whether residual Groq continues its own LPU roadmap or becomes a pure cloud operator on existing silicon [TO VERIFY].

#### Market / Traction / Competitive
- **Customers:** GroqCloud developers and enterprises; Saudi (Aramco Digital/HUMAIN) sovereign inference build-out [TO VERIFY current]. **Competitors:** NVIDIA (now with Groq IP), Cerebras, SambaNova, Together/Fireworks. **Defensibility:** cloud distribution; chip IP no longer exclusive.

#### VC Investment View
- **Attractiveness:** Exited for early holders (license-and-hire); residual GroqCloud equity is a different, cloud-economics bet at ~$3.5B [per Bloomberg]. **Lesson:** NVIDIA prefers licensing + talent deals that avoid merger review; early-stage cap tables should model this outcome. **Data quality:** Medium. **Last updated:** 2026-11-04.

### d-Matrix

- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2019
- **Founders:** Sid Sheth, Sudeep Bhoja (ex-Inphi/Marvell/Broadcom)
- **Stage:** Series C · **Total Funding:** ~$450M [CONFIRMED — company] · **Last Round:** **$275M Series C at $2B valuation (2025-11-12)**, co-led by Bullhound Capital, Triatomic Capital and Temasek; new investors incl. Qatar Investment Authority and EDBI [CONFIRMED — company release/Bloomberg]
- **Key Investors:** Temasek, M12 (Microsoft), Playground Global, Nautilus, Industry Ventures, Bullhound, Triatomic, QIA, EDBI · **Website:** d-matrix.ai
- **Primary:** 02 · **Secondary:** 07 Memory, 04 Chiplets
- **One-Line:** Digital in-memory compute (DIMC) chiplet platform ("Corsair") for low-latency, cost-efficient datacenter inference.

#### Product / Technology
- Digital in-memory compute in SRAM + chiplet/3D packaging (next-gen "Raptor" with stacked DRAM [TO VERIFY]); targets generative/batch inference with high throughput-per-dollar. Company claims up to ~10x faster than GPU for certain inference (company claim). **Risks:** software stack maturity, scaling to largest models.

#### VC View
- **Attractiveness:** High · **Venture-scale:** High · **Use of funds:** ramp production/distribution (Series C). **Acquirers:** AMD, Marvell, Broadcom, hyperscalers. **Risks:** competition, software, sales cycle. **Data quality:** Medium-High. **Last updated:** 2026-11-04.

### Etched

- **Status:** Active · **HQ:** San Jose/Cupertino, US [TO VERIFY] · **Founded:** 2022
- **Founders:** Gavin Uberti, Chris Zhu, Robert Wachen
- **Stage:** Series C · **Total Funding:** ~$1.1B [ESTIMATED: ~$800M as of Jun 2026 per company + $300M Series C]
- **Rounds:** ~$120M Series A (2024; Primary, Positive Sum, Peter Thiel); **~$500M at ~$5B (Jan 2026), led by Stripes** [CONFIRMED as reported — DCD/SiliconANGLE]; **$300M Series C at $10.3B post-money (2026-07-23), led by Sequoia** with a16z, SK hynix, Jane Street, Diffusion Capital [TO VERIFY — secondary sources]; WSJ-reported talks at ~$20B and subsequent ~$21B reports [UNCONFIRMED].
- **Website:** etched.com · **Primary:** 02
- **One-Line:** "Sohu" — an ASIC with the transformer architecture hardwired into silicon, betting on transformer dominance for extreme throughput.

#### Product / Technology
- Transformer-specialized ASIC; on 2026-06-30 announced working Sohu silicon and **>$1B in signed customer contracts** (company claim) [UNCONFIRMED — no customer names or independent benchmarks]. First racks expected summer 2026; shipping status [TO VERIFY]. **Risk (central):** architecture drift (MoE, SSM hybrids, new attention variants).

#### VC View
- **Attractiveness:** High (high-variance, now richly priced) · **Venture-scale:** High · **Upside:** dominant transformer-serving ASIC. **Downside:** architecture obsolescence, single-product risk, valuation ahead of shipments. **Exit:** IPO/strategic. **Data quality:** Medium-Low (claims unverified). **Last updated:** 2026-11-04.

### FuriosaAI

- **Status:** Active · **HQ:** Seoul, KR · **Founded:** 2017 · **Founder/CEO:** June Paik (ex-Samsung/AMD)
- **Stage:** Series D (pre-IPO) · **Total Funding:** ~$1B [ESTIMATED]
- **Rounds:** Declined Meta acquisition offer (~$800M reported, 2025) [CONFIRMED as reported]; $125M Series C bridge at ~$735M (Jul 2025) [CONFIRMED as reported]; Bloomberg reported plans for a ~$500M pre-IPO round (Jan 2026); **$620M Series D at $2.9B post-money (announced 2026-10-28)** [CONFIRMED — Business Wire], with Korea's National Growth Fund reportedly contributing ~$280M [TO VERIFY]. KRW-denominated reports differ slightly (~₩820B round; ~₩3.8T post).
- **Product:** RNGD (Tensor Contraction Processor) — LG AI Research deployment; plans ~20,000 RNGD units in 2026 and >40,000 in 2027 (company plan) [TO VERIFY]; next-gen silicon in development.
- **VC view:** High; Korean sovereign-capital tailwind; IPO candidate. **Data quality:** Medium-High. **Last updated:** 2026-11-04.

### Positron AI

- **Status:** Active · **HQ:** Reno, NV / Bay Area, US [TO VERIFY] · **Founded:** 2023 · **CEO:** Mitesh Agrawal
- **Stage:** Series B · **Total Funding:** ~$300M+ [ESTIMATED] · **Last Round:** **$230M Series B at >$1B post-money (2026-02-04)**, co-led by ARENA Private Wealth, Jump Trading and Unless [CONFIRMED — Business Wire]
- **Product:** Shipping Atlas inference systems; next-gen **Asimov** memory-first ASIC (company claims ~2 TB memory per accelerator) targeting tape-out late 2026, production early 2027 [TO VERIFY]. **Risk:** Asimov pre-silicon. **VC view:** High. **Last updated:** 2026-11-04.

### Fractile (new)

- **Status:** Active · **HQ:** London, UK · **Founded:** 2022 · **Founder/CEO:** Walter Goodwin (Oxford robotics PhD)
- **Stage:** Series B · **Total Funding:** ~$240M [ESTIMATED: ~$17.5M seed + $220M Series B]
- **Rounds:** Seed ~$15–17.5M (Kindred, NATO Innovation Fund, Oxford Science Enterprises) [CONFIRMED]; **$220M Series B (2026-05-13)** led by Accel, Founders Fund and Factorial Funds, ~$1B valuation [CONFIRMED — Sifted/TNW/SiliconANGLE]; Aug 2026: Bloomberg-reported talks to raise ~$600M at **$6.5B pre-money**, following an initial agreement to sell **~$250M of chips to Anthropic** [UNCONFIRMED — talks; companies declined comment].
- **Product:** In-memory-compute inference chips/systems for very fast token generation; chips not shipping until 2027.
- **VC view:** High-variance; first European inference challenger with a frontier-lab anchor. **Last updated:** 2026-11-04.

### Taalas (new — archived on acquisition)

- **Status:** Acquired — AMD definitive agreement announced ~2026-08-06 (terms undisclosed; subject to regulatory approval) [CONFIRMED — AMD IR release]; closing [TO VERIFY]. · **HQ:** Toronto, CA · **Founded:** Aug 2023 · **Founder/CEO:** Ljubisa Bajic (Tenstorrent co-founder; ex-AMD/NVIDIA)
- **Funding:** ~$50M early + **$169M (Feb 2026)** from Quiet Capital, Fidelity, Pierre Lamond → ~$219M total [CONFIRMED — Reuters/SiliconANGLE].
- **Tech:** "Hardcore" model-specific silicon — model weights/architecture fixed in 2 of ~100 metal layers; HC1 runs Llama 3.1 8B; ~2-month turnaround per model (company claim). AMD reportedly plans to pair Taalas decode silicon with Instinct/Helios racks (GPU prefill, Taalas decode) [UNCONFIRMED].
- **Why it matters:** Validates "decode-specialized" silicon as an acquirable asset; second AMD inference-startup absorption after Untether AI's team. **Last updated:** 2026-11-04.

> Rebellions profile (lighter): **Rebellions (KR)** — merged with SK-backed Sapeon (Dec 2024); $250M Series C (Sep 2025, incl. Arm and Samsung) [TO VERIFY]; **$400M pre-IPO round (2026-03-30) led by Mirae Asset and Korea National Growth Fund at ~$2.3B** [CONFIRMED as reported]; total ~$850M; launched RebelRack/RebelPOD systems and US expansion; reportedly hired JPMorgan for a Korean IPO targeted late 2026–H1 2027 [TO VERIFY]. Untether AI archived (see [../deal_tracker/23_exit_and_shutdown_tracker.md](../deal_tracker/23_exit_and_shutdown_tracker.md)). MatX (LLM-specific, $500M Series B) also targets inference — see [01](01_training_accelerators.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Deterministic low-latency serving | High | High | High | Very High (NVIDIA owns Groq IP) | Exited (Groq precedent) | Medium |
| Digital/compute-in-memory inference | High | High | Medium-High | Medium | Real (d-Matrix, Fractile) | High |
| Transformer-hardwired ASIC | High | High | High | Medium | High-variance (Etched @ $10B+) | Medium-High (price risk) |
| Model-specific / hardwired-weights silicon | Medium-High | High | Medium | Medium | Validated by AMD–Taalas | Medium-High |
| Memory-capacity-first appliances | High | Medium-High | Medium | Medium | Real (Positron) | High |
| Sovereign/regional inference (KR) | High | Medium | High | Medium | Real (Rebellions/Furiosa → IPO) | Medium-High |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| Sequoia | VC | Etched | Growth | Led Etched $300M @ $10.3B (Jul 2026) [TO VERIFY] | Transformer ASIC conviction |
| Stripes | Growth | Etched | Growth | Led Etched ~$500M (Jan 2026) | Inference growth |
| Disruptive | Growth | Groq | Growth | Led Groq $750M (2025) and $650M (2026) | Inference cloud |
| Temasek | Sovereign | d-Matrix, Rebellions | B–Growth | Co-led d-Matrix C (Nov 2025) | Asia + efficiency |
| Bullhound / Triatomic | VC | d-Matrix | C | Co-led d-Matrix C | DIMC inference |
| Korea National Growth Fund | Sovereign | Rebellions, FuriosaAI | Pre-IPO | Co-led Rebellions $400M; ~$280M of Furiosa D | Korean sovereign AI silicon |
| Mirae Asset | Financial | Rebellions | Pre-IPO | Co-led Rebellions $400M | Korean IPO pipeline |
| Accel / Founders Fund / Factorial | VC | Fractile | B | Co-led Fractile $220M (May 2026) | European frontier inference |
| ARENA / Jump Trading / Unless | Crossover/trading | Positron | B | Co-led Positron $230M (Feb 2026) | Memory-bound inference |
| Jane Street | Trading firm | Etched, MatX | B–Growth | Participations 2026 | Compute-scarcity thesis |
| Quiet Capital / Fidelity | VC/Crossover | Taalas | A–B | Taalas $169M → AMD exit | Model-specific silicon |
| M12 (Microsoft) | Strategic | d-Matrix | A–B | d-Matrix | Hyperscaler inference signal |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Startup Formation Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------------------------|----------------|:------------:|------------|
| Song Han | MIT | Efficient inference, quantization | AWQ/SmoothQuant define serving efficiency; OmniML→NVIDIA | Likely Startup Signal | Deep Compression, AWQ | 5 | High |
| Tri Dao | Princeton/Together | FlashAttention, SSMs (Mamba) | Attention/SSM kernels shape inference silicon targets (and architecture-drift risk for Etched) | Likely (Together) | FlashAttention, Mamba | 5 | High |
| Jonathan Ross | NVIDIA (ex-Groq, ex-Google TPU) | Deterministic compute | Moved to NVIDIA with Groq license (Dec 2025) | Confirmed (Groq → NVIDIA) | TPU lineage | 5 | High |
| Ljubisa Bajic | Taalas → AMD | Model-specific silicon | Founded Tenstorrent and Taalas; second exit | Confirmed (Taalas, acquired) | Hardwired-weights approach | 5 | High |
| Walter Goodwin | Fractile | In-memory inference | UK frontier-inference challenger | Confirmed (Fractile) | — | 4 | Medium |
| Stanford/Berkeley systems | Stanford/UCB | Serving systems (vLLM lineage), disaggregated prefill/decode | Software that defines hardware needs | Watchlist | vLLM, PagedAttention, DistServe | 4 | Medium |

## 8. Diligence Questions

- **Technical:** Independent perf/$ & latency benchmarks (none public for Sohu)? Compiler/runtime maturity? Largest model that fits efficiently? Decode-only vs. full-stack?
- **Market:** Serviceable inference TAM and segment? Latency-sensitive vs. batch positioning? Fit with prefill/decode disaggregation?
- **Customer:** Committed frontier-lab/cloud offtake (OpenAI–Cerebras, Anthropic–Fractile style) vs. pilots? Concentration?
- **Competitive:** Survives NVIDIA (now with Groq LPU IP) price cuts + Dynamo/vLLM ubiquity? TPU external sales?
- **Financial:** Chips-per-model cost economics? Path to gross-margin-positive serving? Valuation vs. Cerebras public multiple?
- **Founder:** Silicon + compiler track record? Cloud GTM capability? Key-person risk to license-and-hire raids?
- **Exit:** Strategic logic for NVIDIA/AMD/Intel/hyperscaler? How does a license-and-hire structure treat preferred vs. common and employees? Korean IPO feasibility?

## 9. Refresh Notes

| Date | Refresh Type | Entries Added | Entries Updated | Entries Archived | Key Changes | Sources |
|------|--------------|---------------|-----------------|------------------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | 1 (Untether AI) | Initial build; full profiles Groq/d-Matrix/Etched; KR players; heatmap/investors/research | Company sites, trade press |
| 2026-11-04 | Full (Refresh #3) | 2 (Fractile, Taalas) | 7 (Groq, d-Matrix, Etched, SambaNova, Positron, Rebellions, FuriosaAI) | 2 (Groq → Licensed/Acqui-hired by NVIDIA; Taalas → Acquired by AMD) | NVIDIA–Groq ~$20B license + acqui-hire, residual GroqCloud ($3.5B per Bloomberg); d-Matrix $275M C @ $2B; Etched $500M + $300M @ $10.3B, >$1B orders claim; Positron $230M B; Rebellions $400M pre-IPO; FuriosaAI $620M D @ $2.9B; Fractile $220M B + Anthropic deal reports; AMD–Taalas; new profiles FuriosaAI/Positron/Fractile/Taalas; heatmap/investors rebuilt. Counts: 10 total, 7 active, 3 archived | Groq/NVIDIA statements, CNBC, Bloomberg, Business Wire (Positron, FuriosaAI), AMD IR, Reuters, SiliconANGLE, DCD, Sifted, TNW |
