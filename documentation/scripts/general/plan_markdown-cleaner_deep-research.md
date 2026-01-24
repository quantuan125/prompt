---
artifact_type: 'PLAN'
initiative_id: 'T801'
epic_id: 'T801A'
version: '1.0.0'
date: '2025-11-30'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# CONSULTANCY PLAN: Deep Research Markdown Cleaner (Generic Script)

## I. EXECUTIVE SUMMARY

This plan defines the requirements and implementation approach for a **generic Python script** that cleans Markdown reports produced from **ChatGPT Deep Research → `.words` → word2md** workflows. The script will live under `scripts/general`, and its primary goal is to normalize references, strip conversion artifacts, and improve Markdown readability **without changing the underlying content or citation numbering**.

**Consultant Role**: Requirements, constraints, and TDD-style implementation plan.  
**LLM_Developer Role**: Implement the Python script, tests, and documentation as specified.

**Core Objectives**:
- Provide a **repeatable cleanup pipeline** for Deep Research markdown exports (T801 exemplars plus future tasks).
- Preserve **semantic content and numeric reference IDs** while:
  - Converting inline citation links into short-form `[n]` markers.
  - Centralizing all source URLs into a single **Sources** section at the end.
  - Removing word-processor and word2md artifacts (HTML entities, escaped characters, extraneous backslashes).
- Support **test-driven development (TDD)** so behavior is well-specified and regression-safe.

This plan is intentionally implementation-ready so an LLM_Developer can execute it with minimal additional clarification.

---

## II. CONTEXT & EXEMPLARS

### A. Source Files / Exemplars

The script must be validated against these exemplar reports:

- `prompt/artifacts/tasks/T801/research/report/report_T801-RES-001_indicator-design-standards.md`
- `prompt/artifacts/tasks/T801/research/report/report_T801A-RES-001_backend-tti-architecture.md`

Both files share common patterns:
- YAML-style front-matter at the top (must remain untouched).
- Heavy use of **numeric inline citations** in the form `[\[n\]](http...)`.
- Clusters of references at the end:
  - Lines containing multiple `[\[n\]](url-with-#:~:text=...)` entries followed by a title and a bare autolink `<https://...>`.
- HTML entity and tag artifacts introduced by `.words` and word2md, e.g.:
  - `&lt;br/&gt;`, `&lt;small&gt;...&lt;/small&gt;`, `&lt;`, `&gt;`, `&amp;`.
- Backslash escape noise (e.g. `\*`, `\[`), which the client has requested to **remove globally**.

### B. Workflow Context

Typical pipeline:

1. ChatGPT Deep Research exports report to `.words` format.
2. User converts `.words` to Markdown using `https://word2md.com/`.
3. Resulting Markdown contains a mix of:
   - Citation-markdown from Deep Research.
   - Word-style escapes and HTML.
4. This **markdown cleaner script** is run locally to produce a `_CLEAN` version:
   - Same directory as original.
   - Same base filename, suffixed with `_CLEAN`.

The script must be **generic** for future Deep Research artifacts that follow the same pattern.

---

## III. SCOPE & NON-GOALS

### A. In Scope

1. **File handling**
   - Script located in `scripts/general`, e.g. `scripts/general/markdown_cleaner_deep_research.py`.
   - Input:
     - If invoked **without arguments**, clean a default list of known Deep Research reports (configured in the script).
     - If invoked **with one or more file paths**, clean those specified Markdown files.
   - Output:
     - For `path/to/FILENAME.md`, create `path/to/FILENAME_CLEAN.md`.
     - Never overwrite the original `.md`.

2. **Front-matter handling**
   - Detect and preserve the YAML-like front-matter block at the top:
     - From first line `---` through the next line `---` (inclusive).
   - Do **not** modify:
     - Keys, values, quoting, date formats, or spacing.
   - Apply all cleanup **only** to the body after this block.

