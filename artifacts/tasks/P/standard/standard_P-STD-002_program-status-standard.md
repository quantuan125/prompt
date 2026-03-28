---
artifact_type: 'STANDARD'
initiative_id: 'P'
initiative_code: 'PROGRAM'
standard_id: 'P-STD-002'
version: '1.3.0'
date: '2026-03-28'
status: 'accepted'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
approval_date: '2026-03-04'
effective_date: '2026-03-04'
---

# P-STD-002 — Program Status Standard {#p-std-002-program-status-standard}

## Specification

### Specification Index
| # | Substandard | CLAUSE ID | Title | Description |
|:--|:--|:--|:--|:--|
| 1 | General | P-STD-002-CLAUSE-055 | Forward-Only Adoption (General) | Defines forward-only adoption for P-STD-002 requirements per P-ASSUM-001. |
| 2 | P-STD-002A | P-STD-002-CLAUSE-001 | Canonical Status Vocabulary | Defines the canonical 8-state program status enum and per-state semantics. |
| 3 | P-STD-002A | P-STD-002-CLAUSE-002 | Tool Meta-Category Mapping | Requires deterministic mapping of program statuses to tool meta-categories. |
| 4 | P-STD-002A | P-STD-002-CLAUSE-003 | Local Status Extension Mapping | Permits local extension states, but requires mapping to the canonical vocabulary. |
| 5 | P-STD-002A | P-STD-002-CLAUSE-004 | Initial and Terminal States | Defines initial and terminal states and their normative meaning at program scope. |
| 6 | P-STD-002A | P-STD-002-CLAUSE-005 | Transition Matrix | Defines the allowed status transitions and their evidence/role markings. |
| 7 | P-STD-002A | P-STD-002-CLAUSE-006 | Guard Conditions | Defines minimum guard conditions (G1–G10) required for allowed transitions. |
| 8 | P-STD-002A | P-STD-002-CLAUSE-007 | Evidence-Required Transitions | Defines which transitions require evidence pointers and validation. |
| 9 | P-STD-002A | P-STD-002-CLAUSE-008 | Role-Restricted Transitions | Defines which transitions are role-restricted using generic RACI labels. |
| 10 | P-STD-002A | P-STD-002-CLAUSE-009 | Blocked vs On-Hold vs Deferred Semantics | Defines operational meaning of `blocked` vs `on_hold` vs `deferred`, including attribute-compatible encoding. |
| 11 | P-STD-002A | P-STD-002-CLAUSE-010 | Execution Posture Fields (Non-Status) | Defines how execution posture is recorded without extending the status vocabulary. |
| 12 | P-STD-002A | P-STD-002-CLAUSE-011 | Manual Gate Crosswalk (Informative) | Provides a cause-based mapping for manual gates and “waiting approval” states. |
| 13 | P-STD-002B | P-STD-002-CLAUSE-012 | Standard Health Dimensions | Defines required health dimensions at program roll-up and initiative-level deferral rules. |
| 14 | P-STD-002B | P-STD-002-CLAUSE-013 | RAG Threshold Method | Defines the tolerance-based hybrid method for computing Green/Amber/Red per dimension. |
| 15 | P-STD-002B | P-STD-002-CLAUSE-014 | Dimension-Level RAG Computation | Requires independent per-dimension RAG computation against configured tolerances. |
| 16 | P-STD-002B | P-STD-002-CLAUSE-015 | Overall RAG Aggregation | Defines deterministic roll-up rules from dimension RAGs to overall health RAG. |
| 17 | P-STD-002B | P-STD-002-CLAUSE-016 | Initiative Configuration | Permits initiative-configured tolerance values and optional additional dimensions. |
| 18 | P-STD-002B | P-STD-002-CLAUSE-017 | Health Assessment Cadence | Defines minimum cadence expectations and “update on transition” triggers. |
| 19 | P-STD-002B | P-STD-002-CLAUSE-018 | Allowed-Failure Health Impact | Requires health reporting to reflect “allowed failure” and “continue on error” semantics. |
| 20 | P-STD-002C | P-STD-002-CLAUSE-019 | Dependency Edge Schema | Defines the required dependency edge fields, including actionable owner semantics. |
| 21 | P-STD-002C | P-STD-002-CLAUSE-020 | Relationship Semantics | Defines `depends_on` and `blocks` semantics and directionality. |
| 22 | P-STD-002C | P-STD-002-CLAUSE-021 | Category Taxonomy | Defines minimum dependency categories and extension rules. |
| 23 | P-STD-002C | P-STD-002-CLAUSE-022 | Criticality Classification | Defines criticality classes and minimum interpretation rules. |
| 24 | P-STD-002C | P-STD-002-CLAUSE-023 | Dependency Status Enum | Defines a separate dependency-lifecycle enum distinct from program status. |
| 25 | P-STD-002C | P-STD-002-CLAUSE-024 | Optional Schedule Enrichment | Defines optional schedule relationship semantics (FS/SS/FF/SF) and lag. |
| 26 | P-STD-002C | P-STD-002-CLAUSE-025 | Cross-Initiative Interface Contract | Defines the minimum cross-initiative dependency interface for program reporting. |
| 27 | P-STD-002C | P-STD-002-CLAUSE-026 | Conformance Rule | Requires local models to map to the program interface without loss of meaning. |
| 28 | P-STD-002C | P-STD-002-CLAUSE-027 | Roll-Up View Requirement | Requires surfacing cross-initiative dependencies in program status reporting. |
| 29 | P-STD-002C | P-STD-002-CLAUSE-028 | Orchestration Reference Fields (Optional) | Permits optional orchestration identifiers on dependency edges for traceability. |
| 30 | P-STD-002C | P-STD-002-CLAUSE-029 | Category Extension Examples (Informative) | Provides example categories for orchestration and agent handoffs without binding. |
| 31 | P-STD-002D | P-STD-002-CLAUSE-030 | Evidence Pointer Schema | Defines the required evidence pointer entry schema for status updates. |
| 32 | P-STD-002D | P-STD-002-CLAUSE-031 | Evidence Type Taxonomy | Defines baseline evidence types for consistent interpretation and tooling. |
| 33 | P-STD-002D | P-STD-002-CLAUSE-032 | Evidence Requirements by Transition | Requires evidence for terminal transitions and reopen transitions. |
| 34 | P-STD-002D | P-STD-002-CLAUSE-033 | Evidence Validation Rules | Requires evidence pointers to be resolvable and correctly attributed. |
| 35 | P-STD-002D | P-STD-002-CLAUSE-034 | Role Accountability Model | Defines hybrid accountability: routine updates attributed, high-impact transitions restricted. |
| 36 | P-STD-002D | P-STD-002-CLAUSE-035 | Role-Transition Matrix | Defines transition permissions using generic RACI labels (not named roles). |
| 37 | P-STD-002D | P-STD-002-CLAUSE-036 | Update Attribution Fields | Requires `updated_by` and `last_updated` fields to support auditability. |
| 38 | P-STD-002D | P-STD-002-CLAUSE-037 | Conflict Resolution | Defines dispute handling for conflicting updates and escalation requirements. |
| 39 | P-STD-002D | P-STD-002-CLAUSE-038 | Stale-State Governance | Defines minimum stale-state review thresholds, escalation posture, and non-automation boundary for active non-terminal states, including `deferred`. |
| 40 | P-STD-002D | P-STD-002-CLAUSE-039 | Repo-Verifiable Evidence Requirement | Requires terminal transitions to cite repo-verifiable evidence, with platform-agnostic fallbacks. |
| 41 | P-STD-002D | P-STD-002-CLAUSE-040 | Evidence Type Extensions | Extends evidence types with `check`, `workflow_run`, and optional `execution_trace`. |
| 42 | P-STD-002D | P-STD-002-CLAUSE-041 | Aggregation Policy Declaration | Requires explicit aggregation policy for multi-evidence updates with clear semantics. |
| 43 | P-STD-002D | P-STD-002-CLAUSE-042 | Silent Allowed-Failure Prohibition | Prohibits “silent green” completions when failures are allowed without explicit rationale. |
| 44 | P-STD-002E | P-STD-002-CLAUSE-043 | Artifact Set Definition | Defines the canonical artifact set: ledger + narrative, with optional changelog. |
| 45 | P-STD-002E | P-STD-002-CLAUSE-044 | Authority Hierarchy | Defines ledger authority over narrative to prevent drift and ambiguity. |
| 46 | P-STD-002E | P-STD-002-CLAUSE-045 | Format Permissions | Defines default Markdown + frontmatter and permitted non-Markdown ledger formats. |
| 47 | P-STD-002E | P-STD-002-CLAUSE-046 | Ledger Schema Requirements | Defines baseline ledger schema plus concrete extensibility hooks for safe enrichment. |
| 48 | P-STD-002E | P-STD-002-CLAUSE-047 | Placement Rules | Requires deterministic placement and naming per P-STD-004 for status artifacts. |
| 49 | P-STD-002E | P-STD-002-CLAUSE-048 | Update Sequence | Requires ledger-first updates and defines derivation expectations for narratives. |
| 50 | P-STD-002E | P-STD-002-CLAUSE-049 | Drift Prevention Contract | Defines how authority + sequence prevents drift and what to do when drift occurs. |
| 51 | P-STD-002E | P-STD-002-CLAUSE-050 | Schema Versioning and Adoption | Defines schema versioning and forward-only adoption requirements. |
| 52 | P-STD-002E | P-STD-002-CLAUSE-051 | Execution Reference Schema (Optional) | Defines optional execution reference entries that are evidence-bearing, not status-bearing. |
| 53 | P-STD-002E | P-STD-002-CLAUSE-052 | Aggregation Policy Field | Defines how aggregation policy is represented in the ledger schema. |
| 54 | P-STD-002E | P-STD-002-CLAUSE-053 | Execution Posture Fields (Optional) | Defines optional fields capturing sandbox/approval posture without status vocabulary drift. |
| 55 | P-STD-002E | P-STD-002-CLAUSE-054 | Minimum Viable Audit Trail (MVAT) | Defines the minimum required fields per status entry for traceability integrity. |
| 56 | General | P-STD-002-CLAUSE-056 | Status Enum Casing Convention | Requires all canonical status values to use `lowercase_underscore` format. Non-lifecycle enums SHOULD adopt consistent casing within their governing artifact. |


