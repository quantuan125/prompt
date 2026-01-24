---
artifact_type: 'RESEARCH'
initiative_id: 'T801'
research_id: 'T801-RES-001'
version: '1.0.0'
iteration: '1'
date: '2025-11-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: TTI Indicator Design Standards (Initiative-Level)

## I. EXECUTIVE SUMMARY

This research brief commissions a **comprehensive, undergraduate-level investigation** into TTI (Timeframe Trend Identification) indicator design standards at the **Initiative T801 level** to establish cross-epic guidance for PineScript design, LLM_Trader prompt improvements, and Epic T801A backend processing. The research aims to resolve three critical design standards: (1) timeframe-specific indicator applicability (industry standards for which VWAPs/MAs/RSI apply to which timeframes), (2) volume-based trend indicators (CVD/OBV exploration for trend determination), and (3) confidence system design (backend TTI + LLM_Trader protocol integration).

Unlike T801A-RES-001 (Epic-level: Backend TTI Architecture for Epic T801A only), this brief addresses **Initiative-wide** standards that apply across multiple epics, current PineScript filter redesign needs, and future LLM_Trader prompt enhancements.

**Target Deliverable**: Comprehensive research report (Standard to Maximum quality) with industry-standard timeframe applicability matrix, volume indicator recommendations, confidence framework design, and PineScript filter redesign guidance.

**Scope**: Initiative T801 (TTI System) — applies cross-epic to PineScript (tv_ingest), LLM_Trader system prompt, and Epic T801A backend.

## II. RESEARCH SCOPE & OBJECTIVES

### **Primary Research Questions**

#### **Topic 1: [P1] Timeframe-Specific Indicator Applicability (Industry Standards)**

**Problem Context**:
- **Current Failure**: PineScript filters fail; S_VWAP (Session VWAP) appears in daily timeframe CSV despite filters, indicating flawed timeframe applicability logic in tv_ingest backend processing.
- **TTI Inconsistency**: LLM_Trader doesn't reliably follow timeframe-specific rules (e.g., prioritize S_VWAP in 1H timeframe, prioritize W_VWAP in 4H timeframe).
- **Design Standard Gap**: No documented industry-standard guidance exists for which indicators are relevant/irrelevant at specific timeframes.

**Research Objective**: Establish industry-standard timeframe applicability matrix for TTI indicators to redesign PineScript filters, inform Epic T801A backend processing logic, and guide future LLM_Trader prompt improvements.

**Specific Questions**:

1. **VWAP Applicability Standards**:
   - **Session VWAP (S_VWAP)**: Which timeframes is this relevant for (15m, 1H, 4H, 1D)?
   - **Weekly VWAP (W_VWAP)**: Which timeframes? Priority weighting vs S_VWAP per timeframe?
   - **Monthly VWAP (M_VWAP)**: Which timeframes? When does M_VWAP become primary reference vs W_VWAP?
   - **Daily VWAP (D_VWAP)**: Which timeframes? Relationship to S_VWAP (are they equivalent or distinct)?
   - **Industry Rationale**: Why are certain VWAPs irrelevant at certain timeframes (e.g., S_VWAP meaningless in daily timeframe because session resets daily)?

2. **Moving Average Applicability Standards**:
   - **EMA_9, EMA_21**: Typically used at which timeframes (scalping vs swing trading)?
   - **EMA_50**: Medium-term timeframes — industry standard applicability range?
   - **EMA_200, SMA_200**: Long-term indicators — which timeframes are appropriate?
   - **Timeframe-Specific Priority Weighting**: Should shorter EMAs (EMA_9/21) have higher weight in lower timeframes (15m, 1H) vs longer EMAs (EMA_200) in higher timeframes (4H, 1D)?

3. **RSI Applicability & Interpretation**:
   - **Standard RSI**: Universally applicable across all timeframes or timeframe-specific tuning needed (period adjustments)?
   - **RSI_MA**: RSI moving average — industry-standard usage at different timeframes?
   - **Interpretation Differences**: How does RSI interpretation change across timeframes (overbought/oversold thresholds, divergence significance)?

4. **Volume Indicators (Existing)**:
   - **Volume MA_20, Volume MA_30**: Timeframe-specific applicability and interpretation?
   - **Relevance Priority**: Are volume MAs equally weighted across timeframes or de-prioritized in higher timeframes?

5. **PineScript Filter Redesign Guidance**:
   - **Filtering Logic**: Based on industry standards, which indicators should be excluded from which timeframe CSVs?
   - **Backend Processing Logic**: For Epic T801A backend, how should indicator applicability filtering work (pre-scoring filter vs weighted zero in scoring system)?
   - **Error Prevention**: How to prevent current failure mode (S_VWAP in daily CSV) with robust filter design?

