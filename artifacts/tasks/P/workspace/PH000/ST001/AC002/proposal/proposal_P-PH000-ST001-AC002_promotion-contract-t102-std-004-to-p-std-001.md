---
artifact_type: 'PROPOSAL'
initiative_id: 'P'
initiative_code: 'PROGRAM'
activity_id: 'P-PH000-ST001-AC002'
task_id: 'P-PH000-ST001-AC002-TK002'
version: '1.0.0'
date: '2026-02-20'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/plan_P-PH000-ST001-AC002.md'
session_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/snotes/snotes_P-PH000-ST001-AC002-SES002.md'
source_standard: 'prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md'
target_standard: 'prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md'
---

# Proposal: Promotion Contract — T102-STD-004 to P-STD-001 (Full Content Transfer)

## I. PURPOSE

This proposal serves as the **promotion contract** for the full content transfer of `T102-STD-004` (Specification Standard & Guideline) to `P-STD-001` (Program Governance Standard). It is the deliverable of `P-PH000-ST001-AC002-TK002` and must pass `GATE-001` (Client approval) before TK003 execution begins.

The proposal provides:
1. A cross-review gap analysis identifying format and schema violations in the original implementation plan (SES001).
2. Decision-complete, corrected content for all new material (CLAUSE-030, ADR-003, index entries).
3. Mechanical instructions (replacement rules, mapping tables) so TK003 execution requires no implementer decisions.

**Governing decisions**: `P-PH000-ST001-AC002-SES001-DEC001` through `DEC006`, `P-PH000-ST001-AC002-SES002-DEC001` through `DEC003`.

---

## II. GAP ANALYSIS (Cross-Review of Implementation Plan SES001)

A cross-review of the implementation plan (`.claude/plans/plan_P-PH000-ST001-AC002-SES001_full-promotion-t102-std-004.md`, Steps 3–7) against the source standard (`T102-STD-004`) and governing CLAUSEs identified 14 gaps. All gaps are resolved in this proposal.

### A. Blocking Gaps (Format/Schema Violations)

| Gap | Description | Violated CLAUSE | Resolution | Proposal Section |
|:--|:--|:--|:--|:--|
| GAP-1 | CLAUSE-030 uses `### heading: Title` format | `T102-STD-004-CLAUSE-018B` | Rewritten to `n) **CLAUSE-ID (Title)**` format | §V |
| GAP-2 | CLAUSE-030 subclauses use `**030.A — Title**:` format | `T102-STD-004-CLAUSE-020A` | Rewritten to `* **CLAUSE-ID (Title)** —` nested bullet format | §V |
| GAP-3 | ADR-003 header uses `### heading --` format | `T102-STD-004-CLAUSE-025A` | Rewritten to `* **STD-ADR-### (Title)** {#anchor}` format | §VII |
| GAP-4 | ADR-003 Consequences uses narrative prose | `T102-STD-004-CLAUSE-025G` | Rewritten with `(+)/(±)/(-)` prefix bullets | §VII |
| GAP-5 | ADR Index row has misaligned columns (date in Supersedes, DEC ref in Date) | `T102-STD-004-CLAUSE-023A` | Corrected 5-column row matching schema | §VIII |
| GAP-6 | Two `accepted` ADRs (ADR-002 + ADR-003) violates single-accepted rule | `T102-STD-004-CLAUSE-023D` | ADR-002 → `superseded`; ADR-003 supersedes ADR-002; current-first ordering per CLAUSE-023C | §VIII |
| GAP-7 | Specification Index entry for CLAUSE-030 has 3 columns instead of 5 | `T102-STD-004-CLAUSE-002A` | Corrected to 5-column row matching schema | §VI |

### B. Moderate Gaps (Implementer Confusion Risk)

| Gap | Description | Resolution | Proposal Section |
|:--|:--|:--|:--|
| GAP-8 | External References table lists 4 T102-scoped IDs; source file has 8 | Complete table with all 8 T102-scoped IDs, titles populated | §XI |
| GAP-9 | References section treatment ambiguous (add subsection or replace?) | Clarified: restructure as `### External References (Cross-Scope)` table | §XII |
| GAP-10 | SPS step references `Canonical Path` column; actual SPS uses `Adopts`/`Reference` columns | Explicit column mapping provided in AC002 TK006 Steps | AC002 plan TK006 |

