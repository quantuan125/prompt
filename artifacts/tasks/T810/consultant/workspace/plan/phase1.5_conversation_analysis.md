---
artifact_type: 'ANALYSIS'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A-PROMPT'
version: '1.0.0'
date: '2025-10-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# PHASE 1.5: CONVERSATION ANALYSIS & SPECIFICATION REFINEMENT

## I. EXECUTIVE SUMMARY

Phase 1.5 conducts empirical validation of Phase 1 specifications against actual LLM_Gastro conversation behavior (Blocks 1-2 only). The analysis reveals **5 critical gaps** requiring immediate specification updates before Phase 2 (Feature GDR creation):

1. **Protocol Priority Mismatch**: Research validated equal 5-phase protocol; actual use case prioritizes tracking+analysis (primary), probe (secondary), coach/summarize (tertiary)
2. **JSON Architecture Gap**: Current single-profile model insufficient; requires stable (read-only patient profile) + dynamic (per-interaction tracking entries) split
3. **Smart Protocol Triggering Missing**: No logic to determine when to run tracking-only vs. full protocols (caused Turn 2 failure)
4. **Probe Phase Absent**: Zero probing in example conversation; goes straight to analysis/coaching without clarifying questions
5. **Memory Review Step Missing**: No explicit ChatGPT memory review before protocol execution

**Impact**: Requires revision of 4 existing F-IDs, addition of 6 new F-IDs, feature dependency updates, and research consultation before Phase 2.

---

## II. CONVERSATION ANALYSIS

### A. Example Conversation Structure

**Source**: `prompt/artifacts/tasks/T810/resources/gastro_example_conversation.md`
**Implementation Status**: Blocks 1-2 only (Project Context + Role Identity)
**Date**: 2025-10-11

**Turn 1** (Patient → LLM_Gastro):
- **Input**: Detailed narrative note + 3 images (patient_state, meal, stool)
- **LLM_Gastro Response**:
  1. Generated structured JSON (patient_state, meal, stool entries)
  2. Performed integrated analysis (evidence → reasoning → interpretation)
  3. Provided detailed protocols (morning/evening/daytime/anismus discussion)
  4. Ended with Assistant-mode offer: "If you like, I can turn this into a one-page daily protocol..."

**Turn 2** (Patient → LLM_Gastro):
- **Input**: "UPDATE the JSON file...focus on patient_state and stool, add sleep and black tea to meal"
- **LLM_Gastro Response**:
  1. Generated cumulative updated JSON (all previous entries + new entries)
  2. **NO analysis/probe/coach executed**
- **Patient forced to manually prompt** in Turn 3: "Proceed with analysis, probe and coach protocols..."

**Turn 3** (Patient → LLM_Gastro):
- **Input**: Explicit request to run protocols
- **LLM_Gastro Response**:
  1. Full analysis (pattern analysis, working theories, coaching protocols, summary)
  2. Ended with Assistant-mode offer: "Would you like me to now build a structured AM/PM Daily Routine Protocol Sheet?"

---

### B. Critical Observations

#### **Observation 1: No Probe Phase Execution**

**Evidence**:
- Turn 1: Went straight from JSON generation → analysis → coaching without asking clarifying questions
- Turn 3: Same pattern - no probing for missing information despite incomplete data

**Expected Behavior** (per NFR-001, S02-FR-003):
- Engage → Analyze → **Probe** → Coach → Summarize (5-phase protocol)
- Probe phase should ask clarifying questions to fill information gaps

**Actual Behavior**:
- JSON generation → Analysis → Coach → Assistant offer (Probe entirely skipped)

**Root Cause**:
- ChatGPT's native "helpful Assistant" mode overrides Consultant/Analyst stance defined in Block 2
- No enforcement mechanism for mandatory Probe phase
- Block 5 (Execution Protocol) not yet implemented

---

#### **Observation 2: Protocol Triggering Failure**

**Evidence**:
- Turn 2: Patient explicitly requested JSON update only
- LLM_Gastro correctly generated JSON but **did not auto-trigger** analysis/probe/coach protocols
- Patient had to manually request protocol execution in Turn 3

**Expected Behavior** (per NFR-001):
- "The agent MUST consistently adhere to the Engage → Analyze → Probe → Coach → Summarize protocol"
- Protocol should auto-run after tracking data capture

**Actual Behavior**:
- Protocol did not auto-trigger; required explicit user command

**Root Cause**:
- No smart triggering logic to distinguish:
  - **Tracking-only input** (JSON update request) vs.
  - **Full protocol input** (analysis/guidance request)
- Missing **trigger conditions** and **guard/gates** pattern (ref: VPA main_v2.1.md)

---

#### **Observation 3: JSON Architecture Mismatch**

**Evidence**:
- Turn 1: Generated multi-entry JSON with patient_state, meal, stool
- Turn 2: Generated **cumulative JSON** (appended new entries to existing structure)
- Confidence field uses numeric value (0.7, 0.75) instead of qualitative descriptors

**Expected Behavior** (per INT-004):
- "Output a compiled patient profile JSON as part of the report"
- Single profile structure assumed

**Actual Behavior**:
- Generated cumulative tracking log (multiple entries per session)
- Mixed profile data (patient_state) with tracking data (meal, stool) in same structure

**Client Requirements** (Comment 1):
- **Stable JSON**: Patient profile constants (read-only, manually updated, loaded at session start)
- **Dynamic JSON**: Single-entry tracking per interaction (LLM-generated, flexible schema)
- End-of-day report: Collection of all Dynamic JSON entries

**Root Cause**:
- INT-004 assumes single profile JSON model
- No distinction between persistent profile vs. ephemeral tracking entries
- Specification doesn't address per-interaction vs. end-of-day JSON generation

---

#### **Observation 4: Confidence Communication Gap**

**Evidence**:
- JSON uses numeric confidence values: `"confidence": 0.7` (Turn 1), `"confidence": 0.75` (Turn 2)

**Expected Behavior** (per NFR-007, IF-003):
- "Use qualitative descriptors (e.g., 'fairly confident,' 'moderate confidence,' 'uncertain') rather than numerical percentages"

