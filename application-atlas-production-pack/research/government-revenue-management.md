# Research Notes — Government Revenue Management

Research date: **2026-09-08**

## Research Goal

Understand the Application Type sold and used under the "government revenue management" umbrella: what the software's world consists of, who operates it, what the core objects and lifecycles are, how money owed to a government moves from charge to collected cash, and where the Type's boundaries sit against adjacent government-finance Types (Tax Administration, Property Tax Administration, Utility Billing, Public Financial Management) and private-finance Types (invoicing, collections, payment processing).

## Initial Boundary

Working hypothesis before research:

- Government Revenue Management = the government-side "money-in" system: billing / assessment of what payers owe (taxes, fees, fines, service bills) + collection (counter, online) + delinquency handling + reconciliation/reporting to the finance function.
- Nearest neighbors: Tax Administration System (filing/assessment/audit of tax law), Property Tax Administration (appraisal/roll), Utility Billing (metered service), Public Financial Management System (treasury/expenditure), Invoicing Application / Collections Platform / Payment Gateway (private-sector analogs).
- Known market-usage ambiguity: the label "revenue management" is used by at least three product classes — (a) billing & collections systems of record, (b) revenue recovery/compliance collections, (c) payments/experience layers. Research must decide whether these are one Type with packaging variants or separate Types.
- Unknowns: jurisdictional spread (local vs national tax authority), whether revenue forecasting/budgeting is inside the Type (hypothesis: no — separate leaves exist), regional (non-North-American) realizations.

## Research Questions

1. What revenue sources do these systems manage, and how are they configured?
2. What is the central object — the payer account, the bill, the case? How do they relate?
3. How are charges generated (from what source data, with what rate/fee machinery)?
4. How does payment collection work across channels (counter/cashiering, online, mail, recurring)? How are payments applied and receipted?
5. What happens when an account goes unpaid — delinquency states, penalties/interest, notices, payment arrangements, enforcement?
6. How is collected cash attributed, reconciled, and reported (deposits, funds/GL, audit)?
7. Who operates the system (roles), and what does the payer/citizen see?
8. Which capabilities are definitional vs common vs variant vs vendor-specific?
9. Where is the boundary vs Tax Administration System, Property Tax Administration/Assessment, Utility Billing, Invoicing, Collections/Debt Collection, Payment Gateway?
10. Historical check: do paper-era treasurer-office practices (tax roll, receipt book, delinquent list, settlement report) satisfy the same core?

## Representative Products

Selected for market representativeness, different product philosophies, and different customer tiers:

| Product | Vendor | Pole / philosophy | Customer tier | Evidence level |
|---|---|---|---|---|
| Catalis Tax — Billing & Collections | Catalis | dedicated property-tax billing & collections system of record (assessment+billing+collections suite heritage) | counties / local treasurers (US, Canada) | A (official product pages, feature-level) |
| SmartFusion — Billing and Revenue | Harris (Harris Local Government) | ERP-embedded billing & revenue family across utility, tax, misc AR, cash collection, permits, licenses | small/medium municipalities, utility districts | A (official product pages, feature-level) |
| Revenue Management (Neumo, formerly GovOS) | Neumo | recovery/compliance collections: delinquency case management, discovery/audit, outreach | state & local agencies | A (official product pages, feature-level) |
| PayIt | PayIt | digital payments & resident-experience layer over existing systems of record | cities → counties → states/provinces (150M+ residents claimed) | A (official product pages, FAQ) |

Market anchor not directly researched: **Tyler Technologies** — the widely cited incumbent for local government revenue/financial software. tylertech.com returned HTTP 403 and help.tylertech.com timed out (2 attempts each class); no product-specific claims are made for it. National tax-authority administration products (SIGTAS/RAMIS class) were not reachable via search (DuckDuckGo timeout) — the national pole is treated as adjacent-Type territory and marked partially researched.

## Sources

Fetched 2026-09-08 (Tier 1–2 official vendor surfaces):

