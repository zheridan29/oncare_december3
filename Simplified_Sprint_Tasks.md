# Simplified Sprint Tasks - OnCare Medicine Ordering System

## Sprint 1: Foundation & User Management
- Set up Django project structure
- Implement user authentication system
- Create role-based access control (Sales Rep, Pharmacist, Admin)
- Design user registration/login pages
- Create basic dashboard templates

## Sprint 2: Inventory Management
- Design Medicine model with categories and manufacturers
- Implement medicine CRUD operations
- Create inventory dashboard for pharmacists
- Develop stock management system with low stock alerts and reorder points
- Create medicine catalog with search and filtering

## Sprint 3: Order Management & Cart
- Implement shopping cart functionality
- Create order creation workflow for sales representatives
- Design Order and OrderItem models
- Implement order listing, detail views, and status tracking
- Create order history with timeline view
- Implement units_per_box calculation for pricing

## Sprint 4: Payment Processing
- Design PaymentSubmission model
- Implement manual payment submission and verification flow
- Create payment verification interface for pharmacists
- Develop payment rejection mechanism with feedback
- Implement FileUpload for payment receipts
- Create payment status tracking in order workflow
- Ensure single pending payment submission per order

## Sprint 5: Prescription Management
- Implement prescription upload and verification workflow
- Design FileUpload model for prescription documents
- Develop prescription validation rules
- Integrate prescription requirement checks in order process

## Sprint 6: Notification System
- Design Notification model and service
- Implement real-time notification widget
- Create notification routing based on user roles
- Develop action URL transformation for different user views
- Implement notification read/unread tracking and filters

## Sprint 7: ARIMA Forecasting & Analytics
- Implement ARIMA model integration with pmdarima
- Create data collection and preprocessing pipeline
- Develop 6-step ARIMA process (Stationarity, Decomposition, Model Selection, Training, Forecasting, Evaluation)
- Design analytics dashboard with Chart.js visualizations
- Implement forecast generation with model evaluation metrics (AIC, BIC, RMSE, MAE, MAPE)
- Create demand prediction views and export functionality

## Sprint 8: Order Status Workflow
- Implement OrderStatusHistory model for complete audit trail
- Create status history timeline display
- Develop status transition rules and validations
- Implement payment status dependencies (e.g., "Delivered" requires "Paid")
- Create order status update forms with conditional field visibility
- Develop status history filtering and display logic

## Sprint 9: Dashboard Enhancement
- Enhance sales representative dashboard with Processing/Ready for Pickup metrics
- Improve pharmacist order fulfillment dashboard
- Create admin system monitoring dashboard
- Implement real-time cart count badge updates
- Develop order statistics and analytics widgets
- Create export functionality for reports

## Sprint 10: Deployment & Infrastructure
- Configure Render deployment with render.yaml
- Create build.sh script with dependency management
- Set up production database (MariaDB/PostgreSQL)
- Implement logging system with proper directory creation
- Configure Gunicorn for WSGI serving
- Set up static file collection and media handling
- Resolve pmdarima build dependencies (numpy, scipy versioning)
- Configure timezone settings (Asia/Singapore)

---

## Simplified Summary (60 tasks → 36 grouped items)

1. **Django Project Setup**: Project structure, authentication, role-based access, login/registration pages, dashboards
2. **Inventory Management**: Medicine model, CRUD operations, inventory dashboard, stock management, low stock alerts, catalog search
3. **Order Management**: Shopping cart, order workflow, Order/OrderItem models, order views and tracking, order history, pricing calculations
4. **Payment Processing**: PaymentSubmission model, payment submission/verification, rejection mechanism, file uploads, status tracking, single submission restriction
5. **Prescription Management**: Prescription upload/verification, FileUpload model, validation rules, order integration
6. **Notifications**: Notification model/service, real-time widget, role-based routing, URL transformation, read/unread tracking
7. **ARIMA Analytics**: ARIMA integration, data pipeline, 6-step process, analytics dashboard, forecast generation, evaluation metrics, export
8. **Order Status**: OrderStatusHistory model, timeline display, status rules/validations, payment dependencies, conditional forms, filtering
9. **Dashboards**: Sales rep dashboard, pharmacist dashboard, admin dashboard, real-time updates, analytics widgets, export
10. **Deployment**: Render configuration, build script, production database, logging, Gunicorn, static files, dependency resolution, timezone

