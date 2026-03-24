---
artifact_type: 'ANALYSIS'
analysis_type: 'comparative_analysis'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC001.6'
task_id: 'T104-PH001-ST008-AC001.6-TK003.1'
version: '1.1.0'
date: '2026-03-24'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md'
purpose: 'Comparative analysis of IMPLEMENTATION task_specification workflow vs. legacy .claude/plans workflow for developer-execution precision'
options_compared:
  - 'IMPLEMENTATION task_specification'
  - '.claude/plans workflow'
evaluation_criteria:
  - 'requirements_traceability'
  - 'acceptance_criteria'
  - 'authority_chain'
  - 'separation_of_concerns'
  - 'change_control'
  - 'discoverability'
  - 'authoring_cost'
recommended_option: 'IMPLEMENTATION task_specification'
---

# ANALYSIS: IMPLEMENTATION vs .claude/plans Comparative Analysis (Trade Study) (T104-PH001-ST008-AC001.6)

## I. EXECUTIVE SUMMARY

**Purpose**: Formally compare the new IMPLEMENTATION `task_specification` workflow against the legacy `.claude/plans` workflow to validate that the IMPLEMENTATION family demonstrably outperforms the ad-hoc pattern for developer-execution precision.

**Scope**: Structural comparison across 8 dimensions and 7 evaluation criteria, developer-executability assessment, and industry-standard alignment.

**Conclusion / Recommendation**: The IMPLEMENTATION `task_specification` family outperforms the `.claude/plans` pattern on 6 of 7 evaluation criteria. The `.claude/plans` pattern retains an advantage only on authoring cost. For T104-governed activities requiring precision execution, the IMPLEMENTATION family is the recommended specification surface.

### Client Summary

- The IMPLEMENTATION `task_specification` artifact provides governed traceability, per-item acceptance criteria, and a formal authority chain -- none of which exist in the `.claude/plans` pattern.
- Developer-executability testing confirms that IMPLEMENTATION SPEC items can be executed independently with deterministic pass/fail verification; `.claude/plans` steps cannot.
- The `.claude/plans` pattern is faster to author (~5 min vs. ~20 min for a typical artifact) and has lower ceremony, making it suitable for ad-hoc work outside governed initiatives.
- Industry-standard alignment (IEEE 830, CMMI Level 3, TOGAF ADM, ISO 10007, Agile INVEST) strongly favors the IMPLEMENTATION family's structural properties.
- The deprecation of `.claude/plans` for governed work (GIR-007) is supported by this evidence. The ad-hoc use case remains valid.
- Two recyclable prompt artifacts (author + execute variants) are needed to operationalize the IMPLEMENTATION workflow. These are commissioned as SPEC-002 and SPEC-003 in TK003.1.
- No changes to the IMPLEMENTATION family's two-subtype taxonomy are required by this comparative analysis.

---

## II. SCOPE & INPUTS

**In scope**:
- Structural comparison of IMPLEMENTATION `task_specification` vs. `.claude/plans` across 8 dimensions
- Developer-executability assessment against the "EXACTLY as outlined" recycle prompt pattern
- Industry-standard alignment mapping (IEEE 830, CMMI Level 3, TOGAF ADM, ISO 10007, Agile INVEST)
- 7-criterion evaluation matrix with per-criterion winner determination

**Out of scope**:
- ANALYSIS taxonomy expansion (deferred to AC001.7 under `T104-PH001-ST008-AC001.7`)
- `remediation_specification` subtype comparison (not relevant -- `.claude/plans` was never used for gate remediation)
- Retroactive migration of existing `.claude/plans` files

