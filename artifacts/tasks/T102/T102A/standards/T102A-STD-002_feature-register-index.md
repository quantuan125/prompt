# T102A-STD-002 — Feature Register Index

## Specification

1) **T102A-STD-002-CLAUSE-001 (Canonical Placement & Title)**
       - Each Epic dossier SHALL include a subsection titled exactly: `##### v. Feature Register`.
       - The subsection SHALL appear after `Governance & Roadmap` and before `Epic Requirements`.

    2) **T102A-STD-002-CLAUSE-002 (Table Contract)**
       The Feature Register table SHALL use this exact schema:
       - `ID | Code | Title | Description | Feature Lead (R) | Status | Canonical Link (Request)`
       Fill rules:
       - `ID`: the Feature scope identifier (e.g., `T801A1`).
       - `Code`: short feature code (e.g., `BACKEND`, `PROMPT`).
       - `Title`: human-readable feature name with **bold heading**.
       - `Description`: one sentence; scope-level, not design-level.
       - `Feature Lead (R)`: the responsible coordination role for the Feature (typically `LLM_Consultant`).
       - `Status`: one of the allowed status values (see `T102A-STD-002-CLAUSE-003`).
       - `Canonical Link (Request)`: repo-relative link to the Feature Request artifact once created; SHALL be `—` prior to request creation.

    3) **T102A-STD-002-CLAUSE-003 (Allowed Status Values; Minimal Set)**
       Feature Register status SHALL be one of:
       - `proposed`, `in-request`, `approved`, `in-build`, `done`, `deferred`, `dropped`

    4) **T102A-STD-002-CLAUSE-004 (Status Transition Rules)**
       - `proposed → in-request`: when a Request artifact is created (draft).
       - `in-request → approved`: when the Decision Owner approves the Request.
       - `approved → in-build`: when implementation begins.
       - `in-build → done`: when acceptance evidence exists and is recorded.
       - `* → deferred`: Decision Owner explicitly defers.
       - `* → dropped`: Decision Owner explicitly removes from scope.

    5) **T102A-STD-002-CLAUSE-005 (Change Control & Stability)**
       - Adding/removing a Feature row is a governance baseline change and MUST be traceable (proposal/completion reference).
       - Feature Register SHALL remain an index only; detailed requirements/design belong in Feature Request artifacts.

## Decision Record

* **T102A-STD-002-ADR-001 (Feature Register Index)** {#t102a-std-002-feature-register-index}

  * **Context**
    Per `T102A-GDR-001 (Governance Snapshot Standard)`, each Epic dossier must be governance-readable while preserving traceability into living artifacts. Feature scope lists were previously embedded inside Governance & Roadmap, causing churn and mixing governance with scope inventory.

  * **Decision**
    Adopt `T102A-STD-002` as the mandatory standard for Epic Feature Register placement, schema, and maintenance policy.

  * **Alternatives Considered**
    (a) Keep Feature Register inside Governance & Roadmap — rejected (increases churn; mixes scope inventory with governance snapshot).
      (b) Move Feature Register to Concept only — rejected (reduces visibility in the SSOT epic dossier).

  * **Consequences**
    (+) Keeps Governance & Roadmap stable while preserving scope visibility
      (+) Enforces traceability: each feature has a canonical Request link
      (±) Requires discipline to treat register changes as baseline events

## References

`T102A-GDR-001 (Governance Snapshot Standard)`,
  `T102-STD-004 (Specification Standard & Guideline)`,
  `T102-STD-005 (ID Specification & Rules)`,
  `T102-RES-002 (Roadmap Viability)`

## Provenance

None


##### ii. `T102B` Epic: `REQUEST` — Request Workflow

| ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
|:-------|:------|:--------------|:-------|:------|:----------|:-----------|:---------------|
| `T102B-STD-001` | **Request Architecture Standard** | `T102B-STD-001 (Request Governance Snapshot Standard)` | Proposed | LLM_Consultant | — | — | [T102B-STD-001](../../standards/T102B-STD-001_request-architecture-standard.md) |
| `T102B-STD-002` | **Section Classification Standard** | `T102B-STD-004 (Section Classification Policy)` | Proposed | LLM_Consultant | — | — | [T102B-STD-002](../../standards/T102B-STD-002_section-classification-standard.md) |
| `T102B-STD-003` | **Story FR Deferral Standard** | `T102B-STD-002 (Workflow Typology Standard)` | Proposed | LLM_Consultant | — | — | [T102B-STD-003](../../standards/T102B-STD-003_story-fr-deferral-standard.md) |
| `T102B-STD-004` | **Request Lite Specification** | `T102B-STD-002 (Workflow Typology Standard)` | Proposed | LLM_Consultant | — | — | [T102B-STD-004](../../standards/T102B-STD-004_request-lite-specification.md) |

##### iii. `T102C` Epic: `CONCEPT` — Concept Workflow

| ADR ID | Title | Authority STD | Status | Owner | Effective | Supersedes | Canonical Path |
|:-------|:------|:--------------|:-------|:------|:----------|:-----------|:---------------|
| `T102C-STD-001` | Concept Architectural Framework | `T102C-GDR-001` | Proposed | — | 2025-09-28 | — | #t102c-std-001-concept-framework |
