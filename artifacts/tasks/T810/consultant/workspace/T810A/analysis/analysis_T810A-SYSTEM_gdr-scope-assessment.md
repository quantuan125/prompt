---
artifact_type: 'ANALYSIS'
initiative_id: 'T810'
epic_id: 'T810A'
research_id: 'T810A-RES-003'
version: '1.0.0'
date: '2025-10-26'
status: 'review'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
source_artifact: 'prompt/artifacts/tasks/T810/research/brief/brief_T810A-SYSTEM_gdr-scope-assessment.md'
---

# ANALYSIS: Epic GDR Scope Assessment & Revision Path (T810A)

## I. Executive Summary

This analysis evaluates six Epic-level Governing Design Rules (GDRs) in the T810A SPS for true Epic scope vs Feature specificity, validates abstraction levels for retained E-GDRs, confirms E‑RID reference mapping soundness, and recommends precise revision paths. Primary test is cross-feature applicability centered on T810A1 (PROMPT) and T810A2 (PATIENT/schemas), with T810A3/A4 as secondary validation.

Summary classification and priorities:
- F‑GDR (demote to Feature): GDR‑001, GDR‑004 — High priority demotion
- E‑GDR (retain at Epic with abstraction/IG/ADR alignment): GDR‑002, GDR‑003, GDR‑005, GDR‑006 — High priority refinement except GDR‑005 (Medium)

Key revision actions:
- Extract implementation details from GDR bodies into Epic ADRs/IGs; replace A1‑specific references with E‑RIDs.
- Establish Epic ADRs: T810A‑ADR‑002 (Confidence Policy), T810A‑ADR‑005 (GI Sources Catalog), T810A‑ADR‑006 (Dual‑Purpose Reporting).
- Update SPS to remove “Block 4” and A1 INT/IF/NFR anchors in GDR bodies; reference E‑IG‑00x and dependencies instead.

Confidence: High for 001/003/004/005; Moderate‑High for 006; High for 002 with ADR extraction.

---

## II. Research Scope & Method

Scope domains (per brief):
- Domain A: Epic scope validation via cross‑feature applicability (A1/A2 primary, A3/A4 secondary).
- Domain B: Abstraction level validation — identify implementation details to move to Epic ADRs/IGs.
- Domain C: E‑RID mapping validation — ensure authority, completeness, and non‑circularity.
- Domain D: Per‑GDR revision strategy — Abstraction, ADR extraction, Hybrid split, Retention, or Demotion.
- Domain E: Downstream impact — coordination primarily across A1/A2.

Methodology:
- Hypothesis‑based inference from Feature Register, SPS, A2 Plan, and Request artifacts.
- Clinical AI patterns and GI domain knowledge to infer feature behaviors.
- Confidence indicators attached to each classification.

Classification criteria:
- E‑GDR: Applies to A1 + A2 at minimum, or ≥3 features with clear Epic governance value.
- F‑GDR: Primarily/exclusively A1, with no clear A2 (or broader) applicability.

---

## III. Cross‑Feature Applicability Matrix (Domain A)

| GDR | T810A1 (PROMPT) | T810A2 (PATIENT) | T810A3 (REPORT)* | T810A4 (TOOLS)* | Epic Classification | Confidence |
|:----|:-----------------|:-----------------|:-----------------|:----------------|:--------------------|:-----------|
| GDR‑001 Tracking‑First Protocol | ✅ 5‑phase protocol | ❌ | ❓ | ❓ | F‑GDR (Demote) | High |
| GDR‑002 Trust‑and‑Verify | ✅ Qualitative confidence | ✅ Confidence field semantics | ✅ Consumes validated inputs | ❓ | E‑GDR (Abstract + ADR) | High |
| GDR‑003 Stable/Dynamic JSON | ✅ Generate dynamic entries | ✅ Define schemas/authority | ✅ Aggregate | ❓ | E‑GDR (Retain + IG refs) | High |
| GDR‑004 Session Workflow | ✅ Memory review/init steps | ❌ | ❓ Different workflow | ❓ | F‑GDR (Demote) | High |
| GDR‑005 GI Knowledge Sources | ✅ Clinical reasoning sources | ✅ Vocab/scales alignment | ✅ Interpretations | ❓ | E‑GDR (Abstract) | High |
| GDR‑006 Dual‑Purpose Reporting | ✅ Session‑end reporting | ✅ Timestamps/fields align | ✅ Aggregation/reporting | ❓ | E‑GDR (Hybrid Split) | Mod‑High |

*A3/A4 are secondary validation only per brief; primary test is A1/A2 relationship.

