---
artifact_type: 'PROPOSAL'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST007'
activity_id: 'T104-PH001-ST007-AC005'
task_id: 'T104-PH001-ST007-AC005-TK002'
gate_id: 'T104-PH001-ST007-AC005-GATE-000'
version: '1.3.0'
date: '2026-03-11'
status: 'approved'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/plan_T104-PH001-ST007-AC005.md'
analysis_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/analysis/analysis_T104-PH001-ST007-AC005_t102-directory-readiness.md'
purpose: 'GATE-000 decision disposition package for AC005 migration contract closure before manifest authoring and dry-run execution'
consumers:
  - 'T104-PH001-ST007-AC005-GATE-000'
  - 'T104-PH001-ST007-AC005-TK003'
  - 'T104-PH001-ST007-AC005-TK004'
  - 'T104-PH001-ST007-AC005-TK005'
  - 'T104-PH001-ST007-AC005-TK006'
  - 'T104-PH001-ST007-AC005-TK007'
  - 'T104-PH001-ST007-AC005-TK008'
  - 'T104-PH001-ST007-AC005-GATE-001'
---

# PROPOSAL: GATE-000 Decision Disposition Package — T104-PH001-ST007-AC005 (T102 Migration Contract)

## I. EXECUTIVE SUMMARY

- Context: The readiness analysis v2.1.0 identified 18 readiness findings (T102-READ-001 through T102-READ-018), produced the authoritative T102 inventory and classification matrix, and defined the routing/execution rules required for AC005. SES001 locked the first 6 disposition rules. SES002 closed the remaining contract decisions and the RES-ID canonicalization question.
- Goal at GATE-000: Record the client-approved migration contract so `TK003` through `TK012` can proceed deterministically from manifest authoring through post-apply validation.
- Scope: Root/epic routing rules, multi-manifest execution posture, rollback model, cross-initiative rewrite scope, plan-template conformance, and RES-ID canonicalization for non-canonical research filenames.

---

## II. EVIDENCE INDEX

| Evidence Type | Artifact | Path | Notes |
|:--|:--|:--|:--|
| Analysis | T102 Directory Readiness Assessment v2.1.0 | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/analysis/analysis_T104-PH001-ST007-AC005_t102-directory-readiness.md` | TK001 deliverable; authoritative inventory, routing rules, and execution mechanics |
| Analysis | RES-ID Canonicalization Audit | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/analysis/analysis_T104-PH001-ST007-AC005_res-id-canonicalization.md` | Addendum resolving SES002 OQ001 |
| Plan | AC005 Activity Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/plan_T104-PH001-ST007-AC005.md` | Governing activity plan with Gate-000 to Gate-002 sequencing |
| Session Notes | SES001 Planning Refactor | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/snotes/snotes_T104-PH001-ST007-AC005-SES001.md` | Prior disposition locks (DEC001–DEC004) |
| Session Notes | SES002 Implementation Readiness Review | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/snotes/snotes_T104-PH001-ST007-AC005-SES002.md` | Client approval record for GIR-001 through GIR-011 |
| Standard | P-STD-004 | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` | Normative naming and placement authority |
| Standard | P-STD-005 | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` | Normative ID authority for RES canonicalization |
| Precedent | AC004.1 Activity Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004.1/plan_T104-PH001-ST007-AC004.1.md` | Multi-gate migration precedent |

---

## III. DISPOSITION SUMMARY REGISTER

