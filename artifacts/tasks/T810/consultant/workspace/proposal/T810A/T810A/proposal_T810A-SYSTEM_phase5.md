---
artifact_type: 'PROPOSAL'
initiative_id: 'T810'
epic_id: 'T810A'
version: '1.0.0'
date: '2025-11-08'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_document: 'plan_T810A-SYSTEM_migration.md'
target_section: 'Section 5.5 (T810A1 Delta Specification Review)'
update_notes: 'Extracted from Phase 6 proposal to align with Phase 5 coordination scope'
---

# PHASE 5: T810A1 DELTA SPECIFICATION REVIEW

## I. SECTION 5.5: T810A1 DELTA SPECIFICATION REVIEW

### Context

This subsection defines what remains in T810A1 Request as feature-specific after promoting 20+ E-RIDs to Epic scope. Clear delta specification prevents duplication and ensures proper inheritance pattern.

### Analysis Questions

#### AQ-1: After Promoting 20+ E-RIDs, What F-RIDs Remain Unique to T810A1?

**Expected T810A1 Feature-Specific Content** (preliminary list):

**Feature Stories (S01-S10):**
- **S01**: Project Context (9-block implementation specifics)
- **S02**: Role Identity (Consultant/Analyst persona implementation)
- **S03**: Toolbox (deferred to T810A4 per Epic DEP-003)
- **S04**: Knowledge Base (GI knowledge sources per Epic GDR-005)
- **S05**: Execution Protocol (5-phase protocol implementation)
- **S06**: Behavioral Guardrails (no-guessing enforcement per Epic QG-008)
- **S07**: Quality Criteria (NFR implementations per Epic QGs)
- **S08**: Exemplars (prompt-specific examples)
- **S09**: I/O Specification (JSON formats per Epic IG-004)
- **S10**: Integration (cross-feature coordination per Epic IGs)

**Feature-Specific Interfaces (F-IFs):**
- **T810A1-IF-001** (Input Interface): Unstructured text + images input handling
- **T810A1-IF-002** (Output Interface): Conversational output format
- **T810A1-IF-003** (Explicit Classification): Bristol Chart classification implementation (inherits Epic IG-003)
- **T810A1-IF-004** (Reporting Trigger): "/report" command detection (inherits Epic IG-001)
- **T810A1-IF-005** (Session Context Injection): Report loading at session start (inherits Epic IG-006)
- **T810A1-IF-006** (Dynamic JSON Generation): Single-entry JSON format (inherits Epic IG-004)

**Feature-Specific Integration Notes (F-INTs):**
- **T810A1-INT-001** (Internal State Object): Conversation-scoped state management
- **T810A1-INT-002** (Memory Handoff Protocol): Dual-format report generation (inherits Epic IG-006)
- **T810A1-INT-003** (User-Mediated Workflow): Patient-mediated data transfers per Epic CON-001
- **T810A1-INT-004** (Patient Data Architecture): Stable/Dynamic JSON split implementation (inherits Epic GDR-003, IG-004)
- **T810A1-INT-005** (Memory Review Protocol): Step 0 memory scan implementation (inherits Epic IG-005)

**Feature-Specific Assumptions (F-ASSUMs):**
- **T810A1-ASSUM-004** (Session-Scoped Memory Model): Hybrid split — A1's implementation assumption (inherits Epic ASSUM-004 principle)

**Feature-Specific Dependencies (F-DEPs):**
- **T810A1-DEP-008** (Protocol Triggering Research): VPA-style trigger research (demoted from Epic consideration)

**Feature-Specific Constraints (F-CONs):**
- **T810A1-CON-002** (Risk Acceptance): User agreement statement
- **T810A1-CON-003** (Open Knowledge Base): General training + search tools
- **T810A1-CON-005** (Tooling Deferral): MVP tool ecosystem (redundant with Epic DEP-003/CON-001)

**Feature-Specific NFRs (F-NFRs):**
- **T810A1-NFR-001** (5-Phase Protocol Execution): Tracking → Analyze → Probe → Coach → Summarize (inherits Epic QG-001)
- **T810A1-NFR-002** (Protocol Phase Tone Mapping): 6 specific phase tones (inherits Epic QG-002)
- **T810A1-NFR-005** (9-Block Prompt Structure): Compositional prompt framework (inherits Epic QG-005)
- **T810A1-NFR-008** (Protocol Triggering Intelligence): 3-way input detection (related to Epic IG-001)
- **T810A1-NFR-009** (Probe-Before-Answer Enforcement): ≥2 questions minimum (inherits Epic QG-008, IG-002)