### C. Minor Gaps (Non-Blocking, Addressed for Completeness)

| Gap | Description | Resolution | Proposal Section |
|:--|:--|:--|:--|
| GAP-11 | CLAUSE-030 uses `SHALL` instead of `MUST` (inconsistent with CLAUSE-008B preference) | CLAUSE-030 rewritten with `MUST` for obligations, `MAY` for permissions | §V |
| GAP-12 | Guideline Sections I and II.C cite CLAUSE-016 as "Combined-File Canonical Structure" — actual title is "STD Status Management" | Fix during guideline migration (TK005) | §XV |
| GAP-13 | Guideline Section IV has hardcoded T102 example path not in plan's fix list | Include in TK005 hardcoded path fixes | §XV |
| GAP-14 | Guideline has no Changelog section; plan says to add changelog entry | Create Changelog section during TK005 | §XV |

---

## III. CLAUSE RE-IDENTIFICATION MAPPING

All 29 CLAUSEs transfer 1:1. No renumbering, reordering, or content changes (except CLAUSE-015A per §IX).

| # | Source (T102-STD-004) | Target (P-STD-001) | Substandard |
|:--|:--|:--|:--|
| 1 | `T102-STD-004-CLAUSE-001` | `P-STD-001-CLAUSE-001` | A (Core Structure & Lifecycle) |
| 2 | `T102-STD-004-CLAUSE-002` | `P-STD-001-CLAUSE-002` | A |
| 3 | `T102-STD-004-CLAUSE-003` | `P-STD-001-CLAUSE-003` | A |
| 4 | `T102-STD-004-CLAUSE-004` | `P-STD-001-CLAUSE-004` | A |
| 5 | `T102-STD-004-CLAUSE-005` | `P-STD-001-CLAUSE-005` | A |
| 6 | `T102-STD-004-CLAUSE-006` | `P-STD-001-CLAUSE-006` | A |
| 7 | `T102-STD-004-CLAUSE-007` | `P-STD-001-CLAUSE-007` | A |
| 8 | `T102-STD-004-CLAUSE-008` | `P-STD-001-CLAUSE-008` | A |
| 9 | `T102-STD-004-CLAUSE-009` | `P-STD-001-CLAUSE-009` | B (STD Registry & Governance) |
| 10 | `T102-STD-004-CLAUSE-010` | `P-STD-001-CLAUSE-010` | B |
| 11 | `T102-STD-004-CLAUSE-011` | `P-STD-001-CLAUSE-011` | B |
| 12 | `T102-STD-004-CLAUSE-012` | `P-STD-001-CLAUSE-012` | B |
| 13 | `T102-STD-004-CLAUSE-013` | `P-STD-001-CLAUSE-013` | B |
| 14 | `T102-STD-004-CLAUSE-014` | `P-STD-001-CLAUSE-014` | B |
| 15 | `T102-STD-004-CLAUSE-015` | `P-STD-001-CLAUSE-015` | B |
| 16 | `T102-STD-004-CLAUSE-016` | `P-STD-001-CLAUSE-016` | B |
| 17 | `T102-STD-004-CLAUSE-017` | `P-STD-001-CLAUSE-017` | B |
| 18 | `T102-STD-004-CLAUSE-018` | `P-STD-001-CLAUSE-018` | C (Specification Authoring) |
| 19 | `T102-STD-004-CLAUSE-019` | `P-STD-001-CLAUSE-019` | C |
| 20 | `T102-STD-004-CLAUSE-020` | `P-STD-001-CLAUSE-020` | C |
| 21 | `T102-STD-004-CLAUSE-021` | `P-STD-001-CLAUSE-021` | C |
| 22 | `T102-STD-004-CLAUSE-022` | `P-STD-001-CLAUSE-022` | C |
| 23 | `T102-STD-004-CLAUSE-023` | `P-STD-001-CLAUSE-023` | D (Decision Record Authoring) |
| 24 | `T102-STD-004-CLAUSE-024` | `P-STD-001-CLAUSE-024` | D |
| 25 | `T102-STD-004-CLAUSE-025` | `P-STD-001-CLAUSE-025` | D |
| 26 | `T102-STD-004-CLAUSE-026` | `P-STD-001-CLAUSE-026` | D |
| 27 | `T102-STD-004-CLAUSE-027` | `P-STD-001-CLAUSE-027` | D |
| 28 | `T102-STD-004-CLAUSE-028` | `P-STD-001-CLAUSE-028` | D |
| 29 | `T102-STD-004-CLAUSE-029` | `P-STD-001-CLAUSE-029` | D |
| **30** | **(new)** | **`P-STD-001-CLAUSE-030`** | **B** (appended) |

