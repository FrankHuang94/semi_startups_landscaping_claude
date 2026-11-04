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

> **Last refreshed: 2026-11-04 (Refresh #3).** Rows are now a mix of (a) research-lineage companies that *surfaced* from stealth/semi-stealth in 2025–2026 with public funding (Confirmed), and (b) pattern-level watch-items (no company asserted). Rows still marked `[ILLUSTRATIVE]` are method demonstrations, not claims of company formation. Funding figures carry data-quality tags: [CONFIRMED] / [TO VERIFY] / [UNCONFIRMED].

### 2a. Surfaced in 2025–2026 (Confirmed public evidence)

| Signal Name | Category | People / Lab | Evidence | Signal Strength | Possible Thesis | Investor Relevance | Next Step | Confidence |
|-------------|----------|--------------|----------|-----------------|-----------------|--------------------|-----------|------------|
| Unconventional AI | 14/02 | Naveen Rao; Michael Carbin (MIT); Sara Achour (Stanford); MeeLan Lee | $475M seed at $4.5B, a16z + Lightspeed, Lux, DCVC (Dec 2025); no product for ~2 yrs [CONFIRMED, TechCrunch/Bloomberg] | Very High | Analog-silicon AI computer | Very High (follow-on tranche up to $1B) | Track hiring (analog design, compilers), first technical disclosures | Confirmed |
| Ricursive Intelligence | 12 | Anna Goldie, Azalia Mirhoseini (AlphaChip) | $35M seed (Sequoia) + $300M Series A at $4B (Lightspeed), Jan 2026 [CONFIRMED] | Very High | AI that designs chips for AI | Very High | Watch first customer/tape-out disclosures; talent pulls from DeepMind/NVIDIA | Confirmed |
| Majestic Labs | 07/16 | Ofer Shacham, Sha Rabii, Masumi Reynders (ex-Google/Meta silicon) | Emerged Nov 2025 with ~$100M (Series A led by Bow Wave; Lux) [CONFIRMED total] | Very High | Memory-pooled rack-scale AI servers (ship 2027) | High | Monitor memory-supplier partnerships | Confirmed |
| Taalas | 02 | Ljubisa Bajic (ex-Tenstorrent) | Broke cover Feb 2026 with HC1 chip + $169M (~$219M total) [CONFIRMED, Reuters]; AMD-acquisition headline [UNCONFIRMED] | Very High | Model-hardwired inference silicon | High | Verify any M&A via AMD/Reuters | Confirmed |
| Callosum | 02/12 | Danyal Akarca, Jascha Achterberg | Emerged Feb 2026 (~$10.25M); $100M seed led by Atomico, w/ Plural, DCVC, UK Sovereign AI Fund (Aug 2026) [CONFIRMED] | Very High | Heterogeneous AI-compute orchestration | High | Track silicon-partner list (Cerebras, Rebellions) | Confirmed |
| Neurophos | 06/14 | Patrick Bowen, Andrew Traverso; Duke (D. R. Smith) | $110M Series A led by Gates Frontier (Jan 2026) [CONFIRMED]; pre-revenue, chip 2027–28 | Very High | Metasurface optical processing unit | High | Ask for measured-silicon (not simulated) data | Confirmed |
| ChipAgents | 12 | William Wang (UCSB, on leave) | $21M A (Oct 2025), $50M A1 (Feb 2026), $60M ext. (Jul 2026) [company-reported] | Very High | Agentic RTL design/verification | High | Verify customer claims (MediaTek, Micron) | Confirmed |
| Cognichip | 12 | Faraj Aalaei (ex-Aquantia) | Series A reported Apr 2026 (~$60M) [TO VERIFY] | High | "Physics-informed" AI chip-design model | Medium-High | Confirm round size/leads from company PR | To Verify |
| Normal Computing | 14 | Ex-Google Brain/X team | ~$50M raise reported Mar 2026 [TO VERIFY] | High | Thermodynamic / probabilistic AI silicon | Medium | Confirm round; track tape-out disclosures | To Verify |

### 2b. Pattern-level watch-items (no company asserted)

| Signal Name | Category | People / Lab | Evidence | Signal Strength | Possible Thesis | Investor Relevance | Next Step | Confidence |
|-------------|----------|--------------|----------|-----------------|-----------------|--------------------|-----------|------------|
| Exit-diaspora: Groq / Enfabrica / Celestial / Rivos alumni | 02/05/06/04 | Teams not absorbed by NVIDIA / Marvell / Meta after 2025 deals | Licensing + acqui-hire structures (NVIDIA–Enfabrica Sept 2025; NVIDIA–Groq Dec 2025; Marvell–Celestial Dec 2025; Meta–Rivos 2025) leave residual teams [deal terms TO VERIFY in categories 02/05/06/04] | Medium | Next inference / fabric / optical startups | High | Monitor public role changes to "Stealth" 6–24 months post-close | Weak Signal |
| Ex-Google TPU "stealth" role changes | 01/02 | Unnamed ex-TPU engineers (public profile aggregators, Jul 2026) | Single aggregator listing of TPU alumni moving to "Stealth" [UNCONFIRMED] | Low | LLM-specialized silicon (MatX-style) | High | Corroborate with Form D / domain / job postings before outreach | To Verify |
| AI-EDA second wave (analog layout, DFT, physical verification agents) | 12 | UT Austin (Pan), NYU (Garg), NVIDIA Research, DeepMind alumni | Category funded at scale in 2025–26 (Ricursive, ChipAgents); adjacent sub-problems unfunded | Medium | Vertical AI-EDA agents | High | Track DAC 2026 / ICCAD 2026 student authors and spinouts | Weak Signal |
| `[ILLUSTRATIVE]` PIM spinout watch | 07/14 | ETH Zürich (Mutlu group) | Repeated PIM papers in urgent bottleneck; prior industry collaborations | Weak Signal | Near-memory accelerator IP | High | Monitor patent assignees & role changes | To Verify |
| `[ILLUSTRATIVE]` Photonics fabric watch | 06 | Columbia (Bergman group) | Sustained CPO/photonic-fabric publications; ecosystem ties | Weak Signal | Optical interconnect fabric | High | Track grad/postdoc departures & domains | To Verify |
| `[ILLUSTRATIVE]` Analog in-memory cluster | 14 | Multiple (Princeton-style IMC) | EnCharge precedent + Unconventional AI seed shows capital appetite | Weak Signal | Analog tooling (compilers, calibration, test) | High | Map who is *not yet* funded | To Verify |

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
| 2025-11-10 | Majestic Labs | Emergence from stealth + Series A | Company PR; SiliconANGLE, DatacenterDynamics | Confirmed | ~$100M total; ex-Google/Meta silicon leads |
| 2025-12-08 | Unconventional AI | Seed round | TechCrunch; Bloomberg | Confirmed | $475M at $4.5B; first tranche of up to $1B |
| 2025 (H2) | Ricursive Intelligence | Seed round | Company PR | Confirmed | $35M led by Sequoia (~$750M valuation) |
| 2026-01 | Ricursive Intelligence | Series A | Company PR; Crunchbase News | Confirmed | $300M at $4B post, led by Lightspeed |
| 2026-01-22 | Neurophos | Series A | TechCrunch; optics.org; Duke Research | Confirmed | $110M led by Gates Frontier |
| 2026-02 | Callosum | Emergence from stealth + early round | UKTN / Sifted | Confirmed | ~$10.25M (reported as seed/pre-seed) |
| 2026-02-17 | ChipAgents | Series A1 | Business Wire (company PR) | Confirmed | $50M; total $74M |
| 2026-02-19 | Taalas | Emergence from stealth + round | Reuters; The Next Platform | Confirmed | $169M; HC1 chip unveiled |
| 2026-02-24 | MatX | Series B | SiliconANGLE; trade press | Confirmed | $500M led by Jane Street & Situational Awareness LP |
| 2026-03 | Normal Computing | Funding round | Trade press (per coordinator brief) | To Verify | ~$50M |
| 2026-04 | Cognichip | Series A | Trade press (per coordinator brief) | To Verify | ~$60M |
| 2026-07 | (unnamed) ex-Google TPU engineer(s) | Public profile → "Stealth" | Profile aggregator | Weak Signal | No company identified; do not act without corroboration |
| 2026-07-29 | ChipAgents | Series A extension | Company PR via aggregators | Likely | $60M; Series A total $134M (company-reported) |
| 2026-08-20 | Callosum | Seed round | tech.eu; Sifted; Bloomberg Government; Cooley | Confirmed | $100M led by Atomico; UK Sovereign AI Fund's first investment |

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
- Who are the "second-time founder" silicon people likely to start again? (2026 precedent: Ljubisa Bajic → Taalas; Naveen Rao → Unconventional AI.)
- Which Groq / Enfabrica / Celestial / Rivos team members did *not* join the acquirer/licensee after the 2025 deals?
- Are researcher-founder seed rounds now pricing out classic seed funds — and where are the sub-$20M lab spinouts still forming?

---

## Discovery Workflow (repeatable)

1. Pull new signals from allowed sources since last refresh.
2. Tag each with category, people/lab, evidence, strength, confidence.
3. Promote any entity with ≥2 independent High/Very-High signals to the active watchlist.
4. Draft a one-line thesis + outreach next step per promoted entity.
5. Append findings; cross-link to category files and researcher index.
6. Append [REFRESH_LOG.md](REFRESH_LOG.md).

---

## Refresh Notes

| Date | Refresh Type | Added | Updated | Archived | Key Changes | Sources |
|------|--------------|-------|---------|----------|-------------|---------|
| 2026-06-09 | Full (initial) | 4 (illustrative) | 0 | 0 | Method + illustrative schema | — |
| 2026-11-04 | Full (Refresh #3) | 12 watchlist rows (9 surfaced companies + 3 pattern watch-items) + 14 funding-signal rows | 3 illustrative rows retained/updated | 1 illustrative row (AI-EDA founder watch → superseded by confirmed AI-EDA formations) | Populated Recent Stealth Funding Signals; added exit-diaspora watch; mega-seed pattern | TechCrunch, Bloomberg, Reuters, company PRs, tech.eu, Sifted, SiliconANGLE, DatacenterDynamics, optics.org |