#### AQ-2: Which Stories (S01-S10) Reference Promoted E-RIDs That Now Need Inheritance References?

**Story** | **Current F-RID References** | **Promoted to E-RIDs** | **Inheritance Updates Required**
:---|:---|:---|:---
S01 (Project Context) | Implicit references to Epic dossier | — | Add "Inherited Considerations" table referencing Epic E-RIDs
S02 (Role Identity) | T810A1-NFR-002 (Persona) | → T810A-QG-002 | Reference Epic QG-002; retain A1-NFR-002 as delta
S05 (Execution Protocol) | T810A1-NFR-001 (Protocol), NFR-008 (Triggering), NFR-009 (Probing) | → T810A-QG-001, IG-001, QG-008, IG-002 | Reference Epic QG-001/QG-008/IG-001/IG-002; retain A1 implementations
S06 (Behavioral Guardrails) | T810A1-CON-004 (No-Guessing) | → T810A-QG-008 | Reference Epic QG-008; retain A1-NFR-009 enforcement
S07 (Quality Criteria) | T810A1-NFR-001 through NFR-009 | → T810A-QG-001/002/003/004/005/006/007/008 | Reference Epic QGs; retain A1 NFR implementations
S08 (Exemplars) | Implicit quality standards | → T810A-QG-* | Ensure exemplars demonstrate Epic QG compliance
S09 (I/O Specification) | T810A1-IF-006 (Dynamic JSON) | → T810A-IG-004 | Reference Epic IG-004; retain A1-IF-006 schema details
S10 (Integration) | T810A1-INT-002/004/005 | → T810A-IG-004/005/006 | Reference Epic IGs; retain A1 INT implementation notes

#### AQ-3: Are There T810A1-Specific Constraints/Assumptions Not Appropriate for Epic But Critical for A1?

**Feature-Specific Items NOT Promoted (remain at T810A1):**
- **T810A1-ASSUM-004**: Session-scoped memory approach (implementation of Epic ASSUM-004 principle)
- **T810A1-DEP-008**: Protocol triggering research (demoted from Epic)
- **T810A1-CON-002**: Risk acceptance user agreement
- **T810A1-CON-003**: Open Knowledge Base approach
- **T810A1-CON-005**: MVP tooling deferral (redundant with Epic DEP-003/CON-001, consider removal)

**Validation:** All feature-specific items are correctly scoped to A1; no missing constraints/assumptions identified.

### Deliverable: T810A1 Delta Specification Outline

**T810A1 Request Document Structure (Post-Migration):**

1. **Feature Overview**
   - Purpose: Conversational clinical tracking agent for gastrointestinal symptom analysis
   - Relationship to Epic: First feature of T810A, demonstrates Epic governance patterns

