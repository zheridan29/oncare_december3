from django.contrib import admin
from django.utils.html import format_html
from .models import DemandForecast, InventoryOptimization, SalesTrend, CustomerAnalytics, SystemMetrics


class DemandForecastAdmin(admin.ModelAdmin):
    """
    Admin interface for demand forecasts with ARIMA and SARIMAX comparison
    """
    list_display = [
        'medicine_name',
        'forecast_period',
        'forecast_horizon',
        'arima_params',
        'recommended_model_display',
        'arima_mape_display',
        'sarimax_mape_display',
        'improvement_display',
        'created_at',
    ]
    
    list_filter = ['forecast_period', 'created_at', 'medicine']
    search_fields = ['medicine__name']
    readonly_fields = [
        'created_at',
        'arima_params',
        'arima_info_display',
        'sarimax_info_display',
        'model_comparison_display',
        'exogenous_features_display',
        'forecasted_demand_display',
        'sarimax_forecast_display',
    ]
    
    fieldsets = (
        ('Forecast Configuration', {
            'fields': ('medicine', 'forecast_period', 'forecast_horizon'),
        }),
        ('ARIMA Model (Baseline)', {
            'fields': (
                'arima_params',
                'aic',
                'bic',
                'rmse',
                'mae',
                'mape',
                'forecasted_demand',
                'confidence_intervals',
                'arima_info_display',
            ),
        }),
        ('SARIMAX Model (Enhanced)', {
            'fields': (
                'sarimax_results',
                'exogenous_features_display',
                'sarimax_info_display',
                'sarimax_forecast_display',
            ),
        }),
        ('Model Comparison & Recommendation', {
            'fields': ('model_comparison_display',),
            'classes': ('collapse',),
        }),
        ('Training Data', {
            'fields': ('training_data_start', 'training_data_end', 'training_data_points'),
            'classes': ('collapse',),
        }),
        ('Metadata', {
            'fields': ('created_at', 'is_active'),
        }),
    )
    
    def medicine_name(self, obj):
        return obj.medicine.name
    medicine_name.short_description = 'Medicine'
    
    def arima_params(self, obj):
        return f"ARIMA({obj.arima_p},{obj.arima_d},{obj.arima_q})"
    arima_params.short_description = "ARIMA Order"
    
    def recommended_model_display(self, obj):
        recommended = obj.model_comparison.get('recommended_model', 'unknown')
        if recommended == 'arima':
            return format_html(
                '<span style="background-color: #90EE90; padding: 5px 10px; border-radius: 3px;"><strong>ARIMA</strong></span>'
            )
        elif recommended == 'sarimax':
            return format_html(
                '<span style="background-color: #87CEEB; padding: 5px 10px; border-radius: 3px;"><strong>SARIMAX</strong></span>'
            )
        else:
            return "Unknown"
    recommended_model_display.short_description = "Recommended"
    
    def arima_mape_display(self, obj):
        mape = obj.mape
        if mape < 10:
            color = '#90EE90'  # green
        elif mape < 20:
            color = '#FFD700'  # gold
        else:
            color = '#FFB6C6'  # light red
        mape_text = f"{mape:.2f}%"
        return format_html(
            '<span style="background-color: {}; padding: 5px 10px; border-radius: 3px;">{}</span>',
            color,
            mape_text
        )
    arima_mape_display.short_description = "ARIMA MAPE"
    
    def sarimax_mape_display(self, obj):
        sarimax_data = obj.sarimax_results
        if 'error' in sarimax_data:
            return format_html(
                '<span style="background-color: #FFB6C6; padding: 5px 10px; border-radius: 3px;">Error</span>'
            )
        mape = sarimax_data.get('mape')
        if mape is None:
            return '-'
        if mape < 10:
            color = '#90EE90'
        elif mape < 20:
            color = '#FFD700'
        else:
            color = '#FFB6C6'
        mape_text = f"{mape:.2f}%"
        return format_html(
            '<span style="background-color: {}; padding: 5px 10px; border-radius: 3px;">{}</span>',
            color,
            mape_text
        )
    sarimax_mape_display.short_description = "SARIMAX MAPE"
    
    def improvement_display(self, obj):
        improvement = obj.model_comparison.get('improvement_pct', {}).get('mape')
        if improvement is None:
            return '-'
        if improvement > 0:
            color = '#90EE90'
            symbol = '↓'  # downward arrow for better MAPE
        else:
            color = '#FFB6C6'
            symbol = '↑'
        improvement_text = f"{abs(improvement):.1f}%"
        return format_html(
            '<span style="background-color: {}; padding: 5px 10px; border-radius: 3px;">{} {}</span>',
            color,
            symbol,
            improvement_text
        )
    improvement_display.short_description = "MAPE Improvement"
    
    def arima_info_display(self, obj):
        info = (
            f"<b>Order:</b> ARIMA({obj.arima_p},{obj.arima_d},{obj.arima_q})<br/>"
            f"<b>AIC:</b> {obj.aic:.2f}<br/>"
            f"<b>BIC:</b> {obj.bic:.2f}<br/>"
            f"<b>RMSE:</b> {obj.rmse:.4f}<br/>"
            f"<b>MAE:</b> {obj.mae:.4f}<br/>"
            f"<b>MAPE:</b> {obj.mape:.2f}%"
        )
        return format_html(info)
    arima_info_display.short_description = "ARIMA Statistics"
    
    def sarimax_info_display(self, obj):
        sarimax = obj.sarimax_results
        if 'error' in sarimax and sarimax.get('error'):
            return format_html(
                '<span style="color: red;"><b>Error:</b> {}</span>',
                sarimax.get('error', 'Unknown error')
            )
        
        info = (
            f"<b>Order:</b> ARIMA({sarimax.get('order', {}).get('p', '-')},"
            f"{sarimax.get('order', {}).get('d', '-')},"
            f"{sarimax.get('order', {}).get('q', '-')})<br/>"
            f"<b>Seasonal:</b> ({sarimax.get('seasonal_order', {}).get('P', '-')},"
            f"{sarimax.get('seasonal_order', {}).get('D', '-')},"
            f"{sarimax.get('seasonal_order', {}).get('Q', '-')},"
            f"{sarimax.get('seasonal_order', {}).get('m', '-')})<br/>"
            f"<b>AIC:</b> {sarimax.get('aic', 'N/A')}<br/>"
            f"<b>BIC:</b> {sarimax.get('bic', 'N/A')}<br/>"
            f"<b>RMSE:</b> {sarimax.get('rmse', 'N/A')}<br/>"
            f"<b>MAE:</b> {sarimax.get('mae', 'N/A')}<br/>"
            f"<b>MAPE:</b> {sarimax.get('mape', 'N/A')}%"
        )
        return format_html(info)
    sarimax_info_display.short_description = "SARIMAX Statistics"
    
    def model_comparison_display(self, obj):
        comparison = obj.model_comparison
        recommended = comparison.get('recommended_model', 'unknown').upper()
        arima_stats = comparison.get('arima', {})
        sarimax_stats = comparison.get('sarimax', {})
        improvement = comparison.get('improvement_pct', {})
        
        # Format SARIMAX metrics safely
        sarimax_rmse = f"{sarimax_stats.get('rmse', 'N/A'):.4f}" if isinstance(sarimax_stats.get('rmse', 'N/A'), (int, float)) else 'N/A'
        sarimax_mae = f"{sarimax_stats.get('mae', 'N/A'):.4f}" if isinstance(sarimax_stats.get('mae', 'N/A'), (int, float)) else 'N/A'
        sarimax_mape = f"{sarimax_stats.get('mape', 'N/A'):.2f}%" if isinstance(sarimax_stats.get('mape', 'N/A'), (int, float)) else 'N/A'
        
        html = (
            f"<h3>Model Comparison Summary</h3>"
            f"<table style='border-collapse: collapse; width: 100%;'>"
            f"<tr style='background-color: #f0f0f0;'>"
            f"<th style='border: 1px solid #ddd; padding: 8px;'>Metric</th>"
            f"<th style='border: 1px solid #ddd; padding: 8px;'>ARIMA</th>"
            f"<th style='border: 1px solid #ddd; padding: 8px;'>SARIMAX</th>"
            f"<th style='border: 1px solid #ddd; padding: 8px;'>Improvement (%)</th>"
            f"</tr>"
            f"<tr>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'><b>RMSE</b></td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>{arima_stats.get('rmse', 'N/A'):.4f}</td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>{sarimax_rmse}</td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>{improvement.get('rmse', 'N/A')}</td>"
            f"</tr>"
            f"<tr style='background-color: #f9f9f9;'>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'><b>MAE</b></td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>{arima_stats.get('mae', 'N/A'):.4f}</td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>{sarimax_mae}</td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>{improvement.get('mae', 'N/A')}</td>"
            f"</tr>"
            f"<tr>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'><b>MAPE (%)</b></td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>{arima_stats.get('mape', 'N/A'):.2f}%</td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>{sarimax_mape}</td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>{improvement.get('mape', 'N/A')}</td>"
            f"</tr>"
            f"</table>"
            f"<br/>"
            f"<h4>Recommendation: <span style='background-color: #87CEEB; padding: 5px 10px; border-radius: 3px;'><strong>{recommended}</strong></span></h4>"
        )
        return format_html(html)
    model_comparison_display.short_description = "Model Comparison"
    
    def exogenous_features_display(self, obj):
        features = obj.exogenous_features
        if not features:
            return "No exogenous features used"
        feature_list = "<ul>"
        for feature in features:
            feature_list += f"<li>{feature}</li>"
        feature_list += "</ul>"
        return format_html(feature_list)
    exogenous_features_display.short_description = "Exogenous Features Used"
    
    def forecasted_demand_display(self, obj):
        values = obj.forecasted_demand
        if not values:
            return "No forecast values"
        forecast_str = ", ".join([f"{v:.2f}" for v in values[:5]])
        if len(values) > 5:
            forecast_str += f", ... ({len(values)} total)"
        return forecast_str
    forecasted_demand_display.short_description = "ARIMA Forecast Values"
    
    def sarimax_forecast_display(self, obj):
        sarimax = obj.sarimax_results
        values = sarimax.get('forecasted_demand', [])
        if not values:
            return "No forecast values"
        forecast_str = ", ".join([f"{v:.2f}" for v in values[:5]])
        if len(values) > 5:
            forecast_str += f", ... ({len(values)} total)"
        return forecast_str
    sarimax_forecast_display.short_description = "SARIMAX Forecast Values"
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