| GIR ID | Gap/Topic | Decision Area | Recommended Option | Execution Target | Blocking | Client Decision |
|:--|:--|:--|:--|:--|:--|:--|
| GIR-001 | SPS/concept routing | Routing rule | (a) Route to `T102/ssot/` | TK003 | Yes | (a) |
| GIR-002 | `standards/` → `standard/` rename | Routing rule | (a) Rename at all scope levels | TK003, TK004, TK005 | Yes | (a) |
| GIR-003 | Nested consultant archives | Routing rule | (a) Route to canonical `T102/archive/` tiers | TK003 | Yes | (a) |
| GIR-004 | Multi-manifest execution model | Execution mechanics | (a) Individual runs in dependency order | TK007, TK008, TK009, TK010 | Yes | (a) |
| GIR-005 | Rollback granularity | Execution mechanics | (a) Pre-TK009 checkpoint is primary rollback target | TK009, TK010 | Yes | (a) |
| GIR-006 | Cross-initiative reference scope | Execution mechanics | (a) Scan `prompt/**` (not just `T102/**`) | TK011 | Yes | (a) |
| GIR-007 | Classification matrix schema | Planning control | (a) Use 7-column schema from analysis §VI.A | TK001 (retroactive) | Yes | (a) |
| GIR-008 | `consultant/external/` disposition | Routing rule | (a) Reclassify as `analysis_` per T104 precedent | TK003 | Yes | (a) |
| GIR-009 | `consultant/workspace/scripts/` disposition | Routing rule | (a) Script to `prompt/scripts/migrations/`; reports to archive; delete `__pycache__/` | TK003 | Yes | (a) |
| GIR-010 | `standard_` prefix for legacy standard filenames | Routing rule | (a) Add `standard_` prefix during migration | TK003, TK004, TK005 | No | (a) |
| GIR-011 | RES-ID canonicalization for non-canonical research filenames | Routing + identity | (a) Canonicalize all 6 + register 5 during AC005 | TK003, TK004, TK006, TK011 | Yes | (a) |

---

## IV. DETAILED DISPOSITION REGISTER

### GIR-001 - SPS/Concept Routing to `T102/ssot/`

Context:
- `consultant/sps/sps_T102-CONSULTANT.md` and `consultant/concept/concept_T102-CONSULTANT.md` are initiative-level SSOT artifacts under the legacy `consultant/` root.
- `P-STD-004-CLAUSE-005A` requires initiative SSOT content at `T102/ssot/`.
- Archives within these directories need canonical archive placement.

Decision prompt:
- Should SPS and concept artifacts route to `T102/ssot/` with their archives routed to canonical `T102/archive/` tiers?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Route live SPS to `T102/ssot/sps_T102-CONSULTANT.md`, live concept to `T102/ssot/concept_T102-CONSULTANT.md`, and route archived variants to `T102/archive/versioned/ssot/` or `T102/archive/deprecated/ssot/` based on live-successor status. |
| (b) Alternative | Leave SPS and concept under `consultant/` during AC005 and defer the cleanup. |

Recommendation:
- (a) — Direct application of `P-STD-004-CLAUSE-005A`; deferral would leave a known non-conformance at initiative root.

Client Decision:
- `[x] (a)`

---

### GIR-002 - `standards/` to `standard/` Directory Rename

Context:
- Three locations use `standards/` (plural): `consultant/standards/`, `T102A/standards/`, and `T102B/standards/`.
- `P-STD-004-CLAUSE-002A` requires `standard/` (singular).

Decision prompt:
- Should all `standards/` directories be renamed to `standard/` during migration?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Rename `standards/` → `standard/` at all scope levels and migrate files into the canonical singular directory. |
| (b) Alternative | Rename only the initiative root and defer epic-level cleanup. |

Recommendation:
- (a) — Partial renaming would preserve structural drift across epics and weaken self-similarity.

Client Decision:
- `[x] (a)`

---

### GIR-003 - Nested Consultant Archives to Canonical Tiers

Context:
- `consultant/` contains more than 10 nested archive directories across concept, design, request, sps, standards, research, and workspace families.
- `P-STD-004-CLAUSE-009A` requires `archive/versioned/` and `archive/deprecated/`.

Decision prompt:
- Should all nested consultant archives be reclassified under canonical `T102/archive/` tiers?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Route each nested archive item into `T102/archive/versioned/` or `T102/archive/deprecated/` based on whether it has a live successor, preserving the canonical family path. |
| (b) Alternative | Move all nested archives into a flat `T102/archive/consultant/` holding area. |

Recommendation:
- (a) — Single-pass canonicalization avoids a second migration cycle and keeps the archive model toolable.

Client Decision:
- `[x] (a)`

---

### GIR-004 - Multi-Manifest Execution Model

Context:
- AC005 produces 4 manifests: root (`TK003`) plus `T102A`, `T102B`, and `T102C` (`TK004`–`TK006`).
- `migrate_initiative.py` operates on one manifest per invocation.
- The activity plan now includes separate dry-run tasks (`TK007`, `TK008`) before the client review gate and separate live-apply tasks (`TK009`, `TK010`) after it.

