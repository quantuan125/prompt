---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-SES003'
version: '1.0.0'
date: '2026-03-30'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
execution_audience: 'assistant'
purpose: 'Assistant-executed pre-gate hardening brief for AC006: normalize TK001, correct the GATE-001 task stack, and reconcile stale SES002 history before consultant-owned TK002-TK006 authoring.'
---

# IMPLEMENTATION (Task Specification): AC006 GATE-001 Pre-Package Hardening Brief

## I. PURPOSE & AUTHORITY
- Purpose: Govern the exact pre-gate hardening edits needed before the main consultant continues AC006 through `TK006`.
- Authority chain: AC006 plan authorizes the activity -> This artifact specifies HOW the bounded pre-gate hardening pass is executed -> Later consultant-owned artifacts consume the corrected planning surfaces.
- Audience: `LLM_Assistant`
- Filename note: This is an assistant-scoped orchestration artifact using the `-brief` filename convention while retaining `implementation_type: 'task_specification'`.
- This artifact does NOT hold a GDR. Gate decisions remain in the later `gate_disposition` proposal.

## II. TASK SCOPE
- Governing plan task: Session-scoped orchestration support for `P-PH000-ST002-AC006` before consultant completion of `TK002` through `TK006`
- Trigger: The AC006 plan, TK001 audit artifact, and SES002 notes are partially out of sync with the live repo and with the required consultation-only gate stack.
- Deliverable contract: The AC006 plan is amended to include the future `TK006.1` and `TK006.2` sequence, `TK001` is normalized as an explicit completed artifact, post-gate execution ownership is corrected, and SES002 no longer claims that governed edits were never performed.

## III. SPECIFICATION ITEMS

### SPEC-001 - Normalize AC006 task register and gate-readiness stack

| Field | Detail |
|:--|:--|
| Requirement Source | Main-consultant orchestration plan through `TK006`; `guideline_workspace_plan.md` Section VI.L consultation-only gate sequence |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Required end-state posture | The task register contains `TK006.1` and `TK006.2` immediately after `TK006` and before `GATE-001`; `GATE-001` depends on `TK006.2`; `TK007` and `TK008` are no longer owned by `LLM_Consultant`; the gate model, dependency graph, detailed task sections, links register, and changelog all reflect the amended sequence. |
| Explicit non-target / do-not-change constraints | Do NOT create `TK006.1` or `TK006.2` artifacts in this pass. Do NOT author `TK002` through `TK006` deliverables. Do NOT change AC006 scope, AC004 dependency, or the briefing/session-close feature boundary. |
| Validation check | (1) Register order is `TK006`, `TK006.1`, `TK006.2`, `GATE-001`, `TK007`, `TK008`. (2) `TK007` and `TK008` owner cells are `LLM_Assistant`. (3) `GATE-001` entry criteria require `TK000` through `TK006.2`. (4) Plan changelog contains a new amendment entry dated `2026-03-30`. |
| Blocking ambiguity rule | If any planned row already exists for `TK006.1` or `TK006.2`, stop and escalate instead of merging two competing versions. |
| Status | `open` |

#### Implementation Detail

1. In the `### Task Register` table, change the `TK001` row from `planned` to `completed`.
2. Replace the `TK001` row `Action` text with: `Published the three-domain gap audit artifact covering session-close reachability, snotes guidance integration, briefing-surface gaps, authority mapping, and lower-intelligence assistant support requirements.`
3. Insert a new row immediately after `TK006`:

   `| TK006.1 | `P-PH000-ST002-AC006-TK006.1` | External review: GATE-001 package | `planned` | LLM_Subconsultant | TK006 | `analysis/` | `guideline_workspace_analysis.md` | Produce the authoritative independent external-review analysis of the GATE-001 package, including downstream task readiness, plan-guideline compliance, and implementation-spec commissionability. |`

