---
artifact_type: 'RESEARCH_BRIEF'
initiative_id: 'T102'
epic_id: 'T102B'
research_id: 'T102B-RES-001'
version: '1.0.0'
iteration: '1'
date: '2026-01-12'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: Request Artifact Analysis — Industry Standard Comparison (External)

## I. EXECUTIVE SUMMARY

**Context**: The T102 "Request" artifact combines BRD (Business Requirements Document) and SRS (Software Requirements Specification) patterns into a unified feature-level specification. Client QA feedback identifies workflow bottlenecks at the Request stage, including FR/IG duplication, RID repetition from Epic levels, and excessive documentation overhead blocking MVP delivery. A comparative analysis against industry standards is required to inform T102B1 (Request Standard) development.

**Objective**: Conduct external research comparing the current T102 Request artifact structure to industry-standard SRS and BRD/PRD documents. Identify strengths, weaknesses, and propose improvements for optimal integration with the `sps → request → design` workflow.

**Target Deliverable**: A comprehensive analysis report consumed by `LLM_Consultant` and `LLM_Developer` to inform T102B1 feature development and establish the Request artifact standard.

## II. RESEARCH SCOPE & TOPICS

### Part A: Industry Standard Analysis

#### Topic 1: SRS Comparison (IEEE 830 / ISO 29148) ([P1])
**Objective**: Compare T102 Request structure to IEEE 830 and ISO/IEC/IEEE 29148 Software Requirements Specification standards.

**Context**: The T102 Request artifact contains SRS-like sections (Functional Requirements, NFRs, Interfaces, Stories with ACs) but may deviate from or omit standard SRS patterns.

**Specific Questions**:
*   What are the canonical sections of IEEE 830 / ISO 29148 SRS documents?
*   How does the T102 Request map to these sections? (gap analysis)
*   What mandatory SRS elements are missing from T102 Request?
*   What T102 Request elements exceed typical SRS scope?
*   How do industry SRS documents handle requirement traceability (vs. T102 RID system)?

**Deliverable**: SRS comparison matrix with T102 mapping, gaps, and overlaps.

#### Topic 2: BRD/PRD Comparison (BABOK / Product Management) ([P1])
**Objective**: Compare T102 Request structure to Business Requirements Document (BRD) and Product Requirements Document (PRD) patterns.

**Context**: The T102 Request "Part 1 — Business View (BRD)" sections (Source & Scope, Business Objectives, Stakeholders) follow BRD patterns. Comparison to BABOK v3 and modern PRD practices is needed.

**Specific Questions**:
*   What are the canonical sections of BABOK v3 BRD and modern PRD documents?
*   How does T102 Request Part 1 (BRD) map to these standards?
*   What is the industry-standard boundary between BRD/PRD and SRS content?
*   How do industry documents handle the "business context → technical requirements" transition?
*   What PRD elements (user stories, jobs-to-be-done, success metrics) could enhance T102 Request?

**Deliverable**: BRD/PRD comparison matrix with T102 mapping and enhancement opportunities.

#### Topic 3: Agile Requirements Patterns (SAFe / Scrum) ([P2])
**Objective**: Compare T102 Request to Agile requirements artifacts (Epics, Features, User Stories, Acceptance Criteria).

**Context**: T102 uses a waterfall-influenced `sps → request → design` flow. Agile patterns may offer streamlining opportunities for MVP delivery.

**Specific Questions**:
*   How do SAFe Feature specifications compare to T102 Request?
*   What is the typical content granularity at Feature vs. Story level in Agile?
*   How do Agile teams handle "just enough" documentation for MVP?
*   What Agile patterns reduce documentation overhead while maintaining traceability?

**Deliverable**: Agile pattern comparison with adoption recommendations.

### Part B: T102 Request Artifact Analysis

#### Topic 4: Current State Strengths ([P1])
**Objective**: Document what the T102 Request artifact does well compared to industry standards.

**Context**: The T102 Request has evolved through multiple iterations (T102A-SPSST, T810A1-PROMPT exemplar). Strengths should be preserved in T102B1 standard.

**Specific Questions**:
*   What T102 Request patterns are industry-aligned or industry-leading?
*   What makes `request_T810A1-PROMPT.md` effective as a golden exemplar?
*   Which sections provide clear value to downstream consumers (Planner, Developer)?
*   What traceability patterns (RID system, Inherited Considerations) are effective?

**Deliverable**: Strengths inventory with evidence from T810A1 exemplar.

#### Topic 5: Current State Weaknesses ([P1])
**Objective**: Document weaknesses and pain points in the current T102 Request artifact.

**Context**: Client QA feedback identifies FR/IG duplication, RID repetition, and excessive overhead. These need systematic analysis.

