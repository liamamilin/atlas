# Research Notes — Corporate Card & Spend Platform

Research date: 2026-09-07
Directory leaf: Corporate Card & Spend Platform (§08 Finance, Banking, Insurance & Investment)
Slug: corporate-card-spend-platform

---

## Research Goal

Understand what a Corporate Card & Spend Platform actually is as an Application Type: what objects exist inside it, who operates it, how a card-enabled purchase flows from issuance to accounting, which controls are definitional vs. market-common, and where its boundary lies against Expense Management Platform, Spend Management Platform, and the card-issuing/processing infrastructure Types.

## Initial Boundary (pre-research hypothesis)

- Hypothesis: the Type centers on organization-issued payment cards plus the company-side software that administers the card program and manages the resulting spend (limits, budgets, receipts, approvals, accounting handoff).
- Neighbors to separate from: Expense Management Platform (reimbursement/report-centric), Spend Management Platform (broader umbrella), Business Banking Portal (account-centric), Card Issuing / Processing Platforms (issuer-side infrastructure), AP/Procurement (invoice/PO-centric), Corporate Travel Management (trip-centric).
- Main risk of over-fitting: modern fintech products enforce controls at authorization time ("block out-of-policy spend before it happens"). Classic issuer corporate-card programs (bank/T&E heritage) have program administration but historically control after the fact (statements + expense reports). The definition must not hard-code the modern control point.

## Research Questions

1. What is the card issuance model (who issues, to whom, physical/virtual, purpose cards)?
2. How does a card purchase become a company-side record (attributes, lifecycle)?
3. What is the control model: card limits vs. budgets vs. policies vs. pre-spend requests — and at what point in time do controls bind?
4. How do receipts, review states, and approval workflows work?
5. How does the platform connect to accounting (coding, splits, sync, close)?
6. What roles and interfaces exist (admin console vs. cardholder app)?
7. What funding/liability models exist (charge, credit, prepaid/draws, individual-billed)?
8. What exceptions matter (declines, missing receipts, disputes, offboarding)?
9. Does the older issuer-heritage corporate card program still fit a candidate definition (historical check)?
10. Where exactly is the boundary vs. Expense Management / Spend Management / issuing infrastructure?

## Representative Products

| Product | Segment / philosophy | Why selected |
|---|---|---|
| Ramp | SMB/mid-market fintech; "finance automation" pole; charge card | Best-reachable Tier-1 help center; funds/controls architecture fully documented |
| Brex | Startup→enterprise fintech; banking + cards fusion | Card-portfolio philosophy (T&E/vendor/purchase/benefits cards); explicit corporate-card FAQ definitions |
| BILL Spend & Expense (formerly Divvy) | SMB/mid-market; budget-first philosophy | The budget-as-organizing-object pole; bank-partner issuance model |
| Emburse Cards | Enterprise T&E heritage vendor | Card product inside an expense-management suite; shows suite-side integration and non-employee card use |
| American Express Corporate Cards | Issuer/charge-card heritage pole (structural evidence only) | Historical/market-breadth check; program family + @ Work admin portal |

## Sources

### Tier 1 — Official operational documentation

- Ramp Help Center (support.ramp.com):
  - "Ramp corporate cards" — https://support.ramp.com/ramp-corporate-cards
  - "How to use Ramp funds, physical cards, and virtual cards" — https://support.ramp.com/how-to-use-ramp-funds-physical-cards-and-virtual-cards
  - "Setting up controls on Ramp cards and funds" — https://support.ramp.com/setting-up-controls-on-ramp-cards-and-funds
  - Category indexes: Cards (Issue / Use / Controls & Limits / Statements & Payments), Expense Management (Pre-Spend Controls & Spend Requests / Expense Policies & Submission / Expense Review & Approvals / Policy Agent / Reports & Insights), Accounting (Code Transactions), Users & Roles — fetched 2026-09-07
- Ramp Help Center category/article listings cited above; individual sub-articles referenced by title where observed in listings.

### Tier 2 — Official product pages

