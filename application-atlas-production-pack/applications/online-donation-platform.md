# Online Donation Platform

## Overview

An **Online Donation Platform** is the system through which a charitable organization operates an always-available, donor-facing giving capability on the internet: a donation form, page, button, or app through which anyone can make a gift to the organization at any time. The platform records each gift as an attributable donation — an amount, one-time or on a schedule, commonly directed to a chosen cause or fund — settles the money to the organization, produces the receipt and tax documentation, and gives the organization a console over the whole stream of gifts.

The defining structure is small:

```text
Standing donor-facing give capability (evergreen form / page / button / app)
└── Donation recorded as a gift (amount · frequency · donor · designation · payment)
    └── settled to the organization's own money destination
        └── Organization-side giving console
            (operate the surfaces · manage gifts · receipts · payouts · reporting)
```

Everything commonly associated with modern donation products — recurring giving plans, donor-covered fees, suggested amounts, tributes, wallets, crypto, AI-suggested asks, campaign and peer-to-peer modules — is widespread in current products but is not what makes a platform a donation platform. Remove the campaign machinery and a donation platform remains; remove the standing give capability and what is left is campaign software, not this Type.

## Users & Context

Two sides use the same platform, with opposite postures:

**Donors (public side).** Individuals who arrive from the organization's website, emails, social posts, or an app, and give. Their whole interaction is the giving flow: choose an amount, choose one-time or recurring, optionally choose a designation or make the gift in someone's honor, pay, and receive confirmation and a receipt. Most products optimize this flow heavily for phones.

**Organization staff (operating side).** The people accountable for giving revenue and its record:

- **development / fundraising staff** — create and edit donation forms and pages, set suggested amounts and designations, watch results, and pull reports
- **finance / bookkeeping staff** — reconcile deposits, export or sync gift records into accounting, and produce tax-time documentation
- **administrator** — connects the payment account, configures receipts, and manages integrations to the organization's CRM or donor database

The typical context: a nonprofit, charity, church, or similar organization that cannot build and maintain its own payment-and-receipting infrastructure, and instead rents the giving capability as a platform. The donation platform is the **capture layer** at the edge of a wider nonprofit stack — gifts flow in here, then hand off to donor databases, CRMs, and accounting.

## Core Model

### The Defining Core

Three structures, held together. If any one is removed, the product is no longer recognizable as an online donation platform.

- **The standing give capability.** A persistent, organization-controlled surface that accepts gifts at any time — not bound to a campaign, deadline, or event. It may be a form embedded in the organization's website, a hosted page at the platform's domain, a button or snippet installed on the site, or an entry in a giving app. Evergreen availability is the point: this is the organization's permanent giving front door.
- **The gift as the transaction of record.** Each capture event is recorded as a charitable gift by an identified (or explicitly anonymous) donor: an amount, a frequency (a one-time gift or a gift on a schedule), commonly a chosen designation, and a payment. The gift belongs to the organization's stream of donations and the money settles to the organization's own account. The gift — not a purchase, not a pledge, not a ticket — is the center object of the Type.
- **The organization-side giving console.** The organization does not merely paste a widget; it operates the give capability through the platform. It creates and configures capture surfaces (amounts, designations, branding, receipt behavior), and it manages the results: the list of donations received, receipts and tax documentation, payouts and deposits, a light donor surface, and reports. The platform, not the organization's staff, is the system of record for the giving flow.

**One structure, many implementations.** These concepts are realized differently across products:

```text
Concept:  Standing give capability
Realizations:  form embedded in the org's site, hosted donation page,
               installable button/snippet, consumer giving app, text-to-give

Concept:  Money settlement
Realizations:  platform processes payments and pays the org, or the org
               connects its own payment account and money flows there directly

Concept:  Donor identification
Realizations:  contact details entered at checkout, recognized returning
               donor, app account — with explicit anonymous giving where offered
```

### Standard Capabilities

Mature products commonly add the following. They make the Type practical; they do not define it.

- **Donation forms as configurable objects** — the organization builds forms and pages: preset and suggested amounts, one-time vs recurring toggles, designation choices, branding, custom questions.
- **Recurring giving plans** — donors opt into scheduled giving (commonly monthly); products commonly encourage the upgrade at checkout, and give donors a self-service place to manage their plan, payment method, and receipts. Failed charges are commonly retried automatically.
- **Receipts and tax documentation** — confirmation and receipt at the point of giving, donor-accessible receipts and tax documents, and year-end giving reports; in some regions the platform supports the jurisdiction's giving-tax regime (such as Gift Aid-style claims).
- **Designations / causes / funds** — organization-defined purposes a gift can be directed to, which later let the organization split and report its giving.
- **Donor records** — the platform keeps a light record of who gave what, and connects outward: native integrations, sync, or export into donor databases, CRMs, and accounting systems. The deep relationship record belongs to those systems, not here.
- **Reporting** — gifts by period, donor, designation, form, and campaign, for both development and finance audiences.
- **Donor-covered fees** — the option for the donor to add the processing cost to their gift.
- **Mobile-first experience and digital wallets** — phone-first forms and one-tap wallet payment are the modern default.
- **Recovery and conversion machinery** — suggested ask amounts and impact descriptions are common; abandoned-gift recovery (capturing contact details mid-checkout and following up) is offered by several mature products.
- **Refinements offered by some products** — tribute or memorial gifts, matched-giving windows, address validation, custom questions.