class InventoryOptimizationAdmin(admin.ModelAdmin):
    """
    Admin interface for inventory optimization results
    """
    list_display = [
        'medicine_name',
        'optimal_reorder_point',
        'optimal_order_quantity',
        'safety_stock',
        'service_level_display',
        'total_cost_display',
        'calculated_at',
    ]
    
    list_filter = ['service_level', 'calculated_at', 'medicine']
    search_fields = ['medicine__name']
    readonly_fields = [
        'calculated_at',
        'cost_breakdown_display',
    ]
    
    fieldsets = (
        ('Medicine & Configuration', {
            'fields': ('medicine', 'demand_forecast', 'service_level', 'lead_time_days', 'holding_cost_percentage'),
        }),
        ('Optimal Inventory Levels', {
            'fields': (
                'optimal_reorder_point',
                'optimal_order_quantity',
                'optimal_maximum_stock',
                'safety_stock',
            ),
        }),
        ('Cost Analysis', {
            'fields': (
                'expected_holding_cost',
                'expected_stockout_cost',
                'total_expected_cost',
                'cost_breakdown_display',
            ),
        }),
        ('Metadata', {
            'fields': ('calculated_at', 'is_active'),
        }),
    )
    
    def medicine_name(self, obj):
        return obj.medicine.name
    medicine_name.short_description = 'Medicine'
    
    def service_level_display(self, obj):
        return f"{obj.service_level:.0f}%"
    service_level_display.short_description = "Service Level"
    
    def total_cost_display(self, obj):
        total_cost_text = f"${obj.total_expected_cost:.2f}"
        return format_html(
            '<span style="background-color: #FFD700; padding: 5px 10px; border-radius: 3px;">{}</span>',
            total_cost_text
        )
    total_cost_display.short_description = "Total Expected Cost"
    
    def cost_breakdown_display(self, obj):
        html = (
            f"<table style='border-collapse: collapse; width: 100%;'>"
            f"<tr style='background-color: #f0f0f0;'>"
            f"<th style='border: 1px solid #ddd; padding: 8px;'>Cost Type</th>"
            f"<th style='border: 1px solid #ddd; padding: 8px;'>Amount</th>"
            f"</tr>"
            f"<tr>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>Holding Cost</td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>${obj.expected_holding_cost:.2f}</td>"
            f"</tr>"
            f"<tr style='background-color: #f9f9f9;'>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>Stockout Cost</td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'>${obj.expected_stockout_cost:.2f}</td>"
            f"</tr>"
            f"<tr>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'><b>Total Cost</b></td>"
            f"<td style='border: 1px solid #ddd; padding: 8px;'><b>${obj.total_expected_cost:.2f}</b></td>"
            f"</tr>"
            f"</table>"
        )
        return format_html(html)
    cost_breakdown_display.short_description = "Cost Breakdown"
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