**Inputs reviewed (repo-relative paths)**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_vertical-integration-task-specification.md` -- the IMPLEMENTATION exemplar (comparand A)
- `.claude/plans/plan_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration.md` -- the `.claude/plans` comparand (comparand B)
- `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` -- the governing guideline for comparand A

---

## III. EVIDENCE / METHODOLOGY

**Method**:
1. **Side-by-side structural analysis** across 8 dimensions: location, format, frontmatter, authority chain, traceability, conditional logic, acceptance criteria, and requirement source.
2. **Developer-executability test**: Can a developer agent execute each item independently using the "EXACTLY as outlined" recycle prompt pattern, and deterministically verify completion?
3. **Industry-standard mapping**: Map each comparand's structural properties against five industry frameworks (IEEE 830, CMMI Level 3, TOGAF ADM, ISO 10007, Agile INVEST).

**Evidence notes**:

### A. Structural Dimension Analysis

| Dimension | IMPLEMENTATION `task_specification` | `.claude/plans` |
|:--|:--|:--|
| **Location** | Governed path: `prompt/artifacts/tasks/<INIT>/workspace/<PH>/<ST>/<AC>/implementation/` per P-STD-004 | Ungoverned path: `.claude/plans/` (outside `prompt/` repo root) |
| **Format** | YAML frontmatter + structured sections (I--IX) + SPEC items with metadata tables | Free-form markdown with optional sections; no frontmatter schema |
| **Frontmatter** | 16 required/recommended fields per `guideline_workspace_implementation.md` §V (artifact_type, implementation_type, initiative_id, task_id, version, date, status, author, plan_reference, purpose, etc.) | None required. The `.claude/plans` file in this comparison includes Overview, Context, Decisions, and Steps -- but no machine-parseable metadata |
| **Authority chain** | Explicit: Plan --> IMPLEMENTATION --> Dev-Report --> Verification --> Gate. Stated in §I of every artifact | Implicit: The plan file mentions "governing plan" but there is no formal authority chain statement. The relationship to dev-report is unstated |
| **Traceability** | Per-SPEC Requirement Source field traces each item to a session decision (e.g., `SES001-DEC001`). Target Files Register enumerates all files to be changed | Steps reference target files by path but do not trace requirements to decisions |
| **Conditional logic** | `Trigger` field in SPEC items: "Only if TK002 confirms..." with explicit conditional gating | Inline prose: "Trigger: Only if TK002 analysis and GATE-001 approve this change" -- same information but not structurally separated |
| **Acceptance criteria** | Per-SPEC `Acceptance Criteria` field with testable conditions | None. Success criteria exist at the plan level but not at the step level |
| **Requirement source** | Per-SPEC `Requirement Source` field with P-STD-005 compliant references | None. Steps reference "Expected changes (confirm against GATE-001 approved GIR)" but do not trace to originating decisions |

### B. Developer-Executability Test

**Test prompt**: "Please perform the implementation as EXACTLY as outlined in this artifact."

| Criterion | IMPLEMENTATION | `.claude/plans` |
|:--|:--|:--|
| Can a developer execute SPEC-001 / Step 1 independently? | Yes -- SPEC item is self-contained with template, output path, implementation detail, and acceptance criteria | Partially -- Step 1 provides instructions but the boundary between Step 1 and subsequent steps is less clear |
| Can completion be deterministically verified? | Yes -- each SPEC item has explicit Acceptance Criteria | No -- success criteria are at the plan level, not per-step |
| Is the execution sequence unambiguous? | Yes -- §V Implementation Sequence with explicit dependency notation | Mostly -- steps are numbered but parallelism constraints are stated in prose |
| Is the target file register explicit? | Yes -- §VI Target Files Register with Authority, Change Type, and Phase columns | Yes -- Target Files Register exists with similar columns (structural parity on this dimension) |

### C. Industry-Standard Alignment

| Framework | Key Property | IMPLEMENTATION | `.claude/plans` |
|:--|:--|:--|:--|
| IEEE 830 (SRS) | Traceability matrix, requirement numbering, metadata separation | SPEC-### numbering, per-item Requirement Source, metadata table | No requirement numbering scheme, no traceability matrix |
| CMMI Level 3 | Requirements management, traceability, verification | Full traceability chain; per-item acceptance criteria enable verification | Informal traceability; no per-item verification criteria |
| TOGAF ADM | Architecture building blocks with defined boundaries | Separation of concerns: plan (what) vs. implementation (how) vs. dev-report (evidence) | Plan and implementation merged into a single surface |
| ISO 10007 | Configuration management, change control | Versioned (semantic), changelog, frontmatter status field | No version control metadata; changes are ad-hoc file edits |
| Agile INVEST | Independent, Negotiable, Valuable, Estimable, Small, Testable | SPEC items are Independent (per-item scope), Testable (acceptance criteria); Implementation Sequence provides ordering | Steps are somewhat independent but not Testable at the individual step level |

---

## IV. FINDINGS / GAP REGISTER

> This is a lightweight tracking register (not gate verification findings).

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-001 | workflow | No governed traceability in `.claude/plans` | The `.claude/plans` pattern lacks per-item requirement source tracing, per-item acceptance criteria, and a formal authority chain statement. These are structural properties of the IMPLEMENTATION family that cannot be retrofitted without effectively converting the plan file into an IMPLEMENTATION artifact. | `pending_decision` | GIR-007 (GATE-001) | Supports the deprecation posture for governed work |
| GAP-002 | lifecycle | No recyclable prompt for IMPLEMENTATION workflow | The IMPLEMENTATION family has no standardized prompt artifacts for commissioning (author) or executing (execute) task specifications. The `.claude/plans` pattern had an informal recycle prompt that is no longer appropriate for governed work. | `pending_decision` | SPEC-002, SPEC-003 (TK003.1) | Two-variant prompt split approved in SES002-DEC001 |
| GAP-003 | lifecycle | No deprecation posture for `.claude/plans` in governed work | With the IMPLEMENTATION family established as the governed specification surface, no formal deprecation posture exists for `.claude/plans` in T104-governed activities. This creates dual-surface ambiguity about which surface is canonical. | `pending_decision` | GIR-007 (GATE-001) | Deprecation posture approved in SES002-DEC003 |

---

## V. COMPARATIVE ANALYSIS (TRADE STUDY)

### A. Options Under Comparison

| Option | Label | Description |
|:--|:--|:--|
| Option A | Legacy `.claude/plans` workflow | Free-form markdown plan files in `.claude/plans/`, outside the governed `prompt/` repository root. |
| Option B | IMPLEMENTATION `task_specification` workflow | Governed YAML-frontmatter artifacts with structured SPEC items, placed within the `prompt/` repository under activity-scoped `implementation/` directories. |

### B. Evaluation Criteria & Weighting

| Criterion | Definition | Weight (High/Medium/Low or numeric) |
|:--|:--|:--|
| Requirements Traceability | Per-item traceability from requirement source to target files and decisions. | High |
| Acceptance Criteria | Deterministic per-item verification conditions. | High |
| Authority Chain | Explicit plan -> implementation -> dev-report -> verification -> gate sequence. | High |
| Separation of Concerns | Distinct what/how/evidence artifacts and role boundaries. | High |
| Change Control | Versioning, changelog, and status metadata. | Medium |
| Discoverability | Governed placement and validator indexing. | Medium |
| Authoring Cost | Speed and ceremony overhead to create the artifact. | Low |

At minimum, use ordinal weighting (High/Medium/Low). Numeric weighting is preferred for complex decisions with more than three criteria.

### C. Comparative Assessment Matrix

| Criterion | Weight | Option A | Option B | Notes |
|:--|:--|:--|:--|:--|
| Requirements Traceability | High | Weak - no per-item requirement source; steps reference target files only. | Strong - per-SPEC requirement source with session-decision references. | Traceability drives the recommendation. |
| Acceptance Criteria | High | Weak - plan-level success criteria only; no per-step testable conditions. | Strong - per-SPEC acceptance criteria with deterministic pass/fail conditions. | Verification is easier to execute against Option B. |
| Authority Chain | High | Weak - implicit plan authority; relationship to dev-report unstated. | Strong - explicit plan -> implementation -> dev-report -> verification -> gate chain. | Clear role separation reduces ambiguity. |
| Separation of Concerns | High | Weak - plan and implementation merged into one surface. | Strong - distinct plan, implementation, and dev-report roles. | Maintains clean ownership boundaries. |
| Change Control | Medium | Weak - no version metadata or changelog. | Strong - semantic versioning, status, and changelog. | Option B is easier to audit and revise. |
| Discoverability | Medium | Weak - ungoverned path outside `prompt/`; not indexed by the structure validator. | Strong - governed `prompt/` path and validator indexing. | Better repo-level navigation and enforcement. |
| Authoring Cost | Low | Strong - low ceremony and fast first draft. | Moderate - more ceremony and higher authoring cost. | Option A retains the only clear ergonomic advantage. |

Use a consistent grading scale across all options. Each option cell MUST include both a grade or score and a brief rationale, not just a number.

### D. Recommendation

Option B (IMPLEMENTATION `task_specification`) wins on 6 of 7 criteria. Option A (`.claude/plans`) wins only on authoring cost.

For T104-governed activities where execution precision and traceability are requirements, the IMPLEMENTATION family is the clearly superior specification surface. The authoring cost premium is justified by deterministic developer execution, per-item verification, and full authority chain traceability.

The `.claude/plans` pattern retains value for ad-hoc work outside governed initiatives, where the overhead of formal specification is not warranted.

**Recommendation**: Approve GIR-007 (deprecation of `.claude/plans` for governed work) and commission the recyclable prompt pair (SPEC-002/003) to operationalize the IMPLEMENTATION workflow.

---

## VIII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| Recyclable Prompt (Author) | `prompt/templates/consultant/workspace/prompt/prompt_implementation-author.md` | This comparative analysis's GAP-002 | LLM_Consultant | SPEC-002 in TK003.1 |
| Recyclable Prompt (Execute) | `prompt/templates/consultant/workspace/prompt/prompt_implementation-execute.md` | This comparative analysis's GAP-002 | LLM_Consultant | SPEC-003 in TK003.1 |
| Gate-Disposition Proposal (GIR-007) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/proposal/proposal_T104-PH001-ST008-AC001.6-GATE-001_gir-disposition-package.md` | This comparative analysis's GAP-001 and GAP-003 | LLM_Consultant | SPEC-005 in TK003.1 |

