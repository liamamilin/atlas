# Research Notes — Loan Management System

Research date: 2026-09-08
Slug: loan-management-system
Directory leaf: Loan Management System (§08 Finance, Banking, Insurance & Investment)

## Research Goal

Determine what a "Loan Management System" (LMS) actually is in the software market: its defining structure, how the servicing of a loan book works inside real products, who operates it, and where its boundaries sit against the neighboring lending-family leaves (Loan Origination System, Commercial Loan Management, Mortgage Servicing Platform, Consumer Lending Platform, Collections, Credit Management Platform) — several of which are already processed and carry joint-review flags pointing at this leaf.

## Initial Boundary

The leaf sits inside a densely split directory family. Working hypotheses from the prior passes:

1. **From `commercial-loan-management` (processed)**: the market sells single engines spanning consumer + commercial books (Shaw explicitly sells one Spectrum platform across both). Adopted working distinction there: commercial = facility-shaped business credit population (commitments/lines/participations) under negotiated terms. **Instruction carried into this pass: apply the population test (narrowing the sector must not change the core model) and consider variant/alias treatment.**
2. **From `consumer-lending-platform` (processed)**: LOS/LMS = stage-scoped function systems, segment-agnostic; Consumer Lending Platform = borrower-segment-scoped lifecycle platform. LMS is expected to be servicing-scoped.
3. **From `commercial-loan-origination` (processed)**: funding seam confirmed (origination = pre-funding pipeline; loan management = post-funding servicing ledger).
4. Known terminology drift to test: vendors market "LMS" both as servicing-scoped engines AND as end-to-end lending platforms (origination + servicing + collections). The atlas scope for this leaf is the servicing side of the lifecycle.

## Research Questions

1. What is the central object — is it a loan "account", and what data does it carry (terms, schedule, balances, receivables)?
2. What is the recurring servicing loop? (billing → payment application → accrual → status)
3. How is money-in applied (payment allocation/waterfall; over/underpayment; partial payment; reversal)?
4. What life-of-loan actions exist (modifications, due-date changes, draws, delinquency status, payoff, close, charge-off)?
5. What segment differences exist (consumer amortizing vs commercial facility vs specialty) — does the core model survive the population test?
6. What interfaces do servicing operators work in (account query/detail, transaction entry, queues, product configuration, borrower portal)?
7. What rules matter (allocation order, accrual-before-transaction discipline, grace/late-fee machinery, privilege-gated maintenance, audit)?
8. What regulatory/reporting outputs are part of the job (statements, bureau reporting, tax forms, GL export)?
9. What is packaged with the engine vs sold beside it (origination modules, collections modules, portals)?
10. Where exactly are the seams vs the neighboring leaves?

## Representative Products

Selected for market representation, documentation completeness, different product philosophy, and different customer tiers:

| Product | Philosophy | Tier | Role in sample |
|---|---|---|---|
| LoanPro | Modern API-first composable lending platform; origination/servicing/payments/collections suites; fintech + bank tier | Mid-market to enterprise/fintech | In-type sample; end-to-end packaging pole |
| Nortridge Loan System (NLS) | Standalone configurable loan servicing system; 40+ years heritage; extremely diverse loan types incl. specialty | Small/mid lenders, specialty finance | In-type sample; deepest Tier-1 documentation; multi-population anchor |
| Shaw Systems (Spectrum) | Heritage (55+ years claim) ledger-grade servicing workhorse; one engine spanning consumer + commercial + leasing | Banks, non-bank lenders, servicers | In-type sample; population-test anchor (spanning pole) |
| TurnKey Lender | Cloud end-to-end "loan management" suite incl. origination + servicing + collection; global SMB/mid tier | SMB to mid-market, global incl. emerging markets | In-type sample; suite-packaging pole |

Rejected / not fetched:
- Finastra Loan IQ / LoanServ — already sampled in the commercial pass; avoided re-sampling the same vendor twice in one sample (their evidence is inherited from `research/commercial-loan-management.md`).
- nCino — inherited as the origination-led boundary pole from the commercial pass (monitoring/covenants documented, servicing ledger absent) — boundary evidence, not core evidence.
- Sopra, Temenos, Fiserv, Jack Henry core-banking modules — unreachable/unfetched; core-banking-embedded realization remains under-evidenced (same limitation as the commercial pass).
- HES FinTech — backup candidate; not needed (stop conditions reached with 4 products).

