---
artifact_type: 'COMMUNICATION'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2'
feature_code: 'SCHEMA'
version: '1.0.0'
date: '2025-11-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_role: 'LLM_Developer'
---

# DEVELOPER HANDOFF BRIEF: T810A2-SCHEMA F-RID Normalization & Refactor

## I. PURPOSE & SCOPE

- **Goal**: Align all `T810A2` F-RIDs (ASSUM/DEP/NFR/IF/CON/IG/INT/NOTE/RES) and their content with `T102-ADR-005` and the latest consultancy decisions, without changing client-approved meaning.
- **Artifacts in Scope**:
  - `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A2/proposal_T810A2-SCHEMA_phase1.md`
  - (Forward-looking) `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md` when drafted; mirror same F-RID structure and content.
- **Out of Scope**: Epic-level `T810A` artifacts (SPS, Concept, T810A1 Request) except where references need to be updated purely for ID consistency.

## II. GOVERNING RULES & ASSUMPTIONS

1. **ID Pattern & Scope**
   - Treat `T810A2-{CATEGORY}-{NNN}` (e.g., `T810A2-NFR-001`) as the **canonical F-RID shape** per updated `T102-ADR-005` (no `-SCHEMA` suffix in the scope ID).
   - Do not change existing ID tokens unless strictly necessary for de-duplication or deprecated-item annotation.

2. **Category Roles (per T102-ADR-005 + client decisions)**
   - `ASSUM`: Unverified beliefs shaping design (no hard SHALL rules).
   - `DEP`: External prerequisites (Epic decisions, research, platform).
   - `NFR`: High-level quality attributes only; **no implementation “how”**; may reference IG.
   - `IF`: Interfaces and contracts (data structures, direction of flow, error semantics).
   - `CON`: Non-negotiable boundaries; minimal overlap with IG and NOTE.
   - `IG`: Implementation guidance — the **“how”** for NFR/IF/CON; high-level but normative.
   - `INT`: Cross-feature integration notes; **bottom-up** suggestions for Epic governance, not Story-level specs.
   - `NOTE`: Non-normative contextual notes, often direct client language; keep content intact.
   - `RES`: Commissioned research.

3. **Directionality**
   - Feature F-RIDs may reference Epic/Initiative RIDs and DRs.
   - INT items are explicitly allowed to reference other Feature F-RIDs (e.g., `T810A1-*`, `T810A3-*`) per the INT governance exception (see section III.F).

4. **Client Constraints**
   - NOTE items are considered **raw client extracts**; do not change their wording except for minor typos.
   - NFRs must stay high-level and reference IGs for implementation details where needed.

## III. REQUIRED CHANGES BY CATEGORY

### A. ASSUM & CON (Assumptions vs Constraints)

**Objective**: Cleanly separate beliefs (`ASSUM`) from hard rules (`CON`), while preserving meaning.

1. `T810A2-ASSUM-006 (English-Only Operation)`
   - **Action**: Keep as ASSUMPTION (MVP scope belief). Add explicit reference to the relevant constraint/IG items rather than embedding scope rules here.
   - **Edit**:
     - Keep the “designed for English-language operation / multilingual deferred” wording.
     - Add a short final clause: “See `T810A2-CON-00X` / `T810A2-IG-00X` for the authoritative scope rule” once those IDs are confirmed.

2. `T810A2-ASSUM-007 (Manual Workflow Reliability)` vs `T810A2-CON-004 (Manual Profile Management)`
   - **Issue**: ASSUM-007 mixes patient capability assumptions with hard constraints on Stable vs Dynamic JSON.
   - **Action**:
     - In ASSUM-007, keep only the **belief** that patients can reliably perform manual JSON compilation and export.
     - Move any “Stable JSON is manually managed by patient ONLY; Dynamic JSON is LLM-generated…” text to `T810A2-CON-004` and/or `T810A2-IG-004/007` as appropriate.
   - **Edit**:
     - Trim ASSUM-007 to ~2–3 sentences about patient behavior; append references to `CON-004` and `IG-004/007` for implementation details.
     - Ensure `CON-004` holds the single authoritative statement about manual profile management and read-only access.

