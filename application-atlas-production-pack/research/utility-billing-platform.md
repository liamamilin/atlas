# Research Notes — Utility Billing Platform

Research date: 2026-09-10

## Research Goal

Understand what a Utility Billing Platform actually is from real products: what objects it holds (accounts? premises? meters? bills? money?), who operates it, how the meter-to-bill-to-money cycle actually runs, and where its boundaries run — especially against the unprocessed sibling **Utility Customer Information System / CIS** (the central taxonomy question of this pass), the processed **Billing Platform** (§08 generic spine), the processed **Gas Utility Management** (which held itself as the gas vertical edition of this family and flagged this leaf), and the metering/field/rate/revenue siblings in §19.

## Initial Boundary

Hypothesis before research:

- The leaf sits in §19 next to "Utility Customer Information System / CIS" (unprocessed) and near the processed gas/water verticals. Prior passes established:
  - **gas-utility-management** (2026-09-08): L0 = served-premise service account + metered-consumption chain + meter-to-bill-to-money cycle; held as the *gas-industry vertical edition* of the utility customer-management family; explicitly flagged that the CIS and Utility Billing passes should test the vertical-edition framing from their side. It characterized Utility Billing Platform as "the billing engine slice; a billing engine without the service-account spine and service-order loop is a component of this Type, not the whole" — a characterization this pass must test, because the market's "utility billing" products (Springbrook, MuniBilling) visibly carry the full account + meter + service-order structure.
  - **billing-platform** (§08, 2026-09-06): generic vendor-side system of record for what customers owe (billing accounts + charge computation + bill as authoritative lifecycle-managed record + tracked settlement); flagged "vs Utility Billing Platform: the metered-consumption industry instance... satisfies the generic spine but adds utility-specific machinery; kept as a separate leaf."
  - **meter-data-management-system-mdms** (2026-09-09): system of record for *billing-quality meter data* (VEE, bill determinants published to billing/CIS) — the upstream data layer.
- Working hypothesis: Utility Billing Platform = the horizontal, billing-led pole of the utility customer-management family — the system that runs the recurring meter-to-bill-to-money cycle over a population of served premises, with the customer/account record as substrate. The CIS leaf is expected to be the same family under a customer-care-led name at the enterprise tier.
- Suspected risks: (a) alias with Utility CIS (the two names may denote one family at different tiers); (b) collapse into the generic §08 Billing Platform (must show what the utility machinery adds); (c) confusion with MDMS/AMI (data layer) and with telecom charging (real-time balance drawdown).

## Research Questions

