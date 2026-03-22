---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC003'
task_ids:
  - 'T104-PH001-ST008-AC003-TK004'
  - 'T104-PH001-ST008-AC003-TK005'
  - 'T104-PH001-ST008-AC003-TK006'
version: '1.2.0'
date: '2026-03-22'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/plan_T104-PH001-ST008-AC003.md'
purpose: 'Developer-ready execution specification for AC003 post-GATE-001 implementation: active scope A-C only, with the ADR-script gap routed to T103 outside the active AC003 path.'
---

# IMPLEMENTATION (Task Specification): AC003 Cross-Guideline Gap Resolution

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the complete HOW for executing AC003 post-GATE-001 gap resolution work across three active implementation clusters (NOTES package, cross-reference repairs, role/gate wording) covering plan tasks TK004, TK005, and TK006. Cluster D (ADR scripts) is routed to T103 and is not part of the active AC003 path.
- **Authority chain**: Activity plan `T104-PH001-ST008-AC003` authorizes the active AC003 work (TK004–TK006) → This artifact specifies HOW → Dev-report (TK008) records execution → GATE-002 closes the active AC003 activity.
- **Audience**: LLM_Developer (primary consumer for execution), LLM_Reviewer (secondary consumer for GATE-002 verification)
- **This artifact does NOT hold a GDR.** Gate decisions are recorded in the gate-disposition proposals at `AC003/proposal/`.

**Source material**: This specification migrates developer-ready content from:
- `analysis_T104-PH001-ST008-AC003_implementation-spec.md` v1.1.0 (§III per-gap change specifications) — now informative-only
- `analysis_T104-PH001-ST008-AC003_gate-001_remediation-checklist.md` v1.0.0 (§II remediation register) — now informative-only
- `analysis_T104-PH001-ST008-AC003-GATE-001_external-review-reassessment.md` v1.0.0 (current same-gate reassessment review)
- `proposal_T104-PH001-ST008-AC003-GATE-001_gir-disposition-package.md` v1.3.0 (corrected same-gate proposal package)
- `snotes_T104-PH001-ST008-AC003-SES004.md` v1.0.0 (same-gate correction session trail)

**Current-state verification requirement**: File versions have shifted since the source analysis was authored (2026-03-17/18). The developer MUST verify current-state evidence (line numbers, quoted text) against live files before applying each change. The gap fix *intent* documented in each SPEC item remains valid.

---

## II. TASK SCOPE

- **Governing plan tasks**: `TK004` (Cluster A), `TK005` (Cluster B), `TK006` (Cluster C)
- **Out-of-scope routing**: `TK007` (Cluster D) is cancelled from active AC003 scope and routed to T103
- **Trigger**: Task complexity — 13 gaps with 3 active clusters plus an out-of-scope routed cluster touching 13+ target files require structured specification beyond plan-step capacity.
- **Deliverable contract**: Updated guidelines, templates, and governance files per the AC003 activity plan Task Register.
- **Depends On**: `T104-PH001-ST008-AC003-GATE-001` (must record APPROVE or APPROVE WITH CONDITIONS)

---

## III. SPECIFICATION ITEMS

### Cluster A — NOTES Package Fixes (TK004)

**Target files**: 5 files
**P-STD-005 alignment note**: Templates in Cluster A use `<INIT>` as a placeholder token. Per P-STD-005, the conformant placeholder should be `<SID>`. This alignment is informative and should be resolved alongside Cluster A updates.

---

#### SPEC-A01 — GAP-003: Phase Notes Register Session-Path Naming

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-003 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/template_workspace_notes_register_phase.md` |
| Target Section | §II — Phase-Level Session Notes Register |
| Implementation Detail | Replace the session-path example `notes_<INIT>-PH###-SES###.md` with `snotes_<INIT>-PH###-SES###.md` to match the guideline's `snotes_` prefix convention. |
| Acceptance Criteria | Phase register session-path example uses `snotes_` prefix, not `notes_`. |
| Status | `open` |

#### SPEC-A02 — GAP-004 Change 1: Stream Register Session-Path

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-004 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/template_workspace_notes_register_stream.md` |
| Target Section | §II (session-path column) |
| Implementation Detail | Replace `notes_<INIT>-PH###-ST###-SES###.md` with `snotes_<INIT>-PH###-ST###-SES###.md`. |
| Acceptance Criteria | Stream register session-path uses `snotes_` prefix. |
| Status | `open` |

