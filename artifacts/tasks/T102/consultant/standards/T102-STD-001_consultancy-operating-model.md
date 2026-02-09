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
      - Architecture Description Document (ADD) serving as ADR compendium across initiative/epic/feature levels
      - Uniform ADR format: `Context→Decision→Specification→Consequences→Alternatives Considered→References` with repo-relative links
      - Design Log Register maintaining links-only to story-level implementation details
      - Initiative/Epic/Feature ADR indices with governance traceability to parent GDRs

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
          - **What**: ADR compendium; criteria/matrices; C4 views; Design Log Register
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
  `T102-NOTE-003 (Industry Standards)`

## Provenance

`sps_T102-CONSULTANT.md`
