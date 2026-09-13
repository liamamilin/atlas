# Research Notes — Collections Platform

## Research Goal

Identify the smallest stable invariant that defines the **Collections Platform** Type, and place every other observed feature at the correct abstraction level.

Following `WORKFLOW_v1.1.md §22` and `WRITING_GUIDE_v1.1.md §28`, this document separates:

```text
L0 Defining Invariant
L1 Common Mature Structure
L2 Variant / Optional
L3 Vendor-specific
```

Evidence layers per `WORKFLOW_v1.1.md §23`:

```text
A Direct Product Observation (official source, specific product)
B Cross-product Commonality
C Canonical Inference
```

A pre-existing joint-review flag must be addressed from this side. The `collections-automation-platform` pass (2026-09-07, STATUS.md Boundary Issues) flagged that the directory carries "Collections Automation Platform" AND "Collections Platform" as separate §08 leaves while market usage of "collections platform" overlaps both grounds, and hypothesized a clean resolution: if Collections Platform is the financial-institution / lender delinquency collections space, the two are genuinely different Types. This pass tests that hypothesis against the real market.

## Initial Boundary

Target:

> Collections Platform (§08 Finance, Banking, Insurance & Investment; sits between "Debt Collection Management" and "Debt Management Application" in the directory)

Nearest confusing Types:

- Collections Automation Platform (closest name-collision sibling, documented 2026-09-07 — B2B accounts-receivable collections automation)
- Debt Collection Management (agency-side pursuit of charged-off / purchased / placed debt — sibling leaf, unprocessed)
- Loan Management System / Mortgage Servicing Platform (servicing suites that carry collections as a module)
- Debt Management Application (leaf after this one; suspected consumer-side)
- Credit Management Platform (upstream: underwriting/limits; feeds collections risk data)
- Customer Communication Management / Outreach Sequencing Platform (structural rhymes: templated multi-channel outreach over a population)
- Billing Platform (upstream charge creation for service/postpaid arrears)

Working hypothesis:

> A Collections Platform is the creditor-side collections-and-recovery system for delinquent obligations on the organization's own credit accounts: it maintains the delinquent-account population drawn from the organization's book/servicing systems, turns it into strategy-driven collection treatment (automated outreach plus collector work queues), records treatments and outcomes on the account, and carries each account through cure, restructure, settlement, charge-off and recovery.

The hypothesis deliberately keeps "automation", "strategy engines", payment capture, and compliance machinery OUT of the defining core, and treats the first-party/own-book anchor as the seam against agency-side software — both to be tested.

## Research Questions

- What is the object being collected, and how is "delinquent" measured (invoice aging vs missed payments / days past due on repayment obligations)?
- Where does the delinquent population come from (ERP/accounting books vs loan servicing/core systems), and how is the picture kept true?
- What is the standard object model of the collection operation (delinquent account, delinquency stage, treatment, arrangement, promise, settlement, charge-off, recovery)?
- How do automated outreach, treatment strategies, and human collectors divide the work across delinquency stages?
- What happens at the end of the road: cure, restructure, settlement, charge-off, recovery, agency placement, legal, repossession — which are in-type and which are exit ramps?
- How strong is the compliance/regulated-contact layer in this Type compared with B2B AR collections?
- What exactly separates this Type from Collections Automation Platform (B2B AR) and from Debt Collection Management (agency side)?
- Would pre-software collections departments, card-issuer collections of earlier eras, and servicing-suite collections modules still fit the definition? (historical check)

## Representative Products

| Product | Why selected |
|---|---|
| C&R Software Debt Manager | enterprise full-lifecycle collections & recovery platform for creditors (banks, lenders, retailers, telcos, healthcare); canonical "collections and recovery" name; multi-industry creditor pole |
| Qualco Collections & Recoveries (QCR) | European enterprise pole; end-to-end debt collections lifecycle platform; product family spans early-stage accelerator, digital agentic resolution, outsourced-panel management, self-service portal; client base includes banks and debt purchasers |
| Finvi Katabat | first-party lender pole (banks and fintech lenders); digital-first omnichannel strategy engine; explicit "first-party lenders" positioning; same vendor also sells the third-party agency platform (Velosidy), making the first-party/third-party seam vendor-visible |
| LoanPro (collections within a loan servicing suite) | Tier-1 documentation pole; collections as a dedicated layer inside a loan servicing platform — the minimal platform-native form of the Type |
| Finvi Velosidy | NOT a representative of this Type — fetched as boundary contrast: the same vendor's third-party collection agency platform, exhibiting the agency-side object model (client accounts, skip tracing, dialers, propensity-to-pay on placed debt) |

