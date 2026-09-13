# Research Notes — Accounting Software

Research date: 2026-09-06
Methodology: v1.1 (update-v1/)

## Research Goal

Understand what "Accounting Software" (the SMB/small-business category, e.g. QuickBooks-class products) actually is as an Application Type: what objects exist inside it, how money flows through it, what its defining structure is (as opposed to what modern products merely commonly bundle), and where its boundaries lie against General Ledger Systems, Bookkeeping Applications, Invoicing Applications, ERP, and Personal Finance Management.

## Initial Boundary

Initial hypothesis (to be verified, not final):

- Core: maintains a business's books — chart of accounts, double-entry ledger, financial statements.
- Likely wrapped with SMB operational modules: invoicing (AR), bills (AP), bank feeds/reconciliation, sales tax.
- Nearest neighbors: General Ledger System (core engine alone), Bookkeeping Application (activity framing / possible alias), Invoicing Application (billing-first), ERP (accounting embedded in wider operations), Personal Finance Management (personal books), Account Reconciliation Platform (enterprise-scale reconciliation), Tax Preparation (return-centric).
- Main unknowns: is invoicing definitional or common? How visible is double-entry to users? How do regional tax regimes shape the model? Is "bookkeeping software" a separate Type or the same products under another name?

## Research Questions

1. What is the chart of accounts — what categories/types exist, who creates accounts, what rules constrain them?
2. How are transactions recorded — is double-entry user-visible or hidden? What user-facing forms does a "transaction" take (invoice, bill, expense, bank line, journal)?
3. How do AR and AP work — invoice → payment → credit note; bill → payment → vendor credit?
4. How does bank connection work — feeds, import, matching/categorization, reconciliation mechanics?
5. What reports are generated and from what?
6. How are fiscal periods, accounting basis (cash vs accrual), taxes, currencies handled?
7. Who uses it — owner, bookkeeper, accountant — and what surfaces does each get?
8. What is the boundary against GL systems, invoicing apps, ERP, PFM?

## Representative Products

Selected for market representation + documentation completeness + different product philosophy + different customer tier:

| Product | Philosophy / tier | Access result |
|---|---|---|
| Xero | cloud-first global SMB; accountant/partner-centric | product pages fetched (Tier 2); Xero Central help is JS-rendered (no article text) |
| FreshBooks | service-business / invoicing-first heritage; freelancers & micro-SMB | accounting product page + support center fetched (Tier 2 + Tier 1 nav) |
| Wave | free tier for micro-business/solopreneurs; payments-monetized | root + Help Center + 2 help articles fetched (Tier 2 + Tier 1) |
| Zoho Books | suite-integrated; broadest module map; many regional editions | product page + full help docs incl. 3 articles fetched (Tier 2 + Tier 1) |
| QuickBooks Online | US SMB market leader | **unreachable** — 3 WebFetch timeouts (quickbooks.intuit.com root, /accounting/, learn-support). Dropped from evidence base; no product-specific claims made. |

