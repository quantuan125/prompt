---
artifact_type: 'RESEARCH'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A-PROMPT'
version: '1.0.0'
iteration: '1'
date: '2025-10-10'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: LLM_Gastro System Prompt Architecture & Clinical Application Validation

## I. EXECUTIVE SUMMARY

This research brief commissions a focused investigation into industry-standard approaches for modular LLM system prompt architecture, clinical AI interaction patterns, and gastroenterological domain-specific practices. The research aims to validate the proposed 9-block system prompt framework for LLM_Gastro, identify enhancements to the Analyze→Probe→Coach protocol, and establish evidence-based patterns for multimodal image classification, patient profiling, session workflows, and clinical reporting that will directly inform functional requirement development for all system prompt stories (S01-S10).

## II. RESEARCH SCOPE & OBJECTIVES

### **Primary Research Questions**

1. **9-Block Modular System Prompt Architecture Validation**
   - What are industry-standard patterns for structuring LLM system prompts in production environments (OpenAI, Anthropic, Google)?
   - How do clinical AI systems organize system prompts to balance governance, execution logic, and domain knowledge?
   - What are established patterns for modular prompt composition (block-based, compositional, template-driven)?
   - How does the proposed 9-block structure (Project Context, Role Identity, Toolbox, Knowledge Base, Execution Protocol, Behavioral Guardrails, Quality Criteria, Exemplars, I/O Specification) align with or diverge from industry best practices?
   - What are the trade-offs between monolithic vs. modular prompt architectures in clinical use cases?

2. **Multimodal Clinical Image Classification & Trust-and-Verify Patterns (ChatGPT Conversational Interface)**
   - What are industry-standard approaches for communicating classification confidence in clinical AI systems (dermatology, radiology, pathology)?
   - How do medical imaging AI systems implement "trust-and-verify" workflows where users validate AI-generated classifications **through conversational dialogue**?
   - What confidence threshold patterns exist for triggering human verification (e.g., <70% certainty requires confirmation)?
   - How should stool image classification (Bristol Scale) and meal image analysis communicate uncertainty to maintain patient trust **within ChatGPT's text-based conversation interface** (no custom UI elements)?
   - What prompt engineering patterns exist for explicitly stating classification confidence levels with contextual explanations **in natural language responses**?
   - How do clinical AI systems handle context overload (long conversation histories) that may degrade multimodal analysis accuracy?
   - **MVP Constraint:** Research must focus on prompt-only solutions compatible with ChatGPT's native interface; UI enhancements (confidence bars, confirmation buttons) are out of scope.

3. **Analyze→Probe→Coach Protocol Validation & Enhancement**
   - What are evidence-based clinical interaction frameworks that align with the Analyze→Probe→Coach pattern?
   - How do Motivational Interviewing (MI), Cognitive Behavioral Therapy (CBT), and Socratic questioning frameworks structure patient-agent dialogues?
   - What are best practices for transitioning between analytical (detached) and collaborative (empathetic) communication tones in clinical AI?
   - How do existing clinical coaching AI systems (Noom, Omada Health, Virta Health) structure their interaction protocols?
   - What enhancements could strengthen the Analyze→Probe→Coach workflow to ensure robustness across diverse patient scenarios?
   - Are there missing phases or quality checkpoints that should be incorporated into the protocol?

4. **Gastroenterologist Expert Workflow & Knowledge Source Analysis**
   - How do gastroenterologists structure their clinical reasoning process when analyzing patient symptoms, dietary triggers, and stool patterns?
   - What knowledge sources do GI specialists consult during patient consultations (clinical practice guidelines, ROME IV criteria, FODMAP research, Bristol Stool Chart)?
   - What decision trees or diagnostic frameworks do GI experts use to generate hypotheses for conditions like IBS-D, SIBO, bile acid malabsorption, or fat maldigestion?
   - How do GI practitioners balance pattern recognition (experiential knowledge) with evidence-based guidelines?
   - What are common workflows for tracking patient data over time (symptom logs, food diaries, stool tracking)?

