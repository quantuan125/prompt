---
artifact_type: 'PROPOSAL'
initiative_id: 'P'
initiative_code: 'PROGRAM'
activity_id: 'P-PH000-ST001-AC006'
task_id: 'P-PH000-ST001-AC006-TK004'
version: '1.1.0'
date: '2026-02-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/plan_P-PH000-ST001-AC006.md'
session_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/snotes/snotes_P-PH000-ST001-AC006-SES003.md'
source_standard: 'prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md'
target_standard: 'prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md'
precedent_contract: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/proposal/proposal_P-PH000-ST001-AC002_promotion-contract-t102-std-004-to-p-std-001.md'
audit_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC006/analysis/analysis_P-PH000-ST001-AC006_pre-promotion-audit.md'
timeline_uid_inputs:
  - 'prompt/artifacts/tasks/T104/workspace/PH001/ST000/notes_T104-PH001-ST000.md'
  - 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md'
  - 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md'
---

# Proposal: Promotion Contract — T102-STD-005 to P-STD-005 (Universal ID Specification)

## I. Purpose

This proposal is the **promotion contract** for promoting `T102-STD-005 (ID Specification & Rules)` to `P-STD-005 (Universal ID Specification)` via full content transfer with 1:1 CLAUSE re-identification, plus absorption of timeline UID scope (planned as T104-STD-002) into new P-STD-005 CLAUSEs 008-011.

This proposal is the TK004 deliverable of `P-PH000-ST001-AC006` and MUST pass `P-PH000-ST001-AC006-GATE-002` (Client approval) before TK005 execution begins.

This contract provides:
1. Mechanical mapping + replacement rules so TK005 is fully deterministic.
2. Exact normative text for new/amended CLAUSEs (including Canonical ID Schema amendment).
3. Exact ADR-002 body text + index tables required for combined-file compliance.
4. Explicit alias-window terms, including the changeset-based end condition.
5. Tier 1 reference update plan bounded to the SES001 Tier 1 file list (including explicit template check evidence requirements).

**Governing decisions**:
- `P-PH000-ST001-AC006-SES002-DEC002` (hybrid authoring; ambiguities surfaced as GATE-002 open questions)
- `P-PH000-ST001-AC006-SES002-DEC003` (substandard architecture required)
- `P-PH000-ST001-AC006-SES002-DEC004` (absorb RES token Allowed Scope change into TK005)
- `P-PH000-ST001-AC006-SES002-DEC005` (do not rename deprecated skill directory)
- `P-PH000-ST001-AC006-SES003-DEC001` (CLAUSE-001 MUST incorporate timeline UID patterns; no exception-only treatment)
- `P-PH000-ST001-AC006-SES003-DEC002` (Timeline UID schema scope includes SES/GATE/Sub-Activity dotted IDs)
- `P-PH000-ST001-AC006-SES003-DEC003` (alias-window end condition is changeset-based)
- `P-PH000-ST001-AC006-SES003-DEC004` (Tier 1 list locked; template check evidence required)

## II. Source State + Audit Findings (TK003)

Pre-promotion audit verdict: PASS with non-blocking findings (`analysis_P-PH000-ST001-AC006_pre-promotion-audit.md`).

Findings to remediate during promotion (encoded in this contract):
- F001: Specification Index missing (addressed by adding Specification Index in P-STD-005).
- F002: Subclause rendering not fully aligned to `P-STD-001-CLAUSE-020A` (addressed by normalizing subclause formatting in the promoted file).
- F003: ADR missing Traceability subheading (addressed by ensuring ADR-002 contains Traceability, and by adding Traceability to the transferred ADR-001 to meet `P-STD-001-CLAUSE-025B`).

## III. CLAUSE Re-identification Mapping (1:1 Transfer)

All transferred items map 1:1. No renumbering or reordering.

