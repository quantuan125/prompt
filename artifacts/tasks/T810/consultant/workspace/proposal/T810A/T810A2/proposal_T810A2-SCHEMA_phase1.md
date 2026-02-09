---
artifact_type: 'PROPOSAL'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2'
feature_code: 'SCHEMA'
version: '1.0.0'
date: '2025-10-19'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_document: 'request_T810A2-SCHEMA.md'
target_section: 'Section III.E - III.I (Foundational Requirements)'
governance_guide: '../workspace_documentation_rules.md'
completion_log: '../../completion/T810A/T810A2/completion_T810A2-SCHEMA.md'
---

# PROPOSAL: T810A2-SCHEMA Phase 1 Foundational Requirements (F-RIDs)

## I. EXECUTIVE SUMMARY

**Purpose**: This proposal defines the foundational requirements (F-RIDs) for T810A2-SCHEMA (Patient Data Structures) by translating epic-level governance (E-RIDs/E-GDRs) into feature-specific specifications for Sections III.E through III.I of the Request document.

**Scope**: Phase 1 of the T810A2-SCHEMA consultancy process per `plan_T810A2-SCHEMA_phase0-4.md`.

**Key Deliverables**:
1. **Inherited Considerations Table** (Section III.E) — Explicit references to governing E-RIDs and E-GDRs
2. **Feature Assumptions** (Section III.E) — T810A2-specific assumptions delta
3. **Feature Dependencies** (Section III.E) — T810A2-specific dependencies delta
4. **Non-Functional Requirements** (Section III.F) — T810A2-NFR-### items
5. **Interfaces & Data** (Section III.G) — T810A2-IF-### items
6. **Constraints** (Section III.H) — T810A2-CON-### items
7. **Feature Integration Notes** (Section III.I) — T810A2-INT-### items

**Consultation Approach**: Delta-only F-RID proposal following T102-STD-003 (Explicit Inheritance Model). T810A2 inherits all E-RIDs/E-GDRs from T810A Epic; this proposal specifies only feature-specific expansions and deltas.

**Traceability Foundation**: All F-RIDs traceable to:
- **Handoff Brief v1.0.0**: `handoff_brief_T810A2-PATIENT_v1.0.0.md`
- **Epic SPS**: `sps_T810-GASTRO.md` (28 E-RIDs/E-GDRs)
- **T810A1 Request**: `request_T810A1-PROMPT.md` (integration dependencies)
- **Client Directives**: Cara Care exemplar, foundational JSON requirements

**Document Governance**:
- Rules for Plan/Proposal/Completion: `prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md`
- Execution notes (per-activity): `prompt/artifacts/tasks/T810/consultant/workspace/completion/T810A/T810A2/completion_T810A2-SCHEMA.md`

---

## II. INHERITED CONSIDERATIONS TABLE (Section III.E) — FINALIZED

**STATUS**: ✅ **FINALIZED** — IC Table validated at Checkpoint 1 per Activity 1.10 holistic analysis (see `analysis_T810A2-SCHEMA_checkpoint1.md` Section V for validation findings).

**Finalization Methodology**:
1. **Activities 1.1-1.8**: Developed detailed T810A2 F-RIDs with Epic governance references
2. **Activity 1.10**: Systematic E-RID reference scan across all proposal sections
3. **Finalization Rule Applied**: Included E-RIDs referenced in T810A2 F-RIDs; excluded unreferenced E-RIDs
4. **Validation**: Architecture row added (E-ADRs), IG-006 added, T810A1 row removed per governance rules

**Per T102-STD-003-FR-001 (Table Contracts):**

| Source Artifact | Source ID | Category | Inherited Rule IDs |
|:----------------|:----------|:---------|:-------------------|
| SPS | `T810A` | Research | `T810A-RES-001 (System Architecture & Clinical Validation)`, `T810A-RES-002 (Conversation-Driven Empirical Validation)` |
| SPS | `T810A` | Governance | `T810A-GDR-001 (Trust-and-Verify Workflow Standard)`, `T810A-GDR-002 (Schema Split Architecture)`, `T810A-GDR-003 (Dual-Purpose Clinical Reporting)`, `T810A-GDR-004 (GI Knowledge Base Sources)` |
| CONCEPT | `T810A` | Architecture | `T810A-ADR-001 (Trust-and-Verify Confidence Policy)`, `T810A-ADR-002 (Foundational Vocabulary Authority)` [PROPOSED], `T810A-ADR-003 (Dual-Purpose Reporting Policy)`, `T810A-ADR-004 (GI Knowledge Sources Catalog)` |
| SPS | `T810A` | Quality Goals | `T810A-QG-005 (Architecture Maintainability)`, `T810A-QG-006 (Patient Usability)`, `T810A-QG-007 (Confidence Communication)`, `T810A-QG-008 (Clarification Over Guessing)` |
| SPS | `T810A` | Dependencies | `T810A-DEP-001 (Platform Capability)`, `T810A-DEP-002 (Long-term Analysis)`, `T810A-DEP-004 (Patient Data Structures)`, `T810A-DEP-005 (Clinical Safety Framework)` |
| SPS | `T810A` | Assumptions | `T810A-ASSUM-002 (Input Modality & Quality)`, `T810A-ASSUM-003 (LLM Capability)`, `T810A-ASSUM-004 (Platform Memory Uncertainty)` |
| SPS | `T810A` | Constraints | `T810A-CON-001 (System Prompt Scope)`, `T810A-CON-002 (Platform Compatibility)`, `T810A-CON-004 (ChatGPT Architectural Constraints)` |
| SPS | `T810A` | Implementation Guidance | `T810A-IG-002 (Probe Phase Enforcement)`, `T810A-IG-003 (Explicit Classification)`, `T810A-IG-004 (Dynamic JSON Single-Entry)`, `T810A-IG-005 (Memory Review Protocol)`, `T810A-IG-006 (Session Context Handoff)` |

**Changes from Working Draft**:
1. ✅ **Architecture Row ADDED**: 4 E-ADRs included (ADR-001, ADR-002 [PROPOSED], ADR-003, ADR-004)
2. ✅ **IG-006 ADDED**: Session Context Handoff added to Implementation Guidance row
3. ✅ **DEP-002, DEP-005 ADDED**: Long-term Analysis and Clinical Safety Framework dependencies added
4. ✅ **T810A1 Feature Row REMOVED**: Direct cross-feature F-RID references eliminated per T102-STD-003 governance rules

---

## III. PROPOSED FEATURE ASSUMPTIONS (Section III.E - Delta)

**Delta-Only Additions** (no duplication of E-ASSUM items):

* **T810A2-ASSUM-001 (Schema Complexity Balance)** — Structured objects with metadata (≤2 levels deep per `T810A2-CON-001`) can be generated reliably by LLM_Gastro within ChatGPT JSON constraints. Drift (malformed JSON, incorrect nesting) occurs infrequently enough for MVP acceptance. Drift prevention achieved through: 
(1) Simple `T810A2` schema design with HYBRID annotations in ChatGPT Project Knowledge templates, 
(2) T810A1-S05 tracking protocol prompt engineering. Integration coordination detailed in `T810A2-INT-001`.