---

## IV. Abstraction Level Validation (Domain B)

Implementation details embedded in GDR bodies that should move to Epic ADRs/IGs or be removed:

- GDR‑001 (Demote): 5‑phase hierarchy, 2‑loop minimum, Engage→Probe merge — all A1‑specific; remove from Epic.
- GDR‑002 (Abstract/ADR): Numeric confidence thresholds (70%, 90%); image‑specific examples; require qualitative user‑facing language. Move numeric thresholds and examples to T810A‑ADR‑002; keep qualitative governance in GDR.
- GDR‑003 (Abstract/IG): “Block 4” storage wording; A1 “end‑of‑day per INT‑002”; replace with Epic‑neutral “designated knowledge storage” and reference E‑IG‑006 + dependency on A3 (T810A‑DEP‑002).
- GDR‑004 (Demote): Session init steps (Memory Review Step 0, Context Loading Step 1), conflict prompts; retain generalized memory review and handoff in E‑IG‑005/006, not in GDR; demote A1 specifics.
- GDR‑005 (Abstract/ADR): “Block 4” mention; create Epic catalog ADR for authoritative sources and maintenance policy (T810A‑ADR‑005).
- GDR‑006 (Hybrid Split): Voice mandate (“first‑person”), 100–200 token target, trigger commands, validation loop; move to E‑ADR‑006 and E‑IG‑006; keep dual‑purpose principle in GDR.

---

## V. E‑RID Reference Mapping Validation (Domain C)

Validation criteria: Authority preserved, completeness of F‑RID replacement, no circularity, no missing E‑RID coverage.

Summary mapping patterns (by category):
- IF‑006 → E‑IG‑004; IF‑005/INT‑005/INT‑004 → E‑IG‑006/IG‑005/IG‑006; IF‑003 → E‑IG‑003.
- NFR‑001/002/004/007/009 → E‑QG‑001/002/004/007 and E‑IG‑002.
- ASSUM‑001 → E‑ASSUM‑001; CON‑006/007/008 → E‑CON‑002/003/004; DEP‑002/004/005 → E‑DEP‑002/004/005.

Result: Authority preserved; references complete after demotions; no circularity; no material missing coverage. Numeric thresholds for GDR‑002 intentionally moved to ADR.

---

## VI. Per‑GDR Assessments (Domain D)

### GDR‑001 Assessment

**Epic Scope Test**: FAIL
- Feature applicability: A1 only; A2 no; A3/A4 unclear.
- Epic appropriateness: Conversational protocol and 2‑loop pattern are A1‑specific.

**Implementation Details Identified**:
1. 5‑phase hierarchy + 2‑loop pattern — Remove from Epic; demote to A1.
2. Engage phase merged into Probe — Remove from Epic; demote to A1.

**E‑RID Mapping Validation**:
- Current F‑RID refs: T810A1‑NFR‑001/002/008/009; T810A1‑IF‑006; T810A1‑ASSUM‑001.
- Proposed E‑RID mapping: NFR‑001 → T810A‑QG‑001; NFR‑002 → T810A‑QG‑002; NFR‑008 → T810A‑IG‑001; NFR‑009 → T810A‑IG‑002; IF‑006 → T810A‑IG‑004; ASSUM‑001 → T810A‑ASSUM‑001.
- Missing coverage: None required at Epic (loop pattern remains feature‑level).
- Circular reference risk: Low (post‑demotion).

**Recommended Revision Strategy**: DEMOTION
- Rationale: Fails A1+A2 applicability; governance is conversational and feature‑specific.
- Proposed destination: `T810A1‑GDR‑001 (Tracking‑First Protocol)`

**Revision Priority**: HIGH
**Blocking Issues**: None

### GDR‑002 Assessment

**Epic Scope Test**: NEEDS ABSTRACTION
- Feature applicability: A1 qualitative confidence; A2 confidence field semantics; A3 consumption behaviors.
- Epic appropriateness: Cross‑cutting safety/communication governance.

**Implementation Details Identified**:
1. Numeric thresholds (70%, 90%) — Move to ADR; forbid numeric in user‑facing text; allow internal numeric for machine logs.
2. Image‑specific phrasing — Keep as examples in ADR; maintain generalized GDR language.

**E‑RID Mapping Validation**:
- Current F‑RID refs: T810A1‑NFR‑007; T810A1‑IF‑003; T810A1‑CON‑008.
- Proposed E‑RID mapping: NFR‑007 → T810A‑QG‑007; IF‑003 → T810A‑IG‑003; CON‑008 → T810A‑CON‑004.
- Missing coverage: None; numeric guidance shifts to ADR.
- Circular reference risk: Low.

