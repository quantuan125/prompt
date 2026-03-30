---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-TK004'
version: '1.0.0'
date: '2026-03-30'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
execution_audience: 'assistant'
purpose: 'Detailed post-gate execution specification for AC006 session-close skill hardening, including skill rewrite, dual-symlink reachability, explicit snotes guidance, and lower-intelligence assistant scaffolding.'
---

# IMPLEMENTATION (Task Specification): AC006 Session-Close Hardening

## I. PURPOSE & AUTHORITY
- Purpose: Specify the exact downstream execution required to harden `prompt/skills/session-close/SKILL.md` after `GATE-001` approval.
- Authority chain: The AC006 plan defines the execution boundary -> the AC004 session-close standards-input proposal defines the inherited session-close convention -> the AC006 TK001 audit defines the additional briefing/snotes gaps -> this artifact specifies HOW the assistant executes `TK007`.
- Audience: `LLM_Assistant`
- This artifact does NOT hold a GDR. Execution under this artifact MUST NOT begin until `P-PH000-ST002-AC006-GATE-001` records an approving client decision.
- The live `prompt/skills/session-close/SKILL.md` remains the downstream operationalization target. The approved behavior boundary comes from AC004 authority plus the AC006-approved hardening scope, not from the current live file contents alone.

## II. TASK SCOPE
- Governing plan task: `P-PH000-ST002-AC006-TK004`
- Trigger: TK001 established that the current `session-close` skill is too thin, not operationally reachable, and lacks explicit snotes guidance and lower-intelligence assistant scaffolding.
- Deliverable contract:
  - updated `prompt/skills/session-close/SKILL.md`
  - created `.agents/skills/session-close` symlink
  - created `.claude/skills/session-close` symlink
  - validated skill reachability and guidance completeness

## III. SPECIFICATION ITEMS

### SPEC-001 - Rewrite the session-close skill to the approved AC006 boundary

| Field | Detail |
|:--|:--|
| Requirement Source | AC004 session-close standards-input proposal; AC006 TK001 gap audit; AC006 plan TK004 contract |
| Target file(s) | `prompt/skills/session-close/SKILL.md` |
| Required end-state posture | The skill becomes a bounded consultant/assistant execution surface that preserves the consultant-led closeout boundary while adding explicit authority-chain language, snotes authoring guidance, surface-reconciliation logic, and lower-intelligence assistant scaffolding. |
| Explicit non-target / do-not-change constraints | Do NOT broaden the skill into general wrap-up. Do NOT add automation, hooks, scripts, or repo-wide session management. Do NOT edit `prompt/skills/wrap-up/SKILL.md`. |
| Validation check | The resulting skill explicitly references the notes guideline, the status protocol, the authority chain, the closeout workflow, and the notes-register update path, while preserving the manual-only boundary and the non-goals. |
| Blocking ambiguity rule | If any requested skill behavior would broaden the surface beyond session-close, status-surface reconciliation, and snotes closeout guidance, stop and escalate instead of inferring extra scope. |
| Status | `open` |

#### Implementation Detail

1. Replace the current `prompt/skills/session-close/SKILL.md` body with a richer skill that still uses the same `name: session-close` frontmatter key and remains clearly bounded to governed session closeout work.
2. Update the frontmatter description to state that the skill is for governed consultation-session closeout, status-surface reconciliation, and snotes handoff preparation.
3. The rewritten skill body must contain these sections in order:
   - `# Session Close`
   - `## Use Conditions`
   - `## Authority Chain`
   - `## Closeout Workflow`
   - `## Snotes Guidance`
   - `## Lower-Intelligence Assistant Checklist`
   - `## Non-goals`
4. In `## Use Conditions`, state all of the following:
   - the skill is used when a governed AC006-style consultation or execution session is ending
   - the acting executor may be the main consultant or an explicitly commissioned assistant acting under consultant authority
   - the skill is a manual reminder/guidance surface only
5. In `## Authority Chain`, explicitly name:
   - the inherited AC004 session-close standards-input proposal as the convention source
   - `prompt/artifacts/tasks/P/status/status_program.md` Section 7 as the status-reconciliation protocol source
   - `prompt/templates/consultant/workspace/guideline_workspace_notes.md` as the snotes authoring source
6. In `## Closeout Workflow`, include a numbered sequence that instructs the executor to:
   - identify whether the session touched `status_program.yaml`, `status_program.md`, stream/phase plans, roadmap, gate-disposition surfaces, or governed workspace artifacts
   - reconcile status surfaces when lifecycle, dependency, gate, or stale-state triggers were touched
   - determine whether a new `snotes_` file or a session-note amendment is required
   - update the appropriate notes register when a new session note is created
   - prepare a short handoff pack summarizing current scope, decisions, pending actions, and open questions
