---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.6'
task_id: 'T104-PH001-ST008-AC001.6-TK003.5'
version: '1.3.0'
date: '2026-03-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md'
purpose: 'High-level consultant-owned orchestration plan for executing AC001.6 from the already-closed GATE-001 package normalization point through GATE-002 disposition using delegated sub-consultant execution, multi-wave DEV-REPORT traceability, bounded recycle loops, and a downstream readiness review whose accepted substitute was used after Claude direct-authoring failure.'
execution_audience: 'consultant'
---

# IMPLEMENTATION (Task Specification): AC001.6 GATE-001 to GATE-002 Orchestration Plan

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact defines the orchestration model the consultant will use to move AC001.6 from the already-closed `GATE-001` package normalization point through downstream implementation, verification, and `GATE-002` disposition.
- **Authority chain**: AC001.6 plan remains tracked-work authority -> this artifact specifies the orchestration HOW -> delegated sub-consultant and developer/reviewer workers execute the bounded slices -> main consultant advances the phase boundaries and presents the final package to the client.
- **Audience**: Main LLM_Consultant (orchestrator only), delegated LLM_Consultant subagent (consultant-owned execution), LLM_Developer (execution workers), LLM_Reviewer (review and verification workers), Client (decision owner).
- **Boundary**: The main consultant orchestrates only and does not directly perform artifact execution during the run. Consultant-owned execution work is delegated to a sub-consultant agent. `GATE-001` is already closed after `TK003.4` and the initial `TK003.5` orchestration setup; `GATE-002` remains client-owned and is recorded only in the relevant gate-disposition proposal.
- **Trigger**: Client QA requested (a) explicit indexing of the external review inside the `GATE-001` proposal package, (b) a high-level orchestration plan covering remediation through `GATE-002`, (c) clearer DEV-REPORT / VERIFICATION traceability across recycle loops, and (d) delegated consultant execution rather than direct main-consultant artifact work.

## II. ORCHESTRATION MODEL DECISION

### A. Assessment of the Execution Model

- **Conclusion**: Agree with the need for more granular producer evidence and delegated consultant execution; agree only in part with reviewer-local orchestration as a general model.
- **DEV-REPORT recommendation**: The current `guideline_workspace_dev-report.md` supports multiple bounded DEV-REPORTs and one final consolidated DEV-REPORT via `consolidated_from`, but it does not define a formal primary/supplementary DEV-REPORT package taxonomy. The approved posture for AC001.6 is therefore a hybrid: multiple wave DEV-REPORTs plus one primary consolidated `TK010` handoff report. Formal DEV-REPORT package semantics are flagged for later remediation, not improvised here.
- **Reviewer-local recycle scope**: Reviewer-local recycle is allowed only for bounded consultant-owned package/planning remediation. It is not the default model for the main developer-owned implementation waves because that would weaken clean ownership and evidence boundaries.
- **Consultant execution posture**: All consultant-owned artifact execution is delegated to a `gpt-5.4` `high` sub-consultant. The main consultant remains the orchestrator and final presenter only.
- **Gate state**: `GATE-001` closure has already been recorded in the gate package. This orchestration plan starts from that closed state and does not re-open the gate before downstream readiness review or developer commissioning.
- **Execution-variance disposition**: The preferred Claude-authored readiness artifact was not produced because direct authoring failed in the local environment. The consultant-authored downstream-readiness analysis was accepted as the `SPEC-003` substitute, no blocking plan/spec gap was found, and the runtime issue was escalated separately to T103.

### B. Approved Execution Posture by Phase

| Phase | Recommended Model | Why |
|:--|:--|:--|
| Closed `GATE-001` package normalization state | Delegated sub-consultant + developer + reviewer | Keeps consultant-owned package closure off the main consultant while preserving bounded recycle efficiency. |
| Claude second-opinion intake and downstream plan/spec cleanup | Claude direct authoring target + delegated sub-consultant substitute-disposition fallback | Planning-surface remediation stays consultant-owned and traceable; if Claude direct authoring fails, the delegated sub-consultant may accept a consultant-authored substitute disposition before Phase 2 begins. |
| Main developer-owned Phase 2 implementation | Consultant-mediated developer/reviewer waves with wave DEV-REPORTs | Preserves ownership, improves visibility, and feeds a stronger final gate package. |
| `GATE-002` verification and disposition | Independent reviewer + delegated sub-consultant + main consultant presentation | Keeps final evidence and consultant recommendation separate, with the main consultant acting only as orchestrator/presenter. |

