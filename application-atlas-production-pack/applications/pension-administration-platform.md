# Pension Administration Platform

## Overview

A **Pension Administration Platform** is the system of record and operating system for pension schemes: it maintains a registry of scheme members whose entitlements are governed by the scheme's rules, tracks each member's long-horizon accrual (service and/or contribution history), calculates the benefit due at life events under those rules, and administers the payment of those benefits — recurring retirement income and one-off settlements such as lump sums, transfers, and death benefits.

The defining core is deliberately small:

```text
Scheme (governing rule container)
└── Member (identified person, scheme-governed participation)
    └── Accrual record (service / contribution history → entitlement)
        └── Benefit calculation at life events (under scheme rules)
            └── Benefit payment (recurring income and/or one-off settlement)
```

Everything else commonly associated with these products — member portals, case management, pension payroll machinery, indexation processing, statements, employer portals, regulatory reporting — is standard capability that makes the administration practical, not what makes the product a pension administration platform. Older mainframe-era systems and differently positioned regional products fit the same core without any of the modern surfaces.

The platform's horizon is measured in decades: a member's record typically begins at joining the scheme and remains active through employment, leaving, retirement, and death. This long horizon — and the fact that the entitlement is defined by scheme rules rather than by a commercial contract or an investment account alone — is what separates this Type from its neighbors.

## Users & Context

**Primary users** are pension administrators and case handlers working for:

- pension funds and scheme-operating organizations (in-house administration teams)
- third-party administrators (TPAs) and administration bureaus running schemes on behalf of trustees or employers
- master-trust and multi-employer scheme operators
- insurers and specialist providers administering pension books

Their daily work is event-driven: process a retirement, apply a contribution schedule, correct a service record, set up a survivor's pension, chase an employer data discrepancy. Team leads oversee case queues and payment runs; payments specialists operate the recurring pension payroll; administrators handle calculations and correspondence.

**Secondary users:**

- **Members** — scheme participants who check their entitlement, update personal details, model retirement outcomes, and elect payment options through self-service surfaces.
- **Employers** — sponsoring employers who submit contribution and service data and, in some scheme types, are billed for contributions.
- **Auditors, trustees, and regulators** — consumers of reports, audit trails, and statutory returns rather than operators of the system.

The work environment is characterized by batch cycles (contribution processing, indexation, pension payroll, statement generation) interleaved with case work, and by extreme sensitivity to payment accuracy and record integrity, because errors compound over decades and create recoverable debts or regulatory exposure.

## Core Model

### The Defining Core

Four structures. If any one is removed, the product is no longer recognizable as pension administration:

- **Scheme-governed member registry** — members are identified people whose participation is defined by the rules of one or more pension schemes or plans. The scheme — a trust-based occupational scheme, a statutory public plan, a recordkeeping plan — is the governing container: it defines eligibility, accrual, vesting, indexation, survivor benefits, and available payment forms. One platform commonly administers multiple schemes, and one scheme commonly spans multiple sponsoring employers.
- **Long-horizon accrual record** — per member, the history from which entitlement derives: service history and pensionable salary (in defined-benefit schemes), contribution history (in defined-contribution schemes), and the derived entitlement. Records span decades, survive changes of employment, and must be correctable retroactively with effective dates.
- **Rule-based benefit calculation** — computing what a member is entitled to, now or at a future date, from their accrual record under the scheme's rules. In defined-benefit schemes this is formula-based (service, accrual rate, salary, revaluation); in defined-contribution schemes it is the accumulated account value. The rules are the scheme's own — the platform encodes them as configuration, not as fixed behavior.
- **Benefit payment administration** — putting the benefit in the member's hands: recurring retirement-income payments (a pension payroll with gross calculation, tax treatment, bank payment files, and payment advices) and one-off settlements (lump sums, transfers to other schemes, death benefits).

### Objects Around the Core

