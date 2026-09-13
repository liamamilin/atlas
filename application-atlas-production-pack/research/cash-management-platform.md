# Research Notes — Cash Management Platform

Research date: 2026-09-07
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (internal only — not referenced in the final document)

## Research Goal

Understand what a **Cash Management Platform** actually is as an Application Type. The directory places it in §08 between Treasury Management System and Liquidity Management Platform, next to Commercial Banking Platform. The working hypothesis from the processed sibling `business-banking-portal`: this leaf is the **corporate tier platform** that banks operate as a structurally separate product from their SMB business-banking portals (BofA CashPro vs Business Advantage 360; J.P. Morgan Access vs Chase Business Online; Wells Fargo Vantage/CEO vs Business Online). Establish the stable core, separate it from the SMB portal (tier seam), from the corporate-side treasury software (side seam), and from the broader commercial-banking relationship platform (breadth seam).

## Initial Boundary (pre-research hypothesis)

- What it likely is: a bank-operated digital platform through which an organization's treasury function sees consolidated visibility of its bank-held accounts, originates money movement at scale across multiple rails, and accesses liquidity and information services — with machine-grade connectivity (files/APIs/SWIFT) as a first-class channel.
- Likely confusions:
  1. Business Banking Portal (processed) — same bank, lower tier; per-user self-service vs treasury-grade machinery.
  2. Treasury Management System (unprocessed) — corporate-side software over all banks vs bank-operated channel over one bank relationship.
  3. Commercial Banking Platform (unprocessed) — whole relationship (credit + services) vs treasury-operations channel.
  4. Liquidity Management Platform (unprocessed) — liquidity machinery as a service family inside cash management vs a standalone Type.
  5. Payment Gateway / Payment Processing (§08) — merchant card acceptance vs corporate bank-account operations.
- Unknowns going in: whether liquidity structuring (sweeps/pooling/virtual accounts) is definitional or a service family; whether machine-grade access is definitional or just common; how strong the entitlement/approval model is; whether the operator must be a bank.

## Research Questions

1. Who operates the platform — the bank, or the corporate? What exactly is operated?
2. What is the account model — single bank vs multi-bank; entity/currency/country structure of the account portfolio?
3. What visibility surfaces exist (balances, statements, reporting, export formats, multibank data)?
4. What payment machinery exists (rails, templates, bulk/file input, approval chains, tracking, FX)?
5. What liquidity machinery exists (concentration/sweeps, pooling, virtual accounts, real-time liquidity, investments)?
6. What receivables machinery exists (remote deposit, positive pay, receivables files, bill management)?
7. What integration machinery exists (host-to-host/file, APIs, SWIFT, ERP/TMS embedding)?
8. What entitlement/approval model exists at treasury scale (user administration, signing requirements, payment controls)?
9. What fraud controls attach (positive pay, ACH filters, account validation)?
10. Where are the seams: SMB portal (tier), TMS (side), commercial banking platform (breadth), liquidity platform (family)?
11. Historical/regional check: do legacy (dial-up/file/token) and modern (API/mobile) products fit one definition?

## Representative Products

| Product | Bank | Segment focus | Geography | Product philosophy | Evidence quality |
|---|---|---|---|---|---|
| CitiDirect (+ Citi Services solution family) | Citi | global corporates & institutions (vendor-published: 90K+ organizations, 90+ markets, 194 currencies) | global | global transaction-services network; one-click global workflow; CitiConnect files+API integration layer | strong (platform page + liquidity + payments + platform-services pages) |
| HSBCnet (+ HSBC Global Payments Solutions) | HSBC | corporates & institutions, multi-country | global | consolidated single interface for cash, trade, securities, markets; deep self-service reporting; explicit TMS/ERP alignment | strong (about-services page is a full service catalog) |
| J.P. Morgan Access | J.P. Morgan | corporates (vendor-published: 50+ countries, 120+ currencies, 10 languages) | global | self-described "global cash management platform"; connection-option flexibility (online/mobile/direct: APIs, files, SWIFT); ERP/TMS embedding | strong (dedicated Access product page + liquidity solutions page) |
| Wells Fargo Vantage + Global Payments & Liquidity | Wells Fargo | US commercial middle market (bank-published revenue band $25M–$2B) | US-centric | next-gen "treasury management banking" platform (Vantage, replacing CEO) + a structured treasury product family (payables/receivables/liquidity/fraud/information reporting) | strong (Vantage page + Global Payments & Liquidity page) |
| CashPro (named only) | Bank of America | corporate treasury | global | (not directly researched — see access failures) | named-only: BofA's own small-business tier taxonomy (observed 2026-09-06 in the business-banking-portal pass) lists CashPro Online as the separate corporate platform |

Sample covers four global transaction-banking franchises across three US banks and one UK/Asia-global bank, one US middle-market-weighted product, and one named-only cross-reference. Two connection philosophies (portal-first vs connection-option-first), one platform-generation migration (CEO→Vantage) observable in flight.

## Sources

All fetched 2026-09-07. Evidence layers: **A** = directly observed on official pages of that product; **B** = cross-product commonality; **C** = canonical inference.

