---
artifact_type: 'PLAN'
planning_level: 'ACTIVITY'
initiative_id: 'P'
initiative_code: 'PROGRAM'
phase: '0'
stream_id: 'P-PH000-ST001'
activity_id: 'P-PH000-ST001-AC010'
version: '1.0.0'
date: '2026-03-26'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
governance_rules: 'prompt/templates/consultant/workspace/workspace_documentation_rules.md'
procedural_guideline: 'prompt/templates/consultant/workspace/guideline_workspace_plan.md'
parent_plan: 'prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md'
---

# PLAN: P (PROGRAM) — Phase 0 / Stream ST001 / Activity AC010: Cross-Standard Conformance Pass (P-STD-001 Metadata CLAUSEs)

## I. EXECUTIVE SUMMARY

**Purpose**: Bring all existing P-STD standards (P-STD-002, P-STD-004, P-STD-005) into conformance with the P-STD-001 metadata governance CLAUSEs (CLAUSE-031 through CLAUSE-036, including CLAUSE-036G) authored and evolved in AC009. This is a structure-only retrofit — no normative CLAUSE content within the target standards is modified.

**Non-goals**:
- This activity does not modify P-STD-001 (completed and evolved in AC009).
- This activity does not modify normative CLAUSE content within P-STD-002, P-STD-004, or P-STD-005.
- This activity does not include P-STD-003 (deprecated placeholder — excluded per client direction).
- This activity does not perform repo-wide reference sweeps beyond Tier 1.

---

## II. ACTIVITY OUTLINE

**Activity ID**: `P-PH000-ST001-AC010`
**Objective**: Apply the P-STD-001 metadata governance model to all existing P-STD standards so the program-level standards suite is structurally conformant.
**Execution Mode**: `SEQUENTIAL`
**Depends On**: `P-PH000-ST001-AC009` (specifically `P-PH000-ST001-AC009-GATE-002` + `P-PH000-ST001-AC009-TK006`)

**Context**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` (v1.2.0 — design authority)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md` (target)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` (target)
- `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` (target)
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK006_ac010-handoff-boundary.md` (handoff boundary)
- `prompt/templates/consultant/standards/guideline_standard_specs.md` (authoring guide)
- `prompt/templates/consultant/standards/template_standard_specs.md` (structural template)

### Task Register

| Task | Task ID | Name | Status | Owner | Depends On | Target | Reference | Action |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| TK000 | `P-PH000-ST001-AC010-TK000` | Metadata conformance audit of P-STD-002/004/005 | `planned` | LLM_Consultant | — | Gap inventory per CLAUSE-031 through CLAUSE-036 | P-STD-001 v1.2.0 + AC009 handoff | — |
| TK001 | `P-PH000-ST001-AC010-TK001` | Retrofit P-STD-002 (YAML + Provenance + References + Amendment History) | `planned` | LLM_Developer | TK000 | `standard_P-STD-002_program-status-standard.md` | TK000 audit findings | — |
| TK002 | `P-PH000-ST001-AC010-TK002` | Retrofit P-STD-004 (YAML + Provenance + References + Amendment History) | `planned` | LLM_Developer | TK000 | `standard_P-STD-004_file-naming-and-directory-convention.md` | TK000 audit findings | — |
| TK003 | `P-PH000-ST001-AC010-TK003` | Retrofit P-STD-005 (YAML + Provenance + References + Amendment History) | `planned` | LLM_Developer | TK000 | `standard_P-STD-005_universal-id-specification.md` | TK000 audit findings | — |
| TK004 | `P-PH000-ST001-AC010-TK004` | SPS row updates (version bump propagation) | `planned` | LLM_Developer | TK001, TK002, TK003 | `sps_P-PROGRAM.md` | Version changes from TK001-TK003 | — |
| TK005 | `P-PH000-ST001-AC010-TK005` | Dev-report for cross-standard retrofit | `planned` | LLM_Developer | TK004 | DEV-REPORT | `guideline_workspace_dev-report.md` | — |
| TK006 | `P-PH000-ST001-AC010-TK006` | Verification for cross-standard retrofit | `planned` | LLM_Reviewer | TK005 | VERIFICATION | `guideline_workspace_verification.md` | — |
| TK007 | `P-PH000-ST001-AC010-TK007` | Gate-001 disposition proposal | `planned` | LLM_Consultant | TK006 | PROPOSAL (gate_disposition) | `guideline_workspace_proposal.md` | — |
| GATE-001 | `P-PH000-ST001-AC010-GATE-001` | Gate: Client acceptance of cross-standard conformance retrofit | `planned` | Client | TK007 | Pass/fail | `guideline_workspace_plan.md` §VI | — |

