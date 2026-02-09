---
artifact_type: 'COMMUNICATION'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1'
feature_code: 'PROMPT'
version: '1.0.0'
date: '2025-10-28'
status: 'ready_for_handoff'
author: 'LLM_Consultant (Epic)'
decision_owner_role: 'Client'
target_consultant: 'LLM_Consultant (Sub-Consultant)'
source_epic: 'T810A-SYSTEM'
---

# HANDOFF BRIEF: T810A1-PROMPT Epic Changes Integration (Phases 2/3/4)

## I. EXECUTIVE SUMMARY

This handoff brief communicates comprehensive Epic-level changes from **Phases 2, 3, and 4** of T810A Epic population migration to the **T810A1-PROMPT** subconsultant for integration into the Feature Request document (`request_T810A1-PROMPT.md`).

**Critical Context**: Epic T810A migration analysis revealed that significant portions of T810A1 Request content should be elevated to Epic scope OR demoted from incorrectly-scoped Epic items. This brief ensures T810A1 receives all changes for proper Request document updates.

**Parallel Development Model**: T810A1 updates can proceed in parallel with Phase 6 (Epic Holistic Migration Review). Epic governance is now stable after Phases 2-4; T810A1 integration is non-blocking for Epic finalization.

**Expected Actions**: Update T810A1 Request document with:
1. Section restructuring: Split current Section III.E into two sections (Inherited Considerations + Assumptions & Dependencies)
2. Inherited Considerations Table (27 Epic E-RIDs grouped by category)
3. Feature Governance Decisions (2 GDRs demoted from Epic)
4. F-RID renumbering and content removal for promoted items
5. F-RID→E-RID reference updates throughout Request (especially S05 Execution Protocol)

---

## I-A. REQUIRED PRE-IMPLEMENTATION REVIEW

**CRITICAL**: Before implementing changes in this handoff brief, the T810A1 subconsultant MUST review the following materials to understand the full context of Epic migration decisions:

### A. Core Governance Documents
1. **Epic SPS**: `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md`
   - **Purpose**: Authoritative source for all 27 Epic E-RID definitions (ASSUM, DEP, CON, QG, IG)
   - **Usage**: Reference when understanding Epic requirement content and Application Notes

2. **Migration Plan**: `prompt/artifacts/tasks/T810/consultant/workspace/plan/T810A/plan_T810A-SYSTEM_migration.md`
   - **Purpose**: Full context of Phase 2/3/4 Epic migration strategy and decision rationale
   - **Usage**: Understand why specific items were promoted/demoted/retained

3. **Delta Analysis Proposal**: `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/proposal_T810A-SYSTEM_phase5.md`
   - **Purpose**: Detailed F-RID→E-RID mapping analysis; placement guidance; content distribution (47%/53%)
   - **Usage**: Reference for implementation details not fully documented in this brief

### B. ID Specification Standards
4. **T102-STD-004** (Decision Records Index): Format standards for GDRs/ADRs
   - **Location**:   `prompt\artifacts\tasks\T102\consultant\concept\concept_T102-CONSULTANT.md`
   - **Usage**: Validate GDR body format compliance (Context, Decision, Consequences, References)

5. **T102-STD-005** (ID Specification & Rules): Scope IDs, precedence hierarchy, reference syntax
   - **Location**: `prompt\artifacts\tasks\T102\consultant\concept\concept_T102-CONSULTANT.md`
   - **Usage**: Validate E-RID references use formal syntax; understand inheritance rules

### C. Current T810A1 Baseline
6. **T810A1 Request (baseline)**: `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md`
   - **Purpose**: Current Feature Request structure (pre-migration)
   - **Usage**: Understand current organization before applying structural changes

**Review Completion Checkpoint**: Confirm understanding of (1) Epic E-RID content, (2) promotion rationale, (3) inheritance patterns, (4) GDR/ADR format standards, (5) RID reference syntax before proceeding to implementation.

---

## II. PHASE 2 CHANGES: E-RID PROMOTION (27 EPIC REQUIREMENTS)

### A. Overview

**Decision**: 27 Feature-level RIDs promoted from T810A1 to Epic T810A scope (cross-feature applicability validated).

**Categories Promoted**:
| Category | Count | IDs |
|:---------|:------|:----|
| **Assumptions** | 4 | T810A-ASSUM-001 through ASSUM-004 |
| **Dependencies** | 5 | T810A-DEP-001 through DEP-005 |
| **Constraints** | 4 | T810A-CON-001 through CON-004 |
| **Quality Goals** | 8 | T810A-QG-001 through QG-008 |
| **Implementation Guidance** | 6 | T810A-IG-001 through IG-006 |

**Impact on T810A1**: These 27 items must now be **inherited** (not duplicated) in T810A1 Request per T102-STD-003 (ID Specification & Rules).

---

### B. Detailed ID Migration Mapping

**Assumptions** (4 promoted):
1. `T810A1-ASSUM-001` → `T810A-ASSUM-001` (Patient Profile) [Direct promotion]
2. `T810A1-ASSUM-002` → `T810A-ASSUM-002` (Input Modality & Quality) [Direct promotion]
3. `T810A1-ASSUM-003` → `T810A-ASSUM-003` (LLM Capability) [Direct promotion]
4. `T810A1-ASSUM-004` → `T810A-ASSUM-004` (Platform Memory Uncertainty) [Hybrid - Epic principle extracted]
   - **Note**: T810A1-ASSUM-004 retained at Feature level with implementation-specific content (Session-Scoped Memory Model)

**Dependencies** (5 promoted):
1. `T810A1-DEP-001` → `T810A-DEP-001` (Platform) [Direct promotion]
2. `T810A1-DEP-002` → `T810A-DEP-002` (Long-term Analysis) [Rewording for Epic abstraction]
3. `T810A1-DEP-003` → `T810A-DEP-003` (Toolbox Interface) [Rewording for Epic abstraction]
4. `T810A1-DEP-004` → `T810A-DEP-004` (Patient Data Structures) [Rewording for Epic abstraction]
5. `T810A1-DEP-005` → `T810A-DEP-005` (Clinical Safety Framework) [Reference fix]
   - **Demoted**: T810A1-DEP-008 (Protocol Triggering Research) [Retained at Feature - not promoted]

