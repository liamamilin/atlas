# Investment Fund Accounting

## Overview

An **Investment Fund Accounting** system is the official books of record for investment funds and investment portfolios: it keeps a general ledger in which the vehicle's investment activity and its capital activity post as one reconciled accounting record, applies fund-specific accounting machinery to that record, and runs a governed periodic close that produces the vehicle's authoritative financial outputs — NAV where the regime provides, financial statements, investor capital statements, tax packs, and journal-ready feeds to the corporate accounting system.

It answers a question generic accounting software cannot: *what does this fund own, at what value, what does each investor's capital account say, what fees have accrued, and what do the official books and statements look like this period?*

Its boundary is equally specific. It does not maintain the investor register or process subscriptions and redemptions (that is the register leg of fund operations), it does not make or support investment decisions (that is the front office), and it is not the management company's own corporate books. It is the books leg of fund operations — the slice that turns fund activity into official accounting.

## Users & Context

Primary users are fund-accounting professionals — the people whose work product is the official books:

- **fund accountant / controller**: posts and reviews transactions, runs valuations and accruals, strikes NAV or closes the period, produces financial statements
- **administrator's accounting team**: runs the same books on behalf of many client funds, often multi-tenant
- **CFO / financial controller of the manager**: owns the close, signs off on the outputs, answers auditors and investors from the books

Secondary users:

- **auditors and tax preparers**: consume the books, capital statements, and tax outputs
- **investor-facing teams**: receive the outputs (capital statements, reports) for delivery — the delivery itself belongs to adjacent surfaces

The work environment is a periodic-cycle rhythm: daily or intraday data capture, then a recurring close (daily, monthly, quarterly, or per dealing period depending on the fund regime). The asset-owner variant (an insurer's or pension's investment portfolio) is operated by the institution's finance and accounting team on the same books-and-close pattern.

## Core Model

### The Defining Core

```text
Fund / Investment Entity
└── Official Books of Record (investment-aware general ledger)
    ├── Investment Portfolio Accounting
    │     positions · trades · corporate actions · income · cash · valuations
    ├── Investor / Partner Capital Accounts        (fund pole)
    │     contributions · distributions · transfers · allocations
    ├── Fund-Specific Accounting Machinery
    │     fair value · multi-book / multi-basis · multi-currency
    │     fee accruals · waterfalls · NAV per share/unit/class
    └── Governed Periodic Close
          reconcile → value → accrue → allocate → strike NAV / close
          → financial statements · capital statements · tax packs · GL feeds
```

Three structures, jointly held. Remove any one and the product stops being this Type:

- **Official books of record.** The investment record and the accounting record are the same record: trades, corporate actions, income, and cash post to the ledger as accounting entries, so the books are reconciled by construction rather than assembled from a separate position system. Without this, the product is a portfolio management system or a data feed, not the books.
- **Fund-specific accounting machinery.** The portfolio is held at fair value under treatments generic ledgers do not carry: multiple accounting books and bases (GAAP, statutory, IFRS, tax, local regimes) kept concurrently, multiple currencies, fee accruals (management, incentive, carry), and — in the fund pole — investor/partner capital accounts with allocation and waterfall logic producing NAV per share, unit, or class. Without this, the product is generic accounting software.
- **The governed periodic close.** A recurring, controlled cycle — reconcile, value, accrue, allocate, strike NAV or close the books — that ends in the vehicle's authoritative financial artifacts. Without it, the product is an analytics or reporting shell over data that never becomes official.

The binding is investment-fund semantics: the subject is pooled investment vehicles and investment portfolios under fund and investment accounting regimes. Remove it and the same ledger machinery is just corporate accounting.

### What Mature Products Add

These capabilities are widespread but do not define the Type:

- **automated data feeds** — custodian, broker, administrator, and market-data feeds flowing into the books daily
- **reconciliation and exception management** — systematic comparison of feeds against the books, with exception queues and workflow
- **waterfall and allocation engines** — configurable tiered waterfalls, preferred returns, catch-ups, deal-by-deal versus whole-fund carry
- **tax machinery** — partnership tax allocations and investor tax documents generated from the ledger (in regimes that provide them)
- **regulatory-basis reporting** — templates for statutory and regulatory frameworks, updated as regimes change
- **shadow accounting** — the manager keeping its own books to shadow the administrator's official books, for oversight and independence
- **governance and controls** — roles, approval workflows, versioning, audit logs, drill-down from any statement to its source entries
- **performance outputs** — returns and metrics computed from the same books
- **AI document ingestion** — extracting positions and transactions from statements and agreements into the books

### One Structure, Many Implementations

