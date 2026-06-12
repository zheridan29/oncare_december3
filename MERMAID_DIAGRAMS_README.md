# Mermaid Diagrams for OnCare Medicine Ordering System

This directory contains Mermaid diagram files for visualizing the data flow and system architecture of the OnCare Medicine Ordering System.

## Available Diagrams

### 1. `DATA_FLOW_DIAGRAM.mmd`
**Comprehensive Level 1 Data Flow Diagram**

This is the main data flow diagram showing:
- All 4 external entities (Sales Rep, Pharmacist/Admin, System Admin, Payment Gateway)
- All 7 major processes (User Management, Order Processing, Payment Processing, Inventory Management, Prescription Management, Notification System, Analytics & Forecasting)
- All 16 data stores (D1-D16)
- Complete data flows between all components

**Use this for**: Complete system overview, documentation, stakeholder presentations

**How to view**: 
- Copy the content into [Mermaid Live Editor](https://mermaid.live)
- Or use any Markdown viewer that supports Mermaid (GitHub, GitLab, VS Code with Mermaid extension)

---

### 2. `DFD_CONTEXT_DIAGRAM.mmd`
**Level 0 Context Diagram**

Shows the system as a single process with all external entities and their main interactions.

**Use this for**: High-level overview, system boundaries, initial discussions

**Key Features**:
- Simple, easy to understand
- Shows system boundaries clearly
- Identifies all external entities

---

### 3. `DFD_PROCESS_FLOW.mmd`
**Process Flow Diagram**

Shows the relationships and flow between major processes without data stores.

**Use this for**: Understanding process dependencies, workflow visualization

**Key Features**:
- Shows process groupings
- Illustrates process dependencies
- Clean, simplified view

---

### 4. `DFD_ORDER_LIFECYCLE.mmd`
**Order Lifecycle Data Flow**

Detailed diagram showing the complete order lifecycle from creation to delivery.

**Use this for**: Understanding order workflow, training materials, process documentation

**Key Features**:
- Shows three main phases: Order Creation, Payment, Fulfillment
- Includes all relevant data stores
- Shows notification triggers
- Color-coded by phase

---

### 5. `DFD_LEVEL1_PROCESS1_USER_MANAGEMENT.mmd`
**Level 1 DFD: User Management Process**

Decomposes Process 1.0 into 5 sub-processes:
- 1.1 Authenticate User
- 1.2 Register New User
- 1.3 Manage User Profile
- 1.4 Manage User Roles
- 1.5 Track User Sessions

**Use this for**: Understanding authentication flow, user management implementation

---

### 6. `DFD_LEVEL1_PROCESS2_ORDER_PROCESSING.mmd`
**Level 1 DFD: Order Processing Process**

Decomposes Process 2.0 into 5 sub-processes:
- 2.1 Manage Shopping Cart
- 2.2 Create Order
- 2.3 View Orders
- 2.4 Update Order Status
- 2.5 Track Order History

**Use this for**: Understanding order workflow, cart management, status tracking

---

### 7. `DFD_LEVEL1_PROCESS3_PAYMENT_PROCESSING.mmd`
**Level 1 DFD: Payment Processing Process**

Decomposes Process 3.0 into 5 sub-processes:
- 3.1 Submit Payment Information
- 3.2 Verify Payment
- 3.3 Reject Payment Submission
- 3.4 Process Gateway Payment
- 3.5 Manage Payment Status

**Use this for**: Understanding payment flow, verification process, gateway integration

---

### 8. `DFD_LEVEL1_PROCESS4_INVENTORY_MANAGEMENT.mmd`
**Level 1 DFD: Inventory Management Process**

Decomposes Process 4.0 into 5 sub-processes:
- 4.1 Manage Medicine Catalog
- 4.2 Track Stock Movements
- 4.3 Generate Reorder Alerts
- 4.4 Update Stock Levels
- 4.5 Manage Categories & Manufacturers

**Use this for**: Understanding inventory operations, stock management, catalog organization

---

### 9. `DFD_LEVEL1_PROCESS5_PRESCRIPTION_MANAGEMENT.mmd`
**Level 1 DFD: Prescription Management Process**

Decomposes Process 5.0 into 4 sub-processes:
- 5.1 Upload Prescription
- 5.2 Verify Prescription
- 5.3 Validate Prescription Requirements
- 5.4 Store Prescription Files

**Use this for**: Understanding prescription workflow, file management, verification process

---

### 10. `DFD_LEVEL1_PROCESS6_NOTIFICATION_SYSTEM.mmd`
**Level 1 DFD: Notification System Process**

Decomposes Process 6.0 into 4 sub-processes:
- 6.1 Generate Notifications
- 6.2 Route Notifications
- 6.3 Track Notification Status
- 6.4 Deliver Notifications

**Use this for**: Understanding notification flow, event-driven architecture, real-time delivery

---

### 11. `DFD_LEVEL1_PROCESS7_ANALYTICS_FORECASTING.mmd`
**Level 1 DFD: Analytics & Forecasting Process**

Decomposes Process 7.0 into 4 sub-processes:
- 7.1 Collect Historical Data
- 7.2 Run ARIMA Forecasting
- 7.3 Generate Analytics Reports
- 7.4 Calculate Inventory Optimization

**Use this for**: Understanding analytics pipeline, forecasting process, report generation

---

### 12. `DFD_LEVEL1_SUMMARY.md`
**Level 1 DFD Summary Document**

Comprehensive documentation of all Level 1 DFDs with:
- Sub-process descriptions
- Key data stores
- External entities
- Key data flows
- Common patterns

**Use this for**: Quick reference, documentation, understanding all process decompositions

---

### 13. `DFD_LEVEL0_CONTEXT.mmd`
**Improved Level 0 Context Diagram**

Enhanced context diagram following food ordering system best practices:
- Single process representing the system
- All external entities with clear data flows
- No data stores (as per Level 0 standards)
- Simplified, high-level overview

**Use this for**: Initial system overview, stakeholder presentations, system boundaries

**Based on**: [Visual Paradigm Food Ordering System Example](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)

---

### 14. `DFD_LEVEL1_IMPROVED.mmd`
**Improved Level 1 DFD**

Enhanced Level 1 DFD following best practices:
- 5 major processes (optimal range: 5-7)
- Verb phrases for processes (e.g., "Process Orders", "Manage Inventory")
- Nouns for data stores (e.g., "Orders", "Users", "Payments")
- Simplified data store names
- Clear data flow labels

**Use this for**: System documentation, following industry standards, best practices reference

**Based on**: [Visual Paradigm](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp) and [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/dfd-for-food-ordering-system/) food ordering system examples

---

### 15. `DFD_LEVEL2_PROCESS_ORDERS.mmd`
**Level 2 DFD: Process Orders Decomposition**

Shows decomposition of "Process Orders" into sub-processes:
- 2.1 Manage Shopping Cart
- 2.2 Create Order
- 2.3 Update Order Status
- 2.4 Track Order History

**Use this for**: Detailed process understanding, implementation guidance, training

**Based on**: Food ordering system decomposition patterns

---

### 16. `DFD_BEST_PRACTICES_GUIDE.md`
**DFD Best Practices Guide**

Comprehensive guide based on food ordering system examples:
- Naming conventions (verb phrases for processes, nouns for data stores)
- Rules and guidelines
- Common mistakes to avoid
- Comparison with food ordering system
- OnCare-specific adaptations

**Use this for**: Learning DFD best practices, ensuring quality, training team members

**References**:
- [Visual Paradigm - DFD Example](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)
- [GeeksforGeeks - DFD for Food Ordering System](https://www.geeksforgeeks.org/software-engineering/dfd-for-food-ordering-system/)

---

### 17. `DFD_COMPARISON_FOOD_ORDERING.md`
**DFD Comparison: Food vs Medicine Ordering**

Detailed comparison between food ordering system (reference) and medicine ordering system:
- Level 0 comparison
- Level 1 comparison
- Process naming comparison
- Data store naming comparison
- Complexity analysis
- Best practices applied
- Key learnings

**Use this for**: Understanding differences, validating approach, learning from examples

---

### 18. `DFD_LEVEL0_CONTEXT_REWRITTEN.mmd`
**Rewritten Level 0 Context Diagram**

Completely rewritten context diagram following the exact structure from food ordering system examples:
- Single process representing entire system
- All external entities with clear data flows
- No data stores (Level 0 standard)
- Simplified, clean structure matching reference examples

**Use this for**: Official documentation, following exact reference patterns, clean presentation

**Based on**: [Visual Paradigm Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)

---

### 19. `DFD_LEVEL1_REWRITTEN.mmd`
**Rewritten Level 1 DFD**

Completely rewritten Level 1 DFD following the exact pattern from food ordering system:
- 4 main processes (within optimal 5-7 range)
- Verb phrases for processes: "Order Medicine", "Verify Payment", "Order Inventory", "Generate Reports"
- Nouns for data stores: "Orders", "Payments", "Inventory", "Prescriptions"
- Clear, simple structure matching food ordering system pattern
- All best practices applied

**Use this for**: Official system documentation, following reference examples exactly, best practices reference

**Based on**: [Visual Paradigm](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp) and [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/dfd-for-food-ordering-system/) food ordering system examples

---

### 20. `DFD_REWRITTEN_DOCUMENTATION.md`
**Documentation for Rewritten DFDs**

Comprehensive documentation explaining the rewritten DFDs:
- Detailed explanation of Level 0 and Level 1
- Process descriptions
- Data store descriptions
- Comparison with food ordering system
- Best practices applied
- Usage guidelines

**Use this for**: Understanding the rewritten DFDs, documentation reference, training material

---

### 21. `DFD_FOOD_VS_MEDICINE_COMPARISON.mmd`
**Visual Comparison Diagram**

Side-by-side visual comparison of food ordering system and medicine ordering system DFD structures:
- Shows both systems' processes, entities, and data stores
- Visual representation of similarities and differences
- Easy to understand comparison

**Use this for**: Quick visual comparison, presentations, understanding structure differences

---

### 22. `DFD_LEVEL0_CONTEXT_FINAL.mmd`
**Final Context Diagram - Visual Paradigm Aligned**

Simplified context diagram following the **exact structure** from Visual Paradigm Food Ordering System:
- Single process representing entire system
- 4 external entities with minimal, essential data flows
- No data stores (Level 0 standard)
- Matches Visual Paradigm example structure exactly

**Use this for**: Official documentation, exact Visual Paradigm pattern, simplified presentation

**Reference**: [Visual Paradigm Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)

---

### 23. `DFD_LEVEL1_FINAL.mmd`
**Final Level 1 DFD - Visual Paradigm Aligned**

Simplified Level 1 DFD following the **exact pattern** from Visual Paradigm:
- **3 processes** (matches food system's 3 processes):
  - 1.0 Order Medicine
  - 2.0 Generate Reports
  - 3.0 Order Inventory
- **2 data stores** (matches food system):
  - D1: Order
  - D2: Inventory
- Verb phrases for processes
- Nouns for data stores
- Exact structure matching Visual Paradigm example

**Use this for**: Official system documentation, exact Visual Paradigm pattern, simplified structure

**Reference**: [Visual Paradigm Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)

---

### 24. `DFD_VISUAL_PARADIGM_ALIGNED.md`
**Documentation for Visual Paradigm Aligned DFDs**

Comprehensive documentation explaining the final DFDs aligned with Visual Paradigm:
- Detailed explanation matching Visual Paradigm descriptions
- Process-by-process comparison with food system
- Visual Paradigm best practices applied
- Entity mapping (Customer→Sales Rep, Kitchen→Pharmacist, etc.)
- All 8 tips and cautions from Visual Paradigm article

**Use this for**: Understanding the aligned DFDs, reference documentation, training material

**Reference**: [Visual Paradigm Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)

---

### 25. `DFD_ANALYSIS_AND_VP_GUIDE.md`
**Analysis and Visual Paradigm Step-by-Step Guide**

Document that:
- **Analyzes** `DATA_FLOW_DIAGRAM.md` (strengths and comparison with Visual Paradigm guidelines)
- **Summarizes** the Visual Paradigm tutorial (Context diagram, Level 1, tips, cautions)
- **Presents another DFD** built from the VP guide: 4 processes (Order Medicine, Verify Payment, Generate Reports, Order Inventory) and 3 data stores (Order, Inventory, Payment)

**Use this for**: Understanding how to create a DFD from the VP guide, comparing detailed vs VP-style diagrams

**Reference**: [Visual Paradigm Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)

---

### 26. `DFD_LEVEL1_VP_4PROCESS.mmd`
**Level 1 DFD – 4-Process Variant (VP Guide)**

Another DFD created from the Visual Paradigm guide with payment explicitly modeled:
- **4 processes** (verb phrases): 1.0 Order Medicine, 2.0 Verify Payment, 3.0 Generate Reports, 4.0 Order Inventory
- **3 data stores** (nouns): D1 Order, D2 Inventory, D3 Payment
- Follows all VP tips and cautions (no entity–data-store links, no black-hole processes, data flows as data)

**Use this for**: Stakeholder overview with payment visibility, VP-compliant alternative to the 3-process version

**Reference**: [Visual Paradigm Food Ordering System](https://www.visual-paradigm.com/tutorials/data-flow-diagram-example-food-ordering-system.jsp)

---

## How to Use These Diagrams

### Option 1: Mermaid Live Editor (Recommended)
1. Go to [https://mermaid.live](https://mermaid.live)
2. Copy the content from any `.mmd` file
3. Paste into the editor
4. View, edit, or export as PNG/SVG

### Option 2: VS Code
1. Install the "Markdown Preview Mermaid Support" extension
2. Open the `.mmd` file
3. Use the preview feature

### Option 3: GitHub/GitLab
1. Create a Markdown file (`.md`)
2. Wrap the Mermaid code in a code block:
   ````markdown
   ```mermaid
   [paste mermaid code here]
   ```
   ````
3. Commit and push - GitHub/GitLab will render it automatically

### Option 4: Documentation Tools
- **Confluence**: Use Mermaid macro
- **Notion**: Use Mermaid code blocks
- **Obsidian**: Native Mermaid support
- **Jupyter Notebooks**: Use `%%mermaid` magic command

---

## Diagram Types Explained

### Data Flow Diagram (DFD)
Shows how data moves through the system:
- **External Entities**: Users, external systems (rectangles)
- **Processes**: System functions (rounded rectangles)
- **Data Stores**: Databases, file systems (open rectangles with double lines)
- **Data Flows**: Arrows showing data movement

### Process Flow Diagram
Shows the sequence and relationships between processes:
- Focuses on process dependencies
- Shows workflow and sequence
- Useful for understanding system behavior

### Context Diagram
High-level view showing:
- System boundaries
- External entities
- Main data exchanges
- System scope

---

## Color Coding

### External Entities
- **Sales Representative**: Light Blue (#e1f5ff)
- **Pharmacist/Admin**: Light Orange (#fff4e1)
- **System Admin**: Light Pink (#ffe1f5)
- **Payment Gateway**: Light Green (#e1ffe1)

### Processes
- **User Management**: Light Red (#ffcccc)
- **Order Processing**: Light Green (#ccffcc)
- **Payment Processing**: Light Blue (#ccccff)
- **Inventory Management**: Light Yellow (#ffffcc)
- **Prescription Management**: Light Magenta (#ffccff)
- **Notification System**: Light Cyan (#ccffff)
- **Analytics & Forecasting**: Light Red (#ffcccc)

### Data Stores
- All data stores: Light Green (#e1ffe1)

---

## Customization

You can customize these diagrams by:

1. **Changing Colors**: Modify the `fill` and `stroke` values in the style definitions
2. **Adding Details**: Add more processes, data stores, or flows
3. **Simplifying**: Remove less critical flows for simpler views
4. **Reorganizing**: Rearrange components for better readability

---

## Integration with Documentation

These diagrams complement:
- `DATA_FLOW_DIAGRAM.md` - Detailed text-based DFD documentation
- `FUNCTIONAL_REQUIREMENTS.md` - Functional requirements
- `NON_FUNCTIONAL_REQUIREMENTS.md` - Non-functional requirements
- `AGILE_SCRUM_METHODOLOGY.md` - Development methodology

---

## Tips for Best Results

1. **Start with Context Diagram**: Use `DFD_CONTEXT_DIAGRAM.mmd` for high-level discussions
2. **Use Process Flow for Workflows**: Use `DFD_PROCESS_FLOW.mmd` to explain process sequences
3. **Use Order Lifecycle for Training**: Use `DFD_ORDER_LIFECYCLE.mmd` for user training
4. **Use Full DFD for Documentation**: Use `DATA_FLOW_DIAGRAM.mmd` for complete system documentation

---

## Export Options

From Mermaid Live Editor, you can export as:
- **PNG**: For presentations, documents
- **SVG**: For scalable graphics, web use
- **PDF**: For documentation

---

## Support

For Mermaid syntax help, visit:
- [Mermaid Documentation](https://mermaid.js.org/)
- [Mermaid Live Editor](https://mermaid.live)
- [Mermaid GitHub](https://github.com/mermaid-js/mermaid)

---

*Last Updated: December 2025*

