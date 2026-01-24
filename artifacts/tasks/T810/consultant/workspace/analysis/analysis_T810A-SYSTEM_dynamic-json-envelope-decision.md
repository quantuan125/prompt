---
artifact_type: 'ANALYSIS'
initiative_id: 'T810'
epic_id: 'T810A'
feature_id: 'T810A'
feature_code: 'SYSTEM'
activity_id: '2.1'
version: '1.0.0'
date: '2025-12-15'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Comparative analysis of Dynamic JSON per-turn envelope patterns (A/B/C) to unblock T810A-ADR-005 and downstream A1/A2 updates'
---

# DECISION ANALYSIS: Dynamic JSON Per-Turn Envelope (Pattern A vs B vs C)

## I. EXECUTIVE SUMMARY

**Purpose**  
Select the MVP per-turn Dynamic JSON output envelope/pattern for `LLM_Gastro` tracking responses, in order to:  
1) enable **multi-entry** tracking within a single user message (e.g., multiple stool images + current symptoms),  
2) remove the legacy “exactly one object per message” constraint (Epic `T810A-IG-004` → Feature `T810A1-IG-007`), and  
3) establish an Epic-level decision (`T810A-ADR-005`) that downstream features (`T810A1-PROMPT`, `T810A2-SCHEMA`, future `T810A3-REPORTING`) can reference consistently.

**Scope**  
This analysis evaluates three JSON envelope patterns for **per-turn output** (the MVP governance priority):
- Pattern A: mixed chronological array
- Pattern B: per-type arrays under a top-level object
- Pattern C: hybrid entries array + type index

**Non-Negotiables (from QA)**
- Tracking output is emitted in **one fenced `json` codeblock** per LLM_Gastro response when tracking is required.
- A single patient message MAY yield **1+ entries** in that single codeblock (e.g., 4 stool + 1 digestion = 5).
- Per-turn output is a **delta only** (do not regenerate or restate prior entries as a cumulative log).
- IDs may be omitted; chronology relies on timestamp and ordering.
- No programmatic validation; schema adherence is governance/prompt-driven.

**Preliminary Finding (to be ratified by `T810A-ADR-005`)**
- Pattern A is the strongest MVP per-turn contract under the current constraints; Pattern B is attractive for *aggregated storage views* but is weaker as a per-turn delta format; Pattern C adds index maintenance complexity that conflicts with “no validation / low drift risk”.

---

## II. SOURCE MATERIAL SUMMARY

### A. Inputs Reviewed (Primary)

- Epic governance: `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md`
  - Includes `T810A-IG-004 (Tracking Payload Per-Turn Delta)` and `T810A-GDR-002 (Schema Split Architecture)`
- Epic ADR compendium: `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md`
  - ADR index structure per `T102-ADR-004` expectations; includes ADRs that constrain reporting and vocabulary governance
- T810A2 handoff brief: `prompt/artifacts/tasks/T810/consultant/workspace/communication/consultant/handoff_brief_T810A2-SCHEMA_to_T810A1-PROMPT_phase2.md`
  - Defines Patterns A/B/C and prior recommendation for Pattern A (MVP)
- T810A2 request: `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md`
  - Defines decision criteria baseline and `T810A2-INT-002 (Aggregation Format Integration)` assumptions
- T810A1 request: `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md`
  - Defines `T810A1-IG-007` “exactly one object per message” dependency
- T810A1 Phase 2 proposal (working spec): `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A1/proposal_T810A1-PROMPT_phase2.md`
  - Block 5 / `T810A1-S05` contains the “exactly one” instruction to be amended

### B. Aggregation Pattern Exemplars (Implementation-Proximate)

- Pattern A exemplar: `prompt/roles/gastro/data/aggregation_mixed_array_example.json`
- Pattern B exemplar: `prompt/roles/gastro/data/aggregation_per_type_arrays_example.json`
- Pattern C exemplar: `prompt/roles/gastro/data/aggregation_hybrid_index_example.json`

---

## III. DECISION CRITERIA & WEIGHTS (APPROVED IN QA)

Weights used for scoring (sum=1.00):
- Schema Clarity & Usability: 0.30
- Integration Consistency: 0.25
- Clinical Validity & Completeness: 0.20
- Token Optimization: 0.15
- User Experience Alignment: 0.10

