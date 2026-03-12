---
artifact_type: 'COMMUNICATION_BRIEF'
initiative_id: 'T102'
phase_id: 'PH001'
stream_id: 'ST004'
date: '2026-02-10'
status: 'draft'
author: 'LLM_Consultant (T102 / PH001 / ST004)'
decision_owner_role: 'Client'
target_role: 'External Consultant (Independent Reviewer)'
priority: 'HIGH'
subject: 'Second-opinion request — Issues & Risks (I&R) hosting architecture + SPS context-load / modularization implications'
---

# Communication Brief: External Consultant Second Opinion — I&R Hosting Options + SPS Context Load

## 1. Purpose (Why you are receiving this)

The Client is considering a design decision for where **Issues & Risks (I&R)** should be **canonically hosted** across the T102 documentation system, and how that decision interacts with:

1) the Client’s **scanability + maintenance** goals (humans), and  
2) the **LLM context-load / drift** failure modes already observed (agents), and  
3) potential future **modularization** (splitting or annexing parts of SPS and/or registers) impacting downstream T102A development.

An internal research stream (`T102-RES-004`, `T102-RES-006`) has been executed, but the Client is experiencing decision friction because the quantitative matrix in RES-004 produced **equal total scores** for multiple options while still recommending a specific default.

This brief requests an **independent second-opinion review** (high-level, unbiased) and a **re-grading** of the hosting options to help the Client select a baseline architecture and a near-term execution path.

## 2. What “canonically hosted” means in this request

For the purposes of this decision:

- **Canonical hosting** = the source of truth for lifecycle fields (Status, dates, closure/mitigation notes) and the authoritative row set.
- **Aggregation dashboard** = a roll-up / index view that may link to canonical rows but SHOULD NOT duplicate canonical content.
- **Embedded minimum viable** = small local sections required for contextual emphasis, but governed by “link-don’t-duplicate” rules.

Your review should explicitly distinguish these three concepts, because some options mix them (e.g., “Concept roll-up” is not the same as “Concept canonical”).

## 3. Core Problem Statement (Client confusion to resolve)

### 3.1. The conflict in `T102-RES-004`

In `T102-RES-004` Topic 4 (Hosting Options Comparison Matrix), three options achieved **equal totals** under the report’s equal-weight scoring:

- **(a) SPS-only** — total 19/25 (Recommended default in RES-004)
- **(c) SPS + Concept** — total 19/25 (Conditional enhancement in RES-004)
- **(e) Dedicated register** — total 19/25 (Marked PIVOT/Optional in RES-004)

Despite the tie, the report recommends (a) as the baseline default, and (c) as a conditional enhancement.

The Client’s concern: **if scores tie, the recommendation feels under-justified**, and the matrix does not give the Client a decisive basis for selection.

### 3.2. “Option (f)” requested by the Client (not in RES-004)

The Client has additionally requested an option not explicitly scored in RES-004:

- **(f) Concept-only canonical hosting**:
  - Canonical I&R lives in a dedicated register file (or Concept itself),
  - That register is **linked only from Concept** (not SPS),
  - SPS would not be the canonical host for I&R (and might not include full I&R tables).

This may be interpreted as:
- a variant of (e) Dedicated register, but with Concept as the *only* “front door” for navigation and discovery, or
- a stronger form of (c) SPS + Concept, where Concept becomes canonical rather than aggregation-only.

Your review should define (f) precisely, then score it alongside (a)/(c)/(e).

## 4. Evidence Packet (Repo artifacts to review)

### 4.1. Primary research reports (raw)

- `prompt/artifacts/tasks/T102/research/T102-RES-004/report_T102-RES-004_issues-risks-architecture.md`
- `prompt/artifacts/tasks/T102/research/T102-RES-006/report_T102-RES-006_concept-role-dynamic-registers.md`

### 4.2. Internal synthesis / integration analyses (important for context)

Client specifically requests inclusion and consideration of:

- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-004_issues-risks-architecture.md`

Additional relevant synthesis:
- `prompt/artifacts/tasks/T102/workspace/PH000/analysis/analysis_T102-RES-006_integration-impact.md`

### 4.3. Normative constraints (standards)

- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-007_issues-risks-index.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-003_explicit-inheritance-model.md`
- `prompt/artifacts/tasks/T102/standard/standard_T102-STD-006_research-artifacts-index.md` (register architecture precedent)
- `prompt/artifacts/tasks/T102/T102C/standard/standard_T102C-STD-001_concept-architectural-framework.md`

### 4.4. Current SSOT surfaces (to understand practical drift + bloat)

- SPS: `prompt/artifacts/tasks/T102/ssot/sps_T102-CONSULTANT.md`
- Concept: `prompt/artifacts/tasks/T102/ssot/concept_T102-CONSULTANT.md`
- Feature Request exemplar (contains feature-level I&R): `prompt/artifacts/tasks/T102/T102B/ssot/request_T102B1-RST.md`

## 5. What the internal research currently claims (summary, not an instruction)

### 5.1. RES-004 current posture (as written)

RES-004 proposes:
- Baseline: **(a) SPS-only canonical hosting** for Initiative + Epic I&R
- Feature-level I&R: **remove-by-default** (with optional exceptions / thresholding)
- Concept: may become an **aggregation/dashboard enhancement** (not necessarily canonical)
- Dedicated register: viable, but treated as **optional/pivot** (not selected as default)

