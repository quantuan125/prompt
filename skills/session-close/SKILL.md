---
name: session-close
description: Use at session closeout to verify whether status surfaces were affected and reconcile them if lifecycle, gate, dependency, or stale-state triggers were touched.
---

# Session Close

Use this skill when a session is ending and the work may have touched governed status surfaces.

## Closeout checks

1. Check whether the session changed `status_program.yaml`, `status_program.md`, the stream plan, the phase plan, the roadmap, or any gate-disposition surface.
2. If any lifecycle, gate, dependency, or stale-state trigger was touched, reconcile the status surfaces before ending the session.
3. Use `prompt/artifacts/tasks/P/status/status_program.md` Section 7 as the governing protocol for the reconciliation step.
4. Treat `prompt/skills/wrap-up/SKILL.md` as historical-only context for AC004 V1 reminder governance.

## Non-goals

- Do not duplicate wrap-up responsibilities.
- Do not create repo-wide automation.
- Do not broaden this skill into general session management beyond status-surface verification and reconciliation.
