---
artifact_type: 'COMMUNICATION'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2'
feature_code: 'PATIENT'
version: '1.1.0'
date: '2025-10-19'
status: 'ready_for_handoff'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_consultant: 'LLM_Consultant (Sub-Consultant)'
source_feature: 'T810A1-PROMPT'
---

# HANDOFF BRIEF: T810A2-SCHEMA Feature Development (v1.1.0 - S05 Integration Update)

## I. EXECUTIVE SUMMARY

This handoff brief commissions parallel development of Feature **T810A2-SCHEMA (Patient Data Structures)** to support the primary feature **T810A1-PROMPT (LLM_Gastro System Prompt)**. T810A2-SCHEMA defines comprehensive data schemas, controlled vocabularies, and integration patterns for patient profile management and tracking data capture in the LLM_Gastro clinical assistant.

**Critical Context**: T810A1-PROMPT development is currently at **Phase 1.5 completion** following empirical conversation analysis that revealed architectural requirements not captured in initial research. This brief reflects those real-world findings.

**Parallel Development Model**: T810A2-SCHEMA SHALL be developed in parallel with T810A1-PROMPT Phase 2-3 work. T810A1-PROMPT maintains surface-level JSON architecture references; T810A2-SCHEMA contains all detailed specifications.

**Expected Deliverable**: Complete Request document (`request_T810A2-SCHEMA.md`) with functional requirements, JSON schemas, controlled vocabularies, validation rules, and integration patterns.

---

## I-A. v1.1.0 UPDATE SUMMARY (S05 Execution Protocol Integration)

**Update Trigger**: T810A1 Phase 3.3A requirements discovery revealed template-driven architecture and S05-specific integration needs.

**Key Changes from v1.0.0**:

1. **Template-Driven Tracking Architecture** (NEW):
   - Tracking schema templates now have **dual responsibility**: schema definition + instructional templates
   - Templates must be self-documenting (structure teaches LLM how to generate entries)
   - S05 Custom Instructions provide HIGH-LEVEL preface only; templates in Project Knowledge hold DETAILED generation instructions
   - **Design Decision Required**: Inline annotations vs. clean exemplars (see Section III-D below)

2. **Exemplar Generation Responsibility Clarification** (NEW):
   - **T810A2-SCHEMA Responsibility**: Define schemas, controlled vocabularies, validation rules, AND self-documenting template structure
   - **T810A1-S08 Responsibility**: Create concrete exemplar dialogue outputs demonstrating template usage
   - Both inline annotations (if used) AND S08 exemplars will exist; decision on annotation approach in Section III-D

3. **S05 STEP Dependency Integration** (NEW):
   - Phase 1 (Tracking) STEPS depend on template clarity and structure
   - Phase 3 (Probe & Engage) depends on mandatory vs. optional field mapping for question prioritization
   - Research-validated 5-question Probe framework requires field-to-question-type mapping (Section V-C)

4. **Reference Examples Provided** (NEW):
   - `prompt/artifacts/tasks/T810/resources/gastro_example_tracking.json`: Example tracking JSON structure
   - CareCare app screenshots: `carecare_meal_tracking.jpeg` + `carecare_symptoms_tracking.jpeg` (familiar UX patterns to mirror)

**Impact on Development**:
- Templates must be designed as both schemas AND instruction manuals
- Coordination checkpoint added (Checkpoint 0) for template design consultation with T810A1 consultant
- Integration testing with S05 STEPS required before finalization

---

## II. FEATURE IDENTITY & SCOPE

### A. Feature Definition

| Attribute | Value |
|-----------|-------|
| **Feature ID** | T810A2-SCHEMA |
| **Feature Name** | Patient Data Structures |
| **Parent Epic** | T810A-SYSTEM |
| **Depends On** | None (foundational feature) |
| **Depended Upon By** | T810A1-PROMPT (primary), T810A3-REPORT (secondary) |
| **Primary Purpose** | Define and specify all patient data structures, schemas, and vocabularies for LLM_Gastro system |

### B. In Scope

1. **Patient Profile Schema Specification**
   - Complete schema definition (fields, types, constraints, categorization)
   - Constant data (demographics: age, sex)
   - Stable data (conditions, medications, triggers, relievers, allergies, clinical notes)
   - Data categorization framework (constant/stable/dynamic exclusions)
   - Manual update workflow specification
   - Read-only access patterns for LLM consumption

