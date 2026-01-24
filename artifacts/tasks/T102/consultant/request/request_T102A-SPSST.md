---
artifact_type: 'REQUEST'
initiative_id: 'T102'
epic_id: 'T102A'
feature_id: 'T102A1'
feature_code: 'SPSST'
version: '1.0.0'
date: '2025-08-16'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# REQUEST: SPS Structural Template - T102A1

## I. EXECUTIVE SUMMARY

---

## II. TABLE OF CONTENTS

---

## III. CORE CONTENT

<!-- Part 0 — SAD-lite -->

### A. Feature Solution Framework

#### 1. Problem Recap & Constraints
<!-- Briefly restate *what we're solving* and *the guardrails*, by reference—no duplication.* -->

**Problem & Desired Outcome**
- **Problem:** SPS authors produce inconsistent structure/IDs; handoffs to Requests require rework.
- **Desired Outcome:** A clean, unambiguous SPS Structural Template (SPSST) enabling predictable Feature-level handoff.

**Stakeholders & Concerns (42010)**
<!-- Make concerns explicit so criteria are traceable to stakeholder needs.* -->
- **Stakeholders:** Decision Owner, Template Owner, Request Author, Planner.
- **Concern → Criterion mapping:**
  - Author guidance clarity → *Author Usability*
  - Parse/validation stability → *Automation-Readiness*
  - Backward compatibility → *Maintainability*
  - Adoption friction → *Time-to-Adopt, Risk*

**Viewpoints (42010)**
<!-- Declare the "lenses" used to model the concept.* -->
- **Document Architecture Viewpoint:** section schemas, ID contracts, approval signals.
- **Workflow/Handoff Viewpoint:** states, gates (R2→C0→C3), generator/validator touchpoints.

---

#### 2. Decision Criteria & Weights
<!-- Agree *how* we'll judge options; weights are co-owned by Client + Template Owner + Consultants.* -->

**Baseline Criteria**
<!-- Extend criteria if feature-specific needs arise -->
- Author Usability; 
- Maintainability; 
- Automation-Readiness; 
- Consistency w/ current workflow; 
- Risk/Disruption; 
- Time-to-Adopt.

**Weighting Method**
- Sum = **1.00** with weights: **0.25, 0.25, 0.15, 0.15, 0.10, 0.10** respectively for the criteria listed above. 
- **Governance:** multi‑rater scoring; each score requires a one‑line rationale (logged below table).

<!-- Part 1 — Business View (BRD) -->

### B. Source & Scope

* **Initiative:** `T102 (Consultancy Layer Architecture)`
* **Epic:** `T102A (SPS)`
* **Feature:** `T102A1 (SPSST)`
* **Repository Path (source):** `prompt/templates/consultant/sps_T102-CONSULTANT.md`
* **Repository Path (target):** `prompt/templates/consultant/sps_structural_template.md`

**In Scope:**

* Define the structure and instructional content of `sps_structural_template.md`.
* Specify YAML frontmatter keys and validation rules.
* Specify section hierarchy and per-section **[Instructions]** blocks to guide humans/LLMs when filling the SPS.
* Define handoff signals from SPS to Request (at Feature level), limited to IDs and status.

**Out of Scope:**

* `T102A2 (SPSPG)` (*SPS Procedural Guideline*).
* `T102A3 (MANIFEST)` (*SPS manifest/versioning helper*, if/when confirmed).

---

### C. Business Objectives & Success Signals 

* **Primary Objectives:**
  * Provide a **simple, unambiguous SPS template** that captures Problem (III‑A), Epics→Features breakdown (III‑B), Initiative/Global considerations (III‑C), Issues & Glossary (III‑D/E).
  * Ensure **Feature‑level handoff** to Requests by standardizing IDs and required fields.

* **Success Signals (MVP, qualitative):**
  * Authors can complete a blank SPS using the template **with minimal extra guidance sessions**.
  * First pilot Requests created from SPSST **require minimal rework**.

---

### D. Stakeholders

| Role Label | Persona | Responsibility |
| :--- | :--- | :--- |
| Decision Owner | Client | Approves this Feature Request & its ACs. |
| Template Owner | Client | Maintains `sps_structural_template.md`. |
| Request Author | LLM_Consultant | Consumes SPS outputs to produce Feature Requests. |
| Concept Author | LLM_Consultant | Consumes Feature Requests for Concept. |

---

### E. Inherited Considerations

