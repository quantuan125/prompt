---
artifact_type: 'PROPOSAL'
initiative_id: 'T810'
epic_id: 'T810A'
version: '1.0.0'
date: '2025-10-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_document: 'plan_T810A-GASTRO_migration_v1.0.0.md'
target_section: 'Section 2 (Promotion Candidates)'
---

# PHASE 2: PROMOTION STRATEGY PROPOSALS (Feature → Epic)

## I. EXECUTIVE SUMMARY

This proposal presents the detailed architectural analysis and rationale for promoting Feature-level Requirements and Considerations (F-RIDs) from `T810A1 (PROMPT)` to Epic-level governance (E-RIDs) for `T810A (GASTRO)`. The promotion strategy addresses four primary RID categories (Assumptions, Dependencies, Constraints, Quality Goals) plus creation of new Implementation Guidance items to operationalize Epic-level quality standards.

### Key Findings

**Promotion Scope:**
- **Assumptions**: 4 promoted to Epic (3 direct, 1 hybrid split)
- **Dependencies**: 5 promoted to Epic (1 direct, 4 with rewording/fixes); 1 demoted to Feature-level
- **Constraints**: 4 promoted to Epic (2 direct, 2 with refinement); 1 reclassified to Quality Goal
- **Quality Goals**: 8 Epic QGs created (3 direct, 3 hybrid abstractions, 2 major enhancements)
- **Implementation Guidance**: 6 new Epic IGs created to operationalize QGs

**Strategic Patterns:**
- **Hybrid Approach**: Separates Epic-level governance principles from Feature-level implementation specifics (ASSUM-004, CON-004, QG-001, QG-002, QG-005)
- **Rewording for Clarity**: Dependencies reframed as requirements fulfilled by features rather than statements about feature existence
- **Category Reclassification**: CON-004 correctly reclassified from Constraint to Quality Goal based on testability
- **Epic IG Creation**: New Implementation Guidance category items synthesized from Feature-level Interface/Integration specifications to enable GDR de-referencing from F-RIDs

### Decision Patterns Applied

1. **Direct Promotion**: Items with clear Epic-wide applicability and no feature-specific content
2. **Promotion with Rewording**: Items requiring generalization or reference corrections for Epic scope
3. **Hybrid Split**: Items where governance principle applies Epic-wide but implementation details vary by feature
4. **Demotion to Feature**: Items specific to single feature's implementation needs
5. **Category Reclassification**: Items misclassified at Feature level, corrected during promotion

## II. SECTION 2.1: ASSUMPTIONS PROMOTION ANALYSIS

### Context

This section analyzes 4 Feature-level assumptions from `T810A1` for Epic promotion. Assumptions define foundational beliefs about the operating environment, user capabilities, and platform characteristics that must hold true for success.

### Promotion Decisions

#### ASSUM-001 (Patient Profile) — DIRECT PROMOTION

**Original T810A1 Content:**
"The patient has medium-to-high medical literacy, is engaged, and will provide detailed inputs."

**Promotion Decision:** ✅ **DIRECT PROMOTION** with ID change only

**Epic Scope Justification:**
This assumption applies to ALL features across the Epic:
- **T810A1 (PROMPT)**: Requires engaged patient for Socratic dialogue and detailed symptom narratives
- **T810A2 (PATIENT)**: Schemas assume patient provides detailed profile data with clinical accuracy
- **T810A3 (REPORT)**: Depends on patient reviewing and confirming generated reports
- **T810A4 (TOOLS)**: Assumes patient can interact with tool-driven workflows if implemented

The patient engagement and literacy assumption is foundational to the entire Epic's interaction model.

**Promoted E-RID:**
```markdown
**T810A-ASSUM-001 (Patient Profile)** — The patient has medium-to-high medical literacy, is engaged, and will provide detailed inputs.
```

**Action:** Promote as-is: `T810A1-ASSUM-001` → `T810A-ASSUM-001`

---

#### ASSUM-002 (Input Modality & Quality) — DIRECT PROMOTION

**Original T810A1 Content:**
"Inputs will be unstructured English text plus images; the patient is responsible for image quality and final classification confirmations when needed."

**Promotion Decision:** ✅ **DIRECT PROMOTION** with ID change only

**Epic Scope Justification:**
This assumption defines platform-level interaction modality across all features:
- **T810A1 (PROMPT)**: Processes text+images for clinical analysis
- **T810A2 (PATIENT)**: Schemas capture data from these text/image inputs
- **T810A3 (REPORT)**: Aggregates data originally sourced from text/images
- **Epic-Wide**: Image quality responsibility and classification confirmation apply to any feature handling visual data

The input modality and quality responsibility assumption is Epic-level platform constraint.

**Promoted E-RID:**
```markdown
**T810A-ASSUM-002 (Input Modality & Quality)** — Inputs will be unstructured English text plus images; the patient is responsible for image quality and final classification confirmations when needed.
```

**Action:** Promote as-is: `T810A1-ASSUM-002` → `T810A-ASSUM-002`

---

#### ASSUM-003 (LLM Capability) — DIRECT PROMOTION

**Original T810A1 Content:**
"The platform provides state-of-the-art multimodal vision + reasoning sufficient for stool/meal image interpretation and complex text analysis."

**Promotion Decision:** ✅ **DIRECT PROMOTION** with ID change only

**Epic Scope Justification:**
This assumption defines platform-level capability requirements for all features:
- **T810A1 (PROMPT)**: Requires multimodal LLM for image classification + clinical reasoning
- **T810A2 (PATIENT)**: Potentially relies on LLM for schema validation suggestions
- **T810A3 (REPORT)**: Requires LLM for pattern recognition across aggregated data
- **T810A4 (TOOLS)**: Requires LLM for tool selection/execution logic

All features depend on the LLM's multimodal capabilities as foundational platform assumption.

**Promoted E-RID:**
```markdown
**T810A-ASSUM-003 (LLM Capability)** — The platform provides state-of-the-art multimodal vision + reasoning sufficient for stool/meal image interpretation and complex text analysis.
```

**Action:** Promote as-is: `T810A1-ASSUM-003` → `T810A-ASSUM-003`

---

#### ASSUM-004 (Memory Model) — HYBRID SPLIT

**Original T810A1 Content:**
"Session-based memory is primary. Some cross-session/project memory may exist, but its effectiveness is unknown and not relied upon."

**Problem Identified:**
The current text is prompt-specific terminology:
- "Session-based" refers to conversational sessions in T810A1's context
- T810A2 (schemas) doesn't have conversational sessions
- T810A3 (reporting) handles cross-session aggregation, which contradicts "not relied upon"

**Promotion Decision:** ✅ **HYBRID SPLIT ADOPTED (Option C)**

**Rationale for Hybrid Approach:**
Separate Epic-level platform constraint (memory unreliability) from Feature-level implementation approach (how each feature addresses that constraint):
- ✅ Epic establishes platform constraint ALL features face (memory unreliability)
- ✅ Feature-level allows T810A1 to specify HOW it addresses that constraint (session-scoped approach)
- ✅ No over-prescription at Epic level; future features (A2/A3/A4) define their own memory management approaches
- ✅ Accommodates T810A3's cross-session aggregation needs without contradicting Epic assumption

**Epic-Level E-RID** (states platform constraint only):
```markdown
**T810A-ASSUM-004 (Platform Memory Uncertainty)** — ChatGPT's cross-session memory capability exists but its reliability, scope, and persistence are platform-dependent and not guaranteed. Features SHALL NOT rely solely on platform memory for critical data persistence or state management.
```

**Feature-Level F-RID** (T810A1 retains implementation-specific assumption):
```markdown
**T810A1-ASSUM-004 (Session-Scoped Memory Model)** — For conversational prompt features, session-based memory is the primary operational mode. Each conversation session is treated as independent; cross-session continuity is achieved via explicit report injection (per inherited `T810A-IG-006`) rather than relying on platform memory persistence.
```

**Implementation Impact:**
- Epic SPS gains 1 simplified platform constraint (T810A-ASSUM-004)
- T810A1 Request retains 1 feature-specific implementation assumption (T810A1-ASSUM-004)
- T810A1 Inherited Considerations table references Epic ASSUM-004; original A1-ASSUM-004 becomes feature delta

**Action:** Split: `T810A1-ASSUM-004` → `T810A-ASSUM-004` (Epic principle) + `T810A1-ASSUM-004` (Feature implementation)

