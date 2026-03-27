---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC004'
task_id: 'P-PH000-ST002-AC004-TK003.16'
version: '1.0.0'
date: '2026-03-27'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'
execution_audience: 'consultant'
purpose: 'Deterministic consultant-execution specification for AC004 post-approval GATE-002 housekeeping, decisive-authority reconciliation, SES008 creation, and downstream TK004 loop commissioning without touching any TK004 implementation target.'
---

# IMPLEMENTATION (Task Specification): AC004 GATE-002 Closeout And Downstream Loop Commissioning

## I. PURPOSE & AUTHORITY

- Purpose: Specify the exact consultant-owned housekeeping execution required immediately after the Client approves `P-PH000-ST002-AC004-GATE-002`, before any `TK004` implementation work begins.
- Authority chain: The approved `GATE-002` decision in the live proposal authorizes gate closure -> the AC004 activity plan governs task ordering and downstream blocking -> this artifact specifies HOW the consultant-commissioned assistant executes the housekeeping boundary -> the later `TK004` implementation artifact remains the sole authority for downstream operationalization work.
- Audience: `LLM_Consultant` as the governing execution owner and designated consultant-commissioned assistant as the mutation executor for this bounded housekeeping slice.
- Boundary: This artifact does NOT hold a GDR. The authoritative gate decision remains in `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md`.
- Execution under this artifact is consultant-owned non-implementation work. It MUST close the gate and reconcile the decisive documentation surfaces, but it MUST NOT mutate any `TK004` target surface.

## II. TASK SCOPE

- Governing plan task: `P-PH000-ST002-AC004-TK003.16`
- Trigger: The client has confirmed the downstream operating model for this session:
  - `GATE-002` is to be recorded as `APPROVE WITH CONDITIONS`
  - `TK006` verification for the downstream implementation gate will be consultant-authored
  - a new `SES008` must be created instead of amending `SES007`
  - the QA assessment remains the authoritative Gate-002 external-review surface
- Deliverable contract:
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md`
  - New `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md`
  - Updated `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md`

**Explicit non-target surfaces**
- Do NOT edit `prompt/artifacts/tasks/P/status/status_program.yaml`
- Do NOT edit `prompt/artifacts/tasks/P/status/status_program.md`
- Do NOT edit `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md`
- Do NOT edit `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md`
- Do NOT edit `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md`
- Do NOT edit `prompt/skills/session-close/SKILL.md`
- Do NOT edit `prompt/skills/wrap-up/SKILL.md`
- Do NOT edit root `AGENTS.md`
- Do NOT edit `prompt/AGENTS.md`
- Do NOT create any DEV-REPORT, VERIFICATION, `GATE-003` proposal, AC005 child artifact, `T105` artifact, automation hook, script, or repo-wide enforcement artifact

## II.A FIXED EXECUTION TOKENS

- `GATE-002` decision date for this execution is `2026-03-27`.
- Every file mutated under this artifact MUST use `2026-03-27` as its `date` field or session date value where applicable.
- Where this artifact says "increment patch version", increase only the patch component of the live semantic version already present in the target file.
- `SES008` path is fixed and MUST be:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md`

## II.B PREFLIGHT RULE

- Before editing any file, read every in-scope target named in this specification.
- Current repo state wins over stale assumptions, but only within the approved GATE-002 closure boundary defined here.
- If a target already satisfies the required end state, leave it unchanged and record it as verified in handoff notes.
- If a target partially satisfies the required end state, merge only the missing required deltas.
- If any live file would require touching a `TK004` target surface to complete this housekeeping boundary, stop and escalate instead of expanding scope.

## III. SPECIFICATION ITEMS

### SPEC-001 - Close the live GATE-002 proposal and preserve authoritative review placement

| Field | Detail |
|:--|:--|
| Requirement Source | Approved session decision; `guideline_workspace_proposal.md` §V.B and §VII; AC004 QA assessment |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md` |
| Required end-state posture | The proposal records `APPROVE WITH CONDITIONS`, remains anchored to the QA assessment as the authoritative external review, preserves the existing five conditions unchanged, and clearly marks downstream tasks as unblocked after the recorded decision |
| Explicit non-target / do-not-change constraints | Do not broaden V1 scope, do not replace the QA assessment with the older corrected review, do not add any new condition beyond the existing five live conditions |
| Validation check | Confirm the QA assessment appears in frontmatter `external_review_reference`, Gate Package Index, Evidence Index, and References; confirm the GDR is fully populated and internally consistent |
| Blocking ambiguity rule | If the live proposal contains conflicting decision authority that cannot be reconciled without changing the approved conditions, stop and escalate rather than rewriting the decision boundary |
| Status | `open` |

#### Implementation Detail

1. In frontmatter:
   - increment the patch version
   - set `date: '2026-03-27'`
   - keep `status: 'draft'`
   - keep `external_review_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-002-package-qa-assessment.md'`