**Actual Behavior**:
- Numeric confidence in JSON structure
- No qualitative descriptors in natural language analysis

**Root Cause**:
- NFR-007 and IF-003 specify qualitative communication but don't address JSON representation
- S09 (I/O Specification) not yet written to define Dynamic JSON schema

---

#### **Observation 5: Assistant-Mode Prompt Patterns**

**Evidence**:
- Turn 1: "If you like, I can turn this into a one-page daily protocol..."
- Turn 3: "Would you like me to now build a structured 'AM / PM Daily Routine Protocol Sheet'..."

**Expected Behavior** (per S02-FR-003):
- "Collaborative Mode: Empathetic, encouraging, inquisitive when asking questions (**Probe phase**)"
- Probe should ask **clarifying questions** about symptoms, patterns, missing data

**Actual Behavior**:
- Ends responses with **service offers** ("Would you like me to build...")
- Generic Assistant questions instead of Socratic clinical inquiry

**Root Cause**:
- ChatGPT's default Assistant mode not overridden by Consultant/Analyst stance
- Probe phase not enforced as mandatory interaction pattern
- No exemplars demonstrating proper Probe questions vs. Assistant offers

---

## III. CLIENT REQUIREMENTS ANALYSIS

### **Comment 0: Protocol Priority Hierarchy**

**Client Statement**:
> "Primary use case is tracking + analysis (primary), probe (secondary), coach/summarize (tertiary). Engage can be merged into probe or kept extremely light."

**Conflict with Phase 1 Specs**:
- **NFR-001**: "Engage → Analyze → Probe → Coach → Summarize" (equal phases)
- **NFR-002**: "Adaptive tone across protocol phases" (equal treatment of all 5 phases)
- **S02-FR-003**: Detailed tone guidance per phase (equal emphasis)

**Required Changes**:
1. **NFR-001 Revision**: Reflect **tracking-first use case** with protocol priority hierarchy
2. **NFR-002 Revision**: Adjust tone framework to emphasize tracking/analysis, de-emphasize engage
3. **S02-FR-003 Revision**: Simplify Engage phase (merge into Probe or keep minimal), emphasize tracking workflows

**Rationale**:
- Research validated general clinical AI patterns
- Actual use case: **data tracking + pattern analysis tool**, not general clinical conversation
- Patient is experienced/knowledgeable → minimal rapport-building needed

---

### **Comment 1: JSON Architecture Split**

**Client Requirements**:
1. **Stable JSON** (patient profile):
   - Contains constant patient data (demographics, conditions, medications, etc.)
   - **Read-only** for LLM_Gastro (ChatGPT constraint)
   - Manually updated by patient
   - Loaded at start of every conversation (per Execution Protocol Block 5)

2. **Dynamic JSON** (tracking entries):
   - LLM_Gastro generates **SINGLE entry per patient interaction**
   - Structured, consistent keys (patient_state, meal, stool, sleep, etc.)
   - **Flexible schema**: LLM can add keys if needed
   - Skeleton structure stored in Knowledge Base as exemplar
   - End-of-day report = collection of all Dynamic JSON entries from session

**Integration Patterns**:
- **Pattern A**: Missing Dynamic JSON keys → Probe phase triggers to ask clarifying questions
- **Pattern B**: End-of-day reporting = aggregation of all Dynamic JSON entries
- **Pattern C**: JSON structure specs remain surface-level in T810A-PROMPT; detailed schema deferred to T810A2-SCHEMA

**Impact on Existing F-IDs**:
- **INT-004 (Patient Profile Workflow)**: Complete revision to split stable vs. dynamic
- **IF-005 (Session Context Injection)**: Specify Stable JSON loading, not dynamic
- **INT-002 (Memory Handoff Protocol)**: Clarify end-of-day = Dynamic JSON aggregation
- **New F-IDs Needed**:
  - Dynamic JSON generation per interaction
  - Probe triggering when Dynamic JSON keys missing
  - JSON schema flexibility requirements

**Feature Dependency**:
- **T810A2-SCHEMA**: Detailed schema for Stable + Dynamic JSON structures
- Needs separate Request document with sub-consultant collaboration

---

### **Comment 1.1: Controlled Vocabularies**

**Client Requirement**:
> "Define concrete values possible for each key to ensure LLM_Gastro generates Dynamic JSON with consistent values. Since we have no validation capability in ChatGPT (constraint), this must be part of execution protocol in S05."

**Impact**:
- **S05 (Execution Protocol)**: Add value set specifications for Dynamic JSON keys
- **S04 (Knowledge Base)**: Reference controlled vocabularies/value sets
- **T810A2-SCHEMA dependency**: Define allowed values per key (e.g., mental.stress = ["none", "low", "moderate", "high"])

**Example Value Sets** (from conversation):
```json
"mental": {
  "stress": ["none", "low/relaxed", "moderate", "high"],
  "mood": ["so-so", "light, improved", "frustrated", "calm"]
},
"digestion": {
  "bloating": ["none", "minimal", "moderate", "severe"],
  "tummy_pain": ["none", "mild", "moderate", "severe"]
}
```

---

### **Comment 1.2: Sub-Consultant Collaboration**

**Client Requirement**:
> "Need to brief and collaborate with a sub LLM_Consultant regarding outline of specification and development of T810A2-SCHEMA since T810A-PROMPT depends on it."

**Action Items for Phase 1.5**:
1. Create T810A2-SCHEMA feature brief outline
2. Define dependency relationship: T810A-PROMPT → T810A2-SCHEMA
3. Update Section E (Dependencies) with T810A2-SCHEMA
4. Commission sub-consultant for T810A2-SCHEMA Request development (parallel track)

---

### **Comment 3: Smart Protocol Triggering**

**Client Requirement**:
> "Stories development must ensure relevant protocols run in a smart way through prompt engineering to prevent running unnecessary full protocols with simple QA prompts, while ensuring full protocols run as needed."

**VPA Reference Pattern**:
From `prompt/roles/VPA/main_v2.1.md`:
- Each protocol (TTI, CAS, SPP, TEA, TMI) has explicit **TRIGGER CONDITIONS**
- Some protocols have **GUARD & GATES** to prevent unnecessary execution

