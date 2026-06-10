---
category_id: "02"
category_name: "Inference Accelerators"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-06-09"
refresh_count: 1
total_companies: 8
active_companies: 7
archived_companies: 1
stealth_or_semi_stealth_companies: 0
total_disclosed_funding: "~$3B+ [ESTIMATED]"
top_investors: ["BlackRock", "Temasek", "Samsung", "Atreides", "M12"]
key_technical_inflections: ["Cost-per-token economics", "Deterministic low-latency serving", "Transformer-specialized ASICs", "Memory-centric inference", "Sovereign inference clouds"]
key_open_questions: ["Does CUDA lock-in hold for inference?", "Will transformer-hardwired ASICs survive architecture drift?", "Who wins reasoning/long-context serving?"]
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
- **Comparables:** NVIDIA, AMD. **Risks:** software ecosystem, NVIDIA price response, architecture drift.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Technical Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|---------------------------|----------|--------------|--------|
| Groq | US | 2016 | Late | ~$1B+ [TO VERIFY] | BlackRock, Samsung, Cisco | LPU + GroqCloud | API/cloud inference | Deterministic SRAM dataflow, ultra-low latency | Large GroqCloud usage; Saudi deal | High | Active |
| d-Matrix | US | 2019 | Series B | ~$160M+ [TO VERIFY] | Temasek, M12, Playground | Corsair (digital in-memory compute) | DC inference | Digital IMC (SRAM) + chiplets for low-latency batch | Sampling/early customers | High | Active |
| Etched | US | 2022 | Series A | ~$125M+ [TO VERIFY] | Primary, Positive Sum | Sohu — transformer-hardwired ASIC | Transformer serving | Hardwires transformer into silicon for max throughput | Pre-revenue; high hype | High | Active |
| SambaNova | US | 2017 | Series D | ~$1.1B [TO VERIFY] | SoftBank, BlackRock | SN40L systems | Enterprise/gov inference | Dataflow + 3-tier memory; agentic serving | Gov/enterprise | Medium-High | Active (see [01](01_training_accelerators.md)) |
| Positron AI | US | 2023 | Seed/A | ~$75M+ [TO VERIFY] | Valor, Atreides, DFJ Growth | Atlas inference appliance (FPGA→ASIC) | Memory-bound LLM inference | Memory-optimized, power-efficient transformer inference | Early shipments | Medium-High | Active |
| Rebellions | KR | 2020 | Series C/Unicorn | ~$325M+ [TO VERIFY] | KT, Temasek | ATOM/REBEL inference chips | Korea/Asia DC, sovereign | Energy-efficient inference; merged w/ Sapeon | Korean cloud/telco | Medium-High | Active |
| FuriosaAI | KR | 2017 | Series C | ~$200M+ [TO VERIFY] | DSC, Naver | RNGD (Tensor Contraction Processor) | DC inference, sovereign | TCP arch, high efficiency; reportedly declined Meta bid | LG/Korea; Meta interest [TO VERIFY] | Medium-High | Active |
| Untether AI | CA | 2018 | Wound down | ~$150M raised | Intel Cap, Tracker, CPPIB | At-memory compute (speedAI) | DC/edge inference | At-memory compute architecture | Assets/IP→AMD 2025 | Archived | Shut Down |

## 4. Company Profiles

### Groq

- **Status:** Active · **HQ:** Mountain View, US · **Founded:** 2016
- **Founders:** Jonathan Ross (ex-Google TPU), Douglas Wightman
- **Stage:** Late · **Total Funding:** ~$1B+ [TO VERIFY] · **Last Round:** ~$640M Series D, 2024, led by BlackRock; reports of a large 2025 round at multi-billion valuation [TO VERIFY]
- **Key/Strategic Investors:** BlackRock, Samsung Catalyst, Cisco Investments, Tiger Global, Sequoia [TO VERIFY] · **Employees:** ~300+ [ESTIMATED] · **Website:** groq.com
- **Primary:** 02 · **Secondary:** 16 DC Infra
- **One-Line:** Deterministic Language Processing Unit (LPU) and GroqCloud delivering industry-leading inference latency/throughput.