## Sources

All fetched 2026-09-08.

Tier-1 (operational documentation):
- Nortridge User Guide (NLS): https://userguide.nortridge.com/ — incl. Transaction Entry (https://userguide.nortridge.com/topics/transaction-entry) and NLS Service (https://userguide.nortridge.com/topics/nls-service)
- LoanPro Knowledge Base: https://help.loanpro.io/ — incl. Servicing and collections overview (https://help.loanpro.io/servicing-and-collections/servicing-and-collections-overview)

Tier-2 (official product pages):
- LoanPro — homepage https://www.loanpro.io/ ; Loan Management System page https://www.loanpro.io/loan-management-software/
- Nortridge — homepage https://nortridge.com/ ; Loan Management Software https://nortridge.com/loan-management-software/
- Shaw Systems — homepage https://www.shawsystems.com/ ; Loan Management Software https://www.shawsystems.com/loan-management-software/
- TurnKey Lender — homepage https://www.turnkey-lender.com/ ; Loan Management Software https://www.turnkey-lender.com/loan-management-software/

Inherited evidence (fetched in the commercial pass, same research effort):
- research/commercial-loan-management.md — Finastra Loan IQ, Finastra Shaw/Spectrum commercial line, nCino boundary pole.

Vendor-claimed numbers ("25M+ active loans", "$22B annual repayments", "600+ customers", "$750B in active loans", "150+ reports", "3M loans/day", "90% automation", "55+/40+ years") are recorded as vendor claims only and are NOT used as structural facts.

## Product A — LoanPro

### Key observations (evidence layer A unless noted)

- Self-positioning: "composable lending and credit platform built on API-first infrastructure"; suites: Modern Lending Core, Origination Suite, Servicing Suite, Collections Suite, Payments Suite.
- FAQ defines the category: "A loan management system (LMS) is the central platform lenders use to manage the entire loan lifecycle, including origination, servicing, payments, and collections" — i.e., end-to-end packaging vocabulary.
- Credit programs supported: installment loans, credit card, line of credit, lease, hybrid/custom; "specialty lending such as solar loans, construction loans, and BNPL"; "commercial and alternative finance including merchant cash advances and equipment financing". One engine, many populations.
- Servicing overview (Tier-1) — the operational inventory:
  - **Customer portal**: borrower self-service — view account details, make payments, manage loan information.
  - **Agent surfaces**: configurable agent walkthroughs (step-by-step guides through complex processes); account queues serving accounts needing attention; payment processing; adjustments; document management; "other account activities without switching between multiple systems".
  - **Delinquency machinery**: delinquency tracking (delinquency categories), defaults/charge-offs, payment plans, hardship programs enrollment.
  - **Collateral management and insurance tracking** for secured accounts.
  - **End-of-life**: "Agents can calculate payoffs, process final payments, close accounts properly, and archive completed loans for future reference."
  - **Back office**: pre-built reports, ad hoc analytics, direct database connection; smart checklists for multi-step processes (bankruptcy, hardship enrollment); automation engine driven by business logic; automated communications; alerts.
- LMS page: automation engine automates "customer onboarding, applying payments, sending customer communications, performing collateral management, and updating loan status"; communications via email/SMS/direct mail/phone; payments with AutoPay, custom payment schedules, transaction routing; "compliant loan modifications in days" (marketing); migration of "historical account and transaction data from your legacy loan management software" — evidence that loan accounts + transaction history are the migrating record.
- Compliance posture mentions: TILA, Reg Z, TCPA, CARD Act, SCRA, PIPEDA; PCI-DSS, SOC 2/3; role-based access controls.

## Product B — Nortridge Loan System

### Key observations (evidence layer A)