**Recommended Revision Strategy**: ADR EXTRACTION
- Proposed Epic ADR: `T810A‑ADR‑002 (Trust‑and‑Verify Confidence Policy)` — qualitative tiers, example phrasings, optional internal numeric bands; explicitly prohibit numeric in user‑facing prose.
- Proposed revised GDR language (Epic‑level): “Features shall communicate result confidence qualitatively and incorporate user validation appropriate to context. Numeric confidence values, when used, are internal only and must not appear in user‑facing communication.”

**Revision Priority**: HIGH
**Blocking Issues**: None

### GDR‑003 Assessment

**Epic Scope Test**: PASS
- Feature applicability: A1 (generation), A2 (schema authority), A3 (aggregation).
- Epic appropriateness: Canonical data architecture for the Epic.

**Implementation Details Identified**:
1. “Block 4” & A1‑specific INT‑002 references — Replace with Epic‑neutral “designated knowledge storage” and reference E‑IG‑006 + T810A‑DEP‑002.
2. Session‑specific loading phrasing — Reference E‑IG‑005/006 rather than A1 INTs.

**E‑RID Mapping Validation**:
- Current F‑RID refs: T810A1‑IF‑006; INT‑004/005; NFR‑009; CON‑008; DEP‑004/002.
- Proposed mapping: IF‑006 → T810A‑IG‑004; INT‑004 → T810A‑IG‑006; INT‑005 → T810A‑IG‑005; NFR‑009 → T810A‑IG‑002; CON‑008 → T810A‑CON‑004; DEP‑004 → T810A‑DEP‑004; DEP‑002 → T810A‑DEP‑002.
- Missing coverage: None after E‑IG references.
- Circular reference risk: Low.

**Recommended Revision Strategy**: HYBRID SPLIT
- Epic principle (GDR): Establish Stable (patient‑governed) vs Dynamic (LLM‑generated) split and authorities.
- Implementation pattern (E‑IG): Single‑entry rule (E‑IG‑004), session context/memory (E‑IG‑005/006), aggregation via A3.
- Proposed revised GDR language (Epic‑level): “The Epic shall implement a Stable (patient‑governed) and Dynamic (LLM‑generated) data split. Authoritative schemas and value sets are owned by T810A2. Cross‑session aggregation and reporting are owned by T810A3. Features generating tracking data shall follow the single‑entry per interaction rule per E‑IG‑004.”

**Revision Priority**: HIGH
**Blocking Issues**: None

### GDR‑004 Assessment

**Epic Scope Test**: FAIL
- Feature applicability: A1 conversational session workflow; A2 no session; A3 different lifecycle.
- Epic appropriateness: Stepwise session init is A1‑specific prompting pattern.

**Implementation Details Identified**:
1. Step 0 Memory Review, Step 1 Context Loading, conflict prompts — Maintain generalized forms in E‑IG‑005/006; remove A1 specifics from GDR.
2. “Stable JSON > Memory” enforcement — Keep as Epic IG rule; not in GDR body; remove A1 INT references.

**E‑RID Mapping Validation**:
- Current F‑RID refs: INT‑005; IF‑005/006; NFR‑001/002.
- Proposed mapping: INT‑005 → T810A‑IG‑005; IF‑005 → T810A‑IG‑006; IF‑006 → T810A‑IG‑004; NFR‑001/002 → T810A‑QG‑001/002.
- Missing coverage: None.
- Circular reference risk: Low post‑demotion.

**Recommended Revision Strategy**: DEMOTION
- Rationale: Fails A1+A2 scope test; properly lives as A1 governance, while Epic retains generalized E‑IG‑005/006.
- Proposed destination: `T810A1‑GDR‑004 (Session Workflow Architecture)`

**Revision Priority**: HIGH
**Blocking Issues**: None

### GDR‑005 Assessment

**Epic Scope Test**: PASS
- Feature applicability: A1 reasoning; A2 vocab/scale alignment; A3 interpretive consistency.
- Epic appropriateness: Knowledge governance belongs at Epic.

**Implementation Details Identified**:
1. “Block 4” reference — Replace with “designated knowledge storage”.
2. Maintenance policy details — Move enumerations/versioning cadence to ADR.

**E‑RID Mapping Validation**:
- Current F‑RID refs: T810A1‑NFR‑004; IF‑003; CON‑006/007; DEP‑005.
- Proposed mapping: NFR‑004 → T810A‑QG‑004; IF‑003 → T810A‑IG‑003; CON‑006 → T810A‑CON‑002; CON‑007 → T810A‑CON‑003; DEP‑005 → T810A‑DEP‑005.
- Missing coverage: None.
- Circular reference risk: Low.