* **T810A2-ASSUM-002 (Controlled Vocabulary Completeness)** — Cara Care application exemplar provides complete vocabulary coverage per `T810A2-ADR-002`. For MVP, predefined schemas suffice for patient tracking needs without requiring runtime flexible key addition. Schema completeness enables reliable Cara Care dual processing and cross-session LLM communication via manual JSON handoff.

* **T810A2-ASSUM-003 (Template Self-Documentation Sufficiency)** — HYBRID annotation approach (minimal inline hints for complex fields) provides sufficient guidance for LLM_Gastro JSON generation without external documentation or programmatic schema enforcement. If testing reveals annotation insufficiency, contingency is hybrid of: 
  (1) iterate annotation density, 
  (2) accept inconsistency and rely on Probe phase gap-filling. 
Deferred to post-MVP for extensive validation.

* **T810A2-ASSUM-004 (Numeric Scale Interpretability)** — LLM_Gastro can reliably map natural language patient input to numeric scales using semantic anchor labels defined in `T810A2` controlled vocabularies. When input is ambiguous or outside scale range, LLM defaults to Probe phase clarification per `T810A-QG-008` rather than guessing scale value. Probe phase dialogue resolves ambiguity before populating scale field.

* **T810A2-ASSUM-005 (Vocabulary Familiarity)** — Patients using LLM_Gastro recognize Cara Care-aligned vocabulary patterns without requiring extensive explanation. HYBRID template annotations provide minimal contextual hints, but patient familiarity with tracking terminology is assumed. If patients use non-Cara Care terms, Probe phase maps to nearest valid controlled vocabulary value.

* **T810A2-ASSUM-006 (English-Only Operation)** — `T810A2` schemas, controlled vocabularies, and semantic scale labels are designed for English-language operation. Multi-language support (vocabulary translations, scale label localization, internationalization) is deferred beyond MVP scope. ChatGPT's multilingual LLM capabilities may enable some cross-language functionality, but schema design assumes English as primary language.

* **T810A2-ASSUM-007 (Manual Workflow Reliability)** — Patients can reliably perform manual JSON compilation/export workflow: copy Dynamic JSON codeblocks from LLM_Gastro session → save to file → upload to Project Knowledge for future sessions or enter into Cara Care app. Manual workflow friction (multi-step process, potential copy errors) is acceptable for MVP. See `T810A2-CON-004` and `T810A2-IG-004` for authoritative implementation rules.

**Traceability**:
- ASSUM-001: Client directive C1 (drift prevention strategy), T810A-CON-004, Handoff Brief Section III-D
- ASSUM-002: Client directive C2 (NO flexible keys MVP), Section III.G foundational table, Cara Care exemplar
- ASSUM-003: Client directive C3 (Option B+C hybrid contingency), T810A-CON-004
- ASSUM-004: Client directive C4 (Probe fallback approval), E-QG-008 reference, foundational JSON numeric scales
- ASSUM-005: Client directive C5 approval, Handoff Brief Section III-E (Cara Care UX familiarity)
- ASSUM-006: Client directive C5 approval (English-only scope)
- ASSUM-007: Client directive C3 (manual export architecture clarification), impacts INT-002, INT-003, Story S08

**Client Approval Required**: ☐ Feature assumptions accurately capture T810A2-specific beliefs shaping schema design approach

---

## IV. PROPOSED FEATURE DEPENDENCIES (Section III.E - Delta)

**Delta-Only Additions**:

* **T810A2-DEP-001 (Epic Integration Coordination)** — `T810A2` schema specifications fulfill `T810A-DEP-004` and must align with Epic governance (`T810A-GDR-002`, `T810A-IG-002/004/005` integration patterns). Misalignment blocks dependent features (`T810A1-PROMPT` for Dynamic JSON generation, `T810A3-REPORT` for aggregation/continuity). Coordination: Inter-feature integration governed by `T810A` Epic consultant through Epic GDR/ADR development and checkpoint validation. Technical integration details specified in `T810A2-INT` (external/cross-feature) and `T810A2-IG` (internal) category items.

* **T810A2-DEP-002 (Epic Deliverable Validation)** — `T810A2` deliverables  require `T810A` Epic consultant validation for Epic governance and architectural decisions compliance before implementation handoff.

* **T810A2-DEP-003 (Reporting Forward Compatibility)** — `T810A2` schema design should consider `T810A3-REPORT` (Reporting & Continuity: daily report format, aggregation, next-session context injection per `T810A-DEP-002`) forward compatibility. Considerations: JSON schema structure stability for cross-session aggregation, field naming consistency for pattern analysis, controlled vocabulary alignment across features, dual-format output compatibility (markdown narrative + structured JSON per `T810A-ADR-003-FR-006`). Approach: Lightweight Epic governance alignment (`T810A-GDR-003`, `T810A-ADR-003`, `T810A-IG-006`) without formal requirements research; accept calculated rework risk.

* **T810A2-DEP-004 (Research Resource Availability)** — `T810A2-RID` development and Story specifications may require LLM_Researcher commissioning for industry standards research, external validation, or technical feasibility studies beyond `T810A2` consultant expertise (e.g., template format selection, controlled vocabulary validation, JSON schema best practices, ChatGPT Project Knowledge compatibility).

* **T810A2-DEP-005 (Platform Capability)** — `T810A2` schema templates depend on ChatGPT Project Knowledge platform capabilities per `T810A-CON-002 (Platform Compatibility)`. **Platform Constraints** (per `T810A2-RES-001` Deliverable B.6):
  - **File Storage**: 25 files max (Plus), 512MB per file limit
  - **Token Limits**: 32k context window (GPT-4), ~2M tokens Project Knowledge processing upper bound per file
  - **Format Support**: JSON, YAML, Markdown natively supported (text-based; YAML chosen per `T810A2-RES-001` R2.1)
  - **Update Workflow**: Manual replace-only (no version control in UI; requires external governance per `T810A2-RES-001` R1.5)
  - **Performance**: Minimal retrieval latency for small files; no parsing overhead concerns

  Platform constraints validated against `T810A2-NFR-001 (Token Efficiency)` token budget recommendations per `T810A2-RES-001` R5; schema design stays well within limits. 

**Traceability**:
- DEP-001: T810A-DEP-004, T810A-GDR-002, T810A-IG-002/004/005, Handoff Brief v1.1.0
- DEP-002: T810A-ADR-001/002 (proposed)/003/004
- DEP-003: T810A-DEP-002, T810A-GDR-003, T810A-ADR-003, T810A-IG-006
- DEP-004: Plan Section II (LLM_Researcher role)
- DEP-005: T810A-CON-002, T810A2-NFR-001, T810A2-RES-001 R5

**Client Approval Required**: ☐ Feature dependencies accurately capture T810A2 external prerequisites, Epic coordination requirements, and foundational vocabulary governance

---

## V. PROPOSED NON-FUNCTIONAL REQUIREMENTS (Section III.F)

**F-RID Category: NFR (Non-Functional Requirements)**

* **T810A2-NFR-001 (Token Efficiency)** — Schema designs (Stable JSON patient profile + Dynamic JSON entry templates) SHALL optimize for minimal token consumption while maintaining field completeness per `T810A-RES-001`. **Platform-Informed Token Budget Recommendations**:
  - **System Prompt**: 1,500-2,000 tokens target (safe headroom for growth)
  - **Stable JSON Profile**: ≤ 1,000 tokens per patient (including history, chronic conditions, key preferences)
  - **Dynamic JSON Entry**: ≤ 250 tokens per entry (most 80-150 tokens; upper bound prevents unbounded free-text)
  - **Vocabulary Catalog**: 8,000-15,000 tokens total (Epic ADR-002 + T810A2 docs)