RES-004 also identifies governance gaps requiring changes to `T102-STD-007` to make any “remove-by-default at feature scope” posture decision-ready.

### 5.2. RES-006 posture relevant to I&R

RES-006 positions Concept as a **hub-first with thresholds** coordination/audit surface and treats I&R in Concept as:

- **Conditional** and
- **Aggregation-only dashboard**, not canonical hosting

The rationale given is that Concept already shows “drift” failure modes (broken links, extraction/tooling expectation mismatches), so making it canonical for dynamic registers without maintenance hardening increases risk.

## 6. The decision that the Client needs to make (what you should help decide)

### 6.1. Primary decision

Select the baseline **canonical hosting architecture** for I&R for T102:

- (a) SPS-only canonical
- (c) SPS canonical + Concept aggregation dashboard
- (e) Dedicated register canonical (with SPS and/or Concept as front doors)
- (f) Concept-only canonical (Client-proposed; define precisely)

### 6.2. Secondary decisions (should be addressed as part of the recommendation)

1) **Feature-level I&R default posture**
   - Embedded in every feature request by default, or remove-by-default with thresholds/exceptions.

2) **How to manage “SPS context load / bloat”**
   - Keep SPS monolithic but reduce duplication via strict pointer rules, or
   - Split epic dossiers into modular files, or
   - Create annex/register artifacts for register-like content.

3) **Operational reliability requirement**
   - Which surface(s) must be treated as “audit-grade reliable”, and what minimum maintenance protocol is assumed.

## 7. Your requested deliverable (what to send back)

Please provide a short, decision-ready second opinion containing:

### 7.1. A revised scoring matrix

Re-grade (a), (c), (e), and (f) with:
- Your chosen rubric (you may reuse RES-004’s criteria, but you are encouraged to improve it)
- Explicit weights (do not assume equal weights unless you justify why)
- A short explanation for each score (1–2 sentences per criterion per option is sufficient)

If you choose to keep equal weights, include explicit tie-break rules (see next section).

### 7.2. Tie-breaker criteria (required)

If totals tie (again), provide at least 3 tie-breakers such as:

1) **Operational failure mode risk** (drift, broken-link probability, tool friction)
2) **Governance enforceability** (how easily `T102-STD-007` can be amended to match reality without introducing contradictions)
3) **Context-load resilience** (how well the option scales with 5–10+ epics/features without becoming unusable for humans or agents)

### 7.3. A recommendation + rationale

Recommend:
- a baseline option to adopt now, and
- whether any other option should be treated as a later enhancement (and what triggers would justify upgrading).

### 7.4. Minimal transition plan (1 page max)

Provide a “least disruption” transition plan including:
- what must change immediately (if anything),
- what can be deferred,
- what standards must be amended (if any), and
- what acceptance criteria would indicate the architecture is “working”.

## 8. Key risks you should explicitly consider (from observed repo reality)

### 8.1. Standards vs reality mismatch

`T102-STD-007-CLAUSE-001` currently implies Issues & Risks “must be available for each scope across all artifacts”, while current artifacts do not consistently implement this (Concept in particular does not currently host an I&R section/register).

Any recommendation should state whether you interpret CLAUSE-001 as:
- a strict requirement that must be implemented as written, or
- a spec that should be amended to reflect a “canonical vs aggregation vs local emphasis” model.

### 8.2. Concept reliability and “dynamic register” risk

RES-006 documents reliability/drift issues in Concept (register links, extraction expectations). If you recommend Concept as canonical (Option f), you should also specify the minimum governance/maintenance protocol needed to prevent Concept becoming an unreliable audit surface.

### 8.3. SPS bloat / context overload pressure

SPS already carries:
- initiative-level I&R,
- per-epic I&R tables,
- research tables,
- WBS/roadmap content,
and other governance items.

This has already been captured as monitored risks in SPS (e.g., `T102A-RISK-003 (Document Bloat)`, `T102C-RISK-001 (Context Overload)`, `T102-RISK-004 (Documentation Bloat)`). Your recommendation should make clear whether your choice reduces or increases the probability of SPS becoming unmanageable.

## 9. How this interacts with T102A downstream planning (why modularization matters)

T102A is the SPS epic responsible for the SPS structural/procedural system; therefore:

- If I&R remains canonical in SPS and SPS remains monolithic, **T102A must anticipate context scaling** and may need modularization triggers (e.g., “split epic dossiers to separate files once SPS exceeds X size or Y epics/features”).
- If I&R becomes canonical outside SPS (dedicated register or Concept-only), **T102A must define how SPS stays decision-ready** without losing executive visibility.
- If Concept becomes the “hub”, **T102A must assume Concept maintenance becomes part of the operating model** (even if managed by T102C in practice).

Your response should state the expected downstream implications for how T102A should structure SPS documents and what “modularization” means in practice (split files vs annex vs dashboard).

## 10. Administrative notes

- This request is for an **independent second opinion**; you are not being asked to implement changes in-repo.
- The Client remains the decision owner for adopting any option and for approving any resulting standards amendments.
