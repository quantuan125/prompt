---
artifact_type: 'ANALYSIS'
initiative_id: 'P'
activity_id: 'P-PH000-ST001-AC002'
version: 'v1.0.0'
date: '2026-02-19'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
subject: 'Promotion Methodology Comparison: Adopt-by-Reference vs Full Promotion for P-STD-001'
---

# Analysis: Promotion Methodology Comparison — Adopt-by-Reference vs Full Promotion

## I. PURPOSE

This analysis provides a structured, weighted comparison of two candidate promotion methodologies for establishing `P-STD-001` (Program Governance Standard) from `T102-STD-004` (Specification Standard & Guideline). The purpose is to inform GATE-001 of `P-PH000-ST001-AC002` with a decision-ready recommendation grounded in industry precedent and system-specific constraints.

## II. METHODOLOGY OPTIONS

### Option A: Adopt-by-Reference (Current Plan Default)

`P-STD-001` is a thin program-level wrapper that:
- Declares itself the program authority for standard-specification authoring.
- Incorporates all `T102-STD-004` clauses (CLAUSE-001 through CLAUSE-029) by normative reference without reproducing their bodies.
- Documents only program-specific variances (directory placement, portability, reference semantics).
- `T102-STD-004` remains the living document where all substantive development continues.

### Option B: Full Promotion (Client Preference)

`P-STD-001` receives the full normative content of `T102-STD-004`:
- All 29 CLAUSEs are transferred (with re-identification as `P-STD-001-CLAUSE-###`).
- All 4 substandards (A–D) are reproduced under P-STD-001 headings.
- `T102-STD-004` is marked `superseded` with a pointer to `P-STD-001`.
- An alias window (per `T102-STD-005-CLAUSE-003B`) allows existing `T102-STD-004-CLAUSE-*` references to remain valid during migration.
- All future development occurs in `standard_P-STD-001_...md`.

---

## III. EVALUATION CRITERIA & WEIGHTING

| # | Criterion | Weight | Rationale for Weight |
|:--|:--|:--|:--|
| C1 | **Reference Clarity** — Can a downstream consumer find and understand the authoritative content in one step? | 25% | Primary purpose of standards is clarity; indirection undermines adoption |
| C2 | **Scope-Identity Alignment** — Does the ID prefix match the content's actual governance scope? | 20% | Misaligned scope signals cause confusion about authority and precedence |
| C3 | **Development Location Clarity** — Is it unambiguous where amendments are authored? | 15% | Ambiguity about where to edit creates governance drift |
| C4 | **Migration Cost** — Immediate effort to implement the promotion | 10% | One-time cost; should not dominate a structural decision |
| C5 | **Provenance Preservation** — Is the authoring lineage and decision history traceable? | 10% | Important for auditability but achievable under both approaches |
| C6 | **Framework Compliance** — Alignment with existing ID/STD governance rules | 10% | The promotion method should work *with* the governance framework, not around it |
| C7 | **Future Scalability** — How well does the approach scale when additional STDs are promoted? | 10% | P-STD-002 through P-STD-005 are planned; precedent matters |

**Total**: 100%

---

## IV. COMPARATIVE SCORING

Scale: 1 (Poor) — 2 (Weak) — 3 (Adequate) — 4 (Good) — 5 (Excellent)

### C1: Reference Clarity (Weight: 25%)

| | Option A: Adopt-by-Reference | Option B: Full Promotion |
|:--|:--|:--|
| **Score** | **2** | **5** |
| **Rationale** | Downstream consumer reads P-STD-001, finds normative reference to T102-STD-004, must then locate and read T102-STD-004 for actual clause content. Two-hop reference pattern. The guideline/template authority chain becomes ambiguous ("governed by P-STD-001" but content is in T102-STD-004). | Single document. P-STD-001 contains all normative content. Downstream consumer reads one file. Authority chain is direct: guideline → P-STD-001 → done. |
| **Industry Precedent** | ISO uses normative references for *external* standards maintained by different bodies (e.g., ISO 9001 → ISO 19011). Not used for internal scope promotions. | ISO republishes content at international scope (BS 5750 → ISO 9001). RFCs receive new numbers at promotion. CMMI practices are published at the maturity level they govern. |

