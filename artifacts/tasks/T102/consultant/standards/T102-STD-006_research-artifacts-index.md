# T102-STD-006 — Research Artifacts Index

## Specification

* **T102-STD-006-CLAUSE-001 (RES ID Pattern Integration)**
    - Research ID pattern: `<SCOPE_ID>-RES-###` where `SCOPE_ID ∈ {T102, T102A, T102B, T102C, T102D, T102E, ...}`.
    - ID construction follows `T102-STD-005 (ID Specification & Rules)` universal pattern.
    - Sequential numbering (001, 002, ...) within each scope level (Initiative, Epic, Feature).
    - Category definition: "RES — Research: Formally commissioned research with approved brief and validated report artifacts; traceable via Research Artifacts Index per `T102-STD-006`".
    - Integration: `T102-STD-005-CLAUSE-004 (ID Categories)` SHALL include the RES category and scope allowances.

* **T102-STD-006-CLAUSE-002 (Research Table Schema)**
    - **Local SPS Tables** (Initiative/Epic/Feature sections):
      - Placement: Section titled "Research" & Notes" with subsections "Research" and "Notes"."
      - Schema: `| Research ID | Title | Summary | Reference | Brief | Report |`.
      - Column alignment: left-aligned (`:---`).
    - **Concept Aggregation Register** (Section E.3):
      - Placement: `concept` document in Section E (Registers) → Subsection 3 (Research Artifacts Register).
      - Schema: `| Scope | Scope ID | Research ID | Title | Summary | Reference | Brief | Report | Source | Last Verified | Link Status |`.
      - Column alignment: left-aligned (`:---`).
    - **Universal Column Specifications:**
      - Scope (Concept only): PM hierarchy level {Initiative, Epic, Feature}.
      - Scope ID (Concept only): Back-ticked scope identifier (e.g., `T102`, `T102A`).
      - Research ID: Back-ticked full RES-### identifier (e.g., `T102-RES-001`, `T102A-RES-001`).
      - Title: Bold-formatted descriptive name using `**Title Text**` (2–8 words recommended).
      - Summary: Executive summary (1–2 sentences, target <100 words).
      - Reference: Back-ticked, comma-separated list of consuming IDs (e.g., `T102-GDR-006`, `T102-ISSUE-005`).
      - Brief: Markdown link to research brief artifact with repo-relative path.
      - Report: Markdown link to research report artifact with repo-relative path.
      - Source (Concept only): Back-ticked repo-relative path to SPS section containing the local research table (with section anchor), e.g., `../sps/sps_T102-CONSULTANT.md#vii-epic-research--notes`.
      - Last Verified (Concept only): ISO-8601 date `YYYY-MM-DD` of the last link-integrity verification for the entry.
      - Link Status (Concept only): One of `{OK, BROKEN}` indicating whether Brief/Report/Source paths currently resolve.
    - **Artifact Filenames:**
      - Brief files SHALL follow: `brief_<SCOPE-SID>-<SCOPE-NAME>_<title>.md`.
      - Report files SHALL follow: `report_<SCOPE-SID>-<SCOPE-NAME>_<title>.md`.
      - Brief and Report for the same research SHALL share the same `<SCOPE-SID>-<SCOPE-NAME>_<title>` stem.
      - Public links in SPS tables and Concept registers MUST use canonical **unversioned** filenames and MUST omit any `_i<n>` revision suffix.
      - Versioned filename stems (e.g., `*_v1.0.0.md`) are prohibited in public links.
    - **Templates:**
      - `prompt\templates\researcher\template_research_brief.md`
      - `prompt\templates\researcher\template_research_report.md`