#### SPEC-A03 — GAP-004 Change 2: Stream Register Activity Notes Path

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-004 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/template_workspace_notes_register_stream.md` |
| Target Section | §III — Activity Notes Register (Notes File column) |
| Implementation Detail | Replace `notes_[INIT]-PH###-ST###-AC###-SES###.md` with `snotes_[INIT]-PH###-ST###-AC###-SES###.md`. |
| Acceptance Criteria | Activity notes path uses `snotes_` prefix. |
| Status | `open` |

#### SPEC-A04 — GAP-004 Change 3: Stream Register Status Enum

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-004 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/template_workspace_notes_register_stream.md` |
| Target Section | §I (Status field) |
| Implementation Detail | **RETRACTED (SES002)**: Retain `deferred` pending P-STD-002 harmonization at `P-PH000-ST001-AC003-TK013`. No change. |
| Acceptance Criteria | N/A — no change required. |
| Status | `retracted` |

#### SPEC-A05 — GAP-005 Change 1: Activity Register Session-Path

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-005 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/template_workspace_notes_register_activity.md` |
| Target Section | §II (session-path column) |
| Implementation Detail | Replace `notes_<INIT>-PH###-ST###-AC###-SES###.md` with `snotes_<INIT>-PH###-ST###-AC###-SES###.md`. |
| Acceptance Criteria | Activity register session-path uses `snotes_` prefix. |
| Status | `open` |

#### SPEC-A06 — GAP-005 Change 2: Activity Register Status Enum

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-005 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/template_workspace_notes_register_activity.md` |
| Target Section | §I (Status field) |
| Implementation Detail | **RETRACTED (SES002)**: Retain `deferred` pending P-STD-002 harmonization. No change. |
| Acceptance Criteria | N/A — no change required. |
| Status | `retracted` |

#### SPEC-A07 — GAP-005 Change 3: Legacy Template Status Enum

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-005 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/template_workspace_notes.md` |
| Target Section | Status field |
| Implementation Detail | **RETRACTED (SES002)**: Retain `deferred` pending P-STD-002 harmonization. No change. |
| Acceptance Criteria | N/A — no change required. |
| Status | `retracted` |

#### SPEC-A08 — GAP-005 Change 4: Legacy Template Activity Register Path

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-005 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/template_workspace_notes.md` |
| Target Section | §III — Activity Notes Register (path column) |
| Implementation Detail | Replace `notes_[INIT]-PH###-ST###-AC###-SES###.md` with `snotes_[INIT]-PH###-ST###-AC###-SES###.md` in the path column. |
| Acceptance Criteria | Legacy template path uses `snotes_` prefix. |
| Status | `open` |

#### SPEC-A09 — GAP-005 Change 5: Notes Guideline Frontmatter

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-005 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| Target Section | File start (no frontmatter currently exists) |
| Implementation Detail | Add YAML frontmatter block at top of file: `artifact_type: 'PROCEDURAL_GUIDELINE'`, `domain: 'consultant_workspace'`, `topic: 'notes_authoring'`, `version: '1.2.0'`, `date: '2026-03-20'`, `status: 'draft'`, `author: 'LLM_Consultant'`, `decision_owner_role: 'Client'`, `template_references:` array pointing to 6 notes templates (3 register + 3 session). Bump version from v1.1.0 to v1.2.0. Add changelog entry. |
| Acceptance Criteria | Notes guideline has YAML frontmatter matching peer guideline pattern. |
| Status | `open` |

#### SPEC-A10 — SES002: `<INIT>` → `<SID>` Token Alignment

| Field | Detail |
|:--|:--|
| Requirement Source | SES002 client feedback; P-STD-005-CLAUSE-008A |
| Target File | All Cluster A templates |
| Implementation Detail | Align `<INIT>` placeholder tokens to `<SID>` per P-STD-005 conformance where applicable. This is informative and should be applied as a best-effort correction during the Cluster A edit pass. |
| Acceptance Criteria | Template placeholders use `<SID>` where applicable. |
| Status | `open` |

---

### Cluster B — Cross-Reference Repairs (TK005)

**Target files**: 5 files

---

#### SPEC-B01 — GAP-001: Deprecated T102 Standards Paths

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-001 from T104-RES-003 |
| Target File | All AC003 target files |
| Implementation Detail | Grep all AC003 target files for `T102/consultant/standards/`. **Expected result: zero matches** (confirmed in analysis). If any matches are found, replace with `prompt/artifacts/tasks/T102/standard/...`. |
| Acceptance Criteria | Grep returns zero matches for deprecated paths in all AC003 target files. |
| Status | `open` |

