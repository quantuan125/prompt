---
artifact_type: 'PROPOSAL'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC004'
task_id: 'P-PH000-ST001-AC004-TK002.2'
gate_id: 'P-PH000-ST001-AC004-GATE-002'
version: '1.2.0'
date: '2026-03-01'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
analysis_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/analysis/analysis_P-PH000-ST001-AC004_p-std-004-proposal-seeding-assessment.md'
verification_reference: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-002.md'
purpose: 'GATE-002 GIR disposition package — recommended resolutions + rationale for all GIR items from TK002, to enable client decision and unblock downstream implementation.'
consumers:
  - 'P-PH000-ST001-AC004-GATE-002'
  - 'P-PH000-ST001-AC004-TK003'
  - 'P-PH000-ST001-AC004-TK003.1'
  - 'P-PH000-ST001-AC004-TK003.3'
  - 'P-PH000-ST001-AC004-TK003.4'
---

# PROPOSAL: GATE-002 GIR Disposition Package — P-PH000-ST001-AC004

> **Purpose**: Provide a decision-ready disposition package for all TK002 GIR items (GIR-001…GIR-011). Each GIR is presented with clear options, a consultant recommendation, and a Client decision checkbox. The completed decisions in this proposal are the binding inputs for GATE-002 disposition and for downstream execution (primarily TK003 and T104-PH001-ST007).

---

## I. EXECUTIVE SUMMARY

**Context**: TK002 produced 11 GIR items against P-STD-004 (draft). TK002.1 verified the analysis is decision-ready for GATE-002.

**Goal at GATE-002**: The Client records dispositions for each GIR:
- **Resolve now** (authorize implementation in the specified target task),
- **Accept** (explicitly accept the issue/risk as-is),
- **Defer** (explicitly defer with owner + trigger).

**Authority note**: The GATE-002 decision is recorded in the GDR inside `verification_P-PH000-ST001-AC004_gate-002.md`. This proposal is the **authoritative detailed record** of per-GIR dispositions; the GDR should reference this file as its `Decision Reference`.

---

## II. DISPOSITION SUMMARY (GIR-001…GIR-011)

| GIR ID | Type | Severity | Recommended Disposition | Execution Target | Blocking for TK003? | Client Decision |
|:--|:--|:--|:--|:--|:--|:--|
| GIR-001 | Gap | Minor | Resolve | AC004-TK003 | Yes | (a) APPROVED (2026-03-01) |
| GIR-002 | Gap | Minor | Resolve | AC004-TK003 | Yes | (a) APPROVED (2026-03-01) |
| GIR-003 | Gap | Minor | Resolve | AC004-TK003 | Yes | (a) APPROVED (2026-03-01) |
| GIR-004 | Gap | Minor | Resolve | AC004-TK003 | Yes | (a) APPROVED (2026-03-01) |
| GIR-005 | Issue | Minor | Resolve | AC004-TK003 | Yes | (a) APPROVED (2026-03-01) |
| GIR-006 | Issue | Major | Resolve (policy change) | AC004-TK003.4 | Yes | (b) APPROVED (2026-03-01) |
| GIR-007 | Risk | Minor | Accept | GATE-002 disposition only | No | (a) APPROVED (2026-03-01) |
| GIR-008 | Gap | Major | Resolve | AC004-TK003 | Yes | (a) APPROVED (2026-03-01) |
| GIR-009 | Issue | Minor | Resolve | AC004-TK003 | Yes | (a) APPROVED (2026-03-01) |
| GIR-010 | Issue | Minor | New follow-on task | AC004-TK003.1 | No | (b) APPROVED (2026-03-01) |
| GIR-011 | Issue | Major | Defer (rename/enforcement) | AC004-TK003.3 (exec: T104-PH001-ST007) | No | (b) APPROVED (2026-03-01) |

---

## III. GIR DISPOSITION REGISTER (DETAILED)

### GIR-001 — Canonical Root Directories Restriction (New Initiative Roots)

**Context**: TK002 found that the “MUST include” root directory list does not explicitly restrict additional non-canonical roots for *new* initiatives.

**Decision prompt**: How should we disposition GIR-001?