### Promotion Summary

**Epic Assumptions Promoted:** 4 total
- **T810A-ASSUM-001** (Patient Profile) — direct promotion
- **T810A-ASSUM-002** (Input Modality & Quality) — direct promotion
- **T810A-ASSUM-003** (LLM Capability) — direct promotion
- **T810A-ASSUM-004** (Platform Memory Uncertainty) — hybrid split (Epic principle)

**T810A1 Feature Assumptions Retained:** 1 total
- **T810A1-ASSUM-004** (Session-Scoped Memory Model) — hybrid split (Feature implementation)

## III. SECTION 2.2: DEPENDENCIES PROMOTION ANALYSIS

### Context

This section analyzes 6 Feature-level dependencies from `T810A1` for Epic promotion. Dependencies identify external requirements or inter-feature relationships that must be satisfied for successful implementation.

### Promotion Decisions

#### DEP-001 (Platform) — DIRECT PROMOTION

**Original T810A1 Content:**
"Availability of a multimodal LLM capable of processing text + images and maintaining in-session context."

**Promotion Decision:** ✅ **DIRECT PROMOTION** with ID change only

**Epic Scope Justification:**
Platform-level dependency that ALL features share:
- **T810A1 (PROMPT)**: Needs multimodal LLM for prompt execution
- **T810A2 (PATIENT)**: Potentially relies on LLM for schema validation suggestions
- **T810A3 (REPORT)**: Requires LLM for pattern recognition across aggregated data
- **T810A4 (TOOLS)**: Requires LLM for tool selection/execution

**Promoted E-RID:**
```markdown
**T810A-DEP-001 (Platform)** — Availability of a multimodal LLM capable of processing text + images and maintaining in-session context.
```

**Action:** Promote as-is: `T810A1-DEP-001` → `T810A-DEP-001`

---

#### DEP-002 (Long-term Analysis) — DIRECT PROMOTION WITH REWORDING

**Original T810A1 Content:**
"Future feature `T810A3 (REPORT)` to support cross-session summarization and pattern handoff."

**Promotion Decision:** ✅ **DIRECT PROMOTION WITH REWORDING**

**Epic Scope Justification:**
Inter-feature dependency where multiple features require T810A3's capabilities:
- **T810A1 (PROMPT)**: Needs T810A3 for long-term pattern analysis
- **T810A2 (PATIENT)**: Schemas feed into T810A3 aggregation
- **T810A4 (TOOLS)**: Tools might generate reports via T810A3

**Rationale for Rewording:**
- Frames as Epic-level requirement (not just statement about feature existence)
- Clarifies T810A3 fulfills the requirement
- Avoids overlap with Feature Register

**Promoted E-RID:**
```markdown
**T810A-DEP-002 (Long-term Analysis)** — The Epic requires a reporting feature to support cross-session summarization and pattern handoff. This requirement is fulfilled by `T810A3 (REPORT)`.
```

**Action:** Promote with rewording: `T810A1-DEP-002` → `T810A-DEP-002`

---

#### DEP-003 (Toolbox Interface) — DIRECT PROMOTION WITH REWORDING

**Original T810A1 Content:**
"Future feature `T810A4 (TOOLS)` to track custom tool interfaces; deferral governed by `T810A1-CON-005`."

**Promotion Decision:** ✅ **DIRECT PROMOTION WITH REWORDING**

**Epic Scope Justification:**
Inter-feature dependency where custom tool integration is Epic-wide capability:
- **T810A1 (PROMPT)**: Defers tool declarations to T810A4
- **T810A2 (PATIENT)**: Might use tools for schema management
- **T810A3 (REPORT)**: Might use tools for advanced reporting
- **T810A4 (TOOLS)**: Serves as centralized tool registry

**Rationale for Rewording:**
- Frames as Epic-level requirement for centralized tool management
- Clarifies T810A4 fulfills requirement
- Updates CON-005 reference to Epic RID format (CON-001)

**Promoted E-RID:**
```markdown
**T810A-DEP-003 (Toolbox Interface)** — The Epic requires a centralized feature to manage custom tool interfaces and declarations. This requirement is fulfilled by `T810A4 (TOOLS)`. MVP tool usage deferral is governed by `T810A-CON-001` (System Prompt Scope).
```

**Action:** Promote with rewording: `T810A1-DEP-003` → `T810A-DEP-003`

---

#### DEP-004 (Patient Data Structures) — DIRECT PROMOTION WITH REWORDING

**Original T810A1 Content:**
"Patient profile structure, schema validation, and cross-session management are deferred to Feature `T810A2 (PATIENT)`. MVP allows JSON profile generation during reporting from conversation; formal schema, migration, and persistence are out of scope."

**Promotion Decision:** ✅ **DIRECT PROMOTION WITH REWORDING**

**Epic Scope Justification:**
Inter-feature dependency where T810A2 serves as Epic-level schema authority:
- **T810A1 (PROMPT)**: Uses schemas for Dynamic JSON generation
- **T810A3 (REPORT)**: Uses schemas for report structuring
- **T810A4 (TOOLS)**: Tools interact with schema-defined data structures
- **T810A2 (PATIENT)**: Governs schema consistency per `T810A-IG-004`

**Rationale for Rewording:**
- Frames as Epic-level requirement for schema governance
- Removes "deferred" language (T810A2 is part of same Epic)
- Clarifies T810A2's cross-feature authority role
- References GDR-003 for architectural context

**Promoted E-RID:**
```markdown
**T810A-DEP-004 (Patient Data Structures)** — The Epic requires authoritative patient profile structure, schema definitions, and data validation governance. This requirement is fulfilled by `T810A2 (PATIENT)`, which establishes cross-feature schema consistency for Stable JSON (patient profiles) and Dynamic JSON (tracking entries) per `T810A-GDR-003` (Stable/Dynamic JSON Architecture).
```

**Action:** Promote with rewording: `T810A1-DEP-004` → `T810A-DEP-004`

---

#### DEP-005 (Clinical Safety Framework) — DIRECT PROMOTION WITH REFERENCE FIX

**Original T810A1 Content:**
"Dependency on a clinical safety framework (red‑flag escalation, FDA SaMD, ISO 13485, HIPAA‑aligned handling) is deferred to future development. MVP approval requires explicit Client acknowledgment of this deferral per CON‑007."

**Promotion Decision:** ✅ **DIRECT PROMOTION WITH REFERENCE FIX**

**Epic Scope Justification:**
Epic-level scope deferral that applies to ALL features:
- Safety/regulatory compliance out of MVP scope for entire Epic
- All features (A1/A2/A3/A4) operate under this deferral
- No feature implements formal clinical safety framework in MVP
- Referenced by `T810A-CON-003`

**Rationale for Reference Fix:**
Corrects CON-007 reference to proper E-RID format (`T810A-CON-003` with backticks); establishes Epic-wide safety framework deferral as future work item.

**Promoted E-RID:**
```markdown
**T810A-DEP-005 (Clinical Safety Framework)** — Dependency on a clinical safety framework (red‑flag escalation, FDA SaMD, ISO 13485, HIPAA‑aligned handling) is deferred to future development. MVP approval requires explicit Client acknowledgment of this deferral per `T810A-CON-003` (Clinical Compliance Deferral).
```

**Action:** Promote with reference fix: `T810A1-DEP-005` → `T810A-DEP-005`

---

#### DEP-008 (Protocol Triggering Research) — DEMOTED TO FEATURE-LEVEL

**Original T810A1 Content:**
"Implementation of `T810A1-NFR-008` depends on research consultation to investigate VPA-style trigger condition + guard/gate patterns for clinical tracking use case. Research will inform S05 (Execution Protocol) development with validated prompt engineering techniques for input type detection, ChatGPT Assistant mode override strategies, and Probe phase enforcement mechanisms."

**Promotion Decision:** ✅ **DEMOTED TO FEATURE-LEVEL (Option B)**

