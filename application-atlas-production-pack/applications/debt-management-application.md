# Debt Management Application

## Overview

A **Debt Management Application** is a person-side application for getting out of debt. It holds a person's own debts as individual liability records, builds a repayment plan that allocates a stated repayment capacity across those debts, and tracks actual repayment against that plan until each debt is retired.

The defining core is small:

```text
The user's own debts as liabilities of record
└── A repayment plan over those debts (order + allocation of repayment capacity)
    └── Repayment tracked against the plan
        (payments recorded → balances updated → progress surfaced → plan adjusted)
```

Everything else commonly associated with the category — named payoff strategies like "snowball" and "avalanche", month-by-month schedules, what-if scenarios, reminders, bank sync, credit-score features, or administration by a counseling agency — is a widespread realization of one of these three structures or a layer around them, not part of what makes the application what it is. A person with a paper ledger, a written payoff order, and a payment log is doing the same job; a spreadsheet that only prints a schedule is doing less (and is recognizably a calculator, not a debt management application).

The user is always the debtor. When the system's subject is other people's debts being pursued by an organization, the product belongs to a different family entirely (collection and servicing software).

## Users & Context

The primary user is an individual — or a household acting as one — carrying several debts (typically credit cards, personal or student loans, medical bills) who wants a single place to see all of them, decide what gets paid off in what order, and stay on course until done.

Typical situations:

- juggling multiple debts with no clear sense of when each will be paid off
- having a fixed amount available per month for debt payments and wanting to know where it should go
- having just paid off one debt and wanting the freed payment redirected to the next
- wanting to see the effect of a windfall payment, an extra monthly amount, or a tighter month

Two working postures exist. In the self-directed posture, the person runs the plan alone: they enter their own numbers, choose or compose an ordering, and record each payment. In the program-mediated posture, a credit counseling agency administers a debt management program: the person enrolls, deposits one consolidated payment (often with negotiated interest concessions), and uses the application to track the program's progress — the plan is agency-structured rather than self-composed.

There are no organizational roles. Where an agency is involved it is an external party; the person remains the first party whose debts these are.

## Core Model

### The defining core

**1. The debts of record.** Each debt is a persistent, individually addressable record: who is owed, the current balance, and the payoff-relevant terms — the interest rate and the minimum payment. Debts can be of many kinds (credit cards, loans, medical bills — anything with a balance and a payment). This record is what makes the application about debt *management* rather than about spending: an expense is a past event, a debt is a living liability with a retirement date to be engineered.

**2. The repayment plan.** The plan is the organizing object. It has two inputs and one output:

- the debts of record,
- the **repayment capacity** — one stated amount available per month (the sum of the minimums plus whatever extra the person can afford),
- the **ordering** — which debt is targeted with the extra payment first, and where each freed payment goes next.

The plan's output is a schedule: for each debt, when it will be paid off; for the whole, a projected debt-free date and total interest. The ordering may be a named strategy (lowest balance first, highest interest first, cash-flow-oriented, or fully custom) or an agency-structured allocation; conceptually it is the same thing — a rule that decides where the next dollar of extra payment goes.

**3. The tracking loop.** Payments (or program deposits) are recorded as they happen. Recording updates the debt's balance and due date, advances the schedule, and moves the progress picture: which debts are paid off, how far along the active ones are, and how the projected completion date has moved. The plan is then adjusted — the ordering can be changed, the capacity revised, extra or reduced payments recorded — and the loop repeats monthly until nothing is left.

All three are needed together. A calculator without payment recording and progress is below this Type; a liability list without a plan is a net-worth view; a schedule without the debts behind it is a generic planner.

### Standard capabilities of mature products

Mature products commonly add, around that core:

- **strategy selection and comparison** — pick a named payoff order, switch between them, and see them compared side by side on the user's own debts;
- **a month-by-month plan table** — payment, interest, and running balance per debt per month, showing how the freed payment rolls forward as each debt retires;
- **payment history** — a durable record of payments (and purchases on the debt) per account;
- **what-if scenarios** — extra one-off payments (a tax refund, a bonus) and revised monthly amounts applied to the plan;
- **progress views** — paid-off debts, percentage complete, visualizations, snapshots over time;
- **due-date awareness** — a payment calendar so scheduled payments are not missed, with reminders in some products;
- **breadth of debt types** — anything with a balance and a payment; some products add support for deferred or promotional-rate accounts, and the ability to exclude an account from the plan.

### One structure, several realizations

The core is conceptual; products realize each part differently:

```text
Concept:   repayment capacity
Realized as:  a monthly "budget" amount, a total monthly payment input,
              a fixed program deposit

Concept:   ordering rule
Realized as:  named strategies (balance-first, rate-first, cash-flow, custom),
              a user-ranked order, an agency-structured disbursement plan

Concept:   payment recording
Realized as:  manual payment entry, a program deposit to an agency account,
              a printed schedule ticked by hand (the thin pole)
```

Whether the product connects to banks or works entirely on manual entry is a posture choice, not part of the model — some products deliberately require no bank login at all.

## How It Works

### Set up: debts and capacity

```text
Create an account (or open a worksheet)
→ enter each debt: creditor, balance, interest rate, minimum payment
→ state the monthly repayment capacity
```

Entry is usually manual; products that avoid bank connections emphasize that no account numbers or credentials are collected. This step is short by design — the subject is debts, not the whole financial life.

### Generate the plan

```text
Choose an ordering (strategy or custom, or accept the agency-structured plan)
→ the schedule is computed
→ inspect: payoff date per debt, total interest, projected debt-free date
→ compare alternative orderings; adjust the capacity
```

The comparison step is where the strategy machinery lives: the same debts and capacity, evaluated under different orderings, showing the trade-offs (earliest first win vs least total interest) on the user's own numbers.

### Execute monthly

```text
Pay per the schedule
→ record the payment (full, partial, or extra)
→ balances and due dates update; the schedule advances
→ progress is surfaced: paid off / remaining / projected date
→ adjust: switch strategy, add a windfall payment, revise the capacity
```

When a debt retires, its freed minimum plus any extra rolls onto the next target — the rollover mechanic every realization shares, whatever it calls itself. Recording is deliberately tolerant of real life: extra payments beyond the schedule, purchases that grow a balance again — and, in some products, partial or skipped months and deferred accounts that start paying later.

### Completion

Debts progressively move to paid-off; the schedule shortens; progress views mark debts retired and the remaining path. The end state — a projected debt-free date that keeps moving closer — is the product's central feedback loop.

## Interfaces

### Debt account list

The inventory of debts of record.

- typical information: creditor/name, balance, interest rate, minimum payment, due date, target order
- primary actions: add / edit / remove a debt, exclude one from the plan, view its detail

### Plan / schedule view

The month-by-month rendering of the repayment plan.

- typical information: payment per debt per month, interest per month, running balance, current-month position, projected payoff dates
- primary actions: change ordering/strategy, compare strategies, export or print the schedule

### Dashboard / progress

The standing answer to "how am I doing?".

- typical information: projected debt-free date, total interest paid or saved, debts paid off, progress on active debts, capacity vs actuals
- primary actions: record a payment, add a one-off extra payment, adjust the monthly amount

### Payment entry / history

- typical information: recorded payments and purchases per account, by month
- primary actions: record payments (full, extra, or partial in some products), view or export history

### Calculator surface

Some products offer an entry-point calculator usable without an account: enter debts and capacity, see a plan and a debt-free date, then save it into a full account. This is the same model with the persistence leg switched off.

### Client portal (program-mediated variant)

In a counseling-administered debt management program, the person's surface is a portal: the program's payment schedule and progress, deposit records, and access to counselor support. The person deposits rather than pays; the plan itself is administered.

## Important Rules / Behaviors

### The rollover rule

The plan's engine is rollover: when a debt is retired, the payment that used to go to it (minimum plus extra) is applied to the next debt in the ordering. The total monthly outlay stays constant while the extra payment on the current target grows. This single rule is what makes the schedule accelerate, and it is shared across realizations that otherwise have nothing in common.

### The snowball amount is calculated, not typed

The extra payment (the "snowball") is derived — capacity minus the sum of minimums. Changing it means changing the capacity or the minimums; products enforce this rather than letting the two drift apart.

### Balances move in both directions

Real debts are not one-way: purchases land on credit cards again, a month can be short-paid or skipped, an account can be deferred. A debt management application records these and recomputes; a tool that assumes only downward balances will desync from reality quickly. (One documented caveat of static spreadsheets: they typically assume a fixed minimum payment, so credit-card minimums that shrink as balances fall must be updated by hand.)

### Payments update state immediately

Recording a payment adjusts the balance, the due date, and the schedule in the same motion. The record and the plan are one system — this coupling is what separates the Type from a calculator whose output is a snapshot.

### Concessions are program facts, not user controls

In the program-mediated variant, interest reductions depend on creditor participation and are negotiated by the agency; they are never guaranteed and vary per creditor. The person's controllable inputs are the deposit and their own adherence, not the terms.

