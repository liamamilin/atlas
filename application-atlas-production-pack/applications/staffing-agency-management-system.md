# Staffing Agency Management System

## Overview

A **Staffing Agency Management System** is the agency-side business system of record: the software a staffing firm runs its entire operation on. The agency's business is to supply workers to client organizations — permanent hires for a fee, temporary and contract workers on assignment — and this system holds every part of that business: the clients and their job orders, the candidate pool, the submissions made to clients, the placements that represent revenue, and, for temporary staffing, the whole pay-and-bill cycle in which the agency pays the worker and invoices the client.

The defining core is small:

```text
Client (the organization buying workers)
  └── Job order (the client's open position, with its commercial terms)
        └── Candidates, matched and submitted to the client
              └── Placement (the commercial win)
                    ├── Direct hire → placement fee
                    └── Temp/contract assignment → worked time → worker pay + client billing
```

Everything else commonly associated with these products — business-development pipelines, AI matching, client portals, timesheet machinery, payroll processing, dashboards — is standard capability that mature products add around this core. Remove the client-owned job order and the placement-as-revenue-event, and what remains is an employer's applicant tracker or a candidate database; remove the supplier-side posture (the agency that employs and pays the workers), and what remains is the client-side vendor-management system.

## Users & Context

The operator is the staffing firm itself. Several distinct roles work in the same system:

**Primary operators:**

- **Recruiter / resourcer** — works the fill loop: sources and screens candidates, matches them to job orders, submits shortlists to clients, schedules interviews, and drives placements. Their desk is the pipeline view.
- **Account manager / business development** — owns the client relationship: wins new job orders, manages existing accounts, tracks leads and opportunities. In many firms the same person both sells to clients and recruits for them.
- **Back-office / pay-and-bill administrator** — runs the middle and back office: collects and approves timesheets, calculates pay and bill amounts, processes payroll runs, generates client invoices, records payments.

**Secondary users:**

- **Compliance / onboarding staff** — verify that a worker's documents, checks, and certifications are complete before an assignment starts, and track expiries during it.
- **Branch / operations managers** — monitor fill rates, submittal-to-placement ratios, gross profit, and recruiter performance across desks or offices.
- **Finance** — consumes invoicing, payment, and payroll outputs.

**External participants (via portals):**

- **Clients** — in mature deployments, client contacts review submitted candidates, give interview feedback, and approve timesheets through a client or hiring-manager portal.
- **Workers themselves** — temporary workers enter time, complete onboarding documents, and receive communications through worker portals or mobile apps.

Typical context: agencies of every size — from a solo desk to multi-branch enterprises — across industry verticals such as professional/IT, clerical and light industrial, healthcare, and executive search. The work is high-volume and relationship-dense: many job orders, many candidates, recurring timesheet and invoice cycles.

## Core Model

### The Defining Core

Four structures. Remove any one and the product stops being this Type:

**1. The client account of record.** The agency's customers are client organizations, and the system holds them as commercial accounts: company record, contacts (who may be both a hiring contact and, elsewhere, a candidate), relationship and activity history, and the commercial terms under which the agency serves them. The client is the demand-side anchor — every job order belongs to one. This is the structural difference from employer-side recruiting software, where the hiring organization is the system's owner rather than its customer.

**2. The client-owned job order.** The unit of demand: a position a client wants filled, carrying the role's requirements and its commercial terms — either a placement fee (for direct hires) or pay and bill rates (for temporary and contract work). The job order is what the agency works to fill, tracks through its own stages, and reports on (time to fill, submittals, interviews). In several products the job order is literally framed as an *opportunity* — a potential, active, or completed chance at revenue — and business-development leads convert into job orders when a client commits. Orders also arrive from client-side vendor-management systems, in which case the agency system ingests them as job orders to review and work.

**3. The candidate pool and the submission motion.** The supply side: people held as records — sourced from applications, referrals, job boards, or the agency's accumulated database — matched against job orders, and **submitted to the client**. The submittal is the match motion made visible to the buyer: a record that this candidate was proposed for this job order, usually with a resume (sometimes branded or blinded), sent by email or through the client portal, and tracked to an outcome (interview, rejection with reason, placement). Submission history matters: a candidate already submitted to one client is a sensitive record for other clients.

**4. The placement as the commercial outcome.** The record of the win, binding candidate ↔ job order ↔ client. It takes two forms:

- **Direct hire** — the candidate accepts a permanent role; the placement records the salary, start date, and fee percentage, and the agency invoices its fee. The placement is how the firm captures and reports the value of the deal.
- **Temp/contract assignment** — the placement becomes an assignment with start and end dates, a pay rate (what the worker earns) and a bill rate (what the client pays), and it generates the recurring cycle: worked time → approved timesheet → worker pay + client invoice. Extensions produce new placement records; a temp can later be converted to a permanent placement.

The placement is the system's revenue event. Everything upstream exists to produce it; everything downstream (payroll, invoicing, gross profit) flows from it.

### Standard Capabilities

Mature products organize the rest of their capability around the industry's own three-layer division — front office, middle office, back office — a vocabulary the leading vendors themselves use:

**Front office — winning and filling the work:**

- Client CRM and business development: lead pipelines, account management, activity and outreach tracking (email, SMS, phone), conversion of leads into job orders, job-source attribution.
- Sourcing and matching: resume parsing, database search, keyword and AI-assisted matching, multi-board job posting, agency job portals.
- Recruiting workflow: per-job-order pipeline stages, interview scheduling, notes, scorecards.
- Submittal machinery: submittal templates and grids, client portals for requisitions and feedback, resubmittals.

**Middle office — from placement to paycheck and invoice:**

- Onboarding and compliance: document capture with expiry tracking, prerequisite gates (a placement stays pending until its required documents and checks are met), right-to-work and work-authorization checks, background checks, certifications and licences, e-signature.
- Time capture: timesheets in multiple entry formats, mobile and clock-based collection, geofencing, approval chains.
- Pay-and-bill calculation: pay plans and pay rules (including overtime), bill rates and rate cards, burden (employer-cost loading) on the pay rate, margin computation, and checks that pay stays below bill.
- Client invoicing: billable items accumulated from approved time (plus manually added charges), client-specific invoice templates, payment recording.

**Back office — money and record-keeping:**

- Payroll processing for the placed workforce: pay runs, deductions, garnishments, paystubs, year-end forms, multi-jurisdiction tax handling.
- Financial and operational reporting: gross profit, revenue by client or recruiter, fill and submittal ratios, time-to-fill, worker utilization.

**Connective tissue:**

- Worker engagement: candidate/worker portals, mobile apps, aftercare messaging.
- Integration spine: job boards, client VMS systems, payroll and funding providers, background-check and e-signature services, accounting/HRIS.
- AI assistance (current generation): matching, drafting, document extraction, audit rules, question-answering over the agency's own records.

The depth of the middle and back office varies by product: some platforms run the entire pay-to-bill lifecycle natively; others execute it through integrations, exporting placement and time data to specialist payroll and billing systems. Both postures are common; the cycle itself is what the temp/contract form of the Type exists to run.

## How It Works

The core loop runs once per job order; the money cycle runs weekly per assignment; the relationship loop runs continuously.

### Win the work

```text
Lead or client contact
→ opportunity / job order created (role, requirements, fee or pay/bill terms)
→ (if from a client VMS: order ingested, reviewed, converted to a job order)
→ job order opened and owned by a recruiter or desk
```

### Fill the order

```text
Source candidates (database search, applications, job boards, AI matching)
→ screen and interview internally
→ submit shortlist to the client (email or client portal)
→ client feedback / client interviews
→ offer negotiated and accepted
```

### Place and start the worker

```text
Placement record created (candidate ↔ job order ↔ client)
  ├── direct hire: salary, start date, fee % → fee invoiced
  └── temp/contract: start/end dates, pay rate, bill rate → assignment begins
→ onboarding gate: documents, checks, certifications completed
→ (some firms require a manager's approval before the placement is finalized)
```

### Run the assignment (temp/contract)

```text
Worker works the week
→ time entered (mobile, timesheet, clock)
→ timesheet approved (worker → agency → often the client manager)
→ pay calculated from pay rules; bill calculated from bill rates
→ payroll run pays the worker
→ billable items claimed onto the client invoice
→ invoice sent; payment recorded
```

### Collect and manage

Across all of it, managers watch the population as a whole: open job orders and their aging, submittal and interview ratios, placements and gross profit, timesheet completion, invoice and payment status, compliance expiries — and adjust (reassign orders, chase timesheets, follow up invoices).

### Where the system starts and stops

It starts at the lead or job order and ends at the paid invoice and closed placement (or the ongoing assignment's next cycle). It does not run the client's workforce program (that is the VMS seat), does not hire into the agency's own org chart (that is an ATS/HRIS matter for the agency's own employees), and does not replace general accounting, though it feeds it.

