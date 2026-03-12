---
artifact_type: 'PROPOSAL'
initiative_id: 'T102'
phase: '0'
date: '2026-01-24'
version: '0.2.0'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# PROPOSAL: Refactor T102 GDRs into STDs (STD Baseline + Migration Workspace)

## I. PURPOSE

Initialize a dedicated proposal workspace to:
- introduce the **`STD`** artifact family baseline (normative standards), and
- define the migration framing for refactoring legacy `GDR` standards into `STD` standards,
without yet performing the downstream refactors (handled in later streams/activities).

This file is intentionally initialized as a **skeleton** (headings + schema + placeholders) for Stream 3 work and then extended with Stream 4A/4B deliverables.

## II. CONTEXT MATERIALS & INPUTS (REPO-RELATIVE; NOT MODIFIED HERE)

- Roadmap (Phase 0): `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/plan_T102-PH000.md`
- Exemplar proposal (ADR-004/ADR-005): `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor-adr-004-005.md`
- Concept SSOT (baseline ADR/GDR patterns): `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
- SPS SSOT (baseline GDR index patterns): `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`

## III. SCOPE

### A. In scope (Stream 3)
- Establish the baseline **STD Index Schema** (table) above bodies.
- Create placeholders for `T102-STD-009` (STD governance baseline) and `T102-STD-009` (paired normative spec for `STD`).
- Capture any required **Parallelism & Dependencies** notes relevant to the STD migration workflow.

### B. Out of scope (Streams 5+)
- Migrating remaining legacy `GDR` artifacts into `STD` artifacts beyond `T102-STD-004` and `T102-STD-005`.
- Applying approved outputs across SPS/Concept SSOTs (handled in Stream 5).

## IV. PARALLELISM & DEPENDENCIES (PHASE 0)

- Stream 3 depends on Stream 2 completing baseline stabilization of ADR-004/ADR-005 proposal content.
- Streams 4A (STD-004 track) and 4B (STD-005 track) depend on Stream 3 establishing the `STD` baseline pattern (`STD-009` + `ADR-009`).
- Stream 5 applies approved outputs across SPS + Concept SSOTs after Stream 3/4 deliverables exist.

## V. STD INDEX SCHEMA (BASELINE)

**STD Index Schema**

`STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference`

## VI. DRAFT SPECIFICATIONS (STREAM 3)

### A. T102-STD

**Migration Mapping (Legacy `T102-GDR-*` → Replacement `T102-STD-*`)**

Strict one-to-one mapping: `T102-GDR-00x` → `T102-STD-00x`.

| Legacy GDR | Replacement STD | Adopts | Notes |
|:-----------|:----------------|:-------|:------|
| `T102-GDR-001` | `T102-STD-001` | `T102-STD-001 (Consultancy Operating Model)` | — |
| `T102-GDR-002` | `T102-STD-002` | `T102-STD-002 (Canonical YAML Header)` | — |
| `T102-GDR-003` | `T102-STD-003` | `T102-STD-003 (Explicit Inheritance Model)` | — |
| `T102-GDR-004` | `T102-STD-004` | `T102-STD-004 (Decision Records Index)` | — |
| `T102-GDR-005` | `T102-STD-005` | `T102-STD-005 (ID Specification & Rules)` | — |
| `T102-GDR-006` | `T102-STD-006` | `T102-STD-006 (Research Artifacts Index)` | — |
| `T102-GDR-007` | `T102-STD-007` | — | `Adopts` intentionally deferred during migration (placeholder permitted; see Stream 5 Activity 5.0.3). |
| `T102-GDR-008` | `T102-STD-008` | `T102-STD-008 (Organisation Baseline Standard)` | — |

| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |
|:-------|:----------|:-------|:------|:----------|:-----------|:-------------------------|:------------|:----------|
| `T102-STD-001` | **Operating Model Standard** | `Proposed` | Client | — | `T102-GDR-001` | `T102-STD-001 (Consultancy Operating Model)` | CI/Lint + Review MUST verify: workflow sequencing, authority/ownership rules, and approval gates align to the adopted spec. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-002` | **Canonical Header Standard** | `Proposed` | Client | — | `T102-GDR-002` | `T102-STD-002 (Canonical YAML Header)` | CI/Lint + Review MUST verify: artifact YAML headers conform to the adopted schema across SPS/Request/Concept/Design. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-003` | **Inheritance Model Standard** | `Proposed` | Client | — | `T102-GDR-003` | `T102-STD-003 (Explicit Inheritance Model)` | CI/Lint + Review MUST verify: explicit inheritance tables/ID references and variance handling conform to the adopted spec. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-004` | **Specification Standard & Guideline** | `Proposed` | Client | — | `T102-GDR-004` | `T102-STD-004 (Decision Records Index)` | CI/Lint + Review MUST verify: correct index schemas, required body subheadings, and valid authority citations per adopted spec. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-005` | **ID Governance Standard** | `Proposed` | Client | — | `T102-GDR-005` | `T102-STD-005 (ID Specification & Rules)` | CI/Lint + Review MUST verify: valid IDs/tokens per adopted spec, correct formal vs. shorthand reference usage, and RFC2119 keyword constraints via `T102-CON-009`. | `T102-STD-009 (Governance Standards Model)`, `T102-CON-009 (Normative Keywords)` |
| `T102-STD-006` | **Research Workflow Standard** | `Proposed` | Client | — | `T102-GDR-006` | `T102-STD-006 (Research Artifacts Index)` | CI/Lint + Review MUST verify: brief/report gating, indexing/traceability rules, and integration placement conform to the adopted spec. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-007` | **LLM Quality Control** | `Proposed` | Client | — | `T102-GDR-007` | — | CI/Lint + Review MUST verify: source verification, human-in-the-loop review, traceability/logging, and disclosure safeguards are present per the standard (adopted spec intentionally deferred during migration). | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-008` | **Organisation Baseline Standard** | `Proposed` | Client | — | `T102-GDR-008` | `T102-STD-008 (Organisation Baseline Standard)` | CI/Lint + Review MUST verify: a single initiative-level organisation baseline exists with stable actor-to-role mapping and governance ownership. | `T102-STD-009 (Governance Standards Model)` |
| `T102-STD-009` | **Governance Standards Model** | `Proposed` | Client | — | — | `T102-STD-009 (Governance Standards Specification)` | CI/Lint + Review MUST verify: required STD fields, valid `Adopts`, and RFC2119 keyword constraint via `T102-CON-009`. | `T102-STD-005 (ID Governance Standard)`, `T102-CON-009 (Normative Keywords)` |


* **T102-STD-001 (Operating Model Standard)** — The project SHALL follow the consultancy operating model, approval gates, and decision precedence defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) SPS is governance-only and establishes initiative/epic governance boundaries (`T102-STD-001-CLAUSE-001`).
    2) Request is requirements-only and MUST NOT embed decision records (`T102-STD-001-CLAUSE-002`).
    3) Concept is the architecture decision workspace/ADR compendium (`T102-STD-001-CLAUSE-003`).
    4) Design captures story-level decisions and records variances when deviating (`T102-STD-001-CLAUSE-004`).

* **T102-STD-002 (Canonical Header Standard)** — All artifacts SHALL include a canonical YAML header that conforms to the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Use only the canonical header key set (and required scope keys when applicable) (`T102-STD-002-CLAUSE-001`).
    2) Enforce canonical formats/enums for header values (e.g., IDs, status, dates, versions) (`T102-STD-002-CLAUSE-002`).
    3) Provide canonical schema examples/reference as required (`T102-STD-002-CLAUSE-003`).

* **T102-STD-003 (Inheritance Model Standard)** — Downstream artifacts SHALL implement explicit inheritance by ID referencing and variance handling as defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Include the Inherited Considerations table using the required schema/columns (`T102-STD-003-CLAUSE-001`).
    2) Follow precedence and document deviations as local variance ADRs (`T102-STD-003-CLAUSE-002`).
    3) Apply delta-only authoring rules (do not restate upstream text; emphasize ≤5 critical inherited IDs) (`T102-STD-003-CLAUSE-003`).

* **T102-STD-004 (Specification Standard & Guideline)** — The project SHALL use the unified decision record index schemas, body templates, and linking rules defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Use the standardized DR index schemas (GDR/ADR) and column definitions (`T102-STD-004-CLAUSE-001`).
    2) Follow placement standards for DR indices across artifact families (`T102-STD-004-CLAUSE-002`).
    3) Create/update DR entries using the defined workflow and body template (`T102-STD-004-CLAUSE-003`, `T102-STD-004-CLAUSE-004`).
    4) Maintain stable anchors per the anchor stability rules (`T102-STD-004-CLAUSE-007`).

* **T102-STD-005 (ID Governance Standard)** — The project SHALL use the canonical ID schema, token taxonomy, and reference semantics defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) IDs MUST conform to the canonical schema and formatting rules (`T102-STD-005-CLAUSE-001`).
    2) Tokens, taxonomy, and allowed scope usage MUST follow the canonical table (`T102-STD-005-CLAUSE-002`).
    3) Precedence, inheritance directionality, and variance requirements MUST be followed (`T102-STD-005-CLAUSE-003`).
    4) Formal vs shorthand reference usage MUST follow the reference semantics rules (`T102-STD-005-CLAUSE-004`).

* **T102-STD-006 (Research Workflow Standard)** — Formal research artifacts SHALL be indexed and referenced using the Research Artifacts Index architecture defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Use the `RES-###` ID pattern integration rules (`T102-STD-006-CLAUSE-001`).
    2) Maintain the required research table schemas (local + Concept aggregation) (`T102-STD-006-CLAUSE-002`).
    3) Apply placement decision criteria for inline vs indexed vs external research (`T102-STD-006-CLAUSE-003`).
    4) Follow the index maintenance protocol (`T102-STD-006-CLAUSE-004`).
    5) Reference research findings by `RES-###` IDs (link-don’t-duplicate) (`T102-STD-006-CLAUSE-005`).

