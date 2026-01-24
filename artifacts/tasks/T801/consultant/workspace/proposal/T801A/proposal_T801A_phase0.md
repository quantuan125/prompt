---
artifact_type: 'PROPOSAL'
initiative_id: 'T801'
epic_id: 'T801A'
epic_code: 'TTI'
version: '1.1.0'
date: '2025-12-21'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
target_document: 'prompt/artifacts/tasks/T801/consultant/sps/sps_T801-TRADER.md'
target_section: 'III.C.0 + III.C.1 (Epic: T801A - TTI)'
---

# PHASE 0 PROPOSAL: SSOT Epic Dossier Patch — `T801A / TTI`

## I. EXECUTIVE SUMMARY

This Phase 0 proposal provides **SSOT-ready**, token-lean content to correct Epic `T801A (TTI)` and eliminate unrelated residue under `III.C.1`.

**Phase 0 rules**
- `III.C.1` MUST be compact and structurally correct.
- `III.C.1.v (Epic Requirements)` MUST remain placeholders only (Phase 1 will populate `QG/DEP/ASSUM/CON/IG`).
- `III.C.1.vi (Epic Research & Notes)` is out of scope for this patch (retain existing content unchanged).

---

## II. SSOT PATCH SCOPE

**Apply to SSOT**
1. `III.C.0 (Initiative WBS Map)` — ensure `T801A | TTI` is present (only change if drift exists).
2. `III.C.1 (Epic: T801A)` — replace:
   - Epic header + YAML block
   - Subsections `i–v`
   - Subsections `vii–ix`

**Do NOT change**
- `III.C.1.vi (Epic Research & Notes)` — retain as-is.

---

## III. ACCEPTANCE CRITERIA (PHASE 0)

- `III.C.1` contains no unrelated “Gastro” content and no `T810A-*` residue.
- `III.C.1` is minimal: short prose, short bullets, and a compact feature register.
- Feature Register lists `T801A1`–`T801A3` as `proposed` with `TBD` canonical Request links.
- `III.C.1.v (Epic Requirements)` remains placeholders only (no E-RID IDs in Phase 0).

---

## IV. SSOT-READY INSERT BLOCKS (COPY/PASTE)

### A. `III.C.0` — Initiative WBS Map (replace table only if drift exists)

| Level | PM Type | ID | Name |
| :--- | :--- | :--- | :--- |
| 1 | Initiative | T801 | TRADER |
| 2 | Epic | T801A | TTI |

---

### B. `III.C.1` — Epic `T801A` (replace header + YAML + subsections `i–v`)

#### 1. `T801A` Epic: `TTI` — Timeframe Trend Identification
<!-- PURPOSE: Epic dossier skeleton. Inherit global rules from Section III-B; add epic-specific scope, goals, and controls. -->

```yaml
epic_id: 'T801A'
epic_code: 'TTI'
epic_title: 'Timeframe Trend Identification'
epic_type: 'new'              # new | existing | general
epic_status: 'draft'          # draft | review | approved | deprecated
epic_owner: 'LLM_Consultant'  # Role or named owner
```

##### i. Purpose

This Epic establishes a deterministic foundation for timeframe trend identification so outputs are repeatable, timely, and suitable as stable input into higher-level trading workflows.

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

- This Epic inherits initiative-level assumptions, constraints, quality goals, and dependencies from `III.B` and should reference those items by ID when populated in Phase 1.

##### iv. Governance & Roadmap

**Scope & Ownership**
- Epic Owner: `LLM_Consultant`
- Decision Owner: `Client`
- Technical Authority (implementation): `LLM_Developer`

**Feature Register**
<!-- PURPOSE: The official list of work for this Epic. Each Feature is fully specified in its own Request artifact (the WBS dictionary). -->
| ID | Code | Name | Purpose | Owner | Status | Canonical Link (Request) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T801A1` | `BACKEND` | Backend TTI Engine | Deterministic classification + scoring + structured output generation (includes isolated validation environment) | `LLM_Developer` | `proposed` | TBD |
| `T801A2` | `PINE` | PineScript Enhancement | Improve upstream exported inputs needed for deterministic classification | `LLM_Developer` | `proposed` | TBD |
| `T801A3` | `INTEGRATION` | Trader/LLM Integration | Update operating workflow to consume the structured output artifact | `LLM_Developer` | `proposed` | TBD |

**Phase Sequence**
- Phase 0: SSOT dossier cleanup and minimal epic framing.
- Phase 1: Define Epic Requirements (QG/DEP/ASSUM/CON/IG) and record key governance and architecture decisions.
- Phase 2: Specify features via Request artifacts for `T801A1`–`T801A3`.
- Phase 3: Implement and validate in an isolated environment.
- Phase 4: Acceptance validation and cutover decision.

**Success Checkpoints**
- Checkpoint 1: Epic dossier is clean, minimal, and free of unrelated residue.
- Checkpoint 2: Epic Requirements + decisions approved by decision owner.
- Checkpoint 3: Feature Requests approved and implementation unblocked.

**References**
- `T801-RES-001`
- `T801A-RES-001`

##### v. Epic Requirements
<!-- Phase 0 MUST keep this section as placeholders only. -->

**Quality Goals**
- (Phase 1) TBD

**Dependencies**
- (Phase 1) TBD

**Assumptions**
- (Phase 1) TBD

**Constraints**
- (Phase 1) TBD

**Implementation Guidance**
- (Phase 1) TBD

---

### C. `III.C.1` — replace subsections `vii–ix`

##### vii. Epic Governance Decisions

| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|

##### viii. Epic Issues & Risks

**Issues**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

##### ix. Epic Changelog
<!-- Lightweight audit trail for material changes within this Epic. -->
