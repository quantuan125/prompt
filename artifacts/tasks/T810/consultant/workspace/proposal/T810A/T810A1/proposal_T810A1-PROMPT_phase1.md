---
artifact_type: 'PROPOSAL'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1'
feature_code: 'PROMPT'
version: '1.0.6'
date: '2025-12-12'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_document: 'request_T810A1-PROMPT.md'
target_sections: 'F.3 (Constraints - ENHANCE), F.6 (Implementation Guidance - NEW), F.7 (Integration Notes - ENHANCE)'
governance_link: '../workspace_documentation_rules.md'
plan_reference: '../plan/T810A/T810A1/plan_T810A1-PROMPT_frid-enhancement.md'
---

# PHASE 1 PROPOSAL: T810A1-PROMPT F-RID Enhancement (IG Creation & INT Integration)

## I. EXECUTIVE SUMMARY

This proposal presents the Phase 1 consultancy outcomes for enhancing T810A1-PROMPT Feature Requirements by integrating research findings (`T810A1-RES-001`) and T810A2 schema handoff deliverables (`T810A1-NOTE-001`). Phase 0 analysis artifacts have identified specific F-RID implications requiring action in Phase 1.

**Phase Scope**: F-RID Review & Enhancement per `plan_T810A1-PROMPT_frid-enhancement.md` Section IV.

**Key Deliverables**:
1. **F.6 Implementation Guidance (NEW)**: Complete IG category with 8 items (T810A1-IG-001 through IG-008)
2. **F.7 Integration Notes (ENHANCED)**: 3 enhanced existing INT items + 2 new INT items with T810A2 cross-references
3. **F.3 Constraints (ENHANCED)**: MVP deployment constraints proposed (`T810A1-CON-004`, `T810A1-CON-005`)

**Phase 3 QA Alignment (Workspace-Only)**:
- This proposal is the workspace medium for Request optimizations; SSOT changes are not applied until explicit client approval.
- Block-specific placement is governed by `T810A1-ADR-001 (9-Block Architecture Assignment)`; IG/INT items do not restate block applicability.

**Consultation Approach**: This proposal serves as a dynamic workspace for collaborative F-RID specification development. Content is organized by target Request subsection, with full F-RID bodies (not just IDs) presented for client review and iteration.

**Phase 0 Dependencies Satisfied**:
- ✅ Analysis artifacts completed (`analysis_T810A1-PROMPT_frid-enhancement_res-001.md`, `analysis_T810A1-PROMPT_frid-enhancement_note-001.md`)
- ✅ T810A1-NOTE-001 and T810A1-RES-001 entries registered in Request Section I
- ✅ Context materials reviewed per plan Section II

---

## II. SUBPHASE 1.1: F-RID INVENTORY REVIEW

### A. Current F-RID Inventory (Request v1.0.0)

**Purpose**: Establish baseline understanding of existing T810A1 F-RIDs before enhancement.

| Category | Token | Count | Existing IDs | Enhancement Action |
|:---------|:------|:------|:------------|:-------------------|
| Assumptions | `ASSUM` | 1 | T810A1-ASSUM-001 | Review for alignment |
| Constraints | `CON` | 3 | T810A1-CON-001, 002, 003 | **ADD CON-004** (Fixed Keys) + **ADD CON-005** (System Prompt Limit) |
| Non-Functional Requirements | `NFR` | 5 | T810A1-NFR-001 to 005 | Review for research enhancement |
| Dependencies | `DEP` | 1 | T810A1-DEP-001 | Review for T810A2 dependency |
| Interfaces & Data | `IF` | 6 | T810A1-IF-001 to 006 | Review for schema references |
| **Implementation Guidance** | **`IG`** | **0** | **NONE** | **CREATE F.6 subsection** |
| Integration Notes | `INT` | 5 | T810A1-INT-001 to 005 | **ENHANCE + ADD INT-006, INT-007** |
| Governance Decisions | `GDR` | 2 | T810A1-GDR-001, 002 | Review for consistency |

### B. Research-Driven Enhancement Targets (from `analysis_T810A1-PROMPT_frid-enhancement_res-001.md`)

**Source**: T810A1-RES-001 (Execution Protocol Clinical Validation)

| Finding | Target F-RID Category | Rationale |
|:--------|:---------------------|:----------|
| Gate-Based Enforcement (LLM_Consultant patterns) | `IG` (NEW) | Explicit phase transition gates prevent protocol drift |
| OARS Technique (clinical best practices) | `IG` (NEW) | Probe dialogue patterns require IG-level guidance |
| Epistemic Hedging (therapeutic uncertainty) | `IG` (NEW) | Confidence communication needs normative specification |
| VPA Conditional Triggering (input-type detection) | `IG` (NEW) | Protocol selection logic requires internal guidance |
| Anti-Patterns (communication failures) | `IG` (NEW) | Prohibited behaviors need explicit cataloging |

### C. Handoff-Driven Enhancement Targets (from `analysis_T810A1-PROMPT_frid-enhancement_note-001.md`)

**Source**: T810A1-NOTE-001 (T810A2 Schema Handoff)

