# Legal Billing Application

## Overview

A **Legal Billing Application** is a law firm's money-loop system of record: it converts the firm's captured legal work into client bills, tracks those bills to payment, administers client-held funds, and holds the firm's billing money position — work-in-progress, receivables, collections — as an inspectable picture the firm is managed by.

The defining structure is small:

```text
Client + Matter (billing anchors) + Timekeepers with rates
└── Captured billable work (time / expenses / flat fees) as entries
    └── Bill assembly under fee arrangements (draft → review → final invoice)
        └── The firm money loop (delivery → payment/AR → client funds → firm money position)
```

Everything else commonly associated with legal billing software — timers, client portals, online payments, trust-accounting reconciliation, e-billing formats, dashboards, AI time capture — is widespread in current products but is not what makes the product a legal billing application. A paper-era firm running time sheets, typed bills from a rate card, and a receivables ledger fits the same definition.

The boundary that matters most: this is the **firm side** of legal money. The firm generates the bills; the client's legal department reviews and approves them on the other side of the boundary (Legal Spend Management). And this is the **money loop standing alone** — the matter workspace (documents, deadlines, conflicts) belongs to Law Practice Management, which fuses the two.

## Users & Context

The primary users are the people inside a law firm whose work becomes money:

- **Timekeepers (attorneys, paralegals)** — capture their billable time and expenses against clients and matters; their rates are held in the system.
- **Billing staff / billing administrators** — assemble draft bills, apply adjustments and write-offs, run the billing cycle, manage templates and delivery.
- **Partners / firm management** — review pre-bills, approve time, and read the firm money picture (receivables, realization, productivity, compensation allocation).

Secondary concerns: bookkeepers/accountants (books posture varies — embedded or external), IT/administrators (access control, ethical walls), and clients themselves (portal access to invoices and payment).

The work environment is the firm's billing cycle: time captured continuously, bills issued on a cycle (monthly is common but firm-configured), payments and trust balances monitored continuously.

## Core Model

### The Defining Core

```text
Client + Matter (billing anchors) + Timekeepers with rates
└── Captured billable work (time / expenses / flat fees) as entries
    └── Bill assembly under fee arrangements (draft → review → final invoice)
        └── The firm money loop (delivery → payment/AR → client funds → firm money position)
```

- **Client + Matter as billing anchors** — every billable unit of work is attributed to a client and, within the client, to a matter (the legal unit of work: a case, a transaction, a piece of advice). The matter is the container that rates, fee arrangements, and billing settings attach to. Without this legal attribution structure, the product is generic invoicing.
- **Timekeepers with rates** — the people whose work is billed exist in the system as timekeepers, each carrying rate tables (by timekeeper, by level such as partner/associate/paralegal, by client or matter). Rates are configuration, not afterthought: the same hour is worth different amounts depending on who worked it and for whom.
- **Captured billable work as entries** — time entries (with configurable billing increments and activity/task codes), expense entries, and flat fees, each tied to client + matter + timekeeper, marked billable or non-billable. Entries accumulate as unbilled work-in-progress until billed.
- **Bill assembly under fee arrangements** — entries are compiled into draft bills, reviewed and adjusted (pre-bill review, write-downs, holds), then finalized as invoices under the matter's billing arrangement: hourly, flat fee, contingency, retainer, progress billing, split-fee, or task-based electronic billing.
- **The firm money loop** — issued invoices are delivered (print, email, portal, e-billing) and tracked to payment; client-held funds (retainers, trust where the jurisdiction requires) are administered against bills; and the firm's money position — WIP, accounts receivable, realization of billed vs collected, productivity and profitability by timekeeper and client — is held as reports and dashboards.

### Capabilities Shared by Mature Products

These make the loop practical; they do not define the Type:

- **Timers and capture aids** — one-click timers, calendar/task/email conversion to entries, mobile capture, unbilled-time alerts.
- **Batch invoicing and templates** — branded invoice templates, statement designers, batch generation and delivery.
- **Client portal and online payment** — invoices with pay-now paths, payment plans, reminders, native or integrated payment processing.
- **Trust accounting** — separate client-fund ledgers, deposits and disbursements tracked per client/matter, reconciliation, audit trails, compliance with bar/client-money rules where applicable.
- **Time approvals** — supervisory review of time entries before they reach a bill.
- **Access control** — role-based permissions over billing data; segregated access for ethical walls on sensitive matters.
- **Firm reports** — AR aging, WIP, realization, productivity, client profitability, compensation/originating-timekeeper allocation.
- **e-billing format support** — task-based billing codes and electronic invoice formats (LEDES/UTBMS lineage) for clients that mandate them.

