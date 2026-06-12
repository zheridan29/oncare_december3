# Simple DFDs: Level 0 (Context) and Level 1 (Order, Inventory, Payment)

This document covers the Level 0 context diagram and three separate Level 1 Data Flow Diagrams (Order, Inventory, Payment). Based on **DATA_FLOW_DIAGRAM.md** and **DFD_SYSTEM_ANALYSIS.md**.

---

## 0. Level 0 — Context Diagram (Whole System)

**File**: `DFD_LEVEL0_CONTEXT_FINAL.mmd`

**Descriptive paragraph:** The Level 0 Data Flow Diagram presents the OnCare Medicine Ordering System as a single process in the center, with four external entities around it: Sales Representative, Pharmacist/Admin, System Administrator, and External Payment Gateway. At this level there are no data stores—only the system and the flows of data between it and the outside world. The Sales Representative sends orders into the system and receives a bill or order confirmation back; the Pharmacist/Admin receives order information from the system for fulfillment; the System Administrator sends inventory orders into the system and receives reports; and the External Payment Gateway receives inventory or payment-related orders from the system. This context diagram is essential for establishing the system boundary and showing who interacts with OnCare at a high level: it directly supports Neo Care Philippines’ need to see the full picture—customer-facing ordering (Sales Rep), pharmacy fulfillment (Pharmacist/Admin), back-office and reporting (System Admin), and external payment or supply (Payment Gateway)—before diving into internal processes. The diagram humanizes the system by making it clear that the entire application exists to serve these four actors and their main data exchanges, setting the stage for the more detailed Order, Inventory, and Payment flows at Level 1.

**Simple description (in plain language):** The diagram shows the whole system as one box. Four types of users (or systems) talk to it: Sales Reps place orders and get a bill; Pharmacists/Admins get orders to fulfill; System Admins send inventory orders and get reports; and the External Payment Gateway receives orders or payment requests from the system. Nothing is stored at this level—we only see who sends what to the system and what they get back.

**External entities**: Sales Representative, Pharmacist/Admin, System Admin, External Payment Gateway  

**Data flows** (no data stores at Level 0):
- Sales Representative → Order → System; System → Bill → Sales Representative  
- System → Order → Pharmacist/Admin  
- System Admin → Inventory Order → System; System → Reports → System Admin  
- System → Inventory Order → External Payment Gateway  

---

## 1. Order Data Flow

**File**: `DFD_LEVEL1_ORDER_FLOW.mmd`

**Descriptive paragraph:** The Order Data Flow diagram presents a simplified Level 1 view of how orders move through the OnCare system, with two external actors—Sales Representative and Pharmacist/Admin—interacting with three core processes (Manage Cart, Create Order, and Update Order Status) and three data stores (Cart, Order, and Order Status History). This flow directly supports Neo Care Philippines’ need for a clear path from customer-facing ordering to fulfillment: Sales Representatives capture cart items and customer information, create orders, and receive confirmations, while Pharmacists/Admins receive order details, update status (e.g. confirmed, shipped, delivered), and maintain a full history of changes. The separation of Cart (pre-checkout), Order (confirmed records), and Order Status History (audit trail) ensures that the system can track the full order lifecycle while keeping temporary shopping data distinct from committed orders. This architecture is essential for transforming manual or ad-hoc order handling into a traceable, role-based process that supports accountability, customer communication, and operational reporting for Neo Care Philippines’ pharmaceutical distribution.

**External entities**: Sales Representative, Pharmacist/Admin  

**Processes** (verb phrases):
- 1.0 Manage Cart
- 2.0 Create Order
- 3.0 Update Order Status

**Data stores**: Cart (D1), Order (D2), Order Status History (D3)

**Main flows**:
- Sales Rep → Cart items / Customer info → Manage Cart, Create Order → Cart, Order, Order Status History → Order confirmation to Sales Rep
- Pharmacist → Status update → Update Order Status → Order, Order Status History → Order details to Pharmacist

---

## 2. Inventory Data Flow

**File**: `DFD_LEVEL1_INVENTORY_FLOW.mmd`

