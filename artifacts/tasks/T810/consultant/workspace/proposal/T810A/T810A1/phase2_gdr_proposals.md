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
target_document: 'request_T810A1-PROMPT.md'
target_section: 'III.M (Feature Governance Decision Records)'
---

# PHASE 2: FEATURE GDR EXPANSION PROPOSALS

## I. EXECUTIVE SUMMARY

This document proposes 6 Feature-level Governance Decision Records (F-GDRs) for inclusion in `request_T810A1-PROMPT.md` Section III.M. All GDRs have been expanded from draft proposals to full ADR format following T102-ADR-004-FR-002 specifications.

**Key Changes from Draft Proposals**:
- Complete ADR body structure (Context, Decision, Consequences, References)
- **Removed all story-level FR references** per T102-ADR-005 precedence rules
- Referenced only F-IDs (Feature-level requirements) and Research IDs
- Added Phase 1.5 empirical findings where relevant
- Consequences structured with (+)/(±)/(-) notation

**Compliance**:
- ✅ T102-ADR-004-FR-001: GDR Index Schema with required columns
- ✅ T102-ADR-004-FR-002: Decision Records Body with shared subheadings
- ✅ T102-ADR-005-FR-003: Precedence & Directionality (F-GDRs reference F-IDs only, not S-IDs)
- ✅ T102-ADR-005-FR-006: ID References using back-ticked `ID (Title)` tokens

---

## II. PROPOSED SECTION III.M CONTENT

### M. Feature Governance Decision Records

**GDR Index**

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|--------|-------|--------|-------|-----------|------------|--------|
| `T810A1-GDR-001` | Tracking-First Clinical Protocol | Proposed | Client | 2025-10-11 | — | #t810a1-gdr-001-tracking-protocol |
| `T810A1-GDR-002` | Trust-and-Verify Workflow Standard | Proposed | Client | 2025-10-11 | — | #t810a1-gdr-002-trust-verify |
| `T810A1-GDR-003` | Stable/Dynamic JSON Architecture | Proposed | Client | 2025-10-11 | — | #t810a1-gdr-003-json-architecture |
| `T810A1-GDR-004` | Session Workflow Architecture | Proposed | Client | 2025-10-11 | — | #t810a1-gdr-004-session-workflow |
| `T810A1-GDR-005` | GI Knowledge Base Sources | Proposed | Client | 2025-10-11 | — | #t810a1-gdr-005-knowledge-sources |
| `T810A1-GDR-006` | Dual-Purpose Clinical Reporting | Proposed | Client | 2025-10-11 | — | #t810a1-gdr-006-clinical-reporting |

**GDR Bodies**

