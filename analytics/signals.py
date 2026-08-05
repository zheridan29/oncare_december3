import logging

from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from audits.models import AuditLog

from .models import DemandForecast


logger = logging.getLogger(__name__)


@receiver(post_save, sender=DemandForecast)
def log_forecast_model_decision(sender, instance, created, **kwargs):
    """Persist model-decision audit evidence whenever a forecast is first created."""
    if not created:
        return

    comparison = instance.model_comparison or {}
    sarimax = instance.sarimax_results or {}

    recommended_model = comparison.get('recommended_model', 'unknown')
    recommendation_explanation = comparison.get('recommendation_explanation', '')
    fallback_used = bool(sarimax.get('fallback_used'))
    fallback_reason = sarimax.get('fallback_reason', '')

    try:
        AuditLog.objects.create(
            user=None,
            action='create',
            severity='medium' if fallback_used else 'low',
            content_type=ContentType.objects.get_for_model(DemandForecast),
            object_id=instance.id,
            ip_address='127.0.0.1',
            user_agent='system-analytics-forecasting-service',
            session_key='',
            description=(
                f"Forecast model decision recorded for medicine={instance.medicine_id} "
                f"forecast_id={instance.id}: recommended_model={recommended_model}, "
                f"fallback_used={fallback_used}"
            ),
            old_values=None,
            new_values={
                'recommended_model': recommended_model,
                'recommendation_explanation': recommendation_explanation,
                'fallback_used': fallback_used,
                'fallback_reason': fallback_reason,
            },
            changed_fields=['model_comparison', 'sarimax_results'],
            module='analytics',
            function_name='ARIMAForecastingService.generate_forecast',
            request_path='/analytics/api/forecast/generate/',
            request_method='POST',
            metadata={
                'forecast_id': instance.id,
                'medicine_id': instance.medicine_id,
                'forecast_period': instance.forecast_period,
                'forecast_horizon': instance.forecast_horizon,
                'recommended_model': recommended_model,
                'recommendation_explanation': recommendation_explanation,
                'fallback_used': fallback_used,
                'fallback_reason': fallback_reason,
            },
        )

        logger.info(
            "Forecast audit recorded: forecast_id=%s medicine_id=%s recommended_model=%s fallback_used=%s",
            instance.id,
            instance.medicine_id,
            recommended_model,
            fallback_used,
        )
    except Exception as exc:
        logger.error(
            "Failed to persist forecast audit log for forecast_id=%s: %s",
            instance.id,
            exc,
        )
