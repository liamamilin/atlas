# Water Utility Management

## Overview

A **Water Utility Management** application is a water utility's customer-service business system of record.

It holds every served premise's water service as an account, binds the utility's own meters and measured consumption to those accounts, and runs the cycle through which the utility actually operates its customer base: start service, meter it, bill it under configured rates, collect payment, manage deposits, arrears, budget plans and collections, and dispatch the field work — turn-ons, shutoffs, meter sets and exchanges, leak investigations — that physically opens, sustains, and closes each service.

One boundary note matters more for this Type than for most: a water utility's software estate is assembled from cooperating systems, and the market phrase "water utility management" is often used loosely across all of them — the network-operations and monitoring systems, the water-quality program, and the asset/field systems over mains, hydrants, and tanks. This document defines the Type as the utility's **customer-and-money** system: the system of record for the served population and the revenue it generates. The operated estate, the quality program, and the network watch are adjacent systems with their own structures (see Related Application Types).

The market realizes this Type through utility customer-information and billing platforms that serve several commodities — products built to bill "water, sewer, electric, refuse, and more" from one connected system, deployed for the water service — with the drinking-water domain and its metering and rate structures as the vertical anchor.

## Users & Context

Primary users, by relationship to the system:

- **customer service representatives** — front counter and call center; live in the account of record: answer balance and usage questions, start/stop/change service, take payments, set up payment plans, resolve billing and high-bill questions
- **billing and back-office staff** — run the recurring billing cycle, process meter reads (their own or imported), issue bills, apply adjustments, administer rates, deposits, and budget plans
- **collections staff** — work the past-due population through notices, payment arrangements, and shutoff-for-nonpayment decisions
- **field crews** — receive and complete service orders (turn-ons, shutoffs, meter sets and exchanges, re-reads, investigations), typically on mobile devices, with results flowing back to the account

Secondary users: **rate and billing administrators** (configure rates and billing cycles), **management** (revenue, arrears, and consumption reporting), and **customers themselves** through the portal layer (common in current products, extending to daily usage visibility and proactive alerts where metering feeds allow).

Typical operators are municipal water departments, water districts and authorities, rural water cooperatives, investor-owned water companies, and large metropolitan utilities; the same product family also serves European drinking-water utilities. A structural reality shapes the context: water is commonly the **host account** for co-billed services — water, sewer, stormwater, and refuse ride as lines on one account, and the water meter's reads are the consumption basis from which derived charges (most commonly sewer) are computed. A water-only utility runs the same core with a single service line.

## Core Model

The defining structure is three parts held together — remove any one and the product stops being this kind of system:

```text
Served premise (water service point)
  └── Service account  (customer × premise × service state × financial standing)
        ├── Meter → reads → measured consumption
        │     └── Rates → bill → payments / adjustments / deposits / arrears
        │     └── (same reads commonly drive co-billed sewer / stormwater lines)
        └── Service orders (turn-on / shutoff / meter work — office ↔ field)
```

### Service account

The account is the spine. It binds one customer to one served premise's water service, carries the service state (active, inactive, closed) and the account's financial standing, and accumulates the whole relationship: consumption history, bills, payments, arrears, contacts, notes. Everything else hangs off it. Where a utility serves a premise with several services, the services hang as lines on the same account — the dominant deployment shape for this product family, with water as the line whose meter feeds the others.

### Premise and meter

The premise is the physical place where water is delivered and measured; the meter is the identified device at that place, owned and operated by the utility itself — water metering is the reference case of the whole utility family, and it is the utility's own metering population that this system holds. Meters have their own lifecycle in the system — installed at a premise, read periodically, exchanged, tested — and every reading attaches to a meter at a premise. Consumption accumulates on the account through this chain: periodic reads (manual route reads; estimates when a read cannot be obtained; remote feeds in metering-modern utilities), validated into usage per billing period.

Measured consumption is what makes the billing *utility* billing. Non-metered fee components (flat charges, fees, taxes) ride on the same account as a standard companion. These same reads commonly serve double duty: sewer and stormwater charges on the same account are frequently computed from the water meter's consumption, which is why the water metering population is load-bearing beyond the water line itself.

### Rates and the bill

Configured rates convert measured consumption into charges — tiered usage steps (increasing-block structures oriented to conservation are common in water practice), seasonal variations, and residential/commercial class distinctions are the standard shapes, alongside flat fees, minimums, and miscellaneous charges. The bill is the recurring financial artifact of the cycle: charges computed from the period's usage and standing charges, issued as a statement on the account, tracked until settled. The account's financial layer is rich because utilities extend credit: deposits held against the account, payments and adjustments posted, arrears tracked, budget (equal-payment) plans spreading costs across the year, and final bills generated when service stops.

