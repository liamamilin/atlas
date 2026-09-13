# Payroll System

## Overview

A **Payroll System** is an employer-operated application that pays people systematically: it holds pay records for each employee, runs a recurring pay cycle, computes each person's pay from gross earnings down to net take-home, issues the payment, and keeps a durable record of what was paid.

The defining core is small:

```text
Employee pay records
└── Recurring pay cycle (pay schedule → pay period)
    └── Pay run (the unit of work)
        ├── Earnings inputs → Gross pay
        ├── − Statutory withholdings
        ├── − Deductions
        ├── = Net pay → Payment issued to the employee
        └── Durable pay records (run register + pay statements + history)
```

Everything else commonly associated with modern payroll — automated tax filing with government agencies, direct deposit, employee self-service portals, time-tracking imports, benefits deductions, accounting sync — is widespread in current products but is not what makes a payroll system a payroll system. Older desktop-era payroll products that computed pay, printed checks, and produced registers and year-end forms for manual filing satisfy the same core without any of those capabilities.

When the primary job shifts to tracking hours (Time & Attendance), managing the employment relationship (HRIS/HCM), planning pay (Compensation Management), or consolidating pay runs across many countries (Global Payroll Platform), the product is drifting toward a different Application Type.

## Users & Context

The primary user is the person responsible for paying the organization's workforce — typically a payroll administrator, bookkeeper, accountant, or (in small businesses) the owner. Their recurring job is to execute each pay run accurately and on time, and to keep the organization compliant with the tax and record-keeping obligations attached to paying people.

Secondary users:

- **approvers / finance owners** — in larger organizations, a second person reviews and approves runs before money moves; permissions commonly separate who can prepare, manage, and approve pay runs
- **employees** — recipients of pay; in modern products they access their own pay statements and tax forms, and often maintain their own personal and payment details
- **accountants / bookkeepers** — consume payroll outputs (registers, journals, year-end forms) for the books and filings

The work context is a strict rhythm: pay must happen on schedule, in correct amounts, with taxes withheld and remitted as required. Errors are costly and retroactive fixes are laborious, which is why review-before-release and durable records are structural, not optional.

## Core Model

### The Defining Core

**Employee pay record.** The anchor object. One record per paid person, maintained by the employer, holding the terms the computation needs: how the person is paid (salary or hourly rate, sometimes multiple rates), how they are paid (bank or other payment instructions), and what must be withheld or deducted on their behalf (tax elections, benefit deductions, court-ordered garnishments). In many products the record also carries jurisdictional context — where the person works — because that determines which statutory rules apply.

**Pay schedule and pay period.** The employer defines one or more recurring pay schedules (for example weekly, bi-weekly, or monthly). Each schedule divides the year into pay periods. The period is the time window for which pay is computed.

**Pay run.** The unit of work. A pay run executes one schedule over one period for a set of employees. It gathers earnings inputs, computes each employee's pay, and — after review — issues payment and writes the records. A run is the thing the operator starts, reviews, confirms, and later looks up.

**Earnings inputs.** What the person earned in the period: salary amounts that recur by default, imported or entered hours multiplied by rates (regular, overtime, double-time), and period-specific items such as tips, commissions, bonuses, paid-time-off taken, or reimbursements. Some items are taxed as income; some (like expense reimbursements) are not.

**Gross-to-net computation.** The system's computational heart. For each employee in the run: gross pay (sum of earnings) minus statutory withholdings — income tax, social insurance, and similar contributions where the jurisdiction requires the employer to withhold them — minus agreed deductions (benefits premiums, retirement contributions, garnishments, repayments) equals net pay. The computation applies jurisdiction-specific rules (rates, brackets, caps, work-location rules) that the product maintains.

**Payment issuance.** Net pay is delivered to each employee through their chosen payment method — bank transfer (direct deposit) is the modern default, with printed checks and other rails as alternatives. The run produces the money movement: a debit of total pay plus withheld amounts from the employer's account, and per-employee payments.

**Durable pay records.** Every run leaves records: a run-level register (who was paid what, and what was withheld), per-employee pay statements (pay stubs showing gross-to-net detail), cumulative year-to-date history, and the year-end summaries derived from that history. These records are the system's memory and the basis for filings, audits, and employee inquiries.

