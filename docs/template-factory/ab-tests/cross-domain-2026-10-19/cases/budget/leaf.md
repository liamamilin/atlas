# Budgeting Application

## Overview

A **Budgeting Application** helps a person or household decide in advance how much money may go to which purposes over a defined period, and then continuously measures actual spending against those decisions.

The defining core is small:

```text
Spending plan (a budget bound to a period)
└── Allocations: planned amounts assigned to purposes within the plan
    └── Actuals: spending captured in the app, feeding the comparison
        └── Comparison state: planned vs actual vs remaining ("what's left?")
```

Everything else commonly associated with budgeting products — bank connections, account balances, auto-categorization, envelope terminology, budgeting methods such as zero-based or 50-30-20, savings goals, reports — is widespread in current products but is not what makes a product a budgeting application. A product with no bank links and no account tracking at all can be a complete budgeting tool; what it cannot lack is the plan and the running answer to "how much do I have left?"

When the center of gravity shifts from the plan to the classified record of what happened, the product is an Expense Tracking Application; when it shifts to the consolidated picture of accounts, balances, and net worth, it is a Personal Finance Management Application.

## Users & Context

The primary user is an individual or a household — couples and families commonly share one plan — who wants to make spending decisions against a commitment rather than against a running balance. Typical moments of use:

- **at the start of a period** — drafting or refilling the plan: how much for groceries, rent, transport, fun, savings
- **when income arrives** — assigning the newly available money to purposes before it is spent
- **before a purchase** — checking an allocation's remaining amount ("can I afford this within the plan?")
- **during review** — seeing which allocations are running out or overspent, and moving money to fix the plan
- **at period end** — closing the period, optionally carrying unspent amounts, and starting the next plan

A secondary user is the shared partner or family member who records spending into the same plan. The context is personal money: the spender and the planner are the same party, and no approval or reimbursement flow exists — that is the corporate spend-management world, not this one.

## Core Model

### The Defining Core

Four properties. If any one is removed, the product is no longer recognizable as a budgeting application:

- **Spending plan bound to a period** — the plan is the organizing object. It exists for a defined time scope: a recurring period (most commonly a month) or a one-off window (a project, event, or year). Without a period, there is no plan to live within.
- **Allocations** — planned amounts assigned to purposes inside the plan: "this much for food, this much for rent, this much for the car fund." Allocations are the plan's substance. Without them, the product is a wish list or a forecast, not a budget.
- **Actuals in the app** — spending is captured or recorded in the application, at whatever grain the product offers (a simple expense entry or a full categorized transaction). Actuals are what make the plan a live tool instead of a note.
- **Comparison state** — the application continuously shows where actuals stand against allocations: remaining, left to spend, overspent, funded or unfunded. This is the state users consult before spending. Without it, the plan never meets reality.

### One Structure, Many Implementations

The core model is conceptual. Mature products realize each concept differently, and the differences do not change the Type:

```text
Concept:          Spending plan for a period
Implementations:  monthly plan, annual plan, event/project budget, dated goal window

Concept:          Allocation container
Implementations:  envelope, spending category with a budget, fixed/flexible bucket,
                  plan line item, auto-generated planned-spending amount

Concept:          Actuals
Implementations:  manually entered expense, imported transaction,
                  bank-synced and auto-categorized transaction, scheduled entry

Concept:          Comparison state
Implementations:  planned / actual / remaining columns, envelope balance,
                  "left to spend" figure, per-day spending allowance, funded/overspent flags
```

Two implementation choices deserve note because they are frequently mistaken for the definition:

- **The envelope is not the Type.** Envelope budgeting — allocation containers whose balances carry forward — is one popular implementation of the allocation concept. Other products implement the same concept as category budgets, flexible-spending buckets, or auto-computed plan amounts with no envelope anywhere.
- **The budgeting method is not the Type.** Zero-based assignment ("give every dollar a job"), envelope refilling, 50-30-20 ratios, and auto-generated spending plans are philosophies about *how the plan gets drafted*. Several mainstream products explicitly accommodate all of them in one tool. The Type requires a plan; it does not require any particular doctrine for drafting one.

### Standard Capabilities

Capabilities commonly found in mature budgeting products. They make the plan practical but do not define the Type:

- **Income anchoring** — the plan is normally built against expected income for the period: expected income minus planned expenses and savings, with products showing whether the plan is balanced or whether allocations exceed income.
- **Unallocated money** — several products compute and display the money not yet assigned to any purpose (named variously across products). It is derived from account money, income, and allocations — not edited directly.
- **Accounts as optional containers** — many products connect or track accounts (checking, cash, cards) so actuals arrive automatically and balances stay honest; others work entirely from manual entries with no account layer. Accounts can be inside or outside the plan (savings goals and long-term tracking often sit outside day-to-day allocations).
- **Goals and sinking funds** — setting aside an amount each period toward a future expense: annual bills (car maintenance, holidays), save-up goals with target dates, debt pay-down goals.
- **Recurring and scheduled entries** — bills and subscriptions known in advance, often separated from flexible spending so the plan shows committed money first.
- **Rollover** — optionally carrying an allocation's unspent remainder into the next period, per allocation or per product policy.
- **Plan setup assistance** — auto-drafting the plan from income and bills, or pre-filling allocation amounts from recent spending history, for the user to review and edit.
- **Overspending states** — the remaining figure can go negative; products differ in whether a shortfall stays with the allocation, is covered by moving money from elsewhere, or is excluded from the comparison.
- **Transfers and credit-card payments** — money moved between one's own accounts, and payments onto one's own cards, are treated specially so they are not counted as spending; credit-card balances commonly set aside a payment amount inside the plan.
- **Non-monthly budgets** — annual or event-based plans (a year of holiday spending accumulated monthly; a wedding or renovation project) alongside the recurring period.
- **Reports** — plan-versus-actual analytics over time: spending by allocation, trends, comparisons across periods.
- **Sharing** — household plans shared between partners or family members, with joint recording of actuals.
- **Alerts and reminders** — notifications when allocations run low, when bills fall due, or when the plan needs attention.

## How It Works

The recurring loop of a budgeting application is: **plan → fund → spend → compare → adjust**.

### 1. Draft the plan

```text
Choose the period (monthly is the common default; project/annual plans are variants)
→ create allocations for the period's purposes
→ anchor on expected income
→ check that planned amounts do not exceed available income
```

Drafting can be manual (the user writes every allocation), assisted (the product pre-fills from income and bills or from recent spending averages), or auto-generated (the product computes a whole-plan spending allowance). In every case the user can review and change the numbers — the plan remains the user's decision.

### 2. Fund the allocations

When money arrives, it moves from "unallocated" into the plan:

```text
Income received (or money already available)
→ assign it to allocations (directly, or via a refill routine that tops up each allocation)
→ unallocated remainder shrinks; allocation balances grow
```

Method-driven products make this an explicit, deliberate act on every payday ("every dollar gets a job"); auto-plan products perform it continuously and show the resulting "left to spend" state instead. Some products schedule refills to post automatically each period.

### 3. Capture actuals

```text
Spend money
→ record the expense (manual entry) or capture it (bank import/sync)
→ assign it to the allocation it belongs to (manually or via auto-categorization)
→ the allocation's remaining amount drops
```

The actuals layer can be as thin as a list of entered amounts or as rich as a categorized transaction register with payees and schedules. Scheduled and imported actuals may land as "pending" until the user confirms and assigns them, keeping the comparison honest.

### 4. Consult the comparison

Before spending, the user checks the plan: how much remains in the relevant allocation, what is left overall, what remains per day or per week. This is the moment the product exists for — the plan changing the spending decision.

### 5. Adjust and recover

```text
Allocation running out → move money from another allocation (or accept the shortfall)
Plan no longer realistic → edit allocations mid-period; the plan is a living object
Unexpected income → add allocations or build cushion
```

Editing the plan mid-period is normal, not an exception. Method philosophies differ in how much ceremony surrounds it, but no product freezes the plan.

### 6. Close the period

At period end the comparison is final for that period and a new one begins from the plan's template figures. Unspent amounts stay behind unless rollover is enabled for an allocation; goals and annual plans keep accumulating across periods.

## Interfaces

The following surfaces are described in conceptual terms; names and layouts vary by product.

### Plan / budget page

The product's home surface.

