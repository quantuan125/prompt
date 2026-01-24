---
artifact_type: 'REPORT'
initiative_id: 'T102'
epic_id: 'T102C'
version: '1.0.0'
date: '2025-09-26'
status: 'draft'
author: 'LLM_Research'
decision_owner_role: 'Client'
---

Here’s a crisp, standards-backed assessment and recommendation on whether (and how) to include **“Roadmap & Success Checkpoints”** in your SPS (PID-like) document for **T102C (Concept)**.

# Standards assessment (what industry practice says)

**1) PID / Charter norms (PRINCE2, PMI, ISO 21500)**

* **PRINCE2**: A PID **does** carry the *high-level* **Project Plan** (timeline + key milestones) so the Project Board can judge viability and monitor at stage boundaries. Detailed delivery plans live in separate **Stage Plans**. In other words: snapshot milestones in the PID; the operational schedule sits elsewhere. ([PRINCE2 Wiki][1])
* **PMI / PMBOK**: The **Project Charter** typically includes a **summary milestone schedule** (not a sprint-by-sprint plan). It authorizes the work and gives executives an at-a-glance time horizon; deeper planning is maintained in the project management plan and sub-plans. ([Project Management Institute][2])
* **ISO 21500**: Recognizes *charter* and *plans* as distinct artifacts; the standard is guidance-oriented and supports separating governance authorization from detailed planning. ([ISO][3])

**Implication:** Put a **concise, milestone-level roadmap** in SPS for governance; keep *operational plans* outside.

**2) Agile at scale (SAFe)**

* SAFe manages **roadmaps** at portfolio/program/product levels (Portfolio, Solution/Product, and **PI roadmaps**), and conducts **PI Planning** as a cadence event. Governance ( Lean Portfolio **guardrails**) is separate from the day-to-day delivery plan. ([scaledagileframework.com][4])

**Implication:** Treat your SPS as governance (policy/guardrails), and keep the **working roadmap** with the delivery system (ART/teams, Planner).

**3) Architecture/requirements standards (TOGAF, ISO/IEC/IEEE 42010, IEEE 1016, ISO/IEC/IEEE 29148)**

* **TOGAF**: The **Architecture Roadmap** and **Implementation & Migration Plan** are deliverables of **ADM Phase E/F**—they live in **architecture/program** planning artifacts, not governance charters. ([coe.qualiware.com][5])
* **42010 (architecture descriptions)** and **1016 (software design descriptions)** define content for architecture/design **views**, not project schedules. They reinforce keeping technical/architecture decisions in architecture/ADR-style artifacts. ([IEEE Standards Association][6])
* **29148 (requirements)** governs requirements content/quality; project planning is out of scope—another pointer to **not** blending schedules with requirements/governance content. ([ISO][7])

**Implication:** Keep **technical/architecture roadmaps** with Concept/Architecture artifacts, and only summarize governable milestones in SPS.

**4) Your operating model (internal)**

* Your SPS is explicitly positioned as **initiative/epic governance** (PID-like), with **Concept** as the ADR compendium and **Request** as the feature-level spec; governance decisions are GDRs, technical decisions are ADRs. 
* The Request template already states SPS **does not include success metrics/ACs**—those belong at feature/story scopes. 
* The model mandates **explicit inheritance** and **linking** (Inherited Considerations tables, decision precedence), favoring separation + traceable references.

**Bottom line:** Industry practice **supports a hybrid**: a concise, stable **governance snapshot** in SPS (milestones/phase exit signals), with the **working roadmap** and **detailed schedules** maintained externally (Planner / Concept / Stage Plans).

---

# Recommendation

**Choose Option C — Hybrid.**
Keep a **high-level “Roadmap & Success Checkpoints (Governance Snapshot)”** inside SPS; maintain **detailed epic plans** and **sprint/PI calendars** externally (Planner and Concept), referenced from SPS.

**Why this fits:**

* Aligns with PRINCE2/PMI (PID/Charter = milestone snapshot; detailed plans elsewhere). ([PRINCE2 Wiki][1])
* Mirrors SAFe’s separation of **governance guardrails** and **delivery roadmaps**. ([scaledagileframework.com][8])
* Preserves your internal rule: **SPS = governance; Concept/Design = ADR/implementation**. 

---

