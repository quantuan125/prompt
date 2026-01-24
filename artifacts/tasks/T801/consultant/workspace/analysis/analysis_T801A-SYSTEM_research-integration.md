---
artifact_type: 'ANALYSIS'
initiative_id: 'T801'
epic_id: 'T801A'
epic_code: 'TTI'
subphase: '1.0.1'
version: '1.0.0'
date: '2025-11-23'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Cross-research integration analysis for Subphase 1.0.1 to inform E-RID/E-GDR/E-ADR development in Phase 1'
---

# INTEGRATION ANALYSIS: Subphase 1.0.1 Research Report Integration

## I. EXECUTIVE SUMMARY

**Purpose**
Synthesize findings from both commissioned research reports (T801-RES-001 Initiative-level; T801A-RES-001 Epic-level) into actionable governance inputs for Epic T801A development. This analysis:
1. Extracts **key research findings** with direct governance implications
2. Maps findings to **proposed E-RID categories** (QG, DEP, ASSUM, CON, IF, IG)
3. Identifies **cross-research dependencies** (how Initiative standards inform Epic architecture)
4. Assesses **implications for Phase 1 subphases** (1.1-1.7)
5. Prepares **E-GDR/E-ADR candidate decisions** for Subphase 1.6 development

**Scope**
- **T801-RES-001**: Initiative-level indicator design standards (timeframe applicability, volume indicators, confidence systems)
- **T801A-RES-001**: Epic-level backend TTI architecture (numeric scoring, file format, PA detection, divergence/crossover)

**Key Integration Findings**
1. **Numeric Scoring System**: Adopt -2 to +2 symmetric scale with defined thresholds — directly informs T801A-ASSUM-001 validation methodology and T801A-GDR-002
2. **File Format**: JSON with lean schema — directly informs T801A-GDR-004 and T801A-ADR-004; includes versioning and manual override workflows
3. **Timeframe Applicability Matrix**: Enforce indicator inclusion/exclusion at PineScript layer — informs T801A-DEP-001 (PineScript Enhancement) and T801A-IG-002
4. **Volume Confirmation**: Include OBV, defer CVD — informs T801A-IG-003 and future Initiative work
5. **Confidence System Design**: Weighted voting ensemble with threshold calibration — bridges Epic T801A backend needs and future LLM_Trader protocol improvements
6. **Divergence Deferral**: MA crossovers include MVP; divergence detection deferred — validates T801A-CON-002 complexity management

**Decision Ownership**: All governance artifacts derived from this analysis require Client approval before finalization.

---

## II. SOURCE MATERIAL SUMMARY

### A. Research Reports Reviewed

| Research ID | Scope | Topics Covered | Quality Assessment | Enhancement Status |
|:------------|:------|:---------------|:-------------------|:-------------------|
| **T801-RES-001** | Initiative T801 (cross-epic) | Timeframe applicability matrix, Volume indicators (OBV/CVD), Confidence system design, Cross-topic integration | Excellent — enhanced per enhancement brief | Complete |
| **T801A-RES-001** | Epic T801A (backend) | Numeric scoring system, File format selection, PA detection methodology, Divergence/crossover detection | Excellent — enhanced per enhancement brief | Complete |

### B. Context Materials Reviewed

- **Plan File**: `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` (v1.3.0)
- **Current LLM_Trader Prompt**: `prompt/roles/VPA/main_v2.1.md` — TTI protocol (lines 21-55)
- **T810 Structural Exemplars**: SPS, Concept, Analysis patterns
- **T102 Standards**: T102-ADR-004/005 for ID specification and decision record formatting

---

## III. KEY FINDINGS EXTRACTION

### A. T801-RES-001: Initiative-Level Design Standards

#### Finding 1: Timeframe × Indicator Applicability Matrix

**Summary**: Comprehensive matrix defining indicator relevance (High/Medium/Low) across timeframes (15m, 1H, 4H, 1D).

**Critical Governance Implications**:

| Indicator | 15m | 1H | 4H | 1D | Governance Action |
|:----------|:----|:---|:---|:---|:------------------|
| S_VWAP (Session) | High | High | Medium | **Low** → Exclude | Enforce exclusion at PineScript layer for 1D |
| D_VWAP (Daily) | High | High | Medium | **Low** → Exclude | Enforce exclusion at PineScript layer for 1D |
| W_VWAP (Weekly) | Low | Medium | High | High | Primary VWAP for 4H/1D |
| M_VWAP (Monthly) | Low | Low | Medium | High | Primary VWAP for 1D |
| EMA (Short: 9/21) | High | High | High | High | Include all timeframes |
| EMA (Long: 50/200) | Medium | High | High | High | Include all timeframes |
| SMA_200 | Medium | High | High | High | Include all timeframes |
| RSI | Medium | High | High | High | Include all timeframes with confirmation requirements |
| OBV | High | High | High | High | Include all timeframes (per Finding 2) |

**PineScript Filter Pseudocode** (from research report):
```python
IF timeframe IN ['15m', '1H']:
    INCLUDE: S_VWAP, D_VWAP, EMA_9, EMA_21, EMA_50, RSI, OBV
    EXCLUDE: W_VWAP (secondary), M_VWAP (low relevance)
    PRIORITY_WEIGHT: S_VWAP > D_VWAP > EMA_short > RSI

ELIF timeframe == '4H':
    INCLUDE: W_VWAP, EMA_50, EMA_200, SMA_200, RSI, OBV
    EXCLUDE: S_VWAP (irrelevant - session resets)

ELIF timeframe == '1D':
    INCLUDE: W_VWAP, M_VWAP, EMA_200, SMA_200, RSI, OBV
    EXCLUDE: S_VWAP, D_VWAP (session-anchored VWAPs irrelevant)
```

**Maps To**: T801A-DEP-001 (PineScript Enhancement), T801A-IG-002 (Timeframe Filtering), Initiative T801 future work (PineScript redesign)

---

#### Finding 2: Volume Indicator Recommendation

**Summary**: Include OBV as trend confirmation indicator; defer CVD due to data complexity and limited availability.

**Rationale**:
- **OBV (Yes)**: Industry-validated (1963 origin), straightforward computation, exportable from TradingView, high interpretability
- **CVD (No)**: Requires tick-level data not universally available, adds backend complexity, niche use case

**Governance Implications**:
- OBV to be included in backend TTI calculation as confirmation signal
- OBV confirmation enhances confidence scoring (rising OBV + uptrend = higher confidence)
- CVD deferred to future Initiative scope (requires specialized data infrastructure)

**Maps To**: T801A-IG-003 (Volume Confirmation), T801A-QG-002 (Signal Reliability)

---

#### Finding 3: Confidence System Design Framework

**Summary**: Multi-indicator confidence system using weighted voting ensemble with governance-approved thresholds.

**Key Design Principles**:
1. **Weighted Voting Ensemble**: Each indicator votes toward bullish/bearish with assigned weights based on reliability
2. **Threshold-Based Voting**: Require minimum indicator agreement before flagging trend (e.g., ≥3/4 bullish)
3. **Calibration Methodology**: Historical simulation with precision/recall and risk-adjusted metrics (Sharpe/drawdown)
4. **Constraints**: Avoid overfitting (keep ensemble small), ensure interpretability (transparent weights), prevent redundancy (diversify indicator types)

**Initiative-Level Standards Derived**:
- **Standard 1**: Timeframe-specific indicator filtering (matrix enforcement)
- **Standard 2**: OBV volume confirmation (default inclusion)
- **Standard 3**: Confidence scoring with threshold calibration
- **Standard 4**: Indicator type + role clarity (prevent redundancy)
- **Standard 5**: Performance evaluation + lifecycle (promote/demote indicators based on evidence)
- **Standard 6**: Integration prioritization rubric (impact × feasibility × complexity)

**Cross-Topic Integration**:
- Timeframe applicability → gates which indicators participate in confidence scoring
- Volume confirmation (OBV) → acts as confidence modulator (divergence detection)
- Confidence system → receives filtered indicators and produces composite score

**Maps To**: T801A-ASSUM-001 (Confidence System Viability), T801A-QG-002 (Signal Reliability), T801A-IG-004 (Confidence Scoring)

---

### B. T801A-RES-001: Epic-Level Backend Architecture

#### Finding 4: Numeric Scoring System Design

**Summary**: Adopt -2 to +2 symmetric 5-point scale for trend strength.