This Feature inherits the following Epic-level requirements and considerations from `T102A-SPS`. These E-RIDs apply cross-feature and are defined in the Epic SPS.

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :--- | :--- | :--- | :--- |
| SPS | T102 | Constraints | `T102-CON-01 (Markdown Format)` |
| SPS | T102 | Dependencies | `T102-DEP-01 (Client SLA)` |
| SPS | T102A | Quality Goals | `T102A-QG-02 (Traceability)` |

---

### F. Feature Requirements

#### 1. Assumptions

* **Assumptions**
  * SPS documents use **slug IDs** for Epics/Features (no A/B/C labels).
  * SPS **does not** include success metrics or ACs; those are defined in Requests.
  * All artifacts (SPS/REQUEST/CONCEPT) adopt the **YAML Header**; standard documentation retains body metadata.  

#### 2. Constraints

* **T102A1-CON-01 (Scope Discipline)** SPS stays focused on **problem/why + high‑level what** on Initiative and Epic scope, Feature-specific and Stories scope are passed down to REQUEST and CONCEPT. 

#### 3. Non-Functional Requirements

* **T102A1-NFR-01 (Tool Parsing)** Parsable by common Markdown/YAML tooling (compatibility/portability).
* **T102A1-NFR-02 (Author Usability)** Section names and order intuitive for non‑technical users (usability).
* **T102A1-NFR-03 (Stable IDs)** IDs are non‑sequential (slug/UUID‑friendly) to avoid renumbering churn (maintainability).
* **T102A1-NFR-04 (Instructional Pattern)** Every subsection SHALL include a single-line `*[Instructions]*` for the **how**, and HTML comments for **purpose/rationale**

#### 4. Dependencies

* **Dependencies**
  * `prompt/templates/consultant/sps_structural_template.md` (the artifact this Request specifies).
  * `prompt/templates/request/request_structural_template.md` (for alignment of handoff expectations).
  * `prompt/documentation/prompt_main.md`
  * `documentation/general.md` (structure & versioning norms).
  * `prompt/artifacts/tasks/T102/consultant/request/request_T102A-INDEX_T102_v1.0.0_i1.md`

#### 5. Interfaces & Data

* **T102A1-IF-01 (Initiative Data Extraction)** The LLM_Consultant SHALL be able to read `initiative_id`, `epic_id`, `feature_id` from the **header**, and the relevant **approval lists** from the **body**, to complete the Feature Request accurately.
* **T102A1-IF-02 (Epic Data Extraction)** The LLM_Consultant SHALL be able to parse each Epic dossier by identifying its fenced YAML **header** to extract `epic_id`, `epic_status`, and `epic_owner`, and read the `Feature Register` table to identify features ready for the `Request` workflow.

#### 6. Implementation Guidance

#### 7. Integration Notes

* **T102A1-INT-01 (Body Approvals)** Approval signals SHALL be recorded in the **body** following format:
  - SPS: `**Approved Epics:** [T102A, T102B]` 
  - Request: `**Approved Features:** [T102A1]` 
  - Concept: `**Approved Stories:** [T102A1-S01]`
* **T102A1-INT-02 (Document Metadata)** Standard docs use body metadata; artifacts use YAML header.
* **T102A1-INT-03 (Universal IDs)** `initiative_id` across all artifacts; `epic_id`/`feature_id` for feature docs; `story_id` for story docs.
* **T102A1-INT-04 (Traceability)** Canonical Links must be **repo-relative** and stable; IDs must match the formats defined in S1.
* **T102A1-INT-05 (Terminology Clarification)** "Global" refers to Program/Portfolio level, whereas "Initiative" refers to the SPS specifically. This naming distinction affects cross-references across all templates and artifacts.
* **T102A1-INT-06 (Standards Alignment)** Industry standard categorization (PRINCE2 PID, ISO 29148, BABOK v3) establishes reusable pattern for similar governance sections across other stories and templates.
* **T102A1-INT-07 (Documentation Pattern)** Markdown comments under each subsection establish template pattern for explanatory guidance that should be consistently applied across all structural templates.


### G. Feature Governance Decisions

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### H. Open Issues & Risks 

