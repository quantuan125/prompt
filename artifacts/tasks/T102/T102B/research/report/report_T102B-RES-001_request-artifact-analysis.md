---
artifact_type: 'RESEARCH_REPORT'
initiative_id: 'T102'
epic_id: 'T102B'
research_id: 'T102B-RES-001'
version: '1.0.0'
iteration: '1'
date: '2026-01-13'
status: 'draft'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: Request Artifact Analysis - Industry Standard Comparison

## I. EXECUTIVE SUMMARY

**Context**: The T102 "Request" artifact combines BRD (Business Requirements Document) and SRS (Software Requirements Specification) patterns into a unified feature-level specification. Client QA feedback identifies workflow bottlenecks at the Request stage, including FR/IG duplication, RID repetition from Epic levels, and excessive documentation overhead blocking MVP delivery. This research was commissioned to compare the T102 Request artifact against industry standards and inform T102B1 (Request Standard) development.

**Verdict**: **CONDITIONAL GO** - The T102 Request artifact demonstrates strong industry alignment with ISO 29148 and BABOK v3 patterns, exceeding typical BRD/SRS hybrid documents in traceability and governance. However, the current structure creates documentation overhead that conflicts with Agile "just enough" documentation principles. Recommend proceeding with T102B1 development incorporating streamlining proposals from Topic 7.

**Key Findings**:
*   **Finding 1**: T102 Request's hybrid BRD/SRS structure aligns well with ISO/IEC/IEEE 29148:2018 patterns but includes significant content that exceeds typical feature-level specification granularity (story-level FR/ACs at Request stage).
*   **Finding 2**: The RID traceability system (T102-ADR-005) is industry-leading for manual documentation but creates repetition overhead when inheriting from Epic scope.
*   **Finding 3**: SAFe Feature specifications are significantly lighter than T102 Request (name + benefit hypothesis + acceptance criteria vs. 11 major sections), suggesting a "Request Lite" variant would better serve MVP workflows.
*   **Finding 4**: Industry standards support workflow typology differentiation - bug fixes, enhancements, and refactoring typically use lightweight PR templates rather than full SRS/BRD documentation.
*   **Finding 5**: The golden exemplar (T810A1-PROMPT) demonstrates effective patterns including clear stakeholder mapping, robust NFR specifications, and comprehensive governance decisions (GDRs).

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Research stayed within defined boundaries - external industry standards research (WebSearch primary) plus internal artifact analysis (Read secondary). Excluded implementation/testing standards and design artifacts per brief constraints.

**Source of Truth Audit**:
*   **Industry Standards (WebSearch)**:
    *   IEEE 830-1998 SRS structure and templates
    *   ISO/IEC/IEEE 29148:2018 requirements engineering processes
    *   BABOK v3 BRD patterns and elicitation techniques
    *   SAFe Feature specification patterns (benefit hypothesis, acceptance criteria)
    *   Modern PRD templates (Notion, Aha!, ProductPlan patterns)
    *   Gitflow hotfix/bugfix workflow documentation
    *   Technical debt/refactoring documentation practices
    *   RTM (Requirements Traceability Matrix) industry standards
*   **Internal Artifacts (Read)**:
    *   `prompt/artifacts/tasks/T102/consultant/request/request_T102A-SPSST.md` (current T102 Request)
    *   `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md` (golden exemplar)

**Limitations**:
*   Full IEEE 830/ISO 29148 standard documents not directly accessible (summaries and templates used)
*   BABOK v3 chapter-level detail not directly accessible (practitioner resources used)
*   No direct access to Linear or Coda PRD templates (Notion templates analyzed)

---

## III. TOPIC FINDINGS

### Topic 1: SRS Comparison (IEEE 830 / ISO 29148)

**Objective**: Compare T102 Request structure to IEEE 830 and ISO/IEC/IEEE 29148 Software Requirements Specification standards.

#### A. Evidence & Forensics