### General Provisions

1) **P-STD-002-CLAUSE-055 (Forward-Only Adoption)**

   P-STD-002 requirements MUST be adopted forward-only from the standard's effective date, per `P-ASSUM-001` (Forward-only Adoption):
   - existing artifacts are not required to retroactively conform
   - conformance applies at the next status update or artifact creation event

2) **P-STD-002-CLAUSE-056 (Status Enum Casing Convention)**

   All canonical status values defined in `P-STD-002-CLAUSE-001` MUST be encoded in `lowercase_underscore` format (e.g., `on_hold`, `in_progress`, `deferred`).

   Non-lifecycle enums (e.g., gate verdicts, client decisions) defined outside `P-STD-002` are not governed by this CLAUSE but SHOULD adopt a consistent casing convention within their own governing artifact.

   This convention applies forward-only per `P-STD-002-CLAUSE-055`.

### P-STD-002A — Status Vocabulary

2) **P-STD-002-CLAUSE-001 (Canonical Status Vocabulary)**

   Program status values MUST be one of the following eight canonical states:
   - `planned`
   - `ready`
   - `in_progress`
   - `blocked`
   - `on_hold`
   - `deferred`
   - `completed`
   - `cancelled`

   * **P-STD-002-CLAUSE-001A (Definitions)** — Canonical state definitions at program scope:
     - `planned`: work is identified but not yet ready to start.
     - `ready`: prerequisites satisfied; work may start immediately.
     - `in_progress`: active work is underway.
     - `blocked`: progress cannot continue due to an impediment not yet resolved.
     - `on_hold`: work is deliberately paused due to a policy or decision (not an unmet prerequisite).
     - `deferred`: work is intentionally postponed beyond the current scope or cycle. May be resumed in a future scope.
     - `completed`: work is finished and accepted.
     - `cancelled`: work is intentionally terminated and will not be completed.

