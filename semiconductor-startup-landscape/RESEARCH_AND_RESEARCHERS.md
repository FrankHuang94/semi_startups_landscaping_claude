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