Planned samples Experian Tallyman and Pega Collections could not be reached (see Sources); the sample was adjusted within the same philosophy spread: enterprise full-lifecycle ×2, regional/enterprise family, first-party digital SaaS, servicing-suite module.

## Sources

Research date: **2026-09-07**

Directly fetched official pages (all fetched 2026-09-07):

- C&R Software — Debt Manager product page — https://www.crsoftware.com/products/debt-manager (Tier 2; includes solution-stage breakdown, add-on roster, compliance claims)
- Qualco Technology — product site (resolved via qualco.eu redirect) — https://www.qualco.tech/ (Tier 2; Collections & Recoveries family taxonomy: QCR, Agenly, QCR Accelerator, ExtraCollect, Omnichannel Collections, Digital Self-Service Portal; Credit & Lending siblings)
- Finvi — Katabat product page (banks-and-lenders) — https://katabat.com/ (resolves to https://finvi.com/banks-and-lenders/) (Tier 2)
- Finvi — Velosidy product page (collections agencies) — https://finvi.com/velosidy/ (Tier 2; boundary-contrast evidence)
- LoanPro Knowledge Base — https://help.loanpro.io/ (Tier 1)
- LoanPro — Servicing and collections overview — https://help.loanpro.io/servicing-and-collections/servicing-and-collections-overview (Tier 1)
- LoanPro — Delinquency categories — https://help.loanpro.io/delinquency-and-defaults/delinquency-categories (Tier 1)

Prior pass used for boundary alignment:

- applications/collections-automation-platform.md + research notes (processed 2026-09-07), which flagged this leaf for joint review

Source-access limitation: Experian Tallyman returned 403 (experian.com) and a timeout (experian.co.uk); Pega Collections returned 403 twice; docs.loanpro.io transport-errored (help.loanpro.io was used instead). Tallyman and Pega are therefore NOT sampled and no detail about them is asserted from memory. Evidence for Debt Manager, Qualco, and Katabat comes from vendor product pages (capability level, not interface-mechanic level); Tier-1 operational mechanics exist only for LoanPro. Accordingly, interface mechanics in the final document are stated in conceptual terms, and vendor-marketed figures ($8T+ managed, 650+ debt types, 40% agent-performance uplift, 125% connection-rate uplift, "14 days to 5 minutes" hardship approval, delinquency reductions in basis points) are recorded here as marketing claims only and are not asserted as facts anywhere.

## Product Observations

### C&R Software Debt Manager (Layer A — Tier-2 product page)

- Positioning: "Take control of collections and recovery"; "a comprehensive debt collections solution managing the entire risk lifecycle"; claims heritage as a debt-management collection system serving banking and other creditor industries.
- Scope claim: "Unify the entire collections lifecycle from pre-delinquency to legal recovery in a single solution... across 650+ different types of debt" (numeric claim noted, structure is the evidence).
- Lifecycle stages marketed as solutions:
  - **Early intervention**: pre-delinquency identification (analytics to identify at-risk accounts before they enter collections); early-stage collections (targeted, timely communications through customers' preferred channels); payment arrangements (flexible, sustainable payment plans tailored to each customer's situation); context-sensitive agent interface.
  - **Advanced collections**: intelligent workflow automation (route accounts to the right teams at the right time based on risk profiles and treatment strategies); dynamic decisioning (automatically adjust collection strategies based on customer behavior and payment patterns); advanced financial processing (payment allocation across multiple accounts and charge types); real-time communication with compliance controls and complete interaction history.
  - **Recovery operations** (charged-off accounts): advanced segmentation prioritizing accounts by propensity to pay and recovery potential; settlement management with audit trails; "relationship driven recovery" — relationship mapping connecting accounts, customers, and collateral.
  - **Legal management**: case management tracking legal actions from referral through judgment; jurisdiction-specific legal document generation; attorney network management.
  - **Asset management** (collateral): repossession management with integrated workflows; asset tracking (condition, location, valuation); remarketing tools.
  - **Partner ecosystem**: vendor oversight across collection agencies, law firms, and other partners; secure third-party access portal.
