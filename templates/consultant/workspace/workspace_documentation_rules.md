---
artifact_type: 'GUIDE'
scope: 'consultant_workspace'
purpose: 'Governance rules for workspace artifacts: templates, guidelines, role boundaries, and file conventions'
version: '3.3.0'
date: '2026-03-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# Workspace Documentation Rules (Consultant)

## 1. PURPOSE

Define the governance rules for **consultant workspace artifacts** (plans, roadmaps, notes, and supporting templates/guidelines) so they remain toolable, drift-resistant, and consistent across initiatives.

---

## 2. TIMELINE HIERARCHY (LOCKED)

Phase → Stream → Activity → Task
- Reference: `prompt/templates/consultant/workspace/guideline_workspace_plan.md` §II.A

---

## 3. ARTIFACT TYPE INVENTORY

| Artifact Type | File Prefix | Purpose | Template | Guideline |
|:--|:--|:--|:--|:--|
| PLAN (Phase) | `plan_` | Phase-level execution planning | `prompt/templates/consultant/workspace/template_workspace_plan_phase.md` | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| PLAN (Stream) | `plan_` | Stream-level execution planning | `prompt/templates/consultant/workspace/template_workspace_plan_stream.md` | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| PLAN (Activity) | `plan_` | Activity-level task decomposition | `prompt/templates/consultant/workspace/template_workspace_plan_activity.md` | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| ROADMAP | `roadmap_` | Initiative master spine / phase execution | `prompt/templates/consultant/workspace/template_workspace_roadmap.md` | `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md` (Draft 2 STD alignment pending) |
| NOTES (Register) | `notes_` | Index/navigation surface | `prompt/templates/consultant/workspace/template_workspace_notes_register_*.md` | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| NOTES (Session) | `snotes_` | Session records | `prompt/templates/consultant/workspace/template_workspace_notes_session_*.md` | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| ANALYSIS | `analysis_` | Workspace synthesis/audits/assessments/external reviews (type-scoped via `analysis_type`) | `prompt/templates/consultant/workspace/template_workspace_analysis.md` | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| VERIFICATION | `verification_` | Gate evidence + findings register + rework handoff + reviewer verdict | `prompt/templates/consultant/workspace/template_workspace_verification.md` | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| PROPOSAL | `proposal_` | Archetype-specific proposal authoring: E-ID workspace, gate disposition (incl. Gate Decision Record), promotion contract, standards input | `prompt/templates/consultant/workspace/template_workspace_proposal_<archetype>.md` | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| DEV-REPORT | `dev-report_` | Developer execution log + validation evidence + handoff traceability | `prompt/templates/consultant/workspace/template_workspace_dev-report.md` | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| IMPLEMENTATION | `implementation_` | Detailed implementation specification: remediation specifications (gate RECYCLE response), task specifications (complex implementation detail) | `prompt/templates/consultant/workspace/template_workspace_implementation_<subtype>.md` | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

**Artifact status vocabulary** (canonical values for `status` frontmatter key):

| Status | Definition | Applicable Artifact Types |
|:--|:--|:--|
| `draft` | Artifact is being actively authored; not yet finalized | All |
| `active` | Artifact is current and authoritative for its scope | All |
| `completed` | Artifact has fulfilled its purpose; no further changes expected | PLAN, NOTES, ANALYSIS, VERIFICATION, DEV-REPORT, IMPLEMENTATION |
| `failed` | Gate-specific terminal state: work killed or abandoned. MUST NOT be used for non-gate artifacts | Gate rows in PLAN (via PROPOSAL GDR) |
| `superseded` | Artifact was valid for its normative baseline but that baseline has changed due to an external event. A successor artifact/gate exists. The artifact is preserved for historical traceability. MUST NOT be deleted. | ANALYSIS, PROPOSAL, VERIFICATION (gate-scope artifacts) |
| `cancelled` | Work item deliberately terminated before completion. Per `P-STD-002` canonical states. | PLAN work-item rows |

Note: `superseded` is distinct from `cancelled` (deliberate early termination) and from `failed` (quality failure / gate termination). `superseded` carries no quality judgment — the artifact was valid for its baseline; the baseline moved.

---

## 4. TEMPLATE INVENTORY

### A. PLAN Templates
- `prompt/templates/consultant/workspace/template_workspace_plan_phase.md`
- `prompt/templates/consultant/workspace/template_workspace_plan_stream.md`
- `prompt/templates/consultant/workspace/template_workspace_plan_activity.md`

### B. ROADMAP Templates
- `prompt/templates/consultant/workspace/template_workspace_roadmap.md`

