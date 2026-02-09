---
artifact_type: 'PLAN'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A1'
feature_code: 'PROMPT'
version: '1.0.0'
date: '2025-12-15'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# CONSULTANCY PLAN: Multi-Entry Tracking & Aggregation Decision (T810A / T810A1-S05 / T810A2)

## I. EXECUTIVE SUMMARY

This plan defines the Phase 2 consultancy workstream to resolve a tracking/aggregation mismatch uncovered in QA for `T810A1-S05 (Execution Protocol)`: legacy PROMPT governance (`T810A-IG-004`, derived into `T810A1-IG-007`) assumed **exactly one tracking payload object per relevant user message**, but patient inputs can contain **multiple trackable events** in a single turn (e.g., 4 stool images + current bloating → 5 entries). In parallel, the Client prefers the organizational semantics of aggregation **Pattern B**, while prior guidance recommended **Pattern A**. A structured comparative analysis (including Pattern C) and a formal decision record are required to unblock both `T810A2-SCHEMA` and `T810A1-S05` prompt wording.

**Primary Objective**
- Select the MVP per-turn Dynamic JSON **envelope/aggregation pattern** (Pattern A vs B vs C) and define the associated “multi-entry per single message” rule, in a way that is consistent with Epic governance and future `T810A3-REPORTING` needs.

**Secondary Objectives**
- Amend Epic-level governance (`T810A-IG-004`) and dependent Feature F-RIDs (notably `T810A1-IG-007`) to remove the “exactly one object per message” constraint and replace it with a “per-turn delta (1+ entries) without cumulative regeneration” policy.
- Produce a cross-feature handoff brief so `T810A2-SCHEMA` and `T810A1-PROMPT` implement the decision consistently (schemas, exemplars, and S05 Tier 1/Tier 2 instructions).

**Key Deliverables**
1. **Analysis file** (comparative evaluation of Pattern A/B/C for MVP per-turn output + longer-term implications).
2. **Decision record** (Epic-level ADR/GDR) selecting the envelope/pattern and amending Epic governance (`T810A-IG-004`) accordingly.
3. **Communication brief** to both `T810A2-SCHEMA` and `T810A1-PROMPT` defining responsibilities and required edits.
4. **Phase 2 Proposal updates** to `proposal_T810A1-PROMPT_phase2.md` for `T810A1-S05` Tier 1 and Tier 2 tracking instructions (and any cross-block references impacted by the decision).

---

## II. CONTEXT MATERIALS & PREREQUISITES

### A. Required Reading Before Each Subphase

**Epic Governance (SSOT)**
- `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md` — includes `T810A-IG-004 (Tracking Payload Per-Turn Delta)` and `T810A-GDR-002 (Schema Split Architecture)`
- `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md` — Epic ADR compendium (notably `T810A-ADR-002`, `T810A-ADR-003`)

**T810A1 (PROMPT)**
- `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md` — `T810A1-IG-007` and `T810A1-S05` assumptions
- `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A1/proposal_T810A1-PROMPT_phase2.md` — Block 5 (S05) Tier 1/Tier 2 wording

**T810A2 (SCHEMA)**
- `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md` — `T810A2-INT-002 (Aggregation Format Integration)` and manual export workflow assumptions
- `prompt/artifacts/tasks/T810/consultant/workspace/communication/consultant/handoff_brief_T810A2-SCHEMA_to_T810A1-PROMPT_phase2.md` — Pattern A/B/C definitions and trade-offs

**Schema Templates (renamed files — authoritative names)**
- `prompt/roles/gastro/data/template_stable_patient_schema.yaml` — previously referenced as `patient.yaml`/`template_stable_json_example.yaml`
- `prompt/roles/gastro/data/template_dynamic_tracking_schema.yaml` — previously referenced as `combined_dynamic_schema_mvp.yaml`
- `prompt/roles/gastro/data/field_classification_mapping.md`

**Aggregation Exemplars**
- `prompt/roles/gastro/data/aggregation_mixed_array_example.json` (Pattern A)
- `prompt/roles/gastro/data/aggregation_per_type_arrays_example.json` (Pattern B)
- `prompt/roles/gastro/data/aggregation_hybrid_index_example.json` (Pattern C)

