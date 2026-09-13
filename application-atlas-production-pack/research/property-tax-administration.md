# Research Notes — Property Tax Administration

## Research Goal

Understand, from real products, what a Property Tax Administration system (the government-side property tax billing and collection system — treasurer / tax collector software) actually is: its unit of record, its levy/billing machinery, its collection loop, its delinquency and tax-sale machinery, its distribution/settlement duty, its users and interfaces, and its boundaries against the neighboring §24 Types (Property Assessment System, Land Records / Cadastre, Tax Administration System, Government Revenue Management) and against adjacent Types (Utility Billing, payment platforms, mortgage-servicing escrow).

Two inherited obligations from prior passes:
1. Discharge the joint-review flag recorded by the land-records-cadastre-system pass (2026-09-08) and re-ratified by the property-assessment-system pass (2026-09-09): "one parcel spine, three operations — rights-of-record (land records) vs valuation (assessment) vs billing/collection (tax)". The assessment pass's forward note: "the seam is value-of-record vs money-of-record; the certified roll is the hand-off artifact."
2. Examine the Catalis "Property Tax Oversight" product line, flagged by the assessment pass as a possible state-oversight-agency variant.

## Initial Boundary

- The leaf sits in §24 Government, Public Sector & Civic, between "Property Assessment System" and "Tax Administration System".
- Initial hypothesis: the Type is the jurisdiction's system of record for property tax MONEY — levy application to taxable values, bills, payments, delinquency, distribution — not value (assessment) or rights (land records).
- Likely confusions: generic Tax Administration System (all tax types), Government Revenue Management (broader revenue accounting), Utility Billing (recurring service billing), payment gateways (rails), mortgage servicing (the escrow side), and the state-oversight variant.

## Research Questions

1. What is the unit of record — tax bill, tax account, parcel-year liability? How do amount, payments, charges, and status attach to it?
2. How do taxing entities, rates/levies/millage, and special assessments get configured and applied to produce a bill?
3. What is the bill lifecycle (calculation → bill run → print/mail → payment → delinquency → enforcement)?
4. How do payments arrive (counter, mail, bank tape files, escrow agents, online) and how are duplicates, refunds, and protested payments handled?
5. What happens on delinquency (penalties, interest, notices, liens, tax sales, bankruptcy)?
6. What flows in (taxable values / certified roll from assessment; ownership updates) and out (distributions to taxing entities, settlement reports, state reports)?
7. What interfaces do staff and the public face?
8. What roles exist (collector/treasurer, cashier, delinquency staff, taxpayer, escrow agent, taxing entities, state oversight)?
9. Do adjacent local taxes (business, tourist/occupancy, motor vehicle) live in the same system?
10. Where exactly are the boundaries with assessment, generic tax administration, utility billing, payment platforms, and mortgage servicing?

## Representative Products

Selected for market coverage, documentation accessibility, and different postures:

1. **DEVNET — Edge Billing & Collection** (devnetinc.com) — integrated land-records suite vendor; the Collector solution inside a suite spanning "appraisal to collection"; county collector base (e.g., Oakland County MI Treasurer testimonial).
2. **Aumentum Technologies — Aumentum Tax** (aumentumtech.com) — large multi-state suite vendor (ex-Thomson Reuters Aumentum); Tax Collection sold as a product line separate from Property Valuation; "1,000 governments across 39 states".
3. **Catalis — Tax Billing & Collections** (catalisgov.com) — North America (US + Canada) SaaS suite vendor; Billing & Collections beside CAMA, Escrow Payment Management, and Property Tax Oversight product lines.
4. **Grant Street Group — TaxSys** (grantstreet.com) — cloud-hosted tax collection specialist for large counties ("$50 Billion Taxes Collected, 27 Million People Served"); separate Payments (PaymentExpress) and Auctions (LienHub, DeedAuction) lines; clients include San Bernardino County CA, Cobb County GA, Bay County FL.
5. **Harris Govern — Property Tax & Collections** (harrisgovern.com) — multi-suite regional vendor (PACS / RealWare / OpenForms); serves both appraisal districts and tax offices; its public property-search directory lists separate "CAD" (appraisal district) and "TAX" (tax office) portals per Texas county — direct evidence of the organizational value/money seam.

