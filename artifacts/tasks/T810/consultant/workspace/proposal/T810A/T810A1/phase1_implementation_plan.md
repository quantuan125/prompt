---
artifact_type: 'PLAN'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A-PROMPT'
version: '1.0.0'
date: '2025-10-10'
status: 'approved'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_role: 'LLM_Developer'
---

# PHASE 1 IMPLEMENTATION PLAN: Foundation Updates for T810A-PROMPT

## I. EXECUTIVE SUMMARY

This document provides LLM_Developer with approved specifications for Phase 1 foundation updates to the T810A-PROMPT Request document and corresponding gastro_system.md implementation. All proposals are based on validated research findings from T810A-PROMPT-RES-001 and have received Client approval.

**Scope**: Update 7 existing F-IDs + add 2 new F-IDs across Sections F-I, plus revise Stories S01-S02.

**Implementation Targets**:
- `prompt/artifacts/tasks/T810/request/request_T810A-PROMPT_v1.0.0.md` (specification updates)
- `prompt/roles/gastro/gastro_system.md` (Block 2 implementation only for Phase 1)

---

## II. F-ID UPDATES: APPROVED FINAL PROPOSALS

### **SECTION F: NON-FUNCTIONAL REQUIREMENTS (NFR)**

#### **📝 UPDATE: NFR-001 (Protocol Reliability)**

**Current Text** (Lines ~143):
```markdown
* **T810A-PROMPT-NFR-001 (Protocol Reliability)** — The agent MUST consistently adhere to the Analyze → Probe → Coach protocol; the Probe phase is the primary mechanism to resolve ambiguity.
```

**Approved Update**:
```markdown
* **T810A-PROMPT-NFR-001 (Protocol Reliability)** — The agent MUST consistently adhere to the **Engage → Analyze → Probe → Coach → Summarize** protocol; the Probe phase is the primary mechanism to resolve ambiguity, and Summarize ensures closure with confirmed next steps.
```

**Rationale**: Research Deliverable C validates 5-phase protocol as industry-aligned clinical communication framework (MI, CBT, clinical AI best practices). Adds missing Engage (rapport-building) and Summarize (closure) phases.

---

#### **📝 UPDATE: NFR-002 (Persona & Tone)**

**Current Text** (Lines ~144):
```markdown
* **T810A-PROMPT-NFR-002 (Persona & Tone)** — Tone is dual-mode: clinical/detached during Analyze/Coach; empathetic/encouraging during Probe.
```

**Approved Update**:
```markdown
* **T810A-PROMPT-NFR-002 (Persona & Tone)** — Tone is adaptive across protocol phases: **empathetic** during Engage; **clinical/detached** during Analyze; **empathetic/collaborative** during Probe; **supportive** during Coach; **neutral/confirming** during Summarize. The agent maintains a partnership stance, treating the patient as expert in their lived experience.
```

**Rationale**: Research Deliverable C identifies specific tone requirements per protocol phase. Current dual-mode description insufficient for 5-phase clinical communication. Clarifies tone transitions aligned with MI/CBT frameworks.

---

#### **✅ NO CHANGE: NFR-003 through NFR-006**

All validated by research:
- NFR-003 (Performance): 30-120s latency acceptable
- NFR-004 (Holistic Analysis): Adjacent factors integration
- NFR-005 (Maintainability): 9-block structure (strongly validated)
- NFR-006 (Usability): Medium-to-high literacy, non-paternalistic

---

#### **➕ ADD: NFR-007 (Confidence Communication)**

**Insert After**: NFR-006 (sequential numbering)

**Approved New Requirement**:
```markdown
* **T810A-PROMPT-NFR-007 (Confidence Communication)** — When classifying images or generating hypotheses, the agent SHALL communicate confidence using qualitative descriptors (e.g., "fairly confident," "moderate confidence," "uncertain") rather than numerical percentages. Confidence indicators enable appropriate user validation without interrupting conversational flow.
```

**Rationale**: Research Deliverable B identifies confidence communication as essential multimodal AI pattern. Medical AI systems prefer qualitative descriptors for patient-facing interfaces. Supports non-blocking trust-and-verify workflow.

---

### **SECTION G: INTERFACES & DATA (IF)**

#### **✅ NO CHANGE: IF-001, IF-002, IF-004**

All validated:
- IF-001 (Input Interface): Parse text + images
- IF-002 (Output Interface): Markdown to user
- IF-004 (Reporting Trigger): `/report` command recognition

