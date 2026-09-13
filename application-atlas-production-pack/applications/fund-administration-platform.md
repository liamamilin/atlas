# Fund Administration Platform

## Overview

A **Fund Administration Platform** is the system of record for the official books of pooled investment funds and for the capital positions of the investors in those funds — and the production line that turns fund activity into the fund's recurring official financial output.

Its defining core is small:

```text
Administered fund (the organizing record)
└── Official books and records of each fund
    └── Investor register with per-investor capital accounts
        └── Recurring cycle: reconcile → accrue fees → allocate
            → strike NAV / close the books → produce statements
```

The fund administrator's output is the version of the fund's financial picture that investors, auditors, and regulators rely on — distinct from a manager's own working records. Everything commonly associated with the category — automated custodian feeds, investor portals, waterfall engines, AI document extraction, tax preparation — is widespread in current products but is not what makes the product a fund administration platform.

When the dominant purpose shifts to supporting investment decisions, it is drifting toward a Portfolio Management System; when only the investor-facing slice remains, it is an Investor Portal or, for open-ended registered funds, a Transfer Agency function.

## Users & Context

The primary operator is a **fund accountant or administrator**: either staff of an independent third-party administration firm running books for many client funds, or the fund manager's own finance/CFO team running administration in-house (or on a vendor's administered service). Their work is period-driven — dealing dates, month- and quarter-ends, capital-call events, fiscal year-end.

Secondary users:

- **fund controller / CFO**: reviews and approves financials, oversees the close, signs investor deliverables
- **investor relations team**: consumes balances and performance for LP communication
- **auditors and tax preparers**: consume books, records, and supporting packs (downstream, not operators)
- **investors (LPs)**: portal users — read statements, documents, and balances; in some products fulfill capital calls or update payment instructions

The environment is institutional finance: multiple legal entities and currencies per fund family, custodians and brokers holding the fund's assets, external auditors, and — depending on jurisdiction — regulated roles such as depositaries or AIFMs.

## Core Model

### The defining core

**Administered fund.** The system's world is organized around investment funds — legal pooled vehicles — together with closely attached vehicles such as general-partner entities, co-investment special-purpose vehicles, or master-feeder chains. The fund, not a person or a deal, is the unit whose records are kept.

**Official books and records of each fund.** Each fund has a maintained financial record: its investments and positions, cash, income, expenses, and liabilities. Mature products implement this as a real double-entry general ledger sitting under the investment record, so that portfolio positions and the books cannot silently diverge; every figure can be traced back to a source transaction. This books-of-record posture — reconciliation, audit trail, controlled approvals — is inseparable from the Type, because the output is relied upon by outsiders.

**Investor register with per-investor capital accounts.** Ownership is recorded per investor. Two regimes exist:

- open-ended funds: investors hold units/shares in one or more share classes or series, changed by subscriptions and redemptions priced at the fund's net asset value
- closed-ended funds: investors hold commitments; their capital account records contributed capital, distributions, allocated income and gains, and fees

The register is not a contact list — it is the accounting identity of each investor in the fund, and it changes only through recorded transactions.

**Recurring production of official financial output.** On a defined cycle (dealing period, month, quarter, fiscal year), the system converts accumulated activity into the fund's official financial picture:

- fund level: the net asset value per unit/share where the fund deals, or fund financial statements where it does not
- investor level: capital account statements, share/unit statements, and transaction notices

Both are derived from the same books — a single source of truth, so fund-level and investor-level numbers agree by construction.

### Standard capabilities around the core

Mature products commonly add:

- **Reconciliation machinery** — ingestion of custodian, broker, and pricing feeds; automated matching of positions and cash; an exception queue where breaks are worked rather than matched line-by-line; drill-down from any output figure to its source transaction.
- **Fee engines** — management-fee accrual and performance/incentive-fee crystallization per the fund's terms; in open-ended funds, class/series mechanisms such as equalization.
- **Allocation machinery** — allocation of income, gains, and expenses across share classes, series, side pockets, and investor capital accounts, per the fund's governing terms.
- **Waterfall engine** (closed-ended) — computation of carried interest and distribution splits modeled on the fund's partnership agreement.
- **Investor statements and notices** — capital account statements, capital-call notices, distribution notices, and preparation of annual partner tax forms in the relevant jurisdiction's format.
- **Investor portal** — a permissioned, usually branded surface where investors see documents, balances, and performance; increasingly also where they fulfill capital calls or update payment instructions.
- **Multi-entity, multi-currency structures** — master-feeder chains, parallel vehicles, side pockets, co-investment vehicles, consolidated or per-vehicle views.
- **Onboarding and compliance hooks** — subscription document handling, investor onboarding, identity verification (AML/KYC) before an investor enters the register.
- **Audit and tax handoff** — structured books and supporting records delivered to auditors and tax preparers; annual financial statement preparation.
- **Document ingestion** — the unstructured edge of the record: capital statements and notices from underlying funds that arrive as PDFs rather than feeds, extracted and posted to the books.

