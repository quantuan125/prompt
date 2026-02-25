---
artifact_type: 'BRIEF'
initiative_id: 'P'
research_id: 'P-RES-002'
version: '1.0.0'
iteration: '1'
date: '2026-02-25'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH BRIEF: P-RES-002 — Agentic Status Systems Research

## I. EXECUTIVE SUMMARY

**Context**: P-RES-001 benchmarks traditional PM frameworks (PMI/PMBOK, SAFe, PRINCE2, Azure DevOps, Jira) for P-STD-002 CLAUSE authoring. However, the program operates in an agentic CLI + repo-native ecosystem where status is also modeled by modern agent tools and CI/CD orchestration layers. A separate research artifact is needed to evaluate these emerging patterns and produce complementary evidence for P-STD-002.

**Objective**: Produce a decision-ready research report benchmarking modern agentic CLI and orchestration-layer status systems across 4 domains (agentic task lifecycle, orchestration status, repo-native surfacing, integration bridging), with scored recommendations using a weighted evaluation rubric.

**Target Deliverable**: Research report consumed by `P-PH000-ST001-AC003` (Author P-STD-002). Consumer: LLM_Consultant. Complements P-RES-001 findings.

## II. RESEARCH SCOPE & TOPICS

### Part A: Agentic CLI Task/Run Lifecycle (maps to P-STD-002A, P-STD-002B)

