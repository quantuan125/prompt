---
artifact_type: 'PROPOSAL'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST002'
activity_id: 'P-PH000-ST002-AC006'
task_id: 'P-PH000-ST002-AC006-TK003'
version: '1.0.0'
date: '2026-03-30'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md'
analysis_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_briefing-dashboard-comparative-assessment.md'
target_standards:
  - 'AC006 briefing dashboard convention'
  - 'Future status-system initiative briefing expansion'
purpose: 'Structured standards-input proposal for the AC006 briefing dashboard convention and implementation boundary.'
---

# PROPOSAL: Standards Input - AC006 Briefing Dashboard Convention

## I. PURPOSE

- Proposal objective: define the decision-ready convention for the AC006 client-facing briefing dashboard before any concrete briefing artifact is created.
- Input scope: placement, derivation hierarchy, V1 section model, filtering boundary, and execution boundary for the briefing dashboard only.
- Target standards: `AC006 briefing dashboard convention`; `Future status-system initiative briefing expansion`

## II. CURRENT STATE SUMMARY

### A. Baseline

- TK002 selected a separate briefing file over both an embedded `status_program.md` section and a skill-generated-only output.
- `status_program.yaml` already contains the canonical activity state needed to seed a briefing surface.
- `status_program.md` is already the derived narrative and protocol surface; it should not become the primary client continuity dashboard.
- The client needs a stable surface for active work, recent movement, and immediate dependency watch items without reading the full narrative system-of-record.

### B. Problems / Gaps

| Gap ID | Category | Description | Impact |
|:--|:--|:--|:--|
| GAP-001 | structure | No bounded client-facing briefing surface exists today. | Clients must read the full narrative and manually navigate to recent handoff context. |
| GAP-002 | references | The source hierarchy for a briefing dashboard is not yet explicit. | Without a source hierarchy, a future briefing artifact could drift from the authoritative ledger. |
| GAP-003 | workflow | Cross-scope prioritization demand is real, but full prioritization logic exceeds AC006 V1.1. | Without a bounded convention, the feature could sprawl into a broader planning system. |

## III. PROPOSED CONVENTIONS

### A. Convention Set

| Convention ID | Rule | Rationale | Authority Link |
|:--|:--|:--|:--|
| CONV-001 | The active pre-implementation authority for the briefing dashboard is this `standards_input` proposal, not a prematurely created `briefing_program.md` file. | Keeps the consultation-only gate clean and avoids treating an unapproved concrete artifact as active authority. | TK002 comparative analysis |
| CONV-002 | The approved placement for the V1.1 briefing dashboard is `prompt/artifacts/tasks/P/status/briefing_program.md`. | A separate file gives the clearest client-reading surface and the lowest authority-contamination risk. | TK002 comparative analysis |
| CONV-003 | `status_program.yaml` is the authoritative data source for the briefing dashboard. `status_program.md`, notes registers, and session notes are supporting lineage/pointer surfaces only. | Preserves the ledger-first hierarchy and prevents the briefing from becoming a competing authority surface. | `status_program.yaml`; workspace documentation rules |
| CONV-004 | The V1.1 briefing dashboard contains exactly three sections: `Active Work Briefing`, `Recent Movement Watchlist`, and `Dependency Watchlist`. | Gives the client a bounded continuity surface without overloading the feature. | TK002 comparative analysis |
| CONV-005 | `Active Work Briefing` includes only activities whose ledger status is `in_progress`. | Matches the primary client question: what is active now? | TK001 audit; TK002 comparative analysis |
| CONV-006 | `Recent Movement Watchlist` includes a bounded set of recently updated non-terminal activities only when they materially affect short-horizon continuity. | Preserves continuity value while avoiding a second full status digest. | TK001 audit; TK002 comparative analysis |
| CONV-007 | `Dependency Watchlist` includes only open critical dependencies touching activities listed in the first two sections. | Gives a minimal cross-scope prioritization signal without expanding into a full prioritization engine. | TK001 audit; TK002 comparative analysis |
| CONV-008 | Each briefing row MUST include a latest-handoff pointer when a relevant recent session note exists; otherwise the field is `—`. | Turns the briefing into a continuity surface rather than only a filtered status table. | TK001 audit |
| CONV-009 | The briefing dashboard remains prompt-assist-only and manually refreshed in AC006 V1.1. It MUST NOT introduce hooks, scripts, or automation. | Keeps AC006 within the approved bounded rollout. | AC006 executive summary; TK001 audit |

### B. Compatibility Notes

- This proposal does not change the authority of `status_program.yaml` or `status_program.md`.
- This proposal does not authorize deeper prioritization logic, automatic regeneration, or future-initiative commissioning.
- The later TK005 implementation specification must operationalize this convention exactly and must not widen the feature beyond the bounded V1.1 section model.

## IV. DECISION REQUESTS

| Decision ID | Prompt | Options | Recommendation | Owner |
|:--|:--|:--|:--|:--|
| DEC-001 | Where should the briefing dashboard live in AC006 V1.1? | (a) separate `briefing_program.md`; (b) new section in `status_program.md`; (c) skill-generated-only output | **(a)** | Client |
| DEC-002 | What should be the authoritative source hierarchy for the briefing dashboard? | (a) ledger first, supporting pointers second; (b) status narrative as the primary source; (c) latest session notes as the primary source | **(a)** | Client |
| DEC-003 | What should the V1.1 section model be? | (a) Active Work + Recent Movement + Dependency Watchlist; (b) Active Work only; (c) full status-narrative mirror | **(a)** | Client |
| DEC-004 | How far should cross-scope prioritization go in AC006 V1.1? | (a) bounded dependency watchlist only; (b) full prioritization model now; (c) no cross-scope visibility at all | **(a)** | Client |
| DEC-005 | Should AC006 introduce briefing automation? | (a) no, manual prompt-assist-only refresh; (b) yes, automation now | **(a)** | Client |

## V. IMPACT AND RISKS

### A. Impact Assessment

- Positive outcomes:
  - gives the client a dedicated continuity surface without overloading the authoritative status narrative
  - keeps the data hierarchy clean and auditable
  - provides TK005 with a deterministic execution boundary
- Tradeoffs:
  - introduces another derived artifact to maintain
  - requires disciplined manual refresh to avoid stale briefing content
  - intentionally defers richer prioritization logic to later work

### B. Risks

| Risk ID | Description | Severity | Mitigation |
|:--|:--|:--|:--|
| RISK-001 | Authors may treat the briefing as a co-equal authority surface instead of a derived client view. | medium | The convention explicitly binds the briefing to the ledger-first hierarchy and keeps it prompt-assist-only. |
| RISK-002 | The recent-movement section could expand toward a second status digest. | medium | Keep the section bounded to materially relevant non-terminal changes only. |
| RISK-003 | Clients may ask for richer prioritization once the dependency watchlist exists. | medium | Defer full prioritization logic to the future status-system initiative. |

## VI. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/plan_P-PH000-ST002-AC006.md` |
| Supporting Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_briefing-dashboard-comparative-assessment.md` |
| TK001 Audit | `prompt/artifacts/tasks/P/workspace/PH000/ST002/AC006/analysis/analysis_P-PH000-ST002-AC006_session-close-and-briefing-gap-audit.md` |
| Status Ledger | `prompt/artifacts/tasks/P/status/status_program.yaml` |
| Status Narrative | `prompt/artifacts/tasks/P/status/status_program.md` |

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-30 | Initial | Created the AC006 briefing dashboard standards-input proposal defining the separate-file placement, ledger-first derivation hierarchy, bounded V1.1 section model, and manual prompt-assist-only execution boundary. |
