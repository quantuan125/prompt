---
artifact_type: 'ANALYSIS'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1'
feature_code: 'PROMPT'
activity_id: '0.2-RES-001'
version: '1.0.0'
date: '2025-12-09'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Analyze T810A1-RES-001 impact on T810A1 F-RIDs'
---

# F-RID ENHANCEMENT ANALYSIS: T810A1-RES-001 (Execution Protocol Clinical Validation)

## I. EXECUTIVE SUMMARY

**Purpose**  
To translate `T810A1-RES-001 (Execution Protocol Clinical Validation)` into concrete, non‑normative guidance for enhancing T810A1 Implementation Guidance (IG) F-RIDs and related execution protocol behavior, without yet changing the Request text.

**Scope**  
- Focus: Story `T810A1-S05 (Execution Protocol)` and the surrounding multi‑phase consultation pattern.  
- Categories impacted: primarily `T810A1-IG-*` (new category to be created in Phase 1), with indirect implications for INT, NFR, and story acceptance criteria.  
- Sources: `report_T810A1-PROMPT_s05-execution-protocol-clinical-validation.md` (primary), its brief, and relevant Epic governance (e.g., `T810A-ADR-001` Trust-and-Verify Confidence Policy).

**Method**  
1. Synthesize the core clinical and prompt-pattern findings from `T810A1-RES-001` into a compact finding set aligned with the Phase 0 plan bullets.  
2. Map each finding to candidate `T810A1-IG-*` items (IDs only) and clarify how they should influence S05 gates, probe behavior, and tone.  
3. Identify coverage gaps, ambiguities, and open questions that must be resolved with the Client before editing F-RIDs in Phase 1.

**High-Level Outcome (Intent Only)**  
- Five candidate `T810A1-IG-*` items are identified (gate enforcement, OARS-style probing, epistemic hedging, conditional protocol triggering, and anti-pattern avoidance).  
- Research strongly supports introducing **harder gate language** in S05 and a **minimum probe loop** before coaching, but the exact numeric thresholds and loop counts remain a policy choice for Phase 1.  
- The analysis confirms alignment with Epic confidence rules (`T810A-ADR-001`) and highlights a small set of areas where additional clarification from the Client will be needed (e.g., acceptable trade-offs between protocol rigidity and conversational fluidity).

---

## II. SOURCE MATERIAL SUMMARY (T810A1-RES-001)

### A. Source Overview

- **Artifact**: `report_T810A1-PROMPT_s05-execution-protocol-clinical-validation.md` (+ brief).  
- **Role**: Validates the S05 execution protocol against clinical gastroenterology best practices and tested LLM prompt patterns.  
- **Domains Covered**:
  - Clinical consultation phases and patient‑centered communication.
  - Motivational Interviewing and OARS techniques.
  - Epistemic hedging and therapeutic uncertainty language.
  - LLM agent design patterns (gate-based enforcement, VPA-style conditional triggering, anti-pattern catalog).

### B. Key Findings (Structured Summary)

1. **Five‑Phase Consultation Protocol**  
   - Real-world GI consultations proceed through a **structured flow**: open narrative, structured symptom inquiry, analysis, collaborative plan, and summary.  
   - Translating this into S05 implies a **multi‑phase execution protocol** with clearly separated Engage, Analyze, Probe, Coach, and Summarize segments.

2. **OARS Technique & Probing Quality**  
   - Effective consultations use **OARS (Open questions, Affirmations, Reflective listening, Summaries)** to elicit rich context and maintain rapport.  
   - For S05, this suggests Probe phase guidance that emphasizes **open‑ended clarifying questions**, reflective statements, and periodic summaries rather than rapid‑fire interrogation.

3. **Epistemic Hedging & Therapeutic Uncertainty**  
   - Clinicians communicate uncertainty transparently but reassuringly (e.g., acknowledging limits while emphasizing safety and partnership).  
   - For PROMPT, research supports explicit guidance on **qualitative confidence language**, avoiding false reassurance, and avoiding numeric confidence in user‑facing text (aligned with `T810A-ADR-001`).

4. **Gate‑Based Enforcement & Multi‑Loop Requirement**  
   - VPA‑style prompts demonstrate that **explicit gates** (conditions that must be satisfied before moving to the next phase) reduce protocol drift.  
   - Research recommends **at least one full Probe loop** (and preferably more) before entering Coach, with explicit criteria for when coaching is allowed.

5. **VPA Conditional Triggering**  
   - Execution behavior changes based on **input type** (e.g., one‑off question vs tracking update vs complex consult).  
   - For S05, this suggests guidance to detect whether the user is asking a question, submitting tracking data, or initiating a deeper consultation, and to trigger the appropriate protocol variant.

6. **Anti‑Patterns Catalog**  
   - Several communication and behavior anti‑patterns are identified: premature coaching, minimizing symptoms, ignoring explicit fears, over‑reassurance, and generic “assistant” tone.  
   - The research supports creating **explicit prohibitions** against these patterns in PROMPT‑level guidance.

---

## III. F-RID IMPLICATIONS (INTENT ONLY, NO TEXT CHANGES)

### A. Candidate T810A1-IG Items

The table below maps each research finding to a **candidate** `T810A1-IG-*` item. These IDs and short titles are proposed anchors for Phase 1 work; the actual F-RID bodies will be drafted and approved later.

