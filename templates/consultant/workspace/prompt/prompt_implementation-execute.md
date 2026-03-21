<!--
  RECYCLABLE PROMPT: Implementation Execute

  Purpose: Commission the execution of an existing IMPLEMENTATION `task_specification` artifact.
  When to use: A consultant or orchestrator uses this prompt to commission a developer/agent
  to execute an already-authored IMPLEMENTATION artifact. The artifact must exist before
  this prompt is used.

  This prompt is NOT a governed artifact. It has no YAML frontmatter or versioning.
  For the companion authoring prompt, see: prompt_implementation-author.md

  Note: This prompt replaces the old `.claude/plans` recycle pattern for T104-governed
  activities. The `.claude/plans/` pattern is deprecated for governed work (GIR-007).
-->

# Commission: Execute IMPLEMENTATION Task Specification

Please perform the implementation as EXACTLY as outlined in this IMPLEMENTATION artifact at `<implementation_artifact_path>`.

## Instructions

1. **Read the artifact** at `<implementation_artifact_path>` and all referenced context materials (governing plan, guidelines, templates, any files listed in §VII References) before beginning execution.

2. **Check the `execution_audience` frontmatter field** in the artifact:
   - If `execution_audience: 'developer'` (or omitted -- developer is the default): Record all changes in a **DEV-REPORT** artifact per `guideline_workspace_dev-report.md`. The DEV-REPORT is the downstream evidence surface.
   - If `execution_audience: 'consultant'`: The downstream evidence surface is **session notes**, not DEV-REPORT. Do NOT produce a DEV-REPORT (per `guideline_workspace_dev-report.md` §III.A -- consultation-only gates with no developer-mutated deliverables MUST NOT produce a DEV-REPORT).

3. **Execute each SPEC-### item** in the order specified by the **Implementation Sequence** (§V of the artifact). Respect any dependency or parallelism constraints noted there.

4. **For each SPEC item**:
   - Read the metadata table (Requirement Source, Template/Target, Output, Acceptance Criteria)
   - Read the Implementation Detail section
   - Execute the specified work
   - **Verify the Acceptance Criteria** before proceeding to the next SPEC item
   - If a SPEC item has a `Trigger` condition, check whether the condition is met before executing

5. **For conditional SPEC items** (those with a `Trigger` field): If the trigger condition is not met, skip the item and note it as `skipped (trigger not met)` in the evidence surface.

6. **Target Files Register** (§VI): Use this as your checklist. Every file listed should be created or amended as specified. Do not modify files not listed in the register unless the SPEC item explicitly authorizes it.

## Evidence Surface

- **Developer execution**: Produce a DEV-REPORT artifact at the canonical path (`<activity>/dev-report/dev-report_<activity-UID>_<kebab-topic>.md`). Include a traceability matrix mapping each deliverable back to its SPEC item ID.
- **Consultant execution**: Evidence is recorded in session notes. No DEV-REPORT is produced.

## Important Notes

- This prompt replaces the old `.claude/plans` recycle pattern for T104-governed activities.
- Do NOT create files in `.claude/plans/` as part of governed execution.
- The IMPLEMENTATION artifact is the single source of specification authority. If there is a conflict between the artifact and any other surface, the artifact governs.
