# Research Notes — Utility Customer Information System / CIS

## Research Goal

Understand what a **Utility Customer Information System (CIS)** actually is from real products: what objects it holds as its system of record, who operates it, how the customer/service relationship is organized, what the "customer care" operation consists of, how billing and the money cycle sit inside it, and where its boundaries run.

This pass carries **three pre-hung flags from processed siblings** that it must discharge:

1. **utility-billing-platform** (§19, 2026-09-10): "utility billing" and "CIS" are two names/poles of ONE family; keep-both recommended; forward note — *"the CIS pass should test the customer-care-led pole from its side."*
2. **gas-utility-management** (§19, 2026-09-08): held as the gas vertical edition of the utility customer-management family; flagged CIS + Utility Billing to test the vertical-edition framing.
3. **outage-management-system-oms** (§19, 2026-09-09): CIS is the customer-identity/phone/service-point data source the OMS matches callers against; call logging without network-model prediction is the below-Type pole (trouble-call logging).

## Initial Boundary

- The leaf sits in §19 between Meter Data Management (processed) and Utility Billing Platform (processed), near the processed gas/water verticals and Utility Field Service Management (unprocessed).
- Working hypothesis entering the pass: CIS = the same utility customer-management family as Utility Billing Platform, held under a customer-care-led name at the enterprise tier; the customer/service record is the organizing spine and care machinery is first-class.
- Suspected risks: (a) pure alias with Utility Billing Platform (must decide keep-both vs merge honestly); (b) collapse into generic CRM (§07) — must show what the utility machinery adds; (c) confusion with MDMS (upstream data layer) and with the OMS (trouble-call logging below-Type pole).

## Research Questions

1. What objects form the CIS's system of record? Is there a customer record distinct from the service account?
2. What is the organizing spine — the customer/service relationship or the money cycle?
3. What does "customer care" concretely consist of in a CIS (contacts, cases, correspondence, appointments, quotes, marketing)?
4. Is billing always inside a CIS? Is the money cycle part of the defining core or an add-on?
5. How do enterprise CIS products differ from the billing-led products sampled by the sibling pass?
6. Where do the boundaries run: vs Utility Billing Platform, MDMS, OMS, generic CRM, subscriber management (telecom), field service, the commodity verticals, the customer portal?

## Representative Products

Chosen for market representation + documentation accessibility + different product philosophies + different customer tiers. NISC (the co-op-tier vendor most associated with the CIS name) timed out ×2 across prior passes — abandoned per network rules, no claims drawn. Advanced Utility Systems transport-errored ×2 this pass — abandoned, held at cross-pass corroboration strength from the gas pass.

| Product | Vendor | Tier / philosophy | Evidence |
|---|---|---|---|
| Oracle Utilities Customer Care and Billing (Cloud Service) | Oracle | enterprise CIS; deepest official docs; care breadth first-class | A — TOC + 4 topic pages fetched verbatim 2026-09-10 |
| SAP S/4HANA Utilities (IS-U + Customer Engagement) | SAP | enterprise ERP-embedded realization | A− — official SAP learning pages + help-portal PDF via search index |
| Itineris UMAX Utility Suite | Itineris | international CIS+CRM+ERP suite on Microsoft Dynamics 365 | A — homepage + Customer Platform page fetched verbatim |
| Cayenta | Cayenta (N. Harris) | mid-market North American utility suite (CIS + work + financials + HCM) | A — homepage fetched verbatim |
| NorthStar Customer Information & Billing | NorthStar (N. Harris) | mid-market CIS + portal + mobile workforce (Ontario/co-op pole) | A — homepage fetched verbatim |

Cross-pass corroboration (fetched in earlier passes, cited as corroboration only): Advanced Utility Systems CIS Infinity ("electric, water, gas, and multi-service providers"; "meter-to-cash" — gas pass 2026-09-08); MuniBilling + Springbrook Cirrus (the billing-led pole — utility-billing pass 2026-09-10); Gentrack (supplier-side CIS in competitive retail — utility-billing pass).

