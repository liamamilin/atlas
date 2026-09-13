# Research Notes — Consumer Lending Platform

## Research Goal

Understand the software category "Consumer Lending Platform" from real products: what a platform for lending to individual consumers actually consists of, what objects it manages, how a loan moves from application to payoff, who operates it, and where its boundary lies against the neighboring directory leaves (Loan Origination System, Loan Management System, Credit Decisioning Platform, Mortgage Origination/Servicing, Commercial Loan Origination/Management, Collections Platform, Debt Collection Management).

## Initial Boundary (hypothesis before research)

- Hypothesis: a Consumer Lending Platform is the lender-side system of record for consumer credit (personal/installment loans, auto, POS/BNPL, credit lines, cards, short-term products), spanning application → credit decision → funding → servicing → collections.
- Most likely confusions:
  - vs Loan Origination System (LOS): stage-scoped function, segment-agnostic.
  - vs Loan Management System (LMS): servicing-scoped function, segment-agnostic.
  - vs Credit Decisioning Platform: the evaluation engine alone.
  - vs Mortgage Origination/Servicing: real-estate-collateralized consumer credit with its own machinery.
  - vs Commercial Loan Origination/Management: business borrowers, not consumers.
  - vs Collections Platform / Debt Collection Management: the delinquency stage only.
  - vs Digital Banking Application: consumer-facing channel, not lender-side operations.
- Unknowns at start: does the market treat "consumer lending platform" as end-to-end lifecycle, or as origination-only? Is collections part of the defining core? Does the borrower segment (consumer vs commercial) carry the type boundary?

## Research Questions

1. What are the core objects (borrower, application, decision, loan account, schedule, payment)?
2. How does the origination flow actually work, stage by stage?
3. What does servicing consist of (billing, autopay, accrual, adjustments, statements, portal)?
4. How is delinquency handled, and is collections machinery definitional or optional?
5. What configuration exists (credit products, workflows, roles)?
6. How do products differ in packaging: end-to-end vs origination-pole vs servicing-pole?
7. Which capabilities are common-but-not-definitional (AI decisioning, integrations, compliance tooling)?
8. Historical check: would paper-era / core-banking-era consumer lending setups satisfy the definition?

## Representative Products

Selected for market representation + documentation completeness + different philosophies + different customer tiers:

| Product | Pole / philosophy | Customer tier |
|---|---|---|
| LoanPro | API-first "modern lending core"; end-to-end suites (Origination / Servicing / Collections / Payments); servicing heritage | Fintechs + banks + credit unions (US-centric) |
| TurnKey Lender | End-to-end all-in-one consumer + commercial lending automation with proprietary AI decisioning | SMB → enterprise, global non-bank lenders |
| MeridianLink Consumer | Origination-pole consumer LOS for regulated depository institutions | Community banks & credit unions (US incumbent) |
| HES FinTech (LoanBox) | End-to-end configurable loan management, vendor-code-license / on-prem options, AI sibling products (GiniMachine, CollectionAgent) | Global fintechs / niche lenders, multi-region |

Sampling intentionally includes an origination-only consumer LOS (MeridianLink) to test whether servicing is definitional.

## Sources

All fetched 2026-09-07 (Tier 1/2 official vendor surfaces):

- LoanPro — https://www.loanpro.io/ (home incl. FAQ), https://www.loanpro.io/platform/servicing-suite/, https://www.loanpro.io/platform/origination-suite/, https://www.loanpro.io/platform/collections-suite/
- TurnKey Lender — https://www.turnkey-lender.com/ (home), https://www.turnkey-lender.com/consumer-lending-software/
- MeridianLink — https://www.meridianlink.com/products/consumer-lending-software/ (product page incl. FAQ)
- HES FinTech — https://hesfintech.com/ (home incl. FAQ, product-cycle pages)

