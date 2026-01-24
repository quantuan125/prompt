---
story_id: 'T102A-SPSST-S1'
story_status: 'draft'        # draft|review|approved|rework|deprecated
stability: 'soft_lock'       # soft_lock|frozen
ready_to_plan: false
scg: 'B'                     # A=Authoring skeleton, B=Governance & Ops
---

# design_T102A-SPSST-S1.md — YAML Frontmatter & Metadata

> Status: Living design log. Final decisions are canonized in Concept §III‑B.1.
> Scope: Story `T102A‑SPSST‑S1`.

---
## III. CORE CONTENT

### A. Context & Intent

This story standardizes a minimal YAML header across SPS/Request/Concept/Design artifacts and keeps approvals in the body, enabling predictable handoffs and simple parsing. It consolidates proposals (P1/P2), CS1/CS2 decisions, the final header, canonical examples, integration hooks, and ripple tests.

Ready‑to‑plan signal: Concept §III‑A.8 approval + Story Meta `story_status=approved` sets `ready_to_plan=true`.

### B. Proposals (P‑Bank)

#### 0. Option Comparison (story‑scoped, derived from Feature weights)
| Criterion | Wt | O1 (P1) | O2 (P2) |
| --------- | -- | ------- | ------- |
| Author Usability | 0.25 | 4 | 4 |
| Maintainability | 0.25 | 4 | 4 |
| Automation‑Ready | 0.15 | 4 | 5 |
| Consistency | 0.15 | 5 | 4 |
| Risk/Disruption | 0.10 | 4 | 3 |
| Time‑to‑Adopt | 0.10 | 4 | 3 |
| Weighted Total | 1.00 | 4.17 | 3.83 |

Notes: O1/O2 definitions and weights mirror Concept §III‑A (Feature). Story alignment: P1→O1; P2→O2.

#### 1. P1 — Minimal‑Change (legacy keys)

Intent: Keep structure familiar while cleaning approvals and normalizing IDs.

Structure: Legacy YAML (task_id/prefix_id), approvals in body.

Benefits / Trade‑offs / Risks: Low friction; legacy debt; inconsistent enums.

Disposition: Superseded (15/08/2025) — replaced by v1.0.0 header.

Example (archive):
```yaml
# Legacy example (superseded)
task_id: 'T102'
prefix_id: 'SPS-T102'
parent_task: 'T101'
task_type: 'system'
target: 'prompt/templates/consultant'
artifact_type: 'SPS'
version: '1.0.0'
date: '2025-08-14'
status: 'ready_for_review'
dependencies:
  - 'sps_structural_template.md'
  - 'request_structural_template.md'
author: 'LLM Consultant'
decision_owner_role: 'Client'
```

#### 2. P2 — Stronger Schema (pre‑CS1)

Intent: Add artifact_scope, richer enums, and schema for stricter automation.

Structure: Introduced `artifact_scope`, JSON Schema, expanded statuses.

Benefits / Trade‑offs / Risks: Automation gains; authoring overhead; drift from current flow.

Disposition: Superseded (16/08/2025) — simplified to v1.0.0 header.

