---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-SES002'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
execution_audience: 'consultant'
purpose: 'Detailed task specification for Phase A scope amendment: AC006 plan v2.0.0 structural rewrite, AC005 dependency reversal, and cross-surface alignment of stream plan, phase plan, roadmap, status ledger, status narrative, session notes, and stream notes register.'
---

# IMPLEMENTATION (Task Specification): Phase A — AC006 Scope Amendment And Cross-Surface Alignment

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the exact implementation detail for the Phase A scope amendment that was agreed in the `P-PH000-ST002-AC006-SES002` consultation session. It covers the AC006 plan structural rewrite (v2.0.0), the AC005 dependency reversal, and all downstream cross-surface alignment needed to keep the plan/status/roadmap/notes hierarchy consistent.
- **Authority chain**: The AC006 activity plan authorizes work → This artifact specifies HOW the scope amendment is executed → Session notes (SES002) record the decision trail and outcomes.
- **Audience**: `LLM_Consultant` (execution_audience: consultant). This specification governs consultant-owned plan amendment and status reconciliation work. No developer execution role is involved.
- This artifact does NOT hold a GDR. Gate decisions (if applicable) are recorded in gate_disposition proposals.

## II. TASK SCOPE

- **Governing plan task**: `P-PH000-ST002-AC006-SES002` (scope amendment session)
- **Trigger**: The SES002 consultation expanded AC006's boundary to include a briefing dashboard feature and reversed AC005's dependency from AC004 to AC006. These structural changes require a coordinated amendment across nine governed surfaces.
- **Deliverable contract**: All nine surfaces listed in SPEC-001 through SPEC-009 are updated consistently, with version bumps, changelog entries, and no inter-surface drift.

## III. SPECIFICATION ITEMS

### SPEC-001 — AC006 Activity Plan Structural Rewrite (v2.0.0)

| Field | Detail |
|:--|:--|
| Requirement Source | SES002 client decisions: (1) expand scope to include briefing dashboard, (2) eliminate standalone TK002 hardening analysis, (3) add briefing-focused comparative analysis task, (4) add briefing-only standards-input proposal task, (5) move implementation specs pre-gate, (6) renumber entire task register, (7) add post-gate execution tasks |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Required end-state posture | Plan version is `2.0.0`. Task register contains TK000 through TK008 plus GATE-001 with clean integer sequencing. Executive summary, scope, context, gate model, and all task contracts reflect the expanded boundary. Dependency graph shows two parallel pre-gate branches converging at TK006. |
| Explicit non-target / do-not-change constraints | Do NOT modify the TK000 readiness assessment (completed). Do NOT modify or create any analysis, proposal, or implementation artifact — only the plan file itself. Do NOT alter the `analysis/analysis_P-PH000-ST002-AC006_readiness-and-gate-001-package-boundary-assessment.md` reference — it remains valid. |
| Validation check | (1) Task register has exactly TK000–TK008 + GATE-001 with no gaps or interstitial numbering. (2) Every task has explicit Depends On, Target, Reference, and Action fields populated. (3) Frontmatter version reads `2.0.0`. (4) Changelog contains a v2.0.0 entry explaining the structural rewrite. |
| Blocking ambiguity rule | If any task's scope boundary is ambiguous relative to the SES002 discussion, stop and escalate to the consultant rather than inferring. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'1.1.0'` → `'2.0.0'`
- `date`: `'2026-03-28'` (retain, same day)

**Executive Summary rewrite:**
Replace the current executive summary with:
```
**Purpose**: Define and execute the expanded AC006 boundary covering two distinct features: (1) session-close skill hardening (prompt-assist-only evolution of `prompt/skills/session-close/SKILL.md` with `snotes_` guidance), and (2) a client-facing briefing dashboard (a filtered active-work view derived from `status_program.yaml` for session-continuity and high-level planning enablement).

**Non-goal**: Do not expand the session-close skill into hooks, scripts, repo-wide automation, or general session management. The briefing dashboard is a prompt-assist-only derived surface, not an automated reporting tool. AC006 remains prompt-assist only unless a later approved scope change says otherwise.
```

