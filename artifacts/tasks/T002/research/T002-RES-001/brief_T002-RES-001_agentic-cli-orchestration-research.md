---
artifact_type: 'BRIEF'
initiative_id: 'T002'
epic_id: '—'
research_id: 'T002-RES-001'
version: '1.0.0'
iteration: '1'
date: '2026-04-04'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: Agentic CLI Orchestration Research for TECOM (T002-RES-001)

## I. EXECUTIVE SUMMARY

**Context**: The T002 TECOM advisory initiative needs a grounded view of what agentic CLI tools can actually do before recommending any workflow architecture. SES003 consultation found that the earlier hypothesis brief was too abstract: it treated the problem as an architecture selection question without first verifying the available automation primitives. This brief commissions the research needed to close that gap.

**Objective**: Map current agentic CLI capabilities relevant to TECOM's workflow automation needs, identify technical constraints and cost implications, and provide evidence that grounds the revised P0-P4 proposal framework.

**Target Deliverable**: A research report consumed by the LLM_Consultant to inform the hypothesis brief revision, comparative assessment, and eventual advisory note. The report will be synthesized into an analysis artifact (`research_synthesis` subtype) before feeding the advisory.

## II. RESEARCH SCOPE & TOPICS

### Part A: Current Agentic CLI Capabilities

#### Topic 1: Claude Code Automation Primitives (High Priority)
**Objective**: What automation capabilities does Claude Code provide that are relevant to workflow orchestration?
**Context**: TECOM uses agentic CLI tools. The advisory must know what building blocks exist natively.
**Specific Questions**:
* What are Claude Code hooks and what events can they trigger on? Can hooks be used for post-workflow reporting?
* What are Claude Code subagents and how do they relate to skill-activated session contexts?
* What does Claude Code SDK/headless mode enable for unattended execution?
* What are Claude Code scheduled triggers and how do they work for recurring tasks?
* What are Claude Code GitHub Actions integrations and can they serve as a scheduling/orchestration substrate?
* What are MCP servers and how do they bridge between tools?
**Deliverable**: Capability matrix (feature, description, TECOM relevance, constraints)

#### Topic 2: Codex CLI Automation Primitives (High Priority)
**Objective**: What automation capabilities does Codex CLI provide that are relevant to workflow orchestration?
**Context**: TECOM may use Codex CLI (or Anti-Gravity). The advisory must cover both major agentic CLI ecosystems.
**Specific Questions**:
* What are Codex CLI skills and how do they define end-to-end workflows?
* How does `spawn_agent` work for sub-agent orchestration within Codex?
* What scheduling and automation capabilities does Codex provide?
* What are the differences between Claude Code and Codex CLI for multi-agent workflows?
**Deliverable**: Capability matrix (parallel structure to Topic 1)

#### Topic 3: Execution Substrate Taxonomy (High Priority)
**Objective**: What execution models are available and how do they map to different workflow types?
**Context**: GAP-006 identified that TECOM's workflows have not been classified by execution substrate. This topic provides the taxonomy needed for that classification.
**Specific Questions**:
* What types of workflows require interactive CLI sessions vs headless/SDK execution vs external scheduler (cron, GitHub Actions)?
* What are the permission/credential constraints for each execution model?
* What happens when an interactive-only workflow is run in an unattended context?
* How do approval checkpoints work in headless mode?
**Deliverable**: Execution substrate taxonomy table (model, description, suitable workflow types, constraints, TECOM applicability)

### Part B: Cost, Constraints, and Risk Factors

#### Topic 4: Multi-Agent Cost and Token Implications (Medium Priority)
**Objective**: What are the cost and context-window implications of running multiple agents for a small company?
**Context**: RISK-002 identified token/cost expansion as a concern. This topic provides the evidence base.
**Specific Questions**:
* What is the typical token cost per agent session for a workflow-length task?
* How does multi-agent review (specialist + reviewer + aggregator) multiply costs?
* What are practical cost management strategies (model selection, context trimming, caching)?
* What monthly budget range should a 4-person company expect for a multi-agent workflow system?
**Deliverable**: Cost model table with scenarios (single agent, dual agent with review, full orchestration)

#### Topic 5: Industry Orchestrator Patterns Grounded in Agentic CLI (Medium Priority)
**Objective**: What does "orchestration" actually mean in the agentic CLI context, as opposed to traditional distributed systems?
**Context**: The original hypothesis brief referenced Microsoft and Akka patterns. The client assessed these are too abstract. This topic grounds orchestration concepts in what CLI tools actually provide.
**Specific Questions**:
* How do the concepts of "orchestrator," "supervisor," and "coordinator" map to agentic CLI primitives?
* What patterns exist for agent-to-agent communication in CLI-based systems (shared filesystem, structured outputs, MCP)?
* What are documented failure modes and mitigation patterns for multi-agent CLI workflows?
* What open-source frameworks or community patterns exist for agentic CLI orchestration (spec-kit, superpowers, agent-os, get-shit-done)?
**Deliverable**: Pattern mapping table (abstract pattern, CLI implementation, documented examples, TECOM relevance)

### Part C: TECOM-Specific Applicability (Deferred to Post-Discovery)