**Substandard re-identification**:

| Source | Target |
|:--|:--|
| `T102-STD-004A` | `P-STD-001A` |
| `T102-STD-004B` | `P-STD-001B` |
| `T102-STD-004C` | `P-STD-001C` |
| `T102-STD-004D` | `P-STD-001D` |

**ADR re-identification**:

| Source | Target | Status After Promotion |
|:--|:--|:--|
| `T102-STD-004-ADR-001` | `P-STD-001-ADR-001` | `superseded` (unchanged) |
| `T102-STD-004-ADR-002` | `P-STD-001-ADR-002` | `superseded` (changed from `accepted` per GAP-6) |
| **(new)** | **`P-STD-001-ADR-003`** | **`accepted`** |

---

## IV. REPLACEMENT RULES (Ordered)

Apply these find/replace operations to the copied T102-STD-004 content **in this exact order** to avoid double-replacement:

| # | Find | Replace | Scope | Notes |
|:--|:--|:--|:--|:--|
| R1 | `T102-STD-004-CLAUSE-` | `P-STD-001-CLAUSE-` | All occurrences | Catches all CLAUSE refs (longest prefix first) |
| R2 | `T102-STD-004-ADR-` | `P-STD-001-ADR-` | All occurrences | Catches all ADR refs |
| R3 | `T102-STD-004A` | `P-STD-001A` | All occurrences | Substandard A |
| R4 | `T102-STD-004B` | `P-STD-001B` | All occurrences | Substandard B |
| R5 | `T102-STD-004C` | `P-STD-001C` | All occurrences | Substandard C |
| R6 | `T102-STD-004D` | `P-STD-001D` | All occurrences | Substandard D |
| R7 | `T102-STD-004` (standalone, not already caught by R1–R6) | `P-STD-001` | All remaining self-references | Catches heading, prose references |
| R8 | `t102-std-004` (lowercase, in anchor tags `{#...}`) | `p-std-001` | All anchor IDs | Anchors are lowercase |

**CRITICAL**: Do NOT replace references to other T102 IDs. The following MUST remain unchanged — they are External References from P-scope to T102-scope:
* `T102-STD-005` (and all its CLAUSEs: `T102-STD-005-CLAUSE-*`)
* `T102-CON-009`
* `T102-QG-001`
* `T102-STD-001`
* `T102-STD-009`
* `T102-IG-007`, `T102-IG-008`, `T102-IG-009`
* All `T102-PH001-ST001-*` timeline entity IDs in ADR Traceability sections

**Main heading replacement** (manual, not caught by R1–R8):
* From: `# T102-STD-004 — Specification Standard & Guideline {#t102-std-004-specification-standard-and-guideline}`
* To: `# P-STD-001 — Program Governance Standard {#p-std-001-program-governance-standard}`

---

## V. NEW CONTENT: P-STD-001-CLAUSE-030 (Normative Text)

> This CLAUSE is new content authored at P-scope. It has no T102-STD-004 antecedent (per `P-PH000-ST001-AC002-SES001-DEC003`). It is placed at the end of Substandard B (after CLAUSE-017, which becomes P-STD-001-CLAUSE-017 after re-identification).
>
> Format corrected per GAP-1 (CLAUSE-018B), GAP-2 (CLAUSE-020A), GAP-11 (CLAUSE-008B `MUST` preference).

**Insert the following after the last CLAUSE in Substandard B:**