**Scale Definition**:
| Score | Label | Criteria (Rule-Based) |
|:------|:------|:----------------------|
| **+2** | Strong Uptrend | Higher highs/lows confirmed + ADX ≥ 30 + bullish MA crossover + no contradictory signals |
| **+1** | Uptrend | Higher lows forming + ADX 20-25 + majority bullish indicators |
| **0** | Neutral | Range-bound or mixed signals; bullish/bearish factors cancel |
| **-1** | Downtrend | Lower highs forming + ADX 20-25 + majority bearish indicators |
| **-2** | Strong Downtrend | Lower highs/lows confirmed + ADX ≥ 30 + bearish MA crossover + no contradictory signals |

**Scoring Formula Components**:
- Trend Direction: +1/-1 based on HH/HL or LH/LL pattern
- Momentum Strength: +1/-1 based on ADX threshold
- Signal Confirmation: +1/-1 for supporting signals (crossovers, breakouts)
- Contradictory Signals: -1 if opposing warning signs present

**Validation Methodology** (research-provided):
- Backtesting: N ≥ 100 trading days, stratified across regimes
- Acceptance Criteria: ≥70% overall accuracy, ≥80% precision for extreme scores (+2/-2), ≤20% false positive rate
- Ongoing Calibration: Monthly drift check, quarterly threshold review, trader feedback loop
- Production Cutover Gate: Rolling 30+ day window meets criteria + trader sample approval

**Maps To**: T801A-ASSUM-001 (Numeric Scoring Viability), T801A-GDR-002 (Numeric Scoring Foundation), T801A-ADR-002 (Scoring Algorithm Specification)

---

#### Finding 5: Backend TTI File Format

**Summary**: Adopt JSON with lean schema; include versioning and manual override workflow.

**Format Selection Rationale**:
| Format | Schema Rigidity | LLM Ingestion | Traceability | Recommendation |
|:-------|:----------------|:--------------|:-------------|:---------------|
| JSON | High (strict fields/types) | Reliable (explicit structure) | Excellent (diff-able, schema validation) | **Selected** |
| YAML | High (like JSON) | Similar to JSON | Good | Alternative |
| Markdown | Low (free-form) | Very high (natural text) | Weak (hard to validate) | Not recommended |
| Hybrid | Combines structured + narrative | High | High | Future consideration |

**Sample JSON Schema** (research-provided):
```json
{
  "schema_version": "1.0.0",
  "generator_version": "tti-engine/0.1.0",
  "asset": "BTC-USD",
  "timeframe": "1D",
  "trend_score": 2,
  "trend_label": "Strong Uptrend",
  "signals": {
    "price_action": {
      "higher_highs": true,
      "higher_lows": true,
      "breakout": "Above last 30-day high"
    },
    "moving_average": {
      "MA50_cross_MA200": "bullish",
      "cross_date": "2025-11-29"
    },
    "divergence": {
      "RSI_bearish_divergence": false
    }
  },
  "as_of": "2025-11-29",
  "manual_override": false,
  "override_note": null,
  "override_by": null,
  "override_timestamp": null
}
```

**Versioning Strategy**:
- Schema version tracking: `schema_version` field in every output
- Major/Minor/Patch semver for breaking/additive/documentation changes
- Backward compatibility: New fields optional; deprecated fields retained 2 major versions

**Manual Override Workflow**:
1. Trader edits JSON (sets `manual_override: true`, adds `override_note`)
2. Validation before LLM ingestion (syntax + required fields + schema version)
3. Audit trail (`override_by`, `override_timestamp`, archive original)
4. LLM consumption notes override presence

**Maps To**: T801A-GDR-004 (File Format Standard), T801A-ADR-004 (TTI File Schema), T801A-QG-003 (Override-ability)

---

#### Finding 6: Price Action Signal Detection

**Summary**: Implement algorithmic swing-point detection for MVP; defer complex patterns.

**MVP Scope (Partial Algorithmic)**:
- **Higher Highs/Higher Lows (HH/HL)**: Detect via swing point algorithm
- **Swing Points**: Local maxima/minima with 2-bar confirmation on each side
- **Breakouts**: Price exceeds last swing high/low

