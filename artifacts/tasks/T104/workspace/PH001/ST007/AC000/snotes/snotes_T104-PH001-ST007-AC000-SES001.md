---
artifact_type: 'NOTES'
notes_type: 'SESSION_ACTIVITY'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream: 'ST007'
activity_id: 'T104-PH001-ST007-AC000'
session: 'SES001'
version: '1.0.0'
date: '2026-02-14'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
register_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/notes_T104-PH001-ST007.md'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/plan_T104-PH001-ST007.md'
raw_transcript_reference: '—'
---

<!--
Activity sessions capture work that belongs to a single Activity but must be split across multiple sessions to prevent context rot.
ID prefix rule: T104-PH001-ST007-AC000-SES001-[TYPE][###]
-->

# ACTIVITY SESSION NOTES: T104 (CWS) — PH001 / ST007 / AC000 / SES001 (Readiness Gap Resolution & Convention Decisions)

## A. Agenda / Topics

1. Confirm authority surface (TK001): proposal-seeded mode, P-STD-004 status
2. Resolve `workspace/external/` convention gap (TK002): standalone type vs analysis subtype
3. Resolve self-referential migration sequencing (TK003): execution approach + reference update pattern
4. Resolve T104A epic workspace target mapping (TK004): self-similar structure, legacy file renaming
5. Resolve legacy phase 0 files (TK005): archive vs rename-and-relocate
6. Assess impact on AC001/AC002 task registers from resolved gaps
7. Define notes registration for AC000 per guideline §5.1

---

## B. Narrative Summary (Minutes-Style)

### Authority Surface (TK001)
The authority surface was confirmed as **proposal-seeded mode**. P-STD-004 remains in `planned` status (all 4 tasks in `plan_P-PH000-ST001.md` AC004 are `planned`, no work started). The normative input for this stream is `proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` v3.0.0 with all 15 DRs Client-approved. If P-STD-004 is authored before AC001 execution completes, AC001 SHALL reconcile any variance.

### External Artifact Convention (TK002)
The Client clarified that `external/` artifacts are deliberately solicited second-opinion reviews — prompted specifically to provide unbiased outside perspective on internal work. Three industry patterns were assessed: (1) separate artifact type, (2) metadata-differentiated subtype, (3) linked provenance. The **metadata-differentiated approach** was selected — external reviews are reclassified as `analysis_` artifacts with `analysis_type: external_review` in YAML frontmatter. This avoids adding a 15th artifact prefix while preserving the semantic distinction. The existing file `external_T104-PH001-ST002_AC000.txt` will be renamed to `analysis_T104-PH001-ST002-AC000_external-review.md` and placed at the stream-scoped analysis directory. This is recorded as a **lightweight convention addendum** (not a proposal amendment).

### Self-Referential Migration (TK003)
Option B approved: the migration script loads the full manifest into memory before executing any filesystem operations. Additionally, the Client highlighted the need for **reference updating** during migration — old paths must be rewritten to new paths across all `prompt/**` files. The established pattern from `migrate_adr_to_std.py` (regex-based reference rewriting, include/exclude filtering, dry-run + diff reporting, max-files safety cap) was reviewed. The migration script should either extend `update_path_references.py` to accept the manifest as input, or compose: run move operations then reference rewrites sequentially. This requires an additional task in AC001's register.

### T104A Epic Workspace Target Mapping (TK004)
Client approved the recommended mapping: roadmap moves to `T104A/ssot/`, changelog accompanies roadmap in `ssot/`, legacy files assigned to `PH000/ST000/` with UID-conformant renaming:
- `notes_T104A-ROADMAP_phase0.md` → `notes_T104A-PH000-ST000.md`
- `raw_T104A-ROADMAP_2026-01-30_p1.md` → `raw_T104A-PH000-ST000-SES001.md`

### Legacy Phase 0 Files (TK005)
Client approved Option A: rename and relocate to `PH000/`:
- `notes_T104-CWS_phase0.md` → `workspace/PH000/notes_T104-PH000.md`
- `notes_T104-CWS_phase0_stream3.md` → `workspace/PH000/ST003/notes_T104-PH000-ST003.md`

### Impact on AC001/AC002
AC001 requires a new task (TK006) for reference update pass implementation. AC002's reference repair tasks (TK001–TK002) are reduced to verification-only scope if AC001 handles reference rewriting during migration execution. Plan bump to v0.3.0 recommended.

---

## C. Discussion Points (DP Table)

| ID | Topic | Outcome | Rationale | Evidence |
|:---|:------|:--------|:----------|:---------|
| `T104-PH001-ST007-AC000-SES001-DP001` | Authority surface for ST007 | Confirmed: proposal-seeded mode, v3.0.0 | P-STD-004 remains `planned`; proposal is the sole normative input | `plan_P-PH000-ST001.md` AC004 status |
| `T104-PH001-ST007-AC000-SES001-DP002` | External artifact classification approach | Three patterns assessed: separate type, metadata subtype, linked provenance | Convention economy (14 prefixes sufficient), discoverability (single analysis location), tooling support (frontmatter filter) | Industry patterns: ISO 9001, agile doc management, FDA regulatory |
| `T104-PH001-ST007-AC000-SES001-DP003` | Self-referential migration and reference updating | Load-before-execute + reference update pass using established script patterns | `migrate_adr_to_std.py` demonstrates the proven pattern; `update_path_references.py` provides reusable infrastructure | `prompt/scripts/migrations/migrate_adr_to_std.py`, `prompt/documentation/tools_catalog.md` |
| `T104-PH001-ST007-AC000-SES001-DP004` | T104A legacy naming treatment | Assign to PH000/ST000 with UID-conformant rename | T104A predates formal planning; PH000 represents inception/exploration phase; keeps files discoverable in timeline | Convention 4 (timeline hierarchy), Convention 7 (self-similar) |
| `T104-PH001-ST007-AC000-SES001-DP005` | Phase 0 legacy files treatment | Rename + relocate to PH000/ (not archive) | Files represent real inception work; PH000 is natural home; archiving would bury still-relevant notes | Convention 4 (timeline hierarchy) |
| `T104-PH001-ST007-AC000-SES001-DP006` | AC001/AC002 revision scope | AC001 needs new TK006 (reference updates); AC002 becomes verify-only for references | Cleaner model: migration handles rewrites, verification confirms zero remaining old paths | `migrate_adr_to_std.py` pattern analysis |

---

## D. Decisions Captured (DEC Table)

| ID | Decision | Type | Status | Owner | Date | Rationale | Acceptance Signal | Evidence |
|:---|:---------|:-----|:-------|:------|:-----|:----------|:------------------|:---------|
| `T104-PH001-ST007-AC000-SES001-DEC001` | Authority surface frozen: proposal-seeded mode, v3.0.0 | Convention | Confirmed | Client | 2026-02-14 | P-STD-004 not yet authored; proposal is sole normative input | Client approval in QA | TK001 |
| `T104-PH001-ST007-AC000-SES001-DEC002` | External artifacts reclassified as `analysis_` with `analysis_type: external_review` frontmatter metadata; no new prefix | Convention addendum | Confirmed | Client | 2026-02-14 | Convention economy; preserves semantic distinction via metadata; avoids 15th prefix | Client approval in QA | TK002, DP002 |
| `T104-PH001-ST007-AC000-SES001-DEC003` | Migration script uses load-before-execute pattern + integrated reference update pass | Technical | Confirmed | Client | 2026-02-14 | Follows established `migrate_adr_to_std.py` pattern; ensures path references are updated atomically with moves | Client approval in QA | TK003, DP003 |
| `T104-PH001-ST007-AC000-SES001-DEC004` | T104A legacy files mapped to PH000/ST000 with UID-conformant rename; roadmap → ssot/; changelog accompanies roadmap | Convention | Confirmed | Client | 2026-02-14 | Self-similar convention (Conv 7); PH000 represents inception phase | Client approval in QA | TK004, DP004 |
| `T104-PH001-ST007-AC000-SES001-DEC005` | Legacy phase 0 files renamed and relocated to workspace/PH000/ (not archived) | Convention | Confirmed | Client | 2026-02-14 | Files are still-relevant inception work; PH000 is natural timeline home | Client approval in QA | TK005, DP005 |
| `T104-PH001-ST007-AC000-SES001-DEC006` | AC001 task register expanded with TK006 (reference update pass); AC002 TK001–TK002 scope narrowed to verification-only | Plan revision | Confirmed | Client | 2026-02-14 | Cleaner separation: AC001 handles rewrites, AC002 verifies | Client approval in QA | DP006 |

---

## E. Actions / Carry-Forward (ACT Table)

| ID | Action | Owner | Status |
|:---|:-------|:------|:-------|
| `T104-PH001-ST007-AC000-SES001-ACT001` | Enumerate complete current→target directory mapping (TK006) | LLM_Developer | `pending` |
| `T104-PH001-ST007-AC000-SES001-ACT002` | Define deterministic rename rules for raw transcripts, legacy files, and comm_ artifacts (TK007) | LLM_Developer | `pending` |
| `T104-PH001-ST007-AC000-SES001-ACT003` | Draft migration manifest as markdown table with script-parseable format (TK008) | LLM_Developer | `pending` |
| `T104-PH001-ST007-AC000-SES001-ACT004` | Design scripts/validators approach: identify scripts, locations, reuse strategy, dry-run requirements (TK009) | LLM_Developer | `pending` |
| `T104-PH001-ST007-AC000-SES001-ACT005` | Update stream plan to v0.3.0 with AC001/AC002 revisions per DEC006 | LLM_Consultant | `pending` |
| `T104-PH001-ST007-AC000-SES001-ACT006` | Client review gate: manifest + scripts design approval before AC001 (TK010) | Client | `pending` |

---

## F. Open Questions Register (OQ Table)

| ID | Topic | Question | Owner | Status | Needed By |
|:---|:------|:---------|:------|:-------|:----------|

_No open questions — all convention gaps resolved in this session._

---

## G. Session Handoff Pack

- **All 5 convention gaps resolved** (TK001–TK005): authority surface confirmed, external→analysis with metadata, load-before-execute migration, T104A mapped to PH000/ST000, phase 0 files to PH000.
- **AC001/AC002 revisions identified**: new TK006 for reference updates in AC001; AC002 narrows to verify-only.
- **Next steps**: ACT001–ACT004 are development tasks (TK006–TK009) to produce the migration manifest and scripts design. ACT005 updates the plan. ACT006 is the client gate.
- **Plan version**: Current v0.2.0 → target v0.3.0 after ACT005 is completed.

---

## H. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-14 | Initial | Session notes created; recorded 6 decisions (DEC001–DEC006), 6 discussion points (DP001–DP006), 6 actions (ACT001–ACT006) resolving all AC000 convention gaps |
