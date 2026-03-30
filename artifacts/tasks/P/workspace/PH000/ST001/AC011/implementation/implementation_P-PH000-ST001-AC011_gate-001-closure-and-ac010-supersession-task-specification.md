---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC011'
task_id: 'P-PH000-ST001-AC011-TK010'
version: '1.0.0'
date: '2026-03-30'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/plan_P-PH000-ST001-AC011.md'
execution_audience: 'consultant'
purpose: 'Single execution contract for recording the client GATE-001 APPROVE decision, closing AC011, applying the AC010 supersession per the approved closeout matrix, and updating all planning surfaces to reflect the completed successor-baseline transition.'
---

# IMPLEMENTATION (Task Specification): AC011 GATE-001 Closure, AC010 Supersession, and Planning Surface Closeout

## I. PURPOSE & AUTHORITY

- Purpose: Provide one execution contract for all remaining AC011 closure work after the client has approved both GIR-001 (AC011 successor-baseline package) and GIR-002 (AC010 supersession path). This artifact governs `TK010` through `TK010` (single task, multiple SPEC items).
- Authority chain: AC011 plan authorizes the tracked work -> The AC011 GATE-001 proposal (v1.0.2) contains the approved GDR and closeout matrix -> This artifact specifies the exact file-level closure actions -> Execution evidence is recorded directly in the updated artifacts and plan changelogs.
- Audience: `LLM_Consultant` or `LLM_Assistant` executing on the consultant's behalf. This is a consultant-owned orchestration pass, not a developer implementation tranche.
- This artifact does NOT hold a GDR. The gate decision is recorded in the AC011 proposal at `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/proposal/proposal_P-PH000-ST001-AC011_gate-001_governance-amendment-and-remediation-disposition.md`.

## II. TASK SCOPE

- Governing plan task: `P-PH000-ST001-AC011-TK010` (to be registered in the AC011 plan as part of SPEC-001)
- Trigger: Client has approved both GIR-001 and GIR-002 at `P-PH000-ST001-AC011-GATE-001`. The gate package is procedurally and substantively complete. The remaining work is recording the decision, applying the approved AC010 supersession, and closing all planning surfaces.
- Deliverable contract:
  - Record the client APPROVE decision in the AC011 GDR
  - Close `GATE-001` in the AC011 activity plan
  - Apply the AC010 supersession per the approved closeout matrix in the AC011 proposal
  - Update the ST001 stream plan to reflect AC011 closure and AC010 supersession
  - Mark the AC011 activity as `completed`

## III. SPECIFICATION ITEMS

### SPEC-001 — Register TK010 in the AC011 Activity Plan

| Field | Detail |
|:--|:--|
| Requirement Source | This implementation specification requires a governing task entry before execution proceeds |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/plan_P-PH000-ST001-AC011.md` |
| Required end-state posture | The AC011 task register contains a new `TK010` row that is the governing task for this closure pass. `TK010` depends on `GATE-001` (which depends on `TK009`). `TK010` is owned by `LLM_Consultant`. |
| Explicit non-target / do-not-change constraints | Do not modify any existing TK000–TK009 or GATE-001 rows in this step. Do not change any task detail section content for existing tasks. GATE-001 status remains `in_progress` until SPEC-002 is executed. |
| Validation check | Confirm the task register contains a `TK010` row with status `planned` or `in_progress`, owner `LLM_Consultant`, depends on `GATE-001`, and a reference to this implementation specification. |
| Blocking ambiguity rule | If the plan's task register structure has changed since v1.3.0 in a way that makes adding a new row ambiguous, stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/plan_P-PH000-ST001-AC011.md`.
2. In the `### Task Register` table (currently lines 60–72), add a new row after the `GATE-001` row:

```
| TK010 | `P-PH000-ST001-AC011-TK010` | GATE-001 closure, AC010 supersession, and planning surface closeout | `in_progress` | LLM_Consultant | GATE-001 | Plan + proposal + AC010 surfaces + stream plan | `implementation_P-PH000-ST001-AC011_gate-001-closure-and-ac010-supersession-task-specification.md` | — |
```

3. Do NOT add a detailed `### Task TK010` section in `## III. TASKS (DETAILED)` at this step. The implementation specification (this artifact) is the execution contract; a plan-level detail section is not required when the IMPLEMENTATION artifact exists (CONV-011).
4. Do NOT bump the plan version yet — that happens in SPEC-007 after all closure work is complete.

