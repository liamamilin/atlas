# Broker Management Platform

## Overview

A **Broker Management Platform** is the back-office system an insurance brokerage (or independent insurance agency) runs its business on. It maintains the firm's **book of business** — its clients, the insurance policies placed for those clients with external insurers, and the money those placements generate — and moves every policy through a recurring lifecycle of new business, mid-term change, renewal, and cancellation.

The defining structure is small:

```text
Client records
└── Policy records
    │   each binding one client × one external insurer's product
    │   × its terms (cover, premium) × a policy period
    └── Renewal-driven lifecycle
        (new business → in force → mid-term change → renewal → cancel / lapse)
```

The firm behind the system is an **intermediary**: it does not carry the risk itself. It places each client's risk with an insurer, keeps the record of that placement, and earns commission (and sometimes fees) from the insurer for the business it brings. Everything else commonly found in these products — quote tooling, insurer data feeds, commission reconciliation, accounting, document generation, task management, sales pipelines, client portals — is standard capability that mature products add around this core, not what makes the product a broker management platform.

When the system's center of gravity shifts to the insurer's own master policy records and underwriting authority, it has become a different Application Type (Insurance Policy Administration System, Underwriting Workbench). When it shifts to producing quote transactions without holding a persistent book, it is a quote platform, not a management platform.

## Users & Context

The system is the operational hub of a brokerage firm. Typical roles:

Primary users:

- **account executive / producer** — owns client relationships, wins new business, places risks with insurers, is paid in commission splits
- **account handler / customer service representative** — services the in-force book: policy changes, documents, certificates, renewal preparation, client queries
- **accounts / finance staff** — collect premiums, reconcile commission statements, run client ledgers and month-end close

Secondary users:

- **compliance / operations leadership** — oversees audit trails, documentation standards, and (in some markets) client-money rules
- **managers / principals** — read the book: production by insurer and producer, retention, pipeline, financial health

The work is deadline-driven by the insurance calendar: policies expire and must be renewed before they lapse, insurers issue statements that must be reconciled, and clients demand documents (proof of insurance, policy schedules) on short notice. Most daily work happens at a desk in the main system; staff increasingly also work from a browser or mobile surface, and clients increasingly serve themselves through a portal.

## Core Model

### The Defining Core

**Client records.** The book is organized around named clients — individuals, households, or businesses. A client file gathers contact details, the policies held, the money owed and paid, and the history of every interaction. Prospects typically live in the same space as a lighter record until they become clients.

**Policy records.** The central object. A policy record binds one client to one product from one external insurer, for a defined term: what is covered, the premium, the policy period, and the insurer that carries the risk. A client usually holds several policies (different lines, sometimes different insurers). Collectively the policy records are the firm's book of business — the asset the firm lives on.

Two properties of the policy record deserve emphasis:

- *It references an external insurer.* The record names the insurer that actually carries the risk. The brokerage does not hold the master policy — the insurer does. The broker's record is the record of a **placement**: who placed what, with whom, on what terms, for whose benefit.
- *It recurs by period.* Every policy has a term and an expiry. At expiry the policy either renews (often on changed terms and premium), is replaced with another insurer's policy, or lapses. This makes renewal the structural heartbeat of the whole system.

**Renewal-driven lifecycle.** A policy moves through states that are conceptually shared across products even though exact labels vary: quoted → bound/in force → adjusted mid-term (coverage, premium, insurer) → renewal due → renewed or replaced or lapsed → (sometimes) cancelled. Work, tasks, and money all hang off this cycle.

### Standard Capabilities Around the Core

Mature products commonly add the following. They make the platform practical; they are not what defines the Type.