* **T810A2-NFR-002 (Schema Clarity)** — Templates SHALL be self-documenting for LLM_Gastro generation without external documentation or programmatic validation per `T810A-CON-004`. Dual purpose: schema definition + generation instructions. Template format, annotation density, and implementation patterns per `T810A2-IG-002`.

* **T810A2-NFR-003 (Vocabulary Completeness)** — ALL categorical fields SHALL have exhaustive controlled vocabulary specifications. "Completeness" applies to vocabulary DEFINITIONS (all possible values documented), not generation completeness (LLM may generate incomplete entries with null fields per `T810A-IG-002` and `T810A2-NOTE-003`).

* **T810A2-NFR-004 (Clinical Validity)** — Controlled vocabularies and field definitions SHALL align with clinically recognized standards and support pattern analysis use cases. Cara Care application is primary exemplar per `T810A2-CON-002` and `T810A-GDR-004`.

* **T810A2-NFR-005 (Schema Maintainance)** — Schema templates SHALL support future evolution with minimal rework per `T810A-QG-005`. New entry types can be added through `T810A2` governance updates without restructuring foundational schemas. Orthogonal to `T810A2-CON-005` runtime flexibility constraint per `T810A2-NOTE-004`.

**Traceability**:
- NFR-001: T810A-RES-001, T810A-QG-005, NOTE-002 (validation deferral)
- NFR-002: T810A-CON-004, NOTE-002 (format selection, validation deferral)
- NFR-003: T810A-QG-008, T810A-IG-002, CON-005, NOTE-003 (null handling)
- NFR-004: T810A-GDR-004, CON-002
- NFR-005: T810A-QG-005, NOTE-004 (orthogonality to CON-005)

**Client Approval Required**: ☐ Non-functional requirements accurately capture T810A2 quality attributes and constraints

---

## VI. PROPOSED INTERFACES & DATA (Section III.G)

**F-RID Category: IF (Interface Definitions)**

* **T810A2-IF-001 (Stable JSON Interface)** — Define Stable JSON interface contract: schema structure, field types/constraints, read-only access pattern, error states for missing/malformed profiles. Interface specifies WHAT data structures are loaded per `T810A-GDR-002`.

* **T810A2-IF-002 (Dynamic JSON Interface)** — Define Dynamic JSON interface contract: entry type schemas, structured key naming conventions, 100% schema-defined keys per `T810A2-CON-005` (no runtime flexible key addition for MVP). Single-entry generation pattern per `T810A-IG-004`; missing mandatory field handling via null values + Probe triggering per `T810A-IG-002`. Template format (internal YAML, export JSON) and annotation approach per `T810A2-IG-002`. Interface specifications: Entry type schemas per `T810A2-RES-001` Deliverable A.1, controlled vocabulary integration per `T810A2-IF-003`, field classification per `T810A2-IF-004`.

* **T810A2-IF-003 (Controlled Vocabulary Interface)** — Define controlled vocabulary interface contract: vocabularies per Epic `T810A-ADR-002` as authoritative source; LLM_Gastro accesses vocabularies via template-embedded references. Semantic scale mappings (numeric → descriptive labels) embedded inline for cross-feature consistency. Value set enforcement prompt-engineering based per `T810A-CON-004`. Vocabulary documentation patterns per `T810A2-IG-003`. 

* **T810A2-IF-004 (Field Classification Interface)** — Define mandatory/optional field classification interface: categorization principles per entry type enabling Probe phase triggering per `T810A-IG-002`. High-level mapping rules: 
(1) Timestamp fields mandatory for all entry types (clinical temporal analysis), 
(2) Mental state fields mandatory for patient_state (stress, mood pattern analysis), 
(3) Bristol type mandatory for stool (core classification per `T810A-ADR-004`), 
(4) Meal items mandatory for meal (trigger analysis), 
(5) Metadata fields optional (contextual enrichment). 

**Interface Responsibility Matrix**:

| Interface | T810A2 Defines | Epic Governs | Notes |
|:----------|:---------------|:-------------|:------|
| **IF-001** | Schema structure, field types, error states | Loading sequence (IG-005), precedence rules (GDR-002) | T810A2 = WHAT; Epic = WHEN |
| **IF-002** | Entry type schemas, key naming, generation rules | Single-entry pattern (IG-004), Epic vocabulary catalog (ADR-002) | Template format per `T810A2-RES-001` |
| **IF-003** | Controlled vocabularies, semantic scale mappings | Cross-feature vocabulary authority (ADR-002), enforcement principles (GDR-002) | Epic catalog authoritative |
| **IF-004** | Field categorization principles, high-level mapping rules | Probe enforcement (IG-002), minimum question count (≥2) | Exhaustive lists in Story S08 |

**Traceability**:
- IF-001: T810A-GDR-002, T810A-IG-005, Story S01
- IF-002: T810A-IG-004, T810A-IG-002, T810A2-CON-005, T810A2-RES-001, Stories S02-S06
- IF-003: T810A-ADR-002 (proposed), T810A-CON-004, Story S07
- IF-004: T810A-IG-002, T810A-ADR-004, Handoff Brief v1.1.0 Section V-C, Story S08

**Client Approval Required**: ☐ Interface definitions accurately capture T810A2 data exchange patterns (high-level contracts, no implementation details)

---

## VII. PROPOSED CONSTRAINTS (Section III.H)

**F-RID Category: CON (Constraints - Delta)**

* **T810A2-CON-001 (Schema Complexity)** — Schema nesting SHALL NOT exceed 2 levels per `T810A-GDR-002` to maintain LLM generation reliability per `T810A-CON-004`. Nested objects limited to 2 levels deep; metadata arrays with controlled vocabularies permitted. Exception handling deferred per client directive. 

* **T810A2-CON-002 (Vocabulary Authority)** — Controlled vocabularies SHALL follow Cara Care application patterns as primary authority per proposed `T810A-ADR-002` (Foundational Vocabulary Authority). External clinical standards (PHQ-9, GAD-7) deferred to post-MVP; Epic governance evolution triggers upgrade. 

* **T810A2-CON-003 (Specification-Based Validation)** — Schema validation SHALL be specification-based only per `T810A-CON-004`; no programmatic enforcement. `T810A2` defines exhaustive specifications; validation enforcement delegated to Epic governance per `T810A-GDR-002` . 

* **T810A2-CON-004 (Manual Profile Management)** — Stable JSON SHALL be read-only for LLM per `T810A-GDR-002` and `T810A-CON-004`, manually managed by patient ONLY. Dynamic JSON SHALL be LLM-generated per `T810A-IG-004` and manually compiled by patient. No automated backend compilation for MVP. Manual patient update workflow defined by `T810A2-IG-004`. 

* **T810A2-CON-005 (Fixed Schema Keys)** — Dynamic JSON keys SHALL be 100% T810A2-defined for MVP per `T810A-GDR-002`. Runtime flexible key addition prohibited; schema evolution via T810A2 governance updates only per Story S06. Stable JSON remains patient-managed per `T810A2-CON-004`. Simplifies template design, enables exhaustive vocabulary specification per `T810A2-NFR-003`, ensures Cara Care dual processing consistency. 

