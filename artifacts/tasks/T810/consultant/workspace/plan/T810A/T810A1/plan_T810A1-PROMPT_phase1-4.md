---
artifact_type: 'PLAN'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1'
version: '1.2.0'
date: '2025-10-14'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# CONSULTANCY PLAN: T810A1 Request Completion

## I. EXECUTIVE SUMMARY

This plan outlines a systematic 4-phase approach to complete the T810A1 Request document, integrating research findings from T810A1-RES-001 into functional requirements specifications. The plan ensures upstream F-ID updates before Story development, establishes Feature-level GDR governance, systematically specifies Stories S04-S10, and coordinates parallel implementation with LLM_Developer.

**Research Foundation**: Report `report_prompt-architecture-clinical-validation_T810A_v1.0.0_i2.md` provides comprehensive validation across 7 deliverables (9-block architecture, multimodal trust-and-verify, enhanced A→P→C protocol, GI expert workflows, patient profile schema, clinical reporting, session workflows).

---

## II. PHASE OVERVIEW

| Phase | Objective | Key Deliverables | Duration Estimate |
|-------|-----------|------------------|-------------------|
| **Phase 1** | Foundation Review & Updates | Updated F-IDs (NFR/IF/CON/INT), revised S01-S03, updated gastro_system.md Blocks 1-2 | 2-3 hours |
| **Phase 1.5** | Conversation-Driven Refinement | 4 F-ID revisions + 6 new F-IDs, T810A2-SCHEMA brief, research consultation commission | 3-4 hours |
| **Phase 2** | Feature GDR Index Creation | Section III.M with 6+ Feature GDRs documenting governance decisions | 1-2 hours |
| **Phase 3** | Story Specification (S04-S10) | ~40-50 new F-IDs across 7 stories with acceptance criteria | 4-6 hours |
| **Phase 4** | Parallel Implementation | Coordinated gastro_system.md Blocks 4-10 implementation | 3-4 hours |

**Total Estimated Duration**: 13-19 hours of consultancy + development work

**Note**: Phase 1.5 is an **empirical validation gate** inserted after examining actual conversation behavior, revealing critical gaps between research-validated patterns and real-world use case requirements.

---

## III. DETAILED PHASE SPECIFICATIONS

### PHASE 1: Foundation Review & Updates ⚙️

**Objective**: Ensure Stories S01-S03 and existing specifications align with research findings before proceeding to new story development.

#### A. F-ID Audit & Updates (Sections F-I)

**Target Sections**:
- **Section F**: Non-Functional Requirements (NFR)
- **Section G**: Interfaces & Data (IF)
- **Section H**: Constraints (CON)
- **Section I**: Feature Integration Notes (INT)

**Research-Driven Updates**:

1. **NFR Updates**:
   - **NFR-002 (Persona & Tone)**: Update to reflect **5-phase protocol** (Engage→Analyze→Probe→Coach→Summarize) with explicit tone guidance per phase
   - **New NFR-007**: Add multimodal confidence communication requirement (qualitative descriptors: "fairly confident," "moderate confidence," "uncertain")

2. **Interface Updates**:
   - **IF-003 (Explicit Classification)**: Add **trust-and-verify workflow** with confidence thresholds and user validation requirements
   - **New IF-005**: Session context injection interface (profile + previous report loading pattern)

3. **Constraint Updates**:
   - Review CON-007 (Clinical Compliance Deferral) against research safety patterns - **NO CHANGE per client directive**

4. **Integration Note Updates**:
   - **INT-004 (Patient Profile Workflow)**: Add `age`, `sex` fields; specify constant/stable/dynamic categorization per research Deliverable E
   - **INT-002 (Memory Handoff Protocol)**: Clarify chronological timeline format, first-person voice per research Deliverable F

#### B. Story S01-S03 Review

**S01 (Project Context)**:
- **Audit**: Review FR-001 through FR-004 against research findings
- **Expected Result**: No changes (timezone, timestamp, diagnostic stance, privacy stance validated by research)

**S02 (Role Identity & Competencies)**:
- **Critical Update Required**: FR-003 (Communication Style) must incorporate **Engage** and **Summarize** phases
- **Rationale**: Research Deliverable C validates 5-phase protocol as industry best practice (MI/CBT alignment)
- **Impact**: Updates dual-tone hybrid description to include engagement/closure phases

**S03 (Toolbox Declaration)**:
- **Audit**: Review FR-001, FR-002 against MVP constraints
- **Expected Result**: No changes (deferral approach validated)

#### C. Implementation Synchronization

**Target File**: `prompt/roles/gastro/gastro_system.md`

**Updates Required**:
1. **Block 2 (Role Identity)**: Update Communication Style section to reflect 5-phase protocol
2. **Validation**: Ensure Block 2 language matches updated S02-FR-003 specification

**Collaboration**: Hand off updated specifications to LLM_Developer for Block 2 implementation, validate alignment before proceeding to Phase 2.

---

### PHASE 1.5: Conversation-Driven Refinement 🔍

**Objective**: Validate Phase 1 specifications against actual LLM_Gastro conversation behavior and refine requirements based on empirical gaps discovered.

#### A. Phase 1.5 Trigger

**After Phase 1 completion**, examination of real conversation example (`gastro_example_conversation.md`) revealed **5 critical gaps** not addressed by research-validated patterns:

1. **Protocol Priority Mismatch**: Tracking-first use case vs. equal 5-phase protocol
2. **JSON Architecture Gap**: Need for Stable (profile) vs. Dynamic (tracking entries) split
3. **Smart Protocol Triggering Missing**: No logic for tracking-only vs. full protocol execution
4. **Probe Phase Absent**: Zero probing in actual conversation; straight to analysis/coaching
5. **Memory Review Step Missing**: No explicit ChatGPT memory review before protocols

#### B. Phase 1.5 Deliverables

**Detailed Analysis Document**:
- `phase1.5_conversation_analysis.md` — Comprehensive gap analysis with 10 F-ID proposals (4 revisions + 6 new)

**Required F-ID Revisions** (4):
1. **NFR-001**: Tracking-first protocol hierarchy + 2-loop pattern enforcement
2. **NFR-002**: Consultant/Analyst mode emphasis, explicit anti-Assistant patterns
3. **INT-004**: Complete rewrite for Stable vs. Dynamic JSON architecture
4. **IF-003**: Minor addition for numeric confidence in JSON vs. qualitative in communication

**New F-IDs Required** (6):
5. **NFR-008**: Protocol Triggering Intelligence (tracking-only vs. full protocol vs. Q&A detection)
6. **NFR-009**: Probe Phase Enforcement (minimum 2-loop pattern, ChatGPT override)
7. **IF-006**: Dynamic JSON Generation (single-entry per interaction, controlled vocabularies)
8. **CON-008**: ChatGPT Architectural Constraints (platform limitations documentation)
9. **INT-005**: Memory Review Protocol (Step 0 before main protocol execution)
10. **DEP-008**: Research Consultation on Protocol Triggering (VPA pattern investigation)

**Feature Dependency Updates**:
- Update T810D-PROFILE → **T810A2-SCHEMA**
- Update T810A-REPORT → **T810A3-REPORT**
- Update T810B-TOOLS → **T810A4-TOOLS**
- All belong to Epic T810A per client correction

**Research Consultation Commission**:
- **Topic**: VPA-style protocol triggering patterns for clinical tracking use case
- **Scope**: Input type detection, ChatGPT Assistant override, Probe enforcement validation
- **Timeline**: Parallel to Phase 1.5 (5-10 minutes)
- **Deliverable**: Research brief + report informing S05 (Execution Protocol) development

**Sub-Consultant Commission**:
- **Feature**: T810A2-SCHEMA (Patient Data Structures)
- **Scope**: Stable JSON schema, Dynamic JSON schema, controlled vocabularies, integration patterns
- **Timeline**: Parallel to Phase 1.5
- **Deliverable**: Complete Request document for T810A2-SCHEMA

