# Research Notes — Professional Services Automation / PSA

Research date: 2026-09-06
Slug: professional-services-automation-psa
Directory leaf: Professional Services Automation / PSA (§10 Enterprise Operations & Administration)

---

## Research Goal

Understand what a Professional Services Automation (PSA) application actually is from real products: its central objects, the loop that defines it, who uses it, how work flows from winning a deal to billing it, and where its boundaries lie against Project Management, Time Tracking, Workforce Management, ERP, and CRM.

## Initial Boundary (hypothesis before research)

- PSA = the delivery-side operating system of a project-based services firm (consulting, IT services, agencies, A&E, accounting, and internal services divisions).
- Core hypothesis: the defining loop is **client-billable project + staffed resources + time/expense capture + billing conversion + project-level financials**.
- Nearest neighbors: Project Management Application, Time Tracking Application, Workforce Management Platform, ERP, CRM, Agency Management, Legal Practice Management.
- Unknowns: exact object models per product (project vs engagement), role of opportunity/pipeline, billing machinery specifics, utilization/realization metrics, ERP-embedded variants.

## Research Questions

1. What are the central objects (project/engagement/opportunity/resource/assignment/timesheet/invoice)?
2. How does work enter the system — native opportunity/quote, or CRM import?
3. What does resource management look like: capacity model, skills, assignment states, overbooking?
4. What lifecycle does time/expense go through (draft → submit → approve → bill)?
5. How does recorded work convert to billing: rate cards, billing methods, invoice states?
6. What financial measurement exists: utilization, realization, margin, revenue recognition, period close?
7. What roles exist and which interfaces does each use?
8. Is task/schedule management part of the core, or a linked module?
9. What variants exist (agency / IT services / consulting / A&E / govcon; pure-play vs ERP-embedded vs platform-native)?
10. Where are the boundaries vs Project Management, Time Tracking, Workforce Management, ERP, CRM?

## Representative Products

| Product | Positioning | Customer tier | Philosophy | Evidence tier reached |
|---|---|---|---|---|
| Kantata (OX/SX) | Pure-play AI-era PSA; mid-market + enterprise | Mid-market/enterprise | Resource-and-finance-centric pure play | Tier 2 (product pages); help center login-gated |
| Certinia (PS Cloud, ex-FinancialForce) | Salesforce-platform-native PSA + Financial Management Cloud | Enterprise | Platform-native, modular (PSA / FM / CS clouds) | Tier 1 (public Technical Pack) + Tier 2 |
| Deltek Vantagepoint (+ Polaris) | Project-based ERP for A&E/consulting; Polaris = pure PSA | A&E, consulting, GovCon verticals | Vertical ERP with PSA modules; front-office/back-office split | Tier 2 |
| Scoro | All-in-one work management positioned as PSA | SMB/mid-market agencies & consultancies | Work-management-first PSA with financial depth | Tier 2 (help center unreachable ×2) |
| BigTime (+ BigTime Enterprise) | Mid-market PSA, "more than a time tracker, less than an ERP" | SMB/mid-market | Finance-first, GL-delegating (QuickBooks-native) | Tier 1 (KB categories + RM glossary + invoicing + time/expense categories) + Tier 2 |

Selection rationale: market representativeness (pure-play, platform-native, vertical ERP, work-management, mid-market billing-centric), different product philosophies, different customer tiers, and best-available documentation.

## Sources

Tier 1 (official operational documentation):

- BigTime Help Center — https://help.bigtime.net/ (categories: Setup & Account Management; Project & Staff Management; Time & Expense; Invoicing & Payments; Analytics; Resource Management; Quotes; AI)
- BigTime Resource Management Glossary — https://help.bigtime.net/hc/en-us/articles/29712335376535
- BigTime Invoicing & Payments category — https://help.bigtime.net/hc/en-us/categories/9780779768471
- BigTime Time & Expense category — https://help.bigtime.net/hc/en-us/categories/9780778897815
- Certinia Technical Pack (public developer/object reference) — https://help.financialforce.com/TechnicalReference/2026.2/Default.htm
- Certinia developer portal — https://developer.certinia.com/

Tier 2 (official product pages):