## III. MODEL / AGENT ASSIGNMENTS

| Role | Model | Effort | Ownership |
|:--|:--|:--|:--|
| Main consultant | Current Codex main context | n/a | Orchestration only: spawn agents, manage boundaries, integrate status, present final package |
| Delegated sub-consultant | `gpt-5.4` | `high` | Consultant-owned artifact execution, integrity audits, GDR/proposal updates |
| Developer worker | `gpt-5.4-mini` | `xhigh` | Package remediation or downstream implementation within assigned write scope |
| Reviewer worker | `gpt-5.4` | `high` | Review findings, recycle verdicts, formal verification authoring |
| Claude second opinion | `claude` CLI `--model opus --effort medium` | `medium` | Preferred direct authoring path for the repo-tracked `external_review` analysis artifact; not achieved in this run |

## IV. ORCHESTRATION SPECIFICATION ITEMS

### SPEC-001 — GATE-001 Package Remediation Loop

| Field | Detail |
|:--|:--|
| Requirement Source | Client QA; `implementation_T104-PH001-ST008-AC001.6_gate-001-package-remediation.md` |
| Primary Inputs | External review, package-remediation task specification, current proposal / plan / analysis / vertical implementation spec |
| Output | Remediated `GATE-001` package plus delegated sub-consultant integrity confirmation |
| Acceptance Criteria | All five package-remediation SPEC items are closed; the external review is indexed in the proposal; no unresolved package-navigation or downstream-authority ambiguity remains; main consultant performed no direct artifact execution |
| Status | `completed` |

#### Implementation Detail

The main consultant previously spawned one `gpt-5.4-mini` developer worker to execute the package-remediation specification exactly as written. After that worker completed, the main consultant spawned one `gpt-5.4` reviewer worker to assess the remediated package. Once the reviewer passed the package, the delegated sub-consultant performed the consultant-owned closure work on the remediated package. This gate state is now closed and serves as the starting baseline for the remaining orchestration steps.

---

### SPEC-002 — Record the GATE-001 Approval After Remediation Closure

| Field | Detail |
|:--|:--|
| Requirement Source | Client QA + `guideline_workspace_proposal.md` §VII |
| Primary Inputs | Remediated `GATE-001` proposal package; reviewer result from SPEC-001 |
| Output | Updated `GATE-001` proposal/GDR reflecting the already-declared client approval condition as satisfied |
| Acceptance Criteria | `GATE-001` is updated only after the remediation loop closes successfully and the delegated sub-consultant confirms package integrity |
| Status | `completed` |

#### Implementation Detail

After SPEC-001 passes, the delegated sub-consultant reassesses the package-level recommendation. The approved closure state is now recorded in the `GATE-001` proposal/GDR as `APPROVE`, with `Gate Status After Decision = completed`. No separate new client checkpoint is required because the client had already declared approval contingent on correct remediation, and that condition is now satisfied.

---

### SPEC-003 — Run the Claude Code Second-Opinion Readiness Review

| Field | Detail |
|:--|:--|
| Requirement Source | Client instruction; local `.agents/skills/claude-code/SKILL.md` |
| Primary Inputs | AC001.6 plan; remediated `GATE-001` package; downstream implementation artifacts |
| Output | Repo-tracked downstream-readiness analysis artifact assessing whether all downstream tasks beyond `GATE-001` are implementation-ready |
| Acceptance Criteria | Preferred path is a Claude-authored artifact; accepted fallback is a consultant-authored substitute disposition if Claude direct authoring fails and the delegated sub-consultant closes the variance explicitly before Phase 2 commissioning begins |
| Status | `completed` |

#### Implementation Detail

The preferred execution path was to use the local Claude Code skill with `opus` and `medium` effort in a write-capable mode so Claude would directly author the repo-tracked `external_review` analysis artifact. In the actual run, that direct-authoring path failed in the local environment. The delegated consultant-side flow therefore closed `SPEC-003` with the consultant-authored downstream-readiness analysis artifact at `analysis_T104-PH001-ST008-AC001.6_downstream-readiness-second-opinion.md`, explicitly accepting it as the substitute disposition for the failed Claude-authored path. The related skill/runtime reliability issue was recorded separately for T103 follow-up.