**Activity Outline updates:**
- **Objective**: Update to reflect both features.
- **Context list**: Add the following new entries:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC005/plan_P-PH000-ST002-AC005.md` (now depends on AC006)
  - `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` (for standards-input proposal authoring)
  - `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` (for implementation spec authoring)

**Task Register replacement** — replace the entire Task Register table with:

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `P-PH000-ST002-AC006-TK000` | Assess AC006 readiness and harden the `GATE-001` package boundary | `completed` | LLM_Consultant | `P-PH000-ST002-AC004` | `analysis/` | `guideline_workspace_analysis.md` | Published the readiness assessment, added the missing authority inputs, and hardened the plan boundary so later AC006 work can proceed without package ambiguity. |
| TK001 | `P-PH000-ST002-AC006-TK001` | Audit current session-close skill and briefing surface gap | `planned` | LLM_Consultant | TK000 | `analysis/` | `guideline_workspace_notes.md` | Produce the three-domain gap audit covering: (a) session-close skill operational gaps, (b) snotes closeout guidance gaps, (c) client-facing briefing surface gap. Includes authority-source mapping and lower-intelligence assistant support matrix. |
| TK002 | `P-PH000-ST002-AC006-TK002` | Comparative analysis: briefing dashboard architectural options | `planned` | LLM_Consultant | TK001 | `analysis/` | `guideline_workspace_analysis.md` | Produce a comparative analysis evaluating architectural options for the briefing dashboard placement, filtering logic, and derivation method. Session-close skill direction is already covered by the TK001 audit and the existing AC004 standards-input authority. |
| TK003 | `P-PH000-ST002-AC006-TK003` | Standards-input proposal: briefing dashboard | `planned` | LLM_Consultant | TK002 | `proposal/` | `guideline_workspace_proposal.md` | Author a standards-input proposal defining the briefing dashboard conventions, high-level architecture, and implementation boundary. Includes per-feature decision requests for client disposition. |
| TK004 | `P-PH000-ST002-AC006-TK004` | Implementation spec: session-close skill hardening | `planned` | LLM_Consultant | TK001 | `implementation/` | `guideline_workspace_implementation.md` | Author the execution contract for rewriting and validating `prompt/skills/session-close/SKILL.md` as a prompt-assist-only consultant skill with detailed `snotes_` guidance. References the AC004 standards-input proposal as authority source. |
| TK005 | `P-PH000-ST002-AC006-TK005` | Implementation spec: briefing dashboard | `planned` | LLM_Consultant | TK003 | `implementation/` | `guideline_workspace_implementation.md` | Author the execution contract for creating the briefing dashboard artifact. References the TK003 standards-input proposal as authority source. |
| TK006 | `P-PH000-ST002-AC006-TK006` | GATE-001 disposition proposal package assembly | `planned` | LLM_Consultant | TK004, TK005 | `proposal/` | `guideline_workspace_proposal.md` | Assemble the full GATE-001 evidence package referencing: TK000 readiness assessment, TK001 audit, TK002 comparative analysis, TK003 briefing standards-input, TK004 session-close impl spec, TK005 briefing impl spec, and the AC004 standards-input proposal as inherited authority. |
| GATE-001 | `P-PH000-ST002-AC006-GATE-001` | Gate: Client approval of AC006 expanded scope | `planned` | Client | TK006 | GDR | `guideline_workspace_proposal.md` | Decide whether AC006 may proceed from planning into execution-backed work for both the session-close skill rewrite and the briefing dashboard creation. |
| TK007 | `P-PH000-ST002-AC006-TK007` | Execute session-close skill hardening | `planned` | LLM_Consultant | GATE-001 | `prompt/skills/session-close/` | TK004 impl spec | Rewrite `SKILL.md` via skill-creator + writing-skills superpowers skill. Create symlinks to `.agents/skills/session-close` and `.claude/skills/session-close`. Validate operational reachability. |
| TK008 | `P-PH000-ST002-AC006-TK008` | Execute briefing dashboard creation | `planned` | LLM_Consultant | GATE-001 | `prompt/artifacts/tasks/P/status/` | TK005 impl spec | Create the briefing dashboard artifact at the path determined by the approved TK003 standards-input proposal and TK005 implementation spec. |

**Task detail sections** — The detailed task sections (Section III) must be fully rewritten to match the new register. Each task section must follow the existing pattern (Purpose, Deliverable, Inputs Required, Scope, Steps where applicable, Success Criteria). Key requirements per task:

- **TK000**: Retain as-is (completed). No changes to the detailed section.
- **TK001**: Update title to "Audit Current Session-Close Skill And Briefing Surface Gap". Expand scope to three domains: (a) session-close skill operational gaps, (b) snotes closeout guidance gaps, (c) client-facing briefing surface gap. Add input: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC005/plan_P-PH000-ST002-AC005.md`. Add success criteria checkbox: `[ ] Client-facing briefing surface gap is explicit with downstream recommendation`. Add success criteria checkbox: `[ ] Guideline_workspace_proposal.md multi-feature gap is captured as open question`.
- **TK002**: New section. Purpose: Evaluate architectural options for the briefing dashboard. Deliverable: `analysis/analysis_P-PH000-ST002-AC006_briefing-dashboard-comparative-assessment.md`. Inputs: TK001 audit, `status_program.yaml`, `status_program.md`, `guideline_workspace_analysis.md`. Scope in: placement options, filtering logic, derivation method, relationship to existing status hierarchy. Scope out: session-close skill architecture (already decided via AC004 authority), actual dashboard creation. Success criteria: `[ ] At least two placement options are compared`, `[ ] Evaluation criteria include client usability, maintenance burden, authority-hierarchy compliance`, `[ ] Recommendation is scoring-based`.
- **TK003**: New section. Purpose: Propose the briefing dashboard conventions. Deliverable: `proposal/proposal_P-PH000-ST002-AC006_briefing-dashboard-standards-input.md`. Inputs: TK002 comparative analysis, `guideline_workspace_proposal.md`. Scope in: briefing dashboard conventions, high-level architecture, filtering criteria, derivation rules, placement decision. Scope out: session-close skill conventions (already covered by AC004 standards-input). Success criteria: `[ ] Conventions are explicit and file-grounded`, `[ ] Decision requests allow independent feature approval`, `[ ] No implementation work is authorized prematurely`.
- **TK004**: Rewrite. Purpose: Author the execution contract for session-close skill hardening. Deliverable: `implementation/implementation_P-PH000-ST002-AC006_session-close-hardening-task-specification.md`. Inputs: TK001 audit, AC004 standards-input proposal (`proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md`), `guideline_workspace_implementation.md`, Codex skill-creator reference (`/home/quantuan125/.codex/skills/.system/skill-creator/SKILL.md`). Scope in: skill rewrite contract, symlink creation, snotes guidance, skill-creator + writing-skills usage method. Scope out: briefing dashboard (that is TK005). Success criteria: `[ ] Skill rewrite boundary is explicit`, `[ ] Symlink creation for .agents/skills/ and .claude/skills/ is specified`, `[ ] snotes_ authoring guidance is governed by guideline_workspace_notes.md`, `[ ] Codex skill-creator and writing-skills superpowers are specified as implementation method`.
- **TK005**: New section. Purpose: Author the execution contract for briefing dashboard creation. Deliverable: `implementation/implementation_P-PH000-ST002-AC006_briefing-dashboard-task-specification.md`. Inputs: TK003 standards-input proposal, `guideline_workspace_implementation.md`. Scope in: briefing artifact creation contract, filtering logic, derivation rules, placement. Scope out: session-close skill (that is TK004). Success criteria: `[ ] Dashboard creation boundary is explicit`, `[ ] Filtering and derivation logic is specified`, `[ ] Artifact placement is determined by TK003 approved architecture`.
- **TK006**: Rewrite. Purpose: Assemble the GATE-001 disposition proposal. Deliverable: `proposal/proposal_P-PH000-ST002-AC006-GATE-001_session-close-and-briefing-disposition.md`. Inputs: All TK000–TK005 deliverables, AC004 standards-input proposal. Success criteria: `[ ] All pre-gate evidence is indexed`, `[ ] Session-close and briefing dashboard features have independently decidable GIR entries`, `[ ] Readiness assessment is included as required evidence`.
- **GATE-001**: Rewrite. Entry criteria: TK000 through TK006 complete. Both features are explicitly scoped. Both implementation specs are included. Exit criteria: Client records decision in GDR. Post-gate tasks (TK007, TK008) remain blocked until approval.
- **TK007**: New section. Purpose: Execute the session-close skill rewrite per the approved TK004 implementation spec. Deliverable: Rewritten `prompt/skills/session-close/SKILL.md` + symlinks. Blocked by: GATE-001.
- **TK008**: New section. Purpose: Execute the briefing dashboard creation per the approved TK005 implementation spec. Deliverable: Briefing dashboard artifact at approved path. Blocked by: GATE-001.

