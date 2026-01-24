---
artifact_type: 'RESEARCH'
initiative_id: 'T801'
epic_id: 'T801A'
research_id: 'T801A-RES-001'
version: '1.0.0'
iteration: '1'
date: '2025-11-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: Backend TTI Architecture Design

## I. EXECUTIVE SUMMARY

This research brief commissions a **comprehensive, undergraduate-level investigation** into backend TTI (Timeframe Trend Identification) architecture design to inform Epic T801A (Backend TTI Migration) E-RID/E-GDR/E-ADR development. The research aims to resolve four critical architectural unknowns: (1) numeric scoring system design, (2) backend TTI file format selection, (3) price action detection methodology, and (4) divergence/crossover detection feasibility. This research directly addresses the shift from LLM-based TTI generation (current state: unreliable, subjective, slow) to a hybrid architecture where backend provides deterministic calculation and LLM adds interpretive context.

**Target Deliverable**: Comprehensive research report (Standard to Maximum quality) with actionable recommendations, comparative analysis tables, implementation guidance, and validation approaches for each topic to inform E-GDRs (governance decisions) and paired E-ADRs (architectural specifications).

**Scope**: Epic T801A (Backend TTI Migration) only. Initiative-level indicator design standards addressed in separate brief (T801-RES-001).

## II. RESEARCH SCOPE & OBJECTIVES

### **Primary Research Questions**

#### **Topic 1: [P1] Numeric Scoring System Design**

