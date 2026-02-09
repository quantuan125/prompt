---
artifact_type: 'NOTES'
initiative_id: 'T801'
epic_id: 'T801A'
epic_code: 'TTI'
version: '1.0.0'
date: '2026-01-09'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md'
governance_rules: 'prompt/artifacts/tasks/T810/consultant/workspace/workspace_documentation_rules.md'
target_document: 'prompt/artifacts/tasks/T801/consultant/workspace/proposal/T801A_proposal_v1.0.0.md'
target_section: 'III.C.1 (Epic: T801A)'
---

# PHASE 1 PROPOSAL: `T801A / TTI` — Epic Requirements & Governance

## I. EXECUTIVE SUMMARY


---


## II. CONSULTANCY DIALOGUE NOTES (WORKING; NON-NORMATIVE)
<!-- PURPOSE: Capture raw dialogue so nothing is lost; convert into normative bodies above. -->

### A. DEP Dialogue Notes

**Dialogue Date**: 2025-12-29
**Status**: Category confirmed pending cross-category review

**Key Refinements from Research Baseline**:
1. **DEP-001 Title Refinement**: Renamed from "PineScript Enhancement" to "Timeframe-Correct Input" to decouple the dependency (what we need: correct dataset) from the implementation solution (how we achieve it: PineScript OR backend filtering). Client confirmed flexibility between enforcement mechanisms.

2. **DEP-002 Behavioral Contract Clarification**: Confirmed dependency is on behavioral contract stability (webhook in, data out), not code structure. Internal refactors are acceptable. Sandbox development mandate added to ensure operational continuity.

3. **DEP-003 Fallback Strategy**: Confirmed that fallback to inline TTI format is acceptable during transition if JSON artifact is missing or stale, balancing determinism goals with operational pragmatism.

**Cross-Category Implications Discovered**:
- **CON**: Sandbox development requirement (T801A-CON-007 candidate) — isolated environment needed to maintain behavioral contract stability during development
- **ASSUM**: TradingView platform reliability (T801A-ASSUM-006 candidate) — webhook rate limits and payload size constraints may exist but are uncertain; research did not definitively cover this
- **IG**: Initiative Matrix Reference (T801A-IG-007 confirmed) — backend filtering logic SHALL reference T801-RES-001 timeframe applicability matrix as authoritative source

**Ownership Confirmed**:
- Accountability: Client
- Responsibilities: LLM_Consultant (Epic T801A)

**Open Questions Identified**: None for DEP category; cross-category questions logged in Open Questions Register.

### B. CON Dialogue Notes

**Dialogue Date**: 2025-12-30
**Status**: Category confirmed pending cross-category review

**T102 Compliance Analysis**:
Per `T102-STD-005-FR-004`, CON = "Non-negotiable boundary or limitation that must be respected". Items allowing deviation with approval are NOT true constraints and must be reclassified.

**Category Reclassification Decisions**:

| Original ID | Original Title | Assessment | Action |
|:------------|:---------------|:-----------|:-------|
| CON-001 | Backward Compatibility | ✅ True CON — production cutover is hard gate | RETAIN |
| CON-002 | Operational Continuity | ✅ True CON — "MUST NOT be disrupted" is absolute | RETAIN |
| CON-003 | Research-Gated Design | ⚠️ Conditional — "deviations require approval" | → IG-008 |
| CON-004 | Integration Boundary | ⚠️ Conditional — "refactors require approval" | → IG-009 |
| CON-005 | Manual Workflow | ✅ True CON — MVP scope boundary is non-negotiable | → CON-003 |
| CON-006 | Complexity Management | ✅ True CON — MVP scope boundary is absolute | → CON-004 |

**Key Refinements from Research Baseline**:

1. **CON-001 Sandbox Mandate Consolidation**: DEP dialogue identified CON-007 candidate (Sandbox Development Mandate). Per Client direction (Option A), this is an enforcement mechanism for CON-001/002, not a separate constraint. Sandbox requirement now explicitly stated in CON-001 specification.

2. **CON-002 Scope Expansion**: Client clarified "trading operations" scope = entire ecosystem (Option C): LLM_Trader + tv_ingest + analytics + position management. This broader scope affects how we define "disruption" and test boundaries.

3. **CON-003 Rationale Documentation**: Manual workflow acceptance rationale confirmed as hybrid (Option A priority): simplicity focus + platform separation (LLM_Trader on web interface, backend on local system) + operational pragmatism (trader review before LLM consumption).

4. **Constraint vs IG Classification**: Per T102 definition, items with "deviations require approval" language are guidance (IG), not absolute boundaries (CON). Two items reclassified to preserve CON category integrity.

**Gap Items Assessed (Deferred to IG)**:

| Gap ID | Description | Decision |
|:-------|:------------|:---------|
| GAP-CON-A | Token Budget Ceiling | → IG-010; Feature-level + RES needed |
| GAP-CON-B | Validation Threshold Gate | → IG-011; qualitative at Epic level |
| GAP-CON-C | No External Dependencies | → IG-012; "SHOULD" language = guidance |
| GAP-CON-D | Feature Flag Requirement | NOT NEEDED; Client clarified sandbox→full integration model |

**Enforcement Mechanisms Confirmed**:

| Constraint | Enforcement Authority | Phase |
|:-----------|:---------------------|:------|
| CON-001 | Client (decision owner) | Before production deployment |
| CON-002 | LLM_Developer (operational monitoring) | Continuous during development |
| CON-003 | N/A (scope boundary) | MVP definition phase |
| CON-004 | LLM_Developer (reject divergence PRs) | During Feature implementation |

**Ownership Confirmed**:
- Accountability: Client
- Responsibilities: LLM_Consultant (Epic T801A)

**Cross-Category Implications Discovered**:
- **DEP**: CON-001/002 validate DEP-002 sandbox specification; behavioral contract stability reinforced
- **ASSUM**: CON-002 scope (entire ecosystem) informs ASSUM-004 (Platform Reliability) scope
- **QG**: CON-001 sandbox mandate provides validation environment context for QG-002 (Signal Reliability)
- **IF**: CON-002 operational continuity impacts IF-001/002/003 behavioral stability requirements
- **IG**: 5 new IG items from CON dialogue (IG-008 through IG-012)

**Open Questions Identified**: None for CON category; cross-category questions addressed in dialogue.

### C. ASSUM Dialogue Notes

**Dialogue Date**: 2025-12-31
**Status**: Category confirmed pending cross-category review

**T102 Compliance Analysis**:
Per `T102-STD-005-FR-009 (Assumption Rules)`, ASSUM items follow validation lifecycle with status tracking (Pending/Validated/Invalidated/Modified). Validation timing and method specified per assumption.

**Category Refinement Decisions**:

| Original ID | Original Title | Assessment | Action |
|:------------|:---------------|:-----------|:-------|
| ASSUM-001 | Numeric Scoring Viability | Reframed to "Feasibility" — distinguishes belief (ASSUM) from target (QG) | REFINED |
| ASSUM-002 | PA Detection Feasibility | Qualitative language maintained; simpler alternatives may be explored | RETAINED |
| ASSUM-003 | OBV Data Availability | Reframed to "Volume Integration Value" — core assumption is value-add, not exportability | REFINED + RISK FLAGGED |
| ASSUM-004 | Platform Reliability | Merged with ASSUM-006 (webhook constraints) → "External Platform Sufficiency" | MERGED |
| ASSUM-005 | Operational Acceptance | Explicit CON-003 cross-reference added per T102-STD-005-FR-009 | RETAINED + CROSS-REF |
| ASSUM-006 | Webhook Rate Constraints | Merged into ASSUM-004 | → ASSUM-004 |
| NEW | LLM Performance Stability | Added from dialogue discovery (GAP-ASSUM-D) | ADDED as ASSUM-006 |

**Key Refinements from Research Baseline**:

1. **ASSUM vs QG Clarification**: Per T102 definitions, ASSUM = "unverified belief shaping approach" vs QG = "measurable acceptance criterion". Research-derived quantitative thresholds (70% accuracy, 80% precision) belong in QG-002, not ASSUM-001. ASSUM-001 reframed to focus on feasibility belief.

2. **ASSUM-003 Value vs Exportability**: Original ASSUM-003 assumed "OBV can be exported" which is trivially testable. Client clarified the core uncertainty is whether OBV integration ADDS VALUE to TTI output. OBV is a new addition to TTI protocol with significant risk. Fallback strategy: complete removal if validation fails.

3. **ASSUM-004/006 Merge**: Both addressed TradingView platform constraints. Merged into single "External Platform Sufficiency" assumption covering reliability, rate limits, and payload capacity.

4. **ASSUM-005 CON Cross-Reference**: Per T102-STD-005-FR-009, ASSUM items extending CON items SHOULD explicitly reference the governing CON-ID. ASSUM-005 now references T801A-CON-003.

5. **Validation Lifecycle**: Per T102-STD-005-FR-009, each ASSUM specifies validation method, responsible party, and timing (typically Feature SRS development or implementation testing).

**Gap Items Assessed**:

| Gap ID | Description | Decision |
|:-------|:------------|:---------|
| GAP-ASSUM-A | Data Quality (master.csv) | → DEP-004; structural dependency, not assumption |
| GAP-ASSUM-B | Indicator Stability (TradingView) | Covered by ASSUM-004 (platform sufficiency) |
| GAP-ASSUM-C | Context Budget | Validated (1M context vs 100k target); IG-010 covers optimization |
| GAP-ASSUM-D | LLM Performance | → ASSUM-006; concern is performance, not fit |

**Invalidation Consequences (All Recoverable)**:

| ASSUM | If Invalid | Consequence | Fallback |
|:------|:-----------|:------------|:---------|
| ASSUM-001 | Scoring system inaccurate | Recalibration needed | Modify formula with Client approval |
| ASSUM-002 | Swing-point unreliable | Alternative PA approach needed | Feature-level research for simpler alternatives |
| ASSUM-003 | OBV adds no/negative value | Volume confirmation removed | Proceed without volume signal |
| ASSUM-004 | Platform unreliable | Operational impact | Design caching/fallback (scope change) |
| ASSUM-005 | Workflow rejected | Usability redesign | Accelerate automation (post-MVP) |
| ASSUM-006 | Performance degraded | Context optimization needed | Reduce artifact size or restructure prompts |

**Cross-Category Implications Discovered**:
- **DEP**: DEP-004 (Expanded Data Structure) discovered — master.csv requires multi-candle historical data
- **QG**: QG-007 (Consolidated Output Artifact) discovered — combine market data + TTI output for trader convenience
- **CON**: ASSUM-005 explicitly extends CON-003 (cross-reference per T102-STD-005-FR-009)
- **RISK**: T801A-RISK-009 (Volume Integration Risk) created — ASSUM-003 high-risk item

**Ownership Confirmed**:
- Accountability: Client
- Responsibilities: LLM_Consultant (Epic T801A)

**Open Questions Identified**: None for ASSUM category; cross-category items addressed in dialogue.

### D. QG Dialogue Notes

**Dialogue Date**: 2025-12-31
**Status**: Category confirmed pending cross-category review

**T102 Compliance Analysis**:
Per T102-STD-005 category definitions, QG = "Measurable acceptance criteria that define success." Unlike ASSUM (beliefs) or CON (boundaries), QG items define testable targets the Epic must achieve.

**Category Refinement Decisions**:

| Original ID | Original Title | Assessment | Action |
|:------------|:---------------|:-----------|:-------|
| QG-001 | Deterministic Consistency | Expanded to include Interpretability (GAP-QG-B) + Reproducibility (GAP-QG-D) | EXPANDED |
| QG-002 | Signal Reliability | Research-derived thresholds retained with "subject to optimization" clause | RETAINED + NOTE |
| QG-003 | Manual Override | Scope simplified to file-level manual override per CON-003/ASSUM-005 | SIMPLIFIED |
| QG-004 | Rule Maintainability | No change | RETAINED |
| QG-005 | Timeframe Correctness | No change | RETAINED |
| QG-006 | Latency & Resource Efficiency | Quantified with guidance targets (<1 min ideal, ≤3 min max, normal load) | REFINED |
| QG-007 | Consolidated Output | Reframed to "Context Sufficiency" — no consolidation; TTI output replaces master.csv | REFRAMED |
| NEW | MVP Simplicity | Added for Feature-level prioritization (simplicity, low complexity, speed) | ADDED as QG-008 |

**Key Refinements from Research Baseline**:

1. **QG-001 Expansion (Interpretability + Reproducibility)**: Research GAP-QG-B (Interpretability) and GAP-QG-D (Reproducibility) identified as essential for deterministic system. Folded into QG-001 rather than separate QGs — transparent calculation framework must produce interpretable, reproducible results.

2. **QG-002 Threshold Flexibility**: Research-derived thresholds (70%/80%/20%) retained as starting points with explicit "subject to calibration/optimization" clause. Threshold modifications require documented rationale and Client approval.

3. **QG-003 Scope Simplification**: Original QG-003 scope included backend-implemented override logic with audit trail. Client identified scope creep risk. **Decision**: Simplify to file-level manual editing during manual handoff per CON-003/ASSUM-005. Backend produces correct output; override is trader responsibility post-output.

4. **QG-006 Quantification**: Research did not provide specific latency targets. Client provided operational context: current system produces master.csv in sub-seconds to seconds. **Decision**: <1 min ideal, ≤3 min max under normal load. Targets are guidance subject to Feature-level refinement.

5. **QG-007 Reframing (Context Sufficiency)**: Original "Consolidated Output" suggested file merging. Client clarified: no consolidation needed. TTI output JSON artifact is the sole input to LLM_Trader, replacing both inline TTI protocol AND master.csv. Content scope (Option B vs C) deferred to Feature T801A1 exploration.

