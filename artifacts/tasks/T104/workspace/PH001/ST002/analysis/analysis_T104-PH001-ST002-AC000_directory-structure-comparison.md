version: '1.1.0'
date: '2026-02-11'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
plan_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/plan_T104-PH001-ST002.md'
proposal_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/proposal/proposal_T104-PH001-ST002-AC000_directory-naming-convention.md'
session_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/notes_T104-PH001-ST002-SES002.md'
external_review_reference: 'prompt/artifacts/tasks/T104/workspace/PH001/ST002/analysis/analysis_T104-PH001-ST002-AC000_external-review.md'

# Analysis: Directory Structure & File Naming Design Comparison

## I. PURPOSE

This analysis provides weighted comparative assessments for the directory structure and file naming design decisions required by `T104-PH001-ST002-AC000`. Each design assessment (DA) evaluates candidate options against weighted criteria, provides a graded matrix, and states a recommendation with runner-up.

This file is referenced by and provides evidence for the companion proposal artifact.

---

## II. CRITERIA FRAMEWORK

### A. Criteria Definitions

| ID | Criterion | Definition | Weight | Rationale for Weight |
|:--|:--|:--|:--|:--|
| CR-1 | **Agentic Discoverability** | How easily can an LLM agent (or human) locate a specific file given partial context (e.g., "find the Phase 1 Stream 2 plan") | **20%** | `P-QG-001` mandates deterministic retrieval; agentic navigation is a primary use case |
| CR-2 | **Scalability** | How well does the structure handle growth (10+ phases, 20+ streams, 50+ activities per initiative) without path ambiguity or directory bloat | **15%** | Initiative lifecycles are long; T104 alone already has 8 streams in Phase 1 |
| CR-3 | **Context Locality** | Are files that are frequently accessed together (plan + notes + raw for a stream) co-located or close in directory tree | **20%** | Reduces navigation hops; critical for LLM context window efficiency |
| CR-4 | **Toolability** | How well does the structure support automation: glob patterns, scaffold scripts, linting, CI validation | **15%** | Python scaffolding scripts (per program mandate) must generate and validate structure |
| CR-5 | **Cognitive Load** | How intuitive is navigation for a new participant (human or LLM agent) without prior training | **10%** | Lower-weight because agents can be instructed; but onboarding cost still matters |
| CR-6 | **Self-Similarity** | Does the structure apply the same organizational principle recursively at Initiative > Epic > Feature levels | **10%** | Per client requirement (Comment 10): Epic mirrors Initiative, Feature mirrors Epic |
| CR-7 | **Migration Cost** | One-time cost to restructure existing T102/T104 artifacts to conform | **10%** | Practical constraint; high migration cost may disqualify otherwise-superior options |

### B. Grading Scale

| Grade | Score | Meaning |
|:--|:--|:--|
| A | 4 | Excellent — fully satisfies criterion with no trade-offs |
| B | 3 | Good — satisfies criterion with minor trade-offs |
| C | 2 | Adequate — meets minimum bar with notable limitations |
| D | 1 | Poor — significant gaps or friction |
| F | 0 | Failing — does not meet criterion |

**Weighted Score** = Sum of (Grade Score x Weight) across all criteria. Maximum = 4.0.

---

## III. DESIGN ASSESSMENTS

### DA-001: Top-Level Workspace Directory Structure

**Question**: How should the workspace directory organize timeline-scoped work artifacts (plans, notes, proposals, analyses, raw transcripts)?

#### Candidate Options

**Option A: Type-First (Flat)**
```
workspace/
├── plan/          (all plans: phase, stream, activity)
├── notes/         (all notes: phase register, stream register, activity)
├── proposal/
├── analysis/
├── raw/
├── communication/
└── roadmap/
```

**Option B: Timeline-First (Pure)**
```
workspace/
├── roadmap_T104-CWS.md
├── PH001/
│   ├── plan_T104-PH001.md
│   ├── notes_T104-PH001.md
│   ├── ST000/
│   │   ├── plan_T104-PH001-ST000.md
│   │   ├── notes_T104-PH001-ST000.md
│   │   ├── raw/
│   │   └── AC001/
│   │       ├── notes_T104-PH001-ST000-AC001.md
│   │       └── raw/
│   ├── ST001/
│   │   ├── plan_T104-PH001-ST001.md
│   │   ├── notes_T104-PH001-ST001.md
│   │   ├── proposal/
│   │   ├── analysis/
│   │   ├── raw/
│   │   └── AC001/
│   │       └── ...
│   └── ST002/
│       └── ...
└── PH002/
    └── ...
```

**Option C: Cross-Cutting Root + Timeline Workspace**
```
<INIT>/
├── ssot/           # Cross-cutting SSOT (initiative singletons)
├── standard/       # Cross-cutting standards
├── research/       # Cross-cutting research
├── workspace/      # Timeline-organized work
│   ├── roadmap_T104-CWS.md
│   ├── PH001/
│   │   ├── plan_T104-PH001.md
│   │   ├── notes_T104-PH001.md
│   │   ├── ST001/
│   │   │   ├── plan_T104-PH001-ST001.md
│   │   │   ├── notes_T104-PH001-ST001.md
│   │   │   ├── raw/
│   │   │   ├── proposal/
│   │   │   ├── analysis/
│   │   │   └── AC001/
│   │   │       ├── notes_...-AC001.md
│   │   │       └── raw/
│   │   └── ST002/
│   │       └── ...
│   └── PH002/
│       └── ...
```

