---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T104'
initiative_code: 'CWS'
phase: '1'
stream_id: 'T104-PH001-ST008'
activity_id: 'T104-PH001-ST008-AC006'
task_id: 'T104-PH001-ST008-AC006 (multi-task scope: TK001 update, TK002 update, plan amendment for TK001.1)'
version: '1.0.0'
date: '2026-03-28'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md'
execution_audience: 'consultant'
purpose: 'Integrate industry-standard and agentic-environment research findings into TK001 (governance gap analysis) and TK002 (standards-input proposal), amend the AC006 activity plan to add TK001.1 (implementation artifact architecture comparative analysis), and update the plan task register and version to reflect session progress.'
---

# IMPLEMENTATION (Task Specification): Governance Hardening Research Integration & Plan Amendment

## I. PURPOSE & AUTHORITY

- **Purpose**: This artifact specifies the exact file mutations required to: (1) strengthen TK001 with industry-standard and agentic-environment evidence grounding; (2) strengthen TK002 with industry citations, revised CONV-018 risk-based threshold, new conventions CONV-022/CONV-023, enforcement modalities section, and external references; (3) amend the AC006 activity plan to add task TK001.1 and update the task register.
- **Authority chain**: The governing activity plan (`plan_T104-PH001-ST008-AC006.md`) authorizes this work at the AC006 activity level. This artifact specifies HOW the research integration and plan amendment are performed. Execution evidence for this work is captured via the plan changelog entries and session notes (consultant-owned work, no dev-report required).
- **Audience**: `LLM_Consultant` (execution_audience: consultant). This is consultant-owned analytical and plan-authoring work. No developer execution or dev-report is required.
- This artifact does NOT hold a GDR. Gate decisions are recorded in gate_disposition proposals per `guideline_workspace_proposal.md` Section VII.

## II. TASK SCOPE

- **Governing plan task**: `T104-PH001-ST008-AC006` (multi-task scope: TK001 v1→v2, TK002 v1→v2, plan v1→v2)
- **Trigger**: Client review of TK001 and TK002 v1.0.0 drafts identified insufficient industry-standard grounding and agentic-environment evidence. Client also raised four architectural concerns (Implementation Detail cross-model quality, implementation artifact discoverability, remediation specification scope, developer vs. assistant subagent role distinction) requiring new gaps, conventions, and a comparative analysis task.
- **Deliverable contract**: (1) TK001 gap analysis updated to v2.0.0 with industry/agentic grounding and three new gaps; (2) TK002 standards-input proposal updated to v2.0.0 with industry citations, revised CONV-018, new conventions, enforcement modalities, and external references; (3) AC006 activity plan updated to v2.0.0 with TK001.1 task, updated task register, and expanded TK004 deliverable list.

## III. SPECIFICATION ITEMS

### SPEC-001 -- Update TK001 Gap Analysis: Add Industry & Agentic Evidence Base (Section III)

| Field | Detail |
|:--|:--|
| Requirement Source | Client feedback: "lack of industry-standard perspective and best practices for both deliverables" |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` |
| Required end-state posture | Section III (Evidence/Methodology) contains a sixth method step and a new subsection §III.B with a per-gap industry/agentic grounding table |
| Explicit non-target / do-not-change constraints | Do NOT modify Section I (Executive Summary) or Section II (Scope & Inputs) at this step. Do NOT modify the existing five method steps — append only. |
| Validation check | (1) Method step 6 exists after step 5; (2) §III.B subsection exists with a table containing one row per original gap (GAP-001 through GAP-008); (3) Each row contains both a traditional standard citation and an agentic pattern citation |
| Blocking ambiguity rule | If the file has been modified since v1.0.0, STOP and re-read before applying mutations |
| Status | `open` |

#### Implementation Detail

**Step 1: Append method step 6 after line 86**

After the line `5. Bounded each gap to the exact file(s) and section(s) that require amendment, then identified the governance direction that would close the gap permanently.`, append:

```markdown
6. Cross-referenced each gap against traditional process standards (IEEE, ISO, CMMI, PRINCE2, FDA, DO-178C, AS9100D) and modern agentic-environment patterns (Claude Code, Codex CLI, CrewAI, NIST AI RMF, AURA framework) to validate governance direction and identify enforcement models.
```

**Step 2: Insert new subsection §III.B after the Evidence notes block (after line 95)**

After the line ending with `...the commissioning rule for governed delegated execution is implicit rather than explicit.`, insert:

```markdown

### B. Industry & Agentic Evidence Base

| GAP ID | Traditional Standard Grounding | Agentic Environment Grounding |
|:--|:--|:--|
| GAP-001 | IEEE 29148 §5: completeness, verifiability, traceability attributes for requirements; CMMI-DEV RD: entry/exit criteria for work products; PRINCE2 Work Package: minimum content (Product Description, tolerances, constraints, approval methods); SAFe/Scrum Definition of Ready: team-agreed checklist before sprint entry | Claude Code context-amnesia: subagents start fresh — brief must be self-contained; Codex PM pattern: `REQUIREMENTS.md` as single source of truth — "Do not assume anything not written here"; AGENTIF benchmark (Tsinghua): LLMs fail on dense multi-constraint specs due to in-context learning limits |
| GAP-002 | Fagan Inspection: per-item checklist review (structured examination of each requirement); ISO/IEC 20246: item-level examination across review types; FDA 21 CFR 820.30(c): per-design-input completeness assessment; DO-178C §6.3/Table A-3: per-requirement traceability — gaps are certification findings | Claude Code PreToolUse hooks: approve/deny per-action enforcement; CodeRabbit agentic validation: ~46% bug detection in sandboxed per-item review; Codex schema validation of outputs |
| GAP-003 | ISO 9001 §7.5.3: only approved current-revision documents in circulation; ISO 10007/IEEE 828: configuration baseline as single reference point; PRINCE2 Configuration Item Record: status tracking (draft/reviewed/approved) | CrewAI hierarchical authority with `allowed_agents`; AutoGen GroupChat with selector; Academic (ACM 2025): multi-agent conflict resolution remains an open research problem |
| GAP-004 | PRINCE2 Work Package authorization: formal artifact with mutual acceptance before work commences; ITIL Service Design Package: formal handover from Design to Transition; Toyota Production System: standardized work instructions; MIL-STD-1521B: phase-gating through specification artifacts | Claude Code Agent tool prompt as sole delegation channel; Codex+Agents SDK PM-gated pipeline with file-based gating; Microsoft Cloud Adoption Framework: "handoff artifacts (plans, checklists, traces)" as commissioning medium |
| GAP-005 | ISO 9001 §8.7: nonconforming output segregation/containment; Configuration Management baselines: unapproved = no authority; ITIL Release Management: CAB as change authority boundary; FDA 21 CFR Part 11: draft vs approved status legally mandated | Claude Code worktree isolation: `--worktree` prevents draft contamination; Codex sandboxed workspace; GitHub agentic workflows: PRs never merge automatically; Artifact-first pattern: frontmatter status tracking |
| GAP-006 | ISO 9001 §10.2 CAPA: documented nonconformity + actions + results retained; AS9100D §10.2: most rigorous per-finding tracking in aerospace; CMMI VER: defects tracked, analyzed for patterns, used for process improvement; PRINCE2: Issue Register + Quality Register + CIR cross-referencing | Claude Code Session Memory: auto-compaction with background summaries; Continuous-Claude ledger pattern: "compound, don't compact"; Amazon Bedrock AgentCore: chronological event storage with intelligent consolidation |
| GAP-007 | ISO 27001 Annex A 5.12/5.13: classification + metadata-based labeling; RACI matrix: exactly one Accountable per row; PRINCE2 Communication Management Approach: audience mapping per artifact; ITIL Knowledge Management: layered information for different consumer groups | Claude Code tool allowlists/denylists per subagent role; Built-in role archetypes (Explore=read-only, Plan=read-only); Academic (arXiv 2511.08475): Role-Based Cooperation most frequently employed pattern (94.7% of systems) |
| GAP-008 | ISO 9001 §7.5.3: obsolete document prevention; IEEE 828 baseline management: only baselined artifacts are authoritative | Claude Code AGENTS.md: role-specific agent definitions with distinct tool restrictions; CrewAI task-level security postures: same agent, different permissions per context |
```

---

### SPEC-002 -- Update TK001 Gap Analysis: Add Three New Gaps (GAP-009, GAP-010, GAP-011)

| Field | Detail |
|:--|:--|
| Requirement Source | Client QA comments 1.1, 2, 2.1, 4: Implementation Detail cross-model quality, implementation artifact discoverability, assistant subagent role boundary |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` |
| Required end-state posture | GAP Register table (Section IV) contains three additional rows (GAP-009, GAP-010, GAP-011). Section V assessment contains updated cluster descriptions. Change Surface Inventory table is expanded. |
| Explicit non-target / do-not-change constraints | Do NOT modify GAP-001 through GAP-008 rows. Do NOT modify Section VIII (Downstream Actions). |
| Validation check | (1) GAP-009, GAP-010, GAP-011 rows exist in the GAP Register table; (2) Change Surface Inventory table includes the new gaps; (3) Section V cluster narratives reference the new gaps |
| Blocking ambiguity rule | If the GAP Register table structure has changed since v1.0.0, re-read the current structure before appending |
| Status | `open` |