```text
Employee pay record (terms, elections, payment method, work location)
  └── per pay period → Pay run
        ├── Earnings inputs (time / salary / tips / commissions / one-off items)
        ├── Gross pay
        ├── − Statutory withholdings (per jurisdiction)
        ├── − Deductions (benefits, garnishments, agreed)
        ├── = Net pay → Payment issued
        └── Pay records (register + pay statement + YTD history)
              └── accumulates → year-end forms
```

### Standard Capabilities of Mature Products

These are near-universal in current products but are layers on the core, not the core:

- **Automated tax compliance** — the system computes statutory withholdings at run time, then remits and files with tax agencies on the employer's behalf (in full-service products), or produces the reports and forms for the employer to file (in software-only postures). Year-end forms (such as W-2/1099-class documents in the US, or regime equivalents elsewhere) are generated from the accumulated run history and distributed to employees and agencies.
- **Direct deposit** — bank-transfer payment as the default method, with per-employee payment instructions and defined timing between run confirmation and payday.
- **Employee self-service** — employees log in to view pay statements and year-end forms, receive payday notifications, and commonly maintain their own personal, tax-election, and payment details; onboarding flows let new hires enter this data themselves.
- **Time & attendance import** — hours, tips, and commissions flow into the run from a time-tracking source (the product's own module or a third-party application), replacing manual entry.
- **Off-cycle and one-off runs** — payments outside the regular schedule (bonuses, corrections, final pay) executed as separate runs.
- **Review and approval controls** — a pre-release review showing the run's breakdown and the money movement it will trigger; permissions governing who may prepare, manage, and approve runs.
- **Accounting handoff** — payroll expenses and liabilities posted or synced into the organization's general ledger / accounting system.
- **Benefits and deduction administration** — benefit elections and other deductions configured upstream and applied automatically in each run.
- **Reports** — payroll cost reports, registers, and tax-liability summaries.
- **Contractor payments** — paying independent contractors alongside (or instead of) employees, with the corresponding year-end forms.

### One Structure, Many Implementations

The core model is conceptual; products realize it differently:

```text
Concept:  Employee pay record
Implementations:  minimal in-product record (standalone payroll) vs record synced from an HR system

Concept:  Earnings inputs
Implementations:  manual entry, import from own time module, import from third-party time apps, salary defaults

Concept:  Payment issuance
Implementations:  direct deposit, printed check, other bank/app rails

Concept:  Tax compliance
Implementations:  full-service (vendor files and remits, often with error guarantees) vs software-only (reports and forms, employer files)
```

A reader who has only seen one implementation — say, a full-service US cloud product — should still be able to recognize a desktop-era or differently-regulated payroll product from the core model alone.

## How It Works

### One-time setup

Before the first run, the employer configures the system:

```text
Register company / jurisdictions
→ add employees (pay terms, work location, payment method, tax elections, deductions)
→ define pay schedule(s) and pay dates
→ connect inputs (time tracking) and outputs (accounting) as needed
```

In modern products employees often self-onboard: they receive an invitation and enter their own personal, tax, and payment details, which the employer reviews.

### The recurring pay cycle

Each period, the operator executes the defining loop:

```text
Start the run for the schedule's current period
→ confirm pay period and pay date
→ collect earnings inputs
   (import hours/tips/commissions from time tracking, or accept salary defaults,
    or enter manually; add one-off items such as bonuses)
→ system computes gross-to-net per employee
   (gross pay − statutory withholdings − deductions = net pay)
→ review the run
   (per-employee breakdown, totals, changes since last run, the bank debit it implies)
→ adjust if needed (fix hours, edit deductions, add reimbursements)
→ approve / confirm the run
→ system issues payments and debits the employer account
→ employees are notified; pay statements become available
→ run register and history are written
```

The loop repeats every period. Between runs, changes to pay records (raises, new deductions, new hires, terminations) accumulate and take effect in the next run — or in a special off-cycle run when payment cannot wait.

### The compliance loop

Running alongside the pay cycle:

```text
each run withholds statutory amounts
→ withheld amounts are remitted to agencies on the jurisdiction's schedule
   (by the vendor, in full-service products; by the employer, in software-only postures)
→ periodic and annual filings are prepared and submitted
→ at year-end, per-person forms are generated from accumulated history
   and distributed to employees and agencies
```

Jurisdictional context matters throughout: which taxes apply, at what rates, and where they must be paid depends on where the company and each employee are located. Products handle multi-jurisdiction cases (employees in different states or provinces) by applying location-specific rules per employee.

### Corrections

Payroll errors are corrected, not erased:

- **off-cycle runs** pay amounts that missed the regular run
- **retroactive adjustments** correct earlier periods, with the system computing the delta
- **amended filings** correct already-submitted tax forms

Because pay records are durable and legally significant, corrections leave traces rather than overwriting history.

## Interfaces

The following surfaces are described conceptually; exact layouts and names vary by product.

### Payroll dashboard / run list

The operator's home surface.

- shows upcoming and past pay runs, the next scheduled pay date, and the action to start the next run
- primary actions: start a run, review a past run, open reports

### Pay-run editor

The working surface where a run is assembled and approved.

- sections for earnings inputs (imported or entered hours, one-off items), per-employee gross-to-net detail, deductions and adjustments, and the summary of money movement the run will trigger
- primary actions: import/enter time, add earnings items, edit deductions, review breakdown, confirm/approve the run

### Employee pay records

The setup and maintenance surface for the people being paid.

- per-employee compensation terms, work location, payment method, tax elections, deductions, and accumulated pay history
- primary actions: add employee, change pay terms, update elections, view pay history

### Pay schedule and tax settings

Configuration surfaces.

- schedules (frequency, pay dates), jurisdiction registrations, filing details, agency accounts
- primary actions: create/edit schedules, update tax and filing information

### Employee self-service

The employee-facing surface (web/mobile in modern products).

- pay statements, year-end forms, personal and payment details, payday notifications
- primary actions: view/download statements and forms, update own info

### Reports

- payroll cost summaries, run registers, tax liability views
- primary actions: generate, filter, export

## Important Rules / Behaviors

### The run is permission-gated before money moves

Executing a run triggers real money movement (employee payments plus remittance of withheld taxes). Products therefore gate it: only permitted roles can run or approve payroll, and the final step is an explicit confirmation that shows the breakdown and the debit it will cause. Separating preparation from approval is a common control in larger organizations.

### Withholding happens at run time

Statutory amounts are computed and captured with each run — not reconciled later. This is what makes the subsequent remittance and filing loop reliable, and it is why a skipped or late run creates compliance consequences, not just late pay.

### Pay records are durable and legally significant

Registers, pay statements, and year-to-date history persist and accumulate. Year-end forms are derived from them; audits and disputes are answered from them. Corrections are recorded as corrections (off-cycle runs, retro adjustments, amended forms), not as rewrites.

### The employee pay record drives the computation

Changes to pay terms, elections, or work location take effect through the record and apply to subsequent runs. Work location in particular determines which jurisdiction's rules apply to each employee — a structural rule in products that handle multi-jurisdiction workforces.

### Payment timing depends on the rail

Direct deposit requires lead time between run confirmation and payday; checks and other rails differ. Products expose this as scheduling constraints (submission deadlines for a given pay date) rather than as instant settlement.

### The cycle is strict, exceptions are explicit

The regular cycle is scheduled and repeating; anything outside it — bonuses, missed payments, terminations, corrections — goes through explicit off-cycle paths so that the regular run's integrity and the compliance loop are preserved.

## Variants

Common forms of the Type:

- **standalone payroll** — a dedicated payroll product (often with light HR features attached)
- **POS-embedded payroll** — payroll inside a point-of-sale/business platform, with time, tips, and sales flowing in from the same ecosystem (common in hospitality and retail)
- **accounting-embedded payroll** — payroll as an add-on to accounting software, with journals posted natively
- **HCM-platform payroll** — payroll as one module of a human-capital platform, consuming the HR record continuously
- **full-service payroll provider** — the vendor files and remits taxes on the employer's behalf, in some products with guarantees covering the vendor's own filing errors; contrasted with **software-only** postures where the employer files from generated reports
- **contractor-inclusive vs contractor-only** — products that pay employees and contractors, and lightweight products that only pay contractors with the corresponding year-end forms
- **regional editions** — the same core shipped under different statutory wrappers per country or region (tax/social-insurance schemes, payslip conventions, wage-protection rails, local forms)
- **industry editions** — hospitality (tips, tipped wages), retail (commissions, multiple rates), and similar configurations
- **global payroll** — multi-country consolidation of pay runs; structurally adjacent (see Related Application Types)

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Time & Attendance System | input provider (upstream) | centers on capturing hours/attendance; payroll consumes that data to compute and issue pay. Remove pay computation → time system remains; remove time capture → payroll remains (salaried payroll needs none) |
| HRIS / HCM | record master (upstream) | centers on the employment record and HR processes; payroll consumes pay-relevant data (hires, salary changes, deductions). Payroll can run standalone with its own minimal records |
| Global Payroll Platform | sibling, scope gradient | consolidates pay runs across many countries and jurisdictions; a Payroll System runs pay under one (or few) jurisdictions with deep local machinery. Vendors ship them as separate products |
| Accounting Software | downstream receiver | holds the books; payroll posts expenses and liabilities into it. Accounting products may embed payroll, but the pay-run/withholding structure is distinct from the ledger |
| Compensation Management Platform | planning vs execution | plans pay (bands, merit cycles, budgets); payroll executes pay. Compensation terms flow from planning into payroll records |
| Benefits Administration Platform | election source (upstream) | manages benefit enrollment; the resulting deductions are applied inside payroll runs |
| PEO / EOR services | service model, different Type | the provider becomes the legal employer and runs payroll as employer of record; payroll software is a tool of the actual employer |
| Payment Processing Platform | different object model | moves merchant commerce money through card/bank networks; payroll pays employees out of employer funds as a computed obligation, typically over bank rails |

The boundary with **Time & Attendance** and **HRIS** is a producer→consumer relationship: both feed the payroll core but neither computes nor issues pay. The boundary with **Global Payroll Platform** is scope: single-jurisdiction depth versus multi-country consolidation — the closest sibling and the most likely candidate for a shared review.

## Representative Products

- **Square Payroll** — POS-embedded, full-service payroll for very small businesses; contractor-only tier
- **Xero Payroll (powered by Gusto)** — payroll embedded in cloud accounting
- **Zoho Payroll** — standalone suite-native payroll shipped as regional editions (US, Canada, India, GCC)
- **Rippling Payroll** — HCM-platform-native payroll with a separate Global Payroll product line

Gusto — the engine behind Xero's US payroll and a major standalone product — could not be documented directly (its site was unreachable during research); its capabilities are evidenced indirectly through Xero's official product page.

## Sources

Research date: **2026-09-06**

- Square Support Center — "Run payroll for W-2 employees": https://squareup.com/help/us/en/article/5855-run-payroll
- Square Support Center — "Make federal payroll tax payments": https://squareup.com/help/us/en/article/5683-square-payroll-federal-tax-filings
- Square Payroll product page: https://squareup.com/us/en/payroll
- Xero Payroll product page: https://www.xero.com/us/payroll/
- Zoho Payroll product page: https://www.zoho.com/payroll/
- Rippling Payroll product page: https://www.rippling.com/en-US/payroll

> Sourcing limitation: several major payroll vendors (including Gusto, ADP, Paylocity, Sage, and QuickBooks Payroll) were unreachable from the research environment on 2026-09-06. Product evidence therefore skews toward SMB and mid-market cloud products, with one product (Square) documented at operational help-article depth and the others at product-page depth. Precise operational facts (submission cutoffs, deposit schedules, specific form lists, jurisdiction-specific rates) are intentionally not stated in this document; they are product- and jurisdiction-specific and are recorded, where observed, in the paired Research Notes.

Detailed evidence, product-by-product observations, cross-product comparison, and the historical/regional breadth check are recorded in the paired Research Notes.