3. **Citation and URL normalization**
   - Detect inline citation links of the forms:
     - `[\[n\]](http...)`
     - `[_\[n\]_](http...)` or similar italic variants.
     - Sequences like `[\[19\]](url1)[\[20\]](url2)`.
   - Replace such links in the body with short-form numeric markers:
     - `[\[n\]](...)` → `[n]`
     - Sequences: `[\[19\]](url1)[\[20\]](url2)` → `[19][20]` (or `[19] [20]`, per readability choice).
   - Extract and store each URL for later reconstruction in the Sources section:
     - Normalize by:
       - Stripping `#:~:text=...` text-fragment suffixes.
       - Trimming surrounding whitespace.
       - Removing trailing punctuation (`.`, `,`, `;`, etc.) that is obviously outside the URL.
   - **Preserve numeric IDs**:
     - The script **must not change the citation numbers** present in the content.
     - For example, `[\[19\]](url)` becomes `[19]` and contributes to `[19] Title – URL` in Sources.

4. **Descriptive links & bare URLs**
   - For non-numeric links (if present), e.g. `[Some Article](https://example.com/...)`:
     - Replace inline with a simple label aligned to numeric citations as much as possible, e.g.:
       - `Some Article`
       - Optionally followed by `[n]` if the script chooses to map it to a numeric index.
     - Extract URL into the same URL registry used for numeric citations.
   - For bare URLs:
     - Autolinks like `<https://example.com/...>` appearing inline or on their own line.
     - Trailing bare `(https://example.com/...)` fragments at the end of sentences.
     - Remove them from the body text, while adding the underlying URL to the registry.
   - For this first implementation, priority is to:
     - Clean visual noise.
     - Ensure the URL itself is preserved via the Sources section (even if not explicitly numbered in the body today).

5. **Sources section reconstruction**
   - Remove or ignore existing end-of-document reference clusters:
     - Blocks of lines with `[\[n\]](url...)` plus descriptive titles and `<https://...>` autolinks.
   - Reconstruct a single consolidated Sources block at the end of the cleaned document:
     - Use a bold label:
       - `**Sources**`
     - Follow with one line per numeric ID / source, using:
       - `[n] Title – URL`
     - Requirements:
       - Re-use the **existing numeric IDs** from the original citations (e.g. 1, 2, 3, ..., 40).
       - If there are multiple URLs for the same numeric id (e.g. `[\[19\]]`, `[\[20\]]` all pointing to a cluster):
         - Prefer to list **each numeric ID as a separate entry**, even if domain repeats.
       - Where titles exist today (in cluster lines), they should be reused as the `Title` portion where feasible.
       - When no explicit title is available:
         - Fallback to a sensible placeholder, such as the host and path segment (e.g. `luxalgo.com — swing-highs-and-lows-basics-for-traders`).

6. **HTML entities and tags**
   - Decode common HTML entities in the body:
     - `&lt;` → `<`
     - `&gt;` → `>`
     - `&amp;` → `&`
     - Optionally, `&nbsp;` → space, `&quot;` → `"`, `&apos;` → `'` (defensive).
   - Convert or strip HTML-like tags common to Deep Research exports:
     - `&lt;br/&gt;` and `<br/>`:
       - Convert to a **Markdown-friendly line break**, e.g.:
         - A blank line (new paragraph), or
         - A hard-break pattern (`"  \n"`) depending on context.
       - Developer may implement a simple rule: treat each `<br/>` as a blank line.
     - `&lt;small&gt;...&lt;/small&gt;` or `<small>... </small>`:
       - Remove the `<small>` tags but keep the inner text.
   - Ensure that code/pseudo-code sections render correctly post-decoding:
     - Expressions like `MA_short[-2] < MA_long[-2]` must render literally, not as HTML.

