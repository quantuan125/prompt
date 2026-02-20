---
artifact_type: 'NOTES'
notes_type: 'SESSION_ACTIVITY'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream: 'ST007'
activity_id: 'T104-PH001-ST007-AC001'
session: 'SES006'
version: '1.0.0'
date: '2026-02-20'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
register_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/notes_T104-PH001-ST007.md'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md'
raw_transcript_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC001/raw/raw_T104-PH001-ST007-AC001-SES006.txt'
---

# ACTIVITY SESSION NOTES: T104 (CWS) — PH001 / ST007 / AC001 / SES006 (AC001.4 Readiness Review & Convention Amendment)

## A. Agenda / Topics

1. AC001.4 plan readiness review: gap and risk assessment before developer commission
2. Convention 4 AC###/ tree: `notes_...-AC###.md` line removal
3. `verification/` and `dev-report/` placement: stream-level vs activity-level
4. `guideline_workspace_notes.md` update for `snotes_` prefix split and timeline locations
5. AC001.4 scope expansion to include verification/dev-report relocation
6. Implementation plan creation for prerequisite amendments

---

## B. Narrative Summary (Minutes-Style)

**Round 1 — AC001.4 Readiness Assessment**

The Consultant presented a readiness assessment of the AC001.4 plan (plan_T104-PH001-ST007-AC001.4.md) prior to developer commission. The assessment covered plan quality, a filesystem audit of the T104 workspace, identified gaps, and a risk assessment.

Plan quality was rated strong: governance sequencing satisfied (DEC008 precondition met — proposal at v3.2.0 approved), gated execution model in place (GATE-001 dry-run + GATE-002 live), and dependencies well-ordered (TK001→TK002→TK003→TK004→GATE-001→TK005→TK006→TK007→TK008→GATE-002→TK009).

The filesystem audit identified: 11 session notes files needing `snotes_` rename/relocation, ~6–7 `snotes/` directories to create, 7 orphaned AC-scoped files at stream root, and the `verification/` + `dev-report/` directories sitting at ST007 stream level.

Three gaps were identified: GAP-A (TK002 scope bullets under-specify GAP-005 — `dev-report/` and `verification/` not listed); GAP-B (TK002 does not explicitly call out replacing the 2-file threshold logic in `_validate_activity_threshold()`); GAP-C (ST000 orphans are in scope but were excluded from AC001.3 — widened touch surface).

Four risks were assessed: RISK-002 cumulative delta fragility (Medium, mitigated by dual-gate), reference rewrite breadth 18+ rules (Medium, mitigated by 1:1 mapping pattern), plan self-reference issue (Low), new UID-scope validator logic complexity (Low).

Overall verdict: ready for developer commission subject to three minor clarity amendments (GAP-A, GAP-B, GAP-C). The Consultant posed three questions: (Q1) amend TK002 scope before commission? (Q2) `verification/` and `dev-report/` placement? (Q3) commission scope readiness?

The Client responded: Q1 — yes, amend directly into the plan; Q2 — referred to Comment 1 below for analysis; Q3 — not yet, pending the below.

**Round 2 — Comment 1: `notes_...-AC###.md` in Convention 4 AC###/ Tree**

The Client flagged that the Convention 4 AC###/ directory tree in the proposal shows `notes_...-AC###.md` with the label "Activity notes register/index (no SES token)" and requested this be double-checked against `guideline_workspace_notes.md`, which also requires an update to clarify the difference between `notes_` and `snotes_`.

The Consultant audited the two existing files with this pattern:
- `notes_T104-PH001-ST000-AC003.md` — a legacy embedded activity notes file (title: "ACTIVITY NOTES ... Plan Amendment"), containing a single session with DPs, DECs, ACTs; NOT an index-only register.
- `notes_T104-PH001-ST001-AC003.md` — same pattern; legacy embedded activity notes.

Finding: these are pre-convention-split legacy files, covered by the guideline's forward-only rule (§1.6). No actual Activity Notes Register (index-only) exists in T104. Showing `notes_...-AC###.md` in the canonical AC###/ tree implies every activity directory should have one, which is incorrect — the register is optional (§1.3).

Recommendation: remove `notes_...-AC###.md` from Convention 4's AC###/ directory tree. The Activity Notes Register concept remains valid per guideline §1.3 but is optional; its placement is governed by the notes guideline, not the directory convention.

The Consultant also identified that `guideline_workspace_notes.md` is out of date: it still states "All files use the `notes_` prefix" (incorrect since `snotes_` approved in SES005), references `workspace/notes/PH###/ST###/` type-first locations that no longer exist after the timeline migration, and has a stale "Future ideal (deferred)" note about prefix separation — now resolved in reverse (`snotes_` was created for session notes, not `register_` for registers).