- Financial processing: payment processing with intelligent allocation across accounts and charge types; settlement offers; payment schedules/plans; account adjustments.
- Agent experience: "FitAgent" context-sensitive interface — automatically surfaces information based on account status, customer situation, and organizational/regulatory context; "FitAdmin" no-code configuration of workflows, interfaces, decision logic by administrators.
- Compliance/security: role-based access controls, detailed audit trails, PCI/PA-DSS-certified posture, "highly regulated environments" framing; compliance-aware communication.
- Add-ons: AI assistant layer (Zelas AI), AI chatbot for 24/7 customer self-service collections (Cara AI), omnichannel communications (FitComms), financial-hardship resource connection (SpringFour), third-party portal (FitPortal), real-time analytics hub (AYDA), integration services.
- Industries claim: banking, healthcare, telecommunications, retail and more (20+ industries) — evidence that creditor collections extends beyond financial institutions to postpaid/service arrears.

### Qualco Collections & Recoveries (Layer A — Tier-2 product site)

- Positioning: technology for "credit, collections, and lending teams"; Collections & Recoveries is a named product family inside a credit-lifecycle ecosystem (Loan Originator, Loan Manager siblings; Data/ML/Agentic studios).
- Core platform: **Qualco Collections & Recoveries (QCR)** — "an end-to-end platform for managing the entire debt collections lifecycle."
- Family members (each a distinct packaging/depth option):
  - **Agenly** — cloud-native SaaS, agentic AI: "helps collection teams engage customers, guide repayment, and capture secure payments across SMS, Viber, WhatsApp, and more" — "Turn Conversations Into Payments"; marketed for early arrears resolution at banks.
  - **QCR Accelerator** — "a pre-configured solution for early-stage collections designed for small to mid-sized lenders" (segment-tier packaging made explicit).
  - **Qualco ExtraCollect** — "cloud-based SaaS platform that streamlines outsourced debt collection panel management" — the creditor's management of agencies it places accounts with.
  - **Omnichannel Collections** — module "enabling customer outreach through their preferred communication channels."
  - **Digital Self-Service Portal** — "fully configurable self-service collections portal delivering flexible customer journeys."
- Independent certification: QCR renews an "Arum Approved System" certification (Arum is a collections-sector consultancy) — the existence of an independent collections-systems certification scheme is itself market-structure evidence.
- Client roster: banks and debt purchasers/servicers (Intrum, Hoist Finance, Cabot, doValue, Emirates NBD and others shown as logos) — evidence that the same collections platform family is sold across the creditor/debt-purchaser divide.
- Blog framing: "early arrears" as a recognized operational domain (e.g., early-arrears resolution in UK motor finance; agentic AI for early-arrears routing at banks).

### Finvi Katabat (Layer A — Tier-2 product page)