#### SPEC-B02 — GAP-013: Plan Guideline Frontmatter Template Reference

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-013 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Target Section | Frontmatter (`template_reference` key) |
| Implementation Detail | Replace single `template_reference: 'prompt/templates/consultant/workspace/README.md'` with `template_references:` array pointing to 3 live PLAN templates: `template_workspace_plan_phase.md`, `template_workspace_plan_stream.md`, `template_workspace_plan_activity.md`. |
| Acceptance Criteria | Plan guideline frontmatter `template_references` points to 3 live PLAN templates; `README.md` reference is removed. |
| Status | `open` |

#### SPEC-B03 — GAP-014: Naming Authority References (P-STD-004 Proposal → Standard)

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-014 from T104-RES-003 |
| Target File | (1) `guideline_workspace_plan.md` §VIII.D, (2) `guideline_workspace_roadmap.md` §VI.C, (3) `guideline_workspace_notes.md` §7 |
| Implementation Detail | In all three files, replace the old P-STD-004 proposal path `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` with the adopted standard path `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`. |
| Acceptance Criteria | All three guidelines reference P-STD-004 at its adopted standard path. |
| Status | `open` |

#### SPEC-B04 — GAP-015: Verification Guideline Rework Section Reference

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-015 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Target Section | §IX — Re-Assessment Versioning |
| Implementation Detail | Update the reference from `guideline_workspace_plan.md §VII` (Sub-Activity Rules) to `guideline_workspace_plan.md §IV.E` (Task Decomposition Rules). The developer MUST verify the current line number as this file has been bumped since spec authoring. |
| Acceptance Criteria | §IX and §X both reference `guideline_workspace_plan.md §IV.E` — no conflicting navigation. |
| Status | `open` |

#### SPEC-B05 — GAP-016: GDR Section Placement Description

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-016 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Target Section | §VII.C — GDR Field Specification |
| Implementation Detail | Update the placement description from "penultimate section (before Changelog)" to "after the Disposition Register and before the References and Changelog sections" to match the template and live packages (GDR → References → Changelog). The developer MUST verify the current line number as this file has been updated by AC001.5. |
| Acceptance Criteria | Guideline's GDR placement rule matches the template structure. |
| Status | `open` |

#### SPEC-B06 — GAP-017: Client Decision Enum — Missing `pending`

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-017 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Target Section | §VII.C — GDR Field Specification (Client Decision row) |
| Implementation Detail | Add `pending` to the Client Decision enum. **Note**: The developer MUST verify the current enum values in §VII.C as AC001.5 may have already modified this section. If `pending` is already present, confirm and mark as pre-resolved. If the enum now includes `SUPERSEDE` (from AC001.4), preserve that addition. |
| Acceptance Criteria | Client Decision enum includes `pending` and matches the template and lifecycle text. |
| Status | `open` |

---

### Cluster C — Role/Gate Wording Fixes (TK006)

**Target files**: 3 files

---

#### SPEC-C01 — GAP-006: Role Authority Fragmentation (Localized Pointer)

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-006 from T104-RES-003, refined SES002 |
| Target File | `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md` |
| Target Section | §III.B.1 — Organization & Responsibilities |
| Implementation Detail | Add a consolidated pointer note after the existing role/RACI tables: "**Role Authority Note**: The workspace role contract for T104 is distributed across multiple surfaces. For the definitive role-to-artifact ownership matrix, see `workspace_documentation_rules.md` §8. For gate-specific role boundaries (reviewer verdict, client GDR, developer evidence), see `guideline_workspace_verification.md` §II and `guideline_workspace_proposal.md` §VII. Full role consolidation into a single authoritative surface is deferred to T101." |
| Acceptance Criteria | SPS §III.B.1 contains pointer to distributed role authority surfaces. No role definition changes. |
| Status | `open` |

#### SPEC-C02 — GAP-007: Consultant-Authored Task Registers

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-007 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Target Section | §6.A — Consultant (LLM_Consultant) (boundary text) |
| Implementation Detail | Refine the boundary text from "MUST NOT author implementation-level task decomposition or execution proof" to "MUST NOT author implementation-level execution proof. Contract-level task registers and task decomposition in plans are within consultant scope per `guideline_workspace_plan.md` §IV." The developer MUST verify the current §6.A text as this file is now v3.0.0+ (AC001.3 TK007 patches). |
| Acceptance Criteria | §6.A permits consultant-authored task registers while maintaining prohibition on implementation-level execution evidence. |
| Status | `open` |

