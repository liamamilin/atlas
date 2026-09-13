# Home Improvement Contractor Management

## Overview

A **Home Improvement Contractor Management** application is the business system of record for a contractor that sells and produces improvement work in customers' homes — remodelers, design-build firms, and general contractors serving homeowners. It carries each customer from first inquiry through a managed sale, holds the sold work as a durable job at the home, organizes the work as a multi-step production plan executed over days or weeks, and resolves money across the job's life: a deposit when the sale is made, further payments as work progresses, a final balance at completion.

The defining core is small:

```text
Homeowner customer carried through a managed sale
└── Improvement job of record at the home
    └── Production plan (sequenced steps/phases, crews, work orders)
        └── Money across the job's life (deposit → progress → final)
```

Everything else commonly associated with this software — financing offers, e-signature contracts, lead-generation campaigns, warranty tracking, production dashboards — is widespread in current products but is not what makes the system what it is. A paper-era remodeling contractor running an inquiry card file, a written proposal, a signed contract with a deposit, and a whiteboard production schedule satisfies the same core.

The Type sits between two neighbors. It is heavier than small-business field service (the unit of work is a project, not a dispatched visit) and lighter than construction project management (it runs one contractor's business, not a multi-organization construction program). When the center of gravity shifts to multi-party contractual coordination, the product is drifting toward Construction Project Management; when it shifts to same-day service calls, toward Field Service Management.

## Users & Context

The business being run is a consumer-sale project business: work is sold to homeowners, usually in their homes, and produced by crews over an extended schedule.

Primary users:

- **Owner / general manager** — watches the pipeline, production load, and profitability; in small firms, also the salesperson and production manager.
- **Salesperson / closer (often "in-home sales")** — works leads, runs sales appointments in the customer's home, builds and presents proposals, signs contracts, collects deposits. Commission tracking exists because selling is a distinct, compensated role.
- **Production manager / project manager** — turns sold jobs into production plans, assigns crews and workers, tracks steps against expected dates, unblocks delays.
- **Crews and field workers** (in-house or subcontracted) — execute installation steps; receive work orders and schedules; report completion.
- **Office coordinator / bookkeeper** — enters leads, schedules appointments, sends invoices and payment links, syncs accounting.

Secondary concerns: marketing staff running lead-generation and referral campaigns; service staff handling warranty work after completion.

The work environment is split between the office (pipeline, production board, money) and the field (sales appointments in living rooms, installation work at jobsites), so desktop consoles and mobile apps are both first-class surfaces.

## Core Model

### The Defining Core

Four structures, jointly held. Remove any one and the system stops being this Type:

- **The homeowner customer of record, carried through a managed sale.** The customer is a persistent contact that moves from inquiry/lead through estimate or proposal to a recorded sale. The recorded sale is the pivot of the whole model: it is what converts a lead into a customer and brings the job into existence. Without it, the system is a production tracker with no front door.
- **The improvement job of record at the home.** A persistent, individually identified job for the sold work at the customer's residence. It carries the products and scope sold (a job typically holds one or more products — a roof, a bank of windows, a bath remodel — each with its own details) and a jobsite address held separately from the customer's billing address. It is the container that production and money hang from. Without it, the system is a contact list with quotes.
- **Production as a planned multi-step effort.** The job's work is organized as a sequence of steps or phases — commonly templated per product type (for example: order material → delivery → installation → walkthrough) — each with expected start/end dates, actual start/end dates recorded as work happens, an assigned project manager, work crew, and workers, and optionally a work order per step. Work spans days to weeks and is tracked to completion. Without it, the system is a dispatch board for one-visit service calls.
- **Money resolved across the job's life.** A deposit is collected at or shortly after the sale; further payments are tied to progress or completion; the final balance closes the job. Job costs (materials, labor) and — where the business has a sales team — commissions are recorded against the job, so every job can be judged on margin. Without it, the system is a sales CRM with no fulfillment economics.

These four are load-bearing together: a lead tracker with a job list is a CRM; a production scheduler without customers and money is a bare project tool; a sales pipeline with invoicing but no production is a quoting tool; production and money without the sold job are generic project accounting.

### Standard Capabilities

Mature products commonly add the consumer-sale instrument set and the operational wrapper. These make the business practical but do not define the Type:

- **Estimates and proposals** — multi-option or tiered ("good/better/best"), with photos and videos, built from templates that auto-fill priced products and services; measurement data imported from specialist tools (aerial roof measurement, room measuring) via integrations.
- **Contracts and job documents** — e-signature on proposals and contracts; change orders, work orders, and service documents stored on the job; jobsite photos attached to the record.
- **Homeowner financing** — financing offers presented during the sale (multi-lender matching, quick decisions, staged funding), because large-ticket improvement work is often financed.
- **Sales-appointment machinery** — appointment scheduling with driving-route optimization, reminders, two-way texting, and appointment results that drive the pipeline.
- **Lead generation and marketing automation** — lead-provider and call-tracking integrations, drip email campaigns, jobsite-radius prospecting, and post-completion referral and review campaigns.
- **Production coordination** — production calendars, work orders, crew assignment, business-day scheduling rules, and automated customer status updates as steps complete.
- **Warranty and service** — service orders and service scheduling against completed jobs, with warranty reminders.
- **Surveys and reviews** — customer surveys and review requests attached to completed jobs.
- **Reporting** — production aging (how long jobs have sat in each step), work-in-progress, job costing, commission reports, marketing ROI, dashboards.
- **Accounting sync** — invoices, payments, and costs pushed to external accounting (QuickBooks in the North American market).
- **Mobile apps** — for sales (quote and close in the home) and field (work orders, schedules, photos, payments).

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  the recorded sale that creates the job
Implementations:  a "sold" appointment result on the lead record;
                  an accepted/signed proposal; a signed contract with deposit

Concept:  the production plan
Implementations:  templated production processes per product type;
                  free-form task lists; project phases with milestones;
                  Gantt-style timelines with task dependencies

Concept:  money across the job's life
Implementations:  deposit + progress invoices + final invoice;
                  lender-funded contracts (financing pays the contractor upfront);
                  card-on-file and payment links against the job
```

## How It Works

The canonical loop runs from lead to referral:

```text
Lead captured (inquiry, ad, lead provider, referral)
→ sales appointment scheduled and routed
→ in-home visit: measure, build options, present proposal
→ sale recorded (signed proposal/contract; deposit collected; financing arranged)
→ job created from the sale (products, scope, jobsite address)
→ production plan built (steps/phases, crews, expected dates, work orders)
→ production executed step by step (actual dates recorded; customer updated)
→ payments collected across the job (deposit → progress → final balance)
→ job closed: costs and commissions posted; margin visible
→ after-sale: warranty/service, survey, review request, referral campaign
```

**Selling.** A lead enters the system from an inquiry, ad campaign, lead provider, or referral. The office or salesperson schedules a sales appointment — this trade sells in the customer's home — and the appointment is routed and reminded. In the home, the salesperson measures or imports measurements, assembles a proposal from priced templates (often presenting two or three options), and closes: the proposal becomes a signed contract, a deposit is collected, and financing may be arranged on the spot. The recorded sale is the gate: it converts the contact from lead to customer and prompts job creation.

**Producing.** The production manager builds the job's plan — often by applying a templated process for the product sold — and assigns a project manager, crews, and workers. Steps carry expected dates; as work happens, actual dates are recorded, work orders are issued, and the customer is notified of status. Multi-day work appears on production calendars; some products let the business define its working days and automatically push steps that fall on non-working days. Delays surface on production-aging reports.

**Getting paid.** The deposit is held against the job from sale day. As phases complete, progress invoices go out — often as digital invoices with payment links; the final balance is collected at completion. Job costs (materials, labor, subcontractors) and sales commissions post against the job, so margin is visible while work is still in progress, not just at year-end.

**After the sale.** Completed jobs feed the warranty loop (service orders, reminders), the reputation loop (surveys, review requests), and the growth loop (repeat and referral campaigns to past customers).

## Interfaces

The surfaces below are described conceptually; names and layouts vary by product.

### Contact / lead record

The anchor record for a homeowner.

- contact details, lead source, lifecycle stage (prospect/lead/customer), inquiries and appointments, jobs, documents
- primary actions: add lead, schedule appointment, record appointment result, convert lead to customer, create job

### Sales calendar / appointment board

The selling rhythm of the business.

- sales appointments by day, routed by geography; slot scheduling; reminders
- primary actions: schedule, reschedule, record result (sold / not sold / follow-up)

### Estimate / proposal builder

Where the sale is assembled.

- product/service templates with pricing, options and tiers, photos, measurement imports
- primary actions: build estimate, present options, send for e-signature, attach financing offer, collect deposit

### Job / project record

The container for sold work.

- products and scope, jobsite address, status, production link, documents and photos, financial summary
- primary actions: create from sale, add products, attach documents, open production, invoice

### Production board / calendar

The execution view.

- steps and phases per job with expected vs actual dates, assigned crews, work orders; calendar of installations; aging and bottleneck views
- primary actions: apply a production process, assign crew/worker, schedule step, record actual dates, create work order

### Money views

Invoices, payments, deposits, job costs, commissions; payment links and card-on-file; reconciliation and margin reports.

### Service / warranty tab

Service orders and scheduling against completed jobs, with warranty reminders.

### Dashboards and reports

Pipeline and conversion, production status, work-in-progress, job costing, commissions, marketing ROI.

### Mobile apps

Sales app (appointments, quotes, signatures, deposit collection in the home) and field app (work orders, schedules, photos, completion, on-site payment).

## Important Rules / Behaviors

- **The sale gates the job.** In the purpose-built products, a job normally comes into existence through a recorded sale — an appointment result marked sold, or an accepted/signed proposal. A lead whose appointment is not resulted as sold stays a lead; some products let a customer be reverted from a sale. Jobs can also be entered directly for customers without a sales appointment, but the sale-first path is the dominant design.
- **Payments are structured, not single-shot.** The deposit is collected early (partly to secure the schedule), and remaining payments are tied to progress or completion. Financing changes the shape: a lender may fund the contractor upfront while the homeowner repays the lender.
- **Production steps carry expected vs actual dates.** The gap between them is the system's early-warning signal; products compute aging per step and per job, and some automatically push steps that fall on non-working days.
- **The jobsite address is not the billing address.** Work happens at the customer's residence; the model keeps the two apart.
- **Margin is a per-job fact.** Costs and commissions post against the job so profitability is judged job by job — the trade's standard unit of economic truth.
- **The after-sale loop hangs off the completed job.** Warranty work, surveys, reviews, and referral campaigns are recorded against the job that produced them.
- **Lifecycle states are conceptual, not standardized.** Exact stage names, appointment-result options, and job statuses vary by product and are usually configurable by the business.

## Variants

- **Purpose-built remodeler CRM** — the center of gravity is the lead→sale→production pipeline with marketing automation (the classic "remodeling CRM").
- **Enterprise remodeler CRM** — the same shape at larger scale, with heavier reporting/analytics and franchise or manufacturer network programs.
- **Construction-management pole** — builder/remodeler software with client-facing project machinery: specifications, selections, client portals, budgets. Functionally interlocks with Construction Project Management; the strongest products here also serve custom home builders.
- **Suite FSM construction module** — a field-service platform's construction/remodel side: project tracking, phase billing, crew management alongside the service business. Serves contractors that do both service calls and remodel projects.
- **Standalone in-home sales layer** — the sale instrument set (measure → estimate → proposal → financing → e-sign → deposit) sold as its own product and integrated into the management systems above.
- **Trade-specialized deployments** — the same spine configured per product family (roofing, windows and doors, baths, siding, painting, decks), with trade content rather than structural difference.
- **Scale and network variants** — one-person operators (all roles collapsed) through multi-crew firms to franchise/manufacturer networks.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Small Business Field Service Management | closest sibling | the unit of work is a dispatched service call (often one visit, invoice on completion) vs a sale-driven project with a production plan and deposit→progress→final payments; platforms themselves split "service" from "construction/remodel" |
| Construction Project Management | adjacent at the builder/remodeler pole | multi-organization project community with formal cross-party coordination instruments vs one contractor's whole-business system (leads, sales, production, money) for consumer work |
| Handyman Business Management | sibling at the small-job edge | small dispatched multi-skill jobs vs larger project-shaped improvement work with production plans |
| Trade siblings (Roofing, Painting, Flooring, Siding, Solar…) | siblings | the generalist pole of improvement work; trade siblings add trade-specific structures (e.g. flooring's measured-area basis) |
| CRM (Sales) | shares the front half | the lead→opportunity→sale pipeline is shared; the job of record, production plan, and job-life money are not CRM structures |
| Construction Estimating / Quantity Takeoff | capability supplier | estimating and measurement tools feed the proposal; they hold no job of record or production |
| Local Service Marketplace | demand side | lead generation and booking vs the contractor's own execution and billing; lead providers feed this system's lead stage |
| Home Improvement Planner (consumer) | different subject | a homeowner's own project planning vs the contractor's business system |
| Property Maintenance Management | different operator | property managers coordinating portfolios vs the executing contractor's own business |
| Appointment Scheduling Application | fragment | sales-appointment scheduling is one surface, not the organizing object |

The two boundaries that deserve joint review are Small Business Field Service Management (the seam is gradual — small improvement jobs on an FSM product are the boundary pole) and Construction Project Management (the builder/remodeler pole interlocks with that Type's residential small-business pole, which its own research recorded as client-facing approvals — selections and signatures — rather than contract-form instruments).

## Representative Products

- MarketSharp — purpose-built remodeler/home-improvement CRM with production and payments
- ServiceTitan (Residential Remodeling) — trades platform's construction/remodel side
- improveit 360 — enterprise remodeler CRM
- FieldPulse (Contractors) — horizontal SMB platform, generic-contractor pole
- One Click Contractor — standalone in-home sales/estimating layer

The defining core was checked against the market's construction-management pole (CoConstruct, now migrating into Buildertrend) to avoid over-fitting to the CRM-shaped products.

## Sources

Research date: **2026-09-08**

- MarketSharp — root, project-management, convert-leads-to-sales, and payments pages; help center (Jobs, Production, Contact Management categories; Job Details; Adding Production Tasks/Processes; Production Overview; Converting a Lead to a Customer; Payments Setup) — https://www.marketsharp.com/ , https://support.marketsharp.com/hc/en-us
- ServiceTitan — Residential Remodeling industry page and industries map — https://www.servicetitan.com/industries/residential-remodeling , https://www.servicetitan.com/industries
- improveit 360 — root and Project Management feature pages — https://www.improveit360.com/ , https://www.improveit360.com/features/project-management/
- FieldPulse — Contractors solution page — https://www.fieldpulse.com/solutions/contractors
- One Click Contractor — root page — https://oneclickcontractor.com/
- CoConstruct / Buildertrend — migration page (market structure) — https://www.co-construct.com/

> Sourcing limitation: official help-center documentation was reachable only for MarketSharp; the other products' evidence is official product-page level, and several major vendors in this category (Buildertrend, Houzz Pro, Leap, Buildxact, JobNimbus, JobProgress) could not be accessed at all. Precise operational details (exact statuses, limits, defaults, payment-schedule mechanics beyond the deposit/progress/final pattern) are therefore not asserted; claims are calibrated to the reachable evidence.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