**Pseudocode** (research-provided):
```python
# Identify swing highs/lows
for i in range(2, len(price)-2):
    if price[i] > price[i-1] and price[i] > price[i-2] and price[i] >= price[i+1] and price[i] >= price[i+2]:
        swing_highs.append((i, price[i]))
    if price[i] < price[i-1] and price[i] < price[i-2] and price[i] <= price[i+1] and price[i] <= price[i+2]:
        swing_lows.append((i, price[i]))

# Determine trend direction
if last_high > prev_high and last_low > prev_low:
    trend_direction = "Uptrend"
elif last_high < prev_high and last_low < prev_low:
    trend_direction = "Downtrend"
else:
    trend_direction = "Neutral"
```

**Deferred (Post-MVP)**:
- Complex patterns (head-and-shoulders, triangles, wedges)
- MSB/CHOCH/BOS semantic labeling (LLM interpretation layer)
- Advanced PA structure analysis

**Maps To**: T801A-ASSUM-002 (PA Detection Feasibility), T801A-IG-005 (PA Detection Methodology)

---

#### Finding 7: Divergence & Crossover Detection

**Summary**: Include MA crossovers in MVP; defer divergence detection.

**Trade-off Analysis Table** (research-provided):

| Pattern | Backend Feasibility | LLM Interpretive Value | Implementation Cost | Recommendation |
|:--------|:--------------------|:-----------------------|:--------------------|:---------------|
| **MA Crossover (50/200)** | High (deterministic) | Medium | Low | ✅ **Include MVP** |
| **MA Crossover (20/50)** | High | Medium | Low | ✅ **Include MVP** |
| **Regular RSI Divergence** | Medium (swing detection on RSI + price) | High | Medium | ❌ **Defer Post-MVP** |
| **Hidden RSI Divergence** | Low (subjective) | High | High | ❌ **Defer Post-MVP** |
| **MACD Divergence** | Medium | High | Medium | ❌ **Defer Post-MVP** |

**Rationale**:
- **MA Crossovers**: High feasibility + low cost + deterministic = MVP inclusion
- **Divergences**: Medium-low feasibility + tuning burden + false positive risk = defer until scoring validation stable

**Crossover Detection Pseudocode**:
```python
if MA_short[-2] < MA_long[-2] and MA_short[-1] > MA_long[-1]:
    cross_signal = "bullish"   # Golden cross
elif MA_short[-2] > MA_long[-2] and MA_short[-1] < MA_long[-1]:
    cross_signal = "bearish"   # Death cross
```

**Maps To**: T801A-CON-002 (Complexity Management), T801A-IG-006 (Crossover Detection)

---

## IV. CROSS-RESEARCH INTEGRATION MATRIX

### A. How Initiative Standards (T801-RES-001) Inform Epic Architecture (T801A-RES-001)

| Initiative Finding | Epic Integration Point | Governance Implication |
|:-------------------|:-----------------------|:-----------------------|
| **Timeframe Applicability Matrix** | Scoring weight calibration | Indicators excluded by matrix should not contribute to score; priority weights inform scoring formula |
| **OBV Volume Confirmation** | JSON schema `signals.volume` field | Add OBV trend confirmation to JSON output; OBV divergence flags reduce confidence |
| **Confidence System Design** | Scoring algorithm validation | Weighted voting framework validates -2 to +2 scale; precision/recall metrics apply to extreme scores |
| **Indicator Redundancy Constraints** | Scoring formula simplicity | Keep scoring formula to core indicators (MA, RSI, PA structure, OBV) to prevent overfitting |
| **Performance Evaluation Standards** | Validation methodology | Monthly/quarterly calibration cadence aligns with Initiative Standard 5 |

### B. Cross-Research Dependency Chain

```
T801-RES-001 (Initiative Standards)
    │
    ├─► Timeframe Matrix ──────────► T801A-DEP-001 (PineScript Enhancement)
    │                                   └─► Backend receives pre-filtered indicator data
    │
    ├─► OBV Recommendation ────────► T801A-IG-003 (Volume Confirmation)
    │                                   └─► JSON schema includes OBV trend field
    │
    ├─► Confidence Framework ──────► T801A-ASSUM-001 (Scoring Viability)
    │                                   └─► Validation methodology applied to scoring
    │
    └─► Initiative Standards 1-6 ──► T801 Future Work (PineScript Redesign, LLM_Trader Protocol)

T801A-RES-001 (Epic Architecture)
    │
    ├─► -2 to +2 Scoring ──────────► T801A-GDR-002 (Numeric Scoring Foundation)
    │                                   └─► T801A-ADR-002 (Scoring Algorithm Specification)
    │
    ├─► JSON File Format ──────────► T801A-GDR-004 (File Format Standard)
    │                                   └─► T801A-ADR-004 (TTI File Schema)
    │
    ├─► Swing/Breakout Detection ──► T801A-ASSUM-002 (PA Detection Feasibility)
    │                                   └─► T801A-IG-005 (PA Detection Methodology)
    │
    └─► MA Crossover MVP ──────────► T801A-CON-002 (Complexity Management)
                                        └─► T801A-IG-006 (Crossover Detection)
```

