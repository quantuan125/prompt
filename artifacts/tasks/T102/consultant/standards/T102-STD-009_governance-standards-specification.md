# T102-STD-009 — Governance Standards Specification

## Specification

1) **T102-STD-009-CLAUSE-001 (Semantics & Scope)**

   - **Category**: `STD` is a normative `RID` token representing an enforceable standard.
   - **Creation Scope**: `STD` MUST only be created at Program (`P`), Initiative (`I`), Epic (`E`), and Feature (`F`) scopes.
   - **Reference Scope**: Artifacts at any scope MAY reference `STD`.
   - **Invalid Usage**: `STD` MUST NOT be used for informative guidance (`IG`) or integration notes (`INT`).

2) **T102-STD-009-CLAUSE-002 (Adoption Contract)**

   - **Single Canonical Adopted Spec**: Every `STD` entry MUST declare exactly one `Adopts` reference.
   - **Incorporation by Reference**: The adopted normative specification is incorporated by reference into the `STD`. The `STD` remains the authoritative RID-level handle; the adopted spec is the canonical text.
   - **No Rationale Duplication**: `STD` bodies MUST NOT contain alternatives analysis or lengthy trade-offs. These MUST be captured in ADRs.

3) **T102-STD-009-CLAUSE-003 (Precedence & Variance)**

   - **Precedence**: `STD` is a `RID` and therefore takes precedence over `DRID` items per `T102-STD-005-CLAUSE-003`.
   - **Non-Contradiction Rule**: ADRs and lower-scope artifacts MUST NOT contradict applicable `STD` obligations.
   - **Variance Contract**: Any exception MUST be recorded as a Variance ADR and MUST cite the overridden `STD` ID.

4) **T102-STD-009-CLAUSE-004 (STD Authoring Requirements)**

   - `STD` index schemas MUST follow `T102-STD-009-CLAUSE-004A`.
   - `STD` index column guidelines MUST follow `T102-STD-009-CLAUSE-004B`.
   - `STD` body construction MUST follow `T102-STD-009-CLAUSE-004C`.
   - `STD` body conciseness targets MUST follow `T102-STD-009-CLAUSE-004D`.
   - `STD` drift controls MUST follow `T102-STD-009-CLAUSE-004E`.

   - **T102-STD-009-CLAUSE-004A (STD Index Schema)**
     - **STD Index Requirement**: Each scope MUST maintain a `STD` index table using this schema:
       `| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Governed By | Reference |`

   - **T102-STD-009-CLAUSE-004B (STD Index Column Guidelines)**
     - `STD ID`: MUST follow `T102-STD-005-CLAUSE-001`.
     - `Title`: MUST be bold and follow `T102-STD-005-CLAUSE-001` title constraints.
     - `Adopts`: MUST contain exactly one full reference to the canonical adopted normative specification.
     - `Verification`: MUST describe (a) mechanism (CI/Lint/Review), (b) what is checked, and (c) pass/fail evidence.
     - `Governed By`:
       - MUST list the governing basis used to author and maintain the STD (meta-governance) such as program governance (`P-*`) once established.
       - SHOULD include the minimal set of always-applicable governance sources (do not overload).
       - Items in `Governed By` are treated as **authoring/control obligations** (i.e., “these rules apply when producing/maintaining this STD”).
     - `Reference`:
       - MUST be treated as **supporting / traceability** references only (not “governing” and not “adoption”).
       - MUST contain ONLY `RID`-category IDs (e.g., `STD/CON/QG/DEP/IF/...`) per `T102-STD-005-CLAUSE-002`.
       - MUST NOT include `DRID`/`CLAUSE` IDs; those belong in `Governed By` (if governing) or inside the adopted spec itself.
       - References MUST obey `T102-STD-005-CLAUSE-003` directionality (no higher-scope STD referencing lower-scope IDs except permitted `INT` exception patterns).

   - **T102-STD-009-CLAUSE-004C (STD Body Construction)**
     - **Primary Obligation Sentence (required)**:
       - Format: `* **<SID>-STD-### (<Title>)** — <Normative obligation sentence>`
       - The obligation sentence MUST answer “WHAT must be true” at a stable, scope-wide level.
     - **Minimum Viable Conformance (MVC) (recommended; max 5 items)**:
       - MVC provides the minimum stable “WHAT” checkpoints required to conform, without restating the full adopted specification.
       - MVC items MUST be written as an ordered list (e.g., `1)` ...).
       - MVC items SHOULD cite adopted-spec clause IDs where possible (e.g., `T102-STD-003-CLAUSE-001`).
       - MVC items MUST NOT introduce new obligations beyond the adopted specification; if a mismatch occurs, the adopted specification remains canonical.

   - **T102-STD-009-CLAUSE-004D (STD Conciseness)**
     - STD bodies SHOULD target <200 words when feasible (excluding tables), aligning with `T102-STD-005-CLAUSE-006 (Content Quality)`.
     - Pragmatic migration exception: if `Adopts = —` is explicitly intentional, the STD body MAY extend (target ≤300 words) to remain actionable until a canonical adopted spec is available.

   - **T102-STD-009-CLAUSE-004E (Drift Controls)**
     - STD bodies MUST avoid duplicating detailed rules; the adopted normative specification is the single canonical source of truth.
     - If an adopted specification is updated in a way that changes conformance expectations, the corresponding STD body (including MVC) MUST be updated in the same change set.
     - When `STD` bodies are copied into SSOT artifacts (e.g., `sps`), those SSOT copies MUST be updated in the same change set whenever the authoritative STD body changes.

5) **T102-STD-009-CLAUSE-005 (Migration Tolerance)**

   - **Alias Window**: During migration, legacy `GDR` IDs MAY be treated as aliases of their replacement `STD` IDs for enforcement.
   - **No New GDR**: New `GDR` creation MUST be blocked after the migration cutoff milestone/date.
   - **Sunset**: Alias support MUST be removed after the migration completion milestone/date.

## Decision Record

* **T102-STD-009-ADR-001 (Governance Standards Specification)** {#t102-std-009-adr-001-governance-standards-specification}

  * **Context**
    The current `GDR` + `ADR` pairing encourages duplicated narrative (policy and rationale) and creates drift over time. A dedicated standards registry mechanism is required so normative obligations can be indexed and governed independently from decision rationale. This ADR defines the introduction and semantics of `STD` and is adopted by `T102-STD-009`.

  * **Decision**
    Establish `STD` as a normative Requirement ID (`RID`) token used to register enforceable standards and to decouple “what must be followed” from “why the choice was made”. `STD` items govern downstream artifacts via precedence rules in `T102-STD-005`. Normative keyword interpretation is governed by `T102-CON-009`.

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

## References

`T102-STD-009 (Governance Standards Model)`,
    `T102-STD-005 (ID Governance Standard)`,
    `T102-CON-009 (Normative Keywords)`

## Provenance

- `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
