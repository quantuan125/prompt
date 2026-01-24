---
artifact_type: 'PROPOSAL'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A2'
feature_code: 'SCHEMA'
version: '1.0.0'
date: '2025-10-19'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_document: 'request_T810A2-SCHEMA.md'
target_section: 'Section III.M - Stories & Specification'
governance_guide: '../workspace_documentation_rules.md'
completion_log: '../../completion/T810A/T810A2/completion_T810A2-SCHEMA.md'
---

# PROPOSAL: T810A2-SCHEMA Phase 2 Stories & Examples

## I. EXECUTIVE SUMMARY

**Purpose**: This proposal captures the Phase 2 consultancy scope for `T810A2-SCHEMA`, focusing on Section III.M (Stories & Specification) of the Request. It introduces draft example artifacts (Activity 2.0) and outlines Story-level development for S01–S09.

**Scope**: Phase 2 of the T810A2-SCHEMA consultancy process per `plan_T810A2-SCHEMA_phase0-4.md`, limited to:
* Drafting structurally clean, minimal example artifacts (Activity 2.0).
* Preparing the ground for Story specifications S01–S09 (Activities 2.1–2.9).

**Key Deliverables in Phase 2**:
* Draft Stable JSON and Dynamic JSON example templates (`prompt/roles/gastro/data/*.yaml`).
* Draft controlled vocabulary examples, workflow guidance, and field classification mappings (`prompt/roles/gastro/data/*.md`).
* Story-level specification proposals for S01–S09 (to be developed after Activity 2.0).

**Consultation Approach**: Activity 2.0 provides "representative-but-serious" draft examples as a foundation for client review. Story sections then refine and complete requirements, using these drafts as a starting point rather than fixed specifications.

**Traceability Foundation**:
* Consultancy Plan: `plan_T810A2-SCHEMA_phase0-4.md` (Phase 2 section).
* Request: `request_T810A2-SCHEMA.md` (Section III.M Stories & Specification).
* Phase 1 Proposal: `proposal_T810A2-SCHEMA_phase1.md` (F-RIDs).

---

## II. CONTEXT & REFERENCES

### A. Governance & Document Roles

1. Plan (`plan_T810A2-SCHEMA_phase0-4.md`) — roadmap and activity definitions across phases 0–4.
2. Proposal (`proposal_T810A2-SCHEMA_phase2.md`) — Phase 2 normative consultancy artifact for Stories and examples.
3. Completion (`completion_T810A2-SCHEMA.md`) — non-normative execution log; will record Activity 2.0 and subsequent Story work.
4. Request (`request_T810A2-SCHEMA.md`) — single source of truth for feature requirements; Section III.M will be updated using this proposal.
5. SPS (`sps_T810-GASTRO.md`) - single source of truth for initiative and epic governances and requirements
6. Concept (`concept_T810-GASTRO.md`) - single source of truth for all architectural decisions and implementation frameworks

### B. Phase 2 Relationship to Phase 1

1. Phase 1 F-RIDs (ASSUM/DEP/NFR/IF/CON/IG/INT/NOTE/RES) remain the governance foundation for all Stories S01–S09.
2. Phase 2 examples and Stories MUST NOT duplicate F-RID bodies; they expand and operationalize them for Section III.M.
3. Activity 2.0 examples are guided by:
   * `T810A2-IG-002` (YAML Template Format),
   * `T810A2-IG-003` (Vocabulary Documentation Standard),
   * `T810A2-IG-004` (Manual Workflow Guidance),
   * `T810A2-IG-005` (Field Classification Pattern),
   * `T810A2-IG-006` (Schema Evolution Guidance),
   while allowing pragmatic deviations for clarity at draft stage.

---

## III. PHASE 2 ACTIVITIES OVERVIEW

### A. Activity List (Scope)

1. Activity 2.0 — Template Drafting & Deliverable Examples (draft artifacts).
2. Activity 2.1 — Story S01: Stable JSON (Patient Profile) Schema.
3. Activity 2.2 — Story S02: Dynamic JSON Schema (patient_state).
4. Activity 2.3 — Story S03: Dynamic JSON Schema (meal).
5. Activity 2.4 — Story S04: Dynamic JSON Schema (stool).
6. Activity 2.5 — Story S05: Dynamic JSON Schema (sleep).
7. Activity 2.6 — Story S06: Schema Evolution Governance.
8. Activity 2.7 — Story S07: Controlled Vocabularies Register.
9. Activity 2.8 — Story S08: Integration Patterns.
10. Activity 2.9 — Story S09: Validation & Quality Requirements.

### B. Phase 2 Completion Criteria (High Level)

1. Draft examples (Activity 2.0) created and reviewed with Client.
2. Stories S01–S09 specified in Section III.M of the Request with clear traceability to F-RIDs and Activity 2.0 artifacts.
3. Completion log updated with entries for Activity 2.0 and each Phase 2 Story.

---

## IV. ACTIVITY 2.0 — DRAFT TEMPLATES & EXAMPLES (FOUNDATION)

### A. Purpose & Posture

1. Provide concrete, structurally clean, minimal examples of Stable/Dynamic JSON entries, vocab formats, and patient workflows.
2. Enable the Client to react to how schemas and workflows may look in practice before committing to detailed Story-level requirements.
3. Serve as a foundation for S01–S08; examples are intentionally non-exhaustive and subject to refinement.

