---
artifact_type: 'REPORT'
initiative_id: 'P'
research_id: 'P-RES-003'
version: '1.0.0'
iteration: '1'
date: '2026-03-13'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# RESEARCH REPORT: Specification Metadata Governance Research (P-RES-003)

## I. EXECUTIVE SUMMARY

**Context**: `P-STD-001` governs the combined-file structure for program standards but does not currently prescribe a YAML frontmatter schema, an in-file versioning model, or any normative subsection structure inside `## References` and `## Provenance`. The active P-STD files have therefore drifted into different local patterns, while `sps_P-PROGRAM.md` already states in `P-CON-003` that combined standard-specification files shall use YAML frontmatter. The program also relies on repo-native agentic surfaces such as `AGENTS.md` and `CLAUDE.md` wrappers, so the target governance model must work for both formal standards and agent-consumed instruction files.

**Verdict**: **GO**. The research supports standardizing metadata governance in `P-STD-001`, but with a selective pattern: adopt a small authoritative YAML header for current-state metadata, standardize `## References` around a normative/informative taxonomy and a single entry schema, standardize `## Provenance` around a fixed minimum subsection taxonomy, and explicitly define how derivative repo-owned agentic surfaces express scope and authority. A direct copy of large standards-body process machinery would be overfit for this repo; the recommended model is a lighter-weight hybrid grounded in the program's Markdown-primary workflow.[1][4][5][7][10][11][14]

**Key Findings**:
*   **Finding 1**: Structured specification metadata is the norm across W3C/ReSpec, RFC/xml2rfc, ISO public standard records, and IEEE PARs, but none of those ecosystems rely on unstructured narrative alone. The program's current absence of YAML frontmatter on all four active P-STDs is therefore a real governance gap, not merely a stylistic choice.[1][4][6][7]
*   **Finding 2**: Mature standards ecosystems separate current-state metadata from history and references. The best program fit is not "all metadata in YAML" or "all metadata in Provenance"; it is YAML as the authoritative current-state layer and `## Provenance` as the authoritative history/lineage layer, with lint-style consistency checks where fields overlap.[1][3][5]
*   **Finding 3**: The agentic benchmark set is bimodal. Some systems use markdown instruction files with light scoping metadata and hierarchical discovery (`CLAUDE.md`, `AGENTS.md`, Cursor rules, Windsurf rules), while others use explicit structured schemas (GitHub Actions workflows, Copilot path-scoped instructions, MCP tool/prompt/resource objects). The program should adopt a hybrid model that preserves human-readable markdown bodies while adding deterministic machine-readable discovery metadata.[10][11][12][13][14][15][16][17][18][19]

---

## II. METHODOLOGY AUDIT

**Scope Adherence**: Research stayed within the approved brief's recommendations-only boundary. No P-STD-001 CLAUSE text was drafted and no governed artifact structure was modified. Topic coverage includes all 13 brief topics, the required traditional benchmark set, the approved agentic benchmark set, and the Topic 9 cross-surface audit.

**Source of Truth Audit**:
*   **Code base**: Verified the brief's internal packet, `sps_P-PROGRAM.md`, the ST004 and ST001 plans, the four active P-STDs, root and prompt `AGENTS.md`, `.claude/CLAUDE.md`, the four role `CLAUDE_*` wrappers, the four delegated role system files, and the two standard-authoring derivatives (`guideline_standard_specs.md`, `template_standard_specs.md`).
*   **Data Artifacts**: Verified AC003 session notes and the external-review analysis artifact to confirm the approved topic set, the 50/50 traditional-agentic coverage requirement, and the downstream consumer mapping.

**Limitations**:
*   The repo still records `P-PH000-ST004-AC003-GATE-001` as `in_progress` in the stream plan, while this execution proceeded under the user's explicit approval token `APPROVED: RESEARCH`. This is a traceability discrepancy, not an evidence blocker.
*   ISO public pages expose stable publication metadata (status, publication date, edition, committee, ICS), but ISO directives and editorial mechanics are less openly surfaced than W3C and IETF materials. Confidence is therefore higher on ISO metadata-state observations than on ISO internal process detail.[6]
*   Agentic tool documentation is volatile. Retrieval date for Topics 10-13 is 2026-03-13, and those findings should be treated as current-state evidence rather than permanent norms.[10][11][12][13][14][15][16][17][18][19]

---

## III. TOPIC FINDINGS

### Topic 1: Industry YAML/Frontmatter Metadata Schemas
**Objective**: Benchmark how major standards ecosystems structure machine-readable metadata headers for specification documents.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md:1-3`, `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md:1-3`, `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md:1-5`, `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md:1-4`
*   **Observation**: All four active P-STDs begin directly with a title and `## Specification`; none starts with YAML frontmatter.
*   **Source**: `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md:59`
*   **Observation**: `P-CON-003` already says combined standard-specification files shall use Markdown with YAML frontmatter.
*   **Source**: ReSpec documents expose structured config fields such as `specStatus`, `shortName`, `publishDate`, `editors`, `edDraftURI`, `latestVersion`, `previousPublishDate`, and `previousMaturity`, with status-dependent requirements.[1]
*   **Source**: RFC 7991 defines structured `<front>` metadata with `title`, `seriesInfo`, one or more `author` elements, optional `date`, optional `workgroup`, optional `keyword`, plus document-level attributes such as `submissionType`, `consensus`, and `docName`.[4]
*   **Source**: ISO public standard catalogue pages expose structured metadata including `Status`, `Publication date`, `Edition`, `Technical Committee`, and `ICS` classification.[6]
*   **Source**: IEEE SA describes the PAR as a structured document that captures at least title, scope, purpose, need, and stakeholders, with explicit clarity rules enforced by NesCom.[7][8][9]

