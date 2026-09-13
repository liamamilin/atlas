# Utility Customer Information System / CIS

## Overview

A **Utility Customer Information System (CIS)** is a utility operator's customer-and-service system of record: it holds every served premise's utility service as a customer account, accumulates the whole relationship on that record — service state, metering, bills, payments, arrears, contacts, cases — and operates the customer's life cycle from move-in through years of care interactions and recurring bills to move-out.

Two things distinguish it from a generic customer database. First, the account is anchored to a **served premise**: the unit of record is the *service at a place* — a metered utility service (electricity, water, gas, sewer, refuse) delivered to a specific address — not a person and not a device. Second, the care operation is bound to the same record as the money: when a customer calls about a high bill, the representative works from the same account that holds the meter history, the bill, the payment record, and the field work orders.

The market uses two names for this system family. Products named "utility billing" lead with the meter-to-bill-to-money cycle and dominate the small/municipal tier; products named "customer information system" lead with the customer-and-service record and dominate the enterprise and mid-market suite tier. The structure underneath is the same; this document describes the family from the customer-care-led side, where the customer relationship is the organizing spine and billing is one function — albeit an indispensable one — within a broader care-and-commercial operation.

## Users & Context

Primary users, by relationship to the system:

- **customer service representatives (CSRs)** — the front line, at counters and in contact centers. They live in the customer record: answer balance and usage questions, start/stop/transfer service, take payments, resolve billing disputes, log every contact and its outcome.
- **care and case workers** — handle what a simple contact cannot close: high-bill complaints, bankruptcies, payment-assistance arrangements, premise inspections, extended investigations — situations tracked as cases with their own life cycle.
- **billing and back-office staff** — run the recurring billing cycle, correct and reissue bills, administer rates, deposits, and budget plans.
- **collections staff** — work the past-due population through notices, payment arrangements, and disconnect-for-nonpayment decisions.
- **field crews** — receive and complete service orders (turn-ons, turn-offs, meter exchanges, investigations), with results flowing back to the account.

Secondary users: **sales and marketing staff** at the enterprise pole (campaigns over the customer base, quotes for new service or products), **rate and system administrators** (configure rates, bill cycles, care workflows, correspondence templates), **management** (service, revenue, and arrears reporting), and **customers themselves** through the self-service portal that current products commonly provide.

Typical operators are municipal utility departments, water and sewer districts, cooperatives, investor-owned utilities, and private utility companies — from a small town's water department to an enterprise serving millions of service points. In competitive retail markets, the same system family also serves energy suppliers operating the customer seat of a deregulated market.

## Core Model

The system's world is organized around one spine with attached layers:

```text
Customer (person or organization)
  └── relationships & hierarchies (landlord/tenant, parent company, B2B)
        └── Service account  (customer × premise × service state × financial standing)
              ├── Premise / service point → Meter → reads → measured consumption
              │     └── Rates → Bill → payments / adjustments / deposits / arrears
              ├── Care layer: contacts, cases, correspondence, service requests
              └── Service orders (start / stop / change — office ↔ field)
```

### The customer relationship

