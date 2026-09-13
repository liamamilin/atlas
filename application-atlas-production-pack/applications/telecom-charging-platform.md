# Telecom Charging Platform

## Overview

A **Telecom Charging Platform** is a communications service provider's real-time money-computation system for service consumption: the software that rates what network and digital service usage costs, holds each subscriber's money-side state (balances, allowances, reservations), and controls service delivery in real time based on that state.

Every time a subscriber makes a call, opens a data session, sends a message, streams content, or invokes a network API, the operator must answer two questions immediately: *what does this usage cost under the subscriber's plan?* and *can the subscriber's account pay for it?* The charging platform is the system that answers both — and its answers gate the service itself: when the account cannot pay, the usage does not proceed.

The industry's own standards (3GPP charging architecture) define the core of this system as three functions that always appear together: a **rating function** (determining the value of resource usage in monetary or non-monetary units), **account/balance management** (subscriber accounts holding monetary and non-monetary balances), and **quota/credit control** (authorizing and supervising resource usage against those balances in real time). The dominant product form is the *convergent charging system* — one system handling prepaid (real-time balance control) and postpaid (charges accumulating toward a bill) across all service types.

The charging platform is a component of the wider **Telecom BSS** commercial chain — it is where that chain resolves into money — but it has its own market depth: standalone charging engines are sold, deployed, and replaced on their own. Its neighbors are fixed: usage events arrive from **mediation**, commercial terms arrive from the **product catalog** and the subscriber's owned offers, entitlement and status context arrives from **subscriber management**, and the charges it produces flow downstream to **billing**, which aggregates them into invoices per settlement period. Charging computes; billing bills.

## Users & Context

The charging platform has no end-consumer face of its own; subscribers experience it only through its effects (service that stops when balance runs out, real-time notifications, self-service balance views fed by its APIs). Its direct users are the operator's staff:

- **Charging/monetization configuration staff** — define and maintain the rating logic: tariff structures, rate plans, discounts, promotions, allowances, and the mapping from commercial offers to chargeable rules. In mature deployments this work is done against the operator's product catalog and synchronized into the charging engine.
- **Charging operations engineers** — run the platform itself: monitor throughput and latency, manage capacity, handle rating or balance anomalies, and maintain the real-time service-level guarantees the network depends on. Charging sits in the service path, so it is operated with the discipline of network equipment, not back-office software.
- **Customer care agents** (indirect) — read balances, reservations, and charge history through balance-query surfaces to answer "how much do I have left?" and "what was I charged?"; trigger adjustments and goodwill credits where the product supports them.
- **Billing and finance operations** (downstream consumers) — receive the charges and rated events the platform produces; their billing cycles, revenue recognition, and reconciliation all depend on charging output being complete and correct.
- **Partner/wholesale managers** (where partner models exist) — configure revenue-sharing rates and verify partner-related charging and settlement data.

The context is any communications service provider: mobile operators, fixed/broadband providers, cable operators, converged groups, MVNOs and MVNEs (which often run charging as a hosted service for their brands), and digital providers. At operator scale the platform processes enormous real-time event volumes — it is engineered for carrier-grade availability and latency, because a charging outage is a service outage for prepaid users.

## Core Model

The charging platform's world is organized around one computation and one state:

### Usage / service event

The unit of input. Anything chargeable arrives as an event carrying the data rating needs: who (subscriber/service identifier), what (service type), and how much (duration, volume, occurrences, or other measures). A phone call needs calling number and start/end times; a data session needs volume; a message needs occurrence; a content purchase needs the item. Events arrive in real time from the network/service layer (via mediation) for online charging, or as collected usage records for offline batch rating. Some events are not subscriber usage at all but system-generated charges — monthly subscription fees, for example — which flow through the same computation.

### Charge offer / tariff

The unit of commercial terms. Every subscriber holds offers (plans, bundles, options) whose charge definitions say how events of each type are priced: per-minute rates, per-megabyte tiers, free units, bonuses, one-time fees, recurring fees. Rating is offer-driven: the engine identifies the customer, looks up the offers they own, and rates the event according to those offers — if the customer changes offers, subsequent usage is rated under the new terms. The measurement itself is configured as ratable usage metrics — the units an event is measured in (seconds, megabytes, events) and how they are calculated — with linear and non-linear pricing structures on top.

