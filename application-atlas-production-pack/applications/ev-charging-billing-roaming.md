# EV Charging Billing & Roaming

## Overview

An **EV Charging Billing & Roaming** system is the commercial system of record for EV charging sessions: it turns each charging session into priced revenue by applying charging tariffs to what was delivered, billing the right party, and settling the money between the charging market's distinct commercial parties.

The defining structure is small:

```text
Charging Session of Record (CDR)
└── Tariff-driven Session Pricing
    └── Multi-party Settlement
        (driver ↔ charging-service provider ↔ charge point operator
         ↔ site host / roaming partner or hub)
```

Every public charging transaction lives in a market where the party that operates the charge point, the party the driver pays, and the party that owns the site are frequently different companies. The system exists to make that structure work commercially: sessions are recorded and priced individually, invoices are produced for drivers and between businesses, and value flows across provider/operator/host boundaries — with **roaming** as the inter-operator case: a driver whose contract is with one charging-service provider charges on another company's network, and the same session record is cleared between the parties under their agreement.

When the center of gravity shifts to operating the chargers themselves (monitoring, remote configuration, smart charging, maintenance), the product is drifting toward a different Application Type (EV Charging Network Management). When it shifts to card payment handling alone, it is payment processing territory.

## Users & Context

The operators of this system are charging-market businesses, not drivers:

- **Charge point operators (CPOs)** — companies operating charging stations. Their billing, finance, and commercial teams configure tariffs and plans, watch session revenue, invoice business customers, and settle monthly with site hosts, roaming partners, and hubs.
- **Charging-service providers / e-mobility service providers (eMSPs)** — companies selling charging to drivers under their own brand (app, charge card, subscription). Their teams manage driver contracts and entitlements, invoice subscribers, and pay the operators whose points their drivers use.
- **Roaming hub / clearing operators** — intermediaries running the inter-network layer; their staff monitor partner traffic, validate charging data records against agreements, and track inter-party invoices to payment.
- **Secondary actors** — site hosts (owners of the parking/retail/fuel locations receiving revenue shares), fleet and company-car program managers (billed for their drivers' charging, reimbursing home charging), and corporate customers with employee charging entitlements.

Drivers experience the system only at its edges: they authenticate at the charge point (app, charge card, contactless payment, or vehicle-based Plug&Charge) and receive invoices or receipts. The operators of the system work in admin consoles and B2B portals, typically as a continuous monthly operations rhythm (pricing changes, invoice runs, settlement cycles, dispute handling) rather than one-off projects.

## Core Model

### The Defining Core

```text
Charging Session → Charging Data Record (CDR)
      priced by
Tariff → Price components → Amount
      attributed across
Parties: Driver · Charging-service Provider · Charge Point Operator · Site Host · Roaming Partner/Hub
      settled through
Invoices · Clearing · Settlement/Payouts
```

Three structures. If any one is removed, the product is no longer recognizable as this Type:

- **The charging session of record.** Every charging event is captured as an individually identified record bound to a specific charge point, an authorization identity (who charged), and the metered delivery (energy, start/end times). In the industry this completed record is called a **Charge Detail Record (CDR)**. It is the unit everything else hangs on: without it there is only charger telemetry or a tariff catalog with nothing to price.
- **Tariff-driven session pricing.** A maintained tariff model is applied to the session's recorded delivery to compute the amount owed. Charging tariffs are component-based — typically per-energy (per kWh), per-time, per-session/start fees, and occupancy or parking fees, with time-of-day variation and per-customer-type pricing (employees, guests, subscribers, walk-ups). Pricing is decoupled from the session itself: the same session can be priced differently for different drivers under different contracts. Without this leg, a session is a log entry with no commercial value.
- **Multi-party settlement.** The session's value is attributed across the market's distinct commercial roles and moved between them: the driver's provider bills the driver (or the driver's employer/fleet); the provider and the point operator exchange B2B invoices for roaming sessions; the operator settles with site hosts on agreed revenue shares; hubs and clearing services intermediate and track these flows to payment. Without this leg the product collapses into either point-of-sale payment at a charger (a merchant transaction with no provider/operator structure) or a closed single-network loop with nothing to settle.

### The Party Structure

The party model is what distinguishes this Type from generic billing:

- **Driver** — the identified person charging; reachable through an authorization credential.
- **Charging-service provider (eMSP)** — holds the commercial contract with the driver; owns the tariff the driver pays; invoices the driver.
- **Charge point operator (CPO)** — operates the physical charge point; defines access conditions for its network; earns the session revenue; pays site hosts.
- **Site host** — owns the location where chargers stand; receives a contract-based share.
- **Roaming partner / hub** — the inter-network layer through which providers and operators reach each other without bilateral integrations.

Any of the first three roles can merge into one company (an operator billing its own drivers). Roaming is the case where provider and operator differ — and the system's job is unchanged: record the session, price it under the governing agreement, and settle between the parties.

### Capabilities Common in Mature Products

These are widespread in current products but do not define the Type:

- **Authorization and entitlements** — before energy flows, the driver's credential (charge card, app, payment card, vehicle certificate) is checked against contracts and roaming agreements; entitlements decide who pays for a session (private driver, employer-funded, OEM promotion).
- **Plans, subscriptions, and promotions** — pre-pay and monthly post-pay billing, subscription plans with discounted rates, coupons, promotional periods, and one-time-payment rates for unregistered walk-ups.
- **Payment processing integration** — connections to payment gateways, checks on payment ability before or during charging (some products repeatedly authorize as costs accumulate), fraud controls, and — in some products — payment terminals at chargers for ad-hoc users.
- **White-labeled invoicing** — invoices issued in the customer's own branding, with per-session cost breakdowns, for both consumers and businesses.
- **Settlement and reconciliation machinery** — settlement reports per host/partner, validation of hub settlement reports against the platform's own session records, per-invoice payment-status tracking, reminders and collections, and dispute resolution against the retained CDR history.
- **Cross-border machinery** — sessions billed in the charge point's local currency and tax rules while the driver is invoiced at home; multi-currency, VAT automation, exchange rates.
- **Roaming network participation** — membership in one or more roaming networks/hubs, exchange of charge point data and tariffs with partners, and marketplaces of pre-built roaming agreements.
- **Fleet and home-charging scenarios** — public sessions billed directly to the fleet operator, home charging reimbursed to employees with tax-compliant documentation.
- **Billing and revenue analytics** — revenue by location, plan, or partner; VAT and transaction reports; dashboards.

### One Structure, Many Implementations

The core is conceptual; products realize it differently:

```text
Concept:  Session of record (CDR)
Realizations:  CDR registered on the operator's platform (billing-engine pole)
               CDR exchanged across a roaming network (hub pole)
               CDR verified and invoiced by a clearing service (clearing pole)

Concept:  Tariff-driven pricing
Realizations:  operator-configured tariff engine (plans, rate components, margins)
               provider tariffs exchanged via the roaming network
               per-CDR price computation cross-checked against the roaming agreement

Concept:  Multi-party settlement
Realizations:  monthly host/partner settlement reports
               hub-run automated billing between providers and operators
               clearing: B2B invoice per CDR + payment tracking + dispute support
               full-stack billing-as-a-service including collections and payouts
```

## How It Works

### Before charging: build the commercial structure

```text
Onboard parties (operators, providers, hosts, roaming partners)
→ negotiate agreements (roaming terms, host revenue shares, corporate contracts)
→ configure tariffs, plans, and margins per user type / location / contract
→ issue driver credentials (charge cards, app accounts) and register them
→ exchange charge point and tariff data with roaming partners
```

### The session loop: from plug-in to money

```text
Driver authenticates at a charge point (card / app / contactless / Plug&Charge)
→ entitlement and payment-ability checked (contract valid, roaming agreement in place, pre-authorization)
→ energy delivered, metered, and recorded as a session with start/stop and identity
→ session completes as a Charge Detail Record (CDR)
→ tariff applied to the CDR → priced amount(s), with validation/quality checks
→ money attributed: driver invoiced by their provider (immediately or monthly);
  provider invoiced by operator if roaming; operator pays host share
→ invoices tracked to payment; reminders, collections, disputes where needed
→ periodic settlement across parties (monthly cycle typical), payouts executed
```

Two flavors of this loop exist, and mature products support both:

- **Operator-side loop**: the CPO records sessions on its own points, prices them under its own tariffs, bills direct drivers and roaming partners, and settles outward (hosts, hubs).
- **Provider-side loop**: the eMSP's drivers charge on foreign points; the provider receives those sessions via roaming, prices them under its own customer tariffs, invoices drivers, and pays the operators via the hub or clearing service.

### The roaming clearing cycle