### C. NOTES Templates
- Register templates (index-only):
  - `prompt/templates/consultant/workspace/template_workspace_notes_register_phase.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes_register_stream.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes_register_activity.md`
- Session templates (entry files):
  - `prompt/templates/consultant/workspace/template_workspace_notes_session_phase.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes_session_stream.md`
  - `prompt/templates/consultant/workspace/template_workspace_notes_session_activity.md`
- Legacy (deprecated; do not delete):
  - `prompt/templates/consultant/workspace/template_workspace_notes.md`

### D. VERIFICATION Templates
- `prompt/templates/consultant/workspace/template_workspace_verification.md`

### E. DEV-REPORT Templates
- `prompt/templates/consultant/workspace/template_workspace_dev-report.md`

### F. ANALYSIS Templates
- `prompt/templates/consultant/workspace/template_workspace_analysis.md`

### G. PROPOSAL Templates
- `prompt/templates/consultant/workspace/template_workspace_proposal_eid-workspace.md`
- `prompt/templates/consultant/workspace/template_workspace_proposal_gate-disposition.md`
- `prompt/templates/consultant/workspace/template_workspace_proposal_promotion-contract.md`
- `prompt/templates/consultant/workspace/template_workspace_proposal_standards-input.md`
- Legacy (deprecated; redirect-only):
  - `prompt/templates/consultant/workspace/template_workspace_proposal.md`
  - Archived full legacy template: `prompt/templates/consultant/workspace/archive/deprecated/template_workspace_proposal.md`

### H. IMPLEMENTATION Templates
- `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md`
- `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`

---

## 5. GUIDELINE INVENTORY

- PLAN: `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- ROADMAP: `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md`
- NOTES: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
- VERIFICATION: `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
- DEV-REPORT: `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`
- ANALYSIS: `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- PROPOSAL: `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
- IMPLEMENTATION: `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`

---

## 6. ROLE BOUNDARY RULES

### A. Consultant (LLM_Consultant)
- Authors contract-level intent: what + why.
- Owns: roadmaps, phase plans, stream plans (contract-level), guidelines, templates, proposals, analyses.
- Boundary: MUST NOT author implementation-level task decomposition or execution proof.

### B. Planner (LLM_Planner)
- Owns: task decomposition, sequencing, estimation.
- Boundary: MUST NOT alter contract-level intent without Consultant approval.

### C. Developer (LLM_Developer)
- Owns: execution, implementation, dev-reports.
- Boundary: MUST NOT alter contract-level scope; implementation evidence belongs in dev-reports; plan task register `Action` column is updated by developer post-execution.

### D. Reviewer (LLM_Reviewer)
- Owns: verification artifacts for gates, findings classification, and rework handoff evidence.
- Produces verification as a task (TK-before-gate pattern) only for implementation-backed gates after developer execution and DEV-REPORT handoff. The reviewer's verdict is recorded in the verification artifact's Gate Recommendation section; the Gate Decision Record (GDR) is hosted in the consultant-owned `gate_disposition` proposal per `guideline_workspace_proposal.md` §VII.
- Boundary: MUST NOT alter contract-level scope; scope gaps discovered in verification escalate as Situation B findings per `guideline_workspace_verification.md §VII`.

### E. Client
- Decision owner for all approval gates.
- Boundary: All normative decisions require Client approval signal.

---

## 7. WORKFLOW CHAIN AND HANDOFF CONTRACTS

### A. Canonical Workflow Chain

The workspace artifact suite follows two canonical workflow variants depending on whether the gate reviews developer-mutated deliverables or consultant-owned decision-preparation artifacts.

Implementation-backed:
`ROADMAP → PLAN → NOTES / ANALYSIS → [IMPLEMENTATION task_specification where needed] → implementation deliverables → DEV-REPORT → VERIFICATION → [IMPLEMENTATION remediation_specification where RECYCLE] → remediation deliverables → DEV-REPORT → VERIFICATION (re-assessment) → PROPOSAL (GDR where applicable) → SPS / downstream approved artifacts`

Consultation-only:
`ROADMAP → PLAN → NOTES / ANALYSIS → PROPOSAL (GDR where applicable) → downstream approved artifacts`

**Conditional external-impact assessment step**:

When an external event (e.g., a standard amendment, cross-initiative change, regulatory update) is detected that may affect a gate's normative baseline, an impact assessment step precedes gate disposition:

`[External event detected] → ANALYSIS (external-impact classification) → [Decision-Boundary Test] → [boundary unchanged: continue workflow] / [boundary changed: gate supersession — PROPOSAL updated with SUPERSEDE GDR, successor gate created, superseded artifacts deprecated] → downstream gates/artifacts`