Decision prompt:
- Should manifests be executed as individual `migrate_initiative.py` runs in locked dependency order for both dry-run and live apply?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Execute each manifest individually in dependency order: root first, then the three epic manifests. Use the same order for dry-run and live apply, with per-run reports and rollback outputs. |
| (b) Alternative | Concatenate all manifests into a single combined manifest for each run. |

Recommendation:
- (a) — This matches the current tool design, isolates failures, and keeps rollback/evidence scoped by manifest family.

Client Decision:
- `[x] (a)`

---

### GIR-005 - Rollback Granularity

Context:
- Live apply occurs in two ordered passes: root changes in `TK009`, then epic changes in `TK010`.
- If the epic pass fails after the root pass succeeds, the repo is in a partial migration state.

Decision prompt:
- What is the primary rollback target if any live-apply pass fails?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Capture a full checkpoint immediately before `TK009`; both `TK009` and `TK010` emit rollback manifests, but any failure rolls back to the pre-`TK009` checkpoint. |
| (b) Alternative | Allow partial rollback that preserves completed root-pass changes if the epic pass fails. |

Recommendation:
- (a) — Full rollback avoids mixed migrated/unmigrated state and matches AC004.1 precedent.

Client Decision:
- `[x] (a)`

---

### GIR-006 - Cross-Initiative Reference Rewrite Scope

Context:
- T102 paths are referenced from T104 and P artifacts.
- AC004.1 required cross-initiative rewrites across 20 files.

Decision prompt:
- Should AC005 reference rewrites scan all of `prompt/**` rather than only `T102/**`?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Scan `prompt/**` (excluding `prompt/scripts/output/`) for old T102 paths and rewrite all matches. |
| (b) Alternative | Scope rewrites to `T102/**` only and defer cross-initiative references. |

Recommendation:
- (a) — Limiting rewrites to `T102/**` would knowingly leave stale cross-initiative references after migration.

Client Decision:
- `[x] (a)`

---

### GIR-007 - Classification Matrix Schema

Context:
- The original AC005 plan did not lock the classification matrix schema.
- The readiness analysis now defines a 7-column schema at §VI.A.

Decision prompt:
- Should the 7-column schema from the readiness analysis be the authoritative matrix format?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Adopt `file_path`, `root_origin`, `artifact_family`, `epic_scope`, `disposition`, `target_path`, and `notes` as the required matrix columns. |
| (b) Alternative | Use a smaller ad-hoc schema and let manifest authors add fields as needed. |

Recommendation:
- (a) — The locked schema is required for deterministic partitioning into the root and epic manifests.

Client Decision:
- `[x] (a)`

---

### GIR-008 - `consultant/external/` Disposition

Context:
- `consultant/external/` contains one external review artifact.
- T104 AC000 established the precedent of reclassifying external review material as `analysis_` with `analysis_type: external_review`.

Decision prompt:
- Should the same reclassification be applied to T102's `consultant/external/` content?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Reclassify as `analysis_` with `analysis_type: external_review` and route it into the appropriate workspace analysis location. |
| (b) Alternative | Archive it as deprecated non-canonical content. |

Recommendation:
- (a) — The content is legitimate external review evidence and the T104 precedent already establishes the migration posture.

Client Decision:
- `[x] (a)`

---

### GIR-009 - `consultant/workspace/scripts/` Disposition

Context:
- `consultant/workspace/scripts/` contains `migrate_adr_to_std.py`, 2 migration reports, and `__pycache__/`.
- There is no `P-STD-004` workspace scripts family, but `prompt/scripts/migrations/` already exists as the repo script home.

Decision prompt:
- How should the scripts directory contents be handled?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Move `migrate_adr_to_std.py` to `prompt/scripts/migrations/`, archive the reports under `T102/archive/deprecated/workspace/`, and delete `__pycache__/`. |
| (b) Alternative | Archive the entire scripts directory as historical workspace content. |

Recommendation:
- (a) — The script retains cross-initiative utility; only the generated reports are purely historical evidence.

Client Decision:
- `[x] (a)`

---

### GIR-010 - `standard_` Prefix for Legacy Standard Filenames

Context:
- Several legacy T102 standards use `T102-STD-###_kebab.md` without the required `standard_` prefix.
- `P-STD-004-CLAUSE-008A` requires the family prefix in filenames.

