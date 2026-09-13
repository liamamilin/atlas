# Production Accounting Platform

## Overview

A **Production Accounting Platform** is the financial system of record for a media production — a film, television series, episode, commercial, music video, or similar project. It holds the production's **budget** on a production-specific chart of accounts, captures every **actual cost** the production incurs as transactions coded to those accounts, accumulates them into the production's **general ledger**, and runs the recurring **budget-versus-actual control loop** — the cost report — through which the production accountant tracks spending, commitments, and the estimated final cost until the production wraps.

The defining core is small:

```text
Production (the financial unit of record)
└── Budget of record (organized by the production's chart of accounts)
└── Actual cost transactions, coded to budget accounts
    └── General ledger (the production's book of record)
└── Cost report loop (budget vs actuals vs commitments vs estimated final cost)
```

Everything else commonly associated with these products — integrated crew payroll, purchase cards, tax-incentive coding, multi-currency, AI-assisted coding — is widespread in current products but is not what makes the product a production accounting platform. A standalone budgeting-and-actualizing tool built on spreadsheets, and a payroll company's bundled accounting module, both satisfy the same core.

The Type exists because a production is not a going concern: it is a temporary financial entity with a fixed plan, a burst of spending, and a wrap. Its books are organized to answer one question continuously — *what will this production finally cost, and how does that compare to what we said it would cost?* — a question generic accounting software does not ask.

## Users & Context

The primary user is the **production accountant** (and their team — cost controller, assistant accountants), who keeps the production's books and produces the cost report. The work environment is the production office: costs arrive from many directions (vendors, crew, petty cash, cards, payroll), and the accountant's job is to code, post, approve, and report on them against the budget.

Secondary users and their relationship to the system:

- **Line producer / unit production manager** — consumes the cost report and budget views to keep the production inside its approved total; approves overages.
- **Producers and financiers (studio, network, investors)** — receive the cost report as the standing statement of the production's financial health; they are the reason the report is a formatted, shareable deliverable rather than an internal screen.
- **Accounts payable / accounting clerks** — enter invoices, purchase orders, and petty cash; prepare payments.
- **Crew members** — a peripheral but real user surface: they submit timecards, expense claims, and petty cash requests that become coded costs.

The rhythm of use is production-shaped: intense setup before the shoot, a weekly cost-report cycle during production, and a closeout at wrap. Commercials compress the same loop into days; episodic television repeats it per episode across a season.

## Core Model

### The Defining Core

**Production.** The container for everything. A production is a bounded, identified project with its own books, its own budget, its own chart of accounts, and its own lifecycle (setup → production → wrap). All transactions, reports, and controls belong to a production; nothing is booked "to the company" in the abstract. Products model this as a project that is created, worked, and eventually wrapped or closed.

**Budget of record.** The production's anticipated cost, held as an organized structure of **cost accounts** — the production's chart of accounts. Accounts are arranged by department and section (story, writers, producers, production staff, camera, art, locations, post, and so on), commonly with header accounts that roll up sub-accounts. The budget is the plan of record against which all actual spending is judged; it can be built in the platform or imported from a dedicated budgeting tool. In the commercial world, standardized industry budget forms and their line numbering often take the place of a house chart of accounts.

**Actual cost transactions.** Every cost the production incurs enters the books as a transaction coded to a budget account:

- **Accounts payable invoices** — vendor bills for goods and services.
- **Purchase orders (POs)** — commitments to spend, approved before the money is owed; a PO is a financial commitment that shows in reporting before any invoice arrives.
- **Payroll costs** — crew and cast wages, fringes, and employer contributions, arriving as coded payroll cost (see How It Works).
- **Petty cash and purchase cards** — the crew's small and fast spending channels, reconciled back into the books.
- **Journal entries** — accountant-made adjustments, allocations, and corrections.

Posted transactions accumulate into the **general ledger** — the production's detailed book of record, organized by account code, covering the lifetime of the production.