**Traceability**:
- CON-001: T810A-GDR-002, T810A-CON-004, Stories S01-S06
- CON-002: T810A-ADR-002 (proposed), Handoff Brief v1.1.0 Section III-E, Story S07
- CON-003: T810A-GDR-002, T810A-CON-004, Activity 3.4 (Epic coordination), Stories S01-S07
- CON-004: T810A-GDR-002, T810A-CON-004, T810A-IG-004, Story S01
- CON-005: T810A-GDR-002, NFR-003, INT-002, Stories S06/S07

**Client Approval Required**: ☐ Constraints accurately capture T810A2 non-negotiable boundaries (ultra-concise, Epic GDR primary references, no cross-feature F-RID citations)

---

## VIII. PROPOSED FEATURE IMPLEMENTATION & INTEGRATION

**F-RID Category: IG (Implementation Guidance)**

* **T810A2-IG-001 (Null-Before-Probe Pattern)** — LLM_Gastro SHALL default to explicit `null` values for ALL Dynamic JSON fields (mandatory + optional) when patient context insufficient, BEFORE Probe phase triggers per `T810A-IG-002` and `T810A-QG-008`. This enforces no-guessing requirement per `T810A2-NOTE-003`. **JSON Representation** (per `T810A2-RES-001` R6.1): Use explicit `null` keyword (not missing field omission) for unambiguous null state tracking. **Template Annotation Phrasing** (per `T810A2-RES-001` R3.3): Directive style — "If unknown, set to null and ask patient later." Probe phase fills mandatory field nulls in second pass after clarification. Prevents hallucination, enables reliable Probe-based gap-filling per `T810A2-NFR-003`. 

* **T810A2-IG-002 (YAML Template Format)** — Project Knowledge templates SHALL use **YAML format** with native `#` comments for HYBRID annotations per `T810A2-RES-001` R2.1. **Template Format Specification**:
  - **Internal Format**: YAML with native `#` comments for Project Knowledge storage (~30-50% token savings vs JSON per `T810A2-RES-001` B.1)
  - **Output Format**: JSON for runtime Stable/Dynamic JSON generation (interoperability with Cara Care dual processing, `T810A3` aggregation, `T810A-GDR-002` compliance per `T810A2-RES-001` R2.1)
  - **Annotation Density**: Minimal field-level annotation — 70-80% fields no comments, 20-30% short comments on complex/critical fields (qualitative guideline per `T810A2-NOTE-002` and `T810A2-RES-001` R3.1)
  - **Annotation Phrasing**: Short, directive style (e.g., "Allowed values: ...", "Default: null if unknown; probe if null" per `T810A2-RES-001` R3.3)
  - **Token Budget Compliance**: System+knowledge templates target ≤ 2,000 tokens combined per `T810A2-RES-001` R5.1

**Dual Responsibility Implementation** (per `T810A2-RES-001` R3.2): Each YAML template contains top-level comment block (purpose, Stable vs Dynamic, usage) + local comments at critical fields only (scales, controlled vocab, null behavior). Templates serve dual purpose: schema definition + LLM generation instructions per `T810A2-NFR-002`. Bridges `T810A2` schema design with `T810A1-S05` tracking protocol. 

* **T810A2-IG-003 (Vocabulary Documentation Standard)** — Controlled vocabulary specifications SHALL follow `T810A-ADR-002` extracted from `T810A2-RES-001` R6.3. 
  **Table Layout** (per `T810A2-RES-001` R1.5): Base standard on Cara Care-inspired formats from `T810A2-RES-001` Deliverable A (Bristol scale 0-7 with semantic labels, symptom severity scales 1-5 with endpoint descriptions, meal/stool metadata enumerated arrays). 
  **Hybrid Placement Strategy** (per `T810A2-RES-001` R4.1): Embed short critical lists (Bristol 0-7, small severity scales) directly in YAML templates for LLM generation clarity; externalize large/evolving lists (extended meal.metadata, stool.metadata, future entry type vocabularies) in `T810A-ADR-002` catalog + `controlled_vocabularies.md` for maintainability. 
  **Future Vocabulary Additions**: All expansions SHALL follow markdown table pattern with semantic anchors ensuring cross-feature consistency per `T810A-ADR-002`. Specification details in `T810A2-S07`

* **T810A2-IG-004 (Manual Workflow Guidance)** — Patients SHALL manually export Dynamic JSON as **`.json` files** (NOT YAML) for dual-purpose workflows per `T810A2-RES-001` R6.4: 
  (1) Manual Cara Care app entry (dual processing alignment per `T810A2-RES-001` C.2), 
  (2) Future session loading into Project Knowledge per `T810A-IG-006`, 
  (3) Optional `T810A3` aggregation input (post-MVP automated backend per `T810A-GDR-003`). 
  **Manual Compilation Workflow** (per `T810A2-INT-002`): Patient copies Dynamic JSON codeblocks from session → compiles into chronological array → saves file. 
  **File Naming Conventions**: Define standard naming pattern for session organization. 
  **Step-by-Step Patient Instructions**: Document export sequence, compilation rules, upload patterns. 
  **Format Rationale**: JSON output ensures Cara Care field/vocabulary recognition without friction; aggregation format enables `T810A3` forward compatibility with chronological JSON array structure per `T810A-ADR-003` enhancements. Specification details in Story `T810A2-S08`.

* **T810A2-IG-005 (Field Classification Pattern)** — Feature SHALL establish consistent mandatory/optional field categorization principles per entry type to enable Probe phase triggering per `T810A-IG-002`.  
  **High-Level Mapping Rules** (per `T810A2-IF-004`):
  - Timestamp fields mandatory for all entry types (clinical temporal analysis)
  - Entry-specific core fields mandatory (Bristol type for stool, meal items for meal, symptom severity for digestion/mental)
  - Metadata fields optional (contextual enrichment)
  - Context-dependent fields follow clinical necessity (confidence mandatory for image-based entries, optional for self-reported)
  **Categorization Approach**: Field classification SHALL balance clinical data completeness with conversation flow naturalness. Mandatory fields trigger Probe phase when null per `T810A2-IG-001`; optional fields enhance analysis but don't block workflow. Classification serves dual purpose: Probe triggering logic + LLM generation guidance. Specification details in `T810A2-S08` (exhaustive mandatory/optional lists per entry type, field-to-question-type mapping table).

* **T810A2-IG-006 (Schema Evolution Guidance)** — Schema templates SHALL support future evolution with minimal rework per `T810A-QG-005`.
  **Extensibility Principles** (per `T810A2-NFR-005` and `T810A2-RES-001` gap analysis):
  - **Additive Evolution**: New entry types can be added through `T810A2` governance updates without restructuring foundational schemas
  - **Vocabulary Expansion**: Controlled vocabularies use external catalog for large/evolving lists enabling value additions without template modification (per `T810A2-IG-003` hybrid placement)
  - **Field Additions**: Entry type schemas support new optional fields without breaking existing integrations (Cara Care dual processing, `T810A3` aggregation)
  - **Governance Pattern**: Schema changes follow `T810A2` feature update workflow; Epic `T810A-ADR-002` governs cross-feature vocabulary impacts

  **Evolution Constraints** (per `T810A2-CON-005` and `T810A2-NOTE-004`): MVP prohibits runtime flexible key addition; schema evolution is design-time governance-driven only. Future flexibility beyond MVP requires Epic governance amendment. Specification details in `T810A2-S06` (schema maintenance workflow, vocabulary expansion procedures).