#### Implementation Detail

**Step 1: Append three rows to the GAP Register table (Section IV, after the GAP-008 row on line 112)**

After the GAP-008 row, append these three rows to the table:

```markdown
| GAP-009 | workflow | Implementation Detail authoring quality lacks cross-model enforcement | CONV-012 governs the hybrid SPEC structure (metadata table + prose `Implementation Detail`) but does not define authoring rules for the prose block. Implementation Detail authored by one LLM model (e.g., Claude Opus 4.6) may use implicit back-references, embedded conditional logic, or model-specific prose patterns that other high-intelligence models (e.g., GPT 5.4) cannot reliably parse and execute. | `deferred_to_TK002` | `guideline_workspace_implementation.md`, `template_workspace_implementation_task-specification.md`, `template_workspace_implementation_remediation-specification.md` | Grounding: AGENTIF benchmark — LLMs fail on dense multi-constraint specs; IEEE 29148 completeness attribute; Claude Code context-amnesia delegation pattern; Codex "single source of truth" principle. |
| GAP-010 | consistency | Implementation artifact discoverability is insufficient when both execution audiences coexist | The `execution_audience` flag (CONV-013) distinguishes developer-facing from consultant/assistant-facing implementation artifacts, but this flag is in frontmatter only — not visible in directory listings. Live inventory shows ~18 consultant-scoped artifacts vs ~10 developer-scoped artifacts in the same `implementation/` directories. Developer-facing specs (which seed implementation-backed gate workflows and are reviewed by multiple roles) are indistinguishable from lightweight assistant orchestration briefs at the filesystem level. | `deferred_to_TK001.1` | `guideline_workspace_implementation.md`, `workspace_documentation_rules.md` | Grounding: ISO 9001 §7.5.3 — distinct document types should be distinguishable by identification scheme; PRINCE2 Configuration Item Records — each product variant has a distinct CI type; Claude Code role archetypes — structurally distinct, not just flag-differentiated. Requires comparative analysis (TK001.1) before convention design. |
| GAP-011 | consistency | Assistant subagent role boundary is absent from governance | The assistant subagent operates under LLM_Consultant authority executing `execution_audience: 'consultant'` implementation artifacts, but is not a named role in `workspace_documentation_rules.md` §6. Unlike LLM_Developer (which owns DEV-REPORTs and participates in implementation-backed gate workflows), the assistant subagent has no defined boundary rules, no execution evidence requirements, and no explicit scope distinction from LLM_Developer. | `deferred_to_TK002` | `workspace_documentation_rules.md` | Grounding: Claude Code built-in role archetypes with distinct tool restrictions; CrewAI named role definitions (Manager, Worker, Researcher); Microsoft guidance — "roles have distinct tool access and explicit handoff artifacts." Client preference: role name `LLM_Assistant`. |
```

**Step 2: Update Section V cluster narratives (lines 118-134)**

Replace the entire block from `The eight governance gaps fall into three clusters:` through `...explicitly acknowledged as evidence, not silently ignored.` with:

```markdown
The eleven governance gaps fall into four clusters:

**Cluster A — Implementation-Spec Precision** (GAP-001, GAP-002, GAP-009):
- The current IMPLEMENTATION guideline defines the SPEC structure (CONV-012) and audience (CONV-013) but lacks a minimum-detail enforcement floor. A SPEC item that names no exact target files, no end-state posture, and no validation checks is currently valid.
- The current ANALYSIS guideline defines external-review scope for gate-readiness input but does not require per-SPEC commissionability assessment. An external review that says "the package looks complete" without testing whether each SPEC is independently executable is currently valid.
- The Implementation Detail prose block beneath the SPEC metadata table has no cross-model authoring rules. Detail authored by one LLM model may use patterns that other high-intelligence models cannot reliably parse and execute. Industry grounding: IEEE 29148 completeness attributes require self-contained, unambiguous specifications; the AGENTIF benchmark confirms LLMs fail on dense multi-constraint specifications.

**Cluster B — Authority & Commissioning Model** (GAP-003, GAP-004, GAP-005, GAP-007):
- Multiple review-like analyses can coexist in a gate package without explicit authority ordering. The current package rules define a Gate Package Index and Evidence Index but do not require naming one authoritative external review. Industry grounding: ISO 9001 §7.5.3 requires only approved current-revision documents in circulation; ISO 10007 defines configuration baselines as the single reference point.
- Consultant-to-executor commissioning is allowed but not required to flow through an IMPLEMENTATION artifact. A consultant could technically delegate execution through plan steps alone. Industry grounding: PRINCE2 Work Package authorization requires a formal artifact with mutual acceptance; ITIL Service Design Package requires formal handover.
- The `standards_input` boundary for premature concrete artifacts is stated as a SHOULD rather than a MUST, and the enforcement mechanism (reclassifying a premature artifact as lineage-only) is not codified. Industry grounding: ISO 9001 §8.7 requires nonconforming output segregation.
- Consultant-only reminder surfaces versus broader role-protocol surfaces are not distinguished by rule. Industry grounding: ISO 27001 Annex A 5.12/5.13 requires classification and metadata-based labeling; RACI requires exactly one Accountable per row.

**Cluster C — Same-Gate QA & Cross-Family Evidence** (GAP-006, GAP-008):
- Same-gate QA corrections happen but are tracked ad hoc. No rule requires plan task register updates, session records, and proposal evidence-index refreshes. Industry grounding: ISO 9001 §10.2 CAPA requires documented nonconformity + actions + results; AS9100D §10.2 requires the most rigorous per-finding tracking.
- AC003's live analysis-based implementation-spec pattern is a vertical-integration inconsistency that must be explicitly acknowledged as evidence, not silently ignored.

**Cluster D — Implementation Artifact Architecture & Role Boundaries** (GAP-010, GAP-011):
- Developer-facing implementation specs (which seed implementation-backed gate workflows, are mandatory in gate-readiness packages, and are reviewed by multiple roles) are indistinguishable from lightweight assistant orchestration briefs at the filesystem level. The `execution_audience` flag in frontmatter is the only discriminator. Industry grounding: ISO 9001 §7.5.3 requires distinct document types to be distinguishable by their identification scheme; Claude Code uses structurally distinct role archetypes, not just flag-differentiated agents.
- The assistant subagent operates under consultant authority without a named role in the governance suite. Unlike LLM_Developer (distinct role, owns DEV-REPORTs, participates in implementation-backed gate workflows), the assistant has no defined boundary rules. Industry grounding: CrewAI defines named role identities (Manager, Worker, Researcher) with explicit delegation rules; Microsoft guidance requires "distinct tool access and explicit handoff artifacts."
```

**Step 3: Update Change Surface Inventory table (lines 140-148)**

Replace the Change Surface Inventory table with:

```markdown
| Target File | Affected Gaps | Section(s) Requiring Amendment |
|:--|:--|:--|
| `guideline_workspace_implementation.md` | GAP-001, GAP-004, GAP-005, GAP-009 | §IV (CONV-012 minimum-detail enforcement + Implementation Detail authoring sub-rule), §II (commissioning protocol), §VII.E (`standards_input` enforcement), §III (subtype taxonomy pending TK001.1) |
| `template_workspace_implementation_task-specification.md` | GAP-001, GAP-009 | SPEC item metadata table (minimum-detail required fields), Implementation Detail placeholder (cross-model conformance note) |
| `template_workspace_implementation_remediation-specification.md` | GAP-009 | Implementation Detail placeholder (cross-model conformance note) |
| `guideline_workspace_analysis.md` | GAP-002, GAP-003 | §IV.B (`external_review` lifecycle: per-SPEC commissionability), new clause or §V.F (authoritative-review selection) |
| `guideline_workspace_plan.md` | GAP-006 | §VI.L or new §VI.N (same-gate correction tracking requirements) |
| `guideline_workspace_proposal.md` | GAP-003, GAP-005, GAP-006 | §V.B (single-authoritative-review naming in gate package), §V.D (`standards_input` enforcement), same-gate evidence-index refresh |
| `guideline_workspace_notes.md` | GAP-006 | Same-gate correction session registration requirements |
| `workspace_documentation_rules.md` | GAP-004, GAP-007, GAP-010, GAP-011 | §6 (commissioning protocol + LLM_Assistant role boundary), §7.A (consultant-only vs broader role-protocol distinction), §3 (artifact type inventory if subtype added pending TK001.1) |
```

**Step 4: Update Section V.C Recommendation (lines 150-157)**

Replace the Recommendation paragraph with:

```markdown
### C. Recommendation

Recommend packaging all eleven gaps into the TK002 `standards_input` proposal (with GAP-010 deferred to a parallel TK001.1 comparative analysis that feeds a placeholder convention in TK002) because:
1. All gaps share the same governance-hardening boundary: they are pre-implementation rule changes that must be approved before TK004 developer execution.
2. Splitting into multiple proposals would create unnecessary coordination overhead for a single consultation-only `GATE-001`.
3. The change surface is bounded to eight existing files with no new artifact families. The only open architectural question (GAP-010: naming convention vs. subtype split vs. status quo) is isolated to TK001.1 and represented in TK002 as a placeholder decision request (DEC-008).
4. The single-package approach aligns with PRINCE2's "manage by exception" principle: one gate, one disposition, bounded scope.
```

---

### SPEC-003 -- Update TK001 Gap Analysis: Update Executive Summary, Scope, Frontmatter, and Changelog

