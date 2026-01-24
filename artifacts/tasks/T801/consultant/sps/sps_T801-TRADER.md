---
artifact_type: 'SPS'
initiative_id: 'T801'
initiative_code: 'TRADER'
version: '1.0.1'
date: '2026-01-10'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# SYNTHESIZED PROBLEM STATEMENT (SPS): TRADER — T801

## I. EXECUTIVE SUMMARY
<!-- One paragraph describing the core problem, the desired outcome, and the recommended direction. Avoid details; link to sections below. -->

## II. TABLE OF CONTENTS
<!-- Optional for shorter docs. Tools may auto-generate. -->

## III. CORE CONTENT

### A. Problem Definition

#### 1. The Problem
<!-- Define the user/business problem in plain terms. Include who is affected and the current pain. -->

#### 2. The Desired Outcome
<!-- State measurable, verifiable outcomes. Prefer objective targets over activities. -->

#### 3. Business Case
<!-- Why this matters now: impact, urgency, constraints at a high level. -->

### B. Initiative Considerations
<!-- Governance and cross-cutting concerns applicable to all options. Keep bullets short and testable. -->

#### 1. Organization & Responsibilities

**Role Definitions**
| Actor | Role Title(s) | Decision Rights | Primary Responsibilities | Scope Notes |
| :--- | :--- | :--- | :--- | :--- |
| `Client` | Decision Owner | Approves baselines and cutover | Sets priorities; resolves scope conflicts; provides acceptance decisions | Initiative-wide |
| `LLM_Consultant` | Technical Consultant, Project Manager, Product Lead | Proposes baselines/requests; no final approval authority | Leads governance, requirements definition, and high-level project management; coordinates contributors; maintains SSOT coherence | Initiative/Epic/Feature (by assignment) |
| `LLM_Planner` | Planner | Authors implementation plans; no approval authority | Produces feature-level implementation plans and updates plan artifacts | Feature scope |
| `LLM_Researcher` | Research Analyst | No approval authority | Produces research, options, and trade-offs to support decisions | Initiative-wide |
| `LLM_Developer` | Technical Lead, Lead Engineer | No baseline approval authority; advises go/no-go | Implements changes; produces validation evidence; advises feasibility and architecture | Feature delivery |

**Governance RACI**
| Governance Activity | R (Responsible) | A (Accountable) | C (Consulted) | I (Informed) |
| :--- | :--- | :--- | :--- | :--- |
| Approve Initiative baseline | `LLM_Consultant` | `Client` | `LLM_Planner`, `LLM_Developer`, `LLM_Researcher` | — |
| Approve Epic baseline | `LLM_Consultant` | `Client` | `LLM_Planner`, `LLM_Developer`, `LLM_Researcher` | — |
| Approve Feature baseline | `LLM_Consultant` | `Client` | `LLM_Planner`, `LLM_Developer`, `LLM_Researcher` | — |
| Approve Feature implementation plan | `LLM_Planner` | `Client` | `LLM_Consultant`, `LLM_Developer` | `LLM_Researcher` |
| Approve cutover | `LLM_Developer` | `Client` | `LLM_Consultant`, `LLM_Planner` | `LLM_Researcher` |

#### 2. Project Assumptions
<!-- Unverified beliefs shaping scope/approach. Keep each assumption atomic and testable. -->

#### 3. Project Constraints
<!-- Non-negotiable boundaries (compliance, timebox, architecture, tooling). Use SHALL language where applicable. -->

#### 4. Success Criteria & Quality Goals
<!-- Verifiable acceptance criteria. Aim for binary pass/fail checks and clear owners. -->

#### 5. Dependencies
<!-- External prerequisites, upstream inputs, or capacity dependencies. Include ownership and availability windows. -->

#### 6. Interfaces
<!-- Roles and process touchpoints (e.g., Client review, Planner handoff). Define cadence and SLAs. -->

#### 7. Implementation Guidance
<!-- Technical/operational guidance for downstream teams. Keep normative (“SHOULD/SHALL”) where helpful. -->

#### 8. Research & Notes
**Research**

| Research ID | Title | Summary | Linked To | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T801-RES-001` | **Indicator Design Standards** | Timeframe applicability matrix, volume indicators (OBV/CVD), confidence system design, cross-topic integration for PineScript and backend processing | `T801`, `T801A` | [brief](../../research/brief/brief_T801-RES-001_indicator-design-standards.md) | [report](../../research/report/report_T801-RES-001_indicator-design-standards.md) |

**Notes**

#### 9. Governance Decisions
<!-- Record major decisions with context, decision, consequences, and references. Keep entries short; link out if needed. -->

#### 10. Issues & Risks
<!-- Track open issues/risks with status/priority. Prefer a small table. Keep IDs stable. -->

<!-- NOTES
- Keep this document concise; push deep detail to appendices or linked artifacts.
- Maintain end-to-end traceability: every decision should map to criteria, constraints, and downstream handoff.
- Update the frontmatter on each meaningful change (version, date, status).
-->

### C. Epics & Breakdown

#### 0. Initiative WBS Map
<!-- PURPOSE: High-level structural index only; keep synchronized with sections below. -->

| Level | PM Type | ID | Name |
| :--- | :--- | :--- | :--- |
| 1 | Initiative | T801 | TRADER |
| 2 | Epic | T801A | TTI |

---

#### 1. `T801A` Epic: `TTI` — Timeframe Trend Identification
<!-- PURPOSE: Epic dossier skeleton. Inherit global rules from Section III-B; add epic-specific scope, goals, and controls. -->

```yaml
epic_id: 'T801A'
epic_code: 'TTI'
epic_title: 'Timeframe Trend Identification'
epic_type: 'new'              # new | existing | general
epic_status: 'review'          # draft | review | approved | deprecated
epic_owner: 'LLM_Consultant'  # Role or named owner
```

##### i. Purpose

This Epic establishes a deterministic foundation for Timeframe Trend Identification (TTI) protocol from `LLM_Trader` so outputs are repeatable, timely, and suitable as stable input into higher-level trading workflows.

- Reduce variability by standardizing repeatable classification into a deterministic layer.
- Preserve discretionary interpretation via an operator-facing override/annotation path.
- Improve timeliness by reducing latency for routine classifications.

##### ii. Scope

**In Scope**:
  - Deterministic trend classification outputs per supported timeframe.
  - A structured output artifact suitable for both machine parsing and human review.
  - A parallel/playground delivery approach that preserves operational continuity.
**Out of Scope**:
  - Full automation of downstream consumption and end-to-end orchestration.
  - Production cutover without explicit decision-owner approval.
  - Advanced semantic pattern labeling beyond minimal deterministic signals.
  - Changes to other trading protocols outside the TTI domain.

##### iii. Inherited Considerations

<!-- - This Epic inherits initiative-level requirements `III.B` and should reference those items by ID when populated. -->

##### iv. Governance & Roadmap

<!-- Milestone-level oversight. Detailed planning lives in plan artifacts / external PM tools. -->

**Scope & Ownership**
- Gate Approver / Decision Owner (A): `Client`
- Governance / Requirements / PM Lead (R): `LLM_Consultant` (Project Manager, Product Lead; assigned to this Epic scope)
- Planning support (feature-level plans): `LLM_Planner` (Planner)
- Support: `LLM_Researcher`, `LLM_Developer`
- Org baseline (RACI): see `III.B.1 (Organization & Responsibilities)`

**Phase & Gates**
| Phase | Title | Intent | Key Exit Milestone | Duration Band | Gate Approver (A) | Phase Lead (R) | Plan Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | **EPIC DOSSIER FOUNDATION** | Make the epic dossier structurally correct and token-lean | `T801A` dossier clean; Feature list present; no premature E-RIDs | 1–2 sessions | `Client` | `LLM_Consultant` | `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` |
| 1 | **EPIC REQUIREMENTS & DECISIONS** | Develop Epic Requirements + governance decisions, then implement into SSOT after approval | Phase 1 proposal approved by `Client`; epic baseline established for Requests | 2–4 sessions | `Client` | `LLM_Consultant` | `prompt/artifacts/tasks/T801/consultant/workspace/plan/plan_T801A_phase0-1.md` |
| 2 | **FEATURE SPECIFICATION & AUTHORING** | Author Feature Request artifacts for all registered features | Feature Requests approved; implementation unblocked | — | `Client` | `LLM_Consultant` | — (Phase 2 plan) |
| 3 | **SANDBOX BUILD & VALIDATION** | Implement in isolated environment and validate | Sandbox evidence meets acceptance signals; no production disruption | — | `Client` | `LLM_Consultant` | — (Phase 3 plan) |
| 4 | **ACCEPTANCE & CUTOVER** | Final acceptance and explicit cutover decision | Cutover approved by `Client` with rollback controls confirmed | — | `Client` | `LLM_Consultant` | — (Phase 4 plan) |

**References**
- External PM tracking (if used): ticktick (— link)
- Research: `T801-RES-001 (Indicator Design Standards)`, `T801A-RES-001 (Backend TTI Architecture)`

##### v. Feature Register
<!-- PURPOSE: The official list of work for this Epic. Each Feature is fully specified in its own Request artifact (the WBS dictionary). -->
| ID | Code | Title | Purpose | Feature Lead (R) | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A1` | `BACKEND` | Backend TTI Engine | Deterministic classification + scoring + structured output generation (includes isolated validation environment) | `LLM_Consultant` | `proposed` | — |
| `T801A2` | `PINE` | PineScript Enhancement | Improve upstream exported inputs needed for deterministic classification | `LLM_Consultant` | `proposed` | — |
| `T801A3` | `LLM_TRADER` | LLM_Trader System Prompt | Update system prompt to consume TTI output for trading analysis operations | `LLM_Consultant` | `proposed` | — |