---

## V. E-RID MAPPING (PROPOSED)

Based on research findings, the following E-RID drafts are recommended for Subphases 1.1-1.5:

### A. Quality Goals (T801A-QG-###) — Subphase 1.1

| Proposed ID | Title | Research Basis | Draft Specification |
|:------------|:------|:---------------|:--------------------|
| **T801A-QG-001** | Deterministic Consistency | T801A-RES-001 §II (Scoring System) | Backend TTI generation SHALL produce identical output for identical input data across multiple runs. Scoring algorithms SHALL be deterministic (no randomness, no LLM variance). |
| **T801A-QG-002** | Signal Reliability | T801-RES-001 §IV (Confidence System) | Extreme trend scores (+2/-2) SHALL achieve ≥80% precision in backtesting. Overall classification accuracy SHALL exceed 70% threshold. |
| **T801A-QG-003** | Override-ability | T801A-RES-001 §III (Manual Override) | TTI output format SHALL support human readability and manual override with audit trail. Override workflow SHALL include validation and attribution. |
| **T801A-QG-004** | Maintainability | T801A-RES-001 §VI (Architecture) | Backend rule engine SHOULD use configuration-driven rules (JSON/YAML) for indicator thresholds and scoring weights. Hardcoded rules SHALL be minimized. |
| **T801A-QG-005** | Timeframe Correctness | T801-RES-001 §II (Timeframe Matrix) | TTI output SHALL only include indicators applicable to the analyzed timeframe per Initiative T801 timeframe applicability matrix. Irrelevant indicators SHALL NOT appear in output. |

### B. Dependencies (T801A-DEP-###) — Subphase 1.2

| Proposed ID | Title | Research Basis | Draft Specification |
|:------------|:------|:---------------|:--------------------|
| **T801A-DEP-001** | PineScript Enhancement | T801-RES-001 §II (Filter Logic) | Epic T801A requires PineScript filter logic implementing timeframe applicability matrix. Filter SHALL exclude irrelevant indicators (e.g., S_VWAP on 1D). |
| **T801A-DEP-002** | tv_ingest Backend | T801A-RES-001 §VI (Integration) | Epic T801A requires existing tv_ingest backend component for webhook processing and CSV generation. TTI calculation engine integrates into tv_ingest pipeline. |
| **T801A-DEP-003** | LLM_Trader Prompt Update | T801A-RES-001 §III (LLM Consumption) | Epic T801A requires LLM_Trader prompt modification to consume TTI file (JSON) instead of executing TTI protocol inline. |

### C. Assumptions (T801A-ASSUM-###) — Subphase 1.3

| Proposed ID | Title | Research Basis | Draft Specification |
|:------------|:------|:---------------|:--------------------|
| **T801A-ASSUM-001** | Numeric Scoring Viability | T801A-RES-001 §II (Validation) | We assume -2 to +2 scoring can achieve ≥70% accuracy and ≥80% extreme-score precision. Validity tested via playground validation with N≥100 days historical data. |
| **T801A-ASSUM-002** | PA Detection Feasibility | T801A-RES-001 §IV (Swing Detection) | We assume swing-point algorithm (2-bar confirmation) reliably detects trend direction and breakouts. Validity tested via manual trader review of 20+ sample classifications. |
| **T801A-ASSUM-003** | OBV Data Availability | T801-RES-001 §III (Volume) | We assume OBV is exportable from TradingView PineScript and available in webhook payload. Validity tested via PineScript prototype. |

### D. Implementation Guidance (T801A-IG-###) — Subphase 1.4