- Positioning: "Collections and recovery software that helps **first-party** lenders like banks and Fintech companies improve efficiency, leverage more effective strategies and increase customer satisfaction." Also: "the trusted, cloud-based platform that helps banks and lenders deliver secure, personalized, omnichannel debt management, maximizing recovery while improving the customer journey."
- Omnichannel orchestration: "contacting customers through their preferred channel... flexible and configurable communication across email, SMS, voice, print, and more."
- Strategy engine: "combines powerful decision-tree and workflow capabilities in one unified platform, allowing you to design personalized interactive customer experiences" — treatment-strategy authoring is the flagship capability.
- Compliance engine: "fully auditable built-in compliance engine lets you customize rules for every jurisdiction"; PCI DSS, SOC 2, GDPR posture.
- Embedded payments: Finvi Payments embedded directly into the platform (US only) — payment rails as suite capability.
- Client evidence (case studies): a top-20 mortgage lender (compliance in mortgage servicing and default); humm-group consumer finance (hardship application workflow; vendor claims approval time reduced from 14 days to 5 minutes); Capital Services (cardholder outreach, settlement offers, reduced charge-offs); HSBC shown as client logo.
- Family contrast (same vendor's product taxonomy): Velosidy for third-party collection agencies; Simplicity for small agencies; Artiva HCx for healthcare revenue-cycle — Katabat is the vendor's first-party financial-instrument pole.

### LoanPro — collections inside a loan servicing suite (Layer A — Tier-1 documentation)

- The servicing platform has a named **Servicing and collections** domain; "dedicated collections tools also help manage delinquencies and defaults. Your team can track late payments, set up payment plans, and enroll borrowers in hardship programs."
- **Delinquency categories** (formerly "Delinquency Buckets") — Tier-1 mechanics: a loan-level report of how many payments a loan is past due; one category per missed payment (Category 1 = most recent missed payment, Category 2 = next, and so on), each with date, remaining amount due, and days past due; logged payments apply toward the first delinquency category; category variables are usable as conditions in the automation engine to trigger processes.
- **Collections strategies**: hardship and repayment programs as first-class enrollment objects; charge-offs documented under "Delinquency and defaults".
- **Collateral management and tracking**: visibility into secured assets, monitoring collateral value and status through the account lifecycle.
- **Agent surfaces**: account queues "serve them the accounts needing attention"; step-by-step agent walkthroughs for complex processes; payments, adjustments, document management in one place; smart checklists for multi-step processes such as bankruptcy or hardship enrollment.
- **Customer self-service**: customer portal where borrowers view account details and make payments (self-service cure).
- **Communications**: personalized communication based on account status, payment history, and preferences, with an explicit compliance frame (TILA, Reg Z, TCPA named); automated reminders; interactive SMS.
- **Portfolio/back-office**: reporting suite, custom reporting, database access; bankruptcy monitoring via integrated partner (BankruptcyWatch); payoff/close/archive lifecycle ends the account.
- Structural takeaway: a servicing suite can satisfy the minimal form of this Type with queues + delinquency tracking + arrangements/hardship + self-service — no standalone treatment-strategy engine required.

### Finvi Velosidy — boundary contrast, third-party agency platform (Layer A — Tier-2 product page)

- Self-description: "a modern SaaS-based collections platform that allows third-party collection agencies to increase revenue while lowering the cost to collect and minimize operational risk" — note that "collections platform" as a market label is used by the agency side too.
- Object model revealed by its capabilities: **debtor/consumer accounts held for placement** — AI work queues and agent queuing over placed accounts; "Best Channel to Collect", "Best Time to Call", "Propensity to Pay", "Best Payment Arrangement" scoring per consumer; dialer-adjacent operations (connection rates).
- Agency-signature machinery: skip tracing partners (LexisNexis, TransUnion, Experian, IDI); bankruptcy monitoring (BankruptcyWatch); compliance scrubs and FDCPA/TCPA lawsuit-threat monitoring (WebRecon); e-filing (InfoTrack); print/mail partners; client/collaboration portals for creditor clients; debt-buyer/agency partner ecosystem.
- The consumer is "each consumer", the client is "your agency" — the operator is not the creditor. This is the population Debt Collection Management's leaf will describe; recorded here only as boundary evidence.

## Cross-product Comparison

| Finding | Debt Manager | Qualco QCR | Katabat | LoanPro (servicing module) | Level |
|---|---|---|---|---|---|
| delinquent-account population on repayment obligations, tracked by missed payments / days past due | yes ("pre-delinquency to legal recovery", account-status-driven) | yes ("entire debt collections lifecycle"; early-arrears framing) | yes (delinquency reduction as client outcome) | yes (Tier 1: delinquency categories per missed payment with days past due) | L0 |
| recorded collection treatment on the account (outreach, agent actions, notes, interaction history) | yes (real-time communication, complete interaction history, audit trails) | yes (engage customers, guide repayment; omnichannel module) | yes (omnichannel orchestration, configurable communication) | yes (Tier 1: communications, agent walkthroughs, notes/checklists) | L0 |
| outcome loop on the obligation (cure / arrangement / settlement / charge-off-and-recovery as tracked states) | yes (payment arrangements, settlement management, recovery operations, charge-off segmentation) | yes (guide repayment, capture payments; full lifecycle) | yes (settlement offers, reduced charge-offs as outcome) | yes (Tier 1: payment plans, hardship programs, charge-offs, payoff/close) | L0 |
| collector work queue with prioritization/assignment | yes (route accounts to right teams by risk profile and treatment strategy) | yes (collection teams; QCR operational platform) | yes (strategy engine drives queue/experience) | yes (Tier 1: account queues serving accounts needing attention) | L1 |
| treatment-strategy authoring (decision trees / configurable strategies per stage & risk) | yes (treatment strategies, dynamic decisioning) | yes (configurable journeys; agentic routing) | yes (flagship "strategy engine", decision trees) | partial (automation engine rules + checklists instead of a strategy console) | L1 |
| early-stage automated outreach across channels | yes (preferred channels) | yes (Omnichannel Collections; Agenly SMS/Viber/WhatsApp) | yes (email, SMS, voice, print) | yes (automated reminders, interactive SMS, letters) | L1 |
| payment arrangements / plans as first-class objects | yes (payment arrangements, schedules) | yes (guide repayment; flexible journeys) | yes (payment plans; settlement offers) | yes (Tier 1: payment plans; hardship/repayment programs) | L1 |
| hardship / forbearance routing | yes (SpringFour add-on for hardship resources) | implied (restructuring content) | yes (humm hardship case study) | yes (Tier 1: hardship programs, enrollment checklists) | L1 |
| settlement management | yes (settlement offers with audit trails) | yes (restructuring/settlement journeys) | yes (settlement offers) | not evidenced at fetched depth | L1 |
| self-service customer portal (pay, view, arrange) | yes (Cara AI chatbot self-service collections) | yes (Digital Self-Service Portal) | yes (personalized customer journey) | yes (Tier 1: customer portal) | L1 |
| charge-off → recovery continuation (segmentation by propensity/recovery) | yes (Recovery operations stage) | yes (Recoveries in family name; client roster incl. debt purchasers) | yes ("maximizing recovery", charge-off case study) | charge-offs tracked; recovery depth not evidenced | L1 |
| collateral / asset recovery machinery (repossession, remarketing, valuation) | yes (Asset management stage) | not evidenced at fetched depth | not evidenced | collateral tracking present (Tier 1); repossession not evidenced | L2 |
| legal management (case tracking referral→judgment, attorney network, legal documents) | yes (Legal management stage) | not evidenced at fetched depth | not evidenced | bankruptcy monitoring via partner | L2 |
| outsourced agency panel management / placement oversight | yes (vendor oversight of agencies, law firms; partner portal) | yes (ExtraCollect dedicated product) | not evidenced | not evidenced | L2 |
| embedded payment capture / rails | yes (payment processing, allocation) | yes (Agenly captures secure payments) | yes (Finvi Payments embedded, US only) | yes (payments processing in servicing) | L1 |
| regulated-contact compliance machinery (jurisdiction rules, auditability) | yes (compliance controls, audit trails, certified posture) | yes (compliance emphasized) | yes (built-in compliance engine, rules per jurisdiction) | yes (Tier 1: TILA/Reg Z/TCPA frame) | L1 |
| AI: propensity/behavior scoring, agentic self-service | yes (Zelas AI, Cara AI, pre-delinquency identification) | yes (Agenly agentic AI; ML studios) | not prominent on page (strategy-led) | automation rules + partner bankruptcy monitoring | L1/L2 |
| multi-industry creditor use beyond financial institutions (telco/retail/utility arrears) | yes (20+ industries claim) | creditors + debt purchasers in roster | banks/lenders focus | lending focus | L2 |
| pre-delinquency / early-intervention (at-risk accounts before delinquency) | yes (Early intervention stage) | yes (early-arrears framing; early-stage Accelerator) | delinquency reduction framing | not evidenced | L2 |

Evidence-layer note: "yes" entries for LoanPro are Layer A against Tier-1 documentation; entries for the other three products are Layer A against Tier-2 product pages (adequate for capability existence, weaker for interface mechanics). No row rests on a single product except the L2 rows explicitly marked by "not evidenced" elsewhere; those are recorded at L2 precisely because the sample does not establish cross-product commonality.

## L0 — Defining Invariant

```text
Delinquent repayment obligations on the operator's own book as the
managed population
  (customer accounts carrying repayment obligations — credit products or
   postpaid service balances — drawn from the organization's own
   book/servicing systems, tracked through delinquency staging: missed
   payments / days past due)
└── Recorded collection treatment
    (follow-up executed by automated outreach and/or collectors —
     messages, calls, notes, arrangements, promises — logged against the
     account, with next actions scheduled)
    └── Outcome loop closing on the obligation
        (cures through payment, restructured schedules, settlements
         recorded; charge-off and recovery carried as tracked states that
         keep generating work)
```

Three properties. Remove-tests:

- Remove delinquency staging (accounts not tracked as past due on repayment obligations) → the product becomes generic servicing or CRM/contact-center software; the delinquency state is what defines the entire work population. Note this is also the seam against the B2B-AR sibling, whose staged object is the invoice, not the repayment obligation.
- Remove recorded treatment → the product is a delinquency report: it knows who is past due but does nothing about it. (Not collections.)
- Remove the outcome loop → outreach with no money-state tracking; the pursuit never resolves into cures, settlements, or charge-offs. (Not a collections platform — the purpose of the Type is that the delinquency is resolved or carried forward as a tracked, worked state.)

Deliberately NOT in L0 (each fails the remove-test or the historical check):

- **Treatment-strategy engines / decision trees.** Flagship capability of mature products (3 of 4 sampled), but the LoanPro module pole runs collections with automation rules + queues + hardship programs and no strategy console; paper-era and earlier-era collections ran on judgment. L1.
- **Omnichannel outreach specifics** (SMS/WhatsApp/voice/print mix). Channel mix varies by era and region. L1.
- **Payment capture/rails.** Widespread (4/4 in some form) but payment can arrive through existing channels; collections exists without operating rails. L1.
- **Regulated-contact compliance machinery.** Characteristic and heavy in this Type, but pre-regulation collections still was collections, and the *concept* of recorded treatment covers the audit need. L1 (with a strong note — see Important Rules in the final document).
- **Charge-off/recovery/legal/asset machinery.** Standard in full-lifecycle enterprise products (Debt Manager markets all three stages; Qualco's family name includes Recoveries), but lighter forms (servicing-suite modules) satisfy L0 while carrying charge-offs as tracked states only. The *tracking* of charge-off/recovery as outcome states is L0; the *machinery* (legal case management, repossession, remarketing, agency panel management) is L1/L2.
- **Pre-delinquency/early intervention.** L2 — an extension before the population is even delinquent.
- **AI scoring and agentic self-service.** L1/L2, era-current.

## L1 — Common Mature Structure

Capabilities present across the researched sample that make the Type operational at real-world volume:

```text
Collector work queue — accounts needing attention served to collectors,
  prioritized by delinquency stage, balance, risk, or propensity signals,
  with per-collector assignment
Treatment-strategy authoring — configurable treatment paths / decision
  trees per delinquency stage, segment, and risk profile; strategies
  determine which accounts get which treatments when
Early-stage automated outreach — multi-channel contact sequences
  triggered by delinquency state, escalating with stage
Payment arrangements — first-class objects: negotiated schedules that
  restate the obligation and redirect further treatment
Hardship / forbearance routing — enrollment of customers in temporary or
  restructured programs instead of hard pursuit
Settlement management — negotiated closure for less than the full
  balance, recorded with audit trail
Customer self-service — portal or conversational surface where the
  delinquent customer views the obligation, pays, and arranges payment
Regulated-contact compliance machinery — jurisdiction-aware contact
  rules, auditable treatment history, role-based access
Payment capture / allocation — money taken in and applied to the
  obligation (allocation across accounts/charge types at enterprise depth)
Analytics — delinquency/roll/cure/recovery measures, collector
  performance, strategy outcome comparison
Delinquency data feed — accounts and payment behavior flowing in from
  the book/servicing system (or native to it in the servicing-suite form)
```

The characteristic division of labor mirrors the AR sibling but stages it: automation dominates early-stage volume; human collectors dominate mid/late-stage negotiation; recovery operations handle the charged-off tail.

## L2 — Variant / Optional Structure

```text
Packaging
- standalone enterprise platform (full lifecycle, multi-industry)
- European/NPL-market platform family (creditors + debt purchasers)
- digital-first SaaS for first-party lenders
- collections as a module inside a loan servicing suite
- pre-configured early-stage editions for smaller lenders
- agentic digital resolution products as a layer beside the platform

Stage emphasis
- early-stage digital self-service emphasis
- full lifecycle through recovery, legal, and asset/repossession

Industry population
- banking / cards / consumer & installment lending (the §08 heartland)
- telco / utility / retail postpaid arrears (credit-operation framing)
- healthcare revenue-cycle sits adjacent with its own tooling

Operator
- in-house creditor collections and recovery departments
- shared-service centers; strategy teams
- debt purchasers/servicers running the same platform class (adjacent use)

Data & decisioning posture
- strategy consoles vs automation-rule engines
- embedded ML scoring (propensity to pay, best channel/time) vs external
  bureau/risk data feeds vs neither

Regional/regulatory overlays
- jurisdiction-specific contact and collection rules; regional product
  certifications; localization

Extensions
- pre-delinquency early intervention; bankruptcy monitoring; agency panel
  management; debt sale support
```

## L3 — Vendor-specific Structure (research notes only)

- C&R Software: FitAgent context-sensitive agent interface; FitAdmin no-code configuration; Zelas AI / Cara AI / FitComms / FitPortal / AYDA / SpringFour / Callout Services add-on roster; "650+ types of debt" and "$8T+ managed" claims; AWS cloud packaging.
- Qualco: QCR family naming; Agenly agentic-AI product and "Turn Conversations Into Payments" framing; QCR Accelerator early-stage edition; ExtraCollect panel management; Omnichannel Collections / Digital Self-Service Portal module split; Data/ML/Agentic studio layering; Arum Approved System certification; client logos (Intrum, Hoist, Cabot, doValue, Emirates NBD).
- Finvi: Katabat "strategy engine" branding; built-in compliance engine with per-jurisdiction rules; embedded Finvi Payments (US only); family split Katabat (first-party) vs Velosidy/Simplicity (agencies) vs Artiva HCx (healthcare); Best-Time-to-Call / Propensity-to-Pay / Best-Payment-Arrangement AI scoring on Velosidy; humm "14 days to 5 minutes" and basis-point claims; ROI calculator marketing.
- LoanPro: "Delinquency categories (formerly Delinquency Buckets)" per-missed-payment numbering with days-past-due per category; payments applying to Category 1; category variables as automation-engine conditions; smart checklists for bankruptcy/hardship enrollment; BankruptcyWatch partnership; TILA/Reg Z/TCPA compliance framing.

Vendor-marketed numeric claims are not asserted as facts in the Application Document.

## Boundary Findings

### vs Collections Automation Platform (B2B AR) — the flagged collision

The collision flag RESOLVES: the two leaves have distinct canonical cores, confirmed by market structure.

Shared abstract shape (honest family resemblance): both maintain a population of money-owed, run recorded pursuit over it, and close on money-state outcomes. But the object class and everything downstream differ:

```text
                                Collections Automation Platform     Collections Platform
                                    (B2B AR, this pass's sibling)    (this pass)
object of pursuit                   open invoices (trade debt)       repayment obligations on
                                                                     credit accounts (delinquency)
how "past due" is staged            invoice due-date aging           missed payments / days past due
                                                                     on the account (roll between
                                                                     stages; charge-off)
population source                   ERP / accounting books           loan servicing / core book
population class                    B2B trade customers              consumer & commercial credit
                                                                     customers (and postpaid arrears)
treatment machinery                 dunning cadences, disputes,      arrangements, hardship/
                                    deductions, promises             forbearance, restructuring,
                                                                     settlements
terminal horizon                    payment / write-off / agency     cure / restructure / settlement /
                                    referral                         charge-off → recovery, placement,
                                                                     legal, asset
compliance posture                  commercial-relationship oriented regulated-contact regime
```

Vendor behavior confirms the split: the AR sample (Upflow, Chaser, Gaviti, Quadient AR, HighRadius) and this sample (Debt Manager, QCR, Katabat, LoanPro) do not overlap at all — no product appears in both lists, and the two populations use different vocabularies on their own pages (dunning/DSO/credit-to-cash vs delinquency/recovery/settlement/charge-off). Recommendation for joint review: keep both leaves as distinct Types with this boundary; the market-label collision is real but resolvable by object class.

### vs Debt Collection Management (agency side; sibling leaf, unprocessed)

The seam is the ownership relationship, made vendor-visible by Finvi's own taxonomy: Katabat "helps first-party lenders" — the operator pursues obligations on its own book, preserving the customer relationship (cure and hardship preferred where viable); Velosidy "allows third-party collection agencies" — the operator pursues placed consumers for creditor clients, with agency-signature machinery (skip tracing, contingency operations, client portals, dialer economics). In-house recovery of charged-off accounts remains first-party work (Debt Manager's Recovery operations; Qualco's family name); the exit ramps are agency placement (panel management: Debt Manager partner oversight, Qualco ExtraCollect) and debt sale. Debt Collection Management's leaf, when processed, should define the agency-native object model; joint review recommended because platform families straddle the line (Qualco's client roster includes debt purchasers).

### vs Loan Management System / Mortgage Servicing Platform

Servicing owns the account's financial state (schedules, accruals, transactions, payoff). Collections is the delinquency-treatment operation layered on that state. LoanPro demonstrates the module form satisfying this Type's L0 inside servicing; a standalone Collections Platform adds the treatment-strategy console, omnichannel engagement, work distribution at scale, recovery/legal machinery, and compliance tooling. Remove-tests: remove delinquency treatment → servicing remains; remove servicing (accruals/schedules/posting) → collections remains (it feeds from the book).

### vs Debt Management Application (sibling leaf, unprocessed)

Expected to be the opposite side of the table (the consumer/individual managing their own obligations — e.g., debt management plans, payoff planning). Recorded as a note for that pass; this pass makes no claims about it beyond the direction.

### vs Credit Management Platform

Upstream. Credit management decides who gets credit and how much; its outputs (risk, scores, limits) feed collections prioritization. Collections begins when a scheduled payment is missed.

### vs Billing Platform

Upstream for service/postpaid arrears: billing computes and issues what is owed each period; collections begins when the owed amount goes unpaid into delinquency. (For credit products, the analog upstream is the loan servicing schedule.)

### vs Customer Communication Management / Outreach Sequencing Platform

The same structural rhyme the AR sibling recorded: configurable multi-channel cadences over a population. The distinction is the driving object: every treatment here is attached to a delinquent obligation and its money-state, and the loop closes on cure/settlement/charge-off, not on message journeys or pipeline.

### vs ERP-native dunning

Not this Type's historical baseline (that is the AR sibling's). This Type's platform-native baseline is the collections/delinquency module inside loan servicing and core-banking systems — demonstrated by the LoanPro sample.

## Historical / Market-Sample Check (§24)

Would older, regional, platform-native products still fit the L0 definition?

- **Pre-software creditor collections departments** (delinquency ledgers, collector call logs and notes, promise diaries, escalation letters, recovery files): delinquent-account population on the book; recorded treatments by hand; outcomes (cures, arrangements, write-offs) carried on the ledger. Fits — nothing in L0 presumes software-era capabilities.
- **Card-issuer and bank collections systems of earlier eras** (batch delinquency bucketing, collector queues, promise-to-pay tracking, letters): classic L0 with L1 machinery of their time. Fits.
- **Servicing-suite collections modules** (LoanPro today; collections modules of servicing/core systems generally): satisfy L0 natively. Fits as the minimal platform-native form.
- **Regional variation** (digitally-led early-arrears handling in European motor finance; dialer-led US regimes; relationship-first markets): channel mix and compliance regimes vary; the three L0 properties hold. Fits.

The check passes: L0 is not over-fitted to the current AI/omnichannel market, and "strategy engines", "omnichannel", and "AI" correctly sit at L1/L2.

## Uncertainties

- Tier-1 operational documentation was reachable only for LoanPro (servicing-module form). Interface-level mechanics for standalone platforms (exact queue behaviors, state labels, arrangement flows) are inferred from product pages at capability level, not mechanic level; the final document keeps such mechanics conceptual.
- Experian Tallyman and Pega Collections could not be fetched (403/timeout ×2 each). Both are known market names in this space; their absence narrows the sample but does not change the cross-product pattern observed. No detail about either is asserted.
- The exact placement of "debt purchasers running creditor-class platforms" (Qualco roster) between this Type and Debt Collection Management is unresolved; recorded for the Debt Collection Management pass's joint review.
- Whether the treatment-strategy engine should be promoted toward L0 was considered and rejected (LoanPro's module form and historical practice both qualify without it), but it is near-universal in standalone products; a future pass with broader samples could revisit.
- The relationship to the "Debt Management Application" leaf is assumed (consumer-side) but unverified; flagged for that pass.

## Final Synthesis

Canonical Collections Platform, v1.1:

```text
L0 (defining invariant)
- Delinquent repayment obligations on the operator's own book as the
  managed population (credit accounts / postpaid balances drawn from the
  book or servicing system, tracked through delinquency staging:
  missed payments / days past due)
- Recorded collection treatment (automated outreach and/or collector
  actions logged against the account, next actions scheduled)
- Outcome loop closing on the obligation (cures, restructured schedules,
  settlements recorded; charge-off and recovery carried as tracked states
  that keep generating work)

L1 (common mature structure)
- Collector work queues with prioritization and assignment
- Treatment-strategy authoring (paths/decision trees per stage, segment,
  risk); early-stage automated multi-channel outreach
- Payment arrangements and promise handling as first-class objects
- Hardship / forbearance routing; settlement management
- Customer self-service (portal / conversational)
- Regulated-contact compliance machinery and auditable treatment history
- Payment capture / allocation
- Delinquency, roll/cure/recovery and collector analytics
- Continuous delinquency data feed from the book/servicing system

L2 (variant / optional)
- Packaging: standalone enterprise platform / servicing-suite module /
  digital-first SaaS / early-stage editions / agentic digital layers
- Stage emphasis: early-stage digital vs full lifecycle through recovery,
  legal management, asset/repossession
- Industry population: banks/cards/lenders; telco/utility/retail
  postpaid arrears; healthcare adjacent
- Operator: in-house departments, shared services; debt purchasers as an
  adjacent population
- Pre-delinquency early intervention; agency panel management; bankruptcy
  monitoring; embedded ML scoring

L3 (vendor-specific)
- branded interface/agent/AI add-ons, per-jurisdiction compliance engine
  branding, delinquency-category numbering schemes, named AI scorers,
  certification schemes, all vendor-marketed numeric claims
```

The Application Document will present L0 and L1 in natural language (defining core / standard capabilities), name L2 options in Variants, and keep L3 out. The boundary presentations will be: center-of-gravity + object-class distinction vs Collections Automation Platform; ownership-of-the-obligation distinction vs Debt Collection Management; module-form note vs Loan Management System. The collision-resolution recommendation will be recorded in STATUS.md.