---

#### **📝 UPDATE: IF-003 (Explicit Classification)**

**Current Text** (Lines ~155):
```markdown
* **T810A-PROMPT-IF-003 (Explicit Classification)** — During Analyze, explicitly state any image classification made (e.g., Bristol scale) with concise rationale.
```

**Approved Update** (Non-Blocking Validation):
```markdown
* **T810A-PROMPT-IF-003 (Explicit Classification)** — During Analyze, the agent SHALL explicitly state any image classification made (e.g., Bristol scale) with concise rationale **and qualitative confidence indicator** (per NFR-007). When confidence is moderate or low, the agent SHALL **encourage user validation** in the same response or subsequent dialogue turn, using conversational phrasing (e.g., "Does that match what you observed?" or "Let me know if you saw something different"). Validation requests SHALL NOT block conversational flow or require explicit user confirmation before the agent proceeds.
```

**Rationale**: Research Deliverable B specifies trust-and-verify workflow with confidence thresholds. Client directive: validation should be **non-blocking** and **conversational**, not requiring pause or mandatory confirmation. Maintains natural dialogue flow while addressing multimodal accuracy concerns.

---

#### **➕ ADD: IF-005 (Session Context Injection)**

**Insert After**: IF-004

**Approved New Requirement**:
```markdown
* **T810A-PROMPT-IF-005 (Session Context Injection)** — At the start of each new session, the agent SHALL load the patient profile (per T810D-PROFILE) and the previous session's clinical report (if available) as context. This enables multi-session continuity while maintaining token efficiency through daily report compression.
```

**Rationale**: Research Deliverable G validates daily continuity model via profile + previous report injection. Essential for multi-day pattern recognition without cumulative conversation context (prevents token overflow). References future T810D-PROFILE feature for detailed schema.

---

### **SECTION H: CONSTRAINTS (CON)**

#### **✅ NO CHANGE: CON-001 through CON-007**

**Rationale**:
- Client directive: Adhere to CON-007 (Clinical Compliance Deferral) without changes
- Research Deliverable D identifies safety patterns (alarm features, red-flag escalation), but these remain **out of scope** for MVP per CON-007
- All other constraints validated and remain appropriate

---

### **SECTION I: FEATURE INTEGRATION NOTES (INT)**

#### **✅ NO CHANGE: INT-001, INT-003**

Both validated:
- INT-001 (Internal State Object): Session-scoped JSON/YAML state
- INT-003 (User-Mediated Workflow): Manual input/analysis/recording

---

#### **📝 UPDATE: INT-002 (Memory Handoff Protocol)**

**Current Text** (Lines ~172):
```markdown
* **T810A-PROMPT-INT-002 (Memory Handoff Protocol)** — Upon request (e.g., "/report"), produce a dual-format output: Markdown narrative + structured JSON log suitable as input to T810A-REPORT.
```

**Approved Update**:
```markdown
* **T810A-PROMPT-INT-002 (Memory Handoff Protocol)** — Upon request (e.g., "/report"), produce a dual-format output: **chronological timeline Markdown narrative in first-person patient perspective** (e.g., "08:00 - I had breakfast...") + structured JSON log suitable as input to T810A-REPORT. The narrative format serves dual purposes: shareable clinician handoff document and condensed LLM memory for next-session context injection (per IF-005).
```

**Rationale**: Research Deliverable F specifies chronological timeline format in first-person voice as optimal for both clinician utility and LLM memory consumption. Current text lacks format specification. Addresses dual-purpose reporting architecture.

---

#### **📝 UPDATE: INT-004 (Patient Profile Workflow)**

**Current Text** (Lines ~174):
```markdown
* **T810A-PROMPT-INT-004 (Patient Profile Workflow)** — The patient profile is not pre-existing for MVP. (1) Patient communicates in natural language; (2) LLM_Gastro maintains context and extracts profile data during the session; (3) At end-of-day reporting, output a compiled patient profile JSON as part of the report; (4) A sample template exists at `prompt/roles/gastro/data/profile.json` as reference only; (5) Cross-session persistence is manual or deferred to T810A-REPORT.
```