4. Insert a new row immediately after `TK006.1`:

   `| TK006.2 | `P-PH000-ST002-AC006-TK006.2` | Consultant assessment: external review and downstream readiness | `planned` | LLM_Consultant | TK006.1 | `analysis/` | `guideline_workspace_analysis.md` | Produce the consultant's independent assessment of the external review, determine whether the package is ready for client disposition, and define the clean post-gate path toward later GATE-002 packaging. |`

5. Update the `GATE-001` row so its `Depends On` value becomes `TK006.2`.
6. Change the `TK007` owner cell from `LLM_Consultant` to `LLM_Assistant`.
7. Change the `TK008` owner cell from `LLM_Consultant` to `LLM_Assistant`.
8. Rewrite the `**Gate Model**` paragraph so it states that the consultation gate package must include `TK000`, `TK001`, `TK002`, `TK003`, `TK004`, `TK005`, `TK006`, `TK006.1`, and `TK006.2`, while execution tasks remain blocked until client approval.
9. Update the dependency graph text to place `TK006.1` and `TK006.2` between `TK006` and `GATE-001`.
10. In the detailed `TK001` section:
   - change the deliverable from the generic placeholder to `analysis/analysis_P-PH000-ST002-AC006_session-close-and-briefing-gap-audit.md`
   - mark every success-criteria checkbox as complete (`[x]`)
11. Add a new detailed section for `TK006.1` with:
   - deliverable path `analysis/analysis_P-PH000-ST002-AC006-GATE-001_external-review.md`
   - purpose aligned to independent package review
   - inputs required including the AC006 plan, `TK000` through `TK006` outputs, the future `TK004` and `TK005` implementation artifacts, and the proposal guideline / analysis guideline
   - success criteria stating the review covers evidence integrity, role-boundary compliance, downstream-task readiness, and implementation-spec commissionability
12. Add a new detailed section for `TK006.2` with:
   - deliverable path `analysis/analysis_P-PH000-ST002-AC006-GATE-001_external-review-and-downstream-readiness-assessment.md`
   - purpose aligned to consultant synthesis of the external review and downstream readiness
   - inputs required including `TK006.1`, the gate-disposition proposal path, the plan guideline, and the implementation guideline
   - success criteria stating explicit agreement/disagreement with the external review, explicit readiness assessment for downstream tasks, and an implementation-forward plan toward later `GATE-002` readiness
13. Update the `GATE-001` detail section so `Entry Criteria` reads:
   - `TK000 through TK006.2 complete`
   - `Both features are explicitly scoped`
   - `Both implementation specs are included`
   - `The authoritative external review and consultant assessment are included`
14. In the `TK007` and `TK008` detailed sections, do not rewrite scope, but ensure the role-correction is reflected in the register only.
15. In the `## IV. LINKS REGISTER` table, add rows for:
   - this new assistant brief
   - the future `TK006.1` external-review analysis path
   - the future `TK006.2` consultant-assessment analysis path
16. Append a new changelog row:

   `| v2.1.0 | 2026-03-30 | Amendment | Normalized TK001 as a completed artifact, inserted future pre-gate review tasks TK006.1 and TK006.2 before GATE-001, corrected post-gate execution ownership to assistant execution, and aligned the gate package boundary to the consultation-only gate-readiness stack. |`

