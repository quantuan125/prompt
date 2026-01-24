---
artifact_type: 'BRIEF'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1-PROMPT'
research_id: 'T810A1-RES-002'
version: '1.0.0'
iteration: '1'
date: '2025-10-19'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: S05 Execution Protocol Clinical Validation & Best Practices

## I. EXECUTIVE SUMMARY

This research brief commissions a comprehensive investigation into clinical best practices, LLM optimization techniques, and medical AI execution patterns to inform the development of **T810A1-PROMPT Story S05 (Execution Protocol)**. The research aims to discover evidence-based clinical consultation workflows, validate the five-phase protocol architecture (Tracking→Analyze→Probe→Coach→Summarize), identify optimal questioning frameworks, and establish LLM prompt engineering patterns for clinical tracking applications.

This research directly addresses critical S05 development requirements:
- **Phase-by-phase clinical workflow validation** from gastroenterologist/dietitian expert practices
- **Optimal Probe questioning framework discovery** (NOT validation of proposed 5-question pattern; find industry-standard best practices)
- **Analysis presentation best practices** (confidence-based data presentation, when to explain reasoning)
- **ChatGPT Assistant override strategies** and protocol triggering patterns from existing LLM agents
- **Medical LLM execution protocol construction** patterns from similar clinical applications

## II. RESEARCH SCOPE & OBJECTIVES

### **Primary Research Questions**

#### **DOMAIN A: Clinical Best Practices & Expert Workflows**

**1. Gastroenterologist/Dietitian Consultation Techniques & Questioning Practices**
- What are evidence-based questioning practices used by gastroenterologists and dietitians during patient consultations?
- How do GI experts structure patient interviews to gather comprehensive symptom, dietary, and lifestyle information?
- What are established clinical communication frameworks (Motivational Interviewing, patient-centered communication, symptom elicitation techniques) applicable to GI consultation?
- How do experts balance data collection (tracking information) with empathetic engagement to avoid "interrogation feel"?
- What is the optimal number and type distribution of questions in a clinical consultation session? (3 vs. 5 vs. 7 questions; question type balance)
- How do GI practitioners transition between different consultation phases (data gathering vs. analysis vs. coaching)?

**2. Clinical Analysis Best Practices & Data Presentation Patterns**
- What information is most important to analyze and present in GI symptom tracking contexts?
- How do experts present findings based on confidence levels or certainty? (e.g., high-confidence Bristol classification vs. low-confidence classification)
- When should analysis explain reasoning/methodology vs. state conclusions directly?
- How do gastroenterologists communicate uncertainty about symptom patterns or trigger identification?
- What contextual factors determine depth of analysis presentation? (e.g., patient expertise level, severity of symptoms)
- Example scenario: If stool Bristol type confidence >70%, should explanation of classification reasoning be included? What about <70% confidence?

**3. Optimal Probe Questioning Framework Discovery**
- What is the industry-standard or evidence-based framework for clinical questioning in GI consultations?
- CRITICAL: Research should **DISCOVER** optimal framework, NOT validate the proposed 5-question breakdown (1-2 tracking + 1 history + 1-2 immediate context + 1 future)
- What question type distribution yields comprehensive patient data while maintaining engagement?
- How should questions be sequenced? (prioritization: tracking gaps → history → immediate context → future planning)
- What are best practices for iterative vs. batch questioning? (one question at a time vs. multiple questions together)
- How do experts ensure each patient answer is addressed individually vs. lumping responses?

**4. Engagement Dialogue Patterns in Medical Consultations**
- How do GI experts maintain conversational, empathetic dialogue (Socratic questioning) while gathering clinical data?
- What are effective "Engage" techniques? (acknowledging patient answers, validating concerns, building rapport)
- How do consultations avoid feeling like interrogations or assistant-style checklists?
- What language patterns foster collaborative dialogue vs. extractive questioning?
- How do experts integrate patient perspectives and subjective experiences into objective clinical analysis?

**5. Full Five-Phase Protocol Validation from Expert Standpoint**
- How do gastroenterologist/dietitian consultations map to the proposed five-phase protocol?
  - **Phase 1 (Tracking)**: Structured data capture from unstructured patient narratives
  - **Phase 2 (Analyze)**: Clinical reasoning and pattern identification
  - **Phase 2.5 (Coach)** [Optional]: Actionable recommendations when explicitly requested
  - **Phase 3 (Probe & Engage)**: Iterative questioning + empathetic response to answers
  - **Phase 4 (Summarize)**: Session closure and action plan recap