3. `T810A2-CON-001`–`CON-005`
   - **Action**: Keep category and semantics; minimize duplication by:
     - Ensuring CON items state the **boundary** (e.g., “keys SHALL be fixed for MVP”) in 1–2 sentences.
     - Moving explanatory rationale and workflows into IG items (see section III.E).

### B. NFR (Non-Functional Requirements)

**Objective**: Ensure NFRs describe **qualities** and defer specifics to IGs.

1. `T810A2-NFR-001 (Token Efficiency)`
   - **Action**: Keep as-is; this is a pure quality attribute.
   - Optionally reference an IG (future) if you want a single home for token-budget arithmetic or validation checks; not mandatory.

2. `T810A2-NFR-002 (Schema Clarity)`
   - **Current**: Now references `T810A2-IG-002 (YAML Template Format)` inline, plus residual bullets.
   - **Action**:
     - Reduce NFR-002 body to:
       - A single SHALL statement about self-documenting templates (dual-purpose: schema + instructions).
       - A reference to `T810A2-IG-002` for concrete template format and annotation rules.
     - Remove any remaining duplicate bullet lists already codified under IG-002.

3. `T810A2-NFR-003`–`NFR-005`
   - **NFR-003 (Vocabulary Completeness)**: No structural change; ensure it references `IG-003` for documentation patterns.
   - **NFR-004 (Clinical Validity)**: Keep as quality goal; add explicit link to `IG-003` and Epic ADR-002 for how this is implemented.
   - **NFR-005 (Schema Maintainance)**:
     - Ensure the “how” of schema evolution lives in `T810A2-IG-006` and `T810A2-CON-005`.
     - NFR-005 should state the maintainability goal (supporting change with minimal rework) and reference those IG/CON items.

### C. IF (Interfaces)

**Objective**: Keep interfaces focused on **contracts**, not template authoring rules.

1. `T810A2-IF-001`
   - No change beyond verifying references to updated IG items if needed.

2. `T810A2-IF-002 (Dynamic JSON Interface)`
   - **Current**: Contains both interface contract (entry types, key rules) and template-format guidance (YAML vs JSON, annotation density, token bounds).
   - **Action**:
     - Keep only contract-related content:
       - Entry type schemas, key naming conventions.
       - Single-entry generation pattern.
       - Handling of missing mandatory fields at the interface level (null/omission).
     - Replace repeated format bullets with a concise reference to `T810A2-IG-002` for **internal template format** and `T810A2-IG-007` for **export format**.

3. `T810A2-IF-003` / `T810A2-IF-004`
   - **Action**:
     - Keep them as interface definitions.
     - Ensure any detailed vocabulary documentation patterns are referenced to `IG-003`.
     - Confirm that mandatory/optional field classification rules primarily live in `T810A2-IG-005`, while IF-004 describes the contract-level view.

### D. NOTE & RES

**Objective**: Keep notes contextual and non-authoritative, preserving client voice.

1. `T810A2-NOTE-001`–`NOTE-004`
   - **Action**:
     - Do not change wording, except minor typo fixes if absolutely necessary.
     - Ensure any normative behavior described in NOTE-003/NOTE-004 is now **also** encoded in the relevant IG/CON items:
       - NOTE-003 → `T810A2-IG-001` (null-before-Probe).
       - NOTE-004 → `T810A2-IG-006` / `T810A2-CON-005` (schema evolution).
     - Where appropriate, add short cross-references from NOTE items back to those IG/CON F-RIDs, without altering the original client language.

2. `T810A2-RES-001`
   - No category change. Ensure all IG/INT items that claim to be “per RES-001” actually match its described deliverables and naming.

### E. IG (Implementation Guidance)

**Objective**: Make IG items the **single authoritative source** for “how” details, each aligned to one or more NFR/IF/CON/INT.

