---
artifact_type: 'PROPOSAL'
initiative_id: '[ID]'
epic_id: '[ID]'
epic_code: '[CODE]'
phase: '[#]'
version: '1.0.0'
date: 'YYYY-MM-DD'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: '[path to plan file]'
analysis_reference: '[path to analysis file]'
target_document: '[path to SPS/Concept file to be updated]'
target_section: '[e.g., III.C.2 (Epic: T102B)]'
---

# PHASE [#] PROPOSAL: [Epic ID] ([Epic Code]) — [Phase Title]

<!--
PURPOSE: PROPOSAL files serve as the dynamic workspace for E-ID development during consultancy phases.
They use a "working index → full bodies" pattern where Section II tracks all candidate IDs with status,
and Sections III-V contain full normative specification bodies for approved candidates.

WORKFLOW:
1. LLM_Consultant populates Section II (Candidate Inventory) during consultancy dialogue
2. As IDs gain client approval, status changes from "proposed" to "existing" or "rejected"
3. Full normative bodies are written in Sections III-V only for approved IDs (status="proposed" or "existing")
4. Upon phase completion and Gate approval, approved E-IDs are promoted to target SSOT (SPS/Concept)
5. PROPOSAL becomes archival record of phase deliberation and decisions

GOVERNANCE:
- All IDs must comply with T102-ADR-005 (ID Specification)
- All DRs must comply with T102-ADR-004 (Decision Records Index)
- All Issues/Risks must comply with T102-ADR-007 (Issues & Risks Index)
- All RES/NOTE-IDs must comply with T102-ADR-006 (Other IDs)
-->

## I. EXECUTIVE SUMMARY

**Proposal Purpose**: [What this proposal achieves in 1-2 sentences. Example: "Define governance framework and roadmap for Task T102B epic, establishing decision authority, workflow rules, and phase 1 deliverables."]

**Target Document**: `[target_document]`
<!-- Example: `prompt/artifacts/tasks/T102/consultant/sps/sps_T102-CONSULTANT.md` -->

**Target Section**: [target_section]
<!-- Example: §III.C.2 (Epic: T102B) — Governance & Roadmap Framework -->

**Research Foundation**: This proposal is informed by:
<!-- List all RES-IDs that informed this proposal with verdict/summary -->
- `[RES-ID]` ([Title]) — [Verdict/Summary in 1 line]
<!-- Example: `T102B-RES-001` (Request Artifact Analysis) — Confirmed need for versioning and status tracking in Request artifacts -->

**Phase Context**: [How this proposal relates to the phase plan. Example: "This is Phase 0 (Foundation) per plan_T102B_phase0.md. Establishes E-GDRs and E-RIDs needed before workflow implementation can begin."]

**Status**: [Draft / Under Review / Approved]

---

## II. CANDIDATE INVENTORY (WORKING INDEX)
<!--
PURPOSE: Single master index of all proposed IDs across categories. Status determines whether full body is written in Sections III-V.
Use this as the master checklist during consultancy dialogue.

STATUS VALUES:
- "proposed" = New ID presented to client for review; full body written in §III-V
- "existing" = ID already in SSOT; being reviewed/modified; full body in §III-V shows updates
- "rejected" = Client declined; no body written; retained for decision log context
- "deferred" = Postponed to later phase; no body written; tracked for future consideration

BODY REF CONVENTION:
- Reference the section where full body appears (e.g., "§III.A", "§IV.B")
- If no body written (rejected/deferred), leave blank or write "—"
-->

