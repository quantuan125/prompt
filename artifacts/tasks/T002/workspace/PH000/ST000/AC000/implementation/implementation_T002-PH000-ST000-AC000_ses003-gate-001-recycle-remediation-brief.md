---
artifact_type: 'IMPLEMENTATION'
implementation_type: 'task_specification'
initiative_id: 'T002'
initiative_code: 'TECOM'
phase: '0'
stream_id: 'T002-PH000-ST000'
activity_id: 'T002-PH000-ST000-AC000'
task_id: 'T002-PH000-ST000-AC000-TK002.4'
gate_id: 'T002-PH000-ST000-AC000-GATE-001'
version: '1.2.0'
date: '2026-04-04'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md'
proposal_reference: 'prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-001_gate-disposition.md'
execution_audience: 'assistant'
purpose: 'Assistant-scoped execution contract for the next-session GATE-001 RECYCLE remediation cycle: governance reset, research brief production, hypothesis brief major revision, comparative assessment creation, SPS/roadmap update, and in-plan registration of the recycled external review task'
---

# IMPLEMENTATION (Task Specification): T002 SES003 GATE-001 RECYCLE Remediation Brief

## I. PURPOSE & AUTHORITY

- Purpose: Specify the implementation details that will be consumed in the next session to reset GATE-001 into an explicit RECYCLE loop and execute the approved remediation work. The underlying remediation need was triggered by the client's SES003/SES004 consultation assessment that the existing GATE-001 package is substantively insufficient: the hypothesis brief's Options A/B/C framework does not reflect the revised proposal set (P0-P4 + deferred orchestration), the comparative analysis is misplaced, critical gap/risk items are missing, and the SPS also requires the approved `III.B` realignment.
- Authority chain: The governing activity plan (`plan_T002-PH000-ST000-AC000.md`) remains the tracked-work authority. The gate-disposition proposal (`proposal_T002-PH000-ST000-AC000-GATE-001_gate-disposition.md`) is the triggering proposal surface. This artifact is the execution contract that specifies HOW the commissioned assistant execution must amend the plan and produce the remediation artifacts in the next session. It does not itself execute those deliverables in the current authoring session.
- Audience: `LLM_Assistant` in the next session. The consultant's role in this session is to finalize this contract so delegated execution can proceed without relying on unstated assumptions.
- Filename note: This is an assistant-scoped orchestration artifact and uses the `-brief` naming convention per CONV-022.
- This artifact does NOT hold a GDR. Gate decisions remain in the gate-disposition proposal.

## II. TASK SCOPE

- Governing plan tasks: `TK002.4`, `TK002.5`, `TK002.6`, `TK002.7`
- Trigger: Client SES003 consultation determined that the GATE-001 package requires substantive revision based on: (a) revised proposal framework (P0-P4 replacing Options A/B/C), (b) Codex GPT 5.4 adversarial review findings (GAP-006, GAP-007, RISK-001 through RISK-003), (c) client direction to extract comparative analysis into a dedicated artifact, (d) client direction to produce a research brief for deferred agentic CLI capability research, and (e) approved standards-input authority for SPS `III.B` realignment.
- Deliverable contract: (1) amended plan with GATE-001 RECYCLE remediation tasks registered in the correct same-gate recycle order, including a recycled external review task with a proper task ID, (2) research brief at `research/T002-RES-001/`, (3) revised hypothesis brief, (4) new comparative assessment artifact, and (5) updated SPS and roadmap. This artifact is the next-session execution contract for SPEC-001 through SPEC-006. `TK002.8` remains planning-scope only in this brief: it is registered in-plan but not executed here.

## III. SPECIFICATION ITEMS

### SPEC-001 — Amend the Governing Activity Plan (TK002.4, Part A)

| Field | Detail |
|:--|:--|
| Requirement Source | SES004 RECYCLE consultation plus 2026-04-04 QA direction: governance reset is the primary amendment surface and MUST register the recycled external review as a future same-gate task |
| Target file(s) | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md` |
| Required end-state posture | Plan v3.0.0: GATE-001 is reset into an explicit same-gate RECYCLE loop; the Task Register places GATE-001 before the recycle remediation tasks; the recycle loop includes TK002.4 through TK002.7 plus a new recycled external review task `TK002.8`; GATE-001 depends on `TK002.8`; downstream TK003-TK006 remain blocked behind the same gate; and the changelog records the RECYCLE governance reset. |
| Explicit non-target / do-not-change constraints | Do NOT alter TK000 through TK002.3 other than preserving them as completed lineage. Do NOT alter the two-gate structure. Do NOT change TK003-TK006 sequencing or dependencies. Do NOT alter GATE-002 or its dependencies. Do NOT create detailed implementation-level sections for TK002.5-TK002.7 in the plan beyond summary contract stubs that reference this brief. Do NOT specify how TK002.8 executes; only register its task authority and plan-level contract. |
| Validation check | (1) Task Register places `GATE-001` immediately before TK002.4-TK002.8. (2) Task Register contains TK002.4, TK002.5, TK002.6, TK002.7, and `TK002.8` with correct IDs, owners, dependencies, and targets. (3) `GATE-001` shows `Status: in_progress` and `Depends On: TK002.8`. (4) The detailed GATE-001 section explicitly describes the same-gate recycle loop and the recycled external review as a prerequisite to re-disposition. (5) Version is `3.0.0`. (6) Changelog entry exists for v3.0.0. |
| Blocking ambiguity rule | If adding these tasks would conflict with existing gate sequencing or require restructuring the two-gate model, STOP and escalate to the consultant. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md`.
2. Update frontmatter:
   1. Set `version` to `'3.0.0'`.
   2. Set `date` to the execution date of the amendment session.
3. In the Task Register table (Section II), keep `TK000` through `TK002.3` unchanged as completed lineage.
4. Move `GATE-001` so it remains the governing row immediately before the recycle-loop tasks and immediately before the downstream blocked tasks (`TK003+`). Do not create a new gate ID.
5. Immediately AFTER the `GATE-001` row, insert five new rows in this order. The first four are the remediation tasks already governed by this implementation brief; the fifth is the recycled external review task that is registered in-plan only:

   Row 1:
   - Task: `TK002.4`
   - Task ID: `T002-PH000-ST000-AC000-TK002.4`
   - Name: `GATE-001 RECYCLE governance reset + research brief production`
   - Status: `planned`
   - Owner: `LLM_Consultant`
   - Depends On: `GATE-001`
   - Target: `plan_T002-PH000-ST000-AC000.md`, `research/T002-RES-001/`
   - Reference: `guideline_workspace_plan.md`, `template_research_brief.md`
   - Action: `Reset GATE-001 into a same-gate recycle loop and commission the research brief artifact for later execution.`

   Row 2:
   - Task: `TK002.5`
   - Task ID: `T002-PH000-ST000-AC000-TK002.5`
   - Name: `Hypothesis brief major revision`
   - Status: `planned`
   - Owner: `LLM_Consultant`
   - Depends On: `TK002.4`
   - Target: `analysis/`
   - Reference: `guideline_workspace_analysis.md`
   - Action: `Major revision: replace Options A/B/C with P0-P4 + deferred orchestration; update gap/risk register; revise hypothesis statement; extract comparative matrix.`

   Row 3:
   - Task: `TK002.6`
   - Task ID: `T002-PH000-ST000-AC000-TK002.6`
   - Name: `Comparative assessment (NEW artifact)`
   - Status: `planned`
   - Owner: `LLM_Consultant`
   - Depends On: `TK002.5`
   - Target: `analysis/`
   - Reference: `guideline_workspace_analysis.md`
   - Action: `Create comparative_analysis subtype: evaluation methodology, criteria, weighting, and scoring for P0-P4 + deferred orchestration.`

   Row 4:
   - Task: `TK002.7`
   - Task ID: `T002-PH000-ST000-AC000-TK002.7`
   - Name: `SPS + Roadmap update`
   - Status: `planned`
   - Owner: `LLM_Consultant`
   - Depends On: `TK002.5`
   - Target: `ssot/sps_T002.md`, `ssot/roadmap_T002.md`
   - Reference: `guideline_ssot_sps.md`, `guideline_workspace_roadmap.md`
   - Action: `Update SPS problem framing and `III.B` authority surface; update roadmap delivery snapshot and open questions register.`

   Row 5:
   - Task: `TK002.8`
   - Task ID: `T002-PH000-ST000-AC000-TK002.8`
   - Name: `Recycled external review (GATE-001)`
   - Status: `planned`
   - Owner: `LLM_Subconsultant`
   - Depends On: `TK002.7`
   - Target: `analysis/`
   - Reference: `guideline_workspace_analysis.md`
   - Action: `Future same-gate external review of the remediated GATE-001 package. Register task authority only in this amendment; execution is not specified by this brief.`

6. Update the `GATE-001` row:
   1. Keep `Status` as `in_progress`.
   2. Change `Depends On` from `TK002.3` to `TK002.8`.
   3. Change `Action` to: `Gate reset to RECYCLE posture. Same-gate remediation and recycled external review required before re-disposition.`
7. Update the detailed `GATE-001` section:
   1. Revise the entry criteria so the recycle loop requires TK002.4 through TK002.8 rather than the pre-recycle package-refresh path alone.
   2. Keep the same gate ID and the same gate-disposition proposal path.
   3. Add a short recycle re-entry note making clear that the gate remains open, remediation occurs under the same gate, and the recycled external review is the final prerequisite before the refreshed proposal can be re-presented.
