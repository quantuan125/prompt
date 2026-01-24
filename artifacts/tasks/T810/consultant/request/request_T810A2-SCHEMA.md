---
artifact_type: 'REQUEST'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2'
feature_code: 'PROMPT'
version: '1.0.0'
date: '2025-10-05'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# REQUEST: LLM_Gastro System SCHEMA - `T810A2 (SCHEMA)`

## I. EXECUTIVE SUMMARY

---

## II. TABLE OF CONTENTS

---

## III. CORE CONTENT

<!-- Part 0 — SAD-lite -->

### A. Feature Solution Framework

#### 1. Problem Recap & Constraints

**Problem & Desired Outcome**
  *   **Problem:** The LLM_Gastro clinical tracking assistant requires foundational data architecture to reliably capture, structure, and persist patient health information across sessions. Without comprehensive schema specifications, controlled vocabularies, and validation rules, the system risks inconsistent data capture, value drift, clinical utility gaps, and integration failures with the primary feature (T810A1-PROMPT). The ChatGPT platform constraint (read-only file access, no programmatic validation) necessitates prompt‑engineering‑based data governance that depends entirely on exhaustive, unambiguous schema definitions.
  *   **Desired Outcome:** LLM_Gastro reliably generates clinically useful, consistently structured tracking data using a well‑defined patient profile schema (stable patient context) and tracking entry schemas (dynamic tracking entries). All categorical fields have exhaustive controlled vocabularies with semantic mappings. Integration patterns enable smart Probe triggering, efficient end‑of‑day aggregation, and conflict‑free session initialization. The data architecture supports pattern analysis, clinician handoff, and cross‑session continuity without programmatic validation overhead.

**Stakeholders & Concerns:**
  *   **Stakeholders:** LLM_Gastro Agent (Primary Consumer), Patient (Data Governor), T810A1‑PROMPT Feature (Integration Dependency), T810A3‑REPORT Feature (Future Consumer), Clinician (Handoff Recipient).
  *   **Concern → Criterion mapping:**
      *   LLM_Gastro need for clear schema guidance → *Schema Clarity & Usability*
      *   Patient need for familiar UX patterns → *User Experience Alignment*
      *   T810A1‑PROMPT need for integration reliability → *Integration Consistency*
      *   Clinician need for data accuracy → *Clinical Validity & Completeness*
      *   System need for token efficiency → *Token Optimization*

#### 2. Decision Criteria & Weights
<!-- Agree *how* we'll judge options; weights are co-owned by Client + Template Owner + Consultants.* -->

**Baseline Criteria**
1.  **Schema Clarity & Usability:** The degree to which schemas are self‑documenting, unambiguous, and easy for LLM_Gastro to interpret without programmatic validation.
2.  **Clinical Validity & Completeness:** The comprehensiveness of controlled vocabularies and their alignment with clinical standards (Bristol scale, Cara Care patterns).
3.  **Integration Consistency:** The reliability of schema specifications in supporting T810A1‑PROMPT integration points (Probe triggering, aggregation, initialization).
4.  **Token Optimization:** The efficiency of schemas in minimizing token overhead while maintaining clinical utility (target: <200 tokens for patient profile schema).
5.  **User Experience Alignment:** The degree to which schemas mirror familiar UX patterns from Cara Care application for patient comfort.

**Weighting Method**
*   Sum = **1.00** with the following weights reflecting feature priorities:
    *   Schema Clarity & Usability: **0.30**
    *   Clinical Validity & Completeness: **0.30**
    *   Integration Consistency: **0.25**
    *   Token Optimization: **0.10**
    *   User Experience Alignment: **0.05**

*Consultant's note:* Schema clarity and clinical completeness are co‑equal priorities (0.30 each) reflecting the dual requirement for LLM_Gastro interpretability AND clinical utility. Integration consistency is critical (0.25) due to T810A1 dependency. Token efficiency matters but is secondary to correctness. UX alignment is lowest weighted (0.05) since patient interaction is mediated through LLM_Gastro natural language, not direct schema exposure.

<!-- Part 1 — Business View (BRD) -->

### B. Source & Scope