### C2: Scope-Identity Alignment (Weight: 20%)

| | Option A: Adopt-by-Reference | Option B: Full Promotion |
|:--|:--|:--|
| **Score** | **2** | **5** |
| **Rationale** | The `T102` prefix on the living document signals initiative scope, but the content governs all initiatives. New initiatives (T104, T105) would be governed by an initiative-scoped document — a scope mismatch. P-STD-001 exists but is hollow. | `P-STD-001` is the authoritative surface at Program scope. The ID prefix accurately signals governance scope. `T102-STD-004` is superseded and no longer signals authority. |
| **T102-STD-005-CLAUSE-003 Alignment** | Technically compliant (P-STD-001 *exists* at Program scope), but substantively misleading — the program surface contains no program content. | Fully aligned. Program > Initiative precedence is realized in both form and substance. |

### C3: Development Location Clarity (Weight: 15%)

| | Option A: Adopt-by-Reference | Option B: Full Promotion |
|:--|:--|:--|
| **Score** | **2** | **5** |
| **Rationale** | Amendments to the authoring model happen in `standard_T102-STD-004_...md` (an initiative file) while P-STD-001 (the authority) is a separate file. This creates a principal-agent problem: the authority surface doesn't own its own content. Risk of governance drift is high. | All amendments happen in `standard_P-STD-001_...md`. The authority surface and the living content are co-located. No ambiguity about where to make changes. |

### C4: Migration Cost (Weight: 10%)

| | Option A: Adopt-by-Reference | Option B: Full Promotion |
|:--|:--|:--|
| **Score** | **4** | **3** |
| **Rationale** | Low immediate effort: draft a thin P-STD-001 wrapper (~50-100 lines) referencing T102-STD-004. No content transfer. No reference migration needed since T102-STD-004 remains live. | Moderate effort: transfer 29 CLAUSEs + 2 ADRs + substandard structure. Re-identify all CLAUSE IDs. Mark T102-STD-004 as superseded. Establish alias window. Migrate guideline/template authority chains. However, blast radius is limited because cross-initiative references haven't proliferated yet (client observation). |
| **Mitigating Factor** | — | The alias window (CLAUSE-003B) absorbs migration timeline. Existing T102-STD-004-CLAUSE-* references within T102-PH001-ST001 can migrate progressively. |

### C5: Provenance Preservation (Weight: 10%)

| | Option A: Adopt-by-Reference | Option B: Full Promotion |
|:--|:--|:--|
| **Score** | **4** | **4** |
| **Rationale** | T102-STD-004 remains intact with full history. Provenance is trivially preserved by virtue of not moving anything. | P-STD-001 Provenance section records `supersedes: T102-STD-004`. ADR-001 in P-STD-001 documents the promotion decision. T102-STD-004 file remains in repo (marked superseded) as historical artifact. Git history is intact. |
| **Assessment** | Equal. Both approaches adequately preserve provenance. |

### C6: Framework Compliance (Weight: 10%)

| | Option A: Adopt-by-Reference | Option B: Full Promotion |
|:--|:--|:--|
| **Score** | **3** | **5** |
| **Rationale** | T102-STD-005-CLAUSE-003A defines a promotion workflow involving supersession and reference migration. Adopt-by-reference avoids this workflow — it's a workaround, not a promotion in the framework's terms. No existing CLAUSE explicitly authorizes "thin wrapper" promotions. | Directly follows T102-STD-005-CLAUSE-003A: (1) stable content, (2) multi-scope applicability confirmed, (3) old ID superseded, (4) references migrated with alias window. This is the intended path. |

### C7: Future Scalability (Weight: 10%)