3) **P-STD-002-CLAUSE-002 (Tool Meta-Category Mapping)**

   Any artifact that uses program status values MUST support a deterministic mapping to tool meta-categories:
   - **To Do**: `planned`, `ready`, `deferred`
   - **In Progress**: `in_progress`, `blocked`, `on_hold`
   - **Done**: `completed`, `cancelled`

4) **P-STD-002-CLAUSE-003 (Local Status Extension Mapping)**

   Initiatives MAY define local status values in addition to the canonical eight, but:
   - local statuses MUST map to exactly one canonical status for program roll-ups, and
   - local statuses MUST NOT redefine the semantics of any canonical status.

5) **P-STD-002-CLAUSE-004 (Initial and Terminal States)**

   - `planned` MUST be treated as the initial state.
   - `deferred` MUST be treated as a non-terminal, non-initial state. Deferred work may be resumed via `ready` or cancelled.
   - `completed` and `cancelled` MUST be treated as terminal states.

6) **P-STD-002-CLAUSE-005 (Transition Matrix)**

   The canonical status vocabulary MUST be governed as a state machine using the transition matrix below.

   Legend:
   - `D` = DISALLOWED
   - `A(Gx)` = ALLOWED with minimum guard `Gx`
   - `*` suffix = evidence-required
   - `^` suffix = role-restricted

   | From \\ To | `planned` | `ready` | `in_progress` | `blocked` | `on_hold` | `deferred` | `completed` | `cancelled` |
   |:--|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
   | `planned` | D | A(G1) | D | D | D | A(G10) | D | A^*(G7) |
   | `ready` | D | D | A(G2) | D | A(G5) | A(G10) | D | A^*(G7) |
   | `in_progress` | D | D | D | A(G3) | A(G5) | A(G10) | A^*(G8) | A^*(G7) |
   | `blocked` | D | D | A*(G4) | D | A(G5) | A(G10) | D | A^*(G7) |
   | `on_hold` | D | A(G6) | D | D | D | A(G10) | D | A^*(G7) |
   | `deferred` | D | A(G10) | D | D | D | D | D | A^*(G7) |
   | `completed` | D | D | A^*(G9) | D | D | D | D | D |
   | `cancelled` | D | D | A^*(G9) | D | D | D | D | D |

7) **P-STD-002-CLAUSE-006 (Guard Conditions)**

   Allowed transitions MUST satisfy the minimum guard conditions defined below.

   | Guard ID | Guard Condition (minimum) | Evidence Required? | Role Restricted? |
   |:--|:--|:--:|:--:|
   | `G1` | Definition-of-ready satisfied (local checklist or equivalent) | No | No |
   | `G2` | Owner assigned + start “as_of” recorded | No | No |
   | `G3` | Blocker recorded (dependency ID or evidence pointer) | No | No |
   | `G4` | Blocker cleared + resolution evidence pointer | Yes | No |
   | `G5` | Explicit pause decision + hold reason + next review date | No | No |
   | `G6` | Resume criteria set + next action identified | No | No |
   | `G7` | Cancellation reason + decision evidence pointer | Yes | Yes |
   | `G8` | Completion evidence pointer(s) + acceptance confirmation | Yes | Yes |
   | `G9` | Reopen rationale + new plan/work item reference + approval evidence pointer | Yes | Yes |
   | `G10` | Deferral decision + target scope/cycle reference + next review date | No | No |

   * **P-STD-002-CLAUSE-006A (Role restriction semantics)** — When a guard is role restricted, it MUST use generic RACI labels (e.g., “Accountable”) and MUST NOT name specific program roles.