### Service orders

Service orders are the operational instrument connecting the office to the field. They carry the physical acts that change the account's service state — turning service on at a premise, shutting it off, setting or exchanging or testing a meter, investigating a reported high usage or leak, re-reading — and they are dispatched to field crews and completed with recorded results (readings, notes, photos, signatures) that flow back into the account record. The service order is where the money state and the physical state meet.

### What the core deliberately does not include

The water estate itself — source works, treatment plants, distribution mains, hydrants, storage tanks — is not an object in this system's world; it enters only as the delivery context of served premises, and the systems that manage it (asset/work management, network monitoring, SCADA) are adjacent. The water-quality program (sampling locations, standards, compliance reports) is a separate system of record. Likewise, large-scale meter-data infrastructure is an adjacent layer: in this system the meter exists to produce bills, and a deployment running on manual reads is complete without any meter-data platform.

## How It Works

### Start service

```text
Customer requests service
→ service account opened for the customer at the premise
→ credit standing checked, deposit set where required
→ service order created and dispatched to the field
→ crew turns on service (and the meter, if not present, is set)
→ service state becomes active; billing begins
```

### The metering cycle

```text
Meter routes scheduled
→ reads collected (manual, estimated, or fed from remote metering)
→ usage validated and attached to the account per billing period
→ derived charges on co-billed lines computed from the same reads
```

Reads are not always obtainable: products commonly provide for estimated billing, with the account trued up when an actual read arrives.

### The billing cycle

```text
Billing period closes (monthly / quarterly / bi-monthly per schedule)
→ consumption × configured rates → charges (per service line on the account)
→ bill issued as a statement on the account (paper, e-bill, portal)
→ payments posted (counter, mail, online, autopay)
→ unpaid balances age into arrears
→ past-due processing: notices → payment arrangements → shutoff decision
→ shutoff itself is a service order; restoration likewise
```

The coupling between money and service state is the signature behavior of the Type: financial standing drives field action through the service-order machinery, and restored standing closes the loop. Mature products automate the loop itself — generating shutoff orders in bulk for the delinquent population, cancelling them automatically when payment arrives, and creating restoration orders when accounts are made current.

### Change events

Move-ins and move-outs reassign the account layer over the same premise (with final bills cut at stop); meter exchanges close one meter's reading history and open the next with prorated billing; rate changes reconfigure future bills without touching posted history. Every money transaction posts to an audit trail — the account is a ledger, not just a profile.

### Standard capabilities layered on the core

- customer portal (balances, usage, bills, payments) and notifications (email/SMS) as the modern self-service layer
- usage visibility and proactive alerts to customers — high-usage and possible-leak alerts where AMI feeds exist, and conservation-oriented engagement (daily usage views, comparisons, guidance) as a growing capability layer, sometimes delivered by a companion engagement product
- payment machinery: online payments, processors, autopay, cash receipting
- general-ledger integration so the money cycle lands in the finance core
- AMR/AMI integration for automated reads
- mobile workforce tools for service-order dispatch and completion
- reporting and dashboards over consumption, revenue, and arrears
- integration substrate (APIs) to asset management, GIS, accounting, and metering systems

These make the system practical but are not what makes it this Type: deployments without portals, without AMI, and without mobile tools — including the entire paper era — ran the same core.

## Interfaces

Described conceptually; names and layouts vary by product.

### Account / premise workspace

The primary working surface for customer-facing staff — in current products typically a single-screen account hub. Typical information: account holder, service address, service state, current balance, recent bills and payments, usage and reads per service line, open and past service orders, notifications and notes. Primary actions: start/stop/change service, take payment, set up a payment plan, issue adjustment, create and dispatch a service order, answer usage and billing questions.

### Billing and rate configuration

Back-office surface for the revenue machinery. Typical information: rate structures and their components (tiers, seasonal shapes, minimums, class distinctions), billing runs and their progress, read/exception queues. Primary actions: configure rates and cycles, run billing, process reads, correct and reissue bills.

### Service order board / dispatch

The office↔field surface. Typical information: open orders by type (turn-on, shutoff, meter set/exchange, investigation, re-read), priority, assignment, completion status. Primary actions: create, dispatch, reschedule, review completed work flowing back from the field.

### Collections worklist

The arrears surface. Typical information: past-due accounts by age, notice status, payment-arrangement state. Primary actions: generate notices, arrange payment, order shutoff or restoration.

### Reporting / dashboards

Management surface over the served population: revenue, arrears aging, consumption trends, billing-run outcomes.

