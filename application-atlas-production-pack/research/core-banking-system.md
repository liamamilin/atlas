# Research Notes — Core Banking System

Research date: 2026-09-07

## Research Goal

Understand what a Core Banking System actually is as an Application Type: what objects it is built from, who operates it, how money movement and account economics work inside it, what it must contain to be recognized as "the core" of a bank, and where its boundary sits against neighboring financial-infrastructure Types (general ledger systems, banking back-office platforms, banking channels, payment/card processing, loan servicing, accounting software).

## Initial Boundary

Working hypothesis before research:

1. Core banking = the bank's central system of record for customer deposit (and often loan) accounts — the "books" of who owes the bank and whom the bank owes.
2. Likely confusables:
   - General Ledger System (already processed): books of the institution, no customer accounts.
   - Banking Back-office Platform (already processed): staff-facing operations layer (validate→authorize→route→execute) over transactions/instructions.
   - Digital/Mobile/Online Banking and Commercial Banking Platform (processed): customer-facing channels.
   - Payment Processing Platform (processed): merchant/card acquiring rails.
   - Card Processing Platform (processed): issuer-side card scheme connectivity.
   - Loan Management / Commercial Loan Management (processed): loan-book servicing specialists.
   - Accounting Software (processed): business-entity books.
3. Unknowns to resolve by research:
   - Is a payments engine part of the core or a satellite?
   - Is the GL inside the core or external?
   - Is the product/configuration layer definitional or merely common?
   - How do older batch-era cores relate to modern API-first cores — same Type or two Types?

## Research Questions

1. What is the central persistent object — account? contract? customer?
2. What account families does a core carry (current/checking, savings, term deposits, loans, cards, wealth)?
3. How are accounts created — free-form or instantiated from configured products? What does a product define?
4. How does money movement work: posting, available vs ledger balance, holds, reversals, booking vs value date?
5. How does the core connect to the bank's accounting (chart of accounts, journal entries, accounting rules per product)?
6. What periodic/batch machinery exists (interest application, end-of-day, close of business, statements)?
7. What organization/user structure exists (branches, offices, staff, roles, dual control)?
8. What channels and integration surfaces does the core expose (teller, switch/ATM/POS, open APIs, digital channels)?
9. What regulatory machinery is embedded (KYC/customer status, withholding tax, FATCA, limits, audit)?
10. How does the Type vary: universal suite vs composable/ledger-first vs open-source headless; batch vs real-time; segment editions (retail/corporate/community/microfinance/Islamic)?

## Representative Products

Selected for market representativeness, documentation completeness, different product philosophies, and different customer tiers:

| Product | Philosophy / tier | Documentation access |
|---|---|---|
| Oracle FLEXCUBE Universal Banking (14.8) | Universal incumbent core for retail/corporate/investment + Islamic banking; module suite | Public user-guide library on docs.oracle.com (Tier 1, full access) |
| Mambu | Cloud-native SaaS composable core (deposits + lending engine) for challengers and established banks; API-first | Public Documentation Hub + API reference (Tier 1, full access) |
| Apache Fineract | Open-source, headless, cloud-ready core engine; microfinance/digital-financial-services origin | Public system documentation + website (Tier 1, full access) |
| Temenos Core | Market-leading packaged core ("composable core"); 950+ banks claimed; on-prem/cloud/SaaS | Product page only (Tier 2); docs portal login-walled |

Considered and rejected/inaccessible samples:

- **Infosys Finacle** — docs.edgeverve.com unreachable (transport error ×2; also 403 in the earlier banking-back-office pass). Excluded; recorded as limitation.
- **Thought Machine (Vault)** — docs.thoughtmachine.net geo-blocked (403 "Location Not Authorised"). Excluded; recorded as limitation.
- **Fiserv (DNA/Premier/Signature), FIS (Systematics/Horizon/Profile), TCS BaNCS** — operational documentation is client-portal-walled; not fetched. Used nowhere as evidence.

## Sources