**Deliverable**: Timeframe Applicability Matrix with:
- **Matrix Table**: Indicator (rows) × Timeframe (columns: 15m, 1H, 4H, 1D) → Applicability Rating (Primary/Secondary/Irrelevant)
- **Industry Rationale**: Why each indicator is rated as applicable/irrelevant per timeframe (e.g., S_VWAP irrelevant in 1D because session resets daily)
- **Priority Weighting Guidance**: For applicable indicators, relative priority weighting per timeframe (e.g., S_VWAP high priority in 1H, W_VWAP high priority in 4H)
- **PineScript Filter Design**: Specific filter logic recommendations (which indicators to exclude from which timeframe webhooks)
- **Backend Processing Guidance**: For Epic T801A, how to implement applicability filtering in scoring system (pre-filter vs weighted scoring)

---

#### **Topic 2: [P3] Volume-Based Trend Indicators (Optional Exploration)**

**Problem Context**:
- Current TTI protocol focuses on price-based indicators (VWAPs, MAs, RSI) with minimal volume analysis (Volume MA_20/30 only).
- **Question**: Do industry-standard volume indicators (CVD, OBV) provide high-level trend determination value for TTI, or is detailed volume analysis out of scope?
- **Constraint**: Only pursue if indicators are easily exportable from TradingView PineScript and industry-validated for trend (not granular VPA).

**Research Objective**: Evaluate whether volume-based trend indicators (CVD, OBV, time-based volume patterns) should be added to TTI protocol, and if yes, provide PineScript design guidance.

**Specific Questions**:

1. **CVD (Cumulative Volume Delta)**:
   - **Trend Determination Value**: Does CVD provide reliable high-level trend signals (bullish accumulation, bearish distribution)?
   - **Industry Validation**: Is CVD widely used for trend identification (vs detailed order flow analysis)?
   - **TradingView Exportability**: Can CVD be reliably calculated and exported via PineScript webhook?
   - **Interpretation Simplicity**: Can CVD be reduced to simple trend signal (positive delta = bullish, negative = bearish) or does it require complex interpretation?

2. **OBV (On-Balance Volume)**:
   - **Trend Determination Value**: Does OBV trend (rising OBV = bullish, falling = bearish) reliably confirm price trends?
   - **Industry Validation**: Is OBV standard for trend identification or primarily for divergence detection?
   - **TradingView Exportability**: Can OBV be exported via PineScript with minimal complexity?
   - **MVP Fit**: Is OBV simple enough for MVP TTI or should it be deferred to future phases?

3. **Time-Based Volume Patterns** (Alternative):
   - Instead of CVD/OBV, are there simpler volume patterns for trend (e.g., volume increasing on up-moves vs down-moves)?
   - Industry-standard volume trend indicators simpler than CVD/OBV?

4. **Recommendation Criteria**:
   - **High-Level Trend Value**: Does indicator provide trend determination value (not detailed VPA)?
   - **Exportability**: Can indicator be reliably calculated in TradingView PineScript and exported via webhook?
   - **Interpretation Simplicity**: Can indicator be reduced to simple trend signal for backend scoring system (per Epic T801A)?
   - **Industry Validation**: Is indicator widely accepted for trend identification (not experimental or niche)?

5. **MVP Boundary**:
   - If volume indicators recommended, what's the MVP scope (which specific indicators, how to integrate into scoring system)?
   - If deferred, what's the rationale (complexity vs marginal value, exportability challenges, interpretation difficulty)?

**Deliverable**: Volume Indicator Recommendation with:
- **Inclusion Decision**: Should CVD, OBV, or alternative volume indicators be added to TTI protocol (YES/NO with rationale)?
- **Selected Indicators** (if YES): Which specific volume indicators with trend determination value assessment
- **PineScript Design Guidance** (if YES): How to calculate and export via webhook (calculation logic, export format, data structure)
- **Backend Integration Guidance** (if YES): How to integrate into Epic T801A scoring system (weighting strategy, threshold calibration)
- **Deferral Strategy** (if NO): Rationale for deferral (complexity, marginal value, exportability challenges) and conditions for future reconsideration

---

#### **Topic 3: [P2] Confidence System Design (Backend + LLM Exploration)**

