---
artifact_type: 'REQUEST'
initiative_id: 'T102'
epic_id: 'T102B'
feature_id: 'T102B1'
feature_code: 'RST'
version: '0.2.1'
date: '2026-02-06'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
workflow_variant: 'Full Request'
plan_reference: 'prompt/artifacts/tasks/T102/T102B/workspace/plan/plan_T102B-PH001-ST001.md'
---

# REQUEST: Request Structural Template (RST) — T102B1

## I. EXECUTIVE SUMMARY

This Request specifies **T102B1 (RST)** — the normative structural template for Request artifacts within the T102 consultancy workflow. RST defines the canonical section structure, classification schema (Mandatory/Optional/Deferred), and content patterns for feature-level specification documents.

**Traceability**: This Request (v0.2.1) is structurally traceable to `T102B-ADR-002 (Section Classification Standard)` and explicitly emphasizes inherited Initiative/Epic rules per `T102-ADR-003 (Explicit Inheritance Model)` and `T102-ADR-005 (ID Specification & Rules)`.

**Problem**: Current Request artifacts exhibit structural inconsistencies that create documentation overhead, blocking MVP delivery. Key issues include FR/IG duplication, premature story-level specification, and unclear section requirements.

**Solution Intent**: A standardized Request template that aligns with industry patterns (ISO 29148, BABOK v3, SAFe) while reducing authoring friction through explicit section classification and streamlined content patterns.

**Business Value**: Enables consistent, lightweight Request authoring that bridges SPS problem definition to Concept/Design solution exploration without documentation trap overhead.

---

## II. TABLE OF CONTENTS