**Structural Exemplars**
- Analysis exemplar: `prompt/artifacts/tasks/T810/consultant/workspace/analysis/analysis_T810A1-PROMPT_frid-enhancement_res-001.md`
- Plan exemplar: `prompt/artifacts/tasks/T810/consultant/workspace/plan/T810A/T810A1/plan_T810A1-PROMPT_frid-enhancement.md`
- Communication exemplar: `prompt/artifacts/tasks/T810/consultant/workspace/communication/consultant/handoff_brief_T810A2-SCHEMA_to_T810A1-PROMPT_phase2.md`

---

## III. PROBLEM STATEMENT (WORKING, APPROVED IN QA)

### A. Core Mismatch

1. **Multi-event per single user message is common and clinically relevant**
   - Example: multiple stool photos + symptom narrative + meal context in a single turn.
2. Current governance stated **“exactly one tracking payload object per relevant user message”** (`T810A-IG-004` → `T810A1-IG-007`), which fails to represent multi-event turns without data loss.
3. The aggregation/envelope choice (A/B/C) governs the per-turn JSON contract; without an explicit choice, S05 prompt instructions cannot be made unambiguous.

### B. Constraints & Non-Negotiables (from QA)

- **Per-turn output governance is MVP priority** (export/report aggregation may be implemented later in `T810A3`).
- LLM_Gastro outputs tracking JSON **in a single fenced `json` codeblock** per response when tracking is required.
- A single patient message MAY yield **multiple entries** in that single codeblock (e.g., 4 stool + 1 digestion = 5).
- IDs are optional and may be omitted; chronology should rely on timestamp/order.
- Platform constraints: no programmatic validation; schema adherence must be prompt/governance-driven.

---

## IV. DECISION WORKSTREAM (PHASE 2: DEVELOP & DELIVER)

### A. Decision Criteria (to confirm before scoring)

Use (or explicitly revise) the T810A2 baseline criteria set:
1. **Schema Clarity & Usability** (LLM interpretability; low drift risk)
2. **Integration Consistency** (A1/A2/A3 forward compatibility; avoids contradictory governance)
3. **Token Optimization** (per-turn overhead)
4. **User Experience Alignment** (patient copy/paste; manual Cara Care logging workflow)
5. **Clinical Validity & Completeness** (supports multi-event turns without loss)

### B. Weighting Method

Propose weights (Client confirm as Gate before scoring):
- Schema Clarity & Usability: 0.30
- Integration Consistency: 0.25
- Clinical Validity & Completeness: 0.20
- Token Optimization: 0.15
- User Experience Alignment: 0.10

### C. Options Under Evaluation

- **Option 0 (Status Quo / Do-Nothing)**: Keep “exactly one object per message” and accept loss/forced compression of multi-event turns.
- **Option A (Pattern A)**: Single mixed chronological array (per-turn output is always an array of entry objects).
- **Option B (Pattern B)**: Per-type arrays under a top-level object (per-turn output is always a typed container with arrays).
- **Option C (Pattern C)**: Hybrid `entries` array + `index_by_type` index.

---

## V. SUBPHASES, ACTIONS, AND DELIVERABLES

### Subphase 2.0 — Normalize Reference Corrections (Schema Renames)

**Purpose**: Remove ambiguity caused by stale file names in PROMPT and SCHEMA artifacts and ensure all downstream edits reference the renamed schema templates.

**Actions**
- Identify and log all references to:
  - `combined_dynamic_schema_mvp.yaml` → `prompt/roles/gastro/data/template_dynamic_tracking_schema.yaml`
  - `patient.yaml` and/or `template_stable_json_example.yaml` → `prompt/roles/gastro/data/template_stable_patient_schema.yaml`
- Classify the rename changes as:
  - **Editorial-only** (preferred): purely reference corrections, no schema semantics change.
  - **Interface-impacting** (if discovered): requires updating relevant IF/INT items where file names are treated as interface contracts.

**Output**
- Add a “Reference Correction Note” subsection inside the Subphase 2.1 analysis artifact so this is traceable under the `T810A-ADR-005` Provenance chain.

### Subphase 2.1 — Create Comparative Analysis Artifact (Pattern A/B/C)

