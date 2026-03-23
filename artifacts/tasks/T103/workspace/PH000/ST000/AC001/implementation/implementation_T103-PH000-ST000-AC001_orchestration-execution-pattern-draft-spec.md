---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC001'
task_id: 'T103-PH000-ST000-AC001-TK001 through TK006'
version: '1.0.0'
date: '2026-03-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/plan_T103-PH000-ST000-AC001.md'
execution_audience: 'consultant'
purpose: 'Task specification for T103-PH000-ST000-AC001: Orchestration Execution Pattern Draft Specification — producing a draft specification for orchestrator-agent execution patterns, including agent dispatch models, context management, wave boundary protocols, recycle re-entry, and sub-consultant integrity dispatch, sufficient for immediate operational use with normative binding deferred to T103-PH001.'
consumers:
  - 'T103-PH000-ST000-AC001-GATE-001'
---

# IMPLEMENTATION (Task Specification): T103-PH000-ST000-AC001 Orchestration Execution Pattern Draft Specification

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the full task decomposition for T103-PH000-ST000-AC001, covering the consultation phase through a single consultation-only GATE-001. The activity produces a draft specification for orchestration execution patterns that translates the workspace governance suite's artifact-level rules into agent-executable dispatch instructions for the main consultant orchestrator.
- **Authority chain**: AC001 activity plan authorizes tracked work -> This artifact specifies the HOW for each task -> PROPOSAL hosts GDR.
- **Audience**: LLM_Consultant (all tasks — `execution_audience: 'consultant'`), Client (GATE-001).
- **Boundary**: This artifact does NOT hold a GDR. Gate decisions are recorded in the respective `gate_disposition` proposal per `guideline_workspace_proposal.md` §VII.
- **Scope limitation**: AC001 produces a **draft specification only**. Full normative binding (integration into `guideline_workspace_implementation.md`, `workspace_documentation_rules.md`, and template production) is explicitly deferred to T103-PH001. The draft specification is sufficient for immediate operational use but is not a governed guideline amendment.

## II. TASK SCOPE

- **Governing plan task**: `T103-PH000-ST000-AC001-TK001` through `TK006` (full activity lifecycle)
- **Trigger**: Consultation during T104-PH001-ST008-AC001.9 scope definition (2026-03-23) identified that orchestration execution patterns — how the main consultant physically translates plans into agent dispatches — are a T103-domain concern distinct from T104's artifact-level governance rules. The orchestration reliability issues observed in `raw_P-PH000-ST002-AC002_SES003.txt` (Claude Code orchestration) and `raw_T103-PH000-ST000-AC000-SES004.md` (Codex orchestration) confirmed the need for codified execution patterns.
- **Deliverable contract**: Draft orchestration execution specification artifact; no governed guideline amendments in this activity.
- **Cross-initiative dependency**: This activity depends on `T104-PH001-ST008-AC001.9` for its normative baseline (artifact-level authoring rules). AC001.9 defines *what* artifacts are produced; this activity defines *how* the orchestrator dispatches agents to produce them. The dependency is informational, not blocking — AC001 can proceed with the current (pre-AC001.9) artifact rules and reference the future AC001.9 outputs as the normative baseline once available.

## III. ACTIVITY CONTEXT

### A. Identified Execution-Pattern Gaps (From Consultation)

| Gap ID | Gap Area | Evidence Source |
|:--|:--|:--|
| EGAP-001 | Agent dispatch model | No codified pattern for how the orchestrator selects agent types, models, effort levels, and write scopes for developer/reviewer/sub-consultant workers |
| EGAP-002 | Context management | No protocol for what context the orchestrator must provide to each sub-agent role (plan excerpts, artifact paths, scope boundaries, recycle state) |
| EGAP-003 | Wave boundary management | No codified rules for how the orchestrator partitions implementation work into waves, manages wave completion signals, and advances to the next wave |
| EGAP-004 | Recycle re-entry execution | No execution-level protocol for how the orchestrator handles RECYCLE verdicts — re-briefing developers, re-dispatching reviewers, managing evidence version lineage across cycles |
| EGAP-005 | Sub-consultant integrity dispatch | No execution-level protocol for when and how the orchestrator dispatches a sub-consultant for post-loop traceability/integrity validation |

