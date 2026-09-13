# Professional Services Automation / PSA

## Overview

A **Professional Services Automation (PSA) application** is the delivery-side operating system for a project-based services business — consulting firms, IT services companies, agencies, architecture & engineering firms, accounting firms, and internal services divisions of product companies. It runs the closed loop that turns the firm's billable people into revenue: it staffs capacity-bearing professionals onto client projects, captures the time and expenses they incur, converts approved work into client invoices through rate and billing rules, and measures each project's budget, utilization, and margin — rolling all of it up to the firm level.

The defining core is this loop itself. A PSA sits between a time-tracking tool and a full ERP: it is far more than hour capture, because hours are bound to billable projects, priced, approved, invoiced, and measured; and in its pure-play form it is less than an ERP, because it feeds the general ledger rather than owning it. When a product adds general-ledger accounting it becomes a project-based ERP; when it drops billing conversion and utilization economics it becomes a project management or time-tracking tool.

## Users & Context

The organization running a PSA sells the time and expertise of its people, delivered as projects for clients. Its economics are unusual: the "product" is billable hours and expenses, capacity is the constraint, and margin erodes quietly when work is under-scoped, staffed badly, recorded late, or billed late. The PSA exists to make that loop visible and controlled.

Primary users:

- **Consultant / delivery professional** — logs time and expenses against assigned projects, works tasks, sees assignments and utilization.
- **Project / delivery manager** — owns a project's budget versus actuals, requests and manages staff, tracks scope and project health, prepares billing.
- **Resource manager** — matches demand for roles and skills against available capacity, balances workloads, watches the bench and future hiring needs.

Secondary users:

- **Finance / billing staff** — maintain rate cards, review and approve invoices, handle revenue recognition, accounts receivable, and the handoff to the accounting system.
- **Executive / firm leadership** — watches utilization, margin, and the pipeline-to-delivery revenue forecast across the firm.
- **Administrator** — configures rates, approval workflows, permissions, and integrations.

## Core Model

The system is organized around one closed financial loop:

```text
Opportunity / Estimate / Quote
  ↓ won, scoped
Client  ←──  Project / Engagement  (budget · dates · billing arrangement · team)
                ↓ staffed via
        Demand → Assignment  (of Resources)
                ↓ delivery recorded as
        Time entries + Expense entries  (billable / non-billable)
                ↓ approval gate
        Rate application → Invoice → Payment / A/R
                ↓ measured as
        Budget vs Actual · Utilization · Margin  → firm-level roll-up
```

**Project / engagement.** The central object. A bounded body of client work carrying a budget, a timeline, a billing arrangement, a team, and its own financial record. Everything else in the system either feeds it (estimates, assignments, time, expenses) or is derived from it (invoices, profitability).

**Resource.** A staff member modeled as capacity-bearing: a contract with contracted hours, a cost rate to the firm, a bill rate to clients, skills and seniority, and time off. Capacity (contracted hours minus approved absences) is the base for availability and utilization calculations.

**Demand and assignment.** A project needs certain roles and skills for certain periods — a demand. Staffing links a resource to that demand as an assignment, which typically moves through planned states (draft, reserved) to active work. Scheduling checks assignments against capacity and flags overbooking.

**Time and expense entries.** The raw record of delivery. Each entry names the project (and usually a task or work item), the person, the date, hours or amount, and whether it is billable. Entries pass through an approval gate — submit, review, approve, often at multiple levels — before they may be billed.

**Rate card.** The pricing machinery: bill rates and cost rates defined at staffer, role, project, or client level, with custom and locked rates for negotiated arrangements. Rates resolve what an approved hour is worth on the invoice and what it cost the firm.

**Invoice.** Approved billable time and expenses are gathered into draft invoices, reviewed and approved, sent, and tracked to payment. Work performed but not yet invoiced is held as unbilled work-in-progress. Fixed-fee and milestone arrangements are recognized as revenue on a schedule rather than per hour.

**Project financials.** Budget versus actual (hours and money), estimated cost to complete, billable utilization, and margin per project — aggregated to client, department, and firm level.

**Standard capabilities** that mature products add around this loop: opportunity/estimate stages that convert into projects; skills search and staffing recommendations; timesheet timers and daily/weekly views with mobile entry; expense types with receipts and subcontractor/vendor expenses; invoice templates and multi-currency billing; client portals and online payments; revenue recognition; period-close support; reporting on utilization, realization, and margin; integrations with CRM upstream and accounting/GL downstream; and AI assistance for staffing, estimation, and insight.

**Optional capabilities** that depend on segment and scale: task boards and Gantt scheduling inside the product; multi-entity and multi-currency operation; industry compliance packs (for example government-contractor timekeeping rules); internal chargeback for services divisions whose "client" is another department.