8) **P-STD-002-CLAUSE-007 (Evidence-Required Transitions)**

   Any transition marked as evidence-required (`*`) in `P-STD-002-CLAUSE-005` MUST include evidence pointers conforming to `P-STD-002-CLAUSE-030` and MUST satisfy validation rules in `P-STD-002-CLAUSE-033`.

9) **P-STD-002-CLAUSE-008 (Role-Restricted Transitions)**

   Any transition marked as role-restricted (`^`) in `P-STD-002-CLAUSE-005` MUST be executed only by the **Accountable** role (generic RACI), or by a delegate explicitly authorized by the Accountable role and recorded via evidence.

10) **P-STD-002-CLAUSE-009 (Blocked vs On-Hold vs Deferred Semantics)**

   - `blocked` MUST indicate an unmet prerequisite or external impediment that prevents progress.
   - `on_hold` MUST indicate an intentional pause due to a decision or policy, not an unmet prerequisite.
   - `deferred` MUST indicate an intentional postponement to a future scope or cycle, not a temporary pause within the current scope. `deferred` is distinct from `on_hold` in that deferred work is moved to a future cycle, while on-hold work is expected to resume in the current cycle.

   `blocked` MAY be encoded either:
   - as the program status value `blocked`, or
   - as an attribute/flag on `in_progress` (provided the artifact still maps deterministically to the canonical vocabulary per `P-STD-002-CLAUSE-003`).

11) **P-STD-002-CLAUSE-010 (Execution Posture Fields (Non-Status))**

   Tool execution state MUST NOT be added to the canonical program status vocabulary.

   If an artifact records tool execution context, it MUST do so using non-status metadata fields, such as:
   - `approval_policy`
   - `sandbox_mode`
   - `execution_platform` (e.g., `github_actions`, `gitlab_ci`, `local`)

12) **P-STD-002-CLAUSE-011 (Manual Gate Crosswalk (Informative))**

   When mapping automated/manual gating states to program status, implementers SHOULD map by cause:

   | Gate / Wait Condition | Program Status (Recommended) | Rationale |
   |:--|:--|:--|
   | Waiting for policy approval / manual review | `on_hold` | Deliberate pause pending a decision |
   | Waiting for unmet prerequisite (missing input, dependency unresolved) | `blocked` | Progress prevented by an impediment |
   | Manual gate required by process (e.g., release sign-off stage) | `on_hold` | Pause is intentional, not a blocker |

### P-STD-002B — Health Assessment

13) **P-STD-002-CLAUSE-012 (Standard Health Dimensions)**

   Program health reporting MUST include the following dimensions:
   - `time`
   - `cost`
   - `scope`
   - `quality`
   - `risk`
   - `benefits`

   The `benefits` dimension is required at program roll-up scope. At initiative scope, `benefits` MAY be deferred when benefits are not yet measurable, but the deferral MUST be explicitly recorded (e.g., `benefits: unassessed` with a reason and next review date).

14) **P-STD-002-CLAUSE-013 (RAG Threshold Method)**

   Each health dimension MUST be assessed using a tolerance-based hybrid method:
   - Green: within tolerance
   - Amber: near tolerance limit or adverse trend indicates likely breach without intervention
   - Red: tolerance breached, or highly likely to breach absent intervention

15) **P-STD-002-CLAUSE-014 (Dimension-Level RAG Computation)**

   Each dimension’s RAG MUST be computed independently against the tolerance definition for that dimension.

16) **P-STD-002-CLAUSE-015 (Overall RAG Aggregation)**

   Overall health RAG MUST be derived deterministically from the dimension RAGs:
   - if any dimension is Red, overall MUST be Red
   - else if two or more dimensions are Amber, overall MUST be Amber
   - else overall MUST be Green

17) **P-STD-002-CLAUSE-016 (Initiative Configuration)**

   Initiatives MAY configure numeric tolerance values per dimension. The standard requires that tolerances are defined, not what the exact numeric bands are.

   Initiatives MAY add optional health dimensions, provided:
   - the additional dimensions use the same computation method (`P-STD-002-CLAUSE-013` through `P-STD-002-CLAUSE-015`), and
   - the added dimensions do not replace or rename the required dimensions (`P-STD-002-CLAUSE-012`).

18) **P-STD-002-CLAUSE-017 (Health Assessment Cadence)**

   Health MUST be reassessed at least:
   - on any transition into `ready` or `in_progress`, and
   - when entering `blocked` or `on_hold`, and
   - on any transition into a terminal state.

19) **P-STD-002-CLAUSE-018 (Allowed-Failure Health Impact)**

   When status updates rely on an evidence set using aggregation policy `allow_failure` or `continue_on_error`, the health report MUST reflect that semantics.

   At minimum:
   - overall health MUST NOT be Green if any evidence item failed but was treated as “allowed failure” for completion, and
   - the health report MUST mark either `quality` or `risk` as Amber/Red, with a brief rationale.

### P-STD-002C — Dependency Visibility

