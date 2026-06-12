# Data Flow Diagram - Rewritten Based on Food Ordering System Examples

This document provides the rewritten Data Flow Diagrams for the OnCare Medicine Ordering System, following the exact structure and patterns from the food ordering system examples.

## References

1. [Visual Paradigm - DFD Example: Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)
2. [GeeksforGeeks - DFD for Food Ordering System](https://www.geeksforgeeks.org/software-engineering/dfd-for-food-ordering-system/)

---

## Level 0: Context Diagram

**File**: `DFD_LEVEL0_CONTEXT_REWRITTEN.mmd`

### Description
The context diagram shows the OnCare Medicine Ordering System as a single process with all external entities and their data exchanges. This follows the exact pattern from the food ordering system example.

### External Entities
- **Sales Representative** - Places orders, submits payments, uploads prescriptions
- **Pharmacist/Admin** - Verifies payments, manages inventory, fulfills orders
- **System Admin** - Manages users and system configuration
- **External Payment Gateway** - Processes online payments

### Key Data Flows

**From Sales Representative:**
- Order → System
- Payment Information → System
- Prescription → System

**To Sales Representative:**
- Order Confirmation ← System
- Bill ← System
- Medicine Catalog ← System

**From Pharmacist/Admin:**
- Order Status Update → System
- Payment Verification → System
- Inventory Order → System

**To Pharmacist/Admin:**
- Order Details ← System
- Payment Submission ← System
- Inventory Report ← System
- Reorder Alert ← System

**From System Admin:**
- User Management → System

**To System Admin:**
- User List ← System
- System Report ← System

**From/To Payment Gateway:**
- Payment Request → Payment Gateway
- Payment Response ← Payment Gateway

### Characteristics
- ✅ Single process representing entire system
- ✅ No data stores (Level 0 standard)
- ✅ Clear data flow labels
- ✅ All external entities identified

---

## Level 1: Major Processes

**File**: `DFD_LEVEL1_REWRITTEN.mmd`

### Description
The Level 1 DFD decomposes the system into 4 main processes, following the food ordering system pattern of having 3-5 manageable processes.

### Main Processes

#### 1.0 Order Medicine
**Similar to "Order Food" in food system**

- **Purpose**: Handle order placement and processing
- **Inputs**: 
  - Order (from Sales Representative)
  - Customer Information (from Sales Representative)
  - Prescription (from Sales Representative)
- **Outputs**:
  - Order Confirmation (to Sales Representative)
  - Bill (to Sales Representative)
  - Order (to Pharmacist/Admin)
- **Data Stores Used**:
  - D1: Orders (read/write)
  - D3: Inventory (read/write)
  - D4: Prescriptions (read/write)

#### 2.0 Verify Payment
**Similar to payment processing in food system**

- **Purpose**: Process payment submissions and verifications
- **Inputs**:
  - Payment Information (from Sales Representative)
  - Payment Receipt (from Sales Representative)
  - Payment Verification (from Pharmacist/Admin)
  - Payment Response (from External Payment Gateway)
- **Outputs**:
  - Payment Status (to Sales Representative)
  - Payment Details (to Pharmacist/Admin)
  - Payment Request (to External Payment Gateway)
- **Data Stores Used**:
  - D2: Payments (read/write)
  - D1: Orders (read/write)

#### 3.0 Order Inventory
**Similar to "Order Inventory" in food system**

- **Purpose**: Manage inventory, stock movements, and reordering
- **Inputs**:
  - Inventory Order (from Pharmacist/Admin)
  - Medicine Information (from Pharmacist/Admin)
  - Stock Movement (from Pharmacist/Admin)
- **Outputs**:
  - Inventory Report (to Pharmacist/Admin)
  - Reorder Alert (to Pharmacist/Admin)
  - Inventory Order (to External Payment Gateway - if needed)
- **Data Stores Used**:
  - D3: Inventory (read/write)

#### 4.0 Generate Reports
**Similar to "Generate Reports" in food system**

- **Purpose**: Generate analytics, forecasts, and system reports
- **Inputs**:
  - Report Request (from Pharmacist/Admin)
  - Analytics Query (from System Admin)
- **Outputs**:
  - Analytics Report (to Pharmacist/Admin)
  - System Report (to System Admin)
  - Forecast Data (to Inventory data store)
- **Data Stores Used**:
  - D1: Orders (read)
  - D2: Payments (read)
  - D3: Inventory (read/write)

### Data Stores

1. **D1: Orders** - Stores order information, order items, and order status
2. **D2: Payments** - Stores payment submissions, transactions, and payment status
3. **D3: Inventory** - Stores medicine catalog, stock levels, and inventory movements
4. **D4: Prescriptions** - Stores prescription files and verification status

### Key Characteristics

✅ **Process Naming**: All processes use verb phrases
- "Order Medicine" (not "Medicine Ordering")
- "Verify Payment" (not "Payment Verification")
- "Order Inventory" (not "Inventory Ordering")
- "Generate Reports" (not "Report Generation")

✅ **Data Store Naming**: All data stores use nouns
- "Orders" (not "Order Database")
- "Payments" (not "Payment System")
- "Inventory" (not "Inventory Management")
- "Prescriptions" (not "Prescription Files")

✅ **Appropriate Complexity**: 4 processes (within 5-7 optimal range)

✅ **Clear Data Flows**: Descriptive labels indicating what data is flowing

✅ **No Direct Connections**: 
- No data stores connected directly to external entities
- No external entities connected directly to each other

---

## Comparison with Food Ordering System

### Food Ordering System Structure
```
Processes:
1. Order Food
2. Generate Reports
3. Order Inventory

Data Stores:
- Orders
- Inventory

External Entities:
- Customer
- Kitchen
- Manager
- Supplier
```

### Medicine Ordering System Structure
```
Processes:
1. Order Medicine
2. Verify Payment
3. Order Inventory
4. Generate Reports

Data Stores:
- Orders
- Payments
- Inventory
- Prescriptions

External Entities:
- Sales Representative
- Pharmacist/Admin
- System Admin
- External Payment Gateway
```

### Key Differences

1. **Additional Process**: Medicine system has "Verify Payment" as a separate process due to regulatory requirements
2. **Additional Data Store**: Medicine system has "Payments" and "Prescriptions" data stores
3. **More Complex**: Medicine system handles prescriptions and payment verification, which food system doesn't need

### Similarities

1. ✅ Same naming conventions (verb phrases for processes, nouns for data stores)
2. ✅ Same structure (context diagram → level 1 decomposition)
3. ✅ Same best practices (no direct data store to entity connections)
4. ✅ Appropriate complexity (within 5-7 process range)

---

## Best Practices Applied

### ✅ From Food Ordering System Examples

1. **Process Labels**: Verb phrases
   - ✅ "Order Medicine"
   - ✅ "Verify Payment"
   - ✅ "Generate Reports"

2. **Data Stores**: Nouns
   - ✅ "Orders"
   - ✅ "Payments"
   - ✅ "Inventory"

3. **Data Store Rules**:
   - ✅ All data stores associated with at least one process
   - ✅ No data stores connected directly to external entities

4. **External Entity Rules**:
   - ✅ All external entities associated with at least one process
   - ✅ No data flows between external entities without a process

5. **Complexity**:
   - ✅ 4 processes (manageable, within 5-7 range)

6. **Data Flow Labels**:
   - ✅ Descriptive names (e.g., "Order", "Payment Information")
   - ✅ Not vague (e.g., not just "Data" or "Request")

---

## Usage

### For Documentation
- Use Level 0 for high-level system overview
- Use Level 1 for detailed system understanding

### For Development
- Use to understand data flows when implementing features
- Use to identify required data stores and processes

### For Training
- Use to explain system architecture to new team members
- Use to show how different user roles interact with the system

### For Stakeholders
- Use Level 0 for non-technical stakeholders
- Use Level 1 for technical discussions

---

## Next Steps

For more detailed decomposition, create Level 2 DFDs for each process:
- 1.1, 1.2, 1.3... for "Order Medicine"
- 2.1, 2.2, 2.3... for "Verify Payment"
- 3.1, 3.2, 3.3... for "Order Inventory"
- 4.1, 4.2, 4.3... for "Generate Reports"

---

*These DFDs follow the exact structure and best practices from the food ordering system examples, adapted for the specific requirements of the OnCare Medicine Ordering System.*