### One Structure, Many Implementations

```text
Concept:            Books posture
Implementations:    embedded general ledger/AP inside the product, or sync to external books (QuickBooks/Xero)

Concept:            Bill delivery
Implementations:    print/PDF, email, client portal, e-billing delivery platforms, physical mail services

Concept:            Client funds
Implementations:    operating-account retainers, dedicated trust-accounting modules, integrated payment processors with trust safeguards
```

A reader who has only seen a modern cloud billing product should still be able to recognize a desktop-era time-and-billing system from the Core Model.

## How It Works

### Set up the billing structure

```text
Create client records
→ create matters under clients
→ assign timekeepers and their rates (standard, by level, per client/matter)
→ set each matter's billing arrangement (hourly / flat / contingency / retainer / …)
→ configure billing increments, activity codes, invoice templates
```

### Capture the work

```text
Timekeeper works
→ starts a timer (or enters time later, or converts a calendar/task/email entry)
→ entry lands against client + matter + activity code, at the applicable rate
→ expenses captured with receipts; flat fees entered or milestone-triggered
→ entries accumulate as unbilled work-in-progress
→ (in mature products) a supervisor reviews/approves time before billing
```

### Run the billing cycle

```text
Select client-matters with unbilled entries
→ generate draft invoices (pre-bills)
→ review: edit narratives, write down or hold entries, apply adjustments
→ finalize and send (print / email / portal / e-billing), individually or in batch
→ record payments; allocate a single client payment across matters and timekeepers
→ follow up: aging reports, reminders, interest/late fees where configured
```

### Administer client funds and read the money position

```text
Retainer requested → retainer invoice issued → funds received into trust/client-funds ledger
→ bills paid from the ledger as work is billed
→ balances reconciled; audit trail retained
→ firm reports: WIP, AR, realization, productivity, compensation allocation
```

### Core vs Common vs Optional

**Defining core** — without these, not a legal billing application:

- client–matter billing structure with timekeepers and rates
- work capture as entries against that structure
- bill assembly under fee arrangements (draft → review → final)
- the firm money loop (payment/AR tracking, client funds where applicable, firm money position)

**Common mature structure** — present in most modern products:

- timers, mobile capture, unbilled-time alerts
- batch invoicing, templates, statement designers
- client portal, online payments, reminders
- trust accounting with reconciliation and audit trails
- time approvals, role-based access, ethical walls
- firm reports (AR aging, WIP, realization, profitability, compensation)
- e-billing format support

**Variant / optional** — depends on firm size, jurisdiction, era:

- books posture (embedded GL vs external books sync)
- enterprise compliance depth (client-guideline/OCG automation, e-billing delivery platforms, pricing/profitability tools)
- adjacent pillars bundled by the same vendor (case management, CRM, documents, calendaring)
- matter plans with billable milestones, progress billing, split-fee arrangements
- deployment (cloud vs on-premises), multi-currency, invoice translation, physical-mail delivery
- AI-assisted time capture and narrative drafting

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Time entry surface

The timekeeper's daily surface.

- timers, entry grids, calendar-based entry, recent matters
- primary actions: start/stop timers, enter or batch-edit time and expenses, mark billable/non-billable, attach to matter and activity code

### Client & matter records

The billing structure's registry.

- client and matter details, billing settings (arrangement, rates, categories, delivery preferences), WIP and balance summaries
- primary actions: create/edit client and matter, set rates and fee arrangements, hold billing, consolidate matters onto one invoice

### Draft / pre-bill workspace

The billing staff's review surface.

- draft invoices per client-matter with entry-level detail, edit/hold/write-down tools, batch operations, delivery method selection
- primary actions: generate drafts, edit entries and narratives, finalize, void, send

### Invoice & payment tracking

The money-state surface.

- invoice lists by status (draft/sent/paid/overdue), payment recording and allocation, credits and voids, retainer invoices
- primary actions: send, record/allocate payment, issue credit, void, remind

### Trust / client funds ledger

The client-funds surface where the regime requires it.

- per-client/matter ledgers, deposits and disbursements, balances, reconciliation and audit reports

### Reports & dashboards

The firm-management surface.

- AR aging, WIP, realization, productivity and profitability by timekeeper/client, compensation and originating-timekeeper allocation
- primary actions: run, customize, export

## Important Rules / Behaviors

### Entries are attributed, then consumed once

A time or expense entry is captured against a client-matter-timekeeper and remains unbilled WIP until it is included in an invoice; billed entries are consumed. Mature products restrict editing of entries and records once they are billed or paid — corrections happen through adjustments, credits, or void-and-reissue rather than silent edits. Exact edit rules vary by product.