```text
Concept:   Official books of record
Forms:     standalone portfolio-accounting system · accounting module inside
           an investment platform · multi-tenant tool of a fund administrator ·
           asset-owner accounting service

Concept:   Investor / partner capital accounts
Forms:     partnership capital accounts with waterfall allocations (closed-ended)
           shareholder accounting with NAV per class/series (open-ended)
           absent — single-owner entity books (asset-owner pole)

Concept:   The periodic close
Forms:     daily ABOR close with multi-basis books (asset owners)
           monthly/quarterly close with NAV strike (open-ended funds)
           quarterly/year-end close with capital statements and tax packs (closed-ended)
```

## How It Works

### Capture activity into the books

```text
Feeds and manual entry
→ custodian/broker positions, transactions, cash, prices
→ fund capital activity (capital calls, distributions, commitments, transfers)
→ fees and expenses
→ all posted as accounting entries to the fund's ledger
```

The defining property is that investment activity and capital activity land in the same ledger. There is no parallel position system to reconcile against the books by hand; the capital account is a view of the ledger, not a separate workbook.

### Apply the fund-specific machinery

```text
Value the portfolio at fair value (prices, models, private-asset treatments)
→ accrue fees (management fees on the agreed base; incentive/carry per the
  fund's terms)
→ run allocations (income and gains to investor/partner capital accounts
  under the fund's waterfall and allocation rules)
→ maintain parallel books where required (GAAP / statutory / IFRS / tax,
  concurrently, per currency)
```

This is the layer generic accounting software lacks. The allocation logic — who owns what share of what gain, when carry crystallizes, how a partial investor transfer re-bases capital — is the system's core competence, held as configuration rather than as spreadsheets beside a ledger.

### Run the periodic close and produce official outputs

```text
Reconcile feeds and books; clear exceptions
→ value, accrue, allocate
→ strike NAV (open-ended funds: per fund/class/series) or close the period
→ generate the official artifacts:
     financial statements · NAV · investor capital statements ·
     tax documents · journal-ready entries for the corporate ERP
→ retain the audit trail; the books stand as the record of what happened
```

The close is governed: validated data, approval steps, versioning, and drill-down from any output to its source entries. The outputs are authoritative — auditors, regulators, and investors rely on them, and downstream systems (corporate GL, consolidation, reporting) consume them rather than re-derive them.

### Core vs Common vs Optional

**Defining core** — without these, not investment fund accounting:

- official books of record holding the investment portfolio and capital activity as one accounting record
- fund-specific accounting machinery (fair value, multi-book/multi-basis, multi-currency, fee accruals; capital accounts with allocations in the fund pole)
- the governed periodic close producing official financial outputs

**Common mature structure** — present in most modern products:

- automated custodian/broker/market-data feeds
- reconciliation and exception workflows
- waterfall/allocation engines
- tax machinery and investor tax documents
- regulatory-basis reporting templates
- governance, audit trail, drill-down
- performance outputs from the books

**Variant / optional** — depends on fund regime, asset class, operating model, era:

- NAV-per-class/series/side-pocket machinery (open-ended pole)
- commitment/call/distribution/waterfall machinery (closed-ended pole)
- multi-basis daily ABOR close (asset-owner pole)
- shadow-accounting posture (manager-side books)
- multi-tenant operation by third-party administrators
- cloud delivery, AI document extraction, AI assistants

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Fund / entity workbench

The operator's home surface for one fund or a book of funds.

- fund structures, entities, and their accounting state; close status and outstanding exceptions
- primary actions: open a fund's books, post or review entries, launch cycle steps

### Portfolio accounting surface

The investment record inside the books.

- positions, transactions, corporate actions, valuations, cash, by account and currency
- primary actions: post/review transactions, load prices and valuations, run corporate-action processing, reconcile to feeds

### Capital-account / partnership accounting surface

The investor-side record (fund pole).

- capital accounts per investor/partner, contributions, distributions, transfers, allocations, fee and carry calculations
- primary actions: process capital activity, run allocations and waterfalls, generate capital statements

### Close / period-control surface

The governed cycle.

- period status, reconciliation state, exceptions, approvals, task progression
- primary actions: run reconciliation, clear exceptions, approve, strike NAV / close, lock the period

### Reporting and statement generation

- financial statements, NAV reports, capital statements, tax documents, regulatory-basis reports; library plus custom report writer
- primary actions: generate, review, approve, export, deliver

### GL integration / export

- journal-ready entries mapped to the corporate ERP or general ledger; configurable logic and mapping
- primary actions: configure mappings, produce and transmit journals

## Important Rules / Behaviors

### The books are the record, not a view

Investment and capital activity post as accounting entries; statements are generated from the ledger, not re-assembled from separate systems. This is the structural property that separates the Type from a position system plus a spreadsheet.

### Allocation logic is the hard part

