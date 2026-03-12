---
artifact_type: 'REPORT'
initiative_id: 'P'
research_id: 'P-RES-002'
version: '1.0.0'
iteration: '2'
date: '2026-02-25'
status: 'draft'
author: 'LLM_Researcher'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: P-RES-002 — Agentic Status Systems Research

## I. EXECUTIVE SUMMARY

**Context**: `P-RES-001` establishes traditional PM status governance evidence for `P-STD-002` authoring. This research (`P-RES-002`) benchmarks *agentic CLI* and *orchestration-layer* status models that are materially present in the program’s repo-native operating environment (agent CLIs + CI/CD + GitHub repo status surfaces).

**Verdict**: **GO** — `P-STD-002 v1` SHOULD explicitly accommodate agentic/CI status patterns **without expanding the canonical program status enum**. The recommended approach is to keep the 7-state program status vocabulary intact, while adding (a) normative **evidence linkage** to repo-native status surfaces (Checks API / CI) and (b) a normative **execution submodel** (run/step/check references + aggregation rules) that supports deterministic automation and auditability.

**Key Findings**:
* **Finding 1 — Tool-level execution state ≠ program-level status**: Agentic CLIs emphasize *approval gating*, *sandbox/permissions*, and *event streams*, while CI/CD emphasizes *queued/in_progress/completed + conclusion*. Treating those tool states as the program’s canonical status vocabulary creates drift; a bridging layer is required.
* **Finding 2 — GitHub Checks provides the richest, most machine-operable repo-native status primitive**: The Checks model (check suite/run, status + conclusion, rich output + annotations, and PR-required-check integration) supports auditability and deterministic automation substantially better than legacy commit statuses.
* **Finding 3 — Modern orchestration semantics require explicit “allowed failure / continue-on-error / fail-fast” rules**: Without explicit aggregation semantics, parent-level status becomes ambiguous under matrix/parallel execution and will not be reliably agent-updatable.

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Stayed within the commissioned boundaries: agentic CLIs (Claude Code, Codex CLI, Gemini CLI), CI/CD comparators (GitHub Actions + GitLab CI/CD), GitHub repo status surfacing (Checks + Commit Status), repo-native audit patterns, and an explicitly non-normative bridging survey (Topic 7).

**Source of Truth Audit**:
* **Program governance (local)**:
  * `prompt/artifacts/tasks/P/research/P-RES-002/brief_P-RES-002_agentic-status-research.md` (scope authority)
  * `prompt/artifacts/tasks/P/workspace/PH000/ST004/plan_P-PH000-ST004.md` (commissioning context)
  * `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` (constraints + P-STD-002 registry)
  * `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` (indexing rules)
  * `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md` (issues/risks schema)
* **External official sources**: Limited to official docs/API references and official vendor engineering docs/blogs where the official reference surface is not sufficient (e.g., Claude Code sandboxing details).

**Limitations**:
* Agentic CLIs do not consistently publish a single, explicit “run state machine enum” comparable to CI/CD `status`/`conclusion`. Where explicit enums are absent, this report records the documented *observable lifecycle primitives* (approvals, event streams, sandbox/permissions controls) and treats any inferred states as non-authoritative.
* CI/CD and GitHub API documentation differs across GitHub Enterprise Server versions and the public GitHub.com docs; this report cites the specific source pages used and avoids assuming undocumented status values.

---

## III. TOPIC FINDINGS

### Topic 1: Agentic CLI Status State Models (Critical)
**Objective**: Benchmark how modern agent-based CLI tools model task/run lifecycle status and what “status primitives” they expose that a program governance standard can reliably reference.

#### A. Evidence & Forensics
* **Source**: OpenAI Codex — non-interactive mode (`codex exec`) documents JSON Lines (`--json`) output and enumerates machine-readable event types such as `thread.started`, `turn.*`, `item.*`, and `error`. (See: https://developers.openai.com/codex/noninteractive/)
* **Source**: OpenAI Codex — advanced configuration + config reference document `approval_policy` options, `sandbox_mode` options, and observability primitives (local `history.jsonl` + optional OTel event export). (See: https://developers.openai.com/codex/config-advanced/ and https://developers.openai.com/codex/config-reference/)
* **Source**: Anthropic Claude Code (Team) — role-specific permission modes (e.g., `plan`, `developer`) and tool-permission configuration patterns. (See: https://docs.anthropic.com/en/docs/claude-code/team)
* **Source**: Anthropic Claude Code — sandboxing/permissioning design described in an official Anthropic engineering post. (See: https://www.anthropic.com/engineering/claude-code-best-practices)
* **Source**: Google Gemini CLI — CLI provides a structured “stream-json” output format. (See: https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md)
* **Source**: Google Gemini CLI — sandboxing and trusted-folder mechanics are explicitly documented. (See: https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/sandbox.md and https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/trusted-folders.md)
* **Source**: Google Gemini CLI — configuration layering (global/project/settings; env vars). (See: https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/configuration.md)

#### B. Analysis
**Synthesis**:
* In CI/CD systems, “status” is typically a compact, documented state machine. In agentic CLIs, the most reliably documented *status primitives* are:
  1) **Approval state** (auto vs gated tool execution; “ask before running” modes),
  2) **Sandbox / permissions state** (what can be executed and where),
  3) **Event/log emission model** (structured event stream vs narrative output),
  4) **Session/run/task decomposition** (how work is segmented and tracked).
