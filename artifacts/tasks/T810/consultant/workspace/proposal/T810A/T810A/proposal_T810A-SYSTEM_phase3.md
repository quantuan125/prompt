---
artifact_type: 'PROPOSAL'
initiative_id: 'T810'
epic_id: 'T810A'
version: '1.0.0'
date: '2025-10-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_document: 'sps_T810-GASTRO.md, concept_T810-GASTRO.md'
target_section: 'SPS Section III.C.1.vii (Epic GDRs), Concept Section III.B.1 (Epic ADRs)'
---

# PHASE 3B: E-GDR SEQUENTIAL CONSULTATIONS & ADR STUB CREATION

## I. EXECUTIVE SUMMARY

This proposal serves as the dynamic consultation workspace for Phase 3B Epic GDR alignment. Following Phase 3A research findings, this workspace documents the sequential consultation of **4 retained E-GDRs** (GDR-002, 003, 005, 006) with Epic-level language revisions, **3 Epic ADR stub creations** (ADR-002, 005, 006), and resolution of **5 critical questions** identified in research.

**Research Foundation**: `prompt/artifacts/tasks/T810/consultant/workspace/T810A/analysis/analysis_T810A-SYSTEM_gdr-scope-assessment.md`

**Key Phase 3B Outcomes** (per plan Section 3.2):
- **GDR Scope Reduction**: 6 GDRs → 4 E-GDRs (demoted GDR-001/004 to T810A1 per research)
- **Priority Sequencing**: GDR-002 → 003 → 006 → 005 (HIGH → HIGH → HIGH → MEDIUM)
- **ADR Strategy**: Stub creation in Phase 3B; full draft development in Phase 3C
- **Format Compliance**: All proposals follow T102-ADR-004 (Decision Records Index) standards

**Target Artifacts**:
- **GDR Revisions**: `sps_T810-GASTRO.md` Section III.C.1.vii
- **ADR Drafts**: `concept_T810-GASTRO.md` Section III.B.1 (after Phase 3C approval)

**Consultation Workflow** (6-Step Process per GDR):
1. Present research findings (Section VI from analysis)
2. Address critical questions (Section VIII from analysis)
3. Client review & decision
4. Draft revised Epic GDR language
5. Draft Epic ADR stub (if required)
6. Client approval gate

---

## IA. EPIC GOVERNANCE DECISIONS INDEX

**Research Foundation**: `T810A-RES-001 (System Architecture & Clinical Validation)` — establishes multimodal AI patterns, data architecture, knowledge governance, and reporting requirements

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| `T810A-GDR-001` | Trust-and-Verify Workflow Standard | Proposed | Client | TBD | T810A-GDR-002 | #t810a-gdr-001-trust-and-verify |
| `T810A-GDR-002` | Stable/Dynamic JSON Architecture | Proposed | Client | TBD | T810A-GDR-003 | #t810a-gdr-002-sechma-split-arch |
| `T810A-GDR-003` | Dual-Purpose Clinical Reporting | Proposed | Client | TBD | T810A-GDR-006 | #t810a-gdr-003-dual-purpose-reporting |
| `T810A-GDR-004` | GI Knowledge Base Sources | Proposed | Client | TBD | T810A-GDR-005 | #t810a-gdr-004-gi-knowledge-sources |

**Note**: Renumbering reflects priority-first sequencing (HIGH→001-003, MEDIUM→004). Original GDR-001/004 demoted to T810A1-GDR-001/004 per Phase 3A research.

---

## IB. EPIC ARCHITECTURAL DECISIONS INDEX

| EPIC ID | ADR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:--------|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| T810A | `T810A-ADR-001` | Trust-and-Verify Confidence Policy | Proposed | Client | TBD | — | #t810a-adr-001-confidence-policy |
| T810A | `T810A-ADR-003` | Dual-Purpose Reporting Policy | Proposed | Client | TBD | — | #t810a-adr-003-dual-purpose-reporting |
| T810A | `T810A-ADR-004` | GI Knowledge Sources Catalog | Proposed | Client | TBD | — | #t810a-adr-004-gi-sources-catalog |

**Note**: ADR-002/005/006 extract implementation details from GDR-001/004/003 respectively per Phase 3B consultation strategy.

---

## II. GDR-002 CONSULTATION: TRUST-AND-VERIFY WORKFLOW STANDARD

### A. Research Findings Summary

**Epic Scope Test**: NEEDS ABSTRACTION
**Classification**: E-GDR (Retain at Epic with ADR extraction)
**Priority**: HIGH
**Confidence**: High

**Feature Applicability Matrix** (from analysis Section III):
- ✅ **T810A1 (PROMPT)**: Qualitative confidence communication in image classification
- ✅ **T810A2 (PATIENT)**: Confidence field semantics in schema definitions
- ✅ **T810A3 (REPORT)**: Consumption of validated inputs with confidence awareness
- ❓ **T810A4 (TOOLS)**: Future tool selection may require confidence signaling

**Epic Appropriateness**: Cross-cutting safety/communication governance applicable to all features performing classifications or generating results requiring validation.

**Implementation Details Identified** (from analysis Section IV):
1. **Numeric confidence thresholds** (70%, 90%) — Move to ADR; forbid numeric in user-facing text; allow internal numeric for machine logs
2. **Image-specific phrasing** — Keep as examples in ADR; maintain generalized GDR language

**E-RID Mapping Validation** (from analysis Section V):
- **Current F-RID refs**: T810A1-NFR-007, T810A1-IF-003, T810A1-CON-008
- **Proposed E-RID mapping**:
  - NFR-007 → `T810A-QG-007` (Confidence Communication)
  - IF-003 → `T810A-IG-003` (Explicit Classification)
  - CON-008 → `T810A-CON-004` (ChatGPT Architectural Constraints)
- **Missing coverage**: None; numeric guidance shifts to ADR
- **Circular reference risk**: Low

**Recommended Revision Strategy** (from analysis Section VI): **ADR EXTRACTION**

---

### B. Critical Question Resolution

**Question** (from analysis Section VIII, Question 2):
Should numeric confidence thresholds (e.g., 70%, 90%) be retained as internal guidance or removed entirely?

**Options**:
- **Option A**: Retain as ADR-level internal guidance (prohibit numeric in user-facing prose)
  - **Pros**: Predictable validation intensity; consistent prompting across contexts
  - **Cons**: Maintenance overhead; potential false precision
- **Option B**: Remove numeric entirely; qualitative tiers only
  - **Pros**: Simplicity; reduced maintenance
  - **Cons**: Less consistent prompting; harder to calibrate across modalities

**Research Recommendation**: **Option A** (retain in ADR-002)

**Client Decision**: ___________

---

### C. Proposed Revised GDR Language

