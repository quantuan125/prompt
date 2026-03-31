---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-TK006.3'
version: '1.0.0'
date: '2026-03-31'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
execution_audience: 'assistant'
purpose: 'Consolidated post-review normalization pass: record the client GATE-001 decision in the GDR, normalize the activity plan to full guideline_workspace_plan.md compliance, and formalize the GATE-002 execution-evidence path — all in a single assistant-executed pass.'
---

# IMPLEMENTATION (Task Specification): AC006 GATE-001 Normalization And GDR Recording

## I. PURPOSE & AUTHORITY

- Purpose: Specify the exact assistant-executed work required to (a) record the client's GATE-001 approval in the GDR, (b) normalize the AC006 activity plan to full `guideline_workspace_plan.md` compliance, and (c) formalize the GATE-002 execution-evidence path in the same plan amendment.
- Authority chain: The AC006 plan defines the task boundary (`TK006.3`) -> the client's verbal GATE-001 approval (recorded during the SES005 consultation session) authorizes the GDR recording -> the independent consultant assessment identified the plan compliance gaps (Findings F-001 through F-004) -> this artifact specifies HOW the assistant executes the consolidated normalization.
- Audience: `LLM_Assistant`
- Filename note: This artifact uses the `-brief` filename convention per CONV-022 (consultant/assistant-scoped orchestration artifact).
- This artifact does NOT hold a GDR. The authoritative GDR for GATE-001 is hosted in `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md`. This artifact specifies the mechanical steps to update that GDR.
- The live activity plan (`prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md`) remains the downstream operationalization target for plan normalization. The approved behavior boundary comes from `guideline_workspace_plan.md` and `workspace_documentation_rules.md`, not from the current live file contents alone.

## II. TASK SCOPE

- Governing plan task: `P-PH000-ST002-AC006-TK006.3` (to be registered by this execution)
- Trigger: The independent consultant assessment (SES005) identified plan compliance gaps (F-001: Task Register schema deviation, F-002: non-standard sections, F-003: missing Reviewer field) and the client approved the GATE-001 package with the condition that normalization and GATE-002 path formalization occur in a single pass.
- Deliverable contract:
  - Updated GDR in `proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md`
  - Normalized `plan_P-PH000-ST002-AC006.md` (compliant Task Register, removed non-standard sections, added Reviewer field, registered TK006.3, formalized GATE-002)
  - Plan version bumped to `v2.3.0` with changelog entry

## III. SPECIFICATION ITEMS

### SPEC-001 — Record Client GATE-001 Decision In The GDR

| Field | Detail |
|:--|:--|
| Requirement Source | Client verbal approval during SES005 consultation; `guideline_workspace_proposal.md` §VII.C GDR field specification |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` |
| Required end-state posture | The GDR records `Client Decision: APPROVE`, `Gate Status After Decision: completed`, all four GIR client-decision fields are populated with `(a)`, the decision date is `2026-03-31`, and the proposal version is bumped to `v1.2.0`. |
| Explicit non-target / do-not-change constraints | Do NOT modify the Consultant Recommendation, the GIR option tables, the Evidence Index, the Gate Package Index, or any section outside §III (Disposition Summary Register), §IV (Detailed Disposition Register), §VI (Gate Decision Record), and §VIII (Changelog). Do NOT alter the external-review or consultant-assessment references. |
| Validation check | (1) GDR table has no `pending` values remaining. (2) All four GIR rows in §III show `(a)` in the Client Decision column. (3) All four detailed GIR sections in §IV show `[x] (a)` as the selected option. (4) The proposal `version` frontmatter reads `1.2.0` and `date` reads `2026-03-31`. (5) A new changelog row exists for v1.2.0. |
| Blocking ambiguity rule | If any GDR field value is ambiguous or if the proposal file structure has changed since v1.1.0 in a way that makes the GIR locations unclear, stop and escalate to the consultant instead of guessing field placements. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md`.

2. In the **frontmatter**, update:
   - `version: '1.2.0'`
   - `date: '2026-03-31'`
   - Leave all other frontmatter fields unchanged.

