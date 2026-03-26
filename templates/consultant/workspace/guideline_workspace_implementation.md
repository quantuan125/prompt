---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'implementation_authoring'
version: '1.4.0'
date: '2026-03-26'
status: 'draft'
author: 'LLM_Developer'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/workspace/README.md'
---

# Implementation Procedural Guideline (Consultant Workspace)

## I. PURPOSE

Define authoring rules for IMPLEMENTATION workspace artifacts so they are:
- detailed implementation specifications between plan task authority and developer execution evidence,
- scoped to a single logical implementation boundary (task-ID or gate-remediation-cycle),
- compatible with program naming/placement authority (`P-STD-004`) and ID/reference authority (`P-STD-005`).

The IMPLEMENTATION family provides detailed implementation specification between plan task authority and execution evidence. Two subtypes exist, each with a dedicated trigger:
- `remediation_specification` — triggered by a gate `RECYCLE` verdict.
- `task_specification` — triggered when task complexity exceeds plan-step capacity.

**Status notice**: This is Draft 1. Normative binding is deferred to T104J.

---

## II. ROLE BOUNDARY (LOCKED)

- **LLM_Consultant** is the primary author and commissioner for both subtypes.
- **LLM_Planner** may assist with `task_specification` decomposition only when explicitly delegated by the consultant.
- **LLM_Developer** or designated consultant-commissioned agentic execution roles are the primary consumers (execution).
- **LLM_Reviewer** is a secondary consumer for `remediation_specification` (re-assessment input).
- **Client** is the decision owner for gates and approvals downstream.

**Boundary rule**: IMPLEMENTATION artifacts MUST NOT hold a GDR section. Gate decisions remain exclusively in `gate_disposition` proposals per `guideline_workspace_proposal.md` §VII. (CONV-006)

**Execution-boundary rule**: Consultant authorship of an IMPLEMENTATION artifact does not make the consultant the execution owner. Execution evidence still belongs to the developer or agentic execution role that performed the work.

Note: Role definitions are informative pending T101 (Role Standardization).

---

## III. SUBTYPE TAXONOMY

Draft 1 defines exactly two subtypes:

### A. `remediation_specification`

- **Trigger**: Gate verdict of `RECYCLE`.
- **Purpose**: Detailed implementation specification for flipping gate findings from RECYCLE to PASS.
- **Template**: `template_workspace_implementation_remediation-specification.md`
- **Author**: `LLM_Consultant`

### B. `task_specification`

- **Trigger**: Task complexity exceeds plan-step capacity.
- **Purpose**: Detailed implementation specification for complex tasks where plan steps alone do not provide sufficient implementation detail.
- **Template**: `template_workspace_implementation_task-specification.md`
- **Author**: `LLM_Consultant` (primary); `LLM_Planner` only when explicitly delegated by the consultant

Each subtype has a dedicated template (CONV-003). Additional subtypes require a future amendment; Draft 1 is capped at these two.

---

## IV. GOVERNANCE RULES (UNIVERSAL)

The following conventions govern all IMPLEMENTATION artifacts:

| Convention | Rule |
|:--|:--|
| CONV-006 | IMPLEMENTATION artifacts SHALL NOT contain a GDR section |
| CONV-007 | Mandatory frontmatter backlinks: `plan_reference`, `task_id` or `gate_id`, and triggering artifact reference (`verification_reference` or `proposal_reference`) |
| CONV-008 | Mandatory audience/authority preamble in Section I distinguishing this artifact from plan authority and proposal decision authority |
| CONV-009 | For `remediation_specification`, the artifact SHALL exist as a formal task above the gate in the task register (Directive B) |
| CONV-010 | One artifact per logical implementation scope. Logical implementation scope is scoped to a task-ID, a gate-remediation-cycle, or a multi-task implementation phase sharing a common design-decision boundary (e.g., tasks seeded by the same gate's GIR resolutions). |
| CONV-011 | Plan task steps SHALL be high-level summary only when an IMPLEMENTATION artifact exists; the plan step SHALL reference the artifact path |
| CONV-012 | Execution-facing SPEC items in both IMPLEMENTATION templates MUST use the hybrid structure: concise metadata table plus prose `Implementation Detail` block, and the metadata table MUST name exact target files/surfaces, required end-state posture, explicit non-target constraints, validation checks, and a blocking ambiguity rule |
| CONV-013 | `task_specification` MAY declare `execution_audience` to distinguish developer execution from consultant-orchestrated agentic execution without creating a new subtype |
| CONV-014 | When a gate is still deciding a convention that would otherwise require a concrete implementation artifact, authors SHOULD route the convention through a `standards_input` proposal first and MUST NOT treat the premature concrete artifact as active gate authority |

---

## V. FRONTMATTER SPECIFICATION

### A. Required Fields (All Subtypes)

| Field | Value / Description |
|:--|:--|
| `artifact_type` | `'IMPLEMENTATION'` |
| `implementation_type` | `'remediation_specification'` or `'task_specification'` |
| `initiative_id` | Initiative identifier (e.g., `T104`) |
| `initiative_code` | Initiative code (e.g., `CWS`) |
| `phase` | Phase number |
| `stream_id` | Stream UID |
| `activity_id` | Activity UID |
| `task_id` | Task UID |
| `version` | Semantic version (e.g., `1.0.0`) |
| `date` | ISO date |
| `status` | `draft`, `completed`, etc. |
| `author` | Author role |
| `decision_owner_role` | `'Client'` |
| `plan_reference` | Repo-relative path to governing plan |

### B. Additional Required Fields — `remediation_specification`

| Field | Value / Description |
|:--|:--|
| `gate_id` | Full gate UID |
| `verification_reference` | Repo-relative path to verification artifact |
| `proposal_reference` | Repo-relative path to gate-disposition proposal |

### C. Additional Required Fields — `task_specification`

None beyond the universal set.

### D. Optional Fields — `task_specification`

| Field | Value / Description |
|:--|:--|
| `execution_audience` | Optional. `'developer'` by default; `'agentic_executor'` when execution is delegated to designated agentic roles on the consultant's behalf; `'consultant'` only when no downstream execution role exists and the artifact governs consultant-owned non-implementation work |

---

## VI. LIFECYCLE RULES

### A. `remediation_specification`

1. **Created** after a RECYCLE verdict and plan amendment authorizing remediation work.
2. **Consumed** during remediation execution by `LLM_Developer`.
3. **Version-bumped** if remediation scope changes.
4. **Closed** when gate re-assessment passes.

### B. `task_specification`

1. **Created** during task planning or after a plan amendment introducing complex work.
2. **Consumed** during developer or consultant-commissioned agentic execution.
3. **Version-bumped** if specification scope changes.
4. **Closed** when the governing task completes.

---

## VII. RELATIONSHIP TO OTHER ARTIFACTS

### A. Plan

Plan retains tracked-work authority. IMPLEMENTATION provides specification depth. Plan steps reference the artifact path when one exists (CONV-011).

For governed work where an IMPLEMENTATION artifact exists, legacy `.claude/plans/` surfaces are not a co-equal authority surface and should be treated as ad hoc only.

### B. Verification

For `remediation_specification`, the artifact references verification findings by ID. Complementary relationship: revision-checklist = "what needs fixing" (reviewer), remediation specification = "how to fix it" (consultant).

### C. Dev-Report

Developer execution evidence references the IMPLEMENTATION artifact as the specification input. When an IMPLEMENTATION artifact governs the work, the DEV-REPORT SHOULD include `implementation_reference` per `guideline_workspace_dev-report.md`, and its Traceability Matrix SHOULD map deliverables back to relevant SPEC item IDs where practical.

### D. Proposal

IMPLEMENTATION does not hold decision authority. Gate decisions remain in `gate_disposition` proposals.

### E. Standards-Input Boundary

When a consultation-only gate is still deciding a convention or operational pattern, a `standards_input` proposal is the correct pre-implementation authority surface. A concrete implementation artifact may exist prematurely in the worktree for lineage reasons, but it MUST NOT be treated as the approved authority source until downstream execution is authorized.

---

## VIII. TEMPLATE INVENTORY

- `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md`
- `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`

---

## IX. CHANGELOG

`prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_implementation.md`
