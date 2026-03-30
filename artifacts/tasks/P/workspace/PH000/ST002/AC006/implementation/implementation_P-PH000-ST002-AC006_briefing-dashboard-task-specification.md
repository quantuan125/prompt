---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-TK005'
version: '1.0.0'
date: '2026-03-30'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
execution_audience: 'assistant'
purpose: 'Detailed post-gate execution specification for AC006 briefing dashboard creation as a separate derived file bounded to active-work continuity, recent movement, and dependency watch visibility.'
---

# IMPLEMENTATION (Task Specification): AC006 Briefing Dashboard Creation

## I. PURPOSE & AUTHORITY
- Purpose: Specify the exact downstream execution required to create the AC006 client-facing briefing dashboard after `GATE-001` approval.
- Authority chain: The AC006 plan authorizes the feature -> the TK002 comparative analysis selects the architecture -> the TK003 standards-input proposal defines the briefing convention -> this artifact specifies HOW the assistant executes `TK008`.
- Audience: `LLM_Assistant`
- This artifact does NOT hold a GDR. Execution under this artifact MUST NOT begin until `P-PH000-ST002-AC006-GATE-001` records an approving client decision.
- The authoritative source remains `prompt/artifacts/tasks/P/status/status_program.yaml`. The briefing is a derived client continuity surface only.

## II. TASK SCOPE
- Governing plan task: `P-PH000-ST002-AC006-TK005`
- Trigger: TK002 and TK003 established that AC006 needs a separate, bounded briefing dashboard rather than either an embedded narrative section or an ephemeral-only skill output.
- Deliverable contract:
  - new `prompt/artifacts/tasks/P/status/briefing_program.md`
  - no changes to `status_program.yaml`
  - no changes to `status_program.md` beyond any later independently commissioned refresh work

## III. SPECIFICATION ITEMS

### SPEC-001 - Create the separate briefing dashboard artifact at the approved path

| Field | Detail |
|:--|:--|
| Requirement Source | TK002 recommendation; TK003 approved placement convention |
| Target file(s) | `prompt/artifacts/tasks/P/status/briefing_program.md` |
| Required end-state posture | A new standalone Markdown briefing file exists at the approved path and presents a concise client-facing dashboard without introducing a new authoritative state source. |
| Explicit non-target / do-not-change constraints | Do NOT modify `status_program.yaml`. Do NOT splice this content into `status_program.md`. Do NOT create automation, scripts, or regeneration tooling. |
| Validation check | The file exists at the exact path, uses the required section structure, and clearly labels itself as derived from the authoritative ledger. |
| Blocking ambiguity rule | If the approved path already contains a different governed artifact, stop and escalate instead of overwriting it. |
| Status | `open` |

#### Implementation Detail

1. Create `prompt/artifacts/tasks/P/status/briefing_program.md` as a plain Markdown document.
2. Begin the file with:
   - `# Program Briefing Dashboard - P`
   - a short authority note stating that the dashboard is derived from `status_program.yaml` and is not an authority surface
   - an `As Of` line using the current ledger `as_of` / `last_updated` date
3. The file must contain exactly these three major sections, in this order:
   - `## Active Work Briefing`
   - `## Recent Movement Watchlist`
   - `## Dependency Watchlist`
4. Do not add a health table, operational protocol section, or a full evidence digest to this file.

### SPEC-002 - Populate Active Work Briefing from the authoritative ledger

| Field | Detail |
|:--|:--|
| Requirement Source | TK003 conventions `CONV-003`, `CONV-004`, and `CONV-005` |
| Target file(s) | `prompt/artifacts/tasks/P/status/briefing_program.md`; `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Required end-state posture | `Active Work Briefing` lists every ledger entry whose `status` is `in_progress`, with bounded continuity fields and latest-handoff pointers where available. |
| Explicit non-target / do-not-change constraints | Do NOT infer activity state from the narrative when the ledger already provides it. Do NOT include `planned` or `completed` entries in this section. |
| Validation check | Every row in `Active Work Briefing` maps to an `in_progress` ledger entry and no non-`in_progress` row appears there. |
| Blocking ambiguity rule | If the ledger contains malformed or incomplete rows that prevent deterministic extraction, stop and escalate rather than guessing values. |
| Status | `open` |

#### Implementation Detail

1. Read `status_program.yaml` as the primary source.
2. Build the `Active Work Briefing` table with these exact columns:
   - `Scope UID`
   - `Name`
   - `Status`
   - `Last Updated`
   - `Latest Handoff`
   - `Why It Matters Now`
3. Include one row for every ledger entry with `status: in_progress`.
4. For `Latest Handoff`:
   - inspect the entry's `evidence` list
   - if there is at least one `type: session` item, use the most recent session-note path
   - otherwise use `—`
5. For `Why It Matters Now`, use a short one-line summary derived from the ledger name plus any open critical dependency or recent session evidence.

### SPEC-003 - Populate Recent Movement Watchlist as a bounded continuity section

| Field | Detail |
|:--|:--|
| Requirement Source | TK003 conventions `CONV-004` and `CONV-006` |
| Target file(s) | `prompt/artifacts/tasks/P/status/briefing_program.md`; `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Required end-state posture | `Recent Movement Watchlist` includes only non-terminal activities that were updated in the latest ledger cycle and matter for short-horizon continuity. |
| Explicit non-target / do-not-change constraints | Do NOT turn this section into a second full status table. Do NOT include completed items unless the approved convention changes later. |
| Validation check | Every row is a non-terminal ledger entry whose `last_updated` equals the top-level ledger `last_updated`, and the section remains materially smaller than the full status table. |
| Blocking ambiguity rule | If too many rows qualify and the section would become a second full digest, include only the rows with the strongest immediate continuity value and note that the section is intentionally bounded. |
| Status | `open` |