**Recommended Revision Strategy**: ABSTRACTION
- Proposed Epic ADR: `T810A‑ADR‑005 (GI Knowledge Sources Catalog)` — authoritative list, versioning, maintenance.
- Proposed revised GDR language (Epic‑level): “The Epic’s knowledge base shall be grounded in authoritative GI sources managed under a versioned catalog. Storage is designated knowledge storage. Safety remains governed by Epic constraints; comprehensive compliance is deferred.”

**Revision Priority**: MEDIUM
**Blocking Issues**: None

### GDR‑006 Assessment

**Epic Scope Test**: NEEDS ABSTRACTION
- Feature applicability: A1 generates; A2 fields/format alignment; A3 aggregates/consumes.
- Epic appropriateness: Dual‑purpose reporting principle is Epic‑level.

**Implementation Details Identified**:
1. First‑person voice mandate; 100–200 token target; trigger commands; validation loop — Move to ADR/IG.
2. A1 INT‑002 anchoring — Reference E‑IG‑006 and A3 dependency instead.

**E‑RID Mapping Validation**:
- Current F‑RID refs: INT‑002; IF‑005; A3 dependency.
- Proposed mapping: INT‑002/IF‑005 → T810A‑IG‑006; A3 dependency → T810A‑DEP‑002.
- Missing coverage: None.
- Circular reference risk: Low.

**Recommended Revision Strategy**: HYBRID SPLIT
- Epic principle (GDR): “A single report shall serve both clinician handoff and next‑session context injection across the Epic.”
- Implementation pattern (E‑ADR/IG): `T810A‑ADR‑006 (Dual‑Purpose Reporting Policy)` — voice, length targets, triggers, validation loop, JSON export; `E‑IG‑006` governs handoff/injection.
- Proposed revised GDR language (Epic‑level): “The Epic adopts a unified reporting principle serving clinician handoff and LLM memory. Specific format, voice, length targets, triggers, validation loop, and export forms are defined in E‑ADR‑006; cross‑feature handoff is governed by E‑IG‑006.”

**Revision Priority**: HIGH
**Blocking Issues**: None

---

## VII. Downstream Impact (Domain E)

T810A1 (PROMPT):
- Update S05 Execution Protocol to reference A1‑local GDRs/ADRs for demoted 001/004.
- Replace direct GDR body references with E‑IG/E‑QG where implementation details moved. Ensure IF/NFR/INT refer to Epic IGs.
- Maintain prohibition of numeric confidence in user‑facing text; if internal numeric is used in JSON, keep strictly machine‑only.

T810A2 (PATIENT):
- Align schema semantics and controlled vocabularies with E‑IG/E‑ADR outcomes (confidence semantics, scales, timestamps). Avoid duplicating Epic governance.
- Confirm authority boundaries (A2 owns schemas/value sets; A1 generates entries; A3 aggregates).

T810A3 (REPORT):
- Own aggregation/report types and persistence; accept governance from E‑IG‑006 and GDR‑006 (post‑abstraction). Remove A1 INT‑002 anchoring in Epic GDR bodies.

T810A4 (TOOLS):
- No blocking impacts identified; future tool selection policies may reference E‑IG patterns.

Coordination Requirements List:
- Notify A1 subconsultant of demotions (001/004) and new Epic ADRs.
- Provide ADR drafts and SPS redlines for review; confirm updated references in Requests.
- Confirm A2’s schema decisions integrate confidence semantics per ADR‑002.

---

## VIII. Critical Questions for Phase 3B Consultations

1) GDR‑001 — Is the “2‑loop pattern” an Epic requirement or a T810A1 implementation choice?
- Options:
  - A) Epic‑level requirement (harden via E‑IG): Ensures uniformity; risk of misfit for non‑conversational features (A2/A4). Increases governance rigidity.
  - B) Feature‑level decision (A1‑local): Keeps Epic clean; preserves flexibility for A3/A4; requires A1 enforcement via exemplars/tests.
- Trade‑off: Uniformity vs. flexibility. Recommendation: B (Feature‑level only).

2) GDR‑002 — Should numeric confidence thresholds (e.g., 70%, 90%) be retained as internal guidance or removed entirely?
- Options:
  - A) Retain as ADR‑level internal guidance (prohibit numeric in user‑facing prose). Pros: predictable validation intensity; Cons: maintenance overhead, potential false precision.
  - B) Remove numeric entirely; qualitative tiers only. Pros: simplicity; Cons: less consistent prompting across contexts.
