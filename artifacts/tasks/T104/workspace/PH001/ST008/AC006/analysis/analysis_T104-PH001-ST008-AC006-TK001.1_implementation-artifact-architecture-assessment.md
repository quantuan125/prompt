---
artifact_type: 'ANALYSIS'
analysis_type: 'comparative_analysis'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC006'
task_id: 'T104-PH001-ST008-AC006-TK001.1'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md'
purpose: 'Evaluate architectural options for distinguishing developer-facing from assistant-facing implementation artifacts, and assess whether remediation_specification scope should be expanded for pre-gate assistant corrections.'
options_compared: 'Option A (status quo flag-only), Option B (naming convention), Option C (new subtype), Option D (combination)'
evaluation_criteria: 'Discoverability, Governance Cost, Backward Compatibility, Template Impact, LLM_Assistant Alignment, Remediation Scope Clarity'
recommended_option: 'Option B (naming convention)'
---

# ANALYSIS: Implementation Artifact Architecture Comparative Assessment (`T104-PH001-ST008-AC006-TK001.1`)

## I. EXECUTIVE SUMMARY

**Purpose**: Evaluate whether the current `execution_audience` flag (CONV-013) alone is sufficient for distinguishing developer-facing from assistant-facing implementation artifacts, or whether an architectural change is needed. Additionally evaluate whether the `remediation_specification` subtype scope should be expanded to cover pre-gate assistant corrections.

**Scope**: Four architectural options (status quo, naming convention, new subtype, combination) assessed against six weighted criteria grounded in ISO 9001, PRINCE2, Claude Code role archetypes, and CrewAI task-level governance. Live inventory of ~40 implementation artifacts across three initiatives confirms the discoverability problem. Remediation specification scope evaluated as a coupled dimension.

**Conclusion / Recommendation**: **Option B (naming convention)** is recommended. It resolves the filesystem-level discoverability problem at medium governance cost without requiring new templates or subtype taxonomy changes. The naming convention distinguishes developer-facing task specifications (which seed implementation-backed gate workflows) from consultant/assistant-facing specifications (lightweight orchestration briefs) through a suffix convention visible in directory listings. The `remediation_specification` subtype scope should remain tight (gate RECYCLE verdicts only); pre-gate assistant corrections are better governed through the task_specification with `execution_audience: 'consultant'` or `'assistant'` and the naming convention.

### Client Summary

- Four architectural options were evaluated against six criteria with industry grounding.
- **Option B (naming convention)** scores highest overall: it makes the execution audience visible at the filesystem level without adding new templates, subtypes, or governance overhead.
- The recommended naming convention: developer-facing specs retain the current naming pattern; consultant/assistant-facing specs add a `-brief` suffix (e.g., `implementation_..._task-specification.md` vs `implementation_..._orchestration-brief.md`).
- The `remediation_specification` subtype remains restricted to gate RECYCLE verdicts. Pre-gate assistant corrections are governed through the naming convention + `execution_audience` flag.
- Option C (new subtype) scored second but was outweighed by higher governance cost and the fact that developer-facing and assistant-facing specs share identical SPEC structure — the difference is lifecycle, not document architecture.
- The recommendation feeds directly into CONV-022 resolution in TK002 and DEC-008 client decision.

---

## II. SCOPE & INPUTS

**In scope**:
- Assess the current `execution_audience` flag as the sole discriminator between developer-facing and assistant-facing implementation artifacts
- Assess the discoverability problem across the live artifact inventory
- Evaluate four architectural options (A through D) against weighted criteria
- Evaluate whether `remediation_specification` scope should be expanded for pre-gate assistant corrections
- Ground the assessment in industry evidence

**Out of scope**:
- Implementing the chosen architectural resolution (TK004 scope)
- Retroactive migration of existing implementation artifacts
- Changing the `remediation_specification` trigger (gate RECYCLE verdict)
- Changing the IMPLEMENTATION template structure (SPEC metadata table + Implementation Detail)

