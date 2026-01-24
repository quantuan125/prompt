---
eID: 'T102'
epic_id: 'T102A'
feature_id: 'T102A-SPSST'
story_id: 'T102A-SPSST-S3'
story_status: 'review'        # draft|review|approved|rework|deprecated
stability: 'soft_lock'              # soft_lock|frozen
ready_to_plan: true
scg: 'B'                        # A=Authoring skeleton, B=Governance & Ops
---

# design_T102A-SPSST-S3 — Epics & Breakdown 

> **Status:** Living design log (non‑final). Finalized decisions are recorded in the **Concept** artifact.
> **Scope:** Story `T102A‑SPSST‑S3`.
> **Dates covered:** 24/08/2025 → 27/08/2025.

---
## III. CORE CONTENT

### A. Context & Intent

S3 defines the structure and authoring rules for section **Epics & Breakdown** in the SPS. The goal is to transform a narrative‑heavy section into a **standards‑aligned WBS** that positions the **SPS as the Project Initiation Document (PID)**, clarifies Initiative→Epic→Feature inheritance, and provides a clean handoff to the **Request** workflow (WBS dictionary). This design log captures options explored, the chosen architecture, QA decisions, and dated entries.

**References**

* **SPS:** `sps_T102-CONSULTANT.md` (current `T102A-SPSST-S3` implementation for `T102A`)
* **Request:** `request_T102A-SPSST_T102_v1.0.0.md` (S3 FRs/NFRs/Interfaces/Constraints updates)
* **Index (historic):** `request_T102A-INDEX_T102_v.1.0.0_i1.md` (superseded governance approach)
* **Design Exemplar:** `design_T102A-SPSST-S4.md` (structure and style)

**Consultation & Development Summary (must‑carry outcomes)**

<!-- Purpose: Persistent roll‑up of key decisions/principles from all consultations that materially shape S3. Append here to maintain a single must‑carry summary across sessions. Detailed per‑session notes live in Section C (Decision Log Entries). --> 

**Maintenance note:** Append new bullets here after each consultation; do not duplicate upstream SPS/Request logs. Link back to the relevant Decision Log Entry IDs.

* **SPS is the PID.** Governance from the deprecated Epic Index is absorbed into SPS.
* **Formal hierarchy:** Initiative Considerations (`T102A-SPSST-S4`) → Epic & Breakdowns (`T102A-SPSST-S3`) → Feature (`T102B` - Request). Downstream artifacts inherit and specify **delta‑only** where needed.
* **Process vs Structure:** Detailed *how‑to* guidance will move to **SPSPG**; SPS keeps high‑level instructional comments.
* **Data format:** Minimal **Epic YAML header** for machine‑readable identity; descriptive content in Markdown subsections.
* **Terminology:** Replace **Ripple Notes** with **Epic Changelog** for consistency.
* **Individual Epic approvals** enabled; Feature handoff remains Request‑owned.
* **Principle of Inheritance (proposed):** Downstream Request/Concept artifacts inherit from SPS initiative/Epics; downstream artifacts should specify only deltas. Status: proposed — not finalized; ADR to be raised in Concept.

**Session Index (consultations affecting S3)**

| Entry | Date Range    | Focus                                  | Outcome Summary |
| :---: | :------------ | :------------------------------------- | :-------------- |
| 1     | 24/08/2025    | Baseline capture & Index approach      | Baseline recorded (P1) & test adoption with External Index approach (P2) |
| 2     | 26/08/2025    | Epic dossier, terminology, inheritance | P3 adopted; inheritance proposed; SPSPG dependency captured |
| 3     | 11/09/2025    | ADR Formalization & GDR Index          | Finalized ADR standard; added GDR Index              |

---

### B. Architecture Proposals & Evolution

#### 0. Comparative Snapshot (P1 vs P2 vs P3)

| Aspect                | P1 (Baseline)         | P2 (Index‑first)         | P3 (Dossier)                 |
| --------------------- | --------------------- | ------------------------ | ---------------------------- |
| Source of truth       | Mixed in SPS          | Split (SPS + Index)      | Unified in SPS               |
| Visibility of scope   | Low (collapsed lists) | Medium (central index)   | High (visible registers)     |
| Drift risk            | Medium                | High                     | Low                          |
| Automation readiness  | Low                   | Medium                   | Medium‑High (YAML + tables)  |
| Author usability      | Medium                | Low‑Medium               | High                         |

#### 1. P1 — Original SPS `T102A-SPSST-S3` structure (baseline)

**Description**