- Self-positioning: "loan servicing software" (root page title: "Loan Servicing & Management Software") with separate Loan Origination and Loan Collections feature pages; escrow servicing module, participations servicing module, captive finance module, print & mail module.
- FAQ boundary statement (important for the terminology-drift question): "Loan management software covers the full loan lifecycle, including origination, while loan servicing software focuses on post-origination activities. Nortridge handles both seamlessly."
- Loan types / industries documented (population breadth): distressed debt, hard money, medical, mortgage, payday, structured settlement, student, timeshare; auto finance, agriculture, CDFI & non-profit, commercial lending, consumer installment, education, healthcare, micro-finance, real estate & mortgage. One system, 14+ populations.
- **Transaction Entry (Tier-1)** — the payment-application machinery:
  - Accrual discipline: "If the daily accruals on the loan are not up to date, you will be prompted to run accruals for this particular loan" before entering a transaction.
  - Payment distribution: payment amount distributed between Principal, Interest, Late Charges, Fees, and Miscellaneous balances; and between Past Due Receivables, Current Receivables, and unbilled balances. The borrower pays an amount, "the system will account for overpayments or underpayments according to the loan's default distribution."
  - Overridable waterfall: "The default distribution may be overridden"; cannot distribute more than available in the corresponding billing field ("you can not distribute to Past Due Interest if there is no existing Interest Receivable past due"); payment must balance before finalizing.
  - Detail tab: control distribution on an individual billed-payment level when multiple billings are outstanding.
  - **Payoff**: "the system will automatically write-off any balances in excess of the amount of the payment. If the payment is in excess of the payoff amount, the excess will go to suspense." Optional `Set Loan Status = CLOSED`. Zero-amount payoff semantics for clearing payoff dates.
  - US-regulatory machinery: IRS write-off event codes printed on Form 1099-C Box 6 (write-offs ≥ $600); Form 8300 payer designation ("Paid By" other than borrower); US/Canadian ACH/AFT.
  - Grace/late-fee interplay: "If a late billing generated a late fee, and a payment which is applied to that billing is back-dated to prior to the expiration of the grace period, the late fee will be reversed automatically by the system."
  - Quick Payment (simplified entry); Bulk Payments (one transaction distributed among multiple loans, reversible as a unit).
- **NLS Service (Tier-1)** — the scheduled back-office: automated accruals (scheduled runs; parameterizable by loan group, state, account; CPU-scaled threads); automated report generation; automated statement generation (printer/document queue); automated collection campaign updates; ACH (NACHA) file creation for ACH payments; ACH disbursements; payment-card processing by loan group; credit bureau Metro 2 file generation (Equifax/Experian/TransUnion headers); GL interface (external DLL wrapper); NCOA address processing; archiving of loans with ARCHIVE status; bankruptcy notifications/subscriptions (BankruptcyWatch integration); SFTP-based payment return processing; email/SMS on service events.
- Email & SMS for "statements, late notices, posted payments, and other events".
- Security setup: per-function privileges for individual users and groups (e.g., LOAN > Transaction Entry > Payoff).
- Payment processing feature page: ACH, debit/credit cards, cash via PayNearMe; "Configure custom payment waterfalls"; CIF (Customer Information File) borrower records with documents, communication history, user-defined fields; 150+ standard reports (vendor claim); hosting on-premise or cloud.

## Product C — Shaw Systems (Spectrum)

### Key observations (evidence layer A; layer B where inherited)

- Self-positioning: "The only Loan & Lease Management System with embedded AI"; "servicing, collections, loans, lines of credit, and leases".
- Solution lines over one platform: Loan Management, Collections, Spectrum Xpress (rapid go-live), Recovery, Commercial, Leasing, Dealer Floor Plan — servicing, collections, and recovery are separable solution lines (boundary evidence vs Collections).
- Industries served: banking, consumer lending, business lending, fintech, auto finance, home improvement lending, BNPL (+ commercial line, leasing) — one engine across populations (population-test anchor).
- Loan Management page: 360 view ("customer-centric account management and automated communication campaigns"); API-first architecture; payment processing ("comprehensive, scheduled, and on-demand integrated payment tools"); securitization management ("manage, track, and report on sophisticated securitization structures"); pop-up alerts ("real-time alerts inform staff of account conditions and reinforce policy and compliance requirements"); custom screens ("each agent work group can control their preference for borrower and account data views"); risk & compliance ("configuration to guide the loan life cycle path"); automated workflow (smart queuing).
- "Shaw's solution handles all parts of the servicing life cycle. This includes communication through many channels, accounting, customer service, managing delinquencies, recovery, and placement." Also: "We help borrowers change their due dates" — life-of-loan modification as a routine servicing operation.
- Inherited from the commercial pass (same vendor, commercial line): servicing ledger + life management claims supported; commitments/lines/participations; non-accrual status; shadow accounting; credential-gated maintenance; SBA/PPP tracking (US-regional); securitization.

