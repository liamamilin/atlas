# Research Notes — Commercial Loan Management

Research date: 2026-09-07
Methodology: update-v1 (WORKFLOW_v1.1 / WRITING_GUIDE_v1.1)

---

## Research Goal

Understand what lender-side software for managing commercial (business) loans actually is and how it works — specifically the post-funding management of the commercial loan book: what objects exist, what the recurring servicing loop does, how loans change over their life, who operates it, and where its boundary runs against loan origination, generic loan management, mortgage servicing, core banking, and the commercial banking platform.

Prior-pass context: the commercial-banking-platform pass drew the seam "the platform surfaces the relationship; it does not run the loan book" and flagged commercial-loan-origination + commercial-loan-management for joint review. This pass is the discharge opportunity on the management side.

---

## Initial Boundary (hypothesis before research)

- Hypothesis: a Commercial Loan Management application is the lender's servicing system of record for commercial credit — loan/commitment accounts, payment application, interest accrual, fees, collateral, covenants, modifications/renewals/payoffs — with commercial-specific structures (facilities, lines, participations, syndications) that consumer loan servicing lacks.
- Nearest neighbors: Commercial Loan Origination (upstream), Loan Management System (generic sector-neutral leaf), Mortgage Servicing Platform (residential), Collections/Debt Collection (downstream), Core Banking System (GL), Commercial Banking Platform (relationship-facing surface), Credit Risk / Portfolio Analytics platforms (monitoring).
- Unknowns going in: (a) where origination ends and management begins in modern cloud suites; (b) whether syndication/agency machinery is common or a variant; (c) whether a borrower-facing portal is part of the Type or a sibling Type; (d) how much of the market sells one servicing engine spanning consumer + commercial.

## Research Questions

1. What are the core objects of a commercial loan servicing system? (loan, commitment, line/facility, draw, participation…)
2. What does the recurring servicing loop actually do — payments, accrual, fees, balances?
3. How do loans change over their life (draws, rollovers, rate changes, modifications, non-accrual, payoff)?
4. What commercial-specific structures appear (commitments, lines of credit, participations, syndications, covenants, collateral)?
5. Who operates the system, and in what kind of institution (bank, credit union, nonbank, third-party servicer, private credit)?
6. What interfaces exist — internal maintenance screens, queues, reporting, portals?
7. What rules and states matter (non-accrual, credentials/authority, audit, regulatory reporting)?
8. Where is the origination/management seam, and does any sampled product span both without being the servicing ledger?
9. Is there a generic "loan management" type underneath, with consumer/commercial as segment realizations?

---

## Representative Products

Selection rationale: market representativeness (syndicated-lending standard + long-heritage servicing specialist + modern cloud suite), different product philosophies (servicing-ledger-first vs origination-led platform), different customer tiers (global/corporate banks vs mid-market US banks and nonbanks vs cloud-era institutions of all sizes).

1. **Finastra Loan IQ** — the dominant commercial/syndicated loan servicing platform; servicing-ledger-first pole. Sampled with its ecosystem pages (Loan Portal, Simplified Servicing, Specialized Credit, ESG Service, Lending Cloud Service) because they document the boundary surfaces around the core.
2. **Shaw Systems Associates (Spectrum; Commercial Loan Management)** — dedicated long-heritage (company claims 55+ years) loan management/collections vendor serving US banks and nonbank lenders; mid-market pole; its "Commercial" page is literally titled Commercial Loan Management Software, making it a direct leaf anchor.
3. **nCino** — modern cloud "Commercial Loan Origination System" with portfolio monitoring; origination-led pole. Sampled deliberately to test the origination/management seam: it documents monitoring/covenants but not the servicing ledger, which is boundary evidence rather than core evidence.

A fourth pole (core-banking-vendor commercial lending module: Fiserv/FIS/Jack Henry/Temenos) was attempted; product pages were not reachable at guessed URLs and were abandoned per the network-retry rule. The sample stands at three vendor families; core-vendor-module realizations are noted as unverified.

---

## Sources