```markdown
### B. Key Features & Requirements

#### 1. `[TASK_ID][A]` Feature: *[High-Level Title, e.g., "User Account System Overhaul"]*
*   [ ] This feature is ready for review.
*   **type:** `[new/existing/general]`

**Purpose:** *[1-3 sentences explaining the "why" behind this feature.]*

**Context & Research Notes:**
<details><summary>Click to expand notes...</summary>

*   **`NOTE TITLE`**:

</details>

**Stories Breakdown (Optional):**
<details><summary>Click to expand Stories for this Feature...</summary>

> **Story Block `[TASK_ID][A]-[ABB_NAME]`**
> *   **Name:** `[ABB_NAME]` - *[Story Name]*
> *   **Description:** *[1 sentence description of the story.]*
> *   **Rationale:** *[1 sentence why is this story necessary for the feature?]*
> *   **Context:** *[Any other relevant notes or dependencies.]*

</details>
```

**Pros**

* Simple, familiar narrative; low initial authoring friction.
* Embedded rationale (Context & Research) helps newcomers.

**Cons & Gaps**

* Features hidden inside `<details>` → **low visibility** of scope.
* Initiative governance mixed into Epic section → **scope conflation**.
* No machine‑readable Epic identity; not automation‑ready even at a minimal level.
* Missing consistent subsections for Goals, Dependencies/Interfaces, Issues/Risks, and Changelog; weak traceability to Request.

**Decision Status:** Baseline only (historical); not selected.

**Disposition:** Retained as historical context only.

---

#### 2. P2 — External index Governance (intermediate)

**Description**

```markdown
# Request_[INITIATIVE_ID] — Epic Request Index
> Purpose: [Thin governance wrapper description]

## III. CORE CONTENT

### A. Epic Source & Scope
* **Initiative:** 
* **Epic:** 
* **In Scope (Index):** 
* **Out of Scope:** 

### B. Business Objectives & Success Signals 
* **Objectives:**
* **Success Signals (draft/MVP):**

### C. Stakeholders 
`| Role Label | Persona | Responsibility |`

### D. Epic Assumptions & Dependencies 
* **Assumptions:**
* **Dependencies:**

### E. Epic Dependency & Sequencing 
**Order:** 
**Rationale:** 

### F. Epic Non‑Functional Requirements 
* **[EPIC_ID]-NFR-XX:** 

### G. Epic Constraints 
* **[EPIC_ID]-CON-XX:** 

### H. Traceability Matrix (Epic → Feature Requests → Concepts)
`| Epic | Feature | Request | Concept |`

### I. Validation Gates 
* **Gate R0 (Index Ready):** 
* **Gate R1 (Feature Ready):** 
* **Gate R2 (Feature Approved):** 

### J. Open Issues & Risks 
`| ID | Description | Owner | Status |`

### H. Next Steps
```

**Pros**

* Reduces SPS page weight; separates concerns on paper.
* Can serve as a single place to scan Epic approvals/metadata.

**Cons & Risks**

* **Two sources of truth** (SPS vs Index) → drift and re‑sync overhead.
* Authors must context‑switch documents; poorer usability.
* Fragments traceability from SPS→Request since Features live in SPS.

**Decision Status:** Superseded.

**Disposition:** Governance consolidated back into SPS; Index retired to historical reference.

---

#### 3. P3 — Epic Dossier (current architecture)

**Description**

**Principles**

* SPS `T102A-SPSST-S3` is the **Epic dossier** layer; Request is the **Feature WBS dictionary**.
* Keep **YAML minimal** and **subsections explicit**. Visible **Feature Register** replaces collapsed lists.
* **Delta‑only** policy for Epic‑specific assumptions/constraints; inherit from Initiative otherwise.
* **No gate codes in YAML** (gates evolve in Request/Concept); SPS may include a neutral handoff note in Governance.
* Replace **Ripple Notes** → **Epic Changelog**.

**Section‑level framing in `T102A-SPSST-S3`**

* **Procedural Guideline Block** (comment at top): what this section does; pointers to **SPSPG** and Appendix V; authoring micro‑guide.
* **0. Initiative WBS Map**: index‑only `Level | PM Type | ID | Name` (no owners/status) synced with Epic/Feature blocks.
*Initiative WBS Map (structure & guidance)*
- What/Why: High‑level scope index; non‑operational.
- Table schema: `Level | PM Type | ID | Name`
- How (columns):
  - Level: depth integer (1=Initiative, 2=Epic, 3=Feature)
  - PM Type: `Initiative | Epic | Feature`
  - ID: canonical IDs per levelwe
  - Name: descriptive label
– Example rows:
  | Level | PM Type    | ID          | Name                         |
  | :---: | :--------- | :---------- | :--------------------------- |
  | 1     | Initiative | T102        | Consultancy Layer Architecture|
  | 2     | Epic       | T102A       | SPS Workflow Implementation  |
  | 3     | Feature    | T102A‑SPSST | SPS Structural Template      |