### Oracle FLEXCUBE Universal Banking (Tier 1, directly observed)

- Oracle Financial Services Documentation index — https://docs.oracle.com/en/industries/financial-services/ (fetched 2026-09-07)
- Oracle FLEXCUBE library index — https://docs.oracle.com/en/industries/financial-services/flexcube/index.html (fetched 2026-09-07)
- Oracle FLEXCUBE Universal Banking 14.8.0.0.0 Documentation Library (user-guide catalog with per-guide summaries) — http://docs.oracle.com/cd/G27840_01/index.htm (fetched 2026-09-07). Guide titles/summaries directly observed: Core Entities (customer creation, 360° customer view, FATCA), Core Services, CASA — Current and Savings Account (cheque details, amount blocks, stop payment instructions), Term Deposit (incl. Recurring Deposits), Retail Lending, Mortgages, Corporate Deposits, Microfinance, Leasing, Collections, General Ledger (chart of accounts, reporting lines, GL balance transfer, external GL integration), Interest and Charges (data elements, formulas on all balance-type accounts), Interest rules (rules linked to product, applied to contract), Charge and Fees (charge classes, charge rules per product), Products ("concept of 'Product'... create a product and associate various components like charges, fees, tax"), Class (Interest/Charge/Events classes), Settlements (netting payments across modules), Data Entry (teller product + teller operations), Retail Teller, Automated End of Day (BOD/EOD/end-of-cycle routine tasks), Standing Instructions, Switch Interface Gateway (ATM/POS/IVR), Nostro Reconciliation, Messaging System (incoming/outgoing advices), Security Management System (user access roles), Tax, MIS, Dashboard, Islamic suites (profit instead of interest; Mudarabah fund profit distribution), Safe Deposit Locker, Fixed Assets, Machine Learning.

### Mambu (Tier 1, directly observed)

- Mambu Documentation Hub welcome — https://docs.mambu.com/docs/ (fetched 2026-09-07): "core engine of a cloud-based composable banking architecture"; UI + APIs + Ecosystem; guide sections: Managing your Organization, Users and Access Control, Clients and Groups, Loans, Deposits, Credit Arrangements, Cards, Payments, Transactions and Interest, Notifications, Auditing, Accounting, Islamic Banking, Tellers.
- Setting Up New Deposit Products — https://docs.mambu.com/docs/setting-up-new-deposit-products/ (fetched 2026-09-07): deposit product as template for accounts; product types (Current Account with overdrafts, Savings, Fixed Deposit with term/maturity, Savings Plan, Funding Account); product categories; branch availability; interest terms (fixed, index, tiered per balance/period/bands); interest charging frequency; balance basis (min/avg/end-of-day daily balance); interest posting schedule; days-in-year; withholding taxes; recommended deposit/maximum withdrawal; opening balance; term length with early-withdrawal permission; dormancy automation; offset deposits; fees (arbitrary/manual/monthly); accounting rules per product; custom fields.
- Accounting Setup — https://docs.mambu.com/docs/accounting-setup/ (fetched 2026-09-07): enable accounting per product; cash vs accruals methodology; accounting rules per transaction; accounting rates for multicurrency; journal entries; accounting closures; booking date vs value date; inter-branch GL.
- Journal Entries — https://docs.mambu.com/docs/journal-entries/ (fetched 2026-09-07): client transactions auto-logged to GL after products linked; debit/credit validation ("total debit amounts equal to total credit amounts... cannot be saved" otherwise); transaction families generating entries (deposits/withdrawals/transfers/fees/interest/write-offs + reversals; disbursements/repayments/penalties/rescheduling); entry ID vs transaction ID; reversal mechanics (reversal of reversal); manual journal entries; branch dimension; backdating rules.
- Clients and Groups Overview — https://docs.mambu.com/docs/clients-and-groups-overview/ (fetched 2026-09-07): client (individual) vs group (entity/joint) accounts; client/group types; group member roles (CEO, treasurer...); blacklisting on KYC failure or suspicious activity.

