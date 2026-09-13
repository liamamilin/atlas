# Research Notes — Telecom Charging Platform

Research date: 2026-09-10

## Research Goal

Understand what "Telecom Charging Platform" is as an Application Type: what the operator-side charging system actually computes and controls, how the industry itself (3GPP standards, vendor taxonomies) defines charging vs billing vs mediation vs policy control, what objects and flows a charging platform is built around, how suite components, standalone engines, and network-vendor products differ, and where its boundary lies against Telecom BSS (the sibling suite pass), billing, mediation, policy control, subscriber management, product catalog, and utility metering/billing.

Pre-hung seams from sibling passes (to honor):

- From telecom-bss (2026-09-10): "telecom-charging-platform = rating/balance computation vs the chain resolving into it"; and "CRM-first BSS entrants cover the chain's front natively and integrate charging/billing engines — engine ownership is implementation, not definition, and the telecom-charging-platform pass should not treat CRM-first integration as absence of the money side."
- From subscriber-management (2026-09-10): "telecom-charging-platform / subscription-billing seam = money computation vs who-has-what-and-is-active (status gates billing, services feed invoices)."

## Initial Boundary

- Directory context: §19 Energy, Utilities & Telecommunications, inside the telecom BSS neighborhood (Telecom BSS, Telecom OSS, Telecom Order Management, Telecom Charging Platform, Telecom Product Catalog, Subscriber Management, Telecom Revenue Assurance, SIM/eSIM Management, Telecom Number Management, Telecom Provisioning Platform).
- Working hypothesis going in: the charging platform is the operator's money-computation system — it rates service consumption against commercial terms, maintains subscriber balances, and controls service delivery in real time (the OCS/convergent-charging lineage). It is a BSS component with its own market depth (standalone engines exist).
- Known ambiguities going in: (A) "charging" spans online (real-time credit control) and offline (post-event rating) in the standards — where is the Type's center? (B) charging vs billing vs revenue-management naming varies by vendor; (C) some products bundle policy control; (D) 5G/slice/API charging is era-current vocabulary layered on an old core.

## Research Questions

1. What does a charging platform actually compute — what is its unit of work?
2. What money-side state does it hold (balances, buckets, allowances, reservations)?
3. How does it interact with the network/service path in real time (credit control, quota, re-authorization)?
4. How do online vs offline vs convergent charging relate, and which is definitional?
5. What comes in (usage events, offers/tariffs, subscriber state) and what goes out (charges, rated events, balance states)?
6. How do suite components (Ericsson, Netcracker, Amdocs), standalone engines (Optiva), and component vendors with public docs (Oracle) differ in philosophy and coverage?
7. Where exactly are the seams: vs billing, vs mediation, vs policy control, vs subscriber management, vs product catalog, vs the BSS chain?
8. What is variant vs definitional: convergence (prepaid+postpaid), multi-service, 5G/slice/API charging, cloud/SaaS, policy bundling, partner revenue sharing?

## Representative Products

Selected for market representativeness + documentation reachability + different product philosophies + different customer tiers:

- **Ericsson Charging** — network vendor's convergent Online Charging System; "the real-time heart of all BSS"; carrier-grade lineage (Ericsson Charging System), Tier-1 operator focus. (Pole: network-vendor OCS, carrier-grade.)
- **Oracle Communications Elastic Charging Engine (ECE) + BRM** — component vendor; the only sampled product with publicly reachable operational documentation (docs.oracle.com implementation/concept guides). (Pole: component stack with public Tier-1 docs; ECE = charging engine, BRM = billing/subscriber side.)
- **Netcracker Convergent Charging System (CCS)** — mega-suite component inside Revenue Management; cloud-native, 3GPP-conformant, 5G/slice/API monetization focus, SaaS offering. (Pole: suite component, cloud-native/SaaS, 5G-era framing.)
- **Optiva Charging Engine (OCE, now under Qvantel)** — standalone cloud-native converged charging engine, sold on its own or inside Qvantel Flex Suite; MVNO/digital-brand/SaaS pole; TM Forum ODA-listed component. (Pole: best-of-breed standalone engine.)
- **Amdocs Charging** — incumbent suite's charging component (incl. acquired Matrixx Charging); direct fetch blocked (403) on research date; evidence carried from the telecom-bss pass (2026-09-10) which captured the product page quotes. (Pole: incumbent suite component.)

Corroborating industry sources: 3GPP TS 32.240 (charging architecture and principles — the authoritative standard for online/offline/converged charging, OCS/OFCS/CCS), GlobalData revenue-management market definition (hosted by Amdocs and Netcracker), TM Forum ODA component directory.

## Sources

