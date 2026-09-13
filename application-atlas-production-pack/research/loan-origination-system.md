# Research Notes — Loan Origination System (generic)

Research date: 2026-09-08
Leaf: Loan Origination System (DIRECTORY §08 Finance, Banking, Insurance & Investment)
Slug: loan-origination-system

---

## Research Goal

Define the generic, segment-agnostic Loan Origination System (LOS): what it is, who uses it, what its core structure is, how a credit application moves through it, which rules govern it, and where its boundaries sit against the sibling lending-family leaves already processed (Loan Management System, Commercial Loan Origination, Consumer Lending Platform, Credit Decisioning Platform, Credit Scoring Application, Credit Management Platform) and unprocessed siblings (Mortgage Origination Platform, Mortgage Servicing Platform).

This pass must discharge (from this side) the family flags recorded by prior passes:

1. **loan-management-system pass flag** — funding seam + "LMS" terminology drift; joint review recommended when loan-origination-system is processed.
2. **commercial-loan-origination pass flag** — sector seam inside one origination family; population test recommended when the generic leaf is processed.
3. **consumer-lending-platform pass flag** — scope-axis resolution (segment-scoped lifecycle platform vs stage-scoped function systems); cross-reference recommended when LOS/LMS passes run.
4. **credit-decisioning-platform pass flag** — evaluation engine invoked by the LOS at decision points vs case management through funding; LOS-embedded decisioning modules = variant overlap.

## Initial Boundary (working hypothesis before research)

- Core use: the lender's staff-side system for carrying a credit request from intake through evaluation, decision, and closing to funding — ending in a booking handoff (or a recorded decline).
- Primary users: the lender's own origination staff (processors, underwriters, credit approvers, closing/funding operations); the borrower only at the intake/notification edge.
- Nearest neighbors: Loan Management System (post-funding), Consumer Lending Platform / Commercial Loan Origination / Mortgage Origination Platform (segment-scoped siblings), Credit Decisioning Platform (evaluation-engine layer), Credit Scoring Application (measure vs decision), KYC/IDV and fraud platforms (point checks inside intake).
- Unknowns: whether the generic core can be stated so that consumer, commercial, mortgage, and specialty populations all satisfy it without change (population test); how much of the decisioning layer belongs inside the definition; how packaging (standalone vs end-to-end suite) blurs the funding seam.

## Research Questions

1. What is the unit of work inside an LOS, and how is it identified and tracked?
2. What are the pipeline stages, and who/what moves an application between them?
3. How is evaluation machinery configured (auto vs manual vs hybrid), and what decides which path an application takes?
4. What data is assembled and verified before decision, and what happens when data collection fails?
5. What does a decision look like as a record (outcomes, terms, reasons, actor, audit)?
6. What happens after approval — offer, documents, conditions, disbursement — and where exactly does origination end?
7. What terminal outcomes exist besides funded (decline, withdrawal, cancellation, lapse)?
8. Which surfaces exist for staff, borrower, and third-party channels (agents/brokers/dealers)?
9. What integrations form the spine (bureaus, KYC/IDV, fraud, e-signature, core banking, payments, decisioning services)?
10. How does packaging vary (standalone LOS vs end-to-end lending suite vs platform module), and does packaging change the core?

## Representative Products

Selection principles: market representation + documentation completeness + different product philosophy + different customer tier. Four products sampled, spanning segment-neutral SaaS, US bank/credit-union, configurable fintech SaaS, and enterprise commercial poles:

| Product | Pole | Tier | Sources reached |
|---|---|---|---|
| MeridianLink (loan origination software solution page + FAQ) | US bank/credit-union LOS family, multi-line (consumer/mortgage/business/indirect) | Bank / CU | Official solution page + FAQ (A) |
| TurnKey Lender (loan-origination-system page + platform root) | Segment-neutral cloud lending platform, AI-decisioning-first | Mid-market / fintech | Official product page + root (A) |
| HES LoanBox (loan-origination-software page + docs.hesfintech.com) | Configurable multi-segment SaaS; one engine for persons and legal entities | SMB / fintech | Official product page (A) + official product documentation portal (A, Tier-1) |
| nCino (commercial-lending solution page) | Enterprise commercial LOS | Large bank / enterprise | Official solution page (A) |