2. **Tracking Entry Schema Specification**
   - Entry type definitions (patient_state, meal, stool, sleep, exercise, stress_event, medication_taken)
   - Mandatory vs. optional field specifications per entry type
   - Controlled vocabularies for ALL categorical fields (stress levels, Bristol types, passage descriptors, completeness indicators, etc.)
   - Value set definitions with enumerated allowed values
   - Fixed schema keys (no runtime key invention)
   - Per-turn tracking payload envelope specification (delta array of 1+ entries)
   - Timestamp format and timezone handling

3. **Integration Specifications**
   - Probe triggering rules when mandatory tracking fields are missing
   - End-of-day aggregation format (collection of tracking entries)
   - Patient profile loading patterns (session initialization)
   - Cross-session persistence patterns (handoff to T810A3-REPORT)
   - Conflict resolution between ChatGPT memory and patient profile

4. **Validation & Quality Requirements**
   - Schema validation rules (prompt-engineering based, no programmatic validation)
   - Value set enforcement approach
   - Error handling patterns for missing/invalid data
   - Data quality criteria for clinical utility

### C. Out of Scope

- **Execution protocols** (T810A1-PROMPT responsibility)
- **UI/UX for manual patient profile updates** (future feature)
- **Automated validation logic** (ChatGPT platform constraint per `T810A1-CON-008`)
- **Cross-session reporting formats** (T810A3-REPORT responsibility)
- **Clinical knowledge sources** (T810A1-PROMPT S04 responsibility)
- **Protocol triggering logic** (T810A1-PROMPT NFR-008 responsibility)

---

## III. CONTEXT & RATIONALE

### A. Architectural Foundation: Patient Profile vs. Tracking Schema Split

**Original Research Assumption** (Phase 1):
- Single unified patient profile JSON
- Profile generated during conversation, output at end-of-day reporting

**Empirical Reality** (Phase 1.5 Conversation Analysis):
- Real conversation showed **cumulative JSON generation** (Turn 2 regenerated all previous entries)
- No distinction between persistent profile data vs. ephemeral tracking entries
- Mixed patient_state (profile-like) with meal/stool (tracking events) in same structure

**Client Directive** (Phase 1.5 Comment 1):
> "Instead of a single JSON file system, we will need multiple JSON files, at least starting with two: stable and dynamic."

**Architectural Decision**:
- **Patient Profile Schema**: Read-only patient profile data, manually updated, contains persistent clinical context
- **Tracking Payload**: LLM-generated per-turn JSON codeblock containing **1+ tracking entries** (delta-only output)

**Rationale**: ChatGPT platform constraint (read-only file access) necessitates separation between LLM-generated tracking payloads and patient-governed profile data.

### B. Primary Use Case: Tracking-First Workflow

**Client Directive** (Phase 1.5 Comment 0):
> "Primary use case of LLM_Gastro is currently usage for patient notes and tracking throughout the day... tracking + analysis (primary), probe (secondary), coach/summarize (tertiary)."

**Implication for T810A2-SCHEMA**:
- Tracking payload is the PRIMARY per-turn data artifact (generated multiple times per day)
- Patient profile schema is foundational context (loaded once per session, updated rarely)
- Schema design must optimize for rapid, consistent tracking entry generation
- Controlled vocabularies CRITICAL for pattern analysis across multiple entries

### C. Platform Constraints (ChatGPT Architecture)

**From T810A1-CON-008**:
- **File System**: LLM has read-only access; cannot write to patient profile data
- **Validation**: No programmatic validation; enforcement via prompt engineering only
- **Default Behavior**: ChatGPT Assistant mode requires explicit override via exemplars

**Implication for T810A2-SCHEMA**:
- Schema validation is **specification-based**, not programmatic
- Controlled vocabularies must be **explicitly enumerated** in Knowledge Base (Block 4)
- Value set enforcement relies on Execution Protocol (Block 5) instructions and Exemplars (Block 8)
- Risk of value drift without automated validation (logged as `T810A1-ISSUE-004`)

### D. Template-Driven Architecture Design Decision (v1.1.0 NEW)

**From T810A1 Phase 3.3A S05 Requirements Discovery**:

The shift to template-driven tracking fundamentally changes the **responsibility boundary** between S05 (Custom Instructions) and tracking schema templates (Project Knowledge):

**Architectural Principle**:
- **S05 Custom Instructions**: HIGH-LEVEL preface only — "Phase 1 generates structured tracking entry using template from Project Knowledge"
- **Tracking schema template (Project Knowledge)**: DETAILED instructional responsibility — template file IS the instruction manual
- **Rationale**: LLM_Gastro reads the template file and inherently knows how to generate JSON by following the template structure

**T810A2 Dual Responsibility**:
1. Define JSON **schemas** (field types, constraints, value sets)
2. Design **instructional templates** (self-documenting structure that teaches LLM how to generate entries)

