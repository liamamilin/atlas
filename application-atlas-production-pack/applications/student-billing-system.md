# Student Billing System

## Overview

A **Student Billing System** is the institution-side system of record for what its students owe and pay. It holds each student — in K-12 realizations, effectively each family — as a running account that accumulates the charges the institution assesses (tuition and fees by academic period, plus charges from campus services such as housing, meals, parking, and activities), presents bills against that account, records payments and installment plans, applies financial aid as credits, tracks the balance to resolution, and refunds credit balances back to the student.

The problem it solves is administrative and financial at once: an institution enrolls a standing population of students who owe it money under institutional rules — not per-purchase customers — and it must assess the right charges for the right period, collect them through plans and payments that families can actually sustain, keep the ledger accurate enough to reconcile to the institution's books, and handle the reverse flow (refunds, aid credits, sponsor payments) without losing the audit trail.

Its boundary: it manages the **student account and the money moving on it** — not the student's academic record, not the aid awards themselves, not the enrollment commitment, and not the payment rails as such. It typically consumes the student population from a student information system, receives charges from systems that create billable events (registration, housing, campus services), receives financial aid as credits from the aid system, and hands its accounting to the institution's ERP or general ledger.

## Users & Context

Primary staff users:

- **Bursar / student accounts staff** (higher education) — run the billing cycle: assess and post charges, generate statements, set up and monitor payment plans, apply aid credits, issue refunds, follow up on past-due balances. In the researched sample this group is consistently the named audience — staff "responsible for Student Accounts," with job titles such as director of student accounts and manager of student accounts and cashiering.
- **Business office / tuition management staff** (K-12) — configure tuition and fee structures, enroll families in payment plans, record payments and adjustments, and reconcile collections. In private and faith-based schools this is often the same small office that also handles aid and enrollment contracts.
- **Finance office / accountants** — consume the billing system's output as the institution's student receivable: one researched product is explicitly positioned to serve as the school's "accounts receivable subsidiary ledger" beside its general ledger.

Payer-side users:

- **Students** — view their bill and account activity, make payments, set up payment plans, choose refund methods, and grant others permission to pay on their account.
- **Families and authorized payers** (dominant in K-12) — parents pay tuition and incidental bills; students can assign "authorized payers" to their account so family members can view and pay the bill.
- **Sponsors** (variant) — employers and organizations that are billed directly for a student's costs under tuition-benefit arrangements.

The work environment is cyclical: billing runs on the academic calendar. Charges are assessed at registration and period start, bills are issued on billing schedules, plan installments fall due monthly, refunds spike when aid disburses or schedules change, and delinquency follow-up concentrates around term start. In K-12 the cycle anchors on the enrollment season, when families sign up for payment plans for the coming year.

## Core Model

### The defining core

Three structures carry the Type. Remove any one and the software stops being student billing:

```text
Student account          (the running per-student / per-family ledger of record)
        ▲ charges posted          │ payments, plan installments,
        │ (from institutional     │ aid credits, refunds
        │  billable items)        ▼
Charge assessment ────► Collection loop ────► resolved balance
```