2. **Inherited Considerations Table** (NEW SECTION)
   ```markdown
   ### Inherited Considerations

   The following Epic-level Requirements and Considerations (E-RIDs) from `T810A (GASTRO)` apply to this feature:

   | Category | E-RID | Title | Application Notes |
   |:---------|:------|:------|:------------------|
   | ASSUM | T810A-ASSUM-001 | Patient Profile | Conversational agent assumes engaged patient |
   | ASSUM | T810A-ASSUM-002 | Input Modality & Quality | Text+images for symptom tracking |
   | ASSUM | T810A-ASSUM-003 | LLM Capability | Multimodal LLM for Bristol Chart + clinical reasoning |
   | ASSUM | T810A-ASSUM-004 | Platform Memory Uncertainty | Addressed via session-scoped approach (see T810A1-ASSUM-004) |
   | DEP | T810A-DEP-001 | Platform | ChatGPT multimodal LLM platform |
   | DEP | T810A-DEP-002 | Long-term Analysis | T810A3 provides cross-session pattern analysis |
   | DEP | T810A-DEP-003 | Toolbox Interface | T810A4 manages custom tool declarations |
   | DEP | T810A-DEP-004 | Patient Data Structures | T810A2 defines schemas for Dynamic JSON |
   | DEP | T810A-DEP-005 | Clinical Safety Framework | Deferred to future development per Epic scope |
   | CON | T810A-CON-001 | System Prompt Scope | Deliverable is system prompt only |
   | CON | T810A-CON-002 | Platform Compatibility | ChatGPT governance compliance required |
   | CON | T810A-CON-003 | Clinical Compliance Deferral | Regulatory compliance out of MVP scope |
   | CON | T810A-CON-004 | ChatGPT Architectural Constraints | File access, validation, Assistant mode override constraints |
   | QG | T810A-QG-001 | Clinical Protocol Reliability | Implemented via 5-phase protocol (see T810A1-NFR-001) |
   | QG | T810A-QG-002 | Persona & Tone | Implemented via protocol phase tone mapping (see T810A1-NFR-002) |
   | QG | T810A-QG-003 | Performance | 30-120s latency acceptable for consultant-level analysis |
   | QG | T810A-QG-004 | Holistic Analysis | Adjacent factors incorporated in Analyze phase |
   | QG | T810A-QG-005 | Architecture Maintainability | Implemented via 9-block structure (see T810A1-NFR-005) |
   | QG | T810A-QG-006 | Usability | Medium GI literacy + plain language explanations |
   | QG | T810A-QG-007 | Confidence Communication | Qualitative confidence descriptors (see T810A1-IF-003) |
   | QG | T810A-QG-008 | Clarification Over Guessing | Implemented via Probe phase enforcement (see T810A1-NFR-009) |
   | IG | T810A-IG-001 | Protocol Triggering Guidance | Implemented via 3-way input detection (see T810A1-NFR-008) |
   | IG | T810A-IG-002 | Probe Phase Enforcement | ≥2 clarifying questions before coaching (see T810A1-NFR-009) |
   | IG | T810A-IG-003 | Explicit Classification | Bristol Chart classification with confidence (see T810A1-IF-003) |
   | IG | T810A-IG-004 | Dynamic JSON Single-Entry Pattern | Single entry per interaction (see T810A1-IF-006) |
   | IG | T810A-IG-005 | Memory Review Protocol | Step 0: Memory Review (see T810A1-INT-005) |
   | IG | T810A-IG-006 | Session Context Injection & Handoff | Dual-format reports (see T810A1-INT-002) |
   ```

3. **Feature-Specific Requirements** (Delta Content Only)
   - **Assumptions**: T810A1-ASSUM-004 (Session-Scoped Memory Model)
   - **Dependencies**: T810A1-DEP-008 (Protocol Triggering Research)
   - **Constraints**: T810A1-CON-002/003/005 (feature-specific boundaries)
   - **Functional Requirements (S01-S10)**: 10 Stories with 9-block implementation details
   - **Non-Functional Requirements (NFRs)**: T810A1-NFR-001/002/005/008/009 (implementations of Epic QGs)
   - **Interfaces (IFs)**: T810A1-IF-001 through IF-006 (feature-specific interfaces)
   - **Integration Notes (INTs)**: T810A1-INT-001 through INT-005 (implementation details)

4. **GDR References** (Feature-Level Interpretations)
   - How T810A1 implements Epic GDR-001 through GDR-006 governance decisions

5. **Testing & Validation** (Feature-Specific)
   - Test strategies for Epic QG compliance at feature level

### Deliverable Summary

**Post-Migration T810A1 Content Distribution:**
- **Inherited from Epic**: 27 E-RIDs (4 ASSUM, 5 DEP, 4 CON, 8 QG, 6 IG)
- **Feature Delta**: ~30 F-RIDs (1 ASSUM, 1 DEP, 3 CON, 10 FRs [Stories], 5 NFRs, 6 IFs, 5 INTs)
- **Ratio**: ~50% Epic inheritance, ~50% feature-specific delta

**Key Pattern**: T810A1 becomes significantly leaner by referencing Epic governance via Inherited Considerations table, focusing delta content on 9-block implementation specifics.

---

## II. T810A1 REQUEST BASELINE ANALYSIS

### A. Current T810A1 Request Structure

**Document analyzed**: `request_T810A1-PROMPT.md` (version 1.0.0, dated 2025-10-05)

**Current Section Structure**:
- **Section III.A**: Feature Solution Framework (Problem Recap, Decision Criteria)
- **Section III.B**: Source & Scope
- **Section III.C**: Business Objectives & Success Signals
- **Section III.D**: Stakeholders
- **Section III.E**: Inheritances, Assumptions & Dependencies
- **Section III.F**: Non-Functional Requirements (NFRs)
- **Section III.G**: Interfaces & Data (IFs)
- **Section III.H**: Constraints (CONs)
- **Section III.I**: Feature Integration Notes (INTs)
- **Section III.J**: Stories & Specification (S01-S09)
- **Section III.K**: Acceptance Criteria Register
- **Section III.L**: Open Issues & Risks
- **Section III.M**: Research & Notes
- **Section Appendix.A**: Amendment Log

