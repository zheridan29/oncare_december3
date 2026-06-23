# Notification System Testing Guide

## Overview
This guide helps verify that the notification system is working correctly for both Sales Representatives and Pharmacist/Admin users on both dashboard pages.

## System Architecture

### Components
1. **Notification Creation**: `NotificationService.notify_order_placed()` - Called when order is created in `OrderCreateView.form_valid()`
2. **Notification Storage**: `Notification` model in `common/models.py`
3. **Notification API**: `/common/api/notifications/` - Returns unread notifications for current user
4. **Real-time Updates**: `realtime_notifications.js` - Polls API every 10 seconds
5. **UI Widget**: `notifications_widget.html` - Displays notifications on dashboards

### Dashboards Displaying Notifications
1. **Sales Rep Dashboard**: `/orders/` (Orders Dashboard)
2. **Pharmacist Dashboard**: `/inventory/` (Inventory Dashboard)
3. **Pharmacist Dashboard**: `/orders/pharmacist/dashboard/` (Order Fulfillment Dashboard)

## Testing Procedure

### Step 1: Setup
- Ensure you have 2 user accounts: 
  - **Sales Rep**: `sales_rep_user` with role `is_sales_rep = True`
  - **Pharmacist/Admin**: `pharmacist_user` with role `is_pharmacist_admin = True`

### Step 2: Check Notification Widget Visibility
Open browser DevTools (F12) and go to each dashboard URL:

```
For Sales Rep:
1. Navigate to http://127.0.0.1:8000/orders/
   - Should see Notification Widget below statistics cards
   
For Pharmacist:
2. Navigate to http://127.0.0.1:8000/inventory/
   - Should see Notification Widget below statistics cards
   
3. Navigate to http://127.0.0.1:8000/orders/pharmacist/dashboard/
   - Should see Notification Widget below status chart
```

### Step 3: Enable Console Logging
In browser DevTools Console, verify real-time system is running:

**Expected Console Output:**
```
Real-time notifications system initialized
Notification widget found: true
Notification count element found: true
Starting notification polling every 10000 ms
Fetching initial/full notifications
Notification API Response Status: 200
Notifications API Response: {
  notifications: [...],
  unread_count: 0,
  latest_check_time: "2024-...",
  latest_notification_time: null
}
```

### Step 4: Test Notification Creation

**Step 4a: Login as Sales Rep**
1. Open browser Developer Tools (F12)
2. Navigate to Orders Dashboard: `/orders/`
3. Click "New Order" button
4. Select medicines and quantities
5. Fill in delivery address
6. Click "Create Order"

**Step 4b: Verify Notification Created in Database**
```bash
# SSH to server or use Django shell
python manage.py shell

from common.models import Notification
from django.contrib.auth.models import User

# Check notifications for pharmacist
pharmacist = User.objects.get(username='pharmacist_user')  # or your pharmacist username
notifications = Notification.objects.filter(user=pharmacist).order_by('-created_at')[:5]

for notif in notifications:
    print(f"ID: {notif.id}")
    print(f"Title: {notif.title}")
    print(f"Message: {notif.message}")
    print(f"Type: {notif.notification_type}")
    print(f"Priority: {notif.priority}")
    print(f"Is Read: {notif.is_read}")
    print(f"Created: {notif.created_at}")
    print("---")
```

### Step 5: Test API Endpoint

**Step 5a: Check Notification API Response**
```bash
# In browser Console:
fetch('/common/api/notifications/?unread_only=true&limit=10')
  .then(r => r.json())
  .then(data => console.log(data))
```

**Expected Response:**
```json
{
  "notifications": [
    {
      "id": 123,
      "title": "New Order: ORD-20241215-001",
      "message": "New order from ...",
      "notification_type": "order_update",
      "priority": "high",
      "is_read": false,
      "created_at": "2024-12-15T10:30:45.123456+00:00",
      "action_url": "/orders/orders/456/",
      "time_ago": "Just now"
    }
  ],
  "unread_count": 1,
  "latest_check_time": "2024-12-15T10:31:02.654321+00:00",
  "latest_notification_time": "2024-12-15T10:30:45.123456+00:00"
}
```

### Step 6: Verify Real-time Display

**Step 6a: Monitor Pharmacist Dashboard During Order Creation**

Open TWO browser windows/tabs:
- **Tab 1**: Logged in as Sales Rep, at `/orders/` page
- **Tab 2**: Logged in as Pharmacist, at `/inventory/` page, DevTools Console open

Watch the Console in Tab 2 as you create an order in Tab 1:

```
Console Output Sequence:
1. "Starting notification polling every 10000 ms"
2. "Fetching initial/full notifications"
3. "Notification API Response Status: 200"
4. "Notifications API Response: { notifications: [], unread_count: 0, ... }"
5. [Wait up to 10 seconds]
6. "Fetching incremental notifications since: ..."
7. "Notification API Response: { notifications: [{...}], unread_count: 1, ... }"
```

**Expected UI Changes in Tab 2 (/inventory/):**
- Notification card should appear below statistics with title "New Order: ORD-..."
- Red badge should show "1" next to "Unread Notifications"
- Notification should have "High" priority badge in orange
- Should have action button linking to order details