1. `T810A2-IG-001 (Null-Before-Probe Pattern)`
   - **Content Check**:
     - Correctly describes explicit `null` semantics, JSON representation, and annotation phrasing.
     - Aligns with the decision to treat null-before-Probe as IG (implementation of `T810A-QG-008`).
   - **Actions**:
     - Ensure references from `NFR-003`, `NOTE-003`, and `INT-001` point here for the behavior details.
     - Keep the title concise (already is).

2. `T810A2-IG-002 (YAML Template Format)`
   - **Content Check**:
     - Holds all detailed template format decisions (YAML internal, JSON output, annotation density, phrasing, token budget).
     - Correctly referenced from `NFR-002` and `IF-002`.
   - **Actions**:
     - Confirm no duplicate bullet lists remain in NFR/IF sections.
     - Optionally add a short “Relation” line at the end linking to `T810A2-NFR-002` and `T810A2-IF-002`.

3. `T810A2-IG-003 (Vocabulary Documentation Standard)`
   - **Actions**:
     - Keep table layout and hybrid placement strategy here.
     - Ensure `NFR-003`, `NFR-004`, `IF-003`, and `IG-006` reference this instead of restating vocabulary table rules.

4. `T810A2-IG-004 / IG-007 (Manual Workflow Guidance / Manual Export Workflow)`
   - **Goal**: Consolidate into a **single F-RID** (no deprecated IG records).
   - **Actions**:
     - Use `T810A2-IG-004` as the **canonical ID** for manual export workflow and patient JSON compilation guidance.
     - Merge all normative content currently under `T810A2-IG-007` into the body of `T810A2-IG-004`:
       - JSON-only export (not YAML), chronological array structure, dual-purpose use (Cara Care + T810A3), file naming conventions, step-by-step patient instructions.
     - Remove `T810A2-IG-007` as a standalone F-RID definition from the proposal:
       - Delete its dedicated subsection, and
       - Update all references (`INT-002`, traceability tables, NOTES, etc.) to point to `T810A2-IG-004` instead.
     - Update the F-RID summary table so the IG row and total count reflect the consolidated set (IG-001 through IG-006 only, unless new IGs are added later).

5. `T810A2-IG-005 (Field Classification Pattern)`
   - **Actions**:
     - Ensure this IG describes **how** mandatory/optional classification is constructed, leaving contract-level statements in `IF-004` and integration patterns in `INT-001`.
     - Confirm references to `T810A2-S08` for detailed lists are correct and stable.

6. `T810A2-IG-006 (Schema Evolution Guidance)`
   - **Actions**:
     - Make IG-006 the central “how” for schema evolution (keys vs values, external catalog usage, additive evolution).
     - Ensure that `NFR-005`, `CON-005`, `NOTE-004`, and `INT-005` reference IG-006 rather than duplicating the rules.

7. IG Traceability Block
   - **Actions**:
     - Update the IG traceability bullets to match the final set of IG items and their upstream dependencies (IG-001 through IG-006), with all manual-workflow references pointing to `T810A2-IG-004`.

### F. INT (Integration Notes)

**Objective**: Keep INT items as **suggestive, bottom-up integration patterns** that inform Epic-level governance, per the governance exception.

1. Header Block (INT CATEGORY GOVERNANCE)
   - **Content Check**:
     - Accurately describes bottom-up influence, cross-feature F-RID references, and non-prescriptive status.
     - **Actions**:
       - Ensure language stays descriptive (no SHALL on feature behavior).
       - Confirm it references `T102-ADR-005` only implicitly via ID usage, not by redefining ID rules.
       - Preserve the documented **INT governance exception** (bottom-up influence + cross-feature F-RID references) exactly as written; do not tighten it into a general rule for other categories.