* Then one **Epic dossier** per Epic following the pattern below.

**Epic dossier pattern (per Epic)**

The design below is generic (no hardcoded IDs). It explains the intended markdown comments (what/why) and instruction blocks (how). The Concept artifact will implement those comments/blocks literally and without examples.

1) Heading
- What/Why: Introduces a numbered Epic dossier for scanability and referencing.
- Format rule: `#### <ordinal>. `<EPIC_ID>` Epic: `<EPIC_CODE>` — <EPIC_TITLE>`
- How:
  - `<ordinal>` is the sequential number of the Epic within this section.
  - `<EPIC_ID>` is the canonical Epic ID.
  - `<EPIC_CODE>` is a short code for quick referencing.
  - `<EPIC_TITLE>` is a readable title for human audiences.
- Example: `#### 1. `T102A` Epic: `SPS` — SPS Workflow Implementation`

2) YAML identity header
- What/Why: Provides machine‑readable identity for tools and linking.
- Keys (with guidance):
  - `epic_id` (string): equals `<EPIC_ID>` used in the heading; stable identifier.
  - `ePIC_CODE` (string): short code; avoid spaces.
  - `epic_title` (string): descriptive name; human‑friendly.
  - `epic_type` (enum): `new | existing | general`.
  - `epic_status` (enum): `draft | review | approved | deprecated`.
  - `epic_owner` (string): role or named person accountable.
- Example YAML:
  ```yaml
  epic_id: 'T102A'
  ePIC_CODE: 'SPS'
  epic_title: 'SPS Workflow Implementation'
  epic_type: 'existing'
  epic_status: 'review'
  epic_owner: 'LLM_Consultant'
  ```

3) Purpose
- What/Why: Declares the outcome and value of the Epic.
- How: 1–2 short paragraphs; business language; avoid technical “how”.

4) Scope
- What/Why: Prevents scope creep and confusion.
- How: Two bullet lists: In Scope and Out of Scope.
- Example:
  - In Scope: template structure, governance snapshot
  - Out of Scope: automation, unrelated artifacts

5) Governance (table)
- What/Why: Quick controls authors and reviewers can scan.
- How: Two‑column table `Control Item | Details` with items like Tolerances, Reporting Cadence, Downstream Handoff (textual link to Request policy).
- Example:
  | Control Item      | Details                               |
  | :---------------- | :------------------------------------ |
  | Tolerances        | Time ±10% vs plan                     |
  | Reporting Cadence | Bi‑weekly status update               |
  | Downstream Handoff| Request approval policy (see Request) |

6) Inherited Considerations (table)
- What/Why: Lists the most critical rules inherited from the Initiative Considerations that govern this Epic. Full inheritance is assumed.
- How: Four‑column table `Source Artifact | Source ID | Category | Inherited Rule IDs` with emphasis on contextually critical rules using IDs and their Title.
- Example:
  | Source Artifact | Source ID | Category | Inherited Rule IDs |
  | :--- | :--- | :--- | :--- |
  | SPS | T102 | Constraints | `T102-CON-01 (Format Requirements)`, `T102-CON-03 (Documentation Standards)` |
  | SPS | T102 | Dependencies | `T102-DEP-01 (Client Engagement)`, `T102-DEP-02 (Planner Integration)` |

7) Epic Quality Goals
- What/Why: Measures of success tied to this Epic.
- How: Bullets with IDs `[EPIC_ID]-QG-##`; keep atomic and measurable.

8) Epic Dependencies & Interfaces
- What/Why: Lists prerequisites and contracts this Epic must honor.
- How: Bullets with IDs `[EPIC_ID]-DEP-##`; cite referenced artifacts/contracts briefly.

9) Epic Notes & Parking Lot
- What/Why: Background research and context that informs direction.
- How: Bullets with IDs `[EPIC_ID]-NOTE-##`; concise statements.

10) Epic Assumptions (Optional)
- What/Why: Delta assumptions specific to this Epic only.
- How: Bullets with IDs `[EPIC_ID]-ASSUM-##`; do not repeat Initiative assumptions.

11) Epic Constraints (Optional)
- What/Why: Delta constraints specific to this Epic only.
- How: Bullets with IDs `[EPIC_ID]-CON-##`; do not repeat Initiative constraints.

12) Feature Register
- What/Why: Visible, authoritative list of deliverables (features).
- How:
  - Columns: `Feature ID | Name | Purpose (1–2 lines) | Owner | Status | Canonical Link (Request)`
  - Status enum values: `proposed, in‑discovery, in‑request, approved, in‑concept, in‑delivery, done, parked`
  - Canonical Link is the repo‑relative path to the Request file.
