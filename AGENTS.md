---
artifact_type: 'AGENT_GUIDANCE'
scope: 'prompt'
applies_to: 'prompt/**'
version: '1.1.0'
date: '2026-03-20'
authority: 'P-STD-001'
---

# Prompt System Development

This directory contains the agentic workflow system for multi-role LLM collaboration.

## Purpose
Design and maintain consultant, planner, developer, and reviewer role configurations that orchestrate structured problem-solving workflows.

## Scope & Authority
- This file is the scoped governance surface for `prompt/**`.
- Same-family guidance inside `prompt/` takes precedence over broader same-family routing when both apply.
- This file is not a wrapper and therefore does not declare `delegates_to`.
- `AGENTS.md` at the repo root, `.claude/CLAUDE.md`, and role `CLAUDE_*` wrappers remain explicit deferred surfaces outside AC009 scope.

## Primary Focus
Currently developing consultant and developer modes with emphasis on Socratic exploration and systematic implementation practices.

## Standards Authoring
- All combined standard-specification files MUST be authored using:
  - **Guideline**: `prompt/templates/consultant/standards/guideline_standard_specs.md`
  - **Template**: `prompt/templates/consultant/standards/template_standard_specs.md`
- The guideline and template are governed by `P-STD-001` (Program Governance Standard) at `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`.
- Per `P-STD-001-CLAUSE-005B`, any CLAUSE modification in `P-STD-001` requires updating these derivatives in the same changeset.
- `P-STD-001-CLAUSE-031` through `P-STD-001-CLAUSE-036` now govern the standard-file metadata layer: YAML frontmatter is the current-state authority; `## Provenance` is the history / lineage authority.
- `P-STD-001-CLAUSE-008` governs normative drafting vocabulary at program scope. New normative text should use the BCP 14 primary vocabulary set (`MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, `MAY`).

## Advisory: P-STD-001 Authority & Alias Window
- `P-STD-001` (Program Governance Standard) is the authoritative standard for combined standard-specification file authoring.
- During the alias window, legacy `T102-STD-004-CLAUSE-*` references MAY appear for compatibility; new or updated references MUST use `P-STD-001-CLAUSE-*`.
- For combined standard files, the current rationale record MUST use nested DR form: `<STD-ID>-ADR-###`.

## Program Standards Registry

The following program-level standards are authoritative governance surfaces. All agents MUST reference these when working in their respective domains:

| Standard | Title | Domain | Canonical Path |
|:--|:--|:--|:--|
| `P-STD-001` | Program Governance Standard | Combined standard-specification file authoring | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| `P-STD-002` | Program Status Standard | Status vocabulary, health assessment, dependency visibility, update protocol | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` |
| `P-STD-004` | File Naming & Directory Convention | Directory structure, file naming, archival rules | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| `P-STD-005` | Universal ID Specification | Workscope ID governance, timeline UID convention | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |

- `P-STD-003` is deprecated (placeholder ID reserved; no active standard).
- For status values in workspace plans, defer to `P-STD-002` canonical lifecycle states.
- For ID construction and reference semantics, defer to `P-STD-005`.
- For directory placement and file naming, defer to `P-STD-004`.

## Git Operations
- The git repository root for this workspace is `prompt/`.
- Run git commands from `prompt/` (or use `git -C prompt ...`) to avoid operating outside the repository.

## Testing and TDD
- For any testing related to files under `prompt/`, use the workspace-root virtual environment at `venv/`.
- Preferred command form from the workspace root is `venv/bin/python -m pytest ...`.
- If your shell is already inside `prompt/`, use the equivalent `../venv/bin/python -m pytest ...`.
- For `prompt/scripts/` changes, the default regression command is `venv/bin/python -m pytest -q prompt/scripts/tests`.
- In TDD workflows, run the smallest relevant pytest target first, verify the red/green cycle, then rerun the broader affected suite in the same `venv` before completion claims.
