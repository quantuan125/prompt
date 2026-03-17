---
artifact_type: 'ANALYSIS'
analysis_type: 'assessment'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC003'
version: '1.1.0'
date: '2026-03-18'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/plan_T104-PH001-ST008-AC003.md'
purpose: 'Developer-ready implementation specification for 13 AC003-scoped gaps from T104-RES-003. Structured as TK001 gap extraction + TK002 per-gap change specifications.'
---

# ANALYSIS (Assessment): AC003 Cross-Guideline Gap Resolution — Implementation Specification

## I. EXECUTIVE SUMMARY

**Purpose**: This artifact combines the TK001 gap extraction (Section II) and TK002 implementation specification (Section III) into a single chronological document. It provides per-gap change specifications precise enough for developer execution without further clarification.

**Scope**: All 13 AC003-scoped gaps from `T104-RES-003` (GAP-001 through GAP-008, GAP-013 through GAP-017). Gaps routed to AC004 (GAP-009 through GAP-012) are excluded.

**Key findings during extraction**:
- **GAP-008 is pre-resolved**: The stale "proposals are not final decisions" sentence was already removed from `workspace_documentation_rules.md` during AC001.2 work (v2.8.0, 2026-03-15). The implementation spec documents this as verified-resolved; the developer should confirm current state only.
- **GAP-001 scope refinement**: The deprecated `T102/consultant/standards/...` paths do not appear in any AC003 target guideline or template file. The deprecated paths exist in the research brief (a closed AC002 artifact) and various historical workspace artifacts outside AC003 scope. GAP-001's AC003 resolution is limited to confirming no in-scope files contain the deprecated paths.
- **GAP-017 partial pre-resolution**: Template `template_workspace_proposal_gate-disposition.md` v1.3.0 (2026-03-16) already added `N/A — decision gate` to the Reviewer Verdict placeholder. The remaining issue is the omission of `pending` from the Client Decision enum in `guideline_workspace_proposal.md` §VII.C.

**Recommended cluster execution order**: A (NOTES) → B (Cross-refs) → C (Role/gate) → D (Scripts).

**Governance notice**: All change specifications in this document are **informative inputs** to the gate-disposition proposal. They do not carry implementation authority. Implementation authority flows through: Analysis (informative) → Proposal (gate disposition + client approval) → Plan (implementation tasks). Any remediation must be approved by the client at the gate before developer execution begins. This posture is pending codification in `guideline_workspace_analysis.md` via `T104-PH001-ST008-AC001.3` TK005.

---

## II. TK001 — GAP EXTRACTION AND CATEGORIZATION

### A. Extraction Source

- **Primary**: `prompt/artifacts/tasks/T104/research/T104-RES-003/report_T104-RES-003_workspace-artifact-integration-analysis.md` — §III Part B (gap register), §V (artifact updates)
- **Secondary**: `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC002/analysis/analysis_T104-PH001-ST008-AC002_report-integration-and-downstream-impact.md` — §VII (E-ID candidate mapping)

### B. Extracted Gap Register (AC003-Scoped)