* **Initiative:** `T810 (GASTRO)`
* **Epic:** `T810A (SYSTEM)`
* **Feature:** `T810A2 (SCHEMA)`
* **Repository Path (source):** `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md`
* **Repository Path (target — templates):** `prompt/roles/gastro/data/`
* **Repository Path (target — vocabularies):** `prompt/roles/gastro/data/controlled_vocabularies.md`

**In Scope:**
*   Defining complete patient profile schema (stable patient context) with field categorization, data types, constraints, and controlled vocabularies for categorical fields.
*   Defining complete tracking entry schemas for minimum 5 types (**patient_state**, **meal**, **stool**, **sleep**, plus flexible types: **exercise**, **stress_event**, **medication_taken**, **supplements**).
*   Specifying exhaustive controlled vocabularies for ALL categorical fields with semantic scale mappings (numeric values → descriptive labels).
*   Defining integration patterns: Probe triggering rules (mandatory/optional field mapping), end‑of‑day aggregation format, session initialization sequence, conflict resolution examples.
*   Defining validation and quality requirements using prompt‑engineering approach (no programmatic validation).
*   Creating implementation artifacts: patient profile schema template, tracking entry schema templates (one per entry type), controlled vocabulary documentation.
*   Defining template annotation approach (**HYBRID**: minimal inline hints for complex fields, clean structure for straightforward fields).

**Out of Scope:**
*   Execution protocols for LLM_Gastro (`T810A1‑PROMPT-S05` responsibility).
*   Exemplar dialogue outputs demonstrating template usage (`T810A1‑PROMPT-S08` responsibility).
*   UI/UX for manual patient profile updates (future feature).
*   Automated validation logic or programmatic schema enforcement (ChatGPT platform constraint per `T810A1‑CON‑008`).
*   Cross‑session reporting formats and pattern analysis (`T810A3 (REPORT)` responsibility).
*   Clinical knowledge sources for LLM_Gastro (`T810A1‑PROMPT-S04` responsibility).

### C. Business Objectives & Success Signals 

**Primary Objectives:**
1.  To deliver complete Request content with exhaustive schema specifications, controlled vocabularies, and integration patterns that enable `T810A1` to generate clinically valid, consistently structured tracking data without programmatic validation.
2.  To establish foundational data architecture (schema split architecture per `T810A-GDR-002 (Schema Split Architecture)`) that supports token‑efficient session initialization, smart Probe triggering, reliable end‑of‑day aggregation, and conflict‑free memory integration.
3.  To provide self‑documenting schema templates (**HYBRID** annotation approach) that serve dual purpose: schema definition + instructional guides for LLM_Gastro generation behavior.

**Success Signals (MVP, qualitative):**
1.  **Exhaustive Vocabulary Coverage:** ALL categorical fields across ALL entry types have complete controlled vocabulary specifications with no "TBD" or "example only" placeholders. Semantic scale mappings (numeric → descriptive labels) defined for mood (‑2 to 2), stress (1‑5), tummy_pain (1‑5), bloating (1‑5), Bristol scale (1‑7).
2.  **T810A1 Integration Validation:** T810A1 consultant confirms schema specifications align with `T810A1-IF-006 (Tracking Payload Generation)`, `T810A1-INT-004 (Patient Data Architecture)`, and Probe-triggering requirements without conflicts or gaps.
3.  **Template Self‑Documentation:** JSON templates are interpretable by LLM_Gastro without external documentation; **HYBRID** annotation provides clarity for complex fields (stool metadata, meal ingredients) while maintaining clean structure for straightforward fields (timestamps, notes).
4.  **Mandatory/Optional Field Clarity:** Every entry type has explicit mandatory/optional field specifications; Probe triggering rules clearly map missing mandatory fields to question types (Type 1‑6 per research framework).
5.  **Clinical Utility Validation:** Schema specifications support pattern analysis use cases; controlled vocabularies enable correlation tracking (stress levels → symptom severity, meal metadata → stool characteristics); token efficiency target achieved (<200 tokens for patient profile schema).
6.  **Implementation Artifact Completeness:** Deliverable package includes: (a) complete Request document with 9 stories, (b) patient profile schema template at `prompt/roles/gastro/data/template_stable_patient_schema.yaml`, (c) tracking entry schema template at `prompt/roles/gastro/data/template_dynamic_tracking_schema.yaml`, (d) controlled vocabulary documentation at `prompt/roles/gastro/data/controlled_vocabularies.md`.

