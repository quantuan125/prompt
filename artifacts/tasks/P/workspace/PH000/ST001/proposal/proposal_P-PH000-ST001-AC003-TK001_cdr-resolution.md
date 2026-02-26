---
artifact_type: 'PROPOSAL'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC003'
task_id: 'P-PH000-ST001-AC003-TK001'
version: '1.0.0'
date: '2026-02-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
purpose: 'Consolidated Decision Register (CDR) resolution proposal — recommended resolutions for all 13 client-facing decisions from combined P-RES-001 and P-RES-002 integration analyses, for Client confirmation before P-STD-002 authoring'
consumer: 'P-PH000-ST001-AC003-TK002'
---

# PROPOSAL: CDR Resolution — P-STD-002 Authoring Decisions

> **Purpose**: This file consolidates all 13 client-facing decisions identified across the P-RES-001 and P-RES-002 integration recommendation packages. Each decision carries a consultant recommendation. The Client confirms or overrides each decision. Once confirmed, this proposal becomes a normative input to TK002 (Draft P-STD-002 Specification) and TK003 (Draft P-STD-002-ADR-001).

---

## I. DECISION REGISTER

### A. Critical Decisions (must resolve before TK002)

#### CDR-01: Execution Model Boundary

**Domain(s)**: P-STD-002A, P-STD-002E
**Source**: P-RES-002 (RES2-DEC-4)

**Question**: Should tool execution states (approval_policy, sandbox_mode, run lifecycle) become part of the 7-state program status enum?

| Option | Description |
|:--|:--|
| (a) Add to enum | Extend the 7-state vocabulary with tool-specific execution states |
| **(b) Keep as non-status governed fields (Recommended)** | Tool execution is evidence context, not program status. Non-status metadata fields carry execution context without vocabulary drift. |

**Rationale**: P-RES-002 Finding 1: "Tool-level execution state ≠ program-level status." Adding vendor-specific lifecycle states to the program enum creates vocabulary drift and violates the vocabulary stability confirmed by both research streams.

**Impact**: Governs CDR-02 and CDR-04 scope. Affects CLAUSE themes A-10, A-11, E-9, E-11.

**Client Decision**: `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

#### CDR-02: Transition Path — `planned` → `in_progress`

**Domain(s)**: P-STD-002A
**Source**: P-RES-001 (A-DEC-1)

**Question**: Should `planned` → `in_progress` (skipping `ready`) be a permitted transition?

| Option | Description |
|:--|:--|
| (a) Permitted with guard | Allow direct transition with a guard condition |
| **(b) Disallowed (Recommended)** | `ready` serves as a readiness gate preventing work from starting without minimum preparation (definition-of-ready). The v2 transition matrix from P-RES-001 Topic 2 disallows this path. |

**Rationale**: The `ready` state ensures a minimum preparation check before work begins. Skipping it defeats the purpose of readiness governance.

**Impact**: Affects transition matrix CLAUSE in P-STD-002A.

**Client Decision**: `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

#### CDR-03: 7-State Vocabulary Stability Confirmation

**Domain(s)**: P-STD-002A (foundational — affects all domains)
**Source**: Combined (P-RES-001 + P-RES-002)

**Question**: Confirm that the 7-state canonical vocabulary is stable across both research inputs?

| Option | Description |
|:--|:--|
| **(a) Stable — confirmed (Recommended)** | Both P-RES-001 (Topic 1, weighted score 80/90) and P-RES-002 (Topic 1, verdict) independently confirm the 7-state vocabulary. No evidence suggests adding or removing states. |
| (b) Needs revision | Request vocabulary revision before P-STD-002 authoring |

**Rationale**: Foundational decision — all other decisions build on the 7-state vocabulary being stable.

**Impact**: Foundational — affects all 5 domains and all 54 CLAUSE themes.

**Client Decision**: `[ ] (a)` / `[ ] (b)` / `[ ] Override: _______________`

---

#### CDR-09: Evidence Validation + Evidence Anchor

**Domain(s)**: P-STD-002D
**Source**: P-RES-001 (D-DEC-1) + P-RES-002 (RES2-DEC-1)

**Question**: Should evidence validation be normative (MUST) and should GitHub Checks be the primary evidence anchor?