| | Option A: Adopt-by-Reference | Option B: Full Promotion |
|:--|:--|:--|
| **Score** | **2** | **4** |
| **Rationale** | Sets a precedent of thin wrappers at P-scope. When P-STD-002 through P-STD-005 are promoted, each would be a pointer to an initiative-scoped file. The program governance layer becomes a directory of indirections. | Sets a clean precedent: promoted standards live at their governance scope. When P-STD-005 (Universal ID Specification) is promoted from T102-STD-005 + T104-STD-002, the merge target is clearly P-STD-005. |

---

## V. WEIGHTED RESULTS

| Criterion | Weight | Option A Score | Option A Weighted | Option B Score | Option B Weighted |
|:--|:--|:--|:--|:--|:--|
| C1: Reference Clarity | 25% | 2 | 0.50 | 5 | 1.25 |
| C2: Scope-Identity Alignment | 20% | 2 | 0.40 | 5 | 1.00 |
| C3: Development Location Clarity | 15% | 2 | 0.30 | 5 | 0.75 |
| C4: Migration Cost | 10% | 4 | 0.40 | 3 | 0.30 |
| C5: Provenance Preservation | 10% | 4 | 0.40 | 4 | 0.40 |
| C6: Framework Compliance | 10% | 3 | 0.30 | 5 | 0.50 |
| C7: Future Scalability | 10% | 2 | 0.20 | 4 | 0.40 |
| **TOTAL** | **100%** | — | **2.50** | — | **4.60** |

---

## VI. SENSITIVITY ANALYSIS

Even if migration cost (C4) were weighted at 25% (maximum possible):

| Criterion | Reweighted | Option A | Option B |
|:--|:--|:--|:--|
| C1 | 20% | 0.40 | 1.00 |
| C2 | 15% | 0.30 | 0.75 |
| C3 | 10% | 0.20 | 0.50 |
| **C4** | **25%** | **1.00** | **0.75** |
| C5 | 10% | 0.40 | 0.40 |
| C6 | 10% | 0.30 | 0.50 |
| C7 | 10% | 0.20 | 0.40 |
| **TOTAL** | 100% | **2.80** | **4.30** |

Option B (Full Promotion) wins under all reasonable weighting schemes. Option A only approaches parity if migration cost is weighted at >60%, which is not defensible for a one-time structural decision.

---

## VII. RECOMMENDATION

**Option B: Full Promotion** is the recommended methodology for establishing `P-STD-001`.

**Key conditions for implementation**:
1. `T102-STD-004` must be marked `superseded` with a clear pointer to `P-STD-001`.
2. An alias window (per T102-STD-005-CLAUSE-003B) must be established for `T102-STD-004-CLAUSE-*` → `P-STD-001-CLAUSE-*` references.
3. A new CLAUSE governing promotion/demotion lifecycle must be authored within `P-STD-001` itself (as the program authority for such governance).
4. The AC002 activity plan must be amended to reflect full promotion scope (current plan assumes adopt-by-reference).
5. `guideline_standard_specs.md` and `template_standard_specs.md` authority chains must reference `P-STD-001` post-promotion.

---

## VIII. REFERENCES

| Reference | Path |
|:--|:--|
| T102-STD-004 (upstream standard) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-004_specification-standard-and-guideline.md` |
| T102-STD-005 (ID specification rules) | `prompt/artifacts/tasks/T102/standard/standard_T102-STD-005_id-specification-rules.md` |
| AC002 Activity Plan | `prompt/artifacts/tasks/P/workspace/PH000/ST001/AC002/plan_P-PH000-ST001-AC002.md` |
| Program SPS | `prompt/artifacts/tasks/P/ssot/sps_P-PROGRAM.md` |
| Guideline (standard specs) | `prompt/templates/consultant/standards/guideline_standard_specs.md` |

---

## IX. PROVENANCE

| Field | Value |
|:--|:--|
| Created | 2026-02-19 |
| Author | LLM_Consultant |
| Activity | P-PH000-ST001-AC002 (pre-GATE-001 analysis) |
| Requested by | Client |
| Purpose | Inform promotion methodology decision before TK002 drafting |