##### vi. Epic Requirements

* **Assumptions**

  **ASSUM Validation Lifecycle Summary**

  | ID | Title | Status | Validation Method | Timing | Owner | If Invalidated | CON Cross-Ref |
  |:---|:------|:-------|:------------------|:-------|:------|:--------------|:--------------|
  | `T801A-ASSUM-001` | Scoring Feasibility | `Pending` | Playground validation | Feature T801A1 | Client | Escalate: revise scoring approach | — |
  | `T801A-ASSUM-002` | PA Detection Feasibility | `Pending` | Manual trader review | Feature T801A1 | Client | Fallback: simplify/remove PA scoring | — |
  | `T801A-ASSUM-003` | Volume Integration Value | `Pending` | Comparative analysis | Feature T801A1 | Client | Fallback: omit OBV signal | — |
  | `T801A-ASSUM-004` | External Platform Sufficiency | `Pending` | Operational monitoring | Feature T801A2 | Client | Mitigate: reduce scope; escalate platform limits | — |
  | `T801A-ASSUM-005` | Operational Acceptance | `Pending` | Client evaluation | Feature T801A3 | Client | Escalate: revisit workflow/integration approach | `T801A-CON-003` |
  | `T801A-ASSUM-006` | LLM Performance Stability | `Pending` | Performance testing | Feature T801A3 | Client | Mitigate: reduce artifact size/prompt load | — |

  * **T801A-ASSUM-001 (Numeric Scoring Feasibility)** — We assume a deterministic -2..+2 numeric scoring system can replace the current qualitative TTI output (BULLISH/NEUTRAL/BEARISH variations) while achieving acceptable accuracy for trading decisions. Validation: Playground validation with historical data demonstrating scoring system produces consistent, interpretable trend classifications. Validation timing: Feature `T801A1` development.

  * **T801A-ASSUM-002 (PA Detection Feasibility)** — We assume algorithmic price action detection (swing-point algorithm or equivalent simpler approach) can reliably identify HH/HL vs LH/LL patterns for MVP trend classification. Qualitative language intentional at Epic level; quantitative thresholds defined at Feature level. Note: Feature-level research may evaluate simpler alternatives if swing-point proves overly complex. Validation: Manual trader review of sample classifications during playground testing. Validation timing: Feature `T801A1` development.

  * **T801A-ASSUM-003 (Volume Integration Value)** — We assume integrating OBV-based volume confirmation into TTI scoring will improve trend identification accuracy without introducing unacceptable complexity. OBV is a new addition to TTI protocol with significant uncertainty and can introduce risk. Fallback: If validation shows negative or neutral value-add, OBV integration is deferred or removed entirely from MVP. Validation: Comparative analysis of scoring accuracy with/without OBV during `T801A1` playground testing; clear fallback to proceed without volume signal. Validation timing: Feature `T801A1` implementation.

  * **T801A-ASSUM-004 (External Platform Sufficiency)** — We assume the TradingView platform and its webhook infrastructure provide sufficient reliability, rate limits, and payload capacity for consistent TTI artifact generation. Operational constraints detailed in `T801A-RES-002`. TradingView is currently the sole external data dependency per `T801A-IG-012`. Validation: Operational monitoring during sandbox development. Validation timing: Continuous during Feature `T801A2` development.

  * **T801A-ASSUM-005 (Workflow Acceptance)** — We assume the trader (Client) will functionally and experientially accept the manual artifact handoff workflow permitted by `T801A-CON-003`. This includes: 
    (1) functional acceptance — trader can technically perform the workflow; 
    (2) experiential acceptance — workflow does not significantly increase cognitive load or introduce unacceptable delays. Extends `T801A-CON-003` by including override acceptance (manual file editing before LLM_Trader handoff) as part of workflow acceptance validation per `T801A-QG-003` scope simplification. Validation: Client evaluation during playground testing. Validation timing: Feature `T801A3` integration testing.

  * **T801A-ASSUM-006 (LLM Performance Stability)** — We assume adding TTI JSON artifacts to trading session context (within 100k token target budget) will not significantly degrade LLM (GEMINI-PRO-3) response quality or latency. The LLM has 1M+ token context capacity, so fit is not a concern; performance impact is the key assumption. Validation: Performance testing with TTI artifacts added to representative trading prompts. Validation timing: Feature `T801A3` integration testing.

