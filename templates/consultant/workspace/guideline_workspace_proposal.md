---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'proposal_authoring'
version: '1.4.0'
date: '2026-03-15'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/plan_T104-PH001-ST005.md'
decision_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC008/proposal/proposal_T104-PH001-ST005-AC008-TK001.1_gir-disposition-package.md'
template_references:
  - 'prompt/templates/consultant/workspace/template_workspace_proposal_eid-workspace.md'
  - 'prompt/templates/consultant/workspace/template_workspace_proposal_gate-disposition.md'
  - 'prompt/templates/consultant/workspace/template_workspace_proposal_promotion-contract.md'
  - 'prompt/templates/consultant/workspace/template_workspace_proposal_standards-input.md'
---

# Proposal Procedural Guideline (Consultant Workspace)

## I. PURPOSE

Define authoring rules for PROPOSAL workspace artifacts so they are:
- archetype-specific and deterministic,
- aligned to approved gate decisions,
- compatible with naming/placement authority (`P-STD-004`) and ID authority (`P-STD-005`),
- explicit about decision gates vs verification gates.

This guideline is Draft 1 and is governed by AC008 GATE-000 decisions (GIR-001 through GIR-014).

---

## II. ROLE BOUNDARY

- **LLM_Consultant** is the primary author of proposal artifacts.
- **Client** is the decision owner for proposal approval and gate closure.
- **LLM_Reviewer** owns VERIFICATION artifacts and reviewer verdicts for verification gates.
- **LLM_Developer** consumes approved proposal outputs and executes implementation tasks.

Boundary rules:
- Proposal artifacts may contain recommendations and deterministic execution instructions.
- Proposal artifacts MUST NOT claim verification-gate evidence closure unless the gate is explicitly a decision disposition gate and uses a proposal-embedded GDR.

---

## III. PROPOSAL ARCHETYPE TAXONOMY (LOCKED)

Draft 1 allows exactly four proposal archetypes:

1. `eid_workspace`
- Working-index style proposal for iterative E-ID development.
- Template: `template_workspace_proposal_eid-workspace.md`.

2. `gate_disposition`
- Decision package used to resolve gate decision items and record Client disposition.
- Template: `template_workspace_proposal_gate-disposition.md`.

3. `promotion_contract`
- Mechanical transfer contract used to promote content from source artifact(s) to target artifact(s).
- Template: `template_workspace_proposal_promotion-contract.md`.

4. `standards_input`
- Analysis-driven recommendation package intended as input to standards authoring.
- Template: `template_workspace_proposal_standards-input.md`.

Rule: multi-template posture is mandatory. A single, conditional mega-template is not permitted for Draft 1.

---

## IV. LIFECYCLE PER ARCHETYPE

| Archetype | Trigger | Editing posture | Approval signal | Closure posture |
|:--|:--|:--|:--|:--|
| `eid_workspace` | Need iterative decision drafting for E-ID surfaces | Evolving workspace during consultation | Client approval of proposal or downstream gate | Promoted outputs move to SSOT/standards as applicable; proposal remains audit trail |
| `gate_disposition` | Gate decision set must be dispositioned before downstream tasks | Decision register refined until recommendation package is complete | Gate Decision Record (GDR) in the proposal | Gate closes when GDR records APPROVE or APPROVE WITH CONDITIONS |
| `promotion_contract` | Content transfer/promotion requires deterministic instructions | Mechanical mapping and replacement instructions only | Client approval of contract gate/task | Execution follows exact contract steps; source/target traces retained |
| `standards_input` | Standardization initiative requires structured conventions proposal | Analysis + recommendation synthesis | Client approval of proposal for standard drafting intake | Inputs are consumed by standards drafting tasks |

---

## V. REQUIRED STRUCTURE BY ARCHETYPE

All proposal artifacts MUST include these sections:
- Executive Summary
- References
- Changelog

Archetype-specific required sections:

### A. `eid_workspace`

Required ordered sections:
1. Executive Summary
2. Candidate Inventory (working index)
3. Candidate Bodies / Normative Draft Content
4. Decision Record Index and Bodies (when applicable)
5. References
6. Changelog

### B. `gate_disposition`

Required ordered sections:
1. Executive Summary
2. Gate Package
3. Disposition Summary Register
4. Detailed Disposition Register
5. Gate Recommendation
6. Gate Decision Record
7. References
8. Changelog

Disposition item token rule: use `GIR-###`.

**Gate Package section specification**:

The Gate Package section (Section II) MUST include two subsections:

**A. Gate Package Index** — A deliverables-oriented table showing what was produced up to the gate, its status, and reading guidance for the client. This is the client's primary navigation surface.

Required columns: `| Deliverable | Producing Task | Status | Acceptance | Client Priority | Path |`