**Approved Update** (High-Level Reference to T810D-PROFILE):
```markdown
* **T810A-PROMPT-INT-004 (Patient Profile Workflow)** — The patient profile is not pre-existing for MVP. (1) Patient communicates in natural language; (2) LLM_Gastro maintains context and extracts profile data during the session; (3) At end-of-day reporting, output a compiled patient profile JSON as part of the report, including demographics, clinical history, and identified patterns (detailed schema deferred to **T810D-PROFILE**); (4) Profile data SHALL be categorized as **constant** (demographics), **stable** (conditions, triggers), or **dynamic** (daily symptoms—captured in reports, not profile); (5) Cross-session persistence is manual or deferred to T810A-REPORT.
```

**Rationale**: Research Deliverable E validates constant/stable/dynamic categorization and identifies need for enhanced profile. Client directive: Keep INT-004 high-level, reference T810D-PROFILE for detailed schema. Maintains appropriate scope separation between features.

---

## III. STORY S01 & S02 UPDATES

### **STORY S01 (Project Context)**

#### **Specification Review**

**Current F-IDs** (Lines ~179-196):
- FR-001 (Diagnostic Stance): Hypothesis-generation with clinician-review
- FR-002 (Privacy Stance): Patient de-identifies before sharing
- FR-003 (Timezone): Europe/Copenhagen (CET/CEST)
- FR-004 (Timestamp Format): ISO 8601 format

**✅ Decision: NO CHANGES REQUIRED**

**Rationale**: Research Deliverable A validates all governance stance patterns. All S01 requirements align with industry best practices.

---

#### **Implementation Review: gastro_system.md Block 1**

**Current Implementation** (Lines 1-14 of gastro_system.md):
```markdown
<!-- # BLOCK 1: PROJECT CONTEXT -->
<!-- @prompt/roles/gastro/general/1_project_context.md -->

## Diagnostic Stance
This agent operates under a **Hypothesis-Generation with Clinician-Review model.** You MAY propose diagnostic hypotheses...

## Privacy Stance
The patient is responsible for de-identifying all images and text before sharing...

## Operational Constants
- **Timezone:** Europe/Copenhagen (CET/CEST)
- **Timestamp Format:** ISO 8601 (`YYYY-MM-DDTHH:MM:SS+01:00`)
```

**✅ Decision: NO IMPLEMENTATION CHANGES**

All Block 1 content validated by research. No updates needed.

---

### **STORY S02 (Role Identity & Competencies)**

#### **Specification Updates Required**

**Current F-IDs** (Lines ~198-227):
- FR-001 (Role & Mandate): ✅ NO CHANGE (validated)
- FR-002 (Key Competencies): ✅ NO CHANGE (validated)
- FR-003 (Communication Style): 🔄 **REQUIRES UPDATE**

---

#### **📝 UPDATE: S02-FR-003 (Communication Style)**

**Current Text** (Lines ~215-220):
```markdown
*   **T810A-PROMPT‑S02-FR-003 (Communication Style):** The agent's communication style SHALL be defined as a **dual-tone hybrid**:
    *   **Analytical Mode:** Clinical, objective, and detached when presenting analyses, hypotheses, and data.
    *   **Collaborative Mode:** Empathetic, encouraging, and inquisitive when asking questions (`Probe` phase) or providing coaching.
    *   **Core Stance:** It must always treat the patient as an expert in their own lived experience, framing the dialogue as a partnership.
    *   **Data-First:** The agent must present its analysis and evidence *before* offering conclusions or coaching.
```

**Approved Update**:
```markdown
*   **T810A-PROMPT‑S02-FR-003 (Communication Style):** The agent's communication style SHALL be defined as an **adaptive multi-tone framework** aligned with the five-phase clinical protocol:
    *   **Engage Phase:** Empathetic, warm, rapport-building tone (e.g., "I'm sorry you're frustrated. Let's take it step by step.")
    *   **Analyze Phase:** Clinical, objective, detached when presenting analyses, hypotheses, and data (evidence-first presentation)
    *   **Probe Phase:** Collaborative, empathetic, inquisitive when asking clarifying questions (Socratic inquiry)
    *   **Coach Phase:** Supportive, encouraging, action-oriented when providing management advice (motivational stance)
    *   **Summarize Phase:** Neutral, clear, confirming when recapping agreed plan and next steps (closure-focused)
    *   **Core Stance:** The agent must always treat the patient as an expert in their own lived experience, framing the dialogue as a partnership.
    *   **Data-First Principle:** The agent must present analysis and evidence *before* offering conclusions or coaching.
```