```markdown
30) **P-STD-001-CLAUSE-030 (Standard Promotion & Demotion Lifecycle)**

   A combined standard-specification surface MAY be promoted to a higher governance scope (e.g., Initiative → Program) or deprecated when its applicability changes. This clause defines the governance lifecycle for such transitions.

   * **P-STD-001-CLAUSE-030A (Promotion Eligibility)** — A standard is eligible for scope promotion when: (1) its normative content is stable (no open structural amendments in progress), and (2) it applies to, or is adopted by, multiple downstream scopes.

   * **P-STD-001-CLAUSE-030B (Promotion Process)** — A scope promotion MUST satisfy the following process: (1) A promotion contract MUST be drafted documenting: (i) the source standard ID, (ii) the target standard ID at the higher scope, (iii) the re-identification mapping for all CLAUSEs, substandards, and ADRs, (iv) any variances introduced at the new scope, (v) alias window terms per `P-STD-001-CLAUSE-030C`. (2) The promotion contract MUST pass a Client approval gate before execution. (3) The target standard MUST receive the full normative content of the source standard, re-identified to the new scope per `T102-STD-005-CLAUSE-003A`. (4) The source standard MUST be marked `superseded` with a pointer to the target standard. (5) The promotion event MUST be recorded as an ADR in the target standard's Decision Record section.

   * **P-STD-001-CLAUSE-030C (Alias Window)** — Per `T102-STD-005-CLAUSE-003B`, during a defined migration period, superseded CLAUSE IDs (e.g., `T102-STD-004-CLAUSE-001`) MAY be treated as aliases for the promoted CLAUSE IDs (e.g., `P-STD-001-CLAUSE-001`). Alias support MUST be removed after the migration completion milestone, which MUST be defined in the promotion contract.

   * **P-STD-001-CLAUSE-030D (Deprecation)** — A program-level standard MAY be deprecated when it is no longer applicable to any active scope. The standard status MUST be changed to `deprecated`. All adopters MUST be notified via a governance changeset. Deprecated standards MUST NOT be referenced by new authoring.

   * **P-STD-001-CLAUSE-030E (Promotion Record)** — Each promotion event MUST produce: (1) an ADR in the target standard documenting the promotion decision, (2) a supersession notice in the source standard, (3) updates to the relevant SPS STD Index rows (source → `superseded`; target → `draft` or `accepted`).
```

---

## VI. SPECIFICATION INDEX ENTRY (CLAUSE-030)

> Corrected per GAP-7. Matches the 5-column schema defined by `T102-STD-004-CLAUSE-002A`.

**Add as the last row in Substandard B block of the Specification Index:**

```markdown
| 30 | P-STD-001B | P-STD-001-CLAUSE-030 | Standard Promotion & Demotion Lifecycle | Defines governance lifecycle for standard scope promotion and demotion. |
```

---

## VII. NEW CONTENT: P-STD-001-ADR-003 (Decision Record Body)

> Format corrected per GAP-3 (CLAUSE-025A header), GAP-4 (CLAUSE-025G consequences). This ADR supersedes ADR-002 per GAP-6 (CLAUSE-023D).
>
> Per CLAUSE-023C (current-first ordering), this ADR body MUST be placed **BEFORE** ADR-002 in the `## Decision Record` section.

