# User Acceptance Testing (UAT) Results

## System
**ON‑CARE: A Web-Based Ordering System with Customer-Centric Supply Chain Analytics for Neo Care Philippines**

---

## 1. UAT Overview

User Acceptance Testing (UAT) was conducted in a staging environment using realistic sample data (users, medicines, stock levels, orders, and payment records). Representatives from each target role—Sales Representatives, Pharmacist/Admins, and System Administrators—executed business‑oriented scenarios based on the functional requirements and typical workflows at Neo Care Philippines.

The goal was to confirm that ON‑CARE supports day‑to‑day work: placing and tracking orders, maintaining inventory, handling payments and prescriptions, and using dashboards and notifications to manage operations.

---

## 2. UAT Summary of Results

- **Total UAT scenarios executed**: 10  
- **Status**:  
  - **Passed as expected**: 9  
  - **Passed with minor usability suggestions**: 1  
- **Blocking issues**: None identified.  
- **Overall UAT conclusion**: ON‑CARE is **acceptable for deployment**, meeting the business and usability expectations of the participating users, with only minor UI/wording improvements suggested for future refinement.

---

## 3. Detailed UAT Results

| Test Case | Role(s) | Scenario Description | Result | Notes |
|---|---|---|---|---|
| **UAT‑01: Role-based Login and Dashboard** | Sales Rep, Pharmacist/Admin, System Admin | Log in as each role and observe landing page and available menu items. | **Pass** | All roles were redirected to the correct dashboards; menu options matched role permissions. Users found the role labels and navigation intuitive. |
| **UAT‑02: Browse Medicines and View Details** | Sales Rep | Browse medicine catalog, search by name/category, open a medicine detail page. | **Pass** | Search and filtering behaved as expected. Medicine detail pages clearly showed price, units per box, stock status, and prescription requirement. |
| **UAT‑03: Create Order from Cart** | Sales Rep | Add medicines (including boxes) to cart, review cart, and create an order with full customer information. | **Pass** | Cart totals, including units‑per‑box pricing, were correct. Order was created with status “Pending” and payment status “Pending”, and appeared in “My Orders”. |
| **UAT‑04: Track Order and See Status History** | Sales Rep & Pharmacist/Admin | Place an order, then have Pharmacist/Admin update its status through fulfillment; view history as Sales Rep. | **Pass** | Status transitions (Pending → Processing → Ready for Pickup → Delivered) were reflected correctly. Sales Rep saw a clear status history timeline with timestamps and actors. |
| **UAT‑05: Manual Payment Submission and Verification** | Sales Rep & Pharmacist/Admin | Sales Rep submits payment info with receipt; Pharmacist/Admin verifies or rejects it, then Sales Rep views result. | **Pass** | Only one pending submission was allowed per order. Verification updated payment status to “Paid”; rejection stored a reason and unlocked resubmission. Both roles saw up‑to‑date payment status. |
| **UAT‑06: Prescription Upload and Verification** | Sales Rep & Pharmacist/Admin | Create an order for a prescription-required medicine; upload prescription; Pharmacist verifies and fulfills the order. | **Pass** | System enforced prescription upload for flagged medicines. Prescriptions were viewable to Pharmacist/Admin; orders could not be fulfilled until verification was completed. |
| **UAT‑07: Inventory Monitoring and Reorder Alerts** | Pharmacist/Admin | View inventory dashboard, identify low-stock medicines, and inspect reorder alerts. | **Pass** | Low‑stock and out‑of‑stock medicines were highlighted correctly. Reorder alerts showed medicine name, current stock, and reorder point, helping Pharmacist/Admin plan restocking. |
| **UAT‑08: Notifications and Quick Navigation** | Sales Rep & Pharmacist/Admin | Trigger events (new order, payment, low stock) and review notifications and their action buttons. | **Pass (minor UX suggestions)** | Notifications appeared in the widget with correct unread counts and roles. Action buttons linked to the correct order/payment views. Users suggested slightly clearer wording for some notification messages, but this did not block acceptance. |
| **UAT‑09: Admin User and Audit Oversight** | System Admin | Create a new user, change a role, and view related activity/audit entries. | **Pass** | Newly created users could log in with the assigned role. Activity and audit logs showed user actions (login, order creation, etc.) and were filterable for review. |
| **UAT‑10: Basic Analytics and Reports** | Pharmacist/Admin & System Admin | Open analytics dashboard and generate an order or inventory report for a given date range. | **Pass** | Analytics charts rendered correctly with sample data. Generated reports (orders/inventory) matched expectations for the test dataset and exported successfully to CSV/PDF/Excel. |

---

## 4. UAT Conclusion and Recommendations

Based on the UAT sessions:

- **Business workflows are supported end‑to‑end**:  
  - Sales Representatives can comfortably browse medicines, manage carts, submit orders, provide payments, and track status.  
  - Pharmacist/Admins can verify payments, handle prescriptions, manage inventory, and see the operational picture via dashboards.  
  - System Administrators can manage users, monitor health and activity, and generate reports.

- **No critical defects or blockers** were found during UAT.  
- **Minor improvements** suggested by users (mainly around wording/labels and additional tooltips for some dashboard cards and notifications) can be scheduled as post‑launch UI enhancements without affecting overall acceptance.

**Overall**, the UAT outcome supports that ON‑CARE is ready to be accepted by stakeholders and deployed for real‑world use at Neo Care Philippines, with the system behaving in line with the documented functional requirements and user expectations.