Market anchors NOT sampled: Tyler Technologies (tylertech.com returned HTTP 403 twice in the sibling assessment pass; not retried per network rules), Vanguard Appraisals (transport error ×2 in the sibling pass). No claims about them beyond "exists as a major vendor".

## Sources

Fetched 2026-09-09 (all Tier 1 — official vendor pages):

- DEVNET — homepage: https://www.devnetinc.com/ ; Billing & Collection: https://www.devnetinc.com/billing-collections/
- Aumentum Technologies — homepage: https://www.aumentumtech.com/ ; Aumentum Tax: https://www.aumentumtech.com/tax-collection
- Catalis — Tax & CAMA family: https://catalisgov.com/tax-cama/ ; Billing & Collections: https://catalisgov.com/tax-cama/billing-collections/ ; Property Tax Oversight: https://catalisgov.com/tax-cama/property-tax-oversight/ ; Escrow Payment Management: https://catalisgov.com/tax-cama/escrow-payment-management/
- Grant Street Group — homepage: https://www.grantstreet.com/ ; Tax Collection / TaxSys: https://www.grantstreet.com/tax-collection
- Harris Govern — homepage: https://www.harrisgovern.com/ ; Property Tax & Collections: https://www.harrisgovern.com/tax-collection-software/
- Prior-pass context: research/property-assessment-system.md, applications/property-assessment-system.md, applications/land-records-cadastre-system.md (Related Types rows), IAAO General Assessment FAQs (quoted via the assessment pass)

## Product A — DEVNET Edge Billing & Collection

### Key observations (evidence layer A unless noted)

- Self-description: "The DEVNET Edge® Billing & Collection solution will allow for the collection of current and delinquent property taxes and the various political subdivisions that have an authorized property tax levy. The Collector solution performs all billing, collection, distribution, delinquent taxes, tax sales and maintenance processes pertaining to both real and personal property."
- Suite framing (homepage): "the entire property tax life cycle from appraisal to collection."
- Tax Calculation:
  - "Taxing body maintenance allows simple entry of taxing bodies and tax/millage rates"
  - "Easily associate multiple taxing bodies with real estate or personal property"
  - "Fast and accurate calculation of taxes including: TIF, Abatement, Special Assessments, Enterprise Zone, Bond Issues, Railroad, Utilities, Personal Property, Mobile Home, Oil and Gas, Watershed, Drainage, Commercial Surtax, School Tax, Per Capita and other Personal Tax, Reimbursements"
  - "Tax calculation reporting allows for taxing body and tax/millage rate level reporting by county or city"
- Billing, Collection, and Distribution:
  - "Quickly and accurately bills, collects, and distributes tax monies for taxing authorities within the jurisdiction."
  - "One tax collection program that will collect taxes for real estate, personal property, special assessments and surtax"
  - "Ability to bill and collect drainage, watershed and other special districts with the associated account"
  - "Processes regular, protested and refunded payments"
  - "Ability to calculate penalty, interest and assign special fees for collector"
  - "Laser Tax bills generated in desired formats along with paid tax receipts"
  - "Capability to produce collector's books, delinquent books and create delinquent bills"
  - "Processes court order additions, deletions, supplements, write-offs and waivers"
  - "Processes payments including merchant's license, tax sale publication costs, duplicate tax receipts, surtax, land sales"
  - "Software can be broken out by tax year, political sub-division and types of tax"
  - "Special assessments appear on tax statement"
  - "Interest, clerk fee, collector fee, and penalties can be figured by month and be printed on tax receipts for the entire year"
  - "Check generation"
  - "Bar coded tax bills for faster, easier and more accurate tax collection"
  - "Collection of tax bills include collecting by bar code, parcel number, bill number, owner name, and tax buyer name for fast entry of tax payments"
  - "Accepts tape payments from banks and other institutions"
  - "FAST tax distribution including check printing and automatic ACH transfers"
  - "Additions and abatements module for printing corrected tax bills"
  - "Interface with the County's existing financial system"
  - "Online Tax Collection; Disbursement Processing"
  - "Disbursement and settlement reporting of Real Estate, Personal Property, and Surtax countywide or by township when required"
  - "Reporting by district, county, and township when required"
  - "Correction/Court Order Processing; Protested Tax Maintenance; Bankruptcy Maintenance"