#### SPEC-C03 — GAP-008: Stale "Proposals Are Not Final Decisions" (Pre-Resolved)

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-008 from T104-RES-003 |
| Target File | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Target Section | §10 — Anti-Drift Rules |
| Implementation Detail | **PRE-RESOLVED in v2.8.0 (AC001.2)**. Developer confirms current state only: verify that §10.C does not contain "proposals are not final decisions" or equivalent stale wording. No edit expected. |
| Acceptance Criteria | §10.C correctly identifies proposals as hosting the authoritative GDR. |
| Status | `pre-resolved` |

---

### Out-of-Scope Note — ADR Script Path Fixes (TK007) Routed to T103

| Field | Detail |
|:--|:--|
| Requirement Source | GAP-002 from T104-RES-003 |
| Target File | `print_t102_adr_005.py`, `print_t102_adr_007.py` |
| Implementation Detail | **OUT OF ACTIVE AC003 SCOPE**. ADR helper script work is routed to T103 and is not part of the active AC003 implementation path. |
| Acceptance Criteria | N/A — no AC003 action. |
| Status | `routed_to_T103` |

---

## IV. IMPLEMENTATION SEQUENCE

### Recommended Execution Order

| Order | Cluster | Task | Rationale |
|:--|:--|:--|:--|
| 1 | A — NOTES package | TK004 | Self-contained; highest visibility naming drift; 5 files touched |
| 2 | B — Cross-refs | TK005 | Largest cluster (6 gaps); touches the most guidelines |
| 3 | C — Role/gate | TK006 | 1 of 3 gaps pre-resolved; localized changes |
| — | ~~D — Scripts~~ | ~~TK007~~ | **Routed to T103; not part of active AC003 scope** |

### Intra-Cluster Notes

- **Cluster A**: SPEC-A09 (guideline frontmatter) should be done last within Cluster A to capture an accurate version number reflecting the other NOTES changes.
- **Cluster B**: SPEC-B03 touches 3 files with the same replacement — apply in parallel. SPEC-B05 and SPEC-B06 both touch `guideline_workspace_proposal.md` — apply in a single edit pass.
- **Cluster C**: No internal dependencies.

### Developer Verification Protocol

Before applying any SPEC item, the developer MUST:
1. Read the target file's current state
2. Verify the target section exists at the documented location (line numbers may have shifted)
3. Confirm the quoted "current state" still matches (or note the deviation)
4. Apply the change to the actual current state
5. Record any deviations from this specification in the dev-report (TK008)

---

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/plan_T104-PH001-ST008-AC003.md` |
| Source Analysis (informative) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/analysis/analysis_T104-PH001-ST008-AC003_implementation-spec.md` |
| Source Remediation Checklist (informative) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/analysis/analysis_T104-PH001-ST008-AC003_gate-001_remediation-checklist.md` |
| Same-Gate Reassessment External Review | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/analysis/analysis_T104-PH001-ST008-AC003-GATE-001_external-review-reassessment.md` |
| GATE-001 Proposal | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/proposal/proposal_T104-PH001-ST008-AC003-GATE-001_gir-disposition-package.md` |
| SES004 Session Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/snotes/snotes_T104-PH001-ST008-AC003-SES004.md` |
| Historical External Review | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/analysis/analysis_T104-PH001-ST008-AC003_external-review_gate-001-package.md` |
| T104-RES-003 Report | `prompt/artifacts/tasks/T104/research/T104-RES-003/report_T104-RES-003_workspace-artifact-integration-analysis.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |

---

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.2.0 | 2026-03-22 | Maintenance | Frontmatter: replaced single task_id with task_ids YAML array covering TK004, TK005, TK006 to reflect actual multi-task scope. Source: Pre-GATE-001 remediation pass. |
| v1.1.0 | 2026-03-21 | Amendment | Same-gate reassessment refresh: aligned the implementation spec to the corrected AC003 package, added the new reassessment external review and SES004 to the evidence trail, reduced active scope to TK004-TK006 only, and routed TK007 / GAP-002 to T103 outside the active AC003 path. |
| v1.0.0 | 2026-03-20 | Initial | IMPLEMENTATION task_specification created for AC003 post-GATE-001 gap resolution. Migrated 13 per-gap change specifications from analysis artifacts into 16 SPEC items across 4 clusters: A (NOTES, 10 items — 3 retracted), B (cross-refs, 6 items), C (role/gate, 3 items — 1 pre-resolved), D (scripts, 1 item — deferred to T103). Source: analysis_T104-PH001-ST008-AC003_implementation-spec.md v1.1.0 + analysis_T104-PH001-ST008-AC003_gate-001_remediation-checklist.md v1.0.0. |