| Standards Body / System | Primary Structured Metadata Surface | Core Fields Observed | Validation / Controlled Vocabulary Signal | Program-Relevant Takeaway |
| :--- | :--- | :--- | :--- | :--- |
| W3C / ReSpec | ReSpec config block | `specStatus`, `shortName`, `publishDate`, `editors`, `latestVersion`, `edDraftURI` | Status-driven required fields and publish-rule validation | Strong model for compact current-state header |
| IETF / RFC xml2rfc | `<front>` block and document attributes | `title`, `seriesInfo`, `author`, `date`, `workgroup`, `docName`, `submissionType` | Structured vocabulary and ordering rules in RFC 7991 | Strong model for strict identity/publication metadata |
| ISO | Public catalogue record | `Status`, `Publication date`, `Edition`, `Technical Committee`, `ICS` | Stable catalogue fields, weaker open authoring mechanics | Confirms publication-state metadata is always normalized |
| IEEE PAR | PAR form / project metadata | title, scope, purpose, need, stakeholders | NesCom conventions enforce title/scope/purpose clarity | Useful for authority and scope metadata, not full header shape |
| Current P-STD state | None | title only in body; no structured header | None | Confirms current-state governance gap against all benchmarks |

#### B. Analysis
*   **Synthesis**: The external benchmark set does not converge on one syntax, but it does converge on a pattern: current-state metadata is structured, compact, and normalized around identity, lifecycle, ownership, and classification. That makes the program's current "no standard-file frontmatter at all" an outlier rather than a viable equivalent.
*   **Gap Analysis**: Current P-STD state has no structured header despite an SPS-level requirement. The program has the policy without the implementing schema or authority model.

**Comparative Evaluation**

| Option | Program Fit | Industry Alignment | Agentic Operability | Adoption Overhead | Extensibility | Weighted Total |
| :--- | :---: | :---: | :---: | :---: | :---: | ---: |
| Minimal governed YAML header for current-state metadata + narrative Provenance for history | 5 | 4 | 5 | 4 | 4 | 89 |
| Expanded lifecycle-aware YAML header with many conditional fields | 4 | 5 | 4 | 2 | 5 | 79 |
| No YAML header; keep narrative/VCS only | 2 | 2 | 1 | 5 | 2 | 48 |

#### C. Governance Implication
*   **Decision Impact**: `P-STD-001` should gain a new YAML-frontmatter CLAUSE domain defining a compact current-state schema rather than importing a large standards-body metadata set wholesale.
*   **Risk**: `P-CON-003` should be **clarified**, not removed. It is directionally correct, but under-specified without a canonical schema and authority rule.

---

### Topic 2: Mandatory vs Optional Field Taxonomies
**Objective**: Evaluate how standards ecosystems distinguish mandatory, optional, and lifecycle-conditional metadata fields.

#### A. Evidence & Forensics
*   **Source**: ReSpec requires different metadata depending on document status; for example, some statuses require `previousPublishDate` and `previousMaturity`, and review-track states require review end dates.[1]
*   **Source**: RFC 7991 treats some `<front>` components as fixed-order core fields (`title`, `author`, optional `date`) and others as optional extensions such as `workgroup` and `keyword`.[4]
*   **Source**: IEEE NesCom conventions explicitly distinguish required clarity for title, scope, and purpose from other explanatory material such as additional notes.[8]

#### B. Analysis
*   **Synthesis**: The strongest cross-source pattern is three-tiered, not binary: core identity fields, lifecycle-conditional fields, and contextual optional fields.
*   **Gap Analysis**: The program currently has no governed field taxonomy for standards. Artifact frontmatter elsewhere in the repo uses ad hoc sets such as `version`, `date`, `status`, and `author`, but that practice is not yet normalized for P-STDs.

| Recommended Field | Obligation Level | Lifecycle Stage | Rationale |
| :--- | :--- | :--- | :--- |
| `artifact_type`, `initiative_id`, `research_id` or standard ID equivalent | Mandatory | All | Identity and indexing |
| `version`, `date`, `status` | Mandatory | All | Current-state governance baseline |
| `author`, `decision_owner_role` | Mandatory | All | Ownership and review routing |
| `approval_date`, `effective_date` | Conditional | Accepted / active norms | Only meaningful once approved |
| `supersedes`, `superseded_by`, `deprecation_date` | Conditional | Superseded / deprecated | Lifecycle-chain tracking |
| `tags`, `applies_to`, derivative scope metadata | Optional | Where derivative/tool-specific scope exists | Supports agentic retrieval without overloading all standards |

#### C. Governance Implication
*   **Decision Impact**: The recommended P-STD taxonomy is:
    core mandatory fields for every standard file;
    lifecycle-conditional fields for states like `accepted`, `superseded`, or `deprecated`;
    optional contextual fields for implementation detail or derivative-specific needs.
*   **Risk**: Overfilling the header with historical or process metadata would repeat the ISO/IEEE scale mismatch the brief warned about.

---

### Topic 3: Version Tracking Patterns
**Objective**: Evaluate in-file version tracking mechanisms versus VCS-only approaches.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md:645-656`
*   **Observation**: `P-STD-002` already contains `### Amendment History` under `## Provenance`.
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md:498-514`
*   **Observation**: `P-STD-001` records post-promotion amendments only as free-form Provenance table rows, not as a governed revision structure.
*   **Source**: W3C ReSpec and W3C style guidance emphasize latest-version links, previous-version links, dated snapshots, and editor's drafts more than in-body changelog tables.[1][2][3]
*   **Source**: RFCs rely on immutable publication identifiers, `Status of This Memo`, and external errata rather than a living in-body revision table in the published RFC.[4][5]
*   **Source**: IEEE and ISO public records surface approval/publication/edition history externally in catalogues or project records rather than rich changelog sections inside the standard text.[6][7][9]

#### B. Analysis
*   **Synthesis**: Mature standards ecosystems usually separate immutable publication history from the normative body. The program differs because its standards are living repo files under active amendment, so a light in-file history is useful even if traditional bodies do not use it heavily.
*   **Gap Analysis**: Pure VCS history is too opaque for governance review. A large standalone changelog section would add unnecessary ceremony for a 4-6 standard ecosystem.

**Comparative Evaluation**

| Option | Program Fit | Industry Alignment | Agentic Operability | Adoption Overhead | Extensibility | Weighted Total |
| :--- | :---: | :---: | :---: | :---: | :---: | ---: |
| Provenance-embedded amendment history plus VCS backing | 5 | 4 | 4 | 4 | 4 | 85 |
| Standalone revision-history section plus VCS backing | 4 | 4 | 3 | 3 | 4 | 72 |
| VCS-only history, no in-file history | 2 | 3 | 2 | 5 | 3 | 59 |

#### C. Governance Implication
*   **Decision Impact**: Standardize a concise amendment-history subsection inside `## Provenance` and continue to treat git as the authoritative full diff trail.
*   **Risk**: If amendment history is not normalized, later P-STDs will continue to invent local patterns as P-STD-002 already did.