* **Constraints**

  * **T801A-CON-001 (Backward Compatibility)** — All Epic `T801A` development SHALL occur in an isolated sandbox environment separate from production systems. Existing tv_ingest backend and LLM_Trader prompt SHALL remain fully operational and unmodified during development. Production cutover (integration of sandbox work into main system) requires explicit Client approval as a hard gate. No partial integration is permitted; changes deploy as a complete unit after extensive testing and approval.

  * **T801A-CON-002 (Operational Continuity)** — Day-to-day trading operations MUST NOT be disrupted by Epic `T801A` development activities. Scope of "trading operations" includes the entire trading analysis ecosystem: LLM_Trader prompt execution, tv_ingest webhook processing, analytics dashboards, and position management workflows. Any development-related outage or degradation to these components is a constraint violation requiring immediate remediation.

  * **T801A-CON-003 (Manual Workflow Acceptance)** — MVP explicitly permits manual artifact handoff between the backend TTI output and LLM_Trader consumption. Automated delivery mechanisms (file watching, triggers, API integration) are explicitly deferred to post-MVP. Per `T801A-QG-003`, the manual workflow is explicitly leveraged — override is achieved through file editing during manual handoff, not backend configuration.

  * **T801A-CON-004 (Complexity Management)** — MVP explicitly excludes automated divergence detection. RSI divergence (regular and hidden) and MACD divergence are deferred to post-MVP development. Rationale per research (`T801A-RES-001` §V): 
    (1) medium-low feasibility — divergence detection requires swing point detection on both price and indicator values simultaneously; 
    (2) tuning burden — divergence thresholds require extensive calibration to avoid false positives; 
    (3) complexity management — scoring system validation must be stable before adding divergence signals. 
    MA crossovers (50/200, optionally 20/50) remain in scope as an explicit exception.

* **Quality Goals**

  * **T801A-QG-001 (Deterministic Consistency & Interpretability)** — Backend TTI generation SHALL produce identical output for identical input data across multiple runs. Scoring algorithms SHALL be deterministic (no randomness, no LLM variance). **Additionally**, scoring calculations SHALL follow a transparent, documented calculation framework that produces interpretable (not black-box) results — the trader MUST be able to understand why a score was assigned. Results SHALL be reproducible across system updates given the same input data and configuration version. Supports `T801A-ASSUM-001` validation; calculation framework developed in Feature T801A1.

  * **T801A-QG-002 (Signal Reliability)** — Extreme trend scores (+2/-2) SHALL achieve ≥80% precision in backtesting. Overall classification accuracy SHALL exceed 70% threshold. False positive rate SHALL be ≤20% for extreme scores. Reference: `T801A-RES-001` §II (Validation Methodology). **Note**: These quantitative thresholds are research-derived starting points and are subject to calibration/optimization during Feature-level validation. Threshold modifications require documented rationale and Client approval. Validates `T801A-ASSUM-001`; supported by `T801A-IG-003`, `T801A-IG-004`, `T801A-IG-011`.

  * **T801A-QG-003 (Manual Override)** — TTI output format SHALL support human-readable manual editing for post-output override via manual workflow per `T801A-CON-003`. Backend does NOT implement override logic or validation — override is achieved through manual file editing by trader AFTER TTI output is produced, BEFORE handoff to LLM_Trader. Extends `T801A-CON-003`; supported by `T801A-ASSUM-005`; requires `T801A-IF-002` human-editable format; workflow guidance in `T801A-IG-013`.

  * **T801A-QG-004 (Rule Maintainability)** — Backend rule engine SHOULD use configuration-driven rules (JSON/YAML) for indicator thresholds, scoring weights, and classification logic. Hardcoded rules SHALL be minimized. Configuration changes SHALL NOT require code deployment; parameter adjustments achievable via config file modification. Supported by `T801A-IG-001`.

  * **T801A-QG-005 (Timeframe Correctness)** — TTI output SHALL only include indicators applicable to the analyzed timeframe per Initiative T801 timeframe applicability matrix (`T801-RES-001` §II). Irrelevant indicators (e.g., S_VWAP on 1D) SHALL NOT appear in output or contribute to scoring. Depends on `T801A-DEP-001`; supported by `T801A-IG-002`, `T801A-IG-007`.
    Reference: `T801-RES-001 (Indicator Design Standards)`

  * **T801A-QG-006 (Latency & Resource Efficiency)** — TTI artifact generation SHOULD complete within **<1 minute (ideal), ≤3 minutes (maximum)** from webhook receipt under normal load conditions. Resource consumption (memory, CPU) SHALL remain within acceptable ceilings to be determined at Feature level via benchmarking. **Load Profile**: Normal load defined as single trading pair webhook with data for multiple timeframes; extended load scenarios (multiple pairs, high-frequency webhooks) deferred to post-MVP. **Note**: Latency targets are guidance subject to Feature-level refinement based on deployed system characteristics. Supported by `T801A-IG-010` for context budget optimization.

  * **T801A-QG-007 (Context Sufficiency)** — TTI output artifact SHALL provide sufficient market context to **replace both** the inline TTI protocol execution AND the raw master.csv data currently consumed by LLM_Trader. The goal is a single JSON artifact that enables LLM_Trader to perform trading analysis without requiring additional data files or inline calculations. Impacts `T801A-IF-002` (required fields); impacts `T801A-IF-003` (sole input artifact); impacts `T801A-DEP-004` (TTI output replaces master.csv for LLM_Trader); supported by `T801A-IG-014`.

  * **T801A-QG-008 (MVP Simplicity)** — Feature-level solutions for Epic T801A SHALL prioritize simplicity, low complexity, and speed of implementation to achieve baseline MVP functionality. Assessment criteria for Feature development SHOULD weight these factors highly against alternative complex approaches. Complex solutions requiring extensive calibration, tuning, or infrastructure changes SHOULD be deferred to post-MVP unless essential for core TTI functionality. Supported by `T801A-IG-012`; informs all Feature-level development prioritization.

* **Dependencies**

  * **T801A-DEP-001 (Timeframe-Correct Input)** — Backend TTI scoring engine MUST receive timeframe-correct indicator dataset where only timeframe-appropriate indicators are included per the Initiative `T801` timeframe applicability matrix. The enforcement mechanism (PineScript filtering OR backend filtering) is an implementation choice to be determined during Feature-level design; the dependency is on the correctness of the final dataset, not the specific enforcement location. Development occurs within sandbox per `T801A-CON-001`; platform reliability per `T801A-ASSUM-004`.

  * **T801A-DEP-002 (tv_ingest Backend)** — Epic `T801A` requires the existing `tv_ingest` backend component's behavioral contract (webhook ingestion → data processing → CSV storage). Backend integration MUST maintain this behavioral contract stability; internal refactors are acceptable as long as external behavior (webhook acceptance, data storage outputs) remains stable. Development MUST occur in isolated sandbox environment per operational continuity constraint.

  * **T801A-DEP-003 (LLM_Trader Consumption)** — Epic T801A requires modification of the LLM_Trader system prompt (`prompt/roles/VPA/main_v2.1.md`) to consume the generated TTI JSON artifact as authoritative input instead of executing the TTI protocol inline. The prompt modification includes:
    (1) removing inline TTI execution logic,
    (2) adding JSON artifact parsing and interpretation,
    (3) surfacing manual override flags for trader visibility.
  Fallback to inline TTI format is acceptable during transition if artifact is missing or stale. Manual workflow per `T801A-CON-003`; workflow acceptance per `T801A-ASSUM-005`.

  * **T801A-DEP-004 (Expanded Data Structure)** — Epic `T801A` requires an expanded `master.csv` data structure supporting multi-candle historical data for accurate price action, volume calculations and indicator values such as moving averages as input for TTI calculation. Current structure limitations and historical depth specifications detailed in `T801A-RES-002`. Per `T801A-QG-007`, the TTI output artifact replaces the need to deliver raw master.csv to LLM_Trader — the JSON artifact provides sufficient market context. No file consolidation required; TTI JSON is the sole LLM_Trader input artifact. `T801A-IG-016`, `T801A-RES-002` Topic 5

