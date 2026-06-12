# Functional Requirements
## OnCare Medicine Ordering System

**Description**: The OnCare Medicine Ordering System provides comprehensive pharmaceutical supply chain management functionality including user authentication with role-based access control (Sales Representative, Pharmacist/Admin, System Administrator), complete medicine catalog and inventory management with real-time stock tracking and reorder alerts, shopping cart and order management with payment processing and verification workflows, prescription upload and verification, ARIMA-based demand forecasting with 6-step analytical process, real-time notifications, and role-specific dashboards for order fulfillment, inventory monitoring, and system administration.

---

The system will be designed to fulfill the following major functions:

1. **Administering the system** - System administration, user management, system monitoring, audit logging, and configuration management
2. **Authorizing user access** - User authentication, registration, login, password management, and role-based access control
3. **Managing medicine catalog** - Medicine information management, category management, manufacturer management, and medicine search
4. **Managing inventory** - Stock tracking, stock movements, reorder alerts, inventory dashboard, and stock status management
5. **Managing shopping cart** - Add, update, remove cart items, calculate totals, validate stock availability, and display real-time cart count
6. **Processing orders** - Order creation, viewing, status management, editing, cancellation, and order history tracking
7. **Processing payments** - Payment submission, payment verification, payment rejection, payment status management, and payment history
8. **Managing prescriptions** - Prescription upload, prescription verification, prescription validation, and prescription file management
9. **Generating notifications** - Real-time notification generation, notification routing, notification display, and notification tracking
10. **Providing dashboards** - Sales representative dashboard, pharmacist/admin dashboard, system administrator dashboard, and analytics dashboard
11. **Forecasting demand** - ARIMA-based demand forecasting, model evaluation, forecast visualization, and inventory optimization
12. **Generating reports** - Order reports, sales reports, inventory reports, payment reports, and data export
13. **Managing files** - Secure file upload, file access control, file validation, and file storage
14. **Searching and filtering** - Medicine search, order search, filtering capabilities, and sorting options
15. **Integrating systems** - Database integration, caching integration, and external service integration

---

## 1. Administering the System

### 1.1 User Management
**FR-1.1.1**: The system shall allow System Administrators to create, view, edit, and deactivate user accounts.

**FR-1.1.2**: The system shall allow System Administrators to assign and modify user roles.

**FR-1.1.3**: The system shall maintain user activity logs for administrative oversight.

### 1.2 System Monitoring
**FR-1.2.1**: The system shall provide System Administrators with system health monitoring including:
- Server performance metrics
- Database performance
- Application error logs
- Security incident tracking

**FR-1.2.2**: The system shall generate alerts for critical system issues requiring administrator attention.

### 1.3 Audit Logging
**FR-1.3.1**: The system shall maintain comprehensive audit logs for all critical operations including:
- User authentication events (login, logout)
- Order creation and modifications
- Payment processing
- Inventory changes
- Prescription handling
- System configuration changes

**FR-1.3.2**: The system shall allow System Administrators to view and search audit logs with filtering capabilities.

**FR-1.3.3**: The system shall maintain audit logs for compliance and security purposes with appropriate retention periods.

---

## 2. Authorizing User Access

### 2.1 User Registration and Login
**FR-2.1.1**: The system shall provide user registration functionality allowing new users to create accounts with email address, username, password, and role selection (Sales Representative, Pharmacist/Admin, System Administrator).

**FR-2.1.2**: The system shall implement secure login functionality using Django's authentication system, requiring valid username/email and password credentials.

**FR-2.1.3**: The system shall enforce password strength requirements (minimum 8 characters with uppercase, lowercase, numbers, and special characters) during registration and password changes.

**FR-2.1.4**: The system shall provide password reset functionality allowing users to reset forgotten passwords through email verification.

**FR-2.1.5**: The system shall implement session management with automatic logout after 30 minutes of inactivity for security purposes.

### 2.2 Role-Based Access Control
**FR-2.2.1**: The system shall implement role-based access control (RBAC) with three distinct user roles: Sales Representative, Pharmacist/Admin, and System Administrator.

**FR-2.2.2**: The system shall restrict access to features and data based on user roles:
- **Sales Representatives**: Access to order management, cart, prescription upload, and personal dashboard
- **Pharmacist/Admin**: Access to inventory management, order fulfillment, payment verification, analytics, and all sales rep features
- **System Administrator**: Full system access including user management, system monitoring, and administrative functions