5. **Patient Profile Schema & Cross-Session Memory Architecture (MVP Simplicity)**
   - What patient profile schemas are used in existing GI management applications (MyGiHealth, Oshi Health, Cara Care, FODMAP apps)?
   - How should the current profile skeleton (`patient_id, triggers, relievers, medications, supplements, allergies, conditions, notes, last_updated`) be **minimally enhanced** to support MVP GI symptom management?
   - What **essential fields** distinguish constant data (patient demographics), stable data (allergies, conditions), and dynamic data (behavior patterns, current triggers)?
   - How should profile data be structured to optimize LLM consumption in Block 4 (Knowledge Base) while maintaining JSON validation?
   - **MVP Constraint:** Profile schema should prioritize simplicity and LLM consumption efficiency. Advanced features (temporal tracking, version history, medication timelines, profile evolution strategies) are explicitly deferred to Feature T810D-PROFILE. Research should identify only what's **necessary for MVP S04 specification**, not comprehensive long-term tracking.

6. **Clinical Reporting for Dual-Purpose Use (Single Report Type: End-of-Day Summary)**
   - What report structures are standard in gastroenterology practice (colonoscopy reports, symptom diaries, IBD flare logs, dietician consultation summaries)?
   - How do GI clinicians prefer to receive patient-generated data for review (narrative summaries, timeline visualizations, structured data tables)?
   - What are industry patterns for generating **end-of-day timeline-based clinical reports** that aggregate symptoms, meals, stools, and contextual factors **from a single session**?
   - How should reports be structured to serve dual purposes: (1) clinician handoff quality, (2) LLM long-term memory input for future sessions?
   - What validation protocols exist to ensure report accuracy before patient shares with healthcare providers?
   - How do clinical AI systems address token window limitations through strategic report summarization?
   - **MVP Constraint:** Research should focus on **one stable reporting pattern** (triggered by `/report` command, likely end-of-day). Multi-frequency reporting (mid-day summaries, multi-day aggregations, flexible on-demand snapshots) is out of scope for MVP.

7. **Session Workflow & Patient Interaction Patterns**
   - How do clinical AI systems handle first-session initialization with new users (passive profile extraction through natural conversation vs. guided onboarding questionnaires)?
   - What are best practices for proactive vs. reactive analysis in patient-generated health tracking applications (should agent analyze images immediately upon receipt or wait for explicit user questions)?
   - How do clinical coaching AI systems balance dietary/lifestyle recommendation specificity with safety guardrails (general guidance vs. specific targets vs. clinician-deferred recommendations)?
   - What continuity models do health tracking apps use for multi-interaction daily workflows (single continuous conversation thread vs. discrete event-based conversations)?
   - How do clinical AI systems manage "empty profile" states when users begin without pre-existing clinical data?
   - What onboarding patterns create optimal first-session user experience without overwhelming patients with data entry requirements?

### **Secondary Research Objectives**

8. **Clinical Safety Deferral Documentation**
   - Catalog industry approaches to documenting deferred safety/compliance work in clinical AI MVPs
   - Identify appropriate constraint/dependency patterns for flagging future regulatory work (FDA SaMD, ISO 13485)

9. **LLM Gastroenterology Application Landscape**
   - Survey existing LLM applications in gastroenterology (if any) to identify proven patterns and common failure modes
   - Analyze how general-purpose medical LLMs (Med-PaLM 2, GPT-4 medical applications) handle GI-specific reasoning

## III. RESEARCH DELIVERABLES

### **A. System Prompt Architecture Validation Report**
- **9-Block Framework Assessment:** Comparative analysis of proposed structure against industry patterns (OpenAI, Anthropic, clinical AI exemplars)
- **Modularity Best Practices:** Recommendations for block composition, governance placement, and cross-block referencing
- **Clinical AI Adaptations:** Specific considerations for adapting general LLM prompt patterns to clinical gastroenterology use case
- **Implementation Guidance:** Actionable recommendations for finalizing 9-block structure with industry validation

### **B. Multimodal Classification & Trust-and-Verify Framework (ChatGPT Prompt-Only)**
- **Confidence Communication Patterns:** Catalog of industry approaches for stating classification uncertainty **through conversational language** (percentage thresholds, qualitative descriptors like "high/medium/low confidence")
- **Trust-and-Verify Workflow Design:** Step-by-step **conversational patterns** for patient validation of Bristol Scale classifications and meal image analysis within ChatGPT's text interface
- **Context Overload Mitigation:** Strategies for maintaining multimodal accuracy in long conversation sessions
- **Prompt Engineering Patterns:** Concrete implementation examples for confidence scoring integration into Analyze phase **using natural language responses only**
- **User Experience Recommendations:** Best practices for balancing AI utility with appropriate skepticism in text-based dialogue
- **MVP Scope Note:** Research excludes UI elements (confidence bars, buttons, visual indicators); focus solely on prompt engineering for trust-and-verify within ChatGPT's native interface

