---
category_id: "01"
category_name: "Training Accelerators"
primary_datacenter_relevance: "High"
vc_relevance: "High"
last_refreshed: "2026-08-13"
refresh_count: 2
total_companies: 8
active_companies: 6
archived_companies: 2
stealth_or_semi_stealth_companies: 1
total_disclosed_funding: "~$9B+ private, plus a ~$5.5B IPO [ESTIMATED]"
top_investors: ["Jane Street", "General Atlantic", "Fidelity", "Samsung Catalyst", "Situational Awareness LP", "SoftBank", "G42"]
key_technical_inflections: ["Wafer-scale integration", "Dataflow/RDU architectures", "HBM/memory bandwidth ceilings", "CUDA software moat", "Sovereign AI demand", "Merchant custom ASIC (OpenAI/Broadcom) as substitute"]
key_open_questions: ["Can any merchant trainer break CUDA lock-in?", "Does sovereign demand sustain non-NVIDIA training?", "Is wafer-scale economically durable?", "Post-Cerebras-IPO: does the public market fund the next trainer, or did the window take only one?", "Does a lab-designed Broadcom ASIC foreclose the merchant training-chip market?"]
---

# 01 — Training Accelerators

> Chips and systems for training large AI models. The largest TAM and the hardest category for startups. See thesis context in [../INVESTMENT_THESES.md](../INVESTMENT_THESES.md) and stack position in [../MARKET_MAP.md](../MARKET_MAP.md).

## 1. VC Investment Thesis

- **Why this matters now:** Frontier-model training drives the AI capex super-cycle; supply is structurally constrained by NVIDIA allocation, HBM, and CoWoS packaging. Nations and clouds actively want alternatives.
- **Why venture-scale outcomes may/may not be possible:** Possible only with a genuinely differentiated *systems* story (wafer-scale, dataflow, memory bandwidth) **and** a captive demand anchor. Otherwise NVIDIA + hyperscaler in-house silicon (TPU, Trainium) dominate.
- **Key technical inflections:** Wafer-scale integration; reconfigurable dataflow; memory-bandwidth ceilings; optical scale-up; the CUDA/software moat.
- **Key market pull:** Sovereign AI, NVIDIA supply scarcity, cost of frontier training, geopolitical diversification.
- **Likely acquirers:** AMD, Intel, SoftBank, hyperscalers; or IPO for the few at scale.
- **Exit pathways:** IPO (Cerebras path), strategic M&A, pivot to cloud/inference services.
- **Why incumbents may dominate or fail:** NVIDIA's software + supply + systems integration is the deepest moat in compute; incumbents "fail" only if a workload/architecture shift (e.g., extreme memory-bandwidth needs) outruns the GPU roadmap.
- **What type of startup could win:** Wafer-scale/memory-centric systems with sovereign or hyperscaler demand; or a trainer that becomes a vertically integrated AI cloud.
- **What would make it non-investable:** "Better GPU" with no software ecosystem, no supply access, and no anchor customer.

## 2. Market Context

- **Market structure:** Oligopoly (NVIDIA dominant) + hyperscaler in-house (Google TPU, AWS Trainium, Meta MTIA, Microsoft Maia) + a thin merchant-challenger layer.
- **Customer segments:** Frontier model labs, hyperscalers, sovereign AI programs, national labs, large enterprises.
- **Adoption drivers:** Cost/availability of NVIDIA, sovereignty, perf/W, total cost of training.
- **Technical bottlenecks:** Memory bandwidth/capacity (HBM), interconnect (scale-up), packaging supply (CoWoS), software maturity.
- **Supply-chain dependencies:** TSMC leading-edge, HBM (SK hynix/Samsung/Micron), CoWoS/advanced packaging.
- **Competitive landscape:** NVIDIA (H/B/Rubin), AMD (MI300/MI400), Google TPU, AWS Trainium, Intel Gaudi, plus challengers below.
- **Funding environment:** Mega-rounds available for credible systems + demand (Cerebras, SambaNova historically); brutal for sub-scale.
- **Recent M&A:** Graphcore → SoftBank (2024); see [../deal_tracker/20_ma_tracker.md](../deal_tracker/20_ma_tracker.md).
- **Public comparables:** NVIDIA, AMD; **Cerebras (NASDAQ: CBRS since 2026-05-14)**.
- **Key risks:** CUDA lock-in, capital intensity, demand concentration, HBM allocation.