---

### SPEC-004 — Remediate Any Claude-Identified Planning / Specification Gaps

| Field | Detail |
|:--|:--|
| Requirement Source | Claude second-opinion output from SPEC-003 |
| Primary Inputs | Claude findings; AC001.6 plan; downstream implementation artifacts |
| Output | Normalized downstream plan/spec package ready for developer commissioning |
| Acceptance Criteria | Any accepted Claude findings, or findings from an accepted substitute readiness disposition, are either remediated or explicitly dispositioned by the delegated sub-consultant before Phase 2 developer work begins |
| Status | `completed` |

#### Implementation Detail

No blocking planning/specification gap was identified by the accepted readiness disposition. As a result, no separate consultant-owned remediation loop was required before Phase 2 developer work began. The only residual item was the low-risk DEV-REPORT taxonomy follow-up, which was explicitly accepted as future governance work rather than a gate blocker.

---

### SPEC-005 — Execute Developer-Owned Phase 2 Work Under Consultant-Mediated Review Loops

| Field | Detail |
|:--|:--|
| Requirement Source | Approved `GATE-001` package; AC001.6 plan TK004–TK010 |
| Primary Inputs | Approved gate package; normalized downstream implementation specs |
| Output | Completed developer-owned file changes plus wave DEV-REPORT evidence and one primary consolidated `TK010` DEV-REPORT |
| Acceptance Criteria | Each developer-owned wave ends with its own DEV-REPORT and reviewer pass before the next wave begins; `TK010` is a consolidation artifact, not the only implementation report; no reviewer-local nested rework is used for the main implementation waves |
| Status | `completed` |

#### Implementation Detail

For the main Phase 2 work, the main consultant remains the top-level orchestrator. The main consultant may commission multiple `gpt-5.4-mini` developer workers in disjoint write scopes, but each worker should complete its assigned scope before review begins. After a developer wave completes, the main consultant commissions a `gpt-5.4` reviewer on that wave. If findings are returned, the main consultant commissions a fresh developer rework worker against the reviewer findings and repeats the loop. This preserves role separation, DEV-REPORT lineage, and clean evidence ownership.

Approved high-level slicing:

1. Wave A: governance guideline / template surfaces -> `TK010.1` DEV-REPORT
2. Wave B: program-standard surfaces -> `TK010.2` DEV-REPORT
3. Wave C: validator + test surfaces -> `TK010.3` DEV-REPORT
4. `TK010`: primary consolidated DEV-REPORT for `GATE-002` handoff, using `consolidated_from` and an `Artifact Index`

Conditional tasks such as `TK006.1` and `TK007` execute only if authorized by the final `GATE-001` disposition and normalized plan dependencies.

**Governance note**: Current `guideline_workspace_dev-report.md` supports bounded and consolidated reports, but it does not yet define a formal primary/supplementary DEV-REPORT package taxonomy analogous to VERIFICATION packages. AC001.6 therefore uses the approved hybrid model above and explicitly flags DEV-REPORT package semantics as a future remediation candidate rather than inventing an ungoverned subtype now.

---

### SPEC-006 — Produce GATE-002 Verification and Gate Disposition

| Field | Detail |
|:--|:--|
| Requirement Source | AC001.6 plan TK011–TK012 + `GATE-002` |
| Primary Inputs | DEV-REPORT, final changed artifacts, approved task specifications |
| Output | Reviewer-owned `GATE-002` verification artifact and delegated sub-consultant-owned `GATE-002` gate-disposition proposal |
| Acceptance Criteria | Final verification is performed by an independent reviewer agent; delegated sub-consultant performs the integrity audit and proposal authoring; main consultant presents the full package to the client only after verification is complete |
| Status | `completed` |

#### Implementation Detail

After `TK010` DEV-REPORT is complete, the main consultant commissions a separate `gpt-5.4` reviewer to produce the formal `GATE-002` verification artifact. If the verification verdict is `RECYCLE`, the same `GATE-002` identity is preserved, the verification artifact is version-bumped, and a supplementary `revision-checklist` artifact is produced when the findings are too complex for direct rework execution. Once the verification package is complete, the delegated sub-consultant performs the recycle-loop integrity audit across the wave DEV-REPORTs, consolidated DEV-REPORT, and VERIFICATION evidence, then authors the `GATE-002` gate-disposition proposal. The main consultant presents the final package to the client.