- Citi — Services overview (business lines incl. Liquidity Management Services, Payments, Platform and Data Services): https://www.citigroup.com/global → https://services.citi.com/ (A)
- Citi — Platform and Data Services (CitiDirect, CitiConnect, Digital Onboarding, Billing & Statements): https://services.citi.com/solutions/platform-and-data-services (A)
- Citi — CitiDirect product page (scope, stats, how-we-help, mobile, security): https://www.citidirect.com/cdhome (A)
- Citi — Liquidity Management Services (concentration, notional pooling, virtual accounts, CitiDirect Cash Concentration, deposits, online investments, real-time liquidity): https://services.citi.com/solutions/liquidity-management-services (A)
- Citi — Payments (domestic, cross-border WorldLink, clearing, commercial/virtual cards, BaaS): https://services.citi.com/solutions/payments (A)
- HSBC — HSBCnet homepage: https://www.hsbcnet.com/ (A)
- HSBC — About HSBCnet services (full service catalog: accounts, reporting, payments, self-service, cheques/deposits, GPS, trade, liquidity portal, securities, markets): https://www.hsbcnet.com/about-hsbcnet (A)
- J.P. Morgan — Payments hub (APAC page; solution families; Payment Control Center mention): https://www.jpmorgan.com/payments (A)
- J.P. Morgan — Liquidity Solutions (Connected Cash, cash concentration, sweeps, deposits/overdrafts, ERP/TMS/accounting integration): https://www.jpmorgan.com/payments/solutions/treasury/liquidity (A)
- J.P. Morgan — Access product page ("global cash management platform"; connection options; fraud/entitlements; multi-bank balances; ERP/TMS embedding): https://www.jpmorgan.com/payments/solutions/access (A)
- Wells Fargo — Commercial Banking hub (Vantage sign-on; Global Payments and Liquidity entry): https://www.wellsfargo.com/com/ (A)
- Wells Fargo — Vantage platform page (persona-driven design; dashboard; task list; mobile app; CEO→Vantage FAQ; company-admin setup): https://www.wellsfargo.com/com/vantage (A)
- Wells Fargo — Global Payments and Liquidity (payables single-file from ERP; instant payments RTP/FedNow; APIs/sandbox; consolidated/integrated receivables; bill management; liquidity/pooling; fraud services; treasury information reporting; file transmission; SWIFT SCORE/Lite): https://www.wellsfargo.com/com/solutions/global-payments-liquidity/ (A)

Access failures (abandoned per network rules after 1–2 attempts per source):
- CashPro: https://cashpro.bankofamerica.com/ transport error ×1; https://www.cashpro.bankofamerica.com/ transport error ×1; https://www.bankofamerica.com/commercial/ 404 ×1 → CashPro contributes named-only evidence (from BofA's own tier-taxonomy page observed in the 2026-09-06 business-banking-portal pass).
- J.P. Morgan Access first guesses 404 ×2 (jpmorgan.com/technology/access; /solutions/treasury/payments/access) before the correct URL was located via the Liquidity page's related-solutions link.
- Wells Fargo /com/ceo/ 404 ×1 (portal rebranded Vantage; correct pages located via /com/).

Sourcing limitation: all reachable official surfaces are public product/solution pages. Logged-in help centers, user guides, and operational manuals were not accessible. Therefore **no precise operational facts** (cut-off times, numeric limits, default settings, file-format specifications beyond named standards, entitlement matrices) are asserted anywhere. Vendor-published scale figures (markets/currencies/organizations) are recorded here as vendor-published claims and are not treated as verified operational facts.

## Product Observations

### Citi — CitiDirect + Citi Services solution family

Evidence layer A.

- Positioning: Citi's Services business line spans Liquidity Management Services, Payments, Trade & Working Capital, Platform and Data Services, Investor Services, Issuer Services — "cash management, payments & receivables solutions, working capital solutions… across Citi's global network."
- CitiDirect: "Citi's next-generation, award-winning online banking platform… one-click access to global transaction capabilities using an intuitive and user-centric workflow… helps you manage accounts, payments, receivables, liquidity, trade, foreign exchange, and global reporting, and supports numerous transaction types across the globe… across multiple geographies, subsidiaries, and currencies." Vendor-published scale: 90+ markets, 194 foreign currencies, 90K+ organizations.
- Make Payments: "payment templates and saved beneficiary details."
- Liquidity services (family): Cash Concentration ("automated physical cash concentration, based on your timing, amount, and desired frequency… in-country, cross-border, cross-currency, and on a multi-bank basis"); Notional Pooling ("virtually aggregate credit and debit balances… into a single net amount… without commingling of funds"); Virtual Accounts ("streamline accounts to centralize cash while providing user group-level payments, reporting, reconciliation, and tracking"); **CitiDirect Cash Concentration** ("dynamically view, manage, and change structures in CitiDirect, featuring 24/7 access to global structures" — liquidity structures are self-service objects inside the platform); Real-time Liquidity Management ("sharing available balances or moving funds in near real-time across accounts"); Deposits (~90 markets/85 currencies vendor-published); Online Investments (money market funds and time deposits via secure portal).
- Payments family: Domestic Payments (ACH and wires in 90 markets, direct membership in local clearing schemes); Cross-Border (WorldLink — pay to accounts, cards, wallets from a single account); Clearing (24/7 USD Clearing); Commercial Cards; Virtual Cards (single-use/limited-use numbers); BaaS (subproducts: Virtual Account, Payer ID). Vendor-published: 10M instant-payment transactions daily average; 130+ currencies with integrated FX.
- Integration: CitiConnect ("supports global file standards such as ISO 20022 XML… one-window connectivity… from CitiConnect for Files to CitiConnect API. Straight-through processing and straight-through reconciliation"); API Developer Portal (developer.citi.com); vendor-published 11B+ API calls YTD.
- Digital Onboarding: open accounts and manage product documentation online (49 countries vendor-published); **Digital Signer Management** — "update account signatories digitally by deleting, adding or amending authorized signers directly in CitiDirect… in real time" (44 countries vendor-published).
- Billing & Statements: "up-to-date reporting of balances and transaction postings via Account Statements to support your cash reconciliation needs."
- Tracking/inquiry: Payment Advisor ("up-to-the-minute payment status for Funds Transfer activity… any party in the payment chain can check the status of a single transaction"); Trade Advisor; Citi Inquiry Resolution Portal (CIRP).
- AML: banks have a mandatory duty to collect/verify identity documents for "each person who authorizes payment transactions on an account held in an AML regulated country"; otherwise "your ability to process those transactions may be restricted or removed."
- Mobile: CitiDirect Mobile App — "manage payments, account balances, user access and more"; Mobile Token; biometric authentication.

