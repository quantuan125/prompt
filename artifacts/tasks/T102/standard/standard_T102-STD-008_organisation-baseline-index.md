# T102-STD-008 — Organisation Baseline Index

## Specification

1) **T102-STD-008-CLAUSE-001 (Canonical Placement)**
       - Each initiative SPS SHOULD include `III.B.1 Organization & Responsibilities` (baseline) as the canonical governance role mapping for the initiative.
       - Epics SHALL reference this baseline rather than duplicating it (see `T102A-STD-001`).

    2) **T102-STD-008-CLAUSE-002 (Required Content)**
       The baseline subsection SHALL contain, in this order:

       (a) **Role Definitions**
       - A single combined table that maps *actors* to conventional role titles and governance semantics.
       - The Role Definitions table SHALL use this exact schema:
         - `Actor | Role Title(s) | Decision Rights | Primary Responsibilities | Scope Notes`
       - `Role Title(s)` SHOULD use conventional PID/charter labels (e.g., Sponsor/Decision Owner, Project Manager, Product Lead, Technical Lead, Planner).
       - The table SHALL include every *actor label* referenced anywhere else in the initiative SPS (including all epic `##### iv. Governance & Roadmap` and `##### v. Feature Register` sections).
       - Minimum required actors (may be extended per initiative, but not omitted):
         - `Client`
         - `LLM_Consultant`
         - `LLM_Planner`
         - `LLM_Researcher`
         - `LLM_Developer`

       (b) **Governance RACI**
       - A RACI table with the exact column schema:
         - `Governance Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed)`
       - The table SHALL include, at minimum, these governance activities (row titles may be adapted, but intent must remain):
         - Approve Initiative baseline
         - Approve Epic baseline
         - Approve Feature baseline (Feature Request)
         - Approve cutover
       - Rows MAY be added for initiative-specific governance (e.g., “Approve architecture baseline”, “Approve data migration plan”), but SHOULD be kept stable and baseline-level.
       - RACI cells SHALL reference actors using the exact actor labels defined in the Role Definitions table above (no new actor labels introduced only inside the table).

    3) **T102-STD-008-CLAUSE-003 (Maintenance Policy)**
       - Update the baseline only when roles/responsibilities materially change.
       - Treat baseline edits as governance changes; maintain traceability via proposal/completion references where applicable.

## Decision Record

* **T102-STD-008-ADR-001 (Organisation Baseline Index)** {#t102-std-008-org-baseline-index}

  * **Context**
    Per `T102-GDR-008 (Organisation Baseline Standard)`, the initiative requires a stable org baseline so epic governance snapshots can reference consistent actor labels and decision rights without duplication or drift.

  * **Decision**
    Adopt `T102-STD-008` to standardize the structure and maintenance policy of the initiative-level `III.B` “Organization & Responsibilities” subsection.

  * **Alternatives Considered**
    (a) Embed governance RACI inside each epic — rejected (duplication and drift).

  * **Consequences**
    (+) Reduces drift by enforcing a single baseline
      (+) Improves consistency across epics within an initiative
      (±) Requires initial discipline to keep epics delta-only

## References

`T102-GDR-008 (Organisation Baseline Standard)`,
  `T102-GDR-003 (Inheritance Model Standard)`,
  `T102-STD-003 (Explicit Inheritance Model)`,
  `T102-STD-004 (Specification Standard & Guideline)`,
  `T102-STD-005 (ID Specification & Rules)`

## Provenance

- `prompt/artifacts/tasks/T102/T102A/workspace/PH000/proposal/proposal_T102A_governance_&_roadmap.md`