## V. ORCHESTRATION SEQUENCE

```
SPEC-001  GATE-001 package remediation loop
SPEC-002  GATE-001 approval recording by delegated sub-consultant
SPEC-003  Claude second-opinion readiness review
SPEC-004  Planning/spec remediation loop if Claude finds gaps
SPEC-005  Developer-owned Phase 2 execution with wave DEV-REPORTs + primary consolidated TK010
SPEC-006  GATE-002 verification, integrity audit, and final disposition
```

## VI. NON-INTERRUPTION / CONTROL RULES

- The main consultant does not directly execute consultant-owned or developer-owned artifact work during the orchestration run.
- Do not interrupt active developer, reviewer, or delegated sub-consultant workers unless a tool failure blocks progress.
- Do not request client input during a running worker cycle unless the issue changes scope, authority, or gate semantics.
- Re-enter only at phase boundaries: worker completion, reviewer verdict, delegated sub-consultant closure signal, Claude second-opinion result, or explicit client decision point.
- Close workers after their assigned phase completes to avoid stale context carry-over.
- Preserve disjoint write scopes for parallel developer workers.

## VII. TARGET ARTIFACTS / CONTROL SURFACES

| # | Surface | Role Owner | Notes |
|:--|:--|:--|:--|
| 1 | `proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` | Delegated LLM_Consultant | Must reflect external review linkage and final `GATE-001` decision |
| 2 | `implementation_T104-PH001-ST008-AC001.6_gate-001-package-remediation.md` | LLM_Consultant | Governs SPEC-001 execution |
| 3 | `plan_T104-PH001-ST008-AC001.6.md` | LLM_Consultant | Must be implementation-ready before commissioning Phase 2 |
| 4 | Downstream implementation specifications | LLM_Consultant | Must be normalized before Phase 2 developer work |
| 5 | Wave DEV-REPORT artifact(s) + primary consolidated `TK010` | LLM_Developer | Produced only for developer-owned implementation work |
| 6 | `GATE-002` verification artifact | LLM_Reviewer | Independent quality / compliance signal |
| 7 | `GATE-002` gate-disposition proposal | Delegated LLM_Consultant | Final consultant-owned package before presentation |

## VIII. REFERENCES

| Document | Path |
|:--|:--|
| Governing plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| GATE-001 proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` |
| External review | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6-GATE-001_external-review.md` |
| Downstream-readiness substitute disposition | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/analysis/analysis_T104-PH001-ST008-AC001.6_downstream-readiness-second-opinion.md` |
| Package-remediation specification | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_gate-001-package-remediation.md` |
| DEV-REPORT guideline | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` |
| VERIFICATION guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Claude Code skill | `.agents/skills/claude-code/SKILL.md` |
| T103 communication | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/communication/comm_T104-PH001-ST008-AC001.6_claude-code-skill-external-review-execution-reliability.md` |

## IX. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.3.0 | 2026-03-22 | Amendment | Reconciled the actual `SPEC-003` / `SPEC-004` execution path with repo reality: Claude direct authoring failed, the consultant-authored downstream-readiness analysis was accepted as the explicit substitute disposition, no blocking planning/specification gap was skipped, and the downstream work/`GATE-002` package remained valid. |
| v1.2.1 | 2026-03-22 | Amendment | Corrected the Claude second-opinion command shape to a write-capable non-print invocation (`permission-mode default`) so the step matches the delegated direct-authoring model for the repo-tracked `external_review` analysis artifact. |
| v1.1.0 | 2026-03-22 | Amendment | Refined the orchestration contract per QA: main consultant is orchestration-only; delegated sub-consultant executes consultant-owned artifact work; `GATE-001` approval recording no longer requires a second client checkpoint; developer execution now uses wave DEV-REPORTs plus a primary consolidated `TK010`; future DEV-REPORT package taxonomy is explicitly flagged as a governance remediation candidate. |
| v1.0.0 | 2026-03-22 | Initial | Consultant-owned high-level orchestration plan for AC001.6 from `GATE-001` package remediation through `GATE-002` disposition. Encodes the hybrid recycle model: reviewer-local loops for bounded consultant-owned remediation, consultant-mediated loops for main developer-owned Phase 2 implementation. |
