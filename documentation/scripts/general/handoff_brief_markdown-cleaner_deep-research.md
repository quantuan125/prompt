---
artifact_type: 'HANDOFF_BRIEF'
initiative_id: 'T801'
epic_id: 'T801A'
version: '1.0.0'
date: '2025-11-30'
status: 'draft'
author: 'LLM_Consultant'
decision_owner_role: 'Client'
---

# LLM_DEVELOPER HANDOFF BRIEF: Deep Research Markdown Cleaner

## I. PURPOSE & CONTEXT

### A. Problem Statement

The client uses **ChatGPT Deep Research** to generate long-form research reports, exports them as `.words`, and converts them to Markdown via `word2md`. The resulting `.md` files contain:

- Inline numeric citation links (`[\[n\]](https://...)`) scattered throughout the text.
- Duplicate and noisy reference sections at the end (multiple `[\[n\]](url)` blocks plus bare `<https://...>` links).
- HTML entities and tags (`&lt;br/&gt;`, `&lt;small&gt;`, `&lt;`, `&gt;`, `&amp;`).
- Backslash escapes (`\*`, `\[`), which clutter diffs and readability.

The client wants a **generic Python script** that:

- Produces a cleaned version of each report in the same directory with `_CLEAN` suffix.
- Preserves content and citation numbers but removes conversion artifacts.
- Consolidates all sources into a single, well-structured **Sources** block.

### B. Exemplars

Initial implementation and tests should be grounded in:

- `prompt/artifacts/tasks/T801/research/report/report_T801-RES-001_indicator-design-standards.md`
- `prompt/artifacts/tasks/T801/research/report/report_T801A-RES-001_backend-tti-architecture.md`

Future Deep Research exports are expected to exhibit similar patterns.

---

## II. KEY REQUIREMENTS (DEVELOPER-FOCUSED)

### A. File & CLI Behavior

1. **Script location**
   - Implement as: `scripts/general/markdown_cleaner_deep_research.py`.

2. **Invocation**
   - No-arg mode:
     - `python scripts/general/markdown_cleaner_deep_research.py`
     - Cleans a default list of known Deep Research reports (configure inside script).
   - Arg mode:
     - `python scripts/general/markdown_cleaner_deep_research.py path/to/file1.md path/to/file2.md`
     - Cleans each specified file.

3. **Output**
   - For `path/to/report_X.md`, script writes `path/to/report_X_CLEAN.md`.
   - Never overwrite original files.

4. **Console output**
   - Print a short per-file summary:
     - `Cleaning: <src> -> <dst>`
     - `Original chars: N`
     - `Cleaned chars : M`
     - `Bytes saved   : N - M`

### B. Front-matter Handling

1. Detect YAML-like front-matter at the top:
   - From first `---` to the next `---` line inclusive.
2. Copy front-matter **verbatim**:
   - No modifications to keys, values, or quoting.
3. Apply all cleaning only to the body after the second `---`.

### C. Citations & URLs

1. Inline numeric citations:
   - Patterns:
     - `[\[n\]](http...)`
     - `_`-wrapped variants (`[_\[n\]_](http...)`) or similar.
   - Transform:
     - Replace in body with short-form `[n]`.
     - Example: `VWAP resets daily[\[1\]](https://...)` → `VWAP resets daily[1]`.
   - Capture:
     - Extract URL(s), strip `#:~:text=...` fragments, and store in reference registry keyed by `n`.
   - **Important constraint**: do **not** change the numeric ID (`n`) anywhere.

2. Multiple citations:
   - Example: `[\[19\]](url1)[\[20\]](url2)` → `[19][20]` (or `[19] [20]`, your choice).
   - Each numeric id should be tracked separately, even when pointing to the same host.

3. Bare URLs:
   - Patterns:
     - `(https://...)` tails at end of sentences.
     - `<https://...>` autolinks.
   - Transform:
     - Remove from body text.
   - Capture:
     - Add to registry (unindexed or associated with nearest numeric id if obvious).

4. Descriptive links:
   - Example: `[Some Article](https://example.com/...)`.
   - For now, keep the inline text as simple as possible (e.g. `Some Article`) and capture the URL.
   - If you choose to map these to citation numbers, preserve any existing numeric IDs; do not introduce new `[n]` markers into the body unless you are confident it will not confuse readers.

### D. Sources Section

1. Remove or bypass existing reference clusters near the end:
   - Lines with sequences of `[\[n\]](url)` followed by descriptive titles and `<https://...>` lines.

2. Reconstruct a single consolidated block at the very end of the document:
   - Start with:
     - `**Sources**`
   - Then one line per numeric citation id:
     - `[n] Title – URL`

3. Title handling:
   - Where existing titles are present (in today’s clusters), reuse them.
   - Otherwise, fall back to a synthesized label (e.g. `domain — path`).

4. Numeric ID constraints:
   - Preserve the IDs from the original report.
   - Do not renumber (e.g. 19 stays 19).
   - If URLs have no obvious numeric id, you may:
     - Group them as unnumbered sources, or
     - Leave them out of the first version if they are purely redundant with existing numbered entries (use judgment and tests).

### E. HTML & Backslashes