## How It Works

### Set up the give capability

```text
Organization signs up and connects its money destination
→ builds donation form(s) / page(s) / installs button or snippet
→ sets amounts, one-time vs recurring, designations, branding, receipt behavior
→ give capability goes live — evergreen, on the org's site or as its own page/app
```

There is no campaign that must exist for the capability to work; the form is the standing front door.

### A donor gives

```text
Arrive at the form/page/app (from the org's site, email, social, or app)
→ choose an amount (preset or custom)
→ choose one-time or scheduled giving
→ optionally: choose a designation, dedicate the gift, cover the fees
→ pay (card, wallet, bank transfer — product-dependent)
→ confirmation + receipt issued
→ gift recorded: amount · frequency · donor · designation · payment · form of origin
```

This loop is the heart of the Type. Everything the platform does afterwards — records, receipts, payouts, reports — hangs off the gift recorded in this loop.

### Recurring giving as a managed plan

```text
Donor opts into scheduled giving (often prompted during or right after a gift)
→ platform charges on schedule; failed charges commonly retried
→ donor can manage the plan (amount, payment method, pause/cancel) in a self-service portal
→ organization can see and report on the recurring population
```

### The organization manages the stream

```text
Open the console
→ review donations as they arrive (list, donor, amount, designation, form)
→ monitor payouts/deposits and reconcile with accounting (export or sync)
→ issue or retrieve receipts and tax-time documentation
→ read reports (by period, donor, designation, form)
→ edit forms and settings as fundraising needs change
```

### Core vs standard vs optional

- **Defining core** — standing give capability; gift as transaction of record settled to the organization; organization-side console over the flow.
- **Standard capabilities** — configurable forms, recurring plans, receipts/tax documents, designations, donor records with outward sync, reporting, donor-covered fees, wallets, mobile-first checkout.
- **Optional / variant** — tribute gifts, matched giving, abandoned-gift recovery, crypto and non-cash rails, discovery marketplaces, white-labeling, regional tax regimes, campaign/peer-to-peer/event modules.

## Interfaces

### Donation form / checkout

The donor's primary surface and the product's most engineered interface.

- purpose: convert a visitor into a recorded gift
- typical information: organization brand and story elements, amount choices, frequency choice, designation options, fee-coverage option, payment methods, tribute or dedication fields
- primary actions: enter amount, choose frequency and designation, pay, receive receipt

### Organization console

The staff-side surface where the platform is operated.

- purpose: run the giving capability and manage its results
- typical information: donation list and totals, donor lookups, payout/deposit status, form inventory, reports
- primary actions: create/edit forms, configure amounts/designations/receipts, view and export gifts, reconcile deposits, run reports, manage integrations

### Donor self-service portal

Where one exists (common in mature products), the donor manages their side of the relationship.

- purpose: let donors manage recurring plans and retrieve their own documents
- typical information: giving history, plan details, downloadable receipts/tax documents
- primary actions: update payment method, change or pause a plan, download receipts

### Reporting / analytics view

- purpose: read the giving stream
- typical information: totals and trends by period, donor, designation, form, campaign
- primary actions: filter, segment, export

### Embedded and app surfaces

The same give capability delivered as a snippet inside the organization's website, a hosted page, a mobile giving app, or text/QR entry points. The surface changes; the gift loop does not.

## Important Rules / Behaviors

- **The gift is voluntary; there is no receivable.** Unlike dues or invoices, nothing is owed. A recurring plan is a standing authorization the donor can change or stop, not a bill. This is the structural line between donation platforms and membership-billing or invoicing Types.
- **The organization is the beneficiary of record.** Gifts settle to the organization's own money destination — whether the platform processes the payment and pays out, or the organization connects its own payment account and money flows straight there. The platform may hold the money transiently; the claim on it is the organization's.
- **Receipting follows the gift.** The receipt/tax document is generated from the recorded gift, not entered by hand afterwards; in tax-regulated markets the gift record must carry what the regime requires (donor identification, date, amount). The exact regimes and documents vary by country and are a variant, not the core.
- **Donor identity is thin by design.** A gift can usually be completed with minimal contact details, and anonymity is commonly offered. The platform keeps a light donor record and hands richer relationship-keeping to connected systems.
- **Capture surfaces are org-configured.** What donors may choose — amounts, designations, frequency — is defined by the organization in the console; the donor-facing form is a rendering of those settings.
- **Payments can fail.** Failed card charges, abandoned checkouts, and lapsed recurring plans are normal operating conditions; mature products build retry and recovery machinery around them.

