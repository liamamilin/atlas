# Research Notes — EV Charging Billing & Roaming

## Research Goal

Understand what the "EV Charging Billing & Roaming" Application Type actually is, from real products:

> What is the commercial machinery of public EV charging — how does a charging session become priced, billed, and settled money across the charging market's parties (drivers, charging-service providers, charge point operators, site hosts, roaming partners/hubs) — and where does this Type end and its neighbors begin?

## Initial Boundary

Working hypothesis before research:

- The Type is the **commercial layer** of EV charging networks: tariff-driven pricing of charging sessions, billing of the right party, and settlement/clearing between charging-market parties.
- "Roaming" = the inter-operator case: a driver of one charging-service provider charges on a charge point operator's network that is not their provider's; value must flow between the parties.
- Nearest neighbors: EV Charging Network Management (charger fleet operations — the sibling directory leaf), Utility Billing Platform, Payment Processing / Payment Gateway, Subscription Billing Platform, Telecom Charging/BSS (structural analogy of roaming), Mobility-as-a-Service.
- Main unknowns at start: exact object model (CDR, tariffs, tokens); whether pure roaming hubs (no driver billing) belong to the Type; how clearing/settlement is packaged; whether single-network-only billing belongs.

## Research Questions

1. What is the unit of record? (session? CDR? transaction?)
2. How does a session flow from plug-in to money: authorization → metering → pricing → billing → settlement?
3. What exactly is "roaming" operationally: bilateral vs hub; what is exchanged; what is clearing vs settlement?
4. What market roles exist (CPO, eMSP/EMP, hub, host, fleet, OEM) and who does the system serve?
5. What tariff/pricing structures do products actually expose?
6. What rules matter: authorization/entitlement, CDR validation, tax/currency, disputes, dunning/collections, fraud?
7. What interfaces do operators actually work in (consoles, portals, reports, APIs)?
8. Boundary: what distinguishes this Type from charger network management, utility billing, payment processing?

## Representative Products

Chosen for market representativeness + different product philosophies + different customer tiers:

| Product | Philosophy / pole | Customer tier |
|---|---|---|
| Driivz | EV charging & energy operations platform whose billing engine is a flagship module; CPO/eMSP enterprise | enterprise CPOs/eMSPs, OEMs, fuel retailers, utilities |
| Hubject | pure eRoaming network (intercharge) — the hub pole; B2B interoperability, Plug&Charge, financial services | CPOs, eMSPs, OEMs across 75+ countries |
| Gireve | European B2B platform: roaming intermediation + clearing (CDR→invoice→payment tracking) + data services | CPOs, eMSPs, public authorities |
| Last Mile Solutions | full-stack white-label backend (CPO + MSP): "Billing as a Service" + "Roaming as a Service" + payments | CPOs, MSPs, fleets, site owners, installers |

Rejected/alternative samples: AMPECO (white-label eMSP/CPO platform — **unreachable, all fetches failed; excluded**); pure payment-terminal vendors (skew to payment processing); charge point hardware vendor portals (weak docs).

## Sources

Research date: 2026-09-08. All observations below are from official vendor surfaces fetched live this date.

| # | Source | Type | Status |
|---|---|---|---|
| S1 | Driivz — "EV Charging Billing" product page + FAQ (`driivz.com/platform/ev-billing/`) | Tier 2 product page incl. FAQ | fetched |
| S2 | Driivz — blog "The Billing Challenges Behind a Seamless EV Charging Experience" (Anat Gat, product team lead) | Tier 3 official blog, operational detail | fetched |
| S3 | Hubject — homepage + "intercharge overview" (`hubject.com`, `/intercharge-overview`) | Tier 2 | fetched |
| S4 | Gireve — homepage, "EV Roaming Services", "Clearing Services" pages incl. webinar FAQ | Tier 2 + FAQ | fetched |
| S5 | Last Mile Solutions — homepage + "Billing as a Service" page incl. FAQ | Tier 2 + FAQ | fetched |
| S6 | OCPI spec (Open Charge Alliance, GitHub) | industry protocol spec | **unreachable — 2 timeouts, abandoned** |
| S7 | AMPECO — main site + docs | product docs | **unreachable — 3 transport errors, abandoned** |