- Kantata — https://www.kantata.com/ , /psa/resource-management-software , /psa/financial-management-software
- Certinia — https://certinia.com/ , /solutions/professional-services-cloud/
- Deltek Vantagepoint — https://www.deltek.com/en/products/deltek-vantagepoint (plus Deltek Polaris product listing)
- Scoro — https://www.scoro.com/ (module pages: work/task mgmt, project mgmt, time & cost tracking, resource planning, CRM & pipeline, estimating & budgeting, bill & expense mgmt, invoicing)
- BigTime — https://www.bigtime.net/

Source-access limitations:

- Kantata knowledge base (help.mavenlink.com) redirects to Kantata OX login — operational detail not reachable; Kantata evidence is Tier 2 only.
- Scoro help center (support.scoro.com) failed twice with transport errors — abandoned per network rules; Scoro evidence is Tier 2 only.
- Two BigTime KB articles (Invoicing overview; main Glossary) returned 403 — category-level structure used instead; no retry per network rules.
- Deltek Vantagepoint operational docs sit behind the Deltek Support Center login — Tier 2 only.

Consequence: precise numeric defaults, exact state-name sets, and per-product billing-method menus are NOT asserted in the final document; claims are calibrated to category/structure-level evidence.

---

## Product A — Kantata (OX / SX)

### Key observations (Tier 2, evidence layer A)

- Positions itself as "Professional Services Automation Platform" for agencies and professional services firms; mid-market + enterprise (IDC MarketScape AI-Enabled PSA leader claim).
- Platform pillars on product pages: **Resource Management & Forecasting**, **Financial Management**, **Project Management**, **Integrations & MCP connectivity**, plus an AI layer ("Expertise Engine", "Expertise Agent", "Agentic BI").
- Resource management page: resource forecasting / capacity planning ("plan for resource demand in your project pipeline"), resource allocation / scheduling (best-fit matches, evaluate multiple resource plans, see profit impact of allocation decisions), skills inventory (skill-based staffing, skill gaps), talent network (external partners/contractors with skills, calendars, cost rates, availability).
- Financial management page: **project accounting**, **period close**, **invoicing**, **revenue recognition and forecasting**; guardrails preventing time-entry/expense-submission errors; configurable invoice formats; DSO reduction; margin monitoring.
- FAQ (vendor-authored): "PSA platforms connect delivery, resources, and financials… linking actuals, forecasts, capacity, and billing data"; needed financial features listed as project accounting, time and expense tracking, rate management, revenue recognition, invoicing, BI dashboards.
- Industries: software & hi-tech, management consulting, agencies, IT services.
- Help center login-gated → no operational article-level evidence.

## Product B — Certinia (PS Cloud)

### Key observations (Tier 1 Technical Pack + Tier 2, evidence layers A/B)

- Salesforce-platform-native; suite split into **Professional Services Cloud**, **Financial Management Cloud**, **Customer Success Cloud**, plus **Veda AI**.
- Lifecycle framing on product pages: **SELL → STAFF → DELIVER → BILL → RENEW**; "connects how you sell, staff, deliver, bill, and renew on a single platform".
- PS Cloud module cards: **services estimation**, **resource management**, **project management**, **services billing**, **services financials**.
- Technical Pack (public object/API reference) confirms the PSA product family as separately packaged modules with their own object models and permission sets:
  - Professional Services Automation (+ PSA Core, PSA Workspaces)
  - Services Estimator (+ Salesforce CPQ connector, RLM connector)
  - Revenue Management
  - Billing Central (+ workspaces)
  - Accounting (+ Accounting Workspaces)
  - Business Analytics
  - Customer Success Cloud (+ PSA Connector)
  - PSA Direct for Jira, PSA Direct for Concur Expense (external time/expense sources)
  - PSA–Accounting Connector (PSA ↔ GL handoff)
- Developer articles evidence the opportunity→project conversion path ("Create Project from Template API — Opportunity Product Automation").
- Marketing metrics (L3, not canonical): 1,400+ customers; claims of reduced time-to-staff, reduced unbilled time.

## Product C — Deltek Vantagepoint (+ Polaris)

### Key observations (Tier 2, evidence layer A)