### Manual-entry privacy posture

Some products deliberately hold no bank connections — all figures are user-entered. Where integration exists (for example, syncing with a budgeting product), it is an add-on bridge, not the data foundation.

## Variants

- **Self-directed planner/tracker** — the canonical form: person enters debts, picks an ordering, records payments; strategies and what-ifs are first-class (e.g. Undebt.it, PowerPay)
- **Spreadsheet / calculator pole** — plan generation with a printable schedule; the tracking leg is manual (e.g. Vertex42's debt reduction calculator; university-extension online calculators). Thin member at the Type's lower boundary
- **Program-mediated (debt management program)** — a nonprofit credit counseling agency structures the plan, negotiates concessions, collects one monthly deposit and disburses it; the person tracks progress through a client portal (e.g. GreenPath's Debt Management Program). This is the historical industry meaning of "debt management"
- **Mobile-first tracker apps** — app-store payoff trackers with similar structure optimized for phone use; also round-up/micro-payment automation apps that act on debts rather than only tracking them. Market shape noted; operational details not verified this pass
- **Budgeting-embedded debt payoff** — personal finance products that include debt-payoff features among broader functions. Boundary zone: where budgeting is the organizing object and debts are one account class, the product is a budgeting application with debt features
- **Professional use** — advisors and counselors running the same structure on behalf of clients (commercial licenses; agency-administered programs)

A variant remains a variant unless it changes the user, the core objects, or the workflow — for example, an application whose subject is debts the organization is *owed* would no longer fit this Type at all.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Budgeting Application / Personal Finance Management | same person, different organizing object: allocating income across spending categories vs engineering the retirement of liabilities; debt payoff may appear there only as a feature |
| Net Worth Tracker | liabilities as one snapshot figure in a whole-asset picture; no payoff plan or tracking loop |
| Expense Tracking Application | records past spending events; debts here are living liabilities with terms and a retirement schedule |
| Debt Collection Management / Collections Platform | organization-side systems over debts *owed to* clients or the organization — the opposite side of the table; agency objects (creditor clients, placements, commissions) have no counterpart here |
| Loan Management System / Mortgage Servicing Platform | lender- or servicer-side records of loans they own or service; the person here is the borrower, not the holder of the loan |
| Credit Management Platform | seller-side trade credit extended to business customers; commercial relationships, not personal liabilities |
| Loan Origination / Consumer Lending Platform | creating new loans; this Type manages the repayment of debts that already exist |

Two adjacent *services* (not application Types in the directory) are worth separating: **debt settlement** (negotiating a reduced lump-sum payoff — a different intent, paying less than owed) and **debt consolidation loans** (replacing several debts with one new loan). A debt management application plans and tracks repayment of existing debts in full; the program-mediated form's own materials draw these lines explicitly.

## Representative Products

- **Undebt.it** — free web-based debt payoff planner and tracker; snowball/avalanche/custom orderings, payment recording, snowball table, progress snapshots; manual entry, no bank login
- **PowerPay** — Utah State University Extension's free, account-based self-directed debt elimination tool; long-running, education-oriented
- **GreenPath Debt Management Program** — nonprofit credit counseling debt management program with a secure client portal; the program-mediated realization of the same core
- **Vertex42 Debt Reduction Calculator** — widely used Excel/Google Sheets debt snowball calculator; the spreadsheet thin pole (plan + printable schedule)

The core model was checked against the program-mediated form and the spreadsheet form to avoid over-fitting the definition to the modern self-directed app pattern.

## Sources

Research date: **2026-09-08**

- Undebt.it — home, "How Undebt.it Works" tour, FAQ & Help Center — https://undebt.it/ , https://undebt.it/how-undebt.it-works.php , https://undebt.it/faq.php
- PowerPay (Utah State University Extension) — landing and how-to pages — https://extension.usu.edu/powerpay/ , https://extension.usu.edu/powerpay/how-to.php
- GreenPath Financial Wellness — Debt Management Program page — https://www.greenpath.com/debt-management-plans/
- Vertex42 — Debt Reduction (Snowball) Calculator — https://www.vertex42.com/Calculators/debt-reduction-calculator.html

> Sourcing limitation: official documentation for mobile-first payoff apps, round-up/automation apps, and PFM-embedded debt features could not be fetched this pass (app-store listings unreachable; several candidate products defunct or parked; one major counseling agency's site returned access errors). Claims about those variants are therefore kept generic; precise feature, fee, and timeline figures stated by individual vendors were not carried into this document. Product-by-product observations and the cross-product comparison matrix are recorded in the paired Research Notes.
