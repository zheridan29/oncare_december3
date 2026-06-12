# Entity Relationship Diagram (ERD) — Simple Description

Simple, human-friendly description of the OnCare Medicine Ordering System’s Entity Relationship Diagram.

---

## Descriptive paragraph

The Entity Relationship Diagram (ERD) for the OnCare Medicine Ordering System presents the database structure as a set of main entities—User, Order, Order Item, Medicine, Category, Manufacturer, Cart, Cart Item, Order Status History, Stock Movement, Reorder Alert, and related entities such as Payment Submission, Transaction, Notification, and File Upload—and the relationships between them. Users have role-specific profiles (Sales Rep or Pharmacist/Admin) and create orders and cart items; orders contain order items that reference medicines; medicines belong to a category and a manufacturer and are linked to stock movements and reorder alerts; and payment and notification entities support verification and auditability. This structure directly supports Neo Care Philippines’ need for a single, consistent store of data: who placed which order, what was ordered, how stock and reorders are managed, and how payments and status changes are recorded. The ERD is essential for implementing the ordering, inventory, and payment flows described in the Level 1 DFDs and for ensuring that the system can report, audit, and scale without losing the links between users, orders, medicines, and transactions.

---

## Simple description (in plain language)

**What the ERD shows**

The ERD shows the main “things” the system stores and how they connect.

- **People and roles**  
  **User** is the central table for everyone who logs in. Some users have a **Sales Rep profile** (e.g. employee id, territory); others have a **Pharmacist/Admin profile** (e.g. license). So “user” plus “profile” tells the system whether someone is a sales rep or a pharmacist/admin.

- **Orders**  
  A **User** (sales rep) creates **Orders**. Each **Order** has many **Order Items**; each **Order Item** points to one **Medicine** and stores quantity and price. So we can always say: “This order contains these medicines in these amounts.” **Order Status History** stores each status change (who changed it, when, old and new status), so we have a full history for every order.

- **Shopping before checkout**  
  A **User** (sales rep) has a **Cart**, and the cart has **Cart Items**—each pointing to a **Medicine** with a quantity. When they checkout, the cart is turned into an **Order** and **Order Items**.

- **Medicine catalog and inventory**  
  **Medicine** is the main product table (name, price, stock, reorder point). Each medicine **belongs to** one **Category** and one **Manufacturer**. **Stock Movement** records every increase or decrease in stock (and who did it). **Reorder Alert** records when a medicine hits its reorder point so the pharmacist knows what to order. **Medicine Image** stores product images linked to a medicine.

- **Payment and files**  
  **Payment Submission** stores the payment details and status (e.g. pending, verified, rejected) that the sales rep submits and the pharmacist verifies. **Transaction** stores verified payment/transaction records. **File Upload** stores receipts and other files linked to orders or payments. **Notification** stores in-app notifications for users.

**Why it matters**

The diagram shows how all of this fits together in one database: users, their roles, their orders and cart, the medicines and who makes them (manufacturer) and how they’re grouped (category), stock and reorders, and payment and notification data. That way the system can answer questions like “Who placed this order?”, “What’s the stock for this medicine?”, and “What’s the payment status?” without losing the links between tables.

---

## Main entities (quick reference)

| Entity | Purpose |
|--------|--------|
| User | Everyone who logs in (sales rep, pharmacist, admin) |
| SalesRepProfile / PharmacistAdminProfile | Role-specific data for that user |
| Order | A confirmed order (customer, total, status, payment status) |
| OrderItem | One line on an order (medicine, quantity, price) |
| OrderStatusHistory | Log of every status change on an order |
| Cart / CartItem | Temporary cart before checkout |
| Medicine | Product (name, price, stock, reorder point) |
| Category | Grouping for medicines (e.g. by type) |
| Manufacturer | Who makes the medicine |
| StockMovement | Record of stock in/out |
| ReorderAlert | Alert when stock is at or below reorder point |
| PaymentSubmission | Payment details submitted by sales rep, verified/rejected by pharmacist |
| Transaction | Verified payment/transaction record |
| FileUpload | Uploaded files (receipts, prescriptions) |
| Notification | In-app notifications for users |

---

## Diagram files

- **ERD_MERMAID_READY.md** — Full ERD in Mermaid (all tables) and Level 0 simplified version  
- **ERD_DIAGRAM_SIMPLE.mmd** — Simple ERD (User, Order, OrderItem, Medicine, Category, Manufacturer)  
- **ERD_DIAGRAM_COMPLETE.mmd** — Complete ERD (all entities)  
- **ERD_COMPLETE_WORKFLOW.md** — Process-focused ERD (ordering, inventory, roles)

View any `.mmd` or Mermaid block in [Mermaid Live Editor](https://mermaid.live).
