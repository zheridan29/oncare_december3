# DFD Level 1 - Process Decomposition Summary

This document provides an overview of the Level 1 Data Flow Diagrams for each of the 7 major processes in the OnCare Medicine Ordering System.

---

## Overview

Each Level 1 DFD decomposes a major process (1.0-7.0) into its sub-processes, showing:
- **Sub-processes** (1.1, 1.2, etc.)
- **External entities** that interact with the process
- **Data stores** used by the process
- **Data flows** between sub-processes, entities, and data stores

---

## Process 1.0: User Management

**File**: `DFD_LEVEL1_PROCESS1_USER_MANAGEMENT.mmd`

### Sub-Processes:
- **1.1 Authenticate User** - Login & Session management
- **1.2 Register New User** - Account creation
- **1.3 Manage User Profile** - Profile updates
- **1.4 Manage User Roles** - Role assignment (Admin only)
- **1.5 Track User Sessions** - Session tracking

### Key Data Stores:
- D1: User Database
- D2: User Session Database
- D17: Audit Log

### External Entities:
- Sales Representative
- Pharmacist/Admin
- System Admin

### Key Flows:
- Login credentials → Authentication → Session creation
- Registration data → User creation → Profile setup
- Profile updates → Database update → Confirmation
- Role assignments → Database update → User list

---

## Process 2.0: Order Processing

**File**: `DFD_LEVEL1_PROCESS2_ORDER_PROCESSING.mmd`

### Sub-Processes:
- **2.1 Manage Shopping Cart** - Add/Update/Remove items
- **2.2 Create Order** - Convert cart to order
- **2.3 View Orders** - List & detail views
- **2.4 Update Order Status** - Status transitions
- **2.5 Track Order History** - Status timeline

### Key Data Stores:
- D3: Cart Database
- D4: Order Database
- D5: Order Status History
- D9: Medicine Database (for stock checks)

### External Entities:
- Sales Representative
- Pharmacist/Admin

### Key Flows:
- Cart items → Cart management → Order creation
- Customer info → Order creation → Order confirmation
- Status updates → Status change → History recording
- Order queries → Database read → Order details

---

## Process 3.0: Payment Processing

**File**: `DFD_LEVEL1_PROCESS3_PAYMENT_PROCESSING.mmd`

### Sub-Processes:
- **3.1 Submit Payment Information** - Manual payment submission
- **3.2 Verify Payment** - Payment verification
- **3.3 Reject Payment Submission** - Payment rejection
- **3.4 Process Gateway Payment** - Online payment processing
- **3.5 Manage Payment Status** - Status management

### Key Data Stores:
- D4: Order Database
- D6: Payment Submission Database
- D7: Transaction Database
- D8: File Upload Database (receipts)
- D5: Order Status History

### External Entities:
- Sales Representative
- Pharmacist/Admin
- External Payment Gateway

### Key Flows:
- Payment info → Submission → Verification queue
- Verification request → Payment check → Status update
- Rejection request → Rejection record → Resubmission allowed
- Gateway response → Transaction creation → Status update

---

## Process 4.0: Inventory Management

**File**: `DFD_LEVEL1_PROCESS4_INVENTORY_MANAGEMENT.mmd`

### Sub-Processes:
- **4.1 Manage Medicine Catalog** - CRUD operations
- **4.2 Track Stock Movements** - Stock in/out/adjustment
- **4.3 Generate Reorder Alerts** - Low stock detection
- **4.4 Update Stock Levels** - Stock calculations
- **4.5 Manage Categories & Manufacturers** - Catalog organization

### Key Data Stores:
- D9: Medicine Database
- D10: Stock Movement Database
- D11: Reorder Alert Database
- D12: Category Database
- D13: Manufacturer Database

### External Entities:
- Pharmacist/Admin
- Sales Representative (read-only)

### Key Flows:
- Medicine info → Catalog management → Database storage
- Stock movements → Movement recording → Stock update
- Stock levels → Alert generation → Notification
- Categories/Manufacturers → Organization → Catalog structure

---

## Process 5.0: Prescription Management

**File**: `DFD_LEVEL1_PROCESS5_PRESCRIPTION_MANAGEMENT.mmd`