20) **P-STD-002-CLAUSE-019 (Dependency Edge Schema)**

   Dependency visibility MUST be representable as a graph of dependency edges. Each dependency edge MUST include:
   - `from_id` (the upstream/blocker entity ID)
   - `to_id` (the downstream/blocked entity ID)
   - `relationship` (per `P-STD-002-CLAUSE-020`)
   - `category` (per `P-STD-002-CLAUSE-021`)
   - `criticality` (per `P-STD-002-CLAUSE-022`)
   - `owner` (resolution owner; the party who can unblock)
   - `status` (per `P-STD-002-CLAUSE-023`)
   - `evidence` (0+ evidence pointers per `P-STD-002-CLAUSE-030`)

21) **P-STD-002-CLAUSE-020 (Relationship Semantics)**

   The dependency `relationship` MUST be one of:
   - `depends_on`: `to_id` cannot be completed unless `from_id` is satisfied
   - `blocks`: `from_id` directly blocks progress on `to_id`

22) **P-STD-002-CLAUSE-021 (Category Taxonomy)**

   Dependency `category` MUST include at least:
   - `internal`
   - `external`

   Additional categories MAY be used if they do not change the meaning of the minimum set.

23) **P-STD-002-CLAUSE-022 (Criticality Classification)**

   Dependency `criticality` MUST be one of:
   - `critical`
   - `near_critical`
   - `non_critical`

24) **P-STD-002-CLAUSE-023 (Dependency Status Enum)**

   Dependency `status` MUST use a dependency-specific lifecycle enum distinct from program status:
   - `open`
   - `at_risk`
   - `resolved`

25) **P-STD-002-CLAUSE-024 (Optional Schedule Enrichment)**

   Dependencies MAY include optional schedule semantics:
   - `schedule_relation`: one of `FS`, `SS`, `FF`, `SF`
   - `lag`: optional duration/offset value

26) **P-STD-002-CLAUSE-025 (Cross-Initiative Interface Contract)**

   For program reporting, every initiative that publishes dependencies MUST expose a cross-initiative interface that includes, at minimum, the fields required by `P-STD-002-CLAUSE-019`.

27) **P-STD-002-CLAUSE-026 (Conformance Rule)**

   If an initiative uses a local dependency model, it MUST provide a lossless mapping to the program dependency interface in `P-STD-002-CLAUSE-025`.

28) **P-STD-002-CLAUSE-027 (Roll-Up View Requirement)**

   Program status reporting MUST surface a roll-up view of cross-initiative dependencies, including:
   - open critical dependencies, and
   - at-risk dependencies, and
   - the resolution owner per dependency edge.

29) **P-STD-002-CLAUSE-028 (Orchestration Reference Fields (Optional))**

   Dependency edges MAY include optional orchestration reference fields when a dependency is materialized as a CI/CD job or automated run, such as:
   - `platform`
   - `run_id` / `pipeline_id`
   - job/step identifiers

30) **P-STD-002-CLAUSE-029 (Category Extension Examples (Informative))**

   Example non-binding dependency categories include:
   - `orchestration`
   - `pipeline_gate`
   - `agent_handoff`

### P-STD-002D — Update Protocol

31) **P-STD-002-CLAUSE-030 (Evidence Pointer Schema)**

   Status updates MUST reference evidence using an `evidence[]` array of entries. Each evidence entry MUST include:
   - `type` (per `P-STD-002-CLAUSE-031`)
   - `ref` (repo-relative path, stable ID, or URL)
   - `date` (ISO-8601 `YYYY-MM-DD`)
   - `by` (actor identifier)
   - `summary` (1-line description)

32) **P-STD-002-CLAUSE-031 (Evidence Type Taxonomy)**

   Evidence `type` MUST be one of the baseline types:
   - `note`
   - `pr`
   - `build`
   - `test_result`
   - `decision`
   - `session`
   - `sign_off`

33) **P-STD-002-CLAUSE-032 (Evidence Requirements by Transition)**

   Evidence MUST be provided for:
   - any transition into `completed` (guard `G8`)
   - any transition into `cancelled` (guard `G7`)
   - any transition from `completed` or `cancelled` into `in_progress` (guard `G9`)

34) **P-STD-002-CLAUSE-033 (Evidence Validation Rules)**

   Evidence validation MUST be performed for any evidence-required transition.

   At minimum:
   - evidence `ref` MUST resolve to an accessible artifact (path/URL/ID), and
   - evidence `date` MUST be valid ISO-8601 date format, and
   - evidence `by` MUST be present, and
   - evidence `summary` MUST be non-empty.

35) **P-STD-002-CLAUSE-034 (Role Accountability Model)**

   The program update protocol MUST use a hybrid accountability model:
   - routine status updates MUST be attributed (record `updated_by`, `last_updated`)
   - high-impact transitions (terminal or reopen) MUST be role-restricted per `P-STD-002-CLAUSE-035`

36) **P-STD-002-CLAUSE-035 (Role-Transition Matrix)**

   Transition permissions MUST be expressed in generic RACI labels and MUST NOT name specific roles.

   Minimum requirements:
   - the **Responsible** role MAY execute routine non-terminal transitions when guards are satisfied
   - the **Accountable** role MUST execute terminal transitions and reopen transitions

37) **P-STD-002-CLAUSE-036 (Update Attribution Fields)**

   Every status update record MUST include:
   - `updated_by`
   - `last_updated` (timestamp or date-time)