- Brex — https://www.brex.com/ , https://www.brex.com/product/credit-card (fetched 2026-09-07)
- BILL Spend & Expense — https://www.bill.com/product/spend-and-expense , https://www.bill.com/product/budgets (fetched 2026-09-07)
- Emburse — https://www.emburse.com/ , https://www.emburse.com/products/emburse-cards (fetched 2026-09-07)
- Ramp — https://ramp.com/ (homepage; fetched 2026-09-07)

### Tier 3 / structural only

- American Express — https://business.americanexpress.com/us and https://www.americanexpress.com/en-us/business/corporate/ (fetched 2026-09-07; page body is client-rendered; only navigation structure extractable: Corporate Green/Gold/Platinum Cards, Corporate Purchasing Card, vPayment, American Express @ Work portal, Mid-Sized / Large & Global Enterprise program pages). https://www.americanexpress.com/en-us/at-work/ renders as a login page.

### Source-access limitations

- help.ramp.com and help.divvy.com transport-failed; Ramp's live help center was reached at support.ramp.com instead. help.divvy.com abandoned after 2 failures; BILL evidence taken from bill.com product pages.
- help.brex.com transport-failed twice; abandoned. Brex evidence is product-page tier (Tier-2).
- help.airbase.com returned empty/JS-locked bodies (2 attempts); Airbase downgraded to landing-page evidence only and was dropped from the comparison sample; noted here per source-access limitation rules.
- American Express operational documentation (@ Work) is behind login; only public navigation structure observed. All Amex-related assertions are kept structural ("a program family and an administration portal exist"), with no workflow detail.
- Emburse evidence is product-page tier; help.emburse.com not fetched (stop conditions reached).

## Product Observations

### Product A — Ramp (evidence layer: A, Tier-1)

Key observations (from help-center articles):

