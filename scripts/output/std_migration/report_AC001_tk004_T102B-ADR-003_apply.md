# Migration Report

- Mode: apply
- Root: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt`
- Files changed: 1
- Files skipped (include filter): 829
- Files skipped (exclude rules): 0
- Files skipped (encoding): 0
- Safety cap (`max-files-changed`): 5
- Include paths:
  - `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-003_story-fr-deferral-standard.md`
- Exclude globs:
  - `**/scripts/output/**`
  - `**/workspace/scripts/report_*.md`

## Change Summary

- `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-003_story-fr-deferral-standard.md`
  - rename: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-003_story-fr-deferral-standard.md` -> `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-003_story-fr-deferral-standard.md`
  - clause_rewrites: 3
  - dr_body_id_rewrites: 1
  - heading_rewrites: 1

## Unified Diffs

### `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-003_story-fr-deferral-standard.md`

```diff
--- /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-003_story-fr-deferral-standard.md
+++ /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-003_story-fr-deferral-standard.md
@@ -1,8 +1,8 @@
-# T102B-STD-003 — Story FR Deferral Standard
+# T102B-STD-003 — Story FR Deferral Standard
 
 ## Decision
 
-* **T102B-STD-003 (Story FR Deferral Standard)**
+* **T102B-STD-003-ADR-001 (Story FR Deferral Standard)**
 
   * **Context**
     Per `T102B-STD-002 (Workflow Typology Standard)`, story-level specification at Request stage is identified as an industry anti-pattern per SAFe guidance and `T102B-RES-001` W2 findings. Request artifacts need story navigation without detailed FR bodies.
@@ -29,16 +29,16 @@
 
 ## Specification
 
-1) **T102B-STD-003-CLAUSE-001 (Story Index Structure)**
+1) **T102B-STD-003-CLAUSE-001 (Story Index Structure)**
    - Request artifacts MAY include a Story Index for multi-story features.
    - Story Index SHALL contain: Story ID, Title, Purpose summary (1-2 sentences), Design Link (populated post-handoff).
    - Story Index SHALL NOT contain: Detailed FR bodies, acceptance criteria, implementation details.
 
-2) **T102B-STD-003-CLAUSE-002 (Deferral Boundary)**
+2) **T102B-STD-003-CLAUSE-002 (Deferral Boundary)**
    - Story-level FRs (testable behavior per story) SHALL be deferred to Design phase.
    - Story-level acceptance criteria (Gherkin AC) SHALL be deferred to Design phase.
    - Feature-level scope (Story Index with purpose summaries) SHALL remain in Request.
 
-3) **T102B-STD-003-CLAUSE-003 (Exceptions)**
+3) **T102B-STD-003-CLAUSE-003 (Exceptions)**
    - Single-story features MAY include story-level FR in Request if complexity warrants Full Request workflow.
    - Exception requires explicit justification in Request Section Notes.
```
