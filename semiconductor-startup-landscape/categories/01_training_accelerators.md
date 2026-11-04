---
category_id: "01"
category_name: "Training Accelerators"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-11-04"
refresh_count: 2
total_companies: 8
active_companies: 4
archived_companies: 4
stealth_or_semi_stealth_companies: 1
total_disclosed_funding: "~$8B+ private [ESTIMATED] (plus ~$5.5B Cerebras IPO proceeds, May 2026)"
top_investors: ["Tiger Global", "Fidelity", "Atreides", "Benchmark", "Trace Capital", "Jane Street", "SoftBank", "G42"]
key_technical_inflections: ["Wafer-scale integration", "Dataflow/RDU architectures", "HBM/memory bandwidth ceilings", "CUDA software moat", "Sovereign AI demand", "Training-to-inference shift of merchant challengers", "Hyperscaler ASIC external sales (TPU)"]
key_open_questions: ["Can any merchant trainer break CUDA lock-in?", "Does sovereign demand sustain non-NVIDIA training?", "Is wafer-scale economically durable at public-market scrutiny?", "Do merchant 'trainers' all become inference clouds?", "Will Google TPU external sales crowd out merchant challengers?"]
---

# 01 — Training Accelerators

> Chips and systems for training large AI models. The largest TAM and the hardest category for startups. See thesis context in [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md) and stack position in [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis

- **Why this matters now:** Frontier-model training drives the AI capex super-cycle; supply is structurally constrained by NVIDIA allocation, HBM, and CoWoS packaging. Nations, clouds and frontier labs actively want alternatives — OpenAI now buys compute from NVIDIA, AMD, Broadcom (custom), and Cerebras; Anthropic from Google TPU, AWS Trainium and NVIDIA.
- **What changed in 2025–2026:** The merchant "training challenger" cohort has largely **re-positioned toward inference** (Cerebras, SambaNova, Groq), and the category produced its first large venture exit: **Cerebras IPO on Nasdaq (May 14, 2026, ~$5.5B raised)** [CONFIRMED — multiple outlets; exact proceeds TO VERIFY vs. final prospectus]. Capital is again flowing to "next-gen" LLM-specific silicon (MatX $500M Series B, Feb 2026) and open RISC-V compute (Tenstorrent $1.5B Series E, Oct 2026).
- **Why venture-scale outcomes may/may not be possible:** Possible only with a genuinely differentiated *systems* story (wafer-scale, dataflow, memory bandwidth) **and** a captive demand anchor (OpenAI→Cerebras is the template). Otherwise NVIDIA + hyperscaler in-house silicon (TPU, Trainium) dominate.
- **Key technical inflections:** Wafer-scale integration; reconfigurable dataflow; memory-bandwidth ceilings (HBM4); optical scale-up; the CUDA/software moat; frontier labs' multi-vendor compute strategies.
- **Key market pull:** Sovereign AI, NVIDIA supply scarcity, cost of frontier training, geopolitical diversification, frontier-lab demand for fast inference capacity.
- **Likely acquirers:** AMD, Intel, SoftBank, hyperscalers; NVIDIA via **license + acqui-hire** structures (Groq precedent, Dec 2025). Intel's attempt to buy SambaNova (~$1.6B reported) stalled in Jan 2026 [CONFIRMED per Bloomberg].
- **Exit pathways:** IPO (Cerebras done), strategic M&A, licensing-style "non-acquisition" deals, pivot to cloud/inference services.
- **Why incumbents may dominate or fail:** NVIDIA's software + supply + systems integration is the deepest moat in compute; incumbents "fail" only if a workload/architecture shift (e.g., extreme memory-bandwidth needs, fast-token inference) outruns the GPU roadmap.
- **What type of startup could win:** Wafer-scale/memory-centric systems with sovereign or frontier-lab demand; or a trainer that becomes a vertically integrated AI cloud.
- **What would make it non-investable:** "Better GPU" with no software ecosystem, no supply access, and no anchor customer.

## 2. Market Context

- **Market structure:** Oligopoly (NVIDIA dominant) + hyperscaler in-house (Google TPU, AWS Trainium, Meta MTIA, Microsoft Maia) + a thin merchant-challenger layer that is increasingly inference-focused.
- **Hyperscaler context (for comparison only):**
  - **Google TPU v7 "Ironwood"** — GA late 2025; Anthropic committed to up to 1M TPUs / >1 GW capacity in 2026 (Oct 2025) [CONFIRMED — Google/Anthropic announcement]; reports of Meta negotiating TPU use/purchases (Nov 2025) [UNCONFIRMED]. TPU external sales are the most direct threat to merchant challengers.
  - **AWS Trainium3** (3nm) launched at re:Invent Dec 2025; Trainium2 underpins Anthropic's Project Rainier [CONFIRMED — AWS].
  - **Microsoft Maia 200** — next-gen in-house accelerator announced early 2026 [TO VERIFY timing/specs].
  - **Meta MTIA** — in-house inference/training roadmap; Meta also acquired RISC-V startup Rivos (2025) [TO VERIFY — see [04](04_custom_asic_and_chiplets.md)].
  - **OpenAI** — 10 GW custom accelerator program with Broadcom (announced Oct 2025, deployments targeted from H2 2026) [CONFIRMED announcement; deployment status TO VERIFY]; 6 GW AMD MI450 deal (Oct 2025) [CONFIRMED]; >$10B / 750 MW Cerebras deal (Jan 2026) [CONFIRMED deal; value per Bloomberg sources].
- **Customer segments:** Frontier model labs, hyperscalers, sovereign AI programs, national labs, large enterprises.
- **Adoption drivers:** Cost/availability of NVIDIA, sovereignty, perf/W, total cost of training, frontier labs' supplier diversification.
- **Technical bottlenecks:** Memory bandwidth/capacity (HBM3E→HBM4), interconnect (scale-up), packaging supply (CoWoS), software maturity.
- **Supply-chain dependencies:** TSMC leading-edge, HBM (SK hynix/Samsung/Micron), CoWoS/advanced packaging.
- **Competitive landscape:** NVIDIA (Blackwell/Rubin), AMD (MI350/MI450), Google TPU, AWS Trainium, Intel (Gaudi wind-down; partnership with SambaNova), plus challengers below.
- **Funding environment (2026):** Very strong for credible systems + demand: Cerebras Series G $1.1B @ $8.1B (Sep 2025) → Series H $1B @ ~$23B (Feb 2026) → IPO @ ~$56B fully diluted (May 2026); Tenstorrent $1.5B @ $6.2B (Oct 2026); MatX $500M (Feb 2026). Brutal for sub-scale (Esperanto).
- **Recent M&A / exits:** Graphcore → SoftBank (2024); NVIDIA–Groq license + acqui-hire (~$20B reported, Dec 2025); Intel–SambaNova talks ended → partnership + minority stake (Feb 2026); Cerebras IPO (May 2026). See [../deal_tracker/20_ma_tracker.md](../deal_tracker/20_ma_tracker.md).
- **Public comparables:** NVIDIA, AMD; **Cerebras (Nasdaq: CBRS)** now a direct public comp.
- **Adjacent new entrant:** Unconventional AI (Naveen Rao; $475M seed @ $4.5B, Dec 2025, a16z/Lightspeed) [CONFIRMED — TechCrunch/Bloomberg] — brain-inspired/analog AI computers; tracked in [14](14_quantum_neuromorphic_and_non_von_neumann.md).
- **Key risks:** CUDA lock-in, capital intensity, demand concentration (G42 → OpenAI), HBM allocation, TPU/Trainium external sales.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Technical Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|---------------------------|----------|--------------|--------|
| Cerebras | US | 2015 | Public (Nasdaq: CBRS, May 2026) | ~$2.8B private [ESTIMATED] + ~$5.5B IPO [CONFIRMED] | Benchmark, Fidelity, Atreides, Tiger Global | Wafer-Scale Engine (WSE-3) systems & inference cloud | Labs, sovereign, HPC, inference API | Wafer-scale single-die; huge on-chip SRAM/bandwidth | OpenAI >$10B/750 MW deal; G42; cloud rev +281% YoY Q2'26 [TO VERIFY] | High (public comp) | Public (exited via IPO 2026-05-14) |
| SambaNova | US | 2017 | Series D+ (strategic) | ~$1.1B+ [TO VERIFY] | SoftBank, BlackRock, Intel Capital | Reconfigurable Dataflow (RDU) systems; SambaCloud | Enterprise, gov, sovereign inference | Dataflow arch + 3-tier memory; agentic serving | Intel multiyear inference partnership + stake to 8.2% (Feb 2026) | Medium | Active |
| Tenstorrent | CA/US | 2016 | Series E | ~$2.5B+ [ESTIMATED] | Trace Capital, Innovation X, Samsung, AFW, Fidelity | RISC-V + Tensix AI chips/IP | Training+inference, IP licensing | Open RISC-V + scalable Ethernet mesh; IP model | $1.5B Series E @ $6.2B (Oct 2026) | High | Active |
| MatX | US | 2022 | Series B | ~$600M+ [ESTIMATED] | Jane Street, Situational Awareness, Spark | LLM-optimized training/inference chip | Frontier LLM labs | Ex-Google TPU team; LLM-specific arch; claims ~10x vs GPU | $500M Series B (Feb 2026); hardware 2026–27 [TO VERIFY] | High | Active |
| Groq | US | 2016 | Licensed/acqui-hired | ~$3B [ESTIMATED] | BlackRock, Disruptive, Samsung | LPU (deterministic) — inference | Inference (see [02](02_inference_accelerators.md)) | Deterministic SRAM dataflow | NVIDIA non-exclusive license + leadership hire (Dec 2025); residual GroqCloud independent | High | Licensed/Acqui-hired (see 02) |
| Esperanto Tech | US | 2014 | Restructured | ~$160M+ [TO VERIFY] | — | RISC-V many-core (ET-SoC) | Pivoted away from broad AI | 1000+ RISC-V cores | Reports of 2025 wind-down/asset sale [UNCONFIRMED] | Low | Semi-Stealth (status TO VERIFY) |
| Graphcore | UK | 2016 | Acquired | ~$700M raised | Sequoia, BMW i | IPU dataflow | (now SoftBank) | MIMD graph processor | Acquired by SoftBank 2024; role in SoftBank "Izanagi" chip effort [UNCONFIRMED] | Archived | Acquired |
| Habana Labs | IL | 2016 | Acquired | ~$120M raised | Intel Capital, Bessemer | Gaudi training/inference | (now Intel) | Training + inference ASICs | Intel Gaudi line | Archived | Acquired (Intel) |

## 4. Company Profiles

### Cerebras Systems

- **Status:** Public — Nasdaq: CBRS, IPO priced 2026-05-14 [CONFIRMED]. Exited from venture perspective; kept here as the category's public comparable.
- **Headquarters:** Sunnyvale, US
- **Founded:** 2015
- **Founders:** Andrew Feldman, Gary Lauterbach, Sean Lie, Michael James, Jean-Philippe Fricker (SeaMicro alumni)
- **Stage:** Public
- **Total Funding:** ~$2.8B private [ESTIMATED: ~$720M through 2021 + $1.1B Series G + $1B Series H] + ~$5.5B IPO proceeds [CONFIRMED — multiple outlets; exact figure TO VERIFY vs. final prospectus]
- **Funding history (2025–2026):**
  - **Oct 2025:** Withdrew original 2024 S-1 after raising **$1.1B Series G at $8.1B** (led by Fidelity and Atreides, Sep 30 2025) [CONFIRMED].
  - **Feb 4, 2026:** **$1B Series H at ~$23B post-money**, led by Tiger Global; participants incl. Benchmark, Fidelity, Atreides, Alpha Wave, Altimeter, AMD, Coatue, 1789 Capital [CONFIRMED — company release].
  - **May 14, 2026:** IPO priced at **$185/share** (above $150–160 range; upsized from ~$4.8B target), raising **~$5.5B**; ~$56B fully diluted valuation at IPO price; shares reportedly rose ~108% on debut [CONFIRMED pricing; first-day move per press].
- **Key Investors:** Benchmark, Foundation Capital, Eclipse, Coatue, Altimeter, Fidelity, Atreides, Tiger Global, G42 · **Strategic:** G42 (historic anchor), AMD (Series H participant) [CONFIRMED per release]
- **Employees:** ~600+ [ESTIMATED]
- **Website:** cerebras.ai
- **Primary Category:** 01 Training · **Secondary:** 02 Inference, 16 DC Infra
- **One-Line Description:** Wafer-scale AI systems and inference cloud; the largest single-chip processor, now primarily monetized as ultra-fast inference capacity.

#### Product / Technology
- **Builds:** Wafer-Scale Engine (WSE-3) and CS-3 systems; Cerebras Cloud / inference API; datacenters built or leased to host OpenAI capacity.
- **Core architecture:** Entire wafer as one chip — ~900k cores, massive on-wafer SRAM and bandwidth, weight-streaming for large models.
- **Key claims:** Record inference token throughput; eliminates multi-GPU partitioning.
- **Software stack:** Cerebras SDK / PyTorch integration; weight-streaming execution.
- **Supply-chain deps:** TSMC wafer-scale process, custom packaging/cooling, datacenter power.
- **Maturity:** Production; multiple datacenters. **Risks:** Yield/cost, customer concentration (G42 → OpenAI), CUDA ecosystem gap, capex for owned/leased capacity.

#### Market and Customer Traction
- **OpenAI:** Multi-year deal, **>$10B for 750 MW** of Cerebras compute delivered in tranches through 2028 (announced 2026-01-14) [CONFIRMED deal; value per Bloomberg sources]. OpenAI pays to use Cerebras-hosted inference capacity.
- **Financials (post-IPO, secondary-source reporting) [TO VERIFY vs. SEC 8-K/10-Q]:** Q1 2026 revenue ~$193.4M (+94% YoY); Q2 2026 revenue ~$180.1M (below consensus), cloud revenue ~$126M (+281% YoY); Q3 2026 core revenue guidance ~$214–216M; company guided to core gross-margin trough in Q3 and expects 2027 core revenue to more than triple [UNCONFIRMED].
- **Other customers/partners:** G42 (Condor Galaxy), national labs, Mayo Clinic, GSK, Meta Llama API partnership [TO VERIFY current].
- **GTM:** Systems sales + cloud + inference API + frontier-lab capacity contracts.

#### Competitive Landscape
- **Direct/incumbent:** NVIDIA, AMD, Google TPU, Groq-inside-NVIDIA (post-license). **Substitutes:** GPU clusters. **Defensibility:** Wafer-scale IP, systems integration; **risk:** ecosystem breadth, demand concentration.

#### VC Investment View
- **Attractiveness:** Exited (public) — now a valuation benchmark for private challengers (Etched, Tenstorrent, MatX). **Why it matters:** Proves IPO path exists for AI-silicon challengers when anchored by a frontier-lab contract.
- **Upside:** Inference-cloud scale; OpenAI tranches through 2028. **Downside:** Revenue lumpiness (Q2 miss), concentration, margin pressure from capacity build.
- **Diligence Qs (as comp):** Revenue mix OpenAI vs. G42 vs. others? Gross margin of cloud vs. systems? Capex funding of 750 MW build?

#### Data Quality
- **Source confidence:** High for funding/IPO events; Medium for quarterly figures (secondary sources; SEC 8-K not directly fetched). **Verify next:** Q3 2026 results, OpenAI tranche delivery, lock-up expiry. **Last updated:** 2026-11-04. **Sources:** Cerebras investor releases, Bloomberg, TechCrunch, DCD, Benzinga.

### SambaNova Systems

- **Status:** Active (independent) · **HQ:** Palo Alto, US · **Founded:** 2017
- **Founders:** Rodrigo Liang, Kunle Olukotun (Stanford), Christopher Ré (Stanford)
- **Stage:** Series D+ (with strategic investment) · **Total Funding:** ~$1.1B+ [TO VERIFY] · **Last priced round:** Series D ~$676M, 2021, led by SoftBank Vision Fund 2 (~$5B valuation) [TO VERIFY]
- **2025–2026 events:**
  - Late 2025: Intel in advanced talks to acquire SambaNova for ~$1.6B incl. debt [CONFIRMED as reported talks — Bloomberg/heise], far below its 2021 valuation.
  - Jan 2026: Talks **stalled**; SambaNova sought $300–500M from tech/semiconductor investors [CONFIRMED per Bloomberg].
  - Feb 2026: Intel chose a **multiyear AI inference partnership** instead of acquisition and invested ~$35M, lifting its stake to **8.2%** (from 6.8%) [CONFIRMED per Reuters via PYMNTS / CRN].
  - May 2026: Reports of an HSR antitrust review closing without enforcement action relating to Intel's stake [UNCONFIRMED — framing conflicts across sources].
  - Outcome of the $300–500M raise: [TO VERIFY].
- **Key Investors:** SoftBank, BlackRock, Temasek, GV, Intel Capital · **Employees:** ~400–500 [ESTIMATED; layoffs reported 2025 TO VERIFY] · **Website:** sambanova.ai
- **Primary:** 01 Training · **Secondary:** 02 Inference
- **One-Line:** Reconfigurable Dataflow (RDU) systems and SambaCloud inference platform; now an inference-first company with Intel as strategic partner.

#### Product / Technology
- Reconfigurable Dataflow Unit (RDU), large-memory architecture (SN40L), SambaStack software, SambaCloud inference API. Differentiation: dataflow + 3-tier memory for large models; pivoted toward enterprise/gov/sovereign inference + agentic serving. Risks: CUDA gap, GTM concentration, flat-to-down valuation.

#### Market / Competitive / VC View
- **Customers:** US national labs, governments, enterprise, sovereign inference projects [TO VERIFY current]; Intel partnership. **Competitors:** NVIDIA, Cerebras, Groq-in-NVIDIA. **Attractiveness:** Medium (down-round/strategic-sale dynamics) · **Venture-scale:** Medium · **Exit:** Strategic (Intel remains logical acquirer) or recap · **Risks:** valuation reset, demand concentration, software ecosystem.
- **Data quality:** Medium. **Verify next:** 2026 financing outcome, Intel deal scope. **Last updated:** 2026-11-04.

### Tenstorrent

- **Status:** Active · **HQ:** Toronto, CA (major US operations in Santa Clara; several 2026 reports describe it as Santa Clara-based) · **Founded:** 2016
- **Founders:** Ljubisa Bajic (left; founded Taalas — see [02](02_inference_accelerators.md)), Milos Trajkovic, Ivan Hamer; led by **Jim Keller** (CEO)
- **Stage:** Series E · **Total Funding:** ~$2.5B+ [ESTIMATED]
- **Rounds:** Series D ~$693M (Dec 2024; ~$2.6B post per Bloomberg) led by Samsung Securities & AFW Partners [CONFIRMED]; **Series E $1.5B at $6.2B post-money (announced 2026-10-19)**, led by **Trace Capital and Innovation X**, with ARK Invest, Sandisk, Morgan Stanley, T. Rowe Price and Tether Investments participating [CONFIRMED — per Reuters / DCD]. A Form D (Aug 2026) showing ~$1.29B raised may relate to the same round [TO VERIFY].
- **Key/Strategic Investors:** Samsung, Hyundai, LG, Fidelity, Bezos Expeditions, Sandisk, Tether · **Website:** tenstorrent.com
- **Primary:** 01/02 · **Secondary:** 04 Custom ASIC/RISC-V IP
- **One-Line:** Open, RISC-V-based AI compute (Tensix) and licensable IP — the best-funded "open-ecosystem" challenger to CUDA.

#### Product / Technology
- Tensix AI cores + RISC-V CPU IP (Ascalon); scalable Ethernet-connected mesh (Wormhole/Blackhole chips, Galaxy systems); open software (tt-Metalium/TT-Forge). **Differentiation:** open ISA + IP licensing model alongside chips; standard Ethernet scale-out; chiplet roadmap. **Risks:** software maturity vs. CUDA; dual chip+IP focus.

#### Market / Competitive / VC View
- **Customers/partners:** IP deals (LG, Hyundai, Japan's LSTC/Rapidus-linked programs), dev cloud, sovereign interest [TO VERIFY current list]. **Competitors:** NVIDIA, AMD, Arm (IP), SiFive (RISC-V). **Attractiveness:** High (late-stage) · **Venture-scale:** High · **Exit:** IPO most likely · **Acquirers:** Samsung, hyperscalers. **Risks:** software ecosystem, focus, valuation step-up (2.4x in <2 years).
- **Data quality:** Medium-High. **Last updated:** 2026-11-04.

### MatX

- **Status:** Active · **HQ:** Mountain View/San Francisco Bay Area, US [TO VERIFY] · **Founded:** 2022
- **Founders:** Reiner Pope (CEO), Mike Gunter (ex-Google TPU/PaLM)
- **Stage:** Series B · **Total Funding:** ~$600M+ [ESTIMATED] · **Last Round:** **$500M Series B (announced ~2026-02-24)** led by **Jane Street** and Leopold Aschenbrenner's **Situational Awareness** fund [CONFIRMED — multiple outlets incl. The Register]; prior ~$100M Series A led by Spark Capital (2024) [TO VERIFY]. Valuation undisclosed [TO VERIFY].
- **One-Line:** LLM-specific accelerator from ex-Google TPU architects, claiming ~10x efficiency vs. GPUs for large-model training and inference (company claim).
- **Product:** MatX One chip; first hardware shipping targeted 2026–2027 [TO VERIFY]. **Risks:** pre-silicon/early silicon; must win a frontier-lab anchor.
- **VC view:** High (high-variance); one of the few 2026 mega-rounds for a pre-revenue trainer. **Data quality:** Medium-Low. **Last updated:** 2026-11-04.

> Lighter-coverage entries (Esperanto) and archived entries (Graphcore, Habana) are summarized in the table above. Graphcore: reports of further SoftBank capital (~$450M, 2026) and of Graphcore IPU tech feeding SoftBank's "Izanagi" chip program are [UNCONFIRMED]. Groq is profiled in [02](02_inference_accelerators.md).

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Wafer-scale systems | High | Very High | Very High | High | Proven (Cerebras IPO) — no room for a second | Medium (public comp only) |
| Dataflow/RDU | Medium | High | High | High | Narrow (SambaNova valuation reset) | Low-Medium |
| RISC-V open AI compute/IP | Medium-High | High | Medium-High | Medium | Real (IP leverage; Tenstorrent $6.2B) | Medium-High |
| LLM-specific trainers (MatX-style) | High | High | Very High | Very High | High-variance, needs frontier-lab anchor | Medium-High |
| Sovereign-AI trainers | High | High | Very High | Medium | Real (anchor demand) | Medium-High |
| Trainer → inference-cloud pivots | High | Medium | Very High | High | Real but capex-heavy | Medium |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage Preference | Recent Activity | Thesis Signal |
|----------|------|--------------------|------------------|-----------------|---------------|
| Tiger Global | Crossover | Cerebras | Pre-IPO | Led Cerebras Series H ($1B @ ~$23B, Feb 2026) | Pre-IPO AI compute |
| Fidelity / Atreides | Crossover | Cerebras, Tenstorrent | Growth/Pre-IPO | Led Cerebras Series G ($1.1B, Sep 2025) | Public-market bridge |
| Trace Capital / Innovation X | Growth | Tenstorrent | Late | Co-led Tenstorrent Series E ($1.5B, Oct 2026) | Open-ecosystem compute |
| Jane Street / Situational Awareness | Trading firm / AI-thesis fund | MatX (also Etched) | B–Growth | Led MatX $500M Series B (Feb 2026) | "Frontier-lab compute scarcity" |
| SoftBank | Strategic/Growth | SambaNova, Graphcore (acq), Ampere (acq), Arm | Growth | Graphcore + Ampere consolidation | "Own the AI compute stack" |
| G42 | Strategic/Sovereign | Cerebras | Growth | Cerebras anchor | Sovereign AI demand |
| Samsung Catalyst | Strategic | Tenstorrent | A–Growth | Led Tenstorrent D | Memory/foundry adjacency |
| Benchmark | VC | Cerebras | Early | Held through IPO | Wafer-scale conviction |
| Intel Capital | Strategic | SambaNova | Growth | Raised stake to 8.2% (Feb 2026) | Partnership instead of M&A |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Startup Formation Signal | Relevant Papers / Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------------------------|---------------------------|:------------:|------------|
| Kunle Olukotun | Stanford | Dataflow, RDA | SambaNova founder; dataflow lineage | Confirmed Startup (SambaNova) | Plasticine/RDA papers | 5 | High |
| Bill Dally | Stanford/NVIDIA | Accelerator arch, interconnect | Defines the GPU roadmap; talent source | Watchlist (incumbent) | ISCA/MICRO body | 5 | High |
| Berkeley ADEPT/SLICE | UC Berkeley | RISC-V, agile HW, accelerators | RISC-V training-chip talent pipeline | Likely Startup Signal | RISC-V, Gemmini | 4 | Medium |
| Reiner Pope / Mike Gunter (ex-Google TPU) | MatX | LLM-specific silicon | Raised $500M Series B (2026) | Confirmed Startup (MatX) | TPU / PaLM efficiency lineage | 5 | High |
| Naveen Rao | Unconventional AI (ex-Databricks/MosaicML, Nervana) | Brain-inspired/analog AI compute | $475M seed @ $4.5B (Dec 2025) | Confirmed Startup (see [14](14_quantum_neuromorphic_and_non_von_neumann.md)) | — | 4 | High |

See [../researchers/leading_researchers_index.md](../researchers/leading_researchers_index.md).

## 8. Diligence Questions

- **Technical:** Memory-bandwidth advantage vs. HBM4-GPU (Rubin)? Software/compiler maturity vs. CUDA? Tape-out node, yield, packaging supply?
- **Market:** Is demand anchored (sovereign/frontier lab/hyperscaler) or speculative? Does the "trainer" actually earn most revenue from inference?
- **Customer:** Committed multi-year capacity contracts (Cerebras–OpenAI template) vs. pilots? Concentration risk?
- **Competitive:** Survives NVIDIA Rubin + supply expansion? Google TPU external sales? AMD MI450?
- **Financial:** Capital to next milestone? Gross margin at scale? Who funds datacenter capex for capacity contracts? Valuation vs. Cerebras public multiple?
- **Founder:** Shipped silicon before? Can recruit scarce architects/compiler talent (NVIDIA acqui-hire risk)?
- **Exit:** IPO-viable revenue scale? Exposure to license-and-hire structures that leave common/early holders with residual entities?

## 9. Refresh Notes

| Date | Refresh Type | Entries Added | Entries Updated | Entries Archived | Key Changes | Sources |
|------|--------------|---------------|-----------------|------------------|-------------|---------|
| 2026-06-09 | Full (initial) | 9 | 0 | 2 (Graphcore, Habana) | Initial build; thesis, market context, profiles for Cerebras/SambaNova/Tenstorrent; heatmap, investors, research signals | Company sites, S-1, trade press |
| 2026-11-04 | Full (Refresh #3) | 0 (MatX promoted to full profile) | 7 (Cerebras, SambaNova, Tenstorrent, MatX, Groq, Esperanto, Graphcore) | 2 (Cerebras → Public/IPO; Groq → Licensed/Acqui-hired, cross-ref) | Cerebras Series G/H, OpenAI >$10B deal, Nasdaq IPO (May 2026); Intel–SambaNova talks failed → partnership + 8.2% stake; Tenstorrent $1.5B Series E @ $6.2B; MatX $500M Series B; NVIDIA–Groq license; hyperscaler context (Ironwood, Trainium3, Maia 200, OpenAI–Broadcom); counts recomputed (total 8: 4 active, 4 exited/archived) | Cerebras IR release, Bloomberg, TechCrunch, DCD, Reuters (via PYMNTS/DCD), CRN, The Register, Benzinga |