**Constraints** (4 promoted):
1. `T810A1-CON-001` → `T810A-CON-001` (System Prompt Scope) [Title + content refinement]
2. `T810A1-CON-006` → `T810A-CON-002` (Platform Compatibility) [Direct promotion]
3. `T810A1-CON-007` → `T810A-CON-003` (Clinical Compliance Deferral) [Reference update]
4. `T810A1-CON-008` → `T810A-CON-004` (ChatGPT Architectural Constraints) [Content refinement]
   - **Reclassified**: T810A1-CON-004 → T810A-QG-008 (Clarification Over Guessing) [CON → QG reclassification]
   - **Retained**: T810A1-CON-002, CON-003, CON-005 [Feature-specific; not promoted]

**Quality Goals** (8 promoted):
1. `T810A1-NFR-001` → `T810A-QG-001` (Clinical Protocol Reliability) [Hybrid - Epic abstraction]
2. `T810A1-NFR-002` → `T810A-QG-002` (Persona & Tone) [Hybrid - Epic abstraction]
3. `T810A1-NFR-003` → `T810A-QG-003` (Performance) [Direct promotion]
4. `T810A1-NFR-004` → `T810A-QG-004` (Holistic Analysis) [Content refinement]
5. `T810A1-NFR-005` → `T810A-QG-005` (Architecture Maintainability) [Hybrid - Epic abstraction]
6. `T810A1-NFR-006` → `T810A-QG-006` (Usability) [Major content enhancement]
7. `T810A1-NFR-007` → `T810A-QG-007` (Confidence Communication) [Direct promotion]
8. `T810A1-CON-004` → `T810A-QG-008` (Clarification Over Guessing) [CON → QG reclassification]
   - **Hybrid Retention**: T810A1-NFR-001, NFR-002, NFR-005 [Feature implementation details retained]
   - **Demoted**: T810A1-NFR-008 (Protocol Triggering Intelligence) [Retained at Feature - not promoted]

**Implementation Guidance** (6 NEW Epic IGs synthesized):
1. `T810A-IG-001` (Protocol Triggering Guidance) [Synthesized from T810A1-NFR-008, T810A1-IF-004]
2. `T810A-IG-002` (Probe Phase Enforcement) [Synthesized from T810A1-NFR-009, T810A1-NFR-001]
3. `T810A-IG-003` (Explicit Classification) [Synthesized from T810A1-IF-003, T810A1-NFR-007]
4. `T810A-IG-004` (Dynamic JSON Single-Entry Pattern) [Synthesized from T810A1-IF-006, T810A1-INT-004]
5. `T810A-IG-005` (Memory Review Protocol) [Synthesized from T810A1-INT-005]
6. `T810A-IG-006` (Session Context Injection & Handoff) [Synthesized from T810A1-INT-002, T810A1-IF-005]

---

### C. T810A1 Integration Requirements (Phase 2)

**Required Action 1: Section Restructuring & Inherited Considerations Table**

**CRITICAL**: Current **Section III.E (Inheritances, Assumptions & Dependencies)** must be **SPLIT** into TWO separate sections:

1. **NEW Section III.E**: Inherited Considerations (table only — lists all 27 Epic E-RIDs)
2. **NEW Section III.F**: Assumptions & Dependencies (feature-specific F-RIDs only)

**Current Section III.E Structure** (baseline):
```markdown
### E. Inheritences, Assumptions & Dependencies

* **Inherited Considerations**
[Current 2-row table with Research + Governances categories]

**Assumptions**
* T810A1-ASSUM-001 (Patient Profile)
* T810A1-ASSUM-002 (Input Modality & Quality)
* T810A1-ASSUM-003 (LLM Capability)
* T810A1-ASSUM-004 (Memory Model)

**Dependencies**
* T810A1-DEP-001 (Platform)
* T810A1-DEP-002 (Long-term Analysis)
* T810A1-DEP-003 (Toolbox Interface)
* T810A1-DEP-004 (Patient Profile)
* T810A1-DEP-005 (Clinical Safety Framework)
* T810A1-DEP-008 (Protocol Triggering Research)
```

**POST-MIGRATION Structure** (target):

**Section III.E: Inherited Considerations** (NEW — table only)
- **Placement**: After Section III.D (Stakeholders)
- **Content**: 27 Epic E-RIDs grouped by category (Assumptions, Dependencies, Constraints, Quality Goals, Implementation Guidance)
- **Table format**: `Source Artifact | Source ID | Category | Inherited Rule IDs` (matches existing Request exemplar)

**Section III.F: Assumptions & Dependencies** (NEW name — feature-specific only)
- **Placement**: After new Section III.E
- **Content**: ONLY feature-specific items (T810A1-ASSUM-004, T810A1-DEP-008)
- **DELETE from this section**: T810A1-ASSUM-001/002/003, T810A1-DEP-001/002/003/004/005 (now inherited via Section III.E table)

**Impact**: All subsequent sections renumber:
- Current Section III.F → New Section III.G
- Current Section III.G → New Section III.H
- Current Section III.H → New Section III.I
- Current Section III.I → New Section III.J
- Current Section III.J → New Section III.K (continue cascade through remaining sections)

---

**Inherited Considerations Table Template**:

```markdown
### E. Inherited Considerations

This Feature inherits the following Epic-level Requirements and Considerations from `T810A-SYSTEM`. These E-RIDs apply cross-feature and are defined in the Epic SPS.

| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :--- | :--- | :--- | :--- |
| SPS | `T810A` | Assumptions | `T810A-ASSUM-001 (Patient Profile)`, `T810A-ASSUM-002 (Input Modality & Quality)`, `T810A-ASSUM-003 (LLM Capability)`, `T810A-ASSUM-004 (Platform Memory Uncertainty)` |
| SPS | `T810A` | Dependencies | `T810A-DEP-001 (Platform Capability)`, `T810A-DEP-002 (Long-term Analysis)`, `T810A-DEP-003 (Toolbox Interface)`, `T810A-DEP-004 (Patient Data Structures)`, `T810A-DEP-005 (Clinical Safety Framework)` |
| SPS | `T810A` | Constraints | `T810A-CON-001 (System Prompt Scope)`, `T810A-CON-002 (Platform Compatibility)`, `T810A-CON-003 (Clinical Compliance Deferral)`, `T810A-CON-004 (ChatGPT Architectural Constraints)` |
| SPS | `T810A` | Quality Goals | `T810A-QG-001 (Clinical Protocol Reliability)`, `T810A-QG-002 (Persona & Tone)`, `T810A-QG-003 (Analysis Performance)`, `T810A-QG-004 (Holistic Analysis)`, `T810A-QG-005 (Architecture Maintainability)`, `T810A-QG-006 (Usability)`, `T810A-QG-007 (Confidence Communication)`, `T810A-QG-008 (Clarification Over Guessing)` |
| SPS | `T810A` | Implementation Guidance | `T810A-IG-001 (Protocol Triggering Guidance)`, `T810A-IG-002 (Probe Phase Enforcement)`, `T810A-IG-003 (Explicit Classification)`, `T810A-IG-004 (Dynamic JSON Single-Entry Pattern)`, `T810A-IG-005 (Memory Review Protocol)`, `T810A-IG-006 (Session Context Injection & Handoff)` |
| SPS | `T810A` | Governance | `T810A-GDR-002 (Schema Split Architecture)`, `T810A-GDR-003 (Dual-Purpose Clinical Reporting)`, `T810A-GDR-004 (GI Knowledge Base Sources)` |
| SPS | `T810A` | Research | `T810A-RES-001 (System Architecture & Clinical Validation)`, `T810A-RES-002 (Conversation-Driven Empirical Validation)` |
| CONCEPT | `T810A` | Architecture | `T810A-ADR-001 (Trust-and-Verify Confidence Policy)`, `T810A-ADR-003 (Dual-Purpose Reporting Policy)`, `T810A-ADR-004 (GI Knowledge Sources Catalog)` |
```