| Gap ID | Category | Target File(s) | Description | Severity | Cluster |
|:--|:--|:--|:--|:--|:--|
| GAP-001 | `CROSS-REF` | Research brief (closed artifact) | Brief input packet uses deprecated `T102/consultant/standards/...` paths | High | B |
| GAP-002 | `CROSS-REF` | `print_t102_adr_005.py`, `print_t102_adr_007.py` | ADR helper scripts point to non-existent concept path and missing anchors | Medium | D |
| GAP-003 | `TEMPLATE-CONFORMANCE` | `template_workspace_notes_register_phase.md` | Phase register session-path example uses `notes_` instead of `snotes_` | High | A |
| GAP-004 | `TEMPLATE-CONFORMANCE` | `template_workspace_notes_register_stream.md` | Stream register: session-path uses `notes_`, status includes `deferred` | High | A |
| GAP-005 | `TEMPLATE-CONFORMANCE` | `template_workspace_notes_register_activity.md`, `template_workspace_notes.md`, `guideline_workspace_notes.md` | Activity register and legacy template: stale session-path and status; guideline lacks frontmatter | High | A |
| GAP-006 | `ROLE-BOUNDARY` | `sps_T104-CWS.md` (pointer only) | Role authority split across multiple surfaces; no single authoritative contract | High | C |
| GAP-007 | `ROLE-BOUNDARY` | `workspace_documentation_rules.md`, `guideline_workspace_plan.md` | §6.A forbids consultant-authored task registers but live activity plans use them | Medium | C |
| GAP-008 | `GATE-SEMANTICS` | `workspace_documentation_rules.md` | Stale "proposals are not final decisions" wording (**pre-resolved in v2.8.0**) | High | C |
| GAP-013 | `CROSS-REF` | `guideline_workspace_plan.md` | Frontmatter `template_reference` points to `README.md` instead of live PLAN templates | Medium | B |
| GAP-014 | `CROSS-REF` | `guideline_workspace_plan.md`, `guideline_workspace_roadmap.md`, `guideline_workspace_notes.md` | Naming authority references point to old P-STD-004 proposal path instead of adopted standard | Medium | B |
| GAP-015 | `CROSS-REF` | `guideline_workspace_verification.md` | §IX line 211 references `guideline_workspace_plan.md §VII` (Sub-Activity Rules) instead of `§IV.E` (Task Decomposition Rules) | High | B |
| GAP-016 | `CROSS-REF` | `guideline_workspace_proposal.md` | §VII.C says GDR is "penultimate section (before Changelog)" but template places GDR before References AND Changelog | High | B |
| GAP-017 | `CROSS-REF` | `guideline_workspace_proposal.md` | §VII.C Client Decision enum omits `pending`; lifecycle text (§VII.D) and template both include it | Medium | B |

### C. Cluster Assignment Summary

| Cluster | Task | Gaps | Gap Count |
|:--|:--|:--|:--|
| A — NOTES package | TK004 | GAP-003, GAP-004, GAP-005 | 3 |
| B — Cross-reference repairs | TK005 | GAP-001, GAP-013, GAP-014, GAP-015, GAP-016, GAP-017 | 6 |
| C — Role/gate wording | TK006 | GAP-006, GAP-007, GAP-008 | 3 |
| D — ADR script paths | TK007 **(deferred_to_T103)** | GAP-002 | 1 |
| **Total** | | | **13** |

### D. E-ID Candidate Mapping (from AC002 Integration Analysis §VII)

| E-ID | Gap Reference | AC003 Relevance |
|:--|:--|:--|
| E-ID-001 | GAP-003 (NOTES cleanup) | AC003 — highest-signal NOTES fix; session-path naming drift affects human navigation and agentic retrieval |
| E-ID-002 | GAP-008 (GDR wording) | AC003 — **pre-resolved** during AC001.2 (v2.8.0); developer confirms current state only |
| E-ID-003 | GAP-009 (SPS schema) | AC004 scope — not AC003 |
| E-ID-004 | GAP-011 (integration model) | AC004 scope — partially pre-addressed by workspace_documentation_rules.md §7/§8 added in v2.8.0 |

---

## III. TK002 — IMPLEMENTATION SPECIFICATION

### Cluster A — NOTES Package Fixes (TK004)

**Responsible role**: `LLM_Consultant` (template/guideline updates)
**Target files**: 5 files

**P-STD-005 alignment note (SES002)**: Templates in Cluster A use `<INIT>` as a placeholder token for initiative root identifiers. Per P-STD-005-CLAUSE-008A and the `SID` category token definition (P-STD-005 §III.B), the conformant placeholder should be `<SID>` (Scope ID), which covers all scope levels (Program, Initiative, Epic, Feature, Story). This alignment is informative and should be resolved alongside Cluster A template updates during post-gate implementation.

---

#### GAP-003: Phase Notes Register Session-Path Naming

**Target file**: `prompt/templates/consultant/workspace/template_workspace_notes_register_phase.md`
**Target section**: §II — Phase-Level Session Notes Register (line 33)