- Example row:
  | Feature ID    | Name                    | Purpose                         | Owner          | Status     | Canonical Link |
  | :------------ | :---------------------- | :------------------------------ | :------------- | :--------- | :------------- |
  | T102A‑SPSST   | SPS Structural Template | Refactor for clarity/governance | LLM_Consultant | in‑request | ../request/... |

13) Epic‑Level Issues & Risks (table)
- What/Why: Logs open issues/risks for this Epic.
- How:
  - Columns: `ID | Description | Owner | Status`
  - ID prefixes: `[EPIC_ID]-ISSUE-##` or `[EPIC_ID]-RISK-##`
  - Status enum: `Open | In Review | Blocked | Closed`
- Example row:
  | ID             | Description                        | Owner | Status |
  | :------------- | :--------------------------------- | :---- | :----- |
  | T102A‑RISK‑01  | Drift between map and dossiers     | Team  | Monitored |

14) Epic Changelog
- What/Why: Audit trail of material changes.
- How: Bullets using `**YYYY‑MM‑DD** — change summary`.


**Why this design**

* Aligns with PID practice while preventing duplication with `T102A-SPSST-S4` via the **Inheritance Model**.
* Improves scanability (YAML header, governance table) and traceability (IDs + Canonical Links).
* Keeps SPS **human‑first**; defers procedural details to **SPSPG**.

---

### C. Decision Log Entries (chronological)

#### 1. Entry 1 — 24/08/2025 — Baseline capture 
*Summary: The initial, insufficient structure (P1) was recorded with exploration of an external governance index (P2).*

* **Baseline Structure**
  * **Context:** The original SPS P1 structure for Epics used simplified narrative and collapsible Feature blocks.
  * **Decision:** The P1 structure was deemed insufficient for formal governance. It hid the most critical scope information (the Feature list) and conflated Initiative-level concerns with Epic-level details.
  * **Consequences:** 
    - (+) Established the need for a more robust, visible, and standards-aligned structure. 
    - (-) Required a complete redesign rather than an iterative improvement.
  * **Alternatives Considered:** Iteratively adding sections to P1 was considered but rejected as it would not solve the core architectural flaws.
  * **References:** `design_T102A-SPSST-S3.md (Section III.B.1)`

* **External Index Architecture**
  * **Context:** To address the governance gaps in P1, a separate `Epic Index` file was proposed to hold all Epic-level governance information separating it from the SPS.
  * **Decision:** This approach was rejected. It created two competing sources of truth (the SPS for scope, the Index for governance), which would inevitably drift out of sync. It also harmed the authoring experience by forcing context-switching between documents.
  * **Consequences:** 
    - (+) Solidified the principle that the SPS must be the single, authoritative source of truth for Initiative and Epic-level concerns (the "PID model").
    - (+) Improved the authoring experience by avoiding context-switching between documents.
    - (-) Accepted that the SPS artifact will be a very high-level, larger and more complex document.
  * **Alternatives Considered:** Keeping the P2 model was the primary alternative, but the risk of data drift was deemed too high for a human-first workflow.
  * **References:** `design_T102A-SPSST-S3.md (Section III.B.2)`

#### 2. Entry 2 — 26/08/2025 — Consolidated consultation: P3 + terminology + inheritance
*Summary: This entry covers the foundational decisions to adopt the Epic dossier model, standardize terminology, and define the inheritance and dependency model.*

* **Adoption of Epic Dossier Model**
  * **Context:** With the rejection of the external index, governance needed to be consolidated back into the SPS while maintaining clarity and structure.
  * **Decision:** Adopt the **Epic dossier** model, using a minimal YAML identity header for machine-readability and explicit, bolded subsections for human-readable content. `Epic Assumptions` and `Epic Constraints` were made optional to support a "delta-only" approach.
  * **Consequences:**
    - (+) Creates a standardized, repeatable container for managing each Epic.
    - (+) Balances machine-readability (YAML) with human-first usability (Markdown subsections).
  * *   **Alternatives Considered:** A fully narrative approach (rejected as unstructured); a fully table-driven approach (rejected as too rigid).
  *   **References:** `T102A-SPSST-S3-FR-03`, `T102A-SPSST-S3-FR-04`, `T102A-SPSST-S3-FR-05`