Source-access limitation: no product's internal user-guide/help-center was reachable; evidence is page/FAQ level. Consequences: (a) no precise numeric limits, defaults, or step-level UI claims are made anywhere; (b) protocol-level object definitions (OCPI CDR/Tariff/Token fields) could not be verified and are described only at the conceptual level that the fetched vendor pages themselves support; (c) single-product findings are marked product-specific.

## Product A — Driivz

### Key observations (S1, S2 — evidence layer A)

- Platform framing: "smart cloud-based platform spans EV charging operations and network management, energy management tools, industry-specific billing and self-service solutions." Billing is a **module** next to Operations Management, Energy Management, driver app, Reporting.
- Billing engine positioning: "highly configurable billing engine enables EV charging network operators to scale and monetize their networks… Build tariffs, plans, and promotions to suit any driver."
- FAQ defines the domain: "EV charging billing is the process by which EV charging providers monetize their charging networks… pricing options… plans for EV charging based on factors like charging speed (kW), energy (per kWh), time (per minute), time of day… fixed charges like flat fees, transaction fees and parking fees. EV charging billing also encompasses how drivers pay… credit cards, debit cards, pre-payment, immediate payment, and monthly post payment."
- FAQ defines the solution: "manages all aspects of billing operations, including pricing, payment processing, invoicing, reporting and analytics, and settlement with multiple business partners such as hosts or service providers roaming on the network."
- Tariff parameters named: rating by kWh or time, static and dynamic cost factoring, time-of-use tariffs, flat/minimum/transaction fees, maximum charging allowance by time/energy/cost, parking fees, overtime penalties, reservations, coupons, membership plans, free-charging promotions.
- Invoices: findable "based on customer, status, date range"; "detailed cost breakdown by rate for any charging session"; white-labeled invoices issued directly from the platform to drivers and business partners, downloadable in app/portal.
- Payment control at session time: **incremental authorization** (repeated approvals as costs accumulate) and **partial pre-authorization** (small configurable minimum to start charging); out-of-the-box payment gateway integrations; country-specific pre-auth amounts as fraud control; RFID fraud controls (e.g., abnormal simultaneous-usage monitoring, RFID encryption).
- Multi-party settlement: "Billing reports detail each transaction, segmented per host or partner operator roaming on the network, enabling simple and accurate monthly settlement with all business partners"; "**Roaming hubs**: validate settlement reports from roaming hubs using transaction reports generated from CDRs which are all registered directly on the platform."
- CDR appears as the unit behind transaction reports for hub reconciliation.
- Fleet scenarios: depot / home / on-the-go; public sessions billed directly to fleet operator; home charging reimbursable "with full transparency for both the fleet and the driver". Fleet monthly billing cycles charging the company while the operator sees per-driver detail (S2).
- OEM no-pay plans: drivers charge "free" on the partner network for a period; the OEM is billed monthly post-paid for those sessions.
- Entitlement (S2): employees charging onsite at company expense ("Entitlement"); supermarket host coupons.
- Cross-border: "Charging sessions are billed according to the local currency and tax requirements of the charger's physical location, however, the driver receives an invoice with charges converted to their home currency." Multiple currencies, flexible tax management.
- Token assignment (S2): RFID tokens issued to drivers, "assign the right token ID in their back-office platform to each driver".
- S2 growth narrative: from one simple scenario (own chargers, one plan, app payment, invoice per session) → hosts with settlement contracts → subscriptions/promotions → time-of-use → fleets/entitlements → one-time-payment (OTP) premium plan for non-registered users → roaming agreements. Flat fees, minimum/maximum fees, overtime penalties, dunning, host contract minimum terms/early termination all named.
- Reporting: one-click reports for billing, payments, invoices, transactions, cost breakdown, VAT; revenue dashboard by geo-location, billing plans, etc.

## Product B — Hubject

### Key observations (S3 — evidence layer A)