**Current state**:
```
| SES001 | `[INIT]-PH###-SES001` | [Session title] | YYYY-MM-DD | `[path/to/notes_<INIT>-PH###-SES###.md]` |
```

**Recommended change**: Replace the session-path example `notes_<INIT>-PH###-SES###.md` with `snotes_<INIT>-PH###-SES###.md` to match the guideline's `snotes_` prefix convention for session notes files.

**Acceptance criterion**: The Phase Notes Register template's session-path example column uses `snotes_` prefix, not `notes_`.

---

#### GAP-004: Stream Notes Register Session-Path and Status

**Target file**: `prompt/templates/consultant/workspace/template_workspace_notes_register_stream.md`

**Change 1 — Session-path naming (§II, line 35)**:

**Current state**:
```
| SES001 | `[INIT]-PH###-ST###-SES001` | [Session title] | YYYY-MM-DD | `[path/to/notes_<INIT>-PH###-ST###-SES###.md]` |
```

**Recommended change**: Replace `notes_<INIT>-PH###-ST###-SES###.md` with `snotes_<INIT>-PH###-ST###-SES###.md`.

**Change 2 — Activity Notes Register path (§III, line 43)**:

**Current state**:
```
| AC### | `[INIT]-PH###-ST###-AC###-SES###` | [Activity name] | `prompt/artifacts/tasks/[INIT]/workspace/PH###/ST###/notes_[INIT]-PH###-ST###-AC###-SES###.md` |
```

**Recommended change**: Replace `notes_[INIT]-PH###-ST###-AC###-SES###.md` with `snotes_[INIT]-PH###-ST###-AC###-SES###.md` in the Notes File column path.

**Change 3 — Status enum (§I, line 27)**:

**Current state**:
```
**Status**: `[planned|in_progress|completed|on_hold]`
```

**Recommended change**: ~~Replace `deferred` with `on_hold` to align with `P-STD-002` canonical lifecycle states.~~ **RETRACTED (SES002)**: Retain `deferred` pending P-STD-002 harmonization. Industry analysis confirms `deferred` (intentional postponement beyond current scope) is semantically distinct from `on_hold` (temporary pause within current scope). Resolution tracked at `P-PH000-ST001-AC003-TK013`. No change to this enum in AC003 scope.

**Acceptance criteria**:
- All session-path examples in the stream register template use `snotes_` prefix
- Status enum retains `deferred` pending P-STD-002 harmonization

---

#### GAP-005: Activity Notes Register, Legacy Template, and Guideline Frontmatter

**Target file 1**: `prompt/templates/consultant/workspace/template_workspace_notes_register_activity.md`

**Change 1 — Session-path naming (§II, line 37)**:

**Current state**:
```
| SES001 | `[INIT]-PH###-ST###-AC###-SES001` | [Session title] | YYYY-MM-DD | `[path/to/notes_<INIT>-PH###-ST###-AC###-SES###.md]` |
```

**Recommended change**: Replace `notes_<INIT>-PH###-ST###-AC###-SES###.md` with `snotes_<INIT>-PH###-ST###-AC###-SES###.md`.

**Change 2 — Status enum (§I, line 29)**:

**Current state**:
```
**Status**: `[planned|in_progress|completed|on_hold]`
```

**Recommended change**: ~~Replace `deferred` with `on_hold`.~~ **RETRACTED (SES002)**: Retain `deferred` pending P-STD-002 harmonization at `P-PH000-ST001-AC003-TK013`.

---

**Target file 2**: `prompt/templates/consultant/workspace/template_workspace_notes.md` (deprecated legacy template)

**Change 3 — Status enum (line 38)**:

**Current state**:
```
**Status**: `[planned|in_progress|completed|on_hold]`
```

**Recommended change**: ~~Replace `deferred` with `on_hold`.~~ **RETRACTED (SES002)**: Retain `deferred` pending P-STD-002 harmonization at `P-PH000-ST001-AC003-TK013`.

**Change 4 — Activity Notes Register path (§III, line 53)**:

**Current state**:
```
| AC### | `[INIT]-PH###-ST###-AC###-SES###` | [Activity name] | `[planned|in_progress|completed|on_hold]` | `prompt/artifacts/tasks/[INIT]/workspace/PH###/ST###/snotes_[INIT]-PH###-ST###-AC###-SES###.md` |
```

**Recommended change**: Replace `notes_[INIT]-PH###-ST###-AC###-SES###.md` with `snotes_[INIT]-PH###-ST###-AC###-SES###.md` in the path column. ~~Replace `deferred` with `on_hold` in the status column.~~ **RETRACTED (SES002)**: Retain `deferred` pending P-STD-002 harmonization.

---

**Target file 3**: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`

**Change 5 — Add YAML frontmatter**:

**Current state**: The notes guideline has NO YAML frontmatter. It starts directly with `# GUIDELINE: Workspace Notes...`. All other live guidelines (`guideline_workspace_plan.md`, `guideline_workspace_roadmap.md`, `guideline_workspace_verification.md`, `guideline_workspace_analysis.md`, `guideline_workspace_proposal.md`) include YAML frontmatter with `artifact_type`, `domain`, `topic`, `version`, `date`, `status`, `author`, `decision_owner_role`.

**Recommended change**: Add YAML frontmatter block at the top of the file matching the pattern used by peer guidelines:

```yaml
---
artifact_type: 'PROCEDURAL_GUIDELINE'
domain: 'consultant_workspace'
topic: 'notes_authoring'
version: '1.2.0'
date: '2026-03-17'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
template_references:
  - 'prompt/templates/consultant/workspace/template_workspace_notes_register_phase.md'
  - 'prompt/templates/consultant/workspace/template_workspace_notes_register_stream.md'
  - 'prompt/templates/consultant/workspace/template_workspace_notes_register_activity.md'
  - 'prompt/templates/consultant/workspace/template_workspace_notes_session_phase.md'
  - 'prompt/templates/consultant/workspace/template_workspace_notes_session_stream.md'
  - 'prompt/templates/consultant/workspace/template_workspace_notes_session_activity.md'
---
```

Note: Version is bumped from v1.1.0 to v1.2.0 to reflect the frontmatter addition. A changelog entry should be added.

**Acceptance criteria**:
- Activity notes register template uses `snotes_` prefix; status enum retains `deferred` pending P-STD-002 harmonization
- Legacy notes template uses `snotes_` prefix; status enum retains `deferred`
- Notes guideline has YAML frontmatter matching peer guideline pattern
- All 3 gaps (GAP-003, GAP-004, GAP-005) resolved per their acceptance criteria

---

### Cluster B — Cross-Reference Repairs (TK005)

**Responsible role**: `LLM_Consultant` (guideline/template updates)
**Target files**: 5 files

---

#### GAP-001: Deprecated T102 Standards Paths

**Target file(s)**: AC003 in-scope guideline and template files

**Current state**: A grep of all AC003 target files (the 7 guidelines, 6 templates, and 2 scripts) shows **zero matches** for `T102/consultant/standards`. The deprecated paths exist only in:
- The research brief (`brief_T104-RES-003...`) — a closed AC002 artifact
- Historical workspace artifacts (T102 plans, notes, proposals) — outside AC003 scope
- The program roadmap and tools catalog — outside AC003 scope

**Recommended change**: None for AC003 in-scope files. GAP-001 is **confirmed as not applicable** to the target file set. The deprecated paths in the research brief and historical artifacts are outside AC003's localized fix mandate.

**Acceptance criterion**: Confirmed that no AC003 target guideline/template files contain deprecated `T102/consultant/standards/...` paths. If any are discovered during implementation, replace with `prompt/artifacts/tasks/T102/standard/...`.

---

#### GAP-013: Plan Guideline Frontmatter Template Reference

**Target file**: `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
**Target section**: Frontmatter (line 10)

**Current state**:
```yaml
template_reference: 'prompt/templates/consultant/workspace/README.md'
```

**Recommended change**: Replace the single `template_reference` key with a `template_references` array pointing to the 3 live PLAN templates:

```yaml
template_references:
  - 'prompt/templates/consultant/workspace/template_workspace_plan_phase.md'
  - 'prompt/templates/consultant/workspace/template_workspace_plan_stream.md'
  - 'prompt/templates/consultant/workspace/template_workspace_plan_activity.md'
