# Development Plan: Refactor `svc_tv_ingest.py`

**Version:** 1.0.0
**Component:** `tv_ingest`
**Author:** Gemini (Technical Program Manager)

## 1. Objective

Refactor the `TvIngestService` to align with the project's "gold standard" service architecture, as exemplified by `ClosingPositionService`. The goal is to create a lean, focused service layer that orchestrates the core business logic of webhook ingestion and delegates all other responsibilities to the appropriate components.

## 2. Proposed Changes

### 2.1. Simplify `TvIngestService`

The `TvIngestService` will be streamlined to focus solely on orchestrating the webhook ingestion process.

**File:** `components/tv_ingest/service/svc_tv_ingest.py`

**Modifications:**

1.  **Remove Delegated Methods:** Remove all methods that are simple wrappers around `CsvRepository` or `TvIngestDataProcessor`. The UI or other services should interact with these components directly if they need access to that functionality. The methods to be removed are:
    *   `get_available_symbols`
    *   `get_available_timeframes`
    *   `get_data`
    *   `export_data_as_csv`
    *   `clear_data`
    *   `backup_data`
    *   `get_data_summary`
    *   `validate_webhook_payload`
    *   `get_processor_status`
    *   `format_data_for_display`
    *   `get_latest_data`
    *   `export_to_csv`
    *   `export_to_json`
    *   `get_file_info`
    *   `get_llm_context_data`

2.  **Retain Core Orchestration Methods:** The service will retain the methods essential for its primary function.
    *   `__init__`: Will continue to initialize the `CsvRepository` and `TvIngestDataProcessor`.
    *   `render`: Will remain as the entry point for the UI.
    *   `ingest_webhook`: This is the core orchestration method and will be kept.

3.  **Refine `ingest_webhook`:**
    *   Ensure it has robust error handling and logging, similar to the methods in `ClosingPositionService`.

### 2.2. Update `TvIngestFrontendBuilder` (if necessary)

The `TvIngestFrontendBuilder` will be updated to interact directly with the `CsvRepository` and `TvIngestDataProcessor` for data retrieval and other operations that were previously handled by the service.

**File:** `components/tv_ingest/frontend_builder/fb_tv_ingest.py`

**Modifications:**

1.  **Instantiate Dependencies:** The builder will instantiate `CsvRepository` and `TvIngestDataProcessor` directly.
2.  **Update Method Calls:** All calls to the removed service methods will be updated to call the corresponding methods on the repository or data processor. For example, a call to `service.get_available_symbols()` will become `repo.get_available_symbols()`.

### 2.3. Create/Update `CsvRepository` (if necessary)

The `CsvRepository` will be reviewed to ensure it contains all the necessary methods for data management that were previously in the service.

**File:** `components/tv_ingest/backend/processors/csv_repository.py`

**Modifications:**

1.  **Ensure Comprehensive Interface:** Verify that the repository has a complete and well-documented interface for all CRUD (Create, Read, Update, Delete) operations on the CSV data. Add any missing methods that were previously in the service.

## 3. Testing

-   **Unit Tests:** Review and update the unit tests for `svc_tv_ingest.py` to reflect the reduced interface.
-   **Integration Tests:** Create or update integration tests to ensure the `TvIngestFrontendBuilder` correctly interacts with the `CsvRepository` and `TvIngestDataProcessor`.
-   **Manual Testing:** Manually test the "Pine Script Data" page in the Streamlit application to verify that all functionality works as expected after the refactoring.

## 4. Documentation

-   **Update `main.md`:** Update the `main.md` file for the `tv_ingest` component to reflect the new architecture.
-   **Update `change_history.md`:** Add an entry to the `change_history.md` file for this refactoring, with a version bump.