- [I. Executive Summary](#i-executive-summary)
- [II. Table of Contents](#ii-table-of-contents)
- [III. Core Content](#iii-core-content)
  - [A. Problem Definition](#a-problem-definition) — `[M]`
  - [B. Scope](#b-scope) — `[M]`
  - [C. Business Objectives](#c-business-objectives) — `[M]`
  - [D. Stakeholders](#d-stakeholders) — `[O]`
  - [E. Inherited Considerations](#e-inherited-considerations) — `[M]`
  - [F. Feature Requirements](#f-feature-requirements) — `[M]`
  - [G. Governance Decisions](#g-governance-decisions) — `[O]`
  - [H. Issues & Risks](#h-issues--risks) — `[O]`
  - [I. Research & Notes](#i-research--notes) — `[O]`
  - [J. Story Index](#j-story-index) — `[O]`
- [IV. Acceptance Criteria](#iv-acceptance-criteria)
- [V. Approval Gate](#v-approval-gate)
- [VI. Appendix](#vi-appendix)

**Classification Legend**: `[M]` Mandatory | `[O]` Optional | `[D]` Deferred to Design

**Applicability rule** (Full Request): Story Index (Section J) is `[O]` by classification, but is **required** if `story_count > 1` per `T102B-ADR-002-CLAUSE-004`.

---

## III. CORE CONTENT

### A. Problem Definition `[M]`

<!-- ISO 29148 §5.2.1 Purpose; BABOK v3 Problem Statement -->

#### 1. Problem Statement

Request artifacts within T102 currently lack a normative structural standard, resulting in:

| ID | Weakness | Impact | Source |
|:---|:---------|:-------|:-------|
| W1 | FR/IG content duplication | Authoring overhead; maintenance burden | T102B-RES-001 |
| W2 | Story-level FRs at Request phase | Documentation trap blocking MVP delivery | T102B-RES-001 |
| W3 | RID repetition from Epic inheritance | Cognitive load; unnecessary verbosity | T102B-RES-001 |
| W4 | No mandatory/optional section distinction | All sections treated as required regardless of complexity | T102B-RES-001 |
| W5 | Excessive documentation weight | 700+ lines for feature-level spec exceeds SAFe recommendation | T102B-RES-001 |
| W6 | Version/iteration formality | Update friction vs. living document patterns | T102B-RES-001 |
| W7 | Missing current/future state sections | BRD best practice gap | T102B-RES-001 |

**Root Cause**: Absence of a governed structural template with explicit section classification, leading to ad-hoc Request authoring that inherits waterfall documentation patterns incompatible with Agile "just enough" principles.

#### 2. Desired Outcome

A normative Request Structural Template (RST) that:
- Defines canonical section structure for feature-level specification
- Classifies sections as Mandatory, Optional, or Deferred
- Eliminates FR/IG duplication through consolidated patterns
- Defers story-level FRs to Design phase via Story Index navigation
- Enables RLITE variant derivation (<200 lines)

#### 3. Stakeholder Concerns

| Stakeholder | Primary Concern | Success Criterion |
|:------------|:----------------|:------------------|
| Template Author | Structural clarity | Unambiguous section definitions |
| Request Author | Authoring efficiency | Reduced time-to-complete |
| Concept Author | Handoff completeness | Clear intake contract |
| Client | Governance control | Approval evidence requirements |

---

### B. Scope `[M]`

<!-- ISO 29148 §5.2.2 Scope; BABOK v3 Scope Definition -->

**Feature Identity**
- **Initiative**: `T102` (Consultancy Layer Architecture)
- **Epic**: `T102B` (REQUEST)
- **Feature**: `T102B1` (RST — Request Structural Template)

#### In Scope

| Item | Description |
|:-----|:------------|
| Section structure | Define canonical sections A-J for Request artifacts |
| Section classification | Establish Mandatory/Optional/Deferred taxonomy per section |
| YAML header schema | Define required header keys and validation rules |
| FR/IG consolidation | Design pattern eliminating content duplication |
| Story Index pattern | Navigation-only structure deferring story FRs to Design |
| Industry alignment | Conceptual mapping to ISO 29148, BABOK v3, SAFe patterns |
| Instructional content | Per-section authoring guidance embedded in template |

#### Out of Scope

| Item | Rationale | Covered By |
|:-----|:----------|:-----------|
| RLITE template | Separate feature with subset logic | T102B4 |
| Procedural guideline | Workflow rules, not structure | T102B2 (RSPG) |
| Manifest schema | Metadata lineage, not content structure | T102B3 |
| Validation tooling | Implementation, not specification | Future phase |
| Story-level FRs | Deferred to Design per P2 proposal | T102D (DESIGN) |

---

### C. Business Objectives `[M]`

<!-- SAFe Benefit Hypothesis; ISO 29148 Success Criteria -->

#### Benefit Hypothesis

We believe **consistent, lightweight Request authoring** will be achieved if **Template Authors and Request Authors** successfully use **RST section classification and streamlined patterns** to produce feature-level specifications that pass approval gates without documentation trap overhead.

#### Success Signals (MVP)

| ID | Objective | Aligned QG | Measurement |
|:---|:----------|:-----------|:------------|
| OBJ-001 | Reduce authoring overhead | T102B-QG-001 | RLITE derivation enables <200 line variant |
| OBJ-002 | Eliminate content duplication | T102B-QG-002 | No parallel FR/IG sections in RST |
| OBJ-003 | Enable completeness validation | T102B-QG-003 | Mandatory section checklist passes gate |
| OBJ-004 | Maintain industry alignment | T102B-DEP-002 | ISO 29148/BABOK v3 mapping documented |

---

### D. Stakeholders `[O]`

<!-- BABOK v3 Stakeholder Analysis -->

| Role | Persona | Responsibility | RACI |
|:-----|:--------|:---------------|:-----|
| Decision Owner | Client | Approves RST template and this Request | A |
| Template Owner | Client | Maintains RST template post-approval | A |
| Template Author | LLM_Consultant | Authors RST template specification | R |
| Request Author | LLM_Consultant | Consumes RST to produce Request artifacts | C |
| Concept Author | LLM_Consultant | Consumes approved Requests for Concept intake | I |

---

### E. Inherited Considerations `[M]`

<!-- T102-ADR-003 Explicit Inheritance Model -->
<!-- T102-ADR-005 Reference Semantics: formal references in tables use `ID (Title)` -->

This Request follows **explicit ID referencing**: higher-precedence rules are implicitly inherited, but only the most critical inherited items are explicitly emphasized here (ID references only; no upstream text restatement).

| Source Artifact | Scope ID | Category | Inherited Rule IDs |
|:--------------|:---------|:---------|:-------------------|
| SPS | `T102` | Assumptions | `T102-ASSUM-001 (LLM Generation)` |
| SPS | `T102` | Constraints | `T102-CON-001 (Format Requirements)`, `T102-CON-003 (Documentation Standards)` |
| SPS | `T102` | Quality Goals | `T102-QG-002 (End-to-End Traceability)` |
| SPS | `T102` | Dependencies | `T102-DEP-001 (Client Engagement)`, `T102-DEP-002 (Planner Integration)` |
| SPS | `T102` | Implementation Guides | `T102-IG-005 (Canonical Header)`, `T102-IG-007 (ID Standard)` |
| SPS | `T102` | Governances | `T102-STD-001 (Operating Model Standard)`, `T102-STD-003 (Inheritance Model Standard)`, `T102-STD-005 (ID Governance Standard)` |
| SPS | `T102B` | Assumptions | `T102B-ASSUM-001 (SPS Narrative Sufficiency)`, `T102B-ASSUM-002 (RLITE Adoption)`, `T102B-ASSUM-003 (Author Self-Assessment)` |
| SPS | `T102B` | Constraints | `T102B-CON-001 (No Custom Processors)`, `T102B-CON-002 (No Story FR Mandate)`, `T102B-CON-003 (Template Variant Boundary)`, `T102B-CON-004 (Decision Storage Boundary)` |
| SPS | `T102B` | Quality Goals | `T102B-QG-001 (Adoption Friction Reduction)`, `T102B-QG-002 (No Duplication Overhead)`, `T102B-QG-003 (Artifact Completeness)` |
| SPS | `T102B` | Dependencies | `T102B-DEP-001 (SPS Intake Alignment)`, `T102B-DEP-002 (Industry Standards)`, `T102B-IF-001 (SPS Intake Contract)`, `T102B-IF-002 (Approved Request Output)`, `T102B-IF-003 (Request Output Contract)` |
| SPS | `T102B` | Implementation Guides | `T102B-IG-001 (Section Classification)`, `T102B-IG-002 (FR/IG Consolidation)`, `T102B-IG-003 (Story Index Deferral)`, `T102B-IG-005 (Gate Evidence Checklist)`, `T102B-IG-006 (Inheritance Referencing)` |
| SPS | `T102B` | Governances | `T102B-STD-001 (Request Governance Snapshot Standard)`, `T102B-STD-002 (Workflow Typology Standard)`, `T102B-STD-003 (Gate Evidence Standard)`, `T102B-STD-004 (Section Classification Policy)` |
| SPS | `T102B` | Architecture | `T102B-ADR-001 (Request Architecture Standard)`, `T102B-ADR-002 (Section Classification Standard)`, `T102B-ADR-003 (Story FR Deferral Standard)`, `T102B-ADR-004 (Request Lite Specification)` |

Source locations:
- Initiative + Epic dossier: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (see Epic `T102B` Section III.C.2)

---

### F. Feature Requirements `[M]`

<!-- ISO 29148 §5.2.4-5 Functional/Non-Functional Requirements -->

#### F.1 Assumptions

| ID | Assumption | Validation Method |
|:---|:-----------|:------------------|
| `T102B1-ASSUM-001` | Existing Request exemplars provide sufficient pattern evidence | Review of T102A-SPSST, T810A1-PROMPT |
| `T102B1-ASSUM-002` | Section classification (M/O/D) is sufficient granularity | Pilot authoring feedback |

#### F.2 Constraints

| ID | Constraint | Rationale |
|:---|:-----------|:----------|
| `T102B1-CON-001` | RST SHALL use standard Markdown/YAML only | Inherits `T102B-CON-001` |
| `T102B1-CON-002` | RST SHALL NOT mandate story-level FR bodies | Inherits `T102B-CON-002`; addresses W2 |
| `T102B1-CON-003` | RST SHALL NOT embed ADR content | Inherits `T102B-CON-004` |

#### F.3 Functional Requirements

| ID | Requirement | Addresses | Acceptance Check |
|:---|:------------|:----------|:-----------------|
| `T102B1-FR-001` | RST SHALL define canonical section structure (A-J) with explicit purpose per section | W4, W5 | Template contains all sections with purpose comments |
| `T102B1-FR-002` | RST SHALL classify each section as Mandatory, Optional, or Deferred | W4, P4 | Classification marker present per section |
| `T102B1-FR-003` | RST SHALL consolidate FR and IG content into unified requirements sections | W1, P3 | No separate "Implementation Guidance" section exists |
| `T102B1-FR-004` | RST SHALL define Story Index pattern for navigation without story-level FR bodies | W2, P2 | Section J contains index table only |
| `T102B1-FR-005` | RST SHALL define YAML header schema with required keys | S4 (preserve) | Header schema documented with key definitions |
| `T102B1-FR-006` | RST SHALL include per-section instructional comments | S6 (preserve) | Each section contains `<!-- PURPOSE -->` and `*[Instructions]*` |
| `T102B1-FR-007` | RST SHALL support Mandatory-only subset for RLITE derivation | P1 | Mandatory sections identifiable; total enables <200 lines |
| `T102B1-FR-008` | RST SHALL distinguish normative requirements from inline authoring guidance using consistent formatting markers | W1, P3 | Guidance pattern documented and used consistently in template |

#### F.4 Non-Functional Requirements

| ID | Requirement | Quality Attribute | Acceptance Check |
|:---|:------------|:------------------|:-----------------|
| `T102B1-NFR-001` | RST SHALL be parsable by standard Markdown/YAML tooling | Compatibility | No custom syntax or extensions |
| `T102B1-NFR-002` | RST section names SHALL be intuitive for non-technical stakeholders | Usability | Plain language section headers |
| `T102B1-NFR-003` | RST SHALL preserve stable IDs across template versions | Maintainability | ID schema documented; no sequential numbering |
| `T102B1-NFR-004` | RST SHALL align conceptually with ISO 29148, BABOK v3, SAFe patterns | Standards Alignment | Industry mapping documented per section |

#### F.5 Interfaces

| ID | Interface | Direction | Contract |
|:---|:----------|:----------|:---------|
| `T102B1-IF-001` | SPS Feature Bundle | SPS → RST-based Request | Per `T102B-IF-001` |
| `T102B1-IF-002` | Approved Request Output | RST-based Request → Concept | Per `T102B-IF-002`, `T102B-IF-003` |
| `T102B1-IF-003` | RLITE Derivation | RST → RLITE | Mandatory sections subset |

---

### G. Governance Decisions `[O]`

<!-- T102-ADR-004 Decision Records Index -->

| GDR ID | Title | Status | Owner | Effective | Reference |
|:-------|:------|:-------|:------|:----------|:----------|
| — | — | — | — | — | — |

*No feature-level GDRs required at this stage. Epic-level standards (`T102B-STD-001` through `STD-004`) govern RST development.*

---

### H. Issues & Risks `[O]`

<!-- T102-ADR-007 Issues & Risks Schema -->

#### Issues

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:----------------|:--------------|
| `T102B1-ISSUE-001` | Story Index schema | Align Story Index table schema to `T102B-ADR-003-CLAUSE-001` and `T102B-ADR-002-CLAUSE-002` | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-06 | — | — |
| `T102B1-ISSUE-002` | Classification markers | Standardize `[M]`/`[O]`/`[D]` marker usage and applicability rules (no “Conditional” type) | LLM_Consultant | `OPEN` | `LOW` | 2026-02-06 | — | — |

#### Risks

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes |Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:----------------|:--------------|
| `T102B1-RISK-001` | Self-hosting circularity | `request_T102B1-RST.md` may drift from the final `request_structural_template.md` structure during iterative refinement | LLM_Consultant | `MONITORED` | `LOW` | 2026-02-05 | Keep `T102B-ADR-002` canonical; ensure Request v0.2+ remains traceable; re-check during AC003/AC004 | — |

---

### I. Research & Notes `[O]`

<!-- T102 Research Linkage Pattern -->

| Research ID | Title | Summary | Report Link |
|:------------|:------|:--------|:------------|
| `T102B-RES-001` | Request Artifact Analysis | Industry standards comparison; W1-W7 weaknesses; P1-P8 proposals | [report_T102B-RES-001](../research/report/report_T102B-RES-001_request-artifact-analysis.md) |
| `T102B-RES-002` | Epic Foundation Assessment | E-RID candidates; governance gaps | [report_T102B-RES-002](../research/report/report_T102B-RES-002_epic-foundation-assessment.md) |
Additional authoring rules and non-normative analysis from AC002 are maintained in:
- [proposal_T102B1-RST_non_normative.md](../workspace/proposal/T102B1/proposal_T102B1-RST_non_normative.md)

---

### J. Story Index `[O]`

<!-- P2 Proposal: Story Index navigation only; FR bodies deferred to Design -->

Applicability: This Request has `story_count = 4`, so Story Index is required per `T102B-ADR-002-CLAUSE-004`.

Definition: `story_count` is the number of Story rows in the Story Index table (excluding the header row).

This section is navigation only and SHALL NOT include detailed story-level FR bodies or story-level acceptance criteria (deferred to `T102D (DESIGN)` per `T102B-ADR-003`).

| Story ID | Title | Purpose summary | Design Link |
|:---------|:------|:---------------|:------------|
| `T102B1-S01` | RST specification refinement | Canonicalize sections/classification and industry mapping; align to `T102B-ADR-002` | [notes](../workspace/notes/PH001/ST001/notes_T102B-PH001-ST001-AC002.md) |
| `T102B1-S02` | RST template formalization | Author `request_structural_template.md` per approved specification | — |
| `T102B1-S03` | RST self-validation & retrofit | Retrofit this Request to v1.0 full and validate against template | — |
| `T102B1-S04` | Client approval gate | Obtain approval statement and close Stream ST001 | — |

*Story-level FRs and detailed ACs are deferred to Design phase per `T102B-CON-002` and `T102B-ADR-003`.*

---

## IV. ACCEPTANCE CRITERIA

<!-- ISO 29148 Verification; Feature-level ACs -->

| ID | Criterion | Verification Method |
|:---|:----------|:--------------------|
| `T102B1-AC-001` | RST template file exists at `prompt/templates/request/request_structural_template.md` | File presence check |
| `T102B1-AC-002` | RST defines sections A-J with purpose and instructional content | Template inspection |
| `T102B1-AC-003` | Each RST section has explicit M/O/D classification | Classification markers present |
| `T102B1-AC-004` | RST contains no separate "Implementation Guidance" section | Template inspection |
| `T102B1-AC-005` | RST Section J implements Story Index pattern (no story FR bodies) | Template inspection |
| `T102B1-AC-006` | RST Mandatory sections enable RLITE <200 line subset | Line count verification |
| `T102B1-AC-007` | Industry alignment documented per section (ISO 29148, BABOK v3, SAFe) | Mapping table present in [proposal_T102B1-RST_non_normative.md](../workspace/proposal/T102B1/proposal_T102B1-RST_non_normative.md) |
| `T102B1-AC-008` | `request_T102B1-RST.md` retrofitted to RST structure (self-validation) | This Request conforms to approved RST |

---

## V. APPROVAL GATE

<!-- T102B-STD-003 Gate Evidence Standard -->
<!-- T102B-ADR-002-CLAUSE-004 Validation Rules -->

### A. Gate Checklist

- [ ] All `[M]` sections contain substantive content (no placeholder-only mandatory sections).
- [ ] Section classification markers applied consistently; no “Conditional” classification type (applicability is expressed as rules).
- [ ] Inherited Considerations table conforms to `T102-ADR-003-CLAUSE-001` (schema) and `CLAUSE-003` (ID-only emphasis).
- [ ] Story Index is present and populated if `story_count > 1` per `T102B-ADR-002-CLAUSE-004`.
- [ ] Issues & Risks tables conform to `T102-ADR-007` schemas and enums.
- [ ] Industry alignment mapping is available (conceptual; no compliance matrix) in [proposal_T102B1-RST_non_normative.md](../workspace/proposal/T102B1/proposal_T102B1-RST_non_normative.md).
- [ ] No ADR bodies are embedded in this Request (reference-only per `T102B-CON-004`).

### B. Sign-off

| Field | Value |
|:------|:------|
| Approval Status | — |
| Approver | — |
| Role | — |
| Date | — |
| Notes | — |

---

## VI. APPENDIX

### A. Amendment Log

| Date | Requester | Affected Section | Summary |
|:-----|:----------|:-----------------|:--------|
| 2026-02-05 | LLM_Consultant | Initial | v0.1 created per AC001; lightweight structure using industry-standard SRS/BRD hybrid |
| 2026-02-06 | LLM_Consultant | AC002 | v0.2: ADR-002 canonicalization; inheritance table schema; Story Index applicability; industry mapping; gate section added |
| 2026-02-06 | LLM_Consultant | Cleanup | v0.2.1: moved non-normative authoring rules/analysis to proposal; Request tightened to ADR-002 section specs |

### B. References

| ID | Title | Path |
|:---|:------|:-----|
| REF-001 | T102B-RES-001 Report | `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md` |
| REF-002 | T102B-RES-002 Report | `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-002_epic-foundation-assessment.md` |
| REF-003 | T102B Epic Dossier | `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` Section III.C.2 |
| REF-004 | ST001 Plan | `prompt/artifacts/tasks/T102/T102B/workspace/plan/plan_T102B-PH001-ST001.md` |
| REF-005 | T102B-ADR-002 | `prompt/artifacts/tasks/T102/T102B/standards/T102B-ADR-002_section-classification-standard.md` |
| REF-006 | T102B-ADR-003 | `prompt/artifacts/tasks/T102/T102B/standards/T102B-ADR-003_story-fr-deferral-standard.md` |
| REF-007 | T102B-ADR-004 | `prompt/artifacts/tasks/T102/T102B/standards/T102B-ADR-004_request-lite-specification.md` |
| REF-008 | AC002 Non-Normative Proposal | `prompt/artifacts/tasks/T102/T102B/workspace/proposal/T102B1/proposal_T102B1-RST_non_normative.md` |
