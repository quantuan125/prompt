# T102B-STD-003 — Story FR Deferral Standard

## Specification

1) **T102B-STD-003-CLAUSE-001 (Story Index Structure)**
   - Request artifacts MAY include a Story Index for multi-story features.
   - Story Index SHALL contain: Story ID, Title, Purpose summary (1-2 sentences), Design Link (populated post-handoff).
   - Story Index SHALL NOT contain: Detailed FR bodies, acceptance criteria, implementation details.

2) **T102B-STD-003-CLAUSE-002 (Deferral Boundary)**
   - Story-level FRs (testable behavior per story) SHALL be deferred to Design phase.
   - Story-level acceptance criteria (Gherkin AC) SHALL be deferred to Design phase.
   - Feature-level scope (Story Index with purpose summaries) SHALL remain in Request.

3) **T102B-STD-003-CLAUSE-003 (Exceptions)**
   - Single-story features MAY include story-level FR in Request if complexity warrants Full Request workflow.
   - Exception requires explicit justification in Request Section Notes.

## Decision Record

* **T102B-STD-003-ADR-001 (Story FR Deferral Standard)** {#t102b-std-003-adr-001}

  * **Context**
    Per `T102B-STD-002 (Workflow Typology Standard)`, story-level specification at Request stage is identified as an industry anti-pattern per SAFe guidance and `T102B-RES-001` W2 findings. Request artifacts need story navigation without detailed FR bodies.

  * **Decision**
    Define Story Index as the mechanism for story navigation in Request; defer detailed story-level FR bodies and acceptance criteria to `T102D (DESIGN)` workflows.

  * **Alternatives Considered**
    - (a) Full story-level FRs at Request stage — rejected; SAFe anti-pattern per `T102B-RES-001` W2; creates documentation trap blocking MVP delivery.
        - (b) No story reference at all in Request — rejected; loses navigation structure for multi-story features; authors need story-level orientation.

  * **Consequences**
    (+) Reduces documentation trap risk per `T102B-RISK-003`.
        (+) Aligns with SAFe Iteration Planning best practices.
        (+) Enables MVP delivery without blocking on story details.
        (±) Requires clear handoff protocol to Design phase.
        (-) Some stakeholders may expect story details in Request.

## References

`T102B-STD-002 (Workflow Typology Standard)`, `T102B-CON-002 (No Story FR Mandate)`, `T102B-IG-003 (Story Index Deferral)`, `T102B-RISK-003 (Documentation Trap)`

## Provenance

- `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md`
