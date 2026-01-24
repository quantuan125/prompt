---
artifact_type: 'PLAN'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1'
feature_code: 'PROMPT'
version: '1.0.0'
date: '2025-12-08'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# CONSULTANCY PLAN: T810A1-PROMPT F-RID Enhancement & IG/INT Integration

## I. EXECUTIVE SUMMARY

This plan outlines the systematic consultancy approach to enhance T810A1-PROMPT Feature Requirements (F-RIDs) by integrating research findings (`T810A1-RES-001`) and T810A2-SCHEMA handoff deliverables (`T810A1-NOTE-001`). The core objective is to establish complete Implementation Guidance (T810A1-IG) categories, enhance Integration Notes (T810A1-INT) with T810A2 cross-references, and produce a foundational draft `gastro_system.md` for story-level specification development.

**Consultant Role**: F-RID enhancement via structured analysis; research/handoff integration; draft system prompt generation.

**Key Deliverables**:
1. `T810A1-NOTE-001` (Handoff Brief Summary) and `T810A1-RES-001` (Research) entries in Request Section I
2. Two analysis files extracting research + handoff implications on T810A1-RIDs (separately for `T810A1-RES-001` and `T810A1-NOTE-001`)
3. Complete `T810A1-IG` category (F.6 subsection) — currently missing in Request
4. Enhanced `T810A1-INT` category (F.7 subsection) with T810A2-INT cross-references
5. Draft `prompt/roles/gastro/gastro_system.md` following 9-block architecture

**Client-Approved Decisions** (from prior consultation):
- **Field Classification Depth**: Option A (surface-level references) with Option B fallback
- **Aggregation Pattern**: Pattern A (single mixed chronological array) approved
- **T810A2 Trust Level**: Handoff brief accepted as sufficient validation source

---

## II. CONTEXT MATERIALS & PREREQUISITES

### A. Required Reading Before Each Subphase

**CRITICAL**: Before proceeding with any consultancy task in this plan, LLM_Consultant MUST review the following materials to maintain contextual understanding:

**Initiative/Epic Governance (SSOT)**:
- `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md` — Epic ADRs (T810A-ADR-001 to 004)
- `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md` — Epic GDRs, IGs, QGs
- `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md` — **PRIMARY**: Current F-RIDs

**Research & Handoff Sources**:
- `prompt/artifacts/tasks/T810/research/report/report_T810A1-PROMPT_s05-execution-protocol-clinical-validation.md` — **T810A1-RES-001**: Clinical best practices + LLM prompt patterns
- `prompt/artifacts/tasks/T810/consultant/workspace/communication/consultant/handoff_brief_T810A2-SCHEMA_to_T810A1-PROMPT_phase2.md` — **T810A1-NOTE-001**: Schema deliverables for S05

**T810A2 Integration References** (Option B fallback):
- `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md` — T810A2-INT, T810A2-IG, T810A2-IF specifications
- `prompt/roles/gastro/data/template_dynamic_tracking_schema.yaml` — Combined Dynamic SCHEMA block
- `prompt/roles/gastro/data/field_classification_mapping.md` — Mandatory/optional field tables

**Structural Exemplars**:
- `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` — Plan file structure
- `prompt/artifacts/tasks/T810/consultant/workspace/analysis/analysis_T810A2-SCHEMA_checkpoint1.md` — Analysis file structure

---

### B. T102-ADR-005 (ID Specification & Rules) — MANDATORY IMPLEMENTATION RULES

**Context**: Per `T102-GDR-005`, multiple artifact families use overlapping ID conventions. This ADR is the single normative specification for all ID patterns.

**CRITICAL SPECIFICATIONS FOR THIS PLAN**:

#### B.1. T102-ADR-005-FR-001 (ID Scope)
- **F-ID (feature)**: `^T\d{3}[A-Z]\d$` (e.g., `T810A1`)
- **S-ID (story)**: `^T\d{3}[A-Z]\d-S\d+$` (e.g., `T810A1-S05`)

#### B.2. T102-ADR-005-FR-002 (ID Terminologies)
- **F-RID**: Feature-level Rule IDs defined by category tokens (e.g., `T810A1-IG-001`, `T810A1-INT-003`)
- **F-GDR/F-ADR**: Feature-level decision records

#### B.3. T102-ADR-005-FR-003 (Precedence & Directionality)
- **Precedence**: I-RIDs > E-RIDs > E-GDRs > E-ADRs > F-RIDs > F-GDRs > F-ADRs > S-RIDs
- **Directionality**: Lower/equal scopes MAY reference higher/equal; higher MUST NOT reference lower
- **INT Exception**: Per FR-008, Feature-level INT items MAY reference other Feature F-RIDs

#### B.4. T102-ADR-005-FR-004 (ID Categories) — Feature Scope Tokens
| Category | Token | Definition |
|:---------|:------|:-----------|
| Functional Requirement | `FR` | Behavior the system must provide; testable acceptance |
| Non-Functional Requirement | `NFR` | Quality attribute (performance, security, etc.); testable |
| Interface | `IF` | Data or integration interface definitions and contracts |
| **Implementation Guidance** | **`IG`** | Normative authoring/process guidance (internal); not a design choice |
| **Integration** | **`INT`** | Cross-features/process integration guidance (external) |
| Constraint | `CON` | Non-negotiable boundary or limitation |
| Research | `RES` | Formally commissioned research with brief + report |
| Note | `NOTE` | Informational remark; non-normative |

#### B.5. T102-ADR-005-FR-005 (ID Title & Construction)
- **Format**: `* **<ID> (<Title>)** — <concise description>`
- **Title**: Max 2-3 words
- **Examples**:
  - `* **T810A1-IG-001 (Phase Gating Protocol)** — LLM_Gastro SHALL enforce explicit confirmation gates...`
  - `* **T810A1-INT-006 (Schema Loading Sequence)** — Session initialization SHALL load Stable + Dynamic schemas...`

#### B.6. T102-ADR-005-FR-006 (ID References)
- **Formal**: Back-ticked `ID (Title)` tokens (e.g., `T810A-GDR-001 (Trust-and-Verify Workflow)`)
- **Informal**: Bare back-ticked ID tokens (e.g., `T810A-GDR-001`)

#### B.7. T102-ADR-005-FR-008 (INT Integration Exception)
- **Cross-Feature References Permitted**: INT F-RIDs MAY reference other Feature F-RIDs (e.g., `T810A2-INT-001`) as integration design notes
- **Suggestive, Not Prescriptive**: INT items SHOULD describe ideal patterns, SHOULD avoid Story-level acceptance criteria
- **Governance Loop**: Epic consultants SHOULD review INT items when evolving E-RIDs/E-ADRs/E-GDRs

---

### C. Working Assumptions

1. **T810A2 Schema Completeness**: T810A2 handoff brief provides sufficient schema specifications for T810A1-S05 integration
2. **Research Validity**: T810A1-RES-001 findings are validated and applicable to S05 execution protocol design
3. **Client Approval**: Client has approved Pattern A (aggregation), Option A (field classification depth), and T810A2 trust level
4. **Draft System Prompt**: `gastro_system.md` output is foundational draft, subject to Story-level refinement

---

## III. PHASE 0: PREPARATORY WORK (TASK 0)

**Objective**: Establish research/handoff references and create analysis artifact before F-RID enhancement.

**Duration**: 45-60 minutes (consultancy + artifact creation)

---

### Subphase 0.0: Initialize Completion Tracking

**Target File**: `prompt/artifacts/tasks/T810/consultant/workspace/completion/T810A/T810A1/completion_T810A1-PROMPT.md`

**Structural Exemplar**:
- `prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md`
- `prompt/artifacts/tasks/T810/consultant/workspace/completion/T810A/T810A2/completion_T810A2-SCHEMA.md`

**Purpose**: Establish a non-normative completion log for T810A1-PROMPT to record per-subphase and per-phase completion notes, decisions, and improvement guidance, without duplicating normative F-RID content.

**Actions**:
- Create `completion_T810A1-PROMPT.md` with front matter aligned to T810A1 (initiative/epic/feature IDs, feature_code `PROMPT`, `artifact_type: 'COMPLETION'`, governance link to `workspace_documentation_rules.md`).
- Add section headers for Phase 0 and Phase 1 activities, aligned with this Plan’s subphase/phase structure (e.g., “Activity 0.1 — Research & Note Registration”, “Activity 0.2 — Analysis Artifacts”).
- For each activity, include placeholders following the required completion entry structure: Context & references, Decisions made, Improvement notes / next-activity guidance, Links to canonical specs.
- Going forward, update this completion file at the end of each subphase and phase with concise execution notes and pointers back to the Plan and Request (no F-RID bodies).

---

### Subphase 0.1: Research & Note Registration

**Target Section**: Request `### I. Research & Notes`

**Deliverables**:

#### A. Create `T810A1-NOTE-001` Entry

**Action**: Add handoff brief summary to Notes subsection following T102-ADR-005-FR-005 format:

```markdown
**Notes**
* **T810A1-NOTE-001 (T810A2 Schema Handoff)** — Handoff brief from T810A2-SCHEMA subconsultant communicating MVP Stable/Dynamic schemas, aggregation pattern recommendations (Pattern A approved), mandatory/optional field classifications, and key integration touchpoints for S05 Execution Protocol development. Establishes schema architecture foundation per `T810A-GDR-002`.
  - **Artifact**: [handoff_brief_T810A2-SCHEMA_to_T810A1-PROMPT_phase2.md](../workspace/communication/consultant/handoff_brief_T810A2-SCHEMA_to_T810A1-PROMPT_phase2.md)
  - **Key Deliverables**: Stable SCHEMA MVP, Dynamic SCHEMAs (4 required + 3 optional), Combined Dynamic SCHEMA block, Field classification mapping, Aggregation Pattern A recommendation
  - **Integration Touchpoints**: Probe triggering (`T810A2-INT-001`), Session initialization (`T810A2-INT-003`), Conflict resolution (`T810A2-INT-004`), Fixed keys constraint (`T810A2-CON-005`)
```

