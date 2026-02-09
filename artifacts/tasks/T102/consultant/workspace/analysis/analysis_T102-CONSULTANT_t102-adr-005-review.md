# Analysis: T102-STD-005 Refactor & Governance Review

**Date:** 2026-01-19
**Author:** Antigravity (Consultant)
**Subject:** Independent Assessment of Governance Rules and ADR-005 Refactor Proposal

## I. Executive Summary
The proposal to refactor `T102-STD-005` from 11 Functional Requirements (FRs) to ~7 is **sound and recommended**. The consolidation reduces verbosity without compromising the agentic precision required for regex-based parsing and validation. The proposed taxonomy aligns well with the "Identity & Schema" consolidation.

However, specific attention must be paid to the **Precedence Hierarchy** and the **Semantics of Categories** (specifically `IG`, `INT`, and `ASSUM`) to ensure the distinction between "Requirements" (What), "Decisions" (Policy), and "Implementation" (How) remains distinct.

---

## II. Review of Refactor Proposal (`proposal_T102...`)

### 1. Consolidation Strategy (Appropriate)
*   **Merging Scope & Construction (FR-001)**: Excellent move. Separating regex from construction rules created unnecessary cognitive load for authors and agents.
*   **Unified Taxonomy (FR-002)**: Combining Types and Categories into a single table is the single biggest improvement. It eliminates the "lookup loop" where one had to cross-reference multiple tables.

### 2. Risks & Gaps
*   **FR-005 (Category Semantics) Complexity**: By grouping `INT`, `IG`, and `ASSUM` logic into one rule, you risk creating a "junk drawer" rule.
    *   **Risk**: `ASSUM` has a complex lifecycle (Pending -> Validated) that might get lost if buried in a generic semantic rule.
    *   **Recommendation**: Keep `ASSUM` lifecycle rigorous. It is the only "stateful" RID (others are static statements).
*   **Variance Logic**: The proposal mentions "Variance ADR" in `FR-003`. This needs to be explicit. If a Feature deviates from an Epic ADR, it **must** be an ADR, not a Note.

---

## III. Detailed Governance Assessment (QA Rounds 1-3)

### Round 1: Initial Governance Concerns

#### 1. Hierarchy: IID vs. DRID (IG vs. ADR relationship)
**Client Question**: "Should IID > DRID, meaning does `IG` requirements constitute GDR/ADR or should it be the other way around?"

**Analysis**:
*   **Precedence**: `DRID` (Decision) **>** `IID` (Implementation).
*   **Rationale**:
    *   `DRID` (GDR/ADR) represents a **Legislated Decision** (Policy). It implies "We have debated options and selected this path."
    *   `IID` (IG) represents **Guidance**. It implies "Here is the standard way to do X."
    *   While an `IG` describes *how* to implement something, an `ADR` validates *that* it is the chosen standard.
*   **Workflow (The Proviso)**: `T102-STD-004-FR-013` describes a **Promotion Workflow** where `IG` (candidate pattern) $\to$ `ADR` (formal decision).
    *   **In Time**: `IG` might come first (as a draft/pilot).
    *   **In Authority**: Once promoted, the `ADR` is the authority. The `IG` becomes the "body of knowledge" referenced by the `ADR`, or the `ADR` supersedes it.
*   **Recommendation**: Maintain `RID > DRID > IID`.
    *   `RID` (Requirement): "System MUST support high scale." (The Goal)
    *   `DRID` (Decision): "We chose Microservices." (The Policy)
    *   `IID` (Guidance): "Use this microservice template." (The How)

#### 2. IG vs. FR (Industry Standard)
**Client Question**: "What are the differences between IG and FR?"

**Taxonomy**:
| Feature | **FR (Functional Requirement)** | **IG (Implementation Guidance)** |
| :--- | :--- | :--- |
| **Focus** | **Target System** Behavior | **Developer/Author** Behavior |
| **Question** | "What does the software do?" | "How should we build/write it?" |
| **Testability** | Verified by QA / Auto-Tests | Verified by Code Review / Linter |
| **Audience** | User / Tester | Engineer / Author |
| **Example** | "User can login via SSO." | "Use the `auth_provider.py` module." |

**Assessment**: They are fundamentally different. `FR` is a deliverable constraint; `IG` is a process constraint.

#### 3. Level of Definition for IID (IG)
**Client Question**: "Should IID such as IG be defined at initiative or epic levels or is this more feature-specific?"

**Analysis**:
*   **Initiative Level (Global Standards)**: Yes. e.g., "All Python code must follow PEP8." This is an `I-IG`.
*   **Epic Level (Domain Patterns)**: Yes. e.g., "All 'Payment' features must use the Double-Entry Ledger pattern." This is an `E-IG`.
*   **Feature Level (Local Specifics)**: Yes. e.g., "For this specific checkout flow, use the 'One-Click' variant." This is an `F-IG`.