- 3GPP/ETSI TS 132 240 (Charging architecture and principles) — ETSI deliverable pages and full-text excerpts: https://www.etsi.org/deliver/etsi_ts/132200_132299/132240/ (directory); V17.11.0 PDF: https://www.etsi.org/deliver/etsi_ts/132200_132299/132240/17.11.00_60/ts_132240v171100p.pdf ; V19.4.0 PDF: https://www.etsi.org/deliver/etsi_TS/132200_132299/132240/19.04.00_60/ts_132240v190400p.pdf ; section texts via iTecSpec (https://itecspec.com/3gpp/32.240/s/5.1) and FriendlySpec (https://whatthespec.net/friendlyspec/spec/32.240/19.4.0); 3GPP spec page: https://www.3gpp.org/dynareport/32240.htm
- Ericsson — Charging product page: https://www.ericsson.com/en/portfolio/cloud-software-and-services/business-and-operations-support-systems/monetization/charging (fetched in full 2026-09-10)
- Oracle — ECE concept/implementation guides (fetched via search excerpts of docs.oracle.com pages, 2026-09-10): Overview of Charging: https://docs.oracle.com/en/industries/communications/billing-revenue/15.2/concepts/overview-charging1.html ; About Configuring Charging in ECE: https://docs.oracle.com/en/industries/communications/billing-revenue/15.1/charging/configuring-charging-elastic-charging-engine1.html ; Configuring Balance Queries: https://docs.oracle.com/en/industries/communications/billing-revenue/15.1/charging/configuring-balance-queries1.html ; Configuring Business Rules for Charging: https://docs.oracle.com/cd/E70765_01/doc.113/e70768/chr_business_rules.htm ; ECE API appendix: https://docs.oracle.com/cd/E70765_01/doc.113/e70768/chr_apx_api.htm ; ECE Implementing Charging (PDF): https://docs.oracle.com/en/industries/communications/billing-revenue/15.0/charging/ece-implementing-charging.pdf
- Netcracker — Convergent Charging System page (fetched in full): https://www.netcracker.com/portfolio/solutions/monetization-and-customer-experience/netcracker-convergent-charging-system ; 5G Monetization: https://netcracker.com/portfolio/solutions/monetization-and-customer-experience/5g-monetization ; Revenue Management: https://www.netcracker.com/portfolio/products/digital-commerce-monetization/revenue-management ; Cloud OCS press release: https://www.netcracker.com/news/press-releases/netcracker-unveils-cloud-ocs ; GlobalData Digital BSS definition (Netcracker-hosted PDF): https://pages.netcracker.com/rs/937-BYM-547/images/GlobalData_Netcracker_Digital%20BSS_FINAL.pdf
- Optiva / Qvantel — TM Forum ODA Component Directory entry: https://www.tmforum.org/oda/directory/software-providers/directory/optiva/products/optiva-charging-engine ; GSMA-hosted OCE brochure: https://gsma.my.site.com/mwcoem/servlet/servlet.FileDownload?file=00PQt00001crOykMAE ; MWC exhibitor listing: https://www.mwcbarcelona.com/exhibitors/29865-optiva/products/3884-optiva-charging-engine-oce ; next-gen OCE press release: https://www.optiva.com/press-releases/telecom-operators-empowered-by-ai-and-automation-with-next-generation-optiva-charging-engine ; Google Cloud Marketplace press release: https://www.optiva.com/press-releases/optiva-launches-first-5g-telecom-charging-solution-transacted-through-google-cloud-marketplace,-signals-advancement-in-telecom-software-market ; 1Global case study: https://www.optiva.com/casestudy/optiva-charging-engine-on-google-cloud-transforms-1global's-business-inside-and-out ; Qvantel Flex Suite page (fetched in full; optiva.com/optiva-charging-engine-2/ now redirects here): https://www.qvantel.com/qvantel-flex-suite ; Optiva BSS Platform brochure: https://www.optiva.com/_files/ugd/6875ca_597a6eadb8c146838c920d9868b8ac69.pdf
- Amdocs — Charging product page and datasheet (both returned HTTP 403 on 2026-09-10; quotes carried from the telecom-bss pass of the same date, which fetched them successfully): https://www.amdocs.com/products-services/bss-oss/monetization/charging ; https://www.amdocs.com/sites/default/files/2024-12/Amdocs-charging-datasheet-12-2024.pdf ; GlobalData revenue-management definition hosted by Amdocs: https://www.amdocs.com/sites/default/files/2024-11/globaldata-rev-mgmt-competitive-assessment-amdocs-11-2024.pdf

Source-access limitations: Amdocs pages were unreachable (403) on this pass; its evidence is carried over from the sibling telecom-bss pass (same date, Layer A quotes) and is used only for structure/vocabulary. Ericsson, Netcracker, and Optiva evidence is product-page/brochure/press tier (Tier 2); none publishes operational user documentation at public URLs. Oracle ECE is the only sampled product with public operational documentation (Tier 1). 3GPP TS 32.240 provides the authoritative industry-standard semantics (Tier 1 for the domain's concepts, not for any product's behavior). Precise product internals beyond what Oracle/3GPP documents state are deliberately not asserted.

---

## Product A — Ericsson Charging

### Key observations (Layer A)