- Are there missing phases or sub-phases in expert clinical workflows?
- How do experts handle phase transitions? (when to move from analysis to questioning, when to offer coaching)
- What triggers coaching recommendations vs. continued questioning in clinical practice?
- How do expert workflows handle patient-initiated coaching requests mid-session?

#### **DOMAIN B: LLM Optimization & Medical AI Applications**

**6. ChatGPT Assistant Mode Override Strategies (Comparative Agent Analysis)**
- What prompt engineering techniques effectively override ChatGPT's native "helpful Assistant" behavior to enforce Consultant/Analyst mode?
- Comparative analysis of existing LLM agent patterns:
  - **LLM_Consultant**: `prompt\scripts\output\general_2025-08-02-13-53_reconstructed.md`
    - Extract guard/gate patterns ensuring Socratic stance (questions before answers)
    - Identify anti-Assistant behavioral guardrails (prohibit "Would you like me to..." service offers)
    - Analyze Probe enforcement mechanisms
  - **LLM_Trader (VPA)**: `prompt\roles\VPA\main_v2.1.md`
    - Extract protocol triggering patterns (conditional execution based on input type)
    - Identify multi-phase execution workflows
    - Analyze guard clauses preventing premature analysis or recommendations
- What exemplar-based techniques enforce minimum 2-loop conversation pattern (Probe before Coach)?
- How can protocols prevent premature coaching? (anti-pattern: "If you like, I can turn this into a one-page daily protocol...")

**7. Protocol Triggering Logic & Input Type Detection**
- How can LLM_Gastro distinguish between different input types and trigger appropriate protocols?
  - **Tracking-Only Trigger**: Imperative keywords (e.g., "UPDATE the JSON...", "RECORD today's...")
  - **Full Protocol Trigger**: Narrative note + images WITHOUT tracking-only keywords
  - **Q&A Trigger**: Direct informational question unrelated to tracking session
  - **Coaching Request Trigger**: Explicit request for recommendations or advice
- What keyword patterns, context clues, or heuristics enable reliable input type detection?
- What should default behavior be when input type is ambiguous? (default to full protocol vs. minimal response)
- How do VPA-style conditional execution patterns translate to clinical tracking use case?

**8. Probe Phase Enforcement & Trust-and-Verify Workflows**
- What prompt engineering patterns enforce "Probe-first" behavior? (mandatory questions before coaching)
- How do clinical AI systems ensure minimum question thresholds without feeling robotic?
- What confidence threshold patterns trigger patient verification? (e.g., <70% classification confidence requires confirmation)
- How should trust-and-verify workflows be integrated into conversational flow? (seamless vs. explicit validation steps)
- What anti-patterns should be avoided? (over-questioning, ignoring patient cues, formulaic responses)

**9. Existing Medical LLM Applications & Execution Protocols Review**
- What LLM applications exist in doctor/medical fields, specifically gastroenterology/dietitian domains?
- How do these applications structure execution protocols for clinical tracking/consultation?
- What proven patterns exist for multimodal data capture (images + text) in medical contexts?
- How do medical LLMs balance standardized protocols with flexible, patient-centered dialogue?
- What failure modes or common pitfalls exist in medical AI consultation systems?
- Examples to investigate:
  - GI-specific symptom trackers (MyGiHealth, Oshi Health, Cara Care)
  - General medical AI consultants (Ada Health, Buoy Health, Isabel)
  - Health coaching platforms (Noom, Omada Health, Virta Health)

#### **CROSS-PHASE ANALYSIS: Template-Driven Architecture & Phase Integration**

**10. Phase 1 (Tracking) - Template-Driven JSON Generation Best Practices**
- What are industry-standard patterns for template-driven data capture in clinical contexts?
- How should instructional templates be designed to teach LLM generation rules? (inline annotations vs. clean exemplars vs. hybrid)
- How do medical forms/structured data capture tools balance guidance with flexibility?
- What validation approaches exist for prompt-only JSON generation without programmatic validation?

**11. Phase 2 (Analyze) - Confidence-Based Analysis Presentation Patterns**
- How should analysis depth vary based on classification/assessment confidence?
- When should analysis explain "why" vs. state "what"? (reasoning transparency vs. conciseness)
- How do experts present Bristol Chart classifications with varying confidence levels?
- What metadata should be explained proactively vs. on-demand? (confidence scores, missing fields, classification rationale)
- How should analysis prepare context for subsequent Probe phase? (identify gaps explicitly vs. implicitly)