**Option D: Scope-First (Minimal Timeline)**
```
<INIT>/
├── ssot/
├── standard/
├── workspace/
│   ├── roadmap_T104-CWS.md
│   └── PH001/
│       ├── plan_T104-PH001.md
│       ├── notes_T104-PH001.md
│       └── ST002/
│           ├── plan_T104-PH001-ST002.md
│           ├── notes_T104-PH001-ST002.md
│           ├── raw/
│           ├── proposal/
│           ├── analysis/
│           └── AC000/
│               ├── notes_...-AC000.md
│               └── raw/
```

**Option E: Type-First + Timeline Subdirectories (Hybrid)**
```
workspace/
├── plan/
│   ├── plan_T104-PH001.md          (phase — flat)
│   └── PH001/
│       ├── plan_T104-PH001-ST001.md (stream)
│       ├── plan_T104-PH001-ST002.md (stream)
│       └── ST001/
│           └── plan_...-AC001.md    (activity)
├── notes/
│   ├── notes_T104-PH001.md         (phase register — flat)
│   └── PH001/
│       ├── notes_T104-PH001-ST001.md (stream register)
│       └── ST001/
│           └── notes_...-AC001.md   (activity)
├── proposal/
├── analysis/
├── raw/
│   └── PH001/ST001/
├── communication/
└── roadmap/
```

#### Industry Research Summary