8. Add or amend detailed task sections after the `GATE-001` section so dependency order is readable:
   1. `TK002.4` through `TK002.7` receive summary contract stubs only, each pointing back to this implementation brief for execution detail.
   2. `TK002.8` receives a summary task section with:
      - Purpose: independent second-opinion review of the remediated GATE-001 package
      - Deliverable: recycled external review analysis artifact under `analysis/`
      - Scope: review the remediated package only; confirm readiness for re-disposition; remain advisory and do not close the gate
      - Out of scope: authoring the proposal GDR, performing client disposition, or re-reviewing the superseded pre-recycle package as if it were current
      - Steps: high-level summary only
9. Add a changelog entry at the bottom of the file:
   - Version: `v3.0.0`
   - Date: execution date of the amendment session
   - Type: `Amendment`
   - Summary: `SES004 GATE-001 governance reset: converted GATE-001 into an explicit same-gate RECYCLE loop, registered TK002.4 through TK002.8 after the gate row, preserved TK002.3 and earlier work as lineage, and added the recycled external review as a future prerequisite to re-disposition. Implementation detail remains governed by implementation/implementation_T002-PH000-ST000-AC000_ses003-gate-001-recycle-remediation-brief.md.`

---

### SPEC-002 — Produce the Agentic CLI Orchestration Research Brief (TK002.4, Part B)

| Field | Detail |
|:--|:--|
| Requirement Source | SES003 consultation: client directed production of a research brief to commission deferred agentic CLI capability research |
| Target file(s) | `prompt/artifacts/tasks/T002/research/T002-RES-001/brief_T002-RES-001_agentic-cli-orchestration-research.md` |
| Required end-state posture | A complete research brief following `prompt/templates/researcher/template_research_brief.md` that scopes the agentic CLI capability research needed to ground the TECOM advisory. The brief commissions the research; the actual research report is deferred to a subsequent session. |
| Explicit non-target / do-not-change constraints | Do NOT produce the research report itself. Do NOT create an analysis artifact for research synthesis — that comes after the report is produced. Do NOT modify any existing artifacts in this SPEC. |
| Validation check | (1) File exists at the specified path. (2) All template sections are populated (I through IX). (3) Research scope covers: Claude Code capabilities (hooks, subagents, SDK/headless, scheduled triggers, GitHub Actions, MCP), Codex CLI capabilities (skills, spawn_agent, scheduled automations), execution substrate taxonomy (interactive vs headless vs scheduled), multi-agent cost/token implications, and industry orchestrator patterns grounded in agentic CLI realities. (4) Input packet references T002 SSOT artifacts. (5) Success criteria are defined. |
| Blocking ambiguity rule | If the research scope appears to require TECOM-internal information (their actual skill files, tool inventory) that is not yet available, scope those topics as explicitly deferred to post-discovery and mark them as such. Do NOT invent or assume TECOM-specific details. |
| Status | `open` |

#### Implementation Detail

1. Create the directory `prompt/artifacts/tasks/T002/research/T002-RES-001/` if it does not exist.
2. Create the file `brief_T002-RES-001_agentic-cli-orchestration-research.md` at that path.
3. Use `prompt/templates/researcher/template_research_brief.md` as the structural template.
4. Populate the frontmatter:
   - `artifact_type`: `'BRIEF'`
   - `initiative_id`: `'T002'`
   - `epic_id`: `'—'`
   - `research_id`: `'T002-RES-001'`
   - `version`: `'1.0.0'`
   - `iteration`: `'1'`
   - `date`: execution date of the research-brief authoring session
   - `status`: `'draft'`
   - `author`: `'LLM_Consultant'`
   - `decision_owner_role`: `'Client'`
5. Populate Section I (Executive Summary):
   - **Context**: The T002 TECOM advisory initiative requires grounding in the actual capabilities of agentic CLI tools (Claude Code, Codex CLI) to ensure architectural recommendations are technically feasible. SES003 consultation identified that the original hypothesis brief's Options A/B/C lacked this grounding, leading to abstract recommendations disconnected from what TECOM can actually build. This research brief commissions the investigation needed to fill that gap.
   - **Objective**: Map the current agentic CLI ecosystem capabilities relevant to TECOM's workflow automation needs, identify technical constraints and cost implications, and provide evidence that grounds the revised P0-P4 proposal framework.
   - **Target Deliverable**: A research report consumed by the LLM_Consultant to inform the hypothesis brief revision, comparative assessment, and eventual advisory note. The report will be synthesized into an analysis artifact (`research_synthesis` subtype) before feeding the advisory.
6. Populate Section II (Research Scope & Topics) with the following structure:

   **Part A: Current Agentic CLI Capabilities**

   Topic 1: Claude Code Automation Primitives (High Priority)
   - Objective: What automation capabilities does Claude Code provide that are relevant to workflow orchestration?
   - Context: TECOM uses agentic CLI tools. The advisory must know what building blocks exist natively.
   - Specific Questions:
     - What are Claude Code hooks and what events can they trigger on? Can hooks be used for post-workflow reporting?
     - What are Claude Code subagents and how do they relate to skill-activated session contexts?
     - What does the Claude Code SDK/headless mode enable for unattended execution?
     - What are Claude Code scheduled triggers and how do they work for recurring tasks?
     - What are Claude Code GitHub Actions integrations and can they serve as a scheduling/orchestration substrate?
     - What are MCP servers and how do they bridge between tools?
   - Deliverable: Capability matrix (feature, description, TECOM relevance, constraints)

   Topic 2: Codex CLI Automation Primitives (High Priority)
   - Objective: What automation capabilities does Codex CLI provide that are relevant to workflow orchestration?
   - Context: TECOM may use Codex CLI (or Anti-Gravity). The advisory must cover both major agentic CLI ecosystems.
   - Specific Questions:
     - What are Codex CLI skills and how do they define end-to-end workflows?
     - How does `spawn_agent` work for sub-agent orchestration within Codex?
     - What scheduling and automation capabilities does Codex provide?
     - What are the differences between Claude Code and Codex CLI for multi-agent workflows?
   - Deliverable: Capability matrix (parallel structure to Topic 1)

   Topic 3: Execution Substrate Taxonomy (High Priority)
   - Objective: What execution models are available and how do they map to different workflow types?
   - Context: GAP-006 identified that TECOM's workflows have not been classified by execution substrate. This topic provides the taxonomy needed for that classification.
   - Specific Questions:
     - What types of workflows require interactive CLI sessions vs headless/SDK execution vs external scheduler (cron, GitHub Actions)?
     - What are the permission/credential constraints for each execution model?
     - What happens when an interactive-only workflow is run in an unattended context?
     - How do approval checkpoints work in headless mode?
   - Deliverable: Execution substrate taxonomy table (model, description, suitable workflow types, constraints, TECOM applicability)

   **Part B: Cost, Constraints, and Risk Factors**

   Topic 4: Multi-Agent Cost and Token Implications (Medium Priority)
   - Objective: What are the cost and context-window implications of running multiple agents for a small company?
   - Context: RISK-002 identified token/cost expansion as a concern. This topic provides the evidence base.
   - Specific Questions:
     - What is the typical token cost per agent session for a workflow-length task?
     - How does multi-agent review (specialist + reviewer + aggregator) multiply costs?
     - What are practical cost management strategies (model selection, context trimming, caching)?
     - What monthly budget range should a 4-person company expect for a multi-agent workflow system?
   - Deliverable: Cost model table with scenarios (single agent, dual agent with review, full orchestration)

   Topic 5: Industry Orchestrator Patterns Grounded in Agentic CLI (Medium Priority)
   - Objective: What does "orchestration" actually mean in the agentic CLI context, as opposed to traditional distributed systems?
   - Context: The original hypothesis brief referenced Microsoft and Akka patterns. The client assessed these are too abstract. This topic grounds orchestration concepts in what CLI tools actually provide.
   - Specific Questions:
     - How do the concepts of "orchestrator," "supervisor," and "coordinator" map to agentic CLI primitives?
     - What patterns exist for agent-to-agent communication in CLI-based systems (shared filesystem, structured outputs, MCP)?
     - What are documented failure modes and mitigation patterns for multi-agent CLI workflows?
     - What open-source frameworks or community patterns exist for agentic CLI orchestration (spec-kit, superpowers, agent-os, get-shit-done)?
   - Deliverable: Pattern mapping table (abstract pattern, CLI implementation, documented examples, TECOM relevance)

   **Part C: TECOM-Specific Applicability (Deferred to Post-Discovery)**

   Topic 6: TECOM Workflow-to-Substrate Mapping (Deferred)
   - Objective: Map each of TECOM's 10 tools and workflows to the appropriate execution substrate.
   - Context: This requires visibility into TECOM's actual skill files and tool inventory, which is not yet available. Deferred until the PH000 discovery session (pre-April 10).
   - Specific Questions: Deferred.
   - Deliverable: Deferred. Placeholder for post-discovery enrichment.

7. Populate Section III (Constraints, Assumptions & Methodology):
   - Constraints:
     - Boundary: External web research + publicly available documentation only. No access to TECOM internal systems.
     - Timebox: Single research session.
   - Assumptions:
     - Claude Code documentation at `docs.anthropic.com` is the authoritative source for Claude Code capabilities.
     - OpenAI documentation is the authoritative source for Codex CLI capabilities.
     - TECOM's actual tool inventory and skill files are not available; Topic 6 is explicitly deferred.
   - Methodology:
     1. Official documentation (Anthropic, OpenAI) — Highest authority
     2. Open-source project documentation (spec-kit, superpowers, agent-os) — Secondary authority
     3. Community/blog content — Tertiary authority (corroborate only)