**Issues**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A1-ISSUE-001` | **Body Field Name** | Decide exact body field name/format for approved Feature IDs (e.g., `Approved Features: [T102A]`). | LLM_Consultant | `OPEN` | `MEDIUM` | 2025-08-16 | — | — |
| `T102A1-ISSUE-002` | **Ripple Notes Terminology** | Ripple Notes terminology issue? Should this be changed to something more industry-standard. | LLM_Consultant | `OPEN` | `MEDIUM` | 2025-08-16 | — | — |
| `T102A1-ISSUE-003` | **Governance Section** | Determine whether we keep Governance section in v1. | LLM_Consultant | `OPEN` | `MEDIUM` | 2025-08-16 | — | — |

**Risks**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A1-RISK-001` | **Residual Tokens** | Residual v1 tokens may reappear if copied from older docs. | LLM_Consultant | `MONITORED` | `MEDIUM` | 2025-08-16 | Mitigate via validation checklist. | 2025-09-16 |

### I. Research & Notes
**Research**

| Research ID | Title | Summary | Linked To | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |

**Notes**

### J. Stories & Specification 

#### 1. Story `T102A1‑S01` — YAML Frontmatter & Metadata

**Purpose**
Provide a **small, stable, cross-artifact identity & governance header**: *what type of artifact this is, what scope it represents, which IDs bind it to the program, who owns decisions, and what status/date/version it has.* Nothing more (automation fields arrive in v2).

**Functional Requirements**
* **T102A1-S01-FR-01 (Header Keys)**  
  The template SHALL begin with a valid **YAML header** containing only these core keys:  
  `artifact_type, initiative_id, (epic_id), (feature_id), (story_id), version, date, status, author, decision_owner_role, (dependencies)` where keys in parentheses are required when applicable (feature/story docs).

* **T102A1-S01-FR-02 (Key Formats)**  
  The header keys SHALL conform to the following:  
  `artifact_type ∈ {SPS, REQUEST, CONCEPT}`;  
  `initiative_id: ^T\d{3}$` (e.g., `T102`);  
  `epic_id: ^T\d{3}[A-Z]$` (e.g., `T102A`);  
  `feature_id: ^T\d{3}[A-Z]-[A-Z0-9_]+$` (e.g., `T102A1`);  
  `story_id: ^T\d{3}[A-Z]-[A-Z0-9_]+-S\d+$` (e.g., `T102A1-S01`);  
  `version`: SemVer; 
  `date`: ISO-8601 (YYYY-MM-DD);  
  `status ∈ {draft, review, approved, rework, deprecated}`;  
  `author ∈ {LLM_Consultant, LLM_Planner, LLM_Developer, LLM_Reviewer}`;  
  `decision_owner_role = Client`;  
  `dependencies`: list of relative `*.md` paths (optional).

* **T102A1-S01-FR-03 (Schema Examples)**  
  The template SHALL include canonical examples for SPS/REQUEST/CONCEPT headers and reference **header.schema.v1** (structure only; no enforcement in v1).

**Acceptance Criteria**
  **Given** an SPS/Request/Concept artifact created using the template,  
  **When** the YAML header is checked informally against **header.schema.v1**,  
  **Then** only allowed keys are present and formats/enums match;  
  **And** the **body** contains the appropriate approval list as specified;  
  **And** the header matches the canonical example for its artifact type.


#### 2. Story `T102A1‑S02` — Problem Definition (III‑A)

* **T102A1-S02-FR-01** The section SHALL include the subsection headers `1. The Problem`, `2. The Desired Outcome`, and `3. Business Case`.
  * **The Problem:** A concise statement of the pain/constraint, who is affected, and the current impact.
  * **The Desired Outcome:** The state you want after change; avoid naming solutions.
  * **Business Case:** Why this matters now (value, risk, compliance, opportunity) in 2–4 lines.
* **T102A1-S02-FR-02** Under each subsection, include a *[Instructions]* defining what belongs there

**Acceptance Criteria**

* **Given** a user opens Section III‑A,
* **When** they follow the *[Instruction]* for each subsection,
* **Then** each subsection is completed with clear, business‑language entries that fulfill their respective purposes.

#### 3. Story `T102A1‑S03` — Epics & Breakdown (III‑C)

**Purpose**
To define a clear, hierarchical, and standards-aligned structure for **Epics & Breakdown** Section, establishing it as the Initiative’s Work Breakdown Structure (WBS). This design positions the SPS as the central Project Initiation Document (PID), where each Epic is a self-contained dossier with its own metadata, scope, goals, and a register of its child Features.