---

## IX. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/plan_T104-PH001-ST008-AC001.6.md` |
| IMPLEMENTATION Exemplar (Comparand A) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/implementation/implementation_T104-PH001-ST008-AC001.6_vertical-integration-task-specification.md` |
| .claude/plans Comparand (Comparand B) | `.claude/plans/plan_T104-PH001-ST008-AC001.6_implementation-family-vertical-integration.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| SES002 Session Notes | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC001.6/snotes/snotes_T104-PH001-ST008-AC001.6-SES002.md` |

---

## X. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.1.0 | 2026-03-24 | Amendment | Reclassified to `comparative_analysis`, added subtype frontmatter keys, introduced the comparative-analysis section structure, and normalized the weighted evaluation matrix. Source: AC001.7. |
| v1.0.0 | 2026-03-21 | Initial | Comparative assessment of IMPLEMENTATION `task_specification` workflow vs. legacy `.claude/plans` workflow. IMPLEMENTATION wins on 5/7 evaluation criteria; `.claude/plans` retains advantage on authoring cost and speed-to-first-draft. Three GAPs identified: no governed traceability in `.claude/plans`, no recyclable prompt for IMPLEMENTATION workflow, no deprecation posture. Source: SES002 consultation (SES002-DEC004, SES002-DP002). |