3. In **§III. DISPOSITION SUMMARY REGISTER**, update the `Client Decision` column for all four GIR rows:
   - GIR-001: change `pending` to `(a)`
   - GIR-002: change `pending` to `(a)`
   - GIR-003: change `pending` to `(a)`
   - GIR-004: change `pending` to `(a)`

4. In **§IV. DETAILED DISPOSITION REGISTER**, for each of the four GIR subsections (GIR-001 through GIR-004), update the `Client Decision:` line:
   - For GIR-001: change `- [ ] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______` to `- [x] (a)`
   - For GIR-002: change `- [ ] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______` to `- [x] (a)`
   - For GIR-003: change `- [ ] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______` to `- [x] (a)`
   - For GIR-004: change `- [ ] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______` to `- [x] (a)`

5. In **§VI. GATE DECISION RECORD**, update the GDR table to these exact values:

   | Field | Value |
   |:--|:--|
   | Gate ID | `P-PH000-ST002-AC006-GATE-001` |
   | Consultant Recommendation | `APPROVE WITH CONDITIONS` |
   | Client Decision | `APPROVE` |
   | Gate Status After Decision | `completed` |
   | Conditions (if any) | `(1) Plan compliance normalization (Task Register schema, non-standard sections, missing Reviewer field) must be completed in the same pass as GDR recording. (2) A post-approval plan amendment must formalize the GATE-002 execution-evidence path before TK007/TK008 execution begins.` |
   | Decided By | `Client` |
   | Decision Date | `2026-03-31` |
   | Decision Reference | `P-PH000-ST002-AC006-SES005 (verbal approval during independent consultant assessment)` |

6. In **§VIII. CHANGELOG**, append a new row:

   | Version | Date | Type | Summary |
   |:--|:--|:--|:--|
   | v1.2.0 | 2026-03-31 | Amendment | Recorded client GATE-001 decision: APPROVE for all four GIR items (a). Updated GDR with client decision, decision date, and decision reference. Gate status is now completed. |

7. Do NOT change any other section of the proposal file.

### SPEC-002 — Normalize Activity Plan Task Register And Remove Non-Standard Sections

| Field | Detail |
|:--|:--|
| Requirement Source | Independent consultant assessment Finding F-001 (Task Register schema deviation from §IV.B), Finding F-002 (non-standard sections), Finding F-003 (missing Reviewer field); `guideline_workspace_plan.md` §IV.B, §VI.C |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Required end-state posture | The Task Register uses the required `guideline_workspace_plan.md` §IV.B schema (`Task ID \| Description \| Status \| Action`). Non-standard narrative sections ("Gate Model", both "Dependency graph" blocks) are removed. The GATE-001 detailed section includes all four required fields per §VI.C. TK006.1, TK006.2, and TK006.3 statuses are correctly recorded. GATE-001 status is `completed`. |
| Explicit non-target / do-not-change constraints | Do NOT modify §I (Executive Summary), §IV (Links Register), or the detailed task sections for TK000 through TK006 (which are already completed and should be preserved as-is). Do NOT change the plan frontmatter fields other than `version` and `date` (those are handled by SPEC-004). Do NOT rewrite detailed task sections for TK007 or TK008 beyond updating their blocking status reference. |
| Validation check | (1) Task Register has exactly four columns: `Task ID \| Description \| Status \| Action`. (2) No "Gate Model" or "Dependency graph" sections exist in the file. (3) GATE-001 detailed section has Entry Criteria, Reviewer, Exit Criteria, and Gate-Disposition Proposal fields. (4) All task statuses are internally consistent with their completion state. |
| Blocking ambiguity rule | If any task's current status is ambiguous or if removing the Gate Model section would eliminate information not captured elsewhere in the plan, stop and escalate instead of deleting content without a recovery path. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md`.