| Field | Detail |
|:--|:--|
| Requirement Source | Consistency requirement: Executive Summary and Scope must reflect the expanded gap count and new clusters |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` |
| Required end-state posture | Frontmatter `version` is `2.0.0`, `date` is `2026-03-28`. Executive Summary and Scope sections reflect eleven gaps and four clusters. Changelog has v2.0.0 entry. |
| Explicit non-target / do-not-change constraints | Do NOT modify Section VIII (Downstream Actions) or Section IX (References/Links Register) beyond adding new reference entries if needed. |
| Validation check | (1) Frontmatter version = `2.0.0`; (2) Executive Summary mentions eleven gaps; (3) Scope section includes the three new gap topics; (4) Changelog v2.0.0 entry exists |
| Blocking ambiguity rule | Apply this SPEC after SPEC-001 and SPEC-002 mutations are complete |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter (lines 10-11)**

Change:
```yaml
version: '1.0.0'
date: '2026-03-27'
```
to:
```yaml
version: '2.0.0'
date: '2026-03-28'
```

**Step 2: Update frontmatter `assessment_scope` (line 17)**

Change:
```yaml
assessment_scope: 'Governance gaps across implementation-spec precision, external-review sufficiency, commissioning rules, standards-input boundaries, same-gate QA tracking, and AC003 vertical-integration inconsistency.'
```
to:
```yaml
assessment_scope: 'Governance gaps across implementation-spec precision (including cross-model Implementation Detail quality), external-review sufficiency, commissioning rules, standards-input boundaries, same-gate QA tracking, AC003 vertical-integration inconsistency, implementation artifact discoverability, and assistant subagent role boundary.'
```

**Step 3: Update Executive Summary (lines 22-37)**

Replace the Purpose paragraph (line 24) with:
```markdown
**Purpose**: Translate the TK000 baseline readiness assessment and the AC004 QA evidence set into an explicit, bounded governance gap register that defines the exact guideline/template/rules surfaces AC006 must change at `GATE-001`. v2.0.0 incorporates industry-standard and agentic-environment evidence grounding per client request.
```

Replace the Scope paragraph (line 26) with:
```markdown
**Scope**: Eleven governance gap families covering implementation-spec minimum detail, cross-model Implementation Detail authoring quality, per-SPEC commissionability assessment, single-authoritative-review selection, consultant-to-executor commissioning rules, `standards_input` boundary for premature concrete artifacts, same-gate QA correction tracking, consultant-only versus broader role-protocol distinction, AC003 cross-family inconsistency as vertical-integration evidence, implementation artifact discoverability, and assistant subagent role boundary formalization.
```

Replace the Conclusion/Recommendation paragraph (line 28) with:
```markdown
**Conclusion / Recommendation**: Eleven governance gaps are confirmed across four clusters (implementation-spec precision, authority/commissioning model, same-gate QA/cross-family evidence, implementation artifact architecture/role boundaries). Each gap has a bounded change surface, a clear failure mode traced to AC004 QA evidence or live operational observation, a recommended governance direction, and industry-standard/agentic-environment grounding. The change surface spans eight workspace-governance files. All gaps are consultant-owned pre-implementation requirements that must be approved at `GATE-001` before downstream TK004 developer execution begins. GAP-010 (implementation artifact discoverability) is deferred to a parallel TK001.1 comparative analysis.
```

Replace the Client Summary bullet list (lines 32-37) with:
```markdown
- Eleven governance gaps are explicitly documented, each traced to a specific AC004 QA failure mode, AC003 vertical-integration inconsistency, or live operational observation. Each gap is grounded in traditional process standards and modern agentic-environment patterns.
- The gaps target eight workspace-governance files: `guideline_workspace_implementation.md`, `template_workspace_implementation_task-specification.md`, `template_workspace_implementation_remediation-specification.md`, `guideline_workspace_analysis.md`, `guideline_workspace_plan.md`, `guideline_workspace_proposal.md`, `guideline_workspace_notes.md`, and `workspace_documentation_rules.md`.
- The proposed governance direction for each gap is summarized in the GAP Register (Section IV) and expanded in the Assessment section (Section V).
- No gap requires creating new artifact families. One gap (GAP-010) may require a subtype or naming convention change pending the TK001.1 comparative analysis.
- AC003 is incorporated as vertical-integration evidence: its analysis-based implementation-spec pattern is a live instance of the governance weakness AC006 is hardening.
- Three new gaps address client-identified concerns: cross-model Implementation Detail quality (GAP-009), implementation artifact discoverability (GAP-010), and assistant subagent role boundary formalization (GAP-011).
- The gap analysis feeds directly into the TK002 `standards_input` proposal and the parallel TK001.1 comparative analysis.
```

**Step 4: Update Scope section (lines 43-57)**

Replace the **In scope** list with:
```markdown
**In scope**:
- Implementation-spec inclusion and minimum-detail failure modes
- Cross-model Implementation Detail authoring quality
- Per-SPEC commissionability-assessment requirement
- Single-authoritative-review requirement when multiple review-like analyses exist
- Consultant-authorship versus execution-boundary reconciliation
- Consultant-to-lower-intelligence / agentic executor commissioning rule
- `standards_input` boundary for premature concrete artifacts
- Same-gate QA-remediation / session-note / package-tracking requirements
- AC003 cross-family inconsistency as vertical-integration evidence
- Implementation artifact discoverability when both execution audiences coexist
- Assistant subagent role boundary formalization (`LLM_Assistant`)
```

Replace the **Out of scope** list with:
```markdown
**Out of scope**:
- Editing the live guidelines directly (that is TK004 post-GATE-001 scope)
- Mutating the AC004 successor package itself
- Changing the IMPLEMENTATION subtype taxonomy (deferred to TK001.1 comparative analysis)
- Retroactive migration of existing instantiated artifacts
```

**Step 5: Append changelog entry (after line 194)**

Append a new row to the changelog table:
```markdown
| v2.0.0 | 2026-03-28 | Major | Industry-standard and agentic-environment evidence grounding added (§III.B). Three new gaps added: GAP-009 (cross-model Implementation Detail quality), GAP-010 (implementation artifact discoverability — deferred to TK001.1), GAP-011 (assistant subagent role boundary). Cluster structure expanded from three to four. Change surface expanded from seven to eight governance files. Executive Summary, Scope, Assessment, and Change Surface Inventory updated to reflect eleven-gap scope. |
```

---

### SPEC-004 -- Update TK002 Proposal: Add Industry Citations to Convention Rationales

| Field | Detail |
|:--|:--|
| Requirement Source | Client feedback: "lack of industry-standard perspective and best practices"; client preference: lighter approach with one-line citations |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| Required end-state posture | Each CONV-015 through CONV-021 Rationale cell contains a one-line industry citation appended after the existing rationale text |
| Explicit non-target / do-not-change constraints | Do NOT modify the Rule column or Authority Link column of existing conventions. Do NOT delete existing rationale text — append to it. |
| Validation check | Each of the seven convention rows has an expanded Rationale cell containing at least one traditional standard citation and one agentic pattern citation |
| Blocking ambiguity rule | If the convention table structure has changed since v1.0.0, re-read before applying |
| Status | `open` |

#### Implementation Detail

**Step 1: Replace the Convention Set table (lines 70-78)**

Replace the entire table (header + 7 data rows) with the following. Each Rationale cell now ends with a `[Grounding: ...]` citation:

```markdown
| Convention ID | Rule | Rationale | Authority Link |
|:--|:--|:--|:--|
| CONV-015 | Every execution-facing SPEC item MUST name at minimum: (a) exact target file(s)/surface(s), (b) required end-state posture, (c) validation checks, and (d) explicit non-target constraints. A SPEC item missing any of these four elements MUST be treated as draft-incomplete and MUST NOT be commissioned for execution. Additionally, when a SPEC item includes an `#### Implementation Detail` block, the detail MUST use a structured step format that is model-agnostic and independently parseable: each step MUST be numbered and self-contained; file mutations MUST use before/after code blocks with explicit file path and line/section locators; conditional logic MUST be expressed as explicit if/then rules, not embedded in prose. The Implementation Detail MUST be executable by any high-intelligence LLM model without requiring project-specific context beyond what is stated in the SPEC metadata table and the detail block itself. | The AC004 case showed that a SPEC with summary-level content passed external review unchallenged. A minimum-detail floor prevents under-specified SPECs from entering the execution pipeline. The cross-model authoring sub-rule ensures Implementation Detail is not authored in model-specific patterns that fail on non-authoring models. [Grounding: IEEE 29148 completeness/verifiability attributes; CMMI-DEV RD entry/exit criteria; PRINCE2 Work Package minimum content; AGENTIF benchmark — LLMs fail on dense multi-constraint specs; Claude Code context-amnesia — subagents start fresh, brief must be self-contained; Codex "single source of truth" — "Do not assume anything not written here"] | `guideline_workspace_implementation.md` §IV (amend CONV-012), `template_workspace_implementation_task-specification.md`, `template_workspace_implementation_remediation-specification.md` |
| CONV-016 | When an `external_review` analysis serves as a gate-readiness input and the gate package includes an IMPLEMENTATION artifact, the review MUST assess whether each execution-facing SPEC item meets the CONV-015 minimum-detail floor and is independently commissionable for the stated `execution_audience`. | The AC004 external review did not detect the vague implementation spec because per-SPEC commissionability was not a review requirement. [Grounding: Fagan Inspection — per-item checklist review; ISO/IEC 20246 — item-level examination; FDA 21 CFR 820.30(c) — per-design-input completeness; DO-178C §6.3 — per-requirement traceability; Claude Code PreToolUse hooks — per-action enforcement; CodeRabbit agentic validation — ~46% bug detection] | `guideline_workspace_analysis.md` §IV.B (`external_review` lifecycle) |
| CONV-017 | When a gate package contains multiple ANALYSIS artifacts of type `external_review`, the gate-disposition proposal MUST designate exactly one as the **authoritative external review** for that gate. Other review-like analyses are classified as supporting or historical evidence in the Evidence Index. | The AC004 package surfaced two external reviews without explicit authority ordering. The authoritative designation was resolved ad hoc in the QA assessment. [Grounding: ISO 9001 §7.5.3 — only approved current-revision documents in circulation; ISO 10007/IEEE 828 — configuration baseline as single reference; PRINCE2 CIR — status tracking; CrewAI hierarchical authority with `allowed_agents`] | `guideline_workspace_analysis.md` (new clause or §V.F), `guideline_workspace_proposal.md` §V.B (Evidence Index) |
| CONV-018 | When a consultant commissions governed delegated execution to `LLM_Developer`, `LLM_Assistant`, or a designated agentic execution role, the commissioning MUST be mediated through an IMPLEMENTATION artifact (`task_specification` or `remediation_specification`) that the governing plan task explicitly references. Commissioning MAY bypass IMPLEMENTATION mediation only when ALL three conditions are met: (a) change is confined to a single governance surface, (b) no downstream execution dependency exists, and (c) the delegating authority explicitly attests to low execution risk in the plan task's Action field. When the exception is claimed, the plan task's Action field MUST record the attestation (e.g., "Direct commission: single-surface, no dependency, low risk"). | The existing rules allow but do not require IMPLEMENTATION-mediated commissioning. Without this rule, governed execution could bypass the specification surface. The risk-based exception replaces the original count-based threshold ("fewer than three target files") with a three-condition test that scales governance formality with risk. [Grounding: PRINCE2 Work Package — formal authorization with mutual acceptance; ITIL SDP — formal handover; NIST AI RMF — proportional governance (formality scales with risk); AURA framework — risk-based scoring (0-30 auto-approve, 30-60 selective, 60+ escalate); Anthropic research — "too early to mandate specific interaction patterns"; Claude Code Agent tool — sole delegation channel; Codex+Agents SDK — PM-gated pipeline with file-based gating] | `guideline_workspace_implementation.md` §II, `workspace_documentation_rules.md` §6.A |
| CONV-019 | When a consultation-only gate is still deciding a convention or operational pattern, any pre-existing concrete implementation artifact for that scope MUST be reclassified as lineage-only in the gate package Evidence Index. The `standards_input` proposal MUST be the active pre-implementation authority surface. Authors MUST NOT treat the premature concrete artifact as active gate evidence. This elevates existing CONV-014 from SHOULD to MUST. | The AC004 case required explicit quarantine and reclassification of a pre-existing draft `SKILL.md`. The current SHOULD-level rule allowed ambiguity about whether the artifact was active or lineage-only. [Grounding: ISO 9001 §8.7 — nonconforming output segregation; CM baselines — unapproved = no authority; ITIL Release Mgmt — CAB as change authority boundary; Claude Code worktree isolation — draft contamination prevention] | `guideline_workspace_implementation.md` §VII.E, `guideline_workspace_proposal.md` §V.B and §V.D |
| CONV-020 | When same-gate QA or package-coherence defects are discovered after the gate package is assembled, the correction MUST be tracked through three surfaces: (a) plan task register (new sub-task or task status update), (b) session notes (correction session recorded per `guideline_workspace_notes.md`), and (c) gate-disposition proposal (evidence index refreshed to separate current from historical evidence). Silent amendment of live artifacts without cross-surface tracking is a governance violation. | The AC004 case required three correction sessions (SES005-SES007) with multiple plan amendments. Each was tracked ad hoc. A formal cross-surface tracking requirement prevents silent corrections. [Grounding: ISO 9001 §10.2 CAPA — documented nonconformity + actions + results; AS9100D §10.2 — most rigorous per-finding tracking; CMMI VER — defects tracked and analyzed; PRINCE2 Issue Register + Quality Register + CIR cross-referencing] | `guideline_workspace_plan.md` §VI (new clause), `guideline_workspace_notes.md` (same-gate session rule), `guideline_workspace_proposal.md` §V.B |
| CONV-021 | When a gate package defines both a consultant-only operational surface and a broader multi-role operational protocol, the gate-disposition proposal MUST explicitly state which scope each surface serves, using the labels **consultant-scoped** and **program-scoped**. The consultant-scoped surface MUST NOT be presented as if it governs all roles; the program-scoped protocol MUST NOT be restricted to consultant use only. | The AC004 case resolved the distinction between the reminder surface (consultant-only) and `status_program.md` Section 7 (broader role-based protocol) through session discussion rather than by rule. [Grounding: ISO 27001 Annex A 5.12/5.13 — classification + metadata-based labeling; RACI — exactly one Accountable per row; PRINCE2 Communication Management Approach — audience mapping; Claude Code tool allowlists/denylists per subagent role] | `workspace_documentation_rules.md` §7.A (new clause or amendment) |
```

---

### SPEC-005 -- Update TK002 Proposal: Add New Conventions CONV-022 and CONV-023

| Field | Detail |
|:--|:--|
| Requirement Source | Client QA comments 2.1 (implementation artifact architecture) and 4 (developer vs. assistant subagent distinction) |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| Required end-state posture | Convention table has two additional rows (CONV-022, CONV-023) appended after CONV-021. Compatibility Notes section has two additional bullet points. |
| Explicit non-target / do-not-change constraints | Do NOT modify existing convention rows CONV-015 through CONV-021 (those are handled in SPEC-004). |
| Validation check | (1) CONV-022 and CONV-023 rows exist in the Convention Set table; (2) Compatibility Notes for both new conventions exist in §III.B |
| Blocking ambiguity rule | Apply this SPEC after SPEC-004 is complete (the table must already contain the updated CONV-015-021 rows) |
| Status | `open` |

#### Implementation Detail

**Step 1: Append two rows to the Convention Set table (after the CONV-021 row)**

```markdown
| CONV-022 | The architectural distinction between developer-facing implementation specifications (which seed implementation-backed gate workflows and are reviewed by multiple roles) and assistant-facing implementation specifications (lightweight orchestration briefs reviewed only by the commissioning consultant) MUST be resolved through one of: (a) a naming convention distinguishing the two at the filesystem level, (b) a new IMPLEMENTATION subtype for assistant-scoped work, or (c) a combination of naming + subtype. The specific resolution is deferred to the TK001.1 comparative analysis; this convention reserves the requirement that a resolution MUST be adopted. Additionally, the `remediation_specification` subtype scope (currently restricted to gate RECYCLE verdicts) and its overlap with assistant-executed pre-gate corrections MUST be evaluated as a dimension of the same analysis. | Developer-facing specs (~10 in live inventory) are indistinguishable from consultant/assistant specs (~18) at the filesystem level. The `execution_audience` flag in frontmatter is the only discriminator, but it is not visible in directory listings. [Grounding: ISO 9001 §7.5.3 — distinct document types distinguishable by identification scheme; PRINCE2 CIR — each product variant has distinct CI type; Claude Code role archetypes — structurally distinct, not flag-differentiated; ISO 9001 CAPA distinction between corrections (immediate) and corrective actions (systemic) maps to remediation_specification vs. assistant pre-gate fixes] | `guideline_workspace_implementation.md` §III, `workspace_documentation_rules.md` §3 (pending TK001.1) |
| CONV-023 | The assistant subagent MUST be recognized as a named role (`LLM_Assistant`) in `workspace_documentation_rules.md` §6 with explicit boundary rules: (a) operates under LLM_Consultant authority with no independent decision-making; (b) does not produce DEV-REPORTs — execution evidence is captured in session notes or plan changelog; (c) consumes implementation artifacts with `execution_audience: 'consultant'` or `execution_audience: 'assistant'` (final audience label pending TK001.1); (d) is not part of the implementation-backed gate workflow — no VERIFICATION stage for assistant work; (e) is distinct from LLM_Developer, which owns `guideline_workspace_dev-report.md` and participates in the larger development workflow toward implementation-backed gates. The Role-to-Artifact Ownership Matrix (§8) MUST be updated to include `LLM_Assistant`. | The assistant subagent is not a named role in §6; it operates as an unnamed extension of LLM_Consultant. Unlike LLM_Developer, the assistant has no defined boundary rules, no execution evidence requirements, and no explicit scope distinction. [Grounding: Claude Code built-in role archetypes with distinct tool restrictions per subagent; CrewAI named role definitions (Manager, Worker, Researcher) with explicit delegation rules; Microsoft guidance — "roles have distinct tool access and explicit handoff artifacts so that disagreements can be resolved via evidence"] | `workspace_documentation_rules.md` §6 (new §6.F), §8 (ownership matrix update) |
```

**Step 2: Append compatibility notes for CONV-022 and CONV-023 (after the AC003 bullet in §III.B, after line 89)**

After the bullet starting with `- **AC003 vertical-integration evidence (GAP-008)**:`, append:

```markdown
- **CONV-022** does not prescribe a specific architectural resolution. It reserves the requirement that a resolution MUST be adopted, with the specific form determined by TK001.1. Existing implementation artifacts are not retroactively renamed or retyped; the resolution applies to new artifacts authored after approval. The remediation_specification scope evaluation does not expand that subtype's current trigger (gate RECYCLE verdict); it evaluates whether the gray zone of pre-gate assistant corrections needs its own mechanism or can be absorbed by the architectural distinction.
- **CONV-023** introduces `LLM_Assistant` as a new named role. Existing artifacts authored with `execution_audience: 'consultant'` are not retroactively relabeled. The role boundary rules apply to new assistant-executed work after approval. The relationship between `LLM_Assistant` and `LLM_Developer` is explicitly non-overlapping: `LLM_Developer` owns DEV-REPORTs and participates in implementation-backed gate workflows; `LLM_Assistant` operates under consultant authority with session-note-level execution evidence only.
```

---

### SPEC-006 -- Update TK002 Proposal: Add Enforcement Modalities Section (§III.C)

| Field | Detail |
|:--|:--|
| Requirement Source | Client-approved recommendation to include dual-channel enforcement framing for TK004 implementation design |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| Required end-state posture | A new §III.C subsection exists between Compatibility Notes (§III.B) and Decision Requests (§IV) |
| Explicit non-target / do-not-change constraints | Do NOT modify §IV (Decision Requests) at this step — that is handled in SPEC-007. |
| Validation check | §III.C subsection exists with header "Enforcement Modalities" and describes both human-mediated and deterministic/agentic channels |
| Blocking ambiguity rule | Apply this SPEC after SPEC-005 is complete |
| Status | `open` |

#### Implementation Detail

**Step 1: Insert §III.C after the Compatibility Notes section (before the `---` separator preceding §IV)**

Before the line `## IV. DECISION REQUESTS`, insert:

```markdown
### C. Enforcement Modalities

Each convention above can be enforced through two complementary channels. TK004 implementation SHOULD design for both:

| Channel | Mechanism | Applicable Conventions | Notes |
|:--|:--|:--|:--|
| **Human-mediated** | Review checklists, gate-package inspection, external-review scope requirements, consultant/reviewer judgment | All (CONV-015 through CONV-023) | Aligns with traditional standards: Fagan Inspection checklists, ISO 20246 review types, PRINCE2 Work Package acceptance, ISO 9001 CAPA documentation |
| **Deterministic / agentic** | Hooks (PreToolUse approve/deny), sandboxes (workspace-write isolation), tool restrictions (per-subagent allowlists/denylists), frontmatter validation (schema checks), worktree isolation (draft contamination prevention) | CONV-015 (metadata field validation), CONV-018 (attestation field in plan Action column), CONV-019 (frontmatter status check), CONV-022 (naming convention enforcement), CONV-023 (role-identity injection via AGENTS.md) | Aligns with agentic patterns: Claude Code hooks (21 lifecycle events, 4 handler types), Codex sandboxing (read-only/workspace-write/danger modes), CodeRabbit agentic validation |

Not all conventions are equally amenable to deterministic enforcement. CONV-016 (per-SPEC commissionability) and CONV-017 (authoritative review designation) are primarily judgment-based and rely on human-mediated enforcement. CONV-015 metadata validation and CONV-018 attestation are the strongest candidates for deterministic enforcement via hooks or schema validation.

---

```

---

### SPEC-007 -- Update TK002 Proposal: Add New Decision Requests DEC-008 and DEC-009, Update DEC-004

