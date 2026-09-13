# Research Notes — Business Banking Portal

Research date: 2026-09-06
Methodology: WORKFLOW_v1.1 / WRITING_GUIDE_v1.1 (internal only — not referenced in the final document)

## Research Goal

Understand what a **Business Banking Portal** actually is as an Application Type: a bank-operated digital channel through which a business customer's authorized people access and operate the business's bank accounts. Establish the stable core structure, separate it from the consumer online-banking portal and from the corporate/commercial (cash-management) tier, and identify what is common vs vendor/region-specific.

## Initial Boundary (pre-research hypothesis)

- What it likely is: the bank's customer-facing web/mobile channel for business customers (SMB → lower mid-market), providing account visibility, money movement, delegated user access, and business-relevant self-service.
- Likely confusions:
  1. Consumer Online Banking Portal / Mobile Banking Application (person as customer).
  2. Commercial Banking Platform / Cash Management Platform (corporate tier; banks usually sell these as separate products).
  3. Banking Back-office Platform (bank staff-side; already processed leaf documents validate→authorize→execute on the bank side).
  4. Generic "Customer Portal" (support/self-service semantics, not bank-account semantics).
- Unknowns going in: how strong the entitlement/approval machinery is across the market; where the SMB portal ends and the corporate platform begins; whether the directory's surface-defined consumer siblings (online-banking-portal, mobile-banking-application) can be cleanly separated by the customer-type test.

## Research Questions

1. How is the business customer represented — organization vs the individuals who use the portal on its behalf?
2. What account types and views are exposed (balances, pending/posted transactions, statements, cheque/check images)?
3. What money-movement capabilities exist (internal transfers, external transfers, wires, bill pay, batch/file payments, international/FX, direct debit, receivables)?
4. How is access controlled — user administration, per-user entitlements, roles, authorization limits, multi-step approval (maker–checker), audit?
5. What differs structurally from consumer online banking?
6. Where is the seam to the corporate cash-management platform — different Type or tier?
7. Regional shapes: US (check/ACH/wire/RDC-centric), UK (mobile-first, faster payments, tax integrations), AU (BPAY/ABA direct-entry, token-based security)?
8. What ancillary modules attach (remote deposit capture, card management, merchant services, payroll, accounting sync, invoicing, fraud controls such as check monitoring/ACH debit block)?
9. Historical/regional check: do legacy (token/file-based) and digital-native (mobile-first) products fit one definition?

## Representative Products

| Product | Bank | Segment focus | Geography | Product philosophy | Evidence quality |
|---|---|---|---|---|---|
| Business Advantage 360 (Small Business Online Banking) | Bank of America | SMB (bank defines "up to $1M revenue") | US | incumbent full-service portal + separate corporate platform (CashPro) | strong (feature pages + FAQ + account-management pages) |
| Chase Business Online | Chase (JPMorgan Chase) | small business | US | incumbent portal + Payment Center + fraud services; corporate tier spun to J.P. Morgan Commercial Banking | good (product + fraud-services pages) |
| Wells Fargo Business Online | Wells Fargo | small business | US | incumbent portal; corporate tier separate (/com/ Commercial Banking) | moderate (product + transfer-pay pages; entitlement admin not directly observed) |
| CommBiz (+ NetBank contrast) | Commonwealth Bank of Australia | businesses with multiple staff (vs NetBank for owner-managed sole traders) | AU | legacy-heavy business banking with formal authority model (tokens, ABA files, Electronic Account Authority) | strong (product + explicit NetBank-vs-CommBiz comparison) |
| Starling Bank business accounts | Starling Bank (UK digital bank) | SMEs + sole traders (separate account products) | UK | mobile-first digital-native; web banking as companion | moderate (product pages; help center JS-gated) |

Sample covers: three US incumbents, one Asia-Pacific incumbent with an explicit intra-bank tier split, one European digital-native. Two tiers of business customer (owner-managed vs multi-staff) and three regional rails regimes.