**Note**: Feature-specific implementation details for these E-RIDs are documented in T810A1 Sections III.F-K (Assumptions/Dependencies, NFRs, Interfaces, Constraints, Integration Notes, Stories).

**Required Action 2: Update F-RID References to E-RID References**

Replace promoted F-RID citations with E-RID references throughout T810A1 Request.

**Example Replacements**:
- `T810A1-NFR-007` → `T810A-QG-007` (Confidence Communication)
- `T810A1-CON-008` → `T810A-CON-004` (ChatGPT Architectural Constraints)
- `T810A1-INT-005` → `T810A-IG-005` (Memory Review Protocol)
- `T810A1-INT-002` → `T810A-IG-006` (Session Context Injection & Handoff)

**Required Action 3: Feature-Specific Content Cleanup & RID Renumbering**

**CRITICAL**: After deleting promoted F-RIDs from feature-specific sections, ALL retained F-RIDs MUST be renumbered to start from `001` in sequential order within each section.

**Section-by-Section Cleanup Instructions**:

**3.1. Section III.F: Assumptions & Dependencies** (was Section III.E)

**DELETE** (promoted to Epic):
- Remove entire content blocks for: T810A1-ASSUM-001, ASSUM-002, ASSUM-003
- Remove entire content blocks for: T810A1-DEP-001, DEP-002, DEP-003, DEP-004, DEP-005

**RETAIN & RENUMBER**:
- T810A1-ASSUM-004 (Session-Scoped Memory Model) → **Renumber to T810A1-ASSUM-001**
  - **Location**: Under "**Assumptions**" subsection heading
  - **Rationale**: Hybrid implementation (Epic principle + Feature specifics)

- T810A1-DEP-008 (Protocol Triggering Research) → **Renumber to T810A1-DEP-001**
  - **Location**: Under "**Dependencies**" subsection heading
  - **Rationale**: Feature-specific research dependency

---

**3.2. Section III.G: Non-Functional Requirements** (was Section III.F)

**DELETE** (promoted to Epic QGs):
- Remove entire content blocks for: T810A1-NFR-003, NFR-004, NFR-006, NFR-007

**RETAIN & RENUMBER**:
- T810A1-NFR-001 (Protocol Reliability) → **Renumber to T810A1-NFR-001** (no change)
  - **Rationale**: Hybrid (Epic QG-001 principle + Feature 5-phase implementation)

- T810A1-NFR-002 (Persona & Tone) → **Renumber to T810A1-NFR-002** (no change)
  - **Rationale**: Hybrid (Epic QG-002 principle + Feature tone mapping)

- T810A1-NFR-005 (Maintainability) → **Renumber to T810A1-NFR-003**
  - **Rationale**: Hybrid (Epic QG-005 principle + Feature 9-block structure)

- T810A1-NFR-008 (Protocol Triggering Intelligence) → **Renumber to T810A1-NFR-004**
  - **Rationale**: Feature-specific implementation of Epic IG-001

- T810A1-NFR-009 (Probe Phase Enforcement) → **Renumber to T810A1-NFR-005**
  - **Rationale**: Feature-specific implementation of Epic QG-008 + IG-002

**Cross-Reference Updates Required**: After renumbering NFR-005 → NFR-003, NFR-008 → NFR-004, NFR-009 → NFR-005, update ALL references throughout Request (especially in Stories S01-S09, Interfaces, Integration Notes).

---

**3.3. Section III.I: Constraints** (was Section III.H)

**DELETE** (promoted to Epic):
- Remove entire content blocks for: T810A1-CON-001, CON-004, CON-006, CON-007, CON-008

**RETAIN & RENUMBER**:
- T810A1-CON-002 (Risk Acceptance) → **Renumber to T810A1-CON-001**
  - **Rationale**: Feature-specific user agreement statement

- T810A1-CON-003 (Open Knowledge Base) → **Renumber to T810A1-CON-002**
  - **Rationale**: Feature-specific implementation detail

- T810A1-CON-005 (Tooling Deferral) → **Renumber to T810A1-CON-003**
  - **Rationale**: Feature-specific MVP constraint

---

**3.4. Section III.H: Interfaces & Data** (was Section III.G)

**RETAIN ALL** (no deletions):
- T810A1-IF-001 through IF-006 → **No renumbering required** (all feature-specific)

**UPDATE descriptions**: Add explicit Epic IG references:
- T810A1-IF-003: Add reference to `T810A-IG-003` (Explicit Classification)
- T810A1-IF-004: Add reference to `T810A-IG-001` (Protocol Triggering Guidance)
- T810A1-IF-005: Add reference to `T810A-IG-006` (Session Context Injection & Handoff)
- T810A1-IF-006: Add reference to `T810A-IG-004` (Dynamic JSON Single-Entry Pattern)

---

**3.5. Section III.J: Feature Integration Notes** (was Section III.I)

**RETAIN ALL** (no deletions):
- T810A1-INT-001 through INT-005 → **No renumbering required** (all feature-specific)

**UPDATE descriptions**: Add explicit Epic IG/DEP references:
- T810A1-INT-002: Add reference to `T810A-IG-006` (Session Context Injection & Handoff)
- T810A1-INT-004: Add reference to `T810A-DEP-004` + `T810A-IG-004` (Patient Data Structures + Dynamic JSON)
- T810A1-INT-005: Add reference to `T810A-IG-005` (Memory Review Protocol)