**12. Phase 2.5 (Coach) - Optional Coaching Triggers & Shortened Workflow Validation**
- How do expert consultations handle explicit patient requests for coaching mid-session?
- What are valid shortened workflows when coaching is requested before full context gathering?
  - `Analyze → Coach → Probe → Summarize` (coaching on existing data, then gather more context)
  - `Coach → Probe → Summarize` (short Q&A with explicit coaching request)
- When should coaching be deferred despite patient request? (insufficient data, safety concerns)
- How do experts gate coaching to ensure patient readiness and data adequacy?

**13. Phase 3 (Probe & Engage) - Iterative Questioning & Engagement Integration**
- How should "Probe" (questioning) and "Engage" (answering/acknowledging) be integrated?
- What patterns ensure each patient answer is addressed individually vs. lumped together?
- How do experts balance efficiency (asking multiple questions) with empathy (one question at a time, acknowledging responses)?
- What conversational techniques maintain Socratic dialogue flow across multiple question-answer cycles?

**14. Phase 4 (Summarize) - Effective Closure Communication in Clinical Contexts**
- How do gastroenterologists/dietitians close consultation sessions?
- What elements belong in clinical session summaries? (action items, follow-up plans, key takeaways)
- What tone and length are appropriate for TLDR-style closures?
- How should summaries confirm decisions and next steps without overwhelming patients?

## III. DELIVERABLES

### **REQUIRED REPORT STRUCTURE**

**Deliverable**: Research Report (`report_s05-execution-protocol-clinical-validation_T810A1-RES-002_v1.0.0.md`)

**CRITICAL**: Report MUST follow the structural exemplar provided in:
- `prompt/artifacts/tasks/T810/research/report/report_prompt-architecture-clinical-validation_T810A.md`

**Report shall include the following sections** (mirroring exemplar structure):

#### **Section I: Executive Summary**
- Brief overview of research findings across all domains
- Key insights for S05 development
- Critical recommendations summary

#### **Section II: Deliverable A - Clinical Best Practices & Expert Workflows**
- **A.1**: Gastroenterologist/Dietitian Questioning Techniques Synthesis
- **A.2**: Clinical Analysis Best Practices & Confidence-Based Presentation Patterns
- **A.3**: Optimal Probe Questioning Framework (DISCOVERED framework, NOT validation of proposed 5-question pattern)
- **A.4**: Engagement Dialogue Patterns in Medical Consultations
- **A.5**: Five-Phase Protocol Validation from Expert Clinical Standpoint

#### **Section III: Deliverable B - LLM Optimization Techniques**
- **B.1**: ChatGPT Assistant Override Strategies (LLM_Consultant and VPA Comparative Analysis)
- **B.2**: Protocol Triggering Logic & Input Type Detection Heuristics
- **B.3**: Probe Phase Enforcement Mechanisms
- **B.4**: Trust-and-Verify Workflow Integration Patterns

#### **Section IV: Deliverable C - Medical LLM Application Landscape**
- **C.1**: Existing Medical LLM Applications Review (GI/dietitian domain focus)
- **C.2**: Execution Protocol Construction Patterns in Clinical LLM Agents
- **C.3**: Proven Patterns and Common Failure Modes

#### **Section V: Deliverable D - Cross-Phase Integration Analysis**
- **D.1**: Phase 1 (Tracking) - Template-Driven JSON Generation Best Practices
- **D.2**: Phase 2 (Analyze) - Confidence-Based Analysis Presentation Recommendations
- **D.3**: Phase 2.5 (Coach) - Optional Coaching Triggers & Shortened Workflow Validation
- **D.4**: Phase 3 (Probe & Engage) - Iterative Questioning & Engagement Dialogue Integration
- **D.5**: Phase 4 (Summarize) - Clinical Closure Communication Patterns

#### **Section VI: Integrated Recommendations for S05 Development**
- **Recommendation Set 1**: S05-FR-001 (Five-Phase Protocol Execution STEPS)
  - Concrete STEP specifications for each phase informed by research findings
  - Phase transition logic based on expert workflows
  - Integration of discovered optimal questioning framework into Phase 3
- **Recommendation Set 2**: S05-FR-002 (Probe Phase Enforcement)
  - ChatGPT override strategies from comparative agent analysis
  - Anti-Assistant behavioral guardrails
  - Minimum question threshold enforcement mechanisms