- Vantagepoint positioned as **ERP** "built for architecture, engineering, and consulting firms" — "connecting projects, pipeline, people, and financials together in one unified system built for the full project lifecycle".
- Feature set: CRM & Pipeline Intelligence, Resource Management, Project Planning & Delivery (Gantt, project KPIs), Financial Management & Billing (timesheets, expenses, billing/invoicing automation), AI orchestrator ("Dela"), automated workflows & approvals.
- Capability pages: Accounting & Financial Management; CRM & Pipeline Management; Project Management; Resource Management; Payments.
- **Front Office only** deployment option: "connects your pipeline, people, and projects while integrating with your existing financial system" — explicit front-office/back-office split.
- Deltek product taxonomy places **Polaris** under "Resource Intelligence": "an intelligent PSA application that unifies people, projects, time, skills, billing, and revenue recognition" — i.e., Deltek itself distinguishes PSA (Polaris) from project-based ERP (Vantagepoint/Costpoint/Maconomy).
- FAQ: users are executives, project managers, accountants, resource planners, business development staff; purposes: win work, plan utilization, deliver profitably, close the month, analyze performance.
- Vertical context: A&E (98% of Top 500 A&E firms claim), consulting, GovCon (Costpoint for GovCon; DCAA compliance culture).

## Product D — Scoro

### Key observations (Tier 2, evidence layer A)

- Positions itself as "AI-powered Professional Services Automation": "One platform for projects, resourcing, and finances"; industries: consultancy, agency, architecture, engineering & construction, software dev, IT services, events.
- Module taxonomy (product nav):
  - Work: **Work & Task Management**, **Project Management**, **Time & Cost Tracking**, **Resource & Capacity Planning**
  - Sales & Finance: **CRM & Pipeline Management**, **Estimating & Budgeting**, **Bill & Expense Management**, **Client Billing (Invoicing)**
- Stated differentiators: quote estimation matrix (deliverables broken down by role and effort with cost/margin visibility), thorough project financials (budget burn, real-time profitability forecast at role/service/project level, internal + external costs), ease of use.
- Roles: executive, operations manager, project manager, financial manager, team member.
- Integrations: accounting systems (Xero, QuickBooks, Sage Intacct, Exact Online), payments (Stripe), expense (Expensify, Envoice), dev (Jira), calendars, CRM (Salesforce, HubSpot), SSO/SCIM (Okta, Azure AD).
- Granular user permissions; API; MCP server.
- Help center unreachable (2× transport error) → no operational article-level evidence.

## Product E — BigTime (+ BigTime Enterprise)

### Key observations (Tier 1 KB + Tier 2, evidence layers A/B)

- Positioning (marketing, but structurally informative): "Trusted by 3,000+ professional services firms that needed **more than a time tracker and less than an ERP**"; "One PSA Platform, Quote To Cash, **Built Around Your GL**"; "WIP accounting syncs straight to your GL"; "One-click invoicing from project data".
- Module set: **Scoping & Quoting** (services CPQ: margin-informed quote builder, live rate cards, auto-generated SOWs, one-click quote→project conversion), **Time & Expense Tracking**, **Resource Management**, **Project Portfolio Management**, **Invoicing & Payments**, **Reporting & Analytics**; BigTime Enterprise adds multi-entity, multi-currency, BI.
- KB top-level categories (Tier 1): Setup & Account Management; Project & Staff Management; Time & Expense; Invoicing & Payments; Analytics; BigTime Mobile; Integrations; BigTime Resource Management; BigTime Quotes; BigTime AI.
- Resource Management Glossary (Tier 1) — canonical vocabulary:
  - **Staffer / staff member** with a **Contract** (contract capacity, cost rate, contract period, optional default bill/cost rates)
  - **Demand** (requirement for resources) with states fully scheduled / partially scheduled; **Assignment** (planned work assigned to a staffer) with statuses Active / Reserved / Draft
  - **Capacity** = contract capacity − approved time off (incl. public holidays); base for availability and utilization
  - **Contract utilization** = logged billable hours ÷ contract capacity; scheduled utilization configurable
  - **Billable / non-billable** time; average bill rate / average cost rate per project
  - **Overbooking** detection (scheduled hours exceed available capacity) with configurable settings
  - **Time off** with statuses (pending, retracted, accepted, rejected, in progress); full-day vs partial
  - **Skills / skills tree / seniority** for matching; **FTE** planning unit
  - **Cost centers** (3 levels) for profitability analysis; **Actuals** (current work, costs, profit, margins per project)
  - **Task** with firm-customizable lexicon (task/phase/work item/milestone/budget item); Task Editor with assignments, hours, due dates
  - Roles: staffer, manager, administrator; project manager (+ read-only); finance manager