#### Topic 6: TECOM Workflow-to-Substrate Mapping (Deferred)
**Objective**: Map each of TECOM's 10 tools and workflows to the appropriate execution substrate.
**Context**: This requires visibility into TECOM's actual skill files and tool inventory, which is not yet available. Deferred until the PH000 discovery session (pre-April 10).
**Specific Questions**: Deferred.
**Deliverable**: Deferred. Placeholder for post-discovery enrichment.

---

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
* **Boundary**: External web research + publicly available documentation only. No access to TECOM internal systems.
* **Timebox**: Single research session.

### B. Assumptions
* **Claude Code documentation at `docs.anthropic.com`** is the authoritative source for Claude Code capabilities.
* **OpenAI documentation** is the authoritative source for Codex CLI capabilities.
* **TECOM's actual tool inventory and skill files are not available**; Topic 6 is explicitly deferred.

### C. Methodology "Hierarchy of Truth"
Define how to resolve conflicts between sources:
1. **Official documentation** (`docs.anthropic.com`, OpenAI docs) - Highest authority
2. **Open-source project documentation** (spec-kit, superpowers, agent-os) - Secondary authority
3. **Community/blog content** - Tertiary authority (corroborate only)

---

## IV. CROSS-TOPIC INTEGRATION
*Force the researcher to synthesize, not just list facts.*
* **Integration Question 1**: How do Topic 1 (Claude Code) and Topic 2 (Codex CLI) capabilities compare for TECOM's likely workflow types? Are they complementary or competing?
* **Integration Question 2**: How does Topic 3 (execution substrate taxonomy) constrain the applicability of Topics 4-5 (cost and orchestration patterns)?
* **Gap Analysis**: What capabilities are missing in the current agentic CLI ecosystem that would be needed for full orchestration? What workarounds exist?

---

## V. INPUT PACKET (CONTEXT MAP)
*Mandatory section to reduce context-loading time. Point to EXACT files.*

### A. Core Governance
* **SSOT**: `prompt/artifacts/tasks/T002/ssot/sps_T002.md`
* **Plan**: `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/plan_T002-PH000-ST000-AC000.md`

### B. Reference Artifacts
* `prompt/artifacts/tasks/T002/workspace/PH000/ST000/AC000/analysis/analysis_T002-PH000-ST000-AC000_hypothesis-brief.md`
* `prompt/artifacts/tasks/T002/raw_T002-PH000.txt`
* `prompt/artifacts/tasks/T103/workspace/PH000/ST000/AC001/implementation/implementation_T103-PH000-ST000-AC001_orchestration-execution-patterns.md`

### C. Anti-Patterns / Exclusions
* **IGNORE**: Do not reference TECOM internal systems or skill files (not available).

---

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use the standard template located at:
> `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions for this Brief**:
1. **Section I (Exec Summary)**: Provide a clear executive summary distinguishing what is known from current documentation vs what requires TECOM discovery.
2. **Section III (Topic Findings)**: Each topic finding must include a TECOM Relevance column or subsection.
3. **Completeness**: Do NOT delete empty sections. If a topic has no implications, explicitly state "None".

---

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

The research report MUST include an "Issues & Risks" section that implements `T102-STD-007 (Issues & Risks Index)` exactly.

**Issues**
None identified at brief stage.

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**
<!-- GUIDANCE:
Status = `OPEN, MONITORED, MITIGATED, ACCEPTED, CLOSED`,
priority = `Low, Medium, High`
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `T002-RES-001-RISK-001` | Documentation currency | Agentic CLI tools evolve rapidly; findings may be outdated within months. | LLM_Consultant | `OPEN` | `Medium` | 2026-04-04 | Date-stamp all findings; note documentation version/date. | — |
| `T002-RES-001-RISK-002` | Ecosystem divergence | Claude Code and Codex CLI may have fundamentally different orchestration models, making unified recommendation difficult. | LLM_Consultant | `OPEN` | `Low` | 2026-04-04 | Present capabilities side-by-side; let the advisory note recommend based on TECOM's primary tool. | — |

**ID Rules**
* IDs MUST use the scoped, sequential format: `<SCOPE_ID>-ISSUE-###` and `<SCOPE_ID>-RISK-###`.
* IDs MUST remain stable once created (no reuse, no renumbering).

---

## VIII. CRITICAL DEPENDENCIES (E-RID MAPPING)
*Map research findings to the specific governance artifacts they inform.*

* `T002-PH000-ST000-AC000-TK002.5`: Topic 1-5 findings will inform the hypothesis brief revision (P0-P4 grounding).
* `T002-PH000-ST000-AC000-TK002.6`: Topic 3-5 findings will provide evaluation criteria for the comparative assessment.
* `T002-PH000-ST000-AC000-TK003`: Full research synthesis will feed the advisory note English SSOT.

---

## IX. SUCCESS CRITERIA
* Topics 1-5 each have a populated deliverable table or matrix.
* Topic 6 is explicitly marked as deferred with rationale.
* Cross-topic integration section addresses both integration questions.
* The report provides sufficient evidence to distinguish "what is buildable today" from "what requires custom development" for each proposal in the P0-P4 framework.
* Cost model provides actionable budget guidance for a 4-person company.