### **C. Analyze→Probe→Coach Protocol Enhancement Report**
- **Evidence-Based Framework Alignment:** Mapping of Analyze→Probe→Coach against MI, CBT, and Socratic questioning models
- **Protocol Robustness Assessment:** Gap analysis identifying missing phases, quality checkpoints, or failure modes
- **Tone Transition Patterns:** Best practices for dual-tone communication (analytical detachment vs. empathetic collaboration)
- **Enhancement Recommendations:** Specific protocol refinements to strengthen S05 (Execution Protocol) specification
- **Case Study Analysis:** Real-world examples from clinical coaching AI demonstrating successful interaction patterns

### **D. GI Expert Practice & Knowledge Source Synthesis**
- **Clinical Reasoning Workflow:** Synthesis of gastroenterologist diagnostic and management processes
- **Knowledge Source Catalog:** Comprehensive list of authoritative GI resources (ROME IV, FODMAP frameworks, clinical practice guidelines, Bristol Stool Chart standards)
- **Decision Framework Mapping:** Common diagnostic trees for IBS-D, SIBO, bile acid issues, fat maldigestion
- **Pattern Recognition vs. Evidence Balance:** Insights into how experts integrate experiential knowledge with guidelines
- **Block 4 Design Insights:** Recommendations for structuring Knowledge Base content based on expert practice patterns

### **E. Patient Profile Schema Optimization (MVP Simplicity Focus)**
- **Current Skeleton Assessment:** Analysis of existing `profile.json` structure (`patient_id, triggers, relievers, medications, supplements, allergies, conditions, notes, last_updated`)
- **Industry Profile Comparison:** Side-by-side comparison with GI management app schemas (MyGiHealth, Oshi Health, Cara Care) to identify **minimal essential fields**
- **Enhanced Schema Proposal:** Recommended **MVP-scoped additions** distinguishing constant, stable, and dynamic data categories
- **JSON Validation Guidance:** Schema optimization for LLM consumption in Block 4 while maintaining strict validation
- **MVP Scope Note:** Advanced features (temporal tracking with dates, version history, medication timelines, symptom severity trends, complex profile evolution strategies) are explicitly out of scope. Research should deliver the **simplest viable schema** for S04 (Knowledge Base) specification. Comprehensive profiling features deferred to T810D-PROFILE.

### **F. Clinical Reporting Architecture (Single End-of-Day Pattern)**
- **GI Report Structure Standards:** Catalog of standard gastroenterology report formats (symptom diaries, IBD flare logs, dietician summaries)
- **Dual-Purpose Report Design:** Framework for **single-session end-of-day reports** serving both clinician handoff and LLM long-term memory purposes
- **Timeline Generation Patterns:** Best practices for aggregating symptoms, meals, stools, and context into **single-day chronological narratives**
- **Validation Protocol Recommendations:** Pre-handoff quality assurance patterns for patient-generated clinical data
- **Token Optimization Strategies:** Approaches for strategic summarization to address LLM context window limitations
- **Block 9 Design Insights:** Recommendations for `/report` command output format and structure patterns
- **MVP Scope Note:** Research focuses on **one stable reporting frequency** (end-of-day summary triggered by `/report` command). Multi-frequency patterns (mid-day, multi-day aggregations, flexible on-demand) are out of scope.

### **G. Session Workflow & Interaction Pattern Analysis**
- **First-Session Initialization Patterns:** Comparative analysis of passive extraction vs. guided onboarding approaches in clinical AI
- **Proactive vs. Reactive Analysis Models:** Best practices for automatic image analysis vs. user-triggered analysis in health tracking
- **Recommendation Specificity Framework:** Guidelines for balancing specific dietary advice with appropriate safety guardrails
- **Continuity Model Patterns:** Analysis of single-thread vs. discrete-conversation approaches for multi-interaction daily workflows
- **Empty Profile State Handling:** Strategies for optimal first-session user experience without overwhelming data entry
- **Onboarding Experience Design:** Patient-centered patterns for gradual profile building through natural conversation