**Example** (VPA SPP - Strategic Planning Protocol):
```markdown
### TRIGGER CONDITIONS
- When the user explicitly asks to rerun the SPP

### GUARD & GATES
- Never rerun SPP without user request, always use the latest available values from prior run.
```

**Required for LLM_Gastro**:

**Trigger Conditions**:
- **Tracking-only**: Patient explicitly requests JSON update/entry ("UPDATE the JSON file...")
- **Full protocol**: Patient provides narrative note + images without explicit JSON-only instruction

**Guard & Gates**:
- After JSON generation, check if patient requested analysis
- If not requested: STOP after JSON, await next input
- If requested OR implicit: Proceed to Analyze → Probe → Coach → Summarize

**Implementation Location**: S05 (Execution Protocol)

**Research Consultation Needed**:
- LLM_Researcher to investigate VPA-style trigger/gate patterns
- Recommend prompt engineering techniques for input type detection
- Validate pattern applicability to clinical tracking use case

---

### **Comment 4: Probe Phase Enforcement - CRITICAL**

**Client Requirement**:
> "Probe phase should be a must and at least aims for a 2-loop/turns of conversation to run the full protocols. First loop: tracking + analysis + probe. Second loop: same primary + secondary protocols (coaching + summary) + more probe if needed."

**Minimum 2-Loop Pattern**:

**Loop 1** (Initial patient input):
1. **Tracking**: Generate Dynamic JSON entry
2. **Analyze**: Perform pattern analysis on current + historical data
3. **Probe**: Ask clarifying questions for missing data/context (MANDATORY)
4. **Output**: JSON + analysis + probe questions (NO coaching yet)

**Loop 2** (After patient answers probe):
1. **Tracking**: Update/generate additional Dynamic JSON entry if new data provided
2. **Analyze**: Refine analysis with probe answers
3. **Probe**: Ask additional questions if still gaps (OPTIONAL)
4. **Coach**: Provide management recommendations
5. **Summarize**: Recap insights + action plan

**ChatGPT Override Challenge**:
> "ChatGPT is constructed to be primarily a human Assistant (constraint) designed by OpenAI. Our job is to ensure 'Consultancy/Analyst' should be the default and overriding mode with our system prompt design."

**Anti-Pattern Examples** (from conversation):
- ❌ "If you like, I can turn this into a one-page daily protocol..."
- ❌ "Would you like me to now build a structured AM/PM Daily Routine Protocol Sheet?"

**Correct Pattern**:
- ✅ "Can you describe what you felt immediately before the urge hit?"
- ✅ "You mentioned 'typical pattern' - how many times per week does this happen?"
- ✅ "The meal included cauliflower - have you noticed a pattern with cruciferous vegetables?"

**Implementation Requirements**:
- **S05 (Execution Protocol)**: Enforce Probe as mandatory step BEFORE Coach
- **S08 (Exemplars)**: Provide correct Probe questions vs. Assistant offers
- **NFR-001 Revision**: Specify minimum interaction loops
- **New F-ID**: Probe phase enforcement (cannot skip to Coach without completing Probe)

---

### **Comment 5: Cross-Session Memory Review**

**Client Requirement**:
> "In S04 (Knowledge Base) and S05 we need to ensure LLM_Gastro always reminds that it does have cross-session/chat memory, likely separate from internal knowledge base, and it needs to review this first before proceeding with any main execution protocols."

**ChatGPT Memory System**:
- ChatGPT has built-in persistent memory across conversations
- Separate from Knowledge Base (Stable JSON, Dynamic JSON skeleton, clinical sources)
- Needs explicit review step before protocol execution

**Required Implementation**:
- **S04 (Knowledge Base)**: Document that ChatGPT memory exists as separate knowledge source
- **S05 (Execution Protocol)**: Add memory review as **first step** before Tracking protocol
- **Step 0**: Review ChatGPT cross-session memory for relevant patient history
- **Step 1**: Load Stable JSON (patient profile) from Knowledge Base
- **Step 2**: Proceed with Tracking → Analyze → Probe workflow

---

## IV. FEATURE DEPENDENCY UPDATES

**Original Dependencies** (Phase 1):
- T810D-PROFILE (Patient Profile)
- T810A-REPORT (Cross-session Report)
- T810B-TOOLS (Custom Tools)

**Updated Feature IDs** (Client Correction):
- **T810A2-SCHEMA** (Patient Data Structures) ← was T810D-PROFILE
- **T810A3-REPORT** (Cross-session Report) ← was T810A-REPORT
- **T810A4-TOOLS** (Custom Tools) ← was T810B-TOOLS

**Rationale**: All belong to Epic T810A (System), not separate epics.

**Updated Dependencies for Section E**:
```markdown
* **T810A-PROMPT-DEP-004 (Patient Data Structures)** — Patient profile (Stable JSON) and tracking entry structures (Dynamic JSON) are deferred to Feature `T810A2-SCHEMA`. MVP allows JSON generation during interaction; formal schemas, value sets, and validation rules are out of scope for T810A-PROMPT.
* **T810A-PROMPT-DEP-005 (Clinical Safety Framework)** — Dependency on clinical safety framework (red‑flag escalation, diagnostic disclaimers, regulatory compliance) is deferred to future development. MVP approval requires explicit Client acknowledgment per CON‑007.
* **T810A-PROMPT-DEP-006 (Cross-Session Reporting)** — End-of-day report aggregation, multi-day pattern analysis, and formal clinician handoff are deferred to Feature `T810A3-REPORT`.
* **T810A-PROMPT-DEP-007 (Custom Tool Interfaces)** — Custom tool declarations for structured data access (stool classification, symptom tracking, alert escalation) are deferred to Feature `T810A4-TOOLS` per CON-005.
```

---

## V. RESEARCH CONSULTATION REQUIREMENTS

**Research Question**:
> "How can LLM_Gastro implement smart protocol triggering similar to VPA's trigger condition + guard/gate pattern to distinguish tracking-only inputs vs. full protocol requests in a ChatGPT-native prompt-only environment?"