### B. Draft Artifact Set (`prompt/roles/gastro/data/`)

1. YAML Templates (Stable/Dynamic JSON)
   1. `template_stable_patient_schema.yaml` — Stable JSON patient profile draft example.
   2. `template_dynamic_meal_example.yaml` — Dynamic meal entry draft example.
   3. `template_dynamic_stool_example.yaml` — Dynamic stool entry draft example.
   4. `template_dynamic_digestion_example.yaml` — Dynamic digestion entry draft example.
   5. `template_dynamic_mental_example.yaml` — Dynamic mental state entry draft example.
   6. `template_dynamic_sleep_structure.yaml` — Sleep entry skeleton (structure only).
   7. `template_dynamic_medication_structure.yaml` — Medication entry skeleton (structure only).
   8. `template_dynamic_hydration_structure.yaml` — Hydration entry skeleton (structure only).
   9. `template_dynamic_tracking_schema.yaml` — Combined Dynamic SCHEMA block for required entry types (LLM-facing template).

2. Markdown Artifacts (Vocabularies, Workflow, Field Classification)
   1. `vocabulary_catalog_example.md` — Controlled vocabulary examples (Bristol scale, severity scales, metadata keys).
   2. `workflow_patient_instructions_example.md` — Patient instructions for Dynamic JSON export and compilation.
   3. `field_classification_mapping.md` — Draft mandatory/optional field mappings for REQUIRED entry types.

3. JSON Aggregation Pattern Examples
   1. `aggregation_mixed_array_example.json` — Example of single mixed chronological array of entries.
   2. `aggregation_per_type_arrays_example.json` — Example of separate arrays per entry type.
   3. `aggregation_hybrid_index_example.json` — Example hybrid structure with `entries` array and per-type index.

### C. Design Principles Applied

1. **Structural Minimalism** — Examples favor simple, clear structures over exhaustive detail to support Story-level refinement.
2. **Representative-But-Serious Content** — Values and fields are realistic enough for Client review while remaining sample data.
3. **Guided by IG/NFRs, Not Bound by Them** — IG and NFR items inform the examples (e.g., null-before-probe, annotation density) without requiring perfect compliance at draft stage.
4. **Core vs Non-Core Templates** — Core entry types (meal, stool, digestion, mental) include richer examples; non-core types (sleep, medication, hydration) are skeletal.

### D. Validation & Next Steps

1. Review the draft artifacts jointly with the Client to confirm they are a suitable starting point for detailed Story development.
2. Capture Activity 2.0 execution notes and decisions in `completion_T810A2-SCHEMA.md` (Phase 2, Activity 2.0 section).
3. Use agreed drafts as input when authoring Story proposals for S01–S08 in this Phase 2 proposal and in the Request Section III.M.

---

## V. STORY OUTLINES (S01–S09) — PLACEHOLDER

> NOTE: Detailed Story specifications will be developed after Activity 2.0 is approved. This section reserves structure for those future proposals.

### A. Story S01 — Stable JSON (Patient Profile) Schema

1. Purpose — Placeholder.
2. Functional Requirements — To be authored (T810A2-S01-FR-###).
3. Acceptance Criteria — To be authored (Gherkin).

### B. Story S02 — Dynamic JSON Schema (patient_state)

1. Purpose — Placeholder.
2. Functional Requirements — To be authored (T810A2-S02-FR-###).
3. Acceptance Criteria — To be authored (Gherkin).

### C. Story S03 — Dynamic JSON Schema (meal)

1. Purpose — Placeholder.
2. Functional Requirements — To be authored (T810A2-S03-FR-###).
3. Acceptance Criteria — To be authored (Gherkin).

### D. Story S04 — Dynamic JSON Schema (stool)

1. Purpose — Placeholder.
2. Functional Requirements — To be authored (T810A2-S04-FR-###).
3. Acceptance Criteria — To be authored (Gherkin).

### E. Story S05 — Dynamic JSON Schema (sleep)

1. Purpose — Placeholder.
2. Functional Requirements — To be authored (T810A2-S05-FR-###).
3. Acceptance Criteria — To be authored (Gherkin).

### F. Story S06 — Schema Evolution Governance

1. Purpose — Placeholder.
2. Functional Requirements — To be authored (T810A2-S06-FR-###).
3. Acceptance Criteria — To be authored (Gherkin).

### G. Story S07 — Controlled Vocabularies Register

1. Purpose — Placeholder.
2. Functional Requirements — To be authored (T810A2-S07-FR-###).
3. Acceptance Criteria — To be authored (Gherkin).

### H. Story S08 — Integration Patterns

1. Purpose — Placeholder.
2. Functional Requirements — To be authored (T810A2-S08-FR-###).
3. Acceptance Criteria — To be authored (Gherkin).

### I. Story S09 — Validation & Quality Requirements

1. Purpose — Placeholder.
2. Functional Requirements — To be authored (T810A2-S09-FR-###).
3. Acceptance Criteria — To be authored (Gherkin).

---

## VI. CLIENT REVIEW & APPROVAL GATE FOR ACTIVITY 2.0

1. Confirm that all Activity 2.0 draft artifacts listed in Section IV.B exist and are readable.
2. Validate that examples are structurally clear, minimal, and aligned with the desired Stable/Dynamic JSON architecture.
3. Provide feedback on any structural changes needed before Story development.
4. Upon approval, authorize transition to detailed Story specification work (Activities 2.1–2.9).