8. Populate Section IV (Cross-Topic Integration):
   - Integration Question 1: How do Topic 1 (Claude Code) and Topic 2 (Codex CLI) capabilities compare for TECOM's likely workflow types? Are they complementary or competing?
   - Integration Question 2: How does Topic 3 (execution substrate taxonomy) constrain the applicability of Topics 4-5 (cost and orchestration patterns)?
   - Gap Analysis: What capabilities are missing in the current agentic CLI ecosystem that would be needed for full orchestration? What workarounds exist?

9. Populate Section V (Input Packet):
   - Core Governance:
     - SSOT: `prompt/artifacts/tasks/T002/ssot/sps_T002.md`
     - Plan: `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md`
   - Reference Artifacts:
     - `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md`
     - `prompt/artifacts/tasks/T002/raw_T002-PH000.txt`
     - `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/implementation/implementation_T103-PH000-ST000-AC001_orchestration-execution-patterns.md`
   - Anti-Patterns / Exclusions:
     - IGNORE: Do not reference TECOM internal systems or skill files (not available)

10. Populate Section VI (Deliverable Format Requirements):
    - The research report MUST use `prompt/templates/researcher/template_research_report.md`.
    - Section I: Provide a clear executive summary distinguishing what is known from current documentation vs what requires TECOM discovery.
    - Section III: Each topic finding must include a TECOM Relevance column or subsection.
    - Completeness: Do NOT delete empty sections. If a topic has no implications, explicitly state "None".

11. Populate Section VII (Issues & Risks Register):
    - Issues: Empty table (none identified at brief stage).
    - Risks:
      - `T002-RES-001-RISK-001`: Documentation currency — agentic CLI tools evolve rapidly; findings may be outdated within months. Status: `OPEN`. Priority: `Medium`. Mitigation: Date-stamp all findings; note documentation version/date.
      - `T002-RES-001-RISK-002`: Ecosystem divergence — Claude Code and Codex CLI may have fundamentally different orchestration models, making unified recommendation difficult. Status: `OPEN`. Priority: `Low`. Mitigation: Present capabilities side-by-side; let the advisory note recommend based on TECOM's primary tool.

12. Populate Section VIII (Critical Dependencies):
    - `T002-PH000-ST000-AC000-TK002.5`: Topic 1-5 findings will inform the hypothesis brief revision (P0-P4 grounding).
    - `T002-PH000-ST000-AC000-TK002.6`: Topic 3-5 findings will provide evaluation criteria for the comparative assessment.
    - `T002-PH000-ST000-AC000-TK003`: Full research synthesis will feed the advisory note English SSOT.

13. Populate Section IX (Success Criteria):
    - Topics 1-5 each have a populated deliverable table/matrix.
    - Topic 6 is explicitly marked as deferred with rationale.
    - Cross-topic integration section addresses both integration questions.
    - The report provides sufficient evidence to distinguish "what is buildable today" from "what requires custom development" for each proposal in the P0-P4 framework.
    - Cost model provides actionable budget guidance for a 4-person company.

---

### SPEC-003 — Revise the Hypothesis Brief (TK002.5)

| Field | Detail |
|:--|:--|
| Requirement Source | SES003 consultation: client assessed Options A/B/C as premature and insufficient; revised to P0-P4 proposal framework |
| Target file(s) | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md` |
| Required end-state posture | Hypothesis brief v2.0.0: (1) Section V replaces Options A/B/C with the P0-P4 + deferred orchestration proposal framework; (2) Section IV gap register includes GAP-006, GAP-007, RISK-001 through RISK-003; (3) Section VI hypothesis statement revised to reflect "orchestration as validated endpoint, not assumed destination" with "no orchestration as valid final state"; (4) Comparative analysis matrix REMOVED from this artifact (stub reference to new comparative assessment artifact); (5) Research brief referenced as pending input; (6) Analysis type remains `assessment`. |
| Explicit non-target / do-not-change constraints | Do NOT alter Sections I-III except as needed to align the executive summary and scope with the revised content. Do NOT alter Section VII (Engagement Context) — it remains unchanged. Do NOT create the comparative assessment artifact in this SPEC (that is SPEC-004). Do NOT alter the analysis_type — it remains `assessment`. |
| Validation check | (1) Version is `2.0.0`. (2) Section V contains P0-P4 descriptions, NOT Options A/B/C. (3) No weighted scoring matrix exists in this artifact. (4) A stub reference points to the comparative assessment artifact path. (5) Gap register contains GAP-006, GAP-007, RISK-001 through RISK-003. (6) Hypothesis statement includes "no orchestration" as an explicit valid final state. (7) Research brief is referenced as pending input. (8) Changelog entry exists for v2.0.0. |
| Blocking ambiguity rule | If the revision would require changing the analysis_type from `assessment` to a different type, STOP and escalate. If the revision would require altering the Engagement Context (Section VII), STOP and escalate. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md`.
2. Update frontmatter:
   1. Set `version` to `'2.0.0'`.
   2. Set `date` to the execution date of the hypothesis-brief revision session.
   3. Set `task_id` to `'T002-PH000-ST000-AC000-TK002.5'`.
   4. Update `purpose` to: `'Assess TECOM agent workflow improvement options and formalize the hypothesis for PH000 discovery — revised from Options A/B/C to P0-P4 incremental proposal framework with deferred orchestration'`.
   5. Update `assessment_scope` to: `'TECOM agentic workflow improvement — incremental proposal framework (P0-P4) with orchestration as validated endpoint'`.
3. Revise Section I (Executive Summary):
   1. Update **Purpose** to reflect the revised scope: assessing incremental improvement proposals rather than architecture selection.
   2. Update **Scope** to mention P0-P4 framework.
   3. Update **Conclusion / Recommendation** to: A phased, incremental improvement approach — starting with workflow census (P0), then domain-specific review policies (P1), structured report schemas (P2), skill-level improvements (P3), and contingent self-improvement capability (P4) — is recommended over immediate orchestrator architecture selection. Orchestration is the validated endpoint, not the starting point. "No orchestration" is explicitly allowed as a successful final state if P0-P3 resolve the coordination bottleneck without it.
4. Revise Section II (Scope & Inputs):
   1. Add to **In scope**: the P0-P4 proposal framework, SES003 consultation findings, Codex GPT 5.4 SES003 adversarial review findings, and the research brief as a pending input.
   2. Add to **Inputs reviewed**: `prompt/artifacts/tasks/T002/research/T002-RES-001/brief_T002-RES-001_agentic-cli-orchestration-research.md` (noted as pending — research report not yet produced).
   3. Add to **Inputs reviewed**: `SES003 Codex GPT 5.4 adversarial review (session output, 2026-04-03; findings integrated into this revision)`.
5. Revise Section III (Evidence / Methodology):
   1. Add step 6 to the Method list: `Conducted SES003 consultation reassessment with client — identified that Options A/B/C framework is premature; converged on P0-P4 incremental proposal framework`.
   2. Add step 7: `Commissioned SES003 adversarial review via Codex CLI (GPT 5.4, high reasoning) — identified GAP-006, GAP-007, RISK-001 through RISK-003 and challenged Proposal 4 risk level`.
   3. Add step 8: `Commissioned agentic CLI orchestration research brief (T002-RES-001) — deferred to next session for execution`.
6. Revise Section IV (Findings / Gap Register):
   1. Keep GAP-001 through GAP-005 unchanged.
   2. Update GAP-005 disposition from `accepted_as_is` to `mitigated` with notes: `Mitigated by allowing "no orchestration" as a valid final state and framing P0-P4 as incremental validation gates rather than a committed build plan.`
   3. Add the following new rows:

   GAP-006:
   - GAP ID: `GAP-006`
   - Category: `technical`
   - Title: `Execution substrate per workflow undefined`
   - Description: `TECOM's workflows have not been classified by execution model (interactive CLI session, headless/SDK, external scheduler). This determines what is technically buildable for each workflow. Identified by SES003 Codex adversarial review.`
   - Disposition: `pending_decision`
   - Downstream Target: `T002-RES-001 (Topics 3, 6) and PH000 discovery session`
   - Notes: `Topic 3 of research brief provides the taxonomy; Topic 6 (deferred) maps TECOM workflows to it`

   GAP-007:
   - GAP ID: `GAP-007`
   - Category: `governance`
   - Title: `Skill ownership and change governance undefined`
   - Description: `No one has defined who owns each skill, who can change prompts, how changes are tested, or how failures are rolled back. Critical if Proposal 4 (self-improvement skill) enters scope. Identified by SES003 Codex adversarial review.`
   - Disposition: `pending_decision`
   - Downstream Target: `PH000 discovery session`
   - Notes: `Prerequisite for P4; informative for P1-P3`

   RISK-001:
   - GAP ID: `RISK-001`
   - Category: `adoption`
   - Title: `Proposal stack perceived as overengineering`
   - Description: `The P0-P4 framework plus deferred orchestration could overwhelm a 4-person company if presented as a committed build plan rather than incremental validation gates. Identified by SES003 Codex adversarial review and consultant assessment.`
   - Disposition: `accepted_as_is`
   - Downstream Target: `Advisory note framing (TK003)`
   - Notes: `Mitigated by framing: each proposal is validated independently before the next is attempted; TECOM can stop at any point`

   RISK-002:
   - GAP ID: `RISK-002`
   - Category: `cost`
   - Title: `Token/cost expansion with multi-agent review`
   - Description: `Multi-agent review plus aggregation can multiply token usage. For a 4-person company, costs must be measured before recommending layered agents. Identified by SES003 Codex adversarial review.`
   - Disposition: `pending_decision`
   - Downstream Target: `T002-RES-001 (Topic 4) and PH001 implementation`
   - Notes: `Research brief Topic 4 commissions cost model investigation`

   RISK-003:
   - GAP ID: `RISK-003`
   - Category: `technical`
   - Title: `Approval friction in unattended execution`
   - Description: `Agentic CLI workflows may break when moved from interactive to unattended execution due to permissions, credentials, or prompts requiring human intervention. Identified by SES003 Codex adversarial review.`
   - Disposition: `pending_decision`
   - Downstream Target: `T002-RES-001 (Topic 3) and PH000 discovery session`
   - Notes: `Execution substrate taxonomy (Topic 3) will clarify which workflows can go headless`