**Problem Context**:
- **Epic T801A Backend**: No confidence determination system exists; backend TTI needs confidence flags for ambiguous assessments (e.g., conflicting indicators, insufficient data, image quality issues).
- **LLM_Trader Protocols**: Current SPP (Strategy Proposal & Planning) and TEA (Trade Execution & Adjustment) use subjective D-to-A+ grading for confidence, but no systematic confidence framework exists.
- **Integration Question**: Should backend TTI confidence system align with LLM_Trader confidence grading, or are these separate concerns?

**Research Objective**:
- **In-Scope (Epic T801A)**: Design backend TTI confidence system (necessity, calibration methodology, threshold design).
- **Out-of-Scope Exploration**: Identify if confidence frameworks apply to LLM_Trader semantic protocols (SPP/TEA grading) for future Initiative T801 work.

**Specific Questions**:

1. **Backend TTI Confidence Necessity**:
   - When should backend TTI flag "low confidence" (conflicting indicators, insufficient data, edge cases)?
   - **Use Cases**:
     - Indicator conflict: BEARISH price action but BULLISH RSI divergence → confidence flag?
     - Data insufficiency: Missing swing points or incomplete VWAP data → confidence flag?
     - Edge case: Trend score exactly 0 (perfect NEUTRAL) → confidence flag?
   - **Decision Impact**: How should LLM_Trader respond to low-confidence TTI (request manual review, apply conservative bias, etc.)?

2. **Confidence Calibration Methodology**:
   - **Quantitative Approach**: Calculate confidence based on indicator agreement (e.g., 80% indicators bullish → high confidence, 50/50 split → low confidence)?
   - **Threshold-Based Approach**: Confidence levels based on trend score proximity to classification boundaries (e.g., score = -0.9 near NEUTRAL boundary → lower confidence than score = -2.0 strong BEARISH)?
   - **Hybrid Approach**: Combine indicator agreement + score proximity + data sufficiency?

3. **Confidence Threshold Design**:
   - **Confidence Levels**: Binary (confident/uncertain) or multi-level (high/medium/low confidence)?
   - **Threshold Calibration**: What thresholds define each confidence level (e.g., >80% indicator agreement = high confidence)?
   - **File Format Integration**: How should confidence be represented in backend TTI file (Topic 2 from T801A-RES-001)?

4. **LLM_Trader Confidence Framework Exploration** (Out-of-Scope for Epic T801A, but exploratory for Initiative T801):
   - **Current State**: SPP/TEA protocols use D-to-A+ grading subjectively; no systematic confidence framework.
   - **Alignment Question**: Should backend TTI confidence (Epic T801A) inform LLM_Trader confidence grading (SPP/TEA)?
   - **Integration Potential**: Could unified confidence framework apply to both backend TTI and LLM semantic assessments?
   - **Future Work**: Is this worth pursuing at Initiative T801 level (cross-epic standardization) or keep backend TTI confidence isolated?

5. **MVP Recommendation**:
   - **Backend TTI Confidence** (Epic T801A): What's the MVP confidence system design (necessity, calibration, threshold, file format integration)?
   - **LLM_Trader Exploration**: High-level recommendation — should Initiative T801 future work include unified confidence framework research?

**Deliverable**: Confidence System Design with:
- **Backend TTI Confidence System** (Epic T801A scope):
  - **Necessity Assessment**: Should backend include confidence flags (YES/NO with use case analysis)?
  - **Calibration Methodology**: Recommended approach (indicator agreement, score proximity, hybrid) with calculation logic
  - **Threshold Design**: Confidence levels (binary/multi-level) with threshold definitions
  - **File Format Integration**: How confidence appears in backend TTI file (field structure, representation)
- **LLM_Trader Confidence Exploration** (Initiative T801 out-of-scope note):
  - **Alignment Analysis**: Could backend TTI confidence inform LLM_Trader SPP/TEA grading?
  - **Future Work Recommendation**: Should Initiative T801 pursue unified confidence framework (YES/NO with rationale)?
  - **Scope Boundary**: Clear separation — Epic T801A implements backend confidence only; LLM_Trader integration deferred to future initiative work

---

### **Cross-Topic Integration Analysis**

**Integration Objective**: Ensure the three research topics produce **cohesive Initiative-level design standards** applicable across PineScript, LLM_Trader, and Epic T801A backend.

**Key Integration Questions**:

1. **Timeframe Applicability ↔ Backend Scoring System** (T801A-RES-001 Integration):
   - How do timeframe applicability standards (Topic 1) inform Epic T801A scoring system weighting strategy (T801A-RES-001 Topic 1)?
   - Example: If S_VWAP is "Primary" priority in 1H timeframe per Topic 1 matrix, should Epic T801A scoring system weight S_VWAP higher than W_VWAP in 1H calculations?