* **T102-STD-006-CLAUSE-003 (Placement Decision Criteria)**
    - Inline Summary (<300 words): Brief research findings MAY be integrated directly into SPS body sections (Epic Notes, Implementation Guidance) when contextually essential.
    - Local Index Entry (mandatory for all formal research): All commissioned research with approved brief + validated report SHALL appear in the corresponding SPS scope's local Research table.
    - Concept Aggregation (mandatory for all formal research): Master Research Register in Concept Section E.3 SHALL consolidate all Initiative/Epic/Feature research.
    - External-Only (extensive research >3 pages): Research reports stored in dedicated `research/report/` directory; only summary and markdown links appear in indexes.
    - Threshold application: Research findings guide inline placement decisions; all formal research indexed in both SPS local tables and Concept register regardless of report size.

* **T102-STD-006-CLAUSE-004 (Index Maintenance Protocol)**
    - Synchronization approach: Manual verification; tooling deferred to future development per `T102-CON-002 (Minimal Automation)`.
    - Addition workflow: New research commissioned → (1) Create RES-### entry in appropriate SPS scope's local Research table, (2) Update Concept Research Register with aggregated entry including Scope/Scope ID/Source.
    - Update workflow: Research content revisions → Update Summary in both SPS local index and Concept register; keep Brief/Report links pointing to canonical unversioned filenames; preserve version history via git history and in-body metadata (not in public link filenames).
    - Deprecation workflow: Superseded research → Add inline note to Summary (e.g., "Superseded by T102-RES-004 addressing expanded scope"); maintain entry for audit trail; update Reference column to reflect current consuming IDs.
    - Link-integrity verification step: When adding or updating any entry, authors MUST verify that Brief/Report/Source paths resolve to existing files/anchors. For Concept entries, authors MUST update `Last Verified` and set `Link Status` to `OK` or `BROKEN` accordingly.
    - Verification cadence: Review synchronization at each epic handoff gate; escalate material drift to Client for resolution.

* **T102-STD-006-CLAUSE-005 (Cross-Artifact Referencing)**
    - Research findings SHALL be referenced via RES-### ID tokens in back-ticked format, never copy-pasted verbatim.
    - GDRs/ADRs consuming research SHALL cite RES-### in References sections using `RES-SID (Title)` when appropriate.
    - Issues/Risks resolved via research SHALL cite RES-### in resolution notes.
    - Feature/Story artifacts inheriting research context SHALL reference RES-### via Inherited Considerations tables per `T102-STD-003` when critical to downstream scope.
    - Research brief/report MAY be linked using markdown link syntax when full artifact review needed; use RES-### ID for governance traceability.

* **T102-STD-006-CLAUSE-006 (Hybrid Pattern Scalability)**
    - Pattern applies uniformly across Initiative/Epic/Feature scopes with identical table schemas at each level.
    - Feature-level research (e.g., `T102A1-RES-001`) follows dual-indexing: local table in REQUEST artifact + aggregation in Concept register.
    - Story-level research deferred to future need assessment; if required, would follow same pattern with local table in DESIGN artifact.
    - Concept register remains single source of truth for initiative-wide research landscape; SPS/REQUEST local tables provide contextual proximity for authoring efficiency.

* **T102-STD-006-CLAUSE-007 (Concept-as-Master Fallback Mode)**
    - If dual-index drift controls cannot be enforced in practice, the initiative MAY adopt a fallback mode where the Concept Research Register is authoritative and SPS local tables are treated as local views.
    - In fallback mode, Concept entries MUST include `Last Verified` and `Link Status` and MUST be maintained as the coordination audit surface; SPS local tables MUST still exist but MAY be reduced to the minimum required columns for local context.
    - Fallback mode MUST be explicitly declared in Concept to avoid silent governance ambiguity.

* **T102-STD-006-CLAUSE-008 (Evaluation Rubric Specification)**
    - Research briefs that commission comparative or evaluative research MUST include a weighted evaluation rubric.
    - Rubric placement: The rubric MUST appear in Section III (Constraints, Assumptions & Methodology) of the research brief.
    - Rubric schema: Each rubric dimension MUST include: (a) a descriptive label, (b) a numeric weight on a 1–5 scale (1 = lowest priority, 5 = highest priority), and (c) a 1-sentence description of what the dimension measures.
    - Rubric application: Research reports MUST apply the brief's rubric to all topics requiring option comparison, producing per-option scores (1–5 per dimension) and weighted totals.
    - Rubric exemption: Briefs that do not commission comparative evaluation (e.g., pure fact-finding or inventory research) MAY omit the rubric.