| Source (T102-STD-005) | Target (P-STD-005) |
|:--|:--|
| `T102-STD-005-CLAUSE-001` | `P-STD-005-CLAUSE-001` |
| `T102-STD-005-CLAUSE-002` | `P-STD-005-CLAUSE-002` |
| `T102-STD-005-CLAUSE-003` | `P-STD-005-CLAUSE-003` |
| `T102-STD-005-CLAUSE-003A` | `P-STD-005-CLAUSE-003A` |
| `T102-STD-005-CLAUSE-003B` | `P-STD-005-CLAUSE-003B` |
| `T102-STD-005-CLAUSE-004` | `P-STD-005-CLAUSE-004` |
| `T102-STD-005-CLAUSE-005` | `P-STD-005-CLAUSE-005` |
| `T102-STD-005-CLAUSE-005A` | `P-STD-005-CLAUSE-005A` |
| `T102-STD-005-CLAUSE-005B` | `P-STD-005-CLAUSE-005B` |
| `T102-STD-005-CLAUSE-005C` | `P-STD-005-CLAUSE-005C` |
| `T102-STD-005-CLAUSE-005D` | `P-STD-005-CLAUSE-005D` |
| `T102-STD-005-CLAUSE-005E` | `P-STD-005-CLAUSE-005E` |
| `T102-STD-005-CLAUSE-005F` | `P-STD-005-CLAUSE-005F` |
| `T102-STD-005-CLAUSE-006` | `P-STD-005-CLAUSE-006` |
| `T102-STD-005-CLAUSE-007` | `P-STD-005-CLAUSE-007` |
| `T102-STD-005-ADR-001` | `P-STD-005-ADR-001` |

## IV. Replacement Rules (Apply to P-STD-005 Combined File Only)

Replacement rules MUST be applied **only** to the newly-created P-STD-005 combined file (`standard_P-STD-005_universal-id-specification.md`). They MUST NOT be applied to the source file `T102-STD-005_id-specification-rules.md` (which only receives a supersession notice per §XII).

Apply rules in order (specific-first):
- R1: `T102-STD-005-CLAUSE-` -> `P-STD-005-CLAUSE-`
- R2: `T102-STD-005-ADR-` -> `P-STD-005-ADR-`
- R3: `T102-STD-005` (standalone) -> `P-STD-005`
- R4: `t102-std-005` (lowercase anchors) -> `p-std-005`

**External reference protection** (MUST preserve these external references verbatim while applying R1-R4):
- `P-STD-001` (governance/structure)
- `T102-CON-009` (external concept reference)
- `T102-STD-003` (external standard reference)
- `T102-STD-006` (external research workflow reference)

Implementation rule: if a replacement would alter any of the above IDs/titles/paths in the `## References` external references table, do NOT apply it; restore the external references to their authoritative form after replacements.

## V. Promotion Transfer Variances (Approved Scope)

TK005 SHALL apply these variances during transfer:

1. **Heading update**:
   - Replace the main heading with:
     - `# P-STD-005 — Universal ID Specification {#p-std-005-universal-id-specification}`

2. **RES token Allowed Scope absorption** (`P-PH000-ST001-AC006-SES002-DEC004`):
   - In `P-STD-005-CLAUSE-002 (Taxonomy & Terminology)`, update the `RES` token row `Allowed Scope` from `I, E, F` to `P, I, E, F`.
   - No other token rows are modified.

3. **Format normalization to satisfy combined-file governance** (addresses TK003 findings F002/F003):
   - Subclause rendering SHOULD be normalized to `P-STD-001-CLAUSE-020A` style (subclause line contains `— <text>` on same line).
   - ADR bodies MUST include **Traceability** subheading per `P-STD-001-CLAUSE-025B`. This contract mandates adding Traceability to the transferred ADR-001 (format-only change; no decision change).

## VI. P-STD-005-CLAUSE-001 Amendment (Canonical ID Schema) [SES003-DEC001]

The promoted file MUST amend `P-STD-005-CLAUSE-001 (Canonical ID Schema)` so the canonical regex schema explicitly includes timeline UID patterns (Program + Initiative) and examples. Exception-only treatment is not allowed.

**Replace the entire content of `P-STD-005-CLAUSE-001` with the following** (exact text):

