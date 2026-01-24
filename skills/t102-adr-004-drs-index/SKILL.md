---
name: t102-adr-004-drs-index
description: Use when working with files under prompt/ and you need to author, validate, or update Decision Records Index (GDR/ADR) tables and Decision Record body sections according to T102-ADR-004 (Decision Records Index). If RID-style formal references are required, invoke the t102-adr-005-id-spec skill workflow.
allowed-tools: Bash, Read, Grep, Glob
---

# T102-ADR-004 Decision Records Index (DR Index + DR Body)

## Core intent

Apply `T102-ADR-004 (Decision Records Index)` as the single source of truth for Decision Records Index (GDR/ADR) schema, placement, body headings, anchors, and cross-artifact linking patterns.

This skill is intentionally procedural and SSOT-first:
- Do not paraphrase or restate ADR-004 rules in this file (avoid drift).
- Always print ADR-004 and treat the printed output as normative.

## Hard scope gate (prompt-only)

Before using any ADR-004 rules from this skill, confirm the files being created/edited are under `prompt/`.

If the target files are not under `prompt/`, stop and ask for confirmation before applying ADR-004 rules in non-`prompt/` contexts.

## Mandatory first step (view only `T102-ADR-004`)

Do not rely on memory or paraphrase. Always load the current `T102-ADR-004` block:

Run:
- `python3 prompt/skills/t102-adr-004-drs-index/scripts/print_t102_adr_004.py`

Use the printed output as the authoritative reference for the rest of the task. Do not read or quote other sections of the Concept document unless explicitly requested.

## Operational workflow (SSOT-first)

Workflow:
1) Confirm **hard scope gate**: you are creating/editing files under `prompt/`.
2) Print `T102-ADR-004` using the script above.
3) Identify what you are doing: **creating**, **updating**, or **reviewing** a DR Index entry or DR body section.
4) Apply the relevant rules directly from the printed `T102-ADR-004` text (cite the exact heading/bullet from the printed output when enforcing a constraint).

## RID formal references (delegation to ADR-005)

If ADR-004 requires RID-style **formal** references governed by `T102-ADR-005` (e.g., "References include formal reference following T102-ADR-005…"):

1) Explicitly invoke the ADR-005 skill workflow (`t102-adr-005-id-spec`).
2) Print ADR-005:
   - `python3 prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
3) Apply ADR-005’s normative rules for RID construction and formal reference formatting.

Do not duplicate ADR-005 rules here.

## Action mapping (general)

Use this mapping only to decide where to look in the printed ADR-004 block. Treat the printed ADR as normative; treat this section as a workflow aide.

### A) Create/update a DR Index table row

- Confirm the index table schema matches the ADR (columns, ordering, allowed values).
- Ensure IDs, anchors, and status values conform to the ADR’s constraints.
- Ensure placement standards match the artifact type rules in ADR-004.

### B) Create/update a DR body section

- Confirm the body list-item header pattern and anchor formatting match the ADR.
- Confirm required subheadings exist and follow the ADR’s required formatting.
- Confirm cross-artifact linking statements follow ADR-004’s required patterns.

## Red flags (STOP)

- You did not print `T102-ADR-004` first.
- Target files are outside `prompt/`.
- You are about to invent local deviations to the schema/headings because “it’s close enough”.