```markdown
* **P-STD-001-ADR-003 (Full Promotion from T102-STD-004)** {#p-std-001-adr-003-full-promotion-from-t102-std-004}

  * **Context**
    `T102-STD-004` was authored at Initiative scope (T102) but governs a concern applicable to all initiatives program-wide: the combined standard-specification authoring model. As additional initiatives (T104, future) require conformance to the same authoring rules, having the authoritative standard at Initiative scope creates scope-identity misalignment, reference ambiguity, and development location confusion.

  * **Decision**
    Promote `T102-STD-004` to `P-STD-001` via full content transfer with 1:1 CLAUSE re-identification. Mark `T102-STD-004` as `superseded`. Establish an alias window per `T102-STD-005-CLAUSE-003B` for existing references.

  * **Alternatives**
    * *Adopt-by-reference*: `P-STD-001` as thin wrapper incorporating `T102-STD-004` by normative reference. Rejected: creates two-hop reference pattern, scope-identity mismatch, principal-agent problem for development location. Scored 2.50 vs 4.60 in weighted analysis.
    * *Status quo*: No promotion; downstream consumers reference `T102-STD-004` directly. Rejected: `T102` prefix misleads about governance scope; no program-level authority surface exists.

  * **Consequences**
    (+) `P-STD-001` is the single authoritative surface for standard-specification authoring at Program scope.
    (+) All new references use `P-STD-001`; guideline/template authority chains updated from `T102-STD-004` to `P-STD-001`.
    (+) Future standard promotions (`P-STD-002` through `P-STD-005`) follow the precedent and process defined in `P-STD-001-CLAUSE-030`.
    (±) `T102-STD-004` becomes a read-only historical artifact (status: `superseded`); existing references migrate at next touch during the alias window.
    (-) One-time migration effort to re-identify 29 CLAUSEs, 4 substandards, and 2 ADRs; alias window required for transition.

  * **Traceability**
    * `P-PH000-ST001-AC002-SES001-DEC001` (Full Promotion methodology approval)
    * `P-PH000-ST001-AC002-SES001-DEC002` (1:1 CLAUSE renumbering + CLAUSE-030)
    * `P-PH000-ST001-AC002-SES001-DEC003` (CLAUSE-030 placement in Substandard B)
    * `P-PH000-ST001-AC002-SES001-DEC006` (CLAUSE-015A directory canonical form)
    * `analysis_P-PH000-ST001-AC002_promotion-methodology-comparison.md` (weighted criteria analysis)
    * `T102-STD-005-CLAUSE-003A` (promotion contract rules)
    * `T102-STD-005-CLAUSE-003B` (alias window rules)
```

---

## VIII. ADR INDEX UPDATE (Corrected)

> Corrected per GAP-5 (column alignment), GAP-6 (single-accepted ADR rule). Schema per `P-STD-001-CLAUSE-023A`.

**Replace the entire ADR Index table with:**

```markdown
### ADR Index
| ADR ID | Title | Status | Supersedes | Date |
|:--|:--|:--|:--|:--|
| P-STD-001-ADR-003 | Full Promotion from T102-STD-004 | `accepted` | ADR-002 | 2026-02-20 |
| P-STD-001-ADR-002 | Combined Authoring & Governance Standard | `superseded` | ADR-001 | 2026-02-15 |
| P-STD-001-ADR-001 | Specification Standard & Guideline | `superseded` | — | 2026-02-08 |
```

**ADR body ordering** (per `P-STD-001-CLAUSE-023C`, current-first):
1. ADR-003 body (§VII above) — **first**
2. ADR-002 body (transferred from T102-STD-004, re-identified) — second
3. ADR-001 body (transferred from T102-STD-004, re-identified) — third

---

## IX. CLAUSE-015A VARIANCE

> Per `P-PH000-ST001-AC002-SES001-DEC006`. Canonical form grounded in `proposal_T104-PH001-ST002-AC000` Convention 3.

**After applying R1–R8, find the re-identified `P-STD-001-CLAUSE-015A` and replace the designated directory path:**

Old text (after R1–R8 replacement):
```
Combined standard-specification files MUST live under the designated standards directory: `prompt/artifacts/tasks/<SID>/consultant/standards/`.
```

New text:
```
Combined standard-specification files MUST live under the designated standards directory: `prompt/artifacts/tasks/<SID>/standard/`. File naming MUST follow `standard_<SID-STD>_<kebab-title>.md`.
```

**Add informative note immediately after the subclause:**
```markdown
> *Informative*: T102's existing `consultant/standards/` directory is grandfathered per `proposal_T104-PH001-ST002-AC000` Convention 3. New initiatives MUST use `<SID>/standard/`.
```

---

## X. ALIAS WINDOW TERMS

> Per `T102-STD-005-CLAUSE-003B` and `P-PH000-ST001-AC002-SES001-DEC001`.

**Scope**: All existing `T102-STD-004-CLAUSE-*` references across the repository.