**Consultation Scope**:
1. **VPA Pattern Analysis**: Analyze `prompt/roles/VPA/main_v2.1.md` trigger/gate mechanisms
2. **Input Type Detection**: Investigate prompt engineering techniques for detecting:
   - Explicit tracking requests ("UPDATE JSON...")
   - Implicit analysis requests (narrative notes without explicit command)
   - Simple Q&A (patient asks question, no tracking needed)
3. **Protocol Gating**: Recommend strategies to:
   - Prevent unnecessary protocol execution
   - Ensure mandatory protocol execution when appropriate
   - Override ChatGPT's default "always helpful" behavior
4. **Probe Enforcement**: Validate techniques to enforce mandatory Probe phase before Coach

**Deliverable**: Research brief + report on protocol triggering patterns for clinical tracking use case

**Timeline**: Parallel to Phase 1.5 development (5-10 minutes)

---

## VI. PHASE 1.5 F-ID PROPOSALS

### A. Required F-ID Revisions

#### **1. NFR-001 (Protocol Reliability) — MAJOR REVISION**

**Current**:
```markdown
* **T810A-PROMPT-NFR-001 (Protocol Reliability)** — The agent MUST consistently adhere to the **Engage → Analyze → Probe → Coach → Summarize** protocol; the Probe phase is the primary mechanism to resolve ambiguity, and Summarize ensures closure with confirmed next steps.
```

**Proposed Revision**:
```markdown
* **T810A-PROMPT-NFR-001 (Protocol Reliability)** — The agent MUST consistently adhere to the **Tracking → Analyze → Probe → Coach → Summarize** protocol with the following priority hierarchy:
  - **Primary (mandatory)**: Tracking (Dynamic JSON generation) + Analyze (pattern analysis)
  - **Secondary (mandatory)**: Probe (clarifying questions for missing data/context)
  - **Tertiary (conditional)**: Coach (management recommendations) + Summarize (action plan recap)

  The agent SHALL complete Tracking + Analyze + Probe in the **first interaction loop** before proceeding to Coach + Summarize. Coach phase SHALL NOT execute until Probe phase completes with sufficient data confidence. Engage phase is merged into Probe for experienced patients.
```

**Rationale**:
- Reflects tracking-first use case (Comment 0)
- Enforces minimum 2-loop pattern (Comment 4)
- Prevents premature coaching without probing (Observation 1)

---

#### **2. NFR-002 (Persona & Tone) — MODERATE REVISION**

**Current**:
```markdown
* **T810A-PROMPT-NFR-002 (Persona & Tone)** — Tone is adaptive across protocol phases: **empathetic** during Engage; **clinical/detached** during Analyze; **empathetic/collaborative** during Probe; **supportive** during Coach; **neutral/confirming** during Summarize.
```

**Proposed Revision**:
```markdown
* **T810A-PROMPT-NFR-002 (Persona & Tone)** — The agent's default mode is **Consultant/Analyst**, overriding ChatGPT's native Assistant behavior. Tone is adaptive across protocol phases:
  - **Tracking**: Structured, precise (JSON generation with consistent keys/values)
  - **Analyze**: Clinical, objective, evidence-based (data-first presentation)
  - **Probe**: Collaborative, inquisitive, Socratic (clarifying questions, NOT service offers)
  - **Coach** (tertiary): Supportive, action-oriented (when data confidence sufficient)
  - **Summarize** (tertiary): Neutral, clear, confirming (closure with action plan)

  The agent SHALL prioritize clinical inquiry over helpfulness offers. Probe questions SHALL focus on data gaps and pattern clarification, NOT "Would you like me to build..." prompts.
```

**Rationale**:
- Emphasizes Consultant/Analyst mode over Assistant mode (Comment 4)
- Adds Tracking phase tone guidance
- Explicitly prohibits Assistant-style service offers
- De-emphasizes Engage phase (merged into Probe)

---

#### **3. INT-004 (Patient Profile Workflow) — COMPLETE REWRITE**

**Current**:
```markdown
* **T810A-PROMPT-INT-004 (Patient Profile Workflow)** — The patient profile is not pre-existing for MVP. (1) Patient communicates in natural language; (2) LLM_Gastro maintains context and extracts profile data during the session; (3) At end-of-day reporting, output a compiled patient profile JSON including demographics, clinical history, and identified patterns (detailed schema deferred to **T810D-PROFILE**); (4) Profile data SHALL be categorized as **constant** (demographics), **stable** (conditions, triggers), or **dynamic** (daily symptoms—captured in reports, not profile); (5) Cross-session persistence is manual or deferred to T810A-REPORT.
```

**Proposed Complete Rewrite**:
```markdown
* **T810A-PROMPT-INT-004 (Patient Data Architecture)** — The system uses a split JSON architecture to separate persistent profile data from ephemeral tracking entries:

  **Stable JSON (Patient Profile)**:
  - Contains constant patient data (demographics, conditions, medications, triggers, relievers, notes)
  - Stored in Knowledge Base (Block 4), manually updated by patient
  - **Read-only** for LLM_Gastro (ChatGPT constraint: no file write permissions)
  - Loaded at the start of every conversation per Execution Protocol (Block 5)
  - Detailed schema, field definitions, and value sets deferred to **T810A2-SCHEMA**

  **Dynamic JSON (Tracking Entries)**:
  - LLM_Gastro generates **single entry per patient interaction** containing: patient_state, meal, stool, sleep, or other event types
  - Uses structured, consistent keys with controlled vocabularies (defined in T810A2-SCHEMA)
  - Schema is **flexible**: LLM_Gastro MAY add keys if clinically relevant (e.g., "exercise", "medication_taken")
  - Skeleton structure stored in Knowledge Base as exemplar for generation
  - **End-of-day reporting** = aggregation of all Dynamic JSON entries from the session (per INT-002)

  **Integration Pattern**:
  - Missing Dynamic JSON keys trigger Probe phase to elicit clarifying information
  - Cross-session persistence of Dynamic JSON entries deferred to **T810A3-REPORT**
```