### 2026 Update — what changed since the last refresh (2026-08-13)

- **Cerebras went public and the category got a live comparable.** IPO priced 2026-05-14 at $185/share, raising ~$5.5B at a ~$56B implied valuation — the largest semiconductor IPO on record; the stock opened around $350 and closed the first day at ~$311 (+68%). Q1 2026 revenue was $193.4M (core $191.3M, +92% YoY) against 2026 core revenue guidance of ~$855–865M [TO VERIFY]. The enabler was a January 2026 multi-year OpenAI agreement for up to **750MW** of wafer-scale inference systems, reported at **>$20B** and phasing through 2028.
- **The anchor-customer thesis was confirmed, not refuted.** Cerebras did not diversify away from concentration; it traded a sovereign anchor (G42) for a frontier-lab anchor (OpenAI) roughly 23x the size of its annual core revenue guidance. Underwrite the anchor, and underwrite what happens if it renegotiates.
- **SambaNova recapitalized rather than sold.** ~$1B Series F first close at ~$11B post in July 2026, led by General Atlantic with Seligman Ventures, T. Rowe Price and Capital Group; JPMorganChase named it an inference infrastructure partner [TO VERIFY]. Note the direction of travel: the "training" company is now sold as enterprise/agentic *inference* infrastructure.
- **MatX left the "lighter coverage" tier.** ~$500M Series B (2026-02-24) co-led by Jane Street and Situational Awareness LP, with Spark, Triatomic and Harpoon, strategic participation from **Alchip and Marvell**, and angels including Andrej Karpathy and the Collison brothers. MatX One targets TSMC production with first shipments in 2027 and a claimed ~10x efficiency advantage for LLM training [TO VERIFY — vendor claim, unbenchmarked].
- **Tenstorrent raised big and is being circled.** ~$800M at a ~$3.2B valuation led by Fidelity (2025-11), total ~$1.18B; 2026 reporting describes early-stage takeover conversations with Intel and Qualcomm [UNCONFIRMED].
- **The new competitive fact: labs can now build their own.** OpenAI and Broadcom unveiled **"Jalapeño"** (2026-06-24), an LLM-optimized inference accelerator taken from design to tape-out in ~9 months with a claimed ~50% cost advantage over merchant GPUs, inside a 10GW program deploying from 2026 H2 through 2029. Every merchant training/inference startup now has to answer why its customer would not simply commission a Broadcom or Marvell ASIC.
- **Category verdict unchanged but sharper:** training silicon remains the hardest category, and the two winners in it (Cerebras, and arguably Tenstorrent's IP model) won on *demand contracts and business-model design*, not on architecture.

## 3. Startup Landscape Table

| Company | HQ | Founded | Stage | Total Funding | Lead Investors | Core Product | Target Market | Technical Differentiation | Traction | VC Relevance | Status |
|---------|----|---------|-------|---------------|----------------|--------------|---------------|---------------------------|----------|--------------|--------|
| Cerebras | US | 2015 | **Public (NASDAQ: CBRS, 2026-05)** | ~$720M+ private + ~$5.5B IPO [TO VERIFY] | Benchmark, Foundation, G42 | Wafer-Scale Engine (WSE-3) systems & cloud | Labs, sovereign, HPC | Wafer-scale single-die; huge on-chip SRAM/bandwidth | OpenAI 750MW / >$20B deal; Q1'26 rev $193M (+92%) | High | Active |
| SambaNova | US | 2017 | **Series F (2026-07)** | ~$2.1B [TO VERIFY] | General Atlantic, SoftBank, BlackRock | Reconfigurable Dataflow (RDU) systems | Enterprise, gov, sovereign | Dataflow arch + large-memory; agentic serving | ~$11B post; JPMorganChase partner [TO VERIFY] | Medium-High | Active |
| Tenstorrent | CA | 2016 | **Late (2025-11, ~$3.2B)** | ~$1.18B [TO VERIFY] | Fidelity, Samsung, Hyundai, AFW | RISC-V + Tensix AI chips/IP | Training+inference, IP licensing | Open RISC-V + scalable Ethernet mesh; IP model | Ascalon RISC-V IP; Intel/Qualcomm approaches [UNCONFIRMED] | High | Active |
| MatX | US | 2022 | **Series B (2026-02)** | ~$500M+ [TO VERIFY] | Jane Street, Situational Awareness, Spark | MatX One — LLM-optimized training chip | Frontier LLM training | Ex-Google TPU team; transformer-optimized | TSMC production; first shipments 2027 | High | Active |
| Groq | US | 2016 | Late | ~$1B+ [TO VERIFY] | BlackRock, Samsung | LPU (deterministic) — primarily inference | Inference (see [02](02_inference_accelerators.md)) | Deterministic SRAM dataflow | Strong inference traction | High | Active (see 02) |
| Esperanto Tech | US | 2014 | Restructured | ~$160M+ [TO VERIFY] | — | RISC-V many-core (ET-SoC) | Pivoted away from broad AI | 1000+ RISC-V cores | Pivoted/scaled back | Low | Semi-Stealth |
| Graphcore | UK | 2016 | Acquired | ~$700M raised | Sequoia, BMW i | IPU dataflow | (now SoftBank) | MIMD graph processor | Acquired by SoftBank 2024 | Archived | Acquired |
| Habana Labs | IL | 2016 | Acquired | ~$120M raised | Intel Capital, Bessemer | Gaudi training/inference | (now Intel) | Training + inference ASICs | Intel Gaudi line | Archived | Acquired (Intel) |

## 4. Company Profiles

### Cerebras Systems

- **Status:** Active — **public company (NASDAQ: CBRS) since 2026-05-14**
- **Headquarters:** Sunnyvale, US
- **Founded:** 2015
- **Founders:** Andrew Feldman, Gary Lauterbach, Sean Lie, Michael James, Jean-Philippe Fricker (SeaMicro alumni)
- **Stage:** Public
- **Total Funding:** ~$720M+ private [TO VERIFY]; **IPO raised ~$5.5B at $185/share, ~$56B implied valuation** [CONFIRMED announced]
- **Last Round:** IPO, 2026-05-14 — priced $185, opened ~$350, closed day one ~$311 (+68%); largest semiconductor IPO on record [TO VERIFY superlative]
- **2026 financials:** FY2025 revenue ~$510M; Q1 2026 revenue $193.4M (core $191.3M, +92% YoY); FY2026 core revenue guidance ~$855–865M [TO VERIFY]
- **Anchor contract:** OpenAI, announced 2026-01-14 — up to **750MW** of wafer-scale inference capacity, reported at **>$20B**, phased through 2028 [TO VERIFY terms]
- **Key Investors:** Benchmark, Foundation Capital, Eclipse, Coatue, Altimeter, G42 [TO VERIFY mix]
- **Strategic Investors:** G42 (also largest customer) [TO VERIFY]
- **Employees:** ~400+ [ESTIMATED]
- **Website:** cerebras.ai
- **Primary Category:** 01 Training · **Secondary:** 02 Inference, 16 DC Infra
- **One-Line Description:** Wafer-scale AI systems and cloud, the largest single-chip processor for training and fast inference.

#### Product / Technology
- **Builds:** Wafer-Scale Engine (WSE-3) and CS-3 systems; Cerebras Cloud / inference service.
- **Core architecture:** Entire wafer as one chip — ~900k cores, massive on-wafer SRAM and bandwidth, weight-streaming for large models.
- **Key claims:** Eliminates multi-GPU partitioning pain; very high memory bandwidth; record inference token throughput.
- **Software stack:** Cerebras SDK / PyTorch integration; weight-streaming execution.
- **Supply-chain deps:** TSMC wafer-scale process, custom packaging/cooling.
- **Maturity:** Production systems; multiple datacenter deployments. **Differentiation:** Wafer-scale bandwidth. **Risks:** Yield/cost, customer concentration (G42), CUDA ecosystem gap.

#### Market and Customer Traction
- **Segments:** Sovereign AI, labs, pharma/HPC, inference clouds.
- **Customers/partners:** G42 (anchor), national labs, Mayo Clinic, GSK [TO VERIFY current].
- **Deployment:** Multiple "Condor Galaxy"-class systems [TO VERIFY]. **GTM:** Systems sales + cloud + inference API.

#### Competitive Landscape
- **Direct/incumbent:** NVIDIA, AMD, Google TPU, Groq (inference). **Substitutes:** GPU clusters. **Defensibility:** Wafer-scale IP, systems integration; **risk:** ecosystem breadth, demand concentration.

#### VC Investment View
- **Attractiveness:** Now a public comparable rather than a venture opportunity · **Why it matters to the database:** CBRS is the mark-to-market reference for every private trainer and fast-inference company in this database.
- **Upside:** Contracted backlog (OpenAI) far exceeds current revenue. **Downside:** extreme customer concentration — the anchor contract is roughly 23x FY2026 core revenue guidance, so renegotiation or slippage is the dominant risk; plus wafer economics and post-lockup supply.
- **Diligence Qs (updated):** How is the 750MW contract recognized and financed? What is the capital cost of the deployment, and who carries it? Concentration disclosure in the 10-Q. Margin at wafer-scale as volume rises. **Exit:** done (IPO). **Risks:** concentration, capex financing, post-IPO expectations.

#### Data Quality
- **Source confidence:** High for the IPO and reported financials (public filings); Medium for the OpenAI contract economics. **Gaps:** revenue split by customer, deployment capex financing. **Verify next:** next 10-Q concentration disclosure; OpenAI deployment milestones. **Last updated:** 2026-08-13. **Sources:** company press releases, IPO pricing release, Q1 2026 results, trade press.

### SambaNova Systems

- **Status:** Active · **HQ:** Palo Alto, US · **Founded:** 2017
- **Founders:** Rodrigo Liang, Kunle Olukotun (Stanford), Christopher Ré (Stanford)
- **Stage:** Series F · **Total Funding:** ~$2.1B [TO VERIFY] · **Last Round:** **Series F first close ~$1B at ~$11B post-money, July 2026, led by General Atlantic** with Seligman Ventures, T. Rowe Price and Capital Group [TO VERIFY]
- **Key Investors:** General Atlantic, SoftBank, BlackRock, Temasek, GV, Intel Capital [TO VERIFY] · **Employees:** ~500 [ESTIMATED] · **Website:** sambanova.ai
- **Primary:** 01 Training · **Secondary:** 02 Inference
- **One-Line:** Reconfigurable Dataflow (RDU) systems and a full-stack platform for training and agentic inference.

#### Product / Technology
- Reconfigurable Dataflow Unit (RDU), large-memory architecture (SN40L), SambaStack software; "Samba-1" composite model offering. Differentiation: dataflow + 3-tier memory for large models; pivoted toward enterprise/gov inference + agentic serving. Risks: CUDA gap, GTM concentration in gov/enterprise.

#### Market / Competitive / VC View
- **Customers:** US national labs, governments, enterprise; **JPMorganChase named as an inference infrastructure partner (2026)** [TO VERIFY]. **Competitors:** NVIDIA, Cerebras, Groq, and increasingly lab-commissioned merchant ASICs. **Attractiveness:** Medium-High · **Venture-scale:** Medium-High · **Exit:** M&A or IPO · **Acquirers:** systems vendors, hyperscalers. **Risks:** demand concentration, software ecosystem, the gap between an $11B mark and disclosed revenue.
- **2026 note:** the Series F is a repositioning round — SambaNova is now sold as regulated-enterprise and agentic *inference* infrastructure, not as a training platform. Watch whether the second close completes at the same price.
- **Data quality:** Medium. **Verify next:** Series F final close and total raised; revenue; whether reported Intel acquisition interest [UNCONFIRMED] is real. **Last updated:** 2026-08-13.

### Tenstorrent

- **Status:** Active · **HQ:** Toronto, CA · **Founded:** 2016
- **Founders:** Ljubisa Bajic et al.; led by **Jim Keller** (CEO)
- **Stage:** Late (post-Series D) · **Total Funding:** ~$1.18B [TO VERIFY] · **Last Round:** **~$800M led by Fidelity at a ~$3.2B valuation, November 2025** [TO VERIFY]; prior ~$693M Series D led by Samsung Securities/AFW Partners, 2024
- **Key/Strategic Investors:** Fidelity, Samsung, Hyundai, LG, AFW, Bezos Expeditions [TO VERIFY] · **Website:** tenstorrent.com
- **Primary:** 01/02 · **Secondary:** 04 Custom ASIC/RISC-V IP
- **One-Line:** Open, RISC-V-based AI compute (Tensix) and licensable IP — an "anti-CUDA," open-ecosystem bet.

#### Product / Technology
- Tensix AI cores + RISC-V CPU IP; scalable Ethernet-connected mesh (Wormhole/Blackhole chips, Galaxy systems); open software (tt-Metalium/tt-Buda). **Differentiation:** open ISA + IP licensing model (à la Arm) alongside chips; standard Ethernet scale-out. **Risks:** software maturity vs. CUDA; dual chip+IP focus.

#### Market / Competitive / VC View
- **Customers/partners:** IP deals (e.g., LG, Hyundai), dev cloud; Ascalon RISC-V datacenter IP push (late 2025); sovereign/regional programs in Japan, Cyprus, the GCC and the UAE [TO VERIFY]. **Competitors:** NVIDIA, AMD, Arm (IP), SiFive (RISC-V — now $970M funded at ~$3.65B). **Attractiveness:** High · **Venture-scale:** High · **Exit:** IPO or strategic; **2026 reporting describes early takeover conversations with Intel and Qualcomm [UNCONFIRMED — rumor, do not treat as a deal]**. **Acquirers:** Samsung, Qualcomm, Intel, hyperscalers. **Risks:** software ecosystem, focus split between chips and IP.
- **Data quality:** Medium-High. **Verify next:** whether the ~$800M round is formally Series E; status of any strategic approach; Ascalon licensing traction. **Last updated:** 2026-08-13.

### MatX (promoted from lighter coverage, 2026-08-13)

- **Status:** Active · **HQ:** Mountain View, US · **Founded:** 2022 · **Founders:** Reiner Pope, Mike Gunter (ex-Google TPU/LLM infrastructure)
- **Stage:** Series B · **Total Funding:** ~$500M+ [TO VERIFY] · **Last Round:** ~$500M Series B, 2026-02-24, co-led by **Jane Street** and **Situational Awareness LP**, with Spark Capital, Triatomic Capital, Harpoon Ventures; strategic participation from **Alchip** and **Marvell**; angels including Andrej Karpathy and Patrick & John Collison [TO VERIFY]
- **Product:** MatX One — a processor specialized for large-language-model training and serving, manufactured at TSMC, with first shipments targeted for **2027**. Claimed ~10x efficiency vs. GPUs for LLM training [TO VERIFY — vendor claim; no independent benchmark].
- **Why it matters:** one of the largest Series B rounds in semiconductor history, and the clearest example of the 2026 capital shift — a prop-trading firm and a thesis fund co-leading a pre-silicon hardware company. The presence of Alchip and Marvell also tells you the design-services and connectivity path is already contracted.
- **VC view:** Attractiveness High but pre-revenue and pre-silicon; the risk is no longer capital, it is schedule and the merchant-ASIC substitute (OpenAI/Broadcom "Jalapeño" shipped a competing concept in ~9 months). **Diligence:** tape-out date, HBM and CoWoS allocation, named launch customer, compiler/runtime staffing.
- **Data quality:** Medium. **Verify next:** valuation, tape-out status, customer commitments. **Last updated:** 2026-08-13.

> Lighter-coverage entries (Esperanto) and archived entries (Graphcore, Habana) are summarized in the table above; expand to full profiles as public data warrants.

## 5. Category-Level Investment Heatmap

| Subsegment | Market Pull | Technical Difficulty | Capital Intensity | Incumbent Risk | Startup Opportunity | VC Attractiveness |
|------------|:-----------:|:--------------------:|:-----------------:|:--------------:|:-------------------:|:-----------------:|
| Wafer-scale systems | High | Very High | Very High | High | Niche | Medium |
| Dataflow/RDU | Medium | High | High | High | Narrow | Medium |
| RISC-V open AI compute/IP | Medium-High | High | Medium-High | Medium | Real (IP leverage) | Medium-High |
| Transformer-optimized trainers | Medium | High | High | Very High | Narrow | Medium |
| Sovereign-AI trainers | High | High | Very High | Medium | Real (anchor demand) | Medium-High |

## 6. Leading Investors in This Category

| Investor | Type | Relevant Portfolio | Stage Preference | Recent Activity | Thesis Signal |
|----------|------|--------------------|------------------|-----------------|---------------|
| SoftBank | Strategic/Growth | SambaNova, Graphcore (acq), Arm | Growth | Acquired Graphcore | "Own the AI compute stack" |
| G42 | Strategic/Sovereign | Cerebras | Growth | Cerebras anchor | Sovereign AI demand |
| Samsung Catalyst | Strategic | Tenstorrent, Groq | A–Growth | Led Tenstorrent D | Memory/foundry adjacency |
| Benchmark | VC | Cerebras | Early | Long-hold | Wafer-scale conviction |
| Fidelity / BlackRock | Crossover | Cerebras, SambaNova, Groq | Growth/Pre-IPO | Pre-IPO rounds | Public-market bridge |

## 7. Leading Research and Researcher Signals

| Researcher / Lab | Institution | Research Area | Why It Matters | Startup Formation Signal | Relevant Papers / Patents | VC Relevance | Confidence |
|------------------|-------------|---------------|----------------|--------------------------|---------------------------|:------------:|------------|
| Kunle Olukotun | Stanford | Dataflow, RDA | SambaNova founder; dataflow lineage | Confirmed Startup (SambaNova) | Plasticine/RDA papers | 5 | High |
| Bill Dally | Stanford/NVIDIA | Accelerator arch, interconnect | Defines the GPU roadmap; talent source | Watchlist (incumbent) | ISCA/MICRO body | 5 | High |
| Berkeley ADEPT/SLICE | UC Berkeley | RISC-V, agile HW, accelerators | RISC-V training-chip talent pipeline | Likely Startup Signal | RISC-V, Gemmini | 4 | Medium |
| MatX team (ex-Google TPU) | Industry | Transformer-optimized silicon | Confirmed company; pedigree | Confirmed Startup (MatX) | TPU lineage | 4 | Medium |

See [../researchers/leading_researchers_index.md](../researchers/leading_researchers_index.md).

## 8. Diligence Questions

- **Technical:** Memory-bandwidth advantage vs. HBM-GPU? Software/compiler maturity vs. CUDA? Tape-out node, yield, packaging supply?
- **Market:** Is demand anchored (sovereign/hyperscaler) or speculative? Real serviceable training TAM?
- **Customer:** Committed multi-year contracts vs. pilots? Concentration risk?
- **Competitive:** Survives NVIDIA Rubin + supply expansion? AMD/TPU pressure?
- **Financial:** Capital to next milestone? Gross margin at scale? HBM/CoWoS allocation secured?
- **Founder:** Shipped silicon before? Can recruit scarce architects/compiler talent?
- **Exit:** IPO-viable revenue scale? Realistic strategic acquirers given size?

## 9. Refresh Notes

| Date | Refresh Type | Entries Added | Entries Updated | Entries Archived | Key Changes | Sources |
|------|--------------|---------------|-----------------|------------------|-------------|---------|
| 2026-06-09 | Full (initial) | 9 | 0 | 2 (Graphcore, Habana) | Initial build; thesis, market context, profiles for Cerebras/SambaNova/Tenstorrent; heatmap, investors, research signals | Company sites, S-1, trade press |
| 2026-08-13 | Full refresh | 0 | 5 (Cerebras, SambaNova, Tenstorrent, MatX, category thesis) | Cerebras IPO'd (NASDAQ: CBRS, ~$5.5B raised, ~$56B implied) on the back of a >$20B / 750MW OpenAI contract; SambaNova raised ~$1B Series F at ~$11B; Tenstorrent ~$800M at ~$3.2B with reported Intel/Qualcomm approaches; MatX promoted to a full profile after a ~$500M Series B; added the OpenAI/Broadcom "Jalapeño" merchant-ASIC substitution risk to the thesis | Company releases, Q1'26 results, trade press |
