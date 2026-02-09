# AC001 TK001 Pre-flight Verification Report

- Date: 2026-02-08
- Scope: ST003 AC001 pre-execution checks

## Script Availability

- migrate_adr_to_std.py: available

## Skills SSOT Print Checks

- ADR-004 print script: failed (anchor marker not found); fallback to current T102-STD-004/template/guideline artifacts
- ADR-005 print script: success

## Directory Baseline

### consultant/standards
- `T102-STD-005_id-specification-rules.md`
- `T102-STD-009_governance-standards-specification.md`
- `T102-STD-004_decision-records-standard.md`

### T102B/standards
- `T102B-STD-001_request-architecture-standard.md`
- `T102B-STD-002_section-classification-standard.md`
- `T102B-STD-003_story-fr-deferral-standard.md`
- `T102B-STD-004_request-lite-specification.md`

## Inline ADR Presence Snapshot (Concept)

- 26:| `T102-STD-001` | Consultancy Operating Model | — | Proposed | Client | 2025-09-18 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-001_consultancy-operating-model.md` |
- 27:| `T102-STD-002` | Canonical YAML Header | — | Proposed | Client | 2025-09-14 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-002_canonical-yaml-header.md` |
- 28:| `T102-STD-003` | Explicit Inheritance Model | — | Proposed | Client | 2025-09-14 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-003_explicit-inheritance-model.md` |
- 30:| `T102-STD-006` | Research Artifacts Index | — | Proposed | Client | 2025-10-12 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-006_research-artifacts-index.md` |
- 31:| `T102-STD-007` | Issues & Risks Index | — | Proposed | Client | 2026-01-01 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-007_issues-risks-index.md` |
- 32:| `T102-STD-008` | Organisation Baseline Index | — | Proposed | Client | 2026-01-12 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102-STD-008_organisation-baseline-index.md` |
- 40:* **T102-STD-001 (Consultancy Operating Model)** {#t102-std-001-consultancy-model}
- 68:    1) **T102-STD-001-CLAUSE-001 (SPS Implementation)** 
- 74:    2) **T102-STD-001-CLAUSE-002 (REQUEST Implementation)** 
- 81:    3) **T102-STD-001-CLAUSE-003 (CONCEPT Implementation)** 
- 87:    4) **T102-STD-001-CLAUSE-004 (DESIGN Implementation)** 
- 111:* **T102-STD-002 (Canonical YAML Header)** {#t102-std-002-yaml-header}
- 122:    1) **T102-STD-002-CLAUSE-001 (Header Keys)**  
- 126:    2) **T102-STD-002-CLAUSE-002 (Key Formats)**  
- 139:    3) * **T102-STD-002-CLAUSE-003 (Schema Examples)**  
- 165:* **T102-STD-003 (Explicit Inheritance Model)** {#t102-std-003-explicit-inheritance}
- 175:    1) **T102-STD-003-CLAUSE-001 (Table Contracts)** 
- 184:    2) **T102-STD-003-CLAUSE-002 (Precedence)**
- 187:    3) **T102-STD-003-CLAUSE-003 (Authoring Rules)**
- 468:    `T102-STD-003 (Explicit Inheritance Model)`, 
- 470:    `T102-STD-006 (Research Artifacts Index)`,
- 476:* **T102-STD-006 (Research Artifacts Index)** {#t102-std-006-research-index}
- 482:  - **Why:** Balance local context visibility (SPS sections) with initiative-wide research landscape aggregation (Concept master register) while maintaining "link-don't-duplicate" principle per `T102-STD-003`.
- 488:    * **T102-STD-006-CLAUSE-001 (RES ID Pattern Integration)**
- 492:       - Category definition: "RES — Research: Formally commissioned research with approved brief and validated report artifacts; traceable via Research Artifacts Index per `T102-STD-006`".
- 495:    * **T102-STD-006-CLAUSE-002 (Research Table Schema)**
- 522:    * **T102-STD-006-CLAUSE-003 (Placement Decision Criteria)**
- 529:    * **T102-STD-006-CLAUSE-004 (Index Maintenance Protocol)**
- 536:    * **T102-STD-006-CLAUSE-005 (Cross-Artifact Referencing)**
- 540:       - Feature/Story artifacts inheriting research context SHALL reference RES-### via Inherited Considerations tables per `T102-STD-003` when critical to downstream scope.
- 543:    * **T102-STD-006-CLAUSE-006 (Hybrid Pattern Scalability)**
- 550:    (a) SPS‑only research indexing — rejected: no initiative‑wide aggregation visibility; manual cross‑Epic correlation; conflicts with Concept's dynamic workspace role per `T102-STD-001`.
- 560:  (+) Aligns with "link‑don't‑duplicate" principle per `T102-STD-003` avoiding content drift.
- 571:  `T102-STD-003 (Explicit Inheritance Model)`,
- 581:* **T102-STD-007 (Issues & Risks Index)** {#t102-std-007-issues-risks-index}
- 589:    1) **T102-STD-007-CLAUSE-001 (Section Naming & Placement)**
- 592:    2) **T102-STD-007-CLAUSE-002 (Issues Guidance & Enum)**
- 596:    3) **T102-STD-007-CLAUSE-003 (Issues Table Schema)**
- 605:    4) **T102-STD-007-CLAUSE-004 (Risks Guidance & Enum)**
- 609:    5) **T102-STD-007-CLAUSE-005 (Risks Table Schema)**
- 618:    6) **T102-STD-007-CLAUSE-006 (ID Rules)**
- 623:    7) **T102-STD-007-CLAUSE-007 (Resolution Notes Requirement)**
- 629:    8) **T102-STD-007-CLAUSE-008 (Mitigation Notes Requirement)**
- 635:    9) **T102-STD-007-CLAUSE-009 (Cross-Scope Promotion & De-duplication)**
- 639:      - Avoid duplicating full narratives across scopes; prefer ID references and delta-only updates per `T102-STD-003 (Explicit Inheritance Model)`.
- 653:  `T102-STD-003 (Explicit Inheritance Model)`,
- 663:* **T102-STD-008 (Organisation Baseline Index)** {#t102-std-008-org-baseline-index}
- 667:  **Decision:** Adopt `T102-STD-008` to standardize the structure and maintenance policy of the initiative-level `III.B` “Organization & Responsibilities” subsection.
- 671:    1) **T102-STD-008-CLAUSE-001 (Canonical Placement)**
- 673:       - Epics SHALL reference this baseline rather than duplicating it (see `T102A-STD-001`).
- 675:    2) **T102-STD-008-CLAUSE-002 (Required Content)**
- 702:    3) **T102-STD-008-CLAUSE-003 (Maintenance Policy)**
- 717:  `T102-STD-003 (Explicit Inheritance Model)`,
- 792:          - MVC items SHOULD cite adopted-spec clause IDs where possible (e.g., `T102-STD-003-CLAUSE-001`).
- 838:| `T102A-STD-001` | Governance & Roadmap Snapshot | — | Proposed | Client | 2026-01-11 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102A-STD-001_governance-roadmap-snapshot.md` |
- 839:| `T102A-STD-002` | Feature Register Index | — | Proposed | Client | 2026-01-11 | — | `prompt/artifacts/tasks/T102/consultant/standards/T102A-STD-002_feature-register-index.md` |
- 841:* **T102A-STD-001 (Governance & Roadmap Snapshot) — {#t102a-std-001-governance-roadmap-snapshot}**
- 845:  **Decision:** Adopt `T102A-STD-001`, establish a single, mandatory structure and maintenance policy for every Epic subsection titled **“Governance & Roadmap”**.
- 849:    1) **T102A-STD-001-CLAUSE-001 (Canonical Placement & Title)**
- 853:    2) **T102A-STD-001-CLAUSE-002 (Section Structure)**
- 859:    3) **T102A-STD-001-CLAUSE-003 (Scope & Ownership Rules)**
- 862:       - Scope & Ownership SHOULD include a single baseline reference line pointing to the initiative-level Org baseline (see `T102-STD-008`).
- 864:    4) **T102A-STD-001-CLAUSE-004 (Baseline Alignment)**
- 865:       - The initiative-level **Organization & Responsibilities** SHALL be defined in `III.B` and treated as the canonical source of truth (see `T102-STD-008 (Organisation Baseline Standard)`).
- 870:    5) **T102A-STD-001-CLAUSE-005 (Org & Responsibilities Boundaries)**
- 873:       - Feature lead/ownership remains a Feature Register concern (governed by `T102A-STD-002`).
- 875:    6) **T102A-STD-001-CLAUSE-006 (Phase & Gates Contract)**
- 888:    7) **T102A-STD-001-CLAUSE-007 (Operational Boundaries)**
- 892:    8) **T102A-STD-001-CLAUSE-008 (References Semantics)**
- 897:    9) **T102A-STD-001-CLAUSE-009 (Maintenance Policy)**
- 917:  `T102-STD-008 (Organisation Baseline Standard)`,
- 918:  `T102A-STD-002 (Feature Register Index)`,
- 927:* **T102A-STD-002 (Feature Register Index) — {#t102a-std-002-feature-register-index}**
- 931:  **Decision:** Adopt `T102A-STD-002` as the mandatory standard for Epic Feature Register placement, schema, and maintenance policy.
- 935:    1) **T102A-STD-002-CLAUSE-001 (Canonical Placement & Title)**
- 939:    2) **T102A-STD-002-CLAUSE-002 (Table Contract)**
- 948:       - `Status`: one of the allowed status values (see `T102A-STD-002-CLAUSE-003`).
- 951:    3) **T102A-STD-002-CLAUSE-003 (Allowed Status Values; Minimal Set)**
- 955:    4) **T102A-STD-002-CLAUSE-004 (Status Transition Rules)**
- 963:    5) **T102A-STD-002-CLAUSE-005 (Change Control & Stability)**
- 998:| `T102C-STD-001` | Concept Architectural Framework | `T102C-GDR-001` | Proposed | — | 2025-09-28 | — | #t102c-std-001-concept-framework |
- 1000:* **T102C-STD-001 (Concept Architectural Framework) {#t102c-std-001-concept-framework}**
- 1012:  1. **T102C-STD-001-CLAUSE-001 (Core Architecture)** Concept artifacts SHALL implement eight-section structure: Identity & Operating Rules, Executive Context, Decision System (ADR Compendium), Readiness Snapshot, Handoff Snapshot, Registers, Integration & Interfaces, Governance per external research recommendations.
- 1013:  2. **T102C-STD-001-CLAUSE-002 (Handoff Authority)** Section V (Handoff Snapshot) SHALL serve as authoritative handoff locus containing: Package Manifest (immutable IDs/versions), Acceptance Signals (Client sign-off), Completeness Checklist (ADR accepted, FRs approved, risks linked), Links (SPS/Request/Design anchors, no copy-paste) per T102C-GDR-003.
- 1014:  3. **T102C-STD-001-CLAUSE-003 (Readiness Aggregation)** Section IV (Readiness Snapshot) SHALL implement manual YAML roll-up table with Initiative/Epic/Feature states, Ready markers at 80% DoR threshold, Client override capability, and "Top 3 blockers" visibility per T102C-GDR-005.
- 1015:  4. **T102C-STD-001-CLAUSE-004 (Implementation Deferral)** Detailed structural templates and procedural guidelines SHALL be specified within T102C-CST and T102C-CPG feature Request artifacts to maintain separation between architectural framework (Epic ADR) and implementation specification (Feature Request).
- 1043:| `T102A-SPSST-STD-0001` | Approvals in body | — | Accepted | Client | — | — | `prompt/artifacts/tasks/T102/consultant/standards/T102A-SPSST-STD-0001_approvals-in-body.md` |