### **H. Implementation Insights for All System Prompt Stories**
- **S01 (Project Context - Complete):** Validation of governance stance patterns, timezone handling, and timestamp standards against industry norms
- **S02 (Role Identity - Complete):** Validation of dual-tone persona (analytical/collaborative) against clinical coaching best practices
- **S03 (Toolbox - Complete):** Validation of deferral approach for future custom tool development
- **S04 (Knowledge Base):** Patient profile schema insights, clinical knowledge source recommendations, GI expert workflow patterns
- **S05 (Execution Protocol):** Analyze→Probe→Coach enhancements, confidence scoring integration, trust-and-verify checkpoints, session initialization patterns
- **S06 (Behavioral Guardrails):** Trust-and-verify enforcement patterns, confidence threshold guidelines, recommendation specificity boundaries
- **S07 (Quality Criteria):** Measurable success benchmarks for multimodal accuracy, protocol adherence, clinical utility
- **S08 (Exemplars):** Concrete dialogue examples demonstrating confidence communication, trust-and-verify workflows, dual-tone interactions, session initialization
- **S09 (I/O Specification):** Report format patterns, profile JSON schema recommendations, timeline structure insights
- **S10 (Metadata Header):** YAML header best practices from clinical AI systems, governance metadata patterns

### **I. Safety Deferral Patterns**
- **Industry Precedent Analysis:** How do clinical AI MVPs document deferred regulatory work without undermining current scope?
- **Deferral Documentation Patterns:** Common approaches for flagging future safety/compliance work in constraint/dependency sections

## IV. RESEARCH METHODOLOGY

### **A. Standards & Framework Analysis**

**LLM System Prompt Architectures:**
- OpenAI GPT-4 Custom Instructions and System Prompt best practices
- Anthropic Claude Constitutional AI and prompt engineering guidelines
- Google Gemini system instruction patterns
- LangChain/LlamaIndex agent architecture frameworks

**Clinical Interaction Frameworks:**
- Motivational Interviewing (MI) framework documentation (Miller & Rollnick)
- Cognitive Behavioral Therapy (CBT) dialogue structuring (Beck Institute)
- Socratic questioning in medical education (NEJM, medical pedagogy literature)
- Patient-centered communication standards (ACGME, ABIM competencies)

**Gastroenterology Clinical Standards:**
- ROME IV criteria for functional GI disorders
- Bristol Stool Chart official documentation and usage guidelines
- FODMAP framework (Monash University research)
- IBS-D, SIBO, bile acid malabsorption clinical practice guidelines (ACG, WGO)

### **B. Application Comparative Analysis**

**Clinical AI Systems:**
- Isabel (symptom checker interaction patterns)
- UpToDate/DynaMed (clinical decision support presentation)
- Ada Health (symptom assessment confidence scoring)
- Buoy Health (clinical triage dialogue flows)

**Digital Health Coaching Platforms:**
- Noom (behavior change coaching protocols)
- Omada Health (chronic disease management interaction design)
- Virta Health (metabolic health coaching workflows)

**GI Management Applications:**
- MyGiHealth (IBD symptom tracking and reporting)
- Oshi Health (GI telehealth patient profiling)
- Cara Care (IBS management data structures)
- Monash FODMAP app (dietary trigger tracking)

**Medical Imaging AI (for confidence scoring patterns):**
- Dermatology AI (e.g., SkinVision, Miiskin) confidence communication
- Radiology AI (e.g., Aidoc, Zebra Medical) uncertainty handling

### **C. Literature & Expert Practice Review**

**Academic & Clinical Literature:**
- Multimodal medical AI confidence scoring research
- Clinical reasoning and diagnostic frameworks in gastroenterology
- Patient profile data structures in chronic disease management
- Clinical report generation and summarization in digital health

**Expert Practice Analysis:**
- Gastroenterologist clinical reasoning workflows (if interviews/case studies available)
- GI dietician patient consultation patterns
- Chronic GI disease longitudinal tracking best practices

**Artifact Analysis:**
- Existing `profile.json` skeleton structure at `prompt/roles/gastro/data/profile.json`
- Current T810A-PROMPT Request document requirements (Sections III.A-III.J)
- Proposed 9-block system prompt framework from `prompt/documentation/prompt_main.md`