Sibling-pass evidence reused as corroboration (not as primary): commercial-loan-origination pass (nCino, Baker Hill, Moody's Lending Suite, Finastra LaserPro — product pages), consumer-lending-platform pass (LoanPro, TurnKey Lender, MeridianLink Consumer, HES LoanBox — product pages + FAQs), loan-management-system pass (Nortridge user guide, LoanPro knowledge base — Tier-1).

## Sources

Primary (fetched 2026-09-08):

- MeridianLink — https://www.meridianlink.com/solutions/loan-origination-software/ (solution page incl. FAQ)
- TurnKey Lender — https://www.turnkey-lender.com/loan-origination-system/ and https://www.turnkey-lender.com/ (product page + platform root)
- HES FinTech — https://hesfintech.com/loan-origination-software/ (product page); https://docs.hesfintech.com/ (documentation portal); https://docs.hesfintech.com/loanbox/customer-onboarding-and-application-process/what-is-customer-onboarding/ (application process); https://docs.hesfintech.com/loanbox/loan-origination-process/step-by-step-description/ (origination step-by-step)
- nCino — https://www.ncino.com/solutions/commercial-lending (solution page)

Unreachable / not attempted:

- turnkeylender.com (non-hyphenated domain) — 404 ×2 on guessed paths; root on turnkey-lender.com succeeded (recorded per the 1–2-failure rule)
- ncino.com/solutions/loan-origination — 404; commercial-lending page used instead
- MeridianLink client Knowledge Base / product help center — login-walled support class (consistent with prior lending passes); not fetched
- nCino help center — login-walled (confirmed in the commercial-loan-origination pass)
- TurnKey knowledge base / FAQ subpages — not fetched (root + product page sufficient for capability-level claims)
- HES regional solution pages (US/UK/SA/AU/CA/PH) — listed in nav, not fetched; regional regime machinery therefore described at variant level only

Evidence layers: A = directly observed on an official source for a specific product; B = cross-product commonality; C = canonical inference from comparison + boundary reasoning.

---

## Product Observations

### MeridianLink — loan origination software (A)

- Vendor's own definition (FAQ): "Loan origination software (LOS) is a banking software that automates and streamlines the entire loan process—from application to approval and funding."
- Segment span (marketing H1 + FAQ): "consumer, mortgage, business, and indirect lending"; loan types listed: personal loans, credit cards, auto loans, business loans, real estate loans, indirect, "and more."
- Platform framing: "connecting applications, decisions, and workflows into a single, seamless experience"; ecosystem page lists consumer lending, mortgage lending, account opening, digital application (Access), data intelligence, collections, marketing automation as connectable products — an end-to-end suite in which LOS is the lending core.
- Decisioning: "Automate decisioning and processing — Streamline loan underwriting and funding with configurable workflow automation and an advanced decisioning engine built for speed and accuracy." FAQ: "our LOS includes advanced automation tools for underwriting and decisioning."
- Compliance posture: "Automate regulatory compliance with embedded controls, audit trails, and integrations for fraud and identity verification"; FAQ: "built-in features and a robust network of third-party integrations to support compliance and fraud protection."
- Borrower edge: "Deliver a fully digital, mobile-first experience — Guide borrowers seamlessly from application to funding with smart forms, intuitive workflows, and a mobile-first design that reduces abandonment and keeps applications moving."
- Integrations: marketplace of "hundreds of partner integrations including AI-enabled underwriting and identity verification, e-signing, insurance"; FAQ: "open APIs and flexible integrations … including core banking systems."
- Operations: cloud-based (FAQ: "100% cloud-based"); real-time dashboards, tailored reports, "adjust rates on the fly."
- Case-study quotes (customer evidence, treated as claims): "automated decision engine", "decisioning speed and customizable workflows", "underwriting systems … several lines of business running through the system", consolidated "13 lending solutions to 1".

### TurnKey Lender — Loan Origination System (A)

- Positioning: "TurnKey Lender's highly configurable, scalable loan origination software" with "AI-powered credit decisioning"; platform root describes a lending infrastructure for "consumer and commercial finance providers … Non-bank, embedded, and traditional lenders."
- Vendor's own end-to-end borrower flow (LOS page bullet list): "Borrower applies online → Loan options are instantly generated → Borrower signs the agreement in the borrower portal → Application is automatically approved → Funds are disbursed."
- LOS page capability blocks: instant AI credit decisioning ("proprietary … Decision Engine; built into our automated Loan Origination System"); "Adjustable online application flow — Fully configurable loan application process allows for the creation of custom application flows, dictionaries, and loan offers"; "intuitive digital borrower portal"; "robust back-office for your employees"; "advanced analytics and management capabilities"; "highly configurable auditing and employee tracking."
- Data/verification at decision time: "Credit Bureau checks, ID verification, bank account verification and bank statement scoring, as well as 200+ built-in fraud detection rules and blacklists" (numeric rule count = vendor claim, L3).
- FAQ feature list: "digital onboarding, AML (Anti Money Laundering) and KYC (Know Your Customer) compliance checks, loan application processing and credit scoring and automatic decisioning."
- Underwriting companion page (from root nav): "in-depth risk scoring, borrower evaluation, decision rules checks, loan agreement generation, loan offer management."
- Lifecycle span: "Automate loan origination, credit scoring and underwriting, servicing, and collections processes with a single end-to-end solution instead of using 3-5 tools" — the end-to-end packaging pole, with loan management/servicing/debt collection as separately named platform modules.
- Population breadth (root "What kind of a lender are you?"): commercial, consumer, BNPL, AR financing, healthcare, P2P, leasing, non-profit, payday/micro, MCA, equipment, banks.
- Credit product builder: "hyper-flexible credit products with complex schedules, fees, taxes, interest and configurable rules"; collateral module; 75+ preconfigured integrations (accounting, credit bureau, KYC/AML, payment, notification).

### HES LoanBox — LoanBox LOS (A; Tier-1 documentation)

Product page (A):

- Vendor's own definition (FAQ): "Loan origination software supports lenders throughout the full process of creating a new loan, starting from the initial application and ending with the final approval. It automates onboarding, verification, scoring, underwriting, and document preparation."
- Segment-agnostic positioning (FAQ): "A loan origination system is designed for a wide range of lenders: banks, fintech companies, credit unions, and microfinance institutions. It supports a range of lending products, risk policies, and regulatory frameworks."
- "Who can use / connect" (FAQ): integrates "credit bureaus, KYC/AML services, payment gateways, core banking platforms, CRMs, and other third-party data sources."
- Auditability (FAQ): "All scoring inputs, model versions, thresholds, overrides, and final outcomes are logged and time-stamped … every automated decision is verified and ready for internal audits and regulatory reviews."
- Configuration (page): "Flexible process builder — Tailor the lending origination process with no coding required. Build application steps, define decision logic, and craft individualized customer journeys"; "Unlimited product configuration … customizable fees, rates, and repayment structures"; "Automate contract templates … dynamic templates"; underwriting paths "manual, hybrid, or fully automated"; exception handling named as an evaluation criterion in their buying-guide FAQ.
- Partner channel: "Build distribution networks with streamlined agent onboarding. Partners originate loans, monitor earnings, and manage portfolios."
- End-to-end packaging: "HES LoanBox connects origination, servicing, and collections in one platform, eliminating handoffs."

Documentation portal (A, Tier-1) — the operational spine:

- **Two-stage decomposition of the front of the loan**: "Customer onboarding (the application process) is the set of steps that capture a customer's loan request and collect all the data the system needs before the request is handed to origination for a credit decision. … From that point, the application is handed over to the origination process." Intake purpose: "identity, contact details, address, financial data, bank account, and—if the product group requires them—collateral details."
- **Channels converge on one case**: "The process is the same regardless of channel. The same product groups, forms, and data collection logic apply in the Borrower Portal, the Back Office, the Agent Portal, and when the application is started from an agent invitation to a lead." Parties: "a customer (the borrower), an operator (back-office or agent user who initiates the application on behalf of the customer), and optionally an agent attached to the deal."
- **Application identity and lifecycle hygiene**: "The application has a single human-readable application number that identifies it across all channels and status changes." "Starting a new application automatically closes any still-open application the same borrower had from a previous attempt." (Also a timeout on the initial step — precise default kept here, not canonized.)
- **Intake flow**: choose product group → blacklist/duplicate check → loan calculator (amount/term/payment frequency) → data entry (personal/company data, identity documents, address, employment/financial information, bank account) → KYC identity check + bank-account verification via open banking → collateral/extra info if required → review and confirm conditions + supporting documents → handed to origination.
- **Origination step-by-step** (14 documented steps, condensed): application status set to verification; borrower tracking screen (status, requested conditions, supporting documents, "final loan conditions in your contract may differ" notice, Cancel button with confirmation); automatic financial-data retrieval (open banking; failure terminates the application as an error case); automatic credit-bureau report; automated stop-factor controls ("blacklists, age limits, residency rules" — configurable; any stop factor → automatic decline); verification step (configurable None/Manual) where a back-office verifier approves, requests updates (borrower gets a bounded revision task; non-response auto-declines; resubmission re-runs stop factors), or declines with a reason; legal-entity step where the verifier enters company financial figures and the platform computes profitability ratios (margins, EBITDA-class measures, net-worth/net-debt ratios); automatic scoring (result = zone + score value); automatic credit-limit calculation; automatic product selection matching request + limit; underwriting decision per the product group's setting: auto-approve, send to underwriting, or reject; manual decision task where an underwriter approves (setting final amount, term, interest rate, first payment date, loan product), declines (with reason), or returns to the verifier (with free-text reason); final approval — collateral LTV calculation, prime-rate snapshot, status Approved, amortization schedule calculated and validated (invalid schedule → declined), borrower notified — after which the application "leaves the Loan Origination stage and continues into the contract-signing stage."
- **Stage sequence in the docs tree**: customer onboarding → loan origination process → scoring and credit decisioning → contract signing (signing options, signing flow, deadline expiration, "new offer mid-signing" scenario) → loan management and servicing (creating a loan/credit line, activating, disbursement, interest accrual, payment allocation, write-off, adjust) → collection process. Collateral management (requirements, verification, LTV, re-evaluation) and agents/agent portal are sibling modules; borrower portal is the self-service surface; product groups/products drive journeys ("settings that define borrower journeys"); reports/analytics via dashboards.
- **Person vs Legal Entity**: the step-by-step explicitly covers "both borrower types," with legal-entity-specific financial-data entry — one engine, two populations.

### nCino — Commercial Loan Origination System (A; commercial pole)

- Explicit Type naming: "Commercial Loan Origination System"; "Replaces disparate, siloed systems with a streamlined commercial loan origination system."
- Collaboration span: "Improves collaboration and transparency across front, middle, and back offices."
- Policy-driven automation: "Onboards new customers and assesses their needs faster with preconfigured workflows. Automates pre-qualifications and credit approvals based on your institution's policy rules. Identifies parameters in which a loan should be automatically approved, declined, or recommended for manual review." — the auto-approve / auto-decline / manual-review triad, configured from the institution's policy.
- Compliance machinery: "integrated document repository that incorporates your institution's policies and leaves a visual audit trail for auditors and teammates"; "automatic notifications to remind users when a covenant is approaching its due date and serves as a record of compliance for auditing purposes"; "Provides regulators and auditors with loan reports."
- Deal Management: "complete view of the relationship in a single location"; "structuring and management of credit/non-credit deals and products"; "supports creation of sub-loans, information cloning, and bulk editing of details for shared records."
- Companion solutions named separately: Spreads (credit analysis "seamlessly integrated into the commercial loan origination workflow"), Automated Spreading, and Credit Portfolio Management — the last being a distinct solution (portfolio layer, not origination).
- Scale claim ("processed $3.3T in loans in a period of 12 months", "over 2,700 customers globally") — vendor marketing claim, L3, not canonized.

---

## Cross-product Comparison

| Structure / capability | MeridianLink | TurnKey Lender | HES LoanBox | nCino | Layer |
|---|---|---|---|---|---|
| Application/case as identified tracked unit with status | A (applications connected across the suite; digital application from application to funding) | A (configurable application flow; borrower portal + back office) | A (application number across channels/statuses; 14-step status progression) | A (deal/loan records; preconfigured workflows) | B — core |
| Lender-side staged pipeline from intake to funding | A ("from application to approval and funding"; workflow automation) | A (five-step flow ending "funds are disbursed") | A (documented stage sequence onboarding → origination → contract signing → loan creation) | A (preconfigured workflows; front/middle/back-office collaboration) | B — core |
| Data assembly + verification before decision (identity/KYC, bureau, bank data; fraud checks) | A (fraud + IDV integrations; embedded controls) | A (bureau checks, ID verification, bank-account verification, statement scoring, fraud rules, blacklists) | A (KYC + bank-account verification at intake; bureau report; stop factors; open-banking pull) | A (via integrations; document repository with policies) | B — core (machinery varies) |
| Credit evaluation machinery under the lender's policy (rules/scores/models; configurable auto vs manual paths) | A ("advanced decisioning engine"; configurable workflow automation) | A (Decision Engine built into LOS; loan offer generation; decision rules checks) | A (underwriting settings auto/manual; scoring zones; credit-limit rules; product selection; stop factors) | A ("automatically approved, declined, or recommended for manual review" per institution's policy rules) | B — core |
| Recorded decision: approve with terms / decline with reason / refer | A (decisioning + audit trails; case-study mentions of approvals) | A (instant decisions; underwriting decision rules; auditing configurable) | A (auto-approve; underwriter approve/decline-with-reason/return; auto-decline on stop factor or invalid schedule) | A (auto-approve/decline/manual-review; approvals per policy) | B — core |
| Execution to funding: offer/agreement, signing, disbursement | A ("application to funding"; e-signing integrations) | A ("Borrower signs the agreement in the borrower portal … Funds are disbursed") | A (contract-signing stage with expiration/new-offer scenarios; disbursement in the servicing module) | A (document generation/repository in the CLOS context; funding implied in workflow language) | B — core (depth varies) |
| Booking handoff to the loan record / servicing | B (suite connects collections; core banking integrations) | B (loan management/servicing as sibling modules of one platform) | A (docs sequence: origination → contract signing → loan creation/activation/disbursement/servicing) | B (Credit Portfolio Management as separate solution; booking via integrations) | B — seam behavior |
| Borrower self-service application portal with status tracking | A (mobile-first digital application experience) | A (digital borrower portal; borrower signs in portal) | A (tracking screen, cancel button, revision tasks) | — (borrower edge not documented on the reached page; commercial intake is staff-mediated in the sibling pass) | B — common (mature) |
| Audit trail / compliance record | A (embedded controls, audit trails) | A (configurable auditing and employee tracking) | A (scoring inputs/model versions/thresholds/overrides/outcomes logged and time-stamped) | A (visual audit trail; regulator/auditor reports; covenant reminders) | B — common (mature) |
| Configurable loan products / process (no-code product + flow configuration) | A (tailored configurations; "adjust rates on the fly") | A (configurable flows, dictionaries, offers; credit product builder) | A (product groups/products; process builder; scoring model settings) | A (preconfigured workflows; policy parameters) | B — common (mature) |
| Collateral handling in origination | B (insurance integrations) | A (collateral module incl. valuation/re-evaluation) | A (collateral requirements, verification, LTV at final approval) | B (covenant/conditions context) | B — common (not universal) |
| Third-party origination channels (agents/brokers/dealers; indirect) | A (indirect lending line; DecisionLender product) | B (P2P solution; partner channels not on LOS page) | A (agent portal; operators originate on behalf) | B (deal management for relationship products; indirect not on reached page) | B — common, variant-heavy |
| Cross-sell/pricing machinery | A (personalized cross-sell offers; adjust rates) | B (loan offer management) | A (automatic product selection; campaigns) | — | B — common |
| Task queues / staff work assignment | A (workflow automation) | B (back-office) | A (process tasks: verifier task, financial-data task, decision task) | A (front/middle/back-office collaboration) | B — common |
| Reporting / analytics | A (real-time dashboards, reports) | A (advanced analytics and management capabilities) | A (dashboards/reports module) | A (real-time reporting for portfolio management) | B — common |
| End-to-end suite packaging (origination + servicing + collections in one) | A (suite: lending + collections + marketing on one platform) | A ("single end-to-end solution instead of 3-5 tools") | A ("connects origination, servicing, and collections in one platform") | B (platform suite; portfolio management separate) | B — packaging variant, NOT definitional |
| Segment-scoped editions (consumer/commercial/mortgage/indirect) | A (four named lines) | A (consumer + commercial solutions over one platform) | A (one engine, Person + Legal Entity; per-segment solution pages) | A (commercial LOS naming) | B — variant axis |