**Current GDR-002 Body** (from SPS):
```markdown
* **T810A-GDR-002 (Trust-and-Verify Workflow Standard) {#t810a-gdr-002-trust-verify}**

  **Context:** Research validation (`T810A-RES-001` Deliverable B) identifies confidence communication and user validation as essential multimodal AI pattern, particularly for image classification tasks (stool Bristol scale, meal analysis). Without explicit confidence thresholds and validation workflows, the agent risks either overstating certainty (creating false confidence) or understating reliability (undermining clinical utility). Empirical conversation analysis (`T810A-RES-002`) revealed numeric confidence in JSON outputs (`"confidence": 0.7`) without corresponding qualitative communication in natural language, creating disconnect between machine representation and user-facing communication.

  **Decision:** Adopt **Trust-and-Verify Workflow Standard** with qualitative confidence communication and validation intensity thresholds:
  - **High Confidence** (agent assessment: >90% certain): State classification with brief rationale; validation optional ("This appears to be Bristol Type 5-6 based on...")
  - **Moderate Confidence** (agent assessment: 70-90% certain): State classification with detailed rationale + encourage user validation in Probe phase per `T810A1-IF-003` ("I see this as Bristol Type 5, though the lighting makes it somewhat ambiguous. Does that match what you observed?")
  - **Low Confidence** (agent assessment: <70% certain): State uncertainty explicitly + mandatory validation request ("The image quality makes definitive classification difficult. What did you observe?")

  The agent SHALL use qualitative descriptors ("fairly confident," "moderate confidence," "uncertain") in natural language communication per `T810A1-NFR-007`. Numeric confidence fields (e.g., `"confidence": 0.75`) MAY be included in Dynamic JSON for internal tracking and pattern analysis per `T810A1-IF-003`, but SHALL NOT appear in user-facing text.

  Validation requests SHALL NOT block conversational flow; agent proceeds with analysis using stated confidence level and incorporates user corrections in subsequent turns.

  **Consequences:**
  - (+) Industry-aligned multimodal AI pattern validated by research across clinical AI applications
  - (+) Balances clinical accuracy needs with conversational fluidity (validation encouragement, not mandatory blocking)
  - (+) Clear distinction between machine-readable confidence (numeric in JSON) and user-readable confidence (qualitative in prose)
  - (+) Explicit uncertainty communication builds user trust and enables correction loops
  - (±) Moderate/low confidence scenarios increase interaction turns (Probe phase validation before Coach)
  - (±) Threshold boundaries (70%, 90%) are guidelines; actual phrasing adapted per context in Execution Protocol (Block 5)
  - (-) No programmatic validation capability per `T810A1-CON-008`; relies entirely on prompt-based enforcement

  **References:**
  `T810A-RES-001` (Deliverable B: Multimodal Trust-and-Verify Patterns),
  `T810A-RES-002` (Conversation-Driven Empirical Validation),
  `T810A1-NFR-007` (Confidence Communication),
  `T810A1-IF-003` (Explicit Classification),
  `T810A1-CON-008` (ChatGPT Architectural Constraints)

```

**Proposed Revised GDR Language** (Epic-level abstraction, compressed to ~100 words):
```markdown
* **T810A-GDR-001 (Trust-and-Verify Workflow Standard)** {#t810a-gdr-001-trust-and-verify}

  **Context:** Per `T810A-RES-001` Deliverable B, confidence communication and user validation are essential for assessments requiring validation. Features risk overstating certainty or undermining reliability without explicit workflows.

  **Decision:** Features performing classifications SHALL: 
  (1) communicate confidence qualitatively in user-facing prose, never numeric; 
  (2) explain reasoning; 
  (3) invite validation when uncertain; 
  (4) adjust analysis per corrections. 
  
  Adopt `T810A-ADR-001`, defining mandatory numeric thresholds for backend/JSON (0-1 range), qualitative tier mappings, and modality-specific examples.

  **Consequences:**
  - (+) Industry-aligned multimodal pattern per `T810A-RES-001`; cross-feature consistency
  - (±) Numeric thresholds mandatory for backend/JSON; features adapt user-facing phrasing per context
  - (-) No programmatic validation per `T810A-CON-004`

  **References:**
  `T810A-RES-001 (System Architecture & Clinical Validation)`,
  `T810A-QG-007 (Confidence Communication)`,
  `T810A-IG-003 (Explicit Classification)`,
  `T810A-CON-004 (ChatGPT Architectural Constraints)`,
  `T810A-ADR-001 (Trust-and-Verify Confidence Policy)`
```

**Key Abstraction Changes**:
- Added list item format `* **...` per T102-ADR-004-FR-002
- Added periods after all bold subheading labels (**Context.**, **Decision.**, **Consequences.**, **References.**)
- Moved all content inside bold subheadings (nothing outside)
- Added **Consequences.** section with (+)/(±)/(-) bullets
- Added "Adopt `T810A-ADR-001`..." statement in **Decision.** per plan Section 1.1
- Added `T810A-RES-001` reference as research foundation
- Fixed **References.** format to comma-separated backticked items (not bullet list)
- Removed image-specific language ("Bristol Stool Chart")
- Removed numeric thresholds from GDR body (moved to ADR-002)
- Generalized "classifications" to include assessments beyond images
- E-RID references only (no F-RID citations)

**Client Approval**: ___________

---

### D. Proposed Epic ADR (Full Draft — Phase 3B+3C Combined)

**ADR Full Draft**: `T810A-ADR-001 (Trust-and-Verify Confidence Policy)`