**Open Design Question - Template Annotation Approach**:

**Option A: Inline Annotations/Comments**
- Templates include explanatory comments explaining generation rules
- Example: `"stress": "moderate" // Allowed values: none, low, moderate, high`
- Pros: Self-documenting within template file; LLM reads rules directly
- Cons: Adds verbosity to templates; may clutter structure

**Option B: Clean Exemplar Templates**
- Templates are clean JSON exemplars without comments
- Generation rules documented separately in T810A2 Request
- Pros: Clean, minimal template structure; easier to parse
- Cons: Separation between template and rules; relies on LLM inference

**Option C: Hybrid Approach (RECOMMENDED)**
- Minimal inline hints for complex/critical fields only
- Clean structure for straightforward fields
- Example: Add comment only for fields with strict controlled vocabularies or complex validation logic
- Pros: Balance between clarity and cleanliness
- Cons: Requires judgment on which fields need hints

**Responsibility Clarification**:
- **T810A2-SCHEMA**: Decides annotation approach and designs template structure (both inline hints if used)
- **T810A1-S08**: Creates concrete exemplar **dialogue outputs** (showing how LLM uses templates in conversation)
- **Integration**: Both approaches work together — templates teach structure, S08 shows usage in practice

**Recommendation**: Subconsultant should propose preferred approach in Request document with rationale. Checkpoint 0 consultation will validate decision before full schema development.

### E. Reference Examples for Template Design (v1.1.0 NEW)

**Example Tracking JSON** (headstart reference):
- **Path**: `prompt/artifacts/tasks/T810/resources/gastro_example_tracking.json`
- **Purpose**: High-level, NOT APPROVED example structure showing multi-day tracking pattern
- **Key Observations**:
  - Date-based organization with entries array
  - Entry types: stool, meal, patient_state, sleep, supplements, exercise
  - Field patterns: timestamp, label, bristol_type, features, trigger_context, notes
  - Metadata: confidence levels, controlled vocabularies
- **Use Case**: Starting point for template design; NOT final approved structure

**CareCare App Screenshots** (familiar UX pattern reference):
- **Path 1**: `prompt/artifacts/tasks/T810/resources/carecare_meal_tracking.jpeg`
  - Shows meal tracking structure: ingredients, time, tags
  - User-friendly labeling and categorization patterns
- **Path 2**: `prompt/artifacts/tasks/T810/resources/carecare_symptoms_tracking.jpeg`
  - Shows symptom tracking structure: digestion, pain, mental state
  - Controlled vocabulary examples (severity scales, descriptors)
- **Implication**: Tracking schema templates should mirror this familiar UX pattern for patient comfort
- **Integration**: Templates should feel like structured versions of CareCare's intuitive tracking interface

**Usage Guidance**:
- Review both resources before template design
- Extract controlled vocabulary patterns from gastro_example_tracking.json
- Align field naming and structure with CareCare UX familiarity
- Validate template clarity against these reference examples

---

## IV. REFERENCE MATERIALS

### A. Core Planning Documents

**Phase 1.5 Conversation Analysis** (PRIMARY SOURCE):
- **Path**: `prompt/artifacts/tasks/T810/consultant/plan/phase1.5_conversation_analysis.md`
- **Key Sections**:
  - Section II: Conversation Analysis (observations from real LLM_Gastro behavior)
  - Section III: Client Requirements Analysis (Comment 1: JSON architecture split)
  - Section VI: Phase 1.5 F-ID Proposals (INT-004, IF-006 specify T810A2 dependencies)
  - Section VIII: Sub-Consultant Brief Requirements (T810A2 feature outline)

**Phase 1.5 Request Update Proposals**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/plan/phase1.5_request_updates.md`
- **Key Sections**:
  - Section IV-B: INT-004 Complete Rewrite (Schema Split Architecture)
  - Section IV-C: IF-006 New F-ID (Tracking Payload Generation specifications)

**Phase 1-4 Consultancy Plan**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/plan/plan_T810A-PROMPT_phase1-4_v1.0.0.md`
- **Key Sections**:
  - Section III: Phase 1.5 (lines 97-170) - Conversation-Driven Refinement objectives
  - Section IX: Sub-Consultant Brief Requirements (lines 757-842)

**Example Conversation** (EMPIRICAL EVIDENCE):
- **Path**: `prompt/artifacts/tasks/T810/resources/gastro_example_conversation.md`
- **Critical Observations**:
  - Turn 1 JSON structure (patient_state, meal, stool entries)
  - Turn 2 cumulative JSON pattern (regenerated all previous entries)
  - Numeric confidence fields (`"confidence": 0.7`)
  - Value patterns for stress levels, Bristol types, passage descriptors