---

## III. PHASE 3 CHANGES: GDR ALIGNMENT & DEMOTION

### A. Overview

**Decision**: 2 Epic GDRs demoted to T810A1 Feature scope (Feature-specific conversational workflow).

**Demoted GDRs**:
1. `T810A-GDR-001` (Tracking-First Clinical Protocol) → `T810A1-GDR-001`
2. `T810A-GDR-004` (Session Workflow Architecture) → `T810A1-GDR-002`

**Rationale**: Phase 3A research found these GDRs contain T810A1-specific prompt engineering patterns (5-phase protocol, 2-loop minimum, Step 0/1/2 session init) not applicable cross-feature.

**Impact on T810A1**: Add Feature Governance Decisions section with T810A1-GDR-001/002.

---

### B. Demoted GDR Content (Full Text from SPS)

**Placement**: Add to T810A1 Request Section "Feature Governance Decisions" (follow T102-STD-004 format).

#### **T810A1-GDR-001 (Tracking-First Clinical Protocol)**

```markdown
* **T810A1-GDR-001 (Tracking-First Clinical Protocol)** {#t810a1-gdr-001-tracking-first}

  **Context:** Research validation (`T810A-RES-001` Deliverable C) establishes Tracking-First workflow as optimal entry point for gastroenterology conversational AI. Empirical conversation analysis (`T810A-RES-002`) validated 5-phase protocol structure (Greet, Tracking, Probe & Engage, Coach, Close) with minimum 2-loop conversation pattern to ensure adequate clarification before advice. Traditional medical consultation begins with open-ended questioning; adapting this for asynchronous tracking-first context requires explicit protocol design to prevent premature coaching without adequate context gathering.

  **Decision:** Adopt **Tracking-First Clinical Protocol** as the canonical conversation architecture for LLM_Gastro:

  **5-Phase Protocol Structure:**
  - **Phase 0: Greet** — Welcome returning user; trigger Memory review per `T810A-IG-005`
  - **Phase 1: Tracking** — Elicit tracking data (meals, stools, symptoms); generate Dynamic JSON per `T810A-IG-004`
  - **Phase 2: Probe & Engage** — Ask ≥2 clarifying questions per `T810A-IG-002` before moving to coaching; validate confidence per `T810A-QG-007`
  - **Phase 3: Coach** — Provide holistic analysis per `T810A-QG-004`; suggest patterns; frame hypotheses as "working theories" per `T810A-CON-003`
  - **Phase 4: Close** — Offer session-end report per `T810A-IG-006`; confirm next steps

  **Minimum 2-Loop Pattern:**
  - **Loop 1**: Agent asks clarifying questions (Probe)
  - **Loop 2**: Patient responds; agent acknowledges and proceeds to coaching
  - **Rationale**: Prevents single-turn "here's advice" responses observed in empirical analysis; ensures adequate context gathering

  **Protocol Triggering:** Smart protocol selection per `T810A-IG-001`:
  - **Tracking-only input** → Full 5-phase protocol
  - **Direct question** → Q&A mode (skip Tracking phase)
  - **Follow-up clarification** → Resume mid-protocol

  This decision establishes conversation structure grounding all S05 (Execution Protocol) implementation guidance.

  **Consequences:**
  - (+) Industry-validated conversation architecture per `T810A-RES-001`; empirically tested per `T810A-RES-002`
  - (+) Minimum 2-loop pattern enforces adequate probing before coaching per `T810A-QG-008`
  - (+) Tracking-first entry point natural for patient self-reporting workflows
  - (+) Smart protocol triggering enables flexible conversation patterns (tracking, Q&A, follow-up)
  - (±) 2-loop minimum is soft guideline (no programmatic enforcement per `T810A-CON-004`); relies on S05 prompt discipline
  - (±) Full 5-phase execution may extend conversation length vs. single-turn responses; mitigated by conversational tone per `T810A-QG-002`
  - (-) Protocol triggering logic requires S05 implementation testing per T810A1-ISSUE-002

  **References:**
  `T810A-RES-001 (System Architecture & Clinical Validation)`,
  `T810A-RES-002 (Conversation-Driven Empirical Validation)`,
  `T810A-QG-001 (Clinical Protocol Reliability)`,
  `T810A-QG-002 (Persona & Tone)`,
  `T810A-QG-004 (Holistic Analysis)`,
  `T810A-QG-007 (Confidence Communication)`,
  `T810A-QG-008 (Clarification Over Guessing)`,
  `T810A-IG-001 (Protocol Triggering Guidance)`,
  `T810A-IG-002 (Probe Phase Enforcement)`,
  `T810A-IG-004 (Dynamic JSON Single-Entry Pattern)`,
  `T810A-IG-005 (Memory Review Protocol)`,
  `T810A-IG-006 (Session Context Injection & Handoff)`,
  `T810A-CON-003 (Clinical Compliance Deferral)`,
  `T810A-CON-004 (ChatGPT Architectural Constraints)`
```

#### **T810A1-GDR-002 (Session Workflow Architecture)**