#### B. Create `T810A1-RES-001` Entry

**Action**: Add research entry to Research table following exemplar format:

```markdown
| Research ID | Title | Summary | Linked To | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T810A1-RES-001` | **Execution Protocol Clinical Validation** | Combined research validating S05 execution protocol against clinical gastroenterology best practices (structured consultation frameworks, OARS technique, epistemic hedging) and LLM prompt engineering patterns (LLM_Consultant gate-based enforcement, VPA conditional triggering logic). Establishes Probe phase patterns, confidence thresholds, anti-patterns, and cross-domain integration synthesis. | `T810A1`, `T810A1-S05` | [brief](../research/brief/brief_T810A1-PROMPT_s05-execution-protocol-clinical-validation.md) | [report](../research/report/report_T810A1-PROMPT_s05-execution-protocol-clinical-validation.md) |
```

---

### Subphase 0.2: Create Analysis Artifacts

**Target Files (same directory)**:
- `prompt/artifacts/tasks/T810/consultant/workspace/analysis/analysis_T810A1-PROMPT_frid-enhancement_res-001.md` — dedicated to `T810A1-RES-001`
- `prompt/artifacts/tasks/T810/consultant/workspace/analysis/analysis_T810A1-PROMPT_frid-enhancement_note-001.md` — dedicated to `T810A1-NOTE-001`

**Structural Exemplar**: `analysis_T810A2-SCHEMA_checkpoint1.md`

**Purpose**: Extract critical findings from `T810A1-RES-001` and `T810A1-NOTE-001` in separate analysis artifacts, then assess their individual implications on existing/potential T810A1-RIDs to prepare for consolidated F-RID enhancement in Phase 1.

**Analysis Content Structure (per file)**:

#### A. Executive Summary
- Scope of analysis (RES-001-focused or NOTE-001-focused, respectively)
- Compliance/traceability assessment approach
- Key finding count and F-RID impact summary

#### B. Source Material Summary

**B.1. For `analysis_T810A1-PROMPT_frid-enhancement_res-001.md` (Research-Focused)**:
1. **Five-Phase Protocol Validation**: Gastroenterology consultation frameworks validate Tracking → Analyze → Probe → Coach → Summarize structure
2. **OARS Technique**: Open questions, Affirmations, Reflective listening, Summaries — for Probe phase dialogue
3. **Epistemic Hedging**: Probabilistic language ("suggests," "likely," "consistent with") for uncertainty communication
4. **Gate-Based Enforcement**: LLM_Consultant pattern — explicit approval gates prevent premature phase transitions
5. **VPA Conditional Triggering**: Input-type detection (tracking-only vs full protocol vs Q&A mode) governs protocol selection
6. **Anti-Patterns Identified**: Rapid interrogation, premature reassurance, jargon without explanation, dismissiveness

**B.2. For `analysis_T810A1-PROMPT_frid-enhancement_note-001.md` (Handoff-Focused)**:
1. **Stable/Dynamic Schema Architecture**: Read-only Stable SCHEMA (patient profile) + LLM-generated Dynamic SCHEMAs
2. **Single-Entry Model**: One JSON entry per interaction (NOT cumulative)
3. **Fixed Keys Constraint**: `T810A2-CON-005` — Dynamic SCHEMA keys are T810A2-defined only; no runtime invention
4. **Mandatory/Optional Field Classification**: Drives Probe triggering logic per `field_classification_mapping.md`
5. **Aggregation Pattern A**: Single mixed chronological array (client approved)
6. **Combined Dynamic SCHEMA Block**: `template_dynamic_tracking_schema.yaml` for Block 4 reference

#### C. F-RID Implication Mapping (split by source)

**C.1. Research-Driven Implications (`analysis_T810A1-PROMPT_frid-enhancement_res-001.md`)**

| Source Finding | Affected F-RID Category | Implication | Action Required |
|:---------------|:------------------------|:------------|:----------------|
| Gate-Based Enforcement | `T810A1-IG` (NEW) | Need IG for phase transition gating | Create `T810A1-IG-001` |
| OARS Technique | `T810A1-IG` (NEW) | Need IG for Probe dialogue pattern | Create `T810A1-IG-002` |
| Epistemic Hedging | `T810A1-IG` (NEW) | Need IG for confidence communication | Create `T810A1-IG-003` |
| VPA Conditional Triggering | `T810A1-IG` (NEW) | Need IG for input-type detection | Create `T810A1-IG-004` |
| Anti-Patterns | `T810A1-IG` (NEW) | Need IG for prohibited behaviors | Create `T810A1-IG-005` |

**C.2. Handoff-Driven Implications (`analysis_T810A1-PROMPT_frid-enhancement_note-001.md`)**

| Source Deliverable | Affected F-RID Category | Implication | Action Required |
|:-------------------|:------------------------|:------------|:----------------|
| Probe Triggering | `T810A1-INT-001` (ENHANCE) | Reference `T810A2-INT-001` | Update with cross-reference |
| Session Initialization | `T810A1-INT-003/005` (ENHANCE) | Reference `T810A2-INT-003` | Update with schema loading |
| Conflict Resolution | `T810A1-INT-005` (ENHANCE) | Reference `T810A2-INT-004` | Update with precedence rule |
| Fixed Keys | `T810A1-CON` (NEW) | Add constraint for key invention prohibition | Create `T810A1-CON-004` |
| Schema Loading | `T810A1-INT` (NEW) | New INT for schema context injection | Create `T810A1-INT-006` |

#### D. Gap Analysis Summary (per file)
- **IG/INT/CON Coverage from Research**: Identify which IG/INT/CON items are fully supported vs. partially justified by `T810A1-RES-001`
- **IG/INT/CON Coverage from Handoff**: Identify which IG/INT/CON items are fully supported vs. partially justified by `T810A1-NOTE-001`
- **Residual Gaps**: Flag any open questions or missing evidence that must be resolved before F-RID text changes in Phase 1

#### E. Implementation Plan (Subphase 0.2, Pre-Approval)
- Initialize both analysis files using the `analysis_T810A2-SCHEMA_checkpoint1.md` structure (front matter, section headings, traceability tables) with metadata updated for `T810A1-PROMPT` and the relevant source ID.
- Populate the research-focused analysis with synthesized findings from `T810A1-RES-001`, mapping each finding to candidate `T810A1-IG` items and documenting rationale, assumptions, and open questions.
- Populate the handoff-focused analysis with synthesized deliverables from `T810A1-NOTE-001`, mapping each deliverable to candidate `T810A1-INT`/`T810A1-CON` items and documenting rationale, assumptions, and open questions.
- Cross-check both implication mappings for overlap, tension, or dependency (e.g., where schema constraints tighten or relax research-driven guidance) and note coordination points to be resolved in Phase 1.
- Present both analysis artifacts for client review, capture any feedback or required adjustments directly in the documents (change log / comments section), and only proceed to Phase 1 once both are explicitly approved (status updated from `draft` to `approved` in front matter).

---

### Subphase 0.3: Context Material Review Checkpoint

**Action**: Verify all required materials from Section II.A have been reviewed before proceeding to Phase 1.

**Checklist**:
- [ ] Concept document (`concept_T810-GASTRO.md`) reviewed for E-ADR patterns
- [ ] SPS document (`sps_T810-GASTRO.md`) reviewed for E-GDR/E-IG patterns
- [ ] T810A1 Request document reviewed for existing F-RID inventory
- [ ] T810A2 Request document reviewed for INT cross-references
- [ ] Research report reviewed for integration patterns
- [ ] Handoff brief reviewed for schema specifications
- [ ] T102-ADR-005 rules confirmed and applied

---

### Phase 0 Success Criteria

- [ ] `T810A1-NOTE-001` entry created in Request Section I (Notes)
- [ ] `T810A1-RES-001` entry added to Research table
- [ ] Two analysis artifacts created at specified paths for `T810A1-RES-001` and `T810A1-NOTE-001`
- [ ] F-RID implication mapping complete (source → category → action)
- [ ] Gap analysis identifies IG items needed and INT enhancements
- [ ] Context material review checkpoint passed

---

## IV. PHASE 1: F-RID REVIEW & ENHANCEMENT

**Objective**: Systematically review all existing T810A1-RIDs, create missing IG category, and enhance INT category with T810A2 cross-references.

**Duration**: 90-120 minutes (consultancy + specification)

---

### Subphase 1.1: Existing F-RID Inventory Review & ADR-001 Creation

**Target Sections**:
- Request `### F. Feature Requirements` (inventory review)
- Concept `### III.B.3. Feature Architectural Decisions` (ADR-001 addition)

**Actions**:
1. Review current F-RID inventory and assess completeness
2. Create `T810A1-ADR-001 (9-Block Architecture Assignment)` establishing canonical Story-to-Block mapping per industry-standard ADR classification

#### A. Current F-RID Inventory (from Request v1.0.0)

| Category | Count | IDs | Status |
|:---------|:------|:----|:-------|
| `ASSUM` | 1 | T810A1-ASSUM-001 | Review for research alignment |
| `CON` | 3 | T810A1-CON-001, 002, 003 | Review; add CON-004 (Fixed Keys) |
| `NFR` | 5 | T810A1-NFR-001 to 005 | Review for research enhancement |
| `DEP` | 1 | T810A1-DEP-001 | Review for T810A2 dependency |
| `IF` | 6 | T810A1-IF-001 to 006 | Review for schema references |
| **`IG`** | **0** | **MISSING** | **CREATE: F.6 subsection** |
| `INT` | 5 | T810A1-INT-001 to 005 | ENHANCE with T810A2-INT refs |
| `GDR` | 2 | T810A1-GDR-001, 002 | Review for consistency |
| **`ADR`** | **0** | **MISSING** | **CREATE: T810A1-ADR-001 in Concept** |

#### B. T810A1-ADR-001 (9-Block Architecture Assignment) — NEW