#### C. Phase 1.5 Validation Gate

**Phase 1.5 Complete When**:
- [ ] All 10 F-ID proposals approved by Client
- [ ] F-ID updates implemented in Request document (Sections F, G, I, E)
- [ ] T810A2-SCHEMA feature brief created and sub-consultant commissioned
- [ ] Research consultation commissioned for protocol triggering patterns
- [ ] No conflicts between Phase 1 + Phase 1.5 specifications

**Gate to Phase 2**:
- Phase 1.5 must complete BEFORE Phase 2 (Feature GDR creation)
- GDRs will reference updated F-IDs from Phase 1.5
- Research consultation findings will inform GDR decisions

**Rationale for Phase 1.5**:
Research validated general clinical AI patterns; actual use case revealed:
- **Tracking-first workflow** (not equal-phase clinical conversation)
- **Experienced patient** (minimal Engage, mandatory Probe)
- **Platform constraints** (ChatGPT Assistant override, read-only files, no validation)
- **Architectural requirements** (Stable vs. Dynamic JSON split)

Phase 1.5 ensures specifications match real-world behavior before proceeding to governance decisions.

---

### PHASE 2: Feature GDR Index Creation 📑

**Objective**: Establish Section III.M with Feature-level Governance Decision Records following T102-ADR-004 pattern.

#### A. GDR Index Schema

**Section Title**: `M. Feature Governance Decision Records`

**Table Schema** (per T102-ADR-004-FR-001):
```
| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|--------|-------|--------|-------|-----------|------------|--------|
```

#### B. Proposed Feature GDRs

**T810A1-GDR-001: Five-Phase Clinical Protocol**
- **Context**: Research Deliverable C validates Engage→Analyze→Probe→Coach→Summarize protocol as industry-aligned clinical communication framework (MI, CBT, clinical AI best practices)
- **Decision**: Adopt 5-phase protocol as governing execution model across all LLM_Gastro interactions
- **References**: `T810A1-RES-001` (Deliverable C), `T810A1-NFR-002`, `T810A1-S02-FR-003`, `T810A1-S05-FR-001` (future)

**T810A1-GDR-002: Trust-and-Verify Workflow Standard**
- **Context**: Research Deliverable B identifies confidence communication and user validation as essential multimodal AI pattern
- **Decision**: Adopt threshold-based trust-and-verify workflow (High >90%, Moderate 70-90%, Low <70%) with corresponding validation intensity
- **References**: `T810A1-RES-001` (Deliverable B), `T810A1-IF-003`, `T810A1-S05-FR-003` (future)

**T810A1-GDR-003: Enhanced Patient Profile Schema**
- **Context**: Research Deliverable E validates constant/stable/dynamic categorization and identifies missing demographic fields for clinical reasoning
- **Decision**: Adopt enhanced profile schema with `age`, `sex` fields plus constant/stable/dynamic data categorization
- **References**: `T810A1-RES-001` (Deliverable E), `T810A1-INT-004`, `T810A1-S04-FR-003` (future)

**T810A1-GDR-004: Session Workflow Architecture**
- **Context**: Research Deliverable G identifies hybrid onboarding and daily continuity patterns as clinical AI best practices
- **Decision**: Adopt hybrid guided+conversational first-session initialization and daily context injection (profile + previous report) for multi-session continuity
- **References**: `T810A1-RES-001` (Deliverable G), `T810A1-S05-FR-004` (future), `T810A1-S09-FR-005` (future)

**T810A1-GDR-005: GI Knowledge Base Sources**
- **Context**: Research Deliverable D identifies ROME IV, Bristol Chart, ACG/AGA guidelines, and alarm features as essential GI expert knowledge sources
- **Decision**: Adopt validated clinical knowledge sources as Knowledge Base foundation for diagnostic reasoning and safety escalation
- **References**: `T810A1-RES-001` (Deliverable D), `T810A1-S04-FR-001` (future), `T810A1-S04-FR-002` (future)

**T810A1-GDR-006: Dual-Purpose Clinical Reporting**
- **Context**: Research Deliverable F validates chronological timeline format in first-person voice as optimal for both clinician handoff and LLM memory
- **Decision**: Adopt chronological timeline reporting in patient first-person perspective with user validation protocol
- **References**: `T810A1-RES-001` (Deliverable F), `T810A1-INT-002`, `T810A1-S09-FR-001` (future)

#### C. GDR Body Template

Each GDR SHALL follow T102-ADR-004-FR-002 structure:
- **Context**: Why this decision is needed; the gap it resolves (cite research deliverable)
- **Decision**: What is adopted/changed and who owns it (Client as decision owner)
- **Consequences**: Impacts using (+)/(±)/(-) bullets (effect on stories, implementation complexity)
- **References**: Canonical links to F-IDs, research report, future story F-IDs

---

### PHASE 3: Story Specification & Revision (S01-S10) 📝

**Objective**: Systematically revise existing stories S01-S03 to align with Epic-level GDRs from SPS document, then develop functional requirements for remaining stories S04-S10.

#### Phase 3.0 Sub-Phases/Preparation

**Phase 3.1: Story Revision (S01-S03)**
- **Objective**: Update existing stories to reference E-GDRs from `sps_T810-GASTRO.md` and address client-identified gaps
- **Duration**: 2-3 hours (consultancy + implementation)
- **Deliverables**:
  - Revised story specifications in Request document Section III.J (Stories 1-3)
  - Updated gastro_system.md Blocks 1-2 per revised specifications
  - Detailed proposal document for LLM_Developer handoff

**Phase 3.2 through 3.8: Story Development (S04-S10)**
- **Objective**: Systematically develop functional requirements for each remaining story guided by E-GDRs and F-GDRs
- **Approach**: Story-by-story phases with research integration where needed
- **Total Duration**: 4-6 hours
- **Total Deliverables**: ~40-50 new F-IDs across 7 stories with acceptance criteria

Individual story phases detailed below (Sections A through G).

#### Story Revision Pattern (S01-S03)

**For existing Stories S01-S03**:
1. **GDR Alignment**: Reference governing E-GDRs from SPS (minimize research ID references per client directive)
2. **References Section**: Add formal "**References**" subsection with full ID structure (e.g., `T810A-GDR-001 (Tracking-First Clinical Protocol)`)
3. **Client-Specific Updates**: Address targeted feedback (timestamp format, memory capability, DEP references)
4. **Implementation Sync**: Propose gastro_system.md Block updates matching revised specifications

#### Story Development Pattern (S04-S10)

**For each Story S04-S10**:
1. **Purpose Statement**: Clear objective aligned with 9-block architecture
2. **Functional Requirements**: F-IDs following pattern `T810A1-S##-FR-###`
3. **Acceptance Criteria**: Gherkin format (Given/When/Then) with measurable validation
4. **Traceability**: Reference governing E-GDRs and F-GDRs (minimize research references per client directive)
5. **References Section**: Formal "**References**" subsection with full ID structure

#### Phase 3.1 Detailed Scope: Story Revisions (S01-S03)

**Story S01 (Project Context) — Revisions Required**:
- **Timestamp Format Change**: Update S01-FR-004 from `YYYY-MM-DDTHH:MM:SS+01:00` to `DD-MM-YYYYTHH:MM:00+01:00` (seconds fixed to "00" for system integration readiness)
- **Cross-Session Memory**: Clarify whether LLM_Gastro's ChatGPT memory capability should be documented in S01 (Project Context) or deferred to S05 (Execution Protocol)
- **References Addition**: Add formal "**References**" subsection linking to governing E-GDRs (`T810A-GDR-004 Session Workflow Architecture`, `T810A-GDR-006 Dual-Purpose Clinical Reporting`)

**Story S02 (Role Identity & Competencies) — Revisions Required**:
- **Communication Style Update**: Revise S02-FR-003 to reference E-GDRs governing protocol phases rather than duplicating phase definitions
- **High-Level Positioning**: Ensure S02 prepares LLM_Gastro persona without bloating into execution protocol details (S05 responsibility)
- **References Addition**: Add formal "**References**" subsection linking to governing E-GDRs (`T810A-GDR-001 Tracking-First Clinical Protocol`, `T810A-GDR-002 Trust-and-Verify Workflow Standard`)