| Deliverable | Target F-RID Category | Rationale |
|:------------|:---------------------|:----------|
| Stable/Dynamic Schema Architecture | `INT` (ENHANCE) | T810A1-INT-005 needs schema loading sequence |
| Single-Entry Model | `INT` (ENHANCE) | T810A1-INT-001 needs T810A2-INT-001 cross-reference |
| Fixed Keys Constraint (T810A2-CON-005) | `CON` (NEW) | Mirror T810A2 constraint in PROMPT scope |
| Mandatory/Optional Field Classification | `INT` (ENHANCE) | T810A1-INT-001 probe triggering logic |
| Session Initialization (T810A2-INT-003) | `INT` (NEW), `IG` (NEW) | Both INT-006 and IG-006 needed |
| Conflict Resolution (T810A2-INT-004) | `INT` (ENHANCE) | T810A1-INT-003 needs precedence rules |

### D. Implementation Strategy

**Subphase 1.2 Focus**: Create 7+ T810A1-IG items per research findings + handoff schema implications (including MVP tiered deployment packaging)
**Subphase 1.3 Focus**: Enhance 3 existing INT items + create 2 new INT items + add 2 new CON items

---

## III. SUBPHASE 1.2: PROPOSED IG CATEGORY (F.6 SUBSECTION — NEW)

### A. Category Rationale

**Implementation Guidance (IG)** provides normative internal authoring/process guidance per T102-STD-005-FR-004. IG items:
- Govern HOW to implement F-RIDs (not WHAT to implement)
- Are internal to T810A1 (feature-scoped, not cross-feature)
- Use directive language (SHALL/SHOULD) for process adherence
- Support Story-level acceptance criteria development (S05-S10)

**Research Validation**: All proposed IG items trace to validated findings in T810A1-RES-001 or T810A1-NOTE-001.

### B. Proposed T810A1-IG Items (FULL F-RID BODIES)

* **T810A1-IG-001 (Phase Gating Protocol)** — LLM_Gastro SHALL enforce explicit phase-transition gates to prevent premature phase advancement (especially coaching before probing), consistent with `T810A-GDR-001` and `T810A1-NFR-001`.

  **Operational Rules**:
  - LLM_Gastro SHALL present a brief synthesis of the user’s latest input before attempting a major phase transition, and SHALL explicitly ask for confirmation before proceeding.
  - If the user attempts to skip ahead to Coaching before sufficient probing, LLM_Gastro SHALL redirect back to probing with a small number of clarifying questions (per probe enforcement expectations in `T810A1-NFR-005`).
  - LLM_Gastro SHALL prevent endless alignment loops by re-anchoring to a single user-priority outcome when repeated clarification attempts fail.

  **Acceptance Checks**:
  - Coaching guidance does not appear before the probe gate is satisfied.
  - A gate is observable as: (a) synthesis + (b) confirmation question, prior to proceeding.
  - Skip-ahead requests are handled with a redirect back to probing (not ignored).

* **T810A1-IG-002 (OARS Dialogue Pattern)** — LLM_Gastro SHALL use OARS (Open questions, Affirmations, Reflective listening, Summaries) during probing, and SHALL avoid “rapid interrogation” (multiple questions without acknowledging answers) per `T810A1-NFR-005` and `T810A1-RES-001`.

  **Operational Rules**:
  - LLM_Gastro SHOULD ask open-ended questions first, using closed questions only when needed to complete mandatory information.
  - LLM_Gastro SHOULD acknowledge the user’s answer (affirmation or reflection) before asking the next question.
  - LLM_Gastro SHOULD periodically summarize what it believes it heard and ask for confirmation.

  **Acceptance Checks**:
  - Probe turns avoid stacked multi-question interrogations without acknowledgement.
  - At least one reflection/acknowledgement appears in a probing round before advice.
  - Summaries end with a confirmation check when moving toward decisions/recommendations.

* **T810A1-IG-003 (Epistemic Hedging Protocol)** — LLM_Gastro SHALL communicate uncertainty using qualitative hedging aligned to `T810A-ADR-001`, SHALL NOT present numeric confidence in user-facing prose, and SHALL trigger clarification when evidence is ambiguous or confidence is low.

  **Operational Rules**:
  - LLM_Gastro SHALL frame hypotheses as non-diagnostic and provisional (e.g., “could be consistent with…”) and avoid definitive claims.
  - When evidence is weak, mixed, or ambiguous, LLM_Gastro SHALL prioritize clarification questions over conclusions.
  - Numeric confidence SHALL NOT appear in user-facing prose, even if internal classification uses confidence to decide next steps.

  **Acceptance Checks**:
  - Prose contains no numeric confidence values.
  - Uncertainty triggers clarifying questions rather than assertive recommendations.
  - Outputs avoid diagnosing language and preserve clinician-review framing.

