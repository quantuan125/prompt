# Migration Report

- Mode: apply
- Root: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt`
- Files changed: 2
- Files skipped (include filter): 798
- Files skipped (exclude rules): 0
- Files skipped (encoding): 0
- Safety cap (`max-files-changed`): 10
- Include paths:
  - `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
  - `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_decision-records-standard.md`
- Exclude globs:
  - `**/scripts/output/**`
  - `**/workspace/scripts/report_*.md`

## Change Summary

- `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
  - title_rewrites: 5
- `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_decision-records-standard.md`
  - dr_anchor_regenerations: 1
  - title_rewrites: 2
  - token_replacements: 2
  - top_anchor_regenerations: 1

## Unified Diffs

### `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`

```diff
--- /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md
+++ /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md
@@ -34,7 +34,7 @@
 
 | STD ID | Title | Status | Owner | Effective | Supersedes | Current DR | Canonical Path |
 | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
-| `T102-STD-004` | **Specification Standard & Guideline** | Proposed | Client | — | — | `T102-STD-004-ADR-001` | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_decision-records-standard.md` |
+| `T102-STD-004` | **Specification Standard & Guideline** | Proposed | Client | — | — | `T102-STD-004-ADR-001` | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_decision-records-standard.md` |
 
 
 * **T102-STD-001 (Consultancy Operating Model)** {#t102-std-001-consultancy-model}
@@ -466,7 +466,7 @@
   * **References** 
     `T102-STD-005 (ID Governance Standard)`, 
     `T102-STD-003 (Explicit Inheritance Model)`, 
-    `T102-STD-004 (Specification Standard & Guideline)`, 
+    `T102-STD-004 (Specification Standard & Guideline)`, 
     `T102-STD-006 (Research Artifacts Index)`,
     `T102-CON-009 (Normative Keywords)`
 
@@ -715,7 +715,7 @@
   `T102-GDR-008 (Organisation Baseline Standard)`,
   `T102-GDR-003 (Inheritance Model Standard)`,
   `T102-STD-003 (Explicit Inheritance Model)`,
-  `T102-STD-004 (Specification Standard & Guideline)`,
+  `T102-STD-004 (Specification Standard & Guideline)`,
   `T102-STD-005 (ID Specification & Rules)`
 
   **Provenance:**
@@ -912,7 +912,7 @@
   **References:**
   `T102A-GDR-001 (Governance Snapshot Standard)`,
   `T102A-GDR-002 (Governance Freeze Standard)`,
-  `T102-STD-004 (Specification Standard & Guideline)`,
+  `T102-STD-004 (Specification Standard & Guideline)`,
   `T102-STD-005 (ID Specification & Rules)`,
   `T102-STD-008 (Organisation Baseline Standard)`,
   `T102A-STD-002 (Feature Register Index)`,
@@ -975,7 +975,7 @@
 
   **References:**
   `T102A-GDR-001 (Governance Snapshot Standard)`,
-  `T102-STD-004 (Specification Standard & Guideline)`,
+  `T102-STD-004 (Specification Standard & Guideline)`,
   `T102-STD-005 (ID Specification & Rules)`,
   `T102-RES-002 (Roadmap Viability)`
```

### `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_decision-records-standard.md`

```diff
--- /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_decision-records-standard.md
+++ /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-004_decision-records-standard.md
@@ -1,5 +1,5 @@
-# T102-STD-004 — Specification Standard & Guideline
-{#t102-std-004-specification-standard-and-guideline}
+# T102-STD-004 — Specification Standard & Guideline
+{#t102-std-004-specification-standard-and-guideline}
 
 ## Specification
 
@@ -195,7 +195,7 @@
 
 ## Decision Record
 
-* **T102-STD-004-ADR-001 (Specification Standard & Guideline)** {#t102-std-004-adr-001-specification-standard-and-guideline}
+* **T102-STD-004-ADR-001 (Specification Standard & Guideline)** {#t102-std-004-adr-001-specification-standard-and-guideline}
 
   * **Context**
     The current governance surface is split between index artifacts and combined files, which creates a dual-surface authoring pattern that drifts over time and weakens consistency targets tied to `T102-QG-002`. A single canonical combined-file structure is needed so normative clauses and decision rationale remain co-located, machine-checkable, and reviewable.
```