Schema excerpt (archive):
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/header.schema.v1.json",
  "title": "Consultancy Header v1.0.0 (pre-CS1)",
  "type": "object",
  "additionalProperties": false,
  "required": ["artifact_type", "artifact_scope", "version", "date", "status", "author", "decision_owner_role"],
  "properties": {
    "artifact_type": { "enum": ["SPS", "REQUEST", "CONCEPT"] },
    "artifact_scope": { "enum": ["initiative", "feature", "story"] },
    "initiative_id": { "type": "string", "pattern": "^Td{3}$" },
    "epic_id": { "type": "string", "pattern": "^Td{3}[A-Z]$" },
    "feature_id": { "type": "string", "pattern": "^Td{3}[A-Z]-[A-Z0-9_]+$" },
    "story_id": { "type": "string", "pattern": "^Td{3}[A-Z]-[A-Z0-9_]+-Sd+$" },
    "version": { "type": "string", "pattern": "^d+.d+.d+(-[0-9A-Za-z.-]+)?$" },
    "date": { "type": "string", "pattern": "^d{4}-d{2}-d{2}$" },
    "status": { "enum": ["draft", "in_review", "ready_for_review", "approved", "rework", "deprecated"] },
    "author": { "type": "string", "minLength": 3, "maxLength": 60 },
    "decision_owner_role": { "enum": ["Client", "Product Owner", "Architect"] },
    "dependencies": { "type": "array", "items": { "type": "string", "pattern": "^[A-Za-z0-9_./-]+.md$" } }
  }
}
```

Field Reference

| Key                   | Type   | Required | Scope        | Allowed / Pattern / Notes |
| --------------------- | ------ | -------- | ------------ | ------------------------- |
| `artifact_type`       | enum   | Yes      | all          | `SPS` | `REQUEST` | `CONCEPT` | `DESIGN` |
| `initiative_id`       | string | Yes      | all          | `^Td{3}$` (e.g., `T102`) |
| `epic_id`             | string | Req*     | feature docs | `^Td{3}[A-Z]$` (e.g., `T102A`) |
| `feature_id`          | string | Req*     | feature docs | `^Td{3}[A-Z]-[A-Z0-9_]+$` (e.g., `T102A-SPSST`) |
| `story_id`            | string | Req*     | story docs   | `^Td{3}[A-Z]-[A-Z0-9_]+-Sd+$` (e.g., `T102A-SPSST-S1`) |
| `version`             | string | Yes      | all          | SemVer `^d+.d+.d+(-[0-9A-Za-z.-]+)?$` |
| `date`                | string | Yes      | all          | ISO‑8601 `YYYY-MM-DD` |
| `status`              | enum   | Yes      | all          | `draft` | `review` | `approved` | `rework` | `deprecated` |
| `author`              | enum   | Yes      | all          | `LLM_Consultant` | `LLM_Planner` | `LLM_Developer` | `LLM_Reviewer` |
| `decision_owner_role` | enum   | Yes      | all          | `Client` |
| `dependencies`        | array  | No       | all          | relative `*.md` paths only |

Required by scope: feature docs require `epic_id` & `feature_id`; story docs require `story_id`.

Canonical Examples

SPS (initiative)
```yaml
artifact_type: 'SPS'
initiative_id: 'T102'
version: '1.0.0'
date: '2025-08-16'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
dependencies:
  - 'sps_structural_template.md'
  - 'request_structural_template.md'
```

REQUEST (feature)
```yaml
artifact_type: 'REQUEST'
initiative_id: 'T102'
epic_id: 'T102A'
feature_id: 'T102A-SPSST'
version: '1.0.0'
date: '2025-08-16'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
dependencies:
  - 'sps_T102-CONSULTANT.md'
```

CONCEPT (feature; S1 exemplar)
```yaml
artifact_type: 'CONCEPT'
initiative_id: 'T102'
epic_id: 'T102A'
feature_id: 'T102A-SPSST'
version: '1.0.0'
date: '2025-08-16'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
dependencies:
  - 'request_T102A-SPSST_T102_v1.0.0.md'
```

DESIGN (story; S1 exemplar)
```yaml
artifact_type: 'DESIGN'
initiative_id: 'T102'
epic_id: 'T102A'
feature_id: 'T102A-SPSST'
story_id: 'T102A-SPSST-S1'
version: '1.0.0'
date: '2025-08-16'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
dependencies:
  - 'request_T102A-SPSST_T102_v1.0.0.md'
  - 'concept_T102A-SPSST_T102_v1.0.0.md'