2. **Replace the entire Task Register table** (located in §II. ACTIVITY OUTLINE, under the `### Task Register` heading) with a new table using the required §IV.B schema. The replacement table must use exactly these four columns:

   ```
   | Task ID | Description | Status | Action |
   |:--|:--|:--|:--|
   ```

   Populate the rows as follows (preserve the existing task content but reformat into the required schema):

   | Task ID | Description | Status | Action |
   |:--|:--|:--|:--|
   | `P-PH000-ST002-AC006-TK000` | Assess AC006 readiness and harden the GATE-001 package boundary | `completed` | Published the readiness assessment, added the missing authority inputs, and hardened the plan boundary so later AC006 work can proceed without package ambiguity. |
   | `P-PH000-ST002-AC006-TK001` | Audit current session-close skill and briefing surface gap | `completed` | Published the three-domain gap audit artifact covering session-close reachability, snotes guidance integration, briefing-surface gaps, authority mapping, and lower-intelligence assistant support requirements. |
   | `P-PH000-ST002-AC006-TK002` | Comparative analysis: briefing dashboard architectural options | `completed` | Published the comparative analysis selecting a separate `briefing_program.md` file as the bounded V1.1 briefing architecture and deferred richer prioritization to the future status-system initiative. |
   | `P-PH000-ST002-AC006-TK003` | Standards-input proposal: briefing dashboard | `completed` | Authored the briefing dashboard standards-input proposal defining the separate-file placement, ledger-first derivation hierarchy, three-section V1.1 model, and manual prompt-assist-only execution boundary. |
   | `P-PH000-ST002-AC006-TK004` | Implementation spec: session-close skill hardening | `completed` | Authored the detailed post-gate execution specification for the hardened session-close skill, dual-symlink reachability, explicit snotes guidance, and lower-intelligence assistant scaffolding. |
   | `P-PH000-ST002-AC006-TK005` | Implementation spec: briefing dashboard | `completed` | Authored the detailed post-gate execution specification for creating `briefing_program.md` as a separate derived client briefing surface with bounded Active Work, Recent Movement, and Dependency Watch sections. |
   | `P-PH000-ST002-AC006-TK006` | GATE-001 disposition proposal package assembly | `completed` | Authored the base GATE-001 gate-disposition proposal, indexed the current evidence set, and recorded TK006.1 and TK006.2 as deferred next-session inputs before client disposition. |
   | `P-PH000-ST002-AC006-TK006.1` | External review: GATE-001 package | `completed` | Produced the authoritative independent external-review analysis confirming package coherence, GIR soundness, and downstream implementation-spec commissionability. |
   | `P-PH000-ST002-AC006-TK006.2` | Consultant assessment: external review and downstream readiness | `completed` | Assessed the external review, confirmed agreement with all findings, identified packaging posture as the sole remaining blocker, and defined the post-gate path toward GATE-002. |
   | `P-PH000-ST002-AC006-TK006.3` | Post-review normalization and GDR recording | `completed` | Recorded client GATE-001 APPROVE decision in the GDR, normalized the plan to guideline compliance, and formalized the GATE-002 execution-evidence path. |
   | `P-PH000-ST002-AC006-GATE-001` | Gate: client approval of AC006 expanded scope | `completed` | Client approved all four GIR items (a). GDR recorded 2026-03-31. |
   | `P-PH000-ST002-AC006-TK007` | Execute session-close skill hardening | `planned` | — |
   | `P-PH000-ST002-AC006-TK008` | Execute briefing dashboard creation | `planned` | — |
   | `P-PH000-ST002-AC006-GATE-002` | Gate: client approval of AC006 execution evidence | `planned` | — |

3. **Delete the "Gate Model" paragraph**. This is the paragraph starting with `**Gate Model**: \`GATE-001\` is a consultation gate...` located between the Task Register table and the first dependency graph. All the information in this paragraph is already captured in the GATE-001 detailed section's Entry Criteria, Exit Criteria, and the Gate Package evidence requirements.

4. **Delete both "Dependency graph" blocks**. Remove everything from `**Dependency graph (legacy snapshot):**` through the end of the current dependency graph (the second ASCII graph ending with `└─ TK008 (execute: briefing)`), including the `---` separator between the Activity Outline section and the Tasks (Detailed) section. The dependency information is captured by the Task Register's ordering and the `Depends On` fields in each detailed task section.