2. `T810A2-INT-001`–`INT-005`
   - **Actions**:
     - Scan each INT body for any hidden “SHALL” language that applies directly to T810A2 behavior; rephrase such statements into suggestive language (e.g., “pattern is”, “enables”, “suggests”) unless the rule is already codified elsewhere (IG/CON).
     - Ensure INT-002 only covers aggregation format (chronological array for T810A3 + Cara Care alignment) and not manual export steps (those belong to `IG-007`).
     - Confirm each INT item:
       - References the appropriate upstream Epic RIDs and `T810A2` IG/IF/CON items.
       - Does not introduce new Story-level acceptance criteria; Story details should live in S06/S08, not in INT.

3. INT Traceability Block
     - **Actions**:
       - Verify that all cross-feature references (`T810A1-*`, `T810A3-*`) are up to date and that every referenced F-RID actually exists.
       - Ensure that any references that previously pointed to `T810A2-IG-007` now point to the merged `T810A2-IG-004`.

### G. Epic ADR T810A-ADR-002 (Foundational Vocabulary Authority)

**Objective**: Ensure the proposed Epic ADR in Section XI of the proposal conforms to `T102-ADR-004` and cleanly reflects T810A2’s completed F-RID set.

1. **DR Index Row**
   - Verify the index row under “Epic ADR Index Entry (Proposed)” matches `T102-ADR-004-FR-001`:
     - Columns: `ADR ID | Title | Status | Owner | Effective | Supersedes | Anchor`.
     - Values:
       - ID: `T810A-ADR-002`
       - Title: `Foundational Vocabulary Authority`
       - Status: `Proposed`
       - Owner: `Client`
       - Effective: `TBD`
       - Supersedes: `—`
       - Anchor: `#t810a-adr-002-vocabulary-authority`

2. **ADR Body Heading Format**
   - Update the body heading to follow `T102-ADR-004-FR-002` exactly:
     - Current: `* **T810A-ADR-002 (Foundational Vocabulary Authority)** {#t810a-adr-002-vocabulary-authority}`
     - Target:  `* **T810A-ADR-002 (Foundational Vocabulary Authority) — {#t810a-adr-002-vocabulary-authority}**`
   - Keep the anchor value unchanged to preserve anchor stability.

3. **Body Structure & Content**
   - Confirm the ADR body contains the required subheadings in this order:
     - **Context:** (already starts with `Per T810A-GDR-002`, which satisfies FR-005 cross-linking).
     - **Decision:**
     - **Specification:** with sub-FRs `T810A-ADR-002-FR-001` through `FR-006` as currently drafted.
     - **Consequences:**
     - **Alternatives Considered:**
     - **References:**
     - **Provenance:**
   - Do not change the semantics of the Specification items; they already incorporate T810A2’s vocabulary-related F-RIDs correctly.

4. **No Feature-Level ADRs/GDRs in This Pass**
   - Do **not** introduce new `T810A2-ADR-*` or `T810A2-GDR-*` records at this time.
   - Rationale:
     - Cross-feature vocabulary authority and schema requirements are already captured at Epic level in `T810A-ADR-002` and related Epic GDRs/ADRs.
     - T810A2-specific “how” decisions are now encoded in IG items, with `T810A2-RES-001` as provenance.
   - Future option (for consultants, not developers in this pass): If T810A2 later makes major architecture choices that are **only** local to this feature and require lifecycle tracking (separate from Epic changes), those can be promoted into `T810A2-ADR-00X` with:
     - Context citing `T810A-ADR-002` and other Epic GDRs/ADRs, and
     - Specification referencing the existing IG F-RIDs (rather than duplicating them).

## IV. IMPLEMENTATION STEPS (SEQUENCE)

1. **Normalize IG/INT Structure (Proposal File)**
   - Apply the edits described in III.E and III.F to `proposal_T810A2-SCHEMA_phase1.md`, ensuring:
     - Each NFR/IF references IG items instead of duplicating them.
     - Manual export and compilation guidance is consolidated under a single F-RID `T810A2-IG-004` (no deprecated IG IDs).
     - INT items are suggestive and cross-feature references are valid.