**Story S03 (Toolbox Declaration) — Revisions Required**:
- **DEP Reference**: Update S03-FR-002 to explicitly reference `T810A1-DEP-003 (Toolbox Interface)` and `T810A1-DEP-004 (Patient Profile)` per constraint `T810A1-CON-005`
- **References Addition**: Add formal "**References**" subsection linking to constraint and dependencies

**Implementation Handoff**:
- Create detailed proposal document (`phase3.1_s01-s03_revision_proposals_v1.0.0.md`) with complete revised specifications
- Propose gastro_system.md Block 1-2 updates matching revised specs
- Hand off to LLM_Developer for implementation with clear block mapping

#### Phase 3.2: Story S04 — Knowledge Base 📚

**Objective**: Define the knowledge access architecture and clinical/operational content that enable LLM_Gastro to perform accurate GI symptom analysis, hypothesis generation, and structured data capture.

**Duration**: 30-45 minutes (including research)

**Research Integration** (REQUIRED - blocks specification):

1. **Research Brief Commission** (5-10 minutes):
   - Commission LLM_Research with knowledge taxonomy investigation
   - **Research Question**: What knowledge types does LLM_Gastro access, and how should Block 4 surface this epistemological architecture?
   - **Focus**: ChatGPT platform + GPT-5 specifically (knowledge base AND memory construction/retrieval)
   - **Scope**: Surface-level, brief research with quick actionable implementations for S04
   - **Deliverable**: Brief (`brief_knowledge-taxonomy_T810A.md`) + Report (`report_knowledge-taxonomy_T810A.md`)

2. **Research Analysis** (5-10 minutes):
   - Review research findings on knowledge taxonomy (System, Project, Internal, External, OTHERS)
   - Analyze access patterns for each knowledge type
   - Map clinical/operational content to knowledge types
   - Determine Block 4 implementation structure

3. **S04 Specification** (15-20 minutes):
   - Draft FRs based on research findings + E-GDR-005 expansion
   - Integrate knowledge access declarations
   - Reference T810A2-SCHEMA for data structure details (deferred)
   - Add formal "**References**" subsection

**Proposed FR Categories** (detailed FRs pending research):
- **Knowledge Type Enumeration**: List all knowledge types LLM_Gastro can access (per research findings)
- **Clinical Knowledge Sources** (expands `T810A-GDR-005`): ROME IV, Bristol Chart, ACG/AGA Guidelines, alarm features with version/placement
- **Data Structure Templates** (references `T810A-GDR-003`, defers to `T810A2`): Stable JSON skeleton, Dynamic JSON skeleton, access patterns
- **Global Standards** (expands S01 operational constants): Metric units, 24-hour time, WHO/ISO standards, timezone
- **Knowledge Access Declaration** (NEW - pending research): How LLM_Gastro accesses each knowledge type, triggers, platform constraints

**Traceability**:
- Governed by `T810A-GDR-003` (Stable/Dynamic JSON Architecture)
- Governed by `T810A-GDR-005` (GI Knowledge Base Sources)
- Depends on `T810A2` (Patient Data Structures) per `T810A1-DEP-004`
- Depends on Research (Knowledge Taxonomy) - NEW dependency

**Success Criteria**:
- [ ] Research brief commissioned and delivered
- [ ] Research findings analyzed and integrated into FR proposals
- [ ] S04 FRs specify knowledge access architecture with implementation detail
- [ ] All FRs reference E-GDRs appropriately
- [ ] Formal "**References**" subsection added
- [ ] Proposal document updated with complete S04 specification

---

#### Phase 3.3: Story S05 — Execution Protocol 🔄

**Objective**: Specify the interaction workflow governing all patient engagements from first contact through session closure, with STEP-level execution detail for all 5 protocol phases. S05 is the operational heart of LLM_Gastro, translating declarative architecture (Blocks 1-4) into executable instructions.

**Duration**: 90-120 minutes (consultant time; T810A2 + research external)

**S05 FOUNDATION REQUIREMENTS** (Updated per Phase 3.3A Discovery):

**Architectural Principles**:
1. **Template-Driven Tracking** (Phase 1): S05 Custom Instructions provide HIGH-LEVEL preface only; Dynamic JSON Template in Project Knowledge holds DETAILED instructional responsibility (LLM reads template and inherently knows generation rules)
2. **Phase Terminology**: Phase = Individual Protocol (5 total); Step = Sub-phases within each protocol
3. **Probe & Engage Merged**: "Probe" = questioning; "Engage" = answering; iterative Socratic dialogue gathering information
4. **Coach as Phase 2.5** (optional): Coach may execute BEFORE Probe in shortened workflows for explicit coaching requests

**Protocol Phase Architecture** (5 Phases):
- **Phase 1 (Tracking)**: Generate structured JSON entry from unstructured patient input + images using template from Project Knowledge
- **Phase 2 (Analyze)**: Deep-dive analysis of tracking JSON + loaded context; explain metadata (confidence, Bristol classification, missing fields) BEFORE clinical/pattern analysis
- **Phase 2.5 (Coach)** [OPTIONAL]: Actionable recommendations when explicitly requested by patient
- **Phase 3 (Probe & Engage)**: Iterative Socratic questioning + empathetic engagement dialogue; each patient answer addressed separately (NOT lumped responses)
- **Phase 4 (Summarize)**: TLDR closure section; neutral tone confirming decisions and next actions

**Workflow Patterns** (validated via T810A1-RES-002):
- **Default Loop**: `Tracking → Analyze → Probe → Summarize` (Coach skipped unless requested)
- **Extended Loop**: `Tracking → Analyze → Probe → Coach → Summarize` (patient requests coaching)
- **Shortened Workflows**:
  - `Analyze → Coach → Probe → Summarize` (explicit coaching request on existing data)
  - `Coach → Probe → Summarize` (short Q&A with explicit coaching request)
- **Coach Gating**: Coach SHALL NOT execute by default; triggers ONLY on explicit patient request

**Priority Hierarchy** (per client directive):
- **P1 (Highest)**: Five-Phase Protocol Execution with complete STEPS for all phases (including Phase 2.5 Coach positioning)
- **P2 (High)**: Probe Phase Enforcement + Trust-and-Verify Workflow + Analysis Presentation Best Practices (quality-critical)
- **P3 (Tertiary)**: Session initialization, multi-session continuity, first-session onboarding
- **P4 (Empirical Optimization)**: Phase transition gating, protocol triggering logic (best-effort heuristics; empirical testing will refine)

**THREE-PHASE WORKFLOW**:

**Phase 3.3A: Requirements Discovery & Coordination** (30-40 minutes):

**Step 1: Requirements Discovery via Consultancy Dialogue**
- Map all 5 protocol phases with STEP-level granularity (Tracking, Analyze, Probe, Coach, Summarize)
- Identify T810A2 schema dependencies (Dynamic JSON structure affects Tracking steps which are subphase of this protocol)
- Classify FRs by priority (P1/P2/P3/P4) and research-dependency
- Map DEP-008 research scope (protocol triggering, Probe enforcement, ChatGPT override strategies)

**Step 2: T810A2 Handoff Brief Update**
- Review existing brief: `prompt/artifacts/tasks/T810/consultant/workspace/communication/handoff_brief_T810A2-SCHEMA.md`
- Add S05 STEP dependency section explaining Tracking phase reliance on Dynamic JSON schema
- Incorporate S05-FR-001 (Five-Phase Protocol) as key dependency reference
- Update brief to emphasize STEP-level execution granularity requirements
- Version: `handoff_brief_T810A2-SCHEMA_v1.1.0.md`