5. **Add the `Reviewer` field to the GATE-001 detailed section**. In the `### GATE-001: Gate: Client Approval Of AC006 Expanded Scope` section, add the following field after the existing `**Entry Criteria**` block and before the existing `**Exit Criteria**` block:

   ```
   **Reviewer**: Client
   ```

6. **Update the GATE-001 detailed section status**. After the `**Gate-Disposition Proposal**` line, add:

   ```
   **Gate Status**: `completed` — Client approved 2026-03-31. GDR recorded in the gate-disposition proposal.
   ```

7. **Update TK006.1 and TK006.2 Success Criteria checkboxes** in their respective detailed sections. Change all `- [ ]` items to `- [x]` for both tasks, as both are now completed:
   - In the TK006.1 detailed section, change all four success criteria from `[ ]` to `[x]`
   - In the TK006.2 detailed section, change all four success criteria from `[ ]` to `[x]`

8. **Add a minimal TK006.3 detailed section** after the TK006.2 detailed section and before the GATE-001 detailed section. Use this exact content:

   ```markdown
   ### Task TK006.3: Post-Review Normalization And GDR Recording

   **Task ID**: `P-PH000-ST002-AC006-TK006.3`

   **Purpose**: Record the client's GATE-001 approval in the GDR, normalize the activity plan to full guideline compliance, and formalize the GATE-002 execution-evidence path.

   **Deliverable**:
   - Updated GDR in the gate-disposition proposal
   - Normalized activity plan (compliant Task Register, removed non-standard sections, GATE-002 path)

   **Inputs Required**:
   - Independent consultant assessment findings (F-001, F-002, F-003, F-004)
   - Client verbal approval of GATE-001 during SES005

   **Scope**:
   - In scope:
     - GDR recording
     - Task Register schema normalization
     - Non-standard section removal
     - GATE-001 Reviewer field addition
     - GATE-002 path formalization
     - Plan version bump and changelog
   - Out of scope:
     - executing TK007 or TK008
     - modifying any completed analysis, proposal, or implementation artifact other than the GDR update

   **Success Criteria**:
   - [x] GDR records Client Decision = APPROVE with all four GIR items at (a)
   - [x] Task Register uses the required §IV.B schema
   - [x] Non-standard sections removed
   - [x] GATE-001 has all four required §VI.C fields
   - [x] GATE-002 is registered with implementation-backed gate-readiness stack

   **Implementation Spec**: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/implementation/implementation_P-PH000-ST002-AC006_gate-001-normalization-and-gdr-recording-brief.md`
   ```

9. **Update TK007 and TK008 detailed sections**. In both sections, change `**Blocked by**: GATE-001` to `**Depends On**: GATE-001 (completed), GATE-002 (planned)` to reflect that these tasks are now unblocked by GATE-001 but their execution evidence will feed into GATE-002.

### SPEC-003 — Formalize GATE-002 Execution-Evidence Path

| Field | Detail |
|:--|:--|
| Requirement Source | Independent consultant assessment GAP-D; client approval condition (2); `guideline_workspace_plan.md` §VI.L (implementation-backed gate-readiness stack) |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Required end-state posture | A GATE-002 detailed section exists in the plan with all four required §VI.C fields. The GATE-002 follows the implementation-backed gate-readiness stack sequence. Pre-gate readiness tasks are registered. The dependency chain from TK007/TK008 through GATE-002 is explicit. |
| Explicit non-target / do-not-change constraints | Do NOT create the GATE-002 gate-disposition proposal file (that is a future consultant task). Do NOT insert DEV-REPORT, VERIFICATION, or external-review tasks with pre-assigned task IDs beyond TK009–TK012 (reserve space). Do NOT create any new artifact files. |
| Validation check | (1) GATE-002 detailed section has Entry Criteria, Reviewer, Exit Criteria, and Gate-Disposition Proposal fields. (2) The implementation-backed gate-readiness stack is visible in the task dependency chain. (3) No post-GATE-002 tasks are pre-registered. |
| Blocking ambiguity rule | If the implementation-backed gate-readiness stack requires roles or artifact types not yet established in the AC006 context (e.g., `LLM_Reviewer` for verification), use the currently authorized secondary verifier (`LLM_Consultant`) per `workspace_documentation_rules.md` §6.D and note this in the gate section. |
| Status | `open` |

#### Implementation Detail

1. In the same plan file, **add the following new detailed sections after the TK008 detailed section and before §IV. LINKS REGISTER**. Insert them in this exact order:

   First, add the execution-evidence readiness tasks:

   ```markdown
   ### Task TK009: Dev-Report: Session-Close Skill Hardening Execution Evidence

   **Task ID**: `P-PH000-ST002-AC006-TK009`

   **Purpose**: Produce bounded execution evidence for TK007 per `guideline_workspace_dev-report.md`.

   **Deliverable**:
   - `dev-report_P-PH000-ST002-AC006-TK007.md` (path TBD at execution time)

   **Depends On**: TK007

   **Owner**: LLM_Assistant

   ### Task TK010: Dev-Report: Briefing Dashboard Creation Execution Evidence

   **Task ID**: `P-PH000-ST002-AC006-TK010`

   **Purpose**: Produce bounded execution evidence for TK008 per `guideline_workspace_dev-report.md`.

   **Deliverable**:
   - `dev-report_P-PH000-ST002-AC006-TK008.md` (path TBD at execution time)

   **Depends On**: TK008

   **Owner**: LLM_Assistant

   ### Task TK011: Verification: AC006 Execution Evidence Review

   **Task ID**: `P-PH000-ST002-AC006-TK011`

   **Purpose**: Independent verification of TK007 and TK008 execution evidence per `guideline_workspace_verification.md`.

   **Deliverable**:
   - `verification_P-PH000-ST002-AC006-GATE-002.md` (path TBD at execution time)

   **Depends On**: TK009, TK010

   **Owner**: LLM_Consultant (currently authorized secondary verifier per workspace_documentation_rules.md §6.D)

   ### Task TK012: GATE-002 Disposition Proposal Package

   **Task ID**: `P-PH000-ST002-AC006-TK012`

   **Purpose**: Assemble the GATE-002 evidence package for client disposition per `guideline_workspace_proposal.md`.

   **Deliverable**:
   - `proposal/proposal_P-PH000-ST002-AC006-GATE-002_execution-evidence-disposition.md`

   **Depends On**: TK011

   **Owner**: LLM_Consultant

   ### Task TK012.1: External Review: GATE-002 Package

   **Task ID**: `P-PH000-ST002-AC006-TK012.1`

   **Purpose**: Independent external review of the GATE-002 package per `guideline_workspace_analysis.md` §IV.B.

   **Deliverable**:
   - `analysis/analysis_P-PH000-ST002-AC006-GATE-002_external-review.md`

   **Depends On**: TK012

   **Owner**: LLM_Subconsultant

   ### GATE-002: Gate: Client Approval Of AC006 Execution Evidence

   **Gate ID**: `P-PH000-ST002-AC006-GATE-002`

   **Entry Criteria**:
   - TK007 and TK008 execution is complete
   - Dev-reports (TK009, TK010) document execution evidence
   - Verification (TK011) provides independent assessment with verifier verdict
   - Gate-disposition proposal (TK012) packages all evidence
   - External review (TK012.1) provides independent second-opinion audit

   **Reviewer**: Client

   **Exit Criteria**:
   - Client records decision in GDR
   - If APPROVE: AC006 execution is accepted and the activity can proceed toward completion
   - If RECYCLE: remediation tasks are created per §VI.K

   **Gate-Disposition Proposal**: `proposal/proposal_P-PH000-ST002-AC006-GATE-002_execution-evidence-disposition.md` (pending — to be authored as TK012)

   **Gate Type**: Implementation-backed (reviews developer/assistant-mutated deliverables)
   ```

2. **Add the new GATE-002 readiness tasks to the Task Register** (which was already rewritten by SPEC-002). Append these rows after the TK008 row and before the GATE-002 row:

   | Task ID | Description | Status | Action |
   |:--|:--|:--|:--|
   | `P-PH000-ST002-AC006-TK009` | Dev-report: session-close skill hardening execution evidence | `planned` | — |
   | `P-PH000-ST002-AC006-TK010` | Dev-report: briefing dashboard creation execution evidence | `planned` | — |
   | `P-PH000-ST002-AC006-TK011` | Verification: AC006 execution evidence review | `planned` | — |
   | `P-PH000-ST002-AC006-TK012` | GATE-002 disposition proposal package | `planned` | — |
   | `P-PH000-ST002-AC006-TK012.1` | External review: GATE-002 package | `planned` | — |

   The final Task Register should therefore contain rows in this order: TK000, TK001, TK002, TK003, TK004, TK005, TK006, TK006.1, TK006.2, TK006.3, GATE-001, TK007, TK008, TK009, TK010, TK011, TK012, TK012.1, GATE-002.

3. **Update the Links Register** (§IV) to add the new implementation artifact:

   Add this row:

   | Link Type | Target | Path |
   |:--|:--|:--|
   | Implementation | AC006 GATE-001 Normalization Brief | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/implementation/implementation_P-PH000-ST002-AC006_gate-001-normalization-and-gdr-recording-brief.md` |

