# T102-STD-007 — Issues & Risks Index

## Specification

1) **T102-STD-007-CLAUSE-001 (Section Naming & Placement)**
  - The exact heading `Issues & Risks` MUST be used when an Issues & Risks section is present.
  - Initiative and Epic scopes MUST include canonical Issues & Risks tables in their SSOT artifact (SPS).
  - Feature scope Issues & Risks sections are removed by default in Request artifacts.
  - Feature scope MAY include an Issues & Risks section only under an explicit exception mechanism (complexity / risk threshold), including any of:
    - The feature introduces cross-scope impact (multi-feature, template/standard compliance, or Epic gate risk)
    - The feature requires significant external integration coordination
    - The feature contains material unknowns requiring active tracking for approval decisions
  - When an Issues & Risks section is present at any scope, it MUST conform to `T102-STD-007-CLAUSE-002` through `T102-STD-007-CLAUSE-011`.
  - Interpretation: “must be available for each scope” means the canonical tables exist in the scope’s SSOT artifact; Concept aggregation views (if present) are pointers-only audit-surface enhancements and MUST NOT replace canonical per-scope tables.

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
    `| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |`
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
  - If a lower-scope item becomes higher-scope impacting, authors MUST promote it:
    - Feature → Epic promotion: If a Feature issue/risk impacts Epic success (multi-feature impact, template/standard compliance, or Epic gates), create an Epic item and close the Feature item with a Resolution/Mitigation Note referencing the promoted Epic item by back-ticked ID.
    - Epic → Initiative promotion: If an Epic issue/risk becomes Initiative-impacting, create a corresponding Initiative item (e.g., `T102-ISSUE-###`) and close or strictly-localize the Epic item with a Resolution/Mitigation Note referencing the promoted Initiative item by back-ticked ID.
  - De-dup enforcement: The highest-scope active item is canonical. Lower-scope duplicates MUST be either (a) closed with a reference to the canonical item, or (b) explicitly scoped as a local delta (not a narrative duplicate).
  - Downward monitoring guidance: When an Initiative-level item requires local monitoring, Epic-level items MAY be created that reference the Initiative item (downstream → upstream referencing is allowed). Upstream scopes MUST NOT reference downstream items, per `T102-STD-003 (Explicit Inheritance Model)` and `T102-STD-005 (ID Specification & Rules)`.
  - This clause does not prohibit pointers-only Concept audit-surface registers from referencing downstream IDs for inventory/audit purposes under the governed exception defined in `T102-STD-005-CLAUSE-003 (Precedence & Hierarchy)`.
  - Avoid duplicating full narratives across scopes; prefer ID references and delta-only updates per `T102-STD-003 (Explicit Inheritance Model)`.

10) **T102-STD-007-CLAUSE-010 (Content Filtering Criteria)**
  - Authors MUST filter candidate items to ensure Issues & Risks logs contain only actual Issues/Risks (not misclassified governance, guidance, or parking-lot content).
  - Decision tree (apply top-down; first match wins):
    1. If the item is an enforceable obligation/standard requirement, it MUST be expressed as `RID` or `STD` (not `ISSUE`/`RISK`).
    2. If the item is an architectural decision (with alternatives/rationale), it MUST be expressed as an `ADR` (not `ISSUE`/`RISK`).
    3. If the item is a scope assumption/constraint/dependency/quality goal, it SHOULD be expressed using the appropriate ID category (`ASSUM`, `CON`, `DEP`, `QG`) rather than `ISSUE`/`RISK`.
    4. If the item is implementation guidance, it SHOULD be expressed as `IG`.
    5. If the item is integration coordination guidance and is non-normative, it SHOULD be expressed as `INT`.
    6. If the item is non-normative parking-lot context, it SHOULD be expressed as a `NOTE`.
  - Feature-scope filtering gate: A Feature Request MUST NOT pass its approval gate while carrying misclassified Feature-scope `ISSUE`/`RISK` items; items failing the filtering criteria MUST be reclassified or promoted before approval.
  - Tracking governance gaps: Items that represent a known governance gap MAY be tracked as an `ISSUE` temporarily, but MUST be closed with a Resolution Note that references the produced authoritative artifact (`STD`/`ADR`/`RID`) when that artifact exists.
  - Worked examples:
    - `T102-ISSUE-001 (Planner Handoff Schema)`: Track as Issue until the governing interface/standard exists; then close and reference the governing artifact.
    - `T102-ISSUE-004 (IDs Promotion Protocol)`: Governance gap that should ultimately be a `STD`/`ADR`, not a long-lived Issue.
    - `T102B1-ISSUE-002 (Classification markers)`: Feature-level Issue that should be promoted to Epic scope if it impacts Epic governance (`T102B-ISSUE-###`).

11) **T102-STD-007-CLAUSE-011 (Staleness Detection Policy)**
  - OPEN (Issues) and MONITORED (Risks) items older than 90 days without a review touch MUST trigger a staleness review.
  - Staleness age is measured from `Proposed Date` unless a more recent review touch is recorded in the Notes column as a dated entry (e.g., `Reviewed 2026-02-11: <short note>`).
  - A staleness review touch MUST result in one of:
    - Status update (including closure states where appropriate)
    - Refresh of Resolution/Mitigation Notes (including trigger conditions for MONITORED risks)
    - Explicit DEFERRED/ACCEPTED with rationale and governing back-ticked IDs in notes
  - Staleness review cadence SHOULD align with the initiative’s regular review cycles.

## Decision Record

* **T102-STD-007-ADR-001 (Issues & Risks Index)** {#t102-std-007-issues-risks-index}

  * **Context**
    Per `T102-QG-001` and `T102-QG-002`, open issues and risks must remain scannable and traceable across SSOT artifacts. The current SPS/Request ecosystem contains inconsistent “Issues & Risks” implementations (varying table schemas, status enums/casing, and missing resolution/mitigation notes), creating governance drift and blocking reliable cross-scope rollups and future validation/automation.

  * **Decision**
    Standardize the “Issues & Risks” structure across SSOT artifacts using deterministic schemas and lifecycle coupling rules, while adopting a scoped hosting default: canonical Issues & Risks tables are mandatory at Initiative/Epic scope (SPS) and removed-by-default at Feature scope (Request), with an explicit exception mechanism for complex/high-risk features.

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

`sps_T102-CONSULTANT.md` 