### Apache Fineract (Tier 1, directly observed)

- Apache Fineract site — https://fineract.apache.org/ (fetched 2026-09-07): "open source software... designed to create a cloud-ready core banking system"; key features (flexible product configuration, KYC documentation support, four-eyes principles/business rule sets, payment recognitions/repayments system of record, portfolio management); headless open-API design; deployment (cloud/on-prem); history (2006 Grameen Foundation microfinance MIS → Mifos X → Apache incubation 2016).
- Fineract Platform Documentation 1.15.0 — https://fineract.apache.org/docs/current/ (fetched 2026-09-07): functional categories — Infrastructure (codes, extensible data tables, reporting); User Administration (users/roles/permissions); Organisation Modelling (offices, staff, currency); Product Configuration (charges, loan products, deposit products); Client Data (KYC); Portfolio Management (loan accounts, deposit accounts, client/groups); GL Account Management (chart of accounts, general ledger). Channel model (teller, group meetings, online banking, ATM/POS/card network, mobile money, agents) with the platform as "core engine... behind a relatively simple API". Command processing with idempotency and audit; read/write/batch instance types; close-of-business (CoB) batch processing; business-date concept; loan product templates, charges, taxes, accounting entries per feature; savings interest posting.

### Temenos (Tier 2, positioning only)

- Temenos Core Banking product page — https://www.temenos.com/products/core-banking/ (fetched 2026-09-07): "composable and comprehensive core banking"; segment editions (Core for Retail / Business / Corporate & Commercial / Treasury; credit unions & community; Islamic banking; inclusive & community; regionalized solutions); on-premise/cloud/SaaS deployment; "modular core capabilities... product builder tooling"; claims 950 banks in 150+ countries; separate product lines: Core Banking, Digital Banking, Payments, Wealth Management.
- Temenos Documentation Portal — https://docs.temenos.com/ (fetched 2026-09-07): content requires partner/customer login → operational detail NOT observed; no operational claims made from Temenos.

## Product A — Oracle FLEXCUBE Universal Banking

### Key observations (Layer A unless noted)

- Self-positioning: "real-time, online, comprehensive banking solution" for retail, corporate, investment banking, conventional + Islamic.
- **Universal module breadth** around a common core: CASA (current + savings accounts) with cheque details, amount blocks, stop payment instructions; Term Deposits incl. recurring; Corporate Deposits (repayments, rollovers, value-dated changes, deposit lifecycle events); Retail Lending; Mortgages; Microfinance; Leasing; Collections; Asset Management (funds); Safe Deposit Locker; Fixed Assets.
- **Customer as core entity**: "customer creation, 360 degree view of customer information, FATCA customers" — a dedicated Core Entities guide; relationship managers (RM hierarchy) assignable to customers.
- **Product concept is central**: a dedicated "Products" guide — "Explains the concept of 'Product' in Oracle FLEXCUBE and the procedure to create a product and associate various components like charges, fees, tax"; a "Class" guide for mandatory/optional classes (Interest Class, Charge Class, Events Class); Interest guide — create interest rules, link to product, apply to contract; Interest and Charges guide — data elements and formulas "to apply and process Interest and charges on all balance type accounts of the bank".
- **GL inside the core**: General Ledger guide — chart of accounts setup, reporting line structure, alternate reporting structure, transfer GL balances, integrate with an external GL system (both options documented).
- **Batch cycle machinery**: Automated End of Day — "define and automatically trigger everyday routine tasks... during beginning of day, end of cycle, and end of day operations".
- **Branch/teller operations**: Data Entry module (teller product + teller operations), Retail Teller guide, Utility Payments at branch.
- **Channel integration**: Switch Interface Gateway — interface between the core and the bank's switch software for ATM/POS; EMS interface for external systems.
- **Correspondent banking support**: Nostro Reconciliation (define matching rules, upload external statements, match nostro entries).
- **Messaging**: media types, advice formats for incoming/outgoing messages (advices = customer notices/statements).
- **Security**: Security Management System — user access roles, profiles, user activity status.
- **Settlements**: netting payments across modules and money settlements.
- **Islamic banking** as a first-class parallel track: Profit and Charges module (profit formulas instead of interest), Islamic Accounts (Mudarabah profit distribution), Islamic Financing.
- Terminology note (vendor-specific): accounts/deposits/loans are treated as "contracts" with lifecycle events; accounting entries and advices are generated per module and per batch.

