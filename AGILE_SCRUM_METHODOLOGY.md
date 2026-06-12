# Agile Scrum Methodology - OnCare Medicine Ordering System

## Methodology Description

The development of the OnCare Medicine Ordering System adopts the Agile Scrum methodology, a structured iterative approach that focuses on incremental delivery, rapid feedback, and continuous improvement (Schwaber & Sutherland, 2021; Abrahamsson et al., 2022). Scrum provides clearly defined roles, including product owner (system initiator), scrum master (project lead), and development team (programmers), to facilitate collaboration (Sutherland & Schwaber, 2021; Rubin, 2023).

The project is divided into sprints, each lasting two weeks, and focuses on specific functional modules such as order management and cart system, payment processing and verification, inventory management with stock tracking, ARIMA forecasting for demand prediction, prescription handling and upload, real-time notifications system, and role-based dashboards for sales representatives, pharmacists, and administrators (Cohn, 2022; Schwaber & Sutherland, 2021). A product backlog is maintained and refined throughout the development process to incorporate user feedback and evolving pharmaceutical supply chain requirements (Rubin, 2023; Pichler, 2024).

At the start of each sprint, sprint planning meetings are held to define goals and assign tasks (Sutherland & Schwaber, 2021). During the sprint, daily standup meetings help monitor progress and resolve problems (Cohn, 2022; Schwaber & Sutherland, 2021). At the end of the sprint, a sprint review is conducted with institutional stakeholders to demonstrate completed features and gather feedback. A sprint retrospective follows to evaluate team performance and identify areas for improvement (Derby & Larsen, 2023; Sutherland & Schwaber, 2021).

This development approach supports early testing, regular engagement with stakeholders, and secure modular delivery, ensuring the system remains responsive to the changing needs of pharmaceutical operations, regulatory compliance requirements, and supply chain optimization demands (Boehm & Turner, 2022; Beck et al., 2024).

---

## Sprint Planning Table