- **Recommendation Set 3**: S05-FR-003 (Trust-and-Verify Workflow Integration)
  - Confidence threshold recommendations (when to explain reasoning, when to verify with patient)
  - Qualitative confidence communication patterns
- **Recommendation Set 4**: S05-FR-006 (Phase Transition Heuristics)
  - Heuristics for Analyze→Probe, Probe→Coach, Coach→Summarize transitions
  - Best-effort patterns acknowledging empirical optimization needs
- **Recommendation Set 5**: S05-FR-007 (Protocol Triggering Logic)
  - Input type detection keyword patterns
  - Default behavior specification for ambiguous inputs
  - Integration of VPA-style conditional execution

#### **Section VII: Exemplar Phrasing Examples for S08 Integration**
- **Phase 1 (Tracking)**: Template-driven JSON generation examples
- **Phase 2 (Analyze)**: High-confidence vs. low-confidence analysis presentation examples
- **Phase 2.5 (Coach)**: Coaching examples with explicit request gating
- **Phase 3 (Probe & Engage)**: Iterative questioning examples with individual answer engagement
- **Phase 4 (Summarize)**: TLDR closure examples
- **Anti-Patterns**: Examples of what to AVOID (premature coaching, lumped responses, interrogation feel)

## IV. RESEARCH METHODOLOGY

### **A. Clinical Standards & Framework Analysis**

**Clinical Interaction Frameworks:**
- Motivational Interviewing (MI) framework documentation (Miller & Rollnick)
- Patient-centered communication standards (ACGME, ABIM competencies)
- Socratic questioning in medical education (NEJM, medical pedagogy literature)
- Gastroenterology clinical practice communication guidelines

**Gastroenterology Clinical Standards:**
- ROME IV criteria for functional GI disorders
- Bristol Stool Chart official documentation and usage guidelines
- Clinical consultation workflow research (GI-specific)
- Dietary consultation best practices (FODMAP framework, trigger identification methods)

### **B. Application Comparative Analysis**

**Existing LLM Agent Analysis** (PRIMARY):
- **LLM_Consultant**: `prompt\scripts\output\general_2025-08-02-13-53_reconstructed.md`
  - Extract Socratic stance enforcement patterns
  - Identify Probe-before-answer mechanisms
  - Analyze gate patterns preventing premature solutions
- **LLM_Trader (VPA)**: `prompt\roles\VPA\main_v2.1.md`
  - Extract protocol triggering conditional logic
  - Identify multi-phase workflow patterns
  - Analyze guard clauses and behavioral constraints

**Medical LLM Applications:**
- GI Management Applications: MyGiHealth, Oshi Health, Cara Care, Monash FODMAP app
- Clinical AI Systems: Ada Health, Buoy Health, Isabel (symptom checker interaction patterns)
- Digital Health Coaching Platforms: Noom, Omada Health, Virta Health

### **C. Literature & Expert Practice Review**

**Academic & Clinical Literature:**
- Clinical reasoning and diagnostic frameworks in gastroenterology
- Patient interview techniques and consultation effectiveness research
- Medical AI confidence scoring and uncertainty communication research
- Prompt engineering for clinical applications (if available)

**Expert Practice Patterns:**
- Gastroenterologist clinical consultation workflows (case studies, published literature)
- GI dietician patient consultation patterns
- Evidence-based questioning frameworks in medical practice

## V. CRITICAL DEPENDENCIES & CONTEXT

### **Current State Challenges**

The research directly addresses critical T810A1-S05 development blockers:

1. **Optimal Questioning Framework Uncertainty**: Client proposed 5-question breakdown (1-2 tracking + 1 history + 1-2 immediate + 1 future) requires validation or replacement with evidence-based industry-standard framework. Research should **DISCOVER** optimal pattern, not validate proposal.

2. **Analysis Presentation Ambiguity**: Unclear what depth of analysis to present based on confidence levels. Example: if Bristol classification confidence >70%, should reasoning be explained? What about <70%? Research needed on confidence-based presentation patterns.

3. **Phase Integration Gaps**: Five-phase protocol requires validation from expert clinical workflow standpoint. Are phases correct? Missing? Wrong sequencing? Research validates architecture before detailed STEP specification.

4. **Coach Positioning Uncertainty**: Client suggested Coach as "Phase 2.5" (optional, before Probe) with shortened workflows possible. Research should validate shortened workflow viability: `Analyze→Coach→Probe→Summarize` or `Coach→Probe→Summarize`.