1. HTML entities:
   - Decode `&lt;`, `&gt;`, `&amp;`, and optionally `&nbsp;`, `&quot;`, `&apos;`.
2. HTML-like tags:
   - `<br/>` / `&lt;br/&gt;`:
     - Convert to blank lines (or hard breaks) for simple Markdown rendering.
   - `<small>` / `&lt;small&gt;`:
     - Remove tags, keep inner text.
3. Backslashes:
   - Remove **all** `\` characters from the body.
   - Apply this after regex-based extraction so patterns still match correctly.

### F. Whitespace & Formatting

1. Trim trailing whitespace on each line.
2. Collapse 3+ blank lines into at most 2 consecutive blank lines.
3. Ensure a space after heading hashes in the body:
   - `#Heading` → `# Heading`, etc.

---

## III. RECOMMENDED IMPLEMENTATION STRUCTURE

### A. Suggested Helper Functions

Implement small, testable functions:

1. `split_frontmatter(text: str) -> tuple[str | None, str]`
2. `decode_entities_and_html(body: str) -> str`
3. `extract_references(body: str) -> tuple[str, ReferenceRegistry]`
4. `normalize_reference_numbers(registry: ReferenceRegistry) -> ReferenceRegistry`
5. `strip_backslashes(body: str) -> str`
6. `normalize_whitespace(body: str) -> str`
7. `render_sources_section(registry: ReferenceRegistry) -> str`
8. `clean_markdown_text(text: str) -> str`
9. `clean_markdown_file(path: Path) -> Path`

`ReferenceRegistry` can be a simple dataclass or namedtuple-based structure with:

- `by_number: dict[int, list[Reference]]`
- `unindexed: list[Reference]`

Where `Reference` contains:

- `number: int | None`
- `url: str`
- `title_hint: str | None`
- `context: str | None`

### B. Code Style Expectations

- Use standard library only (no new dependencies).
- Clear, descriptive function names.
- Type hints where helpful.
- No side effects beyond printing summary output and writing `_CLEAN` files.

---

## IV. TDD STRATEGY & TEST MATRIX

### A. Test Location

- Add tests to `tests/scripts/test_markdown_cleaner_deep_research.py` (or similar).
- Use pytest.

### B. Core Test Cases

1. **Front-matter**
   - Given input with YAML header, ensure:
     - Header is returned unchanged.
     - Body is isolated correctly.

2. **Entity decoding**
   - `&lt;br/&gt;`, `&lt;small&gt;text&lt;/small&gt;`, `&lt;`, `&gt;`, `&amp;`.
   - Validate decoding and tag removal.

3. **Citation rewriting**
   - Single citation:
     - Input: `VWAP resets daily[\[1\]](https://example.com/a).`
     - Output: `VWAP resets daily[1].`
     - Registry: `number=1`, `url="https://example.com/a"`.
   - Multiple citations:
     - Input: `...[\[19\]](url1)[\[20\]](url2)...`
     - Output: `...[19][20]...`

4. **URL normalization**
   - URLs with `#:~:text=` fragments.
   - Confirm fragment removal.

5. **Bare URL cleanup**
   - Input: `See more (https://example.com/path).`
   - Output: `See more.`
   - URL is preserved in registry.

6. **Backslash removal**
   - Input: `\*escaped\* and \[brackets\].`
   - Output: `*escaped* and [brackets].`

7. **Whitespace normalization**
   - Multiple blank lines, trailing spaces.
   - Heading without space.
   - Assert normalized output.

8. **Sources rendering**
   - Given a registry with several numbered entries, ensure:
     - Block begins with `**Sources**`.
     - Lines follow `[n] Title – URL`.
     - No duplicate entries per numeric id.

9. **End-to-end fixtures**
   - Create trimmed fixtures based on the two T801 reports.
   - Assert:
     - YAML is unchanged.
     - All `[\[n\]](http...)` → `[n]`.
     - No raw `(http...)` or `<https://...>` in body.
     - Backslashes removed.
     - Sources block present with expected ids and sample URLs.

### C. Regression Considerations

- Add tests that confirm non-URL, non-citation content is left structurally intact.
- As additional Deep Research exports are onboarded, extend fixtures to cover new idiosyncrasies.

---

## V. DOCUMENTATION EXPECTATIONS

Create and maintain:

- `documentation/scripts/general/markdown_cleaner_deep_research_guide.md`

The guide should:

- Describe purpose and scope in non-technical language.
- Explain how to run the script (no-arg and with file paths).
- Summarize cleanup behavior and limitations (especially global backslash removal).
- Provide small, representative before/after examples.

This handoff brief plus the plan file:

- `scripts/general/plan_markdown-cleaner_deep-research.md`

together constitute the full specification for the initial implementation.

---

## VI. NEXT STEPS FOR LLM_DEVELOPER

1. Scaffold `markdown_cleaner_deep_research.py` and basic CLI interface.
2. Implement helper functions incrementally, writing tests **before** each behavior (TDD).
3. Validate against synthetic tests, then run on the two T801 exemplar reports.
4. Refine patterns based on any anomalies found.
5. Finalize documentation and ensure all tests pass.

After this, the script can be integrated into the normal workflow for Deep Research reports.