This conditional step applies to both implementation-backed and consultation-only workflow variants. It activates only when an external event is detected — it is not a mandatory step for every gate. Full classification and decision-boundary test rules are in `guideline_workspace_plan.md` §VI.M and `guideline_workspace_proposal.md` §VII.D Step 4a.

Rules:
- `ROADMAP` sets direction. `PLAN` establishes executable work authority.
- `NOTES`, `ANALYSIS`, and `DEV-REPORT` are working artifacts that capture session state, synthesis, and implementation evidence respectively. They feed downstream artifacts but do not close gates.
- `IMPLEMENTATION` provides detailed specification depth between plan task authority and developer execution. It does not hold work authority (PLAN) or decision authority (PROPOSAL GDR).
- For governed work where an IMPLEMENTATION artifact exists, that artifact is the canonical execution-specification surface. Legacy `.claude/plans/` usage is ad hoc only and is not a co-equal governed authority surface.
- `VERIFICATION` produces independent reviewer evidence and a reviewer verdict for implementation-backed gates only. The reviewer verdict is recorded only in the verification artifact.
- `PROPOSAL` packages decisions and hosts the authoritative Gate Decision Record (GDR) for `gate_disposition` proposals. The GDR carries the consultant's recommendation (advisory) and the client's decision (authoritative). The reviewer verdict is not duplicated into the GDR.
- Approved proposal decisions update plan status surfaces and unblock downstream work.

### B. Gate-Readiness Stack (Plan-Level Encoding)

The workflow chain is encoded at the plan level through the **Gate-Readiness Stack** — a canonical pre-gate task sequence. For the full pattern, ownership rules, and the distinction between implementation-backed and consultation-only gates, see `guideline_workspace_plan.md` §VI.L.

### C. Inter-Artifact Linkage Rules

| Rule | Authority |
|:--|:--|
| `ROADMAP` points to execution surfaces; it does not duplicate execution state | Initiative-level |
| `PLAN` is the authority for tracked work and gate placement | Initiative-level |
| `NOTES` captures session history and pending decisions; it is not a baseline authority | Initiative-level |
| `ANALYSIS` synthesizes evidence and findings, but does not close gates | Initiative-level |
| `DEV-REPORT` captures producer evidence only; it does not claim gate closure or verdicts | Initiative-level |
| `VERIFICATION` holds reviewer verdict and findings; it does not host the GDR. The reviewer verdict is not duplicated into the GDR | Initiative-level |
| `PROPOSAL` hosts the authoritative GDR containing the consultant recommendation (advisory) and client decision (authoritative) for `gate_disposition` proposals | Initiative-level |
| `IMPLEMENTATION` provides detailed specification depth; it does not hold work authority (PLAN) or decision authority (PROPOSAL GDR) | Initiative-level |

Reference rule:
- Same-activity session references MAY use shorthand forms such as `SES003-DEC001` when the activity scope is already explicit from context.
- Cross-activity session references MUST use fully-qualified timeline UIDs per `P-STD-005`.

**Superseded artifact linkage rules** (three-layer deprecation model):

When a gate is superseded (`Client Decision = SUPERSEDE`), artifacts produced for the superseded baseline are deprecated using a three-layer model. Each layer serves a different audience:

| Layer | Surface | Required Action | Purpose |
|:--|:--|:--|:--|
| **Layer 1: Frontmatter** | Superseded artifact (ANALYSIS, PROPOSAL, or VERIFICATION) | Set `status: 'superseded'`; add `superseded_by: '<successor-path>'`; add deprecation notice as first body line | Self-documenting: any reader of the artifact immediately sees it is not current |
| **Layer 2: Evidence Index** | Active successor gate-disposition proposal | Move superseded artifact from active evidence to a `Historical Evidence` subsection with `SUPERSEDED` annotation | Gate package clarity: reviewer/client see only current evidence in the primary index |
| **Layer 3: Links Register** | Governing plan (plan-level Links Register) | Add or update links register entry with `superseded` annotation and successor reference | Plan traceability: plan-level audit trail shows the succession chain |

**Deprecation notice format** (Layer 1):
```
> **SUPERSEDED**: This artifact was produced against [baseline X]. It has been superseded by [successor artifact path] which assesses against [baseline Y]. This artifact is preserved for historical traceability only.
```

**Rule**: Superseded artifacts MUST NOT be deleted. They are preserved as historically valid records of work conducted under the prior baseline. Only `status` and the `superseded_by` frontmatter key are changed; the body content is not altered.