```

Body‑level approval signals (Integration Note)

- SPS: `**Approved Epics:** [T102A, T102B]`
- Request: `**Approved Features:** [T102A-SPSST]`
- Concept: `**Approved Stories:** [T102A-SPSST-S1]`

Standard vs Artifact

- Standard docs (e.g., `prompt_main.md`, `sps_structural_template.md`) keep body metadata.
- Artifact docs (SPS, REQUEST, CONCEPT, DESIGN) use the YAML header above.

### C. Decision Log Entries (chronological)

#### 1. Entry 1 — 15/08/2025 — CS1: Header Scope & Enums
*Summary: Establish minimal, stable cross‑artifact header and keep approvals in body.*

* **Title:** CS1 — Minimal Cross‑Artifact Header
* **Context:** Early drafts diverged on header scope, enums, and approval placement. Automation was a future concern; authoring friction needed to stay low.
* **Decision:** Remove `artifact_scope`; limit `status` enum to `draft|review|approved|rework|deprecated`; set `decision_owner_role='Client'`; restrict `author` to role labels; keep `initiative_id` across all artifacts; approvals remain in body.
* **Consequences:**
  - (+) Stable, lightweight parsing surface; easier authoring.
  - (+) Clear ownership of approvals by artifact body; human‑readable.
  - (−) Validators must read body for approvals.
* **Alternatives Considered:** Include `artifact_scope`; encode approvals in YAML; wider role sets.
* **References:** `T102A-SPSST-S1-FR-01..03`; `T102C` Concept §III.B.1.

#### 2. Entry 2 — 16/08/2025 — CS2: Standard vs Artifact Split
*Summary: Confirm split where standards retain body metadata and artifacts carry YAML header.*

* **Title:** CS2 — Confirm Standard/Artifact Split
* **Context:** Need to avoid drift and keep standards readable while ensuring artifacts are machine‑addressable.
* **Decision:** Standard docs (templates, general docs) retain body metadata; artifacts (SPS/REQUEST/CONCEPT/DESIGN) must include the v1.0.0 YAML header.
* **Consequences:**
  - (+) Clear separation of concerns; easier change control.
  - (+) Artifacts are consistently machine‑readable.
  - (±) Requires discipline to avoid accidental header in standards.
* **Alternatives Considered:** Single policy for all docs; extended headers.
* **References:** Concept §III‑A.7 Recommendation; §III‑B.1 Decision Record.

---

### D. Decision Record (Frozen Summary)
#### 1. Decision Record
**Decision Record**
* **Title:** S1 header v1.0.0 — simplified cross-artifact schema & body approvals
* **Context:** Earlier drafts proposed wider key sets and YAML approvals. See **Design record** `design_T102A-SPSST-S1.md` (contains prior P1/P2 and `header.schema.v1`).
* **Decision:** Adopt the v1.0.0 header per Design record §2 and keep approval lists in **body**.
* **Consequences:** 
  - (+) Consistent, minimal parsing across artifacts; 
  - (+) clear human-visible approvals; 
  - (−) body scan needed for approvals.
* **Alternatives considered:** 
  - (a) YAML approvals; 
  - (b) legacy keys; 
  - (c) extension keys in header.
* **References:** Request `E.1` S1 FRs; NFRs; IF/CON; design record §2.


#### 2. Final Proposed Solution
```yaml
artifact_type: 'SPS'
initiative_id: 'T102'
version: '1.0.0'
date: '2025-08-16'
status: 'review'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
dependencies:
  - 'sps_structural_template.md'
  - 'request_structural_template.md'