---

### Topic 4: Semantic Versioning in Specification Governance
**Objective**: Evaluate how standards ecosystems version specification documents and what triggers increments.

#### A. Evidence & Forensics
*   **Source**: W3C tracks maturity status and dated publications; RFCs use sequential RFC identifiers; ISO uses edition/publication records; IEEE surfaces standard numbers, years, and PAR/board approval milestones.[1][4][6][7][9]
*   **Source**: Workspace governance artifacts already use semver-style versions such as `v0.8.0`, `v3.1.0`, and `v2.0.0` in plans, SPS files, briefs, and notes.

#### B. Analysis
*   **Synthesis**: Semver is not an external standards-body norm, but it is already an internal governance convention in this repo and is easier to reason about in a living-document environment than edition-only or serial numbering.
*   **Gap Analysis**: The missing piece is not the version format itself; it is the lack of explicit increment triggers for P-STD files.

#### C. Governance Implication
*   **Decision Impact**: Retain semver for program-governed specification files, but frame it as a program governance convention rather than an industry default. Suggested triggers:
    patch = editorial / metadata-only correction;
    minor = normative addition or compatible restructuring;
    major = breaking governance change, section relocation, or schema incompatibility.
*   **Risk**: Without increment rules, semver will drift into arbitrary label usage and lose its audit value.

---

### Topic 5: Provenance Subsection Taxonomy
**Objective**: Evaluate normative provenance/history subsection categories and the role of companion authoring guides.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md:498-514`
*   **Observation**: `P-STD-001` uses a flat table under `## Provenance` with promotion and amendment rows but no subsections.
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md:645-656`
*   **Observation**: `P-STD-002` uses `### Status`, `### Amendment History`, and `### Activity Plan`.
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md:264-275`
*   **Observation**: `P-STD-004` uses `### Status`, `### Seed Source`, `### Activity Plan`, and `### Seed Decision Inputs`.
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md:456-468`
*   **Observation**: `P-STD-005` uses `### Promotion`, `### Input Sources`, and `### Hardening`.
*   **Source**: `prompt/templates/consultant/standards/template_standard_specs.md:34-40`, `prompt/templates/consultant/standards/guideline_standard_specs.md:72-74`
*   **Observation**: The template gives only placeholder dashes under `## References` and `## Provenance`, and the guideline only says those sections must stay STD-level, not how they are structured.
*   **Source**: Standards-body guidance usually normalizes status, publication context, and reference practices more strongly than bespoke provenance subsection taxonomies; that argues for a fixed minimum program taxonomy rather than open-ended prose.[2][3][5][8]

#### B. Analysis
*   **Synthesis**: The internal drift is real and rooted in under-specification. The safest fix is a single minimum taxonomy that can absorb seed, promotion, and hardening cases without creating separate per-lifecycle templates.
*   **Gap Analysis**: Current files preserve useful provenance ideas, but no two files package them the same way.

**Comparative Evaluation**

| Option | Program Fit | Industry Alignment | Agentic Operability | Adoption Overhead | Extensibility | Weighted Total |
| :--- | :---: | :---: | :---: | :---: | :---: | ---: |
| Fixed minimum taxonomy with reusable subsections | 5 | 4 | 4 | 4 | 4 | 85 |
| Lifecycle-specific provenance templates by standard type | 3 | 4 | 3 | 2 | 5 | 65 |
| Flat free-form provenance notes | 2 | 1 | 1 | 5 | 2 | 43 |

#### C. Governance Implication
*   **Decision Impact**: Standardize a minimum `## Provenance` taxonomy with:
    `Status`,
    `Lineage / Authority`,
    `Amendment History`,
    `Input Sources`.
    Additional lifecycle-specific subsections may be allowed only as governed extensions.
*   **Risk**: If AC009 fixes only P-STD-001 and not the template/guideline derivatives, the same drift will recur.

---

### Topic 6: References Section Standardization
**Objective**: Evaluate how references should be categorized and structured.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md:483-487`
*   **Observation**: `P-STD-001` uses `### References (Internal + Cross-Scope: Program → Initiative T102)` and the first column header `Referenced ID`.
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md:632-635`, `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md:254-257`, `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md:445-448`
*   **Observation**: The later standards use `### External References (Cross-Scope)` and the first column header `ID`.
*   **Source**: RFC 7322 explicitly requires references to indicate whether each reference is normative or informative and recommends split sections when both exist.[5]
*   **Source**: W3C/ReSpec supports references as a distinct managed document concern, and ISO standards separately distinguish normative references and bibliography.[1][3][6]

#### B. Analysis
*   **Synthesis**: The strongest cross-standards pattern is normative/informative, not internal/external. Internal vs external still matters in this repo, but it works better as row metadata than as the primary heading split.
*   **Gap Analysis**: The program lacks both a stable section taxonomy and a stable entry schema.

**Comparative Evaluation**

| Option | Program Fit | Industry Alignment | Agentic Operability | Adoption Overhead | Extensibility | Weighted Total |
| :--- | :---: | :---: | :---: | :---: | :---: | ---: |
| Normative/Informative split with typed row schema | 5 | 5 | 4 | 4 | 4 | 90 |
| Single flat references section with type column only | 4 | 4 | 4 | 5 | 3 | 82 |
| Internal/External split as primary taxonomy | 3 | 2 | 3 | 4 | 3 | 59 |

#### C. Governance Implication
*   **Decision Impact**: Standardize `## References` around `Normative References` and `Informative References`, with row fields that can still capture internal/external scope.
*   **Risk**: Leaving `Referenced ID` versus `ID` unresolved would perpetuate avoidable table-schema drift.

---

### Topic 7: Cross-Artifact Traceability Metadata
**Objective**: Evaluate how specifications should embed links to decisions, parent documents, and derivative artifacts.