* **Standardization of Terminology and Gate Policy**
  * **Context:** Ambiguous terms ("Ripple Notes") and premature hard-coding of gate references ("R2") in early drafts created confusion.
  * **Decision:** 
    - Replace "Ripple Notes" with the industry-standard **"Epic Changelog"**. 
    - Gate logic is owned by the `Request` artifact; the SPS will only make a textual reference to the policy in the `Governance` table, not a hard-coded reference in YAML.
  * **Consequences:** 
    - (+) Improves clarity and aligns with standard project management vocabulary. 
    - (+) Decouples the SPS from the specific implementation details of the downstream `Request` workflow, making the system more modular.
  * **Alternatives Considered:** Keeping "Ripple Notes" (rejected for being non-standard).
  * **References:** `T102A-SPSST-S3-FR-08 (Epic Changelog)`

* **Formalization of Inheritance Model**
  * **Context:** Principle of Inheritance is assumed where downstream scopes such as `Epic` and `Feature` inherit all rules from their parent such as `Initiative`. However, current delta-only approach does not effective in preventing repetition between rules and requirements defined across scopes level and artifacts. This created drift risk and duplications which require formal inheritance model for governance clarity.
  * **Decision:** Adopt the **"Explicit ID Referencing"** inheritance model per `T102-IG-10 (Inheritance Model)` following note `T102-NOTE-04 (Inheritance Philosophy)`
  * **Consequences:**
    - (+) Creates a clear architectural rule that governs how all artifacts in the workflow relate to each other.
    - (+) Ensures that the `SPSPG` will be built from the approved structural template, guaranteeing consistency.
  * **References:** `T102A-SPSST-NFR-05`, `T102A-SPSST-INT-09`, `T102-IG-10 (Inheritance Model)`, `T102-NOTE-04 (Inheritance Philosophy)`

* **SPSPG dependency**
  * **Context:** Authors need process guidance separate from structure.
  * **Decision:** Capture a dependency from S3 (structure) to future **SPSPG** (process). Use S3 instructional comments as Authoring Micro‑Guide to be formalized in SPSPG.
  ```markdown
  <!-- HOW TO ADD/MANAGE EPICS 
  1. This section is the WBS at the Epic level. For a high-level view of all Epics, see the "Initiative WBS Map" below. Each Epic is defined in its own "dossier."
  2. To add a new Epic, copy an existing dossier. Update the H4 heading and the YAML identity block first (id/name/title/type/status/owner).
  3. Use the bolded subsections for human-readable content (Purpose, Scope, etc.).
  4. Use the optional "Epic Assumptions" and "Epic Constraints" sections ONLY for rules that are different from the global ones in Section III-B. Otherwise, the Epic inherits them.
  5. Update the "Feature Register" with the deliverables for the Epic. The "Status" column is the single source of truth for a Feature's progress.
  6. Use the "Epic Changelog" to log any material changes to the Epic's scope or governance.
  7. For the detailed step-by-step process, refer to the "SPS Procedural Guideline (SPSPG)" document.
  -->
  ```
  * **Consequences:**
  * **References:**

#### 3. Entry 3 — 11/09/2025 — Introduction of Epic Governance Decision Register
*Summary: Introduced the `Epic GDR Index` to provide a formal, auditable log for Epic-level governance decisions, distinct from the general changelog.*

* **Title:** Addition of Epic GDR (Governance Decision Record) Index
* **Context:** While the `Epic Changelog` tracks general changes, there was no dedicated, high-visibility location to log formal governance decisions (e.g., changes to scope tolerances, approval of a new dependency).
* **Decision:** A new mandatory subsection, `Epic GDR Index`, will be added to the Epic dossier. It will contain a summary table and a detailed log for formal, client-approved governance decisions.
* **Consequences:**
  - (+) Creates a single, auditable source of truth for all major governance decisions related to an Epic.
  - (+) Clearly separates high-signal governance events from lower-signal `Changelog` entries.
  - (±) Adds a small amount of authoring overhead, but the value in clarity and auditability outweighs this.
* **Alternatives Considered:** 
  - Using the `Epic Changelog` for all entries (rejected as it would mix major decisions with minor status updates).
  - Seperate file for recording Architecture and Governance DRs on Initiative and Epic levels. 
  - Using Concept `T102C` to records all ADR/GDR of all scope levels. 
* **References:** `T102A-SPSST-S3-FR-09 (Epic GDR Index)`

---

### D. Decision Record (Frozen Summary)
<!-- - A single **canonical summary** distilled from the latest *accepted* ADR(s).  
- Purpose: client-friendly “final decision at a glance” without reading the chronology. -->
#### 1. Decision Record
* **Title:** S3 — Epic dossier structure (P3) and handoff signals
* **Context:** P1 (baseline) hid scope; P2 (Index) split sources of truth. P3 consolidates governance in SPS with clear Epic dossiers.
* **Decision (proposed):** Adopt P3 Epic dossier structure (YAML identity + standardized subsections + visible Feature Register). Keep gates in Request; replace Ripple Notes with Epic Changelog. Record inheritance principle as proposed pending GDR.
* **Consequences:**
  - (+) Unified source of truth; higher scanability and traceability.
  - (+) Minimal machine‑readable identity without over‑engineering.
  - (±) Inheritance model details deferred; GDR pending.