**The cost report loop.** The recurring comparison that gives the Type its purpose. Per account, the cost report sets side by side:

```text
Budget (as approved, plus approved overages)
  Actuals to date        — posted costs
  + PO commitments       — approved spending not yet invoiced
  = Total to date
  ETC (estimate to complete)  — what the accountant expects still to spend
  EFC (estimated final cost)  — total to date + ETC
  Variance               — budget vs EFC
```

The cost report is the production's standing financial statement: it goes to producers, studios, and financiers on a regular (commonly weekly) cycle, organized by department, and it is the document against which overages are approved and completion is judged.

### Standard Capabilities

Mature products commonly add the machinery that makes the core loop practical at production scale:

- **Coding structure controls** — sub-accounts, location and episode codes, and free-field tags that let one production's books be sliced by unit, episode, or site; some productions require every transaction to carry a location/episode code, others allow shared coding.
- **Approval workflows** — configurable chains for purchase orders, invoices, timecards, and payments, matching who may commit the production to spend.
- **Payment execution** — cutting checks, ACH transfers, and vendor payment batches from the books.
- **Bank reconciliation and trial balance** — the standard close disciplines, with the trial balance accompanying the cost report as the summary of all ledger accounts.
- **Effective-date and change discipline** — budget and EFC changes are made as dated, reasoned entries rather than silent overwrites (see Important Rules).
- **Multi-budget structures** — one budget per episode or location, reported separately or rolled up.
- **Chart mapping** — mapping the production's own accounts to another chart (a studio's format, a tax-credit report's categories) so the same books can speak to different audiences.
- **Report templates and exports** — saved report configurations, PDF/Excel/CSV output, drill-down from report line to account to ledger to source transaction.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Budget of record
Implementations:  built in-product, imported from a dedicated budgeting tool,
                  standardized industry budget forms (commercials)

Concept:  Payroll as coded cost
Implementations:  payroll processed in the same platform, payroll processed by a
                  bundled service company, payroll logs imported from outside

Concept:  Cost report
Implementations:  editable in-app grid, generated PDF/XLSX deliverable,
                  side-by-side budget sheets in a spreadsheet-based tool
```

A reader who has only seen one implementation should still be able to recognize the others from the core model.

## How It Works

### Set up the production and its books

```text
Create the production
→ establish the chart of accounts (or import/apply a standard one)
→ set coding requirements (sub-accounts, location/episode codes)
→ set up bank accounts and payment methods
→ build or import the budget onto the account structure
→ lock the approved budget
```

Setup decisions — whether sub-accounts are required, whether locations are enforced, how many budgets exist — shape every later transaction.

### Commit and spend

```text
Need arises → raise a PO → route for approval → approved PO commits the money
→ vendor delivers → invoice arrives → matched/coded to the PO and account
→ routed for approval → payment issued (check / ACH)
```

Parallel channels feed the same books: petty cash is issued to crew and documented with receipts; purchase-card charges are imported and coded; crew submit timecards and expense claims. Every channel ends in the same place — a transaction coded to a budget account.

### Payroll enters the books as coded cost

```text
Crew work → timecards submitted and approved
→ hours calculated to gross pay under the applicable union or non-union rules
→ fringes and employer contributions computed
→ payroll funded → payroll cost posted to the ledger as coded invoice lines
   (wages, fringes, and distributions split across the accounts they belong to)