**Gate Model section** — Rewrite to reflect the expanded scope:
```
**Gate Model**: `GATE-001` is a consultation gate for AC006's expanded scope covering both session-close skill hardening and briefing dashboard creation. The gate package MUST include the completed readiness assessment (TK000), the three-domain gap audit (TK001), the briefing comparative analysis (TK002), the briefing standards-input proposal (TK003), and both implementation specifications (TK004, TK005). The session-close skill's authority source is the existing AC004 standards-input proposal, not a new AC006 proposal. Post-gate execution tasks (TK007, TK008) remain blocked until the client approves the gate package.
```

**Dependency graph narrative** — Add after the Gate Model section:
```
**Dependency graph:**

TK000 (completed)
  └─ TK001 (audit: session-close + briefing gap)
       ├─ TK002 (comparative: briefing) → TK003 (proposal: briefing) → TK005 (impl: briefing) ─┐
       └─ TK004 (impl: session-close) ─────────────────────────────────────────────────────────────┤
                                                                                                    └─ TK006 (GATE-001 package)
                                                                                                         └─ GATE-001
                                                                                                              ├─ TK007 (execute: session-close)
                                                                                                              └─ TK008 (execute: briefing)
```

**Links Register** — Add new entries:
- `| Analysis | AC006 Phase A Implementation Spec | prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/implementation/implementation_P-PH000-ST002-AC006_phase-a-scope-amendment-task-specification.md |`
- `| Upstream Authority | AC004 Session-Close Standards Input | prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md |`

**Changelog** — Append:

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v2.0.0 | 2026-03-28 | Structural Rewrite | Expanded AC006 scope to include briefing dashboard feature per SES002 client decisions. Eliminated standalone TK002 hardening analysis. Added briefing-focused comparative analysis (TK002), briefing standards-input proposal (TK003), and briefing implementation spec (TK005). Moved all implementation specs pre-gate. Renumbered entire task register (TK000–TK008 + GATE-001). Reversed AC005 dependency to depend on AC006 instead of AC004. |

---

### SPEC-002 — AC005 Activity Plan Dependency Amendment

| Field | Detail |
|:--|:--|
| Requirement Source | SES002 client decision: AC005 now depends on AC006 instead of AC004 |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC005/plan_P-PH000-ST002-AC005.md` |
| Required end-state posture | Frontmatter version bumped. `Depends On` field in Activity Outline reads `P-PH000-ST002-AC006`. All task `Depends On` fields that previously referenced `P-PH000-ST002-AC004` now reference `P-PH000-ST002-AC006`. Changelog records the amendment. |
| Explicit non-target / do-not-change constraints | Do NOT change AC005's scope, task register structure, deliverables, or gate model. Only the dependency edge changes. |
| Validation check | (1) Grep for `AC004` in the file — should only appear in historical context or changelog, not in any active `Depends On` field. (2) Frontmatter version is bumped from `1.0.0` to `1.1.0`. (3) Changelog entry exists for the dependency change. |
| Blocking ambiguity rule | If AC005 has any other dependency references beyond the `Depends On` field that reference AC004 in an active (non-historical) capacity, escalate rather than changing them. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'1.0.0'` → `'1.1.0'`
- `date`: retain `'2026-03-28'`