2. In `## II. GATE PACKAGE`:
   - ensure the QA assessment remains present in the Gate Package Index row:
     - Deliverable: `AC004 GATE-002 Package QA Assessment`
     - Producing Task: `TK003.12`
     - Status: `completed`
     - Acceptance: `accepted`
     - Client Priority: `Required`
     - Path: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-002-package-qa-assessment.md`
   - ensure the QA assessment remains present in the Evidence Index as the authoritative external-review surface
   - keep the older corrected external review only in the historical evidence table with lineage-only wording
3. In `## V. CONSULTANT GATE RECOMMENDATION`:
   - keep `Consultant recommendation: APPROVE WITH CONDITIONS`
   - keep the condition bullets aligned to the current live five-condition set
   - replace the downstream enforcement line so it states that `TK004` and downstream tasks are now allowed to begin because the GDR below records an approving decision, while the live conditions remain binding during execution
4. In `## VI. GATE DECISION RECORD (GDR)` update the table to exactly:

| Field | Value |
|:--|:--|
| Gate ID | `P-PH000-ST002-AC004-GATE-002` |
| Consultant Recommendation | `APPROVE WITH CONDITIONS` |
| Client Decision | `APPROVE WITH CONDITIONS` |
| Gate Status After Decision | `completed` |
| Conditions (if any) | Treat the QA assessment as the authoritative external-review surface for GATE-002; keep the older corrected review as historical/supporting evidence only.<br>AC004 V1 is manual-only and excludes hooks, scripts, and repo-wide automation.<br>`prompt/skills/session-close/SKILL.md` applies only to consultant-led consultation-session closeout.<br>`status_program.md` Section 7 remains broader and role-based.<br>`prompt/skills/session-close/SKILL.md` remains non-authoritative until TK004 operationalizes the approved convention. |
| Decided By | `Client` |
| Decision Date | `2026-03-27` |
| Decision Reference | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md` |

5. Replace the prose below the GDR table so it no longer describes the gate as pending. It MUST say:
   - the consultant recommendation was populated at authoring time
   - this is a consultation-only gate
   - the client decision has now been recorded
   - downstream work may begin subject to the recorded conditions
6. In `## VII. REFERENCES`, ensure the QA assessment remains listed as `External Review`.
7. In `## VIII. CHANGELOG`, add a new top-row entry summarizing that:
   - Client Decision `APPROVE WITH CONDITIONS` was recorded on `2026-03-27`
   - the GDR now marks `GATE-002` `completed`
   - the QA assessment remains the authoritative external-review surface

### SPEC-002 - Reconcile decisive-reference drift in the standards-input proposal

| Field | Detail |
|:--|:--|
| Requirement Source | Independent assessment residual GAP-001/GAP-002; approved session direction that decisive references must match the live authoritative package |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md` |
| Required end-state posture | The standards-input proposal still preserves lineage context, but its decisive review/session references point to the current authoritative package surfaces rather than the older corrected review / SES006 pair |
| Explicit non-target / do-not-change constraints | Do not change the underlying convention set, decision requests, or standards-input scope; do not remove historical mentions where they are explicitly labeled as lineage |
| Validation check | Confirm frontmatter, impact/risk rationale, and references distinguish decisive authority from historical lineage consistently |
| Blocking ambiguity rule | If changing a reference would alter the meaning of a convention rather than its authority posture, stop and escalate |
| Status | `open` |

#### Implementation Detail

1. In frontmatter:
   - increment the patch version from the live version
   - set `date: '2026-03-27'`
   - keep `status: 'draft'`
   - change `external_review_reference` to:
     - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-002-package-qa-assessment.md`