Scoring scale:
- 5 = excellent
- 3 = acceptable / mixed trade-offs
- 1 = poor / high risk

---

## IV. OPTIONS (PER-TURN OUTPUT CONTRACTS)

### Option 0 — Status Quo / Do-Nothing

**Per-turn shape**: single JSON object per message.  
**Implication**: Multi-event turns require compression, omission, or mixing multiple events into one entry (high data-loss risk).

### Option A — Pattern A (Mixed Chronological Array)

**Per-turn shape**: JSON array of entry objects, ordered by occurrence (or by appearance in the message if timestamps are missing).  
**Delta-friendly**: Yes; the array can contain only the newly inferred entries for this turn.

### Option B — Pattern B (Per-Type Arrays Under a Container)

**Per-turn shape**: JSON object with arrays grouped by entry type (e.g., `stools`, `meals`, `digestion`).  
**Delta-friendly**: Mixed; either:
- emit only arrays that have new items (shape varies per turn), or
- emit all arrays each turn (empty arrays included) which increases tokens and complexity.

### Option C — Pattern C (Hybrid: Entries + Index)

**Per-turn shape**: JSON object with:
- `entries`: chronological array of entry objects, plus
- `index_by_type`: indices pointing into `entries` for each type.
**Delta-friendly**: Not in practice; indexes require correct maintenance rules (high drift risk without validation).

---

## V. COMPARATIVE ANALYSIS (SCORING)

### A. Raw Scores (1–5)

| Option | Schema Clarity & Usability (0.30) | Integration Consistency (0.25) | Clinical Validity & Completeness (0.20) | Token Optimization (0.15) | UX Alignment (0.10) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 0 — Status Quo | 4 | 3 | 1 | 5 | 2 |
| A — Pattern A | 5 | 5 | 5 | 4 | 4 |
| B — Pattern B | 3 | 3 | 5 | 2 | 5 |
| C — Pattern C | 2 | 4 | 4 | 1 | 3 |

### B. Weighted Totals

Weighted total = Σ(score × weight)

| Option | Weighted Total |
| :--- | ---: |
| 0 — Status Quo | 3.20 |
| A — Pattern A | 4.80 |
| B — Pattern B | 3.35 |
| C — Pattern C | 2.75 |

---

## VI. RECOMMENDATION (FOR `T810A-ADR-005`)

### A. Recommended MVP Choice

Adopt **Pattern A (mixed chronological array)** as the **per-turn tracking JSON envelope** (delta of 1+ entries inside one codeblock).

### B. Why Pattern A Wins Under MVP Constraints

- **Delta-first by construction**: emitting “only what’s new this turn” is natural (an array of just the new entries).
- **Lowest drift risk** with “no validation” and multi-entry turns (no indexes to maintain; no variable container semantics).
- **Works for both chronology and type needs**:
  - Chronology is native (timestamps + array order).
  - Type filtering is still trivial downstream (filter by `entry_type`) without changing the per-turn contract.
- **Token efficient** compared to Pattern B variants that require repeated keys or empty arrays per turn.

### C. Pattern B Disposition (not rejected as an idea, rejected as MVP per-turn contract)

Pattern B remains a strong candidate for **post-processing/derived views** (e.g., report export or backend storage layout), but it is weaker as the MVP **per-turn delta** contract because it introduces either:
- variable top-level structure per turn (if only some arrays are present), or
- repeated empty-array scaffolding (if all arrays must always appear).

---

## VII. IMPLICATIONS FOR GOVERNANCE & FEATURE SPECS

### A. Epic Governance Amendments Required

1. **Amend `T810A-IG-004 (Tracking Payload Per-Turn Delta)`**
   - Ensure Epic governance is explicit that the tracking payload is:
     - exactly one per-turn fenced `json` codeblock when tracking is required, and
     - a delta array of **1+ entry objects** (multi-entry turns allowed).
   - Explicitly prohibit cumulative regeneration (preserve original intent).
2. **Update `T810A-GDR-002 (Schema Split Architecture)`**
   - Add explicit adoption reference to `T810A-ADR-005`.
   - Remove/resolve legacy language that asserts “single-entry per interaction” as a mandatory constraint.

### B. T810A1-PROMPT Implications

- Update `T810A1-IG-007` and S05 prompt wording to:
  - allow multi-entry per message,
  - require a single codeblock,
  - align with Pattern A envelope,
  - preserve delta-only semantics.

