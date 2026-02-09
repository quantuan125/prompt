## Research brief — Evaluate the Feature-scoped **Request** vs. updated SPS/Concept operating model

### Executive summary (signals & priority fixes)

* **Fail — Role alignment.** The current **Request** embeds a “**Part 0 — SAD-lite**” (options, scoring matrix, C4 views) which belongs in **Concept**, not Request. Per the operating model, **Request = BRD/SRS only** with no decision bodies; link to Concept ADRs instead. **Priority fix #1:** move “Part 0” content to Concept and keep links only in Request.  
* **Fail — Header conformance.** Header uses legacy keys (`task_id`, `prefix_id`, `parent_task`, etc.), misses **`initiative_id/epic_id/feature_id`**, has enum drift (`status: ready_for_review`) and author token drift (`LLM Consultant` vs `LLM_Consultant`). **Priority fix #2:** adopt the **Canonical YAML Header** exactly and note it’s mandated by **GDR-002**.   
* **Pass (with polish) — Inheritance table.** An “Inherited Considerations” table exists and follows the right idea; tighten to the **exact columns/≤5 IDs rule** and correct the **“Inheritences”** spelling.  
* **Mixed — GDR/ADR referencing.** The Request references standards informally; it should cite **policy via GDRs** and **implementation via ADRs** with **repo-relative anchors** per the Decision Records Index pattern. **Priority fix #3:** convert inline mentions to compliant links. 
* **Mixed — ID hygiene.** Many FID-scoped IDs are good (e.g., `T102A-SPSST-NFR-##`), but **Issues/Risks** use unscoped IDs (`ISSUE-01`, `RISK-01`) and there’s a legacy checklist example (`SPS-T102-001`). Normalize per **ID spec**.  
* **Planner-readiness gaps.** Lacks a **single, consolidated Gherkin AC register per Story** and has solution content that should be downstream. Make it **R2-ready** by (a) removing solution bodies, (b) finalizing ACs/IF contracts, and (c) fixing header/IDs/links.  

---

### Findings by theme

#### 1) Role alignment (Request = BRD/SRS; no decision bodies)

* Operating model: **SPS = governance; Request = requirements only (BRD→SRS) with story-level AC; Concept = ADR compendium (options, matrices, C4)**. The current Request’s **“Part 0 — SAD-lite”** (options, criteria, matrices, C4) violates this, and should live in **Concept** with links from Request.  

#### 2) GDR/ADR referencing discipline

* **Required**: cite **policy via GDRs** (SPS holds Initiative GDR Index) and **implementation via ADRs** (Concept holds ADR indices), using **repo-relative anchors** per the **Decision Records Index** standard. The Request currently uses informal references; convert to anchors that match the ADR/GDR index patterns.  

#### 3) Header conformance (no duplication; adopt the canonical header)

* Per **ADR-002** (adopted by **GDR-002**), headers must include:
  `artifact_type, initiative_id, (epic_id), (feature_id), (story_id), version, date, status, author, decision_owner_role, (dependencies)` with strict enums/regex. The current header **omits** `initiative_id/epic_id/feature_id`, uses **extra legacy keys**, and an invalid **status** value, and **author** token drift. Remove local spec restatements; **link** to ADR-002/GDR-002 instead.   

#### 4) Explicit Inheritance tables

* ADR-003 requires the **exact columns** and **≤5 critical IDs**; the Request’s “Inherited Considerations” largely fits but must **correct the section title spelling** and ensure **ID-only tokens** (no prose duplication). Categories used (Constraints, Dependencies, Quality Goals) are acceptable per ADR-003.  

#### 5) ID hygiene & scope

* Good: FID-scoped FR/NFR/IF/INT tokens (e.g., `T102A-SPSST-NFR-04`, `…-IF-01`, `…-INT-##`).
* Gaps: **Issues/Risks** should be `T102A-SPSST-ISSUE-##` / `…-RISK-##` (not `ISSUE-01`); checklist example uses legacy `SPS-T102-001`. Align all IDs and anchors to **ADR-005** (scope regex, categories, anchor stability).  

#### 6) Section-by-section gaps (III.A → III.J)

* **Move to Concept**: Decision criteria & weights, options table, objective matrix, C4 context/container views, solution recommendation, and any **Feature ADR index/body** content. Keep **links only** in Request.  
* **Keep in Request**: Business view (scope, objectives), SRS (FR/NFR/IF), Story specs & **Gherkin AC** per story, traceability. 

---

### Redlines queue (concrete minimal edits)

