---
artifact_type: 'COMMUNICATION_BRIEF'
initiative_id: 'T102'
epic_id: 'T102A'
phase_id: 'PH001'
date: '2026-02-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_role: 'T102A Epic Owner'
priority: 'HIGH'
subject: 'Decision update — Adopt Option (c) for Issues & Risks hosting (SPS canonical + Concept aggregation) and T102A planning impacts'
---

# Communication Brief: T102A — Option (c) I&R Hosting Decision Impacts

## 1) Decision Summary (What changed)

The Client has locked **Option (c)** as the baseline Issues & Risks (I&R) hosting architecture:

- **SPS remains canonical** for Initiative + Epic I&R tables (authoritative lifecycle fields + authoritative row set).
- **Concept becomes the aggregation dashboard** for cross-scope I&R visibility, and is explicitly:
  - **pointers-only** (link-don’t-duplicate),
  - **non-normative** (audit/navigation surface only; not canonical I&R host).

Decision evidence:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST004/snotes/snotes_T102-PH001-ST004-SES001.md`
- `prompt/artifacts/tasks/T102/workspace/PH001/ST004/analysis/analysis_T102-PH001-ST004_external-review_IandR-hosting-architecture.md`

## 2) Why this matters to T102A (SPS epic)

T102A’s SPS dossier work is directly coupled to:

1) **Canonical I&R tables remain in SPS**: T102A should continue to treat SPS as the authoritative I&R surface for Epic scope.
2) **SPS context-load pressure is addressed by Concept aggregation**: T102A does **not** need to implement immediate SPS modularization solely to achieve cross-scope I&R visibility.
3) **New operating responsibility appears**: Concept I&R aggregation must be maintained as part of the overall governance operating model (not “only T102C”). Canonical content remains protected in SPS, but the dashboard must not drift.

## 3) What does NOT change (avoid unnecessary scope creep)

- No immediate SPS annex/modularization work is required for Option (c) to function.
- No change to “canonical = SPS” posture for Initiative/Epic I&R.
- No automation/tooling requirement is introduced (manual verification remains acceptable in Phase 1).

## 4) Trigger-based follow-ups T102A should plan for

Option (c) buys time, but it does not eliminate growth. T102A should treat modularization as **trigger-based**, not urgent:

- Define a modularization trigger such as:
  - SPS word-count threshold, and/or
  - Epic dossier count threshold.

When/if triggers are hit, the documented evolution path may move toward a “dedicated register” pattern (Option (e)) as a future phase decision.

## 5) Near-term dependencies (where this will be executed)

The standards amendments are planned in:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST005/plan_T102-PH001-ST005.md` (draft amendments; gated approvals)

The transition execution work (Concept hygiene + Concept I&R aggregation + SPS pointer blocks) is proposed/registered in:
- `prompt/artifacts/tasks/T102/workspace/PH001/ST006/plan_T102-PH001-ST006.md` (gated on ST005 approvals)

## 6) Requested T102A owner acknowledgements

1) Confirm T102A will not pursue immediate SPS modularization purely due to I&R roll-up needs.
2) Confirm T102A will incorporate a modularization trigger definition into PH001 planning artifacts when appropriate.
3) Confirm T102A accepts that Concept aggregation maintenance is a shared operating-model concern (even though canonical remains in SPS).