| Option | Description |
|:--|:--|
| **(a) Resolve in TK003 (Recommended)** | Amend P-STD-004 to state new initiative roots SHOULD be limited to the canonical set; grandfathering applies only to legacy initiatives. |
| (b) Accept | Accept potential drift in initiative root directories. |
| (c) Defer | Defer restriction until future cross-initiative validation or tooling. |

**Recommendation**: (a)

**Rationale**: Prevents root-level drift while preserving SES002 grandfathering posture for legacy initiatives.

**Implementation note**: Execute as P-STD-004 CLAUSE amendment in `P-PH000-ST001-AC004-TK003` (target: `P-STD-004-CLAUSE-001A` add new subclause `CLAUSE-001D`).

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-002 — Legacy Role-Scoped Root Deprecation Coverage

**Context**: TK002 found that P-STD-004 deprecates “Legacy standards directories” but does not explicitly cover broader legacy role-scoped roots (e.g., `consultant/`, `planner/`) as a category.

**Decision prompt**: How should we disposition GIR-002?

| Option | Description |
|:--|:--|
| **(a) Resolve in TK003 (Recommended)** | Amend `P-STD-004-CLAUSE-002D` to cover all legacy role-scoped root directories, not only standards directories. |
| (b) Accept | Keep deprecation language narrowly scoped; tolerate ambiguity for other role-scoped roots. |
| (c) Defer | Defer to a later standardization effort once all legacy role roots are inventoried. |

**Recommendation**: (a)

**Rationale**: Makes deprecation policy explicit, reducing future “where should this live?” ambiguity for new work.

**Implementation note**: Execute as P-STD-004 CLAUSE amendment in `P-PH000-ST001-AC004-TK003`.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-003 — Define `<scope-UID>` in Proposal/Analysis/Comm Naming Patterns

**Context**: TK002 found that `<context>` in `proposal_` / `analysis_` / `comm_` naming patterns is undefined and used inconsistently (activity UID vs stream UID vs scope descriptor).

**Decision prompt**: How should we disposition GIR-003?

| Option | Description |
|:--|:--|
| **(a) Resolve in TK003 (Recommended)** | Rename `<context>` → `<scope-UID>` in the prefix registry and add a defining subclause clarifying `<scope-UID>` as a timeline UID or scope ID per `P-STD-005-CLAUSE-001`. |
| (b) Accept | Keep `<context>` informal and flexible, accepting naming variability. |
| (c) Defer | Defer until `guideline_workspace_proposal.md` is authored. |

**Recommendation**: (a)

**Rationale**: “Scope-UID” makes the intent explicit and toolable without requiring new artifact types or path changes.

**Implementation note**: Execute as P-STD-004 CLAUSE amendment in `P-PH000-ST001-AC004-TK003` (target: `P-STD-004-CLAUSE-008A` plus new `CLAUSE-008H` definition).

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-004 — `dev-report_` Naming Reference Treatment

**Context**: TK002 found that `dev-report_` is the only timeline-derived artifact type in the P-STD-004 prefix registry that is not cross-referenced to `P-STD-005-CLAUSE-011`.

**Decision prompt**: How should we disposition GIR-004?

| Option | Description |
|:--|:--|
| **(a) Resolve in TK003 (Recommended)** | Amend `P-STD-004-CLAUSE-008A` to allow both patterns: legacy `dev-report_<activity-UID>_<date>.md` and preferred `dev-report_<activity-UID>_<kebab-topic>_<date>.md`; add an informative note clarifying schema governance and timeline naming exception treatment. |
| (b) Accept | Leave as-is; rely on developer practice and existing dev-report guideline references. |
| (c) Defer | Defer any clarification until `guideline_workspace_dev-report.md` is finalized. |

**Recommendation**: (a)

**Rationale**: The existing prefix registry pattern is not sufficient in practice: multiple dev-reports already use a topic qualifier for navigability. Allowing both patterns prevents forced renames while providing a preferred, more searchable convention going forward.

**Implementation note**: Execute as a P-STD-004 CLAUSE amendment in `P-PH000-ST001-AC004-TK003` by updating the `dev-report_` row in `P-STD-004-CLAUSE-008A` to include the variant pattern (no migration required because both remain valid).

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-005 — P-STD-004 Provenance Status Text Is Stale