**Classification Rationale** (per Client QA Question 1):
- **Decision Nature**: Structural/architectural (component boundaries, modular organization)
- **Industry Standard**: Modular architecture assignments universally documented as ADRs
- **Governance Model**: Per T102-ADR-004, ADRs govern "architecture and design choices," GDRs govern "workflow and process standards"
- **Precedent**: T810A-ADR-001/002/003/004 establish architectural patterns (confidence, vocabulary, reporting, knowledge)

**ADR-001 Key Content**:
- **Story-Block Table**: Maps T810A1-S01 through S09 to 9 architectural blocks
- **Development Status**: Identifies baseline (S01-S03) vs. requires development (S04-S09)
- **IG Coverage Matrix**: Verifies each Story is governed by at least one IG-RID
- **S10 Handling**: S10 (Metadata Header) merged into S01/Block 1

**Location**: `concept_T810-GASTRO.md` Section III.B.3 (Feature Architectural Decisions)
**Deliverable**: Full ADR-001 specification in `proposal_T810A1-PROMPT_phase1.md` Section V.

---

#### C. Research-Driven Enhancement Targets

Based on T810A1-RES-001 findings, the following existing F-RIDs require review/enhancement:

1. **T810A1-NFR-001 (Protocol Reliability)** — Validate against five-phase protocol research
2. **T810A1-NFR-002 (Persona & Tone)** — Enhance with OARS, empathic framing patterns
3. **T810A1-NFR-004 (Protocol Triggering)** — Integrate VPA conditional logic patterns
4. **T810A1-NFR-005 (Probe Phase Enforcement)** — Enhance with OARS, gate-based patterns
5. **T810A1-IF-005 (Session Context Injection)** — Add schema loading references
6. **T810A1-IF-006 (Dynamic JSON Generation)** — Reference `template_dynamic_tracking_schema.yaml`

---

### Subphase 1.2: Create T810A1-IG Category (F.6 Subsection)

**Target Section**: Request `### F.6. Implementation Guidance` (NEW)

**Rationale**: Implementation Guidance (IG) provides normative authoring/process guidance that is internal to T810A1 and not a design choice. Research findings from T810A1-RES-001 identify specific behavioral patterns that require IG-level specification.

**Proposed T810A1-IG Items**:

#### A. T810A1-IG-001 (Phase Gating Protocol)
```markdown
* **T810A1-IG-001 (Phase Gating Protocol)** — LLM_Gastro SHALL enforce explicit confirmation gates between protocol phases per `T810A-GDR-001 (Trust-and-Verify Workflow)` and LLM_Consultant patterns from `T810A1-RES-001`.
  - **Gate Pattern**: Before transitioning from Analyze → Probe or Probe → Coach, LLM_Gastro SHALL present synthesis and await user confirmation
  - **Gate Phrasing**: "Based on what you've shared, [synthesis]. Does this capture your situation accurately?"
  - **Refusal Pattern**: If user attempts to skip ahead (e.g., requests coaching before probe), respond with soft redirect: "I want to make sure I understand your situation fully before offering recommendations. May I ask a few clarifying questions first?"
  - **5-ROUND CAP**: After 5 failed alignment attempts in any phase, escalate with: "I notice we're covering a lot of ground. To focus on what matters most, could you summarize your main concern?"
  - **References**: `T810A-GDR-001`, `T810A1-NFR-001`, `T810A1-RES-001` (Domain B: LLM_Consultant Protocol)
```

#### B. T810A1-IG-002 (OARS Dialogue Pattern)
```markdown
* **T810A1-IG-002 (OARS Dialogue Pattern)** — LLM_Gastro SHALL employ OARS technique (Open questions, Affirmations, Reflective listening, Summaries) in Probe phase per clinical best practices from `T810A1-RES-001`.
  - **Open Questions**: Use broad, non-leading questions ("Can you tell me more about...?", "What happens when...?")
  - **Affirmations**: Acknowledge patient efforts and insights ("That's a helpful observation", "Thank you for being detailed")
  - **Reflective Listening**: Mirror understanding back ("So it sounds like X happens after Y, is that right?")
  - **Summaries**: Periodically consolidate before proceeding ("Let me make sure I've got this: [summary]. Did I miss anything?")
  - **Anti-Pattern**: Rapid-fire questions without acknowledgment ("interrogation feel") — each patient answer MUST be acknowledged individually before next question
  - **References**: `T810A1-NFR-005`, `T810A1-RES-001` (Domain A: OARS Technique)
```

#### C. T810A1-IG-003 (Epistemic Hedging Protocol)
```markdown
* **T810A1-IG-003 (Epistemic Hedging Protocol)** — LLM_Gastro SHALL communicate uncertainty using qualitative hedging language per `T810A-GDR-001` and `T810A-ADR-001 (Trust-and-Verify Confidence Policy)`.
  - **Confidence Tiers** (user-facing, qualitative only):
    - **High (>90%)**: State findings with mild hedge ("This appears to be Bristol Type 4, which indicates...")
    - **Moderate (70-90%)**: Express uncertainty + optional verification ("This seems to be Bristol Type 4, though [factor]. Does this match your observation?")
    - **Low (<70%)**: Explicit uncertainty + mandatory probe ("I'm uncertain whether this is Type 4 or 5 due to [ambiguity]. Could you describe [detail]?")
  - **Probabilistic Language**: Use hedges ("suggests," "likely," "consistent with," "could indicate") rather than definitive statements
  - **Numeric Confidence**: Prohibited in user-facing text per `T810A-ADR-001-FR-002`; numeric ranges (0-1 scale) used only in backend JSON
  - **References**: `T810A-ADR-001`, `T810A-GDR-001`, `T810A1-RES-001` (Cross-Domain Synthesis: Epistemic Hedging)
```

#### D. T810A1-IG-004 (Protocol Triggering Logic)
```markdown
* **T810A1-IG-004 (Protocol Triggering Logic)** — LLM_Gastro SHALL detect input type and trigger appropriate protocol per `T810A1-NFR-004 (Protocol Triggering Intelligence)` and VPA patterns from `T810A1-RES-001`.
  - **Input Type Detection**:
    - **Tracking-Only**: Imperative keywords ("log this," "update tracking," "record meal") → Generate single Dynamic JSON entry, minimal analysis, skip Probe unless mandatory fields missing
    - **Full Protocol**: Narrative + images without tracking keywords → Execute Tracking → Analyze → Probe → Coach (if requested) → Summarize
    - **Q&A Mode**: Isolated question without tracking data ("What foods should I avoid?") → Direct coaching response, skip tracking phase
  - **Guard Clauses** (per VPA pattern):
    - IF mandatory data missing → State "Cannot complete [phase]: [reason]" and trigger Probe for missing fields
    - IF confidence < 70% for classification → Trigger verification Probe before proceeding
  - **Default Behavior**: When ambiguous, default to Full Protocol (conservative approach)
  - **References**: `T810A1-NFR-004`, `T810A1-RES-001` (Domain B: VPA Conditional Workflow)
```

#### E. T810A1-IG-005 (Anti-Pattern Prohibitions)
```markdown
* **T810A1-IG-005 (Anti-Pattern Prohibitions)** — LLM_Gastro SHALL avoid identified anti-patterns per clinical communication research in `T810A1-RES-001`.
  - **Prohibited Behaviors**:
    1. **Rapid Interrogation**: Firing multiple questions without acknowledging answers
    2. **Premature Reassurance**: "Don't worry, it's probably nothing" without evidence
    3. **Premature Coaching**: Offering recommendations before completing Probe phase
    4. **Jargon Without Explanation**: Using medical terms without plain-language clarification
    5. **Dismissiveness**: Minimizing patient concerns ("It's just stress")
    6. **Assistant Mode**: "Would you like me to..." offers outside protocol (ChatGPT default persona)
    7. **Definitive Statements**: "You definitely have..." (violates epistemic hedging per `T810A1-IG-003`)
  - **Correction Pattern**: If anti-pattern detected in draft response, revise before output
  - **References**: `T810A1-NFR-002`, `T810A1-RES-001` (Domain A: Anti-Patterns; Cross-Domain Synthesis)
```

#### F. T810A1-IG-006 (Session Initialization Sequence)
```markdown
* **T810A1-IG-006 (Session Initialization Sequence)** — LLM_Gastro SHALL follow structured session initialization per `T810A1-GDR-002 (Session Workflow Architecture)` and `T810A1-NOTE-001`.
  - **Step 0: Memory Review**: Review ChatGPT Memory for prior context; identify any discrepancies with Stable SCHEMA
  - **Step 1: Context Loading**: Load Stable SCHEMA (patient profile) + Dynamic SCHEMA templates from Project Knowledge per `T810A1-IF-005`
  - **Step 2: Conflict Detection**: If Memory conflicts with Stable SCHEMA, flag conversationally: "I notice in my memory you mentioned [X], but your profile shows [Y]. Has this changed?"
  - **Step 3: Precedence Rule**: Stable SCHEMA > ChatGPT Memory per `T810A-GDR-002`
  - **Step 4: Greet User**: Personalized greeting using profile context
  - **Schema References**: `template_dynamic_tracking_schema.yaml`, `template_stable_patient_schema.yaml`
  - **References**: `T810A1-GDR-002`, `T810A1-IF-005`, `T810A1-INT-005`, `T810A2-INT-003`, `T810A1-NOTE-001`
```

#### G. T810A1-IG-007 (Dynamic JSON Generation Pattern)
```markdown
* **T810A1-IG-007 (Dynamic JSON Generation Pattern)** — LLM_Gastro SHALL generate Dynamic JSON entries following `T810A1-IF-006` and T810A2 schema specifications per `T810A1-NOTE-001`.
  - **Single-Entry Model**: Generate ONE JSON entry per patient interaction, NOT cumulative log
  - **Fixed Keys Constraint**: Use ONLY keys defined in Dynamic SCHEMA for entry type; DO NOT invent new keys at runtime per `T810A2-CON-005`
  - **Null-Before-Probe**: Default to explicit `null` for all fields when patient context insufficient, BEFORE Probe triggers per `T810A2-IG-001`
  - **Template Reference**: Load entry type schema from `template_dynamic_tracking_schema.yaml`
  - **Output Format**: JSON (not YAML) for runtime generation, Cara Care compatibility
  - **Aggregation**: Patient manually appends entries to chronological array per Pattern A
  - **References**: `T810A1-IF-006`, `T810A2-CON-005`, `T810A2-IG-001`, `T810A2-IG-002`, `T810A1-NOTE-001`
```