* **Interfaces**

  * **T801A-IF-001 (Webhook Input Contract)** — Webhook payload interface from TradingView PineScript exporter (`nmaq_exporter.pine`) to tv_ingest backend.

    **Contract Type**: Base (20-column) — canonical per `T801A-RES-002`.

    **Delimiter Rules**:
    - Rows separated by newline `\n`
    - Columns separated by semicolon `;`
    - No header row; no explicit quoting/escaping

    **Field Schema (20 columns)**:
    | # | Field | Type | Example |
    |---:|:------|:-----|:--------|
    | 1 | `symbol` | string | `BINANCE:BTCUSDT` |
    | 2 | `time` | datetime string | `2025-12-23 22:00:00` |
    | 3-6 | `open,high,low,close` | float | `88620.79` |
    | 7 | `volume` | float | `12804.02886` |
    | 8-9 | `vol_ma20,vol_ma30` | float | `15679.57` |
    | 10-13 | `ema9,ema21,ema50,ema200` | float | `88184.41` |
    | 14 | `sma200` | float | `107773.37` |
    | 15-16 | `rsi,rsi_ma14` | float | `43.3861` |
    | 17-19 | `vwap_session,vwap_week,vwap_month` | float | `87753.21` |
    | 20 | `tf` | string code | `60`, `D`, `W` |

    **Multi-Timeframe Semantics**:
    - Chart timeframe: up to 5 rows per alert (configurable via `exportRows`)
    - Additional timeframes: 1 row each (latest only)

    **TradingView Platform Constraints (Environmental)**:
    - Port restrictions: Only 80/443 accepted
    - Processing timeout: ~3 seconds before TradingView cancels
    - Resend on 5xx: Up to 3 retries (max 4 deliveries per trigger)
    - Message body cap: 40,960 characters
    - Timestamp timezone: `str.format()` always UTC+0

    **Schema Versioning**: Deferred to Feature T801A1/T801A2 coordination. Current contract unversioned.

    Supports `T801A-DEP-001`, `T801A-IG-007`, `T801A-IG-015`, `T801A-RES-002`.

  * **T801A-IF-002 (Backend Output Contract)** — TTI output artifact interface from backend TTI engine to downstream consumers (manual handoff, LLM_Trader). Artifact SHALL be JSON with versioned, human-readable schema per `T801A-QG-003` and `T801A-QG-007`.

    **REQUIRED Fields (MVP)** — derived from current TTI protocol + research findings:
    - `schema_version` — artifact schema version (semver format)
    - `generator_version` — TTI engine version
    - `asset` — trading pair identifier
    - `timeframe` — analyzed timeframe
    - `trend_score` — numeric -2 to +2 per `T801A-GDR-002`
    - `trend_label` — text label (Strong Uptrend/Uptrend/Neutral/Downtrend/Strong Downtrend)
    - `signals` object containing:
      - `htf_reference` — higher timeframe assessment reference (e.g., "4H: BEARISH")
      - `price_action` — PA assessment (HH/HL, LH/LL patterns, breakout signals, caution flags)
      - `vwap` — VWAP position assessments (S_VWAP, D_VWAP, W_VWAP, M_VWAP values + position relative to price)
      - `rsi` — RSI + RSI_MA values and assessment
      - `moving_averages` — MA values (EMA_9, EMA_21, EMA_50, EMA_200, SMA_200) and position assessment
      - `volume` — OBV trend direction and confirmation assessment per `T801A-IG-003`
    - `overall_assessment` — final trend assessment with caution indicators (e.g., "BULLISH*")

    **Feature-Level Expansion (Deferred)**: Each major signal field MAY include additional indicator calculations (e.g., MA crossover signals, slope calculations, distance from price) as explored in Feature T801A1. These additional fields contribute to both market context and final TTI output assessment.
    - `manual_override` — boolean flag (sufficient for MVP per dialogue)
    - `as_of` — generation timestamp

    **Context Scope (Option B)**: TTI scoring fields + minimal market context. "Minimal market context" definition to be determined by `T801A-RES-002` research per `T801A-IG-014`. Initial scope includes current price, VWAP levels, and key indicator values as reference points.

    **OPTIONAL Fields (Future Extension)**:
    - `override_note`, `override_by`, `override_timestamp` — full audit trail
    - Extended market context fields per `T801A-QG-007` Option C exploration

    Supports `T801A-QG-003`, `T801A-QG-007`, `T801A-IG-013`, `T801A-IG-014`, `T801A-IG-015`, `T801A-RES-002`.

  * **T801A-IF-003 (LLM_Trader Consumption Interface)** — Interface contract for LLM_Trader prompt consumption of TTI JSON artifact. LLM_Trader prompt (`prompt/roles/VPA/main_v2.1.md`) SHALL consume `T801A-IF-002` JSON artifact as **sole authoritative input** per `T801A-QG-007`.

    **Consumption Contract**:
    - Artifact **replaces both**: (1) inline TTI protocol execution; (2) raw master.csv data delivery
    - LLM_Trader SHALL parse JSON artifact and interpret trend signals for trading analysis
    - **Override Handling**: Silent (Option A per dialogue) — process TTI as-is; trader responsible for noting override context if relevant
    - **Fallback**: Per `T801A-DEP-003`, fallback to inline TTI format acceptable during transition if artifact missing/stale

    **Prompt Modification Requirements**:
    - Remove inline TTI execution logic
    - Add JSON artifact parsing and interpretation
    - Reference `T801A-IF-002` schema for field consumption

    Supports `T801A-DEP-003`, `T801A-QG-007`; workflow guidance in `T801A-IG-013`, `T801A-IG-014`.

