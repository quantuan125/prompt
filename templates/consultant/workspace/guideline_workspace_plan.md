---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'plan_authoring'
version: '1.6.0'
date: '2026-02-14'
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

### C. Register Authority (Anti-Drift)

To prevent duplicate “live registers” from drifting:

- **Stream Plans are SSOT** for Activity truth:
  - Activity `Status`, `Depends On`, deliverable contract, and activity-plan link live in the **Stream Plan**.
- **Phase Plans carry a snapshot index only** (not a second live register):
  - Phase plans MUST use an **Activity Snapshot Index** with an explicit `As-Of` date.
  - Phase snapshot rows MUST NOT be used to author or enforce dependencies.
  - If a consumer needs Activity dependencies or contract detail, they MUST navigate to the Stream plan.

Minimum Phase Activity Snapshot Index requirements:
- MUST include: `**Activity Snapshot As-Of**: YYYY-MM-DD`
- MUST use a reduced schema (navigation/reporting only), e.g.:
  - `Stream | Activity | Activity ID | Name | Status (snapshot) | Owner | Source (Stream Plan)`
- MUST NOT include: `Depends On` (dependencies are authored/enforced at Stream plan level)

---

## IV. ACTIVITY AUTHORING RULES

### A. Required Activity Fields

Every Activity SHOULD include:
- **Purpose**
- **Deliverable**
- **Scope** (what is in-scope; include “Excludes” if helpful)
- **Inputs Required** (only when there are explicit dependencies beyond `Depends On`)
- **Task Register** (in the Stream plan when no standalone Activity Plan exists; otherwise in the Activity Plan)
- **Success Criteria Checklist**

### B. Task Register schema

Every Activity that requires trackable work MUST include a Task Register (in either the Stream plan Activity section or a standalone Activity Plan) with columns:

`Task ID | Description | Status | Action`

Rules:
- `Action` MUST be set to `—` when no action has started.
- `Action` MUST be updated with a concise outcome statement when the task moves to `completed`, `deferred`, `cancelled`, or `failed`.
- Rule of thumb: treat `Status` as lifecycle; treat `Action` as evidence trail.

### C. Activity completion rule

An Activity is considered done only when:
1) its Success Criteria Checklist is verified, AND
2) its Task Register rows are updated to a terminal status (`completed`, `deferred`, `cancelled`, or `failed`) with a non-empty `Action`.

### D. Standalone Activity Plans (Linking + Minimum Stream Detail)

Some Activities (and Sub-Activities) may have dedicated Activity Plan files using:
`prompt/templates/consultant/workspace/template_workspace_plan_activity.md`.

**Rule (minimum stream detail)**: Even when a dedicated Activity Plan exists, the Stream plan MUST retain a minimal “contract stub” so a reader understands the work without opening the Activity Plan.

Minimum contract stub in the Stream plan Activity section:
- **Purpose**
- **Deliverable**
- **Scope**
- **Activity Plan** link (path)
- **Success Criteria Checklist (summary)** (max 5 checkboxes recommended)

Anti-drift boundary:
- Detailed task decomposition MUST live in the dedicated Activity Plan (do not duplicate a full Task Register in the Stream plan when an Activity Plan exists).

**Canonical link location**:
- For Activities (`AC00x`): the Stream plan **Activity Register `Reference`** cell is the canonical link location.
  - The Activity section MAY repeat the path as `**Activity Plan**: ...`, but it MUST match the register `Reference`.
- For Sub-Activities (`AC00x.x`): because Sub-Activities have no register row, the Sub-Activity section MUST carry the link as `**Sub-Activity Plan**: ...` when a plan exists.

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
- **Placement**: In the **Phase Plan** file, as a dedicated section (e.g., "## Phase Gates") placed after the Stream Register and before the Activity Snapshot Index. Phase gates MUST NOT be placed inside stream or activity plans.
- **Scope**: A phase gate governs all streams and activities within the phase, unless the gate's Entry Criteria explicitly names a subset of streams.
- **Enforcement mode**: The Entry Criteria text MUST specify whether the gate is:
  - **Blocking**: No work in the governed scope may begin until the gate passes.
  - **Conformance**: Work in the governed scope may proceed (drafting, analysis, review), but outputs MUST NOT be treated as conformant to the gated precondition until the gate passes. Conformance claims, final approvals, and handoff readiness checks are blocked.
- **Fields**: Phase gates use the same three required fields as activity gates: Entry Criteria, Reviewer, Exit Criteria.
- **Interaction with activity gates**: Phase gates and activity gates may coexist. Activity gates govern local task sequencing; phase gates govern cross-stream preconditions. If both apply, the more restrictive gate governs.

