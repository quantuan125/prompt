# Workspace Templates

This directory contains generic structural templates for workspace artifacts used in the consultancy workflow.

## Available Templates

### `template_workspace_plan.md`

**Purpose**: Generic structural template for PLAN workspace files that provide phase governance for epic/feature development.

**When to Use**:
- Creating initiative-level phase plans
- Creating epic-level phase plans
- Creating feature-level phase plans

**Key Features**:
- YAML frontmatter with metadata fields
- Executive summary with role boundaries
- Context materials & prerequisites section
- Multi-subphase structure with activity registers
- Success criteria checklists at activity, subphase, and phase levels
- Workspace file register for traceability
- Links register for artifact relationships
- Changelog for version tracking

**Structural Reference**:
Based on `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` as the exemplar.

**Compliance**:
- Follows T102 artifact standards (YAML header, Links Register, Changelog)
- References T102-ADR-004 through T102-ADR-007 for governance compliance
- Aligns with `workspace_documentation_rules.md` (Plans are roadmaps only; no full RID/DR bodies)

**Usage Notes**:
1. Replace all placeholder values in `[BRACKETS]` with actual values
2. Remove sections not applicable to your phase scope
3. Customize subphase count (template shows 5 subphases as pattern)
4. Add instructional comments in `<!-- -->` blocks as needed
5. Keep plan concise by referencing proposal/completion files for detailed content

## Governance Principles

Per `prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md`:

**Plan Role**: Roadmap and phase gating; keeps activities, deliverables, gates, and short phase-level status. No per-activity execution logs; no F-RID/E-RID bodies.

**Canonical Sources**:
- **Roadmap**: Plan only
- **Normative Requirements**: Request + Proposal (during active phase)
- **Execution History**: Completion file only

**Anti-Drift Safeguards**:
- Never duplicate full specs across artifacts; always cite IDs
- Keep Plan phase status concise; defer all detail to Completion/Proposal
- Reference by ID and section instead of pasting full bodies

## Markdown Heading Hierarchy

Plans use the following heading hierarchy:

- `##` Phase (Roman Numerals: I., II., III.)
- `###` Subphase (Capital Letters: A., B., C.)
- `####` Planned Activities (Numbers: 1., 2., 3.)
- `#####` Activity (Lowercase Roman: i., ii., iii.)

Below headings, use bullet points (`*`, `-`, `+`) for additional nesting.