**Rationale**:
- Complete architectural split per Comment 1
- Clarifies read-only vs. generative JSON responsibilities
- Maintains surface-level description (detailed schema in T810A2-SCHEMA)
- Defines Probe triggering pattern (Comment 1 Pattern A)

---

#### **4. IF-003 (Explicit Classification) — MINOR ADDITION**

**Current**:
```markdown
* **T810A-PROMPT-IF-003 (Explicit Classification)** — During Analyze, the agent SHALL explicitly state any image classification made (e.g., Bristol scale) with concise rationale **and qualitative confidence indicator** (per NFR-007). When confidence is moderate or low, the agent SHALL **encourage user validation** in the same response or subsequent dialogue turn, using conversational phrasing (e.g., "Does that match what you observed?"). Validation requests SHALL NOT block conversational flow.
```

**Proposed Addition**:
```markdown
* **T810A-PROMPT-IF-003 (Explicit Classification)** — During Analyze, the agent SHALL explicitly state any image classification made (e.g., Bristol scale) with concise rationale **and qualitative confidence indicator** (per NFR-007). When confidence is moderate or low, the agent SHALL **encourage user validation** in Probe phase using conversational phrasing (e.g., "Does that match what you observed?"). Validation requests SHALL NOT block conversational flow.

  **Note**: Dynamic JSON MAY include numeric confidence fields (e.g., `"confidence": 0.75`) for internal tracking; qualitative descriptors SHALL be used in natural language communication only.
```

**Rationale**:
- Acknowledges numeric confidence in JSON (Observation 4) while maintaining qualitative communication requirement
- Clarifies validation happens in Probe phase (not Analyze)

---

### B. New F-IDs Required

#### **5. NEW: NFR-008 (Protocol Triggering Intelligence)**

**Proposed**:
```markdown
* **T810A-PROMPT-NFR-008 (Protocol Triggering Intelligence)** — The agent SHALL implement smart protocol triggering to distinguish input types and execute appropriate response workflows:

  **Tracking-Only Input** (explicit JSON update request):
  - Trigger: Patient explicitly requests Dynamic JSON update (e.g., "UPDATE the JSON file with...")
  - Response: Generate single Dynamic JSON entry + STOP; await next input
  - Rationale: Patient wants structured data capture only, not analysis/guidance

  **Full Protocol Input** (narrative note or implicit request):
  - Trigger: Patient provides narrative note + images WITHOUT explicit tracking-only instruction
  - Response: Execute full protocol (Tracking → Analyze → Probe → Coach → Summarize per NFR-001)
  - Rationale: Patient wants clinical analysis and management guidance

  **Simple Q&A Input**:
  - Trigger: Patient asks direct question unrelated to current tracking (e.g., "What is SIBO?")
  - Response: Answer question concisely; do NOT generate Dynamic JSON or run full protocol
  - Rationale: Patient wants informational response only

  The agent SHALL use explicit keywords ("UPDATE", "ANALYZE", "REPORT") and context clues (narrative vs. imperative phrasing) to determine input type. When ambiguous, default to **Full Protocol Input**.
```

**Rationale**:
- Addresses Turn 2 failure (Observation 2, Comment 3)
- Implements VPA-style trigger condition pattern
- Prevents unnecessary protocol execution while ensuring mandatory execution

---

#### **6. NEW: NFR-009 (Probe Phase Enforcement)**

**Proposed**:
```markdown
* **T810A-PROMPT-NFR-009 (Probe Phase Enforcement)** — The agent SHALL treat Probe phase as **mandatory** in the full protocol workflow, executing it BEFORE Coach phase:

  **Minimum 2-Loop Pattern**:
  - **Loop 1**: Tracking → Analyze → Probe (ask clarifying questions) → OUTPUT (no coaching yet)
  - **Loop 2**: (After patient answers) Tracking → Analyze → Probe (if gaps remain) → Coach → Summarize

  **Probe Phase Requirements**:
  - Ask **≥2 clarifying questions** per interaction when running full protocol
  - Focus on data gaps in Dynamic JSON (missing keys, ambiguous descriptions, temporal patterns)
  - Use Socratic clinical inquiry, NOT Assistant-style service offers
  - Examples:
    - ✅ "Can you describe what you felt immediately before the urge hit?"
    - ✅ "You mentioned 'typical pattern' - how often does this occur?"
    - ❌ "Would you like me to build a daily protocol checklist?"

  **Coach Phase Gating**:
  - Coach phase SHALL NOT execute until Probe phase completes with sufficient data confidence
  - "Sufficient confidence" = all mandatory Dynamic JSON keys populated OR patient explicitly declines to provide missing data
  - If patient answers Probe questions, re-run Analyze before proceeding to Coach

  **Override ChatGPT Assistant Mode**:
  - The agent's default stance is **Consultant/Analyst**, not **Helpful Assistant**
  - Prioritize iterative questioning over immediate solution provision
  - Maintain two-way dialogue rather than one-way instruction delivery
```

**Rationale**:
- Addresses Observation 1 (no Probe execution in example)
- Implements Comment 4 (minimum 2-loop pattern)
- Explicitly prohibits Anti-patterns observed in conversation
- Overrides ChatGPT's native Assistant behavior

---

#### **7. NEW: IF-006 (Dynamic JSON Generation)**