* **Implementation Guidance**

  * **T801A-IG-001 (Configuration-Driven Rules)** — Backend rule engine SHOULD use configuration files (JSON/YAML) to define indicator thresholds, timeframe-specific weights, scoring parameters, and classification logic. Hardcoded rules SHALL be minimized. Configuration changes SHALL NOT require code deployment; parameter adjustments achievable via config file modification. Supports `T801A-QG-004`.

  * **T801A-IG-002 (Timeframe Filtering)** — Backend SHALL validate incoming indicator set against timeframe applicability matrix. Irrelevant indicators (e.g., S_VWAP on 1D timeframe) SHALL be ignored in scoring calculation. Validation occurs after webhook ingestion, before scoring engine execution. Supports `T801A-QG-005`; references `T801A-RES-001` §II.

  * **T801A-IG-003 (Volume Confirmation)** — Backend SHOULD include volume confirmation methodology in trend scoring. Research baseline: OBV (On-Balance Volume) trend direction as confirmation signal — rising OBV + uptrend = confidence boost; falling OBV + uptrend = divergence flag. Divergence flags are optional for MVP. Alternative volume methodologies MAY be explored at Feature level. Supports `T801A-QG-002`; references `T801A-RES-001` §III (OBV recommendation).

  * **T801A-IG-004 (Scoring Mechanism Guidance)** — Backend SHOULD implement transparent scoring calculation where: (1) individual indicators contribute weighted scores per documented methodology; (2) composite score aggregation follows documented formula; (3) weights are configuration-driven per `T801A-IG-001`; (4) calibration methodology documented for ongoing optimization per `T801A-IG-011`. Research baseline: Weighted voting ensemble approach per `T801A-RES-001` §II. Alternative scoring methodologies MAY be explored at Feature level per `T801A-QG-008`. Supports `T801A-QG-001`, `T801A-QG-002`.

  * **T801A-IG-005 (PA Detection Approach)** — Backend SHOULD implement deterministic price action pattern recognition for HH/HL (Higher High/Higher Low) vs LH/LL (Lower High/Lower Low) classification. Research baseline: Swing-point algorithm with configurable confirmation bars per `T801A-RES-001` §IV. Alternative approaches (simpler or more robust) MAY be explored at Feature level per `T801A-QG-008`. Complex patterns (head-and-shoulders, triangles, wedges) are explicitly deferred to post-MVP. Supports `T801A-ASSUM-002`.

  * **T801A-IG-006 (MA Crossover Configuration)** — MA crossover detection SHOULD be configurable per `T801A-IG-001`. Research baseline: 50/200 crossover (Golden Cross/Death Cross) for longer-term trend confirmation per `T801A-RES-001` §V. Additional configurations (20/50 crossover, distance-to-price, slope, velocity calculations) MAY be explored at Feature level. Crossover events SHALL include event date in artifact per `T801A-IF-002`. References `T801A-RES-001` §V.

  * **T801A-IG-007 (Initiative Matrix Reference)** — Backend filtering logic SHALL reference `T801A-RES-001` timeframe applicability matrix as authoritative source for indicator inclusion/exclusion rules. Matrix defines relevance (High/Medium/Low) per indicator × timeframe combination. "Low" relevance indicators SHOULD be excluded from scoring; "High" relevance indicators SHOULD have primary weight. Supports `T801A-DEP-001`, `T801A-IG-002`.

  * **T801A-IG-008 (Research Alignment)** — Implementation SHOULD align with research outcomes from `T801-RES-001` and `T801A-RES-001`. Deviations from research recommendations require: 
  (1) documented rationale explaining why deviation is necessary; 
  (2) explicit Client approval before implementation. 
  Research recommendations serve as design choice baselines, not absolute prescriptions.
    Reference: `T801-RES-001 (Indicator Design Standards)`

  * **T801A-IG-009 (Integration Scope)** — Epic T801A SHALL integrate as extension to existing `tv_ingest` backend component per `T801A-DEP-002`. Fundamental architecture changes (new service patterns, database additions, external API integrations) SHOULD be escalated as separate Initiative work requiring Client decision. Internal refactors are acceptable if external behavioral contract remains stable. CON dialogue reclassification; supports `T801A-CON-001`.

  * **T801A-IG-010 (Artifact Size Guidance)** — JSON artifact SHOULD be optimized for LLM context budget. Exact size thresholds to be determined via Feature-level research based on: (1) typical artifact field count and nesting depth; (2) LLM token consumption analysis; (3) context window utilization patterns. Initial guidance: prefer lean schema with essential fields; defer extended context to post-MVP. Supports `T801A-ASSUM-006`.

  * **T801A-IG-011 (Validation Guidance)** — Scoring system SHOULD demonstrate acceptable accuracy via playground validation before production deployment. Quantitative thresholds (≥70% accuracy, ≥80% extreme-score precision) defined at Feature level per `T801A-QG-002`. Validation methodology: historical data simulation with stratified regime sampling per `T801A-RES-001` §II. Supports `T801A-ASSUM-001`, `T801A-CON-001`.

  * **T801A-IG-012 (Dependency Minimization)** — MVP SHOULD avoid introducing new external service dependencies beyond established TradingView integration. New dependencies (cloud services, databases, external APIs) require: 
  (1) documented necessity rationale; 
  (2) Client approval; 
  (3) operational continuity assessment per `T801A-CON-002`. TradingView webhook remains sole external data dependency. 
  Supports `T801A-QG-008`.

  * **T801A-IG-013 (Override Workflow)** — Manual file editing workflow for post-output override per `T801A-CON-003` and `T801A-ASSUM-005`. Backend does NOT implement override logic or validation — override is achieved through manual JSON file editing by trader AFTER TTI output is produced, BEFORE handoff to LLM_Trader. Workflow: (1) backend produces TTI JSON; (2) trader edits JSON if override needed (sets `manual_override: true`); (3) trader provides edited JSON to LLM_Trader. Supports `T801A-QG-003`.

  * **T801A-IG-014 (Context Content)** — Guidance on "minimal market context" content for TTI JSON artifact per `T801A-QG-007` Option B selection.

    **Minimal Market Context Specification** (per T801A-RES-002):

    **Required Structure**:
    - `schema_version`: Context schema version (e.g., `tv_ingest_context/0.1.0`)
    - `symbol`: Trading pair identifier (e.g., `BINANCE:BTCUSDT`)
    - `as_of`: Generation timestamp (datetime string)
    - `time_source`: Timezone/format metadata for timestamp interpretation
    - `timeframes`: Object containing per-timeframe context data

    **Per-Timeframe Context Fields**:
    - `tf_code`: Raw timeframe code (e.g., `60`, `D`, `W`)
    - `close`: Current close price
    - `ema`: Object with EMA values (9, 21, 50, 200)
    - `sma200`: SMA 200 value (where applicable per timeframe matrix)
    - `rsi`: RSI value
    - `rsi_ma14`: RSI MA14 value
    - `vwap`: Object with applicable VWAP values (session, week, month per timeframe matrix)

    **Optional Chart Timeframe History**:
    - `chart_tf_bars`: Array of recent bars (up to 5) for chart timeframe only
    - Each bar: `time`, `open`, `high`, `low`, `close`, `volume`

    **Size Guidance**:
    - Target: ~1500-2000 characters (~375-500 tokens)
    - Satisfies `T801A-QG-007` without exceeding `T801A-IG-010` context budget

    **Exclusions from Minimal Context**:
    - Delta columns (not emitted by current Pine)
    - VWAP values masked by backend filtering (include only applicable per matrix)
    - Historical bars for non-chart timeframes

  * **T801A-IG-015 (Data Validation)** — Backend SHALL implement validation at two stages:

    **Input Validation**: Validate webhook payload against `T801A-IF-001`. Handle malformed/missing data per Option D (best-effort processing + error flags): (1) attempt calculation with available data; (2) flag missing/invalid fields in output; (3) continue processing rather than rejecting entirely.

    **HTTP Response Code Guidance** (per `T801A-RES-002`): Return HTTP 4xx for client validation errors (column count mismatch, malformed data) to prevent TradingView resend loop. Avoid HTTP 5xx for validation failures — TradingView retries 5xx up to 3 times, creating duplicates.

    **Output Validation**: Validate TTI artifact against `T801A-IF-002` schema before delivery. Reject/flag artifacts that fail schema validation per `T801A-IF-002` "machine-validated" clause.

    Backend SHALL NOT crash on validation failures but produce error artifact or fallback output per `T801A-QG-008`. Supports `T801A-IF-001`, `T801A-IF-002`

    **Input Validation Behavior** (per `T801A-IF-001`):
    - Column count mismatch → validation error (return 4xx not 5xx)
    - Malformed/missing data → best-effort processing + error flags
    - Backend validates before scoring; does not validate row count

  * **T801A-IG-016 (Historical Input Format)** — Guidance on multi-candle historical data format for backend TTI engine per `T801A-DEP-004`.

    **Current-State Format** (per `T801A-RES-002`):
    - **Record shape**: Each row = one candle snapshot for one timeframe
    - **Grouping**: Group by `(symbol, tf)`; `time` is candle timestamp
    - **History depth**:
      - Chart timeframe: up to **5 bars** per alert (configurable via `exportRows`)
      - Other timeframes: **1 bar** per alert (latest only)
    - **Constraint**: No schema version tag or "snapshot id" for dedup

    **Calculation Feasibility**:
    | Calculation | Feasible? | Notes |
    |:------------|:----------|:------|
    | Trend scores | ✅ Yes | Pine provides current indicator values |
    | MA crossovers | ✅ Yes | Pine has long history |
    | Short momentum | ✅ Yes | 5 bars sufficient |
    | Complex PA (HH/HL series) | ⚠️ Limited | May require append mode |
    | RSI divergences | ⚠️ Limited | Deferred per `T801A-CON-004` |

    **Recommendation**:
    - For MVP: Accept 5-bar chart TF + 1-bar other TFs as sufficient for trend scoring
    - For enhanced PA detection: Enable append mode with `MAX_ROWS_PER_SYMBOL` limit
    - Feature T801A2 determines Pine export capabilities; Feature T801A1 consumes

    **Timestamp Caveat**: Timestamps may be formatted incorrectly or use chart TF time for all rows. Document as known limitation.