### Sub-Processes:
- **5.1 Upload Prescription** - File upload & storage
- **5.2 Verify Prescription** - Prescription validation
- **5.3 Validate Prescription Requirements** - Requirement checking
- **5.4 Store Prescription Files** - File management

### Key Data Stores:
- D4: Order Database
- D8: File Upload Database
- D9: Medicine Database (for requirement flags)
- D5: Order Status History

### External Entities:
- Sales Representative
- Pharmacist/Admin

### Key Flows:
- Prescription file → Upload → File storage
- Verification request → Prescription check → Status update
- Order creation → Requirement check → Prescription needed?
- File storage → File management → File availability

---

## Process 6.0: Notification System

**File**: `DFD_LEVEL1_PROCESS6_NOTIFICATION_SYSTEM.mmd`

### Sub-Processes:
- **6.1 Generate Notifications** - Event to notification conversion
- **6.2 Route Notifications** - User-based routing
- **6.3 Track Notification Status** - Read/unread tracking
- **6.4 Deliver Notifications** - Real-time delivery

### Key Data Stores:
- D14: Notification Database
- D1: User Database (for roles & preferences)

### External Entities:
- Sales Representative
- Pharmacist/Admin
- System Admin

### Event Sources:
- Process 2.0: Order Processing
- Process 3.0: Payment Processing
- Process 4.0: Inventory Management
- Process 5.0: Prescription Management

### Key Flows:
- System events → Notification generation → Routing
- User roles → Notification routing → User-specific delivery
- Notification delivery → Status tracking → Read/unread status
- Real-time updates → Notification delivery → User interface

---

## Process 7.0: Analytics & Forecasting

**File**: `DFD_LEVEL1_PROCESS7_ANALYTICS_FORECASTING.mmd`

### Sub-Processes:
- **7.1 Collect Historical Data** - Data aggregation
- **7.2 Run ARIMA Forecasting** - Demand prediction
- **7.3 Generate Analytics Reports** - Business intelligence
- **7.4 Calculate Inventory Optimization** - EOQ & reorder points

### Key Data Stores:
- **Input**: D4 (Order Database), D9 (Medicine Database), D7 (Transaction Database)
- **Output**: D15 (Forecast Database), D16 (Analytics Database)

### External Entities:
- Pharmacist/Admin
- System Admin

### Key Flows:
- Historical data → Data collection → Aggregated data
- Aggregated data → ARIMA forecasting → Forecast results
- Historical data → Analytics generation → Business reports
- Forecast data → Optimization calculation → EOQ & reorder points

---

## Common Patterns Across All Processes

### 1. CRUD Operations
Most processes follow Create-Read-Update-Delete patterns:
- Create: External entity → Process → Data store
- Read: Data store → Process → External entity
- Update: External entity → Process → Data store → External entity
- Delete: External entity → Process → Data store

### 2. Validation Flow
- Input → Validation → Valid data → Storage
- Input → Validation → Invalid data → Error message

### 3. Status Tracking
- Status change → Process → Status history → Notification

### 4. Event-Driven Notifications
- Process event → Notification system → User notification

---

## How to Use These Diagrams

1. **For Development**: Use to understand data flows when implementing features
2. **For Documentation**: Include in system documentation
3. **For Training**: Use to explain system processes to new team members
4. **For Analysis**: Use to identify bottlenecks or optimization opportunities
5. **For Testing**: Use to identify test scenarios and data flow paths

---

## Viewing the Diagrams

All diagrams are in Mermaid format (`.mmd`). To view:

1. **Mermaid Live Editor**: Copy content to [https://mermaid.live](https://mermaid.live)
2. **VS Code**: Install Mermaid extension
3. **GitHub/GitLab**: Create `.md` file with mermaid code blocks
4. **Documentation Tools**: Use Mermaid support in Confluence, Notion, etc.

---

## Related Documents

- `DATA_FLOW_DIAGRAM.md` - Complete Level 0 and Level 1 DFD documentation
- `DATA_FLOW_DIAGRAM.mmd` - Main comprehensive DFD
- `MERMAID_DIAGRAMS_README.md` - Guide to all Mermaid diagrams
- `FUNCTIONAL_REQUIREMENTS.md` - Functional requirements
- `NON_FUNCTIONAL_REQUIREMENTS.md` - Non-functional requirements

---

*Last Updated: December 2025*