**FR-2.2.3**: The system shall redirect users to role-specific dashboards upon successful login based on their assigned role.

**FR-2.2.4**: The system shall prevent unauthorized access to restricted pages and display appropriate error messages when access is denied.

### 2.3 User Profile Management
**FR-2.3.1**: The system shall allow authenticated users to view and update their profile information including name, email, contact details, and preferences.

**FR-2.3.2**: The system shall maintain user profile history and track profile changes for audit purposes.

---

## 3. Managing Medicine Catalog

### 3.1 Medicine Information Management
**FR-3.1.1**: The system shall allow Pharmacist/Admin users to create new medicine entries with comprehensive information including:
- Medicine name, generic name, and brand name
- Category and manufacturer
- Description and dosage information
- Unit price and units per box
- Stock quantity and reorder point
- NDC (National Drug Code) number
- FDA approval date and expiry date
- Prescription requirement flag

**FR-3.1.2**: The system shall allow Pharmacist/Admin users to edit existing medicine information, maintaining an audit trail of all changes.

**FR-3.1.3**: The system shall allow Pharmacist/Admin users to delete medicines from the catalog, with appropriate validation to prevent deletion of medicines with existing orders.

**FR-3.1.4**: The system shall display medicine details including stock status (In Stock, Low Stock, Out of Stock) based on current inventory levels.

**FR-3.1.5**: The system shall support medicine search and filtering by name, category, manufacturer, stock status, and prescription requirement.

### 3.2 Category Management
**FR-3.2.1**: The system shall allow Pharmacist/Admin users to create, view, edit, and delete medicine categories.

**FR-3.2.2**: The system shall organize medicines into categories for better catalog management and user navigation.

**FR-3.2.3**: The system shall prevent deletion of categories that have associated medicines.

### 3.3 Manufacturer Management
**FR-3.3.1**: The system shall allow Pharmacist/Admin users to create, view, edit, and delete manufacturer information.

**FR-3.3.2**: The system shall link medicines to their respective manufacturers for tracking and reporting purposes.

**FR-3.3.3**: The system shall prevent deletion of manufacturers that have associated medicines.

---

## 4. Managing Inventory

### 4.1 Stock Management
**FR-4.1.1**: The system shall track real-time inventory levels for all medicines in the catalog.

**FR-4.1.2**: The system shall automatically update stock quantities when orders are created, fulfilled, or cancelled.

**FR-4.1.3**: The system shall allow Pharmacist/Admin users to manually adjust stock levels through stock movement records.

**FR-4.1.4**: The system shall maintain a complete audit trail of all stock movements including:
- Movement type (in, out, adjustment, return, damage, expired)
- Quantity changes
- Reference to purchase orders or invoices
- User who performed the movement
- Timestamp of the movement

**FR-4.1.5**: The system shall calculate and display stock status automatically:
- **In Stock**: Current stock > reorder point
- **Low Stock**: Current stock ≤ reorder point and > 0
- **Out of Stock**: Current stock = 0

### 4.2 Reorder Alerts
**FR-4.2.1**: The system shall automatically generate reorder alerts when medicine stock levels fall at or below the reorder point.

**FR-4.2.2**: The system shall display reorder alerts in the inventory dashboard for Pharmacist/Admin users.

**FR-4.2.3**: The system shall allow Pharmacist/Admin users to view detailed reorder alert information including medicine name, current stock, reorder point, and recommended order quantity.

### 4.3 Inventory Dashboard
**FR-4.3.1**: The system shall provide Pharmacist/Admin users with an inventory dashboard displaying:
- Total medicines in catalog
- Low stock medicines count
- Out of stock medicines count
- Recent stock movements
- Reorder alerts summary

**FR-4.3.2**: The system shall provide real-time updates to inventory statistics on the dashboard.

---

## 5. Managing Shopping Cart

### 5.1 Cart Operations
**FR-5.1.1**: The system shall allow Sales Representatives to add medicines to a shopping cart with specified quantities (in boxes or units).

**FR-5.1.2**: The system shall calculate cart totals automatically, considering units per box when quantity is specified in boxes.

**FR-5.1.3**: The system shall allow Sales Representatives to view their cart contents including medicine details, quantities, unit prices, and total prices.