**Source**: [IEEE 830-1998 Standard](https://ieeexplore.ieee.org/document/720574), [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html), [ReqView ISO 29148 Templates](https://www.reqview.com/doc/iso-iec-ieee-29148-templates/)

**Observation**: IEEE 830-1998 defines three core SRS sections:
1. **Introduction** (Purpose, Scope, References, Overview)
2. **General Description** (Product Perspective, Product Functions, User Characteristics, Constraints)
3. **Specific Requirements** (Functional requirements, NFRs, Interface requirements)

ISO/IEC/IEEE 29148:2018 supersedes IEEE 830 and defines three requirements engineering processes:
1. **Business/Mission Analysis** - defines problem/opportunity and solution space
2. **Stakeholder Needs and Requirements Definition** - user-oriented capabilities
3. **System/Software Requirements Definition** - technical view of solution

ISO 29148 provides templates for: Stakeholder Requirements Specification (StRS), System Requirements Specification (SyRS), Software Requirements Specification (SRS), and System Operational Concept (OpsCon).

#### B. Analysis

**T102 Request to IEEE 830/ISO 29148 Mapping Matrix**:

| IEEE 830 / ISO 29148 Section | T102 Request Section | Gap Analysis |
|:---|:---|:---|
| Introduction / Purpose | Section A (Feature Solution Framework) | ALIGNED - Problem Recap, Stakeholders & Concerns |
| Introduction / Scope | Section B (Source & Scope) | ALIGNED - In Scope / Out of Scope lists |
| General Description / Product Perspective | Section A.1 (Problem Recap & Constraints) | ALIGNED |
| General Description / User Characteristics | Section D (Stakeholders) | ALIGNED - Role/Persona/Responsibility table |
| General Description / Constraints | Sections F.1-F.2 (Assumptions, Constraints) | ALIGNED |
| Specific Requirements / Functional | Section F / J (Feature Requirements, Stories) | EXCEEDS - Story-level FRs at Request stage |
| Specific Requirements / NFRs | Section F.3 (Non-Functional Requirements) | ALIGNED |
| Specific Requirements / Interfaces | Section F.5 (Interfaces & Data) | ALIGNED |
| External Interface Requirements | Section F.7 (Integration Notes) | ALIGNED |
| Traceability | RID System (E-RID, F-RID, S-RID) | EXCEEDS - Formal ID system with inheritance |
| - | Section A.2 (Decision Criteria & Weights) | EXCEEDS IEEE 830 - Evaluation framework |
| - | Section E (Inherited Considerations) | EXCEEDS IEEE 830 - Epic inheritance mapping |
| - | Section G (Feature Governance Decisions) | EXCEEDS IEEE 830 - GDR/ADR pattern |
| - | Section H (Open Issues & Risks) | EXCEEDS IEEE 830 - Risk register |
| - | Section I (Research & Notes) | EXCEEDS IEEE 830 - Research linkage |
| Verification & Validation | Section K (Acceptance Criteria Register) | PARTIAL - AC summary but not full V&V plan |

**Gap Analysis Summary**:
*   **Missing from T102**: IEEE 830 does not mandate story-level specification at SRS level; T102 includes extensive story FRs (Section J)
*   **T102 Exceeds SRS**: Decision criteria, governance decisions, research linkage, risk registers are not standard SRS elements
*   **ISO 29148 Alignment**: T102 Request effectively combines StRS (Stakeholder Requirements) + SRS (Software Requirements) into single artifact

#### C. Governance Implication

**Decision Impact**: T102 Request is overspecified relative to IEEE 830/ISO 29148 SRS standards. The story-level functional requirements (Section J) exceed typical SRS granularity and create documentation overhead. Consider deferring story-level FRs to Design/Sprint planning per SAFe patterns.

**Risk**: T102B-RISK-001 - Story-level specification at Request stage may create "documentation trap" blocking MVP delivery (per client QA feedback).

---

### Topic 2: BRD/PRD Comparison (BABOK / Product Management)

**Objective**: Compare T102 Request structure to Business Requirements Document (BRD) and Product Requirements Document (PRD) patterns.

#### A. Evidence & Forensics

**Source**: [BABOK v3 BRD Patterns](https://businessanalystmentor.com/business-requirements-document/), [Asana BRD Template](https://asana.com/resources/business-requirements-document-template), [Wrike BRD Guide](https://www.wrike.com/blog/how-write-business-requirements-document/), [Notion PRD Templates](https://www.notion.com/templates/category/product-requirements-doc)

**Observation**: BABOK v3 defines a business requirement as "a representation of goals, objectives and outcomes that describe why a change has been initiated and how success will be assessed."

Standard BRD sections include:
1. Executive Summary
2. Project Context/Background
3. Problem Statement
4. Project Scope (In Scope / Out of Scope)
5. Current State
6. Future State
7. Business Requirements
8. Stakeholders
9. Assumptions, Limitations, and Constraints
10. Cost-Benefit Analysis

Modern PRD templates (Notion, Aha!) emphasize:
- Project Overview with change log
- Goals and Success Metrics
- User Personas and Scenarios
- Features and Requirements (functional + non-functional)
- Lightweight, living documents (1-10 pages)

#### B. Analysis

**T102 Request to BRD/PRD Mapping Matrix**:

| BRD/PRD Section | T102 Request Section | Gap Analysis |
|:---|:---|:---|
| Executive Summary | Section I (Executive Summary) | ALIGNED |
| Project Context | Section A.1 (Problem Recap) | ALIGNED |
| Problem Statement | Section A.1 (Problem & Desired Outcome) | ALIGNED |
| Project Scope | Section B (Source & Scope) | ALIGNED |
| Current State | Not explicitly present | GAP - No dedicated current state section |
| Future State | Section C (Business Objectives & Success Signals) | PARTIAL - Objectives but not future state diagram |
| Business Requirements | Section C + F (Objectives + Feature Requirements) | ALIGNED |
| Stakeholders | Section D (Stakeholders) | ALIGNED |
| Assumptions & Constraints | Section F.1-F.2 | ALIGNED |
| Cost-Benefit Analysis | Not present | GAP - No CBA section (may be appropriate for feature-level) |
| User Personas | Section D (Stakeholders table) | PARTIAL - Role-based, not persona-based |
| Success Metrics | Section C (Success Signals) | ALIGNED - Qualitative MVP signals |

**Synthesis**:
*   T102 Request "Part 1 - Business View (BRD)" sections align well with BABOK v3 patterns
*   T102 lacks Current State/Future State diagrams common in BRD templates
*   T102 exceeds typical PRD granularity with story-level specifications (Section J)
*   Modern PRD templates emphasize "living documents" - T102's formal version/iteration model may create update friction

**Industry Boundary between BRD/PRD and SRS**:
Per research: "BRD sets the vision. FRD defines behavior. SRS specifies implementation." T102 Request combines all three levels, which is atypical. Industry practice typically separates these into distinct artifacts with different audiences and detail levels.

#### C. Governance Implication

**Decision Impact**: T102 Request appropriately combines business context (BRD) with technical requirements (SRS) at feature level, but should consider:
1. Adding Current State/Future State sections for complex features
2. Reducing story-level detail at Request stage
3. Adopting "living document" patterns from modern PRD practices

**Risk**: None identified - BRD/PRD alignment is strong.

---

### Topic 3: Agile Requirements Patterns (SAFe / Scrum)

**Objective**: Compare T102 Request to Agile requirements artifacts (Epics, Features, User Stories, Acceptance Criteria).

#### A. Evidence & Forensics

**Source**: [SAFe Feature Specification](https://framework.scaledagile.com/blog/crafting-clarity-using-feature-templates-to-shape-and-communicate-intent), [SAFe Features and Capabilities](https://framework.scaledagile.com/features-and-capabilities), [Atlassian User Stories](https://www.atlassian.com/agile/product-management/requirements), [SAFe Story](https://framework.scaledagile.com/story)

**Observation**: SAFe Feature template minimum requirements:
- **Name**: Short descriptive title
- **Benefit Hypothesis**: "We believe [business outcome] will be achieved if [users] successfully achieve [user outcome] with [feature]"
- **Acceptance Criteria**: Non-negotiable conditions for acceptance (BDD format: Given/When/Then)

SAFe emphasizes: "A Feature is sized or split, as necessary, to be delivered by an Agile Release Train (ART) in a Planning Interval (PI)."

User Stories follow format: "As a [user role], I want [activity] so that [business value]."

Key Agile documentation principle: "Just-in-time discussions create a shared understanding of the scope that a formal document cannot provide."

#### B. Analysis

**T102 Request vs. SAFe Feature Comparison**:

| SAFe Feature Element | T102 Request Coverage | Assessment |
|:---|:---|:---|
| Feature Name | Section heading | ALIGNED |
| Benefit Hypothesis | Section C (Business Objectives) | PARTIAL - Objectives but not hypothesis format |
| Acceptance Criteria | Section K (AC Register) | ALIGNED but EXCEEDS - AC at story level in Section J |
| Enabler Features | Not explicit | GAP - No enabler/technical feature differentiation |
| WSJF Prioritization | Section A.2 (Decision Criteria & Weights) | EXCEEDS - More elaborate than WSJF |

**Granularity Comparison**:

| Artifact Level | SAFe Content | T102 Content |
|:---|:---|:---|
| Feature | Name + Benefit Hypothesis + AC | 11 major sections (~700+ lines in exemplar) |
| Story | User story format + AC | Full FRs + ACs in Section J (~200+ lines) |

**Agile "Just Enough" Documentation Assessment**:
T102 Request significantly exceeds SAFe's recommended feature-level documentation. SAFe explicitly warns against "cramming in so much detail that the Feature effectively turns into a traditional waterfall artifact."

#### C. Governance Implication

**Decision Impact**: T102 Request follows waterfall-influenced documentation patterns that conflict with Agile "just enough" documentation principles. Consider:
1. Adopting SAFe Benefit Hypothesis format in Section C
2. Deferring story-level FRs to Sprint planning
3. Creating "Request Lite" variant for MVP workflows

**Risk**: T102B-RISK-002 - Current documentation weight may create adoption friction with teams accustomed to Agile lightweight patterns.

---

### Topic 4: Current State Strengths

**Objective**: Document what the T102 Request artifact does well compared to industry standards.

#### A. Evidence & Forensics

**Source**: `request_T810A1-PROMPT.md` (golden exemplar), `request_T102A-SPSST.md` (current pattern)

**Observation from T810A1 Exemplar Analysis**:
1. **Clear Problem/Outcome Framing** (Section A.1): Concise problem statement with stakeholder-concern mapping
2. **Robust NFR Specifications** (Section F.3): 5 detailed NFRs with operational rules and acceptance checks
3. **Implementation Guidance** (Section F.6): 8 detailed IG items with operational rules and acceptance checks
4. **Governance Decisions** (Section G): GDR pattern with context/decision/consequences/references structure
5. **Traceability** (RID System): Comprehensive cross-referencing between SPS, Request, and Concept levels
6. **Research Integration** (Section I): Formal linkage to research briefs and reports
7. **Issues & Risks** (Section H): Structured register with ID/Title/Description/Owner/Status/Priority

#### B. Analysis

**Strengths Inventory**:

| Strength | Evidence | Industry Alignment |
|:---|:---|:---|
| S1: Stakeholder-Concern Mapping | T810A1 Section A.1: "Concern -> Criterion mapping" | EXCEEDS ISO 42010 stakeholder viewpoint pattern |
| S2: Weighted Decision Criteria | T810A1 Section A.2: Sum=1.00 weighted scoring | EXCEEDS typical BRD - quantified evaluation |
| S3: RID Traceability System | E-RID inheritance in Section E (22 inherited items in T810A1) | EXCEEDS RTM standards - hierarchical inheritance |
| S4: GDR Pattern | T810A1-GDR-001, GDR-002 with ADR-style structure | INDUSTRY-ALIGNED with ADR best practices |
| S5: NFR Operational Rules | T810A1-NFR-001 through NFR-005 with detailed operational rules | EXCEEDS IEEE 830 NFR format |
| S6: Implementation Guidance | T810A1-IG-001 through IG-008 with acceptance checks | EXCEEDS typical SRS - bridges to implementation |
| S7: Research Linkage | T810A1-RES-001 with brief/report structure | UNIQUE - formal research artifact integration |
| S8: Issues & Risks Register | Section H with standardized columns per T102-ADR-007 | INDUSTRY-ALIGNED with PRINCE2/PMBOK risk management |

**What Makes T810A1 Effective as Golden Exemplar**:
1. **Balance of Abstraction**: High-level business view (Part 1) transitions smoothly to technical requirements (Part 2)
2. **Operational Specificity**: NFRs and IGs include "Operational Rules" and "Acceptance Checks" that bridge requirements to implementation
3. **Cross-Reference Density**: 28 inherited E-RIDs + 8 IGs + 7 INTs demonstrate comprehensive traceability
4. **GDR Decision Recording**: Formal governance decisions with rationale prevent scope creep and document key choices

#### C. Governance Implication

**Decision Impact**: Preserve the following patterns in T102B1:
- Stakeholder-Concern-Criterion mapping (Section A.1)
- Weighted decision criteria (Section A.2)
- NFR operational rules pattern (Section F.3)
- GDR pattern with ADR structure (Section G)
- Research linkage (Section I)
- Issues & Risks register structure (Section H)

**Risk**: None - these patterns should be retained.

---

### Topic 5: Current State Weaknesses

**Objective**: Document weaknesses and pain points in the current T102 Request artifact.

#### A. Evidence & Forensics

**Source**: Client QA feedback (per brief), artifact analysis of `request_T102A-SPSST.md` and `request_T810A1-PROMPT.md`

**Observation**:
1. **T810A1 Line Count**: ~745 lines for a single feature request
2. **Section J (Stories)**: T810A1 includes 10 stories (S01-S10) with detailed FRs at Request level
3. **Section E (Inherited Considerations)**: 22 inherited E-RIDs create potential repetition
4. **Section F.6 (Implementation Guidance)**: 8 detailed IGs overlap with FR specifications
5. **Section F.7 (Integration Notes)**: 7 INTs create cross-reference overhead

#### B. Analysis

**Weakness Inventory**:

| ID | Weakness | Root Cause | Severity | Evidence |
|:---|:---|:---|:---|:---|
| W1 | FR/IG Duplication | FRs in Section J duplicate guidance in Section F.6 IGs | HIGH | T810A1-NFR-001 overlaps with T810A1-S05 FRs |
| W2 | Story-Level Specification at Request | Stories with full FRs/ACs belong at Design/Sprint level per SAFe | HIGH | T810A1 Section J: 10 stories, ~300 lines |
| W3 | RID Repetition from Epic | Section E inherits E-RIDs that may not all apply to feature | MEDIUM | T810A1 Section E: 22 inherited items |
| W4 | Excessive Mandatory Sections | All sections appear mandatory regardless of feature complexity | MEDIUM | T102A1 includes 8 stories for template definition |
| W5 | Documentation Overhead | 700+ lines for feature-level spec exceeds SAFe recommendation | HIGH | SAFe Feature = name + benefit hypothesis + AC |
| W6 | Version/Iteration Formality | YAML header versioning creates update friction vs. living docs | LOW | Modern PRDs use change logs, not formal versions |
| W7 | Missing Current/Future State | No dedicated sections for state transition visualization | LOW | BRD best practice includes state diagrams |

**Root Cause Analysis - "Documentation Trap"**:
The documentation trap occurs when the Request artifact requires comprehensive completion before implementation can begin. Contributing factors:
1. **Story-level FRs at Request stage** - Creates false completeness requirement
2. **All sections mandatory** - No mechanism to skip sections for simple features
3. **Formal approval gates** - Request must be "approved" before Concept begins
4. **RID overhead** - Creating unique IDs for every item adds cognitive load

**Severity Assessment**:
- **HIGH**: W1, W2, W5 - Directly block MVP delivery
- **MEDIUM**: W3, W4 - Create friction but are manageable
- **LOW**: W6, W7 - Minor improvements, not blockers

#### C. Governance Implication

**Decision Impact**: Address in T102B1:
- Make Section J (Stories) optional or deferred to Design
- Create FR/IG merge strategy to eliminate duplication
- Establish mandatory vs. optional section classification
- Define "Request Lite" pattern for simple features

**Risk**: T102B-RISK-003 - Failure to address W1, W2, W5 will perpetuate documentation trap and block MVP delivery.

---

### Topic 6: Workflow Integration Analysis

**Objective**: Analyze optimal Request artifact role within the `sps -> request -> concept/design` workflow.

#### A. Evidence & Forensics

**Source**: T102 brief, [BRD vs SRS Analysis](https://thebusinessanalystjobdescription.com/brd-vs-srs-vs-frs-detailed-comparison/), [SAFe Workflow Patterns](https://framework.scaledagile.com/)

**Observation**:
Industry standard document flow:
- **BRD** (Business Level) -> **FRD/PRD** (Functional Level) -> **SRS** (Technical Level) -> **Design**

T102 workflow:
- **SPS** (Problem/Epic Level) -> **Request** (Feature Level) -> **Concept/Design** (Story Level)

#### B. Analysis

**Ideal Content Boundaries**:

| Workflow Stage | Ideal Content | Current T102 Content | Gap |
|:---|:---|:---|:---|
| **SPS** | Problem, Epics, Initiative Considerations, Dependencies | Aligned | None |
| **Request** | Feature scope, Business objectives, High-level FRs, NFRs, Stakeholders | Aligned + Story FRs, Story ACs | OVER-SPECIFIED |
| **Concept/Design** | Story specifications, Detailed FRs, Acceptance Criteria, Architecture | Partially duplicated in Request | UNDER-UTILIZED |

**SPS -> Request Boundary**:
- SPS provides: Initiative context, Epic-level scope, inherited considerations (E-RIDs)
- Request should receive: Feature ID, Purpose statement, Epic constraints
- Request should NOT duplicate: Full Epic dependency lists, governance already decided at Epic level

**Request -> Design/Concept Boundary**:
- Request should provide: Feature scope, business objectives, NFRs, key interfaces
- Design/Concept should receive: Story decomposition work
- Request should NOT include: Story-level FRs, detailed acceptance criteria (defer to Design)

**"Minimum Viable Request" Structure**:
Based on SAFe Feature patterns and BRD best practices, minimum viable Request should contain:
1. **Feature Identity** (YAML header + Section A brief)
2. **Problem & Scope** (Sections A.1, B - consolidated)
3. **Business Objectives** (Section C - brief)
4. **Stakeholders** (Section D - table only)
5. **Feature-Level Requirements** (Sections F.2-F.5 - constraints, NFRs, dependencies, interfaces)
6. **Acceptance Criteria** (Section K - feature-level only)
7. **Issues & Risks** (Section H - if any)

**Sections to Defer or Make Optional**:
- Section A.2 (Decision Criteria) - optional for simple features
- Section E (Inherited Considerations) - reference-only, not full duplication
- Section F.6 (Implementation Guidance) - defer to Design
- Section G (Governance Decisions) - optional for simple features
- Section I (Research & Notes) - optional
- Section J (Stories & Specification) - defer to Design/Sprint planning

#### C. Governance Implication

**Decision Impact**: Establish boundary model in T102B1:
- Request = Feature-level specification (BRD + high-level SRS)
- Concept/Design = Story-level specification (detailed SRS + architecture)
- Provide explicit deferral guidance for each optional section

**Risk**: None - boundary clarification reduces ambiguity.

---

### Topic 7: Improvement Proposals

**Objective**: Propose specific improvements to the T102 Request artifact standard.

#### A. Evidence & Forensics

**Source**: Topics 1-6 synthesis, SAFe patterns, modern PRD practices

#### B. Analysis

**Prioritized Improvement Proposals**:

| ID | Proposal | Priority | Effort | Source |
|:---|:---|:---|:---|:---|
| P1 | **Create "Request Lite" Variant** | P1 | MEDIUM | Topic 3, Topic 6 |
| P2 | **Defer Story FRs to Design** | P1 | LOW | Topic 1, Topic 5 (W2) |
| P3 | **Merge FR/IG Sections** | P1 | MEDIUM | Topic 5 (W1) |
| P4 | **Establish Mandatory vs. Optional Sections** | P1 | LOW | Topic 5 (W4) |
| P5 | **Simplify RID Inheritance** | P2 | MEDIUM | Topic 5 (W3) |
| P6 | **Adopt SAFe Benefit Hypothesis Format** | P2 | LOW | Topic 3 |
| P7 | **Add Current/Future State Sections** | P3 | LOW | Topic 2 |
| P8 | **Adopt Living Document Pattern** | P3 | LOW | Topic 2 |

**Detailed Proposal Specifications**:

**P1: Create "Request Lite" Variant**
- **Trigger**: Simple features, bug fixes, minor enhancements
- **Content**: Sections A.1 (brief), B, C, D, F.2-F.5 (consolidated), K (feature-level AC)
- **Omit**: Sections A.2, E (full), F.6, G, I, J
- **Target**: <200 lines

**P2: Defer Story FRs to Design**
- **Current**: Section J includes full story FRs and ACs
- **Proposed**: Section J becomes "Story Index" - story IDs, titles, one-line purpose only
- **Defer to Design**: Full story FRs, detailed ACs, implementation details

**P3: Merge FR/IG Sections**
- **Current**: Section F.6 (Implementation Guidance) duplicates Section J (Story FRs)
- **Proposed**: Single "Feature Requirements & Guidance" section with:
  - Feature-level FRs (F-RID format)
  - Inline implementation guidance per FR where needed
  - Clear delineation: "What" (FR) vs. "How" (IG)

**P4: Establish Mandatory vs. Optional Sections**
- **Mandatory**: A.1, B, C, D, F.2-F.5, K, VIII (Next Steps)
- **Conditional**: A.2 (complex features), E (inherited only if applicable), G (if GDRs exist), H (if issues/risks exist)
- **Optional/Deferred**: F.6 (to Design), I (if research exists), J (to Design)

**P5: Simplify RID Inheritance**
- **Current**: Full duplication of inherited E-RIDs in Section E
- **Proposed**: Reference-only pattern: "This feature inherits [E-RID-001, E-RID-002, ...] from Epic T810A. See SPS Section III-C for details."

**P6: Adopt SAFe Benefit Hypothesis Format**
- **Current**: Section C lists objectives and success signals
- **Proposed**: Add benefit hypothesis: "We believe [business outcome] will be achieved if [users] achieve [user outcome] with [feature]"

**P7: Add Current/Future State Sections**
- **Trigger**: Features involving system changes or process redesign
- **Content**: Brief narrative or diagram showing before/after state
- **Location**: Optional subsection under Section A or B

**P8: Adopt Living Document Pattern**
- **Current**: Formal version/iteration in YAML header
- **Proposed**: Retain YAML version for major milestones; add inline change log for minor updates

#### C. Governance Implication

**Decision Impact**: P1-P4 (P1 priority) should be incorporated into T102B1 standard. P5-P8 (P2-P3 priority) are optional enhancements.

**Risk**: None - proposals are additive and backward-compatible.

---

### Topic 8: T102 Request Structural Assessment

**Objective**: Assess specific T102 Request sections against industry-standard necessity and placement.

#### A. Evidence & Forensics

**Source**: Client QA questions (per brief), Topics 1-3 industry analysis

#### B. Analysis

**Structural Assessment Table**:

| Section | Client QA Question | Industry Finding | Recommendation |
|:---|:---|:---|:---|
| **A. Feature Solution Framework** | Is this section necessary in a hybrid SRS/BRD document? | YES - Combines ISO 42010 stakeholder viewpoints with problem framing. Industry equivalent: BRD "Project Context" + SRS "Introduction". Effective placement at document start. | **KEEP** - Retain but make A.2 (Decision Criteria) optional for simple features |
| **Governance & Roadmap (Missing)** | Should Feature-level requests include development phases/roadmap? When necessary vs. optional? | CONDITIONAL - SAFe recommends roadmap at Epic/Capability level, not Feature level. Feature-level governance (GDRs) appropriate when architectural decisions required. Industry practice: roadmap if >1 PI duration or >3 dependent teams. | **ADD (Optional)** - Add "Development Phases" subsection to Section G when: (1) Feature spans >1 PI, (2) >3 team dependencies, (3) Complex sequencing required. Otherwise omit. |
| **F vs. F.6: FR vs IG Placement** | Where should FRs live relative to Implementation Guidance? | MERGE RECOMMENDED - Industry SRS combines "what" (FR) with "how" (implementation notes) per requirement. Separation creates duplication. ISO 29148 does not mandate separation. | **MODIFY** - Merge F.6 into F.4/F.5 or defer F.6 to Design. FR should be self-contained with inline guidance where needed. |
| **J. Stories & Specification** | Is story-level specification necessary at Request level? | DEFER RECOMMENDED - SAFe Feature level = benefit hypothesis + feature-level AC only. Story FRs belong at Sprint planning per Agile "just enough" documentation. Story-level at Feature spec is waterfall anti-pattern. | **MODIFY** - Convert Section J to "Story Index" (ID, title, one-line purpose). Defer full story FRs/ACs to Design/Concept artifact. |
| **Missing: Current/Future State** | What additional sections are important from industry perspectives? | ADD (Optional) - BRD best practice includes current state analysis and future state vision. Useful for features involving process change or system migration. | **ADD (Optional)** - Add "Current State" and "Future State" subsections to Section A or B for complex features involving process/system changes. |
| **Missing: User Personas** | - | CONSIDER - Modern PRDs emphasize user personas over role-based stakeholder tables. Section D uses roles; personas provide richer user context. | **MODIFY (Optional)** - Allow persona-style descriptions in Section D "Persona" column where beneficial. |

**Summary of Structural Recommendations**:

| Section | Action | Rationale |
|:---|:---|:---|
| A. Feature Solution Framework | KEEP (A.2 optional) | Industry-aligned, effective |
| B. Source & Scope | KEEP | Industry-standard |
| C. Business Objectives | KEEP + add benefit hypothesis | SAFe alignment |
| D. Stakeholders | KEEP (persona optional) | Industry-standard |
| E. Inherited Considerations | MODIFY (reference-only) | Reduce duplication |
| F.1-F.5 | KEEP | Industry-standard |
| F.6 Implementation Guidance | MODIFY (merge or defer) | Reduce FR/IG duplication |
| F.7 Integration Notes | KEEP | Industry-aligned |
| G. Governance Decisions | KEEP (optional) | ADR best practice |
| H. Issues & Risks | KEEP | PRINCE2/PMBOK aligned |
| I. Research & Notes | KEEP (optional) | Unique strength |
| J. Stories & Specification | MODIFY (index only) | Defer detail to Design |
| K. Acceptance Criteria | KEEP (feature-level) | Industry-standard |
| NEW: Governance & Roadmap | ADD (optional) | For complex features |
| NEW: Current/Future State | ADD (optional) | BRD best practice |

#### C. Governance Implication

**Decision Impact**: T102B1 should implement structural modifications above. Key changes:
1. Section J reduction to Story Index
2. FR/IG merge or deferral
3. RID inheritance simplification
4. Optional section classification

**Risk**: T102B-RISK-004 - Structural changes may require template migration for existing Request artifacts.

---

### Topic 9: Development Workflow Typology

**Objective**: Compare industry-standard workflows for different development types beyond discovery.

#### A. Evidence & Forensics

**Source**: [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow), [Hotfix vs Bugfix](https://www.browserstack.com/guide/hotfix-vs-bugfix), [Technical Debt Management](https://www.netguru.com/blog/managing-technical-debt), [Kanban vs Scrum](https://www.atlassian.com/agile/kanban/kanban-vs-scrum)

**Observation**:
Industry recognizes distinct workflow types with different documentation requirements:

1. **Hotfix/Critical Bug**: Urgent, bypasses normal release cycle, minimal documentation
2. **Standard Bug Fix**: Planned, normal release cycle, standard documentation
3. **Enhancement**: Minor changes to existing features, lightweight documentation
4. **Refactoring/Technical Debt**: Code quality improvements, documentation optional
5. **New Feature (Discovery)**: Full feature development, comprehensive documentation

Gitflow pattern: "Hotfix branches are a lot like release branches and feature branches except they're based on main instead of develop. This is the only branch that should fork directly off of main."

Technical debt best practice: "Intel suggests dedicating a certain percentage of IT teams to work on technical debt items with small refactoring installments in each iteration."

#### B. Analysis

**Workflow Typology Matrix**:

| Development Type | Trigger Criteria | Documentation Requirement | T102 Recommendation |
|:---|:---|:---|:---|
| **Hotfix** | Production critical, security vulnerability, P0 incident | PR template only: Problem, Fix, Testing, Rollback plan | No SPS/Request - Direct PR with structured template |
| **Bug Fix (Standard)** | Non-critical defect, planned sprint work | Issue ticket + PR template | No SPS/Request - Issue ticket with AC + PR template |
| **Enhancement (Minor)** | Small change to existing feature, <1 sprint effort | Issue ticket + PR template | No SPS/Request - Issue ticket with scope + PR template |
| **Enhancement (Major)** | Significant change to existing feature, 1-2 sprint effort | Request Lite | Request Lite + PR |
| **Refactoring** | Technical debt reduction, no functional change | PR template with rationale | No SPS/Request - PR template with technical justification |
| **New Feature (Simple)** | New functionality, <1 PI, low complexity | Request Lite | Request Lite + optional Concept |
| **New Feature (Complex)** | New functionality, 1+ PI, high complexity, multiple dependencies | Full SPS -> Request -> Concept | Full T102 workflow |

**Documentation Requirement Decision Tree**:

```
START
  |
  v
Is this a production emergency (P0/P1)?
  |-- YES --> HOTFIX: PR template only
  |-- NO  --> Continue
        |
        v
      Is this a bug fix or refactoring (no new functionality)?
        |-- YES --> BUG/REFACTOR: Issue ticket + PR template
        |-- NO  --> Continue
              |
              v
            Is this an enhancement to existing feature?
              |-- YES --> Is effort < 1 sprint?
              |     |-- YES --> MINOR ENHANCEMENT: Issue ticket + PR
              |     |-- NO  --> MAJOR ENHANCEMENT: Request Lite + PR
              |-- NO --> NEW FEATURE
                    |
                    v
                  Is complexity LOW and duration < 1 PI?
                    |-- YES --> SIMPLE FEATURE: Request Lite + optional Concept
                    |-- NO  --> COMPLEX FEATURE: Full SPS -> Request -> Concept
```

**Criteria for Workflow Selection**:

| Criterion | Threshold for Full Request | Threshold for Request Lite | PR Only |
|:---|:---|:---|:---|
| **Impact** | Cross-team, user-facing | Single team, internal | Localized |
| **Scope** | New capability | Existing capability change | Bug/refactor |
| **Risk** | Architectural, security | Moderate | Low |
| **Complexity** | High (>5 stories) | Medium (2-5 stories) | Low (<2 stories) |
| **Duration** | >1 PI | 1 PI or less | <1 sprint |
| **Dependencies** | >2 teams | 1-2 teams | None |

**PR Template Structure for Lightweight Workflows**:

```markdown
## Type
[ ] Hotfix | [ ] Bug Fix | [ ] Enhancement | [ ] Refactoring

## Problem/Context
Brief description of what this PR addresses.

## Solution
What changes were made and why.

## Testing
How was this tested? What scenarios were verified?

## Rollback Plan (Hotfix only)
How to revert if issues arise.

## Related Issues
Links to issue tickets, if any.
```

#### C. Governance Implication

**Decision Impact**: T102 consultancy layer should support multiple workflow types:
1. **Full Workflow** (SPS -> Request -> Concept): Complex new features only
2. **Lite Workflow** (Request Lite -> optional Concept): Simple features, major enhancements
3. **Direct Workflow** (Issue + PR): Bug fixes, refactoring, minor enhancements, hotfixes

**Integration Recommendation**:
- Add workflow selection guidance to SPS or consultancy intake process
- Establish clear criteria for workflow selection
- Provide PR template for lightweight workflows
- Document when to escalate from Lite to Full workflow

**Risk**: T102B-RISK-005 - Without workflow differentiation, teams may apply heavyweight documentation to lightweight changes, creating friction and adoption resistance.

---

## IV. ISSUE & RISK REGISTER (T102-ADR-007)

**Issues**

| ID | Title | Description | Owner | Status | Priority | Proposed Date |
|:---|:---|:---|:---|:---|:---|:---|
| T102B-ISSUE-001 | FR/IG Merge Strategy | Determine optimal merge pattern for Section F FRs and Section F.6 IGs to eliminate duplication while preserving traceability | LLM_Consultant | OPEN | HIGH | 2026-01-13 |
| T102B-ISSUE-002 | Request Lite Template | Define minimum viable Request template structure for simple features and enhancements | LLM_Consultant | OPEN | HIGH | 2026-01-13 |
| T102B-ISSUE-003 | Section J Deferral | Determine handoff mechanism for Story Index to Design/Concept artifacts | LLM_Consultant | OPEN | MEDIUM | 2026-01-13 |

**Risks**

| ID | Title | Description | Owner | Status | Priority | Proposed Date |
|:---|:---|:---|:---|:---|:---|:---|
| T102B-RISK-001 | Story-Level Documentation Trap | Story-level FRs at Request stage may perpetuate "documentation trap" blocking MVP delivery | LLM_Consultant | OPEN | HIGH | 2026-01-13 |
| T102B-RISK-002 | Agile Adoption Friction | Current documentation weight conflicts with Agile "just enough" principles, may create adoption resistance | LLM_Consultant | OPEN | MEDIUM | 2026-01-13 |
| T102B-RISK-003 | Improvement Implementation Delay | Failure to address P1 proposals (P1-P4) will perpetuate current pain points | LLM_Consultant | OPEN | HIGH | 2026-01-13 |
| T102B-RISK-004 | Template Migration | Structural changes may require migration for existing Request artifacts | LLM_Consultant | OPEN | LOW | 2026-01-13 |
| T102B-RISK-005 | Workflow Undifferentiation | Without workflow typology, heavyweight documentation may be applied to lightweight changes | LLM_Consultant | OPEN | MEDIUM | 2026-01-13 |

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
|:---|:---|:---|:---|
| T102B1-REQUEST | Template Structure | Define Request Lite variant | Topic 7, P1 |
| T102B1-REQUEST | Section J | Convert to Story Index pattern | Topic 8, Section J assessment |
| T102B1-REQUEST | Section F | Merge FR/IG sections | Topic 7, P3 |
| T102B1-REQUEST | Section E | Implement reference-only inheritance | Topic 7, P5 |
| T102B1-REQUEST | Mandatory/Optional | Classify all sections | Topic 7, P4 |
| T102-ADR-XXX | Workflow Typology | Create ADR for workflow selection criteria | Topic 9, Decision Tree |
| T102-TEMPLATE | PR Template | Create lightweight PR template | Topic 9, PR Template Structure |

---

## VI. SOURCE MATERIAL

**Brief Version**: T102B-RES-001 v1.0.0 i1 (2026-01-12)

**Industry Standard Sources (Web Search)**:
*   [IEEE 830-1998 Standard](https://ieeexplore.ieee.org/document/720574)
*   [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html)
*   [ReqView ISO 29148 Templates](https://www.reqview.com/doc/iso-iec-ieee-29148-templates/)
*   [BABOK BRD Patterns](https://businessanalystmentor.com/business-requirements-document/)
*   [Asana BRD Template](https://asana.com/resources/business-requirements-document-template)
*   [Wrike BRD Guide](https://www.wrike.com/blog/how-write-business-requirements-document/)
*   [Notion PRD Templates](https://www.notion.com/templates/category/product-requirements-doc)
*   [SAFe Feature Specification](https://framework.scaledagile.com/blog/crafting-clarity-using-feature-templates-to-shape-and-communicate-intent)
*   [SAFe Features and Capabilities](https://framework.scaledagile.com/features-and-capabilities)
*   [SAFe Story](https://framework.scaledagile.com/story)
*   [Atlassian User Stories](https://www.atlassian.com/agile/product-management/requirements)
*   [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
*   [Hotfix vs Bugfix](https://www.browserstack.com/guide/hotfix-vs-bugfix)
*   [Technical Debt Management](https://www.netguru.com/blog/managing-technical-debt)
*   [Kanban vs Scrum](https://www.atlassian.com/agile/kanban/kanban-vs-scrum)
*   [BRD vs SRS Analysis](https://thebusinessanalystjobdescription.com/brd-vs-srs-vs-frs-detailed-comparison/)
*   [Requirements Traceability Matrix](https://www.testrail.com/blog/requirements-traceability-matrix/)

**Internal Artifacts Analyzed**:
*   `prompt/artifacts/tasks/T102/consultant/request/request_T102A-SPSST.md`
*   `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md`
*   `prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102B-RES-001_request-artifact-analysis.md`