- **Dependants / beneficiaries** — people entitled through the member; survivor benefits require tracking them against the member's record.
- **Employer participation** — sponsoring employers with contribution arrangements; employer-submitted data (contributions, service, salary) is the raw material the accrual record is built from, and its quality is a standing operational concern.
- **Life events / cases** — administrative work is organized around member life events: joining, contribution cycles, absence, leaving, transfer, retirement, death. Mature platforms track these as cases with owners, tasks, and status.
- **Correspondence and documents** — benefit statements, calculation letters, election forms, payment advices; their generation and retention are core outputs of the system.

### Standard Capabilities

A typical modern platform carries most of the following. They are not what makes the product a pension administration platform, but they make administration practical:

- **Member self-service** — entitlement view, benefit statements, personal data updates, document upload, retirement modelling, payment-option elections.
- **Employer data exchange** — submission of contribution/service data (portal or file-based), validation, reconciliation, and discrepancy chasing; employer billing where the scheme type requires it.
- **Case management** — life events tracked as cases with workflow, task assignment, deadlines, and status, so that event processing is auditable and delegable.
- **Pension payroll** — the recurring payment run for members already receiving their pension: gross-to-net calculation, jurisdiction-specific tax treatment, bank payment file generation, payment advices, and annual tax statements.
- **Indexation / increases** — annual revaluation of deferred and in-payment benefits per scheme rules.
- **Death and dependant processing** — survivor benefit calculation and setup.
- **Transfer processing** — calculating transfer values and coordinating with receiving schemes, under the safeguards the regime requires.
- **Overpayment management** — detecting payments made in error and managing recovery.
- **Record correction** — back-service adjustments that recompute history under effective dates.
- **Statements and communications** — annual benefit statements and member letters, generated and retained by the system.
- **Statutory reporting and audit trail** — returns to regulators, trustee reporting, and a full record of who changed what and when.
- **Role-based administration** — administrative access scoped by role and scheme; delegated access for bureau operations.
- **Integrations** — payroll/HR systems (employer data), investment custodians and fund managers (unit prices for defined-contribution accounting), banks (payment files), tax authorities, and document services.
- **Data migration tooling** — scheme conversions are routine events in this market (schemes change administrator); platforms typically carry tooling for bulk record migration and reconciliation.

## How It Works

### Establish membership and begin accrual

```text
Member joins the scheme (employment / enrolment / transfer in)
→ member record created under the scheme
→ employer data begins flowing (contributions, service, salary)
→ validated and applied to the accrual record
→ discrepancies chased with the employer
```

There is no "purchase" and no policy issuance. Membership exists because the scheme's rules and the member's employment say it does; the platform's job is to keep the resulting record true.

### Maintain the accrual record

Contribution and service data arrives periodically from employers (or contribution schedules are processed directly). The platform validates it against expectations, applies it to member records, reconciles totals, and surfaces gaps. Corrections — a missed contribution period, a backdated salary change — are applied with effective dates and recomputed history, because the accrual record is the basis of every future calculation.

### Process a life event

```text
Life event occurs (retirement / leaving / transfer / death)
→ case opened and owned
→ entitlement calculated under scheme rules from the accrual record
→ options presented (payment form / transfer / deferral)
→ member election recorded
→ benefit set up
```

The calculation is the platform's defining intellectual work: it turns decades of history into a concrete entitlement under the scheme's rules. The election step matters because most regimes offer choices (lump sum vs income, transfer vs deferral), and the recorded election determines what is set up.

### Pay the benefit

Two payment shapes coexist:

- **Recurring pension payroll** — for members in payment: each run calculates gross entitlement, applies tax treatment, generates bank payment files, and issues payment advices; annual tax statements follow.
- **One-off settlements** — lump sums, transfer values, and death benefits, calculated and released as single transactions with their own controls.

Payment accuracy is the platform's highest-stakes obligation: an overpayment becomes a recoverable debt from a retiree; an underpayment becomes a complaint and regulatory exposure. Overpayment detection and recovery is therefore a standing process, not an exception handler.

### Maintain over time

```text
Annual indexation applied per scheme rules
→ annual statements generated and issued
→ statutory returns and trustee reporting produced
→ record corrections and audits handled with full audit trail
→ death → survivor benefits calculated and set up
```

### Core vs standard vs optional

**Defining core** — without these, not pension administration:

- scheme-governed member registry
- long-horizon accrual record (service and/or contributions)
- rule-based benefit calculation at life events
- benefit payment administration

**Standard capabilities** — present in most modern products:

- member self-service, employer data exchange, case management, pension payroll, indexation, death/dependant processing, transfers, overpayment management, statements, statutory reporting, audit trail, role-based administration, integrations, migration tooling

**Common variants / optional** — depends on scheme type, market, operating model:

- defined-contribution investment accounting (unitized holdings, investment elections, fund switching)
- auto-enrolment machinery (regime-dependent)
- buy-out / bulk annuity / pension-risk-transfer processing
- actuarial data feeds and valuation support (the valuation itself belongs to a neighboring Type)
- deployment posture (vendor-hosted SaaS, hosted legacy, on-premise)

## Interfaces

The following surfaces are described in conceptual terms; exact layouts and names vary by product.

### Administrator workbench

The administrator's primary surface.

- member search and the member record view (the central screen: personal data, membership, accrual history, entitlement, payments, documents, cases)
- case queues with ownership, status, and deadlines
- calculation screens (entitlement, transfer values, survivor benefits) showing inputs and rule outcomes
- payment-run consoles (pension payroll cycles, one-off settlements, bank file generation)
- correspondence generation and reporting

### Member portal

The member's self-service surface.

- entitlement and accrual view, benefit statements, payment history
- personal detail updates and document upload
- retirement modelling and payment-option elections
- typically read-mostly: members see and elect, administrators compute and execute

### Employer portal / data exchange

The employer's surface for its role as data supplier.

- contribution and service data submission, validation feedback, reconciliation views
- billing/invoicing views where the scheme type bills employers
- member status views scoped to the employer's own workforce

### Operations and batch surfaces

Scheduled and monitored runs that drive the cyclical work.

- contribution processing cycles, indexation runs, pension payroll runs, statement-generation runs
- file import/export for employer data, bank payments, and regulator returns

## Important Rules / Behaviors

### Scheme rules are the supreme law

Everything the platform computes is derived from the scheme's own rules — eligibility, accrual, vesting, indexation, survivor benefits, payment forms. The platform encodes these as configuration; two schemes on the same platform can behave differently in every respect except the core model.

### Effective dating and retro-calculation

Records span decades. Rule changes and data corrections carry effective dates, and affected history is recomputed. A backdated salary change or a retroactive scheme-rule amendment must flow through every calculation that depends on it.

### Payment accuracy and overpayment recovery

The recurring payment run is the platform's most sensitive operation. Overpayments create recoverable debts; underpayments create complaints and regulatory exposure. Detection, correction, and recovery of incorrect payments are standing behaviors, not edge cases.

### Tax treatment is mandatory and jurisdiction-specific

Pension payments are taxed according to the regime of the scheme's jurisdiction. The payment run applies this treatment as part of gross-to-net calculation; the platform cannot treat it as optional.

### Long retention and full audit

Records must persist for the member's lifetime and beyond (survivor benefits), with a complete audit trail of changes. Member data protection obligations apply throughout, and outlive the employment relationship.

### Death changes the record's owner, not its existence

On a member's death, the record does not close: dependants' survivor benefits are calculated and paid, sometimes for decades. Dependant records are first-class, not notes on the member record.

### Transfers are guarded movements of entitlement

Moving entitlement between schemes requires value calculation and coordination with the receiving scheme under regime-specific safeguards; platforms treat transfers as controlled cases rather than simple transactions.

## Variants

- **By scheme type** — defined-benefit administration (formula-based entitlements, service/salary histories, indexation) vs defined-contribution recordkeeping (contribution accounts, often with unitized investment holdings and investment elections) vs hybrid schemes.
- **By operating model** — in-house scheme teams; TPAs and bureaus running many schemes on one platform (software plus BPO); master-trust and multi-employer operators; insurers administering pension books.
- **By regional regime** — UK occupational pensions (including auto-enrolment duties); US corporate plans under ERISA; US public-sector plans (a traditionally distinct, defined-benefit-heavy market); Nordic occupational pensions; Dutch pension funds; Canadian registered plans. Regimes differ in tax treatment, reporting, member protections, and payment conventions — the core model survives all of them.
- **By scale** — single-employer schemes; multi-employer and master trusts with very large member populations; public plans with statutory governance.
- **By adjacent scope** — some platforms extend into buy-out/bulk-annuity processing or broader benefits administration; some bundle actuarial data services or investment administration. These extensions do not change the defining core.
- **By deployment** — vendor-hosted SaaS, hosted legacy environments, and on-premise installations (legacy mainframe systems remain in service in this market because of the decades-long record horizon).

