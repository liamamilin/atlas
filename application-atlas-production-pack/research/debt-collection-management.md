# Research Notes — Debt Collection Management

Research date: 2026-09-08

## Research Goal

Understand "Debt Collection Management" as an Application Type from real products: what a software system for a professional debt recovery operation (collection agency, debt buyer, debt servicer, collection law firm) actually consists of, what objects it manages, how placed/purchased debt moves from intake to outcome, who operates it, and where its boundary lies against the neighboring §08 leaves — especially Collections Platform (processed: first-party own-book delinquency collections) and Collections Automation Platform (processed: B2B AR dunning) — plus Loan Management System, Accounts Receivable Management, Credit Management Platform, and the unprocessed Debt Management Application.

## Initial Boundary

- This is a **flagged leaf**. The collections-platform pass (2026-09-07) recorded in STATUS.md Boundary Issues: platform families straddle the first-party/third-party seam (Qualco's roster includes debt purchasers Intrum/Hoist Finance/Cabot/doValue; Finvi sells Katabat to first-party lenders and Velosidy/Simplicity to collection agencies; C&R Debt Manager markets vendor oversight of agencies/law firms) — **this leaf's core should anchor on the agency-native object model (placed/purchased accounts, creditor-client portals, skip tracing, contingency economics) rather than platform family membership; joint review recommended**. This pass adopts that instruction as its primary hypothesis and tests it against evidence.
- Working hypothesis before research: the operator (agency/buyer/servicer/law firm) pursues debt it did not originate through an ongoing customer relationship — debt placed by creditor clients or acquired in portfolios. The seam vs Collections Platform is ownership of the obligation/relationship; the seam vs Collections Automation Platform is object class (delinquent repayment obligations / placed debt vs open trade invoices).
- Initial understanding: users are collectors, account handlers, skip tracers, legal/asset specialists, client-services staff, compliance officers, and agency management. The pursued parties are mostly consumers (also businesses in commercial collections). The system holds accounts, debtors/clients, promises, payments, letters, commissions, remittances.

## Research Questions

1. What is the unit of record — is it the debtor, the account, the placement, the portfolio?
2. Who is the "client"? How is the creditor relationship modeled, and what flows between client and operator (accounts in, money out, reports back)?
3. What are the compensation mechanics the system must support (commission/contingency, fee models, remittance bases, agency invoicing)?
4. What does the collector's working loop look like (queues, tracing, contact, promises, payments, plans)?
5. What outcome states can an account reach (paid, settled, plan, legal, recalled/returned, uncollectible, bankruptcy)? How do recall/return and legal referral work?
6. Which machinery is agency-signature (skip tracing, client portals, bureau reporting, placement files, dialer economics) and which is shared with first-party collections?
7. How does the debt-buyer pole differ from the agency pole (ownership of debt vs agency for creditor)?
8. Where exactly is the boundary vs Collections Platform (first-party) — is the prior pass's placement/charge-off seam confirmed from this side?
9. What would older, regional, non-cloud products (paper-era agencies, PC-era packages) need in order to satisfy the definition?
10. Where does Debt Management Application (unprocessed sibling) sit — is it consumer-side?

## Representative Products

Selection: market representation + documentation completeness + different philosophies + different customer tiers, with the prior flag in mind (must include agency-native vendors on both sides of the seam; must not build the core on platform-family membership).

1. **Finvi Velosidy** — cloud-native collections platform for third-party collection agencies (North America). Finvi (formerly Ontario Systems) is the largest ARM-sector software family; its own product taxonomy splits Velosidy (third-party agencies) / Katabat (first-party lenders) / Simplicity (small agencies) / Artiva HCx (healthcare RCM) — the vendor itself operationalizes the first-party/third-party seam.
2. **Collect! (Comtech Systems)** — independent, PC-era (since 1988), SMB/mid-market agency workhorse with the deepest publicly reachable Tier-1 documentation; used by first-party, third-party, and legal collections. Documents the agency-native object model at field level.
3. **Qualco Collections & Recoveries (QCR)** — European enterprise platform "covering in-house and 3rd party operations"; used by banks AND debt purchasers/debt servicers (Intrum, Cabot, doValue, Hoist Finance logos); ships a dedicated Outsourced Collections module and a UK DCA accelerator; ExtraCollect covers creditor-side panel management. European debt-servicing pole.
4. **C&R Software Debt Manager** — global enterprise collections & recovery suite (40+ years heritage); creditor-side deployments dominate the testimonials, but it ships Partner ecosystem / vendor oversight machinery — strong boundary evidence for how the creditor side hands off to agencies, and a reminder that platform families span both sides.

Boundary-contrast products (fetched but not sampled as core):
- **C&R PlacementsPlus / Agency Network** — creditor-side placement automation and secure agency data exchange: placement, optimization, agency performance/compliance oversight, remittance of placement data. Confirms agency placement is managed from the creditor side as an exit ramp.
- **Qualco ExtraCollect** — "outsourced debt collection panel management" — the same creditor-side surface in the QCR family.
- **Finvi Katabat** — first-party lenders product line (already sampled by the collections-platform pass).

## Sources

All fetched 2026-09-08 (HTTP OK unless noted):

- C&R Software — Debt Manager product page — https://www.crsoftware.com/products/debt-manager (fetched OK)
- C&R Software — Agency Management (PlacementsPlus / Agency Network / Placement Optimizer) — https://www.crsoftware.com/agency-management (fetched OK)
- Finvi — Velosidy product page (third-party agencies) — https://finvi.com/velosidy/ (fetched OK)
- Finvi — product taxonomy via Velosidy page nav (Velosidy / Artiva HCx / Katabat / Simplicity; blog categories "ARM 1st Party" vs "ARM 3rd Party")
- Qualco Technology — Collections & Recoveries (QCR) product page — https://www.qualco.tech/systems/qualco-collections-recoveries (fetched OK; first attempt /solutions/collections-recoveries/ → 404, root page → OK)
- Collect! (Comtech Systems) — product site — https://www.collect.org/ (fetched OK)
- Collect! — Help Index (v13) — https://www.collect.org/documentation/ → /cv13/Help/index.html (fetched OK)
- Collect! — Client form documentation (field-level) — https://www.collect.org/cv13/Help/client.html (fetched OK)

Not sampled / not asserted: Experian Tallyman (previous pass found it unreachable-class; not attempted here), Finvi Simplicity and Artiva HCx (nav-level evidence only), DebtPayPro, DAKCS, Nortridge collections module. Per source-access limitation, no claims are made about them.

Evidence layers: Collect! documentation = Tier 1 (operational docs); Velosidy / QCR / Debt Manager / Agency Management = Tier 2 (official product pages at capability level). Marketing performance figures on those pages (percentages, dollar volumes, ROI claims) are **not** reproduced anywhere as facts.

## Product Observations

### Finvi Velosidy (third-party agencies) — Tier 2

- Self-positioning: "A modern SaaS-based collections platform that allows third-party collection agencies to increase revenue while lowering the cost to collect and minimize operational risk." Industry page: "Collections Agencies — ARM agencies have been using Finvi's collections and payments solutions for 45 years…"
- AI engine embedded in the workflow: Best Channel to Collect, Best Time to Call, Propensity to Pay (P2P scoring beyond credit scores/income thresholds), Best Payment Arrangement (recommends arrangements "within the bounds of customer expectations", "captures tribal knowledge from top collectors"), Agent Queuing ("dynamic, AI-powered queues… prioritize the right account at the right time", combining P2P/Best Time/Best Channel, agent-selected variables).
- "Compliance, baked in": "regulatory guardrails into every workflow" (structural claim, no regime specifics on page).
- Built on Oracle Cloud Infrastructure; security-first posture.
- Partner ecosystem (the agency's tooling ring): credit data & skip tracing (LexisNexis "collections-and-recovery/skip-tracing", Experian "skip-tracing tools", TransUnion "third-party collections" page, IDI, IMS "data hygiene and compliance scrubbing", RNN "consumer data and asset verification"), bankruptcy monitoring/scrubbing (BankruptcyWatch), legal e-filing (InfoTrack "allows agencies to file court documents electronically"), legal-threat monitoring (WebRecon, "FDCPA/TCPA lawsuits"), dialers (TCN "integrated dialer on Velosidy", LiveVox), compliant SMS/print/mail (Nordis, Renkim, CompuMail "automates the secure delivery of collections letters"), client and consumer portals (Applied Innovation "client and consumer portals make it easy for agencies, creditors, and consumers to collaborate, manage accounts, and complete secure transactions"), dispute management (Provana), analytics (Intelitech), conversational AI (Floatbot, Skit.ai).
- Finvi taxonomy (from page nav): Velosidy → Collections Agencies; Katabat → banks/fintech "first-party lenders"; Simplicity → "small businesses and start-up debt collection agencies"; Artiva HCx → healthcare RCM (providers + outsourcers managing multiple clients). Blog taxonomy: "ARM 1st Party" / "ARM 3rd Party". The vendor's own vocabulary confirms first-party vs third-party as the industry's structural split.
- Testimonials are from collection agencies (Associated Credit Services, Bonneville).

### Collect! (Comtech Systems) — Tier 1 (documentation)

- Positioning: "Receivables Management Software… helps collection agencies, credit unions, and billing offices manage receivables efficiently and profitably." Use cases: "Collection Agencies — First-party, third-party, and legal collections with full compliance automation"; credit unions/banks (internal recovery, early-out programs); medical/dental billing; government (municipal fines, tax recovery); legal offices (judgment enforcement, asset tracking); finance & leasing (auto loans, equipment leasing, consumer finance recovery). Since 1988; 1,400+ companies; 40 countries.
- One platform, two built-in portals:
  - **Client Portal** — "Give your clients real-time visibility into their accounts… Real-time visibility into account status, balances, and progress"; "Reporting scoped to exactly the accounts and portfolios each client should see"; secure document exchange and e-signature. The client is the creditor, and portal visibility is per-client scoped.
  - **Consumer Portal** — self-service payments, flexible payment plan setup, dispute submission "with a full, compliance-ready audit trail"; payments post straight back into the account.
- Core capabilities (vendor's own capability list):
  - Credit Bureau Reporting — "Furnish account data to Equifax, Experian, and TransUnion in compliant Metro 2 format, with a full audit trail of every submission."
  - SMS Integration, Dialer Integration (predictive/auto-dialer platforms for outbound campaigns).
  - **Skip & Score** — "Built-in skip tracing and account scoring to locate hard-to-find debtors and prioritize who to contact first."
  - **Client Organization** — "Layer accounts by client, portfolio, or department with infinite hierarchies and roll-up reporting."
  - **Debtor Organization** — "Link related accounts under a single debtor record for a complete picture of everything they owe."
  - **Judgment Records** — "Track judgments, liens, and asset information alongside the account for full legal-recovery visibility."
  - Task Management & Automation — "Configurable Work Queues and business-rule automation keep every collector on the right account at the right time."
  - Letter Services & In-House Printing — automated letter batching, mail-house integration, tracked against accounts.
- Help Index (Tier 1) confirms the operational vocabulary: Client, Debtor/Accounts, Operator (collector), Contact Plans/Action Plans, Promises ("Automatic Promise Actions - Payment Posting Options"), Transaction Types, Payments/ACH/payment gateways, Letters/Reports writer, Access Rights, Account Toss ("use account toss" = distributing accounts to operators, incl. custom distribution), Account Matching Batch, Archiving, Analytic Dashboard, Web Host portals, REST API endpoints (create/read/update records, contact plans, reports/letters), Commission Rate Plans ("How To Use Commission Rate Plans"), Client Payments ("How To Enter A Client Payment"), Invoices and Statements ("Generate And Print Invoices And Statements"), **"Understand Net Or Gross Or Combined Remittances"**.
- Client form (field-level documentation) — the agency-native object model in detail:
  - Client # / Alt Client #; **Owned By Client** ("master client" hierarchy — group client accounts for account security, auditing, reporting; hierarchical client ownership controls search/account-access scope; Web Host Client Group uses it to control which clients a master client views).
  - Tabs: Debtors ("all debtors listed by this Client", ACTIVE/CLOSED modes), **Invoices** ("Invoice/Statement generated for this Client"), **Payments** ("Client Payments"), Notes, Contacts, Attachments.
  - **Commission To Date** (total commission calculated on all accounts for this client; option "Only payments for comm to date"), Success Rate ("ratio of Paid to Listed accounts… All Paid X 100 / All Listed").
  - Financial roll-ups per client: Listed ("sum of the Principal and Original Interest… of all of the client's debtors"; judgment balance used where a judgment exists), Paid, Closed, Owing, Principal, Interest, Fees, **Legal Fees**, Miscellaneous, Other Charges, Adjustments.
  - **Client Settings** ("contains many settings that will determine how Debtors, Payments, Invoices and Credit Bureau Reporting are handled for this Client… automatically entered into all related forms") — per-client configuration cascades into account behavior.
  - CBR per client: "If you are reporting to Credit Bureaus by client, Trans Union codes go here… Experian codes… Equifax codes… useful if you have a client that wants you to report with their Credit Bureau Account in addition to yours"; Type field requires a valid Metro 2 "creditor classification"; Age Out Report For CBR (7-year).
  - Run Plan (Contact Plan on the client), Operator assignment, Status/Inactive, client timezone (dialing-aware).
- Interpretation: the Client object is the creditor-of-record; accounts are *listed* by clients; the agency's own accounting (commissions earned, client payments received/remitted, invoices issued) hangs off the client. Debtors can carry judgment balances and legal fees — legal collections is inside the same object model.

### Qualco Collections & Recoveries (QCR) — Tier 2

- Positioning: "The #1 debt management software, handling all credit and receivable types, from early collections to legal processes and recoveries. Cover in-house and 3rd party operations. Comply with local regulations… whether integrated into a banking ecosystem or used as a standalone system of record." Manages NPLs (non-performing loans).
- Trusted-by logos: Intrum (testimonial: "creating the world's largest debt-servicing…"), Cabot Portugal (case study), Credit Factor, EuropaFactor, doValue/Hoist Finance (root page) — the debt-purchaser/debt-servicer tier of the market.
- Modules & capabilities: Omnichannel Collections (conversational messaging, bots, live agents, payment processing); Digital Self-Service Portal (24/7 account access, flexible repayment plans, online transactions); **In-House Collections**; **Outsourced Collections** — "Manage external collection activities via automated **assignment and recall**. Facilitate third-party access and enable system integration and performance monitoring"; Decision Engine (analytics, real-time modifications, expandable data hub, customer assessments); Legal Management (customisable process design, **expense tracking**, progress monitoring); Collateral & Real Properties (ownership, rights, valuations, secured debts); Restructuring (product definition to implementation, affordability-based); System of Record (full balance management, GL/ERP integration); Migration & Integration; Corporate Management (portfolio analysis, risk assessment, asset monitoring).
- QCR Accelerator: pre-configured editions — one for small/mid banks & retail lenders (early-stage collections), one "purpose-built for the UK market… Debt Collection Agencies" ("covering first, second, and pre-legal placements"; vendor-claimed performance figures not reproduced).
- Multi-country: 30+ countries, multi-language, multi-currency, per-country setups; GDPR support clauses described at capability level.
- Reports: daily activities, payments, proposed arrangements, portfolio performance over time, collection strategies' efficiency, **outsourcing models**, legal or restructuring processes.
- ExtraCollect (family sibling, creditor side): "streamlines outsourced debt collection panel management."

### C&R Software Debt Manager — Tier 2

- Positioning: "comprehensive debt collections solution managing the entire risk lifecycle… handles over $8 trillion in active accounts" (volume claim not reproduced as fact); "650+ different types of debt"; testimonials from banks, retailers; 20+ industries.
- Lifecycle modules: Collections management (unify "from pre-delinquency to legal recovery"); context-sensitive agent interface; Advanced financial processing ("sophisticated payment processing, settlement offers, payment plans, and account adjustments that intelligently distributes payments across multiple accounts and charge types"); relationship-driven recovery (relationship mapping across customers, accounts, collateral); configurable-without-code administration; enterprise security (PA-DSS & PCI-DSS).
- Stage solutions: Early intervention (pre-delinquency identification, early-stage comms, payment arrangements); Advanced collections (workflow automation routing "accounts to the right teams… based on risk profiles and treatment strategies", dynamic decisioning, payment allocation, real-time comms with compliance controls); **Recovery operations** ("Maximize recovery on charged off accounts…", segmentation by propensity to pay, settlement management with audit trails); **Legal management** ("Track legal actions from referral through judgment", jurisdiction-specific document generation, **attorney network management** — "Assign and track cases across your legal network"); **Asset management** (repossession coordination, asset condition/location/valuation tracking, remarketing); **Partner ecosystem** — "Vendor oversight: Monitor performance and compliance across collection agencies, law firms, and other partners… Secure third-party access."
- Add-ons: FitPortal ("secure third party access… external partners"), Cara AI self-service chatbot, FitComms, AYDA intelligence hub.
- Deployment: AWS cloud options.

### C&R Agency Management (PlacementsPlus / Agency Network) — Tier 2, boundary evidence

- Creditor-side machinery for the agency channel: "Streamline account placements… ensure every account is placed with the right agency at the right time… maintain total control of the recovery process while your agencies do the work"; Placement Optimizer (mathematical optimization for placement decisions); Agency Network ("a single, secure channel… processes over $120B annually… data is validated and exchanged safely with collection agencies and partners" — volume claim not reproduced); testimonial: "The biggest benefit from Agency Network is secure data exchange… house and remit data securely."
- Confirms: the creditor side treats agency placement, data exchange, agency performance/compliance oversight, and recall as a managed workflow — i.e., the placement relationship is an object on *both* sides of the seam (creditor's placement tool vs agency's client/account model).

### Finvi taxonomy — boundary evidence

- Velosidy (third-party agencies) vs Katabat (first-party banks/lenders) vs Simplicity (small/start-up agencies) vs Artiva HCx (healthcare RCM incl. outsourcers "managing multiple clients and business lines"). One family, both sides of the seam, distinct products — platform-family membership cannot define either Type.

## Cross-product Comparison

| Dimension | Finvi Velosidy | Collect! | Qualco QCR | C&R Debt Manager |
|---|---|---|---|---|
| Primary operator | third-party collection agencies | collection agencies (1st/3rd-party & legal), also internal recovery | banks + debt purchasers/debt servicers, in-house AND 3rd-party operations | creditor enterprises (banks, retailers) + partner/agency oversight |
| Unit of record | consumer account worked by agents | **Debtor account listed by a Client** (field-documented) | case/account per receivable, "cases" | account ("650+ debt types"), relationship mapping |
| Creditor client as object | implied (agencies serve creditors; partner client portals) | **explicit: Client object with hierarchy, invoices, client payments, commission, per-client settings & CBR** | Outsourced Collections: assignment/recall of external activities; third-party access | Partner ecosystem: vendor oversight of agencies/law firms (creditor-side view) |
| Recovery economics | "revenue while lowering cost to collect" (agency revenue model) | **commission rate plans, commission-to-date, net/gross/combined remittances, client invoices** | system of record + balance management; buyer/servicer economics | payment allocation across accounts/charge types, settlements |
| Collector loop | AI queues, next-best-action, work queues | work queues, account toss to operators, contact plans, promises, letters | omnichannel engagement, decision engine, queues | workflow routing by risk/treatment strategy, context-sensitive interface |
| Tracing / data | skip-tracing partners (LexisNexis/Experian/TransUnion), data scrubs | built-in Skip & Score; bureau reporting (Metro 2) | decision engine, data hub | relationship mapping, propensity segmentation |
| Legal | InfoTrack e-filing partner, bankruptcy monitoring | Judgment Records (judgments/liens/assets), legal fees fields | Legal Management module, expense tracking | Legal management: referral through judgment, attorney network |
| Assets/collateral | asset verification partner | asset info alongside accounts | Collateral & Real Properties module | Asset management: repossession, remarketing |
| Debt-buyer pole | (agencies; buyers served in family) | legal/1st-party pole documented | **core clientele includes debt purchasers (Intrum/Cabot/doValue/Hoist)** | recovery ops on charged-off accounts; NPL framing at QCR |
| Consumer surface | partner consumer portals, conversational AI | built-in Consumer Portal (payments, plans, disputes) | Digital Self-Service Portal | Cara AI self-service, payment options |
| Client surface | partner client portals | built-in Client Portal, per-client scoped reporting | third-party access + performance monitoring | FitPortal / Agency Network secure exchange |
| Compliance | "regulatory guardrails into every workflow" | "full compliance automation"; audit trails | "comply with local regulations"; GDPR capability | compliance controls in comms; audit trails on settlements |
| Deployment | SaaS on OCI | hosted or on-premise, PC-era lineage | on-prem/IaaS/cloud, multi-country | AWS cloud |

Stable across the sample (candidate common structure):
1. A per-debtor **account** carries the owed balance and all pursuit work.
2. A **creditor counterparty** (client / original creditor / portfolio) structures the operation; accounts enter via placement/listing (or acquisition), and per-client scoping governs visibility, reporting, and money.
3. **Recorded pursuit**: contacts, notes, letters, promises, plans, payments — logged per account, auditable.
4. **Outcome loop**: paid/settled (→ remit/report), payment plan (→ monitor), legal referral (→ judgment), recall/return to client, uncollectible/close; assets/collateral where secured.
5. **Money loop between operator and creditor**: commissions/fees earned on recovery, remittances and invoices to the client (agency pole) or portfolio ownership economics (buyer pole).
6. Regulated-contact posture with audit trails (structural; regime specifics vary by market).
7. Reporting upward: per-client and portfolio-level liquidation/performance reporting; portals as self-service surfaces (era-current but present in all four).

## Abstraction Levels

### Level 0 — Defining Invariant (smallest stable structure)

Three jointly-held structures; remove any one and the product stops being recognizable as this Type:

1. **The placed/purchased debt account of record** — a persistent, individually identified account per debtor (or debtor-linked group) carrying the creditor-of-record, the owed balance (principal/interest/fees as separable components), and the listing/placement or acquisition lineage. This — not the debtor person record, not the client contract — is the unit on which pursuit accumulates. Remove → generic contact/CRM tool with no debt object.

2. **The creditor client as the standing counterparty of the pursuit business** — the operator pursues debt it did not originate through an ongoing customer relationship: accounts are listed/placed by creditor clients (agency pole) or acquired in portfolios (buyer pole); the client (or portfolio) scopes visibility, reporting, and configuration; and the operation's money loop runs operator↔creditor (commission earned on recovery, remittances, client invoicing — or purchase/servicing economics). This is what makes the operation agency-side rather than first-party. Remove → Collections Platform (first-party).

3. **Recorded recovery pursuit closing in recovery outcomes** — per-account treatment history (contact attempts, tracing, correspondence, promises, plans, payments, legal steps) that is auditable, and account-level outcome states that close the work: paid/settled → remit and report to the client; plan → monitor; legal referral → judgment/asset path; recalled/returned to client; uncollectible → close. Remove → a placement manifest or debt registry with a phone.

Jointly-held is load-bearing:
- 1 alone → debtor CRM / collections-call contact list
- 1+2 without 3 → placement manifest / client register / debt inventory, not a pursuit operation
- 1+3 without 2 → first-party collections (Collections Platform)
- 2+3 without 1 → client-accounting or agency-relationship tool with nothing to pursue

### Level 1 — Common Mature Structure

Very common across mature products; expected in the market; not definitional:
- Work queues with prioritization/assignment (incl. "toss"/distribution of accounts to collectors); collector performance management
- Treatment strategy/cadence configuration (contact plans, decision engines, next-best-action; AI-era scoring: propensity to pay, best time/channel)
- Letters/correspondence machinery with batching and mail-house integration; dialer/SMS/email integration
- Payment capture and allocation across balances and charge types; payment plans/promises as first-class objects
- Consumer self-service (portal/bot: pay, set up plans, dispute) with audit trail
- Client-facing reporting/portals scoped per client; secure data exchange with creditors
- Skip tracing and data services (bureau data, contact enrichment, bankruptcy/scrub services)
- Credit-bureau reporting on behalf of clients (Metro 2 class), with per-client bureau codes
- Legal machinery: judgment/lien/asset records, legal-fee tracking, e-filing, attorney network management
- Collateral/asset recovery (repossession, remarketing) where debts are secured
- Compliance machinery: jurisdiction-aware contact rules, guardrails, dispute handling, audit trails
- Per-client configuration that cascades into account behavior (settings, rates, letter programs)
- Portfolio/client-hierarchy organization and roll-up reporting; liquidation/success-rate analytics

### Level 2 — Variant / Optional Structure

- Operator identity: contingent collection agency; first-party/early-out service bureau (Collect! documents 1st-party features; Finvi/TransUnion use "first-party" vocabulary); debt buyer/owner (Qualco's purchaser clientele); collection law firm (judgment enforcement focus); debt servicer for purchasers
- Debt class: consumer credit (cards, loans, telecom/utility, auto deficiency), commercial/B2B debt, healthcare (RCM agencies), government fines/taxes, judgements
- Compensation form: contingency commission, flat fees, per-placement fees, purchase-discount margin (buyer pole) — the invariant is the operator↔creditor money loop, not a specific fee form
- Regional/regulatory packaging: UK DCA editions, multi-country/multi-currency platforms, GDPR-era data-rights tooling (Europe) — regional machinery, not definitional
- Business-model straddles: platform families spanning first-party and third-party lines; agency networks/exchanges; creditor-side panel-management tools (related surface, different Type side)
- Deployment: on-premise ↔ hosted ↔ cloud-native; multi-tenant vs single-tenant

### Level 3 — Vendor-specific (research notes only)

- Velosidy's named AI features (Best Channel to Collect, Best Time to Call, P2P, Best Payment Arrangement) and Oracle Cloud Infrastructure
- C&R's FitAgent/FitAdmin/FitPortal/Zelas AI/Cara AYDA add-on family; Placement Optimizer; Agency Network
- QCR module names, QCR Accelerator editions, Agenly, ExtraCollect; Arum Approved System certification
- Collect!'s Account Toss, Owned By Client hierarchy mechanics, setzone.ctf timezones, Web Host portals, specific Metro 2 code fields
- All vendor performance/ROI figures on the fetched pages (not reproduced as facts)

## Vendor-specific Findings

- Finvi's own four-line taxonomy (Velosidy/Katabat/Simplicity/Artiva) is vendor-specific packaging, but it *evidences* the first-party/third-party seam as an industry-structural fact (their blog taxonomy literally uses "ARM 1st Party"/"ARM 3rd Party").
- Collect!'s "Owned By Client" master-client hierarchy and per-client bureau code fields are implementation choices; the underlying invariant (per-client scoping) is common.
- QCR's "in-house and 3rd party operations" dual coverage shows one engine serving both — supporting the object-model anchor over platform-family anchor (the prior flag's instruction).

## Rejected Findings (considered, rejected from the core)

- **"Third-party only"** — rejected: sampled products document first-party use (Collect! "Features for 1st Party Users", QCR "in-house" operations, service-bureau early-out work); the invariant is the operator-not-original-creditor posture plus client scoping, not a ban on first-party deployments. What is rejected is building the Type on platform-family membership.
- **Skip tracing as definitional** — rejected: paper-era agencies traced via references/directories; several debt classes (recent placements, legal judgments) need little tracing. L1.
- **Contingency commission as the specific definitional form** — rejected: flat-fee, per-placement, and purchase-margin models exist; the invariant is the recovery-based money loop to the creditor, not the fee formula.
- **Credit-bureau reporting** — rejected: strong Collect! evidence and common in the US consumer segment, but regional (not a universal feature of the Type; paper-era and commercial/B2B collections lack it). L1/L2.
- **Compliance machinery as definitional** — rejected: regime-specific and era-specific; every operational collections Type holds it as standard capability, not invariant (consistent with the two processed sibling passes).
- **Placement-file/EDI formats** — rejected as vendor/industry interface detail.
- **AI scoring/queues** — rejected: era-current L1; Collect! (since 1988) and paper-era practice satisfy the core without them.

## Boundary Findings

| Type | Evidence-anchored distinction | Remove/keep test |
|---|---|---|
| Collections Platform (processed) | There: creditor pursues delinquent obligations **on its own book**, own customers, relationship preserved, cure-preferred; agency placement is an exit ramp. Here: operator pursues debt **for others** (placed) or **owned but not originated** (bought); the creditor client is a first-class counterparty with its own money loop (commission/remittance/invoicing). Both sides confirm the seam from their side: collections-platform doc says "agency placement and panel oversight are exit ramps managed from this side"; Finvi sells Katabat (first-party) and Velosidy (agencies) as separate products | Remove the creditor-client counterparty and recovery-economics loop → Collections Platform. Keep them → this Type |
| Collections Automation Platform (processed) | There: open trade invoices, due-date aging, ERP-fed B2B dunning, promise/dispute closing on the receivable. Here: delinquent repayment obligations/placed debt, missed-payment/charge-off lineage, creditor clients, agency economics | Object class + counterparty seam |
| Accounts Receivable Management (processed) | AR pursues one's own customers on one's own open invoices inside the live relationship; here the operator is not the creditor of record | Same as above, sharper |
| Loan Management System (processed) | LMS services the performing book and tracks delinquency, then hands off; this Type runs the pursuit business after handoff (agency/buyer receives what servicing sheds) | Lifecycle seam, confirmed from this side |
| Credit Management Platform (processed) | pre-default risk vs post-default recovery | stage seam |
| Debt Management Application (unprocessed sibling) | Expected consumer-side: the individual managing/repaying their own debts (payoff planners, DMP tools). Opposite side of the table. **Flag for its own pass**; not asserted further | person-as-debtor vs person-as-creditor-side-actor |
| CRM | An agency's *client-acquisition* CRM manages prospects for new placements; this Type's object is the debt account and the recovery loop, not the sales pipeline | object + loop |
| Contact Center / Dialer | Dialers execute contact campaigns; they hold no account balances, commissions, or outcome states | tooling seam |
| Law Practice Management (§11) | Collection law firms may run both; LPMS manages legal matters generally, this Type manages debt-recovery operations with judgments as one outcome | general matters vs debt-recovery loop |
| Government Revenue Management (processed) | government pursues its own statutory receivables with public-funds accountability; agencies pursuing government debt as contracted third parties sit on this side | who owes whom + accountability frame |

The creditor-side panel-management tools (C&R PlacementsPlus/Agency Network, Qualco ExtraCollect) are the mirror image of this Type's client structure; they belong to the creditor's collections stack, not this Type.

## Historical / Market-Sample Check

- **Paper-era agency practice**: creditor sends a placement letter/manifest of delinquent accounts; agency opens a ledger card per debtor; collectors write every contact, promise, and payment on the card; commission computed on collections; monthly statement and remittance check to the client; accounts returned unpaid. All three Level-0 structures present with zero software. ✓
- **PC-era package (Collect!, since 1988)**: same model, documented at field level; no AI, no cloud, no portals in early versions — core intact. ✓
- **Regional variety**: UK DCA packaging (QCR Accelerator UK), European multi-country debt servicing (QCR + Intrum/Cabot/doValue class), North American ARM ecosystem (Finvi, Collect!) — same core across regions. ✓
- **Legal-native collections** (judgment enforcement offices): judgment records + asset tracking + client structure — fits with legal as the pursuit channel. ✓
- **Debt buyers**: own the debt outright; the "client" leg abstracts to portfolio/counterparty economics (acquisition, servicing, remittance-like flows to co-owners/creditors where applicable). The core holds as long as leg 2 is phrased as "operator pursues debt it did not originate through an ongoing customer relationship, with the creditor counterparty/portfolio as first-class object". ✓
- Conclusion: no era/region/platform lock-in in the core. AI scoring, portals, dialers, bureau reporting, cloud are era-current additions.

## Uncertainties

1. **Remittance mechanics depth**: net/gross/combined remittances are documented only at Collect!'s help-title level (title fetched, not the full page); exact flows (who holds trust funds, timing, statement cadence) are industry practice but not evidenced here in detail. Final document states the money loop structurally, without timing/precision claims.
2. **Debt-buyer pole detail**: purchaser-specific objects (portfolio purchase, chain of title, co-servicing) are inferred from Qualco's clientele and NPL positioning, not from purchaser-product documentation. Held as variant-level, with the client leg abstracted to "creditor counterparty / portfolio". If a future pass samples a buyer-native product (e.g., a debt-servicing platform), the abstraction should be re-tested.
3. **First-party service-bureau overlap**: early-out agencies run first-party work on placed accounts; the boundary is the client-scoped placement relationship, but product packaging blurs it (Collect! sells to both). Recorded; keep-both with Collections Platform stands because the object/counterparty models differ.
4. **Regulatory specifics**: no specific statute/regime details asserted; all compliance claims are structural.
5. **Velosidy/QCR/Debt Manager internals**: evidence is product-page capability level; no help-center depth was reachable for them. Interface descriptions in the final document are stated conceptually.
6. **Debt Management Application**: unprocessed; expected consumer-side but unverified — left to its own pass.

## Final Synthesis

Debt Collection Management is the professional recovery operation's system of record: an operator (agency, debt buyer/servicer, collection law firm) pursues debt it did not originate through an ongoing customer relationship — placed by creditor clients or acquired in portfolios — on a per-account record that accumulates an auditable treatment history and closes in recovery outcomes (paid/settled → remit and report to the creditor; plan → monitor; legal/judgment; recalled/returned; uncollectible), with the operation's economics running between operator and creditor client (commission on recovery, remittances, invoicing — or portfolio ownership economics in the buyer pole).

The defining core is three jointly-held structures (placed/purchased debt account of record; creditor client as standing counterparty with client-scoped money/reporting; recorded pursuit closing in outcomes). Everything else — queues, AI scoring, tracing services, portals, bureau reporting, compliance guardrails, legal/asset modules — is common mature structure, and the first-party/third-party seam is anchored in the object model (who is the creditor of record, where does the money flow), not in platform-family membership. This confirms and discharges the collections-platform pass's flag from this side; joint review is available but the two passes now agree on the seam independently.