The customer is a person or an organization, held as a record distinct from any single account. One customer commonly holds several accounts — a homeowner with properties in two towns, a landlord with many tenant accounts, a business with premises across a city. Mature systems therefore carry a relationship layer: landlord/tenant arrangements (with rules for what happens when a rental property reverts to the landlord's account), corporate hierarchies, and multi-premise commercial structures. This layer is what makes the system a *customer* information system rather than a pile of disconnected accounts: the care history, the correspondence, and the commercial relationship accumulate on the customer, while service and money accumulate on the accounts.

### The service account at the premise

The account is the operational spine. It binds one customer to one served premise's utility service, carries the service state (active, inactive, closed) and the account's financial standing, and accumulates everything that happens to the service: consumption, bills, payments, arrears, field work, contacts. Products realize this binding through different object vocabularies — some split it into an account plus a per-service "service agreement" or "contract"; some group the metering side into an "installation" at the premise — but the structure is the same: a persistent, identified account-over-service-point that opens, sustains, and closes through recorded service actions.

### Premise, service point, and meter

The premise is the physical place where service is delivered; the service point is the identified point where the utility's service connects; the meter is the identified device at that point. Meters have their own life in the system — installed, read periodically, exchanged, tested — and every reading attaches to a meter at a premise. Consumption accumulates on the account through this chain: periodic reads (manual route reads, estimates when a read cannot be obtained, remote feeds in metering-modern utilities), validated into usage per billing period. In deregulated markets the service point itself may carry a formal unique identity, because multiple companies may touch the same physical point and must agree on which one they mean.

### Rates, bills, and the money cycle

Configured rates convert measured consumption into charges; the bill is the recurring financial artifact — charges computed from the period's usage and standing charges, issued as a statement on the account, tracked until settled, correctable and reissuable when wrong. The account's financial layer is rich because utilities extend credit: deposits held against the account, payments and adjustments posted, arrears tracked and aged, budget (equal-payment) plans spreading costs across the year, final bills cut when service stops. This money machinery is part of the defining core — a customer system with no bill-and-payment cycle is a CRM, not a utility CIS — but at this pole it is one function among several, not the system's organizing rhythm.

### The care layer

The care layer is what the "customer information" name emphasizes. Its base instrument is the **logged customer contact**: a record of when and why a customer contacted the utility, attributable to the person, the account, or the premise, kept for audit and statistical purposes. Contacts trigger correspondence (letters, emails), reminders, and notifications; a contact that cannot be closed on the spot becomes a **case** — a tracked situation with its own life cycle, used for high-bill complaints, bankruptcies, premise inspections, requests for literature, contractor requests, future-dated changes, and market messages in deregulated environments. Around these sit **service requests** (a customer's request for work or information), **appointments** (scheduled field visits tied to the account), and **correspondence machinery** (templated letters and messages produced from the record). The care layer is modular — products typically let an implementation turn pieces of it on or off and configure their behavior — but the logged-contact-plus-case structure is standard across mature products at this pole.

### Service orders

Service orders are the operational instrument connecting the office to the field. They carry the physical acts that change the account's service state — turning service on, turning it off, exchanging or testing a meter, investigating a reported issue — and they are dispatched to field crews and completed with recorded results that flow back into the account. The service order is where the customer's money state and the physical state meet.

### What the core deliberately does not include

The network itself (mains, pipes, conductors, substations) is not an object in this system's world — network data enters only as the delivery context of served premises. Large-scale meter-data infrastructure is an adjacent layer: here the meter exists to serve the customer relationship and its bills. Real-time outage prediction on a network model belongs to outage management; this system logs the customer's call, it does not predict the outaged device. And the care layer, however rich, is not a generic CRM: its objects are utility-shaped and bound to served premises.

## How It Works

### Establish the relationship: move-in

```text
Customer requests service
→ customer record created or matched (existing customer, new premise)
→ service account opened for the customer at the premise
→ credit standing checked, deposit set where required
→ service order created and dispatched to the field
→ crew turns on service (meter set if not present)
→ service state becomes active; billing begins
```

Move-ins are the system's front door, and mature products treat them as a high-volume guided workflow — including the awkward variants: moving a customer into a premise that is still occupied (forcing the prior occupant's move-out), future-dated moves, and transfers of service responsibility within a customer's own portfolio.

### The live relationship: the care loop

```text
Customer makes contact (phone, counter, portal, email)
→ contact logged against the person / account / premise
→ representative works the record: balance, usage, bills, open orders
→ resolved on the spot → contact closed, outcome recorded
→ not resolvable → case opened with category and owner
→ case worked: investigation, correspondence, follow-ups
→ case closed with outcome; contact history accumulates
```

The loop's signature is that the representative never leaves the customer's record: the bill in dispute, the meter history behind it, the payment record, the open service order, and the past contacts are one picture. Correspondence is produced from the same record — templated letters and notifications triggered by contacts, cases, and billing events.

### The billing cycle: one function inside the relationship

```text
Billing period closes
→ consumption × configured rates → charges
→ bill produced (batch runs over cycle populations; on demand for moves and corrections)
→ bill completed: routed, printed/emailed, posted to the account
→ payments posted; unpaid balances age into arrears
→ past-due processing: notices → payment arrangements → disconnect decision
→ disconnection itself is a service order; restoration likewise
```

This is the family's revenue engine, and it runs exactly as in the billing-led pole of the family: batch bill runs over the served population, a managed bill life cycle (created, completed, corrected, cancelled and reissued, written off), and the money cycle tracked on the account. The difference is emphasis, not structure — here the bill cycle is described to the reader as one function of the customer system; the paired Utility Billing Platform document describes the same cycle as its organizing spine.

### Change events

Move-outs reassign or close the account layer over the premise (with final bills cut at stop); meter exchanges close one meter's reading history and open the next with prorated billing; rate changes reconfigure future bills without touching posted history; landlord reversion moves tenant accounts back to the property owner. Every money transaction posts to an audit trail — the account is a ledger, not just a profile.

### Capability tiers

**Defining core** — without these, not this Type:

- the served-premise service account of record (customer × premise × service state × financial standing)
- the metered-consumption basis (meters at service points, periodic reads, usage per billing period)
- the meter-to-bill-to-money cycle (recurring bills under configured rates; payments, adjustments, deposits, arrears on the same account)

**Standard capabilities** — present across mature products at this pole:

- the customer-relationship layer (persons/organizations, multiple accounts, hierarchies, landlord/tenant)
- the care layer (logged contacts, cases, correspondence, service requests)
- service orders as the office↔field instrument
- the credit machinery (deposits, budget plans, collections, disconnect coupling)
- customer self-service portal
- reporting over service, revenue, and arrears

**Common variants and optional extensions** — depend on market, tier, and era:

- commercial breadth: quotes, sales & marketing campaigns, appointments scheduling, loans, rebate claims
- deregulation machinery: market messages, registration of supply points, supplier/distributor seat split
- interval billing and AMI-era metering integrations; embedded meter-data modules
- contact-center add-ons (telephony, chat, AI assistance); ERP-embedded or suite-embedded packaging

## Interfaces

Described conceptually; names and layouts vary by product.

### Customer 360 workspace

The primary working surface for customer-facing staff — the "one picture" of the customer. Typical information: customer identity and relationships, accounts with service addresses and states, current balance, recent bills and payments, meter and consumption history, open cases and service orders, recent contacts. Primary actions: start/stop/transfer service, take payment, issue adjustment, log a contact, open a case, create a service order, produce correspondence.

### Contact and case worklists

The care operation's management surface. Typical information: open contacts and cases by category, age, owner, priority; SLA or follow-up indicators. Primary actions: assign, work, escalate, correspond, close with outcome.

### Billing and rate configuration

Back-office surface for the revenue machinery: rate structures, bill cycles and calendars, bill runs and their status, exception queues. Primary actions: configure rates, execute bill runs, process reads, correct and reissue bills.

### Collections worklist

The arrears surface: past-due accounts by age, notice status, promise-to-pay state. Primary actions: generate notices, arrange payment, order disconnect or restoration.

### Service order board / dispatch

The office↔field surface: open orders by type (turn-on, turn-off, exchange, investigation, disconnect, restore), priority, assignment. Primary actions: create, dispatch, reschedule, review completed work flowing back from the field.

### Customer portal (common modern layer)

Customer-facing web/mobile surface: balances and bills, usage history, payment initiation, service requests, move-in/move-out requests.

## Important Rules / Behaviors

- **Money and service state are coupled.** Arrears drive notices, then disconnect service orders; payment drives restoration. Deposits are held as credit protection and settled into the account's history. This coupling is the family's signature behavior: financial standing drives field action.
- **A stopped service ends with a final bill.** Stop-service cuts the meter's last read, produces the closing statement, and the balance must resolve — the account persists even when service does not.
- **Contacts are records, not chatter.** The logged contact — who called, why, about which account or premise, with what outcome — is an instrument of record kept for audit and statistical purposes, and it can seed cases, letters, and reminders.
- **Care machinery is implementation-configured.** Products treat cases, correspondence, and related care functions as configurable modules: an implementation defines case categories, letter templates, and workflow behavior. The structure is standard; the configuration is local.
- **Estimates carry an obligation to true up.** Estimated usage is provisional; the next actual read reconciles the account.
- **The account is an audited ledger.** Payments, adjustments, deposits, and write-offs post as attributable financial transactions; corrections appear as their own documents rather than silent rewrites.
- **The customer outlives any single service.** Customers accumulate accounts, premises, and history over years; the relationship layer is what makes the system a customer system rather than an account list.
- **In deregulated markets, identity is formal.** Supply points carry unique registered identities so that multiple market participants can refer to the same physical point unambiguously; market messages (enrollment, switches, moves between suppliers) arrive as structured events the system must process against the right account.

## Variants

- **Commodity composition** — single-commodity utilities vs multi-service organizations holding electricity, water, sewer, refuse, stormwater (and fiber, in some municipalities) on one customer record.
- **Market structure** — the largest structural variant. Where the utility both delivers and sells the service, the system prices and bills the commodity. Where retail competition separates suppliers from the network owner, the customer-and-billing function is operated on the supplier's side of the market, with formal supply-point identity and market-message machinery; the same product family serves both seats.
- **Ownership and scale** — small-city packages at one end; cooperative and municipal suites in the middle; enterprise platforms serving millions of accounts at the other. The core is stable across the range; care and commercial depth scale with it.
- **Packaging philosophy** — standalone CIS products; CIS-plus suites (with work management, financials, even human resources); CIS+CRM+ERP platforms built on general-purpose business platforms; ERP-embedded realizations where the money side is a purpose-built subledger inside the finance core.
- **Deployment** — cloud-hosted vs on-premise vs vendor-hosted; a procurement differentiator, not a structural one.
- **Metering era** — monthly-manual-read deployments vs interval-metered deployments feeding billing and usage analytics; the latter is a growing configuration, not a requirement.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Utility Billing Platform | same family, other pole | the billing-led pole of the same structure: the meter-to-bill-to-money cycle is the organizing spine, the name dominates the small/municipal tier, and the enterprise care breadth is thin or absent; here the customer/service record is the spine and care is first-class |
| Billing Platform (generic) | generic spine | holds billing accounts, computes charges, produces bills for any vendor; this Type adds the utility machinery — served-premise accounts, metered consumption, service-state coupling, utility rates |
| Gas / Water Utility Management | commodity verticals | the same structure anchored on one commodity's domain and market structures; this leaf is the horizontal family |
| Meter Data Management / AMI | adjacent infrastructure | validates and stores billing-quality meter data and publishes bill determinants *to* this system; here the meter exists to serve the customer relationship and its bills |
| Outage Management System | adjacent, data-source seam | predicts outages on a network model and runs crew restoration; this system logs the customer's call and supplies the customer-identity/phone/service-point data the OMS matches against — a call log without network-model prediction is trouble-call logging, not outage management |
| Customer Relationship Management (generic) | care-shaped neighbor | generic CRM has no premise/meter/bill structures; this system's care objects are utility-shaped and bound to served premises, and its spine includes the money cycle |
| Subscriber Management (telecom) | industry analog | the connectivity provider's subscriber system of record; identity and service semantics are connectivity-based, not premise-anchored metered service |
| Utility Field Service Management | adjacent layer | owns crew scheduling and workforce machinery in its own right; here field work appears as service orders bound to service accounts |
| Utility Rate Management | adjacent layer | rate design, modeling, and analysis; here rates are *executed* inside the bill cycle |
| Utility Revenue Assurance | adjacent discipline | audits the revenue chain for leakage; here the revenue cycle is *run* |
| Customer Portal | surface layer | the customer-facing self-service surface over the same records; no transactions of record originate there |
| Customer Energy Management | customer seat | the customer's own view and advice over their usage; no operator records |

## Representative Products

- **Oracle Utilities — Customer Care and Billing (Cloud Service)** — enterprise-tier CIS; its documentation is unusually explicit about both the object model (customer/account/premise/service-point structures with bills, payments, meters, and field activity attached) and the care breadth (contacts, cases, letters, sales & marketing, quotes, appointments)
- **SAP S/4HANA Utilities (IS-U with Customer Engagement)** — enterprise ERP-embedded realization: the customer-centric trio of business partner, contract account, and contract over technical master data, with an interaction-center care layer
- **Itineris — UMAX Utility Suite** — international CIS+CRM+ERP suite for energy and water utilities built on a general-purpose business platform; the clearest statement of care modules natively integrated with the CIS core
- **Cayenta** — mid-market North American utility suite (customer information system with billing, work management, and financials)
- **NorthStar — Customer Information & Billing** — mid-market CIS with customer portal and mobile workforce management, serving municipal and cooperative utilities

The family structure was checked against the billing-led pole (small/municipal utility-billing products), the commodity verticals, the paper-era utility office, and the competitive-retail supplier seat to avoid over-fitting to the enterprise CIS pattern.

## Sources

Research date: **2026-09-10**

- Oracle Utilities — Customer Care and Billing Cloud Service, Business User Guide (TOC; Customer Information; Understanding the "V"; Case Management; Customer Contacts): https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/CCB_BP_Intro.html
- SAP Learning (official) — Exploring Utilities Data Model; Attending the Customer with Customer Engagement; Analyzing Customer Service and Engagement Processes; Understanding Billing Processes and Master Data: https://learning.sap.com/
- Itineris — UMAX Utility Suite and UMAX Customer Platform: https://www.itineris.net/ , https://itineris.net/global/solutionsforutilities/umax-customer-platform/
- Cayenta: https://www.cayenta.com/
- NorthStar: https://www.northstarutilities.com/

> Sourcing limitations: the cooperative-tier vendor most associated with the CIS name could not be reached from the research environment (repeated timeouts across passes), and one municipal-tier CIS vendor's site was unreachable this pass — no claims are drawn from either; their tier is covered by the sampled mid-market products instead. One enterprise vendor's help portal is readable only through indexed excerpts of its official pages, so its evidence is held at slightly reduced strength. Precise operational details (numeric limits, state vocabularies, configuration defaults) are intentionally not stated in this document; they remain in the paired Research Notes.

Detailed evidence, product-by-product observations, the cross-product comparison, and the boundary analysis against the sibling Utility Billing Platform are recorded in the paired Research Notes.