Column definitions:
- `Deliverable`: Plain-language name of the output (e.g., "Research Report", "Verification Report")
- `Producing Task`: The task ID that produced this deliverable (e.g., `TK002`)
- `Status`: Deliverable completion status per `P-STD-002` (e.g., `completed`, `in_progress`)
- `Acceptance`: Gate-level acceptance status: `accepted`, `accepted-provisional`, `blocked`, `pending`, or `N/A`
- `Client Priority`: Reading guidance for the client: `Required` (client must review), `Recommended` (client should review for context), `Reference` (available if needed)
- `Path`: Repo-relative path to the deliverable

**B. Evidence Index** — The existing governance traceability table linking all artifacts reviewed at the gate.

Required columns: `| Evidence Type | Artifact | Path | Notes |`

This table retains its current purpose: linking evidence artifacts (verification, analysis, plans, standards) for audit traceability. It MAY include artifacts not listed in the Gate Package Index (e.g., governing standards, prior gate records, session notes).

### C. `promotion_contract`

Required ordered sections:
1. Purpose
2. Scope and Preconditions
3. Mapping Tables
4. Replacement Rules
5. Exact New Content Blocks
6. Implementation Execution Notes
7. References
8. Changelog

### D. `standards_input`

Required ordered sections:
1. Purpose
2. Current State Summary
3. Proposed Conventions
4. Decision Requests
5. Impact and Risks
6. References
7. Changelog

---

## VI. FRONTMATTER CONVENTIONS

### A. Common required keys

Every proposal artifact MUST include:
- `artifact_type: 'PROPOSAL'`
- `initiative_id`
- `version`
- `date`
- `status`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`
- `plan_reference`

### B. Common recommended keys

When applicable, include:
- `initiative_code`
- `phase`
- `stream_id`
- `activity_id`
- `task_id`
- `gate_id`
- `analysis_reference`
- `purpose`
- `consumers`

### C. Archetype-specific optional keys

- `eid_workspace`:
  - `target_document`, `target_section`, `session_reference`
- `gate_disposition`:
  - `gate_id`, `analysis_reference`, `external_review_reference`, `consumers`
- `promotion_contract`:
  - `source_standard`, `target_standard`, `session_reference`
- `standards_input`:
  - `target_standards`, `analysis_reference`, `external_review_reference`

Policy: additional optional keys are permitted when justified by the archetype; common required keys MUST NOT be omitted.

---

## VII. GATE SEMANTICS & GATE DECISION RECORD (GDR)

### A. Decision gate (`gate_disposition` proposals)

- A decision gate is used to disposition design choices before downstream execution.
- The authoritative approval signal is the proposal-embedded `## Gate Decision Record` section.
- Decision-gate proposals MAY use a proposal-embedded GDR without a separate verification artifact.
- When a verification artifact also exists for the same gate, the proposal-embedded GDR is the authoritative decision record.
- **Plan-level positioning**: The gate-disposition proposal task SHOULD appear as part of the Gate-Readiness Stack — after the verification task and immediately before the gate row in the plan's Task Register. The gate construct MUST include a `Gate-Disposition Proposal` field referencing the proposal path. For the full pattern, see `guideline_workspace_plan.md` §VI.L.

### B. Verification gate

- Verification gates require reviewer-owned verification evidence and verdict taxonomy per `guideline_workspace_verification.md`.
- The verification artifact carries the reviewer verdict in its Gate Recommendation section (§VII of verification template).
- The `gate_disposition` proposal aggregates the reviewer verdict into its GDR alongside the client decision.
- Proposal artifacts MUST NOT substitute for verification artifacts when gate purpose is quality/compliance verification.
- When reviewer verdict or client decision is `RECYCLE`, the proposal MUST describe the same-gate reassessment loop and MUST NOT imply that downstream gate-dependent work may start before reassessment.

### C. GDR Field Specification

Every `gate_disposition` proposal MUST include a Gate Decision Record as the penultimate section (before Changelog):

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `<GATE-ID>` |
| Reviewer Verdict | [PASS / CONDITIONAL PASS / PASS WITH DEFERRALS / RECYCLE / FAIL / N/A — decision gate] |
| Client Decision | [APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT] |
| Gate Status After Decision | [completed / in_progress / failed / pending] |
| Conditions (if any) | [enumerated list or "—"] |
| Decided By | Client |
| Decision Date | YYYY-MM-DD |
| Decision Reference | [session notes path, inline statement, or "pending"] |

**Reviewer Verdict field rules**:
- When a verification artifact exists for the same gate: the Reviewer Verdict MUST match the verdict recorded in the verification artifact's Gate Recommendation section.
- When no verification artifact exists (pure decision gate): the Reviewer Verdict SHOULD be set to the consultant's recommendation verdict, or `N/A — decision gate` if no formal recommendation is applicable.

**Gate Status After Decision field rules**:
- `pending` is used only while the GDR is awaiting a client decision.
- `completed` is used when `Client Decision` is `APPROVE` or `APPROVE WITH CONDITIONS`.
- `in_progress` is used when `Client Decision` is `RECYCLE`; the gate remains open and the same gate ID is reassessed after remediation.
- `failed` is used when `Client Decision` is `REJECT`.

