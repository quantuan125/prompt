Here’s a compact, decision-ready research brief that (a) surveys industry practice, (b) answers the specific questions in your scope, and (c) proposes a high-level structure for the **Concept** artifact that fits T102’s operating model and current constraints.

# RESEARCH BRIEF — Consultancy Handoff Authority & Readiness Aggregation (T102C)

## I. Executive summary

**Bottom line.** Adopt a **hybrid handoff**: make **Concept** the **single authoritative locus for the handoff snapshot** (SoT for *handoff*) while **referencing**—not duplicating—SPS governance and Request requirements. Use a **lean, manual “Readiness Snapshot”** (traffic-light + short checklists) that **rolls up Definition-of-Ready (DoR) states** from Initiative→Epic→Feature without new tooling. This aligns with your accepted operating model (Concept = dynamic ADR workspace; Request = requirements-only) and with industry patterns (single SoT handoff packages; DoR/entry-exit criteria via Kanban; ADR log as canonical decision memory).  ([Scaled Agile Framework][1]) ([GitHub][2])

**Why this works now (v1).** It satisfies **T102C-GDR-001/004** (boundaries; decision canonicalization) and your **low-disruption** constraint by keeping automation out of scope while ensuring unambiguous handoff authority for the LLM_Planner.

---

## II. Findings mapped to your questions

### A) Handoff authority patterns (centralized vs distributed)

**What industry does.**

* **Single SoT handoff packages** are favored to reduce drift and rework; the “single source of truth” pattern shows up across product/ops and consulting handoffs. ([Atlassian][3])
* **ADR compendiums** centralize decisions with light indices and link-outs; good practice is one decision per ADR, with a project-level log as the canonical ledger. ([Architectural Decision Records][4])
* **DoR/DoD & Kanban entry/exit** provide objective gates before downstream pull—widely used in SAFe at Portfolio/ART/Team levels. These serve as “readiness contracts” feeding any SoT handoff. ([Scaled Agile Framework][1])

**Centralized vs distributed—observed outcomes.**

* **Centralized:** clear accountability, easier audit, lower cognitive load for receivers; risk is local bloat unless you “link-don’t-duplicate.” ([Atlassian][3])
* **Distributed:** closer to sources but higher drift/latency and unclear authority in multi-artifact environments. Management literature warns RACI-only matrices often underperform unless decision rights and “who says go” are explicit. ([McKinsey & Company][5])

**Implication for T102.** Your own GDRs already place **decisions in Concept** and **requirements in Request**; making **Concept the authoritative handoff snapshot** is the least-surprise extension of that model.

---

### B) Version sync & completeness verification

**Industry anchors.**

* **42010**: organize architectural information by **stakeholder viewpoints** and **correspondence rules**, which favors a single, coherent handoff description with traceability to underlying views. ([iso-architecture.org][6])
* **29148**: quality requirements must be **necessary, clear, verifiable, unambiguous**—supporting a Request-owned SRS that Concept links to, not edits. ([63069562][7])
* **SAFe Kanban**: enforce **entry/exit criteria** (DoR/DoD) as checks; these are lightweight to roll-up. ([Scaled Agile Framework][8])

**Recommended checks for handoff completeness (v1).**

* **Decision state:** all **relevant ADRs = Accepted** in Concept (indexable). ([GitHub][2])
* **Requirements state:** **Feature FRs** approved in Request and traced to ADRs (ID cross-refs). ([ISO][9])
* **Risk & constraints:** linked from SPS/Request; no duplication in Concept. 
* **Sign-off:** explicit Client approval signal per your header/approval rules. 

---

### C) Lean readiness aggregation (Initiative→Epic→Feature)

**Patterns in practice.**

* **Kanban states + DoR** roll-ups are the simplest multi-tier aggregation (Portfolio/Program/Team). ([Scaled Agile Framework][1])
* **Visual orchestration (Obeya)** reduces cognitive load by surfacing only salient signals. Combine with limited, periodic snapshots (weekly) vs. live dashboards in v1. ([framework.scaledagile.com][10])
* **Cognitive-load framing (Team Topologies)** argues for minimal signal density to avoid overload for decision-makers. ([IT Revolution][11])

**Implication for T102.** A **manual YAML “Readiness Snapshot”** that summarizes per-tier **state + blockers + next gate** matches your **low-disruption** goal and your Governance Snapshot standard (plans live in external PM tool).

---

### D) Integration & authority models

* Use **RACI cautiously**; pair it with **explicit decision rights** (who is *Accountable* to “say go” at handoff). McKinsey highlights RACI pitfalls without clear decision loci. ([McKinsey & Company][5])
* Your accepted **Operating Model** already sets **Client = Decision Owner**, **LLM_Consultant = author**, **LLM_Planner = consumer**—keep that chain in the handoff snapshot. 

