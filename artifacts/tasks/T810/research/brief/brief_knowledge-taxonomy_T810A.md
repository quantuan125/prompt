---
artifact_type: 'RESEARCH'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1-PROMPT'
research_id: 'T810A-RES-003'
version: '1.0.0'
iteration: '1'
date: '2025-10-14'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: LLM_Gastro Knowledge Taxonomy & Access Patterns

## I. EXECUTIVE SUMMARY

This research brief commissions a focused, **surface-level investigation** into ChatGPT platform and GPT-5 knowledge architecture specifically to inform Story S04 (Knowledge Base) specification for Feature T810A1-PROMPT. The research aims to enumerate distinct knowledge types LLM_Gastro can access, define access patterns for each type, and recommend Block 4 implementation structure that surfaces this epistemological architecture to the agent. This is a **quick, actionable research** delivery (5-10 minutes) focused exclusively on ChatGPT/GPT-5 platform capabilities, NOT a comprehensive epistemology investigation.

**Target Deliverable**: Actionable recommendations for S04 FR proposals enabling LLM_Gastro to understand its knowledge access matrix.

## II. RESEARCH SCOPE & OBJECTIVES

### **Primary Research Questions**

1. **ChatGPT Platform Knowledge Architecture**
   - What distinct knowledge types does ChatGPT provide to custom GPTs?
   - How does GPT-5 (or current ChatGPT model) handle knowledge base vs. memory distinction?
   - What are the platform-native knowledge sources available to LLM_Gastro?

2. **Knowledge Type Taxonomy**
   - **System Knowledge**: ChatGPT's cross-session memory system - how is it constructed, fed, retrieved?
   - **Project Knowledge**: File uploads (session-specific vs. cross-session project knowledge) - access patterns, limitations?
   - **Internal Knowledge**: GPT-5 model training knowledge - scope, limitations, update frequency?
   - **External Knowledge**: Native search tools (web search, browsing) - availability, invocation patterns?
   - **OTHERS**: Any additional knowledge sources not captured above?

3. **Access Pattern Analysis**
   - For each knowledge type, how does the LLM access it?
     - Automatic loading at session start?
     - User-mediated (manual file upload)?
     - Tool-invoked (search command)?
     - Context injection?
   - What triggers access for each knowledge type?
   - What are the platform constraints per `T810A1-CON-008`?

4. **Content Mapping for LLM_Gastro**
   - **Clinical sources** (ROME IV, Bristol Chart, guidelines) → Which knowledge type(s)?
   - **Patient profile** (Stable JSON per `T810A-GDR-003`) → Which knowledge type(s)?
   - **Dynamic JSON skeleton** → Which knowledge type(s)?
   - **Session reports** (previous day summaries) → Which knowledge type(s)?

5. **Block 4 Implementation Pattern**
   - How should the system prompt (Block 4) surface this architecture?
   - Should Block 4 enumerate knowledge types explicitly?
   - Should Block 4 declare access patterns?
   - Should Block 4 provide content inventory per knowledge type?
   - What level of detail is appropriate for MVP system prompt?

### **Secondary Research Objectives**

6. **ChatGPT Memory System Deep Dive**
   - How does ChatGPT's cross-session memory work (automatic updates, persistence, user control)?
   - How does memory interact with uploaded files (project knowledge)?
   - What's the relationship between memory and Stable JSON (manual patient profile)?
   - How should `T810A1-INT-005` (Memory Review Protocol) be implemented given platform architecture?

7. **File Upload Architecture**
   - Difference between session-specific file uploads vs. cross-session project knowledge?
   - File persistence patterns across sessions?
   - Read-only constraints per `T810A1-CON-008` - how do these manifest?
   - Token/context window implications for file-based knowledge?

## III. RESEARCH DELIVERABLES

### **A. Knowledge Type Taxonomy Report**
- **Enumeration**: Complete list of distinct knowledge types LLM_Gastro can access on ChatGPT platform
- **Definitions**: Clear definition of each knowledge type (scope, persistence, authority)
- **Platform Validation**: Confirmation these types are ChatGPT/GPT-5 native capabilities

### **B. Access Pattern Matrix**
- **Access Mechanism Table**: For each knowledge type:
  - How accessed (automatic, manual, tool-invoked)
  - When accessed (session start, on-demand, continuous)
  - Who controls access (platform, user, agent)
  - Platform constraints (read-only, token limits, persistence)