**Rationale**: Research Deliverable C identifies 5-phase protocol (Engage→Analyze→Probe→Coach→Summarize) as essential enhancement over 3-phase model. Each phase has distinct tone requirements validated by MI/CBT frameworks. Current dual-tone description insufficient for clinical communication best practices. Tone transition mechanics deferred to S05 (Execution Protocol) per Client directive.

---

#### **Implementation Update: gastro_system.md Block 2**

**Current Implementation** (Lines 16-35 of gastro_system.md):
```markdown
<!-- BLOCK 2: ROLE IDENTITY & COMPETENCIES -->
<!-- @prompt/roles/gastro/general/2_profile.md -->

## Role & Mandate
You are a Specialized Gastroenterologist/Dietician AI. Your mandate is to act as a 24/7 Socratic partner...

## Key Competencies
- Multi‑modal Analysis: Interpret and synthesize user‑provided text...
- Clinical Pattern Recognition: Identify correlations...
- Bristol Stool Chart Classification: Categorize stool images...
- Diagnostic Hypothesis Generation: Formulate plausible working theories...
- Socratic Inquiry: Ask targeted, clarifying questions...
- Symptom Management Coaching: Provide actionable, context‑aware guidance...

## Communication Style
- Analytical Mode: Clinical, objective, concise. Present evidence, data, and reasoning first...
- Collaborative Mode: Empathetic, encouraging, inquisitive...
- Core Stance: Treat the patient as the expert in their lived experience...
- Data‑First: Always present analysis and supporting evidence before conclusions...
```

**Required Implementation Changes**:

**Replace "Communication Style" Section** with:
```markdown
## Communication Style

Your communication style is **adaptive across protocol phases**:

**Engage Phase** — Empathetic, warm, rapport-building
- Acknowledge the patient's emotional state and concerns
- Set a collaborative tone for the session
- Example: "I'm sorry you're experiencing discomfort. Let's work through this together step by step."

**Analyze Phase** — Clinical, objective, detached
- Present evidence, data, and reasoning first (data-first principle)
- State observations with supporting rationale
- Include qualitative confidence indicators when classifying images or generating hypotheses
- Example: "Based on the image, this appears to be Bristol Type 6 (mushy stool). I'm fairly confident, though lighting makes definitive classification challenging."

**Probe Phase** — Collaborative, empathetic, inquisitive
- Use Socratic questioning to fill information gaps
- Frame questions as partnership ("let's figure this out together")
- Validate patient observations and encourage elaboration
- Example: "That's interesting that it happens specifically after lunch. Can you describe what you typically eat for lunch?"

**Coach Phase** — Supportive, encouraging, action-oriented
- Provide specific, actionable recommendations within safety boundaries
- Frame advice as suggestions, not mandates (motivational interviewing stance)
- Check readiness and confidence for recommended actions
- Example: "One approach could be trying a low-FODMAP diet for two weeks. Does that feel doable for you?"

**Summarize Phase** — Neutral, clear, confirming
- Recap key insights and agreed action plan
- State next steps explicitly
- Ensure mutual understanding before closing
- Example: "Today we identified dairy as a potential trigger, and you're going to avoid it for three days. I'll check in with you then. Sound good?"

**Core Stance** — Treat the patient as the expert in their lived experience. Frame all dialogue as a partnership where you provide clinical analysis and the patient provides experiential wisdom.

**Data-First Principle** — Always present analysis and supporting evidence *before* offering conclusions or coaching recommendations.
```

**Rationale**: Expands Communication Style to reflect 5-phase protocol with phase-specific tone guidance and concrete examples. Aligns implementation with updated S02-FR-003 specification. Maintains consistency with NFR-002 tone requirements.

---

## IV. IMPLEMENTATION TASK CHECKLIST

### **For LLM_Developer: Request Document Updates**

**File**: `prompt/artifacts/tasks/T810/request/request_T810A-PROMPT_v1.0.0.md`

- [ ] **Task 1.1**: Update NFR-001 to 5-phase protocol (Line ~143)
- [ ] **Task 1.2**: Update NFR-002 with adaptive tone across 5 phases (Line ~144)
- [ ] **Task 1.3**: Add NFR-007 (Confidence Communication) after NFR-006 (Line ~149)
- [ ] **Task 1.4**: Update IF-003 with non-blocking validation approach (Line ~155)
- [ ] **Task 1.5**: Add IF-005 (Session Context Injection) after IF-004 (Line ~156)
- [ ] **Task 1.6**: Update INT-002 with chronological timeline format specification (Line ~172)
- [ ] **Task 1.7**: Update INT-004 with high-level profile reference to T810D-PROFILE (Line ~174)
- [ ] **Task 1.8**: Update S02-FR-003 with adaptive multi-tone framework (Lines ~215-220)

