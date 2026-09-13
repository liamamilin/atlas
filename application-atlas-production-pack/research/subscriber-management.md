# Research Notes — Subscriber Management

Research date: 2026-09-10

## Research Goal

Understand what a "Subscriber Management" application is in reality: what the subscriber record holds, what lifecycle it manages, how it couples to billing / provisioning / care, and where its boundary lies against CRM, Telecom BSS siblings (Provisioning, Charging, SIM/Number Management), Utility CIS — and against the network-equipment usage of the same name ("subscriber management" on BNG routers).

## Initial Boundary

- Directory context: §19 Energy, Utilities & Telecommunications, grouped with Telecom BSS-family leaves (Telecom BSS, Telecom Provisioning Platform, Telecom Charging Platform, Telecom Product Catalog, SIM / eSIM Management, Telecom Number Management, Telecom Order Management).
- Working hypothesis: the operator-side system of record and lifecycle manager for a connectivity service provider's subscriber base.
- Known ambiguity going in: "Subscriber Management" names at least three market referents — (A) an operator/BSS capability (standalone ISP platforms and embedded BSS modules), (B) a network-edge router function (Juniper/Cisco BNG), (C) network-side subscriber data repositories (the docs reference "network subscriber repository"). The leaf is assumed to be (A); (B)/(C) treated as boundary material.

## Research Questions

1. What is the unit of record — "subscriber", "customer", "account"? How do products name it, and what does it hold?
2. What identifier substrate binds a subscriber to the service (phone number, IMSI, account number, address, MAC, RADIUS credential)?
3. What lifecycle states/transitions exist (activation, suspension, termination), and are state names definitional or operator-configurable?
4. How does subscriber status couple to billing and to network service activation?
5. How is the service/entitlement side modeled (tariff plans, services, packages, eligibility)?
6. Where is the seam with provisioning (the act of configuring the network) and with charging/billing (money)?
7. Is this a standalone application category, an embedded BSS module, or both?
8. What does the BNG/router "subscriber management" referent cover, and why is it not this Type?

## Representative Products

Selected for market representativeness + documentation quality + different product philosophies + different customer tiers:

- **Sonar Software** — standalone unified operations platform "built exclusively for ISPs"; fiber/WISP/cable/MDU/VoIP operators; public Tier-1 knowledge base. (Pole: ISP-side standalone platform, small/regional operators.)
- **Splynx** — all-in-one ISP billing & network management framework; European/global ISP market; public Tier-1 wiki. (Pole: ISP framework with explicit CRM/billing/networking modules.)
- **Oracle Communications** (BRM / Service Broker Subscriber Store / Digital Business Experience) — Tier-1 telco BSS pole with directly reachable official documentation, including a section literally titled "About Subscriber Management". (Pole: large-operator embedded BSS.)
- **Netcracker** — Tier-1 BSS suite vendor; official solution pages and press releases (Tier-2 evidence only). (Pole: mega-suite BSS.)
- **Optiva (Redknee, now merged into Qvantel)** — cloud-native BSS/charging vendor; official press release vocabulary uses "monetization and subscriber management solution". (Pole: charging-centric BSS; Tier-2 evidence only.)
- **Juniper Networks Junos OS Broadband Subscriber Management** — network-equipment referent, studied deliberately for boundary determination (Tier-1 docs).

## Sources

