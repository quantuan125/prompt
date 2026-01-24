---
artifact_type: 'NOTES'
initiative_id: '[INITIATIVE_ID]'
epic_id: '[EPIC_ID]'
epic_code: '[EPIC_CODE]'
phase: '[PHASE_NUMBER]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
plan_reference: '[path/to/plan_file.md]'
proposal_reference: '[path/to/proposal_file.md]'
---

# PHASE NOTES: [Epic ID] Phase [#] — [Phase Title]

<!--
PURPOSE: This LOG serves as a hybrid Decision Log + Meeting Minutes for phase consultancy.
It captures both narrative flow (what happened, how consensus emerged) and structured
decisions (what was decided, why, by whom). This dual approach supports:
1. Continuity: Next-activity guidance for session resumption
2. Training: Process improvements and patterns for future consultations
3. Traceability: Clear decision lineage tied to E-RIDs/E-DIDs
4. Compliance: Industry-standard decision log format (PMI/PRINCE2)
5. Knowledge Management: NOTE candidates for SPS promotion

USAGE GUIDANCE:
- Create one LOG per phase of consultancy
- Update incrementally as subphases complete
- Each subphase gets one complete section (A-D)
- Decisions table grows with each subphase
- NOTE candidates surface as insights emerge naturally from dialogue
- Use this for training data and process refinement

HYBRID NATURE:
This template intentionally combines two industry-standard formats:
1. MINUTES OF MEETINGS (Narrative): Captures discussion flow, context, and consensus-building
2. DECISION LOG (Structured): Records decisions with traceability per PMI/PRINCE2 standards

This combination ensures both qualitative context (training value) and quantitative
traceability (audit/compliance value).
-->

## I. LOG SUMMARY
<!--
PURPOSE: High-level overview of the entire phase log for quick reference.
This section provides executives and stakeholders with fast insight into phase outcomes.
Update this section last, after all subphases are complete or when phase status changes.

WRITING TIPS:
- Keep outcome statements specific and measurable (not vague achievements)
- Focus on deliverables and major milestones (not activities)
- Update status as phase progresses (In Progress → Complete)
- Use this section for executive briefings and status reports
-->

**Phase**: [PHASE_NUMBER] ([Phase Title - e.g., "Foundation & Planning"])
**Subphases**: [List all subphase IDs and titles, e.g., "0.1 Research Commissioning, 0.2 E-RID Definition, 0.3 E-DID Scoping, 0.4 Gate A Approval"]
**Status**: [In Progress / Complete]
**Date Range**: YYYY-MM-DD to YYYY-MM-DD

**Key Outcomes**:
<!-- List 3-5 major achievements from this phase -->
- [Outcome 1 - e.g., "Commissioned 3 internal research initiatives (T102B-RES-001, T102B-RES-002, T102B-RES-003)"]
- [Outcome 2 - e.g., "Defined 12 Epic Requirements (E-RID-001 through E-RID-012) covering governance scope"]
- [Outcome 3 - e.g., "Achieved Gate A approval with client sign-off on epic foundation"]

**Major Decisions**: [Count] decisions made across [Count] subphases
<!-- Example: "14 decisions made across 4 subphases" -->

---

## II. SUBPHASE RECORDS
<!--
PURPOSE: Chronological record of all subphase consultancy activities.
Each subphase gets ONE complete section with structure A-D.

GUIDANCE:
- Document subphases in chronological order
- Complete A-D for each subphase before moving to next
- Narrative Summary (A) should read like meeting minutes
- Decisions Made (B) should follow structured decision log format
- Improvements & Observations (C) feed continuous improvement
- Next-Activity Guidance (D) ensures smooth continuation

WHEN TO CREATE NEW SUBPHASE SECTION:
- When PLAN defines a new subphase (e.g., 0.1 → 0.2)
- When consultation dialogue naturally shifts to new major activity
- When previous subphase reaches logical completion point

REPEATABLE PATTERN:
This section shows 4 subphases as a pattern. Epics may have fewer or more subphases.
Copy the structure and adapt to your phase's actual subphase count.
-->

### Subphase [#.1]: [SUBPHASE TITLE]
<!-- EXAMPLE: "Subphase 0.1: Research Commissioning & Scoping" -->

**Date Range**: YYYY-MM-DD to YYYY-MM-DD
**Status**: [In Progress / Complete]
**Participants**: LLM_Consultant, Client, [other roles if applicable]

#### A. Narrative Summary
<!--
PURPOSE: Capture what the discussion was about, context, and flow (Minutes of Meetings style).
This narrative helps with:
- Training: Understanding how consultations typically progress
- Continuity: Context for future sessions
- Process Improvement: Identifying bottlenecks or friction points
- Knowledge Transfer: Documenting tacit knowledge and decision context

