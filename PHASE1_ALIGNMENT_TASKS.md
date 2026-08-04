# Phase 1 Alignment Tasks

## Goal
Bring the forecasting implementation closer to the documented research claims by improving the SARIMAX workflow, exposing clearer model comparison evidence, and validating the behavior.

## Checklist

### 1. Forecasting core alignment
- [x] Add a period-aware SARIMAX seasonal order helper
- [x] Use the helper when building the SARIMAX model
- [x] Include the seasonal order in the stored SARIMAX results
- [ ] Verify the helper against real forecasting data

### 2. Model comparison evidence
- [x] Preserve ARIMA vs SARIMAX metrics in model_comparison
- [x] Expose a clearer recommended-model summary in the UI/API
- [x] Add a forecast explanation section for the selected model

### 3. Validation and regression coverage
- [x] Add a regression test for the seasonal order helper
- [ ] Run the regression test successfully in the project environment
- [ ] Add a higher-level forecast-generation test using real data

### 4. Documentation and traceability
- [x] Update the alignment report with the implemented improvements
- [x] Link each document claim to the corresponding code path
