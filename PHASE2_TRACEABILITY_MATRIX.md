# Phase 2-3 Traceability Matrix

## Scope
This matrix links documented research and system-architecture claims to implemented code paths, API endpoints, UI surfaces, and test evidence for Phase 2 and Phase 3.

## Matrix

| ID | Claim / Requirement | Code Path | Endpoint / UI Surface | Verification |
|---|---|---|---|---|
| T1 | Use ARIMA and SARIMAX for demand forecasting | analytics/services.py -> ARIMAForecastingService.generate_forecast | /analytics/api/forecast/generate/ | analytics/tests.py -> ARIMAForecastingServiceTests.test_generate_forecast_with_seeded_monthly_sales_data_returns_model_explanation |
| T2 | Use period-aware seasonal settings for SARIMAX | analytics/services.py -> ARIMAForecastingService._get_sarimax_seasonal_order | Stored under DemandForecast.sarimax_results.seasonal_order | analytics/tests.py -> ARIMAForecastingServiceTests.test_get_sarimax_seasonal_order_uses_period_specific_defaults |
| T3 | Compare ARIMA vs SARIMAX and choose a recommended model | analytics/services.py -> ARIMAForecastingService._build_model_comparison | /analytics/api/forecast/<id>/data/ and dashboard comparison panel | analytics/tests.py -> ARIMAForecastingServiceTests.test_generate_forecast_with_seeded_monthly_sales_data_returns_model_explanation |
| T4 | Provide explicit model selection explanation | analytics/services.py -> _build_model_comparison (recommendation_explanation) | analytics/api_views.py -> get_forecast_data, generate_forecast; templates/analytics/dashboard.html -> updateModelComparisonPanel | analytics/tests.py -> AnalyticsForecastAPITests.test_forecast_data_api_includes_comparison_summary_explanation |
| T5 | Expose seasonal order and exogenous features in API summary | analytics/api_views.py -> comparison_summary assembly | /analytics/api/forecast/<id>/data/ | analytics/tests.py -> AnalyticsForecastAPITests.test_forecast_data_api_includes_comparison_summary_explanation |
| T6 | Show analytics step-by-step SARIMAX visual workflow | analytics/views.py -> sarimax_step_by_step_view; analytics/step_analysis.py -> generate_sarimax_step_analysis | /analytics/sarimax-step-by-step/ | Manual verification on Steps 1-5 page behavior and rendering fixes |
| T7 | Handle sparse/non-seasonal exogenous inputs safely with explicit fallback reason | analytics/services.py -> generate_forecast (fallback branch when sanitized exogenous features are empty) | Persisted DemandForecast.sarimax_results fallback fields | analytics/tests.py -> ARIMAForecastingServiceTests.test_generate_forecast_falls_back_when_exogenous_features_are_not_stable |
| T8 | Ensure generate -> fetch workflow preserves consistent comparison summary across API surfaces | analytics/api_views.py -> generate_forecast, get_forecast_data | /analytics/api/forecast/generate/, /analytics/api/forecast/<id>/data/ | analytics/tests.py -> AnalyticsForecastWorkflowAPITests.test_generate_then_fetch_forecast_api_workflow_returns_consistent_model_summary |
| T9 | Ensure model explanation parity across dashboard, forecast decision, and SARIMAX step-by-step surfaces | templates/analytics/dashboard.html, templates/analytics/forecast_decision.html, templates/analytics/sarimax_step_by_step.html | /analytics/, /analytics/forecast-decision/, /analytics/sarimax-step-by-step/ | analytics/tests.py -> AnalyticsUIExplanationParityTests (all methods) |
| T10 | Persist operational audit evidence for model decision, explanation, and fallback state | analytics/signals.py -> log_forecast_model_decision; analytics/apps.py -> AnalyticsConfig.ready | AuditLog entries linked to DemandForecast records | analytics/tests.py -> AnalyticsOperationalEvidenceTests.test_forecast_creation_persists_model_decision_audit_entry |
| T11 | Validate fallback reason remains operationally reviewable through API payload and audit metadata | analytics/api_views.py -> get_forecast_data; analytics/signals.py -> metadata capture | /analytics/api/forecast/<id>/data/ and audits.AuditLog metadata | analytics/tests.py -> AnalyticsOperationalEvidenceTests.test_fallback_reason_is_persisted_and_available_for_operational_review |

## Notes
- T6 currently relies on manual visual verification due interactive rendering behavior.
- T8-T11 represent Phase 3 closure evidence and expand this matrix beyond initial Phase 2 scope.