**Cross-reference**: For full supersession mechanics, see `guideline_workspace_plan.md` §VI.M and `guideline_workspace_proposal.md` §VII.D Step 4a. For analysis-artifact authoring guidance on `status: 'superseded'` and `superseded_by`, see `guideline_workspace_analysis.md` §IX.

---

## 8. ROLE-TO-ARTIFACT OWNERSHIP MATRIX

| Artifact Type | Author | Reviewer | Approver / Decision Owner | Primary Consumer |
|:--|:--|:--|:--|:--|
| ROADMAP | LLM_Consultant | LLM_Consultant / Client as needed | Client where governed decisions apply | Consultant, Client, downstream roles |
| PLAN | LLM_Consultant or LLM_Planner per scope | Reviewer only when gated | Client where approval gates apply | Consultant, Planner, Developer, Reviewer |
| NOTES | LLM_Consultant | None by default | None by default | All roles |
| ANALYSIS | LLM_Consultant | Client / Consultant review as needed | Client when analysis drives approval | Consultant, Client |
| PROPOSAL | LLM_Consultant | Reviewer input when gate-backed | Client | Consultant, Client, downstream implementers |
| VERIFICATION | LLM_Reviewer (preferred) | Client consumes verdict | Client decides through GDR | Consultant, Client |
| DEV-REPORT | LLM_Developer | Reviewer consumes as evidence | None directly | Reviewer, Consultant |
| IMPLEMENTATION | LLM_Consultant (`remediation_specification`); LLM_Consultant or LLM_Planner (`task_specification`) | Reviewer consumes as re-assessment input | Client where gated | Developer, Reviewer |

Source: `T104-RES-003` Topic 8 (Workspace Artifact Integration & Industry Benchmark Analysis).

---

## 9. FILE NAMING & DIRECTORY CONVENTIONS

This workspace adopts the approved directory and file naming conventions defined in:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` (`P-STD-004`)

**Summary (workspace-relevant)**:
- Artifact file prefixes MUST match artifact type (e.g., `plan_`, `notes_`, `roadmap_`, `analysis_`, `proposal_`).
- Timeline UID tokens (`PH###`, `ST###`, `AC###`, `SES###`) determine planning/notes scope and MUST be used consistently.
- Standalone sub-activity artifacts with `AC###.N` scope use the dedicated sibling directory `workspace/PH###/ST###/AC###.N/`; parent `AC###/` placement is legacy-compatibility only.
- Task decomposition inside plans uses tracked Tasks / dotted Sub-Tasks (`TK###.n`) / informal Steps. Tasks and sub-tasks do not create directories.
- Templates live under `prompt/templates/consultant/workspace/` and are referenced by workspace artifacts via repo-relative paths.

---

## 10. ANTI-DRIFT RULES

### A. Link Don't Duplicate

- Artifacts MUST link by ID/path rather than duplicating normative content.
- Reference: `T104-CON-001` (Link Don’t Duplicate).

### B. Normative Source Hierarchy

SSOT (SPS + Concept) → Standards → Guidelines → Templates → Workspace artifacts

- If normative wording changes, update the authoritative source first (SSOT / standard / guideline), then update downstream templates/artifacts as needed.

### C. Execution History

- Session notes (`notes_...-SES###.md`) capture execution history.
- Plans and roadmaps capture intent, not history.
- `gate_disposition` proposals host the authoritative Gate Decision Record (GDR), including the consultant's gate recommendation and the client's closure decision.

---

## 11. MARKDOWN STRUCTURE

| Level | Markdown | Usage |
|:--|:--|:--|
| `#` | Document title | — |
| `##` | Major sections (Roman numerals) | I., II., III. |

---

