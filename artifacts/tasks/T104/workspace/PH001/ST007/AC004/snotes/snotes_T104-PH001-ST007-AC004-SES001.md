---
artifact_type: 'NOTES'
notes_type: 'SESSION_ACTIVITY'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream: 'ST007'
activity_id: 'T104-PH001-ST007-AC004'
session: 'SES001'
version: '1.0.0'
date: '2026-02-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
register_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/notes_T104-PH001-ST007.md'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.md'
raw_transcript_reference: '—'
---

<!--
Activity sessions capture work that belongs to a single Activity but must be split across multiple sessions to prevent context rot.
ID prefix rule: T104-PH001-ST007-AC004-SES001-[TYPE][###]
-->

# ACTIVITY SESSION NOTES: T104 (CWS) — PH001 / ST007 / AC004 / SES001 (AC004 Commissioning QA + Plan Amendment)

## A. Agenda / Topics

1. Review AC004 readiness gaps/risks before developer commissioning (TK001 framing)
2. Lock remaining commissioning decisions: roadmap location, proposal placement semantics, validator profile semantics, concept stub handling, rollback guarantee
3. Amend AC004 activity plan to be commissioning-ready and internally consistent with tooling realities
4. Define gate evidence expectations (inventory, dry-run report, rollback checkpoint)

---

## B. Narrative Summary (Minutes-Style)

This session captured the final commissioning QA for AC004 and resulted in a plan amendment to make the AC004 activity plan decision-complete and implementable.

The Client confirmed the roadmap canonical location is `ssot/` and that proposal placement should be "both" stream-scoped and activity-scoped without duplicating proposal content. Because the validator enforces the UID-scope rule for `AC###` tokens, canonical proposal content remains activity-scoped (e.g., `.../AC002/proposal/` for AC002 UIDs), and a stream-level proposal pointer artifact is used strictly for navigation.

The Client confirmed conservative rollback expectations, approving a two-layer rollback policy: a known-good checkpoint (git commit hash or out-of-tree snapshot) is the rollback guarantee, while the migration tool's rollback manifest is treated as supplemental for move operations only (reference rewrites are content edits and are not reversed by the rollback manifest).

For pre-migration validation, the Client approved that missing required roots and missing SSOT `concept_*.md` remain errors. The `--profile pre-migration` enhancement is therefore limited to suppressing only noise from legacy structure (type-first workspace dirs and root `raw/`).

Finally, concept stub creation was explicitly removed from the migrator manifest surface: `concept_P-PROGRAM.md` is created manually as an explicit post-apply step, rather than introducing an unsupported "create" operation in `migrate_initiative.py`.

---

## C. Discussion Points (DP Table)

| ID | Topic | Outcome | Rationale | Evidence |
|:---|:------|:--------|:----------|:---------|
| `T104-PH001-ST007-AC004-SES001-DP001` | Roadmap canonical location | Confirmed `ssot/` as canonical location | Aligns with stream authority direction; avoids workspace drift | AC004 plan amendment |
| `T104-PH001-ST007-AC004-SES001-DP002` | Proposal "both" semantics vs UID-scope rule | Canonical proposal remains activity-scoped; stream-level pointer used for navigation | UID-scope validator requires AC-scoped files to reside under matching `AC###/`; pointer avoids duplication drift | Validator UID-scope rule; AC004 plan amendment |
| `T104-PH001-ST007-AC004-SES001-DP003` | `--profile pre-migration` semantics | Suppress only type-first workspace dirs + root `raw/`; keep required-root + SSOT checks as errors | Keeps blockers visible while reducing noise during readiness scans | AC004 plan amendment |
| `T104-PH001-ST007-AC004-SES001-DP004` | Concept stub creation mechanism | Manual post-apply creation, not a manifest `create` action | Migrator manifest supports mkdir/move/delete + reference rewrites; creating content is explicitly out of scope | AC004 plan amendment |
| `T104-PH001-ST007-AC004-SES001-DP005` | Rollback guarantee model | Known-good checkpoint is the guarantee; rollback manifest is supplemental | Conservative, auditable rollback without relying on custom "undo content rewrite" logic | AC004 plan amendment |

---

## D. Decisions Captured (DEC Table)

| ID | Decision | Type | Status | Owner | Date | Rationale | Acceptance Signal | Evidence |
|:---|:---------|:-----|:-------|:------|:-----|:----------|:------------------|:---------|
| `T104-PH001-ST007-AC004-SES001-DEC001` | Roadmap canonical location is `ssot/` (not workspace). | Convention | Confirmed | Client | 2026-02-22 | Canonical placement reduces drift and aligns with the stream authority direction for roadmap placement. | Client QA approval | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.md` |
| `T104-PH001-ST007-AC004-SES001-DEC002` | Proposal is "both" by navigation: canonical proposal content remains activity-scoped (UID-scope rule), plus a stream-level pointer artifact (link-only; no duplicated proposal content). | Convention | Confirmed | Client | 2026-02-22 | UID-scope rule requires `AC###` files to be located under the matching activity directory; pointer provides stream-level discoverability without duplication drift. | Client QA approval | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.md` |
| `T104-PH001-ST007-AC004-SES001-DEC003` | `--profile pre-migration` suppresses noise only (type-first workspace dirs, root `raw/`); missing required roots and missing SSOT `concept_` remain errors. | Technical | Confirmed | Client | 2026-02-22 | Keeps hard blockers visible while allowing a focused readiness scan of legacy structure noise. | Client QA approval | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.md` |
| `T104-PH001-ST007-AC004-SES001-DEC004` | `concept_P-PROGRAM.md` is created manually (outside `migrate_initiative.py`). | Process | Confirmed | Client | 2026-02-22 | Avoids extending migrator manifest semantics with unsupported content creation actions. | Client QA approval | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.md` |
| `T104-PH001-ST007-AC004-SES001-DEC005` | Rollback guarantee uses a known-good checkpoint; rollback manifest is supplemental (moves only). | Process | Confirmed | Client | 2026-02-22 | Provides conservative rollback assurances without relying on brittle reverse-rewrite logic. | Client QA approval | `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.md` |

---

## E. Actions / Carry-Forward (ACT Table)

| ID | Action | Owner | Status |
|:---|:-------|:------|:-------|
| `T104-PH001-ST007-AC004-SES001-ACT001` | Create AC004 SES001 session notes file (this file) | LLM_Consultant | `completed` |
| `T104-PH001-ST007-AC004-SES001-ACT002` | Register AC004 SES001 in the stream notes register Activity Notes Register table | LLM_Consultant | `completed` |
| `T104-PH001-ST007-AC004-SES001-ACT003` | Amend AC004 activity plan to reflect DEC001–DEC005 (commissioning-ready) | LLM_Developer | `completed` |
| `T104-PH001-ST007-AC004-SES001-ACT004` | Execute TK001: freeze window + authoritative inventory file for P migration coverage | LLM_Developer | `pending` |
| `T104-PH001-ST007-AC004-SES001-ACT005` | Implement TK002 and TK003 script enhancements and produce dry-run evidence | LLM_Developer | `pending` |
| `T104-PH001-ST007-AC004-SES001-ACT006` | Prepare GATE-001 package: dry-run report + rollback checkpoint evidence | LLM_Developer | `pending` |

---

## F. Open Questions Register (OQ Table)

| ID | Topic | Question | Owner | Status | Needed By |
|:---|:------|:---------|:------|:-------|:----------|

_No open questions — commissioning decisions locked in this session._

---

## G. Session Handoff Pack

- **Decisions locked**: roadmap in `ssot/`; proposal "both" via activity-canonical + stream pointer; pre-migration validator profile suppresses noise only; concept stub created manually; rollback guarantee via known-good checkpoint.
- **Primary artifact updated**: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/plan_T104-PH001-ST007-AC004.md`
- **Register updated**: `prompt/artifacts/tasks/T104/workspace/PH001/ST007/notes_T104-PH001-ST007.md`

---

## H. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-22 | Initial | Activity session notes created for AC004 commissioning QA and plan amendment. 5 decisions captured (DEC001–DEC005). |