2. In `## III. PROPOSED CONVENTIONS`, `CONV-001` authority link text should reference the QA assessment and corrected live GATE-002 proposal, not the older corrected external review.
3. In `CONV-002`, keep lineage language, but change the rationale source from `SES006 corrective session; corrected GATE-002 proposal` to `SES007 corrective session; live GATE-002 proposal`.
4. In `## V. IMPACT AND RISKS`, keep `RISK-001` through `RISK-003` unchanged in meaning, but if any mitigation text references the corrected older review as decisive authority, change it to the QA assessment plus live proposal pair.
5. In `## VI. REFERENCES`, replace:
   - `Corrected External Review` path with the QA assessment path and label it `Authoritative External Review`
   - `Corrective Session Notes` path from `SES006` to `SES007` and label it `Current Corrective Session Notes`
6. If desired for lineage clarity, add two additional historical-reference rows after the decisive rows:
   - `Historical Corrected External Review` -> older corrected review path
   - `Historical Corrective Session Notes` -> `SES006`
7. In `## VII. CHANGELOG`, add a top-row entry stating that decisive references were realigned to the QA assessment and `SES007`, while the older corrected review and `SES006` remain lineage-only context.

### SPEC-003 - Update the AC004 activity plan to reflect gate completion and downstream ownership model

| Field | Detail |
|:--|:--|
| Requirement Source | Approved session orchestration choices; `guideline_workspace_plan.md` gate status rules; AC004 downstream sequencing |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| Required end-state posture | `GATE-002` is marked `completed`; `TK003.16` is marked completed after this housekeeping slice; `TK004` remains pending behind the completed gate and completed housekeeping task; downstream verification ownership reflects the chosen consultant-verifies model |
| Explicit non-target / do-not-change constraints | Do not advance `TK004`, `TK005`, `TK006`, `TK007`, or `GATE-003` to completed; do not rewrite stream/phase/roadmap surfaces in this step |
| Validation check | Confirm task-register order remains valid, downstream dependencies are intact, and the new text does not imply that TK004 already mutated its target files |
| Blocking ambiguity rule | If the live plan shape would require reordering the gate/task model beyond this bounded post-approval amendment, stop and escalate |
| Status | `open` |

#### Implementation Detail

1. In frontmatter:
   - increment the patch version from the live version
   - set `date: '2026-03-27'`
2. In the Task Register:
   - update the `GATE-002` row `Status` from `in_progress` to `completed`
   - replace the `Action` text with a concise statement that:
     - the Client recorded `APPROVE WITH CONDITIONS` on `2026-03-27`
     - the QA assessment remains the authoritative external-review surface
     - the live V1 conditions remain binding downstream
   - update the `TK003.16` row `Status` from `planned` to `completed`
   - replace the `TK003.16` `Action` text with a concise statement that:
     - the consultant-owned post-approval housekeeping specification was executed
     - decisive references were reconciled
     - `SES008` was recorded
     - downstream TK004 commissioning is now unblocked
   - update the `TK006` row owner from `LLM_Reviewer` to `LLM_Consultant`
   - keep `TK006` status `planned`
3. In the `### GATE-002` detailed section:
   - keep the existing entry/exit criteria, but add one short line after the gate-disposition proposal reference stating that the gate is now closed as `APPROVE WITH CONDITIONS` on `2026-03-27` and the downstream conditions remain in force during `TK004`
4. In the `### Task TK003.16` detailed section:
   - add one final sentence to the Purpose or Success Criteria area stating that this task is now complete and served as the final pre-TK004 housekeeping boundary
5. In the `### Task TK004` detailed section:
   - add one sentence near the Purpose or Steps stating that execution is commissioned through a consultant-supervised `gpt-5.4-mini` `xhigh` developer assistant against the successor TK004 implementation specification
6. In the `### Task TK005` detailed section:
   - add one sentence stating that the developer assistant who performs `TK004` also authors the bounded `TK005` DEV-REPORT handoff for consultant verification