## Interfaces

The surfaces below are described conceptually; exact layouts and names vary by product.

### Job order dashboard / pipeline

The recruiter's home surface.

- typical information: open job orders with stage, age, owner, submittal counts, client
- primary actions: create/edit job order, move candidates through stages, submit, close

### Candidate search and profile

The supply-side working surface.

- typical information: resume, skills, work history, notes, current status, submission history
- primary actions: search/match, add to job order, submit to client, log activity, attach documents

### Job order detail

The demand object's record.

- typical information: client, role description, requirements, fee or pay/bill rates, pipeline of candidates with stages, activity history
- primary actions: add candidates, submit, schedule interviews, edit terms, close

### Placement grid

The revenue view.

- typical information: placements with candidate, client, job order, type (direct hire/contract/hourly), fee or rates, start/end dates, status
- primary actions: create placement, approve, extend, convert temp-to-perm, record splits

### Timekeeping / timesheets

The recurring middle-office surface.

- typical information: pending and finalized time cards by worker, placement, and period; approval state
- primary actions: enter/override time, approve, finalize, export to payroll

### Invoicing

The billing surface.

- typical information: unclaimed billable items, draft and sent invoices by client, payment status
- primary actions: claim billables, generate invoice (by client/employee/job order), send, record payment

### Client portal

The client's window into the agency's work.

- typical information: their job orders/requisitions, submitted candidates, interview feedback, timesheet approvals
- primary actions: review and act on submissions, approve time, request candidates

### Worker portal / mobile app

The placed worker's surface.

- typical information: assignment details, timesheets, onboarding tasks, messages
- primary actions: enter time, complete documents, communicate

### Reports and configuration

- reports: fill/submittal/placement ratios, gross profit, recruiter performance, compliance status
- configuration: pipeline stages, custom fields, pay rules, invoice templates, user roles and permissions

## Important Rules / Behaviors

**The placement is the revenue event.** A filled pipeline is not revenue until a placement exists — a fee-bearing hire or a running assignment. Reporting, commissions, and invoicing all key off the placement record.

**Pay must stay below bill.** The agency's margin lives in the spread between what it pays the worker and what it bills the client. Mature products treat this as a checkable rule — audits confirm pay is below bill rate and compare placements against rate cards — because an error here is a direct margin loss.