## V. CRITICAL DEPENDENCIES & CONTEXT

### **Current State Challenges**

The research directly addresses critical T810A-PROMPT development blockers:

1. **Multimodal Trust Gap:** Patient experiences incorrect stool classifications in context-heavy sessions. No current mechanism for LLM_Gastro to communicate classification confidence or trigger patient verification.

2. **Protocol Robustness Uncertainty:** The Analyze→Probe→Coach workflow is conceptually sound but lacks industry validation. Need evidence-based enhancements before finalizing S05 (Execution Protocol) specification.

3. **Patient Profile Schema Ambiguity:** Current `profile.json` skeleton is minimal. Unclear what additional fields are necessary for comprehensive GI symptom management and optimal LLM consumption.

4. **Reporting Dual-Purpose Conflict:** Reports must serve clinician handoff (medical accuracy, professional format) AND long-term memory (LLM-optimized summarization). Unclear how to balance these competing needs.

5. **Knowledge Base Design Vacuum:** S04 specification pending. Need GI expert practice insights to determine what clinical knowledge sources, frameworks, and reasoning patterns belong in Block 4.

6. **Safety Deferral Documentation:** Clinical safety/compliance work deferred to future. Need appropriate F-ID pattern to document this without undermining current scope.

### **Integration with T810A Features**

Research findings will directly inform:

- **S04 (Knowledge Base):**
  - Patient profile schema and loading instructions
  - Clinical knowledge source integration (ROME IV, FODMAP, Bristol Chart)
  - GI expert reasoning frameworks

- **S05 (Execution Protocol):**
  - Validate and enhance Analyze→Probe→Coach workflow
  - Integrate confidence scoring into Analyze phase
  - Add trust-and-verify checkpoints
  - Define tone transition patterns

- **S06 (Behavioral Guardrails):**
  - Trust-and-verify enforcement rules
  - Confidence threshold guardrails (e.g., <70% triggers Probe)
  - Safety deferral documentation

- **S07 (Quality Criteria):**
  - Measurable multimodal accuracy criteria
  - Protocol adherence metrics
  - Clinical utility benchmarks

- **S08 (Exemplars):**
  - Confidence communication examples
  - Trust-and-verify dialogue samples
  - Dual-tone interaction demonstrations

- **S09 (I/O Specification):**
  - `/report` command output structure
  - Profile JSON schema specification
  - Timeline report format

### **Alignment with Initiative Governance**

Research must respect existing requirements:
- **T810A-PROMPT-ASSUM-003 (LLM Capability):** Platform provides multimodal vision + reasoning; research should validate sufficiency
- **T810A-PROMPT-CON-004 (No-Guessing Principle):** Trust-and-verify patterns must enforce this constraint
- **T810A-PROMPT-NFR-001 (Protocol Reliability):** Research enhancements must preserve Analyze→Probe→Coach adherence
- **T810A-PROMPT-DEP-004 (Patient Profile):** Research informs S04 design; detailed schema/backend deferred to T810D-PROFILE

## VI. SUCCESS CRITERIA

The research will be considered successful if it delivers:

1. **Industry-Validated 9-Block Architecture:** Confirmation that proposed structure aligns with best practices, or specific refinement recommendations
2. **Trust-and-Verify Implementation Patterns:** Confidence scoring patterns with threshold recommendations and prompt engineering examples
3. **Enhanced Analyze→Probe→Coach Protocol:** Evidence-based protocol refinements with concrete implementation patterns
4. **GI Expert Practice Synthesis:** Actionable insights into clinical reasoning workflows and knowledge source consumption
5. **Optimized Patient Profile Schema:** Enhanced `profile.json` structure validated against industry GI apps (MVP-scoped, constant/stable/dynamic categorization)
6. **Dual-Purpose Report Architecture:** Format patterns balancing clinician utility and LLM memory optimization
7. **Session Workflow Best Practices:** First-session initialization, proactive/reactive analysis, continuity models, and recommendation specificity patterns
8. **Implementation Insights for All Stories:** Comprehensive guidance covering S01-S10 with industry-validated patterns and recommendations
9. **Safety Deferral Documentation Patterns:** Industry precedent analysis for documenting deferred regulatory work