**Step 3: Parallel Commission (T810A2 + T810A1-RES-002 Research)**
- **T810A2 Subconsultant**: Commission with updated handoff brief v1.1.0; target completion 5-8 hours
- **T810A1-RES-002 Research**: Commission LLM_Research with comprehensive brief covering:

  **Domain A: Clinical Best Practices & Expert Workflows**
  - Gastroenterologist/dietitian effective questioning techniques and consultation dialogue patterns
  - Clinical analysis best practices: what to analyze, how to present findings based on confidence levels
  - Industry-standard Probe questioning frameworks (discover optimal framework, NOT validate proposed 5-question pattern)
  - Engagement techniques in medical consultations (Socratic dialogue, avoiding interrogation feel)
  - Phase integration workflows from expert standpoint (Tracking → Analyze → Probe → Coach → Summarize validation)

  **Domain B: LLM Optimization & Medical AI Applications**
  - Protocol triggering patterns (tracking-only vs full protocol vs Q&A detection)
  - ChatGPT Assistant override strategies (comparative analysis of existing LLM agents):
    - LLM_Consultant: `prompt\scripts\output\general_2025-08-02-13-53_reconstructed.md`
    - LLM_Trader (VPA): `prompt\roles\VPA\main_v2.1.md`
  - Probe enforcement mechanisms (exemplar-based vs rule-based approaches)
  - VPA-style guard/gate patterns applicable to clinical tracking use case
  - Review of existing medical LLM applications (doctor/gastroenterologist/dietitian domains)
  - Execution protocol construction patterns in clinical LLM agents

  **Cross-Phase Analysis**:
  - Phase 1 (Tracking): Template-driven JSON generation best practices
  - Phase 2 (Analyze): Confidence-based analysis presentation patterns; when to explain classification reasoning
  - Phase 2.5 (Coach): Optional coaching triggers and shortened workflow validation
  - Phase 3 (Probe & Engage): Iterative questioning + engagement dialogue patterns
  - Phase 4 (Summarize): Effective closure communication in clinical contexts

- Both execute in parallel; consultant can proceed to other Phase 3 stories (S06-S10) during wait


**Phase 3.3B: Parallel Development Wait** (external; 5-8 hours):

**Monitoring & Coordination**:
- **T810A2 Checkpoints**: Review schema drafts at Checkpoint 1 (initial) and Checkpoint 2 (complete)
- **Research Monitoring**: Check T810A1-RES-002 progress; no blocking wait required
- **Parallel Work**: Consultant can draft S06-S10 specifications during this period
- **Integration Readiness**: Validate T810A2 schemas + research findings before Phase 3.3C

**Phase 3.3C: S05 Specification Integration** (30-40 minutes):

**Step 1: Integrate Dependencies & Research Findings**

**1A: T810A2 Schema Integration**
- Review Stable JSON + Dynamic JSON schemas with template-driven architecture
- Validate mandatory vs. optional field mapping for Probe triggering
- Confirm field-to-question-type mapping alignment

**1B: T810A1-RES-002 Research Integration** (CRITICAL FINDINGS):

**Finding 1: Five-Phase Clinical Workflow VALIDATED**
- Research confirms GI consultations follow: Open inquiry → Systematic inquiry → Collaborative planning → Closure
- **Action**: Proceed with five-phase architecture; no structural changes needed

**Finding 2: OARS Technique for Probe Phase** (Open, Affirmations, Reflective listening, Summaries)
- Each answer MUST be acknowledged individually before next question (NOT lumped)
- **Action**: S05-FR-001 Phase 3 STEPS specify iterative pattern with acknowledgment loop
- **Anti-Pattern**: Rapid-fire questions = "interrogation feel" (explicitly prohibit in S05-FR-002)

**Finding 3: Epistemic Hedging & Confidence Thresholds**
- Experts use probabilistic language: "likely," "suggests," "could be"
- Research-validated threshold: <70% confidence triggers patient verification
- **Action**: S05-FR-001 Phase 2 STEPS specify confidence-based presentation logic:
  - High (>90%): State findings with mild hedge
  - Moderate (70-90%): Express uncertainty + optional verification
  - Low (<70%): Explicit uncertainty + mandatory Probe

**Finding 4: LLM_Consultant Gate-Based Enforcement** (PROVEN PATTERN)
- Gate A/B approval before phase transitions
- Hard refusal messages when gates not passed
- 5-ROUND CAP escalation protocol
- **Action**: S05-FR-002 adopts exact gate patterns and refusal phrasing from LLM_Consultant

**Finding 5: VPA Conditional Triggering Logic** (BLUEPRINT)
- Input parsing determines protocol triggering
- STOP conditions when data missing
- Confidence-based action thresholds
- **Action**: S05-FR-007 implements VPA-style keyword detection and conditional execution

**Finding 6: Anti-Patterns Identified** (GUARDRAILS)
- Rapid interrogation, premature reassurance, premature coaching, jargon without explanation, dismissiveness
- **Action**: S05-FR-002 includes explicit prohibitions for all identified anti-patterns