### SPEC-004 — Plan Version Bump And Changelog

| Field | Detail |
|:--|:--|
| Requirement Source | Standard plan versioning practice; `guideline_workspace_plan.md` changelog conventions |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Required end-state posture | Plan frontmatter shows `version: '2.3.0'` and `date: '2026-03-31'`. A new changelog row records the normalization amendment. |
| Explicit non-target / do-not-change constraints | Do NOT change any other frontmatter field. |
| Validation check | (1) Frontmatter `version` is `2.3.0`. (2) Frontmatter `date` is `2026-03-31`. (3) Changelog has a new row for v2.3.0. |
| Blocking ambiguity rule | If the plan version is already at or above `2.3.0` when the assistant begins execution, stop and escalate — another amendment may have been made between spec authoring and execution. |
| Status | `open` |

#### Implementation Detail

1. In the plan frontmatter, update:
   - `version: '2.3.0'`
   - `date: '2026-03-31'`

2. In **§V. CHANGELOG**, append a new row as the first entry (most recent):

   | Version | Date | Type | Summary |
   |:--|:--|:--|:--|
   | v2.3.0 | 2026-03-31 | Amendment | Recorded GATE-001 client approval. Normalized Task Register to §IV.B required schema (Task ID / Description / Status / Action). Removed non-standard Gate Model and Dependency Graph sections. Added Reviewer field to GATE-001 detailed section. Registered TK006.3 (normalization task). Formalized GATE-002 as the implementation-backed execution-evidence gate with the full readiness stack (TK009–TK012.1). Updated TK006.1 and TK006.2 to completed. Updated TK007/TK008 dependency references. |

