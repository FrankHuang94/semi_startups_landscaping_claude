# Market Map — AI Semiconductor Stack

A structural map of where value, bottlenecks, and venture opportunity sit across the AI compute stack. Use this to navigate categories and to frame thesis conversations.

> **Last updated:** 2026-11-04 (Refresh #3). See the "2026 State of the Stack" section and the updated acquirer map below.

---

## The AI Datacenter Stack (top → bottom)

```
┌──────────────────────────────────────────────────────────────────┐
│  MODELS / WORKLOADS  (training, inference, reasoning, multimodal)  │   ← demand driver
├──────────────────────────────────────────────────────────────────┤
│  SYSTEM SOFTWARE   compilers · runtimes · serving · orchestration  │   ← the moat layer (CUDA)
├──────────────────────────────────────────────────────────────────┤
│  COMPUTE SILICON   training [01] · inference [02] · edge [03]      │
│                    custom ASIC & chiplets [04] · analog/PIM [14]   │
├──────────────────────────────────────────────────────────────────┤
│  MEMORY [07]   HBM4 · CXL · PIM · HBF · memory-dense servers       │   ← #1 bottleneck (2026 shortage)
├──────────────────────────────────────────────────────────────────┤
│  INTERCONNECT  scale-up/scale-out [05] · optical & CPO [06]        │   ← #2 bottleneck
│                D2D / UCIe chiplet links [04][13]                   │
├──────────────────────────────────────────────────────────────────┤
│  PACKAGING & INTEGRATION [13]   CoWoS · hybrid bonding · substrate │   ← #3 bottleneck (supply)
├──────────────────────────────────────────────────────────────────┤
│  POWER & THERMAL [08][16]   GaN/SiC · power delivery · cooling     │   ← rising fast (100kW racks)
├──────────────────────────────────────────────────────────────────┤
│  DESIGN ENABLEMENT [12]   EDA · IP · AI-for-chip-design            │   ← capital-efficient wedge
├──────────────────────────────────────────────────────────────────┤
│  FOUNDRY [13]   leading-edge logic · advanced nodes               │   ← TSMC-dominated
└──────────────────────────────────────────────────────────────────┘
   Adjacencies: Security/Confidential [09] · RF [10] · Analog/Timing [11] · Automotive/Robotics [15] · Quantum [14]
```

---

## The Three Binding Bottlenecks (where venture money should concentrate)

| Rank | Bottleneck | Why it binds | Categories | Startup angle |
|:----:|------------|--------------|------------|---------------|
| 1 | **Memory** (bandwidth + capacity + cost) | HBM supply-limited; model size > on-package memory; **2026 DRAM/HBM shortage** (contract prices roughly doubled in 1H26 per TrendForce [TO VERIFY]; tightness expected into 2027+) | 07, 14 | CXL pooling/compute-memory (XCENA, Panmnesia), memory-dense servers (Majestic), HBF, DRAM-stacked inference (d-Matrix), SRAM-heavy inference |
| 2 | **Interconnect** (scale-up bandwidth/energy) | Copper reach/energy limits; collectives dominate training time; open scale-up standards (UALink, ESUN) vs. NVLink Fusion | 05, 06 | Optical I/O (Ayar, Lumilens), CPO supply chain, merchant UALink/Ethernet scale-up switches (Upscale AI, Xsight) |
| 3 | **Packaging/Power** (supply + density) | CoWoS allocation; racks heading past 200kW with 800V DC distribution; thermal | 13, 08, 16 | Glass substrate, hybrid bonding, new lithography (Substrate, xLight, Lace), in-package/vertical power (PowerLattice; Empower→ADI), GaN, liquid cooling |

> Heuristic: **a startup selling into a binding bottleneck with a strategic acquirer pre-identified is the highest-quality AI-silicon venture profile.**

---

## Value-Chain Position vs. Venture Attractiveness

| Layer | Incumbent dominance | Startup whitespace | VC attractiveness |
|-------|---------------------|--------------------|:-----------------:|
| Models/workloads | OpenAI/Anthropic/Google/Meta | (not silicon) | n/a |
| System software | NVIDIA CUDA | thin (open stacks emerging) | Medium |
| Training silicon | NVIDIA + hyperscaler in-house | narrow (systems/sovereign) | Medium |
| Inference silicon | NVIDIA, but contestable | **wide** (perf/$, latency) | **High** |
| Memory fabric | SK hynix/Samsung/Micron | **architecture layer** | High |
| Interconnect | Broadcom, NVIDIA | NIC/DPU, optical, fabric | **High** |
| Optical/CPO | forming (Broadcom, NVIDIA, Marvell+Celestial) | **strategic pull proven by M&A** | **High** |
| Packaging | TSMC/Amkor/ASE | materials, IP, novel fab | High |
| Power/cooling | Vertiv/Infineon | density, GaN, immersion | High |
| EDA/IP | Synopsys/Cadence (+NVIDIA $2B in Synopsys) | **agentic AI-for-design** (Ricursive, ChipAgents, Cognichip) | **High** |
| Quantum/analog | none (greenfield) | binary moonshots | Medium |

---

## Demand Drivers (what is pulling the market)

1. **AI capex super-cycle** — hyperscaler + sovereign datacenter buildout.
2. **Inference cost crisis** — cost-per-token / perf-per-watt is now a P&L line.
3. **Custom silicon proliferation** — every hyperscaler and frontier lab wants its own chip.
4. **Power & cooling wall** — racks moving 10kW → 100kW+; grid constraints.
5. **Geopolitical re-shoring & sovereign AI** — demand for non-NVIDIA, in-region silicon and supply.
6. **Physical AI** — robotics/humanoids/autonomy as the next compute frontier.

## Structural Risks (what could deflate categories)

- NVIDIA roadmap + software ubiquity neutralizing hardware differentiation.
- AI-capex digestion / demand air-pocket (not visible as of Nov 2026; capex guidance still rising).
- Antitrust scrutiny of licence + acqui-hire structures (a DOJ inquiry into NVIDIA–Groq has been reported [UNCONFIRMED]).
- Valuation compression for 2026 mega-round vintages if public AI-semi multiples reset.
- HBM & CoWoS supply easing (good for builders, compresses scarcity premia).
- Open software stacks commoditizing inference silicon advantages.
- Capital intensity outrunning private funding appetite for hard-tech.

---

## 2026 State of the Stack (Refresh #3)

| Layer | What changed (2025H2–2026) | Implication for venture |
|-------|----------------------------|-------------------------|
| Demand | Big-cloud 2026 capex tracking ~$800B+ with higher 2027 signalled; OpenAI 10 GW (Broadcom) + 6 GW (AMD) + Cerebras >$10B; Anthropic up to 1M Google TPUs | Demand risk low near-term; supply (memory, packaging, power) is the constraint |
| Compute | Vera Rubin + HBM4 ramp 2H26; Google TPUs sold to external customers; Cerebras public; Chinese GPU IPO wave | Merchant startups must show signed capacity contracts, not benchmarks |
| Exits | Licence + acqui-hire (NVIDIA–Groq/Enfabrica); strategic M&A across optics, RISC-V, edge, power; IPO window open | Underwrite multiple exit structures; diligence waterfall terms |
| Capital | $300M+ Series A/seed rounds (Ricursive, Unconventional AI); $500M–$1.5B late rounds (Tenstorrent, MatX, Etched, Ayar, Lumilens) | Crowded trade — favour bottleneck-adjacent, capital-efficient models |

## Likely Acquirer Map (exit planning)

| Acquirer | Buys in | Recent/representative posture |
|----------|---------|-------------------------------|
| NVIDIA | networking, inference IP, software, memory fabric — prefers **licence + acqui-hire** | Groq (~$20B licence + team, Dec 2025), Enfabrica (>$900M licence + team, Sep 2025); $5B Intel stake, $2B Synopsys stake |
| AMD | inference, networking, systems, software, photonics | Taalas (Aug 2026), Untether team, Enosemi, Brium, ZT Systems; up to $5B in Anthropic |
| Broadcom | networking, custom ASIC, optical | merchant ASIC + switching leader |
| Marvell | custom ASIC, interconnect, optical | Celestial AI ($3.25B upfront, closed Feb 2026) |
| Intel / Intel Foundry | packaging, IP, foundry, analog | Habana, Tower; foundry buildout |
| Qualcomm | data-center CPU/RISC-V, SerDes, edge, automotive | Alphawave (~$2.4B), Ventana, Akeana — building a DC silicon unit |
| SK hynix / Samsung / Micron | memory, CXL, PIM, packaging | memory + foundry strategics |
| Infineon / Renesas / ADI / Microchip / NXP | power, analog, timing, edge AI | ADI–Empower ($1.5B), Microchip–Hailo, NXP–Kinara ($307M) |
| Cadence / Synopsys / Siemens EDA | EDA, IP | Cadence–ChipStack; Synopsys–Ansys, sold ARC IP to GlobalFoundries |
| Meta / hyperscalers | custom silicon teams, RISC-V | Meta–Rivos (2025) |
| Connectivity/optical strategics (Ciena, Molex, Arm) | optical engines, CPO supply chain, networking IP | Ciena–Nubis ($270M), Molex–Teramount, Arm–DreamBig (~$265M) |
| Well-funded startups | teams + IP | Tenstorrent–Blue Cheetah, d-Matrix–GigaIO DC unit, Unconventional AI–NeuReality |
| Hyperscalers (Google/AWS/Microsoft) | custom silicon teams, talent | acqui-hire + in-house programs; Google now sells TPUs externally |

See [deal_tracker/20_ma_tracker.md](deal_tracker/20_ma_tracker.md) and [deal_tracker/24_strategic_investor_tracker.md](deal_tracker/24_strategic_investor_tracker.md).
