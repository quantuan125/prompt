# Migration Report

- Mode: apply
- Root: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt`
- Files changed: 1
- Files skipped (include filter): 828
- Files skipped (exclude rules): 0
- Files skipped (encoding): 0
- Safety cap (`max-files-changed`): 5
- Include paths:
  - `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md`
- Exclude globs:
  - `**/scripts/output/**`
  - `**/workspace/scripts/report_*.md`

## Change Summary

- `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md`
  - rename: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md` -> `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md`
  - clause_rewrites: 5
  - dr_body_id_rewrites: 1
  - heading_rewrites: 1

## Unified Diffs

### `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md`

```diff
--- /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md
+++ /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-002_section-classification-standard.md
@@ -1,8 +1,8 @@
-# T102B-STD-002 — Section Classification Standard
+# T102B-STD-002 — Section Classification Standard
 
 ## Decision
 
-* **T102B-STD-002 (Section Classification Standard)**
+* **T102B-STD-002-ADR-001 (Section Classification Standard)**
 
   * **Context**
     Per `T102B-STD-004 (Section Classification Policy)`, a unified section classification schema is required to ensure consistent artifact structure and enable completeness validation per `T102B-QG-003`.
@@ -29,12 +29,12 @@
 
 ## Specification
 
-1) **T102B-STD-002-CLAUSE-001 (Classification Categories)**
+1) **T102B-STD-002-CLAUSE-001 (Classification Categories)**
    - **Mandatory**: Section MUST contain substantive content before approval gate.
    - **Optional**: Section MAY be omitted or contain placeholder text.
    - **Deferred**: Section content belongs in downstream artifacts; SHALL contain reference/placeholder only.
 
-2) **T102B-STD-002-CLAUSE-002 (Full Request Section List)**
+2) **T102B-STD-002-CLAUSE-002 (Full Request Section List)**
    This table classifies sections under the major **Core Content** wrapper only. Major section structure (YAML + major `##` sections) is specified in CLAUSE-005.
    | Section | Classification | Notes |
    |:--------|:---------------|:------|
@@ -49,7 +49,7 @@
    | I. Research & Notes | Optional | Link to RES artifacts; include industry alignment mapping |
    | J. Story Index | Optional | Required if `story_count > 1` per CLAUSE-004 |
 
-3) **T102B-STD-002-CLAUSE-003 (RLITE Section List)**
+3) **T102B-STD-002-CLAUSE-003 (RLITE Section List)**
    This table classifies items under the major **Core Content** wrapper only. Major section structure (YAML + major `##` sections) is specified in CLAUSE-005.
    | Section | Classification | Notes |
    |:--------|:---------------|:------|
@@ -57,7 +57,7 @@
    | Scope | Mandatory | In/Out bullets |
    | Success Criteria | Mandatory | Measurable outcomes |
 
-4) **T102B-STD-002-CLAUSE-004 (Validation Rules)**
+4) **T102B-STD-002-CLAUSE-004 (Validation Rules)**
    - Mandatory sections with empty content SHALL fail gate validation.
    - Optional sections MAY be omitted entirely (no placeholder required).
    - Deferred sections SHALL contain explicit deferral note with target artifact.
@@ -65,7 +65,7 @@
    - Story Index applicability rule: if `story_count > 1`, Section J (Story Index) SHALL be present and populated.
      - Definition: `story_count` is the number of Story rows in the Story Index table (excluding the header row).
 
-5) **T102B-STD-002-CLAUSE-005 (Major Section Structure — Documentation Standards)**
+5) **T102B-STD-002-CLAUSE-005 (Major Section Structure — Documentation Standards)**
    Per `T102-CON-003 (Documentation Standards)`, major section structure SHALL follow `prompt/documentation/main/prompt_main.md`.
    - This ADR’s section lists (CLAUSE-002/003) intentionally classify **Core Content** only.
    - **Additive convention (T102B Request-family artifacts)**: Major `##` section headings SHALL use **Capital Roman numerals** (e.g., `## I. ...`, `## II. ...`) as shown in the tables below. This convention is additive to the heading rules in `prompt_main.md`.
```