| Proposed ID | Title | Research Basis | Draft Specification |
|:------------|:------|:---------------|:--------------------|
| **T801A-IG-001** | Configuration-Driven Rules | T801A-RES-001 §II | Backend rule engine SHOULD use configuration files (JSON/YAML) to define indicator thresholds, timeframe-specific weights, and classification logic. |
| **T801A-IG-002** | Timeframe Filtering | T801-RES-001 §II (Matrix) | Backend SHALL validate incoming indicator set against timeframe applicability matrix. Irrelevant indicators SHALL be ignored in scoring. |
| **T801A-IG-003** | Volume Confirmation | T801-RES-001 §III (OBV) | Backend SHALL include OBV trend direction in scoring. Rising OBV + uptrend = confidence boost; falling OBV + uptrend = divergence flag. |
| **T801A-IG-004** | Confidence Scoring | T801-RES-001 §IV (Confidence) | Backend SHOULD implement weighted voting for composite trend score. Weights calibrated via backtesting with precision/recall metrics. |
| **T801A-IG-005** | PA Detection | T801A-RES-001 §IV | Backend SHALL implement swing-point algorithm with 2-bar confirmation. Trend direction derived from HH/HL or LH/LL patterns. |
| **T801A-IG-006** | Crossover Detection | T801A-RES-001 §V | Backend SHALL detect MA crossovers (50/200, optionally 20/50). Crossover signal included in JSON output with event date. |

### E. Constraints (T801A-CON-###) — Subphase 1.5

| Proposed ID | Title | Research Basis | Draft Specification |
|:------------|:------|:---------------|:--------------------|
| **T801A-CON-001** | Backward Compatibility | Plan file | Epic T801A development SHALL occur in isolated playground. Existing tv_ingest and LLM_Trader SHALL remain functional during development. |
| **T801A-CON-002** | Complexity Management | T801A-RES-001 §V (Divergence) | MVP SHALL NOT include automated divergence detection. Complex patterns (RSI/MACD divergence) deferred to post-MVP to maintain system determinism. |
| **T801A-CON-003** | Research-Gated Design | Both reports | File format, scoring thresholds, and PA detection parameters SHALL align with research recommendations. Deviations require explicit Client approval. |

### F. Interfaces (T801A-IF-###) — Subphase 1.6 

| Proposed ID | Title | Research Basis | Draft Specification |
|:------------|:------|:---------------|:--------------------|
| **T801A-IF-001** | TradingView Webhook Input Contract | T801A-RES-001 §VI (Integration); T801-RES-001 §II (Matrix) | Webhook payload interface SHALL include the required indicator set for the analyzed timeframe per the Initiative timeframe applicability matrix. Payload SHALL include timeframe + asset identifiers and a schema version for validation. Backend SHALL validate presence/format before scoring. |
| **T801A-IF-002** | Backend Output Artifact Contract (JSON) | T801A-RES-001 §III (File Format) | TTI output artifact SHALL be JSON with a lean, versioned schema. Output SHALL include `schema_version`, `trend_score`, `trend_label`, `signals` object, and manual override fields required for auditability. Output SHALL be human-readable and machine-validated. |
| **T801A-IF-003** | LLM_Trader Consumption Interface | T801A-RES-001 §III (LLM Consumption); `prompt/roles/VPA/main_v2.1.md` | LLM_Trader prompt interface SHALL consume the JSON artifact as the authoritative TTI input (not recompute TTI logic inline). LLM_Trader SHALL surface manual override presence and preserve audit trail fields in any downstream outputs. |

---

## VI. E-GDR/E-ADR CANDIDATE DECISIONS — Subphase 1.6

Based on research findings, the following governance decisions and paired architectural decisions are recommended:

### A. Proposed E-GDRs

| GDR ID | Title | Context Summary | Decision Summary | Research Basis |
|:-------|:------|:----------------|:-----------------|:---------------|
| **T801A-GDR-001** | Hybrid TTI Architecture | Current LLM-based TTI unreliable; inconsistent timeframe rule application | Adopt hybrid architecture: backend deterministic calculation → LLM interpretive layer | Both reports; Plan §II.B |
| **T801A-GDR-002** | Numeric Scoring Foundation | Subjective BEARISH/NEUTRAL/BULLISH classifications inconsistent | Adopt -2 to +2 scoring scale with defined thresholds per T801A-RES-001 | T801A-RES-001 §II |
| **T801A-GDR-003** | Playground-First Mandate | Daily trading operations depend on current system reliability | Mandate isolated playground for all T801A development; parallel deployment required | Plan §II.B; T801A-CON-001 |
| **T801A-GDR-004** | Backend File Format Standard | File format impacts LLM consumption, manual override, maintainability | Adopt JSON with lean schema per T801A-RES-001 | T801A-RES-001 §III |
| **T801A-GDR-005** | Initiative Standard Compliance | Epic T801A must align with Initiative T801 design standards | Epic SHALL comply with T801-RES-001 Initiative Standards 1-6 (timeframe filtering, OBV, confidence, etc.) | T801-RES-001 §V |