* OpenAI Codex CLI exposes particularly strong machine-operable primitives for governance bridging: configurable approval policy, configurable sandboxing, and JSON event output. These are directly usable to implement deterministic evidence linkage and “what happened” audit trails.
* Gemini CLI similarly provides structured streaming outputs and explicit sandboxing + trusted folder guardrails, which are governance-relevant primitives even if a single run-status enum is not explicitly published.
* Claude Code provides strong permission-mode primitives and extensive sandboxing/security guidance, but a fully enumerated, published run/task status state machine is not clearly centralized in the official docs surfaced here; treat “permission modes + sandboxing + logs” as the documented primitives.

**Comparative matrix (documented lifecycle/status primitives)**:

| Tool | Documented gating primitive | Documented sandbox/permissions primitive | Documented structured output primitive | Notes for governance mapping |
|:--|:--|:--|:--|:--|
| Claude Code | Permission modes (`plan`, `developer`, etc.) | Sandbox/permissioning guidance | Not confirmed as a stable event schema in official docs used | Map via approval/permissions + evidence pointers (commit/PR/checks) |
| Codex CLI | `approval_policy`, `--full-auto` | `sandbox_mode` | `codex exec --json` streams JSONL events | Strong candidate for defining “agentic operability” requirements |
| Gemini CLI | Trusted folders + config controls | Sandbox + trusted folders | `--output-format stream-json` | Good reference for “structured run output” requirements |

**Scored comparison (rubric applied to “reference value for P-STD-002 patterns”)**  
Rubric note: `Adoption Overhead` is scored as **5 = lowest overhead** / **1 = highest overhead**.

| Option | Program Fit (×5) | Industry Alignment (×4) | Agentic Operability (×5) | Adoption Overhead (×3) | Extensibility (×2) | Weighted Total (max 95) |
|:--|--:|--:|--:|--:|--:|--:|
| Claude Code | 4 | 4 | 4 | 3 | 3 | 71 |
| Codex CLI | 5 | 4 | 5 | 3 | 4 | 83 |
| Gemini CLI | 4 | 4 | 4 | 3 | 4 | 73 |

**Gap analysis**:
* The agentic CLI ecosystem tends to document *controls* (approvals, sandboxing, settings) and *observability primitives* (logs/events) more reliably than a canonical state enum. Therefore, `P-STD-002` SHOULD NOT attempt to standardize tool-native run enums as program status; it SHOULD standardize:
  - minimum required **evidence** for program status transitions, and
  - a stable **execution reference model** (run/step/check identifiers + aggregation rules).