## Sources

Fetched 2026-09-10 (this pass):

- Oracle CCB Business User Guide TOC: https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/CCB_BP_Intro.html
- Oracle CCB — Understanding The V: https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/C1_BP01CustInfo_Understanding_The_V.html
- Oracle CCB — Customer Information: https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/C1_BP01CustInfo_Customer_Information.html
- Oracle CCB — Case Management: https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/C1_BP21Cases_Case_Management.html
- Oracle CCB — Customer Contacts: https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/C1_BP01CustInfo_The_Big_Picture_Of_Customer_Conta.html
- Itineris homepage: https://www.itineris.net/ ; UMAX Customer Platform: https://itineris.net/global/solutionsforutilities/umax-customer-platform/
- Cayenta: https://www.cayenta.com/
- NorthStar: https://www.northstarutilities.com/
- SAP learning (official): https://learning.sap.com/courses/configuring-master-data-and-basic-functions-in-sap-s-4hana-utilities-jp/exploring-utilities-data-model ; https://learning.sap.com/courses/configuring-master-data-and-basic-functions-in-sap-s-4hana-utilities-br/attending-the-customer-with-customer-engagement ; https://learning.sap.com/courses/transitioning-to-sap-s-4hana-for-utilities/analyzing-sap-s-4hana-utilities-customer-service-and-engagement-processes ; https://learning.sap.com/courses/configuring-billing-and-invoicing-in-sap-s-4hana-utilities/understanding-billing-processes-and-master-data-in-sap-utilities
- SAP Service Cloud V2 Add-On for Utilities (help.sap.com PDF, via search index)

Unreachable: NISC (timeouts ×2 across passes), Advanced Utility Systems (transport error ×2 this pass), SAP help portal direct (JS-rendered; used official learning pages + indexed excerpts instead).

## Product Observations

### Oracle Utilities Customer Care and Billing (Cloud Service)

Evidence layer A (fetched verbatim).