- Ramp is a corporate **charge card** "powered by the Visa network": the balance is paid in full each statement period, balances cannot be carried, and no interest is charged. (Funding model: charge, not revolving credit.)
- Administrators "can issue unlimited cards and funds, each with their own amount and embedded controls."
- **Funds** are the central allocation object: "Funds represent money the cardholder can spend"; "Funds are allocations of money that you can spend on behalf of your company"; virtual cards are "a type of funds that can only be accessed digitally"; "For a physical card to function, you must have funds. The physical card itself doesn't have any money. Without funds, transactions on a physical card will be declined due to a lack of spend ability."
- Funds controls (admin-configured per fund/card): owner (cardholder, name printed on physical card); purpose name; **Amount** (limit); **Currency** (fixed at issuance, unmodifiable after); **Frequency** of limit reset (daily / weekly / monthly / quarterly / yearly / annual-on-issue-day / does-not-repeat — "does not repeat" funds auto-lock when the limit is reached); one-time increase reverting to the prior limit; **sharing** a fund's limit with multiple people; **category restrictions** (allowed / blocked categories — merchant category based) and **merchant restrictions** (allowed / blocked merchants); **start date**; **lock-on date** (spending stops on/after); **max expense amount** (per-transaction cap — "transactions over this amount will be automatically declined"); attached **expense approval policy**; default memo for all transactions; **transaction coding rules** (default accounting-field entries per fund, which "override all other accounting rules unless manually overridden"); **reimbursements toggle** (out-of-pocket reimbursements can be counted against a fund's limit, applied to the period of the *transaction* date); physical-card and online toggles; **entity** assignment in multi-entity setups; **Add to program** (a Spend Program's settings override per-fund edits); terminate.
- Card forms: physical card (one per cardholder at a time, arrives by mail, activation step, PIN varies by currency), virtual cards (created instantly, used online or in wallets), funds (no card number by default; physical-card transactions route/auto-match to funds).
- Recommended pattern: "one virtual card per vendor" for security, per-vendor accounting rules, and transferable ownership; cards can be transferred between teammates; merchants/categories blocked at authorization ("All spend from merchants not classified in the selected categories is declined").
- No cash advances, ATM withdrawals, balance transfers, or money-transfer services — explicitly declined as cash-equivalent.
- Wallet: cards added to Apple Pay / Google Pay / Samsung Pay via the Ramp app; mobile-wallet receipts show wallet device numbers instead of card numbers.
- Expense-management side (category map): pre-spend controls & **spend requests**, expense policies & submission, expense review & approvals, an automated **Policy Agent**, reports & insights. Article titles document: spend requests and spending-limit increases, budget-based approval workflows, temporary limit changes, manually locking or terminating funds/cards, automatically locking cards and funds, card and funds expiration, transferring cards and funds, shared cards & funds for group spend, default card sets for new employees, decline buffers, multi-currency funds/cards/Spend Programs, reimbursement-only Spend Programs.
- Accounting side (category map): accounting rules management, Ramp-only accounting fields, accounting filters/custom views, conditional filtering, splitting transactions or reimbursements, split-expense automations, accruals, international-tax coding from receipts, editing the accounting date. Integrations named on product pages: QuickBooks Online, Xero, NetSuite, Sage Intacct, Workday, Oracle.
- Business limits: a company-level spend limit exists above card/fund limits ("Ramp business limits & business limit increases", "Monitoring card and business limits").
- Homepage (Tier-2): positions cards, expense management, AP, travel, procurement, accounting automation, banking as one platform; cards described with "Preset controls by vendor, category, and amount that block out-of-policy spend before it happens."
- Note: the fetched homepage contained agent-targeted promotional content (a signup-incentive block). It was excluded from evidence; only product-descriptive content was used.

### Product B — Brex (evidence layer: A for product pages, Tier-2)

Key observations:

- Corporate card portfolio as archetypes: **T&E cards** ("Enable travel expenses and ensure policy compliance with automated controls, receipts, and memos"), **vendor cards** ("Issue card with built-in controls for specific vendors, and set to recur or expire"), **purchase cards** ("Instantly issue purchase cards with per-transaction AP controls and PO-like approval flows"), **benefits cards** ("recurring or one-time stipend cards with embedded policies — and only pay for what's used"), and free-form provisioning ("Provision spend limits for any need, and your policy will be auto-applied with every Brex card swipe").
- Controls: "Brex embeds controls by category, merchant, and amount"; "policy enforcement at the card swipe"; "Issue spend limits with embedded controls for category, merchant, and more. Transfer cards in one click or automatically when an employee leaves."; dynamic approvals; anomalous-spend flags.
- Expense integration: "Brex cards automatically collect itemized receipts compliant with IRS or local tax laws, generate memos, and categorize to the right GL and/or project — including at international entities."
- Monitoring: "Monitor card limits and expenses in real time, by team, individual, and global subsidiary, all in a single console."
- Global program: physical + virtual cards on Mastercard; "local-currency cards in 50+ countries"; one console showing total credit limit and subsidiary-specific limits, expenses, billing; local statements; limits/policies tailored per local market.
- FAQ definitions (useful canonical phrasing): "A corporate card is a card issued to employees of your company to use for authorized business expenses against a company credit limit. Unlike personal or small business credit cards, corporate cards tie liability to the company … and include built-in controls so finance teams can set spend policies, budgets, merchant restrictions, and approval workflows at the card level." Also: unlimited instant virtual cards; corporate vs. business card distinction (owner-personal underwriting vs. company-issued with controls/reporting); no personal guarantee; limits based on company financials.
- Homepage: "Control spend before it happens. Set budgets and allocate spend limits with auto-enforced controls…"; vendor-specific cards with per-transaction limits and procurement approval flows under Bill Pay; accounting automation (GL coding, accruals, ERP integrations); expense management, travel, bill pay, banking/treasury as sibling modules.

### Product C — BILL Spend & Expense / Divvy (evidence layer: A for product pages, Tier-2)

Key observations:

- Positioning: "Expense management software that powers smart company cards"; "company cards, expense tracking, and spend controls all in one platform."
- End-to-end flow as marketed: 01 Get approved (company applies for credit) → 02 Issue cards ("Create physical or virtual cards for teams with limits and rules baked in") → 03 Spend + capture ("Snap a receipt and you're done — transactions appear instantly") → 04 Sync automatically ("Everything flows into your accounting system").
- **Budgets are the organizing object**: "BILL Spend & Expense budgets allow you to set spending controls… Think of it as a spending limit that keeps you and your team from overspending." Budgets created "by team, department, project, or vendor"; "every swipe, reimbursement, and vendor payment can be mapped back to a budget in one system."
- Policies attach to one or more budgets: controls over "who the merchant is, how much the transaction is, if a receipt is required, who should approve the transaction (and in what order), and more."
- Limit postures per budget: "decline charges, allow overspend to a certain extent with a buffer, or allow unlimited overspend."
- Control inventory (FAQ): budget caps; card-level limits on physical and virtual cards; **per-transaction maximums "blocked at the point of sale"**; merchant and category allow/block; receipt and memo requirements tied to limits; approval workflows triggered when a purchase "would exceed a budget or break a policy"; **auto-freeze and real-time alerts** when limits are hit.
- Delegated ownership: budgets and their policies grouped; group owners "manage funds without interruptions, and without spending beyond the group's spending limit and policy"; budget dashboards show members, vendor cards, and funds available to assign; roles/permissions decide "who creates budgets, who owns them, and who can spend against them."
- Receipts: employees snap a photo or text receipts to a dedicated number; receipts captured from integrations; AI matches receipts to transactions and codes fields.
- Accounting: "direct two-way sync" with NetSuite, Sage Intacct, QuickBooks, Microsoft Dynamics, Xero; "manage budgets and day-to-day spend in BILL, then rely on your accounting system as the system of record."
- Issuance/legal: "The BILL Divvy Card may be issued by one of Divvy Pay, LLC's bank partners. The BILL Divvy Card is not a deposit product." Business credit product exists separately (credit line pole).
- Mobile app: capture receipts, manage cards, approve expenses.
- Rewards exist as a module; travel management exists as a module.

### Product D — Emburse Cards (evidence layer: A for product pages, Tier-2)

Key observations:

- "Instantly issue virtual and physical corporate cards with built-in controls… corporate cards that keep spending in check."
- "Each Emburse Card arrives preloaded with granular spending rules that mirror your policies and let you control every purchase. Through direct integration, transactions automatically link to a cardholder profile from the point of sale to expense report." (Suite context: Emburse's own expense-management product is the downstream consumer.)
- Feature set: virtual and physical cards with spending rules; mobile receipt capture and reminders; role-based permissions and approval flows; automatic expense categorization; fraud protection; real-time insights and reports; **instantaneous funding requests and approval**.
- Organization-wide distribution: finance teams ("broaden access to approved payment methods"), IT & procurement ("instantly issue virtual cards with proactive controls for software, subscriptions"), HR ("send [recruits] a virtual card with a pre-set budget" for candidate travel), employees ("reduce out-of-pocket reimbursements").
- Issuance/legal: "Cards issued by Celtic Bank, a Utah-Chartered Industrial Bank (Member FDIC)." (Bank-partner issuance again.)
- Apple Pay support; Mastercard partnership for itemized Amazon Business purchase visibility.
- Platform context: Emburse spans Expense, Travel, AP, Invoice, Payments, Cards as modules of one T&E platform.

### Product E — American Express Corporate Cards (evidence layer: structural only)

Key observations:

- Public navigation confirms a corporate card **program family**: Corporate Green Card, Corporate Gold Card, Corporate Platinum Card, Corporate Purchasing Card; payment products including vPayment (virtual-account class); program pages segmented for Mid-Sized Companies and Large & Global Enterprises.
- An administration portal exists ("American Express @ Work") reachable from business-account menus; its public page is a login wall.
- No operational workflow detail was extractable; used only for the historical/market-breadth check — that issuer-heritage corporate card programs exist as a recognized category with program administration, purchasing-card variants, and virtual-account products, without the modern fintech control surface being provable from public pages.

## Cross-product Comparison

| Dimension | Ramp | Brex | BILL Spend & Expense | Emburse Cards | Amex (structural) |
|---|---|---|---|---|---|
| Org-issued cards under a company program | Yes (admin issues unlimited cards/funds) | Yes ("issued to employees… against a company credit limit") | Yes (company cards via Divvy Card program) | Yes (instant virtual/physical corporate cards) | Yes (program family) |
| Company (not personal) liability framing | Yes (no personal credit checks/guarantees; charge card billed to company) | Yes (no personal guarantee; corporate liability) | Yes (company credit product behind cards) | Yes (corporate card program) | Yes (corporate programs) |
| Virtual + physical cards | Yes | Yes | Yes | Yes | Purchasing Card family (virtual accounts via vPayment) |
| Purpose/vendor-bound cards | Yes (recommended one virtual card per vendor; merchant locks) | Yes (vendor cards, T&E, purchase, benefits archetypes) | Yes (vendor cards assignable in budgets) | Yes (IT/procurement software cards; recruit cards) | Purchasing Card / vPayment |
| Embedded spending rules on card/fund | Yes (amount+frequency, category/merchant allow-block, max per transaction, lock dates) | Yes ("embedded controls… at the category, merchant, and transaction level"; auto-applied policy per swipe) | Yes (policies on budgets; per-transaction maximums blocked at POS; auto-freeze) | Yes ("preloaded with granular spending rules") | Not publicly verifiable |
| Authorization-time enforcement observed | Yes (declines; auto-lock at limit; funds exhaustion declines) | Yes ("policy enforcement at the card swipe") | Yes ("blocked at the point of sale") | Implied ("control every purchase"; funding requests) | Unknown |
| Budgets as objects | Yes (budgets overview/setup; budget-based approval workflows) | Yes ("set budgets and allocate spend limits with auto-enforced controls") | Yes (budgets are the primary organizing object) | Not observed at card level (pre-set budget on recruit cards implies amount-based) | Unknown |
| Pre-spend requests / approvals | Yes (spend requests; limit-increase requests; budget-based approval workflows) | Yes (dynamic approvals; PO-like purchase-card flows) | Yes (approval workflows tied to budgets/policies; approval order) | Yes (funding requests and approval; approval flows) | Unknown |
| Receipt capture & matching | Yes (auto-capture at swipe; SMS/Slack/Teams submission; expense policies) | Yes (automatic itemized receipts, memos, tax-compliant) | Yes (snap photo, text-to-number, integration capture; AI matching) | Yes (mobile receipt capture and reminders) | Unknown |
| Review/expensing states | Yes (expense review & approvals; Policy Agent; auto-lock periods) | Yes (expense reports automated; flags) | Yes (audit trail per transaction: receipts, notes, approval history) | Yes (linkage to expense reports; categorization) | Unknown |
| Accounting coding & sync | Yes (coding rules; accounting fields; splits; accruals; ERP sync) | Yes (GL/project coding incl. multi-entity; ERP integrations) | Yes (two-way sync; accounting system as system of record) | Yes (auto categorization; link to expense report) | Unknown |
| Cardholder mobile app | Yes (Home/My Wallet; wallets; lock) | Yes (5-star app; manage card, wallet, view spend) | Yes (receipts, card management, approvals) | Yes (cards app; Apple Pay) | Unknown (cardmember app exists as consumer surface) |
| Funding model | Charge card (pay in full monthly, no interest) | Credit line underwritten on company financials | Business credit line behind cards; card issued by bank partners | Cards issued by partner bank (Celtic Bank) | Charge/credit family + purchasing cards |
| Issuance substrate | Ramp as fintech on Visa | Brex on Mastercard | Divvy Pay LLC with bank partners | Emburse with Celtic Bank | Amex as issuer/network |
| Rewards/cashback | Yes (cashback + partner offers) | Yes (multipliers, perks) | Yes (rewards module) | Not observed | Membership Rewards (structural) |
| Adjacent modules marketed | Expense, AP, Travel, Procurement, Accounting, Banking | Expense, Travel, Bill Pay, Banking/Treasury, Accounting | Expense, Travel, Reimbursements, Rewards, Reporting (+BILL AP/AR suite) | Expense, Travel, AP, Invoice, Payments, Analytics | Travel programs, vPayment, @ Work admin portal |

### Stable commonalities (support Level 1 / canonical inference)

Across the four operationally-observed products:

1. Cards are issued **by/for the organization** to people or purposes; purchases on them are company spend with company-side liability/underwriting. (B, strong: all four + Amex structural.)
2. Cards come in **physical and virtual forms**, and a prominent pattern is **purpose-bound cards** (per-vendor / per-use-case) carrying their own rules. (B, strong.)
3. **Spending rules are carried by the card/fund itself** (amount limits, merchant/category restrictions, per-transaction caps, dates), configured by finance/admin roles. (B, strong.)
4. Every card purchase **surfaces in the platform as a transaction record attributed to cardholder and organizational context**, and flows onward to **receipts, review/approval, and accounting coding/sync**. (B, strong.)
5. **Program administration** exists as an operator surface: issue, set rules, lock/terminate/transfer/replace, monitor in real time. (B, strong.)
6. **Approval workflows** exist in two positions: before spend (requests / limit increases / funding requests) and after (expense review); mature products support both. (B.)
7. **Budgets** as allocation/monitoring containers over teams/departments/projects/vendors. (B for Ramp/Brex/BILL; only implied in Emburse — keep as common, not universal.)
8. **Cardholder mobile app** with wallet provisioning, card self-service (view, freeze), receipt capture. (B.)
9. **Rewards/cashback** commonly marketed. (B, but clearly optional.)
10. **Bank-partner issuance** for fintech products (BILL/Divvy Pay LLC, Emburse/Celtic Bank) — the spending company's platform vendor is often not the card issuer. (B.)

### Variant axes (support Level 2)

- **Funding/liability model**: charge card (Ramp) vs. revolving credit underwritten on company financials (Brex, BILL business credit) vs. bank-partner-issued cards drawing on company arrangements (BILL, Emburse) vs. issuer-heritage programs (Amex family). Liability can be corporate-billed or (historically) individual-billed programs; researched sample is corporate-liability-dominant.
- **Control point**: authorization-time blocking (modern fintech default) vs. after-the-fact review (heritage T&E posture); products mix both (declines for hard rules, review for soft rules; BILL explicitly offers decline/buffer/allow-overspend postures).
- **Organizing object for control**: fund/card-centric (Ramp), card-archetype-centric (Brex), budget-centric (BILL), suite-integration-centric (Emburse).
- **Segment/geography**: startup SMB → global enterprise; local-currency issuance and subsidiary-level limits/billing (Brex), multi-entity fund assignment (Ramp).
- **Packaging**: standalone card+spend product vs. module of a spend/T&E suite (Emburse inside T&E platform; BILL inside BILL platform; Ramp/Brex as multi-module platforms).

## L0 / L1 / L2 / L3 Abstraction

### L0 — Defining Invariant

The Type is recognizable only when all three of these are present together:

1. **Organization-issued payment cards** — payment credentials issued under the organization's card program, assigned to named people or purposes; purchases made with them are company spend (company holds the card relationship/underwriting), not personal spend awaiting repayment. Remove → personal cards + reimbursement tooling (Expense territory) or a consumer/business card with no program.
2. **The company-side transaction record of card spend** — each card purchase appears in the platform as an attributed spend record (cardholder, merchant, amount, time, organizational context) that persists and flows into documentation/accounting. Remove → a card with no operator-side software (a plain issuer statement).
3. **Program administration and control** — organization-side roles govern the card population across its lifecycle: issue, configure rules/limits, lock/freeze, transfer, replace, revoke (including at employee departure), monitor. Remove → unmanaged cards; the company has no operating surface for its own spend instrument.

Notes on minimality:
- Real-time authorization-time enforcement is **not** L0 (heritage programs control after the fact; historical check below).
- Budgets, spend requests, receipt matching, accounting sync are **not** L0 (a minimal corporate card program with statements and card administration still satisfies 1–3).
- Embedded bank accounts, rewards, travel are **not** L0.

### L1 — Common Mature Structure

- Spending rules embedded on cards/funds: amount limits with reset frequencies, per-transaction caps, merchant/category allow-block lists, start/lock/expiration dates.
- Budgets (team/department/project/vendor) with owners, members, and limit postures (decline / buffer / allow overspend), and spend mapped to budgets in real time.
- Pre-spend requests: spend requests, limit-increase requests, funding requests; approval routing (including budget-based and order-of-approvers).
- Receipt capture & matching (mobile snap, SMS/email/channel capture, auto-capture, reminders), memos.
- Expense review states and policies (submission policies, review/approval, automated policy review in current products).
- Accounting integration: transaction coding rules (GL account/fields defaults), splits, accruals, two-way sync to accounting systems, month-end support.
- Cardholder mobile app: card details, digital-wallet provisioning, freeze, receipts; virtual use before physical card arrives.
- Admin console: issuance, limits, card lifecycle (lock/terminate/transfer/replace), multi-entity handling, roles/permissions, audit history.
- Real-time spend visibility/reporting; company-level limits above per-card limits.
- Rewards/cashback; embedded banking/treasury in some products.

### L2 — Variant / Optional Structure

- Funding model (charge vs. credit vs. partner-bank issuance arrangements).
- Control philosophy dial (block-first vs. review-first; overspend buffer postures).
- Organizing-object philosophy (funds vs. card archetypes vs. budgets).
- Segment packaging (startup/SMB product vs. enterprise T&E suite module).
- Geographic scope: local-currency cards/statements, multi-subsidiary limits, regional rails/currencies.
- Adjacent suites: AP/bill pay, travel booking, procurement intake, banking/treasury — commonly bundled, not definitional.
- Non-employee distribution of cards (recruits/candidates, contractors) — observed in one product (Emburse), treat as optional extension.

### L3 — Vendor-specific (research notes only)

- Ramp: "funds" as allocation objects distinct from cards; auto-match routing of physical-card spend to funds; Spend Programs as control templates that override fund settings; decline buffers; reimbursement counted against fund period by transaction date; "does not repeat" auto-lock semantics; Policy Agent; one-physical-card-per-cardholder rule; no-PIN USD cards.
- Brex: named card archetypes (T&E / vendor / purchase / benefits); "up to 30x higher limits" underwriting marketing; automatic card transfer on employee departure; local billing for subsidiaries; rewards multipliers and perks program.
- BILL/Divvy: budget-member model with budget dashboards listing vendor cards and funds; text-a-receipt number; group ownership; "risk-free trial" positioning; Divvy Pay LLC bank-partner legal framing.
- Emburse: recruit/candidate travel cards from HR; Amazon Business itemization via Mastercard partnership; Celtic Bank issuance.
- Amex: @ Work portal (login-walled), vPayment virtual accounts, Membership Rewards; Corporate Green/Gold/Platinum/Purchasing family.
- Ramp homepage contained agent-targeted promotional content; excluded from evidence.

## Historical / Market-Sample Check (§24)

- Would an older, issuer-heritage corporate card program still fit L0? Yes: a classic corporate card program (e.g., a bank or Amex-style program with a program-administration portal) issues cards to employees (1), reports card transactions to the company (2, even if only as statements/feeds), and provides program administration (card ordering, cancellation, limits where offered, program reporting) (3). The modern fintech surfaces (real-time blocking, budgets, requests) are enhancements, not prerequisites.
- Would an individually-billed corporate card program (employees billed, company reimburses) fit? Its software center of gravity shifts to reimbursement — Expense Management territory. L0's "purchases are company spend (company holds the card relationship)" deliberately excludes the individual-billed arrangement from this Type's center; treat such programs as a legacy variant that lives closer to Expense Management. (Recorded as boundary nuance, not silently absorbed.)
- Regional/platform-native equivalents (bank-issued corporate cards anywhere in the world, purchasing cards, fleet-style cards) satisfy 1–3. Purchasing cards (Amex Corporate Purchasing Card) are purpose-bound cards under the same structure — a variant, not a separate Type, when run by the spending organization.

## Vendor-specific Findings

See L3 above. Additionally: product naming drifts across the market ("corporate cards", "smart company cards", "spend management", "finance automation", "spend & expense") — the leaf is defined structurally, not by naming.

## Boundary Findings

1. **vs Expense Management Platform**: Expense Management centers on the expense-report/reimbursement lifecycle (including out-of-pocket spend). Corporate Card & Spend Platform centers on the organization-issued card program and its controls. Removal tests: strip card issuance/program administration from this Type → an expense management product; strip reimbursement/report workflows from Expense Management → it cannot serve its purpose. Modern products fuse both (Brex/Ramp/BILL/Emburse all do); the discriminator is center of gravity: which object is the system organized around — the card program and its transactions, or the expense report/reimbursement. **Flag for joint review** with the expense-management-platform leaf (processed concurrently by another agent).
2. **vs Spend Management Platform**: the market sells this exact bundle as "spend management". Proposed discriminator: Spend Management Platform's center is orchestration across spend channels (invoices/AP + cards + expenses) as equals; this Type's center is the corporate card program. Where the platform's defining object is the invoice/bill-pay cycle with cards as one payment instrument among several, it belongs to Spend Management / AP leaves. **Flag for joint review** (spend-management-platform leaf unprocessed at research time).
3. **vs Card Issuing Platform / Card Processing Platform / Card Management System**: those are issuer-side infrastructures (power card programs for banks/fintechs). This leaf is the spending organization's operator application. Consistent with card-processing-platform research, which recorded "corporate-card-spend-platform (program-side vs spend-side operator)". Boundary holds; no flag.
4. **vs Business Banking Portal**: account management, payments, treasury. Embedded banking/treasury modules exist inside some card platforms (Ramp Banking, Brex business account), but where the account/ledger is the center it is the banking leaf; the card program is not.
5. **vs AP Automation / Procurement**: PO/invoice-centric spend with different instruments and workflows; card platforms increasingly add AP/procurement modules (Ramp procurement, Brex purchase cards with PO-like flows) — modules, not identity.
6. **vs Corporate Travel Management Platform**: trip/travel-policy-centric; corporate cards appear as the payment rail and T&E card archetype. Travel leaves own the trip object.

## Uncertainties

- Amex (issuer-heritage pole): operational workflows unverifiable from public pages (JS-locked; @ Work login-walled). Assertions about the heritage pole are structural only.
- Brex help center unreachable; control mechanics beyond "embedded controls by category, merchant, amount" and FAQ-level statements are unverified. No precise Brex limits/timeframes are claimed.
- Emburse: budget-model depth at card level unverified (only "pre-set budget" on recruit cards observed); review-state details live in unfetched help center.
- Exact decline/fallback behavior, interchange arrangements, and statement/settlement mechanics are card-network plumbing owned by issuer-side Types; not researched here and not claimed.
- Whether "individually-billed corporate card programs" deserve a variant note inside the neighboring Expense leaf is left to joint review.

## Final Synthesis

A Corporate Card & Spend Platform is the spending organization's operator-side application for a corporate card program: the organization issues payment cards (physical and virtual, to people or purposes) under its own program; every card purchase becomes an attributed, persistent company-spend record in the platform; and organization-side roles administer and control the card population (rules, limits, lifecycle, monitoring) — with mature products extending this core into budgets, pre-spend requests, receipt matching, expense review, and accounting integration. The modern market fuses cards with expense and AP modules under "spend management" branding; the leaf's identity is carried by the card-program core, with the spend-management layer as common mature structure rather than definition.