2. **Clean Up ASSUM/CON/NOTE Overlaps**
   - Refactor ASSUM-007 and CON-004 per III.A.
   - Add cross-references between NOTE items and their authoritative IG/CON counterparts without changing NOTE wording.

3. **Align Traceability Tables**
   - Update:
     - F-RID count and category summary table.
     - Epic→Feature traceability section.
     - Client directive→F-RID traceability.
   - Ensure they all point to the centralized IG items as the “how” references.

4. **Propagate Patterns to T810A2 Request (When Authored)**
   - When drafting `request_T810A2-SCHEMA.md`, mirror:
     - The same F-RID definitions (IDs, category assignments, and short descriptions).
     - The same references to IG/INT items.
   - Keep proposal and request in sync via a simple check-list.

5. **Optional: Epic-Level References Check**
   - Lightly scan `concept_T810-GASTRO.md` and any Epic ADRs that reference `T810A2-*`:
     - Confirm they reference the correct, current F-RIDs (especially IG-007, IG-006).
     - Do not introduce new Epic→Feature dependencies; only maintain existing references.

## V. ACCEPTANCE CRITERIA (FOR THIS NORMALIZATION PASS)

- All `T810A2` F-RIDs in the proposal follow the updated ID pattern `T810A2-{CATEGORY}-{NNN}` with consistent titles and short descriptions.
- NFR and IF sections no longer embed detailed implementation rules; those are consolidated into applicable IG items.
- IG items (001–006) are the single authoritative source for:
  - Null-before-Probe behavior.
  - YAML/JSON template format and annotations.
  - Vocabulary documentation standards.
  - Manual export and compilation workflows.
  - Field classification patterns.
  - Schema evolution principles.
- INT items are suggestive integration patterns, reference cross-feature F-RIDs where needed, and do not directly impose Story-level obligations on T810A2.
- ASSUM, CON, NOTE items no longer mix categories; constraints and implementation behaviors are always backed by a matching CON/IG item.

---

## VI. OPEN POINTS FOR CONSULTANT CONFIRMATION (BEFORE CODING)

1. Confirm that consolidating manual export guidance under `T810A2-IG-004` (and removing `T810A2-IG-007` as a separate F-RID) matches your intent for having **no deprecated IG IDs**.
2. For `T810A2-NOTE-003` and `NOTE-004`, are you comfortable with adding cross-reference suffixes like “(implemented via `T810A2-IG-001` / `T810A2-IG-006` / `T810A2-CON-005`)” if needed, as long as the original sentences remain unchanged?
3. When the T810A2 Request is created, we will fully restate each F-RID there; confirm that the Proposal should remain the primary working draft and that the Request simply mirrors its final, approved F-RID set and wording.

---

## VII. GLOBAL GOVERNANCE UPDATES: T102-ADR-004 & T102-ADR-005

**Purpose**: Encode the agreed industry-standard workflows and INT governance exception directly into the global T102 standards so future features can reuse them.