**No approved time, no pay, no bill.** For temp/contract assignments, worker pay and client billing both derive from approved worked time. Timesheets move through approval chains (worker → agency, often involving the client's manager) before they become payable and billable; finalized time entries become the billable items claimed on invoices.

**Compliance gates the start of work.** A placement commonly stays in a pending state until its prerequisite documents and checks are complete; documents carry expiry dates that are tracked during the assignment, with reminders when they lapse. The specific regime varies by jurisdiction — work-authorization and payroll-tax machinery in the US, tickets/licences and labour-hire documents in Australia, right-to-work and data-protection machinery in the UK/EU.

**Invoicing is client-specific.** Clients dictate invoice formats, contents, and approval flows; products support per-client billing profiles and templates, and invoices are generated from approved time and agreed rates rather than typed by hand.

**Placements can be governed.** Some products require an administrator's approval before a placement is finalized, and recruiter splits/commissions on a placement are recorded as relationships on the placement itself.

**One person, several roles.** The same person can be a candidate for one client and a hiring contact for another; the record model keeps these roles distinct while sharing the person.

**Conceptual states, vendor labels.** Job orders, submittals, placements, timesheets, and invoices all have lifecycle states, but exact stage and status names vary by product; the flows above are the stable part.

## Variants

Common shapes of the same Type:

- **Business mix** — perm/direct-hire-only desks (fee placements, no timesheets or payroll), temp/contract-heavy desks (the full pay-and-bill middle office), and blended agencies; temp-to-perm conversion flows connect the two.
- **Back-office depth** — native payroll and billing inside the same platform vs integration-export to specialist payroll/billing systems; both postures are common in the market.
- **Industry verticals** — professional/IT staffing, clerical and light industrial (high-volume, shift-oriented), healthcare (credentialing-heavy), executive search (retained, fee-only, low-volume/high-value).
- **Regional regimes** — US (work authorization, multi-state payroll tax, year-end forms), Australia/NZ (tickets and licences, labour-hire documents), UK/EU (right-to-work, data protection); the compliance module takes each regime's shape.
- **Scale and structure** — solo desks and small agencies through multi-branch and franchise networks with shared back offices.
- **VMS posture** — the agency as a supplier into client-run VMS programs (orders flow in, time flows out) vs the agency operating its own client-facing portal or VMS-like surface; larger platforms may do both, and some serve master-vendor arrangements with sub-agencies.
- **Deployment** — cloud SaaS is standard; older on-premise back offices persist in long-established firms.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Applicant Tracking System / ATS | same pipeline shape, other seat | The employer runs its own requisitions and ends at a hire into its organization. Here the operator is a firm filling **client-owned** job orders, ending at a placement the agency monetizes, with a client CRM bundled. |
| Vendor Management System / Contingent Workforce Management | mirror image (buyer side) | The VMS is the buyer's system: it distributes requests to suppliers, selects among submissions, and approves invoices — it never employs or pays the workers. This Type is the supplier's side of the same transaction: it wins the order, employs and pays the temps, and bills. Client VMS orders flow *into* agency systems as job orders. |
| Recruiting Management Platform | convergent in agency mode | Dual-sided recruiting platforms cover client CRM, placements, and revenue tracking; this Type's center of gravity adds the agency's business operations — timesheets, pay/bill, compliance, invoicing. The market overlaps heavily; the seam is the center of gravity. |
| Payroll System | one leg, not the whole | Agency payroll exists to pay placed workers against assignments and approved time, connected to billing and gross profit. A standalone payroll system has no job orders, candidates, or clients. |
| Employee Scheduling Platform | downstream step | Temp coverage may involve rostering and shift scheduling, but scheduling is not the spine; the order → placement → pay/bill chain is. |
| CRM (Sales) | one face of the Type | The client CRM is one of the four core structures; without job orders, candidates, and placements it is just a CRM. |
| Job Board / Career Site Platform | intake channel | Agency job portals and multi-board posting are publishing/intake channels feeding the job orders, not the system of record. |
| Talent Agency Management | different domain | Both are "agency" systems, but talent agencies manage performers' careers and engagements in entertainment; staffing agencies supply workers to employers. Different objects, money flows, and compliance regimes. |

The two most important boundaries are the **operator seat**: employer-side (ATS) vs agency-side (this Type) vs buyer-side (VMS/contingent workforce management). The same requisition-to-worker flow exists on all three sides of the staffing transaction; who owns the record — and who pays the worker — defines the Type.

## Representative Products

- **Bullhorn** — market-leading platform for staffing agencies; front-office ATS & CRM plus a separately licensed middle office (time capture, pay/bill, compliance, invoicing); ecosystem of hundreds of integrated partners.
- **Crelate** — mid-market all-in-one (recruiting, onboarding, timekeeping, payroll, invoicing) with deep operational documentation of the core records.
- **Avionté** — front-and-back-office single platform for high-volume temp/contract staffing; native payroll and billing as its flagship differentiator.
- **JobAdder** — international (Australia-origin) mid-market platform for perm and temp desks; recruiter-experience focus with the pay/bill cycle executed through integrations.

The core model was checked against the perm-only desk shape (fee placements without pay/bill) and against the paper-era agency practice (job order books, candidate card files, time cards, client invoices) to avoid defining the Type by today's temp-heavy, cloud, AI-era implementation.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces:

- Bullhorn — ATS & CRM product page: https://www.bullhorn.com/products/applicant-tracking-system/
- Bullhorn — Middle Office product page (incl. front/middle/back-office FAQ): https://www.bullhorn.com/products/middle-office/
- Crelate Help Center: https://help.crelate.com/ — including "What is a Placement in Crelate?", "What is an Opportunity Record?", "What are Billable Items?", "VMS Opportunity"
- Avionté — homepage and Payroll & Billing: https://www.avionte.com/ , https://www.avionte.com/payroll-billing/
- JobAdder — Features, Temporary Recruitment, Placement Management: https://jobadder.com/features/ , https://jobadder.com/temporary-recruitment/ , https://jobadder.com/placement-management/

> Sourcing limitation: vendor help centers for Bullhorn, Avionté, and JobAdder were not deeply reachable from the research environment on 2026-09-08; claims about those products rest on official product pages, and precise operational details (stage vocabularies, numeric limits, default rates, plan gating) are intentionally not stated. Crelate claims are backed by help-center articles. Vendor volume figures (workers paid, W-2s processed) were observed in marketing material and excluded from the body of this document.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis are recorded in the paired Research Notes.