#### Implementation Detail

1. Build a second table under `## Recent Movement Watchlist` with these exact columns:
   - `Scope UID`
   - `Name`
   - `Current Status`
   - `Recent Signal`
   - `Latest Handoff`
2. Source candidates from ledger entries where:
   - `status` is `planned` or `in_progress`
   - `last_updated` equals the ledger top-level `last_updated`
3. Exclude rows already covered in `Active Work Briefing` unless their recent signal materially adds new continuity value.
4. For `Recent Signal`, summarize the evidence or update reason in one short phrase, for example `dependency reversal recorded`, `new task register amendment`, or `recent session note added`.
5. Keep the section intentionally smaller than the full status narrative. If many rows qualify, prefer the ones most relevant to the AC006 continuity story and immediate upstream/downstream coordination.

### SPEC-004 - Populate Dependency Watchlist as the only cross-scope prioritization signal in V1.1

| Field | Detail |
|:--|:--|
| Requirement Source | TK003 convention `CONV-007` |
| Target file(s) | `prompt/artifacts/tasks/P/status/briefing_program.md`; `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Required end-state posture | `Dependency Watchlist` lists only open critical dependencies touching items surfaced earlier in the briefing. |
| Explicit non-target / do-not-change constraints | Do NOT introduce scoring, prioritization ranks, or a new planning framework in this section. |
| Validation check | Every row corresponds to a ledger dependency edge with `status: open` and `criticality: critical`, and at least one endpoint appears in the briefing's first two sections. |
| Blocking ambiguity rule | If a dependency cannot be tied back to a surfaced activity, omit it instead of widening the watchlist. |
| Status | `open` |

#### Implementation Detail

1. Under `## Dependency Watchlist`, create a table with these exact columns:
   - `Upstream`
   - `Downstream`
   - `Status`
   - `Criticality`
   - `Why It Matters`
2. Source rows only from `dependencies[]` objects in `status_program.yaml` where:
   - `status` is `open`
   - `criticality` is `critical`
   - either `from_id` or `to_id` matches an activity already surfaced in `Active Work Briefing` or `Recent Movement Watchlist`
3. In `Why It Matters`, give one short client-facing explanation tied to the surfaced activity, for example `blocks future commissioning of AC005` or `keeps active execution dependent on upstream closeout`.
4. Do not add a fourth section for prioritization, ranking, or recommendations.

### SPEC-005 - Validate the briefing artifact against the approved AC006 boundary

| Field | Detail |
|:--|:--|
| Requirement Source | TK005 success criteria; TK003 approved conventions |
| Target file(s) | `prompt/artifacts/tasks/P/status/briefing_program.md`; `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Required end-state posture | The final briefing is deterministic, bounded, readable, and clearly subordinate to the ledger-first hierarchy. |
| Explicit non-target / do-not-change constraints | Do NOT back-edit the ledger or narrative to force-fit the briefing. Do NOT create automation or helper scripts during validation. |
| Validation check | Confirm the file has exactly three sections, the section populations follow the rules above, and the authority note is present. |
| Blocking ambiguity rule | If the briefing can only be made to fit by inventing new conventions beyond TK003, stop and escalate instead of widening AC006 V1.1. |
| Status | `open` |

#### Implementation Detail

1. Read the completed `briefing_program.md` top to bottom.
2. Confirm it has exactly three sections and no extra protocol/health/digest sections.
3. Spot-check a sample of rows from each section against `status_program.yaml`.
4. Confirm the file never claims to be authoritative and always points back to the ledger.

## IV. IMPLEMENTATION SEQUENCE
1. Create the new briefing file scaffold.
2. Populate `Active Work Briefing`.
3. Populate `Recent Movement Watchlist`.
4. Populate `Dependency Watchlist`.
5. Run the validation pass.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| TK002 Comparative Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_briefing-dashboard-comparative-assessment.md` |
| TK003 Standards Input | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/proposal/proposal_P-PH000-ST002-AC006_briefing-dashboard-standards-input.md` |
| Status Ledger | `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Status Narrative | `prompt/artifacts/tasks/P/status/status_program.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-30 | Initial | Authored the AC006 briefing dashboard creation specification covering the separate `briefing_program.md` target, exact three-section model, ledger-first derivation rules, and bounded dependency-watch scope. |
