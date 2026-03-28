---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC010'
task_id: 'P-PH000-ST001-AC010-TK000'
version: '1.1.0'
date: '2026-03-28'
status: 'completed'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md'
execution_audience: 'developer'
purpose: 'Unified developer-facing execution contract for the future AC010 metadata retrofit across P-STD-002, P-STD-004, P-STD-005, and any bounded SPS registration-sync follow-on.'
---

# IMPLEMENTATION (Task Specification): AC010 Cross-Standard Metadata Retrofit

## I. PURPOSE & AUTHORITY
- Purpose: Specify the exact future execution required to retrofit `P-STD-002`, `P-STD-004`, and `P-STD-005` to the `P-STD-001` metadata-governance model without reopening AC009 design decisions.
- Authority chain: AC010 plan records `TK000` as the commissioning task for this artifact and authorizes future execution of `TK001` through `TK004` -> this artifact specifies HOW those execution tasks are performed -> future dev-report records execution evidence.
- Audience: `LLM_Developer`
- This artifact does NOT hold a GDR. Gate decisions remain exclusively in the AC010 `gate_disposition` proposal.

## II. TASK SCOPE
- Governing plan task: `P-PH000-ST001-AC010-TK000`
- Traceability note: Frontmatter `task_id` points to the consultant-owned commissioning surface that authored this execution contract; downstream implementation evidence remains owned by `TK001` through `TK005`.
- Trigger: The target standards start from materially different metadata structures, so future execution would otherwise require the developer to make design and lineage-mapping decisions that belong to the consultant.
- Deliverable contract: Future execution updates only the governed metadata surfaces of `P-STD-002`, `P-STD-004`, and `P-STD-005`, then performs bounded SPS registration sync if the existing SPS row text needs refresh.

## III. SPECIFICATION ITEMS

### SPEC-001 — Retrofit `P-STD-002` to the governed metadata model

| Field | Detail |
|:--|:--|
| Requirement Source | AC010 plan `TK001` + AC009 handoff communication + `P-STD-001-CLAUSE-031` through `P-STD-001-CLAUSE-036G` |
| Target file(s) | `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`; `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-002.md` |
| Required end-state posture | File gains governed YAML frontmatter; `## References` is split into `### Normative References` and `### Informative References`; `## Provenance` is split into `### Status`, `### Lineage / Authority`, `### Amendment History`, and `### Input Sources`; no normative `CLAUSE` body content changes |
| Explicit non-target / do-not-change constraints | Do not alter the Specification Index, CLAUSE numbering, clause text, ADR bodies, or the meaning of existing amendment-history entries |
| Validation check | Re-read the opening frontmatter block, the full `## References` section, the full `## Provenance` section, and the new changelog file; confirm only metadata surfaces changed and the amendment-history externalization follows `P-STD-001-CLAUSE-036G` |
| Blocking ambiguity rule | If any intended edit would require changing a normative rule, adding/removing a clause, or rewording an ADR decision, stop and escalate instead of inferring |
| Status | `open` |

#### Implementation Detail

Use `v1.2.0` from the existing Amendment History as the current governed baseline and bump the frontmatter `version` to `1.3.0`, with `date` set to the actual execution date. Set frontmatter to:
- `artifact_type: 'STANDARD'`
- `initiative_id: 'P'`
- `initiative_code: 'PROGRAM'`
- `standard_id: 'P-STD-002'`
- `version: '1.3.0'`
- `date: '<execution-date>'`
- `status: 'accepted'`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`
- `approval_date: '2026-03-04'`
- `effective_date: '2026-03-04'`

Apply the `P-STD-001-CLAUSE-032` authority split explicitly:
- frontmatter is the current-state authority for `version`, `date`, `status`, `approval_date`, and `effective_date`
- `## Provenance` carries supporting status, lineage, amendment history, and input-source context only
- any duplicated current-state facts inside `## Provenance` must restate the frontmatter posture without contradiction

Normalize `## References` exactly as follows:
- `### Normative References`: `P-STD-001`, `P-STD-004`, `P-STD-005`
- `### Informative References`: `P-SPS`, `P-RES-001`, `P-RES-002`, `CDR Proposal`

Normalize `## Provenance` exactly as follows:
- `### Status`: compact table carrying current lifecycle posture `accepted`, approved date `2026-03-04`, and effective date `2026-03-04`
- `### Lineage / Authority`: compact table carrying the governing activity plan plus the three approval surfaces already implied by the current artifact history:
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-001_gir-disposition-package.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-003_execution-disposition-package.md`
  - `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-004_amendment-disposition-package.md`
- `### Amendment History`: because the retrofit adds a sixth inline history entry, externalize the full amendment history to `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-002.md`; place the required blockquote pointer immediately under `### Amendment History`; retain only the three most recent versioned entries inline (`v1.3.0`, `v1.2.0`, `v1.1.0`); preserve the complete prior version history in the changelog table, including the older versioned entries
- `### Input Sources`: list the AC003 governing plan, `P-RES-001`, `P-RES-002`, the CDR proposal, this AC010 readiness assessment, and this AC010 implementation specification