**FR-5.1.4**: The system shall allow Sales Representatives to update quantities of items in the cart.

**FR-5.1.5**: The system shall allow Sales Representatives to remove individual items from the cart.

**FR-5.1.6**: The system shall allow Sales Representatives to clear the entire cart.

**FR-5.1.7**: The system shall display real-time cart count badges in the navigation bar, updating automatically when items are added or removed.

**FR-5.1.8**: The system shall validate stock availability when adding items to cart and prevent adding items that exceed available stock.

---

## 6. Processing Orders

### 6.1 Order Creation
**FR-6.1.1**: The system shall allow Sales Representatives to create orders from cart items, converting cart items to order items.

**FR-6.1.2**: The system shall require Sales Representatives to provide customer information when creating orders, including:
- Customer name
- Contact information
- Delivery address
- Special instructions (optional)

**FR-6.1.3**: The system shall allow Sales Representatives to create orders with up to 5 different medicines per order.

**FR-6.1.4**: The system shall automatically calculate order totals including:
- Individual item totals (quantity × units_per_box × unit_price for boxes)
- Subtotal
- Tax (if applicable)
- Total amount

**FR-6.1.5**: The system shall validate stock availability before order creation and prevent orders that exceed available inventory.

**FR-6.1.6**: The system shall assign a unique order number to each order for tracking purposes.

**FR-6.1.7**: The system shall set initial order status as "Pending" upon creation.

**FR-6.1.8**: The system shall set initial payment status as "Pending" during order creation and prevent selection of "Paid" status at order creation.

### 6.2 Order Viewing and Listing
**FR-6.2.1**: The system shall allow Sales Representatives to view a list of their own orders with filtering and sorting capabilities.

**FR-6.2.2**: The system shall allow Pharmacist/Admin users to view all orders in the system with filtering by status, payment status, date range, and sales representative.

**FR-6.2.3**: The system shall display order details including:
- Order number and creation date
- Customer information
- Order items with quantities and prices
- Order status and payment status
- Total amount
- Status history timeline

**FR-6.2.4**: The system shall provide different order detail views for Sales Representatives and Pharmacist/Admin users, with role-appropriate information and actions.

### 6.3 Order Status Management
**FR-6.3.1**: The system shall support order statuses: Pending, Processing, Ready for Pickup, Delivered, and Cancelled.

**FR-6.3.2**: The system shall allow Pharmacist/Admin users to update order status through the order fulfillment interface.

**FR-6.3.3**: The system shall enforce business rules for status transitions:
- "Delivered" status can only be set when payment status is "Paid"
- Order status updates shall be logged in OrderStatusHistory

**FR-6.3.4**: The system shall maintain a complete status history timeline for each order, showing all status changes with timestamps and user information.

**FR-6.3.5**: The system shall display status history in chronological order with the latest updates at the top.

**FR-6.3.6**: The system shall allow Sales Representatives to view order status and track order progress in real-time.

### 6.4 Order Editing and Cancellation
**FR-6.4.1**: The system shall allow Sales Representatives to edit orders that are in "Pending" status.

**FR-6.4.2**: The system shall prevent editing of orders that have progressed beyond "Pending" status.

**FR-6.4.3**: The system shall allow Sales Representatives to cancel orders, with appropriate status updates and inventory restoration.

**FR-6.4.4**: The system shall log all order edits and cancellations in the order status history.

---

## 7. Processing Payments

### 7.1 Payment Submission
**FR-7.1.1**: The system shall allow Sales Representatives to submit manual payment information for orders, including:
- Payment method selection
- Payment amount
- Payment receipt upload (image or PDF file)
- Payment reference number (optional)
- Payment date

**FR-7.1.2**: The system shall restrict Sales Representatives to only one pending payment submission per order at a time.

**FR-7.1.3**: The system shall prevent new payment submissions when a pending submission exists for an order.

**FR-7.1.4**: The system shall store payment submission files securely with proper access controls.

**FR-7.1.5**: The system shall create PaymentSubmission records with status "Pending" upon submission.

### 7.2 Payment Verification
**FR-7.2.1**: The system shall allow Pharmacist/Admin users to view pending payment submissions in the order detail page.

**FR-7.2.2**: The system shall allow Pharmacist/Admin users to verify payment submissions, updating:
- PaymentSubmission status to "Verified"
- Order payment status to "Paid"
- Creating OrderStatusHistory entry for payment verification