- Services: "Tax Bill / Notice Printing & Mailing" sold as a separate service line.
- Portal (wEDGE, from homepage): "e-government activities such as property tax bill payment and e-file applications."
- Treasurer testimonial (Oakland County MI): "With the launch of the Edge Tax Management system, Oakland County has significantly increased efficiency by effectively identifying and managing outstanding tax obligations and creating dynamic processes that will ultimately reinstate these properties back to the tax rolls."

## Product B — Aumentum Tax (Aumentum Technologies)

### Key observations

- Self-description: "Aumentum Tax is a modern, flexible property tax solution designed to simplify revenue management for local governments. From levy management and special assessments to billing, collection, cashiering, and distribution, Aumentum Tax provides the tools jurisdictions need to manage the complexities of property tax administration."
- Key capabilities list: Levy Management; Billing, Collection & Cashiering; Tax Distribution; Special Assessments; GIS Integration; Executive Dashboard & Reporting; Information Center; Unlimited Event Log; Business Revenue Management; Tax Sale Processing; Integrated Property Tax Workflow.
- Scope: "manages real and tangible property taxes, cashiering, local business taxes, case management for delinquent tangible property and bankruptcy/litigation cases, and reporting, all in a streamlined single-solution Cloud-based interface."
- Components:
  - **Tax Billing & Collection**: "includes the Billing Engine, Cashiering and Accounts Receivable modules. The Aumentum Billing Engine formats and produces property tax bills, business licenses, motor vehicle documents, and other bills. The Aumentum Cashiering module provides user and batch processes to calculate appropriate interest, penalties and fees and to collect and record payments in real time over the counter or through remote cashiering devices. The Accounts Receivable module is the repository for all charges, payments and credits. It calculates late payment interest, penalties and fees."
  - **Records** (shared core): "a complete inventory of the parcels, filings, business revenue or motor vehicles along with a list of the legal parties who have an interest in the inventory."
  - **Assessment Administration** (the sibling product's machinery): "maintains the property inventory and valuation data used to determine assessed values for the assessment roll."
  - **Levy Management**: "responsible for ensuring all appropriate taxes are applied to assessments. Levy Management includes tools for the maintenance of tax entities including Tax Authorities, Tax Authority Groups (Millage Codes) and Tax Authority Funds as well as configuration settings for tax calculations (including processing corrections, transferring tax bills and tax estimation). Levy Management performs the primary tax calculations as well as secondary tax calculations, which includes, for example, tax deductions and credits."
  - **Delinquents**: "Determines what bills are delinquent, automatically calculates additional interest, penalties, and fees, and facilitates the creation of notices. Includes write-off functionality, payment plans, and has a bankruptcy program that allows for creation of the filing."
- Platform framing: "As part of the fully integrated Aumentum Platform, Aumentum Tax works seamlessly with assessment and property records solutions to support the complete property tax lifecycle. Property data flows automatically throughout the platform, creating a single system of record."
- Tax Collection product family (nav): Aumentum Tax, Ascend, Kansas Patriot & Countyworks, MVP Tax, T2, VCSTax — multiple acquired product lines serving different states.

## Product C — Catalis Tax (Billing & Collections; + Escrow Payment Management; + Property Tax Oversight)

### Key observations

- Billing & Collections: "Enterprise property tax collection software for tax billing and management… Our fully integrated solution automates tax billing and collections." "Catalis Tax helps local governments modernize tax administration by unifying billing, collections, and assessment into a single, easy-to-use platform."
- Feature blocks: "Vendor Consolidation — Replace the need for multiple vendors by integrating billing, collections, cashiering, and more."; "Customer Portal — intuitive e-billing and payment platform"; "System Integration — Integrate with land recording systems that file and record legal documents including deeds and mortgages"; "Seamless Reconciliation — end-to-end workflows that streamline monthly audits and closings"; "Cloud & On-Premises Based Systems".
- Named features: "Ownership History Data — maintain full-scale property information and quickly communicate changes"; "Tax Calculation — Calculate taxes and print tax bills across multiple formats for both real estate and personal property"; "Robust Reporting — extensive reports detailing transactions and deposit history."
- Family page stats: "$X B+ in Taxes Collected" with Catalis Tax & CAMA solutions; "States in Operation 20+" (counter animation; exact figure not asserted).
- **Escrow Payment Management** (separate product line): "tax collectors can streamline escrow payment processes with robust reporting, data retrieval, and automated workflows… eliminates the need for balancing checks, manual posting, and refund processing." "Block duplicate escrow payments with software that improves accuracy." "Banks, credit unions, and property owners can quickly find parcel information with smart search capabilities." "Our tool is fully funded by the end users with a small parcel fee"; "no cost to tax collectors." Treasurer testimonial (City of Falls Church VA): "we can provide our tax file to the Catalis platform, which then shares the data with all the escrow companies and banks that request the data… reduction in refunds and duplicate payments."
- **Property Tax Oversight** (separate product line, examined per the assessment pass's flag): "State property tax administrators face several challenges, such as processing vast quantities of data, utilizing outdated systems, and producing complex reports for legislators." Features: "Oversight & Compliance — Monitor and evaluate the performance of jurisdictions valuing and levying property taxes"; "Electronic Filing — Filers can digitally submit and manage any type of filing, from summary data like abstracts to detailed, centrally assessed renditions"; "Analytical Tools — advanced geospatial analytical tools"; "Complex Valuations — administrators can leverage a unified platform to complete centrally assessed valuations using cost, income, and market approaches." User = state-level oversight administrators, NOT the local collector.

## Product D — Grant Street Group TaxSys

### Key observations

- Self-description: "State-of-the-art cloud-based property tax billing, collection, and distribution platform." "TaxSys is a hosted, web-based solution for tax calculation, billing, collection, and distribution. Built for government… proven in large and complex counties." Stats: "$50 Billion Taxes Collected; 27 Million People Served."
- Domain vocabulary: "Our experts speak your language when it comes to tax collection. Whether related to tax liens, supplementals, apportionment, distributions, millage rates, property tax exemptions, or any other process your office handles."
- Day-to-day features: self-service reporting; automated task scheduling; "Extensive account history including call logging, notes, and document attachments"; digital forms; integrated modules; "Real-time data updates to other systems of record"; "Centralized, accurate calculation engine"; "Personalized online taxpayer experience."
- Integrated products: Business Tax Applications; Payment Processing (credit, debit, e-check, digital wallet); Tourist / Occupancy Tax ("file returns and make payments on tourist tax accounts"); Escrow Payment Processing ("An online portal for mortgage companies and tax paying agents to manage their accounts and submit payment files"); Motor Vehicle Transactions; Tax Deed Applications ("automates the entire deed application process"); E-Billing and E-Reminders; Public Portal ("taxpayer inquiry, research, payment, and report downloads"); Integrated Title Searches; Business Intelligence (VisionPro).
- Tax sales: "LienHub® is a comprehensive online auction platform for tax lien sales. These include the annual delinquent tax sales (auctions after tax payments become delinquent) and ongoing sales of county-held tax certificates… Investors can view and manage tax certificates, certificate transfers, and tax deed applications." "DeedAuction® is a complete online auction platform for sales of tax-defaulted property deeds."
- Clients: county tax collectors/commissioners (San Bernardino CA Chief Deputy Tax Collector; Cobb County GA Tax Commissioner; Bay County FL Tax Collector).

## Product E — Harris Govern Property Tax & Collections

### Key observations

- Self-description: "The Harris Govern Property Tax & Collections Software provides a streamlined system… for processing and managing Property Tax & Collections." "Tax Collectors and Treasurers often spend lots of time and resources generating tax bills, processing payments, and managing delinquent taxes."
- Scope: "speeds up traditional local government billing and collections for real property, personal property, business occupancy, tax delinquency, excise, and individual assessment."
- Core features: "Real Property Tax Billing; Accounts Receivable/Cash Collection; Personal Property Tax Billing; Tax Delinquency."
- Named capabilities:
  - "Simplified Tax Bills — generate, process, and approve tax bills from one simple-to-use system… track and process standard bills, refunds, discounts/installments for each tax bill along with all payments to date."
  - "Print Interim/On-Demand Bills — print a comprehensive history of all paid bills… printing receipts for a complete record for all parties."
  - "Tax Distribution & Levy Management — store levy, garnishment, and other information in a central location… the levy management and tax distribution process."
- Benefits: "posts data to Accounts Receivables, generates bills, and prints bills and correspondence in a central location"; "Collect tax payments in-person, through the web, and via payment loads for rapid payment processing"; "Taxpayers can access data and make payments through a controlled and secured system"; "complete access to tax billing and property tax data… transaction history and activities with a sophisticated search tool"; "robust reports that summarize all transactions with full audit trails."
- Organizational-seam evidence: the site's public property-search directory lists, per Texas county, separate "CAD" (County Appraisal District — assessment) and "TAX" (tax office — collection) portals, often on separate systems/URLs — the value operation and the money operation are separate offices with separate systems.

## Cross-product Comparison

| Aspect | DEVNET Edge B&C | Aumentum Tax | Catalis Tax B&C | Grant Street TaxSys | Harris Govern PT&C |
|---|---|---|---|---|---|
| Self-description | "billing, collection, distribution, delinquent taxes, tax sales" | "levy management… to billing, collection, cashiering, and distribution" | "tax billing and management… billing, collections, cashiering" | "tax calculation, billing, collection, and distribution" | "generating tax bills, processing payments, and managing delinquent taxes" |
| Unit of record | tax broken out "by tax year, political sub-division and types of tax"; bills with payments | AR "repository for all charges, payments and credits"; tax bills | property information + bills; transactions/deposit history | "extensive account history" per account | "each tax bill along with all payments to date" |
| Levy/rate machinery | taxing body maintenance; tax/millage rates; multiple taxing bodies per parcel | Levy Management: Tax Authorities, Authority Groups (Millage Codes), Funds; primary + secondary calculations | tax calculation (formats for real estate + personal property) | "millage rates, apportionment, distributions" | "Tax Distribution & Levy Management" |
| Billing | laser bills, bar-coded bills, receipts; collector's/delinquent books | Billing Engine (tax bills, business licenses, motor vehicle docs) | "print tax bills across multiple formats" | centralized calculation engine; e-billing/reminders | simplified bills; interim/on-demand bills; refunds, discounts/installments |
| Collection channels | counter by barcode/parcel/bill/owner/tax-buyer; bank tape payments; online | cashiering over the counter + remote devices; batch | cashiering; customer portal | counter + online (card/e-check/wallet); escrow agent portal | in-person, web, payment loads |
| Delinquency | delinquent books/bills; penalty/interest by month; protested tax; bankruptcy | Delinquents module: determination, charges, notices, write-offs, payment plans, bankruptcy | (collections) | tax liens; supplementals | Tax Delinquency |
| Tax sale | "tax sales" processes; tax buyer named payments | Tax Sale Processing | not surfaced | LienHub (lien certificate auctions) + DeedAuction + deed applications | not surfaced on page |
| Distribution | FAST distribution (checks + ACH); disbursement/settlement reporting | Tax Distribution | not surfaced on page | "apportionment, distributions" | Tax Distribution |
| Escrow/bulk | tape payments from banks | (not surfaced on page) | Escrow Payment Management (separate line) | Escrow Payment Processing portal | payment loads |
| Corrections | court orders, additions/deletions/supplements, write-offs, waivers, abatements, protested | corrections, transferring tax bills, tax estimation | (reconciliation) | supplementals | refunds; standard/corrected bills |
| Public portal | wEDGE (payment, e-file) | Public Access (separate product) | Customer Portal | Public Portal | Harris Govern Online |
| Adjacent revenue | merchant's license, surtax, land sales, special districts | business licenses, motor vehicle, business revenue | (payments family: court/utility/child support) | business tax, tourist/occupancy, motor vehicle | business occupancy, excise |
| Deployment | (suite; on-prem lineage) | Cloud-based | cloud or on-premises | hosted cloud | (suite) |

### Stable commonalities (layer B — cross-product)

All five sampled products carry, in their own words:

1. a persistent tax bill/account as the unit of record (property × tax year liability with payments, charges, status)
2. levy/rate machinery: taxing entities and rates/millage maintained in-system and associated with properties (4/5 explicit on fetched pages; Catalis implies via "tax calculation")
3. bill production: calculation + printing in multiple formats, with receipts (5/5)
4. multi-channel collection: counter/cashiering plus remote channels (online, bank tape files, escrow agents) (5/5)
5. delinquency machinery: delinquency determination, statutory interest/penalties/fees, notices (4/5 explicit; Catalis implied by "collections")
6. distribution/settlement of collected money to taxing entities (4/5 explicit; Catalis not surfaced on the fetched page)
7. corrections machinery: court orders, additions/abatements, supplements, refunds, protested payments (4/5 explicit)
8. a public-facing portal for inquiry/payment (5/5, sometimes as a separate product)
9. reporting with audit trails, by year/subdivision/tax type (5/5)
10. adjacent local revenue in the same platform (business tax/licenses, special assessments, tourist/occupancy, motor vehicle) (5/5, breadth varies)
11. tax sale machinery (3/5 explicit: DEVNET, Aumentum, Grant Street; regime-dependent)

### Canonical inference (layer C)

The Type is best understood as: **the jurisdiction's system of record for property tax money** — it receives certified taxable values from the assessment side, applies the jurisdiction's levies to produce each property's tax bill, records payments against those bills across every channel, pursues delinquent balances under statutory charges, and settles the collected money to the entitled taxing entities. The bill is the liability record; the levy machinery is the Type's specificity; the collection-and-settlement loop is the "administration".

## Canonical Model (four-layer abstraction)

### L0 — Defining Invariant (minimal)

Three jointly-held structures:

1. **The tax bill/account of record** — a persistent, individually identified liability record binding a property (or taxpayer account) × tax period × amount due, carrying payments, adjustments, statutory charges, and status through the year. Remove → a payment portal or AR ledger with no tax liability record; nothing to bill, collect, or settle.
2. **Levy-driven billing against taxable values** — the jurisdiction's taxing entities and their rates/levies configured in-system and applied to taxable values received from the assessment side to compute and produce each bill; one bill commonly aggregates several entities' levies for the same property. Remove → generic invoicing; the property-tax specificity (the levy on a valued parcel) disappears.
3. **The collection-and-settlement loop** — payments recorded against bills across channels (counter, mail, bank/escrow files, online), delinquent balances tracked with statutory charges, and collected monies distributed/settled to the entitled taxing entities. Remove → a bill printer; the "administration" — collecting the money and settling it — is gone.

Jointly-held load-bearing tests:
- 1 alone = accounts-receivable ledger
- 2 without 1 = rate calculator
- 3 without 1+2 = payment processor
- 1+2 without 3 = bill printer
- 1+3 without 2 = generic municipal billing (utility-style)
- 2+3 without 1 = ephemeral transactions with no liability record

### L1 — Common Mature Structure (standard capabilities, not definitional)

- cashiering (over-the-counter, remote/batch devices) with receipts
- payment channels: online (card/e-check/wallet), mail/lockbox, bank tape files, escrow-agent/mortgage-servicer portals
- delinquency machinery: delinquency determination, interest/penalty/fee calculation, notices, payment plans, write-offs
- tax-sale machinery: lien certificate sales, tax-defaulted deed sales, deed applications (regime-dependent)
- escrow/bulk payment processing with duplicate-payment prevention and refund handling
- corrections machinery: court orders, additions/abatements, supplements, bill transfers, protested payments, waivers
- bankruptcy/litigation case handling constraining collection
- distribution/settlement engines: apportionment by entity share, check printing, ACH, settlement/disbursement reporting
- public portal: inquiry, e-billing/reminders, payment, forms, report downloads
- reporting: by tax year / political subdivision / tax type; collector's and delinquent books; audit trails; state reports
- adjacent local revenue in the same platform: business tax/licenses, special assessments, tourist/occupancy tax, motor-vehicle cashiering
- GIS integration, dashboards/business intelligence, workflow/event logs, call logging/notes on accounts

### L2 — Variant / Optional Structure

- office scope: county treasurer vs tax collector vs tax commissioner vs municipal revenue office; combined vs separate appraisal district + tax office (the Texas CAD/TAX model)
- regime machinery: lien states vs deed states vs neither; installment and discount schemes; billing-time exemptions/deductions/credits
- suite posture: standalone collection system ↔ integrated land-records suite (appraisal→collection) ↔ collection + payments/auction specialist
- deployment: on-premises ↔ cloud/SaaS (both documented)
- adjacent-revenue breadth (from property-only to multi-revenue platforms)
- bill printing/mailing as a vendor service
- state-oversight variant (separate product line; see Boundary Findings #8)

### L3 — Vendor-specific (research notes only)

- DEVNET: Edge suite naming, FAST distribution, wEDGE portal, EdgeMaps, "collector's books / delinquent books" terminology, tape payments, tax-buyer payment entry
- Aumentum: Billing Engine / Cashiering / AR module names; Levy Management (Tax Authorities / Authority Groups / Funds); Delinquents module; Information Center, Executive Dashboard, Unlimited Event Log; acquired product lines (Ascend, Kansas Patriot & Countyworks, MVP Tax, T2, VCSTax); "1,000 governments / 39 states / 35M parcels / $120B" stats
- Catalis: brand family (LandNav, GovTech Services, PCI, eGov, Patriot Properties, CAMAlot, Northeast Revaluation, MarketDrive, Axiomatic); Guided Tours; Escrow Payment Management funded by end-user parcel fees ("no cost to tax collectors"); Property Tax Oversight line
- Grant Street: TaxSys, PaymentExpress, LienHub, DeedAuction, VisionPro BI, integrated title searches, "$50B / 27M people" stats
- Harris: PACS / RealWare / OpenForms suites; state-by-state product routing; Safe Passage / Software-for-Life programs; TrueAutomation-lineage public portals

## Vendor-specific Findings

See L3. None promoted to the canonical model. The closest near-promotion candidates: (a) distribution/settlement machinery — held inside the L0 loop because 4/5 sampled products document it and the settlement duty is what distinguishes a revenue administration from a payment processor; (b) tax-sale machinery — held at L1 because regimes differ (lien vs deed vs neither).

## Boundary Findings

1. **vs Property Assessment System** (§24 sibling; joint-review flag DISCHARGED from this side): keep-both RATIFIED on the parcel-spine seam exactly as the prior passes drew it — rights (land records) vs value (assessment) vs money (tax). This pass adds the tax-side evidence: (a) suite vendors sell valuation and tax as separate product lines (Aumentum Valuation vs Aumentum Tax; DEVNET CAMA vs Billing & Collection; Catalis CAMA vs Billing & Collections; Harris CAMA vs Property Tax & Collections) — packaging evidence of the seam; (b) direction of flow: Aumentum Levy Management is "responsible for ensuring all appropriate taxes are applied to assessments" — tax consumes assessment output; DEVNET frames the suite as "the entire property tax life cycle from appraisal to collection"; (c) organizational evidence: Harris Govern's public-search directory lists separate CAD (appraisal) and TAX (collector) portals per Texas county — separate offices, separate systems; (d) the professional anchor from the assessment pass: IAAO — "The assessor does not determine property taxes." The certified roll / taxable values are the hand-off artifact. Remove billing/collection → assessment; remove valuation machinery → tax administration.
2. **vs Land Records / Cadastre System** (§24 sibling): same parcel spine; land records holds the rights record; tax holds the money record. Catalis B&C documents "Integrate with land recording systems that file and record legal documents including deeds and mortgages" — an integration feed (ownership changes drive re-billing), not the same Type.
3. **vs Tax Administration System** (§24 sibling, generic): the generic Type is a revenue authority's machinery for all tax types (income, sales, etc.); Property Tax Administration is the parcel-anchored, roll-fed, levy-and-distribution variant. The sampled products bundle adjacent local taxes (business, tourist/occupancy, motor vehicle) into the same platform — the property-tax core extends to account-anchored local taxes — but the parcel/roll anchor and taxing-entity distribution structure define this leaf. Keep-both; seam = parcel/roll anchor vs general revenue administration.
4. **vs Government Revenue Management** (§24 sibling): broader revenue accounting/collections across sources; PTA is the property-tax-specific machinery. Conceptual boundary (no leaf sampled).
5. **vs Utility Billing**: recurring metered service billing vs statutory levy billing on taxable values; utility billing has no taxing-entity distribution structure and no roll input. Both share "bill → collect → delinquency" surface vocabulary, which is exactly why the levy/roll input and the settlement structure are the distinguishing core.
6. **vs Payment platforms (Payment Gateway / Processing)**: payment processing appears in-sample as a bundled capability or separate product line (Catalis sells "Tax Payments" under a separate Payments family; Grant Street sells PaymentExpress beside TaxSys). The Type's center is the liability record + levy + settlement, not the payment rails.
7. **vs Mortgage Servicing Platform** (§08): the escrow side. Mortgage servicers pay property taxes from escrow; the tax office's escrow portal serves them (Grant Street: "online portal for mortgage companies and tax paying agents… submit payment files"; Catalis Escrow Payment Management). The servicer's own escrow machinery is a different, private-side Type.
8. **State-oversight variant (Catalis Property Tax Oversight) — EXAMINED per the assessment pass's flag**: a state-level product for oversight administrators — monitoring "the performance of jurisdictions valuing and levying property taxes", e-filing of abstracts and centrally assessed renditions, centrally assessed valuations. Verdict: an ADJACENT state-oversight variant with a different user (state oversight agency) and different machinery (monitoring/e-file/central assessment rather than billing/collection). It does not belong in this leaf's core model; if the taxonomy later wants it as a leaf, it belongs beside the assessment/oversight side. Recorded here and in STATUS Boundary Issues as examined-and-held.
9. **vs Permit Management / Code Enforcement** (§24 siblings): different regulatory cases; no seam observed beyond suite bundling.

## Historical / Market-Sample Check

- **Paper-era treasurer/collector**: the tax book (duplicate tax books of bills), rate levies set by taxing districts, handwritten bills and receipts, the delinquent list published before tax sale, and the tax sale itself — all three L0 legs satisfied with no software. Direct textual anchor: DEVNET's own feature names — "collector's books, delinquent books", "duplicate tax receipts", "tax buyer name" — preserve the paper-era artifacts in modern feature language.
- **Older/regional products**: DOS/mainframe-era county tax systems and the ceased-trading Windows-desktop generation seen in sibling passes satisfy the same legs; state-specific machinery (millage caps, abstracts) is regional, not definitional.
- **Non-US regimes**: UK council tax / national business rates (local authority billing, collection, enforcement, and the precept/distribution structure) and Australian local-government rates follow the same structure conceptually — levy on valued property → bill → collect → distribute — with different enforcement machinery (court-based liability orders rather than tax lien sales). Held conceptually; the sample is North America-weighted. Confidence: moderate (reasoned, not directly sampled).
- **Anti-overfit guards**: "millage" vocabulary NOT definitional (rate/levy/precept terminology varies); tax lien sales NOT definitional (deed-state and no-sale regimes exist); escrow portals NOT definitional (bank tape payments are the older realization); online payment NOT definitional (counter + mail satisfy); SaaS NOT definitional; adjacent revenue lines NOT definitional.

## Uncertainties

- Tyler Technologies (widely described as the largest US local-government property-tax platform vendor) could not be fetched (403 ×2 in the sibling pass; not retried) — market anchor only; no structural claims drawn from it.
- Catalis Billing & Collections page is marketing-level; detailed module structure is not publicly documented — Catalis claims held at page level.
- Distribution machinery is not explicitly surfaced on the fetched Catalis B&C page (4/5 sampled products document it) — held common-mature, not asserted universal.
- Non-US regimes not directly sampled; conceptual coverage only.
- Exact statutory parameters (penalty schedules, sale windows, installment counts, discount percentages) vary by jurisdiction and are NOT asserted anywhere.
- Property Tax Oversight's deployment depth (which state agencies use it) — only the vendor page observed.

## Final Synthesis

A Property Tax Administration system is the government's system of record for property tax money: it receives certified taxable values from the assessment side, applies the jurisdiction's levies — taxing entities, rates/millage, special assessments, billing-time deductions and credits — to produce each property's tax bill (one bill commonly aggregating several entities' levies), records payments against those bills across every channel (counter, mail, bank and escrow-agent files, online), pursues delinquent balances with statutory charges and, where the regime provides, tax lien/deed sales, and settles the collected money to the entitled taxing entities with full audit trails. The parcel spine is shared with land records (rights) and assessment (value); this Type owns the money operation. Everything else commonly bundled — cashiering hardware, portals, business/tourist taxes, escrow portals, BI, AI — is standard capability or variant machinery, not the definition.