```markdown
* **T810A-ADR-001 (Trust-and-Verify Confidence Policy)** {#t810a-adr-001-confidence-policy}

  **Context:** Per `T810A-GDR-001`, features must communicate confidence qualitatively while maintaining mandatory numeric thresholds for backend/JSON tracking. Research (`T810A-RES-001` Deliverable B; `T810A-RES-002`) revealed numeric confidence in JSON without qualitative user-facing communication, creating machine/human disconnect. This ADR extracts implementation details from Epic governance for feature-specific adaptation.

  **Decision:** Establish Trust-and-Verify Confidence Policy defining qualitative tiers, mandatory internal numeric ranges for backend/JSON (0-1 scale), modality-specific examples, and explicit prohibition of numeric values in user-facing prose.

  **Specification:**

  **T810A-ADR-001-FR-001 (Qualitative Confidence Tiers)**
  - **High Confidence**: "fairly confident," "this appears to be," "likely" — State classification with brief rationale; validation optional
  - **Moderate Confidence**: "moderate confidence," "appears to be, though [ambiguity]," "suggest" — State with detailed rationale + encourage validation
  - **Low Confidence**: "uncertain," "difficult to classify definitively," "unclear" — State uncertainty explicitly + mandatory validation request

  **T810A-ADR-001-FR-002 (Mandatory Internal Numeric Ranges)**
  - **MANDATORY for backend/JSON tracking** (Dynamic JSON generation, pattern analysis, validation logic):
    - High: >0.9 (0.9-1.0 range)
    - Moderate: 0.7-0.9
    - Low: <0.7 (0.0-0.7 range)
  - **PROHIBITION**: Numeric confidence values SHALL NOT appear in user-facing communication
  - **Use Case**: Backend generation tasks (Dynamic JSON `"confidence": 0.85`), A3 pattern analysis, validation intensity logic
  - Features SHALL implement numeric→qualitative mapping per FR-001 for all user-facing text

  **T810A-ADR-001-FR-003 (Image Classification Examples)**
  - **Bristol Stool Chart** (Types 0-7):
    - **Type 0**: "nothing" (no poop produced despite attempted BM)
      - Tracking: Always confidence=1.0 in Dynamic JSON (`"stool_type": 0, "confidence": 1.0`)
      - User-facing: Intelligent communication required: "I understand you attempted a bowel movement but didn't produce anything. That's important tracking information."
    - **Type 1-7** (standard Bristol scale):
      - High (>0.9): Clear Type 4 → "This appears to be Bristol Type 4 based on smooth texture and shape"
      - Moderate (0.7-0.9): Type 5-6 ambiguity → "I see this as Bristol Type 5, though lighting makes it somewhat ambiguous. Does that match?"
      - Low (<0.7): Poor quality → "Image quality makes definitive classification difficult. What did you observe?"
  - **Meal Analysis**:
    - High: Clear items → "This appears to be a vegetable stir-fry with rice"
    - Moderate: Partial visibility → "This looks like pasta, though some ingredients are partially visible. Can you confirm?"

  **T810A-ADR-001-FR-004 (Cross-Modality Applicability)**
  - **Text Analysis**: Apply tiers to symptom severity assessments, pattern identification
  - **Structured Data**: Apply to controlled vocabulary matching, clinical criteria alignment
  - **Pattern Recognition**: Apply to longitudinal trend analysis, correlation identification

  **T810A-ADR-001-FR-005 (Validation Intensity Mapping)**
  - High (>0.9) → Validation optional ("Does that sound right?")
  - Moderate (0.7-0.9) → Validation encouraged ("Can you confirm?")
  - Low (<0.7) → Validation mandatory ("What did you observe?")
  - Validation SHALL NOT block conversational flow per `T810A-GDR-001`

  **Consequences:**
  - (+) Standardized confidence behavior across features with mandatory backend numeric for A3 pattern analysis
  - (+) Bristol Type 0 handled correctly (confidence=1.0 tracking, intelligent user communication)
  - (±) Features must maintain numeric→qualitative mapping discipline
  - (±) Numeric ranges mandatory for backend; features adapt user-facing phrasing
  - (-) No programmatic validation per `T810A-CON-004`

  **Alternatives Considered:**
  - **Option A**: Optional numeric guidance
    - Rejected: Backend/JSON tracking requires mandatory numeric for A3 aggregation and validation logic
  - **Option B**: Numeric in user-facing with disclaimer
    - Rejected: False precision perception
  - **Option C**: Separate tiers per modality
    - Rejected: Unnecessary complexity

  **References:**
  `T810A-GDR-001 (Trust-and-Verify Workflow Standard)`,
  `T810A-QG-007 (Confidence Communication)`,
  `T810A-IG-003 (Explicit Classification)`,
  `T810A-CON-004 (ChatGPT Architectural Constraints)`

  **Provenance:**
```

**Client Approval for Full Draft**: ___________

---

## III. GDR-003 CONSULTATION: STABLE/DYNAMIC JSON ARCHITECTURE

### A. Research Findings Summary

**Epic Scope Test**: PASS
**Classification**: E-GDR (Retain at Epic with IG reference abstraction)
**Priority**: HIGH
**Confidence**: High

**Feature Applicability Matrix** (from analysis Section III):
- ✅ **T810A1 (PROMPT)**: Generate dynamic tracking entries
- ✅ **T810A2 (PATIENT)**: Define schemas and authority boundaries
- ✅ **T810A3 (REPORT)**: Aggregate cross-session data
- ❓ **T810A4 (TOOLS)**: May consume stable/dynamic split patterns

**Epic Appropriateness**: Canonical data architecture governing patient-controlled vs. LLM-generated data split across entire Epic.

**Implementation Details Identified** (from analysis Section IV):
1. **"Block 4" & A1-specific INT-002 references** — Replace with Epic-neutral "designated knowledge storage" and reference E-IG-006 + T810A-DEP-002
2. **Session-specific loading phrasing** — Reference E-IG-005/006 rather than A1 INTs

**E-RID Mapping Validation** (from analysis Section V):
- **Current F-RID refs**: T810A1-IF-006, INT-004/005, NFR-009, CON-008, DEP-004/002
- **Proposed E-RID mapping**:
  - IF-006 → `T810A-IG-004` (Dynamic JSON Single-Entry Pattern)
  - INT-004 → `T810A-IG-006` (Session Context Injection & Handoff)
  - INT-005 → `T810A-IG-005` (Memory Review Protocol)
  - NFR-009 → `T810A-IG-002` (Probe Phase Enforcement)
  - CON-008 → `T810A-CON-004` (ChatGPT Architectural Constraints)
  - DEP-004 → `T810A-DEP-004` (Patient Data Structures)
  - DEP-002 → `T810A-DEP-002` (Long-term Analysis)
- **Missing coverage**: None after E-IG references
- **Circular reference risk**: Low

**Recommended Revision Strategy** (from analysis Section VI): **HYBRID SPLIT**
- **Epic principle (GDR)**: Establish Stable vs. Dynamic split and authorities
- **Implementation pattern (E-IG)**: Single-entry rule, session context/memory, aggregation

---

### B. Critical Question Resolution

**Question** (from analysis Section VIII, Question 3):
Where should "session initialization" and "end-of-day aggregation" be governed?

**Options**:
- **Option A**: Keep inside GDR-003 body
  - **Cons**: Scope leak to A1; duplicates IGs
- **Option B**: Reference E-IG-005/006 and A3 dependency only
  - **Pros**: Clean separation; proper layering
  - **Cons**: Requires cross-doc navigation

**Research Recommendation**: **Option B** (IGs + dependency)

**Client Decision**: ___________

---

### C. Proposed Revised GDR Language