---

### SPEC-002 — Record Client APPROVE Decision in the AC011 GDR

| Field | Detail |
|:--|:--|
| Requirement Source | Client has approved GIR-001 (option a) and GIR-002 (option a) at GATE-001 |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/proposal/proposal_P-PH000-ST001-AC011_gate-001_governance-amendment-and-remediation-disposition.md` |
| Required end-state posture | The GDR records `Client Decision: APPROVE`, `Gate Status After Decision: completed`, `Decision Date: 2026-03-30`, and a decision reference. Both GIR-001 and GIR-002 client decision checkboxes are marked as approved. The proposal status is updated to reflect the recorded decision. |
| Explicit non-target / do-not-change constraints | Do not modify the substantive content of Sections I through V (executive summary, gate package, disposition registers, consultant recommendation). Do not alter the external review incorporation language. Do not change the changelog entries for v1.0.0 through v1.0.2. |
| Validation check | Confirm the GDR table shows `APPROVE` as the client decision, `completed` as the gate status, today's date as the decision date, and a decision reference. Confirm both GIR checkboxes are marked `[x] (a)`. |
| Blocking ambiguity rule | If the GDR structure has changed since proposal v1.0.2, stop and escalate rather than guessing the new layout. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/proposal/proposal_P-PH000-ST001-AC011_gate-001_governance-amendment-and-remediation-disposition.md`.
2. In `## III. DISPOSITION SUMMARY REGISTER`, update the `Client Decision` column:
   - GIR-001 row: change `pending` to `APPROVE`
   - GIR-002 row: change `pending` to `APPROVE`
3. In `## IV. DETAILED DISPOSITION REGISTER`, under `### GIR-001`, update the client decision checkboxes:
   - Change `- [ ] (a)` to `- [x] (a)`
   - Leave all other options as `[ ]`
4. In `## IV. DETAILED DISPOSITION REGISTER`, under `### GIR-002`, update the client decision checkboxes:
   - Change `- [ ] (a)` to `- [x] (a)`
   - Leave all other options as `[ ]`
5. In `## VI. GATE DECISION RECORD (GDR)`, update the GDR table as follows:

| Field | Value |
|:--|:--|
| Gate ID | `P-PH000-ST001-AC011-GATE-001` |
| Consultant Recommendation | `APPROVE` |
| Client Decision | `APPROVE` |
| Gate Status After Decision | `completed` |
| Conditions (if any) | `—` |
| Decided By | `Client` |
| Decision Date | `2026-03-30` |
| Decision Reference | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/implementation/implementation_P-PH000-ST001-AC011_gate-001-closure-and-ac010-supersession-task-specification.md` |

6. Update the prose paragraph below the GDR table to:
   `The consultant recommendation is the consolidated advisory signal based on the completed AC011 package, the PASS verifier verdict, and the completed external review incorporated into this proposal. The client decision has been recorded as APPROVE on 2026-03-30.`
7. Update the frontmatter:
   - `status`: change from `'draft'` to `'completed'`
   - `version`: change from `'1.0.2'` to `'1.1.0'`
   - `date`: keep as `'2026-03-30'`
8. Add a new changelog row:

```
| v1.1.0 | 2026-03-30 | Closeout | Recorded the client APPROVE decision for GIR-001 and GIR-002 in the GDR, marked both disposition items as approved, and closed the gate on the approving path. Decision reference: AC011 GATE-001 closure implementation specification. |
```

---

### SPEC-003 — Apply Supersession to AC010 Plan

| Field | Detail |
|:--|:--|
| Requirement Source | Approved closeout matrix (proposal v1.0.2, Section IV, GIR-002), SPEC-006 of the original AC011 implementation specification |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md` |
| Required end-state posture | The AC010 plan's GATE-001 row and executive summary reflect that the activity has been superseded by the AC011 successor baseline. The plan preserves all historical content unchanged. A deprecation/supersession notice is added. The plan status is updated to `superseded`. |
| Explicit non-target / do-not-change constraints | Do not rewrite the historical task register action text. Do not remove any existing content from task detail sections. Do not change any existing changelog entries. Do not alter the AC010 plan's `author` field. |
| Validation check | Confirm the plan frontmatter shows `status: 'superseded'`, the GATE-001 row's action text references the successor gate, and a supersession notice is visible in the executive summary. |
| Blocking ambiguity rule | If the AC010 plan has been modified since v1.5.2 in ways that conflict with the supersession posture, stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md`.
2. Update the frontmatter:
   - `status`: change from `'draft'` to `'superseded'`
   - `version`: change from `'1.5.2'` to `'1.6.0'`
   - `date`: change to `'2026-03-30'`
3. In `## I. EXECUTIVE SUMMARY`, immediately after the existing `**Purpose**` paragraph, add a new supersession notice block:

```markdown
> **Supersession Notice**: This activity has been superseded by `P-PH000-ST001-AC011-GATE-001` (approved 2026-03-30). AC010 remains historically valid for its original baseline (`P-STD-001` v1.2.0 metadata-governance model). The successor baseline established by AC011 amends the changelog-governance rules and temporary verification operating model. All AC010 artifacts are preserved as historical evidence and are no longer the active authority for this scope.
```

4. In the task register, update the `GATE-001` row's `Action` column. Change the current text:
   - From: `Closed as APPROVE WITH CONDITIONS on 2026-03-28. The accepted condition is the TK006 verification-ownership exception; no further developer rework was required.`
   - To: `Closed as APPROVE WITH CONDITIONS on 2026-03-28. The accepted condition is the TK006 verification-ownership exception; no further developer rework was required. Superseded by P-PH000-ST001-AC011-GATE-001 (APPROVE, 2026-03-30).`
5. In `### GATE-001` detailed section (around line 297), after the existing `**Exit Criteria**` block, add:

```markdown
**Supersession**:
- Superseded by: `P-PH000-ST001-AC011-GATE-001`
- Successor decision: `APPROVE` (2026-03-30)
- Historical validity: AC010 GATE-001 remains valid for its original baseline; the successor gate establishes the amended baseline.
```

6. Add a new changelog row at the top of the existing changelog table:

```
| v1.6.0 | 2026-03-30 | Supersession | Applied the AC011 successor-baseline supersession per the approved closeout matrix at P-PH000-ST001-AC011-GATE-001. AC010 is now superseded; all artifacts are preserved as historical evidence under the original baseline. |
```

---

### SPEC-004 — Apply Supersession to AC010 Proposal/GDR

| Field | Detail |
|:--|:--|
| Requirement Source | Approved closeout matrix (proposal v1.0.2, Section IV, GIR-002), row 2: AC010 proposal |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md` |
| Required end-state posture | The AC010 GDR is amended to record `SUPERSEDE` as the successor-baseline outcome. The original `APPROVE WITH CONDITIONS` client decision and all historical content are preserved. A supersession notice links to the AC011 gate. |
| Explicit non-target / do-not-change constraints | Do not change the existing GIR-001 client decision checkbox (it remains `[x] (a)`). Do not remove any existing content from the disposition register, consultant recommendation, or evidence index. Do not alter existing changelog entries v1.0.0 through v1.0.2. |
| Validation check | Confirm the GDR table includes a `Successor Gate` field pointing to `P-PH000-ST001-AC011-GATE-001`, the `Gate Status After Decision` shows `superseded`, and the original client decision `APPROVE WITH CONDITIONS` is preserved alongside the supersession record. |
| Blocking ambiguity rule | If the AC010 proposal has been modified since v1.0.2 in ways that change the GDR structure, stop and escalate. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md`.
2. Update the frontmatter:
   - `status`: change from `'draft'` to `'superseded'`
   - `version`: change from `'1.0.2'` to `'1.1.0'`
   - `date`: change to `'2026-03-30'`
3. In `## I. EXECUTIVE SUMMARY`, immediately after the existing summary bullets, add:

```markdown
> **Supersession Notice**: This gate package has been superseded by `P-PH000-ST001-AC011-GATE-001` (approved 2026-03-30). The AC010 cross-standard retrofit was valid under the original `P-STD-001` v1.2.0 baseline. The AC011 successor baseline amends the changelog-governance model; this proposal is now preserved as historical evidence under the original baseline.
```

4. In `## VI. GATE DECISION RECORD (GDR)`, update the GDR table to add the supersession fields while preserving the original decision. Replace the entire GDR table with:

| Field | Value |
|:--|:--|
| Gate ID | `P-PH000-ST001-AC010-GATE-001` |
| Consultant Recommendation | `APPROVE WITH CONDITIONS` |
| Client Decision | `APPROVE WITH CONDITIONS` |
| Gate Status After Decision | `superseded` |
| Conditions (if any) | `Accepted verification-ownership exception: TK006 verification evidence is accepted for this gate even though the artifact was consultant-authored while the gate package framed TK006 as reviewer-owned; no further developer rework required.` |
| Decided By | `Client` |
| Decision Date | `2026-03-28` |
| Decision Reference | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/snotes/snotes_P-PH000-ST001-AC010-SES002.md` |
| Successor Gate | `P-PH000-ST001-AC011-GATE-001` |
| Supersession Date | `2026-03-30` |
| Supersession Basis | `AC011 successor-baseline approval supersedes the AC010 baseline for changelog governance and temporary verification operating model scope.` |

5. Update the prose paragraph below the GDR table to:
   `The original client decision of APPROVE WITH CONDITIONS was recorded on 2026-03-28. This gate has been subsequently superseded by P-PH000-ST001-AC011-GATE-001 (APPROVE, 2026-03-30), which establishes the successor baseline for changelog governance and the temporary verification operating model. The AC010 package remains historically valid for its original baseline.`
6. Add a new changelog row:

```
| v1.1.0 | 2026-03-30 | Supersession | Applied the AC011 successor-baseline supersession per the approved closeout matrix at P-PH000-ST001-AC011-GATE-001. Updated the GDR to record superseded status with successor-gate linkage while preserving the original APPROVE WITH CONDITIONS client decision and all historical content. |
```

---

### SPEC-005 — Apply Supersession to AC010 Verification Artifact

| Field | Detail |
|:--|:--|
| Requirement Source | Approved closeout matrix (proposal v1.0.2, Section IV, GIR-002), row 3: AC010 verification |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/verification/verification_P-PH000-ST001-AC010_gate-001.md` |
| Required end-state posture | The verification artifact is preserved as historical evidence with a deprecation notice linking to the AC011 successor gate. The verifier verdict and all findings/observations remain unchanged. |
| Explicit non-target / do-not-change constraints | Do not change the verifier verdict. Do not modify any existing checklist results, findings, or observations. Do not alter the verification scope or method text. Do not change existing changelog entries. |
| Validation check | Confirm the frontmatter shows `status: 'superseded'`, a supersession/deprecation notice is visible, and no existing verdict or finding content has been altered. |
| Blocking ambiguity rule | If the AC010 verification artifact has been modified since v1.0.0, stop and check whether the changes conflict with the supersession posture before proceeding. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/verification/verification_P-PH000-ST001-AC010_gate-001.md`.
2. Update the frontmatter:
   - `status`: change from `'completed'` to `'superseded'`
   - `version`: change from `'1.0.0'` to `'1.1.0'`
   - `date`: change to `'2026-03-30'`
3. Immediately after the `# VERIFICATION: P-PH000-ST001-AC010-GATE-001` heading (line 26), before `## I. Scope & Method`, add:

```markdown
> **Deprecation Notice**: This verification artifact has been superseded by the AC011 successor baseline established at `P-PH000-ST001-AC011-GATE-001` (approved 2026-03-30). The verifier verdict and all findings remain valid-for-baseline as historical evidence under the original `P-STD-001` v1.2.0 metadata-governance model. No re-verification is required.
```

4. Add a new changelog entry. If a `## Changelog` section exists, add a row. If no changelog section exists, add one at the end of the file:

```markdown
## Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-30 | Supersession | Deprecated under the AC011 successor baseline per the approved closeout matrix at P-PH000-ST001-AC011-GATE-001. Verifier verdict and all findings preserved as historical evidence. |
| v1.0.0 | 2026-03-28 | Initial | Verified the AC010 TK001-TK005 cross-standard metadata retrofit package against P-STD-001 metadata-governance clauses and issued a PASS verdict with no findings. |
```

---

### SPEC-006 — Apply Supersession to AC010 External Review

