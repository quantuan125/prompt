# Migration Report

- Mode: apply
- Root: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt`
- Files changed: 1
- Files skipped (include filter): 822
- Files skipped (exclude rules): 0
- Files skipped (encoding): 0
- Safety cap (`max-files-changed`): 5
- Include paths:
  - `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md`
- Exclude globs:
  - `**/scripts/output/**`
  - `**/workspace/scripts/report_*.md`

## Change Summary

- `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md`
  - rename: `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md` -> `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md`
  - clause_rewrites: 15
  - dr_anchor_regenerations: 1
  - dr_body_id_rewrites: 1
  - heading_rewrites: 1
  - legacy_slug_rewrites: 1

## Unified Diffs

### `/mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md`

```diff
--- /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md
+++ /mnt/c/Users/quant/OneDrive/Documents/Purpose/Crypto/PERP/prompt/artifacts/tasks/T102/consultant/standards/T102-STD-009_governance-standards-specification.md
@@ -1,8 +1,8 @@
-# T102-STD-009 — Governance Standards Specification
+# T102-STD-009 — Governance Standards Specification
 
 ## Decision
 
-* **T102-STD-009 (Governance Standards Specification)** {#t102-std-009-governance-standards-spec}
+* **T102-STD-009-ADR-001 (Governance Standards Specification)** {#t102-std-009-adr-001-governance-standards-specification}
 
   * **Context**
     The current `GDR` + `ADR` pairing encourages duplicated narrative (policy and rationale) and creates drift over time. A dedicated standards registry mechanism is required so normative obligations can be indexed and governed independently from decision rationale. This ADR defines the introduction and semantics of `STD` and is adopted by `T102-STD-009`.
@@ -32,38 +32,38 @@
 
 ## Specification
 
-1) **T102-STD-009-CLAUSE-001 (Semantics & Scope)**
+1) **T102-STD-009-CLAUSE-001 (Semantics & Scope)**
 
    - **Category**: `STD` is a normative `RID` token representing an enforceable standard.
    - **Creation Scope**: `STD` MUST only be created at Program (`P`), Initiative (`I`), Epic (`E`), and Feature (`F`) scopes.
    - **Reference Scope**: Artifacts at any scope MAY reference `STD`.
    - **Invalid Usage**: `STD` MUST NOT be used for informative guidance (`IG`) or integration notes (`INT`).
 
-2) **T102-STD-009-CLAUSE-002 (Adoption Contract)**
+2) **T102-STD-009-CLAUSE-002 (Adoption Contract)**
 
    - **Single Canonical Adopted Spec**: Every `STD` entry MUST declare exactly one `Adopts` reference.
    - **Incorporation by Reference**: The adopted normative specification is incorporated by reference into the `STD`. The `STD` remains the authoritative RID-level handle; the adopted spec is the canonical text.
    - **No Rationale Duplication**: `STD` bodies MUST NOT contain alternatives analysis or lengthy trade-offs. These MUST be captured in ADRs.
 
-3) **T102-STD-009-CLAUSE-003 (Precedence & Variance)**
+3) **T102-STD-009-CLAUSE-003 (Precedence & Variance)**
 
    - **Precedence**: `STD` is a `RID` and therefore takes precedence over `DRID` items per `T102-STD-005-CLAUSE-003`.
    - **Non-Contradiction Rule**: ADRs and lower-scope artifacts MUST NOT contradict applicable `STD` obligations.
    - **Variance Contract**: Any exception MUST be recorded as a Variance ADR and MUST cite the overridden `STD` ID.
 
-4) **T102-STD-009-CLAUSE-004 (STD Authoring Requirements)**
+4) **T102-STD-009-CLAUSE-004 (STD Authoring Requirements)**
 
