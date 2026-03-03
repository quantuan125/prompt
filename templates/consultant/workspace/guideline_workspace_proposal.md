---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'proposal_authoring'
version: '1.0.0'
date: '2026-03-03'
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
2. Evidence Index
3. Disposition Summary Register
4. Detailed Disposition Register
5. Gate Recommendation
6. Gate Decision Record
7. References
8. Changelog

Disposition item token rule: use `GIR-###`.

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

## VII. DECISION GATE VS VERIFICATION GATE SEMANTICS

### A. Decision gate (`gate_disposition` proposals)

- A decision gate is used to disposition design choices before downstream execution.
- The authoritative approval signal is the proposal-embedded `## Gate Decision Record` section.
- Decision-gate proposals MAY use a proposal-embedded GDR without a separate verification artifact.

### B. Verification gate

- Verification gates require reviewer-owned verification evidence and verdict taxonomy per `guideline_workspace_verification.md`.
- Proposal artifacts MUST NOT substitute for verification artifacts when gate purpose is quality/compliance verification.

### C. Shared enforcement rule

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
| v1.0.0 | 2026-03-03 | Initial | Draft 1 proposal authoring guideline delivered for AC008 TK002. Encodes GATE-000 decisions for archetype taxonomy, multi-template posture, frontmatter baseline, gate semantics, authority references, naming/placement, and template inventory. |