## How It Works

### Set up the fund and its terms

A fund is configured once: legal entities and currencies, share classes or commitment terms, the chart of accounts, fee terms, and (for closed-ended funds) the distribution waterfall. Investor onboarding follows: subscription documents are processed, identity checks pass, and the investor enters the register with an initial unit position or recorded commitment.

### Feed the books

Activity arrives from several directions:

- market activity — trades, settlement, corporate actions, income, expenses — often via custodian, broker, and pricing feeds
- investor activity — subscriptions/redemptions at dealing dates, or capital calls and distributions over the fund's life
- documents — statements and notices from underlying investments and banks, arriving on paper/PDF and posted (in current products, often by automated extraction) into the books

### Reconcile

Positions and cash in the books are matched against custodian records. Discrepancies surface in an exception queue and are investigated down to the source transaction. Nothing official is produced until the books agree with the outside world.

### Run the cycle

On the fund's defined cadence:

```text
Reconcile positions and cash
→ accrue fees (management, performance/incentive)
→ allocate income, gains, and expenses to classes/series and capital accounts
→ compute the fund's value
   (NAV strike per unit/share for open-ended funds;
    financial close for closed-ended funds)
→ review and approve
→ generate statements and notices
```

Open-ended funds repeat this every dealing period, because each subscription and redemption must be priced. Closed-ended funds run it at each reporting period, with capital-call and distribution events interleaved: a call is noticed, funded by investors, invested; a distribution is computed (often through the waterfall), paid, and recorded against capital accounts.

### Produce and deliver

Approved output is generated from the books: fund financial statements; investor statements and notices; performance metrics for investors and managers; audit and tax packs. Delivery is by portal, secure document delivery, or file transfer in the client's expected format. The period closes, and the cycle repeats.

### Two regimes, one loop

The open-ended loop (price → deal → restrike) and the closed-ended loop (commit → call → invest → distribute → waterfall) are different activity patterns over the same core: books, register, cycle, output. Products may specialize in one regime or support both.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Fund accountant workspace

The operator's primary surface.

- Purpose: maintain the books and run the cycle
- Typical information: fund selector, positions and cash, journals, reconciliation status, period status
- Primary actions: post or import transactions, work reconciliation exceptions, run allocations and fee calculations, strike NAV / close the period, generate output

### Reconciliation / exception queue

- Purpose: make the books agree with custodians and brokers
- Typical information: unmatched items on both sides, match confidence, source documents
- Primary actions: match, investigate with drill-down, adjust with audit trail

### Fund setup and terms configuration

- Purpose: encode the fund's structure and governing terms
- Typical information: entities, currencies, classes/series, fee terms, waterfall terms, accounting calendar
- Primary actions: configure, version, and maintain fund terms

### Investor register / capital accounts

- Purpose: hold each investor's accounting identity in the fund
- Typical information: commitments or units, contributed and distributed capital, allocated income and fees, transaction history
- Primary actions: record investor transactions, transfer or partially transfer holdings (product-dependent), correct with audit trail

### Statement and notice generation

- Purpose: produce official investor-level deliverables
- Typical information: statement templates, reporting periods, delivery lists
- Primary actions: generate, review, approve, publish

### Investor (LP) portal

- Purpose: give investors self-service access to what the books say
- Typical information: documents, capital account statements, fund performance, notices; sometimes call fulfillment and payment-instruction updates
- Primary actions: download, view, acknowledge or fulfill a call (product-dependent)

### Performance / dashboard views

- Purpose: summarize the fund and the book of funds for the manager
- Typical information: returns (e.g., IRR-family metrics for closed-ended funds), NAV or balance trends, portfolio composition
- Primary actions: view, export, drill down

## Important Rules / Behaviors

### The books are the record of truth

Everything the system tells investors or auditors must trace to recorded, sourced transactions. Output figures carry drill-down to source; changes happen through journals with audit trails, not silent overwrites. Approval steps typically separate preparation from sign-off.

### The register and the books agree by construction

A subscription, redemption, capital call, or distribution posts to both the fund's books and the investor's capital account in one movement. Fund-level and investor-level numbers therefore reconcile without a separate matching exercise — the defining contrast with spreadsheet-assembled reporting.

### Nothing official ships until reconciliation passes