2. **Volume Indicators ↔ Confidence System**:
   - If volume indicators (CVD/OBV) are included (Topic 2), how do they interact with confidence system (Topic 3)?
   - Example: If CVD and price trend conflict, should this trigger low-confidence flag in backend TTI?

3. **Timeframe Applicability ↔ PineScript Filter Design**:
   - How do Topic 1 applicability standards translate to concrete PineScript filter logic?
   - Example: If S_VWAP rated "Irrelevant" for 1D timeframe, should PineScript exclude S_VWAP calculation entirely for daily webhook or export but flag as "not applicable"?

4. **Confidence System ↔ LLM_Trader Protocols**:
   - If backend TTI includes confidence flags (Topic 3), how should LLM_Trader SPP/TEA protocols respond?
   - Example: If backend TTI flags "low confidence," should LLM_Trader apply conservative bias in SPP strategy proposals?

5. **Initiative-Level Standards Propagation**:
   - **PineScript Application**: How do Topics 1-3 standards apply to PineScript redesign (filter logic, indicator export, data structure)?
   - **LLM_Trader Application**: How do standards inform future LLM_Trader prompt improvements (remove/reduce TTI protocol, integrate backend TTI confidence)?
   - **Epic T801A Application**: How do standards inform backend implementation (applicability filtering, volume indicator integration, confidence system design)?

**Deliverable**: Cross-topic integration section in research report with:
- Integration analysis (how Topics 1-3 interact across PineScript, LLM_Trader, Epic T801A)
- Initiative-level design standards summary (unified guidance for cross-epic application)
- Implementation propagation roadmap (how to apply standards to PineScript, LLM_Trader, Epic T801A in sequence)

---

## III. RESEARCH DELIVERABLES

### **A. Timeframe Applicability Matrix Report**
- **Industry-Standard Matrix**: Indicator × Timeframe (15m, 1H, 4H, 1D) → Applicability Rating (Primary/Secondary/Irrelevant)
- **Rationale Documentation**: Why each indicator rated as applicable/irrelevant per timeframe (industry standards, technical rationale)
- **Priority Weighting Guidance**: Relative priority for applicable indicators per timeframe (e.g., S_VWAP high priority in 1H, W_VWAP high priority in 4H)
- **PineScript Filter Design**: Specific filter logic recommendations (exclusion rules per timeframe webhook)
- **Backend Processing Guidance**: Epic T801A applicability filtering approach (pre-filter vs weighted scoring)

### **B. Volume Indicator Recommendation**
- **Inclusion Decision**: Should CVD, OBV, or alternative volume indicators be added to TTI (YES/NO with rationale)?
- **Selected Indicators** (if YES): Which specific volume indicators with trend value assessment
- **PineScript Design Guidance** (if YES): Calculation logic, export format, webhook data structure
- **Backend Integration** (if YES): Epic T801A scoring system integration (weighting, threshold calibration)
- **Deferral Strategy** (if NO): Rationale for deferral, conditions for future reconsideration

### **C. Confidence System Design Specification**
- **Backend TTI Confidence System** (Epic T801A):
  - Necessity assessment (use case analysis)
  - Calibration methodology (indicator agreement, score proximity, hybrid)
  - Threshold design (confidence levels, threshold definitions)
  - File format integration (field structure, representation)
- **LLM_Trader Confidence Exploration** (Initiative T801 note):
  - Alignment analysis (backend TTI confidence ↔ LLM_Trader SPP/TEA grading)
  - Future work recommendation (unified confidence framework viability)

### **D. Cross-Topic Integration & Initiative Standards**
- **Integration Analysis**: How Topics 1-3 interact across PineScript, LLM_Trader, Epic T801A
- **Initiative-Level Standards Summary**: Unified design standards for cross-epic application
- **Implementation Propagation Roadmap**: Sequence for applying standards (PineScript → Epic T801A → LLM_Trader)

### **E. PineScript Filter Redesign Guidance**
- **Filter Logic Specification**: Concrete PineScript filter redesign to prevent current failure mode (S_VWAP in daily CSV)
- **Timeframe-Specific Export Rules**: Which indicators to export for which timeframe webhooks
- **Data Structure Recommendations**: How to represent applicability in webhook payload (exclusion vs flagging)

