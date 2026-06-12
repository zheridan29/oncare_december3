# Data Flow Diagram: System Analysis and Documentation Summary

This document analyzes the OnCare Medicine Ordering System in relation to **all** Data Flow Diagram (DFD) documentation in the project. It summarizes what exists, how the DFDs relate to the actual system, and how to use each artifact.

---

## 1. Documentation Inventory

### 1.1 Main DFD Documents

| Document | Purpose | Level 0 | Level 1 | Data Stores | Best for |
|----------|---------|---------|---------|-------------|----------|
| **DATA_FLOW_DIAGRAM.md** | Comprehensive, implementation-oriented DFD | ✅ 1 process, 4 entities | 7 processes | 16 (D1–D16) | Design, implementation, traceability |
| **DFD_ANALYSIS_AND_VP_GUIDE.md** | Analysis of main DFD + Visual Paradigm guide + alternate DFD | Refers to FINAL | 4 processes (verb phrases) | 3 (Order, Inventory, Payment) | Learning VP rules, stakeholder overview |
| **DFD_VISUAL_PARADIGM_ALIGNED.md** | VP-style DFD aligned with food ordering example | ✅ 1 process, 4 entities | 3 processes | 2 (Order, Inventory) | Teaching, high-level VP alignment |
| **DFD_BEST_PRACTICES_GUIDE.md** | Naming, rules, and common mistakes | N/A | Guidelines | Guidelines | Creating or reviewing DFDs |
| **DFD_COMPARISON_FOOD_ORDERING.md** | Food vs medicine ordering comparison | Side-by-side | Side-by-side | Both | Understanding differences |
| **DFD_REWRITTEN_DOCUMENTATION.md** | Rewritten DFDs based on food examples | ✅ | 4 processes | Simplified | Alternative simplified view |
| **DFD_LEVEL1_SUMMARY.md** | Summary of each Level 1 process decomposition | N/A | 7 processes (sub-processes) | Per process | Quick reference for 1.0–7.0 |
| **MERMAID_DIAGRAMS_README.md** | Index of all Mermaid diagram files | — | — | — | Finding and viewing diagrams |

### 1.2 Mermaid Diagram Files

| File | Type | Processes | Data Stores | Notes |
|------|------|-----------|-------------|--------|
| **DFD_LEVEL0_CONTEXT_FINAL.mmd** | Context (Level 0) | 1 (system) | 0 | VP-aligned; 4 entities |
| **DFD_LEVEL0_CONTEXT_REWRITTEN.mmd** | Context | 1 | 0 | Rewritten variant |
| **DFD_CONTEXT_DIAGRAM.mmd** | Context | 1 | 0 | Original context |
| **DFD_LEVEL1_FINAL.mmd** | Level 1 | 3 | 2 | Order Medicine, Generate Reports, Order Inventory |
| **DFD_LEVEL1_VP_4PROCESS.mmd** | Level 1 | 4 | 3 | Adds Verify Payment; VP-compliant |
| **DFD_LEVEL1_REWRITTEN.mmd** | Level 1 | 4 | — | Rewritten variant |
| **DFD_LEVEL1_IMPROVED.mmd** | Level 1 | — | — | Improved version |
| **DATA_FLOW_DIAGRAM.mmd** | Level 1 | 7 | 16 | Full system (same as DATA_FLOW_DIAGRAM.md) |
| **DFD_LEVEL1_PROCESS1_USER_MANAGEMENT.mmd** | Level 2 (Process 1) | 5 sub-processes | D1, D2, D17 | 1.1–1.5 |
| **DFD_LEVEL1_PROCESS2_ORDER_PROCESSING.mmd** | Level 2 (Process 2) | 5 sub-processes | D3–D5, D9 | 2.1–2.5 |
| **DFD_LEVEL1_PROCESS3_PAYMENT_PROCESSING.mmd** | Level 2 (Process 3) | 5 sub-processes | D6–D8 | 3.1–3.5 |
| **DFD_LEVEL1_PROCESS4_INVENTORY_MANAGEMENT.mmd** | Level 2 (Process 4) | 5 sub-processes | D9–D13 | 4.1–4.5 |
| **DFD_LEVEL1_PROCESS5_PRESCRIPTION_MANAGEMENT.mmd** | Level 2 (Process 5) | 4 sub-processes | D4, D8 | 5.1–5.4 |
| **DFD_LEVEL1_PROCESS6_NOTIFICATION_SYSTEM.mmd** | Level 2 (Process 6) | 4 sub-processes | D14 | 6.1–6.4 |
| **DFD_LEVEL1_PROCESS7_ANALYTICS_FORECASTING.mmd** | Level 2 (Process 7) | 4 sub-processes | D15, D16 | 7.1–7.4 |
| **DFD_LEVEL2_PROCESS_ORDERS.mmd** | Level 2 | Order-focused | — | Order process detail |
| **DFD_ORDER_LIFECYCLE.mmd** | Thematic | Order lifecycle | — | Creation → Payment → Fulfillment |
| **DFD_PROCESS_FLOW.mmd** | Process flow | 7 processes | 0 | Process dependencies only |
| **DFD_FOOD_VS_MEDICINE_COMPARISON.mmd** | Comparison | Food vs Medicine | — | Side-by-side |