- Invoicing & Payments category (Tier 1):
  - **Invoice Creation** (draft invoices, editing, invoice templates, A/R dashboard)
  - **Invoice Review & Approval** (approval/rejection statuses, multi-step "leapfrog" approvals)
  - **Billing Rates** (rate cards, custom billing rates, locked billing rates, staff-level billing rates)
  - **Payments** (manual + automatic payments, autopay enrollment, client portal, AR dashboards, deposit batching)
  - **Multi-currency invoicing** (base currency, currency list, linking currency to the accounting system)
- Time & Expense category (Tier 1):
  - **Tracking Time** (timers, daily/weekly timesheet views, timesheet customization)
  - **Tracking Expenses** (expense types, expense workflow, expense rate cards)
  - **Reviews & Approvals** (timesheet review and approval, multi-level approvals, bulk approve, approval history)
  - **DCAA compliance** (timekeeping compliance, audit trail reporting — GovCon variant)
  - **Multi-currency expenses**; **Vendor expenses and billing** (vendor bills for time, posted to QuickBooks — subcontractor cost flow)
- GL delegation: native QuickBooks Desktop + Online integration (~75% of customers per marketing); accounting sync is the financial back office.

---

## Cross-product Comparison

| Dimension | Kantata | Certinia | Deltek Vantagepoint/Polaris | Scoro | BigTime |
|---|---|---|---|---|---|
| Central work object | Project/engagement | Project (Salesforce-native) | Project (WBS/phase-oriented) | Project | Project |
| Work intake | Pipeline-linked resourcing; CRM integration | Opportunity → estimate → project (CPQ connector; template API) | CRM & pipeline module (native) | CRM & pipeline module (native) | Quote/SOW → one-click project conversion |
| Resource mgmt | Forecasting/capacity, allocation/scheduling, skills, external talent network | Resource mgmt module + Veda staffing agents | Resource mgmt module (utilization views, skills search) | Resource & capacity planning | Demand/assignment model, capacity, skills tree, overbooking |
| Time & expense | Time & expense tracking (guardrails) | Timecards; Jira/Concur connectors | Timesheets & expenses (AI-assisted) | Time & cost tracking; bill & expense mgmt | Timers, daily/weekly timesheets, expense types, vendor expenses |
| Approval gates | Submission guardrails | Approval workflows | Automated workflows & approvals | Approval flows | Timesheet review/approval (multi-level), invoice review/approval |
| Billing | Invoicing module, configurable formats | Services billing + Billing Central | Financial mgmt & billing | Client billing/invoicing | Draft invoice → review/approve → send; rate cards; payments/client portal |
| Revenue recognition | Revenue recognition & forecasting module | Revenue Management module | Revenue recognition (Polaris claim) | Rev rec discussed in finance content | WIP accounting (GL sync) |
| Project financials | Project accounting, period close | Services financials | Accounting & financial mgmt | Budget burn, profitability at role/service/project | Budget vs actuals, cost centers, actuals |
| GL ownership | No (integrations) | Optional (Accounting module in suite) | Yes (it is an ERP) | No (Xero/QB/Sage sync) | No (QuickBooks sync) |
| Utilization economics | Yes (bench, utilization) | Yes | Yes (utilization gaps) | Yes (utilization rate) | Yes (contract utilization) |
| AI layer | Expertise Engine/Agent, agentic BI | Veda agents (estimation/resourcing/delivery/CS) | Dela orchestrator | ELI | AVA, Expense/Resourcing/Insights agents |
| Deployment | SaaS (OX); Salesforce (SX) | Salesforce-native | Cloud ERP (Deltek Cloud) or front-office-only | SaaS | SaaS; Enterprise tier multi-entity/multi-currency |
| Segments | Consulting, IT, agencies, software | Consulting, IT services, software, tax & audit | A&E, consulting, GovCon | Consultancy, agency, A&E, IT, events | Accounting, architecture, consulting, engineering, IT services |

### Stable cross-product commonalities (evidence layer B)