---

##### vii. Epic Research & Notes
<!-- PURPOSE: Provide background, drivers, and key research findings that inform this Epic's direction. -->

**Research**

| Research ID | Title | Summary | Linked To | Brief | Report |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A-RES-001` | **Backend TTI Architecture** | Numeric scoring system (-2 to +2), JSON file format with lean schema, swing-point PA detection, MA crossover inclusion (divergence deferred), validation methodology | `T801A` | [brief](../../research/brief/brief_T801A-RES-001_backend-tti-architecture.md) | [report](../../research/report/report_T801A-RES-001_backend-tti-architecture.md) |
| `T801A-RES-002` | **System Architecture Research** | Map current system pipeline (Code-as-Master), document I/O contracts (20-column base), define minimal market context, clarify historical format, and identify TradingView constraints. | `T801A` | [brief](../../research/brief/brief_T801A-RES-002_system-architecture-research.md) | [report](../../research/report/report_T801A-RES-002_system-architecture-research.md) |

**Notes**

* **T801A-NOTE-001 (LLM_Trader Consumption Adaptation)** — Future research (`T801A3-RES-001`) recommended to analyze VPA Type 1/2 trading-session prompts and specify how `T801A3` consumes the `T801A1` TTI JSON artifact.
* **T801A-NOTE-002 (TradingView Schema Evolution)** — Future research (`T801A2-RES-001`) recommended to assess semicolon-delimited vs JSON payload formats for TradingView alerts and propose safe schema evolution post-MVP.

##### viii. Epic Governance Decisions

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| `T801A-GDR-001` | Hybrid TTI Architecture | Proposed | Client | 2026-01-03 | — | #t801a-gdr-001-hybrid-tti-architecture |
| `T801A-GDR-002` | Numeric Scoring Foundation | Proposed | Client | 2026-01-03 | — | #t801a-gdr-002-numeric-scoring-foundation |
| `T801A-GDR-003` | Playground-First Mandate | Proposed | Client | 2026-01-03 | — | #t801a-gdr-003-playground-first-mandate |
| `T801A-GDR-004` | Backend File Format Standard | Proposed | Client | 2026-01-03 | — | #t801a-gdr-004-backend-file-format-standard |
| `T801A-GDR-005` | Initiative Standard Compliance | Proposed | Client | 2026-01-03 | — | #t801a-gdr-005-initiative-standard-compliance |
| `T801A-GDR-006` | Research Baseline Adoption | Proposed | Client | 2026-01-03 | — | #t801a-gdr-006-research-baseline-adoption |

* **T801A-GDR-001 (Hybrid TTI Architecture) {#t801a-gdr-001-hybrid-tti-architecture}**

  **Context.** Current LLM-based TTI protocol (inline execution within LLM_Trader prompt) produces unreliable, inconsistent trend classifications. Timeframe-specific indicator rules are not consistently applied; qualitative outputs (BEARISH/NEUTRAL/BULLISH variations) lack determinism for algorithmic processing. Per `T801-RES-001` and `T801A-RES-001`, a hybrid architecture separating deterministic calculation from interpretive analysis addresses reliability concerns while preserving LLM contextual insight.

  **Decision.** Adopt `T801A-ADR-001 (Hybrid Integration Pattern)`, establishing hybrid TTI architecture where: (1) backend deterministic engine produces numeric trend classification per timeframe; (2) LLM_Trader consumes structured TTI output for interpretive analysis and trading decisions. Backend calculations replace inline TTI protocol execution. Integration follows file-based handoff with manual workflow per `T801A-CON-003`. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Eliminates LLM variance and timeframe rule inconsistency via deterministic backend
  (+) Preserves LLM interpretive strengths for contextual analysis and trading judgment
  (+) Enables independent backend validation and testing per `T801A-CON-001`/`T801A-CON-003`
  (±) Requires coordinated development across T801A1 (Backend), T801A2 (PineScript), T801A3 (Integration)
  (-) Introduces integration complexity; manual handoff workflow per `T801A-CON-003`

  **References.** `T801A-DEP-002 (tv_ingest Backend)`, `T801A-DEP-003 (LLM_Trader Consumption)`, `T801A-CON-001 (Backward Compatibility)`, `T801A-CON-003 (Manual Workflow Acceptance)`, `T801A-IG-009 (Integration Scope)`, `T801-RES-001 (Indicator Design Standards)`, `T801A-RES-001 (Backend TTI Architecture)`

---

* **T801A-GDR-002 (Numeric Scoring Foundation) {#t801a-gdr-002-numeric-scoring-foundation}**

  **Context.** Existing TTI protocol outputs subjective text classifications (BEARISH, NEUTRAL, BULLISH with variations like "SLIGHTLY BEARISH"). These qualitative outputs are inconsistent across sessions and difficult to track quantitatively for validation. Per `T801A-RES-001` §II (Numeric Scoring System Design), numeric scoring provides deterministic, comparable, and validatable trend strength classification.

  **Decision.** Adopt `T801A-ADR-002 (Scoring Algorithm Specification)`, establishing -2 to +2 symmetric 5-point scale as the foundation for Epic T801A trend classification. Scale: +2 (Strong Uptrend), +1 (Uptrend), 0 (Neutral), -1 (Downtrend), -2 (Strong Downtrend). Scoring formula follows documented deterministic calculation per `T801A-ASSUM-001` validation methodology. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Deterministic, reproducible trend classifications enable validation and optimization
  (+) Numeric scale supports quantitative backtesting per `T801A-QG-002` (≥70% accuracy, ≥80% extreme-score precision)
  (+) Text labels preserved for human readability alongside numeric scores
  (±) Requires threshold calibration via playground validation per `T801A-IG-011`
  (-) Binary text classifications (BULLISH/BEARISH) converted to 5-point scale; may require trader adjustment period per `T801A-ASSUM-005`

  **References.** `T801A-ASSUM-001 (Numeric Scoring Feasibility)`, `T801A-QG-001 (Deterministic Consistency & Interpretability)`, `T801A-QG-002 (Signal Reliability)`, `T801A-IG-004 (Scoring Mechanism Guidance)`, `T801A-IG-011 (Validation Guidance)`, `T801A-RES-001 (Backend TTI Architecture)`

---

* **T801A-GDR-003 (Playground-First Mandate) {#t801a-gdr-003-playground-first-mandate}**

  **Context.** Daily trading operations depend on current system reliability (tv_ingest webhook processing, LLM_Trader prompt execution, position management). Per `T801A-CON-001`/`T801A-CON-002`, development activities MUST NOT disrupt operational continuity. Isolated playground environment enables parallel development, comprehensive validation, and controlled production cutover.

  **Decision.** Adopt `T801A-ADR-003 (Playground Deployment Architecture)`, mandating isolated playground for all Epic T801A development. Playground operates on dedicated feature branch (`feature/t801a-tti`) separate from `main`. Production cutover requires explicit Client approval per `T801A-CON-001` as hard gate. Playground validation demonstrates acceptable accuracy per `T801A-QG-002`/`T801A-IG-011` before production deployment. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Protects operational trading systems from development disruption per `T801A-CON-002`
  (+) Enables comprehensive validation with historical data before production deployment
  (+) Supports iterative calibration and testing without client approval for each change
  (±) Requires parallel maintenance of playground and production environments during development
  (-) Manual merge and cutover process; rollback more complex than feature flags

  **References.** `T801A-CON-001 (Backward Compatibility)`, `T801A-CON-002 (Operational Continuity)`, `T801A-QG-002 (Signal Reliability)`, `T801A-IG-011 (Validation Guidance)`

---

* **T801A-GDR-004 (Backend File Format Standard) {#t801a-gdr-004-backend-file-format-standard}**

  **Context.** TTI output artifact file format impacts LLM consumption reliability, manual override workflow usability, and long-term maintainability. Per `T801A-RES-001` §III (Backend TTI File Format), JSON provides optimal balance of schema rigidity, LLM ingestion reliability, and traceability compared to YAML or Markdown alternatives. Human-readable format required for manual override per `T801A-QG-003`.

  **Decision.** Adopt `T801A-ADR-004 (TTI File Schema)`, establishing JSON with lean, versioned schema as the Epic T801A file format standard. Schema includes: `schema_version`, `trend_score`, `trend_label`, `signals` object (PA, VWAP, RSI, MA, Volume/OBV, Overall Assessment), manual override fields, and timestamp. Format supports both machine validation (`T801A-IF-002`) and human editing (`T801A-QG-003`). Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Reliable LLM ingestion with explicit structure and schema validation per `T801A-IF-002`
  (+) Human-readable format supports manual override workflow per `T801A-QG-003`/`T801A-IG-013`
  (+) Versioning strategy enables backward compatibility and schema evolution
  (±) JSON more verbose than YAML; context budget optimization required per `T801A-IG-010`
  (-) Manual editing requires JSON syntax knowledge; validation catches errors per `T801A-IG-015`

  **References.** `T801A-IF-002 (Backend Output Contract)`, `T801A-QG-003 (Manual Override)`, `T801A-IG-010 (Artifact Size Guidance)`, `T801A-IG-013 (Override Workflow)`, `T801A-IG-015 (Data Validation)`, `T801A-RES-001 (Backend TTI Architecture)`

---

* **T801A-GDR-005 (Initiative Standard Compliance) {#t801a-gdr-005-initiative-standard-compliance}**

  **Context.** Epic T801A operates within Initiative T801 governance framework. Per `T801-RES-001` §V (Initiative Standards 1-6), Initiative Standards 1-6 ensure cross-epic consistency for timeframe filtering, volume indicators, confidence systems, indicator roles, performance evaluation, and integration prioritization. Epic implementations SHALL comply with Initiative standards unless variance explicitly approved per `T801A-IG-007`.

  **Decision.** Adopt `T801A-ADR-005 (Timeframe Applicability Enforcement)`, mandating Epic T801A SHALL comply with T801-RES-001 Initiative Standards 1-6. Backend filtering logic SHALL reference T801-RES-001 timeframe applicability matrix as authoritative source per `T801A-IG-007`. Deviations from Initiative standards require documented rationale and Client approval per `T801A-IG-008`. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Ensures cross-epic consistency for future Initiative T801 work (multi-pair support, enhanced indicators)
  (+) Leverages Initiative-level research investment for Epic implementations
  (+) Prevents technical debt from Epic-specific deviations
  (±) Initiative standards may constrain Epic-level optimization; variance workflow required for exceptions
  (-) Epic T801A blocked if Initiative standards change without Epic alignment assessment

  **References.** `T801A-DEP-001 (Timeframe-Correct Input)`, `T801A-QG-005 (Timeframe Correctness)`, `T801A-IG-007 (Initiative Matrix Reference)`, `T801A-IG-008 (Research Alignment)`, `T801A-RES-001 (Backend TTI Architecture)`

---

* **T801A-GDR-006 (Research Baseline Adoption) {#t801a-gdr-006-research-baseline-adoption}**

  **Context.** Research recommendations from `T801-RES-001` and `T801A-RES-001` vary in prescription level. Some are mandatory baselines requiring Epic-wide compliance (e.g., -2 to +2 scale, JSON format), while others are flexible patterns permitting Feature-level alternatives (e.g., swing-point PA detection). Without explicit classification per `T801A-QG-008`, Feature development may inconsistently apply research guidance.

  **Decision.** Adopt `T801A-ADR-006 (Research Baseline Specification)`, establishing explicit baseline/flexible classification for all research recommendations. Mandatory baselines (SHALL) define non-negotiable Epic architecture; flexible guidances (SHOULD/MAY) provide research-recommended starting points permitting Feature-level alternatives per `T801A-QG-008` (MVP Simplicity). Deviations from mandatory baselines require explicit Client approval; deviations from flexible guidances require documented rationale per `T801A-IG-008`. Client owns governance authority for Epic T801A.

  **Consequences.**
  (+) Clear baseline vs flexible classification guides Feature-level development decisions
  (+) Preserves research value while permitting MVP simplicity per `T801A-QG-008`
  (+) Explicit approval workflow for baseline deviations prevents technical debt
  (±) Feature developers must consult ADR-006 specification before selecting alternatives
  (-) Baseline classifications may over-constrain if research assumptions prove incorrect

  **References.** `T801A-QG-008 (MVP Simplicity)`, `T801A-IG-008 (Research Alignment)`, `T801-RES-001 (Indicator Design Standards)`, `T801A-RES-001 (Backend TTI Architecture)`

##### ix. Epic Issues & Risks

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A-ISSUE-001` | "19 vs 20 vs 44" Schema Confusion | Code comments/UI text reference 19 columns, but base schema is 20 columns and enhanced is 44. Causes developer confusion. | LLM_Consultant (Phase 1); LLM_Developer (T801A1) | `RESOLVED` | `HIGH` | 2026-01-05 | 2026-01-06 |
| `T801A-ISSUE-002` | Row-Count Validation Missing | `EXPECTED_ROWS_PER_ALERT` exists but not enforced in webhook processing. | LLM_Developer | `RESOLVED` | `MEDIUM` | 2026-01-05 | 2026-01-06 |
| `T801A-ISSUE-003` | Config Surface Not Wired | `/config` API toggles don't update running server; operator misunderstanding risk. | LLM_Developer | `DEFERRED` | `MEDIUM` | 2026-01-05 | 2026-01-06 |
| `T801A-ISSUE-004` | Global-Master Dedup Data Loss | Dedup uses `(time, tf)` only; can erase different symbols. | LLM_Developer | `RESOLVED` | `HIGH` | 2026-01-05 | 2026-01-06 |
| `T801A-ISSUE-005` | Legacy Seams in tv_ingest | Multiple code paths inconsistent; docs/tests reference deprecated structures. | LLM_Developer | `DEFERRED` | `MEDIUM` | 2026-01-05 | 2026-01-06 |
| `T801A-ISSUE-006` | 5xx Triggers TradingView Resend | Returns 500 for column-count mismatches; causes up to 4 deliveries creating duplicates. | LLM_Consultant (IG-015); LLM_Developer (T801A1) | `RESOLVED` | `HIGH` | 2026-01-05 | 2026-01-06 |
| `T801A-ISSUE-007` | Pine Timezone Formatting Incorrect | `str.format()` always formats in UTC+0; may produce wrong timestamps. | LLM_Developer | `DEFERRED` | `HIGH` | 2026-01-05 | 2026-01-06 |
| `T801A-ISSUE-008` | Multi-TF Timestamp Semantics Unclear | Exporter builds `timeStr` using chart TF time, not requested TF. | LLM_Developer | `DEFERRED` | `HIGH` | 2026-01-05 | 2026-01-06 |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A-RISK-001` | Unauthenticated Public Webhook | ngrok exposes write-capable endpoint without auth; spam/malicious payload risk. | Client | `ACCEPTED` | `HIGH` | 2026-01-05 | 2026-01-06 |
| `T801A-RISK-002` | Timestamp Timezone Ambiguity | Pine can emit UTC or local TZ; storage is naive; breaks dedup/history keying. | LLM_Consultant | `MITIGATED` | `HIGH` | 2026-01-05 | 2026-01-06 |
| `T801A-RISK-003` | Override Storage Mode Erases History | Default `data_storage_mode=\"override\"` can overwrite prior history. | Client | `MITIGATED` | `MEDIUM` | 2026-01-05 | 2026-01-06 |
| `T801A-RISK-004` | VWAP Filtering tf Code Dependency | If `tf` becomes display-form, VWAPFilter fails-open. | LLM_Developer | `MITIGATED` | `MEDIUM` | 2026-01-05 | 2026-01-06 |
| `T801A-RISK-005` | At-Least-Once Delivery Duplicates/Loss | TradingView resends on 5xx; imperfect dedup can duplicate or drop rows. | Client | `MITIGATED` | `HIGH` | 2026-01-05 | 2026-01-06 |
| `T801A-RISK-006` | 3-Second Webhook Cancellation | TradingView cancels if processing exceeds ~3s; synchronous pipeline may exceed under load. | Client | `MONITORED` | `MEDIUM` | 2026-01-05 | 2026-01-06 |
| `T801A-RISK-007` | Message Body Size Limit | 40960 char cap limits feasible `(exportRows × tf_count)`. | LLM_Consultant | `MITIGATED` | `MEDIUM` | 2026-01-05 | 2026-01-06 |
| `T801A-RISK-008` | Repainting/Confirmation Drift | Multi-TF rows from `request.security()` can change after initial alert delivery. | LLM_Consultant | `ACCEPTED` | `MEDIUM` | 2026-01-05 | 2026-01-06 |
| `T801A-RISK-009` | Volume Integration Risk | OBV-based volume confirmation per `T801A-ASSUM-003` is a new addition to the TTI protocol with significant uncertainty (value-add, complexity, false positives in low-volume conditions). Impact: If realized, volume confirmation is removed from MVP scope. | Client | `MONITORED` | `HIGH` | 2025-12-31 | 2026-01-06 |