```markdown
* **T810A1-GDR-002 (Session Workflow Architecture)** {#t810a1-gdr-002-session-workflow}

  **Context:** Empirical conversation analysis (`T810A-RES-002`) and client directive (Phase 1.5 Comment 2) established three-step session initialization pattern: **Step 0**: Memory review; **Step 1**: Context loading (Stable JSON); **Step 2**: Greet user. ChatGPT Memory feature (`T810A-DEP-001`) provides cross-session persistence but competes with Stable JSON authority per `T810A-GDR-002` (Stable/Dynamic JSON Architecture). Without explicit session initialization protocol, discrepancies between Memory and Stable JSON create confusion and authority conflicts.

  **Decision:** Adopt **Session Workflow Architecture** defining initialization, conversation execution, and session-end patterns:

  **Session Initialization (3-Step Pattern):**
  - **Step 0: Memory Review** — Review ChatGPT Memory for patient profile info; compare to Stable JSON authority per `T810A-IG-005`
  - **Step 1: Context Loading** — Load Stable JSON (patient profile) from Knowledge Base per `T810A-GDR-002`; Stable JSON has authority over Memory in case of conflict
  - **Step 2: Greet User** — Welcome returning user with personalized greeting; enter Phase 1 (Tracking) per `T810A1-GDR-001`

  **Conversation Execution:**
  - Follow 5-phase protocol per `T810A1-GDR-001`
  - Generate Dynamic JSON per `T810A-IG-004` during Phase 1 (Tracking)
  - Apply minimum 2-loop pattern during Phase 2 (Probe & Engage)

  **Session-End Pattern:**
  - Offer session-end report per `T810A-IG-006` during Phase 4 (Close)
  - Export Markdown narrative + structured JSON per `T810A-ADR-003` (Dual-Purpose Reporting Policy)

  This decision establishes session boundaries and context management grounding all S05 (Execution Protocol) session lifecycle implementation.

  **Consequences:**
  - (+) Explicit initialization protocol resolves Memory vs. Stable JSON authority conflicts per `T810A-GDR-002`
  - (+) 3-step pattern ensures fresh context loading every session (mitigates Stable JSON staleness risk per T810A1-RISK-005)
  - (+) Session-end reporting enables cross-session continuity per `T810A-IG-006`
  - (±) Step 0 Memory review relies on prompt discipline (no programmatic comparison per `T810A-CON-004`)
  - (±) Stable JSON authority rule may require patient education on manual update workflow per T810A1-ISSUE-001
  - (-) Session initialization adds overhead to first turn; mitigated by conversational integration (no blocking gates per `T810A-QG-006`)

  **References:**
  `T810A-RES-002 (Conversation-Driven Empirical Validation)`,
  `T810A-GDR-002 (Schema Split Architecture)`,
  `T810A-ADR-003 (Dual-Purpose Reporting Policy)`,
  `T810A1-GDR-001 (Tracking-First Clinical Protocol)`,
  `T810A-QG-006 (Usability)`,
  `T810A-IG-004 (Dynamic JSON Single-Entry Pattern)`,
  `T810A-IG-005 (Memory Review Protocol)`,
  `T810A-IG-006 (Session Context Injection & Handoff)`,
  `T810A-CON-004 (ChatGPT Architectural Constraints)`,
  `T810A-DEP-001 (Platform)`
```

---

### C. T810A1 Integration Requirements (Phase 3)

**Required Action 1: Create Feature Governance Decisions Section**

Add section to T810A1 Request following T102-STD-004 (Decision Records Index) format.

**Placement**: After **Section III.J (Feature Integration Notes)**, before **Section III.K (Stories & Specification)**

**New section header**: `### K. Feature Governance Decisions`

**Impact**: Further section renumbering:
- Current Section III.J (Stories) → New Section III.L
- Current Section III.K (Acceptance Criteria) → New Section III.M
- Current Section III.L (Open Issues & Risks) → New Section III.N
- Current Section III.M (Research & Notes) → New Section III.O

**Structure Template**:
```markdown
### K. Feature Governance Decisions

This section documents T810A1-specific governance decisions governing conversational workflow and session lifecycle architecture. These GDRs were demoted from Epic scope per Phase 3 analysis (Feature-specific prompt engineering patterns not applicable cross-feature).

**Feature GDR Index**

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| `T810A1-GDR-001` | Tracking-First Clinical Protocol | Accepted | Client | 2025-10-27 | — | #t810a1-gdr-001-tracking-first |
| `T810A1-GDR-002` | Session Workflow Architecture | Accepted | Client | 2025-10-27 | — | #t810a1-gdr-002-session-workflow |

[Insert GDR body sections from III.B above]
```

**Required Action 2: Update S05 Execution Protocol References**

Replace direct GDR body references with E-IG/E-QG refs where implementation details moved to Epic level.

**Example Replacements**:
- Replace: "Probe phase SHALL ask ≥2 clarifying questions per GDR-001"
- With: "Probe phase SHALL enforce minimum probing per `T810A-IG-002` implementing T810A1-GDR-001 2-loop pattern"

- Replace: "Generate Dynamic JSON per GDR-003"
- With: "Generate Dynamic JSON per `T810A-IG-004` single-entry pattern"

- Replace: "Communicate confidence qualitatively per GDR-002"
- With: "Communicate confidence qualitatively per `T810A-QG-007` and `T810A-ADR-001` (Trust-and-Verify Confidence Policy)"

**Required Action 3: Maintain Numeric Confidence Prohibition**

Per `T810A-ADR-001` (Trust-and-Verify Confidence Policy):
- **User-facing text**: Qualitative descriptors ONLY ("fairly confident," "uncertain," etc.)
- **JSON tracking**: Numeric confidence (0-1 scale) MANDATORY for backend per ADR-001-FR-002
- **Example**: Dynamic JSON `"confidence": 0.85` is correct; S05 user-facing text "85% confident" is PROHIBITED

---

## IV. PHASE 4 CHANGES: ISSUES & RISKS STRATEGIC DEMOTION

### A. Overview

**Decision**: ALL 9 current "Epic" Issues & Risks demoted to T810A1 Feature scope.

**Rationale**: Phase 4 analysis showed 78% Feature-specific (T810A1 implementation details); T810A1-RISK-004 directly tied to demoted GDR-001 (2-loop pattern).

**Impact on T810A1**: Update existing **Section III.L (Open Issues & Risks)** with 9 items (4 Issues + 5 Risks).

**NOTE**: Section III.L already exists in T810A1 Request baseline (lines 527-554). DO NOT create new section; UPDATE existing section content.

---

### B. Demoted Issues & Risks Content

**Placement**: Add to T810A1 Request Section "Feature Issues & Risks" with IDs updated to T810A1-* per T102-STD-005.

#### **Demoted Issues** (4 → T810A1)

**T810A1-ISSUE-001: Stable/Dynamic JSON Architecture Dependency**
- **Description**: Implementation of Stable JSON (read-only patient profile) vs. Dynamic JSON (per-interaction tracking entries) architecture requires completion of `T810A2-SCHEMA` schema specifications. Surface-level references in `T810A1` may need adjustment based on T810A2 final schemas.
- **Owner**: LLM_Consultant
- **Status**: OPEN
- **Priority**: High

**T810A1-ISSUE-002: Protocol Triggering Logic Implementation**
- **Description**: Smart protocol triggering to distinguish tracking-only vs. full protocol vs. Q&A inputs requires S05 (Execution Protocol) development. Implementation approach (keyword detection, context clues, default behavior) needs validation against actual conversation patterns.
- **Owner**: LLM_Consultant
- **Status**: OPEN
- **Priority**: Medium

**T810A1-ISSUE-003: ChatGPT Assistant Mode Override Strategy**
- **Description**: ChatGPT's native "helpful Assistant" behavior overrides Consultant/Analyst stance defined in system prompt. Probe phase enforcement via S08 exemplars and S05 execution instructions needs empirical testing to validate effectiveness. No programmatic gate control available in ChatGPT interface.
- **Owner**: LLM_Consultant
- **Status**: OPEN
- **Priority**: High

