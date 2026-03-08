---
artifact_type: 'PLAN'
planning_level: 'PHASE'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
phase: '[PHASE-NUMBER]'
version: '1.0.1'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_roadmap: '[path/to/initiative/roadmap.md OR —]'
ssot_sps_target: '[path/to/sps.md OR —]'
ssot_concept_target: '[path/to/concept.md OR —]'
---

<!--
ANTI-DRIFT: Phase plans MUST NOT contain stream-level task registers or activity-level step decomposition.
Link to stream plans for execution detail.
-->

# PLAN: [ID] ([CODE]) — Phase [#]: [Phase Title]

<!--
Section I guidance: Phase plan MUST remain at contract level. No task registers. No execution detail.
-->
## I. EXECUTIVE SUMMARY

**Purpose**: [1–3 sentences]

**Phase [#] Objective**:
1) [Objective 1]
2) [Objective 2]

**Entry Criteria**:
- [Criterion 1]
- [Criterion 2]

**Exit Milestone**: **[Milestone Name]**

**Locked Decisions**:
- [Decision ID]: [Decision summary]

---

<!--
Section II guidance: List SSOT references, governance rules, and structural exemplars only.
-->
## II. CONTEXT MATERIALS & PREREQUISITES

**SSOT / Governance (read-only unless explicitly scoped)**:
- `[path/to/sps.md]` — [Purpose]
- `[path/to/concept.md]` — [Purpose]

**Workspace Governance Rules**:
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md` — artifact role boundaries

**Structural Exemplars** (optional):
- `[path/to/exemplar/plan.md]` — [What it demonstrates]

---

## III. PHASE [#]: [PHASE TITLE]

**Objective**: [What this phase achieves; 1–2 sentences]

<!-- Use canonical P-STD-002 work-item states per guideline_workspace_plan.md §III.A -->
### Stream Register

| Stream | ID | Name | Execution Mode | Depends On | Status | Key Deliverables |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | `T###-PH###-ST###` | [Stream Name] | [PARALLEL\|SEQUENTIAL\|GATED] | — | `planned` | [Deliverable list] |

<!--
ANTI-DRIFT:
  - Stream plans are SSOT for Activity status, dependencies, deliverables, and activity-plan references.
  - Phase plans carry a snapshot index only (navigation + reporting).
-->
### Activity Snapshot Index

**Activity Snapshot As-Of**: YYYY-MM-DD

| Stream | Activity | Activity ID | Name | Status (snapshot) | Owner | Source (Stream Plan) |
|:--|:--|:--|:--|:--|:--|:--|
| 1 | AC001 | `T###-PH###-ST###-AC###` | [Activity Name] | `planned` | LLM_Consultant | `[path/to/stream/plan.md]` |

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | [Phase Plan] | `[relative path]` |
| Roadmap | [Parent Roadmap] | `[relative path]` |
| Notes | [Phase Notes Register] | `[relative path]` |
| SSOT | [SPS] | `[relative path]` |
| SSOT | [Concept] | `[relative path]` |

---

## V. OPEN QUESTIONS REGISTER

| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:---|:------|:---------|:------|:-------|:--------------|:-------------|
| OQ-001 | [Topic] | [Question] | Client | Proposed | YYYY-MM-DD | — |

---

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.1 | YYYY-MM-DD | Amendment | Stream register status comment updated to defer to `P-STD-002` canonical work-item states. |
| v1.0.0 | YYYY-MM-DD | Initial | Phase plan created |