Decision prompt:
- Should legacy standard filenames be renamed to add the `standard_` prefix during migration?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Add the `standard_` prefix during AC005 as part of the manifest moves. |
| (b) Alternative | Leave legacy filenames unchanged and defer prefix cleanup to a separate activity. |

Recommendation:
- (a) — The rename is mechanical and AC005 is already touching these files/directories; deferral would preserve a known standards non-conformance.

Client Decision:
- `[x] (a)`

---

### GIR-011 - RES-ID Canonicalization for Non-Canonical Research Filenames

Context:
- 6 research files use non-canonical identifiers (`T102-CONSULTANT`, `T102A-SPS`, `T102C-CONCEPT`) instead of canonical `<SCOPE>-RES-###` IDs.
- 4 already have canonical RES-IDs in the SPS register (`T102-RES-001`, `T102-RES-002`, `T102A-RES-001`, `T102C-RES-001`) but the filenames were never updated.
- 2 require new assignments: `T102-RES-008` for `concept-analysis` and `T102-RES-009` for `request-analysis`.
- `T102-RES-005`, `T102-RES-006`, and `T102-RES-007` were missing from the concept register and are now recorded there.

Decision prompt:
- How should AC005 handle the 6 non-canonical research filenames and related register gaps?

| Option | Description |
|:--|:--|
| **(a) [Recommended]** | Canonicalize all 6 during AC005: rename the 4 SPS-mapped files, assign `T102-RES-008` and `T102-RES-009`, and treat cross-file reference rewrites as part of `TK011`. |
| (b) Alternative | Canonicalize only the 4 SPS-mapped files and defer the 2 new assignments plus register harmonization to a follow-up activity. |

Recommendation:
- (a) — AC005 is the natural migration window; deferral would leave identity debt in both manifest authoring and rewrite logic.

Client Decision:
- `[x] (a)`

---

## V. GATE RECOMMENDATION

Reviewer recommendation state:
- `N/A — decision gate`

Conditions and/or deferrals:
- —

Downstream enforcement:
- `TK003` through `TK012` MUST NOT begin until the Gate Decision Record below records `Client Decision = APPROVE` or `APPROVE WITH CONDITIONS`.

---

## VI. GATE DECISION RECORD (GDR)

## Gate Decision Record

| Field | Value |
|:--|:--|
| Gate ID | `T104-PH001-ST007-AC005-GATE-000` |
| Reviewer Verdict | `N/A — decision gate` |
| Client Decision | `APPROVE` |
| Conditions (if any) | `-` |
| Decided By | `Client` |
| Decision Date | `2026-03-10` |
| Decision Reference | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/snotes/snotes_T104-PH001-ST007-AC005-SES002.md` |

---

## VII. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/plan_T104-PH001-ST007-AC005.md` |
| Input Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/analysis/analysis_T104-PH001-ST007-AC005_t102-directory-readiness.md` |
| RES-ID Addendum | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/analysis/analysis_T104-PH001-ST007-AC005_res-id-canonicalization.md` |
| SES001 Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/snotes/snotes_T104-PH001-ST007-AC005-SES001.md` |
| SES002 Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC005/snotes/snotes_T104-PH001-ST007-AC005-SES002.md` |
| Stream Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md` |
| P-STD-004 | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| P-STD-005 | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |
| AC004.1 Plan (precedent) | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004.1/plan_T104-PH001-ST007-AC004.1.md` |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.3.0 | 2026-03-11 | Amendment | Reframed TK002 deliverable as the formal `GATE-000` disposition package, added `gate_id`, moved artifact status to `approved`, corrected the GDR Gate ID, aligned downstream execution targets to the rewritten AC005 plan, and kept GIR-011 as the locked RES-ID canonicalization decision. |
| v1.2.0 | 2026-03-10 | Update | Added GIR-011 for RES-ID canonicalization and the supporting addendum analysis to the evidence package. |
| v1.1.0 | 2026-03-10 | Update | Recorded client Gate-000 approval in the GDR for GIR-001 through GIR-010. |
| v1.0.0 | 2026-03-10 | Initial | Initial AC005 migration contract decision package covering routing, execution mechanics, and planning-control decisions. |