1. Client project/engagement as the central financial object.
2. Staff modeled as capacity-bearing resources with skills and rates.
3. Demand → assignment staffing model with capacity/overbooking awareness.
4. Time & expense captured against projects through an approval gate.
5. Rate cards (bill + cost rates) resolving what recorded time is worth.
6. Approved work converted into client invoices with review/approval states.
7. Project-level economics: budget vs actual, utilization, margin/profitability; firm-level roll-up.
8. Pipeline/opportunity stage feeding projects (native or via CRM/CPQ).
9. Role segmentation: delivery staff, project manager, resource manager, finance, executive, admin.
10. Integration posture: CRM upstream, accounting/GL downstream, HRIS/payroll, calendars, dev/expense tools.
11. AI assistance layer (2025–2026 era): staffing/estimation/insight agents.

### Where products differ (variant space)

- GL ownership (delegated vs included vs ERP-native).
- Platform substrate (standalone SaaS vs Salesforce-native vs ERP suite).
- Work-management depth (task boards/Gantt as first-class vs link-out).
- Industry tuning (agency creative vs A&E phase/WBS vs GovCon DCAA).
- Billing model emphasis (T&M vs fixed fee vs retainer vs value-based).
- Client-facing surfaces (client portal, payments).
- Scale features (multi-entity, multi-currency).

---

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant

The smallest structure without which the product stops being a PSA:

```text
Client-billable project/engagement (unit of client work carrying budget & financials)
  + staff modeled as capacity-bearing resources (skills, cost/bill rates) assigned to it
  + time & expense recorded against it through an approval gate
  + approved work converted into client billing (via rates/billing rules)
  + project-level financial measurement (budget vs actual, utilization, margin)
```

Tests:
- Remove the client-billable project → generic project management.
- Remove resources/capacity → task management.
- Remove time/expense capture → generic billing/invoicing.
- Remove billing conversion → resource planning / timesheet tool.
- Remove project financials → time tracking application.

All five links are needed; the Type IS the closed loop.

Historical check: 2000s-era PSAs (OpenAir, Tenrox), agency job-costing systems, Deltek Vision, QuickBooks-coupled timesheet-billing tools all satisfy this loop without AI, client portals, or platform-native architecture → L0 is not over-fitted to the current market.

### L1 — Common Mature Structure

- Opportunity/estimate/quote stage feeding projects (SOW generation; quote→project conversion)
- Resource management machinery: demand, assignment states (draft/reserved/active), skills/seniority matching, overbooking alerts, time off, FTE, scheduled vs actual utilization
- Rate cards: bill rates and cost rates at staff/project/role level; custom and locked rates
- Timesheet lifecycle: entry (timers, daily/weekly views, mobile) → submit → review/approve (multi-level) → locked for billing
- Expense tracking: types, receipts, expense rate cards, vendor/subcontractor expenses
- Invoice machinery: draft → review/approval → send; templates; multi-currency; WIP/unbilled tracking; AR dashboards; payments/client portal
- Revenue recognition (fixed-fee/milestone methods)
- Project accounting: budget vs actual, cost to complete, period-close support
- Reporting/analytics: utilization, realization, margin, pipeline-to-delivery forecasting
- Role model: staffer/consultant, project manager, resource manager, finance/billing, executive, admin
- Integration set: CRM, accounting/GL, HRIS/payroll, calendars, dev tools (Jira), expense tools
- AI assistance: staffing/estimation/insight agents

### L2 — Variant / Optional Structure

- Packaging pole: pure-play standalone vs ERP-embedded (Vantagepoint, Costpoint, Maconomy) vs platform-native (Certinia on Salesforce) vs work-management-flavored (Scoro)
- GL posture: delegate to accounting system (BigTime, Scoro) vs include accounting (Certinia FM Cloud) vs ERP-native GL (Vantagepoint)
- Industry tuning: agency (creative briefs, retainers), IT services, management consulting, A&E (phase/WBS, progress billing), accounting, GovCon (DCAA timekeeping compliance)
- Billing model mix: T&M, fixed fee, milestone, retainer, value/outcome-based
- Client-facing surfaces: client portal, autopay/online payments
- Enterprise scale: multi-entity, multi-currency, multi-office
- Internal chargeback (services divisions billing internal "clients")
- Front-office-only deployment (Vantagepoint) — PSA layer over an existing GL

### L3 — Vendor-specific (research notes only)