| Field | Detail |
|:--|:--|
| Requirement Source | Approved closeout matrix (proposal v1.0.2, Section IV, GIR-002), row 4: AC010 external review |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md` |
| Required end-state posture | The external review is preserved as historical evidence with a deprecation notice linking to the AC011 successor gate. No review content is rewritten. |
| Explicit non-target / do-not-change constraints | Do not change any findings, gap register entries, assessments, or recommendations. Do not alter the existing changelog entries. |
| Validation check | Confirm the frontmatter shows `status: 'superseded'`, a deprecation notice is visible, and no existing review content has been altered. |
| Blocking ambiguity rule | If the AC010 external review has been modified since v1.0.0, stop and check whether the changes conflict before proceeding. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md`.
2. Update the frontmatter:
   - `status`: change from `'draft'` to `'superseded'`
   - `version`: change from `'1.0.0'` to `'1.1.0'`
   - `date`: change to `'2026-03-30'`
3. Immediately after the top-level heading (`# ANALYSIS: AC010 GATE-001 Package External Review ...`), before `## I. EXECUTIVE SUMMARY`, add:

```markdown
> **Deprecation Notice**: This external review has been superseded by the AC011 successor baseline established at `P-PH000-ST001-AC011-GATE-001` (approved 2026-03-30). All findings and assessments remain valid-for-baseline as historical evidence under the original AC010 gate package. No re-review is required.
```

4. Add a new changelog row at the top of the existing changelog table (or create the section if it does not exist):

```
| v1.1.0 | 2026-03-30 | Supersession | Deprecated under the AC011 successor baseline per the approved closeout matrix at P-PH000-ST001-AC011-GATE-001. All review findings preserved as historical evidence. |
```

---

### SPEC-007 — Apply Supersession to AC010 Session Note (SES002)

| Field | Detail |
|:--|:--|
| Requirement Source | Approved closeout matrix (proposal v1.0.2, Section IV, GIR-002), row 5: AC010 SES002 |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/snotes/snotes_P-PH000-ST001-AC010-SES002.md` |
| Required end-state posture | The session note is retained as the durable decision-reference artifact with successor-gate linkage added. No historical content is rewritten. |
| Explicit non-target / do-not-change constraints | Do not change any existing session content, decisions, or action items. Do not alter the existing changelog entries. |
| Validation check | Confirm a successor-gate linkage notice is present and no existing content has been altered. |
| Blocking ambiguity rule | If the session note has been modified since v1.0.0, check that the changes do not conflict before proceeding. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/snotes/snotes_P-PH000-ST001-AC010-SES002.md`.
2. Update the frontmatter:
   - `version`: change from `'1.0.0'` to `'1.1.0'`
   - `date`: change to `'2026-03-30'`
3. At the end of the file, before any existing changelog section (or at the very end if none exists), add a successor-gate linkage section:

```markdown
## Successor-Gate Linkage

This session note remains the durable decision-reference artifact for the AC010 Gate-001 closeout. The AC010 baseline has been superseded by the AC011 successor baseline:

| Field | Value |
|:--|:--|
| Successor Gate | `P-PH000-ST001-AC011-GATE-001` |
| Successor Decision | `APPROVE` |
| Supersession Date | `2026-03-30` |
| Effect | AC010 is preserved as historically valid for its original baseline; the AC011 successor baseline is now the active authority for changelog governance and the temporary verification operating model. |
```

4. If a changelog section exists, add a row:

```
| v1.1.0 | 2026-03-30 | Supersession | Added successor-gate linkage after AC011 GATE-001 approval. AC010 is now superseded; this note remains the durable decision-reference artifact. |
```

If no changelog section exists, add one:

```markdown
## Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-30 | Supersession | Added successor-gate linkage after AC011 GATE-001 approval. AC010 is now superseded; this note remains the durable decision-reference artifact. |
| v1.0.0 | 2026-03-28 | Initial | Recorded the AC010 Gate-001 orchestration chain and durable decision reference. |
```

---

### SPEC-008 — Close GATE-001 and AC011 in the Activity Plan

| Field | Detail |
|:--|:--|
| Requirement Source | GATE-001 client decision recorded in SPEC-002; all closure work completed |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/plan_P-PH000-ST001-AC011.md` |
| Required end-state posture | GATE-001 row shows `completed`. TK010 row shows `completed` with action text summarizing the closure pass. The plan version is bumped to reflect the closure. The plan status remains `draft` (status transitions to `completed` only after the stream plan is updated in SPEC-009). |
| Explicit non-target / do-not-change constraints | Do not modify any existing TK000–TK009 task detail sections. Do not change existing success criteria checkmarks. Do not alter existing changelog entries v1.0.0 through v1.3.0. |
| Validation check | Confirm GATE-001 status is `completed`, TK010 status is `completed`, and a new changelog entry records the closure. |
| Blocking ambiguity rule | If any task between TK000 and TK009 has reverted from `completed` since v1.3.0, stop and investigate before proceeding with closure. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/plan_P-PH000-ST001-AC011.md`.
2. In the task register, update the `GATE-001` row:
   - Change `Status` from `in_progress` to `completed`
   - Update `Action` to: `Closed as APPROVE on 2026-03-30. Client approved both GIR-001 (successor-baseline package) and GIR-002 (AC010 supersession path). AC010 supersession applied per the approved closeout matrix.`