6. **QG-008 MVP Simplicity**: Client emphasized need for QG enforcing simplicity prioritization across Feature development. Assessment criteria SHOULD weight simplicity, low complexity, and speed highly.

**Gap Items Assessed**:

| Gap ID | Description | Decision |
|:-------|:------------|:---------|
| GAP-QG-A | Schema Versioning | Covered by IF-002 (Output Artifact Contract); no separate QG needed |
| GAP-QG-B | Interpretability | → Folded into QG-001 (calculation framework must be transparent) |
| GAP-QG-C | Error Handling | → IG-015 (implementation guidance, not measurable goal) |
| GAP-QG-D | Reproducibility | → Folded into QG-001 (results reproducible across system updates) |

**Cross-Category Implications Discovered**:
- **CON**: CON-003 cross-reference update — QG-003 override workflow explicitly leverages manual handoff
- **ASSUM**: ASSUM-005 cross-reference update — QG-003 override acceptance is validation criterion
- **DEP**: DEP-004 clarification — feeds TTI calculation; TTI output replaces master.csv per QG-007 (no consolidation)
- **IF**: IF-002 requires "human-editable format" clause per QG-003; IF-003 requires "sole input artifact" clause per QG-007
- **IG**: 3 new IG candidates from QG dialogue — IG-013 (Override Workflow), IG-014 (Context Content), IG-015 (Error Handling)

**IG Coverage Assessment**:

| QG | IG Coverage | Status |
|:---|:------------|:-------|
| QG-001 | IG-005 (PA Detection), IG-006 (Crossover Detection) | ✅ Covered |
| QG-002 | IG-003 (Volume Confirmation), IG-004 (Confidence Scoring), IG-011 (Validation Guidance) | ✅ Covered |
| QG-003 | IG-013 (Override Workflow) — NEW | ⏳ To be confirmed in IG dialogue |
| QG-004 | IG-001 (Configuration-Driven Rules) | ✅ Covered |
| QG-005 | IG-002 (Timeframe Filtering), IG-007 (Initiative Matrix Reference) | ✅ Covered |
| QG-006 | IG-010 (Artifact Size Guidance) | ✅ Covered |
| QG-007 | IG-014 (Context Content) — NEW | ⏳ To be confirmed in IG dialogue |
| QG-008 | IG-012 (Dependency Minimization) | ✅ Covered |
| GAP-QG-C | IG-015 (Error Handling) — NEW | ⏳ To be confirmed in IG dialogue |

**Ownership Confirmed**:
- Accountability: Client
- Responsibilities: LLM_Consultant (Epic T801A)

**Open Questions Identified**: None for QG category; cross-category items (IF-002/IF-003 updates, IG-013/014/015) to be addressed in subsequent dialogues.

### E. IF Dialogue Notes

**Dialogue Date**: 2026-01-01
**Status**: Category confirmed pending T801A-RES-002 research for IF-001 finalization

**T102 Compliance Analysis**:
Per T102-STD-005 category definitions, IF = "Interface contracts defining handoffs between system components." IF items specify input/output contracts, data formats, and consumption behavior.

**Category Refinement Decisions**:

| Original ID | Original Title | Assessment | Action |
|:------------|:---------------|:-----------|:-------|
| IF-001 | TradingView Webhook Input | Schema governance undefined; needs research | ⚠️ PARTIAL — pending T801A-RES-002 |
| IF-002 | Backend Output Artifact | Required fields defined; Option B (TTI + minimal context) selected | CONFIRMED |
| IF-003 | LLM_Trader Consumption | Sole input artifact; silent override handling | CONFIRMED |

**Key Refinements from Dialogue**:

1. **IF-001 Schema Governance Gap**: Client identified lack of governance standard for webhook schema versioning between T801A1 (Backend) and T801A2 (PineScript). Current webhook payload is "a bunch of text with data points" — no formal schema. **Resolution**: Commission T801A-RES-002 to document current structure and propose governance model.

2. **IF-001 Validation Failure**: Client prefers Option B+C combination (best-effort processing + error artifact) but concerned about QG-008 MVP Simplicity violation. **Resolution**: Delegate to IG-015 (Error Handling); research to inform implementation approach.

3. **IF-002 Required Fields**: Derived from current TTI protocol (RESOURCE section) + research findings:
   - HTF Reference (higher timeframe assessment)
   - Price Action (PA patterns, breakout signals)
   - VWAP (S/D/W/M_VWAP values + position assessment)
   - RSI (RSI + RSI_MA values + assessment)
   - Moving Averages (EMA_9/21/50/200, SMA_200 + assessment)
   - Volume (OBV trend direction + confirmation) — **added per Client feedback**
   - Overall Assessment (final trend with caution flags)