#### Topic 1: Agentic CLI Status State Models (Critical)
- **Objective**: Benchmark how modern agent-based CLI tools model task/run lifecycle status.
- **Context**: Traditional PM status enums (P-RES-001 scope) may not capture agentic-specific states like "tool-calling", "waiting-for-approval", or "session-suspended". The program needs to understand whether P-STD-002's status vocabulary should accommodate these.
- **Specific Questions**:
  - What status/lifecycle states do Claude Code, Codex CLI, and Gemini CLI use for task and run tracking?
  - How do these tools distinguish between session state (the agent's overall session) and task state (individual work items within a session)?
  - What terminal states exist and what conditions trigger them (success, failure, cancellation, timeout)?
  - How do these models compare to each other and to traditional PM status enums (P-RES-001 findings)?
- **Deliverable**: Comparative matrix of status state models across the three CLIs. Scored comparison per evaluation rubric.

#### Topic 2: Hierarchical/Nested Task Status (High)
- **Objective**: Evaluate how agentic tools represent and aggregate status for nested/hierarchical execution.
- **Context**: Agentic CLIs execute multi-step tasks with sub-agent delegation, tool calls, and parallel operations. How child-level status propagates to parent-level status is a pattern P-STD-002 may need to account for.
- **Specific Questions**:
  - How do agentic CLIs represent nested execution (sub-agents, tool calls within runs, multi-step task decomposition)?
  - What aggregation rules exist for computing parent status from child statuses (all-pass, any-fail, partial-success)?
  - How is execution depth/nesting reflected in status reporting?
- **Deliverable**: Recommended patterns for hierarchical status aggregation with applicability assessment for P-STD-002.

### Part B: Orchestration & CI/CD Status Models (maps to P-STD-002A, P-STD-002C)

#### Topic 3: GitHub Actions vs GitLab CI/CD Workflow Status Architecture (Critical)
- **Objective**: Benchmark the status architecture for two notable CI/CD orchestration platforms to ground P-STD-002 orchestration patterns in recognized, documented practice.
- **Context**: The program is repo-native and GitHub-first, so GitHub Actions is the baseline reference. A second notable platform comparator is required to avoid overfitting the standard to a single vendor model while still keeping scope tight for P-RES-002.
- **Platforms in scope (locked)**:
  - GitHub Actions
  - GitLab CI/CD
- **Specific Questions**:
  - What is the complete status enum set at each hierarchy level (pipeline/workflow, job, step) for each platform?
  - What terminal conclusion/result types exist and how do they differ from in-progress status reporting?
  - How does status propagate upward through the execution graph (job failure → pipeline/workflow failure rules)?
  - How are conditional and matrix-style jobs handled in status computation?
- **Deliverable**: Comparative status architecture diagram(s) + propagation rules. Scored comparison per evaluation rubric (Option A: GitHub Actions; Option B: GitLab CI/CD).

#### Topic 4: Multi-Agent/Pipeline Orchestration Patterns (High)
- **Objective**: Evaluate how orchestration frameworks compute aggregate status across parallel and sequential execution.
- **Context**: Programs may orchestrate multiple agents or pipeline stages. Understanding how aggregate status is computed (majority-pass, first-fail, weighted) informs P-STD-002's dependency and health models. Primary evidence SHOULD be grounded in GitHub Actions and GitLab CI/CD documentation; other orchestration engines MAY be referenced only to support a general taxonomy when primary/official sources exist.
- **Specific Questions**:
  - What aggregate status computation patterns exist in CI/CD and orchestration platforms (GitHub Actions, DAG-based engines)?
  - How is partial success represented when some parallel jobs succeed and others fail?
  - What failure propagation models exist (fail-fast, continue-on-error, allow-failure)?
- **Deliverable**: Taxonomy of aggregate status computation patterns with trade-off analysis.

### Part C: Repo-Native Status Surfacing (maps to P-STD-002D, P-STD-002E)

#### Topic 5: GitHub Checks API vs Commit Status API (Critical)
- **Objective**: Benchmark GitHub’s two repo-native status surfacing mechanisms (modern Checks API vs legacy Commit Status API), since they directly constrain evidence linkage, required checks, and PR-level status aggregation in GitHub-first workflows.
- **Context**: Agentic tools and CI/CD systems report status back to the repo layer via Checks API, commit statuses, and PR status integrations. Understanding these mechanisms informs P-STD-002's update protocol and artifact spec.
- **Specific Questions**:
  - What is the GitHub Checks API status model (check suites, check runs, statuses, conclusions)?
  - How does the legacy commit status API relate to the Checks API?
  - How do PR status indicators (mergeable state, required checks, review states) aggregate from underlying checks?
  - What metadata is available per check (output, annotations, actions)?
- **Deliverable**: Complete model of both APIs + integration patterns and trade-offs. Scored comparison per evaluation rubric (Option A: Checks API; Option B: Commit Status API).

#### Topic 6: Repo-Native Audit Trail Patterns (High)
- **Objective**: Evaluate how agentic tools write status and evidence into version-controlled artifacts.
- **Context**: The program's Markdown-primary, repo-native ecosystem needs to understand what audit trail patterns modern tools produce — commit-linked evidence, status files, changelogs, PR-embedded summaries.
- **Specific Questions**:
  - How do agentic CLIs record their operations in version-controlled repositories (commit messages, generated files, PR descriptions)?
  - What structured status data do these tools produce that could serve as evidence for P-STD-002 status transitions?
  - What patterns exist for linking agentic run outputs to governance artifacts (e.g., commit SHA → status update evidence)?
- **Deliverable**: Taxonomy of repo-native audit trail patterns with applicability assessment.

### Part D: Integration & Bridging Patterns (cross-cutting — Exploratory/Survey)

#### Topic 7: Bridging Agentic Status to Program Governance (Survey)
- **Objective**: Survey emerging patterns for connecting tool-level agentic/CI status to program-level governance status systems.
- **Context**: Few established patterns exist for this bridging. This topic is exploratory/informational — producing clear recommendations but not normative requirements for P-STD-002 v1.
- **Specific Questions**:
  - What patterns exist (if any) for aggregating heterogeneous tool-level statuses into a unified program-level status view?
  - How do organizations reconcile agentic/automated status updates with human-governed status governance?
  - What is the minimum viable bridging pattern for a program with 2-5 initiatives using agentic CLI tools?
- **Deliverable**: Survey of bridging patterns with clear recommendations. **Informational only** — not for P-STD-002 v1 CLAUSE authoring (analogous to Topic 9 in P-RES-001).

## III. CONSTRAINTS, ASSUMPTIONS & METHODOLOGY

### A. Constraints
- **Boundary**: Research is recommendations-only. No P-STD-002 CLAUSE text drafting. No status artifact implementation.
- **Scope**: Program-level status governance patterns as evidenced by modern agentic/CI tools. NOT tool-specific implementation guides.
- **Output**: Research report per `prompt/templates/researcher/template_research_report.md`.
- **Timebox**: Target 1–2 working days of research execution time, prioritizing Topics 1, 3, and 5.

### B. Assumptions
- **Complementary Evidence Base**: P-RES-002 complements (does not duplicate) P-RES-001. Traditional PM framework benchmarking is out of scope — cross-references to P-RES-001 findings are permitted where relevant.
- **Emerging Domain**: Agentic CLI tooling is an emerging field with less established literature than traditional PM. Evidence quality may rely on official tool documentation and API specifications rather than published academic/industry standards. This is expected and acceptable.

### C. Methodology "Hierarchy of Truth"
1. **Official Tool Documentation & API Specifications** (GitHub Docs, Anthropic/Claude Code docs, OpenAI/Codex CLI docs, Google/Gemini CLI docs) — Primary Authority
2. **Program SSOT Files** (`sps_P-PROGRAM.md` constraints, accepted standards) — Governance Context
3. **P-RES-001 Findings** (when available) — Cross-Reference Complement
4. **Community Documentation / Observed Tool Behavior** — Lowest Authority (supplementary; use only when official sources are missing and clearly label as such)

### D. Evaluation Rubric (adapted from P-RES-001)

| Dimension | Weight (1–5) | Description |
|:--|:--|:--|
| Program Fit | 5 | Aligns with the P governance model: multi-initiative, multi-role, Markdown-primary ecosystem |
| Industry Alignment | 4 | Established practice in recognized agentic/CI platforms or documented in official tool specifications |
| Agentic Operability | 5 | Machine-readable, deterministic for LLM agentic role workflows; supports automated read/write update sequences |
| Adoption Overhead | 3 | Migration cost and process burden to implement within the current artifact ecosystem |
| Extensibility | 2 | Supports future growth without structural rework |

Per-option scores MUST use a 1–5 scale. Weighted totals MUST be computed.

## IV. CROSS-TOPIC INTEGRATION

- **Integration 1**: How do agentic CLI status models (Topic 1) compare to GitHub Actions status architecture (Topic 3)? Are there common patterns that P-STD-002 should unify?
- **Integration 2**: How do hierarchical status patterns (Topic 2) interact with aggregate orchestration patterns (Topic 4)? Is there a single aggregation model that covers both?
- **Integration 3**: How does repo-native status surfacing (Topic 5) enable or constrain the audit trail patterns (Topic 6)? What is the minimum Checks API integration needed for P-STD-002 evidence linkage?
- **Gap Analysis**: What status patterns exist in agentic/CI tools that are NOT covered by P-RES-001's traditional PM benchmarking? Identify gaps per P-STD-002 CLAUSE domain.

## V. INPUT PACKET (CONTEXT MAP)

### A. Core Governance
- SSOT: `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
- Plan (research stream): `prompt/artifacts/tasks/P/workspace/PH000/ST004/plan_P-PH000-ST004.md`
- Plan (consumer activity): `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md`
- Authoring authority: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`

### B. Cross-Reference Research
- `prompt/artifacts/tasks/P/research/P-RES-001/brief_P-RES-001_status-standard-research.md` — P-RES-001 brief (scope boundary reference)
- `prompt/artifacts/tasks/P/research/P-RES-001/report_P-RES-001_status-standard-research.md` — P-RES-001 report (cross-reference findings when available)

### C. Consultation Evidence
- `prompt/artifacts/tasks/P/workspace/PH000/ST004/AC001/snotes/snotes_P-PH000-ST004-AC001-SES001.md` — Origin of P-RES-002 scope request (ACT002, OQ001, OQ002)

### D. Standards & Templates
- `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md` — Research commissioning standard
- `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-007_issues-risks-index.md` — Issues & Risks register standard
- `prompt/templates/researcher/template_research_report.md` — Report template

### E. Anti-Patterns / Exclusions
- **IGNORE**: P-RES-001 report findings as normative input — they are cross-reference only
- **IGNORE**: Traditional PM framework benchmarking — that is P-RES-001's domain

## VI. DELIVERABLE FORMAT REQUIREMENTS

The research report MUST use: `prompt/templates/researcher/template_research_report.md`

**Specific Mapping Instructions**:
1. **Section I (Exec Summary)**: Must include a synthesis verdict on whether P-STD-002 needs to accommodate agentic-specific status patterns beyond traditional PM models. Must list top 3 key findings.
2. **Section III (Topic Findings)**: Each topic MUST include Evidence & Forensics (with tool documentation citations), Analysis, and Governance Implication (P-STD-002 CLAUSE domain impact). Topics 1, 3, 5 MUST include scored comparison tables using the evaluation rubric.
3. **Section V (Artifact Updates)**: Must map findings to P-STD-002 substandard domains (P-STD-002A through P-STD-002E) as integration recommendations. Topic 7 items MUST be clearly labeled as **non-normative / vNext candidates** (informational only; not for P-STD-002 v1 clause authoring).
4. **Completeness**: Do NOT delete empty sections. If no implications, explicitly state "None".

## VII. ISSUES & RISKS REGISTER (T102-STD-007)

**Issues**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**Risks**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

**ID Rules**
*   IDs MUST use the scoped, sequential format: `P-RES-002-ISSUE-###` and `P-RES-002-RISK-###`.
*   IDs MUST remain stable once created (no reuse, no renumbering).

## VIII. CRITICAL DEPENDENCIES (E-RID MAPPING)

- **P-STD-002A** (Status Vocabulary): Topics 1-2 findings complement P-RES-001 Topics 1-2.
- **P-STD-002B** (Health Assessment): Topic 2 findings (hierarchical aggregation) complement P-RES-001 Topics 3-4.
- **P-STD-002C** (Dependency Visibility): Topics 3-4 findings (orchestration status/DAG patterns) complement P-RES-001 Topics 5-6.
- **P-STD-002D** (Update Protocol): Topics 5-6 findings (Checks API, audit trails) complement P-RES-001 Topics 7-9.
- **P-STD-002E** (Status Artifact): Topic 6 findings (repo-native patterns) complement P-RES-001 Topics 10-11.

## IX. SUCCESS CRITERIA

- All 7 topics addressed with findings supported by official tool documentation or API specification citations.
- Evaluation rubric applied consistently across comparative topics (Topics 1, 3, 5) with scored comparison tables and weighted totals.
- Topic 3 comparator set is constrained to exactly two platforms: GitHub Actions and GitLab CI/CD.
- Integration recommendations map each finding to at least one P-STD-002 CLAUSE domain.
- Gap analysis identifies patterns NOT covered by P-RES-001.
- No P-STD-002 CLAUSE text drafted (recommendations-only boundary respected).
- Topic 7 (Survey) clearly marked as informational/exploratory.
- Issues and risks registered per T102-STD-007 schema.