**Functional Requirements**
* **T102A1-S03-FR-01 (Procedural Guideline Block)**
  The template SHALL begin with a comprehensive markdown comment block explaining the section's purpose, the core principles of hierarchy (SPS=PID, Request=WBS Dictionary) and detailed instructional methodology and logics on how to fill in this section. 

* **T102A1-S03-FR-02 (Initiative WBS Map)**  
  The section SHALL include a subsection `0. Initiative WBS Map` containing a markdown table with columns `Level | PM Type | ID | Name` to provide a high-level, non-operational index of the project's scope.

* **T102A1-S03-FR-03 (Epic Dossier Structure)**
  Each Epic in the section SHALL be presented as a self-contained dossier, beginning with a unique H4 heading following the exact format: 
  `#### [number]. `[epic_id]` Epic: `[epic_name]` - [epic_title]` 
  (e.g., #### 1. `T102A` Epic: `SPS` - SPS Workflow Implementation).

* **T102A1-S03-FR-04 (Epic YAML Header)**
  Each Epic dossier SHALL begin with a fenced YAML code block containing the following keys for essential, machine-readable metadata:
  - `epic_id`: Matches the Epic ID in the heading. (e.g., "T102A")
  - `epic_name`: Short abbreviation or code letters (e.g., "SPS")
  - `epic_title`: Free text description (e.g., "SPS Workflow Implementation") 
  - `epic_type`: Enum (`new` | `existing` | `general`).
  - `epic_status`: Enum (`draft` | `review` | `approved` | `deprecated`).
  - `epic_owner`: The role or name responsible for the Epic.

* **T102A1-S03-FR-05 (Epic Subsections)**
  Each Epic dossier SHALL include the following subsections, implemented as bolded headings, each with a `<!-- PURPOSE: ... -->` comment explain the "what" and "why" and a `*[Instructions: ...]*` block under the heading to briefly demonstrate the "how":
  - **Purpose**: A 1-2 paragraph description of the Epic's goal.
  - **Scope**: Bulleted lists for `In Scope` and `Out of Scope` items.
  - **Governance**: A small **Control Item** table containing:  
  **Tolerances** (optional, short text); **Reporting Cadence** (optional, short text); **Downstream Handoff (reference)** = "Request approval policy (see Request)";  
  -  **Epic Quality Goals**: A list of measurable success criteria specific to the Epic, with each item prefixed `[EPIC_ID]-QG-###`.
  -  **Epic Dependencies & Interfaces**: A list of prerequisites and contractual touchpoints specific to the Epic, prefixed `[EPIC_ID]-DEP-###`.
  - **Epic Notes & Parking Lot**: A container for background, research, and context, prefixed `[EPIC_ID]-NOTE-###`.
  - **(Optional) Epic Assumptions**: A container for assumptions specific to the Epic, prefixed `[EPIC_ID]-ASSUM-###`.
  - **(Optional) Epic Constraints**: A container for constraints specific to the Epic, prefixed `[EPIC_ID]-CON-###`.

* **T102A1-S03-FR-06 (Feature Register)**  
  Each Epic SHALL include a visible table:  
  `Feature ID | Name | Purpose (1–2 lines) | Owner | Status | Canonical Link (Request)`  
  - The `Status` column SHALL use an enum from the set `{proposed, in-discovery, in-request, approved, in-concept, in-delivery, done, parked}`
  - `Canonical Link (Request)` = the **repo-relative path** to the authoritative Request file for that Feature.

* **T102A1-S03-FR-07 (Issues & Risks)**  
  Each Epic SHALL include a small table: `ID | Description | Owner | Status` containing Epic-specific issues and risks. 
  - The `ID` must be prefixed with the `[EPIC_ID]-ISSUE-##` or `[EPIC_ID]-RISK-##`, 
  - `Status` must use the enum `{Open, In Review, Blocked, Closed}`.

* **T102A1-S03-FR-08 (Epic Changelog)**  
  Each Epic SHALL include a bulleted **Epic Changelog** list for logging material changes to the Epic's scope or governance, following the format `**YYYY-MM-DD** - [Change Summary]`.

* **T102A1-S03-FR-09 (Epic GDR Index)**  
  Each **Epic dossier** SHALL include an index table to record all **epic-level governance decisions** following the implementation from `T102-ADR-004 (Decision Records Index)`

**Acceptance Criteria**

*   **Given** an author opens a blank SPS template to create a new Epic in Section III-C,
*   **When** they follow the instructional guidance,
*   **Then** the new Epic dossier begins with a valid YAML header containing the required keys in the correct format.
*   **And** the dossier contains all required descriptive subsections 
*   **And** the `Feature Register` is a visible markdown table with the specified columns;
*   **And** any Epic-specific quality goals or dependencies are prefixed with the correct `[EPIC_ID]`.


#### 4. Story `T102A1‑S04` — Initiative Considerations (III‑B)

**Purpose**
Provide industry-standard governance factors structure that applies to ALL epics, organized per PRINCE2 PID, ISO 29148, and BABOK v3 standards with clear categorization and reduced cognitive load.

**Functional Requirements**
* **T102A1-S04-FR-01** Rename **Global Considerations** to **Initiative Considerations** to avoid portfolio‑level naming conflicts and clarify scope specificity to the SPS document.
  
* **T102A1-S04-FR-02** Provide six industry-standard subsections with explanatory markdown comments:
  1. **Project Assumptions** (bullets): Factors believed true but unconfirmed per BABOK v3
  2. **Project Constraints** (bullets): Non-negotiable restrictions/limitations per ISO 29148
  3. **Success Criteria & Quality Goals** (bullets): Measurable targets per ISO 29148 verification requirements
  4. **Dependencies & Interfaces** (bullets): External factors and technical contracts
  5. **Implementation Guidance** (bullets): Technical guidance for execution teams
  6. **Notes & Parking Lot**: Everything else (context, out-of-scope items, etc..)
  7. **Initiative GDR Index**: Initiative-level governance decisions using implementation from `T102-ADR-004 (Decision Records Index)`
   
* **T102A1-S04-FR-03** Each subsection SHALL include markdown comments explaining:
  * What content belongs in that category
  * Industry standard references (PRINCE2 PID, ISO 29148, BABOK v3)
  * Clear definitions and purposes for categorization
  
* **T102A1-S04-FR-04** Under each subsection content area, include *[Instructions]* defining what belongs there with plain language guidance.
  

**Acceptance Criteria**

* **Given** an SPS document using the Initiative Considerations template,
* **When** the section is populated following the *[Instructions]* and markdown comment guidance,
* **Then** all entries fit clearly into one of the six subsections with no ambiguity;
* **And** each subsection includes the required explanatory markdown comment;
* **And** the structure follows industry standards (PRINCE2 PID, ISO 29148, BABOK v3);
* **And** cognitive load is reduced through clear categorization and definitions.


#### 5. Story `T102A1‑S05` — Open Issues & Risks (III‑D)

* **T102A1-S05-FR-01** Include a table with columns: `ID | Description | Owner | Status | Target Date`.
* **T102A1-S05-FR-02** Add a **short clarifying line** describing how the log is maintained (statuses: Open / In Review / Blocked / Closed).

**Acceptance Criteria**

* **Given** an issue is logged,
* **When** the table is updated,
* **Then** the entry follows the required columns and guidance.

#### 6. Story `T102A1‑S06` — Project Glossary (III‑E)

* **T102A1-S06-FR-01** Provide bullet fields for `Term` and `Definition`.
* **T102A1-S06-FR-02** Add a *[Instructions]* encouraging client‑originated, plain language; ≤ 25 words per definition.

**Acceptance Criteria**

* **Given** a term is added,
* **When** the glossary is viewed,
* **Then** each term has a definition in client language.

#### 7. Story `T102A1‑S07` — Portfolio Sections (Global)

* **T102A1-S07-FR-01** The SPS template SHALL include the portfolio‑level sections: **IV. Glossary**, **VI. Validation Checklist**, and **VIII. Next Steps**.
* **T102A1-S07-FR-02** **VIII. Next Steps** SHALL explicitly:

  * state that each approved Feature creates a **Feature Request**;
  * list the handoff bundle to Request (Feature ID, Purpose, optional Stories, **Initiative Considerations** bullets);
  * declare that **Concept** begins only after the Feature Request is approved (Gate R2) and consumes the same bundle.
* **T102A1-S07-FR-03** The section order SHALL ensure **III‑C Initiative Considerations** appears **above** **VIII. Next Steps**.

**Acceptance Criteria**

* **Given** the document outline,
* **When** sections are ordered and reviewed,
* **Then** the portfolio sections exist and the order rule is satisfied.

#### 8. Story `T102A1‑S08` — Handoff Protocol (Feature → Request)

* **T102A1-S08-FR-01** In **VIII. Next Steps**, state that **each approved Feature spawns its own Request** artifact.
* **T102A1-S08-FR-02** Provide a mapping guide from SPS fields to Request shells:

  * **BRD.A Source & Scope** ← SPS Feature block + Initiative Considerations;
  * **SRS.F Functional Requirements** ← derived from Feature Purpose and Story notes;
  * **SRS.G NFRs** ← seeded from Initiative Considerations’ Quality Goals.

**Acceptance Criteria**

* **Given** a Feature is marked approved,
* **When** Next Steps are followed,
* **Then** a dedicated Request is created using the specified bundle; Concept waits for Gate R2.


<!-- Part 3 — Validation & Acceptance -->

### K. Acceptance Criteria Register (summary)

| ID | Title | AC Summary |
|----|-------|------------|
| `T102A1-S01` | YAML Frontmatter & Metadata | Required keys valid; approval IDs listed in body. |
| `T102A1-S02` | Problem Definition | Three subsections completed via [Instructions]. |
| `T102A1-S03` | Features & Breakdown | Feature block schema used; plain language; optional Story notes. |
| `T102A1-S04` | Initiative Considerations | Four industry-standard subsections with explanatory comments; follows PRINCE2/ISO 29148/BABOK v3. |
| `T102A1-S05` | Issues & Risks | Table conforms to required columns and guidance. |
| `T102A1-S06` | Project Glossary | Term/definition bullets in client language. |
| `T102A1-S07` | Portfolio Sections | Next Steps, Validation Checklist, and IV Glossary present; order rule met. |
| `T102A1-S08` | Handoff Protocol | Request created per bundle; Concept waits for Gate R2. |
---
## V. APPENDIX 

### A. Amendment Log
| Date | Change Requester | Affected Req. ID | Summary of Change |
|------|------------------|------------------|-------------------|
| 2025-08-01 | Client | Initial | Initial SPS creation |

---

## VI. VALIDATION CHECKLIST

- [x] The Problem Statement (Section III-A) has received explicit client approval.
- [x] All requirements in Section III-B are prefixed with a unique, traceable ID (e.g., `SPS-T102-001`).
- [x] The Decision Owner / Accountable Role has been identified in Section III-C.
- [x] All known open issues, risks, and dependencies have been logged in Section III-D.
- [x] The artifact's YAML header is complete and syntactically correct.
- [ ] The 'Next Steps' section clearly defines the handoff to the Request workflow.

---

## VII. STAKEHOLDER SIGN-OFF

By signing off, stakeholders agree that the problems and requirements detailed in this document accurately reflect the desired work. Architectural and implementation design will be based on the contents of this artifact.

*   **Client:** _________________________ (Name, Date)
*   **Consultant:** _________________________ (Name, Date)

---


## VIII. NEXT STEPS

**Primary Stakeholder & Decision Owner:** `Client` 

**Downstream Consumer:** `LLM_Planner` 

**Implementation Actions & Responsibilities (RACI):**

| # | Action | Responsible | Accountable | Consulted | Informed |
|:--|:---|:---|:---|:---|:---|
| 1 | Create/modify the `SPS`, `Request`, and `Concept` structural templates and procedural guidelines. | `LLM_Consultant` | `Client` | `LLM_Planner` | `LLM_Developer` |
| 2 | Develop the distinct system prompts for each stage of the consultancy workflow. | `LLM_Consultant` | `Client` | `LLM_Planner` | - |
| 3 | Develop the required ID-mapping mechanism/script. | `LLM_Developer` | `LLM_Planner` | `LLM_Consultant` | - |
| 4 | Update the `prompt_main.md` documentation with the new workflow description. | `LLM_Developer` | `Client` | `LLM_Consultant` | - |

---

## IX. CHANGELOG

*   **v1.0.0_i1:** Initial SPS creation documenting the problem of linking two templates.
*   **v1.0.0_i2:** Major revision to expand scope to the full three-artifact (`SPS` → `Request` → `Concept`) workflow, incorporating external feedback and requirements from T101A.
*   **v1.0.0_i3:** Final revision incorporating multiple rounds of external feedback. Globally replaced `SYSTEM_ARCHITECT`, renumbered all requirements, removed success metrics from scope, and added new requirements for template governance and automation hooks. Set `Client` as final Decision Owner, corrected Issue ownership, added Planner sign-off to Concept, renumbered all requirements, and clarified Next Steps with a RACI matrix.
