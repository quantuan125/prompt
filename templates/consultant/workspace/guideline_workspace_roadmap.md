---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'roadmap_authoring'
version: '1.1.0'
date: '2026-02-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/workspace/template_workspace_roadmap.md'
---

# Roadmap Procedural Guideline (Consultant Workspace)

## I. PURPOSE

Define the **authoring rules** for ROADMAP workspace artifacts so they remain toolable, consistent across initiatives, and resistant to drift.

This guideline is intended to be referenced by initiative roadmaps (e.g., `T104`) and later integrated more deeply into `template_workspace_roadmap.md`.

---

## II. CORE SEMANTICS (LOCKED)

### A. Timeline Hierarchy

- Phase → Stream → Activity → Task

### B. Markdown Heading Semantics

- `###` is reserved for **Streams**
- `####` is reserved for **Activities**
- Tasks live inside an Activity as either:
  - a **Task Register** (preferred), and/or
  - a short checklist (only when a full Task Register is unnecessary)

### C. Roadmap Types (Thin Spine vs Phase Execution)

Roadmaps may be authored in one of two common shapes:

1) **Initiative Master Roadmap (“Thin Spine”)**
   - Purpose: a phase register + links + compact epic status snapshot (navigation spine).
   - MUST remain thin: no Stream/Activity/Task execution detail.
   - Points to phase plans and/or epic roadmaps for operational detail.

2) **Phase Roadmap / Phase Plan (Execution Surface)**
   - Purpose: operational sequencing for a specific phase.
   - MAY include Stream Register, Activity Register, and Activity Task Registers.
   - Uses the Phase → Stream → Activity → Task hierarchy for toolable coordination.

**Recommended frontmatter pointers (optional)**:
- `procedural_guideline`: canonical pointer to this guideline.
- `ssot_sps_target`, `ssot_concept_target`: pointers to SSOT surfaces (when applicable).

---

## III. REGISTER RULES

### A. Status enums (Registers)

- Stream Register `Status` MUST be one of: `planned`, `deferred`, `completed`, `cancelled`.
- Activity Register `Status` MUST be one of: `planned`, `deferred`, `completed`, `cancelled`.
- In all register tables, `Status` values MUST be wrapped in backticks.

### B. Status enums (Task Registers)

- Task Register `Status` MUST be one of: `planned`, `deferred`, `completed`, `cancelled`.
- In all Task Register tables, `Status` values MUST be wrapped in backticks.

---

## IV. ACTIVITY AUTHORING RULES

### A. Required Activity Fields

Every Activity SHOULD include:
- **Purpose**
- **Deliverable**
- **Scope** (what is in-scope; include “Excludes” if helpful)
- **Inputs Required** (only when there are explicit dependencies beyond `Depends On`)
- **Task Register**
- **Success Criteria Checklist**

### B. Task Register schema

Every Activity that requires trackable work MUST include a Task Register with columns:

`Task ID | Description | Status | Action`

Rules:
- `Action` MUST be set to `—` when no action has started.
- `Action` MUST be updated with a concise outcome statement when the task moves to `completed`, `deferred`, or `cancelled`.
- Rule of thumb: treat `Status` as lifecycle; treat `Action` as evidence trail.

### C. Activity completion rule

An Activity is considered done only when:
1) its Success Criteria Checklist is verified, AND
2) its Task Register rows are updated to a terminal status (`completed`, `deferred`, or `cancelled`) with a non-empty `Action`.

---

## V. STREAM AUTHORING RULES

### A. Stream Context (Option A)

Each Stream SHOULD include a `Context` block listing only the repo-relative paths that Activities in that Stream are expected to touch.

Notes:
- Section II of a roadmap can list general context inputs; do not duplicate non-touched paths in Stream Context blocks.
- If a Stream has no file touches (e.g., “Validation-only”), state `Context: none (validation-only)`.

### B. Parallelism & Dependencies Standard (Roadmap)

- **Execution Mode**:
  - `PARALLEL`: may be executed concurrently (subject to `Depends On`)
  - `SEQUENTIAL`: intended ordering signal (still enforce via `Depends On` if required)
  - `GATED`: requires explicit exit evidence before dependent work starts
- **Depends On**:
  - comma-separated list of prerequisite **Stream IDs** and/or **Activity IDs** (e.g., `1`, `1.1`, `2.2`)
  - use `—` if none
- **Rule**: `Depends On` is the enforceable constraint; `Execution Mode` is the coordination intent.

---

## VI. TEMPLATE INVENTORY

### A. Roadmap Template

- **Template**: `prompt/templates/consultant/workspace/template_workspace_roadmap.md`
- **What**: Defines the required structure for ROADMAP workspace artifacts.
- **Why**: Ensures consistent heading semantics, register schemas, and anti-drift boundaries.
- **When**: Use when creating any new roadmap file (initiative master or phase execution).
- **How**: Copy the template. For initiative master roadmaps ("thin spine"), keep Phase Register + Links only — no Stream/Activity/Task detail. For phase execution roadmaps, populate Stream/Activity sections per §IV rules.

### B. Roadmap Types

Two shapes are defined (per §II.C):
1. **Initiative Master Roadmap ("Thin Spine")**: Phase Register + Links + compact epic status. MUST remain thin.
2. **Phase Roadmap / Phase Plan (Execution Surface)**: Stream/Activity/Task detail for a specific phase.

### C. Directory & Naming Conventions

- Roadmap files follow the naming and placement rules defined in:
  `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (P-STD-004 proposal)

---

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-01-24 | Initial | Roadmap procedural guideline created |
| v1.1.0 | 2026-02-11 | Update | Added Template Inventory section and P-STD-004 reference; corrected status enum spelling (`deferred`) |