**Problem Context**: Current TTI protocol produces subjective BEARISH/NEUTRAL/BULLISH classifications via LLM semantic interpretation. This leads to inconsistency (same indicator values → different assessments across runs) and unreliability (doesn't follow timeframe-specific rules like S_VWAP priority in 1H vs W_VWAP in 4H).

**Research Objective**: Design a numeric scoring system that deterministically maps indicator values to trend classifications for backend implementation.

**Specific Questions**:
1. **Scoring Scale Options**:
   - What numeric scales are industry-standard for trend scoring (e.g., -2 to +2, 0-100, weighted composite, ternary classification)?
   - Comparative analysis: Pros/cons of each scale for maintainability, interpretability, and LLM consumption ease?
   - Recommendation: Which scale best fits hybrid backend → LLM architecture?

2. **Calculation Methodology**:
   - How to aggregate individual indicator scores into overall trend score?
   - Weighting strategies: Equal weights vs timeframe-specific priority (e.g., S_VWAP higher weight in 1H)?
   - Rules-based classification vs threshold-based vs weighted sums — which methodology is most robust?

3. **BEARISH/NEUTRAL/BULLISH Threshold Calibration**:
   - Industry-standard thresholds for classification boundaries (e.g., score < -1 = BEARISH, -1 to +1 = NEUTRAL, > +1 = BULLISH)?
   - Dynamic threshold adjustment strategies (e.g., based on market volatility, timeframe)?
   - How to handle edge cases (score = exactly 0, conflicting indicators)?

4. **Validation Approach**:
   - How to validate scoring system reliability (backtesting against historical data, manual trader review, hybrid)?
   - Acceptance criteria for production cutover (e.g., 90% agreement with trader's manual TTI classification)?
   - Ongoing calibration methodology (periodic review, feedback loop integration)?

**Deliverable**: Recommended scoring rubric with:
- Chosen numeric scale with rationale
- Calculation formula (aggregation logic, weighting strategy)
- Threshold mapping (numeric scores → BEARISH/NEUTRAL/BULLISH)
- Validation methodology with acceptance criteria
- Implementation guidance (configuration structure, extensibility for new indicators)

---

#### **Topic 2: [P2] Backend TTI File Format Selection**

**Problem Context**: Backend will generate TTI output file consumed by LLM_Trader (trader manually attaches file in chat). File format impacts: (1) LLM consumption ease, (2) human readability for manual override, (3) maintainability for schema updates, (4) schema validation capability.

**Research Objective**: Compare file format options (JSON, YAML, Markdown, hybrid combinations) and recommend optimal format for hybrid backend → LLM architecture.

**Specific Questions**:
1. **Format Comparison**:
   - **JSON**: Pros/cons for LLM parsing, human editability, schema validation (JSON Schema)?
   - **YAML**: Pros/cons for readability, manual override workflow, validation tooling?
   - **Markdown**: Pros/cons for LLM consumption (direct semantic parsing), human readability, structured data representation?
   - **Hybrid** (e.g., YAML frontmatter + Markdown body, JSON + Markdown sections): When is hybrid warranted?

2. **Evaluation Criteria**:
   - **LLM Consumption Ease**: Which format allows LLM to extract TTI data most reliably (minimal hallucination risk, clear structure)?
   - **Human Readability/Editability**: Which format supports trader manual override workflow (quick edits, clear indicator presentation)?
   - **Maintainability**: Which format supports schema evolution (add new indicators, change scoring logic) without breaking backward compatibility?
   - **Schema Validation**: Which format allows automated validation before LLM consumption (detect malformed overrides, enforce required fields)?

3. **Schema Structure**:
   - Required fields: Indicator values (raw + scored), overall trend score, classification (BEARISH/NEUTRAL/BULLISH), confidence flag, metadata (timestamp, timeframe, version)?
   - Optional fields: Divergence signals, crossover events, price action markers, manual override notes?
   - Nested structure vs flat structure: Trade-offs for LLM parsing and human readability?

4. **Implementation Guidance**:
   - Example schema for recommended format (complete structure with all required/optional fields)
   - Versioning strategy (schema version tracking, backward compatibility approach)
   - Manual override workflow design (how trader edits file, validation before LLM ingestion)

**Deliverable**: Recommended file format with:
- Format selection (JSON/YAML/Markdown/Hybrid) with comparative analysis table
- Complete schema structure example
- Evaluation criteria scoring matrix (format × criteria → score + rationale)
- Implementation guidance (validation tooling, override workflow, versioning)
- LLM consumption pattern recommendation (how prompt should reference TTI file)

---

#### **Topic 3: [P3] Price Action Detection Methodology**

**Problem Context**: Current TTI protocol includes "PA" (Price Action) field showing MSB (Market Structure Break), CHOCH (Change of Character), BOS (Break of Structure) signals, but these are LLM-interpreted from insufficient data. Trader wants backend to detect price action signals algorithmically or provide foundation (swing points) for LLM interpretation. Key constraint: Avoid overly complex algorithms that sacrifice reliability.

**Research Objective**: Evaluate price action detection approaches for backend implementation and recommend MVP boundary (what backend calculates vs what LLM interprets).

**Specific Questions**:
1. **Algorithmic Detection Feasibility**:
   - Can MSB/CHOCH/BOS be reliably detected algorithmically in backend (without LLM)?
   - Complexity vs reliability analysis: What's required for algorithmic detection (swing point tracking, volume patterns, structural markers)?
   - Industry-standard algorithms for price action detection: Do robust, well-tested approaches exist?

2. **Alternative PA Approaches**:
   - **Swing Point Tracking Only**: Backend identifies swing highs/lows → LLM labels MSB/CHOCH/BOS semantics (hybrid approach)
   - **Threshold-Based Signals**: Backend detects simple conditions (e.g., price closes above last swing high → potential BOS signal) → LLM interprets context
   - **Hybrid Backend + LLM**: Backend provides swing points + threshold signals → LLM adds semantic labeling (MSB/CHOCH/BOS classification)

3. **Data Requirements**:
   - What data is needed for each approach (swing points, volume patterns, structural markers)?
   - Current TradingView CSV data sufficiency: Does master.csv provide required data or does PineScript need enhancement?
   - Missing data gaps: What additional fields must PineScript export?

4. **MVP Boundary Recommendation**:
   - What should backend deterministically calculate (swing points, thresholds, basic signals)?
   - What should LLM interpret (MSB/CHOCH/BOS labeling, divergence context, multi-timeframe confirmation)?
   - Trade-off analysis: Backend determinism (reliability) vs LLM interpretive value (contextual nuance) for complex patterns

**Deliverable**: Recommended PA detection strategy with:
- Chosen approach (algorithmic, swing-point-only, threshold-based, hybrid) with rationale
- MVP boundary definition (backend responsibilities vs LLM responsibilities)
- Data requirements (existing CSV sufficiency, PineScript enhancement needs)
- Implementation guidance (algorithm pseudo-code if applicable, swing point tracking logic)
- Deferral strategy (what PA complexity to defer to future phases)

---

#### **Topic 4: [P4] Divergence & Crossover Detection Feasibility**

**Problem Context**: TTI protocol benefits from detecting divergence patterns (RSI divergence: hidden/regular bullish/bearish) and crossover events (EMA golden cross, death cross, dynamic support/resistance). Current LLM-based approach is unreliable. Question: Should backend detect these patterns algorithmically or defer to LLM interpretation?

**Research Objective**: Assess divergence and crossover detection feasibility for backend implementation and recommend MVP scope with deferral strategy for complex patterns.

**Specific Questions**:
1. **RSI Divergence Detection Algorithms**:
   - Industry-standard algorithms for detecting regular bullish/bearish divergence (price makes lower low, RSI makes higher low)?
   - Hidden divergence detection complexity (price makes higher low, RSI makes lower low)?
   - Algorithm reliability: Do robust, well-tested approaches exist or is this pattern recognition inherently subjective?

2. **EMA Crossover Detection Patterns**:
   - Simple crossover detection (EMA_9 crosses EMA_21): Straightforward algorithmic implementation?
   - Golden cross (short-term MA crosses above long-term MA) / Death cross (opposite): Industry-standard definitions and detection logic?
   - Dynamic support/resistance (price crosses EMA): Threshold-based signal detection feasibility?

3. **MVP Boundary Recommendation**:
   - What should backend calculate (simple crossovers, straightforward divergence patterns)?
   - What should LLM interpret (complex multi-timeframe divergence confirmation, contextual significance of crossovers)?
   - Complexity threshold: At what point does algorithmic detection sacrifice reliability for marginal determinism gain?

4. **Trade-off Analysis**:
   - **Backend Determinism Value**: Consistent divergence/crossover detection across runs → reliability gain
   - **LLM Interpretive Value**: Multi-timeframe context, trader-specific pattern preferences, edge case handling → contextual nuance
   - **Implementation Cost**: Algorithm complexity, maintenance burden, testing requirements
   - Recommendation: Where is the optimal balance for MVP?

**Deliverable**: Recommended MVP scope with:
- What backend should detect (specific divergence/crossover patterns with implementation feasibility assessment)
- What LLM should interpret (complex patterns, contextual analysis)
- Deferral strategy (what to defer to future phases with rationale)
- Trade-off analysis table (pattern × backend feasibility × LLM value × recommendation)
- Implementation guidance (algorithm pseudo-code for approved patterns, LLM prompt structure for interpretive layer)

---

### **Cross-Topic Integration Analysis**

**Integration Objective**: Ensure the four research topics produce a **cohesive backend architecture** rather than isolated recommendations.

**Key Integration Questions**:
1. **Scoring System ↔ File Format**:
   - How does chosen scoring scale (Topic 1) influence file format schema (Topic 2)?
   - If file format is JSON with strict schema, does scoring system need standardized output structure?

2. **PA Detection ↔ File Format**:
   - How are swing points, MSB/CHOCH/BOS signals represented in TTI file (Topic 3 output → Topic 2 schema)?
   - If PA detection is hybrid (backend swing points + LLM labeling), how does file structure support this?

3. **Divergence/Crossover ↔ Scoring System**:
   - If backend detects divergence/crossovers (Topic 4), how do these signals integrate into overall trend score (Topic 1)?
   - Weighting strategy: How much weight do divergence/crossover signals contribute to final BEARISH/NEUTRAL/BULLISH classification?

4. **Overall Backend Architecture**:
   - Unified recommendation: How do scoring system, file format, PA detection, and divergence detection combine into single backend architecture?
   - Processing pipeline: TradingView webhook → backend TTI engine (Topics 1, 3, 4) → file generation (Topic 2) → LLM consumption
   - Extension points: How does architecture support adding new indicators, changing scoring logic, enhancing PA detection in future phases?

**Deliverable**: Cross-topic integration section in research report with:
- Integration analysis (how topics interact and influence each other)
- Unified backend architecture diagram (processing flow, component interactions)
- Cohesive implementation roadmap (how to build Topics 1-4 as integrated system, not siloed features)

---

## III. RESEARCH DELIVERABLES

### **A. Numeric Scoring System Design Report**
- **Scoring Scale Recommendation**: Chosen scale with comparative analysis (pros/cons table)
- **Calculation Formula**: Aggregation logic, weighting strategy (timeframe-specific priorities), threshold mapping
- **Validation Methodology**: Backtesting approach, acceptance criteria, ongoing calibration plan
- **Implementation Guidance**: Configuration structure (JSON/YAML for rules/thresholds), extensibility design

### **B. Backend TTI File Format Specification**
- **Format Selection**: Recommended format (JSON/YAML/Markdown/Hybrid) with evaluation criteria scoring matrix
- **Complete Schema Example**: Full structure with required/optional fields, nested vs flat design rationale
- **Manual Override Workflow**: How trader edits file, validation before LLM ingestion, override audit trail
- **Versioning Strategy**: Schema version tracking, backward compatibility approach

### **C. Price Action Detection Strategy**
- **Chosen Approach**: Algorithmic/swing-point-only/threshold-based/hybrid with rationale
- **MVP Boundary**: Backend responsibilities (swing points, basic signals) vs LLM responsibilities (MSB/CHOCH/BOS labeling)
- **Data Requirements**: CSV sufficiency analysis, PineScript enhancement needs (missing fields identification)
- **Implementation Guidance**: Algorithm pseudo-code or logic specification, deferral strategy for complex patterns

### **D. Divergence & Crossover Detection Scope**
- **MVP Pattern List**: Which divergence/crossover patterns backend should detect (simple crossovers, straightforward divergence)
- **Deferral Strategy**: Complex patterns deferred to LLM or future phases with rationale
- **Trade-off Analysis**: Pattern × backend feasibility × LLM value × recommendation table
- **Implementation Guidance**: Algorithm pseudo-code for approved patterns, LLM prompt structure for interpretive layer

### **E. Cross-Topic Integration Architecture**
- **Integration Analysis**: How scoring, file format, PA detection, divergence detection interact
- **Unified Backend Architecture Diagram**: Processing flow (webhook → TTI engine → file generation → LLM consumption)
- **Implementation Roadmap**: Phased build strategy (Topics 1-4 as integrated system)
- **Extension Points**: How to add new indicators, change scoring logic, enhance PA detection in future

### **F. E-RID/E-GDR/E-ADR Guidance**
- **E-RID Implications**: How research findings inform Quality Goals, Dependencies, Assumptions, Implementation Guidance
- **E-GDR Recommendations**: Suggested governance decisions (Hybrid Architecture, Numeric Scoring Foundation, File Format Standard)
- **E-ADR Pairing**: How each E-GDR should be paired with architectural specification ADR

---

## IV. RESEARCH METHODOLOGY

### **A. Industry Standards & Best Practices Analysis**

**Primary Sources**:
- Technical analysis literature (scoring systems, divergence detection algorithms)
- Trading system architecture patterns (backend calculation engines, indicator processing pipelines)
- File format standards (JSON Schema, YAML validation, Markdown specifications)
- Price action detection methodologies (swing point tracking, MSB/CHOCH/BOS algorithmic approaches)

**Focus Areas**:
- Industry-standard numeric scoring scales for trend determination
- File format comparative analysis (LLM consumption ease, human readability, schema validation)
- Algorithmic PA detection feasibility vs interpretive LLM approaches
- Divergence/crossover pattern recognition algorithms (reliability vs complexity trade-offs)

### **B. Comparative Analysis Framework**

**Investigation Approach**:
- **Topic 1 (Scoring)**: Compare scoring scales (pros/cons tables), evaluate calculation methodologies, assess validation approaches
- **Topic 2 (File Format)**: Compare JSON/YAML/Markdown/Hybrid against evaluation criteria (scoring matrix), analyze LLM consumption patterns
- **Topic 3 (PA Detection)**: Evaluate algorithmic vs hybrid vs LLM-only approaches, assess data requirements, define MVP boundaries
- **Topic 4 (Divergence/Crossover)**: Assess detection algorithm feasibility, analyze backend vs LLM trade-offs, recommend MVP scope with deferral strategy

### **C. Constraint Validation**

**Backend Architecture Constraints to Respect**:
- **Deterministic Consistency** (T801A-QG-001): Scoring system must produce identical output for identical input
- **Backward Compatibility** (T801A-CON-001): File format must support playground validation without production disruption
- **Manual Override Workflow** (T801A requirement): File format must be human-readable/editable with validation
- **Research-Gated Design** (T801A-CON-003): Recommendations must inform E-GDRs/ADRs, not prescribe final decisions

---

## V. CRITICAL DEPENDENCIES & CONTEXT

### **Current State Challenges**

This research directly addresses **Epic T801A foundational blocking dependencies**:

1. **TTI Unreliability (Current State)**:
   - LLM-based TTI produces inconsistent BEARISH/NEUTRAL/BULLISH classifications (same indicators → different assessments)
   - Doesn't reliably follow timeframe-specific rules (S_VWAP priority in 1H vs W_VWAP in 4H)
   - Subjective assessment logic (no deterministic scoring algorithm)

2. **Data Insufficiency**:
   - Current CSV lacks comparative trend data, price action signals (MSB/CHOCH/BOS), swing points
   - PineScript filters fail (S_VWAP appearing in daily timeframe despite filters)

3. **Performance Cost**:
   - TTI generation consumes significant LLM response time (large protocol in system prompt)

4. **Manual Override Limitation**:
   - No file-based TTI workflow exists; trader cannot manually refresh or override TTI output

### **Desired Hybrid Architecture (Target State)**

**Backend Component**:
- Deterministic calculation: Numeric scoring, rule engine, timeframe-specific weighting
- TTI file generation: Structured output (format per Topic 2 research)
- Price action foundation: Swing points, basic signals (per Topic 3 research)
- Divergence/crossover detection: MVP patterns (per Topic 4 research)

**LLM Component**:
- Consumes backend TTI file (trader manually attaches in chat)
- Interprets TTI data: Adds contextual nuance, multi-timeframe synthesis, trader-specific preferences
- Maintains higher-level protocols: CAS (Current Area Sentiment), SPP (Strategy Proposal & Planning), TEA (Trade Execution & Adjustment)

### **Integration with Epic T801A E-RID/E-GDR/E-ADR Development**

Research findings will directly inform:

- **Subphase 1.1 (Quality Goals)**:
  - T801A-QG-001 (Deterministic Consistency): Scoring algorithm must be deterministic (Topic 1 guidance)
  - T801A-QG-002 (Reliability): TTI accuracy standards (Topic 1 validation approach)
  - T801A-QG-003 (Maintainability): Configuration-driven rules (Topic 1 extensibility design)
  - T801A-QG-004 (Override-ability): Manual workflow support (Topic 2 file format editability)

- **Subphase 1.2 (Dependencies)**:
  - T801A-DEP-001 (PineScript Enhancement): Missing data fields (Topic 3 data requirements)
  - T801A-DEP-002 (tv_ingest Component): Backend integration points (cross-topic architecture)

- **Subphase 1.3 (Assumptions)**:
  - T801A-ASSUM-001 (Numeric Scoring Viability): Validation via Topic 1 research findings
  - T801A-ASSUM-002 (PA Detection Feasibility): Validation via Topic 3 research findings

- **Subphase 1.4 (Implementation Guidance)**:
  - T801A-IG-001 (Configuration-Driven Rules): Topic 1 implementation guidance (JSON/YAML configuration)
  - T801A-IG-002 (File Generation Protocol): Topic 2 schema specification
  - T801A-IG-003 (Error Handling Strategy): Topic 1 edge case handling, Topic 3 PA detection graceful degradation

- **Subphase 1.6 (E-GDR & E-ADR Development)**:
  - **T801A-GDR-001 (Hybrid TTI Architecture)** + **T801A-ADR-001**: Cross-topic integration architecture informs governance decision
  - **T801A-GDR-002 (Numeric Scoring Foundation)** + **T801A-ADR-002**: Topic 1 findings inform scoring algorithm specification
  - **T801A-GDR-004 (Backend File Format Standard)** + **T801A-ADR-004**: Topic 2 findings inform file format selection and schema

### **Alignment with Initiative T801 Governance**

Research must respect Initiative T801 context (broader TTI System beyond Epic T801A):
- **Parallel Research**: T801-RES-001 (Initiative-level: Indicator Design Standards) addresses timeframe applicability, volume indicators, confidence system
- **Cross-Epic Applicability**: Epic T801A backend architecture may inform future epics (e.g., T801B: PineScript TTI Enhancement)
- **LLM_Trader Impact**: File format and scoring system design must support future LLM_Trader prompt improvements (reduce/remove TTI protocol per Epic T801A scope)

---

## VI. SUCCESS CRITERIA

The research will be considered successful if it delivers:

1. **Numeric Scoring System (Topic 1)**:
   - ✅ Clear recommendation: Chosen numeric scale with rationale
   - ✅ Complete specification: Calculation formula, weighting strategy, threshold mapping
   - ✅ Validation approach: Backtesting methodology, acceptance criteria, calibration plan
   - ✅ Implementation guidance: Configuration structure, extensibility design

2. **Backend TTI File Format (Topic 2)**:
   - ✅ Format selection: JSON/YAML/Markdown/Hybrid with evaluation criteria scoring matrix
   - ✅ Complete schema: Required/optional fields, structure example
   - ✅ Manual override workflow: Editing process, validation approach, override audit trail
   - ✅ Versioning strategy: Schema evolution approach, backward compatibility

3. **Price Action Detection (Topic 3)**:
   - ✅ Chosen approach: Algorithmic/swing-point-only/threshold-based/hybrid with rationale
   - ✅ MVP boundary: Backend vs LLM responsibilities clearly defined
   - ✅ Data requirements: CSV sufficiency analysis, PineScript enhancement needs
   - ✅ Implementation guidance: Algorithm logic or pseudo-code, deferral strategy

4. **Divergence & Crossover Detection (Topic 4)**:
   - ✅ MVP pattern list: Which patterns backend detects, which LLM interprets
   - ✅ Deferral strategy: Complex patterns deferred with rationale
   - ✅ Trade-off analysis: Pattern × feasibility × LLM value × recommendation table
   - ✅ Implementation guidance: Algorithm pseudo-code for approved patterns

5. **Cross-Topic Integration (Integration Analysis)**:
   - ✅ Integration documentation: How Topics 1-4 interact (scoring ↔ file format, PA ↔ schema, divergence ↔ scoring)
   - ✅ Unified architecture: Processing flow diagram (webhook → TTI engine → file → LLM)
   - ✅ Implementation roadmap: Phased build strategy, extension points

6. **E-RID/E-GDR/E-ADR Alignment**:
   - ✅ E-RID implications: How findings inform Quality Goals, Dependencies, Assumptions, Implementation Guidance
   - ✅ E-GDR recommendations: Suggested governance decisions with research basis
   - ✅ Actionable path: Clear next steps for LLM_Consultant to develop E-GDRs/ADRs in Subphase 1.6

7. **Research Quality Standards**:
   - ✅ Comprehensive depth: Undergraduate-level analysis per topic (not surface-level)
   - ✅ Standard to Maximum quality: Detailed comparative analysis, industry standards cited, implementation examples
   - ✅ Actionable recommendations: Not just analysis, but clear "we recommend X because Y" guidance

---

## VII. TIMELINE & RESOURCES

### **Research Phases**

**Phase 1: Industry Standards Review** (2-3 minutes)
- Technical analysis literature (scoring systems, divergence algorithms)
- Trading system architecture patterns
- File format standards and LLM consumption best practices

**Phase 2: Topic 1 Research (Numeric Scoring)** (1-2 minutes)
- Scoring scale comparative analysis
- Calculation methodology evaluation
- Threshold calibration strategies
- Validation approach recommendations

**Phase 3: Topic 2 Research (File Format)** (1-2 minutes)
- JSON/YAML/Markdown/Hybrid comparison
- Evaluation criteria scoring matrix
- Schema structure design
- Manual override workflow specification

**Phase 4: Topic 3 Research (PA Detection)** (1-2 minutes)
- Algorithmic detection feasibility assessment
- Alternative PA approaches evaluation
- Data requirements analysis
- MVP boundary recommendation

**Phase 5: Topic 4 Research (Divergence/Crossover)** (1-2 minutes)
- RSI divergence algorithm review
- EMA crossover detection patterns
- MVP scope definition
- Trade-off analysis (backend vs LLM)

**Phase 6: Cross-Topic Integration & Synthesis** (1-2 minutes)
- Integration analysis (Topics 1-4 interactions)
- Unified backend architecture design
- E-RID/E-GDR/E-ADR guidance
- Implementation roadmap

**Total Duration:** 5-10 minutes (comprehensive research, undergraduate-level depth)

### **Required Resources**
- Technical analysis literature and trading system design patterns
- File format standards (JSON Schema, YAML, Markdown specifications)
- Price action detection methodologies
- Algorithmic divergence/crossover detection patterns
- **Quality Level**: Standard to Maximum (comprehensive, actionable, implementation-ready)

---

## VIII. STAKEHOLDER ENGAGEMENT

### **Primary Stakeholders**
- **Client (Decision Owner)**: Final approval of research scope and acceptance of recommendations; E-RID/E-GDR/E-ADR final authority
- **LLM_Consultant**: Primary consumer of research findings for Subphases 1.1-1.6 (E-RID/E-GDR/E-ADR development)
- **LLM_Research**: External research agent conducting the comprehensive investigation (5-10 minutes)

### **Review & Approval Gates**
- **Research Scope Approval** (Gate 1 - Current): Client confirmation of research objectives, topics, methodology
- **Final Deliverable Review** (Gate 2): Client acceptance of research findings and E-RID/E-GDR recommendations
- **E-GDR Integration Review** (Gate 3): Client approval of how research findings inform Subphase 1.6 governance decisions

### **Integration with Phase 1 Consultancy**

Research findings will be integrated into Phase 1 workflow:
1. **Subphase 1.0: Research Commission** (current) — Create brief → Commission with LLM_Research
2. **Parallel Development**: Subphases 1.1-1.5 (E-RID development) proceed while research runs (~10-20 minutes)
3. **Subphase 1.6: E-GDR & ADR Development** — Integrate research findings into governance decisions and architectural specifications
4. **Subphase 1.7: Phase 1 Synthesis** — Research integration summary in Phase 1 proposal document

---

## IX. KNOWN CONSTRAINTS & ASSUMPTIONS

### **Constraints**
- **Epic-Level Scope Only**: Research applies exclusively to Epic T801A (Backend TTI Migration); Initiative-level standards addressed in separate T801-RES-001 brief
- **Time-Boxed**: 5-10 minutes maximum; comprehensive depth but actionable implementation guidance prioritized over exhaustive theoretical coverage
- **Hybrid Architecture Mandate**: Research must assume hybrid backend → LLM architecture (not pure backend or pure LLM approaches)
- **Playground-First Development**: Recommendations must support isolated playground validation (backward compatibility constraint T801A-CON-001)

### **Assumptions**
- Industry-standard numeric scoring scales exist and can be adapted for TTI use case
- File format comparison can definitively recommend optimal choice based on LLM consumption ease, human readability, maintainability criteria
- Price action detection algorithmic approaches are documented (or hybrid backend + LLM approach is viable MVP)
- Divergence/crossover detection algorithms have established reliability assessments (or complexity vs reliability trade-offs are quantifiable)
- Cross-topic integration analysis will reveal cohesive backend architecture (Topics 1-4 are compatible, not conflicting)

### **Out of Scope**
- **Initiative-Level Standards**: Timeframe-specific indicator applicability, volume-based trend indicators, confidence system design (addressed in T801-RES-001)
- **LLM_Trader Prompt Redesign**: How to reduce/remove TTI protocol from LLM system prompt (Epic T801A Feature T801A3 scope, not research scope)
- **PineScript Implementation Details**: How to code swing point detection in PineScript (LLM_Developer responsibility, research provides requirements only)
- **Backend Implementation Code**: Scoring algorithm code, file generation logic (LLM_Developer responsibility, research provides specification/pseudo-code only)
- **Comprehensive Backtesting**: Full historical validation of scoring system (deferred to playground validation phase, research provides validation methodology only)

---

## X. APPENDICES

### **A. Current Artifact References**
- **Primary Context**: Conversation history from current consultancy session (Draft Problem Statement, Subphase 1.0 specifications)
- **Plan File**: `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` (v1.2.0)
- **Current TTI Protocol**: `prompt/roles/VPA/main_v2.1.md` (lines 21-55) — Current LLM-based TTI structure
- **Current CSV Structure**: `components/tv_ingest/data/BINANCE_BTCUSDT/master.csv` — TradingView webhook data
- **Governance Standards**: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (T102-ADR-004/005)

### **B. Research Topic Prioritization Rationale**

| Topic | Priority | Rationale |
|:------|:---------|:----------|
| **Topic 1: Numeric Scoring** | **P1** | Foundation for entire backend; all other topics depend on scoring system design |
| **Topic 2: File Format** | **P2** | Critical for backend → LLM handoff; impacts manual override workflow and LLM consumption ease |
| **Topic 3: PA Detection** | **P3** | High trader priority (PA signals crucial for trend determination); moderate complexity |
| **Topic 4: Divergence/Crossover** | **P4** | Lower priority for MVP (nice-to-have vs essential); complexity may justify deferral |

### **C. Expected Integration with T801-RES-001 (Initiative-Level Research)**

**T801A-RES-001 (Epic-Level)**:
- **Scope**: Backend architecture design (scoring, file format, PA detection, divergence)
- **Informs**: T801A E-GDRs/E-ADRs (Epic T801A governance and architecture)

**T801-RES-001 (Initiative-Level)**:
- **Scope**: Indicator design standards (timeframe applicability, volume indicators, confidence system)
- **Informs**: T801A Dependencies (PineScript requirements), T801A Implementation Guidance (backend processing aligned with indicator standards), Initiative T801 future work

**Cross-Research Coordination**:
- T801-RES-001 Topic 1 (Timeframe Applicability) → Informs T801A-RES-001 Topic 1 (Scoring System) weighting strategy
- T801-RES-001 Topic 3 (Confidence System) → May inform T801A-RES-001 Topic 2 (File Format) schema (confidence field inclusion)

### **D. Research Brief Lineage**

**Precedent Research Briefs**:
- **T810A-RES-001**: System Architecture & Clinical Validation (comprehensive 7-deliverable research, 20+ minutes)
- **T810A-RES-002**: Conversation-Driven Empirical Validation (gap analysis, empirical testing)
- **T810A-RES-003**: Knowledge Taxonomy & Access Patterns (surface-level platform investigation, 5-10 minutes)

**This Research (T801A-RES-001)**:
- **Type**: Comprehensive, undergraduate-level investigation (Standard to Maximum quality)
- **Scope**: Epic T801A Backend TTI Architecture (4 topics, cross-topic integration)
- **Purpose**: Unblock E-RID/E-GDR/E-ADR development (Subphases 1.1-1.6)
- **Methodology**: Industry standards analysis, comparative evaluation, actionable recommendations
- **Parallel Commission**: T801-RES-001 (Initiative-level) runs simultaneously (10-20 minutes total for both)

---

**Prepared by:** LLM_Consultant
**Approval Required:** Client (Decision Owner)
**Target Start Date:** Upon approval (parallel commission with T801-RES-001)
**Expected Completion:** 5-10 minutes from initiation
**Criticality:** **HIGH** — Blocks Epic T801A E-RID/E-GDR/E-ADR development (Subphases 1.1-1.6); enables Phase 1 completion
