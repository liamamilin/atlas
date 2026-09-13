# Church Giving Platform

## Overview

A **Church Giving Platform** is a church-administered system through which monetary contributions are given and recorded. It operates the channels by which givers give — an online giving form, a mobile app, text giving, in-person and kiosk giving — and records every contribution as a discrete gift: an amount, a received date, a payment method, a designated fund, and credit to a giver (a named person, or an explicit anonymous record for gifts that cannot be attributed). The church's staff administer the process: they define the funds, maintain giver records, review and correct gifts, and issue receipts and year-end giving statements.

The defining core is small:

```text
Giving channels operated by the church
└── Gift record (amount · date · method)
    ├── Giver attribution (identified giver, or anonymous record)
    └── Fund designation (the church purpose the gift supports)
        └── Church-side administration (funds, givers, corrections, statements)
```

Everything else commonly associated with these products — recurring tithing, pledge campaigns, text-to-give, kiosks, donor-covered fees, multi-campus reporting, regional tax-receipt formats — is standard capability that mature products carry, not what makes the product a giving platform. The historical check matters here: envelope-based offertory recording, in which each numbered envelope's contents were credited to a member and designated to a fund, satisfies this definition with a purely physical channel. Online payment is how the Type is usually delivered today, not what it is.

When the center of gravity shifts to managing the congregation's life (groups, classes, check-in, pastoral care), the product is a Church Management System that happens to include contributions. When the center is only moving money, with no giver credit, funds, or statements, it is a payment processor.

## Users & Context

**Church side (administrators of the giving process):**

- **Church finance staff / bookkeepers** — configure funds and settings, review donations, generate statements, export to accounting, handle refunds and corrections.
- **Counting teams / volunteers** — count and record cash and checks after services, often under restricted permissions that let them enter but not finalize gifts.
- **Pastors and church administrators** — view giving trends, run pledge campaigns, and use giving data as one signal of congregational engagement.

**Giver side (the congregation):**

- **Members** — give one-time or recurring gifts, designate them to funds, view their giving history, manage their payment methods and recurring schedules, and retrieve their statements.
- **Guests and visitors** — give without an account, typically from a link, QR code, or the church's app.

The usage rhythm is shaped by congregational life: giving peaks around weekend services (in-person and text giving moments), recurring gifts anchor the church's budget planning, and year-end statement generation is a fixed annual cycle. Multi-site churches administer giving across campuses; Catholic parishes and dioceses often use denominationally shaped variants.

## Core Model

### The defining core

**Gift.** The unit of record. Every contribution — card, bank transfer, text gift, cash, or check — becomes a gift record carrying at minimum an amount, a received date, and a payment method. The received date is consequential: it is the date the giver is credited, which matters at year-end boundaries. Gifts also carry method details (check number, card or account digits), optional memos expressing the giver's intent, and internal notes visible only to staff.

**Giver.** The person to whom gifts are credited. Givers are identified people records — in mature products, matched against the church's member database so that giving history lives on the person, not in an isolated payments silo. Two refinements appear in the researched sample: **joint givers** (two people, typically spouses, whose gifts are credited and stated together), and the **anonymous giver** — a standing record for loose cash or unidentified checks, so the money is still recorded and reported even though no person is credited. Anonymous giving is an offline-only mode in practice: digital gifts require a name and payment credential.

**Fund.** The church-defined purpose a gift supports — the general (discretionary) fund, missions, building, benevolence, and so on. Funds record the donor's intent, and every gift is designated to one (or split across several). A default fund receives undesignated gifts. Funds can be listed for donors, reachable only by direct link, or hidden for staff-only designation; they can be closed when a drive ends and reopened seasonally. Funds with giving history are typically preserved rather than deleted, and renaming is treated as a sensitive, logged action precisely because mislabeled funds misrepresent donor intent. Ledger codes connect funds to the church's chart of accounts.