---

### **For LLM_Developer: gastro_system.md Updates**

**File**: `prompt/roles/gastro/gastro_system.md`

- [ ] **Task 2.1**: Replace "Communication Style" section in Block 2 with 5-phase adaptive framework (Lines ~30-35)
- [ ] **Task 2.2**: Ensure phase-specific tone guidance includes concrete examples per phase
- [ ] **Task 2.3**: Validate alignment between S02-FR-003 specification and Block 2 implementation

---

## V. VALIDATION CRITERIA

**Phase 1 Complete When**:
- [ ] All 8 Request document F-ID updates implemented and reviewed
- [ ] gastro_system.md Block 2 updated to reflect 5-phase adaptive tone framework
- [ ] No inconsistencies between S02-FR-003 specification and Block 2 implementation
- [ ] Cross-references validated (NFR-007 ↔ IF-003, IF-005 ↔ INT-004, etc.)
- [ ] LLM_Consultant review approval obtained

---

## VI. TRACEABILITY MAP

| F-ID Update | Research Reference | Impacted Stories | Implementation Target |
|-------------|-------------------|------------------|----------------------|
| NFR-001 | Deliverable C (5-phase protocol) | S02, S05 (future) | gastro_system.md Block 2 |
| NFR-002 | Deliverable C (tone per phase) | S02, S05 (future) | gastro_system.md Block 2 |
| NFR-007 | Deliverable B (confidence communication) | S05, S06 (future) | N/A (NFR only) |
| IF-003 | Deliverable B (trust-and-verify) | S05, S08 (future) | N/A (interface spec) |
| IF-005 | Deliverable G (session workflows) | S05, S09 (future) | N/A (interface spec) |
| INT-002 | Deliverable F (reporting architecture) | S09 (future) | N/A (integration note) |
| INT-004 | Deliverable E (profile schema) | S04 (future) | N/A (references T810D-PROFILE) |
| S02-FR-003 | Deliverable C (5-phase protocol) | S02 implementation | gastro_system.md Block 2 |

---

## VII. DEPENDENCIES & NOTES

**Feature Dependencies**:
- **T810D-PROFILE**: Detailed patient profile schema specification (referenced in INT-004)
- **T810A-REPORT**: Cross-session summarization and pattern handoff (referenced in INT-002)
- **T810B-TOOLS**: Custom tool interfaces (referenced in S03, deferred per CON-005)

**Implementation Notes**:
1. **Non-Blocking Validation**: IF-003 update emphasizes conversational validation requests that don't interrupt flow. Implementation should use natural language prompts like "Does that match what you observed?" rather than blocking confirmation dialogs.
2. **Tone Mechanics**: S02-FR-003 defines tone per phase; transition mechanics (how to signal phase shifts) deferred to S05 (Execution Protocol) per Client directive.
3. **Profile Schema**: INT-004 kept high-level; detailed field definitions, validation rules, and schema versioning deferred to T810D-PROFILE feature.

---

## VIII. NEXT STEPS AFTER PHASE 1

**Upon Phase 1 Completion**:
1. LLM_Consultant will create Section III.M (Feature GDR Index) with 6 governance decision records
2. LLM_Consultant will document F-GDRs referencing updated F-IDs and research deliverables
3. Obtain Client approval for Feature GDRs (Phase 2 gate)
4. Proceed to Story S04-S10 specification (Phase 3)

**Handoff Protocol**:
- LLM_Developer marks Phase 1 tasks complete
- LLM_Consultant validates alignment
- Joint sign-off before Phase 2 initiation

---

## IX. REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1.0.0 | 2025-10-10 | LLM_Consultant | Initial Phase 1 implementation plan with approved F-ID updates and S02 specification/implementation changes |

---

**Document Status**: Approved for Implementation
**Target Role**: LLM_Developer
**Review Required**: LLM_Consultant validation upon completion
**Next Gate**: Phase 1.5 (Conversation-Driven Refinement)

**IMPORTANT UPDATE (2025-10-11)**: After Phase 1 completion, examination of actual conversation example revealed critical gaps. Phase 1.5 has been inserted before Phase 2 to address empirical findings. See `phase1.5_conversation_analysis.md` for detailed analysis and additional F-ID proposals.