* **T810A1-IG-004 (Protocol Triggering Logic)** — LLM_Gastro SHALL detect input type and route behavior accordingly (tracking-only vs full protocol vs simple Q&A) per `T810A1-NFR-004`, and SHALL default to a conservative “full protocol” path when ambiguous.

  **Operational Rules**:
  - LLM_Gastro SHALL route behavior based on input intent: tracking-only logging, simple Q&A, or full protocol execution.
  - When intent is ambiguous, LLM_Gastro SHALL default to the safer, higher-structure path (full protocol) rather than risk missing mandatory probing/guardrails.
  - Tracking-only interactions SHOULD minimize analysis/coaching and focus on correct logging + minimal acknowledgment.

  **Acceptance Checks**:
  - The selected behavior mode is consistent with the user’s intent and risk level.
  - Ambiguous inputs reliably trigger the conservative default.
  - Tracking-only turns do not drift into extensive coaching.

* **T810A1-IG-005 (Anti-Pattern Prohibitions)** — LLM_Gastro SHALL avoid known failure modes in clinical dialogue (e.g., rapid interrogation, premature reassurance, premature coaching, unexplained jargon, dismissiveness, assistant-mode “service offers”, and over-certainty) per `T810A1-RES-001`, and SHALL self-correct before responding.

  **Operational Rules**:
  - LLM_Gastro SHALL prioritize clarity and collaboration: ask fewer questions at a time, explain terms in plain language, and validate the user’s experience without over-promising.
  - LLM_Gastro SHALL avoid “assistant-mode” framing (“I can do X for you”) when it distracts from the inquiry/protocol stance.
  - If an anti-pattern is detected in a draft response, LLM_Gastro SHALL revise before sending.

  **Acceptance Checks**:
  - Responses avoid dismissive or patronizing phrasing and avoid premature reassurance.
  - Recommendations do not appear before sufficient probing and gating.
  - Technical terms are defined when used.

* **T810A1-IG-006 (Session Initialization Sequence)** — LLM_Gastro SHALL follow the session initialization sequence defined by `T810A1-GDR-002`, including Memory review, Stable/Dynamic schema awareness, and conflict detection where ChatGPT Memory diverges from Stable profile data (Stable profile prevails per `T810A-GDR-002`).

  **Operational Rules**:
  - At session start, LLM_Gastro SHALL review available context (conversation + Memory + Stable profile schema) before making assumptions.
  - When Memory conflicts with Stable profile data, LLM_Gastro SHALL treat Stable profile data as authoritative and SHALL ask the user to resolve the discrepancy.
  - LLM_Gastro SHALL preserve the read-only constraint model (no pretending to “update files”) per platform constraints.

  **Acceptance Checks**:
  - Conflicts are surfaced and resolved explicitly rather than silently overwritten.
  - Stable profile precedence is consistently applied when conflicts occur.

* **T810A1-IG-007 (Dynamic JSON Generation Pattern)** — When tracking is required, LLM_Gastro SHALL produce exactly one Dynamic JSON object per relevant user message, SHALL use only `T810A2-SCHEMA` governed keys (no runtime key invention per `T810A1-CON-004` / `T810A2-CON-005`), SHALL use controlled vocabularies where defined, and SHALL use `null` (then probe) when mandatory fields cannot be inferred.

  **Operational Rules**:
  - LLM_Gastro SHALL output a single-entry JSON object model for each relevant tracking turn (not a cumulative session log).
  - LLM_Gastro SHALL use only schema-governed keys and SHALL NOT invent new keys at runtime; if details do not fit, LLM_Gastro SHOULD use the schema’s free-text fields (where available) rather than extending the schema.
  - For mandatory fields that cannot be inferred, LLM_Gastro SHALL output `null` and SHALL ask targeted clarifying questions to complete the record.

  **Acceptance Checks**:
  - Exactly one Dynamic JSON object appears per relevant user message.
  - No runtime key invention occurs in Dynamic JSON outputs.
  - Missing mandatory values produce `null` and trigger probing to fill them.

* **T810A1-IG-008 (Hybrid Tiered Architecture for MVP Deployment)** — MVP deployment SHALL follow a Hybrid Tiered Architecture (core Tier 1 system prompt ≤ **7,500 chars** + Tier 2 extended knowledge + Tier 3 schema knowledge). The canonical full specification remains authoritative; any tiered/condensed derivative MUST trace back to the canonical spec for governance compliance (per `T810A1-ADR-001` and `T810A1-IF-002`).

---

### C. IG Category Summary

| IG ID | Title | Primary Source | Key Pattern |
|:------|:------|:--------------|:-----------|
| IG-001 | Phase Gating Protocol | T810A1-RES-001 (LLM_Consultant) | Explicit confirmation gates, 5-ROUND CAP |
| IG-002 | OARS Dialogue Pattern | T810A1-RES-001 (OARS Technique) | Open questions, Affirmations, Reflective listening, Summaries |
| IG-003 | Epistemic Hedging Protocol | T810A1-RES-001 + T810A-ADR-001 | Qualitative confidence tiers, probabilistic language |
| IG-004 | Protocol Triggering Logic | T810A1-RES-001 (VPA) | Input-type detection, guard clauses, default behavior |
| IG-005 | Anti-Pattern Prohibitions | T810A1-RES-001 (Anti-Patterns) | 7 prohibited behaviors with correction patterns |
| IG-006 | Session Initialization Sequence | T810A1-NOTE-001 + T810A1-GDR-002 | Memory review, schema loading, conflict resolution |
| IG-007 | Dynamic JSON Generation Pattern | T810A1-NOTE-001 + T810A2 | Single-entry model, fixed keys, null-before-probe |
| IG-008 | Hybrid Tiered Architecture for MVP Deployment | Client MVP decision + CON-005 | Tier 1 ≤7,500 chars + Tier 2/3 packaging + traceability |