* **Alternatives considered:** P1 baseline; P2 Index‑first governance (drift risk).
* **References:** Request S3 FR‑01..08; Design Log `design_T102A-SPSST-S3.md` (Entry 3 consolidated).

#### 2. Final Proposed Solution
```markdown
### C. Epics & Breakdown
<!-- HOW TO ADD/MANAGE EPICS
This section is the Initiative’s WBS at Epic scope. It contains:
  (a) a non‑operational Initiative WBS Map (index only), and
  (b) one Epic dossier per Epic (identity YAML + descriptive subsections + registers/logs).
The detailed HOW lives in the SPSPG; this block provides authoring cues only. -->

#### 0. Initiative WBS Map
<!-- PURPOSE: A high-level structural index of the project's scope. It shows hierarchy only; keep synchronized with Epic/Feature sections below. -->
*[Column rules: Level=1/2/3 (Initiative/Epic/Feature); PM Type ∈ {Initiative,Epic,Feature}; ID uses canonical pattern; Name is a short label.]*


| Level | PM Type | ID | Name |
| :---: | :------ | :- | :--- |

---

#### 1. `<EPIC_ID>` Epic: `<EPIC_CODE>` — <EPIC_TITLE>

    ```yaml
    epic_id: '<EPIC_ID>'
    epic_code: '<EPIC_CODE>'
    epic_title: '<EPIC_TITLE>'
    epic_type: '<new|existing|general>'
    epic_status: '<draft|review|approved|deprecated>'
    epic_owner: '<OWNER_ROLE_OR_NAME>'
    ```

**Purpose**
<!-- PURPOSE: State the primary goal and outcome of this Epic. -->
*[Write 1–2 short paragraphs in business language; avoid implementation detail.]*

**Scope**
<!-- PURPOSE: Define the explicit boundaries of this Epic. -->
*[Use bullets; separate clearly into In Scope vs Out of Scope.]*
- In Scope: …
- Out of Scope: …

**Governance**
<!-- PURPOSE: PM control parameters for this Epic; the detailed HOW lives in SPSPG. -->
*[Use a two‑column table. Keep items concise; link to Request for gate policy.]*

| Control Item       | Details |
| :----------------- | :------ |
| Tolerances         | (e.g., “Scope change ≤X% before re-baseline”) |
| Reporting Cadence  | (e.g., “Weekly status @ Fri 16:00 CET”) |
| Downstream Handoff | Request approval policy (see Request) |

**Inherited Considerations**
<!-- PURPOSE: Lists the most critical rules inherited from the Initiative Considerations that govern this Epic. Full inheritance is assumed. -->
*[Group rules by category; emphasize most critical inherited rules with their corresponding IDs and titles in parentheses under `Inherited Rule IDs`]*
| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |

**Epic Quality Goals**
<!-- PURPOSE: Measurable success criteria specific to this Epic. -->
*[Use IDs `[EPIC_ID]-QG-##`; keep atomic and measurable.]*

**Epic Dependencies & Interfaces**
<!-- PURPOSE: Prerequisites and contractual touchpoints specific to this Epic. -->
*[Use IDs `[EPIC_ID]-DEP-##`; include brief rationale or reference.]*

**Epic Assumptions (Optional)**
<!-- PURPOSE: Epic‑specific assumptions that are deltas vs Initiative only. Optional subheading. -->
*[Use IDs `[EPIC_ID]-ASSUM-##`; do not repeat Initiative assumptions.]*

**Epic Constraints (Optional)**
<!-- PURPOSE: Epic‑specific constraints that are deltas vs Initiative only. Optional subheading.-->
*[Use IDs `[EPIC_ID]-CON-##`; do not repeat Initiative constraints.]*

**Epic Notes & Parking Lot**
<!-- PURPOSE: Background, research, and context; keep concise. -->
*[Use IDs `[EPIC_ID]-NOTE-##`; one idea per bullet.]*

