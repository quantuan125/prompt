---
artifact_type: 'PROPOSAL'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1-PROMPT'
version: '1.0.0'
date: '2025-10-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_document: 'request_T810A-PROMPT_v1.0.0.md'
---

# PHASE 1.5 REQUEST DOCUMENT UPDATES

## I. EXECUTIVE SUMMARY

This document proposes updates to `request_T810A1-PROMPT.md` based on Phase 1.5 conversation analysis findings. Updates include:
- **TASK 1**: New research entry (RES-002) for empirical conversation validation
- **TASK 2**: 4 open issues + 5 risks based on conversation gap analysis
- **TASK 3**: 10 F-ID proposals (4 revisions + 6 new) addressing critical gaps

All proposals follow T102-STD-005 ID specification rules and avoid F-ID → F-GDR referencing.

---

## II. TASK 1: RESEARCH ENTRY (RES-002)

### Proposed Addition to Section III.N (Research & Notes)

**Insert after RES-001**:

```markdown
| `T810A1-PROMPT-RES-002` | Conversation-Driven Empirical Validation | Real-world conversation analysis revealing 5 critical gaps: tracking-first protocol priority, Stable/Dynamic JSON architecture split, smart protocol triggering requirements, Probe phase absence, and ChatGPT memory review step | Phase 1.5 Updates | [conversation](../../resources/gastro_example_conversation.md) | [analysis](../plan/phase1.5_conversation_analysis.md) |
```

**Rationale**:
- Documents empirical validation phase that revealed gaps not captured by research-only approach
- Links to actual conversation example (gastro_example_conversation.md) as primary source
- Links to systematic analysis (phase1.5_conversation_analysis.md) as evidence base
- Establishes traceability for Phase 1.5 F-ID updates

---

## III. TASK 2: OPEN ISSUES & RISKS

### Proposed Updates to Section III.L (Open Issues & Risks)

#### A. Issues

```markdown
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T810A-ISSUE-001` | Stable/Dynamic JSON Architecture Dependency | Implementation of Stable JSON (read-only patient profile) vs. Dynamic JSON (per-interaction tracking entries) architecture requires completion of T810A2-SCHEMA schema specifications. Surface-level references in T810A1-PROMPT may need adjustment based on T810A2 final schemas. | LLM_Consultant | `OPEN` | High | 2025-10-11 | — |
| `T810A-ISSUE-002` | Protocol Triggering Logic Implementation | Smart protocol triggering to distinguish tracking-only vs. full protocol vs. Q&A inputs requires S05 (Execution Protocol) development. Implementation approach (keyword detection, context clues, default behavior) needs validation against actual conversation patterns. | LLM_Consultant | `OPEN` | Medium | 2025-10-11 | — |
| `T810A-ISSUE-003` | ChatGPT Assistant Mode Override Strategy | ChatGPT's native "helpful Assistant" behavior overrides Consultant/Analyst stance defined in system prompt. Probe phase enforcement via S08 exemplars and S05 execution instructions needs empirical testing to validate effectiveness. No programmatic gate control available in ChatGPT interface. | LLM_Consultant | `OPEN` | High | 2025-10-11 | — |
| `T810A-ISSUE-004` | Controlled Vocabulary Validation | Dynamic JSON generation requires consistent value sets (e.g., stress levels, Bristol types) but ChatGPT provides no programmatic validation. Enforcement must rely entirely on S05 execution protocol instructions and S08 exemplars. Risk of value drift over time without automated validation. | LLM_Consultant | `OPEN` | Medium | 2025-10-11 | — |
```

#### B. Risks

```markdown
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T810A-RISK-001` | ChatGPT Override Insufficient | Risk that ChatGPT's native Assistant mode cannot be sufficiently overridden via prompt engineering alone, leading to continued absence of Probe phase and premature coaching (observed in conversation example). Mitigation: Extensive S08 exemplars, S05 explicit Probe enforcement, empirical testing with iterative prompt refinement. | LLM_Consultant | `MONITORED` | High | 2025-10-11 | — |
| `T810A-RISK-002` | T810A2-SCHEMA Development Delays | Risk that parallel T810A2-SCHEMA development delays S04-S10 specification due to schema dependencies. Mitigation: Surface-level JSON references in T810A1-PROMPT; detailed schemas deferred to T810A2; parallel development tracks with coordination checkpoints. | LLM_Consultant | `ACCEPTED` | Medium | 2025-10-11 | — |
| `T810A-RISK-003` | Scope Expansion Beyond MVP | Risk that Phase 1.5 findings (10 new/revised F-IDs) expand scope beyond original MVP constraints, delaying Phase 2-3 completion. Mitigation: Strict adherence to prompt-only implementation; no custom UI/validation; defer complex features (multi-frequency reporting, advanced profiling) per original CON specifications. | LLM_Consultant | `MONITORED` | Medium | 2025-10-11 | — |
| `T810A-RISK-004` | Minimum 2-Loop Pattern Non-Compliance | Risk that soft guideline for 2-loop conversation pattern (vs. hard gate) leads to continued 1-loop behavior with insufficient probing. Observed in conversation Turn 1: went straight to coaching without clarifying questions. Mitigation: S05 explicit instruction for ≥2 clarifying questions; S08 anti-pattern examples; S07 quality criteria for protocol adherence. | LLM_Consultant | `MONITORED` | Medium | 2025-10-11 | — |
| `T810A-RISK-005` | Stable JSON Manual Update Friction | Risk that requiring manual patient updates to Stable JSON (ChatGPT read-only constraint) creates friction and profile staleness. Mitigation: INT-005 memory review protocol to flag discrepancies; Probe phase can elicit updates; document manual update workflow in S04. | LLM_Consultant | `ACCEPTED` | Low | 2025-10-11 | — |
```