All fetched 2026-09-07. All are official vendor product/marketing pages (Tier 2). No Tier-1 operational documentation (logged-in help centers, user guides, training academies) was reachable in this pass; the only attempted help-center-class source was the Loan IQ brochure page, which resolved to a stub.

- Finastra Loan IQ product page — https://www.finastra.com/lending/solutions/loan-iq (page title: "Loan IQ | Commercial Loan Management Software | Finastra")
- Finastra Loan IQ Solution Overview brochure page — https://www.finastra.com/viewpoints/brochure/loan-iq-solution-overview (stub: title + positioning only)
- Finastra Loan IQ infographic page — https://www.finastra.com/viewpoints/infographic/loan-iq-premier-commercial-loan-servicing-platform
- Finastra Loan Portal product page — https://www.finastra.com/lending/solutions/loan-portal
- Finastra root navigation (solution taxonomy) — https://www.finastra.com/
- Shaw Systems Commercial Loan Management page — https://www.shawsystems.com/commercial-loan-management/
- Shaw Systems Loan Management page — https://www.shawsystems.com/loan-management-software/
- Shaw Systems Business Lending page — https://www.shawsystems.com/portfolio/business-lending/
- Shaw Systems root — https://www.shawsystems.com/
- nCino Commercial Lending page — https://www.ncino.com/solutions/commercial-lending
- nCino Credit Portfolio Management page — https://www.ncino.com/solutions/credit-portfolio-management
- nCino root — https://www.ncino.com/

**Source-access limitation**: every claim below rests on official product pages (positioning, feature lists, FAQ text). Operational precision — posting order rules, accrual conventions, numeric limits, default schedules, state-machine details — is not observable from these pages and is deliberately not asserted. Assertion strength is calibrated accordingly throughout. No memory-filled operational detail was substituted.

Unfetched/failed (recorded per network-retry rule, max 1–2 attempts each):
- finastra.com/us/products/loan-iq, /products/fusion-loan-iq, /us/en/products/loan-iq, /us/products → 404 (site restructure; correct path found via root)
- ncino.com/products/portfolio-management → 404 (correct path found via root)
- temenos.com/products/lending/, fiserv.com/en/financial-solutions/lending.html, q2.com/products/cloud-lending, fisglobal commercial lending guesses → 404; abandoned
- Bank help centers / user guides for Loan IQ, Shaw Spectrum, nCino → not attempted beyond the brochure stub (login-walled class of source; consistent with prior finance passes)

---

## Product A — Finastra Loan IQ (+ Loan Portal ecosystem)

Vendor self-positioning: "the market's leading loan servicing platform that can support the full spectrum of lending on a modern, unified platform"; page title literally "Commercial Loan Management Software"; brochure title "the market's preeminent and most trusted commercial and syndicated lending solution". IDC MarketScape 2025 category: "Worldwide Corporate Loan Lifecycle Management" (Leader).

### Key observations (evidence layer A unless noted)