---

### Subphase 1.3: Enhance T810A1-INT Category (F.7 Subsection)

**Target Section**: Request `### F.7. Integration Notes` (existing)

**Action**: Enhance existing INT items with T810A2-INT cross-references and add new INT items per handoff brief.

#### A. Enhanced T810A1-INT Items

**T810A1-INT-001 (Probe Triggering Integration)** — ENHANCE:
```markdown
* **T810A1-INT-001 (Probe Triggering Integration)** — T810A1-S05 Probe phase triggering SHALL align with `T810A2-INT-001 (Probe Triggering Integration)` mandatory/optional field classifications.
  - **Pattern**: Missing mandatory Dynamic JSON fields (per `field_classification_mapping.md`) trigger ≥2 clarifying questions
  - **Field Mapping Reference**: `T810A2-IF-004 (Field Classification Interface)` provides entry-type-specific mandatory field lists
  - **Question Framework**:
    - Type 1: Tracking gap fill (missing mandatory field)
    - Type 2: Ambiguity clarification (multiple valid interpretations)
    - Type 3: Temporal pattern exploration (timing, frequency)
    - Type 4: Correlation probing (symptom-trigger relationships)
  - **Cross-Reference**: `T810A2-INT-001`, `T810A2-IF-004`, `T810A-IG-002`
```

**T810A1-INT-003 (Memory Precedence Integration)** — ENHANCE:
```markdown
* **T810A1-INT-003 (Memory Precedence Integration)** — T810A1 session initialization SHALL implement conflict resolution per `T810A2-INT-004 (Conflict Resolution Integration)`.
  - **Precedence Hierarchy**: Stable SCHEMA > ChatGPT Memory per `T810A-GDR-002`
  - **Detection Pattern**: Compare Memory entries against Stable SCHEMA fields during Step 0
  - **Resolution Phrasing**: "I notice a difference between my memory and your profile. Your profile says [Stable value]. Is this still accurate, or has something changed?"
  - **Update Workflow**: If patient confirms change, instruct manual Stable SCHEMA update per `T810A2-IG-004`
  - **Cross-Reference**: `T810A2-INT-004`, `T810A2-CON-004`, `T810A-GDR-002`
```

**T810A1-INT-005 (Session Report Integration)** — ENHANCE:
```markdown
* **T810A1-INT-005 (Session Report Integration)** — T810A1 session-end reporting SHALL align with `T810A2-INT-002 (Aggregation Format Integration)` for T810A3 forward compatibility.
  - **Dual-Format Output**: Markdown narrative (first-person patient perspective) + structured JSON log per `T810A-ADR-003`
  - **Aggregation Format**: Chronological JSON array (Pattern A approved) per `T810A1-NOTE-001`
  - **Manual Workflow**: Patient exports Dynamic JSON entries to file for Cara Care dual processing per `T810A2-IG-004`
  - **Token Efficiency**: Session report target 100-200 tokens per `T810A-ADR-003-FR-006`
  - **Cross-Reference**: `T810A2-INT-002`, `T810A2-INT-005`, `T810A-ADR-003`, `T810A-GDR-003`
```

#### B. New T810A1-INT Items

**T810A1-INT-006 (Schema Loading Integration)** — NEW:
```markdown
* **T810A1-INT-006 (Schema Loading Integration)** — T810A1-S05 session initialization SHALL load T810A2 schema artifacts per `T810A2-INT-003 (Session Initialization Integration)`.
  - **Stable SCHEMA Source**: `template_stable_patient_schema.yaml` (or patient-specific profile file)
  - **Dynamic SCHEMA Source**: `template_dynamic_tracking_schema.yaml` (consolidated block)
  - **Loading Sequence**: Per `T810A1-IG-006` — Memory Review → Stable SCHEMA → Dynamic SCHEMA templates → Greet
  - **Block 4 Reference**: S04-FR-003 (Project Knowledge Authority) loads schemas into context
  - **Cross-Reference**: `T810A2-INT-003`, `T810A1-IF-005`, `T810A1-IG-006`
```

**T810A1-INT-007 (Controlled Vocabulary Integration)** — NEW:
```markdown
* **T810A1-INT-007 (Controlled Vocabulary Integration)** — T810A1 Dynamic JSON generation SHALL use T810A2 controlled vocabularies per `T810A-ADR-002 (Foundational Vocabulary Authority)`.
  - **Vocabulary Source**: `T810A-ADR-002` catalog + `controlled_vocabularies.md`
  - **Enforcement Method**: Prompt-engineering based (no programmatic validation per `T810A-CON-004`)
  - **Value Drift Mitigation**: S05 execution protocol references vocabulary patterns; S08 exemplars demonstrate correct usage
  - **Semantic Scale Mapping**: Numeric → descriptive labels embedded in templates per `T810A2-IG-003`
  - **Cross-Reference**: `T810A-ADR-002`, `T810A2-CON-002`, `T810A2-IF-003`, `T810A2-IG-003`
```

---

### Phase 1 Success Criteria

- [ ] All existing F-RIDs reviewed and enhancement targets identified
- [ ] **T810A1-GDR-003 (9-Block Architecture Assignment) created with Story-Block mapping and IG Coverage Matrix**
- [ ] F.6 subsection created with 7 T810A1-IG items (IG-001 to IG-007)
- [ ] **All IG items include Block Applicability section per T810A1-GDR-003**
- [ ] All IG items follow T102-ADR-005-FR-005 format
- [ ] IG items reference T810A1-RES-001 findings appropriately
- [ ] F.7 subsection enhanced with T810A2-INT cross-references
- [ ] 3 existing INT items enhanced (INT-001, INT-003, INT-005)
- [ ] 2 new INT items created (INT-006, INT-007)
- [ ] All INT items comply with T102-ADR-005-FR-008 (suggestive, cross-feature refs permitted)
- [ ] T810A1-CON-004 created as high-level constraint (implementation details in IG-007/INT-007)

---

## V. PHASE 2: COMPLETE 9-BLOCK SYSTEM PROMPT DEVELOPMENT

**Objective**: Produce foundational draft content for ALL 9 blocks of `gastro_system.md` in a dedicated Phase 2 proposal file, incorporating all Phase 1 F-RIDs (IG, INT, CON, GDR). Development proceeds in two passes: (1) initial foundational draft of all blocks, then (2) per-block in-depth development.

**Duration**: 180-240 minutes (initial draft + per-block refinement + validation)

**Output Artifact**: `proposal_T810A1-PROMPT_phase2.md` (new proposal file for Phase 2)

---

### Subphase 2.0: Phase 2 Proposal Initialization

**Target File**: `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A1/proposal_T810A1-PROMPT_phase2.md`

**Purpose**: Create a dedicated Phase 2 proposal file that serves as the development workspace for all 9 blocks before finalizing in `gastro_system.md`.

**Proposal Structure**:
- **Section I**: Executive Summary (Phase 2 scope, dependencies on Phase 1 proposal)
- **Section II**: Block Development Matrix (per T810A1-GDR-003)
- **Sections III-XI**: Draft content for each Block (1-9) — populated in Subphase 2.1
- **Section XII**: Cross-Block Validation Checklist
- **Section XIII**: Mapping to gastro_system.md
- **Section XIV**: Next Steps (Story-level refinement)

**Input Dependencies**:
- `request_T810A1-PROMPT.md` (F-RIDs from Sections F-I)
- `proposal_T810A1-PROMPT_phase1.md` (IG, INT, CON, GDR specifications)
- `gastro_system.md` v0.x (Blocks 1-3 baseline content)

---

### Subphase 2.1: ALL BLOCKS Foundational Draft (Initial Pass)

**Purpose**: Generate foundational draft content for ALL 9 blocks in a single subphase to establish the complete system architecture before per-block refinement.

**Reference**: `T810A1-ADR-001 (9-Block Architecture Assignment)` from Concept document for Block-to-Story mapping and governing F-RIDs.

**Approach** (per Client QA — Option C: Rich Skeleton approved):
- For each block, produce **paragraph-level draft content** with full section structures
- Most F-RID patterns integrated (may need polishing in per-block refinement)
- Examples and demonstrations outlined with placeholder content
- Comments/placeholders allowed for cross-block dependencies during this draft pass
- This pass prioritizes **complete architecture visibility** over final polish; per-block refinement in Subphases 2.2-2.10 becomes polishing/validation exercise

#### Block 1 (S01) — Project Context [Draft]
- **Baseline**: Review existing content from `gastro_system.md` v0.x
- **Draft Scope**: Diagnostic Stance, Privacy Stance, Operational Constants with IG-006 reference
- **Governing F-RIDs**: IF-001, IF-002, IG-006

#### Block 2 (S02) — Role Identity [Draft]
- **Baseline**: Review existing content from `gastro_system.md` v0.x
- **Draft Scope**: Role & Mandate, Key Competencies, Communication Style (phase tones) with IG-002/IG-003 alignment
- **Governing F-RIDs**: NFR-002, IG-002, IG-003, GDR-001

#### Block 3 (S03) — Toolbox [Draft]
- **Baseline**: Preserve placeholder per CON-003
- **Draft Scope**: Placeholder comment only
- **Governing F-RIDs**: CON-003

#### Block 4 (S04) — Knowledge Base [Draft]
- **Draft Scope**: Knowledge type taxonomy, authority hierarchy outline, schema reference placeholders
- **Governing F-RIDs**: IF-005, IG-006, IG-007, INT-006

#### Block 5 (S05) — Execution Protocol [Draft]
- **Draft Scope**: 5-phase protocol overview, protocol triggering outline, phase execution step placeholders, gate enforcement structure
- **Governing F-RIDs**: NFR-001, NFR-004, NFR-005, GDR-001, GDR-002, IG-001 to IG-007, INT-001