## VII. TIMELINE & RESOURCES

### **Research Phases**

**Phase 1: Framework Analysis**
- LLM system prompt architectures (OpenAI, Anthropic, Google, clinical AI exemplars)
- Modular prompt composition patterns and 9-block validation
- Industry best practices for clinical AI system prompt organization

**Phase 2: Clinical Interaction Patterns**
- Multimodal confidence scoring and trust-and-verify workflows
- Analyze→Probe→Coach validation against MI, CBT, Socratic questioning frameworks
- Session workflow patterns (initialization, proactive/reactive analysis, continuity models)

**Phase 3: Domain Expertise Synthesis**
- GI expert clinical reasoning workflows and knowledge source analysis
- Decision frameworks for IBS-D, SIBO, bile acid malabsorption, fat maldigestion
- Clinical practice guidelines integration patterns (ROME IV, FODMAP, Bristol Chart)

**Phase 4: Data Architecture Analysis**
- Patient profile schema optimization (GI app comparison, constant/stable/dynamic categorization)
- Clinical reporting structures (end-of-day timeline patterns, dual-purpose design)
- Token optimization strategies for LLM memory management

**Phase 5: Interaction Model Research**
- First-session onboarding patterns (passive vs. guided approaches)
- Recommendation specificity guidelines (general vs. specific with safety guardrails)
- Multi-interaction continuity models for daily health tracking

**Phase 6: Synthesis & Documentation**
- Integration of findings across all research dimensions
- Pattern extraction and implementation insights for Stories S01-S10
- Industry precedent documentation for deferred safety/compliance work

**Total Duration:** 5-10 minutes (comprehensive research cycle)

### **Required Resources**
- Access to OpenAI, Anthropic, Google LLM documentation on system prompt best practices
- Motivational Interviewing and CBT framework documentation
- ROME IV criteria, Bristol Stool Chart standards, FODMAP research
- Access to clinical AI application interfaces/documentation (Isabel, Ada Health, UpToDate)
- Access to GI management app structures (MyGiHealth, Oshi Health, Cara Care, Monash FODMAP)
- Medical imaging AI confidence scoring research literature
- **Current Baselines for Analysis:**
  - `prompt/roles/gastro/gastro_system.md` — Completed Blocks 1-3 for validation
  - `prompt/roles/gastro/data/profile.json` — Patient profile skeleton for schema optimization
  - `prompt/artifacts/tasks/T810/request/request_T810A-PROMPT_v1.0.0.md` — Requirements context and story specifications

## VIII. STAKEHOLDER ENGAGEMENT

### **Primary Stakeholders**
- **Client (Decision Owner):** Final approval of research scope and acceptance of recommendations
- **LLM_Consultant:** Primary consumer of research findings for T810A-PROMPT all story development (S01-S10)
- **LLM_Research:** External research agent conducting the focused investigation

### **Review & Approval Gates**
- **Research Scope Approval:** Client confirmation of research objectives and methodology (Gate 1 - Current)
- **Mid-Point Findings (Optional):** Quick checkpoint if critical gaps identified during research
- **Final Deliverable Review:** Client acceptance of research findings, pattern analysis, and implementation insights (Gate 2)

### **Integration with T810A Development**

Research findings will be integrated into T810A-PROMPT story development:
- **S01-S03 Validation:** Confirm completed blocks align with industry best practices
- **S04-S10 Development:** Industry patterns inform functional requirement specification
- **Request Enhancement:** LLM_Consultant translates research insights into F-IDs for trust-and-verify, confidence scoring, safety deferral
- **Design Phase:** Implementation insights guide block-by-block detailed design

## IX. KNOWN CONSTRAINTS & ASSUMPTIONS

### **Constraints**
- Research scope limited to information publicly available or accessible via web search
- No direct patient interviews or clinical trial data
- Gastroenterologist expert practice insights limited to published literature/case studies unless interviews available
- Research must align with ChatGPT native platform capabilities (no custom tooling in MVP per T810A-PROMPT-CON-005)

### **Assumptions**
- Industry frameworks (MI, CBT, clinical AI patterns) contain transferable insights despite not being LLM_Gastro-specific
- Multimodal confidence scoring challenges are common enough in medical AI to have established solutions
- Patient profile patterns in IBD/IBS management apps are applicable to LLM_Gastro use case
- The 9-block prompt framework from T102 consultancy translates effectively to clinical domain