5. **ChatGPT Override Strategy Gaps**: LLM_Gastro must prevent premature coaching and Assistant-mode service offers. Research extracts proven patterns from LLM_Consultant and VPA to inform enforcement mechanisms.

6. **Probe & Engage Merge Confusion**: "Probe" = questioning, "Engage" = answering/acknowledging patient responses. Research clarifies how these integrate iteratively (NOT separate phases) and how to avoid lumped responses.

### **Integration with T810A1 Features**

Research findings will directly inform:

- **S05-FR-001 (Five-Phase Protocol Execution)**:
  - Phase 1 STEPS: Template-driven tracking best practices
  - Phase 2 STEPS: Analysis presentation patterns based on confidence
  - Phase 2.5 STEPS: Optional Coach gating logic
  - Phase 3 STEPS: Research-discovered optimal questioning framework, iterative engagement patterns
  - Phase 4 STEPS: Clinical closure communication

- **S05-FR-002 (Probe Phase Enforcement)**:
  - ChatGPT override strategies from LLM_Consultant/VPA
  - Anti-Assistant behavioral guardrails
  - Minimum question threshold enforcement without robotic feel

- **S05-FR-003 (Trust-and-Verify Workflow)**:
  - Confidence threshold recommendations for patient verification triggers
  - Qualitative confidence communication in prose
  - Seamless trust-and-verify integration into dialogue flow

- **S05-FR-006 (Phase Transition Heuristics)**:
  - Expert-validated transition triggers
  - Best-effort heuristics acknowledging empirical optimization needs

- **S05-FR-007 (Protocol Triggering Logic)**:
  - Input type detection keyword patterns
  - VPA-style conditional execution adaptation
  - Default behavior specification

- **T810A1-S08 (Exemplars)**:
  - Concrete dialogue examples for all phases
  - Anti-pattern examples (premature coaching, lumped responses, interrogation feel)

### **Alignment with Initiative Governance**

Research must respect existing requirements:
- **T810A1-NFR-001 (Protocol Reliability)**: Research enhancements must preserve protocol adherence
- **T810A-GDR-001 (Tracking-First Clinical Protocol)**: Tracking phase primary; research validates priority
- **T810A-GDR-002 (Trust-and-Verify Workflow Standard)**: Research informs verification patterns
- **T810A1-CON-008 (ChatGPT Platform Constraints)**: Prompt-only solutions; no custom tooling in MVP

## VI. SUCCESS CRITERIA

The research will be considered successful if it delivers:

1. **Industry-Validated Optimal Questioning Framework**: DISCOVERED evidence-based framework (NOT validation of proposed 5-question pattern), with question type distribution and sequencing guidance
2. **Clinical Analysis Presentation Patterns**: Confidence-based depth recommendations (when to explain reasoning vs. state conclusions; >70% vs. <70% thresholds)
3. **Five-Phase Protocol Validation**: Expert workflow mapping confirms architecture or identifies gaps/adjustments
4. **ChatGPT Override Strategies**: Concrete prompt engineering patterns extracted from LLM_Consultant and VPA for Probe enforcement and anti-Assistant behavior
5. **Protocol Triggering Heuristics**: Keyword patterns and context clues for input type detection (tracking-only vs. full protocol vs. Q&A vs. coaching request)
6. **Medical LLM Landscape Insights**: Proven patterns and common failure modes from existing GI/medical AI applications
7. **Cross-Phase Integration Guidance**: Specific recommendations for all phases (Tracking templates, Analyze presentation, Coach gating, Probe engagement, Summarize closure)
8. **Exemplar Phrasing Library**: Concrete examples ready for S08 integration (including anti-patterns)
9. **Shortened Workflow Validation**: Confirmation of `Analyze→Coach→Probe→Summarize` and `Coach→Probe→Summarize` viability

## VII. TIMELINE & RESOURCES

### **Research Duration**
- **Target**: 5-10 minutes (comprehensive research cycle covering all domains)
- **Priority**: HIGH — Blocks T810A1-S05 specification and development