7. REPLACE Section V (Assessment) entirely. Remove ALL of the existing content under Section V including Section V header, subsections A/B/B2/B3/C, all three option tables, the evaluation criteria table, the comparative assessment matrix, the weighted scores table, and the recommendation text. Replace with the following new content:

   Section heading: `## V. ASSESSMENT (READINESS / OPTIONS / TRADEOFFS)`

   Subsection `### A. Current State Summary` — Keep the existing current-state description of TECOM's operational context (4-person company, 10 tools, 90% AI utilization, manual coordination bottleneck, no structured documentation, human review required). Update the final paragraph to note that the CEO's binary question (centralized vs independent) was the starting point but the revised assessment identifies a wider solution space.

   Subsection `### B. Revised Proposal Framework` — This replaces the former Options A/B/C. Describe the following proposals:

   **Proposal P0: Workflow Census and Failure Baseline**
   - What: Map TECOM's 10-tool workflow end-to-end: data sources, handoff points, review checkpoints, current failure/rework rates, and execution substrate per workflow (interactive vs headless vs scheduled).
   - Why: Every other proposal depends on understanding what currently exists. Without this, recommendations remain abstract.
   - Prerequisite for: P1, P2, P3, P4, and orchestration.
   - Timing: PH000 discovery session (pre-April 10).
   - Source: Elevated from GAP-001/GAP-002 based on SES003 consultation and Codex adversarial review.

   **Proposal P1: Domain-Specific Review Policies with Shared Reporting Contract**
   - What: Instead of one generic "review agent," create artifact-specific review modules — different rubrics, tolerances, and source checks for different work types (product images, copy, supplier data, pricing, operational reports). All review modules share a common reporting contract (structured output format).
   - Why: Directly addresses the CEO's stated pain ("human review required on all AI outputs"). A single generic review agent creates false confidence because reviewing images requires different criteria than reviewing supplier data.
   - Prerequisite for: Orchestration (review quality must be proven before automated aggregation).
   - Implementation: Each review module is a Claude Code/Codex skill with its own system prompt and domain-specific acceptance criteria.
   - Source: SES003 consultation (client proposal), refined by Codex adversarial review (artifact-specific decomposition).

   **Proposal P2: Structured Report Schema with Machine-Checkable Validation**
   - What: Define a structured report schema for all workflow outputs — not just standardized prose templates, but machine-checkable fields: required fields, status taxonomy, unique job IDs, timestamps, provenance/source links, pass/fail semantics, retry/error codes, and next-action codes.
   - Why: This is the single highest-value intervention. Standardized, machine-readable output is the prerequisite that makes future orchestration trivially composable. Without it, any "thin reporting layer" becomes a fragile summarizer over inconsistent prose.
   - Prerequisite for: Orchestration (agents cannot aggregate what they cannot parse).
   - Implementation: Schema definition + validation checks integrated into each skill's workflow.
   - Source: SES003 consultation (client proposal), hardened by Codex adversarial review (schema-first, not template-first).

   **Proposal P3: Incremental Skill-Level Improvements**
   - What: Fix the atomic units (individual skills/workflows) before adding orchestration on top. Each skill improvement delivers standalone value immediately.
   - Why: Orchestration on top of broken or inconsistent sub-workflows amplifies problems. Lean Startup principle: validate incrementally with the smallest valuable slice.
   - Implementation: Improve one skill at a time, starting with the highest-urgency domain (likely order tracking, pending P0 census).
   - Source: SES003 consultation (client proposal).

   **Proposal P4: Self-Improvement Skill + Maintenance System (Contingent — Deferred)**
   - What: Develop a meta-skill that allows TECOM's agentic CLI to improve its own skill system incrementally, with a maintenance system that updates skills when standards/PIDs change.
   - Why: Avoids manual skill-by-skill maintenance as the system grows.
   - Contingency: Explicitly deferred until P1-P3 are mature and TECOM has: stable skill ownership, version control for prompts/skills, acceptance tests, and rollback processes. Building this before those prerequisites exist creates governance risk (version drift, silent regressions, prompt mutation) without proportional value.
   - Source: SES003 consultation (client addition), risk-assessed by Codex adversarial review (highest-risk, not highest-leverage).

   **Deferred: Orchestration Layer**
   - What: A coordination layer that aggregates outputs from specialist skills into a unified CEO daily brief.
   - Why deferred: The CEO's original question assumed orchestration is the solution. The revised assessment determines that orchestration is the last step, not the first — and it may not be needed if P0-P3 resolve the coordination bottleneck independently.
   - Threshold for introduction: Orchestrate only the top 2-3 workflows once they have stable schemas, measurable quality, and known failure modes. Perfection is not required; observability is.
   - Valid final state: "No orchestration" — independent, well-instrumented agents with a simple digest layer — is explicitly allowed as a successful endpoint.
   - Source: SES003 consultation (consultant + client aligned position), validated by Codex adversarial review.

   Subsection `### C. Recommendation` — State the following:

   Recommend the P0-P4 incremental framework with deferred orchestration. The key insight from SES003 is that the CEO's binary question (one central manager vs many independent agents) is a false dichotomy. The real solution space is wider and requires understanding the actual agentic CLI capabilities, the specific workflow bottlenecks, and the incremental improvement opportunities before committing to any architecture.

   The recommended sequence is: P0 (workflow census) -> P1 (review policies) -> P2 (report schema) -> P3 (skill improvements) -> P4 (contingent on P1-P3 maturity) -> Orchestration (only if validated).

   Each proposal is independently valuable and independently testable. TECOM can stop at any point where the coordination bottleneck is sufficiently reduced.

   Note: The detailed comparative analysis (evaluation criteria, weighting, scoring) for the P0-P4 framework is maintained in a dedicated artifact: `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_comparative-assessment.md`.

   Note: The agentic CLI capability research that grounds these proposals is commissioned via research brief `T002-RES-001`. The research report is pending; findings will be integrated into this assessment and the advisory note when available.

8. Revise Section VI (Hypothesis Statement):
   1. Replace the existing hypothesis with:

   > **If** TECOM implements an incremental improvement framework starting with workflow census (P0), then domain-specific review policies (P1), structured report schemas (P2), and skill-level improvements (P3),
   > **then** the CEO's daily coordination overhead will be measurably reduced at each stage, with orchestration introduced only when validated by evidence from the prior stages,
   > **as measured by**: (a) P0: complete workflow map with execution substrate classification for all 10 tools; (b) P1: review time per domain reduced and review accuracy maintained or improved; (c) P2: all active workflows produce machine-checkable status reports; (d) P3: individual workflow reliability improved (measurable via error/rework rate); (e) orchestration (if introduced): CEO receives a synthesized daily report and manual coordination touchpoints for automated domains drop to zero.

   2. Update hypothesis validation conditions:
   - **Validated** if: each proposal stage achieves its measurement target before the next stage begins.
   - **Partially validated** if: P0-P3 reduce coordination overhead sufficiently that orchestration is not needed. This is an acceptable final state.
   - **Invalidated** if: P0 discovery reveals that the coordination bottleneck is driven by irreducible domain judgment rather than information synthesis (ASSUM-001 fails), OR the agentic CLI capability research (T002-RES-001) reveals that the proposed improvements are technically infeasible within TECOM's tool ecosystem.
   - **If invalidated**: pivot to workflow documentation and process redesign rather than agent architecture.

   3. Update the critical assumption to test:
   - Keep ASSUM-001 (bottleneck nature) as the primary assumption.
   - Add: "The agentic CLI tools TECOM uses (Codex CLI, Claude Code, Anti-Gravity) provide sufficient automation primitives to support at minimum P1 and P2 without custom infrastructure development. This will be validated by T002-RES-001."

9. Do NOT modify Section VII (Engagement Context). It remains unchanged.

10. Revise Section VIII (Downstream Actions):
    1. Update the table to reflect the new artifact landscape:
    - Replace the Advisory Note (EN) row target with the same path but note it now depends on research report completion.
    - Add a row for the comparative assessment artifact.
    - Add a row for the research report (deferred).
    - Keep the SPS, Roadmap, PH000 Discovery Session, and Advisory Note (VI) rows but update trigger conditions as needed.