**Target File (new)**
- `prompt/artifacts/tasks/T810/consultant/workspace/analysis/analysis_T810A-SYSTEM_dynamic-json-envelope-decision.md`

**Structural Requirement**
- Follow `analysis_T810A1-PROMPT_frid-enhancement_res-001.md` sectioning and tone (Executive Summary → Source Summary → Implications → Gaps/Risks → Recommendations).

**Analysis Scope**
- Define each pattern in “per-turn output contract” terms (not backend storage terms).
- Evaluate each option against the confirmed criteria/weights.
- Explicitly analyze:
  - Multi-entry turns (stool images + symptoms)
  - Manual patient compilation workflow (copy codeblocks → build a file)
  - Forward compatibility with `T810A3-REPORTING` (aggregation, reporting timeline)
  - Drift risk given “no validation” constraint

**Gate**
- Present scored table + recommendation and request Client approval before drafting decision record.

---

### Subphase 2.2 — Construct `T810A-ADR-005` and Amend Epic Governance (Dependency: 2.1)

**Purpose**: Convert the chosen pattern into a single authoritative governance decision that downstream features can reference.

**Mandatory Decision Record Choice (fixed by QA)**
- Create **`T810A-ADR-005`** in `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md`.
- `T810A-ADR-005` MUST follow `T102-STD-004 (Decision Records Index)` formatting rules (index row + body + stable anchor).

**Dependency Rule (completion gate)**
- Subphase 2.2 MUST NOT complete until Subphase 2.1 is completed, because:
  - `analysis_T810A-SYSTEM_dynamic-json-envelope-decision.md` MUST be referenced under **Provenance** in `T810A-ADR-005`.

**ADR Content Requirements (minimum)**
- `T810A-ADR-005` MUST:
  - Select the MVP per-turn JSON envelope/pattern (Pattern A/B/C) for tracking output.
  - Define “per-turn delta” semantics: output only the new entries implied by the current user input (no cumulative regeneration).
  - Explicitly allow **1+ entries** per user message when tracking is required.
  - Define chronology rules (timestamp and ordering expectations) and the ID policy (IDs optional; prefer timestamp + order).

**Epic Amendments (required)**
- Update Epic governance in `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md`:
- Amend `T810A-IG-004 (Tracking Payload Per-Turn Delta)` to remove the legacy “ONE entry per interaction” constraint and replace it with the “per-turn codeblock delta of 1+ entries” policy, preserving the original “no cumulative regeneration” intent.
  - Update `T810A-GDR-002 (Schema Split Architecture)` to explicitly mention adoption of `T810A-ADR-005` and resolve any conflicts introduced by the legacy “single-entry” phrasing.

**ID Amendment Rule**
- All amended Epic and Feature items MUST comply with `T102-STD-005 (ID Specification & Rules)` (directionality, category tokens, ID formatting, and reference formatting).

---

### Subphase 2.3 — Cross-Feature Spec Impact Review (A1 + A2)

**Purpose**: Ensure the `T810A-ADR-005` decision is propagated to all dependent requirements and templates without omissions.

**Actions**
- Produce a short impact matrix enumerating:
  - Epic-level impacted items (at minimum: `T810A-IG-004`, `T810A-GDR-002`)
  - `T810A1` impacted items (at minimum: `T810A1-IG-007`, `T810A1-S05` Tier 1/Tier 2 text in Phase 2 proposal)
  - `T810A2` impacted items (at minimum: `T810A2-INT-002`, and any workflow guidance tied to aggregation/pattern choice)
  - Deliverable files in `prompt/roles/gastro/data/` impacted by the selected pattern (aggregation examples, schema template references)

**Output**
- Include the impact matrix in the Subphase 2.1 analysis artifact as an appendix, so it can be referenced by `T810A-ADR-005` Provenance.

---

### Subphase 2.4 — Implement Feature Updates (T810A1 + T810A2) After `T810A-ADR-005`

**Completion Rule**
- Subphase 2.4 starts only after `T810A-ADR-005` is drafted and accepted (or explicitly marked “Accepted” by the Client), because it amends Feature-level requirements and deliverables.

#### A. T810A2-SCHEMA (Requirements + `prompt/roles/gastro/data/` Deliverables)

