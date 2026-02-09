---
artifact_type: 'NOTES'
initiative_id: 'T102'
epic_id: 'T102'
epic_code: 'CDW'
version: '1.0.0'
date: '2026-01-13'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T102/consultant/workspace/plan/T102/roadmap_T102-CDW.md'
target_document: 'roadmap_T102-CDW.md'
target_section: 'Phase 0 Activities'
---

# PHASE 0 NOTES: `T102 / CDW` - Consultancy Development Workflows

## I. EXECUTIVE SUMMARY

Phase 0 consultation for initiative T102 (Consultancy Development Workflows) addressed critical workflow efficiency concerns and established the research foundation for standardizing consultant artifacts. Key outcomes include:

1. **QA Resolution**: Addressed client concerns regarding FR/IG conflict, workflow speed, RID repetition, Feature-level GDRs/ADRs, and Concept artifact conflicts
2. **Research Commission**: Two research briefs created and executed (T102-RES-003 Internal Status Assessment, T102B-RES-001 Request Artifact Analysis)
3. **Initiative Plan**: Created `roadmap_T102-CDW.md` as the master project management document
4. **Key Decisions**: Feature-level GDR/ADR exception-based approach approved, Request Lite <200 lines threshold approved, Story FR deferral to Design approved

---

## II. CONSULTANCY DIALOGUE NOTES (WORKING; NON-NORMATIVE)
<!-- PURPOSE: Capture raw dialogue so nothing is lost; convert into normative bodies above. -->

### A. QA Comment Dialogue Notes

**Dialogue Date**: 2026-01-13
**Status**: Resolved with research commission

**Client QA Comments Addressed**:

1. **FR/IG Conflict (Comment 1)**:
   - **Observation**: Duplication occurs when Epic-level IG describes patterns that Feature IG must re-contextualize, and Story FRs then repeat the same patterns as acceptance criteria
   - **Assessment**: Feature-level IG could absorb story-level implementation detail, with Story FR becoming acceptance criteria only (Gherkin format)
   - **Exemplar Reference**: T810A1 pattern where stories reference IGs rather than duplicating them

2. **Workflow Speed (Comment 1.2)**:
   - **Root Cause**: The `sps -> request -> design` workflow is waterfall-heavy for MVP work
   - **Client Observation**: T810A2 "effectively skips story-level specs" validates this concern
   - **Industry Perspective**: Agile BRD/SRS patterns use thin SPS + deliverable-ready Request + Design only for complex stories

3. **Deliverables at Request (Comment 1.3)**:
   - **Strong Agreement**: Current workflow places deliverable production at Design, but Request should be the "minimum viable spec for implementation"
   - **Recommendation**: Design reserved for high-risk stories requiring detailed architectural decisions, significant integration complexity, or ADR variance documentation

4. **RID Repetition (Comment 2)**:
   - **Observation**: Per T102-STD-005, RIDs defined at scope levels (I-RID, E-RID, F-RID, S-RID) with current pattern requiring repetition
   - **Industry Standard**: ISO 29148 and BABOK v3 use inheritance by reference, not repetition
   - **Proposal**: Request should inherit E-RIDs via table reference, focus on truly feature-specific F-RIDs, NOT redefine ASSUM/CON/QG/DEP unchanged at Epic level

5. **F-GDRs/ADRs Necessity (Comment 3)**:
   - **Industry Analysis**: IEEE 42010, SAFe, MADR Pattern indicate Feature-level ADRs uncommon; typically Epic/Initiative scope
   - **Recommendation**: Feature-level GDRs/ADRs should be optional and exception-based (required when Feature deviates from Epic/Initiative ADRs)
   - **Decision**: **APPROVED** - Exception-based approach for Feature-level GDRs/ADRs

6. **Concept Artifact Conflicts (Comment 4)**:
   - **Observation**: `concept_T102-CONSULTANT.md` contains initiative/epic ADRs that may conflict with feature-level requests
   - **Industry Standard**: 42010 (Architecture evolves alongside requirements), SAFe ART (Architecture runway precedes feature development)
   - **Proposal**: Concept should be additive, not prescriptive at Feature detail level; Feature ADRs added to Concept after Request approval

---

### B. Research Commission Notes

**Dialogue Date**: 2026-01-13
**Status**: Research briefs created and executed

**Research Brief 1: T102-RES-003 (Internal Status Assessment)**:
- **Path**: `prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102-RES-003_initiative-status-assessment.md`
- **Scope**: Internal repository analysis for artifact inventory, epic progress, workflow bottlenecks
- **Output Format**: Standard research report template (NOT plan_ file - corrected per Client feedback)
- **Key Correction**: Removed instruction for researcher to create plan_ file; LLM_Consultant responsible for plan creation