**Current GDR-003 Body** (from SPS):
```markdown
* **T810A-GDR-003 (Stable/Dynamic JSON Architecture) {#t810a-gdr-003-json-architecture}**

  **Context.** Initial research validation (`T810A-RES-001` Deliverable E) identified constant/stable/dynamic data categorization for patient profiles. However, empirical conversation analysis (`T810A-RES-002`) revealed architectural mismatch: actual conversation generated cumulative JSON (Turn 2 regenerated all Turn 1 entries + new entries) instead of single-entry tracking pattern. Client directive (Phase 1.5 Comment 1) specified architectural requirement: "Instead of a single JSON file system, we will need multiple JSON files, at least starting with two: stable and dynamic." ChatGPT platform constraint (`T810A1-CON-008`) imposes read-only file access for LLM, preventing direct profile updates. Without clear architectural separation, the system conflates persistent profile context (demographics, conditions) with ephemeral tracking data (daily meals, stools), creating token inefficiency and cross-session persistence challenges.

  **Decision.** Adopt **Stable/Dynamic JSON Split Architecture** as the canonical data model for LLM_Gastro:

  **Stable JSON (Patient Profile)**:
  - Contains constant patient data (demographics: age, sex) and stable data (conditions, medications, triggers, relievers, allergies, clinical history notes) per `T810A2` specifications
  - Stored in Knowledge Base (Block 4), manually updated by patient outside conversation
  - **Read-only** for LLM_Gastro per `T810A1-CON-008` (ChatGPT file system constraint)
  - Loaded at session start per `T810A1-INT-005` (Step 1: Context Loading after memory review)
  - Detailed field definitions, schema validation, and value sets deferred to `T810A2` per `T810A1-DEP-004`

  **Dynamic JSON (Tracking Entries)**:
  - LLM_Gastro generates **single entry per patient interaction** containing event data: patient_state, meal, stool, sleep, or other clinically relevant observations per `T810A1-IF-006`
  - Uses structured keys with controlled vocabularies (value sets defined in `T810A2`)
  - Schema is **flexible**: LLM_Gastro MAY add keys if clinically justified (e.g., "exercise", "medication_taken", "stress_event")
  - Skeleton structure stored in Knowledge Base as generation exemplar
  - **End-of-day reporting** aggregates all Dynamic JSON entries from session per `T810A1-INT-002`

  **Integration Patterns** per `T810A1-INT-004`:
  - Missing Dynamic JSON keys trigger Probe phase to elicit clarifying information per `T810A1-NFR-009`
  - Cross-session persistence of aggregated Dynamic JSON entries deferred to `T810A3-REPORT` per `T810A1-DEP-002`

  This decision establishes clean separation between LLM-generated ephemeral tracking data (Dynamic JSON) and patient-governed persistent profile (Stable JSON), accommodating ChatGPT platform constraints while enabling clinical workflow.

  **Consequences.**
  - (+) Accommodates ChatGPT read-only constraint by separating LLM-writable (Dynamic JSON) from patient-managed (Stable JSON) data
  - (+) Enables single-entry tracking pattern validated by empirical requirements (no cumulative regeneration)
  - (+) Clear token efficiency: Stable JSON loaded once per session; Dynamic JSON generated per interaction
  - (+) Flexible schema design allows LLM to add clinically relevant keys beyond predefined types
  - (±) Requires manual patient updates to Stable JSON outside conversation (friction but necessary per platform constraint)
  - (±) Surface-level architecture in `T810A1`; detailed schemas in `T810A2` (dependency coordination required)
  - (-) Risk of Stable JSON staleness if patient doesn't maintain profile; mitigated by memory review protocol per `T810A1-INT-005`

  **References.**
  `T810A-RES-001` (Deliverable E: Patient Profile Schema),
  `T810A-RES-002` (Conversation-Driven Empirical Validation),
  `T810A1-INT-004` (Patient Data Architecture),
  `T810A1-INT-005` (Memory Review Protocol),
  `T810A1-IF-006` (Dynamic JSON Generation),
  `T810A1-NFR-009` (Probe Phase Enforcement),
  `T810A1-CON-008` (ChatGPT Architectural Constraints),
  `T810A1-DEP-004` (Patient Data Structures Dependency),
  `T810A1-DEP-002` (Long-term Analysis Dependency)
```

**Proposed Revised GDR Language** (Epic-level abstraction, compressed to ~100 words):
```markdown
* **T810A-GDR-002 (Schema Split Architecture)** {#t810a-gdr-002-sechma-split-arch}

  **Context:** Per `T810A-RES-001` Deliverable E and `T810A-RES-002`, patient-governed vs. LLM-generated data require architectural separation. ChatGPT read-only constraint (`T810A-CON-004`) necessitates split architecture.

  **Decision:** Implement Stable/Dynamic JSON Split: 
  (1) Stable JSON (patient profile: demographics, conditions, medications) stored in designated knowledge storage, manually updated, read-only for LLM, authority over Memory; 
  (2) Dynamic JSON (tracking logs) per `T810A-IG-004` single-entry pattern, flexible schema; 
  (3) T810A2 owns schemas per `T810A-DEP-004`, T810A3 owns aggregation per `T810A-DEP-002`, session loading per `T810A-IG-005`/`T810A-IG-006`.

  **Consequences:**
  - (+) Accommodates platform constraint; token efficiency (Stable once/session, Dynamic per-interaction)
  - (±) Manual patient updates; Epic surface architecture with T810A2 schema details
  - (-) Staleness risk mitigated by `T810A-IG-005`

  **References:**
  `T810A-RES-001 (System Architecture & Clinical Validation)`,
  `T810A-IG-004 (Dynamic JSON Single-Entry Pattern)`,
  `T810A-IG-005 (Memory Review Protocol)`,
  `T810A-IG-006 (Session Context Injection & Handoff)`,
  `T810A-CON-004 (ChatGPT Architectural Constraints)`,
  `T810A-DEP-004 (Patient Data Structures)`,
  `T810A-DEP-002 (Long-term Analysis)`
```

**Key Abstraction Changes**:
- Added list item format `* **...` per T102-ADR-004-FR-002
- Added periods after all bold subheading labels
- Moved all content inside bold subheadings
- Added **Consequences.** section with (+)/(±)/(-) bullets from original GDR-003
- Added `T810A-RES-001` and `T810A-RES-002` references as research foundation
- Fixed **References.** format to comma-separated backticked items
- Removed "Block 4" references → "designated knowledge storage"
- Removed A1-specific INT references (INT-004/005/002)
- Added explicit T810A2/T810A3 ownership statements
- Referenced E-IG-004/005/006 for implementation patterns
- E-RID references only (no F-RID citations)
- Maintained core Stable>Memory precedence rule

**Client Approval**: ___________

---

### D. ADR Requirement Assessment

**Question**: Does GDR-003 require Epic ADR creation?

**Research Assessment** (from analysis Section VI):
> "**Recommended Revision Strategy**: HYBRID SPLIT — Epic principle (GDR): Establish Stable vs. Dynamic split and authorities. Implementation pattern (E-IG): Single-entry rule, session context/memory, aggregation."

**Conclusion**: **No ADR required**. Implementation patterns already exist in E-IG-004/005/006 (created in Phase 2). GDR-003 references existing IGs rather than creating new ADR.

**Client Confirmation**: ___________

---

## IV. GDR-006 CONSULTATION: DUAL-PURPOSE CLINICAL REPORTING

### A. Research Findings Summary

**Epic Scope Test**: NEEDS ABSTRACTION
**Classification**: E-GDR (Retain at Epic with hybrid split)
**Priority**: HIGH
**Confidence**: Moderate-High

**Feature Applicability Matrix** (from analysis Section III):
- ✅ **T810A1 (PROMPT)**: Session-end report generation
- ✅ **T810A2 (PATIENT)**: Timestamps and field format alignment
- ✅ **T810A3 (REPORT)**: Cross-session aggregation and reporting
- ❓ **T810A4 (TOOLS)**: May consume report data

**Epic Appropriateness**: Dual-purpose reporting principle (clinician handoff + LLM memory) is Epic-level governance.

**Implementation Details Identified** (from analysis Section IV):
1. **First-person voice mandate; 100-200 token target; trigger commands; validation loop** — Move to ADR/IG
2. **A1 INT-002 anchoring** — Reference E-IG-006 and A3 dependency instead