#### Block 6 (S06) — Behavioral Guardrails [Draft]
- **Draft Scope**: Anti-pattern list from IG-005, constraint enforcement outline, gate enforcement rules structure
- **Governing F-RIDs**: CON-001 to CON-004, IG-001, IG-005

#### Block 7 (S07) — Quality Criteria [Draft]
- **Draft Scope**: E-QG reference structure, IG-derived checkpoint outline
- **Governing F-RIDs**: E-QG inherited, IG-001 to IG-007 derived

#### Block 8 (S08) — Exemplars [Draft]
- **Draft Scope**: Example category outline (OARS, hedging, anti-patterns, gates, JSON)
- **Governing F-RIDs**: IG-002, IG-003, IG-005

#### Block 9 (S09) — I/O Specification [Draft]
- **Draft Scope**: Input/output interface outline, confidence indicator structure, JSON format outline
- **Governing F-RIDs**: IF-001 to IF-006, IG-003, IG-007, INT-005, INT-007

**Deliverable**: Proposal Sections III-XI populated with skeleton-level draft content for all 9 blocks.

---

### Subphase 2.2: Block 1 (S01) In-Depth Development

**Purpose**: Refine Block 1 draft into complete, specification-grade content per T810A1-S01 FRs.

**Actions**:
- Review existing baseline content from `gastro_system.md` v0.x
- Verify IF-001/IF-002 alignment (input/output interface specifications)
- Add IG-006 operational constants reference for session initialization greeting
- Minor wording enhancements for F-RID alignment; preserve baseline structure

**Deliverable**: Complete Block 1 content in Phase 2 proposal Section III.

---

### Subphase 2.3: Block 2 (S02) In-Depth Development

**Purpose**: Refine Block 2 draft into complete, specification-grade content per T810A1-S02 FRs.

**Actions**:
- Review existing baseline content from `gastro_system.md` v0.x
- Verify NFR-002 phase tone mapping (Engage, Analyze, Probe, Coach, Summarize)
- Ensure communication style aligns with IG-002 OARS collaborative framing
- Ensure Analyze phase tone reflects IG-003 epistemic hedging confidence language
- Minor wording enhancements for IG-002/IG-003 alignment

**Deliverable**: Complete Block 2 content in Phase 2 proposal Section IV.

---

### Subphase 2.4: Block 3 (S03) In-Depth Development

**Purpose**: Confirm Block 3 placeholder status per CON-003.

**Actions**:
- Verify placeholder maintained per CON-003 (Tooling Deferral)
- No content development; block remains deferred to post-MVP

**Deliverable**: Confirmed placeholder in Phase 2 proposal Section V.

---

### Subphase 2.5: Block 4 (S04) In-Depth Development

**Purpose**: Develop complete Block 4 content per T810A1-S04 FRs.

**Content Structure**:
1. **Knowledge Type Taxonomy**: Internal Model, Custom Instructions, Project Knowledge, Memory, Web Search
2. **MVP Content Inventory**: Patient profile (Stable JSON), tracking templates (Dynamic JSON skeletons)
3. **Stable & Dynamic JSON Declaration**: High-level architecture reference per T810A-GDR-002
4. **Authority Hierarchy**: Project > Memory > Internal Model; Web Search for validation

**Governing F-RIDs**: IF-005, IG-006, IG-007, INT-006

**Deliverable**: Complete Block 4 content in Phase 2 proposal Section VI.

---

### Subphase 2.6: Block 5 (S05) In-Depth Development

**Purpose**: Develop complete Block 5 content per T810A1-S05 FRs (highest complexity block).

**Content Structure**:
1. **Protocol Overview**: Tracking → Analyze → Probe → Coach → Summarize
2. **Protocol Triggering**: Input-type detection (Tracking-Only, Full Protocol, Q&A Mode)
3. **Phase Execution Steps**: Detailed steps for each phase with F-RID integration
4. **Gate Enforcement**: Confirmation gates, refusal patterns, 5-ROUND CAP
5. **Session Initialization**: Memory review, schema loading, conflict detection, greeting

**Governing F-RIDs**: NFR-001, NFR-004, NFR-005, GDR-001, GDR-002, IG-001 to IG-007, INT-001

**Deliverable**: Complete Block 5 content in Phase 2 proposal Section VII.

---

### Subphase 2.7: Block 6 (S06) In-Depth Development

**Purpose**: Develop complete Block 6 content per T810A1-S06 FRs.

**Content Structure**:
1. **Anti-Pattern Prohibitions**: 7 prohibited behaviors from IG-005
2. **Constraint Enforcement**: CON-001 to CON-004 compliance rules
3. **Gate Enforcement Rules**: Compliance checks for IG-001 phase gating
4. **Safety Boundaries**: Deferred clinical safety per CON-001

**Governing F-RIDs**: CON-001 to CON-004, IG-001, IG-005

**Deliverable**: Complete Block 6 content in Phase 2 proposal Section VIII.

---

### Subphase 2.8: Block 7 (S07) In-Depth Development

**Purpose**: Develop complete Block 7 content per T810A1-S07 FRs.

**Content Structure**:
1. **Inherited E-QG Criteria**: Reference T810A-QG-001 to QG-008 from Epic SPS
2. **IG-Derived Checkpoints**: Quality verification points from IG-001 to IG-007
3. **Session Quality Checklist**: Pre-Coach/pre-Summarize verification
4. **Output Quality Standards**: Response quality metrics

**Governing F-RIDs**: E-QG inherited, IG-001 to IG-007 derived

**Deliverable**: Complete Block 7 content in Phase 2 proposal Section IX.

---

### Subphase 2.9: Block 8 (S08) In-Depth Development

**Purpose**: Develop complete Block 8 content per T810A1-S08 FRs.

**Content Structure**:
1. **OARS Dialogue Examples**: Per IG-002 (correct vs. rapid interrogation)
2. **Epistemic Hedging Examples**: Per IG-003 (high/moderate/low confidence)
3. **Anti-Pattern Demonstrations**: Per IG-005 (❌ incorrect vs. ✅ correct)
4. **Gate Phrasing Examples**: Per IG-001 (confirmation gates, refusal patterns)
5. **JSON Generation Examples**: Per IG-007 (correct format, fixed keys)

**Governing F-RIDs**: IG-002, IG-003, IG-005

**Deliverable**: Complete Block 8 content in Phase 2 proposal Section X.

---

### Subphase 2.10: Block 9 (S09) In-Depth Development

**Purpose**: Develop complete Block 9 content per T810A1-S09 FRs.

**Content Structure**:
1. **Input Interface**: Text + image parsing per IF-001
2. **Output Interface**: Markdown primary output per IF-002
3. **Explicit Classification**: Confidence indicators per IF-003
4. **Reporting Trigger**: /report command per IF-004
5. **Dynamic JSON Output**: Generation format per IF-006, IG-007
6. **Session Report Format**: Dual-format per INT-005

**Governing F-RIDs**: IF-001 to IF-006, IG-003, IG-007, INT-005, INT-007

**Deliverable**: Complete Block 9 content in Phase 2 proposal Section XI.

---

### Subphase 2.11: Cross-Block Validation

**Action**: Verify all 9 blocks against F-RID specifications and cross-block consistency.

| Block | Story | Primary Validation Items | Verified |
|:------|:------|:------------------------|:---------|
| 1 | S01 | IF-001/002 alignment, IG-006 operational constants | [ ] |
| 2 | S02 | NFR-002 tone mapping, IG-002/003 communication alignment | [ ] |
| 3 | S03 | CON-003 placeholder maintained | [ ] |
| 4 | S04 | IF-005 context injection, IG-006/007 schema references, INT-006 | [ ] |
| 5 | S05 | NFR-001/004/005, GDR-001/002, all IG-001 to IG-007, INT-001 | [ ] |
| 6 | S06 | CON-001 to CON-004, IG-001 gates, IG-005 anti-patterns | [ ] |
| 7 | S07 | E-QG inheritance, IG-derived checkpoints | [ ] |
| 8 | S08 | IG-002/003/005 exemplars demonstrated | [ ] |
| 9 | S09 | IF-001 to IF-006, IG-003/007, INT-005/007 | [ ] |

**Cross-Block Consistency Checks** (per Client QA — Approach A: Sequential Development approved):
- [ ] Block 5 (S05) references Block 4 (S04) schema authority correctly
- [ ] Block 6 (S06) enforces Block 5 (S05) gate rules
- [ ] Block 8 (S08) demonstrates patterns from Block 5 (S05)
- [ ] Block 9 (S09) aligns with Block 5 (S05) output generation

**Development Sequence Note**:
- Subphases 2.2-2.6 (Blocks 1-4-5) developed sequentially due to tight coupling (S05 references S04 schema authority)
- Subphases 2.7-2.10 (Blocks 6-9) may be developed flexibly after Block 5 completion
- Comments/placeholders used during Phase 2.1 draft for cross-block dependencies (Approach B hybrid per Client QA)

---

### Phase 2 Success Criteria

- [ ] Phase 2 proposal file created at `proposal_T810A1-PROMPT_phase2.md`
- [ ] Subphase 2.1: ALL 9 blocks drafted with foundational skeleton content
- [ ] Subphases 2.2-2.10: Each block refined to specification-grade completeness
- [ ] All 9 blocks mapped to governing F-RIDs per T810A1-GDR-003
- [ ] Cross-block validation checklist passed
- [ ] Phase 2 proposal ready for client review before `gastro_system.md` finalization
- [ ] Draft content marked as foundational (subject to Story-level refinement)

---

## VI. PHASE 3: REQUEST OPTIMIZATION & MVP DEPLOYMENT

**Objective**: Optimize Request document token footprint via F-RID consolidation, add the platform constraint (`T810A1-CON-005`), add a separate MVP deployment implementation guidance item (`T810A1-IG-008`) to define the Hybrid Tiered Architecture (Tier 1 ≤7,500 chars + Tier 2 extended knowledge + Tier 3 schema knowledge), and refine the Phase 2 proposal so Subphase 2.1 content is explicitly separable into Tier 1 vs Tier 2 deliverables per block.

