---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000'
task_id: 'T103-PH000-ST000 (stream-level multi-activity registration)'
version: '1.0.0'
date: '2026-03-25'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md'
execution_audience: 'consultant'
purpose: 'Exact-content task specification for registering AC000.2 downstream tasks, creating the AC000.3 sub-activity plan, registering AC002, and updating all parent governance surfaces to reflect the 2026-03-25 consultation decisions.'
---

# IMPLEMENTATION (Task Specification): AC000.2 Downstream Registration, AC000.3 Plan Creation, AC002 Registration, and Parent Governance Updates

## I. PURPOSE & AUTHORITY

- **Purpose**: Provide exact file-level content for creating and amending the plan artifacts discussed in the 2026-03-25 consultation session. This artifact specifies the precise content of every new or amended file so the executing assistant can reproduce the outcome without interpretation.
- **Authority chain**: Client consultation decisions (2026-03-25) -> This artifact specifies exact content -> Executing assistant creates/amends files exactly as specified -> Consultant reviews the result.
- **Audience**: Executing assistant (consultant-orchestrated execution). The assistant MUST create or amend files using the exact content specified in each SPEC item. Do NOT summarize, paraphrase, or interpret the content — reproduce it verbatim.
- This artifact does **not** hold a GDR. Gate decisions are recorded in proposal artifacts only.

**Locked decisions driving this specification** (from 2026-03-25 consultation):

| Decision | Source |
|:--|:--|
| AC000.2 Gate-001 is APPROVED with condition that downstream tasks are registered | Client decision, this session |
| AC000.3 is a new sub-activity under AC000 for defect remediation + optimization assessment | Client decision, this session |
| AC000.3 prioritizes comprehensive analysis (TK001) against `claude --help` and `code.claude.com` docs | Client decision, this session |
| AC000.3 Gate-001 is a consultation-only gate containing the defect audit + optimization comparative analysis | Client decision, this session |
| AC000.3 optimization scope is an architectural decision requiring comparative options within Gate-001 | Client decision, this session |
| AC002 is a new top-level Activity for the external reviewer invocation skill, depends on AC000.3-GATE-002 | Client decision, this session |
| Allowed external source for CLI verification: all directories under `code.claude.com` | Client decision, this session |

## II. TASK SCOPE

- **Governing plan**: `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md`
- **Trigger**: Multiple client decisions in the 2026-03-25 consultation session requiring coordinated plan amendments across AC000.2, AC000.3, AC002, and parent governance surfaces.
- **Deliverable contract**: Amended and new plan artifacts as enumerated in the target files table below.

**Target files (executive write set)**:

| # | File | Change Class | Action |
|:--|:--|:--|:--|
| F1 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/proposal/proposal_T103-PH000-ST000-AC000.2_gate-001_release-readiness-and-supervised-monitoring-commissioning.md` | Amend | Record client APPROVE in GDR |
| F2 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/plan_T103-PH000-ST000-AC000.2.md` | Amend | Register downstream TK004-GATE-002, record GATE-001 as completed |
| F3 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md` | New | Full AC000.3 activity plan |
| F4 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` | Amend | Add AC000.3 contract stub, add AC002 contract stub, update Activity Register |
| F5 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` | Amend | Register AC000.3 as a new sub-activity |
| F6 | `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md` | Amend | Refresh Activity Snapshot Index As-Of date, add AC002 |
| F7 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/notes_T103-PH000-ST000.md` | Amend | Add AC000.3 activity row (JIT: row added now, notes file path populated when SES001 is created in the dedicated AC000.3-TK001 session) |

**Out of scope**:
- AC000.3-TK001 analysis artifact (dedicated session)
- AC000.3-TK002 comparative analysis artifact (dedicated session)
- AC002 detailed activity plan (dedicated session after AC000.3 gates)
- Any `.agents/skills/claude-code/**` file changes
- Any session notes files (JIT rule: created when activities transition to `in_progress`)

## III. SPECIFICATION ITEMS

### SPEC-001 — Record AC000.2 Gate-001 Client APPROVE Decision (F1)

| Field | Detail |
|:--|:--|
| Requirement Source | Client decision, 2026-03-25 consultation |
| Output | Amended `F1` |
| Acceptance Criteria | GDR shows `Client Decision: APPROVE`, `Gate Status After Decision: completed`, `Decision Date: 2026-03-25`, GIR-001 and GIR-002 both show `APPROVE` |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/proposal/proposal_T103-PH000-ST000-AC000.2_gate-001_release-readiness-and-supervised-monitoring-commissioning.md`.

Apply the following targeted edits:

**1. Update the frontmatter version and date:**
```
version: '1.1.0'
date: '2026-03-25'
```

**2. In Section III (Disposition Summary Register), update both GIR rows — change `Client Decision` from `pending` to `APPROVE`:**

Replace:
```
| GIR-001 | Need for a separate release-readiness lane | Whether the client wants a separate governed planning lane for supervised release-readiness and monitoring | (a) Approve the AC000.2 planning-only successor lane | `T103-PH000-ST000-AC000.2-GATE-001` | No | `pending` |
| GIR-002 | Boundary control | Whether the successor lane should stay planning-only until later consultation authorizes execution work | (a) Preserve the planning-only boundary and defer runtime execution | `T103-PH000-ST000-AC000.2-GATE-001` | No | `pending` |
```

With:
```
| GIR-001 | Need for a separate release-readiness lane | Whether the client wants a separate governed planning lane for supervised release-readiness and monitoring | (a) Approve the AC000.2 planning-only successor lane | `T103-PH000-ST000-AC000.2-GATE-001` | No | `APPROVE` |
| GIR-002 | Boundary control | Whether the successor lane should stay planning-only until later consultation authorizes execution work | (a) Preserve the planning-only boundary and defer runtime execution | `T103-PH000-ST000-AC000.2-GATE-001` | No | `APPROVE` |
```

**3. In Section IV (Detailed Disposition Register), update the Client Decision checkboxes for GIR-001:**

Replace:
```
- `[ ] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______`
```

With:
```
- `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______`
```

**4. In Section IV (Detailed Disposition Register), update the Client Decision checkboxes for GIR-002:**

Replace:
```
- `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______`
```

With:
```
- `[x] (a)` / `[ ] (b)` / `[ ] Override: _______`
```

**5. In Section VI (Gate Decision Record), update the GDR table:**

Replace:
```
| Gate ID | `T103-PH000-ST000-AC000.2-GATE-001` |
| Consultant Recommendation | `APPROVE` |
| Client Decision | `pending` |
| Gate Status After Decision | `pending` |
| Conditions (if any) | `-` |
| Decided By | `Client` |
| Decision Date | `—` |
| Decision Reference | `pending` |
```

With:
```
| Gate ID | `T103-PH000-ST000-AC000.2-GATE-001` |
| Consultant Recommendation | `APPROVE` |
| Client Decision | `APPROVE` |
| Gate Status After Decision | `completed` |
| Conditions (if any) | AC000.2 plan must be amended post-gate to register downstream planning tasks (TK004-GATE-002) before execution begins. |
| Decided By | `Client` |
| Decision Date | `2026-03-25` |
| Decision Reference | Current consultation session (2026-03-25) |
```

**6. Update the note below the GDR table:**

Replace:
```
The `Consultant Recommendation` is populated now as the advisory signal for client review. The Gate-001 package is complete and awaits client commissioning of the planning-only successor lane.
```

With:
```
Client decision `APPROVE` recorded on 2026-03-25. Gate-001 is complete. The AC000.2 plan must now be amended with downstream tasks (TK004-GATE-002) per the gate condition before execution begins.
```

**7. Add a changelog entry:**

Append to the changelog table:
```
| v1.1.0 | 2026-03-25 | Decision | Recorded client decision `APPROVE` in the GDR with condition that downstream tasks are registered in the AC000.2 plan amendment. GIR-001 and GIR-002 both approved as recommended. |
```

---

### SPEC-002 — Amend AC000.2 Plan with Downstream Tasks (F2)

| Field | Detail |
|:--|:--|
| Requirement Source | AC000.2 Gate-001 approval condition, 2026-03-25 |
| Output | Amended `F2` |
| Acceptance Criteria | GATE-001 is `completed`, TK004 through GATE-002 are registered as `planned`, plan version bumped |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/plan_T103-PH000-ST000-AC000.2.md`.

