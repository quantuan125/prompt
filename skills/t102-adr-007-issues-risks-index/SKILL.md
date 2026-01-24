---
name: t102-adr-007-issues-risks-index
description: Use when working with files under prompt/ and you need to create, validate, or update Issues & Risks sections/tables (schemas, enums, notes/date coupling, cross-scope promotion) according to T102-ADR-007. If ID/RID formatting is required, invoke the t102-adr-005-id-spec skill workflow.
allowed-tools: Bash, Read, Grep, Glob
---

# T102-ADR-007 Issues & Risks Log Standard (Issues/Risks sections)

## Core intent

Apply `T102-ADR-007 (Issues & Risks Index)` as the single source of truth for Issues & Risks section naming/placement, table schemas, status/priority enums, required notes/date coupling rules, and cross-scope promotion/de-duplication guidance.

This skill is intentionally procedural and SSOT-first:
- Do not paraphrase or restate ADR-007 rules in this file (avoid drift).
- Always print ADR-007 and treat the printed output as normative.

## Hard scope gate (prompt-only)

Before using any ADR-007 rules from this skill, confirm the files being created/edited are under `prompt/`.

If the target files are not under `prompt/`, stop and ask for confirmation before applying ADR-007 rules in non-`prompt/` contexts.

## Mandatory first step (view only `T102-ADR-007`)

Do not rely on memory or paraphrase. Always load the current `T102-ADR-007` block:

Run:
- `python3 prompt/skills/t102-adr-007-issues-risks-index/scripts/print_t102_adr_007.py`

Use the printed output as the authoritative reference for the rest of the task. Do not read or quote other sections of the Concept document unless explicitly requested.

## ADR-005 delegation (IDs + formal references)

ADR-007 relies on ID rules governed by `T102-ADR-005` (e.g., `ISSUE` / `RISK` IDs) and may require back-ticked formal references to governing IDs.

When you need to construct/validate IDs or write RID formal references:
1) Explicitly invoke the ADR-005 skill workflow (`t102-adr-005-id-spec`).
2) Print ADR-005:
   - `python3 prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`
3) Apply ADR-005’s normative rules.

Do not duplicate ADR-005 rules here.

## Operational workflow (SSOT-first)

Workflow:
1) Confirm **hard scope gate**: you are creating/editing files under `prompt/`.
2) Print `T102-ADR-007` using the script above.
3) Identify what you are doing: **creating**, **updating**, or **reviewing** an Issues & Risks section.
4) Apply the relevant rules directly from the printed `T102-ADR-007` text (cite the exact heading/bullet from the printed output when enforcing a constraint).
5) If ID construction or RID formal referencing is required, invoke ADR-005 (above) and apply its printed rules.

## Action mapping (general)

Use this mapping only to decide where to look in the printed ADR-007 block. Treat the printed ADR as normative; treat this section as a workflow aide.

### A) Create/update the “Issues” table

- Confirm the heading/placement matches the artifact type rules in ADR-007.
- Confirm the Issues table schema matches ADR-007 exactly (columns and ordering).
- Confirm `Status` and `Priority` values match ADR-007’s enums and casing.
- Confirm the `Resolution Notes` / `Resolution Date` coupling rules are satisfied for the given `Status`.
- Confirm IDs follow ADR-005 (`ISSUE` category token, scoping, numbering).

### B) Create/update the “Risks” table

- Confirm the heading/placement matches the artifact type rules in ADR-007.
- Confirm the Risks table schema matches ADR-007 exactly (columns and ordering).
- Confirm `Status` and `Priority` values match ADR-007’s enums and casing.
- Confirm the `Mitigation Notes` / `Mitigation Date` coupling rules are satisfied for the given `Status`.
- Confirm IDs follow ADR-005 (`RISK` category token, scoping, numbering).

### C) Promote/de-duplicate cross-scope items

- If an Epic issue/risk becomes Initiative-impacting, follow ADR-007’s promotion guidance (create a new higher-scope item and close/adjust the lower-scope one using the required referencing approach).
- Prefer “link-don’t-duplicate” per ADR-007; avoid copy/pasting narratives across scopes.

## Red flags (STOP)

- You did not print `T102-ADR-007` first.
- Target files are outside `prompt/`.
- You are about to “approximate” columns/enums because “it’s close enough”.
- You are about to restate ADR-005 ID rules inside ADR-007 docs instead of invoking ADR-005.
