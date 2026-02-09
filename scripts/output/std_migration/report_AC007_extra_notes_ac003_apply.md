# Migration Report

- Mode: apply
- Root: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt`
- Files changed: 1
- Files skipped (include filter): 806
- Files skipped (exclude rules): 0
- Files skipped (encoding): 0
- Safety cap (`max-files-changed`): 10
- Include paths:
  - `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC003.md`
- Exclude globs:
  - `**/scripts/output/**`
  - `**/workspace/scripts/report_*.md`

## Change Summary

- `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC003.md`
  - bare_reference_rewrites: 1
  - clause_rewrites: 1

## Unified Diffs

### `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC003.md`

```diff
--- /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC003.md
+++ /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC003.md
@@ -66,7 +66,7 @@
 
 | ID | Topic | Question | Owner | Status | Needed By |
 |:---|:------|:---------|:------|:-------|:----------|
-| `T102-PH001-ST001-AC003-OQ001` | ADR-004 schema wording | When do we update `T102-STD-004-CLAUSE-001` wording that still references `Anchor` schema? | Client | Resolved (2026-02-06) — addressed in AC005 plan amendment | Before ST003 execution (resolved: AC005 prerequisite) |
+| `T102-PH001-ST001-AC003-OQ001` | ADR-004 schema wording | When do we update `T102-STD-004-CLAUSE-001` wording that still references `Anchor` schema? | Client | Resolved (2026-02-06) — addressed in AC005 plan amendment | Before ST003 execution (resolved: AC005 prerequisite) |
 
 #### G. Session Handoff Pack
 
@@ -96,7 +96,7 @@
 
 #### B. Narrative Summary (Minutes-Style)
 
-The session identifies a critical planning gap: no activity in PH001 is currently assigned to redesign `T102-STD-004` before ST003 extraction begins. The existing guideline and template files (created during AC002 as lightweight artifacts) have drifted ahead of the normative CLAUSEs in ADR-004, which still reference `Anchor` schema and pre-Model D body structure. This inversion of authority (derivatives ahead of spec) must be corrected before ST003 can produce conformant combined files.
+The session identifies a critical planning gap: no activity in PH001 is currently assigned to redesign `T102-STD-004` before ST003 extraction begins. The existing guideline and template files (created during AC002 as lightweight artifacts) have drifted ahead of the normative CLAUSEs in ADR-004, which still reference `Anchor` schema and pre-Model D body structure. This inversion of authority (derivatives ahead of spec) must be corrected before ST003 can produce conformant combined files.
 
 The Client approves **Option A** (plan amendment to ST001 adding AC005) rather than creating a new stream. The Client approves **Option X** for Phase 1 token identity: keep the `ADR` token for combined files, with a meta-clause explicitly documenting the dual nature (Decision Record + Normative Specification), deferring ADR/SPEC/STD token separation to Phase 2. AC005 scope is approved as **comprehensive**: all 15 CLAUSEs will be reviewed and updated to match Model D reality, not just the broken ones. Guideline and template updates will occur **within AC005** (self-contained exemplar activity).
```