### **F. Epic T801A Integration Guidance**
- **T801A Dependencies Impact**: How Topic 1 findings inform T801A-DEP-### (PineScript Enhancement requirements)
- **T801A Implementation Guidance Impact**: How Topics 1-3 inform T801A-IG-### (backend processing patterns)
- **Cross-Research Coordination**: How T801-RES-001 findings align with T801A-RES-001 findings (scoring system weighting, file format confidence field)

---

## IV. RESEARCH METHODOLOGY

### **A. Industry Standards & Technical Literature Analysis**

**Primary Sources**:
- Technical analysis textbooks and industry standards (timeframe-specific indicator usage)
- Volume analysis literature (CVD, OBV, volume trend indicators)
- Trading system confidence calibration methodologies
- PineScript documentation (TradingView webhook capabilities, indicator calculation patterns)

**Focus Areas**:
- Industry-standard timeframe applicability for VWAPs, moving averages, RSI, volume indicators
- Volume-based trend indicators (CVD, OBV) — trend determination value vs detailed VPA
- Confidence system design patterns (quantitative calibration, threshold-based levels)

### **B. Comparative Analysis Framework**

**Investigation Approach**:
- **Topic 1 (Timeframe Applicability)**: Survey industry literature for VWAP/MA/RSI usage standards per timeframe; synthesize into applicability matrix
- **Topic 2 (Volume Indicators)**: Evaluate CVD/OBV trend determination value, TradingView exportability, interpretation simplicity
- **Topic 3 (Confidence System)**: Compare confidence calibration methodologies (indicator agreement, score proximity, hybrid); recommend MVP design

### **C. Constraint Validation**

**Initiative T801 Standards to Respect**:
- **Cross-Epic Applicability**: Standards must apply to PineScript, LLM_Trader, and Epic T801A backend (not siloed to single epic)
- **TradingView Exportability**: Volume indicators must be reliably exportable via PineScript webhook (no custom APIs per existing constraints)
- **MVP Focus**: Confidence system must be implementable in Epic T801A MVP (not over-engineered for theoretical future)

---

## V. CRITICAL DEPENDENCIES & CONTEXT

### **Current State Challenges**

This research directly addresses **Initiative T801 cross-epic blocking dependencies**:

1. **PineScript Filter Failure (Current State)**:
   - S_VWAP appearing in daily timeframe CSV despite filters (tv_ingest backend + PineScript logic flawed)
   - No documented industry-standard guidance for timeframe-specific indicator applicability
   - Filter redesign blocked until applicability standards established

2. **LLM_Trader Inconsistency**:
   - Doesn't reliably follow timeframe-specific rules (S_VWAP priority in 1H vs W_VWAP in 4H)
   - No systematic confidence framework for SPP/TEA protocols (subjective D-to-A+ grading)

3. **Epic T801A Backend Design Gap**:
   - Scoring system weighting strategy (T801A-RES-001 Topic 1) requires timeframe applicability standards (Topic 1 of this brief)
   - Confidence system design (Topic 3 of this brief) required for backend TTI file format (T801A-RES-001 Topic 2)

### **Initiative T801 Scope & Cross-Epic Applicability**

**Initiative T801 (TTI System)** encompasses:
- **Epic T801A**: Backend TTI Migration (deterministic calculation, file generation, hybrid architecture)
- **Future Epic T801B** (potential): PineScript TTI Enhancement (filter redesign, data extraction improvements)
- **Future Epic T801C** (potential): LLM_Trader TTI Protocol Improvements (reduce/remove TTI from prompt, integrate backend TTI consumption)

**This Research Applicability**:
- **PineScript** (tv_ingest component + future Epic T801B): Topic 1 (timeframe applicability) → filter redesign; Topic 2 (volume indicators) → export enhancements
- **LLM_Trader** (current prompt + future Epic T801C): Topic 1 → timeframe-specific rule enforcement; Topic 3 → confidence framework exploration
- **Epic T801A Backend**: All three topics inform backend processing logic, scoring system, confidence flags

### **Integration with Epic T801A E-RID/E-GDR/E-ADR Development**

Research findings will directly inform:

- **T801A-DEP-### (Dependencies)**:
  - T801A-DEP-001 (PineScript Enhancement): Topic 1 timeframe applicability matrix → filter redesign requirements
  - T801A-DEP-002 (tv_ingest Component): Topic 2 volume indicators → PineScript export enhancements (if CVD/OBV included)

- **T801A-IG-### (Implementation Guidance)**:
  - T801A-IG-### (Backend Processing Patterns): Topic 1 applicability filtering approach (pre-filter vs weighted scoring aligned with industry standards)
  - T801A-IG-### (Confidence System): Topic 3 confidence calibration methodology, file format integration

