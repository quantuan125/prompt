# T102-STD-001 — Consultancy Operating Model

## Specification

1) **T102-STD-001-CLAUSE-001 (SPS Implementation)** 
      - Project Initiation Document (PID) structure with initiative/epic governance scope
      - Initiative Considerations framework: assumptions, constraints, quality goals, dependencies, implementation guidance, notes/parking lot
      - Initiative GDR Index for governance decision traceability
      - Epic dossier pattern: YAML identity, purpose/scope, governance table, inherited considerations table, quality goals, dependencies, feature register, epic GDR Index

    2) **T102-STD-001-CLAUSE-002 (REQUEST Implementation)** 
      - Business Requirements Document (BRD) + System Requirements Specification (SRS) structure
      - Feature-scoped requirements with story-level acceptance criteria in Gherkin format
      - Inherited considerations table referencing governing SPS rules with delta-only additions
      - No embedded decision records (link to Concept ADRs only via canonical links)
      - Gate approval checkpoints before Detailed Design work authorization

    3) **T102-STD-001-CLAUSE-003 (CONCEPT Implementation)** 
      - Concept MUST serve as the initiative bridge / process manual, the coordination audit surface, and the handoff authority surface, following `T102C-STD-001 (Concept Architectural Framework)`.
      - Concept MAY contain an ADR compendium, but it MUST NOT be framed as "ADR-only"; it MUST also host the initiative-level operating rules and audit-surface registers required for cross-scope coordination.
      - Decision record bodies in Concept MUST follow the uniform ADR structure: `Context→Decision→Specification→Consequences→Alternatives Considered→References`, using repo-relative links.
      - Concept registers MUST follow the obligations in `T102-STD-006 (Research Artifacts Index)` and related register standards; registers MUST be pointers-first and MUST NOT duplicate canonical bodies owned by other artifact types.

      - **T102-STD-001-CLAUSE-003A (Authority Tiers)**
        - Concept content MUST be explicitly authorable into three authority tiers:
          - Tier 1: **Normative bodies** (standards and accepted architectural decisions, including nested ADR rationale when present).
          - Tier 2: **Authoritative snapshots** (handoff package manifests and acceptance signals used for gates/handoffs).
          - Tier 3: **Audit registers** (pointers-only inventories for coordination, drift detection, and navigation).

      - **T102-STD-001-CLAUSE-003B (Strict Exclusions)**
        - Concept MUST NOT host:
          - Full requirements bodies (owned by Request artifacts)
          - Full design bodies (owned by Design artifacts)
          - Duplicated commissioned research bodies (owned by research brief/report artifacts indexed per `T102-STD-006`)
          - Canonical Issues & Risks tables for a scope (owned by that scope’s SSOT artifact; Concept may provide pointers-only aggregation views)

      - **T102-STD-001-CLAUSE-003C (Coordination Responsibilities Allocation)**
        - SPS and Request artifacts MUST contain embedded “minimum viable” local emphasis needed to author/approve the local scope without re-listing full cross-scope inventories.
        - Concept MUST contain cross-scope inventories/registers and drift indicators as the coordination audit surface.
        - INT MUST remain non-normative guidance and MUST be promoted when it becomes relied-upon policy per `T102-STD-005-CLAUSE-005C (Integration Guidance Rules)`.

      - **T102-STD-001-CLAUSE-003D (Default vs Conditional Register Families)**
        - Concept MUST always include, at minimum:
          - Standards index
          - Design register (pointers-only)
          - Research register (per `T102-STD-006`)
          - Workscope register and File register (scope inventory + artifact role mapping)
          - Readiness snapshot and Handoff snapshot (authoritative snapshots)
        - Concept MAY include conditional register families when coordination scale requires them:
          - Issues & Risks aggregation register (pointers-only) when cross-epic I&R coordination is needed or when multiple epics are active
          - Expanded coordination inventories (dependencies, interfaces, integration surfaces) when cross-scope drift risk is observed or when multiple teams/epics rely on shared obligations
          - Overview assets (diagrams/dashboards) when executive scanability degrades due to index growth

    4) **T102-STD-001-CLAUSE-004 (DESIGN Implementation)** 
      - Story-level design logs with final proposed solution, integration notes, dependencies, decision records
      - ADR variance documentation when deviating from upstream Concept framework decisions
      - Explicit traceability references to governing GDR/ADR hierarchy for change impact analysis
      - Ripple test documentation for cross-story coupling validation

## Decision Record

* **T102-STD-001-ADR-001 (Consultancy Operating Model)** {#t102-std-001-consultancy-model}

  * **Context**
    Per `T102-GDR-001`, define the consultancy model using Double Diamond, aligned with ISO/IEC/IEEE 42010, IEEE 1016, ISO 29148, and BABOK v3. Current flow lacks traceability and role separation.

  * **Decision**
    Adopt a four‑stage workflow with clear handoffs and approvals:

        1) **SPS (Project Initiation Document)**
          - **Why**: Establish governance early; avoid scope creep/inversion
          - **What**: Initiative/epic governance with GDR Index; no solutions/technical ADRs
          - **Benefit**: Client retains strategic control

        2) **Request (Business/System Requirements)**
          - **Why**: Turn approved problems into testable requirements without solutions
          - **What**: Feature BRD/SRS with story AC; inherits SPS governance; no decision records
          - **Benefit**: Stable baseline for solution exploration

        3) **Concept (Architecture Description)**
          - **Why**: Compare options and secure approval before implementation
          - **What**: Initiative bridge/process manual; ADR compendium; audit-surface registers (pointers-only); readiness/handoff snapshots
          - **Benefit**: Evidence‑based selection with traceability

        4) **Design (Story Implementation Logs)**
          - **Why**: Capture story‑level implementation decisions with upstream traceability
          - **What**: Final solutions, integration notes, dependencies; ADR variances if deviating
          - **Benefit**: Detailed guidance with preserved audit trail

  * **Alternatives Considered**
    (a) All decisions in SPS — rejected (breaks governance vs. architecture separation; raises churn). 
        (b) Request as SAD‑lite — rejected (reintroduces inversion; duplicates Concept; conflicts with 29148 SRS role). 
        (c) Split Concept by scope (I/E/F) — deferred (more files; client prefers single compendium).

  * **Consequences**
    (+) Standardized workflow; less rework; predictable delivery
        (+) End‑to‑end traceability from problem to implementation
        (+) Industry‑aligned method improves conF-SIDence and adoption
        (-) Initial training needed for template adoption
        (±) Structure may slow early authoring but raises quality

## References

`T102-GDR-001 (Consultancy Operating Model Standard)`, 
  `T102-NOTE-003 (Industry Standards)`,
  `T102C-STD-001 (Concept Architectural Framework)`,
  `T102-STD-005 (ID Specification & Rules)`,
  `T102-STD-006 (Research Artifacts Index)`

## Provenance

`sps_T102-CONSULTANT.md`