**Traceability**:
- IG-001: `T810A-IG-002` (Probe Phase), `T810A-QG-008` (No Guessing), `T810A2-NFR-003`, `T810A2-NOTE-003`, `T810A2-RES-001` R6.1/R3.3, Stories `T810A2-S01`/`T810A2-S02`-`T810A2-S06`
- IG-002: `T810A-GDR-002` (Stable/Dynamic Split), `T810A-IG-004` (Single-Entry), `T810A2-NFR-002`, `T810A2-DEP-005`, `T810A2-IF-002`, `T810A2-NOTE-002`, `T810A2-RES-001` R2.1/R3.1-3.3/R5.1/R6.2/B.1, Stories `T810A2-S01`/`T810A2-S02`-`T810A2-S07`
- IG-003: `T810A-ADR-002` (Vocabulary Authority), `T810A-CON-004` (Specification-Based), `T810A2-CON-002`, `T810A2-IF-003`, `T810A2-DEP-005`, `T810A2-RES-001` R1.5/R4.1/R6.3/Deliverable A, Story `T810A2-S07`
- IG-004: `T810A-GDR-003` (Dual-Purpose Reporting), `T810A-IG-006` (Session Handoff), `T810A2-ASSUM-007`, `T810A2-INT-002`, `T810A2-IF-002`, `T810A2-RES-001` R6.4/C.2, Story `T810A2-S08`
- IG-005: `T810A-IG-002` (Probe Phase), `T810A2-IF-004`, `T810A2-IG-001`, `T810A2-RES-001` gap analysis, Story `T810A2-S08`
- IG-006: `T810A-QG-005` (Adaptability), `T810A2-NFR-005`, `T810A2-CON-005`, `T810A2-NOTE-004`, `T810A2-IG-003`, `T810A2-RES-001` gap analysis, Stories `T810A2-S06`/`T810A2-S07`

**Client Approval Required**: ☐ Implementation guidance accurately captures T810A2 high-level technical patterns for Story-level specification development

---

**F-RID Category: INT (Integration Notes)**

**INT CATEGORY GOVERNANCE**:

**Unique Role**: INT items inform Epic T810A governance for cross-feature coordination (BOTTOM-UP influence: Feature → Epic) vs. other F-RID categories' TOP-DOWN inheritance (Epic → Feature). INT serves as communication artifact to T810A Epic consultant for potential E-IG/E-ADR/E-GDR development.

**Cross-Feature F-RID References**: F-INT-RIDs MAY reference other features' F-RIDs directly (e.g., `T810A1-NFR-009`, `T810A1-INT-005`, `T810A3-*`) for Epic communication clarity. This is EXEMPT from cross-feature coupling prohibition applicable to other F-RID categories.

**Suggestive Patterns**: INT items propose high-level ideal integration patterns that T810A2 may have effects on other features. These are NOT prescriptive SHALL requirements; detailed implementation coordinated by Epic T810A consultant through E-RID governance.

**Flexibility**: INT items are subject to Epic coordination and multiple revisions. Changes to INT do NOT invalidate T810A2 Story specifications (Stories implement inherited Epic governance, not direct INT patterns).

**Scope Boundary**: INT does NOT inform T810A2 Story-level development directly; Stories reference Epic E-IGs/E-GDRs/E-ADRs enhanced via INT-driven coordination.

---

* **T810A2-INT-001 (Probe Triggering Integration)** — `T810A2` mandatory/optional field classification per entry type enables `T810A1-NFR-005 (Probe Phase Enforcement)` Probe triggering per `T810A-IG-002`. Missing mandatory fields suggest Probe phase activation (≥2 clarifying questions). High-level pattern: T810A2 field categorization → `T810A1-S05 (Execution Protocol)` triggering logic → `T810A-IG-002` potential enhancement for field-to-question mapping framework. Detailed field lists in `T810A2-S08`.

* **T810A2-INT-002 (Aggregation Format Integration)** — `T810A2` Dynamic JSON aggregation format supports `T810A3` cross-session pattern analysis and Cara Care dual processing per `T810A-GDR-003`. Chronological JSON array structure (timestamp-ordered entry objects) enables future aggregation without schema restructuring. Manual workflow guidance per `T810A2-IG-004`. Aggregation format specification retained for `T810A3` forward compatibility even though MVP uses manual patient workflow.

* **T810A2-INT-003 (Session Initialization Integration)** — T810A2 Stable JSON + Dynamic JSON skeleton templates support `T810A1-INT-005 (Memory Review Protocol)` session initialization sequence per `T810A-GDR-002`. Loading pattern: Step 0 Memory Review → Step 1 Stable JSON (read-only) + Dynamic JSON templates → `T810A1-S05` protocol execution. Suggests `T810A-IG-005` potential enhancement for standard initialization workflow.

* **T810A2-INT-004 (Conflict Resolution Integration)** — T810A2 Stable JSON precedence hierarchy informs `T810A1-INT-005 (Memory Review Protocol)` conflict detection when ChatGPT Memory conflicts with patient profile per `T810A-GDR-002`. Precedence: Stable JSON > Memory. High-level pattern: T810A2 field categorization → `T810A1` Probe phase clarification → patient updates Stable JSON manually. Suggests `T810A-IG-005` potential enhancement for standard conflict resolution phrasing.

* **T810A2-INT-005 (T810A3 Forward Compatibility)** — T810A2 schema evolution principles enable future `T810A3` requirements without rework per `T810A2-DEP-003`. Extensibility patterns: additive evolution (new entry types), vocabulary expansion (external catalog per `T810A-ADR-002`), field additions (optional fields), aggregation compatibility (chronological array structure per `T810A2-INT-002`). Schema evolution workflow in `T810A2-S06`.

**Traceability**:
- INT-001: `T810A1-NFR-009` (Probe Phase Enforcement), `T810A-IG-002` (Probe Phase), `T810A2-IF-004` (Field Classification), `T810A2-S08`, Handoff Brief v1.0.0 Section V-C
- INT-002: `T810A-GDR-003` (Dual-Purpose Reporting), `T810A2-IG-004` (Manual Workflow Guidance), `T810A2-RES-001` C.2 (Cara Care dual processing), `T810A3` Feature Register (proposed)
- INT-003: `T810A1-INT-005` (Memory Review Protocol), `T810A-GDR-002` (Stable/Dynamic JSON Architecture), `T810A-IG-005` (Memory Review), `T810A1-S05`, `T810A2-RES-001` B.6
- INT-004: `T810A1-INT-005` (Memory Review Protocol), `T810A-GDR-002` (Stable/Dynamic JSON Architecture), `T810A-IG-005` (Memory Review), `T810A2-CON-004`
- INT-005: `T810A2-DEP-003` (T810A3 Forward Compatibility), `T810A-ADR-002` (Vocabulary Authority), `T810A2-NFR-005`, `T810A2-IG-006`, `T810A2-INT-002`, `T810A2-S06`