- Catalis — https://www.catalisgov.com/ (solutions map: Payments, Tax & CAMA, Courts & Land Records, Public Works, Citizen Engagement, Regulatory & Compliance)
- Catalis Tax Billing & Collections — https://catalisgov.com/tax-cama/billing-collections/
- PayIt — https://payitgov.com/ (solutions: property tax, utilities, courts/tickets/fines, licensing & permitting, DMV, outdoors, tolling; platform: agency experience, resident experience, payments, integrations, security)
- Neumo (GovOS rebrand) — https://www.govos.com/ → https://neumo.com/ (product families: Revenue Compliance, Justice, Public Administration, Payments, DMV, Platform)
- Neumo Revenue Management — https://neumo.com/products/payment-solutions/revenue-management/
- Harris Local Government — https://www.harrislocalgov.com/ (portfolio: financial management, payroll, HR, billing and revenue software for municipalities)
- SmartFusion — https://smartfusiongov.com/ (product families: Financial Management, Billing and Revenue, Payroll & HR, Citizen Engagement; solutions incl. Tax Collections, Public Works & Utility)
- SmartFusion Billing and Revenue — https://smartfusiongov.com/product/billing-and-revenue (module add-ons: Utility Billing, Tax Collection, Accounts Receivable, Cash Collection, Permitting, Business Licenses)

Unreachable (recorded limitations):
- Tyler Technologies — tylertech.com 403; help.tylertech.com timeout (market anchor carried without product-specific claims)
- SIGTAS / national tax administration vendor docs — no reachable source found in this environment (DuckDuckGo search timeout; no direct URL known)
- Granicus — reachable but its current lineup (Government Experience Cloud: engagement/service/forms/agenda) no longer includes a revenue/payments pillar; excluded from sample

## Product Observations

### Product A — Catalis Tax (Billing & Collections) — evidence layer A

Official product page (catalisgov.com/tax-cama/billing-collections/), 2026-09-08:

- Positioning: "Enterprise property tax collection software for tax billing and management"; "automates tax billing and collections"; "unifying billing, collections, and assessment into a single, easy-to-use platform" (local-government focus).
- Documented capabilities:
  - Ownership history data: "maintain full-scale property information and quickly communicate changes" — property/parcel records with ownership history are part of the working data.
  - Tax calculation: "Calculate taxes and print tax bills across multiple formats for both real estate and personal property" — bill generation from calculation, multiple formats, two property classes.
  - Robust reporting: "extensive reports detailing transactions and deposit history" — transaction + deposit-level reporting.
  - Customer portal: "intuitive e-billing and payment platform" — payer-facing e-billing + payment.
  - Seamless reconciliation: "end-to-end workflows that streamline monthly audits and closings" — reconciliation as designed workflow.
  - Vendor consolidation: "integrating billing, collections, cashiering, and more" — cashiering named as part of the product family.
  - System integration: "Integrate with land recording systems that file and record legal documents including deeds and mortgages" — upstream/adjacent record integration.
- Packaging: SaaS or on-premises; part of a "Tax & CAMA" family (CAMA = Computer Assisted Mass Appraisal, sold as a separate solution; also Property Tax Oversight for state-level oversight bodies; Escrow Payment Management as separate solution).
- Suite context: separate Payments family (Tax Payments, Utility Payments, Court Payments, Child Support Solutions, "Catalis Checkout") — payments as its own product layer.

### Product B — SmartFusion Billing and Revenue (Harris) — evidence layer A

Official product page (smartfusiongov.com/product/billing-and-revenue), 2026-09-08:

- Positioning: "Billing & Revenue suite simplifies complex fee-based services—from utilities to permits and business licenses"; platform family inside a public-sector ERP (Financial Management / Billing and Revenue / Payroll & HR / Citizen Engagement).
- Module add-ons documented:
  - **Utility Billing**: "track customer details, manage meter data", "generate and print bills", "access accounts receivable data instantly", "usage reports", work-order management; "Seamless Integration with Online Payment Solutions".
  - **Tax Collection** (property tax): "generate accurate tax notices", "processing payments", "managing delinquent accounts", "Maintain Audit Trails", print tax notices.
  - **Accounts Receivable**: customer records, "Create Invoices Instantly", "delinquent accounts, customer history, and revenue trends" reporting, automated billing.
  - **Cash Collection**: "front-end cash collection process across various platforms, including utility billing, tax collections, or other payment types"; "payments are accurately processed and recorded, including miscellaneous transactions"; "Print and manage daily receipts"; "Void receipts when necessary".
  - **Permitting**: permits entered, paid for, processed; inspections tracked; "Automatically calculate fees and penalties"; business status flags (bankruptcy, bad checks, out-of-business).
  - **Business Licenses**: "detailed master record for each" business; "print applications, issue licenses, record payments, and track an unlimited history of license activity"; "Automatically calculate late payment penalties".