## X. APPENDICES

### **A. Current Artifact References**
- **Primary Analysis Target:** `prompt/artifacts/tasks/T810/request/request_T810A-PROMPT_v1.0.0.md`
  - Section III.A (Feature Solution Framework): Decision criteria, weighting
  - Section III.B-III.I (Requirements context): Scope, objectives, NFRs, interfaces, constraints, integration notes
  - Section III.J (Stories & Specification): S01-S03 completed; S04-S10 pending development
- **System Prompt Baseline (Completed Stories):** `prompt/roles/gastro/gastro_system.md`
  - Block 1 (Project Context): Diagnostic stance, privacy stance, timezone, timestamp format
  - Block 2 (Role Identity): Persona, competencies, communication style
  - Block 3 (Toolbox): Placeholder for future custom tools
- **Patient Profile Baseline:** `prompt/roles/gastro/data/profile.json`
  - Current schema: `patient_id, triggers, relievers, medications, supplements, allergies, conditions, notes, last_updated`
- **9-Block Framework Reference:** `prompt/documentation/prompt_main.md`
- **Related Dependencies:** T810A-PROMPT-DEP-004 (Patient Profile schema deferral), T810B-TOOLS (Toolbox deferral), T810D-PROFILE (Backend integration)

### **B. Industry Standards Reference**
- **LLM Frameworks:** OpenAI GPT-4, Anthropic Claude, Google Gemini system prompt documentation
- **Clinical Interaction:** Motivational Interviewing (Miller & Rollnick), CBT (Beck Institute)
- **GI Clinical Standards:** ROME IV, Bristol Stool Chart, FODMAP (Monash), ACG/WGO guidelines
- **Medical AI:** FDA SaMD guidance, ISO 13485 (deferred context only)

### **C. Target Applications for Benchmarking**
- **Clinical AI:** Isabel, UpToDate, Ada Health, Buoy Health
- **Digital Health Coaching:** Noom, Omada Health, Virta Health
- **GI Management:** MyGiHealth, Oshi Health, Cara Care, Monash FODMAP app
- **Medical Imaging AI:** SkinVision, Aidoc (confidence scoring patterns)

### **D. Key Research Outputs by Story**

| Story ID | Research Deliverable | Expected Impact |
|:---------|:---------------------|:----------------|
| S01 (Project Context) | Governance Stance Pattern Validation | Validate diagnostic stance, privacy model, timezone/timestamp standards against clinical AI norms |
| S02 (Role Identity) | Dual-Tone Persona Validation | Confirm analytical/collaborative persona aligns with clinical coaching best practices |
| S03 (Toolbox) | Tool Deferral Approach Validation | Validate placeholder approach for future custom tool development |
| S04 (Knowledge Base) | GI Expert Practice Synthesis + Patient Profile Schema | Recommend clinical knowledge sources, profile loading patterns, expert reasoning frameworks |
| S05 (Execution Protocol) | Enhanced Analyze→Probe→Coach + Session Workflows | Validate/refine protocol, confidence scoring patterns, initialization workflows, proactive/reactive models |
| S06 (Behavioral Guardrails) | Trust-and-Verify Enforcement + Recommendation Specificity | Recommend confidence thresholds, safety boundaries, specificity guidelines |
| S07 (Quality Criteria) | Measurable Success Benchmarks | Recommend accuracy metrics, protocol adherence measures, clinical utility standards |
| S08 (Exemplars) | Confidence Communication + Interaction Pattern Examples | Provide uncertainty handling, trust-and-verify, dual-tone, initialization dialogue examples |
| S09 (I/O Specification) | Dual-Purpose Report Architecture + Profile JSON Schema | Recommend `/report` output patterns, timeline structures, memory optimization approaches |
| S10 (Metadata Header) | YAML Header Best Practices | Recommend clinical AI metadata patterns, governance keys, versioning standards |

---

**Prepared by:** LLM_Consultant
**Approval Required:** Client (Decision Owner)
**Target Start Date:** Upon approval
**Expected Completion:** 5-10 minutes from initiation
**Criticality:** **HIGH** — Blocks T810A-PROMPT Stories S04-S10 specification and development; validates completed Stories S01-S03