## Product B — Mambu

### Key observations (Layer A)

- Self-positioning: "core engine of a cloud-based composable banking architecture"; three interaction surfaces: browser UI, REST APIs, ecosystem connectors.
- **Customer records**: individual client accounts vs group accounts (businesses, joint); client/group types (configurable, e.g. "student", "joint account"); group members with role names; permissions per type; blacklisting where KYC fails or activity suspicious.
- **Product → account instantiation**: "deposit products are flexible and highly-customizable templates for creating individual deposit accounts"; all deposit accounts are associated with deposit products; some attributes overridable at account creation (max withdrawal, min deposit, overdraft limits).
- **Product economics configuration**: interest terms (fixed with rate bounds, index + spread, tiered per balance / per period / per bands); interest rate expression (% per year/month/4-weeks/week/X-days); interest calculation basis (minimum/average/end-of-day daily balance); posting schedule (daily→yearly, fixed dates, on maturity for term products); days-in-year convention; withholding tax on interest with dedicated "Taxes Payable" GL linkage; fees (manual, monthly, arbitrary); deposit/withdrawal constraints; opening balance; term length; automatic dormancy; offset deposits linked to loan interest.
- **Product types** map the deposit family: Current Account (with overdrafts — balance may go negative to a limit), Savings Account, Fixed Deposit (term + maturity + undo maturity), Savings Plan, Funding Account.
- **Accounting**: chart of accounts; accounting enabled per product with cash or accruals methodology; product rules map each transaction type to GL accounts; automatic journal entries per client transaction; strict debits=credits validation; entry ID vs transaction ID cross-reference ("journal entries are also linked to the correspondent client account transaction"); reversals (only manual entries reversible directly; client-transaction entries reversed by reversing the client transaction); backdating with booking-date semantics; booking date vs value date as a documented distinction; multicurrency accounting rates; inter-branch transfer GL account; accounting closures.
- **Portfolio breadth**: deposits, loans (with repayments, interest, penalties, fees, rescheduling, write-offs), credit arrangements (lines of credit), cards (with authorization holds), payments.
- **Organization**: branches and centres; users/roles/permissions; audit trail; tellers module.
- **Islamic banking** as a section (Shariah deposit principles).

## Product C — Apache Fineract

### Key observations (Layer A)

- Self-positioning: "open source software... cloud-ready core banking system"; headless — all capabilities through a practically-RESTful API; mission includes the unbanked/underbanked; lineage as microfinance MIS (Grameen Foundation, 2006) → Mifos X → Apache project. This is the "older/regional/inclusive" pole of the market inside the sample.
- **Functional categories** (from Functional Overview): Infrastructure; User Administration (users, roles, permissions); Organisation Modelling (offices, staff, currency); Product Configuration (charges, loan products, deposit products); Client Data (KYC); Portfolio Management (loan accounts, deposit accounts, client/groups); GL Account Management (chart of accounts, general ledger).
- **Four-eyes principle** and configurable business rule sets as shipped features.
- **Command processing**: every write is a command with idempotency, command audit (persistent command store), hooks — bank-grade attribution.
- **Batch machinery**: batch execution/jobs; read/write/batch instance types; Close of Business (CoB) processing with batch instances; business-date concept (system business date distinct from wall clock).
- **Loan machinery depth** (feature docs): product templates, charges, taxes, backdated interest modification, re-amortization/re-aging, delinquency management, EIR-based income recognition, advanced payment allocation — showing the loan-account engine is part of the core in this family too (inherited from microfinance).
- **Savings interest posting** as a documented process; provisioning (asset-quality) concepts in the platform vocabulary.
- **Channel model**: the docs describe teller, group/center meetings (microfinance), online banking portals, ATM/POS/card networks, mobile money, and agent networks as delivery means over the core.