---

### D. Stakeholders

| Role Label | Persona | Responsibility |
| :--- | :--- | :--- |
| Decision Owner | Client | Approves the final system prompt and its requirements. |
| Primary User | Patient | Interacts with the `LLM_Gastro` agent daily for support. |
| Secondary Consumer | Clinician | Reviews agent-generated summaries to inform patient care. |
| Request Author | LLM_Consultant | Consumes client needs to produce this feature request. |

---

### E. Inherited Considerations

| Source Artifact | Source ID | Category | Inherited Rule IDs |
|:----------------|:----------|:---------|:-------------------|
| SPS | `T810A` | Quality Goals | `T810A-QG-005 (Architecture Maintainability)`, `T810A-QG-006 (Patient Usability)`, `T810A-QG-007 (Confidence Communication)`, `T810A-QG-008 (Clarification Over Guessing)` |
| SPS | `T810A` | Dependencies | `T810A-DEP-001 (Platform Capability)`, `T810A-DEP-002 (Long-term Analysis)`, `T810A-DEP-004 (Patient Data Structures)`, `T810A-DEP-005 (Clinical Safety Framework)` |
| SPS | `T810A` | Assumptions | `T810A-ASSUM-002 (Input Modality & Quality)`, `T810A-ASSUM-003 (LLM Capability)`, `T810A-ASSUM-004 (Platform Memory Uncertainty)` |
| SPS | `T810A` | Constraints | `T810A-CON-001 (System Prompt Scope)`, `T810A-CON-002 (Platform Compatibility)`, `T810A-CON-004 (ChatGPT Architectural Constraints)` |
| SPS | `T810A` | Implementation Guidance | `T810A-IG-002 (Probe Phase Enforcement)`, `T810A-IG-003 (Explicit Classification)`, `T810A-IG-004 (Tracking Payload Per-Turn Delta)`, `T810A-IG-005 (Memory Review Protocol)`, `T810A-IG-006 (Session Context Handoff)` |
| SPS | `T810A` | Research | `T810A-RES-001 (System Architecture & Clinical Validation)`, `T810A-RES-002 (Conversation-Driven Empirical Validation)` |
| SPS | `T810A` | Governance | `T810A-GDR-001 (Trust-and-Verify Workflow Standard)`, `T810A-GDR-002 (Schema Split Architecture)`, `T810A-GDR-003 (Dual-Purpose Clinical Reporting)`, `T810A-GDR-004 (GI Knowledge Base Sources)` |
| CONCEPT | `T810A` | Architecture | `T810A-ADR-001 (Trust-and-Verify Confidence Policy)`, `T810A-ADR-002 (Foundational Vocabulary Authority)`, `T810A-ADR-003 (Dual-Purpose Reporting Policy)`, `T810A-ADR-004 (GI Knowledge Sources Catalog)` |

<!-- Part 2 — System View (SRS) -->

### F. Feature Requirements

#### 1. Assumptions 

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

* **T810A2-ASSUM-007 (Manual Workflow Reliability)** — Patients can reliably perform manual JSON compilation/export workflow: copy tracking payload codeblocks from LLM_Gastro session → save to file → upload to Project Knowledge for future sessions or enter into Cara Care app. Manual workflow friction (multi-step process, potential copy errors) is acceptable for MVP. See `T810A2-CON-004` and `T810A2-IG-004` for authoritative implementation rules.

#### 2. Constraints

* **T810A2-CON-001 (Schema Complexity)** — Schema nesting SHALL NOT exceed 2 levels per `T810A-GDR-002` to maintain LLM generation reliability per `T810A-CON-004`. Nested objects limited to 2 levels deep; metadata arrays with controlled vocabularies permitted. Exception handling deferred per client directive. 

* **T810A2-CON-002 (Vocabulary Authority)** — Controlled vocabularies SHALL follow Cara Care application patterns as primary authority per proposed `T810A-ADR-002` (Foundational Vocabulary Authority). External clinical standards (PHQ-9, GAD-7) deferred to post-MVP; Epic governance evolution triggers upgrade. 