-   - `STD` index schemas MUST follow `T102-STD-009-CLAUSE-004A`.
-   - `STD` index column guidelines MUST follow `T102-STD-009-CLAUSE-004B`.
-   - `STD` body construction MUST follow `T102-STD-009-CLAUSE-004C`.
-   - `STD` body conciseness targets MUST follow `T102-STD-009-CLAUSE-004D`.
-   - `STD` drift controls MUST follow `T102-STD-009-CLAUSE-004E`.
+   - `STD` index schemas MUST follow `T102-STD-009-CLAUSE-004A`.
+   - `STD` index column guidelines MUST follow `T102-STD-009-CLAUSE-004B`.
+   - `STD` body construction MUST follow `T102-STD-009-CLAUSE-004C`.
+   - `STD` body conciseness targets MUST follow `T102-STD-009-CLAUSE-004D`.
+   - `STD` drift controls MUST follow `T102-STD-009-CLAUSE-004E`.
 
-   - **T102-STD-009-CLAUSE-004A (STD Index Schema)**
+   - **T102-STD-009-CLAUSE-004A (STD Index Schema)**
      - **STD Index Requirement**: Each scope MUST maintain a `STD` index table using this schema:
        `| STD ID | Title | Status | Owner | Effective | Supersedes | Adopts | Verification | Governed By | Reference |`
 
-   - **T102-STD-009-CLAUSE-004B (STD Index Column Guidelines)**
+   - **T102-STD-009-CLAUSE-004B (STD Index Column Guidelines)**
      - `STD ID`: MUST follow `T102-STD-005-CLAUSE-001`.
      - `Title`: MUST be bold and follow `T102-STD-005-CLAUSE-001` title constraints.
      - `Adopts`: MUST contain exactly one full reference to the canonical adopted normative specification.
@@ -78,7 +78,7 @@
        - MUST NOT include `DRID`/`CLAUSE` IDs; those belong in `Governed By` (if governing) or inside the adopted spec itself.
        - References MUST obey `T102-STD-005-CLAUSE-003` directionality (no higher-scope STD referencing lower-scope IDs except permitted `INT` exception patterns).
 
-   - **T102-STD-009-CLAUSE-004C (STD Body Construction)**
+   - **T102-STD-009-CLAUSE-004C (STD Body Construction)**
      - **Primary Obligation Sentence (required)**:
        - Format: `* **<SID>-STD-### (<Title>)** — <Normative obligation sentence>`
        - The obligation sentence MUST answer “WHAT must be true” at a stable, scope-wide level.
@@ -88,16 +88,16 @@
        - MVC items SHOULD cite adopted-spec clause IDs where possible (e.g., `T102-STD-003-CLAUSE-001`).
        - MVC items MUST NOT introduce new obligations beyond the adopted specification; if a mismatch occurs, the adopted specification remains canonical.
 
-   - **T102-STD-009-CLAUSE-004D (STD Conciseness)**
+   - **T102-STD-009-CLAUSE-004D (STD Conciseness)**
      - STD bodies SHOULD target <200 words when feasible (excluding tables), aligning with `T102-STD-005-CLAUSE-006 (Content Quality)`.
      - Pragmatic migration exception: if `Adopts = —` is explicitly intentional, the STD body MAY extend (target ≤300 words) to remain actionable until a canonical adopted spec is available.
 
-   - **T102-STD-009-CLAUSE-004E (Drift Controls)**
+   - **T102-STD-009-CLAUSE-004E (Drift Controls)**
      - STD bodies MUST avoid duplicating detailed rules; the adopted normative specification is the single canonical source of truth.
      - If an adopted specification is updated in a way that changes conformance expectations, the corresponding STD body (including MVC) MUST be updated in the same change set.
      - When `STD` bodies are copied into SSOT artifacts (e.g., `sps`), those SSOT copies MUST be updated in the same change set whenever the authoritative STD body changes.
 
-5) **T102-STD-009-CLAUSE-005 (Migration Tolerance)**
+5) **T102-STD-009-CLAUSE-005 (Migration Tolerance)**
 
    - **Alias Window**: During migration, legacy `GDR` IDs MAY be treated as aliases of their replacement `STD` IDs for enforcement.
    - **No New GDR**: New `GDR` creation MUST be blocked after the migration cutoff milestone/date.
```