#### A. Evidence & Forensics
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md:503-514`
*   **Observation**: `P-STD-001` embeds promotion contract and promotion decision links directly in Provenance.
*   **Source**: `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md:457-468`
*   **Observation**: `P-STD-005` embeds promotion activity, input sources, and hardening references in `## Provenance`.
*   **Source**: IEEE PAR and standards project pages expose scope, purpose, need, stakeholders, approval dates, and working-group details through external project records rather than burying full process history in the standard text.[7][8][9]
*   **Source**: RFCs and W3C specifications include publication context and reference links, but the full approval workflow is largely external to the normative body.[3][5]

#### B. Analysis
*   **Synthesis**: The external benchmark supports embedding concise lineage pointers, not full process dossiers, inside the specification itself.
*   **Gap Analysis**: Current P-STDs are directionally correct in keeping lineage inside Provenance, but they do not apply a consistent boundary between "pointer" and "process archive".

#### C. Governance Implication
*   **Decision Impact**: Keep concise lineage pointers in `## Provenance` and keep full gate/process evidence in proposals, plans, verification artifacts, and SPS records.
*   **Risk**: Overloading the standard body with process detail would undermine concision and increase maintenance cost.

---

### Topic 8: Machine-Readable vs Human-Readable Delineation
**Objective**: Define the authority boundary between YAML frontmatter and Provenance narrative.

#### A. Evidence & Forensics
*   **Source**: ReSpec combines structured configuration with generated human-readable publication metadata, effectively treating the structured layer as the driver of the rendered state.[1]
*   **Source**: RFC and catalogue-style ecosystems separate current-state identifiers/publication metadata from explanatory history and status prose.[4][5][6][7]
*   **Source**: `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md:59`
*   **Observation**: The program already requires YAML frontmatter at SPS level but has no rule yet for how it coexists with Provenance.

#### B. Analysis
*   **Synthesis**: The program needs one authoritative current-state layer and one authoritative history layer. The cleanest split is: YAML for the current state used by machines and fast readers; Provenance for history, rationale pointers, and lineage.
*   **Gap Analysis**: Without this split, any future adoption of YAML would simply create duplication and drift.

**Comparative Evaluation**

| Option | Program Fit | Industry Alignment | Agentic Operability | Adoption Overhead | Extensibility | Weighted Total |
| :--- | :---: | :---: | :---: | :---: | :---: | ---: |
| YAML authoritative for current state; Provenance authoritative for history; lint on overlap | 5 | 4 | 5 | 4 | 4 | 89 |
| Provenance authoritative; YAML mirrors selected current-state fields | 3 | 3 | 2 | 3 | 3 | 56 |
| Duplicate fields manually in both layers with no authority rule | 1 | 1 | 2 | 2 | 2 | 30 |

#### C. Governance Implication
*   **Decision Impact**: `P-STD-001` should explicitly state that frontmatter owns current-state values such as status and version, while Provenance owns history and lineage.
*   **Risk**: This is the main control needed to resolve `P-RES-003-RISK-002`.

---

### Topic 9: Benchmark Current P-STD And Agentic Surface State
**Objective**: Audit the current metadata state of all in-scope formal and agentic surfaces against the recommended direction.

#### A. Evidence & Forensics
*   **Source**: `AGENTS.md:1-22`, `prompt/AGENTS.md:11-39`, `.claude/CLAUDE.md:1-5`
*   **Observation**: Root `AGENTS.md` is a routing and scope-control file; `prompt/AGENTS.md` adds a standards registry and authority notes; `.claude/CLAUDE.md` is a thin wrapper that points to `prompt/AGENTS.md`.
*   **Source**: `prompt/roles/consultant/CLAUDE_CONSULTANT.md:1`, `prompt/roles/planner/CLAUDE_PLANNER.md:1`, `prompt/roles/developer/CLAUDE_DEVELOPER.md:1`, `prompt/roles/reviewer/CLAUDE_REVIEWER.md:1`
*   **Observation**: Each role wrapper is a one-line delegation to a deeper `*_system.md` body.
*   **Source**: `prompt/roles/consultant/consultant_system.md:1-19`, `prompt/roles/planner/planner_system.md:1-18`, `prompt/roles/developer/developer_system.md:1-12`, `prompt/roles/reviewer/reviewer_system.md:1-19`
*   **Observation**: The role bodies contain rich natural-language instruction structure but no frontmatter or explicit machine-readable authority metadata.

#### B. Analysis
*   **Synthesis**: The program already has a meaningful hierarchy, but it is encoded mostly by path and indirection, not by explicit metadata. That is workable for humans and partially workable for agents, but it is not deterministic enough for future linting and conformance.
*   **Gap Analysis**: The strongest existing patterns worth preserving are the prompt-level standards registry, the wrapper-to-body delegation pattern, and the root-to-scoped routing model.

**Cross-Surface Gap Matrix**

| Surface | Frontmatter | Version Tracking | References / Provenance Structure | Discovery / Authority Pattern | Change Magnitude |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `P-STD-001` | None | Free-form post-promotion rows only | Unique references heading; flat Provenance table | Governs others but least normalized internally | Major |
| `P-STD-002` | None | Has amendment history | Uses evolved subsection pattern | Good baseline for amendment history | Medium |
| `P-STD-004` | None | None | Uses seed-oriented Provenance subsections | Good baseline for source-input capture | Medium |
| `P-STD-005` | None | Hardening notes, not normalized revision log | Uses promotion/input/hardening pattern | Good baseline for lineage | Medium |
| Root `AGENTS.md` | None | None | No explicit metadata sections | Root routing authority | Medium |
| `prompt/AGENTS.md` | None | None | Registry table but no formal metadata layer | Scoped authority surface for `prompt/` | Medium |
| `.claude/CLAUDE.md` | None | None | Minimal wrapper only | Thin delegation to `prompt/AGENTS.md` | Low |
| Role `CLAUDE_*` wrappers | None | None | Minimal wrapper only | Thin delegation to role bodies | Low |
| Role `*_system.md` bodies | None | None | Natural-language sections only | Real behavioral content behind wrappers | Medium |
| Template / Guideline derivatives | None / placeholders | None | Placeholder `References` and `Provenance` only | Derivative authoring layer | Major downstream impact |

#### C. Governance Implication
*   **Decision Impact**: Topic 9 confirms that AC009 should treat formal standards and derivative agentic surfaces as one metadata-governed ecosystem, but with different change magnitudes.
*   **Risk**: If wrapper files are standardized without corresponding rules for their delegated bodies, authority drift will simply move one level deeper.

