# P-STD-003 — Program Governance Standards & Decision Records Model

## Specification

1) **P-STD-003-CLAUSE-001 (Index Schemas)**

   - Program standards MUST maintain a `STD` index schema per `T102-ADR-009-CLAUSE-004A`.
   - Program decision records MUST maintain ADR index schema and column definitions per `T102-ADR-004-CLAUSE-001`.

2) **P-STD-003-CLAUSE-002 (Placement Standards)**

   - SPS and Concept placement rules for DR indexes MUST follow `T102-ADR-004-CLAUSE-002`.
   - Canonical paths in index rows MUST resolve to combined standard/decision files stored under program standards directories.

3) **P-STD-003-CLAUSE-003 (Adoption Contract)**

   - Every Program `STD` entry MUST declare exactly one adopted normative specification per `T102-ADR-009-CLAUSE-002`.
   - Adopted specifications are incorporated by reference; `STD` bodies MUST remain concise and avoid duplicating full specs.

4) **P-STD-003-CLAUSE-004 (STD Authoring Requirements)**

   - STD body construction, MVC conciseness, and drift controls MUST follow `T102-ADR-009-CLAUSE-004C` through `T102-ADR-009-CLAUSE-004E`.
   - STD index column guidance (including `Governed By` and `Reference` constraints) MUST follow `T102-ADR-009-CLAUSE-004B`.

5) **P-STD-003-CLAUSE-005 (Decision Record Body + Specification Clauses)**

   - Decision record body structure MUST follow `T102-ADR-004-CLAUSE-004`.
   - Specification clause formatting MUST follow `T102-ADR-004-CLAUSE-005`.

6) **P-STD-003-CLAUSE-006 (Precedence, Variance, Lifecycle)**

   - Precedence and variance requirements MUST follow `T102-ADR-004-CLAUSE-010` and `T102-ADR-009-CLAUSE-003`.
   - Lifecycle coherence and status management MUST follow `T102-ADR-004-CLAUSE-008` and `T102-ADR-004-CLAUSE-009`.

7) **P-STD-003-CLAUSE-007 (Migration Tolerance)**

   - Any migration tolerance or alias window for legacy governance IDs MUST follow `T102-ADR-009-CLAUSE-005`.

## Decision Record

* **P-STD-003 (Program Governance Standards & Decision Records Model)** {#p-std-003-governance-standards-and-dr-index}

  * **Context**

    Per `T102-STD-004 (Decision Records Standard)`, consistent decision record schemas and linking patterns are required to prevent governance drift across artifacts. Program standards must unify the Decision Records Index (`T102-ADR-004`) with the Governance Standards Specification (`T102-ADR-009`) so initiatives can adopt a single, stable governance model without duplicating rule bodies.

  * **Decision**

    Adopt a program-level combined governance model that:
    1) Uses the Decision Records Index requirements from `T102-ADR-004`, and
    2) Uses the Standards authoring, adoption, and drift controls from `T102-ADR-009`.

    This combined model is captured as `P-STD-003` and serves as the governing standard for program-level standards and decision record authoring across `prompt/artifacts/tasks/**`.

  * **Alternatives Considered**

    (a) Keep ADR-004 and ADR-009 as separate, initiative-only references — rejected (program adoption would remain inconsistent).

  * **Consequences**

    (+) Establishes a single governance contract for standards + decision records at program scope.
    (+) Reduces drift by enforcing unified schemas and adoption rules.
    (±) Requires initial mapping of program standards to adopted specifications.
    (-) Requires ongoing maintenance when ADR-004 or ADR-009 are revised.

  * **References**

    `T102-ADR-004 (Decision Records Index)`,
    `T102-ADR-009 (Governance Standards Specification)`,
    `T102-STD-004 (Decision Records Standard)`,
    `T102-STD-009 (Governance Standards Model)`,
    `T102-ADR-005 (ID Specification & Rules)`

  * **Provenance**

    - `prompt/artifacts/tasks/T102/consultant/standards/T102-ADR-004_decision-records-index.md`
    - `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md#t102-adr-009-governance-standards-spec`