4. **IF-002 Context Scope**: Client selected **Option B (TTI + minimal market context)** over Option A (TTI only). "Minimal market context" scope to be defined by T801A-RES-002 research. Initial scope includes current price, VWAP levels, and key indicator values.

5. **IF-002 Override Fields**: `manual_override` boolean sufficient for MVP (simplified from full audit trail).

6. **IF-003 Override Handling**: **Option A (Silent)** selected — LLM_Trader processes TTI as-is; trader responsible for noting override context.

**Gap Items Assessed**:

| Gap ID | Description | Disposition | Rationale |
|:-------|:------------|:------------|:----------|
| GAP-IF-A | Error Output Interface | → IG-015 | Error handling is implementation guidance, not contract specification |
| GAP-IF-B | Configuration Interface | → IG (future) | Internal configuration loading is implementation concern |
| GAP-IF-C | Historical Data Interface | → IG-016 | Expanded master.csv format is implementation guidance for DEP-004 |
| GAP-IF-D | Schema Evolution Interface | → T801A-RES-002 | Requires architectural research before governance decision |

**Cross-Category Implications**:
- **T801A-RES-002**: System Architecture Research commissioned — addresses IF-001 schema governance + system pipeline mapping + "minimal market context" definition
- **IG-014**: Context Content guidance updated — "minimal market context" scope pending T801A-RES-002
- **IG-016**: Historical Input Format added — guidance for expanded master.csv structure
- **QG-007**: Context scope confirmed as Option B (TTI + minimal context)
- **DEP-004**: Clarified — feeds backend; TTI output replaces master.csv delivery to LLM_Trader

**Ownership Confirmed**:
- Accountability: Client
- Responsibilities: LLM_Consultant (Epic T801A)

**Open Items for T801A-RES-002**:
1. Current webhook payload structure documentation
2. Schema version governance model proposal
3. "Minimal market context" definition for IF-002 Option B
4. Error handling patterns in current tv_ingest backend
5. Historical data format requirements for DEP-004/IG-016

### F. IG Dialogue Notes

**Dialogue Date**: 2026-01-02
**Status**: Category confirmed with 16 IG items (1 partial pending T801A-RES-002)

**T102 Compliance Analysis**:
Per T102-STD-005-FR-004 category definitions, IG = "Normative authoring/process guidance (internal); not a design choice." IG items provide implementation patterns and execution guidance for downstream Feature development.

**Research-Derived IG (IG-001 to IG-006) — Confirmed with Refinements**:

| Original ID | Original Title | Assessment | Action |
|:------------|:---------------|:-----------|:-------|
| IG-001 | Configuration-Driven Rules | ✅ Appropriate guidance | RETAINED |
| IG-002 | Timeframe Filtering | ✅ Appropriate guidance | RETAINED |
| IG-003 | Volume Confirmation (OBV) | ⚠️ Specific pattern | GENERALIZED — OBV as baseline, alternatives permitted |
| IG-004 | Confidence Scoring | ⚠️ Specific approach | EXPANDED — Renamed "Scoring Mechanism Guidance"; unified scope |
| IG-005 | PA Detection | ❌ Design choice | GENERALIZED — swing-point as T801A-RES-001 baseline, alternatives per QG-008 |
| IG-006 | Crossover Detection | ❌ Design choice | GENERALIZED — configurable per IG-001; 50/200 as T801A-RES-001 baseline |

**Key Refinements from Dialogue**:

1. **IG-003/004/005/006 Generalization**: Per Client feedback, these items were too specific (prescribing algorithms rather than providing guidance). Refined to provide research baselines while preserving Feature-level flexibility per QG-008 (MVP Simplicity).

2. **IG-004 Scope Expansion**: Client approved merging "Confidence Scoring" into broader "Scoring Mechanism Guidance" covering: individual indicator contributions, weight assignment, composite aggregation, and calibration methodology.

3. **IG-005/IG-006 Research References**: Per Client Comment 1, explicitly reference T801A-RES-001 as design choice baseline for swing-point algorithm and 50/200 crossover recommendation.

4. **IG-015 Scope Expansion**: Client approved consolidating input validation AND output validation under single "Data Validation" guidance item. Covers IF-001 input validation and IF-002 schema validation per "machine-validated" clause.

5. **IG-014 Baseline Added**: Per Client selection (Hybrid A+B), added baseline scope (current price, VWAP levels, key indicator values) while marking partial pending T801A-RES-002.

**Confirmed from DEP Dialogue**:
- **IG-007 (Initiative Matrix Reference)**: Backend filtering logic SHALL reference T801-RES-001 timeframe applicability matrix as authoritative source for indicator inclusion/exclusion rules. Identified as implementation guidance rather than a dependency.