- Positioning: "The world's largest international eRoaming network… Connecting Charge Point Operators, eMobility service providers and vehicle manufacturers to provide standardised access to charging infrastructure, across borders and across networks." Stats claimed: 1.1M+ charge points connected, 3,500+ B2B partners, 75+ countries.
- Market-structure framing: "The EV charging market consists of thousands of individual players… Without a common layer…" pain points: fragmented market, lack of interoperability, complex bilateral integrations, poor driver experience, **payment and settlement complexity**, security and trust.
- intercharge platform: "connects charge point operators and eMobility service providers through a single shared eRoaming network. One integration gives you access to the entire ecosystem."
- How it works (their own numbered steps): 01 Connect once (single integration, no multiple individual connections) → 02 Open your infrastructure to the network → 03 customers charge across networks ("eRoaming capabilities regardless of the operator") → 04 "**Authorisation and settlement, handled**: Every charging session is authorised and settled automatically between the relevant parties on the network."
- Key features: partner portal ("full control through the partner portal"), data-driven performance monitoring, "**Automated billing via Hubject Financial Services**: Billing between CPOs and eMSPs on the network is handled automatically through Hubject Financial Services, an additional service available to intercharge network partners", real-time transaction processing.
- Financial Services product line: "Settlement & Clearing via Hubject Financial Services — Simplify and automate compliant financial flows and billing between charging ecosystem partners."
- Other product lines beyond the Type's core: Plug&Charge ecosystem (automatic authorization without app/card), Testing & Certification, EVSE Data Score, Process Monitoring, Analytics, Consulting. Contact form enumerates market roles: CPO, EMP/eMSP, Backend Provider for CPO (CPMS), Backend Provider for EMP (CMS), Vehicle OEM, EVSE Manufacturer, etc.
- Note: no driver-facing billing on the hub itself; the hub's billing object is B2B (between CPOs and eMSPs).

## Product C — Gireve

### Key observations (S4 — evidence layer A)

- Positioning: "By combining market place technology, transaction processing and data management, Gireve is the first B2B digital platform for EV Charging." Stats claimed: 1M monthly transactions, 680,000 charging points connected, 13,000 agreements signed via Gireve.
- Roaming service: "EV charging roaming, contractualisation, billing between partners… services providers and charging network operators need to cooperate by signing contracts and exchanging real time." Gireve offers "a single technical connection, an access to the online marketplace that operates thousands of B2B contracts for e-mobility and a day-to-day operational support."
- Role definitions (their own words):
  - CPO: "in charge of physical charging points monitoring and maintenance, you define the network access conditions, you sign roaming agreements with eMSP and you take care of the management and invoicing for direct and roaming situations."
  - eMSP: "sending and supplying multi-network charging solutions to your EV driver subscribers, you are in charge of customer relationship and invoicing management."
- **Clearing Services** — the most explicit clearing description in the sample:
  - "Our automated tools take care of quality checks and charging price calculation as per CDR, generate B2B invoice, send it to concerned eMSPs and track the status of the payment."
  - Billing: "We handle the price calculation of your CDR with built-in quality checks and algorithms that calculate pricing and cross-check with the roaming agreement."
  - Invoicing: "Gireve generates B2B invoices for each CDR. You can then automatically send these invoices to respective eMSPs directly through the platform."
  - Payment: "track payment per invoice through a follow-up option that sends reminders… fully paid, partially paid or not paid."
  - Webinar FAQ: "Clearing services in EV charging cover key post-charging operations such as verifying Charging Data Records (CDRs), billing, invoicing, and reconciliation. These services ensure that all transactions between Charge Point Operators (CPOs) and eMSPs are accurate and settled efficiently." And: "Clearing services streamline these processes by automating… cross-checking CDR prices with tariff plans, managing disputes, and ensuring invoices are processed accurately and on time."
  - Trusted third party: "Gireve centralises the history of charging sessions and makes automatic calculation to help solve invoicing disputes."
- Operational portal: "Connect Place" (login-gated platform, named but not inspectable).
- Adjacent services beyond the Type's core: Plug & Charge PKI, data services (DaaS, analytics, compliance), consulting/training, "Advenir" (a French subsidy program service — product-specific).

## Product D — Last Mile Solutions

### Key observations (S5 — evidence layer A)