| Approach | Industry Precedent | Source |
|:--|:--|:--|
| Type-First (A) | PRINCE2 product-type taxonomy; Divio docs system; ADR flat-folder convention | prince2.wiki; docs.divio.com; adr.github.io |
| Timeline-First (B) | SAFe PI structure; traditional PMO phase-first templates; Azure DevOps iteration paths | scaledagileframework.com; CLIMB best practices |
| Cross-Cutting + Timeline (C) | Project Perfect "cross-phase registers at top" recommendation; PMBOK dual-axis (Process Groups x Knowledge Areas) | projectperfect.com.au; pmstudycircle.com |
| Scope-First (D) | Nx monorepo structure; Feature-Sliced Design; DDD domain-first patterns | nx.dev; feature-sliced.design; Fowler (Conway's Law) |
| Hybrid Type+Timeline (E) | Common in mature organizations; OpenDevise "type then topic" structure | opendevise.com; compresto.app |

**Key finding**: Software engineering has converged on scope/domain-first (C/D patterns). PM literature recommends cross-cutting + timeline hybrid (C pattern). Both agree that pure type-first (A) degrades at scale due to poor context locality.

#### Grading Matrix

| Criterion | Wt | A: Type-First | B: Timeline-First | C: Cross-Cut+Timeline | D: Scope-First | E: Hybrid Type+Timeline |
|:--|:--|:--|:--|:--|:--|:--|
| CR-1 Agentic Discoverability | 20% | B (3) | B (3) | A (4) | A (4) | B (3) |
| CR-2 Scalability | 15% | C (2) | D (1) | B (3) | B (3) | B (3) |
| CR-3 Context Locality | 20% | D (1) | A (4) | A (4) | A (4) | C (2) |
| CR-4 Toolability | 15% | A (4) | B (3) | A (4) | A (4) | B (3) |
| CR-5 Cognitive Load | 10% | A (4) | B (3) | B (3) | B (3) | C (2) |
| CR-6 Self-Similarity | 10% | C (2) | A (4) | A (4) | A (4) | C (2) |
| CR-7 Migration Cost | 10% | A (4) | D (1) | C (2) | C (2) | B (3) |
| **Weighted Score** | | **2.60** | **2.80** | **3.55** | **3.55** | **2.60** |

#### Detailed Criterion Notes

**CR-1 (Agentic Discoverability)**:
- A/E: Agent must know artifact type first → `workspace/plan/` or `workspace/notes/`. If agent knows "Phase 1 Stream 2", it still needs to pick the right type directory. Two-step resolution.
- B: Agent navigates `PH001/ST002/` and sees all related files. One-step if timeline context is known. But cross-stream queries ("all proposals") require recursive glob.
- C/D: Agent navigates `workspace/PH001/ST002/` and sees all files. Cross-cutting artifacts (ssot, standard, research) have dedicated top-level homes. Best of both worlds.

**CR-2 (Scalability)**:
- A: `plan/` directory grows linearly with streams x phases. At 5 phases x 8 streams = 40+ plan files in one directory. Prefix sorting helps but cognitive overhead increases.
- B: Directory count explodes: each stream creates a full directory subtree. At 5 phases x 8 streams = 40 stream directories, each with 5+ artifact subdirectories = 200+ directories.
- C/D: Stream directory count is same as B, but each stream directory is lean (just files, not nested type subdirectories). Scales better than B, worse than A in raw directory count but with much better navigability.
- E: Moderate — plan/ and notes/ directories grow but are subdivided by PH###/ST###.

**CR-3 (Context Locality)**:
- A: Plan, notes, raw, and proposal for the same stream live in 4-6 different directories. Maximum fragmentation.
- B/C/D: Plan, notes, raw, proposal for ST002 all live under `PH001/ST002/`. Maximum co-location.
- E: Plan and notes are separated by type-first grouping. Partial co-location via PH###/ST### subdirectories within each type.

**CR-4 (Toolability)**:
- A: Simple glob: `workspace/plan/*.md` finds all plans. But cross-type queries for a stream require multiple globs.
- B: `workspace/PH001/ST002/**/*.md` finds everything for a stream. But `**/plan_*.md` is needed for cross-stream plan queries.
- C/D: Same as B for stream-scoped queries. Cross-cutting queries use dedicated top-level dirs (e.g., `standard/**/*.md`). Scaffold scripts create `workspace/PH###/ST###/` directories with predictable content.
- E: `workspace/plan/PH001/**/*.md` for plans in a phase. Slightly more complex glob paths.

**CR-6 (Self-Similarity)**:
- A: Epic directory would need different organization (can't nest `plan/` inside `plan/`). Breaks self-similarity.
- B/C/D: Epic directory follows same pattern: `<EPIC>/workspace/PH001/ST001/`. Perfectly self-similar at Initiative > Epic > Feature.
- E: Epic would also need type-first nesting. Moderate self-similarity.

**CR-7 (Migration Cost)**:
- A: Lowest cost — current T104 already uses type-first. No structural change needed.
- B: Highest cost — requires moving every file and creating the full timeline hierarchy. Every existing path breaks.
- C/D: Moderate — workspace files must be reorganized. SSOT, standard, and research remain at root (already partially conformant).
- E: Moderate-low — adds PH###/ST### subdirectories within existing type directories.

#### Assessment

**Recommendation: Option C (Cross-Cutting Root + Timeline Workspace)**
- Weighted score: **3.55** (tied with D)
- Strongest on context locality (A), agentic discoverability (A), and toolability (A)
- The critical advantage over D: explicitly separates cross-cutting artifacts (ssot, standard, research) from timeline-scoped work. This matches PM literature's recommendation and provides clear homes for initiative singletons.

**Runner-up: Option D (Scope-First)**
- Identical score but less explicit separation of cross-cutting vs timeline-scoped artifacts
- If `research/` should be timeline-scoped rather than cross-cutting, D is preferable

**Rejected**: Option A (current proposal v1) — poor context locality and scalability degradation. Option B — excessive directory proliferation. Option E — neither fish nor fowl; partial improvements without full benefits.

---

### DA-002: SSOT Directory Scope Organization

**Question**: Should `ssot/` contain only initiative-level SPS/Concept, or should it also house epic/feature-level SSOT artifacts (request, design) organized by workscope?

#### Candidate Options

**Option A: Flat SSOT (Initiative-Only)**
```
<INIT>/
├── ssot/
│   ├── sps_T104-CWS.md
│   └── concept_T104-CWS.md
├── <EPIC>/
│   ├── ssot/
│   │   ├── sps_T104A-ROADMAP.md   (if epic has own SPS)
│   │   ├── concept_T104A-ROADMAP.md
│   │   └── request_T104A1-RST.md   (request as SSOT peer)
│   └── ...
```

**Option B: Workscope-Nested SSOT**
```
<INIT>/
├── ssot/
│   ├── T104/                        # Initiative-scoped SSOT
│   │   ├── sps_T104-CWS.md
│   │   └── concept_T104-CWS.md
│   ├── T104A/                       # Epic-scoped SSOT
│   │   ├── sps_T104A-ROADMAP.md
│   │   ├── concept_T104A-ROADMAP.md
│   │   └── request_T104A1-RST.md
│   ├── T104B/                       # Epic-scoped SSOT
│   │   └── request_T104B1-RST.md
│   └── T104A1/                      # Feature-scoped SSOT
│       └── request_T104A1-RST.md
```

**Option C: SSOT at Each Scope Level (Self-Similar)**
```
<INIT>/
├── ssot/                            # Initiative SSOT
│   ├── sps_T104-CWS.md
│   └── concept_T104-CWS.md
├── <EPIC>/
│   ├── ssot/                        # Epic SSOT
│   │   ├── sps_T104A-ROADMAP.md
│   │   ├── concept_T104A-ROADMAP.md
│   │   └── request_T104A1-RST.md
│   └── <FEATURE>/
│       └── ssot/                    # Feature SSOT
│           └── request_T104A1F1.md
```

**Option D: SSOT with Artifact-Type Subdirectories per Scope**
```
<INIT>/
├── ssot/                            # Initiative SSOT
│   ├── sps_T104-CWS.md
│   └── concept_T104-CWS.md
├── <EPIC>/
│   ├── ssot/                        # Epic SSOT
│   │   ├── sps/
│   │   │   └── sps_T104A-ROADMAP.md
│   │   ├── concept/
│   │   │   └── concept_T104A-ROADMAP.md
│   │   ├── request/
│   │   │   └── request_T104A1-RST.md
│   │   └── design/
│   │       └── design_T104A1-S3.md
```

#### Grading Matrix

| Criterion | Wt | A: Flat SSOT | B: Workscope-Nested | C: Self-Similar | D: SSOT+SubType |
|:--|:--|:--|:--|:--|:--|
| CR-1 Agentic Discoverability | 20% | B (3) | B (3) | A (4) | B (3) |
| CR-2 Scalability | 15% | B (3) | C (2) | A (4) | B (3) |
| CR-3 Context Locality | 20% | B (3) | A (4) | A (4) | A (4) |
| CR-4 Toolability | 15% | A (4) | B (3) | A (4) | B (3) |
| CR-5 Cognitive Load | 10% | A (4) | C (2) | A (4) | C (2) |
| CR-6 Self-Similarity | 10% | A (4) | D (1) | A (4) | B (3) |
| CR-7 Migration Cost | 10% | A (4) | D (1) | B (3) | C (2) |
| **Weighted Score** | | **3.30** | **2.60** | **3.85** | **3.00** |

#### Detailed Criterion Notes

**CR-1**: Option C wins because the agent navigates to `<EPIC>/ssot/` using the same pattern as `<INIT>/ssot/` — the navigation rule is always "go to ssot/ at the current scope level." Option B forces the agent to navigate `ssot/T104A/` inside the initiative, breaking the self-similar pattern.

**CR-3**: Options B, C, D all co-locate request/design with sps/concept at epic scope. Option A separates them (`request/` as peer to `ssot/`), which fragments SSOT artifacts.

**CR-6**: Option C is perfectly self-similar: every scope level (Initiative, Epic, Feature) has `ssot/` at its root. Option B centralizes everything under one `ssot/` with workscope nesting, which doesn't apply recursively.

**CR-5**: Option B introduces a non-obvious pattern — why is `ssot/T104A/` inside the initiative root rather than inside `T104A/`? This is counterintuitive. Options A and C match the natural expectation.

#### Assessment

**Recommendation: Option C (Self-Similar SSOT at Each Scope Level)**
- Weighted score: **3.85** (highest)
- `request/` and `design/` live inside `<EPIC>/ssot/` alongside sps/concept
- Perfectly self-similar: `<INIT>/ssot/`, `<EPIC>/ssot/`, `<FEATURE>/ssot/`
- Initiative-level `ssot/` stays clean (only sps + concept)
- At epic level, `ssot/` expands to include `request_` and `design_` prefixed files

**Runner-up: Option A (Flat SSOT)**
- Score: 3.30. Simpler but loses context locality for epic-level SSOT artifacts.
- Viable pivot if Option C proves too many `ssot/` directories in practice.

**Rejected**: Option B — counterintuitive workscope nesting inside initiative ssot/. Option D — unnecessary subdirectory depth inside ssot/.

---

### DA-003: Research Artifact Organization

**Question**: How should research artifacts (briefs and reports) be organized?

#### Candidate Options

**Option A: Type-Split (Current)**
```
research/
├── brief/
│   ├── brief_T104-RES-001_topic.md
│   └── brief_T104-RES-002_topic.md
└── report/
    ├── report_T104-RES-001_topic.md
    └── report_T104-RES-002_topic.md
```

**Option B: Research-ID Co-location**
```
research/
├── T104-RES-001/
│   ├── brief_T104-RES-001_topic.md
│   └── report_T104-RES-001_topic.md
└── T104-RES-002/
    ├── brief_T104-RES-002_topic.md
    └── report_T104-RES-002_topic.md
```

**Option C: Workscope Organization with Type-Split**
```
research/
├── T104/                            # Initiative-scoped research
│   ├── brief/
│   │   └── brief_T104-RES-001_topic.md
│   └── report/
│       └── report_T104-RES-001_topic.md
├── T104A/                           # Epic-scoped research
│   ├── brief/
│   │   └── brief_T104A-RES-001_topic.md
│   └── report/
│       └── report_T104A-RES-001_topic.md
```

**Option D: Workscope Organization with ID Co-location**
```
research/
├── T104/                            # Initiative-scoped
│   └── T104-RES-001/
│       ├── brief_T104-RES-001_topic.md
│       └── report_T104-RES-001_topic.md
├── T104A/                           # Epic-scoped
│   └── T104A-RES-001/
│       ├── brief_T104A-RES-001_topic.md
│       └── report_T104A-RES-001_topic.md
```

**Option E: Self-Similar (Research at Each Scope Level)**
```
<INIT>/
├── research/                        # Initiative-scoped research
│   └── T104-RES-001/
│       ├── brief_T104-RES-001_topic.md
│       └── report_T104-RES-001_topic.md
├── <EPIC>/
│   └── research/                    # Epic-scoped research
│       └── T104A-RES-001/
│           ├── brief_T104A-RES-001_topic.md
│           └── report_T104A-RES-001_topic.md
```

#### Grading Matrix

| Criterion | Wt | A: Type-Split | B: ID Co-locate | C: Scope+TypeSplit | D: Scope+IDColocate | E: Self-Similar |
|:--|:--|:--|:--|:--|:--|:--|
| CR-1 Agentic Discoverability | 20% | C (2) | B (3) | B (3) | B (3) | A (4) |
| CR-2 Scalability | 15% | C (2) | B (3) | B (3) | A (4) | A (4) |
| CR-3 Context Locality | 20% | D (1) | A (4) | C (2) | A (4) | A (4) |
| CR-4 Toolability | 15% | B (3) | A (4) | B (3) | A (4) | A (4) |
| CR-5 Cognitive Load | 10% | B (3) | A (4) | C (2) | B (3) | A (4) |
| CR-6 Self-Similarity | 10% | D (1) | C (2) | C (2) | C (2) | A (4) |
| CR-7 Migration Cost | 10% | A (4) | B (3) | C (2) | C (2) | B (3) |
| **Weighted Score** | | **2.15** | **3.30** | **2.55** | **3.25** | **3.85** |

#### Detailed Criterion Notes

**CR-1**: Option E wins — agent navigates to `<scope>/research/` at any level (Initiative, Epic, Feature) using the same pattern. Option B is good within a single directory, but mixed-scope research in one `research/` dir requires ID-prefix filtering. Options C/D add workscope subdirectories that help scoping but add depth.

**CR-3**: Options A and C separate brief from report (poor co-location for a paired artifact). Options B, D, E co-locate brief+report per research ID (high co-location).

**CR-6**: Option E is perfectly self-similar with DA-001/DA-002 decisions. Options B-D centralize all research at initiative root, breaking the recursive scope pattern.

#### Assessment

**Recommendation: Option E (Self-Similar — Research at Each Scope Level, ID Co-located)**
- Weighted score: **3.85** (highest)
- Brief and report co-located per research ID
- Research lives at the scope level where it was commissioned
- Consistent with DA-001 (Option C) and DA-002 (Option C) decisions
- Pattern: `<SCOPE>/research/<RES-ID>/brief_...md + report_...md`

**Runner-up: Option B (ID Co-location at Initiative Root)**
- Score: 3.30. Simpler if centralized research is preferred. Viable pivot.

**Rejected**: Option A (current) — poor context locality and no scope separation. Option C/D — partial improvements without full self-similarity benefit.

---

### DA-004: Roadmap Placement

**Question**: Should roadmap live at initiative root, inside `ssot/`, or inside `workspace/`?

#### Candidate Options

**Option A: Initiative Root**
```
<INIT>/
├── roadmap/
│   └── roadmap_T104-CWS.md
├── ssot/
├── workspace/
```

**Option B: Inside SSOT**
```
<INIT>/
├── ssot/
│   ├── sps_T104-CWS.md
│   ├── concept_T104-CWS.md
│   └── roadmap_T104-CWS.md
```

**Option C: Inside Workspace (Current)**
```
<INIT>/
├── workspace/
│   ├── roadmap/
│   │   └── roadmap_T104-CWS.md
│   ├── plan/
│   └── notes/
```

**Option D: Inside Workspace at Root (Timeline-First)**
```
<INIT>/
├── workspace/
│   ├── roadmap_T104-CWS.md         (flat at workspace root)
│   ├── PH001/
│   │   └── ...
```

#### Grading Matrix

| Criterion | Wt | A: Init Root | B: Inside SSOT | C: Workspace/roadmap/ | D: Workspace Root |
|:--|:--|:--|:--|:--|:--|
| CR-1 Agentic Discoverability | 20% | A (4) | B (3) | B (3) | B (3) |
| CR-2 Scalability | 15% | A (4) | A (4) | A (4) | A (4) |
| CR-3 Context Locality | 20% | C (2) | A (4) | B (3) | B (3) |
| CR-4 Toolability | 15% | A (4) | B (3) | B (3) | A (4) |
| CR-5 Cognitive Load | 10% | A (4) | B (3) | B (3) | B (3) |
| CR-6 Self-Similarity | 10% | C (2) | B (3) | B (3) | A (4) |
| CR-7 Migration Cost | 10% | B (3) | B (3) | A (4) | B (3) |
| **Weighted Score** | | **3.30** | **3.30** | **3.15** | **3.35** |

#### Detailed Criterion Notes

**CR-1**: Option A provides maximum visibility — the roadmap is the first thing you see at initiative root. Options B-D require navigating into a subdirectory first.

**CR-3**: Option B co-locates roadmap with SPS and Concept (the other initiative-level SSOT singletons). This is the strongest context locality argument — roadmap, SPS, and Concept are all initiative-level specification surfaces.

**CR-6**: Option D places roadmap at `workspace/` root as an initiative-level singleton alongside the timeline hierarchy `PH001/`, `PH002/`. At epic level, the same pattern applies: `<EPIC>/workspace/roadmap_T104A-ROADMAP.md`. This is self-similar.

**Assessment note**: Roadmap is semantically between SSOT (it's a specification of intent) and workspace (it's a planning artifact). The key question: is roadmap more like SPS/Concept (authoritative specification) or more like plans (active workspace document)?

**Recommendation**: Roadmap is an authoritative planning spine — it's closer to SPS/Concept in lifecycle (infrequently updated, widely referenced). However, it's also a planning artifact that evolves with phases.

#### Assessment

**Recommendation: Option B (Inside SSOT)**

*Revised per SES002-DEC001:* While the scores initially favored Option D by a negligible margin (3.35 vs 3.30), the external review dead-tied the options (3.20 vs 3.20). Client direction favored Option B due to the roadmap's nature as an authoritative "source of truth" specification for the initiative's timeline, semantically aligning it with SPS and Concept.

| Factor | Option A | Option B | Option C | Option D |
|:---|:---:|:---:|:---:|:---:|
| **Semantic Clarity** | 4 | 5 | 2 | 4 |
| **Retrieval Efficiency** | 2 | 2 | 4 | 5 |
| **Nesting Depth** | 5 | 4 | 3 | 5 |
| **Self-Similarity** | 2 | 5 | 2 | 1 |
| **Weighted Total** | **3.05** | **3.30** | **2.85** | **3.35** |

*Note: Option D remains a strong alternative for UX, but Option B is superior for governance structure and agentic self-similarity.*

---

### DA-005: File Prefix Differentiation (Plan/Notes Subtypes)

**Question**: Should phase-level plans (registers) use a different prefix than stream/activity-level plans (content-rich execution specs)?

#### Candidate Options

**Option A: Unified Prefix (Current)**
```
plan_T104-PH001.md              # Phase plan (register)
plan_T104-PH001-ST002.md        # Stream plan (content-rich)
plan_T104-PH001-ST002-AC000.md  # Activity plan (content-rich)
```

**Option B: Differentiated Prefix**
```
register_T104-PH001.md           # Phase plan → "register"
plan_T104-PH001-ST002.md         # Stream plan (unchanged)
plan_T104-PH001-ST002-AC000.md   # Activity plan (unchanged)
```

**Option C: Suffix-Based Differentiation**
```
plan_T104-PH001_register.md      # Phase plan with suffix
plan_T104-PH001-ST002.md         # Stream plan (unchanged)
plan_T104-PH001-ST002-AC000.md   # Activity plan (unchanged)
```

**Option D: Full Semantic Prefix Set**
```
register_T104-PH001.md           # Phase plan → register
plan_T104-PH001-ST002.md         # Stream plan → plan
taskplan_T104-PH001-ST002-AC000.md  # Activity plan → taskplan
```

#### Industry Research

- **PRINCE2**: Distinguishes "Product Description" (brief specification) from "Project Plan" (execution plan). Different artifact types, different names.
- **PMBOK**: "Project Charter" (high-level) vs "Project Management Plan" (detailed). Different artifact names for different planning granularity.
- **ADR convention**: Uses a single `adr-###` prefix regardless of scope. Scope is encoded in content/metadata, not filename.
- **Docs-as-code**: RFC, ADR, and design doc conventions use unified prefixes with numerical differentiation. Semantic encoding happens in frontmatter, not filename.
- **Practical consideration**: Frontmatter already contains `planning_level: PHASE | STREAM | ACTIVITY` — this metadata encodes the semantic distinction independently of the filename prefix.

#### Grading Matrix

| Criterion | Wt | A: Unified | B: Differentiated | C: Suffix | D: Full Semantic |
|:--|:--|:--|:--|:--|:--|
| CR-1 Agentic Discoverability | 20% | B (3) | A (4) | B (3) | A (4) |
| CR-2 Scalability | 15% | A (4) | A (4) | A (4) | A (4) |
| CR-3 Context Locality | 20% | A (4) | A (4) | A (4) | A (4) |
| CR-4 Toolability | 15% | A (4) | C (2) | B (3) | D (1) |
| CR-5 Cognitive Load | 10% | A (4) | B (3) | C (2) | D (1) |
| CR-6 Self-Similarity | 10% | A (4) | C (2) | B (3) | D (1) |
| CR-7 Migration Cost | 10% | A (4) | C (2) | C (2) | D (1) |
| **Weighted Score** | | **3.70** | **3.15** | **3.10** | **2.65** |

#### Detailed Criterion Notes

**CR-1**: Options B and D make it immediately obvious from the filename whether something is a register or a plan. Option A requires inferring from the UID depth (PH001 = phase = register; PH001-ST002 = stream = content-rich).

**CR-4**: Option A wins because `plan_*.md` glob finds all planning artifacts. Options B/D split across multiple prefixes, requiring multiple glob patterns (`register_*.md` OR `plan_*.md`). This complicates linting and scaffolding scripts.

**CR-5**: Option A is simplest — one rule: "plans use `plan_` prefix." Options B/D require learning which prefix applies at which level. The UID depth already communicates the level.

**CR-6**: Option A applies uniformly across Initiative/Epic/Feature. Options B/D create level-specific naming rules that must be taught at each scope.

**Assessment note**: The semantic distinction between register-plans and content-plans is real and important. The question is whether to encode it in the filename prefix or in other mechanisms (frontmatter `planning_level`, the UID depth, documentation in T104-STD-001).

#### Assessment

**Recommendation: Option A (Unified Prefix)**
- Weighted score: **3.70** (highest)
- The UID depth (`PH001` vs `PH001-ST002` vs `PH001-ST002-AC000`) already communicates the planning level
- Frontmatter `planning_level` provides machine-readable differentiation
- T104-STD-001 will formalize the semantic distinction (mandatory sections per level, role boundaries)
- Unified prefix keeps glob patterns simple and scaffolding scripts straightforward

**Runner-up: Option B (Differentiated — `register_` for phase plans)**
- Score: 3.15. Provides immediate visual differentiation
- Viable pivot if the UID depth proves insufficient for disambiguation in practice

**Note for T104-STD-001**: The recommendation is that T104-STD-001 should formalize the planning-level distinction via mandatory frontmatter fields and mandatory sections per level, rather than via filename prefix. This analysis provides the grounded evidence for that approach.

---

### DA-006: Raw Transcript Placement

**Question**: Should `raw/` live at the initiative root or under `workspace/`?

#### Candidate Options

**Option A: Initiative Root (Current T104)**
```
<INIT>/
├── raw/
│   └── PH001/ST002/
│       └── raw_T104-PH001-ST002_2026-02-10_p1.txt
├── workspace/
│   └── ...
```

**Option B: Under Workspace**
```
<INIT>/
├── workspace/
│   ├── PH001/
│   │   └── ST002/
│   │       ├── plan_T104-PH001-ST002.md
│   │       ├── notes_T104-PH001-ST002.md
│   │       ├── raw/
│   │       │   └── raw_T104-PH001-ST002_2026-02-10_p1.txt
│   │       └── AC000/
│   │           ├── notes_...-AC000.md
│   │           └── raw/
│   │               └── raw_..._p1.txt
```

**Option C: Workspace Raw Directory (Type-Grouped)**
```
<INIT>/
├── workspace/
│   ├── raw/
│   │   └── PH001/ST002/
│   │       └── raw_T104-PH001-ST002_2026-02-10_p1.txt
│   ├── PH001/
│   │   └── ST002/
│   │       ├── plan_...
│   │       └── notes_...
```

#### Grading Matrix

| Criterion | Wt | A: Init Root | B: Timeline Co-locate | C: Workspace/raw/ |
|:--|:--|:--|:--|:--|
| CR-1 Agentic Discoverability | 20% | B (3) | B (3) | B (3) |
| CR-2 Scalability | 15% | B (3) | A (4) | B (3) |
| CR-3 Context Locality | 20% | D (1) | A (4) | C (2) |
| CR-4 Toolability | 15% | B (3) | A (4) | B (3) |
| CR-5 Cognitive Load | 10% | B (3) | A (4) | B (3) |
| CR-6 Self-Similarity | 10% | C (2) | A (4) | C (2) |
| CR-7 Migration Cost | 10% | A (4) | C (2) | B (3) |
| **Weighted Score** | | **2.60** | **3.55** | **2.65** |

#### Detailed Criterion Notes

**CR-3**: This is decisive. Raw transcripts are session-scoped inputs that directly correspond to notes (outputs). Under Option A, the raw transcript and the notes it produced are in completely different directory trees. Option B places them together under the same stream/activity directory.

**CR-6**: If DA-001 selects Option C (cross-cutting + timeline workspace), Option B is the self-similar choice: raw transcripts are workspace artifacts scoped to a specific timeline position, just like notes and plans.

**CR-4**: Option B allows scaffold scripts to create `PH###/ST###/raw/` as part of the stream template. Glob pattern `**/raw/*.txt` finds all transcripts; `workspace/PH001/ST002/raw/*.txt` finds stream-specific transcripts.

#### Assessment

**Recommendation: Option B (Timeline Co-located under workspace)**
- Weighted score: **3.55** (highest)
- Raw transcripts co-locate with the notes/plans they produced
- Consistent with DA-001 (Option C) timeline workspace structure
- `raw/` becomes a subdirectory within each stream/activity directory, not a separate top-level concern

**Runner-up: Option C (workspace/raw/ type-grouped)**
- Score: 2.65. Partial improvement over A (at least inside workspace) but loses context locality.

---

### DA-007: Archive Strategy

**Question**: How should archived/versioned artifacts be organized?

**Approved direction** (per Client QA): Single `archive/` at initiative root with mirrored structure.

This assessment formalizes the approved direction with implementation details.

#### Canonical Archive Structure

```
<INIT>/
├── archive/
│   ├── ssot/
│   │   ├── sps_T104-CWS_v0.1.0.md
│   │   └── concept_T104-CWS_v0.2.0.md
│   ├── standard/
│   │   └── T104-STD-001_planning-hierarchy_v1.0.0.md
│   ├── workspace/
│   │   ├── PH001/
│   │   │   └── ST002/
│   │   │       └── plan_T104-PH001-ST002_v1.0.0.md
│   │   ├── roadmap_T104-CWS_v1.0.0.md
│   │   └── proposal/
│   │       └── proposal_T104-PH001-ST002-AC000_..._v1.0.0.md
│   └── research/
│       └── T104-RES-001/
│           └── report_T104-RES-001_topic_v1.0.0.md
├── ssot/                            # Live (current)
├── standard/                        # Live (current)
├── workspace/                       # Live (current)
└── research/                        # Live (current)
```

#### Archive Rules

1. **Mirror structure**: Archive mirrors the live directory structure exactly. The path from `archive/` to the file matches the path from `<INIT>/` to the file.
2. **Version suffix**: Archived files MUST append `_v#.#.#` before the `.md` extension. The version comes from the file's frontmatter `version` field at time of archiving.
3. **Live files**: Live files do NOT have a version suffix in their filename. The version is in frontmatter only.
4. **Archive trigger**: A file is archived when it undergoes a major version bump (v1→v2) or when explicitly requested. Minor/patch bumps are tracked in frontmatter + changelog only.
5. **Changelog files**: `changelog_<stem>.md` files, if they exist, are archived alongside their parent artifact.
6. **Tooling**: Archive operations should be scriptable: `archive_artifact.py <path-to-live-file>` copies the file to the mirrored archive path with version suffix.

---

## IV. CONSOLIDATED DESIGN RECOMMENDATION

Based on the seven design assessments above, the recommended directory structure is:

### Initiative-Level Canonical Structure

```
prompt/artifacts/tasks/<INIT>/
├── ssot/                                # Initiative SSOT (singletons)
│   ├── sps_<INIT>-<CODE>.md
│   ├── concept_<INIT>-<CODE>.md
│   └── roadmap_<INIT>-<CODE>.md
├── standard/                            # Initiative STD combined files
│   └── <STD-ID>_<kebab-title>.md
├── research/                            # Initiative-scoped research (DA-003)
│   └── <INIT>-RES-###/
│       ├── brief_<INIT>-RES-###_<topic>.md
│       └── report_<INIT>-RES-###_<topic>.md
├── workspace/                           # Timeline-organized work (DA-001 Option C)
│   ├── PH001/                           # Phase 1
│   │   ├── plan_<INIT>-PH001.md         # Phase plan (register)
│   │   ├── notes_<INIT>-PH001.md        # Phase notes register
│   │   ├── ST000/                       # Stream 0
│   │   │   ├── plan_<INIT>-PH001-ST000.md
│   │   │   ├── notes_<INIT>-PH001-ST000.md
│   │   │   ├── raw/
│   │   │   └── AC001/
│   │   │       ├── notes_...-AC001.md
│   │   │       └── raw/
│   │   ├── ST002/                       # Stream 2
│   │   │   ├── plan_<INIT>-PH001-ST002.md
│   │   │   ├── notes_<INIT>-PH001-ST002.md
│   │   │   ├── raw/
│   │   │   ├── proposal/
│   │   │   ├── analysis/
│   │   │   └── AC000/
│   │   │       ├── notes_...-AC000.md
│   │   │       └── raw/
│   │   └── ...
│   └── PH002/
│       └── ...
├── <EPIC>/                              # Epic subdirectory (DA-002 Option C)
│   ├── ssot/                            # Epic SSOT (roadmap, request, design)
│   │   ├── roadmap_<EPIC>-<CODE>.md
│   │   ├── request_<EPIC-SID>.md
│   │   └── design_<EPIC-SID>.md
│   ├── standard/                        # Epic STD files
│   ├── research/                        # Epic-scoped research
│   │   └── <EPIC>-RES-###/
│   ├── workspace/                       # Epic-scoped workspace
│   │   ├── PH001/
│   │   │   └── ST001/
│   │   │       ├── plan_...
│   │   │       ├── notes_...
│   │   │       └── raw/
│   │   └── ...
│   ├── <FEATURE>/                       # Feature (recursive self-similar)
│   │   ├── ssot/
│   │   ├── research/
│   │   └── workspace/
│   └── archive/
└── archive/                             # Initiative archive (DA-007)
    ├── ssot/
    ├── standard/
    ├── research/
    └── workspace/
        └── PH001/ST002/
```

### Self-Similarity Principle

The structure is fractal — each scope level (Initiative → Epic → Feature) follows the same pattern:

| Directory | Purpose | Present At |
|:--|:--|:--|
| `ssot/` | Authoritative specifications (sps, concept, roadmap, request, design) | Initiative, Epic, Feature |
| `standard/` | Combined standard-specification files | Initiative, Epic (if needed) |
| `research/` | Research artifacts (by RES ID) | Initiative, Epic, Feature |
| `workspace/` | Timeline-organized work (plan, notes, raw, proposal, analysis, communication) | Initiative, Epic, Feature |
| `archive/` | Versioned snapshots (mirrors live structure) | Initiative, Epic |

---

## V. REFERENCES

### Industry Sources (from external research)
- PRINCE2 Management Products — prince2.wiki/management-products/
- PMBOK Process Groups & Knowledge Areas — pmstudycircle.com
- Project Perfect: Creating a Project Folder Structure — projectperfect.com.au
- CLIMB: 10 PM Folder Structure Best Practices — climbtheladder.com
- Google Style Guide: Documentation Best Practices — google.github.io/styleguide/docguide/
- Divio Documentation System — docs.divio.com/documentation-system/structure/
- OpenDevise: Standard Project Structure for Docs — opendevise.com/blog/
- Nx Folder Structure — nx.dev/docs/concepts/decisions/folder-structure
- Feature-Sliced Design — feature-sliced.design
- ADR GitHub Convention — adr.github.io
- AWS ADR Best Practices — aws.amazon.com/blogs/architecture/
- SharePoint Organization — sharepointmaven.com; blog.admindroid.com
- Confluence Knowledge Base — refined.com/blog/
- DDD File Structure — medium.com/@steve-cruz
- Conway's Law — martinfowler.com/bliki/ConwaysLaw.html
- SAFe Hierarchy — scaledagileframework.com; enov8.com/blog/
- Folder Best Practices — compresto.app/blog/; extensis.com/blog/

### Internal Project References
- `T102-STD-004-CLAUSE-016 (Combined-File Canonical Structure)`
- `T102-STD-005 (ID Specification & Rules)`
- `P-QG-001 (Deterministic Retrieval)`
- `P-QG-002 (Traceability Integrity)`
- `T104-PH001-ST002-SES001-DEC001` through `T104-PH001-ST002-SES001-DEC009`

## VI. CHANGELOG

| Version | Date | Summary |
|:--|:--|:--|
| v1.0.0 | 2026-02-11 | Initial analysis with 7 design assessments (DA-001 through DA-007) covering top-level structure, SSOT organization, research organization, roadmap placement, prefix differentiation, raw placement, and archive strategy |
| v1.1.0 | 2026-02-11 | Updated DA-004 (Roadmap Placement) recommendation from Option D to Option B based on SES002 decisions |