```markdown
1) **P-STD-005-CLAUSE-001 (Canonical ID Schema)**

   **Regex Patterns**: usage of all IDs MUST match one of these patterns:

   - **Pattern 1 (Initiative/Epic/Feature/Story Scope ID / SID)**: `^T\\d{3}(?:[A-Z]\\d*)?(?:-[A-Z0-9_]+)*$`
     - Examples: `T102`, `T102A`, `T102A1-S3`, `T102A-SPSST`

   - **Pattern 2 (Initiative/Epic/Feature/Story Tokenized ID)**: `^T\\d{3}(?:[A-Z]\\d*)?(?:-[A-Z0-9_]+)*-[A-Z]+-\\d{3}$`
     - Examples: `T102-QG-001`, `T102A1-NFR-005`, `T102A-SPSST-IG-002`

   - **Pattern 3 (Program Tokenized ID)**: `^P(?:-[A-Z0-9_]+)*-[A-Z]+-\\d{3}$`
     - Examples: `P-STD-001`, `P-CON-001`, `P-ADR-001`

   - **Pattern 4 (Timeline UID)**: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}(?:-ST\\d{3}(?:-AC\\d{3}(?:\\.\\d+)?(?:-TK\\d{3})?)?)?(?:-(?:SES\\d{3}(?:-(?:DP|DEC|ACT|OQ)\\d{3})?|GATE-\\d{3}))?$`
     - Examples (Phase): `P-PH000`, `T104-PH001`
     - Examples (Stream): `P-PH000-ST001`, `T104-PH001-ST002`
     - Examples (Activity): `P-PH000-ST001-AC006`, `T104-PH001-ST002-AC000`
     - Examples (Sub-Activity): `T102-PH001-ST001-AC009.1`
     - Examples (Task): `T102-PH001-ST001-AC009.1-TK003`
     - Examples (Session): `P-PH000-ST001-AC006-SES003`
     - Examples (Gate): `P-PH000-ST001-AC006-GATE-002`
     - Examples (Session Item — DP): `P-PH000-ST001-AC006-SES003-DP001`
     - Examples (Session Item — DEC): `P-PH000-ST001-AC006-SES003-DEC001`
     - Examples (Session Item — ACT): `T104-PH001-ST002-SES001-ACT001`
     - Examples (Session Item — OQ): `P-PH000-ST001-AC006-SES003-OQ001`

   **Markdown Construction**:
   - Format: `* **<ID> (<Title>)** — <Description>`
   - Title Constraints:
     - **RIDs / IIDs / OIDs**: Target: 2 words; Min: 2 words; Max: 3 words.
     - **DRIDs / STDCIDs**: Target: 2–4 words; Min: 2 words; Max: 8 words.
     - Hyphenated compounds count as 1 word.
   - Description: concise statement of the rule/requirement/decision/guidance.
```

## VII. New Timeline UID CLAUSE Text (CLAUSE-008 through CLAUSE-011)

The promoted file MUST insert the following CLAUSEs immediately after `P-STD-005-CLAUSE-007` (exact text). CLAUSE formatting MUST conform to `P-STD-001-CLAUSE-018B` and subclause formatting MUST conform to `P-STD-001-CLAUSE-020A`.

```markdown
8) **P-STD-005-CLAUSE-008 (Timeline UID Schema)**

   Timeline UIDs MUST be stable, immutable identifiers for execution management entities (Phase, Stream, Activity, Task) and for the governance qualifiers (Session, Gate) associated with those entities.

   * **P-STD-005-CLAUSE-008A (Root token)** — A timeline UID root MUST be either `P` (Program) or an initiative root `T###` optionally with an epic suffix (e.g., `T102A`, `T102A1`). Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)$`.

   * **P-STD-005-CLAUSE-008B (Phase UID)** — Phase UIDs MUST have the form `<ROOT>-PH###`. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}$`. Examples: `P-PH000`, `T104-PH001`.

   * **P-STD-005-CLAUSE-008C (Stream UID)** — Stream UIDs MUST have the form `<ROOT>-PH###-ST###`. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}$`. Examples: `P-PH000-ST001`, `T104-PH001-ST002`.

   * **P-STD-005-CLAUSE-008D (Activity UID)** — Activity UIDs MUST have the form `<ROOT>-PH###-ST###-AC###`. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}$`. Examples: `P-PH000-ST001-AC006`, `T104-PH001-ST002-AC000`.

   * **P-STD-005-CLAUSE-008E (Sub-Activity UID)** — Sub-activities MUST be expressed as a dotted suffix on the Activity token: `AC###.<n>`, where `<n>` is a positive integer. Regex: `^AC\\d{3}\\.\\d+$`. Example: `T102-PH001-ST001-AC009.1`.

   * **P-STD-005-CLAUSE-008F (Task UID)** — Task UIDs MUST have the form `<Activity-UID>-TK###` (where Activity-UID MAY include a dotted Sub-Activity). Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}(?:\\.\\d+)?-TK\\d{3}$`. Example: `T102-PH001-ST001-AC009.1-TK003`.

   * **P-STD-005-CLAUSE-008G (Session UID)** — Session UIDs MUST be expressed by appending `-SES###` to an Activity UID or Task UID. Regex (Activity session): `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}(?:\\.\\d+)?-SES\\d{3}$`. Regex (Task session): `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}(?:\\.\\d+)?-TK\\d{3}-SES\\d{3}$`. Example: `P-PH000-ST001-AC006-SES003`.

   * **P-STD-005-CLAUSE-008H (Gate UID)** — Gate UIDs MUST be expressed by appending `-GATE-###` to an Activity UID. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}-ST\\d{3}-AC\\d{3}(?:\\.\\d+)?-GATE-\\d{3}$`. Example: `P-PH000-ST001-AC006-GATE-002`.

   * **P-STD-005-CLAUSE-008I (Composition rules)** — Timeline UID tokens MUST appear in this order: `PH` then `ST` then `AC` (optionally dotted), then optional `TK`, then optional qualifier (`SES` or `GATE`). Session UIDs (`SES`) MAY be further extended with a session item type token (see CLAUSE-008J). Qualifiers and their extensions MUST NOT appear in the middle of the UID.

   * **P-STD-005-CLAUSE-008J (Session Item UID)** — Session item UIDs MUST be expressed by appending `-<TYPE>###` to a Session UID, where `<TYPE>` is one of: `DP` (Discussion Point), `DEC` (Decision), `ACT` (Action), `OQ` (Open Question). Sequences (`###`) reset per session file per `guideline_workspace_notes.md` §2.2. Regex: `^(?:P|T\\d{3}(?:[A-Z]\\d*)?)-PH\\d{3}(?:-ST\\d{3}(?:-AC\\d{3}(?:\\.\\d+)?(?:-TK\\d{3})?)?)?-SES\\d{3}-(?:DP|DEC|ACT|OQ)\\d{3}$`. Examples: `P-PH000-ST001-AC006-SES003-DP001`, `T104-PH001-ST002-SES001-DEC001`, `P-PH000-ST001-AC006-SES003-ACT001`.