- **Positioning is servicing-first**: "automate loan servicing… manage your entire lending portfolio centrally"; "loan servicing platform". Used by "banks, 3rd-party asset servicers and private credit lenders" (FAQ). Deployment: on-premise or container-based cloud; hosting via Lending Cloud Service.
- **Market-shape claims (vendor-published, layer B-adjacent)**: "21 of the top 25 syndicated lenders are Loan IQ clients"; "70% of the world's syndicated loans are serviced via Loan IQ"; "$3.8T in loans syndicated on Loan IQ in 2024". These are vendor claims — recorded, not promoted into the final document.
- **Spectrum of credit handled**: "from SME and bilateral to complex syndicated, as well as specialty loans like CRE, SBA, and export finance — all on one centralized platform"; "consolidate your entire commercial lending portfolio, from high-volume bilateral loans to complex syndications".
- **Specialized credit**: PIK (Payment-in-Kind) module, club deals, non-pro rata, unitranche functionality (FAQ + separate PIK brochure); ESG/sustainability-linked lending via a separate ESG Service.
- **Structural vocabulary in evidence**: deals, commitments, facilities, drawdowns, rollovers, loan increases, repayments, interest, repayment schedules, facility limits, entity associations, compliance documents (Loan Portal page describing real-time Loan IQ data).
- **Finastra Loan Portal** (separate product, explicitly "seamlessly integrated with Loan IQ, built on Corporate Channels"): borrower-side self-service — personalized dashboards by role; real-time loan data on "deals, commitments, repayments"; initiate drawdowns and multiple rollovers with automated validations, flexible remittance instructions, interest netting; request loan increases; make payments incl. pre-payments and fees "through automated, auditable workflows"; facility/loan inquiries (interest, repayment schedules, loan history, facility limits); loan maintenance (compliance documents, entity associations, billing inquiries) with "tracking of submitted instructions"; secure communication and document upload; channels: browser, mobile, chatbot, open APIs, file services, ERP integration. → Boundary evidence: the borrower portal is a sibling product reading the servicing engine's data, not part of the engine.
- **Loan IQ Simplified Servicing** (separate edition/module): "modern, browser-based UI and optimized workflows to high-volume SME and bilateral lending operations" — evidence that the classic engine's UI needed a lighter realization for simpler books.
- **Loan IQ Nexus**: "modern integration layer… connect to any upstream/downstream" — integration seam is a first-class concern.
- **Benefits claims (marketing, not asserted)**: 20% reduction in booking times; 50% integration-cost reduction; doubled business without headcount; "increased automation and built-in controls reduce errors and manual intervention".

### Interpretation

Loan IQ documents the maximal servicing realization: the loan book as the central ledger (booking/deal setup, servicing, syndication shares, specialized credit structures), with origination ("deal setup"/onboarding) present but lightweight, and borrower interaction externalized to a sibling portal product. The objects visible at the edges (deals, commitments, facilities, drawdowns, rollovers, repayments, facility limits, interest, schedules, compliance documents, entity associations) triangulate the engine's internal model.

---

## Product B — Shaw Systems (Spectrum; Commercial Loan Management)

