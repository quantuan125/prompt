---
artifact_type: 'NOTES'
initiative_id: 'T102'
initiative_code: 'CWD'
phase: '0'
stream: '1'
version: '0.1.0'
date: '2026-01-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
roadmap_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md'
notes_index_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md'
---

# STREAM NOTES: T102 (CWD) — Phase 0 / Stream 1: Initialization of Workspace Artifacts

<!--
AUTHORING GUIDELINES (STREAM NOTES; NON-NORMATIVE)

Purpose:
- This file holds the detailed consultation record for Stream 1 (Activities 1.1–1.3).
- It is the detail layer referenced by the Phase Notes Index (`notes_T102-CWD_phase0.md`).

Rules:
- Stream Notes MAY include narrative minutes, option breakdowns, and rationale expansion.
- Stream Notes MUST NOT introduce new obligations. If an item is intended to be enforceable, it MUST be promoted
  into a normative artifact (STD/ADR/RID) and referenced from here.

ID conventions (NOTES-local):
- Session ID: `T102-SES-###` (sequence, no reuse).
- Decision ID: `T102-DEC-###` (sequence, no reuse).
- Action ID: `ACT-###` (sequence, no reuse).

Options hygiene:
- When the phrase “Option X” is used, it MUST be disambiguated by naming the Option Set.
  Example:
  - Option Set: Drift Control (GDR/ADR) → Options A/B/C/D
  - Option Set: Normativity (STD/IG/INT) → Options 1/2/3
-->

## I. STREAM SUMMARY

**Stream**: 1 (Initialization of Workspace Artifacts)  
**Scope**: Roadmap scaffolding, notes scaffolding, changelog scaffolding (no SSOT/proposal edits)  
**Status**: In Progress  

**Key outcomes captured in this stream**:
- Governance direction locked for Phase 0 work: `STD` (reference-style) vs `ADR` (decision record), and `STD` vs `IG` vs `INT` semantics.
- Provenance and reference-style constraints clarified for Phase 0 artifacts (repo-relative provenance; shorthand vs full refs).

---

## II. SESSION RECORDS

### `T102-SES-001` — 2026-01-22 (Stream 1: Activities 1.1–1.3)

**Participants**: LLM_Consultant, Client  
**Primary focus**: Resolve governance drift risks and lock the governance realignment direction before executing Streams 2+.

#### A. Narrative Summary (Minutes-Style)

The session focused on the known failure mode of “paired-document drift” (two artifacts covering the same ground with the same headings) and the knock-on effects in an agentic workflow where long-term memory needs stable references. We aligned on reframing governance away from decision-record-shaped artifacts (GDR) and toward reference-style normative standards (`STD`) to cleanly separate “what must be true” from “why we decided it.”

We also clarified that “guidance becoming law” is a recurring risk when implementation guidance (`IG`) is allowed to contain new obligations. The session therefore evaluated normativity split options and selected a structure that keeps enforceable rules in `STD`, keeps `IG` as informative how-to, and reserves `INT` for non-normative integration coordination notes.

Finally, we agreed on provenance and reference practices to keep artifacts deterministic and readable inside the repository: provenance references are repo-relative paths only; shorthand references are acceptable inline, with full references reserved for dedicated index/reference sections.

#### B. Options Considered (Disambiguated Option Sets)

##### Option Set 1: Drift Control (GDR + ADR duplication)

**Option A — Keep GDR + ADR but make them structurally different**
- Keep the “two artifact types” taxonomy, but avoid duplication by ensuring GDR does not reuse ADR-style headings.
- Intended as a minimal-disruption transition option.

**Option B — Collapse to one decision-record type (ADR only)**
- Remove GDR and represent governance vs architecture via ADR metadata.
- Removes paired-document drift but risks pushing “reference standards” into decision records.

**Option C — Convert governance into Standards (`STD`), not decision records (Selected)**
- Replace governance-shaped GDR content with reference-style standards (`STD`), while keeping ADRs as decision records.
- Chosen because it is the cleanest structural separation and reduces drift risk in the long term.

**Option D — RFC-like standards lifecycle (Variant of Option C)**
- Same conceptual separation as Option C, but with stricter “obsoletes/updates” change control semantics.
- Not selected in this session; held as an escalation path if stronger drift control is later required.

##### Option Set 2: Normativity (where obligations live)

**Option 1 — All IID (`IG`/`INT`) non-normative**
- Simplifies enforcement but may force practical standards into requirements/other artifacts.

**Option 2 — Split: `STD` normative reference; `IG` informative; `INT` non-normative (Selected)**
- Keeps enforceable standards without turning “how-to” guidance into obligations.

**Option 3 — Allow normative `IG` with stronger gates**
- Minimal taxonomy change but high cultural/tooling burden and higher drift risk.

#### C. Decisions Made (Detailed)

<!--
AUTHORING GUIDELINES (DECISIONS TABLE)
- Include an Evidence pointer to the raw consultation transcript (repo-relative path + line anchors).
- `Promotes To` is optional now; fill it when the decision is realized as ADR/STD/RID.
-->

| DEC-ID | Decision | Type | Status | Owner | Date | Evidence | Promotes To |
|:--|:--|:--|:--|:--|:--|:--|:--|
| `T102-DEC-001` | Adopt Drift Control Option C: replace governance-shaped GDR with reference-style `STD` | Governance | Accepted | Client | 2026-01-22 | `prompt/artifacts/tasks/T102/consultant/raw/raw_T102-CDW_phase0_2026-01-22_p5.md#L651` | — |
| `T102-DEC-002` | Adopt Normativity Option 2: `STD` is normative reference; `IG` is informative how-to; `INT` is non-normative integration notes | Governance | Accepted | Client | 2026-01-22 | `prompt/artifacts/tasks/T102/consultant/raw/raw_T102-CDW_phase0_2026-01-22_p5.md#L1059` | — |
| `T102-DEC-003` | Restrict `STD` allowed scopes to I/E/F only | Governance | Accepted | Client | 2026-01-22 | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md#L24` | — |
| `T102-DEC-004` | Allow shorthand references inline; require full references in dedicated references/index sections | Governance | Accepted | Client | 2026-01-22 | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md#L25` | — |
| `T102-DEC-005` | Provenance MUST use repo-relative paths only | Governance | Accepted | Client | 2026-01-22 | `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md#L23` | — |

#### D. Actions / Next-Activity Guidance

| ACT-ID | Action | Owner | Status | Related Roadmap |
|:--|:--|:--|:--|:--|
| `ACT-001` | Convert Phase 0 notes into an index file; place detailed Stream 1 session content into this Stream Notes file | LLM_Consultant | Complete | Stream 1 / Activity 1.2 |
| `ACT-002` | Proceed to Stream 2 to migrate ADR-004/ADR-005 bodies into the proposal draft (after Stream 1 scaffolding complete) | LLM_Consultant | Planned | Stream 2 |

---

## III. REFERENCES (REPO-RELATIVE ONLY)

- Roadmap: `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/roadmap_T102-CWD_phase0.md`
- Phase Notes Index: `prompt/artifacts/tasks/T102/consultant/workspace/notes/notes_T102-CWD_phase0.md`
- Raw consultation transcript: `prompt/artifacts/tasks/T102/consultant/raw/raw_T102-CDW_phase0_2026-01-22_p5.md`
