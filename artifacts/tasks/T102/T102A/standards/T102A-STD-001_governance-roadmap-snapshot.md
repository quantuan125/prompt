# T102A-STD-001 — Governance & Roadmap Snapshot

## Specification

1) **T102A-STD-001-CLAUSE-001 (Canonical Placement & Title)**
       - Each Epic dossier SHALL include a subsection titled exactly: `##### iv. Governance & Roadmap`.
       - The subsection SHALL appear after `Inherited Considerations` and before `Feature Register` in the Epic dossier skeleton.

    2) **T102A-STD-001-CLAUSE-002 (Section Structure)**
       The section SHALL contain, in this order:
       - **Scope & Ownership**
       - **Phase & Gates** (table; indicative; no fixed dates)
       - **References**

    3) **T102A-STD-001-CLAUSE-003 (Scope & Ownership Rules)**
       - Scope & Ownership SHALL name the Decision Owner and the Epic Lead at minimum.
       - If present, Initiative Lead, Research Authority, and Technical Authority MAY be listed for clarity.
       - Scope & Ownership SHOULD include a single baseline reference line pointing to the initiative-level Org baseline (see `T102-STD-008`).

    4) **T102A-STD-001-CLAUSE-004 (Baseline Alignment)**
       - The initiative-level **Organization & Responsibilities** SHALL be defined in `III.B` and treated as the canonical source of truth (see `T102-STD-008 (Organisation Baseline Standard)`).
       - The Epic dossier SHALL NOT duplicate baseline RACI. Instead, the Epic’s Governance & Roadmap section SHALL:
         - reference the baseline, and
         - express epic-specific execution signals via the **Phase & Gates** table (Phase Lead and gate exits).

    5) **T102A-STD-001-CLAUSE-005 (Org & Responsibilities Boundaries)**
       - Org & Responsibilities SHALL map responsibilities only for governance events (phase/baseline approvals and handoffs).
       - Org & Responsibilities SHALL NOT include story/task-level responsibility assignment.
       - Feature lead/ownership remains a Feature Register concern (governed by `T102A-STD-002`).

    6) **T102A-STD-001-CLAUSE-006 (Phase & Gates Contract)**
       The **Phase & Gates** table SHALL use this exact schema:
       - `Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link`
       Fill rules:
       - `Phase`: numeric phase sequence starting at 0.
       - `Title`: short, Title Case with **bold heading**; stable across minor plan revisions.
       - `Intent`: one sentence describing purpose; governance-level, not task-level.
       - `Key Exit Milestone`: one sentence describing the approval-ready exit signal (evidence-linked where possible).
       - `Duration Band`: optional band (e.g., “1–2 sessions”); SHALL be `—` if unknown.
       - `Gate Approver (A)`: the Decision Owner role for phase exit (typically `Client`).
       - `Phase Lead (R)`: the accountable coordinator for producing the exit package (typically `LLM_Consultant`).
       - `Plan Link`: repo-relative link to the plan artifact governing that phase; MAY be shared across phases, but SHOULD be split per phase over time.

    7) **T102A-STD-001-CLAUSE-007 (Operational Boundaries)**
       - Governance & Roadmap SHALL NOT contain sprint calendars, capacity plans, or WBS task breakdown.
       - Story-level acceptance criteria belong in Feature Requests and Stories, not in the Phase & Gates table.

    8) **T102A-STD-001-CLAUSE-008 (References Semantics)**
       - References SHOULD link to the external PM tracking system (if used) and evidence artifacts for gate completion (proposals/completions/validation notes).
       - References SHOULD include evidence links for checkpoint completion when available (proposal approvals, completion artifacts, validation notes).
       - References SHOULD NOT duplicate plan links already present in the Phase & Gates table.

    9) **T102A-STD-001-CLAUSE-009 (Maintenance Policy)**
       - The Governance & Roadmap snapshot SHALL be updated only when a phase gate is approved or when a material governance baseline change occurs.
       - Day-to-day schedule drift remains in plan artifacts / external PM tools referenced from the snapshot.

## Decision Record

* **T102A-STD-001-ADR-001 (Governance & Roadmap Snapshot)** {#t102a-std-001-governance-roadmap-snapshot}

  * **Context**
    Per `T102A-GDR-001 (Governance Snapshot Standard)`, each Epic in an SPS must include a concise governance & roadmap snapshot that preserves traceability into living plans without importing operational planning detail into the SPS.

  * **Decision**
    Adopt `T102A-STD-001`, establish a single, mandatory structure and maintenance policy for every Epic subsection titled **“Governance & Roadmap”**.

  * **Alternatives Considered**
    (a) Embed operational plans inside SPS — rejected (creates churn and breaks governance snapshot intent).
      (b) Remove roadmap/checkpoints from SPS entirely — rejected (reduces governance visibility and weakens handoff oversight).

  * **Consequences**
    (+) Separates stable governance snapshot from living plans while preserving traceability.
      (+) Reduces role confusion by splitting “owner roster” from “gate responsibilities”.
      (+) Enables consistent epic governance reporting across initiatives.
      (±) Requires discipline: only update the snapshot at gates/baseline changes.
      (-) Some existing epics may require refactor to align with the baseline/delta model.

## References

`T102A-GDR-001 (Governance Snapshot Standard)`,
  `T102A-GDR-002 (Governance Freeze Standard)`,
  `T102-STD-004 (Specification Standard & Guideline)`,
  `T102-STD-005 (ID Specification & Rules)`,
  `T102-STD-008 (Organisation Baseline Standard)`,
  `T102A-STD-002 (Feature Register Index)`,
  `T102-RES-002 (Roadmap Viability)`,
  `T102A-RES-001 (SPS Workflow Optimization)`

## Provenance

`concept_T102-CONSULTANT.md`
  `report_T102-CONSULTANT_roadmap-viability.md`
  `report_T102A-SPS_sps-workflow-optimization.md`