* **T810A2-CON-003 (Specification-Based Validation)** — Schema validation SHALL be specification-based only per `T810A-CON-004`; no programmatic enforcement. `T810A2` defines exhaustive specifications; validation enforcement delegated to Epic governance per `T810A-GDR-002` . 

* **T810A2-CON-004 (Manual Profile Management)** — The patient profile schema data SHALL be read-only for the agent per `T810A-GDR-002` and `T810A-CON-004`, manually managed by the patient ONLY. Tracking payloads (JSON) SHALL be agent-generated per `T810A-IG-004` and manually compiled by the patient. No automated backend compilation for MVP. Manual patient update workflow defined by `T810A2-IG-004`. 

* **T810A2-CON-005 (Fixed Schema Keys)** — Tracking schema keys SHALL be 100% T810A2-defined for MVP per `T810A-GDR-002`. Runtime flexible key addition prohibited; schema evolution via T810A2 governance updates only per `T810A2-S06`. Patient profile data remains patient-managed per `T810A2-CON-004`. Simplifies template design, enables exhaustive vocabulary specification per `T810A2-NFR-003`, ensures Cara Care dual processing consistency.


#### 3. Non-Functional Requirements

* **T810A2-NFR-001 (Token Efficiency)** — Schema designs (patient profile schema + tracking entry schema templates) SHALL optimize for minimal token consumption while maintaining field completeness per `T810A-RES-001`. **Platform-Informed Token Budget Recommendations**:
  - **System Prompt**: 1,500-2,000 tokens target (safe headroom for growth)
  - **Patient Profile**: ≤ 1,000 tokens per patient (including history, chronic conditions, key preferences)
  - **Tracking Entry**: ≤ 250 tokens per entry (most 80-150 tokens; upper bound prevents unbounded free-text)
  - **Vocabulary Catalog**: 8,000-15,000 tokens total (Epic ADR-002 + T810A2 docs)

* **T810A2-NFR-002 (Schema Clarity)** — Templates SHALL be self-documenting for LLM_Gastro generation without external documentation or programmatic validation per `T810A-CON-004`. Dual purpose: schema definition + generation instructions. Template format, annotation density, and implementation patterns per `T810A2-IG-002`.

* **T810A2-NFR-003 (Vocabulary Completeness)** — ALL categorical fields SHALL have exhaustive controlled vocabulary specifications. "Completeness" applies to vocabulary DEFINITIONS (all possible values documented), not generation completeness (LLM may generate incomplete entries with null fields per `T810A-IG-002` and `T810A2-NOTE-003`).

* **T810A2-NFR-004 (Clinical Validity)** — Controlled vocabularies and field definitions SHALL align with clinically recognized standards and support pattern analysis use cases. Cara Care application is primary exemplar per `T810A2-CON-002` and `T810A-GDR-004`.

* **T810A2-NFR-005 (Schema Maintainance)** — Schema templates SHALL support future evolution with minimal rework per `T810A-QG-005`. New entry types can be added through `T810A2` governance updates without restructuring foundational schemas. Orthogonal to `T810A2-CON-005` runtime flexibility constraint per `T810A2-NOTE-004`.

#### 4. Dependencies

* **T810A2-DEP-001 (Epic Integration Coordination)** — `T810A2` schema specifications fulfill `T810A-DEP-004` and must align with Epic governance (`T810A-GDR-002`, `T810A-IG-002/004/005` integration patterns). Misalignment blocks dependent features (`T810A1` for tracking payload generation, `T810A3` for aggregation/continuity). Coordination: Inter-feature integration governed by `T810A` Epic consultant through Epic GDR/ADR development and checkpoint validation. Technical integration details specified in `T810A2-INT` (external/cross-feature) and `T810A2-IG` (internal) category items.

* **T810A2-DEP-002 (Epic Deliverable Validation)** — `T810A2` deliverables  require `T810A` Epic consultant validation for Epic governance and architectural decisions compliance before implementation handoff.

