# T300 Implementation Report

## Overview
- Added parsing, sanitization, and normalization safeguards for TradingView custom symbols flowing into the ingest pipeline.
- Followed the provided TDD roadmap (Red -> Green -> Refactor) with targeted unit coverage under `tests/components/tv_ingest`.
- Addressed the WinError 123 root cause where Windows rejected paths such as `components\\tv_ingest\\data\\={"adjustment"_"splits","symbol"_"BINANCE_LINKUSDT_BINANCE_AAVEUSDT"}` issued by `_ensure_symbol_directory`.

## Progress by Stage
- **Stage 0 - Test Harness Setup:** Created `tests/components/tv_ingest/__init__.py`, `unit/__init__.py`, and `conftest.py`; confirmed `pytest` discovered zero tests initially.
- **Stage 1 - Symbol Parsing Helper:** Wrote failing tests for `parse_tradingview_symbol`, implemented JSON/regex-based parsing with whitespace handling, and refactored with docstrings + type hints.
- **Stage 2 - Filename Sanitization:** Introduced tests covering invalid Windows characters and ensured sanitizer collapses unsafe characters; added `normalize_symbol_for_storage` helper for end-to-end checks.
- **Stage 3 - Ingestion Integration:** Added webhook processor tests using `tmp_path`; wired `get_symbol_directory` to the new normalizer so `_ensure_symbol_directory` creates safe folders for custom symbols.
- **Stage 4 - Regression & Acceptance:** Aggregated the new unit suite via `venv/bin/python -m pytest tests/components/tv_ingest/unit -q` (13 passed). Applied Option A from the reviewer handoff by correcting the archived test import to `from tests.archive.tdd_guard_experiment.math_helpers import calculate_percentage_change` so the full suite can execute.
- **Stage 5 - Suite Execution Follow-up:** Running `venv/bin/python -m pytest -m unit -q` now progresses past the archived import, but fails in `tests/prompt/unit/conversation_parsers/test_comparison_json_parser.py::TestComparisonJsonParser::test_merge_comparison_threads_functionality` because neither `ComparisonJsonParser.merge_threads` nor a `merged_view` attribute is present on the result object.

## Issues & Risks
- The full unit suite (`venv/bin/python -m pytest -m unit -q`) currently fails on `test_merge_comparison_threads_functionality`, which expects either a `merge_threads` helper or a `merged_view` on the parsed output. This behavior predates the symbol work and needs clarification from the prompt tooling maintainers.
- Coverage plugin messages now surface during test runs after moving `pytest_plugins` to the top-level `tests/conftest.py` to satisfy pytest 8 requirements. The plugin reports unmet quality gates but does not alter exit codes; confirm whether those gates should be disabled for non-coverage suites.

## Deliverable Checklist
- [x] Test harness package under `tests/components/tv_ingest` created.
- [x] `parse_tradingview_symbol` implemented with defensive fallbacks.
- [x] `sanitize_symbol_for_filename` hardened for Windows-safe output.
- [x] `normalize_symbol_for_storage` added and consumed by ingest directory logic.
- [x] Webhook `_ensure_symbol_directory` verified via unit tests.
- [x] Unit tests executed and passing in the targeted namespace.
- [x] Archived coverage example updated per Option A so imports resolve during suite runs.

## Tests Run
- `venv/bin/python -m pytest tests/components/tv_ingest/unit/test_symbol_parsing.py`
- `venv/bin/python -m pytest tests/components/tv_ingest/unit/test_symbol_sanitization.py`
- `venv/bin/python -m pytest tests/components/tv_ingest/unit/test_webhook_processor_symbol_handling.py`
- `venv/bin/python -m pytest tests/components/tv_ingest/unit -q`
- `venv/bin/python -m pytest -m unit -q` -> fails: `TestComparisonJsonParser::test_merge_comparison_threads_functionality` asserts missing `merge_threads`/`merged_view` support (full trace available from pytest output).
