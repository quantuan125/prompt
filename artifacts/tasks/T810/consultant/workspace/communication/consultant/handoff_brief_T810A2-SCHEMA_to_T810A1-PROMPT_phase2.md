---
artifact_type: 'COMMUNICATION'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2'
feature_code: 'SCHEMA'
version: '1.0.0'
date: '2025-10-19'
status: 'draft'
author: 'LLM_Consultant (T810A2)'
decision_owner_role: 'Client'
target_consultant: 'LLM_Consultant (T810A1)'
source_epic: 'T810A-SYSTEM'
---

# HANDOFF BRIEF: T810A2-SCHEMA MVP SCHEMAs for T810A1-S05 Execution Protocol

## I. EXECUTIVE SUMMARY

This handoff brief communicates the **MVP Stable SCHEMA and Dynamic SCHEMAs** produced in `T810A2` Activity 2.0, together with candidate aggregation patterns, to the **T810A1-PROMPT** subconsultant. The goal is to unblock design and refinement of Story `T810A1‑S05 (Execution Protocol)` and related integration sections.

**Scope of this Brief**:
1. Summarize Stable SCHEMA MVP structure and location.
2. Summarize Dynamic SCHEMA MVP structures and the combined Dynamic SCHEMA block intended for LLM-facing use.
3. Present three alternative aggregation patterns for Dynamic data (JSON-level), with a recommended option and clear trade-offs.
4. Highlight key integration touchpoints and deltas that `T810A1‑S05` should account for (Probe triggering, Session Initialization, Conflict Resolution).

**Decision Ownership**: Final selection of aggregation pattern and any Block 4 / S05 wording changes remains with the Client and T810A1 consultant. T810A2 provides schema options and recommendations only.

---

## II. REQUIRED PRE-REVIEW FOR T810A1 CONSULTANT

Before applying this brief, the T810A1 subconsultant SHOULD review:

1. **T810A2 Request (SCHEMA)**  
   - `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md`  
   - Focus: Interfaces & Data (IF), Integration Notes (INT), Constraints (CON-004/005), and IG-001–006.

2. **T810A2 Phase 2 Proposal**  
   - `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A2/proposal_T810A2-SCHEMA_phase2.md`  
   - Focus: Section IV (Activity 2.0 – Draft Templates & Examples).

3. **Activity 2.0 Artifacts (`prompt/roles/gastro/data/`)**  
   - Stable SCHEMA example: `template_stable_patient_schema.yaml`.  
   - Dynamic SCHEMAs per entry type: `template_dynamic_*_example.yaml` and `template_dynamic_*_structure.yaml`.  
   - Combined Dynamic SCHEMA MVP: `template_dynamic_tracking_schema.yaml`.  
   - Vocabulary, workflow, and field classification drafts:  
     `vocabulary_catalog_example.md`, `workflow_patient_instructions_example.md`, `field_classification_mapping.md`.  
   - Aggregation examples:  
     `aggregation_mixed_array_example.json`,  
     `aggregation_per_type_arrays_example.json`,  
     `aggregation_hybrid_index_example.json`.

4. **T810A1 Request (PROMPT)**  
   - `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md`  
   - Focus: `T810A1-IF-005` (Session Context Injection), `T810A1-IF-006` (Dynamic JSON Generation), `T810A1-INT-004`/`INT-005`, and Story `T810A1‑S05` placeholders.

---

## III. STABLE SCHEMA MVP OVERVIEW

### A. Purpose & Role

1. Stable SCHEMA represents the **patient profile**: demographics, conditions, medications, triggers, relievers, allergies, and notes.
2. It is **patient-managed** and **read-only** for LLM_Gastro, consistent with `T810A2-CON-004` and `T810A1-INT-004`.
3. Runtime representation remains **JSON**; YAML is the authoring format.

### B. Draft Artifact

