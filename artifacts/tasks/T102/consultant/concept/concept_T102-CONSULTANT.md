---
artifact_type: 'CONCEPT'
initiative_id: 'T102'
initiative_code: 'CONSULTANT'
version: '1.1.0'
date: '2026-01-09'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

## III. CORE CONTENT

### A. Identity & Operating Rules
<!--
- Canonical header + links to governing GDRs/ADRs (inheritance table: "link-don't-duplicate").  <!-- T102-GDR-002/003/004/005
- Scope & boundaries (what lives in SPS vs Request vs Design); change log.
-->

### B. Decision System (ADR/STD Compendium)

#### 1. Initiative STD Index

| STD ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-STD-001` | Consultancy Operating Model | — | Proposed | Client | 2025-09-18 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-001_consultancy-operating-model.md` |
| `T102-STD-002` | Canonical YAML Header | — | Proposed | Client | 2025-09-14 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-002_canonical-yaml-header.md` |
| `T102-STD-003` | Explicit Inheritance Model | — | Proposed | Client | 2025-09-14 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-003_explicit-inheritance-model.md` |
| `T102-STD-004` | Specification Standard & Guideline | — | Proposed | Client | — | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_decision-records-standard.md` |
| `T102-STD-005` | ID Specification & Rules | — | Proposed | Client | — | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-005_id-specification-rules.md` |
| `T102-STD-006` | Research Artifacts Index | — | Proposed | Client | 2025-10-12 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md` |
| `T102-STD-007` | Issues & Risks Index | — | Proposed | Client | 2026-01-01 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-007_issues-risks-index.md` |
| `T102-STD-008` | Organisation Baseline Index | — | Proposed | Client | 2026-01-12 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-008_organisation-baseline-index.md` |
| `T102-STD-009` | Governance Standards Specification | — | Proposed | Client | — | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md` |

#### 2. Epic STD Index

##### i. `T102A` Epic: `SPS` — Synthesized Problem Statement Workflow

| STD ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A-STD-001` | Governance & Roadmap Snapshot | — | Proposed | Client | 2026-01-11 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102A-STD-001_governance-roadmap-snapshot.md` |
| `T102A-STD-002` | Feature Register Index | — | Proposed | Client | 2026-01-11 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102A-STD-002_feature-register-index.md` |

##### ii. `T102B` Epic: `REQUEST` — Request Workflow

| STD ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102B-STD-001` | Request Architecture Standard | — | Proposed | LLM_Consultant | — | — | `prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-001_request-architecture-standard.md` |
| `T102B-STD-002` | Section Classification Standard | — | Proposed | LLM_Consultant | — | — | `prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md` |
| `T102B-STD-003` | Story FR Deferral Standard | — | Proposed | LLM_Consultant | — | — | `prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-003_story-fr-deferral-standard.md` |
| `T102B-STD-004` | Request Lite Specification | — | Proposed | LLM_Consultant | — | — | `prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-004_request-lite-specification.md` |

##### iii. `T102C` Epic: `CONCEPT` — Concept Workflow

| STD ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102C-STD-001` | Concept Architectural Framework | — | Proposed | — | 2025-09-28 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102C-STD-001_concept-architectural-framework.md` |

#### 3. Feature STD Index

| STD ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102A-SPSST-STD-0001` | Approvals in body | — | Accepted | Client | — | — | `prompt/artifacts/tasks/T102/consultant/standards/T102A-SPSST-STD-0001_approvals-in-body.md` |

### C. Readiness Snapshot (Lean, manual)
<!-- 
- **A. Roll-up Table** (Initiative/Epics/Features: State | Ready? | Top blockers | Next gate | Updated_at)
- **B. DoR Checklists (brief)** per tier (links to Request/Design for evidence)
- **C. Notes & Overrides** (Client approvals recorded with ID)
-->
### D. Handoff Snapshot (Authoritative)
<!-- 
- **A. Package Manifest** (immutable IDs, doc versions/SHAs)
- **B. Acceptance Signals** (Client sign-off, gate approvals)
- **C. Completeness Checklist** (ADR accepted; FRs approved; risks linked)
- **D. Links** (SPS/Request/Design anchors; no copy-paste)
-->
### E. Registers 
<!-- 
- Risks/Assumptions/Dependencies registers (pointer-based; no duplication)
-->
#### 1. Feature Register

#### 2. Design Register
| Epic ID | Feature ID | Story ID | Design Log | Status | Notes |
| :------ | :--------- | :------- | :--------- | :----- | :---- |
| T102A | T102A-SPSST | T102A-SPSST-S1 | ../design/design_T102A-SPSST-S1.md | review | … |
| T102A | T102A-SPSST | T102A-SPSST-S3 | ../design/design_T102A-SPSST-S3.md | review | … |
| T102A | T102A-SPSST | T102A-SPSST-S4 | ../design/design_T102A-SPSST-S4.md | review | … |

#### 3. Research Artifacts Register

| Scope | Scope ID | Research ID | Title | Summary | Reference | Brief | Report | Source |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Initiative | `T102` | `T102-RES-001` | **Research Integration Governance** | Established three-tier placement strategy, LLM quality control framework, RES-### ID system; recommended dedicated Epic T102E for implementation | `T102-ISSUE-005`, `T102-GDR-006`, `T102-GDR-007` | [brief](../research/brief/brief_T102-CONSULTANT_research-integration-workflow_v1.0.0.md) | [report](../research/report/report_T102-CONSULTANT_research-integration-workflow_v1.0.0.md) | `../sps/sps_T102-CONSULTANT_v1.1.0.md#research--notes` |
| Initiative | `T102` | `T102-RES-002` | **Roadmap Viability** | Confirmed governance snapshot approach aligns with PRINCE2/PMI/SAFe standards; validated hybrid model with governance milestones in SPS and operational plans external | `T102A-GDR-001`, `T102C-GDR-003`, `T102C-GDR-005` | [brief](../research/brief/brief_T102-CONSULTANT_roadmap-viability_v1.0.0.md) | [report](../research/report/report_T102-CONSULTANT_roadmap-viability_v1.0.0.md) | `../sps/sps_T102-CONSULTANT_v1.1.0.md#research--notes` |
| Epic | `T102A` | `T102A-RES-001` | **SPS Workflow Optimization** | Validated emergent governance freeze, handoff criteria, procedural workflows; established 10-point readiness checklist | `T102A-ISSUE-002`, `T102A-ISSUE-003`, `T102A-GDR-002` | [brief](../research/brief/brief_T102A-SPS_sps-workflow-optimization_v1.0.0.md) | [report](../research/report/report_T102A-SPS_sps-workflow-optimization_v1.0.0.md) | `../sps/sps_T102-CONSULTANT_v1.1.0.md#vi-epic-research--notes` |
| Epic | `T102C` | `T102C-RES-001` | **Handoff Aggregation** | Validated T102C-GDR-003 and T102C-GDR-005 handoff authority and readiness aggregation patterns | `T102C-GDR-003`, `T102C-GDR-005`, `T102C-NOTE-003` | [brief](../research/brief/brief_T102C-CONCEPT_handoff-aggregation_v1.0.0.md) | [report](../research/report/report_T102C-CONCEPT_handoff-aggregation_v1.0.0.md) | `../sps/sps_T102-CONSULTANT_v1.1.0.md#vi-epic-research--notes` |



### F. Integration & Interfaces
<!-- 
- Planner consumption notes (schema, payload outline), cross-traceability rules.
-->


### G. Governance

<!-- 
- Local GDRs for Concept (e.g., T102C-GDR-003/005 once accepted) + change control.
-->