### The fee arrangement governs the bill

The matter's billing arrangement determines what a bill contains and how amounts are computed — hourly entries at rate-table rates, a fixed fee regardless of hours, contingency handling, retainer application. The same captured work can produce different bills under different arrangements.

### Pre-bill review is a deliberate gate

Draft bills exist so the firm can catch errors and write down work before the client sees it. This internal review step is structural, not optional polish.

### Client funds are segregated

Where the jurisdiction's client-money rules apply, funds held for clients are kept separate from the firm's operating money, tracked in their own ledgers, and reconciled — a compliance-shaped constraint that shapes the whole payment side.

### Client guidelines reach back into the firm

Corporate clients impose billing guidelines (rates, task codes, invoice formats). The firm side carries machinery to comply — rate tables, activity/task codes, task-based e-billing, electronic delivery — because a bill that violates the guidelines is reduced or rejected on the buyer side.

### Access is controlled by role and by wall

Billing data is confidential and ethically sensitive; products provide role-based permissions and segregated access so that timekeepers and staff see only what their role and ethical walls allow.

## Variants

- **Standalone cloud time & billing** — the billing loop as the whole product, with matter workspace features sold beside it (small-firm pole)
- **Billing-first suite with embedded financials** — billing plus general ledger, payables, and trust accounting as one financial system (desktop-heritage lineage, on-premises or cloud)
- **Enterprise law-firm financial management** — the same loop at Am-Law scale with compliance automation, e-billing delivery, pricing/profitability layers, and embedded cloud financials
- **Non-legal verticals of the same engine** — the generic professional time-and-billing engine sold to accountants, consultants, architects; the legal instantiation is distinguished by matters, timekeeper rate tables, trust funds, and legal fee arrangements
- **Jurisdictional packaging** — trust/client-money machinery shaped by local regimes (US IOLTA-style, UK/AU client money); single-jurisdiction tools satisfy the core without multi-regime support

## Related Application Types

| Application Type | Distinction |
|---|---|
| Law Practice Management System | fuses this money loop with the matter workspace (client file, conflicts, deadlines, documents) and firm operations; remove the matter workspace from LPM and this Type remains |
| Legal Spend Management | the buyer side: the client's control surface over received bills (review gate, budgets, department money position); this Type generates the bills the buyer reviews — the invoice is the shared artifact |
| Legal Matter Management | centers the matter record, file, and progression (the work); here matters appear only as billing attribution anchors |
| Invoicing Application | generic invoice document for arbitrary goods/services; lacks timekeeper capture, matter attribution, legal fee arrangements, trust funds, and firm WIP/realization |
| Time Tracking Application | centers capturing and reviewing time; here capture is one leg of a loop whose center of gravity is the money |
| Professional Services Automation | the same engagement→work→billing→financials loop shape for professional services generally; the legal instantiation adds matters, rate tables, trust, contingency semantics, and e-billing compliance |
| Billing Platform / Subscription Billing | recurring charges against subscriptions and accounts; here bills arise from captured work billed per engagement cycle |

The two most important boundaries: **LPM** (the money loop vs the matter workspace — the market itself sells them as separate modules) and **Legal Spend Management** (firm-side generation vs buyer-side control over the same invoice).

## Representative Products

- Bill4Time — cloud standalone legal time & billing (small-firm pole)
- TimeSolv — cloud time & billing with documented invoicing/trust machinery
- Tabs3 Billing — long-lived billing-first suite with embedded financials option
- Aderant Expert — enterprise law-firm financial management (Am Law pole)

The Core Model was checked against the desktop-heritage and paper-era poles (Timeslips-class time-and-billing lineage; pre-software firm practice) to avoid over-fitting to the modern cloud pattern.

## Sources

Research date: **2026-09-10**

- Bill4Time — https://www.bill4time.com/ , https://www.bill4time.com/billing-and-invoicing/
- TimeSolv — https://www.timesolv.com/ , https://help.timesolv.com/ , https://help.timesolv.com/creating-invoices
- Tabs3 — https://www.tabs3.com/ , https://www.tabs3.com/tabs3-cloud/legal-billing-software/
- Aderant — https://www.aderant.com/

> Sourcing limitation: CosmoLex and Sage Timeslips could not be fetched (access denied on repeated attempts); the embedded-accounting and classic-desktop poles rest on cross-product and family-portfolio evidence rather than direct observation. Precise operational parameters (exact invoice state ladders, default approval chains, plan-gated features) are intentionally not stated; detailed observations are recorded in the paired Research Notes.