9) **P-STD-005-CLAUSE-009 (UID-vs-Seq Decoupling)**

   Timeline UIDs MUST be immutable and MUST NOT be renumbered or changed to accommodate insertion, reprioritization, or re-sequencing.

   * **P-STD-005-CLAUSE-009A (Immutability)** — Once assigned, a timeline UID MUST NOT change for the life of the referenced entity.
   * **P-STD-005-CLAUSE-009B (Seq is display-only)** — Display sequence numbers (e.g., ordering in a table) MUST be treated as presentation-only and MUST NOT be used as stable identifiers.
   * **P-STD-005-CLAUSE-009C (Insertion rule)** — New work inserted between existing work MUST receive a new UID; existing UIDs MUST remain unchanged.
   * **P-STD-005-CLAUSE-009D (Cross-reference stability)** — Artifacts that reference a timeline UID MUST NOT require updates solely due to reordering.

10) **P-STD-005-CLAUSE-010 (LINK Indirection System)**

   Registers MAY use `LINK-###` indirection to reference deliverables (especially long paths) without repeating full paths throughout the register body.

   * **P-STD-005-CLAUSE-010A (LINK construction)** — LINK IDs MUST use the form `LINK-###`. Regex: `^LINK-\\d{3}$`. Example: `LINK-004`.
   * **P-STD-005-CLAUSE-010B (Pointer-only semantics)** — LINK IDs are pointers-only and non-normative. They MUST NOT be used as a substitute for authoritative standards, indices, or enforceable obligations.
   * **P-STD-005-CLAUSE-010C (Mapping requirement)** — Each LINK referenced in a register MUST be defined in an associated Links section/table that maps `LINK-###` to a canonical repo-relative path.
   * **P-STD-005-CLAUSE-010D (Stability)** — LINK IDs SHOULD be stable within the register scope; when a path changes, the mapping SHOULD be updated without changing the LINK ID.

