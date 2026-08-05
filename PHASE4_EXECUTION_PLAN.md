# Phase 4 Execution Plan

## Purpose
Define a practical, test-first plan for post-alignment development after Phase 3 closeout and pre-Phase 4 hardening.

## Preconditions (Completed)
- Phase 3 sections 1-4 completed and documented.
- Pre-Phase 4 hardening completed:
  - Full analytics regression baseline (`analytics` suite) passed.
  - Audit review surface for forecast model decisions added (UI + API + tests).
  - Settings hardened for environment-driven deployment with compatibility fallback.
  - Django system checks passing.

## Phase 4 Goals
1. Expand forecasting reliability and observability.
2. Improve analytics operational workflows for pharmacy/admin users.
3. Tighten deployment readiness and runtime safety.

## Workstreams

### W1. Forecasting Reliability Improvements
- Add explicit alert thresholds for forecast quality drift (MAPE/RMSE bands).
- Add retry/backoff visibility for forecast generation failures.
- Add regression tests for low-data and noisy seasonal edge cases.

### W2. Analytics Workflow Enhancements
- Add a small "model-decision timeline" panel on analytics dashboard from audits API.
- Add filtering by medicine and period for model-decision audits.
- Add CSV export endpoint for model decision audit records.

### W3. Deployment and Configuration Safety
- Add documented `.env` template for DB/hosts/logging variables.
- Add startup checks/warnings for missing critical env vars.
- Validate `settings.py` and `settings_production.py` parity for core keys.

### W4. Test and Quality Gates
- Maintain a focused pre-merge suite:
  - `analytics`
  - `audits`
- Add a CI checklist document for local and staging verification.

## Acceptance Criteria
1. All new forecast reliability tests pass.
2. New analytics operational views/API have deterministic tests.
3. No hardcoded credentials in active settings.
4. `manage.py check` passes under local and production-like env configs.
5. Updated traceability entries map new Phase 4 requirements to tests.

## Suggested Execution Sequence
1. W3 first (config safety foundation).
2. W1 second (forecast quality/stability).
3. W2 third (operational UX/API improvements).
4. W4 continuously across all workstreams.

## Initial Test Commands
1. `venv/Scripts/python.exe manage.py test analytics audits --verbosity 1 --keepdb --noinput`
2. `venv/Scripts/python.exe manage.py check`