### Rating → charge

The defining computation. The engine determines the value of the resource usage — in money or in non-monetary units — under the applicable offer, producing a **charge**: the money-bearing record attributed to the subscriber. Charges are the platform's output to the world: downstream billing aggregates them into invoices; revenue reporting counts them; care agents explain them.

### Subscriber account / balance

The money-side state. Each subscriber account holds balances organized as balance elements — currency, data volume, voice minutes, vouchers, bonuses — that charges draw down and recharges replenish. Balances carry rules: validity periods, consumption order across multiple buckets, credit limits, thresholds. This state is the platform's own record: it is updated in real time as events are rated, and kept consistent with the wider BSS's subscriber/billing records.

### Reservation / quota

The in-flight state. For session-based usage (a call, a data session), the platform does not wait until the session ends to learn the cost. It authorizes usage in limited scope — reserving a slice of balance and granting the network a quota (so many minutes, so many bytes) — and supervises consumption against it. When the quota runs out, the network asks for more (re-authorization); when the session ends, the platform settles: consumes what was used, returns what was not. Reservations prevent one session from spending balance another session needs.

### The service-path interaction (credit control)

What makes this a charging *platform* rather than a rating engine inside billing. The network consults the platform before permitting resource usage; the platform answers in real time — authorize (with quota) or reject (insufficient credit, inactive service). The standards define this as online charging: charging information that *affects, in real time, the service rendered*. An exhausted balance stops or limits service; a top-up during a session can resume it.

### The structure in one picture

```text
Product catalog / offers ──terms──▶ Charge offers owned by the subscriber
                                        │
Usage events (from network, via mediation) ──▶ RATING ──▶ Charge
                                        │                       │
                    ┌───────────────────┘                       ▼
                    ▼                              Rated events / charges ──▶ BILLING
        Subscriber account / balance                          (aggregation per period)
        (currency + non-currency buckets)
                    ▲
        recharge / top-up │ reservations (in-flight sessions)
                    │
        CREDIT CONTROL ◀── consults ── NETWORK (before/during usage)
                    │
        authorize / reject / re-authorize / terminate
```

## How It Works

### The online charging loop (the defining workflow)

```text
Subscriber starts using a service (call, data session, content, API call)
→ network sends an authorization request to the charging platform
→ platform authenticates the subscriber and checks the account
  (credit limit, service status; some products also screen duplicate sessions)
→ platform rates the anticipated usage under the subscriber's owned offers
→ platform reserves balance and grants a quota to the network
→ network delivers service, supervising consumption against the quota
→ quota exhausted → network re-requests; platform re-authorizes
  (or terminates the session if the account cannot pay)
→ subscriber tops up mid-session → balance changes can trigger re-authorization
→ session ends → platform settles: rates the actual usage,
  consumes the reserved amount, returns unused reservation
→ rated event and balance update recorded; charge flows toward billing
```

This loop runs in real time, millions of times concurrently. It is the reason prepaid service works: the network never delivers what the account has not paid for.

### The offline rating path

```text
Network records usage (CDRs / usage records) as it happens
→ mediation collects, normalizes, deduplicates, assembles the records
→ records are submitted to the charging platform as usage requests
→ platform batch-rates them under the subscriber's offers
→ charges and balance updates produced
→ charges flow to billing for the settlement period
```

Offline charging never gates the service — the usage has already happened; it affects only what the subscriber will be billed. Mature platforms run both paths in one convergent system against one subscriber record, which is what lets an operator mix prepaid and postpaid, and online and offline services, freely.

### Configuring the money logic

```text
Commercial offer designed in the product catalog
→ charge/rating rules configured (rate plans, RUMs, discounts, allowances)
→ rules deployed to the charging engine and bound to subscriber offers
→ subscribers purchase/change offers
→ their subsequent usage is rated under the new terms
```