**RECYCLE-specific GDR rule**:
- When `Client Decision = RECYCLE`, `Conditions (if any)` MUST enumerate the remediation tasks/sub-tasks and the re-entry basis required before the same gate is reassessed.

### D. GDR Lifecycle

1. Proposal artifact is authored with GDR section populated as: `Client Decision: pending`, `Gate Status After Decision: pending`, `Decision Date: —`, `Decision Reference: pending`.
2. Client reviews the gate package (proposal + any supporting verification/analysis artifacts).
3. Client issues decision signal (in session, via message, or inline).
4. GDR section is updated by the facilitating role (LLM_Consultant) to record the client's decision.
5. Proposal artifact is version-bumped if other content changes accompany the decision recording.
6. Gate status in the plan task register is updated per `guideline_workspace_verification.md` §VIII mapping.
7. A `RECYCLE` decision records a non-closing client disposition: the gate remains `in_progress`, the same gate ID is preserved for reassessment, and downstream gate-dependent tasks remain blocked.

### E. GDR Enforcement

- Any task with `Depends On: GATE-###` MUST verify that the gate's `gate_disposition` proposal contains a GDR with `Client Decision` = APPROVE or APPROVE WITH CONDITIONS.
- A GDR with `Client Decision: pending` does NOT satisfy downstream dependencies.
- A GDR with `Client Decision: RECYCLE` does NOT satisfy downstream dependencies, even if remediation tasks have been completed.
- If a gate has both a verification artifact and a proposal, the GDR in the proposal is the authoritative decision record.

### F. Shared enforcement rule

Downstream tasks with gate dependency MUST verify that the governing gate artifact contains a populated GDR with an approving client decision state.

---

## VIII. AUTHORITY REFERENCES

Primary authority references for proposal authoring:
- `P-STD-001` (governance and DR handling where applicable)
- `P-STD-004` (naming and placement)
- `P-STD-005` (ID schema)

Legacy `T102-STD-*` references MAY appear as informative aliases only.

---

## IX. NAMING AND PLACEMENT

### A. Filename pattern

Proposal artifacts MUST use:
- `proposal_<scope-UID>_<kebab-topic>.md`

### B. Placement rule (scope aligned)

Placement MUST follow `P-STD-004-CLAUSE-003F`:
- If `<scope-UID>` contains `AC###`, place under `workspace/PH###/ST###/AC###/proposal/`.
- Otherwise, place under `workspace/PH###/ST###/proposal/`.

### C. Template naming rule

Template files MUST use:
- `template_workspace_proposal_<kebab-archetype>.md`

---

## X. TEMPLATE INVENTORY

Active proposal templates:
- `prompt/templates/consultant/workspace/template_workspace_proposal_eid-workspace.md`
- `prompt/templates/consultant/workspace/template_workspace_proposal_gate-disposition.md`
- `prompt/templates/consultant/workspace/template_workspace_proposal_promotion-contract.md`
- `prompt/templates/consultant/workspace/template_workspace_proposal_standards-input.md`

Legacy compatibility surface:
- `prompt/templates/consultant/workspace/template_workspace_proposal.md` (deprecated stub)
- Archived full legacy content: `prompt/templates/consultant/workspace/archive/deprecated/template_workspace_proposal.md`

---

## XI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.4.0 | 2026-03-15 | Amendment | §VII.A: Added Gate-Readiness Stack cross-reference to `guideline_workspace_plan.md` §VI.L for plan-level positioning of gate-disposition proposal tasks and mandatory `Gate-Disposition Proposal` gate field. Source: T104-PH001-ST008-AC001.2. |
| v1.3.0 | 2026-03-15 | Amendment | Split complex schema mappings (§IV/§VIII) into distinct sections: §VIII (Artifact vs Package Concept), §IX (Package Layout Examples), and §X (Template Inventory). Eliminated nested index-of-arrays representation. Refined `gate_disposition` definition in §V.B to resolve template drift. Source: T104-PH001-ST008-AC002 (GATE-002 Verification). |
| v1.2.0 | 2026-03-12 | Amendment | Clarified verification-gate RECYCLE handling in §VII. Added `Gate Status After Decision` to the GDR, defined RECYCLE as same-gate reassessment with `in_progress` gate status, required remediation/re-entry details in RECYCLE conditions, and made downstream blocking explicit until the same gate later receives an approving decision. |
| v1.1.0 | 2026-03-04 | Amendment | §VII expanded from "Decision Gate vs Verification Gate Semantics" to "Gate Semantics & Gate Decision Record (GDR)". Now includes full GDR field specification (§VII.C), GDR lifecycle (§VII.D), and GDR enforcement (§VII.E) — migrated from `guideline_workspace_verification.md` §X per T104-PH001-ST008-AC001 Option B approval. Proposal guideline is now the sole normative GDR authority. |
| v1.0.0 | 2026-03-03 | Initial | Draft 1 proposal authoring guideline delivered for AC008 TK002. Encodes GATE-000 decisions for archetype taxonomy, multi-template posture, frontmatter baseline, gate semantics, authority references, naming/placement, and template inventory. |