**Research Brief 2: T102B-RES-001 (Request Artifact Analysis)**:
- **Path**: `prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102B-RES-001_request-artifact-analysis.md`
- **Scope**: External research comparing T102 Request to IEEE 830/ISO 29148 (SRS), BABOK v3 (BRD), SAFe Feature specs
- **Primary Tool**: WebSearch specified as primary tool per Client feedback
- **Topic 8 Added**: T102 Request Structural Assessment addressing client's specific structural questions
- **Topic 9 Added**: Development Workflow Typology covering bug fix, enhancement, refactoring workflows

**Topic 9 Addition Context**:
- **Client Comment**: Current `sps -> request` workflow does not suit debugging issues or feature enhancements
- **Research Question**: What is the ideal workflow for these development types from industry-standard perspective?
- **Coverage**: Bug/defect resolution, feature enhancement, technical debt/refactoring, lightweight documentation alternatives

---

### C. Initiative Plan Notes

**Dialogue Date**: 2026-01-13
**Status**: Plan file created

**Plan File Creation**:
- **Original Proposal**: `plan_T102_phase0.md`
- **Client Refinement**: Renamed to `roadmap_T102-CDW.md`
- **Rationale**: This is the master project management file for the entire initiative, serving as parent for all epic-level plans
- **Location**: `prompt/artifacts/tasks/T102/consultant/workspace/plan/T102/`

**Industry-Standard Naming Assessment**:
- **SAFe**: "Program Increment (PI) Plan" or "Solution Roadmap"
- **PMBOK**: "Product Development Plan" or "Development Master Plan"
- **BABOK v3**: "Solution Roadmap Document"
- **Note**: Client queried industry-standard formal name for this document type

**Plan Structure**:
- Phase 0 (Foundation & Research Commission) documented
- Research register with T102-RES-003 and T102B-RES-001
- Decision log capturing Phase 0 decisions
- Risk assessment for research and execution phases

---

### D. Research Integration Notes

**Dialogue Date**: 2026-01-13
**Status**: Research completed and integrated

**T102-RES-003 Key Findings (Internal Status Assessment)**:
- **Verdict**: PIVOT RECOMMENDED with structured mitigation
- **Governance Layer**: 80% complete (5/8 GDRs accepted)
- **Execution Layer**: 25-30% complete (critical bottlenecks at SPS->REQUEST handoff)
- **Documentation Debt**: 25-40% content redundancy; 20-30% reduction achievable
- **Critical Gap**: T102B and T102D lack Epic-level ADRs

**T102B-RES-001 Key Findings (External Research)**:
- **Verdict**: CONDITIONAL GO - Strong industry alignment but requires streamlining
- **T102 vs SAFe**: Exceeds SAFe Feature specs by 10x (700+ lines vs name + benefit hypothesis + AC)
- **FR vs IG**: Research recommends merging to eliminate duplication
- **Stories & Specification**: Recommends deferral to Design; keep Story Index only at Request
- **Request Lite**: Recommends <200 lines for simple features (60% authoring reduction)

**Workflow Typology (Topic 9) Findings**:
| Development Type | Recommended Workflow | Documentation Level |
|:-----------------|:---------------------|:--------------------|
| New Feature (Complex) | SPS -> Request -> Design | Full consultancy |
| New Feature (Simple) | SPS -> Request Lite | Simplified Request |
| Bug Fix / Hotfix | Git PR only | PR template with root cause |
| Enhancement | Request Lite or PR | Based on scope/risk |
| Refactoring | Git PR only | PR template with before/after |
| Technical Debt | Request Lite | Lightweight specification |

---

### E. Decision Points Notes

**Dialogue Date**: 2026-01-13
**Status**: Key decisions captured

**Decision 1: Research Execution Sequence**:
- **Assessment**: T102-RES-003 and T102B-RES-001 can run in parallel but sequencing has benefits
- **Decision**: Execute T102-RES-003 first (internal, faster) -> feed findings into T102B-RES-001 refinement
- **Outcome**: Both executed successfully; findings integrated

**Decision 2: Feature-level GDR/ADR Approach**:
- **Proposal**: Feature-level GDRs/ADRs should be optional and exception-based
- **Decision**: **APPROVED** - Required only when Feature deviates from Epic ADRs
- **Implication**: T102B1 Request standard will not mandate Feature-level GDRs/ADRs

**Decision 3: Request Lite Threshold**:
- **Research Recommendation**: <200 lines for simple features
- **Decision**: **APPROVED** - 200-line threshold for Request Lite variant
- **Implication**: T102B1 will define Request Lite template for features below threshold

