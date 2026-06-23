import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicine_ordering_system.settings')
import django

django.setup()

from django.contrib.auth import get_user_model
from django.test import Client
from django.db.models import Q

User = get_user_model()
users = User.objects.filter(Q(role='pharmacist_admin') | Q(role='admin'), is_active=True)[:5]
print('count', users.count())
for u in users:
    print('user', u.pk, u.username, u.email, u.role, u.is_staff, u.is_superuser)

if not users:
    print('No eligible user found')
else:
    client = Client()
    client.force_login(users[0])
    response = client.get('/orders/api/pharmacist/dashboard/')
    print('status', response.status_code)
    print(response.content.decode('utf-8'))