Key cross-product findings:

1. **The unit of work is the application/case**, identified, status-bearing, channel-agnostic. HES documents a single application number across channels and status changes; nCino speaks of deals/loan records; MeridianLink and TurnKey describe application flows with status. (B → core)
2. **The pipeline is lender-side and stage-configured.** All four describe an institution-defined process (stages/workflows/parameters), not a fixed vendor process. (B → core)
3. **Evaluation is policy-governed machinery with a three-way routing posture**: fully automatic, fully manual (underwriter/committee), or hybrid — the same triad appears in HES (auto-approve / send to underwriting / reject), nCino (approved / declined / manual review per policy parameters), TurnKey (Decision Engine with human back office), MeridianLink (decisioning engine + configurable workflows). (B → core)
4. **The decision is a recorded institutional act.** Declines carry reasons; approvals carry final terms (HES: underwriter sets amount/term/rate/product; auto path approves on requested terms); audit trails are first-class in all four. (B → core)
5. **Origination ends at a funding boundary.** HES documents the cleanest seam: origination process ends at "Approved" + schedule validation → contract-signing stage → loan created/activated/disbursed (servicing). TurnKey's flow ends "funds are disbursed." MeridianLink: "application to approval and funding." The booking handoff is the shared terminal act. (B → core, corroborating the commercial-loan-management funding seam)
6. **Borrower self-service and channels are common but shaped per segment**: digital portal (consumer-flavored) vs staff/deal-mediated intake (commercial-flavored) vs agent/broker/dealer channels — one machinery, different channel emphasis. (B → common/variant)
7. **Packaging is the market's noisiest axis**: the same word "LOS" is sold as (a) an origination-scoped module, (b) one module of an end-to-end lending suite spanning servicing and collections (TurnKey, HES, MeridianLink suite framing), and (c) a platform inside a broader bank operating system (nCino). Packaging does not change the core: in every case the documented origination core is the same pre-funding case pipeline. (B → variant)
8. **Population invariance holds**: HES one engine for Person + Legal Entity; TurnKey's industry list; MeridianLink's four lines; nCino's commercial depth. Narrowing the borrower population does not change the core model — this discharges the population-test flag from this side. (B/C)

