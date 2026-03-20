---
artifact_type: 'PROPOSAL'
proposal_type: 'STANDARDS_INPUT'
initiative_id: 'T104'
initiative_code: 'CWS'
phase_id: 'PH001'
stream_id: 'ST008'
activity_id: 'T104-PH001-ST008-AC001.6'
task_id: 'T104-PH001-ST008-AC001.6-TK002.1'
date: '2026-03-20'
version: '1.0.0'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration-audit.md'
external_review_reference: '—'
target_standards:
  - 'T104 workspace governance suite'
  - 'T104J-FEAT-004'
---

# Standards-Input Proposal: AC001.6 IMPLEMENTATION Vertical Integration Architecture

## 1. Purpose

Convert the architectural findings from `T104-PH001-ST008-AC001.6-TK002` into explicit standards-input requests that can be approved at `GATE-001` and then translated into bounded Phase 2 edits.

## 2. Architectural Gaps Requiring Standards Input

| Gap ID | Source Finding | Surface | Problem Summary | Recommended Treatment |
|:--|:--|:--|:--|:--|
| GAP-001 | `FINDING-001` | `guideline_workspace_verification.md` | Complex `RECYCLE` handling still treats `revision-checklist` as the detailed remediation-planning surface, which conflicts with the durable IMPLEMENTATION-family model accepted in AC001.3. | Approve a forward-routing rule that deprecates new complex-remediation use of `revision-checklist` and routes those cases to `IMPLEMENTATION remediation_specification`, while grandfathering existing historical files. |
| GAP-002 | `FINDING-002` | `guideline_workspace_dev-report.md` | DEV-REPORT guidance still lacks an explicit rule to cite the governing IMPLEMENTATION artifact when implementation work is executed under an approved implementation specification. | Approve a traceability rule requiring DEV-REPORT to reference the governing IMPLEMENTATION artifact when one exists. |
| GAP-003 | `FINDING-003` | `workspace_documentation_rules.md` | Live IMPLEMENTATION-family rows exist, but the RECYCLE workflow chain does not yet make the verification-to-remediation-specification handoff explicit enough to prevent future ambiguity. | Approve a wording refinement that explicitly describes the RECYCLE escalation path from VERIFICATION findings into IMPLEMENTATION remediation planning for complex cases. |

## 3. Proposed Conventions

### CONV-001: Complex RECYCLE Forward Routing

For new complex `RECYCLE` cases, `VERIFICATION` remains the reviewer-owned findings and verdict surface, while detailed remediation planning is recorded in `IMPLEMENTATION remediation_specification`. Existing `revision-checklist` artifacts remain valid historical records and do not require retroactive migration.

### CONV-002: DEV-REPORT Traceability to IMPLEMENTATION Authority

When implementation work is governed by an approved IMPLEMENTATION artifact, the DEV-REPORT must cite that artifact in its input or authority references so the implementation record remains traceable to the approved specification.

### CONV-003: Explicit RECYCLE Workflow Chain Wording

`workspace_documentation_rules.md` should state that complex remediation discovered during gate review flows from `VERIFICATION` into `IMPLEMENTATION remediation_specification`, rather than leaving that linkage implicit across multiple documents.

## 4. Decision Requests

### DEC-001: Verification Routing Standard

**Request**: Approve `CONV-001`.

**Options**:
- Option A: Approve forward-routing to `IMPLEMENTATION remediation_specification` for new complex RECYCLE cases; grandfather existing `revision-checklist` files.
- Option B: Keep `revision-checklist` as the primary detailed remediation-planning surface for complex RECYCLE cases.
- Option C: Maintain `revision-checklist` and `IMPLEMENTATION remediation_specification` indefinitely as peer first-class remediation-planning surfaces.

**Consultant Recommendation**: Option A.

**Rationale**: This matches the accepted AC001.3 durable-model decision, preserves role boundaries, and avoids maintaining two competing complex-remediation planning surfaces.

### DEC-002: DEV-REPORT Input Traceability Standard

**Request**: Approve `CONV-002`.

**Options**:
- Option A: Require DEV-REPORT to reference the governing IMPLEMENTATION artifact when one exists.
- Option B: Leave DEV-REPORT guidance unchanged and rely on informal practice.

**Consultant Recommendation**: Option A.

**Rationale**: This closes a traceability gap without changing artifact scope or ownership.

### DEC-003: Documentation-Rules Workflow Clarification

**Request**: Approve `CONV-003`.

**Options**:
- Option A: Add explicit RECYCLE workflow-chain wording connecting VERIFICATION findings to IMPLEMENTATION remediation planning for complex cases.
- Option B: Leave the current wording unchanged and rely on the distributed guideline set to imply the relationship.

**Consultant Recommendation**: Option A.

**Rationale**: Live state already includes most IMPLEMENTATION-family integration. This change narrows the remaining ambiguity without reopening the broader family design.

## 5. Approval Effect

If the Client approves all three decisions at `T104-PH001-ST008-AC001.6-GATE-001`, the approved standards input becomes the exact authority for the corresponding conditional Phase 2 edits. If any decision is rejected or modified, only the approved subset may proceed into Phase 2.
