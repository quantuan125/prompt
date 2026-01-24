---
artifact_type: 'BRIEF'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2-SCHEMA'
research_id: 'T810A2-RES-001'
version: '1.0.0'
iteration: '3'
date: '2025-11-15'
status: 'ready_for_commission'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: Template Format Selection & Controlled Vocabulary Extraction

## I. EXECUTIVE SUMMARY

This research brief commissions a comprehensive investigation into optimal template formats for ChatGPT Project Knowledge storage and exhaustive controlled vocabulary extraction from the Cara Care application exemplar. The research directly addresses the **CRITICAL blocker** for T810A2-SCHEMA Phase 1 F-RID finalization and Phase 2 schema development.

This research serves dual critical purposes:
1. **Part 1 (Cara Care Vocabulary Extraction)**: Systematic extraction of EXHAUSTIVE controlled vocabularies to inform **T810A-ADR-002 (Foundational Vocabulary Authority)** enhancement and enable T810A2 schema specifications
2. **Part 2 (Template Format Selection)**: Investigation of optimal template format (JSON vs. YAML vs. alternatives) for ChatGPT Project Knowledge compatibility, informed by vocabulary extraction token efficiency findings

**Critical Dependencies Addressed**:
- **T810A2-IG-002 (Template Structure & Format)**: Cannot be finalized without format recommendation
- **T810A2-IF-002 (Dynamic JSON Interface)**: Template format placeholder blocks interface specification
- **T810A2-NFR-002 (Schema Clarity)**: Self-documenting template approach requires format analysis
- **T810A2-NFR-003 (Vocabulary Completeness)**: Exhaustive vocabularies required for all categorical fields
- **T810A2-CON-002 (Vocabulary Authority)**: Cara Care exemplar as primary vocabulary source
- **Epic T810A-ADR-002-FR-001**: Foundational JSON Requirements Table enhancement
- **All Story S01-S07 specifications**: Phase 2 development blocked without vocabulary data and template format insights

**Research Output Scope**: This research provides **RECOMMENDATIONS and INSIGHTS ONLY**. The T810A2 subconsultant (LLM_Consultant) is responsible for using research findings to formulate finalized F-RID specifications, Epic ADR-002 enhancements, template drafts, and Activity 1.7 (IG) deliverables.

## II. RESEARCH SCOPE & OBJECTIVES

### **Primary Research Questions**

#### **PART 1: CARA CARE VOCABULARY EXTRACTION**

**1. Exhaustive Controlled Vocabulary Catalog**
- What are the COMPLETE controlled vocabularies used in the Cara Care application for all tracking entry types?
- Required vocabulary categories:
  - **Meal Metadata**: Descriptive tags (e.g., "chili", "oily", "sweet", "light", etc.)
  - **Stool Metadata**: Event descriptors (e.g., "urgent", "full_evacuation", "partial_evacuation", "mucus", etc.)
  - **Bristol Stool Types**: Types 0-7 with official descriptions (Type 0 = "nothing", Types 1-7 per Bristol Chart authority)
  - **Symptom Severity Scales**: Numeric scales with semantic anchor labels
    - Tummy pain (1-5): 1=no pain → 5=extreme pain (descriptive labels per level)
    - Bloating (1-5): 1=no bloating → 5=extreme bloating (descriptive labels per level)
    - Mood (-2 to +2): -2=awful, 0=neutral/so-so, +2=very good/happy (semantic anchors)
    - Stress (1-5): 1=no stress → 5=extreme stress (descriptive labels per level)
  - **Entry Type Categories**: All tracking entry types supported (meal, stool, digestion, mental state, sleep, exercise, medication, etc.)
  - **Field-Level Vocabularies**: Any additional categorical fields with controlled value sets

**2. Semantic Mapping & Clinical Validity**
- For each numeric scale (pain, bloating, mood, stress), what are the exact semantic anchor labels?
- How does Cara Care map natural language patient descriptions to numeric scale values?
- What clinical validity exists for Cara Care vocabularies? (Alignment with Bristol Chart, gastroenterology standards, validated symptom scales)
- Are there any external clinical standards referenced or incorporated? (PHQ-9, GAD-7, ROME IV criteria)

**3. Vocabulary Completeness & Schema Evolution Best Practices**
- How does Cara Care handle vocabulary evolution? (Fixed lists vs. user-extensible values)
- What vocabulary gaps exist between Cara Care and comprehensive GI tracking needs?
- Which vocabularies are REQUIRED vs. OPTIONAL for MVP T810A2 implementation?
- **Schema Evolution Best Practices**: What are recommended extensibility patterns for future development?
  - Principles for schema versioning and backward compatibility
  - Best practices for vocabulary expansion without breaking existing structures
  - Patterns for ease of integration with future features (T810A3 aggregation, external APIs)
  - Governance recommendations for controlled vocabulary maintenance and update workflows
- **NOTE**: Focus on FUTURE-ORIENTED best practices and principles, NOT Cara Care-specific historical patterns

**4. Vocabulary Documentation Format Analysis**
- How are vocabularies presented in Cara Care UI? (Dropdown lists, autocomplete, free text with suggestions)
- What documentation or help text exists for each vocabulary value?
- How are semantically related values grouped or organized?
- What naming conventions or patterns exist across vocabularies?

