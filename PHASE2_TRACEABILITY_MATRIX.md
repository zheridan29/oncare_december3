# Phase 2 Traceability Matrix

## Scope
This matrix links documented research and system-architecture claims to implemented code paths, API endpoints, and tests.

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

## Notes
- T6 currently relies on manual visual verification due interactive rendering behavior.