11) **P-STD-005-CLAUSE-011 (Timeline File Naming)**

   File naming SHOULD be derived from timeline UIDs to preserve determinism and traceability between plans, notes, raw transcripts, and gate evidence.

   * **P-STD-005-CLAUSE-011A (Plan files)** — Plan files MUST use: `plan_<Timeline-UID>.md` where `<Timeline-UID>` is `(<ROOT>-PH###[-ST###[-AC###]])`. Examples: `plan_P-PH000.md`, `plan_P-PH000-ST001.md`, `plan_P-PH000-ST001-AC006.md`.
   * **P-STD-005-CLAUSE-011B (Notes registers)** — Notes register/index files MUST use: `notes_<Timeline-UID>.md` (no `SES###` token). Example: `notes_T104-PH001-ST000.md`.
   * **P-STD-005-CLAUSE-011C (Session notes)** — Session notes files MUST use: `snotes_<Timeline-UID>-SES###.md` where the stem includes the Activity UID (and optional Task UID) followed by the session token. Example: `snotes_P-PH000-ST001-AC006-SES003.md`.
   * **P-STD-005-CLAUSE-011D (Raw transcripts)** — Raw transcripts MUST use: `raw_<Timeline-UID>-SES###.<ext>` where `<ext>` is `txt` or `md`. Example: `raw_P-PH000-ST001-AC006-SES001.txt`.
   * **P-STD-005-CLAUSE-011E (Verification evidence)** — Gate evidence files MUST use: `verification_<Activity-UID>_gate-###.md` where `gate-###` corresponds to the gate number for the activity. Example: `verification_P-PH000-ST001-AC006_gate-001.md`.