---

## III. TASKS (DETAILED)

### Task TK000: Metadata Conformance Audit of P-STD-002/004/005

**Task ID**: `P-PH000-ST001-AC010-TK000`

**Purpose**: Audit all three target standards against the P-STD-001 metadata governance CLAUSEs to produce a precise gap inventory before retrofit execution.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010-TK000_metadata-conformance-audit.md`

**Scope**:
- In scope:
  - Audit each target standard against CLAUSE-031 (YAML frontmatter), CLAUSE-032 (metadata authority), CLAUSE-034 (version tracking), CLAUSE-035 (references taxonomy), CLAUSE-036 (provenance taxonomy including CLAUSE-036G)
  - Identify which structural elements are present, missing, or non-conformant
  - Produce a per-standard gap table with specific remediation actions
- Out of scope:
  - Modifying P-STD-001
  - Modifying normative CLAUSE content within target standards
  - Assessing target standard normative quality

**Inputs Required**:
- `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` (v1.2.0) — authoritative governance model
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC009/analysis/analysis_P-PH000-ST001-AC009-TK006_ac010-handoff-boundary.md` — handoff boundary and retrofit requirements
- Target standards (P-STD-002, P-STD-004, P-STD-005)

**Steps**:
1. Read each target standard and compare against CLAUSE-031 through CLAUSE-036 requirements.
2. For each standard, record: (a) frontmatter presence/completeness, (b) References taxonomy conformance, (c) Provenance taxonomy conformance, (d) Amendment History presence/format, (e) Input Sources presence.
3. Produce a consolidated gap table mapping each finding to the governing CLAUSE and a specific remediation action.

**Success Criteria**:
- [ ] Audit analysis exists at the canonical path
- [ ] All three target standards audited against all relevant CLAUSEs
- [ ] Gap table provides actionable remediation items per standard

---

### Task TK001: Retrofit P-STD-002

**Task ID**: `P-PH000-ST001-AC010-TK001`

**Purpose**: Apply the P-STD-001 metadata governance structure to P-STD-002 (Program Status Standard).

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`

**Scope**:
- In scope: Add YAML frontmatter, normalize References subsections, normalize Provenance subsections, add version tracking
- Out of scope: Modifying normative CLAUSE content; adding or removing CLAUSEs

**Steps**:
1. Add governed YAML frontmatter per CLAUSE-031.
2. Normalize `## References` into `### Normative References` and `### Informative References` per CLAUSE-035.
3. Normalize `## Provenance` into `### Status`, `### Lineage / Authority`, `### Amendment History`, `### Input Sources` per CLAUSE-036.
4. Verify internal consistency after structural changes.

**Success Criteria**:
- [ ] P-STD-002 has valid YAML frontmatter per CLAUSE-031
- [ ] References section conforms to CLAUSE-035
- [ ] Provenance section conforms to CLAUSE-036
- [ ] No normative CLAUSE content modified

---

### Task TK002: Retrofit P-STD-004

**Task ID**: `P-PH000-ST001-AC010-TK002`

**Purpose**: Apply the P-STD-001 metadata governance structure to P-STD-004 (File Naming & Directory Convention).

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`

**Scope**: Same as TK001, applied to P-STD-004.

**Steps**: Same as TK001, applied to P-STD-004.

**Success Criteria**: Same as TK001, applied to P-STD-004.

---

### Task TK003: Retrofit P-STD-005

**Task ID**: `P-PH000-ST001-AC010-TK003`

**Purpose**: Apply the P-STD-001 metadata governance structure to P-STD-005 (Universal ID Specification).

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`