7. In `## Snotes Guidance`, add step-by-step instructions that explicitly require:
   - choosing the correct session-notes surface under `prompt/artifacts/tasks/.../snotes/`
   - using the `guideline_workspace_notes.md` structure and the `A` through `H` sections
   - populating DP / DEC / ACT / OQ tables when the session produced decisions or carry-forward items
   - keeping the session handoff pack aligned with the ACT and OQ tables
8. In `## Lower-Intelligence Assistant Checklist`, provide explicit if/then checks such as:
   - if you changed the status ledger, also refresh the derived narrative
   - if you created or amended a governed session note, verify the notes register
   - if you changed plan/gate state, verify downstream blocking statements still match the gate posture
   - if you touched a package-facing proposal or implementation artifact, verify the evidence references still resolve
9. In `## Non-goals`, preserve and tighten the current boundary:
   - do not duplicate wrap-up responsibilities
   - do not create hooks, scripts, or repo-wide automation
   - do not broaden the skill into general session management
   - do not introduce client-facing briefing generation into this skill
10. Add one short note that the environment's `skill-creator` reference should be used during rewrite authoring, and that writing-skill assistance may be used if available in the execution environment, but the resulting file must still conform to this exact specification.

### SPEC-002 - Create dual symlink reachability for the session-close skill

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 TK001 GAP-001; AC006 plan TK007 execution contract |
| Target file(s) | `.agents/skills/session-close`; `.claude/skills/session-close` |
| Required end-state posture | Both skill-resolution roots expose `session-close` exactly as `wrap-up` is currently exposed, so the skill can be invoked and tested through normal resolution paths. |
| Explicit non-target / do-not-change constraints | Do NOT modify the `wrap-up` symlinks. Do NOT create duplicate nested folders inside `prompt/skills/session-close`. |
| Validation check | Directory listing or equivalent path inspection confirms both symlinks exist and resolve to the same `prompt/skills/session-close` directory. |
| Blocking ambiguity rule | If either root uses a different local symlink convention than expected at execution time, mirror the existing `wrap-up` pattern exactly and do not invent a new layout. |
| Status | `open` |

#### Implementation Detail

1. Inspect the existing `wrap-up` entries in `.agents/skills/` and `.claude/skills/` before creating anything.
2. Create `.agents/skills/session-close` as a symlink that mirrors the same relative-target pattern already used for `wrap-up`.
3. Create `.claude/skills/session-close` using the same mirror rule.
4. Do not move or rename `prompt/skills/session-close/`.
5. After creation, verify that both roots resolve to the same `SKILL.md`.

### SPEC-003 - Validate the hardened skill against the AC006 execution boundary

| Field | Detail |
|:--|:--|
| Requirement Source | AC006 plan TK004 success criteria; TK001 audit GAP-001 through GAP-005 |
| Target file(s) | `prompt/skills/session-close/SKILL.md`; `.agents/skills/session-close`; `.claude/skills/session-close` |
| Required end-state posture | The hardened skill is reachable, clearly bounded, and complete enough for downstream assistant execution without requiring architectural inference. |
| Explicit non-target / do-not-change constraints | Do NOT perform broader status-surface edits in this validation step. Do NOT author new notes or proposals during validation. |
| Validation check | Confirm that the rewritten skill contains the required sections and that the symlink roots resolve correctly. |
| Blocking ambiguity rule | If the rewritten skill fails validation, fix only the missing AC006-required detail; do not broaden the skill or touch unrelated surfaces. |
| Status | `open` |

#### Implementation Detail

1. Read the final `prompt/skills/session-close/SKILL.md` top to bottom.
2. Verify that it explicitly covers:
   - authority chain
   - status-surface reconciliation
   - snotes authoring guidance
   - notes-register update logic
   - lower-intelligence assistant checklist
   - non-goals
3. Verify that both symlink roots resolve to the same live file.
4. If any required section is missing, patch only that missing detail before marking execution complete.

## IV. IMPLEMENTATION SEQUENCE
1. Rewrite the skill file.
2. Create both symlinks.
3. Perform the validation pass.
4. Record execution evidence in the later downstream handoff/reporting surface.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| TK001 Audit | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_session-close-and-briefing-gap-audit.md` |
| AC004 Standards Input | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| Skill-Creator Reference | `/home/quantuan125/.codex/skills/.system/skill-creator/SKILL.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-30 | Initial | Authored the AC006 session-close hardening execution specification covering the rewritten skill contract, dual-symlink reachability, explicit snotes guidance, and lower-intelligence assistant scaffolding. |