### Step 7: Verify on Multiple Dashboards

Repeat Step 6 with Pharmacist logged into different dashboards:
- `/inventory/` (Inventory Dashboard)
- `/orders/pharmacist/dashboard/` (Order Fulfillment Dashboard)
- `/orders/` (if accessible)

**Expected Result**: Same notification appears on all dashboards in real-time

### Step 8: Test Notification Actions

**Step 8a: Click Notification Action Button**
1. In Pharmacist's Inventory Dashboard, look for notification card
2. Click the arrow button on the right
3. Should navigate to order detail page (or correct URL based on notification type)

**Step 8b: Mark as Read**
1. Click "Clear All" button in notification widget header
2. All notifications should disappear
3. In DevTools Console, should see:
```
Notification marked as read
```

### Step 9: Verify Notification Persistence

**Step 9a: Reload Page While Notification Exists**
1. In Pharmacist's Inventory Dashboard
2. Do NOT clear notifications
3. Press F5 to reload page
4. **Expected**: Notification should still be visible (from initial page load context)
5. **Note**: Real-time polling should fetch same notification again

**Step 9b: Open Fresh Browser Tab**
1. Open new tab, navigate to Pharmacist's `/inventory/`
2. **Expected**: Unread notification should appear immediately

## Troubleshooting

### Issue 1: Notification Widget Not Appearing
**Diagnosis:**
- Open DevTools Console
- Should see: "Notification widget found: true"
- If false, check browser Inspector to verify `<div id="notifications-widget">` exists

**Solution:**
- Verify `notifications_widget.html` is included in template:
  ```html
  {% include 'common/notifications_widget.html' %}
  ```
- Check that templates have proper div structure

### Issue 2: Real-time Polling Not Starting
**Diagnosis:**
- Open DevTools Console
- Check for: "Real-time notifications system initialized"
- Check for: "Starting notification polling every 10000 ms"

**Solution:**
- Verify `realtime_notifications.js` is loaded:
  ```html
  <script src="{% static 'js/realtime_notifications.js' %}"></script>
  ```
- Check for JavaScript errors in DevTools

### Issue 3: API Returns 404 or 403
**Diagnosis:**
```javascript
// In DevTools Console:
fetch('/common/api/notifications/')
  .then(r => {
    console.log('Status:', r.status);
    return r.text();
  })
  .then(t => console.log(t))
```

**Solution:**
- Verify URL is correct: `/common/api/notifications/`
- Check `common/urls.py` has proper routing:
  ```python
  path('api/notifications/', views.NotificationAPIView.as_view(), name='api_notifications'),
  ```
- Ensure user is authenticated (check browser cookies/session)

### Issue 4: Notifications Not Created
**Diagnosis:**
```bash
python manage.py shell
from common.models import Notification
print(f"Total notifications: {Notification.objects.count()}")
print(f"Recent: {list(Notification.objects.order_by('-created_at')[:3].values())}")
```

**Solution:**
- Verify `NotificationService.notify_order_placed()` is being called in `OrderCreateView.form_valid()`
- Check `orders/views.py` line 323:
  ```python
  NotificationService.notify_order_placed(self.object)
  ```
- Verify order was created successfully before notification check
- Check Django logs for errors during notification creation

### Issue 5: Notifications Appear for Wrong User
**Diagnosis:**
- Check notification recipient in database:
  ```bash
  python manage.py shell
  from common.models import Notification
  notif = Notification.objects.latest('id')
  print(f"Recipient: {notif.user}")
  print(f"Is Admin/Pharmacist: {notif.user.is_pharmacist_admin or notif.user.is_admin}")
  ```

**Solution:**
- Verify `notify_order_placed()` filters for correct roles:
  ```python
  pharmacist_admins = User.objects.filter(
      Q(role='pharmacist_admin') | Q(role='admin'),
      is_active=True
  )
  ```

## Success Criteria

✅ **All of the following should be true:**

1. When Sales Rep creates order, notification appears immediately on Pharmacist's dashboard
2. Notification widget is always visible on all three dashboards (no empty state hiding)
3. Real-time polling starts automatically when page loads
4. Notification includes: title, message, high priority badge, and action link
5. Notification count appears in widget header and navbar
6. "Clear All" button successfully marks all as read
7. Notification persists across page reloads (until marked as read)
8. Same notification appears on all Pharmacist dashboards simultaneously
9. No JavaScript errors in DevTools Console
10. API returns proper JSON with notification data

## Performance Notes

- **Polling Interval**: 10 seconds for notifications
- **Notification Limit**: Widget shows 10 most recent unread notifications
- **Exclusion**: Completed orders (delivered + paid) are hidden from notifications
- **Optimization**: Polling pauses when browser tab is not visible

## Related Files

- `orders/views.py` (line 323): Notification trigger
- `common/services.py` (line 58): notify_order_placed() implementation
- `common/views.py` (line 220): NotificationAPIView
- `static/js/realtime_notifications.js`: Client-side polling
- `templates/common/notifications_widget.html`: UI widget
- `templates/inventory/dashboard.html`: Inventory dashboard
- `templates/orders/dashboard.html`: Sales rep dashboard
- `templates/orders/pharmacist_dashboard.html`: Pharmacist dashboard