- **Insurer panel management** — the set of insurers the firm places with, organized by line of business, with the firm's appointments and terms of trade.
- **Quote and submission workflow** — capture the client's risk information once, then send it to one or several insurers (through rating tools, insurer portals, or market connectivity), compare the returned quotes and terms, and bind the chosen one into a policy record.
- **Insurer data feeds (carrier download)** — insurers push policy data, documents, endorsements, renewals, and sometimes claim notifications back into the broker's policy records, so the book stays current without re-keying.
- **Commission tracking and reconciliation** — insurers pay the firm commission per policy. The system records expected commission against each policy, imports or receives the insurers' statements, matches them to policies, flags differences, and calculates each producer's share.
- **Premium and client accounting** — invoicing clients for premiums (and fees), recording payments, handling deposits and refunds, bank reconciliation, and a ledger that supports month-end close. In some markets the firm collects premium itself and holds it in a client (trust) account before remitting to insurers; in others insurers bill clients directly and the firm's accounting is lighter. Some products keep all accounting inside the system; others pair in-system trust/commission workflows with an external accounting package for the firm's operating books.
- **Document machinery** — generation of policy schedules, insurance certificates, proposal documents, and client letters from templates, reusing data already held on the client and policy; every produced or received document stored against the client or policy.
- **Task and workflow management with interaction logging** — to-do items tied to clients and policies (renewal follow-ups, outstanding documents, callbacks), alerts for events such as premium increases, and an automatic log of every client interaction. The logging posture is an E&O (errors-and-omissions) defense: the file must show what was said, sent, and advised.
- **Sales layer** — leads, a pipeline for new business, and cross-sell/upsell views over the existing book (which clients lack which coverage).
- **Reporting and business intelligence** — production by insurer and by producer, retention and lapse rates, commission income, pipeline conversion, financial summaries.
- **Client self-service** — a portal or app where clients view policies and coverage, download ID cards and documents, request certificates, and sometimes start a quote.
- **Claims logging** — claims notified by clients are recorded and linked to the policy; full claims handling remains the insurer's side.
- **Roles and permissions** — producers, account handlers, accounting staff, and administrators see and do different things; client files and money functions are permission-scoped.

### One Structure, Many Implementations

The core model is conceptual. Products realize it differently, and a reader who knows only one implementation should still recognize the others:

```text
Concept:  policy record naming an external insurer
Realizations:  placement with any of many appointed insurers (broker posture);
               book concentrated on a few appointed carriers (agency posture);
               scheme business under delegated authority (broker/MGA posture)

Concept:  quote and submission
Realizations:  comparative rating engines quoting many insurers at once;
               direct entry on individual insurer portals with data autofill;
               market-wide e-trading panels; quote-and-buy journeys for clients

Concept:  commission and premium money
Realizations:  full in-system ledger with client (trust) accounts;
               in-system commission tracking plus external operating accounting;
               insurer-billed models with lighter broker-side accounting

Concept:  insurer connectivity
Realizations:  automated data/document downloads from insurers;
               real-time rating connections;
               statement files matched by reconciliation tooling
```

## How It Works

### Win a client and place the risk

```text
Lead arrives (referral, website form, campaign)
→ recorded as a prospect in the sales pipeline
→ risk information captured once on the client file
→ submission sent to one insurer or quoted across several
→ quotes and terms compared
→ client accepts
→ policy bound: a policy record is created
   (client × insurer product × terms × period)
→ documents issued to the client
→ commission expectation recorded against the policy
```

The "capture once, submit many" pattern is the point of the placement workflow: risk data re-keying into each insurer's portal is the industry's classic inefficiency, and products attack it with rating engines, portal autofill, and market connectivity.

### Service the in-force book

Day-to-day work happens on the client and policy files:

```text
Client calls or emails (change of address, new vehicle, added coverage…)
→ handler opens the client file
→ policy record adjusted (coverage, premium, sometimes insurer)
→ documents regenerated and sent
→ interaction logged automatically on the file
→ certificates of insurance issued to third parties on request
```

Claims notified by clients are logged against the policy and passed to the insurer; the broker tracks status rather than adjudicates.

### Renew the book

Renewal is a recurring, bulk-shaped operation rather than a one-off event:

```text
Policies approaching expiry surface on renewal worklists
→ handler reviews the expiring terms (and any premium changes)
→ re-markets the risk if needed (same insurer or alternative)
→ renewal terms agreed with client
→ policy record rolls into the new period
→ documents issued; commission expectation updated
→ unrenewed policies lapse and drop out of the in-force book
```

Products commonly support this with alerts, renewal reports, and mass actions (renewal letters, proposals, certificate redistribution).

### Settle the money

Money moves in two directions and must balance:

```text
Client side:  invoices issued for premiums/fees
              → payments received (or insurer bills the client directly, by variant)
              → client ledger kept current; deposits reconciled
Insurer side:  commission statements arrive per insurer
              → matched against expected commission per policy
              → differences flagged and resolved
              → producers' commission splits calculated and paid
→ month-end close: ledger, reconciliation, financial reports
```