11. Update Section IX (References / Links Register):
    1. Add: Research Brief | `prompt/artifacts/tasks/T002/research/T002-RES-001/brief_T002-RES-001_agentic-cli-orchestration-research.md`
    2. Add: Comparative Assessment | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_comparative-assessment.md`
    3. Add: SES003 Codex Adversarial Review | Session output, 2026-04-03 (findings integrated into v2.0.0 revision)
    4. Add: SES003 Consultation Notes | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/snotes/snotes_T002-PH000-ST000-AC000-SES003.md` (pending creation)

12. Add changelog entry:
    - Version: `v2.0.0`
    - Date: execution date of the hypothesis-brief revision session
    - Type: `Major revision`
    - Summary: `SES003 GATE-001 RECYCLE remediation. Replaced Options A/B/C framework with P0-P4 incremental proposal set + deferred orchestration. Extracted comparative analysis to dedicated artifact. Updated gap register with GAP-006, GAP-007, RISK-001 through RISK-003 (sourced from SES003 Codex GPT 5.4 adversarial review). Revised hypothesis statement to reflect incremental validation and "no orchestration" as valid final state. Added research brief T002-RES-001 as pending input. Sections VII (Engagement Context) unchanged. Driven by SES003 client consultation assessment and Codex adversarial review.`

---

### SPEC-004 — Create the Comparative Assessment Artifact (TK002.6)