### B. Research Foundation

**Research Report** (SECONDARY SOURCE):
- **Path**: `prompt/artifacts/tasks/T810/research/report/report_prompt-architecture-clinical-validation_T810A_v1.0.0_i2.md`
- **Relevant Deliverable**: Deliverable E (Patient Profile Schema)
  - Validates constant/stable/dynamic categorization
  - Identifies missing demographic fields (age, sex) for clinical reasoning
  - Token efficiency recommendations (profile <200 tokens)

**Research Entry in Request**:
- Reference ID: `T810A1-RES-001` (Architecture validation)
- Reference ID: `T810A1-RES-002` (Conversation-driven empirical validation)

### C. Parent Request Document

**T810A1-PROMPT Request Document**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md`
- **Key Dependencies**:
  - Section E: DEP-004 (Patient Data Structures dependency on T810A2)
  - Section F: NFR-001 (Protocol hierarchy - tracking primary)
  - Section G: IF-006 (Tracking Payload Generation requirements)
  - Section H: CON-008 (ChatGPT Architectural Constraints)
  - Section I: INT-004 (Patient Data Architecture - schema split)
  - Section N: RES-002 (Conversation-Driven Empirical Validation)

### D. Framework Standards (T102)

**T102 Concept Document** (GOVERNANCE):
- **Path**: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
- **Relevant ADRs**:
  - T102-ADR-001: Consultancy Operating Model (Request structure)
  - T102-ADR-002: Canonical YAML Header (frontmatter requirements)
  - T102-ADR-003: Explicit Inheritance Model (ID referencing rules)
  - T102-ADR-004: Decision Records Index (GDR/ADR format)
  - T102-ADR-005: ID Specification & Rules (F-ID construction patterns)

---

## V. REQUIREMENTS SUMMARY

### A. Patient Profile Schema Requirements

**High-Level Specification from T810A1-INT-004**:
```
Contains constant patient data (demographics, conditions, medications, triggers,
relievers, clinical history notes)

- Stored in Knowledge Base (Block 4), manually updated by patient outside conversation
- Read-only for LLM_Gastro (ChatGPT file system constraint: no write permissions)
- Loaded at session start per Execution Protocol (Block 5)
```

**Required Field Categories** (from Phase 1 Research + Phase 1.5 Analysis):

1. **Constant Fields** (never change):
   - `age` (integer or age range)
   - `sex` (categorical: male/female/other/prefer_not_to_say)

2. **Stable Fields** (change infrequently):
   - `conditions` (array of diagnosed GI conditions)
   - `medications` (array of current medications with dosage)
   - `supplements` (array of supplements)
   - `allergies` (array of known allergies)
   - `triggers` (array of known symptom triggers)
   - `relievers` (array of known symptom relievers)
   - `notes` (freeform clinical history notes)
   - `last_updated` (ISO 8601 timestamp)

3. **Dynamic Exclusions** (NOT in patient profile schema):
   - Daily symptoms (captured as tracking entries in the tracking payload)
   - Meals (captured as tracking entries in the tracking payload)
   - Stool events (captured as tracking entries in the tracking payload)
   - Sleep data (captured as tracking entries in the tracking payload)

**Specification Depth Required**:
- JSON schema structure with field types and constraints
- Categorical field value sets (e.g., `conditions` allowed values)
- Array vs. object structure decisions
- Null handling and optional field rules
- Token efficiency optimization (target: <200 tokens per profile)
- Manual update workflow documentation

### B. Tracking Entry Schema Requirements

**High-Level Specification from T810A1-IF-006**:
```
LLM_Gastro generates a per-turn tracking payload (single fenced `json` codeblock)
containing 1+ entry objects inferred from the user's current message (delta-only):
patient_state, meal, stool, sleep, or other clinically relevant observations

