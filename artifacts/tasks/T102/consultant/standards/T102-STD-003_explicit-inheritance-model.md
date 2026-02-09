# T102-STD-003 — Explicit Inheritance Model

## Specification

1) **T102-STD-003-CLAUSE-001 (Table Contracts)** 
    Epic dossier from `sps` and relevant sections from `request`, `concept`, and `design` MUST include an **Inherited Considerations** table with EXACTLY these columns:
    `Source Artifact | Scope ID | Category | Inherited Rule IDs`  
      - Source Artifact: one of `{SPS, CONCEPT, REQUEST, DESIGN}`.
      - Scope ID: [I-SID|E-SID|F-SID|S-SID]
      - Use repo-relative anchors when available (e.g., `SPS#t102-gdr-003-inheritance-model`).
      - Category: one of `{Assumptions, Constraints, Quality Goals, Dependencies, Implementation Guides, Notes, Governances, Architecture}`   
      - Inherited Rule IDs: back-ticked list of `ID (Title)` tokens; **≤5 items**;

    2) **T102-STD-003-CLAUSE-002 (Precedence)**
    **I-SID  > E-SID > F-SID >  S-SID**; variances require a local ADR that cites the parent.

    3) **T102-STD-003-CLAUSE-003 (Authoring Rules)**
      - Do **not** restate parent text; list IDs only (delta-only).
      - Prefer the **most critical ≤5** inherited IDs for scanability.
      - Link by anchor; avoid raw URLs.
      - When deviating, create a **variance ADR** in the local artifact.

## Decision Record

* **T102-STD-003-ADR-001 (Explicit Inheritance Model)** {#t102-std-003-explicit-inheritance}

  * **Context**
    Per `T102-GDR-003`, “delta-only” by habit does not avoid duplication and drift. This *mandates* explicit inheritance model. This ADR defines the **implementation contract** (tables, linking, precedence).

  * **Decision**
    Implement **Explicit ID Referencing** in addition to delta-only across all PM scopes:
        **Why**: Prevent rule duplication and governance drift that creates inconsistent decision authority and audit trail gaps across artifact hierarchy
        **What**: Each PM scope **implicitly inherits all higher-precedence rules** per the hierarchy (I-RIDs through S-ADRs) but **explicitly emphasizes only critical inherited items** via "Inherited Considerations" tables using ID references. All scopes record **only deltas/overrides** without restating upstream content verbatim. **Upstream scopes never reference downstream rules** - inheritance flows unidirectionally from higher or equal to lower precedence only.
        **Benefit**: Maintains single source of truth for governance while providing scannable inheritance visibility without verbose duplication

  * **Alternatives Considered**
    (a) **Delta-only model** (rejected): Informal convention proved insufficient;

  * **Consequences**
    (+) Short, scannable upstream references in every artifact; clean audit trail.  
        (+) Future validator can check presence/anchors without changing authoring flow.
        (±) Requires discipline to maintain ID-only references without restating parent content
        (-) Authors must navigate to parent artifacts to read full rule text when needed

## References

`T102-GDR-003 (Inheritance Model Standard)`, 
  `T102-IG-010 (Inheritance Model)`, 
  `T102-NOTE-004 (Inheritance Philosophy)`

## Provenance

`design_T102A-SPSST-S4.md`