38) **P-STD-002-CLAUSE-037 (Conflict Resolution)**

   When conflicting updates occur:
   - the artifact MUST retain the most recent update as authoritative, and
   - disputes MUST be escalated to the Accountable role for resolution, with decision evidence recorded.

39) **P-STD-002-CLAUSE-038 (Stale-State Governance)**

   Status entries in active non-terminal states (`ready`, `in_progress`, `blocked`, `on_hold`, `deferred`) MUST be reviewed for staleness using the `last_updated` field.

   Minimum stale-state thresholds:
   - `ready`: 7 calendar days without update
   - `in_progress`: 7 calendar days without update
   - `blocked`: 3 calendar days without update
   - `on_hold`: 14 calendar days without update
   - `deferred`: 30 calendar days without re-evaluation

   Stale-state review MUST run on a recurring schedule of at least once every 7 calendar days.

   When an entry is detected as stale:
   - the Responsible and Accountable roles MUST be notified;
   - the item MUST be reviewed and either refreshed, confirmed with an exception note, or transitioned to a more accurate state; and
   - if the stale condition remains unresolved through the next review interval, the Accountable role MUST record a resolution decision.

   Stale-state detection MUST NOT by itself force an automatic status transition in the baseline program implementation.

   This CLAUSE supplements transition-based health reassessment in `P-STD-002-CLAUSE-017`; it does not replace it.

40) **P-STD-002-CLAUSE-039 (Repo-Verifiable Evidence Requirement)**

   Terminal transitions MUST cite at least one repo-verifiable evidence pointer (or equivalent for non-repo environments).

   Primary recommendation (when available): checks-style evidence (e.g., GitHub Checks).

   Permitted platform-agnostic alternatives (first-class, not footnotes):
   - commit status evidence
   - CI/CD pipeline or workflow run evidence
   - PR/MR merge evidence
   - commit SHA evidence (when coupled to a verifiable build/test record)

41) **P-STD-002-CLAUSE-040 (Evidence Type Extensions)**

   Evidence `type` MAY be extended with:
   - `check`
   - `workflow_run`
   - `execution_trace`

42) **P-STD-002-CLAUSE-041 (Aggregation Policy Declaration)**

   When a status update references multiple evidence items that must be considered together (nested/parallel evidence), the update MUST declare an aggregation policy:
   - `fail_fast`
   - `allow_failure`
   - `continue_on_error`
   - `manual_gate`

   Informative definitions:

   | Mode | Meaning |
   |:--|:--|
   | `fail_fast` | Any failure causes the aggregated result to be treated as failed. |
   | `allow_failure` | Some failures are permitted if explicitly flagged and justified. |
   | `continue_on_error` | Execution continues despite failures; completion requires explicit exception rationale. |
   | `manual_gate` | Evidence completion depends on an explicit approval decision outside automation. |

43) **P-STD-002-CLAUSE-042 (Silent Allowed-Failure Prohibition)**

   A transition into `completed` MUST NOT rely on an evidence set containing allowed failures unless:
   - the allowed failure(s) are explicitly identified, and
   - an exception rationale is recorded, and
   - health impact is reflected per `P-STD-002-CLAUSE-018`.

### P-STD-002E — Status Artifact

44) **P-STD-002-CLAUSE-043 (Artifact Set Definition)**

   Program status reporting MUST be representable as:
   - a canonical structured ledger artifact, and
   - a derived human-readable narrative artifact.

   A changelog MAY be maintained, but this standard does not prescribe its location in v1 (separate file vs embedded appendix).

   Narrative structure SHOULD use consistent sections (recommended, not required), such as:
   - Summary
   - Status
   - Health
   - Dependencies
   - Evidence
   - Next Actions

45) **P-STD-002-CLAUSE-044 (Authority Hierarchy)**

   The structured ledger MUST be treated as canonical. If the ledger and narrative disagree, the ledger MUST be treated as the source of truth and the narrative MUST be corrected.

46) **P-STD-002-CLAUSE-045 (Format Permissions)**

   The default narrative format SHOULD be Markdown (`.md`) with YAML frontmatter where appropriate.

   The ledger MAY be authored as non-Markdown (e.g., `.yaml`, `.json`) when explicitly permitted by this standard, consistent with `P-CON-003(B)` (Artifact Format Governance).

47) **P-STD-002-CLAUSE-046 (Ledger Schema Requirements)**

   The ledger MUST conform to a baseline schema that supports program roll-up without initiative-specific knowledge.

   Baseline schema requirements (illustrative):
   ```yaml
   schema_version: "1.0"
   scope_uid: "<timeline UID or other governed scope UID>"
   status: "<planned|ready|in_progress|blocked|on_hold|deferred|completed|cancelled>"
   as_of: "YYYY-MM-DD"
   updated_by: "<actor>"
   last_updated: "YYYY-MM-DD"
   health:
     overall: "<green|amber|red|unassessed>"
     dimensions:
       time: "<green|amber|red|unassessed>"
       cost: "<green|amber|red|unassessed>"
       scope: "<green|amber|red|unassessed>"
       quality: "<green|amber|red|unassessed>"
       risk: "<green|amber|red|unassessed>"
       benefits: "<green|amber|red|unassessed>"
   dependencies: []  # list of edges (see P-STD-002C)
   evidence: []      # list of evidence pointers (see P-STD-002D)
   aggregation_policy: "<fail_fast|allow_failure|continue_on_error|manual_gate>"  # optional
   execution_refs: []  # optional (see P-STD-002-CLAUSE-051)
   extensions: {}      # extensibility hook (see below)
   ```

   Extensibility hooks (concrete mechanism):
   - Baseline fields MUST NOT be removed, renamed, or have their semantics overridden.
   - Extensions MUST be stored under `extensions` or in additional fields prefixed with `x_`.
   - Extension keys MUST NOT duplicate any baseline field name.
   - Extensions MAY add extra fields inside structured items (e.g., evidence entries), but added fields MUST be prefixed with `x_`.