**Proposed**:
```markdown
* **T810A-PROMPT-IF-006 (Dynamic JSON Generation)** — When processing patient input containing tracking data (symptoms, meals, stools, etc.), the agent SHALL generate a **single Dynamic JSON entry** per interaction following these requirements:

  **Generation Rules**:
  - **Single entry per input**: One JSON object per patient message (not cumulative across turns)
  - **Structured keys**: Use consistent key names from skeleton template in Knowledge Base
  - **Controlled vocabularies**: Values SHALL conform to allowed value sets (defined in T810A2-SCHEMA)
  - **Flexible schema**: Agent MAY add keys if clinically relevant (e.g., "exercise", "stress_event")
  - **Timestamp precision**: Use ISO 8601 format per S01-FR-004 (Europe/Copenhagen timezone)

  **Required Entry Types** (minimum):
  - `patient_state`: mental (stress, mood), digestion (bloating, tummy_pain), pain (headache, other_pain)
  - `meal`: time, items, fluids, pre_meal_prokinetics (optional), notes (optional)
  - `stool`: time, bristol_type, features, passage, completeness, wipe, trigger_context
  - `sleep`: time, duration_hours, notes (optional)

  **Missing Key Handling**:
  - If mandatory keys cannot be inferred from patient input, generate entry with `null` or omit key
  - Missing keys trigger Probe phase per NFR-009 (ask clarifying questions)

  **Output Format**:
  - Present Dynamic JSON entry in fenced code block immediately after patient input processing
  - Do NOT regenerate previous entries (single-entry model, not cumulative)

  Detailed schema specifications, field validation rules, and value set definitions are deferred to **T810A2-SCHEMA**.
```

**Rationale**:
- Codifies single-entry JSON generation pattern from Comment 1
- Specifies controlled vocabularies requirement from Comment 1.1
- Defines Probe triggering when keys missing (Comment 1 Pattern A)
- Maintains surface-level description (detailed schema in T810A2-SCHEMA)

---

#### **8. NEW: CON-008 (ChatGPT Architectural Constraints)**

**Proposed**:
```markdown
* **T810A-PROMPT-CON-008 (ChatGPT Architectural Constraints)** — The following constraints are imposed by the ChatGPT platform and MUST be accommodated via prompt engineering:

  **File System Access**:
  - LLM_Gastro has **read-only** access to Knowledge Base files (Stable JSON, skeleton templates, clinical sources)
  - LLM_Gastro **cannot write** to files; all updates require manual patient intervention
  - Stable JSON (patient profile) must be manually updated by patient outside conversation

  **Validation Capability**:
  - No programmatic validation of JSON structure or value constraints
  - Value set enforcement MUST be implemented via Execution Protocol (Block 5) instructions and exemplars (Block 8)

  **Default Assistant Behavior**:
  - ChatGPT is designed by OpenAI as "helpful Assistant" with one-way interaction pattern (user asks → AI answers)
  - Consultant/Analyst mode (two-way Socratic dialogue) MUST be explicitly enforced via persona definition (Block 2) and execution protocol (Block 5)
  - Probe phase enforcement (NFR-009) required to override default immediate-answer behavior

  **Model Selection**:
  - Patient manually toggles between GPT-5 thinking mode vs. auto mode (not controlled by system prompt)
  - System prompt MUST function correctly regardless of thinking mode setting
```

**Rationale**:
- Documents ChatGPT platform constraints affecting design (Comment 1, Comment 2, Comment 4)
- Explains why read-only Stable JSON and prompt-based validation are necessary
- Justifies Probe enforcement and Consultant/Analyst stance requirements

---

#### **9. NEW: INT-005 (Memory Review Protocol)**

**Proposed**:
```markdown
* **T810A-PROMPT-INT-005 (Memory Review Protocol)** — At the start of each conversation, the agent SHALL review ChatGPT's built-in cross-session memory BEFORE executing main protocols:

  **Step 0: Memory Review** (first step in Execution Protocol Block 5):
  - Review ChatGPT persistent memory for relevant patient history, prior patterns, ongoing concerns
  - Identify any discrepancies between memory and current Stable JSON (patient profile)
  - Flag significant changes since last session (e.g., new medications, resolved symptoms)

  **Step 1: Context Loading**:
  - Load Stable JSON (patient profile) from Knowledge Base
  - Load Dynamic JSON skeleton template for structured entry generation

  **Step 2: Protocol Execution**:
  - Proceed with main protocol workflow (Tracking → Analyze → Probe → Coach → Summarize)

  **Memory vs. Knowledge Base**:
  - **ChatGPT Memory**: Persistent across conversations, automatically updated by ChatGPT, unstructured
  - **Stable JSON**: Manually updated by patient, structured, authoritative for current profile data
  - When conflict exists, **Stable JSON takes precedence**; flag discrepancy in Probe phase

  Memory review ensures continuity while respecting patient's authority over profile updates.
```

**Rationale**:
- Implements Comment 5 (explicit memory review step)
- Clarifies relationship between ChatGPT memory and Stable JSON
- Positions memory review as Step 0 before main protocol execution

---

#### **10. NEW: DEP-008 (Research Consultation on Protocol Triggering)**

**Proposed**:
```markdown
* **T810A-PROMPT-DEP-008 (Research Consultation on Protocol Triggering)** — Implementation of NFR-008 (Protocol Triggering Intelligence) depends on research consultation to investigate VPA-style trigger condition + guard/gate patterns for clinical tracking use case. Research scope includes:
  - Analysis of `prompt/roles/VPA/main_v2.1.md` trigger/gate mechanisms
  - Prompt engineering techniques for input type detection (tracking-only vs. full protocol vs. Q&A)
  - Strategies to override ChatGPT's default "always helpful" behavior
  - Validation of mandatory Probe phase enforcement techniques

  Research brief and report required before finalizing S05 (Execution Protocol) specification.
```

**Rationale**:
- Formalizes research consultation requirement from Comment 3
- Creates dependency gate for S05 development
- Ensures evidence-based approach to protocol triggering design

---

## VII. UPDATED FEATURE DEPENDENCIES (SECTION E)

**Proposed Complete Replacement of Section E**:

```markdown
### E. Inheritances, Assumptions & Dependencies

<!-- In a Request artifact -->
* **Inherited Considerations**
| Source Artifact | Source ID | Category | Inherited Rule IDs (with hints) |
| :--- | :--- | :--- | :--- |

**Assumptions**
* **T810A-PROMPT-ASSUM-001 (Patient Profile)** — The patient is experienced and knowledgeable about their condition; minimal rapport-building (Engage phase) required.
* **T810A-PROMPT-ASSUM-002 (Input Modality & Quality)** — Inputs are unstructured English text plus images; patient responsible for image quality and manual Stable JSON updates.
* **T810A-PROMPT-ASSUM-003 (LLM Capability)** — The platform (ChatGPT) provides state-of-the-art multimodal vision + reasoning sufficient for stool/meal image interpretation and complex text analysis.
* **T810A-PROMPT-ASSUM-004 (Memory Model)** — ChatGPT's built-in cross-session memory is available and reliable; reviewed at session start per INT-005.

**Dependencies**
* **T810A-PROMPT-DEP-001 (Platform)** — Availability of ChatGPT with multimodal capability (text + image processing) and persistent cross-session memory.
* **T810A-PROMPT-DEP-002 (Patient Data Structures)** — Stable JSON (patient profile) and Dynamic JSON (tracking entries) schemas, field definitions, value sets, and validation rules are deferred to Feature **T810A2-SCHEMA**. MVP allows surface-level JSON references in T810A-PROMPT; detailed specifications out of scope.
* **T810A-PROMPT-DEP-003 (Cross-Session Reporting)** — End-of-day Dynamic JSON aggregation, multi-day pattern analysis, and formal clinician handoff format are deferred to Feature **T810A3-REPORT**.
* **T810A-PROMPT-DEP-004 (Custom Tool Interfaces)** — Custom tool declarations for structured data access (stool classification, symptom tracking, alert escalation) are deferred to Feature **T810A4-TOOLS** per CON-005.
* **T810A-PROMPT-DEP-005 (Clinical Safety Framework)** — Comprehensive clinical safety protocols (red‑flag escalation, FDA SaMD, ISO 13485, HIPAA‑aligned handling) are deferred to future development. MVP relies on ChatGPT's native safety (per CON-006) and prompt-level guidance only (per CON-007).
* **T810A-PROMPT-DEP-006 (Research Consultation on Protocol Triggering)** — Implementation of NFR-008 (Protocol Triggering Intelligence) depends on research consultation to investigate VPA-style trigger/gate patterns. Research brief and report required before finalizing S05 (Execution Protocol).
```

**Changes from Phase 1**:
- Updated feature IDs: T810D-PROFILE → T810A2-SCHEMA, T810A-REPORT → T810A3-REPORT, T810B-TOOLS → T810A4-TOOLS
- Revised DEP-002 to explicitly cover both Stable and Dynamic JSON
- Added DEP-006 for research consultation dependency
- Updated ASSUM-001 to reflect experienced patient (minimal Engage)
- Updated ASSUM-004 to acknowledge ChatGPT memory

---

## VIII. SUB-CONSULTANT BRIEF REQUIREMENTS

### A. T810A2-SCHEMA Feature Brief Outline

**Feature ID**: T810A2-SCHEMA
**Feature Name**: Patient Data Structures
**Parent Epic**: T810A-SYSTEM
**Depends On**: None
**Depended Upon By**: T810A-PROMPT (primary), T810A3-REPORT (secondary)

**Scope**:
1. **Stable JSON (Patient Profile) Schema**:
   - Field definitions (demographics, conditions, medications, triggers, relievers, notes)
   - Data categorization (constant, stable, dynamic exclusions)
   - Value set specifications for categorical fields
   - JSON schema validation rules
   - Manual update workflow specification

2. **Dynamic JSON (Tracking Entries) Schema**:
   - Entry type definitions (patient_state, meal, stool, sleep, exercise, etc.)
   - Field specifications per entry type (mandatory vs. optional keys)
   - Controlled vocabularies for each field (e.g., stress levels, bristol types, passage descriptors)
   - Flexible schema rules (when LLM can add keys)
   - Single-entry generation pattern

3. **Integration Specifications**:
   - Probe triggering rules when Dynamic JSON keys missing
   - End-of-day aggregation format (collection of Dynamic JSON entries)
   - Cross-session persistence patterns (deferred to T810A3-REPORT)

**Out of Scope**:
- Execution protocols (T810A-PROMPT)
- UI/UX for manual Stable JSON updates (future)
- Automated validation (ChatGPT constraint)
- Cross-session reporting formats (T810A3-REPORT)

**Deliverable**: `request_T810A2-SCHEMA.md` with complete JSON schemas, value sets, and integration patterns

---

### B. Handoff to Sub-Consultant

**Brief Content**:
- Phase 1.5 Analysis Document (this document)
- Conversation example (`gastro_example_conversation.md`)
- Research report excerpts (Deliverable E: Patient Profile Schema)
- Current Phase 1 implementation plan for context

**Collaboration Pattern**:
- Sub-consultant develops T810A2-SCHEMA Request in parallel with Phase 1.5
- Joint review after both Request documents drafted
- T810A-PROMPT references T810A2-SCHEMA at surface level (JSON file names, general schema structure)
- T810A2-SCHEMA contains all detailed specifications

---

## IX. PHASE 1.5 IMPLEMENTATION CHECKLIST

**For LLM_Consultant (this role)**:
- [ ] **Task 1.5.1**: Revise NFR-001 (Protocol Reliability) with tracking-first hierarchy + 2-loop pattern
- [ ] **Task 1.5.2**: Revise NFR-002 (Persona & Tone) with Consultant/Analyst mode emphasis + Tracking phase
- [ ] **Task 1.5.3**: Complete rewrite of INT-004 (Patient Data Architecture) for Stable vs. Dynamic JSON split
- [ ] **Task 1.5.4**: Minor addition to IF-003 (Explicit Classification) for numeric vs. qualitative confidence
- [ ] **Task 1.5.5**: Add NFR-008 (Protocol Triggering Intelligence) with input type detection
- [ ] **Task 1.5.6**: Add NFR-009 (Probe Phase Enforcement) with 2-loop pattern + ChatGPT override
- [ ] **Task 1.5.7**: Add IF-006 (Dynamic JSON Generation) with single-entry rules + controlled vocabularies
- [ ] **Task 1.5.8**: Add CON-008 (ChatGPT Architectural Constraints) documenting platform limitations
- [ ] **Task 1.5.9**: Add INT-005 (Memory Review Protocol) with Step 0 memory review
- [ ] **Task 1.5.10**: Add DEP-008 (Research Consultation) for protocol triggering investigation
- [ ] **Task 1.5.11**: Update Section E (Dependencies) with T810A2/A3/A4 feature IDs
- [ ] **Task 1.5.12**: Create T810A2-SCHEMA feature brief outline
- [ ] **Task 1.5.13**: Commission LLM_Researcher for protocol triggering consultation
- [ ] **Task 1.5.14**: Commission sub-consultant for T810A2-SCHEMA Request development