**Church-side administration.** The church is not a passive recipient; it operates the process. Staff create and govern funds, maintain giver records, enter offline gifts, review and commit batches, correct or reassign gifts (normally with the giver's consent), issue receipts and statements, and report on the whole. This administrative half is what separates the Type from a checkout: the platform is the church's system of record for contributions, not merely its card reader.

### Standard capabilities

Mature products commonly add:

- **Recurring giving** — the dominant pattern for congregational giving: a scheduled gift (weekly, biweekly, monthly) that processes automatically, managed by the giver (pause, change amount or fund, cancel) and on the giver's behalf by staff, with failure notifications and card-update assistance.
- **Pledge campaigns** — a time-boxed commitment drive (a building fund, a missions pledge) that givers commit against and the church tracks toward a goal; pledge progress can appear on statements.
- **Giving channels** — the online form (embeddable, shareable as links and QR codes), the church's mobile app, text-to-give with fund shortcuts, and in-person hardware (card readers, kiosks, NFC taps).
- **Giver self-serve account** — giving history, saved payment methods, recurring-gift management, and statement downloads.
- **Guest giving** — giving without an account.
- **Receipts and statements** — an automatic receipt per gift (date, organization, amount, fund, gift identifier) and year-end giving statements for tax filing.
- **Reporting** — giving by fund, giver, campus, payment type, and period; deposit and payout views; recurring-income forecasting.
- **Offline recording** — cash and check entry in batches with counting roles and a commit step; check-reading hardware.
- **Integration** — sync with the church management system's people records; export or API into accounting.
- **Multi-campus** — gifts attributed to campuses without duplicating funds.
- **Donor-covered fees** — the option for givers to add the processing cost to their gift.

### One structure, many implementations

```text
Concept:  Giver attribution
Implementations:  member-database profiles, standalone donor accounts,
                  joint-giver records, anonymous-donor record,
                  numbered-envelope donor numbers (heritage, still supported)

Concept:  Fund designation
Implementations:  selectable fund dropdowns, direct fund links,
                  multi-fund split in one gift, text-give fund shortcuts,
                  campaign-linked funds

Concept:  Giving channel
Implementations:  web form, church app, donor app, SMS, kiosk,
                  card reader, NFC tap, QR code, paper envelope + counting batch

Concept:  Statement
Implementations:  per-gift email receipt, downloadable year-end statement,
                  printed mailed statements, jurisdiction-specific official receipts
```

A reader who has only seen a modern mobile giving flow should still be able to recognize an envelope-based offertory office as the same Type from the core model.

## How It Works

### The church sets up the giving process

Staff define the funds (with a default fund for undesignated gifts), configure the giving form and channels, connect the platform to the church's people records and accounting, and set roles — typically distinguishing full administrators from restricted entry roles. From this point the platform is the church's front door for money.

### A giver gives

```text
Open the giving form / app / text number / kiosk
→ choose amount and fund (or split across funds)
→ choose one-time or recurring
→ pay (card, bank transfer, wallet) — or hand cash/a check to the church
→ receive a receipt
```

Identified givers are credited automatically; guests give without an account; offline gifts are recorded by the church rather than processed. Recurring gifts, once created, process on their schedule without the giver present, and the giver (or staff) can pause, change, or cancel them; failed charges notify the giver — and, where configured, the church — rather than silently disappearing.

### Offline gifts are counted and recorded

Cash and checks follow a counting workflow with its own discipline:

```text
Create a batch (e.g., one per service or per counting team)
→ enter each gift: match the giver (or create/anonymous), amount, fund, method details
→ review
→ commit the batch
```

In products with a batch-commit workflow, gifts stay working entries until commit: invisible to givers, excluded from statements, and not yet triggering automations. Committing makes them fully qualified gifts — visible in giver history, included in statements, receipted, and logged. This two-stage design exists because counting is error-prone and the contribution record is consequential.

### Money settles; the record is maintained

Processed gifts settle to the church's bank account on the processor's schedule. Staff then work the record: refund gifts (fully or, where a split gift was made, by fund portion), reassign designated gifts when a fund closes (normally with the giver's consent), correct entry mistakes, and monitor failed recurring payments.

### Statements close the annual cycle

Per-gift receipts go out at giving time. At year-end, staff generate giving statements — choosing a date range, reviewing contact-data completeness, deciding email versus printed delivery, and optionally adding a cover letter. Statements include only successful, committed gifts; failed, refunded, and uncommitted entries are excluded. Once sent, statements are effectively immutable records, and givers can always retrieve their own statements from their profile.

### Reporting and integration run alongside

Throughout, staff report on giving by fund, giver, campus, and period; recurring-giving projections inform budgeting; and summaries flow outward — to the church management system (giving history on the person record) and to accounting (exports keyed by fund ledger codes).

## Interfaces

### Giving form / page (giver side)

The primary collection surface, reached from the church website, app, links, or QR codes.

- amount entry, fund selection (or multi-fund split), one-time vs recurring, payment method, optional cover-the-fees and memo
- primary actions: give, save/confirm a recurring schedule, receive receipt

### Giver self-serve (app or web profile)

The giver's own view of their giving.

- giving history, saved payment methods, recurring-gift management (pause/change/cancel), downloadable statements
- primary actions: give again, manage recurring, download statement, update contact/payment details

### Admin console (church side)

The staff surface where the record lives. Typical areas:

- **Donations** — the gift ledger: search, filter by fund/method/campus/period, inspect and correct gifts, refund
- **Donors / people** — giver profiles with giving history, recurring schedules, joint-giver links, donor numbers where used
- **Funds** — create/edit/close funds, visibility, ledger codes, descriptions
- **Batches** — in-progress and committed counting batches, batch defaults, commit/delete
- **Statements** — statement creation, deliverability review, email/print generation
- **Reports** — giving by fund/donor/campus/method, pledge progress, deposits, exports
- **Settings** — payment sources, permissions, tax disclaimers, integrations

### Text and in-person surfaces

Short-code or keyword text giving with fund shortcuts; kiosk or card-reader flows for in-service giving moments.

## Important Rules / Behaviors

- **The received date is the credit date.** A gift belongs to the period in which it was received, not when it settled or was entered; year-end statements turn on this rule, and staff are warned to commit batches before generating statements.
- **Uncommitted gifts do not exist for the giver.** Where a batch-commit workflow exists, batched cash and checks stay invisible to giver histories and statements until an authorized role commits them; the commit step is the boundary between a working entry and a contribution of record, and changes to committed records are audit-logged.
- **Statements exclude failed, refunded, and uncommitted gifts.** Only successful, committed gifts are stated — the statement is a tax document, and its contents are deliberately conservative.
- **Sent statements are effectively immutable.** Once issued, a statement typically cannot be edited; corrections require a new statement or direct resolution with the church.
- **Digital giving is never anonymous.** Online channels require a name and payment credential; anonymity exists as an offline recording mode for loose cash and unidentified checks.
- **Funds are preserved, not casually deleted.** Funds with history are commonly closed rather than deleted; renaming is commonly logged; reassigning a giver's designated gift normally requires the giver's consent or a refund.
- **Recurring gifts can outlive their fund's visibility.** A recurring gift may continue processing even if its fund is closed or hidden, until the giver or staff redirects it — so fund changes require donor communication.
- **Failed recurring payments are surfaced, not retried silently.** The giver is notified; the schedule continues at the next occurrence, and recovery is by the giver's action or a one-time make-up gift.
- **Giver data is sensitive.** Access to financial data is permission-gated (often with distinct entry-only roles for counting teams), and pastoral sensitivity extends to the record itself — for example, one product automatically pauses a deceased giver's recurring gifts.
- **Tax-statement formats are regional.** Statement content and official-receipt requirements (itemized totals, receipt numbers, signatures, address rules) vary by jurisdiction; the platform supplies templates, and the church remains the issuer of record.
- **Contributions, not commerce.** These systems typically exclude sales, ticketing, tuition, and reimbursements — other products in the church stack own those; mixing them into the contribution record would corrupt statements.

## Variants

- **Standalone giving platform** — the giving process as the whole product, integrated with whatever ChMS the church already runs.
- **ChMS-suite module** — giving as one product inside a church management suite, with native people-record integration (the record half and the collection half under one roof).
- **Engagement-platform module** — giving embedded in a broader church app/engagement product alongside content, groups, and events.
- **Donor-side marketplace** — a giver-first app in which donors discover and give to many organizations from one account; the church joins a network rather than owning its channels.
- **Denominational variants** — Catholic parish and diocese packaging (parish/diocesan hierarchies, offertory programs, separate recording and collection modules in some suites); other traditions shape vocabulary (tithes, offerings, stewardship) more than structure.
- **Regional variants** — jurisdiction-specific official receipts and statement formats; multi-language giving forms.
- **Scale variants** — small-church free-tier giving (transaction fees only) through enterprise multi-campus deployments with negotiated processing.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Online Donation Platform | closest generic sibling | same gift/designation/receipt skeleton, but giver identity is not anchored in a member database, congregational funds vocabulary and year-end statements are not the center, and ChMS integration is not standard; the church Type is the congregational specialization |
| Church Management System / ChMS | adjacent, deeply integrated | ChMS owns the congregation's life (people, groups, classes, check-in, pastoral care); the giving platform owns collection channels and the contribution record; they meet at the giver record, and ChMS products may embed a contributions module |
| Payment Processing Platform | underlying capability | a processor moves money but holds no giver credit, funds, or statements; some giving vendors vertically integrate processing, which is a business-model choice, not a Type boundary |
| Donor Management System | adjacent expansion | donor cultivation and relationship management across campaigns and communications; the giving platform's donor surface is limited to giving history, payment methods, and statements |
| Nonprofit Fund Accounting | downstream consumer | fund accounting keeps the books (restricted funds, ledgers); the giving platform records intent-level gifts and hands summaries over via ledger codes and exports |
| Membership Billing | different money semantics | dues are owed by right of membership (invoiced, receivable); gifts are voluntary with no billing obligation |
| Fundraising / Peer-to-peer Fundraising Platform | adjacent campaign tooling | event- and campaign-driven fundraising with supporter-led pages; the giving platform's center is the ongoing congregational giving relationship, not discrete fundraisers |

The most important boundary is with the generic Online Donation Platform: the two share most mechanics, and at least one product serves both markets from the same codebase. What keeps the church Type distinct is the member-linked giver record, the congregational funds model, the year-end statement obligation, and the ChMS integration fabric — a specialization with its own object model and vendor ecosystem, not merely a re-skinned donation form.

## Representative Products

- **Planning Center Giving** — giving as a module of a church management suite; record-keeping depth (funds, batches, statements) with Church Center as the giver surface
- **Tithe.ly** — giving-first suite for small and mid-size churches; free giving tier with a bundled church platform
- **Pushpay** — enterprise, mobile-first giving for large and multi-site churches; owns its processing stack
- **Givelify** — donor-side giving app spanning many organizations; the marketplace pole of the Type
- **Vanco** — long-standing faith-payments heritage; online giving with broad ChMS integrations

The core model was also checked against a denominational heritage sample (a Catholic parish management suite with separate offertory-recording and online-giving modules, and with numbered-envelope donor identification still supported inside modern products) to avoid defining the Type by the current mobile-payment implementation alone.

## Sources

Research date: **2026-09-07**

- Planning Center — Giving product page: https://www.planningcenter.com/giving ; Help Center articles: Import donation history, Create and manage funds, Batches, Anonymous donors and loose cash, Donor numbers, Create and share donor statements, Recurring donations (help.planningcenter.com)
- Tithe.ly — product site: https://tithe.ly/ ; Support Center: Donors category, How to Use Multi-Fund Giving, Donation Receipts and Tax Receipts For Donors (support.tithe.ly)
- Pushpay — https://www.pushpay.com/ , https://pushpay.com/product/church-giving/
- Givelify — https://www.givelify.com/ , https://www.givelify.com/organizations/solutions/giving/
- Vanco — https://www.vancopayments.com/
- ParishSOFT — https://www.parishsoft.com/

> Sourcing limitations: Pushpay's and Givelify's help centers were not reachable during research, so observations for those products rest on official product pages and are stated more cautiously than Planning Center and Tithe.ly observations, which draw on official help-center articles. One candidate product (Subsplash Giving) was dropped after repeated fetch failures, and one vendor page (Vanco product page) returned an error, leaving only its root site. Precise fees, limits, and plan details observed during research are intentionally not asserted in this document; they are recorded in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