**Rules**:
1. During the alias window, `T102-STD-004-CLAUSE-###` MAY be treated as an alias for `P-STD-001-CLAUSE-###` (1:1 mapping per §III).
2. New authoring MUST reference `P-STD-001-CLAUSE-###`.
3. Existing references SHOULD be migrated to `P-STD-001-CLAUSE-###` at next touch of the referencing artifact.
4. Alias support MUST be removed after a dedicated governance sync changeset (milestone TBD).

**Migration exclusion**: This activity (`P-PH000-ST001-AC002`) does NOT perform repo-wide remediation sweeps. References within `T102-PH001-ST001` and other T102 plans migrate at next touch or via a future governance sync.

---

## XI. EXTERNAL REFERENCES TABLE (Complete)

> Corrected per GAP-8. All T102-scoped IDs referenced within the P-STD-001 body (Specification section, Decision Record section, and References section).

**Replace the existing `## References` section content with the following structured table:**

```markdown
## References

### External References (Cross-Scope: Program → Initiative T102)

| Referenced ID | Title | Scope | Source Path |
|:--|:--|:--|:--|
| `T102-STD-005` | ID Specification & Rules | Initiative (T102) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md` |
| `T102-CON-009` | Controlled Vocabulary for Normative Language | Initiative (T102) | See `sps_T102-CONSULTANT.md` |
| `T102-QG-001` | Client Readability | Initiative (T102) | See `sps_T102-CONSULTANT.md` |
| `T102-STD-001` | Consultancy Operating Model Standard | Initiative (T102) | See `sps_T102-CONSULTANT.md` |
| `T102-STD-009` | Governance Standards Specification | Initiative (T102) | See `sps_T102-CONSULTANT.md` (status: `deprecated`) |
| `T102-IG-007` | ID Standard | Initiative (T102) | See `sps_T102-CONSULTANT.md` |
| `T102-IG-008` | Decision Logging | Initiative (T102) | See `sps_T102-CONSULTANT.md` |
| `T102-IG-009` | Traceability Framework | Initiative (T102) | See `sps_T102-CONSULTANT.md` |
```

---

## XII. REFERENCES SECTION TREATMENT

> Resolves GAP-9 (ambiguity about existing References section).

**Approach**: The existing comma-separated reference list in T102-STD-004's `## References` section is **replaced** (not supplemented) by the structured External References table in §XI above. Rationale:
* After promotion, ALL references in the section are cross-scope (P → T102).
* The table format provides the Source Path column required for cross-scope traceability.
* No redundancy between old format and new format.

The `## References` section heading is retained (required by `P-STD-001-CLAUSE-001A`). Its content becomes the `### External References (Cross-Scope)` subsection from §XI.

---

## XIII. SUPERSESSION NOTICE (For T102-STD-004)

> Exact text for TK004 to insert into `standard_T102-STD-004_specification-standard-and-guideline.md`.

**Insert immediately AFTER the main heading and BEFORE the `## Specification` section:**

```markdown
> **SUPERSEDED**: This standard has been promoted to **P-STD-001** (Program Governance Standard) as of 2026-02-20. See `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`.
>
> **Alias Window (Active)**: Existing references to `T102-STD-004-CLAUSE-*` remain valid as aliases for `P-STD-001-CLAUSE-*` during the migration period. New authoring MUST reference `P-STD-001`. Alias support will be removed after a dedicated governance sync changeset.
>
> **This file is retained as a read-only historical artifact. Do not modify normative content.**
```

**Add to Provenance section** (at bottom of file, append or update existing Provenance):

```markdown
| Superseded By | `P-STD-001` (Program Governance Standard) |
| Supersession Date | 2026-02-20 |
| Promotion Decision | `P-STD-001-ADR-003` |
```

---

## XIV. PROVENANCE TEMPLATE (For P-STD-001)

> Replaces the existing T102-STD-004 Provenance section in the promoted file.

