# Research & Researchers — VC Sourcing Engine

This file is the entry point to the research-driven sourcing engine: the labs, researchers, papers, and patents most likely to produce the next generation of stealth-mode AI semiconductor startups. Detailed indexes live in [researchers/](researchers/).

> **Ethics & sourcing rules (read first):** Use **only public, lawful, professional** information — publications, lab pages, conference programs, patent databases, public funding/portfolio pages, public professional profiles, open-source repos. **Never** include private personal data, non-public employment details, or confidential deal information. **Never** assert that a researcher is forming a company without public evidence. All startup-formation signals are labeled by confidence.

---

## Index of Researcher Files

| File | Contents |
|------|----------|
| [researchers/leading_researchers_index.md](researchers/leading_researchers_index.md) | Profiles of leading academic & industry researchers |
| [researchers/university_labs_index.md](researchers/university_labs_index.md) | University lab profiles & spinout history |
| [researchers/corporate_research_labs_index.md](researchers/corporate_research_labs_index.md) | Corporate/industrial research lab profiles |
| [researchers/paper_watchlist.md](researchers/paper_watchlist.md) | Breakthrough & commercially-urgent papers |
| [researchers/patent_watchlist.md](researchers/patent_watchlist.md) | Patent clusters & assignment signals |
| [researchers/researcher_to_startup_signal_tracker.md](researchers/researcher_to_startup_signal_tracker.md) | Live signal tracker, scored |

---

## What This Engine Tracks

1. Leading academic researchers
2. Leading university labs
3. Leading corporate research labs
4. Key PhD students & postdocs (where public professional info supports relevance)
5. Breakthrough papers
6. Patent clusters
7. Conference signals (ISSCC, ISCA, MICRO, HotChips, OFC, VLSI, DAC, NeurIPS/MLSys systems tracks)
8. Open-source project signals
9. Lab-to-startup spinout history
10. Technical areas likely to produce startups

## Priority Research Areas (mapped to categories)

| Research area | Category | Why it matters for VC |
|---------------|----------|------------------------|
| AI accelerator architectures | 01/02 | Core compute differentiation |
| Sparse computing | 02/14 | Efficiency at inference |
| Transformer inference acceleration | 02 | Direct cost-per-token impact |
| LLM serving hardware | 02/16 | Serving economics |
| Near-memory & processing-in-memory | 07/14 | #1 bottleneck (memory) |
| CXL memory expansion & pooling | 07 | Memory disaggregation |
| Optical interconnect / CPO / silicon photonics | 06 | #2 bottleneck (interconnect) |
| Chiplets / UCIe / D2D | 04/13 | Disaggregation economics |
| Advanced packaging / HBM architecture | 13/07 | #3 bottleneck (supply) |
| EDA automation / AI-for-chip-design | 12 | Capital-efficient wedge |
| Hardware security / confidential computing | 09 | Trust + crypto acceleration |
| Power delivery / thermal management | 08/16 | 100kW-rack wall |
| Neuromorphic / analog AI / in-memory compute | 14 | Energy-per-token leadership |
| Quantum hardware / cryogenic CMOS | 14 | Long-horizon moonshot |
| Datacenter energy efficiency | 16 | Capex/opex pull |
| Robotics & edge AI silicon | 15/03 | Physical-AI frontier |

---

## Researcher Profile Schema

Each profile in [leading_researchers_index.md](researchers/leading_researchers_index.md) follows:

```
[Researcher Name]
- Institution / Organization
- Role
- Research Areas
- Why This Researcher Matters (VC-oriented)
- Relevant Papers
- Relevant Patents (if public)
- Prior Startup Activity (if public)
- Known Industry Collaborations (if public)
- Open-Source Projects (if public)
- Technical Differentiation
- Potential Startup Thesis
- Startup Signal Level: Confirmed / Likely / Weak / Watchlist Only
- VC Relevance Score: 1–5
- Confidence Level: High / Medium / Low
- Data Gaps
- Sources
```

## Lab Profile Schema

```
[Lab Name]
- Institution / Location / Principal Investigators
- Research Areas / Why It Matters
- Relevant Papers / Patents
- Spinout History
- Corporate Sponsors / Collaborators
- Startup Formation Potential: High / Medium / Low
- Key People to Track
- VC Relevance Score: 1–5
- Sources
```