```

## VIII. ADR-002 Body (Promotion Decision) + ADR-001 Traceability Normalization

### A. ADR Index (Exact Table)

Replace the ADR Index table in P-STD-005 with:

```markdown
### ADR Index
| ADR ID | Title | Status | Supersedes | Date |
|:--|:--|:--|:--|:--|
| P-STD-005-ADR-002 | Promotion from T102-STD-005 | `accepted` | ADR-001 | 2026-02-23 |
| P-STD-005-ADR-001 | ID Specification & Rules | `superseded` | — | 2026-02-23 |
```

### B. ADR-002 Body (Exact Text)

Insert this ADR body **before** ADR-001 (current-first ordering per `P-STD-001-CLAUSE-023C`):

```markdown
* **P-STD-005-ADR-002 (Promotion from T102-STD-005)** {#p-std-005-adr-002-promotion-from-t102-std-005}

  * **Context**
    `T102-STD-005` was authored at Initiative scope but defines ID and governance rules used across Program-level and multi-initiative artifacts. As Program scope standards and cross-initiative workflow artifacts expand, retaining the authoritative ID specification at Initiative scope creates a scope-identity mismatch (e.g., Program artifacts using Program timeline UIDs that are not covered by the canonical schema), and increases the risk of inconsistent ID rules across initiatives.

    Timeline UID conventions (Phase/Stream/Activity/Task, plus Gate/Session qualifiers) were planned as an initiative-scoped standard (`T104-STD-002`) but are inherently cross-initiative and must be unified with the canonical ID schema to maintain mechanical lintability.

  * **Decision**
    Promote `T102-STD-005 (ID Specification & Rules)` to `P-STD-005 (Universal ID Specification)` via full content transfer with 1:1 CLAUSE re-identification per the approved promotion contract. Mark `T102-STD-005` as `superseded` and establish an alias window for `T102-STD-005-CLAUSE-*` references per the contract terms.

    Absorb the timeline UID scope by adding `P-STD-005-CLAUSE-008` through `P-STD-005-CLAUSE-011` and by amending `P-STD-005-CLAUSE-001` to incorporate timeline UID regex patterns (no exception-only treatment).

  * **Alternatives**
    * *Adopt-by-reference*: Keep `T102-STD-005` as authoritative and reference it from Program artifacts. Rejected: preserves scope-identity mismatch and fails to resolve canonical schema conflicts for Program timeline UIDs.
    * *Timeline-only standard*: Promote only timeline UID rules and keep the rest in `T102-STD-005`. Rejected: timeline UIDs and canonical schema must be unified to keep ID validation mechanical and consistent.
    * *Status quo*: No promotion. Rejected: ongoing drift risk and ambiguous authority boundary for cross-initiative governance.

  * **Consequences**
    (+) `P-STD-005` becomes the authoritative Program-level surface for ID rules and timeline UID conventions.
    (+) Program artifacts can reference a Program standard for both canonical ID schema and timeline UIDs, reducing ambiguity and drift.
    (±) Existing `T102-STD-005-CLAUSE-*` references migrate at next touch during the alias window; a governance sync changeset will remove alias support.
    (-) One-time promotion effort: transfer content, insert new CLAUSEs, update Tier 1 references, and mark the source as superseded.

  * **Traceability**
    * `P-PH000-ST001-AC006` (Promotion activity)
    * `P-PH000-ST001-AC006-GATE-001` (Source clean-for-promotion approval)
    * `P-PH000-ST001-AC006-SES002` (Substandard architecture + RES scope absorption decisions)
    * `P-PH000-ST001-AC006-SES003` (Canonical schema amendment mandate; expanded timeline UID scope; changeset-based alias end; Tier 1 lock)
    * `T104-PH001-ST000-SES001` (Stable UIDs; initiative phases; LINK indirection inputs)
    * `T104-PH001-ST002-AC002` (Timeline UID convention scope absorbed)
    * `T102-STD-005-CLAUSE-003A` (Promotion contract rules)
    * `T102-STD-005-CLAUSE-003B` (Alias window rules)
```

### C. ADR-001 Traceability Normalization (Format-Only)

The transferred ADR-001 MUST be updated to include a **Traceability** subheading (per `P-STD-001-CLAUSE-025B`) even though the ADR status is `superseded`. This update is format-only and MUST NOT change the decision content.

Minimum Traceability bullet set to add to ADR-001:
- `T102-STD-005` (Source standard origin)
- `P-PH000-ST001-AC006` (Promotion activity)

## IX. Specification Index (11 CLAUSEs) + Substandard Architecture [SES002-DEC003]

P-STD-005 SHALL use substandard architecture with at minimum two substandards:
- `P-STD-005A` — Workscope ID Governance (CLAUSE-001 through CLAUSE-007; transferred from T102-STD-005)
- `P-STD-005B` — Timeline UID Convention (CLAUSE-008 through CLAUSE-011; absorbed scope)

The following Specification Index table MUST be inserted immediately after `## Specification`:

```markdown
### Specification Index
| # | Substandard | CLAUSE ID | Title | Description |
|:--|:--|:--|:--|:--|
| 1 | P-STD-005A | P-STD-005-CLAUSE-001 | Canonical ID Schema | Defines the canonical ID regex schema and rendering rules. |
| 2 | P-STD-005A | P-STD-005-CLAUSE-002 | Taxonomy & Terminology | Defines ID categories, tokens, and allowed scope semantics. |
| 3 | P-STD-005A | P-STD-005-CLAUSE-003 | Precedence & Hierarchy | Defines inheritance directionality and precedence rules. |
| 4 | P-STD-005A | P-STD-005-CLAUSE-004 | Reference Semantics | Defines reference styles, requirements, and external reference rules. |
| 5 | P-STD-005A | P-STD-005-CLAUSE-005 | Category Semantics | Defines semantics, lifecycle rules, and constraints per token category. |
| 6 | P-STD-005A | P-STD-005-CLAUSE-006 | Status Semantics | Defines status meanings and allowed transitions for governed artifacts. |
| 7 | P-STD-005A | P-STD-005-CLAUSE-007 | Change Semantics | Defines change semantics and recording requirements for governed artifacts. |
| 8 | P-STD-005B | P-STD-005-CLAUSE-008 | Timeline UID Schema | Defines timeline UID regex patterns and composition rules. |
| 9 | P-STD-005B | P-STD-005-CLAUSE-009 | UID-vs-Seq Decoupling | Defines immutable UIDs and display-order decoupling rules. |
| 10 | P-STD-005B | P-STD-005-CLAUSE-010 | LINK Indirection System | Defines LINK-### pointer system for register indirection. |
| 11 | P-STD-005B | P-STD-005-CLAUSE-011 | Timeline File Naming | Defines file naming conventions derived from timeline UIDs. |
```

Substandard naming is a Gate-002 approval item. If the Client prefers alternative substandard codes/names, the contract SHALL be updated before TK005 execution.

## X. Alias Window Terms [SES003-DEC003]

Alias window scope: all `T102-STD-005-CLAUSE-*` and `T102-STD-005-ADR-*` references that are superseded by `P-STD-005-*` equivalents.

Alias window rules: per `P-STD-001-CLAUSE-030C` and `T102-STD-005-CLAUSE-003B`.

**Changeset-based end condition (MANDATED)**:
- Alias support MUST remain in effect until the dedicated governance sync changeset/milestone defined here is executed.
- This contract defines the milestone as: **Governance Sync Changeset: "P-STD-005 Alias Removal"**.
- The milestone is considered executed when:
  - All Tier 1 updates (TK007/TK008) are completed, AND
  - Remaining known Tier 2 references have been migrated (or explicitly accepted as residual historical references), AND
  - A verification sweep confirms that new authoring no longer uses `T102-STD-005-*` IDs except for historical provenance.

## XI. External References Table (P-STD-005 `## References` Section)

TK005 MUST replace the entire P-STD-005 `## References` section with a table of external references. This table is the authoritative insertion surface.

```markdown
## References

### External References (Cross-Scope)
| ID | Title | Scope | Source Path |
|:--|:--|:--|:--|
| P-STD-001 | Program Governance Standard | Program (P) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| T102-STD-003 | Explicit Inheritance Model | Initiative (T102) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md` |
| T102-STD-005 | ID Specification & Rules (Superseded Source) | Initiative (T102) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md` |
| T102-STD-006 | Research Artifacts Index | Initiative (T102) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` |
| T102-CON-009 | Normative Keywords | Initiative (T102) | `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md` |
| T104-PH001-ST000-SES001 | Planning & Consultation QA Session (Inputs: Stable UIDs, Phases, LINK) | Initiative (T104) | `prompt/artifacts/tasks/T104/workspace/PH001/ST000/notes_T104-PH001-ST000.md` |
| T104-PH001-ST002 | Standards Stream Plan (Input: Timeline UID scope) | Initiative (T104) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md` |
| T104-PH001-ST002-AC000 | Directory & File Naming Convention Proposal (Approved) | Initiative (T104) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` |
```

## Provenance
### Promotion
- Promoted from: `T102-STD-005 (ID Specification & Rules)`
- Promotion activity: `P-PH000-ST001-AC006 (Promote T102-STD-005 to P-STD-005)`
- Promotion contract: `proposal_P-PH000-ST001-AC006_promotion-contract-t102-std-005-to-p-std-005.md`
- Alias window: active until Governance Sync Changeset "P-STD-005 Alias Removal" is executed (changeset-based end condition)
```

Note: This contract intentionally includes T104 inputs as references for traceability of absorbed scope. Normative CLAUSE text in P-STD-005 MUST be self-contained and MUST NOT depend on external decision documents for interpretation.

## XII. Supersession Notice Text (Insert into T102-STD-005)

TK006 MUST insert the following supersession notice immediately after the main heading and before `## Specification` in `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md`:

```markdown
> **Superseded**: This standard has been superseded by `P-STD-005 (Universal ID Specification)` at Program scope.
>
> - Successor: `P-STD-005 (Universal ID Specification)` at `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`
> - Superseded on: 2026-02-23
> - Alias window: `T102-STD-005-CLAUSE-*` references MAY be treated as aliases for `P-STD-005-CLAUSE-*` during the defined migration window. Alias support is removed after the Governance Sync Changeset "P-STD-005 Alias Removal" is executed.
```

## XIII. Tier 1 Reference Update Plan (Bounded File List) [SES003-DEC004]

Tier 1 MUST match the SES001 Tier 1 list and MUST include explicit template check evidence if no-op.

### A. P-STD-001 Back-Reference Updates (TK007)

Contracted edits to `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`:
1. References table: `T102-STD-005` row becomes `P-STD-005` with title `Universal ID Specification`, scope `Program (P)`, path `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`.
2. In-body replacements (specific-first):
   - `T102-STD-005-CLAUSE-` -> `P-STD-005-CLAUSE-`
   - `T102-STD-005` -> `P-STD-005`
   - Expected replacement set (normative references): CLAUSEs `P-STD-001-CLAUSE-003F`, `P-STD-001-CLAUSE-009A` through `P-STD-001-CLAUSE-009D`, `P-STD-001-CLAUSE-011A`, `P-STD-001-CLAUSE-012B`, `P-STD-001-CLAUSE-018A` through `P-STD-001-CLAUSE-018E`, `P-STD-001-CLAUSE-019A`, `P-STD-001-CLAUSE-020A`, `P-STD-001-CLAUSE-022A` through `P-STD-001-CLAUSE-022B`, `P-STD-001-CLAUSE-023B`, `P-STD-001-CLAUSE-024E`, `P-STD-001-CLAUSE-028A`, `P-STD-001-CLAUSE-029C`, `P-STD-001-CLAUSE-030A` through `P-STD-001-CLAUSE-030C`.
3. Residual allowance: `T102-STD-005-CLAUSE-003A/003B` MAY remain only when referenced as historical provenance for promotion/alias semantics.

### B. Remaining Tier 1 Files (TK008)

Contracted file list + instructions:
- `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`: update P-STD-005 row (status, supersedes, reference path) and update any narrative text referencing T102-STD-005.
- `prompt/artifacts/tasks/P/standard/P-STD-003_governance-standards-and-dr-index.md`: replace T102-STD-005 references with P-STD-005 equivalents.
- `prompt/templates/consultant/standards/guideline_standard_specs.md`: replace T102-STD-005 references with P-STD-005 equivalents; update changelog if modified.
- `prompt/skills/t102-adr-005-id-spec/SKILL.md`: replace T102-STD-005 references with P-STD-005; add deprecation notice; do NOT rename directory (`P-PH000-ST001-AC006-SES002-DEC005`).
- `prompt/documentation/adr_skills_catalog.md`: replace T102-STD-005 references with P-STD-005.
- `prompt/templates/consultant/standards/template_standard_specs.md`: MUST be checked even if no-op. If no `T102-STD-005` matches, record explicit evidence string: `checked/no matches` in the verification artifact for TK010.

## XIV. TK003 Findings Remediation Mapping (F001-F003)

| Finding | Where addressed in this contract | TK005 action |
|:--|:--|:--|
| F001 (Spec Index missing) | §IX | Insert Specification Index after `## Specification`. |
| F002 (Subclause formatting partial) | §V.3 + §VII clause text | Normalize subclause formatting in promoted file; ensure new clauses use `—` inline text format. |
| F003 (ADR Traceability missing) | §VIII.B + §VIII.C | ADR-002 includes Traceability; ADR-001 gets Traceability added (format-only). |

## XV. Open Questions for GATE-002

Any ambiguity below MUST be resolved by the Client at Gate-002 (or explicitly accepted as an approved assumption):

1. Substandard naming preference: accept `P-STD-005A` / `P-STD-005B` as proposed, or provide alternative names/codes.
2. Timeline UID root scope: confirm whether initiative epics (e.g., `T102A`) are permitted as timeline UID roots (allowed by the regex in CLAUSE-008A), or restrict roots to initiative-only `T###` and program `P`.

## XVI. Success Criteria Checklist (TK004)

- [ ] Contract mirrors the P-STD-001 contract precedent structure (mapping, replacement rules, new normative text, indices, alias terms, Tier 1 plan).
- [ ] CLAUSE re-identification mapping complete (7 clauses + subclauses + ADR-001).
- [ ] Timeline UID CLAUSEs (008-011) are normative-ready and include SES/GATE/Sub-Activity support.
- [ ] ADR-002 body conforms to `P-STD-001-CLAUSE-025` (Context/Decision/Alternatives/Consequences/Traceability; (+)/(±)/(-) consequences).
- [ ] Specification Index included (11 clauses; schema per `P-STD-001-CLAUSE-002A`) and substandard architecture proposed.
- [ ] Alias window terms explicit and changeset-based end condition defined.
- [ ] Tier 1 update plan bounded and file-specific; template check evidence requirement included.
- [ ] P-STD-001 back-reference updates specified.

---

## XVII. Changelog

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-23 | Initial | Promotion contract authored for GATE-002 review. Covers CLAUSE mapping (16 entities), replacement rules (R1-R4), CLAUSE-001 amendment, timeline UID CLAUSEs (008-011), ADR-002 body + index, Specification Index, alias window, Tier 1 update plan, findings remediation. |
| v1.1.0 | 2026-02-24 | Amendment | TK004.1 revision: added CLAUSE-008J (Session Item UID) for DP/DEC/ACT/OQ sub-tokens per guideline_workspace_notes.md §2.2; updated CLAUSE-001 Pattern 4 regex to accommodate session item suffix; updated CLAUSE-008I composition rules to reference CLAUSE-008J. Classification: Situation B (Scope Gap) per guideline_workspace_plan.md §VI.G. Source: Client QA at GATE-002 (2026-02-24). |