For sessions between parties, the back office runs a repeating cycle:

```text
CDRs exchanged or received across the network
→ quality checks (completeness, plausibility)
→ price recomputed and cross-checked against the roaming agreement
→ B2B invoices generated per party / per CDR batch
→ payment tracked (fully / partially / not paid), reminders sent
→ discrepancies raised as disputes, resolved against the retained session history
```

The dispute path is structurally important: the platform holds the authoritative session history, so contested amounts are recomputed and compared against the agreement rather than negotiated blindly.

### Defining vs common vs optional

**Defining core** — session/CDR of record; tariff-driven pricing; multi-party settlement (billing, clearing, payouts).

**Common mature structure** — authorization/entitlements; plans and promotions; payment gateway integration; white-labeled invoicing; settlement reporting and reconciliation; cross-border tax/currency handling; roaming network participation; fleet and home-charging scenarios; analytics.

**Optional / variant** — payment terminals and card-present walk-up charging; credit-risk and collections as an outsourced service; Plug&Charge credential services; EVSE data quality and process monitoring; testing/certification; energy services (smart charging, V2G) riding the same session records; CO₂-certificate monetization.

## Interfaces

Described conceptually; exact layouts and names vary by product.

### Operator billing console

The CPO/eMSP staff workspace.

- tariff and plan configuration (rate components, user types, time windows, margins, promotions)
- invoice management — find invoices by customer, status, date; per-session cost breakdowns
- transaction/session views with pricing detail
- primary actions: configure tariffs, run billing, issue invoices, adjust/credit, export reports

### Settlement / partner workspace

The back-office surface for the multi-party money flows.

- settlement reports per host, partner, or hub; hub-report validation against own session records
- payment-status tracking and reminder handling
- dispute views with the underlying CDR evidence
- primary actions: validate, reconcile, mark paid, raise/resolve disputes, export settlement files

### Roaming partner portal

The hub/network-facing surface.

- connected partners and coverage, agreement status, exchanged charge point and tariff data
- session/CDR traffic views, monitoring of authorization and settlement flows
- primary actions: activate roaming partners, publish tariff/point data, inspect traffic

### Driver-facing surfaces (edge of the system)

- app or web portal: charging history, receipts/invoices with cost breakdown, payment methods
- charge card management
- primary actions: pay, download invoice, manage credentials

### Reports and analytics

- billing, payments, VAT/tax, and revenue reports; dashboards by site, plan, partner, geography

### APIs

- machine interfaces for session/CDR exchange, tariff and point-data publication, and billing data integration with ERP/accounting — the plumbing that makes roaming and settlement possible between systems.

## Important Rules / Behaviors

### Authorization gates the session

No entitlement, no energy: the driver's credential must map to a valid contract or a reachable roaming agreement (or an ad-hoc payment) before charging starts. Entitlements also decide *who pays* — a session can be charged to a private driver, an employer (employee entitlement), or a promotional sponsor instead of the person plugging in.

### The CDR is the arbiter

Priced sessions are computed from the recorded CDR, and disagreements are settled by recomputing from that record and the governing agreement — not by renegotiation. Products emphasize quality checks on CDRs precisely because every downstream invoice depends on them.

### Pricing follows the point's location; invoicing follows the driver

A cross-border pattern in the researched products: a session is priced according to the currency and tax rules of the charger's physical location, while the driver's invoice is produced in the driver's home context. Multi-currency and tax handling is therefore structural, not cosmetic.

### Settlement is cyclical

Money moves in periodic settlement runs (monthly is the common rhythm described across products) rather than per-session, for the B2B legs: hosts, roaming partners, and providers are settled in batches; drivers may be billed per session (immediate payment) or monthly (post-payment).

### Non-payment is a managed process

Failed driver payments trigger payment checks before charging and reminders/collections after; some products go further and internalize the credit risk themselves, paying the operator for every valid session and pursuing the debtor on their own account. Fraud controls (abnormal usage patterns, credential misuse) protect session revenue.

### Commercial terms live in agreements, not in code

Roaming terms, host revenue shares, corporate margins, and promotional conditions are recorded as agreement data that pricing and settlement consult — which is why the system can price the same session differently for different parties.

## Variants