**Activity Outline — Depends On:**
Change `**Depends On**: \`P-PH000-ST002-AC004\`` to `**Depends On**: \`P-PH000-ST002-AC006\``

**Task Register — TK001 Depends On:**
Change the TK001 row `Depends On` column from `P-PH000-ST002-AC004` to `P-PH000-ST002-AC006`.

**Context list:**
Add `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` to the Context section.

**Changelog** — Append:

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-28 | Amendment | Reversed AC005 dependency from AC004 to AC006 per SES002 consultation decision. AC005 commissioning work now depends on AC006 completion, since the client-facing briefing dashboard (being developed in AC006) is a prerequisite for productive T105 commissioning consultation. |

---

### SPEC-003 — Stream Plan Amendment

| Field | Detail |
|:--|:--|
| Requirement Source | SES002 scope expansion and dependency reversal require stream-level plan alignment |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
| Required end-state posture | Activity Register row for AC005 shows `Depends On: AC006` instead of `AC004`. AC006 row shows expanded deliverable summary including briefing dashboard. Executive Summary / Current closure state paragraph updated to reflect SES002 scope expansion. Version bumped. Changelog records the amendment. |
| Explicit non-target / do-not-change constraints | Do NOT change AC001–AC004 rows. Do NOT change the Activities (Planned) detailed sections for AC001–AC004. |
| Validation check | (1) AC005 Activity Register row `Depends On` column reads `AC006`. (2) AC006 row `Deliverable` column mentions both session-close skill hardening and briefing dashboard. (3) Version bumped to `1.13.0`. (4) Changelog entry exists. |
| Blocking ambiguity rule | If the stream plan contains other references to AC005's dependency on AC004 outside the Activity Register (e.g., in the AC005 detailed section), update those too. If uncertain about scope, escalate. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'1.12.0'` → `'1.13.0'`

**Executive Summary — Current closure state:**
Replace the current closure state paragraph with:
```
**Current closure state**: `GATE-002` passed on 2026-03-27, `GATE-003` was approved on 2026-03-28, and AC004 is now closed after the assistant-boundary closeout updates completed through `TK008`. AC006 is in active scope expansion after SES002 widened its boundary to include both session-close skill hardening and a client-facing briefing dashboard. AC005 now depends on AC006 (reversed from AC004) since the briefing dashboard is a prerequisite for productive T105 commissioning consultation. Historical `GATE-001` remains preserved as superseded.
```

**Activity Register — AC005 row:**
Change `Depends On` from `AC004` to `AC006`.

**Activity Register — AC006 row:**
- Change `Deliverable` from: `Active readiness-hardening plan for prompt-assist-only \`session-close\` evolution and detailed \`snotes_\` guidance`
  to: `Expanded scope: session-close skill hardening (prompt-assist-only) + client-facing briefing dashboard (filtered active-work view from status ledger). Two parallel pre-gate branches converging at GATE-001.`

**Activities (Planned) — AC005 detailed section:**
- Change `**Depends On**:` line from `- \`P-PH000-ST002-AC004\`` to `- \`P-PH000-ST002-AC006\``
- Change the `**Planning Posture**:` paragraph to: `AC005 is a separate planned consultation-first activity. It depends on AC006 completion since the briefing dashboard (being developed in AC006) is a prerequisite for productive T105 commissioning consultation. The future initiative-opening and \`comm_\` handoff contract remain explicit.`

**Activities (Planned) — AC006 detailed section:**
- Update `**Purpose**:` to: `Hold the expanded follow-on work for deeper \`session-close\` skill development and a client-facing briefing dashboard after AC004, including detailed prompt-assist-only guidance for status reconciliation, \`snotes_\` authoring, and a filtered active-work view for session continuity and program-level planning enablement.`
- Update `**Deliverables**:` to include:
  - Readiness assessment and GATE-001 package-boundary definition
  - Three-domain gap audit (session-close, snotes, briefing)
  - Briefing dashboard comparative analysis and standards-input proposal
  - Implementation specs for both features (pre-gate)
  - GATE-001 disposition proposal
  - Post-gate: hardened session-close skill + briefing dashboard artifact
- Update `**Scope — In scope**:` to add: `client-facing briefing dashboard for session-continuity and program-level planning enablement; briefing dashboard comparative analysis and standards-input proposal`
- Update `**Planning Posture**:` to reflect SES002 scope expansion.
- Update `**Success Criteria**:` to add:
  - `[ ] Briefing dashboard feature is explicitly scoped with its own standards-input proposal`
  - `[ ] AC005 dependency is reversed to AC006`

**Changelog** — Append:

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.13.0 | 2026-03-28 | Amendment | Expanded AC006 scope per SES002 to include briefing dashboard feature. Reversed AC005 dependency from AC004 to AC006. Updated Activity Register and detailed sections for both AC005 and AC006. |

---

### SPEC-004 — Phase Plan Amendment

