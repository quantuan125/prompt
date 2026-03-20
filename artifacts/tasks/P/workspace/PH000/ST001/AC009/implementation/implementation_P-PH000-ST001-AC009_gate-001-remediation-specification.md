---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'remediation_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC009'
gate_id: 'P-PH000-ST001-AC009-GATE-001'
task_id: 'P-PH000-ST001-AC009-TK005.1'
version: '1.0.0'
date: '2026-03-20'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md'
verification_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001.md'
proposal_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md'
purpose: 'Governed remediation specification for the AC009 Gate-001 recycle loop. Supersedes the temporary revision-checklist as the authoritative HOW-to-fix surface for remediating the gate package and reassessing the same gate ID.'
---

# IMPLEMENTATION (Remediation Specification): GATE-001 Remediation - `P-PH000-ST001-AC009`

## I. PURPOSE & AUTHORITY

- Purpose: Specify the corrective implementation work required to turn the current AC009 Gate-001 recycle posture into a clean reassessment package.
- Authority chain: Plan authorizes work (`P-PH000-ST001-AC009-TK005.1` through `TK005.5`) -> this artifact specifies HOW -> dev-report records execution evidence -> verification re-assesses -> proposal hosts the authoritative GDR.
- Audience: `LLM_Developer` (primary), `LLM_Reviewer` (re-assessment input), `LLM_Consultant` (proposal refresh).
- This artifact does NOT hold a GDR. Gate decision authority remains exclusively in the gate-disposition proposal.

## II. REMEDIATION SCOPE

- Gate: `P-PH000-ST001-AC009-GATE-001`
- Trigger: Active recycle/reassessment loop for the same gate ID.
- Governing plan task: `P-PH000-ST001-AC009-TK005.1`
- Trigger references:
  - `GAP-001` through `GAP-005` in `analysis_P-PH000-ST001-AC009_external-review_gate-001-package.md`
  - Gate-001 proposal recommendation state `RECYCLE`
  - Temporary revision-checklist supersession decision after AC001.3 closed the IMPLEMENTATION-family governance gap

## III. REMEDIATION ITEMS

### REM-001 — Program-Scope Normative Vocabulary Authority

| Field | Detail |
|:--|:--|
| Trigger Reference | `GAP-001` |
| Implementation Detail | Amend `P-STD-001-CLAUSE-008` and the `Normative References` section together so `P-STD-001` no longer presents `T102-CON-009` as the unqualified steady-state normative authority for program-scope drafting. The final wording must keep BCP 14 drafting guidance while expressing a bounded program-scope adoption rule that is compliant with current `P-STD-005` directionality constraints. |
| Expected Format | One coherent authority story across `CLAUSE-008`, `Normative References`, and any derivative guidance that discusses normative vocabulary usage. |
| Acceptance Criteria | `P-STD-001` no longer reads as normatively anchored to a lower-scope source in steady state; clause text and references tell the same story; no derivative file contradicts the updated authority stance. |
| Resolution Status | `open` |

### REM-002 — References Posture Cleanup

| Field | Detail |
|:--|:--|
| Trigger Reference | `GAP-002` |
| Implementation Detail | Rework the `P-STD-001` `References` section so all rows are current-state, scope-clean, and justified. Include `P-STD-004` if placement/naming rules are relied upon. Remove or demote stale T102-era references that are no longer needed as active program-standard support. |
| Expected Format | Rebuilt `### Normative References` and `### Informative References` tables using the governed row schema. |
| Acceptance Criteria | Every reference row has a present-tense purpose; `P-STD-004` is represented consistently with how the standard actually relies on it; legacy T102 rows are removed or explicitly justified. |
| Resolution Status | `open` |

### REM-003 — Provenance Contract Tightening

| Field | Detail |
|:--|:--|
| Trigger Reference | `GAP-003` |
| Implementation Detail | Tighten the `P-STD-001` Provenance rendering and the derivative guidance/template contract so the section stays compact, table-friendly, and LLM-consumable without losing the minimum taxonomy introduced by AC009. The governed contract must describe the compact form rather than leaving it as one-off local formatting. |
| Expected Format | Matching updates to `P-STD-001`, `guideline_standard_specs.md`, and `template_standard_specs.md`. |
| Acceptance Criteria | Frontmatter remains the current-state authority; Provenance remains the lineage/history/input-source authority; the compact structure is governed consistently across the standard and its derivatives. |
| Resolution Status | `open` |

### REM-004 — SPS vs Standard Responsibility Boundary

| Field | Detail |
|:--|:--|
| Trigger Reference | `GAP-002`, AC009 consultation comments |
| Implementation Detail | Reduce drift between `sps_P-PROGRAM.md` and `P-STD-001` so SPS remains a registry/summary surface and the standard remains the detailed behavioral authority. Keep `P-CON-003` concise and ensure the `P-STD-001` body entry does not restate unnecessary internal detail. |
| Expected Format | Targeted SPS edits only; no redesign of the SPS artifact contract. |
| Acceptance Criteria | SPS no longer duplicates detailed standard behavior beyond registry/constraint needs; `P-CON-003` still points to the right governing clause family; boundary is cleanly explainable in the gate package. |
| Resolution Status | `open` |

### REM-005 — Gate Package Reassessment Inputs

| Field | Detail |
|:--|:--|
| Trigger Reference | `GAP-004`, `GAP-005` |
| Implementation Detail | Refresh the AC009 recycle package so the new IMPLEMENTATION artifact replaces the temporary revision-checklist as the live remediation-detail surface, AC001.3 is treated as resolved background context rather than an open blocker, and the reassessment stack is internally coherent. |
| Expected Format | Updated plan, historical checklist note, recycle dev-report, refreshed verification, refreshed proposal. |
| Acceptance Criteria | One live remediation-detail surface only; the proposal no longer asks the client to confirm temporary handling; the verification/proposal/package story is coherent for the same reassessment cycle. |
| Resolution Status | `open` |

## IV. IMPLEMENTATION SEQUENCE

1. Re-baseline the AC009 plan so the recycle loop is explicit.
2. Retire the temporary revision-checklist from live package use and author this remediation specification.
3. Execute `P-STD-001`, derivative, and SPS remediations.
4. Produce recycle dev-report evidence for the remediated package.
5. Re-run Gate-001 verification against the remediated evidence set.
6. Refresh the gate-disposition proposal and re-present the same gate ID.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/plan_P-PH000-ST001-AC009.md` |
| Gate-001 Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/verification/verification_P-PH000-ST001-AC009_gate-001.md` |
| Gate-001 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/proposal/proposal_P-PH000-ST001-AC009_gate-001_metadata-hardening-disposition.md` |
| External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009_external-review_gate-001-package.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-20 | Initial | Created the governed Gate-001 remediation specification for AC009. Supersedes the temporary revision-checklist as the live remediation-detail surface and translates GAP-001 through GAP-005 into execution-ready remediation items. |
