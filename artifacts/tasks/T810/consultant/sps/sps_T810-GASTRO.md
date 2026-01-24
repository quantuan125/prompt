---
artifact_type: 'SPS'
initiative_id: 'T810'
initiative_code: 'GASTRO'
version: '1.0.0'
date: '2025-12-15'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# SYNTHESIZED PROBLEM STATEMENT (SPS): GASTRO — T810

<!-- PURPOSE: This is a minimal structural skeleton for the GASTRO initiative (T810). 
Fill each subsection with concise, decision-ready content. Keep YAML frontmatter current. -->

## I. EXECUTIVE SUMMARY
<!-- One paragraph describing the core problem, the desired outcome, and the recommended direction. Avoid details; link to sections below. -->

## II. TABLE OF CONTENTS
<!-- Optional for shorter docs. Tools may auto-generate. -->

## III. CORE CONTENT

### A. Problem Definition

#### 1. The Problem
<!-- Define the user/business problem in plain terms. Include who is affected and the current pain. -->

#### 2. The Desired Outcome
<!-- State measurable, verifiable outcomes. Prefer objective targets over activities. -->

#### 3. Business Case
<!-- Why this matters now: impact, urgency, constraints at a high level. -->

### B. Initiative Considerations
<!-- Governance and cross-cutting concerns applicable to all options. Keep bullets short and testable. -->

#### 1. Organization & Responsibilities

#### 2. Project Assumptions
<!-- Unverified beliefs shaping scope/approach. Keep each assumption atomic and testable. -->

#### 3. Project Constraints
<!-- Non-negotiable boundaries (compliance, timebox, architecture, tooling). Use SHALL language where applicable. -->

#### 4. Success Criteria & Quality Goals
<!-- Verifiable acceptance criteria. Aim for binary pass/fail checks and clear owners. -->

#### 5. Dependencies
<!-- External prerequisites, upstream inputs, or capacity dependencies. Include ownership and availability windows. -->

#### 6. Interfaces
<!-- Roles and process touchpoints (e.g., Client review, Planner handoff). Define cadence and SLAs. -->

#### 7. Implementation Guidance
<!-- Technical/operational guidance for downstream teams. Keep normative (“SHOULD/SHALL”) where helpful. -->

#### 8. Research & Notes
**Research**

**Notes**

#### 9. Governance Decisions
<!-- Record major decisions with context, decision, consequences, and references. Keep entries short; link out if needed. -->

#### 10. Issues & Risks
<!-- Track open issues/risks with status/priority. Prefer a small table. Keep IDs stable. -->

<!-- NOTES
- Keep this document concise; push deep detail to appendices or linked artifacts.
- Maintain end-to-end traceability: every decision should map to criteria, constraints, and downstream handoff.
- Update the frontmatter on each meaningful change (version, date, status).
-->

### C. Epics & Breakdown

#### 0. Initiative WBS Map
<!-- PURPOSE: High-level structural index only; keep synchronized with sections below. -->

| Level | PM Type | ID | Name |
| :--- | :--- | :--- | :--- |
| 1 | Initiative | T810 | GASTRO |
| 2 | Epic | T810A | SYSTEM |

---

#### 1. `T810A` Epic: `SYSTEM` - Gastroentologist Agent System
<!-- PURPOSE: Epic dossier skeleton. Inherit global rules from Section III-B; add epic-specific scope, goals, and controls. -->

```yaml
epic_id: 'T810A'
epic_code: 'SYSTEM'
epic_title: 'Gastroentologist Agent System'
epic_type: 'new'             # new | existing | general
epic_status: 'draft'         # draft | review | approved | deprecated
epic_owner: 'LLM_Consultant'    # Role or named owner
```

##### i. Purpose
<!-- State the primary goal and outcome of this Epic in 1-2 paragraphs. -->

##### ii. Scope
<!-- Define explicit boundaries: in-scope vs out-of-scope. Keep bullets short. -->

- In Scope:
- Out of Scope:

##### iii. Inherited Considerations
<!-- List inherited governance items this Epic must honor. Reference IDs; avoid duplicating text. -->

##### iv. Governance & Roadmap
<!-- Milestone-level oversight. Detailed planning remains in external PM tools if any. -->

**Scope & Ownership**

**Phase Sequence**

**Success Checkpoints**

**References**

##### v. Feature Register
<!-- PURPOSE: The official list of work for this Epic. Each Feature is fully specified in its own Request artifact (the WBS dictionary). -->
| ID | Code | Name | Purpose | Owner | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T810A1` | `PROMPT` | LLM_Gastro System Prompt | Modular 9‑block prompt for clinical tracking, analysis, probing, and coaching | `LLM_Consultant` | `in-request` | `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md` |
| `T810A2` | `PATIENT` | Patient Data Structures | Patient profile schema + tracking entry schemas + controlled vocabularies | `LLM_Consultant (Sub‑Consultant)` | `proposed` | — |
| `T810A3` | `REPORT` | Reporting & Continuity | Daily report format, aggregation, and next‑session context injection | `LLM_Consultant` | `proposed` | — |
| `T810A4` | `TOOLS` | Tooling Integrations | Custom tools/APIs for advanced workflows (deferred) | `LLM_Consultant` | `proposed` | — |


##### vi. Epic Requirements
<!-- Define the Epic's objectives and verifiable requirements. Keep atomic and testable. -->

**Quality Goals**
<!-- Measurable goals that prove success. -->

**T810A-QG-001 (Clinical Protocol Reliability)** — Features providing clinical interaction SHALL implement structured, repeatable protocols according to research on human expert practices in gastrointestinal and diet domains. Protocols SHALL prioritize data capture and analysis before guidance, ensure sufficient information gathering through probing/clarification loops, and maintain consistent execution across sessions. Protocol designs MUST be founded on industry-standard practices and validated methodologies from clinical gastroenterology and dietary management. Specific phase sequences, loop patterns, and implementation details are feature-defined.

**T810A-QG-002 (Persona & Tone)** — User-facing features SHALL adopt **Consultant/Analyst** persona, overriding ChatGPT's native Assistant behavior. Tone is adaptive based on interaction type and clinical context: structured and precise for data capture, objective and evidence-based for analysis, collaborative and Socratic for clarification, empathetic for engagement, supportive and safety-bounded for guidance, clear and concise for summarization. Features SHALL prioritize clinical inquiry over helpfulness offers. Specific tone mappings for feature-specific interaction types are feature-defined.

**T810A-QG-003 (Analysis Performance)** — Thoughtful responses are prioritized; 30–120 seconds latency is acceptable for consultant-level analysis.

**T810A-QG-004 (Holistic Analysis)** — Clinical analysis performed by features SHALL incorporate adjacent factors when present (stress, sleep, exercise, medications, lifestyle) while maintaining primary focus on gastroenterology and dietary patterns. Features providing analytical capabilities MUST consider multi-dimensional context rather than isolated symptom assessment. Holistic approach applies to all analytical functions (pattern recognition, hypothesis generation, trend analysis) across features.

**T810A-QG-005 (Architecture Maintainability)** — Features SHALL adopt modular, well-documented architectures that enable independent updates to role definitions, knowledge sources, execution logic, and behavioral rules without cascading changes. Implementation patterns (block-based prompt structures, schema-driven definitions, template modularization) are feature-defined. Clear separation of concerns and explicit dependencies are required for sustainable evolution.

**T810A-QG-006 (Patient Usability)** — Language and reasoning target a user with medium literacy in the gastrointestinal domain. Features SHALL present domain-specific clinical terminology alongside clear explanations in plain language for patient understanding. Communication MUST balance professional accuracy with accessibility:

  - **Domain Language with Explanations**: Use clinical terminology (e.g., "Bristol Stool Chart Type 4", "malabsorption", "SIBO") but ALWAYS provide immediate plain-language explanations (e.g., "Bristol Type 4 means soft, smooth stool — considered ideal consistency")
  - **Patient Education Priority**: Every complex concept from gastroenterology or dietetics MUST be explained in accessible terms without condescension
  - **Cognitive Load Management**: Communication SHALL NOT overwhelm the patient; use progressive disclosure (explain foundational concepts before building to advanced patterns)
  - **Non-Paternalistic Tone**: Avoid paternalistic language; maintain partnership stance respecting patient expertise in their lived experience

  Features targeting technical audiences (e.g., schema documentation for developers) may adjust literacy level while maintaining clarity principles.

**T810A-QG-007 (Confidence Communication)** — When classifying images or generating hypotheses, the agent SHALL communicate confidence using qualitative descriptors (e.g., 'fairly confident,' 'moderate confidence,' 'uncertain') rather than numerical percentages. Confidence indicators enable appropriate user validation without interrupting conversational flow.

**T810A-QG-008 (Clarification Over Guessing)** — User-facing features SHALL implement clarification mechanisms rather than guessing or hallucinating when input data is insufficient or ambiguous. Features MUST default to requesting additional information when confidence is low or context is unclear. Implementation patterns (probing loops, confirmation prompts, explicit uncertainty statements) are feature-defined based on interaction model.

**Dependencies**

<!-- External prerequisites -->

* **T810A-DEP-001 (Platform Capability)** — Availability of a multimodal LLM capable of processing text + images and maintaining in-session context.

* **T810A-DEP-002 (Long-term Analysis)** — The Epic requires a reporting feature to support cross-session summarization and pattern handoff. This requirement is fulfilled by `T810A3 (REPORT)`.

* **T810A-DEP-003 (Toolbox Interface)** — The Epic requires a centralized feature to manage custom tool interfaces and declarations. This requirement is fulfilled by `T810A4 (TOOLS)`. MVP tool usage deferral is governed by `T810A-CON-001`.

* **T810A-DEP-004 (Patient Data Structures)** — The Epic requires authoritative patient profile structure, schema definitions, and data validation governance. This requirement is fulfilled by `T810A2 (PATIENT)`, which establishes cross-feature schema consistency for the patient profile schema (stable patient context) and the tracking entry schemas (dynamic tracking entries).

* **T810A-DEP-005 (Clinical Safety Framework)** — Dependency on a clinical safety framework (red‑flag escalation, FDA SaMD, ISO 13485, HIPAA‑aligned handling) is deferred to future development. MVP approval requires explicit Client acknowledgment of this deferral per `T810A-CON-003`.

**Interfaces**

<!-- Governance-level role/process touchpoints -->

**Assumptions**
<!-- Unverified beliefs shaping scope/approach. -->

* **T810A-ASSUM-001 (Patient Profile)** — The patient has medium-to-high medical literacy, is engaged, and will provide detailed inputs.

* **T810A-ASSUM-002 (Input Modality & Quality)** — Inputs will be unstructured English text plus images; the patient is responsible for image quality and final classification confirmations when needed.

* **T810A-ASSUM-003 (LLM Capability)** — The platform provides state-of-the-art multimodal vision + reasoning sufficient for stool/meal image interpretation and complex text analysis.

* **T810A-ASSUM-004 (Platform Memory Uncertainty)** — ChatGPT's cross-session memory capability exists but its reliability, scope, and persistence are platform-dependent and not guaranteed. Features SHALL NOT rely solely on platform memory for critical data persistence or state management.

**Constraints**
<!-- Non-negotiable boundaries (compliance, timebox, architecture, tooling). -->

* **T810A-CON-001 (System Prompt Scope)** — The Epic deliverable is the LLM_Gastro system prompt. UI/UX, backend services, and database management are delegated to external platforms (ChatGPT native capabilities, user-managed applications). Support features (schemas, reports, tools) enable system prompt development; frontend and backend infrastructure are out of Epic scope.

* **T810A-CON-002 (Platform Compatibility)** — The system prompt must comply with ChatGPT's native governance. Do not override safety policies, refusal logic, or content restrictions; content must be additive and compatible. Document any conflicts as known limitations. Development must account for these constraints and minimize policy conflict risk.

* **T810A-CON-003 (Clinical Compliance Deferral)** — Clinical safety protocols (red‑flag escalation, FDA SaMD, ISO 13485, HIPAA‑aligned handling) are deferred to future development. MVP relies on ChatGPT's native safety per `T810A-CON-002`. Formal risk assessment, regulatory compliance, and validation will be addressed later. This is a scope deferral, not acceptance of clinical risk.

* **T810A-CON-004 (ChatGPT Architectural Constraints)** — The following constraints are imposed by the ChatGPT platform and MUST be accommodated via prompt engineering across all features:

  **File System Access**:
  - LLM_Gastro has **read-only** access to Knowledge Base files (patient profiles, templates, knowledge sources)
  - LLM_Gastro **cannot write** to files; profile updates require manual user intervention outside conversation
  - Generated outputs (tracking entry payloads, reports) are conversation-scoped, not persistent file writes

  **Validation Capability**:
  - No programmatic validation of JSON structure, field types, or value constraints
  - Value set enforcement MUST be implemented via Execution Protocol instructions and Exemplars
  - Risk of value drift over time without automated validation

  **Default Behavior Override**:
  - ChatGPT is designed by OpenAI as "helpful Assistant" with one-way interaction pattern (user asks → AI answers)
  - Consultant/Analyst mode (two-way Socratic dialogue) MUST be explicitly enforced via Role Identity, Execution Protocols, and Exemplars
  - Probe phase enforcement required to override default immediate-answer behavior

  **Model Selection**:
  - Users manually toggle between GPT thinking mode vs. auto mode (not controlled by system prompts)
  - System prompts MUST function correctly regardless of thinking mode setting

  These constraints shape Epic architecture decisions including the schema split architecture (patient profile schema vs tracking entry schemas), prompt-based validation patterns, probe enforcement mechanisms, and protocol triggering strategies.

**Implementation Guidance**
<!-- PURPOSE: Define epic-specific implementation patterns and technical conventions -->

* **T810A-IG-001 (Protocol Triggering Guidance)** — Features providing user interaction SHALL implement input type detection to determine appropriate response workflow per `T810A-QG-001`. Features MUST distinguish between:

  **Input Type Categories**:
  - **Data Capture Only**: User explicitly requests structured data entry/update without analysis (e.g., "just track this", "/log entry")
  - **Full Clinical Protocol**: User provides narrative content + context requiring analysis, pattern recognition, and guidance (default assumption for ambiguous input)
  - **Simple Q&A / Ad-hoc Query**: User asks isolated factual question not requiring full clinical workflow

  **Triggering Requirements**:
  - Features SHALL implement keyword/context detection for input classification
  - When input type is ambiguous, features SHALL default to **Full Clinical Protocol** to ensure comprehensive support
  - Explicit trigger commands (e.g., "/report", "/track-only") SHALL override automatic detection
  - Features MAY provide user education on trigger patterns to improve classification accuracy

  **Cross-Feature Application**:
  - **T810A1 (PROMPT)**: Implements 3-way detection (Tracking-Only / Full Protocol / Simple Q&A) per T810A1-NFR-008
  - **T810A3 (REPORT)**: Implements report generation trigger (e.g., "/report", "generate summary") per T810A1-IF-004
  - **Future Features**: Define own input categories aligned with feature-specific workflows

  Implementation details (keyword lists, detection logic, fallback behavior) are feature-defined.

* **T810A-IG-002 (Probe Phase Enforcement)** — Features providing clinical analysis and guidance SHALL implement mandatory clarification/probing loops before delivering coaching or recommendations per `T810A-QG-008` and `T810A-QG-001` .

  **Minimum Probing Requirements**:
  - Features SHALL ask **≥2 clarifying questions** per interaction when data is incomplete or ambiguous BEFORE providing guidance/recommendations
  - Clarifying questions SHALL focus on: missing mandatory data fields, ambiguous patient descriptions, temporal patterns, symptom-trigger correlations, contextual factors
  - Features SHALL use Socratic clinical inquiry (open-ended questions) NOT Assistant-style service offers (e.g., avoid "Would you like me to...")

  **Probe Question Patterns** (Epic-level examples):
  - **Missing Data**: "Can you describe what you felt immediately before [symptom] started?"
  - **Ambiguity**: "You mentioned 'typical pattern' — how many times per week does this occur?"
  - **Correlation**: "The meal included [ingredient] — have you noticed a pattern with this before?"
  - **Temporal Context**: "What time of day did this happen, and what had you eaten in the prior 6 hours?"

  **Probe-Before-Coach Enforcement**:
  - Features SHALL NOT execute coaching/guidance workflows until probing demonstrates sufficient data confidence
  - Minimum interaction loop: (1) Data capture → Analysis → Probe ≥2 questions; (2) Refined analysis with probe answers → Coach → Summarize
  - Features MAY implement adaptive probing (more questions if complexity high, fewer if confidence sufficient)

  **Cross-Feature Application**:
  - **T810A1 (PROMPT)**: Implements ≥2 questions minimum per T810A1-NFR-009 (Probe-Before-Answer Enforcement); embedded in 2-loop pattern
  - **T810A3 (REPORT)**: If interactive, implements clarification for ambiguous report parameters
  - **Non-Interactive Features** (A2, A4): Inherit principle but may not need explicit probing (no user dialogue)

  Implementation details (question templates, confidence thresholds, probe count adaptation logic) are feature-defined.

* **T810A-IG-003 (Explicit Classification)** — Features performing image classification, hypothesis generation, or diagnostic pattern recognition SHALL communicate results with explicit confidence indicators and user validation requests per `T810A-QG-007`.

  **Classification Communication Requirements**:
  - Features SHALL explicitly state any classification made (e.g., Bristol Stool Chart categorization, symptom pattern identification)
  - Classifications SHALL include concise rationale explaining basis for determination
  - Features SHALL provide **qualitative confidence indicator** using standardized descriptors: "high confidence", "moderate confidence", "fairly confident", "uncertain", "low confidence"
  - Numerical percentages (e.g., "85% confident") are prohibited per `T810A-QG-007`

  **User Validation Pattern**:
  - When confidence is **moderate or lower**, features SHALL encourage user validation using conversational phrasing
  - Validation requests SHALL NOT block conversational flow (embedded in natural dialogue, not blocking prompts)
  - Validation phrasing examples: "Does that match what you observed?", "Is this consistent with your experience?", "Would you describe it differently?"

  **Example Classification Pattern**:
  > "Based on the image, I'd classify this as **Bristol Stool Chart Type 4** (soft, smooth, snake-like consistency — generally considered ideal). I'm **fairly confident** in this assessment based on the texture and shape visible. Does that match what you observed?"

  **Cross-Feature Application**:
  - **T810A1 (PROMPT)**: Implements for Bristol Chart classification, symptom pattern hypotheses per T810A1-IF-003
  - **T810A3 (REPORT)**: Implements for pattern confidence in cross-session analysis (e.g., "moderate confidence this trigger pattern is significant")
  - **Future Features**: Apply to any classification/hypothesis generation task

  Implementation details (confidence threshold definitions, validation trigger logic, phrasing templates) are feature-defined.

* **T810A-IG-004 (Tracking Payload Per-Turn Delta)** — Features generating structured tracking data SHALL produce a per-turn delta payload (1+ entries) rather than cumulative logs.

  **Per-Turn Delta Requirements**:
  - When tracking output is required, features SHALL output exactly one fenced `json` codeblock containing the tracking payload
  - The tracking payload SHALL be a delta-only set of entries inferred from the current user message (no cumulative regeneration)
  - The tracking payload envelope SHALL follow `T810A-ADR-005` (Pattern A: mixed chronological array of entry objects)
  - Entries SHALL use schema-defined structure per `T810A2 (PATIENT)` authority (`T810A-DEP-004`)
  - Missing mandatory fields SHALL be handled via `null` values or field omission + probing per `T810A-IG-002`

  **Entry Presentation Pattern**:
  - Present structured tracking payload in a fenced `json` codeblock immediately after processing patient input
  - Use consistent schema adherence (field names, value sets defined by T810A2)
  - Entry serves dual purpose: user-facing confirmation + machine-readable log for aggregation

  **Aggregation Responsibility**:
  - **Session-scoped aggregation**: Individual features MAY maintain internal state for single-session context
  - **Cross-session aggregation**: Deferred to `T810A3 (REPORT)` per `T810A-DEP-002`
  - Features SHALL NOT attempt to maintain cumulative multi-entry logs within conversation

  **Cross-Feature Application**:
  - **T810A1 (PROMPT)**: Implements per-turn tracking payload delta (1+ entries) per T810A1-IF-006
  - **T810A3 (REPORT)**: Consumes entries from A1; performs aggregation, pattern analysis, cross-session summarization
  - **T810A2 (PATIENT)**: Defines authoritative schema for entry structure per `T810A-IG-004` governance

  Implementation details (entry type schemas, field definitions, value set vocabularies) are owned by `T810A2` per `T810A-DEP-004`.

* **T810A-IG-005 (Memory Review Protocol)** — Features with session-based interactions SHALL review ChatGPT's cross-session memory BEFORE executing main protocols.

  **Memory Review Requirements**:
  - Features SHALL implement **Step 0: Memory Review** as first step in session workflow
  - Review scope: ChatGPT persistent memory for relevant patient history, prior patterns, ongoing clinical concerns, recent changes
  - Identify discrepancies between cross-session memory and authoritative data sources (e.g., patient profile schema data)

  **Memory vs. Authoritative Data Conflict Resolution**:
  - **ChatGPT Memory**: Persistent across sessions, automatically updated by ChatGPT, unstructured narrative format
  - **Patient Profile Schema Data**: Manually updated by patient, structured, governance-controlled
  - **Precedence Rule**: When conflict exists, **patient profile data takes precedence** as single source of truth
  - Conflict handling: Flag discrepancy during interaction (e.g., "I notice in my memory you mentioned [X], but your profile shows [Y]. Has this changed?")

  **Session Workflow Integration**:
  - **Step 0**: Memory Review (scan persistent memory, identify discrepancies)
  - **Step 1**: Context Loading (load patient profile schema data + templates per `T810A-IG-006`)
  - **Step 2+**: Execute main protocol workflow

  **Cross-Feature Application**:
  - **T810A1 (PROMPT)**: Implements memory review before 5-phase protocol per T810A1-INT-005
  - **T810A3 (REPORT)**: Implements memory review before report generation (check for recent clinical updates)
  - **T810A2/A4**: Static artifacts (schemas, tools) — memory review not applicable

  Implementation details (memory query patterns, conflict detection logic, discrepancy phrasing) are feature-defined.

* **T810A-IG-006 (Session Context Handoff)** — Features with multi-session workflows SHALL implement context injection and handoff mechanisms.

  **Context Injection Requirements**:
  - At session start, features SHALL load prior session's clinical report/summary (if available) as context
  - Context injection enables multi-session continuity while maintaining token efficiency through daily report compression
  - Features SHALL treat injected reports as read-only reference (not re-editable historical data)

  **Handoff Report Generation** (per `T810A-DEP-002` collaboration with T810A3):
  - Features generating session-end reports SHALL produce **dual-format output**:
    1. **Chronological Timeline Narrative** (Markdown): First-person patient perspective (e.g., "08:00 - I had breakfast..."); serves as shareable clinician handoff document AND condensed LLM memory for next-session injection
    2. **Structured Log**: Machine-readable format suitable for aggregation by `T810A3 (REPORT)`; contains all tracking entries + session metadata

  **Report Trigger Pattern**:
  - Features SHALL implement explicit trigger command (e.g., "/report", "generate summary") per `T810A-IG-001`
  - On-demand generation (user-initiated, not automatic)
  - Report scope: single session or user-defined timeframe

  **Cross-Feature Integration**:
  - **T810A1 (PROMPT)**: Generates dual-format reports per T810A1-INT-002; loads previous report at session start per T810A1-IF-005
  - **T810A3 (REPORT)**: Consumes structured JSON logs from A1; performs cross-session aggregation, pattern analysis, long-term reporting
  - **Context Flow**: A1 generates report → A3 aggregates → A1 injects A3's summary at next session start (future state)

  Implementation details (narrative format, timeline structure, JSON schema) are feature-defined; coordination with T810A3 governed by `T810A-DEP-002`.

##### vii. Epic Research & Notes
<!-- PURPOSE: Provide background, drivers, and key research findings that inform this Epic's direction. -->

**Research**

| Research ID | Title | Summary | Linked To | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T810A-RES-001` | **System Architecture & Clinical Validation** | Industry validation of 9-block modular framework, multimodal trust-and-verify patterns, Analyze→Probe→Coach protocol enhancement, GI expert workflows, patient profile schema optimization, session workflow best practices, and dual-purpose clinical reporting architecture | `T810A`, `T810A1` | [brief](../research/brief/brief_prompt-architecture-clinical-validation_T810A.md) | [report](../research/report/report_prompt-architecture-clinical-validation_T810A.md) |
| `T810A-RES-002` | **Conversation-Driven Empirical Validation** | Real-world conversation analysis revealing 5 critical gaps: tracking-first protocol priority, schema split architecture (patient profile schema vs tracking entry schema), smart protocol triggering requirements, Probe phase absence, and ChatGPT memory review step | `T810A1`, `T810A2` | [conversation](../../resources/gastro_example_conversation.md) | [analysis](../plan/phase1.5_conversation_analysis.md) |