**5. Epic ADR-002-FR-001 Assessment & Enhancement Recommendations** (**HIGH PRIORITY**)
- **Context**: Epic T810A-ADR-002-FR-001 (Foundational JSON Requirements Table) currently defines:
  - **meal**: `ingredients` (array), `metadata` (array: ["chili", "oily", "sweet", "light", ...])
  - **stool**: `type` (0-7), `metadata` (array: ["urgent", "full_evacuation", "partial_evacuation", "mucus", ...]), `confidence` (0.0-1.0)
  - **digestion**: `tummy_pain` (1-5), `bloating` (1-5)
  - **mental**: `mood` (-2 to 2), `stress` (1-5)

- **Research Task**: ASSESS current ADR-002-FR-001 table against Cara Care exhaustive vocabulary findings and make RECOMMENDATIONS for:
  - **Additional Entry Types**: Are there entry types in Cara Care missing from ADR-002-FR-001? (e.g., sleep, exercise, medication_taken, patient_state, hydration, etc.)
  - **Additional Fields per Entry Type**: For existing entry types (meal, stool, digestion, mental), are there additional fields/keys in Cara Care that should be added to ADR-002-FR-001?
  - **Vocabulary Value Set Expansions**: Are there vocabulary values in Cara Care that expand beyond current table definitions (e.g., meal metadata beyond "chili/oily/sweet/light", stool metadata beyond "urgent/full_evacuation/partial_evacuation/mucus")?
  - **Field Data Type Refinements**: Should any field data types be refined (e.g., array → object with structured properties)?
  - **Description Requirement Additions**: Which fields require predefined descriptive labels per T810A-ADR-002-FR-002 (Critical Requirements)?

- **Deliverable**: Gap analysis table + enhancement recommendations (NOT final ADR update; T810A2 subconsultant formulates ADR enhancements post-research)

#### **PART 2: TEMPLATE FORMAT SELECTION**

**6. ChatGPT Project Knowledge Compatibility**
- What file formats does ChatGPT Project Knowledge natively support? (JSON, YAML, Markdown, plain text, etc.)
- What are the file size limits, token consumption patterns, and parsing behavior for each format?
- Does ChatGPT prefer certain formats for structured data storage and retrieval?
- What are the known limitations or compatibility issues with each format?

**7. Comment Support & HYBRID Annotation Approach**
- **JSON Format Analysis**:
  - Native comment support: None (JSON spec prohibits comments)
  - Workaround patterns: `"_comment"` keys, `"__meta"` fields, string annotations
  - Pros: Universal parsing, strict schema validation, widespread tooling support
  - Cons: No native comments (HYBRID annotations require workarounds), verbose syntax, limited readability
  - Token efficiency: Compact but with annotation overhead for HYBRID approach