- **Billing engine for operators** — deep tariff/plan configurability as the product's heart; roaming handled as reconciliation against external hubs. (Enterprise CPO/eMSP tier.)
- **Roaming hub / network** — the inter-party layer itself: single integration into a network of partners, authorization and settlement between CPOs and eMSPs automated network-wide; no driver billing at all.
- **Clearing house** — CDR verification, price computation against agreements, B2B invoice generation, payment tracking, and dispute support as a service between operators and providers.
- **Full-stack billing-as-a-service** — white-label commercial backend combining invoicing, collections and credit risk, tax-compliant payouts, and roaming access for CPOs and MSPs, often alongside station management.
- **Suite module** — billing and roaming shipped as one module of a wider charging management platform (alongside charger operations, energy management, driver apps).
- **Segment flavors** — fleet/depot-oriented deployments (billed to the fleet, home reimbursement), fuel-retail/automaker programs (promotional free-charging billed to the sponsor), and public-infrastructure concessions (operator + host revenue shares).

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| EV Charging Network Management | sibling / complement | operates the chargers (monitoring, connectivity, smart charging, maintenance); this Type operates the money. Products bundle both; the leaves split the two layers |
| Utility Billing Platform | adjacent | recurring billing per utility customer account from meter reads; here the unit is the per-session CDR and the counterparties are multiple independent companies |
| Payment Processing Platform / Payment Gateway | component | card payment handling (pre-auth, gateways, terminals) is one input machinery; this Type's defining structure is the session→pricing→settlement loop across parties |
| Subscription Billing Platform | component | subscriptions/plans are one billing input; the session CDR remains the unit of record |
| Telecom Charging Platform / Telecom BSS | structural analogy | roaming, clearing, and settlement between operators mirror telecom interconnect — but around charging sessions and kWh, with different objects and protocols |
| Mobility-as-a-Service Platform | adjacent | consumer-facing multi-modal trip aggregation and payment; this Type is B2B revenue infrastructure operated by charging-market parties |
| Fleet Management System | adjacent customer | fleets are a served segment (depot/home/public charging billed to the operator); fleet management's core is vehicles/drivers/routes, not charging settlement |

The most important boundary is with **EV Charging Network Management**: the market sells them together as "charging management platforms," and several sampled products ship both halves as separate named modules. The split test is consistent — remove tariffing, invoicing, and settlement and what remains is charger operations; remove charger operations entirely (as pure hubs and clearing houses do) and the commercial Type stands on its own.

## Representative Products

- **Driivz** — EV charging & energy management platform for operators; flagship configurable billing engine with host/partner settlement and hub-report reconciliation
- **Hubject** — international eRoaming network (intercharge); authorization and settlement automated between connected CPOs and eMSPs, plus a financial-services line
- **Gireve** — European B2B platform combining roaming intermediation with clearing services (CDR checks → pricing → B2B invoicing → payment tracking → dispute support)
- **Last Mile Solutions** — full-stack white-label backend for CPOs and MSPs; billing-as-a-service, payments, collections/payouts, and roaming-as-a-service

The defining core was checked across this spectrum — billing-engine, hub, clearing-house, and full-stack poles — so that no single packaging (operator billing vs inter-party clearing) defines the Type.

## Sources

Research date: **2026-09-08**

Primary vendor surfaces (official pages and FAQs, fetched live):

- Driivz — EV Charging Billing (product page + FAQ): https://driivz.com/platform/ev-billing/
- Driivz — "The Billing Challenges Behind a Seamless EV Charging Experience" (official blog): https://driivz.com/solutions/ev-charging-billing/
- Hubject — homepage: https://www.hubject.com/ ; intercharge overview: https://www.hubject.com/intercharge-overview
- Gireve — homepage: https://gireve.com/ ; EV Roaming Services: https://www.gireve.com/ev-roaming-services/ ; Clearing Services: https://www.gireve.com/clearing-services/
- Last Mile Solutions — homepage: https://lastmilesolutions.com/ ; Billing as a Service: https://www.lastmilesolutions.com/billing-as-a-service/

> Sourcing limitation: vendor help centers / user guides and the industry roaming protocol specification (OCPI) were not reachable from the research environment on this date. Assertions are therefore calibrated to page- and FAQ-level evidence: no precise numeric limits, defaults, settlement-day counts, or fee rates are stated, and single-vendor packaging details are kept out of the core description. One additional candidate product (a white-label eMSP/CPO platform) was excluded after repeated fetch failures.

Detailed product-by-product observations, the cross-product comparison matrix, and the historical/market-sample breadth check are recorded in the paired Research Notes.
