---
artifact_type: 'ANALYSIS'
planning_level: 'ACTIVITY'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '1'
stream_id: 'T102-PH001-ST001'
activity_id: 'T102-PH001-ST001-AC003'
version: '0.1.0'
date: '2026-02-05'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Concept-scoped prerequisite governance deltas for Model D (Combined ADR+Spec Files) and bounded rollout changeset + verification checklist for execution in ST003'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
parent_plan: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/plan_T102-PH001-ST001.md'
source_dialogue: 'prompt/artifacts/tasks/T102/consultant/raw/PH001/ST001/raw_T102-PH001-ST001-AC003-2026-02-05.txt'
---

# ANALYSIS: Phase 1 / ST001 / AC003 — Prerequisite Governance Deltas (Model D, Concept-scoped)

## I. EXECUTIVE SUMMARY

**What AC003 delivers (Concept-scoped):**
1) A **delta list** identifying the minimum Concept changes required to support **Model D (Combined ADR+Spec Files)**.
2) A bounded **migration changeset plan** (sequenced execution steps), explicitly packaged for **ST003** execution (not executed in ST001).
3) A **verification checklist** defining what “done” means for the eventual extraction and index normalization.

**Scope boundary (locked by dialogue 2026-02-05):**
- AC003 analysis focuses on **Concept** only (no SPS refactor work here).
- **ADR-009 “golden exemplar” reconciliation** (aligning `T102-STD-009` adoption pointers and STD schema/index expectations to the extracted ADR-009 combined file) is planned under **ST002**, not ST001.

## II. DELTA LIST (TK001)

Delta table schema: `Section | Location | Current State | Required Delta | Priority`

| Section | Location | Current State | Required Delta | Priority |
|:--|:--|:--|:--|:--|
| Initiative ADR Index | `concept_T102-CONSULTANT.md` → `III.B.1` | Already uses Model D schema (`Authority STD` + `Canonical Path`) | No change | P2 |
| Epic ADR Index (T102A) | `concept_T102-CONSULTANT.md` → `III.B.2.i` | Already uses Model D schema | No change | P2 |
| Epic ADR Index (T102B) | `concept_T102-CONSULTANT.md` → `III.B.2.ii` | Still uses old schema (`Paired GDR` + `Anchor`) and table is empty | Replace schema with Model D schema: `ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path` | P1 |
| Epic ADR Index (T102C) | `concept_T102-CONSULTANT.md` → `III.B.2.iii` | Uses old schema (`Paired GDR` + `Anchor`) and has an entry for `T102C-STD-001` with anchor addressing | Replace schema with Model D schema and update the `T102C-STD-001` row to use the extraction inventory canonical path | P1 |
| Feature ADR Index | `concept_T102-CONSULTANT.md` → `III.B.3` | Already uses Model D schema | No change | P2 |
| Inline ADR bodies (all scopes) | `concept_T102-CONSULTANT.md` → `III.B` | ADR bodies (including `Specification/CLAUSE`) are embedded inline under the indexes | Extract into combined files under `prompt/artifacts/tasks/T102/consultant/standards/` and remove inline bodies from Concept (execution in ST003) | P1 |
| ADR Index schema clause wording | `concept_T102-CONSULTANT.md` → `T102-STD-004-CLAUSE-001` | Clause text still describes an ADR Index schema with `Anchor` column | Treat as a governance-text delta; **defer** content update timing to ST002/ST003 (recorded as OQ/Deferred item; do not silently rewrite in ST001 close-out) | P2 |

## III. MIGRATION CHANGESET PLAN (TK002)

This is the bounded, sequenced changeset intended to be **executed in ST003** (Concept rollout stream).

1) Ensure combined-file home exists:
   - Confirm directory: `prompt/artifacts/tasks/T102/consultant/standards/`
2) Extract all ADR bodies into combined files (13 total):
   - Use `prompt/templates/consultant/standards/template_combined_adr_spec_file.md`
   - Follow `prompt/templates/consultant/standards/guideline_combined_adr_spec_file.md`
   - Extraction inventory source: `prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC002.md`
3) Normalize Epic ADR Index schemas in Concept:
   - Update `T102B` and `T102C` Epic ADR Index tables to Model D schema
   - Update row data to use canonical paths from extraction inventory (whole-file granularity)
4) Remove inline ADR bodies from Concept:
   - Concept becomes index-only hub for ADR discovery (tables + links only)
5) Validate canonical paths and completeness:
   - Every `Canonical Path` in Concept resolves to an existing combined file
   - No inline ADR body text remains under `III.B` aside from indexes/register prose

## IV. VERIFICATION CHECKLIST (TK003)

Verification is executed in **ST003** during rollout.

1) `prompt/artifacts/tasks/T102/consultant/standards/` contains **exactly 13** combined files (matches extraction inventory).
2) Each combined file name matches `<ADR-ID>_<title-slug>.md` per the combined-file guideline.
3) Each combined file contains headings in-order: `## Decision` then `## Specification`.
4) All CLAUSE IDs are preserved (no renumbering; no dropped clauses).
5) All Concept ADR indexes use the Model D schema with `Authority STD` and `Canonical Path` (no `Paired GDR` / `Anchor` columns remain in ADR Index tables).
6) Every `Canonical Path` resolves to an existing file.
7) No inline ADR body text remains in Concept Section `III.B` (Concept is index-only for ADRs).

## V. LINKS REGISTER

| Link Type | Target | Path |
|:--|:--|:--|
| SSOT | Concept | `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md` |
| Notes | AC002 inventory | `prompt/artifacts/tasks/T102/consultant/workspace/notes/PH001/ST001/notes_T102-PH001-ST001-AC002.md` |
| Template | Combined file template | `prompt/templates/consultant/standards/template_combined_adr_spec_file.md` |
| Guideline | Combined file guideline | `prompt/templates/consultant/standards/guideline_combined_adr_spec_file.md` |
| Dialogue | AC003 session transcript | `prompt/artifacts/tasks/T102/consultant/raw/PH001/ST001/raw_T102-PH001-ST001-AC003-2026-02-05.txt` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v0.1.0 | 2026-02-05 | Initial | Concept-scoped delta list + bounded ST003 changeset plan + ST003 verification checklist |