- Kantata: OX/SX product split (Mavenlink/Kimble lineage), Expertise Engine™, Sentiment Analysis, MCP connectivity
- Certinia: Veda AI agents (Estimation/Resourcing/Service Delivery/Customer Success), Foundations module, Asperato connector, Lockbox
- Deltek: Dela AI orchestrator, GovWin IQ, ProPricer, Polaris naming, Clarity benchmark reports
- BigTime: AVA/Expense Agent/Resourcing Agent/Insights Agent, BigTime Payments, "Foresight" RM module naming, Lexicon term customization, "three moments of margin erosion" framing, Projector lineage (Enterprise)
- Scoro: ELI AI companion, quote estimation matrix, business maturity quiz
- Marketing metrics (33% on-time delivery, 30% time-to-staff, DSO figures, etc.) — vendor claims, not canonical.

---

## Vendor-specific Findings

See L3 above. None of these belong in the canonical document except as illustrative examples.

## Boundary Findings

1. **vs Project Management Application** — sharpest seam. PM manages work execution (tasks, schedules, teams); PSA adds the resource-capacity economy (billability, rates, utilization) and client billing. Evidence: every sampled PSA includes project management as a module, but PM tools (e.g., generic work management) lack billing conversion and utilization economics. Test: if the system cannot turn approved time into a client invoice and compute billable utilization, it is not a PSA.
2. **vs Time Tracking Application** — time tracking captures hours; PSA binds hours to billable projects, resolves rates, gates through approval, and converts to invoices. Time tracking is a component of PSA, not the Type.
3. **vs Workforce Management Platform** — WFM schedules hourly/shift workforces (labor compliance, coverage); PSA staffs billable professional work (client revenue). Different object (shift vs assignment), different economics (labor cost vs billable revenue). Overlap only in scheduling UI metaphors.
4. **vs ERP** — ERP owns the general ledger and financial back office; PSA owns delivery economics. Pure-play PSAs sync to the GL (BigTime→QuickBooks; Scoro→Xero/QB/Sage; Certinia PSA→Accounting connector). Project-based ERPs (Vantagepoint, Maconomy, Costpoint) embed PSA-like modules plus GL. Test: does the system hold the general ledger? Vantagepoint's own "Front Office only" mode and Deltek's Polaris-vs-Vantagepoint split confirm the industry treats these as distinct layers.
5. **vs CRM** — CRM manages the sales pipeline to closed deals; PSA picks up around the won deal (opportunity → engagement) and manages delivery. Some PSAs include light CRM/pipeline (Scoro, Vantagepoint) — variant, not core.
6. **vs Agency Management System / vertical practice-management systems** — agency management (creative/retainer world) and legal practice management (matter-centric billing) are industry-shaped analogs of the same loop. The directory treats them as separate leaves; PSA here is documented as the horizontal Type. Flagged as potential overlap for joint review if those leaves are processed.
7. **vs Services CPQ / Proposal Management** — quoting/estimation is a front-end module (BigTime Quotes, Certinia Services Estimator), not the Type.
8. **vs Enterprise Resource Scheduling Platform** — resource scheduling in PSA is bound to billable project economics; generic resource scheduling (rooms/equipment/people bookings) has no billing conversion.

## Uncertainties

- Exact timesheet/invoice state-name sets per product (only BigTime's approval structure directly observed at category level; others inferred from module structure).
- WIP accounting mechanics (BigTime marketing asserts "WIP syncs to GL"; KB article unreachable) — kept qualitative.
- Revenue recognition method menus per product — module existence confirmed (Kantata, Certinia, Polaris claim), methods not verified.
- Kantata, Scoro, Deltek operational detail is Tier 2 only (login-gated or unreachable help centers).
- Whether "realization" is a standard metric across products — industry-standard term, but only indirectly evidenced in this sample; kept out of strong claims.
- Degree of task-management depth inside PSAs varies (Scoro/BigTime include task boards; others link out to Jira etc.) — documented as variant.

## Final Synthesis

A PSA is the delivery-side operating system of a project-based services business. Its defining structure is a closed financial loop: client-billable projects staffed by capacity-bearing resources, whose recorded time and expenses pass an approval gate and are converted — through rate cards and billing rules — into client invoices, while budget-vs-actual, utilization, and margin are measured per project and rolled up to the firm. Everything else (quoting, CRM, task boards, client portals, AI agents, GL accounting) is common mature structure, variant packaging, or vendor detail. The Type's sharpest boundaries: against Project Management (no billing economics), Time Tracking (no resource-billing loop), Workforce Management (shift labor vs billable professional work), and ERP (GL ownership).