**Epic GDR Index**
<!-- Provide a single, auditable index of epic-level governance decisions that guide governance, artifacts, and gates across the epic. -->
*[Assign IDs as [EID]-GDR-###; set Client as default owner; keep governance-only decisions (no technical ADRs); use lower-kebab anchors pointing to decision bodies]*

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|--------|-------|--------|-------|-----------|------------|--------|
| [EID]-GDR-001 | <Concise governance decision title> | `Proposed/Accepted/Deprecated` | Client | YYYY-MM-DD | <IDs or —> | #[eid-gdr-001-kebab-title] | 

* **`[EID]-GDR-001` — <Concise Title> — {#[eid-gdr-001-kebab-title]}**
  - **Context**: Brief rationale and background for the governance decision.
  - **Decision**: Single-sentence decision statement (what is adopted/mandated).
  - **Consequences**: Key impacts/tradeoffs; approvals or policy implications.
  - **References**: Related considerations & rules with links/IDs reference (e.g., `T102-CON-01 (Format Requirements)`, `T102A-QG-01 (Clarity)`) and external or internal scopes and standards if relevant (e.g: `T101`, `T102A-SPSST`, `T102D`)

**Feature Register**
<!-- PURPOSE: Official list of features with canonical links to Requests. -->
*[Add rows according to the table instructions. Keep owner `Client` by default. Canonical Link = repo‑relative Request path.]*

| Feature ID | Name | Purpose (1–2 lines) | Owner | Status | Canonical Link (Request) |
| :--------- | :--- | :------------------ | :---- | :----- | :----------------------- |
| [EPIC_ID]-[FEATURE_CODE] | <Short feature name> | <Brief purpose description> | Client | `proposed, in‑discovery, in‑request, approved, in‑concept, in‑delivery, done, parked` | <../path/to/request.md> |

**Epic Issues & Risks**
<!-- PURPOSE: Log Epic‑specific issues/risks. -->
*[Add rows according to the table instructions. Keep owner `Client` by default. ID must be categorized as either an issue or risk]*

| ID | Description | Owner | Status |
| :--| :---------- | :---- | :----- |
| [EPIC_ID]-ISSUE-## / [EPIC_ID]-RISK-## | <Issue/risk description> | <Owner role/name> | `Open, In Review, Blocked, Resolved, Deferred` |

**Epic Changelog**
<!-- PURPOSE: Lightweight audit trail for scope/governance changes. -->
*[Bullets using `**YYYY‑MM‑DD** — change summary`.]*
```

### E. Integration, Dependency & Tracibility
<!-- Design‑level integration and trace links only. Do not duplicate the operative logs in SPS (Epic Dependencies & Interfaces) or Request (Feature Integration Notes). Use this section to point to IDs and required propagation actions. -->
#### 1. Integration Notes

* `T102A-SPSST-INT-S3-01 (Body Approvals)` — Epic dossier pattern (YAML identity + explicit subsections) is the standard for SPS §III‑C.
* `T102A-SPSST-INT-S3-02 (Document Metadata)` — Visible Feature Register acts as single source of truth for feature scope list and canonical links to Request.
* `T102A-SPSST-INT-S3-03 (Universal IDs)` — Gate semantics remain owned by Request; SPS contains only textual reference in Governance.
* `T102A-SPSST-INT-S3-04 (Traceability)` — Principle of Inheritance is recorded as proposed (not finalized); downstream artifacts should specify deltas only.

**Upstream**

* `T102A-SPSST-S4` (Initiative Considerations) provides initiative/project rules. Epics inherit these rules unless an Epic records a delta in its optional Assumptions/Constraints subsections.

**Downstream**

* **Request** consumes: Epic YAML identity, Purpose/Scope, Epic Quality Goals, `[DEP]` list, Feature Register, Issues/Risks, and Epic Changelog entries relevant to the Feature’s context.
* **SPSPG** will formalize the HOW (decomposition patterns, readiness signals, authoring rules) using SPS instructional blocks as source material, which includes the instructional comments designed in `T102A-SPSST-S3-FR-01` as its primary source material.

#### 2. Story-local Dependency

| From (FR)                               | Depends On (FR)                               | Rationale |
| --------------------------------------- | --------------------------------------------- | --------- |
| `T102A-SPSST-S3-FR-05 (Epic Subsections)`   | `T102A-SPSST-S3-FR-04 (Epic YAML Header)`                | Subsections rely on `epic_id` for prefixed IDs and identity context. |
| `T102A-SPSST-S3-FR-06 (Feature Register)`   | `T102A-SPSST-S3-FR-03 (Epic Dossier Structure)`; `T102A-SPSST-S3-FR-04 (Epic YAML Header)` | Feature table sits inside a dossier and uses `epic_id` context; canonical links reference Request artifacts. |
| `T102A-SPSST-S3-FR-07 (Issues & Risks)`     | `T102A-SPSST-S3-FR-03 (Epic Dossier Structure)`; `T102A-SPSST-S3-FR-04 (Epic YAML Header)`; `T102A-SPSST-S3-FR-05 (Epic Subsections)` | Table uses `[EPIC_ID]-ISSUE/RISK-##` prefixes and appears after core subsections. |
| `T102A-SPSST-S3-FR-08 (Epic Changelog)`     | `T102A-SPSST-S3-FR-03 (Epic Dossier Structure)`                  | Changelog is part of the dossier container and follows the required pattern. |
| `T102A-SPSST-S3-FR-02 (Initiative WBS Map)`            | `T102A-SPSST-S3-FR-06 (Feature Register)`         | Must remain synchronized with Epic/Feature entries from registers. |
| `T102A-SPSST-S3-FR-01 (Procedural Guideline Block)`   | —                                             | Instructional; influences authoring but does not block structure. |

#### 3. Tracibility Matrix

| ID                      | Title / Description                         | Status     | Evidence / Location                                         | Notes |
| :---------------------- | :------------------------------------------ | :--------- | :---------------------------------------------------------- | :---- |
| T102A-SPSST-S3-FR-01    | Procedural Guideline Block                  | Addressed  | Final Proposed Solution → top HTML comment (FR‑01)          | —     |
| T102A-SPSST-S3-FR-02    | Initiative WBS Map                          | Addressed  | Final Proposed Solution → `0. Initiative WBS Map` (FR‑02)   | —     |
| T102A-SPSST-S3-FR-03    | Epic Dossier Structure                      | Addressed  | Final Proposed Solution → H4 dossier container              | —     |
| T102A-SPSST-S3-FR-04    | Epic YAML Header                            | Addressed  | Final Proposed Solution → fenced YAML identity              | —     |
| T102A-SPSST-S3-FR-05    | Epic Subsections                            | Addressed  | Final Proposed Solution → Purpose/Scope/Governance/etc.     | —     |
| T102A-SPSST-S3-FR-06    | Feature Register                            | Addressed  | Final Proposed Solution → feature table skeleton            | —     |
| T102A-SPSST-S3-FR-07    | Issues & Risks                              | Addressed  | Final Proposed Solution → issues/risks table                | —     |
| T102A-SPSST-S3-FR-08    | Epic Changelog                              | Addressed  | Final Proposed Solution → changelog bullets                 | —     |
| T102A-SPSST-NFR-02      | Author usability                             | Improved   | Dossier pattern + Feature Register                          | —     |
| T102A-SPSST-IF-02       | Epic data extraction                         | Supported  | YAML identity + Feature Register   

---

### F. Ripple Test Notes
* Dossier headings render; YAML identity parses; Feature Register present.
* Epic‑scoped IDs (QG/DEP/NOTE/ISSUE/RISK) use prefixes with Epic ID.
* No gate codes in YAML; textual governance reference only.


### G. Open Questions & Risks 
<!-- Carry into QA -->

#### 1. Risks Log

| ID | Description | Owner | Status | Target Date | Resolution Link |
|---|---|---|---|---|---|
| T102A-SPSST-S3-RISK-01 | Authors may violate delta‑only policy causing duplication. | Template Owner | Monitored | — | — |
| T102A-SPSST-S3-RISK-02 | Initiative WBS Map can drift from Epic dossiers. | Template Owner | Mitigating | — | — |

#### 2. Questions Log

| Entry | QID | Question | Proposed Answer (if any) | Status | Owner | Target Date | Res. Link |
|:---:|---|---|---|---|---|---|---|
| 3 | T102A-SPSST-S3-Q-01 | Keep SPS governance text neutral while Request finalizes gates? | Yes — SPS stays neutral; Request owns gate codes. | Open | Client | — | — |
| 3 | T102A-SPSST-S3-Q-02 | Standardize status badges/colors in template? | Leave as plain text for v1; styling optional. | Open | Client | — | — |
| 3 | T102A-SPSST-S3-Q-03 | Enforce repo‑relative canonical links only? | Prefer repo‑relative; allow mirrors by exception. | Open | Client | — | — |
| 3 | T102A-SPSST-S3-Q-04 | Lint duplicate Initiative vs Epic deltas? | Desirable; defer enforcement to doc‑lint in a later iteration. | Open | Planner | — | — |
| 3 | T102A-SPSST-S3-Q-05 | Role contracts treated as [INTF] vs guidance in §III‑B? | Contracts as [DEP]/Interfaces; guidance remains in §III‑B. | Open | Consultant | — | — |

---

### G. Appendices

**A. Glossary (local to S3)**

*   **Epic dossier** — The standardized Epic container in `T102A-SPSST-S3` (heading, YAML identity, scope, goals, dependencies, register, and logs).
*   **Canonical Link (Request)** — The repository-relative file path to the authoritative `Request` artifact for a given Feature.
*   **Delta-only policy** — The principle that an Epic (or a `Request`) should only document assumptions, constraints, or NFRs that are new, more specific, or override the rules inherited from its parent artifact.