**Round 3 — Q2: `verification/` and `dev-report/` Placement**

The Client raised the placement question for `verification/` and `dev-report/`, noting that GATEs only exist at activity level per `guideline_workspace_plan.md`, so activity-level placement is more consistent.

The Consultant confirmed and elaborated:
1. GATEs are activity-scoped — `guideline_workspace_plan.md §VI.B` defines gate IDs as `<Activity-ID>-GATE-###`; no stream-level GATEs exist.
2. All existing files have AC-scoped UIDs: `verification_T104-PH001-ST007-AC001.2_gate-002.md`, `verification_T104_PH001-ST007-AC001.3_gate-001_dry-run-approval.md`, `verification_T104_PH001-ST007-AC001.3_gate-002_live-execution.md`, `dev-report_T104-PH001-ST007-AC001.2_2026-02-18.md`. The UID-scope trigger rule (DEC002) already dictates these belong in `AC###/`.
3. Consistency: `raw/` and `snotes/` already exist at both stream and activity levels; keeping `verification/` and `dev-report/` stream-only is the exact orphan pattern UID-scope was designed to eliminate.

Recommendation: move `verification/` and `dev-report/` to activity-level type dirs inside `AC###/`. Remove them from the stream-level type dir list — no stream-scoped instances exist, and on-demand creation rules already permit future stream-scoped artifacts if needed.

The Client approved the recommendation.

**Round 4 — Guideline Update Scope**

The Consultant clarified the scope of the `guideline_workspace_notes.md` update: (a) `snotes_` prefix split documented, (b) type-first locations corrected to timeline paths, (c) "Future ideal (deferred)" stale note removed, (d) Activity Notes Register §1.3 clarified as optional with correct location. The Client confirmed: both `snotes_` split and Activity Notes Register clarification, but keep it concise.

**Round 5 — Implementation Plan Commission**

The Client requested a detailed implementation plan be created at `.claude/plans/`, targeting all relevant files, so that the assistant can execute the amendments exactly. The raw transcript at `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC001/raw/raw_T104-PH001-ST007-AC001-SES006.txt` was specified to be included and referenced in the plan.

The Consultant read the stream notes register and existing plan format for consistency, then created the implementation plan at `.claude/plans/plan_T104-PH001-ST007-AC001-SES006_convention-amendments-and-ac001.4-scope-update.md` covering 6 steps (6 files), with exact find/replace text for every edit and per-step verification checklists.

---

## C. Discussion Points (DP Table)