### B. F-RID→E-RID Detailed Mapping (Based on Actual Request Content)

#### Assumptions (4 total in T810A1 Request)

| Current F-RID | Title (from Request) | Epic Mapping | Status | Notes |
|:--------------|:---------------------|:-------------|:-------|:------|
| T810A1-ASSUM-001 | Patient Profile | → T810A-ASSUM-001 | PROMOTED | Direct text match |
| T810A1-ASSUM-002 | Input Modality & Quality | → T810A-ASSUM-002 | PROMOTED | Direct text match |
| T810A1-ASSUM-003 | LLM Capability | → T810A-ASSUM-003 | PROMOTED | Direct text match |
| T810A1-ASSUM-004 | Memory Model | → T810A-ASSUM-004 | HYBRID | Epic: "Platform Memory Uncertainty" (principle); Feature: "Session-Scoped Memory Model" (implementation) |

**Post-Migration T810A1 ASSUM Content**:
- **RETAIN**: T810A1-ASSUM-004 (Session-Scoped Memory Model) — Feature-specific implementation detail
- **DELETE**: T810A1-ASSUM-001/002/003 — Now inherited from Epic via Inherited Considerations table

---

#### Dependencies (6 total in T810A1 Request: DEP-001 through DEP-005, DEP-008)

| Current F-RID | Title (from Request) | Epic Mapping | Status | Notes |
|:--------------|:---------------------|:-------------|:-------|:------|
| T810A1-DEP-001 | Platform | → T810A-DEP-001 | PROMOTED | "Availability of multimodal LLM..." |
| T810A1-DEP-002 | Long-term Analysis | → T810A-DEP-002 | PROMOTED | Future `T810A3 (REPORT)` dependency |
| T810A1-DEP-003 | Toolbox Interface | → T810A-DEP-003 | PROMOTED | Future `T810A4 (TOOLS)` dependency |
| T810A1-DEP-004 | Patient Profile | → T810A-DEP-004 | PROMOTED | Request: "Patient Profile"; Epic: "Patient Data Structures" (title refined) |
| T810A1-DEP-005 | Clinical Safety Framework | → T810A-DEP-005 | PROMOTED | Direct text match |
| T810A1-DEP-008 | Protocol Triggering Research | DEMOTED | FEATURE-SPECIFIC | VPA-style trigger research; not cross-feature applicable |

**Post-Migration T810A1 DEP Content**:
- **RETAIN**: T810A1-DEP-008 (Protocol Triggering Research) — Feature-specific research dependency
- **DELETE**: T810A1-DEP-001/002/003/004/005 — Now inherited from Epic

---

#### Constraints (8 total in T810A1 Request: CON-001 through CON-008)

| Current F-RID | Title (from Request) | Epic Mapping | Status | Notes |
|:--------------|:---------------------|:-------------|:-------|:------|
| T810A1-CON-001 | System Isolation | → T810A-CON-001 | PROMOTED | Request: "System Isolation"; Epic: "System Prompt Scope" (title refined) |
| T810A1-CON-002 | Risk Acceptance | RETAINED | FEATURE-SPECIFIC | User acceptance statement specific to T810A1 |
| T810A1-CON-003 | Open Knowledge Base | RETAINED | FEATURE-SPECIFIC | General training + search tools (A1-specific implementation detail) |
| T810A1-CON-004 | No-Guessing Principle | → T810A-QG-008 | RECLASSIFIED | CON → QG reclassification; "Clarification Over Guessing" |
| T810A1-CON-005 | Tooling Deferral | RETAINED | FEATURE-SPECIFIC | MVP tool ecosystem (may be redundant with Epic DEP-003/CON-001; consider removal) |
| T810A1-CON-006 | Platform Compatibility | → T810A-CON-002 | PROMOTED | ChatGPT governance compliance |
| T810A1-CON-007 | Clinical Compliance Deferral | → T810A-CON-003 | PROMOTED | Regulatory compliance deferral |
| T810A1-CON-008 | ChatGPT Architectural Constraints | → T810A-CON-004 | PROMOTED | File system, validation, default behavior constraints |