**Duration**: 90-120 minutes (Request optimization + Phase 2 proposal refinement + MVP architecture)

**Client-Approved Decisions** (from QA Round 4):
- **CON-005 Addition**: Approved per T102-ADR-005-FR-005 format
- **MVP Architecture**: Option 3 (Hybrid Tiered) — Core prompt (≤8,000 chars) + Extended Knowledge files
- **Request Simplification**: Task 0 findings approved (consolidate IG bodies, remove INT redundancies)
- **Phase 2 Refinement**: Both Block 5 gate templates AND Block 8 anti-pattern exemplars

---

### Subphase 3.0: T810A1-CON-005 Creation (Request Section F.3)

**Target Section**: Request `### F.3. Constraints`

**Purpose**: Add MVP deployment constraint governing ChatGPT system prompt size limit per T102-ADR-005-FR-005 format.

**T102-ADR-005-FR-005 Format Requirements**:
- **Format**: `* **<ID> (<Title>)** — <concise description>`
- **Title**: Max 2-3 words
- **ID Pattern**: `T810A1-CON-005` (Feature-level Constraint)

**Proposed F-RID Body**:

```markdown
* **T810A1-CON-005 (System Prompt Limit)** — The LLM_Gastro system prompt deployed to the ChatGPT custom GPT platform SHALL NOT exceed **8,000 characters** total.
```

**Deliverables**:
1. `T810A1-CON-005` added to Request Section F.3 (Constraints)
2. Phase 1 proposal updated with CON-005 reference in CON summary table
3. Constraint registered in F-RID inventory table
4. Hybrid Tiered MVP deployment packaging moved to `T810A1-IG-008` (Implementation Guidance), with governance traceability anchored to `T810A1-ADR-001` and `T810A1-IF-002`

---

### Subphase 3.1: Request F-RID Simplification (Task 0 Implementation)

**Target Sections**: Request `### F.6. Implementation Guidance` and `### F.7. Integration Notes`

**Purpose**: Reduce Request document token footprint by consolidating verbose IG bodies to reference pointers and removing redundant INT cross-reference lines per Task 0 analysis.

#### A. IG Body Consolidation

**Rationale**: Per Task 0 analysis, IG-001 through IG-007 contain deeply nested implementation detail (~6,500 chars) that duplicates content naturally belonging in:
1. The system prompt itself (Blocks 5, 6, 8)
2. The exemplars (Block 8)

**Consolidation Strategy** (per T102-ADR-005 — IG items provide directional guidance, not procedural specifications):

| Current Pattern | Proposed Pattern | Estimated Savings |
|:----------------|:-----------------|:------------------|
| Full OARS breakdown in IG-002 (~800 chars) | "Implement OARS pattern per clinical MI best practices. Details in S05/S08." | ~600 chars |
| 3-tier confidence table in IG-003 (~1,000 chars) | "Apply qualitative hedging per T810A-ADR-001. Tier definitions in S05." | ~700 chars |
| 7 anti-patterns with examples in IG-005 (~1,200 chars) | "Enforce anti-pattern prohibitions. Catalog in S06/S08." | ~900 chars |
| 4-step session initialization in IG-006 (~1,100 chars) | "Follow structured session initialization. Sequence in S05." | ~800 chars |
| JSON generation rules in IG-007 (~1,000 chars) | "Generate Dynamic JSON per T810A2 schema specifications. Rules in S05/S09." | ~700 chars |

**Total Estimated Savings**: ~4,000 characters from Request document

**Preservation Rules**:
- **KEEP**: Core directive (SHALL statement), key pattern name, cross-references, Block Applicability section
- **MOVE**: Detailed procedures, example phrasing, step-by-step sequences → System prompt (Phase 2 proposal)
- **FORMAT**: Consolidated body follows T102-ADR-005-FR-005 (concise description with reference pointers)

**Deliverable**: Simplified IG-001 through IG-007 bodies in Phase 1 proposal for Request population

#### B. INT Redundancy Removal

**Rationale**: Per Task 0 analysis, INT-001 through INT-007 each contain redundant "Cross-Reference" lines that duplicate information already in "Integration Touchpoints" sections (~500 chars total).

**Removal Strategy**:
- **KEEP**: Pattern description, Integration Touchpoints narrative section
- **REMOVE**: Redundant "Cross-Reference" bullet lines that merely repeat touchpoint IDs

**Deliverable**: Streamlined INT-001 through INT-007 bodies in Phase 1 proposal

#### C. GDR-001/NFR-001 Overlap Resolution

**Rationale**: Per Task 0 analysis, T810A1-NFR-001 (Protocol Reliability) and T810A1-GDR-001 (Tracking-First Clinical Protocol) both contain the same 5-phase protocol structure content (~600 chars redundancy).

**Resolution Strategy**:
- **NFR-001**: KEEP protocol structure (NFR defines system quality attribute)
- **GDR-001**: REDUCE to decision rationale and references only; remove duplicate structure

**Deliverable**: Deduplicated GDR-001 body in Phase 1 proposal

---

### Subphase 3.2: Phase 2 Proposal — Block 5 Gate Template Addition

**Target Section**: Phase 2 Proposal `### VII.D. System Prompt Draft` (Block 5 Execution Protocol)

**Purpose**: Add Phase Transition Gates subsection to Block 5 with explicit gate confirmation phrasing templates per Task 1 Gap 1 analysis.

**Gap Analysis Summary** (from Task 1):
- ✅ Block 5 states 2-loop minimum
- ✅ Block 5 states "Probe mandatory before Coach"
- ❌ **Missing**: Explicit gate confirmation phrasing template
- ❌ **Missing**: Refusal pattern for premature coaching requests
- ⚠️ 5-ROUND CAP mentioned in Block 6, not Block 5

**Proposed Addition**:

```markdown
## Phase Transition Gates
Before moving from Analyze → Probe or Probe → Coach:

1. **Synthesis Gate**: Present a brief synthesis of understanding:
   - Template: "Based on what you've shared, [synthesis]. Does this capture your situation accurately?"
   - Wait for explicit confirmation, clarification request, or correction

2. **Premature Coaching Redirect**: If patient requests coaching before probing:
   - Template: "I want to make sure I understand your situation fully before offering suggestions. May I ask a couple of clarifying questions first?"
   - Frame as partnership ("together we'll..."), not refusal

3. **5-ROUND CAP Re-Anchor**: After 5 rounds without resolution:
   - Template: "I notice we're covering a lot of ground. To focus on what matters most, could you summarize your main concern in 1–2 sentences?"
   - Prevents infinite clarification loops; re-centers on patient priority
```

**Deliverable**: Block 5 Section VII.D enhanced with Phase Transition Gates subsection

---

### Subphase 3.3: Phase 2 Proposal — Block 8 Anti-Pattern Exemplars Addition

**Target Section**: Phase 2 Proposal `### X.D. System Prompt Draft` (Block 8 Exemplars)

**Purpose**: Add negative examples for trigger detection, gate handling, and anti-patterns per Task 1 Gap 2 analysis.

**Gap Analysis Summary** (from Task 1):
- ✅ Good pattern examples for OARS, hedging, gating, JSON
- ⚠️ Only one brief "Bad pattern (avoid)" for hedging
- ❌ **Missing**: Trigger detection demonstrations (IG-004)
- ❌ **Missing**: Gate handling incorrect examples (IG-001)
- ❌ **Missing**: Full anti-pattern demonstrations (IG-005)

**Proposed Additions**:

#### A. Input Type Detection Examples (per IG-004)
```markdown
### Input Type Detection Examples
**Tracking-Only:**
> User: "Log that I had oatmeal at 8am"
> Response: Generate JSON entry, brief acknowledgment, STOP (no analysis/coaching)

**Full Protocol:**
> User: "I woke up with cramping after last night's dinner"
> Response: Full Tracking → Analyze → Probe → Coach → Summarize protocol

**Q&A:**
> User: "What causes SIBO?"
> Response: Concise educational answer, no JSON, no tracking protocol
```

#### B. Gate Handling Anti-Pattern Examples (per IG-001)
```markdown
### Gate Handling Anti-Patterns
**❌ Skipped Gate (Premature Coaching):**
> User: "I had a high-fat meal and felt bloated"
> Bad Response: "You should try reducing fat intake." (jumped to Coach without Probe)

**✅ Correct Gate Handling:**
> User: "I had a high-fat meal and felt bloated"
> Good Response: "Thank you for tracking that. Before I suggest anything, I'd like to understand the pattern better. How soon after the meal did the bloating start? Have you noticed this with other high-fat meals?"
```

#### C. Full Anti-Pattern Catalog Examples (per IG-005)
```markdown
### Anti-Pattern Demonstrations

**❌ Rapid Interrogation:**
> "What did you eat? When? How much? Any symptoms?"
> (4 questions without acknowledgment)

**✅ Corrected:**
> "What did you eat?" → [patient answers] → "Thank you. When was that?"
> (one question at a time with acknowledgment)

**❌ Premature Reassurance:**
> "Don't worry, it's probably nothing."

**✅ Corrected:**
> "Let's look at this together. What you're describing sounds frustrating—let me understand the pattern better."

**❌ Assistant Mode Offers:**
> "Would you like me to build a structured AM/PM Daily Routine Protocol Sheet?"

**✅ Corrected:**
> "What time of day do you typically notice this pattern?" (Socratic inquiry)

**❌ Definitive Statements:**
> "You have fat maldigestion."

**✅ Corrected:**
> "This pattern is consistent with fat maldigestion, though there could be other explanations. Let's discuss this with your gastroenterologist."
```

**Deliverable**: Block 8 Section X.D enhanced with comprehensive exemplar subsections

---

### Subphase 3.4: Phase 2 Proposal — MVP Deployment Architecture (Section XV)

**Target File**: Phase 2 Proposal `proposal_T810A1-PROMPT_phase2.md`

