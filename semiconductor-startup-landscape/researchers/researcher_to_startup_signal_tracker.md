# Researcher-to-Startup Signal Tracker

Live, scored tracker converting research signals into a ranked VC outreach queue. Public, professional signals only. See framework in [../RESEARCH_AND_RESEARCHERS.md](../RESEARCH_AND_RESEARCHERS.md) and discovery method in [../STEALTH_STARTUP_DISCOVERY.md](../STEALTH_STARTUP_DISCOVERY.md).

## Scoring
- **Signal Strength:** Very High / High / Medium / Low (per the signal framework)
- **VC Relevance:** 1–5
- **Outreach Priority** = function of (signal strength × VC relevance × bottleneck severity)
- **Status:** Confirmed / Likely / Weak / Watchlist Only

## Active Signal Table

| # | Person / Team / Lab | Linked Category | Signal(s) | Strength | Possible Thesis | VC Rel | Status | Next Step / Outreach |
|---|---------------------|-----------------|-----------|:--------:|-----------------|:------:|--------|----------------------|
| 1 | Naveen Verma / Princeton | 14/02 | Confirmed company (EnCharge); ongoing IMC research | Very High | Analog IMC efficiency | 5 | Confirmed | Maintain relationship; track next students |
| 2 | Bergman group / Columbia | 06 | Sustained photonic-fabric papers; ecosystem ties | Medium | Optical interconnect fabric | 5 | Likely | Monitor postdoc departures, patents, domains |
| 3 | Mutlu / ETH (SAFARI) | 07/14 | Repeated PIM papers in urgent bottleneck; industry collabs | Medium | PIM/near-memory IP | 5 | Likely | Watch patent assignees & spinout signals |
| 4 | Bowers group / UCSB | 06 | Laser-on-Si IP; photonics demand | Medium | Laser/DWDM for CPO | 5 | Likely | Track grad departures & licensing |
| 5 | NVIDIA/Google silicon alumni | 02/04/12 | Public role changes from incumbents to "stealth" | High | New inference/EDA/ASIC co. | 5 | Watchlist | Monitor LinkedIn role changes + Form D |
| 6 | AI-EDA founders (ML+EDA crossovers) | 12 | GitHub traction; seed cohort forming → **cohort funded: ChipAgents $134M, Architect Labs $24M, Bronco/Silimate at DAC 2026** | High | AI-native verification/RTL | 5 | **Confirmed (cohort)** | Move from watching to meeting; the seed window is closing |
| 7 | KAIST CXL group | 07 | Panmnesia precedent; continued CXL research; **Marvell's $540M XConn purchase repriced CXL switching** | Medium-High | CXL fabric IP | 4 | Likely | Watch for next KR spinout |
| 8 | Georgia Tech PRC | 13 | Glass/packaging patent clusters; reshoring funding; **glass interposers entered pilot production (2026)** | Weak-Medium | Packaging IP/materials | 4 | Weak | Monitor assignee changes |
| 9 | **Azalia Mirhoseini & Anna Goldie** (AlphaChip) | 12 | **CONVERTED — Ricursive Intelligence, $300M Series A at ~$4B, 2026-01-26**, led by Lightspeed with NVentures/Sequoia | Very High | AI systems designing silicon | 5 | **Confirmed** | Too late for entry; study the pattern — see lesson below |
| 10 | **QuTech / TU Delft cryo-electronics** | 14 | **CONVERTED — FrostByte spun out (2025)**, cryogenic control ICs | High | Quantum control picks-and-shovels | 4 | **Confirmed** | Track follow-on financing and the next Delft spinout |
| 11 | **Nick McKeown / photonic-compute circle** | 06/02 | **OLIX $312M at ~$3.3B (2026-08)**; McKeown joined the board | High | Optical tensor compute without HBM | 5 | **Confirmed** | Map the team's prior affiliations for the next formation |
| 12 | Groq / Enfabrica alumni now inside NVIDIA | 02/05 | **Jonathan Ross, Sunny Madra, Rochan Sankar joined NVIDIA via licence+hire deals (2025)** | High | Next deterministic-inference or fabric company | 5 | Watchlist | Retention periods typically run 2–4 years — set a calendar reminder, monitor departures from 2027 |
| 13 | Hailo / Rivos / Celestial alumni | 03/04/06 | Three teams absorbed or wound down in 2026 | Medium-High | Edge NPU, RISC-V, photonics restarts | 4 | Watchlist | Post-acquisition talent dispersal is the cheapest sourcing channel in the cycle |

## Outreach Queue (ranked)
1. **Act now:** the AI-EDA cohort (#6) — funded and scaling; the remaining entry points are seed-stage teams shipping at DAC.
2. **Confirmed relationships to deepen:** EnCharge/Verma circle (next-gen IMC founders).
3. **Highest-priority watch:** photonics (Bergman/Bowers) and PIM (Mutlu) lab departures.
4. **Structurally new (2026):** alumni dispersal from the year's absorptions — NVIDIA-bound Groq/Enfabrica leaders (#12, on a multi-year clock) and the Hailo/Rivos/Celestial diaspora (#13, available now).
5. **Longer fuse:** packaging/glass (Georgia Tech) and CXL (KAIST) commercialization.

## Lesson from the 2026 conversions (added 2026-08-13)

Two watch-items became companies within months, and both priced beyond venture entry almost immediately — Ricursive at **~$4B less than two months after launch**, OLIX at **~$3.3B in its second round**.

- **The signal that mattered was a named, deployed artifact**, not publication volume: AlphaChip shipped inside four generations of Google TPUs before Ricursive existed. Rank the watchlist by *artifacts in production*, not by citation counts.
- **The entry window is now pre-formation.** By the time a Form D or a launch post appears, the round is priced. The practical implication is that relationship-building has to happen while the researcher is still publishing.
- **Downgrade rule applied:** signals #9, #10 and #11 are marked Confirmed and moved out of the outreach queue; keeping converted items scored as "Likely" would inflate the queue's apparent value.

## Hygiene
- Re-verify each signal at every refresh; **downgrade stale signals** (decay matters).
- Require **≥2 independent High/Very-High signals** before proactive outreach.
- Keep entries factual and public; never record private personal data.

## Refresh Notes
| Date | Refresh Type | Added | Updated | Sources |
|------|--------------|-------|---------|---------|
| 2026-06-09 | Full (initial) | 8 | 0 | Public publications, role changes, patent themes |
| 2026-08-13 | Full refresh | 5 (Mirhoseini/Goldie converted, QuTech/FrostByte, McKeown/OLIX, NVIDIA-bound alumni, 2026 diaspora) | 3 (AI-EDA cohort upgraded to Confirmed, KAIST CXL, Georgia Tech) | Company releases, public role changes, DAC/ISSCC/ISCA 2026 programs |