**T810A1-ISSUE-004: Controlled Vocabulary Validation**
- **Description**: Dynamic JSON generation requires consistent value sets (e.g., stress levels, Bristol types) but ChatGPT provides no programmatic validation. Enforcement must rely entirely on S05 execution protocol instructions and S08 exemplars. Risk of value drift over time without automated validation.
- **Owner**: LLM_Consultant
- **Status**: OPEN
- **Priority**: Medium

#### **Demoted Risks** (5 → T810A1)

**T810A1-RISK-001: ChatGPT Override Insufficient**
- **Description**: Risk that ChatGPT's native Assistant mode cannot be sufficiently overridden via prompt engineering alone, leading to continued absence of Probe phase and premature coaching (observed in conversation example). Mitigation: Extensive S08 exemplars, S05 explicit Probe enforcement, empirical testing with iterative prompt refinement.
- **Owner**: LLM_Consultant
- **Status**: MONITORED
- **Priority**: High

**T810A1-RISK-002: T810A2 Development Delays**
- **Description**: Risk that parallel `T810A2-SCHEMA` development delays S04-S10 specification due to schema dependencies. Mitigation: Surface-level JSON references in `T810A1`; detailed schemas deferred to T810A2; parallel development tracks with coordination checkpoints.
- **Owner**: LLM_Consultant
- **Status**: ACCEPTED
- **Priority**: Medium

**T810A1-RISK-003: Scope Expansion Beyond MVP**
- **Description**: Risk that Phase 1.5 findings (10 new/revised F-IDs) expand scope beyond original MVP constraints, delaying Phase 2-3 completion. Mitigation: Strict adherence to prompt-only implementation; no custom UI/validation; defer complex features (multi-frequency reporting, advanced profiling) per original CON specifications.
- **Owner**: LLM_Consultant
- **Status**: MONITORED
- **Priority**: Medium

**T810A1-RISK-004: Minimum 2-Loop Pattern Non-Compliance**
- **Description**: Risk that soft guideline for 2-loop conversation pattern (vs. hard gate) leads to continued 1-loop behavior with insufficient probing. Observed in conversation Turn 1: went straight to coaching without clarifying questions. Mitigation: S05 explicit instruction for ≥2 clarifying questions; S08 anti-pattern examples; S07 quality criteria for protocol adherence.
- **Owner**: LLM_Consultant
- **Status**: MONITORED
- **Priority**: Medium

**T810A1-RISK-005: Stable JSON Manual Update Friction**
- **Description**: Risk that requiring manual patient updates to Stable JSON (ChatGPT read-only constraint) creates friction and profile staleness. Mitigation: `T810A-IG-005` memory review protocol to flag discrepancies; Probe phase can elicit updates; document manual update workflow in S04.
- **Owner**: LLM_Consultant
- **Status**: ACCEPTED
- **Priority**: Low

---

### C. T810A1 Integration Requirements (Phase 4)

**Required Action: Update Existing Open Issues & Risks Section**

Update **existing Section III.L (Open Issues & Risks)** with 9 demoted items (IDs updated to T810A1-* per T102-STD-005).

**Current Section Location**: Lines 527-554 in T810A1 Request baseline

**Post-Migration Section Number**: **Section III.N** (after Phase 2/3 insertions create new Sections E, F, K)

**Actions**:
1. **REPLACE existing content**: Clear current placeholder content in Section III.L
2. **INSERT 4 Issues**: T810A1-ISSUE-001 through ISSUE-004 (complete descriptions from Section IV.B above)
3. **INSERT 5 Risks**: T810A1-RISK-001 through RISK-005 (complete descriptions from Section IV.B above)

**Format**: Follow SPS Issues & Risks table format (ID, Title, Description, Owner, Status, Priority, Proposed Date, Resolution/Mitigation Date).

**Status/Priority Maintenance**: Preserve current Status/Priority/Owner fields from Epic Issues & Risks as documented in Section IV.B.

---

## V. IMPLEMENTATION GUIDANCE & COORDINATION

### A. Post-Migration T810A1 Request Structure

After integrating Phase 2/3/4 changes, the T810A1 Request will have the following structure:

**1. Feature Overview** (Sections III.A-D — NO CHANGES)
   - Section III.A: Feature Solution Framework
   - Section III.B: Source & Scope
   - Section III.C: Business Objectives & Success Signals
   - Section III.D: Stakeholders

**2. Inherited Epic Considerations** (NEW Section III.E)
   - **Content**: Table with 8 rows grouping 27 Epic E-RIDs + 3 Epic GDRs + 2 Epic RES + 3 Epic ADRs by category
   - **Format**: `Source Artifact | Source ID | Category | Inherited Rule IDs` (matches existing Request exemplar)
   - **Categories**: Assumptions (4 E-RIDs), Dependencies (5 E-RIDs), Constraints (4 E-RIDs), Quality Goals (8 E-RIDs), Implementation Guidance (6 E-RIDs), Governance (3 GDRs), Research (2 RES), Architecture (3 ADRs)
   - **Section Split Impact**: Current Section III.E content SPLITS into E (table only) + F (feature-specific ASSUM/DEP)

**3. Feature-Specific Assumptions & Dependencies** (NEW Section III.F — was part of III.E)
   - **RENUMBERED**: T810A1-ASSUM-004 → ASSUM-001 (Session-Scoped Memory Model)
   - **RENUMBERED**: T810A1-DEP-008 → DEP-001 (Protocol Triggering Research)
   - **DELETED**: ASSUM-001/002/003, DEP-001/002/003/004/005 (promoted to Epic)

**4. Feature-Specific Non-Functional Requirements** (Section III.G — was III.F)
   - **RETAIN**: NFR-001, NFR-002 (no renumbering)
   - **RENUMBERED**: NFR-005 → NFR-003, NFR-008 → NFR-004, NFR-009 → NFR-005
   - **DELETED**: NFR-003/004/006/007 (promoted to Epic QGs)

**5. Interfaces & Data** (Section III.H — was III.G)
   - **RETAIN ALL**: IF-001 through IF-006 (no renumbering)
   - **UPDATED**: Add Epic IG references in descriptions

**6. Feature-Specific Constraints** (Section III.I — was III.H)
   - **RENUMBERED**: CON-002 → CON-001, CON-003 → CON-002, CON-005 → CON-003
   - **DELETED**: CON-001/004/006/007/008 (promoted to Epic)