- **Cross-Research Integration (T801A-RES-001 ↔ T801-RES-001)**:
  - **T801A-RES-001 Topic 1 (Scoring System)** ← **T801-RES-001 Topic 1 (Timeframe Applicability)**: Weighting strategy informed by applicability matrix
  - **T801A-RES-001 Topic 2 (File Format)** ← **T801-RES-001 Topic 3 (Confidence System)**: Schema includes confidence field
  - **T801A-RES-001 Topic 1 (Scoring System)** ← **T801-RES-001 Topic 2 (Volume Indicators)**: Integration of CVD/OBV into scoring algorithm (if included)

### **Alignment with Broader Repository Context**

- **T102-ADR-004/005 Standards**: Research findings may inform future Initiative T801 GDRs (I-GDRs) for cross-epic governance
- **documentation/general.md**: Initiative-level standards may propagate to repository-wide best practices
- **PineScript Filter Redesign Urgency**: Topic 1 findings unlock immediate PineScript fix (S_VWAP in daily CSV failure)

---

## VI. SUCCESS CRITERIA

The research will be considered successful if it delivers:

1. **Timeframe Applicability Matrix (Topic 1)**:
   - ✅ Complete matrix: Indicator × Timeframe → Applicability Rating with industry rationale
   - ✅ Priority weighting guidance: Relative priority for applicable indicators per timeframe
   - ✅ PineScript filter redesign: Concrete filter logic to prevent current failure mode
   - ✅ Epic T801A backend guidance: Applicability filtering approach (pre-filter vs weighted scoring)

2. **Volume Indicator Recommendation (Topic 2)**:
   - ✅ Clear decision: Include CVD/OBV (or alternatives) in TTI protocol — YES/NO with rationale
   - ✅ If YES: PineScript design guidance (calculation, export, webhook structure)
   - ✅ If YES: Epic T801A integration (scoring system weighting, threshold calibration)
   - ✅ If NO: Deferral strategy with conditions for future reconsideration

3. **Confidence System Design (Topic 3)**:
   - ✅ Backend TTI confidence system specification (necessity, calibration, threshold, file format integration)
   - ✅ LLM_Trader confidence exploration (alignment analysis, future work recommendation)
   - ✅ Scope clarity: Epic T801A implementation guidance vs Initiative T801 future work separation

4. **Cross-Topic Integration**:
   - ✅ Integration analysis: How Topics 1-3 interact across PineScript, LLM_Trader, Epic T801A
   - ✅ Initiative-level standards: Unified design guidance for cross-epic application
   - ✅ Implementation propagation roadmap: Sequence for applying standards

5. **Cross-Research Coordination (T801A-RES-001 Integration)**:
   - ✅ Clear documentation: How T801-RES-001 findings inform T801A-RES-001 topics (scoring weighting, file format confidence field, volume indicator integration)
   - ✅ No conflicts: T801-RES-001 and T801A-RES-001 recommendations align cohesively

6. **Research Quality Standards**:
   - ✅ Comprehensive depth: Undergraduate-level analysis per topic (not surface-level)
   - ✅ Standard to Maximum quality: Industry standards cited, comparative analysis, implementation examples
   - ✅ Actionable recommendations: Clear "we recommend X because Y" guidance for PineScript, Epic T801A, Initiative T801

---

## VII. TIMELINE & RESOURCES

### **Research Phases**

**Phase 1: Industry Standards & Literature Review** (2-3 minutes)
- Technical analysis standards (timeframe-specific indicator usage)
- Volume analysis literature (CVD, OBV, trend determination value)
- Confidence system design patterns

**Phase 2: Topic 1 Research (Timeframe Applicability)** (2-3 minutes)
- VWAP applicability standards (S_VWAP, W_VWAP, M_VWAP, D_VWAP)
- Moving average applicability (EMA_9/21/50/200, SMA_200)
- RSI applicability & interpretation differences
- Volume indicator (existing) applicability
- Matrix synthesis + PineScript filter redesign guidance

**Phase 3: Topic 2 Research (Volume Indicators)** (1-2 minutes)
- CVD/OBV trend determination value assessment
- TradingView exportability feasibility
- Interpretation simplicity evaluation
- Recommendation (include/defer) with rationale

**Phase 4: Topic 3 Research (Confidence System)** (1-2 minutes)
- Backend TTI confidence necessity assessment
- Calibration methodology comparison (indicator agreement, score proximity, hybrid)
- Threshold design (binary/multi-level)
- LLM_Trader confidence exploration (alignment analysis, future work recommendation)