**Target Artifact**: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`  
Sections: `T102-ADR-004 (Decision Records Index)` and `T102-ADR-005 (ID Specification & Rules)`

### A. T102-ADR-004 — Decision Promotion Workflow (RES → IG → ADR)

**Objective**: Add an explicit functional requirement describing when to move from research and IGs into formal GDR/ADRs, and how to use Feature vs Epic scope.

1. **Add New FR Under T102-ADR-004**
   - Insert a new item after the existing FR-012:
     - **ID**: `T102-ADR-004-FR-013 (Decision Promotion Workflow)`
     - **Suggested Text** (adapt wording to house style):
       - “**T102-ADR-004-FR-013 (Decision Promotion Workflow)** — Decision records SHOULD follow a staged lifecycle:
         1) **Research (RES)** — Use `RES` F-RIDs to commission and document evidence, options, and empirical findings for a specific scope (Initiative/Epic/Feature).
         2) **Implementation Guidance (IG)** — Encode candidate implementation patterns as `IG` F-RIDs at the appropriate scope (typically Feature); IGs MAY evolve as research is refined.
         3) **Decision Records (GDR/ADR)** — Promote stable, cross-cutting or long-lived patterns into formal GDR/ADR records when:
            - (a) The pattern affects multiple artifacts or features; or
            - (b) The pattern requires explicit governance (ownership, status, supersedes) beyond implementation detail.
         4) **Traceability** — ADR Specifications SHOULD reference governing `RES` and `IG` F-RIDs in **Provenance** and **References**, rather than duplicating detailed patterns.”

2. **Scope Guidance (Epic vs Feature ADRs)**
   - Extend the text of FR-013 (or add a sub-bullet) to clarify scope:
     - “Epic-level ADRs SHOULD be used for cross-feature decisions (e.g., shared vocabularies, common JSON architectures).  
        Feature-level ADRs SHOULD be reserved for significant, feature-local architectural decisions that cannot be reasonably governed at Epic scope.  
        Routine implementation details MAY remain in IG F-RIDs without a dedicated ADR.”

3. **No Immediate Changes to Existing T102 ADR Bodies**
   - This FR only defines the workflow; do not retroactively restructure existing T102 ADRs in this pass.

### B. T102-ADR-005 — INT Integration Exception (Dedicated FR)

**Objective**: Formalize the special behavior of `INT` F-RIDs: bottom-up, cross-feature, suggestive integration notes that may reference other features’ F-RIDs.

1. **Add New FR Under T102-ADR-005**
   - Insert a new item after `T102-ADR-005-FR-007`:
     - **ID**: `T102-ADR-005-FR-008 (INT Integration Exception)`
     - **Suggested Text**:
       - “**T102-ADR-005-FR-008 (INT Integration Exception)** — At Feature scope, `INT` (Integration) F-RIDs have a specialized role:
         - **Bottom-Up Influence**: Feature-level INT items operate primarily as bottom-up integration proposals feeding higher-scope governance (Epic GDRs/ADRs/IGs). They are not direct implementation specifications for Story behavior.
         - **Cross-Feature References Permitted**: INT F-RIDs MAY reference other Feature F-RIDs directly (e.g., `T810A1-NFR-009`, `T810A3-*`) when used as integration design notes for Epic coordination. This is a scoped exception to the general upstream-only directionality rule in `T102-ADR-005-FR-003`.
         - **Suggestive, Not Prescriptive**: INT items SHOULD describe ideal integration patterns (e.g., data flow, sequencing, dependency patterns) and SHOULD avoid embedding Story-level acceptance criteria or strict SHALL requirements. Prescriptive behavior MUST be expressed in higher-scope GDR/ADRs or in Feature-level `CON`/`IG` F-RIDs.
         - **Governance Loop**: Epic consultants SHOULD review INT items when evolving Epic-level E-RIDs/E-ADRs/E-GDRs and, once decisions are adopted, affected INT items SHOULD be updated to reference the new governance rather than acting as standalone sources of truth.”

2. **Align With FR-003 (Precedence & Directionality)**
   - Add a short note to the narrative text under FR-003 (not a new ID) to cross-reference FR-008:
     - Example: “For the scoped exception related to Feature-level INT items, see `T102-ADR-005-FR-008 (INT Integration Exception)`.”

3. **No Changes to Other Categories**
   - Ensure that the exception is clearly limited to `INT` at Feature scope; other categories (`ASSUM`, `CON`, `NFR`, `IF`, `IG`, etc.) remain governed strictly by FR-003.

### C. Developer Implementation Notes (T102 Concept File)

1. Apply the FR additions and narrative tweaks only in `concept_T102-CONSULTANT.md` under the existing T102-ADR-004 and T102-ADR-005 sections; do not create separate files.
2. Keep anchors and existing ADR IDs stable; new FRs are list items within the ADR body, not new ADRs.
3. Use existing formatting conventions from the T102 Concept (Markdown bullet and heading styles).