| Field | Detail |
|:--|:--|
| Requirement Source | New conventions CONV-022 and CONV-023 require client decision requests; CONV-018 threshold model changed from count-based to risk-based |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| Required end-state posture | DEC-004 row is updated with risk-based options. DEC-008 and DEC-009 rows exist in the Decision Requests table. |
| Explicit non-target / do-not-change constraints | Do NOT modify DEC-001, DEC-002, DEC-003, DEC-005, DEC-006, DEC-007 rows. |
| Validation check | (1) DEC-004 Options column references three-condition risk test; (2) DEC-008 row exists for CONV-022; (3) DEC-009 row exists for CONV-023 |
| Blocking ambiguity rule | Apply after SPEC-004 and SPEC-005 are complete |
| Status | `open` |

#### Implementation Detail

**Step 1: Replace DEC-004 row (line 100)**

Replace the existing DEC-004 row with:

```markdown
| DEC-004 | Should governed delegated execution require IMPLEMENTATION-mediated commissioning (CONV-018)? | (a) Yes — MUST for all governed delegation with no exception; (b) Yes — MUST with a risk-based three-condition exception (single surface, no downstream dependency, explicit low-risk attestation); (c) No — current allowance-based rule is sufficient | (b) — the risk-based exception scales governance formality with risk (aligned with NIST AI RMF proportional governance and AURA framework), prevents over-governance for simple tasks while ensuring complex execution flows through the specification surface, and creates an audit trail via the plan task Action field attestation | Client |
```

**Step 2: Append DEC-008 and DEC-009 rows after DEC-007 (after line 103)**

```markdown
| DEC-008 | Should the implementation artifact architecture be changed to improve discoverability of developer-facing vs. assistant-facing specs (CONV-022)? | (a) Yes — require a resolution; specific form determined by TK001.1 comparative analysis; (b) No — current `execution_audience` flag is sufficient | (a) — the live inventory shows 18 consultant-scoped vs 10 developer-scoped artifacts in the same directories; ISO 9001 §7.5.3 and PRINCE2 CIR both require distinct document types to be distinguishable by their identification scheme. Recommendation: approve the requirement, defer the specific resolution form to TK001.1 | Client |
| DEC-009 | Should the assistant subagent be recognized as a named role `LLM_Assistant` with explicit boundary rules (CONV-023)? | (a) Yes — named role with boundary rules in §6 and ownership matrix in §8; (b) No — keep as unnamed extension of LLM_Consultant | (a) — industry practice (CrewAI, Claude Code, Microsoft) requires named role identities with explicit delegation rules; the assistant subagent's operational pattern (no DEV-REPORT, session-note evidence, consultant-authority-only) is sufficiently distinct from LLM_Developer to warrant its own boundary definition | Client |
```

---

### SPEC-008 -- Update TK002 Proposal: Update Impact Assessment and Risk Register

| Field | Detail |
|:--|:--|
| Requirement Source | New conventions and revised CONV-018 require updated impact and risk entries |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| Required end-state posture | Impact Assessment includes bullets for new conventions and industry alignment. RISK-003 is updated for risk-based model. New RISK-005 and RISK-006 entries for CONV-022 and CONV-023. |
| Explicit non-target / do-not-change constraints | Do NOT modify RISK-001, RISK-002, RISK-004. |
| Validation check | (1) Positive outcomes include industry-alignment bullet and new convention bullets; (2) RISK-003 references risk-based three-condition test; (3) RISK-005 and RISK-006 rows exist |
| Blocking ambiguity rule | Apply after SPEC-007 is complete |
| Status | `open` |

#### Implementation Detail

**Step 1: Replace the Positive outcomes list (lines 111-118)**

Replace with:

```markdown
- **Positive outcomes**:
  - SPEC items will have an enforceable quality floor, preventing under-specified execution commissions
  - Implementation Detail blocks will be model-agnostic — executable by any high-intelligence LLM, not only the authoring model
  - External reviews will catch vague SPECs before gate approval rather than after
  - Gate packages will have clear authority ordering when multiple reviews exist
  - Governed delegated execution will always flow through a traceable specification surface
  - Premature concrete artifacts will be explicitly quarantined rather than ambiguously active
  - Same-gate corrections will be visible across all governance surfaces
  - Consultant-scoped versus program-scoped operational surfaces will be unambiguous
  - Developer-facing and assistant-facing implementation artifacts will be architecturally distinguishable (pending TK001.1 resolution form)
  - The assistant subagent will have a named role identity with explicit boundary rules, eliminating operational ambiguity
  - Conventions align with established industry standards (IEEE 29148, ISO 9001, CMMI, PRINCE2, NIST AI RMF), reducing institutional risk of governance divergence from recognized best practices
```

**Step 2: Replace the Tradeoffs list (lines 120-124)**

Replace with:

```markdown
- **Tradeoffs**:
  - Additional authoring overhead for SPEC items (four required metadata elements + structured Implementation Detail format per SPEC)
  - Additional review scope for external reviews covering IMPLEMENTATION artifacts
  - Additional bookkeeping for same-gate corrections (three-surface tracking)
  - The risk-based trivial-execution threshold (CONV-018) introduces an attestation element requiring author judgment — consistent with Anthropic's finding that "it's too early to mandate specific interaction patterns" and AURA's recommendation for progressive automation
  - Architectural resolution for implementation artifact discoverability (CONV-022) may require template amendments and naming convention changes
  - Formal LLM_Assistant role (CONV-023) adds a fifth agent role to the governance suite, increasing the ownership matrix complexity
```

**Step 3: Replace RISK-003 row (line 132)**

Replace with:

```markdown
| RISK-003 | CONV-018 risk-based three-condition exception introduces an attestation element that requires author judgment | Low | The three conditions are independently verifiable (single surface — count check; no downstream dependency — dependency graph check; explicit attestation — Action field audit). Progressive automation through memory-based optimization (per AURA framework) can reduce human intervention frequency over time |
```

**Step 4: Append RISK-005 and RISK-006 rows after RISK-004 (after line 133)**

```markdown
| RISK-005 | CONV-022 architectural resolution (pending TK001.1) may require template changes and naming convention updates that affect existing authoring patterns | Low | The resolution applies to new artifacts only (no retroactive migration). TK001.1 evaluates options before committing to a specific form |
| RISK-006 | CONV-023 `LLM_Assistant` role introduction adds governance surface area (§6 boundary rules, §8 ownership matrix) | Low | The role boundary is deliberately narrow (operates under consultant authority, no DEV-REPORT, session-note evidence only). The incremental governance surface is bounded to two sections |
```

---

### SPEC-009 -- Update TK002 Proposal: Add External Standards References and Update Frontmatter/Changelog

| Field | Detail |
|:--|:--|
| Requirement Source | Client preference for lighter approach with external references section; version bump for structural changes |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| Required end-state posture | Frontmatter `version` is `2.0.0`, `date` is `2026-03-28`, `target_standards` list includes the remediation template. §VI has a new §VI.B subsection for external standards. Changelog has v2.0.0 entry. |
| Explicit non-target / do-not-change constraints | Do NOT modify §VI.A (the existing internal references table — just rename it to §VI.A if not already labeled). |
| Validation check | (1) Frontmatter version = `2.0.0`; (2) `target_standards` includes 8 items; (3) §VI.B exists with external standards table; (4) Changelog v2.0.0 entry exists |
| Blocking ambiguity rule | Apply after all other TK002 SPECs (SPEC-004 through SPEC-008) are complete |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter (lines 9-10)**

Change:
```yaml
version: '1.0.0'
date: '2026-03-27'
```
to:
```yaml
version: '2.0.0'
date: '2026-03-28'
```

**Step 2: Update `target_standards` list (lines 16-23)**

Replace:
```yaml
target_standards:
  - 'guideline_workspace_implementation.md'
  - 'template_workspace_implementation_task-specification.md'
  - 'guideline_workspace_analysis.md'
  - 'guideline_workspace_plan.md'
  - 'guideline_workspace_proposal.md'
  - 'guideline_workspace_notes.md'
  - 'workspace_documentation_rules.md'
```
with:
```yaml
target_standards:
  - 'guideline_workspace_implementation.md'
  - 'template_workspace_implementation_task-specification.md'
  - 'template_workspace_implementation_remediation-specification.md'
  - 'guideline_workspace_analysis.md'
  - 'guideline_workspace_plan.md'
  - 'guideline_workspace_proposal.md'
  - 'guideline_workspace_notes.md'
  - 'workspace_documentation_rules.md'
```

**Step 3: Update §I Purpose (lines 29-33)**

