---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'proposal_authoring'
version: '1.8.0'
date: '2026-03-20'
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
5. Consultant Gate Recommendation
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
- The GDR carries two decision signals: the **Consultant Recommendation** (advisory) and the **Client Decision** (authoritative). The reviewer verdict is recorded only in the verification artifact and is NOT duplicated into the GDR.
- **Plan-level positioning**: The gate-disposition proposal task SHOULD appear as part of the Gate-Readiness Stack — after the verification task for implementation-backed gates, or immediately before the gate row for consultation-only gates. The gate construct MUST include a `Gate-Disposition Proposal` field referencing the proposal path. For the full pattern, see `guideline_workspace_plan.md` §VI.L.

### B. Verification gate

- Verification gates require reviewer-owned verification evidence and verdict taxonomy per `guideline_workspace_verification.md`.
- The verification artifact carries the reviewer verdict in its Gate Recommendation section (§VII of verification template). The reviewer verdict is NOT duplicated into the GDR.
- The `gate_disposition` proposal's Consultant Gate Recommendation section (§V) MUST state whether the consultant recommendation aligns with or departs from the reviewer's verdict, with a reference to the verification artifact.
- Proposal artifacts MUST NOT substitute for verification artifacts when gate purpose is quality/compliance verification.
- When consultant recommendation or client decision is `RECYCLE`, the proposal MUST describe the same-gate reassessment loop and MUST NOT imply that downstream gate-dependent work may start before reassessment.

