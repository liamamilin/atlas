# Leave & Absence Management

## Overview

A **Leave & Absence Management** application is an employer-side system of record for **time away from work**. It maintains the organization's recognized kinds of absence — vacation, sick leave, parental leave, unpaid leave and so on — each configured as a small policy, records every absence as a dated period attributed to a specific employee, moves each absence through a governed request-and-decision flow, and keeps an ongoing account of how much leave each employee is entitled to versus how much they have taken.

The defining structure is small:

```text
Absence type (a configured policy category)
└── Entitlement & balance (per employee, per type)
    └── Absence record (dated period, attributed to an employee, with a state)
        └── Governed entry and decision (request or report → rule check → recorded decision)
```

Everything else commonly associated with the category — self-service portals, approval inboxes, who's-out calendars, accrual engines, carryover rules, statutory-law libraries, payroll integrations — is widespread in current products but is not what makes the product an absence-management system. A paper vacation-request form plus a ledger card of days taken against an annual entitlement realizes the same core.

The boundary in one sentence: this Type governs *planned and approved absence*; it does not record *actual worked time* (Time & Attendance), does not decide *who works when* (Employee Scheduling), and does not *compute pay* (Payroll) — though it feeds all three.

## Users & Context

**Primary users:**

- **Employees** — the largest population. They check their remaining balance, submit absence requests, view their own history, and upload required documentation. Most interaction is occasional and self-service.
- **Managers / approvers** — decide on their team's requests. They work from a queue of pending requests, consult the team calendar to judge coverage, and approve, deny, or record absence on an employee's behalf (for example, a phoned-in sick day).
- **HR administrators** — own the framework rather than the individual requests: they configure absence types and entitlement policies, assign policies to employees, correct balances, set holiday calendars and blackout periods, and run the reporting.

**Secondary consumers:**

- **Payroll** — consumes the outcome (paid leave taken, unpaid leave, accruals) as input to pay computation.
- **Scheduling / workforce planning** — consumes approved absence as a constraint on assignments.
- **Dedicated leave administrators** (in the compliance-oriented pole) — specialists who manage statutory-leave cases, certifications, and return-to-work processes; in some deployments these specialists work for a third-party administrator operating the leave program on the employer's behalf.

The system runs continuously: requests and decisions arrive daily, balances update as absences are taken, and entitlements reset on a leave-year cycle that may or may not match the calendar year.

## Core Model

### The defining core

**Absence type.** The organizing configuration object. An absence type is the organization's named category for a kind of time away — annual leave, sick leave, maternity or paternity leave, unpaid leave, compassionate leave, and, in some products, non-absent categories such as working from home or business trips. Each type carries rules that determine how the system treats it:

- whether bookings of this type **draw on an entitlement** (deduct from a balance) or not;
- whether a booking **requires approval**, or can be recorded directly;
- what **documentation** it requires, and after how many days;
- **who may see it** — many organizations let colleagues see *that* someone is away without revealing *why*, so types carry a visibility setting (private to the employee and their approvers, or public);
- how it renders on calendars and in connected tools.

**Entitlement and balance.** For each employee and each entitlement-bearing type, the system tracks how much leave the employee may take and how much they have taken. The entitlement itself can be established in several ways, and mature products usually support more than one:

- **granted up front** for a leave year (a fixed annual allowance);
- **accrued over time** (per month or per pay period, sometimes scaled by tenure);
- **fixed by statute** (a legal entitlement, in some markets kept separate from the employer's additional, non-statutory allowance);
- **unlimited** (no fixed amount; the system still records usage).

The balance is the running difference — entitlement minus taken, adjusted by carryover from the previous year, manual corrections, and proration for mid-year joiners, leavers, and part-time schedules.

**Absence record.** The transactional object: a dated period (a day, a range of days, or hours) of a specific type, attributed to a specific employee, held persistently with a state — requested, approved or denied, taken, cancelled or amended. Records accumulate into the employee's absence history and the organization's absence data.

**Governed entry and decision.** Absence enters the system through a defined channel: an employee request, or a direct entry by a manager or HR on the employee's behalf (the normal path for unplanned sickness). The entry is checked against the type's rules — balance sufficiency, coverage limits, notice requirements — and a designated authority (the employee's approver, by default the line manager, with overrides configurable) approves, denies, or records it. The decision itself is recorded. Some types are configured to skip human approval; the governed decision step remains, it is simply automatic.

### What mature products add

These structures appear across the researched market and make the Type practical, but a product lacking one can still be a genuine absence-management system:

- **Employee self-service** — request forms, balance views, personal history.
- **Approver inbox and notifications** — pending requests grouped per approver; email or push notifications on request and decision.
- **Who's-out calendar** — a team, department, or company-wide calendar of absences, usually alongside a personal calendar; calendar feeds and chat-tool display keep the rest of the organization informed.
- **Holiday calendars** — public and company holidays, often per location or country, feeding the deduction logic.
- **Working schedules as the deduction basis** — how much an absence costs against the balance depends on the employee's work schedule and which days count (see Rules below).
- **Grant and accrual machinery** — granting cadence, carryover caps, tenure-based rewards, proration rules, rounding.
- **Documentation handling** — attachments on bookings; certificate requirements triggered after a configured number of days; in some markets, electronic medical certificates retrieved automatically.
- **Substitutes and delegation** — colleagues named to cover during an absence; approval authority delegated while the approver is away.
- **Coverage constraints** — blackout dates and caps on concurrent absences per team.
- **Reporting and handoff** — balance reports, absence and sickness statistics, exports, and the payroll handoff of taken leave.

### One structure, many implementations

```text
Concept:   Entitlement
Realized as:  fixed annual allowance · monthly accrual · statutory entitlement
            · tenure-scaled grant · unlimited policy · time-earned banks (overtime, time-in-lieu)

Concept:   Governed decision
Realized as:  manager approval · named approver override · HR/admin approval
            · automatic approval for rule-conforming requests · eligibility determination (statutory pole)

Concept:   Deduction basis
Realized as:  working days vs calendar days · schedule overlap · public-holiday treatment
            · half-day and hourly units · country-specific working-day conventions
```

## How It Works

### 1. Configure the absence framework

Administrators define the absence types and, per type, one or more **policies** — the rules that bind the type to a group of employees: how entitlement is granted or accrued, which days count as leave, whether half-days are allowed, whether a substitute is required, when documentation is due, and what happens on long absences. Policies are assigned to employees (individually, in bulk, or by import), often with an effective date. Holiday calendars and approver assignments complete the framework. Multi-market organizations commonly run several policies per type to reflect country-specific rules.

### 2. The request-and-decision loop

```text
Employee opens the request form (or clicks a day on their calendar)
→ selects type, dates (or hours), optional substitute and note
→ system checks the rules (balance, coverage caps, blocked periods)
→ request lands in the approver's queue; notifications go out
→ approver approves or denies (consulting the team calendar)
→ decision recorded; balance updated; absence appears on calendars
→ employee and requester notified
```

Requests that fail a rule are blocked with an explanation at submission time; approvers typically retain an override path (booking on the employee's behalf with confirmation). Approved absence becomes visible to the team according to the type's visibility setting.

### 3. The unplanned-absence path

Sickness and other unplanned absences enter through the same record structure but a different rhythm: the employee (or a manager receiving a call) records the absence, often after the fact or day by day. Documentation rules attach here — a certificate may become required once an absence exceeds a configured length, prompting the employee to upload one or, in some markets, triggering automatic retrieval of an electronic medical certificate. Sickness records feed absence reporting rather than a planning decision.

### 4. Balance accounting across the leave year

Entitlements live on a cycle (leave year). Over the cycle the system grants or accrues entitlement, deducts taken absence per the deduction basis, applies manual corrections as recorded adjustments, and — at the boundary — computes carryover into the next year under the policy's caps, prorates for employees joining, leaving, or working part-time, and in some products compensates or transfers negative balances. The balance view shows the employee's entitlement, what has been taken, what is pending, and what remains — including, in some products, which portions expire and when.

### 5. Absence in effect

An approved absence radiates outward: it appears on team calendars and calendar feeds, removes the employee from scheduling considerations, names substitutes where required, and — for extended leaves in products that support it — can change the employee's status (for example, to "on leave", pausing notifications and org-chart visibility until an expected return), reduce compensation through the payroll link, and slow or stop the accrual of other paid leave types. Taken leave is handed to payroll as earnings-relevant data.

### 6. The statutory-leave flow (compliance pole)

In jurisdictions with regulated protected leave, a dedicated variant adds a determination layer in front of the case: an employee signals a qualifying life event → the system determines eligibility under the applicable laws and the employer's policies, computing the available entitlement and how it is consumed (continuously or intermittently) → a **case** is opened with its own workflow: notices and letters generated from templates, certification requested from the employee and their healthcare provider, usage tracked against the entitlement bank, concurrent leaves stacked under the governing rules → the case closes with a recorded return-to-work, which scheduling can then rely on. The employer's own policies run through the same machinery alongside the statutory ones.

## Interfaces

**Employee self-service.** The employee's home surface: current balances per type (with pending requests and, where applicable, expiring portions), a personal calendar, the request form, and absence history with documentation. Primary actions: request, cancel or amend, upload documents.

**Approver inbox.** The manager's working queue: pending requests (often grouped per approver for admins), each showing employee, type, dates, balance impact, and team-coverage context. Primary actions: approve, deny, record absence on behalf, view team calendar.

**Team / company calendar (wallchart).** The shared visibility surface: who is away, when, and (subject to visibility rules) why. Color and icon encode type; filters by team or location. Primary actions: view, drill into an absence, book from a selected day.

**Administration & configuration.** The HR surface: absence types and their rules, policies and entitlement settings, holiday calendars, approver assignments, blocked periods, balance corrections, policy assignment with effective dates. Primary actions: create/edit types and policies, assign, adjust balances, import.

**Employee balance ledger.** The per-employee record behind the balance: entitlement entries, deductions, adjustments, carryover — the audit trail of how the current balance came to be (surfaced as an activity view in products with deep entitlement engines).

**Reporting.** Balance summaries, absence and sickness statistics, unused-entitlement reports, exports for payroll and analysis.

**Case workspace (compliance pole).** The leave specialist's surface: case list with statuses, an individual case timeline (communications, documents, determinations), template-based correspondence, and return-to-work tracking.

## Important Rules / Behaviors

**Which days count is a configured rule, not an obvious fact.** Whether an absence "costs" anything on a weekend, a public holiday, or a non-working day depends on the policy's deduction basis — computed against the employee's work schedule and the holiday calendar. The same five calendar days off can deduct three days, five days, or nothing depending on configuration. This is the most consequential and most misunderstood rule in the Type.

**Entitlement mechanics are policy, not arithmetic.** Granting cadence (all at once vs installments), carryover caps and use-by windows, tenure rewards, proration for mid-cycle joins/leaves and part-time schedules, and rounding are all configured per policy. Two employees in the same company on the same type can hold different balances by design.

**Approval authority is explicit and delegable.** Requests route to a designated approver (default: line manager; per-employee overrides are common). Naming a substitute covers work, not authority — substitution does not transfer approval rights, which must be delegated separately. Admins typically retain an approve-anything fallback for coverage.

**Visibility of absence reasons is a privacy surface.** Colleagues commonly see that someone is away; the reason is visible only to the employee's approvers and HR unless the type is marked public. The same privacy discipline extends to calendar feeds and chat integrations.

**Coverage constraints bind employees, with a managed escape hatch.** Blackout periods and concurrent-absence caps block or warn at request time; managers and admins booking on an employee's behalf can typically override with confirmation — the constraint protects planning without removing authority.

**Records are durable and corrections are visible.** Cancelling or amending an absence restores or adjusts the balance; deleting a type does not erase historical bookings; balance corrections are recorded adjustments rather than silent overwrites. The history is the basis for payroll handoff, disputes, and audits.

**Long absences can change the employee's system state.** Products aimed at longer leaves can flip status (pausing notifications and directory visibility), reduce pay through the payroll link, and slow other accruals after configured thresholds — turning a simple record into a managed event with a return date.

## Variants

- **Lightweight standalone tracker** — the whole product is the core: types, allowances, requests, approvals, calendar. Typical of small companies replacing spreadsheets.
- **HR-suite module with an entitlement engine** — absence as a Core-HR module with deep policy machinery (multi-policy types, statutory/non-statutory entitlements, long-term-leave effects) and tight links to attendance, payroll, and analytics. The dominant packaging in the mid-market and enterprise.
- **Statutory-leave compliance platform** — the dedicated pole: a maintained library of leave laws, eligibility determination, case management, certification and return-to-work workflows, pay-during-leave calculation, and accommodations handled alongside leave. Operated by the employer or by a third-party administrator.
- **Geography-tuned deployments** — statutory entitlement separation, country working-day conventions, electronic medical certificates, and country payroll sync appear where the workforce spans regulated markets.
- **Policy-shape variants** — unlimited-leave policies (usage recorded, no fixed amount), time-earned banks (overtime or time-in-lieu converted to leave), and company-wide closures modeled as absence types.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Time & Attendance System | sharpest seam | records *actual worked time* (punches, timesheets) and enforces attendance rules; this Type governs *planned and approved absence* and entitlement. They interlock: absence reduces expected hours; worked time during absence may count elsewhere |
| Employee Scheduling Platform | upstream/downstream | scheduling decides who works when (shifts as objects); approved leave is an input constraint that appears on the schedule and blocks conflicting assignments |
| Payroll System | consumer | payroll computes pay from leave outcomes (paid leave as earnings, unpaid leave as none); it does not own entitlements or the absence record. Pay-during-leave calculation exists only as a compliance-pole extension |
| Human Resource Information System / HCM | packaging parent | the HRIS runs many HR processes on the employee record; absence is one of its modules. This leaf documents that module's discipline, which also exists standalone |
| Approval Workflow Platform | generic machinery | can route leave requests, but has no absence types, entitlement ledger, or balance arithmetic; remove entitlement accounting from this Type and little remains but a leave-template approval flow |
| Benefits Administration Platform | interacting neighbor | leave events affect benefits eligibility, coverage, and billing, but the managed object is absence, not an election |
| Employee Time Clock | adjacent recording layer | may carry leave timesheets as records, but does not own leave policy or balances |
| Employee Portal / Employee Service Portal | presentation surface | portals present leave tasks and hand off to the owning system; this Type owns the transaction and the record |
| HR Case Management | adjacent at the compliance pole | statutory-leave handling is case-shaped, but its center is the absence entitlement lifecycle under law, not multi-topic HR case intake and triage |
| Workforce Management (contact centers) | distant neighbor | coverage-aware time-off approval exists there too, but the center is forecast-driven staffing; leave is one shrinkage input |

The most important boundary is with **Time & Attendance**: both systems hold "day-level employee time" records, and suite products blur them in one interface. The structural test is the object of record — actual worked time versus governed absence against an entitlement.

## Representative Products

- **Timetastic** — standalone lightweight leave planner (UK SMB pole)
- **Personio** — HR suite with a deep absence/entitlement engine (European mid-market pole)
- **Factorial** — global SMB HR suite with broad absence and deduction machinery
- **AbsenceSoft** — dedicated leave-of-absence and accommodations compliance platform (US enterprise pole)

Enterprise HCM suites (Workday, UKG, SAP SuccessFactors) also carry absence modules and are market context for the suite pole; their operational documentation was not directly accessible during research, and no claim in this document depends on them.

## Sources

Research date: **2026-09-07**

- Timetastic — https://www.timetastic.co.uk/ ; Help Centre: https://help.timetastic.co.uk/ (leave types, allowances, approvals, maximum absent, sick leave, booking time off)
- Personio — https://www.personio.com/product/absence-management/ ; Help Centre: https://support.personio.de/hc/en-us (time off types, time off policies, statutory and non-statutory entitlement)
- Factorial — Help Center: https://help.factorialhr.com/ (Absences & approvals; Time-off settings; Time Off Deductions sections)
- AbsenceSoft — https://absencesoft.com/ ; https://absencesoft.com/leave-of-absence/ ; https://absencesoft.com/platform-overview/

> Sourcing limitation: BambooHR's help center and support site were unreachable (blocked) and enterprise HCM documentation (Workday, UKG) is login-gated; the SMB-suite pole is evidenced by Factorial and the enterprise compliance pole by AbsenceSoft. Factorial evidence was gathered at documentation-structure level (documented capability inventory), so claims drawn from it are kept at capability level. Precise numeric limits (carryover caps, certificate thresholds, law-library counts) are product-specific configuration and are deliberately not stated as general facts. Detailed product-by-product observations and the cross-product comparison are recorded in the paired Research Notes.
