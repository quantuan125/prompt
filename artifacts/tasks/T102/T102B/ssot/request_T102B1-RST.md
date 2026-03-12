---
artifact_type: 'REQUEST'
initiative_id: 'T102'
epic_id: 'T102B'
feature_id: 'T102B1'
feature_code: 'RST'
version: '0.3.0'
date: '2026-02-10'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
workflow_variant: 'Full Request'
plan_reference: 'prompt/artifacts/tasks/T102/T102B/workspace/PH001/ST001/plan_T102B-PH001-ST001.md'
---

# REQUEST: Request Structural Template (RST) — T102B1

## I. EXECUTIVE SUMMARY

This Request specifies **T102B1 (RST)** — the normative structural template for Request artifacts within the T102 consultancy workflow. RST defines the canonical section structure, classification schema (Mandatory/Optional/Deferred), and content patterns for feature-level specification documents.

**Traceability**: This Request (v0.3.0) is structurally traceable to `T102B-STD-002 (Section Classification Standard)` and explicitly emphasizes inherited Initiative/Epic rules per `T102-STD-003 (Explicit Inheritance Model)` and `T102-STD-005 (ID Specification & Rules)`.

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
  - [G. Governance Standards](#g-governance-standards) — `[O]`
  - [H. Feature Guidance & Notes](#h-feature-guidance--notes) — `[O]`
  - [I. Research](#i-research) — `[O]`
  - [J. Story Index](#j-story-index) — `[O]`
  - [K. Acceptance Criteria](#k-acceptance-criteria) — `[M]`
- [IV. Approval Gate](#iv-approval-gate)
- [V. Appendix](#v-appendix)
- [VI. Changelog](#vi-changelog)

**Classification Legend**: `[M]` Mandatory | `[O]` Optional | `[D]` Deferred to Design

**Applicability rule** (Full Request): Story Index (Section J) is `[O]` by classification, but is **required** if `story_count > 1` per `T102B-STD-002-CLAUSE-004`.

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
| Section structure | Define canonical sections A-K for Request artifacts |
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
| OBJ-002 | Eliminate content duplication | T102B-QG-002 | No parallel FR\/IG sections in RST |
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

<!-- T102-STD-003 Explicit Inheritance Model -->
<!-- T102-STD-005 Reference Semantics: formal references in tables use `ID (Title)` -->

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
| SPS | `T102B` | Architecture | `T102B-STD-001 (Request Governance Snapshot Standard)`, `T102B-STD-002 (Section Classification Standard)`, `T102B-STD-003 (Story FR Deferral Standard)`, `T102B-STD-004 (Request Lite Specification)` |

Source locations:
- Initiative + Epic dossier: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` (see Epic `T102B` Section III.C.2)

---

### F. Feature Requirements `[M]`

<!-- ISO 29148 §5.2.4-5 Functional/Non-Functional Requirements -->

#### F.1 Assumptions

| ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref | Reference |
|:---|:------|:-------|:------------------|:-------|:------|:---------------|:--------------|:----------|
| `T102B1-ASSUM-001` | Existing Exemplar Sufficiency | `Pending` | Review T102A-SPSST and T810A1-PROMPT patterns for reusable structure signals | AC003 drafting | LLM_Consultant | Escalate as Issue and update structure guidance | `T102B1-CON-001` | `T102B-RES-001` |
| `T102B1-ASSUM-002` | Classification Granularity Sufficiency | `Pending` | Validate M/O/D sufficiency during AC003 and AC004 template/self-hosting checks | AC004 validation | LLM_Consultant | Escalate as Issue and propose classification variance ADR | `T102B1-CON-002` | `T102B-STD-002-CLAUSE-001` |

#### F.2 Constraints

| ID | Title | Description | Reference | Verification | Status | Note |
|:---|:------|:------------|:----------|:-------------|:-------|:-----|
| `T102B1-CON-001` | Markdown/YAML Only | RST SHALL use standard Markdown/YAML only | `T102B-CON-001` | Manual lint/readability review | `Draft` | Inherited constraint |
| `T102B1-CON-002` | No Story FR Mandate | RST SHALL NOT mandate story-level FR bodies | `T102B-CON-002` | Story Index contains navigation only | `Draft` | Addresses W2 |
| `T102B1-CON-003` | No Embedded ADR Bodies | RST SHALL NOT embed ADR bodies in Request artifacts | `T102B-CON-004` | Request sections contain references only | `Draft` | Link-don't-duplicate policy |

#### F.3 Functional Requirements

| ID | Title | Description | Reference | Verification | Status | Note |
|:---|:------|:------------|:----------|:-------------|:-------|:-----|
| `T102B1-FR-001` | Canonical Structure | RST SHALL define canonical section structure (A-K) with explicit purpose per section | `T102B-STD-002-CLAUSE-002` | Template contains all sections with purpose comments | `Draft` | Addresses W4/W5 |
| `T102B1-FR-002` | Section Classification | RST SHALL classify each section as Mandatory, Optional, or Deferred where applicable | `T102B-STD-002-CLAUSE-001` | Classification markers present in template | `Draft` | Addresses W4/P4 |
| `T102B1-FR-003` | FR/IG Consolidation | RST SHALL consolidate FR and IG content into unified requirement surfaces | `T102B-IG-002` | No standalone implementation-guidance major section exists | `Draft` | Addresses W1/P3 |
| `T102B1-FR-004` | Story Index Deferral | RST SHALL define Story Index navigation without story-level FR bodies | `T102B-STD-003-CLAUSE-001` | Section J contains index table only | `Draft` | Addresses W2/P2 |
| `T102B1-FR-005` | YAML Header Schema | RST SHALL define YAML header schema with required keys | `T102-IG-005` | Header schema documented with key definitions | `Draft` | Preserves S4 |
| `T102B1-FR-006` | Instructional Comments | RST SHALL include per-section instructional comments | `T102-CON-001` | Each section contains purpose/instruction guidance | `Draft` | Preserves S6 |
| `T102B1-FR-007` | RLITE Derivation Support | RST SHALL support Mandatory-only subset for RLITE derivation | `T102B-STD-004-CLAUSE-001` | Mandatory sections identifiable; subset remains under RLITE line target | `Draft` | Addresses P1 |
| `T102B1-FR-008` | Normative Guidance Separation | RST SHALL distinguish normative requirements from inline authoring guidance | `T102B-IG-002` | Guidance pattern is documented and consistently applied | `Draft` | Addresses W1/P3 |

#### F.4 Non-Functional Requirements

| ID | Title | Description | Reference | Verification | Status | Note |
|:---|:------|:------------|:----------|:-------------|:-------|:-----|
| `T102B1-NFR-001` | Parser Compatibility | RST SHALL be parsable by standard Markdown/YAML tooling | `T102B-CON-001` | No custom syntax/extensions are present | `Draft` | Compatibility |
| `T102B1-NFR-002` | Section Readability | RST section names SHALL be intuitive for non-technical stakeholders | `T102-QG-001` | Section headings are plain language | `Draft` | Usability |
| `T102B1-NFR-003` | ID Stability | RST SHALL preserve stable IDs across template versions | `T102-STD-005-CLAUSE-007` | Existing IDs remain stable across amendments | `Draft` | Maintainability |
| `T102B1-NFR-004` | Standards Alignment | RST SHALL align conceptually with ISO 29148, BABOK v3, SAFe patterns | `T102B-RES-001` | Industry mapping is present in supporting analysis | `Draft` | Standards alignment |

#### F.5 Interfaces

| ID | Title | Description | Reference | Verification | Status | Note |
|:---|:------|:------------|:----------|:-------------|:-------|:-----|
| `T102B1-IF-001` | SPS Intake Interface | SPS Feature bundle feeds RST-based Request authoring | `T102B-IF-001` | Intake fields map to Request header/core sections | `Draft` | Upstream contract |
| `T102B1-IF-002` | Request Output Interface | Approved Request output feeds Concept intake | `T102B-IF-002`, `T102B-IF-003` | Handoff fields remain complete for Concept | `Draft` | Downstream contract |
| `T102B1-IF-003` | RLITE Derivation Interface | RST Mandatory subset supports RLITE derivation | `T102B-STD-004-CLAUSE-002` | Mandatory-only subset can be extracted deterministically | `Draft` | Variant boundary |

---

### G. Governance Standards `[O]`

<!-- T102-STD-009-CLAUSE-004A STD index schema -->

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Governed By | Reference |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|:-------------|:------------|:----------|
| `T102B-STD-002` | **Section Classification Standard** | `Adopted` | Client | — | — | `T102B-STD-002 (Section Classification Standard)` | Validate Request structure against A-K + major section rules | `T102-STD-009`, `T102-STD-005` | `T102B-STD-003`, `T102B-STD-004` |

*Additional governing standards are inherited via Section E and referenced by ID (link-don't-duplicate).*

---

### H. Feature Guidance & Notes `[O]`

<!-- T102-STD-005 IID/NOTE semantics -->

#### Implementation Guidance (IG)

No feature-scoped IG entries are instantiated in this Request. Implementation guidance remains governed at Epic scope (`T102B-IG-*`) and is applied during template authoring in AC003.

#### Integration Guidance (INT)

No feature-scoped INT entries are populated in AC002.1. Integration guidance population is deferred to AC004 task `T102B-PH001-ST001-AC004-TK017`.

#### Notes

* **T102B1-NOTE-001 (Remediation Evidence Links)** — AC002 non-normative rationale and industry mapping remain in `proposal_T102B1-RST_non_normative.md`. Issues/Risks hosting architecture rationale is governed by `analysis_T102-RES-004_issues-risks-architecture.md` and corresponding report artifacts; this section captures references only (no duplicated policy prose).

---

### I. Research `[O]`

<!-- T102 research linkage pattern -->

| Research ID | Title | Summary | Report Link |
|:------------|:------|:--------|:------------|
| `T102B-RES-001` | Request Artifact Analysis | Industry standards comparison; W1-W7 weaknesses; P1-P8 proposals | [report_T102B-RES-001](../research/report/report_T102B-RES-001_request-artifact-analysis.md) |
| `T102B-RES-002` | Epic Foundation Assessment | E-RID candidates; governance gaps | [report_T102B-RES-002](../research/report/report_T102B-RES-002_epic-foundation-assessment.md) |
| `T102-RES-004` | Issues & Risks Architecture | Accepted cross-scope Issues/Risks architecture and promotion guidance supporting AC002.1 remediation | [report_T102-RES-004](../../consultant/research/report/report_T102-RES-004_issues-risks-architecture.md) |

---

### J. Story Index `[O]`

<!-- P2 Proposal: Story Index navigation only; FR bodies deferred to Design -->

| Story ID | Title | Purpose summary | Design Link |
|:---------|:------|:---------------|:------------|
| `T102B1-S01` | RST specification refinement | Canonicalize sections/classification and industry mapping; align to `T102B-STD-002` | [notes](../workspace/notes/PH001/ST001/notes_T102B-PH001-ST001-AC002.md) |
| `T102B1-S02` | RST template formalization | Author `request_structural_template.md` per approved specification | — |
| `T102B1-S03` | RST self-validation & retrofit | Retrofit this Request to v1.0 full and validate against template | — |
| `T102B1-S04` | Client approval gate | Obtain approval statement and close Stream ST001 | — |

*Story-level FRs and detailed ACs are deferred to Design phase per `T102B-CON-002` and `T102B-STD-003`.*

---

### K. Acceptance Criteria `[M]`

<!-- ISO 29148 Verification; Feature-level ACs -->

| ID | Criterion | Verification Method |
|:---|:----------|:--------------------|
| `T102B1-AC-001` | RST template file exists at `prompt/templates/request/request_structural_template.md` | File presence check |
| `T102B1-AC-002` | RST defines sections A-K with purpose and instructional content | Template inspection |
| `T102B1-AC-003` | Each RST section has explicit M/O/D classification | Classification markers present |
| `T102B1-AC-004` | RST contains no separate "Implementation Guidance" section | Template inspection |
| `T102B1-AC-005` | RST Section J implements Story Index pattern (no story FR bodies) | Template inspection |
| `T102B1-AC-006` | RST Mandatory sections enable RLITE <200 line subset | Line count verification |
| `T102B1-AC-007` | Industry alignment documented per section (ISO 29148, BABOK v3, SAFe) | Mapping table present in [proposal_T102B1-RST_non_normative.md](../workspace/proposal/T102B1/proposal_T102B1-RST_non_normative.md) |
| `T102B1-AC-008` | `request_T102B1-RST.md` retrofitted to RST structure (self-validation) | This Request conforms to approved RST |

---

## IV. APPROVAL GATE

<!-- T102B-STD-003 Gate Evidence Standard -->
<!-- T102B-STD-002-CLAUSE-004 Validation Rules -->

### A. Gate Checklist

- [ ] All `[M]` sections contain substantive content (no placeholder-only mandatory sections).
- [ ] Section classification markers applied consistently; no “Conditional” classification type (applicability is expressed as rules).
- [ ] Inherited Considerations table conforms to `T102-STD-003-CLAUSE-001` (schema) and `CLAUSE-003` (ID-only emphasis).
- [ ] Story Index is present and populated if `story_count > 1` per `T102B-STD-002-CLAUSE-004`.
- [ ] Governance Standards section follows `T102-STD-009-CLAUSE-004A` index schema.
- [ ] Feature Guidance & Notes section includes `IG` / `INT` / `NOTE` subheadings with non-normative content only.
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

## V. APPENDIX

### A. Amendment Log

Version history moved to `## VI. CHANGELOG` per `T102B-STD-002-CLAUSE-005`.

### B. References

| ID | Title | Path |
|:---|:------|:-----|
| REF-001 | T102B-RES-001 Report | `prompt/artifacts/tasks/T102/T102B/research/T102B-RES-001/report_T102B-RES-001_request-artifact-analysis.md` |
| REF-002 | T102B-RES-002 Report | `prompt/artifacts/tasks/T102/T102B/research/T102B-RES-002/report_T102B-RES-002_epic-foundation-assessment.md` |
| REF-003 | T102-RES-004 Report | `prompt/artifacts/tasks/T102/research/T102-RES-004/report_T102-RES-004_issues-risks-architecture.md` |
| REF-004 | T102B Epic Dossier | `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md` Section III.C.2 |
| REF-005 | ST001 Plan | `prompt/artifacts/tasks/T102/T102B/workspace/PH001/ST001/plan_T102B-PH001-ST001.md` |
| REF-006 | T102B-STD-002 | `prompt/artifacts/tasks/T102/T102B/standard/standard_T102B-STD-002_section-classification-standard.md` |
| REF-007 | T102B-STD-003 | `prompt/artifacts/tasks/T102/T102B/standard/standard_T102B-STD-003_story-fr-deferral-standard.md` |
| REF-008 | T102B-STD-004 | `prompt/artifacts/tasks/T102/T102B/standard/standard_T102B-STD-004_request-lite-specification.md` |
| REF-009 | AC002 Non-Normative Proposal | `prompt/artifacts/tasks/T102/T102B/workspace/PH000/proposal/proposal_T102B1-RST_non_normative.md` |

---

## VI. CHANGELOG

| Date | Requester | Affected Section | Summary |
|:-----|:----------|:-----------------|:--------|
| 2026-02-05 | LLM_Consultant | Initial | v0.1 created per AC001; lightweight structure using industry-standard SRS/BRD hybrid |
| 2026-02-06 | LLM_Consultant | AC002 | v0.2: `T102B-STD-002` canonicalization; inheritance table schema; Story Index applicability; industry mapping; gate section added |
| 2026-02-06 | LLM_Consultant | Cleanup | v0.2.1: moved non-normative authoring rules/analysis to proposal; Request tightened to `T102B-STD-002` section specs |
| 2026-02-10 | LLM_Consultant | AC002.1 | v0.3.0: A-K structure adopted; G/H/I/K remediated; Section F RID tables standardized; major sections renumbered; changelog section added |
