# Prompt System Development

This directory contains the agentic workflow system for multi-role LLM collaboration.

## Purpose
Design and maintain consultant, planner, developer, and reviewer role configurations that orchestrate structured problem-solving workflows.

## Primary Focus
Currently developing consultant and developer modes with emphasis on Socratic exploration and systematic implementation practices.

## Standards Authoring
- All combined standard-specification files MUST be authored using:
  - **Guideline**: `prompt/templates/consultant/standards/guideline_standard_specs.md`
  - **Template**: `prompt/templates/consultant/standards/template_standard_specs.md`
- The guideline and template are governed by `P-STD-001` (Program Governance Standard) at `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`.
- Per `P-STD-001-CLAUSE-005B`, any CLAUSE modification in `P-STD-001` requires updating these derivatives in the same changeset.

## Advisory: P-STD-001 Authority & Alias Window
- `P-STD-001` (Program Governance Standard) is the authoritative standard for combined standard-specification file authoring.
- During the alias window, legacy `T102-STD-004-CLAUSE-*` references MAY appear for compatibility; new or updated references MUST use `P-STD-001-CLAUSE-*`.
- For combined standard files, the current rationale record MUST use nested DR form: `<STD-ID>-ADR-###`.

## Git Operations
- The git repository root for this workspace is `prompt/`.
- Run git commands from `prompt/` (or use `git -C prompt ...`) to avoid operating outside the repository.

## Testing and TDD
- For any testing related to files under `prompt/`, use the workspace-root virtual environment at `venv/`.
- Preferred command form from the workspace root is `venv/bin/python -m pytest ...`.
- If your shell is already inside `prompt/`, use the equivalent `../venv/bin/python -m pytest ...`.
- For `prompt/scripts/` changes, the default regression command is `venv/bin/python -m pytest -q prompt/scripts/tests`.
- In TDD workflows, run the smallest relevant pytest target first, verify the red/green cycle, then rerun the broader affected suite in the same `venv` before completion claims.