1. `template_stable_patient_schema.yaml` — structure:
   - `patient_profile.patient_id`, `age`, `sex`, `conditions`, `medications`, `triggers`, `relievers`, `allergies`, `notes`, `last_updated`.
2. This example is **structurally minimal** and representative, not exhaustive.

### C. Implications for T810A1-S05

1. In S05 Step 1 (“Context Loading”), Block 4 and IF-005 SHOULD:
   - Treat Stable SCHEMA as the authoritative profile loaded at session start.
   - State explicitly: conflicts between Memory and Stable SCHEMA are resolved in favor of Stable SCHEMA (per existing INT-005 and CON-004).
2. T810A1-S05 should reference Stable SCHEMA as **definition source** and avoid redefining its fields inline beyond what is needed for clarity.

---

## IV. DYNAMIC SCHEMA MVP OVERVIEW (PER ENTRY TYPE)

### A. Required Entry Types (MVP Core)

1. `meal` — `template_dynamic_meal_example.yaml`  
   - Fields: `entry_type`, `timestamp`, `items`, `ingredients`, `metadata`, `pre_meal_prokinetics`, `notes`.
2. `stool` — `template_dynamic_stool_example.yaml`  
   - Fields: `entry_type`, `timestamp`, `type` (Bristol), `metadata`, `confidence`, `notes`.
3. `digestion` — `template_dynamic_digestion_example.yaml`  
   - Fields: `entry_type`, `timestamp`, `tummy_pain`, `bloating`, `notes`.
4. `mental` — `template_dynamic_mental_example.yaml`  
   - Fields: `entry_type`, `timestamp`, `mood`, `stress`, `notes`.

These drafts map directly into the “Required Entry Types” described under `T810A1-IF-006`, while aligning with T810A2’s Constraints and IGs (fixed keys, null-before-probe, classification rules).

### B. Optional / Skeleton Entry Types (MVP Extended)

1. `sleep` — `template_dynamic_sleep_structure.yaml` (structure only).  
2. `medication_taken` — `template_dynamic_medication_structure.yaml` (structure only).  
3. `hydration` — `template_dynamic_hydration_structure.yaml` (structure only).

These skeletons support S05 wording around “other clinically relevant observations” without fully locking down all fields before T810A2 Stories S05/S06.

### C. Mandatory/Optional Field Classification

1. `field_classification_mapping.md` provides draft mandatory/optional tables for REQUIRED types (meal, stool, digestion, mental).
2. T810A1-S05 SHOULD:
   - Use these classifications to drive **Probe triggering logic** (missing mandatory → ask clarifying questions).
   - Treat optional fields as enrichment that should not block protocol progress.

---

## V. COMBINED DYNAMIC SCHEMA BLOCK (LLM-FACING TEMPLATE)

### A. Artifact and Structure

1. `template_dynamic_tracking_schema.yaml` — consolidated Dynamic SCHEMA block with top-level key:

```yaml
dynamic_schemas:
  meal: { ... }
  stool: { ... }
  digestion: { ... }
  mental: { ... }
```

2. Each subsection (`meal`, `stool`, etc.) mirrors the corresponding per-type YAML drafts, but presented in one place for **Block 4 / S05** usage.

### B. Intended Use

1. T810A1-S05 and Block 4 MAY:
   - Load this `dynamic_schemas` block as the **single SCHEMA reference** for Dynamic entries in Project Knowledge.
   - Reference per-type YAML files as design sources; treat `template_dynamic_tracking_schema.yaml` as the LLM-facing consolidation.
2. Automation to keep per-type YAML and combined YAML in sync is OUT OF SCOPE for this consultancy phase and may be implemented by LLM_Developer later.

---

## VI. AGGREGATION PATTERN OPTIONS (JSON LEVEL)

### A. Pattern A — Single Mixed Chronological Array (Recommended for MVP)

1. Artifact: `aggregation_mixed_array_example.json`