Where the firm collects premium itself, client money may sit in a segregated trust account with regulatory calculations before remittance to insurers — the depth of this machinery depends on the market.

### Capability tiers

- **Defining core** — client records; policy/placement records naming external insurers; renewal-driven lifecycle.
- **Standard capabilities** — insurer panel, quote/submission workflow, insurer data feeds, commission reconciliation, premium/client accounting, documents, tasks and interaction logging, sales layer, reporting, client self-service, claims logging, roles.
- **Common variants and optional capabilities** — regional client-money regimes, scheme building, aggregator trading, book-roll/M&A machinery, comparative-rating depth, wholesale posture, AI assistance, marketing/website add-ons.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Client file

The primary working surface — one unified view of a client relationship.

- typical information: contact details, all policies with insurer and status, money owed/paid, documents, interaction history, tasks
- primary actions: open a policy, log an interaction, create a task, issue a document, start a quote or renewal

### Policy detail

The placement record for one policy.

- typical information: insurer and product, coverage and limits, premium, term and renewal date, commission expectation, linked documents and claims
- primary actions: adjust coverage, re-market, renew, cancel, generate documents, view download history

### Quote / submission workspace

Where new business and re-marketing happen.

- typical information: risk data entry, insurer responses (premium, terms, forms), comparison view
- primary actions: submit to insurer(s), compare, bind the chosen quote into a policy record

### Renewal worklist

The recurring operations surface for the expiring book.

- typical information: policies by renewal date, premium changes, action state
- primary actions: review, re-quote, send renewal documents, roll forward or let lapse

### Commission and accounting surfaces

- typical information: commission statements per insurer, expected vs received per policy, client invoices and payments, producer splits, ledger balances
- primary actions: import/receive statements, match and reconcile, invoice, record payments, run month-end

### Document library and templates

- typical information: templates (schedules, certificates, letters, proposals) and every produced/received document, stored against client or policy
- primary actions: generate from template, attach, email, e-sign

### Task list and activity log

- typical information: tasks by due date and owner, automatic log of calls/emails/texts per client
- primary actions: create/complete tasks, review history

### Reports and dashboards

- typical information: production by insurer/producer, retention, pipeline, commission income, financial summaries
- primary actions: run standard reports, build custom reports, act on results (e.g. batch email from a report)

### Client portal / app

- typical information: the client's policies, coverage, ID cards, documents
- primary actions: download documents, request certificates, contact the firm, sometimes start a quote

### Administration

- typical information: users and roles, insurer panel setup, document templates, workflow and automation rules, data import/export
- primary actions: manage users and permissions, configure lines of business and templates, migrate data in

## Important Rules / Behaviors

### The broker's policy record is not the master policy

The insurer holds the authoritative policy record. The broker's record is a placement record that must be kept in step with the insurer's reality — which is why insurer data feeds exist. A discrepancy between the two is a real operational problem, not a cosmetic one.

### Renewal is the structural deadline

Policies expire. An unrenewed policy lapses, the client loses coverage, and the firm loses the income. Renewal dates therefore drive worklists, alerts, and reports across the whole system; the book is never static.

### Money is tracked in both directions and must reconcile

The firm owes nothing but is owed commission by insurers and premium by clients (in collect-itself models). Commission statements are matched against per-policy expectations; mismatches are surfaced and resolved. Producer pay derives from recorded splits on placed business. Where client money is held, it is kept segregated from the firm's own funds.

### Every interaction is logged

The client file is expected to show what was advised, sent, and agreed. This is an E&O and compliance posture as much as a service feature: if it is not in the file, it did not happen.

### Placement depends on the insurer panel

The firm can only place with insurers it is appointed with. Panel composition (by line of business) shapes what the firm can sell and how competitive its quotes are; scheme and delegated-authority arrangements extend the panel with the firm's own branded products.

### Roles scope money and clients

Producers, handlers, accounting staff, and administrators have different visibility and powers; client files and accounting functions are permission-scoped. Exact role models vary by product and firm size.

## Variants