Source-access limitation: deep operational help centers (help.loanpro.io product guide, docs.hesfintech.com, MeridianLink client documentation, TurnKey KB) were not fetched in this pass; evidence comes from official product pages and vendor FAQs, which include substantial operational descriptions (loan-origination stage lists, servicing feature lists, borrower flow walkthroughs). Precise numeric limits, default settings, fee formulas, and regulatory posture specifics are therefore NOT asserted in the final document; vendor marketing metrics (e.g. "600+ lenders", "50 million borrowers", "25M+ active loans") are recorded here as vendor claims only and excluded from the canonical document.

## Product A — LoanPro

### Key observations (Layer A unless noted)

- Positioning: "composable lending and credit platform built on API-first infrastructure"; suites: **Modern Lending Core** (real-time ledger, Compliance Safeguard), **Origination Suite**, **Servicing Suite**, **Collections Suite**, **Payments Suite**.
- Credit programs page taxonomy: installment loans, credit card, line of credit, lease, hybrid/custom; "virtually any class of credit product, whether business or consumer, unsecured or collateralized" — consumer is one served segment among several (industries nav: financial institutions, consumer lending, business lending, auto lending, neobanks).
- Origination FAQ gives an explicit stage model: **1. Application Intake → 2. Underwriting & Decisioning (integrated decision engine) → 3. Offer Generation → 4. Closing & Funding (automated disbursement) → 5. Servicing Handoff (instant real-time creation of the loan account)**. Origination pain points named: TILA disclosures inconsistent between origination and servicing systems; rigid data gathering; disjointed tools.
- Origination features: API connectivity to acquisition/underwriting/decisioning tools and AI agents; API calculator (borrowers see dynamic rates/payment schedules); dynamic documents (contracts, closing docs, disclosure forms, welcome packages merged with borrower/account data); personalized application (borrowers enter/edit personal info, payment details, origination docs); flexible funding (disburse funds, issue credit cards via integrated payment partners); compliance-aware intake (SCRA, TILA, OFAC via "Smart Verify", ECOA guardrails for AI decisioning).
- Servicing features: agent walkthroughs; communications suite (personalized notices, disclosures); **comprehensive loan recasting** ("backdate any adjustment to our real-time ledger and recalculations happen automatically"); role-based access; automation engine (configurable rule-based automation); reporting suite (regulatory, investor, internal); borrower portal (self-service); AI connectivity.
- Collections features: automation engine; **collections queues** (prioritized agent work); borrower portal hardship self-enrollment; APR match; loan recasting; collateral tracking ("for any necessary repossession actions"); hardship programs (case study: skip-payment, interest-only, pay-what-you-can programs launched for a customer during COVID-19).
- Payments: AutoPay setup, "any payment method imaginable" via supported payment partners.
- Servicing FAQ: servicing = "all post-origination account activity — from payments and interest accrual to customer support and collections" on a real-time ledger; end-to-end = Origination + Servicing suites on one core "eliminating costly data siloes and friction between origination and servicing hand-offs".
- Product classes for servicing: commercial, auto, consumer/installment, leases, lines of credit, credit cards.

## Product B — TurnKey Lender

### Key observations (Layer A unless noted)

- Positioning: "global platform that automates lending processes for consumer and commercial finance providers… automate loan origination, underwriting, servicing, debt collection, and reporting." Modules: Loan Origination Software, Loan Management Software, Debt Collection Software, Credit Scoring & Decisioning, API/Integrations, Underwriting, Loan Servicing, Peer-to-Peer, Risk Management, Decision Management System.
- **Consumer Lending Software** solution page: "your own intelligent, AI-powered, end-to-end consumer lending platform"; target credit products: personal loans, embedded finance, non-profit credit, micro/payday, P2P, credit cards & overdraft, leasing, medical credit; industries: BNPL, auto financing, secured, payday, leasing, P2P, home improvement.
- Platform feature list: proprietary AI decisioning; loan underwriting (risk scoring, borrower evaluation, decision rules checks, loan agreement generation, loan offer management); 75+ preconfigured integrations (accounting, credit bureau, KYC/AML, payment, notification providers); **powerful credit product builder** ("complex schedules, fees, taxes, interest and configurable rules, auto-generate loan statements"); enterprise-grade reporting; debt collection (AI-driven collection priority, **delinquency buckets**, configurable collection strategies, conversation scripts); **collateral management** (valuation/re-evaluation); batch data importing (payments, users, loans).
- Borrower flow stated verbatim on the consumer page: "Borrower applies online quickly and easily → After auto-processing, the borrower signs the loan agreement → Funds are disbursed → Payments are automatically charged until repayment → Borrower continues working with you in their personal portal."
- Staff flow: "Loan terms are calculated based on borrower's data → Loan application is approved automatically or by your staff → Automatic loan servicing and payments can be easily managed manually too → Automated borrower communication is fully configurable → In-depth reporting."
- IDC MarketScape badge: "North American Consumer Lending Decisioning Platforms 2023–2024" — vendor claim, category confirmation only.