```

### E. Integration, Dependency & Tracibility

#### 1. Integration Notes (with NFRs, Constraints, Interfaces)

- T102A-SPSST-INT-S1-01 (Body Approvals)
- T102A-SPSST-INT-S1-02 (Canonical Header Usage)
- T102A-SPSST-INT-S1-03 (Role‑based Author Field)
- T102A-SPSST-IF-01 (Data Extraction)
- T102A-SPSST-CON-01 (Scope Discipline)
- T102A-SPSST-NFR-01 (Tool Parsing)
- T102A-SPSST-NFR-02 (Author Usability)
- T102A-SPSST-NFR-03 (Stable IDs)
- T102A-SPSST-NFR-04 (Instructional Pattern)

**Inherited Considerations**
| Source Artifact | Source ID | Category | Inherited Rule IDs |
| :-------------- | :-------- | :------- | :----------------- |
| SPS            | T102      | Constraints | `T102-CON-01 (Format Requirements)`, `T102-CON-02 (Scope Limitation)`, `T102-CON-03 (Documentation Standards)` |
| SPS            | T102      | Dependencies | `T102-DEP-01 (Client SLA)`, `T102-DEP-02 (Planner Integration)` |
| SPS            | T102      | Implementation Guides | `T102-IG-05 (Canonical Header)`, `T102-IG-07 (ID Standard)`, `T102-IG-10 (Inheritance Model)` |
| SPS            | T102A     | Quality Goals | `T102A-QG-02 (Traceability)` |
| SPS            | T102A     | Dependencies | `T102A-DEP-02 (Request Intake Alignment)` |

#### 2. Story‑local Dependency

| From (FR)                 | Depends On (FR)           | Rationale |
| ------------------------- | ------------------------- | --------- |
| T102A-SPSST-S1-FR-02      | T102A-SPSST-S1-FR-01      | Formats depend on key set definition. |
| T102A-SPSST-S1-FR-03      | T102A-SPSST-S1-FR-01..02  | Examples must reflect allowed keys/enums. |

* `design_T102A-SPSST-S1.md` (design record: P1/P2 archive, CS1/CS2, final header, ripple tests)
* Generator mapping reference (hand-off; S8)
* C4 diagram assets (Context/Container) *if/when exported*

#### 3. Tracibility Matrix (Story FRs only)

| ID                   | Title / Description                                 | Status  | Evidence / Location                                   | Notes                     |
| :------------------- | :-------------------------------------------------- | :------ | :---------------------------------------------------- | :------------------------ |
| T102A-SPSST-S1-FR-01 | Header presence & core keys (allowed set only)      | Met     | `design_T102A-SPSST-S1.md §2.2` (canonical examples)  | —                         |
| T102A-SPSST-S1-FR-02 | Key formats & enums                                 | Met     | `design_T102A-SPSST-S1.md §2.1` (field reference)     | —                         |
| T102A-SPSST-S1-FR-03 | Canonical examples & reference                      | Met     | `design_T102A-SPSST-S1.md §2.2`                       | —                         |
| T102A-SPSST-NFR-01   | Parsable by common Markdown/YAML tooling            | Met     | Simple YAML subset; no custom types                   | —                         |
| T102A-SPSST-NFR-02   | Section names/order intuitive (non-technical users) | Partial | S1 header clarity ✓; broader doc UX covered by S2–S7  | S1 impacts only header UX |
| T102A-SPSST-NFR-03   | Non-sequential IDs (slug/UUID-friendly)             | Met     | Patterns for epic/feature/story IDs                   | —                         |
| T102A_SPSST_IF-01  | Downstream can read IDs from header; approvals body | Met     | Header examples + body approvals (Integration Note 1) | —                         |
| T102A_SPSST_CON-01 | SPS avoids metrics/ACs                              | Met     | Header contains no metrics/ACs                        | —                    

---

### F. Ripple Test Notes

* Header fields parse: verify presence & format per Field Reference (no strict tooling in v1).
* Body approvals present: SPS/Request/Concept carry the approval line.
* Downstream read: generator/planner reads IDs from header; approvals from body.

---

### IX. CHANGELOG
**2025-09-13** — Restructured S1 using S3‑style design log; added story YAML meta; added Option Comparison; split CS1/CS2 decisions with dates; expanded canonical examples to include DESIGN; added Integration & Tracibility with NFR/CON/IF bullets and Inherited Considerations; preserved Ripple Tests.