## How It Works

### 1. Win and scope

```text
Opportunity (from the PSA's own pipeline or a connected CRM)
→ estimate the work by role and effort, priced from rate cards
→ quote / statement of work approved
→ project created with budget, scope, timeline, and billing arrangement intact
```

The point of this stage is that what was sold becomes the baseline the delivery team is held to: the project starts with the sold budget and staffing plan rather than a blank slate.

### 2. Staff the project

```text
Project defines demand (roles, skills, hours, dates)
→ resource manager searches by skills / availability / seniority
→ assignment created (planned → reserved → active)
→ overbooking and bench impact checked against capacity
```

Staffing decisions are made with the financial consequences visible — how an assignment affects utilization, project cost, and margin.

### 3. Deliver and record

```text
Consultants work tasks on assigned projects
→ log time (timers, daily or weekly timesheets, mobile) and expenses
→ mark entries billable or non-billable
→ submit → manager review → approval (single or multi-level)
```

Approved entries become the firm's record of work performed. Unapproved or unsubmitted time is the classic leak: work delivered but never billed.

### 4. Bill

```text
Approved billable time + expenses
→ priced via rate cards and billing rules
→ draft invoice → review / approval → sent
→ payment recorded → accounts receivable tracked
→ fixed-fee work recognized as revenue on its own schedule
```

Invoicing is typically periodic and batched; unbilled work-in-progress is tracked so that nothing delivered goes missing between delivery and billing.

### 5. Measure and close

```text
Budget vs actual (hours and money) per project
→ utilization (billable hours ÷ capacity) per person and firm
→ margin per project, client, service, department
→ period close → summary handed to the accounting system / general ledger
```

The loop closes back at the start: delivery data sharpens the next round of estimates, capacity plans, and revenue forecasts.

## Interfaces

- **Resource planner / scheduler** — the staffing cockpit: people and projects on a shared timeline, capacity and availability heatmaps, assignment states, overbooking alerts. Primary actions: create and adjust assignments, search by skill, compare staffing scenarios.
- **Project workspace** — one project's budget, tasks, team, time and expense records, financials, and health indicators. Primary actions: plan tasks, request staff, track budget burn, prepare billing.
- **Timesheet** — the consultant's daily or weekly entry surface with timers, project/task pickers, and billable flags, plus submission state. Primary actions: enter time, submit, correct rejected entries.
- **Expense entry** — capture of expenses with type, receipt, project attribution, and currency; includes vendor and subcontractor expenses in mature products.
- **Invoice workspace** — draft invoice assembly from approved work, review and approval routing, templates, sending, and an accounts-receivable view of what is outstanding and what remains unbilled.
- **Dashboards and reports** — utilization, margin, budget variance, pipeline-to-delivery revenue forecasts, at project, client, team, and firm level.
- **Administration** — rate cards, approval workflows, permission models, custom fields, integrations.
- **Client portal (optional)** — clients view and pay invoices online.
- **Mobile app** — time, expense, and approval on the go.

## Important Rules / Behaviors

- **Billable versus non-billable is the master distinction.** It decides whether recorded work ever reaches a client invoice, and it feeds utilization. Writing off time is a deliberate, attributed act.
- **Approval gates precede billing.** Time and expenses must be approved before they can be invoiced; invoices themselves commonly pass a review/approval step before sending. Multi-level approval exists in larger firms.
- **Capacity constrains assignments.** Scheduling checks planned work against contracted capacity minus approved absences; overbooking is surfaced as an alert, and utilization is computed from the same capacity base.
- **Rates resolve at multiple levels.** Bill and cost rates can be defined per staffer, role, project, or client; negotiated custom or locked rates override defaults. The exact precedence rules vary by product.
- **Closed periods freeze history.** Once a period is closed for accounting, retroactive edits to time, expenses, or invoices are restricted or require a controlled correction — this is what makes the PSA's numbers trustworthy to finance.
- **Unbilled work is a tracked state, not a gap.** Work performed but not yet invoiced is held as work-in-progress and reconciled at billing time.
- **Billing arrangement shapes revenue.** Time-and-materials work bills from recorded hours; fixed-fee and milestone work recognizes revenue on progress or schedule — the same delivery record feeds different revenue logic.
- **Cost and margin data are permission-sensitive.** Delivery staff typically see their assignments and utilization; cost rates, cost rates of others, and firm margins are restricted to managers, finance, and executives.
- **The general ledger stays downstream.** A pure-play PSA summarizes and syncs to the accounting system; it does not replace it. Products that include the ledger are project-based ERPs — a different packaging of the same delivery loop.

## Variants