- **Regional naming** — the same Type is called an *agency management system* in the US market and *broker* software / *broker management system* in the UK and Commonwealth markets. The researched evidence indicates one Application Type with regional naming rather than two Types.
- **Lines focus** — personal-lines shops (high policy counts, comparative rating, aggregator trading in some markets), commercial-lines brokers (complex risks, submissions, documents), benefits and life/health agencies (different products and commission structures).
- **Agency vs broker posture** — some firms' books concentrate on a few appointed carriers; others place widely across many insurers. The core model fits both; the placement workflow's emphasis differs.
- **Wholesale brokerage** — intermediaries that place specialty risks on behalf of retail brokers rather than end clients; same core objects, different counterparty mix.
- **Scheme-building brokers** (UK-flavored) — firms that build and distribute their own branded products under delegated insurer authority, blurring toward MGA territory.
- **Network and franchise brokers** — member firms of a network sharing panels, schemes, and compliance infrastructure.
- **Deployment shape** — desktop application with cloud-hosted data, pure browser SaaS, or fully hosted/managed service.
- **Suite posture** — standalone management system; suite with rating, websites, licensing, and document-management siblings; or a market-wide platform where brokers, insurers, and MGAs trade on one network.
- **Adviser variant** — financial advisers managing clients' insurance policies alongside financial products; adjacent posture with a different regulatory context.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Insurance Agency Management | same Type under US regional naming | the market uses "agency management system" (US) and "broker management system" (UK) for the same intermediary back-office; this document treats them as one Type with naming variants |
| Insurance Policy Administration System | insurer-side counterpart | manages the insurer's master policy records and premium accounting for its own products; the broker platform manages a placed book referencing many external insurers and earns commission |
| Insurance Quote Platform | adjacent, often bundled | produces quote transactions (comparative rating, quote-and-buy); no persistent book, renewals, or commission ledger — a rater alone cannot run a brokerage |
| Customer Relationship Management / CRM | contains a CRM layer | a CRM centers on relationships and campaigns; the broker platform centers on policy records and their money — a CRM cannot hold the placement, renewal, or commission structures |
| Underwriting Workbench / Insurance Underwriting Platform | insurer-side counterpart | decides risks under delegated authority; the broker platform places risks across insurers without underwriting authority |
| Insurance Claims Management | adjacent module | adjudicates and manages claims for an insurer; broker platforms log claims and link them to policies |
| Brokerage Platform (securities) | name collision only | securities trading and portfolio custody; a different domain despite the shared word "broker" |
| Freight Brokerage Platform | name collision only | logistics intermediary matching shippers and carriers; different domain |
| Financial Advisor Platform | adjacent | advice-centric management of clients' finances, which may include their insurance policies; different regulatory context and center of gravity |

## Representative Products

- **Acturis** — UK SaaS platform serving brokers, insurers, and MGAs; mid-to-large commercial brokers
- **SSP** — long-established UK/global broker, insurer, and MGA solutions; high-street to call-centre brokers
- **HawkSoft** — US agency management system for small independent agencies; all-inclusive subscription
- **Vertafore AMS360** — US agency management system for mid-market and larger agencies; accounting depth
- **EZLynx** — US comparative-rater-first all-in-one system for startup and growth agencies (Applied Systems company)

Applied Epic — the largest US/UK agency and broker system — could not be documented directly in this research pass (vendor site unreachable); the sample rests on the five products above.

## Sources

Research date: **2026-09-06**

- Acturis — product page: https://www.acturis.com/product/ ; root: https://www.acturis.com/
- SSP — broker solutions: https://ssp-worldwide.com/broker ; root: https://ssp-worldwide.com/
- HawkSoft — agency management system: https://hawksoft.com/agency-management-system/ ; accounting: https://hawksoft.com/accounting/ ; feature tour: https://hawksoft.com/agency-management-system/tour/
- Vertafore AMS360 — https://www.vertafore.com/products/ams360
- EZLynx — https://www.ezlynx.com/

> Sourcing limitation: vendor help centers and user guides were not reachable in this research pass; all evidence comes from official product pages. Operational details are therefore described at the level of structure and workflow, not step level — no exact state names, numeric limits, default settings, or reconciliation mechanics are asserted. Applied Systems (Applied Epic) and Open GI were attempted and abandoned after repeated failures.

Detailed evidence, product-by-product observations, the cross-product comparison, and boundary analysis are recorded in the paired Research Notes.
