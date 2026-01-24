## III. CORE CONTENT

### A. FEATURE SOLUTION FRAMEWORK
#### 1. Problem Recap & Constraints
##### i. Problem & Desired Outcome (from Request)
##### ii. Epic-Level Constraints & NFRs (from Index)
##### iii. Feature-Specific Assumptions

#### 2. Decision Criteria & Weights
##### i. Criteria List (names, definitions)
##### ii. Weighting Method (sum = 1.0)

#### 3. Solution Options (incl. O0 “Status Quo / Do Nothing”)
##### i. O0 — Status Quo (baseline)
##### ii. O1 — Option name
##### iii. O2 — Option name
##### iv. O3 — Option name (optional)
- For each option: assumptions, impacts, risks, traceability notes

#### 4. Objective Comparison Matrix & Sensitivity Check
- One table with scores × weights and totals
- Alternate weighting scenario(s) and effect on ranking

#### 5. Conceptual Architecture (views)
- C4 Context & Container views for recommended + runner-up
- Interfaces/integration points (bulleted)

#### 6. Dependency Map & Story Coupling Groups (SCGs)
- Cross-story dependencies, coupling clusters, known ripple zones

#### 7. Recommendation & Rationale
- Primary recommendation, runner-up, risks accepted, next validations (if any)

#### 8. Gate C1 — Framework Approval
- Decision owner, date, notes

---

### B. STORY-LEVEL DESIGN RECORDS (ITERATIVE)
#### 1. Story S# — Title
##### i. Header
- Story ID(s) (from Request), Status {Draft|Proposed|Approved|Rework}, Stability {Draft|Soft-Lock|Frozen}
##### ii. Context & Dependencies
- Inbound/outbound links, SCG membership
##### iii. Proposed Design
- Structure/fields/contract; authoring guidance/Instructions where applicable
##### iv. Traceability
- FR/NFR/AC coverage from Request; related ADRs
##### v. Mini-ADR
- Context → Decision → Consequences → Alternatives
##### vi. Ripple Test Notes
- What regression/slice test proves no breakage (if applicable)
##### vii. Approval
- Decision owner, date

#### 2. Story S# — Title
… (repeat for S1..Sn as needed)

#### 9. Gate C2 — Design Complete (All required Story records approved)
#### 10. Gate C3 — Conceptual Agreement (ready for Planner handoff)
