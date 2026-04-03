---
name: session-close
description: Use for governed consultation-session closeout and status-surface reconciliation when a session is ending.
---

# Session Close

Use this skill when a governed consultation or execution session is ending and the acting executor is either the main consultant or a consultant-commissioned assistant.

## Use Conditions

- Use this skill only for governed session closeout work.
- Use this skill when the session touched status surfaces, gate surfaces, plan surfaces, or governed workspace artifacts that may need reconciliation.
- Use this skill as a manual reminder and guidance surface only.
- Use this skill when the acting executor is the main consultant or a commissioned assistant acting under consultant authority.

## Authority Chain

- Inherited session-close convention source: `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC004/proposal/proposal_P-PH000-ST002-AC004-TK003.8_session-close-standards-input.md`
- Status reconciliation protocol source: `prompt/artifacts/tasks/P/status/status_program.md` Section 7
- Session notes authoring source: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
- During rewrite authoring, use the environment's skill-creator reference if available, and use writing-skill assistance if available, but keep the final behavior within this exact boundary.

## Closeout Workflow

1. Identify whether the session touched `status_program.yaml`, `status_program.md`, stream plans, phase plans, the roadmap, gate-disposition surfaces, or governed workspace artifacts.
2. If any lifecycle, dependency, gate, or stale-state trigger was touched, reconcile the affected status surfaces before closing the session.
3. Decide whether the session requires a new `snotes_` file or an amendment to an existing session note.
4. If a new session note is created, update the applicable notes register so the new session is discoverable.
5. Prepare a short handoff pack that summarizes current scope, decisions, pending actions, and open questions.
6. Do not infer broader automation, wrap-up, or session-management behavior beyond the checks above.

## Snotes Guidance

1. Choose the correct session-notes surface under `prompt/artifacts/tasks/.../snotes/` for the session scope.
2. Use `guideline_workspace_notes.md` and the `A` through `H` section structure for the session note.
3. Populate `DP`, `DEC`, `ACT`, and `OQ` tables when the session produced decisions or carry-forward items.
4. Keep the handoff pack aligned with the `ACT` and `OQ` tables.
5. Use session-scoped IDs that include the `SES###` token.

## Lower-Intelligence Assistant Checklist

- If you changed the status ledger, also refresh the derived narrative so the two surfaces do not diverge.
- If you created or amended a governed session note, verify the notes register row exists or is updated.
- If you changed plan or gate state, verify the downstream blocking statements still match the current gate posture.
- If you touched a package-facing proposal or implementation artifact, verify the evidence references still resolve.
- If a check fails, stop and fix the specific inconsistency rather than broadening scope.

## Non-goals

- Do not duplicate wrap-up responsibilities.
- Do not create hooks, scripts, or repo-wide automation.
- Do not broaden this skill into general session management.
- Do not broaden this skill into client-facing briefing generation.
- Do not use it to replace proposal, analysis, verification, or implementation authority.