---

## 2. DFD “Families” and When to Use Them

### Family A: Detailed 7-Process DFD (DATA_FLOW_DIAGRAM.md / DATA_FLOW_DIAGRAM.mmd)

- **Level 0**: One process (OnCare Medicine Ordering System), four external entities, no data stores.
- **Level 1**: Seven processes — 1.0 User Management, 2.0 Order Processing, 3.0 Payment Processing, 4.0 Inventory Management, 5.0 Prescription Management, 6.0 Notification System, 7.0 Analytics & Forecasting.
- **Data stores**: D1–D16 (User, User Session, Cart, Order, Order Status History, Payment Submission, Transaction, File Upload, Medicine, Stock Movement, Reorder Alert, Category, Manufacturer, Notification, Forecast, Analytics).
- **Use when**: You need full traceability to implementation, training on the complete system, or design/refactoring of a specific area. Process names are partly noun phrases (e.g. “User Management”); Visual Paradigm prefers verb phrases.

### Family B: Visual Paradigm 3-Process (DFD_LEVEL0_CONTEXT_FINAL.mmd + DFD_LEVEL1_FINAL.mmd)

- **Level 0**: One process, four entities (Sales Rep, Pharmacist/Admin, System Admin, External Payment Gateway), no data stores.
- **Level 1**: Three processes — 1.0 Order Medicine, 2.0 Generate Reports, 3.0 Order Inventory. Two data stores: Order, Inventory.
- **Use when**: You want a minimal, VP-style diagram that mirrors the [Visual Paradigm Food Ordering example](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp) (teaching, high-level stakeholder view). All process names are verb phrases.

### Family C: Visual Paradigm 4-Process with Payment (DFD_ANALYSIS_AND_VP_GUIDE.md + DFD_LEVEL1_VP_4PROCESS.mmd)

- **Level 0**: Same as Family B (context is shared).
- **Level 1**: Four processes — 1.0 Order Medicine, 2.0 Verify Payment, 3.0 Generate Reports, 4.0 Order Inventory. Three data stores: Order, Inventory, Payment.
- **Use when**: You want a VP-compliant diagram that explicitly shows payment verification and is still simple (stakeholder overview, documentation that highlights payment).

### Family D: Level 2 Decomposition (DFD_LEVEL1_PROCESS* .mmd)

- Each of the seven major processes (1.0–7.0) is decomposed into sub-processes (e.g. 2.1 Manage Shopping Cart, 2.2 Create Order).
- **Use when**: You need detail on a single area (e.g. order processing, payment, inventory) without the full Level 1 diagram.

---

## 3. Mapping DFD to the OnCare System (Django)

The detailed DFD (Family A) maps to the actual Django apps and responsibilities as follows.

| DFD Process | Django App(s) | Main Models / Concerns |
|-------------|---------------|------------------------|
| 1.0 User Management | `accounts` | User, profiles, roles, login/session |
| 2.0 Order Processing | `orders` | Order, OrderItem, Cart, CartItem, OrderStatusHistory |
| 3.0 Payment Processing | `orders`, `transactions` | PaymentSubmission, Transaction, FileUpload (receipts) |
| 4.0 Inventory Management | `inventory` | Medicine, StockMovement, ReorderAlert, Category, Manufacturer |
| 5.0 Prescription Management | `orders`, `common` (FileUpload) | FileUpload (prescriptions), order prescription flags |
| 6.0 Notification System | `common` | Notification, NotificationService |
| 7.0 Analytics & Forecasting | `analytics` | DemandForecast, ARIMA, reports |

| DFD Data Store | Django Model(s) / Storage |
|----------------|---------------------------|
| D1 User | User, profile models (accounts) |
| D2 User Session | Django session framework |
| D3 Cart | Cart, CartItem (orders) |
| D4 Order | Order, OrderItem (orders) |
| D5 Order Status History | OrderStatusHistory (orders) |
| D6 Payment Submission | PaymentSubmission (orders) |
| D7 Transaction | Transaction (transactions) |
| D8 File Upload | FileUpload (common) |
| D9 Medicine | Medicine, MedicineImage (inventory) |
| D10 Stock Movement | StockMovement (inventory) |
| D11 Reorder Alert | ReorderAlert (inventory) |
| D12 Category | Category (inventory) |
| D13 Manufacturer | Manufacturer (inventory) |
| D14 Notification | Notification (common) |
| D15 Forecast | DemandForecast (analytics) |
| D16 Analytics | SalesReport / analytics data (analytics) |