1. What is the central object of record: the account, the premise/service point, the meter, the bill — and how do they chain?
2. How does the recurring bill cycle actually run (batch runs, cycles, off-cycle/final bills), and which parts are definitional vs common?
3. What is the bill as an artifact — its lifecycle (creation, completion, correction, cancel/rebill, write-off) and its relationship to financial transactions?
4. How does the money cycle work (payments, adjustments, deposits, arrears/collections, budget plans), and how does money couple to service state?
5. What role do service orders play in connecting office and field?
6. How do rates work as configuration (tiers, seasonal, proration, effective dates)?
7. What is actually utility-specific vs the generic §08 billing spine?
8. How does market structure (bundled-supply vs retail competition; supplier seat vs network seat) change the system's scope?
9. Is the "utility billing" product category a bare billing engine or the full customer-management family? (Tests the gas pass's "billing engine slice" characterization.)
10. Where do the boundaries run: vs Utility CIS, MDMS/AMI, rate management, revenue assurance, field service, water/gas verticals, telecom charging, EV charging billing, rent collection?

## Representative Products

Chosen for market representation + documentation accessibility + different product philosophies + different customer tiers. NISC (the co-op pole most literally associated with utility CIS/billing) timed out again (×2 across passes) and is abandoned per network rules.

| Product | Vendor | Pole | Evidence depth |
|---|---|---|---|
| Oracle Utilities Customer Care and Billing (Cloud Service) | Oracle | enterprise-tier CIS/UB; deep official Business User Guide | A — TOC + 4 topic pages fetched verbatim |
| SAP for Utilities (IS-U) — Billing in Contract Accounts Receivable and Payable / Convergent Invoicing | SAP | enterprise ERP-embedded pole; subledger-accounting philosophy (FI-CA) | A− — official Help Portal content via search-index verbatim excerpts (page itself JS-rendered) |
| Itineris — UMAX Utility Suite | Itineris | international enterprise CIS/CRM/ERP suite on Microsoft Dynamics 365 | A — homepage + suite structure fetched |
| Cayenta | Cayenta (Harris) | mid-market North American utility suite (CIS + work + financials + HCM) | A — homepage fetched |
| MuniBilling | MuniBilling | modern cloud small-utility "utility billing" pole; flexible billing engine | A — homepage + features page fetched |
| Springbrook — Cirrus Utility Billing | Springbrook | small-municipality government utility billing | A — product page fetched (re-fetched this pass) |
| Gentrack | Gentrack Group | competitive-retail supplier seat (Energy Suppliers vs Energy Networks sectors) | A — sector page fetched |

Supporting / cross-pass corroboration (fetched 2026-09-08 in the gas-utility-management pass, cited here as corroboration only): Advanced Utility Systems CIS Infinity ("electric, water, gas, and multi-service providers"; "customer service points"; "meter-to-cash"), NorthStar Utilities Solutions, MuniBilling (earlier fetch).

## Sources

- Oracle Utilities Customer Care and Billing Cloud Service — Business User Guide: https://docs.oracle.com/en/industries/utilities/customer-care-billing/264/ccbcs-user-guides/Topics/CCB_BP_Intro.html (fetched 2026-09-10); Billing section: .../Topics/C1_BP05Billing_Billing.html; The Big Picture of Billing: .../Topics/C1_BP05Billing_The_Big_Picture_of_Billing.html; An Overview Of The Bill Creation Process: .../Topics/C1_BP05Billing_A_High_Level_Overview_Of_The_Bill.html; How The System Determines How Much Was Consumed: .../Topics/C1_BP05Billing_How_The_System_Determines_How_Muc.html; Bill Frequency — Bill Cycle vs Bill Segment Duration: .../Topics/C1_BP05Billing_Bill_Frequency_Bill_Cycle_vs_Bi.html (all fetched 2026-09-10)
- SAP Help Portal — Contract Accounts Receivable and Payable (FI-CA, SAP Utilities Industry): https://help.sap.com/docs/SUPPORT_CONTENT/uindustry/3362183821.html ; Utilities, Billing in Contract Accounts Receivable and Payable: https://help.sap.com/docs/SAP_ERP/8885dc274cc4489aa3dd28ac0a9bfa10/0621dd3cfb58431b966b63a752540ce3.html ; Convergent Invoicing (S/4HANA): https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/09d5264e467d4491a82a32335a52e45f/b759a44fc5fb40128f99e90f5233b365.html (content obtained 2026-09-10 via search-index verbatim excerpts; direct fetch JS-rendered)
- Itineris — UMAX Utility Suite: https://www.itineris.net/ (fetched 2026-09-10)
- Cayenta: https://www.cayenta.com/ (fetched 2026-09-10)
- MuniBilling — homepage + Core Features: https://www.munibilling.com/ , https://www.munibilling.com/software (fetched 2026-09-10)
- Springbrook — Cirrus Utility Billing: https://www.springbrooksoftware.com/solutions/utility-billing/ (fetched 2026-09-10)
- Gentrack — Energy Suppliers sector: https://www.gentrack.com/energy-retailers/ (fetched 2026-09-10)
- Cross-pass corroboration (2026-09-08): Advanced Utility Systems https://advancedutility.com/solutions/customer-information-systems/ ; NorthStar https://www.northstarutilities.com/ ; Oracle docs index https://docs.oracle.com/en/industries/utilities/
- Unreachable: NISC (nisc.coop — timeout ×2 across passes), CSA (bot wall, prior pass), Tyler/Banyon (403, prior pass)

**Source-access limitation**: NISC remains unreachable; no claims drawn from it. SAP's Help Portal pages are JS-rendered; evidence taken from verbatim search-index excerpts of the official pages and marked A−. Prepaid utility billing machinery was not documentable this pass and is held as unverified.

## Product A — Oracle Utilities Customer Care and Billing (Cloud Service)

### Key observations (Layer A — directly observed)

- The Business User Guide's section tree is the vendor's own functional taxonomy of the Type: Customer Information · **Premise Management** · **Meter Management** · **Meter Reading** · **Service Orders** · **Billing** · Payments · **Adjustments** · **Credit & Collection** · Financial Transactions · **Deposits** · Statements · Sales & Marketing · **Rates** · Quotes · Service Credits · Appointments · Loans · **Non-Billed Budgets** · Asset Inventory · Case Management · **Umbrella Agreement Management** · Job Streams · Workflow and Notifications · **Overdue Financial Obligations** · Dashboards · Rebate Claims · **Interval Billing** · To Do Processing · Reports.
- **Bill definition** (verbatim): "A bill is used to communicate changes in an account's financial obligations to the customer. Over time, a customer receives many bills."
- **Bill creation** (verbatim): "When the system is asked to produce a bill for an account, it attempts to create one or more bill segments for every non-cancelled / non-closed service agreement linked to the account." For a metered service agreement: "The system first calculates the amount consumed (e.g., the number of lamps, the number of gallons of water, the peak kW, etc.)... Next, the system applies the service agreement's rate to the amount consumed in order to calculate how much the customer owes. A bill segment and a financial transaction are generated to reflect the results of this calculation."
- **Metered vs non-metered algorithms** (verbatim): "There are many bill segment creation algorithms... if the service agreement charges for a deposit, the system neither amalgamates consumption nor does it apply a rate." And: "There are two types of service agreements: Those that charge for some commodity (e.g., electricity, water, garbage, street lighting). Those that charge for something intangible (e.g., deposit, charitable contribution, payment arrangement)."
- **Consumption snapshots** (verbatim): consumption saved on the bill segment as "meter read snapshot" (reads used), "item snapshot" (items at service points), "service quantity snapshot" (billable service quantities derived from both).
- **Bill cycle** (verbatim): "An account's bill cycle defines when the system attempts to create bill segments for the account's service agreements." Accounts may mix service agreements of different durations (biweekly/monthly/quarterly) on one bill cycle. "Batch and real-time bill creation. Anything the batch bill process does for whole sets of accounts, you can do to a specific account on-line / real time."
- **Bill completion** (verbatim): bill routing per person ("controls the format of the printed bill and how the bill is sent"), bill messages, freeze options, and "Sweeps recent financial transactions that have been created since the last bill was completed" (payments, adjustments, bill corrections appear on the bill).
- **Bill error machinery**: "If errors are detected during the bill segment creation process, the bill segment is saved with its error... a user can see all problematic bill segments so they can be corrected en masse." Plus dedicated topics: Bill Exception, Bill Segment Exception, Multi Cancel/Rebill, Off-Cycle Bill Generator, Credit Notes, Correction Notes, Writing Off Bills, Sequential Bill Numbers, Digital Signatures.
- **Market-structure machinery** (verbatim warning): "Some organizations are responsible for presenting 3rd party charges on their bills. Others are responsible for sending their charges to a 3rd party for presentation on their bills." — pass-through / convergent billing for retail-competition markets, documented inside the product.
- **Money cycle**: Payments, Adjustments, Credit & Collection, Deposits, Overdue Financial Obligations, Non-Billed Budgets (budget billing), Loans, Service Credits — the full credit-and-collections furniture of a utility that extends credit.
- Interval Billing as the AMI-era extension; Case Management, Sales & Marketing, Quotes, Appointments as the customer-care breadth of the CIS pole.

## Product B — SAP for Utilities (IS-U): Billing in FI-CA / Convergent Invoicing

### Key observations (Layer A− — official Help Portal content via verbatim search excerpts)

- **FI-CA definition** (verbatim): "Contract accounts receivable and payable (FI-CA) is a type of subledger accounting that is tailored towards the requirements of industry sectors with multiple business partners and a large number of documents for processing."
- **Posting documents** (verbatim): "The following is a list of typical posting documents found in utility companies: Bills and credit memos · Dunning charges · Return charges · Interest · Cash security deposits · Incoming and outgoing payment postings including payments on account and down payments · Budget billing amounts."
- **Master data objects** (verbatim, Convergent Invoicing): "business partner in the role of the contract partner, contract account, and provider contract."
- **Charge pipeline** (verbatim, from the BRIM/FI-CA structure): billable items and consumption items → rating → billing → invoicing documents → posting documents in FI-CA → general ledger. "Invoices and credit memos from contract billing and invoicing are posted in FI-CA automatically."
- **Deregulated market** (verbatim): "In the deregulated market, it is possible that cross-company code invoicing or billing for and by a third party will be required."
- **Mass processing**: billing and invoicing run as mass activities; archiving of billing documents as mass runs.
- Reading: the ERP pole realizes the same cycle with a different philosophy — the money side is a purpose-built subledger (FI-CA) inside the ERP, and utility billing/invoicing are mass processes feeding it. The object vocabulary (business partner, contract account, consumption items, budget billing, dunning, deposits) maps one-to-one onto the CIS vocabulary.

## Product C — Itineris UMAX

### Key observations (Layer A — directly observed)

- Positioning: "AI-powered CIS, CRM & ERP for utilities"; "UMAX supports accurate conversion of meter readings to bills, with extensive customer and field service support capabilities."
- Sectors: energy utilities, water utilities, EV operators — "Whether your utility provides electricity, gas, water, stormwater, wastewater/sewer services, or a combination of these."
- Suite structure: UMAX Customer Platform ("the core... modules that help utilities streamline their business processes and boost customer engagement"), UMAX Real-Time (dynamic pricing, imbalance management — the competitive-market extension), UMAX Add-ons; built on Microsoft Dynamics 365 / Azure / Power Platform.
- Scale framing: "bills generated with UMAX annually" (millions) and "customer accounts served by our clients" — the vendor's own units are bills and customer accounts.
- Customer base spans municipal water/sewer (Boston Water & Sewer, NYC DEP), cities/counties (Dallas, Baltimore), and competitive energy suppliers (Eneco, SSE Business Energy, Flogas) — the same family serving both utility seats and supplier seats.

## Product D — Cayenta

### Key observations (Layer A — directly observed)

- Positioning: "utility-focused solutions that power customer management, billing, financials, work management, and human capital management."
- CIS framing (verbatim): "A Customer Information System built around your customers, consolidating customer service, billing, and account insight into one trusted operational hub."
- Industries: Electric, Water, Gas, Fiber; customer types: Municipalities, Counties, Co-Ops, Investor Owned.
- Suite: CIS + Work Management (asset management, inventory, field operations) + Financial Management (multi-fund accounting) + HCM.
- A division of N. Harris Computer Corporation — corroborates the Harris consolidation of the mid-market noted in the gas pass (Advanced, NorthStar, Cayenta all Harris).

## Product E — MuniBilling

### Key observations (Layer A — directly observed)

- Category name (verbatim): "Cloud Based Utility Billing Software"; customer quote: "MuniBilling was constructed from the ground up as a utility billing platform."
- **Flexible billing engine** (verbatim): "accommodates different tax rates, fees, and adjustable billing tiers for metered and non-metered bills"; "can bill for any service or fee... unlimited rates and tiers and supports integrations with meter reading systems."
- **Billing breadth** (verbatim): "handles recurring flat fee subscriptions, tiered usage, and other one-time charges with ease. Apply credits for any type of utility or service such as – water, recycling, sewer, garbage, gas, electric, stormwater, internet, cable, pest, HOA, amenities... Customize billing options for weekly, monthly, quarterly, semi-annual or annual billing cycles."
- **Modules**: Billing Management; Mobile Service Order Management ("tickets and issues... entered into our customer portal directly by your customers or tenants... establish an audit trail"); Mobile Meter Reader (offline capture, anomaly identification); Customer Portal.
- **Money**: "Secure Payments Options... Lockbox, Credit Card, ACH... improve the integrity of your Accounts Receivables"; real-time reporting "into Accounts Receivable, Billing, Customer Accounts, Meters, and Payments"; "send batches of billing data to mainstream accounting software programs."
- **Seasonal management**: "high volumes of ad hoc customer moves... dormancy period or seasonal rate structures."
- **Market breadth**: Municipalities, Multi-Family (submetering), Higher Education, Private Utility Entities — the "billing entity" market extends beyond utilities proper; the billable-services list includes non-utility items (recreation, snow removal, parking, storage, fees and fines).

## Product F — Springbrook Cirrus Utility Billing

### Key observations (Layer A — directly observed; re-fetch corroborating the gas pass)

- Positioning: "government utility billing software connected in real time to an online payment system, with comprehensive water, sewer, electric, refuse and allocation water billing capabilities"; "Complete 'meter-to-cash' solution for utilities of water, electric, sewage, garbage, storm water and virtually any other billable resource."
- Machinery (verbatim): "Handles tiered rates, winter averaging and credit-based deposits"; "Built in support for all major meter vendors and AMI systems"; walkthrough: "Centralized customer view · Single Account overview · Easy payment acceptance · Unlimited Meters & rates per account · Automated payment options · Integrated past dues and collections · Full meter management · Integrated service requests · Integrated to AP for refunds · Full general ledger integration."
- Embedded in a government finance platform (Cirrus Finance) — the small-municipal pole lands the money cycle in the government GL.

## Product G — Gentrack (supplier seat)

### Key observations (Layer A — directly observed)

- Sector structure: "Energy Suppliers" / "Water Suppliers" / "Energy Networks" as distinct sectors — the supplier/network seat split is the vendor's own market taxonomy.
- Portfolio: Customer Engagement, **Billing & Finance**, Business & Data Applications, DER Management, Integration Layer, **Debt Management**.
- Framing (verbatim): "proven billing and customer experience solutions designed for B2C, SME and I&C energy consumers"; "Improve billing accuracy & collections efficiency"; "Designed for competitive and dynamic utility markets."
- Reading: in competitive retail markets the same object family (customers, meter points, billing, debt) is operated by the *supplier*; the network utility is a separate seat.

## Cross-product Comparison

| Dimension | Oracle CCB | SAP IS-U/FI-CA | Itineris UMAX | Cayenta | MuniBilling | Springbrook Cirrus | Gentrack |
|---|---|---|---|---|---|---|---|
| Category name | Customer Care and Billing | IS-U billing + FI-CA/Convergent Invoicing | CIS, CRM & ERP for utilities | Customer Information System | Cloud Utility Billing Software | Utility Billing (government) | Billing & Finance (energy suppliers) |
| Central record | account → service agreements → bill segments | business partner → contract account → provider contract | customer accounts | customers ("built around your customers") | customer accounts | accounts | customer/meter points |
| Metered consumption | meter read / item / service-quantity snapshots | consumption items | "meter readings to bills" | (in CIS suite) | meter integrations; metered and non-metered bills | unlimited meters per account | meter points |
| Rates | rate applied to consumption; proration; effective dates | rating (Convergent Charging / rating in CI) | (platform) | (in CIS suite) | unlimited rates and tiers | tiered rates, winter averaging | charging |
| Bill as artifact | bill lifecycle: create → complete → routing → print; cancel/rebill; credit/correction notes; write-off; sequential numbers | invoicing documents → posting documents | "bills generated annually" (millions) | billing module | bill runs; bill printing service | generate, print, mail bills | "accurate... on-time bills" |
| Money cycle | payments, adjustments, deposits, credit & collection, overdue obligations, budget billing | FI-CA postings: bills, dunning, returns, interest, deposits, payments, budget billing | (ERP financials) | multi-fund financials | lockbox/card/ACH; AR reporting | payments, past dues, collections, GL integration | credit and debt |
| Service orders | Service Orders section | (field work adjacent) | field service support | work management suite | mobile service orders | integrated service requests | not observed |
| Bill cycle | bill cycle per account; batch + real-time | mass activities | — | — | weekly → annual cycles | — | — |
| Market structure | 3rd-party charge presentation both directions (pass-through/convergent billing) | deregulated: cross-company invoicing, billing for/by third party | energy + water + EV sectors | electric/water/gas/fiber; muni/county/coop/IOU | municipalities, multi-family, higher-ed, private utilities | water/electric/refuse government | supplier seat vs network seat |
| Care breadth | case management, sales & marketing, quotes, appointments | financial customer care | CRM + engagement | customer service hub | portal + call-center service | customer view | customer engagement |

Reading across the sample: the stable, repeated structure is the **meter-to-bill-to-money cycle over a population of billed service accounts** — accounts binding customers to served premises, meters and measured consumption bound to accounts, recurring bill production under configured rates with a managed bill lifecycle, and the money cycle (payments, adjustments, deposits, arrears/collections) tracked on the same account, with service orders as the office↔field instrument. This structure recurs at every tier (small municipal → co-op/mid-market → enterprise), in both deployment eras, on both sides of the retail-competition split, and across commodities. The "utility billing" name and the "CIS" name both denote this family; the naming correlates with tier and with which function the vendor leads with (billing-led at the small/municipal tier, customer-care-led at the enterprise tier) — not with a difference in object model.

## Canonical Model

### Level 0 — Defining Invariant (deliberately small)

Three jointly-held structures:

1. **The billed service account of record** — a persistent, individually identified account binding a customer to a served premise/service point for a metered utility service, carrying the service state (active / inactive / closed) and the account's financial standing; the record is operated open→sustain→close through service actions (start/stop service, transfers), and it accumulates the whole relationship (consumption, bills, payments, arrears). Remove → a rate calculator or billing engine with no served-customer record.
2. **The metered-consumption basis** — meters bound to the account's service points; periodic reads (manual route reads, estimates, remote/AMI feeds as implementations) accumulating measured usage on the account per billing period; meter identity and lifecycle held in the system. Non-metered fee components ride on the same account as a standard companion, but measured consumption is what makes the billing *utility* billing. Remove → fee-based billing (dues, subscriptions), not a utility billing operation.
3. **The meter-to-bill-to-money cycle** — recurring bill production converting consumption into charges under the operator's configured rates; the bill as the authoritative, lifecycle-managed amount-due record (created → completed → presented → corrected/cancelled-rebilled → written off); and the money cycle — payments, adjustments, deposits, arrears, budget plans, collections — tracked as financial transactions on the same account. The system is the authority for what each served customer owes. Remove → a meter-reading/data tool, or ad-hoc invoicing.

Jointly-held is load-bearing:
- (1) alone = CRM / generic billing;
- (2) alone = meter-data territory (MDMS/AMI family);
- (3) alone = the generic §08 Billing Platform spine;
- (2)+(3) without (1) = a billing engine running over meter data (a component, not the market category);
- (1)+(3) without (2) = fee-based billing;
- (1)+(2) without (3) = meter operations with no revenue loop.

Domain binding (what makes it the *utility* leaf): the commodity is a metered utility service — electricity, water, gas, sewer, refuse, stormwater — delivered continuously to premises and measured there. Remove the binding → the generic Billing Platform (§08). Commodity composition (single vs multi-service) is a variant dimension, not the definition.

Historical check (§24 pattern): the paper-era utility billing office — a ledger card per served account, meter route books with periodic reads, a rate schedule, carbon-copy bills with receipt ledgers, past-due/cutoff notices, budget-payment records — satisfies all three legs at analog level. 1990s DOS/Windows utility-billing packages satisfy all three legs. The definition names no AMI, cloud, portal, mobile app, GIS, or any specific regulatory regime, so older, regional, and platform-native realizations fit.

### Level 1 — Common Mature Structure

- **Bill cycles / route cycles as the operational rhythm** — accounts assigned to billing cycles; batch bill runs over the cycle population; on-demand (off-cycle, final) bills for moves and corrections. (Oracle documents the cycle concept explicitly; MuniBilling offers weekly→annual cycles; the paper era had route books + monthly bill runs.)
- **Bill lifecycle machinery** — error/exception queues with en-masse correction, cancel/rebill, credit notes and correction notes, sequential bill numbering, bill print/mail (increasingly as a service).
- **Service orders** — start/stop/transfer, meter exchanges, investigations, disconnect-for-nonpayment and restoration, dispatched to field crews (often mobile) with results flowing back to the account.
- **Credit furniture** — deposits held against accounts, budget/equal-payment plans, arrears machinery (past-due processing → notices → payment arrangements → disconnect decision), write-offs.
- **Payment channels** — counter, mail, lockbox, online, autopay; payment-processor integration.
- **Customer portal and notifications** as the modern self-service layer.
- **Reporting/dashboards** over consumption, revenue, and arrears; **general-ledger integration** so the money cycle lands in the finance core; **meter-vendor/AMI integration**; APIs as the integration substrate.

### Level 2 — Variant / Optional

- **Commodity composition** — single-commodity vs multi-service accounts (electric + water + sewer + refuse on one bill is a named vendor category).
- **Market structure** — bundled-supply utility (prices and bills the commodity) vs retail competition (supplier seat holds accounts; network utility a separate seat; 3rd-party charge presentation / pass-through billing documented inside products in both directions; SAP documents cross-company/third-party billing for deregulated markets).
- **Ownership tier and embedding** — small-city government packages (often embedded in a government finance suite), cooperative/municipal suites, enterprise platforms; standalone vs ERP-embedded (SAP FI-CA) vs platform-suite (Itineris on Dynamics 365).
- **Deployment** — cloud vs on-premise.
- **Metering era** — manual reads vs interval/AMI-fed billing; interval billing and net-energy-metering true-up as energy-specific extensions.
- **Billing-entity breadth** — some products bill non-utility services on the same engine (submetering for multi-family, HOA/amenities, recreation, fees and fines); the engine generalizes, the utility binding remains the category anchor.
- **Prepaid utility billing** — plausible standard furniture in some markets but unverified this pass; held as unverified variant, not asserted.

### Level 3 — Vendor-specific (kept out of the final document)

- Oracle: bill segments, service agreements (SA types), freeze-at-bill-completion, bill routing, sequential bill numbers, digital signatures, net energy metering true-up, Umbrella Agreement Management, Non-Billed Budgets, Job Streams.
- SAP: FI-CA subledger, contract account, provider contract, billable/consumption items, Convergent Charging/Invoicing, dunning charges as posting class, mass-activity archiving.
- Itineris: UMAX branding, Microsoft Dynamics 365/Copilot platform, UMAX Real-Time (imbalance management).
- Cayenta: multi-fund accounting, HCM modules.
- MuniBilling: MuniReadPro/MuniServicePro module names; call-center/bill-print/lockbox/merchant "as a service" offerings.
- Springbrook: Cirrus branding, allocation billing, winter averaging.
- Gentrack: Debt Management portfolio area, Utilities Best Practice Library.

## Vendor-specific Findings

- The Harris consolidation extends further than the gas pass recorded: Advanced, NorthStar, **and Cayenta** are all Harris companies. Family-structure conclusions rest on cross-vendor corroboration (Oracle, SAP, Itineris, MuniBilling, Springbrook, Gentrack).
- Oracle documents the bill lifecycle with unusual depth (cancel/rebill, credit/correction notes, write-off, sequential numbers, digital signatures) — evidence that the *bill as a managed artifact* is a first-class object of the Type, not just a printed output.
- SAP realizes the money side as a purpose-built subledger (FI-CA) inside the ERP — the same cycle, different philosophy; useful as the proof that the cycle, not any particular packaging, is the invariant.
- MuniBilling's market breadth (multi-family submetering, higher-ed, private utilities; billable services incl. HOA, recreation, fees) shows the flexible-billing-engine pole generalizing beyond utilities while keeping the utility category name.
- Oracle's pass-through/convergent-billing warning and SAP's deregulated-market note are direct in-product evidence of the retail-competition market structure — the same Type serves both seats with configuration, not a different object model.

## Boundary Findings

- **vs Utility Customer Information System / CIS (unprocessed sibling)** — the central taxonomy question of this pass. Finding: **one family, two names/poles.** The market's "utility billing" products (MuniBilling, Springbrook, and Cayenta's own CIS) carry the *full* family structure — accounts, meters, service orders, money — not a bare billing engine. The gas pass's characterization of this leaf as "the billing engine slice" is therefore **refined from this side**: a bare billing engine (charges + bills without the service-account spine and service-order loop) is a *component* of the Type, but the product category named "utility billing" is the full family at the billing-led tier. The honest seam: **billing-led pole** (the meter-to-bill-to-money cycle is the organizing spine; the customer record and care functions exist to serve the money cycle; the bill cycle is the operational rhythm; the name dominates the small/municipal tier) vs **customer-care-led pole** (the customer/service record is the organizing spine; billing is one function among care, case management, marketing, quotes, appointments; the name dominates the enterprise tier). L0 is shared; the difference is emphasis, breadth (L1/L2), and tier. **Keep-both recommended**; forward note recorded for the CIS pass to test from its side.
- **vs Billing Platform (§08, processed)** — DISCHARGED from this side: utility billing satisfies the generic spine (billing accounts + charge computation + bill as authoritative lifecycle-managed record + tracked settlement) and adds the utility-specific machinery: the metered-consumption basis, service-state coupling, utility rate schedules, bill cycles over a served population. That pass's structural test ("satisfies the generic spine but adds utility-specific machinery; kept as a separate leaf") is RATIFIED.
- **vs Gas Utility Management (processed)** — DISCHARGED: the vertical-edition framing is RATIFIED from this side. This leaf is the horizontal family; the gas leaf is the same L0 plus the piped-gas domain binding and its market structures. The gas pass's flag ("those passes should test the vertical-edition framing") is answered; keep-both holds. One refinement recorded: the gas pass's "billing engine slice" characterization of this leaf is corrected per the CIS finding above.
- **vs Meter Data Management System (processed)** — MDMS holds billing-quality data (VEE, bill determinants) and publishes them *to* billing/CIS; here the meter exists to produce bills and the bill is the object of record. A UB deployment on manual reads is complete without any MDMS; an MDMS without accounts/bills is not this Type.
- **vs Advanced Metering Infrastructure (processed)** — the device/collection estate upstream; not an object of this Type's world beyond "reads arrive".
- **vs Utility Rate Management (unprocessed)** — expected seam: rate design/simulation/analysis vs rate *execution* inside the bill cycle. Forward note recorded.
- **vs Utility Revenue Assurance (unprocessed)** — expected seam: leakage control over the revenue chain vs *running* the revenue cycle. Forward note recorded.
- **vs Water Utility Management (unprocessed)** — expect the same vertical-edition pattern as gas (the gas pass predicted it; Itineris, Gentrack, Springbrook all carry water as a sector of the same family). Forward note recorded.
- **vs Utility Field Service Management (unprocessed)** — field work appears here as service orders bound to service accounts; the horizontal field-service Type owns crew scheduling/workforce machinery in its own right.
- **vs Customer Energy Management (processed)** — customer-side self-service over one's own energy vs the utility-side billing operation; the portal layer here is a capability, not the Type.
- **vs EV Charging Billing & Roaming (processed)** — session-based charging commercial records (CDRs) vs periodic metered billing; Itineris ships an EV-operator back-office as a *separate sector* from its energy/water utility CIS — corroborates the seam from the market side.
- **vs Telecom Charging Platform (processed)** — real-time balance drawdown (charging) vs periodic bill production (billing); the billing-platform pass's rule holds here.
- **vs Rent Collection / property-management billing (§17)** — contractual rent vs metered service; a tenant ledger has no consumption basis. Reasoning-level, unsampled.
- **"Remove what to become another Type" summary**: remove the money cycle → meter-data/field tooling; remove metered consumption → fee-based billing / generic Billing Platform; remove the service-account spine → a billing engine component; remove the utility binding → generic billing; move the organizing spine to the customer-care record → the CIS pole of the same family.