**Context**: TK002 found that P-STD-004 Provenance §Status still references “pending GATE-001 review” even though GATE-001 passed on 2026-02-27.

**Decision prompt**: How should we disposition GIR-005?

| Option | Description |
|:--|:--|
| **(a) Resolve in TK003 (Recommended)** | Update Provenance §Status text to reflect GATE-001 passed and GATE-002 pending. |
| (b) Accept | Leave stale status text. |
| (c) Defer | Defer until post-GATE-002 amendments are applied. |

**Recommendation**: (a)

**Rationale**: Maintains audit clarity and avoids misleading lifecycle status narratives.

**Implementation note**: Execute as a maintenance fix in `P-PH000-ST001-AC004-TK003`.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-006 — Placement Policy: Activity-Level `analysis/` / `proposal/` Allowed with `<scope-UID>` Match

**Context**: GATE-002 introduces a new Client requirement: `analysis/` and `proposal/` artifacts MAY be stored at activity level (and stream level) as long as directory placement matches the `<scope-UID>` used in the filename. This supersedes the prior “stream-only” restriction and reframes the prior inventory as a **policy alignment** task rather than a migration violation set.

**Decision prompt**: How should we disposition GIR-006?

| Option | Description |
|:--|:--|
| (a) Keep stream-only + migrate | Keep stream-only as the normative rule; migrate any activity-level instances to stream-level. |
| **(b) Allow both + enforce `<scope-UID>` placement match (Recommended)** | Amend P-STD-004 to allow activity-level `analysis/`/`proposal/` and require deterministic placement that matches `<scope-UID>` in the filename. |
| (c) Allow both without enforcement | Allow both placements without a normative scope-alignment rule. |

**Recommendation**: (b)

**Rationale**: Supports multiple activity-scoped analysis subtypes and per-gate proposals while keeping placement deterministic and enforceable.

**Implementation note**: Execute as a P-STD-004 CLAUSE amendment via `P-PH000-ST001-AC004-TK003` (tracked explicitly as `P-PH000-ST001-AC004-TK003.4`).

**Client Decision**: `[ ] (a)` / `[x] (b)` / `[ ] (c)` / `[ ] Override: _______________`  
**Decision date**: 2026-03-01

---

### GIR-007 — Provisional `communication/` Type Subdir + `comm_` Prefix

**Context**: TK002 states the `communication/` type subdir and `comm_` prefix are provisional with full specification deferred to T104G; risk is inconsistent use until that work completes.

**Decision prompt**: How should we disposition GIR-007?

| Option | Description |
|:--|:--|
| **(a) Accept (Recommended)** | Accept the deferral risk as intentional and proceed with provisional status. |
| (b) Resolve now | Attempt to fully specify `communication/` and `comm_` immediately in P-STD-004. |
| (c) Defer decision | Avoid disposition until T104G scope is scheduled. |

**Recommendation**: (a)

**Rationale**: Matches the deliberate deferral strategy already documented; avoids scope expansion inside AC004.

**Implementation note**: No TK003 action required; record as accepted risk at GATE-002.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-008 — Archive Mirrored Structure vs Flat Two-Tier Model

**Context**: TK002 recommends replacing a mirrored archive structure with a flat two-tier archive model: `archive/versioned/` and `archive/deprecated/`.

**Decision prompt**: How should we disposition GIR-008?

| Option | Description |
|:--|:--|
| **(a) Resolve in TK003 (Recommended)** | Amend `P-STD-004-CLAUSE-009` to replace mirrored archive structure with the two-tier model. |
| (b) Accept | Keep mirrored structure. |
| (c) Defer | Defer archive restructuring until after cross-initiative migration evidence is reviewed. |

**Recommendation**: (a)

**Rationale**: Reduces structural coupling and maintenance burden while remaining navigable and toolable with UID-based filenames.

**Implementation note**: Execute as P-STD-004 CLAUSE amendment in `P-PH000-ST001-AC004-TK003` (targets: `P-STD-004-CLAUSE-009A`…`009G`).

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-009 — Fragile Subclause Cross-References in Prefix Registry

**Context**: TK002 found the prefix registry references multiple `P-STD-005-CLAUSE-011*` subclauses. This is fragile if P-STD-005-CLAUSE-011 is later restructured.

