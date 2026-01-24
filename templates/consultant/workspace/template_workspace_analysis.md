---
artifact_type: 'ANALYSIS'
initiative_id: '[ID]'
epic_id: '[ID]'
epic_code: '[CODE]'
research_id: '[RES-ID]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
research_brief: '[path to research brief]'
research_report: '[path to research report]'
target_proposal: '[path to proposal file where analysis will inform]'
target_plan: '[path to plan file for context]'
---

# ANALYSIS: [RES-ID] — [Research Title]

<!-- PURPOSE: This ANALYSIS artifact bridges research outputs and proposal inputs. It synthesizes research findings, extracts actionable insights, maps findings to E-ID candidates, and provides consultant recommendations. Analysis files are created AFTER receiving a research report and BEFORE updating proposals. -->

## I. EXECUTIVE SUMMARY

<!-- PURPOSE: Provide immediate overview of research analysis outcomes and high-level recommendation -->

**Research Commission**: [RES-ID] — [Research Title]
**Analysis Purpose**: [What this analysis achieves in 1-2 sentences]
**Key Recommendation**: [High-level recommendation based on research findings]

**Research Verdict**: [PIVOT RECOMMENDED / CONDITIONAL GO / PROCEED AS PLANNED / RESEARCH EXTENSION REQUIRED / etc.]

**Impact Assessment**: [High / Medium / Low impact on epic/initiative development]

**Critical Insights**:
- [Insight 1: Most significant finding]
- [Insight 2: Key implication]
- [Insight 3: Primary recommendation]

---

## II. SOURCE MATERIAL SUMMARY
<!-- PURPOSE: Provide structured overview of the research inputs being analyzed. This section establishes provenance and context for all downstream analysis. -->

### A. Research Brief Context
**Commission Date**: YYYY-MM-DD
**Commissioning Need**: [Why research was commissioned - what question/uncertainty triggered it]
**Research Topics**:
- [Topic 1]
- [Topic 2]
- [Topic 3]

**Key Questions Addressed**:
1. [Question 1 from brief]
2. [Question 2 from brief]
3. [Question 3 from brief]

**Expected Deliverables**: [What the research was expected to produce]

---

### B. Research Report Overview
**Report Date**: YYYY-MM-DD
**Report Version**: [Version number]
**Research Approach**: [Methodology used - e.g., codebase analysis, documentation review, comparative analysis]
**Scope**: [What was covered and what was explicitly out of scope]

**Key Findings Summary**:
- [Finding 1: Brief summary]
- [Finding 2: Brief summary]
- [Finding 3: Brief summary]
- [Finding 4: Brief summary]

**Research Quality Assessment**: [Confidence level in findings - HIGH/MEDIUM/LOW and why]

---

## III. KEY FINDINGS EXTRACTION
<!-- PURPOSE: Break down research findings into structured, actionable insights organized by topic or theme. Each topic analysis should move from raw finding → consultant assessment → actionable insight → recommendation. This section is the foundation for E-ID candidate mapping. -->

### Topic 1: [TOPIC TITLE]
**Research Finding**: [What the research revealed - direct summary from report]

**Consultant Assessment**:
- **Significance**: [Why this finding matters to epic/initiative success]
- **Confidence**: [HIGH/MEDIUM/LOW - based on evidence quality]
- **Alignment**: [How this relates to current plan/proposal state]

**Actionable Insights**:
- [Insight 1: Specific implication for development]
- [Insight 2: Specific implication for architecture/design]
- [Insight 3: Specific implication for governance/process]

**Recommendation**: [What should be done based on this finding - be specific and actionable]

**E-ID Implications**: [Which E-ID categories this finding affects - e.g., "Will generate E-ASSUM and E-QG candidates"]

---

### Topic 2: [TOPIC TITLE]
**Research Finding**: [What the research revealed]

**Consultant Assessment**:
- **Significance**: [Why this matters]
- **Confidence**: [HIGH/MEDIUM/LOW]
- **Alignment**: [Relationship to current state]

**Actionable Insights**:
- [Insight 1]
- [Insight 2]
- [Insight 3]

**Recommendation**: [Specific action]

**E-ID Implications**: [Affected E-ID categories]

---

### Topic 3: [TOPIC TITLE]
**Research Finding**: [What the research revealed]

**Consultant Assessment**:
- **Significance**: [Why this matters]
- **Confidence**: [HIGH/MEDIUM/LOW]
- **Alignment**: [Relationship to current state]

**Actionable Insights**:
- [Insight 1]
- [Insight 2]
- [Insight 3]

**Recommendation**: [Specific action]

**E-ID Implications**: [Affected E-ID categories]

---

### Topic 4: [TOPIC TITLE]
<!-- Add additional topics as needed based on research scope -->

---

## IV. CROSS-CUTTING SYNTHESIS
<!-- PURPOSE: Identify patterns, themes, and insights that span multiple topics. This section reveals systemic findings that aren't visible when looking at individual topics in isolation. Cross-cutting synthesis often generates the most valuable E-ID candidates. -->