**FR-7.2.3**: The system shall allow Pharmacist/Admin users to reject payment submissions with:
- Rejection reason
- Updating PaymentSubmission status to "Rejected"
- Allowing Sales Representatives to resubmit payment

**FR-7.2.4**: The system shall maintain complete history of all payment submissions, including rejected submissions, for audit purposes.

**FR-7.2.5**: The system shall display payment verification actions only when pending payment submissions exist.

**FR-7.2.6**: The system shall update order payment status automatically upon payment verification.

### 7.3 Payment Status Management
**FR-7.3.1**: The system shall support payment statuses: Pending, Paid, and Rejected.

**FR-7.3.2**: The system shall display payment status prominently in order details for both Sales Representatives and Pharmacist/Admin users.

**FR-7.3.3**: The system shall link payment status to order status, enforcing that "Delivered" order status requires "Paid" payment status.

---

## 8. Managing Prescriptions

### 8.1 Prescription Upload
**FR-8.1.1**: The system shall allow Sales Representatives to upload prescription documents (images or PDF files) when creating orders for prescription-required medicines.

**FR-8.1.2**: The system shall validate that prescription uploads are required for medicines marked as prescription-required.

**FR-8.1.3**: The system shall store prescription files securely with proper access controls and encryption.

**FR-8.1.4**: The system shall associate prescription files with specific orders and order items.

**FR-8.1.5**: The system shall support multiple file formats for prescriptions (JPG, PNG, PDF).

### 8.2 Prescription Verification
**FR-8.2.1**: The system shall allow Pharmacist/Admin users to view uploaded prescription documents in the order detail page.

**FR-8.2.2**: The system shall allow Pharmacist/Admin users to verify prescription authenticity and validity.

**FR-8.2.3**: The system shall track prescription verification status and maintain audit trails.

**FR-8.2.4**: The system shall prevent order fulfillment for prescription-required medicines until prescription is verified.

---

## 9. Generating Notifications

### 9.1 Real-time Notifications
**FR-9.1.1**: The system shall generate notifications for critical events including:
- New order creation (for Pharmacist/Admin)
- Payment submission (for Pharmacist/Admin)
- Payment verification (for Sales Representatives)
- Payment rejection (for Sales Representatives)
- Order status updates (for Sales Representatives)
- Low stock alerts (for Pharmacist/Admin)

**FR-9.1.2**: The system shall display notifications in a real-time notification widget that updates without page refresh.

**FR-9.1.3**: The system shall route notifications to appropriate users based on their roles and the events they should be aware of.

**FR-9.1.4**: The system shall provide action buttons in notifications that redirect users to relevant pages:
- Sales Representative notifications: Link to order detail page
- Pharmacist/Admin notifications: Link to payment verification page

**FR-9.1.5**: The system shall track notification read/unread status and display unread notification counts.

**FR-9.1.6**: The system shall allow users to mark notifications as read.

**FR-9.1.7**: The system shall filter and display only relevant notifications based on user roles.

---

## 10. Providing Dashboards

### 10.1 Sales Representative Dashboard
**FR-10.1.1**: The system shall provide Sales Representatives with a personalized dashboard displaying:
- Total orders count
- Pending orders count
- Processing orders count
- Ready for Pickup orders count
- Recent orders list (last 5 orders)
- Cart summary
- Recent notifications

**FR-10.1.2**: The system shall update dashboard statistics in real-time.

**FR-10.1.3**: The system shall provide quick access to common actions from the dashboard (create order, view cart, view orders).

### 10.2 Pharmacist/Admin Dashboard
**FR-10.2.1**: The system shall provide Pharmacist/Admin users with an order fulfillment dashboard displaying:
- All orders with filtering capabilities
- Order status summary
- Payment verification queue
- Recent order activities

**FR-10.2.2**: The system shall provide inventory dashboard with:
- Total medicines count
- Low stock medicines
- Out of stock medicines
- Recent stock movements
- Reorder alerts

**FR-10.2.3**: The system shall provide analytics dashboard access for demand forecasting and inventory optimization.

### 10.3 System Administrator Dashboard
**FR-10.3.1**: The system shall provide System Administrators with a comprehensive admin dashboard displaying:
- System health metrics
- User activity statistics
- System performance indicators
- Security alerts
- Maintenance schedules