* **T102-STD-007 (LLM Quality Control)** — Any LLM-generated factual claims integrated into governance artifacts SHALL be validated using mandatory quality control safeguards (adopted canonical spec intentionally deferred during migration).
  - **Minimum Viable Conformance**:
    1) Verify factual claims against authoritative sources; unverified claims are excluded or clearly labeled as conjecture.
    2) Require human-in-the-loop review prior to governance integration, with an accountable named owner.
    3) Maintain traceability/logging for LLM usage (inputs, outputs, and methodology metadata) sufficient for auditability.
    4) Disclose LLM usage and enforce a rule that no governance obligation is accepted on LLM-only evidence without validation.
    5) Define escalation triggers for high-risk domains (e.g., legal/regulatory) requiring appropriate human expertise.

* **T102-STD-008 (Organisation Baseline Standard)** — The project SHALL maintain a single initiative-level organisation baseline with stable actor-to-role mapping and governance RACI as defined in the adopted normative specification.
  - **Minimum Viable Conformance**:
    1) Maintain canonical placement of the organisation baseline in the initiative SPS (`T102-STD-008-CLAUSE-001`).
    2) Include the required Role Definitions table and Governance RACI using the mandated schemas (`T102-STD-008-CLAUSE-002`).
    3) Follow the maintenance policy to avoid drift and unnecessary churn (`T102-STD-008-CLAUSE-003`).