**Rationale for Demotion:**
1. **Specificity**: Explicitly references T810A1-NFR-008 and "S05" (A1's Story 5), making it prompt-specific
2. **Uncertain Epic Applicability**: Only 1 of 4 features (A1) clearly needs this; T810A2 definitely doesn't; A3/A4 are uncertain ("maybe")
3. **Research Scope**: Research brief tailored to A1's conversational use case (input detection, Assistant mode override, Probe enforcement) — not generalizable to A3's reporting or A4's tools without separate research
4. **Feature Autonomy**: Allows A3/A4 to define their own triggering research needs if they emerge during development, rather than forcing them into A1's research paradigm

**Retained Feature Content:**
```markdown
**T810A1-DEP-008 (Protocol Triggering Research)** — Implementation of `T810A1-NFR-008` (protocol triggering guidance) depends on research consultation to investigate VPA-style trigger condition + guard/gate patterns for clinical tracking use case. Research will inform S05 (Execution Protocol) development with validated prompt engineering techniques for input type detection, ChatGPT Assistant mode override strategies, and Probe phase enforcement mechanisms.
```

**Action:** Retain as T810A1 feature-specific dependency (no promotion to Epic)

**Related Impact:**
ISSUE-002 (Protocol Triggering Logic Implementation) should also remain at T810A1 feature-level for consistency (tracks DEP-008 implementation).

### Promotion Summary

**Epic Dependencies Promoted:** 5 total
- **T810A-DEP-001** (Platform) — direct promotion
- **T810A-DEP-002** (Long-term Analysis) — direct promotion with rewording
- **T810A-DEP-003** (Toolbox Interface) — direct promotion with rewording
- **T810A-DEP-004** (Patient Data Structures) — direct promotion with rewording
- **T810A-DEP-005** (Clinical Safety Framework) — direct promotion with reference fix

**T810A1 Feature Dependencies Retained:** 1 total
- **T810A1-DEP-008** (Protocol Triggering Research) — demoted from Epic consideration

**Key Rewording Pattern:**
Dependencies DEP-002/003/004 reframed from statements ("Future feature X exists") to requirements ("Epic requires Y, fulfilled by Feature X") to clarify Epic-level requirements separate from Feature Register and remove "deferred" language, establishing T810A2/A3/A4 as Epic-level service providers.

## IV. SECTION 2.3: CONSTRAINTS PROMOTION ANALYSIS

### Context

This section analyzes 5 Feature-level constraints from `T810A1` for Epic promotion, plus 1 constraint (CON-004) identified for category reclassification. Constraints define external limitations or boundaries imposed by platform, compliance, or architectural decisions.

### Promotion Decisions

#### CON-001 (System Prompt Scope) — DIRECT PROMOTION WITH TITLE & CONTENT REFINEMENT

**Original T810A1 Content:**
- **Title**: "System Isolation"
- **Content**: "The deliverable is the system prompt only. No direct API integration with external applications (e.g., 'Care Care'); the user mediates data transfers. Frontend and backend are out of scope."

**Promotion Decision:** ✅ **DIRECT PROMOTION WITH TITLE & CONTENT REFINEMENT**

**Epic Scope Justification:**
Architectural boundary defining Epic deliverable vs. delegated capabilities:
- **T810A1 (PROMPT)**: Delivers the system prompt
- **T810A2/A3/A4**: Provide supporting artifacts (schemas, reporting templates, tool specifications) that enable prompt development
- **Delegated**: UI/UX, backend services, database management to external platforms (ChatGPT native capabilities, user-managed applications)

**Rationale for Title Change:**
"System Isolation" was A1-specific framing; "System Prompt Scope" clarifies Epic focuses on system prompt delivery, delegating infrastructure to external platforms.

**Rationale for Content Refinement:**
- Emphasize "LLM_Gastro system prompt" as Epic deliverable
- Remove "all features" language
- Add Future Consideration note per client guidance for prompt-based architecture permanence

**Promoted E-RID:**
```markdown
**T810A-CON-001 (System Prompt Scope)** — The Epic deliverable is the LLM_Gastro system prompt. UI/UX, backend services, and database management are delegated to external platforms (ChatGPT native capabilities, user-managed applications). Support features (schemas, reports, tools) enable system prompt development; frontend and backend infrastructure are out of Epic scope.

**Future Consideration**: This Epic architecture is prompt-based by design for the initiative lifecycle. Post-initiative evolution to UI/backend capabilities would require separate Epic planning and scope redefinition.
```

**Action:** Promote with title and content refinement: `T810A1-CON-001` → `T810A-CON-001`

---

#### CON-002 (Platform Compatibility) — DIRECT PROMOTION

**Original T810A1 Content:**
"**T810A1-CON-006 (Platform Compatibility)** — The system prompt must comply with ChatGPT's native governance. Do not override safety policies, refusal logic, or content restrictions; content must be additive and compatible. Document any conflicts as known limitations. Development must account for these constraints and minimize policy conflict risk."

**Promotion Decision:** ✅ **DIRECT PROMOTION** with ID change only

**Epic Scope Justification:**
Platform-level compliance constraint that ALL features share:
- All features operate on ChatGPT platform
- All must respect OpenAI governance
- Applies to A1 prompt, A2 schema instructions, A3 reporting logic, A4 tool declarations

**Promoted E-RID:**
```markdown
**T810A-CON-002 (Platform Compatibility)** — The system prompt must comply with ChatGPT's native governance. Do not override safety policies, refusal logic, or content restrictions; content must be additive and compatible. Document any conflicts as known limitations. Development must account for these constraints and minimize policy conflict risk.
```

**Action:** Promote as-is: `T810A1-CON-006` → `T810A-CON-002`

**Reference Impact:**
Referenced by `T810A-GDR-005` (GI Knowledge Base Sources); ensure GDR reference updated to E-RID format.

---

#### CON-003 (Clinical Compliance Deferral) — DIRECT PROMOTION

**Original T810A1 Content:**
"**T810A1-CON-007 (Clinical Compliance Deferral)** — Clinical safety protocols (red‑flag escalation, FDA SaMD, ISO 13485, HIPAA‑aligned handling) are deferred to future development. MVP relies on ChatGPT's native safety (see CON‑006). Formal risk assessment, regulatory compliance, and validation will be addressed later. This is a scope deferral, not acceptance of clinical risk."

**Promotion Decision:** ✅ **DIRECT PROMOTION** with ID change and reference update

**Epic Scope Justification:**
Epic-wide scope deferral that applies to ALL features:
- Regulatory/safety compliance out of MVP for entire Epic
- All features (A1/A2/A3/A4) operate under this deferral
- No feature implements formal clinical safety framework in MVP

**Promoted E-RID:**
```markdown
**T810A-CON-003 (Clinical Compliance Deferral)** — Clinical safety protocols (red‑flag escalation, FDA SaMD, ISO 13485, HIPAA‑aligned handling) are deferred to future development. MVP relies on ChatGPT's native safety (see `T810A-CON-002`). Formal risk assessment, regulatory compliance, and validation will be addressed later. This is a scope deferral, not acceptance of clinical risk.
```

**Action:** Promote with reference update: `T810A1-CON-007` → `T810A-CON-003`

**Cross-Reference Update:**
Internal reference "CON-006" updated to `T810A-CON-002` with backticks for formal reference syntax.

**Related Dependencies:**
Referenced by `T810A-DEP-005` (Clinical Safety Framework); both establish Epic-level safety deferral governance.

---

#### CON-004 (ChatGPT Architectural Constraints) — DIRECT PROMOTION WITH CONTENT REFINEMENT

**Original T810A1 Content:**
"**T810A1-CON-008 (ChatGPT Architectural Constraints)** — The following constraints are imposed by the ChatGPT platform and MUST be accommodated via prompt engineering: [details with Block 2/5/8 references, GDR-003/ISSUE-004 references]"

**Promotion Decision:** ✅ **DIRECT PROMOTION WITH CONTENT REFINEMENT**

**Epic Scope Justification:**
Platform-level technical constraints that ALL features face:
- **T810A1 (PROMPT)**: Read-only Knowledge Base access
- **T810A2 (PATIENT)**: Schema definitions can't write validation rules to files
- **T810A3 (REPORT)**: Reports are conversation outputs not file writes
- **T810A4 (TOOLS)**: Tool declarations must work within ChatGPT's Assistant mode

**Rationale for Content Refinement:**
1. Remove feature-specific references to "Block 2, Block 5, Block 8" (A1's 9-block structure)
2. Generalize to "Role Identity, Execution Protocols, Exemplars"
3. Maintain "LLM_Gastro" terminology per client approval (Initiative is T810-GASTRO)
4. **Remove precedence violations**: Delete `T810A-GDR-003` reference (E-RID cannot reference E-GDR per T102-STD-005-FR-003); delete `T810A-ISSUE-004` reference (E-RID cannot reference ISSUE); delete specific IG references to avoid circular dependencies
5. Generalize final sentence to describe architecture impacts without violating precedence rules

**Promoted E-RID:**
```markdown
**T810A-CON-004 (ChatGPT Architectural Constraints)** — The following constraints are imposed by the ChatGPT platform and MUST be accommodated via prompt engineering across all features:

**File System Access**:
- LLM_Gastro has **read-only** access to Knowledge Base files (patient profiles, templates, knowledge sources)
- LLM_Gastro **cannot write** to files; profile updates require manual user intervention outside conversation
- Generated outputs (Dynamic JSON, reports) are conversation-scoped, not persistent file writes

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

These constraints shape Epic architecture decisions including Stable/Dynamic JSON split, prompt-based validation patterns, probe enforcement mechanisms, and protocol triggering strategies.
```

**Action:** Promote with content refinement: `T810A1-CON-008` → `T810A-CON-004`

---

#### CON-004 (No-Guessing Principle) — RECLASSIFIED TO QUALITY GOAL + HYBRID SPLIT

**Original T810A1 Content:**
"**T810A1-CON-004 (No-Guessing Principle)** — When input is insufficient or unclear, the agent MUST NOT guess or hallucinate; it MUST default to Probe to request clarification."

**Category Reclassification Decision:** ✅ **HYBRID APPROACH ADOPTED**

**Rationale for Reclassification:**
- **Original Category**: CON (Constraint) — Incorrect; this is not an external limitation or boundary
- **Correct Category**: QG (Quality Goal) — Behavioral quality attribute that's testable and defines success criteria
- Mirrors ASSUM-004 hybrid pattern — separate governance principle (Epic QG) from implementation specifics (Feature NFR)

**Epic-Level QG** (high-level quality principle):
```markdown
**T810A-QG-008 (Clarification Over Guessing)** — User-facing features SHALL implement clarification mechanisms rather than guessing or hallucinating when input data is insufficient or ambiguous. Features MUST default to requesting additional information when confidence is low or context is unclear. Implementation patterns (probing loops, confirmation prompts, explicit uncertainty statements) are feature-defined based on interaction model.
```

**Feature-Level NFR** (T810A1 retains specific conversational implementation):
```markdown
**T810A1-NFR-009 (Probe-Before-Answer Enforcement)** — For conversational agent features, when input is insufficient or unclear, the agent MUST NOT guess or hallucinate; it MUST default to Probe phase to request clarification per inherited `T810A-QG-008` (Clarification Over Guessing). Minimum probing requirement: ≥2 clarifying questions before delivering coaching or guidance per `T810A-IG-002` (Probe Phase Enforcement).
```

**Scope Justification:**
- **Epic QG**: Applies to any user-facing feature (A1 conversational agent, A3 if interactive reporting, future features)
- **Feature NFR**: Specific to T810A1's conversational agent behavior (probe loops, ≥2 questions minimum)
- **A2/A4**: Not user-facing interactive features (static schemas/tool declarations) → inherit principle but may not need implementation

**Implementation Impact:**
- Epic SPS gains 1 Quality Goal (T810A-QG-008 Clarification Over Guessing)
- T810A1 Request retains 1 NFR (T810A1-NFR-009 Probe-Before-Answer Enforcement)
- T810A1 Inherited Considerations table references Epic QG-008

**Cross-Reference Updates:**
- GDR-001 (Tracking-First Clinical Protocol) → Update to cite `T810A-QG-008`
- IG-002 (Probe Phase Enforcement) operationalizes this QG → Establish cross-reference
- T810A1 Stories (S05 Execution Protocol) → Reference `T810A1-NFR-009`

**Action:** Reclassify and split: `T810A1-CON-004` → `T810A-QG-008` (Epic principle) + `T810A1-NFR-009` (Feature implementation)

---

#### Constraints NOT Promoted (Remain at T810A1 Feature Level)

**T810A1-CON-002 (Risk Acceptance)**
- Content: "The user accepts the inherent risks of AI-driven consultation."
- Rationale: Feature-specific user agreement; not Epic-level governance

**T810A1-CON-003 (Open Knowledge Base)**
- Content: "The agent may leverage its general training and permitted search tools to formulate hypotheses."
- Rationale: Covered by Epic GDR-005 (GI Knowledge Base Sources) and platform assumptions; redundant at Epic level

**T810A1-CON-005 (Tooling Deferral)**
- Content: "The MVP system prompt operates within ChatGPT's native tool ecosystem. Custom tool declarations are deferred to Feature T810A4."
- Rationale: Redundant with promoted `T810A-DEP-003` (Toolbox Interface dependency on T810A4) and `T810A-CON-001` (Prompt-Only MVP Scope); feature-specific implementation note

### Promotion Summary

**Epic Constraints Promoted:** 4 total
- **T810A-CON-001** (System Prompt Scope) — direct promotion with title/content refinement
- **T810A-CON-002** (Platform Compatibility) — direct promotion
- **T810A-CON-003** (Clinical Compliance Deferral) — direct promotion with reference update
- **T810A-CON-004** (ChatGPT Architectural Constraints) — direct promotion with content refinement

**Epic Quality Goals Created (from CON reclassification):** 1 total
- **T810A-QG-008** (Clarification Over Guessing) — created from CON-004 reclassification

**T810A1 Feature Constraints Retained:** 3 total
- **T810A1-CON-002** (Risk Acceptance) — not promoted
- **T810A1-CON-003** (Open Knowledge Base) — not promoted
- **T810A1-CON-004** (Tooling Deferral) — not promoted (redundant with Epic DEP-003/CON-001)

**T810A1 Feature NFRs Created:** 1 total
- **T810A1-NFR-009** (Probe-Before-Answer Enforcement) — created from CON-004 hybrid split

**Key Refinements:**
- **CON-001**: Title `System Isolation` → `System Prompt Scope`; added Future Consideration note
- **CON-003**: Updated internal reference "CON-006" → `T810A-CON-002`
- **CON-004**: Removed Block references, GDR/ISSUE references (precedence violations), generalized to Epic scope
- **Original CON-004**: Reclassified CON → QG; hybrid split into T810A-QG-008 (Epic) + T810A1-NFR-009 (Feature)

## V. SECTION 2.4: QUALITY GOALS PROMOTION ANALYSIS

### Context

This section analyzes 7 Feature-level NFRs (Non-Functional Requirements) from `T810A1` for promotion to Epic-level Quality Goals (QG). Quality Goals represent cross-feature success criteria that are testable and stable. Note: CON-004 reclassification (Section 2.3) created additional Epic QG-008.

### Promotion Decisions

#### QG-001 (Clinical Protocol Reliability) — HYBRID ABSTRACTION

**Original T810A1 Content:**
"**T810A1-NFR-001 (Protocol Reliability)** — The agent MUST consistently adhere to the **Tracking → Analyze → Probe → Coach → Summarize** protocol with the following priority hierarchy: [detailed 5-phase protocol with 2-loop pattern]"

**Issue Identified:**
The 5-phase protocol (Tracking → Analyze → Probe → Coach → Summarize) and "2-loop pattern" are T810A1-specific architectural choices.

**Scope Analysis:**
- **T810A1 (PROMPT)**: Conversational agent with 5-phase protocol → **YES, A1's implementation**
- **T810A2 (PATIENT)**: Static schema definitions; no protocol execution → **NO**
- **T810A3 (REPORT)**: Might have different workflow (aggregate → validate → format) → **UNCERTAIN, likely different**
- **T810A4 (TOOLS)**: Tool declarations; no execution protocol → **NO**

**Assessment:**
Only 1 of 4 features (T810A1) exhibits this 5-phase protocol. However, the **PRINCIPLE** (structured protocol with tracking-first, probe-before-coach hierarchy) is Epic-wide, captured by T810A-GDR-001 (Tracking-First Clinical Protocol).

**Promotion Decision:** ✅ **HYBRID APPROACH** — Abstracted Epic QG + Feature-specific NFR

**Epic-Level QG** (abstracted principle with research foundation):
```markdown
**T810A-QG-001 (Clinical Protocol Reliability)** — Features providing clinical interaction SHALL implement structured, repeatable protocols according to research on human expert practices in gastrointestinal and diet domains. Protocols SHALL prioritize data capture and analysis before guidance, ensure sufficient information gathering through probing/clarification loops, and maintain consistent execution across sessions. Protocol designs MUST be founded on industry-standard practices and validated methodologies from clinical gastroenterology and dietary management. Specific phase sequences, loop patterns, and implementation details are feature-defined.
```

**Feature-Level NFR** (T810A1 retains specific 5-phase implementation):
```markdown
**T810A1-NFR-001 (5-Phase Protocol Execution)** — The conversational agent SHALL consistently adhere to the **Tracking → Analyze → Probe → Coach → Summarize** protocol per inherited `T810A-QG-001` (Clinical Protocol Reliability) with the following priority hierarchy:
- **Primary (always execute)**: Tracking (structured data capture) + Analyze (pattern analysis)
- **Secondary (mandatory before coaching)**: Probe (≥2 clarifying questions per `T810A-QG-008` Clarification Over Guessing)
- **Tertiary (conditional)**: Coach + Summarize

Minimum 2-loop conversation pattern: Loop 1 (Tracking + Analyze + Probe, no coaching); Loop 2 (refined analysis + Coach + Summarize). Coach and Summarize SHALL NOT execute until Probe phase demonstrates sufficient data confidence.
```

**Action:** Create abstracted T810A-QG-001 + Retain T810A1-NFR-001 with inheritance reference

---

#### QG-002 (Persona & Tone) — HYBRID ABSTRACTION

**Original T810A1 Content:**
"**T810A1-NFR-002 (Persona & Tone)** — The agent's default mode is **Consultant/Analyst**, overriding ChatGPT's native Assistant behavior. Tone is adaptive across protocol phases: [6 specific phase tone mappings]"

**Promotion Decision:** ✅ **HYBRID APPROACH** per client feedback

**Epic Scope Justification:**
Cross-feature persona standard applies to ALL user-facing features:
- **T810A1 (PROMPT)**: Conversational agent uses Consultant/Analyst mode
- **T810A3 (REPORT)**: Reporting might use similar clinical tone
- Future features inherit this persona rather than ChatGPT's default Assistant mode

**Epic-Level QG** (general persona and tone principles):
```markdown
**T810A-QG-002 (Persona & Tone)** — User-facing features SHALL adopt **Consultant/Analyst** persona, overriding ChatGPT's native Assistant behavior. Tone is adaptive based on interaction type and clinical context: structured and precise for data capture, objective and evidence-based for analysis, collaborative and Socratic for clarification, empathetic for engagement, supportive and safety-bounded for guidance, clear and concise for summarization. Features SHALL prioritize clinical inquiry over helpfulness offers. Specific tone mappings for feature-specific interaction types are feature-defined.
```

**Feature-Level NFR** (T810A1 retains specific protocol phase tone mappings):
```markdown
**T810A1-NFR-002 (Protocol Phase Tone Mapping)** — The conversational agent SHALL apply adaptive tone per inherited `T810A-QG-002` (Persona & Tone) with the following protocol-specific mappings:
- **Tracking**: Structured, precise (Dynamic JSON generation with consistent schema adherence)
- **Analyze**: Clinical, objective, evidence-based (data-first presentation with explicit reasoning)
- **Probe**: Collaborative, inquisitive, Socratic (clarifying questions to fill data gaps)
- **Engage**: Empathetic, respectful (build rapport without over-promising)
- **Coach**: Supportive, safety-bounded (practical next steps with appropriate caution)
- **Summarize**: Clear, concise (confirm decisions and next actions)

The agent maintains partnership stance, treating the patient as expert in their lived experience. Clinical inquiry is prioritized over helpfulness offers (avoid Assistant-style "Would you like me to..." prompts).
```

**Action:** Create abstracted T810A-QG-002 + Retain T810A1-NFR-002 with protocol-specific tone mappings

---

#### QG-003 (Performance) — DIRECT PROMOTION

**Original T810A1 Content:**
"**T810A1-NFR-003 (Performance)** — Thoughtful responses are prioritized; 30–120 seconds latency is acceptable for consultant-level analysis."

**Promotion Decision:** ✅ **DIRECT PROMOTION** with ID change only

**Epic Scope Justification:**
Performance expectation applies to analysis-heavy features:
- **T810A1 (PROMPT)**: Clinical analysis requires thoughtful processing
- **T810A3 (REPORT)**: Cross-session pattern analysis requires thoughtful processing
- 30-120s latency standard applies Epic-wide for consultant-level work

**Promoted E-RID:**
```markdown
**T810A-QG-003 (Performance)** — Thoughtful responses are prioritized; 30–120 seconds latency is acceptable for consultant-level analysis.
```

**Action:** Promote as-is: `T810A1-NFR-003` → `T810A-QG-003`

---

#### QG-004 (Holistic Analysis) — DIRECT PROMOTION WITH CONTENT REFINEMENT

**Original T810A1 Content:**
"**T810A1-NFR-004 (Holistic Analysis)** — Analysis SHALL incorporate adjacent factors when present (stress, sleep, exercise) while focusing on gastroenterology/diet."

**Promotion Decision:** ✅ **DIRECT PROMOTION WITH CONTENT REFINEMENT**

**Epic Scope Justification:**
Cross-feature analytical principle:
- **T810A1 (PROMPT)**: Incorporates adjacent factors in clinical analysis
- **T810A3 (REPORT)**: Incorporates adjacent factors in pattern aggregation
- Holistic approach is Epic-level quality standard

**Content Refinement Needed:**
Clarify "Analysis" means general clinical analysis (not T810A1's specific "Analyze" protocol phase); expand to cover all analytical functions.

**Promoted E-RID:**
```markdown
**T810A-QG-004 (Holistic Analysis)** — Clinical analysis performed by features SHALL incorporate adjacent factors when present (stress, sleep, exercise, medications, lifestyle) while maintaining primary focus on gastroenterology and dietary patterns. Features providing analytical capabilities MUST consider multi-dimensional context rather than isolated symptom assessment. Holistic approach applies to all analytical functions (pattern recognition, hypothesis generation, trend analysis) across features.
```

**Action:** Promote with content refinement: `T810A1-NFR-004` → `T810A-QG-004`

---

#### QG-005 (Architecture Maintainability) — HYBRID ABSTRACTION

**Original T810A1 Content:**
"**T810A1-NFR-005 (Maintainability)** — The 9‑block modular prompt structure SHALL be strictly maintained."

**Issue Identified:**
"9-block" is T810A1's specific architecture. T810A2/A3/A4 won't have 9-block structures but should follow maintainability principles.

**Scope Analysis:**
- **T810A1**: 9-block prompt architecture → **YES, A1's implementation**
- **T810A2**: Schema files organization → **Different structure, same principle**
- **T810A3**: Reporting templates → **Different structure, same principle**
- **T810A4**: Tool declarations → **Different structure, same principle**

**Assessment:**
The PRINCIPLE (modular, maintainable architecture enabling independent updates) is Epic-wide; the IMPLEMENTATION (9-block structure) is A1-specific.

**Promotion Decision:** ✅ **HYBRID APPROACH** — Abstracted Epic QG + Feature-specific NFR

**Epic-Level QG** (abstracted principle):
```markdown
**T810A-QG-005 (Architecture Maintainability)** — Features SHALL adopt modular, well-documented architectures that enable independent updates to role definitions, knowledge sources, execution logic, and behavioral rules without cascading changes. Implementation patterns (block-based prompt structures, schema-driven definitions, template modularization) are feature-defined. Clear separation of concerns and explicit dependencies are required for sustainable evolution.
```

**Feature-Level NFR** (T810A1 retains 9-block specifics with framework reference):
```markdown
**T810A1-NFR-005 (9-Block Prompt Structure)** — The 9-block modular prompt structure SHALL be strictly maintained per inherited `T810A-QG-005` (Architecture Maintainability), following the compositional prompt framework defined in `prompt/documentation/prompt_main.md`: (1) Project Context, (2) Role Identity, (3) Toolbox, (4) Knowledge Base, (5) Execution Protocol, (6) Behavioral Guardrails, (7) Quality Criteria, (8) Exemplars, (9) I/O Specification. Each block enables independent updates without cascading modifications.
```

**Action:** Create abstracted T810A-QG-005 + Retain T810A1-NFR-005 with framework reference

---

#### QG-006 (Usability) — DIRECT PROMOTION WITH MAJOR CONTENT ENHANCEMENT

**Original T810A1 Content:**
"**T810A1-NFR-006 (Usability)** — Language and reasoning target a medium-to-high literacy user; avoid paternalistic tone."

**Promotion Decision:** ✅ **DIRECT PROMOTION WITH MAJOR CONTENT ENHANCEMENT**

**Epic Scope Justification:**
User expectation standard applies Epic-wide:
- **T810A1 (PROMPT)**: Conversational agent communication
- **T810A2 (PATIENT)**: Schema documentation
- **T810A3 (REPORT)**: Reports
- All target consistent literacy level and communication style

**Content Enhancement Needed** (per client feedback):
- Specify "medium literacy in gastrointestinal domain"
- Add plain language explanation requirement
- Emphasize patient education without overwhelm

**Promoted E-RID:**
```markdown
**T810A-QG-006 (Usability)** — Language and reasoning target a user with medium literacy in the gastrointestinal domain. Features SHALL present domain-specific clinical terminology alongside clear explanations in plain language for patient understanding. Communication MUST balance professional accuracy with accessibility:

- **Domain Language with Explanations**: Use clinical terminology (e.g., "Bristol Stool Chart Type 4", "malabsorption", "SIBO") but ALWAYS provide immediate plain-language explanations (e.g., "Bristol Type 4 means soft, smooth stool — considered ideal consistency")
- **Patient Education Priority**: Every complex concept from gastroenterology or dietetics MUST be explained in accessible terms without condescension
- **Cognitive Load Management**: Communication SHALL NOT overwhelm the patient; use progressive disclosure (explain foundational concepts before building to advanced patterns)
- **Non-Paternalistic Tone**: Avoid paternalistic language; maintain partnership stance respecting patient expertise in their lived experience

Features targeting technical audiences (e.g., schema documentation for developers) may adjust literacy level while maintaining clarity principles.
```

**Action:** Promote with major content enhancement: `T810A1-NFR-006` → `T810A-QG-006`

**Cross-Reference Note:**
This QG supports T810A-ASSUM-001 (Patient Profile assumption of engaged patient).

---

#### QG-007 (Confidence Communication) — DIRECT PROMOTION

**Original T810A1 Content:**
"**T810A1-NFR-007 (Confidence Communication)** — When classifying images or generating hypotheses, the agent SHALL communicate confidence using qualitative descriptors (e.g., 'fairly confident,' 'moderate confidence,' 'uncertain') rather than numerical percentages. Confidence indicators enable appropriate user validation without interrupting conversational flow."

**Promotion Decision:** ✅ **DIRECT PROMOTION** with ID change only

**Epic Scope Justification:**
Cross-feature quality standard for uncertainty communication:
- **T810A1 (PROMPT)**: Qualitative confidence for image classification and hypotheses
- **T810A3 (REPORT)**: Qualitative confidence for pattern confidence
- Any feature generating hypotheses should follow this standard

**Promoted E-RID:**
```markdown
**T810A-QG-007 (Confidence Communication)** — When classifying images or generating hypotheses, the agent SHALL communicate confidence using qualitative descriptors (e.g., 'fairly confident,' 'moderate confidence,' 'uncertain') rather than numerical percentages. Confidence indicators enable appropriate user validation without interrupting conversational flow.
```

**Action:** Promote as-is: `T810A1-NFR-007` → `T810A-QG-007`

**Cross-Reference Notes:**
- Operationalized by T810A-IG-003 (Explicit Classification)
- Supports T810A-GDR-002 (Trust-and-Verify Workflow Standard)

---

#### NFR-008 (Protocol Triggering Intelligence) — DEMOTED TO FEATURE-LEVEL

**Original T810A1 Content:**
"**T810A1-NFR-008 (Protocol Triggering Intelligence)** — The agent SHALL implement input type detection to determine appropriate response workflow: Tracking-Only Input, Full Protocol Input, Simple Q&A Input."

**Promotion Decision:** ✅ **DEMOTED TO FEATURE-LEVEL** (follows DEP-008 decision)

**Rationale:**
DEP-008 (Protocol Triggering Research) was demoted to T810A1 scope. NFR-008, which depends on DEP-008 research, should remain at T810A1 scope for consistency. Protocol triggering is A1-specific conversational agent concern (input type detection for different workflows); not applicable to A2 (schemas), A3 (reporting), A4 (tools).

**Action:** Retain as **T810A1-NFR-008** (no promotion to Epic)

---

#### NFR-009 (Probe Phase Enforcement) — SUPERSEDED BY CON-004 HYBRID RESOLUTION

**Original T810A1 Content:**
"**T810A1-NFR-009 (Probe Phase Enforcement)** — The agent SHALL treat Probe phase as **mandatory** before Coach phase execution: Ask ≥2 clarifying questions per full protocol execution."

**Status:**
NFR-009's intent is now captured by CON-004 hybrid resolution (Section 2.3):
- **Epic**: `T810A-QG-008` (Clarification Over Guessing) — principle of probing vs. guessing
- **Feature**: `T810A1-NFR-009` (Probe-Before-Answer Enforcement) — specific ≥2 questions requirement

**Action:** Original T810A1-NFR-009 replaced by new T810A1-NFR-009 (Probe-Before-Answer Enforcement) created from CON-004 hybrid split (see Section 2.3)

### Promotion Summary

**Epic Quality Goals Promoted/Created:** 8 total
- **T810A-QG-001** (Clinical Protocol Reliability) — hybrid abstraction from NFR-001
- **T810A-QG-002** (Persona & Tone) — hybrid abstraction from NFR-002
- **T810A-QG-003** (Performance) — direct promotion from NFR-003
- **T810A-QG-004** (Holistic Analysis) — direct promotion with content refinement from NFR-004
- **T810A-QG-005** (Architecture Maintainability) — hybrid abstraction from NFR-005
- **T810A-QG-006** (Usability) — direct promotion with major content enhancement from NFR-006
- **T810A-QG-007** (Confidence Communication) — direct promotion from NFR-007
- **T810A-QG-008** (Clarification Over Guessing) — created from CON-004 reclassification (Section 2.3)

**T810A1 Feature NFRs Retained/Created:** 5 total
- **T810A1-NFR-001** (5-Phase Protocol Execution) — hybrid from QG-001
- **T810A1-NFR-002** (Protocol Phase Tone Mapping) — hybrid from QG-002
- **T810A1-NFR-005** (9-Block Prompt Structure) — hybrid from QG-005
- **T810A1-NFR-008** (Protocol Triggering Intelligence) — retained (follows DEP-008 demotion)
- **T810A1-NFR-009** (Probe-Before-Answer Enforcement) — created from CON-004 hybrid (replaces original NFR-009)

**Key Abstractions:**
- **QG-001**: Added research foundation requirement; removed specific 5-phase protocol; generalized to "structured protocols with tracking-first, probe-before-coach hierarchy"
- **QG-002**: Epic has general interaction type tone principles; T810A1-NFR-002 retains specific protocol phase tone mappings
- **QG-004**: Clarified "Analysis" means general clinical analysis; expanded to cover all analytical functions
- **QG-005**: Title changed to "Architecture Maintainability"; removed "9-block"; generalized to "modular architectures"
- **QG-006**: Changed from "medium-to-high literacy" to "medium literacy in gastrointestinal domain"; added domain terminology WITH plain language explanations; added cognitive load management

**Cross-GDR Impact:**
- GDR-001 → Update to cite `T810A-QG-001` + `T810A-QG-008`
- GDR-002 → Update to cite `T810A-QG-007`
- GDR-004 → Update to cite `T810A-QG-002`
- GDR-006 → Update to cite `T810A-QG-002`

## VI. SECTION 2.5: IMPLEMENTATION GUIDANCE CREATION

### Context

This section documents creation of 6 NEW Epic Implementation Guidance (IG) items to operationalize Quality Goals and enable GDR de-referencing from F-RIDs. Per T102-STD-005, Implementation Guidance contains "normative authoring/process guidance" that features MUST follow. IGs prescribe HOW to achieve QG success criteria, focusing on cross-feature integrations with prescriptive patterns/thresholds.

### IG-to-QG Mapping Strategy

Each IG operationalizes specific QG(s), establishing clear "what → how" governance chain. IGs provide Epic-level prescriptive patterns with cross-feature applicability while deferring implementation specifics to Feature Requests.

### Implementation Guidance Items Created

#### IG-001 (Protocol Triggering Guidance) — NEW EPIC IG

**Related Quality Goal:** `T810A-QG-001` (Clinical Protocol Reliability)

**Purpose:** Establish Epic-level guidance for input type detection and appropriate workflow triggering across user-facing features.

**Source Mapping:** Synthesized from T810A1-NFR-008 (Protocol Triggering Intelligence) + T810A1-IF-004 (Reporting Trigger)

**Epic-Level IG Content:**
```markdown
**T810A-IG-001 (Protocol Triggering Guidance)** — Features providing user interaction SHALL implement input type detection to determine appropriate response workflow per `T810A-QG-001` (Clinical Protocol Reliability). Features MUST distinguish between:

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

Implementation details (keyword lists, detection logic, fallback behavior) are feature-defined per `T810A1-S05` (Execution Protocol).
```

**Scope Justification:** Input type detection applies to any user-facing feature with interactive workflows (A1 conversational agent, A3 if interactive reporting).

**Cross-Reference Notes:**
- Operationalizes `T810A-QG-001` (Clinical Protocol Reliability)
- Referenced by `T810A-GDR-001` (Tracking-First Clinical Protocol)
- Feature implementation: T810A1-NFR-008 (Protocol Triggering Intelligence)

---

#### IG-002 (Probe Phase Enforcement) — NEW EPIC IG

**Related Quality Goals:** `T810A-QG-008` (Clarification Over Guessing) + `T810A-QG-001` (Clinical Protocol Reliability)

**Purpose:** Establish Epic-level minimum probing requirements to ensure clarification before guidance.

**Source Mapping:** Synthesized from T810A1-NFR-009 (Probe Phase Enforcement) + T810A1-NFR-001 (minimum 2-loop pattern)

**Epic-Level IG Content:**
```markdown
**T810A-IG-002 (Probe Phase Enforcement)** — Features providing clinical analysis and guidance SHALL implement mandatory clarification/probing loops before delivering coaching or recommendations per `T810A-QG-008` (Clarification Over Guessing) and `T810A-QG-001` (Clinical Protocol Reliability).

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
```

**Scope Justification:** Probing requirement applies to any feature providing clinical analysis + guidance (A1 primary; A3 if interactive).

**Cross-Reference Notes:**
- Operationalizes `T810A-QG-008` (Clarification Over Guessing)
- Supports `T810A-QG-001` (Clinical Protocol Reliability)
- Referenced by `T810A-GDR-001` (Tracking-First Clinical Protocol)
- Feature implementation: T810A1-NFR-009 (Probe-Before-Answer Enforcement)

---

#### IG-003 (Explicit Classification) — NEW EPIC IG

**Related Quality Goal:** `T810A-QG-007` (Confidence Communication)

**Purpose:** Establish Epic-level pattern for communicating classifications/hypotheses with confidence indicators and validation requests.

**Source Mapping:** Synthesized from T810A1-IF-003 (Explicit Classification) + T810A1-NFR-007 (Confidence Communication)

**Epic-Level IG Content:**
```markdown
**T810A-IG-003 (Explicit Classification)** — Features performing image classification, hypothesis generation, or diagnostic pattern recognition SHALL communicate results with explicit confidence indicators and user validation requests per `T810A-QG-007` (Confidence Communication).

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
```

**Scope Justification:** Classification + confidence communication applies to any feature performing analysis with uncertainty (A1 image classification + hypotheses; A3 pattern analysis).

**Cross-Reference Notes:**
- Operationalizes `T810A-QG-007` (Confidence Communication)
- Supports `T810A-GDR-002` (Trust-and-Verify Workflow Standard)
- Feature implementation: T810A1-IF-003 (Explicit Classification)

---

#### IG-004 (Dynamic JSON Single-Entry Pattern) — NEW EPIC IG

**Related Quality Goal:** `T810A-QG-001` (Clinical Protocol Reliability) — structured data capture

**Purpose:** Establish Epic-level pattern for structured data generation to ensure consistency and prevent cumulative log errors.

**Source Mapping:** Synthesized from T810A1-IF-006 (Dynamic JSON Generation) + T810A1-INT-004 (Patient Data Architecture)

**Epic-Level IG Content:**
```markdown
**T810A-IG-004 (Dynamic JSON Single-Entry Pattern)** — Features generating structured tracking data SHALL produce **single entry per interaction** rather than cumulative logs.

**Single-Entry Requirements**:
- Features SHALL generate ONE structured entry per user interaction containing event-specific data
- Features SHALL NOT regenerate or aggregate previous entries (avoids cumulative errors, token bloat)
- Entries SHALL use schema-defined structure per `T810A2 (PATIENT)` authority (`T810A-DEP-004`)
- Missing mandatory fields SHALL be handled via `null` values or field omission + probing per `T810A-IG-002`

**Entry Presentation Pattern**:
- Present structured entry in fenced code block immediately after processing patient input
- Use consistent schema adherence (field names, value sets defined by T810A2)
- Entry serves dual purpose: user-facing confirmation + machine-readable log for aggregation

**Aggregation Responsibility**:
- **Session-scoped aggregation**: Individual features MAY maintain internal state for single-session context
- **Cross-session aggregation**: Deferred to `T810A3 (REPORT)` per `T810A-DEP-002`
- Features SHALL NOT attempt to maintain cumulative multi-entry logs within conversation

**Cross-Feature Application**:
- **T810A1 (PROMPT)**: Implements single Dynamic JSON entry per interaction per T810A1-IF-006
- **T810A3 (REPORT)**: Consumes entries from A1; performs aggregation, pattern analysis, cross-session summarization
- **T810A2 (PATIENT)**: Defines authoritative schema for entry structure per `T810A-IG-004` governance

Implementation details (entry type schemas, field definitions, value set vocabularies) are owned by `T810A2` per `T810A-DEP-004`.
```

**Scope Justification:** Single-entry pattern applies to any feature generating structured tracking data (A1 primary; potential future data capture features).

**Cross-Reference Notes:**
- Supports `T810A-QG-001` (Clinical Protocol Reliability)
- Implements `T810A-GDR-003` (Stable/Dynamic JSON Architecture)
- References `T810A-DEP-004` (Patient Data Structures)
- Feature implementation: T810A1-IF-006 (Dynamic JSON Generation)

---

#### IG-005 (Memory Review Protocol) — NEW EPIC IG

**Related Quality Goals:** `T810A-QG-001` (Clinical Protocol Reliability) — consistent session workflow

**Purpose:** Establish Epic-level pattern for reviewing cross-session memory before executing protocols to ensure context continuity.

**Source Mapping:** Synthesized from T810A1-INT-005 (Memory Review Protocol)

**Epic-Level IG Content:**
```markdown
**T810A-IG-005 (Memory Review Protocol)** — Features with session-based interactions SHALL review ChatGPT's cross-session memory BEFORE executing main protocols.

**Memory Review Requirements**:
- Features SHALL implement **Step 0: Memory Review** as first step in session workflow
- Review scope: ChatGPT persistent memory for relevant patient history, prior patterns, ongoing clinical concerns, recent changes
- Identify discrepancies between cross-session memory and authoritative data sources (e.g., Stable JSON patient profile)

**Memory vs. Authoritative Data Conflict Resolution**:
- **ChatGPT Memory**: Persistent across sessions, automatically updated by ChatGPT, unstructured narrative format
- **Stable JSON**: Manually updated by patient, structured format, governance-controlled
- **Precedence Rule**: When conflict exists, **Stable JSON takes precedence** as single source of truth
- Conflict handling: Flag discrepancy during interaction (e.g., "I notice in my memory you mentioned [X], but your profile shows [Y]. Has this changed?")

**Session Workflow Integration**:
- **Step 0**: Memory Review (scan persistent memory, identify discrepancies)
- **Step 1**: Context Loading (load Stable JSON, templates per `T810A-IG-006`)
- **Step 2+**: Execute main protocol workflow

**Cross-Feature Application**:
- **T810A1 (PROMPT)**: Implements memory review before 5-phase protocol per T810A1-INT-005
- **T810A3 (REPORT)**: Implements memory review before report generation (check for recent clinical updates)
- **T810A2/A4**: Static artifacts (schemas, tools) — memory review not applicable

Implementation details (memory query patterns, conflict detection logic, discrepancy phrasing) are feature-defined.
```

**Scope Justification:** Memory review applies to session-based interactive features (A1 primary; A3 if session-aware reporting).

**Cross-Reference Notes:**
- Supports `T810A-QG-001` (Clinical Protocol Reliability)
- Implements `T810A-GDR-004` (Session Workflow Architecture)
- References `T810A-GDR-003` (Stable/Dynamic JSON Architecture)
- Feature implementation: T810A1-INT-005 (Memory Review Protocol)

---

#### IG-006 (Session Context Injection & Handoff) — NEW EPIC IG

**Related Quality Goals:** `T810A-QG-001` (Clinical Protocol Reliability) — session continuity

**Purpose:** Establish Epic-level pattern for context injection and session handoff via condensed reports.

**Source Mapping:** Synthesized from T810A1-INT-002 (Memory Handoff Protocol) + T810A1-IF-005 (Session Context Injection)

**Epic-Level IG Content:**
```markdown
**T810A-IG-006 (Session Context Injection & Handoff)** — Features with multi-session workflows SHALL implement context injection and handoff mechanisms.

**Context Injection Requirements**:
- At session start, features SHALL load prior session's clinical report/summary (if available) as context
- Context injection enables multi-session continuity while maintaining token efficiency through daily report compression
- Features SHALL treat injected reports as read-only reference (not re-editable historical data)

**Handoff Report Generation** (per `T810A-DEP-002` collaboration with T810A3):
- Features generating session-end reports SHALL produce **dual-format output**:
  1. **Chronological Timeline Narrative** (Markdown): First-person patient perspective (e.g., "08:00 - I had breakfast..."); serves as shareable clinician handoff document AND condensed LLM memory for next-session injection
  2. **Structured JSON Log**: Machine-readable format suitable for aggregation by `T810A3 (REPORT)`; contains all Dynamic JSON entries + session metadata

**Report Trigger Pattern**:
- Features SHALL implement explicit trigger command (e.g., "/report", "generate summary") per `T810A-IG-001` (Protocol Triggering)
- On-demand generation (user-initiated, not automatic)
- Report scope: single session or user-defined timeframe

**Cross-Feature Integration**:
- **T810A1 (PROMPT)**: Generates dual-format reports per T810A1-INT-002; loads previous report at session start per T810A1-IF-005
- **T810A3 (REPORT)**: Consumes structured JSON logs from A1; performs cross-session aggregation, pattern analysis, long-term reporting
- **Context Flow**: A1 generates report → A3 aggregates → A1 injects A3's summary at next session start (future state)

Implementation details (narrative format, timeline structure, JSON schema) are feature-defined; coordination with T810A3 governed by `T810A-DEP-002`.
```

**Scope Justification:** Context injection + handoff applies to session-based features requiring continuity (A1 primary; A3 for cross-session reporting).

**Cross-Reference Notes:**
- Supports `T810A-QG-001` (Clinical Protocol Reliability)
- Implements `T810A-GDR-006` (Dual-Purpose Clinical Reporting)
- References `T810A-DEP-002` (Long-term Analysis)
- Feature implementations: T810A1-INT-002 (Memory Handoff), T810A1-IF-005 (Session Context Injection)

### Implementation Guidance Summary

**Epic Implementation Guidance Created:** 6 total NEW E-RIDs
- **T810A-IG-001** (Protocol Triggering Guidance) — operationalizes QG-001
- **T810A-IG-002** (Probe Phase Enforcement) — operationalizes QG-008 + QG-001
- **T810A-IG-003** (Explicit Classification) — operationalizes QG-007
- **T810A-IG-004** (Dynamic JSON Single-Entry Pattern) — operationalizes QG-001 + supports GDR-003
- **T810A-IG-005** (Memory Review Protocol) — operationalizes QG-001 + supports GDR-004
- **T810A-IG-006** (Session Context Injection & Handoff) — operationalizes QG-001 + supports GDR-006

**IG-to-QG Mapping Coverage:**
- **QG-001** (Clinical Protocol Reliability) — covered by IG-001, IG-002, IG-004, IG-005, IG-006 (primary QG)
- **QG-007** (Confidence Communication) — covered by IG-003
- **QG-008** (Clarification Over Guessing) — covered by IG-002
- **QG-002/003/004/005/006** — NOT covered by IG (inherent quality attributes vs. operational patterns)

**Rationale for Uncovered QGs:**
QG-002/003/004/005/006 are inherent quality attributes (tone, performance, analysis approach, architecture, communication style) that features implement directly without needing separate process guidance. IG category focuses on **operational patterns** (triggering, probing, classification, data generation, session management) that require cross-feature prescriptive guidance.

**Cross-GDR References Enabled:**
- GDR-001 → references IG-001 (triggering), IG-002 (probing)
- GDR-002 → references IG-003 (classification confidence)
- GDR-003 → references IG-004 (single-entry pattern)
- GDR-004 → references IG-005 (memory review)
- GDR-006 → references IG-006 (dual-format reporting)

**Feature Implementation Ownership:**
- IGs provide Epic-level prescriptive patterns with cross-feature applicability
- Feature Requests (T810A1, T810A2, T810A3, T810A4) own detailed implementation specifications
- T810A1 referenced as primary implementer for most IGs (conversational agent)
- T810A2 owns schema authority referenced by IG-004
- T810A3 owns aggregation/reporting referenced by IG-006

## VII. IMPLEMENTATION NOTES

### Cross-Reference Update Matrix

**Epic GDR Updates Required:**
- **GDR-001** (Tracking-First Clinical Protocol): Update references to cite `T810A-QG-001`, `T810A-QG-008`, `T810A-IG-001`, `T810A-IG-002`
- **GDR-002** (Trust-and-Verify Workflow Standard): Update references to cite `T810A-QG-007`, `T810A-IG-003`, `T810A-CON-004`
- **GDR-003** (Stable/Dynamic JSON Architecture): Update references to cite `T810A-CON-004`, `T810A-IG-004`
- **GDR-004** (Session Workflow Architecture): Update references to cite `T810A-QG-002`, `T810A-IG-005`
- **GDR-005** (GI Knowledge Base Sources): Update references to cite `T810A-CON-002`
- **GDR-006** (Dual-Purpose Clinical Reporting): Update references to cite `T810A-QG-002`, `T810A-IG-006`

**T810A1 Request Document Updates Required:**
- Update Inherited Considerations table to reference promoted Epic E-RIDs
- Add feature delta for retained F-RIDs (ASSUM-004, DEP-008, CON-002/003/005, NFR-001/002/005/008/009)
- Update all Epic RID references to proper backtick format per T102-STD-005

### Total E-RID Creation Summary

**Epic Assumptions:** 4
- T810A-ASSUM-001 through T810A-ASSUM-004

**Epic Dependencies:** 5
- T810A-DEP-001 through T810A-DEP-005

**Epic Constraints:** 4
- T810A-CON-001 through T810A-CON-004

**Epic Quality Goals:** 8
- T810A-QG-001 through T810A-QG-008

**Epic Implementation Guidance:** 6
- T810A-IG-001 through T810A-IG-006

**Total Epic E-RIDs Created:** 27

### Integration Points

**T810A1 ↔ T810A2 Integration:**
- T810A1 uses T810A2 schema authority for Dynamic JSON generation (via IG-004)
- T810A2 defines authoritative data structures (via DEP-004)

**T810A1 ↔ T810A3 Integration:**
- T810A1 generates dual-format reports consumed by T810A3 (via IG-006)
- T810A3 provides cross-session aggregation for T810A1 (via DEP-002)

**T810A1 ↔ T810A4 Integration:**
- T810A1 defers custom tool declarations to T810A4 (via DEP-003)
- T810A4 serves as centralized tool registry (via CON-001)

## VIII. CHANGELOG

- v1.0.0 (2025-10-23): Initial proposal documenting detailed architectural analysis and rationale for promoting Feature-level RIDs from T810A1 to Epic-level governance for T810A. Covers Assumptions (4 promoted), Dependencies (5 promoted, 1 demoted), Constraints (4 promoted, 1 reclassified to QG), Quality Goals (8 created), and Implementation Guidance (6 new IGs created). Establishes hybrid split patterns (ASSUM-004, CON-004→QG-008, QG-001, QG-002, QG-005) separating Epic governance principles from Feature implementation specifics.