48) **P-STD-002-CLAUSE-047 (Placement Rules)**

   Status artifacts MUST be placed and named deterministically in accordance with `P-STD-004` (File Naming & Directory Convention).

49) **P-STD-002-CLAUSE-048 (Update Sequence)**

   Updates MUST be ledger-first:
   1. Update the ledger (canonical).
   2. Update/derive the narrative from the ledger (derived).

50) **P-STD-002-CLAUSE-049 (Drift Prevention Contract)**

   The authority hierarchy (`P-STD-002-CLAUSE-044`) and update sequence (`P-STD-002-CLAUSE-048`) together form the drift prevention contract. Any drift MUST be resolved by correcting the narrative to match the ledger.

51) **P-STD-002-CLAUSE-050 (Schema Versioning and Adoption)**

   The ledger MUST include a `schema_version` field.

   Adoption MUST be forward-only:
   - new or updated status entries MUST conform to the current schema version
   - legacy entries MAY remain in legacy shape until next-touch, provided they remain mappable to the baseline interface

52) **P-STD-002-CLAUSE-051 (Execution Reference Schema (Optional))**

   The ledger MAY include optional execution references. Execution references are evidence-bearing, not status-bearing.

   Example execution reference fields:
   - `platform`
   - `run_id`
   - `check_run_id`
   - `url`
   - `status`
   - `conclusion`
   - `started_at`
   - `completed_at`

53) **P-STD-002-CLAUSE-052 (Aggregation Policy Field)**

   When aggregation policy applies, the ledger MUST represent it as `aggregation_policy` using one of the values defined in `P-STD-002-CLAUSE-041`.

54) **P-STD-002-CLAUSE-053 (Execution Posture Fields (Optional))**

   The ledger MAY include non-status execution posture fields such as:
   - `approval_policy`
   - `sandbox_mode`

   These fields MUST NOT introduce new status values and MUST NOT be used as substitutes for the canonical program status vocabulary.

55) **P-STD-002-CLAUSE-054 (Minimum Viable Audit Trail (MVAT))**

   Every status entry MUST include, at minimum:
   - a canonical program status value (`P-STD-002-CLAUSE-001`)
   - `as_of`
   - `updated_by` and `last_updated`
   - 0+ evidence pointers, and for evidence-required transitions at least 1 evidence pointer (`P-STD-002-CLAUSE-032`)
   - aggregation policy when required (`P-STD-002-CLAUSE-041`)
   - sufficient health reporting to support program roll-up (`P-STD-002-CLAUSE-012`)

## Decision Record

| ADR ID | Title | Status | Supersedes | Date |
|:--|:--|:--|:--|:--|
| `P-STD-002-ADR-001` | P-STD-002 v1 Authoring Decisions | `draft` | — | 2026-02-27 |