## Related Application Types

| Application Type | Distinction |
|---|---|
| Insurance Policy Administration System | structurally the closest neighbor (long-horizon records, rule-based entitlement, payment runs); policy administration centers on a commercial contract sold by an insurer with premiums and coverage, while pension administration centers on scheme membership with trust/statutory rules, employer participation, and employment-based accrual |
| Benefits Administration Platform | employer-side and short-cycle: annual enrollment and elections across many benefit types; pension administration is scheme-side and spans decades through to payment |
| Payroll System | employer-side wage computation and payment, including deducting and forwarding pension contributions; pension administration receives those contributions and maintains the scheme-side record and eventual benefit |
| Actuarial Modeling Platform | values the scheme's liability through scheme-level projections; pension administration maintains member-level records and processes; the two exchange data but neither subsumes the other |
| Retirement Planning Application | consumer-facing projection and planning tool; no administration of records, cases, or payments |
| Fund Administration Platform / Transfer Agency | fund-side: NAV and investor registers for investment funds; a scheme's investments may sit in fund-administered vehicles, but the scheme-side entitlement record belongs to pension administration |
| Wealth Management Platform | individual investment accounts without scheme governance or a pension lifecycle |
| HRIS / Human Resource Information System | holds the employment relationship that feeds pension data; it does not administer scheme membership, entitlement, or benefit payment |

The boundary with **Insurance Policy Administration System** deserves emphasis because the two Types share the same structural pattern (long-horizon governed records → rule-based entitlement → payment). The distinguishing axis is the governance basis of the entitlement: scheme/trust/statute with employer participation and employment-based accrual, versus a commercial contract with premiums. Insurers operating buy-out and bulk-annuity books sit near this boundary — the scheme may be administered on a pension administration platform while the resulting annuity contracts sit in a policy administration system.

## Representative Products

- **Heywood Pension Technologies (Aquila)** — UK; the largest independent UK pension administration software provider, serving defined-benefit and defined-contribution schemes, master trusts, and administrators, with software and administration services.
- **Vitech Systems Group (V3LOX)** — US/UK; institutional pension and benefits administration for public-sector, multiemployer, corporate, and insurance customers.
- **FIS (PensionTrust)** — US; long-established administration software for public-sector pension funds.
- **Etract** — Nordic; pension administration platform used by pension companies in the Nordic market.

These products are listed as market anchors for the Type. On the research date their official documentation could not be reached (see Sources), so they are not cited as evidence for specific capabilities.

## Sources

Research date: **2026-09-06**

Attempted official sources (all unreachable from the research environment):

- Heywood Pension Technologies — https://heywoodpensiontechnologies.com/ (also legacy https://www.aquilaheywood.com/)
- Vitech Systems Group — https://vitech.com/
- FIS — https://www.fisglobal.com/
- Etract — https://www.etract.se/
- TCS BaNCS — https://www.tcs.com/ , https://www.tcwcs.com/

> Sourcing limitation: live fetch of vendor sites and help centers was not possible from the research environment on 2026-09-06 (repeated timeouts, transport errors, and blocked requests; a control fetch to a neutral domain succeeded, confirming restricted egress rather than a total outage). No Tier 1 or Tier 2 sources were obtainable, and no external sources were reachable either. Consequently, this document is written as a canonical model of the Application Type with reduced assertion strength: no product-specific capabilities, limits, defaults, or workflow details are claimed, and no precise operational facts are stated. Product names appear as market anchors only. Detailed research process, the full source-access record, and the abstraction analysis are recorded in the paired Research Notes.