---

## Canonical Model (L0 / L1 / L2 / L3)

### L0 — Defining Invariant (deliberately small)

```text
The credit application as case of record
  (one persistent, individually identified case per borrower's request for
   credit, carrying the applicant — person or organization — the requested
   credit, and the evidence file; reachable from every intake channel)
└── The lender-side origination pipeline
    (the case advances through the lender's own defined stages from intake
     toward funding; the system is the record of in-flight credit work —
     status, ownership, history)
└── Credit evaluation under the lender's policy
    (applicant data assembled from defined sources and verified — identity,
     financials, credit history, bank data, collateral — then assessed against
     the lender's credit policy through configurable machinery: automated
     rules/scores/models, human underwriting, or hybrid routing)
└── The recorded decision executed to funding
    (approve with final terms / decline with reasons / refer — recorded with
     basis and actor as an audit-ready institutional act; approved cases are
     completed as fundable loans — offer/agreement, conditions, disbursement —
     ending in a booking handoff to the loan record; decline, withdrawal and
     cancellation are recorded terminal outcomes)
```

Jointly-held test (load-bearing):

- 1 alone = an application/form tracker, not an origination system.
- 2 without 1 = workflow machinery with nothing case-bound.
- 3 without 2 = the Credit Decisioning Platform (evaluation engine invoked at decision points, no pipeline).
- 1+2 without 3 = a generic BPM tracker; the credit-policy machinery is what makes the pipeline a credit pipeline.
- 1–3 without execution-to-funding = decisioning + case management; the booking handoff is what makes the system an origination SYSTEM rather than a decision service.
- All four minus the recorded-decision leg = a form-plus-disbursement utility with no credit act.