### A. Pattern Analysis
<!-- PURPOSE: Identify recurring themes across multiple research topics -->

**Pattern 1: [PATTERN NAME]**
- **Observation**: [What pattern emerged across topics - reference specific topics from Section III]
- **Implication**: [What this means for epic development, architecture, or governance]
- **Affected Topics**: [List of Topic # references where this pattern appears]
- **Recommendation**: [How to address this pattern systematically]

**Pattern 2: [PATTERN NAME]**
- **Observation**: [What pattern emerged]
- **Implication**: [What this means]
- **Affected Topics**: [Topic references]
- **Recommendation**: [How to address]

**Pattern 3: [PATTERN NAME]**
- **Observation**: [What pattern emerged]
- **Implication**: [What this means]
- **Affected Topics**: [Topic references]
- **Recommendation**: [How to address]

---

### B. Gap Analysis
<!-- PURPOSE: Identify gaps between current state and research-revealed needs -->

**Gap 1: [GAP DESCRIPTION]**
- **Current State**: [What exists now in codebase/documentation/process]
- **Research Reveals**: [What gap was identified through research]
- **Impact**: [What problems this gap causes or will cause]
- **Recommendation**: [How to address gap - specific actions]
- **Priority**: [HIGH/MEDIUM/LOW]

**Gap 2: [GAP DESCRIPTION]**
- **Current State**: [What exists now]
- **Research Reveals**: [What gap was identified]
- **Impact**: [Problems caused]
- **Recommendation**: [How to address]
- **Priority**: [HIGH/MEDIUM/LOW]

**Gap 3: [GAP DESCRIPTION]**
- **Current State**: [What exists now]
- **Research Reveals**: [What gap was identified]
- **Impact**: [Problems caused]
- **Recommendation**: [How to address]
- **Priority**: [HIGH/MEDIUM/LOW]

---

### C. Risk & Opportunity Identification
<!-- PURPOSE: Explicitly catalog risks and opportunities revealed by research. These directly map to E-OID candidates (Issues/Risks) and may influence E-RID candidates (Constraints/Quality Goals). -->

**Risks Identified**:
| Risk | Description | Severity | Likelihood | Mitigation Recommendation | E-OID Candidate |
|:-----|:------------|:---------|:-----------|:--------------------------|:----------------|
| [Risk 1] | [What could go wrong] | [High/Med/Low] | [High/Med/Low] | [How to mitigate] | [E-RISK-###] |
| [Risk 2] | [What could go wrong] | [High/Med/Low] | [High/Med/Low] | [How to mitigate] | [E-RISK-###] |
| [Risk 3] | [What could go wrong] | [High/Med/Low] | [High/Med/Low] | [How to mitigate] | [E-RISK-###] |

**Opportunities Identified**:
| Opportunity | Description | Potential Value | Effort Required | Recommendation | E-OID Candidate |
|:------------|:------------|:----------------|:----------------|:---------------|:----------------|
| [Opp 1] | [What could be gained] | [High/Med/Low] | [High/Med/Low] | [How to capitalize] | [E-NOTE-###] |
| [Opp 2] | [What could be gained] | [High/Med/Low] | [High/Med/Low] | [How to capitalize] | [E-NOTE-###] |
| [Opp 3] | [What could be gained] | [High/Med/Low] | [High/Med/Low] | [How to capitalize] | [E-NOTE-###] |

---

### D. Dependency & Interface Mapping
<!-- PURPOSE: Map external dependencies and integration points revealed by research -->

**Dependencies Identified**:
- **Dependency 1**: [What the epic depends on]
  - **Nature**: [External system, library, process, decision, etc.]
  - **Impact**: [How this dependency affects development]
  - **Mitigation**: [How to manage this dependency]
  - **E-ID Candidate**: [E-DEP-###]

- **Dependency 2**: [What the epic depends on]
  - **Nature**: [Type of dependency]
  - **Impact**: [Effect on development]
  - **Mitigation**: [Management approach]
  - **E-ID Candidate**: [E-DEP-###]

**Interface Points Identified**:
- **Interface 1**: [Where epic interacts with external systems/components]
  - **Type**: [API, file format, protocol, process, etc.]
  - **Requirements**: [What the interface must support]
  - **E-ID Candidate**: [E-IF-###]

- **Interface 2**: [Interaction point]
  - **Type**: [Interface type]
  - **Requirements**: [Interface requirements]
  - **E-ID Candidate**: [E-IF-###]

---

## V. E-ID CANDIDATE MAPPING
<!-- PURPOSE: Map research findings to specific E-ID candidates that should be proposed. This section DIRECTLY feeds into proposal Section II (CANDIDATE INVENTORY). Each candidate listed here should be ready for Socratic dialogue and eventual full body development. Use consistent ID patterns: E-ASSUM-###, E-CON-###, etc. -->

### A. E-RID Candidates

#### A.1 Assumptions (E-ASSUM-###)
<!-- PURPOSE: Identify foundational assumptions revealed or validated by research -->

| Candidate ID | Title | Research Source | Rationale | Priority |
|:-------------|:------|:----------------|:----------|:---------|
| E-ASSUM-001 | [Assumption title - what is assumed to be true] | [Topic #.# or Section reference] | [Why this should be an assumption based on research findings] | [H/M/L] |
| E-ASSUM-002 | [Assumption title] | [Research source] | [Rationale from research] | [H/M/L] |
| E-ASSUM-003 | [Assumption title] | [Research source] | [Rationale from research] | [H/M/L] |

**Total Candidates**: [#]
**Recommendation**: Prioritize [List high-priority IDs] for full body development in consultancy dialogue.

---

#### A.2 Constraints (E-CON-###)
<!-- PURPOSE: Identify constraints (technical, business, regulatory) that limit solution space -->

| Candidate ID | Title | Research Source | Rationale | Priority |
|:-------------|:------|:----------------|:----------|:---------|
| E-CON-001 | [Constraint title - what cannot be changed] | [Topic #.# or Section reference] | [Why this is a constraint based on research] | [H/M/L] |
| E-CON-002 | [Constraint title] | [Research source] | [Rationale from research] | [H/M/L] |
| E-CON-003 | [Constraint title] | [Research source] | [Rationale from research] | [H/M/L] |

**Total Candidates**: [#]
**Recommendation**: Prioritize [List high-priority IDs] for full body development in consultancy dialogue.

---

#### A.3 Quality Goals (E-QG-###)
<!-- PURPOSE: Define quality attributes the solution must achieve -->

| Candidate ID | Title | Research Source | Rationale | Priority |
|:-------------|:------|:----------------|:----------|:---------|
| E-QG-001 | [Quality goal - what quality must be achieved] | [Topic #.# or Section reference] | [Why this quality goal based on research] | [H/M/L] |
| E-QG-002 | [Quality goal title] | [Research source] | [Rationale from research] | [H/M/L] |
| E-QG-003 | [Quality goal title] | [Research source] | [Rationale from research] | [H/M/L] |

**Total Candidates**: [#]
**Recommendation**: Prioritize [List high-priority IDs] for full body development in consultancy dialogue.

---

#### A.4 Dependencies (E-DEP-###)
<!-- PURPOSE: Document external dependencies that must be managed -->

| Candidate ID | Title | Research Source | Rationale | Priority |
|:-------------|:------|:----------------|:----------|:---------|
| E-DEP-001 | [Dependency title - what is depended upon] | [Section IV.D or Topic reference] | [Why this dependency exists per research] | [H/M/L] |
| E-DEP-002 | [Dependency title] | [Research source] | [Rationale from research] | [H/M/L] |
| E-DEP-003 | [Dependency title] | [Research source] | [Rationale from research] | [H/M/L] |

**Total Candidates**: [#]
**Recommendation**: Prioritize [List high-priority IDs] for full body development in consultancy dialogue.

---

#### A.5 Interfaces (E-IF-###)
<!-- PURPOSE: Define interface requirements for system boundaries -->

| Candidate ID | Title | Research Source | Rationale | Priority |
|:-------------|:------|:----------------|:----------|:---------|
| E-IF-001 | [Interface title - what interface is required] | [Section IV.D or Topic reference] | [Why this interface based on research] | [H/M/L] |
| E-IF-002 | [Interface title] | [Research source] | [Rationale from research] | [H/M/L] |
| E-IF-003 | [Interface title] | [Research source] | [Rationale from research] | [H/M/L] |

**Total Candidates**: [#]
**Recommendation**: Prioritize [List high-priority IDs] for full body development in consultancy dialogue.

---

#### A.6 Implementation Guidance (E-IG-###)
<!-- PURPOSE: Provide implementation-level guidance that doesn't fit other categories -->

| Candidate ID | Title | Research Source | Rationale | Priority |
|:-------------|:------|:----------------|:----------|:---------|
| E-IG-001 | [Guidance title - what guidance is needed] | [Topic #.# or Section reference] | [Why this guidance based on research] | [H/M/L] |
| E-IG-002 | [Guidance title] | [Research source] | [Rationale from research] | [H/M/L] |
| E-IG-003 | [Guidance title] | [Research source] | [Rationale from research] | [H/M/L] |

**Total Candidates**: [#]
**Recommendation**: Prioritize [List high-priority IDs] for full body development in consultancy dialogue.

---

### B. E-DID Candidates (GDR/ADR)

<!-- PURPOSE: Identify decisions that require formal documentation. Per T102-ADR-004, GDRs govern epic-level governance decisions and ADRs document architectural choices. ADRs typically pair with GDRs. -->

#### B.1 Governance Decisions (E-GDR-###)
<!-- PURPOSE: Epic-level governance decisions that shape development approach -->

| Candidate ID | Title | Research Source | Decision Context | Priority |
|:-------------|:------|:----------------|:-----------------|:---------|
| E-GDR-001 | [Governance decision title] | [Topic #.# or Section reference] | [What governance decision is needed and why based on research] | [H/M/L] |
| E-GDR-002 | [Governance decision title] | [Research source] | [Decision context from research] | [H/M/L] |
| E-GDR-003 | [Governance decision title] | [Research source] | [Decision context from research] | [H/M/L] |

**Total Candidates**: [#]
**Recommendation**: Prioritize [List high-priority IDs] for full body development in consultancy dialogue.

---

#### B.2 Architectural Decisions (E-ADR-###)
<!-- PURPOSE: Technical architectural decisions that implement governance choices -->

| Candidate ID | Title | Paired GDR | Research Source | Decision Context | Priority |
|:-------------|:------|:-----------|:----------------|:-----------------|:---------|
| E-ADR-001 | [Architectural decision title] | E-GDR-### | [Topic #.# reference] | [What architectural decision is needed per research] | [H/M/L] |
| E-ADR-002 | [Architectural decision title] | E-GDR-### | [Research source] | [Decision context from research] | [H/M/L] |
| E-ADR-003 | [Architectural decision title] | E-GDR-### | [Research source] | [Decision context from research] | [H/M/L] |

**Total Candidates**: [#]
**Recommendation**: Prioritize [List high-priority IDs] for full body development in consultancy dialogue.

---

### C. E-OID Candidates (Issues/Risks/Notes)

<!-- PURPOSE: Catalog operational items revealed by research. Per T102-ADR-007, Issues require resolution, Risks need mitigation, Notes capture lightweight insights (≤200 words per T102-ADR-006-FR-008). -->

#### C.1 Issues (E-ISSUE-###)
<!-- PURPOSE: Problems that require resolution before or during epic execution -->

| Candidate ID | Title | Research Source | Priority | Description | Resolution Approach |
|:-------------|:------|:----------------|:---------|:------------|:--------------------|
| E-ISSUE-001 | [Issue title - what needs resolution] | [Topic #.# or Section reference] | [H/M/L] | [What the issue is] | [How to resolve] |
| E-ISSUE-002 | [Issue title] | [Research source] | [H/M/L] | [Issue description] | [Resolution approach] |
| E-ISSUE-003 | [Issue title] | [Research source] | [H/M/L] | [Issue description] | [Resolution approach] |

**Total Candidates**: [#]
**Critical Issues**: [List any HIGH priority issue IDs that block progress]

---

#### C.2 Risks (E-RISK-###)
<!-- PURPOSE: Potential problems that may occur and require mitigation strategies -->

| Candidate ID | Title | Research Source | Priority | Severity | Likelihood | Mitigation Approach |
|:-------------|:------|:----------------|:---------|:---------|:-----------|:--------------------|
| E-RISK-001 | [Risk title - what might go wrong] | [Section IV.C or Topic reference] | [H/M/L] | [H/M/L] | [H/M/L] | [How to mitigate] |
| E-RISK-002 | [Risk title] | [Research source] | [H/M/L] | [H/M/L] | [H/M/L] | [Mitigation approach] |
| E-RISK-003 | [Risk title] | [Research source] | [H/M/L] | [H/M/L] | [H/M/L] | [Mitigation approach] |

**Total Candidates**: [#]
**Critical Risks**: [List any HIGH severity/likelihood risk IDs requiring immediate attention]

---

#### C.3 Notes (E-NOTE-###)
<!-- PURPOSE: Lightweight insights that don't fit other categories. Per T102-ADR-006-FR-008, Notes must be ≤200 words and capture observations, opportunities, or contextual information. -->

| Candidate ID | Title | Research Source | Content Summary (≤200 words) |
|:-------------|:------|:----------------|:-----------------------------|
| E-NOTE-001 | [Note title - insight captured] | [Section IV.C or Topic reference] | [Brief insight/observation from research - keep ≤200 words] |
| E-NOTE-002 | [Note title] | [Research source] | [Insight content ≤200 words] |
| E-NOTE-003 | [Note title] | [Research source] | [Insight content ≤200 words] |

**Total Candidates**: [#]
**High-Value Notes**: [List note IDs that capture particularly valuable opportunities or insights]

---

### D. E-ID Candidate Summary

<!-- PURPOSE: Provide aggregate view of all E-ID candidates for quick reference -->

| Category | Candidate Count | High Priority | Medium Priority | Low Priority |
|:---------|:----------------|:--------------|:----------------|:-------------|
| E-ASSUM | [#] | [#] | [#] | [#] |
| E-CON | [#] | [#] | [#] | [#] |
| E-QG | [#] | [#] | [#] | [#] |
| E-DEP | [#] | [#] | [#] | [#] |
| E-IF | [#] | [#] | [#] | [#] |
| E-IG | [#] | [#] | [#] | [#] |
| E-GDR | [#] | [#] | [#] | [#] |
| E-ADR | [#] | [#] | [#] | [#] |
| E-ISSUE | [#] | [#] | [#] | [#] |
| E-RISK | [#] | [#] | [#] | [#] |
| E-NOTE | [#] | [#] | [#] | [#] |
| **TOTAL** | **[#]** | **[#]** | **[#]** | **[#]** |

---

## VI. CONSULTANT RECOMMENDATIONS
<!-- PURPOSE: Synthesize analysis into clear, prioritized recommendations for action. This section guides the consultant's next steps and shapes how analysis insights are integrated into the proposal and plan. -->

### A. Priority Actions
<!-- PURPOSE: Define specific, actionable recommendations with clear ownership and timing -->

**Recommendation 1: [RECOMMENDATION TITLE]** (Priority: HIGH)
- **Context**: [Why this is needed - reference research findings]
- **Action**: [What should be done - be specific and actionable]
- **Owner**: [Who should do it - LLM_Consultant, LLM_Planner, LLM_Developer, or Client]
- **Timing**: [When it should be done - IMMEDIATE / NEXT PHASE / BEFORE X / etc.]
- **Dependencies**: [What must happen first, if anything]
- **Success Criteria**: [How to know it's complete - measurable outcomes]
- **E-ID Impact**: [Which E-ID candidates this action affects]

**Recommendation 2: [RECOMMENDATION TITLE]** (Priority: HIGH)
- **Context**: [Why this is needed]
- **Action**: [What should be done]
- **Owner**: [Who should do it]
- **Timing**: [When]
- **Dependencies**: [Prerequisites]
- **Success Criteria**: [Completion criteria]
- **E-ID Impact**: [Affected candidates]

**Recommendation 3: [RECOMMENDATION TITLE]** (Priority: MEDIUM)
- **Context**: [Why this is needed]
- **Action**: [What should be done]
- **Owner**: [Who should do it]
- **Timing**: [When]
- **Dependencies**: [Prerequisites]
- **Success Criteria**: [Completion criteria]
- **E-ID Impact**: [Affected candidates]

**Recommendation 4: [RECOMMENDATION TITLE]** (Priority: MEDIUM)
- **Context**: [Why this is needed]
- **Action**: [What should be done]
- **Owner**: [Who should do it]
- **Timing**: [When]
- **Dependencies**: [Prerequisites]
- **Success Criteria**: [Completion criteria]
- **E-ID Impact**: [Affected candidates]

**Recommendation 5: [RECOMMENDATION TITLE]** (Priority: LOW)
- **Context**: [Why this is needed]
- **Action**: [What should be done]
- **Owner**: [Who should do it]
- **Timing**: [When]
- **Dependencies**: [Prerequisites]
- **Success Criteria**: [Completion criteria]
- **E-ID Impact**: [Affected candidates]

---

### B. Proposal Seeding Strategy
<!-- PURPOSE: Guide how this analysis should inform the proposal. This section provides explicit instructions for updating proposal Section II (CANDIDATE INVENTORY) and prioritizing full body development. -->

**Section II (CANDIDATE INVENTORY) Seeding**:
- Seed **[#] E-RID candidates** from Section V.A:
  - E-ASSUM: [List specific IDs or "all" - e.g., E-ASSUM-001, E-ASSUM-003]
  - E-CON: [List specific IDs]
  - E-QG: [List specific IDs]
  - E-DEP: [List specific IDs]
  - E-IF: [List specific IDs]
  - E-IG: [List specific IDs]

- Seed **[#] E-DID candidates** from Section V.B:
  - E-GDR: [List specific IDs]
  - E-ADR: [List specific IDs]

- Seed **[#] E-OID candidates** from Section V.C:
  - E-ISSUE: [List specific IDs]
  - E-RISK: [List specific IDs]
  - E-NOTE: [List specific IDs]

**Total Candidates to Seed**: [#]

---

**Section III-V (Full Bodies) Prioritization**:
<!-- PURPOSE: Identify which candidates should receive full body treatment immediately vs. defer to consultancy dialogue -->

**Immediate Full Body Development** (Priority: HIGH):
- [E-ID-001]: [Title] — [Why full body is needed now]
- [E-ID-002]: [Title] — [Why full body is needed now]
- [E-ID-003]: [Title] — [Why full body is needed now]

**Defer to Consultancy Dialogue** (Requires Socratic Development):
- [E-ID-004]: [Title] — [Why this needs dialogue - e.g., requires client input, complex tradeoffs, etc.]
- [E-ID-005]: [Title] — [Why this needs dialogue]
- [E-ID-006]: [Title] — [Why this needs dialogue]

**Low Priority / Future Consideration**:
- [E-ID-007]: [Title] — [Why this can wait]
- [E-ID-008]: [Title] — [Why this can wait]

---

**Consultancy Dialogue Focus**:
<!-- PURPOSE: Guide the Socratic dialogue sequence for E-ID candidate development -->

**Start With**: [Which E-RID category to begin with - e.g., "E-ASSUM to establish foundational assumptions"]
**Rationale**: [Why start here based on research findings]

**Dialogue Sequence**:
1. **Phase 1**: [Category] — [Focus topic] — [Why this order]
2. **Phase 2**: [Category] — [Focus topic] — [Why this follows]
3. **Phase 3**: [Category] — [Focus topic] — [Why this follows]

**Key Discussion Points**:
- [Point 1: Specific topic requiring Socratic dialogue and why]
- [Point 2: Specific topic requiring Socratic dialogue and why]
- [Point 3: Specific topic requiring Socratic dialogue and why]

**Questions to Prepare**:
- [Question 1 to explore with client during consultancy]
- [Question 2 to explore with client during consultancy]
- [Question 3 to explore with client during consultancy]

---

### C. Phase Plan Adjustments
<!-- PURPOSE: Recommend any changes to the phase plan based on research findings. Research may reveal that planned activities are insufficient, unnecessary, or need reordering. -->

**Overall Assessment**: [Does research support current plan structure? ALIGNED / MINOR ADJUSTMENTS / MAJOR REVISION NEEDED]

---

**Subphase Modifications**:

**Subphase [#.X]: [Current Subphase Name]**
- **Recommended Change**: [Keep as-is / Rename to [...] / Split into [...] / Merge with [...] / Remove]
- **Rationale**: [Why this change based on research findings]
- **Impact**: [How this affects timeline/dependencies]

**Subphase [#.Y]: [Current Subphase Name]**
- **Recommended Change**: [Modification]
- **Rationale**: [Why based on research]
- **Impact**: [Effect on plan]

---

**Activity Additions**:

**Add Activity**: [New Activity Name] (to Subphase [#.X])
- **Description**: [What this activity entails]
- **Justification**: [Why research reveals this is needed]
- **Effort Estimate**: [Time/resource estimate]
- **Dependencies**: [What must come before]
- **Deliverable**: [What this produces]

**Add Activity**: [New Activity Name] (to Subphase [#.Y])
- **Description**: [Activity details]
- **Justification**: [Why needed per research]
- **Effort Estimate**: [Estimate]
- **Dependencies**: [Prerequisites]
- **Deliverable**: [Output]

---

**Activity Removals**:

**Remove Activity**: [Activity Name] (from Subphase [#.Z])
- **Current Purpose**: [What this activity was meant to do]
- **Justification**: [Why research shows this is unnecessary/redundant]
- **Alternative**: [What replaces this, if anything]

---

**Activity Reordering**:

**Move Activity**: [Activity Name]
- **Current Position**: Subphase [#.A]
- **New Position**: Subphase [#.B]
- **Rationale**: [Why research suggests different sequencing]
- **Dependency Impact**: [How this affects other activities]

---

**Success Criteria Updates**:

**Subphase [#.X] Success Criteria**:
- **Add Criterion**: [New success criterion] — [Why research reveals this is needed]
- **Modify Criterion**: [Current criterion] → [Modified criterion] — [Why change based on research]
- **Remove Criterion**: [Criterion to remove] — [Why research shows this is not relevant]

**Subphase [#.Y] Success Criteria**:
- **Add Criterion**: [New criterion and rationale]
- **Modify Criterion**: [Change and rationale]
- **Remove Criterion**: [Removal and rationale]

---

**Risk Register Updates**:
<!-- PURPOSE: Recommend additions to plan risk register based on research-identified risks -->

**Add to Plan Risks**:
- [E-RISK-###]: [Risk title] — [Why this should be in plan risk register]
- [E-RISK-###]: [Risk title] — [Why this should be in plan risk register]

---

## VII. INTEGRATION ROADMAP
<!-- PURPOSE: Provide step-by-step guidance for integrating this analysis into proposal, plan, and consultancy workflow. This section ensures analysis insights are systematically incorporated. -->

### Step 1: Proposal Update
<!-- PURPOSE: Seed proposal CANDIDATE INVENTORY and update frontmatter -->

**Action Checklist**:
- [ ] **Update Proposal Frontmatter**:
  - [ ] Add `research_analysis: [path to this analysis file]` to frontmatter
  - [ ] Update `version` if material changes
  - [ ] Update `date` to analysis completion date
  - [ ] Add `[RES-ID]` to `research_references` list

- [ ] **Seed Section II (CANDIDATE INVENTORY)**:
  - [ ] Add **[#] E-ASSUM candidates** from Section V.A.1
  - [ ] Add **[#] E-CON candidates** from Section V.A.2
  - [ ] Add **[#] E-QG candidates** from Section V.A.3
  - [ ] Add **[#] E-DEP candidates** from Section V.A.4
  - [ ] Add **[#] E-IF candidates** from Section V.A.5
  - [ ] Add **[#] E-IG candidates** from Section V.A.6
  - [ ] Add **[#] E-GDR candidates** from Section V.B.1
  - [ ] Add **[#] E-ADR candidates** from Section V.B.2
  - [ ] Add **[#] E-ISSUE candidates** from Section V.C.1
  - [ ] Add **[#] E-RISK candidates** from Section V.C.2
  - [ ] Add **[#] E-NOTE candidates** from Section V.C.3
  - [ ] **Total**: [#] candidates added to CANDIDATE INVENTORY

- [ ] **Update Section I (EXECUTIVE SUMMARY)** with research verdict:
  - [ ] Add research impact assessment
  - [ ] Update recommendation if analysis changes direction

- [ ] **Update Section VI.D (CHANGELOG)**:
  - [ ] Add entry: "[Version] [Date] Integrated [RES-ID] analysis with [#] E-ID candidates"

**Expected Outcome**: Proposal Section II populated with all E-ID candidates from this analysis, ready for Socratic dialogue and full body development.

---

### Step 2: Plan Review & Update
<!-- PURPOSE: Update phase plan based on Section VI.C recommendations -->

**Action Checklist**:
- [ ] **Review current plan** against Section VI.C recommendations
- [ ] **Apply subphase modifications**:
  - [ ] Implement subphase changes from Section VI.C
  - [ ] Update subphase descriptions as needed

- [ ] **Update activities**:
  - [ ] Add new activities identified in Section VI.C
  - [ ] Remove activities deemed unnecessary
  - [ ] Reorder activities per new sequencing
  - [ ] Update effort estimates if scope changed

- [ ] **Update success criteria**:
  - [ ] Add research-driven success criteria
  - [ ] Modify criteria per Section VI.C
  - [ ] Remove obsolete criteria

- [ ] **Update risk register**:
  - [ ] Add E-RISK candidates flagged in Section VI.C
  - [ ] Update mitigation strategies based on research

- [ ] **Update plan changelog**:
  - [ ] Document all plan adjustments with reference to [RES-ID]

**Expected Outcome**: Plan updated to reflect research insights, with activities and success criteria aligned to analysis recommendations.

---

### Step 3: Consultancy Preparation
<!-- PURPOSE: Prepare for Socratic dialogue with client based on Section VI.B -->

**Action Checklist**:
- [ ] **Review Section VI.B** (Consultancy Dialogue Focus)
- [ ] **Prepare dialogue sequence** per recommended order
- [ ] **Prepare opening questions** from Section VI.B "Questions to Prepare"
- [ ] **Identify discussion priorities**:
  - [ ] List E-ID candidates requiring client input
  - [ ] List E-ID candidates with complex tradeoffs
  - [ ] List E-ID candidates that need validation

- [ ] **Prepare evidence**:
  - [ ] Extract relevant research findings for reference during dialogue
  - [ ] Prepare examples/scenarios for Socratic questioning
  - [ ] Prepare alternative options for decision points

- [ ] **Review gaps/risks** from Section IV.B and IV.C:
  - [ ] Prepare questions to address gaps with client
  - [ ] Prepare risk mitigation discussion points

**Expected Outcome**: Consultant ready to engage client in Socratic dialogue with prepared questions, sequence, and supporting evidence.

---

### Step 4: Research Register Update
<!-- PURPOSE: Update epic research register to track this research and its integration -->

**Action Checklist**:
- [ ] **Add [RES-ID] to epic research register** with:
  - [ ] Research title and date
  - [ ] Link to research brief
  - [ ] Link to research report
  - [ ] Link to this analysis
  - [ ] Status: COMPLETE / INTEGRATED

- [ ] **Link research to E-ID candidates**:
  - [ ] Cross-reference [RES-ID] with all E-ID candidates in Section V
  - [ ] Enable traceability from candidates back to research

- [ ] **Update SPS if required**:
  - [ ] Add research findings to SPS Section II if they materially change problem framing
  - [ ] Update SPS changelog

- [ ] **Update Concept if required**:
  - [ ] Add research findings to Concept if they affect solution approach
  - [ ] Update Concept changelog

**Expected Outcome**: Research properly registered, linked, and integrated into epic knowledge base.

---

### Step 5: Verification
<!-- PURPOSE: Verify integration is complete and consistent -->

**Action Checklist**:
- [ ] **Verify proposal updates**:
  - [ ] All E-ID candidates from Section V appear in proposal Section II
  - [ ] Proposal frontmatter correctly references this analysis
  - [ ] Proposal changelog documents integration

- [ ] **Verify plan updates**:
  - [ ] All Section VI.C recommendations applied or explicitly deferred
  - [ ] Plan changelog documents adjustments

- [ ] **Verify traceability**:
  - [ ] Research → Analysis → E-ID Candidates → Proposal linkage complete
  - [ ] All E-ID candidates reference source research findings

- [ ] **Verify consultancy readiness**:
  - [ ] Dialogue sequence prepared
  - [ ] Questions prepared
  - [ ] Evidence organized

**Expected Outcome**: Complete integration with full traceability and readiness for next phase.

---

## VIII. APPENDICES

### A. Research Findings Cross-Reference
<!-- PURPOSE: Quick lookup table mapping research findings to analysis sections and E-ID candidates for traceability -->

| Finding ID | Finding Summary | Research Section | Analysis Section | E-ID Candidates Generated | Priority |
|:-----------|:----------------|:-----------------|:-----------------|:--------------------------|:---------|
| Finding 1 | [Brief summary of finding 1] | [Report section #] | [Section III.X] | [E-ASSUM-001, E-QG-002, E-NOTE-005] | [H/M/L] |
| Finding 2 | [Brief summary of finding 2] | [Report section #] | [Section III.Y] | [E-CON-001, E-RISK-003] | [H/M/L] |
| Finding 3 | [Brief summary of finding 3] | [Report section #] | [Section III.Z] | [E-DEP-001, E-IF-002] | [H/M/L] |
| Finding 4 | [Brief summary of finding 4] | [Report section #] | [Section IV.A] | [E-GDR-001, E-ADR-001] | [H/M/L] |
| Finding 5 | [Brief summary of finding 5] | [Report section #] | [Section IV.B] | [E-ISSUE-001] | [H/M/L] |

**Purpose**: Enable quick tracing from research findings → analysis → E-ID candidates.

---

### B. Assumptions & Limitations
<!-- PURPOSE: Document limitations of this analysis to set appropriate expectations and identify areas requiring additional research or validation -->

**Analysis Assumptions**:
- **Analysis Assumption 1**: [What was assumed during analysis - e.g., "Assumed current codebase state matches repository as of [date]"]
- **Analysis Assumption 2**: [What was assumed - e.g., "Assumed client requirements documented in [artifact] remain stable"]
- **Analysis Assumption 3**: [What was assumed - e.g., "Assumed research methodology was sound and findings are reliable"]

**Research Limitations**:
- **Research Limitation 1**: [What the research did not cover - e.g., "Research did not evaluate performance implications of approach X"]
- **Research Limitation 2**: [What was not covered - e.g., "Research scope excluded integration with system Y"]
- **Research Limitation 3**: [What was not covered - e.g., "Research did not include user testing or validation"]

**Consultant Limitations**:
- **Consultant Limitation 1**: [Where consultant expertise may be limited - e.g., "Limited domain expertise in [specific area] - client validation recommended"]
- **Consultant Limitation 2**: [Expertise limitation - e.g., "Analysis based on documentation only - hands-on experimentation not performed"]
- **Consultant Limitation 3**: [Expertise limitation - e.g., "No access to production environment - analysis based on development/staging"]

**Recommended Follow-Up**:
- [Follow-up action 1 to address limitations - e.g., "Commission additional research on performance implications"]
- [Follow-up action 2 to address limitations - e.g., "Validate findings with domain expert"]
- [Follow-up action 3 to address limitations - e.g., "Conduct prototype testing to verify assumptions"]

---

### C. Supporting Evidence
<!-- PURPOSE: Provide quick-reference supporting evidence for key claims in analysis -->

**Evidence for Key Claims**:

**Claim 1**: [Major claim from analysis - e.g., "Current architecture cannot support requirement X"]
- **Evidence**: [Research finding reference - e.g., "Report Section III.B shows..."]
- **Confidence**: [HIGH/MEDIUM/LOW]

**Claim 2**: [Major claim from analysis]
- **Evidence**: [Research finding reference]
- **Confidence**: [HIGH/MEDIUM/LOW]

**Claim 3**: [Major claim from analysis]
- **Evidence**: [Research finding reference]
- **Confidence**: [HIGH/MEDIUM/LOW]

---

### D. Open Questions
<!-- PURPOSE: Document questions that remain unanswered after research and analysis, requiring either additional research or client consultation -->

| Question | Context | Recommended Resolution Approach | Priority |
|:---------|:--------|:--------------------------------|:---------|
| [Question 1] | [Why this is important] | [How to resolve - e.g., "Client consultation" or "Commission RES-###"] | [H/M/L] |
| [Question 2] | [Why this is important] | [Resolution approach] | [H/M/L] |
| [Question 3] | [Why this is important] | [Resolution approach] | [H/M/L] |

---

## IX. CHANGELOG

<!-- PURPOSE: Track versions and changes to this analysis document -->

| Version | Date | Changes | Author |
|:--------|:-----|:--------|:-------|
| 1.0.0 | YYYY-MM-DD | Initial analysis of [RES-ID] report | LLM_Consultant |
| 1.1.0 | YYYY-MM-DD | [Description of changes if revised] | LLM_Consultant |

---

## X. METADATA

<!-- PURPOSE: Provide structured metadata for tooling and automation -->

**Analysis Statistics**:
- Total Research Findings Analyzed: [#]
- Total E-ID Candidates Generated: [#]
- Total Recommendations: [#]
- Analysis Duration: [Time spent on analysis]
- Research Report Pages: [#]

**Traceability Links**:
- Research Brief: [path]
- Research Report: [path]
- Target Proposal: [path]
- Target Plan: [path]
- Related SPS: [path]
- Related Concept: [path]

**Quality Checklist**:
- [ ] All research findings mapped to analysis sections
- [ ] All E-ID candidates include research source reference
- [ ] All recommendations include priority/owner/timing
- [ ] Integration roadmap is actionable
- [ ] Cross-references are valid
- [ ] Changelog updated

---

**END OF ANALYSIS**