- Named role personas on the page: Tax Collector, Tax Clerk, Municipal Clerk, Clerk Treasurer.
- Solution page framing: Tax Collection = "streamlines the entire tax process with automation and integration, ensuring accurate and timely billing every time"; Utility Billing = "track customer and meter data, generate and print accurate bills, access real-time accounts receivable details".

### Product C — Neumo Revenue Management (formerly GovOS) — evidence layer A

Official product page (neumo.com/products/payment-solutions/revenue-management/), 2026-09-08:

- Positioning: "Governments lose revenue every year due to delinquencies, misreported taxes, and noncompliance. Neumo Revenue Management helps recover what's owed with automated workflows, advanced skip tracing, and flexible outreach tools." Collections/recovery-centered.
- Documented capabilities ("End-to-End Revenue Management"):
  - Automated workflows: "Streamline case management, prioritize accounts, and reduce staff workload" — collections as case management over accounts.
  - Integrated communications: "Engage constituents with text, email, and automated outreach to improve response rates."
  - Skip tracing and contact accuracy: "Ensure accurate outreach and reduce returned mail."
  - Flexible payment options: "Support online, recurring, and point-of-sale payments for faster collections."
- Value framing: "targeted audits, delinquency tracking, and compliance programs" recover revenue; "Randomized, transparent processes ensure equal treatment for all taxpayers"; "Ad hoc and SQL-based reporting provide real-time insights into performance"; "Recovered revenue and actionable insights help stabilize budgets".
- Suite context: "Revenue Compliance" family (Tax & Licensing, Short-Term Rental, Compliance Auditing, Unclaimed Property) + "Payments" family (Neumo Payments + Revenue Management). "900M transactions processed", "$44B revenue collected" company-level claims.

### Product D — PayIt — evidence layer A

Official site + FAQ (payitgov.com), 2026-09-08:

- Positioning: "customer experience and payments platform for state and local government"; "serve residents, collect revenue, and operate efficiently"; "even complex and identity-sensitive transactions".
- Revenue-type breadth (solutions): property tax, utilities, courts/tickets/fines, licensing & permitting, motor vehicles (DMV), outdoors licensing, tolling.
- Agency (operator) experience: "See every transaction in real time"; "Match transactions, issue refunds and get insights"; "Reconcile in minutes instead of days with AI-powered matching"; admin console for transaction management and refunds.
- Resident experience: "one place to access services, view transaction history, receive personalized notifications"; "Deliver bills, past-due reminders, and other notifications, even across services and departments"; single resident profile across services and jurisdictions.
- Integration posture: "Connect any system of record" — integrations as a platform pillar; PayIt positions itself above the systems that own billing ("Integrations done for you").
- Delivery/commercial model: "transaction-based pricing", launch "in as little as 90 days", PCI DSS Level 1 / SOC 2 Type 2 / ISO 27001/27018 claims.
- Buyer personas named in FAQ: "treasurers, CFOs, finance and revenue directors, tax and DMV leaders, and court clerks".

## Cross-product Comparison

| Dimension | Catalis Tax B&C | SmartFusion B&R | Neumo Revenue Management | PayIt |
|---|---|---|---|---|
| Center object | property-tax bill/collection cycle on parcel+owner records | per-revenue customer accounts (parcel, meter, business, invoice) | collections case over owed/delinquent accounts | payment transaction + resident profile (over external accounts of record) |
| Charge generation | yes — tax calculation → bill print, real & personal property | yes — bills/notices/invoices from meters, fees, licenses, permits | no (starts from owed/delinquent/under-reported obligations) | no (bills delivered; charges owned by integrated systems) |
| Payment application | yes (counter cashiering + portal payments) | yes (cash collection across platforms; online payment integration) | yes (online, recurring, POS) | yes (real-time transaction view, refunds) |
| Delinquency machinery | collections part of billing cycle; reporting includes delinquency via deposit/transaction reports | delinquent accounts tracked (tax + AR), late-payment penalty automation | core purpose: delinquency tracking, prioritized cases, outreach | past-due reminders delivered to residents |
| Enforcement | — (integration to land records implies lien-recording adjacency; not explicit) | — (not explicit) | outreach/skip-tracing-centered; no lien/intercept claims on page | — |
| Reconciliation/reporting | transactions + deposit history; monthly audits/closings | daily receipts; revenue-trend reporting; audit trails; usage reports | ad hoc + SQL reporting, real-time performance insights | real-time visibility; AI-assisted matching/reconciliation |
| Payer-facing surface | e-billing & payment customer portal | online payment integration (partner layer) | constituent outreach (text/email) | full resident portal: bills, history, notifications, one profile |
| Source-of-charge integration | land recording systems (deeds/mortgages); CAMA family alongside | meter data, work orders, permit/licensing events | n/a (recovery of existing obligations) | "connect any system of record" |
| Multi-revenue scope | property tax (family spans utility/court payments separately) | utility + property tax + AR + permits + licenses + cashiering | misreported taxes, delinquencies, compliance (business-licensing heritage) | property tax, utilities, courts/fines, licensing, DMV, tolling |
| Deployment | cloud or on-prem | ERP suite module | SaaS platform | SaaS platform, transaction-priced |
| Jurisdiction tier | county/local (US/CA), state oversight product exists | city/county/utility district | state & local agencies | city → state/province |