### L1 — Common Mature Structure (widespread; not definitional)

- Borrower-facing digital application portal (apply, upload documents, track status, sign, cancel) with status notifications.
- Contract/agreement generation from templates + e-signature stage between decision and funding.
- Configurable loan products (amount/term/rate/fee structures) and configurable process flows that drive application forms and decision routing.
- Collateral handling in origination: requirements, verification, valuation/LTV at approval.
- Task queues and role-based work assignment (verification tasks, financial-data tasks, decision tasks).
- Reporting/analytics: funnel throughput, decision outcomes, portfolio metrics; rate/pricing adjustments.
- Audit/compliance surfaces: time-stamped decision logs, document repositories with policy context, regulator/auditor reports.
- Integration spine: credit bureaus, KYC/AML and identity-verification services, fraud tools, open-banking/bank-data providers, e-signature, payment rails, core banking/booking systems.
- Duplicate/concurrent-application hygiene (new application closes the borrower's previous open one — observed A-layer at HES; treated as common practice, not invariant).

### L2 — Variant / Optional Structure

- **Packaging**: origination-scoped product vs end-to-end lending suite (origination + servicing + collections) vs module inside a bank platform/suite. The market's "LMS/LOS/platform" labels drift across all three; membership in this Type = documented pre-funding case pipeline, not the label.
- **Segment editions and channel emphasis**: consumer direct-digital; commercial staff/deal-mediated with financial-statement analysis; mortgage collateral-regime machinery (sibling leaf); indirect/dealer and agent/broker channels; embedded/point-of-sale.
- **Decision philosophy**: AI/ML-first instant decisioning (TurnKey, HES/GiniMachine) vs policy-rules-first commercial governance (nCino) vs human-committee heritage (commercial sibling pass evidence).
- **Deployment**: cloud SaaS (dominant in sample), vendor-hosted, on-premise heritage.
- **Regulatory regime machinery**: disclosure documents, adverse-action outputs, bureau regimes, jurisdiction-specific checks (US-weighted in sample; HES ships region pages — not fetched, kept at variant level).
- **Cross-sell/offer optimization, A/B testing of forms, lead-generation modules** (TurnKey), deposit-account bundling with the loan application (MeridianLink).

### L3 — Vendor-specific (research notes only)

- HES: "stop-factor" terminology; scoring "zones" (top/middle); prime-rate snapshot at approval; amortization-schedule validation as an auto-decline trigger; "Account verification" status name; 48-hour intake timeout and 72-hour revision deadline defaults; Keycloak-based user/role management; Metabase-based analytics; "new offer mid-signing" scenario.
- TurnKey: "200+ built-in fraud detection rules"; "90%+ ready-to-use" preconfiguration; one-second auto-processing and 280% efficiency claims; award badges; Decision Engine branding; dictionary/offer configuration vocabulary.
- MeridianLink: product names (Consumer, Mortgage, Access, Opening, DecisionLender, Data Connect, Insight, Engage, Collect); Marketplace; combined loan + deposit application in one session; "adjust rates on the fly."
- nCino: Deal Management (credit/non-credit deal structuring, sub-loans, cloning, bulk editing); Spreads / Automated Spreading; "$3.3T processed / 2,700 customers" claims; covenant due-date notifications from the LOS; front/middle/back-office framing.
- Cross-vendor marketing metrics (speeds, accuracy multiples, NPL reductions) recorded as claims, not facts.

---

## Historical / Market-Sample Check

- **Generational evidence**: lending origination predates software. A paper-era lender runs the same four legs: a loan application form as the identified case (1); the file moving across desks — intake, verification, analysis, approval, closing (2); an underwriter or loan committee applying the institution's written credit policy and scorecards to verified evidence (3); a minuted approval or decline, loan agreement executed, funds disbursed, loan booked into the ledger (4). None of portals, e-signature, bureaus-via-API, AI, or cloud is required. The L0 passes.
- **Regional/platform-native check**: microfinance, Islamic-finance, P2P, and embedded/BNPL forms (all named by sampled vendors as supported populations) satisfy the same core with different evidence classes and product machinery. Core-banking-embedded origination modules satisfy it as platform modules. Regional regulatory machinery (US disclosure/adverse-action emphasis; EU/UK regimes) sits in L2. The sample is US/global-SaaS-weighted; HES's regional pages were not fetched, so regime-specific structures are deliberately kept out of the core.
- **Scale check**: a small lender auto-deciding small-ticket loans in seconds and a large bank running committee-governed commercial facilities both satisfy the core; complexity and committee machinery are variant axes (echoing the commercial sibling pass).
- **Anti-overfitting check**: decision engines, open-banking pulls, e-signature, digital portals, and product-builder studios are the current dominant implementations of the four legs, not definitional — a lender whose analysts hand-verify documents and whose committee minutes approvals in the system still runs the same Type.

---

## Boundary Findings

| Neighboring Type | Seam | Test ("remove what → becomes the other Type") |
|---|---|---|
| Loan Management System (processed) | Funding seam, now confirmed from both sides: origination = pre-funding case pipeline ending in the booking handoff; LMS = post-funding servicing ledger over funded accounts. HES docs sequence the handoff explicitly (origination → contract signing → loan creation/activation/disbursement). Packaging blurs: end-to-end suites document both sides; membership test for this Type = documented pre-funding case pipeline; a documented servicing ledger indicates the end-to-end packaging variant | strip the pipeline, keep the servicing ledger → LMS; strip the servicing loop, keep the pipeline → LOS |
| Consumer Lending Platform (processed) | Scope axis (that pass's resolution, corroborated here): consumer platform = borrower-segment-scoped lifecycle (origination→servicing→collections on one record for individuals); generic LOS = stage-scoped, segment-agnostic. Population invariance observed in the sample (HES Person+Legal Entity one engine; TurnKey industry list; MeridianLink four lines) | add borrower-segment lifecycle packaging → consumer platform; strip the funded-account servicing machinery, keep the stage function → LOS |
| Commercial Loan Origination (processed) | Sector seam inside one origination family, per that pass's adopted distinction: commercial = business borrowers + financial-statement assessment machinery + policy/committee approval; the generic leaf carries the same pipeline without the sector-specific assessment machinery. Population test DISCHARGED from this side: narrowing the sector does not change the core model → keep-both family with variant treatment | narrow the population to business borrowers and add spreading/financial-statement machinery → commercial leaf |
| Mortgage Origination Platform (unprocessed) | Collateral-regime seam (per commercial pass): amortizing residential machinery (escrow setup, disclosures, investor/GSE workflows) vs the generic pipeline. Mortgage lending appears in the sample only as a MeridianLink product line — machinery not documented here | replace generic closing/conditions machinery with mortgage-specific collateral-regime machinery → mortgage origination |
| Credit Decisioning Platform (processed) | Layer seam, corroborated: all four sampled LOS products document embedded decisioning; a standalone decisioning platform has no application pipeline, documents, conditions, or funding execution — it is invoked by the LOS at decision points (that pass's own finding) | strip everything but evaluation rules/models → decisioning platform; remove the invocation seam, keep the full case pipeline → LOS |
| Credit Scoring Application (processed) | Measure vs action: a score is computed inside evaluation; the recorded decision with terms is the LOS output | remove the decision action, keep the measure → scoring |
| Credit Management Platform (processed) | Domain seam: trade/B2B credit governance over customers buying on open account vs lender-side origination of credit requests | swap loan applications for trade-credit customer limits/reviews → credit management |
| CRM | Object seam: origination carries credit-policy evaluation, evidence-based assessment, and closing/funding execution that CRM lacks; CRM-heritage substrates exist (nCino) but the credit machinery is the identity | drop credit policy, assessment, and closing execution → CRM |
| KYC / Identity Verification, Fraud Prevention platforms | Point-check seam: identity/fraud checks are capabilities consumed inside the pipeline (documented at intake in all sampled products), not the pipeline itself | keep only the checks, drop the case pipeline → IDV/fraud platform |
| Underwriting Workbench (insurance, §15) | Sector seam: same word, different domain (insurance risk selection vs credit approval) | swap credit machinery for insurance risk machinery → insurance workbench |
| Financial Aid Management (processed) | Direction seam (that pass's note): aid institutions record-and-certify awards from set-aside funds; lenders evaluate and hold credit for repayment | swap award/certification machinery for credit machinery → financial aid |
| Application Tracking / workflow platforms (generic) | Domain seam: generic trackers lack credit-policy evaluation machinery and the funding/booking terminal act | strip credit policy + booking handoff → generic workflow tracker |

**Joint-review discharges and flags for STATUS.md**:

1. **Discharge (origination side) of the loan-management-system pass flag**: the funding seam is confirmed from the origination side with Tier-1 documentation (HES docs stage sequence; TurnKey flow terminus "funds are disbursed"; MeridianLink definition "from application to approval and funding"). The "LMS/LOS/platform" terminology drift is real: sampled origination-led vendors document end-to-end packaging (origination + servicing + collections in one platform) while the documented origination core stays the same. Membership test adopted: documented pre-funding case pipeline = LOS; documented servicing ledger over funded accounts = (also) LMS — end-to-end suites instantiate both directory leaves as packaging, not as new Types. Joint review of the family remains recommended (see below).
2. **Discharge (origination side) of the commercial-loan-origination pass population-test flag**: the population test passes — the generic core model is unchanged across consumer, commercial, mortgage-line, and specialty populations in all four sampled products. Generic LOS = the full origination Type; Commercial Loan Origination / Mortgage Origination Platform / Consumer Lending Platform stand as sector/segment-scoped siblings (keep-both, consistent with the loan-management-system pass's resolution for the servicing family). Variant treatment recommended at any family joint review.
3. **Corroboration of the consumer-lending-platform pass scope-axis resolution** from a third side (the generic stage-scoped leaf).
4. **Corroboration of the credit-decisioning-platform pass layer seam**: LOS-embedded decisioning is universal in the sample; the boundary (evaluation engine as invoked layer vs case pipeline through funding) holds; that pass's "variant overlap to watch" stands — decisioning modules inside LOS suites are a variant, not a separate Type.
5. **Family joint review still recommended** (directory-level): Loan Origination System + Loan Management System + Consumer Lending Platform + Commercial Loan Origination + Mortgage Origination Platform partition one lending lifecycle across two axes (stage vs segment). All five leaves' passes agree on the same resolution pattern (keep-both, scope axes, funding seam). A directory-level joint review would ratify cross-references and possibly variant treatment.
6. **Bookkeeping note**: applications/commercial-loan-origination.md + research/commercial-loan-origination.md exist (research date 2026-09-07) but no corresponding Processed line for commercial-loan-origination was found in STATUS.md — likely a missed status entry, surfaced to avoid double-processing.

---

## Uncertainties

1. **MeridianLink operational depth**: evidence is the official solution page + FAQ only; the client Knowledge Base is login-walled. No operational micro-detail (stage names, default values, configuration mechanics) asserted for this product.
2. **nCino**: public solution page only; help center login-walled (confirmed in the commercial sibling pass). Deal Management / Spreads / portfolio products described at capability level.
3. **TurnKey**: product page + root only; the knowledge base/FAQ subpages were not fetched. Precise stage vocabularies and defaults not asserted; numeric claims (fraud-rule counts, speed multiples) treated as vendor claims.
4. **Mortgage machinery**: mortgage lending is documented here only as a MeridianLink line and a HES nav entry; the Mortgage Origination Platform leaf (unprocessed) owns the collateral-regime machinery. This pass deliberately does not characterize it.
5. **Indirect/dealer origination** (auto) evidenced thinly (MeridianLink DecisionLender positioning; HES POS/BNPL solution pages listed but not fetched) — treated as a variant, not characterized in depth.
6. **Regional regimes** (EU/UK/other) — HES region pages exist but were not fetched; regime machinery kept at variant level, out of the core.
7. **Borrower-side self-service depth for commercial origination** — the nCino page documents staff-side collaboration; borrower-edge digital intake for commercial is evidenced more strongly in the commercial sibling pass (digital intake as a variant pole) than here.

---

## Final Synthesis

The generic Loan Origination System is the lender's staff-side case system for the pre-funding half of the lending lifecycle. Its defining structure is four jointly-held legs: (1) the credit application as a persistent, identified case of record reachable from every intake channel; (2) a lender-defined origination pipeline that the case advances through, with the system as the record of in-flight credit work; (3) credit evaluation of verified applicant data under the lender's own credit policy, through configurable machinery that routes between automatic decisioning, human underwriting, and hybrid review; and (4) the recorded decision — approve with terms, decline with reasons, refer — executed to funding, ending in the booking handoff of a funded loan to the servicing side (or a recorded decline/withdrawal/cancellation).

The definition is deliberately segment-neutral: the same core holds for a fintech auto-deciding consumer loans, a credit union processing personal and auto applications, and a bank running committee-governed commercial facilities — what changes with population is the evidence class and the surrounding machinery, not the structure. The definition is also era-neutral: the paper application form, the desk-to-desk loan file, the policy manual, and the minuted approval satisfy all four legs.

The funding seam is the Type's hard boundary: origination owns the case until booking; the servicing ledger over the funded account belongs to loan management. The evaluation seam is the Type's layer boundary: decisioning engines and scoring models are capabilities consumed inside the pipeline; standalone, they are different Types. Packaging (standalone LOS vs end-to-end lending suite vs bank-platform module) is the market's noisiest axis and the least structural: the documented origination core is the same in all three packages.