**Post-Migration T810A1 CON Content**:
- **RETAIN**: T810A1-CON-002 (Risk Acceptance), CON-003 (Open Knowledge Base), CON-005 (Tooling Deferral)
- **DELETE**: T810A1-CON-001/004/006/007/008 — Promoted to Epic (CON-004 → QG-008 reclassification)

---

#### Non-Functional Requirements (9 total in T810A1 Request: NFR-001 through NFR-009)

| Current F-RID | Title (from Request) | Epic Mapping | Status | Notes |
|:--------------|:---------------------|:-------------|:-------|:------|
| T810A1-NFR-001 | Protocol Reliability | → T810A-QG-001 | HYBRID | Request: "Tracking → Analyze → Probe → Coach → Summarize"; Epic: "Clinical Protocol Reliability" (principle); Feature retains 5-phase implementation |
| T810A1-NFR-002 | Persona & Tone | → T810A-QG-002 | HYBRID | Request: Protocol phase tone mapping; Epic: Persona principle; Feature retains tone mapping details |
| T810A1-NFR-003 | Performance | → T810A-QG-003 | PROMOTED | Direct text match: "30-120 seconds latency acceptable" |
| T810A1-NFR-004 | Holistic Analysis | → T810A-QG-004 | PROMOTED | "Adjacent factors (stress, sleep, exercise)" |
| T810A1-NFR-005 | Maintainability | → T810A-QG-005 | HYBRID | Request: "9-block modular prompt structure"; Epic: "Architecture Maintainability" (principle); Feature retains 9-block specifics |
| T810A1-NFR-006 | Usability | → T810A-QG-006 | PROMOTED | "Medium-to-high literacy user; avoid paternalistic tone" |
| T810A1-NFR-007 | Confidence Communication | → T810A-QG-007 | PROMOTED | "Qualitative descriptors (fairly confident, moderate confidence, uncertain)" |
| T810A1-NFR-008 | Protocol Triggering Intelligence | RETAINED | FEATURE-SPECIFIC | 3-way input detection (Tracking-Only / Full Protocol / Simple Q&A); implementation of Epic IG-001 |
| T810A1-NFR-009 | Probe Phase Enforcement | RETAINED | FEATURE-SPECIFIC | ≥2 clarifying questions minimum; implementation of Epic QG-008 + IG-002 |

**Post-Migration T810A1 NFR Content**:
- **RETAIN**: T810A1-NFR-001/002/005 (hybrid implementations with feature-specific details), NFR-008/009 (feature-specific implementations)
- **DELETE**: T810A1-NFR-003/004/006/007 — Now inherited from Epic QGs

---

#### Interfaces (6 total in T810A1 Request: IF-001 through IF-006)

| Current F-RID | Title (from Request) | Epic Mapping | Status | Notes |
|:--------------|:---------------------|:-------------|:-------|:------|
| T810A1-IF-001 | Input Interface | RETAINED | FEATURE-SPECIFIC | "Unstructured text + images (stool/meals)" — A1-specific interface |
| T810A1-IF-002 | Output Interface | RETAINED | FEATURE-SPECIFIC | "Human-readable Markdown" — A1-specific output format |
| T810A1-IF-003 | Explicit Classification | RETAINED | FEATURE-SPECIFIC | Bristol Chart classification with confidence; implementation of Epic IG-003 |
| T810A1-IF-004 | Reporting Trigger | RETAINED | FEATURE-SPECIFIC | "/report" command recognition; implementation of Epic IG-001 |
| T810A1-IF-005 | Session Context Injection | RETAINED | FEATURE-SPECIFIC | Load patient profile + previous report at session start; implementation of Epic IG-006 |
| T810A1-IF-006 | Dynamic JSON Generation | RETAINED | FEATURE-SPECIFIC | Single-entry JSON per interaction; implementation of Epic IG-004 |

**Post-Migration T810A1 IF Content**:
- **RETAIN ALL**: T810A1-IF-001 through IF-006 — All feature-specific interface implementations

---

#### Integration Notes (5 total in T810A1 Request: INT-001 through INT-005)