### SPEC-002 - Normalize the TK001 audit artifact to completed consultant evidence

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 plan task contract for `TK001`; live artifact already exists on disk |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_session-close-and-briefing-gap-audit.md` |
| Required end-state posture | The artifact is explicitly a completed `TK001` deliverable with current metadata and no wording that suggests it is merely a draft placeholder. |
| Explicit non-target / do-not-change constraints | Do NOT alter the substantive findings, options, GAP register, or recommendations. Do NOT add new gaps. Do NOT change downstream targets. |
| Validation check | (1) Frontmatter `status` is `completed`. (2) Frontmatter `date` is `2026-03-30`. (3) Changelog contains an amendment row documenting normalization to the completed TK001 deliverable state. |
| Blocking ambiguity rule | If any substantive content appears inaccurate while normalizing metadata, stop and escalate instead of silently rewriting the analysis body. |
| Status | `open` |

#### Implementation Detail

1. Keep the filename unchanged.
2. In frontmatter:
   - change `version` from `1.0.0` to `1.1.0`
   - change `date` from `2026-03-28` to `2026-03-30`
   - change `status` from `draft` to `completed`
3. Leave `analysis_type: 'assessment'` unchanged.
4. Append a changelog row:

   `| v1.1.0 | 2026-03-30 | Amendment | Normalized the artifact as the completed TK001 three-domain gap audit after the AC006 plan and session-history surfaces were aligned to the live repository state. |`

### SPEC-003 - Correct SES002 session history so it matches the live repository

| Field | Detail |
|:--|:--|
| Requirement Source | Session history must not contradict the current governed state shown by the plan, notes register, and status surfaces |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/snotes/snotes_P-PH000-ST002-AC006-SES002.md` |
| Required end-state posture | SES002 acknowledges that the Phase A scope-amendment execution and TK001 audit normalization were carried out after the consultation, and no longer claims that no edits or registrations occurred. |
| Explicit non-target / do-not-change constraints | Do NOT change the DEC table decisions. Do NOT change the agenda or discussion topics. Do NOT add new session decisions. |
| Validation check | (1) Narrative Summary no longer says no plan amendments or notes registration were performed. (2) ACT table statuses reflect actual completion for the already-executed Phase A and TK001 items. (3) Session Handoff Pack no longer says `No concrete edits made`. (4) Changelog contains a `2026-03-30` amendment row. |
| Blocking ambiguity rule | If any claimed completed action is not actually reflected in the repo, stop and escalate instead of marking it completed in the notes. |
| Status | `open` |

#### Implementation Detail

1. In frontmatter:
   - change `version` from `1.0.0` to `1.1.0`
   - change `date` from `2026-03-28` to `2026-03-30`
2. In Section B (`Narrative Summary`):
   - keep the consultation decisions intact
   - replace the final paragraph beginning `The current session intentionally stopped...` with text stating that the consultation itself stopped at planning-level artifacts, but the governed Phase A alignment and TK001 audit publication were subsequently executed and are now reflected in the live repo surfaces
3. In Section E (`Actions / Carry-Forward (ACT Table)`):
   - change `ACT001` through `ACT005` statuses from `pending` to `completed`
   - change `ACT006` status from `pending` to `completed`
4. In Section G (`Session Handoff Pack`):
   - change `Phase A execution: Pending` to language stating that Phase A execution completed and the governed surfaces were aligned
   - change `Phase B execution: Pending — TK001 audit was produced...` to language stating that `TK001` is complete and `TK002` through `TK006.2` remain future work
   - delete the bullet `No concrete edits made...`
5. Append a changelog row:

   `| v1.1.0 | 2026-03-30 | Amendment | Reconciled SES002 history to the live repository after the Phase A alignment work and TK001 gap audit were executed, removing stale statements that those governed edits had not yet occurred. |`

## IV. IMPLEMENTATION SEQUENCE
1. Execute `SPEC-001` first so the AC006 plan becomes the authoritative corrected surface.
2. Execute `SPEC-002` next so the `TK001` artifact metadata matches the plan.
3. Execute `SPEC-003` last so SES002 reflects the already-corrected plan and audit surfaces.
4. After all three SPEC items, run a final read-through of the AC006 plan, the TK001 audit artifact, and SES002 to confirm they no longer contradict each other.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| TK001 Audit Artifact | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_session-close-and-briefing-gap-audit.md` |
| SES002 Notes | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/snotes/snotes_P-PH000-ST002-AC006-SES002.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-30 | Initial | Created the assistant-scoped pre-gate hardening brief for AC006 covering plan normalization, TK001 audit normalization, and SES002 history reconciliation before consultant-owned TK002-TK006 authoring. |