| Field | Detail |
|:--|:--|
| Requirement Source | SES003 consultation: client directed extraction of comparative analysis from hypothesis brief into dedicated artifact |
| Target file(s) | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_comparative-assessment.md` |
| Required end-state posture | A new `comparative_analysis` subtype analysis artifact per `guideline_workspace_analysis.md` and `template_workspace_analysis.md`. Hosts the evaluation methodology, criteria, weighting, and scoring for the P0-P4 + deferred orchestration proposal framework. Replaces the embedded A/B/C matrix that was removed from the hypothesis brief. |
| Explicit non-target / do-not-change constraints | Do NOT modify the hypothesis brief in this SPEC (that was done in SPEC-003). Do NOT include the full proposal descriptions here — reference the hypothesis brief for those. Do NOT alter any other existing artifacts. |
| Validation check | (1) File exists at specified path. (2) Frontmatter `analysis_type` is `'comparative_analysis'`. (3) Section V uses the COMPARATIVE_ANALYSIS template structure (A: Options Under Comparison, B: Evaluation Criteria & Weighting, C: Comparative Assessment Matrix, D: Recommendation). (4) All proposals (P0-P4 + Deferred Orchestration) are represented in the options table. (5) Evaluation criteria are weighted with percentage-based numeric weighting. (6) Each matrix cell includes both a grade and brief rationale. (7) Recommendation section includes dissenting considerations. |
| Blocking ambiguity rule | If the research brief findings (T002-RES-001) would materially change the evaluation criteria or option definitions, note this as a pending dependency and proceed with current best understanding. Do NOT block on pending research. |
| Status | `open` |

#### Implementation Detail

1. Create the file `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_comparative-assessment.md`.
2. Use `prompt/templates/consultant/workspace/template_workspace_analysis.md` as the structural template. Select the COMPARATIVE_ANALYSIS conditional sections; omit all other conditional sections (PATTERN_AUDIT, COMPLIANCE_AUDIT, ASSESSMENT, EXTERNAL_REVIEW, RESEARCH_SYNTHESIS).
3. Populate frontmatter:
   - `artifact_type`: `'ANALYSIS'`
   - `analysis_type`: `'comparative_analysis'`
   - `initiative_id`: `'T002'`
   - `initiative_code`: `'TECOM'`
   - `phase`: `'0'`
   - `stream_id`: `'T002-PH000-ST000'`
   - `activity_id`: `'T002-PH000-ST000-AC000'`
   - `task_id`: `'T002-PH000-ST000-AC000-TK002.6'`
   - `gate_id`: `'T002-PH000-ST000-AC000-GATE-001'`
   - `version`: `'1.0.0'`
   - `date`: execution date of the comparative-assessment authoring session
   - `status`: `'draft'`
   - `author`: `'LLM_Consultant'`
   - `decision_owner_role`: `'Client'`
   - `plan_reference`: `'prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md'`
   - `purpose`: `'Formal comparative analysis of the P0-P4 incremental proposal framework for TECOM agent workflow improvement, with deferred orchestration as the terminal comparison option'`
4. Populate Section I (Executive Summary):
   - **Purpose**: Provide a structured, weighted comparative evaluation of the revised proposal framework (P0-P4 + deferred orchestration) that was adopted in SES003 to replace the original Options A/B/C. This artifact hosts the evaluation methodology extracted from the hypothesis brief.
   - **Scope**: Evaluation of six comparison items: P0 (Workflow Census), P1 (Review Policies), P2 (Report Schema), P3 (Skill Improvements), P4 (Self-Improvement Skill, contingent), and Deferred Orchestration. Plus retention of the original A/B/C comparison as historical context.
   - **Conclusion / Recommendation**: The P0 -> P2 -> P1 -> P3 sequence represents the highest-value implementation path. P4 is contingent. Orchestration should be introduced only after P0-P3 are validated. The original Options A/B/C are superseded.
5. Populate Section II (Scope & Inputs):
   - In scope: Comparative evaluation of P0-P4 + deferred orchestration; historical context for superseded A/B/C options.
   - Out of scope: Proposal definitions themselves (those live in the hypothesis brief); TECOM-internal workflow details (pending discovery); research report findings (pending T002-RES-001).
   - Inputs reviewed:
     - `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md` (v2.0.0)
     - `prompt/artifacts/tasks/T002/ssot/sps_T002.md`
     - SES003 Codex GPT 5.4 adversarial review (session output, 2026-04-03)
     - SES003 consultation session findings
6. Populate Section III (Evidence / Methodology):
   - Method: Evaluation criteria derived from TECOM's stated pain points (raw transcript), SPS constraints, SES003 consultation findings, and Codex adversarial review. Weights reflect TECOM's 4-person company context with manual CEO coordination bottleneck.
7. Populate Section IV (Findings / Gap Register):
   - Note: `This artifact depends on the hypothesis brief (v2.0.0) for proposal definitions and the research brief (T002-RES-001) for agentic CLI capability grounding. The comparative scoring represents current best understanding and will be refreshed when the research report is available.`
   - No additional GAPs beyond those registered in the hypothesis brief.
8. Populate Section V (Comparative Analysis — Trade Study):

   Subsection A — Options Under Comparison:

   | Option | Label | Description |
   |:--|:--|:--|
   | P0 | Workflow Census & Failure Baseline | Map TECOM's 10-tool workflow: data sources, handoffs, review checkpoints, failure rates, execution substrates |
   | P1 | Domain-Specific Review Policies | Artifact-specific review modules with shared reporting contract; replaces generic "review agent" |
   | P2 | Structured Report Schema | Machine-checkable report schema with required fields, status taxonomy, job IDs, pass/fail semantics |
   | P3 | Incremental Skill Improvements | Fix individual skills/workflows before orchestration; each delivers standalone value |
   | P4 | Self-Improvement Skill (Contingent) | Meta-skill for systematic skill self-improvement + maintenance system; deferred until P1-P3 mature |
   | ORCH | Deferred Orchestration Layer | Coordination layer aggregating specialist outputs into unified CEO daily brief; introduced only when validated |
   | (Historical) A | Centralized Monolithic Orchestrator | Original Option A — superseded by P0-P4 framework |
   | (Historical) B | Fully Independent Agents | Original Option B — superseded by P0-P4 framework |
   | (Historical) C | Hybrid Specialist + Thin Reporting | Original Option C — evolved into the P0-P4 framework |

   Subsection B — Evaluation Criteria & Weighting:

   | Criterion | Definition | Weight |
   |:--|:--|:--|
   | CEO Coordination Reduction | Degree to which the proposal reduces manual CEO coordination overhead — the PRIMARY stated pain point | 25% |
   | Time to First Value | How quickly the proposal delivers initial measurable value to TECOM operations | 20% |
   | Technical Feasibility | Likelihood of successful implementation within TECOM's current agentic CLI ecosystem (pending T002-RES-001 validation) | 20% |
   | Complexity & Build Effort | Development and operational complexity appropriate for a 4-person team with no dedicated engineering staff | 15% |
   | Risk Profile | Likelihood and severity of failure modes, including adoption risk, cost expansion, and governance burden | 10% |
   | Composability | Degree to which the proposal enables or contributes to future orchestration capability | 10% |

   Weighting rationale: CEO Coordination Reduction remains highest (25%) as the explicit motivating question. Technical Feasibility is elevated to 20% (from implicit in the original matrix) because the SES003 assessment identified feasibility grounding as the primary gap. Composability replaces Scalability to better reflect the incremental framework's design logic.

   Subsection C — Comparative Assessment Matrix:

   Grading scale: 1 (worst) to 5 (best) for TECOM's context. Each cell must include both a grade and a brief rationale.

   | Criterion | Weight | P0 | P1 | P2 | P3 | P4 (Contingent) | ORCH (Deferred) | Notes |
   |:--|:--|:--|:--|:--|:--|:--|:--|:--|
   | CEO Coordination Reduction | 25% | **2** — Does not directly reduce coordination but is the prerequisite for all proposals that do | **4** — Reduces review bottleneck, one of two main coordination pain points | **3** — Standardized reports improve information flow but don't eliminate manual synthesis alone | **3** — Improved skill reliability reduces rework-driven coordination | **2** — Meta-improvement; indirect coordination benefit only | **5** — Direct: unified daily brief eliminates manual synthesis | P1 + P2 together approach ORCH's score |
   | Time to First Value | 20% | **5** — Immediate: mapping exercise produces actionable insights within one session | **3** — Moderate: requires P0 census + domain-specific rubric development per workflow type | **4** — Fast once P0 identifies workflows: schema definition is bounded | **4** — Fast per skill: each improvement delivers standalone value | **1** — Slow: requires P1-P3 maturity + governance prerequisites | **1** — Slowest: requires P0-P3 as prerequisites | P0 and P3 are fastest to value |
   | Technical Feasibility | 20% | **5** — No technical risk: human-driven discovery exercise | **4** — High: review skills are well-understood in agentic CLI; risk is domain rubric quality | **4** — High: structured output is a standard agentic CLI capability; risk is schema design quality | **4** — High per skill: individual skill improvement is routine | **2** — Medium: self-modifying skill systems raise version drift, regression, and rollback risks | **3** — Medium: depends on execution substrate compatibility (GAP-006) and state management (RISK-003) | Pending T002-RES-001 validation for P1-ORCH |
   | Complexity & Build Effort | 15% | **5** — Low: structured conversation, no development | **3** — Moderate: multiple review modules, each needs domain expertise | **3** — Moderate: schema design + per-skill integration of validation | **4** — Low per skill: bounded scope | **1** — High: versioning, tests, canaries, rollback, ownership governance | **2** — High: triggers, queueing, retries, deduplication, escalation rules | P4 and ORCH are highest complexity |
   | Risk Profile | 10% | **5** — Minimal risk: discovery exercise | **3** — Moderate: false confidence risk if rubrics are poorly designed | **4** — Low: schema errors are detectable and correctable | **4** — Low per skill: isolated blast radius | **1** — High: governance prerequisites unmet; version drift, silent regressions, prompt mutation | **2** — Moderate: approval friction (RISK-003), state concurrency, cost expansion (RISK-002) | P4 is highest risk in current framework |
   | Composability | 10% | **3** — Indirect: census enables composability but doesn't create it | **4** — High: shared reporting contract is a composability primitive | **5** — Highest: machine-checkable schema is THE composability enabler | **3** — Moderate: improved skills are more composable than broken ones | **4** — High: self-maintaining skills stay composable over time | **5** — Highest: orchestration IS composition | P2 is the key composability enabler |

   Weighted Scores:

   | Option | Calculation | Weighted Score |
   |:--|:--|:--|
   | **P0** | (2x25)+(5x20)+(5x20)+(5x15)+(5x10)+(3x10) = 50+100+100+75+50+30 | **405/500 (81%)** |
   | **P1** | (4x25)+(3x20)+(4x20)+(3x15)+(3x10)+(4x10) = 100+60+80+45+30+40 | **355/500 (71%)** |
   | **P2** | (3x25)+(4x20)+(4x20)+(3x15)+(4x10)+(5x10) = 75+80+80+45+40+50 | **370/500 (74%)** |
   | **P3** | (3x25)+(4x20)+(4x20)+(4x15)+(4x10)+(3x10) = 75+80+80+60+40+30 | **365/500 (73%)** |
   | **P4** | (2x25)+(1x20)+(2x20)+(1x15)+(1x10)+(4x10) = 50+20+40+15+10+40 | **175/500 (35%)** |
   | **ORCH** | (5x25)+(1x20)+(3x20)+(2x15)+(2x10)+(5x10) = 125+20+60+30+20+50 | **305/500 (61%)** |

   Subsection D — Recommendation:

   **Recommended implementation sequence**: P0 (81%) -> P2 (74%) -> P1 (71%) -> P3 (73%) -> [P4 if justified (35%)] -> ORCH if validated (61%).

   P0 scores highest because it is the lowest-risk, highest-feasibility prerequisite to everything else. P2 scores second because structured report schemas are the single most important composability enabler. P1 follows because review policies depend on P0 census data and benefit from P2's reporting contract. P3 is interleaved with P1/P2 in practice.

   **Dissenting considerations**:
   - ORCH scores highest on CEO Coordination Reduction (5/5) — the primary pain point. The incremental approach trades immediate coordination relief for lower risk and faster time to first value. If the CEO's coordination overhead is acute and growing, the deferred orchestration approach may feel too slow. The advisory note must explicitly acknowledge this trade-off.
   - P4 scores lowest (35%) primarily due to governance prerequisites (GAP-007) and technical risk. If TECOM develops strong governance through P1-P3, P4's risk profile improves significantly. The low score reflects current readiness, not inherent value.
   - The original Option C (Hybrid) is not "wrong" — it evolved into the P0-P4 framework. The key difference is implementation sequencing and granularity, not strategic direction.

   **Historical context**: The original Options A (46%), B (74%), C (76%) scoring from v1.1.0 of the hypothesis brief is preserved here for traceability. The P0-P4 framework supersedes this comparison. Option C's strategic direction (decentralized specialists + standardized aggregation) remains the destination; P0-P4 provides the implementation path to get there.

   **Pending dependency**: The Technical Feasibility scores for P1-ORCH are based on current best understanding and will be refreshed when the T002-RES-001 research report is available. Scores may shift if the research reveals unexpected constraints or capabilities.

9. Populate Section VIII (Downstream Actions):
   - Advisory Note (EN): `TK003` — comparative assessment feeds the recommendation framing.
   - Research Synthesis: `T002-RES-001 report` — when available, refresh Technical Feasibility scores.
   - Hypothesis Brief: cross-reference maintained via stub in v2.0.0 Section V.C.

10. Populate Section IX (References / Links Register):
    - Plan: `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md`
    - Hypothesis Brief: `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md`
    - SPS: `prompt/artifacts/tasks/T002/ssot/sps_T002.md`
    - Research Brief: `prompt/artifacts/tasks/T002/research/T002-RES-001/brief_T002-RES-001_agentic-cli-orchestration-research.md`
    - Raw Transcript: `prompt/artifacts/tasks/T002/raw_T002-PH000.txt`
    - SES003 Codex Adversarial Review: Session output, 2026-04-03

11. Add changelog entry:
    - Version: `v1.0.0`
    - Date: execution date of the comparative-assessment authoring session
    - Type: `Initial`
    - Summary: `Created comparative assessment for P0-P4 + deferred orchestration framework. Extracted from hypothesis brief v1.1.0 (which hosted the original A/B/C comparison) per SES003 client direction. Expanded to cover six comparison items with percentage-based weighting. Historical A/B/C scores preserved for traceability.`

---

### SPEC-005 — Update the SPS (TK002.7, Part A)

| Field | Detail |
|:--|:--|
| Requirement Source | SES003/SES004 recycle consultation plus the approved standards-input proposal `proposal_T002-PH000-ST000-AC000_sps-iii-b-rid-realignment-standards-input.md` |
| Target file(s) | `prompt/artifacts/tasks/T002/ssot/sps_T002.md` |
| Required end-state posture | SPS v1.1.0: (1) Section `III.A` is updated so the problem framing and desired outcome reflect the revised P0-P4 direction at high level without embedding proposal-detail mechanics; (2) Section `III.B.1` through `III.B.8` are rewritten using the approved TECOM-centered standards-input proposal as the primary authority surface; (3) current draft RID bodies that are misframed around NMAQ consultation mechanics are rebased in place exactly where the approved proposal directs; (4) the normative RID set under `III.B.2` through `III.B.6` contains the exact TECOM-centered bodies specified in this SPEC, with `T002-CON-004` added as the compatible recycle-cycle constraint for "no orchestration" as a valid final state; and (5) the resulting SPS reflects TECOM operating realities, proper RID category discipline, and clear separation between initiative content and NMAQ internal mechanics. |
| Explicit non-target / do-not-change constraints | Do NOT ignore or narrow the approved standards-input proposal. Do NOT embed full P0-P4 proposal details in the SPS — the SPS records the initiative problem, constraints, and governing considerations, not the full remediation design. Do NOT alter the RACI matrix unless the revised `III.B.1` authority reset directly requires a role-boundary clarification. Do NOT invent new RID categories or speculative RID bodies not supported by the approved proposal or later confirmed recycle decisions. |
| Validation check | (1) Version is `1.1.0`. (2) Section `III.A.1` contains the SES003 reframing paragraph and Section `III.A.2` reflects the TECOM-centered desired-outcome bullets from this SPEC. (3) Section `III.B.1` through `III.B.8` reflect the approved section-by-section reclassification from the standards-input proposal. (4) `T002-ASSUM-001` through `T002-ASSUM-003`, `T002-CON-001` through `T002-CON-004`, `T002-QG-001` through `T002-QG-004`, `T002-DEP-001` through `T002-DEP-004`, and `T002-IF-001` through `T002-IF-002` exist with the exact semantic posture defined in this SPEC. (5) `III.B.8` no longer carries the prior NMAQ-internal IG/INT/NOTE bundle as normative initiative content. (6) Changelog entry exists and explicitly records the `III.B` semantic reset authority. |
| Blocking ambiguity rule | If the SPS update would require departing from the approved standards-input proposal, STOP and escalate. If the approved proposal and the current recycle requirements appear to conflict, resolve in favor of the approved `III.B` standards-input authority and only layer in later recycle decisions where they are clearly compatible and evidence-backed. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/T002/ssot/sps_T002.md`.
2. Open `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000_sps-iii-b-rid-realignment-standards-input.md` and treat it as the approved primary authority surface for `III.B`.
3. Update frontmatter:
   1. Set `version` to `'1.1.0'`.
   2. Set `date` to the execution date of the SPS amendment session.