Who owns what share of income and gains, how fees and carry accrue and crystallize, and how partial investor transfers re-basis capital are fund-specific rules held as configuration. Generic ERPs cannot express them; getting them wrong misstates every investor's account.

### Parallel books are normal

The same activity is frequently carried on multiple bases simultaneously (GAAP, statutory, IFRS, tax) and in multiple currencies. The system maintains these as concurrent books of one record, not as copies.

### The close is gated

Official outputs are produced through a controlled cycle — validated data, reconciliation, approvals, versioning. A statement issued from un-reconciled books is the failure mode the governance machinery exists to prevent.

### The register is not here

Investor identity, subscriptions, redemptions, and the authoritative holder record belong to the register leg of fund operations. This system consumes capital activity as accounting events; it does not own who the investors are or process their dealings.

### Shadowing is a posture, not a conflict

When both the administrator and the manager keep books, the manager's system is run deliberately to mirror and check the official books — independence and oversight, not duplicate truth.

## Variants

- **open-ended fund accounting** — dealing-fund regime: NAV per share/unit/class, classes and series, fee crystallization on dealing periods; the classic hedge-fund and mutual-fund form
- **closed-ended / private-capital fund accounting** — commitment-based regime: capital calls, distributions, waterfalls, carry, partnership tax allocations; the PE/VC/private-credit form
- **asset-owner investment accounting** — no investor capital accounts; the institution's portfolio carried on multi-basis books (GAAP/statutory/IFRS/tax) with a daily close and regulatory reporting; the insurer/pension/corporate-treasury form
- **administrator-operated (multi-tenant)** — the same books run at scale on behalf of many client funds
- **shadow accounting** — manager-side books maintained alongside an external administrator's official books
- **asset-class specializations** — loans and private credit, derivatives, real estate, fund of funds; each adds instrument-level accounting depth

A variant remains a Variant unless it changes the defining core; adding the investor register, dealing machinery, and investor-facing services moves a product into fund administration — a different Type despite the shared subject.

## Related Application Types

| Application Type | Distinction |
|---|---|
| Fund Administration Platform | the umbrella: official books **plus** investor register, dealing, and investor services; remove those services from it and what remains is this Type |
| Transfer Agency Platform | the register leg: securityholder register, register-maintaining transactions, holder servicing; no portfolio books or NAV at its center |
| Investment Management Platform | the whole front-to-back lifecycle (decision → execution → reporting); this Type is its back-office books slice and holds no front-office objects |
| Portfolio Management System | decision support and portfolio monitoring; positions without the books; the market itself runs the two as separate systems reconciled across a boundary |
| Performance & Attribution Platform | measurement and analysis of returns; consumes the books, does not produce them |
| Accounting Software / General Ledger System | generic corporate ledger; cannot hold portfolios at fair value, compute NAV per class, accrue incentive fees, or run LP waterfalls |
| Corporate Accounting (management-company books) | sibling books for the manager's own entity; integrates with but is distinct from the fund's books |
| Nonprofit Fund Accounting | terminology false friend: restricted-fund ledgers for donor-restricted resources; no pooled investor capital, no NAV, no valuation machinery |
| Investor Portal | a delivery surface for the outputs; the books stand without it |

The most important boundary is the trio: fund administration (umbrella) / investment fund accounting (books leg) / transfer agency (register leg). The accounting slice is what remains when the investor-facing legs are removed — and every sampled vendor sells or structures it as a distinct capability.

## Representative Products

- SS&C Advent Geneva — classic standalone portfolio and investor accounting for hedge funds and alternative managers
- Allvue Fund Accounting — cloud fund accounting for private-equity and credit managers and fund administrators
- FundCount — unified portfolio and partnership accounting on one ledger for hedge funds, PE, family offices, and administrators
- Clearwater Analytics (Investment Accounting) — asset-owner/asset-manager investment accounting on a daily multi-basis ABOR

## Sources

Research date: **2026-09-10**

- SS&C Advent — https://www.advent.com/ , https://www.advent.com/solutions/geneva/ , https://www.advent.com/solutions/?b=fund-accounting
- Allvue Systems — https://www.allvuesystems.com/ , https://www.allvuesystems.com/solutions/fund-accounting/
- FundCount — https://fundcount.com/ , https://fundcount.com/solutions/partnership-accounting/
- Clearwater Analytics — https://cwan.com/ , https://cwan.com/solutions/investment-accounting-reporting/

> Sourcing limitation: vendor help-center and operational documentation (exact close steps, state names, permission models, numeric parameters) was not publicly reachable for any sampled product on 2026-09-10. The workflow description rests on official product and solutions pages at structure level; precise operational parameters are intentionally not stated. Findings about open-ended fund mechanics rest primarily on one sampled product and should be cross-checked before further generalization.

Detailed evidence, product-by-product observations, cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