#### Product / Technology
- **Builds:** LPU inference chips + GroqCloud API + on-prem systems. **Architecture:** software-scheduled, deterministic dataflow with large on-chip SRAM, no external HBM — predictable ultra-low latency. **Claims:** leading tokens/sec/user at low latency. **Software:** Groq compiler maps models to deterministic schedule. **Deps:** mature node (no HBM dependence is a supply advantage). **Differentiation:** determinism + latency; **risk:** SRAM capacity limits model size per chip → many chips per large model (system cost).

#### Market / Traction / Competitive
- **Customers:** GroqCloud developers, Aramco Digital/Saudi sovereign inference build-out [TO VERIFY], enterprise. **GTM:** cloud API + sovereign data-center deals. **Competitors:** NVIDIA, SambaNova, Cerebras inference, Together/Fireworks (software). **Defensibility:** latency + compiler + cloud distribution.

#### VC Investment View
- **Attractiveness:** High · **Venture-scale:** High · **Why now:** inference cost/latency war + sovereign demand. **Upside:** category-defining inference cloud + IPO. **Downside:** chips-per-model cost economics, NVIDIA price cuts. **Exit:** IPO/strategic. **Acquirers:** few at this size. **Risks:** capital intensity of cloud build, model-size economics.
- **Data quality:** Medium. **Verify next:** latest round/valuation, GroqCloud revenue. **Last updated:** 2026-06-09.

### d-Matrix

- **Status:** Active · **HQ:** Santa Clara, US · **Founded:** 2019
- **Founders:** Sid Sheth, Sudeep Bhoja (ex-Inphi/Marvell/Broadcom)
- **Stage:** Series B · **Total Funding:** ~$160M+ [TO VERIFY] · **Last Round:** ~$110M Series B led by Temasek, 2023 [TO VERIFY]; reports of large Series C in 2025 [TO VERIFY]
- **Key Investors:** Temasek, M12 (Microsoft), Playground Global, Nautilus, Industry Ventures · **Website:** d-matrix.ai
- **Primary:** 02 · **Secondary:** 07 Memory, 04 Chiplets
- **One-Line:** Digital in-memory compute (DIMC) chiplet platform ("Corsair") for low-latency, cost-efficient datacenter inference.

#### Product / Technology
- Digital in-memory compute in SRAM + chiplet/3D packaging; targets generative/batch inference with high throughput-per-dollar and memory-bound efficiency. **Differentiation:** DIMC avoids analog-IMC accuracy issues while cutting memory movement energy. **Risks:** software stack maturity, scaling to largest models.

#### VC View
- **Attractiveness:** High · **Venture-scale:** High · **Acquirers:** AMD, Marvell, Broadcom, hyperscalers. **Risks:** competition, software, sales cycle. **Data quality:** Medium. **Last updated:** 2026-06-09.

### Etched

- **Status:** Active · **HQ:** Cupertino, US · **Founded:** 2022
- **Founders:** Gavin Uberti, Chris Zhu, Robert Wachen (Harvard dropouts)
- **Stage:** Series A · **Total Funding:** ~$125M+ [TO VERIFY] · **Last Round:** ~$120M Series A, 2024, co-led by Primary Venture Partners & Positive Sum; backers incl. Peter Thiel [TO VERIFY]
- **Website:** etched.com · **Primary:** 02
- **One-Line:** "Sohu" — an ASIC with the transformer architecture hardwired into silicon, betting on transformer dominance for extreme throughput.

#### Product / Technology
- Transformer-specialized ASIC (no general-purpose flexibility); claims order-of-magnitude throughput vs. GPUs for transformer inference. **Differentiation:** maximal specialization. **Risk (central):** architecture drift — if dominant models move away from vanilla transformers (e.g., new attention/SSM hybrids), the bet erodes. Pre-revenue; execution/tape-out risk.

#### VC View
- **Attractiveness:** High (high-variance) · **Venture-scale:** High · **Why now:** transformer ubiquity + inference cost. **Upside:** dominant transformer-serving ASIC. **Downside:** architecture obsolescence, single-product risk. **Exit:** strategic/IPO. **Acquirers:** hyperscalers, NVIDIA/AMD. **Data quality:** Medium-Low (pre-revenue). **Last updated:** 2026-06-09.

