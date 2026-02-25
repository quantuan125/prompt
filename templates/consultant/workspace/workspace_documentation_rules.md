---
artifact_type: 'GUIDE'
scope: 'consultant_workspace'
purpose: 'Governance rules for workspace artifacts: templates, guidelines, role boundaries, and file conventions'
version: '2.1.0'
date: '2026-02-25'
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
| ANALYSIS | `analysis_` | Research synthesis | `prompt/templates/consultant/workspace/template_workspace_analysis.md` | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` (Draft 1 planned) |
| VERIFICATION | `verification_` | Gate evidence + findings register + remediation classification | `prompt/templates/consultant/workspace/template_workspace_verification.md` | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` (Draft 1 planned) |
| PROPOSAL | `proposal_` | E-ID development workspace + promotion contract | `prompt/templates/consultant/workspace/template_workspace_proposal.md` | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` (Draft 1 planned) |
| DEV-REPORT | `dev-report_` | Developer execution log + plan traceability | `prompt/templates/consultant/workspace/template_workspace_dev-report.md` (Draft 1 planned) | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` (Draft 1 planned) |

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
- `prompt/templates/consultant/workspace/template_workspace_dev-report.md` (Draft 1 planned — `T104-PH001-ST005-AC006`)

### F. ANALYSIS Templates
- `prompt/templates/consultant/workspace/template_workspace_analysis.md`

### G. PROPOSAL Templates
- `prompt/templates/consultant/workspace/template_workspace_proposal.md`

---

## 5. GUIDELINE INVENTORY

- PLAN: `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- ROADMAP: `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md`
- NOTES: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
- VERIFICATION: `prompt/templates/consultant/workspace/guideline_workspace_verification.md` (Draft 1 planned — `T104-PH001-ST005-AC005`)
- DEV-REPORT: `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` (Draft 1 planned — `T104-PH001-ST005-AC006`)
- ANALYSIS: `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` (Draft 1 planned — `T104-PH001-ST005-AC007`)
- PROPOSAL: `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` (Draft 1 planned — `T104-PH001-ST005-AC008`)

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
- Owns: verification artifacts for gates and remediation classification.
- Boundary: MUST NOT alter contract-level scope; scope gaps discovered in verification escalate as Situation B findings per `guideline_workspace_plan.md §VI.G`.

### E. Client
- Decision owner for all approval gates.
- Boundary: All normative decisions require Client approval signal.

---

## 7. FILE NAMING & DIRECTORY CONVENTIONS

This workspace adopts the approved directory and file naming conventions defined in:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (P-STD-004 proposal)

**Summary (workspace-relevant)**:
- Artifact file prefixes MUST match artifact type (e.g., `plan_`, `notes_`, `roadmap_`, `analysis_`, `proposal_`).
- Timeline UID tokens (`PH###`, `ST###`, `AC###`, `SES###`) determine planning/notes scope and MUST be used consistently.
- Templates live under `prompt/templates/consultant/workspace/` and are referenced by workspace artifacts via repo-relative paths.

---

## 8. ANTI-DRIFT RULES

### A. Link Don't Duplicate

- Artifacts MUST link by ID/path rather than duplicating normative content.
- Reference: `T104-CON-001` (Link Don’t Duplicate).

### B. Normative Source Hierarchy

SSOT (SPS + Concept) → Standards → Guidelines → Templates → Workspace artifacts

- If normative wording changes, update the authoritative source first (SSOT / standard / guideline), then update downstream templates/artifacts as needed.

### C. Execution History

- Session notes (`notes_...-SES###.md`) capture execution history.
- Plans and roadmaps capture intent, not history.
- Proposals capture development workspace, not final decisions.

---

## 9. MARKDOWN STRUCTURE

| Level | Markdown | Usage |
|:--|:--|:--|
| `#` | Document title | — |
| `##` | Major sections (Roman numerals) | I., II., III. |


---

## 10. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v2.1.0 | 2026-02-25 | Update | Added VERIFICATION, DEV-REPORT, ANALYSIS, PROPOSAL to §3 Artifact Type Inventory with role owners. Added §4.D–G template entries. Added VERIFICATION/DEV-REPORT/ANALYSIS/PROPOSAL to §5 Guideline Inventory (Draft 1 planned). Updated §6 role boundaries: LLM_Verifier → LLM_Reviewer (canonical); Developer boundary clarified to include dev-reports; Consultant boundary extended to include analyses. Delivery planned under `T104-PH001-ST005` AC005–AC008. |
| v2.0.0 | 2026-02-11 | Rewrite | Replaced legacy rules with template + guideline inventories, role boundaries, P-STD-004 reference, and anti-drift governance for PLAN/ROADMAP/NOTES (Draft 1) |