---

### Topic 10: Agentic-Native Specification Metadata Schemas
**Objective**: Benchmark how agentic ecosystems structure metadata in instruction and configuration files.

#### A. Evidence & Forensics
*   **Source**: Claude Code uses `CLAUDE.md` as a persistent markdown instruction surface and supports `@path` imports; the docs explicitly state that `CLAUDE.md` files are loaded in full and act as context rather than strict enforcement.[10]
*   **Source**: Cursor rules support project-scoped `.cursor/rules`, global user rules, `AGENTS.md` as a markdown alternative, and rule metadata fields such as `description`, `globs`, and `alwaysApply`; applied rule contents are included at the start of model context.[11]
*   **Source**: Cursor CLI also reads `AGENTS.md` and `CLAUDE.md` from the project root and applies them alongside `.cursor/rules`.[12]
*   **Source**: Windsurf supports `global_rules.md` and `.windsurf/rules`, with workspace-level files tied to globs or natural-language descriptions and discovered across the current workspace, subdirectories, and parent directories to the git root.[13]
*   **Source**: GitHub Actions workflow files are explicit YAML with top-level metadata such as `name`, `run-name`, `on`, and `jobs`.[14]
*   **Source**: GitHub Copilot supports repository-wide `copilot-instructions.md` and path-specific `.instructions.md` files with an `applyTo` field.[15]
*   **Source**: MCP tool, prompt, and resource objects are schema-first and expose fields such as `name`, `description`, `inputSchema`, `arguments`, `uri`, `mimeType`, and `annotations`.[17][18][19]

| Agentic Surface | Metadata Style | Key Fields / Signals | Scope Expression | Program-Relevant Takeaway |
| :--- | :--- | :--- | :--- | :--- |
| Claude Code `CLAUDE.md` | Markdown with path/import conventions | file location, imported paths, loaded-memory behavior | directory and import based | Good fit for markdown body plus light scope metadata |
| Cursor rules / `AGENTS.md` | Mixed markdown + rule metadata | `description`, `globs`, `alwaysApply` | glob and project/user rule scope | Strong evidence for lightweight scoped metadata |
| Windsurf rules | Markdown plus workspace discovery heuristics | rule files, descriptions, workspace/root discovery | workspace, subdirectory, parent-to-root search | Reinforces path-aware discovery with light metadata |
| GitHub Actions | YAML schema-first | `name`, `run-name`, `on`, `jobs` | workflow file path and event triggers | Strong example of deterministic structured metadata |
| GitHub Copilot instructions | Markdown plus scoped metadata | `applyTo`, repo/personal/org instruction layers | explicit path targeting | Strong example of declarative applicability metadata |
| MCP tools/prompts/resources | Schema-first objects | `name`, `description`, `inputSchema`, `uri`, `annotations` | object registration and protocol discovery | Best evidence for machine-validated metadata fields |

#### B. Analysis
*   **Synthesis**: Agentic systems split into two families:
    markdown-body instruction files with light metadata and path-based scope;
    schema-first objects where metadata is explicit and machine-validated.
*   **Gap Analysis**: The program's current agentic surfaces resemble the first family, but without any standardized lightweight metadata layer beyond headings and path structure.

**Comparative Evaluation**

| Option | Program Fit | Industry Alignment | Agentic Operability | Adoption Overhead | Extensibility | Weighted Total |
| :--- | :---: | :---: | :---: | :---: | :---: | ---: |
| Hybrid markdown body plus light structured header / scoped metadata | 5 | 4 | 5 | 4 | 5 | 91 |
| Pure free-text markdown instruction files | 3 | 2 | 2 | 5 | 3 | 59 |
| JSON/schema-first manifests for all repo-owned instruction surfaces | 3 | 4 | 5 | 2 | 4 | 71 |

#### C. Governance Implication
*   **Decision Impact**: For derivative agentic surfaces, standardize a lightweight metadata layer around scope, applicability, and authority, while keeping markdown bodies for the instruction content itself.
*   **Risk**: Forcing all agentic files into JSON would improve machine parsing but misfit the repo's established authoring patterns.

---

### Topic 11: Agentic Specification Discovery & Navigation
**Objective**: Evaluate how agentic systems discover and navigate multi-file instruction ecosystems.

#### A. Evidence & Forensics
*   **Source**: Claude Code documents a multi-file memory/instructions model and exposes `/memory` plus hooks to inspect which instruction files were loaded.[10]
*   **Source**: Cursor supports project rules, user rules, AGENTS/CLAUDE root files, and explicit `@Cursor Rules` inclusion.[11][12]
*   **Source**: Windsurf searches workspace and subdirectories and then continues toward the git root; it deduplicates rules in multi-folder workspaces.[13]
*   **Source**: GitHub Copilot path-specific custom instructions rely on explicit `applyTo` targeting.[15]

#### B. Analysis
*   **Synthesis**: Two robust discovery patterns recur: hierarchical discovery by path/scope and explicit targeting/import.
*   **Gap Analysis**: The program already uses hierarchical discovery informally (`AGENTS.md` at root, scoped prompt `AGENTS.md`, `.claude/CLAUDE.md`, role wrappers), but it does not currently declare the discovery model as governance metadata.

**Comparative Evaluation**

| Option | Program Fit | Industry Alignment | Agentic Operability | Adoption Overhead | Extensibility | Weighted Total |
| :--- | :---: | :---: | :---: | :---: | :---: | ---: |
| Hierarchical discovery with nearest-scope precedence and optional explicit imports | 5 | 4 | 5 | 4 | 4 | 89 |
| Single root registry file only | 3 | 3 | 3 | 3 | 3 | 60 |
| Explicit imports only, no ambient discovery | 2 | 2 | 4 | 2 | 4 | 52 |

#### C. Governance Implication
*   **Decision Impact**: Preserve the repo's hierarchical discovery model, but make scope and precedence explicit so it can be linted.
*   **Risk**: A pure root-registry model would oversimplify the current role- and directory-scoped instruction system.

---

### Topic 12: Agentic Version Tracking & Consistency Enforcement
**Objective**: Evaluate how agentic systems handle drift, consistency, and failure semantics.