**Decision 4: Story FR Deferral**:
- **Research Recommendation**: Move story-level FRs from Request to Design
- **Decision**: **APPROVED** - Significant structural change accepted
- **Implication**: Request keeps Story Index only; detailed Story FRs at Design/Sprint planning

**Decision 5: T801/T801A Dependency**:
- **Context**: T801/T801A waiting for T102B standards
- **Decision**: T801/T801A to wait for T102B-STD-001 formalization before proceeding
- **Implication**: T102B development is blocking dependency for T801 Request artifacts

**Decision 6: Workflow Typology Formalization**:
- **Question**: Should multi-workflow typology (Topic 9) be ADR or GDR?
- **Status**: Open for next session
- **Options**: T102-STD-009 (new Initiative ADR) OR integrate into T102-GDR-001 (Operating Model)

---

## III. KEY DECISIONS CAPTURED

| # | Decision | Status | Date | Informed By |
|:--|:---------|:-------|:-----|:------------|
| 1 | Research execution sequence (T102-RES-003 first) | Approved | 2026-01-13 | Consultant assessment |
| 2 | Feature-level GDR/ADR exception-based approach | Approved | 2026-01-13 | Industry standard analysis |
| 3 | Request Lite <200 lines threshold | Approved | 2026-01-13 | T102B-RES-001 findings |
| 4 | Story FR deferral to Design | Approved | 2026-01-13 | T102B-RES-001 findings |
| 5 | T801/T801A to wait for T102B-STD-001 | Approved | 2026-01-13 | Dependency analysis |
| 6 | Workflow Typology formalization (ADR vs GDR) | Open | - | Pending next session |

---

## IV. OPEN QUESTIONS FOR NEXT SESSION

### A. Hygiene Sprint Priority

**Question**: Should a Hygiene Sprint be prioritized to address documentation debt (25-40% redundancy) identified in T102-RES-003?

**Context**: Research identified significant content redundancy across T102 artifacts that could be reduced by 20-30%.

**Options**:
- (A) Address as part of T102B1 development (integrate cleanup into new standard)
- (B) Separate Hygiene Sprint before T102B1 development
- (C) Defer until after T102B1 standard established

---

### B. Workflow Typology Formalization

**Question**: Should the multi-workflow typology (Topic 9 findings) be formalized as ADR or GDR?

**Context**: Topic 9 established development workflow categories (Discovery, Bug Fix, Enhancement, Refactoring, Technical Debt) with different documentation requirements.

**Options**:
- (A) T102-STD-009 (new Initiative ADR) - More formal, architectural decision
- (B) Integrate into T102-GDR-001 (Operating Model) - Extends existing governance
- (C) T102B-ADR (Epic-level) - Specific to Request artifact scope

---

### C. I-RID/I-ADR Update Assessment

**Question**: Do existing Initiative-level RIDs and ADRs need updating based on research findings?

**Context**: T102-RES-003 identified governance layer at 80% complete but execution layer at 25-30%. Research findings may require I-RID/I-ADR modifications.

**Specific Items to Assess**:
- T102-STD-003 (Explicit Inheritance Model) - Does "list IDs only" guidance need strengthening?
- T102-STD-005 (ID Specification Standard) - Are RID category definitions clear enough given repetition concerns?
- T102-GDR-001 (Operating Model) - Should workflow typology be integrated here?

---

## V. ARTIFACTS CREATED/MODIFIED

| Artifact | Action | Path |
|:---------|:-------|:-----|
| T102-RES-003 Brief | Created | `prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102-RES-003_initiative-status-assessment.md` |
| T102B-RES-001 Brief | Created + Modified | `prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102B-RES-001_request-artifact-analysis.md` |
| T102-RES-003 Report | Created | `prompt/artifacts/tasks/T102/consultant/research/report/report_T102-RES-003_initiative-status-assessment.md` |
| T102B-RES-001 Report | Created | `prompt/artifacts/tasks/T102/T102B/research/report/report_T102B-RES-001_request-artifact-analysis.md` |
| Initiative Plan | Created | `prompt/artifacts/tasks/T102/consultant/workspace/plan/T102/roadmap_T102-CDW.md` |

---

## VI. NEXT STEPS

1. **Client Decision Required**: Resolve open questions (Hygiene Sprint, Workflow Typology, I-RID/I-ADR updates)
2. **T102B-STD-001 Design**: Design Request Architecture Standard informed by T102B-RES-001 findings
3. **Request Lite Template**: Create simplified Request template for <200 line features
4. **SPS Feature Register Expansion**: Add T102A2, T102A3 features (P1 action from T102-RES-003)
5. **Workflow Selection Decision Tree**: Define criteria for workflow selection (Discovery vs PR-only)

---