**E-RID Mapping Validation** (from analysis Section V):
- **Current F-RID refs**: INT-002, IF-005, A3 dependency
- **Proposed E-RID mapping**:
  - INT-002/IF-005 → `T810A-IG-006` (Session Context Injection & Handoff)
  - A3 dependency → `T810A-DEP-002` (Long-term Analysis)
- **Missing coverage**: None
- **Circular reference risk**: Low

**Recommended Revision Strategy** (from analysis Section VI): **HYBRID SPLIT**
- **Epic principle (GDR)**: Unified reporting serving both clinician and LLM
- **Implementation pattern (E-ADR/IG)**: Voice, length, triggers, validation

---

### B. Critical Question Resolution

**Question** (from analysis Section VIII, Question 4):
Should "first-person voice" and "100-200 token" target be Epic-level rules?

**Options**:
- **Option A**: Epic GDR rule
  - **Pros**: Strong consistency across features
  - **Cons**: Constrains future A3 report variants and A1 exploration
- **Option B**: Epic ADR guidance
  - **Pros**: Adjustable; feature flexibility
  - **Cons**: Weaker enforcement signal

**Research Recommendation**: **Option B** (ADR-006 guidance)

**Client Decision**: ___________

---

### C. Proposed Revised GDR Language

**Current GDR-006 Body** (from SPS):
```markdown
* **T810A-GDR-006 (Dual-Purpose Clinical Reporting) {#t810a-gdr-006-clinical-reporting}**

  **Context.** Research validation (`T810A-RES-001` Deliverable F) confirms chronological timeline format in first-person patient perspective as optimal for both clinician handoff (human-readable summary) and LLM memory (context injection for next session). Traditional clinical notes use third-person clinician voice ("Patient reports..."), creating disconnect for patient-authored documentation. Empirical conversation analysis did not test reporting directly but validated tracking-first workflow requiring efficient end-of-day aggregation pattern per `T810A1-INT-002`. Without dual-purpose design, separate formats would be needed for clinician communication vs. LLM memory consumption, increasing complexity and token overhead.

  **Decision** Adopt **Dual-Purpose Clinical Reporting Architecture** with unified format serving both clinician handoff and LLM memory:

  **Report Structure** per `T810A1-INT-002`:
  - **Format**: Chronological timeline Markdown narrative in **first-person patient perspective**
  - **Voice**: "I experienced..." not "Patient experienced..." or "You experienced..."
  - **Content**: Time → Event → Symptom/Meal/Stool → Analysis Summary pattern
  - **Length**: Target 100-200 tokens per daily report for token efficiency per `T810A1-IF-005`

  **Dual-Purpose Use Cases**:
  1. **Clinician Handoff**: Patient shares report with gastroenterologist for consultation prep
  2. **LLM Memory**: Report loaded at next session start per `T810A1-IF-005` (compressed context vs. full conversation history)

  **Validation Protocol** per `T810A1-INT-002`:
  - Agent presents report draft → patient reviews → patient confirms/corrects → agent finalizes
  - Validation enables patient authority over clinical narrative
  - Conversational validation phrasing per `T810A1-NFR-002` (not blocking approval gate)

  **Output Artifacts**:
  - Markdown narrative (human-readable, clinician-shareable)
  - Structured JSON log (machine-readable, future pattern analysis via `T810A3-REPORT` per `T810A1-DEP-002`)

  This decision optimizes for dual-purpose utility while maintaining single-artifact simplicity and patient narrative authority.

  **Consequences.**
  - (+) Industry-validated dual-purpose design reduces artifact proliferation (one report, two use cases)
  - (+) First-person perspective maintains patient ownership and narrative authenticity
  - (+) Chronological timeline format natural for both human reading and LLM context injection
  - (+) Token efficiency target (100-200 tokens) enables sustainable multi-session continuity
  - (+) Validation protocol respects patient authority over clinical narrative per `T810A1-NFR-002`
  - (±) First-person voice unconventional for clinical documentation; may require clinician education on patient-authored format
  - (±) 100-200 token target requires careful summarization; overly aggressive compression risks losing clinical nuance
  - (-) Cross-session pattern analysis and formal clinician handoff deferred to `T810A3-REPORT` per `T810A1-DEP-002`

  **References.**
  `T810A-RES-001` (Deliverable F: Clinical Reporting Architecture),
  `T810A1-INT-002` (Memory Handoff Protocol),
  `T810A1-IF-005` (Session Context Injection),
  `T810A1-NFR-002` (Persona & Tone),
  `T810A1-DEP-002` (Long-term Analysis Dependency)
```

**Proposed Revised GDR Language** (Epic-level abstraction, compressed to ~100 words):
```markdown
* **T810A-GDR-003 (Dual-Purpose Clinical Reporting)** {#t810a-gdr-003-dual-purpose-reporting}

  **Context:** Per `T810A-RES-001` Deliverable F, chronological timeline in first-person patient perspective serves both clinician handoff and LLM memory. Separate formats would increase complexity and token overhead.

  **Decision:** Features generating session reports SHALL: 
  (1) produce unified report for clinician review and LLM memory; 
  (2) align structure/timing/export per `T810A-IG-006`; 
  (3) integrate patient validation. 
  
  Adopt `T810A-ADR-003`, defining voice (first-person), length (100-200 tokens), content patterns, triggers, validation, JSON export, A1/A3 coordination.

  **Consequences:**
  - (+) Industry-validated dual-purpose design per `T810A-RES-001`; cross-feature consistency with ADR flexibility
  - (±) First-person voice unconventional; token targets require careful summarization
  - (-) Advanced features deferred to T810A3 per `T810A-DEP-002`

  **References:**
  `T810A-RES-001 (System Architecture & Clinical Validation)`,
  `T810A-IG-006 (Session Context Injection & Handoff)`,
  `T810A-QG-002 (Persona & Tone)`,
  `T810A-DEP-002 (Long-term Analysis)`,
  `T810A-ADR-003 (Dual-Purpose Reporting Policy)`
```

**Key Abstraction Changes**:
- Added list item format `* **...` per T102-ADR-004-FR-002
- Added periods after all bold subheading labels
- Moved all content inside bold subheadings
- Added **Consequences.** section with (+)/(±)/(-) bullets from original GDR-006
- Added "Adopt `T810A-ADR-003`..." statement in **Decision.** per plan Section 1.1
- Added `T810A-RES-001` reference as research foundation
- Fixed **References.** format to comma-separated backticked items
- Removed implementation details to ADR-006 (first-person voice, 100-200 tokens, Time→Event→Analysis pattern, triggers, validation loop)
- Removed A1 INT-002 reference
- Maintained dual-purpose principle at Epic level
- E-RID references only

**Client Approval**: ___________

---

### D. Proposed Epic ADR (Full Draft — Phase 3B+3C Combined)

**ADR Full Draft**: `T810A-ADR-003 (Dual-Purpose Reporting Policy)`