### C. T810A2-SCHEMA Implications

- Update aggregation guidance and exemplars to:
  - treat Pattern A as the MVP per-turn envelope SSOT (per `T810A-ADR-005`),
  - clearly label Pattern B/C as alternative aggregate layouts (if retained),
  - remove or de-scope `id` fields from exemplars if they are not schema-governed output keys.

---

## VIII. GAP ANALYSIS & RISKS

### A. Gaps to Resolve in `T810A-ADR-005` Wording

1. **Chronology rule**: whether array order is normative when timestamps are equal/unknown.
2. **Multi-image stool policy**: “one stool entry per image” vs “one stool entry per stool event” when images represent separate times.
3. **Optional entry types**: whether additional entry types beyond the MVP set are allowed at runtime (and if so, where the constraint lives).

### B. Primary Risks

1. **Cross-feature drift risk**
   - If Epic governance and feature requirements are not amended together, “exactly one per message” will persist in at least one layer.
2. **Token bloat risk in multi-event turns**
   - Mitigate via delta-only rule + compact notes fields.
3. **Patient compilation ambiguity**
   - Mitigate by explicitly documenting the manual workflow: copy per-turn codeblocks → append arrays into a session file (later aggregated by `T810A3`).

---

## IX. APPENDIX

### A. Reference Correction Note (Schema Template Renames)

The following file renames are authoritative and MUST be reflected in all future references:
- `combined_dynamic_schema_mvp.yaml` → `prompt/roles/gastro/data/template_dynamic_tracking_schema.yaml`
- `patient.yaml` and/or `template_stable_json_example.yaml` → `prompt/roles/gastro/data/template_stable_patient_schema.yaml`

### B. Impact Matrix (High-Level)

| Scope | Owner | Artifact / File | Item | Impact Type | Required Change (per `T810A-ADR-005`) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Epic | Client / Epic consultant | `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md` | `T810A-IG-004` | Amend | Make “single codeblock + delta array + 1+ entries” explicit; keep “no cumulative regeneration” |
| Epic | Client / Epic consultant | `prompt/artifacts/tasks/T810/consultant/sps/sps_T810-GASTRO.md` | `T810A-GDR-002` | Amend | Adopt `T810A-ADR-005` and remove any residual single-entry phrasing conflicts |
| Epic | Client / Epic consultant | `prompt/artifacts/tasks/T810/consultant/concept/concept_T810-GASTRO.md` | `T810A-ADR-005` | Finalize | Status set to Accepted; keep Pattern A as SSOT per-turn envelope |
| Feature A1 | `T810A1-PROMPT` consultant | `prompt/artifacts/tasks/T810/consultant/request/request_T810A1-PROMPT.md` | `T810A1-IG-007` | Verify/Amend | Ensure “exactly one payload per turn” means one codeblock containing an array of 1+ entry objects (not one entry) |
| Feature A1 | `T810A1-PROMPT` consultant | `prompt/artifacts/tasks/T810/consultant/workspace/proposal/T810A/T810A1/proposal_T810A1-PROMPT_phase2.md` | `T810A1-S05` Tier 1/2 | Amend | Rewrite tracking instructions to Pattern A + multi-entry + single codeblock + delta-only |
| Feature A2 | `T810A2-SCHEMA` consultant | `prompt/artifacts/tasks/T810/consultant/request/request_T810A2-SCHEMA.md` | `T810A2-IF-002`, `T810A2-INT-002` | Amend | Treat Pattern A as per-turn output SSOT; treat Pattern B/C as non-default alternatives/derived views |
| Deliverables | `T810A2-SCHEMA` consultant | `prompt/roles/gastro/data/aggregation_mixed_array_example.json` | Pattern A exemplar | Verify | Ensure exemplar remains consistent with “array of entry objects” and schema-governed keys |
| Deliverables | `T810A2-SCHEMA` consultant | `prompt/roles/gastro/data/aggregation_per_type_arrays_example.json` | Pattern B exemplar | Amend | Remove non-normative fields (e.g., `id`); keep as explicitly non-default alternative |
| Deliverables | `T810A2-SCHEMA` consultant | `prompt/roles/gastro/data/aggregation_hybrid_index_example.json` | Pattern C exemplar | Amend | Keep as explicitly non-default alternative; avoid index drift cues; remove `id` if present |