# What to include in SPS (and what to keep out)

**Include in SPS (governance snapshot; stable, concise):**

* **Phase names & intents** (e.g., Foundation → Template Design → Process Design → Integration).
* **Indicative duration bands** (e.g., 2–3w, 3–4w), **no dates**.
* **3–6 executive milestones** that unlock decisions/funding (e.g., “Concept ADR framework baselined”, “Template package validated with 1 real case”).
* **Governance-level “Success Checkpoints”** = **phase exit criteria** (readiness signals), *not* story ACs.
* **Trace links**: to Epic Plan, Concept ADR index, and Planner board.

**Keep out of SPS (externalize):**

* Sprint calendars, team capacity, WBS breakdown, dependency nets, burn charts, acceptance tests, and rolling rescheduling (Planner, Stage Plans, Concept ADRs). ([coe.qualiware.com][5])

---

# Structure optimization (drop-in block for SPS §Epic dossier)

Use this exact block label to signal scope and avoid drift:

```markdown
### Roadmap & Success Checkpoints *(Governance Snapshot)*

**Scope & Ownership**
- Owner: Epic Lead (LLM_Consultant); Decision Owner: Client
- This section is a **milestone-level snapshot** for governance. Detailed plans live in **Epic Plan (Planner)** and **Concept ADR index**.

**Phase Sequence (indicative, no dates)**
| Phase | Intent (1 line) | Key Governance Milestone | Duration Band |
|---|---|---|---|
| 1. Foundation | Confirm epic scope + research integration | E-GDR: Roadmap Baseline approved | 2–3w |
| 2. Template Design (CST) | Produce working concept template | CST v1 validated on 1 real case | 3–4w |
| 3. Process Design (CPG) | Authoring workflow defined | CPG v1 walkthrough approved | 2–3w |
| 4. Integration (MANIFEST) | Package + integration test | Package passes integration checklist | 1–2w |

**Success Checkpoints (phase exits)**
- **Readiness**: Artifact completeness & reviews done (evidence: links).  
- **Integration**: Cross-workflow links verified (SPS → Request → Concept).  
- **Usability**: Non-technical user walkthrough signed off.  
- **Reusability**: Assets pass template re-use criteria.  

**References**
- Epic Plan (Planner): `<link or repo-relative ref>`  
- Concept ADR Index: `<repo-relative anchor>`  
- Inherited Considerations: see §III-B and §III-C tables
```

This keeps SPS **executive-readable** and **low-churn**, while ensuring **traceability** into the living plan—exactly how PRINCE2/PMI/SAFe intend such documents to work. ([PRINCE2 Wiki][1])

---

# If you prefer to extract wholly (Option B)

Create an **“Epic Plan”** artifact (or Planner space) with:

* WBS, dependency map, resourcing, sprints/PI schedule, risked timeline.
* **Change control**: baseline IDs and effective dates; SPS links to the current baseline only.
* Concept holds the **Architecture Roadmap** (Phase E/F outputs), linking work packages to ADRs. ([coe.qualiware.com][5])

---

# Traceability & oversight (best-practice patterns)

* **GDR baseline**: Record “Roadmap Baseline” as an **Epic-level GDR** entry (E-GDR) with **Effective** date; SPS links to the current baseline row in your GDR index. 
* **Inherited Considerations**: Reference governance rules (QG/CON/DEP/IG) via the **Inherited Considerations** table; avoid restating text (delta-only + explicit IDs). 
* **Concept ADRs**: Map major milestones to **Concept ADR** anchors (architecture changes/decisions) rather than embedding technical detail in SPS. 

---

# Review of your proposed tables (tune-ups)

Your “Proposed: Roadmap & Success Checkpoints” is **appropriate** for SPS if you:

1. **Retitle** to “*(Governance Snapshot)*” and **keep durations as bands** (no calendar).
2. **Express “Success Checkpoints” as exit criteria** (governance signals), not ACs. Your bullets already align; keep them concise and evidence-linked.
3. **Add explicit references** to **Epic Plan** and **Concept ADR index** (repo-relative anchors).
4. **Add a Baseline row in the Epic GDR Index** (E-GDR: “Roadmap Baseline vN”).

**Maintainability:** Expect **phase/milestone edits only at gates**; day-to-day drift stays external. That cadence matches governance stability expectations. ([PRINCE2 Wiki][1])