* **T810A2-DEP-003 (Reporting Forward Compatibility)** — `T810A2` schema design should consider `T810A3` (Reporting & Continuity: daily report format, aggregation, next-session context injection per `T810A-DEP-002`) forward compatibility. Considerations: JSON schema structure stability for cross-session aggregation, field naming consistency for pattern analysis, controlled vocabulary alignment across features, dual-format output compatibility (markdown narrative + structured JSON per `T810A-ADR-003-FR-006`). Approach: Lightweight Epic governance alignment (`T810A-GDR-003`, `T810A-ADR-003`, `T810A-IG-006`) without formal requirements research; accept calculated rework risk.

* **T810A2-DEP-004 (Research Resource Availability)** — `T810A2-RID` development and Story specifications may require LLM_Researcher commissioning for industry standards research, external validation, or technical feasibility studies beyond `T810A2` consultant expertise (e.g., template format selection, controlled vocabulary validation, JSON schema best practices, ChatGPT Project Knowledge compatibility).

* **T810A2-DEP-005 (Platform Capability)** — `T810A2` schema templates depend on ChatGPT Project Knowledge platform capabilities per `T810A-CON-002`. **Platform Constraints** (per `T810A2-RES-001` Deliverable B.6):
  - **File Storage**: 25 files max (Plus), 512MB per file limit
  - **Token Limits**: 32k context window (GPT-4), ~2M tokens Project Knowledge processing upper bound per file
  - **Format Support**: JSON, YAML, Markdown natively supported (text-based; YAML chosen per `T810A2-RES-001` R2.1)
  - **Update Workflow**: Manual replace-only (no version control in UI; requires external governance per `T810A2-RES-001` R1.5)
  - **Performance**: Minimal retrieval latency for small files; no parsing overhead concerns

  Platform constraints validated against `T810A2-NFR-001` token budget recommendations per `T810A2-RES-001` R5; schema design stays well within limits.

#### 5. Interfaces & Data

* **T810A2-IF-001 (Patient Profile Schema Interface)** — Define patient profile schema interface contract: schema structure, field types/constraints, read-only access pattern, error states for missing/malformed profiles. Interface specifies WHAT data structures are loaded per `T810A-GDR-002`.

* **T810A2-IF-002 (Tracking Entry Schema Interface)** — Define tracking entry schema interface contract: entry type schemas, structured key naming conventions, 100% schema-defined keys per `T810A2-CON-005` (no runtime flexible key addition for MVP). Per-turn payload generation pattern per `T810A-IG-004` and envelope per `T810A-ADR-005`; missing mandatory field handling via null values + Probe triggering per `T810A-IG-002`. Template format (internal YAML, export JSON) and annotation approach per `T810A2-IG-002`. Interface specifications: entry type schemas per `T810A2-RES-001` Deliverable A.1, controlled vocabulary integration per `T810A2-IF-003`, field classification per `T810A2-IF-004`.

* **T810A2-IF-003 (Controlled Vocabulary Interface)** — Define controlled vocabulary interface contract: vocabularies per Epic `T810A-ADR-002` as authoritative source; LLM_Gastro accesses vocabularies via template-embedded references. Semantic scale mappings (numeric → descriptive labels) embedded inline for cross-feature consistency. Value set enforcement prompt-engineering based per `T810A-CON-004`. Vocabulary documentation patterns per `T810A2-IG-003`. 

* **T810A2-IF-004 (Field Classification Interface)** — Define mandatory/optional field classification interface: categorization principles per entry type enabling Probe phase triggering per `T810A-IG-002`. High-level mapping rules: 
(1) Timestamp fields mandatory for all entry types (clinical temporal analysis), 
(2) Mental state fields mandatory for patient_state (stress, mood pattern analysis), 
(3) Bristol type mandatory for stool (core classification per `T810A-ADR-004`), 
(4) Meal items mandatory for meal (trigger analysis), 
(5) Metadata fields optional (contextual enrichment). 

**Interface Responsibility Matrix**:

#### 6. Implementation Guidance 