## Sources

All fetched 2026-09-06. Evidence layers: **A** = directly observed on official pages of that product; **B** = cross-product commonality; **C** = canonical inference.

- Bank of America — Business Advantage 360 / Small Business Online Banking: https://www.bankofamerica.com/smallbusiness/online-banking/ (A)
- Bank of America — Account Access FAQs: https://www.bankofamerica.com/smallbusiness/online-banking/faqs/account-access/ (A)
- Bank of America — Account Management / Account Permissions: https://www.bankofamerica.com/smallbusiness/online-banking/account-management.go (A)
- Bank of America — Small Business digital tools taxonomy: https://www.bankofamerica.com/smallbusiness/online-banking/features.go (A; page renders as small-business hub)
- Chase — Online Business Banking: https://www.chase.com/business/online-banking (A)
- Chase — Fraud and Security Services: https://www.chase.com/business/banking/services/fraud-security-services (A)
- Wells Fargo — Business Banking hub: https://www.wellsfargo.com/biz/ (A)
- Wells Fargo — Business Online: https://www.wellsfargo.com/biz/online-banking/ (A)
- Wells Fargo — Transfer and Pay: https://www.wellsfargo.com/biz/online-banking/transfer-pay/index (A)
- CommBank — CommBiz: https://www.commbank.com.au/business/online-banking/commbiz.html (A)
- CommBank — Compare NetBank and CommBiz: https://www.commbank.com.au/business/online-banking/compare-netbank-and-commbiz.html (A)
- Starling Bank — Business banking: https://www.starlingbank.com/business/ (A, product pages)
- Starling Bank — help centre: https://help.starlingbank.com/business/ — **unreachable (JS-gated app shell)** → Starling claims kept at product-page strength; no operational details asserted for Starling.

Access failures (abandoned after 1–2 attempts per network rules): Mercury help center (help.mercury.com — JS shell ×1, root also JS-gated ×1); Tide help (tide.co/help 404 ×1); Wells Fargo /business-banking/online-banking/ (404 ×1, replaced by /biz/ URLs).

## Product Observations

### Bank of America — Business Advantage 360 (Small Business Online Banking)

Evidence layer A.