- Trade‑off: Consistency vs. simplicity. Recommendation: A (retain in ADR‑002).

3) GDR‑003 — Where should “session initialization” and “end‑of‑day aggregation” be governed?
- Options:
  - A) Keep inside GDR‑003 body. Cons: scope leak to A1; duplicates IGs.
  - B) Reference E‑IG‑005/006 and A3 dependency only. Pros: clean separation; Cons: requires cross‑doc navigation.
- Trade‑off: Self‑containment vs. clean layering. Recommendation: B (IGs + dependency).

4) GDR‑006 — Should “first‑person voice” and “100–200 token” target be Epic‑level rules?
- Options:
  - A) Epic GDR rule. Pros: strong consistency; Cons: constrains future A3 report variants and A1 exploration.
  - B) Epic ADR guidance. Pros: adjustable; Cons: weaker enforcement signal.
- Trade‑off: Consistency vs. adaptability. Recommendation: B (ADR‑006 guidance).

5) Cross‑reference style — Should Epic GDRs ever cite Feature IDs directly?
- Options:
  - A) Allow direct F‑RID citations. Cons: violates traceability rules, creates coupling.
  - B) Require E‑RID substitution or cross‑reference to other Epic artifacts (IG/QG/DEP/ASSUM/CON) only.
- Trade‑off: Author convenience vs. governance hygiene. Recommendation: B (E‑RID only).

---

## IX. Issues & Risks (SPS Table Format)

### A. Issues

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:----------------|
| T810A-ISSUE-001 | Over‑specific GDR bodies | Epic GDR bodies include A1‑specific details ("Block 4", A1 INT/IF/NFR anchors), causing Epic/Feature scope conflation. | LLM_Consultant | OPEN | High | 2025-10-26 | — |
| T810A-ISSUE-002 | Session workflow scope leak | GDR‑004 enforces A1 conversational session workflow across Epic; belongs at A1 with general memory/handoff left in E‑IG‑005/006. | LLM_Consultant | OPEN | High | 2025-10-26 | — |

### B. Risks

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:----------------|
| T810A-RISK-001 | Confidence threshold miscommunication | Numeric thresholds could appear in user‑facing text and erode trust/safety; must be ADR‑only and prohibited in prose (QG‑007). | LLM_Consultant | OPEN | Medium | 2025-10-26 | — |

---

## X. Validation Checklist

- Authority preserved: E‑GDRs reference E‑RIDs (IG/QG/ASSUM/CON/DEP) not A1 F‑RIDs.
- Completeness: All F‑RID references in GDR bodies replaced or moved; demotions documented.
- Circularity: No E‑RID depends on GDRs that depend back on those E‑RIDs.
- Missing coverage: Numeric confidence guidance captured in ADR; no uncovered GDR concept remains.

---

## XI. Epic ADR Creation Plan (Consolidated)

- T810A‑ADR‑002 — Trust‑and‑Verify Confidence Policy
  - Content Scope: Qualitative tiers; example phrasings; optional internal numeric ranges; cross‑modality applicability; explicit prohibition of numeric in user‑facing prose; alignment with QG‑007 and IG‑003.
  - Justification: Standardize verification behavior across features while de‑risking user‑facing communication.
  - Sequencing: Draft ADR → align with A2 schema semantics for confidence fields → validate with A1 prompt patterns → adopt across A3 ingestion.

- T810A‑ADR‑005 — GI Knowledge Sources Catalog
  - Content Scope: Authoritative source list (ROME IV, Bristol, ACG/AGA, alarm features), versioning metadata, update cadence, deprecation policy.
  - Justification: Centralize evidence sources and maintenance governance; remove enumerations from GDR body.
  - Sequencing: Compile v1 catalog → confirm with A1 knowledge usage → publish and link from SPS; update per cadence.

- T810A‑ADR‑006 — Dual‑Purpose Reporting Policy
  - Content Scope: Narrative voice, length targets, trigger commands, validation loop, JSON export schema, A1/A3 coordination rules; ties to IG‑006.
  - Justification: Unify reporting behavior across features without constraining future A3 variants.
  - Sequencing: Coordinate with A3 aggregation design → finalize voice/length guidance → update A1 trigger/validation flows.

---

## XII. Next Steps

1. Author Epic ADR stubs: ADR‑002, ADR‑005, ADR‑006.
2. Redline SPS GDR sections to implement abstraction/demotion and E‑RID substitutions.
3. Coordinate with A1/A2/A3 owners for reference updates and acceptance.

