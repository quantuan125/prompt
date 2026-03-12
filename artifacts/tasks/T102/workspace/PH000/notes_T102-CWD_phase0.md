---
artifact_type: 'NOTES'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '0'
version: '0.2.0'
date: '2026-01-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
roadmap_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/roadmap/plan_T102-PH000.md'
---

# PHASE NOTES INDEX: T102 (CWD) — Phase 0: Governance Realignment (STD + ADR)

<!--
AUTHORING GUIDELINES (INDEX-ONLY; NON-NORMATIVE)

Purpose:
- This file is the Phase 0 NOTES deliverable for Activity 1.2 in the roadmap.
- This file is an INDEX ONLY: registers + links. It must not carry long narrative minutes.
- Detailed minutes and option breakdowns live in Stream Notes files and are referenced here.

Non-normative rule:
- NOTES files record consultation memory (minutes, decisions, action items, open questions).
- NOTES files MUST NOT introduce new obligations; normative rules belong in STD/ADR/RID artifacts.

ID conventions (NOTES-local, not part of T102-STD-005 unless later promoted):
- Session ID: `T102-SES-###` (sequence, no reuse).
- Decision ID: `T102-DEC-###` (sequence, no reuse).
  - Decisions SHOULD carry `Type` and `Status` to support later promotion and supersession.
  - Promotion is recorded in the `Promotes To` column (e.g., `T102-ADR-###`, `T102-STD-###`, `T102-*-RID-###`).
-->

## I. QUICK SUMMARY (INDEX)

**Phase**: 0 (Governance Realignment: STD + ADR)  
**Status**: In Progress  
**Decision Owner**: Client  

**What this notes file is**: a Phase 0 index (sessions, decisions, actions, open questions).  
**What this notes file is not**: SSOT for standards/specs (those belong in SPS / Concept / proposal artifacts).

---

## II. LINKS REGISTER

| Item | Path |
|:--|:--|
| Roadmap (Phase 0) | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/plan_T102-PH000.md` |
| Stream 1 Notes | `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0_stream1.md` |
| ADR-004/ADR-005 Proposal Draft | `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor-adr-004-005.md` |
| Raw Consultation Transcript (2026-01-22) | `prompt/artifacts/tasks/T102/consultant/raw/raw_T102-CDW_phase0_2026-01-22_p5.md` |

---

## III. SESSIONS REGISTER

| Session ID | Date | Stream/Activity Coverage | Summary | Detailed Notes |
|:--|:--|:--|:--|:--|
| `T102-SES-001` | 2026-01-22 | Stream 1 (Initialization), Activities 1.1–1.3 | Locked governance realignment direction (STD vs ADR, IG vs INT split, provenance and reference style). | `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0_stream1.md` |

---

## IV. DECISIONS REGISTER (ROLL-UP)

<!--
AUTHORING GUIDELINES (DECISIONS REGISTER)
- This table is the roll-up index. Each row MUST point to a source session.
- Keep Decision text short; detail, options, and rationale expansion go in the stream/session notes.
- Use `Promotes To` when a decision is realized as a normative artifact (ADR/STD/RID). Once promoted,
  update `Status` to `Realized` (or `Superseded`) and add the authoritative target ID.
-->

| DEC-ID | Decision (Short) | Type | Status | Owner | Date | Source Session | Promotes To |
|:--|:--|:--|:--|:--|:--|:--|:--|
| `T102-DEC-001` | Reframe governance GDR into `STD` reference artifacts (Option Set: Drift Control / Option C) | Governance | Accepted | Client | 2026-01-22 | `T102-SES-001` | — |
| `T102-DEC-002` | Split normative vs informative: `STD` normative; `IG` informative; `INT` non-normative (Option Set: Normativity / Option 2) | Governance | Accepted | Client | 2026-01-22 | `T102-SES-001` | — |
| `T102-DEC-003` | Limit `STD` scope to I/E/F only | Governance | Accepted | Client | 2026-01-22 | `T102-SES-001` | — |
| `T102-DEC-004` | Allow shorthand references in bodies; full references in dedicated refs/index sections | Governance | Accepted | Client | 2026-01-22 | `T102-SES-001` | — |
| `T102-DEC-005` | Provenance uses repo-relative paths only | Governance | Accepted | Client | 2026-01-22 | `T102-SES-001` | — |

---

## V. ACTIONS REGISTER (ROLL-UP)

<!--
AUTHORING GUIDELINES (ACTIONS)
- Actions are execution commitments, not decisions. Keep them measurable and assign an Owner.
- If an action becomes a roadmap task, include a pointer to the Stream/Activity/Task ID.
-->

| ACT-ID | Action | Owner | Due | Status | Related Roadmap |
|:--|:--|:--|:--|:--|:--|
| `ACT-001` | Convert `notes_T102-CWD_phase0.md` to index-only and add Stream 1 detailed notes file | LLM_Consultant | — | Complete | Stream 1 / Activity 1.2 |

---

## VI. OPEN QUESTIONS REGISTER

| OQ-ID | Question | Owner | Status | Notes |
|:--|:--|:--|:--|:--|
| `OQ-001` | When to formalize NOTES-local IDs (`SES`, `DEC`) into T102-STD-005 taxonomy | Client | Open | Keep NOTES-local until stable; formalize only when enforcement is required. |
