---
artifact_type: 'PROPOSAL'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC004'
task_id: 'P-PH000-ST002-AC004-TK003.8'
version: '1.1.0'
date: '2026-03-27'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'
analysis_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_session-close-reminder-architecture-comparative-assessment.md'
external_review_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-002-package-qa-assessment.md'
target_standards:
  - 'AC004 successor session-close convention'
  - 'T104-PH001-ST008-AC001.10 governance hardening follow-on'
purpose: 'Structured standards-input proposal for the AC004 successor session-close convention, replacing premature concrete-skill authority in the GATE-002 package.'
---

# PROPOSAL: Standards Input - AC004 Successor Session-Close Convention

## I. PURPOSE

- Proposal objective: define the decision-ready session-close convention for AC004 successor gating without treating a premature concrete skill as active authority.
- Input scope: reminder-surface selection, governing protocol pointer, downstream operationalization boundary, and quarantine treatment for the pre-existing concrete skill file.
- Target standards: `AC004 successor session-close convention`; `T104-PH001-ST008-AC001.10 governance hardening follow-on`.

## II. CURRENT STATE SUMMARY

### A. Baseline

- The comparative analysis selected a dedicated session-close architecture over the historical wrap-up skill and the non-skill alternative.
- A concrete `prompt/skills/session-close/SKILL.md` was created before `P-PH000-ST002-AC004-GATE-002` approval, which contaminated the earlier successor package if treated as active evidence.
- The corrected package keeps the concrete file for lineage but removes it from active gate authority.
- The successor implementation specification still needs a stable, explicit pre-implementation source for session-close behavior.

### B. Problems / Gaps

| Gap ID | Category | Description | Impact |
|:--|:--|:--|:--|
| GAP-001 | lifecycle | The earlier successor package treated a premature concrete skill as if the gate had already approved it. | Gate-integrity failure: downstream work appeared partially executed before client disposition. |
| GAP-002 | workflow | The implementation specification still needs an explicit, pre-implementation authority source for session-close behavior. | Without a proposal-level authority surface, downstream execution could infer from the quarantined live file instead of client-approved guidance. |
| GAP-003 | governance | Workspace rules do not yet consistently state when a proposal-level convention is required instead of a prematurely materialized concrete artifact. | Future consultation-only gates could repeat the same contamination pattern. |

## III. PROPOSED CONVENTIONS

### A. Convention Set

| Convention ID | Rule | Rationale | Authority Link |
|:--|:--|:--|:--|
| CONV-001 | The active gate-time authority for AC004 session-close behavior is this `standards_input` proposal, not the live `prompt/skills/session-close/SKILL.md`. | Restores consultation-only gate purity while keeping the selected architecture explicit. | AC004 comparative analysis; live GATE-002 proposal; QA assessment |
| CONV-002 | `prompt/skills/session-close/SKILL.md` is preserved for lineage only until TK004 operationalizes the approved convention after gate approval. | Preserves audit traceability without normalizing premature downstream execution. | SES007 corrective session; live GATE-002 proposal |
| CONV-003 | The governing protocol pointer for session-close behavior is `prompt/artifacts/tasks/P/status/status_program.md` Section 7. | Keeps the operational protocol surface singular and bounded. | AC004 successor operating-model analysis |
| CONV-004 | The session-close convention focuses only on end-of-session status-surface checks and reconciliation triggers. It MUST NOT duplicate wrap-up or repo-wide productivity guidance. | Keeps AC004 V1 bounded and prevents spillover into unrelated guidance surfaces. | AC004 comparative analysis; successor implementation spec |
| CONV-005 | `prompt/skills/wrap-up/SKILL.md` remains historical-only context for AC004 V1 and MUST NOT remain the active reminder surface. | The client rejected the wrap-up-based reminder/tooling direction. | SES005; comparative analysis |
| CONV-006 | Downstream TK004 execution MUST reconcile the live `prompt/skills/session-close/SKILL.md` to this approved convention rather than treating the current file contents as already accepted. | Makes the operationalization boundary explicit and reviewable. | Successor implementation spec; live GATE-002 proposal; QA assessment |

### B. Compatibility Notes

- This proposal does not delete or amend the live concrete skill; it only changes the gate-authority posture around it.
- This proposal complements the successor implementation specification by providing the gate-approved convention source that SPEC-004 must operationalize later.
- This proposal is intentionally activity-scoped. Permanent rule hardening belongs to `T104-PH001-ST008-AC001.10`.

## IV. DECISION REQUESTS

| Decision ID | Prompt | Options | Recommendation | Owner |
|:--|:--|:--|:--|:--|
| DEC-001 | What should be the active gate-time authority for AC004 session-close behavior? | (a) this `standards_input` proposal; (b) the live `prompt/skills/session-close/SKILL.md`; (c) revert to wrap-up skill | **(a)** | Client |
| DEC-002 | How should the pre-existing concrete session-close skill be treated before TK004? | (a) preserve for lineage but keep non-authoritative until operationalized; (b) treat as already approved active surface; (c) delete it immediately | **(a)** | Client |
| DEC-003 | What should TK004 operationalize after gate approval? | (a) the approved session-close convention in this proposal; (b) the live concrete file as-is; (c) a non-skill prose-only reminder surface | **(a)** | Client |

## V. IMPACT AND RISKS

### A. Impact Assessment

- Positive outcomes:
  - restores gate-package integrity without losing lineage;
  - gives the successor implementation specification an explicit pre-implementation authority surface;
  - keeps the selected session-close architecture bounded to AC004 V1.
- Tradeoffs:
  - introduces one more artifact into the gate package;
  - requires downstream authors to distinguish carefully between the approved convention and the quarantined live file;
  - leaves permanent governance hardening to AC001.10 rather than solving it entirely inside AC004.

### B. Risks

| Risk ID | Description | Severity | Mitigation |
|:--|:--|:--|:--|
| RISK-001 | Later authors may still cite the quarantined concrete skill as if it were active gate authority. | medium | QA assessment and live GATE-002 proposal explicitly classify the file as historical/non-authoritative until TK004. |
| RISK-002 | Session-close detail may drift between this proposal and the downstream concrete skill. | medium | SPEC-004 in the successor implementation specification explicitly requires reconciliation to this approved convention. |
| RISK-003 | The repo may accumulate more proposal-level conventions without a durable governance rule. | medium | AC001.10 is widened to codify when `standards_input` must be used instead of premature concrete artifacts. |

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| Comparative Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_session-close-reminder-architecture-comparative-assessment.md` |
| Successor Operating-Model Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_successor-operating-model-and-reconciliation-policy.md` |
| Live GATE-002 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md` |
| Authoritative External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-002-package-qa-assessment.md` |
| Current Corrective Session Notes | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES007.md` |
| Historical Corrected External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004-GATE-002_external-review.md` |
| Historical Corrective Session Notes | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES006.md` |
| Successor Implementation Specification | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/implementation/implementation_P-PH000-ST002-AC004_successor-first-operationalization-task-specification.md` |
| Quarantined Concrete Skill | `prompt/skills/session-close/SKILL.md` |
| Historical Wrap-Up Skill | `prompt/skills/wrap-up/SKILL.md` |

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-27 | Amendment | Realigned decisive references to the QA assessment and SES007, while the older corrected review and SES006 remain lineage-only context. |
| v1.0.0 | 2026-03-26 | Initial | Created the AC004 successor session-close standards-input proposal so the corrected GATE-002 package can carry the dedicated reminder-surface convention without treating the premature concrete skill as active gate authority. |