## 12. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v3.3.0 | 2026-03-22 | Amendment | Expanded the implementation-backed workflow chain to make the full complex `RECYCLE` loop explicit (`IMPLEMENTATION remediation_specification` -> remediation deliverables -> DEV-REPORT -> VERIFICATION re-assessment). Added the governed-work note that IMPLEMENTATION is the canonical execution-specification surface where it exists and `.claude/plans/` is legacy/ad hoc only. Added bounded same-activity session-reference shorthand guidance in §7.C. Source: T104-PH001-ST008-AC001.6-GATE-001 GIR-003, GIR-007, GIR-008. |
| v3.2.0 | 2026-03-20 | Amendment | §7.A: Added conditional external-impact assessment step to the canonical workflow chain — when an external event affects a gate's normative baseline, an impact assessment step precedes gate disposition; supersession path replaces the normal gate close. §7.C: Added three-layer deprecation model for superseded artifacts (frontmatter + Evidence Index + Links Register), deprecation notice format, and preservation rule. §3: Added artifact status vocabulary table with `superseded` definition (distinct from `failed` and `cancelled`). Source: T104-PH001-ST008-AC001.4 GATE-001 (2026-03-20). |
| v3.1.0 | 2026-03-20 | Amendment | §7.A: Clarified that reviewer verdict stays in VERIFICATION only and PROPOSAL GDR carries consultant recommendation + client decision (three-signal model). §7.C: Updated VERIFICATION and PROPOSAL linkage rules to reflect GDR no longer duplicating reviewer verdict. §10.C: Updated GDR execution history note. Source: T104-PH001-ST008-AC001.5. |
| v3.0.0 | 2026-03-20 | Amendment | Added IMPLEMENTATION artifact family: §3 artifact type inventory row, §4.H template entries, §5 guideline entry, §7.A workflow chain with IMPLEMENTATION placement, §7.A IMPLEMENTATION linkage rule, §7.C inter-artifact linkage row, §8 role-to-artifact ownership row. New artifact family = major version bump. Source: T104-PH001-ST008-AC001.3-GATE-001 Path B approval. |
| v2.9.0 | 2026-03-16 | Amendment | Refined §6.D and §7 to distinguish implementation-backed gates from consultation-only gates. Verification is now explicitly limited to implementation-backed flows after DEV-REPORT handoff; consultation-only flows proceed from NOTES/ANALYSIS to PROPOSAL without VERIFICATION. Source: P-PH000-ST002-AC002 Gate 001 consultation. |
| v2.8.0 | 2026-03-15 | Amendment | Added §7 (Workflow Chain and Handoff Contracts) with canonical workflow chain, Gate-Readiness Stack cross-reference, and inter-artifact linkage rules. Added §8 (Role-to-Artifact Ownership Matrix). Fixed stale "proposals are not final decisions" in anti-drift rules (GAP-008). Source: T104-PH001-ST008-AC001.2; T104-RES-003 Topics 2, 3, 8. |
| v2.7.0 | 2026-03-13 | Update | Delivered DEV-REPORT Draft 1 authoring surfaces under AC006: registered `guideline_workspace_dev-report.md` and `template_workspace_dev-report.md`, and removed DEV-REPORT “Draft 1 planned” markers from §3, §4.E, and §5. |
| v2.5.0 | 2026-03-04 | Update | §3 VERIFICATION purpose: removed "Gate Decision Record (GDR)", replaced with "reviewer verdict". §3 PROPOSAL purpose: added "(incl. Gate Decision Record)". §6.D Reviewer boundary: clarified that GDR is hosted in consultant-owned gate_disposition proposal, reviewer produces verdict only. Source: T104-PH001-ST008-AC001 Option B approval. |
| v2.4.0 | 2026-03-03 | Update | Delivered PROPOSAL Draft 1 inventory for AC008: added archetype-specific proposal templates, marked proposal guideline as delivered, and recorded legacy proposal template deprecation + archive path. |
| v2.3.0 | 2026-03-01 | Update | Marked ANALYSIS guideline as delivered and updated ANALYSIS purpose to multi-type (via `analysis_type`). |
| v2.2.1 | 2026-03-01 | Update | §7 authority surface updated to reference `P-STD-004` (standard) instead of the seed proposal. |
| v2.2.0 | 2026-02-25 | Update | §3: VERIFICATION description updated to include rework handoff and GDR. §5: VERIFICATION guideline updated from "planned" to delivered. §6.D: Reviewer boundary updated with TK-before-gate pattern and cross-reference migrated to verification guideline. Source: T104-PH001-ST005-AC005 delivery. |
| v2.1.0 | 2026-02-25 | Update | Added VERIFICATION, DEV-REPORT, ANALYSIS, PROPOSAL to §3 Artifact Type Inventory with role owners. Added §4.D–G template entries. Added VERIFICATION/DEV-REPORT/ANALYSIS/PROPOSAL to §5 Guideline Inventory (Draft 1 planned). Updated §6 role boundaries: LLM_Verifier → LLM_Reviewer (canonical); Developer boundary clarified to include dev-reports; Consultant boundary extended to include analyses. Delivery planned under `T104-PH001-ST005` AC005–AC008. |
| v2.0.0 | 2026-02-11 | Rewrite | Replaced legacy rules with template + guideline inventories, role boundaries, P-STD-004 reference, and anti-drift governance for PLAN/ROADMAP/NOTES (Draft 1) |