Apply the following targeted edits:

**1. Update frontmatter:**
```
version: '2.0.0'
date: '2026-03-25'
```

**2. In Section II Task Register, update GATE-001 row status and action, then append the new downstream rows:**

Replace the GATE-001 row:
```
| GATE-001 | `T103-PH000-ST000-AC000.2-GATE-001` | Gate: Client commissioning of the AC000.2 release-readiness and supervised-monitoring planning lane | `in_progress` | Client | TK003 | Pass/fail | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/proposal/proposal_T103-PH000-ST000-AC000.2_gate-001_release-readiness-and-supervised-monitoring-commissioning.md` | AC000.2 planning package is assembled and awaiting the client commissioning decision in the pending GDR. |
```

With the updated GATE-001 row plus the new downstream rows:
```
| GATE-001 | `T103-PH000-ST000-AC000.2-GATE-001` | Gate: Client commissioning of the AC000.2 release-readiness and supervised-monitoring planning lane | `completed` | Client | TK003 | Pass/fail | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/proposal/proposal_T103-PH000-ST000-AC000.2_gate-001_release-readiness-and-supervised-monitoring-commissioning.md` | Client `APPROVE` decision recorded on 2026-03-25; downstream TK004-GATE-002 are now commissioned. |
| TK004 | `T103-PH000-ST000-AC000.2-TK004` | Resolve SPEC-003: parent governance surface updates | `planned` | LLM_Developer | GATE-001 | Parent governance surfaces | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/implementation/implementation_T103-PH000-ST000-AC000.2_release-readiness-and-supervised-monitoring-commissioning.md` | — |
| TK005 | `T103-PH000-ST000-AC000.2-TK005` | Define the release-readiness execution scope | `planned` | LLM_Consultant | TK004, AC000.3-GATE-001 | `analysis/` | — | — |
| TK006 | `T103-PH000-ST000-AC000.2-TK006` | Author the release-readiness execution plan | `planned` | LLM_Consultant | TK005 | `implementation/` | — | — |
| TK007 | `T103-PH000-ST000-AC000.2-TK007` | Produce Gate-002 consultation proposal | `planned` | LLM_Consultant | TK006 | `proposal/` | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` | — |
| GATE-002 | `T103-PH000-ST000-AC000.2-GATE-002` | Gate: Client acceptance of the release-readiness plan | `planned` | Client | TK007 | Pass/fail | — | — |
```

**3. In Section III (Tasks Detailed), after the existing GATE-001 detailed section, append the following new task detail sections:**