Additional apps (`oncare_admin`, `audits`, `transactions`) support admin dashboards, auditing, and transaction history; they are implied by the DFD’s “System Admin” and “Payment/Transaction” flows.

---

## 4. Key Data Flows (from Documentation)

### 4.1 Order Creation (Sales Rep → System)

1. Browse medicine catalog (read D9).
2. Add to cart → 2.1 Manage Shopping Cart → D3 Cart.
3. Create order → 2.2 Create Order → D4 Order, D5 Order Status History; trigger 6.0 Notification.
4. Submit payment info → 3.1 Submit Payment Information → D6 Payment Submission, D8 File Upload; trigger 6.0 Notification.

### 4.2 Payment Verification (Pharmacist/Admin → System)

1. View payment submission (read D6).
2. Verify payment → 3.2 Verify Payment → update D6, D4 (payment_status), D7 Transaction; notify.
3. Reject payment → 3.3 Reject Payment Submission → update D6; notify.

### 4.3 Inventory and Reports

- Pharmacist/Admin: manage medicine (D9), stock movements (D10), reorder alerts (D11), categories (D12), manufacturers (D13); receive inventory reports and alerts.
- System Admin: request reports → 3.0 Generate Reports (VP) or 7.0 Analytics (detailed) → read Order, Inventory, optionally Payment → Reports.

### 4.4 Context-Level Flows (Level 0)

- **Sales Representative** → Order → System; System → Bill / Order confirmation → Sales Representative.
- **Pharmacist/Admin** ← Order / Order details ← System.
- **System Admin** → Inventory order / user management → System; System → Reports → System Admin.
- **External Payment Gateway** ← Payment / Inventory order ← System (and gateway responses → System).

---

## 5. Visual Paradigm Rules (Summary)

From **DFD_ANALYSIS_AND_VP_GUIDE.md** and **DFD_BEST_PRACTICES_GUIDE.md**:

- **Context diagram**: One process, external entities only, no data stores.
- **Process names**: Verb phrases (e.g. “Order Medicine”, “Verify Payment”), not noun phrases (“Order Processing”).
- **Data store names**: Nouns (e.g. “Order”, “Inventory”, “Payment”).
- **Complexity**: 5–7 processes at Level 1 is manageable; 3–4 is simpler.
- **Rules**: No data store connected to an external entity; no data flow between two external entities; every process has at least one input and one output (no black-hole); data flows represent **data**, not “request” or process flow.

---

## 6. How to Use This Analysis

- **Implementing or debugging a feature**: Use **DATA_FLOW_DIAGRAM.md** and the process/decomposition that matches the feature (e.g. Process 3 for payment). Cross-check with the Django app and models in Section 3.
- **Presenting to stakeholders or teaching DFD**: Use **DFD_LEVEL0_CONTEXT_FINAL.mmd** and either **DFD_LEVEL1_FINAL.mmd** (3-process) or **DFD_LEVEL1_VP_4PROCESS.mmd** (4-process with payment). Use **DFD_VISUAL_PARADIGM_ALIGNED.md** or **DFD_ANALYSIS_AND_VP_GUIDE.md** for the narrative.
- **Creating or reviewing a new DFD**: Use **DFD_BEST_PRACTICES_GUIDE.md** and the VP rules in **DFD_ANALYSIS_AND_VP_GUIDE.md**.
- **Comparing with food ordering or explaining medicine-specific flows**: Use **DFD_COMPARISON_FOOD_ORDERING.md** and **DFD_FOOD_VS_MEDICINE_COMPARISON.mmd**.
- **Finding a diagram file**: Use **MERMAID_DIAGRAMS_README.md**; render `.mmd` files in [Mermaid Live Editor](https://mermaid.live) or a Mermaid-capable viewer.

---

## 7. References

- [Visual Paradigm – Data Flow Diagram: Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)
- [GeeksforGeeks – DFD for Food Ordering System](https://www.geeksforgeeks.org/software-engineering/dfd-for-food-ordering-system/)
- Project files: `DATA_FLOW_DIAGRAM.md`, `DFD_ANALYSIS_AND_VP_GUIDE.md`, `DFD_VISUAL_PARADIGM_ALIGNED.md`, `DFD_BEST_PRACTICES_GUIDE.md`, `DFD_COMPARISON_FOOD_ORDERING.md`, `DFD_REWRITTEN_DOCUMENTATION.md`, `DFD_LEVEL1_SUMMARY.md`, `MERMAID_DIAGRAMS_README.md`, and all `DFD_*.mmd` / `DATA_FLOW_DIAGRAM.mmd` files.

---

*This analysis summarizes all data flow diagram documentation for the OnCare Medicine Ordering System and maps it to the implemented system.*