| Current F-RID | Title (from Request) | Epic Mapping | Status | Notes |
|:--------------|:---------------------|:-------------|:-------|:------|
| T810A1-INT-001 | Internal State Object | RETAINED | FEATURE-SPECIFIC | Session-scoped JSON/YAML state — A1-specific implementation |
| T810A1-INT-002 | Memory Handoff Protocol | RETAINED | FEATURE-SPECIFIC | Dual-format report (Markdown narrative + JSON log); implementation of Epic IG-006 |
| T810A1-INT-003 | User-Mediated Workflow | RETAINED | FEATURE-SPECIFIC | Manual patient workflow for data transfers; implementation of Epic CON-001 |
| T810A1-INT-004 | Patient Data Architecture | RETAINED | FEATURE-SPECIFIC | Stable/Dynamic JSON split; implementation of Epic DEP-004 + IG-004 |
| T810A1-INT-005 | Memory Review Protocol | RETAINED | FEATURE-SPECIFIC | Step 0 memory scan; implementation of Epic IG-005 |

**Post-Migration T810A1 INT Content**:
- **RETAIN ALL**: T810A1-INT-001 through INT-005 — All feature-specific integration implementation notes

---

### C. Content Distribution Summary

**Inherited from Epic (27 E-RIDs)**:
- 4 ASSUM: T810A-ASSUM-001/002/003/004
- 5 DEP: T810A-DEP-001/002/003/004/005
- 4 CON: T810A-CON-001/002/003/004
- 8 QG: T810A-QG-001/002/003/004/005/006/007/008
- 6 IG: T810A-IG-001/002/003/004/005/006

**Feature Delta (30 F-RIDs remain)**:
- **1 ASSUM**: T810A1-ASSUM-004 (Session-Scoped Memory Model — hybrid implementation)
- **1 DEP**: T810A1-DEP-008 (Protocol Triggering Research)
- **3 CON**: T810A1-CON-002/003/005 (feature-specific constraints)
- **10 FRs (Stories)**: T810A1-S01 through S09 (9-block implementation specifics)
- **5 NFRs**: T810A1-NFR-001/002/005 (hybrid implementations), NFR-008/009 (feature implementations)
- **6 IFs**: T810A1-IF-001 through IF-006 (all feature-specific interfaces)
- **5 INTs**: T810A1-INT-001 through INT-005 (all feature-specific integration notes)

**Distribution Ratio**: **47% Epic inheritance (27 E-RIDs), 53% feature delta (30 F-RIDs)** — Confirms ~50/50 split

---

### D. Placement Guidance for T810A1 Request Updates

#### NEW Section Insertions

**1. Inherited Considerations Table**
- **Insert location**: After **Section III.D (Stakeholders)**, before current **Section III.E (Inheritances, Assumptions & Dependencies)**
- **New section header**: `### E. Inherited Epic Considerations`
- **Content**: 27-row table with columns: Category | E-RID | Title | Application Notes
- **Impact**: Current Section III.E → Section III.F (renumber all subsequent sections)

**2. Feature Governance Decisions**
- **Insert location**: After new **Section III.E (Inherited Epic Considerations)**, before renumbered **Section III.F (Assumptions & Dependencies)**
- **New section header**: `### F. Feature Governance Decisions`
- **Content**: T810A1-GDR-001 (Tracking-First Clinical Protocol), T810A1-GDR-002 (Session Workflow Architecture)
- **Impact**: Further section renumbering (original E → F → G, etc.)

**3. Feature Issues & Risks**
- **Insert location**: After **Section III.J (Stories)**, before current **Section III.K (Acceptance Criteria Register)**
- **New section header**: `### K. Feature Issues & Risks`
- **Content**: 4 Issues (T810A1-ISSUE-001 through ISSUE-004), 5 Risks (T810A1-RISK-001 through RISK-005)
- **Impact**: Current Section III.K → Section III.L (renumber remaining sections)

#### Section Modifications

**1. Section III.E (current) → Section III.G (post-migration): Assumptions & Dependencies**
- **DELETE**: T810A1-ASSUM-001/002/003, T810A1-DEP-001/002/003/004/005 (promoted to Epic)
- **RETAIN**: T810A1-ASSUM-004 (hybrid implementation), T810A1-DEP-008 (feature-specific)
- **UPDATE header**: From "Inheritances, Assumptions & Dependencies" to "Feature-Specific Assumptions & Dependencies"

**2. Section III.H (current) → Section III.J (post-migration): Constraints**
- **DELETE**: T810A1-CON-001/004/006/007/008 (promoted to Epic; CON-004 → QG-008)
- **RETAIN**: T810A1-CON-002/003/005 (feature-specific)
- **UPDATE header**: From "Constraints" to "Feature-Specific Constraints"

