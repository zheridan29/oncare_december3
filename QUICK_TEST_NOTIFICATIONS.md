# Quick Start: Verify Notification System Works

## Prerequisites
- Django server running on http://127.0.0.1:8000
- Two user accounts: Sales Rep and Pharmacist/Admin
- Both dashboards can have multiple tabs/windows open simultaneously

## 5-Minute Quick Test

### Setup (1 minute)
1. Open **Browser Tab 1** - Pharmacist Dashboard
   - Login as Pharmacist/Admin user
   - Navigate to http://127.0.0.1:8000/inventory/
   - Open DevTools: Press F12
   - Go to Console tab
   - Verify console shows:
     ```
     Real-time notifications system initialized
     Notification widget found: true
     Starting notification polling every 10000 ms
     ```

2. Open **Browser Tab 2** - Sales Rep Order Creation
   - Login as Sales Rep user  
   - Navigate to http://127.0.0.1:8000/orders/
   - Ready to create order

### Test (2-3 minutes)

**Step 1**: Create Order (in Tab 2 - Sales Rep)
1. Click "New Order" button
2. Select a medicine from dropdown
3. Enter quantity (e.g., 10)
4. Scroll down and click "Create Order"
5. You should see success message

**Step 2**: Check Notification (in Tab 1 - Pharmacist)
1. Watch the Notification Widget area (below statistics cards)
2. Within 10 seconds, you should see:
   - "New Order: ORD-XXXXX" notification appearing
   - Red badge showing unread count
   - Message showing order details
   - "High" priority orange badge

**Expected Console Output** (Tab 1):
```
Real-time notifications system initialized
Notification widget found: true
Starting notification polling every 10000 ms

Fetching initial/full notifications
Notification API Response Status: 200
Notifications API Response: {
  notifications: [],
  unread_count: 0,
  ...
}

[After ~10 seconds, when order is created in Tab 2]

Fetching incremental notifications since: ...
Notification API Response Status: 200
Notifications API Response: {
  notifications: [{
    id: 123,
    title: "New Order: ORD-20241215-001",
    message: "New order from Sales Rep ...",
    notification_type: "order_update",
    priority: "high",
    is_read: false,
    ...
  }],
  unread_count: 1,
  ...
}
```

### Verification (1-2 minutes)

**UI Check**:
- [ ] Notification widget is visible
- [ ] Notification has title "New Order: ORD-..."
- [ ] Notification has message with order details
- [ ] "High" priority badge is orange
- [ ] Unread count badge shows "1"

**Interaction Check**:
1. Click the arrow button on the notification
   - [ ] Should navigate to order detail page
2. Go back to inventory dashboard
3. Click "Clear All" button
   - [ ] All notifications should disappear
   - [ ] Console should show: "Notification marked as read"

**Re-appearance Check**:
1. Press F5 to reload page
2. Verify notification does NOT appear again (because marked as read)

## Expected Results Summary

| What | Expected | Status |
|------|----------|--------|
| Notification widget visible on load | Yes (even when empty) | ✓ |
| Console shows polling started | Yes | ✓ |
| Notification appears after order creation | Yes (within 10 sec) | ✓ |
| Notification includes order details | Yes | ✓ |
| Action button navigates to order | Yes | ✓ |
| Clear All marks as read | Yes | ✓ |
| Notification disappears after read | Yes | ✓ |

## If It Doesn't Work

### Symptom 1: Notification Widget Not Visible
**Solution**:
1. Check DevTools Inspector: Right-click → Inspect
2. Search for `notifications-widget` element
3. If NOT found: Template not including widget
   - Run: `grep -r "notifications_widget" templates/`
   - Should find includes in inventory/dashboard.html

### Symptom 2: Console Shows "Notification widget found: false"
**Solution**:
1. In DevTools Console, run:
   ```javascript
   document.getElementById('notifications-widget')
   ```
2. If returns `null`, widget element missing
3. Check HTML structure in page source (Ctrl+U)