**Decision prompt**: How should we disposition GIR-009?

| Option | Description |
|:--|:--|
| **(a) Resolve in TK003 (Recommended)** | Update P-STD-004 to reference `P-STD-005-CLAUSE-011` at the main-CLAUSE level and use any subclause pointers as informative notes only. |
| (b) Accept | Keep subclause-level references. |
| (c) Defer | Defer until P-STD-005 stabilization is complete. |

**Recommendation**: (a)

**Rationale**: Improves reference resilience while preserving the intent of tying naming patterns to timeline file naming guidance.

**Implementation note**: Execute as P-STD-004 CLAUSE amendment in `P-PH000-ST001-AC004-TK003`.

**Client Decision**: `[x] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-010 — Formal Reference vs Subclause Reference Clarification (P-STD-005)

**Context**: TK002 identifies ambiguity: the formal cross-scope reference format does not explicitly prohibit treating subclause IDs as full-formal references, which may lead to inconsistent authoring.

**Decision prompt**: How should we disposition GIR-010?

| Option | Description |
|:--|:--|
| (a) Bundle into AC004-TK003 | Amend both P-STD-004 and P-STD-005 in the same changeset under TK003. |
| **(b) Create follow-on task (Recommended)** | Keep TK003 scoped to P-STD-004; create a new AC004 task to amend P-STD-005-CLAUSE-004 with an explicit clarification. |
| (c) Defer | Defer to a later standardization/migration effort. |

**Recommendation**: (b)

**Rationale**: Avoids expanding TK003 scope beyond the P-STD-004 deliverable contract while still ensuring the ambiguity is resolved in the authoritative ID standard (P-STD-005).

**Implementation note**: Execute as `P-PH000-ST001-AC004-TK003.1` targeting `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`.

**Client Decision**: `[ ] (a)` / `[x] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

### GIR-011 — Verification File Naming Non-Conformance (`-GATE-###` vs `_gate-###`)

**Context**: TK002 found multiple verification files using `-GATE-###` (hyphen + uppercase token) which conflicts with the `verification_<Activity-UID>_gate-###.md` pattern (underscore + lowercase) in P-STD-005 timeline file naming.

**Decision prompt**: How should we disposition GIR-011?

| Option | Description |
|:--|:--|
| (a) Resolve now in TK003 | Rename all non-conformant verification files immediately as part of AC004. |
| **(b) Defer to T104-PH001-ST007 (Recommended)** | Treat as migration/enforcement work: rename in a coordinated changeset, update scripts/validators, and enforce forward. |
| (c) Accept | Accept inconsistent naming as permanent. |

**Recommendation**: (b)

**Rationale**: Renames are cross-cutting and should be executed with coordinated tooling/script updates to avoid breakage and partial migrations.

**Implementation note**: Execute under `T104-PH001-ST007` as a coordinated second-pass migration/enforcement change, tracked via `P-PH000-ST001-AC004-TK003.3` (rename inventory + mapping + enforcement requirements). This is required for: (1) secondary-vision cleanup for `P/**` and `T104/**`, and (2) first-iteration migration conformance for `T102/**` (enforce `_gate-###` from start).

**Rename inventory (current non-conformant examples)**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/verification/verification_P-PH000-ST001-AC002_gate-002_tk005-supplement.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004_gate-002_post-migration-quality.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004_gate-001_p-migration-readiness.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004_gate-001_convention-compliance.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST007/AC004/verification/verification_T104-PH001-ST007-AC004_gate-001_commissioning-readiness.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC001/verification/verification_P-PH000-ST004-AC001_gate-002_report-acceptance_P-RES-001.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC002/verification/verification_P-PH000-ST004-AC002_gate-002_report-acceptance_iteration-2.md`
- `prompt/artifacts/tasks/T104/workspace/PH001/ST005/AC002/verification/verification_P-PH000-ST004-AC002_gate-002_report-acceptance.md`

**Client Decision**: `[ ] (a)` / `[x] (b)` / `[ ] (c)` / `[ ] Override: _______________`  
**Decision date**: 2026-03-01

---

## IV. DOWNSTREAM EXECUTION MAPPING

### A. TK003 — P-STD-004 Amendments (If Approved at GATE-002)

If the Client selects “Resolve in TK003” for the GIRs below, TK003 MUST implement them in a single deterministic changeset to P-STD-004:
- GIR-001, GIR-002, GIR-003, GIR-004, GIR-005, GIR-006, GIR-008, GIR-009

**Note**: GIR-006 is executed as a placement-policy amendment tracked as `P-PH000-ST001-AC004-TK003.4`.

### B. T104-PH001-ST007 — Migration / Enforcement Scope

If the Client selects “Defer to T104-PH001-ST007” for the GIRs below, no P-STD-004 amendments are required; execution occurs as migration/enforcement work:
- GIR-011

**Tracking note**: Even though execution is in `T104-PH001-ST007`, these items are tracked and work-packaged in AC004 via:
- `P-PH000-ST001-AC004-TK003.3` (GIR-011 `_gate-###` rename + enforcement)