**Phase 5: Cross-Topic Integration & Initiative Standards** (1-2 minutes)
- Integration analysis (Topics 1-3 interactions)
- Initiative-level standards synthesis
- Implementation propagation roadmap
- Cross-research coordination (T801A-RES-001 integration)

**Total Duration:** 5-10 minutes (comprehensive research, undergraduate-level depth)

### **Required Resources**
- Technical analysis literature (timeframe-specific indicator standards)
- Volume analysis resources (CVD, OBV, trend indicators)
- Trading system design patterns (confidence calibration methodologies)
- PineScript documentation (TradingView webhook capabilities)
- **Quality Level**: Standard to Maximum (comprehensive, actionable, cross-epic implementation-ready)

---

## VIII. STAKEHOLDER ENGAGEMENT

### **Primary Stakeholders**
- **Client (Decision Owner)**: Final approval of research scope and acceptance of recommendations; Initiative T801 standards authority
- **LLM_Consultant**: Primary consumer for Epic T801A Subphases 1.2 (Dependencies), 1.4 (Implementation Guidance); future Initiative T801 work
- **LLM_Research**: External research agent conducting comprehensive investigation (5-10 minutes)

### **Review & Approval Gates**
- **Research Scope Approval** (Gate 1 - Current): Client confirmation of research objectives, topics, cross-epic applicability
- **Final Deliverable Review** (Gate 2): Client acceptance of research findings and Initiative T801 standards
- **Epic T801A Integration Review** (Gate 3): Client approval of how findings inform T801A Dependencies and Implementation Guidance

### **Integration with Phase 1 Consultancy & Initiative T801**

Research findings will be integrated into:

1. **Epic T801A Phase 1** (Current):
   - **Subphase 1.2 (Dependencies)**: Topic 1 → T801A-DEP-001 (PineScript Enhancement requirements); Topic 2 → T801A-DEP-002 (volume indicator export if included)
   - **Subphase 1.4 (Implementation Guidance)**: Topic 1 → applicability filtering approach; Topic 3 → confidence system design
   - **Subphase 1.6 (E-GDR & E-ADR)**: Cross-research coordination (T801-RES-001 + T801A-RES-001 findings integrated)

2. **Initiative T801 Future Work**:
   - **PineScript Filter Redesign** (Immediate): Topic 1 applicability matrix → tv_ingest backend filter logic fix
   - **Future Epic T801B** (PineScript Enhancement): Topic 1 → comprehensive filter redesign; Topic 2 → volume indicator export
   - **Future Epic T801C** (LLM_Trader Improvements): Topic 1 → timeframe-specific rule enforcement in prompt; Topic 3 → confidence framework integration (if pursued)

---

## IX. KNOWN CONSTRAINTS & ASSUMPTIONS

### **Constraints**
- **Initiative-Level Scope**: Research applies cross-epic (PineScript, LLM_Trader, Epic T801A); not limited to single epic
- **Time-Boxed**: 5-10 minutes maximum; comprehensive depth but actionable implementation guidance prioritized
- **TradingView Platform Limitation**: Volume indicators (Topic 2) must be TradingView-exportable; no custom APIs
- **Epic T801A Integration Requirement**: Findings must inform Epic T801A E-RIDs (Dependencies, Implementation Guidance) without prescribing final decisions

### **Assumptions**
- Industry-standard timeframe applicability guidance exists for VWAPs, MAs, RSI (Topic 1 matrix can be synthesized)
- CVD/OBV trend determination value can be assessed from literature (TradingView exportability can be validated from PineScript docs)
- Confidence system calibration methodologies are documented (backend TTI confidence design feasible for MVP)
- T801-RES-001 and T801A-RES-001 findings will align cohesively (no fundamental conflicts requiring reconciliation)

### **Out of Scope**
- **LLM_Trader Prompt Implementation**: How to rewrite LLM_Trader prompt to integrate backend TTI (Epic T801A Feature T801A3 or future Epic T801C scope)
- **PineScript Code Implementation**: Actual PineScript filter logic code (LLM_Developer responsibility, research provides specification only)
- **Backtesting Volume Indicators**: Full historical validation of CVD/OBV (deferred to playground validation, research provides trend value assessment only)
- **Comprehensive Confidence Framework**: Unified confidence system across all LLM_Trader protocols (SPP, TEA, CAS) — Initiative T801 future work, not Epic T801A MVP

---

## X. APPENDICES