| Field | Detail |
|:--|:--|
| Requirement Source | SES002 scope expansion and dependency reversal require phase-level snapshot alignment |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md` |
| Required end-state posture | Activity Snapshot Index row for AC005 reflects updated status/dependency context. AC006 row reflects expanded scope. Stream Register row for ST002 reflects the SES002 scope expansion. Version bumped. Changelog records the amendment. |
| Explicit non-target / do-not-change constraints | Do NOT change any rows outside ST002 (AC005, AC006). Do NOT change Stream Register rows for ST000, ST001, ST004. |
| Validation check | (1) AC006 snapshot row `Name` reflects expanded scope. (2) ST002 Stream Register `Key Deliverables` mentions briefing dashboard. (3) Version bumped to `0.4.14`. (4) Changelog entry exists. |
| Blocking ambiguity rule | The phase plan's Activity Snapshot is a thin snapshot only. If the required change implies inserting detailed task-level information, stop — the phase plan carries activity-level data only. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'0.4.13'` → `'0.4.14'`

**Activity Snapshot As-Of:** Update to `2026-03-28` (retain, already current).

**Activity Snapshot — AC005 row (line 77):**
No change to the row itself (it correctly shows `planned` and its owner), but the phase plan does not carry dependency info at the snapshot level. No row-level change needed.

**Activity Snapshot — AC006 row (line 78):**
Change `Name` from `Session-Close Skill Hardening And Snotes Closeout Guidance` to `Session-Close Skill Hardening, Briefing Dashboard & Snotes Closeout Guidance`.

**Stream Register — ST002 row (line 49):**
Change `Key Deliverables` from:
`AC004 is closed after \`GATE-003\` APPROVE and \`TK008\`; AC005 remains planned and AC006 is in readiness hardening`
to:
`AC004 closed; AC006 expanded to session-close + briefing dashboard (SES002); AC005 now depends on AC006`

**Changelog** — Append:

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.4.14 | 2026-03-28 | Housekeeping | Refreshed the PH000 snapshot after SES002 expanded AC006 scope to include briefing dashboard and reversed AC005 dependency to AC006. |

---

### SPEC-005 — Roadmap Amendment

| Field | Detail |
|:--|:--|
| Requirement Source | SES002 scope expansion and dependency reversal require roadmap snapshot alignment |
| Target file(s) | `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md` |
| Required end-state posture | Current Delivery Snapshot — Program Status System row reflects the SES002 scope expansion and AC005 dependency reversal. Version bumped. Changelog records the amendment. |
| Explicit non-target / do-not-change constraints | Do NOT change Phase Register, Links Register, or Open Questions Register. Roadmap is thin-spine — no stream/activity/task execution detail. |
| Validation check | (1) Program Status System snapshot mentions briefing dashboard. (2) Next Milestone mentions both features. (3) Version bumped to `0.2.10`. (4) Changelog entry exists. |
| Blocking ambiguity rule | If the roadmap change implies inserting task-level or stream-level detail, stop — the roadmap is thin-spine only. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'0.2.9'` → `'0.2.10'`

**Current Delivery Snapshot — Program Status System row:**
Replace:
```
| Program Status System | AC004 is closed after the approved `GATE-003` decision, AC005 remains a separate planned follow-on lane, and AC006 is in readiness hardening for future `GATE-001` packaging. | Complete AC006 readiness hardening and later advance the separately governed AC005 and AC006 follow-on lanes as approved | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
```
with:
```
| Program Status System | AC004 closed. AC006 expanded per SES002 to cover session-close skill hardening and a client-facing briefing dashboard. AC005 now depends on AC006. | Complete AC006 pre-gate work (audit, comparative analysis, proposals, implementation specs) and advance to GATE-001 | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
```

**Changelog** — Append:

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.2.10 | 2026-03-28 | Amendment | Refreshed the compact status-system snapshot after SES002 expanded AC006 to include briefing dashboard and reversed AC005 dependency. |

---

### SPEC-006 — Status Ledger Amendment (YAML)

| Field | Detail |
|:--|:--|
| Requirement Source | §7.5 Update Sequence requires ledger update before narrative derivation |
| Target file(s) | `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Required end-state posture | AC005 entry dependency edge changed from `AC004` → `AC006`. AC006 entry name updated to reflect expanded scope. AC006 evidence list includes SES002 reference. Both entries have `last_updated: '2026-03-28'` and `updated_by: LLM_Consultant`. Top-level `last_updated` reflects update. |
| Explicit non-target / do-not-change constraints | Do NOT change any entries outside AC005 and AC006. Do NOT change status values (AC005 stays `planned`, AC006 stays `in_progress`). Do NOT change health dimensions. |
| Validation check | (1) AC005 `dependencies[0].from_id` reads `P-PH000-ST002-AC006`. (2) AC006 `name` includes "Briefing Dashboard". (3) Both entries have updated `last_updated`. (4) Top-level `last_updated` matches. |
| Blocking ambiguity rule | If the YAML structure doesn't match the expected schema for dependency edges, escalate rather than inventing fields. |
| Status | `open` |

#### Implementation Detail

**Top-level fields:**
- `last_updated`: keep at `'2026-03-28'` (same day)

**AC005 entry (lines 561–599):**
- Change `dependencies[0].from_id` from `P-PH000-ST002-AC004` to `P-PH000-ST002-AC006`
- Change `dependencies[0].evidence[0].summary` from `'Dependency clause from source plan row for P-PH000-ST002-AC005: AC004'` to `'Dependency clause from source plan row for P-PH000-ST002-AC005: AC006 (reversed per SES002)'`
- Change `evidence[0].summary` from `'Source plan row for P-PH000-ST002-AC005 (status planned; raw depends_on: AC004)'` to `'Source plan row for P-PH000-ST002-AC005 (status planned; raw depends_on: AC006, reversed per SES002)'`