- Positioning: "Join Europe's leading platform for EV charging and energy transaction management"; "We are the backbone of the EV charging industry… 100% independent & secure — a neutral platform". Stats claimed: 364,000 charge points directly connected, 1.9M active charge cards managed, 210M charging transactions processed, 22 countries, since 2005.
- Service taxonomy (their menu): Commerce (Billing as a Service, Payment as a service, Branded environments, Roaming) / Management tools for CPO/MSP (Station management, Smart energy management, Hardware integration, Helpdesk) / Open APIs and data management.
- Billing as a Service: "Turn charging into revenue. Billing, collection, and payout – automated across all stakeholders." "Get paid for every kWh. Managing charge session revenue is complex. Multiple partners, currencies, and tax rules get in the way… automate everything from invoicing to VAT compliant payouts. End-to-end revenue handling for CPOs and MSPs."
  - Tariffs: "Set tariffs per user type, like employees, and guests. Add start, energy, duration & occupancy fees. Bulk management via charge groups. Full control of margins."
  - Billing: "Invoices based on all charge sessions. Support for subscriptions and service fees. Works for both business users and private customers. Invoicing fully handled on your behalf."
  - Tax: "Automated VAT handling in all regions. Supports multi-currency & exchange rates" (Europe focus; SEPA, CJEU named).
  - Collection & payout: "We handle all collections — including credit risk. Automated payouts to all stakeholders. Support for direct debit & invoice-based billing."
- FAQ (operational):
  - "Who manages payments from drivers and roaming partners — and what if they don't pay? … Our in-house credit management team handles the entire process — including reminders, collections, and even the financial risk. If a session is valid, you get paid."
  - Pricing: "highly flexible tariff engine. You can set detailed pricing rules based on time of day, energy consumption (€/kWh), session duration, grace periods, and even per customer group. Exceptions and custom margins per partner or contract are fully supported."
  - Stakeholder distribution: "As a CPO, you're managing more than just chargers — you're dealing with site owners, business clients, and energy providers, each with their own agreements and revenue shares… Our platform automatically calculates, splits, and distributes revenue to every stakeholder involved — fully transparent, contract-based, and audit-ready."
- Home reimbursement: "fully automated, scalable, and tax-compliant home reimbursement solution. We reimburse employees directly, on behalf of their employer… Also supports charge cards from other platforms."
- Payment unification: "Whether it's a fleet driver with an RFID card, a logistics worker using an app, or a private EV driver tapping a debit card – we unify every payment flow in one system. All transactions, regardless of payment method, are processed through a single, central flow… consistent reporting, and simplified settlement."
- CPO solution: "Turnkey backend to scale your charging network, automate financial settlement… across all hardware and roaming partners. …The industry's most complete Billing-as-a-Service." MSP solution: "White-label platform to manage roaming transactions, automate billing… Full tariff control across all CPOs… Roaming as a Service, available stand-alone."
- One-platform framing: "One platform to manage stations, drivers, roaming, and revenue flows." "Ensuring every charging session generates revenue requires a strong financial backbone."
- Use cases: public infrastructure, corporate fleet charging, fleet & depot, home reimbursement, hospitality & retail, installer.

## Cross-product Comparison