---

## III. Recommendations for T102C GDRs

### T102C-GDR-003 — **Handoff Authority Standard (decision text draft)**

**Decision.** **Concept** SHALL be the **authoritative source for the Handoff Snapshot** to LLM_Planner. The snapshot is a **single section** in Concept that:

1. **Assembles**: links to approved SPS, Request, and Design items;
2. **Proves**: readiness via minimal **DoR-based checklist** and **sign-off**;
3. **Stamps**: version IDs (doc versions + commit SHAs) for **immutability**.

**Rationale.** Aligns with 42010’s coherent description, ADR best practices, and SAFe’s gate-ready pull pattern while respecting T102’s boundaries (Request = requirements; Concept = decisions). ([ISO][12]) 

**Consequences.**

* (+) Single accountable locus for handoff; reduced drift/cognitive load.
* (±) Requires discipline to “link-don’t-duplicate.”
* (–) Adds a small editorial step to maintain the snapshot before each handoff. 

---

### T102C-GDR-005 — **Readiness Aggregation Standard (decision text draft)**

**Decision.** T102C SHALL maintain a **manual YAML Readiness Snapshot** that **rolls up** Initiative/Epic/Feature states using **DoR-derived entry criteria**, with **traffic-light status** and **dated notes**; **no automation** in v1. Aggregation rules:

* **State** ∈ {Funnel, Analyzing, Backlog, Implementing, Done} with **Ready** marker when **DoR ≥ 80%** (checklist, not metrics).
* **Roll-up**: An Epic is **Ready** when **all included Features are Ready** OR **Client grants override** with named risks.
* **Display**: compact table + “Top 3 blockers” list; deeper detail remains in Request/Design & external PM tool. ([Scaled Agile Framework][1]) 

**Consequences.**

* (+) Lean, human-first visibility; mirrors SAFe’s widely-understood flow; easy to adopt.
* (±) Manual upkeep; plan weekly cadence.
* (–) Not a live dashboard; v2 may add automation.

---

## IV. High-level structure for the **Concept** artifact (v1)

> Focus: keep Concept as **dynamic ADR workspace** + **authoritative handoff snapshot** with **lean readiness**—no duplication of SPS/Request content. 

```markdown
---
artifact_type: 'CONCEPT'
initiative_id: 'T102'
version: '1.x.y'
status: '<draft|review|accepted>'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# concept_T102 — Architecture & Decisions Compendium

## I. Identity & Operating Rules
- Canonical header + links to governing GDRs/ADRs (inheritance table: “link-don’t-duplicate”).  <!-- T102-GDR-002/003/004/005 -->
## II. Executive Context
- Scope & boundaries (what lives in SPS vs Request vs Design); change log.

## III. Decision System (ADR Compendium)
- **A. Initiative ADR Index** (canonical table; status, anchor)
- **B. Epic ADR Index**
- **C. Feature ADR Index**
  - *Body sections for each ADR follow ADR-004 schema.*  <!-- one decision per ADR -->

## IV. Readiness Snapshot (Lean, manual)
- **A. Roll-up Table** (Initiative/Epics/Features: State | Ready? | Top blockers | Next gate | Updated_at)
- **B. DoR Checklists (brief)** per tier (links to Request/Design for evidence)
- **C. Notes & Overrides** (Client approvals recorded with ID)

## V. Handoff Snapshot (Authoritative)
- **A. Package Manifest** (immutable IDs, doc versions/SHAs)
- **B. Acceptance Signals** (Client sign-off, gate approvals)
- **C. Completeness Checklist** (ADR accepted; FRs approved; risks linked)
- **D. Links** (SPS/Request/Design anchors; no copy-paste)

## VI. Registers (optional, link-heavy)
- Risks/Assumptions/Dependencies registers (pointer-based; no duplication)

## VII. Integration & Interfaces
- Planner consumption notes (schema, payload outline), cross-traceability rules.

## VIII. Governance
- Local GDRs for Concept (e.g., T102C-GDR-003/005 once accepted) + change control.
```

This skeleton is consistent with your **GDR indices**, **inheritance**, **canonical header**, and **“governance snapshot in SPS; plans external”** posture.

---

## V. Implementation blueprint (v1 → v1.1)

**Phase 1 (now):**

1. Add **Section IV (Readiness Snapshot)** + **Section V (Handoff Snapshot)** to Concept using the template above.
2. Wire indexes to your existing ADR/GDR anchors; ensure Request remains SRS-only. 

**Phase 2 (after 1–2 handoffs):**
3) Introduce **lightweight validation** (checklist completeness, accepted ADR statuses).
4) Consider an **Obeya-style view** (single page) to visualize the snapshot for Client/Planner reviews. ([framework.scaledagile.com][10])