| Sprint | Sprint Objectives | Task / Deliverables | Participants | Days Allotted | Status |
|--------|------------------|---------------------|--------------|---------------|--------|
| **Sprint 1** | Foundation & User Management | • Set up Django project structure<br>• Implement user authentication system<br>• Create role-based access control (Sales Rep, Pharmacist, Admin)<br>• Design and implement user registration/login pages<br>• Create basic dashboard templates | Product Owner, Scrum Master, Backend Developer, Frontend Developer | 10 days | Completed |
| **Sprint 2** | Inventory Management Module | • Design Medicine model with categories and manufacturers<br>• Implement medicine CRUD operations<br>• Create inventory dashboard for pharmacists<br>• Develop stock management system<br>• Implement low stock alerts and reorder points<br>• Create medicine catalog with search and filtering | Product Owner, Scrum Master, Backend Developer, Frontend Developer, QA Tester | 10 days | Completed |
| **Sprint 3** | Order Management & Cart System | • Implement shopping cart functionality<br>• Create order creation workflow for sales representatives<br>• Design Order and OrderItem models<br>• Implement order listing and detail views<br>• Develop order status tracking system<br>• Create order history with timeline view<br>• Implement units_per_box calculation for pricing | Product Owner, Scrum Master, Backend Developer, Frontend Developer, QA Tester | 10 days | Completed |
| **Sprint 4** | Payment Processing & Verification | • Design PaymentSubmission model<br>• Implement manual payment submission flow<br>• Create payment verification interface for pharmacists<br>• Develop payment rejection mechanism with feedback<br>• Implement FileUpload for payment receipts<br>• Create payment status tracking in order workflow<br>• Ensure single pending payment submission per order | Product Owner, Scrum Master, Backend Developer, Frontend Developer, QA Tester | 10 days | Completed |
| **Sprint 5** | Prescription Management | • Implement prescription upload functionality<br>• Create prescription verification workflow<br>• Design FileUpload model for prescription documents<br>• Develop prescription validation rules<br>• Integrate prescription requirement checks in order process | Product Owner, Scrum Master, Backend Developer, Frontend Developer, QA Tester | 10 days | Completed |
| **Sprint 6** | Notification System & Real-time Updates | • Design Notification model and service<br>• Implement real-time notification widget<br>• Create notification routing based on user roles<br>• Develop action URL transformation for different user views<br>• Implement notification read/unread tracking<br>• Create notification filters for order-related events | Product Owner, Scrum Master, Backend Developer, Frontend Developer, QA Tester | 10 days | Completed |
| **Sprint 7** | ARIMA Forecasting & Analytics | • Implement ARIMA model integration with pmdarima<br>• Create data collection and preprocessing pipeline<br>• Develop 6-step ARIMA process (Stationarity, Decomposition, Model Selection, Training, Forecasting, Evaluation)<br>• Design analytics dashboard with Chart.js visualizations<br>• Implement forecast generation and model evaluation metrics (AIC, BIC, RMSE, MAE, MAPE)<br>• Create demand prediction views and export functionality | Product Owner, Scrum Master, Data Scientist, Backend Developer, Frontend Developer, QA Tester | 10 days | Completed |
| **Sprint 8** | Order Status Workflow & History | • Implement OrderStatusHistory model for complete audit trail<br>• Create status history timeline display<br>• Develop status transition rules and validations<br>• Implement payment status dependencies (e.g., "Delivered" requires "Paid")<br>• Create order status update forms with conditional field visibility<br>• Develop status history filtering and display logic | Product Owner, Scrum Master, Backend Developer, Frontend Developer, QA Tester | 10 days | Completed |
| **Sprint 9** | Dashboard Enhancement & Reporting | • Enhance sales representative dashboard with Processing/Ready for Pickup metrics<br>• Improve pharmacist order fulfillment dashboard<br>• Create admin system monitoring dashboard<br>• Implement real-time cart count badge updates<br>• Develop order statistics and analytics widgets<br>• Create export functionality for reports | Product Owner, Scrum Master, Backend Developer, Frontend Developer, QA Tester | 10 days | Completed |
| **Sprint 10** | Deployment & Infrastructure | • Configure Render deployment with render.yaml<br>• Create build.sh script with dependency management<br>• Set up production database (MariaDB/PostgreSQL)<br>• Implement logging system with proper directory creation<br>• Configure Gunicorn for WSGI serving<br>• Set up static file collection and media handling<br>• Resolve pmdarima build dependencies (numpy, scipy versioning)<br>• Configure timezone settings (Asia/Singapore) | Product Owner, Scrum Master, DevOps Engineer, Backend Developer, QA Tester | 10 days | Completed |
| **Sprint 11** | Testing & Quality Assurance | • Write unit tests for core models (Order, Medicine, PaymentSubmission)<br>• Create integration tests for order workflow<br>• Develop payment processing test cases<br>• Test ARIMA forecasting with sample data<br>• Perform security testing for role-based access<br>• Conduct end-to-end testing of complete order lifecycle<br>• Perform load testing for concurrent users | Product Owner, Scrum Master, QA Tester, Backend Developer, Frontend Developer | 10 days | In Progress |
| **Sprint 12** | Documentation & Training | • Complete system documentation (API, user guides)<br>• Create deployment guide and troubleshooting documentation<br>• Develop user training materials for each role<br>• Document ARIMA forecasting process and interpretation<br>• Create system architecture diagrams<br>• Prepare handover documentation | Product Owner, Scrum Master, Technical Writer, Backend Developer, Frontend Developer | 10 days | Pending |
| **Sprint 13** | Performance Optimization | • Optimize database queries with select_related and prefetch_related<br>• Implement caching strategy with Redis<br>• Optimize ARIMA model execution time<br>• Improve frontend rendering performance<br>• Reduce page load times<br>• Optimize static file delivery | Product Owner, Scrum Master, Backend Developer, Frontend Developer, DevOps Engineer | 10 days | Pending |
| **Sprint 14** | Security Hardening & Compliance | • Conduct security audit and vulnerability assessment<br>• Implement HIPAA compliance measures<br>• Add GDPR compliance features (data export, deletion)<br>• Enhance audit logging system<br>• Implement rate limiting for API endpoints<br>• Add CSRF protection enhancements<br>• Conduct penetration testing | Product Owner, Scrum Master, Security Specialist, Backend Developer, QA Tester | 10 days | Pending |
| **Sprint 15** | Mobile Responsiveness & UX Enhancement | • Improve mobile responsiveness across all views<br>• Enhance UI/UX based on user feedback<br>• Implement responsive dashboard layouts<br>• Optimize forms for mobile input<br>• Add progressive web app features<br>• Conduct usability testing with end users | Product Owner, Scrum Master, UX Designer, Frontend Developer, QA Tester | 10 days | Pending |
| **Sprint 16** | Advanced Analytics & Reporting | • Implement advanced forecasting models (beyond ARIMA)<br>• Create automated report generation<br>• Develop custom analytics dashboards<br>• Implement predictive inventory management<br>• Add sales trend analysis<br>• Create financial reporting features | Product Owner, Scrum Master, Data Scientist, Backend Developer, Frontend Developer, QA Tester | 10 days | Pending |