Reading of the comparison:

- Four products, four different centers of gravity, but one shared spine: **payer/account records → owed amounts → collection actions → payments applied → money attributed/reconciled/reported**.
- The billing pole and the recovery pole are complementary halves of one receivables cycle (create-and-collect vs find-and-collect); the payments layer is a channel/visibility realization of the collection stage.
- Delinquency machinery appears in every product in some form (tracking, penalties, reminders, outreach) — it is the cycle's second phase, not an add-on.
- Reporting/reconciliation appears in every product in some form (deposit history, daily receipts, SQL insights, real-time matching) — accountability to the finance function is structural.

## Canonical Model

### L0 — Defining Invariant

Minimal structure without which the product stops being recognizable as government revenue management:

1. **The payer receivable account of record** — an identified payer (property owner, business, resident) and one or more per-revenue-source accounts (parcel/tax account, service account, license account, receivable/case) that persist across cycles and carry balances owed to the government.
2. **The owed-to-collected cycle** — owed amounts arise (from configured charges the government levies, or from delinquent/under-reported obligations identified for recovery) and are worked toward settlement: charge/bill/notice → payment acceptance and application (partial payment normal) → delinquency state with rule-driven consequences → further collection actions → settled/closed.
3. **Attribution and accountability of the money** — payments are applied to specific charges, attributed to revenue sources / the government's funds, and reconciled and reported (deposits, transaction history, collection performance) for the finance function and audit.

Jointly-held is load-bearing:

- 1+3 without 2 → a balance register / static bill list (no management of the cycle).
- 2+3 without 1 → payment processing with receipts but no standing payer relationship (a payments platform).
- 1+2 without 3 → a collections operation that cannot close the loop with treasury/audit — incompatible with the government context, where the money must reconcile to public funds.

Government-ness is part of the invariant in a second sense: the charges arise from the government's own statutory/administrative acts (levies, fee schedules, fines, tariffs), not from commercial price-setting, and the money belongs to public funds.

Historical check (§24 analog): the paper-era treasurer/collector office satisfies this core — tax roll as payer receivable accounts (parcel + owner + amount levied), receipt book as payment application, delinquent list with penalty accrual and lien/turnover as the delinquency cycle, annual settlement report + deposit reconciliation as attribution/accountability. No portal, card rails, or cloud required. Regional breadth (reasoning-based, not directly sampled): UK council-tax arrears collection (liability orders), Indian land-revenue collection, and other jurisdictions' treasurer offices fit the same three-part core — the core is jurisdiction-neutral; enforcement mechanisms differ.

### L1 — Common Mature Structure

Very common in modern products but not required to recognize the Type:

- Rate/fee/levy configuration per revenue source (tax rates/mill levies, fee schedules, penalty & interest rules).
- Counter/cashiering operations: take any payment type, print receipts, void receipts, daily batch close; miscellaneous transactions.
- Online self-service: payer portal with bills, payment history, e-billing, notifications (including past-due reminders).
- Multi-channel payment acceptance: card/ACH/cash/check; online, counter, mail/lockbox, recurring.
- Delinquency automation: penalty/interest accrual, notice sequences, delinquent-account tracking and reporting.
- Payment arrangements: recurring payment setups; escrow/prepayment arrangements (tax escrow documented in one sample, recurring documented in another — treated common-with-caution).
- Reporting & reconciliation machinery: deposit history, transaction reports, revenue-trend reporting, audit trails, GL/finance export or integration.
- Integration with the systems that create the obligations: assessment/CAMA rolls, utility metering, permitting/licensing systems, court/fine systems; land records.
- Refund handling.

### L2 — Variant / Optional Structure

Depends on segment, jurisdiction, packaging, business model:

- Packaging poles (see Boundary Findings): property-tax-centric collection suite vs ERP-embedded multi-fee family vs recovery/compliance collections vs payments/experience layer.
- Revenue-scope: single-source depth (property tax) vs cross-source breadth (everything the government bills).
- Recovery/compliance machinery: discovery/audit of unregistered or under-reported obligations, skip tracing, randomized audit selection — the recovery pole's differentiators.
- Jurisdiction tier and statutory regime: city / county / state-provincial; enforcement machinery (liens, tax sales, license holds, intercepts, collector/attorney handoff) varies by jurisdiction — supported rather than invented by the software.
- Payer identity model: per-agency accounts vs one resident profile spanning services and jurisdictions.
- State-level oversight variants (oversight of local collectors/roll data).
- Deployment: SaaS vs on-premises; transaction-based commercial models for payment-layer products.
- AI-era additions: automated reconciliation matching, AI discovery/guidance (current-generation, uneven).

### L3 — Vendor-specific Structure

Kept in research notes only:

- Catalis: CAMA + GIS sketching family, assessment e-file, Property Tax Oversight (state oversight bodies), Escrow Payment Management as a separate solution, "Catalis Checkout", 529/ABLE plan administration (Regulatory & Compliance family).
- SmartFusion: utility work orders, business status flags (bankruptcy / bad checks / out-of-business), SmartAP vendor-payment rebate product (payments-out, different module).
- Neumo: skip tracing, randomized/transparent audit selection, SQL-based reporting, GovOS heritage (short-term-rental compliance, unclaimed property).
- PayIt: Smart Works suite naming (Smart Reconcile, Smart Guide, Agent Assistant), 90-day launch posture, 9x-satisfaction and $6-per-transaction marketing claims, GovLab event.

## Vendor-specific Findings

- The recovery pole (Neumo) frames "revenue management" as recovering what governments lose to delinquency/misreporting/noncompliance — a collections-and-compliance framing, not a billing framing. Its differentiators (skip tracing, randomized audit selection) are not observed in the other samples and stay product-class-qualified.
- The payments pole (PayIt) explicitly does not own the billing record ("connect any system of record") — direct vendor evidence that a payments layer can sit outside the receivables system of record while still carrying the "collect revenue" job.
- The ERP pole (SmartFusion) dissolves "revenue management" into a family of modules named after the money's origin (Utility Billing, Tax Collection, Accounts Receivable, Cash Collection, Permitting, Business Licenses) — evidence that the market often realizes this Type as a module family rather than one product.

## Rejected Findings

- "Revenue forecasting/budgeting belongs to this Type" — rejected. Revenue estimation appears only as marketing adjacency ("stabilize budgets", "long-term financial planning") in one sample; the directory holds Public Budgeting Platform and Public Financial Management System as separate leaves. No sampled product documents forecasting as a core structure.
- "Government Revenue Management = Tax Administration" — rejected as a merger. The national revenue-authority regime (taxpayer registration, self-assessment filing, audit of declared tax) is a different operating center from the treasurer-side receivables cycle; no sampled product implements the national-authority regime. (Boundary recorded; joint review recommended when Tax Administration System is processed.)
- "This Type is property tax only" — rejected. Property tax is the deepest single-source realization, but the ERP and payments samples span utilities, licenses, permits, fines, DMV and more; the receivables cycle is the invariant, the revenue source is the variant.
- "Cashiering is definitional" — rejected for L0. Two of four samples document counter operations; a jurisdiction could run this Type without a counter (all-digital). Common mature structure, not invariant.
- "AI reconciliation is definitional" — rejected (current-generation feature in one sample; Delinquency-case prioritization automation in another; era-current layer).

## Boundary Findings