- **Trigger Conditions**: What events/actions trigger access for each type

### **C. Content-to-Knowledge Mapping**
- **LLM_Gastro Content Inventory**: Clinical sources, patient profile, JSON skeletons, reports
- **Knowledge Type Assignment**: Which content belongs in which knowledge type(s)
- **Implementation Recommendations**: How Block 4 should reference each content category

### **D. Block 4 Implementation Structure**
- **Recommended Format**: Specific structure for Block 4 content (subsections, headings, declaration patterns)
- **Knowledge Type Declaration Template**: How to enumerate knowledge types in system prompt
- **Access Pattern Declaration Template**: How to surface access mechanisms to LLM_Gastro
- **Content Inventory Template**: How to list what's available in each knowledge type
- **Implementation Example**: Concrete Block 4 snippet demonstrating recommended structure

### **E. Memory vs. Stable JSON Architecture Clarification**
- **INT-005 Implementation Guidance**: How Memory Review Protocol should work given ChatGPT memory architecture
- **Conflict Resolution Patterns**: When memory and Stable JSON conflict, how to resolve (Stable JSON precedence per `T810A-GDR-004`)
- **Practical Workflow**: Step-by-step memory review → profile loading → protocol execution sequence

### **F. S04 FR Proposal Recommendations**
- **Suggested FR Categories**: Based on taxonomy findings, what FR categories should S04 include?
- **Priority Ranking**: Which FRs are essential vs. nice-to-have for MVP Block 4?
- **Implementation Detail Scope**: How detailed should FRs be (high-level architecture vs. specific content listing)?

## IV. RESEARCH METHODOLOGY

### **A. Platform Documentation Analysis**

**Primary Sources**:
- OpenAI ChatGPT Custom GPT documentation
- OpenAI GPT-5 (or current model) technical specifications
- ChatGPT Memory system user documentation
- ChatGPT file upload and project knowledge capabilities
- OpenAI system prompt best practices

**Focus Areas**:
- Knowledge persistence patterns (session-scoped vs. project-scoped vs. cross-session)
- File upload mechanics (automatic loading, manual invocation, token implications)
- Memory system behavior (automatic updates, user control, LLM awareness)
- Search tool availability and invocation patterns

### **B. Platform Behavior Analysis**

**Investigation Approach**:
- Examine how ChatGPT handles uploaded files in custom GPTs
- Test session-specific vs. project knowledge differentiation
- Understand memory persistence and retrieval patterns
- Validate read-only constraints per `T810A1-CON-008`

### **C. Constraint Validation**

**Platform Constraints to Confirm** (per `T810A1-CON-008`):
- File system access (read-only validation)
- Memory update patterns (automatic vs. controllable)
- Knowledge type interaction (memory + files + training + search)
- Token/context window implications

## V. CRITICAL DEPENDENCIES & CONTEXT

### **Current State Challenges**

This research directly addresses **Phase 3.2 Story S04 blocking dependency**:

1. **Knowledge Architecture Ambiguity**: Block 4 needs to declare what knowledge LLM_Gastro can access, but we lack clear taxonomy of knowledge types specific to ChatGPT platform.

2. **Access Pattern Uncertainty**: S04 must specify how knowledge is accessed, but we haven't mapped platform-specific access mechanisms (automatic loading, manual upload, tool invocation).

3. **Content Placement Confusion**: Clinical sources, patient profile, JSON skeletons need to be assigned to specific knowledge types, but the mapping is unclear.

4. **Memory vs. Stable JSON Architecture**: `T810A1-INT-005` (Memory Review Protocol) requires understanding ChatGPT memory system behavior, but integration with Stable JSON (patient profile) is undefined.

5. **Block 4 Structure Vacuum**: No pattern exists for how to surface epistemological architecture in system prompt; need concrete implementation guidance.

### **Integration with T810A1-PROMPT**

Research findings will directly inform:

- **S04 (Knowledge Base)**:
  - FR-001: Knowledge Type Enumeration (per research taxonomy)
  - FR-002: Clinical Knowledge Sources (placement in knowledge types)
  - FR-003: Data Structure Templates (Stable/Dynamic JSON placement)
  - FR-004: Knowledge Access Declaration (access patterns per research findings)
  - FR-005: Global Standards (placement strategy)