**Recommendation**: Allow `IG` at **ALL** levels (I, E, F). However, favor "Promoting" widely used `F-IGs` to `E-IGs` or `I-IGs` to prevent duplication.

#### 4. Integration (INT) at Epic Level
**Client Question**: "Should INT exist at least at epic level to define cross integration between epics?"

**Analysis**:
*   Currently, the proposal restricts `INT` to Feature level (`FR-005`: "Bottom-up proposals...").
*   **Gap**: There is a need for "Horizontal Integration" definitions between Epics (e.g., T102A Handshaking with T102B).
*   **Recommendation**: **Yes, INT should exist at Epic Level (E-INT).**
*   High-level Integration or Interface Control implies `IF` (Interface) usually.
*   If `INT` is strictly "Integration Guidance", it fits at Epic level to define how Epics talk (e.g., "Epic A outputs JSON that Epic B consumes").

---

### Round 2: Advanced Governance Questions

#### 1. Precedence: RID vs. DRID
**Client Question**: "Is it correct to define precedence for RID > DRID?"

**Analysis**:
*   **Logic**: `RID` (Requirement/Constraint) defines the **Problem Space** and **Boundary Conditions** (e.g., "Must be compliant with GDPR"). `DRID` (Decision) defines the **Solution Choice** (e.g., "Use encryption lib X").
*   **Conflict Rule**: A Decision cannot validly violate a Constraint. If a Decision contradicts a Constraint, the Constraint must be changed, or the Decision is invalid. Therefore, the Requirement (Constraint) holds higher precedence.
*   **Nuance**: A Governance Decision (`GDR`) can establish a new Constraint (e.g., "GDR-001: We are a Cloud-First shop" $\to$ Effectively acts as a Constraint). But in terms of pure ID types, if you have a `CON` (Constraint) and an `ADR` (Decision), the `CON` is the law the `ADR` must follow.
*   **Answer**: **YES**, `RID > DRID` is correct. The "What/Constraint" governs the "How/Decision".

#### 2. Interface (IF) and Integration (INT)
**Client Question**: "How detailed should an IF be? Should IF be IID? What about INT?"

**Analysis**:
*   **IF (Interface)**: Represents a **Contract** between two boundaries.
*   **Type**: If it defines a strict contract (API schema, data format, SLA) that **must** be met, it functions as a **Requirement (RID)**.
*   **Level**: Yes, `IF` belongs at Initiative/Epic level to define "Horizontal Contracts" (e.g., "T102A outputs X for T102B").
*   **INT (Integration)**: The ADR-005 proposal defined `INT` as "Guidance" or "Patterns" for integration, often bottom-up.
*   **Ambiguity**: If `INT` is just "loose guidance", it overlaps with `IG`. If `IF` is "strict contract", it works well.
*   **Recommendation**:
    *   Categorize **IF as RID** (Requirement). It is a constraint on both parties.
    *   **Drop INT** as a separate category if it effectively duplicates `IG`. Use `IG` (e.g., `T102-IG-005 Integration Patterns`) for guidance. Or, if `INT` is kept, define it strictly as "Non-contractual Integration Logic" (which is weak).
    *   **Preferred Path**: Use `if_` (Interface) for Contracts (`RID` layer). Use `ig_` (Impl. Guidance) for integration patterns (`IID` layer).

#### 3. OID References (RES/NOTE)
**Client Question**: "Should RES/NOTES be referenced in RIDs? Are they 'Scope Requirements'?"

**Analysis**:
*   **Normative Rule**: Normative text (SHALL/MUST) should not depend on unstable or non-normative IDs (like ISSUE, RISK, NOTE).
*   **RES (Research)**: Research is **Evidence/Context**, not a Requirement itself.
*   **Usage**: You reference `RES` to **justify** a `RID` or `DRID`.
*   **Example**: "System SHALL support < 100ms latency (Ref: `T102-RES-001`)." -> Valid.
*   **Invalid**: "System SHALL implement `T102-RES-001`." -> Invalid (Research is a report, not a spec).
*   **NOTE**: Notes are purely informational. Never normative.
*   **Separation**: They can remain in `OID` (Other/Object ID) or be split into a "Supporting" category. The key is the **Reference Rule**: "Normative RIDs may cite OIDs in 'Context' or 'Reference' fields, but not as the normative subject."

#### 4. IG vs FR Influence
**Client Question**: "Should IG influence FR or vice versa?"