#### A. Evidence & Forensics
*   **Source**: GitHub Actions explicitly models job-level and matrix-level failure semantics through `continue-on-error` and `strategy.fail-fast`.[14]
*   **Source**: Claude Code reloads `CLAUDE.md` after compaction and exposes hooks to inspect loaded instruction files, which helps detect instruction-loading drift.[10]
*   **Source**: Windsurf deduplicates overlapping rule sources and searches to git root, demonstrating explicit handling of multi-source rule discovery.[13]
*   **Source**: Copilot applies multiple instruction layers simultaneously and documents their precedence, which is a consistency-control surface even without explicit file version numbers.[16]

#### B. Analysis
*   **Synthesis**: Agentic ecosystems rarely expose "version history tables" for instruction files. Their consistency model is closer to precedence rules, reload behavior, validation, and failure semantics.
*   **Gap Analysis**: That strengthens the case for a lightweight in-file current-state header plus lint checks, not a heavy central metadata registry.

**Comparative Evaluation**

| Option | Program Fit | Industry Alignment | Agentic Operability | Adoption Overhead | Extensibility | Weighted Total |
| :--- | :---: | :---: | :---: | :---: | :---: | ---: |
| Hybrid consistency model: authoritative headers plus lint/checks and repo-state verification | 5 | 4 | 5 | 4 | 4 | 89 |
| Manual human discipline only | 2 | 1 | 1 | 5 | 2 | 43 |
| Heavy centralized registry with strict validation | 3 | 4 | 4 | 1 | 4 | 63 |

#### C. Governance Implication
*   **Decision Impact**: AC009 should pair any new metadata schema with validation rules for overlapping header/Provenance fields and broken authority-chain references.
*   **Risk**: Manual discipline alone is too weak for a growing multi-surface instruction ecosystem.

---

### Topic 13: Agentic Authority & Governance Hierarchy Resolution
**Objective**: Evaluate how agentic systems express precedence and hierarchy across multiple instruction layers.

#### A. Evidence & Forensics
*   **Source**: GitHub Copilot states that personal instructions take highest priority, repository instructions come next, organization instructions last, while all relevant instructions are still provided.[16]
*   **Source**: Cursor has user rules, project rules, AGENTS/CLAUDE support, and explicit rule-application types such as always-attached or manual inclusion.[11][12]
*   **Source**: Claude Code warns that `CLAUDE.md` is context rather than enforcement and that conflicting files can lead to ambiguous behavior; it also provides tooling to inspect what loaded.[10]
*   **Source**: Windsurf merges global and workspace rules and searches across nested directories and parent directories to git root.[13]
*   **Source**: `AGENTS.md:11-15`, `prompt/AGENTS.md:23-39`, `.claude/CLAUDE.md:1-5`, and the role wrapper files at line 1 show that the repo already uses a root-to-scoped-to-wrapper delegation hierarchy.

#### B. Analysis
*   **Synthesis**: The winning pattern is explicit layered authority, not "one file to rule them all". However, repo-governed authority must distinguish between repo-owned instruction surfaces and external user/tool settings that the repo cannot govern.
*   **Gap Analysis**: The program's current hierarchy exists, but its rules live in prose and indirection rather than a declared precedence model.

**Comparative Evaluation**

| Option | Program Fit | Industry Alignment | Agentic Operability | Adoption Overhead | Extensibility | Weighted Total |
| :--- | :---: | :---: | :---: | :---: | :---: | ---: |
| Explicit repo-owned precedence chain with scope inheritance and wrapper delegation | 5 | 4 | 5 | 4 | 4 | 89 |
| Tool-specific silos with no unified repo model | 2 | 2 | 2 | 3 | 2 | 44 |
| Single global instruction file only | 2 | 1 | 2 | 4 | 1 | 41 |

#### C. Governance Implication
*   **Decision Impact**: Recommended repo-owned authority chain:
    root governance surface;
    scoped governance surface;
    tool-specific wrapper;
    delegated role body.
    Same-family nearest-scope files should override broader ones; wrapper files should point to, not duplicate, their delegated bodies.
*   **Risk**: If AC009 standardizes wrapper files without defining body delegation rules, authority ambiguity will remain.

---

## IV. CROSS-TOPIC INTEGRATION

### Integration 1: Frontmatter ↔ Provenance Delineation
*   **Synthesis**: Topics 1, 2, and 8 converge on a two-layer model. YAML should hold current-state metadata that benefits from deterministic parsing, while `## Provenance` should hold history, lineage, and rationale pointers.
*   **Authority Rule**: If the same conceptual field can appear in both layers, YAML is authoritative for present state and Provenance is authoritative for historical state transitions.

### Integration 2: Version Tracking ↔ Provenance Placement
*   **Synthesis**: Topics 3, 4, and 5 support placing a concise `Amendment History` inside `## Provenance`, not in YAML and not as a separate top-level section.
*   **Recommended Boundary**: YAML stores only the current `version`; Provenance stores dated amendment rows and change summaries; git remains the full diff authority.

### Integration 3: References ↔ Traceability
*   **Synthesis**: Topics 6 and 7 separate citation purpose from governance lineage.
*   **Recommended Boundary**: `## References` should hold cited authorities and supporting materials using a normative/informative taxonomy. Governance-chain pointers such as promotion contracts, supersession, and seed inputs belong in `## Provenance`, not duplicated into References unless the cited artifact is also being used as an external authority.

### Integration 4: SPS Constraint Alignment
*   **Synthesis**: Topics 1 and 8 confirm that `sps_P-PROGRAM.md` `P-CON-003` is directionally correct but operationally incomplete.
*   **Disposition**: `P-CON-003` should remain in force and be clarified to point to the new `P-STD-001` schema and the YAML-versus-Provenance authority split, not amended away.

### Integration 5: Traditional Frontmatter ↔ Agentic Metadata
*   **Synthesis**: Topics 1, 2, and 10 show overlap around identity, status, scope, ownership, and applicability, but divergence in expression style.
*   **Recommended Shared Core**: compact identity/status metadata for all governed artifacts; derivative agentic surfaces add scope and delegation metadata that formal standards do not need in the same way.