**AC006 entry (lines 601–640+):**
- Change `name` from `Session-Close Skill Hardening And Snotes Closeout Guidance` to `Session-Close Skill Hardening, Briefing Dashboard & Snotes Closeout Guidance`
- Append to `evidence[]`:
  ```yaml
  - type: session
    ref: prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/snotes/snotes_P-PH000-ST002-AC006-SES002.md
    date: '2026-03-28'
    by: LLM_Consultant
    summary: 'SES002: expanded AC006 scope to include briefing dashboard, reversed AC005 dependency, and structurally rewrote the task register.'
  ```

---

### SPEC-007 — Status Narrative Amendment

| Field | Detail |
|:--|:--|
| Requirement Source | §7.5 Update Sequence step 3: derive/update narrative from ledger |
| Target file(s) | `prompt/artifacts/tasks/P/status/status_program.md` |
| Required end-state posture | Section 2 Status table row for AC005 remains `planned` (no status change). AC006 row name updated to match ledger. Section 1 Summary `Total Entries` remains 84. Version bumped. Changelog records the amendment. |
| Explicit non-target / do-not-change constraints | Do NOT change Section 7 (Operational Update Protocol). Do NOT change any rows outside AC005 and AC006. Do NOT change status values. |
| Validation check | (1) AC006 row in Section 2 name matches the ledger name. (2) Version bumped to `1.0.5`. (3) Changelog entry exists. |
| Blocking ambiguity rule | The narrative is derived from the ledger. If the narrative contains information that contradicts the ledger after SPEC-006 is applied, correct the narrative to match the ledger. If unsure what the ledger says, read the ledger first. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'1.0.4'` → `'1.0.5'`

**Section 2 — Status table:**
- AC006 row: Change `Name` from `Session-Close Skill Hardening And Snotes Closeout Guidance` to `Session-Close Skill Hardening, Briefing Dashboard & Snotes Closeout Guidance`.
- No other row changes.

**Changelog** — Append:

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.5 | 2026-03-28 | Amendment | Derived narrative refresh after SES002 expanded AC006 scope to include briefing dashboard and reversed AC005 dependency to AC006. Updated AC006 name in Section 2 status table to match ledger. |

---

### SPEC-008 — Session Notes Creation (SES002)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` §1.6 and §6 require a session notes file for each governed consultation session |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/snotes/snotes_P-PH000-ST002-AC006-SES002.md` |
| Required end-state posture | A complete activity session notes file exists with all required sections (A through H) per guideline §6. The file captures the SES002 scope amendment decisions, the dependency reversal, the proposal architecture decision (one briefing-only proposal), and the carry-forward actions. |
| Explicit non-target / do-not-change constraints | Do NOT modify SES001. Do NOT modify any other session notes files. |
| Validation check | (1) File exists at the expected path. (2) All sections A–H are present. (3) Frontmatter `session_id` reads `P-PH000-ST002-AC006-SES002`. (4) Discussion Points, Decisions, and Actions tables are populated. |
| Blocking ambiguity rule | If unsure about the exact decision wording, refer to the SES002 consultation transcript (this conversation) rather than summarizing from memory. |
| Status | `open` |

#### Implementation Detail

**Frontmatter:**
```yaml
---
artifact_type: 'NOTES'
notes_type: 'SESSION_ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream: 'ST002'
activity_id: 'P-PH000-ST002-AC006'
session: 'SES002'
session_id: 'P-PH000-ST002-AC006-SES002'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
register_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
raw_transcript_reference: '—'
---
```

**Title:**
`# ACTIVITY SESSION NOTES: P (PROGRAM) — PH000 / ST002 / AC006 / SES002 (Scope Expansion, Dependency Reversal, and Phase A/B Execution)`

**Section A — Agenda / Topics:**
1. Review client QA concerns about session-close skill operational reachability, client-facing status usability, and high-level planning enablement.
2. Scope expansion decision: add briefing dashboard as a V1.1 extension within AC006.
3. Dependency reversal: AC005 now depends on AC006 instead of AC004.
4. Task register structural rewrite and proposal architecture decisions.
5. Phase A scope amendment execution and Phase B (TK001) audit execution.

**Section B — Narrative Summary:**
This session expanded AC006's boundary significantly. The client identified three critical gaps: (1) the session-close skill cannot be tested because it lacks symlinks to `.agents/skills/` and `.claude/skills/`, (2) the `status_program.md` file is too comprehensive for client-facing session-continuity use — the client needs a filtered "active work briefing" view, and (3) the client wants to use the status system for high-level program planning but cannot do so without a focused review mechanism.

The consultant assessed that the briefing dashboard need was the most critical concern and recommended it as a V1.1 extension within AC006 rather than deferring entirely to T105. The client approved this and further decided that: AC005 should now depend on AC006 (since the briefing dashboard is a prerequisite for productive T105 commissioning), the entire task register should be renumbered, implementation specs should be moved pre-gate, the old TK002 hardening analysis should be eliminated (its content absorbed by the comparative analysis and standards-input proposal), and the briefing dashboard should have its own standalone standards-input proposal while the session-close skill relies on the existing AC004 standards-input authority.

The consultant produced a Phase A implementation specification to govern the nine-surface scope amendment and a TK001 gap audit analysis covering all three domains.