---

## IV. SUBPHASE 1.3: PROPOSED INT/CON ENHANCEMENTS (F.7 & F.3 SUBSECTIONS)

### A. Enhanced Existing INT Items (FULL F-RID BODIES)

* **T810A1-INT-001 (Probe Triggering Integration)** — Probe triggering SHALL align with `T810A2-INT-001 (Probe Triggering Integration)` and `T810A2-IF-004 (Field Classification Interface)` so that missing mandatory fields (including `null`) reliably trigger clarifying questions (per `T810A1-NFR-005` and the OARS requirements in `T810A1-IG-002`).

  The canonical mandatory/optional field mapping is maintained in `prompt/roles/gastro/data/field_classification_mapping.md`.

* **T810A1-INT-003 (Memory Precedence Integration)** — When ChatGPT Memory conflicts with the Stable profile schema, T810A1 SHALL apply the precedence rule defined in `T810A2-INT-004 (Conflict Resolution Integration)` and `T810A-GDR-002 (Schema Split Architecture)` (Stable profile data is authoritative).

  Conflicts SHOULD be surfaced conversationally (non-blocking) and Stable profile updates remain patient-managed per `T810A2-IG-004 (Patient-Managed Profile Updates)` under the read-only platform constraint (`T810A2-CON-004` / `T810A-CON-004`).

* **T810A1-INT-005 (Session Report Integration)** — Session-end reporting SHALL align with `T810A2-INT-002 (Aggregation Format Integration)` and `T810A-ADR-003 (Dual-Purpose Reporting Policy)` by producing a dual-format output: a concise first-person Markdown timeline plus an aggregated Dynamic JSON log (Pattern A per `T810A1-NOTE-001`), suitable for manual export workflows (`T810A2-IG-004`) and forward compatibility with `T810A2-INT-005`.

---

### B. New INT Items (FULL F-RID BODIES)

* **T810A1-INT-006 (Schema Loading Integration)** — Session initialization SHALL operate with schema awareness by referencing the T810A2 schema artifacts defined in `T810A2-INT-003 (Session Initialization Integration)`, specifically:
  - Stable profile template: `prompt/roles/gastro/data/template_stable_patient_schema.yaml`
  - Dynamic schema template: `prompt/roles/gastro/data/template_dynamic_tracking_schema.yaml`

  Under the platform constraint (`T810A-CON-004`), these files are treated as read-only reference knowledge and are retrieved implicitly by ChatGPT Project Knowledge mechanisms rather than explicit “load file” commands.

* **T810A1-INT-007 (Controlled Vocabulary Integration)** — Dynamic JSON generation SHALL use controlled vocabularies defined by `T810A-ADR-002 (Foundational Vocabulary Authority)` and T810A2 value sets (`T810A2-IF-003 (Controlled Vocabulary Interface)`), including semantic-scale mappings specified in `T810A2-IG-003`.

  The MVP vocabulary catalog reference is maintained in `prompt/roles/gastro/data/vocabulary_catalog_example.md`, and value-set enforcement is prompt-based under platform constraints (`T810A-CON-004` / `T810A2-CON-002`).

---

### C. New CON Items (F.3 Subsection — ENHANCE)

* **T810A1-CON-004 (Fixed Keys Constraint)** — T810A1 prompt instructions SHALL NOT direct LLM_Gastro to invent new Dynamic JSON keys at runtime. Key governance is owned by T810A2 per `T810A2-CON-005`.

* **T810A1-CON-005 (System Prompt Limit)** — The LLM_Gastro system prompt deployed to the ChatGPT custom GPT platform SHALL NOT exceed **8,000 characters** total.

---

### D. INT/CON Category Summary

**Enhanced Existing INT Items**:
| INT ID | Title | Enhancement | T810A2 Cross-Reference |
|:-------|:------|:-----------|:---------------------|
| INT-001 | Probe Triggering Integration | Added field classification mapping | T810A2-INT-001, T810A2-IF-004 |
| INT-003 | Memory Precedence Integration | Added conflict resolution phrasing | T810A2-INT-004, T810A2-CON-004 |
| INT-005 | Session Report Integration | Added aggregation format details | T810A2-INT-002, T810A2-INT-005 |

**New INT Items**:
| INT ID | Title | Purpose | T810A2 Cross-Reference |
|:-------|:------|:--------|:---------------------|
| INT-006 | Schema Loading Integration | Session initialization schema references | T810A2-INT-003 |
| INT-007 | Controlled Vocabulary Integration | Value set enforcement for Dynamic JSON | T810A2-IF-003, T810A2-IG-003 |

**New CON Items**:
| CON ID | Title | Purpose | T810A2 Cross-Reference |
|:-------|:------|:--------|:---------------------|
| CON-004 | Fixed Keys Constraint | Prohibit runtime key invention | T810A2-CON-005 |
| CON-005 | System Prompt Limit | Enforce 8,000 char MVP limit | — |