- the list of allocations for the current period with planned, actual, and remaining amounts (some products compress this to a single flexible-spending figure plus committed bills)
- the plan's anchor: expected income, committed bills, unallocated remainder
- primary actions: edit allocation amounts, create allocations, move money between allocations, navigate periods

### Fill / assign surface

The allocation loop as an explicit action (where the product makes it one).

- unallocated money and the allocations to fund
- where the product makes funding an explicit routine, it typically offers per-allocation amounts (with optional rollover of leftovers) or a top-up toward each allocation's budgeted figure; scheduled refills in some products
- primary actions: assign money to allocations, schedule the refill, confirm

### Transaction / entry list

The actuals layer.

- dated expense and income entries (categorized transactions where the product has accounts), each bound to the allocation it hit
- pending states for imported or scheduled items awaiting confirmation/assignment
- primary actions: add entry, assign or reassign to an allocation, split, schedule, match duplicates

### Accounts page (where present)

- account balances, on-plan and off-plan accounts, connection status
- primary actions: add/connect accounts, reconcile, set starting balances
- absent entirely in plan-only products, without loss to the budgeting core

### Goals

- save-up and pay-down goals with target amounts and dates, and the per-period set-aside derived from them
- primary actions: create goal, commit money, track progress

### Reports

- plan-vs-actual over time, spending by allocation or group, trends across periods
- primary actions: choose period, filter, export

### Settings

- period start and length, category/allocation structure, exclusions from the plan, sharing partners, alerts

## Important Rules / Behaviors

### The comparison state is visible before spending

Unlike many record-keeping tools, the budgeting app's key output is a *forward-looking* permission surface: the remaining amount of an allocation is the number the user consults to decide whether to spend. Products surface this at the point of decision — an envelope balance, a left-to-spend figure, a per-day allowance.

### Unallocated money is computed, not typed

Where the product exposes an unallocated figure (money with no job yet), it is derived from account money, income, and existing allocations. Users change it indirectly — by recording income, filling allocations, or moving money back out of allocations. A negative unallocated figure means the plan promised more than the money available.

### Overspending is a first-class state

Actuals can exceed an allocation. Products handle the shortfall differently — the allocation's remaining amount goes negative, other allocations can cover it, or the user can exclude the spending from the comparison — but the comparison must be able to represent failure, not only success.

### Transfers between one's own accounts are not spending

Moving money between one's own accounts, and paying one's own credit card, must not consume allocations. Mature products either special-case these as transfers or exclude their categories from the plan; card spending is planned, and the payment onto the card is handled so it is not double-counted (in some products by reserving a payment amount inside the plan). Debt being paid off is commonly kept outside the plan's spending entirely.

### The plan is a living object

Allocations can be edited, added, and removed at any time, including mid-period; imported transactions may await assignment before they count. The plan's history persists period by period, so past plans remain inspectable.

### Period boundaries matter

A new period starts from the plan's configured amounts, not from whatever was left behind — unless rollover is enabled for an allocation. Annual and goal allocations deliberately straddle periods, accumulating a set-aside each period toward a future expense.

### No ledger semantics

Allocations are plan labels, not ledger accounts: no double-entry posting, no chart of accounts, no financial statements. The product answers "what am I going to do with my money and how am I doing?", not "what are my books?"

## Variants

Common shapes of the Type. A variant stays a variant unless it changes users, objects, or rules so much that the core model no longer applies:

- **Envelope-method products** — allocation containers with balances that carry forward; refill routines each period; strongly method-driven onboarding (a digitized version of cash-envelope budgeting).
- **Zero-based assignment products** — the plan must allocate all available money on receipt; the unallocated figure is the thing to drive to zero; heavy emphasis on the assignment loop.
- **Auto-plan products** — the product generates the spending plan from income, bills, and history, and maintains a computed "left to spend" state; the user adjusts rather than authors. Often method-agnostic, accommodating envelope- or zero-based styles on request.
- **Flex-bucket products** — instead of a budget line per category, a small number of buckets (committed bills, fixed costs, flexible spending, non-monthly), tracking the flexible figure only.
- **Minimal plan-list products** — no accounts, no bank links, no auto-categorization: just planned entries and actual entries and the "what's left" difference, for one period or one project at a time.
- **Project / event budgets** — the same core applied to a single-purpose window (wedding, renovation, holiday), often as a separate plan alongside the recurring household plan.
- **PFM-bundled budgeting** — the plan as one module inside a broader personal-finance product that also holds accounts, net worth, and investments. The budgeting module still centers the plan; the bundle does not change the core.
- **Shared household plans** — one plan jointly edited by partners or family members.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Expense Tracking Application | record-first: the classified log of what happened is the center, and aggregation answers "where does my money go?"; a budget is an optional comparison layer over the record. Budgeting is plan-first: the allocation is the center, and the record feeds the plan-vs-actual comparison. A plan-only product with no record layer is still budgeting; a record-only product is still expense tracking |
| Personal Finance Management Application | whole-picture money overview (accounts, balances, income/spending, net worth, investments) is the center; the plan is one view. A PFM without accounts is not a PFM; a budgeting app without accounts still exists |
| Budgeting & Forecasting Platform (corporate) | organization-side budget cycles: departments, forecast versions, rollups, variance analysis over business performance — different actors and objects entirely |
| Public Budgeting Platform (government) | public-fund appropriations and government fiscal planning — a different domain, not a consumer variant |
| Accounting Software / Bookkeeping Application | books semantics: chart of accounts, balanced double-entry posting, financial statements, tax readiness. Budgeting has allocations, not ledger accounts |
| Net Worth Tracker | position (assets minus liabilities at a point in time) vs plan (allocations over a period); overlap only where products bundle both |
| Expense Management Platform | organization-side employee spending: expense reports, approvals, reimbursement — corporate context, not a personal plan |
| Digital / Mobile Banking Application | a bank app's budgeting view is a capability of one account relationship; the standalone Type plans money regardless of where it is held and survives independently of any bank |
| Debt Management Application | payoff scheduling is the central object there; inside budgeting, debt pay-down appears as a goal or allocation, not as the system's center |
| Retirement Planning Application | long-horizon projection of future finances vs period-scoped spending plan |

The boundary with **Expense Tracking Application** is the most important one, because the two Types overlap on records: mature budgeting apps keep transaction registers, and many expense trackers include budgets. The structural difference is which object is the center — the allocation the record is measured against, or the record itself with its classification and aggregation.

## Representative Products

- **YNAB** — zero-based, method-driven assignment budgeting ("give every dollar a job"); plan/months/categories model with goal machinery
- **Goodbudget** — digital envelope budgeting with a manual core, optional bank sync, household sharing
- **Monarch Money** — sync-first budgeting with a cash-flow framing, auto-suggested plans, category and flexible-bucket modes
- **Quicken Simplifi** — auto-generated Spending Plan inside a broader personal-finance product; explicitly method-agnostic
- **Fudget** — minimal plan-list budgeting with no bank connections and no account tracking

The defining core was checked against pre-software and non-app forms (paper envelope budgeting, kakeibo household ledgers, spreadsheet budgets) and against desktop-era budget modules, to avoid defining the Type by the current sync-first market shape.

## Sources

Research date: **2026-09-06**

- YNAB — API documentation (plans, months, categories, accounts, transactions) and changelog: https://api.ynab.com/
- YNAB — method page: https://www.ynab.com/the-four-rules
- Goodbudget — Help Center: https://goodbudget.com/help/ (incl. Step 1 Add Envelopes, Step 4 Fill Your Envelopes, Step 5 Record Your Expenses, What is Available money?)
- Monarch Money — Help Center, "Creating Your Budget in Monarch": https://help.monarchmoney.com/hc/en-us/articles/360048883631-Creating-Your-Budget-in-Monarch
- Quicken Simplifi — official product page and Spending Plan FAQ: https://www.simplifimoney.com/
- Fudget — official product page: https://fudget.com/

> Sourcing limitations: YNAB's user-facing help center renders only a JavaScript shell and was not usable; YNAB evidence rests on its public API documentation and official method page. EveryDollar and PocketGuard were unreachable (blocked responses) and are treated as market context with no product-specific claims drawn from them. Quicken Simplifi and Fudget evidence is limited to their official product pages. Precise numeric limits, prices, and vendor-claimed figures (e.g. institution-connection counts) are intentionally not stated in this document.

Detailed evidence, product-by-product observations, the cross-product comparison, and the historical / market-sample breadth check are recorded in the paired Research Notes.