- Uses structured keys with controlled vocabularies (value sets defined in T810A2)
- Fixed schema keys (no runtime key invention)
- Schema templates stored in Knowledge Base as generation exemplars
```

**Required Entry Types** (minimum support from IF-006):

1. **`patient_state` Entry Type**:
   ```
   mental:
     - stress: [controlled vocabulary required]
     - mood: [controlled vocabulary required]
   digestion:
     - bloating: [controlled vocabulary required]
     - tummy_pain: [controlled vocabulary required]
   pain:
     - headache: [controlled vocabulary required]
     - other_pain: [controlled vocabulary required]
   ```

2. **`meal` Entry Type**:
   ```
   time: [ISO 8601 timestamp]
   items: [array of food items]
   fluids: [array of beverages]
   pre_meal_prokinetics: [optional boolean or medication name]
   notes: [optional freeform text]
   ```

3. **`stool` Entry Type**:
   ```
   time: [ISO 8601 timestamp]
   bristol_type: [1-7 integer or "Type 1", "Type 2" format]
   features: [controlled vocabulary required - e.g., "mucus", "undigested_food"]
   passage: [controlled vocabulary required - e.g., "urgent", "normal", "difficult"]
   completeness: [controlled vocabulary required - e.g., "complete", "incomplete"]
   wipe: [controlled vocabulary required - number of wipes or descriptor]
   trigger_context: [optional freeform text]
   confidence: [optional numeric 0-1 for internal tracking]
   ```

4. **`sleep` Entry Type**:
   ```
   time: [ISO 8601 timestamp - sleep start time]
   duration_hours: [numeric]
   notes: [optional freeform text]
   ```

5. **Flexible Entry Types** (patient/LLM can add):
   - `exercise`
   - `stress_event`
   - `medication_taken`
   - Other clinically relevant events

**Controlled Vocabulary Examples from Conversation**:
```
From Turn 1 patient_state:
  mental.stress: ["none", "low/relaxed", "moderate", "high"]
  mental.mood: ["so-so", "light, improved", "frustrated", "calm"]
  digestion.bloating: ["none", "minimal", "moderate", "severe"]

From Turn 1 stool:
  bristol_type: [1, 2, 3, 4, 5, 6, 7] or ["Type 1", "Type 2", ...]
  passage: ["urgent", "normal", "difficult", "painful"]
  completeness: ["complete", "incomplete"]
  features: ["mucus", "undigested_food", "blood", "oil", "normal"]