class SalesTrendAdmin(admin.ModelAdmin):
    """
    Admin interface for sales trends
    """
    list_display = [
        'medicine_name',
        'period_type',
        'period_date',
        'quantity_sold',
        'revenue_display',
        'growth_rate_display',
        'trend_direction',
    ]
    
    list_filter = ['period_type', 'trend_direction', 'period_date', 'medicine']
    search_fields = ['medicine__name']
    readonly_fields = ['created_at']
    
    def medicine_name(self, obj):
        return obj.medicine.name
    medicine_name.short_description = 'Medicine'
    
    def revenue_display(self, obj):
        return f"${float(obj.revenue):.2f}"
    revenue_display.short_description = "Revenue"
    
    def growth_rate_display(self, obj):
        if obj.growth_rate is None:
            return '-'
        if obj.growth_rate > 0:
            color = '#90EE90'
        else:
            color = '#FFB6C6'
        growth_rate_text = f"{obj.growth_rate:.2f}%"
        return format_html(
            '<span style="background-color: {}; padding: 5px 10px; border-radius: 3px;">{}</span>',
            color,
            growth_rate_text
        )
    growth_rate_display.short_description = "Growth Rate"


class CustomerAnalyticsAdmin(admin.ModelAdmin):
    """
    Admin interface for customer analytics
    """
    list_display = [
        'customer_display',
        'customer_segment',
        'total_orders',
        'total_spent_display',
        'order_frequency',
        'return_rate_display',
        'last_updated',
    ]
    
    list_filter = ['customer_segment', 'last_updated']
    search_fields = ['customer__username', 'customer__email']
    readonly_fields = ['created_at', 'last_updated']
    
    def customer_display(self, obj):
        return f"{obj.customer.username} ({obj.customer.email})"
    customer_display.short_description = "Customer"
    
    def total_spent_display(self, obj):
        return f"${float(obj.total_spent):.2f}"
    total_spent_display.short_description = "Total Spent"
    
    def order_frequency(self, obj):
        if obj.order_frequency_days is None:
            return '-'
        return f"{obj.order_frequency_days} days"
    order_frequency.short_description = "Order Frequency"
    
    def return_rate_display(self, obj):
        return f"{obj.return_rate:.2f}%"
    return_rate_display.short_description = "Return Rate"
    
    def has_add_permission(self, request):
        return False