**Specific Questions**:
*   Where does content duplication occur between Request and SPS/Concept?
*   What sections create overhead without proportional value?
*   How does the story-level specification detail compare to industry practice?
*   What causes the "documentation trap" blocking MVP delivery?
*   Which mandatory sections could become optional for streamlined MVPs?

**Deliverable**: Weakness inventory with root cause analysis and severity ratings.

### Part C: Integration & Improvement

#### Topic 6: Workflow Integration Analysis ([P1])
**Objective**: Analyze optimal Request artifact role within the `sps → request → concept/design` workflow.

**Context**: Current workflow requires Request completion before any implementation. Client seeks MVP delivery at Request stage, with Design reserved for complex stories.

**Specific Questions**:
*   What is the ideal content boundary between SPS and Request?
*   What is the ideal content boundary between Request and Design?
*   How should Request integrate with Concept ADRs (additive vs. prescriptive)?
*   What "minimum viable Request" structure enables direct development?
*   How do industry workflows handle "thin documentation → implementation → refinement" cycles?

**Deliverable**: Workflow integration model with boundary recommendations.

#### Topic 7: Improvement Proposals ([P1])
**Objective**: Propose specific improvements to the T102 Request artifact standard.

**Context**: Research findings from Topics 1-6 should synthesize into actionable improvement proposals for T102B1 development.

**Specific Questions**:
*   What sections should be mandatory vs. optional in the T102B1 Request standard?
*   How should FR/IG relationship be restructured to reduce duplication?
*   Should Feature-level GDRs/ADRs be standard or exception-based?
*   How should RID inheritance from Epic be simplified?
*   What "Request Lite" variant could serve MVP workflows?

**Deliverable**: Prioritized improvement proposal list with implementation guidance.

#### Topic 8: T102 Request Structural Assessment ([P1])
**Objective**: Assess specific T102 Request sections against industry-standard necessity and placement.

**Context**: Client QA feedback raises specific structural questions about the current `request_T102A-SPSST.md` pattern. These questions require industry-standard comparison to inform T102B1 structure decisions.

**Specific Questions** (Client QA-driven):
*   **Feature Solution Framework (Section A)**: Is this section necessary in a hybrid SRS/BRD document? What is the industry-standard equivalent and placement?
*   **Governance & Roadmap (Missing)**: Should Feature-level requests include a development phases/roadmap section? Where do industry standards place feature lifecycle governance? When is Feature-level Governance & Roadmap necessary vs. optional? What triggers (complexity, duration, dependencies) mandate this section?
*   **FR vs IG Placement**: Based on industry patterns, where should Functional Requirements live relative to Implementation Guidance? Should they merge, remain separate, or adopt a different relationship?
*   **Stories & Specification (Section J)**: Is story-level specification necessary at the Request level, or should this be deferred to Design/Sprint planning? What is industry-standard granularity at Feature specification level?
*   **Missing Sections**: What additional sections/subsections are important to feature development from industry-standard perspectives that T102 Request currently lacks?

**Deliverable**: Structural assessment table mapping each question to industry-standard findings with recommendation (Keep/Modify/Remove/Add).

### Part D: Workflow Typology

#### Topic 9: Development Workflow Typology ([P1])
**Objective**: Compare industry-standard workflows for different development types beyond discovery.

**Context**: Current T102 workflow (`sps → request → design`) suits new feature discovery but may be overly heavy for debugging, enhancement, or refactoring work. Industry-standard alternatives need assessment to determine if T102 should support multiple workflow types or lightweight documentation alternatives.

**Specific Questions**:
*   What industry-standard workflows exist for:
    - **Bug/defect resolution** (hotfix, patch cycles, incident response)
    - **Feature enhancement/improvement** (minor changes to existing features)
    - **Technical debt/refactoring** (code quality improvements)
*   Do these workflows require separate documentation types, or can git PRs with structured templates suffice?
*   What is the industry-standard boundary between "needs SPS/Request" vs. "git PR is sufficient"?
*   How do SAFe/Scrum/Kanban handle lightweight change requests vs. full feature development?
*   What criteria determine workflow selection (impact, scope, risk, complexity)?
*   Are there hybrid approaches that allow "Request Lite" or "Fast Track" paths for lower-risk changes?

**Deliverable**: Workflow typology matrix with documentation requirements per development type and integration recommendations for T102 consultancy layer.

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
*   **Boundary**: External research (industry standards) + internal artifact analysis.
*   **Scope**: Focus on requirements documentation; exclude implementation/testing standards.
*   **Timebox**: Standard research session.

### B. Assumptions
*   IEEE 830, ISO 29148, BABOK v3, and SAFe documentation are accessible via web search.
*   `request_T810A1-PROMPT.md` is an accepted golden exemplar for Request quality.
*   The researcher has access to compare T102A-SPSST and T810A1 artifacts.