| Option | Description |
|:--|:--|
| **(a) MUST + Checks primary with commit status fallback (Recommended)** | Broken evidence pointers undermine traceability (P-QG-002). Checks API scored 89/95 vs Commit Status API 65/95 (P-RES-002 Topic 5). Checks offers richer audit metadata. Commit status fallback preserves portability. |
| (b) SHOULD + any evidence | Advisory evidence validation with no platform preference |
| (c) MUST + no platform preference | Normative validation but no evidence anchor preference |

**Rationale**: Traceability integrity (P-QG-002) requires verifiable evidence. GitHub Checks provides the richest, most governance-suitable repo-native primitive while commit status fallback preserves portability for non-GitHub environments.

**Impact**: Affects CLAUSE themes D-4, D-10, D-11.

**Client Decision**: `[ ] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

#### CDR-10: Aggregation Policy Requirement

**Domain(s)**: P-STD-002B, P-STD-002D
**Source**: P-RES-002 (RES2-DEC-2)

**Question**: Should aggregation policy (fail-fast / allow-failure / continue-on-error / manual-gate) be explicitly declared and required for multi-evidence status updates?

| Option | Description |
|:--|:--|
| **(a) Required — MUST (Recommended)** | Without explicit aggregation, parent-level status is ambiguous for both agents and humans. P-RES-002 Finding 3 and Risk-002 document the governance gap. |
| (b) Recommended — SHOULD | Advisory aggregation policy |
| (c) Optional — MAY | Fully optional aggregation policy |

**Rationale**: Parent-level status ambiguity is the primary governance risk identified by P-RES-002. Making aggregation policy explicit and required closes this gap deterministically.

**Impact**: Affects CLAUSE themes D-12, B-7, E-10.

**Client Decision**: `[ ] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

#### CDR-11: Ledger Schema Depth

**Domain(s)**: P-STD-002E
**Source**: P-RES-001 (E-DEC-1)

**Question**: Should P-STD-002E prescribe a normative ledger schema or defer schema specifics to a companion guideline?

| Option | Description |
|:--|:--|
| (a) Normative schema in P-STD-002E | Full schema prescribed in the standard |
| (b) Schema principles only | Principles in P-STD-002E, detailed schema in a companion guideline |
| **(c) Schema with extensibility hooks (Recommended)** | Normative baseline schema in P-STD-002E with extensibility hooks for initiative-specific enrichment. Provides interoperability guarantees while remaining adaptable. Avoids indirection cost of a separate guideline. |

**Rationale**: A normative baseline provides interoperability; extensibility hooks allow initiative-specific enrichment without requiring a separate guideline artifact.

**Impact**: Affects CLAUSE theme E-4 depth and whether a companion guideline is needed.

**Client Decision**: `[ ] (a)` / `[ ] (b)` / `[ ] (c)` / `[ ] Override: _______________`

---

## II. CLIENT CONFIRMATION

**Instructions**: For each CDR entry above, mark the selected option. If overriding the recommendation, provide the override text.

**Confirmation Statement**:
- [ ] I confirm the decisions marked above. These decisions are binding inputs to P-STD-002 authoring (TK002) and ADR-001 (TK003).
- **Confirmed by**: _______________
- **Date**: _______________

---

## III. SOURCES & TRACEABILITY

| Source | Path | Role |
|:--|:--|:--|
| P-RES-001 Integration Recommendations (v1.0.0) | `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC001-TK003_integration-recommendations-P-RES-001.md` | Baseline (9 decisions) |
| P-RES-002 Integration Recommendations (v2.0.0) | `prompt/artifacts/tasks/P/workspace/PH000/ST004/analysis/analysis_P-PH000-ST004-AC002-TK003_integration-recommendations-P-RES-002.md` | Complement (4 decisions + consolidated register) |
| AC003 Activity Plan (v0.2.0) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md` | Governing plan |

---

## IV. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-02-26 | Initial | CDR resolution proposal created with all 13 consolidated decisions from P-RES-001 + P-RES-002 integration analyses. Organized by priority tier (6 Critical, 4 High, 3 Medium, 1 Low). Each decision carries consultant recommendation and Client confirmation block. |