**Notes**

##### viii. Epic Governance Decisions

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| `T810A-GDR-001` | Trust-and-Verify Workflow Standard | Accepted | Client | 2025-10-27 | — | #t810a-gdr-001-trust-and-verify |
| `T810A-GDR-002` | Schema Split Architecture | Accepted | Client | 2025-10-27 | — | #t810a-gdr-002-data-schema-arch |
| `T810A-GDR-003` | Dual-Purpose Clinical Reporting | Accepted | Client | 2025-10-27 | — | #t810a-gdr-003-dual-purpose-reporting |
| `T810A-GDR-004` | GI Knowledge Base Sources | Accepted | Client | 2025-10-27 | — | #t810a-gdr-004-gi-knowledge-sources |

* **T810A-GDR-001 (Trust-and-Verify Workflow Standard)** {#t810a-gdr-001-trust-and-verify}

  **Context:** Per `T810A-RES-001` Deliverable B, confidence communication and user validation are essential for assessments requiring validation. Features risk overstating certainty or undermining reliability without explicit workflows.

  **Decision:** Features performing classifications SHALL: (1) communicate confidence qualitatively in user-facing prose, never numeric; (2) explain reasoning; (3) invite validation when uncertain; (4) adjust analysis per corrections. Adopt `T810A-ADR-001`, defining mandatory numeric thresholds for backend/JSON (0-1 range), qualitative tier mappings, and modality-specific examples.

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

* **T810A-GDR-002 (Schema Split Architecture)** {#t810a-gdr-002-data-schema-arch}

  **Context:** Per `T810A-RES-001` Deliverable E and `T810A-RES-002`, patient-governed vs. LLM-generated data require architectural separation. ChatGPT read-only constraint (`T810A-CON-004`) necessitates split architecture.

  **Decision:** Implement Schema Split Architecture separating (1) a **patient profile schema** (stable patient context, patient-managed, read-only for the agent, authority over Memory) from (2) a **tracking entry schema** (dynamic tracking entries emitted as a per-turn JSON payload per `T810A-IG-004` and `T810A-ADR-005`). `T810A2` owns schema definitions per `T810A-DEP-004`; `T810A3` owns aggregation per `T810A-DEP-002`; session loading is governed by `T810A-IG-005`/`T810A-IG-006`.
  Adopt `T810A-ADR-005`, defining the MVP per-turn tracking payload envelope (single fenced `json` codeblock containing a delta array of 1+ entry objects) to prevent multi-event data loss and cross-feature drift.

  **Consequences:**
  - (+) Accommodates platform constraint; token efficiency (patient profile loaded once/session; tracking entries emitted per interaction)
  - (±) Manual patient updates; Epic surface architecture with T810A2 schema details
  - (-) Staleness risk mitigated by `T810A-IG-005`

  **References:**
  `T810A-RES-001 (System Architecture & Clinical Validation)`,
  `T810A-IG-004 (Tracking Payload Per-Turn Delta)`,
  `T810A-ADR-005 (Tracking Payload Envelope)`,
  `T810A-IG-005 (Memory Review Protocol)`,
  `T810A-IG-006 (Session Context Injection & Handoff)`,
  `T810A-CON-004 (ChatGPT Architectural Constraints)`,
  `T810A-DEP-004 (Patient Data Structures)`,
  `T810A-DEP-002 (Long-term Analysis)`

* **T810A-GDR-003 (Dual-Purpose Clinical Reporting)** {#t810a-gdr-003-dual-purpose-reporting}

  **Context:** Per `T810A-RES-001` Deliverable F, chronological timeline in first-person patient perspective serves both clinician handoff and LLM memory. Separate formats would increase complexity and token overhead.

  **Decision:** Features generating session reports SHALL: (1) produce unified report for clinician review and LLM memory; (2) align structure/timing/export per `T810A-IG-006`; (3) integrate patient validation. Adopt `T810A-ADR-003`, defining voice (first-person), length (100-200 tokens), content patterns, triggers, validation, JSON export, A1/A3 coordination.

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

* **T810A-GDR-004 (GI Knowledge Base Sources)** {#t810a-gdr-004-gi-knowledge-sources}

  **Context:** Per `T810A-RES-001` Deliverable D, authoritative GI sources (ROME IV, Bristol Chart, ACG/AGA guidelines, alarm features) are essential for diagnostic reasoning and safety escalation. Without explicit catalog, features risk outdated/incomplete knowledge.

  **Decision:** Features requiring clinical GI knowledge SHALL: (1) ground reasoning in authoritative sources per `T810A-ADR-004`; (2) store references in designated knowledge storage; (3) frame hypotheses as "working theories for clinician discussion" per `T810A-CON-003`; (4) operate within constraints per `T810A-DEP-005`/`T810A-CON-002`. Adopt `T810A-ADR-004`, defining source catalog, versioning, update cadence, deprecation, maintenance governance.

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

##### ix. Epic Issues & Risks

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |


##### x. Epic Changelog
<!-- Lightweight audit trail for material changes within this Epic. -->

### D. Project Glossary
<!-- Define project-specific terms used in this SPS for clarity and consistency. -->

## IV. GLOSSARY
<!-- Global glossary or references shared across initiatives, if applicable. -->

---

## V. APPENDIX 

### A. Amendment Log
| Date | Change Requester | Affected Req. ID | Summary of Change |
| :--- | :--- | :--- | :--- |

---

## VI. VALIDATION CHECKLIST
<!-- Use as readiness gate before handoff. Keep criteria concise and verifiable. -->

- [ ] YAML header complete and correct
- [ ] Problem Definition (Section III-A) approved by decision owner
- [ ] Issues and Risks logged in Section III-B.9 and III-C.ix
- [ ] Next Steps clearly define handoff to downstream workflow

---

## VII. STAKEHOLDER SIGN-OFF
<!-- Formal approval section with names/dates for auditability. -->

---

## VIII. NEXT STEPS
<!-- Outline immediate next actions and handoff to downstream workflow (e.g., Request). Keep concise and actionable. -->

---

## IX. CHANGELOG
<!-- Brief audit trail of material changes to this artifact. Keep entries short with date/author/summary. -->