### Integration 6: Traditional Versioning ↔ Agentic Consistency Enforcement
*   **Synthesis**: Topics 3, 4, and 12 show that agentic ecosystems care more about reload, precedence, and validation than about rich in-file revision logs.
*   **Recommended Hybrid**: keep semver and concise amendment history for standards, then add lint-style checks for overlapping metadata, broken delegation chains, and inconsistent derivative headers.

### Integration 7: Traditional Delineation ↔ Agentic Hierarchy Resolution
*   **Synthesis**: Topics 8, 11, and 13 support an explicit repo-owned authority chain.
*   **Recommended Authority Chain**: root governance surface -> scoped governance surface -> tool wrapper -> delegated body. Same-family nearest-scope files override broader ones; wrappers declare delegation rather than duplicating behavior text.

### Gap Analysis
*   **Frontmatter Gap**: All four active P-STDs lack the structured current-state metadata layer that every traditional benchmark exposes in some form.
*   **Versioning Gap**: Only P-STD-002 has a recognizable amendment-history pattern, and it is not yet governed program-wide.
*   **Provenance Gap**: All four active P-STDs carry useful provenance material, but there is no minimum subsection taxonomy and no derivative guidance driving consistency.
*   **References Gap**: The ecosystem lacks a stable normative/informative taxonomy and even basic entry-schema consistency.
*   **Agentic Governance Gap**: Repo-native instruction surfaces already have an implicit hierarchy, but they do not declare scope, precedence, or delegation using governed metadata.

---

## V. ARTIFACT UPDATES

| Artifact ID | Section | Action Required | Content Source |
| :--- | :--- | :--- | :--- |
| `P-STD-001` | New YAML frontmatter CLAUSE domain | Define a compact current-state schema for standard files; include lifecycle-conditional fields and authority rule versus Provenance | Topics 1, 2, 8 |
| `P-STD-001` | New version-tracking CLAUSE domain | Standardize a concise `Amendment History` subsection under `## Provenance`; define version increment triggers | Topics 3, 4 |
| `P-STD-001` | Hardening of `## Provenance` | Replace placeholder-only governance with a fixed minimum taxonomy: `Status`, `Lineage / Authority`, `Amendment History`, `Input Sources` | Topics 5, 7 |
| `P-STD-001` | Hardening of `## References` | Standardize `Normative References` and `Informative References` plus one row schema; retire `Referenced ID` inconsistency | Topic 6 |
| `P-STD-001` | New metadata delineation CLAUSE domain | Declare YAML authoritative for current-state fields and Provenance authoritative for history and lineage; require consistency checks on overlap | Topic 8 |
| `P-STD-001` | Derivative agentic-surface governance | Define how repo-owned `AGENTS.md` / `CLAUDE.md`-family files declare scope, authority, and delegation | Topics 9, 10, 11, 12, 13 |
| `sps_P-PROGRAM.md` | `P-CON-003` | Clarify, do not remove: retain the YAML-frontmatter requirement but point it at the new `P-STD-001` schema and authority rules | Topics 1, 8 |
| `guideline_standard_specs.md` | References / Provenance authoring guidance | Add subsection guidance that mirrors the new `P-STD-001` rules | Topics 5, 6 |
| `template_standard_specs.md` | `## References`, `## Provenance`, header | Replace placeholder dashes with the new canonical shells and add governed frontmatter | Topics 1, 5, 6, 8 |
| `AGENTS.md`, `prompt/AGENTS.md`, `.claude/CLAUDE.md`, role `CLAUDE_*` wrappers | Derivative metadata alignment | Preserve the current routing/delegation model, but add standardized scope and authority metadata once AC009 defines the derivative contract | Topics 9, 11, 13 |
| `P-PH000-ST004-AC003` gate artifacts | Verification workflow | Reuse AC001-style formal `GATE-002` and `GATE-003` verification artifacts, including explicit topic-deliverable checklists and SPS-baseline recheck before sign-off | Prior ST004 execution pattern; Topics 9, 12 |

---

## VI. SOURCE MATERIAL
*   **Brief Version**: `v2.0.0`
*   **Code Commit/Tag**: `4860a2f93ad04ffc5d1326e43df96c8718764eb4`
*   **Files Cited**:
    *   `prompt/artifacts/tasks/P/research/P-RES-003/brief_P-RES-003_specification-metadata-governance-research.md`
    *   `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md`
    *   `prompt/artifacts/tasks/P/workspace/PH000/ST004/plan_P-PH000-ST004.md`
    *   `prompt/artifacts/tasks/P/workspace/PH000/ST001/plan_P-PH000-ST001.md`
    *   `prompt/artifacts/tasks/P/standard/standard_P-STD-001_program-governance-standard.md`
    *   `prompt/artifacts/tasks/P/standard/standard_P-STD-002_program-status-standard.md`
    *   `prompt/artifacts/tasks/P/standard/standard_P-STD-004_file-naming-and-directory-convention.md`
    *   `prompt/artifacts/tasks/P/standard/standard_P-STD-005_universal-id-specification.md`
    *   `AGENTS.md`
    *   `prompt/AGENTS.md`
    *   `.claude/CLAUDE.md`
    *   `prompt/roles/consultant/CLAUDE_CONSULTANT.md`
    *   `prompt/roles/planner/CLAUDE_PLANNER.md`
    *   `prompt/roles/developer/CLAUDE_DEVELOPER.md`
    *   `prompt/roles/reviewer/CLAUDE_REVIEWER.md`
    *   `prompt/roles/consultant/consultant_system.md`
    *   `prompt/roles/planner/planner_system.md`
    *   `prompt/roles/developer/developer_system.md`
    *   `prompt/roles/reviewer/reviewer_system.md`
    *   `prompt/templates/consultant/standards/guideline_standard_specs.md`
    *   `prompt/templates/consultant/standards/template_standard_specs.md`