- **Self-identification as CIS**: "We use the term **customer information** to reference the demographic, geographic, and financial objects that form the core of your CIS system."
- **The "V" — the core object model**: "The 'V' is the shape of a diagram we use to illustrate the objects that form the core of the system: **Person**, **Account**, **Premise**, **Service Agreement**, and **Service Point**. These objects hold demographic, geographic, and financial information about your company's customers and properties." Related objects attached to the V: **bill, payment, meter, field activity, meter read**.
- **Business User Guide TOC** (the CIS pole's full breadth, verbatim section list): User Interface Features; Customer Information; Meter Management; Meter Reading; Service Orders; Billing; Payments; Adjustments; Credit & Collection; Financial Transactions; Deposits; Statements; **Sales & Marketing**; Rates; **Quotes**; Service Credits; **Appointments**; Loans; Non-Billed Budgets; Asset Inventory; **Case Management**; Premise Management; Umbrella Agreement Management; Job Streams; Workflow and Notifications; Overdue Financial Obligations; Dashboards; Rebate Claims; Interval Billing; To Do Processing; Reports.
- **Customer Information sub-topics**: Understanding/Navigating/Maintaining The V; Bill Print Groups; **Landlord Reversion**; Premise Replicator; **Start/Stop**; **Customer Contacts**; **Printing Letters**; Declarations; Service Tasks; **Registration Points**; **Consumer Contracts**; **Customer Service Requests**.
- **Customer Contacts (care machinery, verbatim)**: "Customer contacts are used to record when and why a customer contacted your company. They can also be associated with person, accounts, and premises. This information can be used for both audit and statistical purposes." Sub-topics: person-based vs premise-based contacts; contacts trigger letters; contacts trigger reminders; contacts record notifications; **contacts can be used as case files**; call summary and call tagging.
- **Case Management (verbatim)**: "**Separate module.** … If this module is not applicable to your business you may turn it off." Uses: "a high-bill complaint, a bankruptcy, an inspection of a premise, a customer's request for literature, a contractor's request to extend a line, a customer's rejection of a quote, a customer's request to change information on a future date, the processing of a market message in a deregulated environment." "Since virtually all aspects of case management functionality are controlled by your implementation, you can use it to handle a myriad of business requirements."
- Reading: the enterprise CIS carries the FULL family machinery (metering, billing, payments, adjustments, credit & collections, deposits, rates, statements) AND a first-class care/commercial layer (contacts, cases, letters, sales & marketing, quotes, appointments, loans, rebate claims, service credits). The care layer is explicitly modular and implementation-configurable.

### SAP S/4HANA Utilities (IS-U + Customer Engagement)

Evidence layer A− (official SAP learning pages + help-portal PDF via search index).

- **Data model (official learning, verbatim)**: "Business master data - the customer-centric trio of **business partner, contract account, and contract**." Business Partner = "Person or organization doing business with the company… created in the role of Contract Partner." Contract Account = "An account in which posting data for contracts or contract items for which the same collection/payment agreements apply is processed. Contract accounts are managed on an open item basis within contract accounts receivable and payable." Contract = "An agreement concluded between a utility company and one of its business partners with respect to a specific division."
- **Technical master data**: connection object, premise, **PoD** (point of delivery), installation, device, register. "Installation: Group of all devices, registers and flat rate billing values that are specific to a division, allocated to a premise, and grouped together for billing purposes." "Devices and registers are allocated to the customers via their contracts and installations for billing purposes."
- **Customer Engagement / interaction center (care machinery)**: "the interaction center as a central point of entry to search and manage utilities master data as well as to carry out traditional utilities industry processes such as meter reading, bill correction, move-in/out"; agent inbox as "central shared worklist… inbound & outbound correspondence (e-mail, fax, letter)"; service requests with "multilevel categorization, integration with knowledge articles, ERMS enablement, checklist, rule-based dispatching, time recording, follow-up transactions"; **Fast Move-In/Out** ("move-in for occupied premise, forced move-out"); Collections ("installment plan, promise to pay, deferral, write-off, external agency integration, credit memo"); Financial Inquiries ("account balance overview… open items… locks, dunning history"); Sales Contracts ("Utilities Sales Contract Management manages the life cycle of an energy (commodity) contract… sold in sales channels… quote to shipment").
- Reading: the ERP pole realizes the same structure with different vocabulary — business partner ≈ person, contract account ≈ account, contract ≈ service agreement, connection object/premise/PoD ≈ premise/service point, installation ≈ the metering grouping. The care layer (interaction center, service requests, correspondence, fast move-in/out) is first-class and named "Customer Engagement."

### Itineris UMAX Utility Suite

Evidence layer A (fetched verbatim).

- **Positioning**: "AI-powered CIS, CRM & ERP for utilities"; "UMAX supports accurate conversion of meter readings to bills, with extensive customer and field service support capabilities." Sectors: energy utilities, water utilities, EV operators (EV as a separate sector — corroborates the EV-charging seam from the sibling pass).
- **Suite structure**: "The UMAX Customer Platform delivers a robust set of CIS, CRM and ERP modules… working together on one unified platform, powered by Microsoft Dynamics 365."
- **CIS modules ("UMAX Manage")**: "It delivers powerful **meter-to-cash** capabilities, streamlining billing, customer management, and revenue processes." Modules: Account Management ("complex accounts, including multi-relationships, move-ins/outs, exemptions, landlord/tenant setups, and B2B billing – and resolve customer cases and complaints with full account context"), Broker Management, Contract Management, **Meter Data Management** (embedded MDM module), Asset & Service Management, Product & Pricing, Market Interaction, Billing & Commissions, Payment & Collections.
- **CRM modules**: "This set of customer-engagement modules unify Sales, Marketing, and Customer Service… **natively integrated with the CIS modules**." Sales (UMAX Grow), Marketing (UMAX Engage), Customer Service (UMAX Serve — "360° view of every customer… track all interactions in a single timeline"), Front Office (+ Contact Center add-on with voicebot/chatbot), Field Service (UMAX Maintain), Customer Self-Service (UMAX Empower).
- **ERP modules**: Finance, Supply Chain Management, Project Management.
- Reading: the clearest architectural statement of the CIS pole — CIS (meter-to-cash) and CRM (care) are distinguished as module families but shipped natively integrated on one platform; the customer-care layer is first-class, not an afterthought.

### Cayenta

Evidence layer A (fetched verbatim).

- **Positioning (verbatim)**: "A Customer Information System built around your customers, consolidating customer service, billing, and account insight into one trusted operational hub."
- **Suite**: CIS + Work Management ("asset management, inventory, and field operations") + Financial Management ("multi-fund accounting") + Human Capital Management.
- **Industries**: Electric, Water, Gas, Fiber; Municipalities, Counties, Co-Ops, Investor Owned. A division of N. Harris Computer.
- Reading: mid-market North American CIS — the customer-care-led framing is explicit ("built around your customers"), and the CIS is one pillar of a wider government/utility suite.

### NorthStar

Evidence layer A (fetched verbatim).

- **Positioning**: "NorthStar is a software provider of innovative, customer experience solutions for modern utilities. Whether you need a cloud-based or on-premise CIS, a web-based customer portal, or digital mobile workforce management software…"
- **Solutions**: Customer Information & Billing; Mobile Workforce Management; Cloud & Managed IT; Utility Customer Portal (SilverBlaze); Managed Security; Personalized Video Engagement.
- Reading: mid-market CIS (Ontario/co-op pole) — "Customer Information & Billing" as the product name shows the CIS name carrying billing inside it; customer-experience framing leads.

### Cross-pass corroboration

- **Advanced Utility Systems CIS Infinity** (gas pass, 2026-09-08): municipal-tier CIS; "electric, water, gas, and multi-service providers"; "customer service points"; "meter-to-cash."
- **MuniBilling / Springbrook Cirrus** (utility-billing pass, 2026-09-10): the billing-led pole — full family structure (accounts, meters, service orders, money) under a "utility billing" name at the small/municipal tier, without the enterprise care breadth.
- **Gentrack** (utility-billing pass): supplier-side CIS/billing/debt platform for competitive retail energy markets — the retail-competition seat.

## Cross-product Comparison

| Dimension | Oracle CCB | SAP S/4HANA Utilities | Itineris UMAX | Cayenta | NorthStar |
|---|---|---|---|---|---|
| Category name | Customer Care and Billing (self-describes the objects as "the core of your CIS system") | IS-U / S/4HANA Utilities + Customer Engagement | "CIS, CRM & ERP for utilities" | Customer Information System | Customer Information & Billing |
| Customer record | Person (with relationships, hierarchies) | Business Partner (person/org, Contract Partner role) | Account Management with multi-relationships, landlord/tenant, B2B | customer records ("built around your customers") | customer records |
| Service account | Account + Service Agreement | Contract Account + Contract | Contract Management + Account Management | accounts | accounts |
| Premise / service point | Premise + Service Point | Connection Object + Premise + PoD + Installation | (within account/asset modules) | service addresses | service addresses |
| Metering | Meter Management + Meter Reading (+ Interval Billing) | Installation/Device/Register + meter reading | embedded MDM module | metering within CIS | metering within CIS |
| Billing & money | Billing, Payments, Adjustments, Credit & Collection, Deposits, Statements, Rates | billing + invoicing + FI-CA (contract accounts receivable/payable), budget billing, dunning | Billing & Commissions, Payment & Collections | billing + multi-fund financials | billing |
| Care machinery | Customer Contacts (audit/statistics, letters, reminders, case files, call tagging), Case Management (separate module), Customer Service Requests | Interaction Center, service requests, agent inbox, correspondence, fast move-in/out | CRM modules: Sales, Marketing, Customer Service, Front Office, Field Service, Self-Service | "customer service… in one trusted operational hub" | customer-experience framing, portal |
| Commercial breadth | Sales & Marketing, Quotes, Appointments, Loans, Rebate Claims, Service Credits | Utilities Sales Contracts, sales channels, collections | Sales, Marketing, broker management | — (not documented at fetched depth) | — |
| Field work | Service Orders, Field Activity | maintenance service orders/quotes | Field Service module + mobile app | Work Management pillar | Mobile Workforce Management |
| Deregulation machinery | Registration Points, Consumer Contracts, market messages in cases | PoD ("globally identified unique service point"), market communication | Market Interaction module | — | — |
| Platform | Oracle-owned stack | SAP ERP | Microsoft Dynamics 365/Azure | own suite | own suite + hosted cloud |

Reading across the sample: **the same family structure recurs under the CIS name at every sampled tier** — customer records, service accounts bound to premises/service points, meters and reads, the bill/money cycle, service orders, and a care layer (contacts/cases/correspondence) that is first-class at this pole. The care/commercial breadth (cases, quotes, marketing, appointments, loans) is documented in depth at the enterprise CIS pole and is thin or absent in the billing-led products the sibling pass sampled. The vocabulary differs radically (Oracle's V vs SAP's trio vs Itineris's module families); the structure does not.

## Canonical Abstraction

### L0 — Defining Invariant

**Shared with Utility Billing Platform (keep-both ratified from this side).** The utility customer-management family's defining core is exactly three jointly-held structures:

1. **The served-premise service account of record** — a persistent identified account binding a customer to a served premise/service point for a metered utility service, carrying service state + financial standing, operated open→sustain→close through service actions, accumulating consumption/bills/payments/arrears. (Remove → a CRM contact base or a generic billing account with no served-premise semantics.)
2. **The metered-consumption basis** — meters bound to the account's service points, periodic reads (manual/estimated/remote feeds as implementations) accumulating measured usage per billing period. (Remove → fee-based billing, not utility billing.)
3. **The meter-to-bill-to-money cycle** — recurring bill production converting consumption into charges under configured rates, the bill as the authoritative lifecycle-managed amount-due record, payments/adjustments/deposits/arrears/budget-plans/collections tracked as financial transactions on the same account. (Remove → meter-reading tool or care CRM with no revenue loop.)

Jointly-held load-bearing (re-confirmed from this side): 1 alone = CRM/generic billing; 2 alone = MDMS/AMI territory; 3 alone = generic billing engine; 1+2 without 3 = meter ops with no revenue loop; 1+3 without 2 = fee-based billing; 2+3 without 1 = a billing engine over meter data (component, not category).

**Historical check (§24)**: the paper-era utility office — customer ledger card per served premise, meter book, typed bills with payment stubs, complaint notes, collection letters — satisfies all three structures with no software-era machinery. The enterprise CIS name and its deregulation machinery (PoD, market messages, registration points) are era/market overlays, not definitional. Regional check: North American municipal/co-op CIS, European energy/water CIS, and competitive-retail supplier CIS all fit the same L0. **Passed.**

### L1 — Common Mature Structure (the CIS pole's standard breadth)

- **The customer-relationship layer**: person/organization records distinct from accounts; one customer holding multiple accounts/premises; relationships and hierarchies (landlord/tenant with reversion, B2B, umbrella agreements). Present in every sampled CIS; the spine the care layer attaches to.
- **The care operation**: logged customer contacts (when/why a customer contacted the utility — audit + statistics), cases/complaints, correspondence (letters/emails), reminders/notifications, customer service requests. First-class at this pole.
- **Service orders** as the office↔field instrument (start/stop/change, meter work, investigations).
- **The credit machinery**: deposits, budget/equal-payment plans, arrears aging, collections, disconnect-for-nonpayment coupling.
- **Rate configuration executed inside the bill cycle** (rate design tools are a sibling leaf).
- **Customer self-service portal** as the modern layer.

### L2 — Variant / Optional Structure

- **Care/commercial breadth beyond the base**: case management as a separate turn-off-able module; quotes; sales & marketing; appointments; loans; rebate claims; service credits. CIS-pole-typical, product-variable — not universal, not definitional.
- **Deregulation/retail-competition machinery**: market messages, registration points, consumer contracts, PoD identity, supplier-vs-distributor seat split.
- **Interval billing / AMI-era extensions**; embedded MDM modules (Itineris ships MDM inside the CIS suite — packaging, not identity).
- **ERP integration depth**: purpose-built subledger (SAP FI-CA) vs standalone GL integration vs multi-fund government accounting (Cayenta).
- **Suite composition**: CIS+CRM+ERP on one platform (Itineris); CIS+work+financials+HCM (Cayenta); CIS+portal+mobile workforce (NorthStar); ERP-embedded (SAP).
- **Deployment** (cloud/on-prem/hosted), **AI layers** (Copilot-era), **contact-center add-ons** (voicebot/chatbot).

### L3 — Vendor-specific (Research Notes only)

- Oracle: the "V" diagram and object names (Person/Account/Service Agreement/Premise/Service Point); To Do processing; Job Streams (batch scheduler); Landlord Reversion; Premise Replicator; call summary/call tagging.
- SAP: business partner / contract account / contract trio; connection object / installation / PoD vocabulary; UPIL (Utilities Product Integration Layer); Interaction Center WebClient; parked documents; fast move-in/out naming.
- Itineris: UMAX Manage/Grow/Engage/Serve/Maintain/Empower module names; Broker Management with Letters of Authority; Market Interaction; UMAX Real-Time (dynamic pricing, imbalance management).
- Cayenta: suite composition with HCM; multi-fund accounting framing.
- NorthStar: SilverBlaze portal; personalized video engagement.

## Vendor-specific Findings

- Oracle's Case Management is explicitly a **separate, turn-off-able module** whose behavior is "controlled by your implementation" — care machinery is standard structure at this pole but modular, not monolithic.
- Oracle's customer contacts are **person-based or premise-based** and serve "audit and statistical purposes" — the contact log is an instrument of record, not just a UI trail.
- SAP's PoD exists specifically because "in a deregulated market… it becomes important to uniquely identify service point" — deregulation machinery is a market-structure variant.
- Itineris separates CIS from CRM as module families but ships them "natively integrated" — the strongest architectural statement that the care layer belongs to the same system of record.
- Itineris ships an EV-operator back-office as a **separate sector** from its energy/water utility CIS — corroborates the EV-charging seam recorded by the utility-billing pass.

## Boundary Findings

1. **vs Utility Billing Platform (processed sibling — the central question). DISCHARGED: keep-both RATIFIED from this side.** The sampled CIS products carry the full family L0 (service accounts × meters × bills × money × service orders) — the CIS name is not a care-only system without billing. The billing-led products (MuniBilling, Springbrook) carry the same L0 without the enterprise care breadth. The honest seam is the **organizing emphasis**: at the billing-led pole the meter-to-bill-to-money cycle is the spine and the customer record serves the money cycle; at the CIS pole the customer/service relationship is the spine and billing is one function within a broader care-and-commercial operation. The naming correlates with tier (CIS name at enterprise/mid-market suites; utility-billing name at small/municipal) — a market-positioning observation held at moderate strength. L0 shared; difference is emphasis, L1/L2 breadth, and tier. Both leaves stay.
2. **vs Outage Management System (processed). DISCHARGED.** Oracle's customer contacts record "when and why a customer contacted your company" — interaction logging against customer records, no network-model prediction. This is exactly the below-Type pole the OMS pass flagged: a CIS call/contact log is trouble-call logging, not outage management; the CIS is the customer-identity/phone/service-point data source the OMS consumes. No conflict.
3. **vs Gas Utility Management (processed). DISCHARGED.** The vertical-edition framing holds from this side: Cayenta lists Electric/Water/Gas/Fiber industries; Itineris serves energy/water sectors; Oracle is multi-commodity. The commodity verticals are the same L0 + domain binding; this leaf is the horizontal family.
4. **vs Meter Data Management System (processed).** MDMS holds billing-quality data (VEE, bill determinants) and publishes them *to* billing/CIS; the CIS consumes reads and exists for the customer/money relationship. Itineris embedding an MDM module inside its CIS suite is packaging, not identity.
5. **vs generic CRM (§07).** The CIS carries CRM-shaped care machinery, but its spine is the served-premise service account with metered consumption and the money cycle; a generic CRM has no premise/meter/bill structures, and the CIS's care objects are utility-shaped (high-bill complaints, bankruptcies, premise inspections, market messages). Remove the utility machinery → generic CRM + billing, not a CIS.
6. **vs Subscriber Management (telecom, processed).** The telecom analog holds a subscriber population + service state + lifecycle status, but its identity substrate and service semantics are connectivity-based (E.164/IMSI/account numbers), not premise-anchored metered service. Adjacent analog, different family.
7. **vs Utility Field Service Management (unprocessed).** Forward note: service orders bound to service accounts (this leaf) vs crew/workforce machinery in its own right (that leaf). Same seam the billing pass recorded.
8. **vs Customer Portal / Customer Energy Management.** The portal is the customer-facing surface layer of the same records; the CIS is the operator-side system of record. No transactions of record originate in the portal layer.
9. **"Remove what to become another Type" summary**: remove the money cycle → care CRM over utility customers; remove metered consumption → fee-based billing/generic Billing Platform; remove the service-account spine → a billing engine component; remove the utility binding → generic CRM; move the organizing spine to the money cycle and shrink the care layer → the billing-led pole (sibling leaf, same family).

## Uncertainties

1. **NISC unreachable** (timeouts ×2 across passes) — the co-op-tier CIS pole is unverified first-hand; no claims drawn from it.
2. **Advanced Utility Systems unreachable this pass** (transport error ×2) — held at cross-pass corroboration strength from the gas pass.
3. **SAP help portal JS-rendered** — evidence taken from official SAP learning pages and indexed help-portal excerpts (A−); no precise transaction-level claims drawn.
4. **Tier/naming correlation** (CIS name ↔ enterprise/mid-market; utility-billing name ↔ small/municipal) is a market-positioning observation across two passes' samples, not a measured market census — moderate strength.
5. **Care breadth universality**: the enterprise care/commercial breadth (quotes, marketing, loans, appointments) is documented in depth at Oracle/SAP/Itineris but not at Cayenta/NorthStar at fetched depth — held as pole-typical, not universal.
6. Whether any CIS product ships **without** billing was not observed in the sample; the working finding (billing always inside the CIS family) is held at strong-but-not-absolute strength.

## Final Synthesis

The Utility Customer Information System is the utility operator's **customer-and-service system of record** — the same application family as the Utility Billing Platform, held under the **customer-care-led pole**. Its defining core is the family's three jointly-held structures: the served-premise service account of record, the metered-consumption basis, and the meter-to-bill-to-money cycle. What distinguishes this pole is the organizing emphasis and the breadth around the spine: the customer relationship (persons/organizations with multiple accounts, premises, hierarchies) is the system's center; the care operation (logged contacts, cases, correspondence, service requests, appointments) is first-class; commercial extensions (quotes, sales & marketing, loans) hang off the same record; and billing runs as one function inside the customer relationship rather than as the system's defining rhythm. The name dominates the enterprise and mid-market suite tier; the utility-billing name dominates the small/municipal tier; both denote one structure. Keep-both with the sibling is ratified; the CIS document describes the family from the customer-care-led side.