### A. E-RID Candidates
<!--
PURPOSE: Epic-level requirements following T102-ADR-005 ID specification.
All E-RIDs use format: [EPIC_CODE]-[CATEGORY]-[###]

ID CATEGORIES (per T102-ADR-005):
- ASSUM: Assumptions (factors believed true but not confirmed)
- CON: Constraints (non-negotiable boundaries)
- QG: Quality Goals (measurable success criteria)
- DEP: Dependencies (external prerequisites)
- IF: Interfaces (role/process/data touchpoints)
- IG: Implementation Guidance (patterns and conventions)

Example ID: T102B-ASSUM-001, T801A-CON-002, T103-QG-001
-->

#### A.1 Assumptions ([EPIC_CODE]-ASSUM-###)
<!--
PURPOSE: Factors believed to be true but not yet confirmed. Can be adjustable but carry risk.
Per BABOK v3 and ISO 29148, assumptions are working hypotheses that enable progress but require validation.

EXAMPLES:
- "Client has decision authority to approve GDRs"
- "Existing SPS structure can accommodate epic-level sections"
- "LLM_Consultant can identify all E-IDs during phase 0"
-->
| ID | Title | 1-line Summary | Source | Status | Body Ref |
|:---|:------|:---------------|:-------|:-------|:---------|
| [ASSUM-001] | [Title] | [Summary] | [RES-ID or existing] | [proposed/existing/rejected] | [§III.A if written] |

---

#### A.2 Constraints ([EPIC_CODE]-CON-###)
<!--
PURPOSE: Non-negotiable restrictions or limitations on possible solutions.
Per ISO 29148, these are boundaries that must be respected (e.g., regulatory, technical, resource limits).

EXAMPLES:
- "Must not break existing I-RID/S-RID references"
- "All governance changes require client approval"
- "Cannot introduce new file formats without tooling support"
-->
| ID | Title | 1-line Summary | Source | Status | Body Ref |
|:---|:------|:---------------|:-------|:-------|:---------|

---

#### A.3 Quality Goals ([EPIC_CODE]-QG-###)
<!--
PURPOSE: Measurable targets that define success.
Per ISO 29148, must be verifiable (testable), singular (one goal per ID), and complete (success threshold defined).

EXAMPLES:
- "All E-GDRs trackable via index table (verifiable: count table rows)"
- "Decision log entries reference RIDs (verifiable: grep for ID patterns)"
- "Client can locate any GDR in <30 seconds (verifiable: timed test)"
-->
| ID | Title | 1-line Summary | Source | Status | Body Ref |
|:---|:------|:---------------|:-------|:-------|:---------|

---

#### A.4 Dependencies ([EPIC_CODE]-DEP-###)
<!--
PURPOSE: External prerequisites and commitments this epic relies on.
Per ISO 29148 and BABOK v3, dependencies are external to the epic but required for success.

EXAMPLES:
- "Requires T102-ADR-004 governance rules (dependency on initiative-level standard)"
- "Requires client availability for Gate approval (dependency on stakeholder)"
- "Requires Python 3.8+ for skill scripts (dependency on infrastructure)"
-->
| ID | Title | 1-line Summary | Source | Status | Body Ref |
|:---|:------|:---------------|:-------|:-------|:---------|

---

#### A.5 Interfaces ([EPIC_CODE]-IF-###)
<!--
PURPOSE: Governance-level role/process touchpoints and data contracts.
Per ISO 29148, interfaces define how this epic interacts with external systems, roles, or processes.

EXAMPLES:
- "Gate Approval Interface: Client reviews/approves E-GDRs"
- "SSOT Update Interface: E-IDs promoted to SPS §III.C.2"
- "Research Interface: RES briefs/reports inform E-RID creation"
-->
| ID | Title | 1-line Summary | Source | Status | Body Ref |
|:---|:------|:---------------|:-------|:-------|:---------|

---

#### A.6 Implementation Guidance ([EPIC_CODE]-IG-###)
<!--
PURPOSE: Epic-specific implementation patterns and technical conventions.
Per ISO 29148, these are non-normative guidelines that aid consistent execution.

EXAMPLES:
- "Use frontmatter YAML for all proposal metadata"
- "Name GDRs using [EPIC]-GDR-[###] format"
- "Store proposal files in consultant/workspace/proposal/[EPIC]/"
-->
| ID | Title | 1-line Summary | Source | Status | Body Ref |
|:---|:------|:---------------|:-------|:-------|:---------|

---

### B. E-DID Candidates (GDR/ADR)
<!--
PURPOSE: Epic-level governance and architectural decisions following T102-ADR-004.

GDR/ADR PAIRING (per T102-ADR-004):
- Every ADR must have exactly one paired GDR
- GDR establishes the governance rule (client-owned policy)
- ADR documents the implementation approach (technical solution)
- GDR is referenced in SPS; ADR stored in Concept (or proposal for phase 0)

NAMING CONVENTION:
- GDR: [EPIC_CODE]-GDR-[###] (e.g., T102B-GDR-001)
- ADR: [EPIC_CODE]-ADR-[###] (e.g., T102B-ADR-001)
-->

#### B.1 Governance Decisions ([EPIC_CODE]-GDR-###)
<!--
PURPOSE: Policy-level decisions that establish epic governance rules and authority. Client-owned.

GDR EXAMPLES:
- "Client must approve all E-GDRs before SSOT promotion"
- "All decision records must include Context/Decision/Consequences sections"
- "GDR index tables are mandatory in SPS artifacts"

GDR STATUS VALUES:
- "Proposed" = Awaiting client approval
- "Accepted" = Client approved; active governance rule
- "Rejected" = Client declined; alternative may be proposed
- "Superseded" = Replaced by newer GDR
-->
| GDR ID | Title | 1-line Summary | Source | Status | Body Ref |
|:-------|:------|:---------------|:-------|:-------|:---------|

---

#### B.2 Architectural Decisions ([EPIC_CODE]-ADR-###)
<!--
PURPOSE: Implementation-level decisions that document solution approach. Paired with GDRs per T102-ADR-004.

ADR EXAMPLES:
- "Implement GDR approval via Gate checklist in §VII" (paired with GDR on approval process)
- "Store GDR index in SPS §IV.A using markdown table format" (paired with GDR on index tables)
- "Use YAML frontmatter for proposal metadata" (paired with GDR on metadata tracking)

CANONICAL LINK CONVENTION:
- Format: [artifact_type]_[epic_code]#[anchor]
- Example: concept_T102B#adr-metadata-tracking
- Points to where ADR body is stored (usually Concept, sometimes Proposal for phase 0)
-->
| ADR ID | Title | Paired GDR | 1-line Summary | Status | Body Ref |
|:-------|:------|:-----------|:----------------|:-------|:---------|

---

### C. E-OID Candidates (Issues/Risks/Research/Notes)
<!--
PURPOSE: Epic-level "Other IDs" following T102-ADR-006 and T102-ADR-007.

OTHER ID CATEGORIES:
- ISSUE: Problems requiring resolution (T102-ADR-007)
- RISK: Potential problems requiring monitoring/mitigation (T102-ADR-007)
- RES: Commissioned research with brief/report pairs (T102-ADR-006)
- NOTE: Lightweight insights ≤200 words (T102-ADR-006-FR-008)
-->

#### C.1 Issues ([EPIC_CODE]-ISSUE-###)
<!--
PURPOSE: Problems requiring resolution. Per T102-ADR-007 schema.

ISSUE EXAMPLES:
- "Unclear if existing SPS structure supports epic-level GDR sections"
- "No tooling exists to validate GDR index table format"
- "Client availability for Gate approval uncertain"

ISSUE STATUS (per T102-ADR-007):
- OPEN: Issue identified, resolution in progress
- RESOLVED: Issue fixed, resolution documented
- DEFERRED: Postponed to later phase
- ESCALATED: Requires external resolution
-->
| ID | Title | 1-line Summary | Priority | Status | Body Ref |
|:---|:------|:---------------|:---------|:-------|:---------|

---

#### C.2 Risks ([EPIC_CODE]-RISK-###)
<!--
PURPOSE: Potential problems requiring monitoring/mitigation. Per T102-ADR-007 schema.

RISK EXAMPLES:
- "Client may reject GDR governance overhead"
- "E-ID proliferation may make SSOT maintenance burdensome"
- "Phase 0 may take longer than estimated, delaying phase 1"

RISK STATUS (per T102-ADR-007):
- MONITORED: Risk identified, being watched
- MITIGATED: Risk addressed, mitigation in place
- ACCEPTED: Risk acknowledged, no action taken
- OCCURRED: Risk materialized, now an Issue
-->
| ID | Title | 1-line Summary | Priority | Status | Body Ref |
|:---|:------|:---------------|:---------|:-------|:---------|

---

#### C.3 Research ([EPIC_CODE]-RES-###)
<!--
PURPOSE: Commissioned research with brief/report pairs. Per T102-ADR-006.

RESEARCH WORKFLOW:
1. Create brief in consultant/research/brief/brief_[ID].md
2. LLM_Researcher produces report in consultant/research/report/report_[ID].md
3. Report verdict/findings inform E-RID/E-DID creation
4. RES-ID tracked in this register with links to brief/report

RESEARCH EXAMPLES:
- RES-001: Analysis of existing Request artifact structure (informs ASSUM/CON)
- RES-002: Investigation of GDR storage location options (informs ADR)
- RES-003: Assessment of client decision authority (informs IF)
-->
| RES ID | Title | 1-line Summary | Status | Brief | Report |
|:-------|:------|:---------------|:-------|:------|:-------|
| [RES-001] | [Title] | [Summary] | [Complete/In Progress] | [path to brief] | [path to report] |

---

#### C.4 Notes ([EPIC_CODE]-NOTE-###)
<!--
PURPOSE: Lightweight insights (≤200 words) per T102-ADR-006-FR-008.
Contextual clarifications, philosophy, industry references, or observations.

NOTE GUIDELINES (per T102-ADR-006-FR-008):
- Keep ≤200 words (promotes concision, avoids duplication)
- Link-don't-duplicate: Reference existing content rather than restating
- Promote to substantive artifact if NOTE grows beyond 200 words
- Extracted from Decision Log when topic warrants persistence

NOTE EXAMPLES:
- "Philosophy: Why we pair GDRs with ADRs (ISO 29148 traceability)"
- "Industry context: BABOK v3 assumption vs. constraint distinction"
- "Observation: Client prefers governance-light approaches based on T102A feedback"
-->
| NOTE ID | Title | 1-line Summary | Source | Status | Body Ref |
|:--------|:------|:---------------|:-------|:-------|:---------|

---

## III. E-RID BODIES (NORMATIVE)
<!--
PURPOSE: Full specification bodies for confirmed E-RIDs from Section II.A.
Only write bodies for IDs with status="proposed" or "existing" (for review).
IDs with status="rejected" or "deferred" have no body.

BODY FORMAT:
- Use bullet list format for concision
- Bold the ID and Title: **[ID] ([Title])**
- Provide complete description including context, rationale, and implications
- Reference source (RES-ID, existing doc, client input)
-->

### A. Assumptions ([EPIC_CODE]-ASSUM-###)
<!--
PURPOSE: Full descriptions of assumptions from §II.A.1.
Include context, implications, adjustability, and validation approach.

EXAMPLE:
* **T102B-ASSUM-001 (Client Decision Authority)**
  We assume the client has authority to approve all E-GDRs proposed in this phase without requiring external stakeholder review. This assumption enables rapid Gate approval at phase boundaries. If invalid, additional stakeholders must be identified, and approval timelines extended. Source: T102B-RES-003 (Initiative Status Assessment). Validation: Confirm with client during first consultancy session.
-->

* **[ID] ([Title])**
  [Full description of the assumption, including context, implications, adjustability, and validation approach. Typically 2-5 sentences.]

---

### B. Constraints ([EPIC_CODE]-CON-###)
<!--
PURPOSE: Full descriptions of constraints from §II.A.2.
Include boundary definition, rationale, and consequences of violation.

EXAMPLE:
* **T102B-CON-001 (No Breaking I-RID References)**
  All governance changes must preserve existing I-RID and S-RID references in the codebase. Breaking these references would invalidate traceability and require extensive rework. This constraint stems from the initiative-level decision to use RIDs as the foundational traceability mechanism (T102-GDR-002). Consequence: E-GDR naming and anchoring must be additive only; no renaming or deletion of existing RIDs.
-->

* **[ID] ([Title])**
  [Full description of the constraint, including boundary definition, rationale, and consequences of violation. Typically 2-5 sentences.]

---

### C. Quality Goals ([EPIC_CODE]-QG-###)
<!--
PURPOSE: Full descriptions of quality goals from §II.A.3.
Include measurable criteria, verification method, and success threshold.

EXAMPLE:
* **T102B-QG-001 (GDR Locatability)**
  Client must be able to locate any GDR in the SPS artifact in under 30 seconds using standard text search. Verification: Timed test with 5 random GDRs; success = all found in <30s average. This goal ensures the GDR index (T102B-ADR-001) and anchoring system (T102B-ADR-002) provide effective navigability. Source: T102-QG-003 (Usability).
-->

* **[ID] ([Title])**
  [Full description including measurable criteria, verification method, and success threshold. Typically 3-6 sentences.]

---

### D. Dependencies ([EPIC_CODE]-DEP-###)
<!--
PURPOSE: Full descriptions of dependencies from §II.A.4.
Include what is depended on, provider, and consequences if not met.

EXAMPLE:
* **T102B-DEP-001 (T102-ADR-004 Governance Rules)**
  This epic depends on the governance rules established in T102-ADR-004 (Decision Records Index). Specifically, the GDR/ADR pairing requirement, index table format, and promotion workflow. Provider: T102 initiative (parent). If not met: Cannot establish compliant E-GDRs, phase 0 blocked. Status: Met (T102-ADR-004 accepted 2025-01-10).
-->

* **[ID] ([Title])**
  [Full description including what is depended on, provider, and consequences if not met. Typically 3-5 sentences.]

---

### E. Interfaces ([EPIC_CODE]-IF-###)
<!--
PURPOSE: Full descriptions of interfaces from §II.A.5.
Include interface definition, data contracts, and integration points.

EXAMPLE:
* **T102B-IF-001 (Gate Approval Interface)**
  Interface between LLM_Consultant and Client for E-GDR approval at phase boundaries. Contract: Consultant presents completed proposal with all E-IDs in §II; Client reviews and checks Gate checklist in §VII; approval recorded in §VII with date/signature. Integration: Client response triggers SSOT promotion (T102B-ADR-003). Frequency: Once per phase.
-->

* **[ID] ([Title])**
  [Full description including interface definition, data contracts, and integration points. Typically 3-6 sentences.]

---

### F. Implementation Guidance ([EPIC_CODE]-IG-###)
<!--
PURPOSE: Full descriptions of implementation guidance from §II.A.6.
Include pattern/convention, rationale, and application guidance.

EXAMPLE:
* **T102B-IG-001 (Frontmatter Metadata Convention)**
  All proposal files must include YAML frontmatter with these fields: artifact_type, initiative_id, epic_id, epic_code, phase, version, date, status, author, decision_owner_role, plan_reference, analysis_reference, target_document, target_section. Rationale: Enables programmatic discovery, version tracking, and automated workflow tooling (T102B-ADR-005). Application: Use template_workspace_proposal.md as starting point; update metadata before first consultancy session.
-->

* **[ID] ([Title])**
  [Full description including pattern/convention, rationale, and application guidance. Typically 3-6 sentences.]

---

## IV. E-DID BODIES (NORMATIVE)
<!--
PURPOSE: Full bodies for confirmed GDRs/ADRs from Section II.B following T102-ADR-004 format.

DR BODY FORMAT (per T102-ADR-004):
- Context: Why this decision is needed; what problem/ambiguity it resolves
- Decision: The ruling or solution chosen (governance for GDR, technical for ADR)
- Consequences: Positive (+), neutral (±), and negative (-) outcomes
- References: Related E-RIDs, I-RIDs, other DRs (use backticks for IDs)
- Alternatives Considered (ADR only): Options evaluated and reasons for rejection

INDEXING REQUIREMENT (per T102-ADR-004):
- All GDRs must appear in index table (§IV.A) before bodies (§IV.B)
- All ADRs must appear in index table (§IV.C) before bodies (§IV.D)
- Index provides quick lookup; bodies provide full context
-->

### A. E-GDR Index
<!--
PURPOSE: Master index of all E-GDRs for quick reference. Per T102-ADR-004 requirements.

COLUMN DEFINITIONS:
- GDR ID: Full E-GDR identifier (e.g., T102B-GDR-001)
- Title: Short descriptive title
- Status: Proposed / Accepted / Rejected / Superseded
- Owner: Decision authority (typically "Client" for governance)
- Effective: Date the GDR became active (YYYY-MM-DD)
- Supersedes: ID of previous GDR this replaces (or "—" if none)
- Anchor: Markdown anchor for linking (e.g., #gdr-approval-process)

EXAMPLE ROW:
| T102B-GDR-001 | E-GDR Approval Process | Accepted | Client | 2025-01-15 | — | #gdr-approval-process |
-->
| GDR ID | Title | Status | Owner | Effective | Supersedes | Anchor |
|:-------|:------|:-------|:------|:----------|:-----------|:-------|
| [GDR-001] | [Title] | [Proposed/Accepted] | Client | YYYY-MM-DD | — | #[anchor] |

---

### B. E-GDR Bodies
<!--
PURPOSE: Full normative bodies for all E-GDRs from §IV.A index.

GDR BODY EXAMPLE:
* **T102B-GDR-001 (E-GDR Approval Process) {#gdr-approval-process}**
  **Context**: Without a defined approval process, E-GDRs could be promoted to SSOT without client review, violating the principle of client decision authority (T102-GDR-001). This creates governance ambiguity.
  **Decision**: All E-GDRs proposed in a phase must be reviewed and approved by the client via the Gate Approval checklist (§VII) before promotion to SSOT. Approval is recorded with date and signature.
  **Consequences**:
  (+) Ensures client retains decision authority over governance rules
  (+) Creates audit trail of approval dates for compliance
  (±) Adds Gate review step to phase workflow (time cost vs. governance rigor)
  (-) Blocks SSOT promotion if client unavailable (mitigated by T102B-IF-001 scheduling)
  **References**: `T102-GDR-001` (Client Decision Authority), `T102B-IF-001` (Gate Approval Interface), `T102B-DEP-001` (T102-ADR-004 Governance Rules)
-->

* **[GDR-ID] ([Title]) {#[anchor]}**
  **Context**: [Why this decision is needed; what problem/ambiguity it resolves. 2-4 sentences.]
  **Decision**: [The governance ruling being established. 1-3 sentences.]
  **Consequences**:
  (+) [Positive consequence]
  (+) [Positive consequence]
  (±) [Neutral/tradeoff consequence]
  (-) [Negative consequence requiring mitigation]
  **References**: `[Related E-RID/I-RID]`, `[Related E-RID/I-RID]`

---

### C. E-ADR Index
<!--
PURPOSE: Master index of all E-ADRs for quick reference. Per T102-ADR-004 requirements.

COLUMN DEFINITIONS:
- ADR ID: Full E-ADR identifier (e.g., T102B-ADR-001)
- Title: Short descriptive title
- Paired GDR: The GDR this ADR implements (e.g., T102B-GDR-001)
- Status: Proposed / Accepted / Rejected / Superseded
- Canonical Link: Where the ADR body is stored (format: artifact_type_epic_code#anchor)

CANONICAL LINK CONVENTION:
- Typically points to Concept artifact: concept_T102B#adr-metadata-tracking
- For phase 0 foundational ADRs, may point to Proposal: proposal_T102B_phase0#adr-frontmatter
- Format: [artifact_type]_[epic_code]#[anchor]

EXAMPLE ROW:
| T102B-ADR-001 | GDR Index Table Format | T102B-GDR-002 | Accepted | concept_T102B#adr-index-table |
-->
| ADR ID | Title | Paired GDR | Status | Canonical Link |
|:-------|:------|:-----------|:-------|:---------------|
| [ADR-001] | [Title] | [GDR-ID] | [Proposed/Accepted] | concept_[epic]#[anchor] |

---

### D. E-ADR Bodies
<!--
PURPOSE: ADR bodies typically stored in Concept artifact per T102C-GDR-004.
Include here only if Concept not yet established or for phase 0 foundational ADRs.

ADR BODY EXAMPLE:
* **T102B-ADR-001 (GDR Index Markdown Table Format) {#adr-index-table}**
  **Context**: T102B-GDR-002 requires a GDR index for quick reference, but does not specify format. Options include markdown table, YAML file, JSON registry, or custom tool.
  **Decision**: Implement GDR index as markdown table in SPS §IV.A with columns: GDR ID, Title, Status, Owner, Effective, Supersedes, Anchor. Format enables human readability, version control diffs, and grep-based search without custom tooling.
  **Consequences**:
  (+) No new tooling required; works with existing markdown workflow
  (+) Diffable in git; easy to track changes over time
  (±) Manual maintenance required (no auto-generation)
  (-) No enforced schema; validation requires external script (see T102B-ISSUE-002)
  **Alternatives Considered**:
  - YAML file: Better schema enforcement, but requires parsing; rejected for accessibility
  - JSON registry: Machine-readable, but poor human readability; rejected for usability
  - Custom tool: Full automation, but high development cost; deferred to later phase
  **References**: `T102B-GDR-002` (GDR Index Requirement), `T102-QG-003` (Usability), `T102B-CON-001` (No New Tools Phase 0)

NOTE: If ADR body is stored in Concept, include only a pointer here:
* **T102B-ADR-002 (GDR Anchoring System)**
  **Canonical Location**: `concept_T102B.md#adr-gdr-anchoring`
  **Summary**: [1-sentence summary of the ADR]
-->

* **[ADR-ID] ([Title]) {#[anchor]}**
  **Context**: [Technical problem or architectural choice point. 2-4 sentences.]
  **Decision**: [Solution approach chosen. 1-3 sentences.]
  **Consequences**:
  (+) [Positive consequence]
  (±) [Neutral/tradeoff consequence]
  (-) [Negative consequence]
  **Alternatives Considered**:
  - Option A: [Description] — Rejected because [reason]
  - Option B: [Description] — Rejected because [reason]
  **References**: `[Paired GDR]`, `[Related E-RID]`

---

## V. E-OID BODIES (NORMATIVE)
<!--
PURPOSE: Full bodies for Issues/Risks/Research/Notes from Section II.C.
These follow T102-ADR-006 and T102-ADR-007 schemas.
-->

### A. Issues Register (T102-ADR-007)
<!--
PURPOSE: Full register of all Issues per T102-ADR-007 schema.

COLUMN DEFINITIONS (per T102-ADR-007):
- ID: Full ISSUE identifier (e.g., T102B-ISSUE-001)
- Title: Short descriptive title
- Description: Full problem description (can be detailed)
- Owner: Person/role responsible for resolution
- Status: OPEN / RESOLVED / DEFERRED / ESCALATED
- Priority: HIGH / MEDIUM / LOW
- Proposed Date: When issue was identified (YYYY-MM-DD)
- Resolution Notes: How the issue was resolved (or deferral rationale)
- Resolution Date: When resolution occurred (YYYY-MM-DD)

ISSUE LIFECYCLE:
1. Identified during consultancy → Status: OPEN
2. Resolution proposed → Status: OPEN (resolution notes added)
3. Client approves resolution → Status: RESOLVED (resolution date added)
4. OR: Issue deferred to later phase → Status: DEFERRED (deferral rationale in notes)
5. OR: Issue requires external help → Status: ESCALATED

EXAMPLE ROW:
| T102B-ISSUE-001 | No GDR validation tooling | Currently no automated validation for GDR index table format; manual review required | LLM_Developer | RESOLVED | MEDIUM | 2025-01-10 | Created validation script per T102B-ADR-003; tested with 5 sample GDRs | 2025-01-12 |
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|
| [ISSUE-001] | [Title] | [Description] | Client | [OPEN/RESOLVED/DEFERRED] | [HIGH/MEDIUM/LOW] | YYYY-MM-DD | [Resolution] | YYYY-MM-DD |

---

### B. Risks Register (T102-ADR-007)
<!--
PURPOSE: Full register of all Risks per T102-ADR-007 schema.

COLUMN DEFINITIONS (per T102-ADR-007):
- ID: Full RISK identifier (e.g., T102B-RISK-001)
- Title: Short descriptive title
- Description: Full risk description including likelihood and impact
- Owner: Person/role responsible for monitoring/mitigation
- Status: MONITORED / MITIGATED / ACCEPTED / OCCURRED
- Priority: HIGH / MEDIUM / LOW
- Proposed Date: When risk was identified (YYYY-MM-DD)
- Mitigation Notes: Mitigation strategy or acceptance rationale
- Mitigation Date: When mitigation was implemented (YYYY-MM-DD)

RISK LIFECYCLE:
1. Identified during consultancy → Status: MONITORED
2. Mitigation strategy proposed → Status: MONITORED (mitigation notes added)
3. Mitigation implemented → Status: MITIGATED (mitigation date added)
4. OR: Risk accepted without mitigation → Status: ACCEPTED (acceptance rationale in notes)
5. OR: Risk materializes → Status: OCCURRED (becomes ISSUE; cross-reference added)

EXAMPLE ROW:
| T102B-RISK-001 | Client may reject GDR overhead | Client has expressed preference for governance-light approaches in T102A; may view E-GDR approval process as too bureaucratic | LLM_Consultant | MITIGATED | HIGH | 2025-01-10 | Emphasized audit trail benefit and efficiency of table-based review; client approved streamlined checklist approach | 2025-01-12 |
-->
| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
|:---|:------|:------------|:------|:-------|:---------|:--------------|:-----------------|:----------------|
| [RISK-001] | [Title] | [Description] | Client | [MONITORED/MITIGATED/ACCEPTED] | [HIGH/MEDIUM/LOW] | YYYY-MM-DD | [Mitigation] | YYYY-MM-DD |

---

### C. Research Register (T102-ADR-006)
<!--
PURPOSE: Full register of all commissioned research per T102-ADR-006.

RESEARCH WORKFLOW (per T102-ADR-006):
1. LLM_Consultant identifies knowledge gap → Creates RES brief
2. LLM_Researcher produces RES report with verdict/findings
3. Report informs E-RID/E-DID creation → RES-ID referenced in E-ID "Source" field
4. RES tracked in this register for traceability

COLUMN DEFINITIONS:
- RES ID: Full RES identifier (e.g., T102B-RES-001)
- Title: Short descriptive title
- Summary: 1-2 sentence summary of research focus and verdict
- Linked To: E-RID/E-DID that this research informed (for traceability)
- Brief: Path to research brief file
- Report: Path to research report file

EXAMPLE ROW:
| T102B-RES-001 | Request Artifact Analysis | Analysis of existing Request artifact structure; verdict: Confirmed need for versioning and status tracking | T102B-ASSUM-002, T102B-CON-003 | prompt/artifacts/tasks/T102/consultant/research/brief/brief_T102B-RES-001.md | prompt/artifacts/tasks/T102/consultant/research/report/report_T102B-RES-001.md |
-->
| RES ID | Title | Summary | Linked To | Brief | Report |
|:-------|:------|:--------|:----------|:------|:-------|
| [RES-001] | [Title] | [1-2 sentence summary] | [E-RID/E-DID] | [path to brief] | [path to report] |

---

### D. Notes Register (T102-ADR-006-FR-008)
<!--
PURPOSE: Lightweight insights (≤200 words) extracted from Decision Log or consultancy dialogue.
Per T102-ADR-006-FR-008, NOTEs are for contextual clarifications, philosophy, industry references, or observations.

NOTE GUIDELINES (per T102-ADR-006-FR-008):
- CONCISION: Keep ≤200 words; this forces clarity and avoids duplication
- LINK-DON'T-DUPLICATE: Reference existing content rather than restating
- PROMOTE-IF-SUBSTANTIVE: If NOTE grows beyond 200 words, promote to substantive artifact (RES, E-RID, etc.)
- EXTRACTION SOURCE: Typically Decision Log; captured when topic warrants persistence

NOTE CATEGORIES (examples):
- Philosophy: Why we use certain approaches (e.g., "Why GDR/ADR pairing matters")
- Industry Context: Standards/frameworks that inform decisions (e.g., "BABOK v3 assumption types")
- Observation: Patterns noticed during consultancy (e.g., "Client prefers visual aids over text")
- Clarification: Disambiguation of terms or concepts (e.g., "Difference between E-RID and I-RID")

EXAMPLE NOTE BODY:
* **T102B-NOTE-001 (Why GDR/ADR Pairing Matters)**
  ISO 29148 emphasizes traceability between requirements and design decisions. In our system, GDRs (governance requirements) establish WHAT must be governed, while ADRs (architectural decisions) document HOW governance is implemented. Pairing ensures every governance rule has a documented implementation approach, and every implementation decision has a governance justification. This bidirectional traceability enables impact analysis: "If we change this GDR, which ADRs are affected?" Without pairing, governance becomes aspirational rather than operational. Industry precedent: TOGAF ADR linking, BABOK decision modeling. Per T102-ADR-004, this pairing is normative. [Word count: 98]
-->

* **[NOTE-ID] ([Title])**
  [≤200 words: contextual clarification, philosophy, industry reference, or observation. Link-don't-duplicate per T102-ADR-006-FR-008. Include word count at end: [Word count: ###]]

---

## VI. OPEN QUESTIONS REGISTER
<!--
PURPOSE: Track unresolved questions during consultancy. All questions must be resolved or deferred before approval.

OPEN QUESTIONS WORKFLOW:
1. LLM_Consultant identifies ambiguity → Adds OQ with status=OPEN
2. Question posed to client → Status remains OPEN
3. Client provides answer → Status=ANSWERED, resolution date added
4. OR: Question deferred to later phase → Status=DEFERRED, deferral rationale added
5. Gate approval blocked if any OQ with Blocking=YES and Status=OPEN

COLUMN DEFINITIONS:
- OQ-ID: Unique question identifier (OQ-001, OQ-002, etc.)
- Topic: Subject area (e.g., "Approval Process", "Index Format", "Tooling")
- Question: Full question text (be specific; avoid ambiguity)
- Owner: Person/role responsible for answering (typically Client)
- Status: OPEN / ANSWERED / DEFERRED
- Blocking: YES (blocks Gate approval) / NO (nice-to-have)
- Proposed Date: When question was raised (YYYY-MM-DD)
- Resolved Date: When question was answered/deferred (YYYY-MM-DD)

EXAMPLE ROW:
| OQ-001 | Approval Process | Should E-GDR approval require written signature or verbal confirmation sufficient? | Client | ANSWERED | YES | 2025-01-10 | 2025-01-11 |
(Answer recorded in Decision Log: Client confirmed written approval preferred for audit trail)
-->
| OQ-ID | Topic | Question | Owner | Status | Blocking | Proposed Date | Resolved Date |
|:------|:------|:---------|:------|:-------|:---------|:--------------|:--------------|
| OQ-001 | [Topic] | [Question] | Client | [OPEN/ANSWERED/DEFERRED] | [YES/NO] | YYYY-MM-DD | YYYY-MM-DD |

---

## VII. APPROVAL GATE (CLIENT)
<!--
PURPOSE: Master checklist for client approval. All items must be checked before Phase [#] can proceed to SSOT implementation.

GATE PROCESS:
1. LLM_Consultant completes proposal (all sections populated)
2. LLM_Consultant marks proposal status="ready_for_review" in frontmatter
3. Client reviews proposal against this checklist
4. Client checks each box to confirm compliance
5. Client provides approval statement with date/signature
6. Upon approval, LLM_Consultant promotes E-IDs to SSOT per target_document/target_section
7. Proposal archived as decision record

BLOCKING CONDITIONS:
- Any unchecked box blocks approval
- Any OPEN question with Blocking=YES blocks approval
- Any OPEN issue with Priority=HIGH blocks approval (unless deferred with rationale)
-->

### E-ID Approval
- [ ] All E-RIDs reviewed and approved (§II.A and §III match; no unresolved discrepancies)
- [ ] All E-GDRs reviewed and approved (§II.B.1 and §IV.A/B match; client authority confirmed)
- [ ] All E-ADRs reviewed and approved (§II.B.2 and §IV.C/D match; GDR pairing validated)

### Governance Compliance
- [ ] All IDs compliant with T102-ADR-005 (ID format: [EPIC_CODE]-[CATEGORY]-[###] verified)
- [ ] All DRs compliant with T102-ADR-004 (GDR/ADR pairing, index tables, body format verified)
- [ ] All RES/NOTE-IDs compliant with T102-ADR-006 (research workflow, ≤200 word NOTEs verified)
- [ ] All Issues/Risks compliant with T102-ADR-007 (schema, status values, resolution tracking verified)

### Issue Resolution
- [ ] All Issues resolved or deferred with rationale (§V.A: no OPEN issues with Priority=HIGH)
- [ ] All Risks mitigated/accepted with rationale (§V.B: all risks have mitigation notes)
- [ ] All Open Questions resolved or deferred (§VI: no OPEN questions with Blocking=YES)

### Process Compliance
- [ ] Decision Log updated for all subphases (check: prompt/config/orchestration.json or equivalent)
- [ ] Analysis file reviewed and integrated (check: analysis_reference in frontmatter points to current analysis)
- [ ] Proposal reviewed against plan success criteria (check: plan_reference in frontmatter; compare deliverables)

### Client Approval Statement
**Approval Date**: YYYY-MM-DD
**Approved By**: [Client Name]
**Status**: [Draft / Approved / Requires Revision]
**Comments**: [Any approval conditions, notes, or requested revisions. If "Requires Revision", specify what needs to change before re-review.]

---

## VIII. CHANGELOG
<!--
PURPOSE: Track proposal evolution across versions. Update for all material changes.

VERSIONING:
- MAJOR.MINOR.PATCH (semantic versioning)
- MAJOR: Structural changes (new sections, ID category changes)
- MINOR: Content additions (new E-IDs, new sections within existing structure)
- PATCH: Corrections, clarifications, formatting fixes

EXAMPLE ENTRIES:
| 1.0.1 | 2025-01-12 | Fixed typo in T102B-GDR-001 Context section; clarified OQ-001 |
| 1.1.0 | 2025-01-13 | Added T102B-RES-002 and T102B-ASSUM-003 based on research findings |
| 2.0.0 | 2025-01-15 | Restructured E-ADR section per client feedback; moved ADR bodies to Concept artifact |
-->
| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0.0 | YYYY-MM-DD | Initial draft proposal |