```

**Specification Depth Required**:
- Complete JSON schema for each entry type
- Exhaustive controlled vocabularies for ALL categorical fields
- Mandatory vs. optional field rules per entry type
- Fixed schema keys per entry type (no runtime key invention)
- Timestamp format specification (ISO 8601, Europe/Copenhagen timezone)
- Per-turn delta output rules (NOT cumulative across turns)
- Multiple entries per turn allowed (1+ entries in a single tracking payload)
- Null/missing value handling patterns

### C. Integration Pattern Requirements

**From Phase 1.5 Conversation Analysis - Comment 1 Patterns**:

**Pattern A: Missing Key → Probe Triggering**
- When mandatory tracking keys cannot be inferred from patient input
- Agent SHALL generate entry with `null` or omit key
- Missing keys trigger Probe phase (ask clarifying questions to complete entry)
- Integration point with T810A1-NFR-009 (Probe Phase Enforcement)

**Pattern B: End-of-Day Aggregation**
- End-of-day reporting = collection of ALL tracking entries from session tracking payloads
- Format: Array of entry objects, chronologically ordered
- Integration point with T810A1-INT-002 (Memory Handoff Protocol)

**Pattern C: Session Initialization**
- Patient profile schema loaded at conversation start (Step 1 after memory review)
- Tracking entry schema templates loaded for generation reference
- Integration point with T810A1-INT-005 (Memory Review Protocol)

**Conflict Resolution Pattern**:
- ChatGPT Memory vs. patient profile schema discrepancies
- **Patient profile schema takes precedence** as single source of truth
- Flag discrepancy in Probe phase: "I notice in my memory you mentioned [X], but your profile shows [Y]. Has this changed?"

**Specification Depth Required**:
- Probe triggering conditions (which keys are mandatory vs. optional per entry type)
- End-of-day aggregation JSON structure
- Session initialization sequence specification
- Conflict detection and resolution phrasing examples

### C. Probe Triggering Specifications (v1.1.0 NEW - S05 Integration)

**From T810A1 Phase 3.3A S05-FR-002 (Probe Phase Enforcement)**:

Phase 3 (Probe & Engage) depends on missing mandatory tracking keys to trigger clarifying questions. T810A2 must specify which fields are mandatory vs. optional per entry type, and map these to Probe question types.

**Research-Validated Question Framework** (from T810A1-RES-002):
- Research will discover optimal questioning framework (NOT fixed 5-question pattern)
- Likely distribution (client's working hypothesis; research may adjust):
  - **Type 1-2**: Tracking JSON gaps (data completeness) — 1-2 questions
  - **Type 3**: Patient history (longitudinal patterns from patient profile data + Memory) — 1 question
  - **Type 4-5**: Immediate/recent context (current episode from unstructured input + images) — 1-2 questions
  - **Type 6**: Future planning (anticipatory context) — 1 question

**T810A2 Responsibility - Mandatory/Optional Field Mapping**:

For each tracking entry type, specify:

1. **Mandatory Fields** (missing triggers Probe):
   - List all fields that MUST be populated for clinical utility
   - Example: `patient_state.mental.stress` (mandatory) → If missing, triggers Type 1 Probe question
   - Example: `stool.completeness` (mandatory) → If missing, triggers Type 1 Probe question

2. **Optional Fields** (missing does NOT trigger Probe):
   - List all fields that are nice-to-have but not critical
   - Example: `meal.trigger_context` (optional) → If missing, may trigger Type 4-5 Probe if relevant to immediate context

3. **Field-to-Question-Type Mapping**:
   - Map each mandatory field to appropriate Probe question type (Type 1-6)
   - Example mapping table:

| Entry Type | Mandatory Field | Question Type | Rationale |
|:-----------|:----------------|:--------------|:----------|
| `patient_state` | `mental.stress` | Type 1 (tracking gap) | Essential for pattern analysis; cannot be inferred from images |
| `stool` | `bristol_type` | Type 1 (tracking gap) | Core classification; may require patient confirmation if image unclear |
| `stool` | `completeness` | Type 1 (tracking gap) | Clinical significance (incomplete evacuation patterns) |
| `stool` | `wipe` | Type 1 (tracking gap) | Indicates digestive efficiency |
| `meal` | `trigger_context` | Type 4 (immediate context) | Optional but enhances pattern recognition |

4. **Exemplar Probe Questions** (for S08 coordination):
   - For each mandatory field when missing, provide exemplar Probe question
   - Example: If `patient_state.mental.stress` missing → "How would you describe your stress level today? (none, low, moderate, high)"
   - Example: If `stool.completeness` missing → "Did you feel like you completely emptied your bowels, or was it a partial evacuation?"

**Specification Depth Required**:
- Exhaustive mandatory/optional field lists per entry type
- Field-to-question-type mapping table
- Exemplar Probe questions for all mandatory fields
- Integration with research-validated optimal question count (NOT hardcoded to 5)

**Coordination Point**:
- T810A2 provides field specifications
- T810A1-RES-002 validates optimal question framework
- T810A1-S08 creates concrete dialogue exemplars using both inputs

---

## VI. KNOWN ISSUES & RISKS (from T810A1)

### A. Open Issues

**ISSUE-001: Schema Split Architecture Dependency** (High Priority)
- T810A1-PROMPT Phase 2-3 Story development depends on T810A2 schema completion
- Surface-level references in T810A1 may need adjustment based on T810A2 final schemas
- **Mitigation**: Parallel development with coordination checkpoints

**ISSUE-004: Controlled Vocabulary Validation** (Medium Priority)
- Tracking payload generation requires consistent value sets (stress levels, Bristol types)
- ChatGPT provides no programmatic validation
- Enforcement relies entirely on S05 execution protocol instructions and S08 exemplars
- Risk of value drift over time without automated validation
- **Dependency**: T810A2 must provide EXHAUSTIVE controlled vocabularies

### B. Accepted Risks

**RISK-002: T810A2-SCHEMA Development Delays** (Medium/ACCEPTED)
- Risk that T810A2 development delays T810A1 S04-S10 specification
- **Mitigation**: Surface-level schema/payload references allow parallel development; detailed schemas not blocking for Phase 2

**RISK-005: Patient Profile Manual Update Friction** (Low/ACCEPTED)
- Requiring manual patient updates to patient profile data creates friction and profile staleness
- **Mitigation**: INT-005 memory review protocol flags discrepancies; Probe phase can elicit updates; document manual update workflow in T810A2

---

## VII. DELIVERABLE SPECIFICATION

### A. Required Artifact

**Document**: `request_T810A2-SCHEMA.md`

**Structure** (following T102-ADR-001-FR-002):

```markdown
---
artifact_type: 'REQUEST'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2'
feature_code: 'PATIENT'
version: '1.0.0'
date: '2025-10-11'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# REQUEST: Patient Data Structures - T810A2 (PATIENT)

## I. EXECUTIVE SUMMARY

## II. TABLE OF CONTENTS

## III. CORE CONTENT

### A. Feature Solution Framework
### B. Source & Scope
### C. Business Objectives & Success Signals
### D. Stakeholders
### E. Inheritances, Assumptions & Dependencies
### F. Non-Functional Requirements
### G. Interfaces & Data
### H. Constraints
### I. Feature Integration Notes
### J. Stories & Specification

#### 1. Story T810A2-S01 — Patient Profile Schema
**Purpose**: Define complete patient profile schema with constant/stable field categorization