**3. Section III.F (current) → Section III.H (post-migration): Non-Functional Requirements**
- **DELETE**: T810A1-NFR-003/004/006/007 (promoted to Epic QGs)
- **RETAIN**: T810A1-NFR-001/002/005 (hybrid implementations), NFR-008/009 (feature implementations)
- **UPDATE header**: From "Non-Functional Requirements" to "Feature-Specific Non-Functional Requirements"

**4. Section III.G (current) → Section III.I (post-migration): Interfaces & Data**
- **RETAIN ALL**: T810A1-IF-001 through IF-006 (all feature-specific)
- **UPDATE descriptions**: Add explicit references to Epic IGs (e.g., "implements Epic IG-003")

**5. Section III.I (current) → Section III.K (post-migration): Feature Integration Notes**
- **RETAIN ALL**: T810A1-INT-001 through INT-005 (all feature-specific)
- **UPDATE descriptions**: Add explicit references to Epic IGs/DEPs (e.g., "implements Epic IG-006")

---

## III. ENHANCED INHERITED CONSIDERATIONS TABLE

### A. Table Structure Enhancement

**Column Headers** (refined from handoff brief):
- **Category**: RID category (ASSUM, DEP, CON, QG, IG)
- **E-RID**: Epic Requirement ID (e.g., T810A-ASSUM-001)
- **Title**: Epic requirement title
- **Application Notes**: **Feature-specific implementation references** (critical enhancement)

### B. Complete Inherited Considerations Table Template

```markdown
### E. Inherited Epic Considerations

This Feature inherits the following Epic-level requirements from T810A-SYSTEM. The "Application Notes" column indicates how each Epic requirement is applied or implemented within this Feature.

| Category | E-RID | Title | Application Notes |
|:---------|:------|:------|:------------------|
| **Assumptions** | T810A-ASSUM-001 | Patient Profile | Conversational agent assumes engaged patient with medium-to-high medical literacy per Section III.D (Stakeholders) |
| | T810A-ASSUM-002 | Input Modality & Quality | Text + images (stool/meal) input per T810A1-IF-001; variable image quality expected; patient confirms classifications per T810A1-IF-003 |
| | T810A-ASSUM-003 | LLM Capability | GPT-4V multimodal vision + reasoning for Bristol Chart classification (T810A1-IF-003) and clinical analysis (T810A1-NFR-001) |
| | T810A-ASSUM-004 | Platform Memory Uncertainty | Addressed via session-scoped memory approach (see T810A1-ASSUM-004); Step 0 Memory Review per T810A1-INT-005 |
| **Dependencies** | T810A-DEP-001 | Platform Capability | ChatGPT platform (GPT-4, Memory, Knowledge Base, Web access) per Section III.B (Source & Scope) |
| | T810A-DEP-002 | Long-term Analysis | T810A3-REPORT provides cross-session aggregation; dual-format reports per T810A1-INT-002 enable A3 integration |
| | T810A-DEP-003 | Toolbox Interface | T810A4-TOOLS manages custom tool declarations; MVP defers custom tools per T810A1-CON-005 |
| | T810A-DEP-004 | Patient Data Structures | T810A2-SCHEMA defines Stable/Dynamic JSON schemas; architecture per T810A1-INT-004; generation per T810A1-IF-006 |
| | T810A-DEP-005 | Clinical Safety Framework | Deferred to future development per Epic scope; acknowledged per T810A1-CON-007 (Clinical Compliance Deferral) |
| **Constraints** | T810A-CON-001 | System Prompt Scope | Deliverable is system prompt only per Section III.B (Scope); 9-block structure per T810A1-NFR-005 |
| | T810A-CON-002 | Platform Compatibility | Comply with ChatGPT governance policies; constraints detailed in T810A1-CON-008 |
| | T810A-CON-003 | Clinical Compliance Deferral | MVP excludes regulatory compliance; frame hypotheses as "working theories" per T810A1-CON-007 |
| | T810A-CON-004 | ChatGPT Architectural Constraints | File access (read-only KB), validation (prompt-based), Assistant mode override; detailed in T810A1-CON-008 |
| **Quality Goals** | T810A-QG-001 | Clinical Protocol Reliability | Implemented via 5-phase protocol (Tracking → Analyze → Probe → Coach → Summarize) per T810A1-NFR-001 |
| | T810A-QG-002 | Persona & Tone | Implemented via Consultant/Analyst mode with protocol phase tone mapping (Structured/Clinical/Collaborative/Supportive/Neutral) per T810A1-NFR-002 |
| | T810A-QG-003 | Analysis Performance | 30-120s latency acceptable for consultant-level analysis; thoughtful responses prioritized per T810A1-NFR-003 |
| | T810A-QG-004 | Holistic Analysis | Adjacent factors (stress, sleep, exercise) incorporated in Analyze phase when present per T810A1-NFR-004 |
| | T810A-QG-005 | Architecture Maintainability | Implemented via 9-block modular prompt structure (S01-S09) enabling independent updates per T810A1-NFR-005 |
| | T810A-QG-006 | Usability | Language targets medium-to-high GI literacy; plain language explanations; non-paternalistic partnership stance per T810A1-NFR-006 |
| | T810A-QG-007 | Confidence Communication | Qualitative confidence descriptors ("fairly confident", "moderate confidence", "uncertain") in classifications per T810A1-IF-003; numeric percentages prohibited |
| | T810A-QG-008 | Clarification Over Guessing | Implemented via Probe phase enforcement (≥2 clarifying questions before coaching) per T810A1-NFR-009; default to probing when data insufficient |
| **Implementation Guidance** | T810A-IG-001 | Protocol Triggering Guidance | Implemented via 3-way input detection (Tracking-Only / Full Protocol / Simple Q&A) per T810A1-NFR-008; details in S05 (Execution Protocol) |
| | T810A-IG-002 | Probe Phase Enforcement | ≥2 clarifying questions minimum before coaching per T810A1-NFR-009; Socratic inquiry mode (not Assistant service offers) |
| | T810A-IG-003 | Explicit Classification | Bristol Chart classification with qualitative confidence + user validation requests per T810A1-IF-003; conversational validation phrasing |
| | T810A-IG-004 | Dynamic JSON Single-Entry Pattern | Generate one structured entry per interaction per T810A1-IF-006; no cumulative logs; schema per T810A2-SCHEMA |
| | T810A-IG-005 | Memory Review Protocol | Step 0: Memory Review at session start per T810A1-INT-005; compare ChatGPT Memory vs. Stable JSON; flag discrepancies |
| | T810A-IG-006 | Session Context Injection & Handoff | Dual-format reports (Markdown narrative + JSON log) per T810A1-INT-002; load previous report at session start per T810A1-IF-005 |
```