- Sonar — https://sonar.software/ (product site); Knowledge Base: https://docs.sonar.expert/ — esp. /accounts/account-statuses-overview-example-use-cases, /networking/how-sonar-can-provision, /first-time-setup/getting-started-with-accounts, /accounts/deleting-an-account (Disconnecting an Account), /accounts/archiving-an-account-overview, /billing/services-overview (KB index titles used as documentation-structure evidence).
- Splynx — https://splynx.com/ (product site); wiki: https://wiki.splynx.com/customer_management/customer_services, https://wiki.splynx.com/customer_management/customer_billing, https://wiki.splynx.com/administration/logs/planned_status_service, https://wiki.splynx.com/administration/logs/pending_statuses_and_services; https://splynx.com/blog/business-automation/how-to-streamline-customer-onboarding-in-splynx/; https://deploy.splynx.com/modules/crm/.
- Oracle — https://docs.oracle.com/en/industries/communications/digital-business-experience/26.4/order-cash/order-payment-business-process.html ("About Subscriber Management", Subscriber Onboarding); https://docs.oracle.com/cd/E23521_01/doc.60/e23529.pdf (Service Broker Subscriber Store User's Guide); https://docs.oracle.com/cd/E23521_01/doc.60/e23529/sdl_lcextend.htm (subscriber account lifecycle states); https://docs.oracle.com/en/industries/communications/billing-revenue/15.2/charging/configuring-subscriber-preferences1.html (BRM/ECE subscriber preferences).
- Netcracker — https://netcracker.com/portfolio/solutions/monetization-and-customer-experience/netcracker-cloud-bss; https://www.netcracker.com/portfolio/solutions/monetization-and-customer-experience/next-generation-revenue-management; https://netcracker.com/news/press-releases/robi-axiata-goes-live-with-netcracker-integrated-revenue-and-customer-management-solution (mentions migrated subscriber data for "retail, corporate, interconnect and roaming subscribers"); AIS press release (2025-12-09, "quad-play subscribers").
- Optiva — https://www.optiva.com/press-releases/lifecell-selects-optiva-for-multi-year-renewal-to-accelerate-services-velocity (operator CIO quote: "monetization and subscriber management solution").
- Juniper — https://www.juniper.net/documentation/en_US/junos/information-products/pathway-pages/subscriber-access/index.html; https://www.juniper.net/documentation/us/en/software/junos/subscriber-mgmt-getting-started/topics/topic-map/subscriber-management-introduction.html; Broadband Subscriber Management Getting Started Guide PDF; MX Series Subscriber Management for Customer VLANs Implementation Guide PDF.

Source-access limitations: Netcracker and Optiva product documentation is not publicly reachable at operational depth; evidence for these two is marketing/press tier only, used solely to confirm vocabulary and market structure, never for operational detail. Juniper documentation was reachable but documents the network-equipment referent, used only for boundary analysis. No precise numeric limits, defaults, or timing values are asserted anywhere in the final document.

---

## Product A — Sonar Software (ISP standalone platform)

### Key observations (Layer A unless noted)

