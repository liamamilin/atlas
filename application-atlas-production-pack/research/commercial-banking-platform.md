# Research Notes — Commercial Banking Platform

Research date: **2026-09-07** (single pass)
Methodology: v1.1 (update-v1/). Evidence layers: **A** = directly observed on official pages of that product; **B** = cross-product commonality across the sample; **C** = canonical inference from comparison + Type-boundary reasoning.

---

## Research Goal

Understand the software category "Commercial Banking Platform" as it actually exists in the market: what the bank-operated platforms for commercial/corporate clients contain, who operates and who uses them, how the banking relationship is digitally operated, and how the category differs from its densely neighboring directory leaves (business banking portal, cash management platform, treasury management system, loan management, consumer digital banking).

This leaf sits in the most heavily pre-processed corner of the directory: two adjacent leaves were processed earlier on 2026-09-07 and both recorded explicit joint-review flags pointing at this leaf:

- **business-banking-portal** — confirmed the SMB↔corporate tier seam as a real Type seam ("every sampled bank that operates a business portal also sells a separate corporate/cash-management platform... CashPro vs BA360; JPM Commercial Banking vs Chase Business Online..."); removal test recorded: "scale up rails + treasury machinery → commercial/cash-management platform".
- **cash-management-platform** — recorded a breadth seam with this leaf: "the cash management platform is the treasury-operations channel of the broader commercial relationship... test: strip credit/lending and keep account operations → this Type" — and recommended joint review when this leaf is processed.

This pass discharges those flags where the evidence allows and records what remains for joint review.

---

## Initial Boundary

Working hypothesis before research:

1. The core use is the bank's commercial/corporate clients operating their banking relationship digitally (accounts, payments, credit, other services) — the platform is the bank's own channel, not client-side software.
2. Users are finance/treasury staff acting for an organization under granted authority — not consumers, not bank staff.
3. Nearest neighbors: business banking portal (tier below), cash management platform (function slice within it), corporate TMS (client-side counterpart), banking back-office platform (bank-staff side), commercial loan origination/management (loan lifecycle depth), consumer digital banking (person as customer).
4. Unknowns: whether the credit relationship is definitionally inside the platform or a module; whether the market really sells this as a distinct product from "cash management platform"; how regional banks structure it; whether older (pre-web) platforms fit any candidate definition.

---

## Research Questions

1. Who is the served customer, and how do banks define the "commercial" segment vs business vs corporate/institutional?
2. What does the platform actually contain — which banking product families are surfaced digitally?
3. Is the credit relationship (loans/lines) serviced inside the platform, and how?
4. What is the authority model (users, roles, entitlements, approvals, signers)?
5. What channels exist (web portal, mobile, files/APIs/SWIFT/host-to-host, ERP embedding)?
6. What servicing exists inside the platform (service requests, signer changes, documents, letters)?
7. How do banks structure the platform family (one platform vs several per tier/division)?
8. Regional variety beyond US money-center banks?
9. Historical check: would pre-web corporate banking platforms still fit the definition?
10. Where exactly do the recorded seams (business portal tier seam, cash-management breadth seam) hold?

---

## Representative Products

Selected for market representativeness, documentation reachability, different product philosophies (relationship-breadth platform vs treasury-channel platform), and different customer tiers and geographies:

| Product | Bank | Tier / segment | Geography | Role in sample |
|---|---|---|---|---|
| Wells Fargo Vantage (ex-CEO portal) | Wells Fargo | Commercial Banking division (mid-market to large commercial) | US | commercial-division relationship platform; generational platform replacement evidence |
| J.P. Morgan Connect | JPMorganChase | Commercial Banking division (midsize businesses, innovation economy, CRE) | US | commercial-division platform spanning deposits + loans + cards + merchant accounts |
| J.P. Morgan Access | JPMorganChase | corporate / institutional treasury (Payments) | global | the pure treasury-channel pole of the same bank — contrast case for the breadth seam |
| HSBCnet | HSBC | corporate / institutional | global (UK/Asia/US) | broadest single-platform service catalog incl. trade + securities + markets |
| ANZ Transactive Global | ANZ | institutional & large corporate | Australia/APAC (global network) | regional variety; reachable Tier-1 help center; loans/trade in-platform |

