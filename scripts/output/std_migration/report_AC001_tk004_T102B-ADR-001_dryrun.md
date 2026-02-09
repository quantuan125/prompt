# Migration Report

- Mode: dry-run
- Root: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt`
- Files changed: 1
- Files skipped (include filter): 823
- Files skipped (exclude rules): 0
- Files skipped (encoding): 0
- Safety cap (`max-files-changed`): 5
- Include paths:
  - `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-001_request-architecture-standard.md`
- Exclude globs:
  - `**/scripts/output/**`
  - `**/workspace/scripts/report_*.md`

## Change Summary

- `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-001_request-architecture-standard.md`
  - rename: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-001_request-architecture-standard.md` -> `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-001_request-architecture-standard.md`
  - clause_rewrites: 3
  - dr_body_id_rewrites: 1
  - heading_rewrites: 1

## Unified Diffs

### `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-001_request-architecture-standard.md`

```diff
--- /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-001_request-architecture-standard.md
+++ /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/T102B/standards/T102B-STD-001_request-architecture-standard.md
@@ -1,8 +1,8 @@
-# T102B-STD-001 — Request Architecture Standard
+# T102B-STD-001 — Request Architecture Standard
 
 ## Decision
 
-* **T102B-STD-001 (Request Architecture Standard)**
+* **T102B-STD-001-ADR-001 (Request Architecture Standard)**
 
   * **Context**
     Per `T102B-STD-001 (Request Governance Snapshot Standard)`, a unified architecture is required for the Request artifact family to prevent structural drift and ensure consistent authoring.
@@ -28,18 +28,18 @@
 
 ## Specification
 
-1) **T102B-STD-001-CLAUSE-001 (Artifact Hierarchy)**
+1) **T102B-STD-001-CLAUSE-001 (Artifact Hierarchy)**
    - `T102B1 (RST)` is the canonical Request template defining all possible sections.
    - `T102B4 (RLITE)` is a governed subset of `T102B1` per `T102B-CON-003`.
    - `T102B2 (RPG)` provides section classification per `T102B-STD-002`.
    - `T102B3 (MANIFEST)` defines YAML header schema and metadata requirements.
 
-2) **T102B-STD-001-CLAUSE-002 (Inheritance Model)**
+2) **T102B-STD-001-CLAUSE-002 (Inheritance Model)**
    - Request artifacts SHALL inherit initiative-level IDs via Inherited Considerations table per `T102-STD-003`.
    - Request artifacts SHALL NOT duplicate content from SPS; reference via ID citation only per `T102B-IG-006`.
    - Request artifacts SHALL NOT embed ADR bodies per `T102B-CON-004`.
 
-3) **T102B-STD-001-CLAUSE-003 (Phase 0 Completion Criteria)**
+3) **T102B-STD-001-CLAUSE-003 (Phase 0 Completion Criteria)**
    - Epic Dossier sections i-v complete in SPS.
    - All E-RIDs confirmed (ASSUM, CON, QG, DEP, IF, IG categories).
    - All E-DRIDs confirmed (GDR/ADR pairs).
```