### C. Primary Tools
**WebSearch is the PRIMARY tool for this research brief.** The researcher SHALL use external web search to:
*   Retrieve current IEEE 830 / ISO 29148 SRS structure documentation
*   Retrieve BABOK v3 BRD patterns and templates
*   Retrieve SAFe Feature specification patterns
*   Retrieve modern PRD templates (ProductPlan, Linear, Notion, Coda)
*   Compare industry best practices for requirements documentation

Internal artifact analysis (Read tool) is SECONDARY and used only to:
*   Examine `request_T102A-SPSST.md` and `request_T810A1-PROMPT.md` for comparison
*   Verify T102 governance constraints in SPS/Concept documents

### D. Methodology "Hierarchy of Truth"
1.  **Industry Standards** (IEEE, ISO, BABOK) — Authoritative external reference
2.  **Industry Practice** (SAFe, Agile, Modern PRD) — Practical patterns
3.  **T102 Governance** (`T102-STD-001`, `T102-STD-005`) — Internal constraints
4.  **Exemplar Artifacts** (`T810A1-PROMPT.md`) — Empirical success patterns

---

## IV. CROSS-TOPIC INTEGRATION

*   **SRS ↔ BRD**: What is the optimal integration point between business and technical requirements in T102 Request?
*   **Industry Standards ↔ Strengths**: Do T102 strengths align with or exceed industry standards?
*   **Weaknesses ↔ Agile**: Can Agile patterns address T102 weakness areas?
*   **Integration ↔ Proposals**: Do proposals respect current workflow constraints while enabling improvement?
*   **Structural Assessment ↔ Proposals**: Do structural recommendations from Topic 8 align with improvement proposals from Topic 7?

---

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance
*   SSOT: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
*   Concept: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
*   T102-STD-001: Consultancy Operating Model (workflow definition)

### B. Primary Artifacts for Analysis
*   `prompt/artifacts/tasks/T102/T102A/ssot/request_T102A-SPSST.md` (current T102A1 Request)
*   `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md` (golden exemplar)
*   `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md` (alternative pattern reference)

### C. Industry Standard References (Web Search)
*   IEEE 830-1998 (SRS standard, superseded)
*   ISO/IEC/IEEE 29148:2018 (Requirements engineering)
*   BABOK v3 (Business analysis body of knowledge)
*   SAFe Feature specification patterns
*   Modern PRD templates (ProductPlan, Coda, Notion patterns)

### D. Anti-Patterns / Exclusions
*   **IGNORE**: `*/archive/` directories
*   **IGNORE**: Design artifacts (out of scope)

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions for this Brief**:
1.  **Section I (Exec Summary)**: Must include clear verdict on T102 Request alignment with industry standards.
2.  **Section III (Topic Findings)**:
    *   **Topics 1-3**: Comparison matrices in Evidence sections.
    *   **Topics 4-5**: Strength/weakness inventories with severity ratings.
    *   **Topics 6-7**: Actionable proposals with priority rankings.
    *   **Topic 8**: Structural assessment table with Keep/Modify/Remove/Add recommendations.
    *   **Topic 9**: Workflow typology matrix with documentation requirements per development type.
3.  **Section VI (Source Material)**: Explicitly list industry standard citations and artifact paths.
4.  **Completeness**: Do NOT delete empty sections. If a topic has no implications, explicitly state "None".

---

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

---

## VIII. CRITICAL DEPENDENCIES (E-RID MAPPING)

| Topic | Primary Outputs | Informs / Unblocks |
|:---|:---|:---|
| Topic 1 | SRS comparison matrix | T102B1-FR specifications |
| Topic 2 | BRD/PRD comparison matrix | T102B1 business view sections |
| Topic 3 | Agile pattern analysis | Workflow streamlining options |
| Topic 4 | Strengths inventory | Patterns to preserve in T102B1 |
| Topic 5 | Weaknesses inventory | Pain points to address in T102B1 |
| Topic 6 | Integration model | SPS ↔ Request ↔ Design boundaries |
| Topic 7 | Improvement proposals | T102B1 standard specification |
| Topic 8 | Structural assessment | Section-level Keep/Modify/Remove decisions |
| Topic 9 | Workflow typology matrix | Multi-workflow support in T102 consultancy layer |

---

## IX. SUCCESS CRITERIA

*   Comparison matrices cover IEEE 830, ISO 29148, BABOK v3, and SAFe patterns.
*   At least 5 specific strengths and 5 specific weaknesses are documented with evidence.
*   Improvement proposals are prioritized (P1/P2/P3) with implementation effort estimates.
*   Output directly informs T102B1 feature specification development.
*   Workflow integration model provides clear SPS ↔ Request ↔ Design boundary guidance.
*   Structural assessment table provides clear Keep/Modify/Remove/Add recommendation for each Client QA question.
*   Workflow typology matrix covers at least 4 development types (discovery, bug fix, enhancement, refactoring) with clear documentation requirements per type.
*   All topics include web search citations for industry-standard claims.