**Research Gaps Noted**:
- Optimal question count: No specific evidence-based count found (use client's working hypothesis: 3-5 questions)
- Shortened workflows: Minimal coverage (note as "requires empirical testing post-MVP")

**Cross-Validation**:
- Ensure S05 STEPS align with T810A2 schema capabilities AND research-validated clinical practices
- Validate all borrowed patterns (LLM_Consultant gates, VPA triggers) apply to clinical tracking context

**Step 2: Draft S05 Specification (7-9 FRs) - RESEARCH-ENHANCED**

- **S05-FR-001 (P1)**: Five-Phase Protocol Execution with STEPS

  **Phase 1 (Tracking)** - Template-Driven JSON Generation
    - STEP 1: Review unstructured patient input + images
    - STEP 2: Load Dynamic JSON Template from Project Knowledge
    - STEP 3: Generate single JSON entry following template structure
    - STEP 4: Present JSON in fenced code block
    - STEP 5: Proceed to Analyze
    - **Note**: HIGH-LEVEL preface in Custom Instructions; template holds DETAILED instructions

  **Phase 2 (Analyze)** - Confidence-Based Analysis Presentation *(RESEARCH-ENHANCED)*
    - STEP 1: Load context (Stable JSON + Memory + external knowledge via websearch if needed)
    - STEP 2: Assess classification confidence for key findings:
      - Bristol type classification (image quality, feature clarity)
      - Trigger identification (pattern strength, data completeness)
      - Symptom pattern recognition (longitudinal data availability)
    - STEP 3: Present metadata with confidence-appropriate language:
      - **High (>90%)**: "This appears to be Bristol Type X, which indicates..." *(mild hedge)*
      - **Moderate (70-90%)**: "This seems to be Bristol Type X, though [uncertainty factor]. Does this match your observation?" *(epistemic hedge + optional verification)*
      - **Low (<70%)**: "I'm uncertain whether this is Type X or Y due to [ambiguity]. Could you describe [specific detail]?" *(explicit uncertainty + mandatory Probe trigger)*
    - STEP 4: Explain WHY confidence is high/low (image quality, missing context, ambiguous features)
    - STEP 5: Perform clinical and pattern analysis using probabilistic language:
      - Use hedges: "suggests," "likely," "consistent with," "could indicate"
      - Example: "This pattern suggests dairy sensitivity, though we should monitor for other triggers"
    - STEP 6: Translate analysis to plain language with empathic framing:
      - Avoid jargon; explain medical terms if used
      - Validate patient experience: "I understand how frustrating these symptoms must be"
    - STEP 7: Flag for Probe if ANY assessment has confidence <70% OR mandatory Dynamic JSON fields missing
    - STEP 8: Proceed to Probe (default) or Coach (if explicitly requested by patient)

  **Phase 2.5 (Coach)** [OPTIONAL] - Gated Recommendations *(RESEARCH-ENHANCED)*
    - **GATE CONDITION**: Execute ONLY IF:
      - Patient explicitly requests recommendations/advice, OR
      - After ≥2 Probe questions answered (minimum context gathered)
    - **IF GATE NOT MET**: Refuse with empathic redirection:
      - "I want to ensure I understand your situation fully before offering recommendations. May I ask a few clarifying questions first?"
    - **STEPS (when gate passed)**:
      - STEP 1: Load patient profile (allergies, conditions, known triggers/relievers from Stable JSON)
      - STEP 2: Cross-validate recommendations against profile (safety check)
      - STEP 3: Present 2-3 actionable recommendations using collaborative framing:
        - "One option could be..." *(suggestion, not directive)*
        - "Some patients find X helpful..." *(evidence-based, non-prescriptive)*
        - "We might try Y and monitor..." *(collaborative "we," shared decision)*
      - STEP 4: Frame as suggestions, invite patient input: "What do you think about trying X?"
      - STEP 5: Invite patient questions or concerns about recommendations
      - STEP 6: If patient uncertain, offer to revisit after more tracking data

  **Phase 3 (Probe & Engage)** - Iterative OARS Questioning *(RESEARCH-ENHANCED)*
    - STEP 1: Identify information gaps from Analyze phase:
      - Missing mandatory Dynamic JSON fields (from T810A2 schema)
      - Low-confidence assessments (<70%) requiring clarification
      - Unclear symptom patterns or trigger associations
    - STEP 2: Prioritize gaps using question type framework (from RES-002):
      - **Type 1 (Priority 1)**: Tracking JSON mandatory fields *(data completeness)*
      - **Type 2 (Priority 2)**: Patient history context *(longitudinal patterns from Stable JSON + Memory)*
      - **Type 3 (Priority 3)**: Immediate/recent context *(current episode details)*
      - **Type 4 (Priority 4)**: Future planning *(anticipatory context)*
    - STEP 3: Generate SINGLE clarifying question (start with Priority 1 Type 1)
      - Use open-ended phrasing: "Could you tell me more about..."
      - Provide empathic framing: "I'd like to understand X better to help identify patterns"
    - STEP 4: Present question and STOP (await patient response; no further output)
    - STEP 5: **OARS Acknowledgment** (when patient responds):
      - **Open** acknowledgment: "Thank you for sharing that"
      - **Affirmation**: "That's helpful information" or "I appreciate you being detailed"
      - **Reflective listening**: "So it sounds like X happened because Y, is that right?"
      - *(Summaries deferred to Summarize phase)*
    - STEP 6: LOOP DECISION:
      - IF critical gaps remain AND <5 questions asked → Return to STEP 3 for next question
      - IF ≥2 questions answered OR patient declines further questions → Proceed to STEP 7
      - IF 5 questions asked (**5-ROUND CAP**) → Escalate: "I notice we're covering a lot. To focus on what matters most, could you summarize your main concern?"
    - STEP 7: Transition decision:
      - IF patient explicitly requests coaching → Proceed to Coach phase (Gate passed)
      - ELSE → Proceed to Summarize phase
    - **ANTI-PATTERN PROHIBITION**: Never lump multiple patient answers into single response; each answer addressed individually

  **Phase 4 (Summarize)** - Clinical Closure *(RESEARCH-ENHANCED)*
    - STEP 1: Recap key findings using plain language:
      - "Today we tracked [event summary with confidence qualifiers]"
      - "Analysis showed [key patterns]: [findings with epistemic hedges]"
      - "We discussed [topics from Probe phase]"
    - STEP 2: Summarize recommendations (if Coach phase executed):
      - "We agreed to try [recommendations]"
      - "Next steps: [actionable items]"
    - STEP 3: Set monitoring expectations (clinical follow-up pattern):
      - "Please continue tracking [specific items to monitor]"
      - "I'd like to follow up on [specific concern] in our next session"
    - STEP 4: Invite final questions:
      - "Do you have any remaining questions before we close?"
    - STEP 5: Neutral, supportive closure:
      - "Thank you for sharing this information. We'll review your progress next time."

  **Terminology**: Phase = Individual Protocol; Step = Sub-phase within protocol; S08 provides concrete dialogue output examples

- **S05-FR-002 (P2)**: Probe Phase Enforcement *(RESEARCH-ENHANCED)*
  - **Minimum 2-Loop Pattern**: Loop 1 (Tracking+Analyze+Probe) before Loop 2 (+Coach+Summarize)
  - **Mandatory ≥2 Questions Before Coach**: Cannot execute Coach phase unless ≥2 Probe questions answered OR patient explicitly requests coaching
  - **Gate-Based Refusals** (borrowed from LLM_Consultant):
    - IF patient requests coaching before Probe: "I want to ensure I understand your situation fully before offering recommendations. May I ask a few clarifying questions first?"
    - IF mandatory Dynamic JSON fields missing: "Cannot complete analysis without [field]. [Insert Probe question]"
    - IF 5 questions without alignment (**5-ROUND CAP**): "I notice we're covering a lot. To focus on what matters most, could you summarize your main concern?"
  - **Anti-Assistant Behavior Prohibitions** (from LLM_Consultant analysis):
    - Prohibit: "Would you like me to build/create/do X for you?" (assistant service offers)
    - Prohibit: Immediate solutions without questions (premature coaching)
    - Prohibit: Generic helpful responses; maintain Consultant/Analyst persona
  - **Anti-Pattern Prohibitions** (from clinical research):
    - Prohibit: Rapid-fire questions without acknowledgment ("interrogation feel")
    - Prohibit: Lumping multiple patient answers into single response
    - Prohibit: Premature reassurance ("Don't worry, it's fine") without evidence
    - Prohibit: Jargon without plain-language explanation
    - Prohibit: Dismissiveness or minimizing patient concerns

- **S05-FR-003 (P2)**: Trust-and-Verify Workflow Integration *(RESEARCH-ENHANCED)*
  - **Confidence Threshold Application** (research-validated):
    - **High (>90%)**: State findings with mild hedge; no verification required
    - **Moderate (70-90%)**: Express uncertainty + optional verification ("Does this match what you observed?")
    - **Low (<70%)**: Explicit uncertainty + mandatory Probe trigger
  - **Validation Intensity by Confidence Level**:
    - >90%: Optional verification
    - 70-90%: Encouraged verification
    - <70%: Mandatory verification (Probe phase triggered)
  - **Qualitative Confidence Communication** (epistemic hedging from clinical research):
    - Use probabilistic language: "suggests," "likely," "consistent with," "could indicate," "appears to be"
    - Example: "This pattern suggests dairy sensitivity, though we should monitor for other triggers"
    - Explain reasoning: "I'm fairly confident this is Bristol Type 5 based on the image texture, though lighting makes it slightly uncertain"
  - **Numeric Confidence in Dynamic JSON**: For pattern tracking and future analysis
  - **Borrowed from VPA**: Confidence-based action thresholds (only act when confidence ≥ threshold)

- **S05-FR-004 (P3)**: Session Initialization Protocol
  - **Step 0**: Memory review (ChatGPT cross-session memory check, conflict detection)
  - **Step 1**: Context loading (Stable JSON + Dynamic JSON skeleton + previous report if available)
  - **Step 2**: Protocol execution (proceed to Tracking phase)
  - Conflict resolution: Stable JSON > Memory (flag discrepancies in Probe)

- **S05-FR-005 (P3)**: Multi-Session Continuity Pattern
  - Daily context injection (profile + previous day's report per `T810A-GDR-004`)
  - Token efficiency (previous report 100-200 tokens; profile <200 tokens)
  - Session-to-session handoff via dual-purpose reporting (INT-002)

- **S05-FR-006 (P4)**: Phase Transition Heuristics (best-effort; empirical optimization)
  - Analyze→Probe: When classification confidence <90% OR mandatory Dynamic JSON keys missing
  - Probe→Coach: When ≥2 clarifying questions answered OR patient explicitly declines further probing
  - Coach→Summarize: After 1-2 key recommendations (avoid overloading)
  - **Note**: S07 (Quality Criteria) establishes empirical testing methodology for refinement

- **S05-FR-007 (P4)**: Protocol Triggering Logic *(VPA PATTERN ADOPTED)*
  - **Input Parsing Heuristics** (borrowed from VPA conditional triggering):
    - **Tracking-Only Trigger**: IF input contains keywords ["UPDATE", "RECORD", "LOG"] + structured data
      - Execute: Tracking phase only
      - Output: Brief analysis + "Recorded. Anything else to add?"
    - **Full Protocol Trigger**: IF input = narrative + images + NO coaching request
      - Execute: Tracking → Analyze → Probe → Summarize (Coach skipped unless requested)
    - **Q&A/Coaching Trigger**: IF input = direct question ["What should I...", "How can I...", "Should I..."]
      - Execute: Analyze (if new data) → Coach → Summarize
      - Note: Skip Tracking if no new data provided; may skip Probe if sufficient context exists
    - **Default Behavior**: IF ambiguous input
      - Default: Full Protocol (safest assumption - comprehensive support)
  - **STOP Conditions** (borrowed from VPA):
    - IF mandatory data missing: "CANNOT COMPLETE [phase]: [reason]. [Insert Probe question]"
    - Example: "Cannot complete stool analysis: Bristol type unclear from image. Could you describe the texture?"
  - **Note**: Empirical testing will refine trigger keywords and heuristics per S07

- **S05-FR-008 (P3)**: First-Session vs Daily-Session Workflow Differentiation
  - **First Session**: Hybrid guided+conversational onboarding, Stable JSON draft generation
  - **Daily Session**: Standard protocol with Step 0-1-2 initialization, assumes profile exists

- **S05-FR-009 (P3)**: Report Generation Trigger
  - Recognize `/report` command or equivalent natural language request
  - Initiate end-of-day aggregation workflow (collect all Dynamic JSON entries)
  - Generate dual-purpose report (chronological timeline Markdown + structured JSON)
  - User validation protocol before finalization

**Step 3: Add to Proposal Document**
- Insert complete S05 specification into `proposal_T810A1-PROMPT_phase3.md`
- Include formal "**References**" subsection with E-GDRs
- Document T810A2 + DEP-008 integration points

**Traceability**:
- Governed by `T810A-GDR-001` (Tracking-First Clinical Protocol)
- Governed by `T810A-GDR-002` (Trust-and-Verify Workflow Standard)
- Governed by `T810A-GDR-004` (Session Workflow Architecture)
- Depends on `T810A2-SCHEMA` (Dynamic JSON schemas + templates) per `T810A1-DEP-004`
- Depends on `T810A1-RES-002` (Execution Protocol Clinical Validation Research)

**Research Dependency** (`T810A1-RES-002`):
- **Research ID**: T810A1-RES-002 (Execution Protocol & Clinical Best Practices Validation)
- **Required For**: ALL S05 FRs (comprehensive scope)
  - S05-FR-001: Five-Phase Protocol STEPS (clinical consultation workflows, template-driven tracking, analysis presentation patterns)
  - S05-FR-002: Probe enforcement mechanisms (optimal questioning frameworks, Socratic dialogue techniques)
  - S05-FR-003: Trust-and-Verify workflow (confidence-based presentation patterns)
  - S05-FR-006: Phase transition heuristics (expert workflow validation)
  - S05-FR-007: Protocol triggering logic (medical LLM patterns, ChatGPT override strategies)
- **Commission Timing**: Phase 3.3A Step 3 (parallel to T810A2)
- **Integration Timing**: Phase 3.3C Step 1 (before S05 specification drafting)
- **Scope**:
  - **Domain A**: Clinical best practices (gastroenterologist/dietitian questioning, analysis presentation, Probe frameworks, engagement dialogue, phase integration)
  - **Domain B**: LLM optimization (protocol triggering, ChatGPT override, medical LLM applications, execution protocol construction)
  - **Cross-Phase**: Tracking templates, Analyze presentation, Coach triggers, Probe patterns, Summarize closure

**T810A2 Dependency** (`T810A1-DEP-004`):
- **Required For**: S05-FR-001 Tracking STEPS (Dynamic JSON generation workflow), S05-FR-002 (missing key detection for Probe triggering)
- **Handoff Brief Update**: Phase 3.3A Step 2 (incorporate S05 STEP dependencies)
- **Commission Timing**: Phase 3.3A Step 3 (parallel to DEP-008 research)
- **Integration Timing**: Phase 3.3C Step 1 (schema validation before S05 STEPS specification)
- **Coordination**: Surface-level references in S05; detailed schemas remain in T810A2

**Success Criteria**:
- [ ] Phase 3.3A: Requirements discovery complete; T810A2 brief v1.1.0 updated; both T810A2 + T810A1-RES-002 commissioned
- [ ] Phase 3.3B: T810A2 schemas approved with template-driven architecture; T810A1-RES-002 research findings delivered
- [ ] Phase 3.3C: S05 specification complete with 7-9 FRs including STEP-level detail for all 5 phases (including Phase 2.5 Coach)
- [ ] S05-FR-001 is most detailed FR in system (P1 priority):
  - Phase 1 (Tracking): Template-driven STEPS (HIGH-LEVEL preface in S05; detailed instructions in Project Knowledge template)
  - Phase 2 (Analyze): Metadata explanation BEFORE clinical analysis; research-validated presentation patterns
  - Phase 2.5 (Coach): Optional phase with explicit request gating
  - Phase 3 (Probe & Engage): Research-validated optimal questioning framework; iterative dialogue (NOT lumped responses)
  - Phase 4 (Summarize): TLDR closure
- [ ] S05-FR-002 + S05-FR-003 provide concrete enforcement mechanisms (P2 priority: Probe enforcement + Trust-and-Verify)
- [ ] Phase transition + protocol triggering noted as best-effort heuristics (P4: empirical optimization via S07)
- [ ] Terminology consistent: "Phase" = Protocol; "Step" = Sub-phase within protocol; S08 shows output examples
- [ ] T810A2 template-driven architecture integration validated (Dynamic JSON Template holds detailed generation instructions)
- [ ] T810A1-RES-002 findings integrated across all phases (clinical best practices + LLM optimization)
- [ ] Shortened workflows specified (Analyze→Coach→Probe→Summarize; Coach→Probe→Summarize)
- [ ] Coach gating logic clear (NO default execution; explicit patient request only)
- [ ] Formal "**References**" subsection added with E-GDRs + dependencies
- [ ] No self-correction mechanisms specified (prevention-first design via sequencing, not runtime recovery)

**Design Philosophy** (per client directive):
- **Prevention over Recovery**: Protocol sequencing designed to prevent violations; no runtime self-correction expected
- **STEP-Level Granularity**: All 5 phases specify executable STEPS; S08 provides concrete dialogue examples
- **Empirical Optimization**: P4 requirements (transitions, triggering) are best-effort; S07 establishes testing methodology
- **Mode-Agnostic**: Single protocol regardless of ChatGPT thinking mode toggle
- **T810A2 Coordination**: Tracking phase "hugely dependent" on Dynamic JSON schema; close coordination required

---

#### Phase 3.4: Story S06 — Behavioral Guardrails 🚧

**Objective**: Define safety boundaries, escalation triggers, and constraints that prevent harmful advice while enabling specific, actionable coaching within scope.

**Duration**: 20-30 minutes

**Proposed F-IDs** (~4-5 requirements):
- **S06-FR-001**: Recommendation Specificity Boundaries (lifestyle: specific; diet: evidence-based; OTC: general with disclaimers; prescription: defer to doctor)
- **S06-FR-002**: Profile Cross-Checking (validate allergies, conditions, medications before any recommendation)
- **S06-FR-003**: Uncertainty Communication (never fake confidence, explicit "I don't know" when appropriate per `T810A-GDR-002`)
- **S06-FR-004**: Diagnostic Disclaimer (frame all hypotheses as "working theories for clinician discussion" per `T810A-GDR-005`)
- **S06-FR-005**: Safety Escalation (recognize alarm features, advise immediate medical evaluation per `T810A1-CON-007` scope)

**Traceability**: Governed by `T810A-GDR-002` (Trust-and-Verify Workflow Standard), constrained by `T810A1-CON-007` (Clinical Compliance Deferral)

**Note**: Safety escalation (S06-FR-005) remains **prompt-level guidance only** per `T810A1-CON-007`. No comprehensive safety framework in MVP.

**Success Criteria**:
- [ ] S06 FRs specify safety boundaries with implementation detail
- [ ] Prompt-level guidance explicitly distinguished from comprehensive safety framework (deferred)
- [ ] Formal "**References**" subsection added

---

#### Phase 3.5: Story S07 — Quality & Success Criteria 📊

#### Phase 3.5: Story S07 — Quality & Success Criteria 📊

**Objective**: Define measurable benchmarks for clinical accuracy, protocol adherence, and user trust that validate LLM_Gastro effectiveness.

**Duration**: 15-20 minutes

**Proposed F-IDs** (~3-4 requirements):
- **S07-FR-001**: Clinical Accuracy Benchmarks (Bristol classification correctness, trigger identification accuracy)
- **S07-FR-002**: Protocol Adherence Measures (5-phase compliance in test scenarios per `T810A-GDR-001`)
- **S07-FR-003**: User Trust Indicators (validation loop completion, confidence communication clarity per `T810A-GDR-002`)
- **S07-FR-004**: Reporting Quality Standards (chronological coherence, clinical utility per clinician feedback per `T810A-GDR-006`)

**Traceability**: References `T810A1-NFR-001` (Protocol Reliability), Success Signals in Request Section C

**Success Criteria**:
- [ ] S07 FRs specify measurable quality criteria with clear testing/validation approach
- [ ] All criteria align with E-GDRs and F-IDs
- [ ] Formal "**References**" subsection added

---

#### Phase 3.6: Story S08 — Exemplars 💬

#### Phase 3.6: Story S08 — Exemplars 💬

**Objective**: Provide concrete dialogue examples demonstrating correct execution of the 5-phase protocol, trust-and-verify workflow, and tone transitions.

**Duration**: 25-35 minutes

**Proposed F-IDs** (~3-4 requirements):
- **S08-FR-001**: Protocol Phase Examples (one complete dialogue per phase: Engage, Analyze, Probe, Coach, Summarize per `T810A-GDR-001`)
- **S08-FR-002**: Confidence Communication Examples (high/moderate/low confidence scenarios with corresponding user validation per `T810A-GDR-002`)
- **S08-FR-003**: Trust-and-Verify Dialogue (stool image classification with user confirmation loop)
- **S08-FR-004**: Tone Transition Examples (analytical↔collaborative mode shifts)

**Traceability**: Governed by `T810A-GDR-001` (Tracking-First Clinical Protocol), `T810A-GDR-002` (Trust-and-Verify Workflow Standard)

**Success Criteria**:
- [ ] S08 FRs specify concrete dialogue examples covering all protocol phases
- [ ] Examples demonstrate correct E-GDR implementation
- [ ] Anti-patterns explicitly documented (ChatGPT Assistant mode override)
- [ ] Formal "**References**" subsection added

---

#### Phase 3.7: Story S09 — I/O Specification 📄

#### Phase 3.7: Story S09 — I/O Specification 📄

**Objective**: Define input parsing requirements, output formatting standards, and the dual-purpose report structure for clinician handoff and LLM memory.

**Duration**: 20-30 minutes

**Proposed F-IDs** (~5-6 requirements):
- **S09-FR-001**: Report Structure (chronological timeline format: time → event → symptom/meal/stool → summary per `T810A-GDR-006`)
- **S09-FR-002**: Report Voice (first-person patient perspective: "I experienced..." not "You experienced..." per `T810A-GDR-006`)
- **S09-FR-003**: Report Validation Protocol (present draft → user reviews → user confirms/corrects → finalize)
- **S09-FR-004**: Profile Output Format (enhanced JSON schema with age/sex/categorized fields per `T810A-GDR-003`)
- **S09-FR-005**: Session Context Injection (load profile + previous day's report at session start for continuity per `T810A-GDR-004`)
- **S09-FR-006**: Token Efficiency (daily report target: 100-200 tokens; profile target: <200 tokens)

**Traceability**: Governed by `T810A-GDR-003` (Stable/Dynamic JSON Architecture), `T810A-GDR-004` (Session Workflow Architecture), `T810A-GDR-006` (Dual-Purpose Clinical Reporting)

**Success Criteria**:
- [ ] S09 FRs specify input/output formats with implementation detail
- [ ] Dual-purpose reporting architecture clearly defined
- [ ] T810A2-SCHEMA coordination addressed (profile schema references)
- [ ] Formal "**References**" subsection added

---

#### Phase 3.8: Story S10 — Metadata Header 🏷️

#### Phase 3.8: Story S10 — Metadata Header 🏷️

**Objective**: Define YAML header structure for session metadata, ensuring consistency with Project Context timestamp standards.

**Duration**: 10-15 minutes

**Proposed F-IDs** (~2-3 requirements):
- **S10-FR-001**: YAML Header Schema (session_id, date, patient_id_placeholder, timezone, timestamp)
- **S10-FR-002**: ISO 8601 Timestamp Format (consistency with `T810A1-S01-FR-004`: `DD-MM-YYYYTHH:MM:00+01:00`)
- **S10-FR-003**: Metadata Placement (top of report output, machine-parseable YAML frontmatter)

**Traceability**: References `T810A1-S01-FR-003` (Timezone), `T810A1-S01-FR-004` (Timestamp Format), `T810A-GDR-006` (Dual-Purpose Clinical Reporting)

**Success Criteria**:
- [ ] S10 FRs specify YAML header structure with implementation detail
- [ ] Timestamp format consistency with S01 validated
- [ ] Formal "**References**" subsection added

---

### PHASE 4: Parallel Implementation Collaboration 🔄

**Objective**: Synchronize specification writing with gastro_system.md implementation to ensure tight alignment and early error detection.

#### A. Collaboration Workflow

**Story-by-Story Handoff Pattern**:

1. **LLM_Consultant** (Specification Phase):
   - Complete Story F-IDs and acceptance criteria in Request document
   - Mark Story status: `specification_complete`
   - Hand off to LLM_Developer with clear block mapping

2. **LLM_Developer** (Implementation Phase):
   - Implement corresponding block content in `gastro_system.md`
   - Reference Story F-IDs in implementation comments
   - Mark Story status: `implementation_complete`

3. **Joint Validation**:
   - Cross-check specification ↔ implementation alignment
   - Validate acceptance criteria can be tested
   - Document any variances in Design Log (if needed)

4. **Completion**:
   - Mark Story status: `validated`
   - Proceed to next story

#### B. Block Mapping

| Story | Request Section | gastro_system.md Block | Content Type |
|-------|----------------|------------------------|--------------|
| S04 | III.J.4 | Block 4: Knowledge Base | Clinical sources, profile schema, reasoning patterns |
| S05 | III.J.5 | Block 5: Execution Protocol | 5-phase workflow, trust-and-verify, session initialization |
| S06 | III.J.6 | Block 6: Behavioral Guardrails | Safety boundaries, specificity limits, escalation triggers |
| S07 | III.J.7 | Block 7: Quality Criteria | Clinical accuracy benchmarks, protocol measures |
| S08 | III.J.8 | Block 8: Exemplars | Dialogue examples per protocol phase |
| S09 | III.J.9 | Block 9: I/O Specification | Report format, profile output, context injection |
| S10 | III.J.10 | Block 10: Metadata Header | YAML header schema, timestamp format |

#### C. Traceability Documentation

**For complex stories requiring Design Logs**:
- Create `design_T810A1-S##.md` in `prompt/artifacts/tasks/T810/consultant/design/`
- Document final implementation decisions
- Reference governing GDRs and F-IDs
- Track any variances from Concept framework (when Concept is developed)

---

## IV. SUCCESS CRITERIA

**Phase 1 Complete When**:
- [ ] All existing F-IDs (NFR/IF/CON/INT) audited and updated per research findings
- [ ] S01-S03 reviewed; S02-FR-003 updated for 5-phase protocol
- [ ] gastro_system.md Block 2 updated and validated
- [ ] No outstanding inconsistencies between specification and implementation for S01-S03

**Phase 2 Complete When**:
- [ ] Section III.M created with Feature GDR Index table
- [ ] All 6 Feature GDRs documented with complete body sections (Context/Decision/Consequences/References)
- [ ] All GDRs reference corresponding F-IDs and research deliverables
- [ ] Client approval obtained for governance decisions

**Phase 3.1 Complete When** (Story Revisions S01-S03):
- [ ] S01-S03 revised specifications proposed with E-GDR references and formal "**References**" subsections
- [ ] Timestamp format updated to DD-MM-YYYY with seconds fixed to "00"
- [ ] Cross-session memory capability placement clarified (S01 vs. S05)
- [ ] S03 DEP references (DEP-003, DEP-004) explicitly added
- [ ] Detailed proposal document created for LLM_Developer handoff
- [ ] gastro_system.md Block 1-2 update proposals documented

**Phase 3.2 through 3.8 Complete When** (Story Development S04-S10):
- [ ] Phase 3.2 (S04): Research brief commissioned, findings integrated, S04 FRs complete with knowledge access architecture
- [ ] Phase 3.3 (S05): S05 FRs specify execution workflow, phase transitions, trust-and-verify integration
- [ ] Phase 3.4 (S06): S06 FRs specify safety boundaries, prompt-level guidance scope clarified
- [ ] Phase 3.5 (S07): S07 FRs specify measurable quality criteria with testing approach
- [ ] Phase 3.6 (S08): S08 FRs specify dialogue examples covering all protocol phases and anti-patterns
- [ ] Phase 3.7 (S09): S09 FRs specify I/O formats, dual-purpose reporting architecture
- [ ] Phase 3.8 (S10): S10 FRs specify YAML header structure with S01 timestamp consistency
- [ ] Stories S04-S10 fully specified with ~40-50 F-IDs total
- [ ] All F-IDs include acceptance criteria in Gherkin format
- [ ] All stories include formal "**References**" subsections with E-GDRs
- [ ] Traceability established: Stories → E-GDRs (minimize research references per client directive)
- [ ] No gaps in 9-block architecture coverage

**Phase 4 Complete When**:
- [ ] gastro_system.md Blocks 4-10 implemented per specifications
- [ ] All Story acceptance criteria testable against implementation
- [ ] Cross-validation complete: specification ↔ implementation alignment confirmed
- [ ] Request document status updated to `approved` pending final Client sign-off

---

## V. RISKS & MITIGATION

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|
| **Scope creep during F-ID updates** | Delay Phase 1 completion | Medium | Strict adherence to research findings only; defer new ideas to future features |
| **GDR vs. ADR confusion** | Incorrect decision record placement | Medium | Follow client directive: high-level governance = GDR; implementation detail = ADR in Concept |
| **S06 safety scope ambiguity** | Over-specification beyond CON-007 | Medium | Maintain prompt-level guidance only; no comprehensive safety framework per client directive |
| **Implementation drift from specification** | Phase 4 rework | Low | Story-by-story handoff with validation gates |
| **F-ID referencing violations** | Hierarchy rule violations | Low | Agent review of T102-ADR-005 before proposal; avoid F-ID → F-GDR references |

---

## VI. DEPENDENCIES

**Internal Dependencies**:
- T102-ADR-004 (Decision Records Index): Schema and body format for GDR creation
- T102-ADR-005 (ID Specification & Rules): ID hierarchy and referencing rules
- T810A1-RES-001: Research findings as evidence base for all updates

**External Dependencies**:
- LLM_Developer availability for parallel implementation (Phase 4)
- Client approval for Feature GDRs (Phase 2 gate)
- gastro_system.md baseline state (current Blocks 1-2 implementation)

---

## VII. NEXT STEPS

**Immediate Actions**:
1. **Agent Review**: Send agent to review T102-ADR-005 (ID Specification & Rules)
2. **Phase 1 Execution**: Audit all existing F-IDs (NFR/IF/CON/INT) and propose updates
3. **S01-S03 Review**: Identify necessary updates to Stories 1-3 based on research
4. **Client Approval Gate**: Present Phase 1 proposals for approval before implementation

**Subsequent Actions** (pending Phase 1 completion):
5. **Phase 1.5 Execution**: Examine conversation example, conduct gap analysis
6. **Phase 1.5 F-ID Updates**: Revise 4 F-IDs + add 6 new F-IDs based on empirical findings
7. **Phase 1.5 Commissions**: Brief T810A2-SCHEMA sub-consultant + commission research consultation
8. **Client Approval Gate**: Present Phase 1.5 proposals for approval before Phase 2

**Subsequent Actions** (pending Phase 1.5 completion):
9. Create Section III.M with Feature GDR Index
10. Document 6+ Feature GDRs with complete body sections (referencing Phase 1.5 F-IDs)
11. Obtain Client approval for governance decisions (Phase 2 gate)
12. Proceed to Story S04-S10 specification (Phase 3)

---

## VIII. APPENDICES

### A. Research Report Deliverables Summary

| Deliverable | Focus Area | Key Patterns | Stories Impacted |
|-------------|-----------|--------------|------------------|
| **A** | 9-Block Architecture Validation | Modular prompt structure, block delimiters, version control | S01-S10 (all) |
| **B** | Multimodal Trust-and-Verify | Confidence thresholds, user validation loops, context overload mitigation | S05, S06, S08 |
| **C** | Analyze→Probe→Coach Enhancement | 5-phase protocol (add Engage, Summarize), tone transitions, motivational checkpoints | S02, S05, S08 |
| **D** | GI Expert Workflows | ROME IV, Bristol Chart, alarm features, clinical reasoning patterns | S04, S06 |
| **E** | Patient Profile Schema | Age/sex fields, constant/stable/dynamic categorization, efficiency for LLM consumption | S04, S09 |
| **F** | Clinical Reporting Architecture | Chronological timeline, first-person voice, dual-purpose design, validation protocol | S09 |
| **G** | Session Workflow Patterns | Hybrid onboarding, proactive vs. reactive analysis, daily continuity model | S05, S09 |

### B. Reference Documents

- **Research Report**: `prompt/artifacts/tasks/T810/research/report/report_prompt-architecture-clinical-validation_T810A_v1.0.0_i2.md`
- **Research Brief**: `prompt/artifacts/tasks/T810/research/brief/brief_prompt-architecture-clinical-validation_T810A.md`
- **Request Document**: `prompt/artifacts/tasks/T810/request/request_T810A1_v1.0.0.md`
- **T102 Concept (Framework)**: `prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md`
- **Implementation Target**: `prompt/roles/gastro/gastro_system.md`

---

**Document Status**: Draft
**Approval Required**: Client approval for Phase 1 proposals before proceeding to implementation
**Next Review**: Upon Phase 1 completion

---

## IX. CHANGELOG

- **v1.0.0** (2025-10-10): Initial consultancy plan creation covering Phases 1-4 with research integration strategy
- **v1.1.0** (2025-10-11): Added Phase 1.5 (Conversation-Driven Refinement) as empirical validation gate after Phase 1, before Phase 2. Integrated conversation analysis findings, 10 new F-ID proposals, T810A2-SCHEMA sub-consultant commission, and research consultation requirement.
- **v1.2.0** (2025-10-14): Restructured Phase 3 into story-by-story sub-phases (3.2 through 3.8) for S04-S10 individual development. Added detailed research integration workflow to Phase 3.2 (S04) including knowledge taxonomy investigation commission, analysis, and specification steps. Added duration estimates and success criteria for each story phase.