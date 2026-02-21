---
name: wrap-up
description: Use when user says wrap up, close session, end session, wrap things up, close out this task, or invokes /wrap-up — runs end-of-session checklist for shipping, memory, and self-improvement.
---

# Session Wrap-Up

Run four phases in order. Each phase is conversational and inline (no separate documents).

## Global guardrails (this repo)

- This workspace root is **not** a git repo. Do not run `git status` from the workspace root.
- This workspace contains multiple repos:
  - `prompt/` (git repo)
  - `app/` (git repo; if present)
- Run git commands from the repo root using `git -C <repo> ...`.
- **Prepare-only**: you may propose exact commands, but do **not** execute `git commit` or `git push` unless the user explicitly approves in the moment.
- **Commit scope safety (default)**: only stage/commit changes under `.claude/**` and `.agent/**` (repo-relative) when those directories exist in that repo.
  - If other files are modified, report them as **out of scope for auto-ship** and leave them untouched.

## Phase 1: Ship It

### Commit (prepare-only)

1. Run repo status:
   - `git -C prompt status -sb`
   - If `app/.git` exists: `git -C app status -sb`

2. If there are changes under `prompt/.claude/**`:
   - Propose:
     - `git -C prompt add .claude`
     - `git -C prompt commit -m "Update Claude config/skills"`
     - `git -C prompt push`

3. If there are changes under `prompt/.agent/**` (only if it exists):
      - Propose:
     - `git -C prompt add .agent`
     - `git -C prompt commit -m "Update agent config/skills"`
     - `git -C prompt push`

4. If there are changes under `app/.claude/**` or `app/.agent/**` (only if those exist):
   - Propose the same `git -C app add ...`, commit, push flow.

5. If there are changes outside `.claude/**` and `.agent/**` in either repo:
   - List them explicitly as “NOT INCLUDED (out of scope for auto-ship)”.
   - Do not stage them.

### File placement check (prepare-only)

6. If any files were created during the session, verify placement:
   - For `prompt/` repo: documentation belongs under `prompt/documentation/`
   - For `app/` repo: documentation belongs under `app/documentation/`

7. If any doc-type files exist in the repo root or code directories (`.md`, `.docx`, `.pdf`, `.xlsx`, `.pptx`) and are intended as documentation:
   - Propose `git -C <repo> mv ...` into the appropriate documentation folder.
   - Do not run the move unless user approves.

### Deploy (auto-detect only; otherwise skip)

8. Check if the project has a deploy script/skill:
   - If found, propose the exact command.
   - If not found, explicitly skip deployment (do not ask for manual steps).
222222222222222222
### Task cleanup (report-only)

9. For `prompt/` repo task tracking, use the existing plan artifacts (Activity Registers) under `prompt/artifacts/tasks/**`.
10. Report:
   - in-progress vs completed items (if clearly labeled)
   - obvious orphaned artifacts (files not linked from registers, if detectable)
   - do not edit task artifacts unless user approves.

## Phase 2: Remember It

Review what was learned during the session and suggest where it should live:

- **Auto memory** (agent memory): debugging insights, project quirks, repeated patterns.
- **`CLAUDE.md`/`AGENTS.md`**: permanent project rules and conventions.
- **`.claude/rules/`**: modular, path-scoped rules (if the directory exists; otherwise propose creating it as local-only config).
- **`CLAUDE.local.md`**: private, ephemeral notes that should not be committed.
- **`@import` references**: prefer referencing existing docs over duplication.

Output a short list of “memory candidates” with a recommended placement for each.

## Phase 3: Review & Apply (prepare-only)

Analyze the session for self-improvement findings. If nothing notable, say “Nothing to improve” and proceed.

- Findings categories: skill gap, friction, knowledge, automation.
- Action types: `CLAUDE.md`, `.claude/rules/`, auto memory, skill/hook, `CLAUDE.local.md`.

Prepare-only behavior:
- Propose the specific edits and commands.
- Wait for explicit approval before making edits or committing/pushing.

## Phase 4: Publish It (draft-only)

If publishable material exists:
- Draft the content into an appropriate “drafts” folder (do not post).
- Present title + platform + saved path and wait for user direction.

If none:
- Say “Nothing worth publishing from this.”