### **Required Resources**
- Access to Motivational Interviewing and patient-centered communication framework documentation
- ROME IV criteria, Bristol Stool Chart standards, gastroenterology clinical practice guidelines
- Access to LLM_Consultant and VPA agent prompt files (specified paths provided)
- Access to clinical AI application interfaces/documentation (Ada Health, Buoy Health, GI apps)
- Medical AI confidence scoring research literature
- **Current Baselines for Comparative Analysis:**
  - LLM_Consultant: `prompt\scripts\output\general_2025-08-02-13-53_reconstructed.md`
  - LLM_Trader (VPA): `prompt\roles\VPA\main_v2.1.md`
  - Example tracking JSON: `prompt/artifacts/tasks/T810/resources/gastro_example_tracking.json`
  - CareCare screenshots: `prompt/artifacts/tasks/T810/resources/carecare_meal_tracking.jpeg`, `carecare_symptoms_tracking.jpeg`

## VIII. STAKEHOLDER ENGAGEMENT

### **Primary Stakeholders**
- **Client (Decision Owner)**: Final approval of research scope and acceptance of findings
- **LLM_Consultant (T810A1)**: Primary consumer of research findings for S05 specification development
- **LLM_Research**: External research agent conducting the focused investigation

### **Review & Approval Gates**
- **Research Scope Approval**: Client confirmation of research objectives and methodology (Gate 1 - Current)
- **Final Deliverable Review**: Client acceptance of research findings and S05 integration recommendations (Gate 2)

### **Integration with T810A1 Development**

Research findings will be integrated into T810A1-S05 specification:
- **Phase 3.3A**: Research commissioned in parallel with T810A2-SCHEMA
- **Phase 3.3C Step 1**: Research findings analyzed before S05 STEP specification drafting
- **Phase 3.3C Step 2**: Findings inform all S05 FRs (FR-001 through FR-007)
- **Phase 3.6 (S08)**: Exemplar phrasing examples from research integrated into S08 development

## IX. KNOWN CONSTRAINTS & ASSUMPTIONS

### **Constraints**
- Research scope limited to information publicly available or accessible via web search
- No direct patient interviews or clinical trial data
- Gastroenterologist expert practice insights limited to published literature/case studies
- Research must align with ChatGPT native platform capabilities (no custom tooling in MVP)

### **Assumptions**
- Industry frameworks (MI, patient-centered communication, clinical consultation research) contain transferable insights despite not being LLM_Gastro-specific
- Optimal questioning frameworks from clinical practice can adapt to chatbot context with appropriate modifications
- LLM_Consultant and VPA agent patterns provide sufficient exemplars for ChatGPT override strategy extraction
- Existing medical LLM applications (GI apps, health coaches) use execution protocols adaptable to LLM_Gastro use case

## X. APPENDICES

### **A. Related T810A1 Documents**

**Primary Planning Document**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/workspace/plan/plan_T810A1-PROMPT_phase1-4.md`
- **Key Section**: Phase 3.3 (Story S05 — Execution Protocol), lines 339-562

**T810A1 Request Document**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md`
- **Key Dependencies**:
  - NFR-001 (Protocol Reliability)
  - T810A-GDR-001 (Tracking-First Clinical Protocol)
  - T810A-GDR-002 (Trust-and-Verify Workflow Standard)

**T810A1 SPS Document**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md`
- **Key Context**: Initial problem framing and conceptual solution

### **B. Comparative Analysis Source Files**

**LLM Agent Exemplars** (CRITICAL for Domain B analysis):
- `prompt\scripts\output\general_2025-08-02-13-53_reconstructed.md` (LLM_Consultant)
- `prompt\roles\VPA\main_v2.1.md` (LLM_Trader)

**Reference Examples**:
- `prompt/artifacts/tasks/T810/resources/gastro_example_tracking.json` (tracking structure)
- `prompt/artifacts/tasks/T810/resources/carecare_meal_tracking.jpeg` (meal tracking UX)
- `prompt/artifacts/tasks/T810/resources/carecare_symptoms_tracking.jpeg` (symptom tracking UX)

### **C. Report Structure Exemplar**

**CRITICAL**: Research report MUST use the following structural exemplar:
- **Path**: `prompt/artifacts/tasks/T810/research/report/report_prompt-architecture-clinical-validation_T810A.md`
- **Purpose**: Ensures consistency with previous T810A research deliverables
- **Note to LLM_Research**: Review exemplar structure before drafting report; mirror section organization, heading levels, and depth of analysis

---

**Prepared by:** LLM_Consultant (T810A1)
**Approval Required:** Client (Decision Owner)
**Target Start Date:** Upon approval (Phase 3.3A Step 3)
**Expected Completion:** 5-10 minutes from initiation
**Criticality:** **HIGH** — Blocks T810A1-S05 specification; validates S05-FR-001 through S05-FR-007; informs S08 exemplar development
