# Gas Utility Management

## Overview

A **Gas Utility Management** application is a gas utility's customer-service business system of record.

It holds every served premise's gas service as an account, binds meters and measured gas consumption to those accounts, and runs the cycle through which the utility actually operates its customer base: start service, meter it monthly, bill it under configured rates, collect payment, manage deposits, arrears, budget plans and collections, and dispatch the field work — turn-ons, turn-offs, meter exchanges — that physically opens, sustains, and closes each service.

Its boundary: this is the **customer-and-money** system of a piped-gas utility, not the system that models the pipes themselves (that is the pipeline/network layer), and not the meter-data infrastructure that feeds it. The market realizes it through utility customer-information and billing platforms that serve several commodities — a product built for "electric, water, gas, and multi-service providers" deployed for gas — with the piped-gas domain and its market structures as the vertical anchor.

## Users & Context

Primary users, by relationship to the system:

- **customer service representatives** — front counter and call center; open the account of record constantly: answer balance and usage questions, start/stop/change service, take payments, resolve billing questions
- **billing and back-office staff** — run the recurring billing cycle, process meter reads, issue bills, apply adjustments, administer rates, deposits, and budget plans
- **collections staff** — work the past-due population through notices, payment arrangements, and disconnect-for-nonpayment decisions
- **field crews** — receive and complete service orders (start/stop service, meter exchanges, investigations), typically on mobile devices, with results flowing back to the account

Secondary users: **rate and billing administrators** (configure rates, budgets, deposit rules), **management** (revenue, arrears, and consumption reporting), and **customers themselves** through the portal layer (common in current products).

Typical operators are municipal gas departments, utility cooperatives, and regulated gas distribution utilities; the same product family also serves multi-service utilities where gas is billed alongside electricity, water, or refuse on one account.

## Core Model

The defining structure is three parts held together — remove any one and the product stops being this kind of system:

```text
Served premise (gas service point)
  └── Service account  (customer × premise × service state × financial standing)
        ├── Meter → reads → measured consumption
        │     └── Rates → bill → payments / adjustments / deposits / arrears
        └── Service orders (start / stop / change — office ↔ field)
```

### Service account

The account is the spine. It binds one customer to one served premise's gas service, carries the service state (active, inactive, closed) and the account's financial standing, and accumulates the whole relationship: consumption history, bills, payments, arrears, contacts. Everything else hangs off it. Utility vendors name this population the "customer service points" — the phrase captures that the unit is the *service at a place*, not the person and not the device.

### Premise and meter

The premise is the physical place where gas is delivered and measured; the meter is the identified device at that place. Meters have their own lifecycle in the system — installed at a premise, read periodically, exchanged, tested — and every reading attaches to a meter at a premise. Consumption accumulates on the account through this chain: periodic reads (manual route reads; estimates when a read cannot be obtained; remote feeds in metering-modern utilities), validated into usage per billing period.

### Rates and the bill

Configured rates convert measured consumption into charges — flat blocks, tiered usage steps, and seasonal variations are the standard shapes, with commodity-linked components appearing where the utility sells the gas itself (see Variants). The bill is the recurring financial artifact of the cycle: charges computed from the period's usage and standing charges, issued as a statement on the account, tracked until settled. The account's financial layer is rich because utilities extend credit: deposits held against the account, payments and adjustments posted, arrears tracked, budget (equal-payment) plans spreading costs across the year, and final bills generated when service stops.

### Service orders

Service orders are the operational instrument connecting the office to the field. They carry the physical acts that change the account's service state — turning service on at a premise, turning it off, exchanging or testing a meter, investigating a reported issue — and they are dispatched to field crews and completed with recorded results (readings, notes, photos, signatures) that flow back into the account record. The service order is where the money state and the physical state meet.

### What the core deliberately does not include

