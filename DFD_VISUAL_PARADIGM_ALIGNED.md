# Data Flow Diagram - Aligned with Visual Paradigm Food Ordering System

This document provides the Data Flow Diagrams for the OnCare Medicine Ordering System, following the **exact structure and patterns** from the [Visual Paradigm Food Ordering System example](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp).

## Reference

**Visual Paradigm Tutorial**: [Data Flow Diagram: Examples - Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)

---

## Level 0: Context Diagram

**File**: `DFD_LEVEL0_CONTEXT_FINAL.mmd`

### Description
The context diagram shows the OnCare Medicine Ordering System as a single process with all external entities and their data exchanges. This follows the **exact pattern** from the Visual Paradigm food ordering system example.

### Key Characteristics (from Visual Paradigm)
1. ✅ **One process** representing the entire system
2. ✅ **External entities** that interact with the system
3. ✅ **Data flows** between entities and system
4. ✅ **NO data stores** at this level (Level 0 standard)

### External Entities
- **Sales Representative** - Places orders (similar to Customer in food system)
- **Pharmacist/Admin** - Receives orders for fulfillment (similar to Kitchen in food system)
- **System Admin** - Manages reports and inventory orders (similar to Manager in food system)
- **External Payment Gateway** - Receives inventory orders (similar to Supplier in food system)

### Data Flows

**From Sales Representative:**
- Order → System

**To Sales Representative:**
- Bill ← System

**To Pharmacist/Admin:**
- Order ← System

**From System Admin:**
- Inventory Order → System

**To System Admin:**
- Reports ← System

**To External Payment Gateway:**
- Inventory Order ← System

---

## Level 1: Major Processes

**File**: `DFD_LEVEL1_FINAL.mmd`

### Description
The Level 1 DFD decomposes the system into **3 main processes**, following the **exact pattern** from the Visual Paradigm food ordering system example (which also has 3 processes).

### Main Processes

#### 1.0 Order Medicine
**Exact match to "Order Food" in food system**

Based on Visual Paradigm's description:
> "The Order Food process receives the Order, forwards it to the Kitchen, stores it in the Order data store, and stores the updated Inventory details in the Inventory data store. The process also delivers a Bill to the Customer."

**For Medicine System:**
- Receives **Order** from Sales Representative
- Forwards **Order** to Pharmacist/Admin
- Stores **Order** in Order data store
- Stores updated **Inventory details** in Inventory data store
- Delivers **Bill** to Sales Representative

**Data Flows:**
- Sales Representative → Order → Process 1.0
- Process 1.0 → Order → Pharmacist/Admin
- Process 1.0 → Order → D1 (Order data store)
- Process 1.0 → Inventory details → D2 (Inventory data store)
- D1 → Orders → Process 1.0
- D2 → Inventory details → Process 1.0
- Process 1.0 → Bill → Sales Representative

#### 2.0 Generate Reports
**Exact match to "Generate Reports" in food system**

Based on Visual Paradigm's description:
> "The Manager can receive Reports through the Generate Reports process, which takes Inventory details and Orders as input from the Inventory and Order data stores, respectively."

**For Medicine System:**
- System Admin requests reports
- Process takes **Inventory details** from Inventory data store
- Process takes **Orders** from Order data store
- Process delivers **Reports** to System Admin

**Data Flows:**
- System Admin → Report Request → Process 2.0
- D2 → Inventory details → Process 2.0
- D1 → Orders → Process 2.0
- Process 2.0 → Reports → System Admin

#### 3.0 Order Inventory
**Exact match to "Order Inventory" in food system**

Based on Visual Paradigm's description:
> "The Manager can also initiate the Order Inventory process by providing an Inventory order. The process forwards the Inventory order to the Supplier and stores the updated Inventory details in the Inventory data store."

**For Medicine System:**
- System Admin initiates with **Inventory order**
- Process forwards **Inventory order** to External Payment Gateway
- Process stores updated **Inventory details** in Inventory data store

**Data Flows:**
- System Admin → Inventory order → Process 3.0
- Process 3.0 → Inventory order → External Payment Gateway
- Process 3.0 → Inventory details → D2 (Inventory data store)

