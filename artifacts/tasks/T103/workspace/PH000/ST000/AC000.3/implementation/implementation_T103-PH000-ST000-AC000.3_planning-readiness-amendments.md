---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T103'
initiative_code: 'ADRSS'
phase: '0'
stream_id: 'T103-PH000-ST000'
activity_id: 'T103-PH000-ST000-AC000.3'
task_id: 'T103-PH000-ST000-AC000.3 (pre-TK001 planning-readiness amendments)'
version: '1.0.0'
date: '2026-03-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md'
execution_audience: 'consultant'
purpose: 'Exact-content task specification for correcting §VII.F compliance violations in the stream and phase plans, adding reference material inputs to the AC000.3 plan, and closing the guideline gap regarding phase snapshot scoping of sub-activities — all required before AC000.3-TK001 execution can begin.'
---

# IMPLEMENTATION (Task Specification): AC000.3 Planning-Readiness Amendments

## I. PURPOSE & AUTHORITY

- **Purpose**: Provide exact file-level content for correcting sub-activity register placement violations (§VII.F), enriching the AC000.3 plan with newly available reference material inputs, and closing a guideline gap regarding phase Activity Snapshot Index scoping. This artifact specifies the precise content of every amendment so the executing assistant can reproduce the outcome without interpretation.
- **Authority chain**: Client consultation decisions (2026-03-26) -> This artifact specifies exact content -> Executing assistant amends files exactly as specified -> Consultant reviews the result.
- **Audience**: Executing assistant (consultant-orchestrated execution). The assistant MUST amend files using the exact content specified in each SPEC item. Do NOT summarize, paraphrase, or interpret the content — reproduce it verbatim.
- This artifact does **not** hold a GDR. Gate decisions are recorded in proposal artifacts only.

**Locked decisions driving this specification** (from 2026-03-26 consultation):

| Decision | Source |
|:--|:--|
| Remove AC000.3 from the stream plan Activity Register (§VII.F compliance) | Client approval, 2026-03-26 |
| Remove AC000.1 and AC000.2 from the phase plan Activity Snapshot Index (§VII.F spirit + industry best practice: parent activities only) | Client approval, 2026-03-26 |
| Remove AC000.3 from the phase plan ST000 activity table (§VII.F compliance) | Client approval, 2026-03-26 |
| Add `.agents/skills/claude-code/references/claude-skill.md` and `examples.md` to AC000.3 plan Context and TK002 Inputs | Client approval, 2026-03-26 |
| Amend `guideline_workspace_plan.md` §VII.F to explicitly address phase Activity Snapshot Index scoping | Client approval, 2026-03-26 |

## II. TASK SCOPE

- **Governing plan**: `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md`
- **Trigger**: Gate-001 readiness assessment identified three compliance findings requiring correction before AC000.3-TK001 execution can begin.
- **Deliverable contract**: Amended plan artifacts and guideline as enumerated in the target files table below.

**Target files (executive write set)**:

| # | File | Change Class | Action |
|:--|:--|:--|:--|
| F1 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` | Amend | Remove AC000.3 row from the Activity Register table |
| F2 | `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md` | Amend | Remove AC000.1 and AC000.2 rows from the Activity Snapshot Index; remove AC000.3 row from the ST000 activity table |
| F3 | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md` | Amend | Add reference material paths to Context section and TK002 Inputs Required section |
| F4 | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` | Amend | Add phase snapshot scoping clarification to §VII.F |

**Out of scope**:
- AC000.3-TK001 analysis artifact (dedicated session)
- AC000.3-TK002 comparative analysis artifact (dedicated session)
- Any `.agents/skills/claude-code/**` file changes
- Any session notes files (JIT rule: created when activities transition to `in_progress`)
- AC000 parent activity plan (the AC000.3 contract stub in the stream plan's AC000 section is correct and does not require amendment)
- Notes register (AC000.3 row is already correctly registered as `planned` with `—` per JIT §5.1)

## III. SPECIFICATION ITEMS

### SPEC-001 — Remove AC000.3 from Stream Plan Activity Register (F1)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §VII.F: "Sub-Activities MUST NOT be registered as standalone rows in any higher-level register (Phase/Stream Activity Registers)." |
| Output | Amended `F1` |
| Acceptance Criteria | The stream plan Activity Register contains exactly 3 rows (AC000, AC001, AC002); no sub-activity rows (AC000.x) appear in the register. The AC000.3 contract stub in the AC000 section (lines 131-147) remains unchanged. |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md`.

Apply the following targeted edits:

**1. Update the frontmatter version and date:**

Replace:
```
version: '1.6.0'
date: '2026-03-25'
```

With:
```
version: '1.7.0'
date: '2026-03-26'
```

**2. In Section II, remove the AC000.3 row from the Activity Register table.**

Replace the entire Activity Register table (header + all rows):
```
### Activity Register

| Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|
| AC000 | `T103-PH000-ST000-AC000` | Claude Code skill remediation commissioning and gated execution package | `in_progress` | LLM_Consultant | `—` | AC000 activity plan, original remediation acceptance path, incident-correction analysis, AC000.1 closeout, AC000.2 successor planning lane | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` |
| AC001 | `T103-PH000-ST000-AC001` | Orchestration execution pattern draft specification | `in_progress` | LLM_Consultant | `—` | AC001 activity plan, SES001 notes, execution-pattern assessment, draft execution specification, and GATE-001 proposal | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/plan_T103-PH000-ST000-AC001.md` |
| AC000.3 | `T103-PH000-ST000-AC000.3` | Claude Code skill defect remediation and optimization assessment | `planned` | LLM_Consultant | `—` | AC000.3 activity plan, defect audit analysis, optimization comparative assessment, and GATE-001 consultation package | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md` |
| AC002 | `T103-PH000-ST000-AC002` | External reviewer invocation skill | `planned` | LLM_Consultant | `T103-PH000-ST000-AC000.3-GATE-002` | AC002 activity plan, reviewer-delegation invocation skill, supervised trial evidence, and GATE-001/GATE-002 packages | — |
```

With:
```
### Activity Register

| Activity | Activity ID | Name | Status | Owner | Depends On | Deliverable | Reference |
|:--|:--|:--|:--|:--|:--|:--|:--|
| AC000 | `T103-PH000-ST000-AC000` | Claude Code skill remediation commissioning and gated execution package | `in_progress` | LLM_Consultant | `—` | AC000 activity plan, original remediation acceptance path, incident-correction analysis, AC000.1 closeout, AC000.2 successor planning lane | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000/plan_T103-PH000-ST000-AC000.md` |
| AC001 | `T103-PH000-ST000-AC001` | Orchestration execution pattern draft specification | `in_progress` | LLM_Consultant | `—` | AC001 activity plan, SES001 notes, execution-pattern assessment, draft execution specification, and GATE-001 proposal | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/plan_T103-PH000-ST000-AC001.md` |
| AC002 | `T103-PH000-ST000-AC002` | External reviewer invocation skill | `planned` | LLM_Consultant | `T103-PH000-ST000-AC000.3-GATE-002` | AC002 activity plan, reviewer-delegation invocation skill, supervised trial evidence, and GATE-001/GATE-002 packages | — |
```

**3. Add a new link to the Links Register for this implementation specification.**

Append the following row to the Links Register table (Section IV):
```
| Implementation | AC000.3 planning-readiness amendments specification | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/implementation/implementation_T103-PH000-ST000-AC000.3_planning-readiness-amendments.md` |
```

**4. Append a changelog entry to the Changelog table (Section V).**

Append the following row as the first entry (most recent) in the changelog table:
```
| v1.7.0 | 2026-03-26 | Amendment | Removed AC000.3 from the stream Activity Register per `guideline_workspace_plan.md` §VII.F (sub-activities MUST NOT be standalone register rows). The AC000.3 contract stub in the AC000 section is unchanged and remains the stream-level visibility surface. Added link to the AC000.3 planning-readiness amendments implementation specification. |
```

**Verification check**: After this edit, the Activity Register table MUST contain exactly 3 data rows: AC000, AC001, AC002. The AC000.3 sub-activity contract stub in the AC000 section (starting at "#### Sub-Activity AC000.3:") MUST remain unchanged.

---

### SPEC-002 — Remove Sub-Activity Rows from Phase Plan Surfaces (F2)

| Field | Detail |
|:--|:--|
| Requirement Source | `guideline_workspace_plan.md` §VII.F spirit + industry best practice (phase snapshots should show parent activities only); client approval 2026-03-26 |
| Output | Amended `F2` |
| Acceptance Criteria | The phase plan Activity Snapshot Index contains exactly 3 rows (AC000, AC001, AC002); no sub-activity rows. The ST000 activity table contains exactly 1 row (AC000 only); no sub-activity rows. |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md`.

Apply the following targeted edits:

**1. Update the frontmatter version and date:**

Replace:
```
version: '1.7.0'
date: '2026-03-25'
```

With:
```
version: '1.8.0'
date: '2026-03-26'
```

**2. In the Activity Snapshot Index section, update the As-Of date and remove the AC000.1 and AC000.2 sub-activity rows.**

Replace the entire Activity Snapshot Index block:
```
### Activity Snapshot Index

**Activity Snapshot As-Of**: 2026-03-25

| Stream | Activity | Activity ID | Name | Status (snapshot) | Owner | Source (Stream Plan) |
|:--|:--|:--|:--|:--|:--|:--|
| ST000 | AC000 | `T103-PH000-ST000-AC000` | Claude Code skill remediation commissioning and gated execution package | `in_progress` | LLM_Consultant | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| ST000 | AC000.1 | `T103-PH000-ST000-AC000.1` | Post-GATE-003 Claude Code skill monitoring & testing remediation | `completed` | LLM_Consultant | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| ST000 | AC000.2 | `T103-PH000-ST000-AC000.2` | Release-readiness and supervised monitoring planning | `completed` | LLM_Consultant | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| ST000 | AC001 | `T103-PH000-ST000-AC001` | Orchestration execution pattern draft specification | `in_progress` | LLM_Consultant | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| ST000 | AC002 | `T103-PH000-ST000-AC002` | External Reviewer Invocation Skill | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
```

With:
```
### Activity Snapshot Index

**Activity Snapshot As-Of**: 2026-03-26

| Stream | Activity | Activity ID | Name | Status (snapshot) | Owner | Source (Stream Plan) |
|:--|:--|:--|:--|:--|:--|:--|
| ST000 | AC000 | `T103-PH000-ST000-AC000` | Claude Code skill remediation commissioning and gated execution package | `in_progress` | LLM_Consultant | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| ST000 | AC001 | `T103-PH000-ST000-AC001` | Orchestration execution pattern draft specification | `in_progress` | LLM_Consultant | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| ST000 | AC002 | `T103-PH000-ST000-AC002` | External Reviewer Invocation Skill | `planned` | LLM_Consultant | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
```

**3. In the ST000 Stream Details section, remove the AC000.3 row from the Activities table.**

Replace the ST000 Activities table:
```
**Activities**:

| Activity | ID | Name | Status | Deliverable |
|:--|:--|:--|:--|:--|
| AC000 | T103-PH000-ST000-AC000 | Claude Code skill remediation commissioning and gated execution package | `in_progress` | `plan_T103-PH000-ST000-AC000.md`; `proposal_T103-PH000-ST000-AC000_gate-001_claude-code-skill-remediation-readiness.md`; normalized remediation specification; `AC000.1` monitoring/testing lane; `AC000.2` registration |
| AC000.3 | T103-PH000-ST000-AC000.3 | Claude Code skill defect remediation and optimization assessment | `planned` | `plan_T103-PH000-ST000-AC000.3.md` |
```

With:
```
**Activities**:

| Activity | ID | Name | Status | Deliverable |
|:--|:--|:--|:--|:--|
| AC000 | T103-PH000-ST000-AC000 | Claude Code skill remediation commissioning and gated execution package | `in_progress` | `plan_T103-PH000-ST000-AC000.md`; `proposal_T103-PH000-ST000-AC000_gate-001_claude-code-skill-remediation-readiness.md`; normalized remediation specification; `AC000.1` monitoring/testing lane; `AC000.2` registration |
```

**4. Append a changelog entry to the Changelog table (Section VII).**

Append the following row as the first entry (most recent) in the changelog table:
```
| v1.8.0 | 2026-03-26 | Amendment | Removed AC000.1 and AC000.2 sub-activity rows from the Activity Snapshot Index and removed AC000.3 from the ST000 activity table, per `guideline_workspace_plan.md` §VII.F (sub-activities MUST NOT appear in higher-level registers or snapshots; parent AC000 status reflects sub-activity progress per §VII.G). Refreshed snapshot As-Of to 2026-03-26. |
```

**Verification check**: After this edit, the Activity Snapshot Index MUST contain exactly 3 data rows (AC000, AC001, AC002). The ST000 Activities table MUST contain exactly 1 data row (AC000 only). Sub-activity detail is navigable by drilling into the stream plan → AC000 contract stub → sub-activity sections.

---

### SPEC-003 — Add Reference Material Inputs to AC000.3 Plan (F3)

| Field | Detail |
|:--|:--|
| Requirement Source | Gate-001 readiness assessment finding: GitHub-extracted Claude Code skill exemplar (claude-skill.md + examples.md) should be formally registered as inputs for TK002 comparative analysis |
| Output | Amended `F3` |
| Acceptance Criteria | AC000.3 plan Context section includes both new reference paths; TK002 Inputs Required section includes both new reference paths with descriptions |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md`.

Apply the following targeted edits:

**1. Update the frontmatter version and date:**

Replace:
```
version: '1.0.0'
date: '2026-03-25'
```

With:
```
version: '1.1.0'
date: '2026-03-26'
```

**2. In Section II (Activity Outline), add two new entries to the Context block.**

The current Context block ends with:
```
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
```

Append the following two lines immediately after the last Context entry:
```
- `.agents/skills/claude-code/references/claude-skill.md`
- `.agents/skills/claude-code/references/examples.md`
```

The resulting Context block should end with:
```
- `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
- `.agents/skills/claude-code/references/claude-skill.md`
- `.agents/skills/claude-code/references/examples.md`
```

**3. In Section III, Task TK002 (Skill Optimization Comparative Analysis), add two new entries to the Inputs Required section.**

The current TK002 Inputs Required section is:
```
**Inputs Required**:
- `.claude/skills/codex/SKILL.md` — reference skill (concise, battle-tested)
- `.agents/skills/claude-code/SKILL.md` — skill under evaluation
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/analysis/analysis_T103-PH000-ST000-AC000.3_claude-code-skill-surface-audit.md` — TK001 defect audit (determines what must change regardless of optimization)
```

Replace with:
```
**Inputs Required**:
- `.claude/skills/codex/SKILL.md` — reference skill (concise, battle-tested)
- `.agents/skills/claude-code/SKILL.md` — skill under evaluation
- `.agents/skills/claude-code/references/claude-skill.md` — external exemplar: GitHub-extracted Claude Code skill from the Codex CLI platform (~224 lines, defensive/practical pattern, treats `claude --help` as compatibility floor)
- `.agents/skills/claude-code/references/examples.md` — external exemplar: extended usage patterns companion to `claude-skill.md`
- `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/analysis/analysis_T103-PH000-ST000-AC000.3_claude-code-skill-surface-audit.md` — TK001 defect audit (determines what must change regardless of optimization)
```

**4. In Section IV (Links Register), add two new entries for the reference materials.**

Append the following two rows to the Links Register table:
```
| Skill (external exemplar) | GitHub-extracted Claude Code skill | `.agents/skills/claude-code/references/claude-skill.md` |
| Skill (external exemplar) | Extended usage patterns companion | `.agents/skills/claude-code/references/examples.md` |
```

**5. Append a changelog entry to the Changelog table (Section V).**

Append the following row as the first entry (most recent) in the changelog table:
```
| v1.1.0 | 2026-03-26 | Amendment | Added `.agents/skills/claude-code/references/claude-skill.md` and `examples.md` (GitHub-extracted Claude Code skill exemplar) to the plan Context section, TK002 Inputs Required, and Links Register. These provide an external architectural reference point for the optimization comparative analysis. |
```

**Verification check**: After this edit, the Context section MUST contain the two new reference paths. TK002 Inputs Required MUST list 5 items (was 3). The Links Register MUST contain the two new rows.

---

### SPEC-004 — Amend Guideline §VII.F to Clarify Phase Snapshot Scoping (F4)

| Field | Detail |
|:--|:--|
| Requirement Source | Gap identified during Gate-001 readiness assessment: §VII.F addresses registers but is silent on whether the phase Activity Snapshot Index follows the same scoping rule. Industry best practice (PMI/PMBOK, SAFe, PRINCE2) confirms each planning level shows only its direct children. Client approved a concise guideline clarification. |
| Output | Amended `F4` |
| Acceptance Criteria | §VII.F explicitly states that the phase Activity Snapshot Index follows the same sub-activity exclusion rule. Guideline version bumped. Changelog updated. |
| Status | `open` |

#### Implementation Detail

Read the existing file at `prompt/templates/consultant/workspace/guideline_workspace_plan.md`.

Apply the following targeted edits:

**1. Update the frontmatter version and date:**

Replace:
```
version: '1.18.0'
date: '2026-03-21'
```

With:
```
version: '1.19.0'
date: '2026-03-26'
```

**2. In §VII.F (Register & Placement Rules), append a clarifying bullet after the existing three bullets.**

The current §VII.F text is:
```
### F. Register & Placement Rules (Critical)

- Sub-Activities MUST NOT be registered as standalone rows in any higher-level register (Phase/Stream Activity Registers).
- Only the **parent Activity (AC00x)** is registered.
- Sub-Activities MUST be authored only inside the parent Activity section, as subheadings.
```

Replace with:
```
### F. Register & Placement Rules (Critical)

- Sub-Activities MUST NOT be registered as standalone rows in any higher-level register (Phase/Stream Activity Registers).
- Only the **parent Activity (AC00x)** is registered.
- Sub-Activities MUST be authored only inside the parent Activity section, as subheadings.
- The Phase Activity Snapshot Index (§III.B) follows the same scoping rule: only parent Activities appear as snapshot rows. Sub-Activity status is reflected through the parent Activity's `Status` per §VII.G. Consumers who need sub-activity detail MUST navigate to the Stream plan's Activity contract stub.
```

**3. Update the guideline's dedicated changelog file.**

Read the existing file at `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_plan.md`.

Append the following row as the first entry (most recent) in the changelog table:
```
| v1.19.0 | 2026-03-26 | Amendment | §VII.F: Added fourth bullet clarifying that the Phase Activity Snapshot Index follows the same sub-activity exclusion rule as registers. Phase snapshots show parent Activities only; sub-activity status is reflected through the parent Activity's status per §VII.G. Source: T103-PH000-ST000-AC000.3 planning-readiness assessment (2026-03-26). |
```

**Verification check**: After this edit, §VII.F MUST contain exactly 4 bullets. The fourth bullet MUST reference §III.B, §VII.G, and the Stream plan navigation path. The changelog file MUST have the v1.19.0 entry as the most recent row.

---

## IV. EXECUTION SEQUENCE

The SPEC items SHOULD be executed in the following order to avoid referential inconsistencies:

1. **SPEC-004** (F4) — Amend the guideline first so that subsequent plan amendments cite a current rule.
2. **SPEC-001** (F1) — Amend the stream plan Activity Register.
3. **SPEC-002** (F2) — Amend the phase plan snapshot and ST000 activity table.
4. **SPEC-003** (F3) — Amend the AC000.3 plan Context and TK002 Inputs.

## V. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| Implementation (this file) | AC000.3 planning-readiness amendments | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/implementation/implementation_T103-PH000-ST000-AC000.3_planning-readiness-amendments.md` |
| Plan | AC000.3 sub-activity plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC000.3/plan_T103-PH000-ST000-AC000.3.md` |
| Plan | ST000 stream plan | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/plan_T103-PH000-ST000.md` |
| Plan | T103 phase plan | `prompt/artifacts/tasks/T103/workspace/plan/plan_T103-PH000.md` |
| Guideline | Plan procedural guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Guideline Changelog | Plan guideline changelog | `prompt/templates/consultant/workspace/changelog/changelog_guideline_workspace_plan.md` |
| Session Notes | ST000 SES001 (2026-03-25) | `prompt/artifacts/tasks/T103/workspace/PH000/ST000/snotes/snotes_T103-PH000-ST000-SES001.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-26 | Initial | Created the AC000.3 planning-readiness amendments task specification with 4 SPEC items: SPEC-001 (stream plan Activity Register §VII.F fix), SPEC-002 (phase plan snapshot and ST000 activity table §VII.F fix), SPEC-003 (AC000.3 plan reference material enrichment), SPEC-004 (guideline §VII.F phase snapshot scoping clarification). |