## Product D — Temenos (positioning only, Layer B/C)

- Core banking sold as "composable core" with segment editions (retail, business, corporate & commercial, treasury) and community/credit-union and Islamic editions; regionalized solutions; deployment on-prem/cloud/SaaS; product-builder tooling; separate Digital Banking and Payments product lines integrate with Core. Marketing claims (950 banks, 150+ countries, "first cloud core banking") recorded as vendor claims, not structural evidence.

## Cross-product Comparison

| Structure | FLEXCUBE | Mambu | Fineract | Verdict |
|---|---|---|---|---|
| Customer/party records (individual + entity; types; KYC) | Core Entities, 360° view, FATCA | Clients & Groups, types, KYC blacklisting | Client Data (KYC) | **L0-adjacent** (accounts presuppose customers; record management itself L1) |
| Customer accounts as balances of record | CASA, Term Deposits, loans, etc. | Deposit + loan accounts | Loan + deposit accounts | **L0** |
| Accounts instantiated from configured products | Products + Classes (interest/charge/event); rules linked to product, applied to contract | Deposit/loan products as templates; attributes overridable at open | Product configuration (loan/deposit products, charges) | **L0** (product-defined account economics) |
| Posting engine changing balances | Transactions per module; settlements netting | Deposits/withdrawals/transfers; transaction IDs | Command processing, idempotent writes | **L0** |
| Double-entry GL convergence | GL guide: CoA, reporting lines, transfer, external-GL option | Auto journal entries per transaction; debits=credits validated; linked to client transaction | Chart of accounts + GL management; accounting entries per feature | **L0** (as the accounting leg of posting; GL may be internal or external) |
| Interest machinery (accrual, tiers, application cycle) | Interest rules; Interest & Charges formulas on all balance-type accounts | Full deposit interest config (terms, tiers, basis, schedule, days-in-year) | Savings interest posting; loan EIR | **L1** (the concrete mechanics vary; the presence of bank economics on accounts is L0 via products) |
| Charges/fees machinery | Charge classes/rules per product | Manual/monthly/arbitrary fees per product | Charges as first-class configuration | **L1** |
| Holds / balance restrictions | Amount blocks, stop payments, cheque details | Overdraft limits; card authorization holds | Limits in product config | **L1** |
| Deposit account families (current/checking, savings, term) | CASA + Term/Corporate deposits + Structured | Current, Savings, Fixed, Savings Plan | Deposit products (savings) | **L1** (families; not each family definitional) |
| Loan/credit accounts inside the core | Retail Lending, Mortgages, Microfinance, Leasing | Loans + Credit Arrangements + overdrafts | Loan accounts (deepest machinery in sample) | **L1** (common; a deposits-only core is still a core) |
| Organization structure (branches/offices, staff) | Branch-centric modules; RM hierarchy | Branches & centres; product availability per branch | Offices, staff | **L1** |
| Users/roles/permissions + dual control | Security Management System | Users & access control | Users/roles/permissions; four-eyes | **L1** |
| Audit trail / attributed commands | User activity status; advices | Audit trail section; entry↔transaction linkage | Command store/audit, idempotency | **L1** |
| Periodic processing (interest application, EOD/CoB, statements/advices) | Automated End of Day (BOD/EOD/end-of-cycle) | Accounting closures; dormancy automation | CoB jobs; batch instance types; business date | **L1** (cycle is universal; batch vs real-time posture is L2) |
| Payments/transfers between accounts; standing instructions | Standing Instructions; Settlements; Utility Payments | Transfers; payments products | Payment recognitions; standing machinery | **L1** |
| Channel integration (teller, switch/ATM/POS, APIs) | Teller modules; Switch Interface Gateway; EMS | Tellers; full REST API suite | Headless API; channel descriptions | **L1** (API surface is the modern standard; teller the historical one) |
| Regulatory touchpoints (tax on interest, FATCA, limits) | Tax guide; FATCA; Local limits | Withholding taxes | KYC | **L1** |
| Islamic banking track | Dedicated profit-based modules | Shariah section | — | **L2** (regional/regulatory variant) |
| Multi-currency | Multi-currency modules | Currencies incl. crypto; accounting rates | Currency config | **L1** (common) / crypto **L2** |
| Real-time vs batch-centric posture | "Real-time, online" claim + AEOD batch | Cloud-native, real-time API | Real-time writes + CoB batch | **L2** (processing posture) |
| Deployment (on-prem monolith / cloud / SaaS) | On-prem heritage + cloud offerings | SaaS multi-tenant | Self-hosted JAR/cloud | **L2** |
| Segment packaging | Universal + microfinance + private banking editions | Challenger/SaaS pole | Microfinance/inclusion pole | **L2** |
| Suite breadth (payments hub, treasury, wealth, cards as modules) | All present as modules | Cards/payments/credit arrangements as modules | — (lean engine) | **L2/L3** |

