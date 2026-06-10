# Market Map — AI Semiconductor Stack

A structural map of where value, bottlenecks, and venture opportunity sit across the AI compute stack. Use this to navigate categories and to frame thesis conversations.

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
│  MEMORY [07]   HBM · CXL pooling · PIM · near-memory               │   ← #1 bottleneck
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
| 1 | **Memory** (bandwidth + capacity + cost) | HBM supply-limited; model size > on-package memory | 07, 14 | CXL pooling, PIM, near-memory, base-die IP |
| 2 | **Interconnect** (scale-up bandwidth/energy) | Copper reach/energy limits; collectives dominate training time | 05, 06 | Optical I/O, CPO, memory fabric, Ethernet-for-AI |
| 3 | **Packaging/Power** (supply + density) | CoWoS allocation; 100kW racks; thermal | 13, 08, 16 | Glass substrate, hybrid bonding, GaN power, liquid cooling |

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
| Optical/CPO | early/forming | **greenfield + strategic pull** | **High** |
| Packaging | TSMC/Amkor/ASE | materials, IP, novel fab | High |
| Power/cooling | Vertiv/Infineon | density, GaN, immersion | High |
| EDA/IP | Synopsys/Cadence | **AI-native tools, RISC-V** | **High** |
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
- AI-capex digestion / demand air-pocket.
- HBM & CoWoS supply easing (good for builders, compresses scarcity premia).
- Open software stacks commoditizing inference silicon advantages.
- Capital intensity outrunning private funding appetite for hard-tech.

---

## Likely Acquirer Map (exit planning)

| Acquirer | Buys in | Recent/representative posture |
|----------|---------|-------------------------------|
| NVIDIA | networking, optical, software, memory fabric | Mellanox, Enfabrica investment |
| AMD | inference, networking, systems, software | Pensando, ZT, Untether IP, Silo AI |
| Broadcom | networking, custom ASIC, optical | merchant ASIC + switching leader |
| Marvell | custom ASIC, interconnect, optical | custom-silicon + DSP/optics |
| Intel / Intel Foundry | packaging, IP, foundry, analog | Habana, Tower; foundry buildout |
| Qualcomm | edge, automotive, inference | edge/auto roll-ups |
| SK hynix / Samsung / Micron | memory, CXL, PIM, packaging | memory + foundry strategics |
| Infineon / Renesas / ADI | power, analog, timing | GaN/SiC roll-ups |
| Cadence / Synopsys / Siemens EDA | EDA, IP | AI-tool + IP tuck-ins |
| Hyperscalers (Google/AWS/Microsoft/Meta) | custom silicon teams, talent | acqui-hire + in-house programs |

See [deal_tracker/20_ma_tracker.md](deal_tracker/20_ma_tracker.md) and [deal_tracker/24_strategic_investor_tracker.md](deal_tracker/24_strategic_investor_tracker.md).