```markdown
* **T810A-ADR-003 (Dual-Purpose Reporting Policy)** {#t810a-adr-003-dual-purpose-reporting}

  **Context:** Per `T810A-GDR-003`, features must produce unified reports serving both clinician handoff and LLM memory. Research (`T810A-RES-001` Deliverable F) confirms chronological timeline in first-person patient perspective as optimal for dual-purpose use. This ADR extracts format specifics, voice mandates, length guidance, triggers, and validation from Epic governance for feature adaptation.

  **Decision:** Establish Dual-Purpose Reporting Policy defining voice, structure, triggers, validation, and export patterns for session-end clinical reporting.

  **Specification:**

  **T810A-ADR-003-FR-001 (Narrative Voice Mandate)**
  - **First-Person Patient Perspective**: "I experienced..." (NOT "Patient experienced..." or "You experienced...")
  - **Rationale**: Patient narrative ownership; natural for patient-authored documentation
  - **Example**: "I had breakfast at 8:30 AM with scrambled eggs and toast. Mid-morning I experienced mild bloating..."

  **T810A-ADR-003-FR-002 (Length Targets)**
  - **Target Range**: 100-200 tokens per daily report
  - **Guidance**: Efficiency target for token-constrained LLM memory (not strict limit)
  - Features MAY exceed 200 tokens if clinical nuance requires; SHALL NOT sacrifice critical detail

  **T810A-ADR-003-FR-003 (Content Pattern)**
  - **Template**: Time → Event → Symptom/Meal/Stool → Analysis Summary
  - **Example**: "8:30 AM — Breakfast: scrambled eggs, toast, coffee | 10:00 AM — Mild bloating (severity 3/10) | 12:00 PM — BM (Bristol Type 4, no urgency) | Analysis: Post-breakfast bloating suggests possible egg sensitivity; normal stool consistency indicates no acute GI distress"
  - **Chronological Ordering**: Events in time sequence

  **T810A-ADR-003-FR-004 (Trigger Mechanisms)**
  - **Session-End Auto**: Agent offers report at natural conversation conclusion
  - **Patient Request**: "/report", "can you summarize today?", "generate my daily report"
  - **Mid-Session**: Agent MAY generate interim reports if patient requests

  **T810A-ADR-003-FR-005 (Validation Loop)**
  - **Draft Presentation**: Conversational tone per `T810A-QG-002`
  - **Patient Review**: Reviews for accuracy/completeness
  - **Correction Protocol**: Patient corrects → Agent adjusts → Patient confirms
  - **Phrasing**: "Does this summary capture your day accurately?" (NOT blocking)
  - **Authority**: Patient has final authority

  **T810A-ADR-003-FR-006 (JSON Export Schema)**
  - **Dual Output**: (1) Markdown narrative (clinician-shareable); (2) Structured JSON (appended to Dynamic JSON per `T810A-IG-004`)
  - **JSON Structure**: `{"session_date": "YYYY-MM-DD", "report_markdown": "<text>", "entries_count": N, "validation_status": "confirmed"}`

  **T810A-ADR-003-FR-007 (A1/A3 Coordination)**
  - **T810A1**: Generate session-end report
  - **T810A3**: Aggregate multi-session reports per `T810A-DEP-002`
  - **Handoff**: A1 exports markdown+JSON → A3 consumes per `T810A-IG-006`
  - **Stability**: Core structure remains stable for aggregation

  **Consequences:**
  - (+) Standardized format across features; dual-purpose utility eliminates proliferation
  - (±) First-person voice unconventional; length guidance requires summarization discipline
  - (±) A1/A3 coordination requires format stability
  - (-) Formal handoff features deferred to T810A3

  **Alternatives Considered:**
  - **Option A**: Third-person voice — Rejected: Disconnects patient authorship
  - **Option B**: Separate formats — Rejected: Proliferation; maintenance burden
  - **Option C**: Strict 200-token limit — Rejected: Clinical nuance may require exceeding target

  **References:**
  `T810A-GDR-003 (Dual-Purpose Clinical Reporting)`,
  `T810A-IG-006 (Session Context Injection & Handoff)`,
  `T810A-IG-004 (Dynamic JSON Single-Entry Pattern)`,
  `T810A-QG-002 (Persona & Tone)`,
  `T810A-DEP-002 (Long-term Analysis)`

  **Provenance:**
```

**Client Approval for Full Draft**: ___________

---

## V. GDR-005 CONSULTATION: GI KNOWLEDGE BASE SOURCES

### A. Research Findings Summary

**Epic Scope Test**: PASS
**Classification**: E-GDR (Retain at Epic with abstraction)
**Priority**: MEDIUM
**Confidence**: High

**Feature Applicability Matrix** (from analysis Section III):
- ✅ **T810A1 (PROMPT)**: Clinical reasoning sources for hypothesis generation
- ✅ **T810A2 (PATIENT)**: Vocabulary and scale alignment (Bristol, ROME IV terminology)
- ✅ **T810A3 (REPORT)**: Interpretive consistency for pattern analysis
- ❓ **T810A4 (TOOLS)**: Future tools may reference clinical knowledge

**Epic Appropriateness**: Knowledge governance belongs at Epic level; sources inform reasoning across all clinical features.

**Implementation Details Identified** (from analysis Section IV):
1. **"Block 4" reference** — Replace with "designated knowledge storage"
2. **Maintenance policy details** — Move enumerations/versioning cadence to ADR

**E-RID Mapping Validation** (from analysis Section V):
- **Current F-RID refs**: T810A1-NFR-004, IF-003, CON-006/007, DEP-005
- **Proposed E-RID mapping**:
  - NFR-004 → `T810A-QG-004` (Holistic Analysis)
  - IF-003 → `T810A-IG-003` (Explicit Classification)
  - CON-006 → `T810A-CON-002` (Platform Compatibility)
  - CON-007 → `T810A-CON-003` (Clinical Compliance Deferral)
  - DEP-005 → `T810A-DEP-005` (Clinical Safety Framework)
- **Missing coverage**: None
- **Circular reference risk**: Low

**Recommended Revision Strategy** (from analysis Section VI): **ABSTRACTION**
- Move source enumerations and maintenance policy to ADR-005
- Keep governance principle in GDR

---

### B. Critical Question Resolution

**Question**: No critical question flagged for GDR-005 in research Section VIII.

**Abstraction Decision**: Move authoritative source list (ROME IV, Bristol, ACG/AGA, alarm features) and versioning/maintenance cadence to ADR-005; retain governance principle in GDR.

**Client Confirmation**: ___________

---

### C. Proposed Revised GDR Language

