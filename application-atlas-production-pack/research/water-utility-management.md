# Research Notes — Water Utility Management

## Research Goal

Understand what "Water Utility Management" is as an Application Type: what system (or assembled family of systems) a water utility — a municipal water department, water district, rural water cooperative, water authority, or investor-owned water company — runs to manage its service business; what objects live inside it; what work flows through it; who uses it; and where its boundaries lie against the already-processed horizontal utility family (billing, CIS, asset, field service, GIS, rate, revenue assurance, AMI/MDMS), the processed commodity verticals (gas-utility-management, wastewater-utility-management), and the processed water siblings (water-quality-management, water-network-monitoring).

This pass discharges the forward note left by the wastewater-utility-management pass (2026-09-10): "keep the three commodity verticals (gas/water/wastewater) consistent; the wastewater binding's distinct content is the connection-based service, the derived charge basis, and the estate/regulatory context" — and the gas pass's flag: "vs Water Utility Management (water leaf unprocessed) — same family structure over a different commodity… Flag for the water pass: expect the same vertical-edition pattern."

## Initial Boundary

The leaf sits in DIRECTORY §19 (Energy, Utilities & Telecommunications) in the water cluster: Water Utility Management, Water Network Monitoring (processed 2026-09-10), Water Quality Management (processed 2026-09-10), Wastewater Utility Management (processed 2026-09-10), Wastewater Compliance Management (processed 2026-09-10).

Neighbors:

- Horizontal §19 family (all processed): utility-billing-platform, utility-customer-information-system-cis, utility-asset-management, utility-field-service-management, utility-gis, utility-rate-management, utility-revenue-assurance, AMI, MDMS. The billing pass's Related Types table already names "Gas / Water Utility Management | commodity verticals | the same structure anchored on one commodity's domain and market structures; this leaf is the horizontal family."
- Commodity verticals: gas-utility-management (processed 2026-09-08 — the gas utility's customer-service business system of record; the ratified vertical-edition template), wastewater-utility-management (processed 2026-09-10 — the sewer-service vertical; its Related Types row expects this leaf as "same family, sibling commodity… water and sewer are commonly billed by the same products on one account").
- Water siblings: water-quality-management (the quality program of record — its table says "Water Utility Management | the customer-service business system (accounts, charges, bills); no object overlap with the quality program"), water-network-monitoring (the network operations watch — its table says "Water Utility Management | sibling vertical | the utility's customer-service business system of record (accounts, charges, bills); this leaf is the operations watch over the network").

Working hypothesis (from the ratified family pattern): Water Utility Management = the water utility's customer-service business system of record — served-premise service accounts, the utility's own metering population and measured consumption, the meter-to-bill-to-money cycle, service orders — realized in the market by utility CIS/billing products deployed for water, with water-specific furniture (conservation-oriented rate shapes, leak/high-usage alerts, co-billed sewer/stormwater lines deriving from the same reads).

Known risks: (a) the market label "water utility management" is loose — used across billing/CIS products, operations products, network monitoring, and quality programs (the wastewater pass documented the identical umbrella finding); (b) water and sewer are co-realized by one product population, so the leaf's distinct content must be argued carefully; (c) unmetered flat-rate water billing exists as an older/regional pattern and must be handled in the historical check.

## Research Questions

1. What does a water utility actually operate and sell? (source, treatment, distribution, served premises, metered water)
2. What software does the market sell under the "water utility management" label, and what does each product actually hold?
3. Is the market label ONE coherent Application Type or an umbrella over several software families?
4. Does the ratified commodity-vertical pattern (gas = customer-service business system of record) hold for water?
5. What is actually water-specific: the metering population, rate shapes (tiered/conservation/seasonal), leak/high-usage alerts, conservation engagement, co-billing as the host account?
6. How does the water account relate to sewer/stormwater/refuse lines on the same account, and to the reads that drive them?
7. Where do the distribution estate, water quality, network monitoring, meter-data infrastructure, and customer engagement sit relative to this Type?
8. Would older / regional / differently-positioned products (paper-era billing offices, unmetered flat-rate undertakers, rural cooperatives, European drinking-water companies) still fit the definition?

## Representative Products

Sampled across the poles the market label covers (different tiers, geographies, and product philosophies; inherited evidence marked):

| Product | Pole | Tier / geography | Evidence |
|---|---|---|---|
| Muni-Link | water-led utility billing/CIS (water, sewer, stormwater) | small municipal / rural water (North America) | A — water page fetched this pass; CIS/billing/product pages inherited from wastewater pass (fetched 2026-09-10) |
| Itineris — UMAX | enterprise water CIS/CRM/ERP; dedicated water sector | enterprise; North America + Europe (drinking-water companies) | A — water sector page + customer-platform page fetched this pass; BWSC case inherited (Tier-3, wastewater pass) |
| VertexOne (VXcis + VXconnect; watersmart.com now redirects here) | water CIS + customer engagement/conservation platform | municipal water utilities, water districts (US) | A — home + water-industry page fetched this pass |
| Oracle Utilities — Customer Care and Billing | enterprise customer care & billing; "electricity, natural gas, and water utilities worldwide" | enterprise, worldwide | A — inherited from gas pass (docs fetched 2026-09-08) |
| Advanced Utility Systems — CIS Infinity | mid-market multi-commodity CIS/UB ("electric, water, gas, and multi-service providers") | mid-market (North America/Caribbean) | A — inherited from gas pass (pages fetched 2026-09-08) |
| Springbrook — Cirrus Utility Billing | small-municipality government UB; lists "water, sewer, electric, refuse and allocation water" | small municipal (US) | A — inherited from gas pass (page fetched 2026-09-08) |
| MuniBilling | modern cloud UB (supporting) | small utilities/municipalities | A — inherited from gas pass (homepage fetched 2026-09-08) |

Boundary poles (researched to establish the boundary, not members):

| Product | Pole | Evidence |
|---|---|---|
| iWorQ — Water System Management | asset inventory + maintenance over the water estate (lines, hydrants, valves, structures); NO billing, NO customer accounts | A (search-snippet of official page, this pass) |
| Sedaru | water/collection field operations, GIS-connected | UNREACHABLE (2 transport failures in the wastewater pass — not retried per network rule); Tier-3 only (press: "connect organizational data, systems and people across the water enterprise… Esri ArcGIS, Cityworks CMMS and hydraulic model") |
| Hach WIMS / water-quality products | plant data + quality compliance | processed sibling Types (water-quality-management pass) |
| Water network monitoring products | live network condition + leak/burst events | processed sibling Type (water-network-monitoring pass) |

Tier-3 corroboration: NYC DEP UMAX launch (Itineris news page, fetched this pass); Mount Pleasant Waterworks billing/AMI/portal case (inherited, Wastewater Digest); SAP Best Practices for Water Utilities (inherited: "call center management, meter-to-cash operations, integrated work management, customer financial management, consumption data collection, connections and device management and consumption billing").

## Sources

Fetched this pass (2026-09-10):

- Muni-Link — Water page: https://muni-link.com/water (fetched; page includes the literal heading "Water Utility Management")
- Itineris — UMAX for water utilities: https://itineris.net/global/sectors/water-utilities/ (fetched); UMAX Customer Platform: https://itineris.net/north-america/solutionsforutilities/umax-customer-platform/ (search snippet); NYC DEP launch: https://itineris.net/nycdep-modernizes-operations-with-umax/ (linked from fetched page)
- VertexOne — home: https://www.watersmart.com/ (redirects to https://www.vertexone.ai/home, fetched); Water industry page: https://www.vertexone.ai/solutions/industries/water (fetched, titled "CIS & Billing Software for Water Utilities")
- iWorQ — Water System Management: https://iworq.com/systems/water-system-management-software/ (search snippet; direct URL guess 404)

Inherited evidence (recorded in prior passes' research notes, fetched on their dates):

- Muni-Link home/CIS/billing/product pages (wastewater pass, 2026-09-10): https://muni-link.com/ , https://muni-link.com/features/customer-information-system/ , https://muni-link.com/features/billing/ , http://muni-link.com/products/utility-billing-software
- OpenGov Utility Billing (wastewater pass, snippet-level): https://opengov.com/products/utility-billing
- Oracle Utilities CCB docs (gas pass, 2026-09-08): https://docs.oracle.com/en/industries/utilities/ , https://docs.oracle.com/en/industries/utilities/customer-care-billing/index.html , https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/CCB_BP_Intro.html
- Advanced Utility Systems CIS Infinity (gas pass, 2026-09-08): https://advancedutility.com/ , https://advancedutility.com/solutions/customer-information-systems/
- Springbrook Cirrus Utility Billing (gas pass, 2026-09-08): https://www.springbrooksoftware.com/solutions/utility-billing/
- MuniBilling (gas pass, 2026-09-08): https://munibilling.com/
- BWSC/Itineris case (wastewater pass, Tier-3): https://www.wwdmag.com/utility-management/article/11004078/updating-oldest-us-water-sewer-system-with-newest-software
- Mount Pleasant Waterworks case (wastewater pass, Tier-3): https://www.wwdmag.com/utility-management/article/33010188/new-billing-system-alleviates-bottlenecks-for-a-south-carolina-utility
- Sedaru Tier-3 (wastewater pass): Eagle River press https://www.wwdmag.com/utility-management/news/10931306/colorado-utility-selects-software-platform

Unreachable this pass: itineris.com (JS error), iworq.com water URL guess (404 — corrected via search snippet), oracle.com/utilities/water (404; Oracle evidence inherited from the gas pass's docs.oracle.com fetches instead). Sedaru not retried (2 prior failures, network rule).

Research date: 2026-09-10.

## Product Observations

### Muni-Link (water-led municipal/rural billing CIS) — evidence layer A

- Water page (fetched this pass): "Cloud-Based Water Billing Software for Rural Utilities"; "Muni-Link is a cloud-based utility CIS that automates billing workflows, supports complex rates, and provides secure online payments and a customer portal"; "Built with input from water and sewer utility design partners."
- Rate furniture (water page): "tiered and seasonal rates, sewer calculations, minimum charges, adjustments, notices, delinquency workflows, and reporting"; "Tiered, seasonal, and residential/commercial rate structures"; "Sewer billing logic, minimum charges, adjustments, and misc. charges"; "miscellaneous charges table to customize bills."
- The page's own H2: "Water Utility Management" — "Billing processes for utilities can be complex… Water and sewer utilities face several challenges regarding billing, including: Complex Rates: multiple tiers, seasonal variations in pricing, and differing rates for commercial and residential customers… Customer Base: Water utilities serve a large customer base… Integration: The billing process interconnects with other systems, like customer communication and notifications." Direct evidence that the market phrase "water utility management" names the billing/CIS system.
- Inherited (wastewater pass): CIS "Account Central" one-screen account hub — "account details, usage history, service orders, and notifications"; "balances, transactions, and payment plans"; "usage and meter readings for water, sewer, and stormwater"; service orders "past or present, associated with a customer account"; "Generate or Import Meter Readings — automatically pull readings from your meter reading software or import them manually"; billing cycles "monthly, quarterly, or bi-monthly"; delinquency: "Generate shutoff service orders in bulk. System automatically cancels orders if a customer pays and creates orders to restore service when accounts are made current"; integrations with "asset management, accounting, GIS, and AMR/AMI systems"; modules include Backflow inspection manager, Loans, Stormwater; customers: "municipal utilities, utility authorities, water districts, and regulated utilities."
- Reading: water-led CIS where the water account is the host and sewer/stormwater ride as lines; the money↔service-state coupling (shutoff/restore service orders) is explicit.

### Itineris — UMAX (enterprise water CIS/CRM/ERP; international) — evidence layer A

- Water sector page (fetched this pass): "UMAX for water utilities"; "Water utilities face increasing pressures from climate change, water scarcity, and network leakages. Ensuring a reliable water supply for the future makes water conservation more critical than ever. At the same time, utilities must deliver exceptional customer service while optimizing operations and efficiency."
- "Streamline and automate billing, customer management, and field services"; "Equip your CSRs with real-time data, AI-powered self-service, and omnichannel capabilities"; "To focus on your core business – supplying water – administrative processes must run smoothly, efficiently, and with high automation."
- Family footer: "UMAX supports accurate conversion of meter readings to bills, with extensive customer and field service support capabilities."
- Customer Platform (search snippet): "meter-to-cash capabilities, streamlining billing, customer management, and revenue processes"; Billing Management: "Generate accurate bills and invoices with full billing cycle support, from advanced reads processing to bill production"; Payment & Collections; CSR 360° view; field services.
- Integration posture: "connect effortlessly with your existing systems… SCADA systems, IoT sensor data, weather forecast APIs, smart meter data" — adjacent systems named as integrations, not held objects.
- Water customer base (logos on fetched page): NYC DEP, Boston Water and Sewer Commission, Arizona Water Company, Gwinnett County, Cobb County, Manatee County, Fort Worth, Broward County, Baltimore, Tallahassee, Lansing Board of Water & Light, Regional Water Authority, Cape Fear Public Utility Authority, Georgetown Utility Systems, City of Dallas — and European drinking-water companies Evides, Dunea, De Watergroep, Waterbedrijf Groningen.
- NYC DEP launch (news page linked): "We have successfully launched our cloud-based Customer Information Solution, UMAX, at The New York City Department of Environmental Protection (DEP)."
- Microsoft Marketplace listing (search snippet): "UMAX fits standalone and multi-service utilities providing electric, gas, heat, and water in both investor-owned (commercial) and municipal/city environments."
- Inherited (wastewater pass, Tier-3 BWSC case): "65,000 reads were received, 22,000 bills were created, and $11 million in payments were received" in the first week; "2,400 service orders within the first week"; account structure "supports multiple services on one account, such as master accounts, landlord accounts and consolidated billing."
- Reading: the enterprise water pole — same family structure (reads→bills, payments, service orders, CSR account view) at the largest scale, international breadth including European drinking-water undertakers.

### VertexOne (water CIS + customer engagement platform; watersmart.com heritage) — evidence layer A

- Home (fetched via watersmart.com redirect): "We connect water, gas, and electric utilities, retailers, and energy service providers to their customers and their business operations"; products VXcis ("Billing and CIS"), VXconnect ("Personalized digital experiences, built for utility customers"), MyMeter ("Empower customers with real-time energy insights"), VXsmart ("Advanced analytics and smart meter insights").
- Water industry page (fetched, titled "CIS & Billing Software for Water Utilities"): "Water service should feel seamless—but when something breaks, billing spikes, or trust slips, the impact is immediate"; "With proactive alerts, plain-language billing, and self-service that actually serves, they're reducing call volume, guiding conservation, and making it easier for every customer to stay informed."
- Water client quotes (fetched page): City of Bullhead — "a customer can now go online and see how much water they use in a given day"; EBMUD — "speed, automation, and lower cost of presenting water use information and services to our customers"; Hendersonville TN case — "40% of customers use the data analytics provided by our portal, reducing the burden on customer-facing staff."
- Water client logos: San Antonio Water System, DC Water, EBMUD, EPCOR, Irvine Ranch Water District, Mount Pleasant Waterworks, Fort Wayne, San Jose, Pinellas County, Tempe, Billings, Pocatello.
- Reading: the customer-engagement/conservation pole — usage visibility, proactive alerts, conservation guidance layered over the water account; the same vendor also ships the CIS/billing spine (VXcis). The engagement layer is a capability layer and a standalone-product pole, not a different object model. (WaterSmart, the heritage brand of this pole, now redirects here — the engagement pole has been absorbed into a CIS+engagement platform.)

### Oracle Utilities — Customer Care and Billing (enterprise; inherited from gas pass) — evidence layer A

- "Oracle Utilities provides best-in-class solutions to improve reliability, service, and safety for electricity, natural gas, and water utilities worldwide" — water a first-class served industry.
- CCB: "a customer care and billing system for traditional scalar devices and billing processes… supports one to many utility service types"; REST API: "retrieve customer information details, including meter, financial, and usage information."
- Business User Guide section tree: Customer Information · Premise Management · Meter Management · Meter Reading · Service Orders · Billing · Payments · Adjustments · Credit & Collection · Financial Transactions · Deposits · Statements · Rates · Non-Billed Budgets · Overdue Financial Obligations · Interval Billing · Reports — the enterprise-pole functional taxonomy of exactly the customer × premise × meter × read × bill × money cycle.
- Reading: the enterprise pole documents the family structure with water among the served commodities; service-type-neutral machinery, water carried by the domain binding.

### Advanced Utility Systems — CIS Infinity (mid-market; inherited from gas pass) — evidence layer A

- "a comprehensive customer information system and utility billing platform designed to meet the evolving needs of electric, water, gas, and multi-service providers"; "proven performance across 134 utility companies and 6.6 million customer service points"; "Meter-to-Cash Data in One Place … every aspect of the revenue cycle — from meter reads and billing to payments and collections — centralized within a single platform"; Mobile Workforce Management (service order creation → dispatch → completion with notes/photos/signatures flowing back); "supporting complex rate structures"; portal/SMS/AI/BI layers.
- Reading: the mid-market multi-commodity pole; the vendor's own population unit is the "customer service point."

### Springbrook — Cirrus Utility Billing (small-municipality; inherited from gas pass) — evidence layer A

- "comprehensive water, sewer, electric, refuse and allocation water billing capabilities"; "Complete 'meter-to-cash' solution"; "flexible billing — handles tiered rates, winter averaging and credit-based deposits"; "Unlimited Meters & rates per account"; "Full meter management"; "Integrated service requests"; "Integrated past dues and collections"; full general-ledger integration.
- Reading: the small-municipality pole carries the full water visit economy; "allocation water" and "winter averaging" are water-specific billing classes named by this vendor (product-specific; meaning not researched).

### MuniBilling (small cloud pole; inherited from gas pass) — evidence layer A (supporting)

- Cloud UB with Mobile Service Order Management, Mobile Meter Reader, Customer Portal, "real time reporting… into Accounts Receivable, Billing, Customer Accounts, Meters, and Payments" — the modern cloud pole's object vocabulary matches (accounts, meters, payments, AR).

### iWorQ — Water System Management (boundary pole: asset/maintenance) — evidence layer A (search snippet)

- "Easily track your water asset inventory and maintenance… Map and maintain your water lines, structures, hydrants, valves, and more"; "Record and schedule maintenance… Track cleaning, inspections, and repairs along with date, cost, and time"; "Integrate with iWorQ Work Management"; "Use GIS data or manually map assets"; "Manage asset information including attributes, cost, value, location, and maintenance history"; "Generate reports for improving decisions on repairs, replacements, and budgeting."
- Reading: NO billing, NO customer accounts, NO meters-as-billing-devices. This is the public-works asset-management family deployed for the water estate (iWorQ also ships sewer, stormwater, pavement, signs modules). Confirms the estate boundary.

### Sedaru (boundary pole: water field operations) — UNREACHABLE; evidence layer C (Tier-3 only, inherited)

- Eagle River press (inherited): "real-time solution to connect organizational data, systems and people across the water enterprise… connect its Esri ArcGIS, Cityworks CMMS and hydraulic model in real-time with office and field staff."
- Reading: the water-operations pole is field-work/GIS-connected operations software over the water estate — the horizontal asset/field family's territory with water-specific programs. Held at Tier-3 strength only.

### Tier-3 corroboration (inherited)

- Mount Pleasant Waterworks (water AND wastewater utility): billing/payments modernization; "AMI + portal notify customers of usage issues"; paperless billing; self-service — the leak/high-usage alert layer over the account.
- SAP Best Practices for Water Utilities (2005): CIS for "small and midsize water and wastewater utilities": "call center management, meter-to-cash operations, integrated work management, customer financial management, consumption data collection, connections and device management and consumption billing."

## Cross-product Comparison

| Structure | Muni-Link | Itineris UMAX | VertexOne | Oracle CCB | Advanced CIS Infinity | Springbrook Cirrus | MuniBilling | iWorQ Water | Sedaru |
|---|---|---|---|---|---|---|---|---|---|
| Served-premise service account | ✓ (Account Central) | ✓ (CSR 360° account view) | ✓ (VXcis) | ✓ (Customer Information/Premise) | ✓ ("customer service points") | ✓ (Account overview) | ✓ (Customer Accounts) | — | — |
| Meters + reads + measured consumption | ✓ (generate/import reads; water/sewer/stormwater readings) | ✓ ("accurate conversion of meter readings to bills") | ✓ (usage data; MyMeter insights) | ✓ (Meter Management + Meter Reading; "meter, financial, and usage") | ✓ (meter reads → billing) | ✓ (unlimited meters; full meter management) | ✓ (Mobile Meter Reader; Meters reporting) | — | — |
| Rates → bill → money cycle | ✓ (tiered/seasonal; delinquency workflows) | ✓ (billing cycles; payment & collections) | ✓ (VXcis billing) | ✓ (Rates/Billing/Payments/Deposits/Credit & Collection) | ✓ (complex rate structures; revenue cycle) | ✓ (tiered rates, winter averaging, deposits, past dues) | ✓ (AR/Billing/Payments) | — | — |
| Service orders (office↔field) | ✓ (shutoff/restore bulk orders) | ✓ (field services; 2,400 orders first week at BWSC) | ✓ (via VXcis suite) | ✓ (Service Orders) | ✓ (MWM dispatch→completion flow-back) | ✓ (integrated service requests) | ✓ (Mobile Service Order Management) | work orders over assets | ✓ (field work, Tier-3) |
| Multi-service lines on the water account | ✓ (water, sewer, stormwater) | ✓ (multi-service; master/landlord accounts) | ✓ (multi-service platform) | ✓ (one to many service types) | ✓ (multi-service providers) | ✓ (water, sewer, electric, refuse, allocation water) | ✓ | — | — |
| Customer engagement / usage visibility / alerts | portal + notifications | AI self-service; omnichannel | ✓✓ (core pole: proactive alerts, conservation guidance, daily usage) | companion CX cloud services | portal + SMS + engagement | online payments | Customer Portal | — | — |
| Water estate as assets (lines, hydrants, valves) | — (integrated, not held) | — (integration posture) | — | — (Asset Inventory section exists; estate in WAM family) | — | — | — | ✓ | ✓ (Tier-3) |
| Network live condition / leak-burst events | — | — | — | — | — | — | — | — | — (water-network-monitoring territory) |

Reading: the billing/CIS pole (Muni-Link, Itineris, VertexOne VXcis, Oracle CCB, Advanced, Springbrook, MuniBilling — plus the Tier-3 family: BWSC/Itineris, Mount Pleasant, SAP) carries ONE coherent structure — the utility customer-service business system — deployed for water. The other poles carry different structures with no shared defining core. The market label "water utility management" is an umbrella over the utility's assembled software estate; Muni-Link's own water page uses the phrase as a heading over billing content.

## Canonical Model (four abstraction layers)

### L0 — Defining Invariant

The water utility's customer-service business system of record — the family's three jointly-held structures bound to drinking-water service:

1. **The served-premise service account of record** — persistent identified account binding a customer to a served premise's water service, carrying service state + financial standing, operated open→sustain→close through service actions, accumulating consumption/bills/payments/arrears. Remove → CRM contact base / generic billing account.
2. **The metered-consumption basis over the utility's own metering population** — meters bound to the account's service points, periodic reads (manual route reads, estimates, remote/AMI feeds as implementations) accumulating measured usage per billing period, meter identity and lifecycle (installation, exchange, test) held in the system. The water meter is the family's reference device: these same reads commonly drive the co-billed sewer/stormwater charges. Remove → fee-based billing / MDMS territory.
3. **The meter-to-bill-to-money cycle** — recurring bill production converting consumption into charges under configured rates (tiered/seasonal shapes the standard water furniture), the bill as the authoritative lifecycle-managed amount-due record, payments/adjustments/deposits/arrears/budget plans/collections tracked on the same account. Remove → meter-reading tool or ad-hoc invoicing.

Plus the family's service-order instrument (office↔field work binding money state to physical service state: turn-ons, turn-offs/shutoffs, meter sets/exchanges/tests, leak/high-bill investigations, re-reads).

Binding: the service is **drinking-water service** — potable water the utility produces/treats and delivers through its treatment-and-distribution estate to served premises. The estate itself is held in adjacent systems and enters this system as the delivery context of served premises (the gas leaf's own exclusion, applied here).

Jointly-held load-bearing: (1 alone = CRM/generic billing; 2 alone = MDMS/AMI territory; 3 alone = generic billing engine [the §08 Billing Platform spine]; 1+2 without 3 = meter ops with no revenue loop; 1+3 without 2 = fee-based billing; 2+3 without 1 = billing engine over meter data, a component not a category).

### L1 — Common Mature Structure

- customer portal (balances, usage, bills, payments) and notifications (email/SMS)
- payment machinery (online, autopay, processors); cash receipting; general-ledger integration
- AMR/AMI integration for reads; interval-data extensions at the enterprise pole
- mobile service orders; delinquency workflows (notices → payment arrangements → shutoff → restoration)
- deposits tied to credit standing; budget (equal-payment) plans
- reporting/dashboards over consumption, revenue, arrears
- role-based permissions; multi-service account composition (water + sewer + stormwater + refuse on one account)
- usage visibility and proactive alerts to customers (high-usage/leak-class alerts where AMI feeds exist)

### L2 — Variant / Optional Structure

- **Service composition**: water-only utilities vs water as the host account for sewer/stormwater/refuse (the dominant co-billing pattern; the water reads drive the derived sewer charges)
- **Operator type**: municipal department, water district/authority, rural water cooperative (Muni-Link's rural tier), investor-owned water company (Arizona Water Company), metropolitan utility (NYC DEP), European drinking-water undertaker (Evides, Dunea, De Watergroep)
- **Rate furniture**: tiered/conservation-oriented blocks, seasonal rates, residential/commercial classes (cross-product); allocation water and winter averaging (Springbrook, product-specific); budget-based rate structures NOT evidenced in-sample
- **Customer engagement depth**: portal-only vs engagement platforms with daily usage, proactive alerts, conservation guidance (VertexOne pole; WaterSmart heritage absorbed into it)
- **Water-side companion programs**: backflow/cross-connection inspection management (Muni-Link module, product-specific)
- **Scale tier**: rural/small-municipality packages → mid-market → enterprise (NYC DEP); the core is stable across the range
- **Deployment**: cloud vs on-premise
- **Metering era**: manual route reads vs AMI/interval feeds

### L3 — Vendor-specific (Research Notes only)

- Muni-Link: Account Central one-screen design; Backflow inspection manager; Loans; Stormwater modules; "Forever Support" packaging; Utility Websites.
- Itineris: UMAX on Dynamics 365/Azure; UMAX Real-Time (dynamic pricing, imbalance management — energy-market machinery); Opinum acquisition (data platform); One-V update methodology (inherited).
- VertexOne: VXcis/VXconnect/VXsmart/MyMeter product split; watersmart.com redirect (WaterSmart heritage absorbed); Hendersonville/Bullhead/EBMUD case metrics (marketing claims — not asserted).
- Oracle: "scalar devices" framing; Non-Billed Budgets; Overdue Financial Obligations; Interval Billing section names.
- Advanced: "6.6 million customer service points"; Infinity BI; SOC 2/StateRAMP.
- Springbrook: "allocation water" billing class; "winter averaging"; Cirrus brand.
- MuniBilling: Mobile Service Order Management / Mobile Meter Reader feature names.

## Anti-overfit Register

- **AMI/MDMS infrastructure** — NOT definitional. Manual route reads and estimated billing satisfy the core; the paper era passes. Meter-data platforms are adjacent infrastructure (the horizontal passes' own holding).
- **Conservation rate shapes (tiered/increasing block, seasonal)** — standard water rate furniture, NOT definitional: they are configurations of the same rates→bill machinery; flat-rate water exists as a variant (see historical check).
- **Leak/high-usage alerts, usage portals, conservation engagement** — modern capability layer and a standalone-product pole (VertexOne/VXconnect, WaterSmart heritage), NOT definitional. The customer seat is adjacent (mirrors Customer Energy Management for electricity).
- **Backflow/cross-connection programs** — adjacent compliance program over plumbing/external parties; appears as a module in one sampled product (product-specific).
- **Water loss / non-revenue water accounting** — revenue-assurance and network-monitoring territory, not the customer system's object set.
- **The distribution estate (source, treatment, mains, hydrants, tanks) as managed objects** — NOT definitional; held by the horizontal asset/field family (iWorQ water page, Sedaru-class) and the network siblings. Enters this Type only as delivery context.
- **Water quality compliance (sampling programs, standards, reports)** — the water-quality-management Type; no object overlap (that pass's own boundary row).
- **Network live condition / leak-burst events** — the water-network-monitoring Type; here a customer-side leak surfaces as a high-usage alert or bill dispute, not a network event.
- **Multi-service breadth** — variant, not definitional; the sampled products are multi-service and the water line is the binding.
- **Portal/payments/notifications/mobile/GL** — standard mature structure, not definitional (paper-era billing office satisfies the core).
- **AI features (self-service agents, semantic search)** — era-current layer in current pitches (Itineris, Advanced), not definitional.

## Historical / Market-Sample Check

- **Paper-era water billing office** (mid-20th century municipal water department): ledger card per served premise/customer + meter route books with periodic reads + rate schedule (flat or tiered) + receipt ledgers + turn-on/shutoff orders + past-due notices — satisfies all three legs at analog level. PASS.
- **1990s desktop utility-billing packages**: same three legs digitally. PASS.
- **Rural water cooperative / small town system** (Muni-Link's own stated tier: "Rural Utilities"): metered accounts, small population, simple rates. PASS.
- **Enterprise metropolitan water utility** (NYC DEP/Itineris; BWSC): same legs at scale with master/landlord account structures. PASS.
- **European drinking-water undertaker** (Evides, Dunea, De Watergroep, Waterbedrijf Groningen via Itineris): same legs under a different national regime. PASS — the definition names no regime-specific machinery.
- **Unmetered flat-rate water undertaker** (pre-universal-metering regional patterns; some small systems): fits legs 1+3 with the charge basis as premise/unit rather than measured volume. NOT directly sampled this pass — recorded as a variant/uncertainty, consistent with the wastewater pass's flat-rate leg and the horizontal pass's "non-metered fee components a standard companion" holding. The dominant and defining water pattern is the metered one; the unmetered pattern is the documented edge.
- The L0 names no metering technology, no protocol, no deployment form, no regime, no rate shape specific to one era or region. PASS.

## Boundary Findings

1. **vs wastewater-utility-management (§19, processed) — FORWARD NOTE DISCHARGED.** Same family L0, sibling commodity. Critically, water and sewer are commonly billed on ONE account by the SAME products (Muni-Link, OpenGov, Springbrook, Itineris/BWSC, SAP, VertexOne) — the two leaves are co-realized by one product population; the binding differs. Water's distinct content: the utility's OWN metering population as the charge basis (the family's reference metering case — sewer charges commonly derive from these same reads), drinking-water service (potable supply through the treatment-and-distribution estate), and the conservation/scarcity context (rate shapes, engagement). Wastewater's distinct content (per that pass): connection-based service, derived/flat charge basis, the collection/treatment estate context.
2. **vs gas-utility-management (§19, processed) — FLAG DISCHARGED.** Same family L0, sibling commodity; the gas pass's expected pattern holds. Differences observed: water has no observed supplier-seat/retail-competition split in-sample (the gas pass's Gentrack pole has no water counterpart in this sample — held as an uncertainty, not asserted); water's rate furniture is conservation-oriented (tiered/seasonal) vs gas's commodity-linked structures; water's metering population is the family's reference case.
3. **vs utility-billing-platform / utility-customer-information-system-cis (§19, processed)** — horizontal family; this leaf is the water vertical edition (the pattern the gas pass framed and the billing pass ratified: "Gas / Water Utility Management | commodity verticals"). The horizontal leaves hold the same record-layer machinery for any commodity; this leaf anchors it on drinking-water service and its metering/conservation context.
4. **vs water-quality-management (§21, processed)** — no object overlap: the quality program holds monitoring locations, parameters, standards, compliance evaluations, and regulator-facing reports; this leaf holds accounts, meters, bills, money. A utility runs both; they are different hats. (That pass's boundary row mirrored.)
5. **vs water-network-monitoring (§19, processed)** — the network watch holds the live network condition and drives leak/burst events to field response; this leaf runs the customer-and-money cycle. A customer-side leak surfaces here as a high-usage alert or bill dispute; the same physical leak surfaces there as a network event. (That pass's boundary row mirrored.)
6. **vs utility-asset-management / utility-field-service-management (§19, processed)** — the water estate (mains, hydrants, valves, tanks, structures) and its work programs are held there (iWorQ water page: asset inventory + maintenance, no billing). Here field work appears as service orders bound to service accounts. Meter identity/lifecycle is held in THIS system (meters exist to produce bills); the asset family may also carry meters as assets — a known family overlap the horizontal passes accepted.
7. **vs AMI / MDMS (§19, processed)** — meter-data infrastructure is adjacent; here the meter is grounded at accounts/premises and exists to produce bills. A deployment on manual reads is complete.
8. **vs utility-rate-management (§19, processed)** — rate design/modeling/analysis is adjacent; here rates are executed inside the bill cycle.
9. **vs utility-revenue-assurance (§19, processed)** — the leakage-control discipline over the meter-to-cash chain is adjacent; here the chain is run.
10. **vs customer-engagement platforms (VertexOne VXconnect pole; WaterSmart heritage)** — the customer seat: usage visibility, alerts, conservation guidance with no transactions of record; rides on the account. The same vendor may ship both the CIS spine and the engagement layer (VertexOne does). Held as an adjacent seat / capability layer, mirroring Customer Energy Management for electricity.
11. **vs Sedaru-class water operations products** — field ops/GIS-connected work management over the water estate = the horizontal asset/field family deployed for water (Tier-3 evidence only; vendor unreachable). Not this Type.
12. **UMBRELLA FINDING (the pass's central taxonomy observation)** — the market label "water utility management" is used across billing/CIS products (Muni-Link's water page carries the literal heading "Water Utility Management" over billing content), operations products (Sedaru-class, Tier-3), network monitoring (processed sibling), quality programs (processed sibling), and asset management (iWorQ water). No sampled product holds the whole estate. The leaf is therefore bound to the ratified commodity-vertical pattern (the utility's customer-service business system of record) and the umbrella reality is documented in the final document's Overview and Related Types.

## Uncertainties

1. **Unmetered flat-rate water billing** — a real historical/regional pattern (pre-universal-metering undertakers; some small systems), not directly sampled this pass. Held as variant/uncertainty; the metered basis remains the defining leg (consistent with the gas and horizontal passes).
2. **Budget-based (water-budget) rate structures** — plausible water-industry furniture but not evidenced in-sample; NOT asserted.
3. **Drought-specific rate/surcharge machinery** — seasonal rates evidenced (Muni-Link); drought-specific programs not researched.
4. **"Allocation water" and "winter averaging" (Springbrook)** — water-specific billing classes named by one vendor; meaning not researched; product-specific.
5. **Backflow inspection module (Muni-Link)** — single-vendor; product-specific.
6. **Water retail competition** — no supplier-seat evidence in-sample for water (unlike energy's Gentrack pole); whether any market moves the water customer system to a supplier seat is unknown; held as uncertainty.
7. **Sedaru unreachable (inherited, 2 failures)** — the water-operations pole rests on Tier-3 press/procurement evidence.
8. **Consumer-protection overlays** (shutoff restrictions, medical protections) — deposits/collections machinery evidenced at family strength; jurisdiction-specific programs not researched.
9. **VertexOne marketing metrics** (10X faster, 50% reduction, 30 hrs saved) — vendor claims, not asserted anywhere.

## Final Synthesis

Water Utility Management is the water utility's own customer-service business system of record: the served-premise service account (customer × premise × water-service state × financial standing), the metered-consumption basis over the utility's own metering population (the family's reference metering case — the same reads commonly drive co-billed sewer/stormwater charges), and the meter-to-bill-to-money cycle (recurring bills under configured rates — tiered/seasonal shapes the standard water furniture — with payments, deposits, arrears, budget plans, collections) — operated through service orders that bind money state to physical service state (turn-ons, shutoffs, meter sets/exchanges, leak investigations). The service being managed is drinking-water service: potable water the utility produces/treats and delivers through its treatment-and-distribution estate, which is held in adjacent systems (asset/field family, network monitoring, quality program) and enters this system as delivery context. The market realizes one family structure across every tier (rural water systems → small municipalities → mid-market → the largest metropolitan utilities) and across geographies (North America and European drinking-water undertakers); what varies is the service composition on the account, the rate furniture, the engagement layer, and the deployment. The market label is an umbrella over the assembled estate; this Type is its customer-and-money spine — the second commodity vertical of the ratified utility family pattern (gas → water → wastewater), and the co-realizing host of the wastewater sibling's derived charge basis.
