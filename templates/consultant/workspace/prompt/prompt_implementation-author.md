<!--
  RECYCLABLE PROMPT: Implementation Author

  Purpose: Commission the authoring of an IMPLEMENTATION `task_specification` artifact.
  When to use: A consultant uses this prompt when a plan task's complexity exceeds
  plan-step capacity and requires a detailed implementation specification before
  developer execution can begin.

  This prompt is NOT a governed artifact. It has no YAML frontmatter or versioning.
  For the companion execution prompt, see: prompt_implementation-execute.md
-->

# Commission: Author IMPLEMENTATION Task Specification

You are commissioned to author an IMPLEMENTATION `task_specification` artifact for the following task.

## Context to Read First

Before authoring, read the following materials:

1. **Governing plan**: `<governing_plan_path>`
2. **Governing plan task**: `<task_id>` (the specific task row that authorizes this work)
3. **Implementation guideline**: `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`
4. **Task specification template**: `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`
5. **Any additional context files**: `<additional_context_paths>`

## Output Path

Author the artifact at:

```
prompt/artifacts/tasks/<INITIATIVE>/workspace/<PHASE>/<STREAM>/<ACTIVITY>/implementation/implementation_<ACTIVITY-UID>_<kebab-topic>.md
```

Create the `implementation/` directory if it does not exist.

**Do NOT create a file in `.claude/plans/`.** The IMPLEMENTATION artifact is the governed specification surface for T104-governed activities. The `.claude/plans/` pattern is deprecated for governed work (GIR-007).

## Frontmatter Requirements

Include all required frontmatter fields per `guideline_workspace_implementation.md` §V:

- `artifact_type: 'IMPLEMENTATION'`
- `implementation_type: 'task_specification'`
- `initiative_id`, `initiative_code`, `phase`, `stream_id`, `activity_id`
- `task_id` (the plan task this artifact specifies)
- `version: '1.0.0'`
- `date` (today's date)
- `status: 'draft'`
- `author` (your role)
- `decision_owner_role: 'Client'`
- `plan_reference` (repo-relative path to the governing plan)
- `purpose` (1-line description of what this specification covers)
- `execution_audience` (either `'developer'` or `'consultant'` -- determines whether downstream evidence is DEV-REPORT or session notes)

## Required Sections

### I. Purpose & Authority
- State the purpose of this specification
- Declare the authority chain: Plan --> this artifact --> downstream evidence surface
  - If `execution_audience: 'developer'`: evidence surface is DEV-REPORT
  - If `execution_audience: 'consultant'`: evidence surface is session notes (no DEV-REPORT per `guideline_workspace_dev-report.md` §III.A)
- State the audience (executing role)
- Note that this artifact does NOT hold a GDR
- Include a `Trigger` statement explaining why this task requires an IMPLEMENTATION artifact (e.g., "Task complexity exceeds plan-step capacity" or use a specific trigger condition)

### II. Task Scope
- Reference the governing plan task ID
- State the trigger for this work
- Summarize the deliverable contract
- List dependencies

### III. Context & Rationale (if needed)
- Background information the executing agent needs
- Decisions already approved that constrain the specification

### IV. Specification Items
- Number each item as `SPEC-###`
- For each SPEC item, use the **hybrid structure**:
  1. **Metadata table** with fields: Requirement Source, Template/Target, Output, Acceptance Criteria, Status
  2. **`#### Implementation Detail`** section below the table with structured prose (headings, lists, code blocks as needed)
- For conditional SPEC items, include a `Trigger` field in the metadata table stating the condition under which this item is executed
- Requirement Source values MUST use P-STD-005 compliant references (e.g., `SES001-DEC003` for same-activity scope)

### V. Implementation Sequence
- List SPEC items in execution order
- Note parallelism constraints and dependencies

### VI. Target Files Register
- Table with columns: #, File Path, Authority, Change Type, Confirmed?
- Enumerate every file that will be created or amended

### VII. References
- Table linking all referenced documents

### VIII. Changelog
- Initial entry: `v1.0.0 | <date> | Initial | <summary>`

## Quality Checklist

Before submitting, verify:
- [ ] All SPEC items have Requirement Source, Acceptance Criteria, and Status fields
- [ ] Implementation Sequence covers all SPEC items
- [ ] Target Files Register is complete and matches SPEC item outputs
- [ ] Authority chain in §I correctly reflects the `execution_audience` setting
- [ ] No file is created in `.claude/plans/`