STRUCTURE: Write 2-4 paragraphs covering:
1. Context and objectives: What was this subphase about? What were we trying to achieve?
2. Key topics explored: What questions were discussed? What options were considered?
3. Consensus and decisions: How did we reach agreement? What framework guided decisions?
4. Challenges and resolution: What obstacles arose? How were they addressed?

TONE: Professional but natural, as if writing meeting minutes. Capture the "story" of the consultation.

EXAMPLE:
"This subphase focused on commissioning internal research to establish the epic foundation.
The client identified that existing codebase documentation was insufficient for high-quality
E-RID definition. We discussed the difference between external research (industry standards,
best practices) and internal research (codebase analysis, implementation realities).

During consultation, we explored three research areas: (1) current artifact dependencies,
(2) existing governance implementation, and (3) ADR skills system architecture. The client
expressed concern about research scope creep. We established clear research boundaries using
the RES-BRIEF template with explicit success criteria.

Consensus emerged that internal research should precede E-RID definition to ground requirements
in implementation reality rather than abstract theory. This decision was formalized as DEC-0.1-001.
We commissioned T102B-RES-002 for artifact dependency analysis with a 5-day turnaround.

The main challenge was balancing research depth with timeline constraints. We resolved this by
prioritizing 'implementation blockers' over 'nice to know' analysis, documenting this heuristic
as NOTE-001-Candidate for future research scoping guidance."
-->

[Paragraph 1: Context and objectives for this subphase]
<!-- What was the subphase about? What were we trying to achieve? What was the starting state? -->

[Paragraph 2: Key topics explored during consultation]
<!-- What questions were discussed? What options were considered? What framework guided exploration? -->

[Paragraph 3: How consensus was reached and what was decided]
<!-- How did agreement emerge? What was the pivotal insight or framework? What was decided? -->

[Paragraph 4: Any challenges encountered and how they were addressed]
<!-- What obstacles arose? How were they resolved? What trade-offs were made? -->

---

#### B. Decisions Made
<!--
PURPOSE: Structured decision log per industry standards (PMI PMBOK, PRINCE2).
Each decision gets one row with clear traceability and rationale.