### C. TK003.1 — P-STD-005 Clarification (If Approved at GATE-002)

If the Client selects “Create follow-on task” for GIR-010, TK003.1 MUST amend P-STD-005-CLAUSE-004 to clarify:
- Full formal reference format MUST be used for main CLAUSE IDs (and standard tokens) only
- Subclause IDs MAY appear as inline short-hand pointers, but MUST NOT be treated as full-formal references

---

## V. CLIENT CONFIRMATION

**Instructions**: For each GIR entry in Section III, mark the selected option. If overriding a recommendation, provide the override text.

**Confirmation Statement**:
- [x] I confirm the dispositions marked above. These dispositions are binding inputs to GATE-002 and downstream execution (TK003/TK003.1 and assigned T104 migration work).
- **Confirmed by**: Client
- **Date**: 2026-03-01

---

## VI. GATE DECISION RECORD (GDR)

This section copies the Gate Decision Record structure from `prompt/templates/consultant/workspace/guideline_workspace_verification.md` (§X) and the GDR section in `verification_P-PH000-ST001-AC004_gate-002.md`. Per instruction, GATE-002 closure is recorded **only in this proposal**.

| Field | Value |
|:--|:--|
| Gate ID | `P-PH000-ST001-AC004-GATE-002` |
| Reviewer Verdict | PASS |
| Client Decision | APPROVE |
| Conditions (if any) | — |
| Decided By | Client |
| Decision Date | 2026-03-01 |
| Decision Reference | Client approval recorded in chat on 2026-03-01 |

**Gate Status**: `completed` (recorded in this proposal only)

---

## VII. SOURCES & TRACEABILITY

| Source | Path | Role |
|:--|:--|:--|
| TK002 Analysis Deliverable | `prompt/artifacts/tasks/P/workspace/PH000/ST001/analysis/analysis_P-PH000-ST001-AC004_p-std-004-proposal-seeding-assessment.md` | GIR source + remediation descriptions |
| TK002.1 Verification Evidence | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/verification/verification_P-PH000-ST001-AC004_gate-002.md` | Confirms analysis package decision-readiness |
| External Review Analysis | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/analysis/analysis_P-PH000-ST001-AC004-GATE-002_external-review-disposition.md` | Independent external review of this disposition package |
| AC004 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC004/plan_P-PH000-ST001-AC004.md` | Governing plan for GATE-002 and downstream tasks |

---

## VIII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-28 | Initial | Created GATE-002 GIR disposition proposal with options, recommendations, and Client decision checkboxes for GIR-001…GIR-011; mapped each GIR to TK003, TK008, or T104-PH001-ST007 as appropriate. |
| v1.1.0 | 2026-02-28 | Amendment | QA updates: GIR-004 adds dev-report topic-qualified pattern variant; GIR-006 + GIR-011 option (b) recorded as pre-approved (2026-02-28) and tied to explicit AC004 tracking tasks (TK009/TK010) for T104 migration/enforcement and T102 first-migration conformance. |
| v1.2.0 | 2026-03-01 | Amendment | Recorded GATE-002 approval (proposal-only) via copied GDR; updated dispositions to reflect GATE-002 decisions (including placement-policy change for `analysis/`/`proposal/`); aligned downstream task IDs to the AC004 activity plan; added external review analysis to package traceability. |
