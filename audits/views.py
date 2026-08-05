from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import AuditLog, SecurityEvent, SystemHealth, ComplianceLog  # Add missing model imports
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.http import JsonResponse
from django.views import View
from django.db.models import Avg, Count, Q
from datetime import datetime, timedelta
from django.utils import timezone

class AuditDashboardView(TemplateView):
    template_name = "audits/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()

        context['total_audit_logs'] = AuditLog.objects.count()
        context['security_events'] = SecurityEvent.objects.filter(status__in=['open', 'investigating']).count()
        context['system_health_issues'] = SystemHealth.objects.filter(
            is_healthy=False,
            recorded_at__gte=now - timedelta(hours=24)
        ).count()
        context['compliance_violations'] = ComplianceLog.objects.filter(
            is_compliant=False,
            checked_at__gte=now - timedelta(days=30)
        ).count()

        context['model_decision_audit_count'] = AuditLog.objects.filter(
            module='analytics',
            function_name='ARIMAForecastingService.generate_forecast',
        ).count()
        context['recent_model_decision_logs'] = AuditLog.objects.filter(
            module='analytics',
            function_name='ARIMAForecastingService.generate_forecast',
        ).order_by('-timestamp')[:8]

        return context

class AuditLogListView(ListView):
    model = AuditLog
    template_name = "audits/auditlog_list.html"
    context_object_name = "audit_logs"
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset().select_related('user')

        action = self.request.GET.get('action')
        if action:
            queryset = queryset.filter(action=action)

        severity = self.request.GET.get('severity')
        if severity:
            queryset = queryset.filter(severity=severity)

        username = self.request.GET.get('user')
        if username:
            queryset = queryset.filter(user__username__icontains=username)

        module = self.request.GET.get('module')
        if module:
            queryset = queryset.filter(module__icontains=module)

        forecast_decisions = self.request.GET.get('forecast_decisions')
        if forecast_decisions == '1':
            queryset = queryset.filter(
                module='analytics',
                function_name='ARIMAForecastingService.generate_forecast',
            )

        return queryset.order_by('-timestamp')

class AuditLogDetailView(DetailView):
    model = AuditLog
    template_name = "audits/auditlog_detail.html"
    context_object_name = "audit_log"
    # ...existing code...

class SecurityEventListView(ListView):
    model = SecurityEvent
    template_name = "audits/securityevent_list.html"
    context_object_name = "security_events"
    # ...existing code...

class SecurityEventDetailView(DetailView):
    model = SecurityEvent
    template_name = "audits/securityevent_detail.html"
    context_object_name = "security_event"
    # ...existing code...

class SecurityEventResolveView(UpdateView):
    model = SecurityEvent
    fields = ['status', 'resolved_by', 'resolution_notes', 'resolved_at']  # Use model fields for resolving
    template_name = "audits/securityevent_resolve.html"
    context_object_name = "security_event"
    success_url = reverse_lazy('audits:security_event_list')  # Use correct URL name

class SystemHealthListView(ListView):
    model = SystemHealth
    template_name = "audits/systemhealth_list.html"
    context_object_name = "system_health_metrics"
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by metric type if provided
        metric_type = self.request.GET.get('metric_type')
        if metric_type:
            queryset = queryset.filter(metric_type=metric_type)
        return queryset

class SystemHealthMetricsView(TemplateView):
    template_name = "audits/systemhealth_metrics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get recent metrics (last 24 hours)
        recent_metrics = SystemHealth.objects.filter(
            recorded_at__gte=datetime.now() - timedelta(days=1)
        )
        
        # Group by metric type and get latest values
        metrics_by_type = {}
        for metric in recent_metrics:
            if metric.metric_type not in metrics_by_type:
                metrics_by_type[metric.metric_type] = []
            metrics_by_type[metric.metric_type].append(metric)
        
        # Get latest value for each metric type
        latest_metrics = {}
        for metric_type, metrics in metrics_by_type.items():
            latest_metrics[metric_type] = max(metrics, key=lambda x: x.recorded_at)
        
        context['latest_metrics'] = latest_metrics
        context['unhealthy_metrics'] = SystemHealth.objects.filter(
            is_healthy=False,
            recorded_at__gte=datetime.now() - timedelta(hours=1)
        )
        
        return context