Abandoned: **Bank of America CashPro** — cashpro.bankofamerica.com transport error ×2 (prior pass) + ×1 this pass; business.bofa.com CashPro page transport error ×1. Recorded as unreachable; contributes named-only evidence (BofA sells CashPro as its corporate/commercial platform — from BofA's own tier taxonomy observed in the business-banking-portal pass).

---

## Sources

All fetched 2026-09-07 unless noted. Layer **A** for the product observed.

- Wells Fargo — Vantage platform page (persona-driven design; dashboard; task list incl. paydown loans; self-service; mobile; CEO→Vantage FAQ; company-admin setup): https://www.wellsfargo.com/com/vantage (A)
- Wells Fargo — Commercial Banking division hub (segment claim; solution families incl. lending, trade, treasury; Vantage sign-on): https://www.wellsfargo.com/com/ (A)
- J.P. Morgan — Connect product page (accounts/payments/insights in one platform; deposit+loan+credit card+merchant accounts; offerings; video transcript with dashboard tiles and service-request states; ERP sync): https://www.jpmorgan.com/commercial-banking/connect (A)
- J.P. Morgan — Commercial Banking division page (segment; solutions incl. Credit and Financing; "Digital banking with Connect" summary): https://www.jpmorgan.com/commercial-banking (A)
- J.P. Morgan — Access product page ("global cash management platform"; connection options; fraud/entitlements; multi-bank balances; ERP/TMS embedding): https://www.jpmorgan.com/payments/solutions/access (A)
- HSBC — HSBCnet "About HSBCnet services" (full service catalog: accounts, reporting/admin, payments, self-service, cheques/deposits/positive pay, Global Payments Solutions, Global Trade Solutions incl. trade loans + receivables finance, liquidity portal, securities services, global markets, TMS/ERP alignment): https://www.hsbcnet.com/about-hsbcnet (A)
- ANZ — Transactive Global product page (suite incl. cash management, trade finance, loans, commercial cards, markets; features; security; mobile; help-center links): https://www.anz.com.au/institutional/transactive/ (A)
- ANZ — Digital Services Help, "Loans e-Statements Screen" (loan deals as servicable objects; statement generation steps; deal/borrower/interest/facility-transaction fields; user-permission gating): https://help.online.anz.com/hc/en-au/articles/51104299311001-Loans-e-Statements-Screen (A, Tier-1 help center)
- ANZ — Institutional & Corporate landing (three-tier structure personal/business/institutional; digital-services family incl. Fileactive host-to-host; help center + status page): https://www.anz.com.au/corporate/ (A)

Access failures (abandoned per network rules): CashPro ×2 this pass (see above). All other targets reached on first or second attempt.

**Sourcing limitation (applies to both output files):** all reachable surfaces are public product/solution pages plus one public bank help center (ANZ Digital Services Help). Logged-in portals, user guides, and operational manuals of the other banks were not accessible. Therefore **no precise operational facts** (cut-off times, numeric limits, default entitlements, approval counts, file-format specs beyond named standards) are asserted anywhere; vendor-published scale figures (countries, currencies, revenue bands) are recorded as vendor-published claims, not verified facts.

---

## Product Observations

### Wells Fargo — Vantage (Commercial Banking division platform)

Layer A. Fetched: /com/vantage, /com/.

- Positioning: "Wells Fargo Vantage® delivers the ultimate banking experience through a modernized platform…"; FAQ: "**Vantage is the next generation digital platform for treasury management banking transforming and replacing CEO**. Both CEO and Vantage are available during the migration; however, we encourage using Vantage as CEO will be phased out." → the platform is the successor of a long-running predecessor (CEO = Commercial Electronic Office), i.e., a generational replacement inside one bank.
- Persona-driven design: "dynamic, persona-driven experience tailored to business clients' unique needs, including industry, size, operational context, and lifecycle."
- Dashboard: "easy view and access to account balances, pending tasks, recent transactions, reporting and fraud managing tools."
- Task list (video transcript — the platform's own enumeration of daily banking tasks): "Review and approve payments / Process exceptions / **Manage company users** / **Sign documents** / View balances / **Paydown loans** / View transaction detail / Transfer money / Create wires / **Create FX payments**."
- Self-servicing: "reset your password, update your contact information, or submit servicing requests."
- Onboarding/authority: "To log into Wells Fargo Vantage, you will need to speak to a Wells Fargo representative. **Your company admin is responsible for the initial set up for you to have access**."
- Mobile app: view balances, deposit checks, approve payments; biometric sign-on; mobile token replaces RSA SecurID tokens.
- Division context (from /com/ hub): Commercial Banking serves "commercial businesses with annual revenues ranging from $25 million to $2 billion" (vendor-published claim). Division solution families: Asset Based Lending, Floor Plan Financing, Commercial Loans and Lines of Credit, **Global Payments and Liquidity** ("treasury management solutions"), Equipment Financing, Renewable Energy and Environmental Finance, Global Receivables and Trade Finance, Strategic Capital; industry coverage (healthcare, franchise, technology, government, food & agribusiness, higher education, auto dealerships, beverage, oil & gas, commodity finance, financial sponsors).
- Reading: the platform is the digital surface of the commercial banking relationship; its own task list mixes treasury tasks (wires, transfers, FX payments) with relationship tasks (paydown loans, sign documents, manage company users).

### J.P. Morgan — Connect (Commercial Banking division platform)

Layer A. Fetched: /commercial-banking/connect, /commercial-banking.

- Positioning: "Your accounts, payments and insights—all in one platform." Division summary: "**Manage your eligible deposit, loan, credit card and merchant services accounts all from one dashboard** in our digital banking platform."
- Dashboard tiles (video transcript, Accounts Overview): "**Bank accounts; Loans and lines of credit; Pending approvals; View authorized signers; Business insights**."
- Authority: "Control who sees what with **role-based permissions** and multifactor authentication."
- Servicing: "manage your company's **authorized signers** directly online. Add, view, or remove signers"; "**Account letters** — official account confirmation letters or payment instructions… generate them on demand"; "**Support requests** — submit a request for help with signing in, payment issues, unrecognized transactions" with trackable status sequence "Submitted → Assigned → In progress → Closed" and a dedicated Connect Service Center.
- Account opening: "our digital platform streamlines **accounts opening and management**… real-time updates throughout the process."
- Integration: "connect J.P. Morgan directly to your company's **ERP system**… verify and link a bank account within your business application, check balances and transaction history, all without visiting a separate banking portal"; Direct sync of account names/types/details, balances, transactions, rewards, statements.
- Payment capabilities: FX wires ("international payments in nearly 70 currencies" — vendor-published), **Payment Tracker** ("follow your payments from initiation to completion with real-time status updates… answer client questions and reconcile faster"), mobile banking (send payments, review balances, approve transactions).
- Fraud protection: "Monitor checks, **block unauthorized ACH debits** and **set approval thresholds** so you can catch exceptions."
- Attached commercial services: **Cashflow360** ("send invoices, approve payments and reconcile" — AP/AR platform), **Customer Insights** ("turn your card transaction data into clear views of your customers, sales and markets — included… with your J.P. Morgan card processing relationship").
- Segment (division page): midsize businesses, Innovation Economy (startups pre-seed→IPO), Commercial Real Estate; contact form asks revenue band (pre-revenue → over $2B) and intent (treasury services/payments & cash management, trade financing, equipment financing, term/line of credit business lending…).
- Contrast evidence: the same bank's nav separates "Commercial Banking" ("tailored credit, financing, treasury and payment solutions for businesses of all sizes and commercial real estate") from "Global Corporate Banking" ("financing, liquidity, payments, risk management and investment banking solutions").

### J.P. Morgan — Access (corporate treasury channel — contrast case)

Layer A. Fetched: /payments/solutions/access.

- Positioning: "**Access is a global cash management platform** available in 50+ countries, 120+ currencies and 10 languages (vendor-published)… One platform connects you to your payables and receivables needs through a single provider."
- Scope: "view real-time account balances, make payments and receive funds, **manage multi-bank cash balances**, report on and **forecast cash flow, manage liquidity by region or entity**."
- Connection options: "Online… Mobile… **Direct — APIs, File transmission, SWIFT**… or **embedded directly in your ERP/TMS**."
- Fraud/security: "layers of payment security and **user entitlements** with features like Payment Control and Manager."
- Self-service: 24/7/365 support; "Access resource center and built-in virtual assistant… to answer more than 375 request types" (vendor-published); AI cash-flow analytics/forecasting.
- Not observed: any lending/credit servicing surface on the product page. This is the pure treasury-operations channel of the same bank that also sells Connect to its commercial-banking division clients.
- Reading: banks may operate **two structurally different platforms for two different client tiers/divisions** — a corporate treasury channel (Access) and a commercial-relationship platform (Connect). The directory's "cash management platform" and "commercial banking platform" leaves therefore do not always map to the same product.

### HSBC — HSBCnet

Layer A. Fetched: hsbcnet.com/about-hsbcnet.

- Positioning: "a clear picture of your global banking all in one place… a comprehensive suite of flexible online financial solutions… real-time global account access and customisable setup features, you stay in control over the finances at every level of your organisation."
- Key features: "One easy-to-use consolidated interface that gives you comprehensive and global **cash management, trade and supply chain, securities, and global markets** solutions"; "keep track of your payments, receivables, liquidity, and the changing value of your assets"; multi-level end-to-end security; customisable workspace (local languages/time zones); "**no need to download software updates**" (centralised delivery — implies an installed-software predecessor era); desktop + mobile; "**Ability to align with your in-house Treasury Management Systems and Enterprise Resource Planning systems**."
- Accounts: Account Information (balances/statements, customisable views, print/export; initiate payment-related actions from the account view — payment creation, investigation, recall); Manage bank feeds (automated statement data to accounting software; HK/UK profiles); Term Deposits (view rates, create deposits and maturity instructions, enquire, authorise, amend); Virtual Account Management (virtual accounts "look, feel, and operate like physical bank accounts").
- Reporting: standard/custom reports (MT940, CSV); Automated File Delivery (scheduled); Custom Reports ("Report Writer"); **Administration Reports (for System Administrators)** — "your organisation's users, accounts, and permissions"; **Account Services Activity Log** ("audit trail of all activities performed by users within an organisation's HSBCnet profile… user permissions, payments, and File Upload"); Activity Log Query (administrative changes, sessions, deleted users).
- Payments and transfers: suite of global/regional payment types (Priority Payments, Inter-account Transfers, ACH, SEPA/SEPA Instant, File Upload, Bill/Tax payments, Bank-to-Bank, Direct Debits/Standing Orders); "you can **customise signing requirements**, confirm FX rates, save beneficiary details… track payment statuses, send advices… and be alerted"; "**Availability… subject to account location and user permissions**."
- Self-service and support: service requests via HSBCnet; Message Centre as inbox; real-time status updates; completed requests retained 90 days (vendor-published).
- Cheques and deposits: Cheque Images; Stop Cheques ("depending on your set up, **a second user may be required to approve** submissions"); Remote Deposit Capture; **Exception Management Positive Pay** ("matches cheques being presented… against a list of issued cheque records that your organisation has previously authorised… review, correct, accept, or reject exception items").
- Global Payments Solutions: Global Wallet, Omni Collect, Cash Flow Forecasting, **Treasury APIs**; **SmartServe** ("digital solution for your onboarding and account maintenance needs… open an account with us").
- **Global Trade Solutions**: "Documentary trade, Trade Loans, and Guarantees and Standby DCs. Initiate trade transactions and access real-time trade account information"; "access your **trade facilities**… Documentary credits, Trade Loans, DC advices, Export presentations, Guarantees…"; "Apply for Import DCs, guarantees, Standby DCs and make amendments online… saved templates and clauses"; import presentations accept/reject + settlement instructions; "**Apply for Trade Loans (Buyers or Sellers…) online to get financing**… upload supporting documents"; import/export loan applications online.
- **Receivables Finance**: "Manage your Receivables Finance facility… 24/7 self-service access. Easy **application and drawdown**; check facility availability with funds-in-use view; upload invoices, credit notes, cash allocation files; request drawdown; add a new buyer; facility management; collection performance view."
- Liquidity and investments: **Liquidity Management Portal** ("consolidated view of your cash position globally… self-manage your liquidity": dashboard, global liquidity solutions, investment self-service, cash-flow forecasting).
- Securities Services and Global Markets (HSBC Evolve execution platform — spots/forwards/swaps/options) reachable through/alongside HSBCnet.
- Reading: the single-platform pole — accounts + treasury + trade-credit (loans, facilities, drawdowns) + liquidity + markets under one profile, with organization-side administration (system admins, permissions, activity logs) and bank-side servicing (Message Centre) built in.

### ANZ — Transactive Global

Layer A. Fetched: /institutional/transactive/, /corporate/ (landing), help.online.anz.com article.

- Positioning: "Our intuitive, secure, and configurable digital banking platform designed for **institutional and large corporate** customers. Access a comprehensive suite of services in one place… including **cash management, trade finance, loans, commercial cards, markets, data insights** and more."
- Features: "**Visibility across global accounts** — all your accounts held with ANZ worldwide **and third-party banks**, with real-time data and reports"; "Flexible and intuitive reporting — comprehensive range of reports in multiple common formats that can be **scheduled and emailed**"; "**Control — integrated workflow options including approval frameworks and authorisation limits**"; "Foreign exchange services — create and manage a range of FX services"; "Streamlined transaction management — create, manage and approve transactions, including alerts and notifications"; "**Self-service… Service Requests, allowing you to initiate, track and manage a comprehensive range of operational servicing requests online**" (AU/NZ only); "**User access management — full control over your organisation's digital banking with self-service access to create and manage users, roles, product rules and approval workflows**"; "Data analytics on demand" (AU only).
- Mobile app: real-time/historical balances and transactions "including Commercial Cards billing entities"; "**Approve and reject Payments and Trade Finance transactions**"; dynamic FX rate; payment status/tracking; biometrics; service notifications.
- Security: Two-Factor Authentication; Security Devices (Token / ANZ Digital Key) "to securely log in… and approve transactions and administration activities"; "**Segregation of duties** prevents a single individual from performing all functions within the digital channel"; "**Approval discretion** limits for approving payments and restricting the transaction value users can authorise."
- What's new (evidence of living platform + geography gating): UI refresh; Confirmation of Payee (validate Australian account details); e-Statements (AUD history extended to five years; "e-Statements also now available for **Australian loan accounts**"); Transaction Analysis.
- Tier-1 help center (help.online.anz.com — Zendesk): category tree includes **Loans** → eStatements → "Loans e-Statements Screen": "electronic statements for **eligible Australian-domiciled loan deals**… generate statements from 1 October 2025 onwards… More reportable fields for richer loan data… Downloadable PDF statements… generate and download e-Statements directly from the **Loans menu**, choosing the date range… Select a deal or type in the deal number, name or currency… date range up to six months… sample loan e-Statement with details such as **Deal ID, currency & amount, interest, borrower details and transaction details for facility**… Loans e-statements can be downloaded for eligible deals that are assigned to **User Permissions**… Generate a **Facility Summary Report** from the Facility Summary screen."
- Platform family: ANZ operates a **family** of digital services for this tier — Transactive Global (main platform), **Fileactive** (host-to-host/API: "level up your organisation's treasury process"), Transactive - Trade, FX Online, e-Matching, Cashactive; "Not sure if ANZ Transactive Global is right for you? Take a look at our other **business banking options**" (explicit tier ladder); "Digital Service Status page" + help center + training webinars + security device user guide.
- Bank structure: personal / business / institutional & corporate as three separate site trees — the same three-tier customer model the business-banking-portal pass inferred for US banks, visible in one bank's own navigation.

---

## Cross-product Comparison

| Dimension | WF Vantage | JPM Connect | JPM Access | HSBCnet | ANZ Transactive Global |
|---|---|---|---|---|---|
| Operator = the bank itself (its commercial/corporate business) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Customer = organization acting through authorized users | ✓ | ✓ | ✓ | ✓ | ✓ |
| Organization-side user/authority administration | ✓ ("manage company users", company-admin setup) | ✓ (role-based permissions, authorized signers) | ✓ (user entitlements) | ✓ (system admins, admin reports, activity log, customise signing) | ✓ (users, roles, product rules, approval workflows) |
| Account visibility (balances, transactions, statements) | ✓ | ✓ | ✓ | ✓ | ✓ (incl. third-party banks) |
| Money-movement origination executed by the bank | ✓ (wires, transfers, FX payments) | ✓ (payments, FX wires) | ✓ (payables/receivables) | ✓ (priority/ACH/SEPA/files…) | ✓ (payments, trade finance transactions) |
| Approval machinery (workflows, limits, signers) | ✓ (review/approve, pending tasks) | ✓ (pending approvals, thresholds) | ✓ (entitlements, Payment Control/Manager) | ✓ (signing requirements, second-user approval) | ✓ (approval frameworks, authorisation limits, segregation of duties, discretion limits) |
| Reporting/data delivery incl. machine channels | reporting tools ✓ (direct file/API evidence not fetched this pass) | ✓ (ERP direct sync) | ✓ (APIs, file transmission, SWIFT, ERP/TMS) | ✓ (MT940/CSV, scheduled file delivery, Treasury APIs, TMS/ERP alignment) | ✓ (scheduled/emailed reports; Fileactive host-to-host sibling) |
| Outgoing-item fraud controls | ✓ (fraud managing tools, process exceptions) | ✓ (check monitoring, ACH blocks, thresholds) | ✓ (fraud support layers) | ✓ (Positive Pay exception management, stop cheques) | ✓ (Confirmation of Payee; security devices) |
| Servicing inside the platform (requests, signers, letters) | ✓ (self-servicing, sign documents) | ✓ (support requests w/ status, signers, account letters) | ✓ (resource center, virtual assistant) | ✓ (service requests, Message Centre) | ✓ (Service Requests; contact tools) |
| Mobile companion | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Credit relationship serviced in the platform** | ✓ (**paydown loans** as first-class task) | ✓ (**loans and lines of credit** tile; loans among managed account types) | ✗ not observed | ✓ (trade loans, import/export loan applications; receivables finance facility drawdowns) | ✓ (**Loans** menu, loan deals, loan e-statements w/ interest & facility transactions, Facility Summary) |
| Trade finance operations | division sells trade finance (platform surface not directly observed) | — (Cashflow360 covers AP/AR invoicing) | — | ✓ (documentary trade, DCs, guarantees, presentations) | ✓ (approve/reject trade finance transactions; Transactive - Trade sibling) |
| FX | ✓ (create FX payments) | ✓ (FX wires) | cross-currency via JPM Payments (not on product page) | ✓ (FX rate confirmation on payments; Evolve execution) | ✓ (FX services, dynamic rates) |
| Commercial cards | — (division context) | ✓ (credit card accounts; Customer Insights from card data) | — | — (cards not in fetched catalog) | ✓ (Commercial Cards billing entities in app) |
| Merchant services | — | ✓ (merchant services accounts; Customer Insights) | — | — | — |
| Markets/investments | — | — | — | ✓ (term deposits; liquidity investments; Evolve FX execution) | ✓ (markets in suite; FX Online sibling) |
| Liquidity structures views | ✓ (division sells liquidity; platform view not directly observed) | — | ✓ (liquidity by region/entity, multi-bank balances) | ✓ (Liquidity Management Portal) | — |
| Onboarding / signer administration | rep-led; company admin setup | ✓ (streamlined account opening; signers) | ✓ (streamlined onboarding) | ✓ (SmartServe digital onboarding) | — (not directly observed; device activation documented) |
| Segment emphasis | commercial (revenue $25M–$2B, vendor claim) | midsize / innovation economy / CRE | corporate/institutional treasury | corporate/institutional global | institutional & large corporate (AU/APAC) |

Layer-B commonalities (≥4 of 5, all directly observed per product): bank-operated channel; organization-as-customer; account visibility; bank-executed money movement; organization-controlled authority with approvals; reporting/data delivery; outgoing-item fraud controls; in-platform servicing; mobile companion.

Layer-A single-product and partial observations to keep calibrated: credit servicing is directly observed at 4 of 5 (absent only at Access, the deliberate treasury-channel contrast case); trade operations directly observed at 2 (HSBCnet, ANZ) plus division-level marketing at WF; merchant/card families directly observed only at JPM Connect / ANZ; markets/investments at HSBCnet / ANZ.

---

## Abstraction Hierarchy

### L0 — Defining Invariant (deliberately minimal)

A **Commercial Banking Platform** is a digital platform **operated by a bank** through which an **organization client** conducts its banking relationship with that bank. Removing any element below dissolves the Type:

```text
Bank as operator (the bank's own channel, not client-side software)
└── Organization as the served client (not a person-as-consumer)
    └── The organization's accounts held at the bank, exposed for visibility
        └── Money-movement origination by authorized organization users,
            executed by the bank
            └── Organization-controlled authority: per-user granted rights,
                approval machinery, administered by the organization itself
```

- **Bank-operated**: the platform belongs to the bank that holds the accounts and executes the money movement. Move the operator inside the corporate treasury department aggregating many banks → Treasury Management System.
- **Organization as client**: individuals act only as authorized representatives; there is no personal consumer relationship. Narrow the customer to a person → consumer digital banking / business banking portal (with the tier nuances below).
- **Account visibility + bank-executed money movement**: the records are the real accounts and facilities at the bank; the platform originates, the bank executes and posts.
- **Organization-controlled authority**: users, entitlements, and approvals are granted and administered under the organization's own authority (company admin / system administrators are a stable role across the sample).

Deliberately **not** in L0 (checked against the historical/market-sample rule): web or mobile surfaces (dial-up/file-era corporate banking platforms satisfy the core); machine-grade channels (files/APIs/SWIFT — a mature implementation posture, not the invariant); multi-entity/multi-currency portfolio scale (segment depth); the credit relationship, trade, FX, cards, markets (product-family breadth — see L1/L2); any specific rail or payment type.

### L1 — Common Mature Structure (standard in the current market, not definitional)

Present in nearly all sampled products with direct evidence:

- delegated user administration as a self-service organizational surface (users, roles, permissions, approval workflows)
- multi-rail payment origination (single + batch; domestic + cross-border) with approval chains and signing requirements
- consolidated reporting: statements, scheduled reports, machine formats, delivery to accounting/ERP (APIs, files, SWIFT, host-to-host siblings)
- outgoing-item fraud controls (positive-pay-style exception processing, payee confirmation, debit blocks)
- mobile companion (balances, approvals; check deposit where regional rails support it)
- in-platform servicing: service requests with status, authorized-signer management, document signing, account letters
- onboarding/account-opening support and self-service maintenance
- cash-position/liquidity views over the account portfolio

### L2 — Variant / Optional Structure (depends on tier, division, region, relationship)

- **credit-relationship servicing inside the platform**: loan/line accounts as visible objects (balances, deal/facility views, e-statements with interest and borrower details, paydowns/repayments, facility summary). Common across commercial-relationship platforms in the sample (4/5) but absent at the pure treasury-channel pole — and absent from pre-web platforms. Breadth discriminator vs the cash-management channel, but **not** definitional.
- trade finance operations (documentary credits, guarantees, presentations, trade loan applications)
- commercial card management and card-data insights
- merchant services account views
- markets/investments surfaces (term deposits, FX dealing/execution platforms)
- liquidity structures (concentration, pooling, virtual accounts) — the cash-management leaf's family
- industry/persona tailoring (persona-driven dashboards, industry segments)
- geography-gated feature sets (features vary by country/rail; regional confirmation-of-payee schemes)
- platform family vs single platform (some banks run one platform; others split by division/tier or operate sibling channels for trade, FX, host-to-host)

### L3 — Vendor-specific (research notes only; excluded from the final document)

- WF: Vantage persona model; microfrontends/APIs/AI/ML/GraphQL claims; CEO→Vantage migration and FAQ; mobile token replacing RSA SecurID; revenue band claim ($25M–$2B); division solution-family names.
- JPM: Connect tiles and service-request state sequence (Submitted→Assigned→In progress→Closed); "nearly 70 currencies" FX-wire claim; Cashflow360 (AP/AR); Customer Insights; Payment Tracker; Access stats (50+ countries, 120+ currencies, 10 languages, 375+ request types, virtual assistant); Payment Control and Manager; division taxonomy (Commercial Banking vs Global Corporate Banking).
- HSBC: MT940/CSV formats; 90-day Message Centre retention; 7-year cheque images; second-user approval on stop cheques; SmartServe; Treasury Solutions Group; HSBC Evolve and 450+ currency-pair claim; Bank-to-Bank Transfers; Manage bank feeds (HK/UK only).
- ANZ: Service Requests (AU/NZ only); Data Insights / Transaction Analysis (AU only); AUD e-statement five-year history; Loans e-Statements from 1 Oct 2025 with six-month date-range cap and deal-number lookup; security devices / ANZ Digital Key; Confirmation of Payee; Fileactive / Transactive Trade / FX Online / e-Matching product names; "Features by Geography" documentation pattern.
- Prior-pass vendor facts corroborating structure (not re-fetched this pass): CitiDirect scope/stats, CitiConnect, Digital Signer Management; WF Global Payments and Liquidity page details (from the cash-management-platform pass research notes).

---

## Vendor-specific Findings

See L3. The structurally interesting vendor-specific facts are:

1. **JPMorganChase operates two structurally different platforms for two client tiers**: Access (corporate treasury channel under the Payments organization) and Connect (commercial-banking-division platform spanning deposits, loans, credit cards, merchant services). This shows the "commercial banking platform" is not always the same product as the bank's "cash management platform".
2. **Wells Fargo's platform generation replacement** (CEO → Vantage, both live during migration) documents the Type's multi-generation history inside one bank.
3. **ANZ operates a platform family** (Transactive Global + Fileactive + Transactive Trade + FX Online + e-Matching) rather than a single platform, with an explicit ladder down to its business-banking options — segmentation by tier visible in one bank's own cross-links.
4. **HSBC's single-profile breadth** (accounts + treasury + trade credit + liquidity + securities + markets under one HSBCnet profile) is the maximal single-platform realization in the sample.

---

## Boundary Findings

| Neighboring Type | Seam | Test ("remove what → becomes the other Type") |
|---|---|---|
| Business Banking Portal (processed) | tier seam inside the same banks: owner-managed SMB self-service vs multi-user organizational operations with portfolio scale, machine-grade rails, and multi-family breadth. Confirmed again this pass: JPM and ANZ each sell separate platforms per tier (Access/Connect vs Chase business surfaces; Transactive Global vs "other business banking options") | narrow the customer to the owner-managed SMB tier and strip portfolio/rail machinery → business banking portal |
| Cash Management Platform (processed) | breadth/relationship seam: the treasury-operations channel **within** the commercial relationship vs the relationship container. In today's market the same product frequently fills both leaves (WF Vantage is the commercial division's treasury platform; HSBCnet spans both). JPM shows they can also be different products (Access ≠ Connect) | strip the non-treasury relationship families (credit, cards, merchant, trade) and keep account operations → cash management platform |
| Treasury Management System (unprocessed) | side seam: bank-operated channel over one bank relationship vs corporate-side software aggregating all banks + forecasting/debt/investment/hedging | move the operator from the bank to the corporate treasury department → TMS (the platforms' own words position ERP/TMS as the systems they feed and embed into) |
| Banking Back-office Platform (processed) | operator seam: customer-side origination vs bank-staff-side execution (validate→authorize→post/transmit) | move the operator from the organization to the bank → back-office platform |
| Commercial Loan Origination / Commercial Loan Management (unprocessed) | product seam: loan lifecycle systems (origination pipelines; servicing engines) vs the platform's loan-account visibility/servicing surface (balances, statements, paydowns). The platform surfaces the relationship; it does not run the loan book | deepen to full loan origination/servicing lifecycle → commercial loan management; flag for joint review when those leaves are processed |
| Mortgage Borrower Portal (unprocessed) | single-product servicing vs whole relationship | narrow the domain to one loan product → borrower portal |
| Payment Gateway / Payment Processing Platform (§08) | domain seam: merchant card-acceptance infrastructure vs corporate bank-account operations (merchant services appear only as attached account views) | remove the deposit-account relationship and bank rails → payment processing |
| Online Banking Portal / Mobile Banking Application / Digital Banking Application (unprocessed) | customer-type seam: person vs organization; consumer surfaces lack organization-controlled authority machinery | narrow the customer to a person → consumer digital banking |
| Liquidity Management Platform (unprocessed) | family seam (carried from the cash-management pass): liquidity structures are a service family inside the relationship | remove visibility+payments and keep only liquidity optimization → liquidity platform |

**Discharge of prior flags**: the business-banking-portal tier flag is confirmed held (two additional banks observed selling structurally separate tier platforms). The cash-management breadth flag is **partially discharged**: the seam is real at product level in at least one bank (JPM Access vs Connect), but in most banks the same product instantiates both directory leaves — recorded in STATUS.md for joint review rather than silently merged.

**Historical / market-sample check**: the definition survives without modern-market artifacts. (a) Generational evidence: WF's CEO→Vantage migration ("both available during the migration") shows the Type predates the current platform generation; HSBCnet's "no need to download software updates" and ANZ's separate host-to-host/file sibling (Fileactive) document the installed-software and file-transmission eras that preceded pure web delivery; SWIFT/file connectivity across the sample predates web portals. A dial-up/file-era corporate banking platform (balance reporting + payment files + supervisor approval) satisfies the L0 without web, mobile, credit modules, or multi-family breadth. (b) Regional check: an Australian institutional platform fits without US-specific rails; AU-only features are explicitly geography-gated ("Features by Geography"). (c) Credit-in-core test: fails the historical check (credit modules are a modern breadth phenomenon), so credit stays in the variant layer despite being today's most visible discriminator against the cash-management channel.

---

## Uncertainties

- CashPro (BofA) unverified after repeated access failures; BofA contributes named-only evidence. The sample therefore leans on four banks.
- Logged-in help centers of WF/JPM/HSBC were unreachable; operational precision (approval counts, cut-offs, limits, entitlement matrices) is unobserved and deliberately not asserted. The ANZ help center is the sample's only Tier-1 operational doc source; its geography-gated articles (AU/NZ) were used only for structure, not for generalizable numeric claims.
- Machine-grade channels at WF Vantage were not directly re-verified this pass (the division's treasury page was fetched in the prior pass; the Vantage page this pass shows interactive tasks only). Marked accordingly in the comparison table.
- Whether older platforms actually surfaced any credit information (e.g., via statements) is unknown; the historical check therefore keeps credit out of the defining core rather than asserting its historical absence or presence in detail.
- The exact boundary of "commercial banking" as a bank segment varies by bank (JPM: midsize/innovation-economy/CRE; WF: $25M–$2B revenue claim; ANZ: "institutional & corporate" merges what US banks split). The leaf is defined customer-type-first (organization client of a bank's non-consumer business) rather than by any bank's internal division names.
- Sibling leaves (treasury-management-system, liquidity-management-platform, commercial-loan-origination/management, consumer digital banking surfaces) are unprocessed; their seams here are drawn from this sample's evidence and should be revisited in joint review.

---

## Final Synthesis

A Commercial Banking Platform is the bank-operated digital platform through which an organization client conducts its banking relationship with that bank. Its defining core is small: the bank operates the channel; the customer is an organization whose individuals act under organization-granted authority; the organization's accounts at the bank are exposed for visibility; authorized users originate money movement that the bank executes; and the organization administers its own users' rights and approvals. Around this core, mature platforms add the operational machinery the commercial tier is sold on: self-service user/entitlement administration with approval frameworks and limits, multi-rail payment origination, consolidated reporting with machine-grade delivery (files, APIs, SWIFT, ERP embedding, host-to-host siblings), outgoing-item fraud controls, mobile companions, and in-platform servicing (service requests, signer management, documents). Beyond the treasury channel, the modern commercial-relationship platform typically spans further product families of the same relationship — credit facilities surfaced as servicable accounts (balances, e-statements, paydowns), trade finance operations, commercial cards, merchant services, FX, and sometimes markets — with the exact breadth varying by bank division, tier, and region. The Type is bounded by: below, the business banking portal (owner-managed SMB tier of the same banks); within, the cash-management channel (the treasury-operations slice that in many banks is the same product, in some banks a separate one); beside, the corporate-side TMS; on the other side of the login, the bank-staff back-office; and at the edges, the loan-lifecycle systems, payment-acceptance infrastructure, and consumer surfaces that handle what this platform only surfaces. The market's own structure — banks selling separate tier platforms, operating platform families, and replacing platform generations in place — is evidence that the invariant is the operated banking relationship itself, not any particular module, rail, or era.