## Product D — TurnKey Lender

### Key observations (evidence layer A)

- Self-positioning: "end-to-end loan management software"; nav separates Loan Origination Software, Loan Management Software ("Automated payments and loan servicing"), Debt Collection Software, Credit Scoring & Decisioning; also a separate "Loan Servicing Software" page. FAQ: "offer both business and consumer loans from a single unified platform"; "separate dedicated workplaces tailored exactly to your requirements" for "origination, underwriting, servicing, and collection teams".
- LMS toolset page: "one-stop platform for loan origination, onboarding, loan management, and reporting"; credit product builder: "Create hyper-flexible credit products with complex schedules, fees, taxes, interest and configurable rules, and auto-generate loan statements"; collateral management module ("assets valuation and re-evaluation"); debt collection ("AI-based collections scoring… delinquency buckets, configurable collection strategies"); batch data importing "(including payments, users and loans)"; automatic "due date reminders and automatic fees".
- Borrower lifecycle flow as marketed: "Borrower applies online → after auto-processing, the borrower signs the loan agreement → funds are disbursed → payments are automatically charged until repayment → borrower continues working with you in their personal portal."
- Integrations: 75+ accounting systems, credit bureau, KYC/AML, payment and notification providers; API/ETL tooling.
- Industries: consumer, commercial, BNPL/embedded, AR financing, medical, P2P, leasing/equipment, non-profit, payday/microfinance, merchant cash advance, bank automation.

## Cross-product Comparison

| Dimension | LoanPro | Nortridge (NLS) | Shaw (Spectrum) | TurnKey Lender |
|---|---|---|---|---|
| Category label used | "loan management system" (end-to-end) | "loan servicing & management software" | "Loan & Lease Management System" | "loan management software" (end-to-end) |
| Account population | installment, cards, LOC, lease, MCA, BNPL, commercial | 14+ types: consumer, commercial, student, medical, timeshare, structured settlement, payday, mortgage, ag, microfinance | banking, consumer, business, auto, home improvement, BNPL + commercial, leasing, floor plan | consumer, commercial, P2P, medical, equipment, payday, BNPL, non-profit |
| Servicing loop evidence | automation of "applying payments… updating loan status"; Payments Suite | payment distribution (principal/interest/late/fees/misc; past-due vs current receivables) + scheduled accrual runs | "comprehensive, scheduled, and on-demand integrated payment tools"; accounting | "payments are automatically charged until repayment"; auto fees; statements |
| Billing/statements | statements + communications suite | scheduled statement generation + print/mail | automated communication campaigns | auto-generated loan statements + due-date reminders |
| Life-of-loan actions | "loan modifications in days"; payoff/close/archive | transaction types, payoff with suspense + CLOSED status, bulk ops | due-date changes; life-cycle path configuration | restructuring via product builder |
| Delinquency | delinquency categories, charge-offs, hardship programs | collections module + late notices + collection campaigns | collections/recovery/placement solution lines | debt collection module, delinquency buckets |
| Regulatory outputs | TILA/Reg Z/TCPA/CARD Act/SCRA posture | Metro 2 bureau files, 1099-C, 8300, NACHA | pop-up policy/compliance alerts | KYC/AML |
| Borrower portal | customer portal (Tier-1 documented) | not documented on fetched pages | 360 view + borrower engagement (Amplify line) | personal portal (flow documented) |
| Deployment | cloud (AWS claim) | on-prem or vendor cloud | on-prem heritage + cloud claims | cloud |
| Packaging | origination + servicing + collections suites | servicing engine + origination + collections modules | servicing-led suite + collections/recovery lines | origination + servicing + collection suite |

