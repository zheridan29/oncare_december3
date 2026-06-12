# Data Flow Diagram Best Practices Guide
## Based on Food Ordering System Examples

This guide is based on industry best practices from [Visual Paradigm](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp) and [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/dfd-for-food-ordering-system/) food ordering system examples, adapted for the OnCare Medicine Ordering System.

---

## DFD Levels

### Level 0: Context Diagram
- Shows the system as a **single process**
- Shows all **external entities**
- Shows **data flows** between entities and system
- **No data stores** at this level
- Simple, high-level overview

### Level 1: Major Processes
- Decomposes the system into **5-7 major processes**
- Shows **external entities**
- Shows **data stores**
- Shows **data flows** between processes, entities, and stores
- Each process represents a major function

### Level 2: Sub-Processes
- Decomposes each Level 1 process into sub-processes
- More detailed view of each major function
- Shows internal data flows within a process

---

## Naming Conventions

### Processes
- **Use verb phrases** (e.g., "Process Orders", "Manage Inventory", "Verify Payment")
- Examples:
  - ✅ "Process Orders"
  - ✅ "Manage Users"
  - ✅ "Generate Reports"
  - ❌ "Order Processing" (noun phrase)
  - ❌ "User Management" (noun phrase)

### Data Stores
- **Use nouns** (e.g., "Orders", "Users", "Payments", "Inventory")
- Examples:
  - ✅ "Orders"
  - ✅ "Users"
  - ✅ "Payments"
  - ❌ "Order Database" (too technical)
  - ❌ "User Management System" (process name)

### External Entities
- **Use role names or system names** (e.g., "Customer", "Manager", "Payment Gateway")
- Examples:
  - ✅ "Sales Representative"
  - ✅ "Pharmacist/Admin"
  - ✅ "External Payment Gateway"

### Data Flows
- **Use descriptive names** that indicate what data is flowing
- Examples:
  - ✅ "Order"
  - ✅ "Payment Information"
  - ✅ "Order Status"
  - ❌ "Data" (too vague)
  - ❌ "Request" (use specific request type)

---

## Rules and Guidelines

### 1. Process Rules
- ✅ Process labels should be **verb phrases**
- ✅ A process must have **at least one input** and **at least one output**
- ✅ Processes are numbered (1.0, 2.0, 3.0, etc.) for identification
- ❌ Avoid "black-hole" processes (inputs but no outputs)
- ❌ Avoid "miracle" processes (outputs but no inputs)

### 2. Data Store Rules
- ✅ Data stores are represented by **nouns**
- ✅ A data store must be **associated with at least one process**
- ✅ Data stores are shown as **open rectangles** (or cylinders in some notations)
- ❌ **Never connect data stores directly to external entities**
- ❌ Data stores should not be connected to each other

### 3. External Entity Rules
- ✅ External entities must be **associated with at least one process**
- ✅ External entities are shown as **rectangles**
- ❌ **Never have data flows between two external entities** without going through a process

### 4. Data Flow Rules
- ✅ Data flows show **what data** is being exchanged, not how
- ✅ Data flows are **one-way** (use bidirectional arrows only when necessary)
- ✅ Data flows connect:
  - External entity ↔ Process
  - Process ↔ Data Store
  - Process ↔ Process
- ❌ **Don't mix data flow with process flow**
- ❌ Don't label flows as "request" when connecting to data stores (the data itself is the flow)

### 5. Complexity Guidelines
- ✅ **5-7 processes** are manageable for Level 1 DFD
- ✅ If more than 7 processes, consider grouping related processes
- ✅ Keep diagrams readable and understandable
- ❌ Avoid overcrowding with too many processes

### 6. Numbering Guidelines
- ✅ Numbering does **not necessarily indicate sequence**
- ✅ Numbering is useful for **identifying processes** when discussing with users
- ✅ Use hierarchical numbering:
  - Level 1: 1.0, 2.0, 3.0
  - Level 2: 1.1, 1.2, 2.1, 2.2
  - Level 3: 1.1.1, 1.1.2, 2.1.1

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Connecting Data Store to External Entity
```
WRONG:
Customer --> Orders
Orders --> Customer

CORRECT:
Customer --> Process Orders --> Orders
Orders --> Process Orders --> Order Details --> Customer
```

### ❌ Mistake 2: Data Flow Between External Entities
```
WRONG:
Customer --> Order --> Manager

CORRECT:
Customer --> Process Orders --> Order --> Manager
```

### ❌ Mistake 3: Using Process Names for Data Stores
```
WRONG:
Process --> Order Processing

CORRECT:
Process Orders --> Orders
```

### ❌ Mistake 4: Labeling Data Flows as "Request"
```
WRONG:
Process --> Request --> Data Store

CORRECT:
Process --> Order Information --> Orders
```

### ❌ Mistake 5: Too Many Processes
```
WRONG: 15 processes in Level 1 DFD

CORRECT: 5-7 processes, group related functions
```

---

## OnCare Medicine Ordering System - DFD Structure

### Level 0: Context Diagram
- **System**: OnCare Medicine Ordering System
- **External Entities**: 
  - Sales Representative
  - Pharmacist/Admin
  - System Admin
  - External Payment Gateway

### Level 1: Major Processes (5-7 processes)
1. **1.0 Manage Users** - Authentication and authorization
2. **2.0 Process Orders** - Order creation and fulfillment
3. **3.0 Process Payments** - Payment submission and verification
4. **4.0 Manage Inventory** - Stock and catalog management
5. **5.0 Generate Reports** - Analytics and forecasting

### Level 2: Sub-Processes
Each Level 1 process can be decomposed into 3-5 sub-processes:
- **1.0 Manage Users** → 1.1 Authenticate, 1.2 Register, 1.3 Manage Profile
- **2.0 Process Orders** → 2.1 Manage Cart, 2.2 Create Order, 2.3 Update Status
- **3.0 Process Payments** → 3.1 Submit Payment, 3.2 Verify Payment, 3.3 Reject Payment
- **4.0 Manage Inventory** → 4.1 Manage Catalog, 4.2 Track Stock, 4.3 Generate Alerts
- **5.0 Generate Reports** → 5.1 Collect Data, 5.2 Run Forecasting, 5.3 Generate Reports

---

## Data Store Naming (Simplified)

Instead of technical names, use business-focused names:

| Technical Name | Business Name |
|---------------|---------------|
| User Database | Users |
| Order Database | Orders |
| Payment Submission Database | Payments |
| Medicine Database | Inventory |
| File Upload Database | Prescriptions |
| Notification Database | Notifications |

---

## Comparison: Food Ordering vs Medicine Ordering

### Food Ordering System (Reference)
- **Processes**: Order Food, Generate Reports, Order Inventory
- **Entities**: Customer, Kitchen, Manager, Supplier
- **Data Stores**: Orders, Inventory

### Medicine Ordering System (OnCare)
- **Processes**: Process Orders, Process Payments, Manage Inventory, Manage Users, Generate Reports
- **Entities**: Sales Representative, Pharmacist/Admin, System Admin, Payment Gateway
- **Data Stores**: Orders, Payments, Inventory, Users, Prescriptions, Notifications

---

## References

1. [Visual Paradigm - DFD Example: Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)
2. [GeeksforGeeks - DFD for Food Ordering System](https://www.geeksforgeeks.org/software-engineering/dfd-for-food-ordering-system/)

---

*This guide follows industry best practices for Data Flow Diagrams and is specifically adapted for the OnCare Medicine Ordering System.*