##### x. Epic Changelog
<!-- Lightweight audit trail for material changes within this Epic. -->

- **2026-01-10**: Subphase 1.4 SSOT implementation (approved Phase 1 scope):
  - Inserted 41 E-RIDs into `##### v. Epic Requirements`
  - Inserted 6 E-GDRs (index + bodies) into `##### vii. Epic Governance Decisions`
  - Inserted 17 Epic Issues/Risks into `##### viii. Epic Issues & Risks` (no promoted Feature items)

### D. Project Glossary
<!-- Define project-specific terms used in this SPS for clarity and consistency. -->

## IV. GLOSSARY
<!-- Global glossary or references shared across initiatives, if applicable. -->

---

## V. APPENDIX 

### A. Amendment Log
| Date | Change Requester | Affected Req. ID | Summary of Change |
| :--- | :--- | :--- | :--- |

---

## VI. VALIDATION CHECKLIST
<!-- Use as readiness gate before handoff. Keep criteria concise and verifiable. -->

- [ ] YAML header complete and correct
- [ ] Problem Definition (Section III-A) approved by decision owner
- [ ] Issues and Risks logged in Section III-B.9 and III-C.ix
- [ ] Next Steps clearly define handoff to downstream workflow

---

## VII. STAKEHOLDER SIGN-OFF
<!-- Formal approval section with names/dates for auditability. -->

---

## VIII. NEXT STEPS
<!-- Outline immediate next actions and handoff to downstream workflow (e.g., Request). Keep concise and actionable. -->

---

## IX. CHANGELOG
<!-- Brief audit trail of material changes to this artifact. Keep entries short with date/author/summary. -->