**Purpose**: Enhance Section XV and Subphase 2.1 block bodies so LLM_Developer can construct Tier 1 vs Tier 2 deliverables without ambiguity, while keeping Block 8 detailed exemplars Tier 2-only and preventing Phase 1 IG items from referencing proposal filenames.

**Phase 3 Task 0 (SSOT Verification)**:
- Confirm `T810A1-ADR-001` (Concept SSOT) remains the single authoritative mapping for Story→Block assignment and IG coverage (block applicability is not duplicated inside IG/INT bodies).

**Section XV Structure**:

```markdown
## XV. MVP DEPLOYMENT CONSIDERATIONS

### A. Platform Constraint
- **ChatGPT Custom GPT System Prompt Limit**: 8,000 characters
- **Current `gastro_system.md` Size**: ~21,213 characters (2.65x over limit)
- **Governing Constraint**: `T810A1-CON-005 (System Prompt Limit)`

### B. Hybrid Tiered Architecture (Option 3)

**Architecture Overview**:
    ```
    ┌─────────────────────────────────────────────────────────────┐
    │  TIER 1: System Prompt (≤8,000 chars)                       │
    │  - Core protocol (5-phase overview, triggering, gates)       │
    │  - Essential guardrails (anti-patterns, hedging rules)       │
    │  - Schema references (paths to Knowledge files)              │
    │  - Graceful degradation summary (fallback if Tier 2 unavailable) │
    └─────────────────────────────────────────────────────────────┘
                                │
                                ▼
    ┌─────────────────────────────────────────────────────────────┐
    │  TIER 2: Extended Knowledge (`gastro_system_extended.md`)    │
    │  - Full exemplars (Block 8 complete content)                 │
    │  - Detailed guidance (Block 5 step-by-step procedures)       │
    │  - Quality criteria checkpoints (Block 7 full content)       │
    │  - Edge case handling                                        │
    └─────────────────────────────────────────────────────────────┘
                                │
                                ▼
    ┌─────────────────────────────────────────────────────────────┐
    │  TIER 3: Schema Knowledge (existing files)                   │
    │  - `template_dynamic_tracking_schema.yaml`                        │
    │  - `template_stable_patient_schema.yaml`                       │
    │  - `field_classification_mapping.md`                         │
    │  - `vocabulary_catalog_example.md`                           │
    └─────────────────────────────────────────────────────────────┘
    ```

### C. Tier 1 Content Reduction Strategy

| Block | Current Est. | Tier 1 Target | Reduction Strategy |
|:------|:-------------|:--------------|:-------------------|
| 1 (Project Context) | 1,200 | 400 | Keep stance + timezone only |
| 2 (Role Identity) | 2,000 | 800 | Competencies inline, tone brief |
| 3 (Toolbox) | 300 | 100 | "No external tools" one-liner |
| 4 (Knowledge Base) | 1,500 | 600 | Authority hierarchy + schema refs only |
| 5 (Execution Protocol) | 3,500 | 2,000 | **Critical** — preserve protocol structure |
| 6 (Guardrails) | 1,800 | 800 | Consolidate anti-patterns |
| 7 (Quality Criteria) | 1,200 | 400 | Bullet checklist only |
| 8 (Exemplars) | 2,000 | 800 | 1 good/bad example per pattern |
| 9 (I/O Specification) | 1,700 | 600 | Input types + JSON format summary |
| **Total** | ~15,200 | ~6,500 | +1,500 buffer for formatting |

### D. Implementation Deliverables

1. **`gastro_system_short.md`** (Tier 1): Condensed 9-block prompt (≤7,500 chars)
2. **`gastro_system_extended.md`** (Tier 2): Full exemplars, detailed guidance
3. **`gastro_system.md`** (Canonical): Full specification, authoritative source
4. **Updated `T810A1-CON-005`** in Request: Constraint documentation

### F. Subphase 2.1 (Per-Block Tier Separation) — REQUIRED CHANGES TO PHASE 2 PROPOSAL

**Requirement**: For each block section in Phase 2 (Blocks 1–9), update `### D. System Prompt Draft (Subphase 2.1 — Text)` to include two explicit sub-subsections:
- `#### 1. Tier 1 Draft — gastro_system_short.md`
- `#### 2. Tier 2 Draft — gastro_system_extended.md`

**Rules**:
- Tier 1 stays high-level and must support ≤7,500 chars overall (Block 8 must remain minimal; no full exemplar dialogues in Tier 1).
- Tier 2 may include full procedures and exemplars (Block 8 detailed catalogs live here).
- Tier 1/Tier 2 content MUST not introduce “block applicability” statements for IG/INT items; block applicability remains governed by `T810A1-ADR-001`.

### G. Implementation Guidance Details (IG Annex) — REQUIRED CHANGES TO PHASE 2 PROPOSAL

**Requirement**: Add an “Implementation Guidance Annex” section in Phase 2 proposal to host the detailed templates/patterns that Phase 1 IG items point to, without referencing proposal filenames.

### E. Governance Traceability