### Symptom 3: Polling Shows But Notifications Don't Appear
**Solution**:
1. Create order and immediately check database:
   ```bash
   python manage.py shell
   from common.models import Notification
   print(Notification.objects.count())  # Should be > 0
   ```
2. If no notifications created:
   - Check `orders/views.py` line 323 has `NotificationService.notify_order_placed()`
   - Check order actually saved to database

### Symptom 4: API Returns 404 or 403
**Solution**:
1. In DevTools Console, check:
   ```javascript
   fetch('/common/api/notifications/')
     .then(r => console.log(r.status))
   ```
2. Status 404: URL not found in `common/urls.py`
3. Status 403: User not authenticated or permission denied

### Symptom 5: Notification Appears But Then Disappears
**Solution**:
- This is **normal if the order status is "delivered" and paid**
- Check `common/views.py` line 256-273 for exclusion logic
- Non-completed orders should stay

## Advanced Verification

### Check All 3 Pharmacist Dashboards
The notification system works on all three dashboards:
1. **Inventory Dashboard**: `/inventory/`
2. **Sales Rep Dashboard**: `/orders/` (if pharmacist has access)
3. **Order Fulfillment Dashboard**: `/orders/pharmacist/dashboard/`

**Test**: Create order, then check each URL in separate tabs
- [ ] Notification appears on all 3 dashboards
- [ ] Same notification across all pages
- [ ] Clearing on one clears on all (after refresh)

### Check Database Directly
```bash
python manage.py shell

# 1. Verify notifications were created
from common.models import Notification
from django.contrib.auth.models import User

pharmacist = User.objects.get(username='pharmacist_username')
notifs = Notification.objects.filter(user=pharmacist).order_by('-created_at')[:5]
print(f"Total notifications for pharmacist: {notifs.count()}")

# 2. Check notification details
for n in notifs:
    print(f"\nID: {n.id}")
    print(f"Title: {n.title}")
    print(f"Is Read: {n.is_read}")
    print(f"Priority: {n.priority}")
    print(f"Created: {n.created_at}")

# 3. Verify order placement triggered notifications
from orders.models import Order
latest_order = Order.objects.latest('created_at')
print(f"\nLatest order: {latest_order.order_number}")
print(f"Status: {latest_order.status}")

# Exit
exit()
```

### Check API Endpoint Response
```bash
# Terminal test (you must be authenticated)
curl -b "sessionid=YOUR_SESSION_ID" \
  "http://127.0.0.1:8000/common/api/notifications/?unread_only=true"

# Or in browser Console after logging in:
fetch('/common/api/notifications/?unread_only=true')
  .then(r => r.json())
  .then(d => {
    console.log('Notifications:', d.notifications);
    console.log('Unread count:', d.unread_count);
  })
```

## Files to Review

If you need to debug further, these are the key files:

1. **Notification Creation**:
   - `orders/views.py` line 323 (OrderCreateView.form_valid)
   - `common/services.py` line 58 (notify_order_placed)

2. **API Endpoint**:
   - `common/views.py` line 220 (NotificationAPIView.get)
   - `common/urls.py` (notification endpoint routing)

3. **Real-time JavaScript**:
   - `static/js/realtime_notifications.js` (polling logic)

4. **UI Templates**:
   - `templates/common/notifications_widget.html` (widget HTML)
   - `templates/inventory/dashboard.html` (inventory dashboard)
   - `templates/orders/pharmacist_dashboard.html` (pharmacist dashboard)

5. **View Context**:
   - `inventory/views.py` line 52 (InventoryDashboardView)
   - `orders/views.py` line 49 (OrderDashboardView)
   - `orders/views.py` line 1034 (OrderFulfillmentDashboardView)

## Success Indicators

✅ **System is working if all of these are true:**
1. Notification widget always visible on dashboard load
2. Console shows "Real-time notifications system initialized"
3. Notification appears within 10 seconds of order creation
4. Notification includes: title with order number, message, priority badge
5. Clicking action button navigates somewhere (order detail or list)
6. "Clear All" button successfully hides notifications
7. No JavaScript errors in DevTools Console