Reconciliation exceptions gate the cycle. An unrestriked NAV or an unclosed period blocks downstream statements; this gate is the platform's main operational discipline.

### Fees and allocations follow the fund's own terms

Management and performance fees, equalization, allocations, and waterfalls are computed from configured terms (the fund's governing documents), not from platform defaults. The same platform runs funds with materially different fee and distribution mechanics.

### Investor changes are transactional

The capital account changes only through recorded transactions with defined effective dates (dealing date, call date, distribution date). Corrections are themselves recorded, preserving the audit trail.

### Access is permissioned and the posture is audit-facing

Role-based access separates preparation, approval, and administration; investor portal access is scoped to each investor's own data. Products commonly align with independent-audit control frameworks (e.g., SOC examinations), reflecting that their output is an audit input.

## Variants

- **Operating model** — the largest variant:
  - *administrator-side software*: a multi-tenant platform where an independent administration firm runs many isolated client books
  - *administered service*: the vendor runs the books on its platform, with the manager consuming results (outsourced fund administration)
  - *manager-side software*: the fund's own finance team runs administration in-house, sometimes to "shadow" an external administrator
  - *co-sourcing* hybrids of the above
- **Fund regime** — open-ended/dealing funds (NAV cycle, subscriptions and redemptions, equalization) vs closed-ended/commitment funds (capital calls, distributions, waterfalls); some products support both on one ledger.
- **Asset class tuning** — hedge funds, private equity, venture capital, private credit and CLOs, real assets/real estate, fund of funds, special-purpose vehicles.
- **Regulatory wrapping** — jurisdiction-dependent additions such as depositary or AIFM services (European regimes), entity/corporate services, and AML/KYC programs.
- **Adjacency bundling** — fund formation and closing support, treasury/payment execution, management-company accounting, tax return preparation, fundraising and investor-relationship tooling: frequently bundled, none definitional.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Investment Fund Accounting | the accounting/valuation leg of fund administration taken alone — fund books and NAV machinery without the investor register, statements, notices, and portal as first-class structures |
| Transfer Agency Platform | the official shareholder register and dealing machinery for (typically open-ended, registered) funds — the registry leg without the full books |
| Investor Portal | the LP-facing surface alone: documents, balances, performance — without maintaining the books it reports from |
| Portfolio Management System | front-office investment decisions and monitoring; not the official record and not investor-facing |
| Accounting Software / General Ledger System | a general corporate ledger; lacks NAV-per-class computation, capital accounts, allocations, and waterfall machinery |
| Private Market Investment Platform / Deal Management for PE/VC | deal pipeline and portfolio operations on the front-office side; no books of record |
| Wealth Management Platform | serves advisors and end clients' household portfolios, not fund-level books of record |
| Nonprofit Fund Accounting | different sense of "fund" — restricted-purpose ledgers in nonprofit accounting; no pooled investor capital, no NAV |

The most important seam is with **Investment Fund Accounting**: fund administration is the umbrella that carries fund accounting plus the investor-side legs (register, statements, notices, portal). If a product keeps the books but drops the investor-side structures, it has become fund accounting; if it keeps the register and dealing but drops the books, it has become transfer agency.

## Representative Products

- FundCount — unified fund accounting and administration platform used by administrators and funds, open- and closed-ended
- Juniper Square — administration service and platform for private-markets GPs
- Carta — fund administration suite and service for venture and private equity funds
- Allvue Systems — alternative-investment suite (fund accounting module) serving GPs and fund administrators
- Alter Domus — global third-party fund administrator (service provider with companion technology)

The core model was checked across the software-for-administrators, GP-side service, GP self-service, and outsourced-service poles, and across open- and closed-ended fund regimes, to avoid over-fitting to one packaging.

## Sources

Research date: **2026-09-07**

- FundCount — https://fundcount.com/ ; https://fundcount.com/industries/fund-administration/
- Juniper Square — https://www.junipersquare.com/ ; https://www.junipersquare.com/solutions/administration ; https://www.junipersquare.com/solutions/administration/fund-accounting
- Carta — https://carta.com/fund-management/ ; https://carta.com/fund-management/fund-administration/
- Allvue Systems — https://www.allvuesystems.com/ ; https://www.allvuesystems.com/solutions/fund-accounting/
- Alter Domus — https://www.alterdomus.com/

> Sourcing limitation: vendor marketing/product pages and workflow descriptions were reachable; screen-level help-center articles were not. Precise operational parameters (numeric limits, default cycles, exact state names, pricing) are intentionally not asserted. One major administrator-software vendor (SS&C) was unreachable (403) and no claims rest on it.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