Reading:
1. **The servicing loop + the account of record are the deepest common structure.** All four maintain loan accounts with computable terms; apply incoming money to balances; compute interest/fees; produce bills/statements; and keep balances and status current.
2. **Life-of-account actions are documented in all four** (modifications, due-date changes, payoff/close; delinquency status changes).
3. **Origination is packagable and separable** — Nortridge's own FAQ defines servicing as post-origination; LoanPro/TurnKey ship origination as separate suites; TurnKey separates "Loan Management" from "Loan Servicing" pages while selling both. The market vocabulary "LMS" drifts between servicing-scoped and end-to-end, but the structural constant is the funded-book machinery.
4. **Collections/recovery are consistently separable** — Shaw sells them as solution lines; LoanPro and TurnKey as suites/modules; Nortridge as a feature module. The engine tracks delinquency status and hands off.
5. **One engine spans populations** — the population test passes: narrowing the sector does not change the core model. Nortridge's 14+ loan types, Shaw's consumer+commercial+leasing span, LoanPro's installment/card/LOC/lease/MCA/BNPL list, TurnKey's consumer+commercial+P2P list all run on the same account/servicing machinery.
6. **Borrower portal is common but not universal** — three of four document one; Nortridge's fetched pages emphasize print/mail and staff surfaces instead. Common-mature, not definitional.
7. **US-regulatory machinery appears as product features** (1099-C, 8300, Metro 2, NACHA, SCRA/CARD Act) but is regional; the core model survives without it.

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

A Loan Management System is the lender-side system of record for the funded loan book. Smallest structure without which the Type stops being recognizable:

```text
Lender/servicer operates the book (staff-side operator; borrower self-service is a companion surface)
└── Credit account of record (one persistent, individually identified account per
    loan / line / credit position held by the lender)
    └── Contractual terms held as computable data
        (schedule, rate basis, fees — the data the system computes from)
        └── Recurring servicing loop
            (payment application — money-in allocated across balances per the
             account's waterfall; interest accrual and fee/charge computation;
             billing/statements; balance and status maintenance)
            └── Life-of-account management
                (system-executed, recorded changes to the position —
                 modifications, status changes, delinquency progression,
                 payoff/close — through the end of the account's life)
```

Four properties:

1. **Lender-side system of record** — the operator is the lender or servicer holding the credit; the account belongs to the institution's book, not to the borrower's personal finance view.
2. **The credit account of record with computable terms** — a funded loan/line/credit position persists as an individually identified account whose schedule, rate basis, and fees are data the system computes from, not document references alone.
3. **The recurring servicing loop** — payment application, accrual/fee computation, billing, and balance/status maintenance run continuously for the life of the account. Without this the product is a pipeline, a monitoring dashboard, or a payment calculator.
4. **Life-of-account management as system-executed action** — changes to the position (modifications, status changes, delinquency progression, payoff/close) are executed through and recorded by the system. Without this the product is a statement generator or ledger viewer.

Jointly-held is load-bearing:
- 1+2+4 without 3 = origination-style case file or monitoring layer (nCino shape from the commercial pass).
- 1+3+4 without 2 = payment processor / collections workbench with no whole-position model.
- 2+3+4 without 1 = borrower-facing account portal (banking-platform / borrower-portal territory).

L0 is deliberately era-neutral: a mainframe-era loan master file with payment posting, accrual runs, statements, and payoff processing satisfies it; pre-software practice (loan ledger card + payment register + interest book + payoff quote maintained by loan clerks) satisfies the conceptual core.

### L1 — Common Mature Structure (standard capabilities in mature products; not definitional)

Present in two or more sampled products:

- **Payment processing rails** — ACH/card/check/cash handling, AutoPay/recurring charging, scheduled and on-demand payment runs (all four).
- **Billing and statement generation** — scheduled statements, print/mail or digital delivery, due-date reminders (all four).
- **Scheduled batch processes** — nightly accrual runs, ACH file creation, statement runs, report runs, archiving (Nortridge NLS Service; LoanPro automation engine; Shaw automated workflow).
- **Delinquency tracking and collections support** — delinquency categories/buckets, late notices, payment plans/hardship programs, handoff to collections modules or solution lines (all four).
- **Automation/workflow engines and alerts** — business-logic automations, queues, pop-up alerts (all four).
- **Borrower/customer records** — CIF-style central borrower record with documents, communication history, relationships (Nortridge; Shaw 360 view; LoanPro/TurnKey customer layers).
- **Collateral tracking** — collateral and insurance management for secured accounts (LoanPro, Nortridge, TurnKey; not surfaced on Shaw's fetched pages).
- **Borrower self-service portal** — account view + payments + self-service actions (LoanPro, TurnKey documented; Shaw borrower-engagement line; Nortridge not documented on fetched pages — companion surface, sometimes externalized as a sibling product per the commercial pass).
- **Reporting and portfolio analytics** — standard report libraries, dashboards, ad hoc analytics, direct data access (all four).
- **GL/accounting connectivity and export** (Nortridge GL interface; Shaw accounting; inherited commercial-pass GL connectivity).
- **Credit bureau reporting and external data integrations** — Metro 2-style bureau files, bureau/KYC/payment integrations (Nortridge, LoanPro, TurnKey).
- **Audit trail and privilege-gated maintenance** — per-function security privileges, role-based access, auditable changes (Nortridge, LoanPro; inherited: credential-gated maintenance in the servicing family).
- **Configurable credit/product setup** — no-code loan product / program configuration (all four; the servicing engine is parameterized by product, which is what lets one engine serve many populations).

### L2 — Variant / Optional Structure

Depends on segment, geography, product family, era:

- **Population specialization poles** — consumer/amortizing installment pole vs commercial facility pole (commitments, lines, draws, participations, covenants — the Commercial Loan Management realization) vs specialty asset classes (student, timeshare, structured settlement, hard money, medical, agricultural, microfinance, payday, BNPL, lease). The core model is identical; the machinery around it is population-tuned.
- **Mortgage-flavored machinery** — escrow servicing as a module (Nortridge escrow module); full residential-mortgage machinery (escrow analysis, investor/GSE reporting, foreclosure timelines) is the Mortgage Servicing Platform family.
- **Securitization management** (Shaw; sophisticated investor structures).
- **Dealer floor plan** (Shaw — inventory-secured lines to dealers; adjacent specialty).
- **Origination bundling** — standalone servicing engine vs end-to-end suite (the dominant packaging variant; the servicing-ledger test, not the marketing label, decides membership in this Type).
- **Third-party servicing posture** — servicers operating the engine for originated books (inherited from commercial pass; Shaw recovery/placement lines).
- **Regional regulatory machinery** — US 1099-C/8300/Metro 2/NACHA/SCRA/CARD Act; jurisdiction-specific equivalents elsewhere; nothing in the core requires a specific regime.
- **Deployment posture** — on-premise vs cloud/SaaS (Nortridge documents both poles in one product).
- **AI layers** — embedded AI for servicing/collections propensity, AI-ready infrastructure, AI decisioning (all four; era-current marketing layer).

### L3 — Vendor-specific (research notes only)

- LoanPro: Modern Lending Core / Adaptive Wallet / Smart Panel / Smart Verify branding; Clojure-based automation rules; Best Egg/Octane/WaFd customer-story metrics; "25M+ active loans", "2,000+ programs", "$22B annual repayments" claims.
- Nortridge: NLS Service parameter flags (/Y, /G, /Z, NACHA /H /N /M /F, Metro 2 /H /X /Q); Quick Payment; Bulk Payment auto-fill defaults; $600 1099-C threshold; PayNearMe integration; Sonnet; NCOA scheduling; per-version feature notes (NLS 5.x).
- Shaw: Spectrum / Spectrum Xpress / Amplify / AI Advisor / Insight branding; "only LMS with embedded AI" claim; 55+ years claim; custom screens per workgroup.
- TurnKey Lender: "3 millions loans per working day" claim; country availability list (UK/US/CA/FR/AU/SG); 75+ integrations claim; proprietary AI decisioning; P2P tranche mechanics.

## Vendor-specific Findings

1. **The servicing ecosystem splits into sibling products around one engine** (inherited): Finastra ships Loan Portal (borrower self-service) as a separate product over the servicing engine — borrower-facing surface is not part of the engine in the strongest-servicing vendor's own packaging. LoanPro and TurnKey bundle portals in; Nortridge documents none. Portal = variant, not definer.
2. **Collections/recovery are consistently sold beside the servicing engine** (Shaw solution lines; LoanPro/TurnKey suites; Nortridge module) — supporting the loan-management/collections boundary.
3. **An origination-led platform can reach "portfolio management" without a servicing ledger** (nCino, inherited) — the market label "loan management/lifecycle" spans two system types; the funded-position test (is a servicing ledger documented?) decides.
4. **The same vendor can serve as the anchor for two directory leaves** (Shaw commercial line → Commercial Loan Management; Shaw consumer/lease lines → this leaf) — evidence that the directory's sector split is inside single products.
5. **Terminology drift is vendor-documented**: Nortridge's own FAQ distinguishes "loan management software covers the full loan lifecycle, including origination" from "loan servicing software focuses on post-origination activities"; LoanPro/TurnKey use "LMS" for the end-to-end platform. The category label is packaging-sensitive; the structural constant is the funded book.

## Boundary Findings

| Neighboring Type | Seam | Test ("remove what → becomes the other Type") |
|---|---|---|
| Loan Origination System (§08, unprocessed sibling) | funding seam: pre-funding pipeline (application, decisioning, documents, closing) vs post-funding servicing of the funded book. Handoff at booking/funding. Packaging blurs: vendors market "LMS" end-to-end; origination-led suites market "lifecycle" language without servicing ledgers | strip the servicing loop + account ledger → LOS; strip the pipeline → LMS |
| Commercial Loan Management (§08, processed) | sector seam inside one servicing family — RESOLVED from this side: the population test passes (narrowing the sector does not change the core model; Shaw/Nortridge/LoanPro/TurnKey all span populations on one engine). The commercial leaf = this Type restricted to facility-shaped business credit (commitments/lines/participations) under negotiated terms | narrow the population to facility-shaped commercial credit and add facility machinery → commercial leaf; the generic leaf is the full Type |
| Mortgage Servicing Platform (§08, unprocessed) | product-family variant: residential-mortgage machinery (escrow analysis, investor/GSE reporting, foreclosure timelines) vs the generic account model. Generic LMS covers mortgage loans thinly (Nortridge mortgage page + escrow module) | replace the generic account model with mortgage-specific escrow/investor/foreclosure machinery → MSP |
| Consumer Lending Platform (§08, processed) | scope axis per that pass's resolution: segment-scoped lifecycle platform (origination→servicing→collections on one record for consumer borrowers) vs stage-scoped function system | add borrower-segment lifecycle packaging → consumer platform; strip to the servicing function → LMS |
| Collections Platform / Debt Collection Management (§08, processed) | lifecycle seam: performing-book servicing vs pursuit of defaulted/arrears balances. All four sampled vendors ship collections as a separate module/line; the LMS tracks delinquency status and hands off | remove the performing book, keep pursuit of defaulted balances → collections |
| Core Banking System (§08, processed) | substrate seam: the servicing engine may be a module of the core or a standalone specialist feeding it; in the core the loan account is one family among others | strip the loan-domain servicing model, keep GL/deposit operations → core banking |
| Credit Management Platform (§08, processed) | domain seam: seller-side trade credit (customers buying on open account, limits/orders) vs lender-side loans (borrowers with amortizing/facility accounts) | swap trade-credit customer records for loan accounts → credit management platform |
| Credit Risk Platform (§08, processed) | layer seam: risk measurement over positions vs the transactional servicing ledger | strip the ledger, keep risk measures/limits → credit risk platform |
| Commercial Banking Platform / Mortgage Borrower Portal (§08) | operator/surface seam: bank-staff engine vs client-facing account view | move the operator to the borrower and drop the servicing ledger → banking portal surface |
| Billing/Invoicing / Accounts Receivable (§08) | record seam: open invoices receivable from customers vs a loan account with schedule-driven billing, accrual, and whole-position lifecycle | replace invoice records with loan accounts carrying terms/schedule → LMS |

**Boundary-issue lines to record in STATUS.md**:

1. Population test RESOLVED from this side (commercial-loan-management flag): generic Loan Management System = the full Type; core model unchanged across consumer/commercial/specialty populations. Commercial Loan Management and Mortgage Servicing Platform = sector-scoped siblings; directory keep-both with variant treatment recommended at joint review.
2. Terminology drift + funding seam (loan-origination-system flag reiterated): "LMS" is used in the market for both servicing-scoped engines and end-to-end platforms; membership test = documented servicing ledger over funded accounts. Joint review recommended when loan-origination-system is processed.

## Historical / Market-Sample Check

- **Generational evidence**: Shaw claims five decades of loan management software; Nortridge 40+ years; both carry ledger-era vocabulary (accrual runs, statements, payoff, suspense, archiving). A mainframe-era loan system — master file, payment posting, accrual batch, statements, payoff processing — satisfies L0 without cloud, portals, workflow GUIs, AI, or monitoring dashboards. Pre-software servicing (loan ledger cards, payment registers, interest books, clerk-computed payoff quotes) satisfies the conceptual core; the software digitizes and automates the loop. **Historical check passes.**
- **Regional check**: 1099-C/8300/Metro 2/NACHA/SCRA/CARD Act machinery is US-regional; Canadian AFT appears beside US ACH in the same product (Nortridge); TurnKey claims multi-country availability. Nothing in L0 requires a jurisdiction, payment rail, or regime.
- **Sector check**: the account populations in the sample span consumer, commercial, student, medical, agricultural, microfinance, timeshare, BNPL, lease, P2P — the core model is identical across them. No surface artifact (payment rail, portal, product name) is load-bearing.
- **Packaging check**: standalone engines (Nortridge) and end-to-end suites (LoanPro, TurnKey) both satisfy the core; origination bundling is optional.

## Uncertainties

- **Tier-1 depth is asymmetric**: Nortridge and LoanPro contributed Tier-1 operational documentation; Shaw and TurnKey evidence rests on official product pages (Tier-2). Servicing-loop claims are asserted at the structural level; precise accrual conventions (day-count bases), posting order variants, grace-period defaults, and exact state-machine labels were observed only in Nortridge's guide and are kept out of the final document's precision claims.
- **Core-banking-embedded realizations** (Fiserv/FIS/Jack Henry/Temenos lending modules) remain unverified — same limitation as the commercial pass.
- **Nortridge borrower-portal presence** was not confirmed on fetched pages (print/mail focus); portal-commonality claim is carried by the other three products and worded as "most".
- **Whether the market will consolidate LOS+LMS labels** (or whether atlas leaves LOS/LMS remain both) is a taxonomy judgment for joint review, recorded above, not settled here.
- TurnKey's "Loan Servicing" vs "Loan Management" page split suggests its own vocabulary is not stable; only the page-level claims were used.

## Final Synthesis

A Loan Management System is the lender-side system of record for the funded loan book. Its defining core: a persistent, individually identified credit account per loan/line/credit position held by the lender, with its contractual terms (schedule, rate basis, fees) held as data the system computes from; the recurring servicing loop that bills the borrower, applies incoming money across the account's balances, computes interest accrual and charges, and keeps balances and status current; and life-of-account management — modifications, status changes, delinquency progression, payoff/close — executed through and recorded by the system to the end of the account's life. Around this core, mature products add the machinery a servicing operation runs on: payment processing rails, scheduled billing/statement/statutory output, batch accrual and file-generation processes, delinquency tracking with collections handoff, automation engines and alerts, borrower records and self-service portals, collateral tracking, reporting and GL/bureau connectivity, privilege-gated maintenance with audit trails, and configurable loan-product setup that lets one engine serve many populations. The population test passes: the same core model serves consumer installment books, commercial facility books, and specialty asset classes — which is why sector-scoped siblings (Commercial Loan Management, Mortgage Servicing Platform) are variants of this Type's population, and why vendors can honestly sell one engine across all of them. The boundary that matters most: the origination pipeline ends at funding; this Type takes over the funded account. Collections takes over defaulted balances; risk platforms measure the book; core banks host it; borrowers see it only through companion portals. The Type predates every modern artifact — the servicing ledger is one of the oldest jobs in banking software — which is what makes the small definition stable.