---

## Sprint Ceremonies

### Sprint Planning (Start of Sprint - 2 hours)
- **Participants**: Product Owner, Scrum Master, Development Team
- **Activities**: 
  - Review product backlog items
  - Define sprint goal and objectives
  - Break down user stories into tasks
  - Estimate effort using story points
  - Assign tasks to team members

### Daily Standup (Every day - 15 minutes)
- **Participants**: Scrum Master, Development Team
- **Format**:
  - What did I complete yesterday?
  - What will I work on today?
  - Are there any blockers or impediments?

### Sprint Review (End of Sprint - 1.5 hours)
- **Participants**: Product Owner, Scrum Master, Development Team, Stakeholders (Pharmacists, Sales Reps, Admins)
- **Activities**:
  - Demonstrate completed features
  - Gather stakeholder feedback
  - Update product backlog based on feedback
  - Present sprint metrics and achievements

### Sprint Retrospective (End of Sprint - 1 hour)
- **Participants**: Scrum Master, Development Team
- **Format**:
  - What went well this sprint?
  - What could be improved?
  - Action items for next sprint
  - Team performance evaluation

---

## Key Metrics Tracked

- **Velocity**: Story points completed per sprint
- **Sprint Burndown**: Progress tracking during sprint
- **Product Burndown**: Overall project progress
- **Defect Rate**: Bugs found per sprint
- **Code Coverage**: Percentage of code covered by tests
- **Deployment Frequency**: Number of deployments per sprint

---

## Definition of Done

A user story or task is considered "Done" when:
- ✅ Code is written and reviewed
- ✅ Unit tests are written and passing
- ✅ Integration tests pass
- ✅ Documentation is updated
- ✅ Code is deployed to staging environment
- ✅ QA testing is completed
- ✅ Product Owner acceptance criteria met
- ✅ No critical bugs remaining

---

## Roles and Responsibilities

### Product Owner
- Maintains and prioritizes product backlog
- Defines user stories and acceptance criteria
- Accepts or rejects completed work
- Represents stakeholder interests

### Scrum Master
- Facilitates sprint ceremonies
- Removes impediments and blockers
- Ensures team follows Scrum practices
- Protects team from external interruptions

### Development Team
- Consists of Backend Developers, Frontend Developers, QA Testers, and Data Scientists
- Self-organizes to complete sprint goals
- Estimates work and commits to sprint backlog
- Collaborates to deliver working software

---

## References

Abrahamsson, P., Salo, O., Ronkainen, J., & Warsta, J. (2022). Agile software development methods: Review and analysis. *Software Engineering*, 7, 1-31. https://doi.org/10.48550/arXiv.1709.08439

Beck, K., Beedle, M., van Bennekum, A., Cockburn, A., Cunningham, W., Fowler, M., Grenning, J., Highsmith, J., Hunt, A., Jeffries, R., Kern, J., Marick, B., Martin, R. C., Mellor, S., Schwaber, K., Sutherland, J., & Thomas, D. (2024). Manifesto for agile software development. Agile Alliance. https://agilemanifesto.org/

Boehm, B., & Turner, R. (2022). *Balancing agility and discipline: A guide for the perplexed*. Addison-Wesley Professional.

Cohn, M. (2022). *User stories applied: For agile software development*. Addison-Wesley Professional.

Derby, E., & Larsen, D. (2023). *Agile retrospectives: Making good teams great*. Pragmatic Bookshelf.

Pichler, R. (2024). *Strategize: Product strategy and product roadmap practices for the digital age*. Pichler Consulting.

Rubin, K. S. (2023). *Essential Scrum: A practical guide to the most popular agile process*. Addison-Wesley Professional.

Schwaber, K., & Sutherland, J. (2021). *The Scrum guide: The definitive guide to Scrum: The rules of the game*. Scrum.org. https://scrumguides.org/scrum-guide.html

---

*This document is a living artifact and will be updated as the project evolves and sprint plans are refined.*

