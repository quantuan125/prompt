# Migration Report

- Mode: apply
- Root: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt`
- Files changed: 1
- Files skipped (include filter): 830
- Files skipped (exclude rules): 0
- Files skipped (encoding): 0
- Safety cap (`max-files-changed`): 5
- Include paths:
  - `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-004_request-lite-specification.md`
- Exclude globs:
  - `**/scripts/output/**`
  - `**/workspace/scripts/report_*.md`

## Change Summary

- `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-004_request-lite-specification.md`
  - rename: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-004_request-lite-specification.md` -> `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-004_request-lite-specification.md`
  - clause_rewrites: 5
  - dr_body_id_rewrites: 1
  - heading_rewrites: 1

## Unified Diffs

### `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-004_request-lite-specification.md`

```diff
--- /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-004_request-lite-specification.md
+++ /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-004_request-lite-specification.md
@@ -1,8 +1,8 @@
-# T102B-STD-004 — Request Lite Specification
+# T102B-STD-004 — Request Lite Specification
 
 ## Decision
 
-* **T102B-STD-004 (Request Lite Specification)**
+* **T102B-STD-004-ADR-001 (Request Lite Specification)**
 
   * **Context**
     Per `T102B-STD-002 (Workflow Typology Standard)`, simple features require a lightweight documentation path to reduce adoption friction. RLITE must remain <200 lines per `T102B-CON-003` while providing sufficient context for development.
@@ -31,12 +31,12 @@
 
 ## Specification
 
-1) **T102B-STD-004-CLAUSE-001 (RLITE Scope Boundary)**
+1) **T102B-STD-004-CLAUSE-001 (RLITE Scope Boundary)**
    - RLITE artifacts SHALL remain under 200 lines total per `T102B-CON-003`.
    - RLITE artifacts SHALL NOT expand by section accretion.
    - If scope exceeds boundary during authoring, escalate to Full Request per `T102B-IG-004`.
 
-2) **T102B-STD-004-CLAUSE-002 (RLITE Mandatory Sections)**
+2) **T102B-STD-004-CLAUSE-002 (RLITE Mandatory Sections)**
    - YAML Header (per MANIFEST schema).
    - Feature Purpose (1-2 paragraphs).
    - Inherited Considerations table (per `T102-STD-003`).
@@ -44,13 +44,13 @@
    - Success Criteria (measurable outcomes).
    - Approval Gate section.
 
-3) **T102B-STD-004-CLAUSE-003 (RLITE Excluded Sections)**
+3) **T102B-STD-004-CLAUSE-003 (RLITE Excluded Sections)**
    - Story Index (single-story or no-story features).
    - Detailed NFR section (inherit epic-level NFRs).
    - Extended stakeholder analysis.
    - Research/Evidence sections.
 
-4) **T102B-STD-004-CLAUSE-004 (Selection Criteria)**
+4) **T102B-STD-004-CLAUSE-004 (Selection Criteria)**
    | Factor | Full Request | RLITE | PR-only |
    |:-------|:-------------|:------|:--------|
    | Story count | >3 stories | 1-3 stories | 0-1 stories |
@@ -58,7 +58,7 @@
    | Stakeholder visibility | High (cross-team) | Medium (team) | Low (developer) |
    | Complexity | High | Low-Medium | Trivial |
 
-5) **T102B-STD-004-CLAUSE-005 (Decision Tree Workflow)**
+5) **T102B-STD-004-CLAUSE-005 (Decision Tree Workflow)**
    Authors SHALL apply selection criteria per CLAUSE-004 using this decision workflow:
    1. **Assess story count threshold**: If >3 stories → Full Request; if 0-1 stories → consider PR-only
    2. **Assess architectural impact**: If new patterns/integrations → Full Request; if trivial change → consider PR-only
```