- Self-definition: "a modular, scalable, open, single convergent Online Charging System (OCS) using industry standards and protocols"; "an evolution of the industry-leading Ericsson Charging System"; covers "traditional telecom services as well as digital services, 5G and IoT."
- Positioning inside BSS: "It is the real-time heart of all BSS: a scalable, flexible solution... enabling real-time convergent charging, policy control, decoupling and fast service creation."
- Credit/control split: "It lets the operator control credit while letting users control their costs through flexible packaging, bonuses and discounts."
- Pre-integration list (the platform's neighborhood): "Pre-integrated with CRM, mediation, provisioning, self-care, policy, catalog, and traffic management."
- Key features: "Real-time convergent charging... centralized service creation and rule management for policy control and user self-service... spending control for consumers, and credit risk and multiple-partner revenue sharing management for you"; "Full mobile broadband charging functionality... charge for speed, bandwidth, or service. Send real-time customer alerts and notifications to enable spending control"; "Fully configurable tariff system. Develop unique, personalized, differentiating service bundles combining data, voice, fixed and mobile for all customer segments, using yield management functionality."
- Scale claim: "more than 184 implementations managing more than 2.3 billion end users worldwide" (vendor claim, not independently verified).
- End-user visibility: "Let subscribers request and update account information and remain informed about costs, balances, and bonuses in real time. Eliminate 'bill shocks' and, with end-user notifications, create strong up-sell opportunities."
- Convergence framing: "Maintain one convergent system for all services, all networks, and all payment methods."
- Deployment: "cloud-ready and cloud-enabled"; press releases show cloud-native charging deployments (Vi postpaid modernization, Ooredoo Oman charging upgrade).
- From the sibling BSS pass (same vendor, monetization page): "charging or billing based on any identifier – device, user, slice, API, or partner."

## Product B — Oracle Communications Elastic Charging Engine (ECE) + BRM

### Key observations (Layer A — public operational documentation)

- The two charging modes, verbatim: "Online Charging: Real-time rating of events during a session, such as in prepaid calls." / "Offline Charging: Batch rating of events, typically for post-paid telephone usage."
- The rating input: "ECE receives usage requests containing event data required for rating. For instance, to rate a phone call, ECE needs the calling number and the start and end times. Upon receiving a usage request, ECE identifies the customer and their associated charge offer for rating the event."
- Rating measurement model: "you configure ratable usage metrics (RUMs), which specify the units to measure and how to calculate the measurement"; "some events are rated by measuring duration, and some by measuring volume"; event definitions "specify the data needed for charging the event... stored in an ECE cache."
- Offer-driven rating: "After a customer purchases a package, they own the charge offers that they purchased. ECE uses the charges defined in each customer's offers to determine how much to charge. If a customer changes their offers, their usage is rated according to the charges defined in the new offers." Offers are tracked in BRM "and synchronized in ECE."
- Balance model: "Balances are organized by different types of balance elements... Balance elements are specified when you configure pricing in a charge. They define which balance assets are increased or decreased when the charge is used to rate an event. For example, a charge of one dollar per minute for a phone call affects the U.S. dollars balance." Balances can be "either currency or non-currency, depending on the type of resource the transaction impacts."
- Dual-ledger flow: "After an event is rated, ECE sends the rated event data to the BRM database, and the customer's balance is updated in both ECE and in the BRM database. The same process is used for loading online charging events and offline charging events."
- Prepaid session management (the credit-control loop, verbatim structure): "When a subscriber initiates a prepaid call, the network sends authentication and authorization requests to ECE, which processes them immediately to establish the call. While the session is in progress, ECE tracks the subscriber's balance to ensure that it is sufficient to pay for the call." ECE: (1) authenticates (telco ID "typically the MSID"; broadband "a login name and password"); (2) authorizes — "Credit limit checking... Service status checking. Confirms that the requested service is active in the customer's account. Duplicate session checking"; (3) "Reserves a balance amount for the session. For example, customers can be authorized to download 100 bytes of data or to make a 30-minute telephone call"; if balance insufficient, "ECE calculates the maximum authorization based on the customer's credit limits."
- Reservation mechanics: "ECE sends the validity time for the active reservation or reservation validity to the network mediation client. Reservation validity specifies how long a session can continue before the client must ask for a reauthorization"; "When a prepaid session is authorized, BRM reserves a portion of the customer's balance for the event. This prevents customers from using that balance amount for other services while the session is in progress"; "When the session ends, ECE... returns any unused reserved balance amounts to the customer's balance."
- Server-initiated re-authorization: "Alerts the network that a change that requires reauthorization occurs in a subscriber's account... This is called server-initiation reauthorization." (RAR-class behavior; dynamic quota management and "Triggering RAR Notifications for Ongoing Sessions" appear in the implementation guide TOC.)
- Policy coupling: "If the session uses policy-driven charging, it tracks the balance thresholds that trigger credit-limit notifications to the policy controller. Both in-session and out-of-session notifications are supported"; "you can automatically increase a customer's quality of service when their balance reaches a specified amount. This is known as policy-driven charging."
- Non-usage charges flow through the same record: "An event can also be system-generated, such as monthly subscription fees that are applied to accounts."
- Online scope beyond voice: "online charging can be used for any service that the subscriber connects to and uses in real time, such as broadband access, digital content, streaming radio, and cable television."
- Upstream mediation: "ECE is preintegrated with Oracle Communications Offline Mediation Controller"; for offline, "Call Detail Records (CDRs) are processed by Oracle Communications Offline Mediation Controller, which acts as an ECE client application... performs mediation and normalization tasks, such as checking for duplicate calls and assembling calls that arrive in multiple records. Offline Mediation Controller creates usage requests for ECE to rate the events."
- Downstream: rated events are sent to the BRM database (Rated Event Loader) — the billing side consumes them.
- External client APIs: "Use the Balance API to query balances for one or more subscribers... so they can monitor their network-usage expenses, validate their credit limit, or monitor their active reservation"; "You use the ECE API to integrate ECE with third-party clients, such as top-up systems" (Top-Up API); balance query modes (SUMMARY/DETAILED/ALL/TURBO) return balance elements, credit limits, grantor info, reservation state, rollover info.
- Configurable business rules: systemwide initial/incremental reservation quotas per product-RUM combination, minimum authorization quantities, advice of promotion, rounding rules, consumption rules across balance validity groups, redirecting a subscriber session, midsession rated events.
- Rating depth: linear and non-linear rating; customizing rating; reverse rating on multiple RUMs.

## Product C — Netcracker Convergent Charging System (CCS)

### Key observations (Layer A, product page tier)

- Positioning: "plays a key role in a modern CSP business support environment... The convergent charging engine, an integral part of our Revenue Management suite, which supports complex, end-to-end usage-to-payment business processes, can quickly adapt to any new service, business model or use case and support complex real-time pricing based on any attributes."
- Agnosticism: "uses an agnostic approach for network technology, telecom and non-telecom products, customer types, business models and any line of business with a single convergent platform."
- Standards conformance: "a cloud-native, high-performance and dynamically scalable real-time charging platform that fully conforms to 3GPP architecture."
- 5G monetization: "dynamic slice-based charging scenarios and complex cross-slice charging models, including slice-as-a-service, 5G as-a-service... performs complex charging based on a wide range of slice-related parameters (i.e. latency, throughput, mobility, coverage area, activation, deactivation etc.), taking into consideration analytical data about current network performance"; "supports charging for API call invocation."
- Convergence: "multidimensional convergence... advanced flexibility in how prices are calculated for any charge type, including both usage-based and non-usage based, for any customer type and network technology"; "supports both traditional telco services such as voice, messaging and data, and emerging digital services including XaaS, IoT and 5G-enabled offerings."
- Partner economics: "supports complex multi-partner revenue-sharing models and cross-industry business scenarios for telcos and non-telco verticals (utility, finance, logistics, entertainment, automotive, agriculture smart city, etc.)."
- Distributed architecture (names the platform's internal functions): "latency-critical functions, such as online session management and real-time service quotation, in the edge cloud... Other CCS functions, such as centralized balance management, charging management and unified data storage, are located in a public or telco cloud. Both parts are synchronized in real time to ensure consistency of customer account structures, balances, tariff plans, service charges and other customer-related information."
- Deployment/SaaS: "can be offered in a SaaS model"; "runs on any Kubernetes-compatible cloud (private, public, hybrid)."
- Generational coexistence (5G Monetization page): "uses a 3GPP-compliant converged charging system (CCS) to support 5G and an online charging system (OCS) to support 4G and previous generations of mobile networks. This allows support for complex 4G/5G switchover charging scenarios and hybrid services for the same account."
- Suite context (Revenue Management page): "automates critical business processes, including source-agnostic usage data management, convergent charging and billing, interactive bill design and accelerated debt collection"; component inventory includes "Active Mediation, Converged Charging and Billing, Customer Billing Management, Collections Management, Voucher Management, Online Charging System, Partner Billing Management, Bill Presentment."
- Cloud OCS press release: "centralizes storage for all rating, charging, subscriber and policy information onto a single product"; "catalog-driven configurations."

## Product D — Optiva Charging Engine (OCE, Qvantel)

### Key observations (Layer A, vendor + TM Forum directory tier)

- TM Forum ODA Component Directory: "Optiva's highly scalable, convergent charging solution is a fully cloud-enabled platform for private and public cloud... enables operators to launch and monetize their 4G and 5G networks and any other line of business to deliver advanced monetization services, including Voice over LTE/VoNR, fixed line, broadband, TV, machine to machine, IoT, cloud services, and OTT offerings."
- GSMA brochure: "5G ready, real-time, converged, cloud-native charging solution"; "Fully converged charging for telecom and beyond"; "Embedded rating and policy control function"; "Real-time multi-play charging backed by a universal data model to charge any attribute (SLA, bandwidth), any charging model (subscriptions, bundles, hierarchies), and any business type (mobile, TV, IoT, fixed, etc.)."
- Scale span: "Whether your customer base is 500K or 500M" (MWC listing); "any-play, real-time charging solution... to accelerate 5G monetization from connectivity and Beyond towards B2B2x and partner ecosystem."
- Standalone vs suite (Qvantel page, fetched in full): "Qvantel provides the Optiva Charging Engine on a stand-alone basis and also as part of the Qvantel Flex Suite. Optiva Charging Engine is used by many leading CSPs and supports all services (mobile, fixed, digital services and IoT) for all customers (B2C, B2B, B2B2X)"; "Monetization suite: Our real-time charging engine can be implemented on a stand-alone basis... allowing them to monetize anything and everything"; "launch new products in hours" (vendor claim).
- OCS identity in deployment (1Global case study): "We needed our online charging system (OCS) to be agile and robust"; "1Global's on-premise online charging system (OCS), along with testing and disaster recovery systems, was replaced with one OCS on Google Cloud. Optiva delivered Optiva Charging Engine, a real-time converged charging solution that is 5G ready and updated every 3-6 months through a CI/CD pipeline."
- SaaS/MVNO pole (Google Cloud Marketplace press release): "Full SaaS public cloud converged charging solution will also enable CSPs to fast-track the launch of new mobile virtual network operator (MVNO) businesses."
- Billing-model breadth (Optiva BSS Platform brochure): "Online Rating & Charging: Real-time online rating, charging, and billing that support multiple billing models out-of-the-box, such as up-front fees, one-time fees, subscriptions, usage-based, recurring, and more."
- Integration: "TM Forum API 620 and 637 for product and bundle data" (press release); "Personalization of products during real-time usage of services" (AI-era layer).

## Product E — Amdocs Charging

### Key observations (Layer A quotes carried from the telecom-bss pass, 2026-09-10; direct fetch blocked this pass)

- Product page (as captured 2026-09-10): "A real-time charging system enables telecom providers to rate, charge, and manage service usage instantly. It gives operators immediate control over network services, customer balances, and revenue streams."
- Component inventory (as captured): Charging and Matrixx Charging (acquired pure-play convergent charging vendor) both listed under Monetization; Policy is a separate Amdocs product; Real-Time Billing / Freestyle Billing are separate billing components.
- Market definition hosted by Amdocs (GlobalData): "The revenue management market consists of business support system (BSS) offerings primarily related to mediation, converged rating and charging, online charging systems (OCS), customer billing management, partner billing management, collections management, bill presentment, voucher management, policy control and charging" — charging sits inside a "revenue management" market frame that also contains billing, mediation, collections, vouchers, policy.

## Corroborating industry source — 3GPP TS 32.240 (Layer A, the standard)

Verbatim definitions (TS 32.240, terms & definitions clause):

- "offline charging: charging mechanism where charging information does not affect, in real-time, the service rendered."
- "Offline Charging System: the entity that collects and processes offline charging information prior to delivery to the Billing Domain."
- "online charging: charging mechanism where charging information can affect, in real-time, the service rendered and therefore a direct interaction of the charging mechanism with bearer/session/service control is required."
- "Online Charging System: the entity that performs quota management. Its functionality includes transaction handling, rating, online correlation and management of subscriber accounts/balances."
- "Converged Charging System: the system that combines the functionalities of the Offline Charging System and the Online Charging System into a single converged system."

Architecture and principles:

- "In offline charging, the resource usage is reported from the network to the BD after the resource usage has occurred. In online charging, a subscriber account, located in an OCS or CCS, is queried prior to granting permission to use the requested network resource(s)."
- "authorization for the network resource usage must be obtained by the network prior to the actual resource usage to occur. This authorization is granted by the OCS or CCS upon request from the network... The resource usage authorization may be limited in its scope (e.g. volume of data or duration), therefore the authorization may have to be renewed from time to time as long as the user's network resource usage persists."
- Session-based charging with unit reservation: "the OCS reserves credit from the subscriber account and returns the corresponding quota (e.g. units specifying the number of minutes or bytes allowed) to the NE. The NE, in turn, uses the provided quota to supervise the actual network resource consumption... When the quota is used up, the network element either issues another interim charging event, requesting further units to be allotted, or terminates the session if previously instructed to do so by the OCS. Once the session is terminated... the OCS returns the value of any unused quota... to the subscriber's account."
- Rejection: "If the chargeable event is not authorised by the OCS (e.g. when the subscriber account does not contain sufficient credit), the NE rejects the resource usage pertaining to that chargeable event."
- Rating Function (RF): "determines the value of the network resource usage... receives in return the rating output (monetary or non-monetary units)."
- Account Balance Management Function (ABMF) is a named OCS/CCS function; CTF (Charging Trigger Function) lives in network elements; CDF/CGF produce and transfer CDRs; the Billing Domain (BD) post-processes CDRs "e.g. for the purpose of generating bills."
- Event-based vs session-based charging are the two classes; charging levels span domain/subsystem/service.
- Converged charging: "online and offline charging are combined... offers charging with and without quota management, as well as charging information record generation."
- The standard explicitly scopes itself: "All other aspects of the OCS and CCS are outside the scope of 3GPP" — the standard defines the network-facing semantics; the product around them is vendor territory.

---

## Cross-product Comparison

| Dimension | Ericsson Charging | Oracle ECE (+BRM) | Netcracker CCS | Optiva OCE (Qvantel) | Amdocs Charging |
|---|---|---|---|---|---|
| Self-description | "single convergent Online Charging System (OCS)" | charging engine for online + offline charging, paired with BRM billing | "Convergent Charging System... fully conforms to 3GPP architecture" | "convergent charging solution"; deployed as "one OCS" | "real-time charging system" |
| Positioning | "the real-time heart of all BSS" | component in Oracle Communications monetization stack | "integral part of our Revenue Management suite" | standalone engine or Flex Suite component | suite component (Monetization) |
| Rating | "fully configurable tariff system"; charge for "speed, bandwidth, or service" | usage requests → charge offers → rated events; RUMs; linear/non-linear | "real-time pricing based on any attributes"; usage- and non-usage-based | "universal data model to charge any attribute (SLA, bandwidth)" | "rate, charge, and manage service usage instantly" |
| Balances | "customer balances"; users informed about "costs, balances, and bonuses in real time" | balance elements (currency/non-currency); updated in ECE and BRM; reservations | "centralized balance management"; "customer account structures, balances, tariff plans" synchronized | charging models: "subscriptions, bundles, hierarchies" | "customer balances" |
| Real-time service-path role | "control credit"; spending control; real-time alerts | prepaid session loop: authenticate → authorize → reserve → reauthorize → settle | "online session management" as latency-critical edge function; real-time service quotation | "real-time" in every description; OCS deployments | "immediate control over network services" |
| Offline rating | convergent (single system) | explicit: "Offline Charging: Batch rating of events, typically for post-paid" | convergent; OCS for 4G + CCS for 5G coexistence | convergent | convergent |
| Non-usage charges | bundles/bonuses (packaging) | "system-generated, such as monthly subscription fees" | "both usage-based and non-usage based" | "up-front fees, one-time fees, subscriptions, usage-based, recurring" | (not captured) |
| Policy coupling | "policy control" named; pre-integrated with policy | "policy-driven charging"; balance thresholds notify policy controller | policy info centralized in the product (Cloud OCS PR) | "embedded rating and policy control function" | Policy is a separate Amdocs product |
| Partner economics | "multiple-partner revenue sharing management" | (not captured) | "multi-partner revenue-sharing models" | "B2B2x and partner ecosystem" | (not captured) |
| Upstream/downstream | pre-integrated with "CRM, mediation, provisioning, self-care, policy, catalog" | Offline Mediation Controller upstream; BRM database downstream | Active Mediation + billing in the same suite | TM Forum product APIs; suite integration | suite pre-integration |
| Recharge/top-up | "bonuses"; self-service account updates | Top-Up API for third-party clients | Voucher Management (suite component) | (not captured) | voucher management in market definition |
| 5G/era-current | 5G and IoT named; "any identifier – device, user, slice, API, or partner" | (docs predate 5G-slice framing) | slice-based/cross-slice charging; API-invocation charging | 5G ready; VoLTE/VoNR | (not captured) |
| Deployment | cloud-ready/cloud-enabled; cloud-native deployments in press | on-prem/classic component stack | cloud-native, SaaS, edge-distributed | private/public cloud, SaaS, CI/CD | (not captured) |
| Customer tiers | Tier-1 carriers (2.3B users claim) | enterprise/component deployments | Tier-1 through CSP-to-CSP | "500K or 500M"; MVNOs, digital brands | Tier-1 incumbents |

### Cross-product findings

- **B (5/5 + 3GPP)**: Every product centers on the same computation: service consumption events are rated against the subscriber's commercial terms (charge offers/tariffs) to produce charges. 3GPP names this the Rating Function; every vendor describes it in its own vocabulary.
- **B (5/5 + 3GPP)**: Every product holds subscriber money-side state — accounts/balances in monetary or non-monetary units (currency, data volume, minutes, bonuses/vouchers), with reservations against ongoing sessions. 3GPP names this the Account Balance Management Function; Oracle documents it in operational depth.
- **B (5/5 + 3GPP)**: Every product participates in the service delivery path in real time — the network consults charging before/while resource usage occurs; authorization is scoped (quota), renewed, and refusal stops service. 3GPP defines this as online charging / credit control; Ericsson calls the product "the real-time heart of all BSS"; Netcracker puts "online session management" in the latency-critical edge tier; Oracle documents the full prepaid session loop.
- **B (5/5)**: Convergence — prepaid and postpaid, online and offline, in one system — is the standard mature form (every sampled product claims it; 3GPP defines the CCS as the combination). But it is the mature form, not the smallest definition: the OCS lineage (pure online) and the offline rating function both exist as separable concerns, and 3GPP defines them separately.
- **B (4/5 + 3GPP)**: Offline/post-event rating is co-resident (batch rating of CDRs for postpaid billing), feeding the billing domain downstream. Oracle documents it explicitly; the others express it via "convergent."
- **B (4/5)**: Non-usage charges (subscriptions, one-time fees, recurring) flow through the same engine alongside usage charges — the charging platform is the money-computation point for all charge types, not only metered usage.
- **B (4/5)**: Policy-control coupling is standard (named integration or embedded function); depth varies from loose coupling (Amdocs: separate Policy product) to embedded (Optiva). The money computation and the service-rule engine remain distinguishable concerns.
- **B (3/5 + market definitions)**: Partner/wholesale rating and revenue sharing is standard mature structure (Ericsson, Netcracker, Optiva; present in the GlobalData market frame).
- **B (5/5)**: The integration neighborhood is stable: mediation upstream (usage events in), billing downstream (rated events/charges out), plus catalog (offers/tariffs in), subscriber state (entitlements/status in), CRM/self-care (balance queries, top-ups), provisioning (service activation states).
- **A→B**: Deployment spans on-prem component stacks (Oracle), cloud-ready carrier platforms (Ericsson), cloud-native/SaaS/edge-distributed (Netcracker, Optiva). No deployment model is definitional.
- **A (Oracle)**: The operational core loop is documented end-to-end: usage request → identify customer + owned charge offers → rate (RUMs) → authorize/reserve against balance → (session: quota, re-authorization, top-up mid-session) → settle → rated event to billing database → balances updated in both engines.
- **A (3GPP)**: The standard defines exactly the three concerns the products implement — rating, account/balance management, quota/credit control — and explicitly leaves everything else ("all other aspects of the OCS and CCS") to products.

## Canonical Model (abstraction)

### Level 0 — Defining Invariant

1. **Charging computation over service consumption** — the system's defining act: usage/service events (calls, data sessions, messages, content, API calls) are rated against the subscriber's commercial terms (charge offers/tariffs) to produce charges. The charge is the unit of work and the unit of record. Remove → mediation (event plumbing), billing (invoice machinery), or a stateless tariff calculator.
2. **The subscriber account/balance as money-side state** — per-subscriber accounts holding balances in monetary or non-monetary units (currency, volume, minutes, vouchers/bonuses), which charges draw down, recharges/top-ups replenish, and ongoing sessions reserve against. Remove → a rating calculator with no account state; a wallet ledger with no rating.
3. **Real-time service-path enforcement (credit control)** — the charging system sits in the service delivery path: the network/service layer consults it before and during resource usage; authorization is granted in limited scope (quota), renewed as usage persists, and service is rejected or terminated when the account cannot pay. Remove → offline-only rating (a billing-side rating engine) or policy control (service gating without money computation).

Jointly load-bearing: 1 alone = tariff calculator; 2 alone = wallet/prepaid ledger; 3 without 1+2 = network gating without money (policy control); 1+2 without 3 = offline rating + balance accounting inside a billing system; 2+3 without 1 = a prepaid gate that cannot price; 1+3 without 2 = incoherent (enforcement needs state to enforce against).

### Level 1 — Common Mature Structure

- Convergent charging: prepaid and postpaid handled in one system against one subscriber record (the industry's standard mature form; 3GPP CCS)
- Multi-service/multi-play convergence: voice, data, messaging, content, fixed/broadband, TV, IoT, digital services rated by one engine
- Offline/post-event rating co-resident (batch rating of usage records for postpaid billing), feeding the billing domain
- Non-usage charges through the same engine: subscriptions, one-time fees, recurring fees, system-generated charges
- Session/quota management: unit reservation, re-authorization, mid-session top-up, unused-quota return
- Recharge/top-up and voucher/bonus management; balance query APIs for self-care and third-party clients
- Spending controls, allowances, thresholds, real-time notifications (bill-shock prevention)
- Tariff/offer configuration: rate plans, discounts, promotions — consuming the operator's product catalog (or embedding tariff design at component depth)
- Policy-control coupling: balance-driven service/QoS decisions, credit-limit notifications to the policy controller
- Partner/wholesale rating and revenue sharing (B2B2X economics)
- Carrier-grade scale and real-time SLAs (high event throughput, always-on availability)
- The integration neighborhood: mediation upstream, billing downstream, catalog, subscriber state, CRM/self-care, provisioning

### Level 2 — Variant / Optional Structure

- Deployment: on-prem component stacks, cloud-ready carrier platforms, cloud-native, SaaS, public-cloud marketplace, edge-distributed (latency-critical functions at MEC edge)
- 5G-era monetization: slice-based and cross-slice charging, charging on slice parameters, network-API invocation charging
- Identifier scope: subscriber line, device, user, slice, API, partner ("any identifier" framing)
- MVNO/MVNE charging-as-a-service, multi-tenancy, hosted OCS
- Cross-industry/non-telco charging (utility, finance, logistics, entertainment verticals)
- B2B enterprise charging depth: account hierarchies, credit limits, cost-center charging, aggregated/split billing support
- Interconnect/roaming settlement rating
- Era-current layers: AI personalization during usage, anomaly detection, agentic charging/billing operations

### Level 3 — Vendor-specific (Research Notes only)

- Ericsson: "real-time heart of all BSS" positioning; 184 implementations / 2.3B users claim; evolution from Ericsson Charging System; "any identifier" framing; pre-integration list wording.
- Oracle: ECE/BRM dual-engine split (charging engine + billing/subscriber database); Diameter Gateway / HTTP Gateway / EM Gateway names; Rated Event Loader; Offline Mediation Controller as the pre-integrated mediation client; Pricing Design Center (PDC) as pricing configuration surface; balance query modes (SUMMARY/DETAILED/ALL/TURBO); systemwide quota config per product-RUM combination; RUM terminology; server-initiated reauthorization; policy-driven charging terminology; MSID/login authentication examples.
- Netcracker: CCS naming inside Revenue Management suite; OCS (4G) + CCS (5G) coexistence framing; edge/central distributed split naming; "usage-to-payment" phrase; Cloud OCS "always-active" positioning; GlobalData component list (Voucher Management, Partner Billing Management, etc.).
- Optiva/Qvantel: OCE naming; TM Forum ODA directory listing; TM Forum API 620/637 references; "500K or 500M" scale span; "launch new products in hours"; CI/CD release cadence claims; 1Global/Truphone case study; Google Cloud Marketplace transaction model.
- Amdocs: Charging + Matrixx Charging (acquired) component naming; Policy as separate product; GlobalData market-definition hosting.

## Rejected Findings (anti-overfit)

- **"Charging = billing"** — rejected. Charging computes charges in (near) real time and holds balances; billing aggregates charges per settlement period into invoices, presents, collects. Every sampled architecture separates them (Oracle: ECE vs BRM; Amdocs: Charging vs Real-Time/Freestyle Billing; Netcracker: CCS vs billing components; 3GPP: OCS/CCS vs Billing Domain). They ship together in suites but are distinct functions.
- **"Charging = mediation"** — rejected. Mediation collects/normalizes usage events from network elements (dedup, assembly, normalization); charging rates them. Oracle documents the seam explicitly (Offline Mediation Controller creates usage requests "for ECE to rate the events").
- **"Charging = policy control"** — rejected. Policy decides service-delivery rules (QoS, gating) without computing money; charging computes money and can drive policy via balance thresholds. They couple (Oracle "policy-driven charging"; Optiva "embedded rating and policy control") but remain distinct concerns; bundling is a variant.
- **"Convergence (prepaid+postpaid in one) is definitional"** — rejected as definitional; it is the standard mature form (L1). 3GPP defines OCS and OFCS separately; the OCS lineage (pure online) is a complete charging platform; the offline rating function is a billing-side component.
- **"Multi-service convergence (any service type) is definitional"** — rejected. A single-service charging system is still a charging platform; breadth of service vocabulary is market maturity, not definition.
- **"5G/slice/API charging is definitional"** — rejected; era-current capability layer on the same core (rate events, manage balances, control service).
- **"Cloud-native/SaaS is definitional"** — rejected. On-prem component stacks (Oracle docs) and cloud-ready carrier platforms (Ericsson) are first-class realizations; Optiva's case study is explicitly an on-prem-to-cloud migration.
- **"Policy control must be embedded"** — rejected. Coupling depth varies from separate product (Amdocs Policy) to embedded function (Optiva); the invariant is the money computation, not where policy lives.
- **"Partner revenue sharing is definitional"** — rejected as definitional; standard mature structure (L1), absent from the smallest form.
- **"The charging platform owns the subscriber record"** — rejected. The subscriber population and lifecycle belong to Subscriber Management (sibling pass); the charging platform reads entitlements/offers and holds the money state. Oracle's split is explicit: BRM keeps the offers/subscriber data, synchronized into ECE.

## Boundary Findings

- **vs Telecom BSS** (the pre-hung seam): the BSS is the integrated commercial chain (offer → order → subscription → charging → billing → care) over shared records; the charging platform is the money-computation component the chain resolves into. The charging platform has no orders, no care, no catalog ownership (it consumes offers), no subscriber lifecycle ownership. Remove rating/balance computation → a BSS without its money engine; remove the chain around it → a component, not a BSS. The BSS pass recorded: "telecom-charging-platform = rating/balance computation vs the chain resolving into it."
- **vs Billing (Telecom billing / Subscription Billing Platform)**: charging = per-event/per-session money computation with balance state and real-time enforcement; billing = per-settlement-period aggregation of charges into invoices, presentment, payments, collections. The seam is the rated event / charge: charging produces it, billing consumes it. Suites ship both; the functions remain distinct (Oracle ECE vs BRM is the cleanest documented split).
- **vs Mediation**: mediation is the upstream plumbing that collects and normalizes usage events from network elements (dedup, record assembly, normalization); charging is the money computation over those events. Some vendors sell both; the seam is the normalized usage request.
- **vs Policy control (PCF/PCRF-class)**: policy gates and shapes service delivery by rules; charging prices it and holds the money state. They meet at balance-driven policy (thresholds, QoS changes) and at the network's enforcement point, but the concerns are distinct; bundling is a variant, not the definition.
- **vs Subscriber Management** (the pre-hung seam): subscriber management holds who-has-what-and-is-active (the population and lifecycle record); the charging platform holds the money state (balances, reservations) and computes charges. Status gates charging; entitlements/offers feed rating. Neither subsumes the other.
- **vs Telecom Product Catalog**: the catalog defines offers/tariffs as the source of sellable/chargeable terms; the charging platform consumes them. Some charging products embed tariff configuration — the catalog function at component depth, not the standalone catalog discipline.
- **vs Telecom Revenue Assurance**: revenue assurance is the leakage-control discipline over the chain's data; charging is the enforcement point where pricing logic is applied. Different Types; revenue assurance watches charging, does not do it.
- **vs Utility metering/billing (MDMS / Utility CIS)**: same money-computation skeleton (usage → rate → charge → bill) but a different object world: meter reads and utility commodities vs network usage events; batch settlement cycles vs real-time service-path credit control. A utility billing system does not answer the network's "may this usage proceed" question in milliseconds.
- **vs Generic payment/billing engines**: no usage rating, no network credit control, no telecom service semantics, no quota/reservation mechanics. A payment gateway moves money between parties; a charging platform computes what consumption costs against a service entitlement.

## Historical / Market-Sample Check

- 1990s IN-based prepaid platforms (service node querying a real-time balance before connecting a call) satisfy all three L0 legs with no cloud, convergent-charging, 5G, or AI machinery — the real-time credit-control core predates the modern product wave.
- The batch rating engine (offline-only, inside a billing system) is the boundary case: it rates but does not enforce in the service path. The market does not call it a "charging platform"; it is a billing-side component. This confirms that leg 3 (service-path enforcement) is what makes the platform form, while offline rating is a co-resident function of the mature convergent form.
- Small MVNOs and digital brands run hosted OCS with the same core today (Optiva SaaS pole, Netcracker MVNO cloud) — the Type scales down intact.
- The core is not overfit to the 5G/cloud/AI wave: slice/API charging, SaaS deployment, and AI personalization are all variant layers on the same three-leg core.

## Uncertainties

- Amdocs direct fetch was blocked (403) on this pass; its evidence is carried from the sibling telecom-bss pass (same date) and used only for structure/vocabulary. No operational detail asserted for Amdocs.
- Ericsson, Netcracker, and Optiva evidence is product-page/brochure/press tier; none publishes operational user documentation at public URLs. Their internal mechanics (session state machines, quota algorithms, tariff syntax) are not asserted.
- Oracle ECE is the only sampled product with public operational documentation; its documented mechanics (reservation, re-authorization, balance elements, RUMs) are used as the operational anchor, generalized only where 3GPP or other vendors corroborate.
- Market-share proportions between suite components, standalone engines, and network-vendor products are not measurable from available sources.
- The exact product boundary between "charging" and "billing" varies by vendor (some ship one product spanning both); this pass treats them as distinct functions with distinct directory leaves, per the sibling passes' seams.
- Whether the directory intent includes offline-only rating engines as "charging platforms" cannot be resolved from the directory text; this pass treats the offline rating function as co-resident/billing-side and documents the boundary case.

## Final Synthesis

Telecom Charging Platform is the communications service provider's real-time money-computation system for service consumption. Its defining core is three jointly-held structures: (1) charging computation — usage/service events rated against the subscriber's commercial terms (charge offers/tariffs) to produce charges, the system's unit of work and record; (2) the subscriber account/balance as money-side state — balances in monetary or non-monetary units that charges draw down, recharges replenish, and ongoing sessions reserve against; (3) real-time service-path enforcement — the network consults charging before and during resource usage; authorization is granted in limited scope (quota), renewed as usage persists, and service is rejected or terminated when the account cannot pay. Around this core, mature products add the standard structure: convergent prepaid+postpaid handling, multi-service convergence, co-resident offline batch rating, non-usage charges through the same engine, session/quota management with re-authorization, recharge/voucher management, spending controls and notifications, tariff/offer configuration consuming the product catalog, policy-control coupling, partner revenue sharing, carrier-grade scale, and the mediation-upstream/billing-downstream integration neighborhood. Deployment (on-prem/cloud/SaaS/edge), 5G-era monetization (slices, API invocation), identifier scope, MVNO hosting, cross-industry charging, and AI layers are variants, not definitions. The Type is a BSS component with standalone market depth: it is the point where the BSS commercial chain resolves into money, and the point where the network's service path meets the operator's commercial terms.

Historical check passed: 1990s IN prepaid platforms satisfy the core with no modern machinery; the offline-only rating engine is documented as the billing-side boundary case, not the platform Type.