---

## VI. Risks & mitigations

* **Risk:** Snapshot drift if authors duplicate content. **Mitigation:** enforce “link-don’t-duplicate” rule from GDR-001/004; brief DoR checklists only. 
* **Risk:** Signal overload. **Mitigation:** Obeya-style minimalism; traffic-light plus top 3 blockers only. ([IT Revolution][11])

---

## VII. Validation criteria (post-adoption)

* **Lead time to “Planner-ready”** ↓  by ≥30% across two handoffs.
* **Rework due to missing context** ↓  (count of Planner clarification cycles).
* **Trace coverage**: 100% FR ↔ ADR links for included Features.

---

## Key internal alignment (T102)

* Your **GDR index** shows the pending nature of **T102C-GDR-003/005** and the accepted boundaries/precedence we rely on here. 
* SPS “Epics & Breakdown” is your dossier layer and Request remains the WBS dictionary—this proposal preserves that contract.

---

## Sources (select)

* **SAFe:** Portfolio/ART Kanban, DoR/entry-exit & states; Planning Interval. ([Scaled Agile Framework][1])
* **ISO/IEC/IEEE 42010** (architecture description & viewpoints). ([iso-architecture.org][6])
* **ISO/IEC/IEEE 29148** (requirements quality). ([63069562][7])
* **ADRs:** Cognitect; ADR GitHub; TechTarget best practices. ([Cognitect.com][13])
* **Cognitive load & visual orchestration:** Team Topologies; SAFe + Obeya. ([IT Revolution][11])

---

## Clarifying questions (to finalize GDR text and the CST update)

1. **Authority scope:** Do you want **Concept’s Handoff Snapshot** to be the *only* authoritative go-signal to LLM_Planner (i.e., Planner consumes **only** what’s linked there)?
2. **Snapshot cadence:** Should the **Readiness Snapshot** be updated **weekly** or **at each gate** (R0/R1/R2 equivalents) for v1?
3. **DoR threshold:** Is **“Ready ≥ 80% of DoR checks”** acceptable, with **Client override** allowed (logged in Snapshot)?
4. **Evidence granularity:** For readiness evidence, do you prefer **counts only** (e.g., “6/7 checks met”) or **named checks** surfaced in Concept (kept to ≤7 items per tier)?
5. **Planner schema:** Do we freeze a **minimal JSON/YAML manifest** schema now (IDs, versions/SHAs, links) or leave schema details to T102D (Design) and only document expectations in Concept?

[1]: https://scaledagileframework.com/portfolio-backlog/?utm_source=chatgpt.com "Portfolio Backlog"
[2]: https://github.com/joelparkerhenderson/architecture-decision-record?utm_source=chatgpt.com "Architecture decision record (ADR) examples for software ..."
[3]: https://www.atlassian.com/work-management/knowledge-sharing/documentation/building-a-single-source-of-truth-ssot-for-your-team?utm_source=chatgpt.com "Building a true Single Source of Truth (SSoT) for your team"
[4]: https://adr.github.io/?utm_source=chatgpt.com "Architectural Decision Records (ADRs) | Architectural ..."
[5]: https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-organization-blog/the-limits-of-raci-and-a-better-way-to-make-decisions?utm_source=chatgpt.com "The limits of RACI—and a better way to make decisions"
[6]: https://www.iso-architecture.org/42010/cm/?utm_source=chatgpt.com "ISO/IEC/IEEE 42010: Conceptual Model"
[7]: https://drkasbokar.com/wp-content/uploads/2024/09/29148-2018-ISOIECIEEE.pdf?utm_source=chatgpt.com "[PDF] international standard iso/iec/ ieee 29148"
[8]: https://scaledagileframework.com/planning-interval/?utm_source=chatgpt.com "Planning Interval (PI)"
[9]: https://www.iso.org/standard/72089.html?utm_source=chatgpt.com "ISO/IEC/IEEE 29148:2018 - Systems and software engineering"
[10]: https://framework.scaledagile.com/safe-and-obeya-a-game-changer-for-strategy-execution?utm_source=chatgpt.com "SAFe and Obeya: A Game Changer for Strategy Execution"
[11]: https://itrevolution.com/articles/team-cognitive-load-the-hidden-crisis-in-modern-tech-organizations/?utm_source=chatgpt.com "Team Cognitive Load: The Hidden Crisis in Modern Tech ..."
[12]: https://www.iso.org/obp/ui/?utm_source=chatgpt.com "ISO/IEC/IEEE 42010:2022(en), Software, systems and ..."
[13]: https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions?utm_source=chatgpt.com "Documenting Architecture Decisions - Cognitect.com"