- **Pure-play PSA** — standalone platform covering the full loop, GL delegated to an accounting system; typical for mid-market firms.
- **ERP-embedded PSA** — the delivery loop inside a project-based ERP that also owns the ledger; typical for architecture & engineering and government-contracting firms with heavy accounting needs.
- **Platform-native PSA** — the loop built on a business platform (for example a CRM platform), sharing customer records and extending from sale through delivery to customer success; typical for enterprise IT and software companies' services arms.
- **Work-management-flavored PSA** — lighter, usability-first products where task management and collaboration are first-class alongside the financial loop; typical for agencies and small consultancies.
- **Industry tunings** — agency (retainers, creative scopes), IT services (dev-tool time import), management consulting, A&E (phase-based plans, progress billing), accounting firms, government contracting (compliant timekeeping and audit trails).
- **Billing model mixes** — time-and-materials, fixed fee, milestone, retainer, and value-based arrangements, often combined within one firm.
- **Scale variants** — multi-entity, multi-currency, multi-office deployments at enterprise tier; single-entity simplicity at SMB tier.
- **Internal services variant** — the same loop with internal chargeback instead of external clients.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Project Management Application | overlapping module | manages tasks, schedules, and teams for work execution; lacks billable economics — no rate-based invoicing, no utilization/margin measurement |
| Time Tracking Application | component | captures hours; does not bind them to billable projects, resolve rates, gate approvals into invoicing, or compute billable utilization |
| Workforce Management Platform | adjacent | schedules shift-based workforces for labor coverage and compliance; object is the shift, economics are labor cost — not client-billable delivery |
| ERP | downstream / packaging variant | owns the general ledger and financial back office; a project-based ERP embeds the PSA loop plus ledger accounting, while a pure-play PSA syncs to the ledger |
| CRM | upstream | manages the sales pipeline to the won deal; the PSA picks up around the win and manages delivery; some PSAs include light pipeline management as a variant |
| Agency Management System | industry-shaped analog | same delivery-billing loop tuned to creative/retainer agency practice; heavy overlap, different vertical emphasis |
| Legal Practice Management System | industry-shaped analog | matter-centric delivery and billing with legal-specific rules; the same loop in a regulated vertical form |
| Proposal / CPQ tools | front-end module | estimation and quoting feed the PSA's projects but are not the Type |
| Billing Platform / Invoicing Application | component | generic invoice issuance; lacks the project-resource-approval substrate that determines what is billable |
| Expense Management Platform | component | expense capture and reimbursement; inside a PSA expenses are additionally project-billable |
| Enterprise Resource Scheduling Platform | adjacent | books shared resources (rooms, equipment, people) against time slots; no billable project economics |

The sharpest seam is with Project Management: every PSA contains project management, but a project management tool without billing conversion and utilization economics is not a PSA. The second is with ERP: the question "does this system hold the general ledger?" separates pure-play PSA from project-based ERP.

## Representative Products

- **Kantata** — pure-play, resource- and finance-centric PSA for mid-market and enterprise services firms
- **Certinia (Professional Services Cloud)** — Salesforce-platform-native PSA with modular financial management, enterprise-focused
- **Deltek Vantagepoint / Deltek Polaris** — project-based ERP for A&E and consulting (Vantagepoint) alongside a pure PSA application (Polaris); vertical market leader
- **Scoro** — work-management-flavored PSA for agencies and consultancies, SMB/mid-market
- **BigTime** — mid-market, finance-first PSA with native accounting-system integration; enterprise tier for multi-entity firms

## Sources

Research date: **2026-09-06**

- BigTime Help Center (knowledge base): https://help.bigtime.net/ — categories for Project & Staff Management, Time & Expense, Invoicing & Payments, Resource Management, Quotes; Resource Management Glossary: https://help.bigtime.net/hc/en-us/articles/29712335376535
- BigTime product site: https://www.bigtime.net/
- Certinia Technical Pack (public object/API reference): https://help.financialforce.com/TechnicalReference/2026.2/Default.htm ; developer portal: https://developer.certinia.com/
- Certinia product site: https://certinia.com/ , https://certinia.com/solutions/professional-services-cloud/
- Kantata product site: https://www.kantata.com/ , https://www.kantata.com/psa/resource-management-software , https://www.kantata.com/psa/financial-management-software
- Deltek Vantagepoint product page: https://www.deltek.com/en/products/deltek-vantagepoint (plus Deltek Polaris product listing)
- Scoro product site: https://www.scoro.com/

> Sourcing limitations: the Kantata knowledge base redirects to a customer login, the Scoro help center was unreachable from the research environment, and Deltek's operational documentation sits behind a support-center login. Operational detail for those products is therefore calibrated to their official product pages, and no precise numeric defaults, state-name sets, or billing-method menus are asserted for them. BigTime and Certinia provided directly observable operational documentation; cross-product claims rest on the observed common structure across all five products.

Detailed product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