## Abstraction Hierarchy

### L0 — Defining Invariant

Three structures, all jointly required:

1. **The customer account of record** — a persistent, individually identified account held by the financial institution for a specific customer (person or entity), carrying the institution's own record of the balance owed to or by that customer. Accounts are the center of the system; everything else exists to open, govern, move, and account for them.
2. **The posting engine** — institution-side money movement that changes account balances through posted, attributed transactions, where each posting produces corresponding double-entry accounting entries into the institution's chart of accounts / general ledger (internal or external). Without posting there is no account behavior; without GL convergence there is no bank books integrity.
3. **Product-defined account economics** — accounts are opened under configurable products (account classes) that define their financial behavior — interest accrual and application, charges and fees, terms/maturity, limits, accounting rules — so banking economics apply uniformly across a population of accounts. Remove the product layer → a generic balance table; remove accounts-for-customers → a general ledger system.

L0 is deliberately small: no branch model, no batch cycle, no teller, no payment rails, no lending family, no channel, no deployment posture, no regulatory feature is required by the definition.

### L1 — Common Mature Structure

- Customer records: individual + entity customers, customer types, KYC data, customer status/blacklisting, group/joint relationships, relationship-manager assignment.
- Deposit account families: current/checking, savings, term/fixed deposits (recurring deposits, structured deposits in some products).
- Loan/credit accounts as a second family: retail loans, mortgages, microfinance, overdrafts; delinquency and write-off semantics.
- Interest machinery: accrual conventions, rate structures (fixed/index/tiered), application/posting cycles.
- Charges and fees machinery: rule classes, manual and scheduled fees.
- Balance semantics beyond the raw balance: holds, blocks, overdraft limits, available vs ledger concepts, authorization holds.
- Payments and transfers: internal transfers, standing/recurring instructions, payment products; settlement/netting in larger suites.
- Periodic processing: end-of-day / close-of-business jobs — interest application, dormancy, status updates, statement/notice (advice) generation; accounting closures.
- Chart of accounts and GL layer: CoA management, GL accounts per product/transaction type, accounting reports, bookkeeping corrections (reversals), booking vs value date.
- Organization and access: branches/offices and staff hierarchy; users, roles, permissions, dual control (four-eyes); limits.
- Audit trail: attributed, persistent transaction/journal/command history; idempotent command handling.
- Regulatory touchpoints: withholding tax on interest, tax modules, FATCA-style flags, local limit usage.
- Channel and integration surfaces: teller/cashier stations, switch/ATM/POS interfaces, open APIs for digital channels and fintech integration, external-GL integration, reporting/data delivery.
- Multi-currency support.

### L2 — Variant / Optional Structure