**Analysis**:
*   **Top-Down (Standardization)**: **IG influences FR**.
*   **Example**: `T102-IG-001 (Microservice Pattern)` $\to$ influences $\to$ `T102B-FR-005 (User Profile Service)`. The `FR` must be built **using** the `IG` pattern.
*   **Bottom-Up (Discovery)**: A specific `FR` might reveal a repetitive pattern that gets promoted to an `IG`.
*   **Industry Standard**: Guidance (Standards) exists to constrain and guide Functional Requirements (Instance).

#### 5. NFR Categorization (IID vs RID)
**Client Question**: "Is NFR part of IID or is that more of a requirement?"

**Analysis**:
*   **Standard**: `NFR` (Non-Functional Requirement) is explicitly a **Requirement**. It describes "Quality Attributes" (Performance, Security) that the system **MUST** meet.
*   **vs QG**:
    *   `QG` (Quality Goal) = Project/Process Success (e.g., "Code coverage > 80%", "Handoff complete").
    *   `NFR` (Non-Functional Req) = System Behavior (e.g., "Response < 200ms", "Encryption at rest").
*   **Correction**: `NFR` should be categorized as **RID (Requirement)**, not IID (Implementation Guidance). It is a Constraint on the system, not just a "hint" on how to code.

---

### Round 3: Detailed Specification QA

#### 1. OID References (RES/NOTE) vs. RESID
**Client Question**: "Should we have a RESID as a separate category with precedence SID > RESID > RID?"

**Analysis**:
*   **Separation**: Separating Research/Evidence (`RESID`) from "Other" (`OID`) is logically sound. Research artifacts (Evidence) are foundational.
*   **Precedence Logic (SID > RESID > RID)**:
    *   `SID` (Scope/Goal): Mentions why we are here (e.g., "Build a Trading App").
    *   `RESID` (Evidence): Tells us what is true (e.g., "Latency must be <50ms for trading").
    *   `RID` (Requirement): Defines what to build (e.g., "System SHALL have <50ms latency").
*   **Assessment**: **AGREED**. Evidence (Truth) precedes Requirement (Law). A Requirement cannot validly contradict established Evidence without justification.
*   **Recommendation**: Promote `RES` to `RESID` type (Evidence Category).

#### 2. INT vs. IG (Consolidation vs. Distinction)
**Client Question**: "INT describes external/cross-boundary patterns; IG describes internal patterns. Keep distinct or consolidate?"

**Analysis**:
*   **Industry Standard**: Usually, "Integration Patterns" are a subset of "Implementation Guidance". However, distinguishing **Boundary Contracts** (External) from **Internal Implementation** (Internal) is useful for encapsulation.
*   **Recommendation**:
    *   **Keep Separate IF** the distinction is "Boundary" vs "Internal".
    *   `INT` (or better, `XIG` - Cross-Implementation Guidance?): If it describes interfaces or handshakes, it's critical.
    *   However, if `INT` is just "how these two features talk", it is still Implementation Guidance.
*   **Consolidation Preferred**: `IG` is sufficient. `T102-IG-005 (Integration Patterns)` is cleaner than a whole new token type. You can use tagging/titles to distinguish scope.
*   **Exception**: If you strictly need to filter "Integration Specs" for an external team, a separate token helps. If not, merge into `IG`.

#### 3. NFR Categorization & Scope
**Client Question**: "NFR is part of RID (Requirement). Should it exist at Epic/Initiative level? Is it a Constraint (CON)?"

**Analysis**:
*   **Levels**: **YES**. `NFRs` exist at all levels.
    *   `I-NFR` (Initiative): "System-wide 99.9% Availability."
    *   `E-NFR` (Epic): "Payment Module must handle 10k TPS."
    *   `F-NFR` (Feature): "Login response < 200ms."
*   **Overlap with CON**:
    *   `CON` (Constraint): Usually Business or Environmental limitations. (e.g., "Must use AWS", "Budget < $1M", "Deadline Q1").
    *   `NFR` (Quality Attribute): System characteristics. (e.g., "Scalability", "Security", "Reliability").
*   **Distinction**: `CON` limits choices. `NFR` defines qualities.
*   **Categorization**: Both are **RID (Requirements)**. Keep them distinct tokens to separate "Governance Constraints" from "Technical Qualities."

#### 4. Token Scope Review (FR-002)
**Client Question**: Review Allowed Scope for tokens (I, E, F, S).

**Validation**:
*   `GDR` (I, E, F): **Correct**. Policies can be global or local.
*   `ADR` (I, E, F): **Correct**. Architecture acts at all levels.
*   `ASSUM` (I, E): **Likely F too**. Features make assumptions (e.g., "Assuming API X is ready"). **Recommendation: Add F.**
*   `CON` (I, E): **Likely F too**. Features have constraints. **Recommendation: Add F.**
*   `QG` (I, E): **Correct**. Quality Goals are typically high-level management targets. Feature-level `QGs` are just `NFRs/ACs`.
*   `FR` (F, S): **Correct**. Functional Requirements belong to the specific buildable units.
*   `NFR` (F, S): **Incorrect**. `NFRs` apply globally (Initiative) and locally. **Recommendation: Add I, E.**
*   `IG` (I, E, F): **Correct**. Guidance is fractal.
*   `INT` (F): **Debatable**. As per Q2, if replacing with `IG`, moot. If keeping, Epic level needs integration too.