- Positioning: "Get convenient, secure account access" for small business; separate logins expose the tier structure: Business Advantage 360 (small business) vs **CashPro Online** (corporate treasury platform) vs Merchant Reporting vs Business Investing.
- Account visibility: real-time balance information and pending transactions; 12 months of sortable online transactions; view check and deposit slips online; 18 months of online checking/savings statements; paperless option.
- Account scope: manage checking, savings, CDs, loans, lines of credit and credit cards; can view all linked BofA accounts across states.
- Money movement: one-time or recurring electronic payments and checks to companies and individuals (bill pay); receive eBills; wires same-day / transfers next-day or third-business-day inside or outside the US ("you control the speed"); transfers to/from accounts at other financial institutions.
- Alerts: automatic email/text alerts on conditions (insufficient funds, irregular card/account activity, credit-limit thresholds).
- Self-service account requests: check and deposit slip reorder, check stop payment.
- Accounting: automatic sync with QuickBooks Online; download transactions for QuickBooks Desktop.
- Business credit: free access to Dun & Bradstreet business credit scores (visibility surface).
- **Shared access (Account Management / Account Permissions)**: "Allow trusted employees or an accountant to manage routine business banking tasks"; establish individual account access levels; control user activity with unique individual IDs; additional users created with varying levels of account access who can make payments on behalf of the business; merchant-services access granular (virtual terminal view-only or full access; full-access employees can manage other employees' permissions); owner and sub-user demo tracks exist.
- Identity/profile structure (FAQ): enrollment creates a User ID; accounts linked to the User ID are accessible; **sole proprietors (SSN as Tax ID) may link business + personal under one ID; non-sole-proprietors cannot mix personal and business under the same User ID**; multiple User IDs per business; profiles can be *linked* for cross-viewing (up to 10 small-business profiles + 1 consumer profile) while remaining separate; transfers between linked profiles use explicit "Send to other Bank of America accounts" or wires.
- Cash management attachments: Remote Deposit Online (deposit checks remotely), merchant services, payroll (self-service or full-service; ADP / QuickBooks Online Payroll integrations).
- Tier taxonomy visible on bank site: Small Businesses (up to $1M revenue) → Midsize ($1M–$50M) → Commercial & Corporations ($50M+); "Basic Solutions" vs "Complex Solutions" (CashPro, Global Card Access, liquidity/payables/receivables management) — the corporate tier is a separate platform, not this portal.

### Chase — Chase Business Online

Evidence layer A.

- Positioning: "Easily manage your small business account anytime, from anywhere"; web portal (Chase Business Online) + Chase Mobile app companion.
- Portal headline features: enroll in and access **Fraud Protection Services**; **Payment Center** — "compare all payment options, choose what's right for your business and make digital payments"; **Access & Security Manager** — "Assign account permissions and delegate cash management activities to your team."
- Mobile companion: check deposit (QuickDeposit), payments including Zelle and wires; accept card payments on mobile for eligible accounts.
- Fraud Protection Services (separate but reached from the portal): Check Monitoring (set a review amount; get notified of outgoing checks at/above it; decision checks on a dashboard), Check Protection (criteria per check; mismatched checks require review; unreviewed checks not posted past cut-off), ACH Debit Block (block all ACH debits or whitelist who may debit). Account-tier eligibility applies.
- Tier structure: Chase for Business (small/mid) vs J.P. Morgan Commercial Banking (large corporations, midsize, innovation-economy startups) — separate site/platform.

### Wells Fargo — Business Online

Evidence layer A (product pages; the entitlement-admin surface was **not** directly observed in fetched pages).

- Positioning: "secure online access to your accounts through your desktop and mobile devices."
- Transfer and Pay capabilities enumerated: Transfers (between WF business accounts and accounts at other US financial institutions); Wires (set up recipients, send wires, view history; international); Business Bill Pay ("decide when and how paying bills works best for your business"); Payroll services (via ADP — third-party); Direct Pay (pay employees/contractors/vendors with control over invoices); Zelle (get paid by customers / pay vendors); Merchant Services (accept card payments; settlement to a business deposit account).
- Self-service "find it fast": transfer money, make a bill payment, activate debit card, stop payment on a check.
- Security Center: manage security alerts, sign-on features; Online Access Agreement governs terms.
- Account tiers on the bank side: Initiate/Navigate/Optimize business checking — Optimize includes treasury management services; Commercial Banking and Corporate & Investment Banking are separate divisions with separate portals.
- Enroll/sign-on flows with username/password/passkey.

### Commonwealth Bank of Australia — CommBiz (vs NetBank)

Evidence layer A. The bank publishes an explicit comparison between its consumer-style portal (NetBank) and its business portal (CommBiz) — the single most boundary-revealing source in the sample.

- Positioning: CommBiz = "Online banking for businesses with an eligible CommBank account"; "Best suited to businesses whose finances are managed by **multiple employees**." NetBank = "For smaller businesses whose finances are managed by the **business owner**"; "manage your business and personal finances in one place." Sole traders are pointed at NetBank.
- Eligible products: business transaction accounts, business loans, credit cards (excluding corporate cards), foreign-currency accounts, asset finance, contingent liability facility, term deposit.
- Access control: customisable user access and permissions; assign user permissions and duties; custom user permissions (e.g., view only); **custom authorisation limits**; **multi-level custom Electronic Account Authority** (transaction authorisation rules); built-in transaction approval workflow; "Electronic Account Authorisers … requiring multiple approvers"; authorised signatories/cardholders get access if added as CommBiz Authoriser; two-to-sign payments: "Authoriser can log on to approve at their convenience" (vs NetBank: both signatories must act together); user auditing and reporting built in.
- Money movement: transfers, BPAY, international money transfers; import payment files (ABA format; also BPAY); payables and receivables templates; direct debit facility; international payments + FX (IPFX: spot, forward exchange contracts); trade finance (CommBiz Global Trade: import and trade advance transactions); no transaction limits (vs NetBank daily limits).
- Visibility: transaction history 25 months (vs 24 in NetBank); online statements up to 7 years for transaction accounts/credit cards; **cheque images viewable**; merchant statements; BPAY biller reports; corporate card facility management (view transactions/statements and manage the facility, e.g., add new cardholders).
- Security: two-factor authentication for logon and payment protection — physical security token or eToken on the mobile app (vs NetBank's SMS/app NetCode); fraud and scams monitoring.
- Mobile companion (CommBiz Mobile): authorise payments, view balances, transfer between linked accounts, pay contacts — approval-capable mobile surface.
- Insights/attachments: Daily IQ (cash-flow insights, customer demographics/spending behaviour), investments (cash deposit account), 24/7 helpdesk.

### Starling Bank — business accounts (UK digital-native)

Evidence layer A at product-page strength only (help center unreachable).

- Two account products: Business current account ("from start-ups to established limited companies") and a separate **Sole trader account** ("sole traders, freelancers and landlords") — the segment split is expressed through account products rather than separate portals.
- Services surfaced: built-in accounting ("banking, bookkeeping and tax… one clear view of your cash flow"), Making Tax Digital (record and report income tax/expenses to HMRC from the account), free invoicing tools, VAT returns (paid tier), Tap to Pay on mobile, multi-currency accounts (manage multiple currencies in one app), Business Marketplace integrations (Xero, Penfold, SumUp), online banking "on your laptop" (web companion), mobile app as primary surface.
- UK-regulated bank (PRA/FCA); FSCS protection noted.

## Cross-product Comparison

| Capability | BofA BA360 | Chase Business Online | Wells Fargo Business Online | CommBiz (AU) | Starling (UK) |
|---|---|---|---|---|---|
| Bank-held business accounts as the object of the portal | Yes (A) | Yes (A) | Yes (A) | Yes (A) | Yes (A) |
| Authorized individuals act for the organization (per-user identity) | Yes — unique individual IDs, sub-users (A) | Yes — team delegation via Access & Security Manager (A) | implied, not directly observed | Yes — per-user permissions/duties (A) | not directly observed (help JS-gated) |
| Balances + transaction history + statements | Yes; 12mo transactions, 18mo statements (A) | Yes (A) | Yes (A) | Yes; 25mo history, 7yr statements, cheque images (A) | Yes (A, product-page level) |
| Internal + external transfers | Yes (A) | Yes (A) | Yes (A) | Yes (A) | Yes (A, product-page level) |
| Wire / international payments | Yes (A) | Yes (A) | Yes (A) | Yes — IPFX, spot/forwards (A) | multi-currency accounts (A) |
| Bill pay to companies/individuals | Yes, recurring (A) | Yes — Payment Center (A) | Yes — Business Bill Pay (A) | Yes — BPAY (regional equivalent) (A) | invoicing/payments tooling (different shape) (A) |
| Batch/file payment import | — | — | — | Yes — ABA file import, payables/receivables templates (A) | — |
| Direct debit / receivables machinery | — | — | — | Yes (A) | — |
| User administration with per-user entitlements | Yes — Account Management (A) | Yes — Access & Security Manager (A) | not directly observed | Yes — core positioning (A) | unverified |
| Approval workflow / authorisation limits | via access levels; payments on behalf (A) | delegation of cash-management activities (A) | not directly observed | Yes — Electronic Account Authority, multiple approvers, custom limits (A) | unverified |
| Fraud controls on outgoing items | — (cash-management tier in corporate platform) | Yes — check monitoring/protection, ACH debit block (A) | — | fraud & scams monitoring (A) | — |
| Check deposit (remote/mobile) | Yes — Remote Deposit Online (A) | Yes — QuickDeposit (A) | Yes (mobile app) (A) | cheque images view; deposit not emphasized | — |
| Card management (debit/corporate cards) | manage credit cards (A) | debit card services (A) | activate debit card, replace card (A) | manage corporate cards, add cardholders, issue PINs (A) | — |
| Self-service maintenance (stop payment, reorder checks) | Yes (A) | — | Yes (A) | — | — |
| Accounting integration (QuickBooks/Xero sync) | QuickBooks Online sync / Desktop download (A) | — | — | — | Xero integration, built-in accounting (A) |
| Merchant services / accept payments | Yes (A) | Yes (A) | Yes (A) | merchant statements; terminals (A) | Tap to Pay (A) |
| Payroll | Yes — ADP/QBO payroll (A) | Yes — payroll (A) | Yes — via ADP (A) | — | — |
| Invoicing / tax tooling | — | invoicing (merchant side) (A) | — | — | invoicing, MTD, VAT (A) |
| Separate corporate-tier platform owned by same bank | CashPro (A) | J.P. Morgan Commercial Banking (A) | Commercial Banking /com/ (A) | Institutional banking split (site nav) (A) | n/a (bank has no corporate tier surfaced) |
| Owner-managed single-user alternative offered | sole-proprietor linking rule (A) | — | — | NetBank explicitly positioned for sole traders (A) | separate sole-trader account product (A) |

## Canonical Model

### Level 0 — Defining Invariant

The smallest structure without which the product is no longer recognizable as a business banking portal:

```text
Bank-held accounts of an organization (the business customer)
└── accessed digitally by identified individuals authorized to act for the organization
    ├── visibility over those accounts (balances, transaction history)
    ├── origination of money-movement instructions from those accounts
    └── per-user granted access rights (who may see/do what is controlled,
        under the organization's authority)
```

Five properties. Remove any one and the Type dissolves:

- **Organization as the bank's customer** — the accounts belong to a business entity. Remove this → consumer online banking.
- **Authorized individuals, not anonymous users and not bank staff** — the people using the portal are the business's own authorized representatives with their own credentials. Remove this (bank staff operate everything) → bank back-office platform.
- **Account visibility** — balances and transaction history of the business's accounts. Remove this → a pure payment initiation tool, not a banking portal.
- **Money-movement origination** — the portal exists to let the business act on its money remotely, not merely look. Remove this → a statement viewer.
- **Granted, per-user access rights** — access to accounts and actions is granted to specific people under the organization's authority (even if trivially one person). Remove this — everyone can do everything with no authorization structure — the product stops being able to represent an organization and becomes a personal banking surface.

Level 0 is deliberately small. Multi-user self-administration, approval chains, and limits are **not** in Level 0: a one-person business portal satisfies the Type without them.

### Level 1 — Common Mature Structure

Present in most mature products sampled; not required for recognition:

- **User administration by the customer** — an owner/administrator creates additional portal users (employees, accountants), assigns account-level and function-level rights, and revokes access.
- **Approval workflow** — initiated payments can require authorization by other entitled users before execution; custom authorization limits; approvers can act remotely (not physically co-present).
- **Payee/recipient management** — stored recipients for wires, bill pay, transfers; templates.
- **Multiple payment rails behind one surface** — internal transfers, external transfers, wires, bill pay; rail mix varies by region.
- **Statements and documents** — online statements, transaction search/export, check/cheque images where checks exist.
- **Alerts** — balance/activity/payment notifications.
- **Mobile companion app** — deposit checks (RDC), approve payments, view balances.
- **Self-service account maintenance** — stop payment, check/deposit-slip reorder, card activation/replacement, contact updates.
- **Audit trail of user activity** — who did what, surfaced for the business and for the bank's security.
- **Accounting interoperability** — export or live sync with bookkeeping software.
- **Fraud controls for outgoing items** — check monitoring/protection (positive-pay family), ACH debit block/allowlists (US-shaped; regional equivalents).
- **Card management** — debit card lifecycle; corporate/business card facility administration where cards exist.

### Level 2 — Variant / Optional Structure

Depends on segment, geography, bank scale, deployment era:

- **Segment tier inside one bank** — owner-managed sole-trader mode served either by the consumer portal (NetBank case), a separate account product (Starling sole trader), or a linking rule inside the business portal (BofA sole-proprietor rule); multi-staff mode is the portal's center of gravity.
- **Corporate extension** — the same bank typically operates a second, larger-scale platform for mid-market/corporate customers (cash management, liquidity, file-based payables/receivables at scale, ERP-grade integrations). Where the boundary sits varies; small-bank markets may merge the tiers.
- **Regional rail mix** — US: ACH/wire/check/RDC, bill pay centers; AU: BPAY, ABA direct-entry files, direct debit facilities; UK: app-first banking, faster payments, tax-tooling (MTD/VAT), accounting integrations.
- **Security posture** — physical/electronic tokens and payment-protected 2FA (legacy/global posture) vs app-based auth (digital-native posture).
- **Attached business services** — payroll, merchant services/acquiring views, invoicing, business credit-score visibility, FX/trade modules, lending views (loans, lines, credit cards in one place).
- **Form factor emphasis** — desktop portal-first (incumbents) vs mobile app-first with web companion (digital-native).
- **Data/insight add-ons** — cash-flow analytics, customer spending insights.

### Level 3 — Vendor-specific Structure (research notes only)

- BofA: profile-linking machinery (link up to 10 small-business profiles + 1 consumer profile; linked profiles remain separate; explicit cross-profile transfer mode); Remote Deposit Online; Cash Flow Monitor; free D&B business credit scores.
- Chase: named services — Access & Security Manager, Payment Center, QuickDeposit; Fraud Protection Services mechanics (review-amount thresholds, decision dashboards, cut-off-time non-posting rule; Check Monitoring vs Check Protection mutual exclusivity per account; tier-eligibility of check protection/ACH debit block to higher checking tiers).
- Wells Fargo: Direct Pay (per-payment fees enumerated on page); Digital Wires enrollment eligibility; Optimize checking's treasury-management attachment.
- CommBiz: IPFX (spot/forward FX), CommBiz Global Trade, Daily IQ, eToken/physical token regime, ABA/BPAY file import, "Electronic Account Authority" terminology, merchant terminal statements, cash deposit account investments.
- NetBank (CommBank): daily transfer/international limits with stated figures (research-only; numbers are vendor-specific and changeable), NetCode SMS/app 2FA, transfer-group templates, "merchant statements for sole traders/sole director companies only".
- Starling: award badges/claims, Engine by Starling (banking-as-a-service arm), B2B banking services.

## Historical / Market-Sample Check

- Would older products fit L0? Yes. Token-and-file-based business banking (CommBiz retains ABA file import, physical tokens, formal Electronic Account Authority — a living legacy posture) satisfies L0 with no modern convenience required. Pre-web PC/dial-up corporate banking channels also fit: bank-held organization accounts, authorized users, visibility, payment origination, granted access rights.
- Would regional products fit? Yes. UK app-first (Starling) and AU direct-entry-centric (CommBiz) both fit without US check/RDC/bill-pay specifics — rails are L2.
- Does L0 over-fit multi-user? No — L0 requires *granted per-user access* (satisfied trivially by a single authorized person), not *multiple users*. Multi-user administration is L1, supported by the fact that CommBank explicitly routes owner-managed businesses to its consumer portal while still calling the multi-staff product the business banking solution.
- Sole-trader boundary observed three ways (consumer-portal routing, separate account product, linking rule) — evidence that the Type's center of gravity is the multi-person organization, with the one-person business as a segment variant absorbed differently by different banks.

## Vendor-specific Findings

See Level 3 above. Additionally: BofA/Chase/Wells Fargo all expose their corporate tier as a structurally separate platform (CashPro; J.P. Morgan Commercial Banking; WF Commercial Banking), which is strong evidence that "Business Banking Portal" (SMB-grade, per-user entitlement model, self-service payments) and "Commercial/Cash-Management Platform" (treasury-grade, file/API rails, liquidity machinery) are different products in the same banks — a tier seam, likely a Type seam.

## Boundary Findings

| Neighboring Type | Seam | Test ("remove what → becomes the other Type") |
|---|---|---|
| Online Banking Portal / Mobile Banking Application (consumer; unprocessed §08 siblings) | customer is a person vs an organization; no delegation/authority machinery on the consumer side | remove organization-as-customer + per-user granted authority → consumer online banking |
| Commercial Banking Platform / Cash Management Platform (unprocessed) | SMB-grade self-service payments vs treasury-grade rails, files/APIs, liquidity; banks sell separate platforms (CashPro vs BA360) | remove the SMB self-service framing and scale down the rail machinery → corporate platform is a different leaf; the seam is a joint-review item |
| Banking Back-office Platform (processed) | customer-side origination vs bank-staff-side execution (validate→authorize→post/transmit) | move the operator from the business to the bank → back-office platform |
| Treasury Management System (unprocessed) | bank-provided channel over the bank relationship vs corporate in-house software managing all banks' cash | move the system inside the corporate treasury department → TMS |
| Payment Processing / Gateway (§08) | bank-account operations vs card-acceptance infrastructure; merchant services appear only as attached views | remove deposit-account operations → payment processing |
| Accounting Software (§08) | bank-side records of real accounts vs the business's books; integration partner | remove the bank and the rails → accounting software |
| Customer Portal (§07 generic) | domain object is bank accounts, not support/orders/subscriptions | genericize the domain → customer portal |
| Mortgage Borrower Portal (unprocessed §08) | whole banking relationship vs single loan product servicing | narrow the domain to one loan product → borrower portal |

Intra-sample observation: the consumer/business seam runs through the customer's *operating model* (owner-managed vs multiple authorized people), not through the account product — one bank routes sole traders to its consumer portal, another sells them a separate account with the same app, a third allows linking rules. The Type boundary is real but its expression varies by bank.

## Uncertainties

- Wells Fargo's user-administration/entitlement surface was not directly observed in fetched pages; the multi-user finding for that product rests on the category norm and is marked accordingly (not used to strengthen L0/L1 claims).
- Starling's help center was JS-gated; its approval/entitlement capabilities are unverified here. Starling contributes segment/account-product observations only.
- No precise limits, windows, or default settings are asserted in the final document; NetBank's published numeric limits are vendor facts and were kept in research notes only.
- Mercury/Tide were abandoned after access failures (JS gate / 404); the digital-native angle rests on Starling alone.
- Whether the directory's separate consumer-surface leaves (online-banking-portal, mobile-banking-application, digital-banking-application) can hold distinct Types from this one is a joint-review question recorded in STATUS.md.

## Final Synthesis

A Business Banking Portal is the bank's customer-side digital channel in which the customer is an organization: the bank's record of the business's accounts is exposed to identified, individually authorized representatives of that business, who can see balances and history and can originate payments/transfers from those accounts, with each person's access rights granted under the business's authority. Around this core, mature products add customer-side user administration, approval workflows and limits, payee/template management, multi-rail payments, statements/documents, alerts, mobile companions with check deposit and payment approval, self-service maintenance, audit, accounting interoperability, outgoing-item fraud controls, and attached business services (payroll, merchant services, cards, FX). The segment splits inside banks (owner-managed vs multi-staff; SMB portal vs corporate cash-management platform) are variant/tier phenomena, not separate cores. L0 stays at: organization-held accounts + authorized individuals + visibility + money movement + granted per-user access.