Replace the Purpose section content with:

```markdown
- **Proposal objective**: Approve the governance direction for eleven identified gaps so downstream implementation (TK004) can apply the approved rule changes to the eight target governance files.
- **Input scope**: Pre-implementation governance rules only. This proposal defines the conventions that must govern how IMPLEMENTATION artifacts are authored, reviewed, commissioned, and tracked, and how the assistant subagent role is formalized. It does not implement the rules — that is TK004 scope after `GATE-001` approval. One architectural question (CONV-022: implementation artifact discoverability) is deferred to TK001.1 comparative analysis with a placeholder decision request (DEC-008).
- **Target standards**: `guideline_workspace_implementation.md`, `template_workspace_implementation_task-specification.md`, `template_workspace_implementation_remediation-specification.md`, `guideline_workspace_analysis.md`, `guideline_workspace_plan.md`, `guideline_workspace_proposal.md`, `guideline_workspace_notes.md`, `workspace_documentation_rules.md`
```

**Step 4: Update §II.B Problems/Gaps table (lines 53-62)**

Append three rows to the Problems/Gaps table after GAP-008:

```markdown
| GAP-009 | workflow | CONV-012 governs SPEC structure but not the Implementation Detail prose block. Model-specific authoring patterns fail on non-authoring models. | Cross-model execution failures; assistant or developer subagents cannot reliably parse Implementation Detail authored by a different LLM. |
| GAP-010 | consistency | `execution_audience` flag is in frontmatter only — developer-facing and assistant-facing specs are indistinguishable at filesystem level. | Developer-facing specs (mandatory in gate packages, multi-role reviewed) cannot be easily identified or prioritized among ~18 consultant-scoped artifacts. |
| GAP-011 | consistency | Assistant subagent operates under consultant authority without a named role in §6. | No defined boundary rules, execution evidence requirements, or scope distinction from LLM_Developer. |
```

**Step 5: Rename existing References table as §VI.A and add §VI.B**

After the existing References table (lines 139-152), before the `---` separator, insert:

```markdown

### B. External Standards References

| Standard / Framework | Relevant Section | Applicable Conventions |
|:--|:--|:--|
| IEEE/ISO/IEC 29148:2018 | §5 (SRS content structure), quality attributes (completeness, verifiability, traceability) | CONV-015 |
| ISO 9001:2015 | §7.5.3 (documented information control), §8.7 (nonconforming outputs), §10.2 (CAPA) | CONV-017, CONV-019, CONV-020, CONV-022 |
| ISO 10007:2017 / IEEE 828-2012 | Configuration baseline, change authority, revision status | CONV-017 |
| ISO/IEC 20246:2017 | Work product reviews — item-level examination | CONV-016 |
| CMMI-DEV v1.3/v2.0 | Requirements Development (RD), Verification (VER) — entry/exit criteria, peer review defect tracking | CONV-015, CONV-020 |
| PRINCE2 7th Edition | Work Package authorization, Configuration Item Records, Issue Register, Communication Management Approach | CONV-015, CONV-017, CONV-018, CONV-020, CONV-021 |
| AS9100D | §10.2 — aerospace nonconformance tracking | CONV-020 |
| FDA 21 CFR 820.30 / Part 11 | Design input completeness, draft vs approved status | CONV-016, CONV-019 |
| DO-178C | §6.3 — per-requirement traceability, Table A-3 verification objectives | CONV-016 |
| ISO 27001:2022 | Annex A 5.12 (classification), 5.13 (labeling) | CONV-021 |
| NIST AI RMF 1.0 | GOVERN/MAP/MEASURE/MANAGE — proportional governance | CONV-018 |
| AURA Framework (arXiv 2510.15739) | Risk-based scoring: 0-30 auto-approve, 30-60 selective, 60+ escalate | CONV-018 |
| Claude Code | Subagents (context-amnesia), hooks (21 lifecycle events), worktree isolation, AGENTS.md role definitions | CONV-015, CONV-018, CONV-019, CONV-022, CONV-023 |
| Codex CLI | AGENTS.md, sandboxing (read-only/workspace-write/danger), PM-gated pipeline pattern | CONV-015, CONV-018, CONV-019 |
| CrewAI | Hierarchical authority, `allowed_agents`, named role definitions (Manager/Worker/Researcher) | CONV-017, CONV-023 |
| Anthropic Research (2025) | Measuring Agent Autonomy — 1-10 scale, oversight strategy shifts | CONV-018 |
| AGENTIF Benchmark (Tsinghua) | LLM failure modes on specification-heavy instructions | CONV-015 |
```

**Step 6: Replace changelog entry (line 160)**

Replace the v1.0.0 row and append v2.0.0:

Keep the v1.0.0 row unchanged. Append after it:
```markdown
| v2.0.0 | 2026-03-28 | Major | Industry-standard and agentic-environment grounding added to all convention rationales. CONV-015 expanded with cross-model Implementation Detail authoring sub-rule. CONV-018 revised from count-based to risk-based three-condition exception (NIST/AURA alignment). Two new conventions added: CONV-022 (implementation artifact architecture — pending TK001.1) and CONV-023 (LLM_Assistant role formalization). Two new decision requests: DEC-008 (CONV-022) and DEC-009 (CONV-023). Enforcement modalities section (§III.C) added for TK004 implementation guidance. External standards references (§VI.B) added. Impact assessment and risk register expanded. GAP-009, GAP-010, GAP-011 added to Problems/Gaps summary. Target standards expanded to include remediation-specification template. |
```

---

### SPEC-010 -- Amend AC006 Activity Plan: Add TK001.1 Task and Update Task Register

| Field | Detail |
|:--|:--|
| Requirement Source | Client-approved recommendation to insert TK001.1 comparative analysis between TK001 and TK002, running in parallel with TK002 (placeholder convention) |
| Target file(s) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| Required end-state posture | Task Register contains TK001.1 row. Section III contains a detailed TK001.1 task section. TK002 Depends On updated to include TK001.1. TK004 Deliverable list expanded. Plan version is `2.0.0`. Changelog has v2.0.0 entry. |
| Explicit non-target / do-not-change constraints | Do NOT modify TK000 task section or any gate sections. Do NOT modify Section IV (Links Register) beyond adding new entries. Do NOT modify Section II (Activity Outline) beyond updating the Context list. |
| Validation check | (1) TK001.1 row in Task Register between TK001 and TK002; (2) TK001.1 detailed section in Section III between TK001 and TK002; (3) TK002 Depends On includes TK001.1; (4) Plan version = `2.0.0`; (5) Changelog v2.0.0 entry exists |
| Blocking ambiguity rule | If the plan has been modified since v1.0.0, STOP and re-read before applying mutations |
| Status | `open` |

#### Implementation Detail

**Step 1: Update frontmatter (lines 9-10)**

Change:
```yaml
version: '1.0.0'
date: '2026-03-27'
```
to:
```yaml
version: '2.0.0'
date: '2026-03-28'
```

**Step 2: Insert TK001.1 row in Task Register (between the TK001 row on line 60 and the TK002 row on line 61)**

After the TK001 row, insert:
```markdown
| TK001.1 | `T104-PH001-ST008-AC006-TK001.1` | Produce implementation artifact architecture comparative analysis | `planned` | LLM_Consultant | TK001 | `analysis/` | `guideline_workspace_analysis.md` | — |
```

**Step 3: Update TK002 row Depends On (line 61, now line 62 after insertion)**

Change TK002 row from:
```markdown
| TK002 | `T104-PH001-ST008-AC006-TK002` | Produce standards-input proposal for governance changes | `planned` | LLM_Consultant | TK001 | `proposal/` | `guideline_workspace_proposal.md` | — |
```
to:
```markdown
| TK002 | `T104-PH001-ST008-AC006-TK002` | Produce standards-input proposal for governance changes | `planned` | LLM_Consultant | TK001, TK001.1 | `proposal/` | `guideline_workspace_proposal.md` | — |
```

**Step 4: Update TK004 Deliverable list (lines 310-316)**