**Confirmed from CON Dialogue (Reclassified Items)**:
- **IG-008 (Research Alignment)**: Implementation SHOULD align with research outcomes (T801-RES-001, T801A-RES-001); deviations require documented rationale and Client approval. Reclassified from CON-003 — "deviations require approval" = guidance, not absolute boundary.
- **IG-009 (Integration Scope)**: Epic SHALL integrate as extension to existing tv_ingest; fundamental architecture changes SHOULD be escalated as separate Initiative work. Reclassified from CON-004 — "refactors require approval" = guidance, not absolute boundary.

**Confirmed from CON Dialogue (Gap-Derived Items)**:
- **IG-010 (Artifact Size Guidance)**: JSON artifact SHOULD be optimized for LLM context budget; exact thresholds to be determined via Feature-level research. From GAP-CON-A.
- **IG-011 (Validation Guidance)**: Scoring system SHOULD demonstrate acceptable accuracy via playground validation; quantitative thresholds defined at Feature level. From GAP-CON-B.
- **IG-012 (Dependency Minimization)**: MVP SHOULD avoid introducing new external service dependencies beyond established TradingView integration. From GAP-CON-C.

**Confirmed from QG Dialogue**:
- **IG-013 (Override Workflow)**: Manual file editing workflow for post-output override per CON-003/ASSUM-005.
- **IG-014 (Context Content)**: Baseline scope defined; full scope pending T801A-RES-002.
- **IG-015 (Data Validation)**: Expanded from "Error Handling" to cover input + output validation.

**Confirmed from IF Dialogue**:
- **IG-016 (Historical Input Format)**: Guidance on expanded master.csv structure per DEP-004; pending T801A-RES-002.

**Gap Analysis (No New IG Needed)**:

| Gap ID | Description | Disposition | Rationale |
|:-------|:------------|:------------|:----------|
| GAP-IG-A | Schema Versioning Coordination | Covered by T801A-RES-002 | Research will propose governance model |
| GAP-IG-B | Prompt Modification Patterns | Feature-level concern | IF-003 defines contract; T801A3 implements |
| GAP-IG-C | Testing Coordination | Covered by IG-011 | Playground validation covers cross-feature testing |

**Design Choice Assessment**:

Per T102-STD-005-FR-004, IG is "not a design choice." Items with specific algorithm prescriptions were assessed and generalized:

| IG | Classification | Resolution |
|:---|:---------------|:-----------|
| IG-003 | Specific pattern (OBV) | Generalized: "research baseline, alternatives permitted" |
| IG-004 | Specific approach (weighted voting) | Generalized: unified scoring guidance with baseline |
| IG-005 | Design choice (swing-point) | Generalized: "T801A-RES-001 baseline, alternatives per QG-008" |
| IG-006 | Design choice (50/200) | Generalized: "configurable, T801A-RES-001 recommends baseline" |

**GDR/ADR Candidates Identified**:

Per Client Comment 2, IG dialogue confirmed research integration supports the following governance decisions (detailed in Subphase 1.2 of plan file):

| GDR ID | Title | Related IG |
|:-------|:------|:-----------|
| T801A-GDR-001 | Hybrid TTI Architecture | IG-009 |
| T801A-GDR-002 | Numeric Scoring Foundation | IG-004 |
| T801A-GDR-003 | Playground-First Mandate | IG-011 |
| T801A-GDR-004 | Backend File Format Standard | IG-010, IG-015 |
| T801A-GDR-005 | Initiative Standard Compliance | IG-007, IG-008 |

**Cross-Category Implications**:
- **IF-002**: Added cross-reference to IG-015 for output validation per "machine-validated" clause
- **Research**: IG-005/IG-006 now explicitly reference T801A-RES-001 as design choice baseline
- **Subphase 1.2**: GDR/ADR candidates confirmed for governance development

**Ownership Confirmed**:
- Accountability: Client
- Responsibilities: LLM_Consultant (Epic T801A)

---

### G. Subphase 1.2 — GDR/ADR Development Dialogue Notes

**Dialogue Date**: 2026-01-03
**Activity**: Subphase 1.2 (Epic Governance Decisions)
**Purpose**: Develop E-GDR bodies with paired E-ADR specifications per T102-STD-004 compliance

**Research Baseline Presentation**:
- **Initial Candidates**: 5 GDRs + 5 ADRs from analysis file (research integration + IG dialogue)
- **Source**: `analysis_T801A-SYSTEM_research-integration.md` Section VI + Activity 1.1.6 IG dialogue

**Socratic Dialogue — Key Questions & Decisions**:

1. **Q1 (Gap Analysis):**
   - **GAP-GDR-A (Research Gating)**: Confirmed need for explicit baseline/flexible classification → **Created GDR-006/ADR-006** (Research Baseline Adoption)
   - **GAP-GDR-B (MVP Scope Boundary)**: Assessed as already covered by SSOT scope + CON-003/CON-004 → **No new GDR needed**

2. **Q2 (GDR-ADR Pairing Model):**
   - **Decision**: Maintain 1:1 pairing per QG-008 (MVP Simplicity)
   - **Rationale**: Simpler governance; split GDRs if multi-ADR needed rather than 1:N pairing

3. **Q3 (ADR Specification Depth):**
   - **Decision**: Option C (Hybrid) approved
   - **Pattern-Level**: ADR-001 (Integration), ADR-003 (Playground), ADR-005 (Timeframe Enforcement)
   - **Specification-Level**: ADR-002 (Scoring Algorithm), ADR-004 (TTI Schema), ADR-006 (Research Baseline)

4. **Q4 (GDR-003 Playground Scope):**
   - **Decision**: Option A (Minimal) approved per QG-008
   - **Scope**: Branch strategy (`feature/t801a-tti`) only; no feature flags or CI/CD infrastructure for MVP

5. **Q5 (Research Timing - T801A-RES-002):**
   - **Decision**: Proceed in parallel — Subphase 1.2 now; commission RES-002 in Activity 1.3.1
   - **Partial Items**: ADR-001 (pipeline mapping) and ADR-004 (context scope) marked partial pending RES-002

**Final GDR/ADR Inventory**:

| Item | Count | Key Changes from Initial Candidates |
|:-----|:------|:------------------------------------|
| **E-GDRs** | 6 | +1 (GDR-006 Research Baseline Adoption per GAP-GDR-A) |
| **E-ADRs** | 6 | +1 (ADR-006 Research Baseline Specification); ADR-003 scope minimized to branch strategy only |
| **Partial** | 2 | ADR-001 (pipeline), ADR-004 (context) pending T801A-RES-002 |

**GDR-006/ADR-006 Scope (NEW)**:
- **Mandatory Baselines (SHALL)**: Numeric scoring scale, JSON format, timeframe matrix enforcement, 50/200 MA crossover inclusion
- **Flexible Guidances (SHOULD/MAY)**: Swing-point PA detection, OBV volume confirmation, weighted voting formula, 20/50 MA crossover
- **Deviation Workflow**: Mandatory baselines require Client approval; flexible guidances require documented rationale per IG-008

**T102-STD-004 Compliance Validation**:
- **FR-001 (DR Index Schema)**: ✅ All 6 GDR + 6 ADR entries follow required schema (ID, Title, Status, Owner, Effective, Supersedes, Anchor)
- **FR-002 (Decision Records Body)**: ✅ All bodies use required format with proper anchors and subheading structure
- **FR-005 (Cross-Artifact Linking)**: ✅ GDRs include "Adopt `<ADR-ID>`..." statements in Decision section; ADRs include "Per `<GDR-ID>`..." citations in Context section
- **FR-006 (Anchor Title Stability)**: ✅ All anchors use lower-kebab format prefixed with ID (e.g., `#t801a-gdr-001-hybrid-tti-architecture`)

**Key Outcomes**:
1. **Complete GDR/ADR Bodies**: All 6 GDRs (Section IV.B) and 6 ADRs (Section IV.D) developed with full T102-STD-004 compliance
2. **Research Baseline Classification**: Explicit mandatory vs flexible distinction guides Feature-level development per QG-008
3. **Minimal Complexity Preserved**: Playground deployment (ADR-003) scoped to branch strategy; no over-engineering
4. **Partial Items Tracked**: ADR-001/ADR-004 to be finalized after T801A-RES-002 commission (Activity 1.3.1)
5. **Cross-Category Integration**: GDR/ADR specifications reference all 41 E-RIDs from Subphase 1.1

**Ownership Confirmed**:
- Accountability: Client
- Responsibilities: LLM_Consultant (Epic T801A)

---

### H. Subphase 1.3 — Research Integration & Risk Assessment Dialogue Notes

**Dialogue Date**: 2026-01-05
**Activity**: Subphase 1.3 (Activity 1.3.1 Research Commission + Activity 1.3.3 Risk Assessment)
**Purpose**: Integrate T801A-RES-002 findings to finalize partial E-RIDs, complete partial E-ADRs, and import Issues/Risks register

**Activity 1.3.1 — Research Commission Completion**:
- **Research Commissioned**: T801A-RES-002 (System Architecture Research) per plan file Activity 1.3.1
- **Research Delivered**: 6 topics covered — Pipeline Map, Webhook Contract, Storage Schema Drift, Minimal Context, Historical Format, Schema Governance
- **Key Verdicts**:
  - GO: Finalize IF-001 for Base 20-column webhook contract
  - NO-GO: Enhanced 44-column contract (not emitted by Pine today)
  - RESOLVED: IG-014 (minimal context ~1558 chars), IG-016 (5 bars chart TF, 1 bar others)
  - COMPLETE: ADR-001 (pipeline diagram), ADR-004 (context scope)