**Current GDR-005 Body** (from SPS):
```markdown
* **T810A-GDR-005 (GI Knowledge Base Sources) {#t810a-gdr-005-knowledge-sources}**

  **Context.** Research validation (`T810A-RES-001` Deliverable D) identifies ROME IV criteria, Bristol Stool Chart, ACG/AGA clinical guidelines, and alarm features as essential GI expert knowledge sources for diagnostic reasoning and safety escalation. Without explicitly defined knowledge base sources, the agent risks relying on general training knowledge that may be outdated, incomplete, or inconsistent with current gastroenterology best practices. The agent's core competencies per `T810A1-NFR-004` (holistic analysis incorporating adjacent factors) and clinical reasoning requirements depend on authoritative, validated clinical knowledge rather than general LLM training corpus.

  **Decision.** Adopt **GI Knowledge Base Source Standard** establishing authoritative clinical knowledge for LLM_Gastro Knowledge Base (Block 4):

  **Diagnostic Frameworks**:
  - **ROME IV Criteria**: Functional gastrointestinal disorder classification (IBS, functional dyspepsia, etc.)
  - **Bristol Stool Chart**: Stool type classification system (Types 1-7) for multimodal image analysis per `T810A1-IF-003`

  **Clinical Guidelines**:
  - **ACG Guidelines**: American College of Gastroenterology evidence-based recommendations
  - **AGA Guidelines**: American Gastroenterological Association clinical practice guidelines
  - **International Consensus** (WHO/ISO): Global standards per `T810A1-S01-FR-003` (metric units, 24-hour time)

  **Safety Escalation Knowledge**:
  - **Alarm Features**: Red-flag symptoms requiring immediate medical evaluation (e.g., unexplained weight loss, persistent vomiting, blood in stool, severe abdominal pain)
  - **Escalation Thresholds**: Criteria triggering "discuss with your gastroenterologist urgently" guidance

  **Maintenance Policy**:
  - Knowledge Base sources SHALL be explicitly documented in Block 4 with version/date references where applicable
  - Agent SHALL frame all hypotheses as "working theories for clinician discussion" per `T810A1-CON-007` (diagnostic stance)
  - Safety escalation remains **prompt-level guidance only** (no comprehensive safety framework) per `T810A1-DEP-005`

  This decision establishes authoritative clinical knowledge foundation while maintaining appropriate scope boundaries (prompt-level safety guidance, not regulatory compliance).

  **Consequences.**
  - (+) Evidence-based clinical reasoning grounded in industry-recognized gastroenterology standards
  - (+) Explicit source documentation enables knowledge base versioning and updates
  - (+) Bristol Stool Chart standardization supports consistent image classification per trust-and-verify workflow
  - (+) Alarm features knowledge enables basic safety escalation within prompt-level scope
  - (±) Requires periodic knowledge base updates as clinical guidelines evolve; maintenance responsibility acknowledged
  - (±) ROME IV/ACG/AGA guidelines are US-centric; international guidelines may vary (mitigated by general LLM training for global context)
  - (-) Comprehensive safety framework deferred per `T810A1-CON-007`; MVP relies on ChatGPT native safety per `T810A1-CON-006`

  **References.**
  `T810A-RES-001` (Deliverable D: GI Expert Workflows),
  `T810A1-NFR-004` (Holistic Analysis),
  `T810A1-IF-003` (Explicit Classification),
  `T810A1-CON-006` (Platform Compatibility),
  `T810A1-CON-007` (Clinical Compliance Deferral),
  `T810A1-DEP-005` (Clinical Safety Framework Dependency)
```

**Proposed Revised GDR Language** (Epic-level abstraction, compressed to ~100 words):
```markdown
* **T810A-GDR-004 (GI Knowledge Base Sources)** {#t810a-gdr-004-gi-knowledge-sources}

  **Context:** Per `T810A-RES-001` Deliverable D, authoritative GI sources (ROME IV, Bristol Chart, ACG/AGA guidelines, alarm features) are essential for diagnostic reasoning and safety escalation. Without explicit catalog, features risk outdated/incomplete knowledge.

  **Decision:** Features requiring clinical GI knowledge SHALL: 
  (1) ground reasoning in authoritative sources per `T810A-ADR-004`; 
  (2) store references in designated knowledge storage; 
  (3) frame hypotheses as "working theories for clinician discussion" per `T810A-CON-003`; 
  (4) operate within constraints per `T810A-DEP-005`/`T810A-CON-002`. 
  
  Adopt `T810A-ADR-004`, defining source catalog, versioning, update cadence, deprecation, maintenance governance.

  **Consequences:**
  - (+) Evidence-based reasoning per `T810A-RES-001`; catalog enables versioning without GDR changes
  - (±) Periodic updates required; US-centric guidelines mitigated by LLM global training
  - (-) Comprehensive safety deferred per `T810A-CON-003`

  **References:**
  `T810A-RES-001 (System Architecture & Clinical Validation)`,
  `T810A-QG-004 (Holistic Analysis)`,
  `T810A-IG-003 (Explicit Classification)`,
  `T810A-CON-002 (Platform Compatibility)`,
  `T810A-CON-003 (Clinical Compliance Deferral)`,
  `T810A-DEP-005 (Clinical Safety Framework)`,
  `T810A-ADR-004 (GI Knowledge Sources Catalog)`
```

**Key Abstraction Changes**:
- Added list item format `* **...` per T102-ADR-004-FR-002
- Added periods after all bold subheading labels
- Moved all content inside bold subheadings
- Added **Consequences.** section with (+)/(±)/(-) bullets from original GDR-005
- Added "Adopt `T810A-ADR-004`..." statement in **Decision.** per plan Section 1.1
- Added `T810A-RES-001` reference as research foundation
- Fixed **References.** format to comma-separated backticked items
- Removed specific source enumeration (ROME IV, Bristol, ACG/AGA, alarm features) → moved to ADR-005
- Removed "Block 4" reference → "designated knowledge storage"
- Removed versioning/maintenance details → deferred to ADR-005
- Maintained governance principle: grounding in authoritative sources
- E-RID references only (no F-RID citations)

**Client Approval**: ___________

---

### D. Proposed Epic ADR (Full Draft — Phase 3B+3C Combined)

**ADR Full Draft**: `T810A-ADR-004 (GI Knowledge Sources Catalog)`

