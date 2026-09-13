# Wastewater Utility Management

## Overview

A **Wastewater Utility Management** application is a wastewater utility's customer-service business system of record.

It holds every connected premise's sewer service as an account, converts each premise's service into charges through a configured basis — most commonly measured water consumption or flat/fixed rates rather than a dedicated wastewater meter — and runs the cycle through which the utility actually operates its customer base: connect service, accumulate the charge basis, bill under configured rates, collect payment, manage deposits, arrears and payment plans, and dispatch the field work that opens, sustains, and closes each service.

One boundary note matters more for this Type than for most: a wastewater utility's software estate is assembled from cooperating systems, and the market phrase "wastewater utility management" is often used loosely across all of them — the collection-system and treatment-works operations systems, the plant data and discharge-compliance systems, and the pretreatment program. This document defines the Type as the utility's **customer-and-money** system: the system of record for the served population and the revenue it generates. The operated estate (sewers, manholes, lift stations, treatment works), the utility's own discharge compliance, and its pretreatment regulatory program are adjacent systems with their own structures (see Related Application Types).

The market realizes this Type through utility customer-information and billing platforms that serve several commodities — products built to bill "water, sewer, refuse, and more" from one connected system, deployed for the sewer service — with the wastewater domain and its charge structures as the vertical anchor.

## Users & Context

Primary users, by relationship to the system:

- **customer service representatives** — front counter and call center; live in the account of record: answer balance and charge questions, start/stop/change service, take payments, set up payment plans, resolve billing questions
- **billing and back-office staff** — run the recurring billing cycle, process meter reads (their own or imported), issue bills, apply adjustments, administer rates, deposits, and payment plans
- **collections staff** — work the past-due population through notices, payment arrangements, and further action
- **field crews** — receive and complete service orders (connections, investigations, meter/read-related work), typically on mobile devices, with results flowing back to the account

Secondary users: **rate and billing administrators** (configure rates and billing cycles), **management** (revenue, arrears, and consumption reporting), and **customers themselves** through the portal layer (common in current products).

Typical operators are municipal sewer/water departments, municipal utility authorities, water and sanitation districts, and regulated utilities. A structural reality shapes the context: water and sewer are commonly billed together on one account by the same product — a water-and-sewer utility runs one customer system for both services, and a sewer-only authority frequently derives its charges from water-consumption data supplied by metering it does not itself operate.

## Core Model

The defining structure is three parts held together — remove any one and the product stops being this kind of system:

```text
Connected premise (sewer service point)
  └── Service account  (customer × premise × service state × financial standing)
        ├── Charge basis  (reads / flat rate / surcharge class)
        │     └── Rates → bill → payments / adjustments / deposits / arrears
        └── Service orders (connect / inspect / investigate — office ↔ field)
```

### Service account

The account is the spine. It binds one customer to one served premise's sewer service, carries the service state (active, inactive, closed) and the account's financial standing, and accumulates the whole relationship: charges, bills, payments, arrears, contacts, notes. Everything else hangs off it. Where a utility serves a premise with several services — water, sewer, stormwater, refuse — the services hang as lines on the same account, which is the dominant deployment shape for this product family.

### Premise and the charge basis

The premise is the physical place whose wastewater the utility conveys and treats; the service relationship is a **connection** to the collection system rather than a commodity delivered through a dedicated meter. How service becomes charges is therefore the Type's distinctive structure. Common bases:

- **measured water consumption** — periodic reads from the metering population (frequently the water side's meters or AMI feed, imported into this system) converted into sewer charges
- **flat/fixed rates** — a configured charge per premise or per unit of service, independent of measured flow
- **minimum-plus-usage and class-based structures** — minimum charges, adjustments, and miscellaneous charges layered on either basis
- **industrial-discharger classes** — permitted industrial users billed under separate structures, in some cases against metered discharge quantities

The meter, where reads are used, commonly belongs to the water service; this system consumes reads rather than operating the metering lifecycle itself. A deployment running entirely on flat rates remains complete.

### Rates and the bill

Configured rates convert the charge basis into charges — tiered and seasonal shapes, flat fees, minimums, and sewer-specific calculations are the standard furniture. The bill is the recurring financial artifact of the cycle: charges computed for the period, issued as a statement on the account, tracked until settled. The account's financial layer is rich because utilities extend credit: deposits held against the account, payments and adjustments posted, arrears tracked, payment plans spreading costs, and final bills generated when service stops.

### Service orders

Service orders are the operational instrument connecting the office to the field. They carry the acts that change or verify the account's service state — connecting a premise, investigating a reported issue, read-related field work — and they are dispatched to field crews and completed with recorded results that flow back into the account record. The service order is where the money state and the physical state meet.

### What the core deliberately does not include

The collection system and treatment works — sewers, manholes, lift stations, plant process equipment — are not objects in this system's world; they enter only as the delivery context of served premises, and the systems that manage them (asset/work management, plant data, SCADA) are adjacent. The utility's own discharge compliance (effluent monitoring, regulatory discharge reports) and its pretreatment regulatory program over industrial users are separate systems with their own record structures. Likewise, large-scale meter-data infrastructure is an adjacent layer: in this system reads exist to produce bills.

## How It Works

### Start service

```text
Customer requests service
→ service account opened for the customer at the premise
→ credit standing checked, deposit set where required
→ service order created and dispatched to the field
→ crew makes the connection / activates the service
→ service state becomes active; billing begins
```

### The charge-basis cycle

```text
Billing period approaches
→ charge basis accumulated per premise:
     reads imported from the metering population (or flat rates applied)
→ exceptions and irregularities flagged for review
→ usage/charge basis validated and attached to the account
```

Reads are not always obtainable or regular; products commonly provide for estimated billing, with the account trued up when an actual read arrives.

### The billing cycle

```text
Billing cycle closes (monthly / quarterly / bi-monthly per schedule)
→ charge basis × configured rates → charges
→ bill issued as a statement on the account (paper, e-bill, portal)
→ payments posted (counter, mail, online, autopay)
→ unpaid balances age into arrears
→ past-due processing: notices → payment arrangements → further action
```

The coupling between money and service state is the signature behavior of the Type: financial standing drives field action through the service-order machinery, and restored standing closes the loop.

### Change events

Move-ins and move-outs reassign the account layer over the same premise (with final bills cut at stop); rate changes reconfigure future bills without touching posted history; adjustments and corrections post as attributable transactions. Every money transaction posts to an audit trail — the account is a ledger, not just a profile.

### Standard capabilities layered on the core

- customer portal (balances, usage, bills, payments) and notifications (email/SMS) as the modern self-service layer
- payment machinery: online payments, processors, autopay, cash receipting
- general-ledger integration so the money cycle lands in the finance core
- AMR/AMI integration for automated reads
- mobile workforce tools for service-order dispatch and completion
- reporting and dashboards over revenue, arrears, and consumption
- integration substrate (APIs) to asset management, GIS, accounting, and metering systems

These make the system practical but are not what makes it this Type: deployments without portals, without AMI, and without mobile tools — including the entire paper era — ran the same core.

## Interfaces

Described conceptually; names and layouts vary by product.

### Account / premise workspace

The primary working surface for customer-facing staff — in current products typically a single-screen account hub. Typical information: account holder, service address, service state, current balance, recent bills and payments, usage and reads per service line, open and past service orders, notifications and notes. Primary actions: start/stop/change service, take payment, set up a payment plan, issue adjustment, create and dispatch a service order, answer charge and billing questions.

### Billing and rate configuration

Back-office surface for the revenue machinery. Typical information: rate structures and their components (tiers, flat fees, minimums, sewer calculations), billing runs and their progress, read/exception queues. Primary actions: configure rates and cycles, run billing, process reads, correct and reissue bills.

### Service order board / dispatch

The office↔field surface. Typical information: open orders by type, priority, assignment, completion status. Primary actions: create, dispatch, reschedule, review completed work flowing back from the field.

### Collections worklist

The arrears surface. Typical information: past-due accounts by age, notice status, payment-arrangement state. Primary actions: generate notices, arrange payment, order further field action.

### Reporting / dashboards

Management surface over the served population: revenue, arrears aging, consumption trends, billing-run outcomes.

### Customer portal (common modern layer)

Customer-facing web/mobile surface: balances and bills, usage history, payment initiation, service requests, paperless enrollment.

## Important Rules / Behaviors

- **Money and service state are coupled.** Arrears drive notices, then payment arrangements, then field action through service orders; payment restores standing and closes the loop. Deposits are held against accounts as credit protection and settled into the account's history.
- **A stopped service ends with a final bill.** Stop-service produces the closing statement, and the account's balance must resolve — the account persists even when service does not.
- **The charge basis may arrive from another system.** Reads are imported from the metering population; exception and irregularity checks run before bills are computed, and estimated periods carry an obligation to true up when an actual read arrives.
- **One account, many services.** Water, sewer, stormwater, and refuse commonly bill as lines on one account; a change to one service's basis must not corrupt the others' charges.
- **The account is an audited ledger.** Payments, adjustments, deposits, and write-offs post as attributable financial transactions; posting history is not silently rewritten.
- **Service orders are recorded work.** Field completion returns to the account record; the office and the field see the same state.
- **Industrial dischargers are a governed class.** Where the utility permits industrial users, their billing structures are distinct from domestic service, and their discharge quantities may be metered or reported under the pretreatment program (an adjacent system).

## Variants

- **Service composition** — the largest variant. Sewer billed alone (sewer-only authority), or alongside water (the dominant co-billing pattern), or with stormwater and refuse on one account. The more services on the account, the more the product behaves as a multi-service utility CIS with sewer as one line.
- **Who operates the billing** — municipal department, municipal authority, water/sanitation district, regulated utility; and, at one pole, the billing operation itself purchased as a turnkey service (vendor-run back office: bill production, payments, collections, call center) over the same software spine.
- **Charge basis** — consumption-derived (imported reads), flat/fixed per premise or unit, minimum-plus-usage, and industrial surcharge classes; most utilities mix several.
- **Relationship to water metering** — the utility operates its own meter population vs importing reads from another utility's metering/AMI.
- **Scale and tier** — small-municipality packages at one end; enterprise customer-information suites serving large water-and-sewer utilities at the other. The core is stable across the range; depth (rates machinery, analytics, integration) scales with it.
- **Deployment** — cloud-hosted vs on-premise; a procurement differentiator, not a structural one.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Water Utility Management | same family, sibling commodity | identical family structure over drinking-water service; water and sewer are commonly billed by the same products on one account — the commodity binding differs |
| Utility Billing Platform / Utility Customer Information System | horizontal family | the same record-layer machinery for any commodity; this leaf is the wastewater (sewer-service) vertical edition anchored on connected-premise sewer service and its charge structures |
| Utility Asset Management | adjacent layer | holds the collection-system estate (sewers, manholes, lift stations) as assets with care and whole-life governance; here the estate enters only as the delivery context of served premises |
| Utility Field Service Management | adjacent layer | owns crew scheduling and workforce machinery in its own right; here field work appears as service orders bound to service accounts |
| Wastewater Compliance Management | the utility's other hat | the permitted discharger's own compliance system (discharge points, monitoring data, limit evaluation, regulator-facing reports); no service accounts or billing — the utility wears this hat at its treatment works, not at its customer accounts |
| Pretreatment / control-authority program | the utility's regulator hat | a utility-run regulatory program over external parties (industrial-user permits, inspections, sampling, violations, enforcement) — structurally a government-inspection-shaped system, not a service business system; the connection point is the industrial-user billing class |
| SCADA / plant data management systems | adjacent layer | treatment-works process and lab data consolidated for operations and compliance reporting; no customer or money records |
| Water Network Monitoring | adjacent layer | observation loop over the water distribution network; monitoring, not the customer-and-money record |
| Public Works Management | broader sibling | the municipality's whole civil-asset estate (streets, signs, facilities, sewer); sewer appears as one asset class among many, without the service-account economy |

## Representative Products

- **Muni-Link** — cloud utility billing/CIS for water, sewer, and stormwater utilities (North American municipal tier)
- **OpenGov — Utility Billing** — water/sewer/trash billing inside a local-government platform (municipal tier; the same vendor ships wastewater collection asset management as a separate product)
- **Black Mountain Software — Utility Billing** — utility billing/CIS for municipalities and special districts (small-municipal tier)
- **Minol USA — Municipal Sewer Billing** — turnkey sewer billing program (software plus vendor-operated back office)
- **Itineris — UMAX** — enterprise CIS/CRM deployed by a large retail water-and-sewer utility (enterprise tier)

The adjacent poles referenced in this document — collection-system asset/field management (e.g., GIS-connected sewer work management, CCTV inspection specialists), plant data and discharge-compliance systems (e.g., water-information management platforms), and pretreatment program management — were researched to establish the boundary and are recorded in the paired Research Notes.

## Sources

Research date: **2026-09-10**

- Muni-Link — product, CIS, billing, water, and utility-billing pages: https://muni-link.com/ , https://muni-link.com/features/customer-information-system/ , https://muni-link.com/features/billing/ , https://muni-link.com/water , http://muni-link.com/products/utility-billing-software
- OpenGov — Utility Billing and Wastewater Collection product pages: https://opengov.com/products/utility-billing , https://opengov.com/products/asset-management/wastewater-collection
- Black Mountain Software — Utility Billing: https://blackmountainsoftware.com/utility-billing
- Minol USA — Municipal Sewer Billing Services: https://minolusa.com/municipal-sewer-billing-services
- Itineris UMAX at Boston Water and Sewer Commission (trade press): https://www.wwdmag.com/utility-management/article/11004078/updating-oldest-us-water-sewer-system-with-newest-software
- Boundary research: iWorQ Sewer Management (https://iworq.com/systems/sewer-management-software); Hach WIMS (https://www.hach.com/digital-solutions/wims and related official pages; City of San Diego sole-source certification); Linko Pretreatment & FOG Management (https://aquaticinformatics.com/products/fog-pretreatment-regulatory-software and trade-press case studies); City of Palo Alto staff report on wastewater collection system management software; City of Fargo Industrial User Permit application.

> Sourcing limitations: the collection-operations vendor Sedaru could not be reached from the research environment (repeated transport failures), so that pole rests on procurement and press documents rather than official product documentation. One billing vendor's pages were reachable only via search snapshots (direct fetch refused). Precise numeric details (fee amounts, rate tables, cycle counts, account volumes) are intentionally not asserted in this document; claims are calibrated to what the reachable official sources state. Detailed evidence, product-by-product observations, and the full unreachable-source list are recorded in the paired Research Notes.