- All tiered files MUST trace to canonical `gastro_system.md`
- Changes to canonical spec require synchronized updates to Tier 1/2 files
- Version bumps apply to all three files simultaneously
```

**Deliverable**: Phase 2 proposal enhanced with Section XV (MVP Deployment Considerations)

---

### Phase 3 Success Criteria

- [ ] `T810A1-CON-005` created per T102-ADR-005-FR-005 format
- [ ] `T810A1-CON-005` remains a strict platform constraint (no tier packaging details)
- [ ] `T810A1-IG-008` added for Hybrid Tiered MVP deployment packaging and governance traceability
- [ ] IG-001 through IG-007 bodies consolidated (reference pointers, ~4,000 char savings)
- [ ] INT-001 through INT-007 redundant cross-reference lines removed (~500 char savings)
- [ ] GDR-001/NFR-001 overlap resolved (~600 char savings)
- [ ] Block 5 Phase Transition Gates subsection added to Phase 2 proposal
- [ ] Block 8 Anti-Pattern Exemplars subsections added to Phase 2 proposal
- [ ] Section XV (MVP Deployment Considerations) added to Phase 2 proposal
- [ ] Hybrid Tiered Architecture documented with reduction strategy
- [ ] Phase 2 proposal Subphase 2.1 blocks split into Tier 1 vs Tier 2 subsections (per-block)
- [ ] Phase 2 proposal includes an IG Implementation Guidance Annex (to avoid IG filename references)
- [ ] All changes follow T102-ADR-005 standards
- [ ] Phase 1 and Phase 2 proposals updated for client review

---


## VII. SUCCESS CRITERIA (OVERALL)

**Phase 0 Complete When**:
- [ ] T810A1-NOTE-001 and T810A1-RES-001 entries created in Request
- [ ] Two analysis artifacts created (RES-001-focused, NOTE-001-focused)
- [ ] Context material review checkpoint passed

**Phase 1 Complete When**:
- [ ] T810A1-ADR-001 created in Concept document with Story-Block mapping and IG Coverage Matrix
- [ ] F.6 subsection created with 7+ T810A1-IG items (block applicability governed by `T810A1-ADR-001`)
- [ ] F.7 subsection enhanced with T810A2-INT cross-references
- [ ] 2 new INT items created (INT-006, INT-007)
- [ ] T810A1-CON-004 created as high-level constraint
- [ ] All IDs follow T102-ADR-005 standards
- [ ] Phase 1 proposal approved by client

**Phase 2 Complete When**:
- [ ] Phase 2 proposal file created (`proposal_T810A1-PROMPT_phase2.md`)
- [ ] Blocks 1-3 reviewed and aligned
- [ ] Blocks 4-9 fully developed with draft content
- [ ] Cross-block validation passed
- [ ] Phase 2 proposal approved by client
- [ ] Draft content ready for `gastro_system.md` finalization and Story-level refinement

**Phase 3 Complete When**:
- [ ] T810A1-CON-005 (System Prompt Limit) created per T102-ADR-005-FR-005
- [ ] Request F-RID simplification completed (~5,100 char savings):
  - [ ] IG-001 to IG-007 bodies consolidated to reference pointers
  - [ ] INT-001 to INT-007 redundant cross-reference lines removed
  - [ ] GDR-001/NFR-001 overlap resolved
- [ ] Phase 2 proposal enhanced:
  - [ ] Block 5 Phase Transition Gates subsection added
  - [ ] Block 8 Anti-Pattern Exemplars subsections added
  - [ ] Section XV MVP Deployment Considerations added
- [ ] Hybrid Tiered Architecture documented with reduction strategy
- [ ] All tiered file deliverables specified (Tier 1/2/3)
- [ ] Phase 3 proposals approved by client

---


## VIII. RISKS & MITIGATION

| Risk | Impact | Likelihood | Mitigation |
|:-----|:-------|:-----------|:-----------|
| **IG items too prescriptive** | Conflicts with Story-level flexibility | Medium | Use "SHOULD" language where appropriate; mark as guidance, not absolute requirement |
| **INT cross-references create circular dependencies** | Maintenance overhead | Low | Follow T102-ADR-005-FR-008 governance loop; update INT when E-RIDs evolve |
| **Draft system prompt incomplete** | Story development blocked | Medium | Mark draft as foundational; Stories refine Block-specific content |
| **T810A2 schema changes after handoff** | Integration drift | Low | T810A2 handoff accepted as stable for MVP; post-MVP changes follow governance |

---

## IX. DEPENDENCIES

**Internal Dependencies**:
- T102-ADR-005: ID Specification & Rules (formatting standards)
- T810A-GDR-001/002: Epic governance patterns
- T810A-ADR-001/002: Epic architectural patterns
- T810A1-RES-001: Research findings integration
- T810A1-NOTE-001: T810A2 handoff deliverables

**External Dependencies**:
- Client approval for IG/INT specifications
- T810A2 schema stability (handoff accepted)

---

## X. NEXT STEPS

**Phase 0 Completed**:
- ✅ Analysis artifacts created (RES-001-focused, NOTE-001-focused)

**Phase 1 Completed**:
1. **Subphase 1.1**: F-RID inventory review + T810A1-ADR-001 creation — ✅ Complete (reclassified from GDR-003 to ADR-001)
2. **Subphase 1.2**: Create T810A1-IG category (7 items with Block Applicability) — ✅ Specified in proposal
3. **Subphase 1.3**: Enhance T810A1-INT category (3 updates + 2 new) + CON-004 — ✅ Specified in proposal
4. **Phase 1 Gate**: Phase 1 proposal reviewed — ✅ Approved with refinements in Phase 3

**Phase 2 In Progress**:
5. **Subphase 2.0**: Initialize Phase 2 proposal file — ✅ Complete
6. **Subphase 2.1**: ALL 9 blocks foundational draft (Rich Skeleton) — ✅ Complete
7. **Subphases 2.2-2.10**: Per-block in-depth development — ⏳ Pending (to be enhanced in Phase 3)
8. **Subphase 2.11**: Cross-block validation — ⏳ Pending

**Phase 3 (Current — QA Round 4 Approved)**:
9. **Subphase 3.0**: T810A1-CON-005 Creation (System Prompt Limit) — **NEXT**
10. **Subphase 3.1**: Request F-RID Simplification (IG consolidation, INT cleanup, GDR/NFR dedup) — ⏳ Pending
11. **Subphase 3.2**: Block 5 Gate Template Addition (Phase 2 proposal) — ⏳ Pending
12. **Subphase 3.3**: Block 8 Anti-Pattern Exemplars Addition (Phase 2 proposal) — ⏳ Pending
13. **Subphase 3.4**: MVP Deployment Architecture (Section XV addition) — ⏳ Pending
14. **Phase 3 Gate**: Present updated Phase 1 + Phase 2 proposals for Client approval

**Post-Phase 3 (Upon Phase 3 Approval)**:
15. **gastro_system.md Finalization**: Consolidate Phase 2 proposal into canonical full specification
16. **Tiered File Creation**: Create `gastro_system_short.md` (Tier 1) and `gastro_system_extended.md` (Tier 2)
17. **Story-Level Handoff**: Draft content ready for per-Story (S01-S10) refinement

---

## XI. APPENDICES

### A. T102-ADR-005 Category Reference (Feature Scope)

| Token | Full Name | Definition | Used In |
|:------|:----------|:-----------|:--------|
| `FR` | Functional Requirement | Testable behavior | Stories |
| `NFR` | Non-Functional Requirement | Quality attributes | F.4 |
| `IF` | Interface | Data/integration contracts | F.5 |
| `IG` | Implementation Guidance | Internal authoring guidance | **F.6 (NEW)** |
| `INT` | Integration | Cross-feature patterns | F.7 |
| `CON` | Constraint | Non-negotiable boundaries | F.3 |
| `RES` | Research | Commissioned research | Section I |
| `NOTE` | Note | Informational remarks | Section I |

### B. F-RID Enhancement Summary

| Action | Category | Items | Source |
|:-------|:---------|:------|:-------|
| CREATE | IG | 7 items (IG-001 to IG-007) | T810A1-RES-001, T810A1-NOTE-001 |
| ENHANCE | INT | 3 items (INT-001, INT-003, INT-005) | T810A2-INT cross-refs |
| CREATE | INT | 2 items (INT-006, INT-007) | T810A2-INT patterns |
| ADD | CON | 1 item (CON-004 Fixed Keys) | T810A2-CON-005 |

### C. Reference Documents

- **Request (T810A1)**: `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md`
- **Research Report**: `prompt/artifacts/tasks/T810/research/report/report_T810A1-PROMPT_s05-execution-protocol-clinical-validation.md`
- **Handoff Brief**: `prompt/artifacts/tasks/T810/consultant/workspace/communication/consultant/handoff_brief_T810A2-SCHEMA_to_T810A1-PROMPT_phase2.md`
- **T810A2 Request**: `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md`
- **Combined Schema**: `prompt/roles/gastro/data/template_dynamic_tracking_schema.yaml`
- **Field Classification**: `prompt/roles/gastro/data/field_classification_mapping.md`

---

**Document Status**: Active (Phase 3 Planning)
**Current Phase**: Phase 3 — Request Optimization & MVP Deployment
**Approval Required**: Client approval for Phase 3 execution
**Next Review**: Upon Phase 3 Subphase 3.0 completion (T810A1-CON-005 creation)

---

## XII. CHANGELOG

- **v1.0.4** (2025-12-12): Client QA feedback round 4 integration — **PHASE 3 CREATION**:
  - **ADDED**: Phase 3 (Section VII) — Request Optimization & MVP Deployment:
    - **Subphase 3.0**: T810A1-CON-005 (System Prompt Limit) creation per T102-ADR-005-FR-005
    - **Subphase 3.1**: Request F-RID simplification (IG body consolidation ~4,000 chars, INT redundancy removal ~500 chars, GDR-001/NFR-001 dedup ~600 chars)
    - **Subphase 3.2**: Block 5 Phase Transition Gates template addition (per Task 1 Gap 1)
    - **Subphase 3.3**: Block 8 Anti-Pattern Exemplars addition (per Task 1 Gap 2)
    - **Subphase 3.4**: Section XV MVP Deployment Considerations (Hybrid Tiered Architecture)
  - **CLIENT DECISIONS** (QA Round 4):
    - **Q1**: T810A1-CON-005 approved per T102-ADR-005-FR-005 format
    - **Q2**: Option 3 (Hybrid Tiered Architecture) approved for MVP deployment
    - **Q3**: Task 0 simplifications approved (IG consolidation, INT cleanup, GDR/NFR dedup)
    - **Q4**: Both Block 5 AND Block 8 refinements approved
  - **UPDATED**: Section VI Success Criteria — added Phase 3 completion criteria
  - **UPDATED**: Section X Next Steps — Phase 1 marked complete, Phase 2 in progress, Phase 3 current
  - **RENUMBERED**: Sections VII→VIII (Risks), VIII→IX (Dependencies), IX→X (Next Steps), X→XI (Appendices), XI→XII (Changelog)

- **v1.0.5** (2025-12-12): QA alignment updates — Phase 3.4 enhancement:
  - **UPDATED**: Subphase 3.0 to keep `T810A1-CON-005` strictly a platform constraint (tier packaging moved to new IG)
  - **UPDATED**: Subphase 3.4 to require per-block Tier 1 vs Tier 2 separation and add an IG Implementation Guidance Annex in the Phase 2 proposal
  - **UPDATED**: Phase 1 success criteria to remove “block applicability in IG bodies” (authority remains `T810A1-ADR-001`)

- **v1.0.3** (2025-12-09): Client QA feedback round 3 integration:
  - **RECLASSIFIED**: T810A1-GDR-003 → T810A1-ADR-001 (9-Block Architecture Assignment):
    - **Rationale**: Structural/architectural decision (component boundaries, modular organization) per industry-standard ADR classification
    - **Location Change**: From Request Section G (Feature Governance Decisions) to Concept Section III.B.3 (Feature Architectural Decisions)
    - **References Updated**: All `T810A1-GDR-003` cross-references updated to `T810A1-ADR-001` throughout plan
  - **ENHANCED**: Subphase 2.1 approach per Client QA Answer 1 (Option C: Rich Skeleton):
    - Paragraph-level draft content with full section structures
    - Most F-RID patterns integrated (polishing in per-block refinement)
    - Examples/demonstrations outlined with placeholder content
    - Comments/placeholders allowed for cross-block dependencies
  - **CLARIFIED**: Cross-block development sequence per Client QA Answer 2 (Approach A with Approach B hybrid):
    - Sequential development for Blocks 1-4-5 (tight coupling: S05 references S04 schema authority)
    - Flexible ordering for Blocks 6-9 after Block 5 completion
    - Comments/placeholders used during Phase 2.1 draft for dependencies
  - **CONFIRMED**: LLM_Developer handoff granularity per Client QA Answer 3 (Option 1: Full Proposal Handoff):
    - Complete Phase 2 proposal handed off as single artifact
    - Maintains Phase 2 proposal integrity and cross-block validation before implementation

- **v1.0.2** (2025-12-09): Client QA feedback round 2 integration:
  - **REVISED**: Phase 2 structure to two-pass development:
    - Subphase 2.1: ALL 9 blocks foundational draft (skeleton-level, single subphase)
    - Subphases 2.2-2.10: Per-block in-depth development (one subphase per block)
    - Subphase 2.11: Cross-block validation
  - **RATIONALE**: Initial draft establishes complete architecture; per-block refinement ensures specification-grade completeness
  - Duration estimate for Phase 2 updated: 180-240 minutes (from 120-180)

- **v1.0.1** (2025-12-09): Client QA feedback round 1 integration:
  - **ADDED**: T810A1-GDR-003 reference in Subphase 1.1 (9-Block Architecture Assignment)
  - **REVISED**: Phase 2 completely rewritten to cover ALL 9 blocks (not just Block 5):
    - Subphase 2.0: Phase 2 proposal initialization
    - Subphase 2.1: Block Development Matrix per GDR-003
    - Subphase 2.2: Blocks 1-3 review and alignment
    - Subphases 2.3-2.8: Blocks 4-9 full development
    - Subphase 2.9: Cross-block validation
  - **ADDED**: Output artifact specification (`proposal_T810A1-PROMPT_phase2.md`)
  - **UPDATED**: Phase 1 Success Criteria to include GDR-003, Block Applicability, CON-004
  - **UPDATED**: Overall Success Criteria to reflect new Phase 2 structure
  - **UPDATED**: Next Steps to show current progress and Phase 2 roadmap
  - Duration estimate for Phase 2 updated: 120-180 minutes (from 60-90)

- **v1.0.0** (2025-12-08): Initial consultancy plan creation for T810A1-PROMPT F-RID enhancement. Defines Phases 0-2 for research/handoff integration, IG category creation, INT enhancement, and draft system prompt generation. Incorporates T102-ADR-005 as mandatory implementation rules. Client-approved decisions: Pattern A (aggregation), Option A (field classification depth), T810A2 trust level.