3. In the task register, update the `TK010` row (added in SPEC-001):
   - Change `Status` from `in_progress` to `completed`
   - Update `Action` to: `Recorded the client APPROVE decision in the GDR, applied the AC010 supersession per the approved closeout matrix, and updated all planning surfaces to close the AC011 successor-baseline activity.`
4. Update the frontmatter:
   - `version`: change from `'1.3.0'` to `'1.4.0'`
   - `date`: keep as `'2026-03-30'`
5. In `### GATE-001` detailed section, update the entry criteria checkmarks. The final entry criterion about the closeout matrix is now met. If there is a checkbox format, mark it. If not, note that all entry criteria are now satisfied.
6. Add a new changelog row:

```
| v1.4.0 | 2026-03-30 | Closeout | Closed GATE-001 as APPROVE after the client approved both GIR-001 and GIR-002. Registered and completed TK010 (gate closure, AC010 supersession, and planning surface closeout). All AC010 supersession updates applied per the approved closeout matrix. |
```

---

### SPEC-009 — Update the ST001 Stream Plan

| Field | Detail |
|:--|:--|
| Requirement Source | AC011 GATE-001 closure and AC010 supersession require stream-level record updates |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| Required end-state posture | The stream-plan activity register shows AC011 as `completed` and AC010 as `superseded`. The AC011 contract stub success criteria are updated. The AC010 contract stub reflects the supersession. The dependency notes are current. |
| Explicit non-target / do-not-change constraints | Do not modify any activity entries other than AC010 and AC011. Do not change any existing changelog entries. Do not alter the stream plan's scope, phase, or non-AC010/AC011 activity content. |
| Validation check | Confirm the activity register shows AC011 `completed` and AC010 `superseded`. Confirm the AC011 success criteria checkboxes are all marked. Confirm a new changelog entry records the closure. |
| Blocking ambiguity rule | If the stream plan has been modified since v0.1.27 in ways that change the AC010 or AC011 entries, stop and reconcile before applying updates. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md`.
2. In the `## II. ACTIVITY REGISTER` table (around line 45–48), update the two relevant rows:
   - **AC010 row**: Change `Status` from `completed` to `superseded`. Update the deliverable/summary column to append: `Superseded by P-PH000-ST001-AC011-GATE-001 (2026-03-30).`
   - **AC011 row**: Change `Status` from `in_progress` to `completed`. Update the deliverable/summary column to append: `GATE-001 closed as APPROVE on 2026-03-30; AC010 supersession applied.`
3. In the `#### Activity AC010` contract stub section (around line 310–341), add a supersession notice immediately after the section heading:

```markdown
> **Supersession Notice**: This activity has been superseded by `P-PH000-ST001-AC011-GATE-001` (approved 2026-03-30). AC010 remains historically valid for its original baseline. See AC011 for the active successor baseline.
```

4. In the `#### Activity AC011` contract stub section (around line 351–398), update the success criteria checkboxes. Mark all remaining unchecked items:
   - `[x] P-STD-001 and derivative governance surfaces align to the mandatory dedicated-changelog model` (was `[ ]`)
   - `[x] Workspace verification-governance surfaces align to the temporary operating model without reviewer-only contradictions` (was `[ ]`)
   - `[x] P-STD-002, P-STD-004, and P-STD-005 all use pointer-only Amendment History sections backed by dedicated changelog files` (was `[ ]`)
   - `[x] AC011 GATE-001 closes with a client decision on the successor baseline package` (was `[ ]`)