---

## V. SUBPHASE 1.4 ADDENDUM: GDR/ADR ITEM (Concept: III.B.3. Feature Architectural Decisions)

### A. T810A1-GDR
**Task 0 Verification (ADR-001 as SSOT)**:
- `T810A1-ADR-001 (9-Block Architecture Assignment)` in `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md` already contains the block-specific mapping and IG coverage matrix.
- As a result, individual IG/INT items in this proposal have been consolidated to remove block-applicability duplication and instead reference `T810A1-ADR-001`.

#### 1. Proposed Token-Optimized Replacement Body for `T810A1-GDR-001`

* **T810A1-GDR-001 (Tracking-First Clinical Protocol)** {#t810a1-gdr-001-tracking-first-clinical-protocol}

  **Context:** Research validation (`T810A1-RES-001`) supports a Tracking-First workflow as the safest and most reliable entry point for gastro conversational support with detailed protocol mechanics are maintained in `T810A1-NFR-001` and `T810A1-NFR-005 `

  **Decision:** Adopt **Tracking-First Clinical Protocol** as the canonical conversation architecture for `LLM_Gastro`, with `T810A1-NFR-001` and `T810A1-NFR-005` treated as the normative specifications for phase ordering and probe-before-coach gating.

  **Consequences:**
  - (+) Clear governance anchor for the workflow decision; implementation detail remains in NFRs
  - (+) Reduces duplicate protocol text and cross-artifact drift risk
  - (±) Requires following NFR links for full mechanics and examples

  **References:**
  `T810A1-NFR-001 (Protocol Reliability)`,
  `T810A1-NFR-005 (Probe Phase Enforcement)`,
  `T810A1-RES-001 (Execution Protocol Clinical Validation)`,
  `T810A-IG-005 (Memory Review Protocol)`

### B. T810A1-ADR

**Classification Note** (per Client QA Question 1):
- **Reclassified**: T810A1-GDR-003 → T810A1-ADR-001 (9-Block Architecture Assignment)
- **Rationale**: Structural/architectural decision (component boundaries, modular organization) per industry-standard ADR classification
- **Governance Model**: Per T102-STD-004, ADRs govern "architecture and design choices," GDRs govern "workflow and process standards"
- **Precedent**: T810A-ADR-001/002/003/004 establish architectural patterns (confidence, vocabulary, reporting, knowledge catalog)
- **Location**: `concept_T810-GASTRO.md` Section III.B.3 (Feature Architectural Decisions), not Request Section G

#### 1. ADR Index Table

| ADR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| T810A1-ADR-001 | 9-Block Architecture Assignment | Proposed | Client | 2025-12-09 | — | t810a1-adr-001-9-block-architecture-assignment |

#### 2. T810A1-ADR-001 Body

* **T810A1-ADR-001 (9-Block Architecture Assignment)** {#t810a1-adr-001-9-block-architecture-assignment}

  **Context:** T810A1-PROMPT requires development of a 9-block modular system prompt per `T810A1-NFR-003 (Prompt Maintainability)`. Each block corresponds to a specific Story (S01-S09) that specifies functional requirements for that block. Clear Story-to-Block assignment ensures modular development, traceability, and maintenance consistency per `T810A-QG-005 (Architecture Maintainability)`. Existing content in `gastro_system.md` v0.x provides baseline for Blocks 1-3. Without canonical block assignment, Phase 2 development risks scope drift and Story-Block misalignment.

  **Decision:** Adopt canonical 9-block architecture with explicit Story assignments and F-RID governance per block. Each block receives dedicated Story ID, development scope, and governing F-RID references as following specifications below

  **Specification:**

   **Block 1 — Project Context (Story: T810A1-S01)**
   - **Scope**: Diagnostic stance, privacy policy, operational constants (timezone, timestamp format)
   - **Development Status**: Baseline exists in `gastro_system.md` v0.x; review and align with Phase 1 F-RIDs
   - **Governing F-RIDs**: `IF-001` (Input Interface), `IF-002` (Output Interface), `IG-006` (Session Initialization operational constants reference)
   - **Story S10 Integration**: S10 (Metadata Header) FRs merge into S01 as YAML frontmatter specification; no separate block

   **Block 2 — Role Identity & Competencies (Story: T810A1-S02)**
   - **Scope**: Role mandate, key competencies, communication style per protocol phase (Engage, Analyze, Probe, Coach, Summarize)
   - **Development Status**: Baseline exists in `gastro_system.md` v0.x; review for IG-002/IG-003 alignment
   - **Governing F-RIDs**: `NFR-002` (Persona & Tone), `IG-002` (OARS Dialogue collaborative framing), `IG-003` (Epistemic Hedging confidence language), `GDR-001` (protocol phase tones)

   **Block 3 — Toolbox Declaration (Story: T810A1-S03)**
   - **Scope**: Tool declarations (ChatGPT native tools, external APIs)
   - **Development Status**: Deferred per `CON-003`; preserve placeholder
   - **Governing F-RIDs**: `CON-003` (Tooling Deferral to post-MVP)

   **Block 4 — Knowledge Base (Story: T810A1-S04)**
   - **Scope**: Knowledge type taxonomy (Internal Model, Custom Instructions, Project Knowledge, Memory, Web Search), authority hierarchy, schema references
   - **Development Status**: Requires full development; no baseline
   - **Governing F-RIDs**: `IF-005` (Session Context Injection), `IG-006` (Session Initialization schema loading), `IG-007` (Dynamic JSON template references), `INT-006` (Schema Loading Integration with T810A2 artifacts)

   **Block 5 — Execution Protocol (Story: T810A1-S05)**
   - **Scope**: 5-phase protocol (Tracking → Analyze → Probe → Coach → Summarize), protocol triggering (input-type detection), phase execution steps, gate enforcement, session initialization sequence
   - **Development Status**: Requires full development; highest complexity and F-RID consumption
   - **Governing F-RIDs**: `NFR-001` (Protocol Reliability), `NFR-004` (Protocol Triggering), `NFR-005` (Probe Enforcement), `GDR-001` (Tracking-First Protocol), `GDR-002` (Session Workflow Architecture), `IG-001` (Phase Gating), `IG-002` (OARS Dialogue), `IG-003` (Epistemic Hedging), `IG-004` (Protocol Triggering Logic), `IG-005` (Anti-Pattern detection awareness), `IG-006` (Session Initialization), `IG-007` (Dynamic JSON Generation), `INT-001` (Probe Triggering Integration)

   **Block 6 — Behavioral Guardrails (Story: T810A1-S06)**
   - **Scope**: Anti-pattern prohibitions, constraint enforcement (CON-001 to CON-004), gate compliance checks, safety boundaries
   - **Development Status**: Requires full development; no baseline
   - **Governing F-RIDs**: `CON-001` (Risk Acceptance), `CON-002` (Open Knowledge Base), `CON-003` (Tooling Deferral), `CON-004` (Fixed Keys), `IG-001` (Phase Gating enforcement rules), `IG-005` (Anti-Pattern Prohibitions primary home)

   **Block 7 — Quality & Success Criteria (Story: T810A1-S07)**
   - **Scope**: Verification checkpoints aggregated from E-QGs and IG-derived quality criteria, session quality checklist, output quality standards
   - **Development Status**: Requires full development; no baseline
   - **Governing F-RIDs**: E-QG inherited (`T810A-QG-001` to `T810A-QG-008`), IG-derived checkpoints from `IG-001` to `IG-007`

   **Block 8 — Exemplars (Story: T810A1-S08)**
   - **Scope**: Positive and negative dialogue examples demonstrating OARS dialogue, epistemic hedging, anti-pattern violations, gate phrasing, JSON generation
   - **Development Status**: Requires full development; no baseline
   - **Governing F-RIDs**: `IG-002` (OARS Dialogue demonstrations), `IG-003` (Epistemic Hedging phrasing demonstrations), `IG-005` (Anti-Pattern violation demonstrations)

   **Block 9 — I/O Specification (Story: T810A1-S09)**
   - **Scope**: Input interface (text + image parsing), output interface (Markdown primary), explicit classification confidence indicators, reporting trigger (/report command), Dynamic JSON output format, session report dual-format
   - **Development Status**: Requires full development; no baseline
   - **Governing F-RIDs**: `IF-001` to `IF-006` (all interface specifications), `IG-003` (confidence in output), `IG-007` (JSON output format), `INT-005` (Session Report dual-format), `INT-007` (Controlled Vocabulary Integration)

   **IG Coverage Matrix** (per Client QA Requirement — every Story must have ≥1 governing IG):
   - S01: `IG-006` | S02: `IG-002`, `IG-003` | S03: *None (deferred)* | S04: `IG-006`, `IG-007` | S05: `IG-001` to `IG-007` (all) | S06: `IG-001`, `IG-005` | S07: *Derived from all IGs* | S08: `IG-002`, `IG-003`, `IG-005` | S09: `IG-003`, `IG-007`

  **Consequences:**
  - (+) Clear modular boundaries per `T810A1-NFR-003`; enables isolated Story-level refinement post-Phase 2
  - (+) Traceability: Each Story maps to exactly one Block; each Block maps to exactly one Story (1:1 correspondence)
  - (+) Maintenance: Block-level edits localized per `T810A-QG-005`; reduces merge conflicts in multi-developer scenarios
  - (+) IG coverage verified: Every Story (except deferred S03) governed by ≥1 IG, ensuring implementation guidance completeness
  - (+) Phase 2 scope clarity: Blocks 1-3 baseline exists; Blocks 4-9 require full development
  - (±) S10 (Metadata Header) merged into S01; reduces block count from 10 to 9, simplifies architecture but merges two Story scopes
  - (-) High interdependency between Block 5 (S05) and Blocks 4, 6, 8, 9: S05 references S04 schema authority, S06 enforces S05 gates, S08 demonstrates S05 patterns, S09 aligns with S05 outputs; requires careful cross-block coordination in Phase 2
  - (-) Block 5 highest complexity: Consumes all IG-001 to IG-007 patterns; risk of bloat if not carefully scoped

  **References:**
  `T810A1-NFR-003 (Prompt Maintainability)`,
  `T810A-QG-005 (Architecture Maintainability)`,
  `T810A1-GDR-001 (Tracking-First Clinical Protocol)`,
  `T810A1-GDR-002 (Session Workflow Architecture)`,
  `T810A1-CON-003 (Tooling Deferral)`,
  `T102-STD-004 (Decision Records Index)`

---

## VI. MAPPING SUMMARY

| Phase 1 Deliverable | Target Document/Section | Status |
|:-------------------|:----------------------|:-------|
| Subphase 1.1: F-RID Inventory Review | Context for Subphases 1.2/1.3 | ✅ Completed |
| Subphase 1.1: ADR-001 (9-Block Architecture) | Concept: III.B.3 Feature Architectural Decisions | ✅ Specified |
| Subphase 1.2: IG-001 (Phase Gating Protocol) | F.6 Implementation Guidance (NEW) | ✅ Specified |
| Subphase 1.2: IG-002 (OARS Dialogue Pattern) | F.6 Implementation Guidance (NEW) | ✅ Specified |
| Subphase 1.2: IG-003 (Epistemic Hedging Protocol) | F.6 Implementation Guidance (NEW) | ✅ Specified |
| Subphase 1.2: IG-004 (Protocol Triggering Logic) | F.6 Implementation Guidance (NEW) | ✅ Specified |
| Subphase 1.2: IG-005 (Anti-Pattern Prohibitions) | F.6 Implementation Guidance (NEW) | ✅ Specified |
| Subphase 1.2: IG-006 (Session Initialization Sequence) | F.6 Implementation Guidance (NEW) | ✅ Specified |
| Subphase 1.2: IG-007 (Dynamic JSON Generation Pattern) | F.6 Implementation Guidance (NEW) | ✅ Specified |
| Subphase 1.3: INT-001 (ENHANCED) | F.7 Integration Notes (EXISTING) | ✅ Enhanced |
| Subphase 1.3: INT-003 (ENHANCED) | F.7 Integration Notes (EXISTING) | ✅ Enhanced |
| Subphase 1.3: INT-005 (ENHANCED) | F.7 Integration Notes (EXISTING) | ✅ Enhanced |
| Subphase 1.3: INT-006 (NEW) | F.7 Integration Notes (EXISTING) | ✅ Created |
| Subphase 1.3: INT-007 (NEW) | F.7 Integration Notes (EXISTING) | ✅ Created |
| Subphase 1.3: CON-004 (NEW) | F.3 Constraints (EXISTING) | ✅ Created |

---

## VI. COMPLIANCE VERIFICATION

### A. T102-STD-005 Standards Compliance

| Standard | Requirement | Verification |
|:---------|:-----------|:------------|
| FR-001 (ID Scope) | Feature IDs follow `T\d{3}[A-Z]\d` pattern | ✅ All IDs: `T810A1-*` |
| FR-004 (ID Categories) | IG/INT/CON tokens used correctly | ✅ IG (internal), INT (cross-feature), CON (boundary) |
| FR-005 (ID Title & Construction) | Format: `* **<ID> (<Title>)** — <description>` | ✅ All F-RIDs follow format |
| FR-006 (ID References) | Back-ticked formal/informal references | ✅ All cross-references back-ticked |
| FR-008 (INT Exception) | INT items MAY reference other Feature F-RIDs | ✅ INT-001/003/005/006/007 reference T810A2-INT-* |

### B. Phase 1 Plan Alignment

| Plan Section | Requirement | Verification |
|:-------------|:-----------|:------------|
| IV.A (Subphase 1.1) | F-RID inventory review | ✅ Section II.A-D |
| IV.B (Subphase 1.2) | Create 7+ T810A1-IG items | ✅ Section III.B (IG-001 to IG-008) |
| IV.C (Subphase 1.3) | Enhance 3 INT + create 2 INT + 2 CON | ✅ Section IV.A-C |
| Success Criteria | All F-RIDs follow T102-STD-005 | ✅ Verified in VI.A |
| Success Criteria | IG items reference T810A1-RES-001 | ✅ All IG items cite research |
| Success Criteria | INT items cross-reference T810A2-INT | ✅ All INT items cite T810A2 |

---

## VII. OPEN QUESTIONS FOR CLIENT REVIEW

## VIII. NEXT STEPS

### A. Immediate Actions (Current Session)

1. **Client Review**: Review all proposed F-RID bodies (Sections III & IV) for accuracy, completeness, and alignment
2. **Q&A Iteration**: Respond to open questions (Section VII) and provide clarifications/corrections
3. **Approval Gate**: Explicit client approval before Request population

### B. Request Population (Post-Approval)

4. **Section F.6 Creation**: Insert all 8 IG items into Request as new subsection
5. **Section F.7 Enhancement**: Replace INT-001, INT-003, INT-005 with enhanced versions; add INT-006, INT-007
6. **Section F.3 Enhancement**: Add CON-004 and CON-005 to Constraints subsection
7. **Governance Deduplication**: Update GDR-001 to remove NFR-001 duplication (see Section IX)
8. **Optional Version Bump**: Update Request version/date after approval

### C. Phase 2 Transition

9. **Draft System Prompt Generation**: Begin Phase 2 per plan Section V (Subphases 2.1-2.3)
10. **Execution Protocol Focus**: Prioritize the execution protocol content incorporating IG-001 to IG-007 patterns
11. **Validation**: Run Phase 2 validation checklist before final handoff

---

## IX. CHANGELOG

- **v1.0.6** (2025-12-12): IG self-sufficiency updates (workspace-only; SSOT pending approval):
  - **UPDATED**: IG-001 through IG-007 to be self-contained (operational rules + acceptance checks) without relying on any other proposal file
  - **REMOVED**: Cross-proposal pointers from IG bodies (workspace proposals are not SSOT)

- **v1.0.5** (2025-12-12): Phase 3 QA alignment refinements (workspace-only; SSOT pending approval):
  - **REFINED**: `T810A1-CON-005 (System Prompt Limit)` to remain a strict platform constraint only (8,000 chars)
  - **ADDED**: `T810A1-IG-008 (Hybrid Tiered Architecture for MVP Deployment)` as a separate IG item (Tier 1 ≤7,500 chars; Tier 2/3 packaging; governance traceability)
  - **UPDATED**: IG-001 through IG-007 to remove block-applicability duplication; block mapping remains governed by `T810A1-ADR-001`

- **v1.0.4** (2025-12-12): Phase 3 QA alignment (workspace-only; SSOT pending approval):
  - **ADDED**: `T810A1-CON-005 (System Prompt Limit)` as the governing constraint for the 8,000 character ChatGPT system prompt limit
  - **CONSOLIDATED**: IG-001 through IG-007 bodies to pointer-based guidance; detailed procedures/examples deferred to later-phase implementation artifacts
  - **STREAMLINED**: INT-001 through INT-007 bodies to remove explicit cross-reference bullets; cross-feature links are embedded directly in the INT body text
  - **REMOVED**: Block-applicability duplication from IG/INT items; block mapping remains governed by `T810A1-ADR-001`
  - **PROPOSED**: Token-optimized rewrite for `T810A1-GDR-001` using the standard Context/Decision/Consequences/References body format to remove overlap with `T810A1-NFR-001` (see Section IX)

- **v1.0.3** (2025-12-09): Client QA feedback round 3 integration:
  - **RECLASSIFIED**: T810A1-GDR-003 → T810A1-ADR-001 (9-Block Architecture Assignment):
    - **Classification Rationale**: Structural/architectural decision (component boundaries, modular organization) per industry-standard ADR classification
    - **Location Change**: From Request Section G (Feature Governance Decisions) to Concept Section III.B.3 (Feature Architectural Decisions)
    - **Governance Model**: Per T102-STD-004, ADRs govern "architecture and design choices," GDRs govern "workflow and process standards"
    - **Precedent**: T810A-ADR-001/002/003/004 establish architectural patterns; T810A1-ADR-001 follows this pattern
  - **UPDATED**: All cross-references from `T810A1-GDR-003` to `T810A1-ADR-001` (mapping summary, proposal references)
  - **UPDATED**: Section V title changed from "NEW GDR ITEM" to "NEW ADR ITEM (Concept: III.B.3)"
  - **UPDATED**: Mapping Summary table to reflect Concept document as target location

- **v1.0.2** (2025-12-09): Client QA feedback round 2 integration:
  - **RESTRUCTURED**: T810A1-GDR-003 to follow `T102-STD-004` governance format:
    - Added GDR Index Table (ID, Title, Status, Owner, Effective, Supersedes, Anchor)
    - Restructured body with Context, Decision, Consequences, References sections
    - **Decision section** now outlines each block separately (not grouped in table) with Story ID, scope, development status, and governing F-RID references per block
  - **RATIONALE**: Per `T102-STD-004-FR-002` (Decision Records Body), GDR bodies must follow structured format with individual block specifications

- **v1.0.1** (2025-12-09): Client QA feedback round 1 integration:
  - **ADDED**: T810A1-GDR-003 (9-Block Architecture Assignment) to Section V — establishes canonical Story-to-Block mapping and IG coverage matrix per client requirement
  - **SIMPLIFIED**: T810A1-CON-004 to high-level boundary only; implementation details moved to IG-007 and INT-007
  - **ENHANCED**: All IG items (IG-001 to IG-007) with initial block mapping references per T810A1-GDR-003
  - **REMOVED**: Open questions section (client answers received: A=approved, B=prompt-based sufficient, C=mandatory-only approved, D=qualitative sufficient)
  - **UPDATED**: Mapping Summary to include GDR-003

- **v1.0.0** (2025-12-09): Initial Phase 1 proposal creation. Completes Subphase 1.1 (F-RID Inventory Review), Subphase 1.2 (7 IG items specified), and Subphase 1.3 (3 INT enhanced + 2 INT created + 1 CON created). All F-RIDs follow T102-STD-005 standards. Research-driven (T810A1-RES-001) and handoff-driven (T810A1-NOTE-001) implications integrated.