**Targets**
- `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md` (update impacted IF/IG/INT items; especially aggregation/manual workflow language)
- `prompt/roles/gastro/data/` (update deliverable example files according to the selected pattern and ID policy)

**Minimum Required Outcomes**
- T810A2 requirements reference `T810A-ADR-005` as the SSOT for the per-turn envelope/pattern.
- Any `aggregation_*_example.json` file(s) are aligned with the chosen MVP default; alternatives remain only if explicitly labeled as non-default.
- Any non-normative fields (e.g., `id`) are removed or explicitly de-scoped to avoid accidental “fixed key” drift.

#### B. T810A1-PROMPT (Requirements + Phase 2 Proposal S05)

**Targets**
- `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md` (update dependent F-RIDs; at minimum `T810A1-IG-007`)
- `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A1/proposal_T810A1-PROMPT_phase2.md` (modify Block 5 / `T810A1-S05` Tier 1 + Tier 2 tracking instructions)

**Minimum Required Outcomes**
- S05 Tier 1/Tier 2 tracking instructions reflect:
  - multi-entry per turn (1+ entries),
  - single codeblock output constraint,
  - selected MVP envelope/pattern,
  - “delta-only” rule (no cumulative regeneration).
- T810A1 requirements reference `T810A-ADR-005` and do not conflict with amended Epic `T810A-IG-004`.

---

### Subphase 2.5 — Publish Joint Handoff Brief (Single SSOT, Two Owner Checklists)

**Purpose**: Communicate the decision and the required actions to both feature owners without creating drift across separate handoffs.

**Recommendation**
- Publish **one** joint SSOT brief addressed to both `T810A1-PROMPT` and `T810A2-SCHEMA`, with two explicit owner sections (checklists).

**Target File (new)**
- `prompt/artifacts/tasks/T810/consultant/workspace/communication/consultant/handoff_brief_T810A-SYSTEM_dynamic-json-envelope-decision_to_T810A1-PROMPT_and_T810A2-SCHEMA_v1.0.0.md`

**Structural Requirement**
- Follow `handoff_brief_T810A2-SCHEMA_to_T810A1-PROMPT_phase2.md` structure (Executive Summary → Required Pre-Review → Decision Summary → Required Changes by Owner → Risks/Notes).

**Content Requirements**
- One-page decision summary (chosen pattern + rationale).
- “What changes where” checklists:
  - A1: S05 Tier 1/Tier 2 wording; F-RID updates; exemplar updates.
  - A2: request/proposal INT/IG updates; exemplar JSON adjustments; workflow instructions.
- Coordination rules to prevent drift (SSOT pointers and cross-references).

---

### Subphase 2.6 — Validation & Closure

**Validation Checklist**
- No remaining “exactly one object per message” language in governing specs where multi-entry is required.
- Schema template references use the renamed file names consistently.
- A1 + A2 documents reference the same DR ID as the authoritative decision.
- The decision preserves the Epic intent: **no cumulative regeneration**; per-turn output remains a delta.

**Completion Logging**
- Record the decision and cross-feature handoff in the relevant completion logs (Epic + feature) without duplicating normative text.

---

## VI. RISKS & MITIGATIONS (PRELIMINARY)

1. **Risk: Cross-feature drift** if A1 and A2 are updated asymmetrically.
   - Mitigation: single Epic DR + one joint handoff brief with explicit owner checklists.
2. **Risk: Overloading per-turn outputs** (token bloat) if multi-entry turns become large.
   - Mitigation: require “delta only” outputs; constrain entry verbosity; rely on `notes` field when needed.
3. **Risk: Chronology ambiguity** if timestamps are missing.
   - Mitigation: enforce timestamp format + allow `null` with probe; preserve array order semantics where applicable.

---

## VII. NEXT STEPS

1. Confirm decision criteria weights (Gate).
2. Execute Subphase 2.1 analysis and present scored comparison.
3. Draft and ratify `T810A-ADR-005`; amend Epic governance (`T810A-IG-004`, `T810A-GDR-002`) per `T102-STD-004` / `T102-STD-005`.
4. Implement A1 + A2 updates and publish the joint handoff brief.