### B. Proposed E-ADRs (Paired with GDRs)

| ADR ID | Title | Paired GDR | Specification Summary | Research Basis |
|:-------|:------|:-----------|:----------------------|:---------------|
| **T801A-ADR-001** | Hybrid Integration Pattern | T801A-GDR-001 | Define integration pattern: file-based handoff, webhook trigger, LLM consumption protocol | T801A-RES-001 §VI |
| **T801A-ADR-002** | Scoring Algorithm Specification | T801A-GDR-002 | Define scoring formula: +1/-1 for direction, momentum, confirmation, contradiction; thresholds for each level | T801A-RES-001 §II |
| **T801A-ADR-003** | Playground Deployment Architecture | T801A-GDR-003 | Define playground infrastructure: branch strategy, feature flags, test data, validation gates | Plan §IV.C |
| **T801A-ADR-004** | TTI File Schema | T801A-GDR-004 | Define JSON schema: schema_version, trend_score, trend_label, signals object, override fields | T801A-RES-001 §III |
| **T801A-ADR-005** | Timeframe Applicability Enforcement | T801A-GDR-005 | Define enforcement mechanism: backend validation of indicator set against matrix | T801-RES-001 §II |

---

## VII. IMPLICATIONS FOR PHASE 1 SUBPHASES

### A. Impact Assessment

| Subphase | Current Status | Research Impact | Recommended Action |
|:---------|:---------------|:----------------|:-------------------|
| **1.1 (Quality Goals)** | Pending | High — Research provides measurable acceptance criteria (70%/80% accuracy thresholds) | Incorporate validation methodology into QG definitions |
| **1.2 (Dependencies)** | Pending | High — PineScript filter logic now has concrete pseudocode | Add T801A-DEP-001 with specific filter requirements |
| **1.3 (Assumptions)** | Pending | High — Scoring viability and PA feasibility now testable | Add validation test specifications to each assumption |
| **1.4 (Implementation Guidance)** | Pending | High — Detailed pseudocode available for swing detection, crossover detection, confidence scoring | Incorporate research pseudocode into IG specifications |
| **1.5 (Constraints)** | Existing draft | Medium — Divergence deferral aligns with complexity management | Formalize CON-002 with explicit MVP scope boundary |
| **1.6 (GDR/ADR Development)** | Pending | High — 5 GDRs and 5 ADRs now have research backing | Proceed with research-informed GDR/ADR development |
| **1.7 (Synthesis)** | Pending | Medium — Cross-research integration notes ready for proposal | Include integration matrix in Phase 1 proposal |

### B. Subphase 1.6 Preparation Checklist

Based on this analysis, the following are ready for Subphase 1.6 development:

- [x] **T801A-GDR-001 (Hybrid Architecture)**: Context and decision documented; awaits Client dialogue
- [x] **T801A-GDR-002 (Numeric Scoring)**: Research provides scale, thresholds, validation methodology
- [x] **T801A-GDR-003 (Playground-First)**: Plan file constraint; research validation methodology supports gate criteria
- [x] **T801A-GDR-004 (File Format)**: Research recommends JSON; schema example provided
- [x] **T801A-GDR-005 (Initiative Compliance)**: Initiative Standards 1-6 documented in T801-RES-001
- [x] **T801A-ADR-001 to ADR-005**: Specifications derivable from research pseudocode and examples

---

## VIII. GAP ANALYSIS & OPEN QUESTIONS

### A. Gaps Requiring Client Input