## Sources
- [1] ReSpec Documentation — https://respec.org/docs/
- [2] W3C Publication Rules — https://www.w3.org/pubrules/
- [3] W3C Manual of Style — https://www.w3.org/TR/2021/NOTE-manual-of-style-20210921/
- [4] RFC 7991: The "xml2rfc" Version 3 Vocabulary — https://www.rfc-editor.org/rfc/rfc7991.txt
- [5] RFC 7322: RFC Style Guide — https://www.rfc-editor.org/rfc/rfc7322.txt
- [6] ISO Standard Catalogue Example (publication metadata fields) — https://www.iso.org/standard/75839.html
- [7] IEEE SA PARs, PAR Forms & Continuous Processing — https://standards.ieee.org/faqs/pars/
- [8] IEEE SA NesCom Conventions — https://standards.ieee.org/about/sasb/nescom/conv/
- [9] IEEE SA Initiating the Project — https://standards.ieee.org/develop/initiating-project/
- [10] Claude Code Docs: How Claude remembers your project — https://code.claude.com/docs/en/memory
- [11] Cursor Rules — https://docs.cursor.com/en/context/rules
- [12] Cursor CLI Using — https://docs.cursor.com/en/cli/using
- [13] Windsurf Memories & Rules — https://docs.windsurf.com/plugins/cascade/memories
- [14] GitHub Docs: Workflow syntax for GitHub Actions — https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax
- [15] GitHub Docs: Your first custom instructions — https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/your-first-custom-instructions
- [16] GitHub Docs: Adding personal custom instructions for GitHub Copilot — https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-personal-instructions
- [17] MCP Specification: Tools — https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- [18] MCP Specification: Prompts — https://modelcontextprotocol.io/specification/2025-06-18/server/prompts
- [19] MCP Specification: Resources — https://modelcontextprotocol.io/specification/2025-06-18/server/resources

---

## VII. ISSUE & RISK REGISTER (T102-STD-007)

**Issues**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Resolution Notes | Resolution Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `P-RES-003-ISSUE-001` | ADR Index Inconsistency | ADR Index table exists in P-STD-001 and P-STD-005 but is absent from P-STD-002 and P-STD-004. Structural conformance issue; not a metadata-governance finding. | LLM_Consultant | DEFERRED | Medium | 2026-03-12 | Out of scope for P-RES-003; carry to AC009. | — |
| `P-RES-003-ISSUE-002` | SPS YAML Requirement Drift | `P-CON-003` requires YAML frontmatter but the active P-STDs implement none. | LLM_Consultant | RESOLVED | High | 2026-03-12 | Research recommends keeping the requirement but clarifying the schema and authority rule in P-STD-001. | 2026-03-13 |
| `P-RES-003-ISSUE-003` | Agentic Tooling Documentation Volatility | Agentic source materials evolve quickly and may change after research capture. | LLM_Consultant | MONITORED | Medium | 2026-03-13 | Retrieval dates recorded; findings framed as current-state evidence. | 2026-03-13 |
| `P-RES-003-ISSUE-004` | Approval-State Traceability Drift | User explicitly approved research execution, but ST004 still records AC003 `GATE-001` as `in_progress`. | LLM_Consultant | OPEN | Medium | 2026-03-13 | Administrative traceability fix needed in stream tracking; does not change research conclusions. | — |

**Risks**

| ID | Title | Description | Owner | Status | Priority | Proposed Date | Mitigation Notes | Mitigation Date |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `P-RES-003-RISK-001` | Retrofit Blast Radius | Metadata hardening affects 4 P-STDs plus derivatives and potentially SPS. | LLM_Consultant | OPEN | High | 2026-03-12 | Recommendations favor minimal governed structures over heavy process machinery. | — |
| `P-RES-003-RISK-002` | YAML-Provenance Authority Ambiguity | Overlapping fields could create a new drift vector. | LLM_Consultant | RESOLVED | High | 2026-03-12 | Recommended split: YAML for current state, Provenance for history, with linting on overlap. | 2026-03-13 |
| `P-RES-003-RISK-003` | Standards Body Practice May Not Scale Down | Large standards-body patterns may overfit the program. | LLM_Consultant | MITIGATED | Medium | 2026-03-12 | Recommendations intentionally adopt only small, high-value patterns. | 2026-03-13 |
| `P-RES-003-RISK-004` | Agentic Evidence Maturity Gap | Agentic-native governance is less standardized than traditional standards practice. | LLM_Consultant | MONITORED | Medium | 2026-03-13 | Traditional evidence anchors the baseline; agentic evidence shapes operability and precedence decisions. | 2026-03-13 |

---

## VIII. CRITICAL DEPENDENCIES

*   **P-STD-001 (YAML Frontmatter CLAUSE domain)**: Topics 1, 2, and 8 define the compact schema, obligation levels, and authority split needed to operationalize `P-CON-003`.
*   **P-STD-001 (Version Tracking CLAUSE domain)**: Topics 3 and 4 define semver retention, increment triggers, and Provenance-embedded amendment history.
*   **P-STD-001 (Provenance hardening)**: Topics 5 and 7 define the minimum subsection taxonomy and the traceability boundary between in-spec lineage and external process records.
*   **P-STD-001 (References hardening)**: Topic 6 defines the normative/informative taxonomy and the reference-entry schema normalization needed across all active P-STDs.
*   **P-STD-001 (Agentic surface governance)**: Topics 9, 10, 11, 12, and 13 define the derivative metadata, discovery, precedence, and delegation model for repo-owned `AGENTS.md` / `CLAUDE.md` surfaces.
*   **`sps_P-PROGRAM.md` `P-CON-003`**: Research conclusion is explicit: retain the YAML requirement, but clarify it by reference to the new `P-STD-001` schema and authority rules.
*   **`guideline_standard_specs.md` and `template_standard_specs.md`**: Both derivatives must be updated in AC009/AC010 to carry the new frontmatter shell and standardized `References` / `Provenance` structures.

---

## IX. SUCCESS CRITERIA CHECK

| Criterion | Status | Notes |
| :--- | :--- | :--- |
| All 13 topics addressed | Met | Topics 1-13 included with Evidence, Analysis, and Governance Implication sections |
| Comparative topics scored with weighted totals | Met | Topics 1, 3, 5, 6, 8, 10, 11, 12, 13 include 1-5 scoring and weighted totals |
| Topic 9 gap matrix covers formal + agentic surfaces | Met | Includes four active P-STDs plus root/scoped/wrapper/body agentic surfaces |
| Cross-topic integrations synthesized | Met | Section IV covers Integrations 1-7 plus gap analysis |
| Recommendations-only boundary preserved | Met | No CLAUSE drafting and no governed artifact retrofits performed |
| Issues and risks registered | Met | Section VII uses stable `P-RES-003-ISSUE-*` and `P-RES-003-RISK-*` IDs |