```json
[
  { "entry_type": "meal",   "...": "..." },
  { "entry_type": "stool",  "...": "..." },
  { "entry_type": "mental", "...": "..." }
]
```

2. Rationale:
   - Simple mental model for patient export and future T810A3 analysis.
   - Natural fit with “single entry per interaction” and chronological narrative.
3. T810A1-S05 impact:
   - S05 can describe appending each new entry to the array.
   - Chronology is inherent in array order.

### B. Pattern B — Separate Arrays per Entry Type

1. Artifact: `aggregation_per_type_arrays_example.json`

```json
{
  "meals": [...],
  "stools": [...],
  "mental_entries": [...]
}
```

2. Rationale:
   - Easier to inspect one type at a time (e.g., all meals).
3. T810A1-S05 impact:
   - S05 must specify which array to append to and how cross-array chronology is handled for reporting.

### C. Pattern C — Hybrid: Entries Array + Per-Type Index

1. Artifact: `aggregation_hybrid_index_example.json`

```json
{
  "entries": [ { ... }, { ... }, { ... } ],
  "index_by_type": {
    "meals": [0],
    "stools": [1],
    "mental_entries": [2]
  }
}
```

2. Rationale:
   - Preserves a simple chronological `entries` array.
   - Adds lightweight indices for type-specific views without duplicating data.
3. T810A1-S05 impact:
   - S05 must define how indices are updated when new entries are appended.

### D. Recommendation & Decision Ownership

1. T810A2 Recommendation: **Pattern A (single mixed chronological array)** for MVP due to:
   - Simplicity for patients and clinicians,
   - Minimal S05 complexity,
   - Direct alignment with “single entry per interaction” narrative.
2. Final decision: Deferred to Client + T810A1 consultant:
   - Choice affects S05 wording and potential T810A3 consumption patterns.
   - Once chosen, T810A2 integration notes can be updated to match the selected pattern.

---

## VII. KEY INTEGRATION TOUCHPOINTS & DELTAS FOR T810A1-S05

1. **Probe Triggering (T810A2-INT-001 + T810A1-NFR-005)**  
   - Use mandatory/optional field classifications from `field_classification_mapping.md` to define S05’s rules for when missing fields must trigger clarifying questions.

2. **Session Initialization (T810A2-INT-003 + T810A1-IF-005/INT-005)**  
   - S05 should state: Step 1 loads Stable SCHEMA (profile) + Dynamic SCHEMA skeletons (from `dynamic_schemas`) as context for the Tracking phase.

3. **Conflict Resolution (T810A2-INT-004 + T810A1-INT-005)**  
   - S05 should continue to treat Stable SCHEMA as authoritative when Memory conflicts, with wording aligned to the updated Stable SCHEMA structure.

4. **Fixed Keys vs. Flexible Schema (T810A2-CON-005 vs. earlier T810A1 assumptions)**  
   - Earlier T810A1 text allowed runtime addition of new keys.  
   - MVP constraint: Dynamic SCHEMA keys SHOULD be fixed; new keys are introduced via T810A2 governance (Story S06).  
   - S05 should avoid instructing LLM to invent new keys beyond the defined SCHEMAs.

5. **Controlled Vocabularies (T810A2-S07 + T810A1-ISSUE-004)**  
   - S05 should reference T810A2 vocab patterns and acknowledge that enforcement is prompt-based (no programmatic validation).

---

## VIII. NEXT STEPS & OPEN QUESTIONS

1. T810A1 consultant reviews this brief and selects a preferred aggregation pattern (A, B, or C) with Client input.
2. T810A1-S05 and Block 4 are updated to:
   - Reference Stable SCHEMA and Dynamic SCHEMAs by name and file/path where appropriate.
   - Describe execution steps consistent with the chosen aggregation pattern.
3. Feedback loop to T810A2:
   - Any constraints from S05 (token budgets, phase sequencing, or UX concerns) that require SCHEMA adjustments should be fed back into T810A2 Phase 2 Stories (S01–S09).

