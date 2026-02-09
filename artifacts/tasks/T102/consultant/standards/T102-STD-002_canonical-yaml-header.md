# T102-STD-002 — Canonical YAML Header

## Specification

1) **T102-STD-002-CLAUSE-001 (Header Keys)**  
      The template SHALL begin with a valid **YAML header** containing only these core keys:  
      `artifact_type, initiative_id, (epic_id), (feature_id), (story_id), version, date, status, author, decision_owner_role, (dependencies)` where keys in parentheses are required when applicable (feature/story docs).

    2) **T102-STD-002-CLAUSE-002 (Key Formats)**  
      The header keys SHALL conform to the following:  
      `artifact_type ∈ {SPS, REQUEST, CONCEPT, DESIGN, PLAN, PROPOSAL, REPORT, BRIEF, ROADMAP, LOG, ANALYSIS}`;  
      `initiative_id: ^T/d{3}$` (e.g., `T102`);  
      `epic_id: ^T/d{3}[A-Z]$` (e.g., `T102A`);  
      `feature_id: ^T/d{3}[A-Z]-[A-Z0-9_]+$` (e.g., `T102A-SPSST`);  
      `story_id: ^T/d{3}[A-Z]-[A-Z0-9_]+-S/d+$` (e.g., `T102A-SPSST-S1`);  
      `version`: SemVer; 
      `date`: ISO-8601 (YYYY-MM-DD);  
      `status ∈ {draft, review, approved, rework, deprecated}`;  
      `author ∈ {LLM_Consultant, LLM_Planner, LLM_Developer, LLM_Reviewer}`;  
      `decision_owner_role = Client`;  

    3) * **T102-STD-002-CLAUSE-003 (Schema Examples)**  
    The template SHALL include canonical examples for SPS/REQUEST/CONCEPT headers and reference **header.schema.v1** (structure only; no enforcement in v1).

## Decision Record

* **T102-STD-002-ADR-001 (Canonical YAML Header)** {#t102-std-002-yaml-header}

  * **Context**
    Per `T102-GDR-002`, we need implementation of a unified YAML header schema across all consultancy artifacts. Current templates suffer
      from inconsistent key definitions, enum variations, and parsing conflicts which has consequent to blocking future reliable automation and creating governance gaps in artifact identity management.

  * **Decision**
    Implement the Canonical YAML Header through standardized schema definition and adoption specifications below:

        - **Why**: Eliminate header schema inconsistencies that block automation and create governance gaps
        - **What**: Unified YAML header specification with mandatory key set, format validation, and conformance requirements
        - **Benefit**: Enables reliable artifact parsing, consistent governance signals, and predictable automation development

  * **Alternatives Considered**
    (a) **YAML-embedded approvals** (rejected): Creates parsing complexity and reduces human readability of approval signals; conflicts     
      with established body-based approval patterns
      (b) **Legacy key preservation** (rejected): Maintains existing inconsistencies including `task_id`/`prefix_id` variations; prevents     
    automation standardization
      (c) **Extended header with automation fields** (deferred): Future v2 consideration; v1 focuses on minimal stable foundation

  * **Consequences**
    (+) Consistent artifact identity and governance parsing across all consultancy layers
      (+) Reliable foundation for validation tools and automation development
      (+) Clear separation between machine-readable headers and human-readable approvals
      (+) Standardized artifact lineage tracking through structured ID hierarchy
      (±) Requires migration of existing artifacts with non-conforming headers
      (-) Body parsing still required for approval signals (design trade-off for readability)

## References

`T102-GDR-002 (Canonical Header Standard)`, 
  `T102-IG-005 (Canonical Header)`,
  `T102-CON-001 (Format Requirements)`, 
  `T102-QG-002 (End-to-End Traceability)`

## Provenance

`design_T102A-SPSST-S1.md`