- **The student account.** The center of the world: a persistent, individually identified account per student (per family in K-12 billing) held by the institution. It accumulates charges, payments, credits, and aid application, and it always carries a live balance — "a home for all payments made on student accounts," as one researched product puts it. The account is what makes the money addressable: every charge, payment, plan, refund, and aid credit attaches to it, and the institution's entire student receivable is the population of these accounts. Without the account, the software is a payment tool with no memory.
- **Institutional charge assessment.** The institution defines its billable items — tuition and fees configured by academic period, program, or grade level, plus charges from campus services — and posts them to student accounts. Two properties make this more than invoicing: the charges are assessed by institutional rule against the enrolled population (the account holder exists because of enrollment, not because of a purchase), and they commonly originate in other systems — registration produces tuition, housing produces room charges, campus services produce the rest — and are consolidated onto one account ("automated, consolidated bills that include everything from tuition and housing to parking and athletic fees"). Note that tuition itself is not definitional: public-school fee billing and incidental-only billing satisfy the same structure with fees alone.
- **The collection loop.** The account is presented to the payer as a statement or bill; payments are recorded against it — lump-sum or as installments under a payment plan; and the balance is tracked to resolution. The loop closes in both directions: money in (payments, sponsor payments, aid credits) and money out (refunds of credit balances to the student, by the student's chosen method). Without the loop, the system is a charge catalog nobody collects on.

### Standard capabilities around the core

Mature products almost universally add:

- **Statements and eBills** — consolidated, itemized bills organized by period, delivered electronically, with bill-due and statement-available notifications by email and text.
- **Payment plans** — tuition and fees split into installments across the term or year. Common forms include semester plans, plans the vendor actively manages on the institution's behalf (including following up on delinquent installments), past-due or recovery plans that re-engage students with arrears, extended long-term plans for larger balances, and plans payable in the family's home currency for international students.
- **Student and family self-service** — a portal or app to view the bill and account activity, pay online, and enroll in a plan; several products also let the student grant others permission to view and pay on the account (authorized payers).
- **Financial aid application** — aid awards credited against the account, commonly automatically ("awards are automatically credited to a student's account… applied to tuition bills without extra steps"), so the aid office and the billing office work the same balance.
- **Refunds and disbursements** — credit balances returned to students, with the student choosing the method (bank transfer, prepaid card, or check), status tracking from issuance to deposit, and — in US higher education — compliance machinery around federal refund rules.
- **Notifications and follow-up** — payment reminders, delinquency follow-up and pre-collections, and one-off accommodations such as adjusting a due date for a student in hardship.
- **Reporting and dashboards** — collections, outstanding balances, cash-flow projection, and real-time payment reporting for the business office and leadership.
- **Accounting integration** — the billing system operating as the institution's student-receivable subsidiary ledger: charges, credits, and payments mapped to general-ledger accounts and synced with the ERP; the student population drawn from the SIS.
- **Payment-method breadth and in-person collection** — bank transfer/direct debit, cards, checks, and cash; campus-wide cashiering for in-person payments; payment forms for collections outside the billing cycle.

### One structure, many implementations

The core objects are conceptual; products realize them differently, and recognizing the concept prevents over-fitting to one segment's pattern:

```text
Concept:  the account holder
Realizations:  the student (higher education, with authorized payers),
               the family (K-12 tuition billing),
               the student with a sponsor billed separately

Concept:  the charge
Realizations:  tuition by term, course/program fees, housing and meal
               charges, parking, athletics, activity and incidental fees,
               prepay balances

Concept:  the collection instrument
Realizations:  statement + lump-sum payment, installment payment plan,
               tuition contract with scheduled installments (K-12),
               sponsor invoicing

Concept:  the money coming back
Realizations:  financial-aid credits, sponsor payments, refunds of
               credit balances by chosen method
```

A reader who knows only the US higher-education version — term bills, payment plans, federal refund rules — should still recognize a private school's family tuition plan or a public school's fee collection as the same Type, because the three core structures are all present.

## How It Works

The billing cycle runs on the institution's academic calendar:

### 1. Configure what the institution bills for

Staff define the billable items and their rules: tuition and fee structures by period, program, or grade; billing schedules and due dates; plan options; refund methods; and the accounts each charge type maps to in the general ledger. Configuration made here silently governs everything downstream.

### 2. Assess charges onto student accounts

Charges are posted to each student's account — commonly in batches at registration or period start, and commonly fed from other systems: tuition from registration, room and board from housing, service charges from campus systems. The account consolidates everything the student owes the institution in one running balance.

### 3. Present the bill

The system generates statements — consolidated, itemized, by period — and delivers them to the student (and, in K-12, the family), with notifications when a new statement is available and when a bill is due. The student sees the bill, the account activity behind it, and the current balance in a self-service portal.

### 4. Collect

Payment arrives through the surfaces the institution offers: online payment in full, enrollment in a payment plan that splits the balance into installments, in-person payment at the cashier, or payment by a sponsor or authorized payer. Plan installments are tracked as they fall due; the vendor or institution follows up on missed ones. Aid credits and sponsor payments post against the balance as they arrive.

### 5. Resolve and return

As payments and credits land, the balance moves toward zero. When payments and aid exceed charges — after a schedule change, withdrawal, or aid disbursement — the credit balance is returned to the student as a refund, by the student's chosen method, tracked from issuance to deposit.

### 6. Reconcile and account

Throughout, the office watches collections against expectations: dashboards for outstanding balances and cash-flow projection, real-time payment reporting, and reconciliation of every charge, credit, and payment to the general ledger. The billing system's ledger is the institution's student receivable.

### The delinquency path

When a balance goes unpaid, the loop has a defined recovery path: reminders escalate, plans are restructured (past-due plans exist precisely to bring arrears back into installments), and the stakes are enrollment itself — the researched products frame their recovery machinery as keeping students enrolled and giving those with past-due balances "a way to continue their education." Institutions commonly couple unpaid balances with consequences for the student's standing (such as registration or records holds); the researched pages evidence the enrollment-stakes framing directly, while specific hold mechanics vary by institution.

### The K-12 tuition-contract variant

In private and faith-based K-12 billing, the year starts at enrollment: the family commits through an enrollment contract (a separate system's job), and the payment plan is set up as part of that moment — tuition, fees, discounts, and aid amounts resolved into a schedule of installments that then runs through the year, with incidental charges (lunches, field trips, technology) billed on top and prepaid accounts drawn down as services are used.

## Interfaces

The following surfaces appear consistently across the researched products; names and layouts vary.

### Student account center / bill view (payer side)

Purpose: the payer's window into the account. Typical information: current balance, itemized charges by period, payment history, upcoming due dates, aid credits. Primary actions: view bill, make a payment, enroll in or manage a payment plan, set refund preference, manage authorized payers.

### Staff billing dashboard

Purpose: run the office's day. Typical information: accounts by state (billed, paying on plan, past due, credit balance), collections against projections, real-time payment activity. Primary actions: post or adjust charges, apply a credit, set up or restructure a plan, adjust a due date, issue a refund, send a reminder.

### Payment plan setup

Purpose: turn a balance into a sustainable schedule. Typical information: plan options (number of installments, due dates, payment methods), the balance being spread, plan terms. Primary actions: select a plan, connect a payment method, confirm; staff-side: configure plan options, monitor plan health.

### Refund selection

Purpose: return credit balances. Typical information: available refund amount, disbursement methods, status of a refund from issuance to deposit. Primary actions: choose or update a refund method, track status.

### Charge and billing configuration (admin)

Purpose: define the institution's billing rules. Typical information: tuition and fee structures, billing schedules and due dates, charge-to-GL-account mappings, plan and refund options. Primary actions: create and edit billable items, set schedules, map accounts.

### Reporting

Purpose: oversight for the business office and leadership. Typical information: collections, outstanding balances and aging, cash-flow projections, plan enrollment, refund volumes. Primary actions: filter, export, schedule reports.

## Important Rules / Behaviors

- **The balance is live and cumulative.** The account is a running ledger, not a sequence of one-off invoices: charges, payments, credits, and aid all post to the same balance, and every surface — student view, staff dashboard, GL export — reads the same live number.
- **Charges come from many sources but land on one account.** Registration, housing, campus services, and manual entries all consolidate onto the student's account. The billing system is the consolidation point, not the origin of most billable events.
- **Aid is a credit, not a payment.** Financial aid reduces the balance as a credited award; the award record lives in the aid system, the credit lives here. The two systems are designed to interlock, not merge.
- **Time is structural.** Academic periods, billing schedules, due dates, and plan installment calendars organize everything. The same charge behaves differently in different periods; records are organized by student × period.
- **Delinquency has a defined path and enrollment stakes.** Missed payments escalate through reminders and plan restructuring; the recovery machinery is explicitly framed around keeping students enrolled. Unpaid balances commonly affect the student's standing at the institution.
- **Credit balances flow back out.** Money held beyond what is owed is returned to the student as a refund, by the student's chosen method — in US higher education under federal refund-compliance rules. The refund is part of the loop, not an exception to it.
- **The ledger feeds the books.** Every charge, credit, and payment maps to the institution's general ledger; the billing system is the student-receivable subsidiary ledger, and its accounting must reconcile.
- **Payers can be multiple.** The student, family members, and sponsors may all put money on the same account; several products manage explicitly who may view and pay (authorized payers, sponsor accounts).
- **State names vary.** Products differ in the vocabulary for charges, plans, and balances. The conceptual lifecycle — assessed → billed → collected (or planned) → resolved (or refunded) — is the stable part; exact labels are product-specific.

## Variants

- **Higher-education student accounts (the largest pole).** Per-student accounts billed by term; consolidated bills spanning tuition, housing, parking, and activity fees; semester payment plans including vendor-managed, past-due, long-term, and international-currency variants; Title IV refund machinery and tuition tax-statement processing in the United States; sponsor billing for tuition-benefit employers; campus-wide cashiering.
- **K-12 private / faith-based tuition management.** Family accounts anchored on the enrollment moment: tuition contracts resolved into installment plans at sign-up, aid and discounts applied to the plan, incidental billing and prepay accounts layered on top during the year, and a family help desk often operated by the vendor.
- **Public-school fee collection (the boundary pole).** Districts and public schools collect fees (courses, activities, meals, field trips) and payments from parents — the same collection surface, but the organizing ledger is the school's activity funds and district accounting rather than the per-student account. This pole marks where the Type ends and school-finance/accounting software begins.
- **SIS-embedded module.** Student billing as a first-class module of a student information system (documented beside financial aid, regulatory content, and tax-statement processing), sharing the SIS's population and data model. The objects and workflow do not change with the packaging.
- **Payments-platform posture.** Products that sell the collection machinery as an operated service — actively managed plans, staffed family support, refund processing — beside the institution's ERP, rather than as software the office runs alone.
- **Regional realizations.** Direct-debit-centered regimes (e.g., Australian school billing with school-wide invoicing of excursions and technology), boarding and international schools with home-currency payment, and school-choice scholarship program administration layered onto tuition billing.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Financial Aid Management | upstream credit feeder | owns aid funds, eligibility, and the award record; delivers aid as credits to the student account. The award (what was granted) lives there; the money moving on the account lives here. |
| Enrollment Management | upstream commitment feeder | owns the commitment act — the signed contract and deposit that bind a family to a period. Charges may be assembled onto that document, but invoicing, payment plans, and collection over time live here. |
| Student Information System / SIS | population source | owns the student record and enrollment; the billing system consumes the population and returns financial data. A SIS without the account ledger is still a SIS. |
| Higher Education Administration System | suite container | runs academic administration; student billing exists there as the student-accounts module beside financial aid. The billing core is the same either way. |
| Campus Housing Management | charge source | owns room assignment and the residential lifecycle; computes and schedules housing charges, then hands them to the student account for collection. |
| Campus Card Management | charge source | captures point-of-service events (meals, printing, access-coupled spending) and hands charges off; billing posts them to the account. |
| Billing Platform / Invoicing Application / Accounts Receivable Management | generic cousins | bill commercial customers per transaction. Student billing's receivable population exists by enrollment, charges are assessed by institutional rule per academic period from many campus sources, aid interacts as credits, and the balance carries enrollment stakes — structures generic billing lacks. |
| Payment Processing Platform | embedded capability | moves money; the student billing system owns the account and ledger the money moves on. Processing is bundled inside billing products, not the center. |
| School activity-fund / district finance software | boundary neighbor | centers school-level fund accounting and district oversight; the per-student account is not its organizing ledger. Public-school fee collection sits on this seam. |

The two seams that matter most in practice: **aid ↔ billing** (awards become credits on the account) and **enrollment ↔ billing** (the commitment moment hands over families who then owe money over time). Both seams are documented by products on both sides, which is strong evidence the Types are distinct but designed to interlock.

## Representative Products

- **Nelnet Campus Commerce** — higher-education tuition management and payments platform: consolidated billing and payments on student accounts, payment plans (including actively managed, past-due, long-term, and international variants), sponsor billing, and refund disbursement.
- **FACTS (A Nelnet Company)** — K-12 private and faith-based tuition management: family payment plans, incidental billing and prepay accounts, financial-aid auto-credit, and accounting positioned as the school's accounts-receivable subsidiary ledger (US and Australia/New Zealand realizations).
- **TADS Tuition & Billing (VenturEd Solutions)** — K-12 private-school tuition management sold as a distinct product beside Contracts & Deposits, Admissions, Financial Aid, and its SIS — a direct view of the billing/enrollment product boundary.
- **Anthology Student — Student Accounts module** — the SIS-embedded realization: student accounts as a first-class department module of a major student information system, beside financial aid, regulatory content, and 1098-T tax-statement processing.
- **KEV Group (SchoolCash)** — the K-12 public-district boundary pole: school fees, payments, and activity-fund accounting, documenting where the per-student account gives way to school-level fund accounting.

Together these cover the higher-ed platform, K-12 tuition-management, SIS-embedded, and public-school-fee realizations of the same core model.

## Sources

Research date: **2026-09-09**

- Nelnet Campus Commerce — homepage, Tuition Management, Billing & Payments, Payment Plans, Refunds, Sponsor Billing and Payments, Business Office: https://campuscommerce.com/ (and /payment-solutions/… subpages)
- FACTS — homepage, Financial Intelligence, Accounting/Billing & Payments feature page, AU Payment Plans and Billing: https://factsmgt.com/ (and subpages)
- TADS (VenturEd Solutions) — homepage with product taxonomy (Tuition & Billing, Contracts & Deposits, Educate SIS): https://www.tads.com/
- Anthology / Ellucian — Anthology Student help-center module map, Student Accounts module page, Documentation Suite index (1098-T Processing stream): https://help.anthology.com/CNS/26.2/WebClient/Content/TopNavHome.htm , https://help.anthology.com/CNS/26.2/WebClient/Content/tile-sa.htm , https://help.anthology.com/Content/DocSets/CNSDocSet.htm
- KEV Group (SchoolCash) — homepage: https://www.kevgroup.com/

> Sourcing limitation: TouchNet returned 403 and the Transact domain now serves an unrelated company, so the historically prominent TouchNet/Transact student-accounts family could not be directly evidenced; Blackbaud's tuition-management page returned 404 and Ellucian product-page URLs were not found (404). TADS was evidenced at root level only (subpages blocked), and the Anthology Student Accounts topic tree was JavaScript-gated — module structure and product scope are confirmed from official surfaces, but precise operational details (exact state names, default rules, numeric limits, hold mechanics) were not retrievable and are deliberately not stated. Vendor metrics appearing on marketing pages were recorded in the research notes as vendor claims only.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis are recorded in the paired Research Notes.