| Gap ID | Topic | Description | Recommended Resolution |
|:-------|:------|:------------|:-----------------------|
| **GAP-001** | Scoring Threshold Tuning | Research provides starting thresholds (ADX 25/30) but notes "fine-tuned on historical data" | Accept research defaults for MVP; plan post-MVP calibration |
| **GAP-002** | LLM_Trader Prompt Scope | Research assumes LLM consumes JSON but doesn't specify prompt modification extent | Defer to Feature T801A3 (Integration) scope definition |
| **GAP-003** | OBV Calculation Location | OBV could be calculated in PineScript or backend | Recommend: PineScript exports OBV value; backend consumes |
| **GAP-004** | Crossover Scope | Research mentions 50/200 and optionally 20/50; which to include MVP? | Recommend: 50/200 only for MVP (1D/4H focus); 20/50 for LTF in post-MVP |

### B. Primary Risks

| Risk ID | Description | Impact | Mitigation |
|:--------|:------------|:-------|:-----------|
| **RISK-001** | Scoring validation fails acceptance criteria | Phase 1 assumptions invalidated | Plan iterative calibration; define acceptable deviation range |
| **RISK-002** | PineScript filter logic not implementable | T801A-DEP-001 blocked | Prototype PineScript changes before committing to design |
| **RISK-003** | JSON token overhead impacts LLM performance | LLM context budget strained | Monitor token usage; implement schema compression if needed |

---

## IX. RECOMMENDATIONS & NEXT STEPS

### A. Immediate Recommendations

1. **Proceed with Subphases 1.1-1.5** using E-RID mappings in Section V
2. **Adopt research-recommended defaults** (JSON format, -2 to +2 scale, swing-point algorithm, OBV inclusion, divergence deferral)
3. **Incorporate validation methodology** into T801A-ASSUM-001 testing plan
4. **Use pseudocode examples** from research in Implementation Guidance specifications

### B. Client Decision Points

1. **Confirm E-RID draft mappings** (Section V) before Subphase 1.1-1.5 development
2. **Approve GDR/ADR candidate decisions** (Section VI) for Subphase 1.6 development
3. **Resolve Gap-001 to Gap-004** open questions before finalizing Implementation Guidance
4. **Accept risk mitigations** (Section VIII.B) or propose alternatives

### C. Next Steps (Subphase 1.0.1 Completion)

1. ✅ Research reports reviewed and key findings extracted
2. ✅ Cross-research integration analysis complete
3. ✅ E-RID mappings drafted
4. ✅ GDR/ADR candidates identified
5. ⏳ **Pending**: Client review and approval of this analysis
6. ⏳ **Next**: Begin Subphase 1.1 (Quality Goals Definition) upon approval

---

## X. APPENDIX

### A. Research Report References

| Research ID | File Path |
|:------------|:----------|
| T801-RES-001 | `prompt/artifacts/tasks/T801/research/report/report_T801-RES-001_indicator-design-standards.md` |
| T801A-RES-001 | `prompt/artifacts/tasks/T801/research/report/report_T801A-RES-001_backend-tti-architecture.md` |

### B. Context Material References

| Document | File Path |
|:---------|:----------|
| Plan File | `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` |
| LLM_Trader Prompt | `prompt/roles/VPA/main_v2.1.md` |
| T810 SPS Exemplar | `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md` |
| T810 Analysis Exemplar | `prompt/artifacts/tasks/T810/consultant/workspace/analysis/analysis_T810A-SYSTEM_dynamic-json-envelope-decision.md` |

### C. Terminology

| Term | Definition |
|:-----|:-----------|
| **TTI** | Timeframe Trend Identification — the protocol for assessing trend direction per timeframe |
| **E-RID** | Epic-level Requirements ID (QG, DEP, ASSUM, IG, CON categories) |
| **E-GDR** | Epic Governance Decision Record — policy-level governance decision |
| **E-ADR** | Epic Architectural Decision Record — implementation-level specification paired with GDR |
| **HH/HL** | Higher Highs / Higher Lows — price structure indicating uptrend |
| **LH/LL** | Lower Highs / Lower Lows — price structure indicating downtrend |
| **OBV** | On-Balance Volume — cumulative volume indicator for trend confirmation |
| **CVD** | Cumulative Volume Delta — order flow indicator (deferred from MVP) |
| **MA Crossover** | Moving Average Crossover — signal when short MA crosses long MA |

---

**Document Status**: Draft
**Approval Required**: Client review before proceeding to Subphase 1.1
**Next Review**: Upon Client feedback