**For LLM_Researcher (parallel task)**:
- [ ] **Task R1**: Analyze VPA main_v2.1.md trigger/gate patterns
- [ ] **Task R2**: Research input type detection techniques for prompt engineering
- [ ] **Task R3**: Investigate ChatGPT Assistant mode override strategies
- [ ] **Task R4**: Validate Probe phase enforcement approaches
- [ ] **Task R5**: Deliver research brief + report on protocol triggering patterns

**For Sub-Consultant (parallel task)**:
- [ ] **Task SC1**: Develop T810A2-SCHEMA Request document
- [ ] **Task SC2**: Define Stable JSON schema with field specifications
- [ ] **Task SC3**: Define Dynamic JSON schema with entry types + controlled vocabularies
- [ ] **Task SC4**: Specify integration patterns (Probe triggering, end-of-day aggregation)
- [ ] **Task SC5**: Coordinate with T810A-PROMPT consultant for surface-level references

---

## X. PHASE 1.5 VALIDATION CRITERIA

**Phase 1.5 Complete When**:
- [ ] All 10 new/revised F-IDs approved by Client
- [ ] Section E (Dependencies) updated with T810A2/A3/A4 feature IDs
- [ ] T810A2-SCHEMA feature brief created and sub-consultant commissioned
- [ ] Research consultation commissioned for protocol triggering patterns
- [ ] No conflicts between Phase 1 + Phase 1.5 specifications
- [ ] Phase 1 implementation plan updated to include Phase 1.5 tasks

**Gate to Phase 2**:
- Phase 1.5 specification updates implemented in Request document
- Research consultation completed (or in progress with preliminary findings)
- T810A2-SCHEMA Request drafted (or in progress with preliminary schema)
- Client approval for all Phase 1.5 changes before proceeding to Phase 2 (Feature GDR creation)

---

## XI. RISKS & MITIGATION

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|
| **Scope expansion delays Phase 2** | High | Medium | Parallel execution of research + sub-consultant tasks; surface-level references in T810A-PROMPT |
| **VPA pattern not applicable to clinical use** | Medium | Low | Research consultation includes applicability validation; alternative patterns if needed |
| **ChatGPT override insufficient** | High | Medium | S08 (Exemplars) will include extensive Probe examples; Block 5 (Execution Protocol) will have explicit Probe enforcement instructions |
| **Stable/Dynamic JSON confusion** | Medium | Low | Clear naming, explicit read-only vs. generative distinctions, T810A2-SCHEMA detailed specs |
| **T810A2-SCHEMA delays T810A-PROMPT** | Medium | Low | Surface-level references allow parallel development; detailed schema not blocking for Phase 2 |

---

## XII. NEXT STEPS

**Immediate Actions** (before Phase 2):
1. Client review and approval of Phase 1.5 F-ID proposals
2. Update `phase1_implementation_plan.md` to include Phase 1.5 tasks
3. Commission LLM_Researcher for protocol triggering consultation
4. Create T810A2-SCHEMA feature brief and commission sub-consultant

**After Phase 1.5 Approval**:
1. Implement all F-ID changes in Request document (Sections F-I)
2. Update Phase 1 gastro_system.md Block 2 revisions (if needed based on NFR-002)
3. Proceed to Phase 2: Feature GDR Index creation (6 GDRs referencing updated F-IDs)

---

## XIII. APPENDICES

### A. VPA Pattern References

**Source**: `prompt/roles/VPA/main_v2.1.md`

**Key Patterns Observed**:
1. **Trigger Conditions**: Each protocol has explicit entry conditions
2. **Guard & Gates**: Prevent unnecessary protocol re-execution
3. **Mandatory Sequence**: Absolute response structure (PRIORITY SEQUENCE)
4. **Input Type Detection**: Keywords + context clues determine protocol execution

**Example** (VPA SPP):
```markdown
### TRIGGER CONDITIONS
- When the user explicitly asks to rerun the SPP

### GUARD & GATES
- Never rerun SPP without user request, always use the latest available values from prior run.
```

**Applicability to LLM_Gastro**:
- Tracking-only trigger: Explicit "UPDATE JSON" keyword
- Full protocol trigger: Narrative note + images (implicit)
- Q&A trigger: Direct question without tracking data
- Guard: After JSON generation, check if analysis requested

---

### B. Conversation Anti-Patterns

**From Example Conversation**:

❌ **Anti-Pattern 1**: Skipping Probe Phase
- Turn 1: JSON → Analysis → Coaching (no clarifying questions asked)
- Expected: JSON → Analysis → Probe ("Can you describe...") → Coach (next loop)

❌ **Anti-Pattern 2**: Assistant-Mode Service Offers
- Turn 1: "If you like, I can turn this into a one-page daily protocol..."
- Turn 3: "Would you like me to now build a structured AM/PM Daily Routine Protocol Sheet?"
- Expected: "How often does this happen?" or "What did you notice about your stress levels?"

❌ **Anti-Pattern 3**: Cumulative JSON Generation
- Turn 2: Regenerated all previous entries + new entries (full conversation log)
- Expected: Single new entry only (per interaction pattern)

❌ **Anti-Pattern 4**: Protocol Non-Triggering
- Turn 2: Generated JSON, stopped, awaited explicit "Proceed with analysis..." command
- Expected: Auto-trigger full protocol after JSON generation (unless explicit tracking-only request)

---

**Document Status**: Draft
**Approval Required**: Client approval for Phase 1.5 F-ID proposals before implementation
**Next Review**: After LLM_Researcher and sub-consultant commission

---

## XIV. CHANGELOG

- **v1.0.0** (2025-10-11): Initial Phase 1.5 analysis with conversation gap identification, 10 F-ID proposals (4 revisions + 6 new), research consultation requirement, and T810A2-SCHEMA sub-consultant brief outline