#### 5. ADR vs. IG/FR Tokens (The "Specification" Pattern)
**Client Question**: "ADR > IID (IG > FR)? If we have a detailed ADR (like T102-STD-005) with FRs inside, do we need separate IG/FR? Is existing usage of 'FR' inside ADRs confusing?"

**Analysis**:
*   **The Pattern**: `T102-STD-005` is a **Governance Standard Document** disguised as an `ADR`.
    *   It contains **Rules** (which it calls `FRs`). In this context, `FR-001` means "Functional Rule 001", not "Functional Requirement of the Software".
*   **Confusion Risk**: **High**. Using `FR` for "Governance Rules" AND "Software Requirements" confuses agents and people.
*   **Recommendation**:
    *   **Rename Inner Rules**: In a Governance ADR/Standard, use `STD` (Standard) or `RULE` tokens, NOT `FR`.
    *   **Example**: `T102-STD-005-RULE-001`.
*   **Software FRs**: Reserve `FR` token strictly for "Software Functional Requirements" (e.g., "User clicks button").
*   **Detail Balance**:
    *   `ADR` should record the **Decision** ("We will use Regex IDs").
    *   `IG` (or `STD`) contains the **Specification** (The Regex itself).
    *   **Best Practice**: ADR decides, IG specifies. `ADR-005` decides "We adopt Standard X". `IG-005` defines Standard X.
*   **Transitional fix**: If keeping the spec inside the `ADR` (as you are), clarify that these `FRs` are **Policy Rules**, distinct from Software Requirements.

---

## IV. Research Findings
*From `report_T102A-SPS_sps-workflow-optimization.md`*

The review of the Workflow Optimization report yields findings that directly support the governance refactor:
*   **Traceability over Duplication**: "Use references rather than duplication to manage traceability."
    *   **Support**: Validates `T102-STD-005-FR-004` (Reference Semantics).
*   **Standardized ID Schemes**: Explicit support for `FR-` (Functional), `ASSUM-` (Assumption) prefixing as an industry best practice (ISO 29148).
    *   **Support**: Validates the Token Taxonomy approach in `FR-002`.
*   **Decision Logging**: Identifying `GDR/ADR` structures (Context, Decision, Consequences) as a "strong implementation pattern."
    *   **Support**: Reinforces the need to keep `DRID` structure strict (`FR-006` Content Quality).
*   **Handoff Quality**: The need for "clear objectives and scope" at handoff reinforces that `RIDs` (Scope/Objectives) must be stable and precise.

---

## V. Consolidated Recommendations for T102-STD-005 Refactor

### 1. Precedence & Governance Layout
*   **Explicit Precedence Chain**: `SID (Goal) > RESID (Truth) > RID (Law: CON/NFR/GDR) > IID (Execution: IG/FR)`.
*   **Note**: `GDR` acts as Law (`RID` level). `ADR` acts as Execution Policy (`IID` level).
*   **Reference Logic**: Clarify that `RES` and `NOTE` are Contextual References, not Normative Dependencies.

### 2. Taxonomy & Token Adjustments
*   **RES $\to$ RESID** (Evidence Category). Update Type to `RESID` (Evidence).
*   **Move NFR & IF to RID Category**: Both represent Requirements or Contracts, not just execution guidance.
*   **NFR Scopes**: Allow Scopes `I, E, F, S` to cover the system-wide to story-level hierarchy.
*   **ASSUM/CON Scopes**: Allow Scope `F` (Features) as features regularly carry local assumptions/constraints.
*   **Consolidate INT $\to$ IG**: Merge `INT` (Integration) into `IG` to reduce token bloat. Use descriptive titles/tags to identify cross-epic or cross-feature patterns.

### 3. Naming & Content Quality
*   **Refinement of Category Semantics**: Split `ASSUM` out if the table schema and lifecycle rules are hefty to maintain rigor.
*   **Expand IG Scope**: Explicitly allow `IG` at Initiative/Epic levels for standards enforcement.
*   **Policy Naming**: Rename inner "FRs" within Governance Standard ADRs to `RULE` or `STD` (e.g., `T102-STD-005-RULE-001`) to prevent confusion with Software Requirements.
*   **Detail Balance**: Maintain the pattern where the `ADR` records the decision to adopt a standard, while the `IG/STD` contains the actual technical specification.