class ComplianceLogListView(ListView):
    model = ComplianceLog
    template_name = "audits/compliancelog_list.html"
    context_object_name = "compliance_logs"
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by compliance type if provided
        compliance_type = self.request.GET.get('compliance_type')
        if compliance_type:
            queryset = queryset.filter(compliance_type=compliance_type)
        # Filter by compliance status if provided
        is_compliant = self.request.GET.get('is_compliant')
        if is_compliant is not None:
            queryset = queryset.filter(is_compliant=is_compliant.lower() == 'true')
        return queryset

class ComplianceLogDetailView(DetailView):
    model = ComplianceLog
    template_name = "audits/compliancelog_detail.html"
    context_object_name = "compliance_log"

# API Views
class AuditLogAPIView(View):
    def get(self, request):
        logs = AuditLog.objects.all().order_by('-timestamp')

        module = request.GET.get('module')
        if module:
            logs = logs.filter(module__icontains=module)

        forecast_decisions = request.GET.get('forecast_decisions')
        if forecast_decisions == '1':
            logs = logs.filter(
                module='analytics',
                function_name='ARIMAForecastingService.generate_forecast',
            )

        try:
            limit = min(int(request.GET.get('limit', 100)), 500)
        except ValueError:
            limit = 100

        logs = logs[:limit]

        data = []
        for log in logs:
            data.append({
                'id': log.id,
                'user': log.user.username if log.user else 'Anonymous',
                'action': log.action,
                'severity': log.severity,
                'description': log.description,
                'timestamp': log.timestamp.isoformat(),
                'ip_address': str(log.ip_address),
                'module': log.module,
                'function_name': log.function_name,
                'recommended_model': log.metadata.get('recommended_model') if isinstance(log.metadata, dict) else None,
                'fallback_used': log.metadata.get('fallback_used') if isinstance(log.metadata, dict) else None,
                'fallback_reason': log.metadata.get('fallback_reason') if isinstance(log.metadata, dict) else None,
            })
        return JsonResponse({'audit_logs': data})


class ModelDecisionAuditAPIView(View):
    def get(self, request):
        logs = AuditLog.objects.filter(
            module='analytics',
            function_name='ARIMAForecastingService.generate_forecast',
        ).order_by('-timestamp')[:100]

        data = []
        for log in logs:
            metadata = log.metadata if isinstance(log.metadata, dict) else {}
            data.append({
                'id': log.id,
                'timestamp': log.timestamp.isoformat(),
                'description': log.description,
                'severity': log.severity,
                'forecast_id': metadata.get('forecast_id'),
                'medicine_id': metadata.get('medicine_id'),
                'forecast_period': metadata.get('forecast_period'),
                'recommended_model': metadata.get('recommended_model'),
                'recommendation_explanation': metadata.get('recommendation_explanation'),
                'fallback_used': metadata.get('fallback_used'),
                'fallback_reason': metadata.get('fallback_reason'),
            })

        return JsonResponse({'model_decision_audits': data})

class SecurityEventAPIView(View):
    def get(self, request):
        events = SecurityEvent.objects.all()[:100]  # Limit to 100 recent events
        data = []
        for event in events:
            data.append({
                'id': event.id,
                'event_type': event.event_type,
                'severity': event.severity,
                'status': event.status,
                'description': event.description,
                'detected_at': event.detected_at.isoformat(),
                'ip_address': str(event.ip_address),
                'auto_blocked': event.auto_blocked,
            })
        return JsonResponse({'security_events': data})

class SystemHealthAPIView(View):
    def get(self, request):
        # Get latest metrics for each type
        latest_metrics = {}
        for metric_type, _ in SystemHealth.METRIC_TYPES:
            latest = SystemHealth.objects.filter(metric_type=metric_type).first()
            if latest:
                latest_metrics[metric_type] = {
                    'value': latest.value,
                    'unit': latest.unit,
                    'is_healthy': latest.is_healthy,
                    'status': latest.status,
                    'recorded_at': latest.recorded_at.isoformat(),
                }
        
        return JsonResponse({'system_health': latest_metrics})

class ComplianceAPIView(View):
    def get(self, request):
        logs = ComplianceLog.objects.all()[:100]  # Limit to 100 recent logs
        data = []
        for log in logs:
            data.append({
                'id': log.id,
                'compliance_type': log.compliance_type,
                'requirement': log.requirement,
                'is_compliant': log.is_compliant,
                'violation_severity': log.violation_severity,
                'checked_at': log.checked_at.isoformat(),
            })
        return JsonResponse({'compliance_logs': data})

# Create your views here.