4. In Section `III.A.1 (The Problem)`, add the following paragraph immediately after the existing two-paragraph problem description and before `#### 2. The Desired Outcome`:

   `SES003 consultation (2026-04-03) reassessed the initial framing. The CEO's binary question (centralized orchestrator vs independent agents) was identified as a false dichotomy that constrains the solution space. The revised assessment identifies an incremental improvement path (P0-P4) that addresses the coordination bottleneck through workflow census, domain-specific review policies, structured report schemas, and skill-level improvements, with orchestration as a validated endpoint rather than an assumed destination. Proposal details remain in the hypothesis brief rather than in the SPS.`

5. Replace the numbered list in Section `III.A.2 (The Desired Outcome)` with the following exact bullets:
   1. `clarifies TECOM's real workflow, handoffs, and coordination bottlenecks before any MVP commitment`
   2. `fits a 4-person operating environment with heterogeneous tools and no heavy ongoing administration`
   3. `supports stepwise adoption by domain or workflow slice rather than requiring whole-workflow replacement before first value is tested`
   4. `improves executive visibility, onboarding clarity, and workflow recall in the first validated slice`
   5. `explicitly allows "no orchestration" as a valid final state if incremental improvements (P0-P3) sufficiently reduce coordination overhead`
6. Keep the closing paragraph under `III.A.2` that defines what "done" means for PH000, unless a small wording adjustment is required to keep it compatible with the revised bullets.
7. Replace Section `III.B.1 (Organization & Responsibilities)` with a lean TECOM-centered role boundary using the same two-table structure already present:
   1. `Role Definitions` table rows:
      - `Client` | `TECOM Decision Owner / Executive Sponsor` | `Approves direction, approves any PH001 progression, owns build decisions` | `Provides workflow facts, reviews advisory outputs, confirms whether follow-on work proceeds` | `Initiative-wide`
      - `TECOM Team` | `Workflow Subject-Matter Contributors` | `No baseline approval authority recorded` | `Supplies operational context, tool usage detail, and current-state workflow facts when requested` | `Discovery support`
      - `LLM_Consultant` | `Technical Advisor` | `Proposes analysis and requirement baselines; no final approval authority` | `Produces SPS, hypothesis, comparative analysis, and advisory guidance` | `Advisory-only in PH000`
   2. `Governance RACI` table rows:
      - `Establish initiative baseline` | `LLM_Consultant` | `Client` | `TECOM Team` | `—`
      - `Provide workflow and tooling facts` | `Client` | `Client` | `TECOM Team` | `LLM_Consultant`
      - `Decide whether PH001 proceeds` | `Client` | `Client` | `TECOM Team` | `LLM_Consultant`
8. Replace Section `III.B.2 (Project Assumptions)` with the following exact assumption set:
   1. Update the `ASSUM Validation Lifecycle Summary` table so it contains these three rows:
      - `T002-ASSUM-001` | `Bottleneck Nature` | `Pending` | `Validate in PH000 discovery by mapping the workflow and determining whether a meaningful share of the CEO's coordination burden can be reduced through better status synthesis, workflow clarity, or agent support rather than requiring personal judgment at every handoff` | `PH000` | `Client + LLM_Consultant` | `Pivot from agent-first framing toward workflow redesign / documentation-first remediation` | `T002-CON-001`
      - `T002-ASSUM-002` | `Pilot Sufficiency` | `Pending` | `Validate through staged P0-P4 discovery by confirming one bounded workflow slice is sufficient to test whether agent-supported coordination creates useful value before wider rollout is considered` | `PH000 / PH001 readiness` | `Client + LLM_Consultant` | `Expand discovery scope before committing to implementation` | `T002-CON-003`
      - `T002-ASSUM-003` | `Tool Extractability` | `Pending` | `Validate by confirming at least one initial business domain can be instrumented across the current tool estate without first replacing the entire stack` | `PH000` | `Client + LLM_Consultant` | `Reframe the initiative toward documentation / reporting improvements before automation expansion` | `T002-CON-002`
   2. Replace the assumption bullets with these exact bodies:
      - `T002-ASSUM-001 (Bottleneck Nature)` — `The initiative assumes that a meaningful share of the CEO's current coordination burden can be reduced through better status synthesis, workflow clarity, or agent support rather than requiring the CEO's personal judgment at every handoff.`
      - `T002-ASSUM-002 (Pilot Sufficiency)` — `The initiative assumes that one bounded workflow slice is sufficient to test whether agent-supported coordination can create useful value before wider rollout is considered.`
      - `T002-ASSUM-003 (Tool Extractability)` — `The initiative assumes that at least one initial business domain can be instrumented across the current tool estate without first replacing the entire stack.`
9. Replace Section `III.B.3 (Project Constraints)` with these exact bullets:
   - `T002-CON-001 (Team Capacity)` — `The initial solution SHALL fit a 4-person operating environment and SHALL NOT depend on a large support function or heavy ongoing administration.`
   - `T002-CON-002 (Tool Heterogeneity)` — `The initiative SHALL account for a workflow spanning roughly 10 tools across VBA, Python, Google Apps Script, and manual steps; it SHALL NOT assume a greenfield single-stack environment.`
   - `T002-CON-003 (Incremental Adoption)` — `The initial approach SHALL support stepwise adoption by domain or workflow slice and SHALL NOT require whole-workflow replacement before first value can be tested.`
   - `T002-CON-004 (No-Orchestration Valid Endpoint)` — `The initiative SHALL treat "no orchestration" as a valid and successful final state. If P0-P3 improvements sufficiently reduce the CEO's coordination overhead without requiring an orchestration layer, the initiative is complete. Orchestration SHALL NOT be pursued for its own sake.`
10. Replace Section `III.B.4 (Quality Goals)` with these exact bullets:
    - `T002-QG-001 (Coordination Relief)` — `The initiative SHOULD materially reduce the CEO's manual status-checking and handoff overhead in the first validated slice.`
    - `T002-QG-002 (Onboarding Clarity)` — `The initiative SHOULD make the workflow easier to summarize, teach, and hand over when staff changes occur.`
    - `T002-QG-003 (Executive Reporting)` — `The initiative SHOULD produce a concise executive summary surface that gives the CEO usable visibility across delegated work domains.`
    - `T002-QG-004 (Workflow Recall)` — `The initiative SHOULD reduce dependence on remembering how infrequently used tools or steps operate by making the workflow more explicit and repeatable.`
11. Replace Section `III.B.5 (Dependencies)` with these exact bullets:
    - `T002-DEP-001 (Workflow Walkthrough)` — `Further scoping depends on a mapped walkthrough of TECOM's current end-to-end workflow, handoffs, and review points.`
    - `T002-DEP-002 (Tool Inventory)` — `Further scoping depends on a verified inventory of the active tools, scripts, owners, and integration points used in the current workflow.`
    - `T002-DEP-003 (Data Access)` — `Further scoping depends on clarifying what data access exists for candidate domains such as order tracking, email reporting, and creative operations.`
    - `T002-DEP-004 (Pilot Selection)` — `Further scoping depends on confirming which domain should serve as the first validation slice and how success will be judged.`
12. Replace Section `III.B.6 (Interfaces)` with these exact bullets:
    - `T002-IF-001 (Executive Summary)` — `The CEO-facing interface SHALL provide a consolidated view of key workflow status rather than forcing manual synthesis from many separate reports.`
    - `T002-IF-002 (Status Blocks)` — `Domain-level agents or automations SHALL expose bounded, comparable status outputs that can be consumed consistently by a higher-level reporting surface.`
13. Leave Section `III.B.7 (Project Standards)` minimal. Keep the existing empty standards table and the statement that no initiative-local T002 standard is registered yet unless a formatting-only cleanup is required.
14. Replace Section `III.B.8 (Project Guidances & Notes)` with a minimal non-normative note block only:
    - Remove `T002-IG-001`, `T002-INT-001`, `T002-NOTE-001`, and `T002-NOTE-002`.
    - Add a short note paragraph: `This section is intentionally minimal after the III.B reset. NMAQ internal consultation mechanics, gate posture, and SSOT hygiene belong in plan, proposal, and notes artifacts rather than in the TECOM initiative requirement baseline.`
15. Resolve RID-body conflicts explicitly:
    1. Where the current SPS draft body conflicts with the approved standards-input proposal, rewrite the SPS body in place to match the approved proposal and the exact bodies listed above.
    2. Preserve RID identifiers in place when the approved proposal authorizes rebasing rather than minting a new clean sequence.
    3. Keep still-deferred speculative items out of the normative RID set, including Python-first standardization, order tracking as a formal first slice, and any human-review interface requirement not yet evidenced strongly enough for SPS encoding.
16. Add a changelog entry:
   - Version: `v1.1.0`
   - Date: execution date of the SPS amendment session
   - Type: `Amendment`
   - Summary: `SES004 recycle alignment: rewrote SPS Section III.B using the approved TECOM-centered standards-input proposal as the primary authority surface; rebased draft RID bodies in place where authorized; retained the high-level P0-P4 problem-direction note in Section III.A; and added CON-004 (no-orchestration valid endpoint) as a compatible recycle-cycle constraint.`