class SystemMetricsAdmin(admin.ModelAdmin):
    """
    Admin interface for system-wide metrics
    """
    list_display = [
        'period_display',
        'period_date',
        'total_orders',
        'total_revenue_display',
        'total_customers',
        'inventory_turnover_display',
        'system_uptime_display',
    ]
    
    list_filter = ['period_type', 'period_date']
    readonly_fields = ['created_at']
    
    def period_display(self, obj):
        return f"{obj.get_period_type_display()} - {obj.period_date}"
    period_display.short_description = "Period"
    
    def total_revenue_display(self, obj):
        return f"${float(obj.total_revenue):.2f}"
    total_revenue_display.short_description = "Total Revenue"
    
    def inventory_turnover_display(self, obj):
        return f"{obj.inventory_turnover:.2f}"
    inventory_turnover_display.short_description = "Inventory Turnover"
    
    def system_uptime_display(self, obj):
        uptime_text = f"{obj.system_uptime:.2f}%"
        return format_html(
            '<span style="background-color: #90EE90; padding: 5px 10px; border-radius: 3px;">{}</span>',
            uptime_text
        )
    system_uptime_display.short_description = "System Uptime"
    
    def has_add_permission(self, request):
        return False


# Register models
admin.site.register(DemandForecast, DemandForecastAdmin)
admin.site.register(InventoryOptimization, InventoryOptimizationAdmin)
admin.site.register(SalesTrend, SalesTrendAdmin)
admin.site.register(CustomerAnalytics, CustomerAnalyticsAdmin)
admin.site.register(SystemMetrics, SystemMetricsAdmin)