* **T810A2-IG-001 (Null-Before-Probe Pattern)** — LLM_Gastro SHALL default to explicit `null` values for ALL tracking entry fields (mandatory + optional) when patient context insufficient, BEFORE Probe phase triggers per `T810A-IG-002` and `T810A-QG-008`. This enforces no-guessing requirement per `T810A2-NOTE-003`. **JSON Representation** (per `T810A2-RES-001` R6.1): Use explicit `null` keyword (not missing field omission) for unambiguous null state tracking. **Template Annotation Phrasing** (per `T810A2-RES-001` R3.3): Directive style — "If unknown, set to null and ask patient later." Probe phase fills mandatory field nulls in second pass after clarification. Prevents hallucination, enables reliable Probe-based gap-filling per `T810A2-NFR-003`. 

* **T810A2-IG-002 (YAML Template Format)** — Project Knowledge templates SHALL use **YAML format** with native `#` comments for HYBRID annotations per `T810A2-RES-001` R2.1. **Template Format Specification**:
  - **Internal Format**: YAML with native `#` comments for Project Knowledge storage (~30-50% token savings vs JSON per `T810A2-RES-001` B.1)
  - **Output Format**: JSON for runtime tracking payloads and portable exports (interoperability with Cara Care dual processing, `T810A3` aggregation, `T810A-GDR-002` compliance per `T810A2-RES-001` R2.1)
  - **Annotation Density**: Minimal field-level annotation — 70-80% fields no comments, 20-30% short comments on complex/critical fields (qualitative guideline per `T810A2-NOTE-002` and `T810A2-RES-001` R3.1)
  - **Annotation Phrasing**: Short, directive style (e.g., "Allowed values: ...", "Default: null if unknown; probe if null" per `T810A2-RES-001` R3.3)
  - **Token Budget Compliance**: System+knowledge templates target ≤ 2,000 tokens combined per `T810A2-RES-001` R5.1

**Dual Responsibility Implementation** (per `T810A2-RES-001` R3.2): Each YAML template contains top-level comment block (purpose, patient profile vs tracking schema, usage) + local comments at critical fields only (scales, controlled vocab, null behavior). Templates serve dual purpose: schema definition + LLM generation instructions per `T810A2-NFR-002`. Bridges `T810A2` schema design with `T810A1-S05` tracking protocol. 

* **T810A2-IG-003 (Vocabulary Documentation Standard)** — Controlled vocabulary specifications SHALL follow `T810A-ADR-002` extracted from `T810A2-RES-001` R6.3. 
  **Table Layout** (per `T810A2-RES-001` R1.5): Base standard on Cara Care-inspired formats from `T810A2-RES-001` Deliverable A (Bristol scale 0-7 with semantic labels, symptom severity scales 1-5 with endpoint descriptions, meal/stool metadata enumerated arrays). 
  **Hybrid Placement Strategy** (per `T810A2-RES-001` R4.1): Embed short critical lists (Bristol 0-7, small severity scales) directly in YAML templates for LLM generation clarity; externalize large/evolving lists (extended meal.metadata, stool.metadata, future entry type vocabularies) in `T810A-ADR-002` catalog + `controlled_vocabularies.md` for maintainability. 
  **Future Vocabulary Additions**: All expansions SHALL follow markdown table pattern with semantic anchors ensuring cross-feature consistency per `T810A-ADR-002`. Specification details in `T810A2-S07`

* **T810A2-IG-004 (Manual Workflow Guidance)** — Patients SHALL manually export tracking payloads as **`.json` files** (NOT YAML) for dual-purpose workflows per `T810A2-RES-001` R6.4: 
  (1) Manual Cara Care app entry (dual processing alignment per `T810A2-RES-001` C.2), 
  (2) Future session loading into Project Knowledge per `T810A-IG-006`, 
  (3) Optional `T810A3` aggregation input (post-MVP automated backend per `T810A-GDR-003`). 
  **Manual Compilation Workflow** (per `T810A2-INT-002` and `T810A-ADR-005`): Patient copies per-turn tracking payload codeblocks from the session (each codeblock is a JSON array / “Pattern A”) → appends/merges the entry objects into one chronological JSON array → saves file. 
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

#### 7. Integration Notes

* **T810A2-INT-001 (Probe Triggering Integration)** — `T810A2` mandatory/optional field classification per entry type enables `T810A1-NFR-005 (Probe Phase Enforcement)` Probe triggering per `T810A-IG-002`. Missing mandatory fields suggest Probe phase activation (≥2 clarifying questions). High-level pattern: T810A2 field categorization → `T810A1-S05 (Execution Protocol)` triggering logic → `T810A-IG-002` potential enhancement for field-to-question mapping framework. Detailed field lists in `T810A2-S08`.