## Decision Record

* **T102-STD-006-ADR-001 (Research Artifacts Index)** {#t102-std-006-research-index}

  * **Context**
    Per `T102-GDR-006 (Research Workflow Standard)`, formal research workflow requires architectural implementation specification for artifact indexing, placement strategies, and cross-scope traceability. External research (`T102-RES-001`) validated three-tier placement strategy (inline/appendix/external) and recommended hybrid index architecture: local indexes in SPS artifacts (Initiative/Epic/Feature-level) plus master aggregation register in Concept workspace. Current ad-hoc NOTE pattern created scalability concerns (`T102A-RISK-003`) without structured research governance.

  * **Decision**
    Implement hybrid Research Artifacts Index architecture with dual-layer indexing and standardized placement thresholds:

      - **Why:** Balance local context visibility (SPS sections) with initiative-wide research landscape aggregation (Concept master register) while maintaining "link-don't-duplicate" principle per `T102-STD-003`.
      - **What:** Two-tier index structure: (1) Local Research tables in SPS artifacts at Initiative/Epic/Feature scope levels, (2) Aggregated Research Register in Concept Section E.3 consolidating all research with source traceability and markdown-linked artifacts.
      - **Benefit:** Enables scalable research commissioning without document bloat while providing comprehensive research visibility for decision-making and audit trails.

  * **Alternatives Considered**
    (a) SPS‑only research indexing — rejected: no initiative‑wide aggregation visibility; manual cross‑Epic correlation; conflicts with Concept's dynamic workspace role per `T102-STD-001`.
    (b) Concept‑only research register — rejected: eliminates local context in SPS artifacts; reduces executive readability per `T102-QG-001`.
    (c) Automated synchronization tooling — rejected: violates `T102-CON-002 (Minimal Automation)` v1 constraint; manual verification is sufficient at current scale.
    (d) Embedded research content — rejected: creates document bloat; `T102-RES-001` validated as anti‑pattern.

  * **Consequences**
    (+) Scalable research commissioning without SPS document bloat via structured placement strategy.
    (+) Initiative‑wide research landscape visibility through Concept aggregation supporting decision‑making.
    (+) Maintains local context in SPS/REQUEST for executive readability per `T102-QG-001`.
    (+) Clear audit trail and traceability for LLM‑generated research per `T102-QG-004`.
    (+) Aligns with "link‑don't‑duplicate" principle per `T102-STD-003` avoiding content drift.
    (+) Markdown links to Brief/Report enable one‑click artifact access for validation workflows.
    (±) Requires dual maintenance (SPS local + Concept register) introducing manual synchronization overhead.
    (±) Requires discipline in RES/NOTE ID assignment and updates across two locations.
    (±) Omitting `_i<n>` suffixes and versioned stems from public links requires filename discipline (canonical unversioned filenames in indexes).
    (-) Manual verification approach creates drift risk; periodic review cadence required.
    (-) Migration effort to refactor existing research NOTEs to RES‑### pattern where formal artifacts exist.

## References

`T102-GDR-006 (Research Workflow Standard)`,
  `T102-GDR-007 (LLM Quality Control)`,
  `T102-STD-003 (Explicit Inheritance Model)`,
  `T102-STD-005 (ID Specification & Rules)`,
  `T102-CON-002 (Minimal Automation)`,
  `T102-QG-001 (Client Readability)`,
  `T102-QG-002 (End-to-End Traceability)`,
  `T102-QG-004 (Research Validation Quality)`,
  `T102-RES-001 (Research Integration Governance Research)`

## Provenance

—