### SPEC-002 — Retrofit `P-STD-004` to the governed metadata model

| Field | Detail |
|:--|:--|
| Requirement Source | AC010 plan `TK002` + AC009 handoff communication + `P-STD-001-CLAUSE-031` through `P-STD-001-CLAUSE-036G` |
| Target file(s) | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| Required end-state posture | File gains governed YAML frontmatter; current `External References` is split into canonical normative/informative references; existing `Status`, `Seed Source`, `Activity Plan`, and `Seed Decision Inputs` are preserved by remapping into canonical Provenance subsections; no normative `CLAUSE` body content changes |
| Explicit non-target / do-not-change constraints | Do not alter file/directory conventions, naming stems, or clause numbering; do not rewrite the substantive seed/gate lineage as new decisions |
| Validation check | Re-read the opening frontmatter block and all of `## References` / `## Provenance`; confirm seed lineage is preserved and no normative clause text changed |
| Blocking ambiguity rule | If a lineage note cannot be remapped cleanly without changing its meaning, preserve it via a compact row or bullet inside the canonical subsection rather than inventing a new interpretation |
| Status | `open` |

#### Implementation Detail

Establish the first governed semver baseline for this standard at `1.0.0`, with `date` set to the actual execution date and frontmatter:
- `artifact_type: 'STANDARD'`
- `initiative_id: 'P'`
- `initiative_code: 'PROGRAM'`
- `standard_id: 'P-STD-004'`
- `version: '1.0.0'`
- `date: '<execution-date>'`
- `status: 'draft'`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`

Apply the `P-STD-001-CLAUSE-032` authority split explicitly:
- frontmatter is the current-state authority for `version`, `date`, and `status`
- `## Provenance` carries supporting status context, lineage, amendment history, and input-source context only
- any repeated lifecycle wording inside `## Provenance` must align with the frontmatter posture and must not move historical process detail into frontmatter

Normalize `## References` exactly as follows:
- `### Normative References`: `P-STD-001`, `P-STD-005`
- `### Informative References`: `T104-PH001-ST002-AC000`, `T102-CON-009`

Normalize `## Provenance` exactly as follows:
- `### Status`: compact table carrying current lifecycle posture `draft` and the existing review posture note that the standard is pending `GATE-003` acceptance review
- `### Lineage / Authority`: compact table carrying the seeded-from-approved-proposal lineage and governing activity plan:
  - seed source proposal `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md`
  - governing plan `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/plan_P-PH000-ST001-AC004.md`
  - review lineage pointers `verification_P-PH000-ST001-AC004_gate-001.md`, `verification_P-PH000-ST001-AC004_gate-002.md`, and `verification_P-PH000-ST001-AC004_gate-003-package-audit.md`
- `### Amendment History`: prepend a new `v1.0.0` entry for the metadata-governance retrofit, then preserve the earlier seed and gate-milestone events as `Pre-baseline` entries rather than discarding them
- `### Input Sources`: carry forward the existing seed inputs plus this AC010 readiness assessment and this AC010 implementation specification

### SPEC-003 — Retrofit `P-STD-005` to the governed metadata model

| Field | Detail |
|:--|:--|
| Requirement Source | AC010 plan `TK003` + AC009 handoff communication + `P-STD-001-CLAUSE-031` through `P-STD-001-CLAUSE-036G` |
| Target file(s) | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |
| Required end-state posture | File gains governed YAML frontmatter; `External References` is split into canonical normative/informative references; existing `Promotion`, `Input Sources`, and `Hardening` provenance material is preserved by remapping into canonical Provenance subsections; no normative `CLAUSE` body content changes |
| Explicit non-target / do-not-change constraints | Do not alter regex patterns, token tables, clause numbering, or the substance of promotion/hardening history |
| Validation check | Re-read the opening frontmatter block and all of `## References` / `## Provenance`; confirm promotion and hardening lineage remain visible after normalization |
| Blocking ambiguity rule | If any current provenance statement looks like normative content, preserve the exact statement and escalate only if relocation would require changing semantics |
| Status | `open` |

#### Implementation Detail