* **T810A2-INT-002 (Aggregation Format Integration)** — `T810A2` tracking log aggregation format supports `T810A3` cross-session pattern analysis and Cara Care dual processing per `T810A-GDR-003`. The MVP per-turn tracking payload contract is **Pattern A** per `T810A-ADR-005` (a chronological JSON array of entry objects, delta-only). Manual workflow guidance per `T810A2-IG-004` compiles these per-turn arrays into a single chronological array for export. **Pattern B** and **Pattern C** exemplars are retained as **non-default alternatives** for derived views (e.g., post-processing, reporting layouts) and are not the per-turn generation contract for `LLM_Gastro`.

* **T810A2-INT-003 (Session Initialization Integration)** — T810A2 patient profile schema + tracking schema templates support `T810A1-INT-005 (Memory Review Protocol)` session initialization sequence per `T810A-GDR-002`. Loading pattern: Step 0 Memory Review → Step 1 patient profile (read-only) + tracking schema templates → `T810A1-S05` protocol execution. Suggests `T810A-IG-005` potential enhancement for standard initialization workflow.

* **T810A2-INT-004 (Conflict Resolution Integration)** — T810A2 patient profile precedence hierarchy informs `T810A1-INT-005 (Memory Review Protocol)` conflict detection when ChatGPT Memory conflicts with patient profile per `T810A-GDR-002`. Precedence: Patient Profile > Memory. High-level pattern: T810A2 field categorization → `T810A1` Probe phase clarification → patient updates patient profile manually. Suggests `T810A-IG-005` potential enhancement for standard conflict resolution phrasing.

* **T810A2-INT-005 (T810A3 Forward Compatibility)** — T810A2 schema evolution principles enable future `T810A3` requirements without rework per `T810A2-DEP-003`. Extensibility patterns: additive evolution (new entry types), vocabulary expansion (external catalog per `T810A-ADR-002`), field additions (optional fields), aggregation compatibility (chronological array structure per `T810A2-INT-002`). Schema evolution workflow in `T810A2-S06`.

### G. Feature Governance Decisions

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|

<!-- Feature-level governance decisions will be documented here following Epic GDR patterns -->

### H. Open Issues & Risks

**Issues**
<!-- GUIDANCE:
Status = `OPEN, IN-REVIEW, RESOLVED, BLOCKED, DEFERRED`,
priority = `Low, Medium, High`
-->

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### I. Research & Notes

**Research**