- **INT-005 (Memory Review Protocol)**:
  - Clarify ChatGPT memory behavior for Step 0 implementation
  - Define memory vs. Stable JSON conflict resolution workflow
  - Specify practical memory review → profile loading sequence

- **Block 4 Implementation**:
  - Concrete structure for LLM_Developer to implement
  - Knowledge type declarations
  - Access pattern surfacing
  - Content inventory

### **Alignment with Governance**

Research must respect existing requirements:
- **T810A-GDR-003 (Stable/Dynamic JSON Architecture)**: Research clarifies which knowledge type(s) host Stable JSON
- **T810A-GDR-004 (Session Workflow Architecture)**: Research informs memory review step implementation
- **T810A-GDR-005 (GI Knowledge Base Sources)**: Research identifies which knowledge type(s) host clinical sources
- **T810A1-CON-008 (ChatGPT Architectural Constraints)**: Research validates platform constraints

## VI. SUCCESS CRITERIA

The research will be considered successful if it delivers:

1. **Complete Knowledge Type Taxonomy**: Enumeration of all knowledge types LLM_Gastro can access on ChatGPT platform (System, Project, Internal, External, OTHERS if applicable)

2. **Access Pattern Matrix**: Clear mapping of how each knowledge type is accessed, triggered, and constrained

3. **Content-to-Knowledge Assignments**: Definitive mapping of LLM_Gastro content (clinical sources, profile, skeletons, reports) to knowledge types

4. **Block 4 Implementation Template**: Concrete structure recommendation with example snippet for LLM_Developer

5. **Memory Architecture Clarification**: Practical guidance for INT-005 implementation given ChatGPT memory behavior

6. **S04 FR Recommendations**: Prioritized FR categories with scope guidance for MVP specification

7. **Platform Constraint Validation**: Confirmation of `T810A1-CON-008` constraints (read-only files, memory behavior, etc.)

8. **Actionable Implementation Path**: Clear next steps for LLM_Consultant to draft S04 FRs based on findings

## VII. TIMELINE & RESOURCES

### **Research Phases**

**Phase 1: Platform Documentation Review** (2-3 minutes)
- ChatGPT Custom GPT architecture
- Memory system documentation
- File upload and project knowledge capabilities
- Search tool availability

**Phase 2: Knowledge Type Taxonomy** (2-3 minutes)
- Enumerate distinct knowledge types
- Define scope and persistence for each
- Validate platform-native capabilities

**Phase 3: Access Pattern Mapping** (1-2 minutes)
- Map access mechanisms per knowledge type
- Identify trigger conditions
- Document platform constraints

**Phase 4: Content Assignment & Block 4 Structure** (1-2 minutes)
- Assign LLM_Gastro content to knowledge types
- Draft Block 4 implementation structure
- Create concrete example snippet

**Phase 5: Synthesis & Recommendations** (1-2 minutes)
- S04 FR category recommendations
- INT-005 implementation guidance
- Prioritization and scope guidance

**Total Duration:** 5-10 minutes (surface-level, actionable research)

### **Required Resources**
- OpenAI ChatGPT platform documentation
- GPT-5 (or current model) technical specifications
- ChatGPT Custom GPT best practices
- **Constraint**: NO deep epistemology research; surface-level platform investigation only

## VIII. STAKEHOLDER ENGAGEMENT

### **Primary Stakeholders**
- **Client (Decision Owner)**: Final approval of research scope and acceptance of recommendations
- **LLM_Consultant**: Primary consumer of research findings for S04 specification
- **LLM_Research**: External research agent conducting the focused investigation

### **Review & Approval Gates**
- **Research Scope Approval**: Client confirmation of research objectives and methodology (Gate 1 - Current)
- **Final Deliverable Review**: Client acceptance of research findings and S04 FR recommendations (Gate 2)

### **Integration with Phase 3.2**

Research findings will be integrated into Phase 3.2 workflow:
1. **Research Brief Commission** (current) → 2. **Research Execution** (LLM_Research) → 3. **Research Analysis** (LLM_Consultant reviews findings) → 4. **S04 Specification** (LLM_Consultant drafts FRs based on taxonomy)