7. In the `### Task TK006` detailed section:
   - replace the purpose text `Independently verify` with wording that still preserves evidence-first verification, but explicitly states the artifact is consultant-authored in this activity
   - keep the deliverable path unchanged:
     - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/verification/verification_P-PH000-ST002-AC004_gate-003.md`
8. In the Links Register, ensure this implementation artifact path remains listed.
9. In the Changelog, add a new top-row entry summarizing:
   - `GATE-002` recorded `APPROVE WITH CONDITIONS`
   - `TK003.16` completed the post-approval housekeeping boundary
   - `TK006` verification ownership is consultant-authored for this activity

### SPEC-004 - Create SES008 as the new post-approval corrective session record

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` §5.3 corrective-session rule; explicit session decision to create `SES008` instead of amending `SES007` |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md` |
| Required end-state posture | A new activity-scoped session note captures the gate approval recording, consultant-owned housekeeping execution, and downstream-loop commissioning without rewriting SES007 |
| Explicit non-target / do-not-change constraints | Do not edit `SES007`; do not imply that TK004 has already updated any of its six target files |
| Validation check | Confirm the session note is standalone, uses SES008 IDs consistently, and preserves the distinction between completed housekeeping and pending downstream execution |
| Blocking ambiguity rule | If any requested note content would rewrite the historical meaning of SES007 instead of creating a new corrective trail, stop and escalate |
| Status | `open` |

#### Implementation Detail

1. Create `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md` with frontmatter:
   - `artifact_type: 'NOTES'`
   - `notes_type: 'SESSION_ACTIVITY'`
   - `initiative_id: 'P'`
   - `initiative_code: 'PROGRAM'`
   - `phase: '0'`
   - `stream: 'ST002'`
   - `activity_id: 'P-PH000-ST002-AC004'`
   - `session: 'SES008'`
   - `session_id: 'P-PH000-ST002-AC004-SES008'`
   - `version: '1.0.0'`
   - `date: '2026-03-27'`
   - `status: 'draft'`
   - `author: 'LLM_Consultant'`
   - `decision_owner_role: 'Client'`
   - `register_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md'`
   - `plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md'`
   - `raw_transcript_reference: '—'`
2. Use this exact title:
   - `# ACTIVITY SESSION NOTES: P (PROGRAM) — PH000 / ST002 / AC004 / SES008 (GATE-002 Approval Recording, Consultant-Owned Housekeeping & Downstream Loop Commissioning)`
3. `## A. Agenda / Topics` MUST contain exactly:
   1. Record the Client `APPROVE WITH CONDITIONS` decision for the corrected `GATE-002` package.
   2. Execute the consultant-owned post-approval housekeeping boundary without touching `TK004` implementation targets.
   3. Realign decisive authority references so the QA assessment and live proposal remain the authoritative Gate-002 pair.
   4. Preserve `SES007` as the historical QA-remediation completion session and capture this session separately as `SES008`.
   5. Commission the downstream `TK004 -> TK005 -> TK006 -> TK007 -> GATE-003` loop with consultant-authored verification.
4. `## B. Narrative Summary (Minutes-Style)` MUST state, in prose:
   - the client confirmed `Consultant verifies`
   - the client confirmed `New SES008`
   - this session recorded `GATE-002` as `APPROVE WITH CONDITIONS`
   - the QA assessment remains the authoritative external-review surface
   - the housekeeping assistant was limited to proposal / plan / session-note / notes-register surfaces
   - `TK004` target files remained untouched in this session
   - downstream execution will be delegated to a fresh developer assistant against the existing successor TK004 implementation spec
5. `## C. Discussion Points (DP Table)` MUST include these five rows:

| ID | Topic | Outcome | Rationale | Evidence |
|:---|:------|:--------|:----------|:---------|
| `P-PH000-ST002-AC004-SES008-DP001` | Gate decision posture | `GATE-002` is recorded as `APPROVE WITH CONDITIONS` | The corrected package is decision-ready, but the live V1 conditions remain binding during execution | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md`; `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-002-package-qa-assessment.md` |
| `P-PH000-ST002-AC004-SES008-DP002` | Authoritative external review | The QA assessment remains the single authoritative Gate-002 external-review surface | The proposal package already elevates the QA assessment and demotes the older corrected review to historical support | same as above |
| `P-PH000-ST002-AC004-SES008-DP003` | Session-note handling | A new `SES008` is used instead of amending `SES007` | Notes are session-scoped and later corrective work should create a new session record rather than rewrite the prior one | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| `P-PH000-ST002-AC004-SES008-DP004` | Housekeeping boundary | Post-approval housekeeping is limited to gate-close authority surfaces and must not touch any TK004 implementation target | Gate-close completion and TK004 operationalization are separate execution boundaries | This implementation specification; `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/implementation/implementation_P-PH000-ST002-AC004_successor-first-operationalization-task-specification.md` |
| `P-PH000-ST002-AC004-SES008-DP005` | Downstream verification ownership | `TK006` will be consultant-authored after the developer assistant completes TK004/TK005 | The client explicitly selected consultant verification for the downstream gate | Current client instruction in this session |

6. `## D. Decisions Captured (DEC Table)` MUST include these four rows:

| ID | Decision | Type | Status | Owner | Date | Rationale | Acceptance Signal | Evidence |
|:---|:---------|:-----|:-------|:------|:-----|:----------|:------------------|:---------|
| `P-PH000-ST002-AC004-SES008-DEC001` | Record `GATE-002` as `APPROVE WITH CONDITIONS` with the live five-condition set unchanged | Governance | Confirmed | Client | 2026-03-27 | The package is approval-safe only under the existing bounded V1 conditions | GDR recorded in the live Gate-002 proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md` |
| `P-PH000-ST002-AC004-SES008-DEC002` | Keep the QA assessment as the single authoritative Gate-002 external-review surface | Governance | Confirmed | Client | 2026-03-27 | The package must present one decisive client-facing external review | `external_review_reference` and evidence stack point to the QA assessment | same as above |
| `P-PH000-ST002-AC004-SES008-DEC003` | Use `SES008` rather than amending `SES007` for this post-approval corrective trail | Documentation | Confirmed | Client | 2026-03-27 | Session notes remain historically intact and forward-only | This session note exists and `SES007` remains unchanged | `prompt/templates/consultant/workspace/guideline_workspace_notes.md`; `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES007.md` |
| `P-PH000-ST002-AC004-SES008-DEC004` | Commission the downstream `TK004/TK005` developer loop under consultant supervision and keep `TK006` consultant-authored | Governance | Confirmed | Client | 2026-03-27 | The downstream execution model for this activity has been explicitly chosen in-session | AC004 plan and downstream implementation spec reflect the commissioned role split | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md`; `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/implementation/implementation_P-PH000-ST002-AC004_successor-first-operationalization-task-specification.md` |

7. `## E. Actions / Carry-Forward (ACT Table)` MUST include these four rows:

| ID | Action | Owner | Status |
|:---|:-------|:------|:-------|
| `P-PH000-ST002-AC004-SES008-ACT001` | Record the approving GDR and decisive authority posture in the live Gate-002 proposal | LLM_Consultant | `completed` |
| `P-PH000-ST002-AC004-SES008-ACT002` | Reconcile the standards-input proposal and activity plan to the approved post-gate state | LLM_Consultant | `completed` |
| `P-PH000-ST002-AC004-SES008-ACT003` | Register `SES008` in the ST002 notes register | LLM_Consultant | `completed` |
| `P-PH000-ST002-AC004-SES008-ACT004` | Start the bounded `TK004/TK005` developer loop after housekeeping completes | LLM_Consultant | `pending` |

8. `## F. Open Questions Register (OQ Table)` MUST remain empty using the standard em-dash row.
9. `## G. Session Handoff Pack` MUST include bullets stating:
   - `GATE-002` is now closed as `APPROVE WITH CONDITIONS`
   - the QA assessment is the authoritative external-review surface
   - the standards-input proposal has been realigned to the live decisive package
   - `SES007` remains historical and `SES008` is the new post-approval corrective trail
   - no `TK004` target file was touched in this session
   - the next step is to commission the developer assistant for `TK004` and `TK005`
10. `## H. Changelog` MUST contain one row:
   - `v1.0.0 | 2026-03-27 | Initial | Recorded the GATE-002 approving decision, consultant-owned post-approval housekeeping, decisive-authority reconciliation, and downstream loop commissioning as a new activity session without amending SES007.`

### SPEC-005 - Register SES008 in the ST002 notes register

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` §5.1 JIT registration rule |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` |
| Required end-state posture | The stream notes register indexes SES008 and records the new session in the changelog without embedding any session body content |
| Explicit non-target / do-not-change constraints | Do not alter prior session rows beyond adding the new SES008 entry; do not embed session-note body text in the register |
| Validation check | Confirm the new row points to the new SES008 file and the register remains index-only |
| Blocking ambiguity rule | If the register layout has materially changed from the current table schema, stop and escalate instead of improvising a new schema |
| Status | `open` |