| Research ID | Title | Summary | Linked To | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T810A2-RES-001` | **Template Format & Vocabulary Extraction** | Combined research for ChatGPT Project Knowledge template selection (JSON/YAML/JSONL evaluation for comment support, LLM parsing, token efficiency) and exhaustive Cara Care controlled vocabulary extraction (meal metadata, stool descriptors, symptom scales) to establish foundational vocabulary authority for categorical fields | `T810A2`, `T810A` | [brief](../research/brief/brief_T810A2-SCHEMA_template-format-vocabulary-extraction.md) | [report](../research/report/report_T810A2-SCHEMA_template-format-vocabulary-extraction.md) |

**Notes**
* **T810A2-NOTE-001 (Handoff Brief)** — Handoff brief from T810A consultant that initiate T810A2 feature development `handoff_brief_T810A2-SCHEMA.md`

* **T810A2-NOTE-002 (MVP Validation Approach)** — Template format selection and NFR validation criteria (token efficiency thresholds, self-documentation sufficiency, vocabulary exhaustiveness metrics) are QUALITATIVE for MVP per client directive. Quantitative validation deferred to post-MVP testing with empirical evidence. Story acceptance criteria use subjective validation (e.g., "Developer confirms template interpretability") with understanding that criteria will be refined after implementation testing. Template format decision deferred to RES-001 research; decision point at Story S01 based on ChatGPT Project Knowledge compatibility validation per `T810A-CON-004`.

* **T810A2-NOTE-003 (Null-Before-Probe Strategy)** — LLM_Gastro SHALL default to null values for ALL fields (mandatory + optional) when patient context is insufficient, BEFORE Probe phase triggers per `T810A-QG-008` and `T810A-IG-002`. This enforces no-guessing requirement more strictly than context-dependent approach. Probe phase THEN fills mandatory field nulls in second pass after patient clarification per `T810A2-INT-001`. Null default strategy prevents hallucination and enables reliable Probe phase gap-filling per `T810A2-NFR-003` and `T810A2-IG-001`.

* **T810A2-NOTE-004 (Schema Evolution Scope)** — "Flexible schema" (Story S06) refers to controlled vocabulary VALUE expansion, NOT key structure modification per client directive. `T810A2-CON-005` prohibits runtime key addition for MVP. New KEYS added only via `T810A2` governance-driven schema updates (Story S06 governance workflow). Flexibility applies to controlled vocabulary VALUES expansion within existing key structures, NOT runtime key structure modification. `T810A2-NFR-005` (design-time extensibility) is orthogonal to `T810A2-CON-005` (runtime flexibility prohibition).

### J. Stories & Specification 

#### 1. Story `T810A1‑S01` — Project Context

**Purpose**

**Functional Requirements**

**Acceptance Criteria**

**References**
* `T810A-GDR-005 (GI Knowledge Base Sources)`


### K. Acceptance Criteria Register (summary)

| ID | Title | AC Summary |
| :--- | :--- | :--- |

---

## V. APPENDIX 

### A. Amendment Log
| Date | Change Requester | Affected Req. ID | Summary of Change |
|------|------------------|------------------|-------------------|
| 2025-08-01 | Client | Initial | Initial SPS creation |

---

## VI. VALIDATION CHECKLIST

- [x] The Problem Statement (Section III-A) has received explicit client approval.
- [x] All requirements in Section III-B are prefixed with a unique, traceable ID (e.g., `SPS-T102-001`).
- [x] The Decision Owner / Accountable Role has been identified in Section III-C.
- [x] All known open issues, risks, and dependencies have been logged in Section III-D.
- [x] The artifact's YAML header is complete and syntactically correct.
- [ ] The 'Next Steps' section clearly defines the handoff to the Request workflow.

---

## VII. STAKEHOLDER SIGN-OFF

By signing off, stakeholders agree that the problems and requirements detailed in this document accurately reflect the desired work. Architectural and implementation design will be based on the contents of this artifact.

*   **Client:** _________________________ (Name, Date)
*   **Consultant:** _________________________ (Name, Date)

---


## VIII. NEXT STEPS

**Primary Stakeholder & Decision Owner:** `Client` 

**Downstream Consumer:** `LLM_Planner` 

**Implementation Actions & Responsibilities (RACI):**

| # | Action | Responsible | Accountable | Consulted | Informed |
|:--|:---|:---|:---|:---|:---|
| 1 | Create/modify the `SPS`, `Request`, and `Concept` structural templates and procedural guidelines. | `LLM_Consultant` | `Client` | `LLM_Planner` | `LLM_Developer` |
| 2 | Develop the distinct system prompts for each stage of the consultancy workflow. | `LLM_Consultant` | `Client` | `LLM_Planner` | - |
| 3 | Develop the required ID-mapping mechanism/script. | `LLM_Developer` | `LLM_Planner` | `LLM_Consultant` | - |
| 4 | Update the `prompt_main.md` documentation with the new workflow description. | `LLM_Developer` | `Client` | `LLM_Consultant` | - |

---

## IX. CHANGELOG

*   **v1.0.0_i1:** Initial SPS creation documenting the problem of linking two templates.
*   **v1.0.0_i2:** Major revision to expand scope to the full three-artifact (`SPS` → `Request` → `Concept`) workflow, incorporating external feedback and requirements from T101A.
*   **v1.0.0_i3:** Final revision incorporating multiple rounds of external feedback. Globally replaced `SYSTEM_ARCHITECT`, renumbered all requirements, removed success metrics from scope, and added new requirements for template governance and automation hooks. Set `Client` as final Decision Owner, corrected Issue ownership, added Planner sign-off to Concept, renumbered all requirements, and clarified Next Steps with a RACI matrix.