---

### SPEC-006 — Update the Roadmap (TK002.7, Part B)

| Field | Detail |
|:--|:--|
| Requirement Source | SES003 consultation: revised PH000 deliverables and new open questions require roadmap alignment |
| Target file(s) | `prompt/artifacts/tasks/T002/ssot/roadmap_T002.md` |
| Required end-state posture | Roadmap v1.2.0: (1) Current Delivery Snapshot reflects the active GATE-001 RECYCLE loop, including the registration of `TK002.8` as the final same-gate prerequisite before re-disposition; (2) Open Questions Register includes the new execution-substrate, skill-governance, and agentic-CLI-feasibility questions; (3) Links Register includes the remediation-cycle artifacts that are not already present, without duplicating existing rows; and (4) the roadmap remains a thin-spine initiative surface rather than an execution-log surface. |
| Explicit non-target / do-not-change constraints | Do NOT alter the Phase Register (Section II) — PH000 and PH001 definitions remain unchanged. Do NOT add phase-level detail beyond the thin-spine rule. Do NOT embed proposal details — reference the hypothesis brief and comparative assessment. Do NOT duplicate Links Register rows that already exist in the current roadmap. |
| Validation check | (1) Version is `1.2.0`. (2) Current Delivery Snapshot reflects the RECYCLE same-gate loop and the pending `TK002.8` external review prerequisite. (3) Open Questions Register contains `OQ-T002-004` through `OQ-T002-006`. (4) Links Register includes the comparative assessment, research brief, and SES003/SES004 session-note references without duplicating pre-existing rows. (5) Changelog entry exists. |
| Blocking ambiguity rule | If the roadmap update would require adding new phases or restructuring the phase register, STOP and escalate. |
| Status | `open` |

#### Implementation Detail

1. Open `prompt/artifacts/tasks/T002/ssot/roadmap_T002.md`.
2. Update frontmatter:
   1. Set `version` to `'1.2.0'`.
   2. Set `date` to the execution date of the roadmap amendment session.
3. Update Section III (Current Delivery Snapshot):
   1. Replace the first row ("PH000 Advisory Baseline"):
      - Current State: `Activity plan amended to v3.0.0 with GATE-001 reset into a same-gate RECYCLE loop. Remediation tasks TK002.4 through TK002.7 are registered ahead of recycled external review task TK002.8. Hypothesis brief revision, comparative assessment creation, research brief production, and SPS/roadmap updates are the active remediation surfaces.`
      - Next Milestone: `Complete TK002.5 through TK002.7, commission TK002.8 recycled external review, then refresh the GATE-001 package for re-disposition.`
      - Canonical Link: `prompt/artifacts/tasks/T002/ssot/sps_T002.md`
   2. Replace the second row ("Discovery Gaps"):
      - Current State: `Original gaps (GAP-001 through GAP-005) plus new gaps from SES003: GAP-006 (execution substrate undefined), GAP-007 (skill governance undefined). New risks: RISK-001 (overengineering perception), RISK-002 (token cost expansion), RISK-003 (approval friction in unattended execution).`
      - Next Milestone: `Use T002-RES-001 brief/report outputs and later PH000 discovery evidence to ground technical feasibility and workflow-specific gap validation before any PH001 commitment.`
      - Canonical Link: `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md`
   3. Keep the third row ("PH001 Readiness") unchanged.
4. Update Section V (Open Questions Register). Add the following new rows:
   1. `OQ-T002-004` | Execution Substrates | For each of TECOM's 10 tools, which execution model applies: interactive CLI, headless/SDK, or external scheduler? | Client | Proposed | execution date of the roadmap amendment session | —
   2. `OQ-T002-005` | Skill Governance | Who owns each skill in TECOM's system? How are prompt/skill changes tested and rolled back? | Client | Proposed | execution date of the roadmap amendment session | —
   3. `OQ-T002-006` | Agentic CLI Feasibility | Do Claude Code and/or Codex CLI provide sufficient automation primitives for P1 (review policies) and P2 (report schemas) without custom infrastructure? | LLM_Consultant | Proposed | execution date of the roadmap amendment session | — (Pending T002-RES-001)
5. Update Section IV (Links Register). Add only the missing rows below; do NOT duplicate any row already present in the roadmap:
   1. Analysis | Comparative Assessment | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_comparative-assessment.md`
   2. Brief | Research Brief (T002-RES-001) | `prompt/artifacts/tasks/T002/research/T002-RES-001/brief_T002-RES-001_agentic-cli-orchestration-research.md`
   3. Notes | SES003 Session Notes | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/snotes/snotes_T002-PH000-ST000-AC000-SES003.md`
   4. Notes | SES004 Session Notes | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/snotes/snotes_T002-PH000-ST000-AC000-SES004.md`
6. Add changelog entry:
   - Version: `v1.2.0`
   - Date: execution date of the roadmap amendment session
   - Type: `Amendment`
   - Summary: `SES004 recycle alignment: updated the delivery snapshot to reflect the same-gate RECYCLE loop and pending TK002.8 external review, added OQ-T002-004 through OQ-T002-006, and expanded the links register with the remediation-cycle artifacts that were not already indexed.`

## IV. IMPLEMENTATION SEQUENCE

| Order | SPEC | Task | Depends On | Notes |
|:--|:--|:--|:--|:--|
| 1 | SPEC-001 | Governance reset + plan amendment (TK002.4, Part A) | — | Establishes same-gate RECYCLE ordering and registers the future recycled external review task |
| 2 | SPEC-002 | Research brief (TK002.4, Part B) | SPEC-001 | New file; no dependency on other artifacts |
| 3 | SPEC-003 | Hypothesis brief revision (TK002.5) | SPEC-001, SPEC-002 | References research brief path; major revision of existing artifact |
| 4 | SPEC-004 | Comparative assessment (TK002.6) | SPEC-003 | References hypothesis brief v2.0.0 for proposal definitions |
| 5a | SPEC-005 | SPS update (TK002.7, Part A) | SPEC-003 | Uses the approved `III.B` standards-input proposal as primary authority; can run in parallel with SPEC-006 |
| 5b | SPEC-006 | Roadmap update (TK002.7, Part B) | SPEC-003, SPEC-004 | References comparative assessment path |
| 6 | Plan-registered task | Recycled external review (TK002.8) | SPEC-005, SPEC-006 | Registered by SPEC-001 only; this brief defines the plan-level registration contract, not the execution procedure for TK002.8 |

Note: SPEC-005 and SPEC-006 can be executed in parallel (5a/5b) since they target different files with no cross-dependencies beyond their shared dependency on SPEC-003. This artifact is the next-session execution contract for SPEC-001 through SPEC-006. `TK002.8` remains intentionally limited to in-plan task registration and scope-setting inside SPEC-001.

## V. REFERENCES

| Document | Path |
|:--|:--|
| Governing Plan | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md` |
| Hypothesis Brief (current) | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md` |
| SPS | `prompt/artifacts/tasks/T002/ssot/sps_T002.md` |
| Roadmap | `prompt/artifacts/tasks/T002/ssot/roadmap_T002.md` |
| Approved Standards-Input Proposal | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000_sps-iii-b-rid-realignment-standards-input.md` |
| Research Brief Template | `prompt/templates/researcher/template_research_brief.md` |
| Analysis Template | `prompt/templates/consultant/workspace/template_workspace_analysis.md` |
| Analysis Guideline | `prompt/templates/consultant/workspace/guideline_workspace_analysis.md` |
| Implementation Guideline | `prompt/templates/consultant/workspace/guideline_workspace_implementation.md` |
| Gate-001 Proposal | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/proposal/proposal_T002-PH000-ST000-AC000-GATE-001_gate-disposition.md` |
| Consultant Assessment | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_gate-001-external-review-and-downstream-readiness-assessment.md` |
| Existing Implementation Brief | `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/implementation/implementation_T002-PH000-ST000-AC000_gate-001-package-refresh-brief.md` |

## VI. CHANGELOG

| Version | Date | Type | Summary |
|:--|:--|:--|:--|
| v1.0.0 | 2026-04-03 | Initial | Created SES003 GATE-001 RECYCLE remediation implementation specification. Six SPECs covering: plan amendment, research brief production, hypothesis brief major revision, comparative assessment creation, SPS update, and roadmap update. Commissioned by LLM_Consultant for LLM_Assistant execution. |
| v1.1.0 | 2026-04-04 | Amendment | Narrowed this artifact to an authoring-only planning surface for the next session. Rewrote SPEC-001 as the governance reset authority surface, including registration of the recycled external review task (`TK002.8`) inside the same-gate RECYCLE loop without adding a new standalone SPEC. Updated SPEC-005 to treat the approved `proposal_T002-PH000-ST000-AC000_sps-iii-b-rid-realignment-standards-input.md` as the primary authority for the SPS `III.B` rewrite and resolved conflicts between that approved authority and the earlier narrower SPS-update wording. |
| v1.2.0 | 2026-04-04 | Amendment | Re-promoted this artifact to a next-session execution contract for assistant sub-agents. Added the missing triggering `proposal_reference` backlink, removed planning-only framing, normalized execution-date instructions across the SPEC set, rewrote SPEC-005 into an exact SPS section-by-section replacement contract using the approved standards-input proposal, and corrected SPEC-006 so roadmap updates reflect TK002.8, avoid duplicate links, and index SES003/SES004 rather than stale SES002 references. |