```

**Acceptance criterion**: Plan guideline frontmatter `template_references` points to the 3 live PLAN templates; `README.md` reference is removed.

---

#### GAP-014: Naming Authority References (P-STD-004 Proposal → Standard)

Three guidelines reference the old P-STD-004 *proposal* path instead of the adopted *standard* path.

**Target file 1**: `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
**Target section**: §VIII.D — Directory & Naming Conventions (line 426)

**Current state**:
```
  `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (P-STD-004 proposal)
```

**Recommended change**: Replace with:
```
  `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` (P-STD-004)
```

---

**Target file 2**: `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md`
**Target section**: §VI.C — Directory & Naming Conventions (line 150)

**Current state**:
```
  `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (P-STD-004 proposal)
```

**Recommended change**: Replace with:
```
  `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` (P-STD-004)
```

---

**Target file 3**: `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
**Target section**: §7 — Directory & Naming Conventions (line 250)

**Current state**:
```
  `prompt/artifacts/tasks/T104/workspace/PH001/ST002/AC000/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md` (P-STD-004 proposal)
```

**Recommended change**: Replace with:
```
  `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` (P-STD-004)
```

**Acceptance criterion**: All three guidelines reference `P-STD-004` at its adopted standard path, not the legacy proposal path.

---

#### GAP-015: Verification Guideline Rework Section Reference

**Target file**: `prompt/templates/consultant/workspace/guideline_workspace_verification.md`
**Target section**: §IX — Re-Assessment Versioning (line 211)

**Current state**:
```
- If the verification TASK methodology needs rework (not just the assessed deliverable), a sub-task (TK###.n) is created for the verification task, following `guideline_workspace_plan.md §VII` (Sub-Activity Rules).
```

**Contradicts**: Line 225 of the same guideline, which correctly states:
```
**Task decomposition clarification**: Any verification-driven task rework that needs new tracked authority follows `guideline_workspace_plan.md §IV.E` (Task Decomposition Rules), not the Sub-Activity rules in `§VII`.
```

**Recommended change**: Update line 211 to reference `§IV.E` (Task Decomposition Rules) instead of `§VII` (Sub-Activity Rules):
```
- If the verification TASK methodology needs rework (not just the assessed deliverable), a sub-task (TK###.n) is created for the verification task, following `guideline_workspace_plan.md §IV.E` (Task Decomposition Rules).
```

**Acceptance criterion**: §IX line 211 and §X line 225 both reference `guideline_workspace_plan.md §IV.E` — no conflicting navigation.

---

#### GAP-016: GDR Section Placement Description

**Target file**: `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
**Target section**: §VII.C — GDR Field Specification (line 223)

**Current state**:
```
Every `gate_disposition` proposal MUST include a Gate Decision Record as the penultimate section (before Changelog):
```

**Observed evidence**: The gate-disposition template (`template_workspace_proposal_gate-disposition.md`) places the GDR in §VI, followed by §VII (References) and §VIII (Changelog). The GDR is therefore the *third-to-last* section, not "penultimate" (which means second-to-last). All live gate-disposition packages follow the template's three-section tail (GDR → References → Changelog).

**Recommended change**: Update the placement description to match the template and live packages:
```
Every `gate_disposition` proposal MUST include a Gate Decision Record section after the Disposition Register and before the References and Changelog sections:
```

**Acceptance criterion**: The guideline's GDR placement rule matches the template structure (GDR → References → Changelog).

---

#### GAP-017: Client Decision Enum — Missing `pending`

**Target file**: `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
**Target section**: §VII.C — GDR Field Specification (line 231)

**Current state**:
```
| Client Decision | [APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT] |
```

**Contradicts**:
- §VII.D (line 253): `Client Decision: pending` (lifecycle text uses `pending`)
- Template (line 111): `[APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT / pending]` (template includes `pending`)

**Note on Reviewer Verdict**: The original gap report also flagged `N/A — decision gate` as missing from the template's Reviewer Verdict. This was resolved in template v1.3.0 (2026-03-16). No action needed for Reviewer Verdict.

**Recommended change**: Add `pending` to the Client Decision enum:
```
| Client Decision | [APPROVE / APPROVE WITH CONDITIONS / RECYCLE / REJECT / pending] |
```

**Acceptance criterion**: The guideline §VII.C Client Decision enum includes `pending` and matches the template and lifecycle text.

---

### Cluster C — Role/Gate Wording Fixes (TK006)

**Responsible role**: `LLM_Consultant` (governance surface updates)
**Target files**: 3 files

---

#### GAP-006: Role Authority Fragmentation (Localized Mitigation)

**Target file**: `prompt/artifacts/tasks/T104/ssot/sps_T104-CWS.md`
**Target section**: §III.B.1 — Organization & Responsibilities

**Current state**: Role authority is split across `sps_T104-CWS.md`, `sps_T102-CONSULTANT.md`, `prompt_main.md`, and individual workspace guidelines. No single surface fully defines the role contract used by the gate workflow, especially for `LLM_Reviewer` and Client decision ownership.

**Recommended change (localized mitigation only)**: Add a consolidated pointer note after the existing role/RACI tables in the SPS, directing readers to the authoritative role surfaces:

```markdown
**Role Authority Note**: The workspace role contract for T104 is distributed across multiple surfaces. For the definitive role-to-artifact ownership matrix, see `workspace_documentation_rules.md` §8. For gate-specific role boundaries (reviewer verdict, client GDR, developer evidence), see `guideline_workspace_verification.md` §II and `guideline_workspace_proposal.md` §VII. Full role consolidation into a single authoritative surface is deferred to AC004.
```

**Scope limitation**: This is a pointer-only mitigation. Full role authority consolidation is AC004 scope (GAP-011/012).

> **REFINED (SES002)**: GAP-006 full resolution is blocked on T101 initiative (not commissioned). The localized pointer note is acceptable as an informative flag. `workspace_documentation_rules.md` is the interim highest authority for roles and organization description until T101 is commissioned. Existing program-level development roles: `LLM_Consultant`, `LLM_Developer`, `LLM_Reviewer`, `LLM_Planner`, `Client`.

**Acceptance criterion**: SPS §III.B.1 contains a pointer directing readers to the distributed role authority surfaces. No role definition changes are made.

---

#### GAP-007: Consultant-Authored Task Registers

**Target file**: `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
**Target section**: §6.A — Consultant (LLM_Consultant) (line 103)

**Current state**:
```
- Boundary: MUST NOT author implementation-level task decomposition or execution proof.
```

**Observed evidence**: Live activity plans authored by `LLM_Consultant` (e.g., `plan_T104-PH001-ST008-AC003.md`, the AC003 plan itself) contain task registers with detailed task decomposition. This is contract-level task planning, not implementation-level execution. The plan guideline §IV.B defines task registers as a required activity field. The current wording in §6.A creates a false prohibition.

**Recommended change**: Refine the boundary text to distinguish contract-level task planning from implementation-level execution:
```
- Boundary: MUST NOT author implementation-level execution proof. Contract-level task registers and task decomposition in plans are within consultant scope per `guideline_workspace_plan.md` §IV.
```

**Acceptance criterion**: §6.A boundary text permits consultant-authored task registers in plans while maintaining the prohibition on implementation-level execution evidence.

---

#### GAP-008: Stale "Proposals Are Not Final Decisions" (**Pre-Resolved**)

**Target file**: `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
**Target section**: §10 — Anti-Drift Rules

**Current state (verified 2026-03-17)**: The stale sentence has already been removed. The current §10.C (line 208) reads:
```
- `gate_disposition` proposals host the authoritative Gate Decision Record (GDR) for gate closure decisions.
```

This is the correct post-AC001 wording. The fix was applied in `workspace_documentation_rules.md` v2.8.0 (2026-03-15) as part of the AC001.2 Gate-Readiness Stack work.

**Recommended change**: None. GAP-008 is **verified as pre-resolved**.

**Acceptance criterion**: Developer confirms that `workspace_documentation_rules.md` §10.C does not contain "proposals are not final decisions" or equivalent stale wording. Current text correctly identifies proposals as hosting the authoritative GDR.

---

### Cluster D — ADR Script Path Fixes (TK007)

**Responsible role**: `LLM_Developer` (script updates)
**Target files**: 2 files

> **RECLASSIFIED (SES002)**: Cluster D is reclassified as `deferred_to_T103`. Both ADR helper scripts (`print_t102_adr_005.py`, `print_t102_adr_007.py`) are deprecated and will be revised under the T103 initiative development. No implementation effort should be invested in AC003 scope. GAP-002 is flagged only.

---

#### GAP-002: ADR Helper Script Default Paths

**Target file 1**: `prompt/skills/t102-adr-005-id-spec/scripts/print_t102_adr_005.py`

**Current state (lines 9-10)**:
```python
DEFAULT_CONCEPT_PATH = Path(
    "prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md"
)
```

**Observed evidence**:
- The path `prompt/artifacts/tasks/T102/consultant/concept/` does **not exist** in the live repo.
- The live concept file is at `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`.
- However, the concept file does **not contain** the expected anchor `{#t102-adr-005-id-spec}` (confirmed by grep).
- The ADR-005 content (ID Specification Rules) has been extracted into a standalone standard file at `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md`.
- A prior research report (`T102-RES-006`) already documented this failure: `ERROR: ADR start marker not found: {#t102-adr-005-id-spec}`.

**Recommended change**: The developer must decide the retargeting strategy. Two options:

**Option A (Recommended)**: Retarget the script to read from the standalone standard file directly, replacing the concept-based extraction logic with a simple file read of `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md`. This eliminates the anchor dependency entirely.

**Option B**: Update `DEFAULT_CONCEPT_PATH` to the live concept path (`prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`) and add the expected anchor to the concept file. This preserves the extraction pattern but requires concept file modification.

**Consultant recommendation**: Option A. The standard files are the canonical authority post-extraction. Pointing at the standard directly avoids fragile anchor dependencies.

---

**Target file 2**: `prompt/skills/t102-adr-007-issues-risks-index/scripts/print_t102_adr_007.py`

**Current state (lines 9-10)**:
```python
DEFAULT_CONCEPT_PATH = Path(
    "prompt/artifacts/tasks/T102/consultant/concept/concept_T102-CONSULTANT.md"
)
```

**Same issues as Target file 1**: Non-existent default path, missing anchor `{#t102-adr-007-issues-risks-index}` in live concept.

**Live standard file**: `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`

**Recommended change**: Same retargeting strategy as GAP-002 Target file 1.

**Acceptance criterion**: Both ADR scripts use live path defaults that work without caller overrides. Scripts successfully retrieve the relevant standard content when invoked with default arguments.

---

## IV. AC003 / AC004 SCOPE BOUNDARY

### A. AC003 Scope (13 Gaps — This Activity)

GAP-001 through GAP-008, GAP-013 through GAP-017: localized guideline/template/script fixes as specified in Section III above.

### B. AC004 Scope (4 Gaps — Deferred)

| Gap ID | Category | Description | Notes |
|:--|:--|:--|:--|
| GAP-009 | `SPS-COVERAGE` | SPS initiative-level Research table uses older 4-column schema | **Observation**: This gap may have been pre-resolved by AC002 TK006, which normalized the SPS research table to the `T102-STD-006` 6-column schema (accepted via GATE-002 GIR-004). AC004 should verify current state before re-scoping. |
| GAP-010 | `SPS-COVERAGE` | `T104-IF-004` points status cadence to wrong standard (`T104-STD-003`) | AC004 scope — SPS schema correction |
| GAP-011 | `AGENTIC-INTEGRATION` | Documentation rules lack workflow chain, role matrix, linkage catalogue, agent rules | **Observation**: Partially pre-addressed by `workspace_documentation_rules.md` §7 and §8 added in v2.8.0 during AC001.2. AC004 should assess remaining coverage gap. |
| GAP-012 | `AGENTIC-INTEGRATION` | No explicit Links Register requirement or handoff bundle contract | AC004 scope — integration model work |

### C. Pre-Resolved Gaps (Verification Required)

| Gap ID | Pre-Resolution Source | AC003 Action |
|:--|:--|:--|
| GAP-008 | `workspace_documentation_rules.md` v2.8.0 (2026-03-15, AC001.2) | Developer confirms current state; no edit needed |
| GAP-001 | No in-scope files contain deprecated paths | Developer confirms via grep; no edit needed |
| GAP-017 (partial) | `template_workspace_proposal_gate-disposition.md` v1.3.0 (2026-03-16) added `N/A — decision gate` to Reviewer Verdict | Only the guideline §VII.C Client Decision enum needs `pending` added |

---

## V. DEPENDENCY SEQUENCING

### A. Inter-Cluster Dependencies

The 4 clusters are independent — no cluster's changes depend on another cluster's changes. They may be executed in any order.

### B. Recommended Execution Order

| Order | Cluster | Rationale |
|:--|:--|:--|
| 1 | A — NOTES | Self-contained; highest visibility naming drift; most files touched |
| 2 | B — Cross-refs | Largest cluster (6 gaps); touches the most guidelines |
| 3 | C — Role/gate | 1 of 3 gaps is pre-resolved; localized changes |
| 4 | D — Scripts | Separate developer ownership; self-contained |

### C. Intra-Cluster Dependencies

- **Cluster A**: GAP-005 Change 5 (guideline frontmatter) should be done last within Cluster A to capture an accurate version number reflecting the other NOTES changes.
- **Cluster B**: GAP-014 (naming authority) touches 3 files; no internal ordering dependency. GAP-016 and GAP-017 both touch `guideline_workspace_proposal.md` — apply them in a single edit pass.
- **Cluster C**: No internal dependencies.
- **Cluster D**: Both scripts share the same retargeting pattern; apply in parallel.

---

## VI. REFERENCES

| Document | Path |
|:--|:--|
| AC003 Activity Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC003/plan_T104-PH001-ST008-AC003.md` |
| T104-RES-003 Report | `prompt/artifacts/tasks/T104/research/T104-RES-003/report_T104-RES-003_workspace-artifact-integration-analysis.md` |
| AC002 Integration Analysis | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC002/analysis/analysis_T104-PH001-ST008-AC002_report-integration-and-downstream-impact.md` |
| Plan Guideline | `prompt/templates/consultant/workspace/guideline_workspace_plan.md` |
| Roadmap Guideline | `prompt/templates/consultant/workspace/guideline_workspace_roadmap.md` |
| Notes Guideline | `prompt/templates/consultant/workspace/guideline_workspace_notes.md` |
| Verification Guideline | `prompt/templates/consultant/workspace/guideline_workspace_verification.md` |
| Proposal Guideline | `prompt/templates/consultant/workspace/guideline_workspace_proposal.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Gate-Disposition Template | `prompt/templates/consultant/workspace/template_workspace_proposal_gate-disposition.md` |
| P-STD-004 (adopted standard) | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| T102-STD-005 (live standard) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md` |
| T102-STD-007 (live standard) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md` |

---

## VII. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-18 | Amendment | Relabeled all "Required change" to "Recommended change" (informative posture). Added Executive Summary governance disclaimer. Retracted `deferred` → `on_hold` recommendations (retained `deferred` pending P-STD-002 harmonization at `P-PH000-ST001-AC003-TK013`). Added `<INIT>` → `<SID>` alignment note (P-STD-005). Reclassified Cluster D as `deferred_to_T103`. Refined GAP-006 disposition (flag + defer to T101). |
| v1.0.0 | 2026-03-17 | Initial | Combined TK001 gap extraction + TK002 implementation specification. 13 AC003-scoped gaps mapped into 4 implementation clusters (A: NOTES, B: Cross-refs, C: Role/gate, D: Scripts). Key findings: GAP-008 pre-resolved in AC001.2; GAP-001 does not affect any in-scope target file; GAP-017 partially pre-resolved in template v1.3.0. Recommended execution order: A → B → C → D. |