Vendor self-positioning: "The only Loan & Lease Management System with embedded AI"; "servicing, collections, loans, lines of credit, and leases"; "over five decades of experience developing loan management and collections software" (company claim — heritage evidence for the Type's age). Suite structure: Loan Management, Collections, Recovery, Leasing, Dealer Floor Plan as separate solution lines — servicing and collections are different modules, supporting the boundary with collections.

### Key observations (evidence layer A unless noted)

Commercial Loan Management page (the direct leaf anchor):

- **Object set**: "Commitments — handle multiple draws, subsidiaries, sold participations"; "Lines of Credit — revolving and non-revolving"; "Loans — construction, REO, ARMS loans, all with flexible fees, billing, and rate structures"; "SBA — automatic tracking and reporting, SBA and PPP loans"; "Participations — full functionality for processing loans sold to investors, including automatic distribution of funds"; "Collateral Tracking — cross-collateralization and automatic pricing updates"; "Shadow Loans — full non-accrual tracking and accounting"; "Multiple Pricing Options — variety of interest rate options, fixed to variable tiered rates".
- **Relationship view**: "Customer-Centric View — complete view of customer's relationship with the bank, co-maker, co-signer, guarantor".
- **Portfolio management**: "manage commitments, participations, fees, and SBA loans… expenses, billing, securitizations, asset-based lending, and regulatory needs"; reporting: "Utilize, copy, or edit Shaw provided reports to automatically provide to necessary investors".
- **Operations**: "Users with the right credentials can make loan changes and handle exceptions in commercial lending"; "web services, real-time data, encryption, and queuing".
- **Servicing life cycle** (repeated on Loan Management page): "communications, accounting, customer service, delinquency management, recovery, and placement".

Loan Management page (the engine underneath, sector-neutral):

- **Payment processing**: "comprehensive, scheduled, and on-demand integrated payment tools".
- **360 view**: "customer-centric account management and automated communication campaigns".
- **Securitization management**: "manage, track, and report on sophisticated securitization structures".
- **Pop-up alerts**: "real-time alerts inform staff of account conditions and reinforce policy and compliance requirements".
- **Custom screens**: "each agent work group can control their preference for borrower and account data views".
- **Risk & compliance**: "configuration to guide the loan life cycle path".
- **Automated workflow**; API-first architecture; securitization reporting; "help borrowers change their due dates" (a servicing action example).

Business Lending page: products supported = installment loans, leases, lines of credit, custom loans; same platform claims (API-first, configurable, scalable).

### Interpretation

Shaw documents the servicing ledger at mid-market scale and makes the object model unusually explicit: the account population is commitments (with draws and subsidiaries), lines of credit (revolving/non-revolving), loans (with construction/REO/ARM realizations), SBA loans; the commercial mechanisms are participations (sold shares with automatic fund distribution), cross-collateralization, non-accrual accounting (shadow loans), securitizations; the loop is payment processing (scheduled + on-demand), fee/billing handling, accounting; the life management is credential-gated loan changes and exception handling. Delinquency/recovery exist but as sibling modules.

---

## Product C — nCino (Commercial Lending / Credit Portfolio Management)

Vendor self-positioning: "Commercial Loan Origination System" (CLOS); "Boost revenue, manage risk… through efficient, streamlined processes". Agentic-AI marketing layer ("Digital Partners", "Banking Advisor", "Continuous Credit Monitoring") — vendor-specific, recorded only.

### Key observations (evidence layer A unless noted)

- **The suite's center of gravity is pre-funding and monitoring, not the servicing ledger**: onboarding workflows, pre-qualifications, credit approvals from policy rules, auto-approve/decline/manual-review parameters, credit analysis/spreading (financials extraction), pricing & profitability, CRE analysis. **No payment application, accrual, or servicing-accounting capability is documented anywhere on the fetched pages.**
- **Deal Management** (within CLOS): "access and manage the overall deals of your clients' loan and treasury products in real time"; "complete view of the relationship in a single location"; "structuring and management of credit/non-credit deals and products"; "supports creation of sub-loans, information cloning, and bulk editing".
- **Covenant/compliance machinery**: "generates automatic notifications to remind users when a covenant is approaching its due date and serves as a record of compliance for auditing purposes"; integrated document repository with "visual audit trail"; loan reports "for regulators and auditors".
- **Credit Portfolio Management page**: "manage commercial and small business loans from origination to monitoring"; proactive monitoring, intelligent alerts, "detect credit deterioration earlier", "holistic view of relationship credit health".
- **Real-time reporting "for better portfolio management"** (origination page).

### Interpretation

nCino is the boundary pole. It demonstrates that a modern "commercial lending platform" can own the front/middle office (origination pipeline, relationship/deal view, covenant tracking, credit monitoring) while the servicing ledger (payments, accrual, balances) remains elsewhere. For the Type definition this is disambiguating evidence: origination pipeline = Commercial Loan Origination; servicing ledger + loan-book life management = Commercial Loan Management; monitoring/analytics layered over the book is adjacent (some overlap with covenant tracking). nCino contributes the relationship/deal view and covenant machinery as cross-product commonalities (relationship view also in Shaw and Loan Portal; covenant/compliance documents also in Loan Portal), but it does NOT support the servicing-loop claims.

---

## Cross-product Comparison

| Dimension | Finastra Loan IQ | Shaw Systems (Spectrum/Commercial) | nCino (CLOS/CPM) |
|---|---|---|---|
| Center of gravity | servicing ledger, syndication-heavy | servicing ledger, mid-market | origination + monitoring (no servicing ledger documented) |
| Core account objects | deals, commitments, facilities, drawdowns, rollovers, repayments | commitments w/ draws, lines of credit (revolving/non-revolving), loans, SBA loans | deals, sub-loans (pre-funding); no funded-account ledger documented |
| Terms as computable data | interest, repayment schedules, facility limits | flexible fees, billing, rate structures; fixed→variable tiered rates | policy rules (credit decisions) |
| Servicing loop (payments/accrual) | implied via repayments/pre-payments/fees/interest netting (portal actions write into Loan IQ) | explicit: scheduled + on-demand payment tools, accounting in servicing lifecycle, non-accrual accounting | absent |
| Commercial-credit structures | syndications, participations, club deals, unitranche, PIK, non-pro rata | participations (auto fund distribution), multiple draws/subsidiaries, securitizations, cross-collateralization, asset-based lending | credit/non-credit deal structuring (pre-funding) |
| Relationship view | Loan Portal: entity associations, relationship data; CLOS-style deal view implied | customer-centric view incl. co-maker/co-signer/guarantor | "complete view of the relationship" (Deal Management) |
| Covenant/compliance tracking | compliance documents; ESG service for sustainability-linked loans | compliance configuration guiding the loan life cycle; regulatory needs | covenant due-date notifications; compliance record; audit trail |
| Delinquency handling | not surfaced on fetched pages | delinquency management in servicing lifecycle; collections as sibling module | "detect credit deterioration earlier" (monitoring layer) |
| Investor/3rd-party reporting | syndication machinery; third-party asset servicers as users | investor reports (utilize/copy/edit, auto-provision); securitization reporting | loan reports for regulators/auditors |
| Borrower-facing surface | Loan Portal = separate sibling product | none documented (Amplify "borrower action" tool exists in suite marketing) | none (experience claims only) |
| Collateral | not surfaced on fetched pages | collateral tracking, cross-collateralization | not on fetched pages |
| Deployment | on-prem or container cloud; hosting service | "API-first" modern platform claims; heritage mainframe-era vendor | cloud SaaS |
| Operators | banks, 3rd-party asset servicers, private credit lenders | US banks + nonbank lenders (auto/business/consumer industries) | banks/CUs of all sizes (marketing) |

Reading: the servicing ledger + life management claims are supported by Loan IQ and Shaw (two servicing-led products, independent vendors). The relationship/deal view and covenant/compliance tracking are supported by all three (in different layers). Syndication/participation machinery is strong in Loan IQ and Shaw (participations) — common but depth varies; monitoring/analytics depth is nCino's contribution. Payment application + accrual + accounting is the deepest common structure of the two servicing-led products, and is exactly what the origination-led product lacks — the strongest boundary signal in the sample.

---

## Canonical Model (abstraction levels)

### L0 — Defining Invariant

A Commercial Loan Management application is the lender-operated system of record for the funded commercial loan book. Smallest structure without which the Type stops being recognizable:

```text
Borrower (business/organization) — identified commercial credit customer
└── Commercial credit position (loan / commitment / line of credit held by the lender)
    └── Contractual terms held as computable data
        (schedule, rate basis, fees — the record from which the system computes)
        └── Servicing loop
            (payment application — scheduled and event-driven;
             interest accrual and fee/charge handling;
             balance and status update on the account)
            └── Life-of-loan management
                (lender-side actions that change the position — draws/advances,
                 rollovers, increases, modifications, non-accrual status, payoff —
                 executed and recorded in the system)
```

Five properties:

1. **Identified commercial borrower** — the account population is business credit, not consumer credit.
2. **The commercial credit position as the managed record** — a funded loan, a commitment, or a line of credit persists as an account the lender operates on. Commercial positions are facility-shaped (commitments with available capacity, lines with draw/repay cycles), which is what distinguishes the population from amortizing consumer loans.
3. **Terms as computable data** — the contract (schedule, rate, fees) is held as data the system computes from, not as a document reference alone.
4. **The recurring servicing loop** — money-in and charges are applied to the account per the recorded terms; balances, accruals, and status are maintained by the system. Without this the product is a pipeline or a monitoring dashboard, not loan management.
5. **Life-of-loan management as system-executed actions** — changes to the position (draws, rollovers, rate/term modifications, status changes such as non-accrual, payoff) are made through and recorded by the system as the book's system of record.

L0 is deliberately era-neutral: a mainframe-era loan master file with payment posting, accrual runs, commitment records, and participation ledgers satisfies it without any modern artifact (cloud, portals, workflow GUIs, AI).

### L1 — Common Mature Structure

Present across the sample (two or more products) but not definitional:

- **Borrower/customer relationship view** — account aggregation across a customer's positions, including related parties (co-maker, co-signer, guarantor — Shaw; entity associations — Finastra; relationship deal view — nCino).
- **Collateral tracking** — with cross-collateralization (Shaw; absent from the other two fetched pages but a standard commercial-lending mechanism).
- **Fee/charge and billing machinery** — flexible fee and billing structures (Shaw; fee payments — Finastra).
- **Participation/investor handling** — participations sold to investors with automatic fund distribution (Shaw); syndicated/agent lending as the deep realization (Loan IQ).
- **Investor/regulatory reporting** — investor report distribution (Shaw); regulator/auditor reports (nCino); the syndication reporting complex (Loan IQ).
- **Workflow automation, alerts, queues** — automated workflow, smart queuing, pop-up alerts (Shaw); automated workflows, alerting (nCino); built-in controls (Loan IQ marketing).
- **Credential-gated maintenance and exception handling** — "users with the right credentials can make loan changes and handle exceptions" (Shaw); auditable workflows (Finastra portal actions); audit trail (nCino).
- **Covenant/compliance-document tracking** — covenant due-date notifications and compliance records (nCino); compliance documents (Finastra portal); compliance configuration over the life cycle (Shaw).
- **Integration spine** — APIs/web services, GL/accounting connectivity, upstream/downstream integration layers (Shaw API-first; Loan IQ Nexus; nCino Integration Gateway).
- **Delinquency progression** — tracked status and handoff to collections/recovery (Shaw servicing lifecycle lists delinquency management; collections is a sibling module).

### L2 — Variant / Optional Structure

Depends on segment, geography, product family, era:

- **Syndicated/agency depth** — agent-bank servicing, club deals, non-pro rata, unitranche, PIK (Loan IQ pole; absent from mid-market pages).
- **Securitization management** (Shaw).
- **Government-guaranteed programs** — SBA/PPP tracking and reporting (Shaw; US-regional).
- **Construction/RE lending realizations** — construction loans, REO, draws (Shaw; CRE as a specialty — Loan IQ).
- **Asset-based lending** (Shaw).
- **Borrower self-service portal** — externalized as a sibling product in the strongest servicing ecosystem (Finastra Loan Portal); not present as part of the engine in other products.
- **Third-party servicing posture** — asset servicers and private credit lenders operating the servicing engine for originated books (Loan IQ FAQ).
- **ESG/sustainability-linked lending support** (Finastra ESG Service).
- **AI assistance** — embedded AI for servicing/collections propensity (Shaw Amplify), agentic AI across banking roles (nCino Digital Partners), AI training/assist (Finastra Academy.AI/Assist.AI) — current-era marketing layer.
- **Deployment posture** — on-premise vs container/cloud vs vendor-hosted (Loan IQ FAQ documents both poles in one product).

### L3 — Vendor-specific (research notes only)

- Loan IQ: PIK module as a packaged brochure; Nexus integration-layer branding; Simplified Servicing edition; Lending Cloud Service; ESG Service; market-share claims (21/25, 70%, $3.8T/2024); ING customer story ("95% of the portfolio on Loan IQ").
- Shaw: Spectrum platform name; Spectrum Xpress rapid go-live; Amplify/AI Advisor/Insight AI line; "only LMS with embedded AI" claim; 55+ years claim; custom screens per workgroup; specific industries page structure.
- nCino: Digital Partners (Executive/Analyst/Service/Processor/Client agents), Banking Advisor, Continuous Credit Monitoring, Automated Spreading, nIQ, "2,700+ customers", "$3.3T processed in 12 months", "60–70% faster relationship reviews" claims, Integration Gateway.
- Cross-cutting marketing numbers are vendor claims and are excluded from the final document except as attributed market context where useful.

---

## Vendor-specific Findings

See L3. The structurally informative ones:

1. **The servicing ecosystem splits into sibling products around one engine**: Finastra ships Loan Portal (borrower self-service reading Loan IQ data) and Nexus (integration layer) as separate products — evidence that the borrower-facing surface and the integration spine are not part of the servicing engine itself in the strongest-servicing vendor's own packaging.
2. **A servicing-ledger vendor sells collections/recovery as separate solution lines** (Shaw) — supporting the loan-management/collections boundary.
3. **An origination-led cloud suite can reach "portfolio management" without a servicing ledger** (nCino) — evidence that the market's "commercial lending platform" label spans two different system types, and that "portfolio monitoring" ≠ servicing.
4. **One product can document both deployment poles** (Loan IQ: on-prem and container cloud) — deployment is a variant, not a definer.
5. **Edition ladder within one engine** (Loan IQ Simplified Servicing for SME/bilateral vs classic Loan IQ for complex syndications) — the complexity axis (bilateral ↔ syndicated) is handled inside one vendor as product editions, i.e., it is a variant axis, not two Types.

---

## Boundary Findings

| Neighboring Type | Seam | Test ("remove what → becomes the other Type") |
|---|---|---|
| Commercial Loan Origination | funding seam: pre-funding pipeline (application, credit decisioning, documentation, closing) vs post-funding servicing of the funded book. nCino is the origination pole; Loan IQ/Shaw are the servicing pole. Handoff at booking/funding | strip the servicing loop + funded-account ledger → origination; strip the pipeline → loan management |
| Loan Management System (§08 generic leaf) | sector seam inside one servicing family: many products sell one engine spanning consumer + commercial (Shaw explicitly spans both; its commercial capability is a solution line over one Spectrum platform). Adopted working distinction: the commercial leaf's population is facility-shaped business credit (commitments/lines/participations) under negotiated terms | narrow the account population to amortizing consumer credit and drop facility machinery → consumer/generic loan servicing |
| Mortgage Servicing Platform | product-family seam: residential-mortgage machinery (escrow analysis, investor/GSE reporting, foreclosure timelines) vs commercial facility machinery (commitments, lines, participations, covenants, construction draws). Distinct market product families (Loan IQ/Spectrum vs Black Knight-class MSP) | replace facility structures with amortizing residential collateral machinery → mortgage servicing |
| Commercial Banking Platform (processed) | operator/surface seam discharged on this side: the banking platform surfaces held credit as accounts (balances, e-statements, paydowns) to the organization client; the loan management system runs the book on the bank-staff side (booking, servicing, accrual, modifications). Confirmed: Loan IQ/Shaw are bank-staff systems; Loan Portal is the only borrower surface, and Finastra ships it separately | move the operator from bank staff to the client organization's users and drop the servicing ledger → commercial banking platform / borrower-portal surface |
| Collections / Debt Collection Management | lifecycle seam: arrears pursuit vs whole-book servicing. Shaw ships them as separate solution lines; servicing tracks delinquency status and hands off | remove the performing book and keep pursuit of defaulted balances → collections |
| Credit Risk / Portfolio Analytics platforms | layer seam: monitoring/analytics over the book vs the transactional servicing ledger. nCino's monitoring + portfolio analytics sit adjacent; covenant tracking is the overlapping capability that belongs to loan management's record | remove the servicing ledger and keep risk analytics → credit risk platform |
| Core Banking System | substrate seam: the servicing engine may be a module of the core or a standalone specialist feeding it (Loan IQ Nexus "upstream/downstream"; Shaw "works well with other systems"); the GL is accounting, not the loan book | strip the loan-domain servicing model, keep GL/deposit operations → core banking |
| Banking Back-office Platform (processed) | side seam: bank-staff execution of payments/securities vs bank-staff servicing of the credit book (different domain records) | widen to all payment/instrument operations and drop the loan-book model → back-office platform |
| Loan Origination System (generic §08 leaf) + Consumer Lending Platform (§08) | same funding seam as above, sector-generic variants; joint review recommended when those leaves are processed | — |
| Deal Management for Private Equity / VC; Fund Administration (§08) | entity seam: the managed position is a fund/PE investment, not a lender's loan book | swap the credit-position record for fund/ownership records → fund admin |

**Joint-review flags to record in STATUS.md**:

1. Loan Management System (generic) vs Commercial Loan Management vs Consumer Lending Platform — one servicing family, sector-split in the directory; recommend joint review; adopted working distinction: facility-shaped business credit population.
2. Commercial Loan Origination ↔ Commercial Loan Management — funding handoff; modern cloud suites blur the packaging (origination-led suites market "lifecycle" language: nCino "from origination to monitoring", IDC's own category is "Corporate Loan Lifecycle Management"); recommend joint review when the origination leaf is processed.
3. Discharge (partial) of the commercial-banking-platform pass flag: this pass confirms the loan lifecycle is owned by loan-lifecycle systems; the banking platform only surfaces/services held credit from the client side.

---

## Historical / Market-Sample Check

- **Generational evidence**: Shaw claims five decades of loan management software (mainframe-era heritage); its object vocabulary (commitments, participations, non-accrual, shadow accounting) is the vocabulary of ledger-era servicing. Loan IQ's syndication heritage predates the modern web. A mainframe-era commercial loan system — loan master file, payment posting, interest accrual runs, commitment and participation records, paid-off/closed statuses — satisfies L0 without cloud, portals, workflow GUIs, AI, or monitoring dashboards. Pre-software practice (loan ledger + payment register + commitment book maintained by loan clerks) satisfies the conceptual core; the software digitizes and automates the loop.
- **Regional check**: SBA/PPP machinery is US-regional (Shaw); syndicated/agency lending is international (Loan IQ; ING case); nothing in L0 requires a specific jurisdiction, guarantee program, or accounting regime.
- **Sector check**: the facility/commitment population (not "phone number"-style surface artifacts) is what makes the leaf commercial; consumer amortizing loans still fit the generic servicing loop but not the commercial leaf's account population.
- **Credit-in-core test analog**: borrower portals, AI, and monitoring are modern; none enter the definition. Historical check passes.

---

## Uncertainties

- **No Tier-1 operational documentation was reachable** (help centers, user guides). The servicing loop is asserted at the structural level (payment application, accrual, fee handling, status maintenance) with two servicing-led products behind it; precise posting order, accrual conventions (actual/360 vs 30/360 etc.), grace periods, and state-machine names are NOT asserted and were not observed.
- **Core-banking-embedded realizations** (Fiserv/FIS/Jack Henry/Temenos commercial lending modules) unverified — product pages unreachable; the packaging pole "commercial loan servicing as a core-banking module" is assumed from market structure, not from fetched evidence.
- **Depth of collateral machinery beyond Shaw** unknown (not surfaced on Loan IQ's fetched pages — likely exists inbrochures, not verified).
- **Whether consumer-grade features** (borrower statements, billing paper) are common in the engine — partially evidenced via Loan Portal inquiries; left unasserted.
- **The generic-vs-commercial split** (Loan Management System leaf) is a taxonomy judgment recorded for joint review, not settled here.
- nCino's absence of servicing-ledger documentation is evidence of positioning, not proof of total absence (a logged-in instance might integrate or wrap servicing); worded accordingly.

---

## Final Synthesis

A Commercial Loan Management application is the lender-side system of record for the funded commercial loan book. Its defining core: an identified business borrower's commercial credit positions — loans, commitments, lines of credit — held as accounts; the contractual terms (schedule, rate basis, fees) held as data the system computes from; the recurring servicing loop that applies scheduled and event-driven payments, computes interest accrual and charges, and maintains balances and status; and lender-side life-of-loan management — draws, rollovers, increases, modifications, non-accrual status, payoff — executed through the system. Around this core, mature products add the machinery the commercial book is operated with: relationship views across a customer's positions and related parties, collateral tracking with cross-collateralization, participation/investor handling with automatic fund distribution, investor and regulatory reporting, covenant and compliance-document tracking, workflow automation with credential-gated maintenance and exception queues, delinquency progression, and an integration spine to GL, origination, and banking systems. The market realizes the Type along a complexity axis (high-volume bilateral/SME books ↔ complex syndicated/agency books with PIK/club/unitranche structures), a segment axis (mid-market specialist engines ↔ syndicated-lending standards ↔ core-banking modules — the latter unverified), and an era axis (on-premise ledgers ↔ container/cloud deployment). The boundary that matters most: the origination pipeline ends at funding; this Type takes over the funded book. Borrower-facing self-service, where it exists, is a sibling surface fed by the engine. Monitoring/analytics layers observe the book; collections takes over defaulted positions. The Type predates all modern artifacts — the servicing ledger is one of the oldest jobs in banking software — which is what makes the small definition stable.