DECISION LOG FORMAT (per PMI Decision Log best practices):
- DEC-ID: Unique identifier (DEC-[Phase.Subphase]-[###])
- Decision: Clear statement of what was decided (actionable, specific)
- Rationale: Why this decision was made (context, trade-offs, criteria)
- Owner: Who owns execution/implementation of this decision
- Related IDs: Traceability to E-RIDs, E-DIDs, RES briefs, or other artifacts
- Date: When decision was made

GUIDANCE:
- Use DEC-ID format: DEC-[Phase.Subphase]-[###] (e.g., DEC-0.1-001, DEC-0.1-002)
- Decision should be actionable ("Commission research" not "Research is needed")
- Rationale should capture WHY (trade-offs, criteria, context)
- Owner is typically "Client" (their epic), "LLM_Consultant" (process decisions), or specific role
- Related IDs provide traceability (E-RID-###, T102B-RES-###, etc.)
- Date format: YYYY-MM-DD

EXAMPLES OF GOOD DECISIONS:
✓ "Commission T102B-RES-002 for artifact dependency analysis"
✓ "Adopt T102-ADR-006 NOTE-ID structure for SPS documentation"
✓ "Defer E-RID-008 priority ranking to Phase 1 after research completion"

EXAMPLES OF POOR DECISIONS:
✗ "Research is important" (not actionable)
✗ "We should do better" (vague, no specificity)
✗ "Fix the problem" (no clear scope or ownership)
-->

| DEC-ID | Decision | Rationale | Owner | Related IDs | Date |
|:-------|:---------|:----------|:------|:------------|:-----|
| DEC-[#.1]-001 | [Clear, actionable decision statement] | [Why this was chosen: context, trade-offs, criteria] | [Owner role] | [E-RID/E-DID/RES-ID] | YYYY-MM-DD |
| DEC-[#.1]-002 | [Clear, actionable decision statement] | [Why this was chosen: context, trade-offs, criteria] | [Owner role] | [E-RID/E-DID/RES-ID] | YYYY-MM-DD |

<!--
DETAILED EXAMPLES:

| DEC-ID | Decision | Rationale | Owner | Related IDs | Date |
|:-------|:---------|:----------|:------|:------------|:-----|
| DEC-0.1-001 | Commission T102B-RES-002 for internal artifact dependency analysis | Existing codebase documentation insufficient for E-RID definition; internal research reveals implementation realities that external standards cannot capture | Client | T102B-RES-002, E-RID-001 | 2025-01-15 |
| DEC-0.1-002 | Prioritize "implementation blockers" over "nice to know" analysis in research scope | Timeline constraints require focus; blockers prevent progress while nice-to-know items provide marginal value | LLM_Consultant | T102B-RES-002, T102B-RES-003 | 2025-01-15 |
| DEC-0.2-003 | Adopt MOSCOW prioritization for E-RID classification | Client familiar with MOSCOW; provides clear Must/Should/Could/Won't boundaries for scope management | Client | E-RID-001 through E-RID-012 | 2025-01-17 |
-->

---

#### C. Improvements & Observations
<!--
PURPOSE: Identify process improvements, patterns, and lessons learned.
This section feeds continuous improvement and training data for future consultations.

STRUCTURE:
- Process Improvements: What could be done better in the consultancy workflow?
- Patterns Observed: Reusable insights about how consultations typically progress
- Lessons Learned: What we learned for future similar situations

GUIDANCE:
- Be specific and actionable (not vague or generic)
- Focus on process/methodology (not just content outcomes)
- Think about future consultations: what would help them succeed faster?
- Look for patterns that might apply across epics/initiatives

EXAMPLES:

Process Improvements:
- "RES-BRIEF template should include 'Anti-Goals' section to prevent scope creep during research commissioning"
- "Decision log should be updated in real-time during consultation (not batched at end) to capture rationale while fresh"
- "Gate criteria should be socialized earlier in phase to avoid last-minute rework"

Patterns Observed:
- "Clients often conflate requirements (WHAT) with design (HOW) during E-RID definition; consultant must redirect to requirement level"
- "Internal research consistently produces higher-quality E-RID candidates than external research alone"
- "Research commissioning typically takes 2-3 iterations to achieve clarity on scope boundaries"

Lessons Learned:
- "When client resists research commissioning due to timeline pressure, frame research as 'risk reduction' rather than 'extra work'"
- "Narrative Summary should be drafted immediately after consultation while context is fresh (not days later)"
- "NOTE candidates surface most naturally during consensus-building dialogue (capture them in real-time)"
-->

**Process Improvements**:
<!-- What could be done better in the consultancy process/workflow? -->
- [Improvement observation 1: specific, actionable change to process]
- [Improvement observation 2: specific, actionable change to process]

**Patterns Observed**:
<!-- Reusable insights about how consultations typically progress -->
- [Pattern 1: reusable insight about consultancy dynamics, applicable to future engagements]
- [Pattern 2: reusable insight about consultancy dynamics, applicable to future engagements]

**Lessons Learned**:
<!-- What we learned for future similar situations -->
- [Lesson 1: specific learning with context about when/how to apply it]
- [Lesson 2: specific learning with context about when/how to apply it]

---

#### D. Next-Activity Guidance
<!--
PURPOSE: Ensure smooth continuation when consultation resumes (next subphase or future session).
This section answers: "If I had to hand this off to another consultant RIGHT NOW, what would they need to know?"

STRUCTURE:
- Carry-Forward Items: Incomplete work, unresolved questions, deferred decisions
- Recommended Starting Point: Explicit guidance for next session

GUIDANCE:
- Be ultra-specific: name exact artifacts, sections, line numbers if possible
- Identify prerequisites: what must be ready before next activity can start?
- Flag blockers: what could prevent progress in next activity?
- Reference decision log: tie carry-forward items to DEC-IDs where applicable

CARRY-FORWARD ITEMS FORMAT:
- [Item description] → [Destination: where it should be resolved]

EXAMPLES:

Carry-Forward Items:
- "E-RID-008 priority ranking incomplete (MOSCOW not assigned)" → Subphase 0.3
- "Open question: Should NOTE-IDs support versioning like E-RIDs?" → OQ-007 in issues register
- "Research T102B-RES-002 commissioned but not complete" → Expected completion 2025-01-20
- "Gate A criteria draft exists but not socialized with client" → DEC-0.4-001 deferred approval to 2025-01-21

Recommended Starting Point:
"When resuming, begin by reviewing T102B-RES-002 research report (expected 2025-01-20).
The next major activity is E-RID definition (Subphase 0.2), which requires completed research
findings as prerequisite. Open the SPS file and prepare to translate research findings into
formal E-RID entries using the T102-ADR-005 ID specification format. Client should have
2-hour block available for interactive E-RID definition session."
-->

**Carry-Forward Items**:
<!-- List incomplete items, unresolved questions, deferred decisions with clear destination -->
- [Item 1: incomplete item with specific detail] → [Destination: Subphase #.X / OQ-### / specific artifact]
- [Item 2: unresolved question requiring decision] → [Destination: Open Question OQ-### / Decision needed]
- [Item 3: deferred decision with rationale] → [Destination: When/where it should be resolved]

**Recommended Starting Point**:
<!-- Explicit guidance for next session: where to start, what to review, what prerequisites are needed -->
[Guidance paragraph: "When resuming, begin by [specific action]. The next major activity is [activity description] which requires [prerequisites]. [Additional context or preparation needed]."]

<!-- EXAMPLE:
"When resuming, begin by reviewing the completed T102B-RES-002 research report located at
prompt/artifacts/tasks/T102/research/report/report_T102B-RES-002_artifact-dependencies.md.
The next major activity is E-RID definition (Subphase 0.2), which requires understanding the
artifact dependency map produced by research. Prepare the SPS file for E-RID entry and allocate
a 2-hour focused session with the client for interactive requirement definition. Client should
review research findings before session to maximize efficiency."
-->

---

### Subphase [#.2]: [SUBPHASE TITLE]
<!--
GUIDANCE: Repeat the same A-D structure for each subsequent subphase.
Copy the template structure from Subphase #.1 and fill in specifics.

EXAMPLE: "Subphase 0.2: E-RID Definition & Prioritization"
-->

**Date Range**: YYYY-MM-DD to YYYY-MM-DD
**Status**: [In Progress / Complete]
**Participants**: LLM_Consultant, Client, [other roles if applicable]

#### A. Narrative Summary

[Paragraph 1: Context and objectives for this subphase]

[Paragraph 2: Key topics explored during consultation]

[Paragraph 3: How consensus was reached and what was decided]

[Paragraph 4: Any challenges encountered and how they were addressed]

---

#### B. Decisions Made

| DEC-ID | Decision | Rationale | Owner | Related IDs | Date |
|:-------|:---------|:----------|:------|:------------|:-----|
| DEC-[#.2]-001 | [Clear, actionable decision statement] | [Why this was chosen: context, trade-offs, criteria] | [Owner role] | [E-RID/E-DID/RES-ID] | YYYY-MM-DD |
| DEC-[#.2]-002 | [Clear, actionable decision statement] | [Why this was chosen: context, trade-offs, criteria] | [Owner role] | [E-RID/E-DID/RES-ID] | YYYY-MM-DD |

---

#### C. Improvements & Observations

**Process Improvements**:
- [Improvement observation 1]
- [Improvement observation 2]

**Patterns Observed**:
- [Pattern 1]
- [Pattern 2]

**Lessons Learned**:
- [Lesson 1]
- [Lesson 2]

---

#### D. Next-Activity Guidance

**Carry-Forward Items**:
- [Item 1] → [Destination]
- [Item 2] → [Destination]
- [Item 3] → [Destination]

**Recommended Starting Point**:
[Guidance for next session]

---

### Subphase [#.3]: [SUBPHASE TITLE]
<!-- Repeat structure A-D -->

**Date Range**: YYYY-MM-DD to YYYY-MM-DD
**Status**: [In Progress / Complete]
**Participants**: LLM_Consultant, Client, [other roles if applicable]

#### A. Narrative Summary

[Paragraphs 1-4]

---

#### B. Decisions Made

| DEC-ID | Decision | Rationale | Owner | Related IDs | Date |
|:-------|:---------|:----------|:------|:------------|:-----|
| DEC-[#.3]-001 | [Decision] | [Rationale] | [Owner] | [IDs] | YYYY-MM-DD |

---

#### C. Improvements & Observations

**Process Improvements**:
- [Improvements]

**Patterns Observed**:
- [Patterns]

**Lessons Learned**:
- [Lessons]

---

#### D. Next-Activity Guidance

**Carry-Forward Items**:
- [Items → Destinations]

**Recommended Starting Point**:
[Guidance]

---

### Subphase [#.4]: [SUBPHASE TITLE]
<!-- Repeat structure A-D -->

**Date Range**: YYYY-MM-DD to YYYY-MM-DD
**Status**: [In Progress / Complete]
**Participants**: LLM_Consultant, Client, [other roles if applicable]

#### A. Narrative Summary

[Paragraphs 1-4]

---

#### B. Decisions Made

| DEC-ID | Decision | Rationale | Owner | Related IDs | Date |
|:-------|:---------|:----------|:------|:------------|:-----|
| DEC-[#.4]-001 | [Decision] | [Rationale] | [Owner] | [IDs] | YYYY-MM-DD |

---

#### C. Improvements & Observations

**Process Improvements**:
- [Improvements]

**Patterns Observed**:
- [Patterns]

**Lessons Learned**:
- [Lessons]

---

#### D. Next-Activity Guidance

**Carry-Forward Items**:
- [Items → Destinations]

**Recommended Starting Point**:
[Guidance]

---

## III. NOTE CANDIDATES (T102-ADR-006-FR-008)
<!--
PURPOSE: Lightweight insights (≤200 words) extracted from consultation dialogue for potential
promotion to SPS NOTE-IDs. Per T102-ADR-006-FR-008, NOTEs capture:
- Contextual clarifications
- Philosophy and approach guidance
- Industry references and best practices
- Early observations that don't yet warrant formal requirements

NOT FOR:
- Commissioned research (use RES artifacts)
- Enforceable rules (use GDR/ADR)
- Formal requirements (use E-RID)
- Detailed specifications (use E-DID)

GUIDANCE:
- NOTEs emerge naturally during consultation dialogue
- Capture them in real-time as insights surface
- Keep summaries ≤200 words (lean toward 100-150 words)
- Decide promotion based on reusability across epics/initiatives
- If unsure about promotion, default to YES (easy to archive later)

PROMOTION CRITERIA:
YES if:
- Insight applies across multiple epics/initiatives
- Captures tacit knowledge that would otherwise be lost
- Provides guidance for future similar situations
- Clarifies philosophy or approach (the "why" behind decisions)

NO if:
- Insight is specific to this epic only
- Already documented elsewhere (avoid duplication)
- Too tactical/detailed (belongs in implementation docs)
- Obvious or common knowledge

EXAMPLES:

| Candidate | Subphase | Content Summary (≤200 words) | Promote to SPS? | Rationale |
|:----------|:---------|:-----------------------------|:----------------|:----------|
| NOTE-001-Candidate | 0.1 | Internal research (codebase analysis) consistently produces higher-quality E-RID candidates than external research (industry standards) alone. External research provides theoretical frameworks and best practices, but internal research reveals implementation realities, constraints, and opportunities that external sources cannot capture. When scoping epic foundations, prioritize internal research for "what exists" and "what's possible," then use external research to validate against industry standards. This pattern should inform research commissioning strategy for all future epic initialization phases. | YES | Reusable pattern for all epic foundation phases; captures tacit knowledge about research strategy |
| NOTE-002-Candidate | 0.2 | During E-RID definition, clients often conflate requirements (WHAT must be achieved) with design (HOW it will be achieved). The consultant's role is to redirect focus to requirement level, deferring design to later phases. Use the question "What problem are you solving?" to refocus on requirements when client drifts into solution space. This heuristic helps maintain proper separation of concerns across SDLC phases. | YES | Applies to all consultancy engagements; provides concrete heuristic for common challenge |
| NOTE-003-Candidate | 0.3 | We decided to use MOSCOW prioritization for this epic because the client was already familiar with it from previous projects. | NO | Epic-specific context; no reusable insight for other engagements |
-->

| Candidate | Subphase | Content Summary (≤200 words) | Promote to SPS? | Rationale |
|:----------|:---------|:-----------------------------|:----------------|:----------|
| NOTE-001-Candidate | [#.#] | [Insight summary: contextual clarification, philosophy, pattern, or observation that emerged during consultation dialogue. Keep this ≤200 words, ideally 100-150 words. Focus on the "why" and "when" more than the "what."] | [YES/NO] | [Why promote or not: reusability, uniqueness, value across initiatives] |
| NOTE-002-Candidate | [#.#] | [Insight summary] | [YES/NO] | [Rationale] |
| NOTE-003-Candidate | [#.#] | [Insight summary] | [YES/NO] | [Rationale] |

<!--
DETAILED EXAMPLE WITH CONTEXT:

During Subphase 0.1 (Research Commissioning), the following insight emerged naturally:

DIALOGUE CONTEXT:
Client: "Why can't we just use industry best practices from PMI for governance requirements?"
Consultant: "We can reference PMI for validation, but we need internal research first."
Client: "Why? Won't that slow us down?"
Consultant: "Your codebase has 4 years of accumulated patterns and constraints. PMI doesn't know about your artifact structure, your existing ADR system, or your specific workflow tools. If we define requirements purely from external standards, we'll create an 'ideal world' spec that might be impossible or inefficient to implement in your actual codebase. Internal research grounds requirements in reality."
Client: "Ah, so internal research reveals what's possible, external research validates what's right?"
Consultant: "Exactly. Internal first (what exists, what's possible), external second (what's standard, what's recommended)."

This produced NOTE-001-Candidate:
| NOTE-001-Candidate | 0.1 | Internal research (codebase analysis) consistently produces higher-quality E-RID candidates than external research (industry standards) alone. External research provides theoretical frameworks and best practices, but internal research reveals implementation realities, constraints, and opportunities that external sources cannot capture. When scoping epic foundations, prioritize internal research for "what exists" and "what's possible," then use external research to validate against industry standards. This pattern should inform research commissioning strategy for all future epic initialization phases. | YES | Reusable pattern for all epic foundation phases; captures tacit knowledge about research strategy that isn't documented elsewhere |
-->

---

## IV. CROSS-PHASE CONTINUITY
<!--
PURPOSE: Training data and historical context for future consultations.
This section helps LLM_Consultant improve over time by capturing:
- Reusable patterns that emerged during this phase
- Process improvements for the consultancy methodology
- Training notes for future consultant instances
- Quantitative metrics for process analysis

Update this section when phase completes (or periodically for long phases).
-->

### A. Key Patterns Observed
<!--
PURPOSE: Document reusable patterns that emerged during this phase.
These patterns should be broadly applicable, not phase-specific tactical details.

GUIDANCE:
- Focus on patterns in HOW consultation progresses (not just WHAT was delivered)
- Include when/how to recognize the pattern in future consultations
- Provide guidance on how to respond when pattern is observed

EXAMPLES:
- **Research Scope Creep Pattern**: During research commissioning, scope tends to expand
  without clear boundaries. This pattern manifests when client says "while we're at it,
  let's also analyze..." Respond by documenting scope expansions as separate RES briefs
  rather than expanding existing brief. This maintains clarity and prevents timeline drift.

- **E-RID vs E-DID Confusion Pattern**: Clients often conflate requirements (E-RID) with
  design (E-DID) during foundation phase. Pattern manifests when client describes "how"
  before "what". Respond with question: "What problem are you solving?" to redirect to
  requirement level. Once requirement is clear, note design ideas as E-DID candidates for
  later phases.

- **Gate Criteria Surprise Pattern**: Gate approval often delayed when criteria are
  introduced at gate time rather than socialized early. Pattern manifests as last-minute
  rework or client resistance. Respond by introducing gate criteria in first subphase of
  phase, even if gate is several subphases away. This allows gradual alignment.
-->

- **[Pattern Name]**: [Description of pattern: what it is, when it typically appears, how to recognize it, and how to respond when observed. Include specific examples if possible.]
- **[Pattern Name]**: [Description of pattern with recognition cues and response guidance]
- **[Pattern Name]**: [Description of pattern with recognition cues and response guidance]

---

### B. Process Improvement Recommendations
<!--
PURPOSE: Concrete, actionable recommendations for improving the consultancy process itself.
These should be specific enough that a future consultant could implement them immediately.

GUIDANCE:
- Focus on process/methodology improvements (not content improvements)
- Be specific: name exact artifacts, templates, sections to change
- Explain WHAT to change and WHY it would help
- Prioritize improvements that would have saved significant time/friction

EXAMPLES:
- **Add "Anti-Goals" Section to RES-BRIEF Template**: Research commissioning revealed that
  scope creep occurs when what's OUT of scope is unclear. Adding explicit "Anti-Goals"
  section to RES-BRIEF template (Section IV) would prevent scope expansion by making
  boundaries visible upfront. Estimated time savings: 30-60 minutes per research commissioning
  session due to reduced scope negotiation.

- **Update Decision Log in Real-Time**: Current practice documents decisions at end of subphase.
  This causes rationale loss because context fades. Recommendation: Update decision log during
  consultation dialogue as decisions are made. This requires keeping LOG file open during
  consultation session. Benefit: Richer rationale capture, reduced reconstruction effort.

- **Socialize Gate Criteria Earlier**: Gate A criteria introduced in Subphase 0.4 caused
  last-minute rework. Recommendation: Introduce gate criteria in Subphase 0.1 (first subphase
  of phase) even though gate is later. This allows gradual alignment and reduces surprise.
  Reference gate criteria in each subphase to maintain visibility.
-->

- **[Recommendation Title]**: [WHAT should change in the process, WHERE it should change (specific artifact/template/section), WHY it would help (benefits, time savings, friction reduction), and HOW to implement it]
- **[Recommendation Title]**: [Specific, actionable recommendation with context]
- **[Recommendation Title]**: [Specific, actionable recommendation with context]

---

### C. Training Notes
<!--
PURPOSE: Guidance for future LLM_Consultant instances executing similar phases.
These are lessons learned that would help future consultants succeed faster.

GUIDANCE:
- Write as if mentoring a junior consultant
- Focus on non-obvious insights (not basic process steps)
- Include situational awareness: "watch for X, which signals Y"
- Provide decision heuristics: "when X happens, consider Y"

EXAMPLES:
- **Timeline Pressure Framing**: When client resists research commissioning due to timeline
  pressure, avoid arguing about "importance of research." Instead, frame research as "risk
  reduction" that prevents costly rework later. Quantify if possible: "2 days research now
  prevents 2 weeks rework in Phase 2." This reframes research from cost to investment.

- **Real-Time NOTE Capture**: NOTE candidates surface most naturally during consensus-building
  dialogue, especially when client has "aha" moment. Watch for phrases like "Oh, so we should
  always..." or "That makes sense because..." These signal NOTE-worthy insights. Capture
  immediately in Section III rather than trying to reconstruct later.

- **Decision Rationale Quality**: When documenting decisions, resist urge to write minimal
  rationale like "client requested." Future readers (including client 6 months later) need
  context: what problem was this solving? what alternatives were considered? why this one?
  Spend extra 2 minutes per decision to write rich rationale. This pays dividends during
  Phase reviews and retrospectives.

- **Subphase Transition Timing**: Don't wait for perfect completion to transition to next
  subphase. If 80% of subphase objectives achieved and progress is blocked, document
  carry-forward items and transition. Staying stuck in incomplete subphase reduces momentum
  and creates false sense of incompletion. Better to move forward with explicit tracking.
-->

- **[Training Topic]**: [Guidance for future consultants: situational awareness cues, decision heuristics, non-obvious insights, or mentoring advice that would help them navigate similar situations]
- **[Training Topic]**: [Future consultant guidance with specific context and examples]
- **[Training Topic]**: [Future consultant guidance with specific context and examples]

---

### D. Metrics & Statistics
<!--
PURPOSE: Quantitative summary of phase activity for process analysis and improvement.
These metrics help identify bottlenecks, measure efficiency, and track consultation patterns.

GUIDANCE:
- Update when phase completes (or periodically for long phases)
- Track counts of major deliverables and activities
- Include time-based metrics (duration, velocity)
- Add custom metrics relevant to specific phase

INTERPRETATION GUIDANCE:
- Total Subphases: How many distinct consultation activities?
- Total Decisions: Volume of decision-making (high count may signal complexity or indecision)
- E-RIDs/E-DIDs: Scope indicators for epic
- Issues/Risks: Problem/risk identification rate
- Research Commissioned: Dependency on external analysis
- NOTEs Promoted: Knowledge capture effectiveness
- Phase Duration: Calendar time for completion

BENCHMARKS (indicative, not prescriptive):
- Foundation Phase (0): 2-4 subphases, 10-20 decisions, 8-15 E-RIDs, 1-2 weeks
- Planning Phase (1): 3-5 subphases, 15-25 decisions, 5-10 E-DIDs, 2-3 weeks
- Execution Phase (2): Varies widely by epic scope
-->

| Metric | Value |
|:-------|:------|
| Total Subphases | [#] |
| Total Decisions | [#] |
| Total E-RIDs Proposed | [#] |
| Total E-DIDs Proposed | [#] |
| Issues Resolved | [#] |
| Risks Identified | [#] |
| Research Commissioned | [#] |
| NOTEs Promoted to SPS | [#] |
| Phase Duration (days) | [#] |
| Average Decisions per Subphase | [#] |
| Client Consultation Hours | [#] |

<!--
EXAMPLE WITH INTERPRETATION:

| Metric | Value |
|:-------|:------|
| Total Subphases | 4 |
| Total Decisions | 14 |
| Total E-RIDs Proposed | 12 |
| Total E-DIDs Proposed | 0 (Phase 0 - foundation only) |
| Issues Resolved | 3 |
| Risks Identified | 5 |
| Research Commissioned | 3 (T102B-RES-001, T102B-RES-002, T102B-RES-003) |
| NOTEs Promoted to SPS | 2 (NOTE-001, NOTE-002) |
| Phase Duration (days) | 12 |
| Average Decisions per Subphase | 3.5 |
| Client Consultation Hours | 8 |

INTERPRETATION:
- 12-day duration for Phase 0 is within normal range (10-15 days typical)
- 3 research commissions is moderate (suggests foundation needed grounding in codebase reality)
- 14 decisions across 4 subphases indicates healthy decision-making pace (not rushed, not stalled)
- 2 NOTEs promoted shows effective knowledge capture (not all insights warrant promotion)
- 8 client hours is efficient (suggests focused, well-prepared consultations)
-->

---

## V. CHANGELOG
<!--
PURPOSE: Version history tracking for LOG file evolution.
Follows semantic versioning: MAJOR.MINOR.PATCH

VERSIONING RULES:
- MAJOR (X.0.0): Phase completion, major restructuring
- MINOR (0.X.0): Subphase addition, significant content updates
- PATCH (0.0.X): Minor corrections, clarifications, formatting

GUIDANCE:
- Update changelog with EVERY file modification
- Use YYYY-MM-DD date format
- Describe WHAT changed (not why - that's in content)
- Keep descriptions concise but specific

EXAMPLES:
✓ "Added Subphase 0.2 record with E-RID definition outcomes"
✓ "Updated DEC-0.1-003 rationale with client clarification"
✓ "Corrected date range for Subphase 0.3"

✗ "Made updates" (too vague)
✗ "Fixed stuff" (not specific)
✗ "Client wanted changes" (doesn't describe what changed)
-->

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0.0 | YYYY-MM-DD | Initial log creation for Phase [#] |
| 1.1.0 | YYYY-MM-DD | Added Subphase [#.1] record with research commissioning outcomes |
| 1.2.0 | YYYY-MM-DD | Added Subphase [#.2] record with E-RID definition outcomes |
| 1.2.1 | YYYY-MM-DD | Updated DEC-[#.1]-002 rationale with additional context |
| 1.3.0 | YYYY-MM-DD | Added Subphase [#.3] record with E-DID scoping outcomes |
| 1.4.0 | YYYY-MM-DD | Added Subphase [#.4] record; completed Phase [#] Gate A approval |
| 2.0.0 | YYYY-MM-DD | Phase [#] completed; finalized all metrics and cross-phase continuity sections |

---

<!--
TEMPLATE METADATA
Template Version: 2.0.0
Created: 2026-01-14
Updated: 2026-01-15
Purpose: Generic structural template for LOG workspace files in T102 consultant workflow
Governed By: T102-ADR-004 (Artifact Structure), T102-ADR-006 (NOTE authoring)
Maintained By: T102 Initiative Team

USAGE INSTRUCTIONS FOR TEMPLATE USERS:
1. Copy this template to your workspace directory
2. Rename to: log_[EPIC-ID]_phase[#].md (e.g., log_T102A_phase0.md)
3. Fill in YAML header with initiative/epic/phase details
4. Update "I. LOG SUMMARY" as you begin the phase
5. For each subphase: Copy "Subphase [#.#]" section and fill incrementally
6. Update "II. SUBPHASE RECORDS" in real-time during consultations (don't batch)
7. Add NOTE CANDIDATES to Section III as insights emerge during dialogue
8. Complete "IV. CROSS-PHASE CONTINUITY" at phase end for training value
9. Update "V. CHANGELOG" with each meaningful edit

TIPS FOR EFFECTIVE LOG AUTHORING:
- Write as you work, not retrospectively (capture fresh context)
- Balance narrative (readability) with structure (scannability)
- Link aggressively to avoid duplication (use relative paths)
- Write for your future self: "What would I need to know to resume?"
- Use concrete examples in narrative summaries (aids understanding)
- Record alternatives considered and why they were rejected (valuable for future similar decisions)
- Flag uncertainties or assumptions that might need validation later
- Include enough detail that an external auditor could understand project trajectory
- Update decision log DURING consultation (not after) to capture rich rationale while fresh
- Watch for NOTE candidate signals: "aha" moments, pattern recognition, philosophy clarifications

HYBRID NATURE EXPLAINED:
This template intentionally combines two industry-standard project management formats:

1. MINUTES OF MEETINGS (PMI/PRINCE2):
   - Narrative summaries (Section II.A)
   - Participant tracking
   - Discussion flow and context
   - Consensus-building documentation

2. DECISION LOG (PMI PMBOK):
   - Structured decision records (Section II.B)
   - Traceability to requirements/artifacts
   - Clear ownership and rationale
   - Audit trail for governance

The combination ensures:
- Qualitative context for training/improvement (narrative)
- Quantitative traceability for compliance/audit (structured data)
- Continuity for session resumption (next-activity guidance)
- Knowledge capture for SPS promotion (NOTE candidates)

SUBPHASE STRUCTURE:
Each subphase follows A-D pattern:
A. Narrative Summary (Minutes style): What happened, how, and why
B. Decisions Made (Decision Log style): What was decided with traceability
C. Improvements & Observations: Process refinement insights
D. Next-Activity Guidance: Continuity for future sessions

This structure supports multiple use cases:
- Active use: Tracking current phase progress
- Historical reference: Understanding past decisions
- Training data: Improving future consultations
- Audit compliance: Demonstrating governance rigor
- Knowledge management: Extracting reusable insights (NOTEs)

NOTE CANDIDATE GUIDELINES (T102-ADR-006-FR-008):
NOTEs are lightweight insights (≤200 words) that capture:
✓ Contextual clarifications
✓ Philosophy and approach guidance
✓ Industry references and best practices
✓ Pattern observations from dialogue
✓ Non-obvious design choice rationales

NOTEs are NOT for:
✗ Research findings (use RES artifacts)
✗ Enforceable rules (use GDR/ADR)
✗ Formal requirements (use E-RID)
✗ Detailed specifications (use E-DID)

Promote to SPS when insight applies across multiple epics/initiatives.
Keep in LOG only when insight is epic-specific or transient.

CONTINUOUS IMPROVEMENT:
Section IV (Cross-Phase Continuity) is critical for process improvement:
- Key Patterns: What repeatedly emerges in consultations?
- Process Improvements: What template/workflow changes would help?
- Training Notes: What would help future consultants succeed faster?
- Metrics: How efficient was this phase? Where were bottlenecks?

Use this section to feed back into template refinement and consultant training.
-->