1. **Replace header with canonical keys/enums** (and delete legacy keys):

   ```yaml
   artifact_type: 'REQUEST'
   initiative_id: 'T102'
   epic_id: 'T102A'
   feature_id: 'T102A-SPSST'
   version: '1.0.1'        # bump
   date: '2025-09-23'
   status: 'review'         # ∈ {draft, review, approved, rework, deprecated}
   author: 'LLM_Consultant' # enum token
   decision_owner_role: 'Client'
   dependencies:
     - '../sps/sps_T102-CONSULTANT.md'
     - '../request/request_structural_template.md'
   ```

   Add a short line in **References**: “**Header spec:** see `T102-STD-002` (adopted by `T102-GDR-002`).”  
2. **Remove “Part 0 — SAD-lite” from Request** and paste it (unaltered) into the **Concept** for this feature; in Request, keep a “**Concept References**” subsection with repo-relative anchors to the Concept ADR sections.  
3. **Fix the “Inherited Considerations” block**

   * Rename heading to **Inherited Considerations** (spelling).
   * Keep **≤5 IDs** per row; ensure tokens are **`ID (Title)`** only with repo-relative anchors. 
4. **Normalize IDs** per **ADR-005**

   * Convert `ISSUE-01`/`RISK-01` → `T102A-SPSST-ISSUE-01` / `T102A-SPSST-RISK-01`.
   * Replace any legacy examples like `SPS-T102-001` with proper FID/SID forms.  
5. **Add a consolidated “Acceptance Criteria Register”** (one table) with **Gherkin** scenarios per **Story** in §J; cross-link each to FR/NFR/IF items and keep it human-first but testable. 
6. **Convert informal mentions to compliant anchors**

   * Where you mention headers/IDs/DRs, add anchors to **`T102-STD-002`**, **`T102-STD-004`**, **`T102-STD-005`** and to **SPS GDRs** in the Initiative GDR Index.  

---

### Planner-readiness: residual risks & mitigations

| Risk (blocks R2?)                                | Why it matters                                                                     | Mitigation to unblock                                                                |
| ------------------------------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Role inversion** (solution content in Request) | Planner expects **requirements-only** baseline; solution bodies here create churn. | **Move Part 0** to Concept; keep links only.                                         |
| **Header drift**                                 | Automation/traceability depends on exact keys/enums.                               | Adopt **ADR-002** header; reference **GDR-002** as policy; update enums/tokens.      |
| **ID inconsistencies**                           | Breaks cross-artifact traceability and validation.                                 | Normalize to **ADR-005** (scope regex, categories); fix Issues/Risks/checklist IDs.  |
| **Weak ACs**                                     | Without Gherkin AC per story, Planner can’t plan tests or estimate.                | Add **AC Register** with Gherkin per story; link to FR/NFR/IF items.                 |
| **Reference style**                              | Free-text references impede navigation & audits.                                   | Adopt **ADR-004** link style with repo-relative anchors for all DR mentions.         |

---

### Quick compliance map (what each standard enforces)

* **`T102-STD-001` (Operating Model):** Request = **BRD/SRS only**; Concept = **ADR/solution** (options, matrices, C4). 
* **`T102-GDR-002` + `T102-STD-002` (Header):** One canonical header; **no local restatements**; strict enums/regex.  
* **`T102-STD-003` (Inheritance):** Exact columns; **≤5** IDs; **ID-only** references (no prose duplication). 
* **`T102-STD-004` (DR Index):** One schema/body pattern; **repo-relative anchors**; GDR≠ADR separation. 
* **`T102-STD-005` (ID Spec):** Scope regex (IID/EID/FID/SID); category tokens (FR/NFR/IF/INT…); anchor stability. 

---

## Next actions (minimal, in order)

1. **Strip & paste:** Move Request §III.A.2–§III.A.7 (options/matrices/C4/recommendation) into the **Concept**; leave stubs + links in Request.  
2. **Header swap:** Replace header with the **canonical YAML**; remove legacy keys; correct enums/tokens. 
3. **IDs & ACs:** Normalize all IDs; add **one AC Register** with **Gherkin** per Story under §J; cross-link to FR/NFR/IF. 
4. **Anchors pass:** Convert all DR mentions to **repo-relative anchors** per ADR-004; add an **“References”** subsection listing governing **GDRs/ADRs**. 

---

### Clarifying questions (to finalize R2-ready)

1. Should we **lift the entire options/matrix/C4 set** verbatim into the **Concept** now, or do you want us to **re-score** once the Request is cleaned?
2. Do you prefer the **AC Register** to live at the **end of §J** (single table) or **inline under each Story** (then mirrored in a summary table)?
3. Confirm the canonical **repo-relative anchor scheme** you want us to use (folder depth & naming), or should we follow the examples in the current **SPS/Concept** as the source of truth?  