Establish the first governed semver baseline for this standard at `1.0.0`, with `date` set to the actual execution date and frontmatter:
- `artifact_type: 'STANDARD'`
- `initiative_id: 'P'`
- `initiative_code: 'PROGRAM'`
- `standard_id: 'P-STD-005'`
- `version: '1.0.0'`
- `date: '<execution-date>'`
- `status: 'draft'`
- `author: 'LLM_Consultant'`
- `decision_owner_role: 'Client'`

Apply the `P-STD-001-CLAUSE-032` authority split explicitly:
- frontmatter is the current-state authority for `version`, `date`, and `status`
- `## Provenance` carries supporting status context, promotion lineage, amendment history, and input-source context only
- any repeated current-state facts in `## Provenance` must remain consistent with the frontmatter values and must not relocate hardening or promotion history into frontmatter

Normalize `## References` exactly as follows:
- `### Normative References`: `P-STD-001`, `T102-STD-003`
- `### Informative References`: `T102-STD-005`, `T102-STD-006`, `T102-CON-009`

Normalize `## Provenance` exactly as follows:
- `### Status`: compact table carrying current lifecycle posture `draft`
- `### Lineage / Authority`: compact table carrying the promotion lineage already stated in the file:
  - promoted from `T102-STD-005`
  - promotion activity `P-PH000-ST001-AC006`
  - promotion contract `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/proposal/proposal_P-PH000-ST001-AC006_promotion-contract-t102-std-005-to-p-std-005.md`
  - active alias window note
- `### Amendment History`: prepend a new `v1.0.0` entry for the metadata-governance retrofit, then preserve the promotion and hardening milestones as `Pre-baseline` entries
- `### Input Sources`: preserve the existing input-source list and add the AC006 pre-promotion audit, AC007 hardening assessment, AC007 gate verification, this AC010 readiness assessment, and this AC010 implementation specification

### SPEC-004 — Perform bounded SPS registration sync only if the existing row text needs refresh

| Field | Detail |
|:--|:--|
| Requirement Source | AC010 plan `TK004` + AC009 handoff communication + current SPS schema in `sps_P-PROGRAM.md` |
| Target file(s) | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |
| Required end-state posture | SPS remains within its current schema; no new columns are introduced; rows for `P-STD-002`, `P-STD-004`, and `P-STD-005` are updated only if the existing registration text needs to mention the metadata-governance retrofit or newly governed frontmatter posture |
| Explicit non-target / do-not-change constraints | Do not add a version column; do not change unrelated SPS rows; do not restate the full implementation specification inside SPS |
| Validation check | Re-read the affected SPS rows and confirm they still conform to the live index schema and reflect only bounded registration-sync updates |
| Blocking ambiguity rule | If the retrofit does not require any row-text change, leave SPS untouched and record a no-change result in the future dev-report instead of forcing a cosmetic edit |
| Status | `open` |

#### Implementation Detail

Treat TK004 as registration sync, not schema migration. The current SPS STD Index does not expose an explicit version field, so future execution MUST NOT invent one. Update only what the current row schema can legitimately carry:
- canonical path if it changes (not expected)
- review or description text if it now needs to mention governed frontmatter / metadata-structure conformance
- references only if the retrofit creates a real registration-level change that fits the existing columns

If the retrofitted standards remain accurately described by the current SPS rows, TK004 should be executed as a verified no-op and documented that way.

## IV. IMPLEMENTATION SEQUENCE
1. Read the AC009 handoff communication in full.
2. Execute `SPEC-001` for `P-STD-002`.
3. Execute `SPEC-002` for `P-STD-004`.
4. Execute `SPEC-003` for `P-STD-005`.
5. Re-check the SPS row schema and execute `SPEC-004` only if a bounded registration-sync edit is actually required.
6. Hand off the resulting changes to the future AC010 dev-report task with explicit traceability back to `SPEC-001` through `SPEC-004`.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/plan_P-PH000-ST001-AC010.md` |
| Upstream Handoff Communication | `prompt/artifacts/tasks/P/workspace/PH000/ST001/communication/comm_P-PH000-ST001-AC010_ac009-handoff-boundary.md` |
| Readiness Assessment | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010-TK000_execution-readiness-assessment.md` |
| Governing Metadata Authority | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| SPS | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-28 | Amendment | Clarified `TK000` versus `TK001`-`TK004` traceability, made the `P-STD-001-CLAUSE-032` authority split explicit across the three standards, and added exact `P-STD-002` `CLAUSE-036G` amendment-history externalization instructions including the required changelog file. |
| v1.0.0 | 2026-03-27 | Initial | Authored the unified AC010 developer-facing execution contract for the future cross-standard metadata retrofit. Defines exact target-state mappings for `P-STD-002`, `P-STD-004`, `P-STD-005`, and bounded SPS registration sync. |