```

Whether payroll is processed inside the platform, by a bundled payroll service, or imported from an external provider, the accounting result is the same: payroll lands in the books as coded cost lines the cost report can compare to the labor budget.

### Run the cost report loop

```text
Close the week's transactions (post, code, reconcile)
→ generate the cost report: per account — actuals to date, POs, ETC, EFC, budget, variance
→ accountant reviews each account, updates ETC/EFC where the picture has changed
→ changes recorded with effective date and reason
→ overages beyond budget routed for approval; approved overages folded into total budget
→ report exported and delivered to producers / studio / financiers
→ repeat next week until wrap
```

This loop is the operating heartbeat of the Type. The EFC is a living number: it starts at the approved budget, moves as actual costs and estimates land, and converges on the true final cost as the production completes.

### Wrap and close

```text
Final costs posted → final cost report issued
→ accounting periods closed → books archived with the production's records
→ wrap reporting (final cost, incentive summaries, stakeholder deliverables)
```

The production's books are then complete: a temporary entity's full financial history, from approved budget to final cost.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Budget / EFC grid

The plan-of-record surface: accounts as rows (with header/sub-account hierarchy), budget columns, ETC/EFC columns, actuals alongside. Editable cells for estimates where the user's role and the budget's lock state allow; filters by period, effective date, location/episode; zero-dollar accounts suppressible.

### Cost report generator

Where the weekly deliverable is produced: choose report type (summary / detail / episodic variants), period and date filters, account ranges, coding filters; configure columns (actuals, POs, ETC, EFC, budget, variance, percent complete); save templates; preview; export as PDF/Excel/CSV for stakeholders.

### Chart of accounts explorer

The account structure as a navigable tree: expand headers to sub-accounts, see budget/actual/commitment figures per account, open an account's ledger, drill from a ledger line to its source transaction; export the structure.

### General ledger

The book of record as a searchable, filterable surface: all posted transactions by account, date, coding tags; supports corrections via journal entries and reversal; the audit trail for every figure in the cost report.

### Transaction queues

Work surfaces per cost channel — accounts payable (invoices, approvals, payment batches), purchase orders (open/committed), petty cash, card transactions, payroll invoices (review, split/merge distributions, post). Each queue's job is the same: get a real-world cost correctly coded into the books.

### Approval queues

Pending commitments and payments awaiting the authorized approver, with backup documentation attached and an activity record of who approved what.

### Reports dashboard

The library of standard and saved reports — cost reports, trial balances, GL reports, payroll registers, incentive summaries — with templates and export options.

### Settings

Chart of accounts maintenance, coding types, bank accounts, approval workflow configuration, roles and permissions, accounting-period controls.

## Important Rules / Behaviors

### Every cost must be coded

A transaction is not complete until it carries its account (and, where required, sub-account and location/episode code). Coding discipline is the link between the real world and the budget; products enforce it with required fields, default codes for uncoded imports, and enforced-location modes where every transaction must name its budget.

### Budget and EFC changes are controlled events

Changing the budget or the estimate is not a silent edit: changes carry an effective date and a reason, and the change history is reviewable; some products additionally require later changes to be dated on or after earlier ones. Budgets may be locked so the approved plan cannot drift informally; overages above budget are typically entered only once approved, and the EFC is updated to reflect them.

### POs commit before invoices exist

The purchase order is a commitment that appears in cost reporting before any vendor bill arrives. Cost reports therefore show committed spend (open POs) separately from posted actuals — a production can be over-committed while looking under-spent if POs are ignored.

### The EFC is maintained, not computed

Actuals and POs are computed from transactions; the estimate-to-complete is the accountant's judgment, recorded per account. ETC and EFC move together (changing one updates the other in mature products), and the EFC's credibility with financiers depends on the discipline of the dated, reasoned change record behind it.

### Periods close

Accounting periods are closed as the production proceeds; closed periods are not casually reopened, preserving the integrity of reported weeks. This is what makes a weekly cost report a statement rather than a draft.

### Payroll cost is split, not lumped

Payroll posts to the books as distribution lines — wages, fringes, and employer costs allocated to the accounts and departments they belong to — so labor variance is visible per account, not just in total.

### Permissions follow financial authority

Who may enter transactions, approve commitments, edit budgets or EFC, post to the ledger, and close periods is role-controlled, because each of these actions is a financial commitment of the production.

## Variants

- **All-in-one platform** — accounting and entertainment payroll in one product; payroll posts natively to the ledger (the dominant modern shape among platform vendors).
- **Payroll-service-bundled accounting** — a payroll company provides the accounting software alongside its payroll service, with an automated payroll feed into the books.
- **Standalone budgeting-and-actualizing tool** — spreadsheet-based budgeting with cost logs (POs, petty cash, payroll) and side-by-side original/running/actual comparison; no full ledger; common in the commercial and music-video world where standardized industry budget forms dominate.
- **Feature/one-off vs episodic** — a single budget vs one budget per episode with season-level rollup reporting.
- **Scripted film/TV vs commercial** — house chart of accounts vs standardized industry budget forms and line numbering; bidders and executive producers as additional user roles.
- **Union vs non-union depth** — the weight of payroll machinery (hours-to-gross rules, fringes, guild contributions) varies with the labor regime of the production.
- **Regional/international** — multi-currency books, local payroll regimes, and tax-incentive coding and reporting where productions chase regional credits.
- **Deployment** — cloud SaaS is dominant; desktop/Excel-substrate tools persist where the budget-form tradition is strong.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Accounting Software | adjacent | generic books of a going concern (revenue, receivables, company-wide chart); no production-bounded budget-of-record or cost-report loop |
| Payroll System | complementary | executes pay (taxes, pay stubs, union rules); its cost output lands in production accounting's books; payroll execution is commonly bundled but is not the defining core |
| Film Production Management | adjacent | manages the production's operational side (schedules, breakdowns, call sheets, crew logistics); no books, no budget-vs-actual loop |
| Production Scheduling / Call Sheet Application | adjacent | shoot-day logistics are the object world; money appears only as context |
| Budgeting & Forecasting Platform | different unit & rhythm | plans and forecasts for an ongoing enterprise over fiscal cycles; production accounting controls a temporary project's spend against one approved budget on a weekly loop |
| Expense Management Platform | narrower | employee expense reimbursement is one input channel here; production accounting is the whole books-plus-control-loop |
| Construction Cost Management | analogous structure | same budget-vs-actual job-costing shape over a different object world (contracts, commitments, progress billing on construction projects) |

The most important boundary is with generic accounting software: both have ledgers, invoices, and bank reconciliation. What makes this a distinct Type is that the books exist to hold a temporary production's spending against its own approved budget, and the system's central recurring output is the cost report — not financial statements of a continuing business.

## Representative Products

- **GreenSlate** — all-in-one cloud platform for production accounting and entertainment payroll
- **Wrapbook** — production payroll and accounting platform (Production Accounting Suite)
- **MediaWeb (Media Services / Cast & Crew)** — SaaS production accounting bundled with a payroll service
- **Hot Budget (Hot Bricks)** — standalone budgeting-and-actualizing tool for commercials, promos, and music videos

Movie Magic Budgeting (Entertainment Partners) is the long-standing budget-authoring standard that these platforms import budgets from; it represents the neighboring budgeting capability rather than the accounting core.

## Sources

Research date: **2026-09-09**

- GreenSlate — product page https://greenslate.com/film-production-accounting ; Help Center https://helpcenter.greenslate.com/en/ (Budget Tracking collection: Chart of Accounts, Cost Report, Budget Options articles)
- Wrapbook — product page https://www.wrapbook.com/platform/production-accounting ; Help Center https://help.wrapbook.com/ ("About production accounting", "About Budget/EFC (PAS)", "Cost reports (PAS)")
- Media Services — https://www.mediaservices.com/payroll-tools/mediaweb-production-accounting-software/
- Hot Budget — https://hotbudget.com/overview/ , https://hotbudget.com/feature/

> Sourcing limitations: Entertainment Partners' Movie Magic Budgeting product pages were unreachable during research (404/empty responses); its role is evidenced through import documentation at GreenSlate and Wrapbook. MediaWeb's documentation was reachable only at product-page depth, so claims about it are limited to its published feature list. Precise vendor-specific limits, defaults, and module names are intentionally not stated in this document; they remain in the Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
