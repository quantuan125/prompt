# T102-STD-007 — Issues & Risks Index

## Specification

1) **T102-STD-007-CLAUSE-001 (Section Naming & Placement)**
      - MUST be available for each scope and use the exact heading `Issues & Risks` across all artifacts.

    2) **T102-STD-007-CLAUSE-002 (Issues Guidance & Enum)**
      - Issue `Status` values MUST be uppercase and backticked exactly as listed: OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED
      - Issue `Priority` values MUST be title case and backticked exactly as listed: HIGH, MEDIUM, LOW

    3) **T102-STD-007-CLAUSE-003 (Issues Table Schema)**
      - Issues table MUST use this exact column schema:
        `| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes |Resolution Date |`
      - `Proposed Date` and `Resolution Date` MUST be ISO-8601 (`YYYY-MM-DD`) or `—` if unknown/not applicable.
      - `Resolution Notes` MUST follow these coupling rules:
        - If `Status = OPEN`: `Resolution Notes = —` and `Resolution Date = —`.
        - If `Status = IN-REVIEW`: `Resolution Notes` MAY be populated (planned resolution); `Resolution Date = —`.
        - If `Status ∈ {RESOLVED, BLOCKED, DEFERRED}`: `Resolution Notes` MUST be populated and `Resolution Date` MUST be an ISO-8601 date (not `—`).

    4) **T102-STD-007-CLAUSE-004 (Risks Guidance & Enum)**
      - Risk `Status` values MUST be uppercase and backticked exactly as listed: OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED
      - Risk `Priority` values MUST be title case and backticked exactly as listed: HIGH, MEDIUM, LOW.

    5) **T102-STD-007-CLAUSE-005 (Risks Table Schema)**
      - Risks table MUST use this exact column schema:
        `| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes |Mitigation Date |`
      - `Proposed Date` and `Mitigation Date` MUST be ISO-8601 (`YYYY-MM-DD`) or `—` if unknown/not applicable.
      - `Mitigation Notes` MUST follow these coupling rules:
        - If `Status = OPEN`: `Mitigation Notes = —` and `Mitigation Date = —`.
        - If `Status = MONITORED`: `Mitigation Notes` MAY be populated (planned mitigation / trigger conditions); `Mitigation Date = —`.
        - If `Status ∈ {MITIGATED, ACCEPTED, CLOSED}`: `Mitigation Notes` MUST be populated and `Mitigation Date` MUST be an ISO-8601 date (not `—`).

    6) **T102-STD-007-CLAUSE-006 (ID Rules)**
      - IDs MUST follow `T102-STD-005 (ID Specification & Rules)` category tokens: `ISSUE` and `RISK`.
      - IDs MUST be scoped and sequential using three digits: `<SCOPE_ID>-ISSUE-###` and `<SCOPE_ID>-RISK-###` (e.g., `T102-ISSUE-005`, `T102A-RISK-003`).
      - IDs MUST remain stable once created (no reuse, no renumbering).

    7) **T102-STD-007-CLAUSE-007 (Resolution Notes Requirement)**
      - Resolution notes MUST be captured in the `Resolution Notes` column (not as a separate post-table block).
      - For Issues with `Status = IN-REVIEW`, `Resolution Notes` MAY contain a planned/proposed resolution.
      - For Issues with `Status ∈ {RESOLVED, BLOCKED, DEFERRED}`, `Resolution Notes` MUST include a resolution summary and MUST include back-ticked IDs for governing E-RIDs/E-DRs (and GDR/ADR/RES/NOTE where applicable).
      - Resolution notes MUST be written to support auditability and traceability (avoid vague statements like “fixed” without citing controlling IDs or evidence).

    8) **T102-STD-007-CLAUSE-008 (Mitigation Notes Requirement)**
      - Mitigation notes MUST be captured in the `Mitigation Notes` column (not as a separate post-table block).
      - For Risks with `Status = MONITORED`, `Mitigation Notes` MAY contain a planned/proposed mitigation.
      - For Risks with `Status ∈ {MITIGATED, ACCEPTED, CLOSED}`, `Mitigation Notes` MUST include a mitigation/acceptance summary and MUST include back-ticked IDs for governing E-RIDs/E-DRs (and GDR/ADR/RES/NOTE where applicable).
      - Mitigation notes SHOULD remain concise and “link-don’t-duplicate”.

    9) **T102-STD-007-CLAUSE-009 (Cross-Scope Promotion & De-duplication)**
      - If an Epic issue/risk becomes Initiative-impacting, authors SHOULD create a corresponding Initiative item (e.g., `T102-ISSUE-###`) and:
        - keep the Epic item scoped to the Epic, OR
        - close the Epic item with a Resolution Note that references the promoted Initiative item by back-ticked ID.
      - Avoid duplicating full narratives across scopes; prefer ID references and delta-only updates per `T102-STD-003 (Explicit Inheritance Model)`.

## Decision Record

* **T102-STD-007-ADR-001 (Issues & Risks Index)** {#t102-std-007-issues-risks-index}

  * **Context**
    Per `T102-QG-001` and `T102-QG-002`, open issues and risks must remain scannable and traceable across SSOT artifacts. The current SPS/Request ecosystem contains inconsistent “Issues & Risks” implementations (varying table schemas, status enums/casing, and missing resolution/mitigation notes), creating governance drift and blocking reliable cross-scope rollups and future validation/automation.

  * **Decision**
    Standardize the “Issues & Risks” structure across SSOT artifacts (SPS and Request at minimum) using the full SPS schema as the canonical exemplar, including required guidance comment blocks and required resolution/mitigation notes.

  * **Alternatives Considered**
    (a) Allow each artifact to define its own Issues/Risks schema — rejected: creates drift and blocks cross-scope review.
        (b) Minimal “ID | Description | Owner | Status” tables everywhere — rejected: loses priority/date fields and reduces governance usefulness for complex initiatives.

  * **Consequences**
    (+) Consistent, executive-readable issues/risk logs across SPS and Request artifacts.
        (+) Higher-quality traceability and auditability via mandatory resolution/mitigation notes.
        (+) Easier future validation/automation due to deterministic schemas and enums.
        (±) Slightly higher authoring overhead due to required notes on closure/mitigation.
        (-) Requires migration effort to align legacy sections to the standard.

## References

`T102-STD-003 (Explicit Inheritance Model)`,
  `T102-STD-005 (ID Specification & Rules)`,
  `T102-CON-001 (Format Requirements)`,
  `T102-IG-001 (Comment Blocks)`,
  `T102-IG-006 (Markdown Heading Terminology)`,
  `T102-QG-001 (Client Readability)`,
  `T102-QG-002 (End-to-End Traceability)`

## Provenance

`sps_T102-CONSULTANT_v1.1.0.md` (Section III.B.9; Epic dossier “Epic Issues & Risks” exemplar)