## Variants

- **Embed-first platforms** — the capability lives inside the organization's own website as a snippet or form; the donor may never see the vendor.
- **Hosted-page platforms** — forms and pages live on the platform; the organization links or QR-codes to them.
- **App-first giving** — a consumer giving app carries the flow, sometimes with a discovery layer where donors find organizations to support.
- **Platform-processed vs bring-your-own-processor money flow** — both poles are established in the market; the platform's gift layer is the constant.
- **Congregational specialization** — churches use the same skeleton (gifts, designations, recurring, receipts) with a distinct object layer: giving attributed against member records, congregational funds, and year-end giving statements; this is documented as the church-giving Type.
- **Suite-packaged pole** — donation capture sold as one line of a wider giving platform (with events, peer-to-peer, auctions, CRM) rather than as a standalone product.
- **Regional breadth variants** — multi-currency/multilingual global products vs region-focused ones carrying specific national giving-tax regimes.

## Related Application Types

| Type | Relationship | Distinction |
|---|---|---|
| Donor Management System | closest sibling, other side of the seam | org-side constituency database (constituent → history → cultivation) vs donor-facing collection flow; each embeds slices of the other; the system-of-record side separates them |
| Nonprofit Crowdfunding Platform | sibling, campaign-centered | a campaign container with public crowd progress is the center there; here the evergreen gift transaction is the center — crowdfunding platforms ship standing donation forms as suite overlap, and donation platforms ship campaign modules |
| Peer-to-peer Fundraising Platform | sibling, supporter-centered | supporters run their own fundraising pages there; here the organization runs the give capability and supporters appear only as optional modules |
| Fundraising Management Platform | sibling, program-centered | org-side machinery across the whole fundraising program (campaigns, appeals, events, performance) vs the standing capture flow |
| Church Giving Platform | vertical specialization | same skeleton, but giver attribution anchored in member records, congregational funds vocabulary, and year-end statements as a first-class deliverable |
| Payment Gateway / Checkout Platform | underlying infrastructure | moves money but holds no gift semantics — no designations, tribute, recurring giving plans, receipts, or org giving console |
| Event Registration / Ticketing | adjacent | sells attendance (purchase semantics, capacity); donation platforms record gifts; donation upsells at registration are a bridge, not fusion |
| Membership Billing | adjacent | dues are owed by right of membership; gifts are voluntary with no receivable |
| Nonprofit CRM / Nonprofit Management Platform | suite umbrella | the relationship spine or whole-operations suite; donation capture is the donor-facing module feeding it |
| Consumer/personal crowdfunding | different beneficiary | money to a person or rewards project vs gifts settling to an organization for a charitable purpose |

The Type's center is the **transaction**. The campaign (crowdfunding), the supporter page (peer-to-peer), the program machinery (fundraising management), the constituency database (donor management), and the congregational layer (church giving) are each a different center — which is why the family stays separate Types even though vendors package them together.

## Representative Products

- **Fundraise Up** — enterprise checkout-optimized donation platform installed on the organization's website
- **Bloomerang Fundraising (formerly Qgiv)** — mid-market giving platform whose donation forms line sits beside events, text, peer-to-peer, and CRM
- **Givelify** — app-first giving platform serving both churches and nonprofits, with a donor-side discovery layer
- **Raisely** — lightweight embed-or-share donation forms with bring-your-own payment account, multi-region

## Sources

Research date: **2026-09-08**

- Fundraise Up — https://fundraiseup.com/ , https://fundraiseup.com/features/checkout/
- Bloomerang Fundraising (formerly Qgiv) — https://www.qgiv.com/ , https://www.qgiv.com/donation-forms
- Givelify — https://www.givelify.com/ , https://www.givelify.com/organizations/solutions/giving/ , https://www.givelify.com/organizations/solutions/donor-management/
- Raisely — https://raisely.com/ , https://raisely.com/online-giving

> Sourcing limitation: official product pages (marketing/feature level) were the reachable layer for all four products on 2026-09-08; help-center-level documentation could not be fetched (Donorbox, GiveWP, Givebutter blocked; Qgiv and Fundraise Up help sites unreachable). Precise operational facts — fee levels, payout schedules, receipt timing, plan limits — are therefore intentionally not stated in this document. Vendor marketing statistics are excluded. Claims are calibrated to what product pages state and to cross-product commonality.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the historical/market-sample check are recorded in the paired Research Notes.