### Customer portal (common modern layer)

Customer-facing web/mobile surface: balances and bills, usage history, payment initiation, service requests; in metering-modern deployments, daily usage views and alert subscriptions.

## Important Rules / Behaviors

- **Money and service state are coupled.** Arrears drive notices, then payment arrangements, then shutoff service orders; payment drives restoration. Deposits are held against accounts as credit protection and settled into the account's history.
- **A stopped service ends with a final bill.** Stop-service cuts the meter's last read, produces the closing statement, and the account's balance must resolve — the account persists even when service does not.
- **Meter changes do not break the bill.** An exchange reads out the old meter and reads in the new one; the billing period is prorated across the two devices.
- **Estimates carry an obligation to true up.** Estimated usage is provisional; the next actual read reconciles the account.
- **One account, many services — one read, many charges.** Water, sewer, stormwater, and refuse commonly bill as lines on one account, and derived lines are computed from the water meter's reads; a change to the water basis must flow correctly to the derived charges without corrupting the others.
- **Budget plans spread, not discount.** Equal-payment arrangements average cost across periods while consumption continues to be measured and trued.
- **The account is an audited ledger.** Payments, adjustments, deposits, and write-offs post as attributable financial transactions; posting history is not silently rewritten.
- **Service orders are recorded work.** Field completion (readings, notes, photos, signatures) returns to the account record; the office and the field see the same state.

## Variants

- **Service composition** — the largest variant. Water billed alone (water-only systems), or as the host account for sewer, stormwater, and refuse (the dominant co-billing pattern, where the water reads drive the derived charges). The more services on the account, the more the product behaves as a multi-service utility CIS with water as the anchor line.
- **Operator type and geography** — municipal departments, water districts and authorities, rural water cooperatives, investor-owned water companies, large metropolitan utilities, and European drinking-water undertakers; the core is stable across all of them, with regional rate and regulatory furniture varying on top.
- **Rate furniture** — tiered/conservation-oriented blocks, seasonal rates, residential/commercial classes, minimums, and miscellaneous charges; most utilities mix several. Some products carry additional water-specific billing classes (seasonal averaging, allocation-style arrangements).
- **Customer engagement depth** — portal-only at one end; engagement platforms with daily usage visibility, proactive high-usage/leak alerts, and conservation guidance at the other, sometimes as a companion product riding on the account.
- **Water-side companion programs** — some products add adjacent programs such as backflow/cross-connection inspection management as modules.
- **Scale tier** — rural and small-municipality packages at one end; enterprise platforms serving the largest metropolitan utilities at the other. The core is stable across the range; depth (rate machinery, analytics, integration) scales with it.
- **Deployment** — cloud-hosted vs on-premise; a procurement differentiator, not a structural one.
- **Metering era** — monthly-manual-read deployments vs interval-metered deployments, where interval data feeds billing and usage analytics; the latter is a growing configuration, not a requirement.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Wastewater Utility Management | same family, sibling commodity | identical family structure over sewer service; water and sewer are commonly billed by the same products on one account, with sewer charges derived from the water reads — the commodity binding differs (metered drinking-water supply vs connected-premise sewer service) |
| Gas Utility Management | same family, sibling commodity | identical family structure over piped-gas service; the commodity's measurement and market structures are the domain binding |
| Utility Billing Platform / Utility Customer Information System | horizontal family | the same record-layer machinery for any commodity; this leaf is the water vertical edition anchored on drinking-water service and its metering/conservation context |
| Water Quality Management | the utility's other hat | the quality program of record (monitoring locations, standards, compliance data, regulator-facing reports); no object overlap with the customer-and-money system |
| Water Network Monitoring | adjacent layer | the operations watch over the distribution network (pressures, flows, leak/burst events driven to field response); here a customer-side leak surfaces as a high-usage alert or bill dispute, not a network event |
| Utility Asset Management | adjacent layer | holds the water estate (mains, hydrants, valves, tanks) as assets with care and whole-life governance; here the estate enters only as the delivery context of served premises |
| Utility Field Service Management | adjacent layer | owns crew scheduling and workforce machinery in its own right; here field work appears as service orders bound to service accounts |
| Meter Data Management / AMI | adjacent infrastructure | meter-data collection and validation infrastructure; here the meter is grounded at accounts/premises to produce bills, and the deployment is complete without it |
| Utility Rate Management | adjacent layer | rate design, modeling, and analysis; here rates are *executed* inside the bill cycle |
| Utility Revenue Assurance | adjacent discipline | audits the meter-to-cash chain for leakage; here the revenue cycle is *run* |
| Customer engagement platforms (water) | customer seat | usage visibility, alerts, and conservation guidance for the customer; no transactions of record — a capability layer or companion product riding on the account |
| Public Works Management | broader sibling | the municipality's whole civil-asset estate (streets, signs, facilities, water lines); water appears as one asset class among many, without the service-account economy |