**Session state vs task state (commissioned question)**:
* **Session state (CLI-level)**: These tools publish session-scoped controls that govern *how work may proceed*, not a single “task state enum”.
  - **Codex CLI**: `approval_policy` and `sandbox_mode` are configured for the session/run; the non-interactive JSONL stream emits per-turn/per-item events beneath that session scope. (See: https://developers.openai.com/codex/config-advanced/ and https://developers.openai.com/codex/noninteractive/)
  - **Gemini CLI**: sandbox/trusted-folder controls are session-scoped; `stream-json` output provides machine-readable observability for sub-steps within a run. (See: https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/sandbox.md and https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md)
  - **Claude Code**: permission modes (e.g., `plan`, `developer`) configure what the agent can do during a session; a separate, published “task state enum” is not centralized in the official sources used here. (See: https://docs.anthropic.com/en/docs/claude-code/team)
* **Task state (within-session work items)**: Where CI/CD exposes job-level `status`/`conclusion`, agentic CLIs typically expose *step/tool-call events* (e.g., Codex `item.*`) as the task-equivalent observability surface. (See: https://developers.openai.com/codex/noninteractive/)

**Terminal states and trigger conditions (commissioned question)**:
* **Codex CLI (documented terminal primitives)**:
  - In JSONL mode, Codex explicitly emits `turn.completed` and `turn.failed` events and can emit `error` events for failures, providing machine-operable terminal signals even without a single published run-state enum. (See: https://developers.openai.com/codex/noninteractive/)
* **Claude Code / Gemini CLI (bounded statement)**:
  - The official sources used here emphasize permissions/sandboxing and structured output. They do not publish a single, comparable “terminal enum” list; treat terminal outcomes as evidenced by their repo-native evidence pointers (checks/PR/commits) and any structured outputs the tool emits. (See: https://docs.anthropic.com/en/docs/claude-code/team and https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md)

#### C. Governance Implication
* **Decision Impact** (`P-STD-002A`, `P-STD-002D`, `P-STD-002E`): Keep the 7-state program status vocabulary stable, but add a governed “execution references” submodel (non-status) that can point to tool/CI evidence (runs/checks/artifacts) and capture approval/sandbox posture used during execution.
* **Risk**: Overfitting to one agentic tool’s internal semantics; mitigation is to standardize only the cross-tool bridge primitives (IDs, evidence, aggregation, provenance), not vendor-specific internal states.

---

### Topic 2: Hierarchical/Nested Task Status (High)
**Objective**: Evaluate patterns for representing and aggregating status in nested/hierarchical execution (subtasks, tool calls, parallel steps).

#### A. Evidence & Forensics
* **Source**: OpenAI Codex — `codex exec --json` turns `stdout` into a JSONL event stream and enumerates event types including `thread.started`, `turn.*`, `item.*`, and `error`. (See: https://developers.openai.com/codex/noninteractive/)
* **Observation**: The JSONL stream provides an explicit nesting trace (thread/run → turns → items such as command executions, file changes, and tool calls). This enables deterministic child-unit referencing without requiring a separate “subtask status API”.
* **Source**: GitHub Checks API includes “check runs” with `status` and `conclusion` and rich output/annotations, suitable as child-units beneath a program-level status. (See: https://docs.github.com/en/rest/checks/runs)

#### B. Analysis
**Synthesis**:
* Nested execution is the default in agentic workflows (plans → steps → tool calls → file edits). However, parent/child status aggregation is rarely fully specified in CLI docs.
* CI/CD (and GitHub Checks) provides the clearest usable nesting: many check runs/jobs/steps can roll up into a single “overall” status in PR UI via required checks.
* A program standard should therefore define deterministic parent/child aggregation rules at the program layer (independent of vendor tooling):
  - **Fail-fast** (any child fails → parent fails),
  - **Allow-failure** (child can fail without failing parent, but must be marked),
  - **Continue-on-error** (execution continues; final conclusion depends on policy),
  - **Skipped/manual** semantics.

**Gap analysis**:
* Agentic CLIs lack a cross-vendor documented aggregation model; `P-STD-002` should treat aggregation as a governance-layer rule and require evidence references to child units (checks/jobs/steps) for auditability.

#### C. Governance Implication
* **Decision Impact** (`P-STD-002B`, `P-STD-002D`, `P-STD-002E`): Define parent/child aggregation semantics as normative governance rules (not vendor states), so automated updates can compute program status from referenced evidence.
* **Risk**: Inconsistent aggregation across initiatives/tools if not standardized; mitigation is a single program-level aggregation policy with an explicit “allowed-failure” annotation model.

---

### Topic 3: GitHub Actions vs GitLab CI/CD Workflow Status Architecture (Critical)
**Objective**: Benchmark status architecture and propagation rules for two CI/CD platforms to ground orchestration status patterns in documented practice.

#### A. Evidence & Forensics
* **Source**: GitHub Actions matrix `strategy.fail-fast` and job-level `continue-on-error` controls are documented as workflow syntax. (See: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
* **Source**: GitHub Checks API guide enumerates check run `status` and `conclusion` values (and distinguishes status vs conclusion). (See: https://docs.github.com/en/enterprise-server@3.14/rest/guides/using-the-rest-api-to-interact-with-checks)
* **Source**: GitHub Actions workflow runs API enumerates the status/conclusion vocabulary accepted by its `status` filter parameter. (See: https://docs.github.com/en/enterprise-server@3.20/rest/actions/workflow-runs)
* **Source**: GitHub Actions workflow jobs API enumerates job-level `status` and `conclusion` values and enumerates step-level `status` values. (See: https://docs.github.com/en/enterprise-server@3.18/rest/actions/workflow-jobs)
* **Source**: GitLab Pipelines API enumerates pipeline status values. (See: https://docs.gitlab.com/api/pipelines/)
* **Source**: GitLab Jobs API enumerates job status values. (See: https://docs.gitlab.com/api/jobs/)
* **Source**: GitLab manual jobs (`when: manual`) block pipelines unless configured otherwise (status “manual”). (See: https://docs.gitlab.com/ci/jobs/job_control/)
* **Source**: GitHub “Status checks” UI is the primary repo-native surfacing for CI results on pull requests. (See: https://docs.github.com/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)

#### B. Analysis
**Synthesis**:
* Both platforms implement a hierarchy (workflow/pipeline → jobs → steps) and support conditional execution; the details differ, but key shared patterns exist:
  - **In-progress status** is distinct from **terminal conclusion/result**.
  - Aggregation can be influenced by policy flags (fail-fast, allow-failure, manual steps).
* For a GitHub-first program, the most governance-relevant “status surface” is the PR checks interface, which is heavily aligned with GitHub Checks (Topic 5).

**Element B3a — Complete status/conclusion enum values per hierarchy level (commissioned deliverable)**:

**GitHub (Actions + Checks)**

| Hierarchy Level | `status` (progress) values | `conclusion` (terminal) values | Notes |
|:--|:--|:--|:--|
| Check run (Checks API) | `queued`, `in_progress`, `requested`, `waiting`, `pending`, `completed` | `action_required`, `cancelled`, `timed_out`, `failure`, `neutral`, `skipped`, `stale`, `startup_failure`, `success` | Only GitHub Actions can set `requested`/`waiting`/`pending` (per GitHub docs); `stale`/`startup_failure` are documented terminal outcomes in the checks guide. (See: https://docs.github.com/en/enterprise-server@3.14/rest/guides/using-the-rest-api-to-interact-with-checks) |
| Workflow run (Actions API filter surface) | `in_progress`, `queued`, `requested`, `waiting`, `pending`, `completed` | `action_required`, `cancelled`, `timed_out`, `failure`, `neutral`, `skipped`, `stale`, `success` | The workflow-runs API’s `status` filter accepts both check-run status and conclusion values, which is evidence that GitHub surfaces “progress” and “result” as separate concepts but sometimes conflates them at query/filter surfaces. (See: https://docs.github.com/en/enterprise-server@3.20/rest/actions/workflow-runs) |
| Job (Actions API) | `queued`, `in_progress`, `requested`, `waiting`, `pending`, `completed` | `success`, `failure`, `neutral`, `cancelled`, `skipped`, `timed_out`, `action_required`, `null` | Job-level status/conclusion enums are explicitly enumerated in the workflow jobs API schema. (See: https://docs.github.com/en/enterprise-server@3.18/rest/actions/workflow-jobs) |
| Step (within job) | `queued`, `in_progress`, `completed` | (present, not exhaustively enumerated in schema on this page) | The workflow jobs API enumerates step `status` values; step `conclusion` is shown but not enumerated as a fixed list in the schema excerpt on this page. (See: https://docs.github.com/en/enterprise-server@3.18/rest/actions/workflow-jobs) |

**GitLab CI/CD**

| Hierarchy Level | Status values | Notes |
|:--|:--|:--|
| Pipeline | `created`, `waiting_for_resource`, `preparing`, `pending`, `running`, `success`, `failed`, `canceled`, `skipped`, `manual`, `scheduled` | Pipeline status values are explicitly enumerated by the pipelines API. (See: https://docs.gitlab.com/api/pipelines/) |
| Job | `canceled`, `canceling`, `created`, `failed`, `manual`, `pending`, `preparing`, `running`, `scheduled`, `skipped`, `success`, `waiting_for_callback`, `waiting_for_resource` | Job status values are explicitly enumerated by the jobs API. (See: https://docs.gitlab.com/api/jobs/) |

**Element B3b — Textual architecture description (commissioned deliverable; substitute for diagram)**:

GitHub Actions / GitHub Checks hierarchy:
  Workflow Run (Actions API; `status` + `conclusion` fields; filter surface accepts both status and conclusion values)
    └── Job (Actions API; `status` + `conclusion`)
          └── Step (within job; `status` enumerated; conclusion present but not enumerated in schema on the cited page)
  Check Suite (collection surface for a commit)
    └── Check Run (repo-native check primitive used for PR gating; `status` + `conclusion` + rich output/annotations)

GitLab CI/CD hierarchy:
  Pipeline (Pipelines API; pipeline `status` enumerated)
    └── Job (Jobs API; job `status` enumerated; manual jobs can block/require intervention)
  (Stages are a logical grouping of jobs; governance visibility typically uses pipeline/job status primitives.)

**Scored comparison (rubric applied to “reference platform for P-STD-002 orchestration patterns”)**:

| Option | Program Fit (×5) | Industry Alignment (×4) | Agentic Operability (×5) | Adoption Overhead (×3) | Extensibility (×2) | Weighted Total (max 95) |
|:--|--:|--:|--:|--:|--:|--:|
| GitHub Actions | 5 | 5 | 5 | 4 | 4 | 90 |
| GitLab CI/CD | 3 | 4 | 4 | 3 | 4 | 68 |

**Gap analysis**:
* `P-STD-002` SHOULD use GitHub Actions + Checks as the primary reference because it aligns to actual repo-native surfaces used for governance (PR checks), while still capturing GitLab as a non-GitHub comparator to avoid silently assuming GitHub-only semantics.

#### C. Governance Implication
* **Decision Impact** (`P-STD-002C`, `P-STD-002D`, `P-STD-002E`): `P-STD-002` should incorporate explicit orchestration aggregation semantics (fail-fast / allow-failure / manual/blocked states) and require evidence references to CI runs/checks when CI is the authoritative execution surface.
* **Risk**: Mixing platform-specific status vocabulary into program-level status; mitigation is to standardize a program-level status + execution reference model, not GitHub/GitLab enums.

---

### Topic 4: Multi-Agent/Pipeline Orchestration Patterns (High)
**Objective**: Evaluate status aggregation patterns across parallel/sequential execution and failure-propagation models.

#### A. Evidence & Forensics
* **Source**: GitHub Actions supports `strategy.fail-fast` for matrices. (See: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
* **Source**: GitHub Actions supports job-level `continue-on-error`. (See: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
* **Source**: GitLab supports `when: manual` jobs that block pipelines. (See: https://docs.gitlab.com/ci/jobs/job_control/)
* **Source**: GitLab documents a `manual` pipeline status in badge statuses (status surfacing). (See: https://docs.gitlab.com/user/project/badges/)
* **Source**: GitLab CI YAML `allow_failure` explicitly allows a job to fail without causing the pipeline to fail, and describes how these jobs are treated in status evaluation. (See: https://docs.gitlab.com/ci/yaml/)

#### B. Analysis
**Taxonomy (governance-relevant aggregation patterns)**:
1. **Fail-fast**: abort remaining parallel work on first failure (good for time/cost; reduces evidence completeness).
2. **Continue-on-error / allow-failure**: a subunit can fail while overall workflow remains “successful” per policy; requires explicit marking to avoid hidden failure.
3. **Manual/blocked gating**: human approval/trigger required; creates a distinct “waiting” state which must map to program governance (`on_hold` vs `blocked`) depending on cause.
4. **Skipped/conditional**: subunits do not run; must be distinguishable from success/failure when computing aggregated status.

**Gap analysis**:
* Traditional program status standards often assume linear state transitions. Agentic + CI workflows are graph-shaped and policy-driven; without explicit aggregation semantics, program-level health and dependency visibility will be non-deterministic for agents and humans.

**Distinct observation (commissioned quality uplift)**:
* **Observation**: GitLab’s `allow_failure` creates a “pipeline success with warning semantics” pattern: some subunits can fail while the parent pipeline remains non-failed. Without explicit governance rules, a “green” pipeline can mask governance-significant failures. (See: https://docs.gitlab.com/ci/yaml/)

#### C. Governance Implication
* **Decision Impact** (`P-STD-002B`, `P-STD-002D`): Require an explicit aggregation policy for computing (a) program health signals and (b) parent-level progress/status from child evidence references.
* **Risk**: “Allowed failure” becomes a loophole for poor quality; mitigation is to require explicit labeling + rationale + impact on health (e.g., yellow with documented exception).

---

### Topic 5: GitHub Checks API vs Commit Status API (Critical)
**Objective**: Benchmark GitHub’s two status surfacing mechanisms and determine the minimal, most robust repo-native status primitive for evidence linkage.

#### A. Evidence & Forensics
* **Source**: GitHub Check Runs API — status values (`queued`, `in_progress`, `completed`) and conclusion values (success/failure/etc.), with rich output/annotations and API semantics. (See: https://docs.github.com/en/rest/checks/runs)
* **Source**: GitHub Commit Status API — state values (`error`, `failure`, `pending`, `success`) and combined-state aggregation. (See: https://docs.github.com/en/rest/commits/statuses)
* **Source**: GitHub “About status checks” — describes checks as the PR merge gate surface and notes retention. (See: https://docs.github.com/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)

#### B. Analysis
**Synthesis**:
* Checks are the modern, richly structured model with a clear distinction between `status` (progress) and `conclusion` (result), and support for annotations/output/actions suitable for audit evidence.
* Commit statuses are simpler and widely supported, but provide fewer primitives (single `state` + description/target URL) and weaker audit richness.

**Scored comparison (rubric applied to “repo-native status primitive to anchor P-STD-002 evidence linkage”)**:
Rubric note: `Adoption Overhead` is scored as **5 = lowest overhead** / **1 = highest overhead**.

| Option | Program Fit (×5) | Industry Alignment (×4) | Agentic Operability (×5) | Adoption Overhead (×3) | Extensibility (×2) | Weighted Total (max 95) |
|:--|--:|--:|--:|--:|--:|--:|
| Checks API | 5 | 5 | 5 | 3 | 5 | 89 |
| Commit Status API | 3 | 4 | 3 | 5 | 2 | 65 |

**Gap analysis**:
* If `P-STD-002` does not define a canonical evidence linkage target, initiatives will link to heterogeneous artifacts (logs, screenshots, chat transcripts) and auditability will degrade. Checks provides the best “single primitive” anchor in a GitHub-first program.

#### C. Governance Implication
* **Decision Impact** (`P-STD-002D`, `P-STD-002E`): `P-STD-002` SHOULD standardize evidence linkage to GitHub Checks as the primary mechanism, with commit statuses as a fallback only when checks are unavailable.
* **Risk**: Checks integration often implies GitHub Apps or specific auth patterns; mitigation is to permit a fallback path and specify “minimum viable evidence pointer” fields independent of API choice.

---

### Topic 6: Repo-Native Audit Trail Patterns (High)
**Objective**: Evaluate how agentic tools and CI systems can produce repo-native audit trails suitable as evidence for governance status transitions.

#### A. Evidence & Forensics
* **Source**: OpenAI Codex — `codex exec --json` makes `stdout` a JSONL stream so scripts can capture every event emitted during a run (including `turn.*`, `item.*`, and `error`). (See: https://developers.openai.com/codex/noninteractive/)
* **Source**: Gemini CLI structured `stream-json` output is explicitly provided for machine consumption. (See: https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md)
* **Source**: GitHub status checks are displayed and retained as the repo’s merge gating surface for PRs. (See: https://docs.github.com/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
* **Source**: GitHub Checks API exposes rich fields (output + annotations) that can serve as evidence attachments for governance decisions. (See: https://docs.github.com/en/rest/checks/runs)

#### B. Analysis
**Taxonomy of repo-native audit trail patterns (recommended to standardize as “evidence classes”)**:
1. **PR/commit-linked checks evidence**: check runs and summaries attached to the commit/PR (preferred for CI evidence).
2. **Commit message evidence pointers**: commit messages reference stable IDs (run IDs, check run IDs, artifact paths).
3. **Version-controlled status ledgers**: machine-readable YAML/JSON ledgers stored under deterministic paths (per `P-CON-003(B)`), updated by agents and reviewed by humans.
4. **Narrative status summaries**: Markdown summaries that explain “why” (human readable), linked to machine ledger entries and checks.
5. **Execution trace artifacts (optional)**: stored run logs or JSONL event streams when justified (size/privacy concerns).

**Distinct observation (commissioned quality uplift)**:
* **Observation**: Codex JSONL output and Gemini `stream-json` output are explicitly designed for machine consumption. When persisted as repo artifacts (or summarized into checks output/annotations), these structured streams constitute a verifiable execution trace that supports the MVAT “execution trace artifact (optional)” tier without relying on screenshots or narrative-only claims. (See: https://developers.openai.com/codex/noninteractive/ and https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md)

**Minimum viable audit trail (MVAT) recommended**:
* A stable, version-controlled status ledger entry includes:
  - program status (7-state enum) + timestamp + author role
  - evidence pointer(s) to: check run(s) and/or workflow run(s) and/or PR
  - aggregation policy used (fail-fast vs allow-failure)
  - rationale summary (narrative pointer)

**Gap analysis**:
* Without a standardized evidence pointer schema and explicit linkage to repo-native primitives, status transitions will be unverifiable and governance gates will degrade into narrative-only claims.

#### C. Governance Implication
* **Decision Impact** (`P-STD-002D`, `P-STD-002E`): `P-STD-002` SHOULD define a minimal evidence-pointer schema and require that terminal transitions cite at least one repo-verifiable evidence primitive (checks/PR/commit).
* **Risk**: Privacy/security concerns in storing traces; mitigation is to treat traces as optional and prefer summary + links to platform-native logs.

---

### Topic 7: Bridging Agentic Status to Program Governance (Survey — Informational / vNext)
**Objective**: Survey patterns for aggregating heterogeneous tool-level statuses into a unified program-level governance status view.

#### A. Evidence & Forensics
* **Source**: Checks API provides a stable repo-native “status primitive” that can be referenced from governance artifacts. (See: https://docs.github.com/en/rest/checks/runs)
* **Source**: OpenAI Codex provides structured JSONL event output suitable for linking execution traces to governance artifacts. (See: https://developers.openai.com/codex/noninteractive/)
* **Source**: Gemini CLI provides structured machine output and sandbox/trusted-folder controls. (See: https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md and https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/sandbox.md)

#### B. Analysis
**Recommended bridging pattern (informational; not normative requirements for P-STD-002 v1)**:
* Treat “tool execution” as an **evidence graph** (runs/jobs/checks) and program status as a **governed declaration**.
* Provide a deterministic mapping layer:
  - Tool/CI execution references: `{platform, id, url, status, conclusion, started_at, completed_at}`
  - Aggregation policy: `{fail_fast, allow_failure, continue_on_error, manual_gate}`
  - Program status: 7-state vocabulary, computed suggestions permitted but final is governed
* Use repo-native primitives as the cross-initiative bridge:
  - PR number + commit SHA + checks/check-runs as canonical anchors.

**Crosswalk (example mapping guidance)**:
* “Manual gate / waiting approval” → program `on_hold` (if waiting by policy) or `blocked` (if waiting due to unmet prerequisite).
* “CI failed (required check)” → program `blocked` (if work cannot progress) or remain `in_progress` with explicit blocker evidence pointer.
* “Some jobs allowed to fail” → do not mark program `completed` without declaring exception + health impact.

#### C. Governance Implication
* **Decision Impact**: This topic primarily informs **vNext** bridging architecture work; for `P-STD-002 v1`, incorporate only the minimum deterministic primitives needed to support evidence linkage and aggregation.

---

## III.8 CROSS-TOPIC INTEGRATION

### Integration 1: Agentic CLI models (Topic 1) vs CI/CD architecture (Topic 3)
**Common pattern**: Both agentic CLIs and CI/CD platforms separate **progress state** (what is happening now) from a **terminal result** (what happened), even when their internal UX vocabulary differs.
* **CI/CD**: Explicit `status` vs `conclusion` (e.g., GitHub Checks `queued/in_progress/completed` vs `success/failure/...`; GitLab pipeline/job lifecycle statuses). (See: https://docs.github.com/en/enterprise-server@3.14/rest/guides/using-the-rest-api-to-interact-with-checks and https://docs.gitlab.com/api/pipelines/)
* **Agentic CLIs**: Session-level controls (approvals/sandboxing) + step-level event streams provide the machine-operable progress/terminal surface (e.g., Codex `turn.completed` / `turn.failed` + `item.*`). (See: https://developers.openai.com/codex/noninteractive/)

**Unification recommendation for P-STD-002**: Standardize the program’s 7-state status as a **governed declaration**, and standardize tool/CI execution as an **evidence graph** with explicit `{status, conclusion}` (or equivalent) fields plus aggregation semantics, rather than attempting to import vendor enums into the program’s canonical status vocabulary.

### Integration 2: Hierarchical status (Topic 2) vs aggregate orchestration (Topic 4)
**Single aggregation model suffices**: The same aggregation taxonomy covers both agentic nesting (run → turns → items/tool calls) and CI/CD orchestration (pipeline/workflow → jobs → steps):
* `fail_fast` (any child fails ⇒ parent fails)
* `continue_on_error` (child failures do not stop execution; terminal result depends on policy)
* `allow_failure` (child failure is explicitly tolerated but must be visible)
* `manual_gate` / `blocked` (execution cannot proceed without explicit manual action)
* `skipped` (not executed due to condition/dependency)

**Recommendation**: `P-STD-002` SHOULD require an explicit aggregation policy declaration whenever program status is updated based on nested evidence references, so automated updates remain deterministic and auditable.

### Integration 3: Repo-native surfacing (Topic 5) vs audit trail patterns (Topic 6)
**Minimum Checks API integration for evidence linkage**:
* Minimum viable pattern: create/associate a **check run** for each governance-significant automated operation (CI job set, agentic automation pass, compliance scan), then store the check run reference (ID + URL) as the evidence pointer in the program’s status ledger entry. (See: https://docs.github.com/en/rest/checks/runs and https://docs.github.com/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
* Structured execution traces (Codex JSONL / Gemini stream-json) are the machine-operable “execution trace artifact” class that can be linked to or summarized into the check run output/annotations when needed. (See: https://developers.openai.com/codex/noninteractive/ and https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md)

### Gap Analysis: What is NOT covered by P-RES-001?

| Gap Pattern (agentic/CI specific) | NOT in P-RES-001 | Relevant P-STD-002 CLAUSE |
|:--|:--:|:--|
| Execution reference submodel (run/check identifiers; step/item references) | ✓ | `P-STD-002A`, `P-STD-002E` |
| Approval/sandbox posture as governed execution metadata | ✓ | `P-STD-002E` |
| Machine-operable aggregation policy (fail-fast / allow-failure / manual gate) | ✓ | `P-STD-002B`, `P-STD-002D` |
| Repo-native evidence pointer schema anchored to Checks API primitives | ✓ | `P-STD-002D` |
| Terminal classification via CI “conclusion” semantics (not narrative-only) | ✓ | `P-STD-002A`, `P-STD-002D` |

---

## IV. ISSUE & RISK REGISTER (T102-STD-007)

**Issues**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `P-RES-002-ISSUE-001` | Agentic CLI status enums not standardized | Official docs for agentic CLIs emphasize approvals/sandbox/event output, but do not consistently publish a single run/task status enum comparable to CI/CD `status`/`conclusion`, limiting deterministic direct mapping. | LLM_Consultant | `OPEN` | `HIGH` | 2026-02-25 | — | — |
| `P-RES-002-ISSUE-002` | GitHub version drift risk | GitHub API/docs vary across Enterprise Server versions vs GitHub.com; status/conclusion semantics must be pinned to specific doc sources in `P-STD-002` to avoid drift. | LLM_Consultant | `OPEN` | `MEDIUM` | 2026-02-25 | — | — |

**Risks**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `P-RES-002-RISK-001` | Vendor lock-in via Checks-only evidence | Over-standardizing on GitHub Checks semantics could reduce portability for non-GitHub initiatives. | LLM_Consultant | `MONITORED` | `MEDIUM` | 2026-02-25 | Specify Checks as primary evidence anchor for GitHub-first initiatives, but define an API-agnostic minimum evidence-pointer schema + fallback to commit statuses. | — |
| `P-RES-002-RISK-002` | Silent “allowed failures” degrade governance | CI systems can mark overall pipelines green even with allowed failures; without explicit governance rules, program health/status becomes misleading. | LLM_Consultant | `OPEN` | `HIGH` | 2026-02-25 | Require explicit “allow-failure/continue-on-error/manual gate” annotations in the status ledger + aggregation policy in evidence references; map to health/RAG policy. | — |

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
| :--- | :--- | :--- | :--- |
| `P-STD-002A` | Status Vocabulary | Keep 7-state program enum stable; add non-status “execution reference” vocabulary (run/check identifiers + manual gate states) as governed fields. | Topic 1.B, Topic 7.B |
| `P-STD-002B` | Health Assessment | Add explicit rule: allowed-failure / continue-on-error must affect health assessment (cannot be silently ignored). | Topic 4.B, Topic 6.B |
| `P-STD-002C` | Dependency Visibility | Add orchestration dependency semantics for graph execution (`needs`, pipeline/job dependencies) as an evidence-facing submodel, not program status. | Topic 3.B, Topic 4.B |
| `P-STD-002D` | Update Protocol | Standardize evidence linkage: prefer GitHub Checks; require aggregation policy declarations for nested/parallel evidence. | Topic 5.B, Topic 2.B |
| `P-STD-002E` | Status Artifact | Require status ledger schema to carry evidence pointers (checks/workflow runs/PR/commit), optional execution trace references, and sandbox/approval posture fields when agentic tooling is used. | Topic 6.B, Topic 1.B |

---

## VI. SOURCE MATERIAL

* **Brief Version**: `P-RES-002` brief v1.0.0 (2026-02-25): `prompt/artifacts/tasks/P/research/P-RES-002/brief_P-RES-002_agentic-status-research.md`
* **Local Files Cited**:
  * `prompt/artifacts/tasks/P/workspace/PH000/ST004/plan_P-PH000-ST004.md`
  * `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
  * `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md`
  * `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
* **Official External Sources (primary)**:
  * `OFFICIAL_DOC` — OpenAI Codex — Non-interactive mode (`codex exec` + `--json` JSONL output): https://developers.openai.com/codex/noninteractive/
  * `OFFICIAL_DOC` — OpenAI Codex — Advanced configuration: https://developers.openai.com/codex/config-advanced/
  * `OFFICIAL_DOC` — OpenAI Codex — Configuration reference: https://developers.openai.com/codex/config-reference/
  * `OFFICIAL_DOC` — Anthropic Claude Code docs (Team): https://docs.anthropic.com/en/docs/claude-code/team
  * `OFFICIAL_DOC` — Anthropic engineering post (Claude Code sandboxing/best practices): https://www.anthropic.com/engineering/claude-code-best-practices
  * `OFFICIAL_DOC` — Gemini CLI README + docs: https://raw.githubusercontent.com/google-gemini/gemini-cli/main/README.md ; https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/sandbox.md ; https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/trusted-folders.md ; https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/configuration.md
  * `OFFICIAL_DOC` — GitHub REST API — Check Runs: https://docs.github.com/en/rest/checks/runs
  * `OFFICIAL_DOC` — GitHub REST API guide — Using the REST API to interact with checks (enum lists): https://docs.github.com/en/enterprise-server@3.14/rest/guides/using-the-rest-api-to-interact-with-checks
  * `OFFICIAL_DOC` — GitHub REST API — Workflow runs: https://docs.github.com/en/enterprise-server@3.20/rest/actions/workflow-runs
  * `OFFICIAL_DOC` — GitHub REST API — Workflow jobs: https://docs.github.com/en/enterprise-server@3.18/rest/actions/workflow-jobs
  * `OFFICIAL_DOC` — GitHub REST API — Commit Statuses: https://docs.github.com/en/rest/commits/statuses
  * `OFFICIAL_DOC` — GitHub Docs — Status checks: https://docs.github.com/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks
  * `OFFICIAL_DOC` — GitHub Actions workflow syntax: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions
  * `OFFICIAL_DOC` — GitLab API — Pipelines: https://docs.gitlab.com/api/pipelines/
  * `OFFICIAL_DOC` — GitLab API — Jobs: https://docs.gitlab.com/api/jobs/
  * `OFFICIAL_DOC` — GitLab CI YAML reference (`allow_failure`): https://docs.gitlab.com/ci/yaml/
  * `OFFICIAL_DOC` — GitLab docs — job control/manual jobs: https://docs.gitlab.com/ci/jobs/job_control/