**Section C — Discussion Points (DP Table):**

| ID | Topic | Outcome | Rationale | Evidence |
|:---|:------|:--------|:----------|:---------|
| `P-PH000-ST002-AC006-SES002-DP001` | Client-facing status usability gap | The `status_program.md` file is too comprehensive for session-continuity use; a separate filtered briefing surface is needed | 84 entries, full health table, operational protocol — designed as system-of-record, not client-facing decision surface | `prompt/artifacts/tasks/P/status/status_program.md` |
| `P-PH000-ST002-AC006-SES002-DP002` | Session-close skill operational reachability | The skill file exists but has no symlinks to `.agents/skills/` or `.claude/skills/`, making it unreachable for invocation or testing | Verified: `wrap-up` is symlinked to both locations; `session-close` is not | `.agents/skills/` directory listing; `.claude/skills/` directory listing |
| `P-PH000-ST002-AC006-SES002-DP003` | Proposal architecture for multi-feature gate | One briefing-only standards-input proposal (not combined with session-close); session-close already has AC004 standards-input authority | Each proposal should address one cohesive decision domain; reduces client cognitive load; avoids guideline gap around multi-feature proposals | AC004 `proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md` |
| `P-PH000-ST002-AC006-SES002-DP004` | Elimination of standalone TK002 hardening analysis | Content absorbed by comparative analysis (TK002 new) and standards-input proposal (TK003 new) | Original TK002 was designed for narrower scope; with expanded boundary, a standalone hardening analysis is redundant | SES002 consultation |
| `P-PH000-ST002-AC006-SES002-DP005` | Implementation specs pre-gate sequencing | Both implementation specs (session-close + briefing) must be authored before GATE-001 | Gate decision should be fully informed; client needs to see execution contracts before approving | SES002 consultation |
| `P-PH000-ST002-AC006-SES002-DP006` | Guideline gap: multi-feature proposal governance | Captured as open question in TK001 audit; deferred to future governance activity | The gap exists in `guideline_workspace_proposal.md` but is not AC006's scope to fix | SES002 consultation |

**Section D — Decisions Captured (DEC Table):**

| ID | Decision | Type | Status | Owner | Date | Rationale | Acceptance Signal | Evidence |
|:---|:---------|:-----|:-------|:------|:-----|:----------|:------------------|:---------|
| `P-PH000-ST002-AC006-SES002-DEC001` | Expand AC006 scope to include briefing dashboard as a V1.1 extension | Scope | Confirmed | Client | 2026-03-28 | Client needs a filtered active-work view for session continuity and program-level planning; deferring entirely to T105 would leave the usability gap unresolved for too long | Client approved consultant recommendation | SES002 consultation |
| `P-PH000-ST002-AC006-SES002-DEC002` | Reverse AC005 dependency from AC004 to AC006 | Dependency | Confirmed | Client | 2026-03-28 | The briefing dashboard (AC006) is a prerequisite for productive T105 commissioning consultation (AC005) | Client directed | SES002 consultation |
| `P-PH000-ST002-AC006-SES002-DEC003` | Renumber entire AC006 task register with clean integer sequencing (TK000–TK008) | Planning | Confirmed | Client | 2026-03-28 | v2.0.0 structural rewrite is the appropriate moment for clean numbering | Client approved consultant recommendation | SES002 consultation |
| `P-PH000-ST002-AC006-SES002-DEC004` | Eliminate standalone TK002 hardening analysis; absorb into comparative analysis and standards-input proposal | Planning | Confirmed | Client | 2026-03-28 | Expanded scope makes the standalone artifact redundant | Client directed | SES002 consultation |
| `P-PH000-ST002-AC006-SES002-DEC005` | Produce one briefing-only standards-input proposal; session-close relies on existing AC004 authority | Architecture | Confirmed | Client | 2026-03-28 | Each proposal should address one decision domain; session-close conventions already approved in AC004 | Consultant recommended one briefing-only proposal; client approved | SES002 consultation |
| `P-PH000-ST002-AC006-SES002-DEC006` | Move implementation specs (session-close + briefing) pre-gate as part of GATE-001 evidence package | Planning | Confirmed | Client | 2026-03-28 | Gate decision should be fully informed by execution contracts | Client directed | SES002 consultation |
| `P-PH000-ST002-AC006-SES002-DEC007` | Comparative analysis (TK002) should focus primarily on briefing dashboard; session-close architecture covered by TK001 audit and AC004 authority | Scope | Confirmed | Client | 2026-03-28 | Session-close direction already decided in AC004; briefing dashboard has genuine architectural options | Client approved consultant recommendation | SES002 consultation |

**Section E — Actions / Carry-Forward (ACT Table):**

| ID | Action | Owner | Status |
|:---|:-------|:------|:-------|
| `P-PH000-ST002-AC006-SES002-ACT001` | Amend AC006 plan to v2.0.0 with full task register rewrite | LLM_Consultant | `pending` |
| `P-PH000-ST002-AC006-SES002-ACT002` | Amend AC005 plan dependency from AC004 to AC006 | LLM_Consultant | `pending` |
| `P-PH000-ST002-AC006-SES002-ACT003` | Update stream plan, phase plan, and roadmap for AC005/AC006 changes | LLM_Consultant | `pending` |
| `P-PH000-ST002-AC006-SES002-ACT004` | Update status ledger and derived narrative | LLM_Consultant | `pending` |
| `P-PH000-ST002-AC006-SES002-ACT005` | Register SES002 in the ST002 stream notes register | LLM_Consultant | `pending` |
| `P-PH000-ST002-AC006-SES002-ACT006` | Execute TK001 three-domain gap audit | LLM_Consultant | `pending` |