> Positron, Rebellions, FuriosaAI covered at table level + below as lighter entries; Untether AI archived (see [../deal_tracker/23_exit_and_shutdown_tracker.md](../deal_tracker/23_exit_and_shutdown_tracker.md)).

**Rebellions (KR)** — merged with SK-backed Sapeon; ATOM/REBEL inference chips; Korean unicorn; KT and Temasek backing; sovereign/regional inference. VC relevance Medium-High; acquirer set: Samsung/SK ecosystem. **FuriosaAI (KR)** — RNGD TCP inference chip; reportedly declined a Meta acquisition offer (~$800M) in 2025 [TO VERIFY]; strong efficiency claims; LG/Korean deployments. **Positron AI (US)** — memory-optimized transformer inference appliance, FPGA-now/ASIC-next; power-efficiency angle for memory-bound LLM serving.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Deterministic low-latency serving | High | High | High | High | Real (Groq) | High |
| Digital in-memory compute | High | High | Medium-High | Medium | Real (d-Matrix) | High |
| Transformer-hardwired ASIC | High | High | High | Medium | High-variance (Etched) | Medium-High |
| Sovereign/regional inference | High | Medium | High | Medium | Real (Rebellions/Furiosa) | Medium-High |
| Memory-optimized appliances | Medium-High | Medium | Medium | Medium | Real (Positron) | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage | Recent Activity | Thesis Signal |
|----------|------|--------------------|-------|-----------------|---------------|
| BlackRock | Crossover | Groq | Growth | Led Groq D | Inference cloud at scale |
| Temasek | Sovereign | d-Matrix, Rebellions | B–Growth | Led d-Matrix B | Asia + efficiency |
| Samsung Catalyst | Strategic | Groq | A–Growth | Groq backer | Memory/foundry adjacency |
| M12 (Microsoft) | Strategic | d-Matrix | A–B | d-Matrix | Hyperscaler inference signal |
| Atreides / Valor | VC/Crossover | Positron | A–Growth | Positron | Memory-bound inference |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Startup Formation Signal | Papers/Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------------------------|----------------|:------------:|------------|
| Song Han | MIT | Efficient inference, quantization | AWQ/SmoothQuant define serving efficiency; OmniML→NVIDIA | Likely Startup Signal | Deep Compression, AWQ | 5 | High |
| Tri Dao | Princeton/Together | FlashAttention, SSMs (Mamba) | Attention/SSM kernels shape inference silicon targets | Likely (Together) | FlashAttention, Mamba | 5 | High |
| Jonathan Ross | Groq (ex-Google) | Deterministic compute | Founder pedigree; TPU lineage | Confirmed (Groq) | TPU lineage | 5 | High |
| Stanford/Berkeley systems | Stanford/UCB | Serving systems (vLLM lineage) | Software that defines hardware needs | Watchlist | vLLM, PagedAttention | 4 | Medium |

## 8. Diligence Questions

- **Technical:** Independent perf/$ & latency benchmarks? Compiler/runtime maturity? Largest model that fits efficiently?
- **Market:** Serviceable inference TAM and segment? Latency-sensitive vs. batch positioning?
- **Customer:** Committed cloud/enterprise revenue vs. pilots? Concentration?
- **Competitive:** Survives NVIDIA inference price cuts + Dynamo/vLLM ubiquity?
- **Financial:** Chips-per-model cost economics? Path to gross-margin-positive serving?
- **Founder:** Silicon + compiler track record? Cloud GTM capability?
- **Exit:** Strategic logic for AMD/Qualcomm/hyperscaler acquisition? IPO scale?

## 9. Refresh Notes

| Date | Refresh Type | Entries Added | Entries Updated | Entries Archived | Key Changes | Sources |
|------|--------------|---------------|-----------------|------------------|-------------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | 1 (Untether AI) | Initial build; full profiles Groq/d-Matrix/Etched; KR players; heatmap/investors/research | Company sites, trade press |