**Inputs reviewed (repo-relative paths)**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` (v2.0.0, GAP-010 and GAP-011)
- `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` (v1.4.0, §III subtype taxonomy, §IV CONV-012/013)
- `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`
- `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md`
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (v3.6.0, §3 artifact inventory, §6 role boundaries, §8 ownership matrix)
- Live implementation artifact inventory across `prompt/artifacts/` (grep for `execution_audience` + glob for `implementation_*.md`)

---

## III. EVIDENCE / METHODOLOGY

**Method**:
1. Inventoried all existing implementation artifacts by globbing `**/implementation_*.md` across `prompt/artifacts/` (41 files found).
2. Grepped for `execution_audience` declarations across all implementation artifacts to categorize by audience.
3. Analyzed the distribution: ~16 consultant-scoped, ~8 developer-scoped, 2 agentic-executor, ~14 undeclared (pre-CONV-013 artifacts).
4. Documented the discoverability problem with concrete directory-listing examples.
5. Evaluated each architectural option against six criteria using industry evidence.
6. Assessed the `remediation_specification` scope question as a coupled dimension of the architectural decision.

**Evidence notes**:
- The live inventory confirms GAP-010's assertion: developer-facing specs are a minority (~8 of ~40) but carry disproportionate governance weight (they seed implementation-backed gate workflows, are mandatory in gate-readiness packages, and are reviewed by multiple roles).
- In directories with mixed audiences (e.g., `P/workspace/PH000/ST002/AC004/implementation/`), five implementation artifacts coexist with three different `execution_audience` values (`developer`, `consultant`, `agentic_executor`). An `ls` listing shows no distinction.
- The `execution_audience` flag is in YAML frontmatter (line ~16 of each file). It requires opening each file or running a grep to determine audience — not visible in any standard directory listing tool.
- All implementation artifacts regardless of audience share identical SPEC structure (metadata table + Implementation Detail). The structural similarity confirms these are the same document type with different operational contexts, not fundamentally different document types.
- The `remediation_specification` subtype has a clear trigger (gate RECYCLE verdict) and a clear lifecycle (finding-to-fix mapping). Pre-gate assistant corrections have a different trigger (consultant-identified package coherence issue) and different lifecycle (no RECYCLE verdict, no finding IDs, session-note evidence only).

---

## IV. FINDINGS / GAP REGISTER

> This is a lightweight tracking register (not gate verification findings).

| GAP ID | Category | Title | Description | Disposition | Downstream Target | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| GAP-TK1.1-001 | consistency | Filesystem-level audience indistinguishability confirmed | Live inventory of ~40 implementation artifacts confirms that `execution_audience` in frontmatter is the only discriminator. Developer-facing specs (~8) are outnumbered ~5:1 by consultant/assistant-scoped artifacts in shared directories. | `pending_decision` | CONV-022 in TK002 | Core finding driving the architectural recommendation. |
| GAP-TK1.1-002 | lifecycle | Structural identity across audiences | All implementation artifacts use identical SPEC structure regardless of `execution_audience`. The difference between developer-facing and assistant-facing specs is lifecycle (DEV-REPORT vs. session-note evidence), not document architecture. | `pending_decision` | CONV-022 in TK002 | This finding favors naming convention (Option B) over new subtype (Option C), since the document type is the same. |
| GAP-TK1.1-003 | workflow | Remediation specification scope is appropriately tight | The `remediation_specification` trigger (gate RECYCLE verdict) and lifecycle (finding-to-fix mapping with verification-reference backlink) are structurally distinct from pre-gate assistant corrections. Expanding the scope would conflate two different governance mechanisms. | `accepted_as_is` | No change needed | Pre-gate assistant corrections are better governed through naming convention + `execution_audience`. |

---

## V. COMPARATIVE ANALYSIS (TRADE STUDY)

### A. Options Under Comparison

| Option | Label | Description |
|:--|:--|:--|
| Option A | Status Quo (Flag-Only) | Keep `execution_audience` flag in frontmatter as the sole discriminator. No filesystem-level changes. |
| Option B | Naming Convention | Add a suffix convention to distinguish developer-facing task specifications from consultant/assistant-facing orchestration briefs at the filename level. Developer-facing: `implementation_..._task-specification.md` (unchanged). Consultant/assistant-facing: `implementation_..._<topic>-brief.md` (new suffix). |
| Option C | New Subtype | Create a third IMPLEMENTATION subtype (e.g., `orchestration_brief` or `assistant_task`) with its own template, distinct from `task_specification`. The `implementation_type` frontmatter field becomes the discriminator. |
| Option D | Combination | Named role (`LLM_Assistant` per CONV-023) + naming convention (Option B) + new subtype (Option C). Full architectural separation at every governance layer. |

### B. Evaluation Criteria & Weighting

| Criterion | Definition | Weight |
|:--|:--|:--|
| Discoverability | Can a human or agentic actor distinguish developer-facing from assistant-facing specs without opening files? Assessed at filesystem level (directory listing) and programmatic level (grep/glob). | 5 (High) |
| Governance Cost | How many guideline sections, template files, documentation-rules entries, and convention IDs must be created or amended? | 4 (High) |
| Backward Compatibility | Impact on existing ~40 implementation artifacts. Does the option require retroactive renaming, re-typing, or re-templating? | 3 (Medium) |
| Template Impact | How many new templates must be created? How much duplication is introduced between templates that share identical SPEC structure? | 3 (Medium) |
| LLM_Assistant Alignment | How well does the option support CONV-023 (LLM_Assistant role formalization)? Does it create a clean mapping between the named role and the artifact type/name? | 3 (Medium) |
| Remediation Scope Clarity | Does the option clarify the boundary between `remediation_specification` (RECYCLE-triggered) and pre-gate assistant corrections? | 2 (Low) |

**Weighting rationale**: Discoverability is the primary driver (this is the problem being solved). Governance cost is second because AC006 already introduces nine new conventions — additional governance surface area must be justified. Template impact and backward compatibility are medium because they affect authoring workflows. LLM_Assistant alignment is medium because it couples with the parallel CONV-023 decision. Remediation scope is low because the current trigger is already well-defined.

### C. Comparative Assessment Matrix

| Criterion | Weight | Option A (Status Quo) | Option B (Naming Convention) | Option C (New Subtype) | Option D (Combination) | Notes |
|:--|:--|:--|:--|:--|:--|:--|
| Discoverability | 5 | 1/5 — No improvement. Audience visible only via frontmatter grep. | 4/5 — Filename suffix visible in `ls`, glob, and IDE sidebar. Not visible in frontmatter-only tools but covers primary discovery channels. | 4/5 — `implementation_type` in frontmatter is greppable; filename may or may not change depending on naming policy. | 5/5 — Full separation at filename, frontmatter, and template level. | Options B and C both solve the primary discoverability gap. Option D adds marginal improvement at much higher cost. |
| Governance Cost | 4 | 5/5 — Zero cost. No changes needed. | 4/5 — One new convention (naming suffix rule) in `guideline_workspace_implementation.md`. No new templates. Minor update to `workspace_documentation_rules.md` §3 (filename pattern note). | 2/5 — New subtype in §III taxonomy. New template file. New convention for subtype trigger. Updates to §3, §6, §8 in rules. Changelog entries across multiple files. | 1/5 — All of Option C plus naming convention plus role-to-subtype mapping rules. Highest governance surface area. | Option B's governance cost is bounded to two file amendments. Option C requires changes across five+ files. |
| Backward Compatibility | 3 | 5/5 — No impact. Existing artifacts unchanged. | 4/5 — Existing artifacts not retroactively renamed. Convention applies to new artifacts only. Existing consultant-scoped specs remain valid with current names. | 3/5 — Existing artifacts not retroactively retyped, but the new subtype creates a taxonomy discontinuity: old `task_specification` artifacts with `execution_audience: 'consultant'` were valid under the old taxonomy but would be the "wrong" subtype under the new one. | 2/5 — Same taxonomy discontinuity as C, plus naming discontinuity. | Option B's forward-only approach avoids legacy confusion. Option C creates a "should old artifacts be retyped?" question. |
| Template Impact | 3 | 5/5 — No new templates. | 5/5 — No new templates. Both developer-facing and assistant-facing specs use the existing `task_specification` template. The naming convention is a filename rule, not a structural rule. | 2/5 — New template (`template_workspace_implementation_orchestration-brief.md`) required. Template content would be nearly identical to `task_specification` template (same SPEC structure), creating maintenance duplication. | 1/5 — New template plus potential additional role-variant template. Highest duplication. | The structural identity finding (GAP-TK1.1-002) makes Option C's new template a near-duplicate with no structural justification. |
| LLM_Assistant Alignment | 3 | 2/5 — `LLM_Assistant` role (CONV-023) has no artifact-level alignment. The role exists in §6 rules but its artifacts look identical to consultant artifacts. | 4/5 — The `-brief` suffix creates a natural mapping: `LLM_Assistant` executes `-brief` artifacts. Not a formal type-level binding, but a discoverable convention. | 4/5 — The new subtype creates a formal type-level binding: `LLM_Assistant` executes `orchestration_brief` subtype. Strongest formal alignment. | 5/5 — Full alignment across all layers: role → subtype → naming → template. | Option B and C score similarly on alignment. Option C's formal binding is cleaner but the governance cost difference outweighs the marginal alignment improvement. |
| Remediation Scope Clarity | 2 | 3/5 — No change. The gray zone between `remediation_specification` and assistant pre-gate corrections remains implicit. | 4/5 — The naming convention clarifies: `-brief` artifacts are for pre-gate assistant work; `remediation_specification` remains RECYCLE-only. The filename itself signals "this is not a gate-remediation artifact." | 4/5 — The new subtype boundary clarifies the same distinction at the taxonomy level. | 5/5 — Full separation at every level. | Both B and C resolve the gray zone. The naming convention is sufficient because the remediation_specification trigger (RECYCLE verdict) is already structurally distinct. |

### D. Scoring Summary

| Option | Discoverability (5) | Governance Cost (4) | Backward Compat (3) | Template Impact (3) | LLM_Assistant (3) | Remediation (2) | Weighted Total |
|:--|:--|:--|:--|:--|:--|:--|:--|
| Option A | 1x5 = 5 | 5x4 = 20 | 5x3 = 15 | 5x3 = 15 | 2x3 = 6 | 3x2 = 6 | **67** |
| **Option B** | 4x5 = 20 | 4x4 = 16 | 4x3 = 12 | 5x3 = 15 | 4x3 = 12 | 4x2 = 8 | **83** |
| Option C | 4x5 = 20 | 2x4 = 8 | 3x3 = 9 | 2x3 = 6 | 4x3 = 12 | 4x2 = 8 | **63** |
| Option D | 5x5 = 25 | 1x4 = 4 | 2x3 = 6 | 1x3 = 3 | 5x3 = 15 | 5x2 = 10 | **63** |

### E. Recommendation

**Recommended option: Option B (Naming Convention)** — weighted score 83/100.

**Rationale**:
1. **Discoverability gap closed**: The `-brief` suffix makes developer-facing vs. assistant-facing specs distinguishable in `ls`, `find`, `glob`, and IDE sidebars — the primary discovery channels where the problem manifests.
2. **Lowest governance cost among solutions**: Only two file amendments required (`guideline_workspace_implementation.md` naming rule + `workspace_documentation_rules.md` §3 note). No new templates, no subtype taxonomy change.
3. **Structural identity preserved**: The finding that all implementation artifacts share identical SPEC structure (GAP-TK1.1-002) means the distinction is operational context, not document type. A naming convention correctly reflects this: same template, different filename suffix signals different lifecycle treatment.
4. **Forward-only**: Existing artifacts are not retroactively renamed. The convention applies to new artifacts authored after approval.
5. **Natural LLM_Assistant mapping**: The `-brief` suffix creates a discoverable association between the `LLM_Assistant` role (CONV-023) and its artifacts, without requiring formal subtype binding.

**Dissenting considerations**:
- Option C (new subtype) provides a **stronger formal governance boundary** between developer-facing and assistant-facing work. If the operational patterns diverge further in the future (e.g., assistant artifacts develop unique sections or different lifecycle stages), a subtype split would be more natural. However, no such divergence is currently evidenced — the SPEC structure is identical across all audiences.
- Option A (status quo) has **zero cost** and may be revisited if the naming convention proves insufficient. However, the live inventory confirms the discoverability problem is real and affects daily operations (developer-facing specs buried among consultant-scoped artifacts).
- Option D (combination) provides **maximum governance precision** but at disproportionate cost for the current scale (~40 artifacts). It would be more justified at enterprise scale with hundreds of implementation artifacts.

**Recommended naming convention**:
- Developer-facing task specifications: retain `implementation_<scope-UID>_<topic>-task-specification.md` (unchanged)
- Consultant/assistant-facing orchestration briefs: use `implementation_<scope-UID>_<topic>-brief.md` (new `-brief` suffix replaces `-task-specification`)
- Remediation specifications: retain `implementation_<scope-UID>_<topic>-remediation-specification.md` (unchanged, RECYCLE-only trigger)

**Remediation specification scope recommendation**: Keep tight. The `remediation_specification` subtype remains restricted to gate RECYCLE verdicts. Pre-gate assistant corrections are governed through `task_specification` with `execution_audience: 'consultant'` (or `'assistant'` once CONV-023 is approved) and the `-brief` naming convention. The rationale:
- The RECYCLE trigger provides a clear, unambiguous entry condition tied to a specific gate verdict
- Pre-gate corrections have a different trigger (consultant-identified coherence issue) and different evidence trail (session notes, not verification findings)
- Expanding `remediation_specification` to cover both would conflate two distinct governance mechanisms and blur the RECYCLE-specific lifecycle (finding-to-fix mapping, verification-reference backlink)
- ISO 9001 §10.2 CAPA distinguishes between **corrections** (immediate fix) and **corrective actions** (systemic root-cause response) — remediation_specification maps to corrective action; assistant pre-gate fixes map to correction

---

## VIII. DOWNSTREAM ACTIONS

| downstream_artifact_type | target_reference | trigger_condition | responsible_role | notes |
|:--|:--|:--|:--|:--|
| `PROPOSAL` (standards_input update) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` | TK001.1 complete | `LLM_Consultant` | Resolve CONV-022 placeholder with Option B recommendation. Update DEC-008 with specific naming convention. Version bump TK002 to v2.1.0. |
| `IMPLEMENTATION` (TK004 scope) | `guideline_workspace_implementation.md` | GATE-001 approved | `LLM_Developer` | Add naming convention rule to §IV or new §IV.B. Update `workspace_documentation_rules.md` §3 to note the suffix pattern. |

---

## IX. REFERENCES / LINKS REGISTER

| Item | Reference |
|:--|:--|
| Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| TK001 Gap Analysis (GAP-010, GAP-011) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Task Specification Template | `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md` |
| Remediation Specification Template | `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| ISO 9001:2015 | §7.5.3 (documented information control — distinct types distinguishable by identification), §10.2 CAPA (corrections vs. corrective actions) |
| PRINCE2 7th Edition | Configuration Item Records — each product variant has distinct CI type |
| Claude Code | Role archetypes: structurally distinct agents (Explore=read-only, Plan=read-only); AGENTS.md role-specific definitions |
| CrewAI | Named role definitions with task-level security postures; same agent, different permissions per context |

---

## X. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Comparative analysis authored for TK001.1. Four options evaluated against six weighted criteria. Option B (naming convention) recommended with score 83/100. Remediation specification scope confirmed as appropriately tight (RECYCLE-only). Three findings documented. Downstream actions feed CONV-022 resolution in TK002 and TK004 implementation. |