5. In `## IV. DEPENDENCY NOTES`, update the AC011 dependency note (around line 404). Change:
   - From: `**AC011** (Baseline amendment + operating-model correction) depends on AC010 completion. TK000 and TK001 are now complete, and the activity is the new contract-level unit that will carry the changelog baseline amendment, temporary verifier-model amendment, downstream standards remediation, and AC010 supersession handling.`
   - To: `**AC011** (Baseline amendment + operating-model correction) depends on AC010 completion. AC011 is now complete: GATE-001 closed as APPROVE on 2026-03-30, the successor baseline is active, and AC010 has been superseded per the approved closeout matrix.`
6. Update the frontmatter:
   - `version`: change from `'0.1.27'` to `'0.1.28'`
   - `date`: change to `'2026-03-30'`
7. Add a new changelog row at the top of the existing changelog table:

```
| v0.1.28 | 2026-03-30 | Closeout | Closed AC011 as completed after GATE-001 APPROVE decision on 2026-03-30. Marked AC010 as superseded per the approved closeout matrix. Updated both contract stubs, success criteria, and dependency notes to reflect the completed successor-baseline transition. |
```

---

### SPEC-010 — Final AC011 Plan Status Update

| Field | Detail |
|:--|:--|
| Requirement Source | All closure work is complete; the AC011 plan should reflect the final completed state |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/plan_P-PH000-ST001-AC011.md` |
| Required end-state posture | The AC011 plan frontmatter `status` is `'completed'`. This is the terminal state for the AC011 activity. |
| Explicit non-target / do-not-change constraints | Do not change any content beyond the frontmatter status field. The version was already bumped in SPEC-008. |
| Validation check | Confirm `status: 'completed'` in the frontmatter. |
| Blocking ambiguity rule | If SPEC-008 was not completed successfully, do not mark the plan as completed. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/plan_P-PH000-ST001-AC011.md`.
2. Update the frontmatter:
   - `status`: change from `'draft'` to `'completed'`
3. No additional content changes. The plan version and changelog were already updated in SPEC-008.

## IV. IMPLEMENTATION SEQUENCE

Execute the SPEC items in this exact order:

1. **SPEC-001**: Register TK010 in the AC011 plan (establishes the governing task entry).
2. **SPEC-002**: Record the client APPROVE decision in the AC011 GDR (the gate decision must be recorded before any supersession action is taken).
3. **SPEC-003**: Apply supersession to the AC010 plan.
4. **SPEC-004**: Apply supersession to the AC010 proposal/GDR.
5. **SPEC-005**: Apply supersession to the AC010 verification artifact.
6. **SPEC-006**: Apply supersession to the AC010 external review.
7. **SPEC-007**: Apply supersession to the AC010 session note (SES002).
8. **SPEC-008**: Close GATE-001 and TK010 in the AC011 activity plan.
9. **SPEC-009**: Update the ST001 stream plan to reflect AC011 closure and AC010 supersession.
10. **SPEC-010**: Final AC011 plan status update to `completed`.

**Sequencing rationale**: The GDR must be recorded (SPEC-002) before any AC010 supersession work begins (SPEC-003 through SPEC-007), because the supersession updates are conditional on the recorded approval. The AC011 plan closure (SPEC-008) happens after all AC010 supersession is complete so the TK010 action text can accurately summarize the full pass. The stream plan (SPEC-009) is updated last because it depends on both the AC011 closure and AC010 supersession being recorded. SPEC-010 is the terminal step.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/plan_P-PH000-ST001-AC011.md` |
| Parent Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md` |
| AC011 Gate Proposal (with closeout matrix) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/proposal/proposal_P-PH000-ST001-AC011_gate-001_governance-amendment-and-remediation-disposition.md` |
| AC011 Original Implementation Specification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/implementation/implementation_P-PH000-ST001-AC011_governance-amendment-and-remediation-task-specification.md` |
| AC011 External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/analysis/analysis_P-PH000-ST001-AC011_external-review_gate-001-package.md` |
| AC011 Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC011/verification/verification_P-PH000-ST001-AC011_gate-001.md` |
| AC010 Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md` |
| AC010 Proposal | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md` |
| AC010 Verification | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/verification/verification_P-PH000-ST001-AC010_gate-001.md` |
| AC010 External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010_external-review-gate-001-package.md` |
| AC010 Session Note | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/snotes/snotes_P-PH000-ST001-AC010-SES002.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-30 | Initial | Authored the AC011 GATE-001 closure and AC010 supersession implementation specification covering ten SPEC items: TK010 registration, GDR recording, five AC010 supersession surfaces, AC011 plan closure, stream plan update, and final status transition. |