* **T102-STD-009 (Governance Standards Model)** — The project SHALL use `STD` as the authoritative registry token for enforceable standards, replacing `GDR`. Each `STD` item MUST: 
  (a) state a concise obligation and 
  (b) declare exactly one adopted canonical normative specification that contains the detailed rules. Rationale, trade-offs, and alternatives MUST be captured in `ADR` records, not inside `STD` bodies. 
  - **Minimum Viable Conformance**:
    1) `STD` semantics and scope MUST follow the defined token rules (`T102-STD-009-CLAUSE-001`).
    2) `STD` adoption contract MUST be enforced (single canonical adopted spec) (`T102-STD-009-CLAUSE-002`).
    3) `STD` precedence and variance requirements MUST be applied (`T102-STD-009-CLAUSE-003`).
    4) `STD` index schema and authoring guidelines MUST be followed (`T102-STD-009-CLAUSE-004`).
    5) Migration tolerance MUST be applied as specified (`T102-STD-009-CLAUSE-005`).

### B. T102-ADR

| ADR ID | Title | Authority STD | Status | Effective | Supersedes | Anchor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T102-STD-009` | **Governance Standards Specification** | `T102-STD-009 (Governance Standards Model)` | `Proposed` | Client | — | #t102-std-009-governance-standards-spec |

* **T102-STD-009 (Governance Standards Specification) {#t102-std-009-governance-standards-spec}**

  * **Context**

    The current `GDR` + `ADR` pairing encourages duplicated narrative (policy and rationale) and creates drift over time. A dedicated standards registry mechanism is required so normative obligations can be indexed and governed independently from decision rationale. This ADR defines the introduction and semantics of `STD` and is adopted by `T102-STD-009`.

  * **Decision**

    Establish `STD` as a normative Requirement ID (`RID`) token used to register enforceable standards and to decouple “what must be followed” from “why the choice was made”. `STD` items govern downstream artifacts via precedence rules in `T102-STD-005`. Normative keyword interpretation is governed by `T102-CON-009`.

  * **Specification**

    * **T102-STD-009-CLAUSE-001 (Semantics & Scope)**

      - **Category**: `STD` is a normative `RID` token representing an enforceable standard.
      - **Creation Scope**: `STD` MUST only be created at Initiative (`I`), Epic (`E`), and Feature (`F`) scopes.
      - **Reference Scope**: Artifacts at any scope MAY reference `STD`.
      - **Invalid Usage**: `STD` MUST NOT be used for informative guidance (`IG`) or integration notes (`INT`).

    * **T102-STD-009-CLAUSE-002 (Adoption Contract)**

      - **Single Canonical Adopted Spec**: Every `STD` entry MUST declare exactly one `Adopts` reference.
      - **Incorporation by Reference**: The adopted normative specification is incorporated by reference into the `STD`. The `STD` remains the authoritative RID-level handle; the adopted spec is the canonical text.
      - **No Rationale Duplication**: `STD` bodies MUST NOT contain alternatives analysis or lengthy trade-offs. These MUST be captured in ADRs.

    * **T102-STD-009-CLAUSE-003 (Precedence & Variance)**

      - **Precedence**: `STD` is a `RID` and therefore takes precedence over `DRID` items per `T102-STD-005-CLAUSE-003`.
      - **Non-Contradiction Rule**: ADRs and lower-scope artifacts MUST NOT contradict applicable `STD` obligations.
      - **Variance Contract**: Any exception MUST be recorded as a Variance ADR and MUST cite the overridden `STD` ID.

    * **T102-STD-009-CLAUSE-004 (STD Authoring Requirements)**

      - `STD` index schemas MUST follow `T102-STD-009-CLAUSE-004A`.
      - `STD` index column guidelines MUST follow `T102-STD-009-CLAUSE-004B`.
      - `STD` body construction MUST follow `T102-STD-009-CLAUSE-004C`.
      - `STD` body conciseness targets MUST follow `T102-STD-009-CLAUSE-004D`.
      - `STD` drift controls MUST follow `T102-STD-009-CLAUSE-004E`.

      * **T102-STD-009-CLAUSE-004A (STD Index Schema)**

        - **STD Index Requirement**: Each scope MUST maintain a `STD` index table using this schema:
          `| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Reference |`

      * **T102-STD-009-CLAUSE-004B (STD Index Column Guidelines)**

        - `STD ID`: MUST follow `T102-STD-005-CLAUSE-001`.
        - `Title`: MUST be bold and follow `T102-STD-005-CLAUSE-001` title constraints.
        - `Adopts`: MUST contain exactly one full reference to the canonical adopted normative specifcation.
        - `Verification`: MUST describe (a) mechanism (CI/Lint/Review), (b) what is checked, and (c) pass/fail evidence.
        - `Reference`: MUST list governing IDs such as `T102-STD-005` and initiative-wide constraints (e.g., `T102-CON-009`).

      * **T102-STD-009-CLAUSE-004C (STD Body Construction)**

        - **Primary Obligation Sentence (required)**:
          - Format: `* **<SID>-STD-### (<Title>)** — <Normative obligation sentence>`
          - The obligation sentence MUST answer “WHAT must be true” at a stable, scope-wide level.
        - **Minimum Viable Conformance (MVC) (recommended; max 5 items)**:
          - MVC provides the minimum stable “WHAT” checkpoints required to conform, without restating the full adopted specification.
          - MVC items MUST be written as an ordered list (e.g., `1)` ...).
          - MVC items SHOULD cite adopted-spec clause IDs where possible (e.g., `T102-STD-003-CLAUSE-001`).
          - MVC items MUST NOT introduce new obligations beyond the adopted specification; if a mismatch occurs, the adopted specification remains canonical.

      * **T102-STD-009-CLAUSE-004D (STD Conciseness)**

        - STD bodies SHOULD target <200 words when feasible (excluding tables), aligning with `T102-STD-005-CLAUSE-006 (Content Quality)`.
        - Pragmatic migration exception: if `Adopts = —` is explicitly intentional, the STD body MAY extend (target ≤300 words) to remain actionable until a canonical adopted spec is available.

      * **T102-STD-009-CLAUSE-004E (Drift Controls)**

        - STD bodies MUST avoid duplicating detailed rules; the adopted normative specification is the single canonical source of truth.
        - If an adopted specification is updated in a way that changes conformance expectations, the corresponding STD body (including MVC) MUST be updated in the same change set.
        - When `STD` bodies are copied into SSOT artifacts (e.g., `sps`), those SSOT copies MUST be updated in the same change set whenever the authoritative STD body changes.

    * **T102-STD-009-CLAUSE-005 (Migration Tolerance)**

      - **Alias Window**: During migration, legacy `GDR` IDs MAY be treated as aliases of their replacement `STD` IDs for enforcement.
      - **No New GDR**: New `GDR` creation MUST be blocked after the migration cutoff milestone/date.
      - **Sunset**: Alias support MUST be removed after the migration completion milestone/date.

  * **Alternatives Considered**

    - **Keep GDR + ADR pairing** — rejected due to predictable narrative duplication and drift.
    - **Make ADR the only DRID and place all standards in ADR** — rejected because it collapses normative reference and rationale, reintroducing “spec overload”.
    - **Adopt Option B immediately (separate standard docs)** — deferred to reduce migration complexity; planned as the next evolution once `STD` registry stabilizes.

  * **Consequences**

    (+) Establishes a stable standards registry (`STD`) and separates “rules” from “reasons”.
    (+) Reduces duplication by requiring standards to adopt canonical specs rather than restating them.
    (+) Enables stronger lint/CI validation through uniform STD index schema and adoption contract.
    (±) Requires clear author training on where obligations vs rationale belong.
    (-) Introduces additional artifacts (STD + adopted spec + ADR rationale) that must be maintained with disciplined linkage.

  * **References**

    `T102-STD-009 (Governance Standards Model)`,
    `T102-STD-005 (ID Governance Standard)`,
    `T102-CON-009 (Normative Keywords)`

### C. Additional T102-RIDs
#### 1. CON

* **T102-CON-009 (Normative Keywords)** — Normative requirement keywords (MUST/SHALL/SHOULD/MAY) SHALL be interpreted per RFC 2119 and MUST be written in UPPERCASE to carry normative meaning.

## VII. PROVENANCE (REPO-RELATIVE PATHS ONLY)

- `prompt/artifacts/tasks/T102/consultant/workspace/roadmap/plan_T102-PH000.md`
- `prompt/artifacts/tasks/T102/workspace/PH000/proposal/proposal_T102-CWD_refactor-adr-004-005.md`
- `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
- `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
