---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'dev-report_authoring'
version: '1.5.0'
date: '2026-04-02'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
template_reference: 'prompt/templates/consultant/workspace/template_workspace_dev-report.md'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md'
decision_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC006/proposal/proposal_T104-PH001-ST005-AC006-TK001.1_gir-disposition-package.md'
---

# DEV-REPORT Procedural Guideline (Consultant Workspace)

## I. PURPOSE

Define authoring rules for DEV-REPORT workspace artifacts so they are:
- developer-owned execution evidence,
- bounded to a specific implementation slice,
- usable as verification and handoff input without becoming gate verdicts,
- compatible with naming/placement authority (`P-STD-004`) and ID/reference authority (`P-STD-005`).

This guideline is Draft 1 (exemplar-derived). It encodes the approved AC006 GATE-000 GIR decisions for DEV-REPORT authoring.

---

## II. ROLE BOUNDARY

- **LLM_Developer** is the primary author of DEV-REPORT artifacts.
- **LLM_Reviewer** consumes DEV-REPORT artifacts as navigation input during verification; reviewer verdicts remain inside VERIFICATION artifacts.
- **LLM_Consultant** may reference DEV-REPORT artifacts when authoring plans, analyses, or proposals, but does not use them as substitutes for those artifact types.
- **Client** is the decision owner for gates and approvals downstream of the implementation slice.

Boundary rules:
- DEV-REPORT artifacts capture implementation evidence, not contract-level scope changes.
- DEV-REPORT artifacts MUST NOT claim gate closure, reviewer verdicts, or client decisions.
- Full session chronology belongs in `snotes_` and `raw_` artifacts; DEV-REPORT artifacts may summarize only execution-relevant outcomes.

---

## III. TRIGGER & LIFECYCLE

### A. When a DEV-REPORT is required

Author a DEV-REPORT whenever developer-executed work mutates deliverables and reaches a bounded review, handoff, or gate-ready boundary.

Consultation-only gates with no developer-mutated deliverables MUST NOT produce a DEV-REPORT.

Valid bounded slices include:
- a single task,
- a grouped contiguous task range,
- a task range through a gate-handoff boundary,
- a remediation or closeout slice that is explicitly bounded.

### B. Grouped task ranges

One DEV-REPORT MAY cover multiple related tasks when they form one cohesive implementation package. The report MUST state the bounded task/gate slice clearly in frontmatter and in the title.

### C. Consolidated / retroactive reports

Consolidated or retroactive DEV-REPORT artifacts are allowed only when:
- the report declares the exact bounded slice being packaged, and
- the report references the source artifacts or prior execution evidence it is closing out.

### D. DEV-REPORT Package Taxonomy (Scope Decomposition)

| Posture | When To Use | Required Frontmatter Posture | Review / Gate Entry Point |
|:--|:--|:--|:--|
| Single-report posture | One DEV-REPORT covers the full bounded execution slice. | `package_role` omitted or `primary`; no `primary_report`; `consolidated_from` omitted unless the report is explicitly consolidated. | Directly to review or gate packaging. |
| Primary DEV-REPORT | A multi-report package needs one gate-facing producer-evidence surface. | `package_role: 'primary'`; `consolidated_from` MAY list supplementary reports; `primary_report` omitted. | Primary review surface, then gate packaging. |
| Supplementary DEV-REPORT | A bounded subordinate slice needs its own producer-evidence record under one package. | `package_role: 'supplementary'`; `primary_report` MUST point to the governing primary DEV-REPORT; `consolidated_from` omitted. | Drill-down evidence under the primary report. |
| Consolidated DEV-REPORT | One primary DEV-REPORT aggregates and links multiple supplementary reports. | `package_role: 'primary'`; `consolidated_from` MUST list every supplementary DEV-REPORT in the package; `primary_report` omitted. | Consolidated gate-facing review surface. |

Same-gate recycle remediation slices are bounded evidence segments and SHOULD be represented as supplementary DEV-REPORT artifacts beneath one primary gate-facing report.

Rules:
- A multi-report DEV-REPORT package MUST contain exactly one primary DEV-REPORT.
- Each supplementary DEV-REPORT MUST set `package_role: 'supplementary'`.
- Each supplementary DEV-REPORT MUST set `primary_report` to the repo-relative path of its governing primary DEV-REPORT.
- A primary DEV-REPORT in a multi-report package MUST set `package_role: 'primary'`.
- A consolidated DEV-REPORT is a primary DEV-REPORT and MUST populate `consolidated_from` with every supplementary DEV-REPORT included in the package.
- A single-report posture MUST NOT populate `primary_report`; it MAY omit `consolidated_from`; if `package_role` is present it MUST be `primary`.