Rating configuration is the platform's most business-sensitive surface: a mis-configured tariff mis-prices the entire base. Changes follow controlled deployment paths, and the platform's pricing logic is one of the main enforcement points for revenue protection.

### Feeding the subscriber-facing edge

```text
Subscriber (or care agent, or app) requests balance information
→ balance query against the platform's account state
→ balances, reservations, allowances returned
→ self-service top-up / recharge
→ platform credits the balance (immediately usable, even mid-session)
```

## Interfaces

The surfaces are operator-facing consoles and machine interfaces; exact layouts vary by product.

### Rating / tariff configuration

- Purpose: define and maintain how usage is priced.
- Typical information: rate plans, ratable usage metrics, price tiers, discounts, promotions, allowances, validity rules, offer-to-charge bindings.
- Primary actions: create/modify rating rules, bind them to catalog offers, deploy to the engine, test and version changes.

### Charging operations / monitoring

- Purpose: keep the real-time money engine healthy.
- Typical information: event throughput, latency, error and rejection rates, balance-engine health, session/reservation counts, rated-event flow to billing.
- Primary actions: monitor, alert, capacity-manage, investigate rating anomalies, replay or correct failed events.

### Balance and top-up interfaces (APIs)

- Purpose: let surrounding systems read and change the money state.
- Typical information: balance elements (currency and non-currency), active reservations, credit limits, validity/rollover state.
- Primary actions: query balances (for self-care apps, care agents, IVR systems), execute top-ups/recharges, apply adjustments and vouchers.

### Integration surfaces

- Upstream: mediation systems delivering normalized usage requests (online events and offline records).
- Downstream: billing systems consuming rated events and charges.
- Sideways: policy controller (balance thresholds, QoS-relevant notifications), CRM/self-care (offers owned, balance views), provisioning (service status).

### Self-service edge

- Purpose: the subscriber's window into their own money state.
- Typical information: current balance, allowances remaining, recent charges, top-up options.
- Primary actions: check balance, top up, buy bundles (where the product extends to offer purchase).

## Important Rules / Behaviors

### Authorization gates service

The platform's answers control the network: no authorization, no usage. Rejection reasons are structural — insufficient credit, service not active on the account — and the network enforces the decision by not delivering (or by terminating) the resource usage. This is the property that makes charging part of the service path rather than back-office accounting.

### Authorization is scoped and renewed

Permission to use the network is granted in limited scope (a quota of minutes or bytes), not for the whole session in advance. The network supervises consumption against the quota and returns for more; the platform re-authorizes while the account can pay. Unused reservations are returned to the balance at settlement.

### Reservations hold balance

While a session is in flight, its reserved amount is not available to other sessions. This prevents concurrent services from overspending one balance, and it means the *visible* balance and the *spendable* balance can differ — a distinction every balance-query consumer must respect.

### Rating is offer-driven and point-in-time

Usage is rated under the offers the subscriber owns at the time of usage. Changing offers changes subsequent rating, not past charges. Rating configuration is therefore a controlled, versioned, business-critical artifact — errors mis-price the base at real-time speed.

### One account, many units

Balances are not only money: data buckets, minutes, vouchers, and bonuses are all balance elements with their own consumption rules, validity, and ordering. A charge can consume several balance elements at once (pay from a free-unit bucket first, then currency).

### Convergence is the operating model

Prepaid and postpaid, online and offline, all service types — one system, one subscriber record. This is the industry's standard answer to mixed payment models and mixed services, and it is why charging sits at the center of the money side rather than at the edge. The bill, however, remains downstream: charging produces charges; billing turns them into invoices per settlement period.

### Charging state and subscriber state interlock

The platform checks service status and entitlements before authorizing: a suspended or unentitled service is not charged and not delivered. Conversely, charging state (exhausted balance, credit limit) can drive service restrictions and policy actions. The subscriber record's lifecycle (sibling Subscriber Management territory) gates the platform; the platform's money state constrains the service.

## Variants

Common shapes of the Type:

- **By payment-model emphasis** — pure prepaid OCS lineages (real-time balance control as the whole product), postpaid-centric rating deployments, and the dominant convergent form handling both.
- **By service breadth** — mobile-centric engines (voice/data/messaging), multi-play engines adding fixed/broadband/TV, and digital-service engines adding content, IoT, and API consumption.
- **By deployment** — on-premises carrier platforms, cloud-ready stacks, cloud-native/SaaS engines (including public-cloud marketplace distribution), and edge-distributed topologies where latency-critical session handling runs close to the network and central balance management runs in a core cloud.
- **By business model** — operator-owned platforms; hosted charging for MVNO/MVNE programs (charging-as-a-service, multi-tenant); cross-industry engines rating non-telco consumption for verticals that borrow the same mechanics.
- **By era-current capability** — 5G slice-based and cross-slice charging (pricing on latency, throughput, coverage, slice lifecycle), network-API invocation charging, AI-assisted personalization and anomaly detection. These extend the same core to new chargeable events and new pricing dimensions.

A variant remains this Type as long as the three-part core — rating consumption, holding balances, enforcing in the service path — is intact. Remove the service-path enforcement and only offline rating remains (a billing-side rating engine); remove the money computation and only policy control remains.

## Related Application Types

| Application Type | Relationship | Distinction |
|---|---|---|
| Telecom BSS | the suite it lives in | BSS is the integrated commercial chain (offer → order → subscription → charging → billing → care) over shared records; the charging platform is the money-computation component that chain resolves into — no orders, no care, no catalog ownership |
| Telecom Billing / Subscription Billing Platform | downstream consumer | billing aggregates charges per settlement period into invoices, presentment, payments, collections; charging computes charges in (near) real time and holds balances. Suites ship both; the functions stay distinct |
| Mediation (usage data management) | upstream supplier | mediation collects and normalizes usage events from network elements (dedup, assembly); charging rates them. The seam is the normalized usage request |
| Policy Control (PCF/PCRF-class) | coupled sibling | policy gates and shapes service by rules without computing money; charging computes money and can drive policy via balance thresholds. Coupling depth varies; bundling is a variant |
| Subscriber Management | upstream state | holds the subscriber population, entitlements, and lifecycle status; charging reads them and holds the money state. Status gates charging; neither subsumes the other |
| Telecom Product Catalog | upstream terms | the catalog defines offers/tariffs as the source of sellable terms; charging consumes them. Tariff configuration inside a charging product is the catalog function at component depth |
| Telecom Revenue Assurance | watching discipline | revenue assurance detects leakage between consumption and charges across the chain; charging is the enforcement point it watches, not the watcher |
| Utility Customer Information System / Meter Data Management | structural neighbor | same money-computation skeleton (usage → rate → charge → bill) over a different object world: meter reads and settlement cycles vs real-time network usage and service-path credit control |
| Payment Gateway / Payment Processing | different money layer | payment engines move money between parties; charging computes what consumption costs against a service entitlement before any money moves |

The most important boundary is with **billing**: the industry separates them consistently (charging engine vs billing system; rated event vs invoice; real-time balance vs settlement period), even when one vendor ships both in one suite. The second most important is with the **BSS chain**: the charging platform is a component with standalone market depth, not a small BSS — it has no orders, no catalog ownership, no care.

## Representative Products

- **Ericsson Charging** — the network vendor's convergent Online Charging System, positioned as "the real-time heart of all BSS"; carrier-grade lineage, Tier-1 operator deployments, cloud-native evolution.
- **Oracle Communications Elastic Charging Engine (with BRM)** — the component vendor's charging engine paired with its billing/revenue management core; the sampled product with publicly reachable operational documentation, and the clearest documented split between the charging engine and the billing/subscriber side.
- **Netcracker Convergent Charging System** — the mega-suite's charging component inside its Revenue Management suite; cloud-native, 3GPP-conformant, 5G/slice/API monetization focus, SaaS and edge-distributed deployment options.
- **Optiva Charging Engine (Qvantel)** — the standalone cloud-native converged charging engine, sold on its own or inside the Qvantel Flex Suite; serves operators from hundreds of thousands to hundreds of millions of subscribers, MVNO programs and digital brands; TM Forum ODA-listed component.
- **Amdocs Charging** — the incumbent suite's real-time charging component (alongside the acquired Matrixx charging line); documented here from the sibling Telecom BSS research pass.