**Flexibility Disclaimer**: All INT items subject to Epic coordination and multiple revisions. INT patterns are suggestive (not prescriptive SHALL requirements). Formal handoff brief to T810A Epic consultant at Checkpoint 1.

**Client Approval Required**: ☐ Integration notes accurately capture T810A2 cross-feature coordination patterns for Epic governance development

---

## IX. RESEARCH & NOTES PREVIEW (Section III.M)

**Purpose**: Document research needs and important client directives for eventual request Section III.M implementation.

**Research Needs** (for Activity 1.9 registration):

* **T810A2-RES-001 (Template & Vocabulary Research)** — Combined research scope executed in single research run with sequential execution order: (1) **Cara Care Vocabulary Extraction**: Systematic extraction of EXHAUSTIVE controlled vocabularies (meal metadata, stool descriptors, symptom scales with semantic anchor labels) from Cara Care application exemplar; evaluate Cara Care resources (screenshots, documentation, app access) for vocabulary completeness; deliverable: complete controlled vocabulary catalog for `T810A-ADR-002` (Foundational Vocabulary Authority) implementation with enumerated value sets for ALL categorical fields. (2) **Template Format Selection**: Investigate optimal template format (JSON with comment workarounds vs. YAML vs. JSONL) for ChatGPT Project Knowledge storage; research criteria: native comment support for HYBRID annotations, LLM_Gastro parsing reliability, token efficiency impact (informed by vocabulary extraction results), schema clarity per `T810A2-NFR-002`; evaluate against business requirements (Section III.A-III.D) and technical F-RIDs; deliverable: format recommendation with trade-off analysis for Story S01 template creation. Priority: CRITICAL (Phase 2 blocking — Stories S01-S07 depend on vocabulary catalog + template format decision). Execution: Post-Checkpoint 1 via LLM_Researcher.

**Notes** (consolidated client directives):

* **T810A2-NOTE-001 (Handoff Brief)** — Handoff brief from T810A consultant that initiate T810A2 feature development `handoff_brief_T810A2-SCHEMA.md`

* **T810A2-NOTE-002 (MVP Validation Approach)** — Template format selection and NFR validation criteria (token efficiency thresholds, self-documentation sufficiency, vocabulary exhaustiveness metrics) are QUALITATIVE for MVP per client directive. Quantitative validation deferred to post-MVP testing with empirical evidence. Story acceptance criteria use subjective validation (e.g., "Developer confirms template interpretability") with understanding that criteria will be refined after implementation testing. Template format decision deferred to `T810A2-RES-001` research; decision point at Story S01 based on ChatGPT Project Knowledge compatibility validation per `T810A-CON-004`.

* **T810A2-NOTE-003 (Null-Before-Probe Strategy)** — LLM_Gastro SHALL default to null values for ALL fields (mandatory + optional) when patient context is insufficient, BEFORE Probe phase triggers per `T810A-QG-008` and `T810A-IG-002`. This enforces no-guessing requirement more strictly than context-dependent approach. Probe phase THEN fills mandatory field nulls in second pass after patient clarification per `T810A2-INT-001`. Null default strategy prevents hallucination and enables reliable Probe phase gap-filling per `T810A2-NFR-003` and `T810A2-IG-001`.

* **T810A2-NOTE-004 (Schema Evolution Scope)** — "Flexible schema" (Story S06) refers to controlled vocabulary VALUE expansion, NOT key structure modification per client directive. `T810A2-CON-005` prohibits runtime key addition for MVP. New KEYS added only via `T810A2` governance-driven schema updates (Story S06 governance workflow). Flexibility applies to controlled vocabulary VALUES expansion within existing key structures, NOT runtime key structure modification. `T810A2-NFR-005` (design-time extensibility) is orthogonal to `T810A2-CON-005` (runtime flexibility prohibition). Schema evolution implementation guidance per `T810A2-IG-006`.

---

## X. F-RID SUMMARY & TRACEABILITY MATRIX

### A. F-RID Count by Category

| Category | Count | IDs |
|:---------|:------|:----|
| ASSUM | 7 | T810A2-ASSUM-001 through ASSUM-007 |
| DEP | 5 | T810A2-DEP-001 through DEP-005 |
| NFR | 5 | T810A2-NFR-001 through NFR-005 |
| IF | 4 | T810A2-IF-001 through IF-004 |
| CON | 5 | T810A2-CON-001 through CON-005 |
| IG | 7 | T810A2-IG-001 through IG-007 |
| INT | 5 | T810A2-INT-001 through INT-005 |
| NOTE | 4 | T810A2-NOTE-001 through NOTE-004 |
| RES | 1 | T810A2-RES-001 |
| **TOTAL** | **42** | **42 F-RIDs proposed** |

### B. Epic to Feature RID Traceability

| Epic RID | T810A2 F-RID Expansion | Expansion Type |
|:---------|:----------------------|:---------------|
| T810A-GDR-002 (Schema Split Architecture) | T810A2-IF-001, IF-002, INT-003, INT-004, CON-004 | **Primary expansion** — T810A2 fulfills this GDR |
| T810A-CON-004 (ChatGPT Architectural Constraints) | T810A2-CON-001, CON-003, CON-004, IF-003, NFR-002, NOTE-002 | **Constraint translation** — Platform constraints shape schema design |
| T810A-QG-005 (Architecture Maintainability) | T810A2-NFR-005 | **Quality goal inheritance** — Maintainability + extensibility |
| T810A-QG-008 (Clarification Over Guessing) | T810A2-NFR-003, NOTE-003 | **Quality goal application** — Null-before-Probe strategy |
| T810A-RES-001 (System Architecture & Clinical Validation) | T810A2-NFR-001, NFR-004 | **Research application** — Token efficiency + clinical validity |
| T810A-IG-002 (Probe Phase Enforcement) | T810A2-INT-001, NFR-003, NOTE-003 | **Implementation guidance application** — Probe triggering + null handling |
| T810A-IG-004 (Dynamic JSON Single-Entry) | T810A2-IF-002 | **Implementation guidance application** — Single-entry generation pattern |
| T810A-GDR-003 (Dual-Purpose Clinical Reporting) | T810A2-INT-002 | **Integration alignment** — Aggregation format serves dual purpose |
| T810A-GDR-004 (GI Knowledge Base Sources) | T810A2-NFR-004, CON-002 | **Quality goal application** — Clinical validity standards |

### C. Client Directive to F-RID Traceability

| Client Directive Source | F-RID Implementation |
|:------------------------|:---------------------|
| QA1-C1: Token efficiency optimization (all schemas, no hard caps) | NFR-001, NOTE-002 (validation deferral) |
| QA1-C2: Template format + validation deferral | NFR-002, NOTE-002, RES-005 |
| QA1-C3: Null default strategy + vocabulary completeness | NFR-003, NOTE-003, IG-001 |
| QA1-C4: Cara Care primary authority | NFR-004, CON-002 |
| QA1-C5: Design-time extensibility (orthogonal to CON-005) | NFR-005, NOTE-004 |
| QA-A1: Template format research (Option D) | RES-005 (CRITICAL priority) |
| QA-A2: Null-before-Probe (Option C prescriptive + context-dependent) | NOTE-003, IG-001 |
| QA-A3: Story S06 scope clarification | NOTE-004 |
| QA-A4: Qualitative validation for MVP | NOTE-002 |
| Handoff Brief v1.0.0 (Foundational JSON requirements) | ASSUM-002, ASSUM-004 |
| Handoff Brief v1.0.0 (Template-Driven Architecture) | NFR-002, ASSUM-003 |
| Handoff Brief v1.0.0 (Probe Triggering) | INT-001, IF-004 |