* **P-STD-002-ADR-001 (P-STD-002 v1 Authoring Decisions)** {#p-std-002-adr-001-p-std-002-v1-authoring-decisions}

  * **Context**
    `P-STD-002` is authored as a program-wide status governance standard to unify status vocabulary, transitions, health assessment, dependency visibility, evidence linkage, and status artifact schema across `prompt/artifacts/tasks/**`.

    This standard is authored using the combined standard-specification model governed by `P-STD-001`.

    Inputs:
    - P-RES-001 integration recommendations (baseline coverage across domains A–E)
    - P-RES-002 integration recommendations (evidence anchoring, execution references, aggregation policy)
    - Consolidated Decision Register (CDR) confirmations (14 binding decisions, including the deferred-state amendment) in `proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md`

    CDR numbering note:
    - “CDR-03 (7-state vocabulary stability)” was not elevated to a binding client-facing decision because both research streams independently confirmed the 7-state vocabulary before the consolidated register was assembled. It is recorded as a non-CDR confirmation in the CDR proposal preamble. The numbering gap (CDR-02 → CDR-04) is intentional.
    - The deferred-state amendment is captured separately as CDR-15 after the original 13 binding decisions.

  * **Decision**
    `P-STD-002` adopts the confirmed 14 binding CDR decisions as normative inputs:
    - CDR-01: keep tool execution states out of the 8-state vocabulary; record as non-status fields.
    - CDR-02: disallow `planned` → `in_progress` direct transition (must go through `ready`).
    - CDR-04: use generic RACI labels, not named program roles, for role restrictions.
    - CDR-05: map “manual gate / waiting approval” by cause to `on_hold` vs `blocked`.
    - CDR-06: dependency edge `owner` means resolution owner.
    - CDR-07: use separate 3-state dependency status enum.
    - CDR-08: numeric tolerance bands are initiative-configured; the standard requires definition, not fixed percentages.
    - CDR-09: evidence validation is normative (see `P-STD-002-CLAUSE-033`); checks-style evidence is the primary recommendation with commit status as a first-class fallback (see `P-STD-002-CLAUSE-039`).
    - CDR-10: aggregation policy declaration is required for multi-evidence updates (see `P-STD-002-CLAUSE-041`).
    - CDR-11: ledger schema is normative with extensibility hooks.
    - CDR-12: `benefits` is required at program roll-up; may be deferred at initiative level with explicit recording.
    - CDR-13: narrative artifact has recommended sections, not a fixed required template (see `P-STD-002-CLAUSE-043`).
    - CDR-14: changelog location is not prescribed in v1.
    - CDR-15: add `deferred` as 8th canonical state, semantically distinct from `on_hold`; map to "To Do" meta-category; 30-day staleness threshold; add CLAUSE-056 casing convention for status enums.

  * **Alternatives**
    - Reduce to a 3-state vocabulary with attributes (`todo/in_progress/done` + flags) — rejected; loses governance precision.
    - Extend the program status vocabulary with tool execution states — rejected; creates vocabulary drift and vendor coupling.
    - Make evidence linkage informative-only — rejected; undermines traceability integrity requirements.

  * **Consequences**
    (+) Establishes deterministic, portable governance for program status and evidence linkage.
    (+) Enables cross-initiative roll-ups (health + dependencies) without initiative-specific schemas.
    (±) Requires explicit mapping for any local extension statuses and local dependency models.
    (-) Introduces additional authoring burden (evidence pointers + aggregation policy) for terminal transitions.

    Risk mitigation traceability:

    | Risk | Source | Mitigation |
    |:--|:--|:--|
    | P-RES-001-RISK-001 (overfitting to one tool) | P-RES-001 | Generic RACI labels (CDR-04) + platform-agnostic evidence fallbacks (CDR-09) |
    | P-RES-001-RISK-002 (narrative/ledger drift) | P-RES-001 | Ledger authority + update sequence + drift prevention contract (P-STD-002E) |
    | P-RES-002-RISK-001 (Checks-only portability) | P-RES-002 | Commit-status fallback + platform-agnostic evidence pointer schema (P-STD-002D) |
    | P-RES-002-RISK-002 (silent allowed failures) | P-RES-002 | Aggregation policy required + allowed-failure health impact + prohibition on silent completion |

  * **Traceability**
    - `P-PH000-ST001-AC003-TK001` (CDR proposal + theme mapping)
    - `P-PH000-ST001-AC003-TK002` (author Specification)
    - `P-PH000-ST001-AC003-TK003` (author ADR-001)
    - `P-PH000-ST001-AC003-TK013` (deferred-state + casing convention amendment)
    - `P-PH000-ST004-AC001-TK003` (P-RES-001 integration recommendations)
    - `P-PH000-ST004-AC002-TK003` (P-RES-002 integration recommendations)

## References

### Normative References
| ID | Title | Scope | Source Path |
|:--|:--|:--|:--|
| P-STD-001 | Program Governance Standard | Program (P) | `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md` |
| P-STD-004 | File Naming & Directory Convention | Program (P) | `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md` |
| P-STD-005 | Universal ID Specification | Program (P) | `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md` |

### Informative References
| ID | Title | Scope | Source Path |
|:--|:--|:--|:--|
| P-SPS | Program SPS | Program (P) | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |
| P-RES-001 | Status Standard Research | Program (P) | `prompt/artifacts/tasks/P/research/P-RES-001/report_P-RES-001_status-standard-research.md` |
| P-RES-002 | Agentic Status Systems Research | Program (P) | `prompt/artifacts/tasks/P/research/P-RES-002/report_P-RES-002_agentic-status-research.md` |
| CDR Proposal | AC003 TK001 CDR Resolution Proposal | Program (P) | `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md` |

## Provenance

### Status
| Field | Value |
|:--|:--|
| Current lifecycle posture | `accepted` |
| Approved | `2026-03-04` |
| Effective | `2026-03-04` |

### Lineage / Authority
| Field | Value |
|:--|:--|
| Governing activity plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md` |
| Approval surface | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-001_gir-disposition-package.md` |
| Approval surface | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-003_execution-disposition-package.md` |
| Approval surface | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/proposal/proposal_P-PH000-ST001-AC003-GATE-004_amendment-disposition-package.md` |

### Amendment History
> Full version history: `prompt/artifacts/tasks/P/standard/changelog/changelog_standard_P-STD-002.md`

### Input Sources
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC003/plan_P-PH000-ST001-AC003.md`
- `prompt/artifacts/tasks/P/research/P-RES-001/report_P-RES-001_status-standard-research.md`
- `prompt/artifacts/tasks/P/research/P-RES-002/report_P-RES-002_agentic-status-research.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/proposal/proposal_P-PH000-ST001-AC003-TK001_cdr-resolution.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/analysis/analysis_P-PH000-ST001-AC010-TK000_execution-readiness-assessment.md`
- `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC010/implementation/implementation_P-PH000-ST001-AC010_cross-standard-metadata-retrofit-task-specification.md`
