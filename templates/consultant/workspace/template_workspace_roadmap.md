---
artifact_type: 'ROADMAP'
initiative_id: '[INITIATIVE-ID]'
initiative_code: '[INITIATIVE-CODE]'
epic_id: '[EPIC-ID OR —]'
epic_code: '[EPIC-CODE OR —]'
phase: '[PHASE-NUMBER]'
version: '1.0.1'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
template_reference: 'prompt/templates/consultant/workspace/template_workspace_roadmap.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_roadmap.md'
ssot_sps_target: '[path/to/sps.md OR —]'
ssot_concept_target: '[path/to/concept.md OR —]'
phase0_plan: '[path/to/plan_<ID>-PH000.md OR —]'
phase1_plan: '[path/to/plan_<ID>-PH001.md OR —]'
parent_roadmap: '[path/to/parent/roadmap.md OR —]'
parent_activity: '[Activity ID in parent roadmap OR —]'
roadmap_changelog: '[path/to/changelog.md OR —]'
---

<!--
PURPOSE
  Standard template for ROADMAP workspace artifacts used by LLM_Consultant.

ROLE
  Roadmaps are planning + coordination tools:
    - Define Phase → Stream → Activity → Task structure
    - Provide Stream + Activity registers (toolable tables)
    - Provide concise objectives, deliverables, and success criteria

  Variant: Initiative Master Roadmap (“Thin Spine”)
    - Phase register + links + compact epic status snapshot
    - MUST remain thin; no Streams/Activities/Tasks
    - Points to phase plans / epic roadmaps for operational detail

BOUNDARIES (ANTI-DRIFT)
  - Roadmaps MUST NOT contain full F-RID/E-RID bodies or SSOT decision bodies.
  - Roadmaps MUST NOT become execution logs (use NOTES for session records).
  - Roadmaps SHOULD link to SSOT artifacts rather than duplicating content.

HEADING SEMANTICS (LOCKED)
  - `###` is reserved for Streams
  - `####` is reserved for Activities
  - Tasks are checklist items inside Activities
-->

# ROADMAP: [ID] ([CODE]) — Phase [#]: [Phase Title]

<!-- EXAMPLE: "ROADMAP: T104 (CWS) — Phase 0: Initiative Scaffolding & Standards" -->

## I. EXECUTIVE SUMMARY

**Purpose**: [1–3 sentences]

**Phase [#] Objective**: [1–2 sentences]

**Phase Exit Milestone**: **[Milestone Name]**
- [Binary statement of what must be true to exit this phase]

**Role Boundaries**:
- `LLM_Consultant`: [Responsibilities]
- `LLM_Researcher`: [If applicable]
- `LLM_Developer`: [If applicable]
- `Client`: [Decision authority + approvals]

**Locked Decisions (if any)**:
- [Decision bullet; include reference to NOTES entry if applicable]

---

## II. CONTEXT MATERIALS & PREREQUISITES

**SSOT / Governance (read-only unless explicitly scoped)**:
- `[path/to/sps.md]` — [Purpose]
- `[path/to/concept.md]` — [Purpose]

**Workspace Governance Rules**:
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md` — artifact role boundaries

**Structural Exemplars** (optional):
- `[path/to/exemplar/roadmap.md]` — [What it demonstrates]

---

## III. PHASE [#]: [PHASE TITLE]

**Objective**: [What this phase achieves; 1–2 sentences]

**Constraints**:
- [Constraint 1]
- [Constraint 2]

### Parallelism & Dependencies Standard (Roadmap)

- **Execution Mode**:
  - `PARALLEL`: may be executed concurrently (subject to `Depends On`)
  - `SEQUENTIAL`: intended ordering signal (still enforce via `Depends On` if required)
  - `GATED`: requires explicit exit evidence before dependent work starts
- **Depends On**: comma-separated list of prerequisite **Stream IDs** and/or **Activity IDs** (e.g., `1`, `1.1`, `2.2`). Use `—` if none.
- **Rule**: `Depends On` is the enforceable constraint; `Execution Mode` is the coordination intent.

### Stream Register

| Stream | Name | Objective | Status | Owner | Execution Mode | Depends On | Start | Target | Completion | Key Deliverables |
|:------|:-----|:----------|:-------|:------|:--------------|:----------|:------|:-------|:-----------|:----------------|
| 1 | **[Stream Name]** | [1-sentence objective] | `planned` | LLM_Consultant | PARALLEL | — | — | — | — | `[deliverable]` |

### Activity Register

| Stream | Activity | Name | Status | Owner | Execution Mode | Depends On | Start | Target | Completion | Deliverable(s) |
|:-------|:---------|:-----|:-------|:------|:--------------|:----------|:------|:-------|:-----------|:--------------|
| 1 | 1.1 | **[Activity Name]** | `planned` | LLM_Consultant | PARALLEL | — | — | — | — | `[path/to/deliverable.md]` |

---

### Stream 1: [STREAM TITLE]

**Objective**: [What this stream achieves; 1–2 sentences]
**Execution Mode**: [PARALLEL | SEQUENTIAL | GATED]
**Depends On**: [— | 1 | 1.1 | 2.2 | comma-separated]

**Exit Evidence (only if `Execution Mode = GATED`)**:
- [ ] [Binary gate condition]
- [ ] [Evidence link(s) recorded in Links Register]

#### Activity 1.1: [Activity Title]

**Purpose**: [Why this activity exists; what it unlocks]
**Status**: [Complete | Planned | In Progress | Blocked]
**Deliverable**: `[path/to/deliverable/file.md]` — [Brief description]

**Inputs Required**:
- [Input 1]: `[source file or dependency]`
- [Input 2]: `[source file or dependency]`

**Task List**:
1. [Task description]
2. [Task description]
3. [Task description]

**Success Criteria Checklist**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

<!-- Repeat Stream + Activity blocks as needed -->

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:----------|:-------|:-----|
| Roadmap (this file) | [Roadmap Name] | `[relative path]` |
| Notes | [Phase Notes] | `[relative path]` |
| Changelog | [Roadmap Changelog] | `[relative path]` |
| SSOT | [SPS] | `[relative path]` |
| SSOT | [Concept] | `[relative path]` |
| Proposal | [Phase Proposal] | `[relative path]` |
| Analysis | [Research Analysis] | `[relative path]` |
| Research | [Research Brief] | `[relative path]` |
| Research | [Research Report] | `[relative path]` |

---

## V. OPEN QUESTIONS REGISTER

| ID | Topic | Question | Owner | Status | Proposed Date | Resolved Date |
|:---|:------|:---------|:------|:-------|:--------------|:-------------|
| OQ-001 | [Topic] | [Question] | Client | Proposed | YYYY-MM-DD | — |

---

## VI. CHANGELOG

`[path/to/changelog_roadmap_<id>_phase<#>.md]`