### B. Gate Model

- **GATE-001** (Consultation-only): Analysis + draft specification + gate-disposition proposal -> client approval of draft specification
- No GATE-002 — this activity produces no governed guideline amendments

### C. Cross-Initiative Interface

T103-AC001 produces the **execution-level patterns** that operationalize `T104-PH001-ST008-AC001.9`'s artifact-level authoring rules. The interface is:
- **AC001.9 (T104)** defines: what artifacts the developer/reviewer/consultant must produce, what schemas they follow, how artifacts relate to each other in recyclable loops
- **AC001 (T103)** defines: how the orchestrator physically dispatches agents to produce those artifacts, manages context windows, handles wave boundaries, and assembles gate packages

### D. Governance Standing

T103 currently has no SPS or PRD. This activity operates under inherited governance from:
- `workspace_documentation_rules.md` (workflow chain and role-to-artifact ownership)
- `guideline_workspace_plan.md` (plan authoring rules)
- `guideline_workspace_analysis.md` (analysis authoring rules)
- `guideline_workspace_proposal.md` (gate-disposition proposal rules)
- `guideline_workspace_implementation.md` (this specification's authoring rules)

Full T103 governance (SPS, PRD) is anticipated in T103-PH001.

---

## IV. SPECIFICATION ITEMS

### SPEC-001 — Create AC001 Activity Plan and Register in ST000 Stream Plan

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §IV; stream plan registration rules §IV.D |
| Primary Inputs | This implementation specification; T103-PH000-ST000 stream plan; `guideline_workspace_plan.md` |
| Output | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/plan_T103-PH000-ST000-AC001.md` |
| Acceptance Criteria | Activity plan exists at canonical path with full task register matching this specification's task decomposition (TK001–TK006 + GATE-001); AC001 is registered in the ST000 stream plan activity register with a contract stub per §IV.D; stream plan version bumped |
| Owner | LLM_Consultant |
| Task ID | `T103-PH000-ST000-AC001-TK001` |
| Status | `open` |

#### Implementation Detail

1. Instantiate the activity plan template (`template_workspace_plan_activity.md`) for `T103-PH000-ST000-AC001`.
2. Populate the activity outline:
   - **Activity ID**: `T103-PH000-ST000-AC001`
   - **Name**: Orchestration Execution Pattern Draft Specification
   - **Objective**: Produce a draft specification for orchestrator-agent execution patterns covering agent dispatch, context management, wave boundaries, recycle re-entry, and sub-consultant integrity dispatch — sufficient for immediate operational use, with normative binding deferred to T103-PH001.
   - **Execution Mode**: `GATED`
   - **Depends On**: `—` (independently startable; AC000 outputs are informational inputs)
3. Populate the task register with TK001–TK006 + GATE-001 as specified in §V.
4. Register AC001 in the ST000 stream plan (`plan_T103-PH000-ST000.md`):
   - Add a row to the Activity Register after AC000 (and AC000.1 if present as a sub-activity)
   - Add a contract stub in the Activities (High-Level) section with Purpose, Deliverable, Scope, Activity Plan link, and Success Criteria Checklist (summary)
   - Bump the stream plan version
   - Add AC001 to the Links Register
5. Context section of the activity plan should reference:
   - `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
   - `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
   - `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`
   - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_gate-001-to-gate-002-orchestration-plan.md` (AC001.6 orchestration exemplar)
   - `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/implementation/implementation_T104-PH001-ST008-AC001.9_recyclable-loop-artifact-governance.md` (cross-initiative interface)
   - `raw_P-PH000-ST002-AC002_SES003.txt` (Claude Code orchestration evidence)
   - `raw_T103-PH000-ST000-AC000-SES004.md` (Codex orchestration evidence)
   - This implementation specification

---

### SPEC-002 — Produce AC001 SES001 Session Notes

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` §1.6, §5.1 (JIT registration), §6 |
| Primary Inputs | Consultation conversation context (2026-03-23); this implementation specification |
| Output | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/snotes/snotes_T103-PH000-ST000-AC001-SES001.md` |
| Acceptance Criteria | Session notes file exists at canonical path following `template_workspace_notes_session_activity.md`; captures the consultation decisions, discussion points, and actions from the 2026-03-23 session that established AC001 scope; registered in the ST000 stream notes register (JIT per §5.1) |
| Owner | LLM_Consultant |
| Task ID | `T103-PH000-ST000-AC001-TK001` (bundled with SPEC-001) |
| Status | `open` |

#### Implementation Detail

1. Create the session notes file using `template_workspace_notes_session_activity.md`.
2. Title: `ACTIVITY SESSION NOTES: T103 (ADRSS) — PH000 / ST000 / AC001 / SES001 (Orchestration Execution Pattern — Scope Consultation)`
3. Capture the following from the consultation record:
   - **Agenda**: (a) Orchestration execution pattern gaps assessment, (b) Initiative boundary decision (T103 vs T104), (c) AC001 scope and planning level determination, (d) Gate model confirmation
   - **Discussion Points**:
     - DP001: Two-concern decomposition identified — artifact-level rules (T104 AC001.9) vs orchestration execution patterns (T103 AC001)
     - DP002: Orchestration reliability issues observed in raw session evidence (SES003, SES004) — boundary confusion, integrity assumptions, shared dependency constraints
     - DP003: T103 governance standing — no SPS/PRD; draft specification only until PH001
     - DP004: Activity vs stream level decision — activity under ST000 recommended
   - **Decisions**:
     - DEC001: AC001 at activity level under ST000 (not a new stream) — Status: `Confirmed`, Owner: Client
     - DEC002: Consultation-only single gate (GATE-001); no implementation-backed gate since output is a draft specification — Status: `Confirmed`, Owner: Client
     - DEC003: Normative binding (guideline amendments, template production) deferred to T103-PH001 — Status: `Confirmed`, Owner: Client
     - DEC004: AC001 independently startable (`Depends On: —`); AC000 outputs are informational inputs — Status: `Confirmed`, Owner: Client
     - DEC005: Cross-initiative interface — AC001.9 (T104) provides normative baseline for AC001 (T103) execution patterns — Status: `Confirmed`, Owner: Client
   - **Actions**:
     - ACT001: Produce T103-AC001 implementation specification (this artifact) — Owner: LLM_Consultant, Status: `completed`
     - ACT002: Execute AC001 plan creation (SPEC-001) — Owner: LLM_Consultant, Status: `pending`
   - **Open Questions**: None remaining at session close
   - **Handoff**: Implementation specification produced; assistant to execute SPEC items sequentially per §V
4. Register the session in the ST000 stream notes register per JIT rule (§5.1). If the stream notes register (`notes_T103-PH000-ST000.md`) exists, add a row. If it does not exist, create it using `template_workspace_notes_register_stream.md`.

---

### SPEC-003 — Produce Orchestration Execution Pattern Assessment

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_analysis.md` §III (`assessment` type), §V |
| Primary Inputs | AC001.6 orchestration plan; raw session evidence (SES003, SES004); `workspace_documentation_rules.md`; `guideline_workspace_plan.md`; `guideline_workspace_implementation.md` |
| Output | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/analysis/analysis_T103-PH000-ST000-AC001_orchestration-execution-pattern-assessment.md` |
| Acceptance Criteria | Analysis artifact exists at canonical path following `template_workspace_analysis.md`; `analysis_type: 'assessment'`; contains GAP register with EGAP-001 through EGAP-005 (minimum); includes Assessment section (§V.B) with current state, options, and recommendations per gap; includes Downstream Actions section (§VIII) |
| Owner | LLM_Consultant |
| Task ID | `T103-PH000-ST000-AC001-TK002` |
| Status | `open` |

#### Implementation Detail

1. Create the analysis artifact using `template_workspace_analysis.md`.
2. Frontmatter:
   - `artifact_type: 'ANALYSIS'`
   - `analysis_type: 'assessment'`
   - `initiative_id: 'T103'`
   - `initiative_code: 'ADRSS'`
   - `phase: '0'`
   - `stream_id: 'T103-PH000-ST000'`
   - `activity_id: 'T103-PH000-ST000-AC001'`
   - `task_id: 'T103-PH000-ST000-AC001-TK002'`
   - `plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/plan_T103-PH000-ST000-AC001.md'`
   - `purpose: 'Assessment of orchestration execution pattern gaps across agentic CLI environments, identifying agent dispatch, context management, wave boundary, recycle re-entry, and sub-consultant integrity dispatch deficiencies.'`
3. **Executive Summary**: Summarize the five execution-pattern gaps, their origin in operational evidence, and the recommended draft specification approach. Include Client Summary subsection since this analysis feeds GATE-001.
4. **Scope & Inputs**:
   - In scope: Agent dispatch model patterns, context management protocols, wave boundary management, recycle re-entry execution patterns, sub-consultant integrity dispatch patterns
   - Out of scope: Artifact-level authoring rules (T104 AC001.9), governed guideline amendments, template production, T103 PH001 governance work
   - Inputs: List AC001.6 orchestration plan, raw session files, workspace_documentation_rules.md §7-§8, guideline_workspace_plan.md §VI.L, guideline_workspace_implementation.md (CONV-013)
5. **Evidence / Methodology**: Review of raw orchestration session transcripts against the workspace governance suite's implicit execution expectations. For each gap, cite the specific session evidence that exposed the gap and the specific governance rule that is silent.
6. **Findings / GAP Register**: Minimum five entries:

   | GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
   |:--|:--|:--|:--|:--|:--|:--|
   | EGAP-001 | workflow | Agent dispatch model | No codified pattern for orchestrator selection of agent types, models, effort levels, and write scopes. AC001.6 and T103-AC000 invented ad-hoc dispatch tables (§III of orchestration plans). | `pending_decision` | TK003 | Exposed across both CLI environments |
   | EGAP-002 | workflow | Context management protocol | No protocol for what plan/artifact/scope context the orchestrator must inject into each sub-agent's prompt. Sub-agents in SES003 and SES004 lost context mid-execution. | `pending_decision` | TK003 | Critical for context efficiency |
   | EGAP-003 | workflow | Wave boundary management | No codified rules for how implementation work is partitioned into waves, how wave completion is signaled, and how the orchestrator advances. AC001.6 SPEC-005 defined waves ad-hoc. | `pending_decision` | TK003 | Directly tied to DEV-REPORT package taxonomy (AC001.9 GAP-001) |
   | EGAP-004 | workflow | Recycle re-entry execution | No execution-level protocol for how the orchestrator manages RECYCLE verdicts: re-briefing developers with reviewer findings, re-dispatching reviewers with updated evidence, tracking version lineage. | `pending_decision` | TK003 | Directly tied to recyclable-loop handoff contract (AC001.9 GAP-004) |
   | EGAP-005 | workflow | Sub-consultant integrity dispatch | No execution-level protocol for when and how the orchestrator dispatches sub-consultant for post-loop traceability/integrity validation before gate packaging. | `pending_decision` | TK003 | Directly tied to sub-consultant traceability audit (AC001.9 GAP-003) |

7. **Assessment section** (§V.B):
   - **Current State Summary**: For each gap, describe what the orchestrator currently does (ad-hoc, in-context invention) and what failures this produces (context loss, boundary confusion, integrity assumptions).
   - **Options**: For each gap, present at least two options:
     - Option A: Codify as a section within a new draft `orchestration_specification` companion document
     - Option B: Codify as an extension to `guideline_workspace_implementation.md` (new `implementation_type: 'orchestration_specification'`)
   - **Recommendation**: Recommend Option A (draft companion document) for PH000 since it avoids amending a governed guideline without T103 governance standing. Option B can be pursued in PH001 once T103 has proper governance.
8. **Downstream Actions**: Map each gap to TK003 (draft specification authoring).

---

### SPEC-004 — Draft Orchestration Execution Specification

| Field | Detail |
|:--|:--|
| Requirement Source | TK002 analysis recommendations; AC001.6 orchestration plan as exemplar |
| Primary Inputs | TK002 analysis artifact; AC001.6 orchestration plan; `workspace_documentation_rules.md` §7-§8; `guideline_workspace_plan.md` §VI.L |
| Output | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/implementation/implementation_T103-PH000-ST000-AC001_orchestration-execution-patterns.md` |
| Acceptance Criteria | Draft specification exists as an IMPLEMENTATION `task_specification` with `execution_audience: 'consultant'`; covers all five EGAP areas with codified patterns; includes decision tests for when each pattern applies; references AC001.9 artifact-level rules as normative baseline (with explicit note that AC001.9 may not yet be complete); self-declares as draft-only with normative binding deferred to T103-PH001 |
| Owner | LLM_Consultant |
| Task ID | `T103-PH000-ST000-AC001-TK003` |
| Depends On | TK002 |
| Status | `open` |

#### Implementation Detail

1. Create the draft specification as an IMPLEMENTATION `task_specification` artifact with `execution_audience: 'consultant'`.
2. Structure the specification around five SPEC items, one per EGAP:

   **SPEC-D001 — Agent Dispatch Model**:
   - Define a standard agent assignment table schema: `| Role | Agent Type | Model | Effort | Write Scope | Ownership |`
   - Define selection criteria for model/effort based on task complexity and ownership
   - Define write-scope boundary rules (disjoint scopes for parallel workers; no overlapping file writes)
   - Reference `workspace_documentation_rules.md` §8 role-to-artifact ownership matrix as the authoritative role assignment
   - Include decision test: when to use developer workers vs reviewer workers vs sub-consultant workers

   **SPEC-D002 — Context Management Protocol**:
   - Define a minimum context injection template for each sub-agent role:
     - **Developer worker**: plan excerpt (task scope + deliverable + success criteria), implementation specification (if exists), write-scope file list, recycle state (if applicable, including reviewer findings)
     - **Reviewer worker**: plan excerpt (gate entry/exit criteria), DEV-REPORT path(s), artifact paths under review, verification guideline reference
     - **Sub-consultant worker**: plan excerpt (full activity context), evidence index (all artifacts produced in the loop), traceability audit criteria, gate-disposition proposal template reference
   - Define context efficiency rules: what to include vs what to reference by path
   - Define context refresh rules: when the orchestrator must re-inject updated context (e.g., after a recycle verdict)

   **SPEC-D003 — Wave Boundary Management**:
   - Define wave partitioning criteria: group tasks by dependency chain, write-scope disjointness, or thematic cohesion
   - Define wave completion signal: when the orchestrator considers a wave done (all tasks in terminal status, DEV-REPORT produced)
   - Define wave advancement protocol: orchestrator checks wave completion, dispatches reviewer, processes reviewer verdict, then advances or recycles
   - Cross-reference to AC001.9 DEV-REPORT package taxonomy: each wave produces a supplementary DEV-REPORT; the final wave's completion triggers the consolidated DEV-REPORT

   **SPEC-D004 — Recycle Re-Entry Execution**:
   - Define the orchestrator's recycle handling sequence:
     1. Receive RECYCLE verdict from reviewer
     2. Assess reviewer findings (Situation A vs Situation B per `guideline_workspace_verification.md` §VII)
     3. If Situation B: amend plan before proceeding (or dispatch sub-consultant to amend)
     4. If remediation specification needed: dispatch sub-consultant to author it
     5. Re-brief developer with: original task scope + reviewer findings + remediation specification (if exists)
     6. Re-dispatch developer for remediation work
     7. Re-dispatch reviewer with updated evidence (version-bumped verification artifact)
   - Define version-lineage tracking: how the orchestrator maintains the chain of DEV-REPORT versions and verification versions across cycles
   - Cross-reference to AC001.9 recyclable-loop evidence handoff contract

   **SPEC-D005 — Sub-Consultant Integrity Dispatch**:
   - Define the trigger: after a recyclable loop completes (reviewer passes) and before gate packaging
   - Define the dispatch protocol: what context the orchestrator provides to the sub-consultant (full evidence index, plan authority, role boundary matrix, expected audit criteria)
   - Define the output contract: sub-consultant produces a structured traceability assessment that the orchestrator incorporates into the gate-disposition proposal evidence index
   - Cross-reference to AC001.9 sub-consultant traceability audit protocol (artifact-level rules)

3. Include a §IV (Non-Interruption / Control Rules) section adapted from the AC001.6 orchestration plan pattern.
4. Include a §V (Decision Tests) section with a summary decision table:

   | Situation | Pattern | Reference |
   |:--|:--|:--|
   | Single-task, single-agent | No orchestration needed; direct execution | — |
   | Multi-task, single-wave | Agent dispatch + context management | SPEC-D001, D002 |
   | Multi-task, multi-wave | Add wave boundary management | SPEC-D003 |
   | Recyclable loop (RECYCLE verdict) | Add recycle re-entry | SPEC-D004 |
   | Gate packaging after recyclable loop | Add sub-consultant integrity dispatch | SPEC-D005 |

5. Explicitly declare: "This specification is draft-only for operational use. Normative binding into `guideline_workspace_implementation.md` or `workspace_documentation_rules.md` is deferred to T103-PH001."

---

### SPEC-005 — Produce GATE-001 Gate-Disposition Proposal

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_proposal.md` §V.B, §VII; `guideline_workspace_plan.md` §VI.L (consultation-only sequence) |
| Primary Inputs | TK002 analysis artifact; TK003 draft specification |
| Output | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/proposal/proposal_T103-PH000-ST000-AC001-GATE-001_gir-disposition-package.md` |
| Acceptance Criteria | Gate-disposition proposal exists at canonical path; contains GIR items for the draft specification acceptance and the deferred normative-binding acknowledgment; consultant recommendation populated; GDR pending client decision |
| Owner | LLM_Consultant |
| Task ID | `T103-PH000-ST000-AC001-TK004` |
| Depends On | TK003 |
| Status | `open` |

#### Implementation Detail

1. Create the gate-disposition proposal following established pattern.
2. Build the gate package index referencing the TK002 analysis and TK003 draft specification.
3. Create GIR items (minimum):
   - **GIR-001**: Accept the orchestration execution pattern assessment as a valid identification of the five execution-pattern gaps — approve the assessment findings
   - **GIR-002**: Accept the draft orchestration execution specification as sufficient for immediate operational use — approve the draft specification for operational adoption
   - **GIR-003**: Acknowledge that normative binding (guideline amendments, template production, formal `orchestration_specification` implementation_type) is deferred to T103-PH001 — approve the deferral
   - **GIR-004**: Acknowledge the cross-initiative interface with T104-PH001-ST008-AC001.9 — approve that AC001.9 artifact-level rules form the normative baseline for the execution patterns
4. Populate the consultant recommendation as `APPROVE`.
5. Leave the GDR pending client decision.

---

### SPEC-006 — GATE-001: Client Approval of Draft Specification

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §VI |
| Primary Inputs | TK004 gate-disposition proposal |
| Output | Client decision recorded in the GDR |
| Acceptance Criteria | GDR records client decision; if `APPROVE`, AC001 is closed (no Phase 2 since the output is a draft specification, not a governed amendment) |
| Owner | Client |
| Gate ID | `T103-PH000-ST000-AC001-GATE-001` |
| Status | `open` |

#### Implementation Detail

Consultation-only gate. No DEV-REPORT or VERIFICATION required. Client reviews the gate package (assessment + draft specification + proposal) and records a decision in the GDR. If approved, AC001 is closed and the draft specification is available for immediate operational use.

---

## V. IMPLEMENTATION SEQUENCE

```
Phase 1 — Consultation (GATE-001) [Single phase; no Phase 2]
  SPEC-001  TK001   Create AC001 activity plan + register in ST000 stream plan
  SPEC-002  TK001   Produce SES001 session notes (bundled with SPEC-001)
  SPEC-003  TK002   Produce orchestration execution pattern assessment
  SPEC-004  TK003   Draft orchestration execution specification
  SPEC-005  TK004   Produce GATE-001 gate-disposition proposal
  SPEC-006  GATE-001  Client approval of draft specification
```

**Dependency chain**: TK001 -> TK002 -> TK003 -> TK004 -> GATE-001

---

## VI. RISKS

| Risk ID | Description | Mitigation |
|:--|:--|:--|
| R-001 | Cross-initiative dependency — AC001.9 (T104) artifact-level rules may not be complete when AC001 draft specification is authored. Draft specification references may point to future-state rules. | Draft specification explicitly declares dependency on AC001.9 as normative baseline and notes which rules are current vs anticipated. Draft status accommodates this. |
| R-002 | T103 governance standing — T103 has no SPS/PRD. Draft specification cannot be normatively bound until PH001 establishes governance. | Explicitly deferred. GATE-001 GIR-003 records the deferral. |
| R-003 | Platform coupling — Orchestration patterns depend on specific CLI capabilities (Claude Code sub-agents, Codex agents). Patterns may not generalize across platforms. | Draft specification should include platform-specific notes where patterns diverge and a portability assessment section. |
| R-004 | Draft specification staleness — If the draft specification is not bound in PH001, it may drift as operational practices evolve. | Register the PH001 binding requirement explicitly in the GATE-001 GDR so it becomes a traceable intake item for PH001 planning. |

---

## VII. REFERENCES

| Document | Path |
|:--|:--|
| Governing plan (to be created) | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/plan_T103-PH000-ST000-AC001.md` |
| ST000 stream plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| AC001.6 orchestration plan (exemplar) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_gate-001-to-gate-002-orchestration-plan.md` |
| AC001.9 implementation specification (cross-initiative interface) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.9/implementation/implementation_T104-PH001-ST008-AC001.9_recyclable-loop-artifact-governance.md` |
| Raw Claude Code orchestration evidence | `raw_P-PH000-ST002-AC002_SES003.txt` |
| Raw Codex orchestration evidence | `raw_T103-PH000-ST000-AC000-SES004.md` |
| Documentation rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Plan guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| IMPLEMENTATION guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| VERIFICATION guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| T103 phase plan | `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md` |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-23 | Initial | Task specification for T103-PH000-ST000-AC001: Orchestration Execution Pattern Draft Specification. Covers consultation-only activity lifecycle through GATE-001. Five execution-pattern gaps identified: agent dispatch model, context management, wave boundary management, recycle re-entry execution, sub-consultant integrity dispatch. Cross-initiative interface with T104-PH001-ST008-AC001.9 established. Produced from AC001.9 SES001 consultation (2026-03-23). |