**Section F — Open Questions Register (OQ Table):**

| ID | Topic | Question | Owner | Status | Needed By |
|:---|:------|:---------|:------|:-------|:----------|
| `P-PH000-ST002-AC006-SES002-OQ001` | Briefing dashboard placement | Whether the briefing should be a separate file (`briefing_program.md`) or a new section in `status_program.md` — to be resolved by TK002 comparative analysis | LLM_Consultant | Open | Before `P-PH000-ST002-AC006-TK003` starts |
| `P-PH000-ST002-AC006-SES002-OQ002` | Guideline gap for multi-feature proposal governance | `guideline_workspace_proposal.md` does not currently address when a gate package spans features with existing authority and features needing new authority — to be captured as TK001 finding and deferred to future governance activity | LLM_Consultant | Open | Captured in TK001 audit |

**Section G — Session Handoff Pack:**
- AC006 scope was expanded per client decisions to include briefing dashboard feature.
- AC005 dependency reversed from AC004 to AC006.
- Task register structurally rewritten (TK000–TK008 + GATE-001).
- Phase A implementation spec was authored to govern the nine-surface scope amendment.
- TK001 gap audit was authored covering three domains.
- Phase A execution (applying the nine-surface amendments) remains pending.
- No proposal, comparative analysis, or implementation spec artifact was authored in this session beyond the Phase A task specification.

**Section H — Changelog:**

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Recorded the SES002 scope expansion, dependency reversal, task register rewrite, and proposal architecture decisions. Authored Phase A implementation spec and TK001 gap audit. |

---

### SPEC-009 — Stream Notes Register Amendment

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_notes.md` §5.1 JIT Registration requires register update when session notes are created |
| Target file(s) | `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` |
| Required end-state posture | Section III Activity Notes Register contains a new row for `P-PH000-ST002-AC006-SES002`. Version bumped. Changelog records the amendment. |
| Explicit non-target / do-not-change constraints | Do NOT modify existing register rows. Do NOT modify Sections I, II, or IV. |
| Validation check | (1) New row exists in Section III for AC006 SES002. (2) Notes File path is correct. (3) Version bumped to `1.17.0`. (4) Changelog entry exists. |
| Blocking ambiguity rule | If the register already contains a row for `P-PH000-ST002-AC006-SES002`, do not duplicate it. |
| Status | `open` |

#### Implementation Detail

**Frontmatter changes:**
- `version`: `'1.16.0'` → `'1.17.0'`

**Section III — Activity Notes Register:**
Append new row after the AC006 SES001 row:

```
| AC006 | `P-PH000-ST002-AC006-SES002` | Scope Expansion, Dependency Reversal, and Phase A/B Execution | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/snotes/snotes_P-PH000-ST002-AC006-SES002.md` |
```

**Changelog** — Append:

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.17.0 | 2026-03-28 | Amendment | Registered AC006 activity session `P-PH000-ST002-AC006-SES002` for scope expansion, dependency reversal, task register rewrite, and Phase A/B execution. |

---

## IV. IMPLEMENTATION SEQUENCE

Execute SPEC items in this order:

1. **SPEC-001** — AC006 plan v2.0.0 rewrite (this is the primary structural authority; all other changes derive from it)
2. **SPEC-002** — AC005 plan dependency amendment
3. **SPEC-003** — Stream plan amendment (derives from SPEC-001 + SPEC-002)
4. **SPEC-004** — Phase plan amendment (derives from SPEC-003)
5. **SPEC-005** — Roadmap amendment (derives from SPEC-003)
6. **SPEC-006** — Status ledger YAML amendment (must precede narrative per §7.5)
7. **SPEC-007** — Status narrative amendment (derived from SPEC-006)
8. **SPEC-008** — Session notes creation (SES002)
9. **SPEC-009** — Stream notes register amendment (must follow SPEC-008)

**Parallelism note**: SPEC-001 and SPEC-002 are independent and may be executed in parallel. SPEC-003 through SPEC-005 are independent of each other but all depend on SPEC-001 + SPEC-002. SPEC-006 must precede SPEC-007. SPEC-008 must precede SPEC-009.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| AC005 Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC005/plan_P-PH000-ST002-AC005.md` |
| Stream Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/plan_P-PH000-ST002.md` |
| Phase Plan | `prompt/artifacts/tasks/P/workspace/PH000/plan_P-PH000.md` |
| Roadmap | `prompt/artifacts/tasks/P/ssot/roadmap_P-PROGRAM_phase0.md` |
| Status Ledger | `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Status Narrative | `prompt/artifacts/tasks/P/status/status_program.md` |
| Stream Notes Register | `prompt/artifacts/tasks/P/workspace/PH000/ST002/notes_P-PH000-ST002.md` |
| AC004 Standards-Input | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md` |
| TK000 Readiness Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_readiness-and-gate-001-package-boundary-assessment.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Created the Phase A scope amendment task specification covering nine governed surfaces: AC006 plan v2.0.0, AC005 dependency reversal, stream/phase/roadmap alignment, status ledger and narrative, session notes, and stream notes register. |