```markdown
## Provenance

| Field | Value |
|:--|:--|
| Supersedes | `T102-STD-004` (Specification Standard & Guideline) |
| Promotion Date | 2026-02-20 |
| Promotion Contract | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/proposal/proposal_P-PH000-ST001-AC002_promotion-contract-t102-std-004-to-p-std-001.md` |
| Promotion Decision | `P-STD-001-ADR-003` |
| Alias Window | Active — existing `T102-STD-004-CLAUSE-*` references valid as aliases until migration completion |
| Original Authoring | T102-PH001-ST001 (Initiative T102, Consultancy Development Workflow) |
| Original Author(s) | LLM_Consultant |
| Original Provenance | `prompt/artifacts/tasks/T102/workspace/PH001/ST001/AC009/proposal/proposal_T102-CWD_PH001-ST001-AC009_std-004-redesign.md`, `prompt/artifacts/tasks/T102/workspace/PH001/ST001/AC009.1/proposal/proposal_T102-CWD_PH001-ST001-AC009.1_tk003_std-004-clause-019-sequencing-amendment.md` |
| Promotion Author | LLM_Consultant |
| Analysis Evidence | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/analysis/analysis_P-PH000-ST001-AC002_promotion-methodology-comparison.md` |
| Session Evidence | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/snotes/snotes_P-PH000-ST001-AC002-SES001.md` |
```

---

## XV. GUIDELINE REVISION CORRECTIONS

> Pre-existing errors and structural gaps to fix during TK005 (guideline migration).

### A. CLAUSE-016 Mis-Citation Fix (GAP-12)

The guideline incorrectly cites `CLAUSE-016` as governing canonical file structure in two locations:

| Location | Current (Incorrect) | Corrected |
|:--|:--|:--|
| Section I (Purpose) | `T102-STD-004-CLAUSE-016 (Combined-File Canonical Structure)` | `P-STD-001-CLAUSE-001 (Canonical File Structure)` |
| Section II.C heading | `[per T102-STD-004-CLAUSE-016]` | `[per P-STD-001-CLAUSE-001]` |

**Rationale**: CLAUSE-016 is "STD Status Management" (status enums and supersession metadata). CLAUSE-001 is "Canonical File Structure" (required sections and order). The guideline's Section II.C describes canonical section order — this is governed by CLAUSE-001, not CLAUSE-016.

### B. Section IV Example Path (GAP-13)

Current hardcoded example:
```
prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md
```

Replace with portable example:
```
prompt/artifacts/tasks/<SID>/standard/standard_<SID-STD>_<kebab-title>.md
```

### C. Changelog Section Creation (GAP-14)

The guideline currently has no Changelog section. Add after Section VII:

```markdown
---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v4.0.0 | 2026-02-20 | Major | Authority chain migrated from `T102-STD-004` to `P-STD-001` following full promotion (`P-STD-001-ADR-003`). All CLAUSE references updated. Hardcoded T102 paths replaced with `<SID>/standard/` portable form per `P-STD-001-CLAUSE-015A`. Pre-existing CLAUSE-016 mis-citations corrected to CLAUSE-001. |
```

---

## XVI. REFERENCES

| Reference | Path |
|:--|:--|
| T102-STD-004 (source standard) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md` |
| T102-STD-005 (ID specification / promotion rules) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md` |
| AC002 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/plan_P-PH000-ST001-AC002.md` |
| Implementation Plan (SES001, historical) | `.claude/plans/plan_P-PH000-ST001-AC002-SES001_full-promotion-t102-std-004.md` |
| Analysis (promotion methodology) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/analysis/analysis_P-PH000-ST001-AC002_promotion-methodology-comparison.md` |
| Session Notes (SES001) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/snotes/snotes_P-PH000-ST001-AC002-SES001.md` |
| Session Notes (SES002) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/snotes/snotes_P-PH000-ST001-AC002-SES002.md` |
| Program SPS | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |
| Guideline (standard specs) | `prompt/templates/consultant/standards/guideline_standard_specs.md` |
| Template (standard specs) | `prompt/templates/consultant/standards/template_standard_specs.md` |
| T104 Directory Convention (DEC006 source) | `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` |

---

## XVII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-20 | Initial | Promotion contract authored: 14-gap cross-review resolved; CLAUSE-030 normative text (CLAUSE-018B/020A format); ADR-003 body (CLAUSE-025A/025G format); corrected ADR Index (CLAUSE-023A/023D compliance); complete External References table (8 T102-scoped IDs); CLAUSE-015A variance; alias window terms; supersession notice; guideline revision corrections. Source: `notes_P-PH000-ST001-AC002-SES002.md` |