#### Implementation Detail

1. In frontmatter:
   - increment the patch version from the live version
   - set `date: '2026-03-27'`
2. In `## III. ACTIVITY NOTES REGISTER`, insert a new AC004 row immediately after the existing `SES007` row:

| Activity | Session ID | Name | Notes File |
|:--|:--|:--|:--|
| AC004 | `P-PH000-ST002-AC004-SES008` | GATE-002 Approval Recording, Consultant-Owned Housekeeping & Downstream Loop Commissioning | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md` |

3. In `## V. CHANGELOG`, add a new top-row entry:
   - `v<next-patch> | 2026-03-27 | Amendment | Registered AC004 activity session P-PH000-ST002-AC004-SES008 for GATE-002 approval recording, consultant-owned post-approval housekeeping, decisive-authority reconciliation, and downstream loop commissioning.`

### SPEC-006 - Preserve the TK004 boundary and hand off cleanly to the downstream developer loop

| Field | Detail |
|:--|:--|
| Requirement Source | User-approved orchestration model; existing successor TK004 implementation artifact |
| Target file(s) | All files in scope of this housekeeping task |
| Required end-state posture | Housekeeping completes without mutating any of the six TK004 target files, and the consultant can immediately hand off the existing TK004 implementation spec to a downstream developer assistant |
| Explicit non-target / do-not-change constraints | Do not touch any TK004 target file named in the successor first-operationalization task specification |
| Validation check | Confirm the final changed-file set contains only the five housekeeping files named in this artifact |
| Blocking ambiguity rule | If any proposed edit would spill into a TK004 target file, stop and escalate instead of partially performing the housekeeping boundary |
| Status | `open` |

#### Implementation Detail

1. After all edits are complete, the changed-file set produced by this housekeeping slice MUST be limited to:
   - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md`
   - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md`
   - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md`
   - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md`
   - `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md`
2. Do not create the downstream developer prompt or mutate the downstream files in this step. The only allowed downstream handoff is that the main consultant may use this completed housekeeping result to commission the already-authored TK004 implementation specification in the next execution phase.

## IV. IMPLEMENTATION SEQUENCE

1. Read all five in-scope target files.
2. Close the live GATE-002 proposal and record the approving GDR.
3. Reconcile the standards-input proposal to the decisive review/session surfaces.
4. Update the AC004 activity plan for gate completion and downstream ownership.
5. Create `SES008`.
6. Register `SES008` in the ST002 notes register.
7. Validate that only the five allowed housekeeping files changed.
8. Hand back to the main consultant for downstream developer-loop commissioning.

## V. VALIDATION COMMANDS

Run the following checks from the repo root after edits are complete:

```bash
git -C prompt diff --check -- \
  artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md \
  artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md \
  artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md \
  artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md \
  artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md
```

Expected result:
- no whitespace or patch-format errors

```bash
rg -n "external_review_reference|Client Decision|Gate Status After Decision|Decision Reference|SES008" \
  prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md \
  prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md \
  prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md \
  prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md \
  prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md
```

Expected result:
- QA assessment remains the decisive review path
- `GATE-002` GDR shows `APPROVE WITH CONDITIONS` and `completed`
- `SES008` is referenced consistently across proposal, plan, session note, and notes register

```bash
git -C prompt diff --name-only -- \
  artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md \
  artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md \
  artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md \
  artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES008.md \
  artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md
```

Expected result:
- only the five housekeeping files named in this artifact appear in the changed-file subset

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/plan_P-PH000-ST002-AC004.md` |
| Live Gate-002 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-GATE-002_operating-model-disposition.md` |
| Authoritative External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/analysis/analysis_P-PH000-ST002-AC004_external-review_gate-002-package-qa-assessment.md` |
| Standards-Input Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md` |
| Current Corrective Session | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/snotes/snotes_P-PH000-ST002-AC004-SES007.md` |
| Stream Notes Register | `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` |
| Successor TK004 Implementation Specification | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/implementation/implementation_P-PH000-ST002-AC004_successor-first-operationalization-task-specification.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-27 | Initial | Created the consultant-owned post-approval housekeeping task specification for AC004 GATE-002 closure, decisive-authority reconciliation, SES008 creation, and clean handoff to the downstream TK004 execution loop without touching any TK004 target surface. |