---

## XI. PROPOSED EPIC ARCHITECTURAL DECISION (T810A-ADR-002)

**Purpose**: T810A2 consultancy proposes `T810A-ADR-002` (Foundational Vocabulary Authority) for Epic T810A governance adoption to ensure cross-feature vocabulary consistency across T810A1/T810A2/T810A3.

**Approval Workflow**: This Epic ADR proposal will be submitted to `T810A` Epic consultant for independent analysis and Client approval per Epic governance procedures. If adopted, `T810A-ADR-002` will be added to Epic Concept document (`concept_T810-GASTRO.md` Section III.B.2.i Epic ADR Index).

**Rationale**: Foundational vocabulary table (Plan Section III.G) contains CLIENT-MANDATED controlled vocabularies (meal metadata, stool descriptors, numeric scale semantics) required for Cara Care dual-processing alignment per `T810A-CON-002` and cross-feature aggregation compatibility per `T810A-DEP-002`. Promoting to Epic ADR ensures T810A1/T810A3 inherit authoritative vocabularies and prevents feature-level drift.

---

### Epic ADR Index Entry (Proposed)

| ADR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| `T810A-ADR-002` | Foundational Vocabulary Authority | Proposed | Client | TBD | — | #t810a-adr-002-vocabulary-authority |

---

### Epic ADR Body Specification

* **T810A-ADR-002 (Foundational Vocabulary Authority) — {#t810a-adr-002-vocabulary-authority}**

  **Context:** Per `T810A-GDR-002`, Stable/Dynamic JSON architectures require controlled vocabularies for categorical fields. Without authoritative cross-feature vocabulary governance, features risk inconsistent terminology, aggregation incompatibility per `T810A-DEP-002`, and Cara Care dual-processing misalignment per `T810A-CON-002`. Research (`T810A-RES-001` Deliverable E) confirms Cara Care application as primary exemplar for GI tracking vocabulary patterns.

  **Decision:** Establish Foundational Vocabulary Authority defining authoritative controlled vocabularies for Epic features requiring patient tracking JSON structures. Vocabulary catalog governs meal/stool metadata, numeric scale semantics, and cross-feature consistency. Cara Care application serves as primary exemplar per `T810A-GDR-004` vocabulary authority model. Adopt `T810A-ADR-002`, defining foundational JSON requirements table as Epic governance.

  **Specification:**

   1) **T810A-ADR-002-FR-001 (Foundational JSON Requirements Table)** — Enhanced per `T810A2-RES-001` Deliverable A.5 gap analysis and client directive (Activity 1.9 QA)

      | Entry Type | Classification | Key | Data Type | Range/Values | Descriptions Required |
      |:-----------|:--------------|:----|:----------|:-------------|:----------------------|
      | **meal** | **REQUIRED** | `ingredients` | array | list of ingredient strings | Meal components |
      | **meal** | **REQUIRED** | `metadata` | array | ["chili", "oily", "sweet", "light", "salty", "fibrous"] | Descriptive tags (explicitly enumerate ALL per `T810A2-RES-001` R1.2) |
      | **stool** | **REQUIRED** | `type` | integer | 0-7 | Bristol scale descriptions for each (Type 0 = "nothing" per `T810A2-RES-001` A.1) |
      | **stool** | **REQUIRED** | `metadata` | array | ["urgent", "full_evacuation", "partial_evacuation", "mucus", **"blood"**] | Event descriptors (**"blood" added** per `T810A2-RES-001` A.5 clinical validity) |
      | **stool** | **REQUIRED** | `confidence` | float | 0.0-1.0 | LLM image analysis confidence |
      | **digestion** | **REQUIRED** | `tummy_pain` | integer | 1-5 | 1=no pain → 5=extreme; predefined descriptions per `T810A2-RES-001` R1.3 |
      | **digestion** | **REQUIRED** | `bloating` | integer | 1-5 | 1=no bloating → 5=extreme; predefined descriptions per `T810A2-RES-001` R1.3 |
      | **mental** | **REQUIRED** | `mood` | integer | -2 to 2 | -2=awful, 0=neutral (so-so), 2=very good (happy) per `T810A2-RES-001` R1.3 |
      | **mental** | **REQUIRED** | `stress` | integer | 1-5 | 1=no stress → 5=extreme stress per `T810A2-RES-001` R1.3 |
      | **sleep** | **OPTIONAL** | `duration` | string/enum | ["<4h", "4-6h", "6-8h", ">8h"] OR integer (hours) | Sleep duration ranges |
      | **sleep** | **OPTIONAL** | `notes` | string (optional) | free text | Sleep quality notes |
      | **medication** | **OPTIONAL** | `medications` | array of strings | Simple: ["Imodium", "Probiotics"] | Medication entries (structured objects deferred to post-MVP per `T810A2-RES-001` R1.2) |
      | **hydration** | **OPTIONAL** | `water_intake` | float/enum | cups OR liters OR range category | Water consumption |

      **MVP Scope Boundary** (per Activity 1.9 QA COMMENT 2):
      - **REQUIRED Entry Types** (MVP Core): meal, stool, digestion, mental — Story specifications developed in Phase 2
      - **OPTIONAL Entry Types** (MVP Extended): sleep, medication, hydration — Templates developed in Activity 2.0; Story specifications deferred to post-MVP
      - **DEFERRED Entry Types** (Post-MVP): exercise, skin, period, patient_state, others per `T810A2-RES-001` A.1

      **Enhancement Rationale**:
      - **"blood" in stool.metadata**: Clinically critical for IBD/colitis differentiation (alarm symptom per `T810A2-RES-001` A.5)
      - **"salty", "fibrous" in meal.metadata**: Common dietary triggers per `T810A2-RES-001` R1.2
      - **Semantic anchor labels**: All scales populated per `T810A2-RES-001` R1.3 (Bristol 0-7, pain/bloating/mood/stress)
      - **OPTIONAL entry types**: Enable holistic GI tracking (sleep quality, medication effects, hydration patterns correlate with symptoms) while controlling MVP scope


   2) **T810A-ADR-002-FR-002 (Critical Requirements)**
      - Value set definitions: What each numeric level means  
      - Descriptive labels for each scale point  
      - Guidance for LLM_Gastro on scale mapping from natural language input

   3) **T810A-ADR-002-FR-003 (Vocabulary Governance)**
       - **Vocabulary Versioning**: Track vocabulary catalog version (e.g., "v1.0.0")
       - **Controlled Expansion**: New vocabulary values approved via Epic consultant coordination
       - **Cross-Feature Notification**: Features notified of vocabulary additions/deprecations
       - **Backward Compatibility**: Vocabulary additions SHALL NOT break existing JSON structures

   4) **T810A-ADR-002-FR-004 (Cross-Feature Consistency)**
      - **T810A1 (PROMPT)**: System prompt references vocabulary catalog for Dynamic JSON generation
      - **T810A2 (PATIENT)**: Schema specifications implement vocabulary as authoritative source
      - **T810A3 (REPORT)**: Aggregation logic depends on vocabulary consistency for pattern analysis
      - **Enforcement**: Features SHALL NOT deviate from catalog without Epic ADR amendment

   5) **T810A-ADR-002-FR-005 (Cara Care Alignment)**
      - **Primary Exemplar**: Cara Care application UX patterns and terminology
      - **Supplementary Research**: Clinical vocabularies from `T810A-ADR-004` (ROME IV, ACG/AGA guidelines) for medical terminology
      - **Patient Familiarity**: Vocabulary assumes patient familiarity with Cara Care-aligned tracking terms per `T810A2-ASSUM-005`
      - **Vocabulary Extraction**: Systematic extraction via research commission (`T810A2-RES-001` Part 1: Cara Care Vocabulary Extraction)

   6) **T810A-ADR-002-FR-006 (Maintenance Governance)**
      - **Owner**: Client (vocabulary adoption/expansion authority)
      - **Updates**: LLM_Consultant proposes, Client approves
      - **Update Triggers**: Cara Care application updates, clinical guideline changes, patient feedback
      - **Documentation**: ADR body maintains vocabulary catalog with version history
      - **Traceability**: Link to research IDs (`T810A-RES-001`, `T810A2-RES-001`), Cara Care resources, clinical standards


  **Consequences:**
  - (+) Centralized vocabulary authority; cross-feature aggregation compatibility per `T810A-DEP-002`; Cara Care dual-processing alignment per `T810A-CON-002`
  - (+) Systematic vocabulary governance prevents drift; Epic-level updates avoid feature-level inconsistencies
  - (±) Cara Care exemplar assumes patient UX familiarity; vocabulary expansion requires Epic coordination overhead
  - (±) Research commission required for exhaustive vocabulary extraction (`T810A2-RES-001` Part 1)
  - (-) English-only MVP scope per `T810A2-ASSUM-006`; multilingual vocabularies deferred

  **Alternatives Considered:**
  - **Option A**: Feature-distributed vocabularies — Rejected: Cross-feature inconsistency; aggregation incompatibility; maintenance burden
  - **Option B**: Embed in GDR-002 — Rejected: GDR updates for every vocabulary addition create governance overhead
  - **Option C**: External vocabulary file — Rejected: Lacks traceability; governance unclear
  - **Option D**: No controlled vocabularies — Rejected: Violates `T810A2-NFR-003` (Vocabulary Completeness); pattern analysis unreliable

  **References:**
  `T810A-GDR-002 (Schema Split Architecture)`,
  `T810A-GDR-004 (GI Knowledge Base Sources)`,
  `T810A-ADR-001 (Trust-and-Verify Confidence Policy)`,
  `T810A-ADR-003 (Dual-Purpose Reporting Policy)`,
  `T810A-ADR-004 (GI Knowledge Sources Catalog)`,
  `T810A-DEP-002 (Long-term Analysis)`,
  `T810A-CON-002 (Platform Compatibility)`,
  `T810A-QG-006 (Patient Usability)`,
  `T810A-RES-001 (System Architecture & Clinical Validation)`,

  **Provenance:**
  `handoff_brief_T810A2-SCHEMA.md`,
  `plan_T810A2-SCHEMA_phase0-4.md` 

