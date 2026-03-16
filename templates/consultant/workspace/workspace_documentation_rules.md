---
artifact_type: 'GUIDE'
scope: 'consultant_workspace'
purpose: 'Governance rules for workspace artifacts: templates, guidelines, role boundaries, and file conventions'
version: '2.9.0'
date: '2026-03-16'
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

---

## 5. GUIDELINE INVENTORY

- PLAN: `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- ROADMAP: `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md`
- NOTES: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
- VERIFICATION: `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
- DEV-REPORT: `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`
- ANALYSIS: `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- PROPOSAL: `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`

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
`ROADMAP → PLAN → NOTES / ANALYSIS → implementation deliverables → DEV-REPORT → VERIFICATION → PROPOSAL (GDR where applicable) → SPS / downstream approved artifacts`

Consultation-only:
`ROADMAP → PLAN → NOTES / ANALYSIS → PROPOSAL (GDR where applicable) → downstream approved artifacts`

Rules:
- `ROADMAP` sets direction. `PLAN` establishes executable work authority.
- `NOTES`, `ANALYSIS`, and `DEV-REPORT` are working artifacts that capture session state, synthesis, and implementation evidence respectively. They feed downstream artifacts but do not close gates.
- `VERIFICATION` produces independent reviewer evidence and a reviewer verdict for implementation-backed gates only.
- `PROPOSAL` packages decisions and hosts the authoritative Gate Decision Record (GDR) for `gate_disposition` proposals.
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
| `VERIFICATION` holds reviewer verdict and findings; it does not host the GDR | Initiative-level |
| `PROPOSAL` hosts the authoritative GDR for `gate_disposition` proposals | Initiative-level |

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
- `gate_disposition` proposals host the authoritative Gate Decision Record (GDR) for gate closure decisions.

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
