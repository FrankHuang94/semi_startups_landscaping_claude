# Stealth Startup Discovery

A discipline for identifying early signals of future AI semiconductor startups **before** formal funding announcements — so a VC team can be the first call.

> **This file finds signals, not secrets.** Everything here must come from public, lawful, professional sources. We do not publish private personal data, non-public employment information, confidential deal terms, or speculation presented as fact. Every entry is labeled **Confirmed / Likely / Weak Signal / To Verify**.

---

## 1. Methodology

**Allowed sources**
- Company websites & domain launch / placeholder pages
- Public funding announcements & press releases
- SEC Form D filings (where applicable)
- University lab pages & published papers
- Patent databases & assignment records
- Conference agendas (ISSCC, ISCA, MICRO, HotChips, OFC, VLSI, DAC, MLSys)
- Public professional profiles (e.g., public LinkedIn role/title changes)
- GitHub repositories & open-source activity
- Job postings (including "stealth"/"confidential" hardware roles)
- Investor portfolio pages & accelerator demo days / cohorts
- Public incorporation/company registries where legally accessible

**Disallowed**
- Private personal information
- Non-public employment information
- Confidential deal information
- Scraped private data
- Speculation presented as fact

**Confidence labels**
- **Confirmed** — public funding / incorporation / company statement
- **Likely** — multiple converging public signals
- **Weak Signal** — single early indicator
- **To Verify** — lead requiring confirmation

---

## 2. Stealth Startup Watchlist

> Seed examples below illustrate the schema and method. Populate/replace at each refresh from live public signals. Entries marked `[ILLUSTRATIVE]` are method demonstrations, not claims of company formation.

| Signal Name | Category | People / Lab | Evidence | Signal Strength | Possible Thesis | Investor Relevance | Next Step | Confidence |
|-------------|----------|--------------|----------|-----------------|-----------------|--------------------|-----------|------------|
| `[ILLUSTRATIVE]` PIM spinout watch | 07/14 | ETH Zürich (Mutlu group) | Repeated PIM papers in urgent bottleneck; prior industry collaborations | Weak Signal | Near-memory accelerator IP | High | Monitor patent assignees & role changes | To Verify |
| `[ILLUSTRATIVE]` Photonics fabric watch | 06 | Columbia (Bergman group) | Sustained CPO/photonic-fabric publications; ecosystem ties | Weak Signal | Optical interconnect fabric | High | Track grad/postdoc departures & domains | To Verify |
| `[ILLUSTRATIVE]` Analog in-memory cluster | 14 | Multiple (Princeton-style IMC) | Field-wide commercialization momentum (EnCharge precedent) | Weak Signal | Energy/token inference IP | High | Map who is *not yet* funded | To Verify |
| `[ILLUSTRATIVE]` AI-EDA founder watch | 12 | ML-systems + EDA crossovers | GitHub traction in RTL/verification LLM tooling | Weak Signal | AI-native verification | High | Watch repo adoption + seed rounds | To Verify |

---

## 3. Research-to-Company Formation Signals

Track teams whose public work suggests possible startup formation. Cross-reference [RESEARCH_AND_RESEARCHERS.md](RESEARCH_AND_RESEARCHERS.md) and the signal framework there.

- Repeated, high-citation publications targeting a **commercially urgent** bottleneck (memory, interconnect, packaging, inference cost).
- Patent filings transitioning from university assignee to a new/unknown entity.
- Public collaborations between an academic group and a hyperscaler/chip company.
- A lab with prior spinout history publishing a new "platform-shaped" result.

## 4. Recent Stealth Funding Signals

Track public, lawful funding indicators:
- **SEC Form D** filings naming a new entity with hardware/semiconductor descriptors.
- Seed announcements on investor portfolio pages before press coverage.
- Accelerator cohort listings (e.g., deep-tech / hard-tech tracks).
- Investor blog posts hinting at a new category bet.

| Date | Entity | Signal Type | Public Source Type | Confidence | Notes |
|------|--------|-------------|--------------------|------------|-------|
| — | — | Form D / portfolio page / cohort | — | — | Populate at refresh |

## 5. Job Posting Signals

Stealth/confidential companies frequently reveal themselves through hiring. Track public postings for:

- AI accelerator architecture · ML compiler · RTL design · physical design
- HBM PHY · SerDes · silicon photonics · CPO
- EDA · memory systems · datacenter networking · power delivery · packaging

| Role cluster | Likely category | Stealth tell | Confidence |
|--------------|-----------------|--------------|------------|
| "Stealth" + SerDes/PHY + compiler | 02/05 | New silicon team forming | Likely |
| Photonics packaging + test | 06 | Optical startup ramping | Likely |
| ML-compiler + kernel + "confidential" | 02/12 | Inference startup pre-launch | Likely |

## 6. Investor Signal Tracker

VC firms / partners repeatedly investing in adjacent areas often telegraph the next category. Track:
- Firms with 2+ recent AI-silicon deals (see [deal_tracker/21_vc_investor_tracker.md](deal_tracker/21_vc_investor_tracker.md)).
- Strategic arms (NVIDIA, Samsung, Intel Capital) co-investing — a strong validation + exit signal.
- Partners moving firms or launching dedicated hard-tech funds.

## 7. Next Outreach / Sourcing Questions (for expert calls)

- Which labs are producing the strongest PhD talent in accelerators/photonics/memory?
- Which researchers recently left major chip companies (NVIDIA, Google, Apple, Broadcom)?
- Which technical bottlenecks are incumbents *not* solving?
- Which open-source hardware/software projects are gaining real developer pull?
- Which hyperscaler pain points are creating startup opportunities right now?
- Who are the "second-time founder" silicon people likely to start again?

---

## Discovery Workflow (repeatable)

1. Pull new signals from allowed sources since last refresh.
2. Tag each with category, people/lab, evidence, strength, confidence.
3. Promote any entity with ≥2 independent High/Very-High signals to the active watchlist.
4. Draft a one-line thesis + outreach next step per promoted entity.
5. Append findings; cross-link to category files and researcher index.
6. Append [REFRESH_LOG.md](REFRESH_LOG.md).