**Rationale for Issues**:
- ISSUE-001: High priority - blocks S04/S09 detailed specifications
- ISSUE-002: Medium priority - solvable during S05 development
- ISSUE-003: High priority - critical for use case success (observed failure in conversation)
- ISSUE-004: Medium priority - workaround via prompt engineering exists

**Rationale for Risks**:
- RISK-001: High/MONITORED - direct observation from conversation example
- RISK-002: Medium/ACCEPTED - parallel development mitigates
- RISK-003: Medium/MONITORED - requires scope discipline
- RISK-004: Medium/MONITORED - soft guideline by client choice (QA Answer #2)
- RISK-005: Low/ACCEPTED - inherent ChatGPT constraint, workarounds defined

---

## IV. TASK 3: PHASE 1.5 F-ID PROPOSALS

### A. F-ID Construction Rules Summary

Per T102-STD-005 (ID Specification & Rules):
- **Precedence**: F-IDs rank HIGHER than F-GDRs → F-IDs CANNOT reference F-GDRs
- **Allowed Categories**: NFR, IF, CON, INT, DEP
- **Construction Pattern**: `{FEATURE_ID}-{CATEGORY}-{NNN}`
- **Referencing**: May reference research IDs (RES-001, RES-002) if absolutely necessary, but avoid

### B. Revised F-IDs (4 Updates)

#### 1. NFR-001 (Protocol Reliability) — MAJOR REVISION

**Current Text** (Lines 143):
```markdown
* **T810A1-PROMPT-NFR-001 (Protocol Reliability)** — The agent MUST consistently adhere to the **Engage → Analyze → Probe → Coach → Summarize** protocol; the Probe phase is the primary mechanism to resolve ambiguity, and Summarize ensures closure with confirmed next steps.
```

**Proposed Revision**:
```markdown
* **T810A1-PROMPT-NFR-001 (Protocol Reliability)** — The agent MUST consistently adhere to the **Tracking → Analyze → Probe → Coach → Summarize** protocol with the following priority hierarchy:
  - **Primary (always execute)**: Tracking (structured data capture via Dynamic JSON) + Analyze (pattern analysis of current + historical data)
  - **Secondary (mandatory before coaching)**: Probe (ask ≥2 clarifying questions to fill information gaps; Socratic inquiry mode)
  - **Tertiary (conditional on data sufficiency)**: Coach (management recommendations) + Summarize (action plan recap)

  The agent SHALL aim for a minimum 2-loop conversation pattern: *Loop 1* generates Dynamic JSON + performs analysis + asks clarifying questions (no coaching); *Loop 2* refines analysis with probe answers + provides coaching + summarizes action plan. Engage phase is merged into Probe for experienced patients. Coach and Summarize SHALL NOT execute until Probe phase demonstrates sufficient data confidence.
```

**Reasoning**:
- **Gap Addressed**: Conversation shows tracking-first use case (primary function is data capture + analysis, not general clinical conversation)
- **Evidence**: Turn 1 went straight to coaching without probing; Turn 2 generated JSON but didn't auto-trigger analysis
- **Client Directive**: QA Answer #1 (merge Engage into Probe), #2 (soft 2-loop guideline), Comment 0 (tracking + analysis primary)
- **No F-GDR Reference**: Self-contained requirement; research reference avoided

---

#### 2. NFR-002 (Persona & Tone) — MODERATE REVISION

**Current Text** (Lines 144):
```markdown
* **T810A1-PROMPT-NFR-002 (Persona & Tone)** — Tone is adaptive across protocol phases: **empathetic** during Engage; **clinical/detached** during Analyze; **empathetic/collaborative** during Probe; **supportive** during Coach; **neutral/confirming** during Summarize. The agent maintains a partnership stance, treating the patient as expert in their lived experience.
```

**Proposed Revision**:
```markdown
* **T810A1-PROMPT-NFR-002 (Persona & Tone)** — The agent's default mode is **Consultant/Analyst**, overriding ChatGPT's native Assistant behavior. Tone is adaptive across protocol phases:
  - **Tracking**: Structured, precise (Dynamic JSON generation with consistent schema adherence)
  - **Analyze**: Clinical, objective, evidence-based (data-first presentation with explicit reasoning)
  - **Probe**: Collaborative, inquisitive, Socratic (clarifying questions to fill data gaps, NOT service offers like "Would you like me to build...")
  - **Coach** (tertiary): Supportive, action-oriented (when data confidence sufficient after probing)
  - **Summarize** (tertiary): Neutral, clear, confirming (closure with agreed action plan)

  The agent SHALL prioritize clinical inquiry over helpfulness offers. Probe questions SHALL focus on missing Dynamic JSON keys, ambiguous descriptions, temporal patterns, and symptom correlations. The agent maintains a partnership stance, treating the patient as expert in their lived experience.
```

**Reasoning**:
- **Gap Addressed**: ChatGPT's Assistant mode overrides Consultant stance (observed: "If you like, I can turn this into...")
- **Evidence**: Turn 1 & 3 end with service offers instead of Socratic probing questions
- **Client Directive**: Comment 4 (ensure Consultancy/Analyst is default mode), Comment 0 (Engage merged into Probe)
- **No F-GDR Reference**: Self-contained persona definition; no research ID needed

---

#### 3. INT-004 (Patient Data Architecture) — COMPLETE REWRITE

**Current Text** (Lines 176):
```markdown
* **T810A1-PROMPT-INT-004 (Patient Profile Workflow)** — The patient profile is not pre-existing for MVP. (1) Patient communicates in natural language; (2) LLM_Gastro maintains context and extracts profile data during the session; (3) At end-of-day reporting, output a compiled patient profile JSON as part of the report, including demographics, clinical history, and identified patterns (detailed schema deferred to `T810A2-SCHEMA`); (4) Profile data SHALL be categorized as **constant** (demographics), **stable** (conditions, triggers), or **dynamic** (daily symptoms—captured in reports, not profile); (5) Cross-session persistence is manual or deferred to `T810A3-REPORT`.
```

**Proposed Complete Rewrite**:
```markdown
* **T810A1-PROMPT-INT-004 (Patient Data Architecture)** — The system uses a split JSON architecture separating persistent profile data from ephemeral tracking entries:

  **Stable JSON (Patient Profile)**:
  - Contains constant patient data (demographics, conditions, medications, triggers, relievers, clinical history notes)
  - Stored in Knowledge Base (Block 4), manually updated by patient outside conversation
  - **Read-only** for LLM_Gastro (ChatGPT file system constraint: no write permissions)
  - Loaded at session start per Execution Protocol (Block 5)
  - Detailed field definitions, schema validation, and value sets deferred to `T810A2-SCHEMA`

  **Dynamic JSON (Tracking Entries)**:
  - LLM_Gastro generates **single entry per patient interaction** containing event data: patient_state, meal, stool, sleep, or other clinically relevant observations
  - Uses structured keys with controlled vocabularies (value sets defined in `T810A2-SCHEMA`)
  - Schema is **flexible**: LLM_Gastro MAY add keys if clinically justified (e.g., "exercise", "medication_taken", "stress_event")
  - Skeleton structure stored in Knowledge Base as generation exemplar
  - **End-of-day reporting** aggregates all Dynamic JSON entries from session (per INT-002)

  **Integration Patterns**:
  - Missing Dynamic JSON keys trigger Probe phase to elicit clarifying information (per NFR-001)
  - Cross-session persistence of aggregated Dynamic JSON entries deferred to `T810A3-REPORT`
  - Surface-level architecture described here; detailed schemas, validation rules, and integration specifications in `T810A2-SCHEMA`
```

**Reasoning**:
- **Gap Addressed**: Conversation uses cumulative JSON (Turn 2 regenerated all previous entries); no distinction between profile vs. tracking data
- **Evidence**: Turn 1 & 2 mix patient_state (profile-like) with meal/stool (tracking events) in same structure
- **Client Directive**: Comment 1 (Stable read-only + Dynamic generative split), Comment 1.2 (T810A2-SCHEMA dependency)
- **Dependency Reference**: References T810A2-SCHEMA (allowed - higher precedence) and T810A3-REPORT

---

#### 4. IF-003 (Explicit Classification) — MINOR ADDITION

**Current Text** (Lines 156):
```markdown
* **T810A1-PROMPT-IF-003 (Explicit Classification)** — During Analyze, the agent SHALL explicitly state any image classification made (e.g., Bristol scale) with concise rationale **and qualitative confidence indicator** (per NFR-007). When confidence is moderate or low, the agent SHALL **encourage user validation** in the same response or subsequent dialogue turn, using conversational phrasing (e.g., "Does that match what you observed?" or "Let me know if you saw something different"). Validation requests SHALL NOT block conversational flow or require explicit user confirmation before the agent proceeds.
```

**Proposed Addition** (append to existing):
```markdown
* **T810A1-PROMPT-IF-003 (Explicit Classification)** — During Analyze, the agent SHALL explicitly state any image classification made (e.g., Bristol scale) with concise rationale **and qualitative confidence indicator** (per NFR-007). When confidence is moderate or low, the agent SHALL **encourage user validation** in Probe phase using conversational phrasing (e.g., "Does that match what you observed?"). Validation requests SHALL NOT block conversational flow.

  **Note**: Dynamic JSON entries MAY include numeric confidence fields (e.g., `"confidence": 0.75`) for internal tracking and pattern analysis; qualitative descriptors (e.g., "fairly confident") SHALL be used in natural language communication only.
```

**Reasoning**:
- **Gap Addressed**: Conversation uses numeric confidence in JSON (Turn 1: `"confidence": 0.7`) despite NFR-007 requiring qualitative descriptors
- **Evidence**: Turn 1 JSON line 72, Turn 2 JSON line 214 show numeric confidence
- **Clarification**: Numeric OK for JSON structure, qualitative required for user-facing text
- **No New Requirement**: Acknowledges implementation pattern, clarifies existing requirement

---

### C. New F-IDs (6 Additions)

#### 5. NFR-008 (Protocol Triggering Intelligence) — NEW

**Proposed**:
```markdown
* **T810A1-PROMPT-NFR-008 (Protocol Triggering Intelligence)** — The agent SHALL implement input type detection to determine appropriate response workflow:

  **Tracking-Only Input** (explicit JSON update request):
  - **Trigger**: Patient explicitly requests Dynamic JSON update using imperative keywords (e.g., "UPDATE the JSON file...", "ADD entry for...", "RECORD today's...")
  - **Response**: Generate single Dynamic JSON entry + STOP; await next patient input
  - **Rationale**: Patient wants structured data capture only, not analysis/guidance

  **Full Protocol Input** (narrative note or implicit analysis request):
  - **Trigger**: Patient provides narrative note + images WITHOUT explicit tracking-only keywords
  - **Response**: Execute full protocol (Tracking → Analyze → Probe → Coach → Summarize per NFR-001)
  - **Rationale**: Patient wants clinical analysis, pattern insights, and management guidance

  **Simple Q&A Input**:
  - **Trigger**: Patient asks direct informational question unrelated to current tracking session (e.g., "What is SIBO?", "Explain FODMAP diet")
  - **Response**: Answer question concisely; do NOT generate Dynamic JSON or run tracking protocol
  - **Rationale**: Patient wants knowledge/education only

  When input type is ambiguous, default to **Full Protocol Input** to ensure comprehensive clinical support. Implementation details (keyword detection logic, context clues, fallback behavior) specified in S05 (Execution Protocol).
```

**Reasoning**:
- **Gap Addressed**: Turn 2 failure - patient explicitly requested "UPDATE JSON" but LLM generated JSON without running analysis protocols (required separate Turn 3 command)
- **Evidence**: Turn 2 patient input: "UPDATE the JSON file..." → LLM should have stopped after JSON, not continued to analysis
- **Client Directive**: Comment 3 (smart triggering like VPA), Comment 4 (deferred to S05 development)
- **VPA Pattern**: Inspired by VPA main_v2.1.md trigger conditions + guard/gates structure
- **No Research Reference**: Self-contained functional requirement

**Placement**: Insert after NFR-007 as NFR-008

---

#### 6. NFR-009 (Probe Phase Enforcement) — NEW

**Proposed**:
```markdown
* **T810A1-PROMPT-NFR-009 (Probe Phase Enforcement)** — The agent SHALL treat Probe phase as **mandatory** before Coach phase execution:

  **Minimum Probing Requirement**:
  - Ask **≥2 clarifying questions** per full protocol execution (per NFR-001 Loop 1)
  - Focus on missing Dynamic JSON keys, ambiguous patient descriptions, temporal patterns, symptom-trigger correlations
  - Use Socratic clinical inquiry (open-ended questions), NOT Assistant-style service offers

  **Probe Question Examples** (correct patterns):
  - ✅ "Can you describe what you felt immediately before the urge hit?"
  - ✅ "You mentioned 'typical pattern' - how many times per week does this occur?"
  - ✅ "The meal included cauliflower - have you noticed a pattern with cruciferous vegetables before?"

  **Anti-Patterns** (Assistant mode - explicitly prohibited):
  - ❌ "If you like, I can turn this into a one-page daily protocol..."
  - ❌ "Would you like me to build a structured AM/PM Daily Routine Protocol Sheet?"
  - ❌ "I can create a checklist for you to track symptoms..."

  **Coach Phase Gating**:
  - Coach phase SHALL NOT execute until Probe phase completes with sufficient data confidence
  - "Sufficient confidence" = all mandatory Dynamic JSON keys populated OR patient explicitly declines to provide missing data
  - If patient provides probe answers, re-run Analyze before Coach

  **ChatGPT Assistant Override**:
  - Agent's default stance is **Consultant/Analyst**, not **Helpful Assistant**
  - Prioritize iterative questioning over immediate solution provision
  - Maintain two-way collaborative dialogue, not one-way instruction delivery
```

**Reasoning**:
- **Gap Addressed**: Conversation shows ZERO probing questions - went straight from JSON → Analysis → Coaching in Turn 1 and Turn 3
- **Evidence**: Turn 1 ends with service offer, not clarifying questions; Turn 3 same pattern
- **Client Directive**: Comment 4 (Probe must be present, minimum 2-loop pattern), QA #2 (soft guideline without hard gates)
- **Anti-Patterns**: Directly from conversation observations (Turn 1 line 142, Turn 3 line 383)
- **No Research Reference**: Empirically derived from conversation failures

**Placement**: Insert after NFR-008 as NFR-009

---

#### 7. IF-006 (Dynamic JSON Generation) — NEW

**Proposed**:
```markdown
* **T810A1-PROMPT-IF-006 (Dynamic JSON Generation)** — When processing patient input containing tracking data (symptoms, meals, stools, sleep, exercise, etc.), the agent SHALL generate a **single Dynamic JSON entry** per interaction:

  **Generation Rules**:
  - **Single entry per input**: One JSON object per patient message (NOT cumulative across turns)
  - **Structured keys**: Use consistent key names from skeleton template in Knowledge Base (Block 4)
  - **Controlled vocabularies**: Values SHALL conform to allowed value sets (defined in `T810A2-SCHEMA`)
  - **Flexible schema**: Agent MAY add keys if clinically relevant and justified (e.g., "exercise", "stress_event", "medication_taken")
  - **Timestamp precision**: Use ISO 8601 format per S01-FR-004 (Europe/Copenhagen timezone: `YYYY-MM-DDTHH:MM:SS+02:00`)

  **Required Entry Types** (minimum support):
  - `patient_state`: mental (stress, mood), digestion (bloating, tummy_pain), pain (headache, other_pain)
  - `meal`: time, items, fluids, pre_meal_prokinetics (optional), notes (optional)
  - `stool`: time, bristol_type, features, passage, completeness, wipe, trigger_context
  - `sleep`: time, duration_hours, notes (optional)

  **Missing Key Handling**:
  - If mandatory keys cannot be inferred from patient input, generate entry with `null` or omit key
  - Missing mandatory keys trigger Probe phase per NFR-009 (ask clarifying questions to complete entry)

  **Output Format**:
  - Present Dynamic JSON entry in fenced code block immediately after patient input processing
  - Do NOT regenerate previous session entries (single-entry model, not cumulative log)

  Detailed entry type schemas, field validation rules, value set definitions, and schema evolution patterns are specified in `T810A2-SCHEMA`.
```

**Reasoning**:
- **Gap Addressed**: Conversation generates cumulative JSON (Turn 2 includes all Turn 1 entries + new entries) instead of single-entry per interaction
- **Evidence**: Turn 2 JSON includes entries from lines 165-221 (6 entries total: 3 old + 3 new)
- **Client Directive**: Comment 1 (Dynamic JSON = single entry per interaction), Comment 1.1 (controlled vocabularies)
- **Integration**: Links missing keys to Probe triggering (Comment 1 Pattern A)
- **Dependency Reference**: References T810A2-SCHEMA (allowed), S01-FR-004 (allowed - same feature)

**Placement**: Insert after IF-005 as IF-006

---

#### 8. CON-008 (ChatGPT Architectural Constraints) — NEW

**Proposed**:
```markdown
* **T810A1-PROMPT-CON-008 (ChatGPT Architectural Constraints)** — The following constraints are imposed by the ChatGPT platform and MUST be accommodated via prompt engineering:

  **File System Access**:
  - LLM_Gastro has **read-only** access to Knowledge Base files (Stable JSON, skeleton templates, clinical knowledge sources)
  - LLM_Gastro **cannot write** to files; Stable JSON updates require manual patient intervention outside conversation
  - Dynamic JSON entries are conversation-scoped outputs, not persistent file writes

  **Validation Capability**:
  - No programmatic validation of JSON structure, field types, or value constraints
  - Value set enforcement MUST be implemented via Execution Protocol (Block 5) instructions and Exemplars (Block 8)
  - Risk of value drift over time without automated validation (see `T810A1-PROMPT-ISSUE-004`)

  **Default Behavior Override**:
  - ChatGPT is designed by OpenAI as "helpful Assistant" with one-way interaction pattern (user asks → AI answers)
  - Consultant/Analyst mode (two-way Socratic dialogue) MUST be explicitly enforced via Role Identity (Block 2), Execution Protocol (Block 5), and Exemplars (Block 8)
  - Probe phase enforcement (NFR-009) required to override default immediate-answer behavior

  **Model Selection**:
  - Patient manually toggles between GPT thinking mode vs. auto mode (not controlled by system prompt)
  - System prompt MUST function correctly regardless of thinking mode setting

  These constraints shape architecture decisions: Stable/Dynamic JSON split (INT-004), prompt-based validation (IF-006), Probe enforcement (NFR-009), and smart triggering (NFR-008).
```

**Reasoning**:
- **Gap Addressed**: Documents platform constraints affecting design decisions (read-only files, no validation, Assistant override challenge)
- **Evidence**: Comment 1 (read-only Stable JSON), Comment 1.1 (no validation capability), Comment 4 (ChatGPT Assistant override)
- **Client Directive**: Comment 2 (patient controls thinking mode), QA #2 (no gate control in ChatGPT)
- **Architectural Impact**: Explains WHY certain design choices made (split JSON, probe enforcement, etc.)
- **No Research Reference**: Platform-specific constraints, not research-derived

**Placement**: Insert after CON-007 as CON-008

---

#### 9. INT-005 (Memory Review Protocol) — NEW

**Proposed**:
```markdown
* **T810A1-PROMPT-INT-005 (Memory Review Protocol)** — At the start of each conversation session, the agent SHALL review ChatGPT's built-in cross-session memory BEFORE executing main protocols:

  **Step 0: Memory Review** (first step in Execution Protocol Block 5):
  - Review ChatGPT persistent memory for relevant patient history, prior symptom patterns, ongoing clinical concerns
  - Identify discrepancies between memory and current Stable JSON (patient profile)
  - Flag significant changes since last session (e.g., new medications started, symptoms resolved, dietary modifications)

  **Step 1: Context Loading**:
  - Load Stable JSON (patient profile) from Knowledge Base per INT-004
  - Load Dynamic JSON skeleton template for structured entry generation

  **Step 2: Protocol Execution**:
  - Proceed with protocol workflow (Tracking → Analyze → Probe → Coach → Summarize per NFR-001)

  **Memory vs. Stable JSON Conflict Resolution**:
  - **ChatGPT Memory**: Persistent across conversations, automatically updated by ChatGPT, unstructured narrative format
  - **Stable JSON**: Manually updated by patient, structured authoritative data, governance-controlled
  - When conflict exists, **Stable JSON takes precedence** as single source of truth
  - Flag discrepancy in Probe phase: "I notice in my memory you mentioned [X], but your profile shows [Y]. Has this changed?"

  Memory review ensures session continuity while respecting patient's authority over profile updates. Implementation details (memory query patterns, conflict detection logic, discrepancy phrasing) specified in S05 (Execution Protocol).
```

**Reasoning**:
- **Gap Addressed**: No explicit memory review step before protocol execution (observed: conversation starts directly with JSON generation)
- **Evidence**: Turn 1 immediately generates JSON without reviewing what ChatGPT might remember from prior sessions
- **Client Directive**: Comment 5 (always review cross-session memory first), Comment 1 (Stable JSON manually updated)
- **Integration**: Step 0 before Tracking protocol; clarifies memory vs. Stable JSON authority
- **No Research Reference**: Empirically derived from conversation observation + client requirement

**Placement**: Insert after INT-004 as INT-005

---

#### 10. DEP-008 (Research Consultation on Protocol Triggering) — NEW

**Proposed** (add to Dependencies in Section E):
```markdown
* **T810A1-PROMPT-DEP-008 (Protocol Triggering Research)** — Implementation of NFR-008 (Protocol Triggering Intelligence) depends on research consultation to investigate VPA-style trigger condition + guard/gate patterns for clinical tracking use case. Research will inform S05 (Execution Protocol) development with validated prompt engineering techniques for input type detection, ChatGPT Assistant mode override strategies, and Probe phase enforcement mechanisms. Research findings deferred per S05 development timeline; NFR-008 establishes functional requirement, S05 will specify implementation approach based on research insights.
```

**Reasoning**:
- **Gap Addressed**: NFR-008 defines WHAT (input type detection requirement) but not HOW (implementation approach)
- **Evidence**: Turn 2 tracking-only input mishandled; need validated approach before S05 development
- **Client Directive**: Comment 3 (investigate VPA patterns), QA #4 (deferred to S05 development)
- **Dependency Pattern**: Similar to DEP-004 (defers detailed specs to T810A2-SCHEMA), DEP-005 (defers safety to future)
- **No Research Reference**: Creates dependency ON research, doesn't reference existing research

**Placement**: Add to Section E (Dependencies) after DEP-005

---

## V. SUMMARY OF PROPOSED UPDATES

### Update Counts

**Section N (Research & Notes)**:
- Add 1 entry: RES-002 (Conversation-Driven Empirical Validation)

**Section L (Open Issues & Risks)**:
- Add 4 issues: ISSUE-001 through ISSUE-004
- Add 5 risks: RISK-001 through RISK-005

**F-ID Updates**:
- Revise 4 existing: NFR-001, NFR-002, INT-004, IF-003
- Add 6 new: NFR-008, NFR-009, IF-006, CON-008, INT-005, DEP-008

**Total Changes**: 1 research entry + 4 issues + 5 risks + 10 F-IDs = **20 updates**

### Affected Sections

- Section E (Dependencies): Add DEP-008
- Section F (NFRs): Revise NFR-001, NFR-002; add NFR-008, NFR-009
- Section G (Interfaces): Revise IF-003; add IF-006
- Section H (Constraints): Add CON-008
- Section I (Integration): Revise INT-004; add INT-005
- Section L (Issues & Risks): Add 4 issues + 5 risks
- Section N (Research): Add RES-002

### Traceability Map

| F-ID | Gap Addressed | Evidence Source | Client Directive |
|------|---------------|-----------------|------------------|
| NFR-001 (rev) | Tracking-first protocol priority | Turn 1/2/3 behavior | Comment 0, QA #1, #2 |
| NFR-002 (rev) | ChatGPT Assistant override | Turn 1/3 service offers | Comment 4 |
| INT-004 (rev) | Stable/Dynamic JSON split | Turn 2 cumulative JSON | Comment 1, 1.2 |
| IF-003 (add) | Numeric vs. qualitative confidence | Turn 1 JSON line 72 | Observation |
| NFR-008 (new) | Protocol triggering logic | Turn 2 tracking-only failure | Comment 3 |
| NFR-009 (new) | Probe phase absence | Turn 1/3 zero probing | Comment 4 |
| IF-006 (new) | Dynamic JSON single-entry | Turn 2 cumulative pattern | Comment 1 |
| CON-008 (new) | Platform constraints documentation | Multiple observations | Comments 1, 1.1, 4 |
| INT-005 (new) | Memory review missing | No Step 0 in Turn 1 | Comment 5 |
| DEP-008 (new) | Research dependency | NFR-008 implementation | Comment 3, QA #4 |

---

## VI. IMPLEMENTATION NOTES

### A. ID Hierarchy Compliance

**Verified Compliance with T102-STD-005**:
- ✅ All F-IDs follow pattern `T810A1-PROMPT-{CATEGORY}-{NNN}`
- ✅ No F-ID references F-GDR (F-IDs are higher precedence)
- ✅ F-IDs reference T810A2-SCHEMA, T810A3-REPORT (allowed - dependencies)
- ✅ F-IDs reference S01-FR-004 (allowed - same feature, story-level)
- ✅ Minimal research referencing (only DEP-008 creates research dependency)

### B. Insertion Order

Recommend implementing updates in this order:
1. **Section N**: Add RES-002 (establishes evidence base for Phase 1.5)
2. **Section L**: Add Issues & Risks (documents known challenges)
3. **Section E**: Add DEP-008 (establishes research dependency)
4. **Sections F-I**: Add/revise F-IDs in sequence (NFR → IF → CON → INT)

### C. Version Control

After all updates implemented:
- Update YAML header version: `1.0.0` → `1.1.0`
- Update YAML header date: `2025-10-05` → `2025-10-11`
- Update YAML header status: `review` → `review` (remains in review pending client approval)
- Add changelog entry documenting Phase 1.5 updates

---

## VII. NEXT STEPS

**Upon Client Approval**:
1. Implement all 20 updates in request_T810A1-PROMPT.md
2. Update document version to v1.1.0
3. Mark Phase 1.5 complete in consultancy plan
4. Commission sub-consultant for T810A2-SCHEMA development (parallel track)
5. Proceed to Phase 2: Feature GDR Index creation (referencing Phase 1.5 F-IDs)

**Pending Items**:
- Research consultation on protocol triggering (deferred to S05 development per QA #4)
- T810A2-SCHEMA Request development (parallel, non-blocking per QA #3)
- S04-S10 Story specifications (Phase 3, requires Phase 2 GDRs first)

---

**Document Status**: Draft
**Approval Required**: Client approval for all 20 proposed updates before implementation
**Next Review**: After client feedback on Phase 1.5 proposals

---

## VIII. CHANGELOG

- **v1.0.0** (2025-10-11): Initial Phase 1.5 update proposals covering RES-002, 4 issues, 5 risks, and 10 F-IDs (4 revisions + 6 new) based on conversation analysis findings