**Research Integration Summary**:

| E-RID/ADR | Pre-Research Status | Post-Research Action | Outcome |
|:----------|:-------------------|:---------------------|:--------|
| **IF-001** | ⚠️ Partial | Finalized with Base 20-column schema + TradingView constraints | ✅ Confirmed |
| **IG-014** | ⚠️ Partial | Finalized with lean JSON spec (~1500-2000 chars) | ✅ Confirmed |
| **IG-015** | Confirmed | Updated with HTTP 4xx response guidance | ✅ Confirmed |
| **IG-016** | Confirmed | Updated with 5-bar/1-bar depth specifics | ✅ Confirmed |
| **ASSUM-004** | Confirmed | Updated with TradingView operational constraints + fallback | ✅ Confirmed |
| **DEP-004** | Confirmed | Updated with historical depth clarification | ✅ Confirmed |
| **ADR-001** | ⚠️ Partial | Added FR-006 (Pipeline Mapping with Mermaid diagram) | ✅ Confirmed |
| **ADR-004** | ⚠️ Partial | Updated FR-006 (Minimal Market Context Scope) | ✅ Confirmed |

**TradingView Platform Constraints** (Environmental — per T801A-RES-002):
- Processing timeout: ~3 seconds before cancellation
- Message body cap: 40,960 characters
- Resend on 5xx: Up to 3 retries (4 total deliveries)
- Timestamp formatting: `str.format()` always UTC+0 (ISSUE-007)
- Port restrictions: Only 80/443

**Activity 1.3.3 — Issues/Risks Register Import**:

**Issues Imported (8 total)**:
| Priority | Count | Key Items |
|:---------|:------|:----------|
| HIGH | 5 | ISSUE-001 (Schema Confusion), ISSUE-004 (Dedup Data Loss), ISSUE-006 (5xx Resend Loop), ISSUE-007 (Timezone Bug), ISSUE-008 (Multi-TF Timestamp) |
| MEDIUM | 3 | ISSUE-002 (Row Validation), ISSUE-003 (Config Wiring), ISSUE-005 (Legacy Seams) |

**Risks Imported (8 total)**:
| Priority | Count | Key Items |
|:---------|:------|:----------|
| HIGH | 3 | RISK-001 (Unauthenticated Webhook - ACCEPTED), RISK-002 (Timezone Ambiguity), RISK-005 (At-Least-Once Delivery) |
| MEDIUM | 5 | RISK-003 (Override Storage), RISK-004 (VWAP tf Dependency), RISK-006 (3s Timeout), RISK-007 (Message Size), RISK-008 (Repainting) |

**HIGH Priority Resolution Strategy**:
- **ISSUE-001**: Document canonical 20-column in finalized IF-001 ✅ DONE
- **ISSUE-006**: Add IG-015 guidance for 4xx responses ✅ DONE; implement in T801A1
- **ISSUE-007/008 + RISK-002**: Document as known limitation; log for T801A2 fix
- **ISSUE-004**: Log for T801A1 dedup key fix `(symbol, time, tf)`
- **RISK-001**: ACCEPTED per QG-008 (MVP Simplicity); monitor during sandbox
- **RISK-005**: Add IG-015 idempotent processing guidance ✅ DONE; implement in T801A1

**ASSUM-004 Elevation Assessment**:
- **Question**: Should ASSUM-004 be elevated to CON given TradingView constraints?
- **Decision**: Maintain as ASSUM per T102-STD-005 semantics
- **Rationale**: TradingView constraints are environmental facts we cannot negotiate; ASSUMPTION is whether constraints are sufficient for our use case (validatable)
- **Action**: Updated ASSUM-004 with explicit constraint documentation + validation criteria + fallback strategy

**Key Outcomes**:
1. **All Partial E-RIDs Finalized**: IF-001, IG-014 now confirmed with complete specifications
2. **All Partial E-ADRs Completed**: ADR-001, ADR-004 now include full pipeline mapping and context scope
3. **16 Issues/Risks Imported**: Complete register with priority-based resolution strategy
4. **No New E-RIDs Required**: Research findings integrate into existing inventory
5. **Phase 1 Proposal Ready**: All blocking items resolved; ready for Activity 1.3.2 (Cross-Category Analysis) and 1.3.4 (Final Preparation)

**Ownership Confirmed**:
- Accountability: Client
- Responsibilities: LLM_Consultant (Epic T801A)

---