```markdown
* **T810A-ADR-004 (GI Knowledge Sources Catalog)** {#t810a-adr-004-gi-sources-catalog}

  **Context:** Per `T810A-GDR-004`, features must ground clinical GI reasoning in authoritative sources. Research (`T810A-RES-001` Deliverable D) identifies ROME IV, Bristol Chart, ACG/AGA guidelines, and alarm features as essential for diagnostic reasoning and safety escalation. This ADR centralizes catalog, versioning, update cadence, and maintenance governance for ADR-level updates without GDR changes.

  **Decision:** Establish GI Knowledge Sources Catalog as centralized, versioned reference for all Epic features requiring clinical GI knowledge.

  **Specification:**

  **T810A-ADR-004-FR-001 (Diagnostic Frameworks)**
  - **ROME IV Criteria**: Functional GI disorder classification (IBS, functional dyspepsia/constipation); Version ROME IV (2016), monitored for ROME V
  - **Bristol Stool Chart**: Types 0-7 (Type 0="nothing" per ADR-002-FR-003; Types 1-2 constipation, 3-4 normal, 5-7 diarrhea); Application: multimodal analysis per `T810A-IG-003`, patient self-reporting

  **T810A-ADR-004-FR-002 (Clinical Practice Guidelines)**
  - **ACG**: IBS management, functional dyspepsia treatment, colorectal cancer screening
  - **AGA**: Clinical practice updates for functional GI disorders, diagnostic testing
  - **International**: WHO/ISO standards (metric units, 24-hour time), global dietary terminology

  **T810A-ADR-004-FR-003 (Safety Escalation)**
  - **Alarm Features**: Unexplained weight loss (>10 lbs), persistent vomiting (>24h), blood in stool, severe abdominal pain, nocturnal diarrhea, rectal bleeding, family history colorectal cancer/IBD
  - **Thresholds**: "Discuss with gastroenterologist urgently" triggers
  - **Stance**: Frame as "working theories for clinician discussion" per `T810A-CON-003`

  **T810A-ADR-004-FR-004 (Versioning)**
  - **Tracking**: Version/publication year (e.g., "ROME IV (2016)", "ACG IBS Guidelines (2021)")
  - **Effective Dates**: Track adoption into knowledge base
  - **Deprecation**: Note replacement source and migration date

  **T810A-ADR-004-FR-005 (Update Cadence)**
  - **Annual Review**: Catalog reviewed annually
  - **Triggered Updates**: Upon major guideline publication (ROME V, ACG/AGA revisions)
  - **Safety-Critical**: Immediate alarm features updates
  - **Notification**: Features notified of breaking changes

  **T810A-ADR-004-FR-006 (Deprecation Procedures)**
  1. Monitor professional society publications
  2. Evaluate A1/A2/A3 impact
  3. Document replacement strategy
  4. Changelog entry with effective date
  5. Brief subconsultants

  **T810A-ADR-004-FR-007 (Maintenance Governance)**
  - **Owner**: Client (source adoption/deprecation authority)
  - **Updates**: LLM_Consultant proposes, Client approves
  - **Approval Gates**: Clinical source changes require explicit Client approval
  - **Documentation**: ADR body version history
  - **Traceability**: Link to research IDs, guideline publications, clinical advisories

  **Consequences:**
  - (+) Centralized catalog; easier maintenance; versioning enables evolution tracking
  - (±) Annual review discipline required; US-centric guidelines; A1/A2/A3 coordination
  - (-) Comprehensive safety deferred per `T810A-CON-003`

  **Alternatives Considered:**
  - **Option A**: Distributed references — Rejected: Maintenance burden, version drift
  - **Option B**: Embed in GDR — Rejected: GDR updates for every guideline change
  - **Option C**: External file — Rejected: Lacks traceability

  **References:**
  `T810A-GDR-004 (GI Knowledge Base Sources)`,
  `T810A-QG-004 (Holistic Analysis)`,
  `T810A-IG-003 (Explicit Classification)`,
  `T810A-CON-002 (Platform Compatibility)`,
  `T810A-CON-003 (Clinical Compliance Deferral)`,
  `T810A-DEP-005 (Clinical Safety Framework)`

  **Provenance:**
```

**Client Approval for Full Draft**: ___________

---

## VI. CROSS-REFERENCE STYLE DECISION (APPLIES TO ALL GDRs)

### Critical Question Resolution

**Question** (from analysis Section VIII, Question 5):
Should Epic GDRs ever cite Feature IDs directly?

**Options**:
- **Option A**: Allow direct F-RID citations
  - **Cons**: Violates traceability rules; creates coupling
- **Option B**: Require E-RID substitution or cross-reference to Epic artifacts (IG/QG/DEP/ASSUM/CON) only
  - **Pros**: Governance hygiene; proper precedence hierarchy
  - **Cons**: None (aligns with T102-ADR-005)

**Research Recommendation**: **Option B** (E-RID only)

**Implementation**: All 4 revised GDRs above use E-RID references only (T810A-QG-###, T810A-IG-###, T810A-CON-###, T810A-DEP-###, T810A-ADR-###). No F-RID citations appear in GDR bodies.

**Client Confirmation**: ___________

---

## VII. PHASE 3B SUMMARY & NEXT STEPS

### A. Consultation Outcomes

**GDR Revisions Proposed**:
- ✅ **GDR-002** (Trust-and-Verify) → Revised as **GDR-001** (ADR extraction) — HIGH priority
- ✅ **GDR-003** (Stable/Dynamic JSON) → Revised as **GDR-002** (IG reference abstraction) — HIGH priority
- ✅ **GDR-006** (Dual-Purpose Reporting) → Revised as **GDR-003** (Hybrid split) — HIGH priority
- ✅ **GDR-005** (GI Knowledge Sources) → Revised as **GDR-004** (Abstraction) — MEDIUM priority

**ADR Stubs Created**:
- ✅ **T810A-ADR-001** (Trust-and-Verify Confidence Policy) — Linked to GDR-001
- ✅ **T810A-ADR-004** (GI Knowledge Sources Catalog) — Linked to GDR-004
- ✅ **T810A-ADR-003** (Dual-Purpose Reporting Policy) — Linked to GDR-003

**Critical Questions Resolved**:
- ✅ **Q1** (GDR-002): Retain numeric thresholds in ADR → Client decision: ___________
- ✅ **Q2** (GDR-003): Reference E-IG-005/006 for session init → Client decision: ___________
- ✅ **Q3** (GDR-006): Voice/length as ADR guidance → Client decision: ___________
- ✅ **Q4** (Cross-reference): E-RID only, no F-RID citations → Client confirmation: ___________

### B. Client Approval Gate

**Phase 3B Approval Checklist**:
- [ ] All 4 revised GDR language proposals approved
- [ ] All 3 ADR stub content scopes approved
- [ ] All 4 critical questions resolved with client decisions
- [ ] E-RID reference compliance confirmed (no F-RID citations in GDR bodies)

**Authorization to Proceed**:
- [ ] **Phase 3C**: Expand ADR stubs into full drafts with T102-ADR-004 compliance
- [ ] **Phase 3D**: Renumber GDRs (002→001, 003→002, 006→003, 005→004); handle demoted GDR-001/004
- [ ] **Phase 3E**: Implement in SPS/Concept artifacts; draft T810A1 coordination brief

**Client Approval**: ___________

---

## VIII. CLARIFYING QUESTIONS

To ensure Phase 3C (ADR full drafts) addresses all requirements and risks:

1. **ADR Specification Depth**: For Phase 3C full ADR drafts, should Specification sections include detailed FR-### functional requirements (similar to T102-ADR-004 exemplar) or high-level content descriptions?

2. **Numeric Threshold Calibration** (ADR-002): Should internal numeric ranges (70%, 90%) be treated as fixed thresholds or guideline ranges subject to feature-specific calibration?

3. **GDR Conciseness Target**: Current revised GDR bodies are ~150-200 words. Should they be further compressed to ~100 words or is current length acceptable for "concise, direct, authoritative" per client guidance?

4. **ADR Provenance Documentation**: Should Phase 3C ADR drafts include detailed provenance sections citing research analysis findings and T810A1 Request sources, or brief provenance statements?

5. **Phase 4 Issues/Risks Integration**: Research Section IX identified 2 new Issues + 1 new Risk. Should these be integrated into Phase 4 (Epic Issues & Risks Triage) or addressed separately before Phase 4?