## Sources

Research date: **2026-09-10**

- 3GPP TS 32.240 (Charging architecture and principles) — via ETSI deliverables: https://www.etsi.org/deliver/etsi_ts/132200_132299/132240/ (V17.11.0, V19.4.0); section texts: https://itecspec.com/3gpp/32.240/s/5.1 , https://whatthespec.net/friendlyspec/spec/32.240/19.4.0 ; spec page: https://www.3gpp.org/dynareport/32240.htm
- Ericsson — Charging product page: https://www.ericsson.com/en/portfolio/cloud-software-and-services/business-and-operations-support-systems/monetization/charging
- Oracle — Elastic Charging Engine documentation: Overview of Charging: https://docs.oracle.com/en/industries/communications/billing-revenue/15.2/concepts/overview-charging1.html ; Configuring Charging: https://docs.oracle.com/en/industries/communications/billing-revenue/15.1/charging/configuring-charging-elastic-charging-engine1.html ; Balance Queries: https://docs.oracle.com/en/industries/communications/billing-revenue/15.1/charging/configuring-balance-queries1.html ; Business Rules: https://docs.oracle.com/cd/E70765_01/doc.113/e70768/chr_business_rules.htm ; API appendix: https://docs.oracle.com/cd/E70765_01/doc.113/e70768/chr_apx_api.htm
- Netcracker — Convergent Charging System: https://www.netcracker.com/portfolio/solutions/monetization-and-customer-experience/netcracker-convergent-charging-system ; 5G Monetization: https://netcracker.com/portfolio/solutions/monetization-and-customer-experience/5g-monetization ; Revenue Management: https://www.netcracker.com/portfolio/products/digital-commerce-monetization/revenue-management ; Cloud OCS announcement: https://www.netcracker.com/news/press-releases/netcracker-unveils-cloud-ocs
- Optiva / Qvantel — TM Forum ODA directory entry: https://www.tmforum.org/oda/directory/software-providers/directory/optiva/products/optiva-charging-engine ; OCE brochure (GSMA-hosted): https://gsma.my.site.com/mwcoem/servlet/servlet.FileDownload?file=00PQt00001crOykMAE ; next-gen OCE release: https://www.optiva.com/press-releases/telecom-operators-empowered-by-ai-and-automation-with-next-generation-optiva-charging-engine ; 1Global case study: https://www.optiva.com/casestudy/optiva-charging-engine-on-google-cloud-transforms-1global's-business-inside-and-out ; Qvantel Flex Suite (OCE standalone): https://www.qvantel.com/qvantel-flex-suite
- Amdocs — Charging product page (evidence carried from the Telecom BSS research pass of the same date): https://www.amdocs.com/products-services/bss-oss/monetization/charging
- Market-definition corroboration — GlobalData revenue-management definition (hosted by Amdocs and Netcracker): https://www.amdocs.com/sites/default/files/2024-11/globaldata-rev-mgmt-competitive-assessment-amdocs-11-2024.pdf

> Sourcing limitation: Amdocs pages were unreachable (HTTP 403) on the research date; its evidence is carried from the same-day Telecom BSS pass and used only for structure and vocabulary. Ericsson, Netcracker, and Optiva publish product-page/brochure-tier material only; no operational user documentation is publicly reachable for them. Oracle's Elastic Charging Engine is the only sampled product with public operational documentation, and 3GPP TS 32.240 supplies the industry-standard semantics; operational specifics beyond what those sources state (session state machines, quota algorithms, tariff syntax, numeric limits) are intentionally not asserted in this document.

Detailed evidence, product-by-product observations, the cross-product comparison matrix, and the boundary analysis against Telecom BSS, billing, mediation, policy control, subscriber management, and utility metering/billing are recorded in the paired Research Notes.