---

## Research-to-Startup Signal Framework

| Signal | Strength | Interpretation |
|--------|----------|----------------|
| Company incorporated by researcher | **Very High** | Possible startup formation |
| Researcher leaves university/corporate lab for "stealth" role | High | Strong sourcing signal |
| Seed funding announced | **Very High** | Confirmed company formation |
| Patent assigned to a new entity | High | Possible commercialization |
| Lab publishes repeated papers in a commercially urgent bottleneck | Medium | Watchlist |
| Researcher collaborates with hyperscaler or chip company | Medium | Commercial relevance |
| Job postings for hardware architects under a stealth company | High | Possible startup ramp |
| Domain launch / website placeholder | Medium | Early formation signal |
| GitHub project gains industry adoption | Medium | Open-source commercialization potential |
| Conference tutorial/keynote on an emerging bottleneck | Low/Medium | Thought-leadership signal |

> Operating rule: a single signal is a lead, not a conclusion. Two or more independent high/very-high signals on the same person/team warrants proactive outreach. Always cross-check against [STEALTH_STARTUP_DISCOVERY.md](STEALTH_STARTUP_DISCOVERY.md).

---

## How to Use This for Sourcing

1. **Map bottlenecks → labs.** Start from the three binding bottlenecks (memory, interconnect, packaging/power) and the labs that lead them.
2. **Score people.** Use VC Relevance (1–5) × Signal Level to rank.
3. **Watch the leading indicators.** LinkedIn role changes, patent assignees, new domains, stealth job posts, accelerator cohorts.
4. **Build the first-call list.** Maintain a ranked outreach queue in [researchers/researcher_to_startup_signal_tracker.md](researchers/researcher_to_startup_signal_tracker.md).
5. **Re-verify.** Signals decay; confirm at each refresh and downgrade stale ones.

---

## Engine Performance — 2026-08-13 Refresh

The point of this engine is to be early. Measured against the initial build, it was directionally right and operationally late.

**Conversions recorded this cycle:**

| Watch-item at initial build | Outcome | Elapsed |
|---|---|---|
| AI-EDA agents (theme) + Mirhoseini & Goldie (researcher watchlist, "Likely") | **Ricursive Intelligence** — $300M Series A at ~$4B post, 2026-01-26 | Watchlist → $4B in under a year |
| AI-EDA seed cohort | **ChipAgents** ($134M cumulative), **Architect Labs** ($24M seed), Bronco AI, Silimate | ~12 months |
| Cryo-CMOS / quantum control (theme) | **FrostByte** — QuTech / TU Delft spinout | ~12 months |
| *(not on the watchlist)* | **OLIX** — $312M at ~$3.3B, London, photonic tensor compute | Missed |

**What this changes about the method:**

1. **Score on deployed artifacts, not publication counts.** Both large conversions came from people whose work was already in production silicon — AlphaChip ran in four generations of Google TPUs before Ricursive existed. A paper that shipped beats a paper that is cited.
2. **The entry window is pre-formation.** Ricursive was priced at ~$4B within two months of launching. For top-tier researchers, "watch for the Form D" is already too late; the relationship has to exist while they are still publishing.
3. **Widen the geographic sweep.** The one clean miss (OLIX) was European, founded in 2024, and became the largest semiconductor venture round in European history. The lab list in this file skews US; add UK/EU/Israel/Korea labs and sovereign-program-adjacent formation.
4. **Add a post-absorption talent sweep — new for this cycle.** 2026 dispersed an unusual amount of senior silicon talent: Groq's and Enfabrica's leadership into NVIDIA (licence-and-hire deals, typically with multi-year retention, so reachable around 2027–2029), and the Hailo, Rivos and Celestial AI teams into their acquirers. Track departures from acquirers as deliberately as departures from labs.
5. **Record outcomes, including misses.** A watchlist without a scoreboard cannot be calibrated. Converted items are now marked Confirmed and removed from the outreach queue in [researchers/researcher_to_startup_signal_tracker.md](researchers/researcher_to_startup_signal_tracker.md) rather than left inflating it.

**Where the engine should point next (from the 2026 conference cycle):** MoE data movement, chiplet-scale interconnect (UCIe-Advanced), and memory reliability/ECC co-design — see section I of [researchers/paper_watchlist.md](researchers/paper_watchlist.md).