The pipe network itself (segments, valves, pressure zones) is not an object in this system's world — network data enters only as the delivery context of served premises. Real-time telemetry, network modeling, and integrity machinery belong to other systems. Likewise, large-scale meter-data infrastructure is an adjacent layer: in this system the meter exists to produce bills, and a deployment without AMI machinery remains complete.

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
```

Reads are not always obtainable: products commonly provide for estimated billing, with the account trued up when an actual read arrives.

### The billing cycle

```text
Billing period closes
→ consumption × configured rates → charges
→ bill issued as a statement on the account
→ payments posted (counter, mail, lockbox, online, autopay)
→ unpaid balances age into arrears
→ past-due processing: notices → payment arrangements → disconnect decision
→ disconnection itself is a service order; restoration likewise
```

The coupling between money and service state is the signature behavior of the Type: financial standing drives field action. In utility practice, an unpaid balance works through notices and payment arrangements toward a disconnect decision — and the disconnect itself is field work recorded against the account through the same service-order machinery, as is the restoration that follows payment.

### Change events

Move-ins and move-outs reassign the account layer over the same premise (with final bills cut at stop); meter exchanges close one meter's reading history and open the next with prorated billing; rate changes reconfigure future bills without touching posted history. Every money transaction posts to an audit-trail — the account is a ledger, not just a profile.

### Standard capabilities layered on the core

- customer portal (balances, usage, payments) and notifications (SMS/email) as the modern self-service layer
- payment machinery: online payments, payment processors, lockbox, autopay
- reporting and dashboards over consumption, revenue, and arrears; general-ledger integration so the money cycle lands in the finance core
- mobile workforce tools for service-order dispatch and completion
- integration substrate (APIs) to metering/AMI systems and to the surrounding utility product family

These make the system practical but are not what makes it this Type: deployments without portals, without AMI, and without mobile tools — including the entire paper era — ran the same core.

## Interfaces

Described conceptually; names and layouts vary by product.

### Account / premise workspace

The primary working surface for customer-facing staff. Typical information: account holder, service address, service state, current balance, recent bills and payments, meter and consumption history, open service orders. Primary actions: start/stop/change service, take payment, issue adjustment, create service order, answer usage and billing questions.

### Billing and rate configuration

Back-office surface for the revenue machinery. Typical information: rate structures and their components, billing runs and their status, estimate and read queues. Primary actions: configure rates, run billing, process reads, correct and reissue bills.

### Service order board / dispatch

The office↔field surface. Typical information: open orders by type (turn-on, turn-off, exchange, investigation), priority, assignment. Primary actions: create, dispatch, reschedule, review completed work flowing back from the field.

### Collections worklist

The arrears surface. Typical information: past-due accounts by age, notice status, promise-to-pay state. Primary actions: generate notices, arrange payment, order disconnect or restoration.

### Reporting / dashboards

Management surface over the population: revenue, arrears aging, consumption trends, billing-run outcomes.

### Customer portal (common modern layer)

Customer-facing web/mobile surface: balances and bills, usage history, payment initiation, service requests.

## Important Rules / Behaviors

- **Money and service state are coupled.** Arrears drive notices, then disconnect service orders; payment drives restoration. Deposits are held against accounts as credit protection and settled into the account's history.
- **A stopped service ends with a final bill.** Stop-service cuts the meter's last read, produces the closing statement, and the account's balance must resolve — the account persists even when service does not.
- **Meter changes do not break the bill.** An exchange reads out the old meter and reads in the new one; the billing period is prorated across the two devices.
- **Estimates carry an obligation to true up.** Estimated usage is provisional; the next actual read reconciles the account.
- **Budget plans spread, not discount.** Equal-payment arrangements average cost across periods while consumption continues to be measured and trued.
- **The account is an audited ledger.** Payments, adjustments, deposits, and write-offs post as attributable financial transactions; posting history is not silently rewritten.
- **Service orders are recorded work.** Field completion (readings, notes, photos, signatures) returns to the account record; the office and the field see the same state.

## Variants

- **Market structure** — the largest variant. Where the utility both delivers and sells the gas (the dominant North American pattern for local distribution utilities), the customer system prices and bills the commodity itself, including commodity-linked charge components; where retail competition separates suppliers from the pipe owner, the customer-account-and-billing function is instead operated on the supplier's side of the market with the network utility as a distinct seat. Which seat a given system serves changes its commercial scope more than its object model.
- **Commodity composition** — gas-only utilities vs multi-service utilities billing gas alongside electricity, water, sewer, or refuse on one account.
- **Ownership and scale** — small-city government packages at one end; cooperative and municipal suites in the middle; enterprise platforms serving millions of service points at the other. The core is remarkably stable across the range; depth (rates machinery, analytics, integration) scales with it.
- **Deployment** — cloud-hosted vs on-premise; a live differentiator in procurement, not in structure.
- **Metering era** — monthly-manual-read deployments vs interval-metered deployments, where interval data feeds billing and usage analytics; the latter is a growing configuration, not a requirement.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Gas Pipeline Management | sibling | the pipeline operator's **network** system of record — connected pipe-segment model with integrity, pressure/hydraulic, and inspection lifecycle; its products consume customer data only as load on the network. Here the served-customer economy is the managed world |
| Utility Customer Information System | horizontal family | the record-layer machinery of the same family for any commodity; this leaf is the gas-industry vertical edition anchored on piped-gas service and its market structures |
| Utility Billing Platform | horizontal family | the billing engine slice; a billing engine without the service-account spine and service-order loop is a component of this Type, not the whole |
| Meter Data Management / AMI | adjacent infrastructure | meter-data collection and validation infrastructure; here the meter is grounded at accounts/premises to produce bills, and the deployment is complete without AMI |
| Utility Field Service Management | adjacent layer | owns crew scheduling and workforce machinery in its own right; here field work appears as service orders bound to service accounts |
| Utility GIS | adjacent layer | models the network assets and their geography; not a managed object of this Type |
| Customer Energy Management | customer seat | usage visibility and advice for the customer; no transactions of record |
| Water Utility Management | same family, other commodity | identical family structure over water service; the commodity's measurement and market structures are the domain binding |
| Energy retail / supplier systems | different market seat | in competitive retail markets the supplier holds customer accounts and billing on supplier-facing suites; adjacent seat, same object family |
| Propane / LPG delivery management | different business | bottled-gas delivery is a route/tank logistics business, not a piped metered utility service |

## Representative Products

- **Advanced Utility Systems — CIS Infinity** — mid-market customer information and utility billing platform for electric, water, gas, and multi-service providers (North America / Caribbean)
- **Oracle Utilities — Customer Care and Billing (Cloud Service / Customer to Meter family)** — enterprise-tier customer care and billing serving electricity, natural gas, and water utilities worldwide
- **Springbrook — Cirrus Utility Billing** — small-municipality government utility billing (water/electric/refuse pole of the same product family)
- **Gentrack** — supplier-side customer, billing and debt platform for competitive retail energy markets (the "supplier seat" of the family)
- **NorthStar Utilities Solutions** — CIS/portal/mobile-workforce suite for small utilities

## Sources

Research date: **2026-09-08**

- Advanced Utility Systems — CIS Infinity product pages: https://advancedutility.com/ , https://advancedutility.com/solutions/customer-information-systems/
- Oracle Utilities — documentation index and Customer Care and Billing Cloud Service guides: https://docs.oracle.com/en/industries/utilities/ , https://docs.oracle.com/en/industries/utilities/customer-care-billing/index.html , https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/CCB_BP_Intro.html
- Springbrook — Cirrus Utility Billing: https://www.springbrooksoftware.com/solutions/utility-billing/
- Gentrack — sector pages: https://www.gentrack.com/ , https://www.gentrack.com/energy-retailers/
- NorthStar Utilities Solutions: https://www.northstarutilities.com/
- MuniBilling: https://munibilling.com/

> Sourcing limitation: the vendors most literally associated with the phrase "gas utility management" (NISC, CSA) and several others (Tyler, Banyon) could not be reached from the research environment on 2026-09-08, and no sampled product's gas-specific commercial modules (commodity-cost recovery, gas-unit conversions, safety-call handling) were directly documentable. Claims about those structures are therefore kept at variant/uncertainty strength, and the document's core describes only the structure corroborated across the reachable sample. Detailed evidence and the full unreachable-source list are recorded in the paired Research Notes.