**7. Feature Integration Notes** (Section III.J — was III.I)
   - **RETAIN ALL**: INT-001 through INT-005 (no renumbering)
   - **UPDATED**: Add Epic IG/DEP references in descriptions

**8. Feature Governance Decisions** (NEW Section III.K)
   - **Content**: T810A1-GDR-001 (Tracking-First Clinical Protocol), T810A1-GDR-002 (Session Workflow Architecture)
   - **Format**: GDR Index table + full GDR bodies (Context, Decision, Consequences, References) per T102-STD-004

**9. Stories & Specification** (Section III.L — was III.J)
   - **RETAIN**: Stories S01-S09 (9-block implementation specifics)
   - **UPDATE**: S05 Execution Protocol references (replace demoted GDR-001/004 with E-IG refs)

**10. Acceptance Criteria Register** (Section III.M — was III.K)

**11. Open Issues & Risks** (Section III.N — was III.L)
   - **UPDATED**: Replace placeholder content with 4 Issues (T810A1-ISSUE-001 through 004) + 5 Risks (T810A1-RISK-001 through 005)

**12. Research & Notes** (Section III.O — was III.M)

**Content Distribution**:
- **Inherited from Epic**: 27 E-RIDs + 3 GDRs + 2 RES + 3 ADRs = 35 items (47% of requirements)
- **Feature Delta After Renumbering**: 2 ASSUM + 1 DEP + 5 NFRs + 6 IFs + 3 CONs + 5 INTs + 2 GDRs + 9 Stories + 9 Issues/Risks = 42 items (53% of requirements)

---

### B. Request Document Update Checklist

**STEP 1: Section Restructuring (Phase 2 — Section Split)**

- [ ] **SPLIT current Section III.E into TWO sections**:
  - **Step 1.1**: Create NEW **Section III.E: Inherited Considerations**
    - INSERT after Section III.D (Stakeholders)
    - Content: Table ONLY (no subsections) grouping 35 inherited items by category
    - Use template from Section II.C above

  - **Step 1.2**: Create NEW **Section III.F: Assumptions & Dependencies**
    - Rename current "### E. Inheritences, Assumptions & Dependencies" header to "### F. Assumptions & Dependencies"
    - REMOVE "Inherited Considerations" table from this section (now in Section III.E)
    - Keep ONLY feature-specific Assumptions & Dependencies subsections

- [ ] **Renumber ALL subsequent sections** after split:
  - Old III.F → New III.G
  - Old III.G → New III.H
  - Old III.H → New III.I
  - Old III.I → New III.J
  - Old III.J → New III.K (will become III.L after GDR insertion)
  - Old III.K → New III.M (will become III.M after GDR insertion)
  - Old III.L → New III.N (will become III.N after GDR insertion)
  - Old III.M → New III.O (will become III.O after GDR insertion)

---

**STEP 2: F-RID Content Cleanup & Renumbering (Phase 2 — DELETE promoted RIDs)**

- [ ] **Section III.F (Assumptions & Dependencies) cleanup**:
  - DELETE entire content blocks: ASSUM-001, ASSUM-002, ASSUM-003
  - DELETE entire content blocks: DEP-001, DEP-002, DEP-003, DEP-004, DEP-005
  - RENUMBER: ASSUM-004 → ASSUM-001
  - RENUMBER: DEP-008 → DEP-001

- [ ] **Section III.G (Non-Functional Requirements) cleanup**:
  - DELETE entire content blocks: NFR-003, NFR-004, NFR-006, NFR-007
  - RETAIN: NFR-001, NFR-002 (no renumbering)
  - RENUMBER: NFR-005 → NFR-003
  - RENUMBER: NFR-008 → NFR-004
  - RENUMBER: NFR-009 → NFR-005

- [ ] **Section III.I (Constraints) cleanup**:
  - DELETE entire content blocks: CON-001, CON-004, CON-006, CON-007, CON-008
  - RENUMBER: CON-002 → CON-001
  - RENUMBER: CON-003 → CON-002
  - RENUMBER: CON-005 → CON-003

- [ ] **Update ALL cross-references** throughout Request after renumbering:
  - Find/Replace: T810A1-NFR-005 → T810A1-NFR-003 (especially in Stories S01-S09)
  - Find/Replace: T810A1-NFR-008 → T810A1-NFR-004 (especially in Stories S05, Interfaces)
  - Find/Replace: T810A1-NFR-009 → T810A1-NFR-005 (especially in Stories S05, S06)
  - Find/Replace: T810A1-ASSUM-004 → T810A1-ASSUM-001 (in Integration Notes)
  - Find/Replace: T810A1-DEP-008 → T810A1-DEP-001 (in Dependencies, NFRs)
  - Find/Replace: T810A1-CON-002/003/005 → T810A1-CON-001/002/003 (throughout)

---

**STEP 3: Epic Reference Updates (Phase 2 — F-RID→E-RID replacements)**

- [ ] **Replace promoted F-RID citations with E-RID references** throughout Request:
  - T810A1-ASSUM-001/002/003 → T810A-ASSUM-001/002/003
  - T810A1-DEP-001/002/003/004/005 → T810A-DEP-001/002/003/004/005
  - T810A1-CON-001/006/007/008 → T810A-CON-001/002/003/004
  - T810A1-CON-004 → T810A-QG-008 (reclassification)
  - T810A1-NFR-003/004/006/007 → T810A-QG-003/004/006/007

- [ ] **Add Epic IG/GDR/ADR references** in Interfaces & Integration Notes:
  - T810A1-IF-003: Add `T810A-IG-003`
  - T810A1-IF-004: Add `T810A-IG-001`
  - T810A1-IF-005: Add `T810A-IG-006`
  - T810A1-IF-006: Add `T810A-IG-004`
  - T810A1-INT-002: Add `T810A-IG-006`
  - T810A1-INT-004: Add `T810A-DEP-004 + T810A-IG-004`
  - T810A1-INT-005: Add `T810A-IG-005`

---

**STEP 4: Feature Governance Decisions (Phase 3 — NEW Section III.K)**

- [ ] **CREATE NEW Section III.K: Feature Governance Decisions**
  - **Placement**: After NEW Section III.J (Feature Integration Notes), before NEW Section III.L (Stories)
  - **Content**: GDR Index table + T810A1-GDR-001 full body + T810A1-GDR-002 full body
  - **Format**: Follow template from Section III.C above (T102-STD-004 compliance)