---

# Implementation guidance for T102C

1. **SPS (§Epic dossier):** Insert the **Governance Snapshot** block above (label & table exactly).
2. **E-GDR entry:** Create **`T102C-GDR-00X — Roadmap Baseline v1`** with Context → Decision → Consequences → References; populate **Effective** date; link to Epic Plan + Concept ADR index. 
3. **Epic Plan (external):** Host the working plan in Planner (or `T102C-EPIC-PLAN.md`) with WBS, dependencies, resourcing, sprints/PI, and change log.
4. **Concept ADR index:** Add “Architecture Roadmap” section that ties work packages to ADRs; keep it synchronized at PI boundaries. ([coe.qualiware.com][5])
5. **Validation rules:**

   * SPS contains **no acceptance tests**; those belong to Request/Story. 
   * **Inherited Considerations** table present and ID-only (no restatements). 
   * **Links resolve** (SPS ↔ Epic Plan ↔ Concept ADRs).
6. **Change policy:** Minor wording/scope clarifications may update SPS; any schedule/sequence change becomes a **new Roadmap Baseline (E-GDR)** and Planner update.

---

# Decision summary

* **Appropriateness:** Yes—**at milestone level** inside SPS. Detailed roadmaps belong in Planner/Concept. ([PRINCE2 Wiki][1])
* **Conciseness:** The proposed table is right-sized; keep it to **one screen**.
* **Maintainability:** Update only at **gates/baselines**; all rolling changes live outside SPS.

---

## Citations (key sources)

* PRINCE2 PID scope & role of plans. ([PRINCE2 Wiki][1])
* PMI Charter content (summary milestones). ([Project Management Institute][2])
* ISO 21500 (charter/plans separation concept). ([ISO][3])
* SAFe roadmap types, PI Planning, and governance guardrails. ([scaledagileframework.com][4])
* TOGAF Phase E/F (Architecture Roadmap, Implementation & Migration Plan). ([coe.qualiware.com][5])
* Architecture & design standards scope (42010, 1016); requirements scope (29148). ([IEEE Standards Association][6])
* Your internal governance separation & inheritance model.

---

## Next actions (quick checklist)

* [ ] Add the **Governance Snapshot** block to SPS §T102C Epic dossier.
* [ ] Create **E-GDR “Roadmap Baseline v1”** with Effective date + anchors.
* [ ] Stand up **Epic Plan** (Planner / `T102C-EPIC-PLAN.md`); link from SPS.
* [ ] Ensure **Concept ADR index** exposes the Architecture Roadmap linkage.
* [ ] Add validator checks (presence, anchors, link resolution).

---

## To confirm (high-level questions)

1. Which tool will host the **Epic Plan** (Planner board vs. repo doc)?
2. Do you want **one** Roadmap Baseline per Epic (recommended) or per Feature within the Epic?
3. What **gate cadence** should trigger SPS roadmap updates (e.g., end of each stage/PI vs. only when baselines change)?
4. Should we add a **standard “Evidence” column** to the Success Checkpoints table (links to reviews, walkthroughs, or test runs)?

[1]: https://prince2.wiki/management-products/baselines/project-initiation-documentation/?utm_source=chatgpt.com "Project initiation documentation"
[2]: https://www.pmi.org/learning/library/charter-selling-project-7473?utm_source=chatgpt.com "The Charter - Selling your Project - PMI"
[3]: https://www.iso.org/standard/50003.html?utm_source=chatgpt.com "ISO 21500:2012 - Guidance on project management"
[4]: https://scaledagileframework.com/roadmap/?utm_source=chatgpt.com "Roadmap"
[5]: https://coe.qualiware.com/resources/togaf/9-1/part2-adm/phase-f-migration-planning/?utm_source=chatgpt.com "Phase F: Migration Planning | QualiWare Center of Excellence"
[6]: https://standards.ieee.org/ieee/42010/6846/?utm_source=chatgpt.com "IEEE/ISO/IEC 42010-2022"
[7]: https://www.iso.org/standard/72089.html?utm_source=chatgpt.com "ISO/IEC/IEEE 29148:2018 - Requirements engineering"
[8]: https://scaledagileframework.com/guardrails/?utm_source=chatgpt.com "Lean Budget Guardrails"