| Nearby Type | Relationship | Discriminator ("what to remove / what remains") |
|---|---|---|
| Tax Administration System (§24 sibling, unprocessed) | adjacent, regime-side | Tax administration centers on the taxpayer registry + declaration/filing/assessment + audit of tax law (self-assessment regimes, national/state revenue authorities). This Type centers on the owed-account → cash cycle operated by treasurers/revenue offices. Remove the receivables cycle and keep registration/filing/audit → tax administration. Remove the filing/assessment regime and keep owed accounts → collections → this Type. Overlap zone: local property-tax products fuse appraisal+billing+collection (Catalis sells both). Joint review recommended when that leaf is processed. |
| Property Tax Administration (§24 sibling) | upstream sibling | Property tax administration owns appraisal/roll/exemptions (the obligation's creation); this Type owns the collection cycle (the obligation's settlement). Direct market evidence: Catalis sells CAMA and Billing & Collections as separate solutions. Remove billing/collection from a property-tax product → it becomes assessment administration. |
| Property Assessment System (§24 sibling) | upstream | Valuation/appraisal only; no receivable accounts, no payments. |
| Utility Billing Platform (§19) | overlapping module Type | The §19 leaf centers the metered-service utility operator's meter→bill→pay cycle. Inside local government, utility billing commonly lives as one revenue source/module of this Type (SmartFusion module; PayIt vertical). A pure utility billing product remains a different Type; the boundary is center-of-gravity (single metered service vs cross-source receivables management). |
| Invoicing Application (§08, processed) | adjacent (private analog) | Invoicing is document-centric per-transaction payment demand between commercial parties. This Type is a standing multi-revenue receivables operation over persistent statutory accounts (tax cycles, licenses, tariffs) with fund accounting and public audit. Remove the standing accounts + statutory machinery → invoicing. |
| Debt Collection Management / Collections Platform (§08) | adjacent | Private-lens debt portfolios and agency operations vs government revenue recovery grounded in statutory obligations and public accountability. The recovery pole of this Type (one sampled product) is the overlap zone; it stays here because the obligations are government revenue (taxes/fees), not purchased or contracted debt portfolios. |
| Payment Gateway / Payment Processing (§08) | embedded rails / layered service | Rails move money; this Type owns the owed amount and the payer account. A payments layer (one sampled product) integrates to systems of record and adds adoption/reconciliation — adjacent packaging, not the same Type; the Type is recognizable without any rails (paper era). |
| Public Financial Management System / Public Budgeting Platform (§24 siblings) | downstream / upstream | PFM owns budget execution, expenditure, treasury-wide financials; budgeting owns revenue estimation. This Type feeds receipts in (deposits, GL export) and consumes levy/fee authority — money-in operationalization, not planning or expenditure. |
| Government Procurement Platform (§24, processed 2026-09-08) | opposite direction | Procurement = public money-out under formal process; this Type = public money-in under statutory charge. Complementary halves of public finance. |

## Uncertainties

1. **National tax-authority pole unsampled.** SIGTAS/RAMIS-class products could not be reached; the claim that the national revenue-authority regime is a distinct Type rests on directory structure + the local-market sample, not on direct observation. Marked for joint review with Tax Administration System.
2. **Tyler Technologies (market anchor) unverified.** 403/timeout. The market-centering claim (Tyler as incumbent) is common knowledge in the segment but carries no product-specific evidence here; the abstraction does not depend on it.
3. **Enforcement depth (liens, tax sales, intercepts)** — structurally expected in this Type and adjacent to land-records integration (one sample integrates with deed/mortgage recording), but no sampled page documents enforcement workflows at operational depth. Assertions kept generic.
4. **Payment plans** — prepayment/escrow documented in one sample, recurring payments in two; "payment plan" as an arrears-installment construct is plausible but not directly documented at feature level. Kept qualified.
5. **Regional (non-North-American) realizations** — reasoning-based only (historical/regional check done by argument, not by sampling regional products). The core is phrased jurisdiction-neutral to absorb this.
6. **Customer-portal universality** — three of four samples document payer-facing digital surfaces directly or via the payments-layer pole; one (SmartFusion) documents online-payment integration rather than a native portal. Portal treated as common, not definitional.

## Final Synthesis

Government Revenue Management is the treasurer/revenue-office system of record for money owed to a government. Its canonical core is three jointly-held structures: (1) persistent payer receivable accounts across the government's revenue sources; (2) the owed-to-collected cycle — charges arise from the government's own levies/fees/fines/tariffs (or from identified delinquent/under-reported obligations) and are worked through billing/notice → payment application → delinquency consequences → enforcement or settlement; (3) attribution and accountability — payments applied to specific charges, attributed to revenue sources/funds, reconciled through deposits, and reported for public finance and audit.

The market realizes the Type through four packaging poles — property-tax-centric collection suites, ERP-embedded billing & revenue families, recovery/compliance collections, and payments/experience layers — which are variants of one receivables cycle, not separate Types. Upstream (assessment/appraisal, tax-filing regimes) and downstream (PFM/GL) neighbors own the obligation's creation and the money's ultimate accounting; this Type owns the settlement of the obligation. The paper-era treasurer office (tax roll + receipt book + delinquent list + settlement report) satisfies the core, so none of the modern digital machinery is definitional.
