---
artifact_type: 'GUIDE'
scope: 'consultant_workspace'
purpose: 'Governance rules for workspace artifacts: templates, guidelines, role boundaries, and file conventions'
version: '3.8.0'
date: '2026-03-28'
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
| VERIFICATION | `verification_` | Gate evidence + findings register + rework handoff + verifier verdict | `prompt/templates/consultant/workspace/template_workspace_verification.md` | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| PROPOSAL | `proposal_` | Archetype-specific proposal authoring: E-ID workspace, gate disposition (incl. Gate Decision Record), promotion contract, standards input | `prompt/templates/consultant/workspace/template_workspace_proposal_<archetype>.md` | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| DEV-REPORT | `dev-report_` | Developer execution log + validation evidence + handoff traceability | `prompt/templates/consultant/workspace/template_workspace_dev-report.md` | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| IMPLEMENTATION | `implementation_` | Consultant-authored implementation specifications that commission downstream execution: remediation specifications (gate RECYCLE response), task specifications (complex implementation detail for developer or assistant execution) | `prompt/templates/consultant/workspace/template_workspace_implementation_<subtype>.md` | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

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
- Boundary: MUST NOT personally perform implementation execution or claim execution proof as consultant evidence. The consultant MAY author IMPLEMENTATION artifacts, including `task_specification`, and MAY commission execution to `LLM_Developer`, `LLM_Assistant`, or designated lower-intelligence agentic execution roles when plan/gate authority permits.

### B. Planner (LLM_Planner)
- Owns: task decomposition, sequencing, estimation.
- Boundary: MUST NOT alter contract-level intent without Consultant approval.

### C. Developer (LLM_Developer)
- Owns: execution, implementation, dev-reports.
- Boundary: MUST NOT alter contract-level scope; implementation evidence belongs in dev-reports; plan task register `Action` column is updated by developer post-execution.

### D. Verifier (LLM_Reviewer / LLM_Consultant)
- Owns: verification artifacts for gates, findings classification, and rework handoff evidence.
- Operating model: `LLM_Reviewer` is the preferred future-state primary verifier. `LLM_Consultant` is the currently authorized secondary verifier under the temporary operating model and MAY author implementation-backed verification when independent of the implementation-producing task for that cycle.
- Produces verification as a task (TK-before-gate pattern) only for implementation-backed gates after developer execution and DEV-REPORT handoff. The verifier verdict is recorded in the verification artifact's Gate Recommendation section; the Gate Decision Record (GDR) is hosted in the consultant-owned `gate_disposition` proposal per `guideline_workspace_proposal.md` §VII.
- Boundary: MUST NOT alter contract-level scope; scope gaps discovered in verification escalate as Situation B findings per `guideline_workspace_verification.md §VII`.

### E. Client
- Decision owner for all approval gates.
- Boundary: All normative decisions require Client approval signal.

### F. Assistant (LLM_Assistant)
- Owns: consultant-commissioned execution support when explicitly named by an IMPLEMENTATION artifact or equivalent commissioning surface.
- Boundary: MUST NOT own `DEV-REPORT`, MUST NOT replace `LLM_Developer`, and MUST NOT alter contract-level scope.

---

## 7. WORKFLOW CHAIN AND HANDOFF CONTRACTS

### A. Canonical Workflow Chain

The workspace artifact suite follows two canonical workflow variants depending on whether the gate reviews developer-mutated deliverables or consultant-owned decision-preparation artifacts.

Implementation-backed:
`ROADMAP → PLAN → NOTES / ANALYSIS → [IMPLEMENTATION task_specification where needed] → implementation deliverables → DEV-REPORT → VERIFICATION → [IMPLEMENTATION remediation_specification where RECYCLE] → remediation deliverables → DEV-REPORT → VERIFICATION (re-assessment) → PROPOSAL (GDR where applicable) → ANALYSIS (external_review, LLM_Subconsultant) → SPS / downstream approved artifacts`

Consultation-only:
`ROADMAP → PLAN → NOTES / ANALYSIS → [IMPLEMENTATION task_specification where post-gate execution is commissioned] → PROPOSAL (GDR where applicable) → ANALYSIS (external_review, LLM_Subconsultant) → downstream approved artifacts`

The `[IMPLEMENTATION ...]` step is conditional: it applies only when the consultation-only gate authorizes governed post-gate execution through a commissioning artifact per `guideline_workspace_implementation.md` / CONV-018. When the consultation-only gate does not authorize downstream execution, this step is omitted.

**External review step**:
The `ANALYSIS (external_review)` step is authored by `LLM_Subconsultant` as an independent second-opinion quality audit of the gate package. The external review is advisory input; it does NOT override the `PROPOSAL`-hosted GDR authority. The main `LLM_Consultant` MUST review the external review findings and incorporate them into a final assessment before the gate proceeds to client disposition. See `guideline_workspace_plan.md` §VI.L for the full Gate-Readiness Stack pattern.

**Conditional external-impact assessment step**:

When an external event (e.g., a standard amendment, cross-initiative change, regulatory update) is detected that may affect a gate's normative baseline, an impact assessment step precedes gate disposition:

`[External event detected] → ANALYSIS (external-impact classification) → [Decision-Boundary Test] → [boundary unchanged: continue workflow] / [boundary changed: gate supersession — PROPOSAL updated with SUPERSEDE GDR, successor gate created, superseded artifacts deprecated] → downstream gates/artifacts`

This conditional step applies to both implementation-backed and consultation-only workflow variants. It activates only when an external event is detected — it is not a mandatory step for every gate. Full classification and decision-boundary test rules are in `guideline_workspace_plan.md` §VI.M and `guideline_workspace_proposal.md` §VII.D Step 4a.

Rules:
- `ROADMAP` sets direction. `PLAN` establishes executable work authority.
- `NOTES`, `ANALYSIS`, and `DEV-REPORT` are working artifacts that capture session state, synthesis, and implementation evidence respectively. They feed downstream artifacts but do not close gates.
- `IMPLEMENTATION` provides detailed specification depth between plan task authority and developer execution. It does not hold work authority (PLAN) or decision authority (PROPOSAL GDR).
- When a consultation-only gate discovers premature downstream execution or a prematurely materialized concrete artifact, the artifact MUST be preserved for lineage but removed from active gate authority until reclassified, quarantined, or later operationalized under an approved downstream task.
- For governed work where an IMPLEMENTATION artifact exists, that artifact is the canonical execution-specification surface. Legacy `.claude/plans/` usage is ad hoc only and is not a co-equal governed authority surface.
- `VERIFICATION` produces independent verifier evidence and a verifier verdict for implementation-backed gates only. The verifier verdict is recorded only in the verification artifact.
- `PROPOSAL` packages decisions and hosts the authoritative Gate Decision Record (GDR) for `gate_disposition` proposals. The GDR carries the consultant's recommendation (advisory) and the client's decision (authoritative). The verifier verdict is not duplicated into the GDR.
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
| `VERIFICATION` holds verifier verdict and findings; it does not host the GDR. The verifier verdict is not duplicated into the GDR | Initiative-level |
| `PROPOSAL` hosts the authoritative GDR containing the consultant recommendation (advisory) and client decision (authoritative) for `gate_disposition` proposals | Initiative-level |
| `IMPLEMENTATION` provides detailed specification depth; it does not hold work authority (PLAN) or decision authority (PROPOSAL GDR) | Initiative-level |

Reference rule:
- Same-activity session references MAY use shorthand forms such as `SES003-DEC001` when the activity scope is already explicit from context.
- Cross-activity session references MUST use fully-qualified timeline UIDs per `P-STD-005`.

### D. Recyclable-Loop Evidence Accumulation and Handoff

Rules:
- Each recycle cycle MUST produce cycle-local evidence rather than overwriting lineage.
- Rework under the same gate MUST preserve the same gate identity.
- Final gate packaging MUST preserve a navigable lineage from the active gate-facing evidence back to prior cycle evidence.

| Boundary | Required Outbound Artifact | Minimum Contents | Blocking Rule |
|:--|:--|:--|:--|
| Developer -> Verifier | DEV-REPORT | `source_plan`, `implementation_reference` when an IMPLEMENTATION artifact exists, `package_role`, `primary_report`, and `consolidated_from` when a multi-report package exists, traceability matrix, handoff section | Verifier MUST not start gate review until the developer evidence package is complete. |
| Verifier -> Consultant | VERIFICATION | Evidence Set coverage of the active producer-evidence package, findings or explicit no-findings posture, verifier verdict | Consultant MUST not package a gate disposition until verifier verdict and evidence coverage are present. |
| Consultant -> Developer | IMPLEMENTATION | Explicit task/gate linkage, references to the controlling approved GIR package or the controlling verification findings, depending on the path | Developer MUST not begin remediation or follow-on execution without explicit authority. |
| Consultant -> Client | PROPOSAL | Gate Package Index, Evidence Index, consultant recommendation, GDR when the archetype is `gate_disposition` | Client MUST not be asked to disposition the gate without the proposal package. |

Lineage rules:
- Supplementary DEV-REPORTs accumulate across bounded execution slices within the same package.
- Consolidated primary DEV-REPORTs point to supplementary reports through `consolidated_from`.
- VERIFICATION re-assessment remains same-gate and version-bumped rather than renamed to a new gate.
- Proposal evidence indexes SHOULD surface current active evidence first and preserve historical evidence as lineage context rather than deleting it.

This subsection does not alter the consultant/developer/verifier ownership model; it governs evidence flow and handoff obligations only.

**Superseded artifact linkage rules** (three-layer deprecation model):

When a gate is superseded (`Client Decision = SUPERSEDE`), artifacts produced for the superseded baseline are deprecated using a three-layer model. Each layer serves a different audience:

| Layer | Surface | Required Action | Purpose |
|:--|:--|:--|:--|
| **Layer 1: Frontmatter** | Superseded artifact (ANALYSIS, PROPOSAL, or VERIFICATION) | Set `status: 'superseded'`; add `superseded_by: '<successor-path>'`; add deprecation notice as first body line | Self-documenting: any reader of the artifact immediately sees it is not current |
| **Layer 2: Evidence Index** | Active successor gate-disposition proposal | Move superseded artifact from active evidence to a `Historical Evidence` subsection with `SUPERSEDED` annotation | Gate package clarity: verifier/client see only current evidence in the primary index |
| **Layer 3: Links Register** | Governing plan (plan-level Links Register) | Add or update links register entry with `superseded` annotation and successor reference | Plan traceability: plan-level audit trail shows the succession chain |

**Deprecation notice format** (Layer 1):
```
> **SUPERSEDED**: This artifact was produced against [baseline X]. It has been superseded by [successor artifact path] which assesses against [baseline Y]. This artifact is preserved for historical traceability only.
```

**Rule**: Superseded artifacts MUST NOT be deleted. They are preserved as historically valid records of work conducted under the prior baseline. Only `status` and the `superseded_by` frontmatter key are changed; the body content is not altered.

**Cross-reference**: For full supersession mechanics, see `guideline_workspace_plan.md` §VI.M and `guideline_workspace_proposal.md` §VII.D Step 4a. For analysis-artifact authoring guidance on `status: 'superseded'` and `superseded_by`, see `guideline_workspace_analysis.md` §IX.

---

## 8. ROLE-TO-ARTIFACT OWNERSHIP MATRIX

| Artifact Type | Author | Verifier | Approver / Decision Owner | Primary Consumer |
|:--|:--|:--|:--|:--|
| ROADMAP | LLM_Consultant | LLM_Consultant / Client as needed | Client where governed decisions apply | Consultant, Client, downstream roles |
| PLAN | LLM_Consultant or LLM_Planner per scope | Verifier only when gated | Client where approval gates apply | Consultant, Planner, Developer, Verifier |
| NOTES | LLM_Consultant | None by default | None by default | All roles |
| ANALYSIS | LLM_Consultant | Client / Consultant review as needed | Client when analysis drives approval | Consultant, Client |
| ANALYSIS (`external_review`) | LLM_Subconsultant | LLM_Consultant (mandatory review before gate) | Client via GDR (advisory input only) | Consultant, Client |
| PROPOSAL | LLM_Consultant | Verifier input when gate-backed | Client | Consultant, Client, downstream implementers |
| VERIFICATION | LLM_Reviewer (preferred future-state primary) / LLM_Consultant (currently authorized secondary) | Client consumes verdict | Client decides through GDR | Consultant, Client |
| DEV-REPORT | LLM_Developer | Verifier consumes as evidence | None directly | Verifier, Consultant |
| IMPLEMENTATION | LLM_Consultant (primary author/commissioner); LLM_Planner only when explicitly delegated by the consultant for decomposition support | Verifier consumes as re-assessment input | Client where gated | Developer, LLM_Assistant, Verifier, designated agentic executors |

Source: `T104-RES-003` Topic 8 (Workspace Artifact Integration & Industry Benchmark Analysis).

---

## 9. FILE NAMING & DIRECTORY CONVENTIONS

This workspace adopts the approved directory and file naming conventions defined in:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` (`P-STD-004`)

**Summary (workspace-relevant)**:
- Artifact file prefixes MUST match artifact type (e.g., `plan_`, `notes_`, `roadmap_`, `analysis_`, `proposal_`).
- Developer-facing implementation task specifications retain `-task-specification`; consultant/assistant orchestration artifacts use `-brief`; remediation artifacts retain `-remediation-specification`.
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

Workspace guideline changelogs are externalized to dedicated files. The `CHANGELOG` section in each main guideline MUST be a pointer only, and the version table MUST live in the dedicated file listed below.

| Document | Dedicated changelog file |
|:--|:--|
| `workspace_documentation_rules.md` | `prompt/templates/consultant/workspace/changelog/changelog_workspace_documentation_rules.md` |
| `guideline_workspace_plan.md` | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_plan.md` |
| `guideline_workspace_analysis.md` | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_analysis.md` |
| `guideline_workspace_dev-report.md` | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_dev-report.md` |
| `guideline_workspace_implementation.md` | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_implementation.md` |
| `guideline_workspace_notes.md` | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_notes.md` |
| `guideline_workspace_proposal.md` | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_proposal.md` |
| `guideline_workspace_roadmap.md` | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_roadmap.md` |
| `guideline_workspace_verification.md` | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_verification.md` |

Rule:
- Every workspace guideline MUST end with a `CHANGELOG` section containing only the repo-relative path to its dedicated changelog file.
- The dedicated changelog file MUST be the only place where version rows are added, amended, or reordered.
- The dedicated changelog file MUST live under `prompt/templates/consultant/workspace/changelog/`.