- Processing posture: batch-centric EOD cores vs real-time/always-on API cores (coexists: even "real-time" cores run EOD-style jobs).
- Deployment: on-prem licensed monolith, private cloud, multi-tenant SaaS, self-hosted open source.
- Product-scope packaging: universal suite (deposits + loans + cards + wealth + treasury as modules) vs slim composable core (ledger + products, everything else satellite) vs segment editions (retail, corporate & commercial, community/credit union, microfinance, Islamic).
- Islamic banking as a parallel economics track (profit distribution instead of interest) — regional/regulatory variant present in three sampled vendors.
- Regional/regulatory parameterization (country clusters, localized rails and reports).
- Crypto/digital asset custody as deposit-account content (single product).
- Embedded advanced analytics/ML, dashboards.
- Wealth management, safe deposit, fixed assets, instruments inventory — peripheral modules in some suites.

### L3 — Vendor-specific (research notes only)

- FLEXCUBE: "contract" as the unit for deposits/loans; CASA terminology; mandatory/optional "Classes"; AEOD; Data Entry / Retail Teller module naming; MIS pools; "advices"; cluster releases per region (LATAM/Europe/Vietnam/India/Russia/China/Microfinance clusters).
- Mambu: product categories vs product types split; Savings Plan type; offset deposits; Credit Arrangements; Mambu Process Orchestrator; Configuration as Code; sandbox tenants; Technical Success Packages gating.
- Fineract: read/write/batch instance types; command-handler architecture; CoB terminology; provisioning concepts; share accounts (platform vocabulary); Fineract CN deprecation.
- Temenos: composable-core framing; single code base claims; SaaS operations model.

## Rejected Findings (considered, not promoted)