| Aspect | Driivz | Hubject | Gireve | Last Mile Solutions |
|---|---|---|---|---|
| Unit of record | CDRs "registered directly on the platform"; transaction reports per session | "every charging session is authorised and settled" on the network | CDR explicitly: quality checks, price calculation per CDR, B2B invoice per CDR | "invoices based on all charge sessions"; "every charging session generates revenue" |
| Tariff/pricing engine | kWh/min/kW rating, TOU, flat/min/transaction fees, parking, overtime, reservations, coupons, plans, promotions | provider tariffs exchanged across network (implied by settlement between parties) | price calculation per CDR cross-checked against the roaming agreement | start/energy/duration/occupancy fees, time-of-day, grace periods, per user type, per partner/contract margins, charge groups |
| Authorization/entitlement | token IDs assigned to drivers; incremental & partial pre-authorization | "every charging session is authorised" (hub + Plug&Charge line) | (driver identified via provider contract; not detailed on page) | charge cards (1.9M managed), app, debit card; tariffs per user type (employees/guests) |
| Who gets billed | drivers (immediate/monthly), fleets, OEMs (no-pay plans), OTP walk-ups | B2B: CPO ↔ eMSP (via Financial Services) | B2B: invoices per CDR sent to eMSPs | B2C and B2B; collections incl. credit risk; invoicing on behalf |
| Settlement/payout | monthly settlement with hosts & partner networks; validate hub settlement reports vs own CDRs | automated billing between CPOs and eMSPs on the network | payment tracking (fully/partially/unpaid), reminders, dispute solving | automated payouts to all stakeholders, contract-based revenue splits, audit-ready |
| Roaming packaging | roaming agreements + hub reconciliation | the product (single-integration network) | single connection + marketplace of thousands of B2B contracts | Roaming-as-a-Service (stand-alone available) |
| Tax/currency | charger-location currency/tax, driver invoice in home currency | not detailed on fetched pages | not detailed on fetched pages | VAT automation, multi-currency, exchange rates |
| Disputes/reconciliation | hub report validation vs platform CDRs | process monitoring (adjacent product) | CDR history centralised, automatic calculation to solve invoicing disputes | "if a session is valid, you get paid" (credit risk taken) |
| Adjacent (non-defining) modules | operations mgmt, energy mgmt, driver app, analytics | Plug&Charge, testing/certification, EVSE data, process monitoring | PnC PKI, data services, consulting, subsidy program service | station mgmt, smart charging, helpdesk, branded environments, CO₂ certificates |

### Cross-product commonalities (layer B)

1. **Session → priced record → money.** All four anchor on the individually recorded charging session (CDR named explicitly by Driivz and Gireve; "session" by Hubject and LMS) and exist to turn it into invoices and payouts.
2. **Tariff-driven pricing as a distinct engine.** All four expose tariff configuration decoupled from the session itself (rate components, per user type, time-of-day, margins).
3. **Multi-party money attribution.** All four name the party structure: driver, provider (eMSP), operator (CPO), site host/owner, roaming partners; all four produce settlement/payouts along that structure (host settlement, partner settlement, hub reconciliation, stakeholder payouts).
4. **Authorization precedes billing.** Sessions start with an identified driver entitlement (token/card/app; Hubject states authorization explicitly; Driivz manages token IDs; LMS manages charge cards).
5. **Roaming as the inter-operator structure.** Either as network membership (Hubject, Gireve), reconciliation against hub reports (Driivz), or a purchasable service (LMS). Bilateral "one-to-one agreements" are consistently framed as the pain the products remove.
6. **Billing operations machinery.** Invoice generation (B2C and B2B), payment tracking, reminders/collections, dispute handling with the CDR history as arbiter, reporting.
7. **Cross-border machinery** (tax/currency) present in the two products selling billing engines/full-stack (Driivz, LMS); not evidenced on the hub pages → hold as common-mature, not defining.

### Where the products differ (philosophy poles)

- **Billing-engine pole** (Driivz): the deep object is the tariff/plan; roaming is reconciliation against external hubs.
- **Hub pole** (Hubject): the deep object is the network of parties; authorization+settlement automation between them; no driver billing at all.
- **Clearing-house pole** (Gireve): the deep object is the CDR pipeline (check → price → invoice → payment track → dispute).
- **Full-stack BaaS pole** (LMS): everything above plus collections, credit risk, payouts, white-label; billing packaged as a service with station management as a sibling module.

## Canonical Model (Step 5 output)

Three jointly-held structures — remove any one and the Type stops being recognizable:

```text
Charging Session of Record (CDR)
  authorization/token → charge point → metered delivery → completed record
        ↓ priced by
Tariff-driven Session Pricing
  tariff components (energy / time / session / occupancy, time-of-day, per plan or agreement)
        ↓ attributed across
Multi-party Charging-market Settlement
  driver ↔ charging-service provider ↔ charge point operator ↔ site host / roaming partner or hub
  invoices + clearing + settlement/payouts close the loop
```