### HSBC — HSBCnet

Evidence layer A.

- Positioning: "Gain total visibility of your global finances, trade transactions and FX positions with HSBCnet… a clear picture of your global banking all in one place… a comprehensive suite of flexible online financial solutions… to help you increase productivity and manage your cash flow. With real-time global account access and customisable setup features, you stay in control over the finances at every level of your organisation."
- Key features: "One easy-to-use consolidated interface that gives you comprehensive and global cash management, trade and supply chain, securities, and global markets solutions"; "keep track of your payments, receivables, liquidity, and the changing value of your assets"; flexible reporting; multi-level end-to-end security; customisable workspace (local languages/time zones); centrally-delivered enhancements (no local software updates); desktop + mobile; **"Ability to align with your in-house Treasury Management Systems and Enterprise Resource Planning systems."**
- Accounts: Account Information (balance and statement information, customisable views, print/export in various formats; initiate payment-related actions from the account view — payment creation, investigation, recall); Manage bank feeds (automated statement data delivered to accounting software; HK/UK profiles only); Term Deposits (view rates, create deposits and maturity instructions, enquire, authorise, amend); **Virtual Account Management** ("reduce the number of physical accounts… centralising transaction processing. Virtual accounts look, feel, and operate like physical bank accounts — you can access balances and transactions, as well as produce statements").
- Reporting: Reports and Files Download (standardised or custom reports; **Swift MT940** and CSV formats; filters); Automated File Delivery (scheduled delivery at pre-determined times); Create and Manage Custom Reports ("Report Writer"); Administration Reports (users, accounts, permissions — real-time, PDF/XLS/CSV); **Account Services Activity Log** ("audit trail of all activities performed by users within an organisation's HSBCnet profile… retains historical data… user permissions, payments, and File Upload"); Activity Log Query (administrative changes, session usage, deleted users).
- Payments and transfers: "online suite of global and regional payment types… pay with accounts domiciled around the world through many global and domestic payment options. In addition to creating and submitting your payment instructions, you can **customise signing requirements**, confirm FX rates, save beneficiary details, track payment statuses, send advices to stakeholders, and be alerted on payment activities." Types: Priority Payments (wires, domestic/international, real-time FX); Inter-account Transfers (between HSBC accounts on the same profile anywhere in the world); ACH Payments (domestic, single/multiple beneficiaries, high-volume/batch); Eurozone-SEPA Credit Transfers (+ SEPA Instant where available); **File Upload** (payment files); Bill Payments and Tax/statutory payments; Bank to Bank Transfers (for financial institutions); Direct Debits and Standing Orders (UK). "Availability… subject to account location and user permissions."
- Self-service and support: service requests via HSBCnet; Message Centre as the inbox for requests; real-time status updates; completed requests retained 90 days (vendor-published).
- Cheques and deposits: Cheque Images (US accounts, 7 years vendor-published); Stop Cheques ("depending on your set up, a second user may be required to approve submissions before the local cut-off time"); Remote Deposit Capture (UK/US); **Exception Management Positive Pay** ("matches cheques being presented for payment against a list of issued cheque records that your organisation has previously authorised… and submitted to us"; review/correct/accept/reject exception items same day).
- Global Payments Solutions (through HSBCnet): Global Wallet, HSBC Omni Collect, Cash Flow Forecasting, **Treasury APIs**; Treasury Solutions Group; SmartServe (digital onboarding/account maintenance).
- Liquidity and investments: **HSBC Liquidity Management Portal** — "a consolidated view of your cash position globally… tools to help you self-manage your liquidity": Liquidity Management Dashboard; Global Liquidity Solutions; Liquidity Investment Solutions self-service; Cash Flow Forecasting.
- Trade solutions (documentary trade, trade loans, guarantees; templates and clauses; import presentations), Receivables Finance (facility management, drawdown, invoice upload).
- Securities Services and Global Markets (HSBC Evolve execution platform) also reachable through HSBCnet.