### **A. Current Artifact References**
- **Primary Context**: Conversation history from current consultancy session (Draft Problem Statement, Subphase 1.0 specifications)
- **Plan File**: `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` (v1.2.0, Subphase 1.0 dual research brief strategy)
- **Current TTI Protocol**: `prompt/roles/VPA/main_v2.1.md` (lines 21-55) — Current LLM-based TTI structure with indicators
- **Problematic CSV**: `components/tv_ingest/data/BINANCE_BTCUSDT/master.csv` — S_VWAP in daily timeframe failure
- **Parallel Research Brief**: `brief_T801A-RES-001_backend-tti-architecture.md` — Epic-level backend architecture research
- **Governance Standards**: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` (T102-ADR-004/005)

### **B. Research Topic Prioritization Rationale**

| Topic | Priority | Rationale |
|:------|:---------|:----------|
| **Topic 1: Timeframe Applicability** | **P1** | **Immediate Impact**: Unlocks PineScript filter fix (S_VWAP in daily CSV failure); informs Epic T801A scoring system weighting (T801A-RES-001 Topic 1); cross-epic standard for PineScript, LLM_Trader, Epic T801A |
| **Topic 3: Confidence System** | **P2** | **Epic T801A Dependency**: Required for backend TTI file format schema (T801A-RES-001 Topic 2 confidence field); high value for ambiguous TTI assessments; LLM_Trader exploration high strategic value |
| **Topic 2: Volume Indicators** | **P3** | **Optional Exploration**: Nice-to-have vs essential; complexity may justify deferral; prioritize core indicators (VWAPs, MAs, RSI) before volume expansion |

### **C. Expected Cross-Research Integration (T801A-RES-001 ↔ T801-RES-001)**

| T801-RES-001 Topic | Informs T801A-RES-001 Topic | Integration Mechanism |
|:-------------------|:----------------------------|:----------------------|
| **Topic 1 (Timeframe Applicability)** | **T801A Topic 1 (Scoring System)** | Weighting strategy: Applicability matrix defines relative priority per timeframe (e.g., S_VWAP high weight in 1H, W_VWAP high weight in 4H) |
| **Topic 3 (Confidence System)** | **T801A Topic 2 (File Format)** | Schema design: File format must include confidence field per Topic 3 specification |
| **Topic 2 (Volume Indicators)** | **T801A Topic 1 (Scoring System)** | If CVD/OBV included, scoring algorithm integrates volume signals into overall trend score |
| **Topic 1 (Timeframe Applicability)** | **T801A Topic 3 (PA Detection)** | Data requirements: If certain indicators irrelevant per timeframe, PA detection may rely on reduced data set |

### **D. Immediate PineScript Filter Fix Roadmap**

**Current Failure**: S_VWAP appearing in daily timeframe CSV

**Research Unlocks Fix**:
1. **T801-RES-001 Topic 1 Completion**: Timeframe applicability matrix confirms "S_VWAP irrelevant for 1D timeframe"
2. **PineScript Filter Redesign**: Update tv_ingest backend + PineScript webhook filter logic to exclude S_VWAP from daily CSV
3. **Validation**: Test with historical data, confirm S_VWAP no longer appears in daily timeframe output

**Timeline**: Research (5-10 min) → Filter redesign (LLM_Developer, 30-45 min) → Validation (15-20 min) = **1-2 hours total to fix current failure**

### **E. Research Brief Lineage**

**Precedent Research Briefs**:
- **T810A-RES-003**: Knowledge Taxonomy & Access Patterns (surface-level platform investigation, 5-10 minutes)

**Parallel Research (T801)**:
- **T801A-RES-001**: Backend TTI Architecture (Epic-level, 4 topics, 5-10 minutes) — runs simultaneously with this brief

**This Research (T801-RES-001)**:
- **Type**: Comprehensive, undergraduate-level investigation (Standard to Maximum quality)
- **Scope**: Initiative T801 (cross-epic) — applies to PineScript, LLM_Trader, Epic T801A
- **Purpose**: Establish design standards (timeframe applicability, volume indicators, confidence system) for cross-epic application
- **Methodology**: Industry standards analysis, comparative evaluation, actionable cross-epic recommendations
- **Parallel Commission**: T801A-RES-001 (Epic-level) runs simultaneously (10-20 minutes total for both)

---

**Prepared by:** LLM_Consultant
**Approval Required:** Client (Decision Owner)
**Target Start Date:** Upon approval (parallel commission with T801A-RES-001)
**Expected Completion:** 5-10 minutes from initiation
**Criticality:** **HIGH** — Unlocks immediate PineScript filter fix; establishes Initiative T801 design standards; informs Epic T801A Dependencies and Implementation Guidance