The closest boundary is with Wastewater Utility Management, because the two Types are co-realized by one product population: the same CIS/billing products bill water and sewer on one account, and the water meter's reads are the sewer charge's basis. The structural test: the account's water line — its own metering population and its drinking-water service — is this Type's binding; the sewer line's connection-based service and derived charge basis belong to the sibling.

## Representative Products

- **Muni-Link** — cloud utility billing/CIS for water, sewer, and stormwater utilities, from rural water systems to municipal authorities (North American municipal/rural tier)
- **Itineris — UMAX** — enterprise CIS/CRM/ERP suite with a dedicated water-utilities sector practice, deployed by metropolitan water utilities and European drinking-water companies (enterprise tier)
- **VertexOne (VXcis / VXconnect)** — water CIS and customer-engagement platform family (conservation, alerts, self-service) serving water utilities and districts (municipal tier; the heritage WaterSmart engagement line is now part of this family)
- **Oracle Utilities — Customer Care and Billing** — enterprise customer care and billing serving electricity, natural gas, and water utilities worldwide
- **Advanced Utility Systems — CIS Infinity** — mid-market customer information and utility billing platform for electric, water, gas, and multi-service providers
- **Springbrook — Cirrus Utility Billing** — small-municipality government utility billing (water, sewer, electric, refuse)

The core model was checked against the paper-era water billing office, 1990s desktop billing packages, rural cooperative systems, and European drinking-water undertakers to avoid over-fitting to the modern cloud pattern.

## Sources

Research date: **2026-09-10**

Fetched this pass:

- Muni-Link — Water (utility billing) page: https://muni-link.com/water
- Itineris — UMAX for water utilities: https://itineris.net/global/sectors/water-utilities/ ; UMAX Customer Platform: https://itineris.net/north-america/solutionsforutilities/umax-customer-platform/ ; NYC DEP launch announcement: https://itineris.net/nycdep-modernizes-operations-with-umax/
- VertexOne — home (via watersmart.com redirect): https://www.vertexone.ai/home ; Water industry page ("CIS & Billing Software for Water Utilities"): https://www.vertexone.ai/solutions/industries/water
- iWorQ — Water System Management (boundary research): https://iworq.com/systems/water-system-management-software/

Inherited evidence (fetched in prior passes, recorded in their research notes):

- Muni-Link — home, CIS, billing, and product pages (wastewater-utility-management pass, 2026-09-10): https://muni-link.com/ , https://muni-link.com/features/customer-information-system/ , https://muni-link.com/features/billing/ , http://muni-link.com/products/utility-billing-software
- OpenGov — Utility Billing (wastewater pass, snippet-level): https://opengov.com/products/utility-billing
- Oracle Utilities — Customer Care and Billing documentation (gas-utility-management pass, 2026-09-08): https://docs.oracle.com/en/industries/utilities/ , https://docs.oracle.com/en/industries/utilities/customer-care-billing/index.html , https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/CCB_BP_Intro.html
- Advanced Utility Systems — CIS Infinity (gas pass, 2026-09-08): https://advancedutility.com/ , https://advancedutility.com/solutions/customer-information-systems/
- Springbrook — Cirrus Utility Billing (gas pass, 2026-09-08): https://www.springbrooksoftware.com/solutions/utility-billing/
- MuniBilling (gas pass, 2026-09-08): https://munibilling.com/
- Boston Water and Sewer Commission / Itineris case and Mount Pleasant Waterworks case (wastewater pass, trade press): https://www.wwdmag.com/utility-management/article/11004078/updating-oldest-us-water-sewer-system-with-newest-software , https://www.wwdmag.com/utility-management/article/33010188/new-billing-system-alleviates-bottlenecks-for-a-south-carolina-utility

> Sourcing limitations: the water-operations vendor most associated with the operational pole (Sedaru) could not be reached from the research environment (repeated transport failures in the wastewater pass; not retried), so that pole rests on press and procurement documents rather than official product documentation. One boundary vendor's page was captured via search snippet rather than direct fetch. Precise numeric details (rate tables, fee amounts, cycle counts, account volumes, vendor marketing metrics) are intentionally not asserted in this document; claims are calibrated to what the reachable official sources state. Detailed evidence, product-by-product observations, and the full unreachable-source list are recorded in the paired Research Notes.