- **YAML Format Analysis**:
  - Native comment support: YES (# comment syntax)
  - HYBRID annotation clarity: Inline comments directly annotate fields without structural overhead
  - Pros: Human-readable, native comments for self-documentation, concise syntax
  - Cons: Less universal tooling, potential parsing ambiguity, whitespace sensitivity
  - Token efficiency: Generally more concise than JSON, especially with comments

- **Alternative Formats**:
  - **JSONL** (JSON Lines): Single-line JSON entries for array structures
  - **JSON5**: Extended JSON with comment support, trailing commas, unquoted keys
  - **TOML**: Configuration format with native comments and structured data
  - **Hybrid Markdown + Code Blocks**: Markdown with embedded JSON/YAML code blocks

**8. LLM Parsing Reliability & Generation Accuracy**
- For each format, how reliably can LLM_Gastro:
  - **Parse** templates to understand schema structure and generation instructions?
  - **Generate** valid structured entries following template patterns?
  - **Interpret** HYBRID annotations (inline hints for complex fields)?
  - **Maintain** format consistency across multiple generation cycles?
- What error rates or failure modes exist for each format in LLM generation tasks?
- How does annotation density impact parsing accuracy? (Minimal annotations vs. exhaustive field-level guidance)

**9. Self-Documentation & Template Clarity (NFR-002)**
- Which format best supports the **dual responsibility** requirement? (Templates as both schema definition + LLM generation instructions)
- **HYBRID Annotation Patterns**:
  - **Option A: Inline Hints** — Minimal annotations for complex fields only
  - **Option B: Exhaustive Field-Level Guidance** — Every field documented inline
  - **Option C: Clean Exemplars with Separate Docs** — No inline annotations; separate schema documentation
  - **Option D: Hybrid of A+C** — Minimal inline + supplementary external schema docs
- What annotation density optimizes LLM generation reliability without excessive token overhead?
- How should annotations guide LLM behavior? (Instructional phrasing, constraint specifications, examples)

**10. Token Efficiency Impact & Platform-Informed Budget Recommendations (NFR-001)**
- **Critical Analysis**: Part 2 MUST be informed by Part 1 vocabulary extraction results AND Q11 platform constraints
- How do vocabulary token counts vary across template formats?
- What is the token overhead of each annotation approach (inline comments vs. workarounds)?
- Token count comparison matrix:
  - Stable JSON patient profile (with/without annotations)
  - Dynamic JSON entry templates (with/without annotations)
  - Controlled vocabulary catalog (inline vs. external reference)
- What optimization opportunities exist? (Field abbreviations, value compression, schema modularity)
- How does template format impact overall system token consumption? (Profile loading + generation instructions + vocabulary catalog)
- **Token Budget Recommendations**: Based on platform limits (Q11) and format analysis, what are RECOMMENDED token budgets for:
  - System prompt (total character/token allocation for LLM_Gastro prompt within platform limits)
  - Stable JSON patient profile (recommended max tokens)
  - Dynamic JSON entry templates (recommended max tokens per entry type)
  - Controlled vocabulary catalog (total token consumption estimate)
  - **CRITICAL DISCLAIMER**: Recommendations are NOT final decisions; final token budgets determined by consultant + client

**11. ChatGPT Platform Constraints** (**HIGH PRIORITY**)
- Investigate ChatGPT Project Knowledge platform limits and constraints:
  - **File Storage Limits**:
    - Maximum file size (individual file upload limit)
    - Total storage quota across all Project Knowledge files
    - Number of files limit (max files allowed)
  - **Token Limits**:
    - System prompt character/token limit (e.g., reported 8000 character limit for project system prompt)
    - Context window size (total tokens available for conversation context)
    - Maximum input tokens (per user message)
    - Maximum output tokens (per assistant response)
  - **Format Restrictions**:
    - Supported file formats for Project Knowledge uploads
    - Parsing behaviors for each format (JSON vs. YAML vs. Markdown vs. plain text)
    - Retrieval patterns (how ChatGPT accesses and parses Project Knowledge files during conversation)
  - **Update Workflows**:
    - File update mechanisms (in-place edit supported vs. replace-only workflow)
    - File versioning or history tracking
  - **Performance Characteristics**:
    - File retrieval latency (impact on conversation response time)
    - Parsing overhead (token consumption for file processing)
- **Deliverable**: Platform constraint documentation for DEP-005 validation, token budget establishment for NFR-001, template design constraints for IG-002

**12. Maintainability & Schema Evolution (NFR-005)**
- Which format best supports future schema evolution with minimal rework?
- How easily can new entry types be added?
- How can controlled vocabularies be updated without breaking existing templates?
- What version control and migration patterns exist for each format?
- How does format choice impact Story S06 (schema governance workflow) complexity?

#### **CROSS-PART INTEGRATION ANALYSIS**

**13. Vocabulary Integration with Template Format**
- Should vocabularies be:
  - **Embedded in templates** (inline value lists for each categorical field)?
  - **Referenced externally** (separate controlled vocabulary catalog file)?
  - **Hybrid approach** (common vocabularies external, entry-specific vocabularies inline)?
- How does vocabulary placement impact template token efficiency?
- What is the optimal structure for Epic T810A-ADR-002 vocabulary catalog in each format option?

**14. Cara Care Dual Processing Alignment (INT-002, NFR-004)**
- How well does each format support manual patient workflow? (Copy Dynamic JSON → save to file → upload to Project Knowledge OR enter into Cara Care app)
- Does Cara Care application expect specific JSON structure for dual processing?
- What compatibility requirements exist between T810A2 templates and Cara Care data import?
- Can templates support BOTH LLM generation AND Cara Care dual processing without format conflicts?

**15. T810A1-S05 Integration Requirements**
- **Template-Driven Architecture Context**: Templates have dual responsibility (schema + instruction manual)
- How does format choice impact T810A1-S05 tracking protocol prompt engineering?
- What level of template self-documentation is needed for S05 STEP execution without external docs?
- Should S05 Custom Instructions reference template structure, or should templates be fully self-contained?
- Integration considerations: Insights for Activity 1.8 (INT) cross-feature integration specifications

## III. DELIVERABLES

### **REQUIRED REPORT STRUCTURE**

**Deliverable**: Research Report (`report_template-format-vocabulary-extraction_T810A2-RES-001_v1.0.0.md`)

**CRITICAL**: Report MUST follow the structural exemplar provided in:
- `prompt/artifacts/tasks/T810/research/report/report_T810A1-PROMPT_s05-execution-protocol-clinical-validation.md`

**Report shall include the following sections**:

#### **Section I: Executive Summary**
- Brief overview of research findings across both parts
- Key insights for T810A2-SCHEMA F-RID finalization and Phase 2 development
- Critical recommendations summary

#### **Section II: Deliverable A — Cara Care Vocabulary Extraction**
- **A.1**: Exhaustive Controlled Vocabulary Catalog
  - Complete vocabulary tables for all tracking entry types
  - Meal metadata value set with descriptions
  - Stool metadata value set with descriptions
  - Bristol Stool Types 0-7 with official descriptions
  - Symptom severity scales with semantic anchor labels (pain, bloating, mood, stress)
  - Entry type categories enumeration
  - Field-level categorical vocabularies
- **A.2**: Semantic Mapping & Clinical Validity Analysis
  - Numeric scale → descriptive label mappings
  - Natural language → scale value mapping patterns
  - Clinical validity assessment (Bristol Chart alignment, gastroenterology standards)
  - External clinical standard references (PHQ-9, GAD-7, ROME IV where applicable)
- **A.3**: Vocabulary Completeness & Schema Evolution Best Practices
  - Fixed lists vs. extensible values analysis
  - Vocabulary gap identification
  - REQUIRED vs. OPTIONAL vocabularies for MVP
  - **Schema Evolution Best Practices**: Extensibility principles, versioning patterns, backward compatibility recommendations, governance protocols for future development
- **A.4**: Vocabulary Documentation Format Best Practices
  - Cara Care UI presentation patterns
  - Documentation and help text examples
  - Semantic grouping and organization patterns
  - Naming conventions
- **A.5**: Epic ADR-002-FR-001 Assessment & Enhancement Recommendations (**HIGH PRIORITY**)
  - Current ADR-002-FR-001 table review (meal, stool, digestion, mental entry types)
  - Gap analysis: Additional entry types in Cara Care (sleep, exercise, medication_taken, patient_state, etc.)
  - Gap analysis: Additional fields per existing entry type
  - Gap analysis: Vocabulary value set expansions beyond current table
  - Enhancement recommendations table with rationale
  - **NOTE**: Recommendations ONLY (T810A2 subconsultant formulates final ADR enhancements)

#### **Section III: Deliverable B — Template Format Analysis**
- **B.1**: ChatGPT Project Knowledge Compatibility Matrix
  - Supported formats with file size limits and token consumption
  - Parsing behavior and retrieval patterns for each format
  - Known limitations and compatibility issues
- **B.2**: Comment Support & HYBRID Annotation Comparison
  - JSON format analysis (comment workarounds, pros/cons, token efficiency)
  - YAML format analysis (native comments, pros/cons, token efficiency)
  - Alternative formats evaluation (JSONL, JSON5, TOML, Markdown hybrid)
  - HYBRID annotation pattern comparison (inline hints vs. exhaustive vs. clean exemplars vs. hybrid)
- **B.3**: LLM Parsing Reliability & Generation Accuracy Assessment
  - Format-specific parsing reliability analysis
  - Generation accuracy and error rates
  - Annotation density impact on parsing
  - Format consistency maintenance analysis
- **B.4**: Self-Documentation & Template Clarity Assessment
  - Dual responsibility support evaluation (schema + instructions)
  - Annotation density optimization insights
  - LLM behavior guidance patterns
  - NFR-002 (Schema Clarity) compliance evaluation
- **B.5**: Token Efficiency Impact & Platform-Informed Budget Recommendations
  - Vocabulary token count comparison across formats (informed by Part 1)
  - Annotation overhead quantification
  - Token count comparison matrix (Stable JSON, Dynamic JSON, vocabulary catalog)
  - Optimization opportunities identification
  - System-wide token consumption projection
  - **Token Budget Recommendations** (informed by B.6 platform limits):
    - System prompt recommended allocation
    - Stable JSON recommended max tokens
    - Dynamic JSON entry recommended max tokens per type
    - Vocabulary catalog estimated tokens
    - **DISCLAIMER**: "These token budget recommendations are NOT final decisions. Final token budgets will be determined collaboratively by the T810A2 subconsultant and client based on this data, platform constraints, and operational requirements."
- **B.6**: ChatGPT Platform Constraints Documentation (**HIGH PRIORITY**)
  - File storage limits (max file size, total quota, number of files)
  - Token limits (system prompt limit, context window, input/output maximums)
  - Format restrictions (supported formats, parsing behaviors, retrieval patterns)
  - Update workflows (in-place edit vs. replace-only)
  - Performance characteristics (retrieval latency, parsing overhead)
- **B.7**: Maintainability & Schema Evolution Analysis
  - Future schema evolution support assessment
  - New entry type addition complexity
  - Vocabulary update patterns
  - Version control and migration patterns
  - Story S06 (schema governance) impact analysis

#### **Section IV: Deliverable C — Cross-Part Integration Analysis**
- **C.1**: Vocabulary Integration with Template Format
  - Embedded vs. external vs. hybrid vocabulary placement analysis
  - Token efficiency impact of placement strategy
  - Epic T810A-ADR-002 vocabulary catalog structure considerations for each format option
- **C.2**: Cara Care Dual Processing Alignment
  - Manual patient workflow support evaluation
  - Cara Care JSON structure compatibility assessment
  - Template format dual-purpose support (LLM generation + Cara Care import)
  - Format conflict identification and mitigation strategies
- **C.3**: T810A1-S05 Integration Insights
  - Template-driven architecture alignment assessment
  - S05 tracking protocol prompt engineering impact
  - Template self-documentation sufficiency for S05 STEPS
  - S05 Custom Instructions vs. template self-contained guidance trade-off analysis
  - **NOTE**: Insights inform Activity 1.8 (INT) cross-feature integration specifications

#### **Section V: Integrated Recommendations**
- **Recommendation 1: Controlled Vocabulary Catalog Data for T810A-ADR-002 Enhancement**
  - Exhaustive vocabulary tables ready for Epic governance population (raw data, not formatted ADR)
  - Semantic mappings and clinical validity documentation
  - Schema evolution best practices and governance protocols
  - ADR-002-FR-001 enhancement recommendations (gap analysis + rationale)

- **Recommendation 2: Template Format Selection**
  - PRIMARY recommendation: JSON vs. YAML vs. Alternative format with rationale
  - ChatGPT compatibility assessment, comment support analysis, token efficiency data, LLM reliability findings
  - HYBRID annotation approach recommendation: Inline hints vs. exhaustive vs. clean exemplars
  - Trade-off analysis: Pros/cons matrix with weighted criteria

- **Recommendation 3: Template Structure & Annotation Patterns**
  - Recommended annotation density (minimal vs. exhaustive field-level) with supporting evidence
  - Template dual responsibility implementation insights (schema + instructions)
  - Instructional annotation phrasing guidelines
  - External documentation needs assessment (if any)

- **Recommendation 4: Vocabulary Placement Strategy**
  - Embedded vs. external vocabulary catalog recommendation with rationale
  - Epic T810A-ADR-002 catalog format and structure insights
  - Vocabulary versioning and update workflow considerations

- **Recommendation 5: Token Budget Recommendations**
  - Platform-informed token budget recommendations (system prompt, Stable JSON, Dynamic JSON, vocabulary catalog)
  - Optimization strategies for token efficiency
  - **DISCLAIMER**: "These are recommendations only. Final token budgets determined by consultant + client."

- **Recommendation 6: T810A2 F-RID Enhancement Insights**
  - IG-001 (Null Handling): Insights on null handling patterns from format analysis
  - IG-002 (Template Format): PRIMARY insights for format selection and HYBRID approach
  - IG-003 (Vocabulary Docs): Documentation standard insights from Cara Care analysis
  - IG-004 (Manual Workflow): Workflow considerations based on format choice
  - IF-002 (Dynamic JSON Interface): Interface recommendations informed by vocabulary data
  - IF-003 (Controlled Vocabulary Interface): Access pattern insights
  - NFR-001, NFR-002, NFR-003, NFR-004, NFR-005: Validation data and optimization insights

## IV. RESEARCH METHODOLOGY

### **A. Cara Care Application Analysis**

**Primary Research Methods**:
- **Systematic UI Exploration**: Comprehensive walkthrough of Cara Care application tracking workflows
  - Meal tracking interface and metadata vocabularies
  - Stool tracking interface and Bristol Chart implementation
  - Symptom tracking interfaces (pain, bloating, stress, mood scales)
  - Mental state and contextual tracking features
  - Additional entry types (sleep, exercise, medication, hydration, patient state if present)

- **Resource Extraction**:
  - Analyze provided Cara Care screenshots:
    - `prompt/artifacts/tasks/T810/resources/carecare_meal_tracking.jpeg`
    - `prompt/artifacts/tasks/T810/resources/carecare_symptoms_tracking.jpeg`
  - Extract visible vocabulary values, scale labels, UI patterns
  - Identify entry types and field structures

- **Documentation Review**:
  - Cara Care app help documentation (if accessible)
  - Cara Care published research or clinical validation studies
  - Third-party Cara Care reviews or usage guides

- **Comparative Analysis**:
  - Compare extracted vocabularies against Bristol Stool Chart authority
  - Validate against gastroenterology clinical standards (ROME IV, ACG/AGA guidelines)
  - Cross-reference with example tracking JSON: `prompt/artifacts/tasks/T810/resources/gastro_example_tracking.json`
  - **ADR-002-FR-001 Gap Analysis**: Compare Cara Care findings against existing Epic ADR-002-FR-001 table to identify enhancement opportunities

**Exhaustiveness Criteria**:
- ALL categorical fields must have complete value set enumeration
- ALL numeric scales must have semantic anchor labels documented
- ALL entry types must be identified with field inventories
- Vocabulary completeness validated against T810A2-NFR-003 requirement

### **B. Template Format Investigation**

**ChatGPT Project Knowledge Research**:
- **Official Documentation**: ChatGPT Project Knowledge file format specifications, platform limits documentation
- **Community Knowledge**: Best practices from ChatGPT power users and developers; reported platform constraints
- **Empirical Testing** (if possible):
  - Upload sample JSON, YAML, and alternative format files to Project Knowledge
  - Test LLM retrieval, parsing, and generation accuracy for each format
  - Measure token consumption for identical content across formats

**Format Comparison Framework**:
- **Criteria Matrix**:
  1. Comment support (native vs. workarounds)
  2. LLM parsing reliability (accuracy rate)
  3. LLM generation consistency (format maintenance)
  4. Token efficiency (vocabulary overhead, annotation overhead)
  5. Human readability (maintainability)
  6. Schema evolution support (extensibility)
  7. ChatGPT compatibility (native support vs. limitations)
  8. Dual processing support (Cara Care import compatibility)

- **Weighted Scoring**: Criteria weighted by T810A2 priorities:
  - CRITICAL: ChatGPT compatibility, LLM reliability, token efficiency, platform constraints
  - HIGH: Comment support (HYBRID approach), dual processing support
  - MEDIUM: Human readability, schema evolution

**HYBRID Annotation Testing** (if feasible):
- Test sample templates with varying annotation densities
- Measure LLM generation accuracy vs. annotation overhead
- Identify optimal annotation density for NFR-002 (Schema Clarity) + NFR-001 (Token Efficiency) balance

### **C. Literature & Standards Review**

**Clinical Standards**:
- **Bristol Stool Chart**: Official descriptions for Types 0-7
- **Gastroenterology Severity Scales**: Validated symptom severity scales (pain, bloating)
- **Mental Health Scales**: PHQ-9 (depression), GAD-7 (anxiety) if Cara Care incorporates

**JSON/YAML/Data Format Standards**:
- JSON specification (RFC 8259)
- YAML specification (YAML 1.2)
- ChatGPT Project Knowledge format documentation
- LLM-friendly data format best practices (if available)

**Platform Constraints Research**:
- ChatGPT official documentation for Project Knowledge limits
- Community-reported platform constraints and workarounds
- Token limit specifications (system prompt, context window, input/output)

**T810A2 Governance & Requirements**:
- Plan file (`plan_T810A2-SCHEMA_phase0-4.md`)
- Proposal file (`proposal_T810A2-SCHEMA_phase1.md`)
- Request document (`request_T810A2-SCHEMA.md`)
- Epic T810A-ADR-002 (Foundational Vocabulary Authority) specification in Concept document

## V. CRITICAL DEPENDENCIES & CONTEXT

### **Current State Challenges**

The research directly addresses **CRITICAL blockers** for T810A2-SCHEMA development:

1. **IG-002 (Template Format) Dependency**: Cannot finalize Activity 1.7 (Implementation Guidance) without template format recommendation. IG-002 blocked awaiting RES-001 Part 2 findings.

2. **Vocabulary Catalog Gap**: T810A2-NFR-003 (Vocabulary Completeness) requires exhaustive controlled vocabularies for ALL categorical fields. Currently undefined which Cara Care vocabularies exist and are required for MVP.

3. **Epic ADR-002 Enhancement**: T810A-ADR-002-FR-001 (Foundational JSON Requirements Table) requires enhancement with additional entry types/fields discovered in Cara Care. Part 1 Deliverable A.5 provides gap analysis and recommendations.

4. **Platform Constraints Unknown**: DEP-005 (ChatGPT Project Knowledge Platform) requires validation; token limits impact template design and NFR-001 budgets. Part 2 Deliverable B.6 resolves this blocker.

5. **Phase 2 Development Blocker**: Stories S01-S07 cannot be developed without:
   - Complete controlled vocabulary data (Story S07 dependency)
   - Template format recommendation (Story S01 dependency)
   - Platform constraint validation (token budgets, file limits)
   - Vocabulary and format insights for schema design

6. **Token Efficiency Validation**: T810A2-NFR-001 (Token Efficiency) requires empirical token count data. Research must quantify vocabulary token consumption to inform template format selection and optimization strategies.

7. **Dual Processing Compatibility**: T810A2-INT-002 (Manual Compilation & T810A3 Aggregation) requires templates that support BOTH LLM generation AND Cara Care app data entry. Format selection must ensure compatibility.

### **Integration with T810A2 F-RIDs**

Research findings will inform T810A2 subconsultant's development of:

- **T810A2-IG-001 (Null Handling Pattern)**: Insights on null handling conventions across formats
- **T810A2-IG-002 (Template Structure & Format)**: **PRIMARY DEPENDENCY** — Format recommendation + HYBRID approach insights
- **T810A2-IG-003 (Controlled Vocabulary Documentation Standard)**: Documentation format insights from Cara Care vocabulary analysis
- **T810A2-IG-004 (Manual Export Workflow Guidance)**: Workflow considerations based on format choice
- **T810A2-IF-002 (Dynamic JSON Interface)**: Template format data removes placeholder; vocabulary integration insights
- **T810A2-IF-003 (Controlled Vocabulary Interface)**: Vocabulary placement strategy insights; Epic T810A-ADR-002 catalog structure data
- **T810A2-NFR-001 (Token Efficiency)**: Token count validation data; platform-informed budget recommendations; optimization insights
- **T810A2-NFR-002 (Schema Clarity)**: Self-documentation sufficiency assessment; HYBRID annotation effectiveness data
- **T810A2-NFR-003 (Vocabulary Completeness)**: Exhaustive vocabulary catalog data fulfills completeness requirement
- **T810A2-NFR-004 (Clinical Validity)**: Cara Care vocabularies validated against clinical standards; Bristol Chart alignment confirmed
- **T810A2-NFR-005 (Schema Extensibility)**: Schema evolution best practices; extensibility recommendations
- **T810A2-CON-002 (Vocabulary Authority)**: Cara Care as primary authority substantiated with research evidence
- **T810A2-INT-002 (Manual Compilation & T810A3 Aggregation)**: Dual processing insights; aggregation format considerations

### **Alignment with Initiative/Epic Governance**

Research must respect existing Epic governance:
- **T810A-GDR-002 (Schema Split Architecture)**: Template format must align with architectural separation (Stable = patient-managed, Dynamic = LLM-generated)
- **T810A-ADR-002 (Foundational Vocabulary Authority)**: Part 1 deliverable provides enhancement recommendations for ADR-002-FR-001; T810A2 subconsultant formulates final ADR updates
- **T810A-CON-004 (ChatGPT Architectural Constraints)**: Template format must be compatible with platform constraints (no programmatic validation, prompt-only solutions); Part 2 validates platform limits
- **T810A-IG-004 (Dynamic JSON Single-Entry)**: Templates must support single-entry generation pattern
- **T810A-QG-008 (Clarification Over Guessing)**: Vocabulary completeness enables no-guessing requirement

## VI. SUCCESS CRITERIA

The research will be considered successful if it delivers:

1. **Exhaustive Controlled Vocabulary Data**: Complete enumeration of ALL Cara Care vocabularies (meal metadata, stool metadata, Bristol types, severity scales, entry types, additional fields) with semantic mappings and clinical validity documentation. Raw vocabulary data ready for T810A2 subconsultant to enhance Epic T810A-ADR-002.

2. **Epic ADR-002-FR-001 Enhancement Recommendations**: Gap analysis comparing Cara Care findings against existing Epic ADR-002-FR-001 table with enhancement recommendations (additional entry types, additional fields, vocabulary expansions, data type refinements).

3. **Template Format Recommendation with Rationale**: PRIMARY format recommendation (JSON vs. YAML vs. Alternative) with comprehensive trade-off analysis, ChatGPT compatibility validation, token efficiency quantification, and LLM reliability assessment.

4. **HYBRID Annotation Approach Insights**: Optimal annotation density recommendation (minimal inline hints vs. exhaustive field-level vs. clean exemplars) with supporting evidence and trade-off analysis.

5. **ChatGPT Platform Constraints Documentation**: Comprehensive platform limits documentation (file storage, token limits, format restrictions, update workflows, performance) for DEP-005 validation and template design.

6. **Token Efficiency Validation Data & Budget Recommendations**: Empirical token counts for Stable JSON, Dynamic JSON, and vocabulary catalog across format options. Platform-informed token budget recommendations with DISCLAIMER that final budgets determined by consultant + client.

7. **Schema Evolution Best Practices**: Future-oriented extensibility principles, versioning patterns, backward compatibility recommendations, governance protocols (NOT Cara Care-specific historical analysis).

8. **Vocabulary Placement Strategy Insights**: Embedded vs. external vocabulary catalog recommendation with Epic T810A-ADR-002 structure considerations and versioning workflow insights.

9. **Cara Care Dual Processing Compatibility Assessment**: Template format options evaluated for manual patient workflow support (copy Dynamic JSON → save to file → upload OR enter into Cara Care app).

10. **IG-002 Finalization Enablement**: Research findings sufficient to enable T810A2 subconsultant to finalize T810A2-IG-002 (Template Structure & Format) with normative SHALL/SHOULD specifications per Activity 1.7 requirements.

11. **T810A2 F-RID Enhancement Data**: All vocabulary and format dependencies resolved; comprehensive insights provided to enhance/clarify existing F-RIDs (IG, IF, NFR, CON, INT categories).

12. **Story S01-S07 Development Readiness**: All vocabulary data, platform constraints, and format insights delivered; Phase 2 schema development can proceed with T810A2 subconsultant creating finalized specifications.

## VII. TIMELINE & RESOURCES

### **Research Duration**
- **Target**: 10-15 minutes (comprehensive research cycle covering both parts with sequential execution)
- **Priority**: **CRITICAL** — Blocks Activity 1.7 (IG) finalization, blocks Phase 2 (Schema Development & Validation), blocks Story S01-S07 specifications

### **Sequential Execution Order**
- **Phase 1: Cara Care Vocabulary Extraction** (5-7 minutes)
  - Vocabulary catalog data development
  - Semantic mapping and clinical validation
  - Epic ADR-002-FR-001 gap analysis
  - Schema evolution best practices research
  - Token count baseline establishment

- **Phase 2: Template Format Selection** (5-8 minutes)
  - ChatGPT platform constraints investigation
  - Format comparison analysis INFORMED by Phase 1 token data
  - HYBRID annotation testing
  - Platform-informed token budget recommendations
  - Recommendation synthesis

### **Required Resources**
- Access to Cara Care application screenshots:
  - `prompt/artifacts/tasks/T810/resources/carecare_meal_tracking.jpeg`
  - `prompt/artifacts/tasks/T810/resources/carecare_symptoms_tracking.jpeg`

- Access to example tracking JSON:
  - `prompt/artifacts/tasks/T810/resources/gastro_example_tracking.json`

- Access to T810A2 governance documents:
  - Plan file (`plan_T810A2-SCHEMA_phase0-4.md`)
  - Proposal file (`proposal_T810A2-SCHEMA_phase1.md`)
  - Request file (`request_T810A2-SCHEMA.md`)

- Access to Epic T810A:
  - Concept file (`concept_T810-GASTRO.md`) Section III.B.2.i — T810A-ADR-002-FR-001 (Foundational JSON Requirements Table)
  - Governance file (`sps_T810-GASTRO.md`)

- Access to Bristol Stool Chart official documentation
- Access to ChatGPT Project Knowledge format documentation and platform limits
- Access to JSON/YAML specification standards

## VIII. STAKEHOLDER ENGAGEMENT

### **Primary Stakeholders**
- **Client (Decision Owner)**: Final approval of research scope and acceptance of findings
- **LLM_Consultant (T810A2 Subconsultant)**: Primary consumer of research findings; responsible for using research insights to finalize Activity 1.7 (IG) F-RIDs, enhance Epic ADR-002, create template drafts, and enhance existing F-RIDs
- **LLM_Research**: External research agent conducting the focused investigation; delivers recommendations and insights ONLY (not finalized F-RIDs or ADR updates)

### **Review & Approval Gates**
- **Research Scope Approval**: Client confirmation of research objectives and methodology (Gate 1 - Current)
- **Final Deliverable Review**: Client acceptance of integrated research findings (Gate 2)

### **Integration with T810A2 Development**

Research findings will be integrated into T810A2 consultancy workflow per Activity 1.9 subactivity structure:
- **Activity 1.9 Commission**: RES-001 commissioned NOW; research execution by LLM_Research
- **Activity 1.9 Subactivity (Post-Research)**: T810A2 subconsultant reviews research report and makes enhancements:
  1. Review entire RES-001 research report
  2. Enhance existing F-RIDs in proposal file (Activities 1.1-1.6 completed F-RIDs: ASSUM, DEP, NFR, IF, CON)
  3. Enhance Epic T810A-ADR-002-FR-001 using vocabulary data and gap analysis recommendations
  4. Document impacts/dependencies for Activity 1.7 (IG) and Activity 1.8 (INT)
  5. Mark Activity 1.9 COMPLETE
- **Activity 1.7 Finalization**: T810A2 subconsultant uses RES-001 insights to finalize IG-001, IG-002, IG-003, IG-004 and create concrete template drafts for `prompt\roles\gastro\data`
- **Activity 1.8 (INT)**: Proceeds after Activity 1.7 finalization; T810A1-S05 integration insights inform INT specifications
- **Phase 2 Initialization**: T810A2 subconsultant develops Phase 2 schema specifications informed by RES-001
- **Checkpoint 1**: T810A Epic consultant reviews all Phase 1 F-RIDs with RES-001 findings integrated

## IX. KNOWN CONSTRAINTS & ASSUMPTIONS

### **Constraints**
- Research scope limited to information publicly available or accessible via web search
- Cara Care application access limited to screenshots and documentation (no direct app usage assumed)
- No programmatic validation or code execution for template testing (per T810A-CON-004)
- Research must align with ChatGPT native platform capabilities
- Template format must support manual patient workflow (no automated backend for MVP)
- Single research execution without intermediate checkpoints (per client directive)

### **Assumptions**
- Cara Care application vocabularies are clinically sufficient for MVP T810A2 tracking needs
- ChatGPT Project Knowledge format preferences and platform limits can be inferred from documentation and community knowledge
- Template format choice can be validated qualitatively without extensive empirical LLM generation testing
- Vocabulary token efficiency from Part 1 provides sufficient data for Part 2 format selection
- T810A2 subconsultant will use research insights to develop finalized F-RID specifications, Epic ADR-002 enhancements, and template drafts post-research completion
- Epic T810A-ADR-002-FR-001 current state (meal, stool, digestion, mental entries) represents approved baseline for gap analysis

## X. APPENDICES

### **A. Related T810A2 Documents**

**Primary Planning Document**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/workspace/plan/T810A/T810A2/plan_T810A2-SCHEMA_phase0-4.md`
- **Key Sections**: Activity 1.7 (lines 701-755), Activity 1.9 (lines 790-900+)

**T810A2 Proposal Document**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A2/proposal_T810A2-SCHEMA_phase1.md`
- **Key Sections**: All F-RID categories (ASSUM, DEP, NFR, IF, CON), Section IX (Research & Notes Preview)

**T810A2 Request Document**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md`
- **Key Dependencies**: NFR-001 (Token Efficiency), NFR-002 (Schema Clarity), NFR-003 (Vocabulary Completeness), NFR-004 (Clinical Validity), NFR-005 (Schema Extensibility)

***T810A Epic Related Documents**
- Governance: `prompt\artifacts\tasks\T810\consultant\sps\sps_T810-GASTRO.md`
- Architecture Decisions: `prompt\artifacts\tasks\T810\consultant\concept\concept_T810-GASTRO.md`

### **B. Reference Examples**

**Cara Care Resources** (CRITICAL for Part 1 analysis):
- `prompt/artifacts/tasks/T810/resources/carecare_meal_tracking.jpeg` (meal tracking UI and metadata vocabularies)
- `prompt/artifacts/tasks/T810/resources/carecare_symptoms_tracking.jpeg` (symptom tracking UI and severity scales)
- `prompt/artifacts/tasks/T810/resources/gastro_example_tracking.json` (example tracking JSON structure)

### **C. Report Structure Exemplar**

**CRITICAL**: Research report MUST use the following structural exemplar:
- **Path**: `prompt/artifacts/tasks/T810/research/report/report_T810A1-PROMPT_s05-execution-protocol-clinical-validation.md`
- **Purpose**: Ensures consistency with previous T810A research deliverables
- **Note to LLM_Research**: Review exemplar structure before drafting report; mirror section organization, heading levels, depth of analysis, and deliverable format (Deliverable A, B, C, etc.)

### **D. Epic Governance References**

**T810A-ADR-002 (Foundational Vocabulary Authority)** — APPROVED:
- **Path**: `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md` Section III.B.2.i
- **Status**: Approved (per Activity 1.7 QA)
- **Current ADR-002-FR-001 Table** (lines 117-130):
  - meal: `ingredients` (array), `metadata` (array)
  - stool: `type` (0-7), `metadata` (array), `confidence` (0.0-1.0)
  - digestion: `tummy_pain` (1-5), `bloating` (1-5)
  - mental: `mood` (-2 to 2), `stress` (1-5)
- **Research Output**: Part 1 Deliverable A.5 provides gap analysis and enhancement recommendations for this table; T810A2 subconsultant formulates final ADR updates post-research

**T810A-GDR-002 (Schema Split Architecture)**:
- **Path**: `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md` Section III.C.1
- **Relevance**: Architectural constraints for template format selection

**T810A-CON-004 (ChatGPT Architectural Constraints)**:
- **Relevance**: Platform compatibility validation for template format choice; platform constraints investigation (Part 2 Deliverable B.6)

---

**Prepared by:** LLM_Consultant (T810A2 Subconsultant)
**Approval Required:** Client (Decision Owner)
**Target Start Date:** Upon approval (Activity 1.9 immediate commissioning)
**Expected Completion:** 10-15 minutes from initiation (Part 1: 5-7 min, Part 2: 5-8 min)
**Criticality:** **CRITICAL** — Blocks Activity 1.7 (IG) finalization, blocks Phase 2 (Schema Development & Validation), blocks Story S01-S07 specifications, enables T810A-ADR-002 Epic governance enhancement
**Status:** **READY FOR COMMISSION**