---

## IV. HANDOFF BRIEF UPDATE RECOMMENDATIONS

Based on T810A1 Request baseline analysis, the handoff brief requires the following enhancements:

### A. Critical Updates

**Update 1: Enhanced Inherited Considerations Table** (PRIORITY: CRITICAL)
- **Change**: Replace current table with Section III.B template (detailed Application Notes with T810A1-* mappings)
- **Location**: Handoff brief Section II.C (Phase 2 Integration Requirements)
- **Rationale**: Provides T810A1 subconsultant with explicit traceability for where each Epic E-RID is implemented at feature level

**Update 2: Add Post-Migration Structure Outline** (PRIORITY: CRITICAL)
- **Change**: Insert new section after Phase 2 changes documenting 5-section post-migration structure
- **Content**: From Section II.D "Placement Guidance for T810A1 Request Updates" above
- **Location**: New section in handoff brief after Phase 2 integration requirements
- **Rationale**: Gives T810A1 subconsultant clear mental model of post-migration Request organization

**Update 3: Add Precise Placement Guidance** (PRIORITY: HIGH)
- **Change**: Update implementation checklist with specific section insertion points and renumbering impacts
- **Content**: From Section II.D "NEW Section Insertions" and "Section Modifications" above
- **Location**: Handoff brief Section V.A (Request Document Update Checklist)
- **Rationale**: Prevents placement errors; ensures consistent Request structure

### B. Completion Criteria

Handoff brief update complete when:
- [ ] Inherited Considerations Table enhanced with detailed Application Notes (27 rows updated)
- [ ] Post-migration structure outline added (5-section framework documented)
- [ ] Placement guidance added with section insertion points (3 new sections, 5 modified sections)
- [ ] Content distribution explicitly stated (47% Epic, 53% Feature delta)
- [ ] All F-RID→E-RID mappings validated against T810A1 Request baseline