Replace the TK004 Deliverable list with:
```markdown
**Deliverable**:
- Updated `prompt/templates/consultant/workspace/guideline_workspace_implementation.md`
- Updated `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`
- Updated `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md`
- Updated `prompt/templates/consultant/workspace/guideline_workspace_analysis.md`
- Updated `prompt/templates/consultant/workspace/guideline_workspace_plan.md`
- Updated `prompt/templates/consultant/workspace/guideline_workspace_proposal.md`
- Updated `prompt/templates/consultant/workspace/guideline_workspace_notes.md`
- Updated `prompt/templates/consultant/workspace/workspace_documentation_rules.md`
```

**Step 5: Insert TK001.1 detailed task section (between TK001 section ending at line 147 and TK002 section starting at line 149)**

After the TK001 Success Criteria block (ending with `- [ ] The change surface is bounded to the correct guideline/template/rules artifacts`), insert:

```markdown

### Task TK001.1: Produce Implementation Artifact Architecture Comparative Analysis

**Task ID**: `T104-PH001-ST008-AC006-TK001.1`

**Purpose**: Evaluate whether the current `execution_audience` flag (CONV-013) alone is sufficient for distinguishing developer-facing from assistant-facing implementation artifacts, or whether an architectural change (naming convention, subtype split, role-linked template variant, or a combination) is needed. Additionally, evaluate whether the `remediation_specification` subtype scope should be expanded or whether pre-gate assistant corrections need a separate governance mechanism.

**Deliverable**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006-TK001.1_implementation-artifact-architecture-assessment.md`

**Scope**:
- In scope:
  - Assess the current `execution_audience` flag as the sole discriminator between developer-facing and assistant-facing implementation artifacts
  - Assess the discoverability problem: ~18 consultant-scoped vs ~10 developer-scoped artifacts in the same `implementation/` directories
  - Evaluate architectural options:
    - **Option A (Status quo)**: Keep `execution_audience` flag as sole discriminator. Tradeoff: low cost, discoverability problem persists.
    - **Option B (Naming convention split)**: Add a naming prefix/suffix to distinguish (e.g., `implementation_..._task-specification.md` vs `implementation_..._assistant-task.md`). Tradeoff: medium cost, improves filesystem discoverability, no governance rule changes.
    - **Option C (New subtype)**: Create a third IMPLEMENTATION subtype (e.g., `assistant_task`) with its own template, distinct from `task_specification`. Tradeoff: higher cost, cleanest governance separation, requires §III taxonomy amendment.
    - **Option D (Combination)**: Named role (`LLM_Assistant` per CONV-023) + naming convention + subtype. Tradeoff: highest cost, most complete separation.
  - Evaluate whether `remediation_specification` scope (currently restricted to gate RECYCLE verdicts) should be expanded to cover pre-gate assistant corrections, or whether these corrections should be governed by the assistant-scoped architectural variant
  - Ground the assessment in industry evidence: ISO 9001 §7.5.3 (document type identification), PRINCE2 CI types, Claude Code role archetypes, CrewAI task-level security postures
- Out of scope:
  - Implementing the chosen architectural resolution (that is TK004 scope)
  - Retroactive migration of existing implementation artifacts
  - Changing the `remediation_specification` trigger (gate RECYCLE verdict)

**Inputs Required**:
- `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` (v2.0.0, GAP-010 and GAP-011)
- `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` (current §III subtype taxonomy)
- `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md`
- `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md`
- `prompt/templates/consultant/workspace/workspace_documentation_rules.md` (§3, §6, §8)
- Live implementation artifact inventory (grep for `execution_audience` across `prompt/artifacts/`)

**Steps**:
1. Inventory all existing implementation artifacts by `execution_audience` value and assess usage patterns.
2. Document the discoverability problem with concrete examples.
3. Evaluate each architectural option (A through D) against the criteria: discoverability, governance cost, backward compatibility, template impact, and alignment with the LLM_Assistant role formalization (CONV-023).
4. Evaluate whether the remediation_specification scope should be expanded or kept tight, and how pre-gate assistant corrections should be governed under each option.
5. Recommend one option with rationale.

**Success Criteria**:
- [ ] All four options are evaluated with tradeoff analysis
- [ ] The remediation_specification scope question is explicitly assessed
- [ ] A recommendation is provided that can be directly consumed by TK002 (CONV-022 placeholder)
- [ ] The analysis is grounded in industry evidence
```

**Step 6: Update TK002 Scope section to reflect expanded scope (in the TK002 task section)**

In the TK002 task section, after the existing In scope list, add:
```markdown
  - Formalize the assistant subagent as a named role (`LLM_Assistant`) with explicit boundary rules
  - Incorporate TK001.1 findings for implementation artifact architecture (CONV-022 placeholder)
  - Define cross-model Implementation Detail authoring requirements
  - Define dual-channel enforcement modalities (human-mediated + deterministic/agentic) for TK004 guidance
```

**Step 7: Add Links Register entry (in Section IV, after line 411)**

Append to the Links Register table:
```markdown
| Template | Implementation Remediation-Specification Template | `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md` |
```

**Step 8: Append changelog entry (after line 419)**

Append a new row to the changelog table:
```markdown
| v2.0.0 | 2026-03-28 | Major | Added TK001.1 (implementation artifact architecture comparative analysis) between TK001 and TK002 with parallel dependency. Updated TK002 Depends On to include TK001.1. Expanded TK002 scope to include LLM_Assistant role formalization, TK001.1 findings integration, cross-model Implementation Detail requirements, and enforcement modalities. Expanded TK004 deliverable list to include remediation-specification template. Added remediation-specification template to Links Register. Industry research integration commissioned per client request. |
```

---

## IV. IMPLEMENTATION SEQUENCE

**Recommended execution order:**

1. **SPEC-001** — TK001 §III industry/agentic evidence base (independent)
2. **SPEC-002** — TK001 §IV new gaps GAP-009/010/011 (independent of SPEC-001)
3. **SPEC-003** — TK001 frontmatter, Executive Summary, Scope, Changelog (depends on SPEC-001 + SPEC-002)
4. **SPEC-004** — TK002 convention rationale industry citations (independent)
5. **SPEC-005** — TK002 new conventions CONV-022/023 (depends on SPEC-004)
6. **SPEC-006** — TK002 enforcement modalities §III.C (depends on SPEC-005)
7. **SPEC-007** — TK002 decision requests DEC-008/009, DEC-004 update (depends on SPEC-005)
8. **SPEC-008** — TK002 impact/risk updates (depends on SPEC-007)
9. **SPEC-009** — TK002 external references, frontmatter, changelog (depends on SPEC-004 through SPEC-008)
10. **SPEC-010** — AC006 plan amendment: TK001.1 + task register + version bump (independent of SPEC-001 through SPEC-009)

**Parallelization note**: SPEC-001/002 (TK001 updates) and SPEC-004 (TK002 convention update) can execute in parallel. SPEC-010 (plan amendment) can execute in parallel with all other SPECs.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/plan_T104-PH001-ST008-AC006.md` |
| TK001 Gap Analysis (target) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/analysis/analysis_T104-PH001-ST008-AC006_implementation-governance-gap-analysis.md` |
| TK002 Standards-Input Proposal (target) | `prompt/artifacts/tasks/T104/workspace/PH001/ST008/AC006/proposal/proposal_T104-PH001-ST008-AC006_governance-input-disposition.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Task-Specification Template | `prompt/templates/consultant/workspace/template_workspace_implementation_task-specification.md` |
| Remediation-Specification Template | `prompt/templates/consultant/workspace/template_workspace_implementation_remediation-specification.md` |
| Workspace Documentation Rules | `prompt/templates/consultant/workspace/workspace_documentation_rules.md` |
| Reference Implementation (Block A pattern) | `prompt/artifacts/tasks/T102/workspace/PH001/ST002/AC000/implementation/implementation_T102-PH001-ST002-AC000_block-a-planning-housekeeping.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-03-28 | Initial | Implementation specification authored for AC006 research integration and plan amendment. Ten SPEC items covering: TK001 industry/agentic evidence grounding (SPEC-001/002/003), TK002 convention citation and expansion (SPEC-004/005/006/007/008/009), and AC006 plan amendment with TK001.1 insertion (SPEC-010). Three new gaps (GAP-009/010/011), two new conventions (CONV-022/023), two new decision requests (DEC-008/009), CONV-018 revised to risk-based model, CONV-015 expanded with cross-model Implementation Detail authoring sub-rule, enforcement modalities section, and external standards references. |