> **Internal vs External Impact**: `RECYCLE` is the correct decision for **internal recycle** — where the gate review identified deficiencies within the original scope and the decision boundary is unchanged. When a disruption originates from an **external event** (outside the gate's review scope) and changes the decision boundary, `SUPERSEDE` is the correct decision. See §VII.C for the `SUPERSEDE` enum and `guideline_workspace_plan.md` §VI.M for the full classification test and supersession mechanics.

### C. GDR Field Specification

Every `gate_disposition` proposal MUST include a Gate Decision Record as the penultimate section (before Changelog):

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `<GATE-ID>` |
| Consultant Recommendation | [APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT / SUPERSEDE] |
| Client Decision | [APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT / SUPERSEDE] |
| Gate Status After Decision | [completed / in_progress / failed / pending / superseded] |
| Conditions (if any) | [enumerated list or "—"] |
| Decided By | Client |
| Decision Date | YYYY-MM-DD |
| Decision Reference | [session notes path, inline statement, or "pending"] |

**Consultant Recommendation field rules**:
- The Consultant Recommendation is the consultant's consolidated gate-level advisory signal, synthesizing all GIR item dispositions into a single recommendation using the Client Decision taxonomy (`APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT / SUPERSEDE`).
- For implementation-backed gates (where a verification artifact exists): the Consultant Gate Recommendation section (§V) MUST state whether the recommendation aligns with or departs from the reviewer's verdict recorded in the verification artifact. The reviewer verdict is NOT duplicated into the GDR.
- For consultation-only gates (no verification artifact): the Consultant Recommendation is the sole advisory signal. No reviewer verdict exists to reference.

**Gate Status After Decision field rules**:
- `pending` is used only while the GDR is awaiting a client decision.
- `completed` is used when `Client Decision` is `APPROVE` or `APPROVE WITH CONDITIONS`.
- `in_progress` is used when `Client Decision` is `RECYCLE`; the gate remains open and the same gate ID is reassessed after remediation.
- `failed` is used when `Client Decision` is `REJECT`.
- `superseded` is used when `Client Decision` is `SUPERSEDE`; the gate is closed due to an external baseline change. A successor gate with the updated baseline replaces this gate. The prior assessment is preserved as historically valid-for-baseline.

**RECYCLE-specific GDR rule**:
- When `Client Decision = RECYCLE`, `Conditions (if any)` MUST enumerate the remediation tasks/sub-tasks and the re-entry basis required before the same gate is reassessed.

**SUPERSEDE-specific GDR rule**:
- When `Client Decision = SUPERSEDE`, `Conditions (if any)` MUST reference (a) the successor gate ID and (b) the external event that triggered supersession. The prior assessment is preserved as historically valid-for-baseline and MUST NOT be deleted or retroactively corrected.
- The superseded gate's GDR is a permanent historical record. Its `status` is updated to `superseded`; no other fields are changed retroactively except the `Conditions` and `Decision Date`.

**Prior-assessment preservation rule**:
- When a gate is superseded (`Client Decision = SUPERSEDE`), the prior GDR's assessment record is preserved as historically valid-for-baseline. The superseded gate-disposition proposal artifact's frontmatter is updated to `status: 'superseded'` with a `superseded_by` key pointing to the successor gate's proposal. A deprecation notice is added as the first body line. The prior assessment record itself is not altered.
- This rule distinguishes supersession from rejection: `REJECT` terminates work; `SUPERSEDE` terminates only the gate's baseline context, not the validity of the work done under that baseline.

### D. GDR Lifecycle

1. Proposal artifact is authored with GDR section populated as: `Consultant Recommendation: <consultant's recommendation>`, `Client Decision: pending`, `Gate Status After Decision: pending`, `Decision Date: —`, `Decision Reference: pending`. The Consultant Recommendation is populated at authoring time (not pending), as it represents the consultant's advisory signal that informs the client's decision.
2. Client reviews the gate package (proposal + any supporting verification/analysis artifacts).
3. Client issues decision signal (in session, via message, or inline).
4. GDR section is updated by the facilitating role (LLM_Consultant) to record the client's decision.

**Step 4a — External-Impact Assessment (Conditional)**:

> This step activates when an external event is identified that may affect the gate's normative baseline, either before or after the client has reviewed the gate package. It is a conditional branch — if no external event is detected, proceed directly from step 4 to step 5.

> 4a.1. The facilitating role (LLM_Consultant) performs an external-impact classification:
>   - **Classification test**: "Did the event originate from this gate's own review process?" If yes → Internal impact → continue with steps 4–7 normally (§VI.K recycle if RECYCLE, normal close if APPROVE/REJECT). If no → External impact → continue.
>   - **Decision-Boundary Test**: "Does the external event change the decision boundary (the normative standard/baseline cited in the gate's entry criteria, or the scope of the decision the gate is asked to make)?"
>
> 4a.2. If the decision boundary is **unchanged** (inputs-only external impact): Continue with existing GDR lifecycle. The gate remains the same gate ID. Updated inputs are incorporated into the gate package.
>
> 4a.3. If the decision boundary is **changed**: Gate supersession is triggered.
>   - The facilitating role updates the current gate's GDR: `Client Decision: SUPERSEDE`, `Gate Status After Decision: superseded`, `Conditions: <successor gate ID> + <external event description>`, `Decision Reference: <session notes path>`.
>   - A successor gate is created in the plan with a new gate ID and updated entry criteria referencing the new baseline.
>   - A new gate-disposition proposal is authored for the successor gate with GDR in `pending` state.
>   - The superseded gate's proposal frontmatter is updated: `status: 'superseded'`, `superseded_by: '<successor proposal path>'`.
>   - The superseded gate's analysis and verification artifacts are deprecated per the three-layer model (see `guideline_workspace_analysis.md` §IX and `workspace_documentation_rules.md` §7.C).

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
| v1.8.0 | 2026-03-21 | Maintenance | §VII.C: Added `SUPERSEDE` to the Consultant Recommendation field rules prose parenthetical to match the GDR table enum. OBS-001 cleanup from T104-PH001-ST008-AC001.4-GATE-002 verification observation. Source: T104-PH001-ST008-AC001.4 GATE-002 (2026-03-20). |
| v1.7.0 | 2026-03-20 | Amendment | §VII.C: Added `SUPERSEDE` to `Client Decision` and `Consultant Recommendation` enum values; added `superseded` to `Gate Status After Decision` enum; added SUPERSEDE-specific GDR rule (conditions MUST reference successor gate ID + external event); added prior-assessment preservation rule. §VII.D: Added Step 4a (external-impact assessment conditional branch) between steps 4 and 5 — classification test, decision-boundary test, inputs-only path, and supersession path with proposal/artifact update instructions. §VII.B: Added clarifying note distinguishing internal RECYCLE (§VI.K of plan guideline) from external-impact SUPERSEDE (§VI.M of plan guideline). Source: T104-PH001-ST008-AC001.4 GATE-001 (2026-03-20). |
| v1.6.0 | 2026-03-20 | Amendment | §VII.C: Replaced `Reviewer Verdict` with `Consultant Recommendation` in GDR field specification. New field uses Client Decision taxonomy (`APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT`) as the consultant's consolidated gate-level advisory signal. Reviewer verdict remains only in the verification artifact per `T104-CON-001` (Link Don't Duplicate). §VII.A/B: Updated gate semantics to reflect three-signal model (reviewer verdict in verification, consultant recommendation in GDR, client decision in GDR). §V.B: Renamed Section 5 to "Consultant Gate Recommendation". §VII.D: Updated GDR lifecycle to populate consultant recommendation at authoring time. Source: T104-PH001-ST008-AC001.5. |
| v1.5.0 | 2026-03-16 | Amendment | Clarified §VII.A plan-level positioning for gate-disposition proposals: implementation-backed gates place the proposal after verification; consultation-only gates place it immediately before the gate with no verification artifact required. Source: P-PH000-ST002-AC002 Gate 001 consultation. |
| v1.4.0 | 2026-03-15 | Amendment | §VII.A: Added Gate-Readiness Stack cross-reference to `guideline_workspace_plan.md` §VI.L for plan-level positioning of gate-disposition proposal tasks and mandatory `Gate-Disposition Proposal` gate field. Source: T104-PH001-ST008-AC001.2. |
| v1.3.0 | 2026-03-15 | Amendment | Split complex schema mappings (§IV/§VIII) into distinct sections: §VIII (Artifact vs Package Concept), §IX (Package Layout Examples), and §X (Template Inventory). Eliminated nested index-of-arrays representation. Refined `gate_disposition` definition in §V.B to resolve template drift. Source: T104-PH001-ST008-AC002 (GATE-002 Verification). |
| v1.2.0 | 2026-03-12 | Amendment | Clarified verification-gate RECYCLE handling in §VII. Added `Gate Status After Decision` to the GDR, defined RECYCLE as same-gate reassessment with `in_progress` gate status, required remediation/re-entry details in RECYCLE conditions, and made downstream blocking explicit until the same gate later receives an approving decision. |
| v1.1.0 | 2026-03-04 | Amendment | §VII expanded from "Decision Gate vs Verification Gate Semantics" to "Gate Semantics & Gate Decision Record (GDR)". Now includes full GDR field specification (§VII.C), GDR lifecycle (§VII.D), and GDR enforcement (§VII.E) — migrated from `guideline_workspace_verification.md` §X per T104-PH001-ST008-AC001 Option B approval. Proposal guideline is now the sole normative GDR authority. |
| v1.0.0 | 2026-03-03 | Initial | Draft 1 proposal authoring guideline delivered for AC008 TK002. Encodes GATE-000 decisions for archetype taxonomy, multi-template posture, frontmatter baseline, gate semantics, authority references, naming/placement, and template inventory. |