### J.P. Morgan — Access

Evidence layer A.

- Positioning (bank's own words): "Access is a **global cash management platform** available in 50+ countries, 120+ currencies and 10 languages… One platform connects you to your payables and receivables needs through a single provider, with robust security and controls needed to help protect your business." Also: "a suite of digital, end-to-end solutions that helps you manage your business and working capital. With a range of connection options, Access can be tailored to your business's exact needs."
- Benefits: self-service tools and support 24/7/365; "advanced fraud support — layers of payment security and **user entitlements** with features like **Payment Control and Manager**"; "cash flow visibility — leverage transaction data and AI to support cash flow analytics and short-to-midterm forecasting."
- Connection options: **Online** ("manage your global treasury needs virtually through a single platform — whether it's cash management, customized pay-ins for clients or reporting and reconciliation"); **Mobile** ("check balances, review payments and manage your liquidity on the go"); **Direct** ("connect to Access in the following ways, including: APIs, File transmission, SWIFT").
- Video transcript (official): "view real-time account balances, make payments and receive funds, **manage multi-bank cash balances**, report on and forecast cash flow, **manage liquidity by region or entity**… Connect using online banking, Developer Portal, or SWIFT via APIs and file transmission — or **embedded directly in your ERP/TMS**." Virtual assistant "built for online treasury management to answer more than 375 request types" (vendor-published).
- Liquidity solutions family (separate page): Connected Cash ("real-time liquidity positioning, self-service features and forecasting… 24x7 flexibility, visibility and control… integrates across mobile, desktop and third party systems"); Cash concentration ("move funds globally on the same day"); Deposits and overdrafts; **Sweeps** ("achieve real-time cash positioning through API sweep execution"); benefits list: gain visibility; streamline data ("integrating with enterprise resource planning, treasury management and accounting software"); automate cash management (invoicing, payments, reconciliation); enhance cash-flow forecasting (integrated forecasting tools aggregating financial data).
- Related: Account Solutions, Payments Solutions, Cross-Currency FX (vendor-published: send 120 currencies, receive 40, 200+ countries), Third-party money, Kinexys (blockchain). Payment Control Center named in fraud-insights video ("spot suspicious payments before they clear").
- Recognition: Coalition Greenwich "Best Bank for Corporate Cash Management" (vendor-published award).

### Wells Fargo — Vantage + Global Payments and Liquidity

Evidence layer A.

- Vantage positioning: "the next generation digital banking platform, delivering a dynamic, persona-driven experience tailored to business clients' unique needs, including industry, size, operational context, and lifecycle." Dashboard: "easy view and access to account balances, pending tasks, recent transactions, reporting and fraud managing tools." Web↔mobile continuity; self-service (password reset, contact info, servicing requests).
- Vantage task list (official video): review and approve payments; process exceptions; manage company users; sign documents; view balances; paydown loans; view transaction detail; transfer money; create wires; create FX payments.
- Vantage mobile app: view balances, deposit checks, approve payments; biometric authentication; mobile token replaces RSA SecurID.
- FAQ: "Is Wells Fargo Vantage the same as Wells Fargo CEO? Yes, Vantage is the next generation digital platform for **treasury management banking** transforming and replacing CEO." Onboarding: "To log into Wells Fargo Vantage, you will need to speak to a Wells Fargo representative. **Your company admin is responsible for the initial set up** for you to have access to Vantage."
- Global Payments and Liquidity (the treasury product family served through the platform):
  - Payables: consolidated payable service ("transmission of a **single file containing multiple payment types and remittance information directly from an ERP or accounts payable system to the bank**. Additionally, all payments can be reviewed and approved through our online banking system"); instant payments (24/7/365; API channel with intelligent routing across RTP/FedNow); Payments APIs (developer portal Wells Fargo Gateway; documentation; **sandbox**); commercial and virtual card solutions.
  - Receivables: consolidated receivables ("automatically post cash receipts to your ERP… using our consolidated cash receipts file"); integrated receivables ("send us a file of your open invoices; we reassociate with remittance detail before sending a cash application file back to your ERP"); bill management (e-invoice, reminders, ACH collection, accounting sync, auto-reconciliation); global invoice payments (international customers pay in local currencies; auto-reconciled with invoices).
  - Liquidity: deposits ("cash forecasting tools and pooling arrangements to intercompany loans"); liquidity management ("ensuring sufficient funds… minimizing the risk-adjusted costs of financing").
  - Fraud: account validation services (real-time account ownership/status screening); ACH Fraud Filter (pay-or-return decisions, auto-stop unauthorized transactions); Fraud Manager (access ACH Fraud Filter, Positive Pay "through our online banking platform"); Payment Authorization (limits on check cashing); Perfect Receivables (proxy account numbers to route incoming ACH/wire); Positive Pay with payee validation (match presented checks against the check issue file).
  - Information reporting & data services: treasury information reporting ("real-time transaction alerts, **multibank reporting**, and multicurrency reporting… through the Wells Fargo Vantage portal"); file transmission services; global payments information messaging (**SWIFT**: SCORE membership model, SwiftNet interface software, cloud-based SWIFT Alliance Lite); data and reporting APIs; Vantage as the online banking platform.
  - Solutions tiers: Business Essentials (ACH/wires/checks/desktop deposit; fraud tools; visibility: transaction and image search, alerts, statements & notices, express balance information reporting, ACH NOC Returns Reports); Bill Manager (syncs QuickBooks, Xero, NetSuite, Intacct; automatic reconciliation).
- Segment: commercial businesses "with annual revenues ranging from $25 million to $2 billion" (bank-published).

### Bank of America — CashPro (named only)

No direct fetch succeeded (see access failures). Named evidence from BofA's own site (observed 2026-09-06, business-banking-portal pass): BofA's small-business tier taxonomy lists "CashPro Online" as the corporate-tier platform alongside Business Advantage 360, under "Complex Solutions" with liquidity/payables/receivables management. Used only as evidence that the tier structure exists at a fifth bank; no capability claims.

## Cross-product Comparison

| Capability | CitiDirect (Citi) | HSBCnet (HSBC) | J.P. Morgan Access (JPM) | WF Vantage + GPL (WF) |
|---|---|---|---|---|
| Bank-operated platform over the bank relationship | Yes (A) | Yes (A) | Yes (A) | Yes (A) |
| Organization as customer; treasury/multi-entity scope | "multiple geographies, subsidiaries, and currencies" (A) | "every level of your organisation" (A) | "manage liquidity by region or entity" (A) | commercial segment, multi-account (A) |
| Consolidated account visibility (balances/statements) | Yes — accounts + statements for reconciliation (A) | Yes — Account Information, custom views, export (A) | Yes — real-time account balances (A) | Yes — dashboard + express balance reporting (A) |
| Multi-currency / multi-country | 194 currencies, 90+ markets (vendor-published) (A) | accounts domiciled around the world (A) | 120+ currencies, 50+ countries (vendor-published) (A) | multicurrency reporting (A) |
| Payment origination, multiple rails | payments + templates + saved beneficiaries (A) | priority/ACH/SEPA/inter-account/bill/tax/bank-to-bank/direct debit (A) | make payments (A) | ACH/wires/checks/instant RTP-FedNow (A) |
| Bulk/file payment input | CitiConnect for Files (A) | File Upload (A) | File transmission (A) | single consolidated file from ERP/AP (A) |
| API connectivity | CitiConnect API + developer portal (A) | Treasury APIs (A) | APIs + Developer Portal (A) | Payments APIs + Gateway portal + sandbox (A) |
| SWIFT connectivity | ISO 20022 via CitiConnect (A) | MT940 report format (A) | SWIFT as a connection option (A) | SCORE, SwiftNet, Alliance Lite (A) |
| Signing/approval/entitlements | Digital Signer Management; AML per-authorizer identity (A) | customise signing requirements; second-user approval (stop cheques); user permissions gate payment types (A) | user entitlements; Payment Control and Manager (A) | review and approve payments; company admin manages users; payment authorization limits (A) |
| Liquidity machinery | concentration / notional pooling / virtual accounts / real-time liquidity; self-service structure management in CitiDirect (A) | Virtual Account Management; Liquidity Management Portal (dashboard/solutions/investments/forecasting) (A) | cash concentration; sweeps (API execution); Connected Cash real-time positioning (A) | pooling arrangements; intercompany loans; cash forecasting tools (A) |
| Receivables machinery | receivables management (named) (A) | RDC; cheque images; Positive Pay exception management; Omni Collect (A) | receive funds; pay-ins (A) | consolidated/integrated receivables files to ERP; bill management; global invoice payments; proxy accounts (A) |
| Fraud controls | not directly observed on fetched pages | Positive Pay + Exception Management (A) | Payment Control and Manager; layered security (A) | Positive Pay w/ payee validation; ACH Fraud Filter; account validation; payment authorization (A) |
| Reporting/export | customized reports (A) | MT940/CSV; scheduled delivery; custom reports; admin reports; activity log (A) | reporting and reconciliation; AI forecasting (A) | real-time alerts; multibank; multicurrency; file transmission (A) |
| ERP/TMS integration | CitiConnect STP into "your technology suite" (A) | "align with your in-house TMS and ERP" (A) | "embedded directly in your ERP/TMS" (A) | single file from ERP; cash receipts file back to ERP (A) |
| Mobile companion | CitiDirect Mobile (payments, balances, user access; token; biometrics) (A) | HSBCnet Mobile (A) | Mobile (balances, payments, liquidity) (A) | Vantage app (balances, deposit checks, approvals; biometrics; mobile token) (A) |
| Self-service servicing | CIRP inquiry portal (A) | Message Centre service requests (A) | virtual assistant; 24/7/365 support (A) | self-service password/contact/servicing requests (A) |
| Deposits/investments | Online Investments (MMFs, time deposits) (A) | Term Deposits (create/authorise/amend) (A) | deposits and overdrafts (A) | deposits (A) |
| Trade/working capital attached | trade, LCs, supply chain finance (A) | trade solutions; receivables finance (A) | via Payments family (A) | separate trade/receivables solution family (A) |
| Bank's own naming | "cash management, payments & receivables solutions" (A) | "global cash management… solutions" (A) | "global cash management platform" (A) | "treasury management banking" platform (A) |

Reading of the comparison:

- The four products agree on a channel structure: bank-operated platform; consolidated visibility over a multi-account/multi-currency portfolio; payment origination across many rails with interactive + bulk/file + API + SWIFT access; organization-controlled entitlements/approvals. (B)
- Liquidity machinery is present in all four but takes different shapes (self-service structure management at Citi; a dedicated liquidity portal at HSBC; API sweeps at JPM; advisory-led pooling at WF) — a service family, not one uniform structure. (B)
- Fraud controls are strong where observed (HSBC, JPM, WF) but were not directly observed at Citi on fetched pages — kept product-attributed. (A, product-specific gaps recorded)
- Machine-grade access (file/API/SWIFT) is universal in the sample and is the bank platforms' answer to ERP/TMS integration; the TMS/ERP appears as the *other* system in every product's own words. (B)
- Segment span: WF explicitly serves the middle market ($25M–$2B revenue) with the same platform family; the global three serve large multinationals. The Type spans mid-market to global corporate. (B)

## Canonical Model

### Level 0 — Defining Invariant

The smallest structure without which the product is no longer recognizable as a Cash Management Platform:

```text
Bank-operated platform over an organization's bank-held accounts
(the account portfolio: many accounts across entities, currencies, countries)
├── Consolidated cash visibility over that portfolio
│   (balances, transactions, statements — exportable/integrable)
├── Money-movement origination that the bank executes
│   (multiple rails; interactive AND machine-grade channels —
│    bulk file and/or API, beyond interactive UI entry)
└── Organization-controlled authority over who may act and approve
    (per-user entitlements / signing requirements under the
     organization's own administration)
```

Four properties. Remove any one and the Type dissolves:

- **Bank-operated, over the bank's own records of the organization's accounts** — the platform is the bank's channel, and the objects are the accounts the organization holds at that bank. Remove this (the system moves inside the corporate, aggregating many banks) → Treasury Management System.
- **Consolidated cash visibility across the portfolio** — balances, transactions, statements across many accounts/entities/currencies, in forms that can be exported or machine-delivered. Remove this → a pure payment initiation tool.
- **Money-movement origination executed by the bank, at portfolio scale** — the organization instructs; the bank executes on real accounts and real rails; bulk/file or API input is a first-class channel alongside the UI. Remove the machine-grade channel and the portfolio scale → a business banking portal.
- **Organization-controlled authority** — the organization (not the bank alone) administers who may see, originate, and approve, per user. Remove this → the platform cannot represent an organization's treasury and degenerates into a personal banking surface.

Deliberately **not** in Level 0 (tested and demoted):

- **Liquidity structuring (sweeps, pooling, virtual accounts)** — present in all sampled products but as a *service family* with different shapes (self-service structures, portal dashboards, API sweeps, advisory-led arrangements). A platform with visibility + payments + authority at portfolio scale is still recognizably a cash management platform without any particular liquidity structure; and liquidity structures are frequently bank-configured services surfaced through the platform rather than platform-native objects. Also kept out to avoid collision with the sibling leaf Liquidity Management Platform.
- **Receivables machinery, fraud controls, specific report formats** — common mature structure, not definitional.
- **Any specific rail mix** (ACH/wire/SEPA/check/instant) — regional variant.

### Level 1 — Common Mature Structure

Present across the sampled products; not required for recognition:

- **Liquidity service family** — cash concentration/sweeps (automated movement of funds between accounts on schedules or triggers), notional pooling (virtual netting of balances without commingling), virtual accounts (non-physical sub-accounts that behave like accounts for payments/reporting/reconciliation), real-time liquidity positioning, and short-term investment of surplus (term deposits, money-market funds) surfaced through the platform.
- **Receivables machinery** — remote deposit capture, cheque images, positive-pay matching with exception decisioning, consolidated/integrated cash-receipts files posted back to the corporate ERP, bill presentation/collection, proxy account numbers for incoming payment routing.
- **Fraud controls on outgoing and incoming items** — positive pay (with payee validation), ACH debit filters/blocklists, account validation screening, payment authorization limits, exception-processing queues inside the platform.
- **Reporting and data delivery** — standardized statement/report formats (e.g., MT940, CSV), scheduled/automated file delivery, custom report builders, administration reports, and audit/activity logs of user actions.
- **Payment operations tooling** — templates, saved beneficiaries, payment status tracking, payment advices, alerts, FX rate confirmation on cross-currency payments, payment investigation/recall from the account view.
- **Entitlement administration by the organization** — company administrators create/modify users, grant account- and function-level rights, set signing requirements/approval chains; admin reports and activity logs expose the entitlement state.
- **Mobile companion** — balances, payment review/approval, sometimes deposit capture; token/biometric authentication.
- **Self-service servicing** — service-request channels with message centers/inquiry portals; virtual assistants; 24/7 support postures.
- **Onboarding and account administration** — digital account opening, document management, digital signer/signatory management.
- **Deposits and short-term investments** — term deposits with create/authorise/amend flows; money-market fund access.

### Level 2 — Variant / Optional Structure

Depends on segment, geography, bank scale, era:

- **Segment tier** — middle-market commercial (one sampled bank publishes a $25M–$2B revenue band) vs global corporate/institutional; same platform family, different depth.
- **Connection philosophy** — portal-first (one consolidated interface for cash + trade + securities + markets) vs connection-option-first (online/mobile/direct as equal citizens, ERP/TMS embedding as a headline capability).
- **Rail mix** — US (ACH/wire/check/instant RTP-FedNow), EU (SEPA/instant), UK (direct debits/standing orders), regional clearing schemes; ISO 20022 migration posture.
- **Breadth of attached families** — trade & working capital, securities services, global markets/FX execution, commercial/virtual cards, banking-as-a-service — present in some products, absent or separate in others.
- **Security posture** — physical tokens → mobile tokens → biometrics; per-market AML identity verification duties for payment authorizers.
- **Platform generation** — legacy portals being replaced by modernized platforms in flight (CEO→Vantage), with both live during migration.
- **AI/analytics layer** — AI-assisted cash-flow analytics/forecasting, virtual assistants (era-common, depth varies).

### Level 3 — Vendor-specific Structure (research notes only)

- Citi: CitiDirect (platform), CitiConnect for Files / CitiConnect API, WorldLink Payment Services (cross-border to accounts/cards/wallets from a single account), CitiDirect Cash Concentration (self-service structure management), Digital Signer Management, Payment Advisor / Trade Advisor / CIRP, Spring by Citi (ecommerce acceptance), Citi Token Services, 24/7 USD Clearing; vendor-published figures (90+ markets, 194 currencies, 90K+ organizations, ~$2T monthly physical pooling flows, 10M instant transactions/day, 11B+ API calls YTD).
- HSBC: HSBCnet (platform), Report Writer, Manage bank feeds (HK/UK only), Global Wallet, HSBC Omni Collect, SmartServe onboarding, Treasury Solutions Group, HSBC Evolve (markets execution), Liquidity Management Portal naming; 90-day message retention and 7-year cheque images (vendor-published).
- J.P. Morgan: Access (platform), Connected Cash, Payment Control and Manager / Payment Control Center, Access resource center + virtual assistant (375+ request types, vendor-published), Kinexys (blockchain), Developer Portal; vendor-published figures (50+ countries, 120+ currencies, 10 languages; FX send 120/receive 40 across 200+ countries).
- Wells Fargo: Vantage (platform, replacing CEO/Commercial Electronic Office), Wells Fargo Gateway (developer portal), Perfect Receivables (proxy account numbers), Bill Manager (QuickBooks/Xero/NetSuite/Intacct sync), Business Essentials tier, ACH NOC Returns Reports, SWIFT SCORE/Lite posture; bank-published segment band ($25M–$2B revenue) and "one in seven cross-border transactions globally" claim.
- Bank of America: CashPro Online as the corporate platform (named only; capabilities not verified).

## Historical / Market-Sample Check

- Would older products fit L0? Yes. The pre-web corporate banking channel (dial-up balance reporting files, bulk payment files, bank-configured ZBA sweeps, paper signing arrangements backed by bank-recorded authority) satisfies all four L0 properties: bank-operated, consolidated reporting, file-grade origination, organization-controlled authority. The sampled CEO→Vantage migration shows the same core surviving a full platform-generation change: the FAQ explicitly says Vantage "is the next generation digital platform for treasury management banking transforming and replacing CEO."
- Would regional products fit? Yes. US check/ACH/positive-pay machinery, UK direct-debit/standing-order machinery, and SEPA machinery are all rail-level differences (L2). HSBCnet's catalog explicitly varies "by country/region" while the platform identity stays constant.
- Does L0 over-fit the modern API era? No — L0 requires machine-grade access *or* interactive origination at portfolio scale with the organization controlling authority; the file-based legacy posture satisfies "machine-grade" via bulk files. What L0 does require is that origination is not limited to one-person interactive entry over a handful of accounts — that shape is the business banking portal.
- Single-bank vs multi-bank: the sampled platforms are bank-operated over that bank's accounts, but JPM Access advertises "manage multi-bank cash balances" and WF advertises "multibank reporting" — i.e., the bank platform aggregates *data* about accounts at other banks while executing *money movement* on its own. L0 stays at "bank-operated over the organization's accounts at that bank"; multi-bank data aggregation is L1/L2. The fully bank-agnostic corporate hub (operated by a non-bank over many banks) is treated as the TMS-side seam, not this Type.

## Vendor-specific Findings

See Level 3. Additional structural observations:

- All four banks sell the corporate tier as a structurally separate platform from their SMB business portals (BofA: CashPro vs Business Advantage 360; JPM: Access vs Chase Business Online; WF: Vantage vs Business Online; Citi: CitiDirect vs CitiBusiness; HSBC: HSBCnet vs business banking). This confirms the tier seam recorded by the business-banking-portal pass.
- Every product's own words place the corporate TMS/ERP *outside* the platform: HSBCnet "align[s] with your in-house Treasury Management Systems and ERP"; JPM Access is "embedded directly in your ERP/TMS"; WF ships files "directly from an ERP or accounts payable system to the bank" and posts receipts "back to your ERP"; Citi integrates "with your technology suite." The platform is the bank-side endpoint of that integration, not the treasury system itself.
- Liquidity structures straddle the platform/service line: Citi lets clients "dynamically view, manage, and change structures in CitiDirect" (platform-native self-service), while WF describes pooling/intercompany-loan strategies implemented with treasurers (advisory-led). Both shapes exist in the market.

## Boundary Findings

| Neighboring Type | Seam | Test ("remove what → becomes the other Type") |
|---|---|---|
| Business Banking Portal (processed) | tier seam inside the same banks: SMB self-service payments + per-user entitlements vs treasury-grade portfolio operations + machine-grade rails | scale the account portfolio up, add bulk/file/API origination and treasury service families → Cash Management Platform; scale down → business banking portal |
| Treasury Management System (unprocessed) | side seam: bank-operated channel over one bank relationship vs corporate-side software aggregating all banks and adding forecasting/debt/investment/hedging | move the operator from the bank to the corporate treasury department → TMS; the bank platform's own words position the TMS/ERP as the system it feeds and embeds into |
| Commercial Banking Platform (unprocessed) | breadth seam: whole commercial relationship (credit, lending, industry services) vs the treasury-operations channel within it | strip credit/lending and keep account operations → cash management platform; the channel is often the digital surface *of* the commercial platform |
| Liquidity Management Platform (unprocessed) | family seam: liquidity structures (concentration/pooling/virtual accounts) are a service family sold through cash-management platforms; a standalone liquidity leaf likely means corporate-side liquidity analytics or MMF investment portals | remove visibility+payments and keep only liquidity optimization → liquidity platform |
| Payment Gateway / Payment Processing Platform (§08) | domain seam: corporate bank-account operations vs merchant card-acceptance infrastructure | remove the deposit-account relationship and bank rails → payment processing; ecommerce acceptance (e.g., Spring by Citi) and commercial cards sit adjacent, not core |
| Banking Back-office Platform (processed) | operator seam: customer-side origination vs bank-staff-side execution (validate→authorize→post/transmit) | move the operator from the organization to the bank → back-office platform |
| Payment Orchestration Platform (§08) | merchant-side multi-PSP routing vs bank-rail corporate payments | replace bank accounts/rails with PSPs and checkout semantics → orchestration |
| Digital Banking Application / Online Banking Portal (§08, unprocessed) | customer-type seam: person vs organization; consumer surfaces lack portfolio-scale operations and entitlement administration | narrow the customer to a person → consumer digital banking |

Naming collision noted: "cash management" also names consumer brokerage sweep products ("cash management accounts"). Those are banking overlays on brokerage relationships (already recorded in the brokerage-platform pass) and are not this Type.

## Uncertainties

- CashPro capabilities unverified (access failures); BofA contributes tier-structure evidence only.
- Citi's fraud-control surface was not directly observed on fetched pages; fraud machinery is asserted as common from HSBC/JPM/WF evidence, with Citi's gap recorded.
- All sources are public product/solution pages; logged-in help centers were unreachable. No precise operational facts (cut-off times, limits, default entitlements, format specifications) are asserted in either file.
- Vendor-published scale figures (markets/currencies/organizations/flows) are marketing claims; recorded as such, not treated as verified facts.
- The exact shape of the sibling leaves (treasury-management-system, liquidity-management-platform, commercial-banking-platform) is unprocessed; the seams here are drawn from this sample's evidence and should be revisited in joint review when those leaves are processed.
- Whether "Liquidity Management Platform" as a directory leaf will resolve to the bank-side liquidity service family, a corporate-side analytics product, or an MMF investment portal is unknown; flagged for joint review.

## Final Synthesis

A Cash Management Platform is the bank-operated corporate platform through which an organization's treasury function operates its account portfolio at that bank: it sees consolidated cash visibility across many accounts, entities, currencies and countries; it originates money movement that the bank executes across multiple rails, through interactive surfaces and machine-grade channels (bulk files, APIs, SWIFT) that integrate with the corporate's ERP/TMS; and it administers, under the organization's own authority, who may see, originate, and approve. Around this core, mature platforms surface the bank's treasury service families — liquidity structures (concentration, sweeps, pooling, virtual accounts, short-term investment), receivables machinery (remote deposit, positive pay, receivables files back to the ERP), outgoing/incoming fraud controls, reporting and data delivery in standard formats, payment operations tooling, mobile companions, self-service servicing, and digital onboarding/signer management — with trade, securities, markets, cards and BaaS attached variably. The Type is bounded by four seams: below it, the business banking portal (SMB self-service tier of the same banks); beside it, the corporate-side Treasury Management System (which the platform feeds and embeds into); around it, the Commercial Banking Platform (the broader relationship whose treasury channel this is); and within it, the liquidity service family (which the sibling Liquidity Management Platform leaf must be reviewed against). L0 stays at: bank-operated platform + portfolio-scale consolidated visibility + bank-executed money movement via interactive and machine-grade channels + organization-controlled authority.