**Scope**: Same as TK001, applied to P-STD-005.

**Steps**: Same as TK001, applied to P-STD-005.

**Success Criteria**: Same as TK001, applied to P-STD-005.

---

### Task TK004: SPS Row Updates

**Task ID**: `P-PH000-ST001-AC010-TK004`

**Purpose**: Update SPS entries if version changes occurred during TK001-TK003 retrofit.

**Deliverable**:
- Updated `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (if version bumps occurred)

**Steps**:
1. Check if TK001-TK003 resulted in version bumps for any target standard.
2. If yes, update the corresponding SPS STD Index rows.

**Success Criteria**:
- [ ] SPS rows reflect current versions for all retrofitted standards

---

### Task TK005: Dev-Report for Cross-Standard Retrofit

**Task ID**: `P-PH000-ST001-AC010-TK005`

**Purpose**: Produce bounded execution evidence for the retrofit pass.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/dev-report/dev-report_P-PH000-ST001-AC010_cross-standard-retrofit.md`

**Steps**:
1. Record execution evidence per `guideline_workspace_dev-report.md`.

**Success Criteria**:
- [ ] Dev-report exists with traceability to audit findings and retrofit actions

---

### Task TK006: Verification for Cross-Standard Retrofit

**Task ID**: `P-PH000-ST001-AC010-TK006`

**Purpose**: Independent verification that all target standards conform to P-STD-001 metadata governance CLAUSEs after retrofit.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/verification/verification_P-PH000-ST001-AC010_gate-001.md`

**Steps**:
1. Verify per `guideline_workspace_verification.md`.
2. Check each target standard against CLAUSE-031 through CLAUSE-036.
3. Verify no normative CLAUSE content was modified.

**Success Criteria**:
- [ ] Verification artifact exists with reviewer verdict

---

### Task TK007: Gate-001 Disposition Proposal

**Task ID**: `P-PH000-ST001-AC010-TK007`

**Purpose**: Author the gate-disposition proposal for client acceptance of the cross-standard conformance retrofit.

**Deliverable**:
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md`

**Steps**:
1. Author per `guideline_workspace_proposal.md`.

**Success Criteria**:
- [ ] Gate-001 proposal exists with GDR section for client decision

---

### GATE-001: Client Acceptance of Cross-Standard Conformance Retrofit

**Gate ID**: `P-PH000-ST001-AC010-GATE-001`

**Entry Criteria**:
- TK001-TK003 complete (all target standards retrofitted)
- TK004 complete (SPS updated)
- TK005 complete (dev-report)
- TK006 complete (verification with reviewer verdict)
- TK007 complete (gate-disposition proposal with GDR)

**Reviewer**: Client

**Exit Criteria**:
- Client records `APPROVE` or `APPROVE WITH CONDITIONS` in the GATE-001 GDR
- All P-STD standards are structurally conformant to P-STD-001 metadata governance

**Gate-Disposition Proposal**: `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/proposal/proposal_P-PH000-ST001-AC010_gate-001_cross-standard-retrofit-disposition.md`

---

## IV. DEPENDENCY NOTES

- **AC009 GATE-002** must record an approving GDR before AC010 execution begins.
- **AC009 TK006** (handoff boundary document) provides the explicit design-authority freeze for AC010. The handoff surface defines exactly which CLAUSE requirements AC010 must retrofit and what AC010 must not reopen.
- This activity does not modify any T102 or T104 artifacts.

---

## V. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-26 | Initial | Created AC010 activity plan for cross-standard conformance pass. Defines audit, per-standard retrofit, SPS update, and gate-readiness stack. Scope: structure-only conformance of P-STD-002, P-STD-004, P-STD-005 to P-STD-001 metadata governance CLAUSEs (CLAUSE-031 through CLAUSE-036G). Evidence: SES003 consultation + AC009 stream plan contract stub. |