---

## 11. Forecasting Demand

### 11.1 Demand Forecasting
**FR-11.1.1**: The system shall allow Pharmacist/Admin users to generate demand forecasts for individual medicines using ARIMA (AutoRegressive Integrated Moving Average) models.

**FR-11.1.2**: The system shall implement a 6-step ARIMA forecasting process:
1. **Stationarity Testing**: Test time series data for stationarity
2. **Seasonal Decomposition**: Decompose time series into trend, seasonal, and residual components
3. **Auto ARIMA Model Selection**: Automatically select optimal ARIMA parameters
4. **Model Training**: Train the selected ARIMA model on historical data
5. **Forecast Generation**: Generate future demand predictions
6. **Model Evaluation**: Calculate and display accuracy metrics (AIC, BIC, RMSE, MAE, MAPE)

**FR-11.1.3**: The system shall validate that sufficient historical data exists before generating forecasts (minimum data points required).

**FR-11.1.4**: The system shall display forecast results with confidence intervals and visualization charts.

**FR-11.1.5**: The system shall allow users to export forecast data for external analysis.

### 11.2 Analytics Dashboard
**FR-11.2.1**: The system shall provide an analytics dashboard with interactive charts using Chart.js for:
- Historical sales trends
- Forecast vs actual comparisons
- Seasonal patterns
- Model performance metrics

**FR-11.2.2**: The system shall display ARIMA step-by-step analysis including:
- Stationarity test results
- Seasonal decomposition charts
- Model selection parameters
- Training results
- Forecast visualizations
- Evaluation metrics

**FR-11.2.3**: The system shall provide demand prediction views showing forecasted quantities for specified time periods (daily, weekly, monthly).

### 11.3 Inventory Optimization
**FR-11.3.1**: The system shall calculate Economic Order Quantity (EOQ) based on forecasted demand and cost parameters.

**FR-11.3.2**: The system shall calculate optimal reorder points based on forecasted demand, lead time, and service level requirements.

**FR-11.3.3**: The system shall provide cost analysis including holding costs and stockout costs for inventory optimization decisions.

---

## 12. Generating Reports

### 12.1 Report Generation
**FR-12.1.1**: The system shall allow authorized users to generate reports for:
- Order summaries
- Sales statistics
- Inventory reports
- Payment transactions
- Forecast results

**FR-12.1.2**: The system shall support export of data in common formats (CSV, PDF, Excel) for external analysis.

**FR-12.1.3**: The system shall allow filtering and date range selection for report generation.

---

## 13. Managing Files

### 13.1 File Upload
**FR-13.1.1**: The system shall support secure file uploads for:
- Prescription documents
- Payment receipts
- Other order-related documents

**FR-13.1.2**: The system shall validate file types and sizes before accepting uploads.

**FR-13.1.3**: The system shall store uploaded files securely with proper access controls.

### 13.2 File Access
**FR-13.2.1**: The system shall restrict file access based on user roles and order associations.

**FR-13.2.2**: The system shall allow authorized users to view and download files associated with their orders.

---

## 14. Searching and Filtering

### 14.1 Medicine Search
**FR-14.1.1**: The system shall provide search functionality for medicines by name, generic name, category, or manufacturer.

**FR-14.1.2**: The system shall support filtering medicines by stock status, prescription requirement, and price range.

### 14.2 Order Search
**FR-14.2.1**: The system shall allow users to search orders by order number, customer name, date range, status, and payment status.

**FR-14.2.2**: The system shall provide sorting capabilities for order lists by date, status, amount, and customer name.

---

## 15. Integrating Systems

### 15.1 Database Integration
**FR-15.1.1**: The system shall integrate with MariaDB/PostgreSQL database for data persistence.

**FR-15.1.2**: The system shall maintain data consistency across all modules through proper database relationships and constraints.

### 15.2 Caching Integration
**FR-15.2.1**: The system shall integrate with Redis for session storage and data caching to improve performance.

### 15.3 External Services
**FR-15.3.1**: The system shall support integration with external services for:
- Email notifications (future enhancement)
- Payment gateways (future enhancement)
- SMS notifications (future enhancement)

---

*This document defines the functional requirements for the OnCare Medicine Ordering System and shall be reviewed and updated as the system evolves.*