---

## VII. SUB-ACTIVITY RULES (AC00x.x)

### A. Definition

A **Sub-Activity** is a **temporary decomposition** of a parent Activity used only to control remediation work that remains within the **same scope** and produces the **same final deliverable(s)** as the parent Activity.

Sub-Activities exist to keep a plan readable when an Activity must be amended mid-stream (remediation / mandatory update), without inflating higher-level registers.

### B. When to Use (Allowed Triggers)

Use a Sub-Activity only when the parent Activity requires remediation due to one of the following:
- **Parallel implementation drift**: two or more work paths changed the same deliverable surface, requiring a corrective pass to reconcile and re-align.
- **Higher-authority mandatory update**: a governing decision, standard, or gate outcome requires updates to the parent Activity's deliverable(s), within the same scope.

### C. When NOT to Use

Do NOT use Sub-Activities when any of the following are true:
- A **new deliverable contract** is introduced (create a new Activity instead).
- Ownership changes in a way that requires independent gating or accountability (create a new Activity or a Gate as appropriate).
- The work is normal execution detail that fits in a Task Register (use Tasks).
- You need stream/phase-level dependency visibility on the remediation itself (in that case, restructure Activities; do not hide a critical path inside a Sub-Activity).

### D. Activity vs Sub-Activity Decision Test

- Create a new **Activity (AC00x)** when the plan needs a **new contract-level unit** (distinct deliverable, distinct gate responsibility, or distinct dependency surface).
- Create a **Sub-Activity (AC00x.x)** when work is a **remediation slice** of an existing Activity, staying within the same scope and deliverable(s).

### E. Sub-Activity ID Format (Approved)

Sub-Activities MUST use **dotted numeric** IDs:

- Parent Activity: `AC009`
- Sub-Activity: `AC009.1`, `AC009.2`, ...

Rules:
- The suffix after `.` MUST be numeric (`1`, `2`, ...). Letters (e.g., `AC009A`) MUST NOT be used for Sub-Activities.
- Lettered tokens (A/B/C) MAY be used for **options/alternatives** in narrative text (e.g., "Option A"), but not as plan work IDs.

### F. Register & Placement Rules (Critical)

- Sub-Activities MUST NOT be registered as standalone rows in any higher-level register (Phase/Stream Activity Registers).
- Only the **parent Activity (AC00x)** is registered.
- Sub-Activities MUST be authored only inside the parent Activity section, as subheadings.

### G. Status Semantics

- The parent Activity's register `Status` MUST reflect overall completion of the Activity, including any Sub-Activity remediation work.
- If a completed Activity requires remediation, authors SHOULD treat this as a **plan amendment** and update the parent Activity section and changelog so the current plan state is unambiguous.

### H. Authoring Pattern (Recommended)

Inside the parent Activity section, author each Sub-Activity as:

`#### Sub-Activity AC00x.x: <Title>`

Include the same contract fields as needed (Purpose/Scope/Task Register/Success Criteria), but keep the deliverable contract anchored to the parent Activity.

---

## VIII. TEMPLATE INVENTORY

The following templates are available for PLAN artifacts. Each template defines the required structure for its planning level. Authors MUST use the appropriate template when creating new plan files.

### A. Phase Plan Template

- **Template**: `prompt/templates/consultant/workspace/template_workspace_plan_phase.md`
- **What**: Defines the required structure for phase-level plan files.
- **Why**: Ensures consistent section ordering, register schemas, and frontmatter across all phase plans (including the Activity Snapshot Index anti-drift boundary).
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
  `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (P-STD-004 proposal)

---

## IX. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.3.0 | 2026-02-11 | Amendment | Added §VI.F Phase-Level Gates authoring rule: ID format, placement, scope, enforcement mode (blocking vs conformance), interaction with activity gates |
| v1.4.0 | 2026-02-11 | Update | Added Template Inventory section referencing PLAN templates; corrected status enum spelling (`deferred`) |
| v1.5.0 | 2026-02-14 | Amendment | Standardized Sub-Activity workflow: dotted numeric `AC00x.x` IDs, allowed triggers (remediation/mandatory updates), and register constraints (Sub-Activities not listed in higher-level Activity Registers) |
| v1.6.0 | 2026-02-14 | Amendment | Standardized anti-drift register authority: Phase plans use Activity Snapshot Index (as-of dated, no dependency authoring); Stream plans remain SSOT. Standardized linking rules for standalone Activity Plans and minimum stream-level contract stubs |