## Product C — MeridianLink Consumer

### Key observations (Layer A unless noted)

- Positioning: "MeridianLink Consumer is a **cloud-based loan origination system (LOS)** that empowers banks and credit unions" — explicitly the origination pole for regulated depository institutions.
- Loan types: personal loans, credit cards, auto loans, business loans, real estate loans (HELOC mentioned in product copy), indirect loans; "supports a full suite of lending products… while connecting with hundreds of partner integrations."
- Features: advanced decisioning engine (configurable rules, **visual logic trees**, real-time data; automated underwriting); real-time borrower communication (SMS/email status updates); built-in reporting/analytics (dashboards, up to three years of origination data via "Insight Lite"); native cross-sell engine (apply for another product within the same application session); mobile-first application with adaptive fields; consolidated platform "allowing borrowers to apply for multiple loan products within a single application session"; compliance ("embedded controls, audit trails, and integrations for fraud and identity verification").
- Servicing handoff evidence: "a frictionless, mobile-ready application that **syncs directly to your core for immediate onboarding** and quicker access to funds" — servicing is NOT carried by this product; it hands off to the institution's core system. Also sells separate Collections product (MeridianLink Collect) and indirect lending product (DecisionLender).
- Market-defining FAQ (vendor's own definition of the category): "Consumer lending software is a digital platform that helps banks, credit unions, and financial institutions manage the **entire lifecycle** of personal loans—automating tasks like loan applications, underwriting, decisioning, documentation, compliance, and servicing… features such as credit checks, loan origination workflows, document management, and borrower portals… integrate with core banking systems, credit bureaus, and third-party fintech tools." — the market's own umbrella definition is lifecycle-wide even though this specific product is origination-scoped.

## Product D — HES FinTech (LoanBox)

### Key observations (Layer A unless noted)

- Positioning: "core lending software"; "One loan management software for the entire lending cycle": **Digital onboarding → Loan origination → Loan servicing → Debt collection**; sibling AI products GiniMachine (decisioning) and CollectionAgent (collections) usable standalone or embedded.
- Digital onboarding: white-label lending portal; application forms that "flex by product line and region"; KYC/KYB checks at approval stage; data stored for returning borrowers.
- Loan origination: underwriting logic the credit team changes without a developer ("set cut-off thresholds, scorecards, and underwriting rules yourself"); credit bureau and alternative data feeds; no-code builder.
- Loan servicing: "recalculate amortization schedules yourself when terms change"; "run disbursement, accruals, partial payments, and write-offs on every product"; "post payments on ACH, SEPA, cards, and mobile wallets."
- Debt collection: score overdue accounts live, rank by likelihood of recovery; route simple cases to automated outreach, complex files to agents or partner agency; contact/channel/fee limits configurable.
- Product catalog for individuals: personal/consumer, auto, BNPL, microfinance, P2P, student, healthcare, POS, mortgage (mortgage listed under a separate page — edge overlap noted).
- Category FAQ (vendor's own distinction): "Lending software is a broader term that may include origination, decisioning, servicing, collections, and analytics. A loan management system (LMS) specifically focuses on the **servicing stage**, including tracking balances, payments, schedules, fees, interest calculations, documents, and borrower interactions. On many modern platforms, both components are combined into a single end-to-end lending solution."
- Deployment: cloud / on-premise / hybrid; optional code license ("eliminates vendor lock-in"); compliance: embedded KYC, AML monitoring, audit logs; integrations: credit bureaus, open banking, core systems, payment gateways, CRMs, identity tools.

## Cross-product Comparison

| Structure / capability | LoanPro | TurnKey Lender | MeridianLink Consumer | HES LoanBox | Layer |
|---|---|---|---|---|---|
| Consumer borrower record (individual credit subject) | ✔ (customer data; portal) | ✔ (borrower evaluation; returning-borrower data) | ✔ (applicant/borrower) | ✔ (onboarding, KYC, returning borrowers) | A→B |
| Configured credit product (amount/term/rate/fee/schedule rules) | ✔ (credit programs; templates; "2,000 programs" claim) | ✔ (credit product builder: schedules/fees/taxes/interest/rules) | ✔ (loan types; configurable workflows/forms/decisioning criteria) | ✔ (configurable products; no-code underwriting logic) | A→B |
| Application intake incl. digital self-service | ✔ (personalized application) | ✔ (apply online) | ✔ (online + in-branch channels; mobile-first) | ✔ (white-label portal, regional forms) | A→B |
| Credit evaluation machinery (data + rules/scorecards/AI + manual) | ✔ (decision engine integration; 100+ data providers claim) | ✔ (AI scoring + decision rules + staff approval) | ✔ (rules, visual logic trees, real-time data) | ✔ (scorecards, thresholds, bureau/alt data, AI engine) | A→B |
| Decision & offer (approve/decline/counter; offer management) | ✔ (offer generation stage) | ✔ (loan offer management) | ✔ (instant approvals; cross-sell offers) | ✔ (cut-off thresholds; auto decisions) | A→B |
| Documents & disclosures generation at origination | ✔ (contracts, closing docs, disclosures) | ✔ (loan agreement generation) | ✔ (documentation; audit trails) | ✔ (docs; statements) | A→B |
| Funding / disbursement transition to loan account | ✔ (flexible funding; card issuance; servicing handoff "instant creation of the loan account") | ✔ (funds disbursed) | ✔ (syncs to core for onboarding; funding stage) | ✔ (disbursement in servicing) | A→B |
| Loan account as record: balance, accrual, schedule | ✔ (real-time ledger; recalculation) | ✔ (servicing; statements) | ✘ (out of scope — core handles) | ✔ (amortization, accruals, partial payments, write-offs) | A |
| Payment collection (recurring + methods) | ✔ (AutoPay; ACH/cards/etc.) | ✔ (payments automatically charged) | ✘ | ✔ (ACH/SEPA/cards/wallets) | A→B |
| Delinquency / collections machinery | ✔ (collections queues, hardship programs, collateral/repossession tracking) | ✔ (delinquency buckets, strategies, scripts) | ✘ (separate product) | ✔ (scoring, routing, agency handoff) | A→B |
| Borrower self-service portal | ✔ | ✔ (personal portal) | partial (application journey; cross-sell session) | ✔ (borrower portal) | A→B |
| Servicing agent tools / workflows | ✔ (agent walkthroughs, automation) | ✔ (manual management alongside automation) | ✔ (manual reviews; workflows) | ✔ (back office) | A→B |
| Compliance machinery (disclosures, audit, KYC/AML, access control) | ✔ (Compliance Safeguard, TILA/SCRA/OFAC/ECOA mentions, role-based access) | ✔ (KYC/AML integrations) | ✔ (embedded controls, audit trails, fraud/IDV) | ✔ (KYC/AML monitoring, audit logs) | A→B |
| Integration spine (bureaus, identity, payments, core banking) | ✔ | ✔ (75+ preconfigured) | ✔ (hundreds of partners; core sync) | ✔ | A→B |
| Credit card / revolving programs | ✔ | ✔ | ✔ | ✔ (credit cards & overdraft listed) | A→B |
| Secured lending / collateral tracking | ✔ | ✔ | not observed | ✔ (secured-loans solution) | B |
| Indirect / dealer channel (auto) | ✔ (auto lending industry page) | ✔ (auto financing; dealers named) | ✔ (DecisionLender separate product) | ✔ (auto finance solution) | B |
| P2P lending mode | ✘ | ✔ | ✘ | ✔ | B |
| On-prem / code-license deployment | ✘ (SaaS posture) | ✘ (SaaS posture) | ✘ (cloud) | ✔ | A |

Key comparison findings:

- **All four products carry the same threefold spine**: consumer borrower → application evaluated against a configured product → funded loan account with scheduled repayment. (Layer B)
- **Packaging split confirmed**: MeridianLink Consumer is origination-scoped and hands servicing to the bank core; LoanPro, TurnKey, HES are end-to-end. The market label "consumer lending platform" is used across both poles; the vendors' own category FAQs define consumer lending software as lifecycle-wide. (Layer A/B)
- **Collections machinery is present in every end-to-end product and absent in the origination-pole product** → treat delinquency/collections as standard mature structure of the lifecycle form, not a defining invariant of the Type (an origination-scoped consumer lending product still exists and still markets itself in this category). (Layer B, boundary-relevant)
- **The money math belongs to the platform**: interest accrual, amortization schedule, payment application, recalculation after term changes are repeatedly framed as platform-owned calculations (LoanPro recasting on a real-time ledger; HES "recalculate amortization schedules yourself when terms change"; TurnKey product builder computes schedules/fees; LoanPro FAQ names "payments and interest accrual" as servicing's core). (Layer B)
- Regulated-disclosure machinery appears in all four, with US-specific statutes (TILA/SCRA/ECOA) named only by the US-centric products (LoanPro, MeridianLink) and KYC/AML named by the globally-positioned products (TurnKey, HES) → regulatory regime is a variant dimension, disclosure/audit machinery is common. (Layer A→B)
- AI decisioning is heavily marketed by all four (era-typical); earlier-stage and manual underwriting remain described as modes ("approved automatically or by your staff", "instant decisioning… instant approvals" alongside "manual reviews") → AI is not definitional. (Layer B)

## Canonical Model (working)

```text
Credit Product Configuration
        │ defines
        ▼
Consumer Borrower / Applicant ──► Application
        │                              │ verification + credit evaluation
        │                              ▼
        │                         Decision / Offer
        │                              │ accepted
        │                              ▼
        │                     Documents & e-execution ──► Funding / Disbursement
        │                              │ creates
        ▼                              ▼
     Borrower ◄────────────────  Loan Account (terms, schedule, balance, accrual)
                                       │
                     ┌─────────────────┼──────────────────────┐
                     ▼                 ▼                      ▼
                Servicing loop    Delinquency states      Payoff / Charge-off
        (billing, payments,        (late fees, collections,
         adjustments, statements,   hardship, modification,
         borrower portal)           collateral, agencies)
```

## Abstraction Hierarchy

### L0 — Defining Invariant (minimal)

1. **The consumer borrower as the credit subject** — an identified individual person whose identity, financial profile, and credit standing are recorded and evaluated; the person (not a business, not a merchant) is the unit the platform lends to. Remove → commercial/SME lending platform.
2. **The application-to-decision flow over a configured credit product** — the consumer requests credit under a product whose amount/term/rate/fee/schedule parameters are configured; the platform gathers applicant data (identity, income, credit standing), evaluates against the product's rules (automated and/or human), and records a decision with offer terms. Remove → a servicing ledger / core-banking loan account with no origination machinery.
3. **The loan account of record with scheduled repayment** — an accepted offer becomes a funded loan account the platform keeps as the record of the credit relationship: contractual terms, balance, interest accrual, payment schedule, and the payment history that moves it toward payoff (or default states). Remove → a lead/decision tracker, not a lending platform.

Note on scope: the full mature form of the Type spans origination + servicing on one platform, but the origination-only realization exists (sampled directly) and markets under the same category name. The three invariants above are what every realization shares; origination-scope vs lifecycle-scope is treated as a packaging pole.

### L1 — Common Mature Structure

- credit bureau / alternative data integrations and identity & fraud verification at intake
- automated decisioning (rules, scorecards, AI models) with manual-review queues
- offer generation and borrower-facing application journey (multi-product apply, cross-sell)
- dynamic document generation (agreements, disclosures) with e-execution
- disbursement via payment rails; card/line issuance for revolving products
- recurring billing, autopay, multiple payment methods; payment application against the account
- statements, notices, borrower communications; borrower self-service portal
- delinquency tracking, collections queues/strategies, hardship programs and loan modifications, collateral/repossession tracking where secured, agency handoff
- servicing agent consoles, workflow automation, agent guidance
- product/workflow configuration studios; role-based access; audit trails
- reporting/analytics (origination conversion, portfolio health, delinquency)
- integration spine (core banking, payments, e-signature, communications, data providers)

### L2 — Variant / Optional Structure

- packaging pole: end-to-end platform vs origination-scoped (servicing delegated to a bank core) vs servicing-scoped product sold into the same category
- lender type: banks/credit unions vs non-bank finance companies vs fintechs vs embedded/merchant-financed credit
- product mix: personal/installment, auto (incl. indirect/dealer), POS/BNPL, credit lines & credit cards, payday/micro, P2P, student, medical, non-profit, leasing-adjacent
- secured vs unsecured; collateral machinery depth
- geography/regulatory regime (US TILA-class disclosure regime vs KYC/AML-centric regimes elsewhere; specific statutes are regime facts, not type structure)
- deployment: SaaS vs on-prem vs code license; API-first lending-as-a-service posture vs application suites
- HELOC / real-estate-adjacent products appearing inside consumer platforms (overlaps the mortgage leaves)

### L3 — Vendor-specific (kept out of final document)

- LoanPro: "Modern Lending Core", "Compliance Safeguard", "Smart Verify", real-time ledger recasting branding, "APR Match", payments/partnership branding
- TurnKey Lender: proprietary AI scoring brand, portfolio-performance-based subscription pricing model, "TurnKey Consumer" packaging, IDC/Gartner/Everest badges
- MeridianLink: "MeridianLink One" platform umbrella, "Insight/Insight Lite" analytics, "DecisionLender" indirect product, visual logic trees as decisioning UI
- HES: LoanBox/GiniMachine/CollectionAgent product trio, code-license model, regional landing pages
- Vendor metrics ("600+ lenders", "25M+ active loans", "50 million borrowers", "58 countries") — marketing claims, recorded as claims only.

## Rejected Findings (not promoted to core)

- **AI/proprietary scoring** — all four market it, but all four equally describe human/manual and rule-based modes; a non-AI consumer lender platform is not imaginable as a different type. Not definitional.
- **Collections machinery** — universal in end-to-end samples but absent in the origination-pole sample; standard for the lifecycle form, not an invariant of the Type.
- **Borrower portal** — common to all sampled end-to-end products but the origination-pole product's consumer surface is application-only; portal is common, not defining.
- **Credit cards/revolving as a product class** — widely supported but the installment loan is the primitive; revolving support is a product-mix variant.
- **Specific statutes (TILA, SCRA, ECOA, OFAC)** — named only by US-centric products; regime-dependent, stays variant.
- **Precise integration counts, program counts, processing-time metrics** — vendor marketing figures; excluded.

## Historical / Market-Sample Check

- Pre-digital / core-banking-era consumer lending (credit union loan officer with paper applications, manual committee approval, passbook-style loan accounts with coupon-book payments, ledger delinquency tracking) satisfies all three L0 invariants: consumer borrower, application→decision, loan account with scheduled repayment. Digital intake, instant decisioning, autopay, and portals are modern implementations, not requirements.
- Regional microfinance/payday products (fee-based, short-term, small principal) and Islamic-finance-structured products (fee/lease realizations) fit the same spine; both are explicitly served by sampled platforms.
- Conclusion: L0 abstracts above era, region, and platform. Passed.

## Boundary Findings

- **vs Loan Origination System (LOS)**: the LOS leaf is stage-scoped (origination) and segment-agnostic; this leaf is borrower-segment-scoped (consumer) and spans the lifecycle in its mature form. They overlap on the origination stages; an origination-only consumer product (sampled) legitimately sits in both readings. The directory keeps both leaves: LOS names the function, Consumer Lending Platform names the segment-scoped business platform. Boundary held by scope axis, not by capability list.
- **vs Loan Management System (LMS)**: LMS is servicing-scoped; one sampled vendor explicitly distinguishes "lending software" (broader) from "LMS" (servicing stage) while noting the market merges them end-to-end. Same scope-axis resolution as LOS.
- **vs Mortgage Origination/Servicing**: mortgage = real-estate-collateralized consumer credit with distinct machinery (escrow, closing/investor workflows); consumer platform covers non-mortgage consumer credit, though sampled products list HELOC-class products — edge overlap recorded.
- **vs Commercial Loan Origination/Management**: borrower type is the discriminator (individual consumer vs business entity). Sampled platforms serve both segments and split their marketing along this line (TurnKey, HES: separate consumer/commercial solutions; LoanPro: consumer/business/auto industries).
- **vs Credit Decisioning Platform**: decisioning is one stage here; decisioning platforms are standalone evaluation engines without the loan account/servicing record. Remove the loan account and this Type collapses into decisioning.
- **vs Collections Platform / Debt Collection Management**: collections is a stage/module here (and a separate sampled product at the origination pole); dedicated collections systems operate charged-off/post-charge-off treatment as the primary object.
- **vs Digital Banking Application / Online Banking Portal**: those are consumer-facing channel surfaces of a financial institution; this Type is the lender-side operating system. A borrower portal inside this Type serves the loan relationship only.
- **"Remove-what" test**: remove the consumer-borrower constraint → commercial lending; remove application→decision → loan management; remove the loan account → credit decisioning / lead management; remove credit entirely → generic CRM or banking channel.

## Taxonomy note (for STATUS.md Boundary Issues)

Consumer Lending Platform overlaps Loan Origination System and Loan Management System leaves on stages; the resolution used here is scope-axis (segment-scoped lifecycle platform vs stage-scoped function systems). Both sampled poles (origination-scoped product marketing as a "consumer lending software" product; vendors' own lifecycle-wide category FAQs) are documented. Worth a directory-maintainer glance at whether LOS/LMS leaves should carry a "see also segment platforms" cross-reference.

## Uncertainties

- Servicing depth at the origination pole: MeridianLink's servicing involvement beyond core sync was not verifiable from public pages (client-facing docs gated). Servicing-inclusive claims for that product are avoided.
- Regional deployment details for TurnKey Lender (documents describe capabilities globally; no jurisdiction-specific claims taken).
- Payment-rail specifics (exact methods, settlement timing) — vendor marketing-level only; not asserted.
- The extent to which standalone consumer-servicing-only products (no origination) market themselves under the "consumer lending platform" label was not directly sampled; the HES category FAQ implies servicing-stage products exist as a labeled subset.
- Deep API/help-center documentation for all four products was not fetched; operational micro-details (state names, exact waterfall order, default fees) intentionally absent.

## Final Synthesis

A Consumer Lending Platform is the lender-side system of record for credit to individual consumers. Its defining core is three structures — the consumer borrower as credit subject, the application-to-decision flow over a configured credit product, and the loan account of record with scheduled repayment — carried from application through decision, documents, and funding into servicing (payments, accrual, adjustments, communications) and, in the mature lifecycle form, through delinquency and collections to payoff or charge-off. The market realizes it as end-to-end platforms and as origination-scoped or servicing-scoped poles under the same category name; AI decisioning, portals, bureau integrations, disclosure machinery, and collections modules are standard mature capabilities rather than definitional structure; borrower segment, product mix, regulatory regime, and packaging are variant dimensions.