```markdown
### Task TK004: Resolve SPEC-003 — Parent Governance Surface Updates

**Task ID**: `T103-PH000-ST000-AC000.2-TK004`

**Purpose**: Execute the deferred SPEC-003 parent governance surface updates that were part of the AC000.2 commissioning implementation specification but remained `open` after the Gate-001 planning package was assembled.

**Deliverable**:
- Updated `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md`
- Updated `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md`
- Updated `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md`
- Updated `prompt/artifacts/tasks/T103/workspace/PH000/ST000/notes_T103-PH000-ST000.md`

**Scope**:
- In scope:
  - Update parent AC000 plan to reflect AC000.1 completion and AC000.2 successor lane
  - Update ST000 stream plan to reflect AC000.2 as active successor planning sub-activity
  - Refresh phase snapshot date
  - Update ST000 notes register to index AC000.2 sessions
- Out of scope:
  - `.agents/skills/claude-code/**` changes
  - AC000.3 or AC002 registration (handled by separate stream-level implementation)

**Inputs Required**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/implementation/implementation_T103-PH000-ST000-AC000.2_release-readiness-and-supervised-monitoring-commissioning.md` — SPEC-003 detail

**Steps**:
1. Execute SPEC-003 exactly as specified in the AC000.2 commissioning implementation artifact.
2. Verify that parent surfaces show AC000.1 completed, AC000.2 registered, and AC000 still in progress.

**Success Criteria**:
- [ ] SPEC-003 surfaces are updated per the implementation specification
- [ ] Parent AC000 plan shows AC000.2 as the successor lane

---

### Task TK005: Define the Release-Readiness Execution Scope

**Task ID**: `T103-PH000-ST000-AC000.2-TK005`

**Purpose**: Produce a consultant-owned analysis that defines the scope of the release-readiness execution work — which Manual Codex Matrix scenarios, which Reliability Incident Matrix scenarios, which Direct CLI Live Matrix cases, and which orchestration-pattern documentation must be completed before the Claude Code skill can be treated as production-ready.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/analysis/analysis_T103-PH000-ST000-AC000.2_release-readiness-execution-scope.md`

**Scope**:
- In scope:
  - Review the testing guide's Manual Codex Matrix, Reliability Incident Matrix, Direct CLI Live Matrix, and Release Gate criteria
  - Cross-reference AC000.3 analysis output (when available) to determine which scenarios are affected by the corrected skill baseline
  - Produce a prioritized execution scope for later commissioning
- Out of scope:
  - Executing the matrices
  - Modifying `.agents/skills/claude-code/**`

**Inputs Required**:
- `.agents/skills/claude-code/references/claude-code-testing.md` — current testing guide
- AC000.3 Gate-001 analysis output (when available) — corrected baseline information

**Steps**:
1. Review the testing guide's stated release gate criteria.
2. Map each criteria to a prioritized execution scope item.
3. Publish the scoped analysis for TK006 consumption.

**Success Criteria**:
- [ ] Release-readiness scope analysis exists at the canonical path
- [ ] The analysis enumerates specific matrix scenarios and prioritizes them

---

### Task TK006: Author the Release-Readiness Execution Plan

**Task ID**: `T103-PH000-ST000-AC000.2-TK006`

**Purpose**: Author a detailed execution plan for the release-readiness work that can be later commissioned under a separate governed consultation.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/implementation/implementation_T103-PH000-ST000-AC000.2_release-readiness-execution-plan.md`

**Scope**:
- In scope:
  - Translate the TK005 scope analysis into an actionable execution plan
  - Define the task sequence, owners, and acceptance criteria for later commissioning
- Out of scope:
  - Executing the plan
  - Creating a new sub-activity (that is a downstream decision after Gate-002)

**Inputs Required**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/analysis/analysis_T103-PH000-ST000-AC000.2_release-readiness-execution-scope.md` — scoped analysis

**Steps**:
1. Translate the prioritized scope items into concrete execution tasks.
2. Publish the execution plan for Gate-002 packaging.

**Success Criteria**:
- [ ] Execution plan exists at the canonical path
- [ ] The plan is actionable and references specific matrix scenarios

---

### Task TK007: Produce Gate-002 Consultation Proposal

**Task ID**: `T103-PH000-ST000-AC000.2-TK007`

**Purpose**: Package the completed release-readiness planning work for client acceptance at Gate-002.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/proposal/proposal_T103-PH000-ST000-AC000.2_gate-002_release-readiness-plan-acceptance.md`

**Scope**:
- In scope:
  - Present the scoped analysis and execution plan as a consultation-only gate package
  - Populate a pending GDR for client commissioning of the execution work
- Out of scope:
  - Implementation-backed evidence (this is a consultation-only gate)

**Inputs Required**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/analysis/analysis_T103-PH000-ST000-AC000.2_release-readiness-execution-scope.md`
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/implementation/implementation_T103-PH000-ST000-AC000.2_release-readiness-execution-plan.md`

**Steps**:
1. Author the consultation-only gate-disposition proposal for AC000.2 Gate-002.
2. Populate the GDR in pending state.

**Success Criteria**:
- [ ] Gate-002 proposal exists with a pending GDR

---

### GATE-002: Client Acceptance of the Release-Readiness Plan

**Gate ID**: `T103-PH000-ST000-AC000.2-GATE-002`

**Entry Criteria**:
- TK004 through TK007 are completed
- The release-readiness scope analysis exists
- The release-readiness execution plan exists
- The Gate-002 proposal exists with a populated pending GDR

**Reviewer**: Client

**Exit Criteria**:
- Client records a decision in the Gate-002 proposal GDR
- If Gate-002 is approved, the release-readiness execution work can be commissioned as a future governed sub-activity or activity

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/proposal/proposal_T103-PH000-ST000-AC000.2_gate-002_release-readiness-plan-acceptance.md`
```

**4. In Section IV (Links Register), append:**
```
| Analysis | AC000.2 release-readiness execution scope | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/analysis/analysis_T103-PH000-ST000-AC000.2_release-readiness-execution-scope.md` |
| Implementation | AC000.2 release-readiness execution plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/implementation/implementation_T103-PH000-ST000-AC000.2_release-readiness-execution-plan.md` |
| Proposal | AC000.2 Gate-002 release-readiness plan acceptance | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/proposal/proposal_T103-PH000-ST000-AC000.2_gate-002_release-readiness-plan-acceptance.md` |
```

**5. Add a changelog entry:**

Append to the changelog table:
```
| v2.0.0 | 2026-03-25 | Amendment | Recorded Gate-001 as `completed` after client APPROVE decision on 2026-03-25, registered downstream tasks TK004-GATE-002 for the post-Gate-001 release-readiness planning lane, and added the detailed task sections and links for the new downstream work. |
```

---

### SPEC-003 — Create AC000.3 Activity Plan (F3)

| Field | Detail |
|:--|:--|
| Requirement Source | Client decision, 2026-03-25 consultation |
| Output | New `F3` |
| Acceptance Criteria | AC000.3 plan exists with Phase A (TK001-GATE-001 consultation) and Phase B (TK004-GATE-002 implementation-backed) task registers, all tasks at `planned` status |
| Status | `open` |

#### Implementation Detail

Create a new file at `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md` with the following exact content:

```markdown
---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC000.3'
version: '1.0.0'
date: '2026-03-25'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
parent_plan: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md'
---

# PLAN: T103 (ADRSS) - Phase 0 / Stream `T103-PH000-ST000` / Sub-Activity `AC000.3`: Claude Code Skill Defect Remediation and Optimization Assessment

## I. EXECUTIVE SUMMARY

**Purpose**: Conduct a comprehensive audit of the Claude Code skill surfaces against the authoritative CLI documentation, identify and remediate all defects, and present architectural optimization options for client decision — all within a two-phase gated workflow.

**Non-goal**: This sub-activity does not execute the Manual Codex Matrix, Reliability Incident Matrix, or any runtime monitoring work. It does not create the external reviewer invocation skill (AC002). It does not reopen upstream `GATE-003`.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `T103-PH000-ST000-AC000.3`
**Objective**: Audit the five Claude Code skill surface files against the live installed CLI (`claude --help`, v2.1.83+) and the canonical external documentation (`code.claude.com`), catalogue all defects with severity classification, present architectural optimization options as a comparative analysis, obtain client approval at Gate-001, then execute the approved remediation and optimization scope through an implementation-backed Gate-002.
**Execution Mode**: `GATED`
**Depends On**: `T103-PH000-ST000-AC000.1-GATE-002`

**Context**:
- `.agents/skills/claude-code/SKILL.md`
- `.agents/skills/claude-code/references/claude-code-cli.md`
- `.agents/skills/claude-code/references/claude-code-testing.md`
- `.agents/skills/claude-code/scripts/validate_claude_code_skill.py`
- `.agents/skills/claude-code/scripts/test_validate_claude_code_skill.py`
- `.claude/skills/codex/SKILL.md`
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/analysis/analysis_T103-PH000-ST000-AC000.1_claude-code-skill-post-gate-003-runtime-observations.md`
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/dev-report/dev-report_T103-PH000-ST000-AC000.1_runtime-monitoring-and-testing-remediation_2026-03-24.md`
- `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
- `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`
- `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md`
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md`

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK001 | `T103-PH000-ST000-AC000.3-TK001` | Comprehensive Claude Code skill surface audit | `planned` | LLM_Consultant | `T103-PH000-ST000-AC000.1-GATE-002` | `analysis/` | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` | — |
| TK002 | `T103-PH000-ST000-AC000.3-TK002` | Skill optimization comparative analysis | `planned` | LLM_Consultant | TK001 | `analysis/` | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` | — |
| TK003 | `T103-PH000-ST000-AC000.3-TK003` | Produce Gate-001 consultation proposal | `planned` | LLM_Consultant | TK002 | `proposal/` | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` | — |
| GATE-001 | `T103-PH000-ST000-AC000.3-GATE-001` | Gate: Client approval of the defect remediation + optimization scope | `planned` | Client | TK003 | Pass/fail | — | — |
| TK004 | `T103-PH000-ST000-AC000.3-TK004` | Publish remediation + optimization implementation specification | `planned` | LLM_Consultant | GATE-001 | `implementation/` | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` | — |
| TK005 | `T103-PH000-ST000-AC000.3-TK005` | Execute the approved remediation + optimization | `planned` | LLM_Developer | TK004 | `.agents/skills/claude-code/` surfaces | — | — |
| TK006 | `T103-PH000-ST000-AC000.3-TK006` | Produce dev-report for Gate-002 | `planned` | LLM_Developer | TK005 | `dev-report/` | `prompt/templates/consultant/workspace/guideline_workspace_dev-report.md` | — |
| TK007 | `T103-PH000-ST000-AC000.3-TK007` | Produce Gate-002 verification | `planned` | LLM_Reviewer | TK006 | `verification/` | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` | — |
| TK008 | `T103-PH000-ST000-AC000.3-TK008` | Produce Gate-002 gate-disposition proposal | `planned` | LLM_Consultant | TK007 | `proposal/` | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` | — |
| GATE-002 | `T103-PH000-ST000-AC000.3-GATE-002` | Gate: Client acceptance of the remediated and optimized skill | `planned` | Client | TK008 | Pass/fail | — | — |

---

## III. TASKS (DETAILED)

### Task TK001: Comprehensive Claude Code Skill Surface Audit

**Task ID**: `T103-PH000-ST000-AC000.3-TK001`

**Purpose**: Produce a consultant-owned analysis that audits every CLI flag, command pattern, behavioral claim, and validator assumption in the five Claude Code skill surface files against the authoritative CLI documentation. This is the primary defect-discovery task that seeds all downstream remediation work.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/analysis/analysis_T103-PH000-ST000-AC000.3_claude-code-skill-surface-audit.md`

**Scope**:
- In scope:
  - Audit `.agents/skills/claude-code/SKILL.md` against `claude --help` and `code.claude.com` documentation
  - Audit `.agents/skills/claude-code/references/claude-code-cli.md` against the same authoritative sources
  - Audit `.agents/skills/claude-code/references/claude-code-testing.md` for references to non-existent flags or features
  - Audit `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` for structural false-positives (e.g., `--version` masking invalid flags, "docs agree with docs" checks)
  - Audit `.agents/skills/claude-code/scripts/test_validate_claude_code_skill.py` for assertions covering non-existent features
  - Catalogue each defect with: severity (`blocking`, `degrading`, `cosmetic`), affected file(s), line reference(s), description, and remediation recommendation
  - Identify any features present in `claude --help` or `code.claude.com` that the skill does NOT document but SHOULD
- Out of scope:
  - Fixing any defects (that is TK005)
  - Optimization or restructuring (that is TK002)
  - Reopening `GATE-003`
  - Executing manual matrices or live runtime tests

**Inputs Required**:
- `.agents/skills/claude-code/SKILL.md` — primary skill contract under audit
- `.agents/skills/claude-code/references/claude-code-cli.md` — CLI reference under audit
- `.agents/skills/claude-code/references/claude-code-testing.md` — testing guide under audit
- `.agents/skills/claude-code/scripts/validate_claude_code_skill.py` — validator under audit
- `.agents/skills/claude-code/scripts/test_validate_claude_code_skill.py` — pytest coverage under audit
- `claude --help` output from the installed CLI (run live during analysis)
- `https://code.claude.com/docs/en/cli-reference` and related pages under `code.claude.com` (allowed external source)
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/analysis/analysis_T103-PH000-ST000-AC000.1_claude-code-skill-post-gate-003-runtime-observations.md` — prior runtime observations (GAP-001 through GAP-005) to cross-reference

**Steps**:
1. Run `claude --help` and capture the complete flag surface of the installed CLI.
2. Fetch the canonical documentation from `code.claude.com/docs/en/cli-reference` and any related sub-pages.
3. Read each of the five target skill surface files end-to-end.
4. For every CLI flag, command pattern, and behavioral claim in the skill surfaces, verify it against `claude --help` and the canonical documentation.
5. For every validator check and parser test case, verify whether it tests actual CLI behavior or merely internal document consistency.
6. Catalogue each defect in a structured gap/defect register with severity classification.
7. Cross-reference the AC000.1 runtime observations (GAP-001 through GAP-005) to determine which were truly resolved and which persist.
8. Identify any new CLI features or flags that the skill should document but currently does not.
9. Publish the analysis artifact per `guideline_workspace_analysis.md`.

**Success Criteria**:
- [ ] Analysis artifact exists at the canonical path with `analysis_type: assessment`
- [ ] Every CLI flag in the five skill surface files has been verified against `claude --help`
- [ ] Every CLI flag in the five skill surface files has been cross-referenced against `code.claude.com` documentation
- [ ] Defect register includes severity, affected files, line references, and remediation recommendations
- [ ] Validator structural issues (false-positive patterns) are identified and catalogued
- [ ] AC000.1 GAP-001 through GAP-005 resolution status is re-assessed against the live CLI

---

### Task TK002: Skill Optimization Comparative Analysis

**Task ID**: `T103-PH000-ST000-AC000.3-TK002`

**Purpose**: Produce a comparative analysis evaluating architectural options for optimizing the Claude Code skill's size and structure, using the battle-tested Codex skill as a reference point. This is an architectural decision for client approval within Gate-001.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/analysis/analysis_T103-PH000-ST000-AC000.3_skill-optimization-comparative-analysis.md`

**Scope**:
- In scope:
  - Compare `.claude/skills/codex/SKILL.md` (~65 lines, battle-tested) against `.agents/skills/claude-code/SKILL.md` (~260 lines)
  - Identify which sections in the Claude Code skill are essential safety properties vs governance verbosity
  - Present multiple architectural options with tradeoffs against weighted criteria
  - Provide consultant recommendations while preserving client decision authority
- Out of scope:
  - Implementing any optimization (that is TK005)
  - Modifying the Codex skill itself

**Inputs Required**:
- `.claude/skills/codex/SKILL.md` — reference skill (concise, battle-tested)
- `.agents/skills/claude-code/SKILL.md` — skill under evaluation
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/analysis/analysis_T103-PH000-ST000-AC000.3_claude-code-skill-surface-audit.md` — TK001 defect audit (determines what must change regardless of optimization)

**Steps**:
1. Map both skills to a common structural framework (Workflow, Quick Reference, Following Up, Critical Evaluation, Error Handling, Guardrails).
2. Identify sections in the Claude Code skill that have no equivalent in the Codex skill and evaluate their operational necessity.
3. Evaluate the essential safety properties (Single-Flight Rule, Runtime Outcome Classification, Provenance basics) and determine whether they can be compressed vs moved to a reference doc.
4. Present architectural options with weighted evaluation criteria (context cost, safety-property retention, operational clarity, maintainability).
5. Publish the comparative analysis per `guideline_workspace_analysis.md` with `analysis_type: comparative_analysis`.

**Success Criteria**:
- [ ] Comparative analysis exists at the canonical path with `analysis_type: comparative_analysis`
- [ ] At least three architectural options are presented with tradeoffs
- [ ] Evaluation criteria are weighted and each option is scored
- [ ] Consultant recommendation is included but does not pre-determine the client decision

---

### Task TK003: Produce Gate-001 Consultation Proposal

**Task ID**: `T103-PH000-ST000-AC000.3-TK003`

**Purpose**: Package the TK001 defect audit and TK002 optimization comparative analysis into a consultation-only gate package for client approval of the remediation and optimization scope.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/proposal/proposal_T103-PH000-ST000-AC000.3_gate-001_defect-remediation-and-optimization-scope.md`

**Scope**:
- In scope:
  - Present the defect audit findings as GIR items requiring client disposition
  - Present the optimization architectural options as a GIR item requiring client decision
  - Populate a pending GDR for client review
- Out of scope:
  - Implementation-backed evidence (this is a consultation-only gate)
  - Verification artifact (consultation-only gates omit verification)

**Inputs Required**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/analysis/analysis_T103-PH000-ST000-AC000.3_claude-code-skill-surface-audit.md` — defect audit
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/analysis/analysis_T103-PH000-ST000-AC000.3_skill-optimization-comparative-analysis.md` — optimization options

**Steps**:
1. Author the consultation-only gate-disposition proposal per `guideline_workspace_proposal.md`.
2. Present each blocking/degrading defect cluster as a GIR item.
3. Present the optimization scope as a separate GIR item with the comparative analysis options.
4. Populate the GDR in pending state.

**Success Criteria**:
- [ ] Gate-001 proposal exists at the canonical path with a pending GDR
- [ ] Each defect cluster has a GIR with recommended remediation option
- [ ] Optimization scope has a GIR with architectural options from TK002

---

### GATE-001: Client Approval of the Defect Remediation and Optimization Scope

**Gate ID**: `T103-PH000-ST000-AC000.3-GATE-001`

**Entry Criteria**:
- TK001 through TK003 are completed
- The skill surface audit analysis exists
- The optimization comparative analysis exists
- The Gate-001 proposal exists with a populated pending GDR

**Reviewer**: Client

**Exit Criteria**:
- Client records a decision in the Gate-001 proposal GDR
- If Gate-001 is approved, TK004 through GATE-002 are commissioned as the implementation-backed remediation lane
- The approved GIR resolutions define the exact remediation and optimization scope for TK004

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/proposal/proposal_T103-PH000-ST000-AC000.3_gate-001_defect-remediation-and-optimization-scope.md`

---

### Task TK004: Publish Remediation + Optimization Implementation Specification

**Task ID**: `T103-PH000-ST000-AC000.3-TK004`

**Purpose**: Translate the Gate-001 approved defect remediation and optimization scope into a detailed developer-facing implementation specification.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/implementation/implementation_T103-PH000-ST000-AC000.3_defect-remediation-and-optimization.md`

**Scope**:
- In scope:
  - Encode each approved defect fix as a SPEC item with exact file targets and acceptance criteria
  - Encode the approved optimization scope as SPEC items
  - Define the validator correction strategy (remove false-positive patterns, add negative regression guards)
- Out of scope:
  - Defects or optimization options not approved at Gate-001

**Inputs Required**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/proposal/proposal_T103-PH000-ST000-AC000.3_gate-001_defect-remediation-and-optimization-scope.md` — approved GIR resolutions
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/analysis/analysis_T103-PH000-ST000-AC000.3_claude-code-skill-surface-audit.md` — defect detail

**Steps**:
1. Translate each approved GIR resolution into SPEC items per `guideline_workspace_implementation.md`.
2. Define the execution sequence and file-level mutation set.
3. Include negative regression test requirements for each defect category.

**Success Criteria**:
- [ ] Implementation specification exists at the canonical path
- [ ] Every approved defect fix has a SPEC item with exact file targets
- [ ] Validator correction strategy includes negative regression guards

---

### Task TK005: Execute the Approved Remediation + Optimization

**Task ID**: `T103-PH000-ST000-AC000.3-TK005`

**Purpose**: Execute the developer-owned remediation and optimization work against the five Claude Code skill surface files per the TK004 implementation specification.

**Deliverable**:
- Updated `.agents/skills/claude-code/SKILL.md`
- Updated `.agents/skills/claude-code/references/claude-code-cli.md`
- Updated `.agents/skills/claude-code/references/claude-code-testing.md`
- Updated `.agents/skills/claude-code/scripts/validate_claude_code_skill.py`
- Updated `.agents/skills/claude-code/scripts/test_validate_claude_code_skill.py`

**Scope**:
- In scope:
  - Remove or correct all defects identified in TK001 and approved at Gate-001
  - Apply the approved optimization scope from TK002/Gate-001
  - Fix validator structural issues (remove `--version` masking, add live CLI verification, add negative regression guards)
  - Update pytest coverage to match the corrected validator
- Out of scope:
  - Defects or optimization options not approved at Gate-001
  - Unrelated workspace governance files

**Inputs Required**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/implementation/implementation_T103-PH000-ST000-AC000.3_defect-remediation-and-optimization.md` — execution authority

**Steps**:
1. Execute the implementation specification exactly as authored in TK004.
2. Run the corrected validator with `--json` and `--live-smoke` to verify zero false-positives.
3. Run the corrected pytest suite to verify test coverage.

**Success Criteria**:
- [ ] All SPEC items from TK004 are resolved
- [ ] Corrected validator produces `FAIL=0` against the live CLI without false-positive masking
- [ ] Corrected pytest passes with updated assertions

---

### Task TK006: Produce Dev-Report for Gate-002

**Task ID**: `T103-PH000-ST000-AC000.3-TK006`

**Purpose**: Capture developer execution evidence for the remediation and optimization work.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/dev-report/dev-report_T103-PH000-ST000-AC000.3_defect-remediation-and-optimization_YYYY-MM-DD.md`

**Inputs Required**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/implementation/implementation_T103-PH000-ST000-AC000.3_defect-remediation-and-optimization.md` — execution authority

**Steps**:
1. Author the dev-report per `guideline_workspace_dev-report.md` after TK005 is complete.
2. Include concrete command output for validator and pytest runs.
3. Map deliverables back to SPEC item IDs in the traceability matrix.

**Success Criteria**:
- [ ] Dev-report exists at the canonical path with concrete validation evidence
- [ ] Traceability matrix maps to TK004 SPEC items

---

### Task TK007: Produce Gate-002 Verification

**Task ID**: `T103-PH000-ST000-AC000.3-TK007`

**Purpose**: Independently verify the remediation and optimization execution slice.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/verification/verification_T103-PH000-ST000-AC000.3_gate-002_defect-remediation-and-optimization.md`

**Inputs Required**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/implementation/implementation_T103-PH000-ST000-AC000.3_defect-remediation-and-optimization.md` — execution authority
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/dev-report/dev-report_T103-PH000-ST000-AC000.3_defect-remediation-and-optimization_YYYY-MM-DD.md` — developer evidence

**Steps**:
1. Perform evidence-first verification per `guideline_workspace_verification.md`.
2. Independently re-run the corrected validator and pytest.
3. Verify that each TK001 defect is actually resolved in the corrected files.
4. Record the reviewer verdict.

**Success Criteria**:
- [ ] Verification artifact exists with a reviewer verdict
- [ ] Independent reruns corroborate the developer evidence
- [ ] Each defect from TK001 is verified as resolved

---

### Task TK008: Produce Gate-002 Gate-Disposition Proposal

**Task ID**: `T103-PH000-ST000-AC000.3-TK008`

**Purpose**: Package the remediation and optimization execution evidence for client acceptance.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/proposal/proposal_T103-PH000-ST000-AC000.3_gate-002_defect-remediation-and-optimization-acceptance.md`

**Inputs Required**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/verification/verification_T103-PH000-ST000-AC000.3_gate-002_defect-remediation-and-optimization.md` — reviewer verdict
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/implementation/implementation_T103-PH000-ST000-AC000.3_defect-remediation-and-optimization.md` — execution authority

**Steps**:
1. Author the gate-disposition proposal per `guideline_workspace_proposal.md`.
2. Populate the GDR in pending state.

**Success Criteria**:
- [ ] Gate-002 proposal exists with a pending GDR

---

### GATE-002: Client Acceptance of the Remediated and Optimized Skill

**Gate ID**: `T103-PH000-ST000-AC000.3-GATE-002`

**Entry Criteria**:
- TK004 through TK008 are completed
- Dev-report exists with concrete validation evidence
- Verification artifact exists with a reviewer verdict
- Gate-002 proposal exists with a populated pending GDR

**Reviewer**: Client

**Exit Criteria**:
- Client records a decision in the Gate-002 proposal GDR
- If Gate-002 is approved, AC000.3 moves to terminal closeout and the corrected skill baseline is available for AC002 (External Reviewer Invocation Skill)

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/proposal/proposal_T103-PH000-ST000-AC000.3_gate-002_defect-remediation-and-optimization-acceptance.md`

---

## IV. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Plan (this file) | AC000.3 sub-activity plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md` |
| Plan | AC000 parent activity plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` |
| Plan | AC000.1 sub-activity plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/plan_T103-PH000-ST000-AC000.1.md` |
| Plan | AC000.2 sub-activity plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/plan_T103-PH000-ST000-AC000.2.md` |
| Plan | ST000 stream plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| Analysis | AC000.1 runtime observations | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.1/analysis/analysis_T103-PH000-ST000-AC000.1_claude-code-skill-post-gate-003-runtime-observations.md` |
| Skill (under audit) | Claude Code skill contract | `.agents/skills/claude-code/SKILL.md` |
| Skill (reference) | Codex skill contract | `.claude/skills/codex/SKILL.md` |

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-25 | Initial | Created the AC000.3 sub-activity plan for Claude Code skill defect remediation and optimization assessment, with a two-phase gated workflow: Phase A (consultation-only Gate-001 for defect audit + optimization options) and Phase B (implementation-backed Gate-002 for remediation execution). |
```

---

### SPEC-004 — Amend Stream Plan with AC000.3 and AC002 Contract Stubs (F4)

| Field | Detail |
|:--|:--|
| Requirement Source | Client decision, 2026-03-25 consultation |
| Output | Amended `F4` |
| Acceptance Criteria | Activity Register includes AC000.3 (sub) and AC002 rows; AC000.3 contract stub exists under AC000; AC002 contract stub exists as a new Activity section; version bumped |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md`.

Apply the following targeted edits:

**1. Update frontmatter:**
```
version: '1.6.0'
date: '2026-03-25'
```

**2. Update the Executive Summary Purpose to include AC000.3 and AC002:**

Replace:
```
**Purpose**: Create the missing stream-level governance shell for the Claude Code skill remediation slice, link the existing AC000 consultation artifacts into a valid execution chain, close the `AC000.1` monitoring/testing remediation slice cleanly at `GATE-002`, register the `AC000.2` release-readiness successor lane, and package the new AC001 draft orchestration execution specification lane.
```

With:
```
**Purpose**: Create the missing stream-level governance shell for the Claude Code skill remediation slice, link the existing AC000 consultation artifacts into a valid execution chain, close the `AC000.1` monitoring/testing remediation slice cleanly at `GATE-002`, register the `AC000.2` release-readiness successor lane, register `AC000.3` as the defect remediation and optimization assessment lane, register `AC002` as the external reviewer invocation skill activity, and package the new AC001 draft orchestration execution specification lane.
```

**3. In the Activity Register, append a new AC002 row after the AC001 row:**

```
| AC002 | `T103-PH000-ST000-AC002` | External reviewer invocation skill | `planned` | LLM_Consultant | `T103-PH000-ST000-AC000.3-GATE-002` | AC002 activity plan, reviewer-delegation invocation skill, supervised trial evidence, and GATE-001/GATE-002 packages | — |
```

**4. Under the AC000.2 contract stub section (after its Success Criteria), add the AC000.3 contract stub:**

Insert the following after the AC000.2 section and before the `### Activity AC001` section:

```markdown
#### Sub-Activity AC000.3: Claude Code Skill Defect Remediation and Optimization Assessment

**Trigger**: Client-identified live runtime evidence (2026-03-25) confirming that the `-C`/`--cd` flags documented in the skill surfaces do not exist in Claude CLI v2.1.83, combined with structural validator false-positive masking the defect. Broad skill surface audit required against authoritative CLI documentation.

**Purpose**: Conduct a comprehensive audit of all five Claude Code skill surface files against the installed CLI and canonical external documentation, remediate all confirmed defects, and present architectural optimization options for client decision.

**Sub-Activity Plan**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md`

**Success Criteria Checklist (summary)**:
- [ ] TK001 comprehensive audit identifies all CLI surface defects across all 5 target files
- [ ] TK002 comparative analysis presents architectural optimization options with tradeoffs
- [ ] Gate-001 records the client's approved remediation + optimization scope
- [ ] Post-Gate-001 implementation resolves all blocking/degrading defects
- [ ] Corrected validator produces zero false-positives against the live CLI
- [ ] Gate-002 closes with client acceptance of the remediated skill
```

**5. After the AC001 section, add the AC002 contract stub:**

Insert the following after the AC001 section and before `## IV. LINKS REGISTER`:

```markdown
### Activity AC002: External Reviewer Invocation Skill

**Activity ID**: `T103-PH000-ST000-AC002`

**Purpose**: Create a dedicated invocation skill that enables Codex CLI to spawn Claude Code as an external reviewer (LLM_Reviewer) using the base `claude-code` skill, with explicit patterns for session management, artifact authoring, continue/resume workflows, and peer-AI dialogue.

**Deliverable**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC002/plan_T103-PH000-ST000-AC002.md` — detailed AC002 task and gate authority
- New invocation skill (e.g., `.agents/skills/claude-code-reviewer/SKILL.md`)
- Supervised trial evidence from a real Codex-orchestrated review

**Scope**:
- In scope:
  - Design the reviewer-delegation invocation skill
  - Implement the skill on the corrected base skill foundation (post-AC000.3)
  - Supervised trial: Codex uses the new skill for a real external review
- Out of scope:
  - Modifying the base `claude-code` skill (that is AC000.3)
  - Modifying the Codex skill itself

**Activity Plan**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC002/plan_T103-PH000-ST000-AC002.md` (to be created in a dedicated session after AC000.3 gates)

**Inputs Required**:
- Corrected `.agents/skills/claude-code/SKILL.md` (post-AC000.3-GATE-002)
- `.claude/skills/codex/SKILL.md` — reference for Codex-side invocation patterns

**Success Criteria Checklist (summary)**:
- [ ] AC002 activity plan exists and is linked from the stream plan
- [ ] Reviewer invocation skill exists and is validated
- [ ] Supervised trial demonstrates successful Codex-orchestrated Claude Code review
- [ ] `T103-PH000-ST000-AC002-GATE-002` is dispositioned by the client
```

**6. In Section IV (Links Register), append the following rows:**

```
| Plan | AC000.3 sub-activity plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md` |
| Plan | AC002 activity plan (to be created) | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC002/plan_T103-PH000-ST000-AC002.md` |
| Implementation | Stream-level planning registration specification | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/implementation/implementation_T103-PH000-ST000_ac000.2-ac000.3-ac002-planning-registration.md` |
```

**7. Add a changelog entry:**

Append to the changelog table:
```
| v1.6.0 | 2026-03-25 | Amendment | Registered AC000.3 as a new sub-activity under AC000 for defect remediation and optimization assessment, registered AC002 as a new top-level activity for the external reviewer invocation skill, updated the Activity Register and Links Register, and expanded the stream scope to include the 2026-03-25 consultation decisions. |
```

---

### SPEC-005 — Amend AC000 Parent Plan to Register AC000.3 (F5)

| Field | Detail |
|:--|:--|
| Requirement Source | Client decision, 2026-03-25 consultation |
| Output | Amended `F5` |
| Acceptance Criteria | AC000.3 appears in the AC000 plan as a registered sub-activity, version bumped |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md`.

Apply the following targeted edits:

**1. Update frontmatter:**
```
version: '1.7.0'
date: '2026-03-25'
```

**2. Update the Executive Summary Purpose** — append to the existing purpose text:

Add after the current purpose sentence ending with "...supervised release-readiness work.":
```
 It also registers `AC000.3` as the defect remediation and optimization assessment lane after client-identified live CLI defects were confirmed on 2026-03-25.
```

**3. Update the Non-goal** — append:

Add after the current non-goal text:
```
 `AC000.3` remediates confirmed skill defects and presents optimization options but does not execute the external reviewer invocation skill (AC002).
```

**4. In the Task Register table, after the GATE-002 row for AC000.1 (or the last row referencing AC000.2), append a reference row for AC000.3:**

Note: AC000.3 has its own dedicated activity plan, so the parent AC000 plan should only carry a brief reference row, not a full task register. Add this row to the existing register:

```
| AC000.3 | `T103-PH000-ST000-AC000.3` | Claude Code skill defect remediation and optimization assessment | `planned` | LLM_Consultant | `T103-PH000-ST000-AC000.1-GATE-002` | Sub-activity plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md` | — |
```

**5. In Section III (if a section for sub-activities exists), or after the AC000.2 sub-activity section, add:**

```markdown
#### Sub-Activity AC000.3: Claude Code Skill Defect Remediation and Optimization Assessment

**Trigger**: Client-identified live runtime evidence (2026-03-25) confirming `-C`/`--cd` flags do not exist in Claude CLI v2.1.83 and structural validator false-positive masking. Broad skill surface audit required.

**Purpose**: Comprehensive audit of the five Claude Code skill surface files against authoritative CLI documentation, defect remediation, and optimization assessment.

**Sub-Activity Plan**:
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md`

**Success Criteria Checklist (summary)**:
- [ ] Comprehensive defect audit completed (TK001)
- [ ] Optimization comparative analysis completed (TK002)
- [ ] Gate-001 approved with remediation + optimization scope
- [ ] Implementation-backed remediation executed and accepted at Gate-002
```

**6. In the Links Register, append:**
```
| Plan | AC000.3 sub-activity plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md` |
```

**7. Add a changelog entry:**

Append to the changelog table:
```
| v1.7.0 | 2026-03-25 | Amendment | Registered AC000.3 as a new sub-activity for Claude Code skill defect remediation and optimization assessment, triggered by client-identified live CLI defects confirmed on 2026-03-25. |
```

---

### SPEC-006 — Refresh Phase Plan Activity Snapshot (F6)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §III.C — phase plans carry snapshot only |
| Output | Amended `F6` |
| Acceptance Criteria | Activity Snapshot Index As-Of date is `2026-03-25`, AC002 appears in the snapshot, version bumped |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md`.

Apply the following targeted edits:

**1. Update frontmatter:**
```
version: '1.7.0'
date: '2026-03-25'
```

**2. Find the Activity Snapshot Index section** and update the `As-Of` date:

Replace the existing `**Activity Snapshot As-Of**:` line with:
```
**Activity Snapshot As-Of**: 2026-03-25
```

**3. In the Activity Snapshot Index table, append a row for AC002:**

```
| ST000 | AC002 | `T103-PH000-ST000-AC002` | External reviewer invocation skill | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
```

Note: AC000.3 is a sub-activity under AC000 and does not get its own row in the phase snapshot — it is covered by the AC000 row which should remain `in_progress`.

**4. Add a changelog entry:**

Append to the changelog table:
```
| v1.7.0 | 2026-03-25 | Snapshot refresh | Updated Activity Snapshot As-Of to 2026-03-25, added AC002 to the snapshot index, and preserved AC000 as `in_progress` to reflect the active AC000.3 sub-activity. |
```

---

### SPEC-007 — Update Stream Notes Register with AC000.3 Row (F7)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` §5.1 (JIT registration) |
| Output | Amended `F7` |
| Acceptance Criteria | AC000.3 activity row exists in the Activity Notes Register with `planned` status and no notes file path yet (JIT: notes file path populated when SES001 is created in the dedicated session) |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/artifacts/tasks/T103/workspace/PH000/ST000/notes_T103-PH000-ST000.md`.

Apply the following targeted edits:

**1. Update frontmatter:**
```
version: '1.9.0'
date: '2026-03-25'
```

**2. Update the Stream Summary Scope** — append:

Add to the existing Scope text:
```
, and the `AC000.3` defect remediation and optimization assessment lane
```

**3. In Section III (Activity Notes Register), append a new row after the AC001 row:**

```
| AC000.3 | `T103-PH000-ST000-AC000.3` | Claude Code Skill Defect Remediation and Optimization Assessment | `planned` | — |
```

Note: Per JIT rule (§5.1), the Notes File column is `—` because AC000.3 has not yet transitioned to `in_progress`. The notes file path will be populated when AC000.3-TK001 begins execution in its dedicated session.

**4. Add a changelog entry:**

Append to the changelog table:
```
| v1.9.0 | 2026-03-25 | Amendment | Registered AC000.3 activity row in the Activity Notes Register with `planned` status per JIT rule. Notes file path deferred until AC000.3 transitions to `in_progress`. |
```

---

## IV. IMPLEMENTATION SEQUENCE

Execute the SPEC items in the following order:

1. **SPEC-001** (F1) — Record AC000.2 Gate-001 GDR approval first, as it establishes the authority for downstream work.
2. **SPEC-002** (F2) — Amend AC000.2 plan with downstream tasks, which depends on the Gate-001 approval being recorded.
3. **SPEC-003** (F3) — Create AC000.3 activity plan. This is a new file with no dependencies on other SPEC items but should be created before registering it in parent surfaces.
4. **SPEC-005** (F5) — Amend AC000 parent plan to register AC000.3 (depends on F3 existing).
5. **SPEC-004** (F4) — Amend stream plan with AC000.3 and AC002 contract stubs (depends on F3 existing).
6. **SPEC-006** (F6) — Refresh phase plan snapshot (depends on F4 stream plan being updated).
7. **SPEC-007** (F7) — Update notes register (can run in parallel with SPEC-006).

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Stream Plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| AC000.2 Plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/plan_T103-PH000-ST000-AC000.2.md` |
| AC000.2 Gate-001 Proposal | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.2/proposal/proposal_T103-PH000-ST000-AC000.2_gate-001_release-readiness-and-supervised-monitoring-commissioning.md` |
| AC000 Parent Plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` |
| Phase Plan | `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md` |
| Notes Register | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/notes_T103-PH000-ST000.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Activity Plan Template | `prompt/templates/consultant/workspace/template_workspace_plan_activity.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| Codex Skill (reference) | `.claude/skills/codex/SKILL.md` |
| Claude Code Skill (under audit) | `.agents/skills/claude-code/SKILL.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-25 | Initial | Created the stream-level task specification for the 2026-03-25 consultation session deliverables: AC000.2 Gate-001 GDR recording, AC000.2 plan amendment with downstream tasks, AC000.3 activity plan creation, AC002 stream registration, and parent governance surface updates. |
