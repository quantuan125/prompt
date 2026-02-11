---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'plan_authoring'
version: '1.4.0'
date: '2026-02-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/workspace/README.md'
---

# Plan Procedural Guideline (Consultant Workspace)

## I. PURPOSE

Define the **authoring rules** for PLAN workspace artifacts so they remain toolable, consistent across initiatives, and resistant to drift.

This guideline is intended to be referenced by initiative plans (e.g., `T104`) and later integrated more deeply into the workspace plan templates.

---

## II. CORE SEMANTICS (LOCKED)

### A. Timeline Hierarchy

- Phase → Stream → Activity → Task

---

## III. REGISTER RULES

### A. Status enums (Registers)

- Stream Register `Status` MUST be one of: `planned`, `deferred`, `completed`, `cancelled`.
- Activity Register `Status` MUST be one of: `planned`, `deferred`, `completed`, `cancelled`.
- In all register tables, `Status` values MUST be wrapped in backticks.

### B. Status enums (Task Registers)

- Task Register `Status` MUST be one of: `planned`, `deferred`, `completed`, `cancelled`, `failed`.
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
- `Action` MUST be updated with a concise outcome statement when the task moves to `completed`, `deferred`, `cancelled`, or `failed`.
- Rule of thumb: treat `Status` as lifecycle; treat `Action` as evidence trail.

### C. Activity completion rule

An Activity is considered done only when:
1) its Success Criteria Checklist is verified, AND
2) its Task Register rows are updated to a terminal status (`completed`, `deferred`, `cancelled`, or `failed`) with a non-empty `Action`.

---

## V. STREAM AUTHORING RULES

### A. Stream Context (Option A)

Each Stream SHOULD include a `Context` block listing only the repo-relative paths that Activities in that Stream are expected to touch.

Notes:
- Section II of a plan can list general context inputs; do not duplicate non-touched paths in Stream Context blocks.
- If a Stream has no file touches (e.g., “Validation-only”), state `Context: none (validation-only)`.

### B. Parallelism & Dependencies Standard (Plan)

- **Execution Mode**:
  - `PARALLEL`: may be executed concurrently (subject to `Depends On`)
  - `SEQUENTIAL`: intended ordering signal (still enforce via `Depends On` if required)
  - `GATED`: requires explicit exit evidence before dependent work starts
- **Depends On**:
  - comma-separated list of prerequisite **Stream IDs** and/or **Activity IDs** (e.g., `1`, `1.1`, `2.2`)
  - use `—` if none
- **Rule**: `Depends On` is the enforceable constraint; `Execution Mode` is the coordination intent.

---

## VI. GATE RULES

### A. Purpose

A Gate is a named checkpoint in the plan where work pauses for stakeholder review
before dependent work proceeds. Gates produce no deliverable — they produce a
review decision.

### B. Gate ID Format

`<Activity-ID>-GATE-###` (e.g., `T102-PH001-ST001-AC006-GATE-001`)

### C. Gate Fields

Every Gate MUST include:
- **Entry Criteria**: What must be ready for the gate review
- **Reviewer**: Role responsible for the review decision
- **Exit Criteria**: What approval/evidence is needed to pass

### D. Placement in Task Register

Gates appear in the Task Register as a special row type:
- Status enum: `planned` (awaiting review), `completed` (gate passed), or `failed` (gate failed)
- Gates MUST be listed in dependency order alongside tasks
- Downstream tasks that depend on the gate MUST use `Depends On: GATE-###`

### E. Gate vs Task Distinction

- A **Task** produces a deliverable (artifact, update, code)
- A **Gate** produces a review decision (pass/fail)
- Gates MUST NOT be used as tasks; tasks MUST NOT be used as gates

### F. Phase-Level Gates

Phase-level gates govern entry into, or conformance claims within, an entire phase or a named subset of streams. They differ from activity-level gates in scope:

- **ID Format**: `<Phase-ID>-GATE-###` (e.g., `T102A-PH001-GATE-001`)
- **Placement**: In the **Phase Plan** file, as a dedicated section (e.g., "## Phase Gates") placed after the Stream Register and before the Activity Register. Phase gates MUST NOT be placed inside stream or activity plans.
- **Scope**: A phase gate governs all streams and activities within the phase, unless the gate's Entry Criteria explicitly names a subset of streams.
- **Enforcement mode**: The Entry Criteria text MUST specify whether the gate is:
  - **Blocking**: No work in the governed scope may begin until the gate passes.
  - **Conformance**: Work in the governed scope may proceed (drafting, analysis, review), but outputs MUST NOT be treated as conformant to the gated precondition until the gate passes. Conformance claims, final approvals, and handoff readiness checks are blocked.
- **Fields**: Phase gates use the same three required fields as activity gates: Entry Criteria, Reviewer, Exit Criteria.
- **Interaction with activity gates**: Phase gates and activity gates may coexist. Activity gates govern local task sequencing; phase gates govern cross-stream preconditions. If both apply, the more restrictive gate governs.

---

## VIII. TEMPLATE INVENTORY

The following templates are available for PLAN artifacts. Each template defines the required structure for its planning level. Authors MUST use the appropriate template when creating new plan files.

### A. Phase Plan Template

- **Template**: `prompt/templates/consultant/workspace/template_workspace_plan_phase.md`
- **What**: Defines the required structure for phase-level plan files.
- **Why**: Ensures consistent section ordering, register schemas, and frontmatter across all phase plans.
- **When**: Use when creating a new phase plan (e.g., `plan_T104-PH001.md`).
- **How**: Copy the template, fill in frontmatter placeholders, populate sections per this guideline's rules.

### B. Stream Plan Template

- **Template**: `prompt/templates/consultant/workspace/template_workspace_plan_stream.md`
- **What**: Defines the required structure for stream-level plan files, including contract-level activity sections.
- **Why**: Ensures activity contracts are consistent (Purpose/Deliverable/Scope/Task Register/Success Criteria).
- **When**: Use when creating a new stream plan (e.g., `plan_T104-PH001-ST005.md`).
- **How**: Copy the template, fill in frontmatter, define activities at contract level per §IV rules.

### C. Activity Plan Template (Skeleton)

- **Template**: `prompt/templates/consultant/workspace/template_workspace_plan_activity.md`
- **What**: Defines the required structure for standalone activity plan files with task-level detail.
- **Why**: Provides consistent decomposition structure when activities exceed stream plan contract-level depth.
- **When**: Use when an activity has ≥5 tasks, requires detailed step decomposition, or exceeds contract-level scope. See trigger rule in template.
- **How**: Copy the template, fill in frontmatter, decompose tasks with optional informal Steps.

### D. Directory & Naming Conventions

- All plan files follow the naming and directory placement rules defined in:
  `prompt/artifacts/tasks/T104/workspace/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (P-STD-004 proposal)

---

## IX. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.3.0 | 2026-02-11 | Amendment | Added §VI.F Phase-Level Gates authoring rule: ID format, placement, scope, enforcement mode (blocking vs conformance), interaction with activity gates |
| v1.4.0 | 2026-02-11 | Update | Added Template Inventory section referencing PLAN templates; corrected status enum spelling (`deferred`) |
