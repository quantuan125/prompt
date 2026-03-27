---
name: session-close
description: Use for consultant-led consultation-session closeout and status-surface verification when a governed consultation session is ending.
---

# Session Close

Use this skill only when the acting role is `LLM_Consultant` and the session being closed is a governed consultation session.

## Closeout checks

1. Check whether the session changed `status_program.yaml`, `status_program.md`, the stream plan, the phase plan, the roadmap, or any gate-disposition surface.
2. If any lifecycle, gate, dependency, or stale-state trigger was touched, reconcile the status surfaces before ending the session.
3. Use `prompt/artifacts/tasks/P/status/status_program.md` Section 7 as the governing protocol for the reconciliation step.
4. Treat `prompt/skills/wrap-up/SKILL.md` as historical-only context for AC004 V1 reminder governance.
5. Treat this skill as a manual reminder surface only; do not implement it through hooks, scripts, or repo-wide automation in AC004 V1.

## Non-goals

- Do not duplicate wrap-up responsibilities.
- Do not create hooks, scripts, or repo-wide automation.
- Do not broaden this skill beyond consultant-led consultation-session closeout.
- Do not broaden this skill into general session management beyond status-surface verification and reconciliation.