## IX. KNOWN CONSTRAINTS & ASSUMPTIONS

### **Constraints**
- **Surface-level only**: NO deep epistemology or comprehensive knowledge management research
- **Platform-specific**: Focus exclusively on ChatGPT/GPT-5 capabilities, not general LLM knowledge architecture
- **Time-boxed**: 5-10 minutes maximum; actionable implementation guidance prioritized over theoretical depth
- **Documentation-based**: Rely on publicly available OpenAI documentation; no platform experimentation

### **Assumptions**
- ChatGPT Custom GPT documentation contains sufficient detail on knowledge types and access patterns
- GPT-5 (or current model) architecture is documented with knowledge handling capabilities
- Memory system behavior is documented or can be inferred from user-facing documentation
- File upload patterns (session vs. project knowledge) are clarified in platform documentation
- The knowledge taxonomy identified will be sufficient for MVP S04 specification

### **Out of Scope**
- Deep epistemology research (how LLMs "know" things philosophically)
- Comprehensive knowledge management frameworks
- Cross-platform comparison (Claude, Gemini, etc.)
- Future platform capabilities (stick to current ChatGPT state)
- Custom tooling or API integration (MVP uses native ChatGPT capabilities only per `T810A1-CON-005`)

## X. APPENDICES

### **A. Current Artifact References**
- **Primary Analysis Target**: `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md` (E-GDRs governance context)
- **Request Document**: `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md` (S04 placeholder, INT-004, INT-005, CON-008)
- **Implementation Target**: `prompt/roles/gastro/gastro_system.md` (Block 4 placeholder awaiting specification)
- **Consultancy Plan**: `prompt/artifacts/tasks/T810/consultant/workspace/plan/plan_T810A1-PROMPT_phase1-4.md` (Phase 3.2 workflow)

### **B. Initial Knowledge Type Hypotheses** (to be validated/refined by research)

**Client-Provided Hypotheses**:
1. **System Knowledge**: ChatGPT cross-session memory (platform interface-constructed)
2. **Project Knowledge**: Uploaded documents/files in dedicated database (RAG system)
3. **Internal Knowledge**: GPT-5 trained knowledge (OpenAI training corpus)
4. **External Knowledge**: Native search tools (web search capability)
5. **OTHERS**: To be discovered by research

**Research Validation Questions**:
- Are these 5 types exhaustive for ChatGPT platform?
- Is "Project Knowledge" accurately described (session-specific vs. cross-session)?
- Are there additional knowledge types not captured?
- How do these types interact (e.g., memory + project knowledge)?

### **C. Key Research Outputs for S04**

| Research Finding | S04 FR Impact | Implementation Detail |
|:-----------------|:--------------|:----------------------|
| Knowledge Type Taxonomy | FR-001: Knowledge Type Enumeration | List all types LLM_Gastro can access |
| Clinical Content Placement | FR-002: Clinical Knowledge Sources | Specify which knowledge type hosts ROME IV, Bristol Chart, etc. |
| Stable JSON Placement | FR-003: Data Structure Templates | Specify which knowledge type hosts patient profile |
| Access Pattern Matrix | FR-004: Knowledge Access Declaration | Specify how LLM_Gastro accesses each type |
| Block 4 Structure Recommendation | All S04 FRs | Implementation template for LLM_Developer |
| Memory System Behavior | INT-005 refinement | Memory Review Protocol implementation guidance |

### **D. Research Brief Lineage**

**Precedent Research**:
- **T810A-RES-001**: System Architecture & Clinical Validation (comprehensive 7-deliverable research)
- **T810A-RES-002**: Conversation-Driven Empirical Validation (gap analysis triggering Phase 1.5)

**This Research (T810A-RES-003)**:
- **Type**: Surface-level, platform-specific investigation
- **Scope**: Knowledge taxonomy only (narrower than RES-001)
- **Purpose**: Unblock S04 specification (tactical vs. strategic research)
- **Methodology**: Documentation analysis (not empirical testing like RES-002)

---

**Prepared by:** LLM_Consultant
**Approval Required:** Client (Decision Owner)
**Target Start Date:** Upon approval
**Expected Completion:** 5-10 minutes from initiation
**Criticality:** **HIGH** — Blocks T810A1-PROMPT Story S04 specification; enables Phase 3.2 completion