### Data Stores

1. **D1: Order** - Stores order information (matches "Order" in food system)
2. **D2: Inventory** - Stores inventory details (matches "Inventory" in food system)

### Key Characteristics (from Visual Paradigm Tips)

✅ **Process labels are verb phrases**
- "Order Medicine" (not "Medicine Ordering")
- "Generate Reports" (not "Report Generation")
- "Order Inventory" (not "Inventory Ordering")

✅ **Data stores are nouns**
- "Order" (not "Order Database")
- "Inventory" (not "Inventory Management System")

✅ **Appropriate complexity**
- 3 processes (within 5-7 manageable range)

✅ **Data store rules**
- All data stores associated with at least one process
- No data stores connected directly to external entities

✅ **External entity rules**
- All external entities associated with at least one process
- No data flows between external entities without going through a process

✅ **Data flow rules**
- Clear, descriptive labels
- No "request" flows (data flows represent data, not process flow)

---

## Comparison: Food vs Medicine Ordering System

### Food Ordering System (Visual Paradigm Example)

**Processes:**
1. Order Food
2. Generate Reports
3. Order Inventory

**Data Stores:**
- Order
- Inventory

**External Entities:**
- Customer
- Kitchen
- Manager
- Supplier

### Medicine Ordering System (OnCare)

**Processes:**
1. Order Medicine
2. Generate Reports
3. Order Inventory

**Data Stores:**
- Order
- Inventory

**External Entities:**
- Sales Representative
- Pharmacist/Admin
- System Admin
- External Payment Gateway

### Mapping

| Food System | Medicine System | Role |
|------------|-----------------|------|
| Customer | Sales Representative | Places orders |
| Kitchen | Pharmacist/Admin | Receives orders for fulfillment |
| Manager | System Admin | Manages reports and inventory |
| Supplier | External Payment Gateway | Receives inventory orders |
| Order Food | Order Medicine | Process orders |
| Generate Reports | Generate Reports | Generate reports |
| Order Inventory | Order Inventory | Order inventory |

---

## Visual Paradigm Best Practices Applied

### ✅ Tips from Visual Paradigm Article

1. **Process labels should be verb phrases; data stores are represented by nouns**
   - ✅ All processes use verb phrases
   - ✅ All data stores use nouns

2. **A data store must be associated with at least one process**
   - ✅ D1 (Order) associated with Process 1.0 and 2.0
   - ✅ D2 (Inventory) associated with Process 1.0, 2.0, and 3.0

3. **An external entity must be associated with at least one process**
   - ✅ Sales Representative → Process 1.0
   - ✅ Pharmacist/Admin → Process 1.0
   - ✅ System Admin → Process 2.0 and 3.0
   - ✅ External Payment Gateway → Process 3.0

4. **Don't let it get too complex; normally, 5-7 processes are manageable**
   - ✅ 3 processes (well within range)

5. **DFDs are non-deterministic—the numbering does not necessarily indicate a sequence**
   - ✅ Process numbering (1.0, 2.0, 3.0) is for identification, not sequence

6. **Data stores should not be connected to an external entity**
   - ✅ No direct connections between data stores and external entities

7. **Data flows should not exist between two external entities without going through a process**
   - ✅ All data flows go through processes

8. **A process that has inputs but no outputs is considered a "black-hole" process**
   - ✅ All processes have both inputs and outputs

### ✅ Cautions from Visual Paradigm Article

**Don't mix up data flow and process flow**
- ✅ Data flows represent data exchange, not process steps
- ✅ No "request" labels on data flows
- ✅ Data stores are treated as data holders, not processors

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

## Files

1. **`DFD_LEVEL0_CONTEXT_FINAL.mmd`** - Context diagram (Level 0)
2. **`DFD_LEVEL1_FINAL.mmd`** - Level 1 DFD with 3 processes
3. **`DFD_VISUAL_PARADIGM_ALIGNED.md`** - This documentation

---

*These DFDs follow the **exact structure and best practices** from the [Visual Paradigm Food Ordering System example](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp), adapted for the specific requirements of the OnCare Medicine Ordering System.*




