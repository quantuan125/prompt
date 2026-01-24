---
name: t102-adr-005-id-spec
description: Use when working with files under prompt/ and you need to construct, validate, or reference RIDs (I-RID/E-RID/F-RID/S-RID), including category-token usage (e.g., ASSUM/CON/QG/FR/NFR/INT) and formal RID reference formatting governed by T102-ADR-005.
allowed-tools: Bash, Read, Grep, Glob
---

# T102-ADR-005 ID Specification & Rules (RIDs only)

## Core intent

Apply `T102-ADR-005 (ID Specification & Rules)` as the single source of truth for RID construction and referencing.

This skill is intentionally scoped:
- Applies only when the work touches artifacts under `prompt/` (filesystem prefix).
- Applies only to RIDs and RID references as defined in `T102-ADR-005` (not ADR/GDR authoring rules).

## Hard scope gate (prompt-only)

Before using any RID rules from this skill, confirm the files being created/edited are under `prompt/`.

If the target files are not under `prompt/`, stop and ask for confirmation before applying `T102-ADR-005` rules in non-`prompt/` contexts.

## Mandatory first step (view only `T102-ADR-005`)

Do not rely on memory or paraphrase. Always load the current `T102-ADR-005` block:

Run:
- `python3 prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`

Use the printed output as the authoritative reference for the rest of the task. Do not read or quote other sections of the Concept document unless explicitly requested.

## Operational workflow (SSOT-first)

This skill intentionally avoids re-stating the ADR rules (to prevent drift). The `T102-ADR-005` block you printed is the single source of truth.

Workflow:
1) Confirm **hard scope gate**: you are creating/editing files under `prompt/`.
2) Print `T102-ADR-005` using the script above.
3) Identify what you are doing: **constructing**, **validating**, or **referencing** a RID.
4) Apply the relevant rules directly from the printed `T102-ADR-005` text (quote/cite the relevant `T102-ADR-005` heading or bullet from the printed output when enforcing a constraint).

## Action mapping (general)

Use this mapping to decide *where* to look in the printed `T102-ADR-005` block. Treat the printed ADR as normative; treat this section as a workflow aide.

### A) Construct a new RID (create a new list item / new ID)

- Confirm the artifact’s **scope ID** category (initiative/epic/feature/story) matches the scope you are authoring.
- Select a **category token** that is allowed for that scope (use the printed “Allowed tokens by scope” rules).
- Construct the ID using the ADR’s universal shape (scope + category + number) and follow any numbering discipline described in the ADR.
- When introducing a RID as a list item, follow the ADR’s required **title + description** format and keep the title short.
- Keep IDs/anchors stable: don’t churn identifiers unless the ADR’s stability/migration guidance explicitly requires it.

### B) Validate an existing RID (spot-check conformance)

- Confirm the scope portion and overall ID shape match the ADR’s scope patterns.
- Confirm the category token is valid for the given scope (and not an invented/typo token).
- Confirm the title/intro list item formatting follows the ADR’s required pattern for “introduced” IDs.
- Confirm numbering is consistent with the ADR’s expectations for that section/scope.

### C) Reference a RID (formal vs informal)

- If you are writing in a **formal reference context** (e.g., a “References” subsection or an Inherited Considerations table), use the ADR’s required back-ticked `ID (Title)` token form.
- If you are writing in **inline prose**, follow the ADR’s allowed informal patterns (don’t assume bare IDs are acceptable in formal contexts).
- Check **precedence & directionality** before creating cross-scope references: do not create prohibited downstream references.

### D) Special-case guidance to apply (still SSOT-driven)

- **INT (Integration) items**: Treat INT as integration notes/guidance, not story-level acceptance criteria. If the ADR allows a scoped exception for cross-feature references, apply it explicitly and keep INT items suggestive rather than prescriptive.
- **ASSUM (Assumption) items**: Track the assumption lifecycle/validation state as required, include a validation method/owner, and record disposition upon validation. Ensure any required cross-references are present when an ASSUM extends/depends on another item.

## Common mistakes to prevent

- Inventing new category tokens not listed in `T102-ADR-005`.
- Mixing scope IDs and rule IDs (e.g., calling an F-ID like `T102A1` an “F-RID”).
- Creating downstream references (higher scope referencing lower scope) without an explicit, cited exception.
- Using bare IDs in formal References where `ID (Title)` is required.
- Applying these rules outside `prompt/` without explicit user confirmation.

## Red flags (STOP)

- “I remember the pattern” or “this looks right” without printing `T102-ADR-005` first.
- Target files are outside `prompt/`.
- You are about to edit ADR/GDR structures (that belongs to a separate ADR-004-focused skill).

## Quick examples (shape only; confirm against printed `T102-ADR-005`)

- RID construction shape: `{SCOPE_ID}-{CATEGORY}-{NNN}` (e.g., `T102A1-NFR-002`)
- Formal reference shape: back-ticked `ID (Title)` token (e.g., `T102A1-NFR-002 (Author Usability)`)