**Descriptive paragraph:** The Inventory Data Flow diagram presents a Level 1 view of how medicine catalog and stock data move through the OnCare system, with Pharmacist/Admin and Sales Representative as external actors, three core processes (Manage Medicine Catalog, Track Stock, and Generate Reorder Alerts), and five data stores (Medicine, Stock Movement, Reorder Alert, Category, and Manufacturer). This flow directly supports Neo Care Philippines’ need for accurate, up-to-date inventory: Pharmacists/Admins maintain the catalog, record stock movements, and receive reorder alerts when stock is low, while Sales Representatives only query the catalog to show products and build orders without modifying inventory. The architecture implements a clear separation of responsibilities—inventory control stays with the pharmacy side, and customer-facing staff get read-only access to product information—which is essential for data integrity, compliance, and avoiding overselling. By linking low stock to reorder alerts and reports, the diagram reflects how the system supports supply chain visibility and strategic restocking decisions for Neo Care Philippines’ pharmaceutical distribution.

### Simple description (in plain language)

This diagram shows how **inventory** works in the system.

**Pharmacists and admins** are the ones who maintain the medicine list. They add or edit medicines, set categories and manufacturers, and record when stock goes in or out. The system stores: the medicine catalog, every stock movement, reorder alerts, and the category and manufacturer lists. When stock gets low, the system creates reorder alerts and shows them to the pharmacist so they know what to order. Pharmacists can also run inventory reports and see current stock status.

**Sales representatives** do not change inventory. They only look up the catalog—what medicines exist, their details, categories, and so on—so they can show products to customers and add items to orders. So in short: the pharmacist manages and sees everything; the sales rep only sees the catalog.

**External entities**: Pharmacist/Admin, Sales Representative  

**Processes** (verb phrases):
- 1.0 Manage Medicine Catalog
- 2.0 Track Stock
- 3.0 Generate Reorder Alerts

**Data stores**: Medicine (D1), Stock Movement (D2), Reorder Alert (D3), Category (D4), Manufacturer (D5)

**Main flows**:
- Pharmacist → Medicine info / Stock movement → Manage Catalog, Track Stock → Medicine, Stock Movement, Categories, Manufacturers → Inventory report, Reorder alerts to Pharmacist
- Sales Rep → Medicine query → Manage Catalog → Medicine catalog to Sales Rep

---

## 3. Payment Data Flow

**File**: `DFD_LEVEL1_PAYMENT_FLOW.mmd`

**Descriptive paragraph:** The Payment Data Flow diagram presents a Level 1 view of how payment information moves through the OnCare system, with three external actors—Sales Representative, Pharmacist/Admin, and External Payment Gateway—interacting with three core processes (Submit Payment, Verify Payment, and Reject Payment) and three data stores (Payment Submission, Transaction, and File Upload). This flow directly supports Neo Care Philippines’ need for controlled, auditable payment handling: Sales Representatives submit payment details and receipts for orders, receive confirmations, and may receive verification or rejection notices; Pharmacists/Admins verify or reject submissions and see verification status; and the External Payment Gateway optionally exchanges payment requests and responses with the system. The separation of Payment Submission (manual proof and status), Transaction (verified records), and File Upload (receipts) ensures that every submission is traceable and that only verified payments update order and transaction records. This architecture is essential for moving from informal or manual payment confirmation to a clear, role-based workflow that supports accountability, reduces disputes, and aligns with operational and compliance expectations for Neo Care Philippines’ pharmaceutical ordering and distribution.

**External entities**: Sales Representative, Pharmacist/Admin, External Payment Gateway  

**Processes** (verb phrases):
- 1.0 Submit Payment
- 2.0 Verify Payment
- 3.0 Reject Payment

**Data stores**: Payment Submission (D1), Transaction (D2), File Upload (D3)

**Main flows**:
- Sales Rep → Payment info / Receipt → Submit Payment → Payment Submission, File Upload → Confirmation to Sales Rep
- Pharmacist → Verify / Reject → Verify Payment or Reject Payment → update Payment Submission, Transaction → Verification status / Rejection notice to Sales Rep and Pharmacist
- Optional: External Payment Gateway ↔ Verify Payment (request/response)

---

## How to view

Copy the contents of each `.mmd` file into [Mermaid Live Editor](https://mermaid.live) or use any Mermaid-supported viewer (e.g. VS Code with Mermaid extension, GitHub/GitLab).