* **T810A1-GDR-001 (Tracking-First Clinical Protocol) {#t810a1-gdr-001-tracking-protocol}**

  **Context.** Research validation (`T810A1-RES-001` Deliverable C) confirms the Engage→Analyze→Probe→Coach→Summarize protocol as industry-aligned clinical communication framework (Motivational Interviewing, Cognitive Behavioral Therapy, clinical AI best practices). However, empirical conversation analysis (`T810A1-RES-002`) revealed that the primary use case is **tracking + analysis** (data capture and pattern recognition), not general clinical conversation. The equal 5-phase protocol assumption creates architectural friction: patients need rapid tracking-first workflow with optional full protocol execution. Without protocol priority hierarchy, the agent defaults to comprehensive consultation mode even for simple tracking inputs, violating user intent and creating unnecessary interaction overhead.

  **Decision.** Adopt **Tracking-First Clinical Protocol Hierarchy** as the governing execution model for LLM_Gastro:
  - **Primary (always execute)**: Tracking (structured data capture via Dynamic JSON per `T810A1-IF-006`) + Analyze (pattern analysis of current + historical data per `T810A1-NFR-004`)
  - **Secondary (mandatory before coaching)**: Probe (Socratic inquiry with ≥2 clarifying questions per `T810A1-NFR-009`)
  - **Tertiary (conditional on data sufficiency)**: Coach (management recommendations) + Summarize (action plan recap)

  The protocol SHALL aim for a minimum 2-loop conversation pattern: Loop 1 generates Dynamic JSON + performs analysis + asks clarifying questions (no coaching); Loop 2 refines analysis with probe answers + provides coaching + summarizes action plan. Engage phase is merged into Probe for experienced patients per `T810A1-ASSUM-001`. Coach and Summarize SHALL NOT execute until Probe phase demonstrates sufficient data confidence per `T810A1-NFR-009`.

  This decision establishes tracking + analysis as the foundation; clinical consultation (Probe→Coach→Summarize) builds upon it rather than competing equally.

  **Consequences.**
  - (+) Aligns protocol with actual use case (tracking-first workflow) validated by real conversation behavior
  - (+) Maintains industry-validated 5-phase clinical communication framework while adapting priority hierarchy
  - (+) Enables smart protocol triggering per `T810A1-NFR-008` (tracking-only vs. full protocol execution)
  - (+) Supports rapid daily tracking interactions without forcing unnecessary full consultation overhead
  - (±) Requires careful Execution Protocol (Block 5) specification to balance tracking efficiency with clinical inquiry depth
  - (±) Soft guideline for 2-loop pattern (no hard gates in ChatGPT) requires Probe enforcement via exemplars per `T810A1-NFR-009`
  - (-) Deviates from research-validated equal-phase model; relies on empirical validation to justify hierarchy

  **References.**
  `T810A1-RES-001` (Deliverable C: Clinical Protocol Validation),
  `T810A1-RES-002` (Conversation-Driven Empirical Validation),
  `T810A1-NFR-001` (Protocol Reliability),
  `T810A1-NFR-002` (Persona & Tone),
  `T810A1-NFR-008` (Protocol Triggering Intelligence),
  `T810A1-NFR-009` (Probe Phase Enforcement),
  `T810A1-IF-006` (Dynamic JSON Generation),
  `T810A1-ASSUM-001` (Patient Profile)

---

* **T810A1-GDR-002 (Trust-and-Verify Workflow Standard) {#t810a1-gdr-002-trust-verify}**

  **Context.** Research validation (`T810A1-RES-001` Deliverable B) identifies confidence communication and user validation as essential multimodal AI pattern, particularly for image classification tasks (stool Bristol scale, meal analysis). Without explicit confidence thresholds and validation workflows, the agent risks either overstating certainty (creating false confidence) or understating reliability (undermining clinical utility). Empirical conversation analysis (`T810A1-RES-002`) revealed numeric confidence in JSON outputs (`"confidence": 0.7`) without corresponding qualitative communication in natural language, creating disconnect between machine representation and user-facing communication.

  **Decision.** Adopt **Trust-and-Verify Workflow Standard** with qualitative confidence communication and validation intensity thresholds:
  - **High Confidence** (agent assessment: >90% certain): State classification with brief rationale; validation optional ("This appears to be Bristol Type 5-6 based on...")
  - **Moderate Confidence** (agent assessment: 70-90% certain): State classification with detailed rationale + encourage user validation in Probe phase per `T810A1-IF-003` ("I see this as Bristol Type 5, though the lighting makes it somewhat ambiguous. Does that match what you observed?")
  - **Low Confidence** (agent assessment: <70% certain): State uncertainty explicitly + mandatory validation request ("The image quality makes definitive classification difficult. What did you observe?")

  The agent SHALL use qualitative descriptors ("fairly confident," "moderate confidence," "uncertain") in natural language communication per `T810A1-NFR-007`. Numeric confidence fields (e.g., `"confidence": 0.75`) MAY be included in Dynamic JSON for internal tracking and pattern analysis per `T810A1-IF-003`, but SHALL NOT appear in user-facing text.

  Validation requests SHALL NOT block conversational flow; agent proceeds with analysis using stated confidence level and incorporates user corrections in subsequent turns.

  **Consequences.**
  - (+) Industry-aligned multimodal AI pattern validated by research across clinical AI applications
  - (+) Balances clinical accuracy needs with conversational fluidity (validation encouragement, not mandatory blocking)
  - (+) Clear distinction between machine-readable confidence (numeric in JSON) and user-readable confidence (qualitative in prose)
  - (+) Explicit uncertainty communication builds user trust and enables correction loops
  - (±) Moderate/low confidence scenarios increase interaction turns (Probe phase validation before Coach)
  - (±) Threshold boundaries (70%, 90%) are guidelines; actual phrasing adapted per context in Execution Protocol (Block 5)
  - (-) No programmatic validation capability per `T810A1-CON-008`; relies entirely on prompt-based enforcement

  **References.**
  `T810A1-RES-001` (Deliverable B: Multimodal Trust-and-Verify Patterns),
  `T810A1-RES-002` (Conversation-Driven Empirical Validation),
  `T810A1-NFR-007` (Confidence Communication),
  `T810A1-IF-003` (Explicit Classification),
  `T810A1-CON-008` (ChatGPT Architectural Constraints)

---

* **T810A1-GDR-003 (Stable/Dynamic JSON Architecture) {#t810a1-gdr-003-json-architecture}**

  **Context.** Initial research validation (`T810A1-RES-001` Deliverable E) identified constant/stable/dynamic data categorization for patient profiles. However, empirical conversation analysis (`T810A1-RES-002`) revealed architectural mismatch: actual conversation generated cumulative JSON (Turn 2 regenerated all Turn 1 entries + new entries) instead of single-entry tracking pattern. Client directive (Phase 1.5 Comment 1) specified architectural requirement: "Instead of a single JSON file system, we will need multiple JSON files, at least starting with two: stable and dynamic." ChatGPT platform constraint (`T810A1-CON-008`) imposes read-only file access for LLM, preventing direct profile updates. Without clear architectural separation, the system conflates persistent profile context (demographics, conditions) with ephemeral tracking data (daily meals, stools), creating token inefficiency and cross-session persistence challenges.

  **Decision.** Adopt **Stable/Dynamic JSON Split Architecture** as the canonical data model for LLM_Gastro:

  **Stable JSON (Patient Profile)**:
  - Contains constant patient data (demographics: age, sex) and stable data (conditions, medications, triggers, relievers, allergies, clinical history notes) per `T810A2` specifications
  - Stored in Knowledge Base (Block 4), manually updated by patient outside conversation
  - **Read-only** for LLM_Gastro per `T810A1-CON-008` (ChatGPT file system constraint)
  - Loaded at session start per `T810A1-INT-005` (Step 1: Context Loading after memory review)
  - Detailed field definitions, schema validation, and value sets deferred to `T810A2-SCHEMA` per `T810A1-DEP-004`

  **Dynamic JSON (Tracking Entries)**:
  - LLM_Gastro generates **single entry per patient interaction** containing event data: patient_state, meal, stool, sleep, or other clinically relevant observations per `T810A1-IF-006`
  - Uses structured keys with controlled vocabularies (value sets defined in `T810A2-SCHEMA`)
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
  - (±) Surface-level architecture in T810A1-PROMPT; detailed schemas in T810A2-SCHEMA (dependency coordination required)
  - (-) Risk of Stable JSON staleness if patient doesn't maintain profile; mitigated by memory review protocol per `T810A1-INT-005`

  **References.**
  `T810A1-RES-001` (Deliverable E: Patient Profile Schema),
  `T810A1-RES-002` (Conversation-Driven Empirical Validation),
  `T810A1-INT-004` (Patient Data Architecture),
  `T810A1-INT-005` (Memory Review Protocol),
  `T810A1-IF-006` (Dynamic JSON Generation),
  `T810A1-NFR-009` (Probe Phase Enforcement),
  `T810A1-CON-008` (ChatGPT Architectural Constraints),
  `T810A1-DEP-004` (Patient Data Structures Dependency),
  `T810A1-DEP-002` (Long-term Analysis Dependency)

---

* **T810A1-GDR-004 (Session Workflow Architecture) {#t810a1-gdr-004-session-workflow}**

  **Context.** Research validation (`T810A1-RES-001` Deliverable G) identifies hybrid onboarding (guided + conversational) and daily continuity patterns (profile + previous report injection) as clinical AI best practices. Empirical conversation analysis (`T810A1-RES-002`) revealed missing Step 0: no explicit ChatGPT cross-session memory review before protocol execution, creating risk of memory-profile discrepancies. Client directive (Phase 1.5 Comment 5) mandated: "LLM_Gastro always reminds that it does have cross-session/chat memory... it needs to review this first before proceeding with any main execution protocols." Without structured session workflow, the agent lacks consistent initialization pattern and risks conflating ChatGPT's automatic memory with patient-governed Stable JSON, undermining data authority and introducing inconsistent session context.

  **Decision.** Adopt **Session Workflow Architecture** with memory-first initialization:

  **First-Session Initialization** (Hybrid Onboarding):
  - Guided profile elicitation for critical constant/stable fields (age, sex, conditions, medications, triggers, relievers)
  - Conversational style maintains partnership stance per `T810A1-NFR-002` (not checklist interrogation)
  - Output initial Stable JSON draft for patient to review and manually save

  **Daily Session Workflow** (Multi-Session Continuity) per `T810A1-INT-005`:
  - **Step 0: Memory Review** (FIRST STEP before protocols):
    - Review ChatGPT persistent memory for relevant patient history, prior symptom patterns, ongoing clinical concerns
    - Identify discrepancies between memory and current Stable JSON (patient profile)
    - Flag significant changes since last session (e.g., new medications started, symptoms resolved, dietary modifications)
  - **Step 1: Context Loading**:
    - Load Stable JSON (patient profile) from Knowledge Base per `T810A1-INT-004`
    - Load Dynamic JSON skeleton template for structured entry generation per `T810A1-IF-006`
    - Load previous session's clinical report (if available) per `T810A1-IF-005` for continuity
  - **Step 2: Protocol Execution**:
    - Proceed with main protocol workflow (Tracking → Analyze → Probe → Coach → Summarize per `T810A1-NFR-001`)

  **Memory vs. Stable JSON Conflict Resolution** per `T810A1-INT-005`:
  - ChatGPT Memory: Persistent across conversations, automatically updated by ChatGPT, unstructured narrative format
  - Stable JSON: Manually updated by patient, structured authoritative data, governance-controlled
  - **When conflict exists, Stable JSON takes precedence** as single source of truth
  - Flag discrepancy in Probe phase: "I notice in my memory you mentioned [X], but your profile shows [Y]. Has this changed?"

  This decision establishes memory review as mandatory Step 0, respects patient authority over profile updates, and enables consistent session initialization across first-time and returning interactions.

  **Consequences.**
  - (+) Industry-validated session workflow patterns aligned with clinical AI best practices
  - (+) Explicit memory review step prevents ChatGPT automatic updates from overriding patient-governed Stable JSON
  - (+) Clear conflict resolution hierarchy (Stable JSON > ChatGPT Memory) with graceful discrepancy flagging in Probe
  - (+) Multi-session continuity via previous report injection reduces redundant questioning
  - (±) Hybrid onboarding requires careful balance between guided elicitation and conversational partnership stance
  - (±) Memory review adds initial overhead to each session; mitigated by streamlined Step 0 implementation
  - (-) Relies on patient diligence to keep Stable JSON updated; staleness risk accepted per `T810A1-RISK-005`

  **References.**
  `T810A1-RES-001` (Deliverable G: Session Workflow Patterns),
  `T810A1-RES-002` (Conversation-Driven Empirical Validation),
  `T810A1-INT-004` (Patient Data Architecture),
  `T810A1-INT-005` (Memory Review Protocol),
  `T810A1-IF-005` (Session Context Injection),
  `T810A1-IF-006` (Dynamic JSON Generation),
  `T810A1-NFR-001` (Protocol Reliability),
  `T810A1-NFR-002` (Persona & Tone)

---

* **T810A1-GDR-005 (GI Knowledge Base Sources) {#t810a1-gdr-005-knowledge-sources}**

  **Context.** Research validation (`T810A1-RES-001` Deliverable D) identifies ROME IV criteria, Bristol Stool Chart, ACG/AGA clinical guidelines, and alarm features as essential GI expert knowledge sources for diagnostic reasoning and safety escalation. Without explicitly defined knowledge base sources, the agent risks relying on general training knowledge that may be outdated, incomplete, or inconsistent with current gastroenterology best practices. The agent's core competencies per `T810A1-NFR-004` (holistic analysis incorporating adjacent factors) and clinical reasoning requirements depend on authoritative, validated clinical knowledge rather than general LLM training corpus.

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
  `T810A1-RES-001` (Deliverable D: GI Expert Workflows),
  `T810A1-NFR-004` (Holistic Analysis),
  `T810A1-IF-003` (Explicit Classification),
  `T810A1-CON-006` (Platform Compatibility),
  `T810A1-CON-007` (Clinical Compliance Deferral),
  `T810A1-DEP-005` (Clinical Safety Framework Dependency)

---

* **T810A1-GDR-006 (Dual-Purpose Clinical Reporting) {#t810a1-gdr-006-clinical-reporting}**

  **Context.** Research validation (`T810A1-RES-001` Deliverable F) confirms chronological timeline format in first-person patient perspective as optimal for both clinician handoff (human-readable summary) and LLM memory (context injection for next session). Traditional clinical notes use third-person clinician voice ("Patient reports..."), creating disconnect for patient-authored documentation. Empirical conversation analysis did not test reporting directly but validated tracking-first workflow requiring efficient end-of-day aggregation pattern per `T810A1-INT-002`. Without dual-purpose design, separate formats would be needed for clinician communication vs. LLM memory consumption, increasing complexity and token overhead.

  **Decision.** Adopt **Dual-Purpose Clinical Reporting Architecture** with unified format serving both clinician handoff and LLM memory:

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
  `T810A1-RES-001` (Deliverable F: Clinical Reporting Architecture),
  `T810A1-INT-002` (Memory Handoff Protocol),
  `T810A1-IF-005` (Session Context Injection),
  `T810A1-NFR-002` (Persona & Tone),
  `T810A1-DEP-002` (Long-term Analysis Dependency)

---

## III. IMPLEMENTATION NOTES

### A. Compliance with T102-ADR-005 (ID Specification & Rules)

**FR-003 (Precedence & Directionality)**:
- ✅ All GDRs reference **only F-IDs** (Feature-level requirements) and Research IDs
- ✅ **Zero story-level FR references** (S-IDs) - all removed from draft proposals
- ✅ Upstream-to-downstream referencing maintained (F-GDRs reference F-IDs, not vice versa)

**Removed Story-Level References**:
- GDR-001 Draft: `T810A1-S02-FR-003`, `T810A1-S05-FR-001` → Removed (replaced with `T810A1-NFR-001`, `T810A1-NFR-002`)
- GDR-002 Draft: `T810A1-S05-FR-003` → Removed (replaced with `T810A1-IF-003`, `T810A1-NFR-007`)
- GDR-003 Draft: `T810A1-S04-FR-003` → Removed (replaced with `T810A1-INT-004`, `T810A1-IF-006`)
- GDR-004 Draft: `T810A1-S05-FR-004`, `T810A1-S09-FR-005` → Removed (replaced with `T810A1-INT-005`, `T810A1-IF-005`)
- GDR-005 Draft: `T810A1-S04-FR-001`, `T810A1-S04-FR-002` → Removed (replaced with `T810A1-NFR-004`, `T810A1-IF-003`)
- GDR-006 Draft: `T810A1-S09-FR-001` → Removed (replaced with `T810A1-INT-002`)

**Referencing Pattern**:
- F-IDs: NFR (Non-Functional Requirements), IF (Interfaces), INT (Integration Notes), CON (Constraints), DEP (Dependencies), ASSUM (Assumptions)
- Research IDs: RES-001, RES-002
- NO references to: S-IDs (story-level FRs), F-GDRs (GDRs don't reference each other in v1)

### B. Compliance with T102-ADR-004 (Decision Records Index)

**FR-001 (DR Index Schema)**:
- ✅ 7 columns: GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor
- ✅ ID Pattern: `T810A1-GDR-###` per T102-ADR-005-FR-002
- ✅ Status: "Proposed" (pending Client approval)
- ✅ Owner: "Client" (decision owner per artifact header)
- ✅ Effective: "2025-10-11" (today's date, becomes active upon approval)
- ✅ Supersedes: "—" (all new GDRs, no superseded decisions)
- ✅ Anchor: Lower-kebab format (`#t810a1-gdr-001-tracking-protocol`)

**FR-002 (Decision Records Body)**:
- ✅ Title format: `* **T810A1-GDR-### (Title) {#anchor}**`
- ✅ Shared subheadings: Context, Decision, Consequences, References
- ✅ Consequences notation: (+) positive, (±) neutral/mixed, (-) negative/trade-off
- ✅ References: Back-ticked `ID (Title)` tokens per T102-ADR-005-FR-006

### C. Integration with Phase 1.5 F-IDs

**GDR-001 (Tracking-First Protocol)**:
- Incorporates `T810A1-NFR-001` (revised priority hierarchy)
- Incorporates `T810A1-NFR-008` (Protocol Triggering Intelligence)
- Incorporates `T810A1-NFR-009` (Probe Phase Enforcement)

**GDR-002 (Trust-and-Verify)**:
- Incorporates `T810A1-IF-003` (numeric vs. qualitative confidence clarification)

**GDR-003 (Stable/Dynamic JSON)**:
- Incorporates `T810A1-INT-004` (complete rewrite for Stable/Dynamic split)
- Incorporates `T810A1-IF-006` (Dynamic JSON Generation specifications)
- Incorporates `T810A1-CON-008` (ChatGPT Architectural Constraints)

**GDR-004 (Session Workflow)**:
- Incorporates `T810A1-INT-005` (Memory Review Protocol - new Step 0)

**GDR-005 (GI Knowledge Sources)**:
- No Phase 1.5 updates (stable from Phase 1)

**GDR-006 (Clinical Reporting)**:
- No Phase 1.5 updates (stable from Phase 1)

### D. Version Control

**After Client Approval**:
- Update `request_T810A1-PROMPT.md` to include Section III.M with complete GDR Index + Bodies
- No version bump required (Section M addition completes existing v1.0.0 scope per Phase 2 plan)
- Add changelog entry: "Phase 2: Added Section III.M (Feature Governance Decision Records) with 6 F-GDRs establishing governance for tracking-first protocol, trust-and-verify workflow, Stable/Dynamic JSON architecture, session workflow, GI knowledge sources, and dual-purpose reporting"

---

## IV. CLARIFYING QUESTIONS FOR CLIENT

Before implementing GDRs in request document, please confirm:

1. **GDR Scope**: Do the 6 proposed GDRs adequately cover all governance decisions for T810A1-PROMPT, or are additional GDRs needed (e.g., for Protocol Triggering Intelligence, Probe Phase Enforcement)?

2. **Phase 1.5 Integration**: Are the Phase 1.5 F-ID incorporations (NFR-001, NFR-008, NFR-009, INT-004, IF-006, CON-008, INT-005) correctly reflected in GDR bodies?

3. **Story-Level Reference Removal**: Confirm that removing all story-level FR references (S-IDs) from GDRs is correct per T102-ADR-005 precedence rules, even when GDRs logically govern story-level implementation?

4. **GDR vs. ADR Distinction**: Should any of these GDRs actually be Feature ADRs (F-ADRs) instead of F-GDRs? Current understanding: GDRs = governance/policy decisions, ADRs = architectural/implementation decisions. All 6 proposals are governance-level, so F-GDR classification seems correct.

5. **Consequences Detail Level**: Are the (+)/(±)/(-) consequence bullets sufficiently detailed, or should they be more granular (e.g., specific implementation impacts on Stories S04-S10)?

6. **Reference Completeness**: Are there any missing F-ID references that should be included in GDR References sections?

---

## V. NEXT STEPS

**Upon Client Approval**:
1. Insert complete Section III.M (GDR Index + Bodies) into `request_T810A1-PROMPT.md`
2. Update Section II (Table of Contents) to include Section M
3. Add changelog entry documenting Phase 2 completion
4. Mark Phase 2 complete in consultancy plan (`plan_T810A-PROMPT_phase1-4_v1.0.0.md`)
5. Proceed to Phase 3: Story Specification (S04-S10 development with ~30-40 new F-IDs)

**Pending Items**:
- Phase 3: Stories S04-S10 functional requirements (will reference governing GDRs)
- T810A2-SCHEMA sub-consultant collaboration (parallel track)
- Research consultation on protocol triggering (deferred to S05 development per `T810A1-DEP-008`)

---

**Document Status**: Draft
**Approval Required**: Client approval for all 6 F-GDR proposals before insertion into request document
**Next Review**: After client feedback on GDR expansions

---

## VI. CHANGELOG

- **v1.0.0** (2025-10-11): Initial Phase 2 GDR expansion proposals with complete ADR body structure per T102-ADR-004-FR-002, removed all story-level FR references per T102-ADR-005-FR-003, integrated Phase 1.5 F-ID updates, and structured consequences with (+)/(±)/(-) notation