- **Session of record**: each charging event is an individually identified record bound to a charge point, an authorization identity, and metered energy/times; it terminates as a completed record (industry term: Charge Detail Record, CDR). Without it: charger telemetry (network management) or meter data without commercial identity.
- **Tariff-driven pricing**: a maintained tariff model is applied to the session's delivery to compute amounts. Without it: a session log with no commercial value (meter-data territory).
- **Multi-party settlement**: the session's value is attributed across the market's distinct commercial roles — the driver's charging-service provider and the charge point's operator, plus site hosts and roaming partners where present — and the system moves money along that structure (driver invoicing, B2B invoices between provider and operator, host/roaming settlement, payouts). Without it: card payment at a charger (payment processing) — a merchant transaction with no provider/operator structure; or a closed single-network loop with no settlement object — a degenerate form the products outgrow toward roaming.

Historical/market-sample check: early network-era charging backends (proprietary RFID/app billing of drivers on one operator's network, monthly statements, per-session records priced from tariffs) satisfy the three legs with no roaming hub, no OCPI, no cloud. Pure roaming hubs satisfy the legs at the B2B level (CDR exchange + tariff cross-check + inter-party settlement) without any driver billing. The definition therefore survives both the thin ancestor and the hub pole.

## Abstraction Levels

### L0 — Defining Invariant

1. The charging session of record (CDR) — identified per-session commercial record (point, authorization, metered delivery).
2. Tariff-driven session pricing — tariff model applied to the session to compute amounts.
3. Multi-party charging-market settlement — value attributed and moved across the provider/operator/host/roaming party structure (billing + clearing/settlement).

### L1 — Common Mature Structure

- driver contracts/entitlement plans (subscriptions, pre-pay, post-pay, promotions, coupons)
- charge token/card management (RFID cards, app identities, Plug&Charge credentials)
- payment gateway integration and payment controls (pre-authorization, incremental authorization)
- white-labeled invoicing (B2C and B2B) and billing reports
- settlement reporting and reconciliation (hosts, partner networks, hub reports)
- billing/revenue analytics and dashboards
- cross-border machinery: multi-currency, VAT/tax by charger location, home-currency invoicing
- roaming network participation (hub membership, roaming agreements, marketplace contracts)
- EVSE/location data exchange with partners (adjacent to roaming)
- fleet scenarios: depot/home/on-the-go billing, home-charging reimbursement, entitlements

### L2 — Variant / Optional

- business-model pole: standalone billing engine vs roaming hub/clearing house vs full-stack BaaS vs suite module (billing as one module of a charging management platform)
- payment terminal / card-present ad-hoc charging (walk-up OTP pricing, premium rates)
- credit risk & collections as an outsourced service (dunning, reminders)
- EVSE data quality and process monitoring services
- Plug&Charge credential ecosystems and testing/certification services
- subsidy/program services (e.g., named French subsidy program administered via a roaming platform — product-specific)
- CO₂ certificate monetization of sessions (product-specific)
- V2G / smart-charging energy services riding the same session record
- regional regulatory packaging (payment terminals, VAT regimes) — region-dependent

### L3 — Vendor-specific (research notes only)

- Driivz: plan/promotion parameter catalog ("most extensive list of billing parameters"), incremental/partial pre-authorization naming, "First Time Right" program, OEM no-pay plan packaging, Recharge CEO quote on roaming reconciliations.
- Hubject: intercharge network stats (1.1M+ charge points, 3,500+ partners, 75+ countries, 250+ new partners/year), EVSE Data Score, Plug&Charge Confidence Score, truck-reservation whitepaper line, Hubject Financial Services as separate entity line.
- Gireve: Connect Place portal name, "Advenir" subsidy service, roaming barometer publications, "13,000 agreements signed" stat.
- Last Mile Solutions: evc-net status page, Alliance program, migration services, eRE CO₂ certificate offering, "by Threeforce" footer, 2005 founding stat, 210M transactions stat.

## Vendor-specific Findings

See L3. None of these enter the canonical core; several (pre-authorization styles, network stats, subsidy services) are packaging or scale claims.

## Boundary Findings

- **vs EV Charging Network Management** (sibling leaf): network management = charger fleet operations — monitoring, OCPP-class connectivity, remote configuration, smart charging, maintenance (Driivz "Operations Management", LMS "Station management" modules are exactly this). This Type = the commercial layer. Test: remove billing/roaming from any sampled product → what remains is charger network management; remove the charger operations from it → what remains is billing/roaming machinery (the pure hub pole is proof of concept: Hubject/Gireve carry no charger operations at all). Market packaging bundles both in "charging management platforms", which is why the two leaves must be kept distinct as modules of one product family.
- **vs Utility Billing Platform**: utility billing bills recurring service per customer account from meter readings; here the unit is the per-session CDR, priced from charging tariffs, and the counterparty structure spans multiple independent companies (provider ≠ operator ≠ host). Utilities appear as customers of this Type (Driivz sector page) but utility billing machinery is a different Type.
- **vs Payment Processing Platform / Payment Gateway**: payment at the charger (card terminal, pre-auth, gateway) is one input machinery. The defining structure here is the session→CDR→tariff→settlement loop across parties; card-present payment with no provider/operator settlement structure is payment-processing territory. Sampled products integrate gateways rather than being gateways.
- **vs Subscription Billing Platform**: subscriptions/plans are one billing input (entitlements and recurring fees); the unit of record here remains the session CDR.
- **vs Telecom Charging Platform / Telecom BSS**: structural analogy (roaming, clearing, settlement between operators) but different domain objects and protocols (charging sessions/kWh vs calls/minutes); no evidence of shared product lineage.
- **vs Mobility-as-a-Service Platform**: MaaS is consumer-facing multi-modal trip aggregation; this Type is B2B revenue infrastructure for charging. eMSP drivers are the consumers touched (app/invoices), but the operator of the system is a charging-market party, not a traveler.
- **"What to remove to leave the Type"** test: remove tariff pricing → meter-data/network telemetry; remove settlement structure → point-of-sale payments; remove the CDR → tariff catalog + payments with no session anchor (not this Type).

## Uncertainties

1. **AMPECO and OCPI spec unreachable** — the eMSP-side platform pole and the protocol object model are evidenced only via the four fetched vendors' own pages. Driver-side invoicing details (e.g., per-session vs aggregated invoices, real-time price display) are inferred from FAQ-level statements, not step-level docs.
2. **Authorization mechanics inside the Type vs inside network management**: all sampled products state authorization exists; whether the authorization engine lives in the billing/roaming product or in the CSMS is packaging-dependent — held as common-mature structure, not defining.
3. **Clearing vs settlement terminology**: Gireve uses "clearing" for CDR→invoice→payment-tracking; Hubject uses "settlement & clearing" for inter-party billing; Driivz calls it "monthly settlement". The industry does not use one canonical term — final document keeps both words, conceptually defined.
4. **Pure-hub pricing detail**: how hubs compute their own fees (roaming fees, commissions) is not documented on fetched pages — do not assert.
5. **Regional depth**: Europe-heavy sample (3/4 products). North American pole reached only via Driivz. Time-of-use/tax machinery is described in general terms; country-specific rules not asserted.

## Final Synthesis

EV Charging Billing & Roaming is the commercial system of record for EV charging sessions. Its defining core is three jointly-held structures: (1) the charging session of record — each session captured as an individually identified record (charge point, authorization identity, metered delivery) terminating as a priced commercial record (CDR); (2) tariff-driven session pricing — maintained tariff models (energy/time/session components, time-of-day, per user type or roaming agreement) applied to the session to compute the amounts; (3) multi-party charging-market settlement — the session's value attributed and moved across the market's distinct commercial parties (driver's charging-service provider, charge point operator, site hosts, roaming partners/hubs), through driver invoicing, B2B invoices between provider and operator, clearing/validation of CDRs against agreements, settlement and payouts, with disputes resolved against the retained session record.

The Type spans a product spectrum — billing engines for operators, roaming hubs/clearing houses between them, and full-stack white-label backends — all anchored on the same three structures. Roaming is not an add-on feature but the multi-party case of the settlement structure: when driver's provider and point operator differ, the same session record is priced under the governing agreement and cleared between the parties.

Historical check passes: single-network session billing (no hub) and pure clearing (no driver billing) both satisfy the core; no modern-specific capability (cloud, OCPI-class protocols, payment terminals, Plug&Charge, VAT automation) is required by the definition.