- [ ] **UPDATE Section III.L (Stories) — S05 Execution Protocol**:
  - Replace demoted GDR-001/004 references with E-IG references:
    - "Per T810A-GDR-001..." → "Per T810A-IG-001 (Protocol Triggering Guidance) + T810A-IG-002 (Probe Phase Enforcement)..."
    - "Per T810A-GDR-004..." → "Per T810A-IG-005 (Memory Review Protocol)..."
  - Retain T810A1-GDR-001/002 references for Feature-specific workflow details

---

**STEP 5: Issues & Risks Update (Phase 4 — UPDATE existing Section III.N)**

- [ ] **UPDATE existing Section III.N (Open Issues & Risks)**:
  - **REPLACE placeholder content** with demoted Issues & Risks
  - **INSERT 4 Issues**: T810A1-ISSUE-001 through ISSUE-004 (from Section IV.B)
  - **INSERT 5 Risks**: T810A1-RISK-001 through RISK-005 (from Section IV.B)
  - **Format**: Issues table + Risks table per SPS standard
  - **Preserve**: Status/Priority/Owner fields from Epic versions

---

**STEP 6: Final Validation**

- [ ] **Verify section renumbering cascade**: E, F, G, H, I, J, K, L, M, N, O
- [ ] **Verify GDR format compliance** (T102-STD-004): Context, Decision, Consequences, References
- [ ] **Verify RID reference syntax** (T102-STD-005): Backticks, formal format
- [ ] **Verify content distribution**: 47% Epic inheritance (35 items), 53% Feature delta (42 items)

---

### C. Coordination Checkpoints

**Checkpoint 1: Section Restructuring & Table Format**
- **Section Split**: Verify Section III.E SPLIT into E (table only) + F (feature ASSUM/DEP only)
- **Table Format**: Confirm table uses `Source Artifact | Source ID | Category | Inherited Rule IDs` format (8 rows grouping 35 items)
- **Categories**: Verify 8 category rows: Assumptions, Dependencies, Constraints, Quality Goals, Implementation Guidance, Governance, Research, Architecture
- **Item Count**: Confirm 27 E-RIDs + 3 GDRs + 2 RES + 3 ADRs = 35 total inherited items
- **Section Renumbering**: Validate cascade E→F→G→H→I→J→K→L→M→N→O

**Checkpoint 2: RID Renumbering & Cleanup**
- **Deletions**: Verify 20 F-RIDs completely removed (ASSUM-001/002/003, DEP-001/002/003/004/005, CON-001/004/006/007/008, NFR-003/004/006/007)
- **Renumbering**: Confirm ASSUM-004→001, DEP-008→001, NFR-005→003, NFR-008→004, NFR-009→005, CON-002→001, CON-003→002, CON-005→003
- **Cross-References**: Validate ALL references updated throughout Request (especially Stories S01-S09)

**Checkpoint 3: GDR Integration & Placement**
- **Placement**: Confirm Section III.K placement (after J, before L)
- **Format**: Verify GDR Index table + full bodies (Context, Decision, Consequences, References) per T102-STD-004
- **S05 Updates**: Validate demoted GDR-001/004 replaced with E-IG references in Execution Protocol

**Checkpoint 4: Issues & Risks Update**
- **Section Update**: Confirm existing Section III.N (was III.L) updated with 9 items (not new section created)
- **Content**: Verify 4 Issues + 5 Risks with complete descriptions from Section IV.B
- **Status/Priority**: Validate preservation from Epic versions

---

### D. Success Criteria

T810A1 Request document integration complete when:

**1. Section Restructuring**
- [ ] **Section III.E split** completed (E: Inherited Considerations table only; F: Feature ASSUM/DEP only)
- [ ] **Section renumbering** cascade verified (E→F→G→H→I→J→K→L→M→N→O)
- [ ] **Table format** matches exemplar (`Source Artifact | Source ID | Category | Inherited Rule IDs`)
- [ ] **35 inherited items** grouped in 8 category rows (Assumptions, Dependencies, Constraints, Quality Goals, Implementation Guidance, Governance, Research, Architecture)

**2. F-RID Content Cleanup**
- [ ] **20 promoted F-RIDs** completely removed (ASSUM-001/002/003, DEP-001/002/003/004/005, CON-001/004/006/007/008, NFR-003/004/006/007)
- [ ] **10 retained F-RIDs** renumbered to start from 001:
  - ASSUM-004→001, DEP-008→001, NFR-005→003, NFR-008→004, NFR-009→005, CON-002→001, CON-003→002, CON-005→003
- [ ] **ALL cross-references** updated throughout Request (Stories, Interfaces, Integration Notes)

**3. Epic Reference Integration**
- [ ] **F-RID→E-RID replacements** completed (20 promoted items)
- [ ] **Epic IG references** added to Interfaces & Integration Notes descriptions

**4. Feature Governance Decisions**
- [ ] **Section III.K** created with T810A1-GDR-001/002 (placement: after J, before L)
- [ ] **GDR format** compliant with T102-STD-004 (Context, Decision, Consequences, References)
- [ ] **S05 Execution Protocol** updated (demoted GDR-001/004 → E-IG references)

**5. Issues & Risks**
- [ ] **Existing Section III.N** updated (was III.L; not new section created)
- [ ] **9 items** inserted (4 Issues + 5 Risks with complete descriptions from Section IV.B)
- [ ] **Status/Priority/Owner** preserved from Epic versions

**6. Format Compliance**
- [ ] **T102-STD-004** compliance (GDR bodies format)
- [ ] **T102-STD-005** compliance (RID reference syntax with backticks)
- [ ] **Issues & Risks tables** follow SPS format

**7. Validation**
- [ ] **4 Coordination checkpoints** passed
- [ ] **Content distribution** verified (47% Epic / 53% Feature = 35 / 42 items)
- [ ] T810A1 subconsultant confirms integration complete

---

## VI. SUMMARY & NEXT STEPS

This handoff brief communicates comprehensive Epic changes from Phases 2/3/4:
- **Phase 2**: 27 E-RIDs promoted (Inherited Considerations Table)
- **Phase 3**: 2 GDRs demoted (Feature Governance Decisions)
- **Phase 4**: 9 Items demoted (Feature Issues & Risks)

**T810A1 Next Steps**:
1. Update Request document per Implementation Guidance (Section V.A)
2. Complete Coordination Checkpoints (Section V.B)
3. Validate Success Criteria (Section V.C)
4. Confirm integration complete with Epic consultant

**Epic Next Steps**:
- Epic consultant proceeds to Phase 6 (Holistic Migration Review)
- T810A1 work can proceed in parallel (non-blocking)
- Final coordination after Phase 6 if additional changes identified

---

**END OF HANDOFF BRIEF**