- Self-positioning: "The unified operations platform built exclusively for Internet Service Providers"; modules: Accounts, Billing Tools, Communications, Ticketing, Scheduling, Network & IPAM, Inventory, Purchase Orders, Location Tools, Tasks, Reports. Industries: Fiber, WISP, Cable, MDU, VoIP.
- The unit of record is the **Account**: "Subscriber profiles, service history, and communication logs in a single record." Homepage flow: "Subscriber signs up → Account created with full service history and contact log → Service activated (Network provisioned, equipment shipped, customer online) → Revenue captured (Auto-billing fires)". Uses "subscriber" and "account" interchangeably across its own copy (e.g., KB article "Troubleshooting DHCP: Why Isn't My Subscriber Getting an Address?").
- **Account statuses are a first-class, operator-configurable structure**: default statuses Lead / Active / Inactive; operators routinely create custom statuses (Pending Install, Collections, Failed Install, termination-specific winback/non-winback statuses, Vacation). Documentation states statuses "control whether or not an account will be billed, whether or not their services are active, and can work together with Address Lists/RADIUS Groups to receive specific service levels." — the status is a switch that gates billing and service activation simultaneously.
- **Disconnection is distinct from deletion**: KB contains both "Disconnecting an Account" and "Archiving an Account"; plus "Disconnection Reason Management" — termination is recorded with reasons; the population outlives the service.
- Account structure supports **Account Types** (residential/business visible on homepage screenshot counts), **Account Groups**, **Child Accounts** (hierarchy), **Serviceable Addresses** (anchor & linked; future serviceable addresses) — the subscriber is tied to a service location.
- **Service binding**: Billing KB shows "Services: Overview", "Building a Data Service", "Building Packages", "How to: Adding a Service to an Account", "Configure Service Eligibility Criteria" — services/packages are catalog-defined, then attached to accounts; eligibility criteria govern which services can attach.
- **Provisioning linkage is documented in detail** ("Automating IP Assignments, Data Rates, and Network Access in Sonar"): "automatic provisioning based on account status or activity"; IP assignments can be pushed from Sonar down to DHCP server / RADIUS / LTE core as static leases, or received back as "soft assignments" from DHCP/PPPoE/LTE (matching by MAC or IMSI/IMEI stored on the account's inventory items); data rates and network access are controlled by grouping accounts by account traits and forwarding to inline devices (MikroTik), FreeRADIUS, LTE platforms (Telrad/Baicells), or Preseem; RADIUS/CoA integration ("Setting Up CoA Proxy"); usage data flows back into accounts (Netflow, RADIUS accounting, Preseem, API, PacketLogic).
- Self-service: Customer Portal (configurable, white-label); Field Tech App; API/webhooks ("Everything you see in the Sonar web client has an API endpoint and every action has a webhook").
- Multi-company support ("Managing Multiple Companies") — operator-brand layering is a supported variant.
- Regulatory/industry packaging: FCC Form 477/BDC exports, FCC Broadband Label generation, CPUC reporting, BEAD readiness — market-specific packaging around the subscriber record, not structural.

## Product B — Splynx (ISP framework)

### Key observations (Layer A unless noted)

- Self-positioning: "ISP Billing & Network Management System"; modules: ISP Billing, Ticketing, Network management, Sales (CRM), Customer management, Scheduling and field services, Automated inventory management, Open API; solutions: TR-069 ACS, Wi-Fi Hotspot (Powerlynx).
- Unit of record is the **Customer**; the customer profile has a **Services tab**: "all the products/services provided to that specific customer… you can edit existing services or add new ones to the customer's account. This is where you manage all services for a client, which will affect the bill they receive." Available services: **Internet, Voice, and Recurring services**, each instantiated from a **tariff plan** ("select a service from the list of existing tariffs").
- **Plan change is a managed operation with future dating**: "Change plan" from the admin portal — choose `New plan start date` and `New plan`; pro-rating and refund rules referenced in Config → Finance → Change plan. Layer A evidence for future-dated service modification.
- **Planned/pending status & service changes**: Administration → Logs → "Planned customer status & service changes" — "a list of statuses or plans that will undergo upcoming changes… a customer's status is scheduled to change on a specific day or when a new service is set to be activated on a particular day"; new services enter **pending status** until their start date. Layer A evidence for scheduled lifecycle transitions.
- Onboarding workflow (blog): lead via self-registration widget → quote → "Convert" the lead to a customer, "instantly issuing the invoice based on the quote and adding the active service plan to the customer" — lead→customer conversion creates the service state.
- Network coupling: RADIUS server, ACS (TR-069), IPAM, bandwidth management, network sites — customer provisioning tied to network identity (PPPoE credentials, IP addresses, device management).
- Self-service: customer portal + white-labeled mobile app ("pay the invoices, easily contact support, manage services, check statistics").
- Testimonial vocabulary (Layer B corroboration only): "manage our WISP customers… easily, and quickly provision new customers, delegate their IP addresses, apply shaping and record statistics."

## Product C — Oracle Communications (BRM / Service Broker Subscriber Store / Digital Business Experience)

### Key observations (Layer A unless noted)

- A documentation section literally titled **"About Subscriber Management"** (Digital Business Experience, Order to Payment): "Subscriber Management lets you synchronize subscriber information to BRM from Siebel CRM." Subscriber data is created in BRM (billing/revenue management) from order data; CSR updates accounts in Siebel CRM, which synchronize one-way to BRM. This shows: in a Tier-1 operator stack, "subscriber management" names the maintenance of the subscriber record of record, kept separate from CRM even when CRM holds the customer conversation.
- Lifecycle language (same page): "This process starts with targeted marketing… prospects provide their details to create accounts with the CSP, **becoming subscribers**. Subscribers can then place orders…"; "The Subscriber Onboarding feature creates subscriber data in BRM from order data while processing orders."
- **Service Broker Subscriber Store** (network-facing subscriber profile store): "To deliver subscriber-specific services… maintains a subscriber profile for each subscriber in the Subscriber Store"; each subscriber represented by a profile associated "through the network ID for that user. The network ID can be an International Mobile Subscriber Identity (IMSI) number, SIP address, E.164 number, or other type of network ID"; each subscriber also gets an internal user ID. Profile elements include accountState, accountType (prepaid / postpaid / hybrid), dateOfBirth, groups, language, notificationChannel, subscriberActivationDate.
- **Explicit, configurable lifecycle states**: default states "Pre-Active, Active, Suspended, Locked, Deactivated"; operators can add/change/delete states; the provisioning API validates state values; "Service Broker does not otherwise interpret the meaning of a particular state value. It is the role of the back end system to associate a particular state with service provisioning logic." — status is carried as data and interpreted downstream.
- **System-of-record discipline**: "BRM remains the system of record for subscriber data" (when multiple systems touch subscriber data, one is designated the record; downstream stores cache/refresh via change notification).
- BRM/ECE **subscriber preferences** stored "at the account level and the service level"; "subscriber life cycle state transition notifications" exist as an event type — lifecycle transitions are explicit events that other systems react to.
- The Subscriber Store documentation notes it "is intended to supplement the information in the operator's existing subscriber repository or billing system" — acknowledging separate network-side subscriber repositories as neighbors.

## Product D — Netcracker (Tier-2 evidence only)

### Key observations

- BSS suite organized around Customer Engagement / Digital BSS / Digital OSS / Revenue Management; subscriber vocabulary appears in press releases: "care… operations for subscribers as well as roaming and interconnect partners"; "migrated subscriber data to the new solution from a multi-source system containing information on retail, corporate, interconnect and roaming subscribers"; AIS deployment serving "B2C and B2B quad-play subscribers".
- Confirms (Layer B, weak): subscriber is the unit of the operator's base even in quad-play/multi-line-of-business stacks; subscriber-data migration is a recognized program activity (multiple legacy sources → one record). No operational detail accessible; no operational claims taken from this vendor.

## Product E — Optiva (Tier-2 evidence only)

### Key observations

- Official press release quotes the operator CIO: "We will leverage Optiva's **monetization and subscriber management solution**…" — "subscriber management" used by a BSS vendor as a named capability alongside monetization.
- Vendor profiles (secondary sources; corroboration only) describe the portfolio as "monetization and subscriber management solutions include real-time billing, charging, policy, and customer care modules" — subscriber management positioned adjacent to (not equal to) charging/billing. No operational detail accessible.

## Product F — Juniper Junos OS Broadband Subscriber Management (network-equipment referent; boundary analysis)

### Key observations (Layer A)

- "The Juniper Networks Junos OS subscriber management feature provides subscriber access, authentication, and service creation, activation, and deactivation. You can also collect accounting information and statistics for subscriber service sessions."
- "Broadband Subscriber Management is a method of dynamically provisioning and managing subscriber access in a multiplay or triple play network environment. This method uses AAA configuration in conjunction with dynamic profiles to provide dynamic, per-subscriber authentication, addressing, access, and configuration…"
- Subscribers are **sessions** on the BNG: created/modified/deleted via RADIUS Access-Accept / CoA / disconnect messages or DHCP/PPP client messages; a subscriber service = dynamic profile template + authentication attributes (filters, CoS, IGMP); service activation/deactivation is dynamic per session.
- Implementation guide: "Subscriber management is performed by the Broadband Network Gateway (BNG) router… Subscriber management is also called AAA (authentication, authorization, and accounting), or AAAA (which adds address assignment)."
- Conclusion: this is the **network-edge realization of per-subscriber control** — a router capability, not a standalone application product. Its "subscriber" is a live session, not the durable population record. It documents that the operator-side record (where one exists) and the edge enforcement are distinct layers.

---

## Cross-product Comparison

| Dimension | Sonar | Splynx | Oracle (BRM/Subscriber Store) | Netcracker / Optiva (Tier-2) | Juniper BNG (different referent) |
|---|---|---|---|---|---|
| Unit of record | Account (holding subscriber profile, service history, comm logs) | Customer | Subscriber (profile / record of record) | "subscriber" (press vocabulary) | subscriber session (ephemeral, network) |
| Identifier substrate | account ID; serviceable address; MAC / IMSI / IMEI on inventory items; RADIUS credentials | customer ID; PPPoE/IP credentials | network ID: IMSI, SIP address, E.164 + internal user ID | not observed | PPP/DHCP identity, RADIUS username, MAC |
| Service binding | catalog services/packages attached to account; eligibility criteria | tariff-plan services (Internet/Voice/Recurring) attached on Services tab | service-level & account-level profile data; service chain elements | offer/catalog language | dynamic profile + RADIUS attributes per session |
| Status / lifecycle | default Lead/Active/Inactive + custom; status gates billing AND service activation | planned/pending status & service changes; future-dated | Pre-Active/Active/Suspended/Locked/Deactivated; configurable; state-transition events | not observed | session create/modify/delete via RADIUS/CoA |
| Provisioning link | "automatic provisioning based on account status"; pushes IP/rates/access to DHCP/RADIUS/LTE/inline devices | RADIUS/ACS/IPAM provisioning tied to customer | state interpreted by back-end provisioning logic; BRM syncs from order flow | fulfillment language (Tier-2) | IS the network provisioning itself |
| Billing link | status controls whether billed; services priced → invoices | services tab "will affect the bill they receive" | BRM = system of record incl. billing; subscriber preferences | revenue-management adjacency (press) | "subscribers can be billed based on the service level and usage" |
| Self-service surface | customer portal | portal + mobile app | CSR tools; preferences collected via client tools | care apps (Tier-2) | none |

### Cross-product findings

- **B (cross-product)**: Every operator-side product centers on a durable, identified record per service consumer (called subscriber / customer / account — vocabulary varies), carrying at least: identity/contact data, one or more attached services, and an operational status.
- **B**: Status is an explicit, controlled attribute whose change is an event with downstream consequences — gating billing (Sonar: statuses "control whether or not an account will be billed"; Splynx: services "will affect the bill they receive") and gating network service activation (Sonar: statuses "control… whether or not their services are active"; Oracle: back-end systems "associate a particular state with service provisioning logic").
- **B**: Service attachment is catalog-driven — services/plans are defined once and instantiated per subscriber (Sonar services/packages; Splynx tariff plans; Oracle service-level profile objects).
- **B**: The subscriber record binds to network identity and equipment, but the identifier substrate varies (phone/E.164, IMSI, SIP, MAC, RADIUS credentials, IP, serviceable address) — no single identifier is universal.
- **A→B**: Future-dated / planned changes exist (Splynx planned changes; Sonar scheduled events; dated plan changes) — scheduled lifecycle is common but not universal.
- **A (product pair)**: Termination is recorded (reasons, winback/non-winback, archiving) and the record persists after service ends (Sonar disconnection + archiving; Splynx logs; Oracle keeps deactivated state as a state, not a deletion).
- **A**: One vendor documents multi-system discipline explicitly: when CRM and subscriber management coexist, subscriber data has a designated system of record and synchronized copies (Oracle "About Subscriber Management", one-way CRM→BRM sync).

## Canonical Model (abstraction)

### Level 0 — Defining Invariant

1. **Subscriber population of record** — the service provider keeps a persistent, identified record for each of its service consumers (the subscribers). The population outlives any single service transaction and outlives service termination (deactivation ≠ deletion). Remove → a contact list / CRM contact base.
2. **Per-subscriber service state** — each record carries what services the subscriber currently has, with their operational parameters/entitlements, instantiated from a service catalog. This is operational state that other systems (charging, provisioning, care) consume. Remove → a directory with no service semantics.
3. **Managed subscriber lifecycle** — operator-controlled, recorded transitions of the subscriber and their services (onboarding/activation, modification, suspension/resumption, termination), including the controlled status attribute that drives downstream effects. Remove → a static registry / roster.

Jointly load-bearing: 1 alone = contact list; 2 alone = entitlement database; 3 alone = workflow engine over nothing; 1+2 without 3 = static snapshot; 1+3 without 2 = lifecycle machinery over nothing; 2+3 without 1 = per-service tracking with no standing population.

### Level 1 — Common Mature Structure

- Service catalog (plans/services/packages defined once, attached per subscriber; eligibility rules)
- Status-gated coupling: status drives billing participation and service activation/access level
- Network identity & equipment binding (SIM/IMSI, MAC, CPE, credentials, IP) and provisioning hand-off to network systems
- Service location / serviceability linkage
- Account hierarchy and typing (residential/business, child accounts, groups)
- Self-service portal for subscribers
- CSR-facing detail view: service history, communication logs, notes, documents
- Search/list over the population; status-based reporting

### Level 2 — Variant / Optional Structure

- Account-type poles: prepaid / postpaid / hybrid (Oracle-documented); recurring vs prepaid billing styles (ISP pole)
- Future-dated / planned status and service changes
- Disconnection reasons, winback/collections/failed-install status taxonomies, vacation/seasonal suspension
- Usage-data ingestion and usage-based policies (ISP pole)
- Multi-brand / multi-company operation; MVNO / wholesale subscriber layers (Tier-2 telco evidence)
- Subscriber-data migration between systems (major telco program activity, Tier-2)
- Regulatory reporting packaging around the subscriber record (FCC/BDC, CPUC — regional packaging)

### Level 3 — Vendor-specific (Research Notes only)

- Sonar: DHCP Batcher, Sonar Flow, vacation mode implementation, CoA proxy setup, RADIUS group/address-list mechanics, sonarPay, Sonar Retain, Looker-based BI, GraphQL API with per-object endpoints/webhooks.
- Splynx: Powerlynx hotspot product, TR-069 ACS packaging, "Convert lead" one-step create-with-service, config keys for refund-on-plan-change.
- Oracle: Subscriber Provisioning API operations (storeSubscriber/getSubscriber/updateSubscriber/deleteSubscriber), PCP Profile Adapter/AQ change-notification caching, iFC service-chain profile data, /config/subscriber_preferences_map object.
- Juniper: dynamic profiles, RADIUS VSAs, domain maps, L2-BSA wholesale, enhanced subscriber management architecture, subscriber-access licensing.
- Netcracker/Optiva: product branding (Cloud BSS, Revenue Management Cloud, Charging Engine), Qvantel/Optiva merger (Dec 2025).

## Rejected Findings (anti-overfit)

- **Phone number / MSISDN as the subscriber identity** — rejected. Substrate varies (IMSI, SIP, E.164, MAC, account number, serviceable address) across the sample; fixed/cable/ISP products have no MSISDN. The invariant is "some network-recognizable identifier binding", not any particular identifier.
- **SIM binding as definitional** — rejected; only mobile-flavored stacks use SIMs; SIM lifecycle is a neighboring leaf (SIM / eSIM Management).
- **Specific status vocabularies (Lead/Active/Inactive; Pre-Active/Active/Suspended/Locked/Deactivated)** — rejected as definitional; both sampled sets are explicitly operator-configurable. The invariant is a controlled status whose transitions drive downstream systems, not any name set.
- **Billing/invoicing inside the Type** — rejected as definitional. Billing appears throughout as a coupled-but-distinct function (status gates billing; services "affect the bill"); charging/billing has its own leaves. Subscriber management is the record that billing reads, not the money computation.
- **CRM-as-subscriber-management** — rejected; Oracle's own integration architecture keeps them as two systems with one-way sync of the subscriber record; Splynx ships "CRM" as one module among several in a platform whose record center is the serviced customer.
- **BNG/router "subscriber management" as the Type** — rejected for this leaf: ephemeral sessions + AAA enforcement, no standing population of record, no commercial lifecycle. Recorded as a homonym/boundary issue.
- **Portal/ticketing/inventory/field-service as part of the Type** — rejected; these are platform satellites in ISP standalone products, not the defining center.

## Boundary Findings

- **vs Customer Relationship Management / CRM**: CRM's center is the commercial relationship (leads, deals, interactions); subscriber management's center is the operational service state (entitlements + status + lifecycle). They interoperate (CRM conversation → subscriber record of record) but answer different questions. Strip service entitlement/lifecycle → CRM/contacts.
- **vs Telecom Provisioning Platform**: provisioning is the act of configuring network elements/services; subscriber management is the subscriber-side state of record from which the act is directed (Sonar documents its own provisioning as driven by account status; Oracle leaves state→provisioning interpretation to back-end logic). In the BNG referent, "subscriber management" collapses into network provisioning — evidence that the leaf's identity rests on the standing record, not the network act.
- **vs Telecom Charging Platform / Subscription Billing**: charging/billing computes money (rating, balances, invoices); subscriber management holds who-has-what and whether they are active. They couple through status and service attachment (status gates billing; services feed invoices) but neither subsumes the other.
- **vs SIM / eSIM Management & Telecom Number Management**: credential and number populations are managed resources of their own; the subscriber record binds them (IMSI on inventory items; IMSI/E.164 as network IDs) but the resource lifecycle is the neighbor's center.
- **vs Telecom Order Management**: orders are the transactions that cause change (add/change/disconnect); subscriber management is the persistent state those transactions write. Oracle's own flow shows the seam: order processing → "Subscriber Onboarding… creates subscriber data in BRM".
- **vs Utility Customer Information System / CIS**: same skeleton (customer of record + service + lifecycle + billing coupling), but the utility CIS is centered on meters/rates/usage of utility commodities; different object center and regulatory world. Adjacent, not identical.
- **vs Customer Portal**: the portal is the subscriber-facing surface (pay, manage services, view usage); subscriber management is the operator-facing record the portal reads/writes. Portal is a common attached surface, not the Type.
- **Network-equipment homonym**: "subscriber management" on BNG routers (Juniper/Cisco-class) names per-session AAA/addressing/CoS enforcement. Same words, different referent: session-scoped, network-internal, no commercial lifecycle, no standing population. Recorded in STATUS.md as a boundary issue; directory context (BSS neighborhood) resolves the intended referent.
- **Network-side subscriber repositories** (the docs' "network subscriber repository"): databases that hold subscriber data for network elements. Neighbor with the same population, different consumer (network lookup vs operator management). Oracle's Subscriber Store explicitly "supplements" the operator's existing subscriber repository — coexistence is documented vendor behavior.

## Uncertainties

- Precise state machines (which transitions are legal from which state) are product- and deployment-configured; no cross-product transition table can be asserted.
- Netcracker/Optiva operational behavior unverified (marketing-tier only); they are used solely as market-structure corroboration.
- The relative share of standalone-platform vs embedded-BSS realizations in the market is not measurable from available sources; both poles are documented, market share is not.
- Whether directory intent includes the network-equipment homonym cannot be confirmed from the directory text alone; resolved by §19 neighborhood context and recorded as a boundary issue rather than silently decided.

## Final Synthesis

A Subscriber Management application is the connectivity service provider's operator-side system of record for its subscriber base. Its defining core is the standing population of subscriber records, each carrying the services the subscriber currently has (instantiated from a service catalog) plus a controlled operational status; the application manages the subscriber lifecycle — onboarding/activation, service modification (often future-dated), suspension/resumption, recorded termination — and the status transitions drive downstream systems: billing participation and network service activation/access. Identity is bound through whatever network-recognizable substrate the service uses (account number, serviceable address, phone number, IMSI, MAC, credentials). Everything else commonly bundled around it — portals, ticketing, inventory, field service, usage policies, regulatory reporting — is mature packaging, not the defining core. The same name appears on network-edge router functions (per-session AAA enforcement) and on network-side subscriber repositories; both are neighbors, not this Type.

Historical check: paper-era subscriber ledgers and cable-TV subscriber card files — a persistent population, each entry noting the service taken and activation/disconnection — satisfy the defining core with no modern machinery, so the core is not overfit to current cloud/BSS implementation.