---

## XII. CLIENT APPROVAL GATE

**Phase 1 Completion Criteria** (per Consultancy Plan):

- [ ] **Gate 0: Foundation Approval** — Section III.A-III.D approved (completed in Phase 0)
- [ ] **Checkpoint 1: F-RID Review** — Review criteria below:

**Review Criteria for Client Approval**:

1. [ ] Inherited Considerations table correctly references governing E-RIDs/E-GDRs per T102-STD-003
2. [ ] No F-RID duplicates E-RID content (delta-only principle maintained)
3. [ ] All F-RID categories (ASSUM, DEP, NFR, IF, CON, INT) complete and coherent
4. [ ] F-RID IDs follow T102-STD-005 construction pattern: `T810A2-{CATEGORY}-{NNN}`
5. [ ] Traceability matrix demonstrates clear E-RID → F-RID expansion logic
6. [ ] No conflicts identified with T810A1 F-RIDs (integration alignment validated)
7. [ ] Client directives (foundational JSON requirements, Cara Care exemplar, HYBRID annotation) reflected in F-RIDs
8. [ ] F-RIDs provide sufficient specification depth for Story S01-S09 development (Phase 2)

**Authorization to Proceed**:

☐ **Client Approval**: All review criteria satisfied; authorize transition to Phase 2 (Schema Development & Validation)

**Blocking Issues**: ____________________________________________________________

---

## XIII. CLARIFYING QUESTIONS FOR CLIENT

Before proceeding to Phase 2 (Schema Development & Validation), please confirm:

1. **Inherited Considerations Completeness**: Does the Inherited Considerations table accurately capture the governing E-RIDs/E-GDRs for T810A2? Are there any E-RIDs we should add or remove?

2. **F-RID Scope Boundaries**: Do the proposed 25 F-RIDs provide sufficient foundational requirements for developing detailed Story specifications (S01-S09) in Phase 2, or are there gaps we should address now?

3. **Integration Alignment Confidence**: Given the T810A1 integration dependencies (IF-006, INT-004, INT-005, NFR-009), do you foresee any alignment risks that we should proactively address in Phase 1 before Story development?

4. **Schema Complexity Trade-offs**: The proposed CON-001 (Schema Complexity Constraint) limits nested objects to ≤2 levels deep. Does this balance adequately address your "structured but not overcomplicated" directive, or should we define more explicit complexity thresholds?

5. **Mandatory/Optional Field Mapping Approach**: T810A2-INT-001 and IF-004 propose mandatory/optional field mapping to enable Probe triggering. Should we develop this mapping in Phase 1 (before Story specs) or defer to Story S08 (Integration Patterns) in Phase 2?

---

## XIV. CHECKPOINT 1 VALIDATION ANALYSIS REFERENCE

**Activity 1.10 Holistic F-RID Validation** has been completed. Comprehensive validation analysis (Level 1-3) documented in separate analysis artifact per workspace documentation standards.

**Analysis Artifact**: `prompt/artifacts/tasks/T810/consultant/workspace/analysis/analysis_T810A2-SCHEMA_checkpoint1.md`

**Validation Summary**:
- **Overall Result**: ✅ PASS (with 4 corrections required)
- **Issues Identified**: 1 CRITICAL, 1 MODERATE, 2 MINOR
- **Fixes Status**: ✅ APPLIED (see sections below for implemented corrections)

**Implemented Corrections** (per analysis artifact Section VI):
1. ✅ **DEP-005 Split**: Platform capability content retained; vocabulary authority portion removed (Section IV corrected)
2. ✅ **RES-001 Title Shortening**: Title updated to "Template & Vocabulary Research" (Section IX corrected)
3. ✅ **IG Count Correction**: Section X.A updated to IG: 7 items
4. ✅ **IC Table Finalization**: Section II replaced with validated IC Table (Architecture row added, IG-006 added, T810A1 row removed)

**Refer to analysis artifact for complete validation findings, compliance assessment, and Epic T810A governance alignment validation.**

**END OF PROPOSAL**