**Functional Requirements**:
- FR-001: Constant field specifications (age, sex)
- FR-002: Stable field specifications (conditions, medications, triggers, relievers)
- FR-003: Schema structure and data types
- FR-004: Token efficiency optimization (<200 tokens)
- FR-005: Manual update workflow

**Acceptance Criteria**: [Gherkin format]

#### 2. Story T810A2-S02 — Tracking Entry Schema (patient_state)
**Purpose**: Define patient_state entry type with controlled vocabularies

**Functional Requirements**:
- FR-001: Mental state fields (stress, mood) with value sets
- FR-002: Digestion fields (bloating, tummy_pain) with value sets
- FR-003: Pain fields (headache, other_pain) with value sets
- FR-004: Timestamp and metadata fields

**Acceptance Criteria**: [Gherkin format]

#### 3. Story T810A2-S03 — Tracking Entry Schema (meal)
#### 4. Story T810A2-S04 — Tracking Entry Schema (stool)
#### 5. Story T810A2-S05 — Tracking Entry Schema (sleep)
#### 6. Story T810A2-S06 — Flexible Schema Extension Rules
#### 7. Story T810A2-S07 — Controlled Vocabularies Register
#### 8. Story T810A2-S08 — Integration Patterns
#### 9. Story T810A2-S09 — Validation & Quality Requirements

### K. Acceptance Criteria Register
### L. Open Issues & Risks
### M. Feature GDRs (if any governance decisions needed)
### N. Research & Notes

## V. APPENDIX
## VI. VALIDATION CHECKLIST
## VII. STAKEHOLDER SIGN-OFF
## VIII. NEXT STEPS
## IX. CHANGELOG
```

### B. Content Depth Requirements

**Story Specification**:
- Each story (S01-S09) SHALL have 3-7 functional requirements (F-IDs)
- All F-IDs SHALL follow pattern `T810A2-S##-FR-###`
- All requirements SHALL have Gherkin-format acceptance criteria (Given/When/Then)
- **Critical**: ALL categorical fields SHALL have EXHAUSTIVE controlled vocabularies specified

**Schema Documentation**:
- Provide schema examples for the patient profile schema and each tracking entry type
- Document field types, constraints, mandatory/optional status
- Specify null handling and validation rules (prompt-engineering based)

**Integration Specifications**:
- Document Probe triggering rules (which missing keys trigger clarifying questions)
- Specify end-of-day aggregation format
- Define session initialization pattern
- Provide conflict resolution examples

### C. Quality Criteria

1. **Completeness**: All field types, value sets, and integration patterns fully specified
2. **Traceability**: Clear references to T810A1-PROMPT dependencies (INT-004, IF-006, NFR-009)
3. **Usability**: Sub-consultant without prior context can implement from specifications alone
4. **Consistency**: Follows T102 consultancy framework (ADR-001 through ADR-005)
5. **Clinical Utility**: Schema supports pattern analysis and clinician handoff use cases

---

## VIII. COLLABORATION PATTERN

### A. Parallel Development Workflow

**T810A1-PROMPT Consultant** (Primary):
- Maintains surface-level schema split architecture references in Request document
- References T810A2 for detailed schemas ("detailed schema deferred to T810A2")
- Continues Phase 2-3 development (GDR creation, Story S04-S10 specification)

**T810A2-SCHEMA Sub-Consultant** (You):
- Develops complete Request document with exhaustive schema specifications
- Provides controlled vocabularies for ALL categorical fields
- Documents integration patterns and validation rules

### B. Coordination Checkpoints

**Checkpoint 1: Initial Schema Draft** (Target: 2-3 hours after handoff)
- Share Stable JSON schema draft for review
- Share patient_state entry type schema draft
- Identify any blocking questions or ambiguities

**Checkpoint 2: Complete Schema Review** (Target: 5-6 hours after handoff)
- Share complete Request document draft
- Review integration patterns for consistency with T810A1-PROMPT
- Validate controlled vocabularies against conversation example

**Checkpoint 3: Final Approval Gate** (Target: 7-8 hours after handoff)
- Client reviews complete T810A2 Request
- T810A1 consultant validates integration points
- Approve for implementation handoff

### C. Communication Protocol

- **Questions/Clarifications**: Direct to T810A1-PROMPT consultant (include reference to this handoff brief)
- **Blocking Issues**: Escalate to Client (Decision Owner) with impact assessment
- **Status Updates**: Provide brief progress update at each checkpoint

---

## IX. SUCCESS CRITERIA