7. **Backslash cleanup**
   - Remove **all backslash characters (`\`)** from the Markdown body.
   - This includes:
     - Escaped punctuation (`\*`, `\[`).
     - Any stray backslashes produced by word2md.
   - **Note**: This is intentionally aggressive per client instruction; the script should **not attempt to selectively preserve any backslashes** in the cleaned body.
   - YAML front-matter is excluded from this removal (front-matter is copied verbatim).

8. **Whitespace and formatting normalization**
   - Preserve overall document structure (headings, paragraphs, lists, tables).
   - Apply light normalization:
     - Collapse 3+ consecutive blank lines down to 2.
     - Trim trailing spaces/tabs on each line.
     - Ensure a space after heading hashes:
       - `##Heading` → `## Heading`.
     - Optionally preserve or remove very specific artifacts (such as ` )_.) `) if encountered; these can be handled by regex heuristics with unit tests.

### B. Out of Scope

- Changing wording, meaning, or structure of the narrative content.
- Editing or normalizing YAML front-matter.
- Complex semantic restructuring (e.g. reorganizing sections or tables).
- Sophisticated detection of “descriptive link titles” beyond the simple patterns described.

---

## IV. FUNCTIONAL REQUIREMENTS

### A. Script Interface (CLI)

1. **Location & Name**
   - File: `scripts/general/markdown_cleaner_deep_research.py`.

2. **Invocation**
   - `python scripts/general/markdown_cleaner_deep_research.py`
     - Cleans a **default list** of known Deep Research reports.
   - `python scripts/general/markdown_cleaner_deep_research.py path/to/file1.md path/to/file2.md`
     - Cleans the specified files.

3. **Behavior**
   - For each input file:
     - Validate that the file exists and is readable.
     - Compute output path: `<original-name>_CLEAN.md` in the same directory.
     - Run the cleaning pipeline on the body.
     - Write front-matter + cleaned body to the output path.
   - Print a small summary per file:
     - Example:
       - `Cleaning: <src> -> <dst>`
       - `Original chars: NNN`
       - `Cleaned chars : MMM`
       - `Bytes saved   : NNN - MMM`

### B. Cleaning Pipeline (Conceptual Functions)

LLM_Developer should structure the implementation into small, testable units. Suggested functional decomposition:

1. `split_frontmatter(text: str) -> tuple[str | None, str]`
   - Input: raw file contents.
   - Output:
     - `frontmatter` (including delimiters) or `None` if absent.
     - `body` string for processing.

2. `decode_entities_and_html(body: str) -> str`
   - Responsibilities:
     - Decode HTML entities (`&lt;`, `&gt;`, `&amp;`, etc.).
     - Replace `<br/>` / `&lt;br/&gt;` with appropriate line breaks.
     - Strip `<small>` tags while preserving content.

3. `extract_references(body: str) -> tuple[str, ReferenceRegistry]`
   - `ReferenceRegistry` is a structured in-memory representation, e.g.:
     - `by_number: dict[int, list[Reference]]`
     - `unindexed: list[Reference]`
   - `Reference` fields:
     - `number: int | None`
     - `url: str`
     - `title_hint: str | None`
     - `source_context: str | None` (optional snippet or line where found).
   - Responsibilities:
     - Find all `[\[n\]](http...)` patterns:
       - Add `Reference(number=n, url=normalized_url, title_hint=None, ...)` to registry.
       - Replace in body with `[n]`.
     - Find descriptive `[label](http...)` links:
       - Replace in body with `label` (or `[label]`), optionally leaving `[n]` appended if mapping is used.
       - Add to `unindexed` or `by_number` depending on strategy.
     - Find bare autolinks `<http...>` and `(http...)`:
       - Remove from body.
       - Add to `unindexed` or attach to nearby numeric IDs if clearly associated.

4. `normalize_reference_numbers(registry: ReferenceRegistry) -> ReferenceRegistry`
   - Responsibilities:
     - Ensure that **existing numeric IDs** are preserved as-is.
     - Deduplicate same URL under the same number where obvious.
     - For unindexed URLs:
       - Option 1 (conservative for v1): keep them unindexed but still list in Sources with synthetic IDs that **do not appear in the body** (e.g. grouped as “Unnumbered sources” – optional).
       - Option 2 (if you choose): infer the numeric id from context; however, this is not mandatory for v1 and should be done only when safe.

5. `strip_backslashes(body: str) -> str`
   - Responsibilities:
     - Remove **all backslash characters (`\`)** from the body.
     - Applied **after** reference extraction and HTML decoding so regex patterns still work reliably.

6. `normalize_whitespace(body: str) -> str`
   - Responsibilities:
     - Trim trailing spaces.
     - Collapse multiple blank lines.
     - Fix heading spacing.

7. `render_sources_section(registry: ReferenceRegistry) -> str`
   - Responsibilities:
     - Generate the final Sources block:
       - Leading `\n\n**Sources**\n`.
       - Then one line per numeric id:
         - `[n] Title – URL`
     - Where `Title`:
       - Comes from the cluster titles near the end of the original file when available.
       - Falls back to a synthesized title if necessary.

8. `clean_markdown_text(text: str) -> str`
   - Orchestrates all steps:
     - Split front-matter vs body.
     - Decode entities/HTML.
     - Extract references and rewrite body.
     - Strip backslashes.
     - Normalize whitespace.
     - Append rendered Sources section.
     - Reattach front-matter.

9. `clean_markdown_file(path: Path) -> Path`
   - Wrapper around `clean_markdown_text` for filesystem IO.

---

## V. TEST-DRIVEN DEVELOPMENT (TDD) APPROACH

LLM_Developer should follow a TDD-style workflow. Below is a suggested test plan.

### A. Test Location & Structure

- Place tests under `tests/scripts/test_markdown_cleaner_deep_research.py` (or similar).
- Use pytest.
- Organize tests around **small behaviors** corresponding to the helper functions above.

### B. Core Test Categories

1. **Front-matter splitting**
   - Input: text with and without YAML front-matter.
   - Assert:
     - Front-matter is returned exactly as-is, including newlines.
     - Body starts immediately after second `---`.

2. **Entity & HTML decoding**
   - Inputs:
     - Strings containing `&lt;br/&gt;`, `&lt;small&gt;text&lt;/small&gt;`, `&lt;`, `&gt;`, `&amp;`.
   - Assert:
     - Entities decode correctly.
     - `<br/>` yields blank lines.
     - `<small>` tags are removed, but content remains.

3. **Citation extraction & rewriting**
   - Inputs:
     - Snippets like: `VWAP resets daily[\[1\]](https://example.com/a)` plus multi-citation examples.
   - Assert:
     - Body becomes: `VWAP resets daily[1]`.
     - Registry contains:
       - `number=1`, `url="https://example.com/a"`.
     - Multiple citations produce `[1][2]` or `[1] [2]`.

4. **URL normalization**
   - Inputs:
     - URLs with and without `#:~:text` fragments.
   - Assert:
     - Fragment `#:~:text=...` is removed.
     - Core URL remains.

5. **Descriptive links & bare URLs**
   - Inputs:
     - `See [TradingView docs](https://tradingview.com/...) for details.`
     - `See the guide (https://example.com/path).`
     - Soft and hard cases for `<https://example.com/>`.
   - Assert:
     - Inline text becomes as agreed (e.g. `See TradingView docs for details.`).
     - `(https://example.com/path)` tail removed.
     - URLs captured into registry.

6. **Backslash removal**
   - Inputs:
     - `This has \*escaped\* characters and \[brackets\].`
   - Assert:
     - Output: `This has *escaped* characters and [brackets].`

7. **Whitespace normalization**
   - Inputs:
     - Strings with extra blank lines and trailing spaces.
   - Assert:
     - No trailing spaces.
     - Max 2 consecutive blank lines.
     - Heading spacing fixed.

8. **Sources section rendering**
   - Setup:
     - Construct a `ReferenceRegistry` with:
       - Several numbered references.
       - Optional unindexed references.
   - Assert:
     - Rendered section starts with `**Sources**`.
     - Each numeric id has one line `[n]`.
     - No duplicates for the same id/url pair.

9. **End-to-end exemplar tests**
   - Use **fixtures** that contain trimmed-down versions of the two T801 reports.
   - Run `clean_markdown_text` and assert:
     - YAML block untouched.
     - All `[\[n\]](http...)` removed and converted to `[n]`.
     - No raw URLs like `(https://...)` remain in the body.
     - A Sources block exists at the end with entries for all cited URLs.
     - All backslashes removed from the body.

### C. Regression Safety

- Add tests that assert **unchanged behavior** for:
  - Lines that have no citations or URLs (should be passed through, aside from whitespace).
  - Tables and code blocks that contain no HTML-encoded elements.
- As new Deep Research artifacts appear, expand the fixtures and tests to cover new patterns.

---

## VI. DOCUMENTATION & USAGE GUIDE

LLM_Developer will create a dedicated documentation file, following the structure of `documentation/testing/prompt_reconstructor_guide.md`, at:

- `documentation/scripts/general/markdown_cleaner_deep_research_guide.md`

The guide should cover:

1. **Overview & Purpose**
   - What the script does and why it exists.
2. **Installation & Prerequisites**
   - Python version, project environment expectations.
3. **How to Run**
   - CLI examples (no-arg and with file arguments).
4. **Behavior Details**
   - What gets cleaned (citations, HTML, backslashes).
   - What is preserved (YAML front-matter, citation numbers).
   - Examples of before/after snippets (small).
5. **Limitations & Caveats**
   - Aggressive backslash removal.
   - Possible edge cases with unusual markdown.
6. **Extensibility**
   - How to extend the script for new patterns or future exports.

---

## VII. HANDOFF BRIEF TO LLM_DEVELOPER

A separate handoff brief will be created to give LLM_Developer a concise, implementation-focused summary. The brief will:

- Live at: `scripts/general/handoff_brief_markdown-cleaner_deep-research.md`.
- Follow the structural style of:
  - `prompt/artifacts/tasks/T810/consultant/workspace/communication/developer/handoff_brief_T810A2-SCHEMA_rid-normalization.md`.
- Include:
  - Problem statement.
  - Key requirements and constraints (especially “no change to numeric IDs” and “remove all backslashes”).
  - File locations and naming.
  - TDD expectations and core test matrix.
  - Implementation notes and edge cases drawn from the exemplar reports.

---

## VIII. IMPLEMENTATION CHECKLIST

The following checklist can be used by LLM_Developer to track progress:

1. **Scaffold script**
   - [ ] Create `scripts/general/markdown_cleaner_deep_research.py`.
   - [ ] Implement CLI interface (arg parsing, default file list).
2. **Core helpers**
   - [ ] `split_frontmatter`
   - [ ] `decode_entities_and_html`
   - [ ] `extract_references`
   - [ ] `normalize_reference_numbers`
   - [ ] `strip_backslashes`
   - [ ] `normalize_whitespace`
   - [ ] `render_sources_section`
   - [ ] `clean_markdown_text` and `clean_markdown_file`
3. **Tests**
   - [ ] Unit tests for each helper.
   - [ ] Integration tests on exemplar snippets.
   - [ ] Full end-to-end tests on sample T801 reports (or reduced fixtures).
4. **Documentation**
   - [ ] `documentation/scripts/general/markdown_cleaner_deep_research_guide.md` written and linked from any relevant index docs.
5. **Validation**
   - [ ] Run script on both T801 exemplar reports.
   - [ ] Manually spot-check:
     - No backslashes in body.
     - All citations preserved as `[n]`.
     - Clean, consolidated Sources section.

Once this checklist is complete and tests pass, the script will be ready for regular use in the Deep Research report workflow.