- **"End-of-day batch processing" as definitional** — rejected: modern cores run continuous real-time posting; batch is a processing posture (L2), and even real-time cores retain EOD-style jobs, so the invariant is the *periodic processing of account economics*, not batch.
- **"Branch/teller operations" as definitional** — rejected: the API-first/headless realization has no teller surface and serves digital channels only; teller is the historical channel (L1).
- **"Payments engine inside the core" as definitional** — rejected: internal transfers are postings (L0 via the account), but external rails/schemes are satellites in all sampled architectures (dedicated Payments product lines at the suite vendor; separate gateways/processors).
- **"Loans are part of the core"** as definitional — rejected: every sampled product carries loan accounts, but the deposit account is the family with no counter-example in the sample, and savings-bank/microfinance deposit-focused deployments fit the Type without a full lending suite; loan accounts are L1 (common family), loan *servicing depth* belongs to lending-specific Types.
- **"Multi-entity / multi-country" as definitional** — rejected: single-entity community banks and single-country challengers are cores.
- **"Real-time API" as definitional** — rejected by the historical check: batch-era cores (and Fineract's 2006-era lineage) satisfy the Type without it.

## Boundary Findings

- **vs General Ledger System (processed)**: the GL system's defining objects are the institution's books (CoA + balanced journals + periods + statements); a core banking system's defining objects are *customer accounts* whose postings converge into books. A core *contains* GL machinery; a GL system contains no customer accounts or product economics. Removal test: remove customer accounts from a core → GL system territory; add customer accounts to a GL → you are building a core.
- **vs Accounting Software / Bookkeeping (processed)**: those are the books of a business entity recording its own economy; a core banking system is the books *of money held for third parties* (customers), with banking economics (interest on deposits, charges, overdrafts) computed by the system. Same double-entry spine, different object of record.
- **vs Banking Back-office Platform (processed)**: the back-office Type is a staff-facing operations layer — tracked instructions validated→authorized→routed→executed, with exception/repair queues; its "execute" step posts to the bank's books (the core) and/or transmits to rails. The core is the system of record being posted into, and computes account economics; the back-office orchestrates operations across systems. Vendors sell adjacent or overlapping products here (see STATUS Boundary Issues note), but the seam is record-and-economics vs operations-and-exception-flow.
- **vs Digital Banking Application / Online Banking Portal / Mobile Banking Application / Commercial Banking Platform (processed)**: those are customer-facing channels through which customers *originate* instructions; the core is institution-side, never customer-facing, and *executes/posts* what channels originate. The channel can be removed and the core stands (teller-era cores; headless cores).
- **vs Payment Processing Platform (processed) / Card Processing Platform (processed)**: those are rail-side (merchant acquiring / issuer scheme connectivity). The core holds the funding accounts whose balances move as a result of rail activity and may screen or route, but scheme message processing, interchange, chargebacks are outside the core. Card modules inside cores manage card-account linkage and authorization holds, not scheme processing.
- **vs Loan Management System / Commercial Loan Management (processed)**: dedicated lending Types center the loan lifecycle (facility-shaped credit positions, covenant/participation machinery, servicing depth). Inside a core, the loan account is one account family among others with standard schedule/interest/delinquency machinery. Lending platforms integrate to cores as servicing engines or satellites; large universal cores embed a servicing-depth subset. Boundary is depth-and-center, not presence.
- **vs Treasury Management System / Liquidity Management (bank side)**: treasury systems manage the bank's own liquidity/positions; the core holds customer accounts and provides the balances/data treasury consumes. (Treasury leaf unprocessed at pass time; seam held directionally.)
- **vs Banking Operations Management (processed)**: management layer over the bank's operations function (visibility, workforce, SLAs) — no accounts, no posting; pure adjacency.
- **vs ERP (processed)**: ERPs integrate a non-bank business's back office on a shared transactional core; banks run ERP for procurement/HR *alongside* the core banking system, which is the banking-specific system of record. Different worlds of record; integration spine, not overlap.

## Historical / Market-Sample Check (per §24 reasoning)

- The sampled set itself spans eras and audiences: a 30-year packaged suite heritage (Temenos), a batch-era universal monolith still marketed real-time (FLEXCUBE), a 2006 microfinance-MIS lineage open-sourced into a cloud core (Fineract), and a SaaS challenger core (Mambu). 
- Older/regional/platform-native cores (branch-teller cores of the 1980s–90s generation, national savings-bank systems, microfinance MIS) carry exactly the L0 triple — customer accounts + posting with bookkeeping convergence + product/account-class economics (interest, charges, terms) — while lacking every modern L1 signature (open APIs, real-time, cloud). The definition therefore does not over-fit the current cloud-native generation.
- Conversely, a modern "ledger-first engine" without product/account economics is not recognizable as a core banking system (it is a ledger component), so L0 cannot shrink further.

## Uncertainties

- Finacle (EdgeVerve) and Thought Machine could not be fetched (transport error / geo-block). Both are canonical market members; their exclusion is compensated by structural coverage from three fully documented products but means the "modern ledger-first" pole (Thought Machine-style contract/ledger semantics) is represented only indirectly through Mambu/Fineract.
- Fiserv/FIS/TCS BaNCS operational docs are client-walled; the US community-bank tier is evidenced only through Temenos's community/credit-union positioning, not through a US-heritage core's documentation.
- Precise EOD job inventories, exact interest conventions, and numeric limits vary per product/implementation and were deliberately not generalized (precision rule). Where stated (e.g., Mambu posting-frequency options, days-in-year 360/365), they are product-documented facts, not Type claims.
- The exact split of accounting ownership between core and an external GL is institution- and product-dependent (FLEXCUBE documents both internal GL and external-GL integration; Mambu documents GL as an internal module); the Type claim is "double-entry convergence exists", not "GL is always internal".

## Final Synthesis

A Core Banking System is the financial institution's own central system of record for customer money: the place where customer accounts live as balances the institution owes or is owed, where every movement of that money is posted as an attributed transaction with matching double-entry bookkeeping, and where the economics of each account — interest, charges, terms, limits — are defined once as configurable products and applied to every account opened under them. Everything else in the bank's estate — channels, payment rails, card processing, lending specialists, treasury, analytics — originates instructions against, reads from, or posts into this system. It is not the customer's surface (channels), not the operations layer (back office), not the rails (payments/card processing), and not the books alone (general ledger): it is the account-and-economics engine those all assume.