**T810A2-SCHEMA Request Development Complete When**:
- [ ] Complete Request document with 9 stories (S01-S09) fully specified
- [ ] All story functional requirements have Gherkin acceptance criteria
- [ ] Stable JSON schema fully documented with field types, constraints, categorization
- [ ] All 5 Dynamic JSON entry types (patient_state, meal, stool, sleep, flexible) fully documented
- [ ] EXHAUSTIVE controlled vocabularies provided for ALL categorical fields
- [ ] Integration patterns (Probe triggering, aggregation, initialization, conflict resolution) fully specified
- [ ] Validation and quality requirements documented
- [ ] No blocking dependencies on T810A1-PROMPT for Request completion
- [ ] Client approval obtained for T810A2-SCHEMA Request document

---

## X. CLARIFYING QUESTIONS FOR SUB-CONSULTANT

Before proceeding, please confirm understanding and raise any questions:

1. **Scope Clarity**: Is the distinction between T810A2 responsibilities (data schemas) vs. T810A1 responsibilities (execution protocols) clear?

2. **Controlled Vocabularies**: Do you have sufficient examples from the conversation to extrapolate complete value sets, or do you need additional guidance on vocabulary completeness?

3. **Schema Complexity**: Should Stable JSON fields like `conditions`, `medications`, `triggers` be simple string arrays, or structured objects with additional metadata (e.g., dosage, frequency)?

4. **Flexible Entry Types**: How many additional entry types beyond the 4 minimum (patient_state, meal, stool, sleep) should be pre-specified vs. left as "LLM MAY add if clinically justified"?

5. **Validation Depth**: How detailed should prompt-engineering validation rules be (e.g., "Bristol type must be integer 1-7" vs. more nuanced field interdependencies)?

6. **Timeline**: Does the 7-8 hour target timeline with 3 checkpoints align with your availability and working pace?

---

## XI. APPENDIX

### A. Key Term Definitions

**Stable JSON**: Read-only patient profile containing constant and stable data, manually updated by patient outside conversation, loaded at session start.

**Dynamic JSON**: LLM-generated single tracking entry per patient interaction, containing ephemeral event data (symptoms, meals, stools, sleep).

**Controlled Vocabulary**: Exhaustive enumeration of allowed values for a categorical field (e.g., stress levels: ["none", "low", "moderate", "high"]).

**Probe Triggering**: When missing mandatory Dynamic JSON keys trigger LLM to ask clarifying questions before proceeding to Coach phase.

**Single-Entry Model**: LLM generates ONE JSON object per patient input, NOT cumulative across conversation turns.

### B. Conversation Example Key Observations

**Turn 1 JSON Structure** (lines 46-121):
```json
{
  "patient_state": {
    "time": "2025-03-04T07:50:00+01:00",
    "mental": {"stress": "moderate", "mood": "so-so"},
    "digestion": {"bloating": "minimal", "tummy_pain": "none"},
    "confidence": 0.7
  },
  "meal": {
    "time": "2025-03-04T08:00:00+01:00",
    "items": ["black tea", "GF porridge", ...],
    "notes": "..."
  },
  "stool": {
    "time": "2025-03-04T10:00:00+01:00",
    "bristol_type": "5-6",
    "features": ["urgent", "mucus", "undigested food visible"],
    "passage": "urgent",
    "completeness": "incomplete feeling",
    "wipe": "many (>10) wipes",
    "confidence": 0.7
  }
}
```

**Turn 2 JSON Pattern** (lines 165-221):
- Regenerated ALL Turn 1 entries PLUS 3 new entries
- Anti-pattern: cumulative log instead of single-entry model
- T810A2 specification must prevent this pattern

### C. Client Directives Summary

**Comment 0**: Tracking + analysis primary, probe secondary, coach/summarize tertiary
**Comment 1**: Stable read-only JSON + Dynamic generative JSON split
**Comment 1.1**: Define concrete controlled vocabularies; no validation capability in ChatGPT
**Comment 1.2**: Sub-consultant needed for T810A2-SCHEMA feature
**Comment 2**: Patient controls GPT thinking mode toggle
**Comment 3**: Smart protocol triggering like VPA pattern
**Comment 4**: Probe phase mandatory, minimum 2-loop pattern, Consultant/Analyst default mode
**Comment 5**: Always review ChatGPT cross-session memory first

---

**Document Status**: Draft
**Approval Required**: Sub-Consultant acknowledgment of handoff before proceeding
**Next Review**: Checkpoint 1 (Initial Schema Draft) at +2-3 hours

---

## XII. CHANGELOG

- **v1.0.0** (2025-10-11): Initial handoff brief creation for T810A2-SCHEMA parallel development, integrating Phase 1.5 conversation analysis findings, client directives, and T810A1-PROMPT dependency specifications