## IV. IMPLEMENTATION SEQUENCE

1. **SPEC-001** — Record the client decision in the GDR first, so the gate is formally closed before plan surfaces are modified.
2. **SPEC-002** — Normalize the plan Task Register and remove non-standard sections, including adding the TK006.3 detailed section and updating success criteria checkboxes.
3. **SPEC-003** — Formalize the GATE-002 path by adding the implementation-backed readiness tasks and the GATE-002 detailed section, then updating the Task Register and Links Register.
4. **SPEC-004** — Bump the plan version and record the changelog entry last, so the changelog accurately reflects all changes made in steps 1–3.

**Critical ordering note**: SPEC-002 rewrites the Task Register, and SPEC-003 appends to it. The assistant MUST apply SPEC-002 first (rewrite), then SPEC-003 (append additional rows). Do NOT attempt to build the final Task Register in a single step that merges both SPEC-002 and SPEC-003 — this risks omitting rows if either spec is applied out of order.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Gate-Disposition Proposal (GDR target) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Proposal Guideline (GDR spec) | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Independent Consultant Assessment (findings source) | SES005 consultation session record (this conversation) |
| External Review | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-001_external-review.md` |
| Consultant Assessment (TK006.2) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006-GATE-001_external-review-and-downstream-readiness-assessment.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-31 | Initial | Authored the consolidated normalization and GDR recording brief covering four SPEC items: GDR recording (SPEC-001), plan normalization (SPEC-002), GATE-002 formalization (SPEC-003), and plan version bump (SPEC-004). |