### E. Scope Decomposition vs Temporal Iteration

| Question | If Yes | If No |
|:--|:--|:--|
| Does the execution slice contain multiple bounded evidence segments that belong to one gate-facing package? | Create supplementary DEV-REPORTs beneath one primary report. | Keep a single DEV-REPORT posture. |
| Is the change only a correction to the same report artifact? | Version-bump the existing report. | Create a supplementary DEV-REPORT when this is a new recycle cycle under the same gate. |

- Scope decomposition creates supplementary DEV-REPORTs beneath one primary report.
- Temporal correction of the same report artifact version-bumps the existing report.
- New recycle cycles produce supplementary DEV-REPORTs rather than reusing version bumps.

### F. Relationship to plan and gates

- The plan remains the execution authority.
- The DEV-REPORT records what was implemented under that authority.
- When an implementation-backed gate follows, the DEV-REPORT provides producer evidence and handoff inputs only; the verification artifact provides the reviewer verdict, and the proposal-hosted GDR records the client decision.
- Consultation-only gates omit DEV-REPORT because no developer execution slice is being reviewed.
- **Plan-level positioning**: When an implementation-backed gate follows, the DEV-REPORT task SHOULD appear as part of the Gate-Readiness Stack — immediately after the implementation tasks and before the verification task. For the full pattern, see `guideline_workspace_plan.md` §VI.L.

---

## IV. FRONTMATTER CONVENTIONS

### A. Common required keys

Every DEV-REPORT artifact MUST include:
- `artifact_type: 'DEV-REPORT'`
- `initiative_id`
- `version`
- `date`
- `status`
- `author: 'LLM_Developer'`
- `decision_owner_role: 'Client'`
- `source_plan`

### B. Common recommended keys

When applicable, include:
- `initiative_code`
- `phase`
- `stream_id`
- `activity_id`
- `task_id`
- `scope`
- `implementation_reference`
- `package_role`

### C. Bounded optional keys

Use these only when they add real traceability value:
- `target_gate`
- `consumers`
- `primary_report`
- `consolidated_from` for primary DEV-REPORTs that consolidate supplementary reports or close out a retroactive bounded slice

Policy:
- `task_id` MAY hold a bounded range string when the report covers a grouped task or task-to-gate slice.
- `package_role` allowed values are exactly `primary` and `supplementary`.
- `primary_report` is permitted only on supplementary DEV-REPORTs.
- `consolidated_from` is permitted only on primary DEV-REPORTs.
- Optional keys MUST NOT replace the required narrative sections that explain scope and evidence.

---

## V. REQUIRED STRUCTURE

Every DEV-REPORT artifact MUST include these core sections, in order:
1. `Executive Summary`
2. `Implementation Log`
3. `Validation Evidence`
4. `Traceability Matrix`
5. `Handoff`
6. `Changelog`

Optional sections:
- `Artifact Index` when the report packages many outputs or evidence artifacts
- `Notes / Deferrals` when the execution slice intentionally leaves bounded follow-up items

### A. Executive Summary

The summary MUST state:
- what was completed in scope,
- what was intentionally not completed in scope,
- the resulting readiness or handoff posture when relevant.

### B. Implementation Log

The implementation log MUST be organized by bounded task or subtask block.

Each block SHOULD record:
- files updated or created,
- changes applied,
- outputs produced (if any),
- implementation result.

Single-task sections remain valid, but grouped blocks are the default when multiple contiguous tasks form one package.

### C. Validation Evidence

The validation section MUST include:
- commands or checks run,
- the result of each command/check,
- brief interpretation explaining what the evidence demonstrates.

Expected non-zero exits are allowed only when explicitly labeled as expected and briefly explained.

### D. Traceability Matrix

Every DEV-REPORT artifact MUST include a traceability matrix that maps each task/gate in scope to its produced deliverable or evidence surface.

When the execution slice is governed by an IMPLEMENTATION artifact, the Traceability Matrix SHOULD map the produced deliverables back to the relevant SPEC item IDs where practical.

### E. Handoff

Every DEV-REPORT artifact MUST include a handoff section. When no external handoff exists, the section MUST explicitly say so.