QuickBooks and Sage are retained only as market-context anchors (they are referenced by the sampled vendors' own comparison/migration pages), not as evidence sources.

## Sources

Tier 1 (official operational documentation, directly fetched):

- Zoho Books Help — Chart of Accounts: https://www.zoho.com/books/help/accountant/chart-of-accounts.html
- Zoho Books Help — Manual Journals: https://www.zoho.com/books/help/accountant/manual-journal.html
- Zoho Books Help — Banking > Reconciliation: https://www.zoho.com/books/help/banking/reconciliation.html
- Zoho Books Help — full documentation TOC (module map): https://www.zoho.com/books/help/getting-started/welcome.html
- Wave Help Center — Overview of your Chart of Accounts page: https://support.waveapps.com/hc/en-us/articles/115004972106
- Wave Help Center — Overview of the Reports page: https://support.waveapps.com/hc/en-us/articles/115005085723
- Wave Help Center root (category map): https://support.waveapps.com/hc/en-us
- FreshBooks Support Center root (category map): https://support.freshbooks.com/hc/en-us

Tier 2 (official product pages):

- Xero — homepage + Accounting software page: https://www.xero.com/ , https://www.xero.com/accounting-software/
- FreshBooks — Accounting software page: https://www.freshbooks.com/accounting
- Wave — homepage: https://www.waveapps.com/
- Zoho Books — homepage: https://www.zoho.com/books/

Unreachable / degraded:

- QuickBooks (quickbooks.intuit.com) — all attempts timed out; Xero Central (central.xero.com) — JS-rendered, article text not retrievable. Consequence: no QuickBooks-specific observations; Xero claims rest on product pages only (Tier 2), not help articles.

## Product Observations

### Zoho Books (evidence layer A unless noted)

From the help documentation TOC (module map) and three fetched articles:

- **Organization as container**: settings include Organization Profile, Opening Balances, Users & Roles, Preferences, Currencies, Payment Terms, Taxes, Revenue Recognition. Books belong to an "organization"; multi-org supported; demo org available.
- **Chart of Accounts (Tier 1 article)**: default accounts grouped into categories — Assets (Cash, Bank, Fixed Asset, Stock, Accounts Receivable, Payment Clearing, Deferred Tax Asset, Other Current Assets, Other Asset), Liability (Accounts Payable, Credit Card, Long Term Liability, Deferred Tax Liability, Overseas Tax Payable, Other Current/Other Liability), Equity, Income (Income, Other Income), Expense. Users create accounts (type, name, code, description, dashboard watchlist); import CoA from CSV/TSV/XLS; export; accounts with transactions cannot be deleted; system default accounts cannot be deleted or marked inactive.
- **Manual Journals (Tier 1 article)**: "journals are used to record debit and credit entries for transactions in chronological order. These entries are then posted to the general ledger." Manual journals exist for entries that standard modules can't produce (depreciation, accruals, error corrections). Explicit rule: "Ensure that the amount debited is always equal to the amount credited." Statuses: Draft → Pending Approval → Approved/Rejected → Published; draft amounts do not affect accounts until published. Reporting Method per journal: Accrual only / Cash only / Accrual and Cash. Journals impact Balance Sheet and P&L and are reviewable in General Ledger, Trial Balance, Journal Report. Recurring journals, reverse journals, journal templates, 13th-month adjustment journals (regional year-end practice), base currency adjustment journals.
- **Banking (Tier 1 reconciliation article + TOC)**: add bank/credit card accounts; bank feeds; manually add transactions; match & categorize; transaction rules (auto-categorization); reconciliation per account per period — enter start/end date and the bank statement's closing balance, select transactions, cleared amount must equal closing balance (difference zero); only matched/categorized/manually-added transactions appear; undo/delete reconciliation (undoing a non-recent reconciliation requires undoing all later ones); opening balance cannot be edited once transactions are reconciled.
- **AR chain (TOC)**: Quotes (convert to sales order/invoice, progress invoices) → Sales Orders → Invoices (record payment, early payment discount, late fees) → Payments Received → Credit Notes (apply to invoice, refund) → Recurring Invoices → Retainer Invoices. Customer statements, customer portal, payment links, online payments via Stripe/PayPal/GoCardless/Authorize.net/Braintree/etc.
- **AP chain (TOC)**: Purchase Orders → Bills → Payments Made (vendor payments, refunds) → Vendor Credits. BillPay add-on (vendor onboarding, PO matching, bill reconciliation, batch payments).
- **Expenses**: expense recording, mileage, recurring expenses, billable expenses.
- **Items/Inventory**: items with stock tracking, inventory adjustments, price lists; advanced inventory via Zoho Inventory add-on.
- **Accountant module (TOC)**: manual journals, budgets, chart of accounts, sub-accounts, transaction locking (period lock), fixed assets, manage clients (practice use), DATEV export (Germany).
- **Transaction Approval (TOC)**: simple / multi-level / custom approval workflows for transactions.
- **Reports (TOC)**: Business Overview, Sales, Inventory, Payables, Receivables, Payments Received, Activity, Tax reports, Custom Reports; scheduled report emailing.
- **Compliance/regional (TOC)**: e-Invoicing — VeriFactu (Spain), Peppol UBL (Belgium); 17+ regional editions (US, UK, AU, CA, DE, FR, IN, SA, UAE, etc.); VERI*FACTU compliance notice on homepage.
- **Other**: audit trail (version history shown on homepage), custom fields/modules, branches (multi-location), customer & vendor portals, timesheets/projects, import/export/backup, migration guides from QuickBooks Online, Tally, FreshBooks, Wave; AI features (Zia); MCP server; free plan + 5 paid editions.

### Wave (evidence layer A unless noted)

From Help Center articles and root:

- **Chart of Accounts (Tier 1 article)**: "a chart of accounts is a record of your financial accounts. When you categorize a transaction, it's categorized to an account within the chart of accounts. Wave uses this information to help generate your reports." Tabs = account types: Asset; Liabilities & Credit Cards; Income; Expense; Equity. Pre-populated with "common accounts related to the business type you selected during setup". Users add/edit/archive accounts (archive, not delete). **No custom tabs, new account types, or subaccounts** (explicit product limitation). Tax line mapping (US tax lines) assignable to income/expense accounts. "Payment account" concept (bank/credit-card accounts used to record payments).
- **User-facing transaction model**: categorization of transactions (video: "Understand categorizing transactions in Wave"; article "Categorize or recategorize transactions") — the debit/credit engine is hidden behind categorization. Recording personal transactions from a business account is a supported special case.
- **Reports (Tier 1 article)**: organized by topic — Financial statements (Profit & Loss / Income Statement, Balance Sheet, Cash Flow); Taxes (Sales Tax report); Payroll reports (if payroll add-on used); Tags (project-style profitability); Customers (Income by Customer, Aged Receivables, Customer Credits); Vendors (Purchases by Vendor, Aged Payables); Detailed reporting (Account Balances, Trial Balance, Account Transactions (General Ledger)). Reports exist "for tax filing" and export is supported. Accrual vs cash-basis reporting article exists.
- **Module map (help categories + homepage)**: Accounting; Transaction Imports (bank connections, statement upload); Invoices & Estimates; Payments (Wave's own card/bank payment processing; PCI-DSS Level 1); Payroll (add-on); Receipts & Bills. Web-based; mobile companion app. Plans: free Starter + paid Pro; monetized via payments/payroll/advisors. Wave Advisors (paid bookkeeping/accounting coaching service).
- Positioning: "built for small business owners and solopreneurs… not accountants" (marketing claim, layer A as positioning only).

### Xero (evidence layer A for product pages; no help-article text retrievable)

From homepage and Accounting Software page (Tier 2):

- Positioning: "online accounting software" for small business; "invoicing, payroll, and reporting in one place".
- **Bank feeds**: "Xero's bank feed securely imports your transactions into Xero bookkeeping software each business day"; reconciliation "on a single screen"; connect all business bank accounts; track cash flow.
- **Invoicing & payments**: send online invoices, accept online payments, pay bills, purchase orders, quotes.
- **Expenses**: claim expenses, mileage tracking; employees submit expenses via Xero Me app.
- **Reports/insights**: "run quick reports for fresh insights"; cash flow, P&L surfaced in mobile app FAQ.
- **Accounting method**: setup FAQ names the cash vs accrual choice as a basic setup decision.
- **Migration**: import chart of accounts, invoices, bills, contacts, fixed assets from previous software (links to Xero Central "Convert to Xero").
- **Collaboration**: real-time shared access with bookkeeper/accountant; partner programme (250k accountants/bookkeepers claimed); practice-side products (Xero Cashbook, Xero Ledger, Workpapers) for accountants.
- **Platform**: cloud, MFA required at login, mobile app, 1000+ app ecosystem (Stripe, GoCardless, Vend, Shopify named), plans (Starter/Standard/Premium), AI assistant (JAX).
- Note: Xero's own pages use "accounting software" and "bookkeeping software" interchangeably (e.g. "imports your transactions into Xero bookkeeping software") — relevant to the Bookkeeping Application boundary question.

### FreshBooks (evidence layer A for product page + support nav)

From the Accounting product page (Tier 2) and support center (Tier 1 nav):

- Positioning: "Simple Double-Entry Accounting For Your Business"; accounting features framed around invoicing/billing clients + financial reports + accountant collaboration.
- **Chart of accounts**: "customizable chart of accounts"; accountant can "update your journal entries and chart of accounts".
- **Reports**: "tax-ready financial reports like Profit and Loss, Balance Sheet, and Trial Balance reports"; FAQ entries for year-end reports, P&L.
- **Bank reconciliation**: "link your bank account and create automated workflows for bank reconciliation and transaction management".
- **Accountant collaboration**: grant accountant access to real-time data; accountant runs reports, files taxes.
- **Module map (product page footer + support categories)**: Invoicing, Payments, Time Tracking, Accounting, Expenses & Receipts, Reports, Mileage, Bookkeeping (own feature page), Projects, Proposals, Estimates, Clients, Payroll, Team Management, Bill Pay, mobile apps, Instant Payouts, Buy Now Pay Later, Financing. Support categories: Invoices; Payments; Expenses and Bank Connections; Projects and Time Tracking; Reports and Accounting ("organize your finances with bank reconciliation"); Team Members and Payroll; Clients; Estimates and Proposals.
- Audience pages: freelancers, contractors, self-employed, small businesses, accountants; industry pages (construction, legal, agencies…).

### QuickBooks Online — not researched

All fetch attempts timed out. No observations recorded; no claims in either file rely on QuickBooks. Market presence is indirectly evidenced by sampled vendors' own comparison and migration pages (Wave "Wave vs QuickBooks", Xero "Xero vs Quickbooks", Zoho migration guide "From QuickBooks Online").

## Cross-product Comparison

| Structure / capability | Xero | FreshBooks | Wave | Zoho Books | Layer |
|---|---|---|---|---|---|
| Business-entity books (organization container, settings, opening balances) | yes (per-org plans) | yes | yes | yes (explicit "organization") | B |
| Chart of accounts with asset/liability/equity/income/expense categories | yes (CoA import on migration) | yes ("customizable chart of accounts") | yes (5 explicit types) | yes (5 categories, default types listed) | B (A: Wave, Zoho) |
| Transactions posted to accounts; reports derived from accounts | yes | yes | yes (explicit) | yes (explicit) | B |
| Double-entry engine (debit=credit) | implied | explicit (marketing: "double-entry accounting") | implied (Trial Balance + General Ledger reports) | explicit (manual journals rule) | B |
| User-facing transaction forms: invoice / bill / expense / bank line / journal | yes | yes | yes | yes (all five explicit) | B |
| AR: invoices → payments → credit notes | yes | yes | yes | yes (explicit chain) | B |
| AP: bills → payments → vendor credits | yes (pay bills) | yes (bill pay) | yes (Receipts & Bills) | yes (explicit chain) | B |
| Bank connection + feeds/import + matching/categorization + reconciliation | yes (daily feeds, single-screen rec) | yes (bank connections, automated rec) | yes (Transaction Imports category) | yes (full Tier 1 mechanics) | B |
| Financial statements: P&L, Balance Sheet (+ Cash Flow) | yes | yes (P&L, BS, Trial Balance) | yes (P&L, BS, CF) | yes | B |
| Trial balance / general ledger detail reports | implied | yes (Trial Balance) | yes (Trial Balance, GL) | yes (GL, Trial Balance, Journal Report) | B |
| Sales tax tracking + tax reports | yes (tax time framing) | yes (tax-ready framing) | yes (Sales Tax report, tax line mapping US) | yes (tax settings + tax reports) | B |
| Cash vs accrual basis | yes (setup FAQ) | not directly observed | yes (article exists) | yes (per-journal reporting method) | B |
| Accountant/bookkeeper as distinct collaborator role | yes (partner programme, practice tools) | yes (accountant access) | yes (Advisors service) | yes (Accountant module, manage clients) | B |
| Contacts (customers & vendors) | yes | yes (clients) | yes | yes (explicit module) | B |
| Items / products & services | yes | yes | yes | yes (items + inventory) | B |
| Quotes/estimates → invoice | yes (quotes) | yes (estimates) | yes (estimates) | yes (quotes → SO → invoice) | B |
| Recurring transactions | yes | yes | yes | yes (recurring invoices + journals) | B |
| User roles & permissions | yes | yes (team management) | limited evidence | yes (users & roles, approvals) | B |
| Audit trail / activity log | not directly observed | not directly observed | not directly observed | yes (audit trail, activity logs) | A (single product) |
| Payroll | add-on | add-on | add-on | via integration | B (optional) |
| Inventory depth | yes (feature) | not core | no | yes (items + add-on) | B (optional) |
| Projects / time tracking | add-on | core-adjacent | tags (lighter) | yes (projects + timesheets) | B (optional) |
| Multi-currency | yes (FAQ mentions FX payments) | not directly observed | yes (foreign currency balances article) | yes (currencies settings, base currency adjustment) | B (optional) |
| Budgets | not observed | not observed | not observed | yes | A (single product) |
| Fixed assets | yes (migration import) | not observed | not observed | yes | B (optional) |
| Purchase orders / sales orders | yes | not observed | not observed | yes | B (optional) |
| E-invoicing compliance (VeriFactu, Peppol) | not observed | not observed | not observed | yes | A (single product, regional) |
| Customer/vendor portals | not observed | client-facing invoice view | client payment view | yes (explicit portals) | B (optional) |
| Online payments processing | via partners | own + partners | own (PCI L1) | via partners | B (optional) |
| Free tier | no (trial) | no (trial) | yes | yes (free plan) | B (variant) |
| AI assistant | yes (JAX) | not observed | not observed | yes (Zia) | B (optional) |
| Desktop app | no (cloud+mobile) | mobile apps | web+mobile | web + Windows desktop + mobile | B (variant) |

## Canonical Abstraction

### L0 — Defining Invariant

The smallest structure without which the product stops being recognizable as accounting software:

1. **Business-entity books** — the system maintains the books of a defined business entity (organization), not a person's personal finances.
2. **Chart of accounts** — a user-manageable catalog of categorized ledger accounts (at minimum asset / liability / equity / income / expense families).
3. **Balanced transaction posting** — every recorded economic event is posted to the books as balanced ledger entries against those accounts (double-entry: debits equal credits), whether or not the UI exposes debits/credits.
4. **Financial statement derivation** — the posted ledger is summarized, as of a date / for a period, into at least a profit-and-loss statement and a balance sheet.

Test: remove the entity container → personal finance manager. Remove the CoA → expense tracker / invoicing app. Remove balanced posting → budgeting/tracking tool. Remove statement derivation → a data-entry ledger with no accounting output. All four are required.

Historical / market-sample check: this definition holds for desktop-era products (Peachtree/Sage 50, QuickBooks desktop), regional products (Tally, DATEV-ecosystem tools, freee-class JP products), and nonprofit/fund variants — all maintain CoA + balanced posting + statements. It does not depend on cloud delivery, bank feeds, invoicing, or any modern UX pattern.

### L1 — Common Mature Structure

Present in essentially all mature modern products; expected by the market but not definitional:

- AR subledger: customers, invoices, payments received, credit notes; statements; recurring invoices
- AP subledger: vendors, bills, payments made, vendor credits
- Bank connection: feeds or statement import, transaction matching/categorization, per-account per-period reconciliation
- Report suite: P&L, balance sheet, cash flow, trial balance, general ledger detail, aged receivables/payables, sales reports, tax reports
- Sales tax configuration and tax reporting ("tax-ready" positioning)
- Cash vs accrual reporting basis
- Contacts (customers & vendors), items (products & services)
- Quotes/estimates convertible to invoices
- Accountant/bookkeeper collaboration (invited access; accountant-only functions such as journals, CoA edits, period locks)
- Opening balances + migration import/export
- User roles & permissions; audit trail
- Source-document attachment (receipts, files)
- Cloud/web surface + mobile companion

### L2 — Variant / Optional Structure

Depends on segment, geography, deployment, business model:

- Payroll (add-on in every sampled product)
- Inventory management depth (multi-level, reorder, warehouses)
- Projects / time tracking / billable hours; profitability tags
- Multi-currency (plan- or edition-dependent)
- Budgets; fixed assets; revenue recognition; purchase/sales orders
- E-invoicing / fiscal compliance per country (VeriFactu, Peppol, DATEV export)
- Tax line mapping to national return forms (US)
- Customer & vendor self-service portals; online payment acceptance (own rails vs partner rails)
- Approval workflows (simple/multi-level)
- Branches / multi-entity; nonprofit fund accounting
- Deployment: cloud-first vs desktop heritage; free tier vs paid; AI assistants; industry editions (construction, nonprofit, retail)

### L3 — Vendor-specific (research notes only)

- Wave: no subaccounts/custom account types (explicit limitation); "payment account" concept; Wave Connect (Google Sheets add-on); Wave Advisors done-for-you bookkeeping; US tax line mapping rollout.
- Zoho Books: 13th-month adjustment journals; DATEV export; branches; MCP server; Zoho ecosystem integration (Expense, Inventory, CRM, Billing); BillPay add-on; free plan; 17+ regional editions.
- Xero: JAX AI partner; practice-side products (Xero Cashbook, Xero Ledger, Workpapers); Xero Me employee app; MFA-mandatory login.
- FreshBooks: instant payouts, BNPL, financing; "Bookkeeping" marketed as a separate feature page of the same product.
- QuickBooks: not researched (unreachable).

## Vendor-specific / Rejected Findings

Rejected from the canonical model (with reasons):

- **"Accounting software = invoicing + payments"** — rejected. Invoicing/payments are L1 AR machinery; a GL system without invoicing is still accounting software; FreshBooks' invoicing-first framing is a philosophy, not the Type's structure.
- **"Bank feeds are definitional"** — rejected. Feeds are a modern convenience layer; statement upload and manual entry achieve the same books (Wave supports upload; all products support manual entry). Reconciliation (the control) is L1; the feed (the transport) is L2.
- **"Cloud/web is definitional"** — rejected. Desktop-era and desktop-current products (Sage 50 class, Zoho's Windows app) satisfy the L0. Deployment is L2.
- **"Free pricing is part of the category"** — rejected. Business-model variant only.
- **"Payroll/inventory/projects are part of accounting"** — rejected as Core; they are L1/L2 modules that every sampled vendor ships as add-ons or separate products.
- **"Debits and credits must be user-visible"** — rejected. The invariant is balanced posting, not its visibility; Wave hides it behind categorization yet produces trial balances.

## Boundary Findings

1. **vs General Ledger System (sibling leaf, §08)**: the GL is the L0 engine alone (CoA + journal + ledger + trial balance), typically sold mid-market/enterprise and as an ERP module. Accounting Software = GL core + SMB operational layer (AR/AP/bank/tax surfaces) + owner/bookkeeper-facing UX. Test: strip AR/AP/bank/tax surfaces → a GL system remains; a GL system lacks the SMB money-flow surfaces. Related Types sharing the engine, not duplicates.
2. **vs Bookkeeping Application (sibling leaf, §08)**: probable Alias/Variant. Vendors themselves use the terms interchangeably — Xero's own page says bank feeds import "into Xero bookkeeping software"; Zoho maintains a "Bookkeeping Software" page pointing at Books; FreshBooks ships a "Bookkeeping" feature page inside its accounting product. Bookkeeping names the activity; accounting software names the product category. Flag for joint review when Bookkeeping Application is processed.
3. **vs Invoicing Application (sibling leaf, §08)**: invoicing apps center on customer billing; accounting software centers on the books. Invoicing-first products (FreshBooks) still implement the full books core; standalone invoicing tools lack CoA/statements. Test: remove the ledger → invoicing app remains. Overlap zone: micro-business products where invoicing is the primary daily surface but books exist underneath.
4. **vs ERP (§10)**: ERP embeds finance/accounting as one module among operations (inventory, manufacturing, HR, supply chain) for larger organizations; accounting software is finance-first and SMB-scaled. Test: remove operational modules → accounting software remains. Mid-market products blur the edge (suite creep).
5. **vs Personal Finance Management (§08)**: PFM maintains a person's accounts/budgets; no business CoA, no statements, no sales tax, no AR/AP. The entity container (business vs person) is the wall.
6. **vs Account Reconciliation Platform (§08)**: consistent with the earlier cross-check — bank reconciliation inside accounting software is a per-account feature; the enterprise platform manages a population of account×period reconciliations with certification/sign-off. Capability-inside-broader-Type relationship.
7. **vs Tax Preparation Application (§08)**: books produce tax-ready reports; tax prep produces and files returns. Some vendors bundle both; the objects differ (ledger vs return forms).
8. **vs Expense Management / AP-Automation / AR-Management (§08 siblings)**: point capabilities that accounting software implements in lightweight built-in form; the standalone platforms target mid/enterprise scale and depth (approval chains, OCR, collections automation).

## Uncertainties

- QuickBooks Online structure unverified (unreachable). The four-product sample is consistent, but the US market leader's current module map is unconfirmed; no claim depends on it.
- Xero evidence is Tier 2 only (help center JS-rendered); Xero-specific mechanics (e.g. reconciliation UI details) are not asserted.
- Whether any mainstream SMB product ships **without** a cash-basis option was not verified; cash vs accrual is treated as common (B), not universal.
- Exact plan/edition gating of multi-currency, budgets, approvals etc. varies and was not systematically mapped (L2 territory; not needed for the canonical model).
- Nonprofit fund accounting was not sampled; assumed to fit L0 (CoA + posting + statements) with fund dimensions as L2 — unverified.

## Final Synthesis

Accounting Software is the small-business implementation of the universal bookkeeping structure: **one business entity's books = chart of accounts + balanced posting of every economic event + derived financial statements**. Around that invariant, mature products wrap the SMB money flows — invoicing customers (AR), paying bills (AP), categorizing and reconciling bank activity, tracking sales tax — and expose three user populations: the owner (daily money flows, dashboard, simple categorization), the bookkeeper (categorization, reconciliation, cleanup), and the external accountant (journals, CoA, period locks, reports, tax). The debit/credit engine may be hidden behind friendlier forms (categorize a bank line, send an invoice), but the trial balance, general ledger, and balance sheet it produces are the Type's signature. Everything else — payroll, inventory, projects, multi-currency, portals, AI, regional e-invoicing — is segment/region/plan-dependent structure, not definition.
