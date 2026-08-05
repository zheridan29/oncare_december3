from django.test import TestCase, Client
from django.urls import reverse

from .models import AuditLog


class AuditModelDecisionReviewTests(TestCase):
	def setUp(self):
		self.client = Client()

		self.forecast_audit = AuditLog.objects.create(
			user=None,
			action='create',
			severity='medium',
			ip_address='127.0.0.1',
			user_agent='test-agent',
			session_key='',
			description='Forecast model decision recorded',
			module='analytics',
			function_name='ARIMAForecastingService.generate_forecast',
			metadata={
				'recommended_model': 'sarimax',
				'recommendation_explanation': 'SARIMAX selected due to lower MAPE.',
				'fallback_used': False,
				'fallback_reason': '',
			},
		)

		self.other_audit = AuditLog.objects.create(
			user=None,
			action='update',
			severity='low',
			ip_address='127.0.0.1',
			user_agent='test-agent',
			session_key='',
			description='Unrelated profile update',
			module='accounts',
			function_name='UserProfileView.update',
			metadata={},
		)

	def test_audit_log_list_forecast_decision_filter(self):
		response = self.client.get(reverse('audits:audit_log_list'), {'forecast_decisions': '1'})

		self.assertEqual(response.status_code, 200)
		logs = list(response.context['audit_logs'])
		self.assertEqual(len(logs), 1)
		self.assertEqual(logs[0].id, self.forecast_audit.id)

	def test_audit_logs_api_forecast_decision_filter(self):
		response = self.client.get(reverse('audits:api_audit_logs'), {'forecast_decisions': '1'})

		self.assertEqual(response.status_code, 200)
		payload = response.json()
		self.assertEqual(len(payload['audit_logs']), 1)
		self.assertEqual(payload['audit_logs'][0]['recommended_model'], 'sarimax')
		self.assertFalse(payload['audit_logs'][0]['fallback_used'])

	def test_model_decisions_api_returns_operational_fields(self):
		response = self.client.get(reverse('audits:api_model_decisions'))

		self.assertEqual(response.status_code, 200)
		payload = response.json()
		self.assertEqual(len(payload['model_decision_audits']), 1)
		decision = payload['model_decision_audits'][0]
		self.assertEqual(decision['recommended_model'], 'sarimax')
		self.assertIn('lower MAPE', decision['recommendation_explanation'])