| ID | Topic | Outcome | Rationale | Evidence |
|:--|:--|:--|:--|:--|
| `T104-PH001-ST007-AC001-SES006-DP001` | `notes_...-AC###.md` in Convention 4 AC###/ tree | Misleading; should be removed from tree | Existing files with this pattern are legacy embedded activity notes, not index-only registers per guideline §1.3; Activity Notes Register is optional | Filesystem audit: `notes_T104-PH001-ST000-AC003.md` and `notes_T104-PH001-ST001-AC003.md` are legacy files with embedded sessions |
| `T104-PH001-ST007-AC001-SES006-DP002` | `verification/` and `dev-report/` directory placement | Move to activity level (inside AC###/) as primary placement | GATEs are activity-scoped per `guideline_workspace_plan.md §VI.B`; all existing files have AC-scoped UIDs; UID-scope rule (DEC002) requires AC-scoped files in AC###/ | All 4 existing files in ST007/verification/ and ST007/dev-report/ have AC001.x UIDs |
| `T104-PH001-ST007-AC001-SES006-DP003` | `guideline_workspace_notes.md` out of date | Requires update for snotes_ prefix split, timeline locations, and Activity Notes Register clarification | Guideline says "All files use notes_ prefix" (wrong since snotes_ approved); locations reference type-first paths that no longer exist | SES005-DEC003 (snotes_ prefix), proposal v3.2.0 Convention 4 (timeline locations) |
| `T104-PH001-ST007-AC001-SES006-DP004` | AC001.4 scope expansion | Plan must be amended to include verification/dev-report relocation and clarified TK002 scope | Original plan built against v3.2.0; v3.3.0 adds activity-level verification/dev-report dirs, expanding TK001 manifest scope | AC001.4 plan review |

---

## D. Decisions Captured (DEC Table)

| ID | Decision | Type | Status | Owner | Date | Rationale | Acceptance Signal | Evidence |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| `T104-PH001-ST007-AC001-SES006-DEC001` | Remove `notes_...-AC###.md` from Convention 4 AC###/ directory tree in the proposal. Activity Notes Register placement is governed by `guideline_workspace_notes.md` (optional artifact, not standard AC###/ furniture). | Convention | `Confirmed` | Client | 2026-02-20 | Line is misleading; existing files are legacy embedded notes, not registers; register is optional per guideline §1.3 | Client QA approval (Comment 1) | SES006 discussion |
| `T104-PH001-ST007-AC001-SES006-DEC002` | Add `verification/` and `dev-report/` as activity-level type subdirectories inside `AC###/` in Convention 4. GATEs are activity-scoped; verification and dev-report evidence is co-located with the activity it governs. | Convention | `Confirmed` | Client | 2026-02-20 | GATEs are activity-scoped per guideline_workspace_plan.md §VI.B; all existing files have AC-scoped UIDs; UID-scope consistency | Client QA approval (Q2 recommendation) | SES006 discussion |
| `T104-PH001-ST007-AC001-SES006-DEC003` | Remove `verification/` and `dev-report/` from stream-level type subdirectory list in Convention 4. Stream-level placement remains valid via on-demand creation rules if future stream-scoped artifacts arise, but is not listed as a canonical type dir. | Convention | `Confirmed` | Client | 2026-02-20 | No stream-scoped instances exist; keeping in stream-level list creates inconsistency with UID-scope principle | Client QA approval (Q2 recommendation) | SES006 discussion |
| `T104-PH001-ST007-AC001-SES006-DEC004` | Update `guideline_workspace_notes.md` to: (a) document `snotes_` prefix for session notes, (b) update file locations from type-first to timeline paths, (c) resolve "Future ideal (deferred)" note, (d) clarify Activity Notes Register as optional with updated location. Scope: concise, both snotes_ split and Activity Notes Register clarification. | Governance | `Confirmed` | Client | 2026-02-20 | Guideline is out of date with approved convention changes (SES005-DEC003, SES005-DEC005) | Client QA approval (Q2 + Comment 1) | SES006 discussion |
| `T104-PH001-ST007-AC001-SES006-DEC005` | Amend AC001.4 plan to align with proposal v3.3.0: expand TK001 scope (verification/dev-report file relocation), expand TK002 scope (explicit GAP-005 bullets + UID-scope threshold replacement), update references from v3.2.0 to v3.3.0. | Process | `Confirmed` | Client | 2026-02-20 | AC001.4 manifest must be built against the current authority surface (DEC008 governance constraint) | Client QA approval (Q1 + Q3) | SES006 discussion |

---

## E. Actions / Carry-Forward (ACT Table)

| ID | Action | Owner | Status |
|:--|:--|:--|:--|
| `T104-PH001-ST007-AC001-SES006-ACT001` | Create SES006 session notes file (this file) | LLM_Consultant | `completed` |
| `T104-PH001-ST007-AC001-SES006-ACT002` | Create implementation plan at `.claude/plans/plan_T104-PH001-ST007-AC001-SES006_convention-amendments-and-ac001.4-scope-update.md` | LLM_Consultant | `completed` |
| `T104-PH001-ST007-AC001-SES006-ACT003` | Amend proposal → v3.3.0 (DEC001, DEC002, DEC003) | LLM_Consultant | `pending` |
| `T104-PH001-ST007-AC001-SES006-ACT004` | Update `guideline_workspace_notes.md` (DEC004) | LLM_Consultant | `pending` |
| `T104-PH001-ST007-AC001-SES006-ACT005` | Amend AC001.4 plan (DEC005) | LLM_Consultant | `pending` |
| `T104-PH001-ST007-AC001-SES006-ACT006` | Update stream notes register with SES006 entry | LLM_Consultant | `pending` |
| `T104-PH001-ST007-AC001-SES006-ACT007` | Update stream plan: authority surface version + SES006 Links Register entry | LLM_Consultant | `pending` |

---

## F. Open Questions Register (OQ Table)

*None — all items resolved in session.*

---

## G. Session Handoff Pack

- **Key outcome**: 5 decisions approved (DEC001–DEC005) as prerequisite amendments before AC001.4 developer commission.
- **Proposal amendment**: v3.2.0 → v3.3.0 — `verification/` and `dev-report/` moved to activity level; `notes_...-AC###.md` removed from AC###/ tree.
- **Guideline update**: `snotes_` prefix documented; timeline locations corrected; Activity Notes Register clarified as optional.
- **AC001.4 scope expanded**: TK001 now includes verification/dev-report file relocation; TK002 scope explicitly covers GAP-005 and threshold replacement.
- **Implementation plan**: `.claude/plans/plan_T104-PH001-ST007-AC001-SES006_convention-amendments-and-ac001.4-scope-update.md`

---

## H. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-20 | Initial | Session notes created: AC001.4 readiness review, Convention 4 amendments (verification/dev-report to activity level, notes_...-AC###.md removal), guideline update scope, AC001.4 plan expansion. 5 decisions captured (DEC001–DEC005). |