When a review or gate follows, the handoff MUST identify:
- next owner,
- must-review inputs,
- pending decision or next execution step.

### F. Artifact Index

An artifact index is conditional, not universal. Add it only when the report packages enough outputs that a separate inventory improves navigation.

---

## VI. VALIDATION EVIDENCE POSTURE

### A. Minimum evidence standard

The minimum DEV-REPORT validation posture is:
- command/check result,
- concise interpretation,
- enough detail for a reviewer to navigate and independently verify.

Prose-only “verified” claims are insufficient.

### B. Git / checkpoint evidence

Git commit IDs, rollback checkpoints, or repo-state evidence are optional unless they are materially relevant to the slice being reported. Include them when the implementation contract, rollback posture, or gate package depends on that information.

### C. Raw output handling

Do not inline large raw logs in the body. Summarize key results in the DEV-REPORT and reference the supporting artifact or output location when needed.

---

## VII. NAMING & PLACEMENT

### A. Filename pattern

DEV-REPORT artifacts MUST use:
- `dev-report_<scope-UID>_<kebab-topic>_<YYYY-MM-DD>.md`

`<scope-UID>` MUST be the bounded execution scope for the report:
- use the activity UID when the slice is activity-scoped,
- use the stream UID when the slice is stream-scoped,
- use a sub-activity UID when the report is scoped to a standalone `AC###.N`.

### B. Directory placement

Placement is scope-aligned:
- if `<scope-UID>` contains `-AC###`, place the file under the matching activity `dev-report/` directory,
- if `<scope-UID>` is stream-scoped, place the file under the stream `dev-report/` directory,
- if `<scope-UID>` is a standalone sub-activity UID (`AC###.N`), place the file under that sibling sub-activity directory per `P-STD-004`.

### C. Naming authority note

DEV-REPORT uses a date suffix by design. The dated filename does not replace the responsibility to keep the report bounded and topic-specific.

---

## VIII. TRACEABILITY, HANDOFF, & BOUNDARIES

### A. Plan linkage

- DEV-REPORT artifacts MUST reference the governing `source_plan`.
- When an IMPLEMENTATION artifact governs the execution slice, the DEV-REPORT SHOULD include `implementation_reference` pointing to that specification surface.
- Task and gate references inside the report MUST use fully qualified IDs or explicit repo-relative artifact paths.
- The plan task register `Action` column remains the concise execution record; the DEV-REPORT is the fuller producer evidence surface.

### B. Verification relationship

- DEV-REPORT artifacts are verification inputs, not verification outputs.
- Reviewers MUST still perform independent evidence-first verification per `guideline_workspace_verification.md`.

### C. Proposal and analysis relationship

- Proposals may cite DEV-REPORT artifacts as execution evidence or package inputs.
- Analyses may reference DEV-REPORT artifacts for pattern or compliance assessment, but DEV-REPORT itself does not replace ANALYSIS or PROPOSAL semantics.

### D. Notes / raw boundary

- DEV-REPORT captures implementation evidence and execution outcomes.
- `snotes_` and `raw_` artifacts capture conversation chronology and transcript material.
- If a decision matters to execution, summarize only the execution-relevant result and point to the session artifact when detailed chronology matters.

### E. Multi-report package linkage

- Supplementary DEV-REPORTs MUST link upward to the primary DEV-REPORT through `primary_report`.
- Primary consolidated DEV-REPORTs MUST link downward to every supplementary DEV-REPORT through `consolidated_from`.
- Recycle-cycle supplementary DEV-REPORTs SHOULD also carry `recycle_gate_id`, `recycle_iteration`, and `cycle_scope` alongside the required linkage model. These keys supplement, but do not replace, `package_role`, `primary_report`, and `consolidated_from`.
- Verification and proposal surfaces SHOULD cite the primary DEV-REPORT first and use supplementary DEV-REPORTs as drill-down evidence. This SHOULD is intentional as a general DEV-REPORT guidance posture; the VERIFICATION guideline independently mandates the ordering for reviewer-owned Evidence Set sections via SPEC-002.

---

## IX. TEMPLATE INVENTORY

- **Template**: `prompt/templates/consultant/workspace/template_workspace_dev-report.md`
- **Use for**: all new DEV-REPORT artifacts in consultant workspace flows
- **How**: copy the template, populate the required frontmatter, keep the core sections, and remove optional sections only when they are genuinely not needed

---

## X. CHANGELOG

`prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_dev-report.md`