| Source Finding                    | Candidate F-RID ID   | Short Title                    | Implication for S05 / PROMPT                           | Proposed Phase 1 Action                        |
| :-------------------------------- | :------------------- | :----------------------------- | :----------------------------------------------------- | :--------------------------------------------- |
| Gate‑Based Enforcement            | `T810A1-IG-001`      | Execution Gate Rules           | Define **hard preconditions** for phase transitions.   | Create F-RID specifying gates for S05 phases.  |
| OARS Technique                    | `T810A1-IG-002`      | Probe Question Pattern         | Require OARS‑style probes and reflective listening.    | Create F-RID describing Probe dialogue style.  |
| Epistemic Hedging                 | `T810A1-IG-003`      | Confidence Communication       | Align confidence language with `T810A-ADR-001`.        | Create F-RID formalizing hedging/tone rules.   |
| VPA Conditional Triggering        | `T810A1-IG-004`      | Input‑Type Detection           | Adjust protocol based on user input type.              | Create F-RID for routing based on intent.      |
| Anti‑Patterns (communication)     | `T810A1-IG-005`      | Prohibited Behaviors           | List behaviors PROMPT must avoid or reframe.          | Create F-RID banning specific anti‑patterns.   |

### B. Relationship to Existing Requirements (High-Level)

- **Stories**:  
  - S05 currently describes an execution protocol but lacks a structured IG category that **centralizes** gate rules and probe behavior. The proposed `T810A1-IG-*` items would become the **normative home** for these rules, with S05 stories referencing them rather than re‑stating logic.

- **NFRs / INTs**:  
  - Existing non‑functional and integration requirements around tone, confidence, and session handling would be **aligned** with the new IG items (e.g., NFRs on persona and tone, INTs governing session memory and JSON generation).  
  - No immediate deletions are implied; the analysis instead suggests **tightening cross‑references** from NFR/INT items back to the IG category.

---

## IV. GAP ANALYSIS & RISKS

### A. Coverage Strength

- Research provides **strong qualitative support** for:
  - Having **explicit gates** between phases.  
  - Enforcing at least one Probe loop before coaching.  
  - Using OARS techniques and hedging language.  
  - Avoiding common conversational anti‑patterns.

- Coverage is **moderate** for:
  - Exact numeric thresholds or counts (e.g., “minimum 2 probe turns” vs “at least 1”).  
  - Specific trigger conditions for shifting between variants of the execution protocol (tracking vs consult vs quick Q&A).

### B. Identified Gaps

- **Quantitative Protocol Parameters**  
  - The research argues for “multiple” probe interactions but does not mandate a precise number. Phase 1 must decide whether to encode **hard numeric minima** (e.g., 2 loops) or more flexible criteria.

- **Edge-Case Handling**  
  - Limited explicit guidance on high‑urgency or safety‑critical scenarios (e.g., red‑flag symptoms) where protocol might need to **skip or compress** certain phases while still honoring clinical communication norms.

- **Interaction with Platform Constraints**  
  - The research assumes stable execution of gate logic but does not fully address **ChatGPT behavior quirks** (e.g., refusal overrides, system message interactions). Phase 1 needs to consider how to encode gates robustly within these constraints.

### C. Risk Summary (If Unaddressed)

- Without IG items, S05 risks **continued drift** towards single‑loop, assistant‑style behavior with premature coaching.  
- Lack of clear anti‑pattern prohibitions could allow the model to **revert to generic assistant tone**, undermining clinical positioning and trust.  
- Ambiguous gate rules may yield **inconsistent user experiences** between sessions or different prompts.

---

## V. OPEN QUESTIONS & RECOMMENDATIONS FOR PHASE 1

### A. Questions for Client / Governance

1. **Gate Strictness**: How strict should S05 gates be? Is a **hard requirement** (e.g., “at least 2 Probe turns”) acceptable, or should we favor softer but strongly worded guidance?  
2. **High-Urgency Exceptions**: In suspected red‑flag scenarios, is it acceptable to **shorten or skip** phases (e.g., fast‑track to Coach/Summarize with safety advice), and how should this be framed?  
3. **Tone vs Efficiency**: When probe loops grow long, how should the agent balance thoroughness with user fatigue (e.g., explicit check‑ins like “Is it okay if I ask two more questions?”)?

### B. Recommendations for Phase 1 Editing

- Treat the five candidate `T810A1-IG-*` items as the **primary vehicles** for encoding execution protocol behavior and communication rules.  
- Keep S05 story text focused on **narrative scenario and acceptance criteria**, with detailed protocol logic living in IG items.  
- When drafting IG bodies:
  - Reuse wording patterns already validated in `T810A2` IG/INT items where applicable (for consistency).  
  - Align all confidence language with `T810A-ADR-001`; avoid numeric confidence in user‑facing examples.  
  - Make anti‑patterns explicit and testable (e.g., “shall not move to Coach before confirming understanding at least once”).

---

## VI. APPROVAL STATUS & CHANGE LOG

### A. Approval Status

- **Status**: `draft`  
- **Intended Use**: Input to Phase 1 F-RID and story edits for `T810A1-PROMPT`. This document is **non-normative** and does not itself change any F-RIDs.

### B. Change Log

- **2025-12-09 — Initial Draft (Subphase 0.2)**  
  - Created first version of `analysis_T810A1-PROMPT_frid-enhancement_res-001.md` based on Phase 0 plan.  
  - Summarized `T810A1-RES-001` findings, proposed five candidate `T810A1-IG-*` items, and documented gaps and recommendations for Phase 1.