## Uncertainties

1. **NISC (co-op pole)** unreachable ×2 across passes — the cooperative tier is corroborated only via Cayenta's customer-type list and the gas pass's NorthStar fetch; no NISC claims drawn.
2. **Prepaid utility billing** machinery unverified this pass; held as unverified variant.
3. **Regulatory/consumer-protection overlays** (deposit rules, disconnection restrictions, medical protections) observed only as capability classes (deposits, collections, service-state coupling); jurisdiction-specific programs not researched.
4. **SAP evidence** taken from verbatim search-index excerpts of official Help Portal pages (direct fetch JS-rendered); marked A−, quotes verbatim.
5. **Same-vendor consolidation** — three of the extended sample (Advanced, NorthStar, Cayenta) are Harris; contained by cross-vendor corroboration, recorded.
6. **Exact tier boundaries** between "utility billing" and "CIS" naming are a market-positioning observation, not a measured one; held at moderate strength.

## Final Synthesis

The Utility Billing Platform is the utility operator's meter-to-bill-to-money system of record: served premises held as billed service accounts, meters and measured consumption bound to those accounts, and a recurring bill cycle converting consumption into charges under configured rates — with the bill as the authoritative, lifecycle-managed amount-due record and the money cycle (payments, adjustments, deposits, arrears, collections) tracked on the same account, coupled to service state through service orders. The market realizes one family structure across all tiers and both market structures; the "utility billing" and "CIS" names are two poles of that family (billing-led vs customer-care-led), correlated with tier; the gas and water leaves are commodity vertical editions of the same L0. What varies — commodity composition, market seat, tier, deployment, metering era, billing-entity breadth — is variant dimension, not definition.
